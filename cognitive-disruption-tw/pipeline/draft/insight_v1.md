# 動機合流與「認知破壞」—— Insight Draft v1

**子標題**：似是而非協同內容的工業化基礎設施、作為環境層傷害的認知破壞假說，與跨域防治的結構必要性

**版本**：insight_v1 ｜ **日期**：2026-06-16 ｜ **定位**：政策／防治取向威脅評估草稿
**目標讀者**：跨機關防治單位、平台治理、政策制定者
**狀態**：🟢 Reviewer 審畢（publishable，零 must-fix）；已套用 should-fix（c062）＋nice-fix（c036/c037/c038）。CD／FM 為待驗證的可證偽假設，FM 倍增器鏈為命題最弱一環。

> **本稿與 answer-key 的關係**：`../draft_v1.md` 是以兩份台灣在地報告為骨架的命題種子，其「kwara 型／FIMI 型」二分骨架在本稿被取代。本稿以 66 份獨立 accepted 來源論證命題，兩份台灣報告**僅作 Q8 的案例實例**（佐證特定主張），不是組織軸線。
>
> **三個全稿層級的誠實邊界（先講在前面）**：
> 1. **認知破壞（CD）與加乘效應（FM）是本研究提出的詮釋性、可證偽假設，不是已證實事實。** FM 是命題鏈最弱一環——**沒有任何一手研究實證「資訊環境飽和 → 母體信任基線下降 → 後續操作更有效」這條完整鏈** [c058, c050, c079]。
> 2. **合流（convergence）的判讀是本研究主張，不是 Meta 立場。** Meta H1 2026 把詐騙中心與影響力操作列為**分開的**執法類別，未宣稱兩者共用基礎設施 [c001]。共用基礎設施的證據來自 c010 / c024 / c008，不是 c001。
> 3. **c021（Roberts flooding）全文未取得，僅作概念錨**；本稿引用其 flooding 概念但**不含逐字一手引文**。

---

## TL;DR

- 多個獨立來源顯示「財務動機操作」與「影響力操作」在**手法與基礎設施層合流**：同一套 GAN 假頭像基礎設施跨詐騙／spam／協同放大三種用途，研究者明言「動機無法判定」[c024]；政治影響力操作的假人設＋AI 影像＋外包手法被原樣用於商業銷售引流 [c010]；造謠外包供應商的客戶橫跨政黨、企業與國家連結行為者 [c008]。
- 不同動機共用同一套**工業化基礎設施**：批量身分生產、AI 素材複用、cloaking、跨語言帳號供應鏈、可棄式資產輪替、針對主流偵測方法的對抗工程。EEAS 一手繪製 38,000 個頻道、505 起事件、90 國的分層、可棄式 FIMI 基礎設施 [c032]；生成式 AI 把這套基礎設施的邊際成本壓低、規模放大、形態改變 [c079, c008]。
- 本研究主張這類操作的首要傷害是**對資訊環境本身的無差別污染**（稱「認知破壞」），它逼近但不等同於既有框架——firehose of falsehood [c019]、information disorder [c018]、liar's dividend [c020]、flooding／censorship-through-noise [c021]——CD 補充的是一個**動機獨立、環境層、加乘效應**的傷害定位。
- **FM（倍增器）鏈是最弱的一環**：量→個人接受有實證 [c019]，liar's dividend 對文字有效但**對影片無效、且不降低整體媒體信任** [c050]；效果端被多份同儕審查與機構報告標為高估或 critical unknown [c035, c034, c079]。「飽和→母體信任基線下降→後續操作更有效」這條完整鏈**無一手實證** [c058]。
- 既然動機是可替換 payload、操作者住在各領域偵測方法的盲區交界，**跨域整合不是道德呼籲、是結構必要**：每套單一偵測法都有可被對抗工程繞過的盲區（平台移除率最佳一輪平均仍僅 50.4%、TikTok 4%）[c026]；唯有疊加多方法＋共用交換接口（IMS 三層 [c028]、DISARM→STIX2→OpenCTI 已交換 >100 起事件 [c030, c031]、EEAS Infrastructure Matrix [c032]）才能收斂盲區。

## Context

過去解釋網路可疑內容用兩條軸線：**政治攻擊框架（P）**——以意圖與外國性為判定核心（FIMI、認知作戰、影響力操作）；與**詐騙獲利框架（S）**——以金流與獲利模式為判定核心（內容農場、廣告變現、釣魚）。兩條軸線各有成熟的偵測方法與承辦機關。

本研究論證的命題鏈是：**(P ∪ S) 失效 → I 共用工業化基礎設施 → CD 認知破壞（FM 倍增器）→ 需 XD 跨域防治**。研究焦點是 I→CD→XD；P 與 S 作為「被取代的舊分類軸」對照。命題的論證以廣泛的學術文獻、各國威脅情報、平台揭露為證據基礎；兩份台灣一手報告（FB 外連可疑站／YouTube 養生協同網）僅作 Q8 的具體實例。

**範圍邊界**：時間以 2016+ 為主（CIB 概念成形、firehose、information disorder、FIMI-EEAS、2023+ 生成式 AI slop），經典理論允許更早作背景。地理以全球文獻與威脅情報為主結構，中文資訊環境為主要受害場域。深度為**論證型**——把命題建成一條可被證偽的鏈，明白標出哪幾環有實證、哪幾環是推論。

本稿以 Q1–Q8 對應的八個 Finding 組織。每段以證據強度 tier 標籤開頭（【強證據】／【爭議中】／【推測】／【專家意見】）。**tier 描述證據的知識論強度（關於來源）；Confidence 描述 Drafter 對該主張的把握（關於推論）**——兩者獨立。

## Findings

### Finding 1（Q1）：財務動機與影響力操作的動機分類正在系統性失效——這是學界自陳，不是外加詮釋

【強證據】 動機分類失效最硬的單一學術證據來自對 GAN 假頭像帳號的系統分析：Yang、Singh 與 Menczer（Indiana OSoMe）整理出 1,420 個用 GAN 生成頭像的 X 帳號，證明它們「被用於散布詐騙、spam，並放大協同訊息」，並直接寫下「**Their motives remain unclear, given the varied nature of the amplified content**」——研究者面對同一帳號群放大的內容種類雜駁，**無法**判定單一動機 [c024]。這比任何外加詮釋都硬：是論文作者本人撞到了「動機」這個分類軸的失效。

【強證據】 同儕審查的 HKS Misinformation Review 研究進一步證明手法跨域挪用：原用於政治造謠的三件手法——「fake persona creation, AI-generated imagery, and outsourcing」——被原樣用於商業銷售引流（LinkedIn n=1,003 GAN 假頭像帳號、橫跨 ≥63 個雇主），論文明文「**bridge the political and economic domains**」，並點名「emerging disinformation field is primarily focused on political messaging」而忽略了經濟動機 spammer [c010]。c024（X，跨 scam/spam/influence）與 c010（LinkedIn，商業 lead-gen）互補，構成 I 軸 GAN-face 跨平台、跨用途的雙實證錨。

【專家意見】 機構級論述把這個合流定位為產業結構轉變。EEAS／EUvsDisinfo 描述「a quiet revolution」：過去由威權政府與情報機構經營的操作，如今「outsourced to private firms that sell disinformation and deception as a service」；具體到 Team Jorge——同一供應商「Its clients included political parties, corporations, and, allegedly, state-linked actors」[c008]。同一套 for-hire 基礎設施服務政治、商業與國家客戶，是「動機是基礎設施上可替換 payload」的供給側論述。（此為 EU 對外機構立場文，frame 偏 FIMI／外國性；它證的是 P 客戶與商業供應商合流，不直接證純詐騙端 S。）

【爭議中】 平台與 AI 供應商的威脅揭露也記錄了跨動機共用工具鏈：OpenAI 報告威脅行為者把 AI 整合進既有 toolchain、自 2024-02 起破壞 40+ 違規網絡橫跨詐騙、惡意網路活動與隱蔽影響力操作 [c002]（依摘要層 sourcing，未經 deep-read 一手驗證）；Google GTIG 觀察生成式 AI 多用於提升既有作業效率（偵察、在地化、內容生成），跨國家級攻擊與資訊操作行為者 [c004]（依摘要層 sourcing，未經 deep-read 一手驗證）。Woolley（J. Democracy）亦指同一套 bot／sockpuppet 工具跨政府、企業、網紅行為者 [c075]（依摘要層 sourcing，未經 deep-read 一手驗證）。S 端的工業化規模亦有官方記錄：USCC 指東南亞詐騙中心 2023 年約 $43.8B 收入（≈緬柬寮合計 GDP 約 40%）、在經濟特區內運作以規避執法、與人口販運與洗錢交織為單一犯罪生態 [c038]（依摘要層 sourcing，未經 deep-read 一手驗證）——使「以動機（獲利）就能把 S 與工業化基礎設施 I 切開」更難成立。

**Confidence**: 高 — c024（qs=4 同儕審查級實證）、c010（qs=5 同儕審查）、c008（qs=4 機構）三源獨立、方向一致，含 ≥1 個 qs≥4 一手驗證；學界自陳「motives unclear / bridge the domains」是最強授權。
**Counter-evidence**: 「共用 vendor 不等於同一行為者」的反框架成立——c023 記錄 CIB 偵測訊號高度碎裂、不同群體用不同戰術，可被讀成「各自獨立行為者、非統一操作」[c023]（依摘要層 sourcing，未經 deep-read 一手驗證）。本研究承認 c024 的「motives unclear」也意味著「無法證明是同一行為者」；命題主張的是**基礎設施與手法層**合流，不是行為者同一。

### Finding 2（Q2）：不同動機操作共用同一套工業化基礎設施與 TTP

【強證據】 EEAS 第三份 FIMI 威脅報告一手繪製了這套基礎設施的規模與分層結構：套用 Infrastructure Matrix 於 2024 年 505 起 FIMI 事件，揭露「some 38,000 channels」、targeting「90 different countries」、「322 different organisations」[c032]。報告把基礎設施描述為**多層、各層分工**的網絡——「a central network of channels openly controlled by a threat actor. This backbone ... is composed of multiple layers of networks, each fulfilling distinct roles」[c032]，並指出資產「often short-lived and disposable—active only for a single campaign or swiftly removed by platforms」，其 transient nature 使識別困難 [c032]。這直接對位 I 軸的「批量生產、資產輪替與重新分配」與 Q6「偵測盲區」，且是機構級權威數字（高於 preprint）。

【強證據】 批量身分生產基礎設施在跨動機案例中反覆出現：Team Jorge 的 AIMS 軟體「capable of creating and coordinating thousands of fake social-media accounts, complete with synthetic photos, biographies, and backstories」，用途為「flood debates, spread narratives, or harass opponents」[c008]；c024 的 1,420 個 GAN 帳號＋c010 的 1,003 個 GAN 帳號是同一類批量假身分基礎設施的量化指紋 [c024, c010]。NATO StratCom 2025 實驗則證明這套基礎設施**可商品化購得**：一次實驗驅動「over 100,000 units of inauthentic engagement」、辨識「30,011 unique inauthentic social media accounts」跨 7 平台，且「for €121, we received 17,442 comments」[c026]——基礎設施門檻極低、可向商業供應商購得。

【爭議中】 跨案例與既有協同手法框架的對齊也有同儕審查支撐：Shao 等（Nature Communications）量化分析「14 million messages spreading 400 thousand articles」，證 social bots 在散布低可信內容上扮演不成比例的角色 [c070]（依摘要層 sourcing，未經 deep-read 一手驗證）；Starbird 等把資訊操作概念化為「collaborative work」、拆成分散式工作流程 [c042]（依摘要層 sourcing，未經 deep-read 一手驗證）；Ong & Cabañes 的菲律賓民族誌記錄付費造謠的勞動分工與生產線 [c051]（依摘要層 sourcing，未經 deep-read 一手驗證）；Keller 等以參與者名單實證政治洗草（astroturfing）的協同操作層 [c054]（依摘要層 sourcing，未經 deep-read 一手驗證）。這些一致指向「工業化生產而非單一行為者」，但多屬政治場域，跨到純獲利場域的對齊仍部分靠推論。

**Confidence**: 高 — c032（qs=5 機構一手）、c008（qs=4）、c026（qs=4）三源含 ≥1 qs≥4 一手；批量身分、AI 素材複用、可棄式資產三類 TTP 在多源交叉出現。
**Counter-evidence**: 共用基礎設施可能是「共用 vendor／多租戶（multi-tenant）」而非「同一操作者」——這是 brief 點名的 shared_vendor_not_actor 反框架。c023 的碎裂訊號支持此讀法 [c023]（依摘要層 sourcing，未經 deep-read 一手驗證）。本研究的主張對此**相容**：命題要的正是「基礎設施／供應商層共用」，這恰恰使「以動機歸因行為者」更困難，而非更容易。

### Finding 3（Q3）：生成式 AI 把這套基礎設施的邊際成本壓低、規模放大、形態改變——但「量產≠影響」

【強證據】 SIO／CSET／OpenAI 聯合報告是 AI→IO 規模效應的奠基分析：「As generative models drive down the cost of generating propaganda, more actors may find it attractive to wage [influence operations]」、「campaigns will become easier to scale when text generation is automated」，並指 AI 改變的不只是量、也是形態——「dynamic, personalized, and real-time content generation like one-on-one chatbots」[c079]。EEAS 用「laptop 取代整棟 troll farm」的對照（c008 的「What once took a troll farm and a whole building in St. Petersburg now takes a laptop」[c008]）給出同一命題的鮮明措辭。

【專家意見】 但同一份 SIO/CSET/OpenAI 報告**明確把效果端列為 critical unknown**：報告以 speculate 語氣處理「更多／更便宜內容是否轉為更大影響」，現有效果證據僅止於 GPT-2「could produce text that successfully mimicked the style and substance of human-written articles」(mimic，非更大說服) [c079]。EEAS 也對 AI 生成內容誠實標記不確定——「AI-generated text is also probably used in FIMI operations, but its detection remains challenging」[c032]。**這是 Q3→Q5 的關鍵閘門**：AI 證實了「I 軸基礎設施更便宜、更大、形態更多樣」，但**沒有**證實「量產自動提升操作成效」。

【爭議中】 供給端的工業化生產有新聞與量測佐證：404 Media 追到 FB Creator Bonus「pays you $100 for 1,000 likes」驅動印度／越南／菲律賓跨地域 AI slop 量產、手法經 YouTube 教學與 Telegram 指南商品化傳播 [c013]；MIT Tech Review 描述 AI slop「優化以遊戲搜尋演算法，把優質內容埋在 spam 下」並延伸至模型崩塌風險 [c014]（依摘要層 sourcing，未經 deep-read 一手驗證）；DeGenTWeb 首度系統量測 LLM 主導網站的母體佔據，並指出「detectors of LLM-generated text perform much worse than advertised」[c048]（依摘要層 sourcing，未經 deep-read 一手驗證）；犯罪學綜述把 AI 對詐騙的影響定為「industrialising deception」並與組織網絡 convergence [c045]（依摘要層 sourcing，未經 deep-read 一手驗證）。

**Confidence**: 中高 — c079（qs=4）與 c008（qs=4）對「成本／規模」主張一致且 deep-read 驗證；但效果端的不確定性使整體 Finding 不可拉到「AI 必然放大傷害」。
**Counter-evidence**: 「slop 只是演算法副產物／純獲利、非協同操作」的反框架（just_spam / just_profit）有代表性論者：Carrigan 主張 slop 是 engagement farming 的產物、反映共享誘因結構而非協同意圖 [c016]（依摘要層 sourcing，未經 deep-read 一手驗證）；Digital Content Next 把 slop 歸因於演算法視覺度設計 [c017]（依摘要層 sourcing，未經 deep-read 一手驗證）。本研究承認大量 slop 確由變現誘因驅動——但這正是「動機（獲利）是基礎設施上可替換 payload」的供給端版本，不否證 I 軸合流。

### Finding 4（Q4）：「認知破壞」對位既有框架——它補充了一個動機獨立、環境層的傷害定位，並非全為新詞

> **CD 定義（本節範圍說明，非證據主張）**：本研究提出的**認知破壞（CD）**＝以海量、似是而非、高度協同的內容飽和**資訊環境本身**，系統性壓低整個母體的信任與辨識基線，傷害對象是**認知共有財（epistemic commons）**而非被說服／被騙的個人。CD 是一個**詮釋性、可證偽的假設**。以下逐一把 CD 對位到既有框架，講清楚補充了什麼、哪裡只是改名。

【強證據】 **firehose of falsehood（c019）**：RAND 原典提供 CD「以量淹沒」最接近的既有理論——四特徵「High-Volume and Multichannel / Rapid, Continuous, and Repetitive / Lacks commitment to objective reality / Lacks commitment to consistency」，並以個人說服心理學為地基（「Repeated exposure to a statement has been shown to increase its acceptance as true」、「repetition leads to familiarity, and familiarity leads to acceptance」）[c019]。**CD 補充的位置**：firehose 仍是**為了推某套敘事**（payload 有方向）；CD 主張傷害本身**獨立於任何特定敘事**（飽和即傷害）。這是補充，不是改名。

【強證據】 **information disorder（c018）**：Wardle & Derakhshan 的三型（mis/dis/mal-information）以「falseness × intent × harm」區分，仍以**單則內容＋意圖**為分析單位 [c018]。**CD 補充的位置**：CD 的傷害不取決於單則內容真偽或行為者意圖（真假混雜＋cloaking 本身即傷害）。值得注意連 information disorder 作者都在推動「看穿超越單則假新聞網站、看更大結構」[c018]——CD 是這個方向的延伸。

【強證據】 **liar's dividend（c020）**：Chesney & Citron 把傷害定位在「a skeptical public will be primed to doubt the authenticity of real audio and video evidence」，且紅利「flows ... in proportion to success in educating the public」、「can be invoked just as well against authentic as against adulterated content」[c020]。這幾乎就是 CD「壓低母體辨識基線」的法學前身——**CD 把這個個案機制一般化**為基礎設施層、無特定行為者的無差別傷害。（注意：c020 屬理論／質性論證，未量化紅利規模。）

【推測】 **flooding／censorship-through-noise（c021）**：Roberts 的 flooding 是 CD「以量稀釋、壓低碰到可信來源機率」的理論祖源，與 fear、friction 並列為審查三機制 [c021]。**本研究全文未取得 c021，僅以概念錨援引 Roberts (2018)，不含逐字一手引文**——此為已知 sourcing gap（見「我們不知道的」）。flooding 原指**國家審查者**的主動行為；CD 主張同一機制可由**無特定行為者的工業化內容飽和**達成，此延伸是本研究主張。

【爭議中】 **CD↔cognitive warfare 的對位來源不足**：accepted 池中唯一 cognitive-warfare 標記的 c022 深讀後是「社群媒體對軍事人員的定向風險」，**不提供** cognitive warfare 的正式定義 [c022]——此為負面發現。可用的替代橋接是 Pace & Coelho「information as a weapon of mass disruption: from information disorder to cognitive warfare」[c078]（依摘要層 sourcing，未經 deep-read 一手驗證）與 c052 的「politics of noise / narrative flooding」近期案例 [c052]（依摘要層 sourcing，未經 deep-read 一手驗證）。CD↔cognitive warfare 的嚴格對位仍待補一手機構定義（NATO ACT du Cluzel）。

【爭議中】 **epistemic commons 一側的學術支撐**：CD「傷害集體知識而非個人」有同儕審查文獻群可對接——Tanasoca 論證 bot 灌量造成的「epistemic double-counting」扭曲集體判斷 [c067]（依摘要層 sourcing，未經 deep-read 一手驗證）；de Ruiter 把 deepfake 傷害定位在共享信任基礎 [c061]（依摘要層 sourcing，未經 deep-read 一手驗證）；Kay 等的「generative algorithmic epistemic injustice」對位 CD 對集體知識的傷害 [c063]（依摘要層 sourcing，未經 deep-read 一手驗證）；Nguyen 的 echo chamber／epistemic bubble 區分則幫助釐清 CD 與既有資訊環境傷害框架的差異 [c065]（依摘要層 sourcing，未經 deep-read 一手驗證）。

**Confidence**: 中 — 對位的四個核心框架（c018/c019/c020 deep-read，c021 概念錨）都是 qs=5 一手原典，對位關係紮實；但「CD 補充了一個獨立新層」這個主張本身是 Drafter 的詮釋，Reviewer 應審計 CD 是否在某些段落只是 firehose／flooding 的改名。
**Counter-evidence**: 哲學側有反誇大的約束——Habgood-Coote 批判 deepfake「epistemic apocalypse」式預測過度，指社會規範與歷史先例使深偽沒那麼可怕 [c066]（依摘要層 sourcing，未經 deep-read 一手驗證）。CD 須限縮在「特定生態位飽和＋來源判斷掏空」，不可滑向「認知末日」。

### Finding 5（Q5）：加乘效應（FM）是命題鏈最弱的一環——「飽和→信任基線下降→後續操作更有效」這條完整鏈無一手實證

> **本 Finding 逐環標記 FM 鏈的證據狀態。讀完本節，讀者應確知 FM 是本研究最弱、最多推論的一環。**

【強證據】 **環 1（量→個人接受）有實證，但止於個人信念層**：firehose 的有效性建立在個人說服心理學——多來源、重複曝光提高個人對單一敘事的接受度 [c019]。c058（Falling for Russian Propaganda，n=1,500）也測到「exposure to disinformation is positively associated with belief」[c058]。**但兩者都停在「個人對單一敘事的相信」**，不涵蓋母體信任基線或跨域 spillover。

【爭議中】 **環 2（liar's dividend → 逃避問責）有實證，但帶反向邊界條件**：APSR 的五個 survey experiment（n>15,000）證明指控「假新聞」能跨黨派抬高政客支持度——「claims of misinformation ... raise politician support across partisan subgroups」[c050]。但**關鍵邊界**：這些策略「are effective against text-based reports of scandals, but are largely ineffective against video evidence and **do not reduce general trust in media**」[c050]。後者**直接反向約束** FM 的「母體信任基線下降」環：此實證**沒有**觀察到整體媒體信任被拉低。liar's dividend 抬高的是個別政客支持，不是降低整體媒體信任。

【推測】 **環 3（飽和→母體信任基線下降→後續操作更有效）無一手實證**：這是 FM 的完整鏈，也是 brief 命題的核心倍增器主張。**accepted 池中沒有任何一手研究實證這條完整鏈。** c058 被特別任務檢驗後確認**不補此 gap**——它測的是個人對俄烏單一敘事的相信，由意識形態與黨派媒體信任預測，**未**測 cross-domain spillover、母體信任基線、或飽和→後續操作更有效 [c058]；它甚至給出反向線索「trust in mainstream media is negatively associated with belief」（prebunking-friendly）[c058]。c020 把 liar's dividend 接到「對傳統新聞來源信任下降」的宏觀趨勢，但 Chesney/Citron **未提供量測**，屬推論 [c020]。c079 把效果端框為 critical unknown [c079]。accepted 池中**最接近**受眾端的探測是 c062——一份「深偽是否侵蝕認知信任」的 tweet 主題分析——但它是觀察性主題分析、研究對象是**深偽影片**（c050 已證 liar's dividend 對影片無效），測的是圍繞深偽的信任**論述**而非「飽和→母體信任基線下降→後續操作更易」的因果鏈，**因此逼近但不補** FM 環 3 [c062]（依摘要層 sourcing，未經 deep-read 一手驗證）。**FM 環 3 是假設，不是證據。**

【爭議中】 **反框架在效果端的強約束（必須誠實呈現其最強版本）**：Altay 等（qs=5 同儕審查）指「prevalence and impact are overstated」、「Sharing and liking are not believing」、假訊息僅佔「0.15% of the American media diet」、「61% of the French participants did not consult any unreliable sources during the 30 days」、連政治廣告「only have weak and indirect effects」[c035]。Cato 的政策版同源：「only about 0.15 percent of the average American media diet is fake news」、效果「concentrated within populations that already have strong opinions」（congenial misinformation）[c034]。**CD/FM 與此反框架的相容切點**：c035/c034 反的是**個人說服／消費層**——CD **不**主張個人被說服，而主張母體在**特定生態位**辨識成本上升；Altay 的 0.15% 是消費分布，不否證「協同 AI slop 飽和搜尋／推薦生態位、壓低碰到可信來源機率」這個環境結構傷害。但這個切點本身仍需受眾端實證才能從假設升級。其他反框架佐證：c049（第三人效果——人們高估造謠威脅因假設他人易受騙）[c049]（依摘要層 sourcing，未經 deep-read 一手驗證）。

**Confidence**: 低 — FM 完整鏈無一手實證，最強可用環止於個人信念層（c019）與帶反向邊界的 liar's dividend（c050）；c035/c079 是 qs≥4/5 的效果端約束。低 Confidence 是誠實標記，不是蒐集失敗。
**Counter-evidence**: 本 Finding 本身就是以反框架為骨架寫的——c035、c034、c050（影片無效＋不降媒體信任）、c079（critical unknown）、c058（反向線索）共同界定 FM 的有效範圍。沒有反向強證據被隱藏。

### Finding 6（Q6）：各領域主流偵測方法各有結構盲區，且有操作者針對特定方法做對抗工程的記錄

【強證據】 平台偵測的盲區有 NATO StratCom 2025 實驗的硬量化：即使是「歷年最佳」一輪，「an average of 50.4% of identified inauthentic accounts were removed」——意即近半未被移除；逐平台「Facebook removed 39%, while Instagram and TikTok had lower removal rates of 22% and 4%」[c026]。一個官方廣告渠道就能用 €121 買到 17,442 則造假留言 [c026]。這直接量化 Q6「平台內容／CIB 偵測的結構盲區」，並是「單一平台單一方法偵測不足」的機構級實證。

【爭議中】 偵測方法的結構性 gap 有 DISINFOX 團隊的論述：「while the cybersecurity domain benefits from mature threat exchange frameworks, there has been little progress in the automatic and interoperable sharing of knowledge about disinformation campaigns」[c031]——disinfo 情資無法像 cyber threat 那樣自動互通，本身就是盲區。CIB 偵測的訊號碎裂亦有 preprint 記錄：協同訊號高度碎裂、不同群體用不同戰術、偵測與下架執行之間有落差 [c023]（依摘要層 sourcing，未經 deep-read 一手驗證）。

【爭議中】 操作者**針對特定偵測方法做對抗工程**的記錄：Graphika 記錄 GAN-collage（混合盜用照片與 AI 生成成分）比純 GAN 假臉更難偵測，是針對 GAN 偵測器的對抗設計 [c025]（依摘要層 sourcing，未經 deep-read 一手驗證）；c024 自身的偵測法依賴 GAN 頭像「consistent eye placement」artifact，作者明示 2024 後 diffusion 頭像不在涵蓋——偵測法本身會被新生成技術繞過 [c024]；搜尋偵測層有 IEEE S&P 的 linguistic-collision 搜尋中毒量測，記錄規避自動更正以污染搜尋結果的手法 [c046]（依摘要層 sourcing，未經 deep-read 一手驗證）。

【推測】 **金流偵測盲區與「零變現」**：反詐騙的主流方法是追金流；一個近乎零變現的影響力導向協同網絡會讓金流線索歸零。此機制在 Q8 的台灣 YouTube 養生案有具體實例（見 Finding 8），但 accepted 池中針對「反詐金流追蹤盲區」的獨立文獻稀薄——此為已知的 Q6 覆蓋缺口。

**Confidence**: 中 — c026（qs=4 機構實驗）對平台偵測盲區是硬證據；對抗工程記錄多為 qs=4 think-tank（c025）與 snippet 層（c046），方向一致但金流端薄。
**Counter-evidence**: 偵測訊號碎裂（c023）也可被讀成「沒有統一操作者可偵測」而非「操作者刻意躲盲區」——兩種讀法本研究都承認；命題只需要「盲區存在且可被利用」，不需要證明每個盲區都是刻意工程。

### Finding 7（Q7）：跨域整合已有具體、可運行的交換接口——不是「應跨域」口號

【強證據】 **DISARM→STIX2 接口已被實證可運行**：DISINFOX「models the incidents through DISARM Tactics, Techniques, and Procedures (TTPs), a MITRE ATT&CK-like framework for disinformation, with a custom data model based on the ... STIX2 standard」，並「validating the platform with the exchange of more than 100 disinformation incidents」於成熟 CTI 平台 OpenCTI [c030]。姊妹論文給出三件套技術骨架（DISARM TTP 建模 → STIX2 映射 → 交換架構），並自陳「the first academic and technical effort to integrate disinformation threats in the CTI ecosystem」[c031]——表明接口已可運行但仍在早期、未成熟普及。

【強證據】 **IMS 三層框架是跨組織共用操作圖像的一手機構接口**：IMS（由法國 VIGINUM 開發、與 EEAS 達成共識）把分析分為「tactical (incident-level data), operational (narratives and infrastructure), and strategic (linking to threat actors and intent)」[c028]。其 operational 層把**基礎設施**與敘事並列為分析單位——這是 IMS 與本研究 I 軸最接近的對接點。IMS 工作組成員（EU DisinfoLab、CheckFirst、VIGINUM、EEAS、DFRLab 等）本身就是 XD「平台×研究者×公部門協調」的成功先例 [c028]。EEAS 的 FIMI Infrastructure Matrix（Nodes=channels，Edges=關係）是另一個分類接口 [c032]。

【專家意見】 **可制裁／可援用等級證據是 XD 的關鍵門檻**：要把認知破壞從「描述」推進到「處置」，證據品質須跨過 liability 線。EEAS 反覆強調的痛點正是研究者蒐集的資料常不足以支援責任追究；具體技術路徑包括把識別碼（tracker／channel_id／AI 素材雜湊／上傳時間戳）變成可向平台申訴的標的，並以 HMAC 簽章／RFC 3161 時戳／SHA-256 manifest 達到可制裁等級（此路徑源自上游 fimi-ims／kwara program 的設計，本稿作為 XD 接口主張援引，非 accepted 來源證據）。NATO StratCom 2025 亦把解方指向跨平台行為偵測——「a shift towards behavioural detection methods focused on timing patterns, account relationships, and coordinated activity across platforms」[c026]，並提到歐盟制裁框架的法律掛鉤。

【爭議中】 prebunking／inoculation 作為 XD 的受眾端手法有同儕審查支撐 [c077]（依摘要層 sourcing，未經 deep-read 一手驗證）。**接口的覆蓋缺口**：DISARM／STIX／IMS 都是 FIMI／disinfo 導向，**未涵蓋反詐金流端**——XD 的完整接口仍須加上金流／識別碼維度，這是 brief 點名「反詐×反假訊息×平台安全×執法」整合中最薄的一塊。（CheckFirst 的造謠供應鏈集體記錄法可作另一個共享觀測單元接口，但該來源在 INDEX 被列為 thin，本稿不引為證據。）

**Confidence**: 中高 — c030/c031（qs=4，>100 事件已交換驗證）、c028（qs=4 機構框架源）、c032（qs=5）對「接口已存在且可運行」是紮實證據；但「可制裁等級證據」路徑部分源自 program 內部設計、非 accepted 來源，Reviewer 應審計此處歸屬。
**Counter-evidence**: 自由意志主義反方（Cato）主張「Rather than top-down approaches ... embracing greater user control」，警告反制滑向審查 [c034]。本研究把 XD 定位在**基礎設施層偵測×情資交換×可制裁等級證據（對行為者）**，而非內容真偽審查（對言論），以回應此反方——XD 不是擴大內容審查。

### Finding 8（Q8）：兩份台灣一手報告作為命題的具體實例（佐證特定 Q，非組織骨架）

> **定位**：以下兩案是 answer-key（`../draft_v1.md`）已分析的台灣一手報告，在本稿**僅作實例**佐證前述 Q 的特定主張。它們不是研究的組織軸線，本稿也不以「kwara 型／FIMI 型」二分作骨架。案例事實取自 answer-key；其結論不外推超出兩案作者標明的信心等級。

【推測】 **一個 2026 年台灣 FB 外連可疑站案例**（answer-key 案例一）佐證 **Q2 共用 TTP** 與 **Q6 對抗工程**：報告以數位資產層指紋（共用 tracker ID／GA4／GTM／AdSense／私有 CDN 樞紐／TLS 時序）整理出三個操作者群體，自承指紋只能畫「群體邊界」而非「操作者邊界」；其中一群改用 URL path-based 鑑別（而非可剝除的 query 參數），**繞過了「剝參數對照組」這個 cloaking 偵測的主流方法**——這是 Q6「針對特定偵測方法做對抗工程」的單案實例。此案的「動機」端（廣告／影音變現）對應 S 框架，但獲利框架解釋不了「為何協同得如此同質、為何用工業化共用基礎設施」。（單一在地案例，Drafter 推論層；其結論不外推。）

【推測】 **一個 2026 年台灣 YouTube 養生協同網案例**（answer-key 案例二）佐證 **Q1 兩端撞牆**、**Q4 認知破壞機制** 與 **Q6 金流盲區**：以台灣事實查核中心標記的影片為種子、用標題相似度展開，識別 83 個協同頻道；**95% 以上不開任何變現功能**（零變現直接打破「商業內容農場」的獲利框架）、養生內容不違規（打破政治攻擊與內容審核）、報告無法確認外國性——它**卡在 P/S 二分的正中間**，正是 Finding 1 動機分類失效的在地實例。零變現使反詐金流線索歸零（Finding 6 的金流盲區實例）。報告觀察到的「先建信任、再硬轉向（養生→色情／日文勵志／投資）」是 payload 可替換的單案線索，但報告**明確承認沒有養生受眾流動到極化頻道的證據**——對應 Finding 5 的 FM 環 3 gap。（單一在地案例，Drafter 推論層；FM spillover 在本案同樣是未證的 gap。）

【爭議中】 在地脈絡有 Doublethink Lab 的補充佐證：記錄針對台灣的中國資訊操作交織內容農場、與國媒協同、由中港柬經營的 FB 頁、連向簡中內容農場，2024 大選前記錄逾萬則可疑資訊 [c040]（依摘要層 sourcing，未經 deep-read 一手驗證）。這把兩案放進「中文資訊環境同時涉內容農場＋協同操作＋詐騙地理」的在地背景。

**Confidence**: 低 — 兩案是單一在地報告、answer-key 自承歸因未完成、樣本不大；作為「實例」佐證特定主張是恰當的，但不可當作命題的獨立證據基礎（命題的證據基礎是 Finding 1–7 的廣泛來源）。
**Counter-evidence**: 兩案的合流讀法本身是 answer-key 的詮釋；FB 案的「三群體」可能因內容層相似而收斂、YouTube 案的協同可能是共用 playbook 而非同一操作者——兩種替代解釋 answer-key 都未排除。

## Counter-framing engagement

本節明白回應 brief 的 `counter_framing_keywords` 四把鑰匙，集中呈現反框架的最強版本（Dr7：以下段落 tier 繼承來源機制，snippet-only 來源 cap 在【爭議中】）。

【爭議中】 **just_spam（slop 只是低品質演算法副產物、無協同意圖）**：Carrigan 與 Digital Content Next 主張 slop 反映共享演算法誘因結構而非協同 [c016, c017]（依摘要層 sourcing，未經 deep-read 一手驗證）。本研究回應：承認大量 slop 由變現誘因驅動，但這是「動機（獲利）作為可替換 payload」的供給端，不否證 I 軸合流（Finding 3）。

【爭議中】 **just_profit（純獲利、廣告分潤可完整解釋）**：404 Media 把 slop 追到 Creator Bonus 變現供應鏈 [c013]。本研究回應：獲利能解釋「為什麼做」，解釋不了「為何用工業化共用基礎設施＋對抗工程」（Finding 2、6）。

【爭議中】 **no_measurable_effect（效果被高估）**：Altay（qs=5）與 Cato 的 0.15%／效果集中既有信者／暴露≠接受 [c035, c034]，加上 c079 的 critical unknown、c050 的「不降整體媒體信任」、c036（對造謠的無差別警告本身會高估其效果與危險、並產生降低對真實資訊信任的負面下游效果）、c037（信念—意圖—行為關係薄弱、從消費推論接受會誇大負面效果）[c079, c050, c036, c037]（c036／c037 依摘要層 sourcing，未經 deep-read 一手驗證）。本研究回應：**這是本稿最重要的約束，已寫進 Finding 5 的低 Confidence**——CD 限縮在環境層、FM 環 3 明標為假設。

【爭議中】 **shared_vendor_not_actor（共用 vendor 不等於同一行為者）**：c023 的碎裂 CIB 訊號 [c023]（依摘要層 sourcing，未經 deep-read 一手驗證）。本研究回應：命題主張的正是**基礎設施／供應商層共用**，這恰恰使動機歸因更難——與此反框架相容而非衝突（Finding 1、2）。

## What we don't know（證據邊界）

1. **FM 倍增器鏈是命題最弱的一環**：「資訊環境飽和 → 母體信任基線下降 → 後續操作更有效」這條完整鏈**無一手實證**。最強可用環止於個人信念層（c019），且 c050 對「母體信任基線下降」給出**反向**證據（liar's dividend 不降整體媒體信任）。c058 經特別任務檢驗確認**不補**此 gap。要把 CD/FM 從假設升級為結論，最需補的是**受眾端縱貫研究**（institutional trust erosion 量測、跨域 spillover 追蹤）——accepted 池中無此類研究（最接近的受眾端探測 c062 是觀察性 tweet 主題分析、且針對深偽影片，不補此完整鏈，見 Finding 5）。

2. **CD 是詮釋性、可證偽假設，不是已證實事實**：CD「補充了一個獨立新層」是 Drafter 的詮釋；Reviewer 應審計 CD 在哪些段落只是 firehose／flooding／liar's dividend 的改名、哪些段落真有獨立補充。CD 的環境層傷害有供給側結構證據（c032 規模、c048 母體佔比）與機制推論，但**沒有「母體辨識力是否真的下降」的受眾端實證**。

3. **Meta 非歸屬邊界（c001）**：Meta H1 2026 把詐騙中心（10.9M 帳號，scam 類別數字）與隱蔽影響力操作（俄/伊/中三大來源）列為**分開的**執法類別，**未**宣稱兩者共用 tactics／infrastructure [c001]。本稿主張的合流是**本研究詮釋**，證據來自 c010/c024/c008，**不得**掛在 Meta 名下。c001 只提供「兩種工業化操作並存」的並列事實。

4. **c021（Roberts flooding）sourcing gap**：全文未取得（Amazon 零售頁），本稿僅以概念錨援引 Roberts (2018)，**不含逐字一手引文**。若結論要逐字引 flooding 定義，operator 須補 Princeton UP 電子書／圖書館 PDF。

5. **CD↔cognitive warfare 對位來源不足**：accepted 池中唯一 cognitive-warfare 標記的 c022 不提供正式定義（負面發現）。本稿以 c078／c052 替代橋接，但嚴格的機構級對位仍待補（NATO ACT du Cluzel）。

6. **Q6 金流盲區與 Q7 反詐接口薄**：針對「反詐金流追蹤盲區」的獨立文獻稀薄；DISARM／STIX／IMS 接口未涵蓋反詐金流端——XD「反詐×反假訊息×平台安全×執法」整合中，反詐這一塊最薄。

7. **次級（Dr3 摘要層）證據的限制**：本稿多處引用的 c002/c004/c014/c040/c046/c048/c067/c078 等為 snippet 層次級證據（未經 deep-read 一手驗證，tier cap 在【爭議中】）。這些補了 deep-read 未覆蓋的 axis（epistemic-security、computational-propaganda、台灣/scam 群），但其具體細節未經一手核對，Reviewer 引用前宜抽查。

8. **外推範圍**：deep-read 的效果端實證（c050/c058/c035/c034）多為美國樣本／英法樣本，對中文資訊環境／台灣場域不可直接外推；兩個 Q8 台灣案為單一在地報告，結論以中文資訊環境為主。

## Source index

依首次引用順序：

- **c058** — Falling for Russian Propaganda: Factors that Contribute to Belief in Pro-Kremlin Disinformation (Social Media + Society, 2023) — https://doi.org/10.1177/20563051231220330
- **c050** — The Liar's Dividend: Can Politicians Claim Misinformation to Evade Accountability? (APSR, 2024) — https://doi.org/10.1017/s0003055423001454
- **c079** — Generative Language Models and Automated Influence Operations (SIO/CSET/OpenAI, 2023) — https://arxiv.org/pdf/2301.04246
- **c001** — Meta Adversarial Threat Report / Integrity Reports, H1 2026 (Meta) — https://transparency.meta.com/reports/integrity-reports-h1-2026/
- **c010** — This salesperson does not exist (HKS Misinformation Review, 2022) — https://misinforeview.hks.harvard.edu/article/research-note-this-salesperson-does-not-exist...
- **c024** — Characteristics and prevalence of fake social media profiles with AI-generated faces (Yang/Singh/Menczer, OSoMe, 2024) — https://arxiv.org/pdf/2401.02627
- **c008** — The rise of the disinformation-for-hire industry (EUvsDisinfo/EEAS, 2025) — https://euvsdisinfo.eu/the-rise-of-the-disinformation-for-hire-industry/
- **c002** — Disrupting malicious uses of AI: October 2025 (OpenAI) — https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/
- **c004** — Adversarial Misuse of Generative AI (Google GTIG, 2025) — https://cloud.google.com/blog/topics/threat-intelligence/adversarial-misuse-generative-ai
- **c075** — Digital Propaganda: The Power of Influencers (Woolley, J. Democracy, 2022) — https://doi.org/10.1353/jod.2022.0027
- **c038** — China's Exploitation of Scam Centers in Southeast Asia (USCC, 2025) — https://www.uscc.gov/sites/default/files/2025-07/Chinas_Exploitation_of_Scam_Centers_in_Southeast_Asia.pdf
- **c023** — Coordinated Inauthentic Behavior on TikTok: detection challenges (arXiv, 2025) — https://arxiv.org/pdf/2505.10867
- **c032** — 3rd EEAS Report on FIMI Threats — architecture of FIMI operations (EEAS, 2025) — https://www.eeas.europa.eu/sites/default/files/documents/2025/EEAS-3nd-ThreatReport-March-2025-05-Digital-HD.pdf
- **c026** — Social Media Manipulation for Sale: 2025 NATO Experiment (NATO StratCom COE) — https://stratcomcoe.org/publications/download/Social-Media-Manipulation-FINAL-FILE.pdf
- **c070** — The spread of low-credibility content by social bots (Nature Communications, 2018) — https://doi.org/10.1038/s41467-018-06930-7
- **c042** — Disinformation as Collaborative Work (Starbird/Arif/Wilson, 2019) — https://doi.org/10.1145/3359229
- **c051** — Architects of Networked Disinformation (Ong & Cabañes, 2019) — https://doi.org/10.7275/2cq4-5396
- **c054** — Political Astroturfing on Twitter (Keller/Schoch/Stier, 2019) — https://doi.org/10.1080/10584609.2019.1661888
- **c013** — Where Facebook's AI Slop Comes From (404 Media, 2024) — https://www.404media.co/where-facebooks-ai-slop-comes-from/
- **c014** — AI slop is flooding the internet (MIT Technology Review, 2025) — https://www.technologyreview.com/2025/12/23/1130396/...
- **c048** — DeGenTWeb: A First Look at LLM-dominant Websites (He/Ardi/Govindan, 2026) — https://arxiv.org/abs/2605.00087
- **c045** — Crime at Machine Speed: AI's Industrialisation of Deception (Bailo et al., 2026) — https://doi.org/10.3390/sci8030054
- **c016** — You can't understand 'AI slop' without understanding engagement farming (Carrigan, 2026) — https://markcarrigan.net/2026/01/14/...
- **c017** — Where AI slop fits into algorithmic visibility (Digital Content Next, 2026) — https://digitalcontentnext.org/blog/2026/01/13/...
- **c019** — The Russian "Firehose of Falsehood" Propaganda Model (RAND PE-198, 2016) — https://www.rand.org/pubs/perspectives/PE198.html
- **c018** — Information Disorder (Wardle & Derakhshan, Council of Europe, 2017) — https://rm.coe.int/information-disorder-report-version-august-2018/16808c9c77
- **c020** — Deep Fakes: A Looming Challenge (Chesney & Citron, California Law Review, 2019) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3213954
- **c021** — Censored: Distraction and Diversion Inside China's Great Firewall (Roberts, 2018) — https://www.amazon.com/Censored-Distraction-Diversion-Inside-Firewall/dp/0691178860 *(全文未取得，概念錨)*
- **c022** — Hacking Humans / NATO StratCom COE (2023) — https://stratcomcoe.org/publications/the-current-digital-arena-and-its-risks-to-serving-military-personnel/102 *(負面發現：不提供 cognitive-warfare 定義)*
- **c078** — Information as a weapon of mass disruption: from information disorder to cognitive warfare (Pace & Coelho, 2022) — https://doi.org/10.21544/2359-3075.v28n3.g
- **c052** — Digital authoritarianism and the politics of noise (Jovanovic-Harrington, 2026) — https://doi.org/10.2298/fid2601121j
- **c067** — Against Bot Democracy: The Dangers of Epistemic Double-Counting (Tanasoca, 2019) — https://doi.org/10.1017/s1537592719001154
- **c061** — The Distinct Wrong of Deepfakes (de Ruiter, 2021) — https://doi.org/10.1007/s13347-021-00459-2
- **c063** — Epistemic Injustice in Generative AI (Kay/Kasirzadeh/Mohamed, 2024) — https://doi.org/10.1609/aies.v7i1.31671
- **c065** — Echo Chambers and Epistemic Bubbles (Nguyen, 2018) — https://doi.org/10.1017/epi.2018.32
- **c066** — Deepfakes and the epistemic apocalypse (Habgood-Coote, 2023) — https://doi.org/10.1007/s11229-023-04097-3
- **c062** — Do deepfake videos undermine our epistemic trust? A thematic analysis of tweets (Twomey/Ching/Aylett, PLOS ONE, 2023) — https://doi.org/10.1371/journal.pone.0291668
- **c035** — Misinformation on Misinformation (Altay/Berriche/Acerbi, 2023) — https://journals.sagepub.com/doi/10.1177/20563051221150412
- **c034** — The Misleading Panic over Misinformation (Cato Institute, 2024) — https://www.cato.org/policy-analysis/misleading-panic-over-misinformation
- **c036** — Negative Downstream Effects of Alarmist Disinformation Discourse (Political Behavior, Springer, 2024) — https://link.springer.com/article/10.1007/s11109-024-09911-3
- **c037** — (Why) Is Misinformation a Problem? (Adams et al., Perspectives on Psychological Science, 2023) — https://journals.sagepub.com/doi/10.1177/17456916221141344
- **c049** — People believe misinformation is a threat because they assume others are gullible (Altay & Acerbi, 2023) — https://doi.org/10.1177/14614448231153379
- **c025** — Portrait Mode: GAN Collages and Fake Personas (Graphika, 2022) — https://graphika.com/posts/portrait-mode-gan-collages-and-fake-personas
- **c031** — Toward interoperable representation and sharing of disinformation incidents — DISARM↔STIX mapping (2025) — https://arxiv.org/pdf/2502.20997
- **c046** — Measuring and Analyzing Search Engine Poisoning of Linguistic Collisions (IEEE S&P, 2019) — https://doi.org/10.1109/sp.2019.00025
- **c030** — DISINFOX: open-source threat exchange platform (2025) — https://arxiv.org/pdf/2504.01803
- **c028** — Building a common operational picture of FIMI — IMS framework (EU DisinfoLab, 2026) — https://www.disinfo.eu/building-a-common-operational-picture-of-fimi/
- **c077** — Information Warfare: Lessons in Inoculation to Disinformation (Fitzpatrick/Gill/Giles, 2022) — https://doi.org/10.55540/0031-1723.3132
- **c040** — The Chinese Infodemic in Taiwan (Doublethink Lab, 2023) — https://medium.com/doublethinklab/the-chinese-infodemic-in-taiwan-25e9ac3d941e

---

*本稿為政策／防治取向之第一版 insight draft，以 66 份獨立 accepted 來源論證命題鏈。CD／FM 框架為待驗證的可證偽假設；FM 倍增器鏈為命題最弱一環，已逐環標記證據狀態。合流判讀為本研究主張，非任何單一平台立場。歡迎 Reviewer 證偽與補強。*
