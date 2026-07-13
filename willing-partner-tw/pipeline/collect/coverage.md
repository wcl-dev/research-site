# Collection coverage — willing-partner-tw

Candidates: 29 | Tracks run: T1 (academic, 1 query), T3 (web: WebSearch + WebFetch + raw curl). T2/T4 不適用（無 sources.yaml；seeds/ 已承擔 curated 角色）。

本輪是 **gap-filling run**：seeds/ 六份已驗證報告承載 A/B/C/D 主體證據，Collector 只補 brief §6b 缺口＋brief_expanded queries 未覆蓋處，刻意不重撈 seeds 已含來源（Meta newsroom 2016/2018/2025、MyGoPen 贊助辦法、Cofacts opendata repo、Li & Chen、韌性社會調查、OSF/OTF/NED 金流等 must_include 均在 seeds，未重複入池）。

## Brief question × track（cell = candidate count；seeds 覆蓋另註）

| Brief Q | T1 academic | T3 web | seeds 已覆蓋 | total new |
|---------|-------------|--------|--------------|-----------|
| Q1 (A 承諾語料) | 0 | 7 (c001–c005, c027–c028) | 7 句核實引文 | 7 |
| Q2 (B 機制) | 0 | 2 (c006, c013) | 比對機制＋AI 旁證全套 | 2 |
| Q3 (B 撤資) | 0 | 9 (c007–c015) | CrowdTangle/X API/日經鏈 | 9 |
| Q4 (A×B 對照對) | 0 | c001+c009 組成台灣對 | 全球 2 對已備 | 2 |
| Q5 (C 槓桿) | 3 (c019–c021) | 9 (c018, c022–c029) | 槓桿清單 8 項 | 12 |
| Q6 (D 背景) | 0 | 2 (c016–c017) | 三份金流圖 | 2 |

## Language

| Language | count | note |
|----------|-------|------|
| zh-TW | 14 | 台灣線一手（TFC 徵信×2 primary-verified、2019 語料×2 primary-verified） |
| en | 15 | 全球撤資敘事＋學術支撐 |

C5 zh-TW T1 gap：學術庫查詢以 EN 跑（label freshness），zh-TW 學術缺口屬預期，台灣線由一手網頁/press 承擔。

## Blind spots（zero / near-zero cells）

- **Q2 × T1 = 0**：預期缺口——Q2 依 brief 憲法只准用平台自述措辭，學術文獻本來就不是合格語源；seeds 的 OpenAI/Anthropic 旁證已足。
- **Q1/Q3 × T1 = 0**：預期——承諾/撤資語料是新聞事件語料，非學術對象。
- **c019 是 Q5「label freshness」的唯一強學術錨**——若 Gatekeeper 刷掉，該論證須依 brief 指示「明確標為本研究論證」。
- **IFCN State of Fact-Checkers 2025 原始報告未收**（TFC 在地化版在 seeds）——若 Drafter 需原始全球數據，需補一筆。
- **Cofacts cofacts.tw 授權原文（缺口#4）未完成**：快照存在已證（c026），內文未展開。

## 驗證紀律報告（quote discipline per brief Exclusion）

- primary-verified = 4（c001, c002, c016, c017）：全部經 raw HTML curl＋逐字讀出，可直接入稿引用。
- press = 14：來源具名可信但引文未逐字核對——引文入稿前須 curl 核對。
- unverified = 11：搜尋摘要或 WebFetch-summary 層級（含 c007 簽署名單這種 load-bearing 主張）——**禁止未核對入稿**，各筆 collection_note 已標下一步。
