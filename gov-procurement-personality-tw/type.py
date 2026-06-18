#!/usr/bin/env python3
"""定型:主類型(標的×決標原則) + 跨類型特質旗標(巨額/偏直接議價)。
   演繹給軸、資料給門檻(見 explore.py 分位數)。"""
import json, csv
from pathlib import Path
from collections import Counter, defaultdict

BASE = Path(__file__).parent
d = json.loads((BASE / "data" / "fingerprints_2022h2.json").read_text())
cols = d["_meta"]["columns"]
rows = [dict(zip(cols, r)) for r in d["rows"]]

# 門檻(來自 explore.py 分布的自然斷點)
MERIT_TH = 0.40        # mev_sh>=0.4 視為「比優導向」(p75=0.41)
CAPITAL_TH = 20e6      # 平均單案>=NT$20M 視為巨額(p90=20.6M)
DIRECT_TH = 0.15       # 限制性未經評選佔比>=15% 視為偏直接議價(p90=0.03,明顯離群)

for r in rows:
    n = r["n"]
    r["mev_sh"] = r["n_mev"] / n
    r["ltd_noeval_sh"] = r["n_ltd_noeval"] / n
    r["avg_award"] = r["total_award"] / n
    attr = {"工程": r["n_works"]/n, "財物": r["n_goods"]/n, "勞務": r["n_services"]/n}
    r["dom_attr"] = max(attr, key=attr.get)
    merit = r["mev_sh"] >= MERIT_TH
    # 主類型
    if r["dom_attr"] == "工程":
        r["type"] = "工程發包型"
    elif r["dom_attr"] == "財物":
        r["type"] = "設備採買型"
    else:  # 勞務
        r["type"] = "委外比優型" if merit else "勞務比價型"
    # 跨類型特質旗標
    r["capital"] = r["avg_award"] >= CAPITAL_TH
    r["direct"] = r["ltd_noeval_sh"] >= DIRECT_TH

# 交叉表 標的 × 比價/比優
print("== 交叉表:主導標的 × 決標原則 ==")
ct = defaultdict(int)
for r in rows:
    ct[(r["dom_attr"], "比優" if r["mev_sh"] >= MERIT_TH else "比價")] += 1
for a in ["工程", "財物", "勞務"]:
    print(f"  {a}:  比價={ct[(a,'比價')]:>3}   比優={ct[(a,'比優')]:>3}")

# 主類型分布
print("\n== 主類型分布(150 機關) ==")
for t, c in Counter(r["type"] for r in rows).most_common():
    share_money = sum(r["total_award"] for r in rows if r["type"] == t) / sum(r["total_award"] for r in rows)
    print(f"  {t:8s}  機關 {c:>3} ({c/len(rows)*100:4.1f}%)   佔窗內總金額 {share_money*100:4.1f}%")

# 特質旗標
print("\n== 特質旗標 ==")
print(f"  巨額資本級(avg>=NT$20M):  {sum(r['capital'] for r in rows)} 機關,",
      f"佔窗內金額 {sum(r['total_award'] for r in rows if r['capital'])/sum(r['total_award'] for r in rows)*100:.1f}%")
print(f"  偏直接議價(限制未評>=15%): {sum(r['direct'] for r in rows)} 機關")

# 每型代表(取件數最多前 4)
print("\n== 每型代表機關 ==")
for t in ["設備採買型", "工程發包型", "委外比優型", "勞務比價型"]:
    ex = sorted([r for r in rows if r["type"] == t], key=lambda r: -r["n"])[:5]
    print(f"  [{t}] " + " / ".join(r["agency"] for r in ex))

# 偏直接議價清單(廉政關注,含金額脈絡)
print("\n== 偏直接議價機關(>=15%,需個案脈絡,非違法證據) ==")
for r in sorted([r for r in rows if r["direct"]], key=lambda r: -r["ltd_noeval_sh"]):
    print(f"  {r['ltd_noeval_sh']*100:5.1f}% ({r['n_ltd_noeval']}/{r['n']})  avg NT${r['avg_award']/1e6:7.1f}M  [{r['type']}{' +巨額' if r['capital'] else ''}]  {r['agency']}")

# 存檔
with open(BASE / "data" / "typed_2022h2.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["agency", "type", "n", "total_award", "avg_award", "dom_attr",
                "mev_sh", "ltd_noeval_sh", "capital", "direct"])
    for r in sorted(rows, key=lambda r: (r["type"], -r["n"])):
        w.writerow([r["agency"], r["type"], r["n"], r["total_award"], round(r["avg_award"]),
                    r["dom_attr"], round(r["mev_sh"], 3), round(r["ltd_noeval_sh"], 3),
                    int(r["capital"]), int(r["direct"])])
print("\n→ data/typed_2022h2.csv 已存")
