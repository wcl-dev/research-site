#!/usr/bin/env python3
"""P2 — full classification of dataset 176455 (165 遭停止解析涉詐網站).

176455 has 48,575 rows (民國年月, 網域, 網站性質) with no description column.
Per codebook v1.2: dedup to registrable domain, run the typosquat detector
(D3 = A vs non-A; A is a LOWER BOUND), take D4 from the 網站性質 industry tag.

Reads the query_rows JSON dump (path passed as argv[1]); writes
coded-176455.csv; prints aggregates.
"""
import json, csv, sys, re
from collections import Counter
from pathlib import Path

P2 = Path(__file__).parent
sys.path.insert(0, str(P2))
from typosquat_detect import load_brands, detect, parse_domain  # noqa: E402

TLDS_2 = {"com.tw", "gov.tw", "org.tw", "net.tw", "edu.tw", "co.uk"}

# 網站性質 -> D4
PROP_D4 = {
    "金融保險": "INVEST", "電子商務": "SHOP", "運輸倉儲": "SHOP",
    "資訊服務": "UNK", "政府機構與國營事業": "IMPGOV", "釣魚網站": "UNK",
}


def registrable(domain):
    """Return the registrable domain, e.g. agile.hosting1023.shop -> hosting1023.shop"""
    d = re.sub(r"^[^a-z0-9]+", "", domain.strip().lower())
    labels = [l for l in d.split(".") if l]
    if len(labels) >= 3 and ".".join(labels[-2:]) in TLDS_2:
        return ".".join(labels[-3:])
    if len(labels) >= 2:
        return ".".join(labels[-2:])
    return d


def main():
    src = sys.argv[1]
    data = json.load(open(src, encoding="utf-8"))
    rows = data["rows"]            # [民國年月, 網域, 網站性質]
    brands = load_brands(P2 / "brand-reference.csv")

    # group by registrable domain
    reg = {}   # regdom -> {hosts:set, props:Counter, months:set, rows:int}
    for ym, dom, prop in rows:
        rd = registrable(dom)
        e = reg.setdefault(rd, {"hosts": set(), "props": Counter(),
                                "months": set(), "rows": 0})
        e["hosts"].add(dom.strip().lower())
        e["props"][prop] += 1
        e["months"].add(ym)
        e["rows"] += 1

    coded = []
    for rd, e in reg.items():
        # A if the registrable domain OR any of its hostnames is a typosquat hit
        hit = detect(rd, brands)
        if hit["flag"] != "A":
            for h in e["hosts"]:
                r = detect(h, brands)
                if r["flag"] == "A":
                    hit = r
                    break
        d3 = "A" if hit["flag"] == "A" else "U"     # v1.2: A vs non-A
        prop = e["props"].most_common(1)[0][0]
        d4 = PROP_D4.get(prop, "UNK")
        coded.append({"regdom": rd, "d3": d3, "d4": d4, "prop": prop,
                      "brand": hit["brand"], "d5": hit["d5"],
                      "hosts": len(e["hosts"]), "rows": e["rows"]})

    with open(P2 / "coded-176455.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["regdom", "d3", "d4", "prop",
                                          "brand", "d5", "hosts", "rows"])
        w.writeheader()
        w.writerows(coded)

    n_rows = len(rows)
    n_host = len(set(d.strip().lower() for _, d, _ in rows))
    n_reg = len(reg)
    print(f"=== 176455 full classification ===")
    print(f"raw rows: {n_rows}   distinct hostnames: {n_host}   "
          f"distinct registrable domains: {n_reg}")
    print(f"inflation: {n_rows/n_reg:.1f}x rows per registrable domain\n")

    # domain-farm top
    farms = sorted(reg.items(), key=lambda kv: len(kv[1]["hosts"]), reverse=True)
    print("top 12 domain farms (by distinct hostnames):")
    for rd, e in farms[:12]:
        print(f"  {rd:28} {len(e['hosts']):5} hostnames  {e['rows']:5} rows")

    # D3 — A lower bound (per registrable domain)
    a = sum(1 for c in coded if c["d3"] == "A")
    print(f"\nD3 (per registrable domain, v1.2 A-vs-nonA):")
    print(f"  A (typosquat-confirmed impersonation, LOWER BOUND): "
          f"{a} ({a/n_reg*100:.1f}%)")
    print(f"  non-A: {n_reg-a} ({(n_reg-a)/n_reg*100:.1f}%)")

    # D4
    d4 = Counter(c["d4"] for c in coded)
    print(f"\nD4 (from 網站性質, per registrable domain):")
    for d, cnt in d4.most_common():
        print(f"  {d:8} {cnt:6} ({cnt/n_reg*100:.1f}%)")

    # impersonated targets among the A's
    tgt = Counter(c["brand"] for c in coded if c["d3"] == "A")
    print(f"\nimpersonated targets among A registrable domains "
          f"({a} total):")
    for b, cnt in tgt.most_common(25):
        print(f"  {cnt:4}  {b}")

    # 網站性質 raw distribution
    props = Counter(p for _, _, p in rows)
    print(f"\n網站性質 raw distribution (rows): {dict(props.most_common())}")


if __name__ == "__main__":
    main()
