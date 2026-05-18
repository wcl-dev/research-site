# Synthesizer V2 Output — llm-user-side-bias

**Date**: 2026-05-18
**Stage**: synthesize_v2 → draft_v2
**Pass**: V2 integration of V1 (21 deep-read extracts) + V2 (17 new, c046–c082 range)
**Total extracts**: 38 (V1: 21 + V2: 17)
**Themes produced**: 11
**Unassigned extracts**: 0
**Brief questions covered**: Q1, Q2, Q3, Q4

---

## Structural Note: What This Thematic Structure Holds

The V1 Synthesizer organized 5 themes around the identity-trigger gap (t01 / t02) plus its theoretical frames (t03 / t04 / t05). The V2 pass adds 18 multi-turn / knowledge-gated extracts that do two things at once:

1. **They give the pilot's empirical observations published mechanistic explanations** — attention dispersion (c061 Du), ICL distribution-bias (c058 Wei), foot-in-the-door dynamics (c081 Crescendo), turn-level credit asymmetry (c051 He TRACE), context-dependent abstention (c066 Wen).
2. **They uniformly frame those mechanisms as malicious-user attacks on a defending model — never as the model's own differential governance policy.** The pilot's reframing is therefore not a gap *in coverage* but a gap *in framing*: the techniques are well-described; their use as discrimination is not.

V2 themes are organized around four ideas:

- A four-layer threat model (**t06**): L4 platform / L3 weights / L2 base capability / L1 conversation. This is the empirical scaffolding; the literature populates each layer.
- A framing inversion (**t07**): same mechanism, inverted agent. Drafter must build the central argument around this.
- A new injustice category (**t08**): the pilot's D-experiment anchored in the abstention/discrimination literature even though no published paper directly theorizes the asymmetry.
- A mechanism cluster (**t09**) and a structural-synthesis cluster (**t10**) explaining *how* identity persists across turns and *why* L1 is the meta-layer.

**t11** captures cross-model evidence — what the V2 literature does and does not say about Chinese-origin LLMs (DeepSeek, Qwen, GLM, ChatGLM, Ernie).

V1 themes (t01–t05) are preserved as **supporting frames** with V2 extracts integrated where they extend or anchor the V1 argument (c051 into t01; c071 into t03; c066 into t04; c047 into t05; c015 into t02).

Pilot signals carried forward into the Drafter:

- **S1 (V1 single-turn)**: DeepSeek refuses 228 for Taiwanese/Chinese identity; answers for no identity; topic-specific; language-switching (C → SC 合規, T → TC 合宜).
- **S2 (V1 single-turn)**: ChatGPT/Gemini show subtle identity-responsive framing without outright refusal.
- **S3 (V1 local)**: Vanilla local thinking-chain contains explicit CCP framing; abliterated version produces full Taiwan-mainstream historiography → model **knows** but is trained not to say.
- **S4 (V2 multi-turn — Stage 3)**: T1 identity persists into T2 thinking; safe-then-sensitive progression unlocks 5× content; adversarial follow-up unlocks ("大屠殺", "10,000–30,000"); identity carries over across topics; same role multi-turn after T-identity refusal → 2921 chars of substantive depth.

---

## t01 — Declared Identity as Access-Control Trigger: The Persistent Research Gap

- Cluster: `identity_trigger_gap` | Type: protocol | Q: Q1
- Extracts: c012, c013, c011, c002, c051 | Tiers: strong=2, contested=3

Existing peer-reviewed work establishes that declared user identity shifts LLM guardrail behavior (c012 Li EMNLP 2024; c013 Bernardelle ACM 2025), but no prior study applies this mechanism to national or geopolitical identity on Chinese-origin LLMs. The V1 pilot finding (DeepSeek refuses 228 conditional on Taiwanese/Chinese identity) sits in this gap; the V2 multi-turn evidence (c051 He TRACE) shows identity declared in T1 carries disproportionate downstream weight, extending the gap into the conversation dimension.

**Drafter anchors**: c012 — 44%/76% refusal for conservative/liberal personas. c011 — "Equitable access does not ensure equitable interaction quality." c051 (NEW) — "Turn-level contributions are non-uniform, phase-dependent, and target-specific."

---

## t02 — Topic-Level Censorship as the Established Baseline

- Cluster: `existing_llm_bias_studies` | Type: protocol | Q: Q1, Q3
- Extracts: c001, c003, c004, c005, c007, c008, c009, c015, c020 | Tiers: strong=4, contested=5

The dominant LLM political-bias literature measures censorship as a property of topic-model pairs (c001 Pan & Xu; c005 Ko; c008 Zhou & Zhang). Bang et al.'s content-vs-style framework (c020) reads the pilot's vocabulary signals (合規 vs. 合宜) as style-level access mechanism. c015 Casademunt connects the baseline to the pilot's L2 layer by showing censored models knowingly suppress recoverable information.

**Drafter anchors**: c001 — refusal rates BaiChuan 60.23% / DeepSeek ~36% / Ernie 32% / ChatGLM 10% vs. 0–2.8% non-China. c004 — "state-aligned information suppression far beyond China's digital borders." c015 — Qwen3 "occasionally answers correctly… indicating they possess knowledge they are trained to suppress."

---

## t03 — Informational Sovereignty as State Strategy and Platform-Layer Architecture

- Cluster: `geopolitical_frameworks` | Type: comparison_framework | Q: Q2
- Extracts: c021, c023, c041, c035, c037, c071 | Tiers: strong=2, contested=4

Chinese LLM content control is best read as deployment of a deliberate state information-sovereignty strategy (c023 Spartak three-pillar; c041 Atlantic Council $1.5B/yr discourse-power) with conceptual scaffolding from c021 Gillibrand & Draper. The parallel Russian case (c035 Pravda) and demonstrability of deliberate political fine-tuning (c037 PoliTune) establish that the pilot's findings sit within an extant institutional architecture, not a corporate-moderation choice. **c071 Deng MASTERKEY (NEW V2)** — the only V2 evidence that Ernie alone explicitly forbids "Content Harmful to National Security and Unity" and that the platform suspends accounts on repeated jailbreak attempts — anchors this theme to the **L4 platform layer**. This is the single cleanest published cross-vendor architectural distinction the Drafter has.

**Drafter anchors**: c023 — three-pillar framing. c071 (NEW) — "Only Ernie has a policy explicitly forbidding any harm to national security and unity" + Ernie account suspension. c035 — Pravda "information laundromat" across 80+ countries.

---

## t04 — Epistemic Injustice and the User-Rights Frame

- Cluster: `algorithmic_discrimination` | Type: comparison_framework | Q: Q2
- Extracts: c029, c033, c066 | Tiers: strong=2, contested=1

Identity-triggered differential LLM access can be theorized as epistemic injustice — specifically "access injustice" (c029 Kay) and "generative hermeneutical erasure" (c033 Mollema). **c066 Wen TACL 2025 (NEW V2)** supplies the three-axis (query / model / human-values) abstention decomposition that locates the pilot's identity-conditioned refusal precisely: not query-axis (the query is the same), not model-axis (the model has the knowledge — proven by abliteration), but **human-values-axis abstention conditioned on user identity** — a sub-case the survey acknowledges in general but does not enumerate. The pilot's contribution is to show the framework's blind spot.

**Drafter anchors**: c029 — four-dimensional taxonomy of generative algorithmic epistemic injustice. c033 — "Generative hermeneutical erasure = the automation of 'epistemicide'." c066 (NEW) — "Earlier context in multi-turn conversations can impact judgments for either query answerability or human values alignment in later conversational turns."

---

## t05 — AI as Geopolitical Infrastructure: Empirical Anchors

- Cluster: `cross_cluster` | Type: mixed | Q: Q3
- Extracts: c001, c005, c007, c039, c004, c047 | Tiers: strong=4, contested=2

A convergent body of peer-reviewed and authoritative grey-literature evidence validates that LLMs function as geopolitical information infrastructure. c001 Pan & Xu and c007 Guey et al. quantify the US-origin vs. Chinese-origin alignment split at scale (19,712 prompts × 11 LLMs). c004 Qiu CoT audit proves DeepSeek withholds knowledge it possesses. c039 Freedom House documents AI-for-censorship across 72 countries. **c047 Shen ACM CCS 2024 (NEW V2)** shows Political Lobbying is the structurally most-jailbreakable forbidden scenario across all 6 evaluated LLMs (0.855 baseline ASR), with **ChatGLM at 0.973 ASR** on Political Lobbying. The pilot's identity-conditioned 228 refusal sits at the intersection of this fragile zone.

**Drafter anchors**: c005 — DeepSeek R1 reasoning trace verbatim CCP narratives ("Taiwan has always been an inseparable part of China's territory"). c007 — US-origin → Pro-US, Chinese-origin → Pro-China across 19,712 prompts. c047 (NEW) — Political Lobbying 0.855 ASR; ChatGLM 0.973 ASR.

---

## t06 — The Four-Layer Threat Model: L4 / L3 / L2 / L1 as Empirical Structure

- Cluster: `cross_cluster` | Type: mixed | Q: Q1, Q3
- Extracts: c071, c037, c058, c004, c015, c081, c061, c051, c082, c064 | Tiers: strong=4, contested=6

The pilot's three empirical stages plus the V2 literature jointly support a four-layer model of LLM information control. The layers are **nested**: removing any upper layer reveals the threat at the next layer down.

| Layer | What it is | Pilot evidence | Literature anchor |
|------|------------|----------------|-------------------|
| L4 Service platform | Visible refusal + account discipline | Cloud single-turn 228 refusal; IP-independence | c071 MASTERKEY Table I; Ernie account suspension |
| L3 Weight alignment | Length compression + framing in weights | Vanilla 1/4–1/6 length; CCP framing in thinking-chain | c037 PoliTune; c058 Wei P=λPH+(1−λ)PS theory |
| L2 Base capability | Model has the knowledge; suppression is policy | Abliterated DeepSeek produces full Taiwan-mainstream historiography | c004 Qiu CoT audit; c015 Casademunt elicitation |
| L1 Conversation | Context modulates every turn's filtering | Stage-3 identity persistence; gradient erosion; adversarial unlock | c081 Crescendo; c061 Du attention-shifting; c051 He TRACE; c082 Anil; c064 Srivastav |

**Drafter anchors per layer**: L4 — c071 verbatim policy + suspension. L3 — c058 P=λPH+(1−λ)PS decomposition. L2 — c015 "occasionally answers correctly." L1 — c081 Table 3 (B alone 36.2% / A→B→C 99.9%).

---

## t07 — Framing Inversion: From Malicious-User Attack to Model-Side Governance

- Cluster: `cross_cluster` | Type: comparison_framework | Q: Q1, Q2
- Extracts: c081, c082, c061, c047, c052, c063, c064, c065, c068, c072, c073, c049, c048 | Tiers: strong=5, contested=8

Every V2 paper that documents a multi-turn / context-erosion / knowledge-gating mechanism frames the mechanism as a **malicious user attacking a defending model** — Crescendo (c081), Anil many-shot (c082), Du attention-shifting (c061), Shen DAN (c047), Echo Chamber (c052), Chain of Attack (c063), Srivastav decomposition (c064), Siren (c065), PAIR (c068), Puzzler (c072), Perez red-team (c073), Li multi-step (c049), Ding nested (c048).

**The pilot inverts the polarity.** The same mechanism — context modulates filtering — is the model implementing differential access policy based on declared user identity. The technique inventory transfers cleanly; the agent of harm and the direction of harm do not. This framing inversion is the pilot's central conceptual contribution and is uncovered by any V2 paper.

**Drafter must**:
1. State the inversion explicitly in the introduction.
2. For each V2 mechanism re-used, immediately re-cast in user-rights terms.
3. Acknowledge no V2 paper occupies this position; cite the absence as part of the contribution.

**Drafter anchors**: c081 — "highlight the shortcomings of the current alignment" (defensive framing). c072 — "guessing game with the LLM" (informed-attacker framing; pilot inverts to discriminated-uninformed-user). c082 — "double-edged sword" (Anthropic's own statement that long context is a new vulnerability class; pilot adds: also a new governance lever).

---

## t08 — Knowledge-Gated Discrimination as a New Injustice Category

- Cluster: `knowledge_gated_access` | Type: comparison_framework | Q: Q4
- Extracts: c066, c072, c047, c058, c049 | Tiers: strong=3, contested=2

The pilot's D-experiment — users who demonstrate prior knowledge ("大屠殺", "10,000–30,000 deaths") unlock substantive responses while equally-positioned uninformed users receive epistemic-denial refusals ("我还没有学会") — operationalizes a discrimination pattern that has theoretical scaffolding (c066 Wen three-axis) and an inverse-polarity operational analog (c072 Puzzler 96.6% QSR via implicit clues; SmoothLLM detects 4.0%) but no published direct theorization. c058 Wei supplies the ICL distribution-bias formalism. c047 Shen documents the persona-conditioning class. c049 Li is the earliest peer-reviewed multi-step paradigm reference.

**The literature gap is part of the theoretical contribution claim**: only c072 directly operationalizes the asymmetry, and even there frames the informed user as attacker — not the uninformed user as discrimination victim.

**Drafter anchors**: c072 — "Each clue is not sufficient to reveal the intent of the original malicious query… playing a 'guessing game' with the LLM" + 96.6% closed-source QSR + 57.9–82.7% above baselines. c066 — type (v) abstention "refuses to offer concrete answers due to the lack of knowledge or certainty" matches "我还没有学会" template.

---

## t09 — Identity Persistence and Conversational Drift: The Mechanism

- Cluster: `multiturn_dialogue_safety` | Type: protocol | Q: Q1
- Extracts: c061, c081, c051, c052, c047, c058, c073, c049, c068, c048 | Tiers: strong=5, contested=5

The pilot's Stage-3 observations find published mechanistic explanations:

| Pilot observation | Literature mechanism |
|-------------------|----------------------|
| T1 identity persists into T2 thinking | c061 Du — attention dispersion on refusal-trigger keywords in historical responses |
| Gradient erosion (safe→sensitive) | c081 Crescendo — foot-in-the-door; A→B→C raises compliance 17.3%→99.9% |
| Some turns matter disproportionately | c051 He TRACE — non-uniform, phase-dependent, target-specific |
| Conversational drift | c052 Echo Chamber — gradual escalation |
| Identity as role-conditioning | c047 Shen DAN — persona-assignment canonical class |
| ICL theoretical apparatus | c058 Wei — context shifts λ in P=λPH+(1−λ)PS |
| Iterative refinement | c068 PAIR — "fewer than twenty queries" |
| Nested scenario | c048 ReNeLLM — single-prompt narrative wrapping |
| Earliest precedent | c073 Perez 2022 — "harms that occur over the course of a conversation" |
| Earliest peer-reviewed multi-step | c049 Li 2023 — multi-step privacy extraction |

**Drafter anchors**: c061 — attention-dispersion mechanism verbatim. c081 — Table 3 turn-by-turn quantitative decomposition. c051 — turn-level non-uniformity.

---

## t10 — Conversation Layer (L1) Subsumes the Other Three Layers

- Cluster: `cross_cluster` | Type: mixed | Q: Q1, Q3
- Extracts: c081, c082, c064, c066, c058, c015, c061, c051, c004 | Tiers: strong=5, contested=4

The V2 literature converges: single-turn safety evaluation is insufficient because the conversation layer modulates every filter applied at higher layers. **L1 is therefore not a separate layer but the meta-layer that operates over the others** — the most subtle yet most persistent threat.

- L4 visible refusal disappears when conversation is structured benign (c081 cross-vendor jailbreak; c068 PAIR <20 queries).
- L3 framing compression can be re-baselined by ICL (c058 Wei: 1 shot → 8% → 20 shots → 81% ASR on GPT-4).
- L2 latent knowledge is recoverable (c015 Casademunt sampling/few-shot/fine-tuning recover withheld knowledge) when conversation primes the right context (c061; c004 CoT proof of withholding).

**Drafter anchors**: c081 — "Multi-turn jailbreaks can easily circumvent these [single-turn alignment] measures." c082 — "double-edged sword" + "new class of jailbreaking vulnerabilities." c064 — alignment fails for lack of "holistic context awareness." c066 — multi-turn-context abstention is a survey-identified gap.

---

## t11 — Chinese-Origin LLM Design Specificity: Cross-Model Evidence

- Cluster: `cross_cluster` | Type: mixed | Q: Q3
- Extracts: c001, c003, c005, c015, c047, c058, c071 | Tiers: strong=4, contested=3

The V2 literature touches Chinese-origin LLMs only in fragments. **The pilot's specific models (DeepSeek-R1, Qwen3, GLM-4) are not tested anywhere in the V2 corpus** — only adjacent models (QWen-7b, ChatGLM, Ernie, Qwen3) appear, and only in non-Chinese-political-sensitivity test scopes. V1 sources (c001, c003, c005) provide the empirical bulk.

| Paper | Chinese-origin coverage | Scope | Datum |
|-------|------------------------|-------|-------|
| c058 Wei (V2) | QWen-7b | ICA general | up to ~59% ASR |
| c047 Shen (V2) | ChatGLM | Political Lobbying (US) | 0.973 ASR |
| c071 Deng (V2) | Ernie | Policy only; suspension | (excluded from ASR) |
| c015 Casademunt | Qwen3 | Falun Gong / Tiananmen | "occasionally answers correctly" |
| c001 Pan & Xu | DeepSeek + ChatGLM + Ernie + BaiChuan | 145 political questions | DS ~36% refusal |
| c003 Naseh | DeepSeek | 10,030 prompts | 99.57% ZH censorship |
| c005 Ko | 6 Chinese-origin incl. DS-R1, Qwen3 | Taiwan sovereignty | 0/10 |

**The pilot's empirical scope (its specific models × its specific topics) is genuinely uncovered.** This strengthens the contribution-novelty claim. Drafter must not imply any V2 paper tests the pilot's models on its topics.

**Drafter anchors**: c071 — Ernie-only national-security policy. c047 — ChatGLM 0.973 ASR. c015 — Qwen3 Falun Gong / Tiananmen partial-suppression.

---

## Coverage Summary

| Brief Q | Themes | Count |
|---------|--------|-------|
| Q1 — Identity-trigger + multi-turn priority | t01, t02, t06, t07, t09, t10 | 6 |
| Q2 — Theoretical frameworks | t03, t04, t07 | 3 |
| Q3 — Empirical validation + Chinese-origin | t02, t05, t06, t10, t11 | 5 |
| Q4 — Knowledge-gated discrimination | t08 | 1 (by design — literature thin) |

**No uncovered questions.** Q4 has only one dedicated theme because the underlying literature is genuinely thin (cited as such by Gatekeeper, Segmenter, V1 + V2 Synthesizer). This thinness is itself part of the contribution claim.

| Theme type | Count | Themes |
|-----------|-------|--------|
| protocol | 3 | t01, t02, t09 |
| comparison_framework | 4 | t03, t04, t07, t08 |
| mixed | 4 | t05, t06, t10, t11 |

Multi-assigned extracts (high overlap is expected — V2 evidence supports cross-theme empirical-structural integration): c081 ∈ {t06, t07, t09, t10}; c061 ∈ {t06, t07, t09, t10}; c047 ∈ {t05, t07, t08, t09, t11}; c058 ∈ {t06, t08, t09, t10, t11}; c066 ∈ {t04, t08, t10}; c051 ∈ {t01, t06, t09, t10}; c071 ∈ {t03, t06, t11}; c015 ∈ {t02, t06, t10, t11}; c004 ∈ {t02, t05, t06, t10}.

---

## Open Questions for Drafter

1. **c021 Gillibrand & Draper — CRITICAL — ACCESS BLOCKED** (V1 unchanged): t03 keystone remains paywalled. Drafter must work from abstract-level characterization only.
2. **c039 Freedom House 2023 — CRITICAL — ACCESS BLOCKED** (V1 unchanged): t05 institutional anchor inaccessible.
3. **c061 Du attention-shifting — NEW V2 CRITICAL — ACCESS PARTIAL**: qs=5 mechanism paper available only as abstract. The mechanism claim is verbatim-quote-safe; quantitative numbers from the full paper are not.
4. **c082 Anil Many-shot — NEW V2**: only Anthropic blog summary retrieved; specific cross-model ASR numbers require full PDF.
5. **Anchor literature absent**: Waight 2026 (Nature), Samokhodskyi/ELN 2026, Gary King — never appeared in V1 or V2. Drafter must caveat dialogue-partner positioning.
6. **2026 preprint retraction verification incomplete**: c051 and c052 verified by Segmenter. Others (c050, c054–c057, c077) not deep-read; do not rely on them.
7. **Pilot's specific models (DeepSeek-R1, Qwen3, GLM-4) on its specific topics (228, Tiananmen, cross-strait) have zero direct comparators in the V2 literature** — captured in t11. Frame as novelty, not limitation.
8. **Framing inversion (t07) must be carried explicitly into the article's central argument.** The risk of Drafter reading V2 extracts purely for mechanism descriptions and forgetting the "agent of harm" inversion is the single biggest risk on this handoff. Each V2 extract's "Caveats / limitations" section flags it; Drafter should re-read those sections.
9. **counter_framings absent in brief_expanded.yaml** — balance check N/A (unchanged from V1). However, every V2 extract's framing is *itself* a counter-framing to the pilot's framing (V2 = attack framing; pilot = governance framing). Drafter should treat the entire V2 literature as the implicit counter-framing.
10. **No empirical comparator for the pilot's Stage-3 multi-turn findings in a politically-sensitive cross-lingual setting.** Closest is c065 Siren (learned natural-conversation attacks, but not Chinese-origin model and not political content). Pilot's MT methodology is genuinely novel in this scope.

---

## Theme-Level Drafter Guidance Summary

| Theme | Drafter use |
|-------|-------------|
| t01 | Literature gap — identity-trigger mechanism is established but applied to US-demographic identities, not geopolitical identity on Chinese-origin LLMs. |
| t02 | Established baseline the pilot departs from. |
| t03 | "Why it's policy, not bug" argument; L4 platform anchor via c071. |
| t04 | User-rights framework; c066 supplies the precise scaffold. |
| t05 | Empirical credibility scaffolding; political-content fragility added via c047. |
| t06 | **Empirical-structural spine of the article.** Use the L4/L3/L2/L1 table as organizing framework. |
| t07 | **Central conceptual contribution.** Frame the entire article around the inversion. |
| t08 | New injustice category; literature thinness is part of the contribution. |
| t09 | The mechanism — how identity persists and drifts across turns. |
| t10 | Synthesis claim — L1 is the meta-layer over L2/L3/L4. |
| t11 | Cross-model evidence — bound the contribution by acknowledging what is and is not tested. |
