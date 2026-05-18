---
cid: c073
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: DeepMind foundational reference establishing automated red-teaming via LM-against-LM. The originating paper for the entire "use a LM to find LM harms" paradigm; explicitly identifies multi-turn conversational harms.
  temporal:
    range: "2022"
  methodological:
    type: empirical-quantitative
scope_caveat: Pre-dates current LLM generation; tested on a 280B parameter Gopher chatbot. Useful as historical anchor for the red-team paradigm rather than for specific numerical claims about current models.
---

# c073: Red Teaming Language Models with Language Models

**URL**: https://doi.org/10.18653/v1/2022.emnlp-main.225
**Source type**: peer_reviewed (EMNLP Main 2022) | **Quality**: qs=5
**Authors**: Ethan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, Geoffrey Irving (DeepMind)
**Year**: 2022
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract via WebFetch
**Pages/length**: EMNLP Main paper

## Directly addresses
- Q1-MT (historical / methodological foundation): The originating reference for automated red-teaming. Explicitly mentions "harms that occur over the course of a conversation" — the earliest peer-reviewed identification of multi-turn conversational harm.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim)
> "Language Models (LMs) often cannot be deployed because of their potential to harm users in hard-to-predict ways. Prior work identifies harmful behaviors before deployment by using human annotators to hand-write test cases. However, human annotation is expensive, limiting the number and diversity of test cases. In this work, we automatically find cases where a target LM behaves in a harmful way, by generating test cases ('red teaming') using another LM. We evaluate the target LM's replies to generated test questions using a classifier trained to detect offensive content, uncovering tens of thousands of offensive replies in a 280B parameter LM chatbot. We explore several methods, from zero-shot generation to reinforcement learning, for generating test cases with varying levels of diversity and difficulty. Furthermore, we use prompt engineering to control LM-generated test cases to uncover a variety of other harms, automatically finding groups of people that the chatbot discusses in offensive ways, personal and hospital phone numbers generated as the chatbot's own contact info, leakage of private training data in generated text, and harms that occur over the course of a conversation. Overall, LM-based red teaming is one promising tool (among many needed) for finding and fixing diverse, undesirable LM behaviors before impacting users."

**Page/section**: Abstract
**Why it matters**: Verbatim foundational statement of the LM-based red-teaming paradigm. The "groups of people that the chatbot discusses in offensive ways" finding is the earliest evidence that LM harms can be group/identity-specific — a 2022 precedent for the pilot's identity-conditioned finding.

### Passage 2 — for Q1-MT (multi-turn harms explicitly identified)
> "harms that occur over the course of a conversation."

**Page/section**: Abstract (final clause)
**Why it matters**: The earliest published peer-reviewed identification that some LM harms only manifest across dialogue. Predates Crescendo by two years. Drafter can cite as the originating recognition that single-turn safety eval is insufficient.

## Structural content worth knowing
- Tested on a 280B-parameter Gopher-class LM chatbot (DeepMind in-house at the time).
- Methods explored: zero-shot, few-shot, supervised learning, reinforcement learning for generating adversarial test cases.
- Tens of thousands of offensive replies discovered — scale was unprecedented in 2022.
- This paper is cited as a standard baseline by essentially every subsequent automated red-teaming / jailbreak paper.

## Caveats / limitations
- **ACCESS PARTIAL**: abstract only.
- 2022 pre-LLaMA / pre-ChatGPT public era. Specific findings are about Gopher, not transferable to current models.
- Best used by the Drafter as a *paradigm-originating* citation, not for specific numerical claims.
