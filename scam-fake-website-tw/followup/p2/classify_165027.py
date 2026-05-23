#!/usr/bin/env python3
"""P2 — full classification of dataset 165027 (moda 停止解析網域, 1,466 rows).

Rule layer: parse the formulaic 描述 column ("一頁式詐騙購物網站") to extract the
impersonated entity and assign D3/D4/D5. Generic descriptions fall back to the
typosquat detector on the domain. Per codebook v1.1.

Reads the query_rows JSON dump; writes coded-165027.csv; prints aggregates.
"""
import json, csv, re, sys
from collections import Counter
from pathlib import Path

P2 = Path(__file__).parent
sys.path.insert(0, str(P2))
from typosquat_detect import load_brands, detect  # noqa: E402

SRC = ("/Users/wclim/.claude/projects/-Users-wclim-randomfindings/"
       "5e5435ee-308b-4896-aed0-3efcbc618aa4/tool-results/"
       "mcp-twinkle-hub-opendata-query_rows-1779430899230.txt")

# entity strings that are NOT a specific brand (codebook v1.1 §3)
GENERIC = {"電商一頁式", "一頁式", "電商", "電子商務", "購物", "詐騙網站", "網站", ""}
# generic industry descriptors -> U (codebook v1.1 "模糊具名規則")
INDUSTRY_DESC = ["網路廣告平台業", "客制化科技", "客製化科技", "科技公司",
                 "生technology"]

SUFFIXES = ["購物網站首頁", "購物網站登入頁面", "購物網站", "購物網頁",
            "網站登入頁面", "登入頁面", "帳號詐騙", "詐騙", "網站", "網頁"]
PREFIXES = ["疑似", "假冒", "偽冒", "連至"]


def extract_entity(desc):
    s = (desc or "").strip()
    changed = True
    while changed:
        changed = False
        for p in PREFIXES:
            if s.startswith(p):
                s = s[len(p):]; changed = True
    for suf in SUFFIXES:                       # strip one longest trailing suffix
        if s.endswith(suf):
            s = s[: -len(suf)]; break
    return s.strip()


def normalize_brand(entity):
    e = entity
    for junk in ["股份有限公司", "有限公司", "票證", "生物科技", "創意",
                 "一頁式詐騙", "一頁式", "詐騙", "數位科技", "24H", "24h", " "]:
        e = e.replace(junk, "")
    return e.strip()


def d5_of(entity):
    e = entity
    if "LINE" in e or "line" in e.lower():
        return "TELCO"
    if any(k in e for k in ["一卡通", "悠遊卡", "ECPay", "綠界", "電子發票",
                            "支付", "Pay"]):
        return "FIN"
    if any(k in e for k in ["財政部", "國稅", "健保", "監理", "台電", "政府",
                            "戶政", "自來水"]):
        return "GOV"
    if any(k in e for k in ["郵政", "黑貓", "宅配", "物流", "7-11", "超商",
                            "賣貨便", "全家"]):
        return "LOGI"
    return "ECOM"


def classify(row, brands):
    num, desc, domain, created = row
    entity = extract_entity(desc)
    norm = normalize_brand(entity)
    # generic e-commerce one-pager -> typosquat fallback on domain
    if entity in GENERIC or norm in GENERIC:
        res = detect(domain, brands)
        if res["flag"] == "A":
            return dict(D3="A", D4="SHOP", D5=res["d5"] or "ECOM",
                        entity=res["brand"], method="typosquat", conf="M")
        return dict(D3="U", D4="SHOP", D5="", entity="(generic 一頁式)",
                    method="rule-generic", conf="L")
    # generic industry descriptor -> U (v1.1 rule)
    if any(ind in entity for ind in INDUSTRY_DESC):
        return dict(D3="U", D4="OTHER", D5="", entity=entity,
                    method="rule-industry", conf="L")
    # named brand -> A
    if entity and entity not in GENERIC:
        d4 = "OTHER" if ("LINE" in entity and "帳號" in (desc or "")) else "SHOP"
        return dict(D3="A", D4=d4, D5=d5_of(entity), entity=norm or entity,
                    method="rule-desc", conf="H")
    # fallback
    res = detect(domain, brands)
    if res["flag"] == "A":
        return dict(D3="A", D4="SHOP", D5=res["d5"] or "ECOM",
                    entity=res["brand"], method="typosquat", conf="M")
    return dict(D3="U", D4="UNK", D5="", entity="(unparsed)",
                method="none", conf="L")


def main():
    data = json.load(open(SRC, encoding="utf-8"))
    rows = data["rows"]
    brands = load_brands(P2 / "brand-reference.csv")
    coded = []
    for row in rows:
        c = classify(row, brands)
        coded.append({"編號": row[0], "網域": row[2], "創建日期": row[3], **c})

    with open(P2 / "coded-165027.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["編號", "網域", "創建日期", "D3", "D4",
                                          "D5", "entity", "method", "conf"])
        w.writeheader()
        w.writerows(coded)

    n = len(coded)
    print(f"=== 165027 full classification (n={n}) ===\n")
    d3 = Counter(c["D3"] for c in coded)
    print(f"D3: A={d3['A']} ({d3['A']/n*100:.1f}%)  "
          f"B={d3['B']} ({d3['B']/n*100:.1f}%)  "
          f"U={d3['U']} ({d3['U']/n*100:.1f}%)")
    print(f"D4: {dict(Counter(c['D4'] for c in coded))}")
    print(f"D5 (A rows): {dict(Counter(c['D5'] for c in coded if c['D3']=='A'))}")
    print(f"method: {dict(Counter(c['method'] for c in coded))}")

    # dedup by domain
    uniq = len(set(c["網域"] for c in coded))
    print(f"\ndedup: {n} rows -> {uniq} unique domains")

    # top impersonated targets (A rows, normalized entity)
    ents = Counter(c["entity"] for c in coded if c["D3"] == "A")
    print(f"\ntop 20 impersonated targets (A rows):")
    for e, cnt in ents.most_common(20):
        print(f"  {cnt:4}  {e}")

    # creation-date year distribution (trend)
    yrs = Counter((c["創建日期"] or "")[:4] for c in coded if c["創建日期"])
    print(f"\n創建年份分布: {dict(sorted(yrs.items()))}")


if __name__ == "__main__":
    main()
