# Review of defense-cut-supply-chain-pivot-tw insight_v1 (multi-model meta-merge)

**Reviewed on**: 2026-05-20
**Draft**: projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v1.md
**Review mode**: multi_model — three independent reviewers + meta-merge (this document)
**Reviewed by**: Claude (r_claude.md), Codex (r_codex.md), Gemini (r_gemini.md, advisory)
**Review pass**: #1 of insight_v1.md (no prior review baseline → Claude general-verdict weight = 1.0, full strict adversarial)
**Sources consulted by reviewers**: accepted.jsonl (79 records), extracts/ (19 deep-reads, incl. 10 MOPS primary financials), brief.md, brief_expanded.yaml, extracts/INDEX.md, rejected.jsonl (1 record: c023)

## Verdict

Per-finding meta-verdict (status ↔ score: ✅=0, ⚠️=1, ❌=2, 🚨=3):

- **Finding 1** (4700 億 = 本土軍工 + 非紅供應鏈財源): **⚠️ needs tightening**
- **Finding 2** (工具機聚落西進是一手財報坐實的結構性存量): **✅ solid**
- **Finding 3** (「砍案 → 西進加速」是壓力與條件，非事實): **⚠️ needs tightening**
- **Finding 4** (雙鏈差別待遇): **⚠️ needs tightening**
- **Finding 5** (西進三層風險機制): **⚠️ needs tightening**
- Counter-framing engagement (6 frameworks) — structural: **✅ solid**
- What we don't know — structural: **✅ solid** (one L7 omission noted)

**Overall meta-verdict: 🟡 needs revision pass — close to publishable; one lightweight targeted patch pass, NOT re-Drafter.**

This is a draft with evidence discipline clearly above pipeline average. All three reviewers agree there is **zero 🚨 and zero ❌**: no concept-fidelity violation, no rejected-cid hard error (rejected pool is only c023, which the draft correctly avoided), no extract-level fabrication. Finding 2 is unanimously ✅. The disagreement is narrow: Claude rated Findings 1/3 ✅ and the overall 🟢; Codex rated Findings 1/3/4/5 ⚠️ and the overall 🟡; Gemini (advisory) rated overall 🟢.

The meta-verdict resolves to 🟡 via §8 R3 (≥2 models ⚠️ on findings carrying source-fidelity / confidence-calibration issues — applies to F4 and F5, where Claude and Codex both flag ⚠️) and the §9.2 Claude-over-tolerance escalation rule (Claude 🟢 on F1/F3 where Codex raises a *specific, non-pre-caveated* L1/L2 issue → escalate those findings to ⚠️). It is **not** an R4 🟢 because R4 requires Codex to have no findings worse than ✅ on a fidelity/calibration axis, and Codex carries four ⚠️. It is firmly **not** 🔴 (no R1 trigger). The gap between 🟢 and 🟡 here is one revision pass, not a rewrite.

## Source-pool Integrity

`integrity_check.py` output (`integrity_report.json`): `actual_accepted_n: 79`, `actual_extract_n: 19`, `any_count_mismatch: false`. Claude and Codex: `usable: true`, zero errors, zero hallucinated cids. Their accepted/extract counts match.

**`any_hard_error: true` — VERIFIED FALSE POSITIVE. Not a halt condition. Documented here per operator instruction.**

The report flags Gemini `usable: false` with one error `rejected_cid_cited: c023`. This is a **false positive**, verified by the operator and independently confirmed in the meta-merge:

- The rejected pool contains exactly one record, c023 (rejected for a dead URL).
- **All three reviewers mention c023, all in the same benign L1-audit context** — correctly noting that c023 is the rejected record and that the draft properly avoided citing it:
  - Gemini r_gemini.md L24: 「引用之 [c023] 在 rejected.jsonl 中（因 URL 失效），Draft 正確避開，改引其他新聞源。」
  - Codex r_codex.md L24: 「無 rejected cid；未引用 rejected c023，通過硬錯誤檢查。」
  - Claude r_claude.md L33: 「無 cid 落在 rejected.jsonl（rejected 僅 c023，未被引用）。」
- Gemini did **not** misuse c023 as evidence. It correctly audited that the draft avoided the rejected cid — the substantively correct L1 behaviour.
- The check flagged Gemini and not Codex/Claude solely because of **citation form**: Gemini wrote the cid in bracket form `[c023]` inside its audit note (`bracket_citation_count: 24` for Gemini vs 3 for Claude, 0 for Codex), while Codex/Claude wrote plain `c023`. `integrity_check.py`'s bracket-detection heuristic cannot distinguish (a) an evidentiary citation of a rejected record from (b) a reviewer correctly naming the rejected record it is auditing.

**Resolution for this merge**: Gemini is treated as integrity-substantively-clean. It remains junior / advisory per spec §2 regardless (its weight is governed by §8, not by this false positive). No Gemini recommendation was discarded on integrity grounds.

**Calibration finding for `integrity_check.py` (production run #2 calibration data)**: the `rejected_cid_cited` hard-error check false-positives when a reviewer **correctly** cites a rejected cid, in bracket form, inside a "draft correctly avoided this" L1-audit note. The check currently bracket-matches any rejected cid token without context. Recommended fixes (either is sufficient):
1. Exclude rejected-cid mentions that occur within audit-context sentences (e.g. co-occurring with negation / 「避開」/「未引用」/「rejected.jsonl」/「通過硬錯誤檢查」 in the same clause), or
2. Make the meta-reviewer / operator context-check every `rejected_cid_cited` hit before halting (i.e. demote it from automatic hard-error to "review-required flag").
Without one of these, a well-behaved Gemini review that *correctly performs the L1 rejected-cid audit* will keep tripping the halt — a perverse incentive that penalises the desired behaviour. This is the single most actionable tooling-calibration item from run #2.

## Model Consensus / Conflict

**Consensus (all three agree):**
- **Finding 2 is ✅ solid** — unanimous. The 10 MOPS primary financials (c071–c080) for 程泰/東台/瀧澤/上銀/亞德客 are cross-verified at extract level by both senior reviewers; Claude audited ~15 quantitative sub-claims against 8 extracts with zero divergence.
- **Zero 🚨 / zero ❌** — no reviewer raised a hard error, concept-fidelity violation, or extract-level fabrication.
- **No rejected-cid misuse** — all three confirm the draft avoided c023.
- **Time-ordering honesty (Finding 3)** — all three explicitly praise that the draft holds the line "2026-Q1 financials precede the 2026-05-08 cut → financials cannot show post-cut behaviour" and frames "cut → westward shift" as conditional probability, not fact. This directly satisfies the brief FAILURE MODE「把『軍購砍 → 西進』當必然結果」.
- **L8 skipped** — all three note Synthesizer was skipped per M4, no `themes.jsonl`, so the conceptual-fidelity lens does not fire.
- **Q5 not smuggled** — all three confirm Finding 5 keeps "mechanism exists" distinct from "industry case has occurred"; the draft uses 亞德客 to *bound* the risk rather than overclaim it.

**Conflict (where the models diverge):**
- **Finding 1**: Claude ✅ / Codex ⚠️ / Gemini ✅. Codex is the sole source of the budget-arithmetic clarity catch (3000 + 3350 > 4700 reads as additive). Resolved to ⚠️ — see Finding 1 below.
- **Finding 3**: Claude ✅ / Codex ⚠️ / Gemini ⚠️. Codex flags 「確定無法補回」as overreaching c026; Gemini flags weak engagement with the c021「醞釀投資潮」media framing. Two ⚠️ vs one ✅. Resolved to ⚠️.
- **Finding 4**: Claude ⚠️ / Codex ⚠️ / Gemini ✅. Both senior reviewers agree B-chain evidence is thin; Gemini's ✅ is advisory and per §8 R5/R6 cannot offset two senior ⚠️. Resolved to ⚠️.
- **Finding 5**: Claude ⚠️ / Codex ⚠️ / Gemini ⚠️. Unanimous ⚠️.
- **Overall**: Claude 🟢 / Codex 🟡 / Gemini 🟢 (advisory). Per §8 R6 Gemini's overall verdict is advisory and cannot tip the meta-verdict; the real disagreement is Claude 🟢 vs Codex 🟡. Resolved to 🟡 — see Verdict above.

**How the disagreement was used, not flattened**: Claude's 🟢 is not "wrong" — its point that no finding needs a rewrite stands and is preserved in the regeneration guidance (patch-level, not re-Drafter). Codex's 🟡 is not "hyper-critical noise" — its F1 arithmetic catch and F3「確定」catch are specific, extract-checkable, and not pre-caveated by the draft, so §9.3 (Codex-bias downgrade) does **not** apply to them. The meta-verdict 🟡 carries Codex's catches into the revision list while carrying Claude's "patch not rewrite" judgment into the regeneration guidance.

## Per-finding review

### Finding 1 — 被砍的 4700 億，砍掉的是「本土軍工 + 無人載具」，也砍掉了非紅供應鏈承諾的財源

**Meta-status**: ⚠️ needs tightening

**Citations / fidelity (L1–L2)**:
- [Consensus] Core budget figures (9000 億對外軍購 / 3000 億本土軍工 / 7800 億 / 62.4% / 4700 億落差 / 三大重點含「打造非紅供應鏈」) are word-aligned with c019 (qs=5 deep-read) — verified independently by Claude and Codex against c019 Passages 1–3. No divergence.
- [Codex L1 — sole catch, drives the ⚠️] The phrase "集中落在『本土軍工產業鏈 + 委製 + 3350 億無人載具』" presents an **arithmetic-confusion risk**: 3000 + 3350 already exceeds 4700, so a lay reader (the stated audience: 對外公開、一般大眾) may read these as additive line items. The draft does not explicitly state that these are overlapping reporting categories / political line-item descriptions rather than a clean sum. This catch is **not pre-caveated by the draft** (the draft's caveat at line 35 addresses 已簽合約 vs 未來規劃, a different issue), so §9.3 Codex-bias downgrade does NOT apply — it remains a genuine ⚠️.
- [Codex L1] The counter-framing claim "『程序問題而非實質』在 accepted 集合內無直接證據支撐" should be reworded to the precise "accepted set 未見能證明實質無影響的來源" — a phrasing tightening, minor.

**Counter-evidence / overlooked sources (L3–L4)**:
- [Claude L4] c017 (qs=4, 股市對砍案即時反應, 雷虎 -9%) is an unused same-direction source that would extend the 內銷衝擊 argument from budget figures to an observable market reaction. Minor add.
- [Codex L4] c020 (3350 億無人機預算砍) and c025 (deep-read, 無人機廠商第一人稱衝擊, 年產約 500 架供國軍) are unused and directly support the "內銷活水被砍" claim — c025 in particular is more direct than the currently-cited c047/c048. Recommended add.

**Confidence calibration (L5)**:
- [Consensus] Declared 高. Acceptable — figures rest on qs=5 deep-read c019 + multiple corroborating summary-tier sources. [Codex L5] adds the caveat that the L1 arithmetic ambiguity, if unaddressed, will drag perceived credibility; calibration itself is sound.

**Suggested revision** (patch-level): Rewrite the 4700/3000/3350 passage so the three numbers read as "different reporting-tier descriptions of the deleted 本土 / 無人載具 items" rather than an additive budget sum; optionally add c017 / c020 / c025.

### Finding 2 — 工具機聚落西進中國，是早於砍案、已被一手財報坐實的結構性存量

**Meta-status**: ✅ solid — unanimous

**Citations / fidelity (L1–L2)**:
- [Consensus, strongest section of the draft] Each of the five firms (程泰/東台/瀧澤/上銀/亞德客) has primary-doc citation for every figure; all are MOPS deep-read financials. [Claude L2] audited ~15 quantitative sub-claims against 8 MOPS extracts — zero divergence (亞崴蘇州帳面值, 程泰吳江, 蘇州東昱實收/帳面, 瀧澤機電浙江, 中國上銀公司匯出/帳面/銷貨佔比/進貨佔比, 亞德客寧波/八家合計/功能性貨幣/應收帳款集中度). [Codex L2] independently confirmed the same firm-by-firm. [Gemini L2] independently confirmed 上銀 17.26% and 亞德客 378 億 / 94%.
- [Consensus] The draft correctly scopes 亞德客 as 精密機械／自動化元件廠 (not CNC 整機) and explicitly marks it a baseline illustration, not a「軍購砍 → 西進」case — matching the c079 scope_caveat.

**Counter-evidence (L3)**:
- [Consensus] The draft proactively cites c071 (上銀 disperses 東歐+東南亞, not deeper into China) and c077 (瀧澤 low-tier-in-China / high-tier-in-Taiwan layering) as honest counter-evidence — verified against extracts.

**Minor catches (do not move the status)**:
- [Codex L2] "台灣只是上市掛牌地" (line 46) is slightly overstated rhetoric — recommend softening to "台灣主要是上市與部分營運／貿易節點". Wording only.
- [Codex L3] Could add one line that 出口中國佔比下降 ≠ 脫鉤 (in-locale manufacturing can substitute for exports) — c062 extract already hints at this. Optional.
- [Gemini L4] c027 (qs=3, 65 家工具機廠赴上海搶單) could reinforce the "聚落式集體動向" narrative. Optional, qs=3.

**Suggested revision**: none required — finding holds. Optionally soften the "上市掛牌地" phrasing.

### Finding 3 — 「軍購砍 → 西進加速」目前只能說是壓力與條件，不是已發生的事實

**Meta-status**: ⚠️ needs tightening

**Citations / fidelity (L1–L2)**:
- [Consensus] Time-ordering claims all carry MOPS Q1 citations (c074/c076/c078/c080); the draft correctly frames "cut → shift" as conditional. All three reviewers explicitly praise this as the draft's best discipline.
- [Codex L1/L2/L5 — sole catch, drives the ⚠️] Condition (1) at line 59 reads「內銷國防訂單的預期增量**確定無法**由年度／補充預算補回...此條件偏成立 [c026]」. c026 supports only「不再提二次特別預算」; it does **not** support「確定無法補回」. The hedge「偏成立」is present, but the word「確定」inside the clause is a near-high-certainty term that c026 does not license — an orphan/overreach. This is **not pre-caveated** (the surrounding hedge addresses a different aspect), so §9.3 does not downgrade it. Genuine ⚠️.
- [Codex L2] The c078 "浙江嘉善廠房仍在興建中" claim is partly reconstructed from extract abstract/附註 rather than a verbatim primary passage — recommend softening to「extract 記錄顯示」rather than asserting it as a verbatim primary passage.
- [Claude L2/L5] Marginal: "上銀美國曝險低於 3% [c071]" is a 2024-年報 figure (c071 temporal range 2014–2025) placed in a sentence next to "2026 Q1" — a reader may misread it as a Q1 number. Recommend tagging it as 上銀 2024-年報口徑. Nuance-level.

**Counter-evidence / overlooked sources (L3–L4)**:
- [Gemini L3 — third-opinion catch, integrity-clean] The draft mentions 工具機景氣回穩 [c074] but engages weakly with the tension between the c021「醞釀登陸投資潮」media framing and the financial fact「本期匯出為 0」. Gemini recommends explicitly noting the media framing may carry time-lag or be over-hyped. Valid as third-opinion data; it co-points with Codex's general F3 ⚠️ and reinforces the status (it does not, alone, set it — per §8 R6).
- [Codex L4] c045/c044 (南向資料) could be added as a counter showing hedge need not run through China; c010 (政治風險與 firm exit) could calibrate the policy-shock → relocation conditionality. Both summary-tier, optional.

**Confidence calibration (L5)**:
- [Consensus] Declared 中 — correct, given the prospective nature of the causal link. [Codex L5] notes the「確定」wording is inconsistent with a 中 confidence and should be weakened for internal consistency.

**Suggested revision** (patch-level): Change「確定無法由年度／補充預算補回」to「目前 accepted set 只能確認不再提二次特別預算，年度／補充預算能補多少仍未知」; tag「上銀美國曝險 < 3%」as 2024-年報口徑; optionally add one sentence contrasting the c021 media framing with the Q1 zero-outflow fact.

### Finding 4 — 雙鏈差別待遇：工具機外銷補不上、無人機整機外銷強勁但仍有西進壓力

**Meta-status**: ⚠️ needs tightening (Claude ⚠️ + Codex ⚠️ — senior consensus; Gemini ✅ advisory cannot offset, §8 R5)

**Citations / fidelity (L1–L2)**:
- [Consensus] A-chain statistics (c062 TAMI, c063 台中市府, both qs=5 deep-read) are word-aligned and verified — total exports −7.7%, 對中佔比 32.2%→26.7%, 輸美實質稅率 24.7%, 毛利率 < 20%, 台中減班休息 49 家次/1,357 人. B-chain c018 (qs=4 deep-read) figures (產值 129 億, 整機外銷 21 倍, 29.5 億, 36 國) word-aligned.
- [Claude L2] "車床類年減 18.3%" is in c062's INDEX summary but not in the c062 extract verbatim — fidelity acceptable (INDEX confirms it) but it is an extract-unverifiable sub-claim; recommend the Drafter confirm the source page.
- [Codex L1/L2] The B-chain "仍有西進壓力" framing in the title and section-head risks letting a reader infer an *observable* B-chain westward shift. Codex recommends retitling to「仍有供應鏈中國依賴與上游牽制」. Claude reaches the same place via L2: the draft holds the line in body text (line 70 explicitly says 零組件依賴 is structural, not realised westward shift) but the title/closing 語氣 is the weak point. **Senior consensus that B-side phrasing needs tightening.**
- [Codex L2] 瀧澤 c077 supports CNC 車床 用於「國防航太工業零件加工」 — it does not directly support「無人機零組件」; the draft marks the cross-chain inference 【專家意見】, acceptable, but should avoid equating 國防航太 with 無人機.

**Counter-evidence / overlooked sources (L3–L4) — senior consensus this is the main gap**:
- [Claude L3+L4 + Codex L4 — Consensus] B-chain export evidence is markedly thinner than A-chain: B rests on **one deep-read (c018) + two summary-tier (c029/c059)**, vs A-chain's two qs=5 deep-reads. Both reviewers name unused ready qs=4 B-chain sources in accepted: c030, c032, c033, c057, c058 (台歐/波蘭/捷克 無人機合作、對歐出口成長). Recommend adding 1–2.
- [Claude L3+L4] c015 (qs=5 peer-reviewed; INDEX explicitly flags it as "decoupling-is-costly counter-evidence required for dual-chain balance") is unused — the dual-chain framing and Counter-framing (2) both need this academic counter-evidence. (Codex and Gemini both independently raise c015 under Finding 5 — see there.)
- [Codex L4] c025 could reinforce the 內銷活水 importance to the B-chain; c056 (DSET formal page, currently 403) is the core 非紅供應鏈 policy source and Finding 4 cites only the c059 FB summary for the B-chain policy layer.
- [Gemini L4] c029 (波蘭吸走 6 成出口) — Gemini recommends *promoting* the 60% figure from 【爭議中】 to 【強證據】 since multiple media cross-confirm it. **Meta-note: do NOT adopt this as written.** c029 is summary-tier; promoting a summary-tier figure to 【強證據】 conflicts with Dr3 tier discipline and with Claude's L1 audit. Treat Gemini's catch as "c029 is well-corroborated and worth keeping" but retain the 【爭議中】 tier. This is a §8 R5 / §9 case where the advisory reviewer's *recommendation* is overridden while its *observation* (c029 is solid) is noted.

**Confidence calibration (L5)**:
- [Consensus] Declared 中 — correct. A/B contrast is well-sourced; the cross-chain "工具機西進掏空無人機長期承諾" extrapolation has no single direct source, correctly pulling the overall to 中.

**Suggested revision** (patch-level): Retitle / soften the B-chain head to「無人機鏈仍有中國零組件依賴與上游母機外移風險；尚無 B 鏈西進一手案例」; add 1–2 qs=4 B-chain export sources (c030/c032/c033) to balance A/B evidence depth; add a second same-direction source for「電池稀土依賴中國」rather than relying solely on the c059 FB post; the Drafter should confirm the c062 page for「車床類 −18.3%」.

### Finding 5 — 西進的風險機制：中國長臂管轄、美國 BIS 鎖出、技術擴散三層

**Meta-status**: ⚠️ needs tightening — unanimous (Claude ⚠️ + Codex ⚠️ + Gemini ⚠️)

**Citations / fidelity (L1–L2)**:
- [Consensus] BIS/Entity List mechanism is strongly sourced: c041 (qs=5 deep-read, Federal Register primary text — Inspur Taiwan, all-items, policy-of-denial) and c040 (qs=5, EAR framework) are word-aligned and verified by all three.
- [Consensus] The draft correctly limits 瀧澤 c077 (公司法修正 → 資本調整) as a 公司法 / non-sanctions matter, and correctly limits 上銀 c071 (專利維權勝訴) as a technology-diffusion side-fact, NOT 長臂管轄 binding — fidelity-model behaviour, praised by Claude and Codex.
- [Consensus] c011 is correctly held at 【爭議中】 summary-tier with explicit "未經 deep-read" labelling — Dr3 tier ceiling respected. All three confirm.
- [Codex L2] "工具機（尤其五軸加工中心）正是典型雙用途品項" — c040 extract does not list machine tools / 五軸 verbatim; recommend rewording to "依 EAR dual-use 框架推論" or adding c042/eCFR.
- [Consensus — operator-specified review point] Finding 5 does **not** smuggle "mechanism exists" into "industry case has occurred": the draft explicitly states accepted set has no named「工具機廠因西進被 BIS/EAR 鎖出」case and uses 亞德客 to *bound* the risk. All three confirm this passed.

**Overlooked sources (L4) — the draft's clearest L4 gap, senior consensus**:
- [Claude L4 + Codex L4 — Consensus] **c042 (qs=5, primary_doc — eCFR Part 744 Entity List current statutory text) and c043 (qs=5, primary_doc — 台灣戰略性高科技貨品出口管制名單) are unused.** INDEX.md explicitly instructs the Drafter to cite c042 as the Q5 法源 and c043 to cover the Taiwan-side strategic-goods control layer. Finding 5 currently runs only "US BIS + China counter-measures" two ends and **omits the Taiwan-side control layer entirely**. This is the highest-priority L4 gap and a direct reinforcement of brief PRIMARY 訴求 2.
- [Codex L4 — Codex-unique catch] c036 (中國反制不當域外管轄) corresponds more directly to 長臂管轄 法制 than the currently-cited c038/c039; recommend adding c036 or lowering the certainty of that segment.
- [Codex L1/L4 — Codex-unique, brief-coverage] **Wassenaar Arrangement** is named in brief Q5 but the draft barely processes it — only BIS/EAR appear. Recommend either citing a Wassenaar source or adding to "What we don't know" that the Wassenaar/ECCN treaty layer was not deep-read. (Claude's L6 review did not surface this specific Wassenaar gap — a catch Codex adds and the meta-merge preserves.)
- [Claude L4] c012 (qs=5 peer-reviewed, chokepoint-economy framing) could be a second academic anchor for the lock-out argument, reducing reliance on the single blocked c011.

**Counter-evidence (L3)**:
- [Consensus — Codex L3 + Gemini L3] **c015 (Thomas Christensen, "Mutually Assured Disruption" / decoupling-is-costly) is unused.** Both Codex and Gemini independently flag this: the draft's Finding 5 risk narrative is one-sided on "technology diffusion → defence cost" and c015 provides the academic counter that cross-strait interdependence can be a stabilising force and decoupling carries its own conflict risk. Recommend adding c015 to the 技術擴散 segment or Counter-framing engagement. (Claude raised the same c015 under Finding 4 / dual-chain balance — so all three reviewers converge on c015 being the key missing counter-evidence, just attached to different findings.)
- [Consensus] 亞德客 as a deep-westward-but-not-locked-out case is well-handled — it correctly bounds the risk rather than overclaiming.

**Confidence calibration (L5)**:
- [Consensus] Declared 中 — correct. BIS mechanism is high; 長臂管轄/技術擴散 are summary-tier/indirect; the named industry lock-out case is absent. The draft writes the gap out explicitly and does not smuggle it into a realised case.

**Suggested revision** (patch-level): Add c042 (Entity List current statutory text) and c043 (Taiwan strategic-goods control list) — both INDEX-instructed and currently unfulfilled; add c036 for the 長臂管轄 法制 layer; add c015 as the decoupling-cost counter-evidence; reword "五軸正是典型雙用途品項" to a framework inference; add a "What we don't know" line that Wassenaar/ECCN treaty text was not deep-read.

## Structural issues (not tied to a single finding)

These are cross-cutting commentary, parked here per spec §6 rather than forced into a finding row.

**Counter-framing engagement (6 frameworks) — ✅ solid [Claude, Consensus]**
- [Claude L3] The draft explicitly addresses all six declared counter_framings from brief_expanded.yaml, with honest tier labelling (【爭議中】/【推測】). No reviewer flagged a missing or mishandled counter-framing. The one gap inside this section is the absence of c015 (decoupling-cost academic counter) under Counter-framing (2) — folded into the Finding 5 revision list above.

**What we don't know — ✅ solid, one omission [Claude L7 + Codex L7]**
- [Consensus] The 7-item "What we don't know" list is praised by all three for honest coverage (B-chain no MOPS primary, no named lock-out case, c011 summary-tier, post-cut causality unverifiable, signed-contract impact unknown, c056 403, 南移 lacks quantification). access_blocked sources (c011 tandfonline 403, c056 dset.tw 403) have their confidence impact explicitly acknowledged.
- [Codex L7 — Codex-unique omission catch] Missing: Wassenaar / ECCN treaty text not deep-read, and the Taiwan-side strategic-goods control layer (c043) not incorporated. Add a line.
- [Claude L6/L7 — Claude-unique omission catch] **Q6 (international comparison: US/Ukraine/Israel/Korea) is not covered by any finding.** brief marks Q6「（斟酌）」optional, so this is **not a hard structural defect** — but accepted set contains c012 (chokepoint economies, qs=5) and c016 (ally-shoring, qs=5) tagged for Q6. For a public-facing deliverable, explicitly stating "本稿不處理 Q6 國際比較（屬 brief 斟酌題）" is more honest than the current silent omission. Gemini independently raises the same Q6 point [Gemini L6] and suggests using c012/c016 for a one-line international anchor. Recommend: add a one-line scope statement to "What we don't know", optionally a short c012/c016 comparison paragraph.

**L6 brief-question coverage [Claude]**
- [Claude L6] Q1→F1 ✅, Q2→Context+F4 ✅, Q3→F2 ✅, Q5→F5 ✅, Q4 (斟酌) distributed across F3/F4/Counter-framing (5) ✅. Q6 (斟酌) silently omitted — see above. No mandatory brief question is unaddressed.

**L8 conceptual fidelity — SKIPPED [Consensus]**
- [Consensus] Synthesizer was skipped per M4; there is no `synthesize/themes.jsonl` and no `evidence_scope_distribution`. Per reviewer.md L8 spec, the conceptual-fidelity lens does not fire. The draft correctly does not use Dr2 `**{scope}**` paragraph tags. (Claude notes the extracts' front-matter carries per-extract `evidence_scope`, but L8 requires the themes.jsonl-level `evidence_scope_distribution` — different object, lens still does not fire.) No finding here.

**Operator-note compliance (v2-specific, all confirmed clean) [Claude]**
- MOPS Track-4 primary financials (c071–c080) fully used; Synthesizer-skip handled correctly (no Dr2 scope tags); c050 correctly superseded by c079/c080 and not cited; c075 partial-download handled correctly (paired with c076); 2026-Q1-financials-precede-cut handled honestly in Finding 3. No misjudgement.

**Instruction-following audit (spec §9.4)**
- Meta-merge grep of the three reviews for `state.yaml`, `handoff_log`, `exit_plan_mode`: **no occurrences in any review body.** All three reviewers stayed within review scope. No instruction-following violation to flag for operator.

## Summary recommendations

This draft is close to publishable. One lightweight targeted patch pass resolves all ⚠️ items — **no re-Drafter required**. Caveats that all three reviews preserved (B-chain has no primary-doc, no named lock-out case, post-cut causality unverifiable, c011 summary-tier) are already in the draft's "What we don't know" and must remain.

1. **[Highest priority — Finding 5] Add c042 + c043** (both qs=5 primary_doc, both INDEX-instructed and currently unfulfilled). c042 = Entity List current statutory text as the Q5 法源; c043 = Taiwan-side strategic-goods control layer, currently entirely absent. Direct reinforcement of brief PRIMARY 訴求 2.
2. **[Finding 1] Rewrite the 4700/3000/3350 passage** so the numbers do not read as an additive budget sum — present them as different reporting-tier descriptions of the deleted 本土/無人載具 items. (Codex's sole catch; genuine clarity issue for a general-public audience.)
3. **[Finding 3] Weaken「確定無法由年度／補充預算補回」** to「accepted set 只能確認不再提二次特別預算，補回多少仍未知」— c026 does not license「確定」. (Codex's sole catch; restores text/confidence consistency.)
4. **[Finding 4] Soften the B-chain title/head** to make explicit there is no B-chain westward-shift primary case, and add 1–2 ready qs=4 B-chain export sources (c030/c032/c033) to balance A/B evidence depth. (Claude + Codex consensus.)
5. **[Finding 5] Add c015** (decoupling-cost counter-evidence) to balance the one-sided risk narrative, and add a "What we don't know" line on Wassenaar/ECCN not being deep-read. (Codex + Gemini consensus on c015.)
6. **[Structural] Add a one-line scope statement** that Q6 international comparison is not covered (brief 斟酌題) — explicit beats silent for a public deliverable; optionally a short c012/c016 paragraph. (Claude + Gemini.)
7. **[Minor]** Tag「上銀美國曝險 < 3%」as 2024-年報口徑 (Claude); soften「台灣只是上市掛牌地」(Codex); Drafter confirm c062 source page for「車床類 −18.3%」(Claude).

**Do NOT do**: promote c029 (波蘭 6 成出口) from 【爭議中】 to 【強證據】 (Gemini's advisory suggestion) — c029 is summary-tier and promoting it would break Dr3 tier discipline. Keep it 【爭議中】.

## Regeneration guidance (if needed)

The draft reaches 🟡 needs revision pass — **patch-level, not re-Drafter.** Recommended: operator runs one lightweight revision pass, or hands the Drafter a targeted patch (not a full rewrite).

- **Critical issues to feed back (patch-level)**: (1) Finding 5 — add c042/c043 (INDEX-instructed Q5 法源 unfulfilled); (2) Finding 1 — fix the 4700/3000/3350 additive-reading ambiguity; (3) Finding 3 — weaken「確定」; (4) Finding 4 — soften B-chain head + add 1–2 qs=4 B-chain sources; (5) Finding 5 — add c015 + Wassenaar gap note.
- **Sources to prioritise deep-reading (if operator has resources, not blocking)**: c011 (tandfonline 403 — Q5 技術擴散 core academic source, currently summary-tier only); c056 (dset.tw 403 — Q2 非紅供應鏈 14-point policy blueprint). Both are "value-add if available", neither blocks publication.
- **Brief questions that need rephrasing**: none. brief Q1–Q5 + 斟酌 Q4/Q6 structure is sound; Q6 being skipped is a draft trade-off (brief already marks it 斟酌), not a brief defect.

## Spec / tooling calibration observations (production run #2)

1. **`integrity_check.py` `rejected_cid_cited` false-positive** (detailed in Source-pool Integrity above): the check halts on a *correct* L1 rejected-cid audit when the cid is written in bracket form. It penalises the desired reviewer behaviour. Fix: exclude audit-context mentions, or demote the check from automatic hard-error to review-required flag. **This was the only thing that would have wrongly halted run #2** and is the top tooling item.
2. **Verdict formula §8 worked cleanly for a three-way split.** The Claude-🟢 / Codex-🟡 / Gemini-🟢(advisory) configuration resolved unambiguously: R6 removed Gemini's overall verdict from the tally; R3 + the §9.2 Claude-over-tolerance escalation produced 🟡; R4 was correctly blocked because Codex carried four ⚠️. No formula ambiguity encountered.
3. **§9.3 Codex-bias downgrade — correctly did NOT fire here.** Codex's two sole-source catches (F1 arithmetic, F3「確定」) were checked against the draft and found to be specific, extract-verifiable, and NOT pre-caveated. §9.3 only downgrades a Codex hedge-catch that the draft *already explicitly caveats*; that condition was not met, so both catches were preserved at ⚠️. Suggest the spec add an explicit worked example of "§9.3 does not fire" — meta-reviewers may otherwise over-apply the downgrade and silently drop legitimate Codex catches.
4. **Gemini advisory recommendations need a "observation vs recommendation" split.** Gemini's c029 catch contained a *correct observation* (c029 is well-corroborated) wrapped in an *incorrect recommendation* (promote to 【強證據】). The current §8 R5/R6 wording says Gemini's verdict cannot tip the meta-verdict, but does not address the case where a Gemini *recommendation* would, if adopted verbatim, violate tier discipline. Suggest §9 add: "the meta-reviewer adopts Gemini's observation but may reject its recommendation when the recommendation conflicts with Dr3 tier rules or a senior reviewer's L1 audit." This run handled it correctly by judgment; the spec should make it explicit.
5. **Convergent catches across findings.** All three reviewers flagged c015 as missing counter-evidence, but attached it to *different* findings (Claude→F4, Codex→F5, Gemini→F5). Boundary-alignment strategy A (draft's explicit Finding 1–5) handled this fine because the meta-merge cross-references the catch — but a purely mechanical per-finding merge would have under-counted c015's importance. Worth a spec note that convergent catches should be detected across finding boundaries, not just within them.
