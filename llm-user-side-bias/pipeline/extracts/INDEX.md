# Segmenter index — llm-user-side-bias

## V1 pass (May 15, 2026)

Deep-read budget: 17 / Prioritized: 17 (of 32 accepted)

### V1 Deep-read (depth 1 — must, qs=5)

- c001: Pan & Xu 2026 PNAS Nexus — Chinese LLM political censorship benchmark: DeepSeek ~36% refusal rate vs. 0% for non-China models; origin effect dominates language effect; LLM censorship via reply not removal; transnational propagation risk.
- c005: Ko 2026 Taiwan sovereignty benchmark — 17-LLM bilingual benchmark; all 6 Chinese-origin models fail; DeepSeek R1 and Qwen3 Max score 0/10 in both Chinese AND English (language-consistent censorship, not language-selective); verbatim CCP propaganda in R1 reasoning traces.
- c008: Zhou & Zhang 2024 Nature Scientific Reports — Bilingual GPT political framing inconsistency: same model gives pro-China framing in Chinese, more critical framing in English; attributes gap to Chinese state censorship in training corpora; develops "political identity" concept.
- c012: Li, Chen, Saphra EMNLP 2024 — THE direct evidence for identity-trigger mechanism: user identity biographies shift ChatGPT guardrail behavior; conservative vs. liberal personas → asymmetric refusal rates; demographic identity (race, age, gender) all modulate guardrails; sycophantic guardrails.
- c013: Bernardelle, Fröhling, Civelli ACM 2025 — Synthetic persona injection shifts LLM political ideology; establishes declared identity as active behavioral lever; asymmetric manipulability (easier to shift right-authoritarian); preprint arXiv:2412.14843.
- c020: Bang, Chen, Lee ACL 2024 — Content-vs-style political bias framework; "what is said" vs. "how it is said"; lexical polarity as style bias signal; directly applicable to interpreting 合規 vs. 合宜 as style-level identity signals.
- c021: Gillibrand & Draper 2023 — Informational sovereignty as distinct AI regulatory concept; distinguishes from data sovereignty and digital sovereignty. ACCESS BLOCKED — paywall. Operator must obtain.
- c023: Spartak 2025 — China's information sovereignty as deliberate three-pillar state strategy (legislative, technological, cultural); cyber sovereignty definition; AI in information control quantified; institutional coordination documented.
- c029: Kay, Kasirzadeh, Mohamed AAAI AIES 2024 — Epistemic injustice in generative AI; introduces four dimensions: amplified testimonial injustice, manipulative testimonial injustice, hermeneutical ignorance, access injustice; "access injustice in multilingual contexts" is directly applicable. Partial access; preprint arXiv:2408.11441.
- c039: Freedom House 2023 Freedom on the Net — Authoritative 72-country AI-for-repression documentation. ACCESS BLOCKED — all URLs return 404. Operator must download PDF directly from freedomhouse.org.

### V1 Deep-read (depth 2 — should, qs=4 with distinctive why_relevant)

- c002: de Man 2025 — Emotional framing modulates Chinese LLM censorship (Kimi/Ernie); four behavioral patterns; post-generation filtering evidence; parallel mechanism to identity-triggered refusal.
- c003: Naseh et al. 2025 (R1dacted) — Defines global vs. local censorship distinction; 10,030-prompt dataset; 97.3% Type 1 (hard refusal) censorship rate; cross-language censorship rates (Chinese 99.57%); verbatim CCP narrative response to Taiwan question; model-embedded not API-level.
- c004: Qiu, Zhou, Ferrara 2025 — CoT auditing proves DeepSeek withholds known answers; Type 1 (hard refusal) vs. Type 2 (semantic divergence) censorship types; "state-aligned information suppression far beyond China's digital borders"; "censorship leakage" through open-source weights.
- c007: Guey et al. 2025 — Largest geopolitical bias map (11 LLMs, 19,712 prompts); US-origin → Pro-US; Chinese-origin → Pro-China; stance reversals by language; -2 to +2 bias scale.
- c009: Yadav et al. 2025 — Safety vs. propaganda distinction operationalized; PSP dataset; "most LLMs perform some form of censorship"; country-specific censorship pattern variation.
- c011: Amiri-Margavi et al. 2026 — Counterfactual audit: zero refusal rates across all nationalities BUT systematic interaction quality disparities persist; "equitable access does not ensure equitable interaction quality."
- c015: Casademunt et al. 2026 — Censored LLMs know but suppress; Tiananmen and Falun Gong as specific examples; elicitation techniques show knowledge is withheld, not absent.
- c033: Mollema 2025 (AI Ethics) — Taxonomy of AI epistemic injustice; introduces "generative hermeneutical erasure" = epistemicide through LLM suppression of non-dominant epistemologies; 6-type taxonomy.
- c035: Atlantic Council/DFRLab 2025 (Pravda) — Documented Russian state AI training poisoning; 80+ countries targeted; "information laundromat" mechanism; demonstrates AI-as-geopolitical-tool pattern.
- c037: Agiza et al. AAAI AIES 2024 (PoliTune) — Fine-tuning choices deliberately embed political bias; PEFT enables efficient ideological alignment; establishes intentionality of political bias in LLMs.
- c041: Atlantic Council/DFRLab 2023 (Chinese discourse power) — China's discourse power strategy; $1.5B/year propaganda spend; AI + big data for targeted information operations; 200M overseas social followers; cyber sovereignty as strategic vector.

### V1 Skipped with reason
- c006, c017, c019, c022, c024, c025, c026, c030, c031, c032, c044 — see V1 skip-reasoning rationale documented in this index's prior version (commit history) and in the operator-overrides section below.

---

## V2 pass (May 18, 2026)

Deep-read budget: 18 / Prioritized: 18 (of 32 V2 accepted, c046–c082)

### V2 Deep-read (depth 1 — must — V2 brief's priority extraction list)

- **c081**: Russinovich, Salem, Eldan 2024 (Microsoft, Crescendo) — qs=5 — Canonical multi-turn jailbreak. Full PDF (~22 pages) extracted via pdftotext. **Key headline numbers**: Crescendo achieves 98% binary ASR on GPT-4 AdvBench; A→B→C three-turn sequence raises compliance from 17.3% to 99.9%; cross-vendor jailbreak (ChatGPT, Gemini, Claude, LLaMA-2/3 all succumb). Key conceptual contribution: "foot-in-the-door" psychology + model's own outputs as attack surface. **No Chinese-origin model tested**. FRAMING INVERSION NOTED.
- **c082**: Anil et al. 2024 (Anthropic, Many-shot Jailbreaking) — qs=5 — In-context-learning power-law scaling on safety alignment. Blog summary only (partial; full PDF retrieval recipe in extract). **Key headline numbers**: tested up to 256 shots; ASR reduced from 61% to 2% with prompt-classification mitigations. "Long context windows are a double-edged sword." FRAMING INVERSION NOTED.
- **c061**: Du, Mo, Wen 2025 (AAAI, attention shifting) — qs=5 — Mechanistic explanation of why MT works: "successful multi-turn jailbreaks can effectively disperse the attention of LLMs on keywords associated with harmful behaviors, especially in historical responses." **ACCESS PARTIAL — abstract only**; full PDF behind AAAI subscription. Single most important mechanism paper. FRAMING INVERSION NOTED.
- **c058**: Wei et al. 2026 (TPAMI, ICA/ICD) — qs=5 — Canonical ICL-effects-on-alignment paper. Full PDF (16 pages) extracted. **Key headline numbers**: ICA achieves 81% ASR on GPT-4 with 20-shot; 87% on Vicuna with 10-shot; theoretical framework P = λPH + (1-λ)PS for safe/harmful distribution decomposition. **QWen-7b is in evaluation set** (Chinese-origin model coverage). FRAMING INVERSION NOTED.
- **c066**: Wen et al. 2025 (TACL, abstention survey) — qs=5 — Three-axis framework (query / model / human-values). Full PDF (first 8 pages) extracted. Crucially, explicitly identifies multi-turn context-dependent abstention as an under-studied gap: "earlier context in multi-turn conversations can impact judgments for either query answerability or human values alignment in later conversational turns." THE conceptual scaffold for theorizing the pilot's identity-conditioned refusal.
- **c072**: Chang et al. 2024 (ACL Findings, Puzzler) — qs=4 — Closest published operationalization of knowledge-gated access. Full PDF extracted. **Key headline numbers**: 96.6% QSR average on closed-source LLMs; 57.9%-82.7% higher than baselines; 100% QSR on GPT-3.5/GPT-4/GPT-4-Turbo. Sun Tzu "When unable to attack, defend" framing. Detection-evasion: SmoothLLM detects only 4.0% of Puzzler prompts. **CENTRAL CONCEPTUAL FRAMING INVERSION** — Puzzler shows informed-attacker mechanism; pilot's D-experiment is the discrimination-against-uninformed-user inverse.
- **c047**: Shen et al. 2024 (ACM CCS, "Do Anything Now") — qs=5 — Empirical taxonomy of 1,405 in-the-wild jailbreak prompts. Full PDF (21 pages) extracted. **Key headline numbers**: Political Lobbying is most jailbreakable forbidden scenario (0.855 ASR average across 6 LLMs); five prompts achieve 0.95 ASR on ChatGPT and GPT-4. **ChatGLM (Chinese-origin) in evaluation set**: 0.973 ASR on Political Lobbying.
- **c052**: Alobaid, Jordà, Castillo 2026 (Echo Chamber) — qs=4 — Gradual-escalation MT attack. **ACCESS PARTIAL — abstract only**. Verified not retracted as of 2026-05-18. The closest published analog to the pilot's gradient-erosion finding in method/name. FRAMING INVERSION NOTED.

### V2 Deep-read (depth 2 — should — additional qs=4/5 with high pilot relevance)

- **c049**: Li et al. 2023 (EMNLP Findings, Multi-step Privacy Attacks on ChatGPT) — qs=4 — **ACCESS PARTIAL** — abstract only. Earliest peer-reviewed multi-step jailbreak paradigm reference; useful as historical anchor.
- **c063**: Yang et al. 2025 (ACL Findings, Chain of Attack) — qs=4 — **ACCESS PARTIAL** — abstract only. Multi-turn interrogation mechanism with 83% vs 64% ASR over single-turn baseline. Verbatim statement that "previous jailbreak attacks primarily focus on single-turn dialogue scenarios, leaving vulnerabilities in multi-turn dialogue contexts inadequately explored."
- **c064**: Srivastav & Zhang 2025 (ACL REALM workshop, Safe in Isolation, Dangerous Together) — qs=4 — **ACCESS PARTIAL** — abstract only. Agent-driven decomposition: "decomposing harmful queries into seemingly benign sub-tasks." 90%+ ASR across GPT-3.5-Turbo, Gemma-2-9B, Mistral-7B. Mechanistically the closest analog to the pilot's "individually benign turns, cumulatively unlocked" finding.
- **c068**: Chao et al. 2025 (IEEE SaTML, PAIR) — qs=4 — **ACCESS PARTIAL** — abstract only. Canonical iterative-refinement attack: "fewer than twenty queries" to produce jailbreak. Social-engineering framing. Cited as baseline by essentially every MT paper.
- **c073**: Perez et al. 2022 (EMNLP, DeepMind Red Teaming) — qs=5 — **ACCESS PARTIAL** — abstract only. Originating paper for automated red-teaming. Explicitly identifies "harms that occur over the course of a conversation" — earliest peer-reviewed multi-turn-harm recognition.
- **c071**: Deng et al. 2024 (NDSS, MASTERKEY) — qs=4 — Full PDF (first 4 pages) extracted. **CRITICAL CROSS-VENDOR DATA**: only paper in V2 set that includes Ernie (Baidu, Chinese-origin) in scope. Direct verbatim documentation that **only Ernie explicitly forbids "Content Harmful to National Security and Unity"** (Table I). Documents that repeated jailbreak attempts on Ernie cause account suspension. Cross-vendor ASR: OpenAI > Bing 14.51% > Bard 13.63%. **THIS IS THE SINGLE CLEANEST PUBLISHED L4-PLATFORM-LAYER REFERENCE.**
- **c048**: Ding et al. 2024 (NAACL Long, ReNeLLM/Wolf in Sheep's Clothing) — qs=4 — **ACCESS PARTIAL** — abstract only. Nested-scenario / narrative wrapping attack. Two-component generalization: Prompt Rewriting + Scenario Nesting.
- **c065**: Zhao & Zhang 2025 (ACSAC, Siren) — qs=4 — **ACCESS PARTIAL** — abstract only. Learning-based MT attack simulating real-world human jailbreak behaviors. 90% ASR (LLaMA-3-8B attacker vs Gemini-1.5-Pro). Methodologically the closest published analog to the pilot's natural-conversation design.
- **c051**: He, Wen, Qi 2026 (TRACE — Not All Turns Matter) — qs=4 — **ACCESS PARTIAL** — abstract only. Verified not retracted. **The single strongest published statement that turn-level contributions are non-uniform, phase-dependent, and target-specific.** Directly supports the pilot's observation that T1 identity declaration disproportionately weights downstream behavior. ~25% relative ASR improvement over RL baselines.

### V2 Skipped with reason

V2 papers not deep-read in this pass (13 of 32 accepted). All available for operator-override deep-read if needed.

- **c046** RoleLLM (ACL Findings 2024, qs=4): role-playing benchmark, not a safety study. Persona elicitation more than persona attack. Skip: relevance is structural/lexical not load-bearing for the pilot's identity-trigger argument. Notable for **bilingual scope (RoleLLaMA English + RoleGLM Chinese)** — operator may want to retrieve if persona-attack-vs-role-play distinction needs reinforcement.
- **c050** MultiBreak benchmark (2026 preprint, qs=3): 10,389 prompts / 2,665 intents scalable MT benchmark. Skip: methodological reference, not load-bearing.
- **c053** Defamiliarization Attack (MDPI Electronics 2026, qs=3): literary-theory framed reframing attack. Skip: peripheral to brief.
- **c054** ContextualJailbreak (2026 preprint, qs=3): evolutionary red-teaming. Skip: methodological, qs=3.
- **c055** Intention Deception (2026 preprint, qs=3): intent-inversion attack. Skip: qs=3 background.
- **c056** Persona-Invariant Safety Alignment (2026 preprint, qs=4): defensive counterpart. Skip: defensive framing, abstract-only access expected, low marginal value once c062 covers defense.
- **c057** Persona-Conditioned Adversarial Prompting (2026 IBM preprint, qs=4): multi-identity red-teaming. **NOTABLE SKIP** — this is methodologically the closest parallel to the pilot's identity-disclosure cells (multi-identity attacker conditioning). Operator may want to retrieve if pilot's methodology section needs more analog references.
- **c059** Adaptive Safe Context Learning (2026 preprint, qs=3): defensive MT alignment framing. Skip: defense paper, qs=3.
- **c060** SAFEDREAM (already implied), c062 MTSA (qs=4): defensive MT alignment frameworks. c062 abstract retrieved but not segmented in this pass — operator may want to retrieve full PDF if the Drafter needs defensive counter-evidence. Notable text: "in multi-round dialogues, malicious intentions may be hidden in interactions, leading LLMs to be more prone to produce harmful responses."
- **c069** MART (NAACL Long 2024, qs=4): Meta's multi-round automatic red-teaming defense. Skip: defensive industry methodology, less load-bearing.
- **c070** Survey on In-Context Learning (EMNLP Main 2024, qs=3): foundational ICL survey. Skip: c058 Wei et al. covers the ICL+alignment angle more precisely.
- **c075** Comprehensive Study of Jailbreak Attack vs Defense (ACL Findings 2024, qs=4): 9 attacks × 7 defenses survey. Skip: taxonomic, less load-bearing once c047 Shen et al. covers the empirical taxonomy.
- **c077** SafeDream (2026 preprint, qs=3): proactive jailbreak detection. Skip: qs=3 detection paper.
- **c079** Defensive Prompt Patch (ACL Findings 2025, qs=3): generalizable prompt-based defense. Skip: qs=3.
- **c080** Defending Against Alignment-Breaking Attacks via Robustly Aligned LLM (ACL Long 2024, qs=3): defensive framework. Skip: qs=3.

### V2 Retraction Check (per V2 brief instruction)

Gatekeeper flagged 2026 preprints for retraction check: c050, c051, c052, c054, c055, c056, c057, c077.
- **c051 He et al.**: verified, no retraction notice (May 2026-05-18).
- **c052 Echo Chamber**: verified, no retraction notice (submitted 2026-01-09, no notice).
- Other 2026 preprints (c050, c054, c055, c056, c057, c077): not deep-read in this pass; abstract metadata showed no retraction flag during V2 Gatekeeping. Recommend Drafter cite only via Segmenter-verified extracts (c051, c052) and not via skipped 2026 preprints unless full retraction-status verification is performed.

---

## Cross-paper themes noticed (V2)

For Synthesizer attention:

1. **The framing inversion (central conceptual contribution)**: Every single V2 paper that documents a multi-turn / context-erosion mechanism frames it as **malicious user attacking the model's defense**. The pilot frames the *same mechanism* as **the model implementing differential access policy based on user identity**. The technique inventory in the literature directly supports the pilot's mechanistic observations (Crescendo gradient, Wei ICA distribution-bias, Du attention-shifting, Puzzler knowledge-gating, Srivastav decomposition, He turn-credit asymmetry) — but the *agent of harm* is inverted. The pilot's user-rights frame is genuinely novel; no V2 paper occupies this position.

2. **Chinese-origin model coverage in V2 is thin but present**: c058 includes QWen-7b; c047 includes ChatGLM; c071 includes Ernie (policy-only). No V2 paper tests DeepSeek, GLM-4, or Qwen3 — all the models the pilot tests. No V2 paper tests Chinese-political-sensitivity topics. The pilot's empirical scope is genuinely uncovered.

3. **Political content is structurally fragile across alignment**: c047 finds Political Lobbying is THE most jailbreakable forbidden scenario across all 6 commercial LLMs (0.855 baseline ASR; 0.987 max-ASR). Pilot operates exactly in this least-robust zone, on a more contested political scope (cross-strait sovereignty / Tiananmen).

4. **Knowledge-gated access is genuinely undertheorized**: only c072 (Puzzler) directly operationalizes "informed-vs-uninformed" mechanism; c066 (Wen abstention survey) provides framework scaffold but does not enumerate the case. Confirms V2 Gatekeeper's observation that knowledge-gated cluster is thin — the pilot's D-experiment finding sits in a genuine theoretical gap.

5. **Multi-turn-as-mechanism is well-established (single-turn safety eval is broken)**: c081, c082, c052, c058, c061, c063, c064, c068, c051 all converge on this — single-turn alignment evaluation is insufficient. The L1 conversation-layer threat model has strong support; multiple authors (Crescendo, TRACE) state this in the strongest terms.

6. **L4 platform-layer is documented only via c071 (Ernie account suspension)**: This is the single cleanest published reference distinguishing Chinese vs Western chatbot platform-layer architecture. Drafter should give this prominence.

## Key quotes for Drafter consideration as anchor citations

1. **For the L1 conversation-layer existence claim**:
   - Russinovich et al. c081: "Multi-turn jailbreaks can easily circumvent these [single-turn alignment] measures."
   - Wen et al. c066: "Earlier context in multi-turn conversations can impact judgments for either query answerability or human values alignment in later conversational turns."
   - He et al. c051: "Turn-level contributions in multi-turn jailbreaking are non-uniform, phase-dependent, and target-specific."

2. **For the gradient-erosion mechanism**:
   - Du et al. c061: "Successful multi-turn jailbreaks can effectively disperse the attention of LLMs on keywords associated with harmful behaviors, especially in historical responses."
   - Russinovich et al. c081 Table 3: Three-turn sequence raises compliance from 17.3% to 99.9%.

3. **For the knowledge-gated access framing**:
   - Chang et al. c072: "Each clue is not sufficient to reveal the intent of the original malicious query, [so] traditional safety alignment mechanisms of LLMs struggle to defend against these types of attacks. This can be likened to playing a 'guessing game' with the LLM."
   - Wei et al. c058: P = λPH + (1−λ)PS distribution decomposition formalism.

4. **For the China-origin L4 platform layer**:
   - Deng et al. c071 Table I: "Only Ernie has a policy explicitly forbidding any harm to national security and unity."
   - Deng et al. c071: "Repeated unsuccessful jailbreak attempts on Ernie result in account suspension."

5. **For abstention as theoretical scaffold**:
   - Wen et al. c066: Three-axis framework (query / model / human-values); five expression types including "(v) refuses to offer concrete answers due to the lack of knowledge or certainty" (= the "我还没有学会" pattern).

## Operator overrides needed

1. **c021 (Gillibrand & Draper 2023) — CRITICAL** (V1 unchanged): qs=5 source on informational sovereignty. ACCESS BLOCKED. Drafter's Q2 framing depends on this. Operator must obtain via institutional access or author contact.

2. **c039 (Freedom House 2023) — CRITICAL** (V1 unchanged): qs=5 source. ACCESS BLOCKED. Operator should download PDF directly from freedomhouse.org/report/freedom-on-the-net/2023.

3. **c061 (Du et al. attention shifting 2025) — NEW V2 CRITICAL**: qs=5 source, abstract only via WebFetch. The mechanism paper for the entire L1 threat model. Operator should retrieve full PDF via AAAI institutional access at https://ojs.aaai.org/index.php/AAAI/article/view/34553. Without the full paper, Drafter cannot quote specific attention-mechanism evidence, only the abstract claim.

4. **c082 (Anil Many-shot Jailbreaking) — V2 NOTABLE**: Anthropic blog summary retrieved; full PDF not extracted. Recovery: `curl https://www-cdn.anthropic.com/af5633c94ed2beb282f6a53c595eb437e8e7b630/Many_Shot_Jailbreaking__2024_04_02_0936.pdf` (operator to verify URL).

5. **c057 (Persona-Conditioned Adversarial Prompting, IBM 2026)**: Notable V2 skip. Multi-identity persona red-teaming is methodologically the closest analog to the pilot's identity-disclosure cells. Operator may want to retrieve if the pilot's methodology section needs more direct analog references.

6. **Anchor literature gap unchanged**: Waight 2026, Samokhodskyi ELN 2026, Gary King — none in V1 or V2 accepted sets. Operator must manually locate and add, or Drafter must caveat dialogue-partner positioning.

7. **2026 preprint retraction verification (incomplete)**: c051 and c052 verified by Segmenter (no retraction). c050, c054, c055, c056, c057, c077 not deep-read; Drafter should treat these as background-only unless operator runs retraction verification.
