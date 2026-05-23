#!/usr/bin/env python3
"""Typosquat / brand-impersonation detector for scam domains (Phase 2).

Decides, from a domain string ALONE, whether it impersonates a known brand
(-> D3=A) or shows no detectable brand (-> stays U). Built for dataset 176455,
which has no description column. High-precision lower-bound detector: it cannot
catch impersonations that put the brand only on the page, not in the domain.

Matching layers:
  1. substring   — non-strict brand token (>=4 chars) contained in the domain
  2. label-exact — short (<=3 char) or strict-flagged token == a whole label
                   or hyphen-segment
  3. fuzzy       — windowed SequenceMatcher >= 0.86 for non-strict tokens >=6 chars

Usage:
  python3 typosquat_detect.py validate   # precision/recall on 160055 pilot
  python3 typosquat_detect.py apply      # rescue-rate on 176455 300-sample
"""
import csv, sys, re, json
from difflib import SequenceMatcher
from pathlib import Path
from collections import Counter

P2 = Path(__file__).parent
P1 = P2.parent / "p1"
TLDS_2 = {"com.tw", "gov.tw", "org.tw", "net.tw", "edu.tw", "co.uk"}


def load_brands(path):
    brands = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#") or line.startswith("canonical,"):
            continue
        p = line.split(",")
        if len(p) < 4:
            continue
        brands.append({
            "canonical": p[0], "d5": p[1], "strict": p[2].strip() == "1",
            "tokens": [t.strip().lower() for t in p[3].split(";") if t.strip()],
        })
    return brands


def parse_domain(domain):
    d = re.sub(r"^[^a-z0-9]+", "", domain.strip().lower())
    labels = d.split(".")
    if len(labels) >= 3 and ".".join(labels[-2:]) in TLDS_2:
        core = labels[:-2]
    else:
        core = labels[:-1] if len(labels) > 1 else labels
    return [c for c in core if c]


def _alpha(s):
    return re.sub(r"[^a-z]", "", s.lower())


def detect(domain, brands):
    core = parse_domain(domain)
    full_nd = "".join(_alpha(l) for l in core)            # alpha only, all labels
    full_kd = "".join(re.sub(r"[^a-z0-9]", "", l.lower()) for l in core)
    labels_kd = {re.sub(r"[^a-z0-9]", "", l.lower()) for l in core}
    segs = set()
    for lab in core:
        for seg in re.split(r"[-_]", lab):
            if seg:
                segs.add(seg.lower())
                segs.add(_alpha(seg))
    hits = []
    for b in brands:
        for tok in b["tokens"]:
            tok_a = _alpha(tok)
            tok_flat = tok.replace("-", "").replace("_", "")
            if b["strict"] or len(tok_a) <= 3:
                if tok in segs or (tok_a and tok_a in segs) or tok_flat in labels_kd:
                    hits.append((b, tok, "label-exact"))
            else:
                if tok_a and tok_a in full_nd:
                    hits.append((b, tok, "substring"))
                elif tok_flat and tok_flat != tok_a and tok_flat in full_kd:
                    hits.append((b, tok, "substring"))
                elif len(tok_a) >= 6:
                    L, best = len(tok_a), 0.0
                    for i in range(max(1, len(full_nd) - L + 1)):
                        w = full_nd[i:i + L]
                        if w:
                            best = max(best, SequenceMatcher(None, w, tok_a).ratio())
                    if best >= 0.86:
                        hits.append((b, tok, f"fuzzy:{best:.2f}"))
    if hits:
        hits.sort(key=lambda h: 1 if h[2].startswith("fuzzy") else 0)
        b, tok, method = hits[0]
        return {"flag": "A", "brand": b["canonical"], "d5": b["d5"],
                "token": tok, "method": method}
    return {"flag": "U", "brand": "", "d5": "", "token": "", "method": ""}


def registrable(domain):
    core = parse_domain(domain)
    return core[-1] if core else domain


def validate(brands):
    """Precision/recall on the 160055 pilot (domain-only vs gold A/B labels)."""
    samples = {}
    for line in (P1 / "pilot-sample.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            if r["dataset"] == "160055":
                samples[r["uid"]] = r["domain"]
    gold = {}
    with open(P1 / "coding-claude.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["uid"] in samples:
                gold[r["uid"]] = r["D3"]
    tp = fp = fn = tn = 0
    catches, misses, falsepos = [], [], []
    for uid, dom in samples.items():
        res = detect(dom, brands)
        algo_a = res["flag"] == "A"
        gold_a = gold[uid] == "A"
        if algo_a and gold_a:
            tp += 1; catches.append((uid, dom, res["brand"], res["method"]))
        elif algo_a and not gold_a:
            fp += 1; falsepos.append((uid, dom, gold[uid], res["brand"], res["method"]))
        elif not algo_a and gold_a:
            fn += 1; misses.append((uid, dom))
        else:
            tn += 1
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    print("=== VALIDATE on 160055 pilot (n=40, domain-only vs gold labels) ===")
    print(f"gold A={tp+fn}  gold non-A={fp+tn}")
    print(f"algo flagged A={tp+fp}  ->  TP={tp} FP={fp} FN={fn} TN={tn}")
    print(f"PRECISION={prec:.2f}  RECALL={rec:.2f}")
    print(f"\ncatches ({len(catches)}):")
    for u, d, br, m in catches:
        print(f"  {u:12} {d:32} -> {br} [{m}]")
    print(f"\nfalse positives ({len(falsepos)}):")
    for u, d, g, br, m in falsepos:
        print(f"  {u:12} {d:32} gold={g} -> WRONGLY {br} [{m}]")
    print(f"\nmissed gold-A ({len(misses)}) — domain carries no detectable brand:")
    for u, d in misses:
        print(f"  {u:12} {d}")


def apply_176455(brands):
    domains = [l.strip() for l in (P2 / "sample-176455-300.txt").read_text(
        encoding="utf-8").splitlines() if l.strip()]
    flagged = []
    for dom in domains:
        res = detect(dom, brands)
        if res["flag"] == "A":
            flagged.append((dom, res["brand"], res["d5"], res["method"]))
    regs = Counter(registrable(d) for d in domains)
    print("=== APPLY on 176455 300-row random sample ===")
    print(f"rows: {len(domains)}")
    print(f"distinct registrable domains: {len(regs)}  "
          f"(top farms: {', '.join(f'{k}×{v}' for k,v in regs.most_common(6))})")
    print(f"\nflagged A (rescued from U): {len(flagged)}  "
          f"= {len(flagged)/len(domains)*100:.1f}% of rows")
    for dom, br, d5, m in flagged:
        print(f"  {dom:34} -> {br} ({d5}) [{m}]")
    # rescue rate on a per-registrable-domain basis
    flagged_regs = {registrable(d) for d, *_ in flagged}
    print(f"\nflagged distinct registrable domains: {len(flagged_regs)} "
          f"of {len(regs)} = {len(flagged_regs)/len(regs)*100:.1f}%")


if __name__ == "__main__":
    brands = load_brands(P2 / "brand-reference.csv")
    mode = sys.argv[1] if len(sys.argv) > 1 else "validate"
    print(f"loaded {len(brands)} brands, "
          f"{sum(len(b['tokens']) for b in brands)} tokens\n")
    if mode == "validate":
        validate(brands)
    elif mode == "apply":
        apply_176455(brands)
    else:
        print("usage: typosquat_detect.py [validate|apply]")
