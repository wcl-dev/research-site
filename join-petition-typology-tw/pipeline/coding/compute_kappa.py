#!/usr/bin/env python3
"""Inter-model reliability: Cohen's kappa between original sonnet codes (val_gold.json)
and an independent opus re-coding. Usage: compute_kappa.py <recode_output.json>
Honest scope: this is inter-MODEL (sonnet × opus, blind, same codebook) agreement —
a proxy for inter-coder reliability that tests codebook unambiguity, NOT human double-blind.
"""
import json, sys
from collections import Counter

HERE = __file__.rsplit("/", 1)[0]
gold = json.load(open(f"{HERE}/val_gold.json"))
out = json.load(open(sys.argv[1]))
recodes = {c["url"]: c for c in (out.get("result", out).get("codes", []))}

pairs_for = {}
both = [u for u in gold if u in recodes]
print(f"gold={len(gold)} recoded={len(recodes)} overlap={len(both)}\n")

def form(c): return c["d1_target"] + c["d2_enable"] + c["d3_outcome"]

def collect(getter):
    return [(getter(gold[u]), getter(recodes[u])) for u in both]

def kappa(pairs):
    n = len(pairs)
    if n == 0: return (0, 0, 0)
    po = sum(a == b for a, b in pairs) / n
    ca, cb = Counter(a for a, _ in pairs), Counter(b for _, b in pairs)
    cats = set(ca) | set(cb)
    pe = sum((ca[k] / n) * (cb[k] / n) for k in cats)
    k = (po - pe) / (1 - pe) if pe < 1 else 1.0
    return (po, k, n)

def interp(k):
    return ("poor" if k < 0.2 else "fair" if k < 0.4 else "moderate" if k < 0.6
            else "substantial" if k < 0.8 else "almost-perfect")

print(f"{'variable':14}{'%agree':>8}{'kappa':>8}  strength")
vars_ = [
    ("d1_target", lambda c: c["d1_target"]),
    ("d2_enable", lambda c: c["d2_enable"]),
    ("d3_outcome", lambda c: c["d3_outcome"]),
    ("form_score", form),
    ("motive", lambda c: c["motive"]),
    ("constituency", lambda c: c["constituency"]),
    ("org_backing", lambda c: c["org_backing"]),
    ("org_binary", lambda c: 0 if c["org_backing"] == "none" else 1),
    ("ai_essay", lambda c: c["ai_essay"]),
    ("topic", lambda c: c["topic"]),
]
for name, g in vars_:
    po, k, n = kappa(collect(g))
    print(f"{name:14}{po*100:>7.0f}%{k:>8.2f}  {interp(k)}")

# org_backing audit: of the 57 gold org-backed, how many does opus also call org-backed?
gold_org = [u for u in both if gold[u]["org_backing"] != "none"]
agree_org = sum(recodes[u]["org_backing"] != "none" for u in gold_org)
print(f"\norg_backing audit: gold org-backed in overlap = {len(gold_org)}; "
      f"opus also org-backed = {agree_org} ({round(100*agree_org/len(gold_org)) if gold_org else 0}%)")
# motive confusion (the load-bearing contested var)
print("\nmotive confusion (rows=sonnet gold, cols=opus):")
mc = Counter((gold[u]["motive"], recodes[u]["motive"]) for u in both)
print("       opus0  opus1  opus2")
for a in (0, 1, 2):
    print(f" gold{a}  " + "  ".join(f"{mc[(a,b)]:5d}" for b in (0, 1, 2)))
