# Review of defense-cut-supply-chain-pivot-tw insight_v2

**Reviewed on**: 2026-05-21
**Draft**: projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v2.md
**Review pass**: #2（v2+ review pass — 審 insight_v2.md，第一輪 consolidated review 在 review/review.md，審的是 insight_v1.md，verdict 🟡 patch-level）
**Reviewer**: Claude（multi_model — 平行 reviewer 之一，meta-merge 階段才做 lens 加權）
**Sources consulted**: accepted.jsonl（79 records）、extracts/（19 deep-reads，含 10 筆 MOPS 一手財報）、brief.md、brief_expanded.yaml、extracts/INDEX.md、rejected.jsonl（1 record：c023）、前一輪 review/review.md

## Verdict

逐 Finding 狀態：

- **Finding 1**（4700 億 = 本土軍工 + 無人載具 + 非紅供應鏈財源）：✅ solid
- **Finding 2**（工具機聚落西進是一手財報坐實的結構性存量）：✅ solid
- **Finding 3**（「砍案 → 西進加速」是壓力與條件，非事實）：✅ solid
- **Finding 4**（雙鏈差別待遇）：✅ solid
- **Finding 5**（西進三層風險機制）：⚠️ needs tightening
- Counter-framing engagement（6 框架）— 結構：✅ solid
- What we don't know — 結構：✅ solid

**Overall：🟢 publishable with minor edits。**

🚨 數：**0**。❌ 數：**0**。前一輪 4 個 ⚠️（F1/F3/F4/F5）中，F1/F3/F4 經 6 patch 修訂後已達 ✅；F5 patch 落地正確、實質改善，但補進的台灣端法源（c043）與「雙向出口管制」論述引入了一個新的措辭精度問題（見 F5），仍掛 ⚠️，惟屬 minor-edit 等級，不需 revision pass。整體較 v1（🟡）明顯收斂，已達可發表門檻。

本稿證據紀律在 pipeline 平均之上：41 個被引 cid 全部落在 accepted.jsonl（c001–c080）、無一落在 rejected.jsonl（rejected 僅 c023，未被引用，draft 正確避開）；無 extract 層級的捏造；Dr3 tier 規則（摘要層證據 cap【爭議中】）逐筆遵守。

## 6 個 v1→v2 patch 落地查證

| # | Patch | 是否解決前輪 ⚠️ | 有無引入新問題 |
|---|---|---|---|
| 1 | F5 +c042 +c043（法源補三端） | ✅ 已落地 — F5【爭議中】段明引 c042 eCFR Part 744、c043 台灣戰略貨品名單 | ⚠️ 見 F5：「台灣端管制」論述措辭把 c043（一份比對清單資料集）寫成廠商面臨的「鎖出」風險，方向略偏 |
| 2 | F1 4700/3000/3350 改寫 | ✅ 已解決 — F1【強證據】段明寫「4700 億是原版 1.25 兆與砍後 7800 億的總落差，不是 3000+3350 的加總」，並區分「大分類 vs 被標舉的指標品項」 | 無 — 數字仍精確，未引入新數字錯誤 |
| 3 | F3「確定無法補回」改弱 | ✅ 已解決 — F3 條件(1)現為「方向上偏成立、量級未知」，與「壓力與條件」framing 一致；「確定」一詞已移除 | 無 |
| 4 | F4 軟化 B 鏈 framing +c030/c032/c033 | ✅ 已解決 — F4 標題改為「B 鏈仍有中國零組件依賴與上游母機外移風險」，內文明寫「不主張 B 鏈已發生可觀察的西進」；c030/c032/c033 三筆 qs4 來源已補入、皆 cap【爭議中】+ 摘要層 annotation | 無 — 新 cid 未被放進【強證據】段，未違反 Dr3 |
| 5 | F5 +c015 + Wassenaar gap | ✅ 已解決 — F5 新增【爭議中】段引 c015（脫鉤亦有代價 counter-evidence）；What we don't know 新增 Wassenaar/ECCN 條約層 gap 一行 | 無 |
| 6 | +Q6 scope statement | ✅ 已解決 — Context 段新增「斟酌題範圍說明」、What we don't know 末項明寫 Q6 國際比較為刻意取捨而非遺漏 | 無 |

6 個 patch 全部落地，5 個乾淨解決前輪 ⚠️，第 1 個解決了前輪 ⚠️（法源層不再只談美中兩端）但 c043 的論述定位需一句話收緊（見 F5）。前輪「Do NOT do」項（不要把 c029 升格【強證據】）— v2 draft 正確保留 c029 在【爭議中】，未誤升。

## Per-finding review

### Finding 1 — 被砍的 4700 億，砍掉的是「本土軍工 + 無人載具」，也砍掉了非紅供應鏈承諾的財源

**Status**：✅ solid

**Citations audit（L1）**：
- 無 orphan。核心預算數字（1.25 兆二分結構 9000 億／3000 億、砍後 7800 億、62.4%、4700 億落差、三大重點含「打造非紅供應鏈」）全部繫於 c019（qs=5 deep-read）。
- 【強證據】tier 標示正確：c019 為 qs=5 一手深讀，達高信心門檻；【爭議中】段（c026/c022/c024、c049/c047/c048）皆 cap 在摘要層 tier 且附「依摘要層 sourcing」annotation。
- 無過度宣稱：4700 億落差精確掛 c019，已簽 69.51 億合約是否受影響明白標【爭議中】「中等不確定」。

**Claim-vs-source fidelity（L2）**：
- 對 c019 extract 三段 Passage 逐句核對：「9000 億對外軍購 + 3000 億本土軍工」（Passage 1）、「三大重點含打造非紅供應鏈」（Passage 2）、「砍後 7800 億 = 前 3000 億 FMS + 後 4800 億愛國者三型、佔 62.4%、落差 4700 億」（Passage 3）— **逐字對齊，零分歧**。
- patch #2 查證：前輪 Codex 的「3000+3350 讀起來像加總」catch 已修好。draft 現明寫「3000 億指原版『打造本土軍工產業鏈』的整體匡列；3350 億無人載具是政治論述中常被單獨點名的重點項目；兩者涵蓋範圍重疊、不能直接相加」。對一般大眾讀者，加總誤讀風險已消除。

**Counter-evidence check（L3）**：
- grep accepted.jsonl「程序」「實質」相關訊號：未見任何能證明「砍案對產業實質無影響」的來源。draft 的措辭「accepted 集合內未見任何能證明『砍案對產業實質無影響』的來源」已是前輪建議的精確版本，正確。

**Overlooked sources（L4）**：
- c017（qs=4，砍案後股市即時反應、雷虎 -9%）、c020（qs=4，3350 億無人機預算砍）、c025（deep-read，無人機廠商第一人稱衝擊、單廠年產約 500 架）為同方向未引用來源。前輪即標為「optional add」。v2 仍未納入 — 但這是 cherry-pick 邊界內的合理取捨（draft 已有 c049 一手合約數字 + c047/c048 pipeline），不構成 L4 缺陷。c025 是 deep-read 一手第一人稱衝擊，若 operator 想再強化「內銷活水被砍」可考慮補，但非必要。

**Confidence calibration（L5）**：
- 宣稱「高」。c019 為 qs=5 deep-read + 多筆摘要層交叉一致，達「≥3 sources incl. qs≥4」門檻；「已簽合約是否受影響」明白降為中等不確定。calibration 正確。

**Suggested revision**：
- 無 — finding 成立。若 operator 有餘裕，可選擇性補 c025（deep-read 第一人稱衝擊），但非必要。

### Finding 2 — 工具機聚落西進中國，是早於砍案、已被一手財報坐實的結構性存量

**Status**：✅ solid（前輪三模型一致 ✅，v2 未動此段，維持）

**Citations audit（L1）**：
- 五家廠商（程泰／東台／瀧澤／上銀／亞德客）每一個數字皆有 MOPS 一手 primary_doc 引用。【強證據】tier 對應 qs=5/qs=4 一手財報，正確。
- 無 orphan：亞崴蘇州帳面值、程泰吳江、蘇州東昱實收/帳面、瀧澤機電浙江帳面值、中國上銀匯出/帳面/銷貨佔比/進貨佔比、亞德客寧波/八家合計/功能性貨幣/應收帳款集中度，全部繫 cid。

**Claim-vs-source fidelity（L2）**：
- 抽查 c074 extract：程泰「五家中國子公司本期匯出/收回欄全為 0」— c074 Passage 1 確認附表七 2026 Q1「本期匯出/收回」欄全 0，draft 對齊。
- 抽查 c077 extract：瀧澤機電(浙江)「營業項目生產三軸以上聯動數控機床」「浙江嘉善」— c077 Passage 3 逐字確認。
- 前輪 Claude L2 已對 ~15 個量化子claim 對 8 份 MOPS extract 核對、零分歧；v2 未改動此段任何數字，無需重審 — 維持前輪結論。
- 前輪 Codex 的「台灣只是上市掛牌地」措辭 catch：v2 draft 現為「台灣主要是上市與部分營運／貿易節點」，已採前輪建議軟化。✅

**Counter-evidence check（L3）**：
- draft 主動引 c071（上銀轉投資網絡橫跨歐美日、風險段認知分散方向是「東歐＋東南亞」）與 c077（瀧澤「低階機在中國、高階與智慧產線根留台灣」分層）作 counter-evidence — 對 extract 核對，c071/c077 確有此內容。誠實處理「西進是分層的、不是全產能搬遷」。

**Overlooked sources（L4）**：
- c027（qs=3，65 家工具機廠赴上海搶單）、c066（qs=3，天下「成也中國敗也中國」）為同方向 see-also。皆 qs=3，draft 不引屬合理取捨，非缺陷。

**Confidence calibration（L5）**：
- 宣稱「高」。五家廠商西進存量由 MOPS 一手財報逐條坐實 + 產業新聞 c021 獨立佐證，遠超「≥3 sources incl. qs≥4」門檻。正確。

**Suggested revision**：
- 無 — finding 成立，是全稿最紮實的一段。

### Finding 3 — 「軍購砍 → 西進加速」目前只能說是壓力與條件，不是已發生的事實

**Status**：✅ solid

**Citations audit（L1）**：
- 時序 claim 皆有 MOPS Q1 引用（c074/c076/c078/c080）；「2026 Q1 財報截至 2026-03-31，早於 2026-05-08 砍案」由四筆季報 cid 支撐。
- 【專家意見】tier 用於「條件性的機率上升」這條前瞻推論 — tier 標示正確，前瞻外推不冒充【強證據】。

**Claim-vs-source fidelity（L2）**：
- patch #3 查證：前輪 Codex 的「確定無法補回」overreach catch 已修好。draft 條件(1)現為「目前 accepted 集合只能確認國防部表態『不再提二次特別預算』[c026]……年度／補充預算實際能補回多少，accepted 證據無法回答，故此條件只能說『方向上偏成立、量級未知』」。c026 的證據邊界（只支撐「不再提二次特別預算」）與 draft 措辭已對齊，「確定」一詞移除。✅
- 抽查「2026 Q1 浙江嘉善廠房仍在興建中」：draft 寫「extract 記錄顯示 2026 Q1 浙江嘉善廠房仍在興建中」— 前輪 Codex 建議用「extract 記錄顯示」而非斷言為逐字一手段落，v2 已採此措辭。✅
- 抽查「上銀美國曝險低於 3%」：draft 寫「上銀年報（2024-年報口徑）顯示其美國市場曝險低於 3% [c071]」— c071 extract「銷售美國市場之比重低於 3%」確認；前輪 Claude 建議標「2024-年報口徑」以免讀者誤讀為 Q1 數字，v2 已加註。✅
- 抽查「程泰工具機本業 2026 Q1 由鉅額虧損轉小幅獲利 [c074]」：c074 Passage 2 確認部門損益由 2025 同期 (982,854) 轉為 2026 Q1 30,191。對齊。

**Counter-evidence check（L3）**：
- 前輪 Gemini 指 v1 對「c021 醞釀投資潮媒體框架 vs 一手財報本期匯出 0」之間張力處理偏弱。v2 draft 第二段【爭議中】現明寫「工商時報『台工具機業醞釀登陸投資潮』的媒體框架 [c021] 與一手財報『2026 Q1 本期匯出為 0』[c074] 之間其實有張力 ——『醞釀／評估』是業者意向與趨勢觀察，可能帶有時間落差、也可能被媒體放大成已實現的投資潮」。此前輪 ⚠️ 已實質修好。✅
- Counter-evidence 段引 c074（程泰工具機本業轉盈 → 景氣回穩、不一定急於西進）與 c071（上銀美國曝險 < 3%）— 誠實保留「若景氣回升、廠商不一定急於西進」的另一面。

**Overlooked sources（L4）**：
- c010（qs=5 摘要層，政治風險提高外資退出率、firm entrenchment 緩解）為前輪 Codex 點名的 optional add，可校準「政策衝擊 → 遷移」的條件性。v2 未納入 — 屬可選，非缺陷（draft 的條件式 framing 已自足）。

**Confidence calibration（L5）**：
- 宣稱「中」。「西進是結構性存量且砍案前趨勢向上」由一手財報強力支撐；「砍案 → 加速」受財報時序限制本質前瞻 — 整體標「中」與證據狀態相符，內部一致（「確定」已移除，不再與「中」矛盾）。正確。

**Suggested revision**：
- 無 — finding 成立。時序誠實（2026 Q1 財報早於砍案、因此「砍案 → 西進」只能是壓力與條件）守得乾淨，直接命中 brief FAILURE MODE「把『軍購砍 → 西進』當必然結果」。

### Finding 4 — 雙鏈差別待遇：工具機外銷補不上、無人機整機外銷強勁但 B 鏈仍有中國零組件依賴與上游母機外移風險

**Status**：✅ solid

**Citations audit（L1）**：
- A 鏈統計（c062 TAMI、c063 台中市府，皆 qs=5 deep-read）對應【強證據】，正確。B 鏈 c018（qs=4 deep-read）對應【強證據】，達門檻。
- 補進的 c030/c032/c033 三筆 B 鏈外銷來源皆在【爭議中】段，每筆附「依摘要層 sourcing，未經 deep-read 一手驗證」— **未被放進【強證據】段，未違反 Dr3**。patch #4 落地正確。
- 跨鏈「工具機西進掏空無人機長期承諾」推論標【專家意見】，tier 正確。

**Claim-vs-source fidelity（L2）**：
- 抽查「2025 1–8 月工具機總出口年減 7.7%」「對中佔比 32.2%→26.7%」：c062 Passage 1/2 逐字確認。
- 「車床類年減 18.3%」：c062 extract 三段 Passage **未含**此數字逐字（Passage 1 只有「切削工具機 -8.9%、總出口 -7.7%」）。draft 已誠實加註「依 INDEX 確認此一車床類數字載於 TAMI 同份產業現況報告」，INDEX.md line 29 確有「車床類年減 18.3%」。前輪 Claude 的「建議 Drafter 確認 source page」catch — v2 已用 INDEX 引註處理，屬可接受的 extract-unverifiable 子claim 誠實標示。非分歧。
- 「輸美實質稅率 24.7%（MFN 4.7% + 對等 20%）」「毛利率低於 20%」「台中減班休息 49 家次/1,357 人」：c063 Passage 2/3 逐字確認。
- 「無人機產值 129 億、整機外銷成長 21 倍、外銷產值 29.5 億、買方 36 國」：c018 Passage 1/2 逐字確認。
- patch #4 查證 — 前輪 Codex/Claude 的「B 鏈標題語氣易讓讀者誤推可觀察的西進」catch：v2 標題已改為「B 鏈仍有中國零組件依賴與上游母機外移風險」，且內文【爭議中】段開頭明寫「accepted 集合**沒有**『某無人機廠商西進中國』的一手案例，本稿不主張 B 鏈已發生可觀察的西進；……指的是供應鏈依賴與結構性風險，不是已實現的西進事實」。標題與內文一致，前輪 ⚠️ 已修好。✅
- 跨鏈推論的誠實處理：draft 明寫「『國防航太工業零件』不等同於『無人機零組件』，c077 直接支持的是『工具機是國防／航太零件母機』，『掏空工具機產能 → 侵蝕無人機長期製造基礎』這一步是結構性外推」。對 c077 Passage 5 核對（CNC 車床用途「國防航太工業零件加工」），draft 未把「國防航太」等同「無人機」— fidelity 模範。

**Counter-evidence check（L3）**：
- 前輪 senior consensus 的主缺口（B 鏈外銷證據遠薄於 A 鏈）：v2 補入 c030/c032/c033 三筆 qs4 B 鏈外銷來源，並明寫「這些摘要層來源彼此買方市場（波／德／捷）一致，使……相當穩固」，同時誠實標「個別成長倍數（749%／21 倍／10 倍）因統計口徑與基期不同而互有出入，須以方向一致、量級互證的方式並讀」。B/A 證據深度落差已縮小且被誠實揭露。
- Counter-evidence 段引 c074（程泰工具機本業轉盈 → 工具機外銷弱是相對且可能回升）與「accepted 集合對『無人機廠商西進中國』沒有一手案例」— 誠實。

**Overlooked sources（L4）**：
- c057/c058（DSET 台歐/對歐無人機合作、出口成長 40 倍）為前輪點名的同方向未引用 qs4 來源。v2 已補 c030/c032/c033 三筆，B 鏈外銷交叉佐證已足，c057/c058 不補不構成缺陷。
- c056（DSET《民主之翼》14 點藍圖，dset.tw 403）— B 鏈政策層核心智庫報告，draft 在 What we don't know 已標其 403 無法 deep-read。處理正確。

**Confidence calibration（L5）**：
- 宣稱「中」。A/B 對比由 qs=5 產業統計 + qs=4 報導支撐（高）；跨鏈「掏空無人機長期承諾」外推無單一來源直接證明（拉低整體）。標「中」正確。

**Suggested revision**：
- 無 — finding 成立。B 鏈標題與內文已一致，雙鏈未被 over-claim。

### Finding 5 — 西進的風險機制：中國長臂管轄、美國 BIS 鎖出、技術擴散三層

**Status**：⚠️ needs tightening

**Citations audit（L1）**：
- BIS/Entity List 機制由 c041（qs=5 deep-read，Federal Register 一手）+ c040（qs=5 gov，EAR 框架）支撐，【強證據】tier 正確。
- patch #1 查證 — c042（eCFR Part 744 法源）、c043（台灣戰略貨品名單）已補入 F5 第二段【爭議中】，皆附「依摘要層 sourcing，未經 deep-read 一手驗證」annotation，cap【爭議中】正確（per Dr3，摘要層證據 tier 上限【爭議中】，operator note #3 確認此為 by-design，非 tier 錯誤）。
- c011（技術擴散學術核心，tandfonline 403）正確 cap【爭議中】+「未經 deep-read」標示。
- 無 rejected cid（c023 未被引用）。

**Claim-vs-source fidelity（L2）**：
- 抽查 c041：「BIS 2025 年 3 月最終規則一次將 12 家實體加入 Entity List，其中 1 家位於台灣 Inspur Taiwan（新北市），管制強度全品項 + policy of denial」— c041 Passage 1/2 逐字確認。「Entity List 法律效果：受 EAR 管轄品項出口/再出口/境內移轉須額外許可、喪失多數例外」— c041 Passage 3 逐字確認。
- 抽查「工具機（尤其五軸加工中心）依 EAR 雙用途品項框架推論正屬此類典型品項」：c040 extract Passage 1 只有「EAR 管轄 dual-use items 與較不敏感軍品」的一般定義，**未逐字列出工具機/五軸**。前輪 Codex 建議改為「依 EAR dual-use 框架推論」。v2 draft 現明寫「依 EAR 雙用途品項框架推論正屬此類典型品項（c040 extract 取得的是 EAR/BIS 一般框架，未逐字列出工具機品項，此處為框架性推論而非條文直引）」— 已採前輪建議、誠實標示為框架推論。✅
- 抽查「上銀 2018 起對 5 家陸廠發明專利訴訟全勝、累計查處 126 家工廠 [c071]」：c071 extract 確認「2018 至今提告 5 家大陸廠商……均獲勝訴」「累計至 2024 已查處 126 家工廠」。draft 並誠實標「這是上銀『主動維權且勝訴』……不是上銀被中國長臂管轄綁定」— 證據方向描述精準。
- 抽查「瀧澤董事會因『中國大陸公司法修正』而須處理浙江孫公司減資與增資調整案 [c077]」：c077 Passage 4 逐字確認。draft 並明標此屬「公司法、非制裁法」面向 — 精準。

  **⚠️ 唯一新引入的精度問題（patch #1 副作用）**：F5 第二段【爭議中】把 c043 描述後接出的論述為——

  > 「換言之，『非紅供應鏈鎖出』這個議題對台灣廠商是**雙向**的：一方面台灣廠商可能因深度西進而觸及美方 EAR／Entity List 風險，另一方面台灣也有自己的戰略貨品管制制度需要遵循。」

  c043 的 why_relevant 與 INDEX line 55 描述 c043 為「台灣經濟部維護的戰略性高科技貨品出口管制名單……協助企業比對交易對象是否落入出口管制實體清單」——它是一份**供台灣出口商比對交易對手的合規工具清單**，本質是台灣作為**管制執行方**的制度。draft 用「台灣也有自己的戰略貨品管制制度需要遵循」描述大致成立（出口商確有遵循義務），但放在「『非紅供應鏈鎖出』對台灣廠商是雙向的」這個句子裡，語意會讓讀者誤推「台灣端管制也是一種對台灣廠商的『鎖出』風險」。實際上 c043 證據只支撐「台灣有自己的出口管制清單制度」，**不支撐**「台灣端管制構成台灣國防供應鏈廠商的西進鎖出風險」。這是把一個「制度存在」事實，輕微 framing 成與美方 Entity List 對稱的「風險」。屬措辭精度問題，非事實錯誤——draft 已 cap【爭議中】+ 摘要層 annotation，傷害有限，但「雙向鎖出」這個對稱修辭略過頭。

**Counter-evidence check（L3）**：
- patch #5 查證 — c015（Thomas Christensen「脫鉤亦有代價」）已補入 F5 新增【爭議中】段：「跨國的亞太生產分工長期以來是一股『和平的力量』，而過度脫鉤本身會帶來衝突風險」，並導出「政策上的正確問題不是『要不要與中國有任何生產關係』，而是『哪些品項、哪種國防關聯性的西進需要被管制』」。前輪三模型收斂指出的「F5 風險敘事單面」缺口已修好。✅
- grep accepted.jsonl「脫鉤」「decoupling」相關訊號：c015 是唯一一筆，draft 已引。無遺漏的 counter-evidence。

**Overlooked sources（L4）**：
- 前輪 Codex 點名 c036（中國反制不當域外管轄）較 c038/c039 更直接對應長臂管轄法制。查 accepted.jsonl：accepted 集合中**並無 c036**（c036 不在 c001–c080 的 accepted 範圍 / 未進 pool）— 此前輪 catch 在 v2 已無 actionable 對象，不再適用。draft 現引 c037/c038/c039 處理中國端長臂管轄法制，皆摘要層【爭議中】、tier 正確。
- c012（qs=5 摘要層，chokepoint economy 框架）為前輪 Claude 點名可作鎖出論述第二個學術錨點，減少對單一被封鎖 c011 的依賴。v2 在 Context 與 What we don't know 提及 c012 作 Q6 沾邊來源，但未在 F5 引為鎖出框架。屬可選 add，非缺陷（c041 一手 + c011 摘要層已足夠支撐機制層）。

**Confidence calibration（L5）**：
- 宣稱「中」。BIS Entity List 機制與法源由一手規則文本強力支撐（高）；「工具機西進後被鎖出」的產業個案屬 evidence gap、「技術擴散 → 中國軍力」核心連結屬摘要層（c011 被封鎖）— 整體標「中」正確。
- Q5 偷渡檢查（operator fair-game 點）：draft【專家意見】段明寫「accepted 集合**沒有**『某台灣工具機廠因西進中國而被 BIS／EAR 鎖出歐美訂單』的具名案例」，並用亞德客「深度西進卻沒有被鎖出問題（做氣動元件、非國防相關）」**界定風險適用邊界**，明確區分「機制存在」與「個案已發生」。**未從機制偷渡到個案。** ✅

**Suggested revision**：
- 把 F5 第二段「『非紅供應鏈鎖出』這個議題對台灣廠商是雙向的」收緊為「美方 Entity List 是對台灣廠商的西進鎖出風險；台灣端的戰略貨品管制清單（c043）則是台灣作為出口管制執行方的合規制度」—— 拆開「鎖出風險」與「台灣自身合規義務」兩件事，不要用「雙向鎖出」的對稱修辭把後者也染成風險。一句話可改，屬 minor edit。

## Structural issues（not tied to a single finding）

**Missing brief-question coverage（L6）**：無強制 brief 問題遺漏。Q1→F1 ✅、Q2→Context+F4 ✅、Q3→F2 ✅、Q5→F5 ✅、Q4（斟酌）分散於 F3/F4/Counter-framing(5) ✅。Q6（斟酌）— patch #6 已在 Context「斟酌題範圍說明」與 What we don't know 末項明寫「不展開 Q6 國際比較，是刻意取捨而非遺漏」，前輪 Claude/Gemini 共同點出的「Q6 靜默遺漏」已修好。✅

**Counter-framing engagement（6 框架）— ✅ solid**：六個 brief_expanded.yaml 宣告的 counter_framing 全部明確回應，tier 標示誠實（【爭議中】/【推測】）。框架(4)「工具機跟國防製造能力的連結是想像的」誠實承認「accepted 集合沒有『某工具機廠西進後直接削弱某國防專案』的具名個案」、把連結標【爭議中】而非【強證據】。框架(6)「藍白砍預算是程序問題」標【推測】、明說「評估牽涉預算審議程序的價值判斷，超出本稿產業結構分析範圍」— 守住 brief FAILURE MODE「不變成純政治批判」。無框架被遺漏或誤處理。

**Missed gaps in「What we don't know」（L7）**：9 項 gap 清單覆蓋誠實 — B 鏈無 MOPS 一手檔、Q5 無具名鎖出個案、Wassenaar/ECCN 條約層未 deep-read、c011 技術擴散僅摘要層、砍案→西進因果無法用現有財報驗證、已簽合約是否受影響未確認、c056（DSET 403）、南移缺量化、Q6 不在範圍。patch #5 的 Wassenaar gap 一行已落地。**未發現明顯遺漏的 gap。** access_blocked 來源（c011 tandfonline 403、c056 dset.tw 403）的信心衝擊在 What we don't know 與 F5 Confidence reasoning 都有明確承認。

**Access_blocked sources' impact**：c011（Q5 技術擴散核心學術源，tandfonline 403）、c056（Q2 非紅供應鏈核心智庫報告，dset.tw 403）— 兩者的缺席都在 What we don't know 明列、且 F5 Confidence reasoning 明寫「『技術擴散 → 中國軍力』的核心連結……屬摘要層證據，拉低整體 Confidence」。承認充分。

**L8 — skipped**：L8: skipped — Synthesizer skipped per M4, no themes.jsonl。本 project 無 `synthesize/themes.jsonl`、無 `evidence_scope_distribution`，依 reviewer.md L8 規格，concept-fidelity lens 不觸發。draft 正確未採用 Dr2 `**{scope}**` 段落標籤。（extracts front-matter 各帶 per-extract `evidence_scope`，但 L8 要求的是 themes.jsonl 層級的 `evidence_scope_distribution` — 不同物件，lens 仍不觸發。）

**Operator-note 合規（v2-specific，全部 clean）**：
- MOPS Track-4 一手財報（c071–c080）10 筆全部使用，未誤判「MOPS 缺席」。✅
- Synthesizer 依 M4 跳過 → draft 正確未採 Dr2 scope 標籤。✅
- 6 個新 cid（c042/c043/c015/c030/c032/c033）皆為 Dr3 secondary 層、皆 cap【爭議中】+「未經 deep-read 一手驗證」annotation，未誤放入【強證據】段 — 未誤判為 tier 錯誤。✅
- c050（亞德客 airtac.net URL 失效）— draft 正確引 c079/c080，未引 c050。✅
- c075（東台 partial 下載）— draft 與 c076 配對使用，未因 c075 缺西進敘述而推論東台無西進。✅
- 2026 Q1 MOPS 財報截至 2026-03-31 早於砍案 — F3 把「砍案→西進」定為壓力與條件，by-design 時序誠實，未誤判。✅

## Summary recommendations

本稿已達 🟢 publishable with minor edits。6 個 v1→v2 patch 全部落地，F1/F3/F4 三個前輪 ⚠️ 乾淨升 ✅，F5 patch 實質改善但留一個一句話可改的措辭精度問題。

1. **[唯一 ⚠️ — Finding 5] 收緊「雙向鎖出」措辭**：把「『非紅供應鏈鎖出』這個議題對台灣廠商是雙向的」改寫為拆開「美方 Entity List = 西進鎖出風險」與「台灣端戰略貨品管制清單（c043）= 台灣作為出口管制執行方的合規制度」兩件不同性質的事，不要用對稱修辭把台灣自身合規義務也染成「鎖出風險」。一句話可改。
2. **[可選 — Finding 1]** 若 operator 有餘裕，可補 c025（deep-read，無人機廠商第一人稱衝擊、單廠年產約 500 架）強化「內銷活水被砍」— 非必要，F1 現已 ✅。
3. **[可選 — Finding 5]** c012（qs=5 摘要層 chokepoint economy 框架）可作鎖出論述的第二個學術錨點，減少對被封鎖 c011 的單點依賴 — 非必要。

**Do NOT do**：不要把 c029（波蘭 6 成出口）、c030/c032/c033 等任何摘要層來源升格【強證據】— v2 已正確保留在【爭議中】，維持。

## Regeneration guidance（if needed）

本稿達 🟢 — **不需 revision pass，更不需 re-Drafter**。建議 1 為一句話 inline 修訂，operator 可直接改、或併入下次 patch。

- **Critical issues to feed back**：僅一項，且非 critical — F5「雙向鎖出」措辭收緊（建議 1）。其餘為 optional add。
- **Sources to prioritise deep-reading（若 operator 有資源，不阻擋發表）**：c011（tandfonline 403 — Q5 技術擴散核心學術源，目前僅摘要層）；c056（dset.tw 403 — Q2 非紅供應鏈 14 點政策藍圖）。兩者皆「補上加分、缺亦不阻擋」。
- **Brief questions that need rephrasing**：無。brief Q1–Q5 + 斟酌 Q4/Q6 結構健全；Q6 不展開是 draft 取捨（brief 已標斟酌），非 brief 缺陷。
