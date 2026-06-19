#!/usr/bin/env python3
"""Draw the hybrid case-control coding sample + the calibration set.

Decision (brief.md D-1, revised → hybrid case-control, 2026-06-18):
  cases    = ALL crossers (附議 >= 5000)            → 162
  controls = ALL high-traction non-crossers (>=500) + stratified-random tail
Outputs:
  data/sample.jsonl        (gitignored; full text; the main coding input)
  coding/calibration.jsonl (tracked; ~20 boundary cases spanning the 2x2 grid)
  coding/sample_strata.md  (tracked; reproducible strata summary)
Deterministic: random.seed(42).
"""
import json, os, random, re

random.seed(42)
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
CORPUS = os.path.join(DATA, "idea_2020_2024.json")

TAIL_TARGET = 700          # random tail controls (endorse < 500), proportional by year
KEEP = ("publishDate", "網址", "標題", "提議內容", "利益與影響",
        "附議數量", "附議門檻", "關注數量", "留言數量", "提議者", "_year")

# Curated calibration cases — title substrings, one per intended grid cell
CALIB = [
    ("虐童致死", "crossed · form-hi/motive-0 民粹重刑"),
    ("兒少性侵犯公開長相", "near · form-hi/motive-0 民粹重刑"),
    ("優化偏鄉醫療精進", "crossed · form-hi/motive-2 真工具(支持)"),
    ("假偏鄉", "crossed · form-hi/motive-2 真工具(反對)"),
    ("藝文表演票券定型化", "crossed · form-hi/motive-2"),
    ("教學支援工作老師", "crossed · form-hi/motive-2"),
    ("軍公教年終", "crossed · form-lo/動員 自利"),
    ("有前科不得擔任民意代表", "crossed · form-lo/motive-0 道德宣洩"),
    ("童年無價", "crossed · form-lo/motive-0 情緒+媒體時機"),
    ("選舉流程改革法案", "died · form-hi/motive-2 高品質卻石沉"),
    ("中華足協", "died · form-hi/motive-2 小眾石沉"),
    ("幼兒園稽查", "died · form-hi/motive-2 石沉"),
    ("沒有車輛，就沒有傷害", "tail · 純表達/脫離現實"),
    ("規劃狗狗的健保", "tail · form-lo 模糊"),
    ("全國學校午餐升級計畫", "tail · form-hi 卻幾乎零附議(關鍵反例)"),
    ("新竹縣市合併", "tail · essay"),
    ("臺灣自願安樂死", "near · 混合"),
    ("終止校園言語暴力", "near · 混合/情緒"),
    ("強化政府公開招標監督", "tail · form-hi 程序型卻石沉"),
    ("廢除違憲又違法的交通檢舉", "near · form-mid 法律論述/民怨"),
]


def to_int(x):
    try:
        return int(str(x).strip())
    except (TypeError, ValueError):
        return None


def slim(r):
    return {k: r.get(k) for k in KEEP}


def main():
    rows = json.load(open(CORPUS))
    for r in rows:
        r["_e"] = to_int(r.get("附議數量")) or 0
    cases = [r for r in rows if r["_e"] >= 5000]
    high = [r for r in rows if 500 <= r["_e"] < 5000]
    tail_pool = [r for r in rows if r["_e"] < 500]

    # stratified-random tail by year (proportional)
    by_year = {}
    for r in tail_pool:
        by_year.setdefault(r["_year"], []).append(r)
    tail = []
    for y, lst in sorted(by_year.items()):
        k = round(TAIL_TARGET * len(lst) / len(tail_pool))
        tail += random.sample(lst, min(k, len(lst)))

    controls = high + tail
    sample = cases + controls
    for r in sample:
        r["is_case"] = r["_e"] >= 5000
        r["stratum"] = ("case" if r["_e"] >= 5000 else
                        "high_traction" if r["_e"] >= 500 else "tail")

    with open(os.path.join(DATA, "sample.jsonl"), "w") as f:
        for r in sample:
            o = slim(r); o["is_case"] = r["is_case"]; o["stratum"] = r["stratum"]
            f.write(json.dumps(o, ensure_ascii=False) + "\n")

    # calibration set
    calib, used = [], set()
    for sub, note in CALIB:
        for r in rows:
            if sub in (r.get("標題") or "") and r["網址"] not in used:
                o = slim(r); o["_calib_note"] = note
                calib.append(o); used.add(r["網址"]); break
    with open(os.path.join(HERE, "calibration.jsonl"), "w") as f:
        for o in calib:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")

    # strata summary (tracked)
    lines = ["# Sample strata — join-petition-typology-tw", "",
             f"corpus: {len(rows)} | seed=42 | tail_target={TAIL_TARGET}", "",
             f"- cases (附議≥5000): {len(cases)}",
             f"- high_traction controls (500–4999): {len(high)}",
             f"- tail controls (<500, stratified random): {len(tail)}",
             f"- **sample total: {len(sample)}**",
             f"- calibration cases matched: {len(calib)}/{len(CALIB)}", "",
             "tail by year:"]
    for y, lst in sorted(by_year.items()):
        k = round(TAIL_TARGET * len(lst) / len(tail_pool))
        lines.append(f"  - {y}: pool {len(lst)} → sampled {min(k,len(lst))}")
    open(os.path.join(HERE, "sample_strata.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))
    miss = [sub for sub, _ in CALIB if not any(sub in (o.get("標題") or "") for o in calib)]
    if miss:
        print("UNMATCHED calib titles:", miss)


if __name__ == "__main__":
    main()
