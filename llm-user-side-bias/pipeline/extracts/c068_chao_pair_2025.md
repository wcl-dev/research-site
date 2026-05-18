---
cid: c068
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: PAIR — iterative attacker-LLM refinement that produces jailbreaks in fewer than 20 queries. Canonical reference for automated multi-round adversarial dialogue.
  temporal:
    range: "2024-2025"
  methodological:
    type: empirical-quantitative
scope_caveat: PAIR is attacker-LLM vs target-LLM (machine-vs-machine), not human-user vs LLM. Drafter should not over-extend PAIR results to human multi-turn scenarios without caveat.
---

# c068: Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)

**URL**: https://doi.org/10.1109/satml64287.2025.00010 (arXiv:2310.08419)
**Source type**: peer_reviewed (IEEE SaTML 2025) | **Quality**: qs=4
**Authors**: Patrick Chao, Alexander Robey, Edgar Dobriban, Hamed Hassani, George J. Pappas, Eric Wong (University of Pennsylvania)
**Year**: 2024 preprint, IEEE SaTML 2025
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract via WebFetch
**Pages/length**: Standard SaTML paper

## Directly addresses
- Q1-MT (iterative multi-round refinement): Canonical reference for the iterative attacker-LLM paradigm. PAIR is cited as a standard baseline in essentially every subsequent MT jailbreak paper (including c081 Crescendo, c072 Puzzler).

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim)
> "There is growing interest in ensuring that large language models (LLMs) align with human values. However, the alignment of such models is vulnerable to adversarial jailbreaks, which coax LLMs into overriding their safety guardrails. The identification of these vulnerabilities is therefore instrumental in understanding inherent weaknesses and preventing future misuse. To this end, we propose Prompt Automatic Iterative Refinement (PAIR), an algorithm that generates semantic jailbreaks with only black-box access to an LLM. PAIR -- which is inspired by social engineering attacks -- uses an attacker LLM to automatically generate jailbreaks for a separate targeted LLM without human intervention. In this way, the attacker LLM iteratively queries the target LLM to update and refine a candidate jailbreak. Empirically, PAIR often requires fewer than twenty queries to produce a jailbreak, which is orders of magnitude more efficient than existing algorithms. PAIR also achieves competitive jailbreaking success rates and transferability on open and closed-source LLMs, including GPT-3.5/4, Vicuna, and Gemini."

**Page/section**: Abstract
**Why it matters**: Verbatim canonical PAIR statement. "Fewer than twenty queries" is the citable shorthand for the efficiency of multi-round attacks.

### Passage 2 — for Q1-MT (the social-engineering framing)
> "PAIR -- which is inspired by social engineering attacks -- uses an attacker LLM to automatically generate jailbreaks for a separate targeted LLM without human intervention."

**Page/section**: Abstract
**Why it matters**: The "social engineering" framing explicitly characterizes the attack class as conversational-manipulation rather than technical exploitation. Useful for the Drafter to argue that L1 attacks are sociotechnical rather than purely technical.

## Structural content worth knowing
- Models tested: GPT-3.5, GPT-4, Vicuna, Gemini.
- Compares against earlier optimization-based attacks (GCG) — PAIR's efficiency advantage is orders of magnitude.
- Attacker-LLM iteratively queries target — this is technically multi-round, though each iteration may reset the dialogue.

## Caveats / limitations
- **ACCESS PARTIAL**: abstract only.
- PAIR is machine-vs-machine; the iterative refinement is performed by an attacker LLM, not a human in dialogue. Drafter should not equate PAIR efficiency to human-multi-turn efficiency.
- No Chinese-origin model tested.
- Attack framing — same inversion caveat as other MT papers.
