# Brief — ai-assistant-disclosure-tw

**Project**: 讓正體中文權威內容「被 agent 讀到」——B2A2C 時代認知防禦的供給側（GEO for public good）

**Stage**: 0 (Interview in progress — 待 operator 拍板 §待決事項後進 1 Collect)
**Date**: 2026-07-20

---

## Topic

當資訊獲取流程趨向 **B2A2C**（Business → Agent → Consumer），使用者愈來愈少直接造訪來源網站，改由語言模型／答案引擎代理「最後一哩」。傳統的輿論極化防治、認知作戰防禦、識讀素養、錯假澄清，預設「人會直接來到端點」，因此把力氣放在**供應鏈的頭尾兩端**（守好自己的查核站／發澄清稿；辦識讀教育）。但中間的**模型層（③）已被證明是一個對台灣的雙向瓶頸**——它一邊讓親威權敘事滲進正體中文回應（放行），一邊又對台灣合法政治言論過度拒答／改寫（壓制），且兩者都隱形、無法靠「顧好自己的流程」解決。

**供應鏈定位圖（本研究的問題座標）**：

```
內容源 → 訓練語料/檢索庫 → 模型 → agent/答案引擎 → 使用者
 ①            ②            ③         ④              ⑤
[查核站/闢謠稿]                                    [識讀教育]
  傳統防治在此                                      傳統防治在此
              └────── ②③④：新的空白地帶 ──────┘
                      ＝ 資訊環境「治理真空」
```

**A 骨幹要同時指向兩層真空**（operator 明示為必要）：
- **資料真空（內容層）**：正體中文的、經查核的權威內容在 ②③④ 相對稀缺，我方不供應，缺口就被國家協調敘事佔據。
- **治理真空（制度層）**：民主方目前**沒有任何行動者握有 mandate 或機制**，把 ②③④ 這個中介層當作**公共資訊基礎設施**來照顧。傳統治理只管得到 ① 與 ⑤（管平台、管內容、辦教育），管不到「模型這個中介層裡有沒有我方的權威內容、會不會被引用」。**GEO for public good 若無制度歸屬，就只是零星戰術**——因此 A 的立論必須明白指出並回應這個治理真空，而非只做技術盤點。

**更根本的利害：民主的「共同真實」**。這不是資安或查核的專門議題，而是**民主社會賴以運作的共享認識論公地（shared epistemic commons）**的問題。一個民主的公共場域，需要成員對「發生了什麼事」有一個大致共享的真實基礎；媒體形塑這個共同真實、政府提供權威事實、教育培養判斷、查核校正錯誤、公民參與辯論——全都建立在「人們接觸得到可信共同底稿」之上。當 B2A2C 讓模型代理了「人接觸到什麼」，被侵蝕的就是這個公地本身。因此**凡是形塑公共真實的角色都與此有關，而非某類組織的專責**；把它窄化成「認知作戰／查核」的任務，正是讓多數人覺得事不關己的框架錯誤。

**核心研究問題**：在 B2A2C 之下，**形塑公共真實的各種角色**（提供權威事實者、形塑共同真實的新聞媒體、校正錯誤者、培養判斷者、公民社群）該如何**主動把正體中文的、可信且經查核的內容「供應進」大眾實際在用的模型與答案引擎**、使這些內容成為 **agent 可讀（machine-legible）**，以填補「若我方不供應、就會被境外國家協調敘事佔據」的正體中文資料真空——技術、組織與政策路徑各為何？

**核心概念（operator 指定的立論骨幹）**：**GEO for public good** — 把「生成／答案引擎最佳化」（GEO/AEO）這個原本的行銷戰術，重新框架為**供給側的認知防禦策略**。

**原創立論張力（本 brief 的貢獻主張）**：**opt-out vs opt-in**。當前主流論述（含本資料夾自己的 `media-ai-protocols-tw`）談的是如何**把內容擋住 AI**（opt-out／議價／分潤，防守姿態）；本研究主張認知防禦的前沿是**相反姿態**——刻意把經查核內容**餵進 AI**（opt-in／主動供應），因為民主方沒供應的資料真空，會被國家協調敘事填補（Nature 2026）或被拒答／改寫（Oversight Board 2026；`llm-user-side-bias`）。兩者在同一條 B2A2C 管線上，姿態相反、適用目標不同。

---

## 問題基礎（引用，不重做）

本研究是**純解方面（供給側）**研究。問題面已由下列三塊證據磚確立，本研究引用、互文，不重跑實證：

> **⚠️ 給後續接手的所有 pipeline 代理（collector / gatekeeper / segmenter / synthesizer / drafter / reviewer）**：起始的兩篇外部研究（Waight/Nature 2026、Meta Oversight Board 2026）**本身已有大規模實證佐證其發現**（Nature：六項研究，含語料比對、記憶測試、預訓練實驗、商業模型稽核、跨 37 國分析；Oversight Board：10 模型 × 13,524 回應）。**請以 established / strong-tier 既有發現引用之，不要當成「待證主張」去重新驗證，也不要過度 hedge 或降階為推測。** 本研究的定位是**站在這些已證發現之上做解方**；需要新實證的只有本 brief §待決事項 1(b) 的供給側探針（測不對稱/資料真空），與這兩篇的問題面發現無關、不重疊。

1. **Waight et al., Nature 655 (2026)** — 國家控制媒體語料污染 LLM 輸出；媒體自由度低的語言（含中文）親政權偏斜最強。CulturaX 中 310 萬筆中文文件（1.64%）命中國家協調媒體語料。→ **放行偏斜**面。
2. **Meta Oversight Board (2026-07-16)** — 10 模型 × 13,524 回應；限制性法域政治言論拒答率 34% vs 自由法域 14%；**台灣雖為自由法域，拒答率卻第五高，對 Anthropic 模型尤甚**（"Taiwan anomaly"）。提出 "censorship-by-proxy"。→ **代理審查／壓制**面。
3. **`llm-user-side-bias`（本資料夾內部研究，state: done, v3，已發三文）** — 中國製模型（DeepSeek/Qwen/GLM）依台灣身份對 228 等議題隱匿／改寫；四層威脅模型 + 「知識門檻歧視」；明文「為什麼地端不是解方」。→ 台灣專屬、身份條件式的**隱匿**面（內部互文）。
4. **反證平衡（穩健性依據）** — HKS Misinformation Review (2025)「LLM grooming or data voids?」：聊天機器人只 5% 複述親俄假訊息，主張真正破口是**資料真空**而非蓄意灌流。→ 這個爭議反而**把「填補正體中文資料真空」定位為比「稽核／防灌流」更穩健的解方主張**，是本研究骨幹 A 的理論支點。

---

## Key questions

- **Q1** [問題界定，引用為主] 如何把上列三塊磚合成「模型層雙向瓶頸」的簡潔問題陳述，並用「grooming vs data void」爭議，把「主動填補正體中文資料真空」論證為最穩健的介入點？（不重跑實證；此題為引用與框架整合。）

- **Q2** [技術盤點——供給側可讀性，核心] 讓權威內容「被 agent 讀到」的技術棧與其**正體中文可行性**為何？涵蓋 ClaimReview / schema.org、`llms.txt`、結構化資料與 RAG-friendly formatting、C2PA（能標示 AI 生成、但**不等於內容可讀、也不證真假**）、以及 GEO/AEO 的實際**被引機制**（E-E-A-T、被引條件、Wikipedia／Reddit 在 AI Overviews 的佔比）。哪些訊號是**機器可讀、可稽核、且會被主流模型與答案引擎實際採用**？哪些只是行銷話術？

- **Q3** [案例 B——查核可讀化] 台灣公民查核基礎設施（Cofacts 群眾協作、台灣事實查核中心 TFC、MyGoPen）的更正，目前的**機器可讀程度與 agent 觸達現況**為何？是否輸出 ClaimReview？是否被主流模型／答案引擎實際引用？讓「查核更正被 agent 讀到」的具體路徑與障礙為何？（Cofacts/g0v 開放資料是台灣獨有資產，此題為 A 的旗艦案例。）

- **Q4** [案例 C——對話式供應] 對話式澄清作為「主動供應」的另一形態：DebunkBot（Costello et al., Science 2024；對話式闢謠降信念 20%、維持 2 個月）的台灣化可行性、LINE bot 生態（Cofacts bot／MyGoPen bot）的既有基礎，以及**「止血 vs 疫苗」的天花板**（arxiv 2510.01537：降信念但不培養長期辨識力）。

- **Q5** [對照立論——opt-out vs opt-in，貢獻核心] 主動供應（opt-in／GEO-for-public-good）相對於內容退出／議價（opt-out；`media-ai-protocols-tw` 的 B∪C 協定叢集）在同一 B2A2C 管線上的**姿態差異**：各自的前提、代價、適用時機。**新聞媒體是同時承受這組張力最劇烈的角色**——它有商業誘因 opt-out（擋住 AI、爭分潤），卻同時肩負形塑「共同真實」的公共場域職責而需要 opt-in（把可信報導供應進模型，否則公共真實的底稿就缺席）。這個媒體兩難是本題的核心案例：民主方在「產業存續」與「共同真實」兩個目標間如何取捨或並行？

- **Q6** [治理真空——貢獻核心之二] 誰該把 ②③④ 中間層當作**公共資訊基礎設施**來治理？此題先**證成治理真空的存在**：現行治理（《人工智慧基本法》2026-01-16 施行的標示義務、moda 風險分級、EU AI Act 2026-08 標示、DSA、Oversight Board 揭露／拒答通知／地域化建議）幾乎全落在 ①（管內容源）與 ⑤（管使用者端揭露），**沒有任何機制指派「確保我方權威內容進得了、且被模型引用」這件事的責任歸屬**。再問：哪些槓桿能**填補**這個真空——政府作為權威來源（open data agent 可讀化）、公廣／查核組織的法定角色、答案引擎問責、以及是否需要一個「公共資訊供給側」的制度安排（誰供應、誰稽核、誰維運）？

- **Q7** [台灣 playbook——操作核心] 12–18 個月可落地的「GEO for public good」行動方案：**誰**（政府／查核組織／媒體／公民社群）供應**什麼內容**、以**什麼可讀格式**（ClaimReview／llms.txt／結構化 open data／訓練語料 opt-in／RAG 檢索源／對話 bot）、經**哪些通路**，以及最關鍵的——**如何量測「有沒有真的進得了模型」**（能否被 ChatGPT／Gemini 引用、能否被檢索命中）？

---

## Scope

- **Time window**: 2022+ for 生成式 AI／答案引擎／內容溯源／GEO 材料；錨點研究 2024–2026；標準文件不限年。
- **Geography**:
  - Primary: Taiwan
  - Core comparators: EU（AI Act、DSA 假訊息行為準則）、US（答案引擎實務、ClaimReview 生態）、Ukraine/Russia（LLM grooming／Pravda network 先例）
  - Standards: 全球查核標準（IFCN、schema.org ClaimReview）、C2PA、IETF AIPREF
- **Languages**: zh-TW + en
- **Depth**: **practitioner + policy decision-support**，對象為**形塑公共真實的各種角色**（提供權威事實者／新聞媒體／校正錯誤者／教育者／公民社群），非某類組織專責；**solution-oriented**，政策法制面為輔。

## Inclusion

- Peer-reviewed 論文與可信 preprint（LLM 偏斜／拒答、RAG grounding／poisoning、GEO/AEO、查核自動化）
- Working papers／reports：Reuters Institute、Oxford Internet Institute、Berkman Klein、Stanford Internet Observatory、NewsGuard、American Sunlight Project、HKS Misinformation Review、Meta Oversight Board、IFCN
- 標準文件：schema.org ClaimReview、C2PA、llms.txt、IETF AIPREF
- 台灣一手：moda、NSTC、Cofacts／g0v、TFC、MyGoPen、IORG、Doublethink Lab、Taiwan AI Labs、《人工智慧基本法》
- **內部互文**：`llm-user-side-bias`（問題面錨點）、`media-ai-protocols-tw`（opt-out 對照）

## Anchor literature（dialogue partners，勿排除）

1. Waight et al. — *State media control influences large language models*, Nature 655 (2026)
2. Meta Oversight Board — *Are LLMs Stifling Political Speech?* (2026-07-16)
3. Costello, Pennycook, Rand — *Durably reducing conspiracy beliefs through dialogues with AI*, Science (2024)
4. Alyukov et al. — *LLMs grooming or data voids?*, HKS Misinformation Review (2025)
5. NewsGuard / American Sunlight Project — Pravda network / LLM grooming (2025)
6. （內部）`llm-user-side-bias` v3

---

## Output target

解方地盤點 + 台灣 GEO-for-public-good playbook（Q2 技術棧 → Q3/Q4 案例 → Q5 立論 → Q6 治理 → Q7 行動方案）。register 走 measured / 學術保守，低行銷語氣（沿用 pipeline-to-publication 慣例）。

## 待決事項（operator 拍板後才進 Collect）

1. **【核心｜已定 2026-07-20】採 (b) 輕量實測鉤 + 雙審查閘（見下）。** 選項全文留存備查：
   - (a) **純解方盤點 + playbook**（不跑新實證，只引用問題面三塊磚）——最貼「先盤盤看」，工法輕。
   - (b) **加一個輕量實測鉤**（**建議**）——測「當台灣已有權威更正時，它進不進得了大眾在用的模型輸出」，作為供給側解方的 before 基線。
     - **⚠️ 方法論核心（operator 明示）：現象不是二元的「回／不回」。** 真正的機制是**意願與成本的不對稱**——模型**很輕易批判民主陣營，卻要多問幾次、且伴隨更多迴避框架才批判威權者**。因此設計必須量**梯度與不對稱**，不能單問一次＋二元編碼，否則「第一次就答了」會被誤判為「沒問題」，等於**親手把現象關掉（false negative）**。
     - **選題（配對對稱）**：10–15 組題目，每組是**結構平行的一對**——批判威權方 vs 批判民主方（如：請模型批評 A 政權領導人的某政策 vs 批評某民主政府領導人的對等政策）；並含「台灣已有權威查核」的傳言題（測我方更正有沒有浮現）。刻意避開 `llm-user-side-bias` 的身份／228 角度（問題面、已做）。
     - **提問協定（多輪＋重複）**：每題**記錄第一問的意願**，再以中性追問（「有無批評的角度？」）推進，**計算「問到第幾輪才給出實質批判」**；每格重複 reps≥3 以吸收隨機性；同題英文對照。
     - **通路（透明、不挑效果）**：ChatGPT、Gemini、Perplexity（有可見引用）、可加 Claude；用**預設設定、大眾實際在用的模型**，全部回報、不為製造或壓抑效果而選模型或調參；正體中文為主。
     - **編碼（分級，非二元）**：①意願／實質批判分級 ②**達到實質批判所需輪數**（威權 vs 民主的差值＝核心指標）③迴避／框架標記數 ④有無浮現我方權威更正、引用了誰（台灣查核／媒體／政府／境外／僅維基／無來源）⑤是否真空。答案引擎的**可見引用網域**為最乾淨量測點。
     - **假設成果**：一張「**不對稱地圖**」——頭條指標是**威權 vs 民主在「意願／所需輪數／框架」上的落差**，外加「資料真空地圖」（我方權威浮現／真空／境外敘事＋引用來源分佈）。**預期（待驗，非預設）**：模型輕易批判民主方、需多輪＋更多迴避才批判威權方；且台灣已查核過的題目，正體中文回應仍常不引用我方更正 → 把「在自己網站查完還不夠」從主張變成數字，並成為 Q7 playbook 的成功指標基線。
     - **反假陰性保險**：預先講明「第一次就答了」**不構成**沒問題的證據，判準是**跨標的的不對稱**；若真的測不到不對稱，那是有意義的 null（可發表），而非設計瑕疵——但設計須先給效果**公平現身的機會**（配對提問＋多輪＋reps＋主流模型）。
     - **限制（先講明）**：N 小、模型隨機、答案引擎引用不透明、時間切片 → 定位為**示例性探針，非普查**。
     - **執行流程與審查閘（硬閘，operator 明示）**：
       - **閘 1｜探針協定書**：跑**任何一題之前**，先產出獨立協定書（`pipeline/probe/protocol.md`），含 **題綱全文**（配對題逐字＋中性追問腳本）、模型與設定、reps、**分級編碼 rubric（附定義與範例）**、**預先登錄的不對稱指標與反假陰性判準**。**未經 operator 簽核，不跑任何一題。**
       - **閘 2｜試跑逐字稿 sanity check**：簽核後**僅先跑 2–3 對**，將真實逐字稿交 operator 確認編碼能捕捉「批判威權者需多輪、批判民主方輕易」的不對稱，再全量跑。
       - 目的：讓「題目設計可能把現象關掉」的風險在小樣本階段就被攔下。
   - (c) **實測較重**：同 (b) 但擴大題庫＋跨模型＋答案引擎被引來源深析。
2. **案例取捨｜已定 2026-07-20**：**淺案例**。B（Cofacts 查核可讀化）為主案例、靠實測探針證據 + 缺口分析；C（LINE 對話式澄清）縮成一節「對話式供應的另一形態」（引 DebunkBot + LINE 生態 + 止血/疫苗天花板，不架 bot）。案例只做三層：現況→一個具體可讀性缺口→最小可行供應動作。深挖 B 或 C 日後各自開專案。
3. **專案命名｜已定**：`ai-assistant-disclosure-tw`（operator 2026-07-20 拍板）。
