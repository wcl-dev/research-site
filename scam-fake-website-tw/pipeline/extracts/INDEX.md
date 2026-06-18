# Segmenter index — scam-fake-website-tw

Deep-read budget: 20 / Prioritized: 20 (of 43 accepted)

研究問題:台灣詐騙中「假冒網域／假網站」佔多少比例 —— A(冒名型)與 B(非冒名型)
拆開測量並對照。pipeline 已確立「無單一官方數字」;Segmenter 的工作是把各 proxy
的「確切數字 + 分母 + 日期」抽出來,讓 Drafter 三角測量。

## Deep-read (depth 1 — must；qs=5 全數 + 一手 rescued PDF)

- **c022**: 165_遭停止解析涉詐網站 (open dataset 176455) — 刑事局依詐欺條例第42條停止解析 **48,575** 個涉詐網域(4 個月快照);網站性質 **金融保險 76.2%／電子商務 17.8%**。supply-side 最廣口徑;「網站性質」是產業別非 A/B 軸。
- **c023**: moda 聲請詐騙網域停止解析清單 (open dataset 165027) — 唯一名義可拆 A/B 的官方集;實測 **1,466 列幾乎全為 A 型假冒電商**(假冒類 1,068 + 偽冒電商 393);創建日期 2022→2025:51→214→517→588。
- **c024**: 165_假投資(博弈)網站 (open dataset 160055) — B 型最純 proxy:站次 2021→2024 高峰 17,306、2025 回落 12,362;通報件數 2024 高峰 36,755、2025 降 22,315。Q6 趨勢核心。
- **c029**: 詐欺犯罪危害防制條例 (statute D0080226) — 第42條(停止解析)、第29-41條(平台義務)、第39條(裁罰,Meta 4 次 1,850 萬之依據)。supply-side 制度骨幹。
- **c037**: TWNIC 2025 濫用防制透明度報告 — 2025 全年停止解析 **79,039** 個網域(.tw 844／非 .tw 78,195);「網路釣魚」4,824、「經認定違法濫用」76,930;PhishingCheck 貢獻 2,822。supply-side 最權威縱貫數字。
- **c041**: moda 網詐網 3.0 上線 — 累計通報逾 **43 萬**、確認詐騙逾 **21 萬**(到 2025-11);「金融投資/身分冒充類詐騙較高峰下降 97%/94%」(基準期不明)。
- **c042**: moda 網路詐騙通報查詢網成效報告 (114/6/12) — **operator-rescued 一手 PDF**。通報 **219,616**／下架 **122,119**(Meta 117,845／LINE 1,438／Google 211／TikTok 15／**詐騙網站下架 1,621**／其他 989)。1,621/122,119=1.33% 是唯一獨立計數的「詐騙網站」格。最常被仿冒公眾人物前 20(元大銀行居首)。
- **c043**: 114年詐欺犯罪19.8萬件 (警政統計通報) — 受理案件數分母 **約 19.8 萬件**(2024);官方按「手法」分類、24 歲以上以投資詐欺最多。C 軸根因官方證據。
- **c044**: 114年全般刑案61.48萬件詐欺占32.14% (警政統計通報) — 最外層分母:全般刑案 **614,800 件**、詐欺占 **32.14%**。多層分母換算起點。

## Deep-read (depth 2 — should；qs=4 直接命中 brief 問題 + 必含一手報告救援)

- **c025**: 桃園市查獲前五項詐騙手法統計108-113 (open dataset 171507) — C 軸縱貫證明:6 年官方統計分類軸 100% 是「手法」、無「媒介」軸;投資詐欺查獲人數居首(3,956)。
- **c027**: 嘉義市113年詐欺管道與手法一覽表 (open dataset 52459) — Q7 關鍵示例:罕見有「管道」維度,但「管道」只到 channel(網路詐騙 89%/電話/簡訊),仍切不出「假網站」。
- **c030**: 新北地院 111金訴1726 判決 — B 型一手認定:詐欺機房自架 5 個自創品牌假投資網站(zsdsd/impvcu/highleve14dc/gmb2tw/doublecoin),法院認定「投資群組隨時更換」(快閃輪換)。
- **c031**: 南投地院 114原金易5 判決 — A+B 同案:附表一 8 名被害人含 A(BYBITPRO 冒 Bybit、AliExpress 冒站)與 B(亦莊國際、HOT、buysemu);完整 FB→LINE→假投資網站導流鏈。
- **c032**: 高雄地院 114訴432 判決 — A/B/counter 三樣態:B(信仲金融/安順/裕隆假貸款站)、A(假冒富邦/樂天銀行站、釣魚簡訊停車費站)、counter(IG/FB/探探真平台假賣家,17 人中約 4-5 人無假網站)。
- **c034**: 臺中地院 114審金易10 判決 — **counter-framing 載重證據**:8 名被害人「全部」經真平台假帳號/假客服(DCView/臉書/Threads/蝦皮/新竹物流)受騙,無一經獨立假網站。假網站佔比反向錨點。
- **c040**: 中央社 — moda 網詐網成效 — 最新累計:通報 **508,193**／下架 **247,071**(到 2025-12-18);Meta 移除約 **780 萬則**對台詐騙廣告;Meta 裁罰 4 次共 **1,850 萬元**。
- **c047**: Whoscall 2025年度防詐報告 — Q1 最接近的單一量化:惡意連結中網路釣魚網站約 **30.52%**、惡意軟體下載 35.72%;分母為「惡意連結」非詐騙案件。(主頁 JS-only,以摘要層 + c048 deep-read。)
- **c050**: 台灣數位信任協會《2024冒名詐騙報告書》— A 型業界量化:Watchmen 偵測逾 **300 萬筆**冒名電話簡訊 + **近萬個**詐騙網頁;被冒名對象橫跨政府/金融/電商/電信/影視/零售。(經 Wayback 2025-05-16 救回。)
- **c051**: 台灣數位信任協會《2025社群冒名詐騙報告書》— A 型社群冒名貼文七種類型:貸款申請 **31%**、贈書 26%、投資資訊 17%…;「假網站」是冒名貼文導流三去處之一(另兩條:停留社群、進 LINE 群組)。(經 Wayback 2025-12-12 救回。)

## Fast-skip — snippet-layer usable (Dr3 secondary evidence)

- c038: (`access_status: js_only`, `snippet_status: usable`) — https://rpz.twnic.tw/#/governance — JS SPA 僅得標題;accepted 摘要描述 DNS RPZ 停止解析治理機制,且資料已被 c037 完整取代。Drafter 可引摘要作 RPZ 機制背景。
- c039: (`access_status: ok`, `snippet_status: usable`) — https://twnic.tw/blog/ — TWNIC 部落格資安專欄;accepted 摘要含 RPZ 機制與年度攔阻統計的敘述性說明,可作 c037 的機制補述。
- c046: (`access_status: js_only`, `snippet_status: usable`) — https://165dashboard.tw/ — 165 打詐儀表板 JS SPA;accepted 摘要載「2025 全年約 16.2 萬件／893 億財損」—— 是 Q1 重要分母,Drafter 可依摘要層引用(標 contested、註明依摘要 sourcing),且 165 儀表板本身就是「按手法分類」的核心展示物(C 軸)。
- c048: (`access_status: ok`, `snippet_status: usable`) — https://technews.tw/ — TechNews 轉述 Whoscall 報告;accepted 摘要「惡意軟體下載連結與網路釣魚網站合計佔可疑連結逾六成」可回溯,佐證 c047。
- c049: (`access_status: 403`, `snippet_status: usable`) — https://www.trendmicro.com/zh_tw/security-intelligence/threat-report.html — 趨勢科技頁 anti-bot 403,Wayback 快照僅得 hub landing(無內文)。accepted 摘要載 brief 三個載重數字「96% 詐騙網站 24h 內消失、61.1% 民眾看過假冒品牌詐騙網站、2025 財損增 65%、網購詐騙 2025 年中躍居第一」—— Q4/Q6 核心,Drafter 可依摘要層引用(標 contested、註明依摘要 sourcing 未一手驗證)。
- c050 / c051: 已升為 deep-read（見上,經 Wayback 救回）。
- c052: (`access_status: ok`, `snippet_status: usable`) — https://dtatw.org/scamtracker/ — 數位信任協會詐騙追蹤器;accepted 摘要點明其為民間替代估計工具,Q7 可引為「替代估計法」一例。
- c054: (`access_status: ok`, `snippet_status: usable`) — https://www.cib.npa.gov.tw/...id=1885 — 刑事局打詐新聞索引;accepted 摘要含阻斷詐騙網站、假投資辦公室套路等 supply-side 行動描述,Q5 可引為定性補充。
- c057: (`access_status: ok`, `snippet_status: usable`) — https://www.mof.gov.tw/singlehtml/285 — 財政部防詐頁;accepted 摘要點名「假冒財政部『普發一萬』釣魚網站」具體 A 型事件,Q2 可引為指標案例。
- c058: (`access_status: ok`, `snippet_status: usable`) — https://www.fsc.gov.tw/...id=96 — 金管會防詐專區;accepted 摘要含假投資冒名金融機構/名人警示,Q2 A 型(金融冒名)定性佐證。
- c059: (`access_status: ok`, `snippet_status: usable`) — https://www.moi.gov.tw/News.aspx?n=4&sms=9009 — 內政部高額詐欺財損趨勢新聞;新聞索引頁已滾動、細頁不可達(Wayback 索引快照亦無細頁)。accepted 摘要明確載「假投資/網購詐騙路徑:臉書廣告→LINE群組→詐騙網站」與高額財損集中度 —— 此 funnel 已由 deep-read 的 c031(法院認定)、c051(NGO 報告)雙重一手確認;Drafter 可引摘要,且有 c031/c051 一手背書。

## Fast-skip — no usable evidence / 背景 (excluded from primary evidence pool)

- c001: qs=3_background_only (`snippet_status: thin`) — https://doi.org/10.1109/ACCESS.2025.3540001 — 國際 phishing 偵測系統性回顧;C5 國際可比背景、非台灣 empirics,brief 明令不作台灣結論。Drafter 僅可引為「phishing 佔比抽樣方法」方法論背景。
- c003: qs=3_background_only (`access_status: paywall`, `snippet_status: thin`) — https://doi.org/10.1145/3689938 — 「7 Days Later」phishing 站存活期研究;DOI 轉址 ACM DL,proceedings 頁無單篇全文。國際可比背景,佐證假網站快閃化的方法論,非台灣數據。
- c004: qs=3_background_only (`access_status: 403`, `snippet_status: thin`) — https://doi.org/10.1145/3658644.3690272 — SCAMMAGNIFIER 假購物站量測;ACM DL 403。國際可比背景,B 型量測方法,非台灣數據。
- c008: qs=3_background_only (`snippet_status: thin`) — https://doi.org/10.3390/electronics13193910 — 電商詐騙偵測系統性回顧;國際可比背景。
- c009: qs=3_background_only (`snippet_status: thin`) — https://doi.org/10.1109/ICDSAAI59313.2023.10452509 — 線上詐騙類型 prevalence survey;國際可比背景。
- c021: qs=3_background_only (`snippet_status: thin`) — https://doi.org/10.1109/ACCESS.2026.3605001 — illicit-web 生態 AI 偵測 survey;國際可比背景,Q7 量測挑戰框架。
- c026: qs=3_background_only (`snippet_status: usable`) — https://data.gov.tw/dataset/38262 — 165 詐騙闢謠專區開放資料;A 型案例的定性素材,非量化分母。摘要 usable,Drafter 如需 A 型樣態定性敘述可酌引。
- c028: qs=3_background_only (`snippet_status: usable`) — https://data.gov.tw/dataset/133172 — 臺北市電腦網路犯罪縱貫;網路犯罪附帶趨勢,非假網站專屬,Q6 旁證。摘要 usable。
- c033: qs=3_background_only (`access_status: ok`, `snippet_status: usable`) — 高雄地院 114訴707 判決 — B 型佐證(法院確認假投資平台網頁存在),但細節較薄;c030/c031/c032 已充分覆蓋 B 型,深讀邊際效益低。摘要 usable,Drafter 可作 B 型補充引用。
- c035: qs=3_background_only (`access_status: ok`, `snippet_status: usable`) — 士林地院 114原訴5 判決 — counter 證據(真平台雅虎奇摩購物中心盜刷),單案細節窄;c034 已是更強的 counter 載重證據。摘要 usable。
- c036: qs=3_background_only (`access_status: ok`, `snippet_status: usable`) — 高等法院 114上訴3836 判決 — A 型法律對應(冒用政府機關名義加重詐欺),量化內容薄;c029 已涵蓋法律面。摘要 usable。
- c045: qs=3_background_only (`snippet_status: usable`) — https://www.npa.gov.tw/...id=2218 — 青少年嫌疑犯涉案類型;人口軸旁證,非假網站專屬,Q6 弱旁證。摘要 usable。
- c053: qs=2 (`snippet_status: thin`) — https://dtatw.org/news/ — 數位信任協會新聞索引頁;路由作用已達成(導向 c050/c051 原報告,二者均已 deep-read),自身無獨立證據價值。

## Operator overrides needed

- **c042 一手 PDF 已成功救援並 deep-read**:operator 已把 fraudbuster 403 的《成效報告》PDF 救回本地(collect/primary_pdfs/),Segmenter 已直接讀取一手 PDF 抽出全部載重數字(通報 219,616／詐騙網站下架 1,621 等)。無需再 override。
- **c049 趨勢科技 96%/61.1% 仍未一手驗證**:該頁 403、Wayback 僅得 hub landing。brief 三個載重數字(96% 24h、61.1% 看過假冒品牌站、網購 2025 躍居第一)目前只靠 pre-interview deep-research + 摘要層。若 operator 能從他環境取得趨勢科技《2026 五大詐騙趨勢預測》原報告 PDF,可把 c049 從 contested 升至 strong tier —— 這是 Q4(假網站生命週期)最重要的單一外部數字,值得救援。
- **165 儀表板 c046 的精確手法佔比**:165dashboard.tw 為 JS SPA,各手法(假投資/網購/釣魚)精確百分比未取得;c043/c044 警政統計通報細頁亦 HTTP 400。Drafter 若需「假投資佔受理案件 X%」的精確值,operator 可考慮從 165 儀表板 API 或另一環境補抓。目前可用 c024/c025/c027 的逐站/逐手法聚合 + operator prior「高度依賴假網站類型合計約 4-5 成」三角估計。
