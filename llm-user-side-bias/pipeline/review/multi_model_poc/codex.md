# Review of llm-user-side-bias insight_v2

**Reviewed on**: 2026-05-18  
**Draft**: `projects/llm-user-side-bias/pipeline/draft/insight_v2.md`  
**Sources consulted**: accepted.jsonl (32 records), extracts/ (21 deep-reads), brief.md

## Verdict

One-line status per finding:
- Finding 1: ⚠️ needs tightening
- Finding 2: ⚠️ needs tightening
- Finding 3: ❌ has gap
- Finding 4: ⚠️ needs tightening
- Finding 5: ⚠️ needs tightening
- Finding 6: ❌ has gap

Overall: 🟡 needs revision pass

## Per-finding review

### Finding 1 — 身份觸發機制是真實且可重製的（機制先例）
**Status**: ⚠️ needs tightening

**Citations audit** (L1):
- Draft claim:「身份觸發機制是真實且可重製的（機制先例）｜高 — 多篇 qs=5 同行評審研究支持 [c012, c013]」。`c012` 強；`c013` 支持 persona 改變政治輸出，但不是 guardrail/refusal access-control。高信心可保留，但需明確寫成「declared persona / identity prompts can modulate behavior」，不要寫成完整「access-control trigger」已被多篇複現。
- Draft claim:「支撐這一機制的學術先例存在，但從未延伸至地緣政治或國族身份場景 [c012, c013, c011]」過寬。`c011` 已測 nationality，但場景是 career advice / interaction quality，不是 geopolitics；應改成「未延伸至中國源模型 × 國族身份 × 地緣政治敏感主題」。

**Claim-vs-source fidelity** (L2):
- Draft claim:「Li 等人：同一請求、宣告不同政治身份，ChatGPT 的拒答率出現 44% 對 76% 的系統性落差 [c012]」忠實。extract:「44% for conservative personas and 76% for liberal personas」。
- Draft claim:「Bernardelle 等人確立合成人格是改變 LLM 政治輸出的有效向量 [c013]」大致忠實，但來源是 political orientation/output，不是拒答或存取。extract:「Persona assignment is an effective vector」。
- Draft claim:「Amiri-Margavi...身份（包含國籍）仍會造成系統性互動品質差異 [c011]」忠實。extract:「systematic...disparities in interaction quality」。

**Counter-evidence check** (L3):
- `c011` 是重要反例/界線：它顯示「zero refusal rates」但仍有 quality disparities。draft 有承認，但在信心表把「身份觸發機制」說成「存取控制」時，應避免把 quality disparity 與 refusal/access gate 混成同一機制。
- accepted set 未顯示已有研究直接做「國族身份 × 中國源模型 × 敏感政治主題」；novelty claim 在限定語下成立。

**Overlooked sources** (L4):
- `c006` accepted Q1：ChatGPT/Gemini/Bing cross-lingual guardrail on authoritarian Russia，與 pilot 的 ChatGPT/Gemini + political guardrail design 是明顯 dialogue partner；draft 在缺口一提三篇 anchor，卻未把 accepted 的 `c006` 納入或列為需取得全文。
- `c019` accepted Q3：ChatGPT political bias baseline，低邊際價值但可補一句「身份觸發不是從零開始，而是政治 bias literature 的延伸」。

**Confidence calibration** (L5):
- Warranted: Medium-high, not High if phrased as「access-control trigger」。High only applies to narrower claim:「declared identity/persona can shift model behavior」。

**Suggested revision**:
- 將信心表第一列改為：「宣告身份/persona 會調節 LLM 政治輸出與部分 guardrail 行為｜中高；拒答型 access-control 機制主要由 c012 支撐，c013/c011 為鄰近證據。」

**Concept-fidelity** (L8):
- `themes.jsonl` has `evidence_scope_distribution`; draft has no `**{...}**` scope tags. This is a `missing_scope_tag` for t01 paragraphs.

### Finding 2 — 先導研究的 DeepSeek 二二八發現屬新型態
**Status**: ⚠️ needs tightening

**Citations audit** (L1):
- Draft claim:「先導研究...填入了這個空白...這已不是主題層審查，而是使用者身份驅動的差別存取 [pilot]」depends entirely on `[pilot]`, which is not in accepted.jsonl and has no extract provided here. It is allowed as project-internal evidence from brief.md, but reviewer cannot verify raw cells, prompts, or outputs.
- Draft claim:「先導研究正是首個這樣的實驗 [pilot]」is too absolute unless bounded to「在本次 accepted set / 檢索所及」。

**Claim-vs-source fidelity** (L2):
- Pilot fidelity cannot be audited from extracts. brief.md supports the core pattern: DeepSeek refuses Q1 when Taiwanese/Chinese identity is declared, answers with no identity, and shows 合規/合宜 vocabulary split.
- Draft claim:「而這一機制對地理位置（台灣 IP vs. 香港 IP）不敏感」is brief-supported for DeepSeek, but the same brief also reports Gemini IP-driven vocabulary difference. Draft should state DeepSeek-specific IP insensitivity, not general identity-trigger mechanism.

**Counter-evidence check** (L3):
- `c005` and `c003` show Chinese-origin censorship can be language-consistent, but they do not prove identity-signal causation. Draft line:「Ko...實際上支持了『審查是身份/身份信號驅動而非語言本身驅動』的解釋」overreaches: Ko supports non-language-selective censorship for Chinese models, not identity-triggered censorship.
- `c008` shows language as trigger in GPT; this is adjacent but also a counter-pressure against collapsing language and identity.

**Overlooked sources** (L4):
- `c006` is the main omitted accepted source for cross-lingual guardrail behavior in ChatGPT/Gemini/Bing and should be listed in gaps or route map.
- `c020` is cited later, but not in the pilot novelty paragraph where 合規 vs. 合宜 is interpreted as style signal.

**Confidence calibration** (L5):
- Draft says「中高」for this finding. Warranted: Medium. The novelty claim rests on negative search plus small unpublished pilot, not on replicated evidence.

**Suggested revision**:
- Rewrite as「在本次文獻集與先導資料中，DeepSeek 二二八結果呈現一個待驗證的新型態；目前應定位為 hypothesis-generating novelty，而非已確立的新機制。」

**Concept-fidelity** (L8):
- Missing scope tags for t01/t02 paragraphs. Claim scope should be `{conceptual: identity_trigger_gap, methodological: pilot/hypothesis-generating}` and should not imply broader geographic generality beyond CN/TW/HK pilot cells.

### Finding 3 — 中國源模型系統性審查的背景前提
**Status**: ❌ has gap

**Citations audit** (L1):
- Citation density is strong: `[c001, c003, c004, c005, c007, c015]` includes multiple qs≥4/5 sources.
- Problem is not source count but causal language. Draft claim:「這是刻意設計的存取管制政策，而非訓練資料的無意副產品」is stronger than several sources allow. `c001` explicitly says it「does not establish a causal linkage」; `c004` leaves training corpus / fine-tuning / filtering unresolved.

**Claim-vs-source fidelity** (L2):
- Draft claim:「68.75% 達到百分之百拒答率...英語 100%...中文 99.57% [c003]」忠實。
- Draft claim:「de Man...顯示審查是後生成的輸出層過濾，而非前生成封鎖 [c002]」overstates. extract says「suggesting post-generation filtering」; draft turns suggestion into conclusion.
- Draft claim:「Qiu...直接確立『模型知道答案，但刻意不輸出』[c004]」mostly supported on suppression, but「刻意」should be softened to「輸出層被抑制 / withheld」。

**Counter-evidence check** (L3):
- `c001` warns observational design cannot prove state causality. This is directly relevant counter-evidence to「刻意設計的政策」。
- `c005` has method limitations already listed by draft, but draft still uses Ko in high-confidence background. That is acceptable only if Pan/Xu and R1dacted remain primary.

**Overlooked sources** (L4):
- `c017` accepted Q3: ChineseSafe documents Chinese-specific safety categories; useful for distinguishing safety taxonomy from political censorship.
- `c006` accepted Q1: relevant to guardrail-related political bias and false information in ChatGPT/Gemini/Bing; would help situate non-China models.

**Confidence calibration** (L5):
- High is warranted for「中國源模型有系統性親中/審查模式」。
- High is not warranted for「刻意設計的存取管制政策」unless rephrased as an inference from convergent evidence, not a proven causal fact.

**Suggested revision**:
- Replace「刻意設計的存取管制政策」with「與中國監管與政策環境高度一致的模型層存取抑制；現有研究尚未完全分離訓練資料、微調與後生成過濾的因果權重。」

**Concept-fidelity** (L8):
- Missing scope tags for t02/t05. Several claims should be scoped to `{geographic: CN/TW, methodological: empirical-quantitative}` rather than global LLMs.

### Finding 4 — 「資訊主權」作為理論框架
**Status**: ❌ has gap

**Citations audit** (L1):
- Draft relies on `[c021, c023, c041, c037, c009]`. Citation density is enough, but `c021` is access-blocked and only abstract-level; draft correctly caveats this.
- Draft claim:「DeepSeek 對二二八事件的身份觸發拒答...是一個三支柱體系的末端表達」is cited `[pilot, c023]` but is an interpretive bridge, not directly sourced. The parenthetical caveat helps, but the sentence still reads stronger than the evidence.

**Claim-vs-source fidelity** (L2):
- `c023` supports the three-pillar China information sovereignty frame. extract:「legislative, technological, and cultural measures」。
- `c041` supports targeted discourse infrastructure. extract:「four State Key Laboratories」 and「targeted information operations」。
- `c037` supports PEFT ideological alignment, but not identity-triggered differential access. Draft caveat is good; keep it.
- `c009` supports safety-vs-censorship distinction. It does not by itself prove DeepSeek’s identity-triggered refusal is state-policy-driven.

**Counter-evidence check** (L3):
- Accepted set contains several sovereignty sources not deep-read or not used (`c022`, `c024`, `c025`, `c026`). Because `c021` is blocked, ignoring these weakens the theoretical frame.
- `c001` causal caveat again matters: policy alignment is plausible, but direct state-policy implementation cannot be claimed as proven.

**Overlooked sources** (L4):
- `c025`: technological sovereignty as capability rather than autarky; directly helps the “active capability” framing.
- `c022`: information sovereignty threats in LLM deployment; likely bridges abstract sovereignty to user-level informational autonomy.
- `c024`: comparative digital sovereignty models; useful for avoiding China-only exceptionalism.
- `c026`: authoritarian vs democratic governance model; relevant to regime-type framing.

**Confidence calibration** (L5):
- Draft says Medium; that is fair for the framework overall.
- Any subclaim mapping 合規=legislative, identity detection=technological, 合宜=cultural should be Low/interpretive unless pilot raw and c023 details are further developed.

**Suggested revision**:
- Keep informational sovereignty as a frame, but label the three-pillar mapping as「分析假說」and add `c025` or `c022` as fallback theoretical support while `c021` remains blocked.

**Concept-fidelity** (L8):
- Missing scope tags for t03. Claims should distinguish `{geographic: CN}` from `{geographic: global}`; the Russia/Pravda analogy is global/comparative, not evidence for China’s LLM mechanism.

### Finding 5 — 「知識不平等」作為規範框架
**Status**: ⚠️ needs tightening

**Citations audit** (L1):
- Draft uses `[c029, c033, c020, pilot]`. Citation density is thin but acceptable for a normative framework because `c029` is qs=5 and `c033` is directly on AI epistemic injustice.
- Draft claim:「這是一種系統性設計的知識剝奪」is stronger than `c029/c033`; they support the category of harm, not the design intent in this case.

**Claim-vs-source fidelity** (L2):
- `c029` supports four dimensions including access injustice. extract:「access injustice」 and「multilingual contexts」。
- `c033` supports generative hermeneutical erasure. extract:「automation of epistemicide」。
- Draft correctly notes that applying c033 to national-identity-triggered historical access is the author’s extension, not the paper’s direct claim.
- `c020` supports content/style distinction, but「合規 vs 合宜 是知識不平等在語言表面留下的痕跡」is interpretive. Source supports style analysis, not epistemic injustice.

**Counter-evidence check** (L3):
- The draft already lists a major gap: no quantitative user-impact evidence for Taiwanese users. Good.
- `c011` suggests harm can occur even when access is equal; this could enrich the framework by separating denial, quality disparity, and style targeting.

**Overlooked sources** (L4):
- `c030`, `c031`, `c032` are accepted Q2 sources on conversational AI / language bias / epistemic oppression but were skipped due access issues. Draft should at least mention them as blocked adjacent sources if the epistemic injustice frame remains central.
- `c044` human-rights framing is accepted and relevant to the advocacy piece’s “rights” language.

**Confidence calibration** (L5):
- Medium is warranted for「知識不平等作為規範框架」。
- Low-to-medium for「系統性設計的知識剝奪」unless rephrased as normative interpretation of the pilot.

**Suggested revision**:
- Replace「這是一種系統性設計的知識剝奪」with「可被詮釋為 access injustice；是否構成系統性設計，需依擴大實驗與政策/模型證據確認。」

**Concept-fidelity** (L8):
- Missing scope tags for t04. Claim scope should stay `{conceptual: algorithmic_discrimination, methodological: commentary}`; do not present it as empirical measurement of harm.

### Finding 6 — 「AI 作為地緣政治工具」的倡議主張
**Status**: ❌ has gap

**Citations audit** (L1):
- Draft confidence table says High —「Freedom House + 多篇實證 [c001, c004, c007, c041] 支撐，但 c039 全文不可及」。High is not calibrated because `c039` is access-blocked and `c041/c035` are policy/grey-literature, while `c001/c004/c007` show model bias/suppression rather than full infrastructure claims.
- Draft claim:「任何使用中國源 LLM 的人，都可能成為這一差別存取體系的對象 [c001, c004]」is too broad. `c001/c004` support transnational propagation risk and DeepSeek suppression, not “anyone” as object of identity-based differential access.

**Claim-vs-source fidelity** (L2):
- `c035` supports Russia training contamination, not Chinese alignment/fine-tuning. Draft correctly says「類似目標、不同機制」; good.
- `c039` only has abstract/index-level access. Draft correctly caveats, but should not use it to sustain High confidence.
- `c001` supports transnational propagation risk. extract:「extend beyond China's borders」。This is weaker than universal exposure.

**Counter-evidence check** (L3):
- `c001` says language effects are less pronounced than origin effects, but still present; advocacy route should not erase language-side mechanisms.
- `c007` shows US-origin models pro-US and China-origin pro-China. That supports geopolitical bias broadly, but also complicates a China-only narrative: the advocacy should frame China as the case under study, not the only geopolitical actor.

**Overlooked sources** (L4):
- `c017`: Chinese-specific safety categories could strengthen “Chinese regulatory censorship layer”.
- `c026`: authoritarian vs democratic governance would support regime-type contrast.
- `c044`: human-rights obligations could anchor the public advocacy claim more directly than epistemic theory alone.

**Confidence calibration** (L5):
- Warranted: Medium-high for “AI/LLMs can function as geopolitical information infrastructure.”
- Warranted: Medium or Low for “identity-triggered differential access is a scalable geopolitical tool” until pilot is replicated and c039 is retrieved.

**Suggested revision**:
- Lower confidence to Medium-high and split the claim: established geopolitical model alignment vs. not-yet-established identity-triggered differential access at scale.

**Concept-fidelity** (L8):
- Missing scope tags for t05. The draft’s advocacy claim blends `{geographic: CN}`, `{global}`, and `{TW}` without marking the evidence boundary.

## Structural issues (not tied to a single finding)

- Missing brief-question coverage (L6): Q1, Q2, Q3 are all addressed. No structural omission in brief coverage.
- Missed gaps in "What we don't know" (L7): Draft lists major gaps well, but misses `c006` as an accepted, directly adjacent cross-lingual guardrail dialogue partner. It also does not explicitly flag that no raw pilot transcript/extract was available for reviewer fidelity checks.
- Access_blocked sources' impact not acknowledged: c021 and c039 are acknowledged. However, accepted-but-blocked adjacent Q2 sources (`c022`, `c024`, `c030`, `c031`, `c032`, `c044`) are not acknowledged, even though they affect the sovereignty / epistemic injustice / rights framing.
- L8 concept-fidelity: `themes.jsonl` contains `evidence_scope_distribution`; draft contains no Dr2 `**{<scope>}**` tags. This is a global `missing_scope_tag` issue across all theme-linked paragraphs. It is not a semantic contradiction, but it violates the Dr2 contract and makes scope overreach harder to audit.
- Source pool integrity: all cited `cNNN` IDs checked against accepted/rejected sets; no cited `cNNN` appears in rejected.jsonl. `[pilot]` and `[anchor:*]` are outside accepted.jsonl and are explicitly marked as such by the draft.

## Summary recommendations

1. Downgrade or narrow causal/design-intent language: especially「刻意設計的存取管制政策」、「國家政策導向」、「系統性設計的知識剝奪」。
2. Add scope tags or otherwise satisfy Dr2 L8 expectations because themes.jsonl carries evidence_scope_distribution.
3. Add `c006` to the dialogue-partner/gap discussion; it is accepted and directly adjacent to cross-lingual guardrail behavior in ChatGPT/Gemini/Bing.
4. Lower confidence on the pilot novelty and advocacy-scale claims until raw pilot outputs and blocked c039/c021 evidence are available.
5. Separate three claims throughout: model-origin geopolitical bias, language-triggered framing, and declared-identity-triggered differential access.

## Regeneration guidance (if needed)

If the operator wants to re-run the Drafter with this review:
- Critical issues to feed back: causal overreach; missing L8 scope tags; unsupported “first” language; over-merging language trigger with identity trigger.
- Sources to prioritise deep-reading: `c006`, `c021`, `c039`, `c022`, `c025`, `c030`/`c031`/`c032`, plus raw pilot transcripts if available.
- Brief questions that need rephrasing: none. The brief is clear; the weakness is mostly confidence calibration and scope discipline.