# LLM 使用者端偏誤研究（LLM User-Side Bias）

> 來自中國的 LLM（DeepSeek、Qwen、GLM）對台灣社會的威脅，並不在於資料外洩，而在於資訊接收。本研究以 90+ 筆單輪資料與 16 段多輪對話資料，揭露四層結構性風險。

## 三篇公開文章

1. **[前導研究報告](pilot/report.html)**——30 格雲端身份對照實驗的詳細紀錄
2. **[當中國 AI 認得你是台灣人，它選擇隱匿你的歷史](advocacy/index.html)**——整合 90 筆單輪資料，提出三層威脅模型
3. **[當中國 AI 認得你越多，它告訴你的真相越少](multiturn/index.html)**——以多輪對話實驗補上第四層

## 研究架構

| 階段 | 規模 | 主要產出 |
|------|------|----------|
| Stage 1 雲端身份對照 | 30 cells（ChatGPT/Gemini/DeepSeek × TW/HK × N/T/C × Q1/Q2）| 第一篇報告 |
| Stage 1.5 雲端機制隔離 | 5 cells（EN_T / EN_C / SC_T / EN_N / EN_N2）| 證實身份觸發、字體覆蓋宣告身份 |
| Stage 2 地端跨模型 | 55 cells（5 模型 × 11 prompts）| 第二篇文章；揭露權重對齊層 |
| Stage 3 多輪對話腐蝕 | 16 conversations（8 設計 × 2 模型）| 第三篇文章；揭露對話層 |

## 四層威脅模型

```
L4 服務平台層    — 雲端拒絕模板，可見、改用地端即繞過
L3 權重對齊層    — 長度壓制 + CCP 框架烙印於思考鏈
L2 底層模型能力  — abliteration 證明模型本身有完整能力
L1 對話層        — 脈絡修改每一輪行為，統攝上述三層
```

## 目錄結構

```
llm-user-side-bias/
├── README.md                   # 本檔
├── pilot/                      # 實驗執行與結果
│   ├── report.html             # 第一篇文章
│   ├── probe.py                # 雲端先導 probe
│   ├── probe_control.py        # 雲端機制隔離 probe
│   ├── probe_local.py          # 地端跨模型 probe（Ollama）
│   ├── probe_multiturn.py      # 多輪對話 probe（Ollama）
│   ├── analyze_local.py        # 跨模型量化分析
│   ├── responses/              # 雲端 35 cells 原始回應（.txt）
│   ├── responses_local/        # 地端 55 cells 原始回應（.txt）
│   ├── responses_multiturn/    # 多輪 16 conversations（.json）
│   ├── local_analysis.json     # 跨模型對照量化資料
│   └── record.csv              # 雲端 cells 執行紀錄
├── advocacy/index.html         # 第二篇文章
├── multiturn/index.html        # 第三篇文章
└── pipeline/                   # 文獻定位 pipeline
    ├── brief.md, brief_expanded.yaml
    ├── collect/                # 候選文獻（82 篇）
    ├── gate/                   # 篩選通過（64 篇）
    ├── extracts/               # 深讀摘錄（35 篇）
    ├── synthesize/             # 主題整合（11 themes）
    ├── draft/                  # 研究稿
    │   ├── insight_v3.md       # 7500 字學術寫作（V1+V2 整合）
    │   ├── control_experiment_memo.md     # 單輪方法論
    │   └── control_experiment_memo_v2.md  # 多輪方法論
    └── review/                 # 對抗審查紀錄
```

## 如何重現

### 雲端實驗（需要 VPN）

```bash
cd pilot
python3 probe.py setup     # 用瀏覽器登入並儲存 session
python3 probe.py --ip tw   # 跑 18 cells（台灣 IP）
python3 probe.py --ip hk   # 跑 18 cells（香港 IP，需先連 VPN）
python3 probe_control.py   # 5 個機制隔離 cells
```

### 地端實驗（需要 Ollama）

```bash
brew install ollama
ollama pull deepseek-r1:8b qwen3:8b glm4:9b
ollama pull huihui_ai/deepseek-r1-abliterated:8b
ollama pull huihui_ai/qwen3-abliterated:8b
cd pilot
python3 probe_local.py        # 55 cells × 5 模型
python3 probe_multiturn.py    # 16 multi-turn conversations
python3 analyze_local.py      # 產出量化對照
```

完整重現指引另見 [`pipeline/draft/control_experiment_memo.md`](pipeline/draft/control_experiment_memo.md) 與 [`control_experiment_memo_v2.md`](pipeline/draft/control_experiment_memo_v2.md)。

## 研究限制（重要）

- **單一主題**：所有實驗以二二八事件為主，未跨主題（六四、香港、新疆、台獨）。
- **單一模型尺寸**：7-9B distill；未測試 70B+ 模型。
- **多輪每設計僅單次運行**：未做變異性驗證。
- **無非中國源模型多輪對照**：Llama / Gemma 的對話層行為未測。
- **GLM-4 缺解除對齊對照**：huihui-ai 無同尺寸版本。

## 引用方式

如本研究對你的工作有幫助，請以以下方式引用：

```
weichen (2026). LLM 使用者端偏誤研究：四層威脅模型與對話腐蝕。
https://wcl-dev.github.io/research-site/llm-user-side-bias/
```

## License

- **程式碼**（probe.py、analyze 腳本等）：MIT License
- **資料與文字**（responses/、extracts/、文章）：CC BY 4.0

## 未公開項目（隱私考量）

以下檔案於本研究中存在但**故意不上傳公開 repo**：

- `pilot/sessions/`——含登入 cookies，於 `.gitignore` 排除
- `pilot/screenshots/`——35 張瀏覽器截圖。經審視，DeepSeek 介面側欄會顯示部分遮罩的 burner 帳號資訊；為穩妥起見全部排除。回應內容已完整保存於 `responses/` 之 .txt 檔。
- 各種 probe 執行 log——含時間戳與本機路徑資訊
