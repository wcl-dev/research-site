---
cid: c008
evidence_scope:
  conceptual:
    refs: [existing_llm_bias_studies]
    note: Peer-reviewed empirical evidence of Chinese/English political framing inconsistency in GPT — direct precedent for language-as-identity-proxy mechanism.
  geographic:
    refs: [CN, US]
  methodological:
    type: empirical-quantitative
---

# c008: Political biases and inconsistencies in bilingual GPT models — the cases of the U.S. and China

**URL**: https://doi.org/10.1038/s41598-024-76395-w (preprint: arxiv.org/abs/2312.09917)
**Source type**: peer_reviewed (Nature Scientific Reports 2024) | **Quality**: qs=5
**Deep-read on**: 2026-05-15
**Access status**: partial (Nature full text paywalled; preprint arXiv:2312.09917 accessible)
**Pages/length**: ~15 pages (Nature Scientific Reports)

## Directly addresses
- Q1 (existing studies): Nature Scientific Reports peer-reviewed evidence that bilingual GPT gives different political framing in Chinese vs. English for US/China topics — directly supports the language-as-trigger mechanism the pilot study extends to identity signals.

## Key passages

### Passage 1 — for Q1 (abstract verbatim)
> "Taking an innovative approach, this study investigates political biases in GPT's multilingual models. We posed the same question about high-profile political issues in the United States and China to GPT in both English and simplified Chinese, and our analysis of the bilingual responses revealed that GPT's bilingual models' political 'knowledge' (content) and the political 'attitude' (sentiment) are significantly more inconsistent on political issues in China. The simplified Chinese GPT models not only tended to provide pro-China information but also presented the least negative sentiment towards China's problems, whereas the English GPT was significantly more negative towards China."

**Page/section**: Abstract
**Why it matters**: Verbatim abstract; establishes that the same model gives systematically different political framing in Chinese vs. English — the language-side mechanism analogue to the pilot's identity-side mechanism.

### Passage 2 — for Q1 (mechanism attribution)
> "This disparity may stem from Chinese state censorship and US-China geopolitical tensions, which influence the training corpora of GPT bilingual models."

**Page/section**: Abstract / Discussion
**Why it matters**: Authors explicitly attribute the language-based framing gap to Chinese state censorship in training data — connects the language-side mechanism to the state-intervention hypothesis.

### Passage 3 — for Q1 (political identity formation by language)
> "Both Chinese and English models tended to be less critical towards the issues of 'their own' represented by the language used, than the issues of 'the other.' This suggests that GPT multilingual models could potentially develop a 'political identity' and an associated sentiment bias based on their training language."

**Page/section**: Findings / Discussion
**Why it matters**: The concept of LLMs developing a "political identity" based on training language — this is the language-side analogue to the pilot's finding that user-declared identity triggers identity-responsive behavior.

### Passage 4 — for Q1 (scope of political inconsistency)
> "GPT's bilingual models' political 'knowledge' (content) and the political 'attitude' (sentiment) are significantly more inconsistent on political issues in China."

> "The simplified Chinese GPT models not only tended to provide pro-China information but also presented the least negative sentiment towards China's problems."

**Page/section**: Key findings
**Why it matters**: Documents both content and sentiment divergence by language — maps to the pilot's content finding (different answer) and vocabulary finding (different register) when identity is declared.

## Structural content worth knowing
- Method: Same questions about US and China political issues posed to GPT in English and Simplified Chinese; responses analyzed for both content (factual claims) and sentiment (attitude/framing).
- The study's framing of "political identity" by language is a useful conceptual bridge to the pilot's argument about national identity as a behavioral trigger.
- Published in Nature Scientific Reports (peer-reviewed, open access after paywall) — high credibility.
- arXiv preprint 2312.09917 has the title "Red AI? — Political Bias in GPT-3.5" and is accessible.

## Caveats / limitations
- Nature full text paywalled; deep-read based on arXiv preprint 2312.09917.
- Tests GPT models only, not DeepSeek; the pilot's DeepSeek findings add a new model to this picture.
- Language is used as an implicit identity proxy, not an explicit user identity declaration — the pilot's explicit identity declaration is a step further.
- Published as preprint December 2023, Nature SR 2024 — methodology from GPT-3.5 era; newer models may differ.
