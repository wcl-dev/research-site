# MOPS 年報 PDF — 操作員手動下載清單

**為什麼需要你下載**：v2 的整個存在理由就是補上 v1 刻意跳過的 MOPS primary-data
層。Collector Track 4 試抓 `mopsfin.twse.com.tw/?co_id=<ticker>`，但該站是 JS SPA、
`co_id` 參數不被吃 → clean-abort（brief.md lines 205-211 已預期）。primary_doc 證據
只能靠人手動下載。

**下載哪裡**：
- 主站 MOPS — <https://mops.twse.com.tw/> → 用「公司代號」查 → 找「年報」電子書 PDF
- 或直接上各公司投資人關係（IR）網站，通常比 MOPS 介面好抓
- 抓 **最新一期年報 PDF**（FY2024 為完整版；若 FY2025 年報已公告則一併）

**年報內該找的段落**（給之後 Segmenter 深讀定位用）：
- 「重要轉投資事業」名單 → 中國子公司設立 / 增資
- 合併財報「營運部門資訊 / 部門別資訊」→ 地區別營收（中國 / 海外佔比）
- 公司治理 / 營運概況中的「中國市場策略」「軍用商規業務」自述段
- 法說會簡報（investor conference）若有，一併

**下載後放哪**：`projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/collect/mops_pdfs/`
檔名建議 `<ticker>_<公司>_年報<年度>.pdf`，例如 `2049_上銀_年報2024.pdf`。
放好後告訴我，我會跑 Collector top-up 用 pdftotext 抽成 primary_doc candidates、
補跑 Gatekeeper，再接 Segmenter。

---

## Tier 1 — 最高優先（PRIMARY 訴求：工具機西進證據）

- [ ] **2049 上銀科技 HIWIN** — 中國子公司、滾珠螺桿產能配置
- [ ] **1583 程泰機械 Goodway** — 大陸轉投資
- [ ] **4526 東台精機 Tongtai** — 中國子公司
- [ ] **6609 瀧澤科技 Takisawa Taiwan** — 海外營運
- [ ] **1590 亞德客 Airtac** — 中國市場營收佔比。⚠️ 原 c050（airtac.net 自家 IR
      年報）已失效（HTTP 404 + TLS 憑證錯誤）；改從 MOPS co_id 1590 抓最新年報。

## Tier 2 — 次優先（雙鏈 nuance：無人機整機）

- [ ] **2634 漢翔航空 AIDC** — 軍規訂單、複材業務
- [ ] **2645 長榮航太 EGAT** — 國防訂單佔比
- [ ] **5206 神通資訊 SYSTEX** — 軍用商規業務
- [ ] **8033 雷虎科技 THUNDER TIGER** — 國防 / 無人艇業務

## Tier 3 — 最低優先（零組件）

- [ ] **5351 鈺創科技 Etron** — AI 視覺記憶體業務

## 範圍外 — 自行斟酌

- [ ] **建準電機 SUNON** — 未上市（brief 註「查 OTC」）。若有公開發行 / 興櫃資料
      可手動補；不在 deterministic 10 家內。

---

**最低可用門檻**：Tier 1 的 4 家（2049 / 1583 / 4526 / 6609）就能撐起 PRIMARY
訴求的工具機西進實證。Tier 2/3 抓得到更好、抓不到不擋 pipeline。
