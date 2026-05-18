# Review of llm-user-side-bias insight_v1.md

**Reviewed on**: 2026-05-15
**Draft**: projects/llm-user-side-bias/pipeline/draft/insight_v1.md
**Sources consulted**: accepted.jsonl (32 records), extracts/ (17 deep-reads, including INDEX.md), brief.md

---

## Verdict

- Section 一 (Literature positioning / empty niche): WARN — needs tightening on two specific statistics
- Section 二/Framework 1 (Informational sovereignty): WARN — c021 claim goes beyond what the access-blocked abstract warrants; Spartak three-pillar description has a specific attribution mismatch
- Section 二/Framework 2 (Epistemic injustice): WARN — one claim attributed to c029 uses language not present in the extract; c033 paraphrase overstates "knowledge extinction" framing
- Section 三 (Contribution): OK — accurately scoped
- Section 四 (Argument path): WARN — c003 statistic misquoted; c039 cited beyond available content
- Section 五 (Gaps): OK — honestly enumerated; one additional gap not listed

Overall: REVISE — most issues are single-sentence corrections, but two statistical misquotations and one abstract-overreach are substantive and must be fixed before the advocacy piece is written.

---

## VERIFIED CLAIMS

The following claims were checked against extracts and confirmed accurate:

1. Pan & Xu (2026) 145-question benchmark, BaiChuan 60.23% refusal rate, DeepSeek ~36%, non-China models at 0% [c001] — VERIFIED. Extract passage 1 verbatim: "BaiChuan: 60.23% of prompts"; "DeepSeek: ∼36%"; "0% for GPT 3.5 and GPT 4o."

2. Qiu et al. (2025) chain-of-thought vs. output comparison mechanism [c004] — VERIFIED. Extract passage 3 confirms Type 2 censorship: "model generates an on-topic CoT, yet the subsequent answer is off-topic." Claim that "model knows the answer but deliberately does not output it" is an accurate characterization.

3. Ko (2026) "17 tested models, 15 show language bias, all 6 Chinese-origin models fail" [c005] — VERIFIED. Abstract verbatim: "15 out of 17 tested models exhibit measurable language bias, with Chinese-origin models showing particularly severe issues."

4. Ko (2026) CCP propaganda verbatim in DeepSeek R1 chain-of-thought [c005] — VERIFIED. Extract passage 3 confirms "Taiwan has always been an inseparable part of China's territory since ancient times" appears in R1's reasoning traces; draft quotes this as "台灣自古以來就是中國領土不可分割的一部分" — this is an accurate Chinese rendering of the extract's English translation of the verbatim CoT.

5. Li et al. (2024) conservative vs. liberal persona asymmetric refusal rates: 44% vs. 76% [c012] — VERIFIED. Extract passage 2 verbatim: "conservative-leaning requests have a refusal rate of 44% for conservative personas and 76% for liberal personas."

6. Atlantic Council c041 "$1.5 billion annually" in propaganda [c041] — VERIFIED. Extract passage 2 verbatim: "Over $1.5 billion spent annually on propaganda since 2008."

7. Atlantic Council c041 "four State Key Laboratories utilizing big data" [c041] — VERIFIED. Extract passage 3 verbatim: "China launched 'four State Key Laboratories dedicated to using big data to better tailor content to specific audiences.'"

8. Amiri-Margavi et al. (2026) zero-refusal-but-quality-disparity finding [c011] — VERIFIED. Extract passage 2 verbatim: "Both models exhibit zero refusal rates across all identities... we observe systematic, model-specific disparities in interaction quality."

9. Bernardelle et al. (2025) persona injection as effective political output vector [c013] — VERIFIED. Extract confirms "persona assignment is an effective vector for altering political output."

10. Spartak (2025) three legislative pillars: Cybersecurity Law, Data Security Law, Personal Information Protection Law [c023] — VERIFIED. Extract passage 2 lists all three, enacted 2016-2021.

---

## UNSOURCED CLAIMS

**U1. "合規"/"合宜" vocabulary description presented as established fact**

Draft (Section 一): "拒絕詞彙還依身份分別採用「合規」（簡體中文，監管語彙）或「合宜」（繁體中文，社會適切語彙）" — and again in Section 二: "「合規」詞彙對應立法支柱...繁體中文使用者收到的「合宜」軟性語言則對應文化支柱"

This is cited only to [pilot], which is the author's own unpublished 30-cell experiment. No external source confirms that "合規" is specifically regulatory vocabulary or that "合宜" specifically signals soft social-appropriateness framing. The draft correctly marks this as [pilot] only, but the elaboration in Section 二 — mapping each vocabulary choice directly onto specific pillars of Spartak's framework — treats a single-experiment observation as an established structural fact. This mapping from pilot observation to three-pillar theory is an inferential leap not warranted by either source alone.

Suggested revision: Mark the three-pillar mapping explicitly as "pilot study's interpretive hypothesis, requiring verification."

**U2. Gemini IP-driven vocabulary difference ("屠殺" vs. "軍事鎮壓") as a "訊號"**

Draft (TL;DR): The three pilot signals are listed as established findings including "Gemini IP 驅動詞彙差異." No citation other than [pilot]. This is fine as a pilot observation, but the TL;DR presents it alongside the more robustly documented DeepSeek finding without distinguishing its weaker evidential status (single-data-point vocabulary difference). If the review is assessing whether to publish, this asymmetry should be made explicit.

Suggested revision: Add a qualifier in TL;DR differentiating the strength of the three pilot signals.

**U3. "宣告台灣身份或中國身份的使用者拒絕回答...而且...不同" characterization**

Draft Section 一 presents the pilot design ("30 個實驗格") and then describes DeepSeek's behavior in detail. The description is accurate to the [pilot] cite. This is acceptable as an unpublished pilot claim — no external validation required for the characterization of the pilot's own data, which the author controls. Not flagged as a problem, but noted that the pilot data itself is not peer-reviewed and this context should be explicit in any publication.

---

## OVERCONFIDENT CLAIMS

**OC1. c003 statistic misquoted — critical**

Draft (Section 四, step 2): "97.3% 的政治敏感提問遭到強硬拒答"

This is factually wrong. The extract for c003 (passage 5) states: "66 out of 96 categories (68.75%) result in a 100% censorship rate." The 97.3% figure appears in Table I of c003 as the proportion of Type 1 (hard refusal) vs. Type 2 (soft refusal) among censored prompts — it is the breakdown within the censored set, not the overall refusal rate of all political queries. The actual per-category censorship rate ceiling is 100% for 68.75% of categories, and 89.58% of categories have rates above 90%. The draft converts an internal-breakdown statistic (97.3% of censored prompts are Type 1) into a claim about overall refusal rate. This is a misrepresentation of the source.

Source passage (c003 extract, passage 5): "66 out of 96 categories (68.75%) result in a 100% censorship rate." Table I shows "97.3% Type 1, 2.7% Type 2" — this is a type-distribution statistic, not a total-refusal-rate statistic.

Suggested revision: Replace "97.3% 的政治敏感提問遭到強硬拒答" with "96個主題類別中68.75%達到百分之百拒答率 [c003]."

**OC2. c003 English refusal rate claim in TL;DR inverted**

Draft (TL;DR and Section 一): "DeepSeek R1 在 96 個主題類別中有 68.75% 達到百分之百拒答率，且跨語言一致：英語 100%、中文 99.57%"

The cross-language figures are internally consistent with the extract (English 100.00%, Chinese 99.57%). However the framing "跨語言一致" is slightly misleading: the extract shows English has a *higher* censorship rate (100%) than Chinese (99.57%), which is a notable finding (censorship is not lower in English). The draft treats this as evidence of consistency when it actually shows English-language DeepSeek censorship is marginally *more* complete. This is not wrong, but it undersells a counterintuitive finding.

Suggested revision: Acknowledge that English censorship rate equals or slightly exceeds Chinese — this strengthens the argument that censorship is model-embedded, not language-selective.

**OC3. c021 three-concept distinction stated as if verified from full text**

Draft (Section 二, Framework 1): "Gillibrand & Draper（2023）區分了三個概念：資料主權（誰擁有資料）、數位主權（誰控制基礎設施）、資訊主權（誰透過 AI 系統控制什麼資訊流向誰）"

The c021 extract is ACCESS BLOCKED. The extract record states only that the paper "proposes 'informational sovereignty' as a new framework distinct from data sovereignty" (from the accepted.jsonl abstract). The three-way breakdown (data sovereignty / digital sovereignty / informational sovereignty with parenthetical definitions) is not confirmed in the available abstract text. The parenthetical glosses ("誰擁有資料", "誰控制基礎設施", "誰透過 AI 系統控制什麼資訊流向誰") may be accurate, but they cannot be verified from available materials.

The draft's own footnote says "全文因付費牆不可及，以下依據摘要層次引用" — but this disclaimer appears only after the detailed three-concept breakdown has already been presented as if established. The detail level of the claim exceeds what the abstract warrants.

Verified available content: the abstract confirms informational sovereignty is "distinct from data sovereignty" — only one of the two claimed distinctions (data vs. informational) is directly supported. The additional distinction from "digital sovereignty" is inferred, not confirmed.

Suggested revision: Limit c021 claim to "Gillibrand & Draper propose 'informational sovereignty' as a concept distinct from data sovereignty" and note the digital sovereignty distinction is inferred from the general framing of the paper, pending full-text access.

**OC4. c029 "access injustice" definition overstates available evidence**

Draft (Section 二, Framework 2): "Kay、Kasirzadeh 與 Mohamed（AAAI AIES 2024）在生成式 AI 語境中定義了「生成式演算法知識不平等」，其中最相關的一個維度是存取不平等（access injustice）——「特別在多語境下，知識不平等從資訊取用差異中浮現」"

The extract for c029 is partial (abstract + structure from OJS; preprint available but details unspecified). The quoted definition "特別在多語境下，知識不平等從資訊取用差異中浮現" is a paraphrase, not a verbatim quote. The available extract states only that "access injustice" is one of four dimensions with "particular attention to 'multilingual contexts.'" The specific formulation "知識不平等從資訊取用差異中浮現" is a Drafter construction, not from the source.

The extract caveat specifically warns: "'Access injustice' dimension details are not specified in available content beyond the naming — Drafter should not over-claim specific passage quotes beyond what is above."

Suggested revision: Remove the quoted definitional phrase; replace with "Kay et al. identify 'access injustice' as one of four dimensions of generative algorithmic epistemic injustice, with particular relevance to multilingual contexts [c029]."

**OC5. c033 "知識滅絕" framing overstates the paper's scope**

Draft (Section 二, Framework 2): "透過 LLM 對概念多元性的壓制，自動化地執行「知識滅絕」（epistemicide），系統性地消除特定知識框架的能見度"

The c033 extract confirms "epistemicide" is used by Mollema, and the mechanism is described as "AI systems' 'view from nowhere' epistemically inferiorizes non-Western epistemologies." However, the c033 paper focuses on suppression of non-Western epistemologies broadly — the extract caution note explicitly states: "Hermeneutical erasure concept focuses on suppression of non-Western epistemologies broadly — the pilot's case is more specific (national identity triggering access denial on a particular historical event)."

The draft applies "epistemicide" to the Taiwan 228 Event case as if it is a direct fit. This is an inferential extension of a concept designed for broader epistemological hierarchy critique. The application is plausible but requires explicit acknowledgment that this is the author's extension of the concept, not what c033 directly claims.

Suggested revision: Add "此概念原指去殖民學術脈絡中的普遍知識壓制；先導研究將其延伸至國族身份觸發的歷史知識存取場景" to clearly mark the inferential extension.

---

## OVERLOOKED SOURCES

**OS1. c002 (de Man 2025) — emotional framing modulates Chinese LLM censorship**

The draft never cites c002. The de Man (2025) paper directly tests how prompt-level framing (emotional framing) modulates censorship in Kimi.com and Ernie 4.5 Turbo — an even closer methodological parallel to identity-triggered refusal than some cited sources. The extract notes "four behavioral patterns including unusual transparency about safety layers." This source would strengthen Section 一's claim that "prompt framing modulates Chinese LLM censorship" is a documented mechanism, not only identity-framing.

Why it matters: The draft argues identity framing triggers differential access, but only cites c012 (US political identity) and c013 (Western political compass) as precedents. c002 provides a Chinese-LLM-specific framing-sensitivity precedent that directly mirrors the pilot mechanism.

**OS2. c008 (Zhou & Zhang 2024, Nature Scientific Reports) — bilingual GPT framing inconsistency**

The draft cites c007 (Guey et al.) for the broad geopolitical bias mapping but never cites c008, which is a qs=5 peer-reviewed paper in Nature Scientific Reports specifically documenting Chinese/English political framing inconsistency in GPT. The INDEX.md notes c008 shows "same model gives pro-China framing in Chinese, more critical framing in English; attributes gap to Chinese state censorship in training corpora."

Why it matters: Section 一 argues all existing research focuses on "model-level" not "user-level" questions. c008 partially overlaps with the identity-trigger mechanism (language as identity proxy). Citing c008 would strengthen the background map and also force the author to be more precise about what distinguishes the pilot from language-switching studies.

**OS3. c015 (Casademunt et al. 2026) — censored LLMs know but suppress**

Draft cites c004 (Qiu et al.) for the "model knows but withholds" argument. c015 provides additional independent evidence for this claim with different methodology (elicitation techniques show withheld knowledge can be recovered). Both sources support the same claim; the draft's omission of c015 misses an opportunity to show convergent evidence from multiple independent studies.

**OS4. c009 (Yadav et al. 2025) — safety vs. propaganda distinction**

Draft makes a distinction between "safety-driven refusals" and "state-directed censorship" implicitly throughout but never operationalizes it with an academic source. c009 (Yadav et al.) directly operationalizes exactly this distinction with the PSP dataset. Citing c009 would sharpen the conceptual contribution claim in Section 三.

---

## SOURCE-LIMITATION FLAGS

**SL1. c021 (Gillibrand & Draper 2023 IJODR) — CONFIRMED ACCESS BLOCKED**

The draft appropriately flags this ("全文因付費牆不可及"). However, the three-concept breakdown (see OC3 above) goes beyond what the abstract supports. The draft's inline warning comes *after* the detailed claim has been presented. The warning should precede or be integrated into the specific claim, not placed after the full elaboration.

Additionally: c021 is described in the draft's confidence table as "中" confidence with "取得 c021 全文後升至高" — this is accurate self-assessment. But Section 二 presents the informational sovereignty framework with more assurance than this confidence rating warrants. The section text and the confidence table are internally inconsistent.

**SL2. c039 (Freedom House 2023) — CONFIRMED ACCESS BLOCKED (404)**

The draft appropriately flags this. The claim "Freedom House 72 國記錄" in Section 四 step 5 and the confidence table is correctly cited as abstract-level. The draft states "72 國、AI 作為壓制工具" which is confirmed in the gate record abstract — this is within bounds. The draft does not over-specify from c039 content, so no violation here. However, the advocacy piece framing in Section 四 relies on c039 as a primary policy anchor without being able to cite specific findings. This is a structural weakness for the final advocacy piece even if the current memo handles it correctly.

**SL3. Three anchor papers (Waight 2026, Samokhodskyi/ELN 2026, Gary King)**

The draft uses [anchor: waight2026], [anchor: samokhodskyi2026], [anchor: gary_king] notation and explicitly acknowledges these are not in the accepted set. However, two specific claims require scrutiny:

(a) Draft (Section 一): "從 Waight 等人（2026）/Samokhodskyi-ELN（2026）的「訓練/語言側機制研究」出發" — the characterization of Waight as "訓練側機制研究" is consistent with brief.md's description ("State media in training data correlates with biased outputs"). The characterization of Samokhodskyi as "語言側機制研究" is consistent with brief.md ("Russian-language prompts reproduce Kremlin framing; language-side mechanism"). These are within bounds of what the brief says.

(b) Draft (Section 四, step 3): "Gary King 的中國網路審查研究 [anchor: gary_king] 在此處作為歷史比較出現：LLM 審查是否延續了既有網路管控邏輯" — The brief says only "mechanisms of Chinese internet censorship; relevance: does LLM content control mirror or diverge from existing internet censorship frameworks?" The draft correctly frames this as an open question rather than attributing a specific answer to Gary King. This is within bounds.

No violations for anchor papers beyond what is already disclosed.

**SL4. c011 (Amiri-Margavi et al. 2026) — nationality-specific findings not accessible**

The draft claims c011 shows "身份（包含國籍）仍會造成系統性互動品質差異." The c011 extract confirms nationality is one of three identity variables tested (alongside age and gender), and the abstract confirms "systematic, model-specific disparities in interaction quality." However, the extract explicitly cautions: "Specific nationality findings not detailed in accessible content (which nationalities, which differences)." The draft presents the nationality finding as established when the extract acknowledges it cannot be verified from available content. This is a mild overreach but worth noting.

Suggested revision: Add "包含國籍（具體差異模式待全文確認）" or similar hedge.

---

## STRUCTURAL NOTES

**ST1. Pilot data not disclosed as unpublished/unreviewed**

The [pilot] citation is used throughout as if it has equivalent status to the cited peer-reviewed literature. The draft never explicitly states that the pilot study is unpublished, not peer-reviewed, and based on 30 cells. This is acceptable in a private research memo (as the document header states), but if this memo is used as a basis for an advocacy piece or cited document, the pilot's status must be made explicit. The brief describes it as "30 cells: ChatGPT / Gemini / DeepSeek × TW/HK IP × N/T/C identity × 2 topics" — this is a very small experiment and should be characterized as exploratory/hypothesis-generating, not as established evidence.

**ST2. The "zero existing research" niche claim is strong but unverified**

Draft (Section 一): "沒有任何研究問：同一個使用者，若宣告不同國族身份，會得到不同品質的回答嗎？" and Section 三: "但沒有任何研究將兩者交叉"

This is a strong negative existence claim. The accepted set does not contain such research, but the accepted set is not a complete census of the field — it is 32 papers selected from 45 candidates (which themselves represent an imperfect collection). The INDEX.md notes c006 (Urman & Makhortykh 2024) was access-blocked and skipped — this cross-lingual guardrail study of ChatGPT/Gemini on Russia topics might partially address this space. The niche claim is likely correct but should be hedged: "no research we have located" rather than "no research exists."

**ST3. Framework-to-pilot mapping in Section 二 is tight but inferential**

The three-pillar mapping of pilot findings onto Spartak's framework (c023) is intellectually creative and plausible, but the extract cautions that Spartak's paper "does not directly discuss LLMs specifically — discusses broader Chinese internet information control infrastructure." The draft treats this mapping as if it is analytically established rather than the author's application of an adjacent framework. This should be flagged as the author's interpretive argument, not a finding that c023 directly supports.

**ST4. c003 "10,030 道問題資料集" is described accurately but the dataset is English-primary**

Draft (Section 一): "建立了更大規模的 10,030 道問題資料集" — accurate.
But the draft does not mention that the 10,030 prompts are English-language only (cross-language comparison was a separate translation-based analysis). The cross-language rates (English 100%, Chinese 99.57%) come from a translated subset. This is a methodological nuance relevant to how the study is used to support claims about Chinese-language censorship.

**ST5. Section 四 "argument path" is addressed to an assumed advocacy piece**

The document header states "目標讀者：研究者本人（非最終倡議文章）" but Section 四 ("最有力的論述路徑") is structured as a blueprint for a public advocacy article. This creates a dual-audience ambiguity that affects how confidently certain claims can be stated. The reviewer flags this not as a content error but as an audience-clarity issue: if Section 四 will inform a public-facing piece, the source-limitation flags (SL1-SL4) become critically important there.

**ST6. Gap in "What we don't know" — c008 and language-vs-identity distinction not addressed**

The draft's Section 五 lists five gaps but does not flag the following: the relationship between language-triggered bias (documented by c008, c005, and others) and identity-triggered bias (the pilot's claim) is not fully theorized. Ko (2026) shows Chinese model censorship is language-*consistent* (same in English and Chinese), which actually complicates a simple "language = identity signal" explanation. The pilot's mechanism (declared identity in natural language, not language choice itself) is a distinct mechanism, but the draft does not explicitly contrast the two and explain why the pilot's mechanism adds something the language-trigger studies have not already captured.

---

## Per-section audit using standard lenses

### Section 一 — Literature Positioning

**L1 (Citation density)**: All major factual claims are cited. No orphan factual claims detected. Density is appropriate.

**L2 (Claim-vs-source fidelity)**: 
- c001 refusal rates: VERIFIED (see VC1)
- c003 "97.3%" statistic: MISMATCH (see OC1) — this is the most serious fidelity error in the draft
- c005 "17 models, 15 fail": VERIFIED
- c005 "逐字重複的中共黨國宣傳文字": VERIFIED — extract passage 3 confirms verbatim CCP propaganda in R1 reasoning
- c007 "19,712 個雙語提示測試 11 個模型": VERIFIED (c007 abstract verbatim)
- c012 "44% 對 76%": VERIFIED (extract passage 2)

**L3 (Counter-evidence honesty)**: 
Ko (2026) extract passage 2 shows Chinese model censorship is language-consistent (not language-selective) — this actually *complicates* the "language = identity signal" interpretation and supports a stronger "model-embedded identity trigger" claim. The draft does not engage with this nuance. It is not wrong, but the counter-evidence (that Ko's finding undermines simple language-switching explanation) strengthens the pilot's claim when properly engaged. The draft misses an opportunity here.

**L4 (Overlooked sources)**: c002 (de Man 2025), c008 (Zhou & Zhang 2024) are unmentioned (see OS1, OS2).

**L5 (Confidence calibration)**: "中國源模型系統性審查的背景前提" rated "高" — warranted given c001 (qs=5), c003, c004, c005, c007 convergence.

### Section 二 — Theoretical Frameworks

**L1 (Citation density)**: All claims cited. c021 cited with appropriate warning.

**L2 (Claim-vs-source fidelity)**:
- c021 three-concept breakdown: EXCEEDS AVAILABLE EVIDENCE (see OC3)
- c023 three pillars: VERIFIED (extract passage 2)
- c023 surveillance systems "識別...隱性暗示": PARTIALLY VERIFIED — the specific quote "能夠識別與政治敏感話題相關的隱性暗示或隱喻" is a paraphrase of the extract's "capable of identifying not only explicit violations, but hidden hints or metaphors related to politically sensitive topics." The paraphrase is accurate in substance.
- c029 "access injustice" definition: EXCEEDS AVAILABLE EVIDENCE (see OC4)
- c033 "epistemicide": VERIFIED as a term used in the paper, but application to pilot is an inferential extension (see OC5)
- c037 PEFT "以極低成本嵌入模型": VERIFIED — extract confirms "PEFT enables efficient ideological alignment" and the paper studies "parameter-efficient" fine-tuning

**L3 (Counter-evidence honesty)**: The c037 extract cautions that the paper "shows how easily bias can be embedded; doesn't prove that Chinese developers used these specific techniques." The draft uses PoliTune to argue "身份觸發的差別回應是可以設計、可以實作的政策選擇" — this is a reasonable inference from c037 but should be qualified as "technically feasible" not "demonstrated."

**L4 (Overlooked sources)**: c009 (Yadav et al. safety/propaganda distinction) would sharpen the "设计選擇 not safety" argument in this section.

**L5 (Confidence calibration)**: "資訊主權" rated "中" — appropriate given c021 access block.

### Section 三 — Contribution Statement

**L1**: Single citation-free section — accurately described as no-citation contribution synthesis. No orphan factual claims.

**L2**: Not applicable (no citations to verify).

**L6 (Brief question coverage)**: Section 三 addresses Priority 1 (empty niche) and Priority 3 (validation) from the brief. Priority 2 (theoretical frameworks) is covered in Section 二.

**L8 (Concept-fidelity)**: No themes.jsonl with evidence_scope_distribution detected in project. L8: skipped — project does not use Seg2 evidence_scope tagging.

### Section 四 — Argument Path

**L2 (Key fidelity check)**:
- "97.3% 的政治敏感提問遭到強硬拒答": MISMATCH — already flagged as OC1
- "審計研究確認模型「知道答案但刻意不輸出」" [c004]: VERIFIED
- "Freedom House 72 國記錄 [c039]": within bounds of access-blocked abstract

**L3**: c035 (Pravda/Russia) is used as a parallel case. The extract cautions that Russia's mechanism (training-data poisoning) differs from China's (direct model alignment). The draft does not acknowledge this distinction: "俄羅斯正在用相同邏輯毒化 AI 訓練資料" (emphasis mine) — the use of "相同邏輯" (same logic) elides the mechanistic difference. The two states use *different* mechanisms (Russia: training data contamination; China: alignment/fine-tuning). Calling it "同一邏輯" overstates the parallel.

Suggested revision: Replace "相同邏輯" with "類似目標但不同機制" or similar.

### Section 五 — Gaps

**L7 (Gaps)**: The five gaps listed are legitimate and complete for the sources the Drafter knew about. The additional gap not listed (see ST6) is the language-vs-identity distinction theoretical gap.

---

## Summary Recommendations

1. **CRITICAL — Fix c003 statistic** (OC1): "97.3% 的政治敏感提問遭到強硬拒答" misrepresents the source. Replace with the correct figure: 68.75% of topic categories reach 100% refusal rate. This is the most factually serious error.

2. **SUBSTANTIVE — Limit c021 claims to abstract level** (OC3): The three-way data/digital/informational sovereignty breakdown with parenthetical definitions cannot be verified from available material. Trim to what the abstract confirms; mark the rest as "inferred."

3. **SUBSTANTIVE — Remove or re-attribute the c029 quoted definition** (OC4): The phrase "特別在多語境下，知識不平等從資訊取用差異中浮現" is Drafter-constructed paraphrase, not a source quote. Use only what the abstract confirms.

4. **TIGHTEN — Flag c033 "epistemicide" as an inferential extension** (OC5): The concept applies broadly to non-Western epistemology suppression; the pilot's case is a specific instantiation the author is proposing, not what Mollema directly claims.

5. **TIGHTEN — Distinguish Russia/China mechanisms in Section 四** (L3, Section 四): "相同邏輯" overstates the parallel. Russia uses training-data poisoning; China uses alignment/fine-tuning. These are structurally different geopolitical AI control strategies.

6. **ADD — Consider citing c002 and c008 in Section 一** (OS1, OS2): These overlooked sources directly strengthen the framing-sensitivity and bilingual-inconsistency background map.

7. **ADD — Consider citing c009 in Section 二/三** (OS4): Yadav et al.'s safety/propaganda distinction operationalizes the paper's conceptual contribution claim more precisely.

8. **STRUCTURAL — Add explicit statement that pilot is unpublished/exploratory** (ST1): The memo is private, but any downstream use requires this caveat to be prominent.

9. **STRUCTURAL — Hedge "no existing research" niche claim** (ST2): Change to "no research we have located" given the incomplete coverage of the field.

---

## Regeneration Guidance

If the operator wants to re-run the Drafter with this review:

**Critical issues to feed back**:
- c003 statistic is wrong: 97.3% is a type-distribution figure (proportion of hard vs. soft refusals *among* censored prompts), not an overall refusal rate. Correct figure is 68.75% of topic categories reach 100% refusal rate.
- c021 three-concept breakdown cannot be verified from abstract alone — limit to confirmed abstract claim.
- c029 definitional quote is Drafter-constructed — remove quotes, use descriptive summary only.

**Sources to prioritize deep-reading**:
- c002 (de Man 2025): add to Section 一 background on framing-sensitive Chinese LLM censorship
- c008 (Zhou & Zhang 2024): add to Section 一 as qs=5 Nature Scientific Reports precedent for language-framing inconsistency
- c009 (Yadav et al. 2025): add to Section 二/三 to sharpen safety/censorship distinction
- c021 (Gillibrand & Draper): operator must obtain full text before finalizing Section 二 informational sovereignty claims

**Brief questions that need rephrasing**: None — the brief is well-formed. The structural issues arise from execution, not brief design.

---

## Overall Verdict: REVISE

The draft is intellectually coherent and well-structured. The literature positioning is accurate in broad strokes and the identified niche is real. However, two statistical misrepresentations (OC1 — c003 97.3% figure), one abstract-overreach (OC3 — c021 three-concept breakdown), and one fabricated quote (OC4 — c029 definition) must be corrected before this memo can safely inform an advocacy piece. These are not interpretation disagreements — they are factual errors against the sources the Drafter cited. The remaining issues (OC2, OC5, ST1-ST6) are hedging and framing improvements that would strengthen credibility without altering the core argument.

The core argument — that identity-triggered differential access is a novel and underresearched phenomenon, grounded in documented censorship infrastructure and supported by adjacent mechanism precedents — holds up under adversarial review. The contribution claim in Section 三 is accurately scoped and not overclaimed.
