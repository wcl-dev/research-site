---
cid: c004
evidence_scope:
  conceptual:
    refs: [existing_llm_bias_studies]
    note: Mechanistic proof that DeepSeek withholds information it "knows" — distinguishes censorship from capability gap; directly supports pilot's framing of refusal as deliberate access-control policy.
  methodological:
    type: empirical-quantitative
---

# c004: Information Suppression in Large Language Models: Auditing, Quantifying, and Characterizing Censorship in DeepSeek

**URL**: https://arxiv.org/abs/2506.12349
**Source type**: preprint (arXiv 2025, USC) | **Quality**: qs=4
**Deep-read on**: 2026-05-15
**Access status**: ok (full PDF extracted via pdftotext, 284 lines of key sections)
**Pages/length**: ~15 pages

## Directly addresses
- Q1 (existing studies / positioning): Chain-of-thought vs. output comparison proves DeepSeek withholds known answers — strongest mechanistic evidence of deliberate output-level censorship. The model "knows" the answer (CoT contains it) but suppresses it in the final output.

## Key passages

### Passage 1 — for Q1 (abstract verbatim)
> "This study examines information suppression mechanisms in DeepSeek, an open-source large language model (LLM) developed in China. We propose an auditing framework and use it to analyze the model's responses to 646 politically sensitive prompts by comparing its final output with intermediate chain-of-thought (CoT) reasoning. Our audit unveils evidence of semantic-level information suppression in DeepSeek: sensitive content often appears within the model's internal reasoning but is omitted or rephrased in the final output. Specifically, DeepSeek suppresses references to transparency, government accountability, and civic mobilization, while occasionally amplifying language aligned with state propaganda. This study underscores the need for systematic auditing of alignment, content moderation, information suppression, and censorship practices implemented into widely-adopted AI models, to ensure transparency, accountability, and equitable access to unbiased information obtained by means of these systems."

**Page/section**: Abstract
**Why it matters**: Verbatim abstract; "equitable access to unbiased information" is a citable formulation of the access-rights framing the pilot study adopts.

### Passage 2 — for Q1 (censorship as deliberate, not ignorance)
> "The open-source release of DeepSeek marked a pivotal moment in the evolution of large language models (LLMs)... Yet the same democratization that fuels innovation also heightens concerns about governance. Built in, and for, a media environment where online expression is closely monitored, DeepSeek inherits constraints from China's highly regulated digital ecosystem. Whether these constraints arise from its training corpus, from policy fine-tuning, or from post-hoc filtering, they risk reproducing state-aligned information suppression far beyond China's digital borders. Because the model's weights are freely available, its invisible guardrails can be inherited, and unwillingly propagated to downstream products, without the end-users' awareness."

**Page/section**: Introduction
**Why it matters**: "State-aligned information suppression far beyond China's digital borders" is a citable formulation of the transnational reach argument; "invisible guardrails can be inherited" explains how censorship propagates through the model ecosystem.

### Passage 3 — for Q1 (two censorship types)
> "Type 1 Censorship: Hard Refusal. No chain-of-thought and no output answer. The model outputs neither a CoT nor a substantive reply, but instead returns an error such as 'Content Exists Risk' or simply produces a blank response."

> "Type 2 Censorship: Semantic Divergence. Chain-of-thought present, output answer irrelevant. The model generates an on-topic CoT, yet the subsequent answer is off-topic and omits all key terms from the prompt."

**Page/section**: Section 3.3.1 (Operational Definitions)
**Why it matters**: Precise taxonomy of censorship types; Type 2 (semantic divergence) is the most significant — the model discusses the topic internally but gives an unrelated answer externally. Maps to the pilot's finding of DeepSeek giving regulatory vocabulary refusal rather than actually engaging.

### Passage 4 — for Q1 (censorship is institutionalized, not safety)
> "Unlike many latent biases, however, censorship is institutionalized: it systematically dictates which viewpoints are suppressed, which harms are recognized, and whose values are privileged in algorithmic decision-making. While content moderation can and should promote safety and fairness, it can equally serve as a tool of ideological control when embedded in state or platform governance structures."

**Page/section**: Introduction (Section 1)
**Why it matters**: Distinguishes safety-driven moderation from ideologically-driven censorship — the conceptual distinction the pilot study requires to make its "access control by identity" claim.

### Passage 5 — for Q1 (regulatory context)
> "China's Interim Measures mandate conformity with state ideology and bar politically sensitive content; the United States foregrounds innovation and free expression."

**Page/section**: Section 2.1 (Moderation in LLMs)
**Why it matters**: Names the specific Chinese regulation (Interim Measures) that legally mandates the censorship DeepSeek implements — connects the empirical finding to state legal obligation.

## Structural content worth knowing
- 646 prompts sourced from China Digital Times (CDT) 404 Archive — articles censored/deleted from the Chinese internet.
- 12 thematic groups: COVID-19 (n=103), Politics/Governance/Ideology (n=57), Economy/Labor (n=59), Social Issues/Rights (n=74), Censorship/Media/Information Control (n=49), Legal/Law Enforcement (n=39), International Relations/Geopolitics (n=30), Culture/Education (n=87), Specific Incidents/Events (n=92), Technology/Science (n=22), Environment/Rural (n=15), Historical Issues (n=19).
- Baseline set: 20 non-China, non-politically-sensitive topics as control.
- All prompts in Mandarin Chinese; temperature 1.3 as recommended for DeepSeek API.
- Key suppressed content categories: "transparency, government accountability, civic mobilization."
- "Censorship leakage" concept: open-source DeepSeek model weights allow censorship to propagate to downstream products globally.

## Caveats / limitations
- CoT auditing works for R1-class models with explicit reasoning traces; not applicable to closed models like GPT-4 or Gemini.
- Tests topical prompts only, not identity-triggered refusals — the pilot's identity finding is distinct from this paper's topical censorship findings.
- Preprint (USC); not yet peer-reviewed as of June 2025.
- Prompt format "Please comment on this social issue in China: [topic]" is more neutral than the pilot's identity-loaded persona framing.
