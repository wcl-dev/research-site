# Brief — willing-partner-tw

**Project**: Willing Partner：平台對事實查核夥伴的說一套做一套——承諾語料、萃取與撤資行為、夥伴能動性（台灣為主案例）

**Stage**: 0 (Interview complete — 本輪 interview 以對話形式完成，含五路對抗式預審) → 1 (Collect)
**Date**: 2026-07-04

---

## Topic

大型平台（以 Meta 為核心案例）在事實查核合作關係中呈現**進場承諾與退場行為的落差**（say-do gap）：
進場時以「willing partner」語域招募公民社會夥伴（「we rely on fact-checkers」「期待與更多在地查核單位合作」），
夥伴的查核產出被納入平台的偵測與降觸及系統（平台自述為比對基準／each rating 的最大化利用）；
退場時（2025-01 起）以「too politically biased」「a tool to censor」重新定性同一批夥伴，
單方終止資源與支持，而累積的知識資產與據此建立的系統留在平台。

研究以**三幕結構**組織：**A（承諾語料）× B（萃取與撤資行為）＝gap 本體；C（夥伴能動性與槓桿）＝silver lining**。
台灣（TFC、MyGoPen、Cofacts、蘭姆酒吐司）為主案例；D（境外資金生態）僅作背景脈絡。

**方法紀律（本 brief 的憲法條款）**：這是審計不是控訴。核心論證必須釘在**可文件化的行為對照**
（同一行為者、進場 vs 退場、逐字引文），不得依賴動機推論或證據缺席論證當 headline。

## Key questions

- **Q1** [A] 平台進場期（2016–2021）對查核夥伴說了什麼？逐字、具日期、一手來源：Meta newsroom 2016/2018 系列、Facebook 台灣 2019（TFC）/2020（MyGoPen）在地宣言、LINE 訊息查證 2019 上線語料、Google.org 2021 捐贈語料。已有 7 句核實種子（見 seeds/promise-archive-meta.md），缺 2019 Meta 讚 TFC 原話（走 Wayback 補 Facebook Journalism Project 台灣公告）。
- **Q2** [B] 夥伴產出如何進入平台系統？只用平台自述措辭（rating 作為相似內容比對基準、"make the most of each rating"）；「training data」僅得出現在直接引文內。AI 時代平行機制（OpenAI 紅隊→分類器、Anthropic Constitutional Classifiers）作為同構旁證。
- **Q3** [B] 撤資與終止的行為紀錄：2025-01 美國 3PFC 終止全程、CrowdTangle 2024-08 關閉與 MCL 閹割、X API 2023 收費牆、台灣線 TFC 合約 2026-01 到期危機（Meta 佔預算 ~50%，日經口徑）。每項標明「平台留下什麼、夥伴失去什麼」。
- **Q4** [A×B，核心] Say-do gap 對照對：同一行為者的進場語 vs 退場語（Meta newsroom 2018 "we rely" vs 2025 "biased"；台灣 2020 求偶 vs 2025-12 不回應）。對照對必須 same-actor、dated、primary-verified。
- **Q5** [C] 夥伴能動性與槓桿清單：MyGoPen 商模轉身（授權＋教育、不收捐款）、Cofacts 開放策略（可分叉、泰國 fork）、政府反詐需求管道（數位部/刑事局/iWIN）、2020 大選改變平台執法的紀錄、94% 平台問責立法民意。槓桿的理論核心：**在地感測知識會過期，平台拿走的是快照不是感測器**——此句需找可引用的支撐或明確標為本研究論證。
- **Q6** [D，背景] 同一批夥伴的境外資金生態（OSF/NED/OTF/State Dept 地圖已在 seeds/），僅回答：Meta 撤資後的替代財源現實有多薄？NED 關燈梯度作為「上下游雙黑箱」脈絡一句帶過，不展開成獨立軸線。

## Scope

- **Time window**: 2016-12（3PFC 啟動）→ 2026；第二、三幕以 2024–2026 為重心。
- **Geography**: 台灣為主案例；全球機制脈絡（US/EU）僅服務 Q2/Q3 的機制與撤資敘事；不做跨國比較研究。
- **Languages**: zh-TW + en。
- **Depth**: 論證型研究報告；讀者為關注平台問責的政策與公民社會社群；**partner-safe 是硬約束**（見 Failure conditions）。

## Inclusion

- 平台一手文件：Meta newsroom/transparency center、Zuckerberg/Kaplan 原始貼文與逐字稿、LINE 官方公告
- 夥伴一手文件：TFC 官網（FAQ/捐款徵信/年度報告/2025 State of Fact-Checking）、MyGoPen 贊助辦法與公告、Cofacts repo/LEGAL.md/Hugging Face
- IFCN/Poynter 文件、查核組織聯名信
- 具名媒體報導（中央社、日經亞洲、TNL、Rest of World、Tech Policy Press）
- 學術與研究機構：CITR CrowdTangle 調查、台灣韌性社會研究中心民調、Li & Chen (TechPolicy.Press 2025)
- AI 實驗室一手技術文件（OpenAI red-teaming whitepaper、Anthropic Constitutional Classifiers 論文）
- 金流一手資料庫：OSF grants DB、usaspending.gov、OTF 專案頁（seeds/ 已含，Collector 只補缺不重撈）

## Exclusion

- WebFetch/AI 摘要作為引文來源（引文一律 curl 原文核對——見 memory: feedback-webfetch-summary-fabrication）
- 無法溯源到一手出處的流傳語錄（含 seeds 中已標 UNVERIFIED 的 Zuckerberg 2016-11 NPR 轉述句）
- 匿名爆料、未具名「內部人士」說法
- 純意見專欄（Karp 素材除外——其角色是話語標本，非證據）
- 中共官方「NED fact sheet」類文件（seeds 已驗證其無台灣具體內容，只會污染）

## Existing knowledge（operator priors — 經五路對抗式預審，Drafter 以此為起點）

1. **已審計的證據基座**（seeds/extraction-audit-journal.jsonl：40 主張、頂端 20 條全過對抗查證、零 refuted）：
   三個承重錨點＝Meta 自述比對機制（1.8 億則警示）、CrowdTangle 時間軸＋量化損害、OpenAI/Anthropic 自家論文。
2. **措辭地雷清單（違反即 review 打掉）**：
   - 不得以本研究口吻稱 rating 為「training data」（Meta 官方否認字面訓練；用「比對基準／預測地面真值」）
   - 「拿到想要的才走」是動機推論，**不可證**；可證的是「走時承諾清零、資產留存」。政治轉向（2025 美國政局）必須列為對等競爭解釋
   - 「Meta 佔 TFC 預算 50%」溯源=日經轉述，且 TFC 捐款徵信不含平台授權收入（科目不同），引用需雙口徑並陳
   - 「EU DSA 逼平台全球一致」論證已查死（DSA 不強制第三方查核），禁用
   - 證據缺席（「未承諾刪標註」）只能當 caveat 不能當 headline
   - **同主體紀律（禁止移花接木，operator 2026-07-04 明令）**：
     (a) say-do 對照對必須 same-actor **且 same-program**（Meta 3PFC 承諾只能對 Meta 3PFC 退場）；
     (b) OpenAI/Anthropic 素材只能支撐「機制同構」（外部知識→專有系統），**不得支撐「變臉」敘事**——
     兩家無被記錄的求偶→退場弧線，暗示即捏造；在稿中須自成一節並明文標注此限制；
     (c) 「平台」「Big Tech」作主詞的句子不得承重；承重主張一律點名具體行為者；
     (d) 定稿附引文歸屬表（actor × date × 語域 courtship/exit/technical），供 Reviewer 逐格核對無跨主體配對
3. **鋼人讓步（報告必須主動承認）**：ThreatExchange/HMA 開源（BSD）是真實不可撤銷回流；StopNCII 機構已移交；命題收斂為「**現金與存取關係系統性可撤銷；已釋出的碼、已移交的機構、已訓練的人是例外**」。
4. **鋼人已陣亡論證（不得替平台引用）**：「IFCN 聯名信＝顯示性偏好證明合作划算」——預算依賴下的求延續證明議價劣勢，非划算。
5. **Karp 用法**：話語章標本（股東信道德語域 vs 財報電話「kill them」語域的雙聲道落差），不是證人。他與台灣線零連接（七封信無台灣/台積電）。
6. **夥伴保護紅線（operator 關係約束）**：不評價 TFC/MyGoPen/Cofacts 的獨立性或忠誠；他們的損失與能動性只用**他們自己的公開陳述＋可查行為**呈現。

## Process notes

- `reasoning_chain: skipped` — interview 以對話形式完成（非 Interviewer §2.5 產線），命題三次收斂的推理軌跡在 run memory 與 seeds/extraction-audit-journal.jsonl，不另出 reasoning_chain.md。
- validate_gate warnings（Q-marker/qs/keyword 覆蓋、counter_framings 匹配）多為體質誤報：candidates 用 A/B/C/D concept_targets 而非 Q-marker，且 collect 是 seeds 補撈非標準全撈；check 21 引用完整性（唯一 hard-block 級）clean。
- check 22/23 引文/數值回溯因 draft 採「三幕」標題（非 Findings）被 SKIP → 已手動補償驗證兩個承重數字（1.8億 US-scope、10.6%）；工具側 heading 變體擴充記 AUD-B3 後續。

## Reconnaissance seeds (§6b)

`pipeline/seeds/`（本輪對話已收集、多數逐字核對，Collector 從缺口出發、不重撈）：
- `promise-archive-meta.md` — 承諾語料 7 句（6 primary 核實；缺口：2019 Meta-TFC 原話 → Wayback）
- `extraction-audit-journal.jsonl` — 五路×8 主張全文＋對抗查證 verdicts＋價值帳本合成
- `agency-archive-tw.md` — 台灣夥伴能動性檔案＋槓桿清單 8 項＋防雷旗（含未證實項清單）
- `funding-osf-state-google.md` / `funding-otf.md` / `funding-ned-family.md` — D 背景金流圖
- `karp-quotes.md` — 話語章標本 12 句＋書評反面接收
已知待補缺口：TFC 2025/2026 徵信、IFCN 聯名信台灣簽署名單、Cofacts cofacts.tw 授權原文（前次 403）、2019 Facebook Journalism Project 台灣公告。

## Success criteria

1. 每一個 say-do 對照對都是 same-actor、dated、primary-verified；至少 3 對（全球 2 對＋台灣 1 對）。
2. 第二幕機制主張全部使用平台自述措辭；「training data」只出現在引號內。
3. 第三幕槓桿清單至少 6 項有一手證據，且整幕可被夥伴組織直接當「談判籌碼盤點」使用（partner-safe 檢驗：夥伴讀了會轉發，不會抗議）。
4. 動機層只呈現行為結構＋兩個對等競爭解釋（萃取完成 vs 政治轉向），不裁決。
5. 台灣素材逐項標 documented / 查無；「查無」不得升格為否定存在。
6. 全部主張 tier-tagged（Dr1 spec）；核心對照對全數 tier `strong`。

**Failure conditions**:

- headline 依賴證據缺席論證或動機推論
- 任何未經一手核對的引文入稿（含 seeds 已標 UNVERIFIED 者）
- 夥伴被寫成受害者或被收買者（兩者都違反 partner-safe）
- D 背景膨脹成第二主軸（金流圖自己很精彩，但那是另一篇研究）
- 讀起來像 Karp 式的道德檄文——修辭高於帳本即失敗
- **合成大反派**：任何跨主體移花接木（A 家的承諾配 B 家的行為），或以集體主詞掩護單一主體證據——即使只出現一處，整節重寫

## Expected output

`draft/insight_v1.md`（~180–220 行）：
- TL;DR（5 bullets）
- 第一幕：承諾語料（含台灣在地對照組）
- 第二幕：萃取與撤資（價值帳本收斂版＋鋼人讓步內嵌）
- 幕間：say-do 對照對（本報告的承重牆，並列排版）
- 第三幕：夥伴能動性與槓桿清單
- 話語章（短）：Karp 標本與「修辭不可信、帳本可信」的方法自證
- What we don't know（含全部「查無」清單與兩個未裁決的動機解釋）
- Source index
