# Review of defense-cut-supply-chain-pivot-tw insight_v1

**Reviewed on**: 2026-05-20
**Draft**: projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v1.md
**Sources consulted**: accepted.jsonl（79 records）、extracts/（19 deep-reads，含 10 MOPS 一手財報）、brief.md、brief_expanded.yaml、extracts/INDEX.md、rejected.jsonl（1 record）
**Review mode**: multi_model（Claude reviewer，review pass #1，無先前 baseline）

## Verdict

逐 Finding 一行狀態：

- Finding 1（4700 億砍掉本土軍工 + 非紅供應鏈財源）：✅ solid
- Finding 2（工具機聚落西進是已被一手財報坐實的結構性存量）：✅ solid
- Finding 3（「砍案 → 西進加速」目前只能說是壓力與條件）：✅ solid
- Finding 4（雙鏈差別待遇）：⚠️ needs tightening
- Finding 5（西進三層風險機制）：⚠️ needs tightening
- Counter-framing engagement（6 框架）：✅ solid
- What we don't know：✅ solid（但見 L7 一處漏列）

**Overall：🟢 publishable with minor edits**

這是一份證據紀律明顯高於 pipeline 平均水準的草稿。L1 citation 密度乾淨、L1 hard-error 零、摘要層 sourcing 標注一致、時序誠實（砍案 vs 財報截止日）嚴格遵守。沒有 🚨、沒有 ❌。兩個 ⚠️（Finding 4、Finding 5）都屬「收緊」而非「重寫」級別：一是 Finding 4 在 B 鏈一處措辭略微把「機制」講成接近「事實」，二是 Finding 5 漏引兩筆 qs=5 的 Q5 一手法源（c042/c043）。建議以一次輕量 revision pass 處理，不需 re-Drafter。

## Per-finding review

### Finding 1 — 被砍的 4700 億，砍掉的是「本土軍工 + 無人載具」，也砍掉了非紅供應鏈承諾的財源

**Status**: ✅ solid

**Citations audit（L1）**:
- 所有事實性子句皆有 cite。【強證據】段引 c019（qs=5 deep-read）、【爭議中】段引 c026/c022/c024 並明標「依摘要層 sourcing」。【爭議中】69.51 億合約段引 c049（deep-read）+ c047/c048（標摘要層）。citation 分層清楚。
- 無 orphan claim。無 over-claim：高信心子句（金額、預算結構）由 qs=5 deep-read c019 支撐，並有多筆摘要層交叉，符合 High 門檻。
- 無 cid 落在 rejected.jsonl（rejected 僅 c023，未被引用）。

**Claim-vs-source fidelity（L2）**:
- 「9000 億對外軍購 + 3000 億本土軍工 / 7800 億 / 62.4% / 4700 億落差 / 前 3000 億 FMS、後 4800 億愛國者三型」— 與 c019 Passage 1+3 逐字對齊（「約9,000億元用於對外軍購，其餘3,000億元將打造本土軍工產業鏈」「總金額匡列7,800億元」「占了…62.4%，兩者落差為4,700億元」）。無偏差。
- 「三大重點含『打造非紅供應鏈』」— 與 c019 Passage 2 逐字對齊（「加強台灣『不對稱戰力』、構築『台灣之盾』防空系統、打造『非紅供應鏈』」）。draft 由此推出「軍購案本身就是非紅供應鏈承諾的一部分」是合理的、被一手 framing 直接支撐的論述，非外掛價值判斷。fidelity 佳。
- 69.51 億合約四家得標廠（長榮航太、智飛、中光電智能機器人、神通）+ 履約至 2027/9 — 與 c049 Passage 1+2 對齊。

**Counter-evidence check（L3）**:
- draft 的 Counter-evidence 欄正確指出 counter-framing (6)「砍預算是程序問題」在 accepted 集合內無「實質無影響」的直接證據。
- **一處可補強**：accepted 集合內 c017（qs=4，「軍購砍後股市反應，雷虎跌逾 9%、NCSIST/神通/長榮航太/台船同跌」）是「砍案確有可量測的即時市場衝擊」的證據。它對 Finding 1「被砍 4700 億集中落在本土訂單上」是同向佐證（市場已 price in 對具名國防股的衝擊），draft 未引。這不是 counter-evidence 遺漏，而是「可加強的正向 demand-shock 證據」— 屬 L4 範疇，列在下方。L3 本身：無被遺漏的反向訊號。

**Overlooked sources（L4）**:
- c017（qs=4，股市對砍案反應，雷虎 -9%）與 c020（qs=4，3350 億無人機預算砍 + 台中 vs 嘉義聚落政治）— 兩筆 Q1 tagged、deep-read 未及，但摘要具名具數。c017 能把 Finding 1「內銷訂單衝擊」從「預算數字」推進到「市場已反映」；c020 能補「3350 億無人載具」砍項的具體政治脈絡。建議至少 c017 補引。非 cherry-pick 指控（draft 的 c049/c047/c048 已涵蓋內銷 pipeline），屬「可顯著加值的未用源」。

**Confidence calibration（L5）**:
- 宣告「高」。金額與預算結構由 qs=5 deep-read c019 + 多筆摘要層交叉，滿足 High（≥3 sources incl. qs≥4）。draft 同時自我降載「已簽合約是否受影響屬中等不確定」— calibration 精準，無 over-claim。

**Suggested revision**:
- 在【爭議中】69.51 億段或 Confidence 欄補引 c017（股市對砍案的即時反應），把「內銷衝擊」從預算面延伸到已可觀測的市場面。

### Finding 2 — 工具機聚落西進中國，是早於砍案、已被一手財報坐實的結構性存量

**Status**: ✅ solid

**Citations audit（L1）**:
- 五家公司（程泰、東台、瀧澤、上銀、亞德客）每一筆數字皆有 primary-doc cite（c073/c075/c076/c077/c078/c071/c072/c079/c080），全部為 deep-read 一手財報。c021（趨勢新聞）明標【爭議中】並說明「醞釀投資潮 ≠ 已實現投資統計」。citation 紀律優良。
- 無 orphan。Confidence「高」由 10 筆 MOPS deep-read 支撐，遠超 High 門檻。
- 無 rejected cid。

**Claim-vs-source fidelity（L2）**— 逐筆抽查：
- 程泰「五家 100% 持股子公司（蘇州、吳江、嘉興、上海）」、「亞崴機電(蘇州)與程泰機械(吳江)期末投資帳面價值各逾新台幣 5 億元」— c073 Passage 1：亞崴蘇州帳面值 555,606 仟元、程泰吳江 585,245 仟元，皆逾 5 億。✅
- 東台「蘇州東昱精機實收資本額約新台幣 8 億元、營業項目明載聯動數位控制機床…、期末投資帳面價值逾 10 億元」— c075 附表八：蘇州東昱實收 761,125、帳面 1,005,554；c076 附表七：實收 799,875、帳面 1,075,217。「約 8 億」與「逾 10 億」對兩個時點都成立。✅（draft 同時引 c075+c076 配對，正確）
- 瀧澤「中國孫公司瀧澤機電(浙江)…2026 Q1 帳面價值約新台幣 4.5 億元」— c078 附表四：瀧澤機電(浙江)期末帳面 452,620 仟元 ≈ 4.5 億。✅
- 上銀「中國上銀公司實收資本額人民幣 3 億元」「2026 Q1 累積匯往中國上銀公司約新台幣 15 億元、期末帳面價值 28.2 億元」「賣給中國上銀公司約 11 億元、佔合併營收 17%」「中國上銀公司 88% 進貨來自台灣母廠」— c072 Passage 1+2：累積匯出 NT$1,498,040 仟（≈15 億）、帳面 NT$2,820,985 仟（≈28.2 億）、銷貨 1,102,645 仟（≈11 億）佔合併營收 17%、進貨佔其 88%。**全部逐字對齊**。✅
- 亞德客「8 家全資子公司（2 製造 + 6 批發/智能裝備）」「期末對陸投資帳面金額合計約新台幣 378 億元（光寧波約 302 億元）」「功能性貨幣為人民幣」「94% 應收帳款集中中國」「2026 Q1 寧波帳面升至約 331 億元」— c079 Passage 1-3 + c080 Passage 1：寧波 FY2025 帳面 NT$30,223,795 仟（≈302 億）、八家合計約 378 億、功能性貨幣人民幣、94.42% 應收在中國；c080 寧波 2026 Q1 帳面 NT$33,121,984 仟（≈331 億）。✅。draft 亦正確區分亞德客為「精密機械／自動化元件廠而非 CNC 工具機整機」、且明標「亞德客非『軍購砍 → 西進』的案例…價值是 baseline illustration」— 完全符合 c079 scope_caveat 的指引，未 over-claim。
- **audited 五家公司共 ~15 個量化子句 against 8 個 MOPS extracts，found no divergence。** 這是本稿最紮實的一段。

**Counter-evidence check（L3）**:
- draft 的 Counter-evidence 欄主動引 c071（上銀風險段認知到的分散方向是「東歐＋東南亞」而非西進加碼）與 c077（瀧澤「低階機在中國、高階根留台灣」分層）— 與 extract 對齊（c071 structural note「東歐+東南亞」、c077 Passage 2 + caveat「分層」）。counter-evidence 處理誠實且精準，未被遺漏。

**Overlooked sources（L4）**:
- Q3 baseline 尚有多筆 see-also 級未用源：c066（qs=4「工具機出口成也中國敗也中國」）、c027（qs=3「65 家工具機廠赴上海搶單」）、c028（qs=3 友嘉 FFG 兩岸佈局）。draft 已有 10 筆 MOPS 一手檔 + c021，證據厚度足夠，不引這些 see-also 屬合理取捨，非 cherry-pick。不 flag。

**Confidence calibration（L5）**:
- 宣告「高」。10 筆一手財報 deep-read + c021 新聞獨立佐證，calibration 正確。

**Suggested revision**:
- none — finding holds。

### Finding 3 — 「軍購砍 → 西進加速」目前只能說是壓力與條件，不是已發生的事實

**Status**: ✅ solid

**Citations audit（L1）**:
- 每一事實子句有 cite。「2026 Q1 財報截至 2026-03-31」「程泰本期匯出全為 0」「瀧澤 2025-07-18 最新核准、2026 Q1 嘉善廠房興建中、認列投資利益約 3600 萬元」皆有 c074/c076/c078/c080 等 primary-doc 支撐。【專家意見】段的條件 (1) 引 c026 並標摘要層。citation 乾淨。
- 無 orphan。無 rejected cid。

**Claim-vs-source fidelity（L2）**:
- 「程泰五家中國子公司本期匯出／收回欄全為 0、無新增匯出」— c074 Passage 1 + caveat：「2026 Q1…台灣匯出累積投資金額（美元計）並無新增匯出 —『本期匯出/收回』欄全為 0」。✅
- 「瀧澤…2018 年投審會核准…2022、2025 年（最近一次 2025-07-18）持續追加核准，2026 Q1 浙江嘉善廠房仍在興建中、本季認列投資利益約新台幣 3600 萬元」— c078 Passage 2（註 5：107.02.22 / 111.04.13 / 114.07.18 核准）+ Passage 1（瀧澤機電浙江本季認列投資利益 36,308 仟元）+ Passage 3（嘉善廠房興建）。✅。draft 對「西進是動態累積進行式」的論述完全由 c078 的 caveat（「西進是動態、且 2025 年仍有新核准…延續至軍購砍案前夕的進行式」）背書。
- **時序誠實（operator note #6）**：draft 全段嚴守「財報截至 2026-03-31，早於 2026-05-08 砍案 → 財報拍不到砍案反應」，把「砍案 → 西進」定為條件性機率而非事實。【專家意見】段三條件 + Confidence「中」+ Counter-evidence（程泰本業轉盈、若景氣回升不一定急西進）構成完整的不確定性處理。**這正是 brief FAILURE MODE「把『軍購砍 → 西進』當必然結果」的反面**，Finding 3 把它做對了。

**Counter-evidence check（L3）**:
- Counter-evidence 欄引 c074（程泰工具機本業 2026 Q1 由鉅額虧損轉小幅獲利）+ c071（上銀美國曝險 < 3%）。c074 對齊 extract Passage 2（部門損益由 (982,854) 轉 30,191）。
- **L2/L5 邊際瑕疵（極輕微）**：「上銀美國曝險低於 3%」cite 為 [c071]，c071 原文是「銷售美國市場之比重低於 3%」— 此為 2024 年報口徑（c071 temporal range 2014-2025）。draft 把它放在「2026 Q1 工具機景氣有回穩跡象」的句子裡並列，讀者可能誤以為是 2026 Q1 數字。建議在該處註明此為上銀 2024 年報口徑、或改置於不暗示季度的位置。屬 nuance 級，不影響 Finding 結論。

**Overlooked sources（L4）**:
- 無關鍵遺漏。draft 已動用 c074/c076/c078/c080 四筆 2026 Q1 一手財報，正是論證時序限制最有力的證據組。✅

**Confidence calibration（L5）**:
- 宣告「中」。理由欄寫得精準：「西進是結構性存量且砍案前趨勢向上」由一手財報強力支撐，但「砍案 → 加速」受財報時序限制、本質前瞻 → 整體標中。完全符合 spec（「Low：unresolved；Medium：…」此處是「核心因果連結未解 + 前瞻」，標中而非高，calibration 正確且誠實，未 over-claim）。

**Suggested revision**:
- 將「上銀美國曝險低於 3% [c071]」標注為上銀 2024 年報口徑，避免與同句「2026 Q1」並讀產生時點混淆。

### Finding 4 — 雙鏈差別待遇：工具機外銷補不上、無人機整機外銷強勁但仍有西進壓力

**Status**: ⚠️ needs tightening

**Citations audit（L1）**:
- 工具機（A）段每一統計子句有 cite（c062 TAMI、c063 台中市府），皆 qs=5 deep-read。無人機（B）段引 c018（qs=4 deep-read）。【爭議中】段的「波蘭吸走 6 成出口」「電池稀土依賴中國」引 c029/c059 並標摘要層。【專家意見】跨鏈段引 c077 並自標【專家意見】。citation 分層清楚。
- 無 orphan。無 rejected cid。

**Claim-vs-source fidelity（L2）**:
- 「2025 年 1-8 月工具機總出口年減 7.7%、車床類年減 18.3%；對中出口佔比由 2021 年 32.2% 降至 2025 年 1-8 月 26.7%」— c062 Passage 1+2：總出口年減 7.7%、對中由 32.2% 降至 26.7%。✅。**「車床類年減 18.3%」需查**：c062 extract Passage 1 載「切削工具機…減少 8.9%」，未逐字載「車床 -18.3%」；但 INDEX.md c062 摘要明寫「車床類年減 18.3%」。此數字應來自 c062 PDF 內未抽進 extract 的表格 — fidelity 上可接受（INDEX 證實該數字出自 c062），但屬「extract 未涵蓋、靠 INDEX 佐證」的子句，嚴格上 Reviewer 無法以 extract 逐字驗證。建議 Drafter 確認該數字頁碼。
- 「輸美實質稅率 24.7%（MFN 4.7% + 對等 20%）…比日韓 15% 高近 10 個百分點…毛利率低於 20%」「台灣 70% 精密機械/工具機廠集中台中…2025/9 機械設備製造業 49 家次、1,357 人減班休息」— c063 Passage 1+2+3 逐字對齊。✅
- 「2025 無人機產業產值 129 億（年增逾 2.5 倍）、整機外銷成長 21 倍、外銷產值 29.5 億；2026 Q1 出口已超 2025 全年、洽談訂單破百億、36 國買方」— c018 Passage 1+2 逐字對齊。✅
- **【爭議中】B 鏈段一處措辭偏緊（核心 ⚠️）**：draft 寫「無人機整機的零組件仍依賴中國 —— DSET 指出台灣無人機國家隊雖 2025 年波蘭出口超過美國、年產目標 18 萬架，但電池與稀土仍依賴中國 [c059]」。c059 是 DSET FB 貼文、摘要層、qs=4，draft 已標「依摘要層 sourcing」— 這部分處理正確。但問題在 brief operator note：「B 鏈無 MOPS 一手檔，primary-doc 層 A 鏈 heavy，請審 Finding 4 雙鏈對比是否在 B 側 over-claim」。逐句檢視，draft 在 B 側**整體守得住**：【爭議中】段第一句明寫「『無人機外銷蓬勃』絕不等於『無人機鏈沒有西進壓力』」，第二句把零組件依賴定為「結構性」而非「已西進」。**唯一偏緊處**是【專家意見】跨鏈段的收尾：「無人機今天外銷蓬勃，不保證上游母機產能流失後，這條『非紅供應鏈』的長期承諾還站得住」— 這句本身有自標【專家意見】且寫「這條推論超出單一來源直接陳述、屬結構性外推」，誠實。但 Confidence 欄把整個 Finding 標「中」的理由之一就是這條外推 — calibration 因此是對的。結論：B 側**沒有從「機制」偷渡到「事實」**，但「電池與稀土仍依賴中國」這句單靠 c059 一筆摘要層 FB 貼文支撐，證據基礎偏薄，建議補一筆同向源（見 L4）。

**Counter-evidence check（L3）**:
- Counter-evidence 欄誠實寫「accepted 集合對『無人機廠商西進中國』沒有一手案例…『無人機鏈仍有西進壓力』主要靠零組件依賴與上下游邏輯推得，而非已觀察到的西進事實」— 這正是 operator note 要審的點，draft 主動自曝，未遮掩。✅
- **可補的 counter-evidence**：c015（qs=5 peer-reviewed，INDEX 明標為「decoupling-is-costly counter-evidence required for dual-chain balance」）論「跨國亞太生產是和平力量、脫鉤帶衝突風險」。這是雙鏈 framing 平衡所需的學術級 counter-evidence，draft 完全未引。Finding 4 與 Counter-framing engagement (2)（西進是商業合理性）都應觸及這個框架。屬 L3+L4 交界遺漏。

**Overlooked sources（L4）**:
- B 鏈外銷對沖的證據可顯著加厚：c030（qs=4「無人機外銷暴衝 749%、國內軍購 500 億同步」— 雙訊號 nuance）、c032（qs=4「波蘭最大買家、影響力不僅半導體」）、c033（qs=4「買方市場組合 波/德/捷」）、c057/c058（qs=4 think_tank，台歐無人機共同生產、對歐出口成長 40 倍）。draft B 鏈段目前**只靠 c018 一筆 deep-read + c029/c059 兩筆摘要層**，相對 A 鏈的 c062+c063 兩筆 qs=5 deep-read，B 側證據明顯單薄。這與 brief operator note「B 鏈無 MOPS 一手檔」是已知結構限制，但 c030/c032/c033/c057/c058 是 accepted 內現成、與 B 鏈直接相關的 qs=4 源，未用至少 1-2 筆屬可改進的覆蓋缺口。
- c015（qs=5，雙鏈平衡 counter-evidence）— 如 L3 所述。

**Confidence calibration（L5）**:
- 宣告「中」。理由欄精準：工具機外銷弱 / 無人機外銷強的對比由 qs=5 + qs=4 支撐（高），但「工具機西進掏空無人機長期承諾」跨鏈外推無單一來源直接證明 → 拉低整體至中。calibration 正確。**唯一建議**：B 鏈外銷段本身若補入 c030/c032/c033 等 qs=4 源後，「無人機外銷強」這半邊會更接近 High；目前 B 側只有 c018 一筆 deep-read，標「中」是合理的保守，但證據可加厚。

**Suggested revision**:
- B 鏈外銷段補引 c030/c032/c033 至少一筆 qs=4 源以平衡 A/B 證據厚度；「電池稀土依賴中國」若有第二筆同向源宜並引，避免單靠 c059 一筆摘要層 FB 貼文。

### Finding 5 — 西進的風險機制：中國長臂管轄、美國 BIS 鎖出、技術擴散三層

**Status**: ⚠️ needs tightening

**Citations audit（L1）**:
- BIS 段引 c041（qs=5 deep-read 一手規則文本）+ c040（qs=5 deep-read，EAR 框架）。長臂管轄段引 c077（一手財報側證）+ c039/c038/c037（皆標摘要層）。技術擴散段引 c071（一手）+ c011（標摘要層）。【專家意見】evidence-boundary 段引 c041/c061/c079。citation 分層清楚、摘要層標注一致。
- 無 orphan。無 rejected cid。
- **L1 觀察（非 error）**：c038（qs=3）、c037（qs=3）、c039（qs=4）— 長臂管轄第二層其中兩筆是 qs=3。draft 已全標【爭議中】+「依摘要層 sourcing」，tier 處理正確（Dr3 secondary capped at [contested]）。但「2025 年中國首次動用《阻斷辦法》反制」這個具體事實宣稱單靠 c039 一筆 qs=4 摘要層支撐 — 屬 single-source 摘要層，draft 已標【爭議中】，calibration 一致。

**Claim-vs-source fidelity（L2）**:
- 「BIS 2025 年 3 月最終規則一次將 12 家實體加入 Entity List，其中 1 家位於台灣 —— 新北市的 Inspur Taiwan（浪潮台灣），因其為中國浪潮集團子公司被連帶列管，管制強度『全品項』+『推定駁回』」— c041 Passage 1+2 逐字對齊（「adding 12 entities…China (11) and Taiwan (1)」「Inspur Taiwan…New Taipei City」「For all items subject to the EAR」「Policy of denial」「subsidiaries of…Inspur Group」）。✅
- 「Entity List 法律效果：一旦實體被列，任何受 EAR 管轄品項的出口、再出口、境內移轉都須額外許可、且喪失多數例外」— c041 Passage 3 對齊。✅
- 「EAR 管轄雙用途品項與較不敏感軍品的出口移轉」— c040 Passage 1 對齊。✅
- 「瀧澤董事會 113 年度因『中國大陸公司法修正』而須處理浙江孫公司的減資與增資調整案」— c077 Passage 4 逐字對齊。✅。draft 精準把這定位為「公司法、非制裁法面向」，與 c077 caveat 一致，未誇大為「瀧澤被長臂管轄」。
- 「上銀年報揭露在中國市場長期面對仿冒與專利侵權…2018 年起對 5 家陸廠的發明專利訴訟全勝、累計查處 126 家工廠」— c071 Passage 3 逐字對齊。✅。draft **主動加註**「須精準描述證據方向：這是上銀『主動維權且勝訴』…不是上銀被中國長臂管轄綁定」— 完全符合 c071 caveat「方向是上銀主動維權，非被中國長臂管轄綁定；Drafter 引用須精準描述其證據方向」。fidelity 模範。
- **c011 處理（operator note 指定重點審查）**：draft 寫「一份 qs=5 的同儕審查研究記錄了台灣資源流向 PLA 關聯的中國廠商、提升中國國防微電子能力的先例 [c011]（依摘要層 sourcing，未經 deep-read 一手驗證）…因 publisher 封鎖無法 deep-read，僅能以摘要層【爭議中】引用」。對照 INDEX.md c011（「tandfonline 403；摘要載明台灣資源流向 PLA 關聯陸廠提升中國國防微電子能力 — Q5 技術擴散先例，qs5 核心，摘要層 usable，Drafter 應顯著引用並標注未經 deep-read」）— draft 的處理**完全守住 Dr3 tier ceiling**：標【爭議中】、明寫「未經 deep-read 一手驗證」、明寫「依摘要層」、並在 What we don't know 第三點再次自曝「這條 Q5 核心論述只有摘要層證據」。tier 沒有滑出 [contested]。✅
- **【專家意見】evidence-boundary 段（operator note 指定重點審查 — Q5 個案是否從機制偷渡到事實）**：draft 寫「accepted 集合**沒有**『某台灣工具機廠因西進中國而被 BIS／EAR 鎖出歐美訂單』的具名案例：c041 的 Inspur Taiwan 是中資雲端公司、非工具機廠，c061 的『32 實體名單台灣一家上榜』也僅能示範『列管機制存在』」。逐句檢視 Finding 5 全段與 Counter-framing engagement，**沒有任何一處把「機制存在」寫成「個案已發生」**。draft 反而用亞德客（深度西進卻未被鎖出，因非國防、賣中國內需）來**界定風險的適用邊界**，並明寫「本 Finding 的正確讀法是『機制與法源已坐實、適用條件清楚，但對工具機產業的個案尚未在 accepted 證據中出現』」。這是 brief operator note 與 fair-game weak point #1 要審的核心 — **draft 守住了**。

**Counter-evidence check（L3）**:
- Counter-evidence 欄引 c079（亞德客深度西進數十年、EPS 42 元、未見被鎖出）並正確解讀為「鎖出風險有適用條件」。誠實。
- 無被遺漏的反向訊號。draft 對「風險是有條件的」這個 nuance 處理得比多數草稿細緻。

**Overlooked sources（L4）— 這是 Finding 5 的主要可改進點**:
- **c042（qs=5，primary_doc）未引**。INDEX.md 明確指引：「c042（eCFR Part 744 Entity List 現行法條文本）…Drafter 引 Q5 法源時可直接引 c042 URL + 摘要，並以 c041 extract 為機制說明主體」。Finding 5 BIS 段目前只引 c041（單一規則）+ c040（框架），**漏掉 Entity List 的現行 statutory text 一手法源**。brief PRIMARY 訴求 2 明列「EAR Entity List」為須具體呈現的機制 — 補引 c042 能把「機制」從「一次最終規則」升級到「現行法條」層級。
- **c043（qs=5，primary_doc）未引**。INDEX.md：「c043（台灣經濟部戰略性高科技貨品出口管制名單）…Drafter 可引以說明『台灣自身也有戰略貨品管制清單』」。brief Q5 明列「Wassenaar、EAR Entity List」並要求台灣端證據；draft Finding 5 完全是「美國 BIS + 中國反制」兩端，**漏掉台灣自身的戰略貨品管制這一層**。補引 c043 能讓 Q5 機制論述涵蓋台灣端。
- **c012（qs=5，peer_reviewed）未引**。why_relevant：「chokepoint-economy framing transfers to 工具機/無人機 lock-out exposure」— 是 Q5 鎖出論述的學術框架源。draft Finding 5 的學術源只有 c011（摘要層、被封鎖）。c012 雖也是摘要層，但能為「鎖出」提供第二個學術錨點，減輕 c011 單源的脆弱性。
- 綜合：Finding 5 是全稿 L4 缺口最明顯的一節 — 三筆 qs=5（c042/c043/c012）與 Q5 直接相關卻未用。其中 c042/c043 是 INDEX.md 明文指引 Drafter 該引的。這不是 cherry-pick（draft 無偏向性遺漏），而是「INDEX 指引的法源未落地」。

**Confidence calibration（L5）**:
- 宣告「中」。理由欄精準：BIS 機制與法源由一手規則文本強力支撐（高），但「工具機西進後被鎖出」的產業個案屬 evidence gap、「技術擴散 → 中國軍力」屬摘要層 → 拉低整體至中。calibration 正確且誠實。**補引 c042/c043 後**，「機制與法源」這半邊會更穩固，但因「個案 gap」仍在，整體標「中」仍恰當 — 不需改 Confidence 等級。

**Suggested revision**:
- BIS 段補引 c042（Entity List 現行 statutory text）作 Q5 法源、補引 c043（台灣戰略性高科技貨品管制名單）補上台灣端管制層；技術擴散段可並引 c012 為「鎖出/chokepoint」第二學術錨點。

## Structural issues（not tied to a single finding）

- **Missing brief-question coverage（L6）**：
  - Q1（軍購砍事實基底）→ Finding 1 ✅；Q2（工具機/無人機/買方市場界定）→ Context + Finding 4 ✅；Q3（西進歷史模式 baseline）→ Finding 2 ✅；Q5（長臂管轄 + 鎖出機制）→ Finding 5 ✅；Q4（廠商選擇空間，brief 標「斟酌」）→ Finding 3 + Finding 4 + Counter-framing (5) 分散涵蓋 ✅。
  - **Q6（國際比較：美、烏、以、韓如何處理本國國防製造業 vs 中國訂單）完全沒有 finding 涵蓋**。brief 把 Q6 標為「（斟酌）」optional，故這**不是必須修補的結構缺陷**；但 accepted 集合內有 c012（chokepoint economies 台/韓/日/荷）、c016（ally-shoring 經濟治國，qs=5）兩筆明確 tagged Q6 的源未用。建議：要麼在 What we don't know 補一條「Q6 國際比較未展開（屬 brief 斟酌題，本稿聚焦台灣產業結構）」明確交代範圍，要麼用 c012/c016 補一小段比較。目前 draft 對 Q6 是「靜默略過」，對「對外公開、一般大眾讀者」的成品，明說「本稿不處理 Q6」會比靜默更誠實。
- **Missed gaps in「What we don't know」（L7）**：
  - draft 的 What we don't know 七條覆蓋面佳（B 鏈無一手檔、Q5 個案缺、c011 摘要層、砍案→西進時序、已簽合約、c056 DSET 403、南移缺量化）。**唯一漏列**：Q6 國際比較未做（見 L6）。建議補一條。
  - access_blocked 源的處理：c011（tandfonline 403）、c056（dset.tw 403）、c050（airtac.net 404，已被 c079/c080 取代）— draft 在 What we don't know 明確點名 c011、c056 並說明對 confidence 的影響；c050 依 operator note #3 正確未引、未提（已 superseded）。**access_blocked 對 confidence 的衝擊已被充分承認**。✅
- **Operator note 合規檢查（v2 特有，確認未誤判）**：
  - MOPS Track-4 一手財報層（c071-c080）— draft 充分動用，未 flag「MOPS 缺席」。✅
  - Synthesizer 依 M4 跳過、無 themes.jsonl — draft 正確未採 Dr2 `**{scope}**` 標籤。✅
  - c050 已 superseded — draft 正確引 c079/c080、未引 c050。✅
  - c075 partial 下載 — draft 正確以「c075 缺西進敘述 ≠ 東台無西進」處理、配對 c076。✅
  - c079/c080 url 指向未存盤 PDF — 屬 archive 路徑瑕疵、非 citation 完整性問題，證據在 extract 內，不 flag。✅
  - 2026 Q1 財報早於砍案 — draft Finding 3 把「砍案→西進」定為壓力與條件，時序誠實，不 flag 為 hedge 缺陷。✅

- **L8（concept-fidelity）：skipped — Synthesizer skipped per M4, no themes.jsonl。** 本 project 無 `synthesize/themes.jsonl`、無 `evidence_scope_distribution`，draft 亦正確未採 Dr2 `**{scope}**` 段落標籤。依 reviewer.md L8 規格，本 lens 不觸發。（附帶觀察：extracts 的 front-matter 雖各自帶 `evidence_scope`，但 L8 要求的是 themes.jsonl 層的 `evidence_scope_distribution`，兩者不同 — L8 仍不觸發。）

## Summary recommendations

1. **Finding 5 補引 c042 + c043 兩筆 qs=5 一手法源**（最高優先）。INDEX.md 明文指引 Drafter 該引 c042（Entity List 現行 statutory text）作 Q5 法源、c043 補台灣端戰略貨品管制層；目前 Finding 5 的 Q5 機制只有美國 BIS + 中國反制兩端，漏掉台灣自身管制層，且法源僅靠單一最終規則 c041。這是 brief PRIMARY 訴求 2 的直接強化。
2. **Finding 4 B 鏈外銷段補 qs=4 源以平衡 A/B 證據厚度**。目前 B 鏈只靠 c018 一筆 deep-read + c029/c059 兩筆摘要層，相對 A 鏈兩筆 qs=5 deep-read 明顯單薄；accepted 內 c030/c032/c033/c057/c058 是現成 qs=4 B 鏈源，補 1-2 筆即可。
3. **補一條 What we don't know 交代 Q6 國際比較未做**，並可選擇性用 c012/c016 補一小段美韓以比較。Q6 雖為 brief 斟酌題，但對外公開成品「明說不處理」優於靜默略過。
4. （次要）Finding 1 補引 c017（股市對砍案即時反應，雷虎 -9%）把內銷衝擊延伸到可觀測市場面；Finding 3 將「上銀美國曝險 < 3% [c071]」標注為 2024 年報口徑避免時點混淆。

## Regeneration guidance（if needed）

本稿達 🟢 publishable with minor edits，**不需 re-Drafter**，建議由 operator 直接做一次輕量 revision pass 或交 Drafter 做 targeted patch（非全文重寫）：

- **Critical issues to feed back（patch 級，非重寫）**：
  1. Finding 5 補 c042/c043（INDEX 明文指引的 Q5 法源未落地）；
  2. Finding 4 B 鏈補 1-2 筆 qs=4 外銷源（c030/c032/c033 擇一二）；
  3. What we don't know 補 Q6 未涵蓋一條。
- **Sources to prioritise deep-reading（若操作者有資源）**：
  - c011（tandfonline 403）— Q5「技術擴散 → 中國軍力」核心學術源，目前只有摘要層，若補 deep-read 可把 Finding 5 技術擴散層從【爭議中】提升證據基礎；
  - c056（dset.tw 403）— Q2 非紅供應鏈 14 點政策藍圖，補後可讓「非紅供應鏈承諾」的政策路徑展開。
  - 兩者皆非阻擋 publish 的必要條件，屬「若有資源則加值」。
- **Brief questions that need rephrasing**：無。brief 的 Q1-Q5 + 斟酌 Q4/Q6 結構合理，draft 對 PRIMARY/SECONDARY success criteria 與 6 個 counter_framings 都有對應。Q6 被略過是 draft 取捨問題（brief 已標斟酌），非 brief 本身缺陷 — 不需改 brief。
