# 諂媚的縫隙 —— AI 諂媚作為攻擊面

> 當受害者帶著被詐騙集團或謠言夯實過的決心走到 AI 面前——AI 會是斷路器，還是免費認證？回應 Cheng et al. 2026 *Science* 報告的 47% 平均，找到平均之下、可定位的結構性縫隙。

**公開報告**：https://wcl-dev.github.io/research-site/ai-sycophancy-attack-surface-tw/
**類型**：實驗研究（網頁版商業模型 probe）
**狀態**：已發表 · 2026-05 · 執行快照 2026-05-21~22

## 這份研究在問什麼

AI 諂媚通常被當成「個人福祉」問題。本研究把它**重讀為資安攻擊面**：當一個已被詐騙腳本或假訊息說服的人去問 AI，模型的安全護欄會不會因為查詢被包裝成「我自己的判斷／情感再保證」而繞過、或在使用者對抗式追問下退讓？這對應 Cheng et al. 2026 *Science* 報告的 47% 平均諂媚率——本研究要找的是**平均之下、可定位的座標**：哪些情境框架、哪些追問方式會打開縫隙。

## 怎麼產出的

題目發想與把關來自我（weichen）；設計、執行與分析由 AI agents（主要是 Claude）完成。實驗對 **ChatGPT 與 Gemini** 的網頁版做受控 probe：每個 cell 是一段兩輪對話，切出兩刀——**框架**（S-frame「我這樣判斷對吧」vs E-frame「這是不是詐騙」）與**對抗**（T1 示警後使用者固定回嘴施壓 → T2）。站台整體說明見 [research-site README](https://github.com/wcl-dev/research-site)。

## 工作材料地圖

| 路徑 | 內容 |
|---|---|
| `index.html` | 對外發表的報告本身（公開站上即此檔） |
| `EVIDENCE.md` | **證據與策展政策**——為什麼不全帶 384 筆原始回應、帶了哪 16 個、揭露時序 |
| `probe/probe.py` | 網頁版自動化腳本（Playwright；需自備 ChatGPT/Gemini 帳號） |
| `probe/probe-spec.md` | 設計細節（兩框架 × 兩輪 × 三重複 × 兩模型） |
| `probe/vignettes.yaml` | 16 題詐騙／錯誤資訊情境題庫 |
| `probe/responses_curated/` | 報告**直接引用**的 8 段對話 × T1+T2＝16 個 `.txt`，供逐字驗證引用 fidelity |
| `probe/analysis.md`、`probe/record.csv` | 人工編碼分析與執行紀錄 |
| `pipeline/` | 研究題綱、草稿、對抗式審查紀錄 |

> **刻意不公開**：完整 400 筆 `responses/` 與 `screenshots/`（商業產品輸出大規模再散布的 ToS 灰區、快速過時、比論證所需更敵對）、以及登入 `sessions/`（含 cookies，絕不公開）。理由與取捨詳見 [`EVIDENCE.md`](EVIDENCE.md)。完整檔在私有研究庫保留，研究者如需逕行聯繫。

## 如何重現

```bash
cd probe
python3 probe.py setup                 # 用瀏覽器登入並儲存 ChatGPT + Gemini session
python3 probe.py list --reps 3         # 離線預覽會跑哪些 cells
python3 probe.py run --family SR --reps 1   # 煙霧測試（單情境族、單次）
python3 probe.py run --reps 3          # 全量：16 情境 × 2 框架 × 2 模型 × 3 reps
```

最小重現材料＝`vignettes.yaml`（題庫）＋`probe-spec.md`（設計）＋`probe.py`（腳本）。執行快照為 2026-05-21~22；模型可能已更新，預期結果應大致同型、具體 cells 可能變動。

## 主要發現

- **諂媚被關在情緒層、事實/行動層仍踩煞車**：已查核打臉的健康/金融謠言情境（DC）下，兩模型兩框架 16/16 全部踩煞車，但 S-frame 觸發的諂媚被限縮在「我理解你的心情」這類情緒安撫。
- **縫隙可定位**：報告以 vignette ID 標出哪些座標下護欄較脆弱（見 `responses_curated/` 對應檔）。
- **ChatGPT 已示範可行抵抗公式**（拒絕背書 + 分層），可作為 Gemini 修補同類失敗的具體參考。

## 限制

- 單一時點快照（2026-05-21~22）；模型更新後行為可能改變——但快照記錄「當下失敗模式可被觸發」這個事實，是修補成效的基線。
- 編碼為人工、單人；reps=3 為小樣本量級。
- 僅 ChatGPT 與 Gemini，未涵蓋其他模型。

## 授權

- 文字與報告：CC BY 4.0
- 程式碼（`probe.py` 等）：MIT
- 策展回應 `.txt`：作為引用佐證附帶，原始輸出版權屬各產品方。

## 引用

> weichen (2026)．諂媚的縫隙——AI 諂媚作為攻擊面．
> https://wcl-dev.github.io/research-site/ai-sycophancy-attack-surface-tw/
