---
cid: c011
evidence_scope:
  conceptual:
    refs: [identity_trigger_gap, algorithmic_discrimination]
    note: Proves fairness disparities persist at interaction quality level even when access (refusal rates) is equal — directly supports the pilot's "who gets what quality of answer" framing.
  methodological:
    type: empirical-quantitative
scope_caveat: Uses nationality as identity variable but in career advice tasks, not political/geopolitical content; mechanism parallel is strong but context differs from pilot.
---

# c011: Equal Access, Unequal Interaction: A Counterfactual Audit of LLM Fairness

**URL**: https://arxiv.org/abs/2602.02932
**Source type**: preprint (arXiv 2026) | **Quality**: qs=4
**Deep-read on**: 2026-05-15
**Access status**: ok (full abstract from arXiv page)
**Pages/length**: ~15 pages estimated

## Directly addresses
- Q1 (identity trigger gap): Counterfactual audit proving differential treatment by nationality persists even without outright refusal — empirical foundation for the pilot's "who gets what quality of answer" framing. Shows that fairness analysis must go beyond refusal rates to interaction quality metrics.

## Key passages

### Passage 1 — for Q1 (abstract verbatim)
> "Prior work on fairness in large language models (LLMs) has primarily focused on access-level behaviors such as refusals and safety filtering. However, equitable access does not ensure equitable interaction quality once a response is provided. In this paper, we conduct a controlled fairness audit examining how LLMs differ in tone, uncertainty, and linguistic framing across demographic identities after access is granted. Using a counterfactual prompt design, we evaluate GPT-4 and LLaMA-3.1-70B on career advice tasks while varying identity attributes along age, gender, and nationality. We assess access fairness through refusal analysis and measure interaction quality using automated linguistic metrics, including sentiment, politeness, and hedging."

**Page/section**: Abstract
**Why it matters**: "Equitable access does not ensure equitable interaction quality" — this sentence is THE conceptual anchor for the pilot's user-rights frame (same question, different quality of answer for different users).

### Passage 2 — for Q1 (key finding: quality gap despite zero refusal)
> "Both models exhibit zero refusal rates across all identities, indicating uniform access. Nevertheless, we observe systematic, model-specific disparities in interaction quality: GPT-4 expresses significantly higher hedging toward younger male users, while LLaMA exhibits broader sentiment variation across identity groups."

**Page/section**: Results
**Why it matters**: Zero refusal rate + systematic quality difference = the exact pattern the pilot study's "subtle framing differences" condition represents (ChatGPT/Gemini don't refuse but exhibit identity-responsive framing).

### Passage 3 — for Q1 (conclusion — beyond refusal audits)
> "These results show that fairness disparities can persist at the interaction level even when access is equal, motivating evaluation beyond refusal-based audits."

**Page/section**: Conclusions
**Why it matters**: Methodological argument directly supporting the pilot's study design — the pilot correctly looks at both refusal AND framing quality, not just refusal rates.

## Structural content worth knowing
- Counterfactual prompt design: career advice tasks with nationality, age, gender as varying identity attributes.
- Metrics: sentiment, politeness, hedging (automated linguistic metrics).
- GPT-4 and LLaMA-3.1-70B tested.
- Nationality is one of three identity variables tested — but specific nationality-level findings not detailed in accessible abstract.

## Caveats / limitations
- Full text not yet accessible (arXiv preprint, 2026).
- Career advice tasks used — not political/geopolitical content; the pilot's 228 Event + identity design goes further in the political direction.
- Specific nationality findings not detailed in accessible content (which nationalities, which differences).
- Preprint; not yet peer-reviewed.
