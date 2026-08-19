# Review of defense-cut-supply-chain-pivot-tw insight_v2

**Reviewed on**: 2026-05-21
**Draft**: `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v2.md`
**Sources consulted**: accepted.jsonl (79 records), extracts/ (19 deep-reads), brief.md

## Verdict

One-line status per finding:
- Finding 1: ✅ solid
- Finding 2: ✅ solid
- Finding 3: ✅ solid
- Finding 4: ⚠️ needs tightening
- Finding 5: ⚠️ needs tightening

Overall: 🟢 publishable with minor edits

## Per-finding review

### Finding 1 — 被砍的 4700 億，砍掉的是「本土軍工 + 無人載具」，也砍掉了非紅供應鏈承諾的財源
**Status**: ✅ solid

**Citations audit** (L1):
- 前輪 ⚠️「4700/3000/3350 讀成加總」已修好。draft 明確寫「4700 億是總落差」「不是 3000 億 + 3350 億」「兩者涵蓋範圍重疊、不能直接相加」。
- 無 rejected cid；rejected pool 僅 c023，draft 未引用。
- 小 L4 殘留：c025（無人機廠商第一人稱衝擊、年產約 500 架）仍未用。這不是硬傷，因 F1 已用 c049/c047/c048 建出內銷 pipeline，但 c025 會比 c047/c048 更直接支撐「產業衝擊」。

**Claim-vs-source fidelity** (L2):
- c019 Passage 1 支持「約 9000 億對外軍購、其餘 3000 億打造本土軍工產業鏈」；Passage 3 支持「7800 億、62.4%、落差 4700 億」；Passage 2 支持「打造非紅供應鏈」為三大重點。draft 對 c019 的核心轉述忠實。
- c049 extract 支持「四家得標廠、69.51 億、履約至 2027-09-30」。draft 也正確保留「已簽合約是否受砍案影響未確認」。

**Counter-evidence check** (L3):
- draft 對「程序問題而非實質」只採有限版本，未把 political framing 變成主論點。accepted set 未見能證明「砍案對產業無實質影響」的來源。

**Overlooked sources** (L4):
- 可選補強：c017 股市反應、c020 3350 億無人機預算砍、c025 廠商反應。缺席不影響 finding 成立。

**Confidence calibration** (L5):
- 高，合理。預算結構與政策目標由 qs=5 c019 深讀支撐；具體無人機 pipeline 則以【爭議中】處理，tier 正確。

**Suggested revision**:
- none — finding holds；若還要磨稿，可加 c025 一句補「廠商第一人稱衝擊」。

### Finding 2 — 工具機聚落西進中國，是早於砍案、已被一手財報坐實的結構性存量
**Status**: ✅ solid

**Citations audit** (L1):
- citation density 充足：程泰、東台、瀧澤、上銀、亞德客均有 MOPS primary-doc citation。
- 無高信心孤證；五家公司分散支撐「結構性存量」。
- 亞德客被定位為「精密機械／自動化元件廠而非 CNC 工具機整機」與「baseline illustration」，避免了概念偷渡。

**Claim-vs-source fidelity** (L2):
- c071/c072 支持上銀中國上銀公司人民幣 3 億資本、累積匯出約 NT$15 億、帳面價值 NT$28.2 億、台灣母廠賣中國子公司佔合併營收 17%。
- c077/c078 支持瀧澤浙江子公司「生產三軸以上聯動數控機床」、2026 Q1 帳面價值約 NT$4.5 億、本季投資利益 NT$36m。
- c079 支持亞德客 8 家中國子公司、約 NT$378 億對陸投資帳面值、功能性貨幣人民幣、94.42% 應收帳款在中國。
- 未發現 extract-level divergence。

**Counter-evidence check** (L3):
- draft 主動放入上銀「東歐＋東南亞」分散、瀧澤「低階中國／高階台灣」分層，counter-evidence honesty 合格。

**Overlooked sources** (L4):
- c027、c028、c066 可作 see-also，但 qs 較低或重複，不必納入正文。

**Confidence calibration** (L5):
- 高，合理。這是 v2 最穩的 finding。

**Suggested revision**:
- none — finding holds.

### Finding 3 — 「軍購砍 → 西進加速」目前只能說是壓力與條件，不是已發生的事實
**Status**: ✅ solid

**Citations audit** (L1):
- 前輪 ⚠️「確定無法補回」已改弱為「方向上偏成立、量級未知」。這與 c026 只能支持「不再提二次特別預算」相符。
- MOPS Q1 時點 citation 密度足夠：c074/c076/c078/c080 均早於 2026-05-08，支撐「財報拍不到砍案反應」。

**Claim-vs-source fidelity** (L2):
- c074 extract 明確支持「程泰五家中國子公司 2026 Q1 無新增匯出」與「工具機本業轉小幅獲利」。
- c078 支持「2025-07-18 仍有核准」「浙江子公司 2026 Q1 認列投資利益約 NT$36m」。draft 寫「extract 記錄顯示 2026 Q1 浙江嘉善廠房仍在興建中」，已避開逐字引用；可接受，因 c078 caveat 說嘉善廠房細節來自 abstract/不動產附註而非完整逐字 passage。
- draft 正確把 c021「醞釀登陸投資潮」與 c074「Q1 本期匯出為 0」放成張力，不再把媒體趨勢語言讀成已發生事實。

**Counter-evidence check** (L3):
- 已納入景氣回穩、程泰轉盈、上銀美國曝險低於 3% 等反向訊號。這些足以防止「砍案必然西進」的 failure mode。

**Overlooked sources** (L4):
- c010 可補 policy shock→firm relocation 的學術框架，c044/c045 可補南移替代，但現稿已有 Counter-framing (5)，非必要。

**Confidence calibration** (L5):
- 中，正確。draft 把「結構性存量」與「砍案後加速」拆開，因果語氣守住了。

**Suggested revision**:
- none — finding holds.

### Finding 4 — 雙鏈差別待遇：工具機外銷補不上、無人機整機外銷強勁但 B 鏈仍有中國零組件依賴與上游母機外移風險
**Status**: ⚠️ needs tightening

**Citations audit** (L1):
- 前輪 patch 大致落地：標題已由「仍有西進壓力」改成「中國零組件依賴與上游母機外移風險」，並新增 c030/c032/c033，且三者都放在【爭議中】摘要層，Dr3 tier 正確。
- 仍有一個 citation-density 弱點：B 鏈「電池與稀土仍依賴中國」是 finding 標題級 claim，但正文只靠 c059（DSET FB 摘要層）。這不是錯，但對一個 public memo 的關鍵 counter-nuance 仍偏薄。

**Claim-vs-source fidelity** (L2):
- c062/c063 對工具機外銷弱勢支撐很強：總出口 -7.7%、中國佔比 26.7%、對台工具機輸美 24.7% 實質稅率、毛利率低於 20%、49 家次/1,357 人減班休息，均與 extract 對齊。
- c018 對無人機外銷強支撐很強：產值 129 億、整機外銷 21 倍、外銷 29.5 億、36 國買方，均與 extract 對齊。
- cross-chain 推論仍需小心。draft claim：「工具機（A）是製造無人機相關零組件的『母機』。」c077 extract 原文只支持「CNC 車床重要用途：……國防航太工業零件加工」。draft 隨後有寫「國防航太不等同於無人機零組件」並標【專家意見】，所以不是 fidelity violation；但建議把第一句也改成「國防／航太零件母機」，再把無人機放在下一句作外推。

**Counter-evidence check** (L3):
- draft 有承認「沒有某無人機廠商西進中國的一手案例」，也承認外銷低基期與波蘭集中度風險。這一點合格。
- 仍應避免讀者把「B 鏈仍有中國零組件依賴」讀成「B 鏈已西進」。正文有守住，但 TL;DR 的「仍依賴中國、且長期受上游工具機產能掏空牽制」語氣較強，最好同樣加「目前無 B 鏈西進一手案例」的短 caveat。

**Overlooked sources** (L4):
- c057、c058 未用；它們可補台烏歐共同生產與對歐出口成長，會讓 B 鏈外銷對沖更紮實。
- 對「電池／稀土依賴中國」沒有第二來源；若 accepted set 內找不到，應在句內保留「依 c059 摘要層」而不要把它當已 fully established 的 B 鏈底層事實。

**Confidence calibration** (L5):
- 中，正確。A/B 對比本身高；B 鏈零組件依賴與 A→B 長期牽制是摘要層 + 結構外推，拉低整體 confidence。

**Suggested revision**:
- 把「工具機是製造無人機相關零組件的母機」改成「工具機是國防／航太零件加工的母機；延伸到無人機零組件屬結構外推」；另為 c059 的電池／稀土依賴補第二來源，或明確說「目前僅摘要層支撐」。

### Finding 5 — 西進的風險機制：中國長臂管轄、美國 BIS 鎖出、技術擴散三層
**Status**: ⚠️ needs tightening

**Citations audit** (L1):
- 前輪 patch 已落地：c042、c043、c015 都已補入，且 c042/c043/c015 均依 operator note 放在【爭議中】並標「未經 deep-read 一手驗證」，沒有 Dr3 tier 錯誤。
- draft 沒有偷渡「工具機西進後已失去歐美訂單」。它明確寫 accepted set 沒有具名產業案例，這通過 Q5 最重要的 over-claim 檢查。
- 仍有一個 L4/L1 弱點：中國端長臂法制仍主要靠 c038/c039/c037 摘要層，未用更直接的 c036（RFI：中國立法反制不當域外管轄、在華跨國企業風險增）。不是硬傷，但 c036 比 c037 更貼近「法制架構」。

**Claim-vs-source fidelity** (L2):
- c041 extract 支持 Inspur Taiwan、all items subject to EAR、policy of denial、Entity List 法律效果。draft 對 BIS 鎖出機制忠實。
- c040 extract 只支持 EAR 管轄 dual-use items；draft 已修成「工具機依 EAR 雙用途品項框架推論」而非條文直引，前輪問題已修好。
- c077 支持「中國公司法修正→浙江孫公司減資／增資調整」，draft 正確把它定位為公司法支配，不說成制裁法案例。
- c071 支持上銀中國仿冒／專利訴訟勝訴與查處 126 家工廠；draft 正確說這是技術擴散風險側面，不說成長臂管轄。
- c043 的用法稍微偏滿：accepted snippet 說它是「幫企業 screen trading partners against export-control entity lists」的政府資料集；draft 進一步寫成「台灣自身亦有戰略性高科技貨品出口管制名單／制度」。方向可接受，但它不是完整台灣出口管制法規文本。若要稱「法源層次補齊」，最好補「名單／資料集層」而非「完整法源」。

**Counter-evidence check** (L3):
- c015 已納入，並用來限制「全面脫鉤」強主張；亞德客也被用作深度西進但未鎖出的 counter-case。這是 v2 的實質改善。
- Q5「機制存在 vs 個案發生」界線守住：draft 明確說 Inspur Taiwan 非工具機廠，亞德客非國防相關、非歐美依賴。

**Overlooked sources** (L4):
- c036 應補到中國長臂／反長臂法制段，或至少替換 c037 作較直接來源。
- c012/c016 可作非紅供應鏈／chokepoint economies 的國際框架，但 draft 已選擇不展開 Q6，缺席可接受。

**Confidence calibration** (L5):
- 中，正確。BIS 機制高；台灣端 c043、長臂法制、技術擴散與具名工具機 lock-out case 都有 evidence gap，整體不能標高。

**Suggested revision**:
- 把 c043 描述收窄為「台灣端出口管制名單／screening dataset」，不要暗示它已補完整台灣法源；另補 c036 或把中國端法制語氣再降一格。

## Structural issues (not tied to a single finding)

- Missing brief-question coverage (L6): Q1→F1、Q2→F4、Q3→F2/F3、Q4→F3/F4/Counter-framing、Q5→F5 均有覆蓋。Q6 已在 Context 與 What we don't know 明列「斟酌題、刻意不展開」，可接受。
- Missed gaps in "What we don't know" (L7): 主要 gaps 都有列出：B 鏈無 MOPS 一手檔、沒有工具機西進後失去歐美訂單具名案例、Wassenaar/ECCN 未 deep-read、c011/c056 access gap、砍案後因果需等後續財報。可再補一個小 gap：台灣端 c043 只是名單／資料集，非完整出口管制法規與品項分類分析。
- Access_blocked sources' impact not acknowledged: c011、c056 已明列；c015 也標摘要層。合格。
- L8: skipped — Synthesizer skipped per M4, no themes.jsonl. No Dr2 `evidence_scope_distribution`; draft 正確未使用 Dr2 scope tags。
- Patch verification: 6 個 v1→v2 patch 均已實際落地；未發現新 cid 被放進【強證據】違反 Dr3 的問題。

## Summary recommendations

1. F4：補強或收窄「B 鏈電池／稀土依賴中國」；目前只有 c059 摘要層支撐。
2. F4：把 A→B 母機推論的第一句再收窄，先說「國防／航太零件」，再說「延伸到無人機屬結構外推」。
3. F5：補 c036，或降低中國端長臂法制段的制度確定性。
4. F5 / What we don't know：註明 c043 是台灣端管制名單／資料集，不是完整台灣出口管制法規與 ECCN/Wassenaar 對應。

## Regeneration guidance (if needed)

If the operator wants to re-run the Drafter with this review:
- Critical issues to feed back: none requiring re-Drafter；只需 minor edit pass。
- Sources to prioritise deep-reading: c059/c056 for B 鏈零組件依賴與非紅供應鏈政策；c036 for 中國反長臂法制；Wassenaar/ECCN or Taiwan SHTC statutory text if Q5 法規層要更硬。
- Brief questions that need rephrasing: none.