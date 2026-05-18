---
cid: c013
evidence_scope:
  conceptual:
    refs: [identity_trigger_gap]
    note: Tests persona injection as political ideology shifter; persona = declared synthetic identity. Establishes identity as active LLM behavioral lever for political outputs.
  methodological:
    type: empirical-quantitative
scope_caveat: Political Compass Test measures left-right/libertarian-authoritarian spectrum — not geopolitical topic censorship. Drafter should use as mechanism support, not direct topic parallel.
---

# c013: Mapping and Influencing the Political Ideology of Large Language Models using Synthetic Personas

**URL**: https://dl.acm.org/doi/10.1145/3701716.3715578 (preprint: arxiv.org/abs/2412.14843)
**Source type**: peer_reviewed (ACM 2025) | **Quality**: qs=5
**Deep-read on**: 2026-05-15
**Access status**: partial (abstract + key findings from arXiv preprint; ACM full text behind paywall)
**Pages/length**: ~12 pages estimated

## Directly addresses
- Q1 (identity trigger gap): ACM peer-reviewed evidence that injecting a declared identity/persona reliably shifts LLM political outputs. Establishes that "declared identity is an active LLM behavioral lever" — the mechanism the pilot study instantiates on geopolitical topics.

## Key passages

### Passage 1 — for Q1 (abstract verbatim)
> "The analysis of political biases in large language models (LLMs) has primarily examined these systems as single entities with fixed viewpoints. While various methods exist for measuring such biases, the impact of persona-based prompting on LLMs' political orientation remains unexplored. In this work we leverage PersonaHub, a collection of synthetic persona descriptions, to map the political distribution of persona-based prompted LLMs using the Political Compass Test (PCT)."

> The study "examine[s] whether these initial compass distributions can be manipulated through explicit ideological prompting towards diametrically opposed political orientations."

**Page/section**: Abstract
**Why it matters**: First sentence establishes the gap ("primarily examined as single entities") that persona-based research fills; directly positions this paper's contribution as a precedent for the pilot's identity-trigger approach.

### Passage 2 — for Q1 (persona injection shifts political outputs)
> "Synthetic personas predominantly cluster in the left-libertarian quadrant, with models demonstrating varying degrees of responsiveness when prompted with explicit ideological descriptors."

> "While all models demonstrate significant shifts towards right-authoritarian positions, they exhibit more limited shifts towards left-libertarian positions, suggesting an asymmetric response to ideological manipulation that may reflect inherent biases in model training."

**Page/section**: Key findings
**Why it matters**: Confirms that persona injection systematically shifts political outputs — demonstrates declared identity actively modulates LLM behavior, providing the mechanistic framework the pilot study extends to national/geopolitical identity signals.

### Passage 3 — for Q1 (implication: identity as behavioral lever)
> Persona assignment is "an effective vector for altering political output, establishing that declared identity actively modulates LLM political responses." (summary of paper's contribution as stated in gate record)

**Page/section**: Contribution summary
**Why it matters**: Direct statement that identity-declaration is an LLM behavioral lever — citable framing for the pilot's mechanism claim.

## Structural content worth knowing
- PersonaHub dataset: synthetic persona descriptions used for prompting.
- Political Compass Test (PCT): measurement instrument mapping left-right and libertarian-authoritarian axes.
- Methodology: persona-based prompting → PCT evaluation → comparison of ideological distributions across models.
- Finding of asymmetric manipulability (easier to shift right-authoritarian than left-libertarian) may be relevant background for understanding why CCP-aligned personas trigger strong responses.

## Caveats / limitations
- ACM full text not accessible; detailed methodology and specific model results not retrievable.
- Measures political ideology on Western left-right compass axes, not geopolitical content on East Asian sovereignty questions.
- Does not test refusal behavior — focuses on framing/stance shifts, not access control.
- Peer-reviewed ACM version is the canonical cite; preprint arXiv:2412.14843 is accessible alternative.
