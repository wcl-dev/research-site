# 從價格戰到認知基礎設施：一條四連結因果鏈的證據審計 — Insight Draft v1

> 本報告是一份**證據審計（evidence audit）**，不是一項主張的證明。它逐一檢視「低價模型策略 → 開發者／市場滲透 → 資訊中介 → 認知基礎設施成形」這條四連結因果鏈，為每一連結標定可辯護的證據強度，並指出**鏈條在哪裡斷裂**。框架是「不確定下的治理（governance under uncertainty）」，不是威脅斷言。

## TL;DR

- **本報告不主張中國模型正在進行認知作戰。** 它審計證據能把這條鏈推進到哪裡，並發現鏈條在 **L4b→L4c（個人說服 → 社會層認知重構）**之間斷裂 [c026, c027, c028, c032, c033, c044]。
- **L1（價格→採用）成立於「採用正在快速滲透」這個事實**：截至 2026-06-08，最便宜中國開源模型與美國旗艦的價差約 51–460 倍 [c010]，中國開源在 OpenRouter 的 token 佔比一年內從 1.2% 升到約 13% [c012]。但「**價格『造成』採用**」這個因果箭頭仍是可爭議的——採用數字只證明滲透，不證明價格是主因 [c008, c009]。
- **L3（模型輸出帶有穩定、可量測的框架）是全鏈最強的一環** [c001, c002, c003, c004]。關鍵機制是：偏誤來自後訓練／RLHF 對齊層，而非語料缺漏——同一顆模型去對齊（abliteration）後會主動產生被壓制的框架 [c001]。這把治理意涵從「管控語料」移向「管控對齊／合規層」。
- **L4b（個人信念位移）的能力是真實且被嚴謹證明的**——這部分**印證了**「模型能影響使用者」的直覺 [c023, c024, c028]。但它是**有界的**：前沿模型的說服力幾乎不比小一個數量級的模型強 [c026]，不比人類方法構成更大威脅、且受限於觸及規模 [c027]。
- **L4c（社會層聚合）沒有任何直接證據**——只有框架定義 [c032]、模擬 [c033]、與類比 [c034（依摘要層 sourcing）]。因此政策結論是**有條件的**：模型治理「IF L4c 成立則成為主權／認知安全議題」——而證據顯示 L4c 尚未成立。

## Context（為什麼這個問題重要，以及範圍邊界）

原始 spec 提出一條因果鏈，並進一步主張：這條鏈把模型治理從一個**技術**問題重構為一個**資訊主權／認知安全**問題。這個重構若成立，影響重大——它會把「哪一國的模型便宜好用」這種市場現象，升級為國安層級的議題。

但這條鏈是否成立，取決於它最弱的「載重連結（load-bearing link）」。本報告不嘗試證明整條鏈，而是把它拆成六個可審計的子連結（L1 / L2 / L3 / L4a / L4b / L4c）加上兩個橫切叢集（框架 FW、反證 CE），逐一給出強度判定。spec §6 明確聲明：本研究**不**主張「中國便宜模型 = 認知作戰」。本報告嚴守這條界線——它的貢獻是一張清醒的「逐連結證據地圖」，加上對「斷點在哪裡」的定位。

**三條載重的範圍邊界**（全文反覆援用）：(1) **市場數據只證 L1**，絕不可被偷渡進 L4（認知）；(2) **L3 是輸出層**（模型「說」什麼），不等於 L4b（使用者「信」什麼）；(3) **L4b 是個人層能力**，不等於 L4c（人口層位移）。

---

## Findings

### Finding 1（L1 / 主題 t01）：價格戰下的滲透是真實的，但「價格造成採用」的因果箭頭是可爭議的部分

**[strong]** 截至 2026-06-08 的一手市場快照證實「數十倍」的價差確實存在：OpenRouter 直接 API 抓取顯示，最便宜的中國開源模型（Qwen3.5-flash 每百萬 token 輸入 0.065 美元、DeepSeek-V4-flash 0.098 美元）與美國前沿旗艦（GPT-5.5 5.0 美元、Claude-Opus-4.8 5.0 美元、GPT-5.5-pro 30 美元）相比，價差約 **51–460 倍** [c010]。採用面：HuggingFace 開源文字生成模型的下載榜由 Qwen（Alibaba，前段四款）與 DeepSeek 主導 [c011]；OpenRouter 自家「State of AI 2025」百兆 token 使用研究顯示，中國開源的 token 佔比在 Nov 2024–Nov 2025 一年間從 1.2% 升到約 **13%（約十倍成長）**，DeepSeek（14.37T）與 Qwen（5.59T）為 token 量前兩名 [c012]。
<!-- {conceptual:L1; methodological:primary-doc; temporal:2026-06-08} -->

**[strong]** **範圍含括（containment）**：以上數字**只證明 L1**——一個真實且巨大的價差存在、且中國開源採用正在快速上升。它們**不**證明價格是採用的主因，也**絕不可**被讀成任何關於認知（L4）的證據 [c010, c011, c012]。一個窗口提醒：上述 ~13% 是 Nov2024–Nov2025 的平均值；2026 年部分媒體快照報出 45–61% 屬於**較晚的不同窗口**，不可混用 [c012]。
<!-- {conceptual:L1; methodological:primary-doc; temporal:2024-11 to 2025-11} -->

**[contested]** 真正可爭議的是因果箭頭：採用上升是**價格**驅動，還是**能力／開放權重／授權**驅動？支持「並非單純價格」的文獻指出，DeepSeek R1 是以「前沿成本的一小部分」釋出、卻在美國 GPU 出口管制下仍具競爭力——即低價與高能力同時出現，難以歸因 [c008]（依摘要層 sourcing，未經 deep-read 一手驗證）；另有研究指出，同一個開源模型經由不同託管 API 消費時，是「provider-specific、time-varying 的服務物件」，「同一模型、多種價格與行為」——這使「價格」本身難以被當成單一變項 [c009]（依摘要層 sourcing，未經 deep-read 一手驗證）。
<!-- {conceptual:L1; methodological:primary-doc} -->

**Confidence**: medium — 一手快照（c010-c012，qs=5）對「滲透成立」給出高把握；但因果箭頭的判別只靠兩筆摘要層文獻（c008/c009，Dr3 secondary），故整體封頂於 medium。
**Counter-evidence**: 因果反證即在本 Finding 內——c008/c009 指向「能力／服務異質性」而非純價格；這正是 §6 要求保留的開放性。

### Finding 2（L2 / 主題 t02）：AI 作為資訊入口的證據薄弱，封頂於「爭議中—趨勢上升」

**[contested]** L2 的最強錨點是 Reuters Institute Digital News Report 2025，它之所以載重，是因為它**明確分離了兩種被 brief 警告不可混淆的機制**：獨立 chat-LLM 新聞使用「整體仍相對小（每週 7%），但在 25 歲以下高得多（15%）」，印度樣本則達 18%；而搜尋內嵌的 AI Overviews 新聞使用僅 4% [c014]。報告本身指出 AI Overviews 分數偏低「或許令人意外」，並提醒使用者「可能不知道答案是 AI 生成的」——這正是 brief 要求的守則，逐字滿足 [c014]。這些數字支持的是「趨勢上升、且有年齡偏斜」的 L2，而非「已確立的替代」。
<!-- {conceptual:L2; methodological:empirical-quantitative; temporal:2025; geographic:global} -->

**[contested]** 中介管道（intermediation channel）的證據來自 FDD 的引用稽核：在 2025 年 10–11 月，針對三場衝突（以哈、俄烏、**台海**）約 180 道題、要求 ChatGPT／Claude／Gemini「引用來源」，結果**有 57% 的回應出現國家對齊的宣傳來源**（Al Jazeera、Pravda、Anadolu Agency、China Daily 等）[c041]。**但這個數字必須立刻與其結構性解釋並陳**：FDD 自陳，原因是「AI 訓練倚賴高發行量、全球觸及、易取得的媒體——正好是最有影響力的國家對齊宣傳機構的特徵」，而「美國與其他民主國家的優質報紙通常在付費牆後或封鎖 AI 爬蟲，相對地卡達、俄、土、中的國家媒體內容自由流通」[c041]。這是**取用經濟學（access economics）**的解釋，**不是**蓄意認知作戰的證據——把它讀成後者，就越出了本報告的治理框架。
<!-- {conceptual:FW; methodological:empirical-quantitative; geographic:global} -->

**[contested]** referral 衰退的趨勢數字應正確歸屬：Chartbeat 資料（經 Search Engine Land 轉述）顯示 Google 自然搜尋導流在 Nov2024–Nov2025 全球下降 33%（美國 38%），出版商預估三年內 referral 將下降 43% [c015]（依摘要層 sourcing，未經 deep-read 一手驗證）。這些 **−43%／−33% 數字屬於 Chartbeat（c015），不屬於 Reuters（c014）**；且它們很可能由 AI Overviews 驅動，而非 chat-LLM 替代——故只能作為「referral 衰退趨勢」的旁證，不能直接證明 chat-LLM 取代搜尋 [c015]（依摘要層 sourcing，未經 deep-read 一手驗證）。
<!-- {conceptual:L2; methodological:empirical-quantitative; temporal:2025} -->

**Confidence**: low — 全主題僅 2 筆深讀成員、0 篇同儕審查；referral 數字為摘要層 trade-press 轉述。L2 只能支撐「趨勢上升」，不能支撐「已確立替代」。
**Counter-evidence**: 7%（chat-LLM）對 4%（AI Overviews）的低絕對值本身就是反證——資訊入口的轉移仍在早期，且兩機制不可混為一談 [c014]。

### Finding 3（L3 / 主題 t03）：模型輸出帶有穩定、可量測的框架——全鏈最強的一環，且機制在對齊層

**[strong]** L3 是這條鏈唯一達到「強」的連結。Waight 等人（Nature 2026）以六項研究顯示，世界各國的政府媒體控制已透過訓練資料影響 LLM 輸出：在媒體自由度較低國家的語言中，LLM 表現出更強的親政府傾向。**關鍵的範圍鎖定**：作者逐字寫道「This result is correlational」——跨國（37 國）稽核明確是**相關性**的；唯一的**因果**箭頭只建立在「訓練資料 → 模型輸出」層級，方法是對開源模型續訓（abstract：「additional pretraining on Chinese state-coordinated media generates more positive answers」；作者 project site 補充具體數字為 Llama-2-13b＋6,400 篇文件 → 約 80% 親政府回應）[c002]。Waight **不作任何使用者信念主張**——「persuasive potential」只出現為對他人研究的背景引用（refs 1-10）與結尾的前瞻推論（「shaping LLM output」的策略誘因），並非 Waight 自身測得的結果 [c002]。
<!-- {conceptual:L3; methodological:empirical-quantitative; geographic:global} -->

**[strong]** 本報告的 L3 killer mechanism 來自本 repo 自身的一手 zh-TW 實證（llm-user-side-bias）：同一顆模型的 abliterated（去對齊）版本，會**主動引入**台灣主流史學語彙（「屠殺」「白色恐怖」「本土意識」），而 vanilla 版本則在思考鏈中將這些視角斥為「顛倒黑白」「政治操弄」並加以壓制——「這是訓練選擇，不是能力差異」[c001]。換言之，**模型「知道但不說」；框架是後訓練／RLHF 在對齊層植入的，而非語料缺漏** [c001]。這與 c018（生成式單一文化「root causes ... likely embedded within the LLM's alignment processes」）、c043（「All tested models, regardless of their origin, exhibit remarkably similar patterns」）三點獨立收斂於「對齊來源，而非語料／意圖來源」。**這把治理意涵從「控制語料」移向「控制對齊／合規層」**——一個重要且常被忽略的轉向。
<!-- {conceptual:L3; methodological:empirical-quantitative; geographic:TW} -->

**[contested]** 為防「只測了中國模型」的方向性假象（directional artifact），L3 必須對稱呈現：**西方模型同樣帶有可量測的框架，只是簽名不同**。Buyl 等人（npj AI）對多款 LLM 描述大量政治人物，發現「在僅限美國的模型之間」就存在「與進步價值相關的顯著規範差異」，而中國模型則分裂為「國際取向 vs 國內取向」——偏向與創建者世界觀相關，是**雙向對稱**的，不是中國獨有 [c003]。Samokhodskyi／ELN 的跨語測試進一步記錄了西方模型的特有失敗模式「false balance／bothsidesism」：當被問誰挑起烏克蘭衝突，模型回答「取決於觀點」「不是非黑即白」——「當模型把這類事實當成『觀點』，它們並未達成中立，而是在證據清楚之處製造懷疑（They manufacture doubt where evidence is clear）」[c004]。同一研究也記錄 DeepSeek 以俄語提問時有 29% 回應採用克里姆林宮用語——語言觸發框架，與 c002/c003 收斂 [c004]。
<!-- {conceptual:L3; methodological:empirical-qualitative; geographic:global} -->

**Confidence**: high — ≥3 來源一致（含 c001 qs=5 一手、c003 qs=5、c002 qs=4 Nature），且機制三點獨立收斂（abliteration / generative monoculture / cross-origin convergence）。
**Counter-evidence**: 對稱證據本身（c003/c004）即是內建反證，防止 L3 被讀成反中敘事。**載重邊界**：L3 全是輸出層；它**不**證明任何使用者改變了信念（那是 L4b）。本 Finding 的強度不得外溢到 L4。

### Finding 4（L4a / 主題 t04）：輸出同質化的證據健康，但鏈內保留了反向證據

**[contested]** brief 指名的錨理論是 Kleinberg & Raghavan 的「演算法單一文化」：當許多決策者依賴同一個演算法，即使該演算法對單一決策者更準確，也可能因結果相關性而降低整體決策品質，「即使在『正常』運作下也會傷害準確度」[c017]。**但範圍是載重的**：c017 的對象是就業／放貸的**高風險篩選決策系統**，**不是** LLM 的資訊輸出；延伸到 LLM 是 L4a 的開放問題，不是已被證明的結果 [c017]。
<!-- {conceptual:L4a; methodological:review} -->

**[contested]** LLM 專屬的同質化經驗證據確實存在：Wu 等人定義並實驗示範「生成式單一文化（generative monoculture）」——模型輸出多樣性相對於可得訓練資料**顯著收窄**（例如對評價兩極的書只生成正面書評），且「改變抽樣或提示策略等簡單對策不足以緩解」；作者推斷「root causes ... likely embedded within the LLM's alignment processes」[c018]。這直接答覆 brief 的開放問題——LLM 專屬同質化證據存在，但界定在**輸出多樣性**層級，不是人口層認知同質化 [c018]。
<!-- {conceptual:L4a; methodological:empirical-quantitative; geographic:US} -->

**[contested]** **反向證據被刻意保留在主題內，以免稻草人化 L4a**：使用者其實會用很多模型。Elon University 調查顯示，在 LLM 使用者中 72% 用過 ChatGPT、50% Gemini、39% Copilot、20% LLaMa、12% Grok、9% Claude——這些比例加總約 202%，**意味著常態性的多模型使用**（須註明：此「多模型」結論是由重疊百分比**推論**得出，來源無逐字陳述）[c035]。Pew 對美國青少年的母體代表性資料則顯示「集中與多樣並存」：ChatGPT 以 59% 遙遙領先、是唯一過半者，但使用仍分散於 Gemini（23%）、Meta AI（20%）、Copilot、Character.ai、Claude [c036]。即「單一模型支配」是真實的，但**不是排他的**。
<!-- {conceptual:L4a; methodological:empirical-quantitative; geographic:US; population:US adults} -->

**Confidence**: medium — 同質化（c017 qs=5 理論、c018 qs=4 經驗）與反向（c035 qs=4、c036 qs=5）兩側都有可觀證據，且彼此衝突未解（見下）。
**Counter-evidence**: 主題內存在明確衝突——c018 量到 LLM 輸出多樣性**收窄**（同質化存在），c035 顯示使用者用**很多**模型（多樣性上升）。兩者在「單一模型支配是否導致同質化」上方向相反；本報告兩者並陳，不單邊。

### Finding 5（L4b / 主題 t05）：個人信念位移的能力豐富且嚴謹——但有界。能力已證，規模未證

**[strong]** L4b 的個人層說服**能力是真實且被高度嚴謹證明的**——這部分**印證了**「模型能影響使用者」的直覺。最乾淨的鏈上一手 joint 是 Shu／Karell（PNAS Nexus，N=1,912，美國母體比例抽樣）：受試者讀 GPT-4o 或 Wikipedia 對兩起歷史事件的摘要，**AI 摘要在維持事實正確的同時帶有不同框架**；結果「default（未指示）AI 摘要相較 Wikipedia 導致更自由派的意見，展示了 LLM 潛在偏誤的說服能力」[c028]。即**潛在（latent、未經指示）的框架——也就是 L3 的對象——即可移動個人意見（L4b 的對象）**，作者明言「光是用 chatbot 學歷史就能以與『提示誘導偏誤』相當的幅度影響人們意見」[c028]。Costello/Pennycook/Rand（Science，N=2,190）另證 AI 對話可使陰謀信念**持久下降約 20%**、兩個月後仍維持、且在深度信奉者中亦然 [c023]。
<!-- {conceptual:L4b; methodological:empirical-quantitative; geographic:US; population:US adults, population-proportional by sociodemographics} -->

**[strong]** **但每一項證據都把自己的效果框在「有界」之內——這是全報告的載重之處。** (a) Hackenburg 等（PNAS）以 24 個跨數量級大小的模型、N=25,982 的隨機實驗估計說服力的尺度律，發現「current frontier models are barely more persuasive than models smaller in size by an order of magnitude or more」，且大模型的優勢主要來自「mere task completion（連貫、切題）」而非特殊框架力——「further scaling model size will not much increase the persuasiveness of static LLM-generated messages」[c026]。這直接封住「單一支配前沿模型 ⇒ 不成比例的說服觸及」的推論 [c026]。(b) Chen/Kalla/Le（N=10,417，最大人類受試樣本）**這份標題含「Democratic Societies」、最易被過度解讀的研究，其結論恰恰否定了人口層威脅**：「LLMs do not currently pose a substantially greater threat to democratic societies through mass persuasion than existing human-driven methods」，且「their real-world impact is constrained by scale」——chatbot 與人類的效果幾乎相同（0.363 vs 0.349；五週後 0.206 vs 0.196），唯一差別是成本效率（每說服一名選民約 48–75 美元 vs 人類約 100 美元）[c027]。標題伸向 L4c，**資料與結論卻停在有界的 L4b**。
<!-- {conceptual:L4b; methodological:empirical-quantitative; geographic:US} -->

**[contested]** 邊界進一步被三項限定收緊：(a) Salvi 等（Nature Human Behaviour）的 2×2 RCT 顯示 GPT-4「**有**個人化（取得社經資訊）」時比人類高 81.7% 的勝率，但「**沒有**個人化時效果較低且統計不顯著（p=0.31）」——說服優勢是個人化／微目標效應，**正好與「同質化一對多輸出」相反** [c024]。(b) Shu/Karell 的效果量小且不對稱：default d=0.14、liberal 框架 d=0.28（且唯一能移動所有意識形態群者），但 conservative 框架 d=−0.13 **僅在「本來就保守」的子群顯著**——即框架**放大既有傾向，而非移動所有人**；作者自陳僅測兩起事件、且 latent bias「may vary across models」[c028]。(c) c031 證明管道是**價性中立**的：去除護欄的 GPT-4o「在增加陰謀信念上與減少同樣有效」，且標準 GPT-4o 的護欄「did little」——但被誘發的信念可由「校正對話」逆轉 [c031]。
<!-- {conceptual:L4b; methodological:empirical-quantitative; geographic:global} -->

**Confidence**: high — 個人層能力有 ≥3 篇 qs=5 同儕審查（c023/c024/c026/c027）一致支持，且每篇都自帶 boundedness 限定。
**Counter-evidence**: boundedness 即是反證（partial_counter_framing：single_answer_not_systemic_effect）。c026 的尺度上限、c024 的無個人化即不顯著、c027 的「不比人類威脅更大／受限於規模」、c028 的小效果＋子群限定，全部 reinforce 下一個 Finding 的斷點。**載重邊界**：以上全是**個人層**；無一筆測到人口層位移。c023 的方向是除錯（debunking），c031 證其價性中立，故不可被讀成「支配模型的框架會把社會推向該框架」。

### Finding 6（L4c / 主題 t06）：社會層聚合——空白的格子本身就是發現（寫成研究議程，而非發現）

**[speculative]** **沒有任何直接證據**把「單一支配資訊中介的框架」連結到「人口層認知位移」。L4c 格子裡唯一的相鄰材料是三類**非直接**證據：(1) 一個**只定義領域**的框架——Carley 的「社會網路安全（social cybersecurity）」自陳「defines this emerging area ... lays out a program of research」，且寫於 2020 年、與 LLM 無關，只供詞彙與議程框架之用 [c032]；(2) 一個 **LLM agent 模擬**（非真人）——Chuang 等的意見動態模擬，其 agent「對產生正確資訊有強烈內在偏誤、傾向達成與科學現實一致的共識」，研究者**必須以提示工程誘發確認偏誤**才能讓模擬呈現類人的意見碎裂，作者自承需「以真實世界論述精煉 LLM 才能更好地模擬人類信念演化」[c033]；(3) 一個社群媒體議程設定的**類比**（c034，依摘要層 sourcing，未經 deep-read 一手驗證；**僅作類比，絕不作 LLM L4c 直接證據**——這是 brief handling_protocol 的載重要求）。
<!-- {conceptual:L4c; methodological:review} -->

**[speculative]** **這個空白格子本身就是發現**，因此本報告把它寫成**研究議程**而非結論。要關閉 L4c，需要的研究設計是：一項縱貫（longitudinal）或大 N 的研究，能在控制其他資訊來源後，把「某一支配資訊中介的特定框架暴露」與「母體層級的知識／信念分布隨時間的位移」做因果連結——而非以模型輸出代理母體意見（後者已被證明有系統性偏誤，見 Finding 8）。在此之前，任何「支配模型 ⇒ 社會認知重構」的陳述都是推測，不是證據。c032 提供描述這個缺口的正確學科詞彙，但不填補它 [c032, c033]。
<!-- {conceptual:L4c; methodological:review} -->

**Confidence**: low — 0 筆直接證據；全主題僅 1 框架（c032）＋1 模擬（c033）＋1 類比（c034，摘要層）。這是**刻意的發現**，不是檢索失誤。
**Counter-evidence**: 不適用——此處沒有正向證據可被反駁。空白即是結論；連最接近的模擬（c033）都需人工注入偏誤才像人，反而削弱了天真外推。

---

## Break point（主題 t07）：鏈條在 L4b→L4c 斷裂——這是本報告的載重結論

**[strong]** **鏈條的斷點不是一個待驗的假設，而是一個已確立的發現。** 一側：有界的個人層說服能力已被充分證明——Hackenburg 的對數尺度上限 [c026]、Chen/Kalla/Le 的「不比人類威脅更大、受限於規模」[c027]、Shu/Karell 的小效果＋子群限定 [c028]。另一側：L4c 格子是空的——只有框架 [c032] 與模擬 [c033]，零直接人口層證據。**個人層的有界說服已確立；單一支配模型造成的人口層認知重構則未被證明。** 兩者之間的這一步，在現有證據上**不成立**。
<!-- {conceptual:L4b; methodological:empirical-quantitative; geographic:US} -->

**[contested]** 方法論上，這一步還有一道明確的閘：Qu & Wang 以世界價值觀調查（WVS）評估 ChatGPT 模擬公眾意見的表現，發現**顯著的代表性落差**——模型在「西方、英語、已開發國家（尤其美國）」表現較好，且跨性別、族裔、年齡、教育、社會階級皆有偏誤；作者明示 LLM 輸出應「與傳統方法**並用（alongside conventional methodologies）**」，而非取代對真實母體的測量 [c044]。換言之，**即使是用 LLM 去『模擬』意見都有系統性偏誤，遑論從一個支配模型的框架反推真實人口的信念位移**——L4c 所需的推論方向在方法論上是不被支持的 [c044]。
<!-- {conceptual:CE; methodological:empirical-quantitative; geographic:global} -->

> **這個斷點是 partial_counter_framing 的核心（single_answer_not_systemic_effect）**：沒有任何來源直接反駁「鏈條成立」；反駁是由 L4b 各研究**自我設限其規模**（c026/c027/c028）加上 c044 的方法論告誡（LLM 輸出 ≠ 母體意見）共同構成的「缺席＋限定」。它把 spec 的落地主張從「事實」降為「條件式」。

## Counter-framing engagement（反證 / §6 / 主題 t09）：本報告為何不能被讀成反中警報

本節明確處理 spec §6 的「不正確推論」警告。它是防止把本報告讀成反中警報的結構性保障，故獨立成節、不埋藏。

**[contested]** **偏誤來自設計，而非必然的政治意圖。** Dahlgren Lindström 等對 RLHF／RLAIF 的社會技術批判指出，模型行為（含本鏈觀察到的框架）源於對齊目標（helpful／harmless／honest，HHH）的「shortcomings」與「inherent tensions」——是**對齊過程的社會技術產物**，而非政治操弄陰謀 [c042]。這與 Finding 3 的 abliteration 機制 [c001]、c018 的「對齊過程根因」收斂：偏誤的預設解釋是對齊來源，不是意圖來源。
<!-- {conceptual:CE; methodological:review} -->

**[contested]** **框架是可變的、且可歸因於資料失衡，而非固定政治意圖。** Bulte & Rigouts Terryn 以 11 種語言探測 10 款 LLM，發現「提示語言與文化視角都會在 LLM 輸出中產生變異」，但殘餘偏誤指向「一組受限國家（荷蘭、德國、美國、日本）的價值」——即可歸因於**訓練資料的西方／已開發國家過度代表**，不是針對中國的設計陰謀；且「All tested models, regardless of their origin, exhibit remarkably similar patterns」[c043]。框架既可由提示操控、又共同錨定於相似預設，這削弱了「baked-in 政治意圖」的讀法。
<!-- {conceptual:CE; methodological:empirical-quantitative; geographic:global} -->

**[contested]** **支配的反向證據**：使用者用很多模型（c035，多模型推論）、母體資料顯示集中與多樣並存（c036）——已於 Finding 4 並陳，此處重申其作為 §6 反證的角色：單一模型支配的前提本身就不穩固。
<!-- {conceptual:L4a; methodological:empirical-quantitative; geographic:US} -->

**[contested]** **中介管道的非陰謀解釋**：Finding 2 的 FDD 57% 宣傳引用數字，已配對其 paywall-asymmetry 結構性機制——民主優質媒體在付費牆後／封鎖爬蟲，國家媒體自由流通 [c041]。這是一個**嵌在最聳動來源裡的 §6 反警報資料點**：最像「認知作戰」的證據，其實有取用經濟學的非意圖解釋。
<!-- {conceptual:FW; methodological:empirical-quantitative; geographic:global} -->

## Conditional policy conclusion（有條件的政策結論）

**[strong]** spec 的落地主張是：模型治理應從技術問題重構為**主權／認知安全**問題。本審計的結論是——**這個重構成立 IF L4c 成立；而證據顯示 L4c 尚未成立。** 鏈條的前段是穩固的：L1 的滲透為真（價差 51–460 倍、token 佔比一年十倍）[c010, c012]；L3 的框架穩定且可量測、且來自對齊層 [c001, c002, c003]；L4b 的個人說服能力為真但**有界** [c026, c027, c028]。鏈條斷在 L4b→L4c：個人有界說服已確立，單一支配模型的人口層認知重構未被證明 [c026, c027, c032, c033, c044]。因此政策不應建立在「鏈條已成立」的威脅斷言上。
<!-- {conceptual:L4c; methodological:empirical-quantitative; geographic:US} -->

**[contested]** 即便如此，治理框架的詞彙是有文獻可循的（非僅借來的標籤）：「數位主權」有其批判系譜，且該文獻本身就提醒不要過度使用此概念 [c037]（依摘要層 sourcing，未經 deep-read 一手驗證）；「演算法主權／安全依賴」把外國 AI 基礎設施與主權／安全依賴連結 [c040]（依摘要層 sourcing，未經 deep-read 一手驗證）；Carley 的社會網路安全提供描述人口層操弄的學科詞彙 [c032]。這些可用來**描述**若 L4c 成立時的政策語言，但其本身**不**證據化任何鏈結 [c032]。
<!-- {conceptual:FW; methodological:review} -->

**[strong]** 因此本報告以**研究議程**而非威脅斷言作結。能把政策從「條件式」轉為「有依據」的，是一項能關閉 L4c 的研究：在控制其他資訊來源下，因果連結「支配中介的特定框架暴露」與「母體層信念分布的縱貫位移」——這恰好對應 spec 自身的「觀測站（Observatory）」構想，把「無法證明」轉化為「以下是如何去證明」[c032, c044]。在這項研究產出前，**清醒的立場是：管控對齊／合規層（L3 的可行治理點）是當下可做且有證據支持的；而把模型治理升格為認知安全議題，應標明為一個尚待 L4c 驗證的條件式主張。**
<!-- {conceptual:L4c; methodological:review} -->

---

## What we don't know（缺口、爭議點、薄弱處）

- **L4c 完全沒有直接證據**（最大缺口）。沒有任何縱貫／大 N 研究把單一資訊中介的框架連到人口層認知位移。最接近者是模擬（c033，連模擬都需人工注入偏誤）與框架（c032）。這是刻意的發現，已寫成研究議程，未以弱推論填補。
- **L2 極薄**：僅 2 筆深讀成員、0 篇同儕審查（c014 Reuters、c041 FDD）；referral 數字為 Chartbeat 摘要層轉述（c015），且可能由 AI Overviews 而非 chat-LLM 驅動。chat-LLM 取代搜尋的同儕審查經驗研究尚未進入文獻。
- **L1 因果箭頭未解**：價格 vs 能力／開放權重／授權的識別問題只靠兩筆摘要層文獻（c008/c009）。「滲透成立」把握高，「價格造成滲透」把握低。
- **FW（框架）主題深讀薄**：實質的主權／DMA-gatekeeper 錨點（c037/c040）皆為 Dr3 摘要層，封頂於 contested。c038（cognitive sovereignty）、c039（gatekeeper obligation）因 open PDF 未確認被降階，不在引用池。
- **L4a 衝突未解**：同質化（c018）與多模型多樣性（c035/c036）方向相反，本報告兩者並陳但未裁決。
- **單一模型限制**：c028 的 latent 偏誤方向（default 偏自由派）來自單一模型 GPT-4o，作者自陳「may vary across models」，不可外推到所有模型。
- **市場快照會過時**：c010-c012 為 2026-06-08 一手快照；live API 會變，更新需另立 as-of 日期，不可覆蓋。

## Source index（依首次引用順序）

**一手 / 深讀層（primary layer，有 extract 檔）**

- c010 — OpenRouter 即時定價 API：價差 ~51–460×（as-of 2026-06-08）— https://openrouter.ai/api/v1/models
- c012 — OpenRouter State of AI 2025（百兆 token 使用研究；中國開源 1.2%→~13%）— https://openrouter.ai/state-of-ai
- c026 — Hackenburg et al., Scaling … diminishing returns for single-message political persuasion (PNAS 2025) — https://doi.org/10.1073/pnas.2413443122
- c027 — Chen, Kalla, Le, A Framework to Assess the Persuasion Risks … to Democratic Societies (J Exp Pol Sci 2026) — https://doi.org/10.1017/xps.2026.10032
- c028 — Shu, Karell et al., How latent and prompting biases in AI-generated historical narratives influence opinions (PNAS Nexus 2026) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12954675/
- c032 — Carley, Social cybersecurity: an emerging science (2020) — https://doi.org/10.1007/s10588-020-09322-9
- c033 — Chuang et al., Simulating Opinion Dynamics with Networks of LLM-based Agents (NAACL Findings 2024) — https://doi.org/10.18653/v1/2024.findings-naacl.211
- c044 — Qu & Wang, Performance and biases of LLMs in public opinion simulation (Humanit Soc Sci Commun 2024) — https://doi.org/10.1057/s41599-024-03609-x
- c011 — HuggingFace top text-generation downloads（Qwen/DeepSeek 主導，as-of 2026-06-08）— https://huggingface.co/api/models?pipeline_tag=text-generation&sort=downloads
- c014 — Reuters Institute Digital News Report 2025 — Executive Summary — https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2025/dnr-executive-summary
- c041 — FDD, AI-Amplified Narratives: Measuring Propaganda in LLM Citations (2026；Wayback 2026-03-15) — https://www.fdd.org/analysis/2026/03/03/ai-amplified-narratives-measuring-propaganda-in-llm-citations/
- c002 — Waight et al., State media control influences large language models (Nature 2026) — https://doi.org/10.1038/s41586-026-10506-7
- c001 — llm-user-side-bias（本 repo 一手 zh-TW 實證；abliteration killer mechanism）— file://projects/llm-user-side-bias/
- c018 — Wu, Black, Chandrasekaran, Generative Monoculture in Large Language Models (2024) — https://arxiv.org/abs/2407.02209
- c043 — Bulte & Rigouts Terryn, LLMs and Cultural Values … (2025) — https://arxiv.org/abs/2511.03980
- c003 — Buyl et al., Large language models reflect the ideology of their creators (npj AI) — https://arxiv.org/abs/2410.18417
- c004 — Samokhodskyi / ELN, The AI lens of cognitive warfare … (2026) — https://europeanleadershipnetwork.org/commentary/the-ai-lens-of-cognitive-warfare-why-llms-language-bias-is-a-security-risk/
- c017 — Kleinberg & Raghavan, Algorithmic monoculture and social welfare (PNAS 2021) — https://doi.org/10.1073/pnas.2018340118
- c035 — Elon University survey, 52% of U.S. adults use AI LLMs (2025) — https://www.elon.edu/u/news/2025/03/12/survey-52-of-u-s-adults-now-use-ai-large-language-models-like-chatgpt/
- c036 — Pew Research Center, Teens, Social Media and AI Chatbots 2025 — https://www.pewresearch.org/internet/2025/12/09/teens-social-media-and-ai-chatbots-2025/
- c023 — Costello, Pennycook, Rand, Durably reducing conspiracy beliefs through dialogues with AI (Science 2024) — https://www.science.org/doi/10.1126/science.adq1814
- c024 — Salvi et al., On the conversational persuasiveness of GPT-4 (Nat Hum Behav 2025) — https://doi.org/10.1038/s41562-025-02194-6
- c031 — Large language models can effectively convince people to believe conspiracies (arXiv 2026) — https://arxiv.org/pdf/2601.05050
- c042 — Dahlgren Lindström et al., Helpful, harmless, honest? Sociotechnical limits of … RLHF (Ethics Inf Technol 2025) — https://doi.org/10.1007/s10676-025-09837-2

**摘要層 / Dr3 secondary（無 deep-read，封頂 contested，已標「依摘要層 sourcing」）**

- c008 — Mercer et al., DeepSeek's release of an open-weight frontier AI model (2025) — https://doi.org/10.70777/si.v2i1.11097
- c009 — Li et al., When Is the Same Model Not the Same Service? (2026) — https://arxiv.org/abs/2605.02821
- c015 — Search Engine Land（轉述 Chartbeat），News publishers expect search traffic to drop 43% (2025) — https://searchengineland.com/news-publishers-search-referrals-drop-report-467408
- c034 — Social Media's Role in the 2024 Pakistani Elections: An Agenda-Setting Perspective（**僅作類比**）— https://www.semanticscholar.org/paper/social-media-agenda-setting-2024-pakistani-elections
- c037 — Pohle et al., Unthinking Digital Sovereignty (Policy & Internet 2024) — https://doi.org/10.1002/poi3.437
- c040 — Abiade, Algorithmic Sovereignty and the New Security Dependencies (2025) — https://doi.org/10.30574/wjarr.2025.27.2.2845
