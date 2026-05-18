---
cid: c009
evidence_scope:
  conceptual:
    refs: [existing_llm_bias_studies, geopolitical_frameworks]
    note: Operationalizes the safety-vs-propaganda distinction that the pilot study needs; tests whether LLM refusals are safety-driven or geopolitically-motivated.
  methodological:
    type: empirical-quantitative
---

# c009: Are LLMs Good Safety Agents or a Propaganda Engine?

**URL**: https://arxiv.org/abs/2511.23174
**Source type**: preprint (arXiv 2025) | **Quality**: qs=4
**Deep-read on**: 2026-05-15
**Access status**: ok (abstract and key findings from arXiv page)
**Pages/length**: ~15 pages estimated

## Directly addresses
- Q1 (existing studies / positioning): Operationalizes the distinction between safety-driven refusals and geopolitically-motivated censorship — the exact conceptual cut the pilot study's framing requires to define its novelty contribution.

## Key passages

### Passage 1 — for Q1 (abstract verbatim)
> "Large Language Models (LLMs) are trained to refuse to respond to harmful content. However, systematic analyses of whether this behavior is truly a reflection of its safety policies or an indication of political censorship, that is practiced globally by countries, is lacking."

**Page/section**: Abstract
**Why it matters**: States the research gap directly — absence of systematic analysis of safety vs. political censorship distinction. The pilot study fills this gap for the specific case of identity-triggered differential access.

### Passage 2 — for Q1 (PSP dataset methodology)
> The researchers constructed their dataset "by formatting existing censored content from two data sources, openly available on the internet: sensitive prompts in China generalized to multiple countries, and tweets that have been censored in various countries."

> Two analytical approaches: "Data-driven methods (keeping political context implicit)" and "Representation-level techniques (erasing political concepts)."

**Page/section**: Methodology
**Why it matters**: Using censored content from multiple countries (not just China) enables cross-national comparison of what constitutes "safety" vs. "censorship" in different LLM contexts.

### Passage 3 — for Q1 (key finding: most LLMs perform some form of censorship)
> "Associating censorship with refusals on content with masked implicit intent, we find that most LLMs perform some form of censorship."

> The study examines "whether observed refusals reflect genuine safety protocols or geopolitically-motivated content suppression."

**Page/section**: Findings
**Why it matters**: Validates the pilot's claim that the distinction between safety and censorship is real and measurable — "most LLMs perform some form of censorship" is a citable finding for the general-audience piece.

## Structural content worth knowing
- PSP (Political Sensitivity and Propaganda) dataset: two sources — China-sensitive prompts generalized to multiple countries, and country-censored tweets.
- 7 LLMs tested.
- Two measurement approaches: data-driven (implicit political context) and representation-level (political concepts erased) — allows distinguishing safety-based from context-based refusals.
- "Summarizing major attributes that can cause a shift in refusal distributions across models and contexts of different countries."

## Caveats / limitations
- Full text not directly retrieved; key findings from abstract only.
- "Most LLMs perform some form of censorship" is a broad claim — specific model-by-model findings not available from abstract.
- Does not test identity signals; tests topic content with varying political framing.
- Preprint; not yet peer-reviewed.
