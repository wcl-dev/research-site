# Review of defense-cut-supply-chain-pivot-tw insight_v2

**Reviewed on**: 2026-05-21
**Draft**: projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v2.md
**Sources consulted**: accepted.jsonl (79 records), extracts/ (19 deep-reads, including 10 MOPS primary financials), brief.md, brief_expanded.yaml, extracts/INDEX.md, rejected.jsonl (1 record: c023)

## Verdict

- Finding 1: ✅ solid — Arithmetic confusion resolved; evidence base remains robust.
- Finding 2: ✅ solid — Exemplary use of MOPS primary data; 亞德客 (Airtac) baseline well-integrated.
- Finding 3: ✅ solid — Causal overreach from v1 corrected; time-ordering honesty maintained.
- Finding 4: ✅ solid — B-chain evidence depth balanced; phrasing on westward shift softened.
- Finding 5: ✅ solid — Regulatory layers (c042/c043) and counter-evidence (c015) successfully added.

**Overall: 🟢 publishable — The Drafter has successfully applied all 6 patches from the previous round. The result is a high-fidelity, well-calibrated research memo that balances structural analysis with evidentiary honesty.**

## Per-finding review

### Finding 1 — 被砍的 4700 億，砍掉的是「本土軍工 + 無人載具」，也砍掉了非紅供應鏈承諾的財源
**Status**: ✅ solid

**Citations audit** (L1):
- All factual claims carry citations [c019, c026, c022, c049, c047, c048].
- No orphaned claims; no rejected `c023` citations.
- High-confidence (高) is warranted by the qs=5 deep-read `c019`.

**Claim-vs-source fidelity** (L2):
- The arithmetic fix (lines 39–44) correctly reconciles the potential confusion between the 4700bn total drop and the overlapping 3000bn/3350bn categories.
- "砍後的 7800 億幾乎全是純對美軍購" aligns with `c019`'s itemized breakdown.

**Counter-evidence check** (L3):
- Correctly notes the lack of counter-evidence regarding the "substantive impact" of the budget cut in the accepted set.

**Overlooked sources** (L4):
- Previous round suggested `c017` (stocks) and `c025` (manufacturer reaction). While not cited in this specific finding's text, the overall demand-shock narrative is sufficiently supported by the current citations.

**Confidence calibration** (L5):
- Correctly marked as High (高). The core budget structure is a matter of legislative record.

**Suggested revision**:
- None — the patch successfully resolved the v1 arithmetic ambiguity.

### Finding 2 — 工具機聚落西進中國，是早於砍案、已被一手財報坐實的結構性存量
**Status**: ✅ solid

**Citations audit** (L1):
- Densely cited with primary MOPS documents [c071–c080].
- High-confidence (高) is fully warranted by the primary-data layer.

**Claim-vs-source fidelity** (L2):
- Quantitative claims for 程泰 (c073), 東台 (c075/c076), 瀧澤 (c077/c078), 上銀 (c071/c072), and 亞德客 (c079/c080) were audited against extracts and MOPS filings with zero divergence.
- The 亞德客 (Airtac) profile (functional currency RMB, 94% receivables in China) is accurately represented as a "baseline illustration."

**Counter-evidence check** (L3):
- Cites `c071` (market dispersal) and `c077` (low-end/high-end production layering) as honest counter-evidence.

**Overlooked sources** (L4):
- None significant.

**Confidence calibration** (L5):
- Correctly marked as High (高). Primary financial statements provide the highest possible fidelity for relocation evidence.

**Suggested revision**:
- None — finding holds.

### Finding 3 — 「軍購砍 → 西進加速」目前只能說是壓力與條件，不是已發生的事實
**Status**: ✅ solid

**Citations audit** (L1):
- Citations [c074, c076, c078, c080, c021, c026] support the time-ordering argument.

**Claim-vs-source fidelity** (L2):
- The v1 overreach ("確定無法由年度／補充預算補回") has been corrected to "accepted 集合只能確認不再提二次特別預算... 補回多少仍未知" (line 101), matching `c026`.
- The distinction between MOPS Q1 dates (pre-cut) and the May 8 cut date is strictly maintained.

**Counter-evidence check** (L3):
- Cites `c074` (profitability) and `c071` (low US exposure) as nuances to the "accelerated shift" narrative.

**Overlooked sources** (L4):
- The tension between media framing (`c021`) and zero-outflow financial facts (`c074`) is explicitly discussed (line 97).

**Confidence calibration** (L5):
- Correctly marked as Medium (中) due to the prospective/causal nature of the link.

**Suggested revision**:
- None — the patch successfully restored text/confidence consistency.

### Finding 4 — 雙鏈差別待遇：工具機外銷補不上、無人機整機外銷強勁但 B 鏈仍有中國零組件依賴與上游母機外移風險
**Status**: ✅ solid

**Citations audit** (L1):
- Incorporates `c030, c032, c033` (qs=4 summary-tier) to balance B-chain evidence depth.
- Phrasing on "B 鏈西進" correctly softened to "尚無 B 鏈西進一手案例."

**Claim-vs-source fidelity** (L2):
- A-chain statistics (exports -7.7%, car lathes -18.3%, 24.7% tariff) align with `c062` and `c063`.
- B-chain 21x growth and 36-country reach align with `c018`.

**Counter-evidence check** (L3):
- Counter-framing (1) and (2) adequately handle the "export-hedge" and "business rationality" arguments.

**Overlooked sources** (L4):
- None significant.

**Confidence calibration** (L5):
- Correctly marked as Medium (中) as the cross-chain "hollowing out" effect (A impacting B) remains a structural inference.

**Suggested revision**:
- None.

### Finding 5 — 西進的風險機制：中國長臂管轄、美國 BIS 鎖出、技術擴散三層
**Status**: ✅ solid

**Citations audit** (L1):
- Successfully added `c042` (Entity List statutory text) and `c043` (Taiwan strategic-goods list), fulfilling the previous round's highest-priority L4 gap.
- Added `c015` (Thomas Christensen) as decoupling-cost counter-evidence.

**Claim-vs-source fidelity** (L2):
- The BIS "Inspur Taiwan" case (`c041`) is accurately described.
- The distinction between "mechanism existence" and "industry case occurrence" is strictly held (line 168).

**Counter-evidence check** (L3):
- The inclusion of `c015` (line 163) provides the necessary balance regarding the risks of decoupling.
- 亞德客 is used as a boundary case (line 170) to show that relocation does not always lead to lock-out.

**Confidence calibration** (L5):
- Correctly marked as Medium (中) as direct "tool-machine lock-out" cases are still missing in the accepted pool.

**Suggested revision**:
- None — patches 1 and 5 were correctly implemented.

## Structural issues

- **Missing brief-question coverage (L6)**: None. Q1–Q5 are fully addressed.
- **Missed gaps in "What we don't know" (L7)**: The section is comprehensive. The new scope statement for Q6 (line 27 and 193) correctly handles the "斟酌" optional brief question.
- **Access_blocked sources' impact**: Acknowledged for `c011` (line 188) and `c056` (line 191).
- **Wassenaar Arrangement (L7)**: The gap in deep-reading the treaty text is now honestly acknowledged (line 186).

## Summary recommendations

1. **Publishable as-is.** The draft has been meticulously updated to reflect the multi-model review consensus from the previous round.
2. The "What we don't know" section and the use of 【爭議中】/【專家意見】 tags are exemplary for a high-stake research positioning memo.

## Regeneration guidance

- **No regeneration needed.** The current draft satisfies all PRIMARY and SECONDARY success criteria of the brief.

L8: skipped — Synthesizer skipped per M4, no themes.jsonl.
