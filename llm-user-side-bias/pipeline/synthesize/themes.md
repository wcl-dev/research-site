# Synthesizer Output — llm-user-side-bias
**Date**: 2026-05-15
**Stage**: synthesize → draft
**Brief questions covered**: Q1, Q2, Q3
**Total extracts in corpus**: 21 (deep-read)
**Themes produced**: 5
**Unassigned extracts**: 0

---

## Structural Note: The Core Tension This Thematic Structure Must Hold

The brief's novelty claim rests on a specific gap: existing research asks "**what topics** do LLMs block?" whereas the pilot asks "**to whom** do LLMs block the same topic?" The thematic structure below is designed to make this gap legible to the Drafter. Theme t01 names the gap explicitly. Theme t02 maps the established baseline that t01 departs from. Themes t03 and t04 provide the theoretical anchors for explaining *why* this gap matters. Theme t05 provides the empirical validation scaffolding.

The pilot study findings are the empirical spine throughout:
- **Signal 1**: DeepSeek refuses 228 Event for Taiwanese/Chinese identity, answers freely for no-identity
- **Signal 2**: ChatGPT/Gemini show subtle identity-responsive framing without outright refusal
- **Signal 3**: Gemini uses 屠殺 (TW IP) vs. 軍事鎮壓 (HK IP) for the same event

---

## Theme t01 — Declared Identity as Access-Control Trigger: The Research Gap

**Cluster source**: `identity_trigger_gap`
**Theme type**: `protocol`
**Linked brief questions**: Q1

### Definition

Existing literature on user-identity signals in LLMs establishes the *mechanism* — that declared identity shifts guardrail behavior — but does not test this mechanism on geopolitical or national-identity topics. The gap between this mechanism evidence (c012, c013) and the pilot's application of it to Chinese-origin LLMs and East Asian political content defines the study's novelty claim. Two adjacent papers (c002, c011) confirm that framing-sensitive and quality-differential effects exist in Chinese LLMs and in nationality-variable fairness audits, respectively, without closing the gap.

### Key sources

| cid | Title (short) | Quality | Role |
|-----|---------------|---------|------|
| c012 | Li, Chen, Saphra — ChatGPT Doesn't Trust Chargers Fans (EMNLP 2024) | qs=5 | Primary mechanism evidence — peer-reviewed proof that declared identity shifts guardrail behavior |
| c013 | Bernardelle et al. — Synthetic Persona Injection (ACM 2025) | qs=5 | Corroborating mechanism evidence — persona as active political behavioral lever |
| c011 | Amiri-Margavi et al. — Equal Access, Unequal Interaction (2026) | qs=4 | Quality-differential even at zero refusal — bridges access-refusal and access-quality frames |
| c002 | de Man — Emotional Framing and Chinese LLM Censorship (2025) | qs=4 | Parallel mechanism in Chinese LLMs — framing modulates censorship |

### Anchor quotes / paraphrases

1. **c012** (Li et al.): "ChatGPT appears to infer a likely political ideology and modify guardrail behavior accordingly." Conservative-leaning requests: 44% refusal for conservative personas, 76% for liberal personas. Same request, different identity → different refusal rate.

2. **c011** (Amiri-Margavi et al.): "Equitable access does not ensure equitable interaction quality once a response is provided." Zero refusal across all nationalities but systematic interaction-quality disparities. — This sentence is the conceptual anchor for the pilot's secondary signals (ChatGPT/Gemini don't refuse but exhibit identity-responsive framing).

3. **c013** (Bernardelle et al.): "While all models demonstrate significant shifts towards right-authoritarian positions, they exhibit more limited shifts towards left-libertarian positions, suggesting an asymmetric response to ideological manipulation." — Persona injection is an established, reproducible lever.

### How this theme serves the research angle

This theme establishes that the mechanism the pilot exploits — declared identity shifting LLM behavior — is real, peer-reviewed, and reproducible. But *every existing paper in this cluster tests US-centric demographic/political identities, not national identity on geopolitical history topics*. That is the gap. DeepSeek refusing 228 Event for Taiwanese or Chinese identity is the first empirical test of this mechanism on a Chinese-origin LLM in a geopolitical context. The Drafter should use this theme to frame the pilot as "extending Li et al.'s mechanism to a new domain" rather than discovering an entirely unrelated phenomenon.

---

## Theme t02 — What Existing Research Measures: Topic-Level Censorship as the Baseline

**Cluster source**: `existing_llm_bias_studies`
**Theme type**: `protocol`
**Linked brief questions**: Q1, Q3

### Definition

The established LLM political bias literature measures censorship and framing differences at the *topic level* — asking "does model X refuse/distort this topic?" for Chinese-sensitive subjects. This body of work (c001, c003, c004, c005, c007, c008, c009, c015, c020) provides the empirical baseline from which the pilot's identity-triggered finding departs. Collectively these studies confirm that Chinese-origin LLMs exhibit systematic, model-embedded censorship, but none tests whether the *same user asking the same question with different declared identity* receives different treatment.

### Key sources

| cid | Title (short) | Quality | Role |
|-----|---------------|---------|------|
| c001 | Pan & Xu — Chinese LLM Censorship (PNAS Nexus 2026) | qs=5 | Gold-standard topic-level benchmark; DeepSeek ~36% refusal rate |
| c005 | Ko — Taiwan Sovereignty Bilingual Benchmark (2026) | qs=5 | Topic-level Taiwan-specific benchmark; all 6 Chinese-origin models fail |
| c008 | Zhou & Zhang — Bilingual GPT Political Framing (Nature SR 2024) | qs=5 | Language-level mechanism; same model, Chinese vs. English framing gap |
| c020 | Bang, Chen, Lee — What Is Said and How It Is Said (ACL 2024) | qs=5 | Content-vs-style distinction; framework for 合規 vs. 合宜 interpretation |
| c003 | Naseh et al. — R1dacted (2025) | qs=4 | Global vs. local censorship distinction; 97.3% hard refusal rate |
| c004 | Qiu, Zhou, Ferrara — DeepSeek CoT Audit (2025) | qs=4 | CoT proves model knows but withholds — mechanistic proof of deliberate suppression |
| c007 | Guey et al. — 11-LLM Geopolitical Bias Map (2025) | qs=4 | Largest-scale bias map; US/China origin → alignment split |
| c009 | Yadav et al. — Safety vs. Propaganda (2025) | qs=4 | Safety/censorship distinction operationalized |
| c015 | Casademunt et al. — Censored LLMs as Testbed (2026) | qs=4 | "Knows but suppresses" framing for Tiananmen, Falun Gong |

### Anchor quotes / paraphrases

1. **c001** (Pan & Xu): Refusal rates — "BaiChuan: 60.23%; DeepSeek: ~36%; Ernie Bot: 32%; ChatGLM: 10%." Non-China models: "0% for GPT-3.5 and GPT-4o to 2.8% for Llama2-uncensored." And: "Unlike traditional forms of censorship that involve outright content removal or blocking access, LLM-based censorship typically involve some kind of reply—such as an apology or justification for not answering or even inaccurate information—making the suppression of information less obvious."

2. **c004** (Qiu et al.): "State-aligned information suppression far beyond China's digital borders. Because the model's weights are freely available, its invisible guardrails can be inherited, and unwillingly propagated to downstream products, without the end-users' awareness."

3. **c020** (Bang et al.): Content bias = "what is said"; style bias = "how it is said" (lexical polarity). — This framework precisely names the pilot's 合規 vs. 合宜 finding: the vocabulary switch is a *style-level* identity signal, not a content-level difference.

### How this theme serves the research angle

This theme is the "established landscape" that the pilot's identity-trigger finding stands against. Every study here asks a question of the form: *does model X refuse topic Y?* None asks: *does model X treat user A and user B differently on topic Y?* The Drafter should use this theme to demonstrate the pilot study's empirical novelty by contrast — the baseline literature is topic-centric; the pilot is user-centric. Crucially, c020's content/style framework gives the Drafter a precision tool for interpreting the pilot's vocabulary signals (合規 vs. 合宜) as style-level censorship, not merely different answers.

---

## Theme t03 — Informational Sovereignty as State Strategy

**Cluster source**: `geopolitical_frameworks`
**Theme type**: `comparison_framework`
**Linked brief questions**: Q2

### Definition

Chinese LLM censorship is not a corporate content-moderation choice — it is an expression of a state-level information sovereignty strategy with a multi-decade institutional architecture. This theme assembles the theoretical and empirical evidence that China's approach to AI information control is deliberate, legislated, and strategically coordinated (c023, c041), that similar geopolitical weaponization of AI infrastructure is documented in the Russian case (c035), that fine-tuning is a technically straightforward mechanism for embedding ideological alignment (c037), and that the "informational sovereignty" concept provides the most precise theoretical frame for this phenomenon (c021).

### Key sources

| cid | Title (short) | Quality | Role |
|-----|---------------|---------|------|
| c021 | Gillibrand & Draper — Informational Sovereignty (IJODR 2023) | qs=5 | Primary theoretical anchor — "informational sovereignty" as distinct from digital/data sovereignty. ACCESS BLOCKED |
| c023 | Spartak — China's Information Sovereignty (2025) | qs=5 | Three-pillar strategy (legislative, technological, cultural); legislative architecture documented |
| c041 | Atlantic Council/DFRLab — Chinese Discourse Power (2023) | qs=4 | $1.5B/year propaganda infrastructure; AI + big data for targeted information operations |
| c035 | Atlantic Council/DFRLab — Exposing Pravda (2025) | qs=4 | Russian state AI training poisoning — parallel case showing geopolitical weaponization of LLMs |
| c037 | Agiza et al. — PoliTune (AAAI AIES 2024) | qs=4 | Fine-tuning as deliberate ideological alignment mechanism; proves intentionality argument |

### Anchor quotes / paraphrases

1. **c023** (Spartak): China defines information sovereignty as "the right of the state to control the Internet within its borders and independently decide questions of data flows and cybersecurity." Three-pillar implementation: (1) Legislative — Cybersecurity Law, Data Security Law, Personal Information Protection Law; (2) Technological — "advanced monitoring systems... capable of identifying not only explicit violations, but hidden hints or metaphors related to politically sensitive topics"; (3) Cultural — promotion of traditional values as defense against Western influence.

2. **c041** (Atlantic Council): China launched "four State Key Laboratories dedicated to using big data to better tailor content to specific audiences." Chinese firms use "big data and cloud computing technologies" for "targeted information operations." $1.5 billion spent annually on propaganda since 2008.

3. **c035** (Atlantic Council/DFRLab): Pravda network operates across "more than eighty countries and regions" functioning as an "information laundromat, amplifying and saturating the news cycle" with Kremlin-aligned narratives — "Western users receive content containing pro-Kremlin, anti-Ukrainian messaging through AI tools trained on contaminated sources."

### How this theme serves the research angle

This theme provides the "why it's not a bug, it's a policy" argument. The Drafter should use it to establish that DeepSeek's identity-triggered 228 Event refusal is legible within an established state information sovereignty framework — not a coincidental coding choice by a company. The three-pillar structure from c023 maps directly onto the pilot's finding: the "legislative" pillar explains the regulatory vocabulary 合規; the "technological" pillar explains the identity-detection mechanism; the "cultural" pillar explains the language-switching (Traditional Chinese refusal uses softer vocabulary 合宜, calibrated for a different cultural-political audience). The access-blocked c021 is the theoretical keystone for this theme — operator must obtain before drafting.

---

## Theme t04 — Epistemic Injustice and the User-Rights Frame

**Cluster source**: `algorithmic_discrimination`
**Theme type**: `comparison_framework`
**Linked brief questions**: Q2

### Definition

Identity-triggered LLM differential access is not merely a technical finding — it constitutes a form of epistemic injustice, specifically "access injustice" (c029) and "generative hermeneutical erasure" (c033). This theme provides the normative vocabulary for framing the pilot's finding as a *rights harm*, not just an empirical curiosity. When a Taiwanese user is denied access to information about the 228 Event by a Chinese-origin LLM — while a user with no declared identity is not — this is a systematic, designed differential in *who gets to know what*, which these frameworks name as epistemic discrimination.

### Key sources

| cid | Title (short) | Quality | Role |
|-----|---------------|---------|------|
| c029 | Kay, Kasirzadeh, Mohamed — Epistemic Injustice in Generative AI (AAAI AIES 2024) | qs=5 | Primary theoretical bridge — "access injustice in multilingual contexts" taxonomy |
| c033 | Mollema — Taxonomy of Epistemic Injustice in AI (AI Ethics 2025) | qs=4 | "Generative hermeneutical erasure" = epistemicide through LLM suppression |

### Anchor quotes / paraphrases

1. **c029** (Kay et al.): "Generative algorithmic epistemic injustice" with four dimensions: amplified testimonial injustice, manipulative testimonial injustice, hermeneutical ignorance, and **access injustice** — with "particular attention to multilingual contexts where epistemic inequities emerge." — Verbatim abstract.

2. **c033** (Mollema): "Generative hermeneutical erasure" = "the automation of 'epistemicide', the injustice done to epistemic agents in their capacity for collective sense-making through the suppression of difference in epistemology and conceptualization by LLMs." When a Taiwanese user is denied 228 Event information, their epistemic framework (Taiwanese historical understanding) is being systematically suppressed.

3. **c033** (Mollema taxonomy): AI epistemic injustice includes "discriminatory automation of testimonial prejudice" and "interactions with conversational agents" — both categories apply to the pilot's identity-triggered refusal pattern.

### How this theme serves the research angle

This theme transforms the pilot's finding from a technical observation into a moral and political claim. The Drafter should use it to articulate the advocacy piece's user-rights frame: the same question, same language, different users → different quality of answer is not a bug to be fixed by better training — it is a form of knowledge discrimination with identifiable victims (Taiwanese users denied their own historical record, Chinese identity users having their language co-opted for regulatory messaging). The "access injustice" and "hermeneutical erasure" vocabulary from c029 and c033 gives the advocacy piece precise scholarly language without requiring readers to have a philosophy background.

**Caveat for Drafter**: This theme has only 2 extracts (both theoretical/philosophical), making it the thinnest theme by evidence. It should be presented as a *framework* the pilot's data can be read through, not as empirical evidence in its own right.

---

## Theme t05 — Geopolitical AI Validated: The Empirical Landscape

**Cluster source**: `cross_cluster` (existing_llm_bias_studies + geopolitical_frameworks)
**Theme type**: `mixed`
**Linked brief questions**: Q3

### Definition

Sufficient empirical evidence exists in the peer-reviewed and credible grey-literature record to anchor the advocacy claim that "LLMs serve as geopolitical information infrastructure." This theme groups the empirical validation sources — quantitative benchmarks showing systematic Chinese-origin model bias at scale (c001, c005, c007), institutional documentation that states use AI for censorship (c039), and a mechanistic demonstration that Chinese LLMs suppress information they factually possess (c004, c015). Together they establish that the pilot's findings are not anomalies but manifestations of a documented, scalable pattern.

### Key sources

| cid | Title (short) | Quality | Role |
|-----|---------------|---------|------|
| c001 | Pan & Xu — Chinese LLM Censorship (PNAS Nexus 2026) | qs=5 | Gold-standard peer-reviewed benchmark for Chinese LLM refusal at scale |
| c005 | Ko — Taiwan Sovereignty Benchmark (2026) | qs=5 | Taiwan-specific benchmark; CCP propaganda in DeepSeek R1 reasoning traces |
| c039 | Freedom House — Freedom on the Net 2023 | qs=5 | 72-country institutional documentation of AI-as-censorship-tool. ACCESS BLOCKED |
| c007 | Guey et al. — 11-LLM Geopolitical Bias Map (2025) | qs=4 | 19,712-prompt bias map; US/China origin alignment split quantified |
| c004 | Qiu et al. — DeepSeek CoT Audit (2025) | qs=4 | "Knows but suppresses" — strongest mechanistic proof of deliberate censorship |

### Anchor quotes / paraphrases

1. **c005** (Ko): "DeepSeek R1's chain-of-thought reasoning explicitly incorporates CCP narratives, stating in its reasoning traces that 'Taiwan has always been an inseparable part of China's territory since ancient times' and 'we must accurately convey the core position of the One China principle.' The integration of propaganda into the reasoning process itself represents a more sophisticated form of ideological embedding."

2. **c007** (Guey et al.): "Significant and consistent ideological alignments correlated with the LLMs' geographic origins; U.S.-based models predominantly favored Pro-U.S. stances, while Chinese-origin models exhibited pronounced Pro-China biases." — 19,712 prompts, 11 models.

3. **c001** (Pan & Xu): "This influence may extend beyond China's borders. Companies outside of China building applications on Chinese-developed foundation models could inadvertently propagate censorship." And: "Our results reveal important differences between China-originating models and non-China-originating models, suggesting that state intervention may play a role in shaping political biases in China LLMs."

### How this theme serves the research angle

This theme provides the empirical credibility scaffolding that an advocacy piece needs. Before making the pilot's novel identity-triggered claim, the Drafter needs to show that the broader context — Chinese LLMs exhibiting systematic geopolitical alignment — is not contested. The sources here are enough to make that case for a general-audience Taiwan reader. The pilot's 228 Event finding then lands as an instance of a documented pattern, not an isolated curiosity. The access-blocked c039 (Freedom House) is important here — it is the most authoritative institutional source and the one most recognizable to a policy audience.

---

## Unassigned Extracts

**None.** All 21 deep-read extracts are assigned to at least one theme.

Multi-assigned extracts (intentional — these cross thematic boundaries):
- **c001** (Pan & Xu): appears in t02 (baseline) and t05 (validation) — it serves both as the primary topic-level benchmark and as a validation anchor.
- **c004** (DeepSeek CoT Audit): appears in t02 (baseline) and t05 (validation) — the "knows but suppresses" finding is both a baseline characterization and a validation of deliberate censorship.
- **c005** (Ko Taiwan): appears in t02 (baseline) and t05 (validation) — same logic.
- **c007** (Guey geopolitical map): appears in t02 (baseline) and t05 (validation).

---

## Brief Question Coverage

| Brief Q | Themes covering it | Status |
|---------|-------------------|--------|
| Q1 — Identity-trigger gap / positioning | t01, t02 | Covered — t01 names the gap; t02 maps the landscape being departed from |
| Q2 — Theoretical frameworks | t03, t04 | Covered — t03 = sovereignty/authoritarianism; t04 = epistemic injustice |
| Q3 — Validation | t02, t05 | Covered — t02 provides baseline evidence; t05 provides advocacy-scale anchors |

All three brief questions have at least one theme. No uncovered questions.

---

## Open Questions (for Drafter)

1. **c021 (Gillibrand & Draper) — CRITICAL — ACCESS BLOCKED**: The `informational sovereignty` theoretical anchor (t03's keystone) is paywalled. Drafter must note this limitation and either (a) work from abstract-level characterization only, clearly caveating that full text was not accessible, or (b) wait for operator to obtain. Do not fabricate passage-level quotes from this source.

2. **c039 (Freedom House 2023) — CRITICAL — ACCESS BLOCKED**: 72-country AI-censorship documentation (t05's institutional anchor) not accessible via WebFetch. Same caveat applies.

3. **Anchor literature absent**: Waight et al. 2026 (Nature), Samokhodskyi/ELN 2026, Gary King (Citizen Lab) are named in the brief as "dialogue partners" but are not in the accepted extract set. Drafter must caveat that positioning relative to these papers relies on the brief's description rather than direct citation of accessible text.

4. **t04 thinness**: Two extracts, both theoretical — no empirical backup. Drafter should frame t04 content as "framework for interpreting findings" rather than "evidence that X is true."

5. **Ko 2026 (c005) caveats**: Single-author with explicit Taiwan MP affiliation; 10-prompt benchmark with no inter-rater reliability. Pair with Pan & Xu (c001) for key empirical claims; do not rely on Ko alone.

6. **No counter_framings in brief_expanded.yaml**: Balance check not applicable. The brief does not contain adversarial counter-framing sources. Drafter should nevertheless acknowledge the limits of what the literature currently can claim causally — Pan & Xu, c004, and c005 all explicitly disclaim causal proof of state intervention. The "state intervention" claim is strong correlation / inference, not demonstrated direct causation.

---

## Theme-Type Summary

| Theme type | Count | Themes |
|-----------|-------|--------|
| protocol | 2 | t01, t02 |
| comparison_framework | 2 | t03, t04 |
| mixed | 1 | t05 |
