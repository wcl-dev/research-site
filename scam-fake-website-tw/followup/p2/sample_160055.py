#!/usr/bin/env python3
"""P2 — 160055 sampling + full rule-layer.

160055 has 8,574 distinct WEBSITE_NM (45,258 weekly rows). A census-by-hand of
D3 (A/B/U) is not feasible, so D3 is estimated from a random sample of distinct
site names (dual-coded Claude+Codex). D4 IS classified full-coverage by keyword
rule (reliable). This script: draws the n=400 sample, runs the full D4 rule,
runs a D3 brand-match lower bound, prints the dataset shape.
"""
import json, random, re, sys
from collections import Counter
from pathlib import Path

P2 = Path(__file__).parent
sys.path.insert(0, str(P2))
from typosquat_detect import load_brands, detect  # noqa: E402

SRC = ("/Users/wclim/.claude/projects/-Users-wclim-randomfindings/"
       "5e5435ee-308b-4896-aed0-3efcbc618aa4/tool-results/"
       "mcp-twinkle-hub-opendata-query_rows-1779431328222.txt")
SAMPLE_N = 400
SEED = 42


def d4_of(name):
    """Keyword D4 — full-coverage, reliable. Dataset prior = INVEST."""
    n = name.lower()
    if any(k in name for k in ["娛樂城", "博弈", "彩券", "賭", "casino"]) or \
       any(k in n for k in ["casino", "bet", "lottery"]):
        return "GAMBLE"
    if any(k in name for k in ["借貸", "貸款", "信貸", "媒合"]) or \
       any(k in n for k in ["loan", "credit"]):
        return "LOAN"
    if any(k in name for k in ["徵才", "求職", "人力", "招聘"]) or "job" in n:
        return "JOB"
    if any(k in name for k in ["購物", "商城", "拍賣", "賣場", "電商", "mall"]) or \
       any(k in n for k in ["shop", "store", "mall", "mart", "buy", "market"]):
        return "SHOP"
    return "INVEST"   # dataset prior (假投資/博弈 channel)


def main():
    data = json.load(open(SRC, encoding="utf-8"))
    rows = data["rows"]          # [WEBSITE_NM, cnt, urls]
    brands = load_brands(P2 / "brand-reference.csv")
    n = len(rows)
    total_cnt = sum(int(r[1]) for r in rows)
    print(f"=== 160055 shape ===")
    print(f"distinct site names: {n}   total CNT: {total_cnt}")

    # full-coverage D4 (site-count and CNT-weighted)
    d4_site = Counter(); d4_cnt = Counter()
    for nm, cnt, _ in rows:
        d = d4_of(nm)
        d4_site[d] += 1
        d4_cnt[d] += int(cnt)
    print(f"\nD4 (full rule layer, all {n} sites):")
    for d in ("INVEST", "SHOP", "GAMBLE", "LOAN", "JOB"):
        print(f"  {d:8} sites={d4_site[d]:5} ({d4_site[d]/n*100:4.1f}%)   "
              f"CNT={d4_cnt[d]:6} ({d4_cnt[d]/total_cnt*100:4.1f}%)")

    # D3 brand-match lower bound (rule layer only, full coverage)
    bm = 0; bm_cnt = 0
    for nm, cnt, _ in rows:
        # treat the site NAME as if it were a domain string for token matching
        if detect(nm, brands)["flag"] == "A":
            bm += 1; bm_cnt += int(cnt)
    print(f"\nD3 brand-match lower bound (rule layer on site name): "
          f"A>={bm} sites ({bm/n*100:.1f}%), CNT {bm_cnt} ({bm_cnt/total_cnt*100:.1f}%)")
    print("  (lower bound only — name-token match misses brands not in the list)")

    # draw the random sample
    random.seed(SEED)
    sample = random.sample(rows, SAMPLE_N)
    with open(P2 / "sample-160055-400.jsonl", "w", encoding="utf-8") as f:
        for i, (nm, cnt, urls) in enumerate(sample, 1):
            f.write(json.dumps({"idx": i, "name": nm, "cnt": int(cnt),
                                "urls": int(urls), "d4": d4_of(nm)},
                               ensure_ascii=False) + "\n")
    print(f"\nwrote sample-160055-400.jsonl (n={SAMPLE_N}, seed={SEED})")
    samp_cnt = sum(int(r[1]) for r in sample)
    print(f"  sample CNT total: {samp_cnt}  (mean {samp_cnt/SAMPLE_N:.1f})")


if __name__ == "__main__":
    main()
