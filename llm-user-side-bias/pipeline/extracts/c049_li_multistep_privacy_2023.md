---
cid: c049
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety, knowledge_gated_access]
    note: Early (2023) canonical reference establishing that multi-step jailbreak prompts extract privacy content from ChatGPT that single-step queries cannot — the earliest published precursor of the multi-turn paradigm.
  temporal:
    range: "2023"
  methodological:
    type: empirical-quantitative
scope_caveat: Only abstract retrieved. Detailed extraction mechanism and quantitative numbers not extracted in this pass.
---

# c049: Multi-step Jailbreaking Privacy Attacks on ChatGPT

**URL**: https://aclanthology.org/2023.findings-emnlp.272/
**Source type**: peer_reviewed (EMNLP Findings 2023) | **Quality**: qs=4
**Authors**: Haoran Li, Dadi Guo, Wei Fan, Mingshi Xu, Jie Huang, Fanpu Meng, Yangqiu Song
**Year**: 2023
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract only via WebFetch from ACL Anthology landing page
**Pages/length**: ACL Findings paper, ~10 pages

## Directly addresses
- Q1-MT (historical anchor): The earliest peer-reviewed paper to operationalize multi-step jailbreak as an attack paradigm. Useful as the historical reference point for "multi-step" as a category.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim)
> "With the rapid progress of large language models (LLMs), many downstream NLP tasks can be well solved given appropriate prompts. Though model developers and researchers work hard on dialog safety to avoid generating harmful content from LLMs, it is still challenging to steer AI-generated content (AIGC) for the human good. As powerful LLMs are devouring existing text data from various domains (e.g., GPT-3 is trained on 45TB texts), it is natural to doubt whether the private information is included in the training data and what privacy threats can these LLMs and their downstream applications bring. In this paper, we study the privacy threats from OpenAI's ChatGPT and the New Bing enhanced by ChatGPT and show that application-integrated LLMs may cause new privacy threats. To this end, we conduct extensive experiments to support our claims and discuss LLMs' privacy implications."

**Page/section**: Abstract
**Why it matters**: Establishes the multi-step paradigm in the privacy-extraction domain. Useful as the originating "multi-step" citation. Drafter can use this to show that the multi-turn vulnerability has been recognized since 2023.

## Structural content worth knowing
- Targets ChatGPT and New Bing.
- Domain is privacy extraction, not political content — relevance to the pilot is paradigmatic (multi-step works), not topical.

## Caveats / limitations
- **ACCESS PARTIAL**: only abstract. Drafter should cite as foundational/historical reference only, not for specific numbers.
- Privacy-extraction framing — distinct from the pilot's geopolitical-content framing. Mechanism transfers; subject matter does not.
