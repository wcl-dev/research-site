#!/usr/bin/env python3
"""P1 inter-rater reliability — Cohen's kappa between two independent coders.

Reads coding-claude.csv + coding-codex.csv (cols: uid,D3,D4,D5,confidence,note),
computes Cohen's kappa per dimension, prints a report. D5 kappa is computed only
on rows where BOTH coders assigned D3=A (D5 is conditional on D3=A).
"""
import csv, sys
from collections import Counter
from pathlib import Path

P1 = Path(__file__).parent


def load(path):
    out = {}
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            uid = (r.get("uid") or "").strip()
            if not uid:
                continue
            out[uid] = {k: (r.get(k) or "").strip() for k in ("D3", "D4", "D5")}
    return out


def kappa(pairs):
    """pairs: list of (a, b). Returns (kappa, po, n)."""
    n = len(pairs)
    if n == 0:
        return None, None, 0
    po = sum(1 for a, b in pairs if a == b) / n
    cats = set(a for a, _ in pairs) | set(b for _, b in pairs)
    ca = Counter(a for a, _ in pairs)
    cb = Counter(b for _, b in pairs)
    pe = sum((ca[c] / n) * (cb[c] / n) for c in cats)
    k = (po - pe) / (1 - pe) if (1 - pe) > 1e-9 else 1.0
    return k, po, n


def main():
    a = load(P1 / "coding-claude.csv")
    b = load(P1 / "coding-codex.csv")
    uids = sorted(set(a) & set(b))
    miss = sorted((set(a) ^ set(b)))
    print(f"=== P1 inter-rater reliability (Claude vs Codex) ===")
    print(f"rows aligned: {len(uids)}  |  claude={len(a)} codex={len(b)}"
          f"  |  unmatched uids: {len(miss)}")
    if miss:
        print(f"  unmatched: {miss[:10]}")
    print()

    # D3 / D4 over all aligned rows
    for dim in ("D3", "D4"):
        pairs = [(a[u][dim], b[u][dim]) for u in uids]
        k, po, n = kappa(pairs)
        print(f"{dim}: kappa={k:.3f}  agreement={po*100:.1f}%  n={n}"
              f"  {'PASS' if k >= 0.7 else 'FAIL (<0.70)'}")
        disagree = [u for u in uids if a[u][dim] != b[u][dim]]
        if disagree:
            print(f"  {len(disagree)} disagreements:")
            for u in disagree:
                print(f"    {u}: claude={a[u][dim]:8} codex={b[u][dim]:8}")
        # per-dataset for D3
        if dim == "D3":
            for ds in ("165027", "160055", "176455"):
                dsp = [(a[u][dim], b[u][dim]) for u in uids if u.startswith(ds)]
                dk, dpo, dn = kappa(dsp)
                ks = f"{dk:.3f}" if dk is not None else "n/a"
                print(f"  [{ds}] kappa={ks} agreement={dpo*100:.1f}% n={dn}")
        print()

    # D5 only where both coded D3=A
    both_a = [u for u in uids if a[u]["D3"] == "A" and b[u]["D3"] == "A"]
    pairs = [(a[u]["D5"], b[u]["D5"]) for u in both_a]
    k, po, n = kappa(pairs)
    ks = f"{k:.3f}" if k is not None else "n/a"
    verdict = "" if k is None else ("PASS" if k >= 0.7 else "FAIL (<0.70)")
    print(f"D5 (on rows both coded A): kappa={ks}  agreement={po*100 if po else 0:.1f}%"
          f"  n={n}  {verdict}")
    disagree = [u for u in both_a if a[u]["D5"] != b[u]["D5"]]
    for u in disagree:
        print(f"    {u}: claude={a[u]['D5']:8} codex={b[u]['D5']:8}")
    print()

    # distribution summary
    print("=== D3 distribution ===")
    for label, src in (("claude", a), ("codex", b)):
        c = Counter(src[u]["D3"] for u in uids)
        print(f"  {label}: A={c['A']} B={c['B']} U={c['U']}")


if __name__ == "__main__":
    main()
