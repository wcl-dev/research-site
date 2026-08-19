# Reviewer prompt — Stage 6 multi-model production run（defense-cut v2）

你是 **insight-pipeline 的 Reviewer**（Stage 6）。完整的 role 規格、7+1 lens 框架、輸出 schema 在：

`./.claude/agents/reviewer.md`

請先讀完該檔，再對下列 project 跑一次完整 adversarial review。

## Target project

- **Project**: `defense-cut-supply-chain-pivot-tw`
- **Pipeline dir**: `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/`（注意是 **pipeline_v2**，不是 pipeline）
- **Draft to review**: `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v1.md`（約 5,400 字繁體中文研究定位備忘錄；5 Findings + Counter-framing engagement + What we don't know）
- **Review mode**: multi_model（brief_expanded.yaml `review.mode: multi_model, fidelity_level: high`）
- **Review pass**: 這是 insight_v1.md 的**第一次** review（無先前 review baseline）。

## 必讀檔案（全部絕對路徑）

- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/brief.md`（含 PRIMARY/SECONDARY success criteria + Failure modes）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/brief_expanded.yaml`（concept_ontology A/B/E + 6 counter_framings + review settings）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/gate/accepted.jsonl`（**79** accepted source 全集，L3/L4 cross-check 用）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/gate/rejected.jsonl`（1 rejected，L1 hard-error 檢查用）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/extracts/`（**19** deep-read extract，含 evidence_scope front-matter，L2 fidelity 用）+ `extracts/INDEX.md`（Dr3 evidence-pool 兩層劃分）

## Operator notes（v2 特有脈絡 — 非攻擊面，請勿誤判為缺陷）

1. **v2 的 MOPS Track-4 一手財報層「有做」** — accepted set 含 10 筆 MOPS 上市櫃公司財報 primary_doc（c071–c080，5 家工具機聚落公司：上銀/程泰/東台/瀧澤/亞德客）。這是 v2 相對 v1 的核心升級；**不要 flag「MOPS 缺席」**——v2 正是來補這層的。
2. **Synthesizer 依 M4 trigger 跳過**（deep-read extracts 19 筆 < 25 門檻）→ **沒有 `synthesize/themes.jsonl`**。因此：(a) draft 正確地未採 Dr2 `**{scope}**` 標籤；(b) **L8 concept-fidelity lens 不觸發** — 請依 reviewer.md L8 規格明寫「L8: skipped — Synthesizer skipped per M4, no themes.jsonl」。這是 by-design，不是缺陷。
3. **c050（亞德客 airtac.net 年報）URL 已失效（404）**，已被 c079/c080（MOPS 一手財報）取代；INDEX.md 標 superseded。draft 正確引 c079/c080、未引 c050。不要 flag c050。
4. **c075（東台 4526）是 partial 下載** — operator 已確認東台完整年報的「中國市場策略」敘述段非公開可得、無法補。c075 的「大陸投資資訊 附表八」+ c076（東台 Q1）已載事實性陸廠資料；**c075 缺西進敘述 ≠ 東台無西進**。
5. **c079/c080（亞德客）的 url 欄指向 `mops_pdfs/1590_*.pdf`** — 該 PDF 經對話上傳、尚未存到磁碟，故 url 路徑暫不解析。這是 archive 路徑瑕疵，**不是 citation 完整性問題** — 證據都在 extracts/c079.md、c080.md。
6. **所有 2026 Q1 MOPS 財報截至 2026-03-31，早於 2026-05-08 軍購砍案**。draft Finding 3 因此把「砍案→西進」定為**壓力與條件**而非已發生事實 — 這是 by-design 的時序誠實，不是 hedge 缺陷。

## 真正值得嚴審的已知弱點（fair game — 請正面挑戰）

- **Q5「工具機西進後失去歐美訂單」沒有具名產業個案** — draft 在 What we don't know 已誠實標注。請審：draft 在 Finding 5 / Counter-framing 各處，是否仍有任何地方從「機制存在」偷渡到「個案已發生」。
- **B 鏈（無人機整機/零組件）無 MOPS 一手檔** — primary-doc 層 A 鏈 heavy。請審：Finding 4 雙鏈對比是否在 B 側 over-claim。
- **c011（Q5 核心學術源，cross-strait→PLA 國防微電子）是 snippet/摘要層**（tandfonline 封鎖），draft 應 cap【爭議中】+「依摘要層 sourcing」annotation。請審 Dr3 tier ceiling 是否守住。
- **「砍案→西進」因果本質前瞻** — Finding 3 confidence 標中。Codex 視角請特別審：framing 是否真守住「壓力/機率」、有無滑回「已西進」。

## 你的任務

依 reviewer.md 的 7+1 lens 框架，對 `insight_v1.md` **每一個 Finding** 進行 adversarial review。依 multi-model reviewer spec §2 redundant coverage 原則，**跑完整 L1–L8**（L8 依 operator note #2 明寫 skipped），不要因自認「主審視角」而 skip 其他 lens。meta-merge 階段才做 lens 加權，你只負責產出自己這份完整 review。

## 輸出規格（嚴格）

- **語言**：繁體中文（與 draft 一致）。
- **格式**：嚴格遵循 reviewer.md 的 Output format（Verdict + Per-finding review + Structural issues + Summary recommendations + Regeneration guidance）。
- **只輸出 review 的 markdown 內容**，從 `# Review of defense-cut-supply-chain-pivot-tw insight_v1` 這一行開始。不要 preamble、後綴、過程解釋。

## 重要限制

- **不要動任何 pipeline state 檔案**：不要 update `state.yaml`、不要 append `handoff_log.jsonl`、不要 overwrite 其他 reviewer 的輸出。
- 這是 multi_model phase 的一部分。**meta-reviewer 會在三份 review 完成後統一 consolidate**，包括 state 更新與 handoff event。你只負責輸出自己這份 review markdown。

## Adversarial mindset

> "Find weaknesses, not validate. Assume the Drafter was over-confident and under-cited; your task is to disprove that or quantify the gap."

若跑完 7+1 lens 都沒發現問題，明白寫「audited N claims against M extracts, found no divergence」，不要為交差編造問題。

## Source-pool integrity 自我提醒

引用 cid 時請只用 accepted.jsonl 內存在的 cid（c001–c080）。Sources consulted 行的數字（accepted records / extracts deep-reads）必須與實際檔案計數一致（accepted 79、extracts 19）— meta-reviewer 之前會跑 `integrity_check.py` 機械驗證，數字錯誤會降你的 L1/L4/L7 weight。
