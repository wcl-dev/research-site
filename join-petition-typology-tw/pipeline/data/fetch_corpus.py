#!/usr/bin/env python3
"""Fetch the full Join 提點子 corpus (行政院版本, 2020–2024) from the official
open-data endpoint and compute the crossing (成案) base rate.

Source: join.gov.tw toOpenData v2 — the same feed behind data.gov.tw dataset 58036.
Use the RAW JSON (not the normalised CSV): the CSV has column-misalignment on rows
whose free-text contains commas/newlines; the raw JSON 附議數量 is clean.

Reproducible: re-run to regenerate raw/ + idea_2020_2024.json + crossers.json.
Heavy files are gitignored; crossers.json (small) is kept as a tracked artifact.
"""
import json, os, sys, urllib.request

YEARS = range(2020, 2025)
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
URL = "https://join.gov.tw/toOpenData/v2/ey/idea?year={year}"


def to_int(x):
    try:
        return int(str(x).strip())
    except (TypeError, ValueError):
        return None


def fetch():
    os.makedirs(RAW, exist_ok=True)
    rows = []
    for y in YEARS:
        path = os.path.join(RAW, f"idea_{y}.json")
        if not os.path.exists(path):
            with urllib.request.urlopen(URL.format(year=y), timeout=90) as r:
                open(path, "wb").write(r.read())
        d = json.load(open(path))
        for rec in d:
            rec["_year"] = str(y)
        rows += d
        print(f"  {y}: {len(d)} rows", file=sys.stderr)
    return rows


def main():
    rows = fetch()
    crossers = [r for r in rows if (v := to_int(r.get("附議數量"))) is not None and v >= 5000]
    json.dump(rows, open(os.path.join(HERE, "idea_2020_2024.json"), "w"), ensure_ascii=False)
    json.dump(
        [{k: r.get(k) for k in ("publishDate", "網址", "標題", "附議數量", "提議者", "_year")} for r in crossers],
        open(os.path.join(HERE, "crossers.json"), "w"), ensure_ascii=False, indent=1,
    )
    n = len(rows)
    print(f"TOTAL {n} | 成案≥5000: {len(crossers)} ({100*len(crossers)/n:.2f}%)")


if __name__ == "__main__":
    main()
