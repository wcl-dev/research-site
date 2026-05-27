# Review of ai-kiosk-consent-tw insight_v1 — Gemini

**Reviewed on**: 2026-05-27
**Draft**: projects/ai-kiosk-consent-tw/pipeline/draft/insight_v1.md
**Sources consulted**: accepted.jsonl (92 records), extracts/ (27 deep-reads), brief.md, themes.jsonl (9 themes)

## Verdict
- F1: ✅ solid | 保守下界與上界雙端展開，符合 Brief 關於 A/B/C 分離的要求。
- F2: ✅ solid | 時間軸與資料流拆解詳盡，Showcase A/B 具備強證據支持。
- F3: ✅ solid | 五源交叉驗證 vendor wording vacuum，論證強度高。
- F4: ✅ solid | 憲法與法律 spine 論證嚴密，特別是釋字 603 與 111 憲判 13 的轉化運用。
- F5: ⚠️ needs tightening | CyberLink 作為反例的論證具備高度洞察，但需注意其 SDK 供應商與 Kiosk 部署方的角色差異。
- F6: ✅ solid | 勾選對照表為 Mandatory 要求，已準確執行。
- F7: ✅ solid | 「結構性零」的四重論證是本案最尖銳發現，申訴 proxy 算力推論嚴謹。
- F8: ✅ solid | 誠實處理 EU AI Act 的覆蓋限制，國際對照具備參考價值。

## Per-finding analysis

### Finding 1 (Q1a) — 部署規模雙端展開
- **L1 Citation density**: ✅ 每項數據皆有引用（c032, c041, c033, c049, c046, c047, c082）。
- **L5 Confidence calibration**: ✅ 區分 [strong] 下界與 [contested] 上界（1000+ 台 kiosk），標註正確。
- **L6 Brief-question coverage**: ✅ 涵蓋 Q1a，且嚴格執行 B（身分辨識）、C（會員資料）分離，避免數字膨脹。
- **L8 Concept-fidelity**: ✅ 帶有 `{conceptual:A; temporal:2024+; geographic:TW}` 等標籤。

### Finding 2 (Q1b) — 雙 use-case showcase
- **L1 Citation density**: ✅ 具備 ≥3 源 cross-confirmed。
- **L2 Claim-vs-source fidelity**: ✅ Showcase A（雙月）引用 c032 關於「雲端回傳總部」的描述準確。
- **L7 Gaps / unknowns**: ✅ 誠實標註「桌面觀察 AI 系統」為 [contested-planned]。
- **L8 Concept-fidelity**: ✅ A∩D 交集點（無告知介面）描述具體。

### Finding 3 (Q2 + Q7) — Wording vacuum 系統性現象
- **L1 Citation density**: ✅ 五源交叉驗證（c032, c041, c037, c042, c038），密度極高。
- **L3 Counter-evidence honesty**: ✅ 主動引入 CyberLink (c045) 作為 framing 對照，非選擇性呈現。
- **L5 Confidence calibration**: ✅ 標註 [strong] 具備充足證據。

### Finding 4 (Q4) — 法律與憲法 spine
- **L2 Claim-vs-source fidelity**: ✅ 釋字 603 與 111 憲判 13 的引用與 case-transfer 論證嚴密，特別是關於「間接識別性」的標準運用。
- **L5 Confidence calibration**: ✅ 直接引用 primary docs (c053, c054, c097, c098)，[strong] 標籤名實相符。
- **L7 Gaps / unknowns**: ✅ [speculative-mechanism] 段落誠實標註 RAM/cache 留存機制為技術推論。

### Finding 5 (Q4 + Q7) — Vendor internal split
- **L3 Counter-evidence honesty**: ⚠️ 提到 CyberLink (c045) 的 D 軸承認。需注意 c045 為 2023 年資料，且 CyberLink 角色為上游 SDK 提供者，其與下游 kiosk 部署方（WiXtar）的責任界限應更明確區分，以防 WiXtar 援引「責任在下游餐廳」之辯護。
- **L5 Confidence calibration**: ✅ 標註為 [contested]，符合其 partial_counter_framing 性質。

### Finding 6 (D 軸三層對照) — 勾選對照表
- **L6 Brief-question coverage**: ✅ 完美回應 Brief 要求之「業者 × 三層」勾選對照表。
- **L1 Citation density**: ✅ 每格勾選皆附帶 cnn 引用來源。

### Finding 7 (Q3 + Q6) — 四重結構性沉默
- **L2 Claim-vs-source fidelity**: ✅ 「3,058 件/年」推論被正確標註為 **capacity upper-bound proxy**而非投訴量下界，避免了 Over-claim。
- **L4 Overlooked sources**: ✅ 成功整合新北 (c105)、桃園 (c106) 及台中 (c107) 的 Opendata 資料，量化論證紮實。
- **L6 Brief-question coverage**: ✅ Q3 (退出層) 與 Q6 (執法) 合併處理，邏輯連貫。

### Finding 8 (Q5) — 國際最低標準對照
- **L3 Counter-evidence honesty**: ✅ 誠實指出 EU AI Act Art. 5 對餐飲 kiosk 的禁令**不直接覆蓋**（僅限職場/教育），避免了「國外都禁了」的過度情緒化 framing。
- **L2 Claim-vs-source fidelity**: ✅ BIPA Home Depot 案 (c073) 引用準確，為台灣 A∩D 灰區提供極佳對照。

## Cross-cutting concerns
- **Integrity**: 引用之 cid 全數位於 `accepted.jsonl` 中，未見 `rejected.jsonl`（如 c001, c003 等）之誤用。
- **L8 Scope tagging**: Findings 標段皆具備 `{conceptual:…}` 等 scope tag，符合 Dr1 spec。
- **Consistency**: TL;DR 核心論點與 Findings 內容一致，特別是「四重結構性零」與「憲法 spine」的對應。

## Overall verdict
🟢 **publishable as-is**
(僅 Finding 5 關於 vendor 角色細微差異建議在 meta-merge 時由 Claude 主審酌予潤飾，但不影響整體品質)
