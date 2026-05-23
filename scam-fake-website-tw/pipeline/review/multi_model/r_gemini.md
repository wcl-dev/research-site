# Review of scam-fake-website-tw insight_v1 — Gemini

**Reviewed on**: 2026-05-21
**Draft**: projects/scam-fake-website-tw/pipeline/draft/insight_v1.md
**Sources consulted**: accepted.jsonl (43 records), extracts/ (20 deep-reads), brief.md

## Verdict
- Finding 1: ✅ solid | 方法論說明極為完整，精確區分不同分母，符合 brief 核心要求。
- Finding 2: ⚠️ needs tightening | 「A 型下界」的定義略顯混亂，須區分「全 A 型」與「電商 A 型」。
- Finding 3: ✅ solid | 成功利用 160055 序列與法院判決互補，B 型定義純淨。
- Finding 4: ⚠️ needs tightening | 過度依賴摘要層數據 (c049)，信心標註雖正確但內容存在過度引用風險。
- Finding 5: ✅ solid | 法律架構與執行數據對接精確，嚴格區隔 supply/demand 值得肯定。
- Finding 6: ❌ has gap | 趨勢判定「高原期」過於主觀，數據顯示仍有兩位數成長。
- Finding 7: ✅ solid | 成功落實 brief 的 counter-framing 要求，稀釋效應處理誠實。
- Finding 8: ✅ solid | 資料缺口盤點詳盡，符合 Q7 成功標準。

Overall: 🟢 publishable with minor edits | 報告架構嚴謹，量化骨幹紮實，符合 adversarial 審核下之高 fidelity 要求。

## Per-finding review

### Finding 1 — 為何沒有單一官方「假網站佔比」數字
**Status**: ✅ solid
**L1 citations**: 引用密度極高，由 3 個官方資料集 (c025/c043/c027) 交叉證實 C 軸錯位。
**L2 fidelity**: 引用 c047 指出 Whoscall 30.52% 分母為「惡意連結」而非「全案件」，精確對應 extract passage 1。
**L5 confidence calibration**: 宣告【強證據】符合 3+ 來源且含 qs=5 之標準。
**Suggested revision**: none — finding holds.

### Finding 2 — A 型冒名規模與最常被冒名對象
**Status**: ⚠️ needs tightening
**L2 fidelity**: 報告將 moda 165027 的 1,466 筆稱為「A 型假冒網域規模下界」，但 c023 extract 指明該集「母體偏向假冒電商」。
**L8 concept-fidelity**: A 型範圍涵蓋政府、金融與電商，但 1,466 僅是「電商通報」窗口的數字。若將其泛稱為「A 型下界」會產生 scope overreach。
**Suggested revision**: 應修正為「A 型假冒電商網域之規模下界」。

### Finding 3 — B 型非冒名型詐騙網站規模
**Status**: ✅ solid
**L2 fidelity**: 引用 c024 數據 17,306 (2024 高峰) 與 c030/c031/c032 法院判決樣態完全吻合。
**L8 concept-fidelity**: 明確區分 B 型自創品牌與 A 型冒名，且未誤用 A 型證據於 B 型推論。
**Suggested revision**: none — finding holds.

### Finding 4 — 假網站在詐騙流程中的角色與生命週期
**Status**: ⚠️ needs tightening
**L5 confidence calibration**: 雖然標註了【爭議中】與 contested，但「96% 網站 24h 消失」此一載重數字在 c049 中標註為「未一手驗證」。在 Finding 4 中作為核心論點，風險較高。
**L2 fidelity**: c030 法院判決僅提到「隨時更換」，並未給出 24h 比例。報告過度依賴外部 secondary 數據。
**Suggested revision**: 應補充「法院判決僅認定頻繁輪換，24 小時之具體比例仍有待一手數據驗證」之警語。

### Finding 5 — 供給端攔阻成效
**Status**: ✅ solid
**L1 citations**: 引用 c029, c037, c022, c040 等強證據，引用 cid 全數在 accepted.jsonl 內。
**L2 fidelity**: 引用 moda c042 passage 1 關於「1.33% 網站下架佔比」之數據與 extract 逐字吻合。
**Suggested revision**: none — finding holds.

### Finding 6 — 2023–2026 趨勢
**Status**: ❌ has gap
**L2 fidelity**: c023 passage 3 顯示 2024 (517 筆) 至 2025 (588 筆) 仍有 13.7% 的成長。
**L5 confidence calibration**: 報告將此稱為「趨於高原 (高原期)」，這在趨勢分析中屬於 speculative 推論，且與數據呈現的「持續增加」方向不完全一致。
**Suggested revision**: 應將「高原期」改為「成長趨緩但仍持續創下新高」。

### Finding 7 — 需求端稀釋反證
**Status**: ✅ solid
**L3 counter-evidence**: 完美對應 brief 要求。引用 c034 passage 1「8 名被害人全部經由真平台受騙」作為強力的反面錨點。
**L8 concept-fidelity**: 成功處理「手法分流」—— 假投資依賴網站、網購依賴話術，避免了單一比例的誤導。
**Suggested revision**: none — finding holds.

### Finding 8 — 資料缺口與替代估計法
**Status**: ✅ solid
**L7 missed gaps**: 誠實列出調查局數據缺失與 Q6 趨勢薄弱的問題，符合 adversarial 審稿精神。
**Suggested revision**: none — finding holds.

## Structural issues
- **L6 brief-question coverage**: ✅ 全部覆蓋 Q1–Q7。Q4 由 Finding 4 與 Finding 7 (反證) 共同回答，結構優異。
- **L7 missed gaps**: ✅ 報告在 "What we don't know" 節中精確點出 `access_blocked` 來源 (c049) 與 `165dashboard` SPA 的限制。
- **Source-pool integrity**: ✅ 所有引用 cid 均在 accepted.jsonl 中，無 rejected cid。Extracts deep-read 數量 (20) 與 Sources consulted 說明一致。

## Summary recommendations
1. **修正趨勢描述**：將 Finding 6 與趨勢摘要表中的「高原期」修正為更精確的「增速放緩但總量續增」，避免主觀判定。
2. **精確化 A 型稱呼**：將 moda 的 1,466 筆數據明確限制在「A 型假冒電商」子類，而非廣義 A 型下界，以符合 L8 概念忠誠度。
3. **加強 c049 警語**：在 Finding 4 關於 96% 消失率的部分，應更明確指出這是「業界推測值」，目前尚無官方統計可對接。
