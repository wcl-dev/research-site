#!/usr/bin/env python3
"""P2 — 160055 D3 inter-rater kappa + A/B/U estimate.

Reads the two independent codings (Claude, Codex) of the n=400 random sample of
distinct 160055 site names. Computes Cohen's kappa, a consensus coding, and the
A/B/U estimate two ways: per-site (unweighted) and CNT-weighted (report-volume),
each with a confidence interval (Wald for per-site, bootstrap for CNT-weighted).
"""
import csv, json, math, random
from collections import Counter
from pathlib import Path

P2 = Path(__file__).parent
N_TOTAL_SITES = 8574
N_TOTAL_CNT = 104834


def load_coding(path):
    out = {}
    with open(path, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            idx = (r.get("idx") or "").strip()
            d3 = (r.get("D3") or "").strip().upper()
            if idx and d3 in ("A", "B", "U"):
                out[int(idx)] = d3
    return out


def kappa(pairs):
    n = len(pairs)
    po = sum(1 for a, b in pairs if a == b) / n
    cats = set(a for a, _ in pairs) | set(b for _, b in pairs)
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    pe = sum((ca[c] / n) * (cb[c] / n) for c in cats)
    return (po - pe) / (1 - pe) if (1 - pe) > 1e-9 else 1.0, po


def wald(p, n):
    return 1.96 * math.sqrt(p * (1 - p) / n)


def main():
    sample = {}
    for line in (P2 / "sample-160055-400.jsonl").read_text("utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            sample[r["idx"]] = r
    claude = load_coding(P2 / "coding-160055-claude.csv")
    codex = load_coding(P2 / "coding-160055-codex.csv")
    idxs = sorted(set(claude) & set(codex))
    n = len(idxs)
    print(f"=== 160055 D3 inter-rater (n={n}) ===")
    print(f"claude rows={len(claude)} codex rows={len(codex)} aligned={n}\n")

    k, po = kappa([(claude[i], codex[i]) for i in idxs])
    print(f"Cohen's kappa (D3, A/B/U) = {k:.3f}   agreement = {po*100:.1f}%   "
          f"{'PASS' if k >= 0.7 else 'FAIL (<0.70)'}")
    dis = [i for i in idxs if claude[i] != codex[i]]
    print(f"disagreements: {len(dis)}")
    cm = Counter((claude[i], codex[i]) for i in dis)
    for (a, b), c in cm.most_common():
        print(f"  claude={a} codex={b}: {c}")

    # binary collapse: A vs non-A (B and U merged). The 3-way kappa fails on the
    # B/U boundary; the load-bearing distinction is A (impersonation).
    kb, pob = kappa([("A" if claude[i] == "A" else "N",
                      "A" if codex[i] == "A" else "N") for i in idxs])
    print(f"\nbinary A-vs-nonA kappa   = {kb:.3f}   agreement = {pob*100:.1f}%   "
          f"{'PASS' if kb >= 0.7 else 'FAIL'}")
    print("  (diagnosis: 3-way fail is localised to the B/U boundary; "
          "A vs non-A is reliable)")

    # consensus: agree -> code; disagree -> U
    consensus = {i: (claude[i] if claude[i] == codex[i] else "U") for i in idxs}

    print("\n=== D3 distribution (per-site, unweighted) ===")
    for label, cod in (("claude", claude), ("codex", codex),
                       ("consensus", consensus)):
        c = Counter(cod[i] for i in idxs)
        print(f"  {label:10} A={c['A']:3} ({c['A']/n*100:4.1f}%)  "
              f"B={c['B']:3} ({c['B']/n*100:4.1f}%)  "
              f"U={c['U']:3} ({c['U']/n*100:4.1f}%)")

    # per-site estimate (consensus) with Wald CI
    c = Counter(consensus[i] for i in idxs)
    print(f"\n=== 160055 per-site A/B/U estimate (consensus, n={n}) ===")
    for cat in ("A", "B", "U"):
        p = c[cat] / n
        ci = wald(p, n)
        print(f"  {cat}: {p*100:.1f}% ± {ci*100:.1f}%   "
              f"-> ~{p*N_TOTAL_SITES:.0f} of {N_TOTAL_SITES} sites "
              f"[{(p-ci)*N_TOTAL_SITES:.0f}-{(p+ci)*N_TOTAL_SITES:.0f}]")

    # CNT-weighted estimate (consensus) with bootstrap CI
    rows = [(consensus[i], sample[i]["cnt"]) for i in idxs]
    tot = sum(cnt for _, cnt in rows)
    wpt = {cat: sum(cnt for d, cnt in rows if d == cat) / tot
           for cat in ("A", "B", "U")}
    random.seed(42)
    boot = {cat: [] for cat in ("A", "B", "U")}
    for _ in range(2000):
        samp = [random.choice(rows) for _ in rows]
        t = sum(cnt for _, cnt in samp)
        for cat in ("A", "B", "U"):
            boot[cat].append(sum(cnt for d, cnt in samp if d == cat) / t)
    print(f"\n=== 160055 CNT-weighted A/B/U estimate (consensus, "
          f"sample CNT={tot}) ===")
    print("  (weights each sampled site by its report count — approximates the "
          "share of\n   the 104,834 total reports that involve A vs B sites)")
    for cat in ("A", "B", "U"):
        lo, hi = sorted(boot[cat])[50], sorted(boot[cat])[1949]
        print(f"  {cat}: {wpt[cat]*100:.1f}%   bootstrap 95% CI "
              f"[{lo*100:.1f}%, {hi*100:.1f}%]")

    # write consensus coding
    with open(P2 / "coding-160055-consensus.csv", "w", encoding="utf-8",
              newline="") as f:
        w = csv.writer(f)
        w.writerow(["idx", "name", "cnt", "d4", "D3_claude", "D3_codex",
                    "D3_consensus"])
        for i in idxs:
            w.writerow([i, sample[i]["name"], sample[i]["cnt"],
                        sample[i]["d4"], claude[i], codex[i], consensus[i]])
    print(f"\nwrote coding-160055-consensus.csv")


if __name__ == "__main__":
    main()
