# 台灣餐飲業 AI Kiosk 即時 demographic inference 部署的同意機制落差 — Insight Draft v1

**Project**: ai-kiosk-consent-tw · **Stage**: 5 (Draft) → 6 (Review) · **Date**: 2026-05-27
**研究焦點**: A∩D 灰區 — 「demographic inference 型部署」∩「告知/選擇/撤回三層同意 axis」的交集
**對照背景**: B(身分辨識)、C(會員 PII 資料流)— 列入 ontology 僅作 firewall，不計入 A 區部署數

## TL;DR

- **A 區部署規模必須雙端展開、不可給單一數字**：保守下界為一手確認 2 brand（雙月食品社 × WiXtar、金色三麥 × 星益欣）[c032, c041]；vendor-claimed 上界為 WiXtar 對媒體公開「30+ 餐飲品牌、超過 1000 台 AI Kiosk」，但 inference 啟用比例 vendor 未揭露 [c033]。**B 區智取櫃（銓幻元 99% 比對既有資料庫）、C 區拍檔 POS 不算進 A 區**[c049, c046]。
- **「inference 不算個資蒐集」業者 framing 在現行法下站不住**：個資法 §6 雖未把人臉/聲紋列入特種個資 [c054]，但釋字 603（指紋身分證案）已確立資訊隱私權對「高度識別性生物特徵」的憲法保護 [c097]；111 憲判 13（健保資料庫案）更明示「客觀上仍有還原可能性即仍屬個資，無論還原方法難易」，直接打掉「即時推論、不存原始影像」的常見抗辯 [c098]。
- **A∩D 灰區是四重結構性沉默 — 結構性零本身就是核心發現**：(1) 司法院 35 件人臉辨識/生物特徵裁判 0 件在餐飲 inference 場景 [c096]，但行政法院已有 profiling/特徵分析 doctrine 萌芽（高雄高行 114 簡 216 兒少案）[c095]；(2) 新北市 12 年（103-114）+ 桃園市 5 年（109-113）兩個消費爭議申訴 schema **零個 biometric/個資/inference category**，新北 services_others 2,235 件 + 桃園「其他」823 件 = 3,058 件/年 — **此為兩縣市 residual buckets 容量上界 proxy（invisible-ceiling），不是 inference 投訴量下界**；全國層消保會申訴 schema 同樣未列 biometric/inference 獨立 category [c079, c080] [c105, c106]；(3) 律所與行政院 PDPC 修法分析皆未觸及 §6 inference 灰區 [c055, c059]；(4) TAHR NGO 雖有立場但無投訴/案件量化 [c081, c082]。
- **vendor wording vacuum 不是「業界不知怎麼寫」、是 framing 選擇** — 跨**上游 SDK 供應商 / 中游 kiosk 整合商 / 終端餐廳**三層 vendor 結構 + **vendor 自家發布管道內部**都出現方向相反的 framing：上游 CyberLink FaceMe（2023）自家行銷文主動承認「人臉辨識需透過用戶『知情同意』」「用戶有權隨時取消/刪除」[c045]；星益欣執行長**康惠媚**於 2024/06/05 信傳媒聯訪自承「**台灣市場對於隱私個資較為敏感**」+ 採「**僅針對性別、人種、外觀『輪廓』辨識**」defensive framing [c108]；對照同 vendor 在中游 PR 案例稿 / 趨勢攻略 / CIO 詳細報導 / Marie Claire 共 4 層 + WiXtar 隱私政策（c109 generic 不涵蓋 inference）+ 雙月食品社官網 footer（隱私條款 deadlinks）+ **WiXtar YouTube channel 2025-12-15 vendor 一手 PR 影片** 共 **6 個 text/policy 發布管道**對告知/選擇/撤回三層全部零 wording [c110]；**且 vendor 自家 PR 影片本體（3:17）視覺檢視亦看不出同意介面 UI、機器周邊看不出告示與指示**（operator 視覺觀察）— wording vacuum 首次以 visual modality 補上 D 軸 UI silence [c110]。「業界不能寫」defence 被 **10 個 publication-channel / modality layer cross-confirmed**證據**削弱**（不是直接打掉）— vendor 在 CEO 媒體聯訪層已有 framing，卻未延伸至個資法 §8 五要素具體揭露；具體告知地點、形式、責任層仍待 PDPC 函釋釐清。
- **2025/11/11 個資法修正 + PDPC 籌備為政策時機，但修法本身未直接觸及 inference 灰區** — 立法理由 wording「為 AI 全面應用時代建立資料治理」屬 framing，條文核心為 PDPC 組織建構與 6 年過渡期；§6 特種個資定義未動 [c059, c055]。憲法面，111 憲判 13 主文第 2 項已就「欠缺獨立監督機制」明令違憲、要求 3 年內修法（2025-08-12 屆滿），2025/11/11 公布實質落後憲法判決 3 個月 [c098]。

## Context

本研究聚焦在 **A∩D 灰區** — A 區為即時 demographic inference 型部署（推測年齡、性別、語言、情緒等族群屬性，技術上不必比對既有身分庫，可純 edge inference），D 軸為知情同意三層（告知 / 選擇 / 撤回）；研究焦點為兩者交集，因為這是台灣個資法現行架構最尖銳、最有政策意義的單一缺口。研究嚴格與 B 區（生物特徵身分識別，例如智取櫃人臉取餐 [c049]）、C 區（POS + 會員 profile，例如拍檔科技 [c046]、Berry AI 廚房分析 [c047]）分軌計算，避免「把 inference 與 identification 混為一談給出膨脹的部署數字」此 brief 失敗條件。

時點上，2023/12/05 PDPC 籌備處成立；2022/08/12 111 憲判 13 命令 3 年內修法以建立獨立監督機制 [c098]；2025/11/11 總統公布個資法部分條文修正案，賦予 PDPC 監管職權 [c059]；6 年過渡期意味實質運作仍需多年。國際層面，EU AI Act Art. 5 emotion recognition 禁令僅及於職場與教育機構 [c067]，商業餐飲場景的 inference 治理在國際層面也仍是灰區，主要依賴 GDPR Art. 9 與 EDPB 意見 [c077] —— 台灣的政策設計有比歐盟更早正視此商業灰區的空間。

## Findings

### Finding 1 (Q1a) — A 區部署規模必須雙端展開：保守下界 2 brand vs vendor-claimed 上界 30+/1000+

**[strong]** A 區一手確認的保守下界為兩個品牌：(a) 雙月食品社 × WiXtar 3-in-1 AI Kiosk「先判斷年齡、性別、語言」並切換虛擬服務員，vendor 一手新聞稿明文「將消費者精細分類，並由 AI 影像生成技術塑造的虛擬人物進行個性化推薦」[c032]；(b) 金色三麥 × 星益欣「AI 餐酒實驗室」「已導入 AI 人臉辨識導購系統，根據顧客表情與特徵推薦酒款」[c041]。**這是 Drafter 願意以強證據聲稱的 A 區部署最低數字**。**部署事實具體化**：vendor 自家 YouTube channel 2025-12-15 PR 影片明文「**雙月食品社公園店**自 **2025/10 起的實際使用狀況**」[c110] — 截至本研究 retrieval (2026-05-27) 雙月公園店 inference 部署運作約 7 個月，是 vendor 一手具體分店 + 上線時間 confirmation。
<!-- {conceptual:A; temporal:2024+; geographic:TW} -->

**[contested]** vendor-claimed 上界由數位時代（BNext）獨立報導引 WiXtar 公開：「已在台灣 30 多間合作餐飲品牌旗下門市導入超過千台 AI Kiosk」[c033]。但有三層黑箱必須揭露：(i) 30+ 品牌名單未具名公布；(ii) WiXtar 產品線含 inference 與非 inference 配置，**千台 kiosk 中啟用 demographic inference 模組的比例 vendor 未揭露**；(iii) 「4 種虛擬店員劇本」背後 demographic 分類規則（年齡門檻、性別二分、語言對映）未公開 [c033]。Drafter 不能寫「台灣已有 1000+ 台 kiosk 做 demographic inference」，只能寫「WiXtar 部署 1000+ 台 kiosk，其中啟用 inference 比例未明」。
<!-- {conceptual:A; temporal:2024+; geographic:TW} -->

**[contested]** 歷史錨點與 2024+ F&B kiosk 必須分軌計算 — TAHR 一手記載至少 2014 年起 7-11/全家/萊爾富/星巴克/屈臣氏結帳櫃台上方已部署人臉辨識「搜集客戶族群資料投放廣告」[c082]，技術型態屬 A 區族群分類，但場景是 retail / 超商而非 F&B kiosk；提供 10+ 年「告知/同意機制長期缺席」的縱貫錨點，但**不可與 2024+ 雙月/金色三麥 inference 部署合為單一規模數字**。
<!-- {conceptual:A; temporal:2014+; geographic:TW} -->

**[speculative]** B 區與 C 區明確 callout 為「do not count toward A」：銓幻元 MCS 智取櫃以「99% 相似度比對既有資料庫」為核心技術 → B 區身分比對 [c049]；拍檔科技 30% 連鎖餐飲市占但功能為 POS + member 推薦 → C 區 [c046]；Berry AI 廚房 inventory + 人計數 → 營運分析非身分比對 [c047]。**這三家若被合進 A 區會直接觸發 brief 失敗條件**。
<!-- {conceptual:B,C; geographic:TW} -->

**Confidence**: medium — 保守下界 strong、上界 contested（單一 vendor 自報未獨立驗證），規模本身就是 vendor 揭露黑箱。
**Counter-evidence**: c044 CyberLink FaceMe SDK 產品頁摘要層列「age & gender detection for fast-food restaurants」*(依摘要層 sourcing，未經 deep-read 一手驗證)*，意味 SDK 上游廠商產品線本身已將「快餐 inference」列為標準 use case，部署數可能比已具名的 2 brand 更廣，但 vendor 揭露不足無法量化。

---

### Finding 2 (Q1b) — 雙 use-case showcase：消費者使用情境完整時間軸 + 可見/不可見動作 + 資料 artifact 流向

#### Showcase A — 雙月食品社 × WiXtar 3-in-1 AI Kiosk（米其林必比登推薦店）

**[strong]** 時間軸 + 動作 + artifact 拆解：
<!-- {conceptual:A; temporal:2024+; geographic:TW} -->

| 階段 | 消費者可見動作 | 系統不可見動作 | 資料 artifact 流向 |
|---|---|---|---|
| t₀：進店 | 看到 kiosk + 攝影鏡頭，無告示、無同意提示 | 鏡頭啟動 | （無消費者可見任何 D 軸介面） |
| t₁：站到 kiosk 前 | 螢幕顯示虛擬服務員（女性顧客看到「美女」、男性顧客看到「創辦人」） | AI 影像辨識 → 推估年齡/性別/語言 → 從至少 4 種虛擬店員劇本擇一切換 | 即時臉部畫面進入 RAM / 推論管線 |
| t₂：點餐 | 與虛擬服務員互動、瀏覽推薦菜色 | 持續 inference + 推薦策略運算 | 點餐序列 + inference 結果累積 |
| t₃：結帳 | 完成交易（雙月數位交易佔 90%） | 訂單記錄上傳 | **vendor 明文「藉由雲端運算，將資料完整回傳台灣總部」[c032]**；外籍遊客語音通過 OpenAI / 微軟 API 跨境傳輸 [c033] |

關鍵 framing 證據：vendor 一手稿全頁 0 次出現「同意、告知、隱私、個資、保護、權利、撤回、刪除、特徵、生物」十個關鍵字 [c032]。BNext 獨立報導同樣 0 出現 [c033]。

#### Showcase B — 金色三麥 × 星益欣「AI 餐酒實驗室」

**[strong]** 時間軸 + 動作 + artifact 拆解：
<!-- {conceptual:A; temporal:2025; geographic:TW} -->

| 階段 | 消費者可見動作 | 系統不可見動作 | 資料 artifact 流向 |
|---|---|---|---|
| t₀：進店 / 入座 | 看到「拍照玩 AI 調酒師」介面 framing | （消費者主動拍照前，桌面攝影機規劃中） | — |
| t₁：拍照互動 | 「只要拍一張照片，AI 就能推算性格特質，並推薦相應酒款」[c042] | 人臉表情 + 特徵分析 → 性格 / 偏好推算 | 臉部畫面 + 推論結果 — 留存期 vendor 未說明（資訊缺口） |
| t₂：飲酒中 | （規劃中）桌面觀察 AI 系統偵測空杯、使用頻率 | 持續 inference | 飲酒行為時序資料；vendor 「規劃推出」狀態 [c041] |
| t₃：服務員主動互動 | 「提醒服務人員主動出擊」（推薦加點） | 推薦邏輯運算 | — |

關鍵 framing 證據：CIO Taiwan 詳細報導全頁 0 字提同意 / 告知 / 隱私 [c041]；Marie Claire 消費者體驗報導同樣 0 字提 [c042]。消費者全程感知為「玩遊戲」，不會被 framing 觸發「我正在參與生物特徵蒐集」的認知 — 此 framing 設計讓 D 軸對消費者**結構性不可見**。

**[contested]** 雙 showcase 共同特徵：(i) 消費者站到機器前的瞬間就被掃描，無任何告知介面 — 此 claim 在 patch 4 階段獲 visual evidence 部分 corroboration: vendor 自家 YouTube PR 影片 (3:17, 2025-12-15, [c110]) 視覺檢視「**影片中看不出同意介面、機器周邊看不出告示與指示**」(operator 視覺觀察)，此為 vendor PR 影片視覺檢視非完整現場 fieldwork，但與 9 個 text/policy publication channels 的 wording vacuum 跨 text + visual 兩 modality cross-confirmed；(ii) 「使用 kiosk 即默示同意」的 framing 在實作上是「沒有任何同意介面，預設參與」；(iii) 資料 artifact 是否留存、留多久、傳輸到哪、是否進會員 profile，vendor 公開資料皆未說明 — 此**留存政策黑箱**是 Q1b 跨 case 一致的資訊 gap。**部署範疇 visible expansion** [c110]: vendor 自家 channel 揭露雙月公園店部署不只 kiosk inference，還含「**影像辨識出餐**」+「**AI 巡店系統 / 店長管理大師**」店內持續視覺監控延伸到 staff 監控 + 出餐 QC — 比 c032/c033 早期 PR 揭露範圍更廣，artifact 流向涵蓋 kiosk-side inference + 店內 ambient 視覺監控雙軌。
<!-- {conceptual:A∩D; temporal:2024+; geographic:TW} -->

**Confidence**: high — 兩個 case 皆有 ≥3 源 cross-confirmed 部署事實 + 5+ 源 cross-confirmed D 軸 wording vacuum。
**Counter-evidence**: 桌面觀察 AI 系統 vendor 明示「規劃推出」非「已部署」，Drafter 維持 [contested-planned] 標記不誇大。

---

### Finding 3 (Q2 + Q7) — A 區告知層 vendor 與媒體 wording vacuum 是 5 源 cross-confirmed 系統性現象

**[strong]** inference 型 A 區部署在「告知」層的 vendor / 媒體 wording 實況 — **6 個 PR / 案例 / vendor 自家 channel 發布管道**：(a) c032 雙月 WiXtar 一手新聞稿 0 字提同意/告知/隱私；(b) c041 CIO Taiwan 金色三麥詳細報導 0 字提；(c) c037 WiXtar 2026 餐飲 AI 趨勢攻略 thought leadership 0 字提；(d) c042 Marie Claire 消費者體驗報導 0 字提；(e) c038 TechNews 星益欣 × 金色三麥報導 0 字提；(f) **WiXtar YouTube channel 2025-12-15 vendor 一手 PR 影片 description**「VLM 影像分析:客層辨識、特徵行為分析」**0 字提**同意/告知/隱私 [c110]。**六源 cross-confirmed** — vendor 連在自家最新（post-EU AI Act + post-2025/11/11 修法）的 PR channel 都連 boilerplate 隱私聲明都沒提，wording vacuum 是 Q2 對個資法 §8 落差的最直接事實層證據。**三重 negative finding**：(i) WiXtar 隱私權政策（wixtar.com/agreement/privacy）內容是電商 cookies / 信用卡會員範圍，**完全不涵蓋 AI Kiosk / 人臉辨識 / 生物特徵 / demographic inference / 影像處理**[c109]；(ii) 雙月食品社官網（moonmoonfood.com）footer「隱私條款 | 條款及細則」字眼但**未提供可點擊 URL**（純文字 deadlinks）[c109]；(iii) vendor 自家 PR 影片本體 (3:17) 視覺檢視亦**看不出同意介面 UI、機器周邊看不出告示與指示**（operator 視覺觀察）[c110] — wording vacuum 首次以 visual modality 補上 D 軸 UI silence。**合計 10 個 publication-channel / modality layer cross-confirmed wording vacuum**。
<!-- {conceptual:A∩D; temporal:2024+; geographic:TW} -->

**[contested]** **但 5 層 wording vacuum 不是全稱沉默 — 存在一個 publication-channel exception**：星益欣執行長**康惠媚**於 2024/06/05 信傳媒聯訪明文 frame：「**因為台灣市場對於隱私個資問題較為敏感**，因此目前所謂的將消費者分類，**僅針對性別、人種以及外觀（服裝）這種『輪廓』進行辨識**」[c108]。這是 vendor side 首個 confirmed 一手 defensive framing — **業者不是不知道隱私敏感性、也不是完全沉默，而是 publication-channel 分裂**：CEO 媒體聯訪層有 framing、PR 案例稿 / 趨勢攻略 / CIO 詳細報導 / Marie Claire / 隱私政策 5 個下游發布管道零 wording。framing 選擇是「在 narrative 層 articulate『輪廓辨識 ≠ 人臉特徵』defensive narrative」、**而非延伸至 §8 五要素具體實作層揭露**。
<!-- {conceptual:A∩D; temporal:2024-06-05; geographic:TW} -->

**[strong]** wording vacuum 不是 vendor 「沒空寫」、是「framing 性地不認為需要寫」 — 跨 vendor framing 對照證明此點：上游 CyberLink FaceMe 在 2023 年自家行銷文中主動寫「在提供便利與個人化顧客服務提供同時，人臉辨識技術也需符合安全法規，提供隱私保護，需要透過用戶『知情同意』才能以個人資料進行客製化服務」[c045]；星益欣康惠媚在 CEO 媒體聯訪層自承「台灣市場對隱私個資較為敏感」[c108]。**台灣 vendor 已有示範如何 framing 知情同意**，業界 wording vacuum 在 PR / 政策 5 層的沉默不能再用「業界不知怎麼寫、技術不能描述」當藉口。
<!-- {conceptual:A∩D; temporal:2023; geographic:TW} -->

**[contested]** vendor 在自家網域中也有結構性切割 — WiXtar 案例新聞稿、產品頁、隱私政策三者完全切割，案例新聞稿不導流到隱私政策、隱私政策只談「網站訪問」不談 kiosk 部署 [c032]。即使讀者主動找隱私政策也找不到 kiosk inference 相關說明，此**結構性切割**正是 D 軸告知層 broken 的具體呈現。
<!-- {conceptual:A∩D; geographic:TW} -->

**Confidence**: high — 五源 cross-confirmed + 一源 vendor 反例（CyberLink）證明此非 industry-wide 不能寫。
**Counter-evidence**: c045 CyberLink 自家承認知情同意，是 vendor wording vacuum 的孤例反證；Drafter 把它寫成 framing 對照而非主結論 counter-finding（detailed treatment 見 Finding 5）。

---

### Finding 4 (Q4) — 「inference 不算個資蒐集」業者 framing 完整法律拆解：個資法 + 憲法 spine

**[strong]** 個資法本文與條文形式：§6 把特種個資限縮為 6 類（病歷、醫療、基因、性生活、健康檢查、犯罪前科）— **這是 closed list，不含「等」字，人臉/聲紋等高度識別性生物特徵在條文形式上確定未列入** [c054]。但這不等於業者可主張「inference 不算蒐集」 — §6 是「特別嚴格之蒐集禁制」，未列入只是退到「一般個資」層級，仍受 §5（目的拘束）、§8（告知義務）、§19-§20（蒐集與利用限制）完整拘束 [c053]。
<!-- {conceptual:A∩D; temporal:2025-11-11 修法後; geographic:TW} -->

**[strong]** 憲法 spine（釋字 603 + 111 憲判 13）的論證骨幹：
<!-- {conceptual:A∩D; geographic:TW} -->

- 釋字 603（2005 指紋身分證案）對「資訊隱私權」的權威定義：「保障人民決定**是否揭露**其個人資料、及在**何種範圍內、於何時、以何種方式、向何人**揭露之決定權」 — 五個動詞正好對映 D 軸（告知/選擇/撤回）的全部內涵 [c097]。「使用 kiosk 即默示同意」這種 framing 在此標準下，於「人民決定是否揭露」此資訊自決核心受到實質侵蝕（**Scope caveat**：釋字 603 原因案件為國家強制蒐集（state action），餐飲 kiosk 為私部門商業行為，doctrine 直接適用上有水平效力（horizontal effect）中介；本研究援引其資訊隱私權定義 + 比例原則邏輯，屬通說可承載之 transferable scope）。
- 釋字 603 對指紋的論證（人各不同 / 終身不變 / 與身分連結後居於「鎖鑰地位」 / 可形成監控之敏感性資訊）同樣可類比適用於人臉、聲紋；大法官要求「目的須法律明確、必須通過比例原則中度審查」[c097] —— 此「法律明定目的」要件源自 state action 場景，**直接套用到私部門商業 inference 需經水平效力與個資法 §5、§19 中介論證**：私部門個資法架構不必然要求每一商業蒐集目的有單一法律明確授權，而是要求蒐集行為與特定目的有合理關聯。餐飲業 AI Kiosk 即時 demographic inference 在此框架下，「個人化推薦 / 節省人力」目的的特定性、合理性與成比例性皆有實質檢驗壓力。
- 釋字 603 對「身分證防偽、辨識失智者、無名屍體」等具公益正當性的目的尚且認定「損益失衡、手段過當」 — 那麼餐飲業以「個人化推薦」「節省人力」這類純商業目的蒐集 demographic inference，**在比例原則審查下的合憲性壓力顯著大於釋字 603 已宣告違憲的指紋蒐集** [c097]。

**[strong]** 111 憲判 13（健保資料庫案）對「inference 不識別個人 = 非個資」此 framing 的 spine-level 反駁：「個資若經處理，依其資料型態與資料本質，客觀上仍有還原而間接識別當事人之可能時，**無論還原識別之方法難易**，若以特定方法還原而可間接識別該個人者，**其仍屬個資**。」[c098] 只要該影像在處理過程中**客觀上仍有還原可能性**，就**仍屬個資、仍受憲法保障**。憲法法庭明示個資法 §2 第 1 款「得直接或間接識別該個人」的法律定義即在表彰此憲法意旨 [c098]。**[speculative-mechanism]** 至於「edge inference 系統在處理流程中是否實質在 RAM / cache 短暫留存原始畫面」屬技術 mechanism 推論 — 本研究**未取得 vendor 系統架構文件或第三方技術稽核報告直接驗證**；列入 What we don't know 待技術專家或 vendor 揭露填補。若該機制存在，c098 還原識別性標準直接打掉 no-storage framing；若不存在，c098 仍可從「inference 結果本身配合店面 metadata（時段／座位／消費序列）即構成間接識別」的角度涵蓋。
<!-- {conceptual:A∩D; geographic:TW} -->

**[strong]** 111 憲判 13 把資訊隱私權拆成「事前控制權（同意）」+「事後控制權（刪除/停止/限制）」**兩層架構**，正好對映 D 軸三層；憲法法庭並明文認定「個資法欠缺停止利用請求權違憲」、要求 3 年內修法 [c098]。**憲法已認定立法欠缺撤回機制違憲，而餐飲業實作層更是完全空白 — 法律端 + 實作端兩端皆 broken**。
<!-- {conceptual:A∩D; geographic:TW} -->

**[contested]** **vendor 一手 framing「輪廓辨識 ≠ 人臉特徵比對」二分的法律拆解**（c108 信傳媒康惠媚 2024/06/05 confirmed verbatim）：星益欣 CEO 主張「目前所謂的將消費者分類，僅針對性別、人種以及外觀（服裝）這種『輪廓』進行辨識」[c108]。此 framing 在台灣個資法 + 憲法層面有三個直接 challenge：
<!-- {conceptual:A∩D; temporal:2024+; geographic:TW} -->

1. **「輪廓」≠「特徵比對」但仍是個資**：個資法 §2 第 1 款「直接或間接識別」標準下，性別 / 人種 / 衣著外觀即時分類**結合店面 metadata（時段 / 座位 / 消費序列 / 結帳交易紀錄）**仍可間接識別具體個人 [c053]。111 憲判 13【35】「客觀上仍有還原可能性即仍屬個資，**無論還原方法難易**」標準對此邊界直接適用 [c098] — vendor「輪廓不算人臉特徵」二分**不能脫離個資法**。**Vendor 自我矛盾**：c108 信傳媒主張「**僅針對性別、人種以及外觀『輪廓』辨識**」(2024-06-05)，但 vendor 自家 YouTube channel 2025-12-15 PR 影片 description **明文寫「VLM 影像分析:客層辨識、特徵行為分析**」[c110] — **vendor 在自家發布管道用「特徵行為分析」wording 描述系統能力**，與 CEO 媒體聯訪「輪廓 ≠ 特徵比對」二分**正面矛盾**。可解讀為 (a)「輪廓」是 vendor PR-side defensive framing、實際技術為「特徵行為分析」；或 (b)「特徵行為分析」是 vendor 自家行銷 trait-based inference 廣告框架、實際範圍可能更窄 — 但無論哪種，vendor 跨發布管道對系統能力的 self-description 不一致本身證明此 framing 戰略 fluid，**不能被消費者作為 §8 告知標的依賴**。
2. **「人種」是 EU AI Act Art. 5(1)(g) 明文禁止的 6 類敏感屬性之一**：EU AI Act 禁止以 biometric data 推斷「種族」「政治意見」「宗教信仰」「性生活」「性傾向」「工會會員」六類 [c067]。c108 vendor 明文承認以「**人種**」做即時分類 — 在 EU 標準下這是 categorically prohibited 行為類別。台灣 §6 / EU AI Act 在「人種推斷禁制」上的落差正是 PDPC 修法政策建議的具體點。
3. **「台灣市場對隱私個資較為敏感」承認 = 業者已認知 D 軸告知 / 同意機制必要性**：c108 vendor wording 本身證明已認知敏感性 [c108]，但選擇以「輪廓辨識 (≠ 人臉特徵)」defensive framing 回應，**而非以個資法 §8 五要素揭露 + opt-out 介面回應**。這是 framing 選擇問題不是法遵能力問題 — 釋字 603「資訊隱私權」對「決定**是否揭露**個人資料」的權威定義 [c097]，要求的是給消費者「決定」的機會，而非由 vendor 替消費者決定「這只是輪廓不算個資所以不需告知」。

**[contested]** 2025/11/11 修法對 A∩D 灰區的實質影響有限：行政院新聞稿立法理由 wording「建立 AI 全面應用時代的資料治理」是 framing 而非 enforceable 條文 [c059]；fblaw 律所對修法核心的分析是「PDPC 組織建構 + 監管權限賦予」**而非 §6 inference 灰區的填補** [c055]。修法為未來 PDPC 函釋 / 子法建立法源，但目前 §6 特種個資定義未動，A∩D 灰區的填補仍需 PDPC 後續函釋。**c108 vendor「輪廓 vs 特徵比對」defensive framing 是 PDPC 函釋首要應處理的具體業者立場**。
<!-- {conceptual:A∩D; temporal:2025; geographic:TW} -->

**Confidence**: high — 4 源 strong（c053 / c054 / c097 / c098）+ 2 源 contested（c055 / c059）— 法律與憲法 spine 都是 primary doc 一手條文與判決原文。
**Counter-evidence**: 業者「我們不識別個人、只做即時推論、不存資料」framing 在 111 憲判 13 標準下被結構性瓦解。國發會在 111 憲判 13 程序中曾陳述「健保資料『非用於識別』故與釋字 603 場景有本質差異」此 framing[c098]，**結構與業者「inference 不識別個人」framing 同構**，但被憲法法庭以「無還原可能性才脫離個資法」邏輯直接駁回 — 是業者 framing 在司法層面已有同構先例敗訴的最直接證據。

---

### Finding 5 (Q4 + Q7) — vendor 三層責任結構下的 framing 分裂：supply chain 上游 vs 中游 vs 終端的同意機制 wording 選擇

**[contested]** 同產業內部的同意機制 framing 跨「上游 SDK 供應商 / 中游 kiosk 整合商 / 終端餐廳部署方」三層出現方向相反的 framing 選擇：
<!-- {conceptual:A∩D; temporal:2023-2026; geographic:TW} -->

- **上游 SDK 供應商（CyberLink FaceMe，2023 餐飲應用 marketing）**：主動承認 D 軸三層 — (a) 告知層 — 「人臉辨識技術也需符合安全法規，提供隱私保護」；(b) 同意層 — 「需要透過用戶『知情同意』才能以個人資料進行客製化服務」；(c) 撤回層 — 「用戶也有權利隨時取消人臉資料的授權或是刪除他們的個人資料」[c045]。**這是台灣 vendor 自家行銷文中對 D 軸三層完整承認的孤例**。
- **中游 kiosk 整合商（WiXtar，2024–2026 跨多發布管道）**：呈現**vendor 自家內部 publication-channel 分裂**：
  - CEO 媒體聯訪層（信傳媒 2024/06/05）：康惠媚自承「台灣市場對隱私個資較為敏感」+「僅針對性別、人種、外觀『輪廓』辨識」defensive framing [c108]
  - PR 案例稿 / 趨勢攻略層（2024–2026）：c032 雙月案例稿、c037 2026 趨勢攻略 thought leadership 七大模組 framing **對 D 軸三層全部零字提**
  - **vendor 自家 YouTube channel 層（2025-12-15）**：vendor PR 影片 description 描述「VLM 影像分析:客層辨識、**特徵行為分析**」+「影像辨識出餐」+「AI 巡店系統」，**對 D 軸三層全部零字提**；影片本體 (3:17) 視覺檢視亦看不出同意介面、機器周邊告示 (operator 視覺觀察) [c110] — **與 c108 CEO 媒體聯訪「輪廓 ≠ 特徵比對」defensive framing 形成自我矛盾**：vendor 自家用「特徵行為分析」wording
  - 隱私權政策層（wixtar.com/agreement/privacy, undated）：政策**存在**但內容是電商 cookies / 信用卡會員範圍，**完全不涵蓋 AI Kiosk / 人臉辨識 / 生物特徵 / demographic inference / 影像處理** [c109]
- **終端部署方（金色三麥 × 星益欣 case，2025/05 CIO Taiwan 深度報導；雙月食品社 moonmoonfood.com）**：對 D 軸三層零 wording [c041]；雙月官網 footer「隱私條款 | 條款及細則」字眼但**未提供可點擊 URL**（純文字 deadlinks）[c109]。

**Scope caveat**: (i) 三層橫跨 2023（c045 CyberLink）→ 2024/06/05（c108 信傳媒）→ 2026（c037 WiXtar / c041 CIO 報導）跨時比較，非同年同產品線的直接對照；EU AI Act 通過後（2024）CyberLink 是否更新 framing 本研究未驗證。(ii) c045 是 SDK 供應商的 thought leadership / marketing，**不必然代表 SDK 部署到下游 kiosk 時 CyberLink 會合約強制下游 kiosk 整合商複寫同樣 wording**，這是 SDK 廠商自我定位而非具拘束力的合約條款。(iii) **WiXtar 自家內部 publication-channel 分裂**：CEO 聯訪層有 defensive framing（c108），下游 PR / 政策 5 層零 wording — framing 選擇不是 industry-level 不能寫的問題，而是發布管道的 strategic split。

**[contested]** 此 vendor 三層 framing 分裂的政策意義是 brief counter_framing `implied_consent` 的 partial counter（caveat-tier rescue per Dr7）：業者側 implied_consent / no_storage / no_identification 全為 **OMISSION 而非陳述**（業者用沉默而非辯論），但 CyberLink 在自家行銷文中主動承認知情同意，構成 vendor-side 內部分裂、作為 implied_consent counter-framing 的 mechanism-inference rescue。即使把 D 軸法遵責任在三層之間分配，**仍存在「整條 supply chain 至少一層 vendor 已公開承認需做知情同意」的事實**。這**削弱**（不是直接打掉）兩個業者潛在 defence：
<!-- {conceptual:A∩D; geographic:TW} -->

1. 「業界 wording vacuum 是法遵不能寫、技術不能描述」 — 上游 CyberLink（c045）+ 中游 WiXtar CEO 媒體聯訪（c108）**兩層都有 vendor 主動 framing 紀錄**，證明 D 軸 / 隱私敏感性 wording 在多個 publication-channel 都是可寫、可 framing 的；
2. 「同意機制設計責任完全在下游餐廳、不在 vendor」 — SDK 廠商（CyberLink）若認為自己純技術供應、與 D 軸無關，不會主動把三層 wording 寫進自家 marketing；CEO 媒體聯訪（c108）若認為「責任在下游」，也不會用第一人稱主動承認「台灣市場對隱私個資較為敏感」。

WiXtar / 星益欣若援引「責任界線、我們不負責告知」defence，CyberLink 的 framing 模板使「整合商 / 終端完全不需提及」此立場至少不能再宣稱代表業界共識。**但本研究不主張這直接 transfer 為「WiXtar / 星益欣必須在每篇新聞稿中重複 §8 五要素」此硬規範** — 個資法 §8 告知義務的具體地點（店面公告？kiosk 開頭畫面？隱私政策？）與形式（哪一層 vendor 主責）仍需 PDPC 函釋釐清，這是 Finding 4 政策建議呼應的具體 gap。

**Confidence**: medium — 三層 framing 對照本身 strong tier（CyberLink c045 1 源 + 星益欣 CEO 聯訪 1 源 [c108] + WiXtar/星益欣 PR/政策 5 源 zero wording cross-confirmed），但 partial_counter_framing 性質意味此 Finding 是 caveat-tier rescue，**不應升為 [strong] 主結論**（per Dr7）；三層責任界線本身仍是政策待釐清議題。
**Counter-evidence**: (a) CyberLink 為 SDK 供應商，可能把實際 D 軸告知 / 同意取得義務的執行責任推給下游 kiosk 整合商或終端餐廳；其 framing wording 是 marketing 自我定位而非具拘束力的合約義務。但即使如此，SDK 廠商選擇主動承認 D 軸三層此 framing 本身仍是 evidence。(b) WiXtar / 星益欣**自家 CEO 在媒體聯訪層已有 defensive framing**（c108 康惠媚自承「台灣市場對隱私個資較為敏感」+「輪廓辨識」）— 但此 framing **未延伸至 PR 案例稿 / 趨勢攻略 / 隱私政策層**的 §8 五要素具體揭露;原版 F5 描繪「完全沉默」需 narrow 為「**publication-channel 分裂**:聯訪層有 framing、PR / 政策 5 層 wording vacuum」。(c) c045 為 2023 年資料,AI Act 通過後（2024）CyberLink 是否更新 framing 未驗證;c108 為 2024/06/05 信傳媒 articulation,後續 vendor 是否在其他發布管道延續此 framing 也未追蹤。(d) 雙月 c032 / 金色三麥 c041 兩個 case 的店面實作層 D 軸有無告示 / 同意介面 / 退出選項，本研究依公開資料推論為缺席，patch 4 階段補上 vendor 自家 PR 影片 visual modality 觀察（c110, operator 看 3:17 影片本體後報告「畫面上看不出來會有知情同意和機器周邊有說明與指示」），與公開資料推論一致 — **但完整現場 fieldwork (operator 親訪雙月公園店或金色三麥分店實地觀察) 仍未進行**，可進一步確認或反駁。

---

### Finding 6 (D 軸三層對照) — 同意機制三層 vendor × 告知/選擇/撤回 勾選對照表（brief HARD requirement）

**[contested]** A 區四家代表 vendor 對 D 軸三層的實作對照（✓ = 有明文 wording，✗ = 完全零 wording，? = vendor 公開資訊無法確認；對照標準為個資法 §8 第 1 項應告知事項 + 111 憲判 13 事前/事後控制權雙層架構 [c098]）：
<!-- {conceptual:A∩D; temporal:2023-2026; geographic:TW} -->

| Vendor / 部署方 | 告知層 | 選擇層 | 撤回層 | Source（一手 wording 出處） |
|---|---|---|---|---|
| **雙月食品社 × WiXtar**（kiosk 部署終端） | ✗ 零 wording¹ | ✗ 無人工替代描述 | ✗ 零 wording | c032 vendor 一手稿 + c033 BNext + c042 Marie Claire 全頁掃描 |
| **金色三麥 × 星益欣**（kiosk 部署終端） | ✗ 零 wording¹ | ✗ 無人工替代描述 | ✗ 零 wording | c041 CIO Taiwan + c038 TechNews + c042 Marie Claire 全頁掃描 |
| **WiXtar**（中游 kiosk 廠商 thought leadership） | ✗ 七大模組 framing 中 0 字提 D 軸 | ✗ 未提 | ✗ 未提 | c037 WiXtar 2026 趨勢攻略 |
| **CyberLink FaceMe**（上游 SDK 供應商） | ✓ 「需符合安全法規，提供隱私保護」 | ✓ 「需要透過用戶『知情同意』才能以個人資料進行客製化服務」 | ✓ 「用戶有權利隨時取消人臉資料的授權或是刪除他們的個人資料」 | c045 CyberLink 自家行銷文 |

¹ 六源 + 三層 negative finding cross-confirmed：c032 (WiXtar 雙月) + c033 (BNext) + c037 (WiXtar 趨勢) + c041 (CIO 金色三麥) + c042 (Marie Claire) + **c110 (WiXtar YouTube channel 2025-12-15 vendor 一手 PR 影片 description)** 全頁掃描 0 hit 於「同意、告知、隱私、個資、保護、權利、撤回、刪除、特徵保護、生物」十個關鍵字；隱私政策 c109 generic 不涵蓋 inference；雙月官網 footer deadlinks；**c110 影片本體 (3:17) 視覺檢視亦看不出同意介面 UI / 機器周邊告示** (operator 視覺觀察) — 跨 text + visual 兩 modality cross-confirmed。

**[contested]** 對照個資法 §8 第 1 項應告知五要素（蒐集者名稱、目的、項目、利用期間 + 地區、對象、方式、當事人權利、不提供之影響）：雙月 / 金色三麥兩部署終端對五要素**全部 0 項回應**；CyberLink 雖在 framing 層完整承認三層，但對「同意取得方式」具體 implementable 設計（店面公告？kiosk 同意鈕？隱私政策？雲端 opt-out portal？）也未提 [c045] — **即使是 framing 正確的 vendor，也未提供 implementable 同意機制設計**，此 gap 正是 PDPC 函釋 / 施行細則應補的具體部分。
<!-- {conceptual:A∩D; geographic:TW} -->

**Confidence**: medium — vendor wording 五源 cross-confirmed 為 strong；勾選對照本身是 Drafter 對比個資法 §8 的中介判斷，故整體標 medium。
**Counter-evidence**: CyberLink 為 SDK 供應商而非 kiosk 終端，理論上法律責任在下游；但 SDK 上游已寫 framing 仍是強反例。

---

### Finding 7 (Q3 + Q6) — A∩D 灰區的四重結構性沉默：結構性零本身就是核心發現

**[contested]** **這不是「沒有問題」、是「沒有資料」就是核心發現** — A∩D 灰區的政策結構性失靈，由四個獨立 angle 的「結構性零」交叉確認：
<!-- {conceptual:A∩D; temporal:2011-2025; geographic:TW} -->

**(1) 司法零** — 司法院裁判書系統中含人臉辨識 / 生物特徵的 35 件裁判，**0 件**在餐飲 inference 場景 [c096] *(依摘要層 sourcing，未經 deep-read 一手驗證)*。**邊界判例**：高雄高等行政法院 114 年度簡字第 216 號（兒少福利與權益保障法案，非餐飲場景）已明文論述「自動化資料處理、特徵分析、行為定位、強制身分核實」對兒童的 profiling 風險 [c095] *(accepted record metadata 層 — 顯示行政法院已有 profiling / 特徵分析 doctrine 萌芽，餐飲 inference 場景的零判決不等於完全無 doctrine 可援引)*。

**(2) 申訴 schema 零（visibility-blind residual pool 容量上界 proxy，非投訴量下界）** — 新北市消費爭議第一次申訴案件 12 年縱貫資料（103-114 年）18+ 個 category，**全無 biometric / 個資 / inference 獨立 column**；即使消費者就 kiosk inference 投訴，只能歸入 services_others（113 年 = 2,235 件）或 business_others（113 年 = 3,074 件）兩個 opaque residual buckets [c105]（**注**：c105 extract 內部 Passage 1 對 103 年數字、Passage 2 對 113 年數字並列呈現；本研究採 Passage 2 full time-series 為準）。桃園市 5 年縱貫（109-113 年）25 個 zh-TW 具名 category + 「其他」，113 年「其他」823 件（占 18%），第二縣市重複確認 schema 結構性零 [c106]。**新北 services_others 2,235 + 桃園「其他」823 = 3,058 件/年**，此為兩縣市 residual buckets 「若 A∩D 投訴存在則 absorb 進此 opaque pool」之 **schema-design 容量上界 proxy**（invisible-ceiling）— bucket 內 inference 比例 unknown，**不能讀作 inference 投訴量下界**；採 services_others 為主係因「服務類爭議」場景與餐飲 kiosk 接近，若聯合計入 business_others 3,074 件則上界 proxy 達 5,309 件 / 年[c105]。**全國層**：行政院消保會全國申訴統計現有公開 schema 同樣未列 biometric / inference 獨立 category [c079] *(metadata 層 sourcing — 本研究未取得 row-level deep-read 進一步驗證)*；消保會線上申訴系統存在但渠道使用層的 silence 與縣市層平行 [c080] *(同前)*。台中市 row-level 因 DNS proxy 失敗，僅 schema metadata 層 corroborate [c107] *(依摘要層 sourcing，未經 deep-read 一手驗證)*。

**(3) 律所 / 行政院 framing 零** — fblaw 律所對 2025/11/11 修法的分析聚焦於 PDPC 組織建構，**未觸及 §6 inference 灰區** [c055]；行政院 PDPC 修法新聞的立法理由 wording「AI 全面應用時代資料治理」是 framing 抽象化，條文實質**未動 §6 特種個資範圍**、未直接觸及 inference 灰區的法律屬性 [c059]。

**(4) NGO 量化零** — TAHR 在「你的臉孔不是你的臉孔」「下一張臉在哪」等立場文件中對「匿名化即不算個資」「inference 不算」業者 framing 已有 push-back，但**無具體投訴 / 案件量化數據** [c081, c082]；NGO 立場層存在、量化層空白。

**[contested]** 「結構性零」非「實質零」的重要區分：四重零不等於「無消費者投訴、無問題」，而是「投訴 / 司法 / 律法 / NGO 四個系統皆無 visibility framework 可辨識此議題」。新北 + 桃園兩縣市 schema 連「殯葬設施、禮券」這類細項都有獨立 category — 表示**未添加 biometric / inference category 是設計者未把此議題列入優先，不是「無法 represent」** [c106]。這個 schema-design 層的結構性 invisibility 是 A∩D 灰區政策失靈的根源。
<!-- {conceptual:A∩D; geographic:TW} -->

**[contested]** 結構性零的雙重結構性原因（國際比較對照）：(i) 台灣個資法 §28 損害賠償需證明實際損害（不像 BIPA statutory damages $1,000-$5,000/筆推定），消費者起訴經濟誘因不足；(ii) class action 程序門檻高、無成熟機制 [c073]。Q6 執法零不只是「監管不力」，也是「私人 enforcement 機制缺位」雙重 institutional friction。
<!-- {conceptual:A∩D; geographic:TW,US-IL} -->

**Confidence**: medium — schema-design 結構性零有 row-level cross-locality confirmation；司法零依摘要層；framing 零有兩源 cross-confirm；NGO 立場明確但量化空白。
**Counter-evidence**: 「結構性零 → 政策失靈」這層歸因，理論上有「實際無問題故無投訴」的另類解釋；但 TAHR 立場 + 國際比較（Home Depot 案）+ vendor wording vacuum 三方匯流，本研究判斷「實質零」假說站不住。

---

### Finding 8 (Q5) — 國際最低標準對照：EU AI Act + GDPR + BIPA + SG PDPA 對台灣的可借鏡標準

**[strong]** **EU AI Act Art. 5 對台灣餐飲 kiosk 的覆蓋其實有限，Drafter 不能誇大 EU 限制範圍** — Art. 5(1)(f) emotion recognition 禁令僅及於職場 + 教育機構，**商業餐飲場合完全不在禁止範圍** [c067]；Art. 5(1)(g) biometric categorisation 禁令只禁「推斷種族 / 政治 / 工會 / 宗教 / 性生活 / 性傾向」6 類敏感屬性，**推斷年齡 / 性別 / 語言 / 情緒未列入** [c067]。雙月「先判斷年齡、性別、語言」+ 金色三麥「按表情推薦啤酒」**完全落在 EU AI Act 已禁止範圍之外**。但 Art. 5 禁令的存在本身即承認「依生物特徵推斷他人屬性是有 categorical 風險的行為，需立法干預」 — 台灣 §6 修法政策方向可參考此邏輯。
<!-- {conceptual:A∩D; temporal:2024+; geographic:EU} -->

**[strong]** GDPR Art. 9 + EDPB Opinion 11/2024（機場 FR）才是國際真正涵蓋商業 demographic inference 的 spine — GDPR 將生物特徵資料列入特種個資、原則禁止，例外要求 explicit consent + biometric template sole control 原則 [c077]。**111 憲判 13 在獨立監督機制設置上主動援引 GDPR + EDPB + 4 國 DPA** [c098] — 證明 GDPR 不是 Q5 的「外國背景」，而是台灣憲法層次承認的最低參考標準。
<!-- {conceptual:A∩D; temporal:2024; geographic:EU} -->

**[contested]** Home Depot 自助結帳 BIPA 集體訴訟（2024+）是 Q5 最接近台灣餐飲 kiosk 的單一國際先例 — 訴狀核心事實「kiosk 上方鏡頭啟動，綠框顯示掃描中 + 無告示無警告 + 無人工替代」三點同時對映台灣 A∩D 灰區結構 [c073]。BIPA 雙標準：(a)「事前書面知情同意」(b)「公開揭露保留與銷毀政策」、加上 statutory damages $1,000-$5,000/筆，創造 plaintiff 經濟誘因 → 私人 enforcement 強 [c073]。**台灣個資法 §8 告知範圍與 BIPA 接近，但同意形式（書面 vs implied）+ statutory damages（有 vs 無）是兩大關鍵落差** — 修法可借鏡此兩條 implementable 路徑。
<!-- {conceptual:A∩D; geographic:US-IL} -->

**[contested]** 新加坡 PDPC biometric 指引提供「同類監管機構漸進立法」可參考路徑 — 指引明示 scope 排除 commercial inference、留待 future guidance，是亞洲監管機構同類問題的階段性處理範例 [c076]。台灣 PDPC 籌備中可借此 framework 設計逐步函釋路徑：(a) 先發布告知義務具體化函釋（個資法 §8 對 A 區的適用），(b) 後續再處理特種個資範圍修法（§6 修法 future work）。
<!-- {conceptual:A∩D; geographic:SG} -->

**Confidence**: medium — 3 源 strong + 3 源 contested；國際對照本身的 transferability 一向有比較法 caveat。
**Counter-evidence**: EU AI Act 對餐飲 inference 場景的覆蓋有限是必須誠實告知讀者的，把 AI Act 當「EU 已禁餐廳 inference」的 framing 是常見誤讀，本 Finding 已主動防範。

---

## Counter-framing engagement

**[contested]** 本節對應 brief_expanded.yaml `counter_framing_keywords` 的四個 framing：
<!-- {conceptual:A∩D; geographic:TW} -->

- `inference_not_collection` — 業者 framing「inference 不算個資蒐集」遭 111 憲判 13【35】「無還原可能性才脫離個資法」標準大幅削弱 [c098]；vendor 一手 verbatim articulate 為「輪廓辨識 (僅針對性別、人種、外觀)」defensive framing [c108]，**業者不是沉默而是主動採此 framing** — 但「輪廓不算個資」二分**在個資法 §2 第 1 款「直接或間接識別」標準下不能脫離個資法**。**已在 Finding 4 處理（含 c108 vendor framing 三點法律拆解）**。
- `no_storage` — 業者 framing「不存 / 立即刪除」被 c032 雙月 vendor 一手稿「藉由雲端運算，將資料完整回傳台灣總部」一句明文打掉 + c033 BNext 證實 OpenAI / 微軟雲端跨境傳輸 [c032, c033]。**已在 Finding 2 showcase A artifact 流向處理**。
- `no_identification` — 業者 framing「不識別個人 / 匿名」被 111 憲判 13【35】「直接或間接識別」標準大幅削弱 [c098]；c108 vendor 一手「輪廓辨識 ≠ 人臉特徵比對」二分是此 framing 的具體 articulation，在「結合店面 metadata 仍可間接識別」標準下不能脫離個資法。國發會在 111 憲判 13 中陳述同構 framing 已被憲法法庭駁回 [c098]。**已在 Finding 4 處理**。
- `implied_consent` — 業者 framing「使用即同意 / 默示同意」面臨 supply chain 上游 vendor 內部分裂的 partial counter（caveat-tier rescue per Dr7）：SDK 上游 CyberLink（2023）主動承認「需透過用戶『知情同意』」[c045]，業界 best practice 至少在 SDK 行銷層已存在；中游 kiosk 整合商 / 終端餐廳 wording vacuum 之具體 §8 告知形式與責任分層仍待 PDPC 函釋。**已在 Finding 5 處理為 contested-tier 三層 framing 對照段**，不升為主結論。

## What we don't know

- **WiXtar 30+ 品牌名單**：vendor 未具名公布，Drafter 僅能以「雙月 + 金色三麥」為已具名子集；其餘 28+ 品牌身分、各品牌啟用 inference 模組比例皆 unknown。
- **AI Kiosk 留存政策**：兩個 showcase 皆未說明 inference 結果 / 原始臉部影像的留存期、傳輸對象具體名單、是否進會員 profile；vendor 公開資料完整空白。
- **PDPC §6 / §8 函釋全文**：c050 / c051 / c052 PDPC 函釋頁為 js_only access blocked；本研究以 c055 fblaw 律所 + c059 行政院新聞 parallel coverage 替代，但函釋全文若取得可升級 Q4 證據層級。Operator 若可從非 CC 環境取得 JS-rendered 內容可救援。
- **台中市消費爭議 row-level**：c107 因 DNS proxy 失敗未取得，僅 schema-level corroborate；Drafter 已用新北 + 桃園雙縣市 row-level confirmation 結論不阻塞，但跨三縣市對齊仍是缺口。
- **全國層消保會申訴 schema row-level deep-read**：c079 全國申訴統計 + c080 線上申訴系統屬 metadata 層 sourcing；row-level 結構性零是否與新北 / 桃園縣市層完全平行，本研究未做 deep-read 驗證 — 若 operator 後續取得，F7「全國層」claim 可從 metadata-tier 升級為 row-level 雙重 confirm。
- **Edge inference 系統 RAM / cache 留存機制**：F4 [speculative-mechanism] 段所指「多數 edge inference 系統在處理流程中於 RAM / cache 短暫留存原始畫面」屬技術機制推論；需 vendor 系統架構文件、第三方技術稽核報告或學術 benchmark 驗證 — 本研究未取得，列為待補 technical fact。
- **c095 高雄高行 114 簡 216 判決內文**：F7 邊界判例僅以 accepted record metadata 引用，未做 deep-read 取得判決全文 — 行政法院 profiling doctrine 萌芽 wording 強度待 deep-read 確認。
- **8/8 跨媒體 D 軸沉默的對話框架傳染路徑**：vendor → 產業 IT 媒體（CIO/TechNews）→ 商業媒體（BNext/工商時報）→ lifestyle 媒體（Marie Claire）四層 D 軸 framing 一致缺席 — 這個 framing 統一性是 vendor 主動設計還是媒體角度被動沿用，本研究未做溯源分析。
- **桌面觀察 AI 系統實際部署狀態**：金色三麥 vendor 明示「規劃推出」，是否已落地、預定 timeline、與第一階段人臉導購系統的合併部署計畫，公開資料未述。
- **CyberLink vendor framing 在後 EU AI Act 環境的更新**：c045 文章日期 2023，AI Act 通過後（2024）CyberLink 對 emotion recognition 描述是否調整，本研究未取得新版本。
- **counter / primary balance**：本研究 counter=2 theme / primary=7 theme（extract 端 ratio ≈ 1:1.7），c108 信傳媒康惠媚 quote 將「業者側完全沉默」narrow 為「CEO 媒體聯訪有 framing、PR/政策 5 層 wording vacuum」；CyberLink 內部對照 + c108 已盡可能補上 counter；若 Reviewer 認為仍偏向 thesis 方向，可在 review 階段提示 hedge 加強點。
- **[AIO-generated, not vendor-articulated] 三條 vendor「defensive framing」原為 AIO 摘要產出，非 vendor 一手主張**：研究過程中曾接觸三條描述為 vendor 立場的具體 wording — (a)「系統不具備人臉特徵比對的功能」、(b)「無留存影像檔案的行為」、(c)「主動使用手機掃碼登入會員 = 個資法當事人明確同意」。本研究對 operator 提供之原始來源（信傳媒 c108 + Yahoo 報導 + WiXtar 隱私政策 c109 + 雙月食品社官網）進行 fact-check 後，**vendor 一手 primary source 中均未找到此三條 specific wording**。Operator 後續確認三條為 AI Overview / AIO 摘要 over-generation 產出 — 不是 vendor 公開主張。本研究**不採信亦不引用**此三條為 vendor framing 證據。**唯一 confirmed vendor 一手 defensive framing 是 c108 信傳媒康惠媚「僅針對性別、人種以及外觀『輪廓』進行辨識」一句** — vendor 在 CEO 媒體聯訪層的 framing 範圍**比 AIO 摘要呈現的更窄**，只 articulate 了「輪廓辨識」此一二分，**沒有**延伸到「不留存」「不識別」「明確同意」三層。這反而**強化** F3 wording vacuum claim — vendor 在 §8 五要素揭露的真空比原本評估的還深，沒有 AIO 摘要呈現的「完整 defensive narrative」可援引。**Research-integrity note**：本研究在 patch 3 階段透過嚴格 fact-check WebFetch 一手來源避免採信 AIO over-generation；此 episode 是 vendor framing 文獻分析的 cautionary tale — AI 系統(AIO)在沒有 user explicit consent 認證下 fabricate vendor 立場推論，跟本研究主題（AI kiosk demographic inference 未經消費者同意推論身分屬性）是同型 framing 問題。
- **WiXtar 隱私權政策 / 雙月食品社獨立隱私政策的更深層 deep-read**：c109 已 confirm wixtar.com/agreement/privacy 是 generic 不涵蓋 inference、雙月官網 footer deadlinks；但 WiXtar 是否在 metamatch / FAQ / 客戶服務後台另有 inference-specific 告知條款，本研究未追蹤。

## 政策建議（concrete actionable items）

**For PDPC 籌備處**：
- 發布**個資法 §8 告知義務對 A 區 demographic inference 的適用函釋**，明示「站到 kiosk 前的瞬間即啟動 inference」屬蒐集行為、須符 §8 告知五要素；逐項建議告知形式（店面公告 + kiosk 開頭畫面 + 隱私政策三軸）。
- 修法 future work：**§6 特種個資範圍更新**，將「具高度識別性的生物特徵 inference 結果（年齡 / 性別 / 語言 / 情緒推估）」納入；若採「納入 §6 + 書面同意」設計，須評估對 kiosk 場景的實質禁止效果（書面同意實作上極困難）[c054]。
- 借鏡 EU AI Act Art. 5 的「敏感屬性 categorical 風險」邏輯設計子法，將「以生物特徵推斷種族 / 政治 / 性傾向」明文禁止 [c067]。

**For 立委 / 立法院**：
- 將「**事前書面同意 + statutory damages（推定式）+ class action 程序簡化**」三件套納入未來個資法修法討論，借鏡 BIPA enforcement infrastructure [c073]。
- 督促 PDPC 籌備處在 6 年過渡期內優先處理 inference 灰區函釋，不要把 §6 修法無限期延後。

**For 消保處**：
- **更新全國消費爭議申訴 schema**，新增「生物特徵蒐集 / inference / 自動化決策」獨立 category，所需成本極低、benefit 為 Q6 量化的 enabler [c105, c106]；改革對象是「全國共用 schema 框架」而非單一縣市。
- 與 PDPC 籌備處共同制定 inference 場景的「告知 / 選擇 / 撤回」三層建議標準，發布 industry guidance。

**For 消基會 / NGO**：
- 將「無告示 + 無人工替代」的雙月 / 金色三麥 case 作為示範性個案調查，補上 TAHR 立場層之外的量化案例層 [c081, c082]。
- 仿 Home Depot 案 plaintiff 模式設計告知缺失的民事訴訟模板，創造私人 enforcement 樣本。

## Source index

| cid | Title | URL |
|---|---|---|
| c032 | 全球唯一 3-in-1 AI Kiosk 攜手米其林必比登「雙月食品社」打造 AI 全自動餐廳 | https://www.wixtar.com/about/news/26 |
| c033 | 佳世達子公司推 AI 點餐機!2 大神功能搞定外國旅客（數位時代 BNext） | https://www.bnext.com.tw/article/79340/benq-wixtar-aikiosk |
| c037 | WiXtar 2026 餐飲 AI 趨勢攻略 | https://www.wixtar.com/about/blog/18 |
| c038 | 星益欣 × 金色三麥 AI 餐酒實驗室（TechNews 2025/05/21） | https://finance.technews.tw/2025/05/21/ai-wine-lab |
| c041 | 【影】人臉導購與桌面偵測 金色三麥端出 AI 餐酒新體驗（CIO Taiwan） | https://www.cio.com.tw/93910/ |
| c042 | AI 比朋友更懂你?金色三麥信義「二代酒窖店」玩 AI 調酒師（Marie Claire） | https://www.marieclaire.com.tw/lifestyle/taste/88285/lebledor-brewery-ai |
| c044 | CyberLink FaceMe SDK 產品頁 | https://tw.cyberlink.com/faceme/ |
| c045 | Reinventing the Restaurant Experience with AI Facial Recognition（CyberLink FaceMe insights） | https://tw.cyberlink.com/faceme/insights/articles/220/reinventing-restaurant-experiences-through-facial-recognition |
| c046 | 拍檔科技 — 30% 連鎖餐飲市占 POS + member 推薦 | （vendor 一手頁面） |
| c047 | Berry AI — 廚房 inventory + 人計數 operations analytics | （vendor 一手頁面） |
| c049 | 智取櫃人臉辨識取餐完整指南（銓幻元 MCS） | https://www.mcstation.ai/blog/ai-face-recognition-smart-cabinet-guide |
| c053 | 個人資料保護法本文（2025/11/11 修法後現行版本） | https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021 |
| c054 | 個人資料保護法 §6 — 全國法規資料庫 | https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=I0050021&flno=6 |
| c055 | fblaw 律所 2025/11/25 修法 newsletter | https://www.fblaw.com.tw/ |
| c059 | 政院通過 PDPC 組織法草案及個資法部分條文修正草案 | https://www.ey.gov.tw/Page/9277F759E41CCD91/747cda78-926f-4205-99b3-1a735fc1b97b |
| c067 | EU AI Act Article 5 — Prohibited AI Practices | https://artificialintelligenceact.eu/article/5/ |
| c073 | Home Depot Faces Illinois Class Action Over Alleged Facial Recognition at Self-Checkout | https://idtechwire.com/home-depot-faces-illinois-class-action-over-alleged-facial-recognition-at-self-checkout/ |
| c076 | 新加坡 PDPC biometric 指引 | https://www.pdpc.gov.sg/ |
| c077 | EDPB Opinion 11/2024 機場 FR | https://www.edpb.europa.eu/ |
| c079 | 行政院消費者保護會 — 受理消費者申訴及調解案件之統計 | https://cpc.ey.gov.tw/Page/C116BB7EE606AA23 |
| c080 | 行政院消費者保護會線上申訴系統 | https://appeal.cpc.ey.gov.tw/ |
| c081 | TAHR「你的臉孔不是你的臉孔」 | https://www.tahr.org.tw/ |
| c082 | TAHR「下一張臉在哪 (1)」— 2014+ 零售 FR 縱貫錨點 | https://www.tahr.org.tw/ |
| c095 | 高雄高等行政法院 114 年度簡字第 216 號判決（兒少福利與權益保障法；含 profiling 論述） | https://judgment.judicial.gov.tw/FJUD/data.aspx?ty=JD&id=KSTA%2c114%2c%e7%b0%a1%2c216%2c20260121%2c1&ot=in |
| c096 | 司法院裁判書系統「餐飲場景 inference 型生物特徵蒐集判決」negative finding | https://judgment.judicial.gov.tw/ |
| c097 | 釋字第 603 號 — 戶籍法捺指紋始核發身分證規定違憲 | https://cons.judicial.gov.tw/docdata.aspx?fid=100&id=310902 |
| c098 | 111 年憲判字第 13 號 — 健保資料庫案 | https://cons.judicial.gov.tw/docdata.aspx?fid=2200&id=343001 |
| c105 | 新北市消費爭議第 1 次申訴案件群組分析（opendata dataset_id=124152） | https://data.gov.tw/dataset/124152 |
| c106 | 桃園市政府每年度消費爭議申訴案及調解案商品類型分析表（opendata dataset_id=149422） | https://data.gov.tw/dataset/149422 |
| c107 | 台中市消費爭議事件處理（opendata dataset_id=88043；row-level 受 DNS proxy 阻擋） | https://data.gov.tw/dataset/88043 |
| c108 | AI 點餐機可猜測消費者喜好 — 星益欣 CEO 康惠媚 verbatim「輪廓辨識」defensive framing（信傳媒 2024/06/05 李海琪；v1_patch3 supplement） | https://www.cmmedia.com.tw/home/articles/47296 |
| c109 | WiXtar 隱私權政策（undated, generic 不涵蓋 inference）+ 雙月食品社官網 footer 平行 negative finding（v1_patch3 supplement） | https://www.wixtar.com/agreement/privacy |
| c110 | WiXtar YouTube channel vendor 一手 PR 影片（2025-12-15, 3:17）—雙月公園店 2025/10 起部署 VLM 客層辨識/特徵行為分析 + AI 巡店；description text + 影片本體 visual 雙重 D 軸 wording/UI vacuum 確認（v1_patch4 supplement） | https://www.youtube.com/watch?v=9mGAXdgNm04 |
