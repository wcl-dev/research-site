# Review of llm-user-side-bias insight_v2

**Reviewed on**: 2026-05-18
**Draft**: `projects/llm-user-side-bias/pipeline/draft/insight_v2.md`
**Sources consulted**: accepted.jsonl (45 records), extracts/ (22 deep-reads), brief.md, themes.jsonl

## Verdict

- Finding 1 — 主題層審查研究：✅ solid | 數據引用精確，建立穩固基底
- Finding 2 — 先導研究定位：✅ solid | 成功識別研究缺口，機制對照嚴謹
- Finding 3 — 資訊主權框架：⚠️ needs tightening | 三支柱對應具啟發性，但部分核心文獻僅依賴摘要
- Finding 4 — 知識不平等框架：⚠️ needs tightening | 理論高度充足，但缺乏量化影響數據

Overall: 🟡 needs revision pass | 結構完整且論點強大，但存在嚴格的格式違規（欠缺 L8 範疇標籤）且部分文獻可及性限制了論述深度。

## Per-finding review

### Finding 1 — 主題層審查研究
**Status**: ✅ solid

**Citations audit** (L1):
- 引用密度極高（[c001, c003, c004, c005, c007, c002, c008, c015]），所有事實聲明均有對應 cid。
- 中國源模型拒答率 [c001]、R1dacted 規模 [c003]、CoT 審計 [c004] 均屬高信心聲明且來源 qs≥4。

**Claim-vs-source fidelity** (L2):
- **Pan & Xu (2026) [c001]**: 數據精確對應（百川 60.23%、DeepSeek ~36%、文心一言 32%）。
- **Naseh (2025) [c003]**: 正確引用 68.75% 類別完全拒答之發現。
- **de Man (2025) [c002]**: 準確提取「延遲審查啟動」作為後生成過濾之證據。
- **Zhou & Zhang (2024) [c008]**: 正確標注為 Nature SR 同行評審之高品質證據。

**Counter-evidence check** (L3):
- 未發現明顯遺漏。Draft 提及「跨語言一致」[c003] 與「語言偏差」[c005] 之衝突並提供了解釋路徑。

**Overlooked sources** (L4):
- 接受集中 c017 (ChineseSafe) 提供了更細緻的監管分類基準，雖非必要，但若要強化「刻意設計」之論點可補強。

**Confidence calibration** (L5):
- 宣告信心為「高」，符合 ≥3 來源且 qs≥4 之準則。

**Suggested revision**:
- 無 — 此部分為全文最穩固之實證基底。

### Finding 2 — 先導研究定位
**Status**: ✅ solid

**Citations audit** (L1):
- 引用 [pilot, c012, c013, c011] 支撐身份觸發機制之先例。
- 準確識別 Li et al. (2024) [c012] 為最接近之機制先例（qs=5）。

**Claim-vs-source fidelity** (L2):
- **Li et al. (2024) [c012]**: 準確引用其 44% vs 76% 之拒答落差。
- **Amiri-Margavi (2026) [c011]**: 準確指出即使不拒答，互動品質仍有國籍差異。

**Counter-evidence check** (L3):
- **c213 (Kurata 2024)**: 提及身份預測「對假訊息的需求」，此為「使用者側」研究，Draft 聲明「尚無研究問：宣告不同身份是否得到不同品質回答」依然成立，因 c213 焦點在 demand side 而非 LLM access control side。

**Overlooked sources** (L4):
- 無。

**Confidence calibration** (L5):
- 宣告信心為「中高」，考慮到 pilot 之小規模特性，此標註符合誠實原則。

**Suggested revision**:
- 建議在缺口五中明確區分「宣告身份」（declared identity）與「推論身份」（inferred identity），以防禦對 pilot 人為標籤設計的潛在批評。

### Finding 3 — 資訊主權框架
**Status**: ⚠️ needs tightening

**Citations audit** (L1):
- 核心理論 c021 與政策文獻 c039 均標註為「全文不可及」，符合 L7 之誠實要求。

**Claim-vs-source fidelity** (L2):
- **Spartak (2025) [c023]**: 準確提取「三支柱」框架（立法、技術、文化），並與 pilot 之詞彙觀察進行了極具說服力的對應。
- **Agiza (2024) [c037]**: 準確引用 PEFT 作為政治對齊技術之可行性證明。

**Counter-evidence check** (L3):
- 無。

**Overlooked sources** (L4):
- **c024 (Fratini 2024)**: 提供了中/美/歐主權模型的對照，可協助文章第三步「地緣政治基礎設施」之全球定位。

**Confidence calibration** (L5):
- 宣告信心為「中」，主要受限於 c021 全文不可及，此判定準確。

**Suggested revision**:
- 在引用 c023 時，應更明確說明「三支柱」是 Spartak 對中國整體網路主權的觀察，而將其應用於 LLM 是本研究的推論性貢獻。

### Finding 4 — 知識不平等框架
**Status**: ⚠️ needs tightening

**Citations audit** (L1):
- 引用 [c029, c033] 建立理論支撐。

**Claim-vs-source fidelity** (L2):
- **Mollema (2025) [c033]**: 準確引用「生成式詮釋抹除」（generative hermeneutical erasure）與「知識滅絕」（epistemicide）。
- **Kay et al. (2024) [c029]**: 準確引用「存取不平等」（access injustice）維度。

**Counter-evidence check** (L3):
- 無。

**Overlooked sources** (L4):
- **c030 (Laacke 2023)**: 專門論述對話式 AI 偏見如何構成對使用者作為「認識主體」之傷害，可強化第四步的規範性主張。

**Confidence calibration** (L5):
- 宣告信心為「中」，正確指出缺乏量化實證支持。

**Suggested revision**:
- 將「知識滅絕」概念與 pilot 觀察到的「二二八拒答」更緊密結合：強調這不只是「沒給答案」，而是系統性地使該歷史詮釋框架在使用者視野中消失。

## Structural issues (not tied to a single finding)

- **L8 Concept-fidelity 嚴重缺失 (missing_scope_tag)**: 專案 `themes.jsonl` 已定義 `evidence_scope_distribution`，但 `insight_v2.md` 全文未包含任何 `**{<scope>}**` 標籤。依據 Dr2 合約，每個對應到主題的段落必須攜帶範疇標籤。
- **Missing brief-question coverage (L6)**: 無，Q1–Q3 均有充分覆蓋。
- **Missed gaps in "What we don't know" (L7)**: 缺口列表極其詳盡，尤其是對 c021/c039 可及性的說明展現了 senior-level 的嚴謹性。

## Summary recommendations

1. **強制修正結構標籤**：依據 `themes.jsonl` 的 `evidence_scope_distribution`，為每個 Finding 的段落補上 `**{<scope>}**` 標籤（如：`**{geographic: CN, TW, methodological: empirical-quantitative}**`），這是通往 publishable 狀態的首要條件。
2. **強化 c023 之應用辯護**：在 Section 二框架一中，更清晰地界定 Spartak 框架與 LLM 現象之間的詮釋性橋樑。
3. **新增 c030 與 c024 以補強理論廣度**：c030 可深化認識主體受損的論述；c024 可提供主權競爭的全球背景。

## Regeneration guidance

If the operator wants to re-run the Drafter with this review:
- **Critical issues to feed back**: 全文補上範疇標籤（L8 compliance）；深化規範性框架（t04）與 pilot 發現的連結。
- **Sources to prioritise deep-reading**: 若可能，請 operator 協助取得 `c021` 與 `c039` 全文，以將「資訊主權」信心從「中」提升至「高」。
- **Formatting mandate**: 確保 Draft v3 嚴格遵循 Dr2 輸出規格，包含段落末尾的範疇標記。
