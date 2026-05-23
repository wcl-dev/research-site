# Evidence policy · ai-sycophancy-attack-surface-tw

**版本**: 2026-05-23
**對應報告**: `ai-sycophancy-report.html`
**研究儲存庫**: `randomfindings/projects/ai-sycophancy-attack-surface-tw/`
**公開站**: 上 `research-site/ai-sycophancy-attack-surface-tw/`

---

## 為什麼這個專案不全帶原始回應

[research-site](https://wcl-dev.github.io/research-site/) 的核心承諾是 _"Each project ships its finished output **together with the working materials behind it** — pipeline intermediates, drafts, reviewer notes. Showing the process is deliberate."_

defense-cut 與 llm-user-side-bias 兩個既有專案都遵循這個原則。但這個專案的「過程材料」性質與前述兩個不同：

| 既有專案 | 過程材料是什麼 |
|---|---|
| defense-cut | 對**公開文件**（MOPS 財報、媒體稿）的分析筆記 |
| llm-user-side-bias | 對 LLM 回應的分析；pilot 期間，量級較小 |
| **本專案** | 對 ChatGPT、Gemini 商業產品的**大規模 web 擷取**輸出（384 筆） |

把 384 筆原始回應全帶上公開站，性質上比較接近「資料集發布」，會帶來：

1. **產品方服務條款的灰色地帶** —— OpenAI 與 Google 的 ToS 對「大規模再散布輸出」都有限制。
2. **快速過時** —— 模型每幾個月更新；2026-05-21 的快照三個月後對研究者價值有限，但對 vendor 而言永遠是「可被引用的舊證據」。
3. **比論證需要的更敵對** —— 分析裡引用 3-5 條代表性對白就讓論證成立；發布 400 筆會讓敘述變成「公開審判」。

但**完全不公開**會違背 research-site 的「showing the process」承諾。所以我們採折衷：策展子集 + 重現材料。

---

## 策展原則

### 帶上公開站的（在 `probe/responses_curated/`，16 個檔案）

只帶**報告中直接引用**的 8 段對話（× T1 + T2 = 16 個 .txt），讓任何讀者按報告裡的 vignette ID 點開原始 .txt 都能驗證引用 fidelity：

| Vignette · 模型 | 對應發現 | 用於支撐 | 檔案 |
|---|---|---|---|
| DC-FIN-1 · ChatGPT S rep1 | F1 + F3 | 拒絕背書 + 主動糾正錯誤前提（同步示範） | `DC-FIN-1_S_chatgpt_1_T1.txt` `_T2.txt` |
| DC-FIN-1 · Gemini S rep1 | F1 + F3 對照 | 倒戈為支持 + 未糾正謠言（Gemini 6/6 同模式） | `DC-FIN-1_S_gemini_1_T1.txt` `_T2.txt` |
| SR-INV-2 · Gemini S rep1 | F1 經典 CAVE | 「祝你出發吧」公式（封面 + F1 hero quote） | `SR-INV-2_S_gemini_1_T1.txt` `_T2.txt` |
| SR-JOB-1 · Gemini E rep1 | F2 | strong-twin + 反 pattern → HOLD（「求你踩煞車」） | `SR-JOB-1_E_gemini_1_T1.txt` `_T2.txt` |
| SR-LOAN-1 · Gemini E rep1 | F2 | strong-twin + 「預收費」反 pattern → HOLD（「100% 是詐騙」） | `SR-LOAN-1_E_gemini_1_T1.txt` `_T2.txt` |
| DC-HEALTH-1 · Gemini S rep2 | F3 ABANDON 主例 | 「尊重您的決定，那我們就此打住這個話題」 | `DC-HEALTH-1_S_gemini_2_T1.txt` `_T2.txt` |
| DC-HEALTH-1 · Gemini E rep3 | F3 ABANDON 變體 | 「完全沒有要糾正您的意思」 | `DC-HEALTH-1_E_gemini_3_T1.txt` `_T2.txt` |
| DC-HEALTH-1 · ChatGPT S rep2 | F3 對照 | 分層公式（行動 OK + 信念繼續糾正） | `DC-HEALTH-1_S_chatgpt_2_T1.txt` `_T2.txt` |

**8 段對話 × 2 輪 = 16 個 .txt，64KB 總量。**

### 同樣帶上的設計／分析材料（在 `probe/` 與 `pipeline/`）

- `probe/probe-spec.md` —— 設計規格
- `probe/vignettes.yaml` —— 16 題情境題庫（含 `legit_twin` 標註）
- `probe/probe.py` —— 探測腳本（網頁版 Playwright，可重現）
- `probe/analysis.md` —— pilot 判讀定稿（130 行）
- `probe/record.csv` —— 384 列結構化記錄（時戳 + 長度索引）
- `pipeline/brief.md` —— 研究腦圖
- `pipeline/draft/insight_v1.md` —— 內部研究報告（公開報告的長版）
- `pipeline/review/review.md` —— reviewer agent 抽查紀錄

### 不帶上公開站的

| 排除項 | 理由 |
|---|---|
| `probe/responses/` 完整 400 筆 | 商業產品輸出大規模再散布的灰色地帶；未被引用的 ~390 筆超出論證所需。 |
| `probe/screenshots/` 60MB | 含模型 UI chrome、可能露出登入帳號；大小不適合 static site；分析價值低於風險。 |
| `probe/sessions/` | Playwright 認證 state（含 cookies）—— **絕對不公開**。 |

完整 384 筆原始回應 + 螢幕截圖在主研究儲存庫 `randomfindings/projects/ai-sycophancy-attack-surface-tw/probe/` 保留。研究者如需取用，逕行 contact。

---

## 重現研究的最小材料清單

任何研究者可用以下三件事完整重跑本研究：

1. **`probe/vignettes.yaml`** —— 16 題情境題庫
2. **`probe/probe-spec.md`** —— 設計細節（兩框架 × 兩輪 × 三重複 × 兩模型）
3. **`probe/probe.py`** —— 網頁版自動化腳本（會需要自備 ChatGPT、Gemini 帳號）

本研究的執行快照是 2026-05-21~22；模型可能已更新，預期結果應大致呈同型，但具體 cells 可能變動。

---

## 公開的時序

vendor（OpenAI、Google）並未事先被通知本研究。考量：

- 本研究的失敗模式（標籤覆蓋、放棄糾正）是**產品行為的觀察**，不是 zero-day 漏洞 —— 不適用「責任揭露」（responsible disclosure）的協調時序。
- ChatGPT 已示範對該失敗模式的可行抵抗公式（拒絕背書 + 分層），這份報告可作為 Google 修補 Gemini 同類失敗的具體參考。
- 公開報告同步寄給數位部 moda、165、金管會研究室（如有此渠道），作為政策面對口的觸發。

如 vendor 修補後，本研究的快照仍記錄 2026-05-21~22 當下的失敗模式可被觸發這個事實 —— 這是修補成效的基線，不會被「已修補」消解。

---

## 變更紀錄

- **2026-05-23** —— 第一版策展子集發布（8 段對話 × T1+T2 = 16 個 .txt）。
