#!/usr/bin/env python3
"""探索 pcc-tender 機關行為指紋:驗證分區加總 + 印各維度分布,供定型用。"""
import json, statistics as st
from pathlib import Path

DATA = Path(__file__).parent / "data" / "fingerprints_2022h2.json"
d = json.loads(DATA.read_text())
cols = d["_meta"]["columns"]
rows = [dict(zip(cols, r)) for r in d["rows"]]

# 1) 驗證三組分類是否各自加總到 n(抓謄寫錯誤)
bad = []
for r in rows:
    if r["n_open"] + r["n_selective"] + r["n_ltd_eval"] + r["n_ltd_noeval"] != r["n"]:
        bad.append(("招標方式", r["agency"]))
    if r["n_lowest"] + r["n_mev"] != r["n"]:
        bad.append(("決標原則", r["agency"]))
    if r["n_works"] + r["n_goods"] + r["n_services"] != r["n"]:
        bad.append(("標的", r["agency"]))
print(f"== 驗證 ==  機關數={len(rows)}  分區加總不符={len(bad)}")
for b in bad[:20]:
    print("   !!", b)

# 2) 算 shares
for r in rows:
    n = r["n"]
    r["open_sh"] = r["n_open"] / n
    r["ltd_eval_sh"] = r["n_ltd_eval"] / n
    r["ltd_noeval_sh"] = r["n_ltd_noeval"] / n
    r["mev_sh"] = r["n_mev"] / n
    r["works_sh"] = r["n_works"] / n
    r["goods_sh"] = r["n_goods"] / n
    r["services_sh"] = r["n_services"] / n
    r["avg_award"] = r["total_award"] / n
    # 主導標的
    attr = {"工程": r["works_sh"], "財物": r["goods_sh"], "勞務": r["services_sh"]}
    r["dom_attr"] = max(attr, key=attr.get)
    r["dom_attr_sh"] = attr[r["dom_attr"]]

def quant(key, fmt="{:.2f}"):
    xs = sorted(r[key] for r in rows)
    qs = [xs[0], xs[len(xs)//10], xs[len(xs)//4], xs[len(xs)//2],
          xs[3*len(xs)//4], xs[9*len(xs)//10], xs[-1]]
    print(f"  {key:14s} min/p10/p25/med/p75/p90/max = " + " ".join(fmt.format(q) for q in qs))

print("\n== 維度分布(分位數) ==")
for k in ["ltd_noeval_sh", "ltd_eval_sh", "open_sh", "mev_sh", "works_sh", "goods_sh", "services_sh"]:
    quant(k)
print("  avg_award (NT$M):")
xs = sorted(r["avg_award"]/1e6 for r in rows)
qs = [xs[0], xs[len(xs)//4], xs[len(xs)//2], xs[3*len(xs)//4], xs[9*len(xs)//10], xs[-1]]
print("                 p0/p25/med/p75/p90/max = " + " ".join(f"{q:.1f}" for q in qs))

# 3) 主導標的分布
from collections import Counter
print("\n== 主導標的計數 ==", dict(Counter(r["dom_attr"] for r in rows)))

# 4) 紅旗:限制性未經評選佔比最高
print("\n== 限制性招標(未經公開評選) 佔比 TOP 15 ==")
for r in sorted(rows, key=lambda r: -r["ltd_noeval_sh"])[:15]:
    print(f"  {r['ltd_noeval_sh']*100:5.1f}%  ({r['n_ltd_noeval']:>3}/{r['n']:>3})  avg NT${r['avg_award']/1e6:7.1f}M  {r['agency']}")

# 5) 最有利標佔比最高(比優型)
print("\n== 最有利標系 佔比 TOP 15 ==")
for r in sorted(rows, key=lambda r: -r["mev_sh"])[:15]:
    print(f"  {r['mev_sh']*100:5.1f}%  dom={r['dom_attr']}  {r['agency']}")

# 6) 平均單案金額最高(資本密集)
print("\n== 平均單案金額 TOP 12 ==")
for r in sorted(rows, key=lambda r: -r["avg_award"])[:12]:
    print(f"  NT${r['avg_award']/1e6:8.1f}M/案  總 NT${r['total_award']/1e9:6.1f}B  ltd_noeval={r['ltd_noeval_sh']*100:4.1f}%  {r['agency']}")
