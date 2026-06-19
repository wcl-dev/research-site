#!/usr/bin/env python3
"""用 OpenFun 公司資料 API（g0v company.g0v.ronny.tw，免 Token）系統性歸戶廠商→控制集團。
方法：①對每家 IT 廠商 search→統編→show→統計董監事「所代表法人」席次（誰控制董事會）。
      ②反向 /api/fund 查各大集團在哪些公司占董監席位 → 抓出分名子公司。
來源：經濟部商業發展署商工登記（董監事名單含所代表法人）／經歐噴整理。
"""
import json, urllib.request, urllib.parse, time
from pathlib import Path
from collections import Counter

OUT = Path(__file__).parent / "data"; OUT.mkdir(exist_ok=True)
BASE = "https://company.g0v.ronny.tw"

def get(path):
    for _ in range(3):
        try:
            with urllib.request.urlopen(BASE+path, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(1)
    return {}

def board_legal_persons(ubn):
    """回傳 (資本, [(法人名, 席次)], 總席次)"""
    d = get(f"/api/show/{ubn}"); d = d.get("data", d)
    bm = d.get("董監事名單") or []
    c = Counter()
    for m in bm:
        rep = m.get("所代表法人")
        if isinstance(rep, list):
            name = rep[1] if len(rep) > 1 and rep[1] else None
        else:
            name = rep or None
        c[name or "(自然人)"] += 1
    cap = d.get("實收資本額(元)") or d.get("資本總額(元)")
    return cap, c.most_common(), len(bm), d.get("公司名稱")

def resolve(name):
    d = get("/api/search?" + urllib.parse.urlencode({"q": name, "alive_only": "true"}))
    data = d.get("data", [])
    if not data:
        d = get("/api/search?" + urllib.parse.urlencode({"q": name}))
        data = d.get("data", [])
    if not data:
        return None
    # 取第一個（最相關）；若名稱完全相符優先
    best = data[0]
    for r in data:
        if (r.get("公司名稱") or "") == name:
            best = r; break
    return best.get("統一編號"), best.get("公司名稱")

# 要歸戶的 IT 廠商（去分公司/英文，取核心名）
VENDORS = [
 "中華電信","資拓宏宇國際","精誠資訊","精誠科技整合","精誠軟體服務","叡揚資訊","凌群電腦",
 "關貿網路","神通資訊科技","康大資訊","宏碁資訊服務","安碁資訊","國眾電腦","凌網科技",
 "凌誠科技","台灣國際商業機器","碩睿資訊","藍新資訊","華電聯網","三商電腦","敦陽科技",
 "敦陽資訊","展昇資訊","晶茂資訊科技","嘉誠資訊","駿永資訊科技","奕祥資訊","大鐸資訊",
 "桓基科技","台灣富士通","康和資訊系統","宏碁雲架構服務","鉅林國際資訊","台灣源訊科技",
 "葳橋資訊","資通電腦","大同世界科技","中華系統整合","中華資安國際","東捷資訊服務",
 "中孚科技","台灣恩益禧","藍新科技","宏碁股份",
]

# 反向：各大集團董監版圖
GROUPS = ["中華電信","宏碁","精誠資訊","神通電腦","聯華實業","大同","三商投資控股",
          "東元電機","遠傳電信","大眾","驊宏資通","研華"]

print("="*70, "\n[1] 廠商 → 董事會控制法人\n", "="*70)
resolution = {}
for v in VENDORS:
    r = resolve(v)
    if not r:
        print(f"  {v:14s}  ✗ 查無"); resolution[v]={"found":False}; continue
    ubn, official = r
    cap, lps, seats, _ = board_legal_persons(ubn)
    top = lps[0] if lps else ("(無)",0)
    # 控制法人＝最大法人席次（排除自然人）且 >=1/3
    ctrl = next(((n,c) for n,c in lps if n!="(自然人)"), None)
    capm = f"{int(cap)/1e8:.2f}億" if cap and str(cap).isdigit() else "?"
    ctrl_s = f"{ctrl[0]}({ctrl[1]}/{seats}席)" if ctrl else "—(無法人董監)"
    print(f"  {official[:18]:18s} 統編{ubn} 資本{capm:>7s} 控制法人:{ctrl_s}")
    resolution[v] = {"found":True,"ubn":ubn,"name":official,"capital":cap,
                     "seats":seats,"legal_persons":lps,"control":ctrl}
    time.sleep(0.15)

print("\n"+"="*70, "\n[2] 各集團董監版圖（/api/fund 反向）\n", "="*70)
group_members = {}
for g in GROUPS:
    d = get("/api/fund?" + urllib.parse.urlencode({"q": g}))
    mem = [(r.get("統一編號"), r.get("公司名稱")) for r in d.get("data",[])]
    group_members[g] = {"found": d.get("found"), "members": mem}
    print(f"\n  ◆ {g}  (found {d.get('found')})")
    for ubn,nm in mem[:30]:
        print(f"      {ubn}  {nm}")
    time.sleep(0.15)

(OUT/"company_resolution.json").write_text(json.dumps(
    {"resolution":resolution,"group_members":group_members}, ensure_ascii=False, indent=2))
print(f"\n→ 已寫 {OUT/'company_resolution.json'}")
