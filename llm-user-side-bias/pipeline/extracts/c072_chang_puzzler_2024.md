---
cid: c072
evidence_scope:
  conceptual:
    refs: [knowledge_gated_access, multiturn_dialogue_safety]
    note: Closest published operational analog of the pilot's D-experiment "knowledge-gated access" finding. Puzzler attacks by feeding LLM implicit clues that an informed attacker who already knows the answer can construct — the model "guesses" what the attacker is really asking and complies.
  temporal:
    range: "2024"
  methodological:
    type: empirical-quantitative
scope_caveat: Authors frame Puzzler as a malicious-attacker tool requiring prior knowledge to generate clues; the pilot's D-experiment inverts the polarity — same mechanism (informed user gets answers, uninformed user gets refusals) but the harm is *to* the uninformed user, not *by* the informed one. Drafter must explicitly note this framing inversion.
---

# c072: Play Guessing Game with LLM — Indirect Jailbreak Attack with Implicit Clues (Puzzler)

**URL**: https://aclanthology.org/2024.findings-acl.304/ (arXiv:2402.09091v2)
**Source type**: peer_reviewed (ACL Findings 2024) | **Quality**: qs=4
**Authors**: Zhiyuan Chang, Mingyang Li, Yi Liu, Junjie Wang, Qing Wang, Yang Liu (ISCAS / NTU Singapore)
**Year / venue**: ACL Findings 2024 (Bangkok, August 2024)
**Deep-read on**: 2026-05-18
**Access status**: ok (full PDF, 647 lines via pdftotext)
**Pages/length**: ~12 pages

## Directly addresses
- Q4-KG (knowledge-gated access): **The single closest published operationalization of the pilot's knowledge-gating D-experiment.** Puzzler explicitly relies on the attacker already knowing the answer to construct clues that the LLM must "guess." Mechanistically isomorphic to the pilot's finding that users who already show awareness of "10,000–30,000 deaths" and "大屠殺" terminology unlock substantive responses after the model refused the same naked query.
- Q1-MT (multi-turn): Puzzler's three-phase pipeline (Defensive Measures Creation → Offensive Measures Generation → Indirect Jailbreak Attack) is in effect a multi-turn attack constructed through LLM-to-LLM chains.

## Key passages

### Passage 1 — for Q4-KG (abstract verbatim — the "guessing game" framing)
> "With the development of LLMs, the security threats of LLMs are getting more and more attention. Numerous jailbreak attacks have been proposed to assess the security defense of LLMs. Current jailbreak attacks primarily utilize scenario camouflage techniques. However, their explicit mention of malicious intent will be easily recognized and defended by LLMs. In this paper, we propose an indirect jailbreak attack approach, Puzzler, which can bypass the LLM's defensive strategies and obtain malicious responses by implicitly providing LLMs with some clues about the original malicious query. In addition, inspired by the wisdom of 'When unable to attack, defend' from Sun Tzu's Art of War, we adopt a defensive stance to gather clues about the original malicious query through LLMs. The experimental results indicate that the Query Success Rate of the Puzzler is 14.0%-82.7% higher than baselines on the most prominent LLMs."

**Page/section**: Abstract
**Why it matters**: The verbatim "guessing game" / "implicit clues" framing. Quotable as the cleanest published statement that LLM defenses are vulnerable to attackers who already know enough about the answer to construct clues — the inverse mechanism of the pilot's D-experiment.

### Passage 2 — for Q4-KG (the prior-knowledge requirement, intuition)
> "As illustrated in Figure 1, when we provide associated behaviors such as 'time my visit during the store's busiest hours' and 'study the layout of the store', LLMs have the capability to infer the underlying intent of 'steal from a store' and generate the desired output. Importantly, since this does not explicitly convey the malicious intent, i.e., each clue is not sufficient to reveal the intent of the original malicious query, traditional safety alignment mechanisms of LLMs struggle to defend against these types of attacks. This can be likened to playing a 'guessing game' with the LLM, where we provide verbal descriptions as hints without directly revealing the answer."

**Page/section**: Section 1 (Introduction)
**Why it matters**: This is the verbatim statement that the *attacker must already know* enough about the answer to construct the clues. The pilot's D-experiment inverts this: the model behaves *as if* a user who shows knowledge in their prompt deserves a response (informed user → answered), while a user with the same naked query but no prior demonstration of knowledge gets refused (uninformed user → "我还没有学会"). Same mechanism, opposite polarity of harm.

### Passage 3 — for Q4-KG (the Art of War / defensive-stance methodology)
> "Nevertheless, acquiring the clues of malicious intent poses a significant challenge. It is akin to launching a direct attack on the LLMs when we approach them with direct queries. As Sun Tzu wisely stated in The Art of War, 'When unable to attack, defend.' In light of this wisdom, we initially assume a defensive stance when interacting with the LLMs. By adopting this defensive viewpoint, we prevent the LLMs from blocking our queries and instead encourage them to generate a diverse set of defensive measures in response to the original malicious intent. Building upon this defensive foundation, we can inquire about the offensive aspects of the defensive measures, which still fall outside the safety alignment mechanisms of the LLMs, thereby successfully obtaining the aforementioned clues of the malicious intent."

**Page/section**: Section 1 (Introduction) and Section 3.1 (Defensive Measures Creation)
**Why it matters**: The "defensive-stance" technique is methodologically novel and is the operational mechanism of knowledge-extraction-via-indirection. The model will answer "how to prevent X" when it refuses "how to do X", and the answer to (1) reveals the components of (2). Mechanistically parallel to how the pilot's abliterated DeepSeek reveals what vanilla DeepSeek "knows but does not say."

### Passage 4 — for Q4-KG (quantitative ASR)
> "For the closed-source LLMs, Puzzler achieves a QSR of 96.6% on average, which is 57.9%-82.7% higher than baselines."

> Table 1 (AdvSub dataset, Query Success Rate):
> - GPT-3.5: 100% (Puzzler) vs. 37%/90%/53%/40% (baselines)
> - GPT-4: 100% (Puzzler) vs. 26%/13%/40%/0% (baselines)
> - GPT4-Turbo: 100% (Puzzler) vs. 13%/0%/7%/0% (baselines)
> - Gemini-pro: 83% (Puzzler) vs. 14%/47%/0%/17% (baselines)
> - LLama2-7B-chat: 3% (Puzzler) vs. 0%/0%/0%/0% (baselines)
> - LLama2-13B-chat: 29% (Puzzler) vs. 2%/0%/0%/0% (baselines)
>
> Following Rate (whether the response actually addresses the original malicious query): >85% for closed-source LLMs.

**Page/section**: Section 5.1 / Table 1
**Why it matters**: Hard cross-model numbers showing that the closer the model is to commercial state-of-the-art (GPT-4, GPT-4-Turbo), the *more* vulnerable it is to knowledge-gated indirection — 100% QSR. This is a critical finding: the technique is *stronger* on better models. Implies the L1 knowledge-gating threat does not go away with capability scaling.

### Passage 5 — for Q4-KG (Puzzler evades jailbreak detection)
> "SmoothLLM... achieves an ACC of 4.0% when applied to Puzzler."

> "JailGuard achieves an ACC of 38.0% when applied to Puzzler, which is 18.0%-62.0% lower than the ACC achieved on other baselines."

> Table 3 (jailbreak detection accuracy):
> - SmoothLLM on Puzzler: 4.0% (other methods: 26%-100%)
> - JailGuard on Puzzler: 38.0% (other methods: 56%-100%)

**Page/section**: Section 5.3 / Table 3
**Why it matters**: Puzzler is essentially undetectable by current jailbreak-detection systems because each individual prompt is benign. This is structurally important: a knowledge-gated mechanism does not leave detectable adversarial signatures. Mirrors the pilot's observation that natural multi-turn conversation does not trigger refusal templates because individual turns appear benign.

### Passage 6 — for Q4-KG (open-source LLM resistance via over-refusal)
> "Open-source LLMs are highly sensitive to prompts containing content from publicly reported jailbreak templates, and they are very likely to refuse responses to prompts with such sensitive words, even if benign queries are added to the jailbreak template. This phenomenon is particularly evident on LLama2-7B-chat, resulting in Puzzler and baselines being unable to jailbreak it. Although this overprotection phenomenon can protect LLMs from attacks, it may affect their usability to some extent."

**Page/section**: Section 5.1
**Why it matters**: Confirms a key pilot observation: over-refusal (LLama2-7B blanket refusal) and knowledge-gated access (GPT-4 100% QSR via Puzzler) are two ends of the *same* spectrum. The pilot operates in the middle: the model has *learned* to selectively respond based on context cues.

## Structural content worth knowing

- **Figure 1**: Side-by-side: malicious direct query → refusal vs. indirect clues (defensive behaviors) → compliance. Visually the cleanest illustration of knowledge-gated access.
- **Figure 2 (Puzzler pipeline)**: 3-phase architecture: (1) Defensive Measures Creation (extract malicious content, prompt LLM for defensive points); (2) Offensive Measures Generation (evaluate defenses, prompt for their offensive counterparts); (3) Indirect Jailbreak Attack (concatenate offensive measures as clues).
- **Tables 1 and 2**: Cross-model QSR and Following Rate on 2 datasets (AdvBench Subset and MaliciousInstructions) × 4 closed-source + 2 open-source models × 4 baselines + Puzzler. Comprehensive.
- **Table 3**: Detection-evasion comparison.
- **No Chinese-origin model in evaluation set** (GPT-3.5, GPT-4, GPT-4-Turbo, Gemini-pro, LLama2-7B/13B).

## Caveats / limitations

- **FRAMING INVERSION ALERT — and this is the central one for the pilot.** Chang et al.'s frame: malicious user with prior knowledge constructs indirect clues to manipulate a defending model. Pilot's frame: a discriminating model uses prior-knowledge-display to grant differential access — users *who can demonstrate they already know* get answered; users *who only have questions* get refused. Both observe the same mechanism (knowledge-bearing-context unlocks responses); the agent and the harm direction differ. Drafter MUST highlight this explicitly — it is the central conceptual contribution.
- Puzzler authors do not theorize the asymmetry between informed and uninformed users — they only operationalize one side.
- No political/identity-conditioned topics tested. AdvBench/MaliciousInstructions are safety-harm domains.
- Open-source LLMs (LLama-2) resist Puzzler via blanket over-refusal — pilot's local-model findings (cloud-template refusal disappears but length compression remains) suggest Chinese-origin local models may behave differently.
