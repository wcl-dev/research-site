#!/usr/bin/env python3
"""P3 — aggregate the 6 stratum codings into the flagship 手法×媒介 table.

Reads strata/*.csv (310 victim rows, 6 手法 strata), builds the D4×D1
contingency table, per-stratum D1 distributions (count, %, medium-known %),
and the D6 loss-weighted view. Prints the result; this is the demand-side
core of the study.
"""
import csv, re
from collections import Counter, defaultdict
from pathlib import Path

P3 = Path(__file__).parent
STRATA = [("invest", "假投資"), ("shop", "網購"), ("logistics", "假冒物流"),
          ("cscancel", "解除分期假客服"), ("romance", "假交友"),
          ("impgov", "假冒機構")]
D1_ORDER = ["M1", "M2", "M3", "M4", "M5", "M6", "M0"]
D1_LABEL = {"M1": "獨立假網站", "M2": "真平台假帳號", "M3": "假冒/自建APP",
            "M4": "通訊軟體無網站", "M5": "純電話", "M6": "實體面對面",
            "M0": "判決未述/無法判定"}


def parse_loss(s):
    digits = re.sub(r"[^0-9]", "", s or "")
    return int(digits) if digits else 0


def main():
    rows = []
    for key, label in STRATA:
        f = P3 / "strata" / f"{key}.csv"
        for r in csv.DictReader(open(f, encoding="utf-8")):
            rows.append({"stratum": key, "stratum_zh": label,
                         "D1": (r.get("D1") or "").strip(),
                         "D4": (r.get("D4") or "").strip(),
                         "loss": parse_loss(r.get("D6_loss"))})
    n = len(rows)
    print(f"=== P3 demand-side aggregation — {n} victim rows, "
          f"{len(STRATA)} 手法 strata ===\n")

    # flagship: stratum (手法) × D1 (媒介) contingency table
    print("【旗艦表】手法 × 核心媒介（D1）—— victim 計數")
    hdr = "手法".ljust(10) + "".join(d.rjust(7) for d in D1_ORDER) + "    n"
    print(hdr)
    by_str = defaultdict(Counter)
    for r in rows:
        by_str[r["stratum"]][r["D1"]] += 1
    for key, label in STRATA:
        c = by_str[key]
        tot = sum(c.values())
        line = label.ljust(10) + "".join(str(c[d]).rjust(7) for d in D1_ORDER)
        print(line + f"  {tot:4}")
    allc = Counter(r["D1"] for r in rows)
    print("─" * 62)
    print("合計".ljust(10) + "".join(str(allc[d]).rjust(7) for d in D1_ORDER)
          + f"  {n:4}")

    # per-stratum D1 row-% and medium-known %
    print("\n【各手法 D1 分布】row% / 排除 M0 後的 medium-known%")
    for key, label in STRATA:
        c = by_str[key]
        tot = sum(c.values())
        known = tot - c["M0"]
        print(f"\n  {label}（n={tot}，其中判決有述媒介 {known}）")
        for d in D1_ORDER:
            if c[d] == 0:
                continue
            rowpct = c[d] / tot * 100
            kp = f"，known {c[d]/known*100:.0f}%" if known and d != "M0" else ""
            print(f"    {d} {D1_LABEL[d]}: {c[d]} （{rowpct:.0f}%{kp}）")

    # overall pooled (with caveat)
    print("\n【整體 pooled D1 分布】（⚠ 此為分層樣本 pooled，各手法 n 接近均等、"
          "非依真實盛行率加權；不可當母體估計，僅供觀察）")
    known_all = n - allc["M0"]
    for d in D1_ORDER:
        kp = (f"，known {allc[d]/known_all*100:.1f}%"
              if d != "M0" else "")
        print(f"  {d} {D1_LABEL[d]}: {allc[d]} （pooled {allc[d]/n*100:.1f}%{kp}）")

    # D6 loss-weighted
    print("\n【財損加權 D1 分布】（依各 victim 的 NT$ 財損加權；缺額者不計入）")
    loss_by_d1 = Counter()
    for r in rows:
        loss_by_d1[r["D1"]] += r["loss"]
    tot_loss = sum(loss_by_d1.values())
    print(f"  有財損數字的總額：NT${tot_loss:,}")
    for d in D1_ORDER:
        if loss_by_d1[d]:
            print(f"  {d} {D1_LABEL[d]}: NT${loss_by_d1[d]:,} "
                  f"（{loss_by_d1[d]/tot_loss*100:.1f}%）")

    # the headline framings
    print("\n【「假網站」口徑】")
    m1 = allc["M1"]
    m1m3 = allc["M1"] + allc["M3"]
    print(f"  狹義（M1 獨立假網站）：{m1}/{n} = {m1/n*100:.1f}% pooled "
          f"／ medium-known {m1/known_all*100:.1f}%")
    print(f"  含假冒/自建APP（M1+M3）：{m1m3}/{n} = {m1m3/n*100:.1f}% pooled "
          f"／ medium-known {m1m3/known_all*100:.1f}%")
    print(f"  M0（判決未述媒介）：{allc['M0']}/{n} = {allc['M0']/n*100:.1f}% "
          f"—— M1 為下界，部分 M0 可能是未記錄的 M1")


if __name__ == "__main__":
    main()
