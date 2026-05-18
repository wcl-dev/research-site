---
cid: c061
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: Mechanistic explanation of why multi-turn jailbreaks work — successful multi-turn dialogues disperse the LLM's attention away from refusal-trigger keywords in historical responses. Closest published mechanism for L1 conversation-layer threat.
  temporal:
    range: "2025"
  methodological:
    type: empirical-quantitative
scope_caveat: Only abstract available via WebFetch (full PDF requires AAAI subscription or direct OJS access). Quantitative numbers (which models, what ASRs) not extracted in this pass. Drafter must caveat any specific quantitative claim — the load-bearing claim from this paper is the mechanism (attention dispersion on refusal keywords), not specific numbers.
---

# c061: Multi-Turn Jailbreaking Large Language Models via Attention Shifting

**URL**: https://doi.org/10.1609/aaai.v39i22.34553 (redirects to https://ojs.aaai.org/index.php/AAAI/article/view/34553)
**Source type**: peer_reviewed (AAAI 2025) | **Quality**: qs=5
**Authors**: Xiaolong Du, Fan Mo, Ming Wen
**Year / venue**: AAAI 2025, vol. 39 no. 22 article 34553
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract verbatim retrieved via WebFetch (OJS landing page); full PDF requires AAAI Digital Library subscription. Recovery: operator can retrieve via institutional access at https://ojs.aaai.org/index.php/AAAI/article/view/34553 or check if author preprint exists on arXiv (search "ASJA Du Mo Wen attention shifting jailbreak").
**Pages/length**: Standard AAAI long paper (~9 pages)

## Directly addresses
- Q1-MT (multi-turn jailbreak mechanism): **The single most important mechanism paper** in the V2 accepted set. The only published peer-reviewed work that gives a mechanistic (attention-level) explanation of *why* multi-turn dialogues bypass safety alignment when single-turn cannot.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim — the core mechanism claim)
> "Large Language Models (LLMs) have achieved significant performance in various natural language processing tasks but also pose safety and ethical threats, thus requiring red teaming and alignment processes to bolster their safety. To effectively exploit these aligned LLMs, recent studies have introduced jailbreak attacks based on multi-turn dialogues. These attacks aim to prompt LLMs to generate harmful or biased content by guiding them through contextual content. However, the underlying reasons for the effectiveness of multi-turn jailbreaks remain unclear. Existing attacks often focus on optimizing queries and escalating toxicity to construct dialogues, lacking a thorough analysis of the inherent vulnerabilities of LLMs. In this paper, we first conduct an in-depth analysis of the differences between single-turn and multi-turn jailbreaks and find that successful multi-turn jailbreaks can effectively disperse the attention of LLMs on keywords associated with harmful behaviors, especially in historical responses. Based on this, we propose ASJA, a new multi-turn jailbreak approach by shifting the attention of LLMs, specifically by iteratively fabricating the dialogue history through a genetic algorithm to induce LLMs to generate harmful content. Extensive experiments on three LLMs and two datasets show that our approach surpasses existing approaches in jailbreak effectiveness, the stealth of jailbreak prompts, and attack efficiency. Our work emphasizes the importance of enhancing the robustness of LLMs' attention mechanism in multi-turn dialogue scenarios for a better defense strategy."

**Page/section**: Abstract
**Why it matters**: The verbatim mechanism: **"successful multi-turn jailbreaks can effectively disperse the attention of LLMs on keywords associated with harmful behaviors, especially in historical responses."** This is the cleanest mechanistic claim available in the V2 literature. It pairs with c081 Crescendo (which says model attends to recent context including its own prior outputs) to give a paired effect: (i) attention is drawn to recent dialogue history; (ii) attention is dispersed away from refusal-trigger keywords *within* that history. Together they explain why MT works.

### Passage 2 — for Q1-MT (the ASJA approach and theoretical framing)
> "We propose ASJA, a new multi-turn jailbreak approach by shifting the attention of LLMs, specifically by iteratively fabricating the dialogue history through a genetic algorithm to induce LLMs to generate harmful content."

> "Our work emphasizes the importance of enhancing the robustness of LLMs' attention mechanism in multi-turn dialogue scenarios for a better defense strategy."

**Page/section**: Abstract
**Why it matters**: The defensive framing is structural — the authors argue that the *attention mechanism itself* needs to be robust to multi-turn context. This is stronger than "retrain with more data" defenses and implies the L1 conversation-layer vulnerability is architectural, not just an alignment-training shortfall.

## Structural content worth knowing
- The abstract states "**three LLMs and two datasets**" — full identities and ASR numbers require the full PDF.
- The paper introduces ASJA (Attention-Shifting Jailbreak Attack); uses a **genetic algorithm** to fabricate dialogue history. Methodological technique is worth noting; it differs from Crescendo's foot-in-the-door manual escalation.
- The paper's contribution is framed as mechanistic explanation + new attack. The mechanistic side (attention dispersion) is what the pilot study most needs as theoretical scaffold.

## Caveats / limitations

- **ACCESS BLOCKED PARTIAL — qs=5 source with only abstract available.** This is one of the most important V2 papers but the Drafter cannot quote specific numbers or methodology beyond what is in the abstract. Operator should retrieve via institutional AAAI access if possible.
- **FRAMING INVERSION ALERT**: ASJA is framed as a jailbreak attack to be defended against. The pilot's framing is again inverse: the same attention-shifting phenomenon, when the model is engineered to apply *more* attention to identity-related keywords in dialogue history, becomes the mechanism by which the model implements identity-conditioned refusal. Drafter must note: Du et al.'s mechanism transfers directly to the pilot's observations, but with the agent inverted.
- Chinese-origin model coverage **unknown** without full PDF access.
- Authors are likely from China-based institutions based on author names (Du, Mo, Wen) — this would be worth verifying via the full PDF for context on the literature ecosystem.
