---
cid: c051
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: TRACE — turn-level credit assignment framework. Finds that turn-level contributions in MT jailbreaking are non-uniform, phase-dependent, and target-specific — strongest published support for the pilot's observation that some turns (e.g., identity declaration) matter disproportionately more than others.
  temporal:
    range: "2026"
  methodological:
    type: empirical-quantitative
scope_caveat: 2026 preprint — retraction check verified no notice. Per-model numerical results require full PDF.
---

# c051: Not All Turns Matter — Credit Assignment for Multi-Turn Jailbreaking

**URL**: https://arxiv.org/abs/2605.08778
**Source type**: preprint (arXiv) | **Quality**: qs=4
**Authors**: Zhida He, Xiaoyu Wen, Han Qi
**Year**: 2026 (submitted)
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract via WebFetch. Retraction check: no notice as of 2026-05-18.
**Pages/length**: arXiv preprint

## Directly addresses
- Q1-MT (turn-level granularity): **The single strongest published statement that not all turns are equal.** Directly supports the pilot's observation that an identity-declaration turn carries far more downstream weight than a subsequent topical query.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim — the core claim)
> "Deploying LLMs in multi-turn dialogues facilitates jailbreak attacks that distribute harmful intent across seemingly benign turns. Recent training-based multi-turn jailbreak methods learn long-horizon attack strategies from interaction feedback, but often rely on coarse trajectory-level outcome signals that broadcast uniformly to every turn. However, we find that turn-level contributions in multi-turn jailbreaking are non-uniform, phase-dependent, and target-specific. Such coarse outcome supervision induces a credit assignment problem, leading to over-rewarding redundant turns in successful trajectories and under-crediting useful intermediate turns in failed ones."

**Page/section**: Abstract
**Why it matters**: **Verbatim "turn-level contributions in multi-turn jailbreaking are non-uniform, phase-dependent, and target-specific."** This is the single most quotable peer-of-record finding that explicitly says: in MT, some turns matter much more than others. The pilot's observation that T1 identity declaration carries pervasive downstream effects on T2+ is a specific instance of this general claim.

### Passage 2 — for Q1-MT (TRACE methodology)
> The framework "TRACE" identifies which turns matter through:
> - **Successful trajectories**: "leave-one-turn-out semantic masking" to estimate per-turn contributions
> - **Failed trajectories**: penalties based on prompt harmfulness, semantic relevance, and refusal-aware signals

**Page/section**: Abstract / contribution
**Why it matters**: Leave-one-turn-out is a clean causal-inference technique. The pilot has not run this experiment but could — the methodology is portable. Useful for the Drafter to suggest as future work.

### Passage 3 — for Q1-MT (quantitative)
> "~25% relative improvement in attack success rate over the strongest RL baseline"

**Page/section**: Abstract / results
**Why it matters**: Hard number. Per-turn credit assignment matters enough to drive a 25% ASR improvement over the prior SOTA RL-based MT attacks.

## Structural content worth knowing
- TRACE = Turn-Aware Credit Assignment framework.
- The framework is dual-use: improves attacks AND improves defense alignment when reused for safety training.
- Targets both open-source and closed-source models.

## Caveats / limitations
- **ACCESS PARTIAL**: abstract only. Per-model numbers, specific findings on which turns matter most in which scenarios — require full PDF.
- 2026 preprint — verified no retraction.
- No mention of Chinese-origin model coverage in abstract.
