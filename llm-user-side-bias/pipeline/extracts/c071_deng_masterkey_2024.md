---
cid: c071
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: MASTERKEY — cross-vendor jailbreak study comparing ChatGPT, Bing Chat, Bard, AND Ernie (Baidu's Chinese-origin chatbot). Documents vendor-specific defense architectures and policy enforcement gaps.
  temporal:
    range: "2024"
  geographic:
    refs: [US, China]
  methodological:
    type: empirical-quantitative
scope_caveat: Ernie was included in policy analysis (Table I) but explicitly excluded from the jailbreak ASR experiments because "repeated unsuccessful jailbreak attempts on Ernie result in account suspension." Drafter should not over-claim cross-vendor ASR numbers including Ernie.
---

# c071: MASTERKEY — Automated Jailbreaking of Large Language Model Chatbots

**URL**: https://doi.org/10.14722/ndss.2024.24188
**Source type**: peer_reviewed (NDSS 2024) | **Quality**: qs=4
**Authors**: Gelei Deng, Yi Liu, Yuekang Li, Kailong Wang, Ying Zhang, Zefeng Li, Haoyu Wang, Tianwei Zhang, Yang Liu (NTU Singapore / UNSW / Huazhong UST / Virginia Tech)
**Year**: 2024
**Deep-read on**: 2026-05-18
**Access status**: ok (PDF retrieved from NDSS Symposium, first ~4 pages = 276 lines extracted)
**Pages/length**: NDSS conference paper

## Directly addresses
- Q1-MT (cross-vendor commercial-chatbot baseline): MASTERKEY is the broadest published cross-vendor evaluation, **including Ernie** (Baidu's Chinese-origin chatbot). Documents how different vendors' policy enforcement differs in striking ways.
- Q4-KG (auxiliary): The empirical finding that Bing Chat and Bard use *on-the-fly* generation analysis (vs. ChatGPT's input/output filtering) is mechanistically relevant — different defense layers translate to different identity/context sensitivity profiles.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim)
> "Large language models (LLMs), such as chatbots, have made significant strides in various fields but remain vulnerable to jailbreak attacks, which aim to elicit inappropriate responses. Despite efforts to identify these weaknesses, current strategies are ineffective against mainstream LLM chatbots, mainly due to undisclosed defensive measures by service providers. Our paper introduces MASTERKEY, a framework exploring the dynamics of jailbreak attacks and countermeasures. We present a novel method based on time-based characteristics to dissect LLM chatbot defenses. This technique, inspired by time-based SQL injection, uncovers the workings of these defenses and demonstrates a proof-of-concept attack on several LLM chatbots."

> "By fine-tuning an LLM with jailbreak prompts, we create attacks with a 21.58% success rate, significantly higher than the 7.33% achieved by existing methods."

**Page/section**: Abstract
**Why it matters**: Establishes cross-vendor scope and the ASR baseline (7.33% existing methods → 21.58% MASTERKEY). Cross-vendor evaluation is a structural property of the paper.

### Passage 2 — for Q1-MT (cross-vendor scope including Ernie)
> "We comprehensively evaluate five state-of-the-art LLM chatbots: GPT-3.5, GPT-4, Bard, Bing Chat, and Ernie [8] with a total of 850 generated jailbreak prompts. We carefully examine the performance of MASTERKEY from two crucial perspectives: query success rate which measures the jailbreak likelihood... and prompt success rate which measures the prompt effectiveness."

> "We do not include Ernie in this study [the empirical jailbreak effectiveness study] for a couple of reasons. First, although Ernie exhibits decent performance with English content, it is primarily optimized for Chinese, and there are limited jailbreak prompts available in Chinese. A simple translation of prompts might compromise the subtlety of the jailbreak prompt, making it ineffective. Second, we observe that repeated unsuccessful jailbreak attempts on Ernie result in account suspension, making it infeasible to conduct extensive trial experiments."

**Page/section**: Section II / Section III.B (Target Selection)
**Why it matters**: **Critical for the pilot's framing.** Ernie is included in policy analysis but excluded from ASR experiments because *the platform suspends accounts that try to jailbreak it*. This is the cleanest published evidence that Chinese-origin LLM platforms operate at a different threat-model level — the platform layer (L4 in the pilot's framework) actively monitors and disciplines users, in addition to model-level safety. Quote this directly to support the pilot's four-layer threat model.

### Passage 3 — for Q1-MT (vendor-policy comparison — Table I)
> Comparison of usage policies across providers — **Ernie is the ONLY provider that explicitly forbids "Content Harmful to National Security and Unity"** (specified ✓ and enforced ✓).
>
> Table I row "Content Harmful to National Security and Unity":
> - OpenAI: specified ✗, enforced ✗
> - Google Bard: specified ✗, enforced ✗
> - Bing Chat: specified ✗, enforced ✗
> - **Ernie: specified ✓, enforced ✓**

**Page/section**: Table I (Section III.A — Usage policies)
**Why it matters**: **Direct documentary evidence that Chinese-origin chatbots include a "National Security and Unity" prohibition that no Western chatbot has.** Quote this verbatim — it is the single cleanest published data point distinguishing China-origin from US-origin chatbot policy.

> "Only Ernie has a policy explicitly forbidding any harm to national security and unity."

**Page/section**: Section III.A (commentary on Table I)
**Why it matters**: Direct citable claim distinguishing Chinese vs. Western chatbot policies. Maps directly onto the pilot's "L4 service platform layer" — where the explicit refusal templates live.

### Passage 4 — for Q1-MT (Bing/Bard use on-the-fly generation analysis)
> "Modern LLM chatbot services including Bing Chat and Bard implement additional content filtering mechanisms beyond the generative model to enforce the usage policy."

> "We reveal that Bing Chat and Bard, where an on-the-fly generation analysis is deployed to evaluate semantics and identify policy-violating keywords."

**Page/section**: Section II (Introduction) / Section III.B summary
**Why it matters**: Documents that some Western chatbots use real-time output analysis, not just input/output filtering. Useful for the Drafter to distinguish between alignment-layer (L3), platform-layer keyword filtering (L4), and output-layer real-time analysis. The pilot's four-layer threat model can be enriched by referencing these distinctions.

### Passage 5 — for Q1-MT (cross-vendor ASR)
> "We achieve a notably higher success rate with OpenAI models compared to existing techniques. Meanwhile, we are the first to disclose successful jailbreaks for Bard and Bing Chat, with query success rates of 14.51% and 13.63% respectively."

**Page/section**: Section II / cross-vendor results summary
**Why it matters**: Concrete cross-vendor ASR numbers: OpenAI > Bing 14.51% > Bard 13.63%. Shows that vendor-specific defense architectures produce measurably different vulnerability profiles. Quote-ready cross-vendor benchmark.

### Passage 6 — for Q1-MT (the time-based SQL-injection analogy)
> "We observe a parallel between time-sensitive web applications and LLM chatbots. Drawing inspiration from time-based SQL injection attacks in web security, we propose to exploit response time as a novel medium to reconstruct the defense mechanisms."

**Page/section**: Section II (contribution overview)
**Why it matters**: Methodological novelty — using response *time* to fingerprint vendor defenses. Not directly relevant to the pilot, but useful context on how the field analyzes black-box vendor differences.

## Structural content worth knowing

- **Table I (Usage Policies)**: 10 prohibited categories × 4 providers (OpenAI, Bard, Bing Chat, Ernie). Cleanest published cross-vendor policy comparison. **Ernie is unique in forbidding "Content Harmful to National Security and Unity"**.
- **Figure 1**: Side-by-side jailbreak example (Normal Mode refusal vs. Jailbreak Mode compliance).
- 850 generated jailbreak prompts × 4 categories × 5 questions × 10 rounds = 68,000 queries total.
- Ernie (Baidu, China) is included in scope but the authors explicitly cannot fully test it because of platform-level user-suspension.
- Authors are from NTU Singapore + Chinese institutions — the Ernie observation is from researchers with relevant linguistic and platform access.

## Caveats / limitations

- Ernie's exclusion from the empirical ASR study is a methodological gap but the *reason for exclusion* (account suspension) is itself a finding the Drafter should cite.
- Models tested in empirical study: GPT-3.5, GPT-4, Bing Chat, Bard. Ernie policy-only.
- **No multi-turn / dialogue-level evaluation** — MASTERKEY is single-prompt evaluation; the pilot's MT findings are not directly comparable in terms of ASR numbers.
- **Useful for L4 platform-layer evidence and for cross-vendor policy comparison**, less so for the L1 conversation-layer threat model that the V2 brief centers.
