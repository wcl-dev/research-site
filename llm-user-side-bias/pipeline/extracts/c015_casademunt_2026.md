---
cid: c015
evidence_scope:
  conceptual:
    refs: [existing_llm_bias_studies]
    note: Frames the "LLM knows but withholds" structure as distinct from capability gap; supports the conceptual distinction between knowledge and access in the pilot's theoretical framing.
  methodological:
    type: empirical-quantitative
---

# c015: Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation

**URL**: https://arxiv.org/abs/2603.05494
**Source type**: preprint (arXiv 2026) | **Quality**: qs=4
**Deep-read on**: 2026-05-15
**Access status**: ok (abstract and key findings from arXiv page)
**Pages/length**: ~15 pages estimated

## Directly addresses
- Q1 (existing studies / positioning): Frames the "LLM knows but withholds" structure as a distinct phenomenon — supports the conceptual distinction between capability (what the model knows) and access (what it reveals) in the pilot's theoretical framing.

## Key passages

### Passage 1 — for Q1 (knowing vs. revealing — key concept)
> "Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation — modifying prompts or weights so that the model answers truthfully — and lie detection — classifying whether a given response is false."

> Models like Qwen3 "frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress."

**Page/section**: Abstract + Introduction
**Why it matters**: Establishes that censored models knowingly suppress information — the model has the knowledge but the training has conditioned suppression. Directly supports framing refusal as deliberate access-control policy, not capability gap.

### Passage 2 — for Q1 (techniques for recovering withheld knowledge)
> "Sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses."

> "Prompting the censored model to classify its own responses performs near an uncensored-model upper bound."

**Page/section**: Key findings
**Why it matters**: Shows that suppressed knowledge is recoverable through prompt engineering — confirms the model "knows" the answer; the withholding is a policy layer, not a knowledge gap. This is the mechanistic foundation for the pilot's claim that refusal is access control.

### Passage 3 — for Q1 (Tiananmen and Falun Gong as suppressed knowledge)
> "Censored models like Qwen3 frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress."

**Page/section**: Introduction / Key findings
**Why it matters**: Specific named examples (Tiananmen, Falun Gong) are adjacent to the 228 Event topic in the pilot's study — both are politically sensitive Chinese-government-censored events. The "occasionally answers correctly" finding means the suppression is probabilistic, not absolute — relevant for understanding the pilot's identity-conditioned variation.

## Structural content worth knowing
- Treats naturally censored Chinese LLMs as an experimental testbed for honesty research — novel methodological framing.
- Strongest elicitation techniques also transfer to DeepSeek R1 (frontier open-weights model).
- "No technique fully eliminates false responses" — important caveat for the pilot's claim that identity-triggered censorship can be probed.
- Linear probes trained on unrelated data offer cheaper alternative to full elicitation techniques.

## Caveats / limitations
- Focuses on Qwen3 and similar Chinese models; DeepSeek applicability only noted for R1.
- arXiv preprint 2026; not yet peer-reviewed.
- Knowledge elicitation framing is different from identity-triggered access control — the pilot's finding is not about recovering suppressed information but about differential suppression by declared identity.
