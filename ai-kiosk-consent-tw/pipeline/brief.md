# Brief — ai-kiosk-consent-tw

**Project**: 台灣餐飲業 AI Kiosk 即時 demographic inference 部署的同意機制落差 —— A∩D 灰區研究

**Stage**: 0 (Interview complete, Mode C) → 1 (Collect)
**Date**: 2026-05-26

---

## Topic

台灣許多餐飲業者導入 AI Kiosk 做點餐，其中一群 kiosk 在消費者站到機器前的瞬間就執行**即時 demographic inference** —— 推測年齡、性別、語言、情緒 —— 並依推論結果即時改變畫面（虛擬服務員、商品推薦）。這類部署**往往沒有事前知情同意機制**：店面沒告示、kiosk 沒同意鈕、隱私政策不涵蓋、消費者無法選擇退出。

本研究聚焦在 **A∩D 灰區** —— 也就是「inference 型部署」 ∩「同意機制 axis」的交集 —— 因為這是最尖銳、最有政策意義的問題：
- 業者很可能主張「我們只做即時推論、不識別個人、不存資料，所以不算個資蒐集」
- 個資法第 6 條把人臉、聲紋**未列入特種個資**，法律上有灰區
- 2025/11/11 個資法修正 + PDPC（個人資料保護委員會）籌備中，正是檢視這個灰區的時機點

研究**會跟 B（身分辨識型，如智取櫃人臉取餐）區分計算**，避免把兩種混為一個數字；B、C（會員 PII 資料流）退為對照背景。

## Key questions

> **A** = demographic inference（雙月／金色三麥模式：推測年齡／性別／情緒，不必比對身分庫）
> **D** = 知情同意 axis（告知 / 選擇 / 撤回 三層）
> B（身分辨識）、C（會員 PII 資料流）退為對照／背景

- **Q1a** [A 部署測繪] 台灣餐飲業有多少業者在 kiosk 端部署即時 demographic inference？列出業者、功能（年齡／性別／語言／情緒推測）、技術鏈（edge AI / 上傳雲端 / 第三方 API）、是否與會員系統綁定。**必須跟 B（身分辨識型 kiosk，如智取櫃人臉取餐）區分計算**。
- **Q1b** [A 代表性案例 showcase] 選 2 個代表性部署，詳細描述消費者實際使用情境的完整流程 —— 走進店面 → 站到 kiosk 前的瞬間（kiosk 偵測什麼、多快、消費者知不知道）→ 畫面如何依推論結果變動 → 點餐過程收集了哪些訊號 → 完成後資料去哪（本機刪除 / 上傳雲端 / 進會員 profile）。包含每一步的**時間軸、消費者可見／不可見的動作、產生的資料 artifact**。候選 showcase：雙月食品社 × WiXtar 3-in-1 AI Kiosk；金色三麥 × 星益欣「AI 餐酒實驗室」。
- **Q2** [D — 告知層] inference 型部署有沒有對消費者事前告知？告知層級為何（無 / 店面公告 / kiosk 開頭畫面 / 隱私政策小字）？告知內容涵蓋哪些要素（蒐集目的、項目、留存期限、傳輸對象、撤回機制）？對照個資法第 8 條應告知事項，落差在哪？
- **Q3** [D — 選擇／退出層] 消費者能否選擇退出 inference？人工替代是否可用？退出成本（時間、價格、便利性）有多大？「使用 kiosk 即默示同意」這種 framing 在實作上長什麼樣（畫面、流程、是否強制）？
- **Q4** [A 法律屬性 — 核心 framing 拆解] 「不識別個人、只推論年齡／性別／情緒」這種 demographic inference 在台灣個資法是不是「個人資料蒐集」？個資法第 2 條「特徵」、第 6 條把人臉／聲紋**未列入特種個資**的後果？2025/11/11 修法 + PDPC 籌備中對此有沒有改變？業者「inference 不算蒐集」的法律論證實際能不能站？
- **Q5** [國際對照 — 最低標準參照] GDPR Art. 9 對「biometric data for identification」、EU AI Act 對 emotion recognition + biometric categorisation 的禁止／限制、Illinois BIPA、加州 CCPA、新加坡 PDPA 對「商業空間 inference 型 biometric」的同意要求？哪些是台灣立法或自律可借鏡的最低標準？
- **Q6** [執法 / 申訴實況] 台灣有沒有消費者投訴／民事訴訟／PDPC 函釋／消保處或消基會申訴統計、司法院裁判書、行政裁罰，是針對餐飲場景的 inference 型生物特徵蒐集？實際發生過多少案例？官方／民間執法強度多大？
- **Q7** [業者實體分析] WiXtar 星益欣、Berry AI、銓幻元 MCS、拍檔科技、雙月食品社、金色三麥的公開說明、官網隱私政策、新聞稿對 inference 型蒐集涵蓋到什麼程度？實際 wording 跟個資法第 8 條告知事項、跟 GDPR / BIPA 要求落差多大？

## Scope

- **Time window**: 2023+ 為主（PDPC 籌備處 2023/12/05 成立、AI kiosk 大量導入、個資法 2025/11/11 修法的可比期間）；2020+ 允許作技術／法規背景
- **Geography**: 台灣為主；國際資料（GDPR、BIPA、CCPA、新加坡 PDPA、EU AI Act）僅作對照背景，不作主結論
- **Languages**: zh-TW 為主，en 為輔（GDPR / AI Act / BIPA / 學術 biometric privacy 研究）
- **Depth**: surveillance（部署現況盤點）+ comparative（業者實際做法 vs 個資法應做的 vs 國際最低標準）三軸對照；產出為**可對外發表的政策報告**，目標讀者為 PDPC、立委、消保處、媒體

## Inclusion

- 政府／監管機關文件：PDPC（個人資料保護委員會籌備處）公告／函釋／解釋、法務部個資法解釋函令、行政院消保處申訴統計、數位部 AI 治理政策、公平會（若涉及不公平交易）
- 法律文件：個資法本文（PCode I0050021）、施行細則、2025/11/11 修正案立法理由、相關判決（司法院裁判書系統）
- 業者一手公開資料：雙月食品社、金色三麥、WiXtar、Berry AI、銓幻元 MCS、拍檔科技的**官網隱私政策、新聞稿、案例介紹頁**（業者側 primary source）
- 品質新聞報導：iThome、TechNews、數位時代、CIO Taiwan、foodnext 食力、中央社、自由、聯合 —— 對上述業者實際部署的描述
- 消費者組織：消基會（中華民國消費者文教基金會）刊物／申訴公告
- 國際對照：GDPR Art. 9 + EDPB guidelines、EU AI Act（特別是 Art. 5 對 emotion recognition 限制）、Illinois BIPA + 訴訟案例、加州 CCPA、新加坡 PDPA biometric guidelines
- 學術 / 智庫：ACM CHI / CSCW / FAccT 對 retail biometric privacy 的同儕審查研究（國際可比情境）

## Exclusion

- 純技術 SEO 衛教文（「人臉辨識原理 1-2-3」教學文，無原始案例或法律分析）
- 廠商行銷頁中無實證資料的部分（純產品介紹頁、無部署案例描述、無隱私政策連結）
- 機場海關、邊境、校園、政府機關的人臉辨識（非餐飲零售場景）
- 通用監視器討論（CCTV）— 跟 kiosk 點餐 inference 機制無關
- 純資安 / 駭客攻擊角度的生物辨識討論（資料外洩、深度偽造）— 跟同意機制不直接相關
- 2022 年以前的資料，除非為法規縱貫序列或基礎技術背景

## Existing knowledge（operator priors — fresh start，把 §6b recon 七 fact 當 seed）

operator 選 (a) 全 fresh，pipeline 從零跑。Drafter 視同空白起跑，但 Interviewer 在 §6b 已驗證的七個事實作為 seed：

1. **F1 雙月食品社**：WiXtar 3-in-1 AI Kiosk「先判斷年齡、性別、語言」→ 顯示客製化虛擬服務員（女性顯示美女、男性顯示創辦人）；數位交易佔 90%。米其林必比登。
2. **F2 金色三麥**：星益欣「AI 餐酒實驗室」— 人臉辨識按表情／特徵推薦啤酒；規劃「桌面觀察 AI 系統」偵測空杯／使用頻率。
3. **F3 智取櫃廠商**（如銓幻元 MCS）：「人臉辨識取餐」屬**身分驗證型**（B 區），與 F1/F2 的 demographic inference（A 區）**不同層**，要分開計算。
4. **F4 個資法灰區**：第 6 條特種個資**不含**人臉、聲紋；但因高識別力仍受「一般個資」規範保障（PDPC 籌備處引虹膜為例的論證邏輯）。「inference 不算蒐集」的業者論證是否站得住，是 Q4 的核心。
5. **F5 個資法修法**：2025/11/11 總統公布個資法部分條文修正案，賦予 PDPC 獨立監管職權；**為 AI 全面應用時代建立資料治理**為立法理由之一。
6. **F6 PDPC 籌備處**：2023/12/05 成立籌備處，正式委員會待修法後設立。
7. **F7 業者 framing 灰區**：雙月／金色三麥模式技術上**不一定要把人臉跟身分庫比對**，可純 demographic inference；這給業者「我們不識別個人」的辯護空間 —— 但 EU AI Act Art. 5 對 emotion recognition 與 biometric categorisation 已採禁止／限制立場。

## Reconnaissance seeds（§6b 已找到的 ground-truth）

- WiXtar/news/26 — 雙月食品社 3-in-1 AI Kiosk 案例
- wixtar/blog/18 — 2026 餐飲 AI 應用趨勢攻略（拋出問題的起點）
- foodnext/news/industry/paper/6611085368 — 金色三麥 AI 餐酒實驗室
- cio.com.tw/93910 — 金色三麥人臉導購＋桌面偵測
- technews 2025/05/21 — 星益欣 × 金色三麥
- mcstation.ai/blog/ai-face-recognition-smart-cabinet-guide — 智取櫃人臉辨識（B 區對照）
- pdpc.gov.tw — 個人資料保護委員會籌備處
- law.pdpc.gov.tw — 個資法 + 施行細則
- ey.gov.tw 行政院新聞 — 2025 個資法修法草案通過
- fblaw.com.tw 2025-11-25 — 個資法修正案總統公布

## Success criteria（§8）

**好的最終洞察 — 以下須全部成立**：

1. **量化部署測繪**：列出至少 N 家在 kiosk 端做 demographic inference 的台灣餐飲業者（清單 + 功能 + 技術鏈），且**與 B 區身分辨識型清楚分開**。
2. **2 個 use-case 詳細 showcase**（候選雙月、金色三麥）：消費者實際使用情境的完整時間軸 + 可見/不可見動作 + 資料 artifact 流向。
3. **同意機制三層對照表**（告知 / 選擇 / 撤回）—— 對上述業者每家逐項勾選做到了沒、做到什麼程度，對照個資法第 8 條 + GDPR/BIPA 最低標準。
4. **「inference 不算個資蒐集」業者 framing 的完整法律拆解**（Q4）— 個資法第 2 條／第 6 條／第 8 條解釋、2025/11/11 修法的影響、PDPC 籌備處論證邏輯（虹膜類比）、與 EU AI Act Art. 5 emotion recognition 禁令的對照。
5. **執法現況**（Q6）— 是否有 PDPC 函釋、消保處／消基會申訴、司法院裁判、行政裁罰；若無，明確說「無」並解釋意義。
6. 每個量化數字 **tier-tagged**（per Dr1 spec）；業者公開說法與實際做法之落差有具體 wording 引用。

**失敗條件**：

- 讀起來像「人臉辨識倫理通論」，沒有針對台灣餐飲 inference 型部署的具體實況。
- 把 A（inference）跟 B（identification）混為一談，給出膨脹的部署數字。
- 沒對「inference 不算個資蒐集」這個業者 framing 做完整法律拆解，只 hand-wave「應該不行吧」。
- 同意機制只有 narrative 描述，沒做業者 × 三層的勾選對照表。
- 用 GDPR / BIPA 結論直接當台灣結論，不做台灣個資法的本地分析。
- 沒分開 supply-side（業者部署數）vs demand-side（消費者實際被掃描的暴露率），混用。

## Expected output

`draft/insight_v1.md` —— 政策報告型量化簡報（約 180–260 行），結構：

- TL;DR（5 點，cite-supported，含「A∩D 灰區」核心論點）
- Context（A vs B 區分、§6b recon 七 fact 摘要、PDPC 籌備＋2025/11 修法時點）
- Findings，對應 Q1a/Q1b/Q2–Q7（每點 tier-tagged）
- **2 個 use-case showcase**（候選雙月 + 金色三麥的時間軸 + artifact 流）
- **同意機制三層對照表**（業者 × 告知/選擇/撤回）
- **「inference 不算蒐集」法律拆解**（個資法 + EU AI Act + PDPC 論證對照）
- 國際最低標準對照（GDPR / BIPA / CCPA / 新加坡 PDPA / EU AI Act）
- 執法 / 申訴實況
- 資料缺口與政策建議
- Source index

審查：**multi_model**（Claude + Codex + Gemini 平行 + meta-merge），fidelity_level: high
