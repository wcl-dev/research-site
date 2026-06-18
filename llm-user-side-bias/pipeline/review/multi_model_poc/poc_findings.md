# Multi-model Reviewer PoC — Findings note

**Date**: 2026-05-18
**Target**: `projects/llm-user-side-bias/pipeline/draft/insight_v2.md` (211 lines, Dr1 positioning memo)
**Models**: Claude (Sonnet, reviewer subagent) / Codex (gpt-5.5, CLI exec) / Gemini (CLI -p, plan mode)
**Outputs**: `claude.md` (266L) / `codex.md` (223L) / `gemini.md` (127L)

每個模型讀同一份 [reviewer_prompt.md](reviewer_prompt.md)，自行 agentic 讀 brief / draft / accepted.jsonl / extracts/。

## 差異 matrix

| 維度 | Claude | Codex | Gemini |
|---|---|---|---|
| Finding 切片 | 6（TL;DR + 章節一–五）— 唯一辨識出 Dr1 positioning memo 格式 | 6（信心表 6 列） | 4（粗顆粒，合併） |
| Verdict 分布 | 3✅ / 3⚠️ / 0❌ / 0🚨 | 0✅ / 4⚠️ / 2❌ / 0🚨 | 2✅ / 2⚠️ / 0❌ / 0🚨 |
| Overall | 🟢 publishable with minor edits | 🟡 needs revision | 🟡 needs revision |
| L8 處理 | 語義版抽樣（注意到 v2 是 Dr1 格式，state.yaml 明說） | 機械觸發 missing_scope_tag（每 finding 都標） | 列為 "Critical structural issue"（最嚴格） |
| 數據準確性 | accepted: 32 / extracts: 17 — 正確 | accepted: 32 / extracts: 21 — 正確 | accepted: 45 / extracts: 22 — **錯誤**（實際 32） |
| 來源完整性 | 引 cid 全部 in accepted | 引 cid 全部 in accepted | **提及 c213（不在 accepted）— hallucinated cid** |

## 各自獨有的 catches（cross-model novelty）

### Claude 獨有

1. **TL;DR + Section 一「美國中心 / 從未延伸至國族身份」vs c011 nationality 變項的細緻語義張力** — 對照 c011 extract caveat「Nationality is one of three identity variables tested」，指出措辭過強。Codex 抓到了類似但比較表面（"too broad"），Gemini 完全沒抓。
2. **c037 PoliTune 概念維度落差** — 西方左右光譜 vs. 國族／地緣政治維度的延伸，這個概念差只有 Claude 明確點出。
3. **v1 review baseline 追蹤** — Claude 唯一讀了既有 review.md，所以能說「v1 的 OC1/OC2/OC3/OC4/OC5 critical 修正落地」並把本次定位為「修正是否徹底 + 殘留弱點」。
4. **理解 Dr1 positioning memo 格式合約彈性** — 知道 state.yaml 寫了「未採 Dr2 tier-tagging」，把 L8 改為語義版抽樣。

### Codex 獨有

1. **c001 explicitly disclaims causal linkage** — 抓到 Drafter「刻意設計的存取管制政策」與 c001 原話「does not establish a causal linkage」的硬性衝突。**這是三份中唯一抓到 causal language overreach 的**。
2. **De Man hedge fading**：原文「suggesting post-generation filtering」→ Draft「顯示審查是後生成的輸出層過濾」— suggestion → conclusion 的擴大解讀。
3. **Ko c005 詮釋 overreach**：Drafter 把 Ko 解讀成「審查是身份驅動非語言驅動」— Codex 指出 Ko 實際只支持 non-language-selective censorship，不支持 identity causation。
4. **三類 claim 必須分開**：model-origin geopolitical bias、language-triggered framing、declared-identity-triggered differential access — 系統性提出「合併三種機制是 v2 的核心問題」。
5. **覆蓋面最廣的 overlooked sources（L4）列舉**：c006 / c017 / c022 / c024 / c025 / c026 / c030 / c031 / c032 / c044 — 全面 cross-check accepted set。

### Gemini 獨有

1. **c213 補強建議** — 但 **c213 不在 accepted.jsonl，是 hallucinated cid**。
2. **強制 L8 修正作為 publishable 首要條件** — 比另兩個更要求 Drafter 補 scope tag（雖然 v2 是 Dr1 格式可豁免）。
3. **「合宜 → 知識滅絕」的概念連結建議** — 把 c033 epistemicide 與 pilot 二二八觀察更緊密結合的建議，是 Gemini 唯一明確提出的概念延伸。

## 模型行為特徵

| | Claude | Codex | Gemini |
|---|---|---|---|
| 對 pipeline 內部 schema 熟悉度 | 高（讀 state.yaml notes、辨識 Dr1） | 中（不知 Dr1，照 Dr2 機械跑） | 低（不知 Dr1，且數錯 records） |
| Adversarial 強度 | 中（v1 已落地，傾向認可） | 高（causal overreach 全面抓） | 中低（多項 ✅ solid） |
| L2 fidelity 細緻度 | 細（含意譯品質判斷） | 細（含原文 vs draft 措辭精確比對） | 中（多為對應正確/不正確的二元判斷） |
| L4 overlooked sources 覆蓋 | 中（c006 + Q2 epistemic 群） | 高（10 個額外 cid 列舉） | 低（c017 / c024 / c030 各一） |
| 寫作 verbose 度 | 高（266L） | 中（223L） | 低（127L） |
| 出錯類型 | 偏寬容（critical 已落地的假設） | 偏嚴厲（causal claim 全部要 hedge） | 數據錯誤 + hallucinated cid |

## Spec 設計含意（給後續 multi-model-reviewer.md spec 起草用）

### 1. Meta-merge 不是平均，是「分工 + 互補」

三個模型的盲點互補，平均化會稀釋價值：
- **Claude 是 schema-aware reviewer** — 處理 pipeline 內部格式合約（Dr1/Dr2、state.yaml notes、既有 review baseline）。
- **Codex 是 causal-overreach hunter** — 抓 Drafter 對 source 信心的過度延伸（「suggesting → showed」「does not establish causal → 刻意設計」）。
- **Gemini 是粗顆粒結構審** — 看大方向格式合約，但細節 fidelity 與 source pool 完整性可能出錯。

Spec 應該明定**每個模型的「主審視角」**而非要求三份都用同一份 7-lens checklist。例如：
- Claude → L2/L6/L7/L8（fidelity + structural + schema-aware）
- Codex → L1/L3/L4/L5（citation + counter-evidence + overlooked + calibration）
- Gemini → L1/L8（粗框 + 格式合約強制）— 但 source pool 引用必須 cross-check Claude/Codex 的 cid 集合。

### 2. Source pool integrity 必須有 cross-check

Gemini 出現 hallucinated cid（c213）+ 數錯 records — 這在生產 review 中是 hard error。Spec 必須要求：

> 每份 review 的所有 `[cNNN]` 引用，meta-merger 必須 cross-check against `accepted.jsonl`。不在 accepted 的 cid → flag 為 model_hallucination；數字（記錄數、extracts 數）必須與實際檔案計數一致。

### 3. Finding boundary alignment 是 meta-merge 第一步

三個模型對「v2 算幾個 Finding」答案不同（6 / 6 / 4）。meta-merge 前必須先對齊：
- Option A：以 Drafter 的信心分布表為準（自然 6 個），把 Gemini 的 4 個對應 unfold。
- Option B：以 Dr1 章節結構為準（一–五 + TL;DR = 6 個），把 Codex 的 Findings 對應 mapping。
- Option C：保留三套各自 boundary，meta-report 用「topic cluster」概念跨切片整合。

### 4. L8 觸發策略需要明定

三模型對 L8 處理差異最大：
- Claude 看 state.yaml 知道 Drafter 沒用 Dr2 格式 → 改語義版抽樣
- Codex 機械觸發 missing_scope_tag
- Gemini 升級為 Critical structural issue

Spec 應該規定：**L8 觸發判斷由「主審 schema 角色」（Claude）統一裁決**，Codex/Gemini 跑 L8 時，若主審判定 Drafter 為 Dr1 格式則跳過 L8 機械檢查，避免 false-positive critical。

### 5. Verdict 整合規則

Overall 三個模型差異（🟢 vs 🟡 vs 🟡）反映「對 v1 review 是否落地」的不同認知。整合規則建議：
- **若任一模型 verdict ≥ 🔴 或有 🚨 finding** → meta verdict = revision required
- **若 ≥2 模型 verdict 為 🟡** → meta verdict = 🟡，operator 看 Codex 的 detail
- **若 ≥2 模型 verdict 為 🟢 且 Codex 無 🚨/❌** → meta verdict = 🟢
- Claude 較寬容，Codex 較嚴格 — Codex 的 ❌/🚨 應**升 weight**而非平均

### 6. 跑時成本與時長

- 三模型並行：實測 ≤ 8 分鐘（Gemini 最快，Codex 最久 ~6 分鐘）
- token 估算：Claude ~96k total、Codex ~未直接顯示但類似量級、Gemini 無顯示
- 對 production pipeline 來說，這是可接受的延遲

## 結論

PoC 印證了 multi-model reviewer 的價值：**三個模型各自抓到另外兩個漏掉的東西**，且失誤模式（Gemini hallucination、Codex 過嚴、Claude 偏寬容）剛好相互校正。

但平均化或投票合併會稀釋價值；正確做法是**分工 + cross-check**，spec 要明定主審視角、source pool integrity check、boundary alignment 策略。
