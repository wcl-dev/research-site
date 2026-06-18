# Brief — cognitive-disruption-tw

**Project**: 似是而非內容的動機合流與「認知破壞」—— 為何協同式 AI slop 已無法用「政治攻擊／詐騙獲利」二分解釋，及跨域防治的結構必要性

**Stage**: 0 (Interview complete, Mode B 自主) → 1 (Collect)
**Date**: 2026-06-16

---

## Topic

過去解釋網路可疑內容用兩條軸線：**政治攻擊**（FIMI／認知作戰／影響力操作，判定核心是意圖與外國性）與**詐騙獲利**（內容農場／廣告變現／釣魚，判定核心是金流）。本研究主張：面對由生成式 AI 大量生產、高度協同的「似是而非內容」（AI slop），這個二分法正在系統性失效——

- 不同動機的操作**共用同一套工業化基礎設施與 TTP**（批量身分生產、AI 素材複用、cloaking、跨語言帳號供應鏈、資產輪替、針對主流偵測方法的對抗工程）；
- 動機（政治／獲利）是這套基礎設施上**可替換的 payload**，而非操作的本質；
- 其首要傷害不在於說服特定個人或詐騙特定金額，而在於以海量內容**飽和資訊環境本身**、壓低整個母體的信任與辨識基線——本研究稱為**「認知破壞」（cognitive disruption）**：一種無差別、基礎設施層的傷害，作為所有後續惡意操作的**加乘效應（force multiplier）**。

研究要論證的是這個**命題**（以廣泛的學術文獻、各國威脅情報、平台揭露為證據基礎），而非單一案例描述。手上兩份台灣一手報告（FB 外連可疑站／YouTube 養生協同網）作為命題的**案例佐證之一**（answer-key），**不是研究的組織軸線**——草稿不應以「kwara 型／FIMI 型」二分作骨架。

研究同時要論證**防治的結構必要性**：若動機標籤本身是錯誤分類軸，則以動機分工的防治體系（反詐／反假訊息／內容審核／威脅情報各管一塊）必有結構盲區，操作者正住在盲區交界；唯有跨域整合（多偵測方法疊加、共用交換接口）能收斂盲區。

## Key questions

> 命題鏈：(P ∪ S) 失效 → I 共用基礎設施 → CD 認知破壞（FM 倍增器）→ 需 XD 跨域防治
> P=政治攻擊框架　S=詐騙獲利框架　I=共用工業化基礎設施　CD=認知破壞(harm model)　FM=force multiplier　XD=跨域整合

- **Q1 [動機分類失效／合流]** 學術與威脅情報界如何分類協同操作的動機（影響力 vs 財務獲利 vs 其他）？有哪些已記錄案例顯示「financially-motivated 與 influence operations 界線模糊／合流」？平台（Meta／Google／OpenAI）與機構（EEAS／DFRLab／Stanford IO）報告怎麼描述這個趨勢？
- **Q2 [共用工業化基礎設施與 TTP]** 不同動機的操作是否共用同一套基礎設施與 TTP——批量帳號（bulk creation）、AI 生成人設與影像、cloaking／偽裝、跨語言帳號供應鏈（account farm）、資產輪替與重新分配、中介者（bulletproof hosting／amplification）？跨案例的證據與 DISARM／ATT&CK 對齊在哪？
- **Q3 [AI slop 的角色與規模效應]** 生成式 AI 如何降低協同操作的邊際成本、改變其規模與形態？「AI slop」作為現象，學界與業界如何描述其對搜尋／推薦／資訊環境的影響（flooding、SEO 污染、synthetic media 氾濫）？
- **Q4 [認知破壞作為傷害模型]** 既有哪些框架描述「對資訊環境本身的傷害」——information disorder（Wardle/Derakhshan）、epistemic security、firehose of falsehood、liar's dividend、information pollution、認知作戰／cognitive warfare、censorship through noise？本研究主張的「認知破壞＝無差別 force multiplier」與這些框架有何異同、補充了什麼？哪些已有實證、哪些仍是推論？
- **Q5 [force multiplier 機制與其證據狀態]** 有沒有實證或理論支持「資訊環境飽和 → 信任基線下降 → 後續操作（詐騙／政治）更有效」這條倍增器鏈？受眾端有沒有量測（institutional trust erosion、audience capture、pre-bunking、cross-domain spillover）？這條鏈哪幾環有證據、哪幾環仍是 gap？**（誠實標記證據邊界）**
- **Q6 [偵測方法的結構盲區]** 各領域主流偵測方法——CIB 帳號互動偵測、平台內容違規審核、反詐金流追蹤、數位資產指紋——各有什麼結構盲區？文獻／報告有沒有記錄操作者「針對特定偵測方法做對抗工程／住在盲區交界」的案例？
- **Q7 [跨域整合框架與交換接口]** 有哪些既有的跨域整合框架與交換接口——DISARM、STIX/TAXII、EU DisinfoLab IMS、EEAS FIMI、ABCDE／SCOTCH／BEND 等 disinfo 分析框架、liability-grade evidence／可制裁等級證據？跨機構（反詐 × 反假訊息 × 平台安全 × 執法）協作的具體障礙與成功先例？
- **Q8 [在地案例佐證]** 手上兩份台灣一手報告（FB 外連可疑站／YouTube 養生協同網）如何作為上述命題的具體實例？各自佐證哪幾個 Q（特別是 Q1 兩端撞牆、Q2 共用 TTP、Q4 認知破壞機制、Q6 偵測盲區）？**這些案例是實例，不是主軸。**

## Scope

- **Time window**: 2016+ 為主（俄式 firehose／2016 後 CIB 概念成形／2017 information disorder／2022 FIMI-EEAS／2023+ 生成式 AI slop）；經典理論（censorship through noise、propaganda）允許更早作背景
- **Geography**: 全球文獻與威脅情報為主結構；台灣兩案作在地實例；中文資訊環境為主要受害場域
- **Languages**: en 為主（學術與威脅情報主體），zh-TW 為輔（在地案例、認知作戰在地研究）
- **Depth**: 論證型（argument）為主——把「合流→認知破壞→跨域必要」建立成一條**可被證偽的命題鏈**，明白標出哪幾環有實證、哪幾環是推論；comparative 為次（比較動機框架、比較偵測方法）；產出為政策／防治取向的草稿，目標讀者為跨機構防治、平台治理、政策制定者

## Inclusion

- **平台威脅揭露**：Meta Adversarial Threat Reports（含 H1 2026）、Google TAG／Mandiant、OpenAI "Disrupting malicious uses of AI"、平台透明度報告
- **機構／智庫**：EEAS FIMI Threat Report、EU DisinfoLab、DFRLab、Stanford Internet Observatory、RAND（firehose of falsehood）、Carnegie、ASPI、NATO StratCom COE（認知作戰）
- **學術同儕審查**：information disorder、coordinated inauthentic behavior、computational propaganda、epistemic security、influence operations taxonomy、content farm／SEO spam、synthetic media trust、detection evasion
- **框架文件**：DISARM（disarmframework.com）、STIX/TAXII（OASIS）、ABCDE（Camille François）、SCOTCH、BEND（Carley）、EU DisinfoLab IMS
- **在地**：台灣事實查核中心、IORG、Doublethink Lab、台灣兩案一手報告（answer-key）、認知作戰在地研究
- **AI slop 現象調查**：品質科技媒體（404 Media、The Verge、MIT Tech Review、Wired）對 AI 內容農場／slop 的調查

## Exclusion

- 純技術 SEO 教學文、無實證或框架的行銷內容
- 與「協同操作／資訊環境傷害」無關的一般 AI 倫理泛論
- 個別事實查核條目（單則假訊息的真偽判定），除非用作 TTP 或機制的實例
- 純國際關係地緣政治評論，無資訊操作機制分析
- 2010 年以前資料，除非為理論基礎（propaganda、censorship through noise）

## Existing knowledge (answer-key / seed)

- `../draft_v1.md` — 命題種子（第一次直接綜合，以兩案二分為骨架；其框架待 pipeline 由獨立證據佐證後取代）
- 上游 program `projects/fimi-ims/`：EU DisinfoLab IMS 框架（戰略／操作／戰術三層）、kwara→IMS 整合規劃、DISARM 用法
- 相關前作：`ai-cognitive-infrastructure-tw`（需求側說服效果，與本稿供給側基礎設施互補）、`scam-fake-website-tw`（冒名／cloaking）

## Success criteria

1. 用**至少 3 個案例（非僅手上兩案）**佐證「financially-motivated 與 influence ops 共用基礎設施／合流」。
2. 把「認知破壞」對位到既有框架（information disorder／epistemic security／firehose／liar's dividend），講清楚**補充了什麼、哪裡是新主張**。
3. force multiplier 那條鏈**逐環標記證據狀態**（實證 vs 推論），不誇大。
4. 防治段給出**具體交換接口**（不是「應跨域」口號），對位 DISARM／IMS／STIX／可制裁等級證據。
5. 兩案以**實例**身分出現（佐證特定 Q），不作組織骨架、不通篇「kwara 型／FIMI 型」。
