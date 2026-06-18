# Research Brief — From Price War to Cognitive Infrastructure: An Evidence Audit of the LLM-Penetration → Cognition Causal Chain

> **reasoning_chain: skipped** — this brief was authored manually around a four-link causal-chain spine (L1→L2→L3→L4a/b/c), not as an Interviewer Q-chain. The chain decomposition table below IS the reasoning chain; a separate reasoning_chain.md would duplicate it. The validator's "Q1–Q4 have 0 supporting records" warning is a known false alarm — records are tagged by `link`, not Q-index.

## Core Research Question

The source spec proposes a four-link causal chain: **low-cost model strategy → developer/market penetration → information intermediation → cognitive-infrastructure formation**, and asks whether this chain reframes model governance from a *technical* problem into an *information-sovereignty / cognitive-security* problem.

This pipeline does **not** attempt to *prove* that chain. It performs an **evidence audit** of it:

> For each link in the chain, what is the best available published evidence, how strong is it, and **where does the chain break**? Specifically: which links are empirically established (strong), which are contested-but-supported, and which are currently speculative leaps where the spec's own "incorrect-inference" warnings (§6) bite hardest?

The deliverable is an honest **chain-of-evidence map**, not a confirmation of the thesis.

## Why this scope (and not the spec's WP1–4 verbatim)

The original spec is a multi-year *research-program roadmap* (4 RQs × 4 hypotheses × 4 work packages × 3 observatories). It cannot be run as a single pipeline, and large parts of it overlap with existing work in this repo:

- **RQ3 / H3 (models have stable knowledge framing)** is already covered empirically by `llm-user-side-bias` (3 stages: cloud single-turn, local cross-model, multi-turn) and touched by `ai-sycophancy-attack-surface-tw`. Re-running WP2's "multi-model × political question bank × framing coding" would duplicate existing findings.
- **WP1 (market penetration dashboard)** is a data-engineering artifact, not a literature/evidence pipeline.
- **WP2 (model comparison)** is an *experiment* (requires actually running models), out of scope for a synthesis pipeline.
- **WP3 / WP4** are framework-building, suited to a conceptual paper, not a first empirical cut.

What is **genuinely novel and pipeline-runnable** is the **causal chain itself** — the coupling claim that *price-driven penetration amplifies framing into societal-level cognition* (the spec's distinctive contribution, RQ4 / H4). This brief targets exactly that, by auditing the evidence for every link the coupling claim depends on.

## The chain, decomposed into auditable links

| Link | Claim (maps to) | Audit task |
|---|---|---|
| **L1** | Price ↓ → developer/market adoption ↑ (RQ1 / H1) | Gather usage/share/pricing evidence. Is the price→adoption causal arrow supported, or merely correlated with other factors (capability, openness, licensing)? |
| **L2** | Adoption ↑ → users contact original sources less; AI answer replaces search (RQ2 / H2) | Gather zero-click / referral-decline / "AI-as-information-entry" evidence. **Guard:** distinguish "LLM chat replacing search" from "AI Overviews in search" — they are different mechanisms. |
| **L3** | Model output carries stable, measurable knowledge framing (RQ3 / H3) | Strongest link. Cite the existing empirical base (incl. this repo's own `llm-user-side-bias`, Waight Nature 2026, ELN/Samokhodskyi) as the anchor. Question: how *stable* and *cross-context-reproducible* is the framing? |
| **L4a** | Single-model dominance → output homogenization (technical: algorithmic/model monoculture, model collapse) | **Decomposed link — do not treat L4 as one claim.** Find monoculture/homogenization evidence. Expect *contested* (theory exists, LLM-specific empirics thin). |
| **L4b** | Homogenized output → shifts individual belief/framing (persuasion / framing effect) | Find AI-specific persuasion/framing-effect evidence. Expect *weak / analogical* — media-effects literature exists, AI-specific is thin. |
| **L4c** | Aggregated individual effects → **societal cognitive structure** (the spec's landing claim) | **The speculative leap. Expect near-empty.** Mark speculative plainly; the chain most likely breaks between L4b and L4c. |

A separate **counter-evidence cluster** operationalizes the spec's §6 ("incorrect inferences"): evidence that *breaks* the chain — adoption driven by capability not price; bias from training data / RLHF / safety policy / commercial choice rather than political intent; single-answer ≠ systemic effect.

## What this pipeline should find

### Priority 1 — L4, the load-bearing speculative link (decomposed into L4a / L4b / L4c)
The whole spec hinges on L4 being more than a hypothesis. **Do not treat L4 as one claim** — decompose so inflation has nowhere to hide:
- **L4a (homogenization):** "Model monoculture" / "algorithmic monoculture" (Kleinberg & Raghavan and successors); model collapse; output homogenization at scale.
- **L4b (individual belief shift):** AI-specific persuasion / framing-effect studies — does a model's framing measurably change what a user believes?
- **L4c (societal aggregation):** any longitudinal or large-N study linking a single information intermediary's framing to population-level shifts in knowledge/belief.

Handling protocol:
1. **Direct evidence first** (esp. L4a).
2. **Analogy evidence must be labelled as analogy:** search-engine agenda-setting / social-media echo-chamber literature may be cited ONLY as "mechanism has precedent in prior information infrastructure; transfer to LLMs is untested" — never as direct LLM evidence.
3. **Seek disconfirming evidence too** (don't straw-man L4): users running multiple models, increasing not decreasing model diversity, users still cross-checking sources.
4. **Write the gap as a research agenda:** what study design would close L4c? (This feeds back into the spec's Observatory idea — converts "can't prove it" into "here's how you would.")

### Priority 1 — L2, AI as information entry
- Zero-click search, referral-traffic decline, "Google Zero", post-2023 search-behavior shifts
- Empirical studies on users *not* clicking through to sources after an AI/LLM answer
- The distinction (and any data separating) chat-LLM substitution vs. in-search AI summaries

### Priority 2 — L1, price → adoption (includes a PRIMARY MARKET-DATA SNAPSHOT)
L1 carries an explicit quantitative component, not just literature. Two evidence types, kept separate:

**(a) Primary market-data snapshot** — collector WebFetches *actual numbers* from primary dashboards, not papers about them:
- OpenRouter token-share / model rankings
- Artificial Analysis pricing table (price per Mtok across providers; the "tens-of-X" spread the spec claims)
- HuggingFace download counts / GitHub dependency or star signals for open-weight models
- Discipline (mandatory): **stamp every figure with as-of date 2026-06-07**; these are live and stale fast. **Fetch the primary source, never a vendor's or media's restated number** (per `feedback-aio-vendor-framing`). The snapshot becomes a dated, source-linked quantitative block in the report.
- **Containment:** market numbers prove L1 (adoption rising) ONLY. They must not be smuggled into L4 (cognition shaped). Flag any source that makes that jump.

**(b) Literature on the causal arrow:**
- DeepSeek / Qwen / MiniMax / Zhipu / Tencent price-war reporting (esp. 2024–2026)
- Studies or analyses separating *price* from *capability / openness / licensing* as adoption drivers (the causal-identification problem for L1)

### Priority 2 — Framework anchors for "cognitive infrastructure"
The spec borrows FIMI Exposure Matrix / Information Ecosystem / Platform Governance / Cognitive Security. Find the actual sources behind these so the framing rests on real literature, not borrowed labels:
- "Information intermediary" / "infrastructure" theory applied to platforms (search, social, OS) — the historical analogy the spec leans on
- Cognitive security / FIMI frameworks (EU EEAS, DISARM, etc.)
- Platform governance & "essential facility / gatekeeper" framing (e.g. EU DMA gatekeeper concept) applied to AI
- Information / digital / AI sovereignty literature

### Priority 3 — Counter-evidence (operationalizes spec §6)
- Adoption explained by capability/openness, not price
- Bias sourced from training data / RLHF / safety / commercial choice, not political intent
- Critiques of over-claiming "AI cognitive warfare" / methodological cautions on inferring systemic cognitive effects from individual outputs

## Known anchor literature (dialogue partners — do NOT exclude)

1. **This repo's own `llm-user-side-bias`** — L3 primary evidence; intertextual self-citation.
2. **Waight et al., Nature 2026** — state media in training data → biased outputs (training-side framing mechanism); L3.
3. **Samokhodskyi / ELN 2026** — prompt-language reproduces Kremlin framing; L3 cross-lingual.
4. **Kleinberg & Raghavan, "algorithmic monoculture"** — closest existing theory for L4; test whether it has been extended to LLMs.

## Research angle to develop

**Frame: the chain is only as strong as its weakest load-bearing link.** The contribution is not "China's cheap models are cognitive warfare" (the spec explicitly disclaims this) but a sober map: L1 and L3 are reasonably supported, L2 is contested-but-trending, and L4 — once decomposed — most likely breaks between **L4b (analogical)** and **L4c (near-empty)**. Therefore the policy claim ("model governance = sovereignty/cognitive-security issue") is *conditional* on L4c, which the evidence does not yet support — and the report says exactly what study would be needed to support it. This is a **governance-under-uncertainty** frame, not a threat-assertion frame.

## Output target

Single Drafter pass producing a Traditional-Chinese evidence-audit report (~5000–7000 字): per-link evidence with explicit strength tiers, an honest statement of where the chain breaks, and a conditional policy conclusion. Suitable downstream for `pipeline-to-publication` → `generate-research-html`.

## Search strategy hints

### L4 (priority — the hard one)
- "algorithmic monoculture" LLM OR "model monoculture"
- "homogenization" "language model" output OR opinion
- "AI" "convergence" framing OR "issue salience" OR "agenda setting"
- "information intermediary" "cognition" OR "belief"
- "single source" "epistemic" population scale AI

### L2
- "zero-click" search 2024 OR 2025 OR 2026
- "AI Overviews" referral traffic decline study
- "LLM" replacing search engine user behavior empirical
- "Google Zero" OR "search referral" publisher decline

### L1
- OpenRouter token share model usage 2025 2026
- "Artificial Analysis" pricing benchmark LLM
- DeepSeek OR Qwen OR MiniMax price war API cost
- LLM adoption drivers price vs capability open-weight

### Frameworks
- "cognitive security" framework FIMI EU
- "DISARM" framework information manipulation
- "digital sovereignty" OR "information sovereignty" AI
- "gatekeeper" "Digital Markets Act" AI OR platform
- platform "essential facility" information infrastructure theory

### Counter-evidence (§6)
- critique "AI cognitive warfare" overclaim
- LLM bias source RLHF OR "training data" OR "safety" not political
- methodological caution inferring societal effect single output AI
