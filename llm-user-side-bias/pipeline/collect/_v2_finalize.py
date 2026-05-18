#!/usr/bin/env python3
"""V2 finalize: pick high-relevance subset, write candidates_v2.jsonl with c046+ ids.

Input:  /tmp/llm-bias-v2/merged.jsonl
Output: projects/llm-user-side-bias/pipeline/collect/candidates_v2.jsonl

Selection rules:
  - Drop pure-vision / multimodal-only jailbreaks (out of brief: text LLM identity).
  - Drop knowledge_gated_access records that are clearly unrelated (off-topic word match).
  - Cap multiturn at ~30 best (prioritize 2024–2026, broad coverage).
  - Keep cross-cluster records (relevant to both).
  - Manually whitelist canonical papers regardless of automatic ranking.

why_relevant generated per record from title+abstract — format:
  "Q1-MT: <specific contribution, <15 words>"  for multiturn cluster
  "Q4-KG: <specific contribution, <15 words>"  for knowledge-gated cluster
  Both prefixes for cross-cluster.

Banned phrases in why_relevant: 'adjacent to', 'context for', the bare title.
"""
import json
import re
from pathlib import Path

PROJECT = Path("(internal-tool/)projects/llm-user-side-bias")
TMP = Path("/tmp/llm-bias-v2")
OUT = PROJECT / "pipeline/collect/candidates_v2.jsonl"

# --- Drop rules -------------------------------------------------------------

# Vision/multimodal-only or other off-text-LLM scope: drop.
VISION_RE = re.compile(
    r"\b(vision-language|vision language|multimodal|multi-modal|"
    r"image[- ]input|visual prompt|typographic|figstep|MLLM|VLM|"
    r"medical mllm|MMJ-Bench|REVEAL|White-box Multimodal|"
    r"Bi-Modal|cross-modality)\b",
    re.I,
)

# Off-topic in knowledge_gated cluster (string matched but topic-wrong)
KG_DROP_RE = re.compile(
    r"\b(remote sensing|spatial pyramid|code completion|"
    r"hallucination on hallucination|JAILFUZZ)\b",
    re.I,
)

# --- Hand-crafted why_relevant per known canonical paper --------------------
# Keyed by case-insensitive substring of title.
WHY_OVERRIDES = {
    "multi-turn jailbreaking large language models via attention shifting":
        "Q1-MT: Mechanistic analysis of why multi-turn dialogues bypass safety — attention shifts away from refusal tokens.",
    "chain of attack: hide your intention through multi-turn":
        "Q1-MT: Multi-turn interrogation attack hides malicious intent across turns — direct analog of pilot's gradient-erosion finding.",
    "red queen":
        "Q1-MT: Empirical benchmark exposing latent multi-turn risks absent in single-turn evaluations across frontier LLMs.",
    "multibreak":
        "Q1-MT: Scalable multi-turn jailbreak benchmark for evaluating LLM safety — establishes evaluation methodology.",
    "echo chamber":
        "Q1-MT: Multi-turn jailbreak relies on conversational context echo — supports L1 conversation-layer threat model.",
    "not all turns matter":
        "Q1-MT: Per-turn credit assignment in multi-turn jailbreaks identifies which dialogue turns drive successful bypass.",
    "siren: a learning-based multi-turn":
        "Q1-MT: Simulates real human multi-turn jailbreak behaviors — closer to ecological dialogues than synthetic adversarial.",
    "mtsa: multi-turn safety alignment":
        "Q1-MT: Defense via multi-round red-teaming — countermeasure framing for multi-turn vulnerabilities documented in pilot.",
    "assessing and mitigating multi-turn jailbreak":
        "Q1-MT: Crescendo-attack empirical study — direct citation for crescendo mechanism referenced in V2 brief.",
    "mart: improving llm safety with multi-round automatic":
        "Q1-MT: Multi-round automatic red-teaming — Meta's defensive training approach against multi-turn attacks.",
    "multi-step jailbreaking privacy":
        "Q1-MT+Q4-KG: Early (2023) multi-step jailbreak on ChatGPT — privacy-extraction version of gradient erosion.",
    "rolellm: benchmarking, eliciting":
        "Q1-MT: Persona/role-play elicitation benchmark — relevant to L1 conversation-layer persona-attack mechanism.",
    '"do anything now"':
        "Q1-MT: In-the-wild jailbreak prompt characterization including DAN-style persona attacks — empirical taxonomy.",
    "open sesame":
        "Q1-MT: Universal black-box jailbreak generation — single-turn baseline that multi-turn attacks compare against.",
    "wolf in sheep":
        "Q1-MT: Nested jailbreak prompts using narrative wrapping — closely related to persona/role-escalation pattern.",
    "comprehensive study of jailbreak attack versus defense":
        "Q1-MT: Survey covering attack/defense landscape — provides taxonomic position for multi-turn family.",
    "hitchhiker's guide to jailbreaking chatgpt":
        "Q1-MT: Prompt-engineering jailbreak survey — single/multi-turn taxonomy with persona-attack subsection.",
    "masterkey":
        "Q1-MT: Automated jailbreaking via dialogue manipulation — early example of automated multi-turn attack generation.",
    "play guessing game":
        "Q1-MT+Q4-KG: Indirect jailbreak via implicit clues — operational example of knowledge-gated access (user must know to ask).",
    "drattack":
        "Q1-MT: Prompt decomposition jailbreak — splits malicious request across turns, parallel to pilot's gradient progression.",
    "defending jailbreak prompts via in-context adversarial game":
        "Q1-MT: In-context adversarial defense — counterpoint to in-context attack vector observed in pilot.",
    "a survey on in-context learning":
        "Q1-MT: Comprehensive ICL survey — foundational reference for in-context-learning effects on alignment.",
    "jailbreak and guard aligned language models with only few in-context demonstrations":
        "Q1-MT: Few-shot in-context jailbreak (Wei et al.) — canonical demonstration of ICL as alignment bypass.",
    "many-shot jailbreaking":
        "Q1-MT: Anthropic many-shot jailbreaking — in-context-learning-as-bypass; canonical paper for L1 threat model.",
    "red teaming language models with language models":
        "Q1-MT: Foundational red-team paper — Perez et al.; establishes automated adversarial dialogue evaluation paradigm.",
    "jailbreaking black box large language models in twenty queries":
        "Q1-MT: PAIR attack — iterative dialogue refinement to jailbreak, multi-turn cousin of pilot's adversarial follow-up.",
    "tongue-tied":
        "Q1-MT: Language-induced safety bypass — methodologically parallel to identity-induced refusal documented in pilot.",
    "against the achilles":
        "Q1-MT: Red-teaming survey for generative models — taxonomy reference covering multi-turn attack family.",
    "know your limits: a survey of abstention":
        "Q1-MT+Q4-KG: Abstention survey — when LLMs should refuse; conceptual frame for asymmetric refusal across users.",
    "harry potter is still here":
        "Q4-KG: Knowledge leakage in unlearned models — proves model retains information it claims to lack (parallel to pilot's L2 base-capability).",
    "casting a spell: sentence pairing":
        "Q4-KG: Limitation-breaking via sentence-pair priming — knowledge-gated access via prior-text scaffolding.",
    "defamiliarization attack":
        "Q1-MT: Literary-theory-framed prompt attack — narrative reframing parallel to pilot's identity reframing.",
    "contextualjailbreak":
        "Q1-MT: Evolutionary red-teaming with conversational priming — direct relative of pilot's multi-turn priming mechanism.",
    "stay in character, stay safe":
        "Q1-MT: Role-playing safety defense via self-evolution — countermeasure framing for persona attack.",
    "disentangling intent from role":
        "Q1-MT: Persona-invariant safety alignment — addresses exactly the persona-leakage problem L1 threat model identifies.",
    "persona-conditioned adversarial prompting":
        "Q1-MT: Multi-identity persona red-teaming — methodologically analogous to pilot's identity-disclosure cells.",
    "mitigating the safety-utility trade-off in llm alignment via adaptive safe context":
        "Q1-MT: Adaptive safe context learning — defensive ICL framing matching pilot's context-modulation observations.",
    "jailbreaker in jail":
        "Q1-MT: Moving-target jailbreak defense; references multi-turn attack surface (2023, foundational).",
    "prompt-based jailbreaking of leading llm chatbots: a survey":
        "Q1-MT: 2026 survey of prompt-based jailbreak attacks — current taxonomy reference for V2 positioning.",
    "civicshield":
        "Q1-MT: Multi-turn defense framework for government chatbots — applied/policy-relevant deployment of multi-turn safety.",
    "redefining ai red teaming in the agentic era":
        "Q1-MT: Agentic red-teaming framing — pertinent if pilot work extends to agentic conversational settings.",
    "safedream":
        "Q1-MT: Proactive early-jailbreak detection via world-model — defensive multi-turn vulnerability framing.",
    "ranking manipulation for conversational search":
        "Q1-MT: Conversational manipulation of search engines — adjacent multi-turn manipulation in retrieval context.",
    "safe in isolation, dangerous together":
        "Q1-MT: Agent-driven multi-turn decomposition jailbreak — directly mirrors pilot's gradient-erosion mechanism.",
    "jailbreaking frontier foundation models through intention deception":
        "Q1-MT: Intention-deception multi-turn attack — methodological parallel to pilot's adversarial-follow-up unlock.",
    "from domains to instances: dual-granularity data synthesis for llm unlearning":
        "Q4-KG: LLM unlearning evaluation — establishes whether models truly forget vs. only refuse to surface.",
    "pig: privacy jailbreak attack on llms via gradient-based iterative in-context":
        "Q1-MT+Q4-KG: Iterative ICL jailbreak extracting private info — operational form of knowledge-gated extraction.",
    "the geometry of intent": None,  # vague; likely drop
    "title pending 47": None,  # placeholder paper id; drop
}

# Force-include via keyword (must be in selected set even if filter would drop)
FORCE_INCLUDE_TITLE_RE = re.compile(
    r"crescendo|multi-turn jailbreaking large language models via attention|"
    r"red queen|chain of attack|multibreak|echo chamber|mart:|rolellm|"
    r"do anything now|wolf in sheep|jailbreak and guard aligned language|"
    r"many-shot|hitchhiker's guide|masterkey|"
    r"survey on in-context learning|red teaming language models with language|"
    r"harry potter is still here|defamiliarization|contextualjailbreak|"
    r"disentangling intent from role|persona-conditioned adversarial|"
    r"adaptive safe context|jailbreaking black box large language models in twenty|"
    r"safe in isolation|intention deception|play guessing game|"
    r"multi-step jailbreaking privacy|know your limits: a survey of abstention|"
    r"casting a spell|not all turns matter|mtsa: multi-turn safety alignment|"
    r"siren: a learning-based|pig: privacy jailbreak",
    re.I,
)


def make_why_relevant(rec):
    title_low = rec["title"].lower()
    for key, val in WHY_OVERRIDES.items():
        if key in title_low:
            return val  # may be None -> drop
    # Generic: write a specific contribution line from abstract.
    cluster = rec["cluster"]
    abs_ = rec.get("abstract_or_snippet", "")[:400]
    # Detect dominant theme
    if "multi-turn" in (title_low + abs_.lower()) or "multi turn" in (title_low + abs_.lower()):
        prefix = "Q1-MT"
        sub = "Multi-turn jailbreak study"
    elif "in-context" in (title_low + abs_.lower()):
        prefix = "Q1-MT"
        sub = "In-context-learning safety study"
    elif "persona" in (title_low + abs_.lower()) or "role" in (title_low + abs_.lower()):
        prefix = "Q1-MT"
        sub = "Persona/role-play safety study"
    elif "knowledge" in (title_low + abs_.lower()) or "elicit" in (title_low + abs_.lower()):
        prefix = "Q4-KG"
        sub = "Knowledge-elicitation / asymmetric-access study"
    elif "jailbreak" in (title_low + abs_.lower()) or "refusal" in (title_low + abs_.lower()):
        prefix = "Q1-MT"
        sub = "Jailbreak / refusal study"
    else:
        prefix = "Q1-MT"
        sub = "LLM safety study"
    # Brief contribution: first 12 words of abstract trimmed.
    words = abs_.split()[:18]
    contrib = " ".join(words)
    contrib = contrib.rstrip(".,;:")
    return f"{prefix}: {sub} — {contrib}"


# --- Load merged --------------------------------------------------------------

with (TMP / "merged.jsonl").open() as f:
    recs = [json.loads(l) for l in f if l.strip()]

# Apply drop rules
kept = []
for r in recs:
    title = r["title"]
    abstract = r.get("abstract_or_snippet", "")
    blob = title + " " + abstract
    if VISION_RE.search(blob):
        continue
    if r["cluster"] == "knowledge_gated_access" and KG_DROP_RE.search(blob):
        continue
    # Override-explicit drops (value None)
    title_low = title.lower()
    drop = False
    for key, val in WHY_OVERRIDES.items():
        if key in title_low and val is None:
            drop = True
            break
    if drop:
        continue
    kept.append(r)

# Rank: force-include first, then year desc, then cross-cluster bonus.
def rank_key(r):
    forced = 0 if FORCE_INCLUDE_TITLE_RE.search(r["title"]) else 1
    cross = 0 if "+" in r["cluster"] else 1
    yr = -(r.get("year") or 0)
    return (forced, cross, yr)

kept.sort(key=rank_key)

# Cap multiturn-only at 25; knowledge_gated and cross stay all.
final = []
mt_only_count = 0
for r in kept:
    if r["cluster"] == "multiturn_dialogue_safety":
        if mt_only_count >= 25:
            continue
        mt_only_count += 1
    final.append(r)

print(f"Final kept: {len(final)}")
by_c = {}
for r in final:
    by_c[r["cluster"]] = by_c.get(r["cluster"], 0) + 1
for k, v in sorted(by_c.items()):
    print(f"  {k}: {v}")

# Assign c046+ ids and why_relevant, write output
out_lines = []
for i, r in enumerate(final, start=46):
    rec = {
        "id": f"c{i:03d}",
        "title": r["title"],
        "url": r["url"],
        "source_type": r.get("source_type", "preprint"),
        "year": r.get("year"),
        "author_or_org": r.get("author_or_org", ""),
        "abstract_or_snippet": r.get("abstract_or_snippet", ""),
        "why_relevant": make_why_relevant(r),
        "search_query": r.get("search_query", ""),
        "cluster": r["cluster"],
        "source_track": "track1_openalex",
    }
    out_lines.append(json.dumps(rec, ensure_ascii=False))

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w") as f:
    f.write("\n".join(out_lines) + "\n")

print(f"\nWrote {len(out_lines)} records to {OUT}")
print(f"ID range: c046 .. c{46 + len(out_lines) - 1:03d}")
