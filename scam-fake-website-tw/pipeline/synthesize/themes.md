# Synthesizer themes — scam-fake-website-tw

**Stage**: 4 (Synthesize) → 5 (Draft)
**Date**: 2026-05-21
**Input**: 20 deep-read/snippet extracts (extracts/) · brief_expanded.yaml keyword_expansions · brief.md Q1–Q7

研究問題:台灣詐騙中「假冒網域／假網站」佔多少比例 —— A(冒名型)與 B(非冒名型)拆開測量並對照。
pipeline 已確立「無單一官方數字」。本階段把 20 個 extract 編成 8 個主題,使 Drafter 能按 Q1–Q7
逐題三角測量,且 A、B **分開呈現不混合**。

## 統計總覽

- **主題數**: 8（t01–t08）
- **theme_type 分布**: evidence_cluster ×6（t01/t02/t03/t04/t07/t08）, regulatory_mechanism ×1（t05）, narrative_anchor ×1（t06）
- **extract 覆蓋**: 20/20 已指派至 ≥1 主題;unassigned = 0（0%,遠低於 30% 門檻）
- **brief Q 覆蓋**: Q1–Q7 全部 ≥1 主題;無 uncovered question
- **partial_counter_framing**: t06（real_platform_not_fake_site,scope-qualification + mechanism-inference rescue）
- **counter / primary balance**: counter=3（t06）/ primary=17 ≈ 1:5.7 —— 見下方說明
- **cluster_source 覆蓋**: metrics_vocab（t01/t07/t08）、synonyms（t02）、adjacent_concepts（t03/t04）、technical_jargon（t05）、counter_framings（t06）。未產出主題的 cluster:無（5 clusters 全部命中)。

## A vs B 的拆分原則（load-bearing）

brief 核心要求 A、B 各自佔比拆開測量並對照。主題結構保證 Drafter 能分開呈現:
- **A 型** 的規模證據集中在 **t02**（c023 moda 電商清單實測 ≈100% A、c050 數位信任協會冒名報告、c042 最常被仿冒名人）。
- **B 型** 的規模證據集中在 **t03**（c024 假投資博弈逐週序列、c030/c031/c032 法院認定自架自創品牌站）。
- **關鍵方法論發現**(t08):官方資料集 165027（c023）設計上可拆 A/B,但實測 1,466 列幾乎全為 A 型假冒電商
  —— **無任一官方來源同時涵蓋 A∪B 全集並按冒名軸拆分**。這本身是 t08 的 theme-worthy 發現,
  Drafter 不可給「一個共同分母下的 A/B 精確拆分」。

## counter / primary balance 說明

`brief_type.intent = surveillance` —— 依 Synthesizer 定義,surveillance brief 不強制 counter-framings
對稱拆分。但 brief 的失敗條件明列「忽略真平台假賣場／純 LINE 群組這個會稀釋假網站佔比的反面證據」,
故仍建立專屬 counter 主題 **t06** 並標 `partial_counter_framing`。

- counter 主題 extract 數 = 3（c034/c032/c051,t06）
- primary 主題 extract 數 = 17
- 比值 ≈ 1:5.7（primary 多於 counter）

依步驟 3,surveillance intent 下**不**因此 ratio 觸發 `balance_warning`(該規則僅對 comparative/exploratory
intent 生效)。但 Gatekeeper 已 flag:真正稀釋假網站佔比的需求端反證僅靠小型載重集（c034/c035/c059），
其中 c034/c032/c051 已 deep-read/snippet 進入 t06。Drafter 必須在「What we don't know / 攔阻 vs 受害
落差」明確 engage 此不對稱:**反面證據雖少但載重,不可因量少而埋沒;亦不可反向過度外推單一手法類別。**

---

## t01 — 為何沒有單一官方「假網站佔比」數字 —— 多分母方法論問題（C 軸根因）

- **theme_type**: evidence_cluster
- **cluster_source**: metrics_vocab
- **linked_brief_questions**: Q1
- **extracts**: c025, c027, c043, c044, c042, c047
- **tier_counts**: strong 2 / contested 2 / speculative 2

官方詐騙統計按「手法／類型」分類,「假網站」是橫跨多類型的「媒介／工具」,結構上不被獨立計數。
本主題彙整可用的多種分母(全般刑案 61.48 萬件 / 詐欺占 32.14% — c044;受理詐欺 19.8 萬件 — c043;
惡意連結中釣魚網站 30.52% — c047;moda 下架 122,119 中詐騙網站 1,621＝1.33% — c042)及各自佔比/區間,
並把「為何沒有單一數字」這個方法論問題本身講清楚。Drafter 應以此建立「多層分母、每層都標來源與限制」
的方法論骨架,直接回應 brief success criteria #1（至少 3 個不同分母的可引用佔比/區間）。

## t02 — A 型冒名規模與最常被冒名對象 —— 政府／金融／電商／物流／名人

- **theme_type**: evidence_cluster
- **cluster_source**: synonyms
- **linked_brief_questions**: Q2
- **extracts**: c023, c042, c050, c051, c031, c032
- **tier_counts**: strong 1 / contested 2 / speculative 3

A 型(冒名型假冒網域)的規模 proxy 與被冒名對象排序:moda 電商通報停止解析清單 1,466 列(c023)
實測幾乎 100% 為 A 型假冒電商(假冒類 1,068 + 偽冒電商 393),是 A 型假冒電商網域規模下界;
數位信任協會偵測「近萬個冒名詐騙網頁」(c050);moda「最常被仿冒公眾人物」前 20、元大銀行居首(c042)。
被冒名對象橫跨政府/國營、金融、電商、物流、電信、影視、零售與財經名人(c050/c051)。法院判決
(c031/c032)提供 typosquatting 一手實例(dowappbybit.com 冒 Bybit、假冒富邦/樂天銀行站)。

## t03 — B 型非冒名型詐騙網站規模 —— 自創品牌假投資／假博弈／假貸款站

- **theme_type**: evidence_cluster
- **cluster_source**: adjacent_concepts
- **linked_brief_questions**: Q3
- **extracts**: c024, c030, c031, c032
- **tier_counts**: strong 1 / contested 3

B 型(自創品牌、不冒充任何真實對象的詐騙網站)的規模 proxy:開放資料集 160055 假投資博弈網站
(c024)2021-2025 逐週序列,站次 2024 高峰 17,306、件數 36,755,是 B 型最乾淨的官方 proxy;
三份法院判決一手認定詐欺機房自架自創品牌站 —— c030（zsdsd/impvcu/highleve14dc 等 5 站）、
c031（亦莊國際/HOT/buysemu）、c032（信仲金融/安順/裕隆假貸款站）。**無官方來源同時涵蓋 A∪B
並按冒名軸拆分**,B 型只能以這組窄而純的 proxy 給規模量級,不可與 A 型放在同一分母下拆比例。

## t04 — 假網站在詐騙流程中的角色與生命週期 —— 導流路徑與快閃化

- **theme_type**: evidence_cluster
- **cluster_source**: adjacent_concepts
- **linked_brief_questions**: Q4
- **extracts**: c030, c031, c051, c023
- **tier_counts**: strong 1 / contested 2 / speculative 1

假網站在詐騙流程中的位置與生命週期:典型導流鏈為社群假廣告 → LINE 群組 → 假投資/假購物網站
註冊(c031/c051 三來源交叉確認);法院判決認定假投資網站「投資群組隨時更換」、機房同時持有多個
網域輪換(c030),A 型亦同(c031 同集團用 fswg./gyte. 兩近似網域)。假網站快閃化是其難以被穩定
計數成統計類別的結構性原因 —— c023 的「創建→停止解析」日期欄可量化存活時間,與趨勢科技
「96% 詐騙網站 24h 內消失」(載重外部數字,在 t07 經摘要層引用,須標 contested)互相印證。

## t05 — 供給端攔阻成效 —— TWNIC RPZ 停止解析、moda 下架、《詐欺犯罪危害防制條例》

- **theme_type**: regulatory_mechanism
- **cluster_source**: technical_jargon
- **linked_brief_questions**: Q5
- **extracts**: c022, c029, c037, c040, c041, c042, c061
- **tier_counts**: strong 4 / contested 2 / speculative 1

政府與基礎設施單位對假網站的攔阻/下架機制與規模。制度骨幹:《詐欺犯罪危害防制條例》第 42 條
(停止解析)、第 29-41 條(平台義務)、第 39 條(罰則,Meta 4 次 1,850 萬元裁罰依據)— c029。
執行量:TWNIC 2025 全年停止解析 79,039 個網域(c037);刑事局單一管道 4 個月停止解析 48,575 個
(c022);moda 累計下架 24.7 萬則、其中詐騙網站 1,621(c040/c042);PhishingCheck 2025 貢獻 2,822
件通報(c061)。**全是 supply-side 指標 —— Drafter 必須與 demand-side 受害佔比嚴格分開,不可混用,
這是 brief 的明確失敗條件之一。** 三套口徑(刑事局/moda/TWNIC)不可加總。

## t06 — 需求端稀釋反證 —— 真平台假帳號／純 LINE 群組詐騙不經獨立假網站

- **theme_type**: narrative_anchor
- **cluster_source**: counter_framings
- **linked_brief_questions**: Q4
- **extracts**: c034, c032, c051
- **tier_counts**: contested 2 / speculative 1
- **partial_counter_framing**: `true` — framing_id `real_platform_not_fake_site`
  - reason: scope qualification + mechanism inference — c034/c032 法院判決顯示「網購／物流解除設定」
    整類詐騙幾乎不用獨立假網站(真平台假客服話術);c051 顯示 A 型冒名貼文僅三條導流路徑之一通往
    假網站。counter-position 非缺席,但屬範圍限定／導流分流的 caveat-level 證據,非對立佔比數字。
- **conflict 標記**: c034 vs c031 —— 是否依賴獨立假網站,按手法類別分流(假投資高度依賴 / 網購物流
  幾乎不依賴),Drafter 須分層、不可外推單一比例。

brief 明令不可忽略的反面證據:相當一部分詐騙完全不經過獨立假網站。臺中地院 114審金易10(c034)
8 名被害人全部經真平台(蝦皮、DCView、臉書、Threads、新竹物流)假帳號／假客服受騙;高雄地院
114訴432(c032)同案 17 人中約 4-5 人為真平台假賣家路徑;數位信任協會報告(c051)指冒名貼文導流
終點僅約三分之一是假網站,另兩條是停留社群與進 LINE 群組。本主題是「假網站佔比」的反向錨點,
防止 Drafter 高估佔比 —— Drafter 應把它寫成 caveat / contested-tier 段落(辯論式),非主結論 Finding。

## t07 — 2023-2026 趨勢 —— 假投資站回落、A 型冒名電商網域續增、攔阻量級躍升

- **theme_type**: evidence_cluster
- **cluster_source**: metrics_vocab
- **linked_brief_questions**: Q6
- **extracts**: c023, c024, c037, c041, c042
- **tier_counts**: strong 4 / speculative 1
- **⚠ thin-cell flag**: Q6 是 pipeline 已知最薄的格。本主題的 5 個 extract tier 看似不弱,但趨勢
  並非來自現成趨勢報告 —— 全靠資料集逐年／逐週列三角導出(c023 創建日期 51→214→517→588;
  c024 站次年序 17,306→12,362;c037 RPZ 量級躍升)。c041/c042 的官方降幅主張(97%／94%)**基準期
  不明**。Drafter 須把趨勢標為「由縱貫資料列導出、非現成趨勢統計」,並把基準期不明的降幅主張
  分開處理、不可當受害率下降。

假網站詐騙的 2023-2026 縱貫變化:B 型假投資博弈站次 2022-2024 急升至 17,306、2025 回落至 12,362;
A 型假冒電商網域創建量 2022→2025 由 51 增至 588 後高原;TWNIC RPZ 攔阻量級由 2021-2022 年約千餘
躍升至 2025 年約 8 萬。三者方向一致(2025 假投資/冒充類偵測量回落),但 2025 回落須謹慎(可能是
真實下降,也可能是 160055 資料集 2026 起被 176455 取代、更新趨緩所致)。

## t08 — 資料缺口與替代估計法 —— 165 無媒介別交叉表、無單源覆蓋 A∪B

- **theme_type**: evidence_cluster
- **cluster_source**: metrics_vocab
- **linked_brief_questions**: Q7
- **extracts**: c027, c023, c025, c043
- **tier_counts**: strong 2 / contested 2
- **⚠ thin-cell flag**: Q7 亦薄,但部分屬本質性 —— 缺口本身就是發現。少數 extract 直接提出替代
  估計法;c027(嘉義市「管道」維度)是最具體的示例。Drafter 應把「替代估計法需要的不只是加欄位,
  而是加細粒度到媒介層」當作 Q7 的核心答案,並確認法務部調查局無公開假網站量化資料(Gatekeeper
  已 flag must_include_skipped)。

要回答「假網站佔比」台灣現行統計缺什麼:官方分類軸 100% 是「手法」、無「媒介別」交叉表(c025/c043);
即使有「管道」維度的資料集(c027 嘉義市)粒度也只到 channel 層(網路詐騙 89%)、切不出假網站;
無任一官方來源同時涵蓋 A∪B 全集並按冒名軸拆分(c023 實證 165027 偏 A 型電商)—— 「無單源覆蓋
A∪B」本身就是 brief 的核心方法論發現,須在 Q7 與「資料缺口」段明說。

---

## Drafter 交接備註

1. **A/B 分開呈現是硬要求**:t02(A)與 t03(B)分屬不同主題,Drafter 須維持分開的 Finding 與
   A vs B 對照表;t08 已把「無單源覆蓋 A∪B」釘為 theme-worthy 發現,Drafter 不可給單一共同分母下
   的精確 A/B 拆分。
2. **supply-side vs demand-side 不可混用**:t05 是純 supply-side(攔阻/下架量),t01/t06 含 demand-side
   視角;Drafter 須明確區分,這是 brief 失敗條件。
3. **partial_counter_framing(t06)**:寫成 caveat / contested-tier 段落,不寫成主結論;cross-reference
   counter_framing_keywords 的 real_platform_not_fake_site。
4. **thin cells(t07 Q6 / t08 Q7)**:證據薄已 flag —— Drafter 應在「What we don't know」surface
   為覆蓋缺口,不可 padding;基準期不明的官方降幅主張須分開標註。
5. **摘要層 sourcing**:c042/c047/c049/c050/c051 部分數字依摘要層／Wayback 救援,Drafter 引用須標
   contested tier 並註明 sourcing 層級(per Dr3)。
