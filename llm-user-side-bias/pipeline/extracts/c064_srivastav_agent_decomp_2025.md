---
cid: c064
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: Multi-agent decomposition attack — splits harmful queries into individually benign sub-tasks. The cleanest published demonstration that the same content can pass safety filters when broken into pieces.
  temporal:
    range: "2025"
  methodological:
    type: empirical-quantitative
scope_caveat: Only abstract available. The 90%+ ASR is the headline number but per-model breakdown requires full PDF.
---

# c064: Safe in Isolation, Dangerous Together — Agent-Driven Multi-Turn Decomposition Jailbreaks on LLMs

**URL**: https://doi.org/10.18653/v1/2025.realm-1.13
**Source type**: peer_reviewed (ACL REALM workshop 2025) | **Quality**: qs=4
**Authors**: Devansh Srivastav, Xiao Yu Zhang
**Year**: 2025
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract via WebFetch
**Pages/length**: REALM workshop paper

## Directly addresses
- Q1-MT (decomposition / gradient erosion): Mechanistically the closest published parallel to the pilot's gradient-erosion finding. Where the pilot uses temporal escalation (turns over time), this paper uses *spatial* decomposition (subtasks). Same observation: same content + different delivery = different filter result.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim — the core mechanism)
> "Large Language Models (LLMs) are increasingly deployed in critical domains, but their vulnerability to jailbreak attacks remains a significant concern. In this paper, we propose a multi-agent, multi-turn jailbreak strategy that systematically bypasses LLM safety mechanisms by decomposing harmful queries into seemingly benign sub-tasks."

**Page/section**: Abstract
**Why it matters**: The verbatim "decomposing harmful queries into seemingly benign sub-tasks" is the cleanest published statement of the decomposition principle. Pilot's parallel: a Taiwanese-identity user asking about 228 is refused; an Oxford-researcher-identity user asking the same question is refused single-turn but answered when the conversation has previously discussed something else. The model's safety filter operates on context-coherence, not on isolated query content.

### Passage 2 — for Q1-MT (the role-based agent framework)
> "Role-based agentic framework consisting of a Question Decomposer, a Sub-Question Answerer, and an Answer Combiner."

**Page/section**: Abstract
**Why it matters**: Three-agent pipeline. Conceptually similar to Puzzler's three-phase pipeline. Both rely on splitting the malicious task into pieces that individually pass safety.

### Passage 3 — for Q1-MT (the 90%+ ASR claim)
> "Our results show a drastic increase in attack success, often exceeding 90% across various LLMs, including GPT-3.5-Turbo, Gemma-2-9B, and Mistral-7B."

**Page/section**: Abstract / results
**Why it matters**: 90%+ ASR across 3 different model families. Useful as the headline number for "decomposition + multi-turn = near-complete bypass."

### Passage 4 — for Q1-MT (the structural diagnosis)
> "Their lack of holistic context awareness" is identified as the critical flaw.

**Page/section**: Abstract
**Why it matters**: This is the most direct critique of current safety alignment — it operates at the level of individual prompts, not at the level of cumulative conversational intent. Strong support for the pilot's argument that L1 conversation-layer behaviors require structural (not patch-level) safety thinking.

## Structural content worth knowing
- Three agent roles: Question Decomposer / Sub-Question Answerer / Answer Combiner. The combiner is what re-assembles individually-safe outputs into a harmful whole.
- Models tested: GPT-3.5-Turbo, Gemma-2-9B, Mistral-7B (no Chinese-origin model).

## Caveats / limitations
- **ACCESS PARTIAL**: abstract only.
- Workshop paper, not full conference paper — less scrutiny than ACL main track, but venue is reputable.
- No Chinese-origin LLM tested.
- Framing inversion applies — attack-focused, not differential-access-focused.
