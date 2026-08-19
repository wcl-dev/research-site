# Review of defense-cut-supply-chain-pivot-tw insight_v1

**Reviewed on**: 2026-05-19
**Draft**: `./projects/defense-cut-supply-chain-pivot-tw/pipeline/draft/insight_v1.md`
**Sources consulted**: accepted.jsonl (72 records), extracts/ (23 deep-reads — c103, c130, c131, c132, c133, c134, c135, c136, c137, c138, c141, c142, c143, c145, c146, c150, c154, c155, c157, c158, c159, c170, c177), brief.md + brief_expanded.yaml + themes.jsonl (7 themes with evidence_scope_distribution)

## Verdict

- Finding 1（軍購砍案事實基底）: ✅ 大致 solid，唯 c131「3350 億」的編列邏輯敘述把 brief 觸發事件的 21 萬架 / 1320 艘編列邏輯與 c142 Hellscape 論述混合過密，建議將「依國防部論述」分離一層。
- Finding 2（A 軸工具機）: ⚠️ 需要 tightening — c159 量化錨堅實，但「機械公會理事長一人具名 9 家業者」其實是 8 家具名 + 莊大立自家共 9 家（draft 描述精確），c132 中「日本高階工具機銷大陸也持續成長」這個對比錨被 draft 省略，loss of nuance；另 Finding 2【強證據】#1 漏標 `temporal` scope，違反 Dr2 scope-tag contract。
- Finding 3（B 軸無人機）: ✅ 大致 solid，nuance 保留完整，但「c130 廠商匿名（新北市某無人機廠商董事長）揭年產 500 架軍用偵蒐無人機規模」是 c137 不是 c130 — 引用編號錯置。
- Finding 4（A∩B 雙鏈交集）: ⚠️ 需 tightening — c164/c174 在 accepted.jsonl **仍是 accepted 且摘要含具體 case（顧立雄確認、騰雲 / 銳鳶 II SD 模組、Singapore vendors → PRC 來源、商周 rebranding 模式）**，draft 將兩者完全踢出 evidence pool 並寫「沒有『台灣某 X 廠商整機被驗出含中國零件』的具體 case」是 over-pessimistic — 摘要層的 sourcing 可派生 partial claim（標 contested + caveat 即可）。這是本 review 最重要的一刀。
- Finding 5（長臂管轄）: ⚠️ 需 tightening — c151 摘要明文「BIS added 32 entities across China, India, Iran, Singapore, **Taiwan**, Turkey, UAE」直陳 Taiwan-domiciled 實體確有被列入 Entity List；draft「直接管轄已及於台灣 claim 因此無法成立」是 over-cautious，事實層面 Taiwan 已在列只是具名 entity 待 operator 核實。另外 c167 MOEA 77 工具機對俄管制（accepted 摘要明確的「Taiwan 鏡像 FDPR」實例）draft 全文未提，是 L4 overlooked source。
- Finding 6（三條 hedge 路徑）: ⚠️ 需 tightening — Finding 6 結語直接寫「P_south 證據基底最薄」邏輯成立，但 corpus 中 c003 / c007 / c008 / c017 / c122 / c123 / c129（南向 + GVC + 越南外派意願）被 INDEX 全部標 qs=3 background 沒 deep-read，這個 corpus bias caveat 雖在「Confidence」段有提，但 Finding 6 主文層的 hedge 不足 — 一般讀者會誤以為這是事實判斷而非 corpus limit。
- Counter-framing engagement: ✅ 6 條 framing 處理完整，#3 partial inferential 處理符合 Synthesizer t01 規範；唯 #3 寫「c114 / c115 / c117 SS landing 無 PDF、c165 gov.cn 404、c168 PwC 403 — 全部 fast-skip 或 access_blocked」省略了 c115 摘要本身已有「US long-arm + China countermeasures」的學術論述 sourcing，accepted.jsonl 摘要可作為 partial 補強。
- What we don't know: ✅ caveat 完整透明，唯第 3 點「c151 Federal Register 是否含台廠 pending」陳述跟 accepted 摘要事實落差 — 應改寫為「c151 摘要已揭含 Taiwan，具名實體待 operator 核實」。

**Overall**: 🟡 needs revision pass — 整體 narrative arc 與 PRIMARY/SECONDARY 訴求 coverage 完整，雙鏈 framing 通透、tier + scope tag 系統性套用、caveat 透明度高（Drafter 已主動把 c158 公司自述、c150 analogous mechanism、c143 烏克蘭橋接 三條自我預測攻擊面 explicit handled）。但**對 accepted.jsonl 摘要層 sourcing 的利用不足**（特別 c164 / c174 / c151 / c167 / c115）導致 Finding 4 / 5 過度 over-cautious、What we don't know 第 3 點事實層面與 corpus 落差。Revision 不需 re-Drafter，但建議：(a) 把 c164/c174 摘要派生為 Finding 4 的 contested-tier 補強 case；(b) 把 c151 摘要事實 ingest 進 Finding 5 / What we don't know #3 重寫；(c) Finding 3 引用編號 c130→c137 typo 修正；(d) 補 Finding 2 missing temporal scope。

---

## Per-finding review

### Finding 1 — 軍購砍案事實基底：4700 億不是均勻打擊
**Status**: ✅ solid

**Citations audit** (L1):
- 所有事實 claim 皆有 ≥1 cid，無 orphan。
- 高 confidence 段（【強證據】）有 c131 + c134 + c138 + c142 四 cid（包含 ≥1 qs=5 c134），滿足「≥3 sources incl. ≥1 qs≥4」門檻。
- 無 rejected.jsonl cid 引用。
- c142 在 Finding 1 引用為「依 Hellscape 不對稱作戰 + 反封鎖、需建置本土自製量能 國防部論述」— 但 c142 是 CNAS 美方智庫，**不是國防部論述**。Drafter 把 Hellscape 來源歸為「國防部」隱含偷渡，雖然國防部確有採納 Hellscape 框架（c134 報導者亦有提），但本句 sourcing 嚴格說應加 c134 而非單獨 c142。

**Claim-vs-source fidelity** (L2):
- c138 Passage 2「通過的部分均為對美軍購項目，但拿掉無人機商購及中科院委製等案。主要包括 AI 情報模組，部隊覺知套件（TAK）等。另包括中科院編列 361 億元的強弓飛彈量產案」→ draft「被排除的具體項目包含中科院編列 361 億的強弓飛彈量產案、TAK 部隊覺知套件、AI 情報模組、NCSIST 委製案、無人機商購等 [c138]」— **fidelity OK**。
- c130 Passage 3「藍白刪掉的無人機預算，將來台灣有事，就是讓台灣國軍以生命付出代價」「一旦缺乏穩定訂單，台灣無人機、無人船要在全球市場維持價格競爭力，將變得更加困難」→ draft「TechNews 直陳『一旦缺乏穩定訂單，台灣無人機、無人船要在全球市場維持價格競爭力，將變得更加困難』」— **fidelity OK**，且 draft 補充「TechNews 屬媒體分析語言、非業者財務模型」自我 caveat。
- c136 三位學者 Passage 1-3 → draft 三人具名引用 — **fidelity OK**。

**Counter-evidence honesty** (L3):
- c135「藍白共識：數字不是關鍵，有發價書就同意」+ c131 羅廷瑋自我矛盾 → draft 在【爭議中】段 explicit 對比，符合 t02 partial counter-framing rescue 規範。
- 唯 Drafter 寫「Drafter 不主張政治評價，但不可只引 c135 的程序立場而省略 c138 的剜除清單與 c131 的自相矛盾」— 這段是 review 角度自言自語（Drafter 對 Reviewer 預警），語體略 meta；general public 讀者讀來會困惑「為什麼一份對外文章在寫『Drafter 不主張』」。建議將 meta-review-aware 語句移至 「What we don't know」 段或刪除。

**Overlooked sources** (L4):
- c134 報導者「沈伯洋『有手有腳沒大腦』」金句、9000 億對美 + 3000 億本土的官方口徑分項在 Finding 1 內未 explicit 引用 — Finding 1 倚重 c131 / c138 但 c134 是 brief Q1 narrative anchor，draft 只在 Finding 1 cited c134 一次（「Hellscape 不對稱作戰 + 反封鎖」），可加強。

**Confidence calibration** (L5):
- declared high — 一手新聞 + 國防部官員回應 + 三位具名學者 + 即時股價，符合「≥3 sources incl. qs≥4」門檻。OK。

**L8 scope-tag audit**:
- 【強證據】#1 標 `{conceptual:A∪B; geographic:TW,US; methodological:news-reportage}` — themes.jsonl t03 evidence_scope_distribution `conceptual: {B:2, A∪B:5, counter-framing-6:1}, geographic: {TW:7, US:2}` — **claim_scope ⊆ theme distribution**, OK。
- 【強證據】#2（c130 股價）標 `{conceptual:A∪B; geographic:TW}` — t03 distribution 包含 — OK。
- 【爭議中】（c135 / c131）標 `{conceptual:A∪B; geographic:TW; methodological:news-reportage}` — OK。
- 【專家意見】（c136）標 `{conceptual:A∪B; geographic:TW; methodological:expert-opinion}` — t03 methodological 含 expert-opinion: 1，OK。
- **L8 結論：concept-fidelity 合格，無 scope overreach / disjoint。**

**Suggested revision**:
- 將「Drafter 不主張政治評價，但不可只引 c135 的程序立場而省略 c138 的剜除清單」這段 meta-review 語句移除或改寫為對讀者的中性陳述。Hellscape sourcing 加 c134。

---

### Finding 2 — A 軸：工具機西進壓力具結構性
**Status**: ⚠️ 需要 tightening

**Citations audit** (L1):
- 【強證據】#1 (c159 MOF) sourcing 充分；【強證據】#2 (c132) 業者具名動向 OK；【強證據】#3 (c158 FFG) OK。三段各依靠單一主 cid + 周邊補強，符合「≥3 sources incl. ≥1 qs≥4」門檻。
- 無 orphan claim。
- **L8 漏標 temporal**：【強證據】#1 標 `{conceptual:A; geographic:TW,CN,US,JP,DE; methodological:empirical-quantitative}` — t04 evidence_scope_distribution 有 `temporal: {2025-2026:1, 2024+:1, 2017-2025H1:1}`，但 draft 該段 scope tag **完全省略 temporal 軸**，違反 Dr2 contract「每個 paragraph 在 theme 提供 distribution 時須有完整 scope tag」。

**Claim-vs-source fidelity** (L2):
- c159 量化：「台灣工具機出口 2024 年跌至 US$22 億，僅為 2012 峰值 52%」「台灣從 2022 年第 5 跌至 2024 年第 8；2019→2024 期間，台灣工具機出口 -27.7%，中國 +90%」「對中國 + 香港 5 年累計 -16.8%」「同期對美 +24.5%」「2024 年美國佔比 24.2% 首次超越中港 23.7%」— **fidelity OK**，MOF 一手量化數字 draft 引用精確。
- c132 業者具名：「上銀、銀泰兩家生產滾珠螺桿及線性滑軌的傳動系統元件廠在大陸接單很好」「已在大陸設廠的台中精機、程泰、東台、友嘉集團、百德、瀧澤科、台灣麗馳等工具機廠」+「莊大立坦言其所屬大立機器… 正評估赴大陸設廠生產價格比較不具競爭力的機型」— **draft fidelity OK**。
- c132 中還有一句 draft 漏引：「這幾年大陸工具機生產品質提升，與台灣差距正逐漸拉近... 日本高階工具機銷大陸也持續成長」— 「日本高階工具機銷大陸持續成長」是 c132 提供的**重要對照錨**：顯示台商西進非孤例（區域共通現象），對 Drafter 在 Finding 6「南移東南亞證據薄」段落需要的「對美 friend-shoring 對沖也在發生」nuance 互補。draft 漏掉此句，是 evidence-set under-utilization。
- c158 friendly：「FFG has more than 40% of the market share of high-end machine tools in mainland China」+「among foreign-funded enterprises in mainland China」+「Xiaoshan Development Zone」 → draft 引用精確，且 explicit 標「公司自述未經 MOPS 一手驗證」caveat — fidelity OK。

**Counter-evidence honesty** (L3):
- draft「Counter-evidence」段已 explicit 「c159 同時顯示對美機械出口 5 年 +24.5%、首次超越中港 — 西進並非唯一方向」— honesty 高。
- 唯「不過 c159『機械』廣義含半導體設備，工具機本身對美增幅較弱；這是 nuance」— c159 extract 中**沒有**明確區分「機械廣義 vs 工具機本身對美增幅」的數據；Drafter 這句 nuance 屬合理推論但 sourceable 不完整。建議改寫為「c159 對美 24.5% 為機械全項統計，工具機 line item 細部對美增幅在原文中未獨立揭露」。

**Overlooked sources** (L4):
- c006 (peer reviewed, qs=4) — Hao Yuan 2024 *Making sense of the interaction between geopolitics and middle-technology trap: evidence from China's catching-up CNC machine tool industry* — 直接是「中國 CNC 工具機在美中出口管制下的 catch-up」學術評析；INDEX 標為 qs=4 academic depth-2 backlog 沒 deep-read。c006 的 abstract 已揭「Chinese CNC machine-tool industry significantly influenced by economic decoupling between China and the US」— 對 Finding 2 + 4 + 5 的橋接是有用的 academic anchor。Drafter 未利用、Segmenter 未升級到 depth-1，accepted 但未被 cited — **L4 overlooked relevant source**。
- c022 (qs=3) machine tool perspective — INDEX 標 background，但對 A 軸基底可能仍有 supporting；非高優先 overlooked。

**Confidence calibration** (L5):
- declared high — sourcing 充分；但 firm-level evidence 仍缺（MOPS pending），draft 已 explicit。Confidence 「high with caveat」是合理 calibration。

**L8 scope-tag audit**:
- 【強證據】#1 scope tag 缺 temporal 軸（如前述）— `missing_scope_tag` partial violation per Dr2 contract。
- 【強證據】#2 標 `{conceptual:A; geographic:TW,CN; methodological:news-reportage,primary-disclosure}` — t04 evidence_scope_distribution 含 `methodological: {news-reportage:1, primary-disclosure:1, empirical-quantitative:1}`，subset OK。
- 【強證據】#3 標 `{conceptual:A; geographic:TW,CN; methodological:primary-disclosure}` — OK。
- **L8 結論：subset 關係滿足，但【強證據】#1 漏 temporal tag = `missing_scope_tag`。**

**Suggested revision**:
- 補【強證據】#1 scope tag 中的 `temporal: 2019-2024` 或 `2024+`。
- 加引 c132「日本高階工具機銷大陸持續成長」對照錨。
- 改寫「不過 c159『機械』廣義含半導體設備…」為「c159 對美 24.5% 為機械全項，工具機 line item 對美增幅細部未獨立揭露」以匹配實際 extract 內容。

---

### Finding 3 — B 軸：無人機外銷對沖能量強，但波蘭 #2 vs 中國 #1 nuance 必須保留
**Status**: ✅ 大致 solid（一個引用編號錯置）

**Citations audit** (L1):
- 所有 factual claim 有 cid，無 orphan。
- 高 confidence 段 sourcing 充分（c133 + c145 + c146 + c155 + c157 + c170 跨 6 個獨立 sources）。
- **引用編號 typo**：第 4【強證據】末段「**c130 廠商匿名（新北市某無人機廠商董事長）揭年產 500 架軍用偵蒐無人機規模**，間接給出中型廠的訂單蒸發 baseline [c137]」— 第一個 c130 應為 c137（c137 是新北業者，c130 是 TechNews 股價）。中文敘述跟引用框 `[c137]` 對，但句中提到的「c130 廠商匿名」是 typo，應為「c137 廠商匿名」。

**Claim-vs-source fidelity** (L2):
- c133「整機外銷產值 +21 倍、外銷產值 29.5 億」「36 國採購方陸續與進駐亞創中心廠商洽商」「龔明鑫... 都希望與台灣合作，也有非紅供應鏈無人機產品的需求」— **fidelity OK**。
- c157「ranking second and fourth in Poland and Czechia respectively... China remained the leader」→ draft「波蘭排第 2、捷克排第 4，中國仍居首」— **fidelity OK**。
- c145「sells its drones at prices only 25 percent more than Chinese-made ones」 → draft「25% 成本溢價」— **fidelity OK**。
- c146「The company's plan to replace Chinese-made engines with Australian ones was found to be 20 times more expensive」→ draft「以澳洲引擎替代中國引擎，發現澳洲版貴 20 倍」— **fidelity OK**。
- c154「Marcin Jerzewski 對 Focus Taiwan 表態『台灣可在馬達、電池等 key components 供應，但需與國際夥伴更清楚協調』」— Drafter 進一步補「三個 hedge word（could / if / needed）顯示這是政策展望而非實績」— c154 extract Passage 1 確實有 `could`，但 `if` 和 `needed` 是否原文 verbatim 在我可見的 extract 中沒看到完整原句；建議 Drafter 自我審查這句 quotation strength（或弱化為「c154 措辭以 conditional 為主」）。

**Counter-evidence honesty** (L3):
- draft 顯式保留 c157 波蘭 #2 / 中國 #1、c145 + c146 成本溢價 + 20 倍零組件溢價 — counter-evidence 處理完整。

**Overlooked sources** (L4):
- c149 ArmyRecognition Taiwan drone — INDEX 標 depth-2 backlog 沒抓；可能補充廠商 + 機種 detail，但非關鍵 overlooked。
- 主要 sources 完整覆蓋，L4 clean。

**Confidence calibration** (L5):
- declared high — 跨 6 sources，符合門檻。OK。

**L8 scope-tag audit**:
- 【強證據】#1 標 `{conceptual:B,E; geographic:TW,US,EU,JP,IN,VN; methodological:news-reportage}` — t05 evidence_scope_distribution `conceptual:{B:8, E:5, A∩B:1}, geographic:{TW:8, US:5, EU:4, JP:1, IN:1, VN:1, CN:2, AU:1, LV:1, DE:1, PL:2, CZ:2, UA:2}` — subset 關係 OK。
- 【爭議中】標 `{conceptual:B,E; geographic:TW,EU,PL,CZ,UA; methodological:news-reportage}` — OK。
- 【強證據】#3 標 `{conceptual:B; geographic:TW,US,AU,LV; methodological:news-reportage}` — OK。
- 【強證據】#4 標 `{conceptual:B; geographic:TW,US; methodological:commentary}` — t05 methodological 含 `news-reportage:7, commentary:1`，subset OK。
- **L8 結論：concept-fidelity 合格。**

**Suggested revision**:
- 修第 4【強證據】末段「c130 廠商匿名」→「c137 廠商匿名」typo。
- 弱化 c154 hedge word 引用為「c154 措辭以 conditional 為主（could / would）」以避免 verbatim claim 越界。

---

### Finding 4 — 雙鏈交集（A∩B）：工具機西進掏空無人機長期承諾 + 紅供應鏈底層依賴
**Status**: ❌ 有 evidence gap（重大 — c164/c174 摘要 sourcing 未利用）

**Citations audit** (L1):
- 各段 sourcing 完整，無 orphan。
- 【強證據】#1 c143 引用精確；【強證據】#2 c155 + c145 引用精確；【爭議中】c131 引用精確；【強證據】#4 c142 引用精確。
- **無 rejected cid 引用**。

**Claim-vs-source fidelity** (L2):
- c143 Passage 3 「Every drone involved in the war in Ukraine depends on China. From palm-sized quadcopters... nearly every unmanned system... contains materials and components that originate in Chinese factories」→ draft 直接 verbatim 引述 — **fidelity OK**。
- c155 Passage 2「supply chains remain exposed to US export controls and, paradoxically, China-sourced battery materials and rare-earth magnets」→ draft「美方出口管制（上游）+ 中國電池材料 / 稀土磁鐵（下游原料）雙夾擊」— **fidelity OK**。
- c143 五大 chokepoints 中國份額：「90 percent of global sintered-magnet output」「two-thirds of the world's lithium」「more than seventy percent of its graphite anode material」→ draft「約 90% 全球燒結磁鐵產出、約 2/3 全球鋰加工、70%+ 石墨陽極材料」— **fidelity OK**。
- c142「Taiwan's drone industrial base is inhibited by high manufacturing costs due to the need for non-PRC supply chains, coupled with technological dependency on allies like the United States」→ draft verbatim — **fidelity OK**。

**Counter-evidence honesty** (L3):
- draft 已 explicit「在地化故事真實發生（c146 Taiwan UAV、c177 AIDC-Shield AI、c145 Thunder Tiger Blue UAS）— 並非『都失敗』」— L3 honest。

**Overlooked sources** (L4) — **本 review 最重要的一刀**：
- **c164 (newtalk 驟雲 / 銳鳶 PRC 零件)** 在 accepted.jsonl 內 quality_score=5、verdict=accept。Accepted 摘要明文：「Whistleblower revealed NCSIST 騰雲 (Tengyun) and 銳鳶 II (Ruiyu II) UAVs contained PRC-made network chips + removable SD modules. Suppliers reportedly sourced via Singapore vendors but parts originated in China. **MND Defense Minister 顧立雄 confirmed discovery during acceptance testing**; manufacturers ordered to replace.」 — 這就是「台灣某 X 廠商整機被驗出含中國零件」的具體 case！且**部長層級具名確認**，sourcing 質量極高。Drafter 因「URL 失效」直接放棄該 cid 並寫「Finding 4 主要靠 c143 烏克蘭結構性陳述 + c145 / c155 結構性數字撐起，**沒有『台灣某 X 廠商整機被驗出含中國零件』的具體 case**」是 over-pessimistic — 即使原文 URL 失效，accepted 摘要本身（已通過 Gatekeeper 驗證並進 corpus）可派生 contested-tier 補強 claim。建議 Drafter 在 Finding 4 加一段「【爭議中】**{conceptual:A∩B,B; geographic:TW; methodological:news-reportage}** 2024-09 國防部長顧立雄具名確認 NCSIST 騰雲 / 銳鳶 II 無人機在驗收測試中被發現含中國製網路晶片與 SD 模組（透過新加坡供應商繞道採購），廠商被要求更換 [c164 摘要派生；原 URL 失效，sourcing 限於 accepted.jsonl 摘要層]」。
- **c174 (BusinessWeekly UAV rebranded-PRC)** 同樣 quality_score=5、verdict=accept。Accepted 摘要：「Reports Taiwan drone bidders 'rebranding' Chinese OEM products as Taiwanese to satisfy non-red procurement requirements」— 這是「rebranding 為非紅」的系統性 mechanism whistleblower。同樣可作為 contested-tier sourcing 派生 claim。
- **c167 (MOEA 77 工具機對俄管制)** quality_score=5、verdict=accept。Accepted 摘要：「Since March 2024, Taiwan's MOEA Trade Administration added export restrictions on 77 machine tool categories destined for Russia and Belarus (mirroring US FDPR). **Demonstrates the operational mechanism by which FDPR cascades into Taiwan trade-control practice**」— 這是 Finding 5 / Finding 4 的「FDPR → Taiwan trade-control」**台灣本土實例 mechanism**，比 Haas 案還 directly relevant。INDEX 標 c167 「內容錯誤」fast-skip，但 accepted 摘要已是 Gatekeeper 驗證後的 sourcing，至少可作為「regulatory mechanism」partial reference。draft 全文未提，是 L4 overlooked。
- c143 + c155 + c142 + c131 + c145 五個 deep-read sources 處理完整，但**錯失三個 accepted-snippet sources 對 brief「非紅供應鏈宣稱 vs 實況落差」topic 的具體填補**，是 Finding 4 weight 不足的主因。

**Confidence calibration** (L5):
- declared medium — 由於缺一手台灣 case，medium 是 calibration 合理；但 **c164/c174 摘要派生後，Finding 4 可從 medium 升 medium-high**（具體台灣 case 已有，雖 sourcing 限於 accepted-snippet 而非 deep-read）。

**L8 scope-tag audit**:
- 【強證據】#1 標 `{conceptual:A∩B,B; geographic:global,CN,TW,US,DE; methodological:commentary}` — t06 evidence_scope_distribution `conceptual:{A∪B:1, B:3, E:1, A∩B:1}, geographic:{TW:3, global:1, CN:3, US:2, DE:1}` — claim_scope `geographic:{global, CN, TW, US, DE}` ⊆ theme distribution OK。
- 【強證據】#2 標 `{conceptual:B,A∩B; geographic:TW,US,DE,CN; methodological:news-reportage}` — OK。
- 【爭議中】（c131）標 `{conceptual:A∪B; geographic:TW; methodological:news-reportage}` — t06 distribution 含 A∪B:1，OK。
- 【強證據】#4 標 `{conceptual:B; geographic:TW,US; methodological:commentary}` — OK。
- **L8 結論：concept-fidelity 合格，未見 scope overreach。**

**Suggested revision**:
- **【重大】補一段【爭議中】tier 段落，將 c164（顧立雄具名 + NCSIST 騰雲/銳鳶 II PRC 零件）+ c174（BusinessWeekly rebranding 模式）以「sourcing 限於 accepted.jsonl 摘要層、原 URL 失效」caveat 派生 — 這是 Finding 4 + brief SECONDARY #4「非紅供應鏈宣稱 vs 實況落差」最具體的台灣 case anchor，不該因 URL 失效就完全踢出。**
- 同時 What we don't know #2 從「c164 / c174 URL 失效 — 具體個案 anchor 缺位」改寫為「c164 / c174 URL 失效，僅能引摘要層 sourcing；具名實體驗收測試的細節（哪一架次、哪一供應商）仍 pending」。

---

### Finding 5 — 長臂管轄 + 非紅供應鏈鎖出機制
**Status**: ⚠️ 需 tightening（c151 摘要事實層落差 + c167 overlooked）

**Citations audit** (L1):
- 各段 sourcing 完整、無 orphan。
- 【強證據】#1 (c103 法律機制) + 【強證據】#2 (c150 Haas) + 【強證據】#3 (c141) + 【強證據】#4 (c142) 構成法律 + 執法 + 戰略三層證據鏈。
- 高 confidence sourcing 充分。

**Claim-vs-source fidelity** (L2):
- c103 Passage 2 + 3 + 4 + 5 FDPR / Footnote 4 / Huawei / 2022 半導體 destination-based 規則 → draft 引用精確 — **fidelity OK**。draft 寫「**要件由『specific entity』降到『knowledge』**」對應 c103「The amended rule no longer required... Instead, a license requirement was imposed... when there is knowledge」— fidelity OK。
- c150 Passage 1「41 violations... six Chinese entities and two Russian entities on the BIS Entity List」+ Passage 2「$2.5 Million... January 17」+ Passage 5「computer numerical control (CNC) vertical and horizontal machining centers and CNC lathes」→ draft 引用精確 — **fidelity OK**。
- **claim-fidelity 高度**；Drafter 對 c150 自我預測攻擊面「Haas 是美國母公司、非台灣 case」已 explicit 在【強證據】#2 末段 caveat handle：「雖然 Haas 是美國母公司，與『台灣母公司 → 中國子公司』結構不完全等價，但 c150 揭露的關鍵法律重點是：CNC 工具機在 EAR 分類雖為 EAR99... 只要客戶為 Entity List 上實體，仍須申照」— L2 attack surface 已 self-defused。
- c143 對台灣的延伸（Drafter 自我預測攻擊面 (c)）：draft 在 Finding 4 寫「c143 中... 連被視為非紅典範的烏克蘭戰場，每架無人機仍仰賴中國組件」— c143 確實全文未具名台灣（extract scope_caveat 明標「文章本身未提台灣 — Drafter 引用時用作『全球無人機供應鏈中國份額』基底數字」），但 draft 把它用作「全球基底」而非「對台論述」— fidelity OK。

**Counter-evidence honesty** (L3):
- draft「Counter-evidence」段已 explicit「c150 Haas 案是美國母公司直接出貨給 Entity List 客戶，與台灣廠商西進結構不完全等價」— L3 honesty 高。

**Overlooked sources** (L4) — **重大**：
- **c151 (Federal Register Sep 2025 Entity List)** 在 accepted.jsonl 摘要明文：「BIS added **32 entities across China, India, Iran, Singapore, Taiwan, Turkey, UAE**. Federal Register URL redirected to unblock page (some access friction). Operator TODO: fetch the unredirected federal register PDF and identify which entries are Taiwan-based, to verify whether any Taiwan-domiciled firm has been Entity-Listed」 — **摘要層已直陳「Taiwan-domiciled 實體已在 Sep 2025 Entity List」事實**，只是具名 entity 仍待 operator 核實 PDF。draft 在【強證據】#1 + What we don't know #3 寫「對台灣具體廠商的直接管轄 / 列管尚未一手出現（c151 Federal Register 2025-09 Entity List 是否含台廠 pending operator follow-up）」、「直接管轄已及於台灣 claim 因此無法成立；現階段全部以『analogous mechanism』橋接論述」— **這跟 accepted 摘要事實落差**。Drafter 應改寫為「c151 摘要已揭 32 家中含 Taiwan-domiciled 實體，具名 entity 待 operator 核實 PDF；『直接管轄已及於台灣』是 partial established fact，只是具名 case 細節 pending」。
- **c167 (MOEA 77 工具機對俄管制)** — 如 Finding 4 L4 catch 中所述，accepted 摘要明文「Taiwan 鏡像 FDPR 對工具機的實例」是 Finding 5「FDPR → Taiwan trade-control practice」的**最 directly relevant** 台灣本土實例。INDEX 標「內容錯誤 fast-skip」但摘要層 sourcing 可派生 partial claim。Drafter 全文未提，是 L4 overlooked。
- **c099 (October 2022 US export controls on China chips — peer-reviewed, qs=4)** — accepted 但 INDEX depth-2 backlog 未 deep-read。c099 是 2022 規則的學術評析，可補強 c103 同事件的學術視角。非高優先 overlooked，但若 Drafter 要強化 Finding 5 的學術 sourcing 可補。
- **c115 (US Long-Arm Jurisdiction + China's Countermeasures, qs=5)** — Drafter 在 Counter-framing #3 段寫「c114 / c115 / c117 SS landing 無 PDF... 全部 fast-skip 或 access_blocked」— 但 c115 accepted 摘要「**US long-arm jurisdiction has evolved from a system tool for resolving domestic interstate judicial disputes to a core means of maintaining global hegemony and containing strategic rivals**... fill the research gap on the coordinated countermeasures of the state and enterprises and the response strategies」— 摘要本身已是「US 長臂 vs China 反制」直接論述 sourcing，至少可作為「該議題學術文獻存在」partial signal，不該完全踢出。

**Confidence calibration** (L5):
- declared medium — 「對台灣具體廠商的直接管轄 / 列管尚未一手出現」是 calibration 的依據；但 c151 摘要已揭 Taiwan 在列，**confidence 應升 medium-high**（雖然具名實體未到位，但「直接管轄已及於台灣」這個 categorical claim 由 partial-fact 派生）。

**L8 scope-tag audit**:
- 【強證據】#1 (c103) 標 `{conceptual:counter-framing-3,A; geographic:US,global; methodological:empirical-qualitative}` — t07 evidence_scope_distribution `conceptual:{counter-framing-3:1, B:3, E:1, A:1}, geographic:{US:4, global:3, TW:1, CN:2, RU:1}, methodological:{empirical-qualitative:1, commentary:3, primary-doc:1}` — subset OK。
- 【強證據】#2 (c150) 標 `{conceptual:A; geographic:US,CN,RU; methodological:primary-doc}` — OK。
- 【強證據】#3 (c141) 標 `{conceptual:B,E; geographic:US,global; methodological:commentary}` — OK。
- 【強證據】#4 (c142) 標 `{conceptual:B; geographic:TW,US; methodological:commentary}` — OK。
- **L8 結論：concept-fidelity 合格。**

**Suggested revision**:
- **【重大】改寫 What we don't know #3 + Finding 5 Confidence 段：c151 摘要已揭 Taiwan-domiciled 實體在 Sep 2025 Entity List 32 家中；「直接管轄已及於台灣」是 partial established fact，具名 entity 細節 pending。**
- 將 c167 摘要事實納入 Finding 5 作為「Taiwan 鏡像 FDPR 對工具機」本土實例 mechanism reference（caveat：原 URL 內容錯誤，sourcing 限於 accepted 摘要層）。
- Counter-framing #3 段重述 c115 摘要層 sourcing 為「該議題學術文獻存在但無 open access PDF」而非完全踢出。

---

### Finding 6 — 三條 hedge 路徑的差異化盤點
**Status**: ⚠️ 需 tightening

**Citations audit** (L1):
- 各 hedge 路徑的 sourcing 列表完整；P_west 多 cid 交叉；外銷對沖多 cid 交叉；P_south 只引 c133 + c177 + 點名「c169 access_blocked」— sourcing 不足但這正是 Drafter 想表達的「證據基底最薄」論點。
- 「Drafter 不能寫『南移是替代主軸』— 證據基底不夠」— 這是 honest framing。

**Claim-vs-source fidelity** (L2):
- 各段引用無 over-claim。
- c137 廠商匿名「全世界都加強不對稱作戰…立法院真的不能去擋這筆預算」+「即使沒有國防安全問題，無人機仍可廣泛運用在民生需求」→ Drafter 推「軍方訂單缺失 → 民生市場部分對沖」屬合理 inference，且 explicit 標「廠商個別 trade-off 的 firm-level evidence 在本研究中缺位（MOPS 一手財報 pending）」— L2 honesty 高。

**Counter-evidence honesty** (L3):
- 「Counter-evidence: c159 MOF 對美機械出口 5 年 +24.5%、首次超越中港 — friend-shoring 對美對沖在『機械』廣義層面已具量化證據」— L3 OK。

**Overlooked sources** (L4):
- c003 (Industrial policy GVC), c007 (BRI MIC2025 SE Asia), c008 (industrial upgrading TW), c017 (台商 IT 電子業時空), c060 (TW-CN trade interdep), c067 (TW strategic importance), c109 (weaponization trade barrier TW-CN), c118 (NSP flagship soft power), c122 (新南向 HR), c123 (新南向 cross-strait), c129 (越南外派意願) — 這 11 個 cid 在 accepted.jsonl 中 verdict=accept，但 INDEX 標為 qs=3 background 沒 deep-read 或 qs=4 depth-2 backlog 沒 deep-read。**P_south「證據基底最薄」這個結論很可能不是 ground truth、而是 corpus-curation bias（Segmenter prioritise 軍購 + A/B 軸；南向 cluster 被 down-prioritise）**。Drafter 在 Finding 6「Confidence」段確有 explicit「『P_south 弱』可能反映 corpus bias（南向辦公室統計 c169 access_blocked）而非真實 hedge 結構」 — 已 honest，但 Finding 6 主文層讀者讀來會誤以為這是事實判斷。建議將「Drafter 不能寫『南移是替代主軸』」改寫為「在本研究 deep-read corpus 中無法支持『南移是替代主軸』，corpus 中相關 qs=3 background sources（c003 / c007 / c122 / c123 / c129）未進 deep-read budget — 此判斷的 evidence 基底是 corpus curation 決定」。

**Confidence calibration** (L5):
- declared medium — 對 P_west / 外銷對沖部分 medium 偏低（c132 + c158 + c159 + c133 + c145 sourcing 充分支持 high）；對 P_south 部分 medium 偏高（evidence 真的太薄）。Aggregation 為 medium 是合理 compromise。

**L8 scope-tag audit**:
- 【強證據】標 `{conceptual:A∪B; geographic:TW,CN; methodological:empirical-quantitative,news-reportage}` — Finding 6 cross-cuts multiple themes（t04 + t05 + t06 + t03）；其 evidence_scope_distribution 各 theme 不一致。Drafter 選 `A∪B` 是合理 union 處理。
- 【爭議中】（c137）標 `{conceptual:B; geographic:TW; methodological:news-reportage}` — t05 distribution 含，OK。
- **L8 結論：concept-fidelity 合格，但 Finding 6 inherently cross-theme，scope tag 力度自然較弱（是 structural 問題非 Drafter 缺失）。**

**Suggested revision**:
- 將 P_south 判斷重述為「在本研究 deep-read corpus 中 evidence 不足以支持 P_south 主軸；qs=3 background sources（c003 / c007 / c122 / c123 / c129）未進 deep-read budget，是 corpus curation 決定而非事實結論」。Finding 6 主文層提此 nuance，不要只在 Confidence 段提。

---

## Structural issues (not tied to a single finding)

### Missing brief-question coverage (L6)
- **Q1 ✅** 軍購案事實基底 — Finding 1 全覆蓋。
- **Q2 ✅** 工具機（A）+ 無人機相關（B）+ 無人機買方（E）界定 — Finding 2 / 3 / 4 全覆蓋。
- **Q3 ✅** 西進承接中國資金的歷史模式 — Finding 2（c132 + c158 + c159 三角錨）。
- **Q4 ✅**（斟酌）廠商實際選擇空間 — Finding 6 + c137 inference 處理，但 firm-level evidence 缺已 explicit caveat。
- **Q5 ✅** 長臂管轄 + 非紅供應鏈鎖出機制 — Finding 5 全覆蓋。
- **Q6 ⚠️**（斟酌）國際比較 — draft「What we don't know #4」explicit 標「scope-by-design 缺位」，符合 brief 斟酌題定位。OK。
- **brief 結論：Q1-Q5 全覆蓋，Q6 斟酌題 explicit 缺位。No structural gap.**

### Missed gaps in "What we don't know" (L7)
- 第 3 點 c151 Entity List 陳述跟 accepted 摘要事實落差（如 Finding 5 L4 catch）— 需重寫。
- 第 2 點 c164/c174 URL 失效 — 摘要層 sourcing 可派生（如 Finding 4 L4 catch）— 需重寫。
- **未列的 gaps**：(a) c167 MOEA 77 工具機對俄管制摘要可作為 Taiwan FDPR mechanism partial reference，未提；(b) Q6 國際比較雖標 scope-by-design 缺位，但 c142 / c143 / c155 等智庫報告其實提供片段比較（美國 export-control 制度 + CSIS Five Materials 同盟政策建議 + Asia Times 美德雙重技術夥伴）— 可在 What we don't know 段補「片段比較 sourcing 散在 c142/c143/c155 但無 dedicated comparison study」。
- access_blocked sources（c114/c115/c117/c161/c162/c163/c164/c165/c166/c167/c168/c171/c173/c174/c144/c148/c156/c178/c179/c153/c147/c152/c149/c172/c169/c176 — 共 26 cid）的影響在 draft 中**整體匯總**處理（What we don't know #1, #2, #3 涵蓋 MOPS + c164/c174 + c151），算合格但稍籠統 — 一般讀者讀來會難以區分「真的事實 unknown」vs「accept 但 deep-read 不足」。

### Access-blocked sources' impact acknowledged?
- ✅ MOPS（c139）+ c164/c174 + c151 + c169 南向辦公室 都有 explicit 提及；
- ⚠️ c167 MOEA 77 工具機（內容錯誤而非 access_blocked，但同等影響）draft 未提；
- ✅ c114/c115/c117 學術 SS landing 在 Counter-framing #3 explicit 提；
- ✅ Operator TODO list 完整（What we don't know #6「補立法院公報 KMT 立委質詢全文 + 親藍智庫對軍購效率的評析」）— 透明度高。

### Multi-model reviewer self-positioning (review.mode caveat)
- Draft 在多處出現 meta-review-aware 語句（e.g. Finding 1「Reviewer 對因果強度若要求量化，須回頭仰賴 c145」、Finding 2「Reviewer 應 flag 的 fidelity 邊界」、Finding 4「Reviewer Codex 預期會在此 hedge-attack」、Finding 5「Reviewer Codex 預期會嚴抓『橋接而非先例』的措辭」）— 這些是 Drafter 寫給 Reviewer / meta-merge 的內部信號，對 general public 讀者是冗餘 / 困惑 source。建議在 final publish 版移除或改寫為中性 caveat。

---

## Summary recommendations

1. **【最高優先】補 Finding 4 一段 c164 + c174 摘要派生 contested-tier 段落**：顧立雄部長具名 + NCSIST 騰雲 / 銳鳶 II PRC 零件 + Singapore vendors 繞道 + BusinessWeekly rebranding 模式 — 這是 brief SECONDARY #4「非紅供應鏈宣稱 vs 實況落差」最具體的台灣 case anchor，不該因 URL 失效就完全踢出。Sourcing caveat 標「accepted.jsonl 摘要層派生、原 URL 失效，具名實體驗收細節 pending」。
2. **【高優先】改寫 Finding 5 Confidence + What we don't know #3**：c151 摘要已揭 Taiwan-domiciled 實體在 Sep 2025 Entity List 32 家中；「直接管轄已及於台灣」應從「無法成立」改為「partial established fact，具名 entity 細節 pending」。Confidence 可從 medium 升 medium-high。
3. **【中優先】補 c167 MOEA 77 工具機對俄管制摘要至 Finding 5**：作為「FDPR → Taiwan trade-control practice」本土 mechanism reference（比 Haas 案還 directly relevant 的台灣本土實例，雖然客戶端是俄羅斯非中國，但機制可橋接）。
4. **【中優先】修 Finding 3 第 4 段「c130 廠商匿名」→「c137 廠商匿名」typo**。
5. **【中優先】補 Finding 2【強證據】#1 scope tag 中漏標的 temporal 軸**（per Dr2 contract）。
6. **【中優先】加 c132「日本高階工具機銷大陸持續成長」對照錨至 Finding 2**，給「西進非台灣孤例」一個區域 anchor。
7. **【低優先】Finding 6 P_south「證據基底最薄」改寫為「corpus curation 決定」**，避免讀者誤以為是事實判斷。
8. **【低優先】final publish 版移除 meta-review-aware 語句**（「Reviewer Codex 預期會...」「Drafter 不主張...」等）— 對 general public 讀者冗餘。

## Regeneration guidance (if needed)

整體 narrative arc 與 PRIMARY/SECONDARY 訴求 coverage 完整，**不需 re-Drafter**。建議 operator / Drafter 進 v2 revision pass 即可。

**Critical issues to feed back**:
- Finding 4 / 5 / What we don't know #2 + #3 對 accepted.jsonl 摘要層 sourcing 的利用過度保守 — c164 / c174 / c151 / c167 / c115 摘要均可派生 contested-tier 或 partial-fact claim，不該因 URL 失效 / SS landing 無 PDF 就完全踢出 evidence pool。
- 一個引用編號 typo（Finding 3 c130→c137）。
- 一個 scope tag 漏標（Finding 2【強證據】#1 missing temporal）。
- Finding 6 P_south 結論的 corpus-curation framing 需要從 Confidence 段提到主文層。

**Sources to prioritise deep-reading (operator next round)**:
- c151 Federal Register Sep 2025 Entity List PDF — 確認 Taiwan-domiciled 具名實體（高優先）。
- c164 Newtalk + c174 BusinessWeekly 替代 URL — search Google cache / Wayback Machine 找替代 sourcing。
- c139 MOPS 10 priority ticker 年報 — 仍是 firm-level evidence 主要缺口，但需 operator 手動下載（per brief 已標 pending）。

**Brief questions that need rephrasing**:
- 無 — brief Q1-Q5 各 Finding 對應清楚，Q6 斟酌題定位合理。
