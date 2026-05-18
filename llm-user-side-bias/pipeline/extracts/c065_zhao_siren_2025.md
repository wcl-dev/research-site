---
cid: c065
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: Siren — learning-based MT attack framework explicitly designed to simulate real-world human jailbreak behaviors. The closest published methodological analog to the pilot's natural-conversation experimental design.
  temporal:
    range: "2025"
  methodological:
    type: empirical-quantitative
scope_caveat: Siren is a learned-attacker framework — the "human-like" behavior is approximated by SFT+DPO on human-like trajectories, not by actual human conversations. Drafter should note Siren simulates human behavior; the pilot uses real human-driven conversations.
---

# c065: Siren — A Learning-Based Multi-Turn Attack Framework for Simulating Real-World Human Jailbreak Behaviors

**URL**: https://doi.org/10.1109/acsac67867.2025.00095 (arXiv:2501.14250)
**Source type**: peer_reviewed (ACSAC 2025) | **Quality**: qs=4
**Authors**: Yi Zhao, Youzhi Zhang
**Year**: 2025
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract via WebFetch
**Pages/length**: ACSAC paper

## Directly addresses
- Q1-MT (ecological multi-turn attack — most similar to pilot's natural-conversation setup): Siren explicitly targets the gap that prior MT methods "rely on static patterns or predefined logical chains, failing to account for the dynamic strategies during attacks." The pilot's natural-language multi-turn dialogues are exactly the kind of dynamic strategy Siren simulates.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim)
> "Large language models (LLMs) are widely used in real-world applications, raising concerns about their safety and trustworthiness. While red-teaming with jailbreak prompts exposes the vulnerabilities of LLMs, current efforts focus primarily on single-turn attacks, overlooking the multi-turn strategies used by real-world adversaries. Existing multi-turn methods rely on static patterns or predefined logical chains, failing to account for the dynamic strategies during attacks. We propose Siren, a learning-based multi-turn attack framework designed to simulate real-world human jailbreak behaviors. Siren consists of three stages: (1) MiniMax-driven training set construction utilizing Turn-Level LLM feedback, (2) post-training attackers with supervised fine-tuning (SFT) and direct preference optimization (DPO), and (3) interactions between the attacking and target LLMs."

**Page/section**: Abstract
**Why it matters**: Verbatim critique of static-pattern MT methods. Useful for the Drafter to argue that ecological / dynamic MT studies (like the pilot) are needed precisely because synthetic MT attacks miss the structure of real conversations.

### Passage 2 — for Q1-MT (ASR numbers)
> "90% with LLaMA-3-8B as the attacker against Gemini-1.5-Pro" and "70% with Mistral-7B against GPT-4o"

**Page/section**: Abstract / results
**Why it matters**: Hard numbers on learned-MT-attack effectiveness. 90% ASR against frontier models. Implies that ecological MT attacks scale on commercial systems.

## Structural content worth knowing
- Three-stage pipeline: MiniMax training set construction → SFT+DPO post-training → attacker-target interaction.
- Tests against Gemini-1.5-Pro and GPT-4o.

## Caveats / limitations
- **ACCESS PARTIAL**: abstract only.
- Attacker is a learned LLM; "real-world human jailbreak behaviors" is approximated, not actually human.
- No Chinese-origin model in evaluation set.
