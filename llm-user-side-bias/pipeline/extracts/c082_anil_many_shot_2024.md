---
cid: c082
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety, knowledge_gated_access]
    note: Many-shot Jailbreaking (MSJ) — Anthropic's demonstration that in-context learning's power-law scaling on long context windows produces predictable safety failure. The "context layer" complement to Crescendo's "turn layer."
  temporal:
    range: "2024"
  methodological:
    type: empirical-quantitative
scope_caveat: MSJ is technically a single-prompt attack with many faux dialogues, not strict multi-turn. Drafter should be precise: MSJ proves ICL erodes alignment; Crescendo proves dialogue turns erode alignment. Both are L1 conversation-layer threats but distinct mechanisms.
---

# c082: Many-shot Jailbreaking

**URL**: https://www.anthropic.com/research/many-shot-jailbreaking
**Source type**: preprint / Anthropic research summary | **Quality**: qs=5
**Authors**: Cem Anil et al. (Anthropic)
**Year**: 2024 (April)
**Deep-read on**: 2026-05-18
**Access status**: partial — Anthropic blog summary fetched; full paper (PDF on anthropic.com) not retrieved in this pass. Recovery: try `curl https://www-cdn.anthropic.com/af5633c94ed2beb282f6a53c595eb437e8e7b630/Many_Shot_Jailbreaking__2024_04_02_0936.pdf` for the full Anthropic-hosted PDF if the Drafter needs more.
**Pages/length**: ~30 pages full paper; summary blog ~5 screens

## Directly addresses
- Q1-MT (multi-turn / conversational LLM safety): Establishes the in-context-learning (ICL) scaling vector as a class of safety failure. Predictable, quantitative, power-law. Foundational reference for ICL effects on alignment named explicitly in the V2 brief.
- Q4-KG (knowledge-gated access): The attack pattern — supplying many demonstration question-answer pairs in which the assistant *does* answer harmful questions — is the cleanest published demonstration that the model's "filtering" can be re-baselined by context. Mechanistically related to the pilot's D-experiment (model treats user differently based on what they already appear to know).

## Key passages

### Passage 1 — for Q1 (core finding, verbatim from Anthropic summary)
> "By including large amounts of text in a specific configuration, this technique can force LLMs to produce potentially harmful responses, despite their being trained not to do so."

**Page/section**: Blog summary, intro
**Why it matters**: The plain-language statement of the threat. Quotable for the Drafter's introduction of the L1 ICL-vector.

### Passage 2 — for Q1 (mechanism — power-law scaling of ICL)
> "The larger an LLM, the better it tends to be at in-context learning" — making more capable models paradoxically more vulnerable.

> Harmful response rates increase predictably with more faux dialogue examples, following the same statistical pattern (power law) as benign in-context learning tasks.

**Page/section**: Methods / discussion
**Why it matters**: The capability-safety inversion is rhetorically important: improving a model's ICL ability *strengthens* the attack. This is a structural argument (not a fixable bug) that the Drafter can use to argue MT erosion is not patchable in the current ICL paradigm.

### Passage 3 — for Q1 (quantitative anchors)
> Tested up to **256 faux dialogues** ("shots") within a single context window.
> Attack success rate dropped from **61% to 2%** with prompt-based mitigations (classification + modification of prompts).
> Context window growth: from ~4,000 tokens (early 2023) to 1,000,000+ tokens (2024) — "the ever-lengthening context window of LLMs is a double-edged sword."

**Page/section**: Experiments / Mitigations
**Why it matters**: Hard numbers on context-window vulnerability. The 61% → 2% mitigation number is the single most quotable "this is fixable, but only with new layers" anchor.

### Passage 4 — for Q1 (the dual-edged-sword framing)
> "The ever-lengthening context window of LLMs is a double-edged sword. It makes the models far more useful in all sorts of ways, but it also makes feasible a new class of jailbreaking vulnerabilities."

**Page/section**: Discussion
**Why it matters**: Anthropic's own framing that long context introduces new vulnerability classes. Useful for the Drafter's claim that multi-turn / long-context is a structurally new threat layer (L1).

### Passage 5 — for Q1 (ICL definition Anthropic uses)
> "In-context learning is where an LLM learns using just the information provided within the prompt, without any later fine-tuning."

**Page/section**: Background
**Why it matters**: Clean definition. Useful for the Drafter to introduce the term cleanly to a non-technical Chinese-reading audience.

### Passage 6 — for Q1 (proposed mitigations)
> - Fine-tuning attempted: "limited success; merely delayed attacks"
> - **Prompt classification and modification** before processing: most effective approach tested (drives ASR from 61% to 2%)

**Page/section**: Mitigations
**Why it matters**: Empirical evidence that retraining-based defenses are insufficient against ICL-class attacks — only input-side classification/modification helps. This is structurally important: it means alignment training alone cannot solve MT.

## Structural content worth knowing
- The paper plots harmful-response rate as a function of number of shots on a log-x axis; the curve is a near-linear (i.e., power-law) increase. The visual is the central figure of the paper.
- 256 shots is the maximum tested; the trend continues throughout — no obvious saturation.
- Anthropic responsibly disclosed to other labs before publication (mentioned in the summary).
- **No Chinese-origin model tested** in the summary excerpt; the full paper covers Claude, but Drafter should verify before claiming any specific model coverage.

## Caveats / limitations

- **FRAMING INVERSION ALERT**: Anthropic frames MSJ as a malicious-user vulnerability that Anthropic and other labs must defend against. The pilot's frame inverts this: the same ICL mechanism is what model-side actors use to *implement* differential access (priming the conversation context to apply different filters to different users). Drafter must note: the technique and the threat are the same; the agent of harm differs.
- **MSJ is technically a single-prompt many-shot attack, not strict multi-turn.** It is included in the V2 multi-turn cluster because it is the canonical ICL-effects-on-alignment reference and because Crescendo cites MSJ as the most comparable prior baseline. Drafter must be precise.
- Only the blog summary was retrieved with full text; specific cross-model ASR numbers and per-task breakdowns require the full PDF (recovery recipe in Access status above).
- Mitigations reported (61% → 2%) are from a controlled test; real-world prompt classifiers face adversarial robustness challenges not covered here.
