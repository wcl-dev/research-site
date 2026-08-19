# Reviewer prompt — Stage 6 multi-model review（defense-cut v2，**第二輪 / v2+ review pass**）

你是 **insight-pipeline 的 Reviewer**（Stage 6）。完整 role 規格、7+1 lens 框架、輸出 schema 在：

`./.claude/agents/reviewer.md`

請先讀完該檔，再對下列 project 跑一次完整 adversarial review。

## Target project

- **Project**: `defense-cut-supply-chain-pivot-tw`
- **Pipeline dir**: `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/`（**pipeline_v2**，不是 pipeline）
- **Draft to review**: `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/draft/insight_v2.md`（**注意是 insight_v2.md** — 約 6,000 字繁體中文研究定位備忘錄；5 Findings + Counter-framing engagement + What we don't know）
- **Review mode**: multi_model（brief_expanded.yaml `review.mode: multi_model, fidelity_level: high`）
- **Review pass**: 這是 **第二輪 review（v2+ review pass）**。insight_v1.md 已經過第一輪 multi_model review（verdict 🟡 needs revision pass — patch-level），Drafter 據此做了 revision pass 產出 insight_v2.md。前一輪的 consolidated review 在 `pipeline_v2/review/review.md`（你可讀以了解前一輪挑出什麼、據以檢查 v2 是否真的修好）。

## 必讀檔案（全部絕對路徑）

- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/brief.md`（PRIMARY/SECONDARY success criteria + Failure modes）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/brief_expanded.yaml`（concept_ontology A/B/E + 6 counter_framings）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/gate/accepted.jsonl`（**79** accepted source 全集，L3/L4 cross-check 用）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/gate/rejected.jsonl`（1 rejected，L1 hard-error 檢查用）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/extracts/`（**19** deep-read extract + `extracts/INDEX.md`，L2 fidelity + Dr3 evidence-pool 用）
- `./projects/defense-cut-supply-chain-pivot-tw/pipeline_v2/review/review.md`（**前一輪** consolidated review — 用於 L3 baseline / 檢查 v2 是否修好前輪 ⚠️）

## v1 → v2 的 6 個 patch（Drafter 已套用 — 請逐一查證是否真的落地，並評估有無修出新問題）

1. **F5 +c042 +c043** — 補台灣端出口管制法源（c042 eCFR Part 744 Entity List 法源；c043 台灣經濟部戰略性高科技貨品出口管制名單）。F5 法源層原本只有「美 BIS／中反制法」兩端，現補成三端。
2. **F1 4700/3000/3350 改寫** — 4700 億改述為「原 1.25 兆 vs 砍後 7800 億的總落差」；3000 億／3350 億描述為重疊本土/無人載具項目的不同口徑，不再讀起來像 3000+3350 的加總。
3. **F3「確定無法補回」改弱** — 改為「方向上偏成立、量級未知」，與 Finding 3 的「壓力與條件」framing 一致。
4. **F4 軟化 B 鏈 framing +c030/c032/c033** — 標題改為含「B 鏈仍有零組件依賴與母機外移風險」；補 3 筆無人機外銷 qs4 來源。
5. **F5 +c015 + Wassenaar gap** — 補 c015（脫鉤成本 counter-evidence）；What we don't know 補 Wassenaar/ECCN gap 一行。
6. **+Q6 scope statement** — Context 與 What we don't know 各補一行，明寫 Q6 國際比較是 brief 斟酌題、刻意不在範圍。

## Operator notes（v2 脈絡 — 非攻擊面，請勿誤判為缺陷）

1. **v2 的 MOPS Track-4 一手財報層「有做」** — accepted set 含 10 筆 MOPS 上市櫃財報 primary_doc（c071–c080，5 家工具機聚落公司）。不要 flag「MOPS 缺席」。
2. **Synthesizer 依 M4 跳過** → 無 `synthesize/themes.jsonl` → draft 正確未採 Dr2 scope 標籤；**L8 不觸發** — 請依 reviewer.md L8 規格明寫「L8: skipped — Synthesizer skipped per M4, no themes.jsonl」。
3. **6 個新 cid（c042/c043/c015/c030/c032/c033）皆為 Dr3 secondary 層**（INDEX.md `snippet_status: usable`，無 extract 檔）→ draft 正確將它們 cap【爭議中】+「依摘要層 sourcing，未經 deep-read 一手驗證」annotation。這是 Dr3 by-design，**不要 flag 為 tier 錯誤**。
4. **c050（亞德客 airtac.net）URL 失效**，已由 c079/c080 取代；INDEX 標 superseded。draft 正確引 c079/c080。
5. **c075（東台 4526）是 partial 下載** — 東台完整年報「中國市場策略」敘述段非公開可得；c075 缺西進敘述 ≠ 東台無西進。
6. **所有 2026 Q1 MOPS 財報截至 2026-03-31，早於 2026-05-08 軍購砍案** — draft Finding 3 把「砍案→西進」定為壓力與條件，是 by-design 的時序誠實。

## 真正值得嚴審的點（fair game）

- 6 個 patch 是否真的修好前輪 ⚠️、有沒有引入新問題（例如新 cid 是否被放進【強證據】段而違反 Dr3、F1 改寫後數字是否仍精確）。
- Q5「工具機西進後失去歐美訂單」仍無具名產業個案 — draft 在 What we don't know 已標。請審 F5 / Counter-framing 有無從「機制存在」偷渡到「個案已發生」。
- B 鏈（無人機整機/零組件）primary-doc 仍 A 鏈 heavy — F4 補了 c030/c032/c033（皆摘要層）後，雙鏈對比是否仍在 B 側 over-claim。
- 「砍案→西進」因果本質前瞻 — Finding 3 framing 是否守住「壓力/機率」。

## 你的任務

依 reviewer.md 的 7+1 lens 框架，對 `insight_v2.md` **每一個 Finding** 進行完整 adversarial review（跑完整 L1–L8；L8 依 note #2 明寫 skipped）。這是 fresh review，不是只檢查 patch 有沒有落地 — 但請善用 review.md 作為 L3 baseline。meta-merge 階段才做 lens 加權。

## 輸出規格（嚴格）

- **語言**：繁體中文。
- **格式**：嚴格遵循 reviewer.md 的 Output format（Verdict + Per-finding review + Structural issues + Summary recommendations + Regeneration guidance）。
- **只輸出 review 的 markdown 內容**，從 `# Review of defense-cut-supply-chain-pivot-tw insight_v2` 這一行開始。不要 preamble／後綴／過程解釋。

## 重要限制

- **不要動任何 pipeline state 檔案**：不要 update `state.yaml`、不要 append `handoff_log.jsonl`、不要 overwrite 其他 reviewer 的輸出或前一輪的 review 檔。
- meta-reviewer 會在三份 review 完成後統一 consolidate，包括 state 更新與 handoff event。你只負責輸出自己這份 review markdown。

## Adversarial mindset

> "Find weaknesses, not validate. Assume the Drafter was over-confident and under-cited; your task is to disprove that or quantify the gap."

若跑完 7+1 lens 都沒發現問題，明白寫「audited N claims against M extracts, found no divergence」，不要為交差編造問題。

## Source-pool integrity 自我提醒

引用 cid 時只用 accepted.jsonl 內存在的 cid（c001–c080）。**若需提及被 reject 的 c023，請用純文字 `c023`、不要用方括號 `[c023]`** — integrity_check.py 的 bracket-detection 會把方括號形式誤判為 rejected_cid_cited 硬錯誤。Sources consulted 行的數字必須與實際一致（accepted 79、extracts 19）。
