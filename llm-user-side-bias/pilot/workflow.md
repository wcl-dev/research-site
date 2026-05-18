# Pilot 操作 SOP

預計時程：**資料蒐集 ≈ 2.5 小時，編碼分析 ≈ 2-3 小時**。建議分兩個半天完成。

## 0. 前置準備（一次性，~30 分鐘）

### 帳號
- [ ] **ChatGPT**：不用帳號（訪客模式）。確認 chatgpt.com 直接可用
- [ ] **Gemini**：建立一個 burner Google 帳號專用於本研究
  - 帳號設定：**繁體中文介面**、**位置設定為台灣**（避免介面語言污染）
  - 在 gemini.google.com 用此帳號完成一次「你好」對話，確認可用
- [ ] **DeepSeek**：建立一個 burner 郵箱（如 ProtonMail）→ 用此郵箱在 chat.deepseek.com 註冊
  - 繁體中文介面

### VPN
- [ ] 安裝商用 VPN（NordVPN / Surfshark / ProtonVPN 任一）
- [ ] 確認有「香港」出口節點
- [ ] **驗證 IP 切換**：先連香港節點，到 https://whatismyipaddress.com/ 確認 IP 顯示 Hong Kong；斷開後確認顯示 Taiwan

### 瀏覽器
- [ ] 推薦 **Chrome 隱私視窗**（每次重開 = 新 session）
- [ ] 全螢幕截圖工具：macOS 內建 `Cmd+Shift+5` → 選「擷取整個視窗」
- [ ] 建議：螢幕設成單視窗最大化，每張截圖一致

### 工作目錄
- 截圖存：`pilot/screenshots/{model}_{ip}_{identity}_{question}.png`
- 文字存：`pilot/responses/{model}_{ip}_{identity}_{question}.txt`
- 記錄表：`pilot/record.csv`

## 1. 蒐集流程（重複 36 次）

### 每次提問的 9 個步驟

1. **確認 IP 設定**：當前是 TW 還是 HK？（每組 6 個 cell 同 IP 連續做，避免頻繁切換）
2. **開新對話視窗**：
   - ChatGPT：開新隱私視窗 → 到 chatgpt.com → 點「不登入繼續」
   - Gemini：登入後點左上角「新對話」（每次！）
   - DeepSeek：登入後點「New chat」
3. **記錄 model 版本**（如果 UI 顯示）：例如 ChatGPT 顯示「GPT-5」、Gemini 顯示「2.5 Pro」
4. **貼上 prompt**（從 `prompts.md` 複製對應的字串）
5. **送出，等回應完成**（不要中斷生成、不要追問）
6. **截圖整個聊天視窗**（含 prompt + 完整回應）
   - 檔名：`{model}_{ip}_{identity}_{question}.png`
   - 例：`chatgpt_tw_T_Q1.png`
7. **複製回應文字** → 貼到對應 .txt 檔
   - 檔名：`{model}_{ip}_{identity}_{question}.txt`
8. **在 `record.csv` 補資料**（時間、字數、觀察到的 model 版本、初步印象）
9. **關閉視窗**（ChatGPT 用完關隱私視窗就是新 session；Gemini/DeepSeek 下次記得開「新對話」）

### 建議蒐集順序（最小化 VPN 切換）

```
階段 A：TW IP（不開 VPN）— 18 cells
  ChatGPT × {N, T, C} × {Q1, Q2}  → 6 cells
  Gemini  × {N, T, C} × {Q1, Q2}  → 6 cells
  DeepSeek × {N, T, C} × {Q1, Q2} → 6 cells

[切換 VPN 到香港，驗證 IP]

階段 B：HK IP（VPN 開啟）— 18 cells
  同樣 18 cells，但 IP 改為 HK
```

每階段 ~1 小時 20 分鐘。

## 2. 編碼分析（資料蒐集完成後）

依 `rubric.md` 對每個 .txt 回應評分，填到 `record.csv` 的編碼欄位。

完成後，分析以下對比：

| 對比 | 怎麼看 |
|---|---|
| **身份效應** (N vs T vs C) | 同 model、同 IP 下，N/T/C 三個身份的回應在用詞、視角、拒答率上是否系統性不同？ |
| **IP 效應** (TW vs HK) | 同 model、同身份下，TW 和 HK 兩個 IP 是否有差異？ |
| **議題特異性** (Q1 vs Q2) | 上述兩種效應在 Q1（二二八）和 Q2（北韓）上的強度是否不同？ |
| **模型差異** | 哪個模型對使用者端訊號最敏感？最不敏感？ |

## 3. Pilot 成功判準

任一條件成立 → 進入 Stage 2（完整研究）：

- 至少 1 個模型在 Q1 上、N/T/C 之間出現**可肉眼辨識**的回應差異
- 任一模型在 TW vs HK IP 下出現用詞或拒答行為的差異
- 任一模型在 Q1（台灣題）和 Q2（控制題）的使用者端敏感度顯著不同

若 36 cells 全部回應幾乎一致 → 重新思考研究框架（也許要加 prompt 強度、改題目，或承認效應太弱）。

## 4. 注意事項與限制

- **Gemini/DeepSeek 登入了 burner 帳號**：技術上每次「新對話」≠「新使用者」 — 模型可能用帳號歷史推斷。若 pilot 發現顯著差異要謹慎解讀，full study 階段可考慮用多 burner 帳號。
- **VPN 偵測**：商用 VPN 的 IP 池有時會被 Cloudflare 標記。如果遇到 challenge / 拒絕服務，記錄下來、換節點重試。
- **時間漂移**：所有 36 cells 盡量同一天完成。模型每幾週可能熱更新，跨日資料解讀要謹慎。
- **生成隨機性**：LLM 同一 prompt 多次生成本就有差異。pilot 沒做重複，所以單一 cell 的「差異」要從**跨 cell 的系統性 pattern** 來判斷，不是單一句話。
