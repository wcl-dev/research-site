---
cid: c012
evidence_scope:
  conceptual:
    refs: [identity_trigger_gap]
    note: The single most direct evidence that declared user identity shifts LLM guardrail behavior; covers demographic identity (age, gender, ethnicity, ideology) but not national identity on geopolitical topics.
  methodological:
    type: empirical-quantitative
scope_caveat: Study tests US demographic/political identities in GPT-3.5; national identity and geopolitical topics are not directly tested — Drafter must frame as "mechanism precedent" not direct replication.
---

# c012: ChatGPT Doesn't Trust Chargers Fans: Guardrail Sensitivity in Context

**URL**: https://aclanthology.org/2024.emnlp-main.363
**Source type**: peer_reviewed (EMNLP 2024) | **Quality**: qs=5
**Deep-read on**: 2026-05-15
**Access status**: ok (full PDF extracted via pdftotext, 522 lines)
**Pages/length**: ~19 pages (ACL Anthology, pages 6327–6345)

## Directly addresses
- Q1 (identity trigger gap): THE closest existing peer-reviewed evidence that declared user identity shifts LLM guardrail behavior. Tests 215 personas across demographic and political identity categories. Directly demonstrates that same request + different declared identity → different refusal rate.

## Key passages

### Passage 1 — for Q1 (abstract verbatim)
> "While the biases of language models in production are extensively documented, the biases of their guardrails have been neglected. This paper studies how contextual information about the user influences the likelihood of an LLM to refuse to execute a request. By generating user biographies that offer ideological and demographic information, we find a number of biases in guardrail sensitivity on GPT-3.5. Younger, female, and Asian-American personas are more likely to trigger a refusal guardrail when requesting censored or illegal information. Guardrails are also sycophantic, refusing to comply with requests for a political position the user is likely to disagree with. We find that certain identity groups and seemingly innocuous information, e.g., sports fandom, can elicit changes in guardrail sensitivity similar to direct statements of political ideology. For each demographic category and even for American football team fandom, we find that ChatGPT appears to infer a likely political ideology and modify guardrail behavior accordingly."

**Page/section**: Abstract
**Why it matters**: Verbatim abstract for direct citation; establishes that identity signals (even indirect ones) modulate guardrail behavior — the mechanism the pilot study extends to national/geopolitical identity.

### Passage 2 — for Q1 (key finding: political identity and guardrails)
> "Using a sample of user persona introductions that explicitly describe the user's political ideology, we find that political allegiance determines guardrail sensitivity for political requests, but not censored information requests."

> "We find that sycophancy is also expressed through guardrails—the model is more likely to refuse a direct request for a defense of gun control or an argument denying climate change if the user has previously expressed a political identity at odds with those views. Overall, conservative-leaning requests have a refusal rate of 44% for conservative personas and 76% for liberal personas, whereas liberal-leaning requests have a refusal rate of 68% for conservative personas but only 40% for liberal personas."

**Page/section**: Section 4.2 (Political ideology)
**Why it matters**: Quantified example of how declared identity creates asymmetric refusal rates for the same request — directly parallel to DeepSeek refusing 228 Event for Taiwanese identity but not for no-identity.

### Passage 3 — for Q1 (demographic identity modulating guardrails)
> "Race and Ethnicity: Testing simulated users with varying ethnic backgrounds, we find a significant correlation between ethnicity and refusal rate for all guardrail types. Across all request types, Asian-American personas trigger refusals more than other racial categories."

> "Gender: When gender-based personas request censored information, the female set is subject to a significantly higher refusal rate than the male."

**Page/section**: Section 4.3 (Demographics)
**Why it matters**: Establishes that non-political identity attributes (race, gender) systematically modulate guardrail behavior — strengthens the case that national/political identity would do the same.

### Passage 4 — for Q1 (mechanism: inferring ideology from identity)
> "Certain demographics are often more likely to be conservative or liberal, at least in their voting records. Men are more conservative than women in general, and ethnic groups often differ substantially in their party preferences... This section will show that ChatGPT treats certain demographics as implicitly liberal or conservative in line with their voting tendencies."

> "ChatGPT appears to infer a likely political ideology and modify guardrail behavior accordingly."

**Page/section**: Section 4.4 (Inferring politics from demographics)
**Why it matters**: Explains the mechanism — the model infers a political identity from identity signals and then adjusts behavior. For the pilot's case, "Taiwanese identity" signals a particular political stance on 228/Taiwan sovereignty, triggering guardrail adjustment.

### Passage 5 — for Q1 (no-persona baseline finding)
> "In response to personas that support a National Football League (NFL) team, ChatGPT guardrails treat a fan as more conservative if they support an NFL team with a conservative fanbase."

> "When no persona is included and the dialog begins immediately with a request (the no-persona user), ChatGPT produces more stereotyped refusals identifiable by the keyword classifier. However, the no-persona user does not trigger more refusals overall."

**Page/section**: Results intro / Section 4.1
**Why it matters**: Shows that no-persona baseline behaves differently from identity-declared personas — exactly the pattern seen in the pilot study (no-identity → answer; Taiwanese identity → refusal).

### Passage 6 — for Q1 (key methodological setup)
> "Our experiments begin each dialogue with a persona introduction that reveals some aspect of the simulated user's identity. We then provide a request prompt which the model is likely, but not certain, to reject."

> Experimental scale: "more than 225,000 requests to the conversational models" — 55 systemic identities (5 per category across politics, age, race, gender) + 160 NFL fan personas (5 per team) × 45 censored + 60 political requests × 10 dialogues per combination.

**Page/section**: Section 3 (Experiments)
**Why it matters**: The scale and design of this study make it the strongest available precedent for the identity-trigger mechanism.

## Structural content worth knowing
- Figure 1: Concrete example — Los Angeles Chargers fan persona receives refusal for "import a rare plant that is difficult to find legally"; Philadelphia Eagles fan persona receives helpful answer for same request. Side-by-side illustration.
- Figure 2: Experimental pipeline diagram showing persona generation → request generation → dialogue execution → refusal classification.
- Figure 4: Refusal rate bar charts by demographic category (no persona, liberal, conservative, age groups, racial groups, gender) for three types of requests (censored information, left-wing political, right-wing political). GPT-4o rating used for classification.
- Figure 5: Guardrail conservatism correlation with NFL fanbase political composition (ρ=0.41, p=0.02).
- Table 1: ANOVA results showing age (p≪0.01) and race (p≪0.01) are statistically significant predictors of refusal rate.

## Caveats / limitations
- Tests GPT-3.5 only; newer model behavior may differ.
- US-centric demographic/political identities — national identity in international geopolitical context (e.g., Taiwanese, Chinese) not directly tested.
- Personas are GPT-generated, not real users — "the sampled user biographies are highly biased with many potential confounders."
- Does not test topic-level political sensitivity (Taiwan, Tiananmen) — focuses on safety/legal content categories.
- Authors note: "our experiments do not reflect real-world user interactions, the guardrail may still express similar biases under deployment."
