# Segmenter index — ai-kiosk-consent-tw

Deep-read budget: 27 / Prioritized: 27 (of 92 accepted)

研究焦點:**A∩D 灰區** — inference 型部署 × 同意機制 axis 的交集。深讀以 A 區
(demographic inference) + D 軸 (告知/選擇/撤回) 為主,B 區 (身分比對)、C 區
(POS+會員 PII) 各列 1 條 contrast extract 確保 Drafter 不會把 B/C 算進 A。

關鍵發現:
- **Q1b 兩 showcase 一手 wording 已俱備** (c032 雙月 + c041 金色三麥) + 多個 vendor/媒體 cross-check
- **Q2/Q3 D 軸完全缺席** structurally cross-confirmed across vendor pages (c032/c041)、tech press (c033/c038)、lifestyle media (c042)、vendor thought leadership (c037)、行政院新聞 (c059)、律所 newsletter (c055)
- **Q4 framing 對照 SHARPEST evidence**: c045 (CyberLink 自家主動承認知情同意) vs c032/c041 (WiXtar/星益欣 完全沉默) — 同類 vendor 不同 framing 的 internal split
- **Q4 憲法 spine 已建構**: c097 釋字 603 + c098 111憲判13 兩判
- **Q5 國際對照三軸俱備**: c067/c068/c069 EU AI Act Art. 5 + c073 BIPA Home Depot + c076 SG PDPC + c077 EDPB Opinion + c070 EC guidelines
- **Q6 結構性零三方確認** ⚡:司法零 (c096 Collector 已確認 35 judgments 0 餐飲 inference) + 申訴 schema 零 (c105+c106 row-level 確認、c107 schema-level corroboration) + framing 層零 (c055 律所 + c059 行政院 newsletter 都未提 inference 灰區)
- **Q1a 歷史錨點**: c082 TAHR 2014 retail FR 部署 (7-11/全家/萊爾富/星巴克/屈臣氏)

## Deep-read (depth 1 — must;qs=5 全數 + 載重 framing 對照 + 憲法/法律 spine + Q6 quantitative)

### A 區 vendor 一手 + Q1b showcase
- **c032** [conceptual: A]: WiXtar 雙月案例 vendor 一手新聞稿 — A 區部署 + D 軸 wording vacuum 雙重 evidence。
- **c033** [conceptual: A]: 數位時代 BNext WiXtar 雙月獨立報導 — 「30+ 餐飲品牌、超過 1000 台 AI Kiosk」規模天花板 + OpenAI/微軟 雲端技術鏈具名。
- **c037** [conceptual: A]: WiXtar 2026 餐飲 AI 趨勢攻略 — vendor thought leadership 把 VLM/inference 列為「七大模組」標配,framing 層 D 軸 vacuum。
- **c038** [conceptual: A]: TechNews 金色三麥 × 星益欣原始報導 — 部分 wording 取得但 accepted 摘要的「八維智能/典通客層」未在 WebFetch 確認,標 access_status=partial。
- **c041** [conceptual: A,D]: CIO Taiwan 金色三麥詳細報導 — Q1b 金色三麥 case 主 wording source。
- **c042** [conceptual: A]: Marie Claire 金色三麥消費者體驗 — 「拍一張照片,AI 推算性格特質」consumer-facing flow 主 wording。

### D 軸 framing 對照 SHARPEST evidence
- **c045** [conceptual: A,D]: CyberLink FaceMe 餐飲應用 marketing — **載重**: vendor 自家主動承認「人臉辨識需知情同意」「用戶有權隨時取消/刪除」— framing 對照 c032/c041 的 SHARPEST counterpoint。

### 法律 spine — 個資法本文 + 修法
- **c053** [conceptual: A,D]: 個資法本文 (2025/11/11 修法後現行版) — 全文 + 修法歷程。
- **c054** [conceptual: A,D]: 個資法 §6 特種個資定義 — **人臉/聲紋未列入** — Q4 法律屬性核心條文。
- **c055** [conceptual: D]: fblaw 律所 newsletter 2025/11/25 — 修法核心為 PDPC 組織建構,不直接觸及 §6 inference 灰區;parallel 替代 c050/c051/c052 PDPC js_only。
- **c059** [conceptual: D]: 行政院 PDPC 組織法 + 個資法修正草案新聞 — 立法理由「建立 AI 全面應用時代資料治理」載重 wording + 6 年過渡期。

### 憲法 spine — Q4 比例原則
- **c097** [conceptual: A,D]: 釋字第 603 號 (2005 指紋身分證) — 資訊隱私權憲法上保護 spine。
- **c098** [conceptual: A,D]: 111 憲判字第 13 號 (個資法 §6 I 4) — 事後控制權 + 比例原則。

### 國際對照 Q5
- **c067** [conceptual: A,D]: EU AI Act Article 5 禁令原文 — emotion recognition (workplace/edu) + biometric categorisation 禁令。
- **c068** [conceptual: A,D]: EC AI Act Service Desk Art. 5 官方解析。
- **c069** [conceptual: A,D]: FPF Red Lines 對 emotion recognition 禁令範圍分析 — 商業場合是否涵蓋的細部討論。
- **c073** [conceptual: A,D]: Home Depot self-checkout BIPA 集體訴訟 — Q5 最接近台灣餐飲 kiosk 的國際先例。
- **c076** [conceptual: A,D]: 新加坡 PDPC biometric 指引 — 「scope 排除 commercial inference,留待 future guidance」 — 同類監管機構漸進立法路徑。
- **c077** [conceptual: A,D]: EDPB Opinion 11/2024 機場 FR — GDPR Art. 9 explicit consent + biometric template sole control 原則。

### 對照背景 (B/C contrast,確保 Drafter 不會把 B/C 算進 A)
- **c049** [conceptual: B]: 銓幻元 MCS 智取櫃 — 99% 相似度比對既有資料庫 → B 區身分比對,**not to be counted toward A**。
- **c046** [conceptual: C]: 拍檔科技 — 30% 連鎖餐飲市占,但功能為 POS + member 推薦 (C 區),**not to be counted toward A**。
- **c047** [conceptual: C]: Berry AI — 廚房 inventory + 人計數 (operations analytics),**not to be counted toward A**。

### Q1a 歷史錨點 + NGO 立場
- **c081** [conceptual: A,D]: TAHR「你的臉孔不是你的臉孔」 — NGO 立場,push-back「匿名化即不算個資」「inference 不算」業者 framing;Gatekeeper 標為 G4 balance 1 counter。
- **c082** [conceptual: A]: TAHR「下一張臉在哪 (1)」 — **載重**: 至少 2014 年起 7-11/全家/萊爾富/星巴克/屈臣氏結帳櫃台上方 FR 「搜集客戶族群資料投放廣告」 — Q1a 10+ 年歷史錨點,但需與 2024+ kiosk 部署**分開計算**。

### Q6 quantitative 結構性零(twinkle-hub MCP 503,改 CSV API direct)
- **c105** [conceptual: A,D]: 新北市消費爭議申訴群組分析 12 年縱貫 — schema 18 個 categories + residual buckets,**無 biometric/個資/inference** 獨立 category;113 年 services_others_quantity 2,235 件 (10 年成長 5 倍) 是 inference 投訴的隱形池。
- **c106** [conceptual: A,D]: 桃園市消費爭議申訴分析 — 25 個 zh-TW 具名 category + 「其他」,113 年「其他」823 件 (18%);第二縣市 row-level confirmation。
- **c107** [conceptual: A,D]: 台中市消費爭議事件處理 — 訪問被 JSON API DNS / proxy 阻擋,僅 schema metadata level corroboration;operator 可從另環境救援。

## Fast-skip — snippet-layer usable (Dr3 secondary evidence)

按 brief Q 對映分組,所有以下記錄 `accepted.jsonl` 含具實質內容的摘要,Drafter 在 Dr3 規則下可作 secondary evidence 引用 (cap 至 contested tier,必須註明依摘要 sourcing 未經 deep-read 一手驗證)。

### A 區 vendor 補充 (Q1b 二手描述)
- c034: (`access_status: ok`, `snippet_status: usable`) — https://www.techbang.com/posts/115914-... — Computex 2024 雙月 × WiXtar 展示報導;摘要含「全自動餐廳」context;Drafter 可作 Q1b 雙月 case 補述。
- c035: (`access_status: ok`, `snippet_status: thin`) — iDS 安防媒體對雙月案的描述;摘要短 (27 字) 無實質增量;c032 + c033 已覆蓋。
- c036: (`access_status: ok`, `snippet_status: usable`) — WiXtar Kiosk 產品介紹頁;摘要點出「Q7 隱私政策實體分析素材」 — Drafter 在 Q7 vendor 評價可引摘要層描述,實際隱私政策 wording 未 deep-read。
- c039: (`access_status: ok`, `snippet_status: thin`) — 工商時報金色三麥獨立報導;摘要 24 字短,與 c041/c042 內容平行,deep-read 邊際 0。
- c040: (`access_status: ok`, `snippet_status: usable`) — foodnext 食力金色三麥報導;摘要點明「§6b recon 核心引用源之一」 — Drafter 可引摘要作 Q1b 金色三麥次要佐證。
- c043: (`access_status: ok`, `snippet_status: thin`) — 今周刊金色三麥商業背景;與本研究 A∩D 核心問題距離較遠 (商業敘事為主)。
- c044: (`access_status: ok`, `snippet_status: usable`) — CyberLink FaceMe SDK 產品頁;摘要載「age & gender detection for fast-food restaurants」 — Drafter 在 Q1a 廠商分析 + Q7 SDK 上游分析可引摘要層作 CyberLink 產品線 secondary evidence。

### A 區 B/C 對照補充
- c048: (`access_status: ok`, `snippet_status: usable`) — 頂呱呱劍潭店;摘要描述「常客 3 個月再次來訪會被識別並詢問是否點上次餐點」 — 屬 B 區身分比對 (常客識別),Drafter 在 Q1a 區分軌可引摘要層作 B 區補充對照,但不能算進 A 區。

### D 軸 / 法律分析補充
- c050: (`access_status: js_only`, `snippet_status: usable`) — PDPC 第 6 條行政函釋 (js_only) — accepted 摘要描述 PDPC 對第 6 條的見解;Drafter 可引摘要,但實質函釋全文未取得;operator 可從非 CC 環境 fetch JS-rendered 內容救援。
- c051: (`access_status: js_only`, `snippet_status: thin`) — PDPC 第 2 條函釋 (js_only);摘要 27 字短,與本研究核心問題距離較遠。
- c052: (`access_status: js_only`, `snippet_status: thin`) — PDPC 第 8 條函釋 (js_only);摘要 19 字短;c055/c059/c060 律所 newsletter parallel coverage 已替代。
- c056: (`access_status: js_only`, `snippet_status: thin`) — PDPC 2025/11/11 修法公告 (js_only);摘要 32 字,c055 + c059 + c060 三條 newsletter 已 parallel cover。
- c057: (`access_status: ok`, `snippet_status: usable`) — Atsumi & Sakai 日系律師 2025 修法 newsletter (PDF);摘要載「日系律師事務所 2026/03/13 newsletter」 — Drafter 在 Q4 跨國 law firm 觀點對照可引摘要。
- c058: (`access_status: ok`, `snippet_status: thin`) — 廉貞律所 2025 修法解析;摘要 30 字短,c055 + c060 已 parallel cover。
- c060: (`access_status: ok`, `snippet_status: usable`) — 理律法律事務所 2025/11/11 修法逐條解析;摘要短但 source 權威,Drafter 在 Q4 修法分析可引摘要層作 c055 補強。
- c061: (`access_status: ok`, `snippet_status: usable`) — 理律對 PDPC 籌備處預告施行細則 + 三項子法草案;摘要點明「修法後實際運作框架」 — Drafter 在 Q4 / Q7 政策建議可引摘要層作子法 timing 補述。
- c062: (`access_status: ok`, `snippet_status: usable`) — hsu.legal 律師事務所對人臉辨識規範綜合解析;摘要點明「機場/商業場所/告知同意三軸」 — Drafter 在 Q4 / Q5 商業場所 framing 可引摘要層。
- c063: (`access_status: ok`, `snippet_status: thin`) — 網管人雜誌「面子之爭」;摘要 27 字短。
- c064: (`access_status: ok`, `snippet_status: thin`) — 高律師事務所「淺談個資法 (六)」;摘要 20 字短。
- c065: (`access_status: ok`, `snippet_status: thin`) — 極憲焦點「刷臉行不行」;摘要 15 字短。
- c066: (`access_status: ok`, `snippet_status: usable`) — 雇主以生物特徵作出勤管理分析;摘要點明「虹膜雖非特種個資但具高度識別功能」邏輯 — 對 PDPC 籌備處引虹膜為例的論證邏輯 (brief F4 seed) 直接相關,Drafter 在 Q4 可引摘要層作此論證的 律師 layer。

### 對照背景 / 國際輿論
- c085: (`access_status: ok`, `snippet_status: usable`) — 央廣「小心你的臉」對商場校園 FR 部署現況綜合報導;摘要點明「直接觸及 Drafter Q1a/Q2 場景描述」 — Drafter 在 Q1a 商場 context 補充可引摘要層。
- c087: (`access_status: ok`, `snippet_status: usable`) — 聯合報對人臉辨識比例原則的法律觀點;摘要 20 字短但 framing「比例原則」是 Q4 核心切點 — Drafter 在 Q4 可引摘要層作媒體層 legal commentary。
- c083: (`access_status: ok`, `snippet_status: thin`) — TAHR「下一張臉在哪 (2)」 — 風險論述,c081 + c082 已覆蓋 NGO 核心立場。
- c084: (`access_status: ok`, `snippet_status: thin`) — TAHR 公部門 FR 側記 — 公部門場景非本研究商業 kiosk 核心。

### 國際 Q5 補充 (qs=4 academic + industry)
- c070: (`access_status: ok`, `snippet_status: usable`) — EC 2025/02/04 Prohibited AI Practices Guidelines;摘要點明「解釋 Art. 5 實務適用」 — Drafter 在 Q5 EU AI Act 實務細節可引摘要層。
- c071: (`access_status: ok`, `snippet_status: thin`) — 美國律所 BIPA litigation wave 分析;摘要 28 字短,c072 + c073 已 parallel cover。
- c072: (`access_status: ok`, `snippet_status: usable`) — WilmerHale 2024 BIPA 年度回顧;摘要 40 字含 trends — Drafter 在 Q5 BIPA enforcement trend 可引摘要。
- c074: (`access_status: ok`, `snippet_status: thin`) — CCPA biometric 解析 (commercial law firm);摘要 21 字短。
- c075: (`access_status: ok`, `snippet_status: thin`) — 加州 DOJ CCPA 官方頁;摘要 20 字短,只能作 source authority pointer 不能引實質 wording。
- c078: (`access_status: ok`, `snippet_status: usable`) — EDPB biometrics 文件總集;摘要點明「對 remote biometric identification 與 biometric categorisation 在公開空間的禁令呼籲」 — Drafter 在 Q5 EDPB 立場可引摘要層作 c077 補強。

### 司法判決 (4 判 + 1 totals)
- c092: (`access_status: ok`, `snippet_status: usable`) — 最高法院 114 台上 5166 加重詐欺;摘要含人臉辨識**定義 wording**「將臉部影像與資料庫中之臉部資料進行分析比對且驗證身分」 — Drafter 在 Q4 法律屬性 (identification 而非 categorisation) 拆解可引摘要層作司法定義 evidence。
- c093: (`access_status: ok`, `snippet_status: usable`) — 憲判字 115 審裁 431 雇主人臉辨識記錄員工出勤;摘要點明「識別型場景非餐飲 inference」 — Drafter 在 Q4 法律屬性 cross-context 可引摘要層作 employment-context 對照。
- c094: (`access_status: ok`, `snippet_status: usable`) — 北高行 113 地訴 195 勞基法生物特徵出勤紀錄;摘要點明「勞動法承認生物特徵作為識別型工具」 — Drafter 在 Q4 / Q5 employment exception 可引摘要層。
- c095: (`access_status: ok`, `snippet_status: usable`) — 高高行 114 簡 216 兒少法生物特徵 profiling 論述;摘要含「自動化資料處理、特徵分析、行為定位、強制身份核實、資訊過濾和大規模監視等對兒童風險」— Drafter 在 Q4 / Q5 兒童 cross-context 可引摘要層 (注意:餐飲場景未必排除兒童,可作 special consideration)。
- c096: (`access_status: ok`, `snippet_status: usable`) — 司法院裁判書系統「餐飲場景 inference 型生物特徵蒐集判決『無相關案例』總結」 — **Collector 一手 negative finding,Q6 司法零的核心 evidence**;Drafter 在 Q6 結構性零的第一軸即引此 record (摘要層即足夠 supportive)。

### 法規補充
- c088: (`access_status: ok`, `snippet_status: usable`) — 個資法施行細則 (PCode I0050022);摘要點明「配合修法將另案修正」 — Drafter 在 Q4 / Q6 修法 timing 可引摘要層。
- c089: (`access_status: ok`, `snippet_status: usable`) — PDPC 籌備處組織規程 (PCode I0000114);摘要點明「2023/12/05 成立」 — Drafter 在 Q4 PDPC timing 可引摘要層。

### 行政院消保處
- c079: (`access_status: ok`, `snippet_status: thin`) — 行政院消保會全國申訴統計索引頁;摘要 22 字短,實際數據要點進 detail page 抓 — 本 session 未深讀 detail page (Q6 已由 c105+c106+c107 三縣市 dataset 充分量化結構性零)。
- c080: (`access_status: ok`, `snippet_status: thin`) — 消保會線上申訴系統 — 是 portal 非數據 source,摘要 10 字。

### Opendata 法律 Q&A datasets (背景查詢工具,非直接 evidence)
- c099-c104: opendata datasets (個資法 Q&A / GDPR / Global CAPE) — Collector 已標為背景查詢工具,Drafter 不直接引用 row-level,作為 Q4 / Q5 法律問答查詢的「source authority pointer」即可。Twinkle-hub MCP 此 session 持續 503,operator 若需 row-level data 可從另環境試 MCP 或直接 download CSV/JSON。

## Fast-skip — no usable evidence (excluded from primary evidence pool)

### qs=3 EN academic 背景 (Q5 framing material,非台灣 empirics)
- c002: (`access_status: ok`, `snippet_status: thin`) — New Jim Crow (DOI 10.26443) — 國際 framework 論文;非台灣 specific。
- c006: (`access_status: ok`, `snippet_status: usable`) — Demystifying the Draft EU AI Act (Veale et al.) — EU AI Act 立法背景;C5 國際可比背景,Drafter 在 Q5 EU AI Act timing 可酌引摘要。
- c008: (`access_status: ok`, `snippet_status: thin`) — Global governance of AFR (Almeida et al.) — 國際 framework 綜論;非載重。
- c009: (`access_status: ok`, `snippet_status: thin`) — Human Rights Impact with AI — 國際 high-level;非載重。
- c010: (`access_status: ok`, `snippet_status: thin`) — Neuromarketing / neuro-rights — 國際 framework;邊緣相關。
- c011: (`access_status: ok`, `snippet_status: thin`) — Protection of rights when using FR (Heliyon) — 國際 framework;非台灣。
- c013: (`access_status: ok`, `snippet_status: usable`) — Restricting Data Sharing and Collection of FR Data by Consent (Khan et al.) — 系統分析方法論;Drafter 在 Q5 consent design methodology 可酌引摘要。
- c014: (`access_status: ok`, `snippet_status: thin`) — Face, FRT and personal privacy — 國際 framework。
- c015: (`access_status: ok`, `snippet_status: thin`) — Saving Face — 國際 ACM 論文。
- c016: (`access_status: ok`, `snippet_status: thin`) — Should Biometric Be Protected Under Federal Privacy Statute — 美國 federal 提案,Q5 邊緣。
- c017: (`access_status: ok`, `snippet_status: thin`) — Biometric Privacy + Employment Law (UIC) — Q5 employment context,c066/c094 已 parallel cover。
- c021: (`access_status: ok`, `snippet_status: thin`) — Facial recognition technology legal perspective — 國際 framework。
- c022: (`access_status: ok`, `snippet_status: thin`) — Legal Firewall under Algorithmic Panopticon — Chinese context,Q5 邊緣。
- c026: (`access_status: ok`, `snippet_status: thin`) — Transparency around FRT in law enforcement — law enforcement context,本研究排除。
- c027: (`access_status: ok`, `snippet_status: thin`) — Privacy-Enhancing Face Biometrics Survey — 純技術 survey。
- c028: (`access_status: ok`, `snippet_status: usable`) — Ethics of Emotion in AI Systems (Stark & Hoey) — Q5 emotion recognition ethics framing 可酌引摘要層作 Q5 補述。
- c030: (`access_status: ok`, `snippet_status: thin`) — European risk-based approaches — EU constitutional framing,非直接 Q5 載重。

### qs=2 法規 (低載重)
- c090: (`access_status: ok`, `snippet_status: thin`) — PDPC 籌備處編制表 (PCode I0000115) — 純行政編制,無實質。
- c091: (`access_status: ok`, `snippet_status: thin`) — PDPC 籌備處辦事細則 (PCode I0010101) — 內部運作規範,Q4 / Q6 邊際 0。
- c104: (`access_status: ok`, `snippet_status: thin`) — Global CAPE 參與名單 — 純國際合作 metadata,非載重。

## v1_patch3 post-pipeline supplements (2026-05-27)

新增 2 個 extracts 接續 v1 hand-edit patch 1 (F4+F7) + patch 2 (F5 三層 vendor 結構) 後,operator 提供 vendor framing 描述觸發的 fact-check 結果:

- **c108** [conceptual: A,D]: 信傳媒 cmmedia.com.tw/home/articles/47296 (2024-06-05 李海琪) — **載重**: 星益欣執行長**康惠媚**媒體聯訪 verbatim quote「**因為台灣市場對於隱私個資問題較為敏感**,因此目前所謂的將消費者分類,**僅針對性別、人種以及外觀（服裝）這種『輪廓』進行辨識**」。**首個** confirmed vendor 一手 defensive framing — 推翻原 F3「業者用沉默而非辯論」的全稱描繪;narrow F3 wording vacuum 至「case-study / 趨勢攻略 / CIO 報導 / Marie Claire / 隱私政策 5 層 wording vacuum;CEO 媒體聯訪層 vendor 有 defensive framing」。F4 法律拆解現可直接 ENGAGE vendor 一手 framing 而非 deduce from silence。「人種分類」對應 EU AI Act Art. 5(1)(g) 6 類敏感屬性禁制清單之一,是國際對照 sharpest 違規類別。
- **c109** [conceptual: D]: wixtar.com/agreement/privacy (undated) + 雙月食品社 moonmoonfood.com footer deadlinks — WiXtar 隱私權政策**存在**但內容是電商會員 / cookies / 信用卡範圍的一般政策,**完全不涵蓋 AI Kiosk / 人臉辨識 / 生物特徵 / demographic inference / 影像處理 / 即時運算**。個資法 §8 五要素只完成蒐集者+目的+項目三項,期間/對象/方式/權利/不提供影響未明確。雙月食品社官網 footer「隱私條款 | 條款及細則」字眼但**未提供可點擊 URL**(純文字 deadlinks)。F3 narrower-scope wording vacuum 在「隱私政策層」+「終端餐廳官網層」的 negative-finding 雙重佐證。
- **c110** [conceptual: A,D]: WiXtar YouTube channel 一手 PR 影片 (2025-12-15, 3:17, 984 views) — **載重**: 雙重 evidence layer。(a) Description verbatim: 雙月食品社**公園店**(具體分店) 自 **2025/10** 起部署「VLM 影像分析:客層辨識、**特徵行為分析**」+「影像辨識出餐」+「AI 巡店系統」— vendor 自家用「特徵行為分析」wording 正面矛盾 patch 3.1 修正的 AIO-hallucinated「無人臉特徵比對」description, F4 強化。(b) Visual observation (operator 2026-05-27): 影片本體 3:17 內畫面**看不出同意介面、機器周邊看不出告示與指示**, F3 wording vacuum 首次以 visual modality 補上 D 軸 UI silence;但 caveat: 此為 vendor PR 影片視覺檢視, 不等於現場 fieldwork (operator 未親訪雙月公園店)。F3 wording vacuum 從原 5 個 PR 發布管道擴張到**10 個 publication-channel / modality layers cross-confirmed**;F1 部署事實 specific 化 (雙月公園店 2025/10 起 7 個月);F2 showcase artifact 流向擴張 (VLM / AI 巡店);F5 vendor 自家發布管道分裂第三軸補上。

## Operator overrides needed

- **c105/c106/c107 opendata via twinkle-hub MCP** — gateway 此 session 持續 503。本 Segmenter 改以 data.gov.tw + 縣市 CSV API direct download 取得 c105 (新北市) + c106 (桃園市) row-level data;c107 (台中市) JSON API DNS proxy failure,僅取得 schema metadata。若 operator 想 row-level confirm 台中 dataset,可:(a) 自家環境試 `curl https://newdatacenter.taichung.gov.tw/api/v1/no-auth/resource.download/<resource_id>`,(b) 等 twinkle-hub MCP 恢復後 `mcp__twinkle-hub__opendata-query_rows(88043, limit=30)`。
- **c038 TechNews 金色三麥**: accepted 摘要描述「八維智能商品推薦模型/典通客層辨識模組」精確 wording,但 WebFetch (含 redirect follow) 未確認此 wording 出現於回傳內容 — 可能 CDN cache 版本差異或 dynamic content。Drafter 引用此精確 wording 應回到 accepted snippet (snippet_status: usable, contested tier per Dr3);若需 verbatim 一手驗證可請 operator 從另一環境 (非 Claude Code) 重抓 finance.technews.tw/2025/05/21/ai-wine-lab 原始版本。
- **c050/c051/c052/c056 PDPC js_only** — Gatekeeper 已標 qs=3 + segmenter_route_dr3;本 Segmenter 用 c055 + c059 + c060 律所/行政院 parallel coverage 替代。若 operator 可從 non-CC 環境 JS-rendered fetch PDPC 函釋全文,Drafter 可升級 Q4 函釋層 evidence (目前依賴律所 + 行政院 framing source)。
- **opendata c099-c103 法律 Q&A datasets** — twinkle-hub MCP 503,本 session 未取得 row-level;這些 datasets 對 Drafter 主要為「source authority pointer」(讓 Drafter 知道 NDC / 法務部 有 Q&A 結構化資料庫存在),非直接 evidence。Drafter 若需 specific Q&A 內容可請 operator MCP 復原後 query 或從 data.gov.tw 直接 download CSV。
