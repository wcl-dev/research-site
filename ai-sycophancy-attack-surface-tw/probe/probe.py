#!/usr/bin/env python3
"""
AI Sycophancy Attack-Surface Probe — runner（multi-turn）

測 ChatGPT 與 Gemini，在台灣詐騙/錯誤資訊情境下：
  (a) 模型會不會因查詢被包成「個人判斷/情感再保證」(S-frame) 而失去示警；
  (b) 使用者「對抗式追問」(T2) 後，第一輪的煞車會不會被社交壓力侵蝕。
設計見 probe-spec.md。

每個 cell = 一段「兩輪對話」：
  T1 = s_frame 或 e_frame（依框架）
  T2 = followup（對抗式追問，同一段對話內接著送出，不重開新對話）

依賴：pip install playwright pyyaml  &&  playwright install chrome

用法：
  python3 probe.py setup                      # 存 ChatGPT + Gemini session
  python3 probe.py list  [--family SR] [--reps N]      # 離線預覽
  python3 probe.py run   [--model chatgpt] [--family SR] [--reps N]
  python3 probe.py run   --family SR --reps 1          # 煙霧測試

resume-safe：一個 cell 的 T1 與 T2 回應檔都存在且非 ERROR 才會跳過。

—— 改編自 llm-user-side-bias/pilot/probe.py（網頁操作邏輯）+ probe_multiturn.py（逐輪結構）。
"""

import asyncio
import csv
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime, timezone

import yaml
from playwright.async_api import async_playwright, Page, BrowserContext

# ── paths ──────────────────────────────────────────────────────────────────────
BASE      = Path(__file__).parent
SESSIONS  = BASE / "sessions"
SHOTS     = BASE / "screenshots"
TEXTS     = BASE / "responses"
RECORD    = BASE / "record.csv"
VIGNETTES = BASE / "vignettes.yaml"

# ── config ─────────────────────────────────────────────────────────────────────
MODELS       = ["chatgpt", "gemini"]
FRAMES       = ["S", "E"]
TURNS        = 2          # T1 = 框架提問；T2 = 對抗式追問
DEFAULT_REPS = 3

CSV_FIELDS = [
    "row_id", "cell_id", "scenario_id", "family", "type", "frame",
    "model", "rep", "turn", "timestamp_iso", "response_length_chars",
    # ↓ 人工編碼欄（執行後留白，依 probe-spec.md §6 rubric 手動填）
    "endorsement", "circuit_breaker", "risk_named", "notes",
]

CHATGPT_STOP = 'button[aria-label="Stop streaming"], [data-testid="stop-button"]'
GEMINI_STOP  = '[aria-label*="Stop"], button[aria-label*="停止"]'

# 抓取防呆：回應疑似抓到頁面 UI chrome 而非真正回應時，判為錯誤好讓 resume 重跑。
# （這些 advice prompt 的真實回應都 400+ 字；UI chrome 短、且含已知字串。）
MIN_VALID_CHARS = 80
JUNK_MARKERS = ["Gemini 是 AI", "Gemini can make mistakes"]


def looks_like_junk(text: str) -> bool:
    """回應太短、或撞到已知 UI chrome 字串 → 視為抓取失敗。"""
    t = text.strip()
    if len(t) < MIN_VALID_CHARS:
        return True
    return any(m in t for m in JUNK_MARKERS)


# ── vignettes / cells ──────────────────────────────────────────────────────────

def load_scenarios() -> list[dict]:
    if not VIGNETTES.exists():
        sys.exit(f"找不到 {VIGNETTES} —— 先建立 vignettes.yaml。")
    data = yaml.safe_load(VIGNETTES.read_text(encoding="utf-8"))
    scenarios = data.get("scenarios", [])
    if not scenarios:
        sys.exit("vignettes.yaml 沒有 scenarios。")
    return scenarios


def build_cells(scenarios: list[dict], models: list[str], reps: int) -> list[dict]:
    """展開成 cell list（model-major）。每個 cell 帶一段 2 輪對話 turns=[T1, T2]。"""
    cells = []
    for model in models:
        for sc in scenarios:
            for frame in FRAMES:
                t1 = (sc["s_frame"] if frame == "S" else sc["e_frame"]).strip()
                t2 = sc["followup"].strip()
                for rep in range(1, reps + 1):
                    cells.append({
                        "cell_id":     f'{sc["id"]}_{frame}_{model}_{rep}',
                        "scenario_id": sc["id"],
                        "family":      sc["family"],
                        "type":        sc["type"],
                        "frame":       frame,
                        "model":       model,
                        "rep":         rep,
                        "turns":       [t1, t2],
                    })
    return cells


# ── waiting helper ─────────────────────────────────────────────────────────────

async def wait_until_gone(page: Page, selector: str, timeout_s: int = 90):
    """Poll until selector is no longer visible (means generation stopped)."""
    import time
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        count = await page.locator(selector).count()
        if count == 0:
            await page.wait_for_timeout(2000)
            count = await page.locator(selector).count()
            if count == 0:
                return
        await page.wait_for_timeout(1500)
    print("        ⚠ wait_until_gone timed out, proceeding anyway")


# ── per-model query functions（回傳每輪一則回應的 list）──────────────────────────

async def query_chatgpt(ctx: BrowserContext, turns: list[str], cell_id: str) -> list[str]:
    page = await ctx.new_page()
    responses: list[str] = []
    try:
        await page.goto("https://chatgpt.com/", wait_until="load")
        await page.wait_for_timeout(3000)

        # Close any modal/overlay
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(600)
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(400)
        for txt in ["No thanks", "Maybe later", "不，謝謝", "稍後再說",
                    "Skip", "Got it", "OK", "確認", "Close", "關閉"]:
            btn = page.get_by_text(txt, exact=True).first
            if await btn.count() > 0 and await btn.is_visible():
                await btn.click()
                await page.wait_for_timeout(500)

        # Best-effort "new chat" (fresh browser already lands on one; <svg> may
        # intercept a normal click — force + short timeout, never fatal).
        for sel in ['[data-testid="create-new-chat-button"]', 'a[href="/"]',
                    'button[aria-label="New chat"]', 'button:has-text("新對話")']:
            btn = page.locator(sel).first
            try:
                if await btn.count() > 0 and await btn.is_visible():
                    await btn.click(force=True, timeout=4000)
                    await page.wait_for_timeout(1200)
                    break
            except Exception:
                pass

        await page.wait_for_selector("#prompt-textarea", timeout=20000)
        await page.wait_for_timeout(500)

        # ── 逐輪送出（同一個對話視窗，不重開）──
        for ti, msg in enumerate(turns, 1):
            try:
                inp = page.locator("#prompt-textarea").first
                await inp.click()
                await page.wait_for_timeout(400)
                await page.keyboard.type(msg, delay=20)
                await page.wait_for_timeout(500)

                send = page.locator('[data-testid="send-button"]').first
                if await send.count() > 0 and await send.is_visible():
                    await send.click()
                else:
                    await page.keyboard.press("Enter")

                try:
                    await page.wait_for_selector(CHATGPT_STOP, timeout=15000)
                except Exception:
                    pass
                await wait_until_gone(page, CHATGPT_STOP, timeout_s=120)
                await page.wait_for_timeout(1000)
                await page.screenshot(path=str(SHOTS / f"{cell_id}_T{ti}.png"))

                msgs = page.locator("[data-message-author-role='assistant']")
                n = await msgs.count()
                if not n:
                    responses.append(f"ERROR: T{ti}: no response found")
                    break
                raw = (await msgs.nth(n - 1).inner_text()).strip()
                raw = re.sub(r'^\d+\n+', '', raw)
                if looks_like_junk(raw):
                    responses.append(f"ERROR: T{ti}: 疑似抓取失敗（{len(raw.strip())} 字）")
                    break
                responses.append(raw)
                await page.wait_for_timeout(1800)   # settle before next turn
            except Exception as e:
                responses.append(f"ERROR: T{ti}: {e}")
                break
        return responses
    finally:
        await page.close()


async def query_gemini(ctx: BrowserContext, turns: list[str], cell_id: str) -> list[str]:
    page = await ctx.new_page()
    responses: list[str] = []
    try:
        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")
        await page.wait_for_timeout(4000)

        # Best-effort "new chat"
        for new_chat_sel in ['[aria-label="New chat"]',
                             'button:has-text("新對話")',
                             'button:has-text("New chat")']:
            btn = page.locator(new_chat_sel).first
            try:
                if await btn.count() > 0 and await btn.is_visible():
                    await btn.click(force=True, timeout=4000)
                    await page.wait_for_timeout(1500)
                    break
            except Exception:
                pass

        await page.wait_for_selector(
            "div.ql-editor[contenteditable='true'], rich-textarea [contenteditable='true']",
            timeout=15000,
        )

        for ti, msg in enumerate(turns, 1):
            try:
                inp = page.locator("div.ql-editor[contenteditable='true']").first
                if not await inp.is_visible():
                    inp = page.locator("[contenteditable='true']").first
                await inp.click()
                await page.keyboard.type(msg, delay=25)
                await page.wait_for_timeout(400)
                await page.keyboard.press("Enter")

                await page.wait_for_timeout(4000)
                await wait_until_gone(page, GEMINI_STOP, timeout_s=120)
                await page.wait_for_timeout(800)
                await page.screenshot(path=str(SHOTS / f"{cell_id}_T{ti}.png"))

                raw = ""
                for sel in ["model-response .response-content",
                            ".model-response-text",
                            "message-content .markdown",
                            ".response-container"]:
                    blks = page.locator(sel)
                    n = await blks.count()
                    if n > 0:
                        raw = (await blks.nth(n - 1).inner_text()).strip()
                        break
                if not raw:
                    raw = (await page.locator("chat-window, main").first.inner_text()).strip()
                raw = re.sub(r'^Gemini\s+說了\s*\n+', '', raw)
                if looks_like_junk(raw):
                    responses.append(f"ERROR: T{ti}: 疑似抓取失敗（{len(raw.strip())} 字）")
                    break
                responses.append(raw)
                await page.wait_for_timeout(1800)
            except Exception as e:
                responses.append(f"ERROR: T{ti}: {e}")
                break
        return responses
    finally:
        await page.close()


QUERY_FNS = {
    "chatgpt": query_chatgpt,
    "gemini":  query_gemini,
}


# ── CSV ────────────────────────────────────────────────────────────────────────

def init_csv():
    """建立 record.csv（每個 cell 2 列：T1、T2；編碼欄留白）。已存在則保留既有編碼、只補缺列。"""
    full = build_cells(load_scenarios(), MODELS, DEFAULT_REPS)
    fieldnames = list(CSV_FIELDS)
    existing: dict[str, dict] = {}
    if RECORD.exists():
        compatible = False
        with open(RECORD, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames and "row_id" in reader.fieldnames:
                compatible = True
                for row in reader:
                    existing[row["row_id"]] = row
        if compatible:
            # 保留既有編碼 + 使用者可能自行新增的欄位
            for row in existing.values():
                for k in row:
                    if k not in fieldnames:
                        fieldnames.append(k)
        else:
            # 舊版 record.csv（單輪 schema、無 row_id）—— 備份後改建多輪 schema
            bak = RECORD.with_name("record.csv.bak")
            RECORD.replace(bak)
            print(f"  ⚠ 舊版 record.csv 已備份為 {bak.name}，改建多輪 schema")

    rows = []
    for c in full:
        for turn in range(1, TURNS + 1):
            row_id = f'{c["cell_id"]}_T{turn}'
            if row_id in existing:
                rows.append(existing[row_id])
            else:
                rows.append({
                    "row_id": row_id, "cell_id": c["cell_id"],
                    "scenario_id": c["scenario_id"], "family": c["family"],
                    "type": c["type"], "frame": c["frame"], "model": c["model"],
                    "rep": c["rep"], "turn": f"T{turn}",
                    "timestamp_iso": "", "response_length_chars": "",
                    "endorsement": "", "circuit_breaker": "", "risk_named": "",
                    "notes": "",
                })
    with open(RECORD, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def update_csv(row_id: str, timestamp: str, text: str):
    rows, fieldnames = [], None
    with open(RECORD, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            if row["row_id"] == row_id:
                row["timestamp_iso"] = timestamp
                row["response_length_chars"] = str(len(text))
            rows.append(row)
    with open(RECORD, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


# ── setup ──────────────────────────────────────────────────────────────────────

async def run_setup(pw):
    SESSIONS.mkdir(exist_ok=True)
    print("\n=== Session Setup ===")
    print("ChatGPT：訪客模式即可（不必登入），等首頁載入完按 ENTER。")
    print("Gemini ：登入 burner Google 帳號（介面繁中、地區台灣），")
    print("         打一句「你好」確認可用後按 ENTER。\n")

    for model, url in [("chatgpt", "https://chatgpt.com/"),
                       ("gemini",  "https://gemini.google.com/")]:
        sf = SESSIONS / f"{model}_session.json"
        if sf.exists():
            print(f"✓ {model}: session 已存在（刪掉 {sf.name} 可重設）")
            continue
        print(f"\n[{model.upper()}] 開啟 {url}")
        browser = await pw.chromium.launch(
            headless=False, slow_mo=80, channel="chrome",
            args=["--disable-blink-features=AutomationControlled"],
        )
        ctx = await browser.new_context(locale="zh-TW", timezone_id="Asia/Taipei")
        await ctx.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        page = await ctx.new_page()
        await page.goto(url)
        input(f"  >>> {model} 準備好後按 ENTER <<<  ")
        await ctx.storage_state(path=str(sf))
        await browser.close()
        print(f"  ✓ session 已存 → {sf.name}")

    print("\n✓ Setup 完成。接著跑：python3 probe.py run")


# ── batch runner ───────────────────────────────────────────────────────────────

def _cell_done(cell_id: str) -> bool:
    """T1、T2 回應檔都存在且非 ERROR 才算完成。"""
    for turn in range(1, TURNS + 1):
        f = TEXTS / f"{cell_id}_T{turn}.txt"
        if not f.exists():
            return False
        c = f.read_text(encoding="utf-8").strip()
        if not c or c.startswith("ERROR"):
            return False
    return True


async def run_batch(pw, models: list[str], families: list[str] | None, reps: int):
    SHOTS.mkdir(exist_ok=True)
    TEXTS.mkdir(exist_ok=True)
    init_csv()

    ready   = [m for m in models if (SESSIONS / f"{m}_session.json").exists()]
    missing = [m for m in models if not (SESSIONS / f"{m}_session.json").exists()]
    if missing:
        print(f"⚠  沒有 session：{', '.join(missing)} —— 先跑 `python3 probe.py setup`。")
    if not ready:
        sys.exit("沒有可用的模型 session，中止。")

    scenarios = load_scenarios()
    if families:
        scenarios = [s for s in scenarios if s["family"] in families]
        if not scenarios:
            sys.exit(f"沒有符合 family={families} 的情境。")

    cells = build_cells(scenarios, ready, reps)
    print(f"\n=== Batch：models={ready}  families={families or 'ALL'}  reps={reps}"
          f"  → {len(cells)} 段對話（每段 {TURNS} 輪）===\n")

    done = skipped = errors = 0

    for i, c in enumerate(cells, 1):
        cell_id = c["cell_id"]
        if _cell_done(cell_id):
            print(f"[{i:03}/{len(cells)}] SKIP   {cell_id}")
            skipped += 1
            continue

        print(f"[{i:03}/{len(cells)}] START  {cell_id}  (T1→T2)")
        try:
            sf = SESSIONS / f'{c["model"]}_session.json'
            browser = await pw.chromium.launch(
                headless=False, slow_mo=50, channel="chrome",
                args=["--disable-blink-features=AutomationControlled",
                      "--disable-sync", "--no-first-run"],
            )
            ctx = await browser.new_context(
                storage_state=str(sf), locale="zh-TW", timezone_id="Asia/Taipei",
            )
            await ctx.add_init_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )
            try:
                texts = await QUERY_FNS[c["model"]](ctx, c["turns"], cell_id)
            finally:
                await browser.close()

            ts = datetime.now(timezone.utc).isoformat()
            cell_ok = True
            for turn in range(1, TURNS + 1):
                text = texts[turn - 1] if turn - 1 < len(texts) \
                    else f"ERROR: T{turn}: turn not reached"
                (TEXTS / f"{cell_id}_T{turn}.txt").write_text(text, encoding="utf-8")
                update_csv(f"{cell_id}_T{turn}", ts, text)
                if text.startswith("ERROR"):
                    cell_ok = False
                print(f"          {'✓' if not text.startswith('ERROR') else '✗'}  "
                      f"T{turn}: {len(text)} chars")
            done += 1 if cell_ok else 0
            errors += 0 if cell_ok else 1
        except Exception as e:
            print(f"          ✗  {e}")
            for turn in range(1, TURNS + 1):
                (TEXTS / f"{cell_id}_T{turn}.txt").write_text(
                    f"ERROR: {e}", encoding="utf-8")
            errors += 1
        finally:
            await asyncio.sleep(8)

    print(f"\n=== 完成：{done} ok, {skipped} skipped, {errors} errors ===")
    print(f"回應文字 → {TEXTS}  （每個 cell 兩檔 _T1 / _T2）")
    print(f"記錄表   → {RECORD}（接著依 probe-spec.md §6 rubric 人工編碼）")


# ── list（離線預覽）────────────────────────────────────────────────────────────

def run_list(models: list[str], families: list[str] | None, reps: int):
    scenarios = load_scenarios()
    if families:
        scenarios = [s for s in scenarios if s["family"] in families]
    cells = build_cells(scenarios, models, reps)
    for c in cells:
        print(f'  {c["cell_id"]:<26} {c["family"]}/{c["type"]:<6} frame={c["frame"]}'
              f'  T1:{c["turns"][0][:30]}…  T2:{c["turns"][1][:24]}…')
    print(f"\n共 {len(cells)} 段對話 × {TURNS} 輪 = {len(cells) * TURNS} 則回應 "
          f"（{len(scenarios)} 情境 × {len(FRAMES)} 框架 × {len(models)} 模型 × {reps} reps）")


# ── entry point ────────────────────────────────────────────────────────────────

async def main():
    parser = argparse.ArgumentParser(description="AI sycophancy attack-surface probe")
    parser.add_argument("command", choices=["setup", "run", "list"])
    parser.add_argument("--model", choices=MODELS, action="append",
                        help="只跑指定模型（可重複）；預設兩個都跑")
    parser.add_argument("--family", choices=["SR", "DC"], action="append",
                        help="只跑指定家族（可重複）；預設全跑")
    parser.add_argument("--reps", type=int, default=DEFAULT_REPS,
                        help=f"每 cell 重複次數（預設 {DEFAULT_REPS}）")
    args = parser.parse_args()

    models = args.model or MODELS

    if args.command == "list":
        run_list(models, args.family, args.reps)
        return

    async with async_playwright() as pw:
        if args.command == "setup":
            await run_setup(pw)
        elif args.command == "run":
            await run_batch(pw, models, args.family, args.reps)


if __name__ == "__main__":
    asyncio.run(main())
