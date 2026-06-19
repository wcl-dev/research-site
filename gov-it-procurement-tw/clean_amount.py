#!/usr/bin/env python3
"""用 OpenFun 公司資料 API 的「財政部稅籍行業代號」客觀判定大額廠商是否為 IT，
量化「系統」關鍵字網的非 IT 污染（重電/環保/醫療/工程顧問），算出乾淨 IT 金額。
行業代號來源：財政部稅籍（經 g0v company.g0v.ronny.tw／歐噴整理）。"""
import json, urllib.request, urllib.parse, time
from pathlib import Path
OUT = Path(__file__).parent / "data"
BASE = "https://company.g0v.ronny.tw"

def get(p):
    for _ in range(3):
        try:
            with urllib.request.urlopen(BASE+p, timeout=30) as r: return json.load(r)
        except Exception: time.sleep(1)
    return {}

def industry(name):
    d = get("/api/search?"+urllib.parse.urlencode({"q":name,"alive_only":"true"}))
    data = d.get("data") or get("/api/search?"+urllib.parse.urlencode({"q":name})).get("data")
    if not data: return None, None
    ubn = data[0]["統一編號"]
    d = get(f"/api/show/{ubn}"); d = d.get("data",d)
    mof = d.get("財政部") or {}
    rows = mof.get("行業") if isinstance(mof,dict) else None
    primary = rows[0] if rows else None  # [code, name]
    return ubn, primary

# 前 30 大金額廠商（IT 母體 by amount，含疑似污染）
BIG = [
 ("中欣行",17839075210),("中華電信",16879508394),("KC Cottrell",12506879742),
 ("台灣世曦工程顧問",10109947319),("三商電腦",8702393714),("伸峰科技",7024888458),
 ("遠大資訊",6645343000),("資拓宏宇",6201725820),("虹華科技",5949915786),
 ("Mitsubishi",5859897871),("捷雷科技",5542290000),("遠傳電信系統整合",5017420303),
 ("台灣國際商業機器",5004693797),("士林電機廠",4730575233),("中華電信數據通信",3835694442),
 ("大同股份",3627445893),("工業技術研究院",3460815620),("資訊工業策進會",3355552816),
 ("台灣固網",3172571988),("群冠高科",3140765700),("神通資訊科技",2962519695),
 ("中興工程顧問",2896720343),("台灣奇異電力",2732050111),("台灣日立",2700000000),
 ("駿永資訊科技",2668196491),("台灣恩益禧",2649553907),("凌群電腦",2634100872),
 ("大同智能",2625000000),("東元電機",2608600000),("山林水環境工程",2464277000),
]
# IT 行業代號前綴（財政部稅務行業）：電腦/軟體/系統/資訊/電信/電腦批發
IT_PREFIX = ("46411","46412","582","620","6201","6202","631","639","6190","6120","6110","61","620100")
# 外商/查無→人工標註
MANUAL = {"KC Cottrell":"非IT(韓商脫硫環保)","Mitsubishi":"非IT(商社/重機)","台灣日立":"非IT(空調重機)"}

print(f"{'廠商':22s}{'金額(億)':>9s}  {'主行業':28s} 判定")
it_amt=nonit_amt=0
results=[]
for name,amt in BIG:
    if name in MANUAL:
        verdict="非IT"; ind=MANUAL[name]
    else:
        ubn,prim=industry(name); time.sleep(0.12)
        code = prim[0] if prim else ""
        ind = f"{prim[0]} {prim[1]}" if prim else "(查無)"
        is_it = any(code.startswith(p) for p in IT_PREFIX)
        verdict = "IT" if is_it else "非IT?"
    if verdict.startswith("IT"): it_amt+=amt
    else: nonit_amt+=amt
    results.append((name,amt,ind,verdict))
    print(f"  {name:20s}{amt/1e8:8.1f}  {ind[:28]:28s} {verdict}")

TOTAL_AMT=378953239819
print(f"\n前 30 大金額中：IT {it_amt/1e8:.0f}億 / 非IT {nonit_amt/1e8:.0f}億")
print(f"非IT 污染 ≈ {nonit_amt/TOTAL_AMT*100:.1f}% 的帳面總額（{nonit_amt/1e8:.0f}億 / {TOTAL_AMT/1e8:.0f}億）")
print(f"乾淨 IT 名目金額估 ≈ {(TOTAL_AMT-nonit_amt)/1e8:.0f}億（保守：僅清前 30 大可見污染）")

(OUT/"contamination.json").write_text(json.dumps(
  {"big30":[{"name":n,"amt":a,"industry":i,"verdict":v} for n,a,i,v in results],
   "nonit_amt":nonit_amt,"it_clean_amt_est":TOTAL_AMT-nonit_amt,
   "nonit_share_of_total":nonit_amt/TOTAL_AMT}, ensure_ascii=False, indent=2))
print(f"→ 已寫 {OUT/'contamination.json'}")
