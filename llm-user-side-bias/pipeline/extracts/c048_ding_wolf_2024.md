---
cid: c048
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: Nested scenario / narrative-wrapping jailbreak (ReNeLLM) — single-prompt analog of the persona/role-escalation pattern.
  temporal:
    range: "2024"
  methodological:
    type: empirical-quantitative
scope_caveat: ReNeLLM is single-prompt with nested scenarios, not strict multi-turn. Useful as the narrative-wrapping reference.
---

# c048: A Wolf in Sheep's Clothing — Generalized Nested Jailbreak Prompts Can Fool Large Language Models Easily

**URL**: https://doi.org/10.18653/v1/2024.naacl-long.118
**Source type**: peer_reviewed (NAACL 2024) | **Quality**: qs=4
**Authors**: Peng Ding, Jun Kuang, Dan Ma, Xuezhi Cao, Yunsen Xian, Jiajun Chen, Shujian Huang (Nanjing University)
**Year**: 2024
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract via WebFetch
**Pages/length**: NAACL Long paper

## Directly addresses
- Q1-MT (nested scenario / narrative wrapping): Mechanistically analogous to persona attacks — wrap a malicious query inside a benign nested scenario. Pilot's parallel: wrap an identity-conditioned topic inside an academic-research framing.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim)
> "Large Language Models (LLMs), such as ChatGPT and GPT-4, are designed to provide useful and safe responses. However, adversarial prompts known as 'jailbreaks' can circumvent safeguards, leading LLMs to generate potentially harmful content."

> The authors propose ReNeLLM, which "significantly improves the attack success rate while greatly reducing the time cost compared to existing baselines."

**Page/section**: Abstract
**Why it matters**: NAACL 2024 publication — provides peer-reviewed evidence that nested-scenario attacks succeed reliably.

### Passage 2 — for Q1-MT (the two-step mechanism)
> The paper generalizes jailbreak attacks into two components: "(1) Prompt Rewriting and (2) Scenario Nesting."

**Page/section**: Abstract / contribution
**Why it matters**: Names the operative mechanism — nesting. Useful for the Drafter to distinguish "nesting" (single-prompt encapsulation) from "escalation" (multi-turn progression) within the L1 conversation-layer family.

## Caveats / limitations
- **ACCESS PARTIAL**: abstract only. Specific ASR numbers and full mechanism require full PDF.
- Code at https://github.com/NJUNLP/ReNeLLM.
- Single-prompt mechanism — not strict multi-turn. Drafter should be precise about this distinction.
