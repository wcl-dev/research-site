# Pilot 階段

## 目的

驗證「使用者端訊號（IP + 身份自陳）影響 LLM 回應」這個假設**有沒有可觀察的效應**，並驗證操作 SOP 順不順。

## 規模

**36 cells**（3 模型 × 2 IP × 3 身份 × 2 題）

| 文件 | 用途 |
|---|---|
| [`prompts.md`](prompts.md) | 6 個 prompt 完整字串 + 為何選這 2 題 |
| [`workflow.md`](workflow.md) | 操作 SOP — 前置準備、蒐集步驟、編碼流程 |
| [`rubric.md`](rubric.md) | 6 個維度的編碼準則 |
| [`record.csv`](record.csv) | 36 cells 已預填基本欄位，蒐集時填入觀察 |
| `screenshots/` | 截圖存放（命名：`{cell_id}.png`）|
| `responses/` | 文本回應存放（命名：`{cell_id}.txt`）|

## 預計時程

| 階段 | 時間 |
|---|---|
| 前置（VPN、burner 帳號）| ~30 min |
| 蒐集 TW IP 18 cells | ~80 min |
| 切換 VPN + 驗證 | ~10 min |
| 蒐集 HK IP 18 cells | ~80 min |
| 編碼分析 36 個回應 | ~2-3 hr |
| **合計** | **~半個工作天 + 一個編碼日** |

## 成功判準（任一即繼續 Stage 2）

1. 同模型、同 IP 下，N/T/C 三身份在 terminology / perspective / refusal 任一維度出現可見差異
2. 同模型、同身份下，TW IP 和 HK IP 出現可見差異
3. Q1（台灣題）和 Q2（控制題）的使用者端敏感度明顯不同

若三條件都不滿足 → 重新思考研究框架（見 rubric.md 末段）。

## 開始之前的檢查清單

- [ ] 已建立 Gemini burner 帳號（繁中介面、位置台灣）
- [ ] 已建立 DeepSeek burner 帳號（繁中介面）
- [ ] 已安裝商用 VPN，確認有 HK 出口節點
- [ ] 已在 https://whatismyipaddress.com/ 驗證能切換 TW ↔ HK IP
- [ ] Chrome 已準備好（隱私視窗）
- [ ] 截圖工具就緒（macOS `Cmd+Shift+5`）
- [ ] 開好兩個 Finder 視窗指向 `screenshots/` 和 `responses/`

完成後，依 [`workflow.md`](workflow.md) 開始蒐集。
