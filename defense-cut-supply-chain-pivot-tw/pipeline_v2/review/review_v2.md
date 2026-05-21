# Review of defense-cut-supply-chain-pivot-tw insight_v2 (multi-model meta-merge)

**Reviewed on**: 2026-05-21
**Draft**: projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v2.md
**Review mode**: multi_model — three independent reviewers + meta-merge (this document)
**Reviewed by**: Claude (r_claude.md), Codex (r_codex.md), Gemini (r_gemini.md, advisory)
**Review pass**: #2 of insight_v2.md — **v2+ review pass WITH a prior baseline** (round-1 consolidated review at `pipeline_v2/review/review.md` reviewed insight_v1.md, verdict 🟡 needs revision pass). Per spec §8 "Claude verdict pass-aware", this is the **first time the v2+ weighting path is exercised**: Claude general-verdict weight = **0.8** (not 1.0). See "Spec / tooling calibration observations" for how this affected the merge.
**Sources consulted by reviewers**: accepted.jsonl (79 records), extracts/ (19 deep-reads, incl. 10 MOPS primary financials), brief.md, brief_expanded.yaml, extracts/INDEX.md, rejected.jsonl (1 record: c023), prior `review/review.md`

## Verdict

Per-finding meta-verdict (status ↔ score: ✅=0, ⚠️=1, ❌=2, 🚨=3):

- **Finding 1** (4700 億 = 本土軍工 + 無人載具 + 非紅供應鏈財源): **✅ solid** — round-1 ⚠️ resolved
- **Finding 2** (工具機聚落西進是一手財報坐實的結構性存量): **✅ solid** — unchanged from round-1, holds
- **Finding 3** (「砍案 → 西進加速」是壓力與條件，非事實): **✅ solid** — round-1 ⚠️ resolved
- **Finding 4** (雙鏈差別待遇): **✅ solid** — round-1 ⚠️ resolved
- **Finding 5** (西進三層風險機制): **⚠️ needs tightening** — one residual sentence-level minor edit (c043「雙向鎖出」phrasing)
- Counter-framing engagement (6 frameworks) — structural: **✅ solid**
- What we don't know — structural: **✅ solid**

**Overall meta-verdict: 🟢 publishable with minor edits.**

**Round-1 → round-2 trajectory: 🟡 needs revision pass → 🟢 publishable with minor edits.** The 6 patches from the round-1 review all landed; **5 of the 6 prior ⚠️ items (F1, F3, F4, and the structural Q6/Wassenaar gaps) resolved cleanly to ✅**, and the patch-level revision approach worked as intended — no re-Drafter was needed and none is needed now. The single residual is F5's ⚠️, a one-sentence phrasing-precision issue introduced as a side-effect of patch #1 (the c043 Taiwan-side control source). It is a minor edit, not a revision pass.

This draft has evidence discipline clearly above pipeline average. All three reviewers agree there is **zero 🚨 and zero ❌**: no concept-fidelity violation, no rejected-cid hard error (rejected pool is only c023, which the draft correctly avoided — verified by all three), no extract-level fabrication. The verdict resolves to 🟢 via spec §8 **R4** (≥2 models 🟢 + Codex carries no ❌/🚨 + integrity clean). It is **not** R3 🟡 (the F5 residual is a sentence-level minor edit with the source already cap'd 【爭議中】 — it does not constitute a revision-pass-level fidelity/calibration failure). It is firmly **not** 🔴 (no R1 trigger).

## Source-pool Integrity

`integrity_check.py` output (`integrity_report.json`): **all clean.** `any_hard_error: false`, `any_count_mismatch: false`, `actual_accepted_n: 79`, `actual_extract_n: 19`. All three reviews `usable: true`, zero `errors`, zero `hallucinated_cids`, empty `lens_multipliers` for all three. No halt condition; no per-review weight penalty applied; the full meta-merge proceeded normally.

**Calibration note — the round-1 false positive did NOT recur.** Round 1's integrity report flagged `any_hard_error: true` / Gemini `usable: false` (`rejected_cid_cited: c023`), which the round-1 meta-merge verified as a false positive: `integrity_check.py`'s bracket-detection heuristic mis-fired because Gemini wrote the cid in bracket form `[c023]` inside a benign L1-audit "draft correctly avoided this" note. **This round, the false positive did not recur** — `integrity_report.json` is clean for all three reviewers. The reviewers wrote the rejected cid in plain-text `c023` form per an updated prompt reminder (Gemini's `bracket_citation_count` this round is 12, but none of them collided with the rejected cid in a way that tripped the heuristic). The underlying `integrity_check.py` bracket-heuristic bug flagged in round 1 — that the `rejected_cid_cited` check matches any rejected-cid token without audit-context awareness — **remains an open tooling item**: the prompt reminder is a workaround, not a fix. The check is one prompt-drift away from re-tripping. The round-1 recommendation stands: exclude audit-context mentions, or demote the check from automatic hard-error to review-required flag.

## Model Consensus / Conflict

**Consensus (all three agree):**
- **Overall verdict 🟢** — all three reviewers independently rate the draft publishable (Claude 🟢 "publishable with minor edits", Codex 🟢 "publishable with minor edits", Gemini 🟢 "publishable"). This is the clearest possible R4 configuration: there is no overall-verdict disagreement to resolve.
- **Findings 1, 2, 3 are ✅ solid** — unanimous. F2 unchanged from round-1 (already unanimous ✅); F1 and F3 round-1 ⚠️ resolved to unanimous ✅ after patches #2 and #3.
- **Zero 🚨 / zero ❌** — no reviewer raised a hard error, concept-fidelity violation, or extract-level fabrication.
- **All 6 round-1 patches landed.** All three reviewers independently verified the 6 patches were actually applied, and that the 6 new cids (c042/c043/c015/c030/c032/c033) were all placed at Dr3 SECONDARY 【爭議中】 tier with the "依摘要層 sourcing" annotation — none mis-promoted to 【強證據】. Claude's per-patch verification table and Codex's patch-verification line both confirm this; Gemini confirms per-finding.
- **No rejected-cid misuse** — all three confirm the draft avoided c023.
- **Time-ordering honesty (Finding 3)** — all three praise that the draft holds the line "2026-Q1 financials precede the 2026-05-08 cut → financials cannot show post-cut behaviour", directly satisfying the brief FAILURE MODE「把『軍購砍 → 西進』當必然結果」.
- **Q5 not smuggled** — all three confirm Finding 5 keeps "mechanism exists" distinct from "industry case has occurred"; the draft uses 亞德客 to *bound* the risk (深度西進卻未被鎖出，因做氣動元件、非國防相關) rather than overclaim it.
- **L8 skipped** — all three note Synthesizer was skipped per M4, there is no `synthesize/themes.jsonl` and no `evidence_scope_distribution`, so the conceptual-fidelity lens does not fire. The draft correctly does not use Dr2 `**{scope}**` paragraph tags.

**Conflict (where the models diverge):**
- **Finding 4**: Claude ✅ / Codex ⚠️ / Gemini ✅. The sole dissent is Codex, on two points: (a) the B-chain「電池與稀土仍依賴中國」claim rests only on the single summary-tier source c059; (b) the A→B「母機」cross-chain inference's first sentence could be tightened. **Resolved to ✅** — see Finding 4 below. The reason: the draft *already explicitly caveats* both items (c059 is tagged 【爭議中】+「依摘要層 sourcing」; the A→B inference is marked 【專家意見】 and the draft itself writes「『國防航太工業零件』不等同於『無人機零組件』… 這一步是結構性外推」). Per spec §9.3, a Codex hedge/caveat catch that the draft already explicitly caveats and that neither Claude nor Gemini sees is downgraded to **minor priority**. §9.3 fires here; Codex's catches are preserved below as minor-priority notes, not as a status-moving ⚠️.
- **Finding 5**: Claude ⚠️ / Codex ⚠️ / Gemini ✅. **Senior consensus ⚠️** — both Claude and Codex independently land on the same catch: the draft's use of c043 (the Taiwan strategic-goods control dataset) is slightly over-stretched. Gemini's ✅ is advisory and per spec §8 R5/R6 cannot offset two senior ⚠️. **Resolved to ⚠️** — see Finding 5.

**How the disagreement was used, not flattened:** This round there is no overall-verdict conflict to resolve — all three converge on 🟢. The only live per-finding disagreements are F4 (one Codex ⚠️ vs two ✅) and F5 (two senior ⚠️ vs one Gemini ✅). F4 was resolved *down* to ✅ because §9.3 specifically governs the Codex-only-flag-on-already-caveated-content case — but Codex's observations are still carried into the regeneration guidance as optional improvements, not silently dropped. F5 was resolved *to* ⚠️ because two senior reviewers independently converged on the *same* catch with extract-level reasoning — that convergence is signal, not noise, and Gemini's advisory ✅ cannot override it. The meta-verdict 🟢 carries Codex's "F4/F5 still have minor edges" into the recommendations while carrying the unanimous "publishable" judgment into the overall verdict.

## Round-1 → Round-2 patch trajectory

The round-1 consolidated review issued 6 patch recommendations and an explicit "Do NOT do". This round's three reviewers independently verified each. Consolidated result:

| Round-1 patch | Round-1 target | Round-2 status | New problem introduced? |
|---|---|---|---|
| #1 — Add c042 + c043 (F5 法源層, highest priority) | F5 ⚠️ | **Landed.** F5 法源層補齊為「美 BIS/EAR + 台灣戰略貨品管制 + 中國反制法制」三端; c042 correctly *moved out* of the 【強證據】 paragraph to avoid a Dr3 strong-tier slip. | **Yes — minor.** The c043 Taiwan-side framing introduced one sentence-level phrasing-precision issue (the「雙向鎖出」symmetric rhetoric). This is the sole residual ⚠️ — see Finding 5. |
| #2 — Rewrite 4700/3000/3350 additive-reading ambiguity | F1 ⚠️ | **Landed, clean.** Draft now states 4700 億 explicitly as the 原版1.25兆 vs 砍後7800億 總落差, not an additive 3000+3350 sum. Resolves F1 to ✅. | No. |
| #3 — Weaken「確定無法補回」 | F3 ⚠️ | **Landed, clean.** Condition (1) now reads「方向上偏成立、量級未知」, consistent with c026's evidence boundary and the 中 confidence. Resolves F3 to ✅. | No. |
| #4 — Soften B-chain title/head + add 1–2 qs4 B-chain sources | F4 ⚠️ | **Landed, clean.** Title changed to「B 鏈仍有中國零組件依賴與上游母機外移風險」; body explicitly states「不主張 B 鏈已發生可觀察的西進」; c030/c032/c033 added at 【爭議中】. Resolves F4 to ✅. | No — new cids correctly kept out of 【強證據】. |
| #5 — Add c015 decoupling-cost counter-evidence + Wassenaar gap line | F5 ⚠️ + structural | **Landed, clean.** c015 added as a new 【爭議中】 counter-evidence paragraph; Wassenaar/ECCN gap added to "What we don't know". | No. |
| #6 — One-line Q6 out-of-scope scope statement | structural | **Landed, clean.** Q6 scope statement added to Context + a full "What we don't know" bullet. The round-1 silent-omission concern is resolved. | No. |
| "Do NOT do" — do not promote c029 to 【強證據】 | — | **Honoured.** c029 (波蘭 6 成出口) kept at 【爭議中】. | — |

**Calibration-relevant evidence**: the patch-level revision worked. 5 of 6 prior ⚠️ items resolved cleanly to ✅; the 6th (patch #1) resolved its target ⚠️ (法源層不再只談美中兩端) but introduced one new sentence-level phrasing issue — a contained, well-understood side-effect, not a regression. No re-Drafter was needed and none is needed now. This is direct evidence that the round-1 meta-verdict (🟡 patch-level, NOT re-Drafter) was correctly calibrated.

## Per-finding review

### Finding 1 — 被砍的 4700 億，砍掉的是「本土軍工 + 無人載具」，也砍掉了非紅供應鏈承諾的財源

**Meta-status**: ✅ solid (round-1 ⚠️ resolved)

**Citations / fidelity (L1–L2)**:
- [Consensus] Core budget figures (約 9000 億對外軍購 / 3000 億本土軍工 / 砍後 7800 億 / 62.4% / 4700 億落差 / 三大重點含「打造非紅供應鏈」) are word-aligned with c019 (qs=5 deep-read). [Claude L2] audited c019's three extract Passages line-by-line — zero divergence; [Codex L2] independently confirmed Passages 1/3; [Gemini L2] confirmed the arithmetic reconciliation at draft lines 39–44.
- [Consensus — round-1 ⚠️ resolved] Patch #2 landed. Codex's round-1 sole catch (3000 + 3350 reads as additive for a lay reader) is fixed: the draft now explicitly writes that 4700 億 is the 原版1.25兆 vs 砍後7800億 **總落差**, that 3000 億 and 3350 億 are different reporting-tier descriptions of overlapping 本土/無人載具 items, and that they「涵蓋範圍重疊、不能直接相加」. [Codex L2] and [Claude L2] both confirm the additive-misreading risk is removed for the stated general-public audience.
- [Claude L1] No orphan citations; the 4700 億落差 is precisely bound to c019; the「已簽 69.51 億合約是否受影響」point is honestly marked 【爭議中】「中等不確定」.

**Counter-evidence / overlooked sources (L3–L4)**:
- [Consensus] No counter-evidence in the accepted set proves「砍案對產業實質無影響」; the draft's phrasing「accepted 集合內未見任何能證明…的來源」is the precise round-1-recommended form. Correct.
- [Claude L4 + Codex L4] c025 (deep-read, 無人機廠商第一人稱衝擊, 單廠年產約 500 架) remains unused — both reviewers note it would more directly support the「內銷活水被砍」argument than the currently-cited c047/c048. Optional add — not a defect; the draft already builds the 內銷 pipeline with c049 (一手合約數字) + c047/c048.

**Confidence calibration (L5)**:
- [Consensus] Declared 高 — correct. c019 is a qs=5 deep-read meeting the「≥3 sources incl. qs≥4」threshold; the「已簽合約是否受影響」sub-claim is honestly stepped down to 中等不確定.

**Suggested revision**: none required — finding holds. Optionally add c025 (deep-read first-person impact) — not necessary.

### Finding 2 — 工具機聚落西進中國，是早於砍案、已被一手財報坐實的結構性存量

**Meta-status**: ✅ solid — unanimous, unchanged from round-1

**Citations / fidelity (L1–L2)**:
- [Consensus, strongest section of the draft] Each of the five firms (程泰/東台/瀧澤/上銀/亞德客) has a MOPS primary-doc citation for every figure. [Claude L2] audited specific extracts (c074 程泰 附表七「本期匯出/收回」欄全 0; c077 瀧澤機電浙江嘉善「生產三軸以上聯動數控機床」) — zero divergence, and notes round-1's ~15-sub-claim audit against 8 extracts still holds since v2 did not touch this section. [Codex L2] independently confirmed 上銀 (c071/c072), 瀧澤 (c077/c078), 亞德客 (c079) figures with zero divergence. [Gemini L2] confirmed the firm-by-firm audit with zero divergence.
- [Consensus] The draft correctly scopes 亞德客 as 精密機械/自動化元件廠 (not CNC 整機) and explicitly marks it a baseline illustration, not a「軍購砍 → 西進」case — matching the c079 scope caveat.
- [Codex L2] Round-1's「台灣只是上市掛牌地」over-statement was softened in v2 to「台灣主要是上市與部分營運／貿易節點」 — round-1 minor catch resolved.

**Counter-evidence (L3)**:
- [Consensus] The draft proactively cites c071 (上銀 disperses 東歐+東南亞) and c077 (瀧澤 low-tier-in-China / high-tier-in-Taiwan layering) as honest counter-evidence — verified against extracts. Honestly handles「西進是分層的，不是全產能搬遷」.

**Confidence calibration (L5)**:
- [Consensus] Declared 高 — correct. Five firms' westward stock is line-by-line confirmed by MOPS primary financials + independent industry news (c021), far exceeding the「≥3 sources incl. qs≥4」threshold.

**Suggested revision**: none required — finding holds; the draft's most solid section.

### Finding 3 — 「軍購砍 → 西進加速」目前只能說是壓力與條件，不是已發生的事實

**Meta-status**: ✅ solid (round-1 ⚠️ resolved)

**Citations / fidelity (L1–L2)**:
- [Consensus] Time-ordering claims all carry MOPS Q1 citations (c074/c076/c078/c080); the draft correctly frames "cut → shift" as conditional probability. All three reviewers explicitly praise this as the draft's best discipline.
- [Consensus — round-1 ⚠️ resolved] Patch #3 landed. Codex's round-1 sole catch (「確定無法補回」over-reaches c026) is fixed: condition (1) now reads「目前 accepted 集合只能確認國防部表態『不再提二次特別預算』[c026]…故此條件只能說『方向上偏成立、量級未知』」. [Codex L1/L2] confirms this matches c026's evidence boundary; [Claude L2/L5] confirms the「確定」removal restores internal consistency with the 中 confidence; [Gemini L2] confirms the correction at draft line 101.
- [Codex L2] The「2026 Q1 浙江嘉善廠房仍在興建中」claim is correctly written as「extract 記錄顯示」(round-1's recommended hedge, since this detail is reconstructed from extract abstract/附註 rather than a verbatim primary passage) — round-1 catch resolved.
- [Claude L2] The「上銀美國曝險低於 3%」claim is correctly tagged「2024-年報口徑」(round-1's recommended tag, to prevent a reader misreading it as a Q1 number) — round-1 minor catch resolved.

**Counter-evidence (L3)**:
- [Consensus — round-1 Gemini catch resolved] Round-1 Gemini flagged that v1 engaged weakly with the tension between c021's「醞釀登陸投資潮」media framing and c074's「2026 Q1 本期匯出為 0」financial fact. v2 now explicitly writes this tension into the second 【爭議中】 paragraph — [Claude L3] and [Codex L3] both confirm the round-1 ⚠️ is substantively resolved.
- [Consensus] The counter-evidence section honestly retains the other side: c074 (程泰 工具機本業轉盈 → 景氣回穩、不一定急於西進) and c071 (上銀 美國曝險 < 3%).

**Confidence calibration (L5)**:
- [Consensus] Declared 中 — correct, given the prospective nature of the「砍案 → 加速」causal link. With「確定」removed, the text is now internally consistent with the 中 confidence.

**Suggested revision**: none required — finding holds. The time-ordering discipline directly hits the brief FAILURE MODE「把『軍購砍 → 西進』當必然結果」.

### Finding 4 — 雙鏈差別待遇：工具機外銷補不上、無人機整機外銷強勁但 B 鏈仍有中國零組件依賴與上游母機外移風險

**Meta-status**: ✅ solid (round-1 ⚠️ resolved; Claude ✅ + Gemini ✅; Codex's lone ⚠️ downgraded per §9.3 — see below)

**Citations / fidelity (L1–L2)**:
- [Consensus] A-chain statistics (c062 TAMI, c063 台中市府, both qs=5 deep-read) word-aligned and verified — 總出口年減 7.7%、對中佔比 32.2%→26.7%、輸美實質稅率 24.7%、毛利率 < 20%、台中減班休息 49 家次/1,357 人. B-chain c018 (qs=4 deep-read) figures (產值 129 億、整機外銷 21 倍、29.5 億、36 國) word-aligned.
- [Consensus — round-1 ⚠️ resolved] Patch #4 landed. The round-1 senior-consensus catch (the B-chain title/語氣 could let a reader infer an *observable* B-chain westward shift) is fixed: the title is now「B 鏈仍有中國零組件依賴與上游母機外移風險」and the body explicitly opens「accepted 集合**沒有**『某無人機廠商西進中國』的一手案例，本稿不主張 B 鏈已發生可觀察的西進」. [Claude L2] and [Codex L1] both confirm title and body are now consistent.
- [Claude L2] The「車床類年減 18.3%」sub-claim is not verbatim in the c062 extract but is confirmed in INDEX.md; the draft honestly annotates「依 INDEX 確認此一車床類數字載於 TAMI 同份產業現況報告」 — an acceptable extract-unverifiable-sub-claim disclosure.
- [Codex L2] The cross-chain「工具機是製造無人機相關零組件的母機」inference: c077 directly supports only「CNC 車床 用於『國防航太工業零件加工』」. The draft marks the inference 【專家意見】 and itself writes「『國防航太工業零件』不等同於『無人機零組件』… 這一步是結構性外推」 — [Codex L2] confirms this is **not a fidelity violation** and recommends, as a stylistic preference, that the first sentence also be split (國防/航太 first, 無人機 in the next sentence as the extrapolation). **§9.3 downgrade applies** — see below.

**§9.3 Codex-bias resolution (the F4 ✅ vs ⚠️ split)**:
Codex is the sole F4 dissent, on two points: (a) the B-chain「電池與稀土仍依賴中國」rests only on the single summary-tier source c059; (b) the A→B「母機」first-sentence phrasing. **Neither moves the status to ⚠️**, because per spec §9.3 a Codex hedge/caveat catch is downgraded to minor priority when the draft *already explicitly caveats the item* and neither Claude nor Gemini sees it:
- (a) c059 is already tagged 【爭議中】+「依摘要層 sourcing，未經 deep-read 一手驗證」 in the draft body. The draft does not present「電池稀土依賴中國」as an established 【強證據】 fact — it is explicitly summary-tier. Codex's catch is real but already pre-caveated → minor priority.
- (b) The A→B inference is already marked 【專家意見】 and the draft already explicitly disclaims國防航太 ≠ 無人機零組件. Codex's request is a stylistic split of a sentence whose fidelity Codex itself confirms is sound → minor priority.
Claude rates F4 ✅ and Gemini rates F4 ✅. With both already-caveated Codex catches downgraded per §9.3, **F4 meta-status is ✅**. Codex's two points are preserved in the regeneration guidance as optional polish, not dropped.

**Counter-evidence / overlooked sources (L3–L4)**:
- [Consensus] B-chain export evidence depth was the round-1 senior-consensus gap; v2 added c030/c032/c033 (three qs=4 B-chain export sources at 【爭議中】), and the draft honestly notes the individual growth multiples (749%/21 倍/10 倍) diverge by statistical basis and must be read for direction-consistency, not taken singly. The A/B evidence-depth gap is narrowed and the residual is honestly disclosed.
- [Claude L4 + Codex L4] c057/c058 (DSET 台歐/對歐無人機合作) remain unused same-direction qs4 sources — optional, the B-chain export cross-corroboration is now sufficient.

**Confidence calibration (L5)**:
- [Consensus] Declared 中 — correct. The A/B contrast is well-sourced (high); the cross-chain「工具機西進掏空無人機長期承諾」extrapolation has no single direct source, correctly pulling the overall to 中.

**Suggested revision**: none required — finding holds. Optional polish (Codex): split the A→B「母機」first sentence; the「電池稀土依賴中國」line already carries its 摘要層 caveat — no change needed unless a second source surfaces.

### Finding 5 — 西進的風險機制：中國長臂管轄、美國 BIS 鎖出、技術擴散三層

**Meta-status**: ⚠️ needs tightening — senior consensus (Claude ⚠️ + Codex ⚠️; Gemini ✅ advisory cannot offset two senior ⚠️, per §8 R5/R6). **Minor edit, not a revision pass.**

**Citations / fidelity (L1–L2)**:
- [Consensus] The BIS/Entity List mechanism is strongly sourced: c041 (qs=5 deep-read, Federal Register primary text — Inspur Taiwan 新北市, all-items-subject-to-EAR, policy-of-denial) and c040 (qs=5, EAR framework) are word-aligned and verified by all three. [Claude L2] confirmed c041 Passages 1/2/3 verbatim.
- [Consensus — round-1 ⚠️ resolved] Patches #1 and #5 landed. c042 (eCFR Part 744), c043 (台灣戰略貨品名單) and c015 (Christensen decoupling-cost) were all added at Dr3 SECONDARY 【爭議中】 tier with the「依摘要層 sourcing」annotation; c042 was correctly *moved out* of the original 【強證據】 F5-P1 paragraph to avoid a Dr3 strong-tier slip. The round-1「五軸正是典型雙用途品項」over-reach is fixed — the draft now writes「依 EAR 雙用途品項框架推論…此處為框架性推論而非條文直引」 ([Codex L2] and [Claude L2] both confirm).
- [Consensus] The draft correctly limits 瀧澤 c077 (中國公司法修正 → 資本調整) as a 公司法 / non-sanctions matter, and 上銀 c071 (專利維權勝訴) as a technology-diffusion side-fact, NOT 長臂管轄 binding. Fidelity-model behaviour.

**The residual ⚠️ — senior-consensus catch on c043「雙向鎖出」phrasing**:
Both Claude and Codex independently land on the same point, with extract-level reasoning:
- [Claude L2 — the catch in full] F5's second 【爭議中】 paragraph writes:「換言之，『非紅供應鏈鎖出』這個議題對台灣廠商是**雙向**的：一方面台灣廠商可能因深度西進而觸及美方 EAR／Entity List 風險，另一方面台灣也有自己的戰略貨品管制制度需要遵循。」 c043's accepted snippet / INDEX line describes it as a Taiwan-government open dataset for *exporters to screen their trading partners against export-control entity lists* — i.e. Taiwan acting as a *control-enforcement authority*. The draft's literal claim「台灣也有自己的戰略貨品管制制度需要遵循」is broadly correct (exporters do have a compliance duty), but placed inside the「『非紅供應鏈鎖出』對台灣廠商是雙向的」sentence, the symmetric「雙向鎖出」rhetoric invites the reader to infer that the Taiwan-side control is *itself a lock-out risk for Taiwan defence-chain firms* — symmetric with the US Entity List. c043's evidence supports only「台灣有自己的出口管制清單制度」; it does **not** support「台灣端管制構成台灣國防供應鏈廠商的西進鎖出風險」.
- [Codex L2 — same catch, independently] c043's usage is「稍微偏滿」: the accepted snippet says c043 is a government dataset for screening trading partners; the draft writes it up as「台灣自身亦有戰略性高科技貨品出口管制名單／制度」. Codex's framing: if the draft wants to claim「法源層次補齊」, it should say「名單／資料集層」rather than「完整法源」.
- **This is a phrasing-precision issue, not a fidelity violation.** The paragraph is correctly cap'd 【爭議中】+「依摘要層 sourcing」, so the harm is contained — a reader is already told the source is summary-tier. It is a single-sentence over-symmetric framing, fixable in one edit.

**Counter-evidence (L3)**:
- [Consensus — round-1 ⚠️ resolved] Patch #5 landed. c015 (Christensen「脫鉤亦有代價」) is added as a new 【爭議中】 counter-evidence paragraph, and the draft draws the correct policy conclusion「正確問題不是『要不要與中國有任何生產關係』，而是『哪些品項、哪種國防關聯性的西進需要被管制』」. The round-1 senior-consensus「F5 風險敘事單面」gap is resolved.
- [Consensus] 亞德客 is used as a boundary case (深度西進卻未被鎖出，因做氣動元件、非國防相關) — correctly bounds the risk rather than overclaiming.

**Overlooked sources (L4)**:
- [Codex L4] c036 (中國反制不當域外管轄) would correspond more directly to 長臂管轄 法制 than the currently-cited c037/c038/c039. **Meta-note**: [Claude L4] independently checked the accepted pool and found **c036 is not in accepted.jsonl (c001–c080)** — it never entered the pool. Codex's round-1 c036 catch therefore has no actionable target in v2; the draft's c037/c038/c039 (all 摘要層 【爭議中】) is the correct available handling. This Codex catch is **not actionable** and is not carried into the recommendations.
- [Claude L4] c012 (qs=5 summary-tier, chokepoint-economy framing) could be a second academic anchor for the lock-out argument, reducing reliance on the single blocked c011 — optional, c041 一手 + c011 摘要層 already suffice for the mechanism layer.

**Confidence calibration (L5)**:
- [Consensus] Declared 中 — correct. The BIS Entity List mechanism is high (一手規則文本); the named「工具機西進後被鎖出」industry case is an evidence gap and「技術擴散 → 中國軍力」is summary-tier (c011 blocked). The draft writes the gap out explicitly and does not smuggle it into a realised case. [Claude L5] confirms the operator Q5「偷渡」check passed — the draft explicitly states the accepted set has no named「工具機廠因西進被 BIS/EAR 鎖出」case and uses 亞德客 to bound the risk's applicability.

**Suggested revision** (minor edit — one sentence): Tighten the F5 second-paragraph「『非紅供應鏈鎖出』這個議題對台灣廠商是雙向的」 — split the two unlike things: "美方 Entity List 是對台灣廠商的西進鎖出風險；台灣端的戰略貨品管制清單（c043）則是台灣作為出口管制執行方的合規制度". Do not use the symmetric「雙向鎖出」rhetoric to colour Taiwan's own compliance duty as a "lock-out risk". One sentence; operator can edit inline.

## Structural issues (not tied to a single finding)

These are cross-cutting commentary, parked here per spec §6 (strategy A: the draft's explicit Finding 1–5 are the canonical finding IDs; Counter-framing engagement and What-we-don't-know are structural, not findings).

**Counter-framing engagement (6 frameworks) — ✅ solid [Claude, Consensus]**
- [Claude L3] The draft explicitly addresses all six declared counter_framings from brief_expanded.yaml with honest tier labelling (【爭議中】/【推測】). Framework (4)「工具機跟國防製造能力的連結是想像的」honestly concedes the accepted set has no named個案 and marks the link 【爭議中】; framework (6)「藍白砍預算是程序問題」is marked 【推測】 and the draft explicitly says the assessment「超出本稿產業結構分析範圍」 — holding the brief FAILURE MODE「不變成純政治批判」. [Codex] and [Gemini] flag no missing or mishandled counter-framing.

**What we don't know — ✅ solid [Claude L7 + Codex L7 + Gemini L7]**
- [Consensus] The 9-item "What we don't know" list is praised by all three for honest coverage: B-chain has no MOPS primary-doc, Q5 has no named lock-out case, Wassenaar/ECCN treaty layer not deep-read, c011 technology-diffusion source is summary-tier only, 砍案→西進 causality unverifiable with current financials, signed-contract impact unknown, c056 (DSET 403), 南移 lacks quantification, Q6 out of scope. Patch #5's Wassenaar gap line and patch #6's Q6 scope bullet both landed.
- [Codex L7 — optional micro-add] Codex suggests one further small gap line: that the Taiwan-side c043 is a 名單/資料集, not a complete Taiwan export-control statute with ECCN/Wassenaar mapping. This is the same observation as the Finding 5 residual ⚠️; folding the F5 phrasing fix already addresses the substance. A separate gap line is optional.
- [Consensus] access_blocked sources (c011 tandfonline 403, c056 dset.tw 403) have their confidence impact explicitly acknowledged in both "What we don't know" and the F5 Confidence reasoning.

**L6 brief-question coverage — ✅ [Claude L6, Consensus]**
- [Claude L6] Q1→F1 ✅, Q2→Context+F4 ✅, Q3→F2 ✅, Q5→F5 ✅, Q4 (斟酌) distributed across F3/F4/Counter-framing (5) ✅. Q6 (斟酌) — patch #6 added the explicit scope statement to Context and "What we don't know"; the round-1 silent-omission concern is resolved. [Codex L6] and [Gemini L6] independently confirm full Q1–Q5 coverage and accept the Q6 explicit out-of-scope handling. No mandatory brief question is unaddressed.

**L8 conceptual fidelity — SKIPPED [Consensus]**
- [Consensus] Synthesizer was skipped per M4; there is no `synthesize/themes.jsonl` and no `evidence_scope_distribution`. Per reviewer.md L8 spec, the conceptual-fidelity lens does not fire. The draft correctly does not use Dr2 `**{scope}**` paragraph tags. [Claude] notes the extracts' front-matter carries per-extract `evidence_scope`, but L8 requires the themes.jsonl-level `evidence_scope_distribution` — a different object, lens still does not fire. No finding here.

**Operator-note compliance (v2-specific, all confirmed clean) [Claude, Consensus]**
- MOPS Track-4 primary financials (c071–c080) fully used; Synthesizer-skip handled correctly (no Dr2 scope tags); the 6 new cids (c042/c043/c015/c030/c032/c033) all at Dr3 SECONDARY 【爭議中】 with the「未經 deep-read」annotation, none mis-promoted; c050 (亞德客 airtac.net 404) correctly superseded by c079/c080 and not cited; c075 (東台 partial download) correctly paired with c076; 2026-Q1-financials-precede-cut handled honestly in Finding 3. No misjudgement.

**Instruction-following audit (spec §9.4)**
- Meta-merge grep of the three review bodies (r_claude.md, r_codex.md, r_gemini.md) for `state.yaml`, `handoff_log`, `exit_plan_mode`: **no occurrences in any review body.** All three reviewers stayed within review scope. No instruction-following violation to flag for operator.

## Summary recommendations

This draft is publishable with minor edits. **No revision pass and no re-Drafter are required.** The round-1 → round-2 trajectory (🟡 → 🟢) confirms the patch-level revision worked: 5 of 6 prior ⚠️ items resolved cleanly to ✅. Caveats that all three reviews preserved — B-chain has no MOPS primary-doc, Q5 has no named lock-out case, post-cut causality unverifiable, c011 technology-diffusion source summary-tier only — are already in the draft's "What we don't know" and must remain.

1. **[Sole residual ⚠️ — Finding 5] Tighten the「雙向鎖出」phrasing.** Rewrite「『非紅供應鏈鎖出』這個議題對台灣廠商是雙向的」to split two unlike things: "美方 Entity List = 對台灣廠商的西進鎖出風險" vs. "台灣端戰略貨品管制清單（c043）= 台灣作為出口管制執行方的合規制度". Do not use symmetric「雙向鎖出」rhetoric to colour Taiwan's own compliance duty as a "lock-out risk". One sentence; operator can edit inline or fold into a future patch. (Claude L2 + Codex L2 senior consensus.)
2. **[Optional — Finding 1]** Add c025 (deep-read, 無人機廠商第一人稱衝擊, 單廠年產約 500 架) to strengthen「內銷活水被砍」 — not necessary, F1 is ✅. (Claude L4 + Codex L4.)
3. **[Optional — Finding 4]** Split the A→B「母機」inference's first sentence (國防/航太 first, 無人機 as the extrapolation in the next sentence) — stylistic; Codex confirms the fidelity is already sound and the inference already 【專家意見】-marked. (Codex L2.)
4. **[Optional — Finding 5]** c012 (qs=5 summary-tier, chokepoint-economy framing) could be a second academic anchor for the lock-out argument, reducing reliance on the single blocked c011 — not necessary. (Claude L4.)
5. **[Optional — structural]** Add one micro-line to "What we don't know" noting c043 is a 名單/資料集 not a complete Taiwan export-control statute — substance is already covered by recommendation 1; optional. (Codex L7.)

**Do NOT do**: do not promote c029/c030/c032/c033 or any summary-tier source to 【強證據】 — v2 correctly keeps them 【爭議中】, maintain.

**Not actionable**: Codex's round-1 c036 catch (中國反制不當域外管轄, suggested for the 長臂管轄 法制 layer) — c036 is **not in accepted.jsonl** (verified by Claude's L4 pool check); it never entered the pool. The draft's c037/c038/c039 handling is the correct available option. No action.

## Regeneration guidance (if needed)

The draft reaches 🟢 publishable with minor edits — **no revision pass, no re-Drafter.** Recommendation 1 is a one-sentence inline edit; the operator can apply it directly or fold it into a future patch.

- **Critical issues to feed back**: none. The single residual (F5「雙向鎖出」phrasing) is a minor edit, not a critical issue.
- **Sources to prioritise deep-reading (if operator has resources, not blocking publication)**: c011 (tandfonline 403 — Q5 技術擴散 core academic source, currently summary-tier only); c056 (dset.tw 403 — Q2 非紅供應鏈 14-point policy blueprint). Both are "value-add if available", neither blocks publication.
- **Brief questions that need rephrasing**: none. brief Q1–Q5 + 斟酌 Q4/Q6 structure is sound; Q6 being out of scope is now an explicit draft trade-off (brief marks it 斟酌), not a defect.

## Spec / tooling calibration observations (production run #2, v2+ review pass — Phase-4 verdict-formula calibration)

1. **First exercise of the §8 v2+ Claude-weight-0.8 path — worked, but had no effect on the outcome this round.** This is the first multi-model review pass run *with a prior baseline*, so per spec §8 "Claude verdict pass-aware" Claude's general-verdict weight was set to 0.8 (not 1.0). In practice the reduced weight **did not change any verdict** this round, because all three reviewers converged on 🟢 — there was no Claude-vs-Codex disagreement for the weight to tip. The v2+ weighting path is therefore *exercised and verified non-breaking*, but this run did not stress-test it (it would only bite when Claude is the lenient outlier and Codex disagrees). Calibration note for the spec: **the v2+ Claude-weight-0.8 path still needs a run where it is load-bearing** before it can be considered fully validated. A useful spec addition would be a worked example of the weight actually changing a borderline 🟢/🟡 outcome.
2. **§9.2 Claude-over-tolerance check correctly did NOT fire.** Claude is not the most lenient reviewer this round — all three are 🟢, and Gemini (all-✅ on every finding) is strictly the most lenient. §9.2 only escalates when Claude's 🟢 is more lenient than the other two; that condition is not met. No escalation applied. (Contrast round 1, where §9.2 *did* fire on F1/F3.)
3. **§9.3 Codex-bias downgrade fired cleanly on Finding 4 — a clean positive case.** Round 1's calibration note asked the spec to add a worked example of §9.3 *firing*. F4 this round is exactly that example: Codex is the sole F4 dissent, on two items (c059 single-source for 電池稀土; A→B母機 phrasing) — and the draft *already explicitly caveats both* (c059 tagged 【爭議中】+「依摘要層 sourcing」; the A→B inference 【專家意見】-marked with an explicit國防航太≠無人機 disclaimer). Per §9.3 the catches were downgraded to minor priority and F4 resolved to ✅ (matching Claude + Gemini), with Codex's observations preserved in the regeneration guidance rather than dropped. This is the firing-case companion to round 1's not-firing case (F1/F3, where Codex's catches were NOT pre-caveated and so were preserved at ⚠️). Together the two runs give the spec a clean firing / not-firing pair — recommend the spec cite both.
4. **§8 R4 path resolved a unanimous-🟢 configuration without ambiguity.** Three-reviewer 🟢 + Codex zero ❌/🚨 + integrity clean mapped directly to R4 overall 🟢. The only judgment call was whether F5's two-senior-⚠️ residual should pull the overall down via R3 — it does not, because R3 governs revision-pass-level fidelity/calibration failures, and the F5 residual is a single sentence-level phrasing edit on an already-【爭議中】-cap'd source. Recommend the spec clarify that a per-finding ⚠️ that is purely a sentence-level minor edit does not, by itself, trigger an R3 overall downgrade — otherwise a meta-reviewer could mechanically read "two seniors ⚠️ on F5" as an R3 hit and wrongly downgrade a genuinely publishable draft.
5. **`integrity_check.py` bracket-heuristic bug — round-1 false positive did not recur, but the bug is unfixed.** This round's `integrity_report.json` is fully clean: the reviewers wrote the rejected cid as plain-text `c023` per an updated prompt reminder, so the `rejected_cid_cited` bracket-detection heuristic did not mis-fire. **However, the underlying bug — that the check matches any rejected-cid token without audit-context awareness — remains unfixed.** Gemini's `bracket_citation_count` this round is still 12; a single prompt drift that puts a rejected cid in bracket form inside a "draft correctly avoided this" audit note would re-trip the false positive. The prompt reminder is a workaround, not a fix. Round 1's recommendation stands and should be prioritised: exclude audit-context mentions, or demote `rejected_cid_cited` from automatic hard-error to review-required flag.
6. **Patch-level revision validated.** The round-1 meta-verdict was 🟡 "patch-level, NOT re-Drafter". This round confirms that judgment was correctly calibrated: the 6-patch revision pass moved the draft 🟡 → 🟢, resolved 5/6 prior ⚠️ cleanly, introduced exactly one contained side-effect (the F5「雙向鎖出」phrasing), and required no re-Drafter. This is positive evidence that the spec's distinction between "revision pass / targeted patch" and "re-Drafter" is operationally meaningful and that the meta-reviewer's round-1 routing decision was sound.
