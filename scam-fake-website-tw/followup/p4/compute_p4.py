#!/usr/bin/env python3
"""P4 — prevalence-weighted estimate of the fake-website share.

Takes the P3 per-手法 D1 distribution and weights it by real-world 手法
prevalence (嘉義 52459, 2,461 詐欺 cases, 113年, case-level). Produces a
RANGE under several mapping/M0 assumptions — not a false-precise point.
The 6 P3 strata cover ~58% of all 詐欺 cases; the uncovered ~42% is bounded
qualitatively in the P4 report, not here.
"""

# --- P3 per-手法 D1 victim counts (from aggregate_p3.py) ---
P3 = {
    # stratum: {M1, M2, M3, M4, M5, M0, n}
    "假投資":   dict(M1=8,  M2=0,  M3=38, M4=0,  M5=0,  M0=24, n=70),
    "網購":     dict(M1=4,  M2=61, M3=0,  M4=1,  M5=0,  M0=5,  n=71),
    "假冒物流": dict(M1=27, M2=0,  M3=0,  M4=0,  M5=0,  M0=29, n=56),
    "解除分期": dict(M1=0,  M2=0,  M3=0,  M4=0,  M5=22, M0=0,  n=22),
    "假交友":   dict(M1=2,  M2=0,  M3=0,  M4=15, M5=0,  M0=17, n=34),
    "假冒機構": dict(M1=0,  M2=0,  M3=0,  M4=0,  M5=57, M0=0,  n=57),
}

# --- 手法 prevalence weights: 嘉義 52459, 113年, case count ---
W = {
    "假投資":   577,                 # 假投資
    "網購":     305,                 # 假網拍
    "假冒物流": 231,                 # 解除分期付款(騙賣家) — the 賣貨便 seller scam
    "解除分期": 6,                   # 解除分期付款(騙買家) — classic 假客服 phone scam
    "假交友":   172 + 57,            # 假交友(投資詐財)+(徵婚詐財)
    "假冒機構": 42 + 41,             # 假冒機構(公務員)+猜猜我是誰
}
COVERED = sum(W.values())
ALL_CASES_52459 = 2461


def rate(stratum, cats, denom_excl_m0=False):
    s = P3[stratum]
    num = sum(s[c] for c in cats)
    den = s["n"] - (s["M0"] if denom_excl_m0 else 0)
    return num / den if den else 0.0


def weighted(cats, denom_excl_m0=False, m0_as_m1_strata=()):
    """Weighted rate across the 6 strata. m0_as_m1_strata: strata whose M0
    is reassigned to M1 (per the logistics-subagent finding that 物流 M0 is
    very likely unrecorded M1)."""
    tot = 0.0
    for st, w in W.items():
        s = P3[st]
        if st in m0_as_m1_strata:
            num = sum(s[c] for c in cats) + (s["M0"] if "M1" in cats else 0)
            den = s["n"]
        else:
            num = sum(s[c] for c in cats)
            den = s["n"] - (s["M0"] if denom_excl_m0 else 0)
        r = num / den if den else 0.0
        tot += w * r
    return tot / COVERED


def main():
    print("=== P4 — prevalence-weighted fake-website share ===")
    print(f"weight basis: 嘉義 52459, 113年, {ALL_CASES_52459} 詐欺 cases (case-level)")
    print(f"6 P3 strata cover {COVERED} cases = "
          f"{COVERED/ALL_CASES_52459*100:.0f}% of all 詐欺 cases\n")

    print("per-手法 M1 (獨立假網站) rate, and 52459 weight:")
    for st in W:
        print(f"  {st:9} w={W[st]:4}  M1 rate={rate(st,['M1'])*100:5.1f}%  "
              f"M1+M3={rate(st,['M1','M3'])*100:5.1f}%  "
              f"(n={P3[st]['n']}, M0={P3[st]['M0']})")

    print("\n--- WEIGHTED estimates for the covered ~58% of 詐欺 cases ---\n")

    print("M1 獨立假網站（狹義「假網站」）:")
    a = weighted(["M1"])
    b = weighted(["M1"], denom_excl_m0=True)
    c = weighted(["M1"], m0_as_m1_strata=["假冒物流"])
    print(f"  S1 全分母（M0 計入分母、不視為 M1）:        {a*100:.1f}%")
    print(f"  S2 medium-known（排除 M0 分母）:            {b*100:.1f}%")
    print(f"  S3 物流 M0 視為 M1（subagent 判斷）:        {c*100:.1f}%")
    print(f"  → 狹義假網站 案件加權區間 ≈ {a*100:.0f}–{c*100:.0f}%")

    print("\nM1+M3（含假冒/詐騙集團自建 APP）:")
    a3 = weighted(["M1", "M3"])
    b3 = weighted(["M1", "M3"], denom_excl_m0=True)
    print(f"  S1 全分母:                                 {a3*100:.1f}%")
    print(f"  S2 medium-known:                           {b3*100:.1f}%")
    print(f"  → 含假冒APP 案件加權區間 ≈ {a3*100:.0f}–{b3*100:.0f}%")

    print("\nM2 真平台假帳號（明確非假網站）:")
    print(f"  全分母: {weighted(['M2'])*100:.1f}%   "
          f"medium-known: {weighted(['M2'],denom_excl_m0=True)*100:.1f}%")
    print("M5 純電話:")
    print(f"  全分母: {weighted(['M5'])*100:.1f}%   "
          f"medium-known: {weighted(['M5'],denom_excl_m0=True)*100:.1f}%")
    print("M0 判決未述:")
    m0w = weighted(["M0"])
    print(f"  全分母: {m0w*100:.1f}%")


if __name__ == "__main__":
    main()
