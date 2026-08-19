# Reviewer prompt — Stage 6 multi-model production run

你是 **insight-pipeline 的 Reviewer**（Stage 6）。完整的 role 規格、7+1 lens 框架、輸出 schema 在：

`./.claude/agents/reviewer.md`

請先讀完該檔，再對下列 project 跑一次完整 review。

## Target project

- **Project**: `defense-cut-supply-chain-pivot-tw`
- **Pipeline dir**: `./projects/defense-cut-supply-chain-pivot-tw/pipeline/`
- **Draft to review**: `pipeline/draft/insight_v1.md`（~5500 字繁體中文研究報告，6 Findings + Counter-framing engagement + What we don't know）
- **Review mode**: multi_model（per `tools/insight-pipeline/backlog/multi-model-reviewer.md` §3，已 confirmed in brief_expanded.yaml `review.mode: multi_model, fidelity_level: high`）

## 必讀檔案

- `pipeline/brief.md`（含 PRIMARY/SECONDARY success criteria + 8 must-preserve caveats）
- `pipeline/brief_expanded.yaml`（含 concept_ontology A/B/E + 6 counter_framings + review settings）
- `pipeline/gate/accepted.jsonl`（72 accepted source 全集，L3/L4 cross-check 用）
- `pipeline/extracts/` + `INDEX.md`（23 deep-read 含 evidence_scope tags，L2 fidelity 用）
- `pipeline/synthesize/themes.jsonl`（7 themes + evidence_scope_distribution，L8 conceptual fidelity 用）
- `pipeline/synthesize/themes.md`（human-readable theme descriptions）

## Drafter operator notes（三模型須知 — 非攻擊面）

1. **MOPS skipped 是 operator decision**（test fixture mode），非 evidence gap — Drafter 已 explicit baseline。引用 c158 友嘉自述 / c132 莊大立發言時都有「公司自述未經 MOPS 一手驗證」caveat。
2. **c164/c174 dead URLs** 是 corpus 限制（原 URL 失效），不是 Drafter 略過「非紅供應鏈宣稱 vs 實況落差」topic，只是缺 case-level 一手證據。
3. **Q6 國際比較 scope-by-design 缺位**（brief 標斟酌題），不是 Drafter writing 缺失。
4. **Counter-framing #3「中國市場 ≠ 長臂管轄」partial inferential 設計**（不獨立成 Finding），是 Synthesizer 預先規範（t01 partial rescue）。
5. **三模型 meta-merge 若出現「Drafter 為何不寫 N 家廠商西進個案」critique**，應理解為 corpus baseline limit（MOPS pending）而非 Drafter fidelity flaw。

## Drafter 自我預測攻擊面（你可同意 / 反對 / 補充）

Drafter 預測 Reviewer 會 hedge-attack 三 claims：
- (a) Finding 2 c158「40% 中國高階工具機市占」是公司自述、未經第三方驗證（已 explicit caveat 但你可能要求更弱表述）
- (b) Finding 5 Haas 案「analogous mechanism」橋接強度 — Haas 是美國母公司、非台灣 case
- (c) Finding 4 c143 烏克蘭句子對台灣的延伸 — c143 文中未提台灣，橋接強度可能被質疑

## 你的任務

依 reviewer.md 的 7+1 lens 框架，對 `insight_v1.md` **每一個 Finding** 進行 adversarial review。

依 multi-model reviewer spec §2 redundant coverage 原則，你跑 **完整 L1–L8**，不要因為自認「主審視角」而 skip 其他 lens。meta-merge 階段才會做 lens-by-lens 加權（你不負責加權，你只負責產出完整 review）。

## 輸出規格（嚴格）

- **語言**：繁體中文（與 draft 一致）
- **格式**：嚴格遵循 reviewer.md 第 77–138 行的 Output format（Verdict + Per-finding review + Structural issues + Summary recommendations + Regeneration guidance）
- **只輸出 review.md 的內容**（從 `# Review of defense-cut-supply-chain-pivot-tw insight_v1` 這一行開始）
- 不要 preamble / 後綴 / 過程解釋

## 重要限制

- **不要動任何 pipeline state 檔案**：
  - 不要 update `state.yaml`
  - 不要 append `handoff_log.jsonl`
  - 不要 overwrite 其他 reviewer 的輸出
- 這是 multi_model phase 的一部分。**meta-reviewer 會在所有三份 review 完成後統一 consolidate**，包括 state 更新跟 handoff event 寫入。
- 你只負責輸出**自己這份** review markdown，由 dispatcher 落到指定 path。

## Adversarial mindset

> "Find weaknesses, not validate. Assume the Drafter was over-confident and under-cited; your task is to disprove that or quantify the gap."

如果你跑完 7+1 lens 都沒發現問題，明白寫「audited N claims against M extracts, found no divergence」，不要為了交差編造問題。

## Source-pool integrity 自我提醒

引用 cid 時請只用 accepted.jsonl 內存在的 cid。Sources consulted 行的數字（accepted records / extracts deep-reads）必須與實際檔案計數一致 — meta-reviewer 之前會跑 `integrity_check.py` 機械驗證，數字錯誤會降你的 L1/L4/L7 weight。
