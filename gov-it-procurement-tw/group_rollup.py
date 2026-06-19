#!/usr/bin/env python3
"""集團層市場集中度：用 OpenFun 商工登記董監事資料歸戶後，重算 IT 採購集中度。
回答 operator 假設「帳面幾千家、實為少數集團分名隱藏寡占」是否成立。
集團歸屬證據見 data/company_resolution.json（董監事所代表法人席次）。
集團層聚合直接由 pcc-tender CASE-WHEN group_by 全母體查得（非僅 top-N）。"""
import json
from pathlib import Path
OUT = Path(__file__).parent / "data"

TOTAL_N = 13339
TOTAL_AMT = 378953239819  # 勞務165398029245 + 財物213555210574

# 集團層（pcc-tender CASE-WHEN 全母體聚合結果，2026-06-19）
# 註：CASE 內 '駿永' 誤打成 '驅永'，故 駿永33件落入長尾；驊宏實際≈40件（影響 <0.3pt，不重算）
GROUPS = [  # (group, n, amt, n_entities)
 ("中華電信系", 707, 32064017614, 12),
 ("精誠系", 394, 7661326988, 17),
 ("宏碁系", 215, 5352868652, 11),
 ("叡揚(獨立)", 149, 2076269154, 2),
 ("凌群(獨立)", 122, 4123020612, 5),
 ("聯華神通系", 108, 3364988922, 5),
 ("關貿(財政部官股)", 102, 1524620997, 1),
 ("工研院(法人)", 91, 3460815620, 1),
 ("敦陽系", 86, 1466464452, 3),
 ("大眾投控", 81, 2447706613, 2),
 ("遠傳系", 79, 5816028092, 4),
 ("資策會(法人)", 70, 3355552816, 1),
 ("三商投控", 68, 10979803361, 2),
 ("驊宏資通", 40, 350000000, 1),   # 修正 駿永+驊宏 估值
]
TAIL_N, TAIL_AMT, TAIL_ENT = 11060, 295092014234, 4424

# 帳面（實體層，未歸戶）對照——展示「分名隱藏」幅度
ENTITY = {"中華電信": 405, "精誠系(同名)": 235, "宏碁(同名)": 98, "聯華神通(神通資訊)": 80}

named_n = sum(g[1] for g in GROUPS)
named_amt = sum(g[2] for g in GROUPS)
named_ent = sum(g[3] for g in GROUPS)

print("="*64)
print(f"IT 母體：{TOTAL_N:,} 件 / NT${TOTAL_AMT/1e9:.0f}B / 約 {named_ent+TAIL_ENT:,} 個 distinct 實體")
print("="*64)
print(f"\n14 大集團合計：{named_n:,} 件（{named_n/TOTAL_N*100:.1f}%）"
      f" / NT${named_amt/1e9:.0f}B（{named_amt/TOTAL_AMT*100:.1f}%）/ 僅 {named_ent} 個實體")
print(f"其他·獨立長尾：{TAIL_N:,} 件（{TAIL_N/TOTAL_N*100:.1f}%）"
      f" / NT${TAIL_AMT/1e9:.0f}B / {TAIL_ENT:,} 個實體（平均 {TAIL_N/TAIL_ENT:.1f} 件/家）")

cum = 0
print("\n集團層 CRn（件數）：")
for i,(g,n,a,e) in enumerate(GROUPS,1):
    cum += n
    if i in (1,3,4,8,14):
        print(f"  CR{i:<2} = {cum:>5,} 件 = {cum/TOTAL_N*100:4.1f}%   （最後加入：{g}）")

cum_a = 0
print("\n集團層 CRn（金額）：")
gs = sorted(GROUPS, key=lambda x:-x[2])
for i,(g,n,a,e) in enumerate(gs,1):
    cum_a += a
    if i in (1,3,4,8,14):
        print(f"  CR{i:<2} = NT${cum_a/1e9:6.1f}B = {cum_a/TOTAL_AMT*100:4.1f}%   （含：{g}）")

print("\n「分名隱藏」幅度（帳面實體 → KYC 集團）：")
print(f"  中華電信   405 → 707 件  (+{(707-405)/405*100:.0f}%)")
print(f"  宏碁        98 → 215 件  (+{(215-98)/98*100:.0f}%)")
print(f"  精誠       235 → 394 件  (+{(394-235)/235*100:.0f}%)")
print(f"  神通        80 → 108 件  (+{(108-80)/80*100:.0f}%)")

print("\n— 中華電信系金額佔比（單一集團）：", f"{32064017614/TOTAL_AMT*100:.1f}%（件數 {707/TOTAL_N*100:.1f}%）→ 大案更集中")

derived = {
  "total_n": TOTAL_N, "total_amt": TOTAL_AMT,
  "named_groups": [{"group":g,"n":n,"amt":a,"entities":e} for g,n,a,e in GROUPS],
  "tail": {"n":TAIL_N,"amt":TAIL_AMT,"entities":TAIL_ENT},
  "cr_count": {"cr4": sum(g[1] for g in GROUPS[:4])/TOTAL_N,
               "cr8": sum(g[1] for g in GROUPS[:8])/TOTAL_N,
               "cr14": named_n/TOTAL_N},
  "cr_amt": {"named_share": named_amt/TOTAL_AMT,
             "cht_share": 32064017614/TOTAL_AMT},
  "hidden_uplift": {"中華電信":(405,707),"宏碁":(98,215),"精誠":(235,394),"神通":(80,108)},
}
(OUT/"group_concentration.json").write_text(json.dumps(derived, ensure_ascii=False, indent=2))
print(f"\n→ 已寫 {OUT/'group_concentration.json'}")
