#!/usr/bin/env python3
"""V2 collect: merge tmp tracks, dedupe by URL, cluster-tag, filter noise.

Reads /tmp/llm-bias-v2/{mt,kg}_q*.jsonl produced by search_academic.py and
writes /tmp/llm-bias-v2/merged.jsonl with one record per unique URL.
"""
import json
import re
from pathlib import Path

TMP = Path("/tmp/llm-bias-v2")

CLUSTER_MAP = {
    "mt_": "multiturn_dialogue_safety",
    "kg_": "knowledge_gated_access",
}

KW = {
    "multiturn_dialogue_safety": [
        "multi-turn", "multiturn", "multi turn",
        "jailbreak", "jail-break",
        "crescendo",
        "persona attack", "role-play", "role play", "role-playing", "roleplay",
        "conversational attack", "conversation attack", "dialogue attack",
        "in-context", "in context learning",
        "chain of", "multi-round", "multiround",
        "context window", "context-window",
        "safety alignment", "alignment bypass",
        "adversarial dialogue", "adversarial conversation",
        "refusal", "red team", "red-team",
        "follow-up", "follow up",
        "many-shot", "many shot",
    ],
    "knowledge_gated_access": [
        "knowledge-gated", "knowledge gated",
        "asymmetric information", "asymmetric access",
        "prior knowledge", "user knowledge",
        "elicit", "uncover", "extract knowledge",
        "adversarial prompt",
        "epistemic", "differential access",
        "jailbreak", "in-context",
        "context-dependent", "context dependent",
    ],
}

EXCLUDE_RE = re.compile(
    r"\b(image generation|deepfake|recommender system|recommendation system|"
    r"medical image|protein|molecular|drug discovery|robotics|"
    r"autonomous driving|speech synthesis|text-to-image|stable diffusion|"
    r"imagenet)\b",
    re.I,
)


def has_kw(text: str, kws):
    t = text.lower()
    return any(k in t for k in kws)


records: dict = {}
clusters_seen: dict = {}

for path in sorted(TMP.glob("*.jsonl")):
    if path.name == "merged.jsonl":
        continue
    prefix = path.stem.split("_")[0] + "_"
    cluster = CLUSTER_MAP.get(prefix)
    if cluster is None:
        continue
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            url = r.get("url") or ""
            if not url:
                continue
            title = r.get("title") or ""
            abstract = r.get("abstract_or_snippet") or ""
            blob = title + " " + abstract
            if EXCLUDE_RE.search(blob):
                continue
            if not has_kw(blob, KW[cluster]):
                continue
            if len(abstract) < 50:
                continue
            if url in records:
                clusters_seen[url].add(cluster)
                continue
            r["cluster"] = cluster
            records[url] = r
            clusters_seen[url] = {cluster}

for url, cs in clusters_seen.items():
    if len(cs) > 1:
        records[url]["cluster"] = "+".join(sorted(cs))

print(f"Total deduped relevant records: {len(records)}")
by_cluster = {}
for r in records.values():
    by_cluster[r["cluster"]] = by_cluster.get(r["cluster"], 0) + 1
for k, v in sorted(by_cluster.items()):
    print(f"  {k}: {v}")

with (TMP / "merged.jsonl").open("w") as f:
    for r in records.values():
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
