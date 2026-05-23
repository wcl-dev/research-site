# Review of scam-fake-website-tw insight_v1 — Multi-model meta-merge

**Reviewed on**: 2026-05-21
**Draft**: projects/scam-fake-website-tw/pipeline/draft/insight_v1.md
**Review mode**: multi-model (Claude + Codex + Gemini parallel → meta-merge), fidelity_level: high
**Reviewed by**: Claude (`multi_model/r_claude.md`), Codex (`multi_model/r_codex.md`), Gemini (`multi_model/r_gemini.md`, advisory)
**Meta-merge**: meta-reviewer per `backlog/multi-model-reviewer.md` §6–§9; review pass v1 (strict-adversarial; Claude general-verdict weight 1.0, Codex senior weight applies, Gemini advisory verdict-weight 0.3)

---

## Overall verdict

**🟡 needs revision pass (one light-to-moderate edit cycle; no re-Drafter required).**

This is a two-layer verdict per §8. The draft's methodological discipline is genuinely above baseline — all three reviewers independently confirm it: A/B strictly split, supply-side vs demand-side given a dedicated reconciliation section, every percentage carries a denominator, tier tags present, the `real_platform_not_fake_site` counter-framing engaged with an explicit `counter-of-counter`, and zero rejected-cid citations / zero orphan claims / zero concept-fidelity violations. There is **no 🚨, no re-Drafter trigger** (§8 R1 not fired).

But the merge does not land at Claude's 🟢. Two senior reviewers (Claude schema-aware + Codex causal-overreach) **both** identify the same class of defect — Drafter-derived quantities presented as if source-stated — and Codex raises three **L2 fidelity ❌** findings (F4, F6, F7) that meet §8 R2: a senior reviewer ❌ on L2 with **no senior counter-evidence** elevates the finding to ❌. Per §8 R3 (≥2 models 🟡+ with a source-fidelity issue → overall 🟡) and the §9 Claude-over-tolerance rule (Claude 🟢 while Codex 🟡 and Gemini flags F6 ❌ → escalate), the meta verdict is **🟡, not 🟢**.

This is a revision, not a rejection. Every blocking issue is a sentence-level fix (delete an unsupported number, downgrade one tier, re-attribute one quantity) achievable in a single light edit pass.

### Blocking causes (must fix before publish) — 3

| # | Finding | Issue | Lens / source |
|---|---|---|---|
| B1 | F7 (+ TL;DR + What we don't know) | "冒名社群貼文只有約三分之一導向假網站" — c051 states only "three categories of导流去處, one of which is fake sites"; it never gives 1/3. "Three categories" cannot be inferred to "约三分之一". Quantitative overreach in TL;DR and What we don't know (load-bearing because TL;DR is the headline). | [Codex L2 ❌] + [Claude L2 ⚠️] consensus |
| B2 | F6 | "TWNIC RPZ 攔阻量級由 2021–2022 年約千餘躍升至 2025 年約 8 萬 [c037]" — c037 extract caveat explicitly states the page has no year-over-year table and the 2021–2024 basis is from brief reconnaissance, not c037. The 2021–2022 baseline is therefore an **uncited claim**; c037 supports only the 2025 figure. | [Codex L2 ❌] + [Gemini L5 ❌] |
| B3 | F4 | "此鏈由三個獨立來源交叉確認 …… c051" — c051 supports the social-ad→LINE→fake-investment front-end导流, but its extract caveat states it does not assert the chain necessarily ends in fake-site registration. c031/c030 (court) support the site leg; c051 does not. "Three independent sources cross-confirm" overstates c051's role. | [Codex L2 ❌] + [Gemini L2 ⚠️] |

### Non-blocking issues (fix recommended; do not gate publish) — 5

| # | Finding | Issue | Lens / source |
|---|---|---|---|
| N1 | F5 | Confidence line says "4 個 qs≥4 來源（c037/c022/c042/c040）"; accepted.jsonl has **c042 qs=3** (gate-capped, 403 PDF). Correct: 3 qs≥4 (c037/c022/c040) + c042 rescued PDF qs=3. The "高" tier itself still holds (≥3 sources incl. qs≥4 met even after removing c042). | [Claude L5] |
| N2 | F5 para3 | Arithmetic misplacement: "其餘 96.5% 是社群平台內容（Meta 117,845、LINE 1,438、Google 211、TikTok 15）". 96.5% = Meta **alone** (117,845/122,119); the four-platform total is 97.86%; all non-website content is 98.67%. The 96.5% is anchored to the wrong list. | [Claude L2] |
| N3 | F1 | Confidence line "多分母骨架的每層分母都有 qs≥4 來源" — the third denominator layer (165 dashboard 16.2萬/893億) rests on c046, qs=3 snippet-layer. Body prose already marks this contested; only the Confidence-line generalisation needs the one-sentence fix. | [Claude L5] |
| N4 | F1/F4/F8 | c048 (TechNews secondary recovery of the Whoscall 30.52%, accepted, qs=3) not cited. c047 (Whoscall blog) is JS-only; c048 is the pipeline's traceable secondary backstop. Not citing it makes the 30.52% look like a single unverified source when it is actually corroborated. Codex frames this as L4; Claude calls it the draft's most substantive L4 gap. Also nice-to-have: c059 (official MOI funnel, qs=4) for F4, c058 (FSC, qs=3) for F2. | [Claude L4] + [Codex L4] consensus |
| N5 | F2/F3/F6 | Single-source paragraphs tagged 【強證據】: F3 para1 (c024 alone), F6 para1 (mixed). Per the spec "High/強證據 = ≥3 sources incl. qs≥4". Both reviewers note this; severity is minor because the claims are pure dataset-fact statements from qs=5 platinum datasets, and each Finding's overall Confidence is already downgraded to 中. | [Codex L5] + [Claude L5] (minor) |

---

## Per-finding consolidated verdict

| Finding | Claude | Codex | Gemini (adv.) | **Meta-verdict** | Driver |
|---|---|---|---|---|---|
| F1 — 多分母方法論 (Q1) | ✅ | ⚠️ | ✅ | **⚠️ needs tightening** | N3 (Confidence-line qs claim) + N4 (c048 unused). §8 R3-lite: one senior ⚠️ on L4/L5, no ❌. |
| F2 — A 型冒名規模 (Q2) | ⚠️ | ⚠️ | ⚠️ | **⚠️ needs tightening** | 3-model consensus ⚠️. "A 型下界" scope wording + c058 unused. No ❌. |
| F3 — B 型規模 (Q3) | ✅ | ⚠️ | ✅ | **⚠️ needs tightening** | Codex L5: F3 para1 【強證據】 on single source. N5. No ❌. |
| F4 — 媒介角色／生命週期 (Q4) | ⚠️ | ❌ | ⚠️ | **❌ has gap** | §8 R2: Codex L2 ❌ on c051 over-attribution, no senior counter-evidence. B3. |
| F5 — 供給端攔阻成效 (Q5) | ⚠️ | ✅ | ✅ | **⚠️ needs tightening** | N1 (qs miscount) + N2 (96.5% arithmetic). Codex/Gemini ✅; Claude ⚠️ is decisive — both are quantitative-precision defects in a brief that makes number-precision a deliverable. |
| F6 — 2023–2026 趨勢 (Q6) | ✅ | ❌ | ❌ | **❌ has gap** | §8 R2: Codex L2 ❌ (uncited 2021–2022 baseline) + Gemini ❌. All three converge on F6 as the weakest finding. B2. |
| F7 — 需求端稀釋反證 (Q4 caveat) | ✅ | ❌ | ✅ | **❌ has gap** | §8 R2: Codex L2 ❌ on the "三分之一" overreach (located in TL;DR + What we don't know, not the F7 body). B1. The F7 *body* is genuinely the draft's most careful section — see Model conflict. |
| F8 — 資料缺口 (Q7) | ✅ | ⚠️ | ✅ | **⚠️ needs tightening** | Codex L1/L3: "調查局無公開量化資料" sentence is a pipeline-search result, not an accepted-source finding — relocate to What we don't know with that label. |

**Per-finding verdict line**: F1 ⚠️ · F2 ⚠️ · F3 ⚠️ · F4 ❌ · F5 ⚠️ · F6 ❌ · F7 ❌ · F8 ⚠️ — 0 ✅ / 5 ⚠️ / 3 ❌ / 0 🚨.

Note the spread between Claude's per-finding ✅ count (5) and the merged count (0): this is the §9 Claude-over-tolerance correction operating finding-by-finding. Claude's per-finding L1/L2/L4/L8 spot-checks are detailed and were retained as evidence; but where Claude rated a finding ✅ and Codex flagged an L2 fidelity ❌ that Claude did not engage at the same depth (F4 c051, F6 baseline, F7 "三分之一"), the meta-merge defers to Codex per the operating-discipline rule "when Claude says ✅ but Codex says ⚠️/❌, default to Codex unless there is specific reason to side with Claude." On F7 specifically, Claude *did* independently catch the "三分之一" issue (Claude L2 ⚠️ on F7) and recommended the same fix — so this is consensus, not a lone Codex catch.

---

## Model conflict

The three reviewers diverged on the **overall verdict** (Claude 🟢 / Codex 🟡 / Gemini 🟢) and on **three findings**. Per §8 the disagreements are preserved here rather than averaged.

### Conflict 1 — F4 and F7: severity of the c051 over-use

- **Codex** rates both F4 and F7 ❌ (L2 fidelity), treating the c051 mis-attribution as a `has gap`-level defect.
- **Claude** rates F4 ⚠️ and F7 ✅. On F7 Claude *agrees* the "三分之一" is a Drafter derivation not in c051 ("「三分之一」嚴格說是 drafter 的推算而非 c051 原文") and recommends the identical fix — but Claude scores the finding ✅ because the F7 *body* (not the TL;DR) handles the caveat carefully and labels it caveat-tier.
- **Gemini** (advisory) rates F4 ⚠️ and F7 ✅, siding with Claude on severity.

**Meta-resolution**: The catch is **consensus** (all three see the c051 issue exists); the disagreement is purely severity. Per §8 R2 a senior-reviewer L2 ❌ with no senior counter-evidence elevates the finding — and there is no counter-evidence here, because Claude *concedes* the fact. So F4 and F7 merge to ❌. **However**, the §9 "Codex hyper-critical" guard partially applies to F7: the F7 *body* paragraph does carry an explicit caveat and contested tier, so the ❌ is scoped narrowly — the blocking defect is the **TL;DR + What we don't know** wording (B1), not the F7 body, which all three reviewers praise. F4's ❌ is not softened: the over-claim ("三個獨立來源交叉確認") sits in the F4 first paragraph itself, which is the load-bearing sentence.

### Conflict 2 — F6: "高原期" vs the actual catch

- **Codex** ❌: the real defect is the **uncited 2021–2022 TWNIC baseline** (L2 citation gap).
- **Gemini** ❌: the defect is the word **"高原期"** being subjective when c023 shows 2024→2025 still grew 13.7% (517→588).
- **Claude** ✅: sees neither as blocking; notes the three longitudinal series are direction-consistent and Confidence is already 中.

**Meta-resolution**: All three agree F6 is the **weakest finding** (Codex ❌, Gemini ❌, and Claude's own narrative calls Q6 "最薄的格"). The merge takes F6 → ❌ on the **Codex** catch (B2), because an uncited quantitative claim is a harder defect than a word-choice quibble. Gemini's "高原期" point is valid third-opinion data (integrity clean → Gemini per-lens catches count) and is folded in as a **recommended** rewrite, not a separate blocker: "高原期 / 趨於高原" → "成長趨緩但仍持續創新高" is the more honest description and costs nothing. Gemini's overall verdict (🟢) does not tip anything per §8 R6.

### Conflict 3 — F1 para3 scope tag

- **Codex L8** flags F1 para3's `{conceptual:A}` as scope_overreach: c042's "詐騙網站下架" 1,621 figure is supply-side A∪B/C, not pure A.
- **Claude L8** rates F1 para3 `{A}` ✅: the paragraph's lead claim is the Whoscall 30.52% phishing-site share, which is A-leaning, and `{A}` ⊆ theme t01's `evidence_scope_distribution`.

**Meta-resolution**: This is a genuine schema-level disagreement between the two senior reviewers, and per §7 L8 is **Claude's primary lens**. Claude's reasoning is schema-anchored (subset check against t01's distribution passes) and the paragraph's *primary* claim is the Whoscall figure. Codex's point is not wrong — the c042 1.33% clause inside that paragraph is broader than A — but it does not rise to a `concept_fidelity_violation` (no 🚨 trigger). **Resolution**: not a blocker. Recommended as an optional precision edit: if the Drafter wants to be maximally precise, split F1 para3's scope or move the c042 clause's effective scope note, but this is below the revision bar. Logged as a model-conflict, not a finding defect. (Awareness note: the meta-reviewer runs as Claude and shares Claude reviewer's schema lens — this conflict was deliberately left as Codex's standing minority objection rather than dismissed.)

### Where all three agreed (consensus, high confidence)

- **F6 is the weakest finding** — unanimous.
- **The draft's A/B separation, supply/demand reconciliation, denominator discipline, and `counter-of-counter` are genuinely strong** — all three say so explicitly; this is not flattery, it is the reason the verdict is 🟡 (revision) not 🔴 (re-Drafter).
- **No rejected-cid citation, no orphan claim, no concept-fidelity violation** — all three independently confirmed; integrity_report.json corroborates (zero hallucinated cids across all three reviews).
- **F2 needs the "A 型下界" wording tightened** — all three flag it (Claude: nice-to-have c058; Codex: avoid "全台排名" reading; Gemini: restrict 1,466 to "A 型假冒電商" sub-class). Gemini's framing here is the crispest and is adopted in the recommendations.

---

## Source-pool integrity

`integrity_check.py` output (`review/integrity_report.json`) — **all three reviews integrity-CLEAN**:

| Review | usable | claimed/actual accepted_n | claimed/actual extract_n | hallucinated_cids | lens_multipliers |
|---|---|---|---|---|---|
| r_claude.md | ✅ true | 43 / 43 | 20 / 20 | none | none |
| r_codex.md | ✅ true | 43 / 43 | 20 / 20 | none | none |
| r_gemini.md | ✅ true | 43 / 43 | 20 / 20 | none | none |

`any_hard_error: false` · `any_count_mismatch: false`. No integrity-based down-weighting applied to any review. Gemini's per-lens catches therefore count as valid third-opinion data (no count_mismatch multiplier). The merge weights are the §8 base weights only: Claude general-verdict 1.0 (v1 strict-adversarial pass) + schema/L6/L7/L8 1.3; Codex L1–L5 1.4 with 1.5 on ❌; Gemini verdict 0.3 / lens 0.5.

Separate from review-integrity: the **draft itself** was cross-checked against `gate/accepted.jsonl`. Every cid in the draft (c022–c061 range) exists in accepted.jsonl; none of the 20 rejected cids (incl. c060/c062 法務部調查局) is cited. The accepted-pool quality scores were used to verify N1/N3 — confirmed: c042 quality_score=3, c046 quality_score=3, against which the Confidence-line "qs≥4" claims are inaccurate.

---

## Instruction-following audit (§9.4)

Grepped the three review bodies for `state.yaml`, `handoff_log`, `exit_plan_mode` mentions in review prose — **none found**. All three reviewers stayed within the review schema and did not leak pipeline-control instructions into their output. No operator flag required.

---

## Consolidated revision recommendations

Ordered by priority. Items 1–3 are **blocking**; 4–8 are recommended within the same edit pass.

1. **[B1] Delete "约三分之一導向假網站" wherever it appears** (TL;DR point 5, F4 Counter-evidence line, F7, What we don't know). c051 supports only "假網站僅是冒名社群貼文三條導流去處之一（另兩條為停留平台、導入 LINE）". Replace the quantity with the categorical statement, or — if a number is wanted — explicitly mark it "（粗估，假設三類等權）". The TL;DR instance is the load-bearing one. [Codex L2 ❌ + Claude L2 ⚠️ consensus]

2. **[B2] Fix the F6 TWNIC baseline citation.** c037 supports only the 2025 figure (79,039). Either (a) find a citable 2021–2024 RPZ source, or (b) rewrite to "2025 年 RPZ 停止解析達 79,039 個網域；可深讀的年對年基期來源缺如，2021–2022 約千餘係 brief reconnaissance 數字、本 pipeline 未取得一手出處". Do not present the "兩個量級成長" as `[c037]`-backed. [Codex L2 ❌ + Gemini L5 ❌]

3. **[B3] Re-scope c051's role in F4.** Change "此鏈由三個獨立來源交叉確認" to "假網站站段由 2 份法院判決（c030/c031）認定；社群→LINE 前端導流由 c051（數位信任協會）確認" — c051 confirms the front-end, not fake-site registration. [Codex L2 ❌ + Gemini L2 ⚠️]

4. **[N1+N3] Correct the two Confidence-line qs counts.** F5: "4 個 qs≥4 來源（c037/c022/c042/c040）" → "3 個 qs≥4（c037/c022/c040）+ c042 rescued 一手 PDF（qs=3 gate-capped）". F1: "每層分母都有 qs≥4 來源" → "前兩層（c044/c043）為 qs5，第三層 165 儀表板分母依 c046 摘要層、已標 contested". Both Confidence *tiers* (高 / 高) stay — only the qs labels are wrong. [Claude L5]

5. **[N2] Fix the F5 para3 arithmetic.** "其餘 96.5% 是社群平台內容（Meta…TikTok…）" → "扣除詐騙網站 1,621 件（1.33%）後，98.67% 為非獨立網站內容，其中 Meta 單一平台即佔 96.5%（117,845/122,119）". The 96.5% is Meta-alone, not the four-platform list. [Claude L2]

6. **[N4] Cite c048 as the traceable secondary for the Whoscall 30.52%** (F1 para3, F8 para2, TL;DR point 2). c048 exists in accepted.jsonl precisely for this JS-blocked backstop role. Nice-to-have in the same pass: add c059 (qs=4 official MOI funnel) to F4's funnel paragraph and c058 (qs=3 FSC) to F2's financial-impersonation list. [Claude L4 + Codex L4 consensus]

7. **[Gemini, recommended] Replace "高原期 / 趨於高原"** in F6 and the 2023–2026 趨勢摘要 table with "成長趨緩但總量續創新高" — c023 shows 2024→2025 still grew 13.7%, so "高原" understates continued growth. [Gemini L5, third-opinion]

8. **[F2 + F8 wording]** (a) Restrict the moda 1,466 figure to "A 型假冒**電商**網域規模下界" rather than generic "A 型下界" (Gemini's crispest framing; Codex's "avoid 全台排名 reading" same intent). (b) F8: relocate "調查局無公開假網站量化資料" from the F8 body into What we don't know, labelled "pipeline 搜尋結果（must_include_skipped），非 accepted source 證明" (Codex L1/L3). [Codex + Gemini]

### Caveats that all three reviews preserved (must remain in any v2)

- Supply-side blocking volume ≠ demand-side victim share — keep the dedicated reconciliation section.
- A and B have **no common denominator**; A% and B% can only be given as separate ranges, never a single shared-denominator split.
- The "96% / 24h" and "61.1%" Trend Micro figures are unverified snippet-layer (c049, 403 + Wayback hub-landing only); keep them contested-tagged. Claude additionally recommends sharpening the wording from "常被引用的外部數字" to make explicit that this number is **not traceable to source inside this pipeline** — adopted as a recommended (non-blocking) precision edit.

---

## Meta-merge summary

- **Catches attributed**: Codex — 3 blocking (B1/B2/B3, all L2 fidelity ❌) + L5/L4 contributions on N5/N4; Claude — N1/N2/N3 (L5 qs-count + L2 arithmetic), L4 on N4 (c048), and consensus on B1; Gemini (advisory) — B2 corroboration (F6 ❌), the "高原期" rewrite (rec. 7), and the crispest F2 wording (rec. 8). No new finding was invented in this merge; every item traces to at least one input review.
- **Verdict path**: §8 R1 not fired (no 🚨 / no rejected-cid). §8 R2 fired three times (Codex L2 ❌ on F4/F6/F7, no senior counter-evidence) → three findings ❌. §8 R3 + §9 Claude-over-tolerance → overall escalated from Claude's 🟢 to **🟡**. §8 R6 honoured — Gemini's 🟢 overall verdict did not tip the merge; its per-lens catches (integrity clean) were used as third-opinion data.
- **Why 🟡 not 🔴**: all 3 ❌ findings are sentence-level fixes; the draft has no structural failure, no brief-success-criterion missed (L6: Q1–Q7 all covered, all 5 success criteria met), no failure-condition triggered. One light edit pass resolves all 8 items.

### Spec / schema observations for the audit log

- **§8 R2 worked as intended on a v1 strict pass.** With Claude general-verdict weight at 1.0 (not the v2+ 0.8), Claude's per-finding ✅ count was still fully overridden on F4/F6/F7 by Codex L2 ❌ — confirming R2 is the operative rule, not the weight. The weight matters for *verdict-score ordering*; R2 is categorical. This is the correct design and is worth noting: a pure weighted-average would have landed 🟢 here (Claude 1.0×🟢 + Gemini 0.3×🟢 outweighs Codex 1.4×🟡), which is exactly the "average-mush" failure §8 R2 exists to prevent.
- **F7 is a clean test case for the §9 Codex-hyper-critical guard interacting with R2.** Codex's F7 ❌ is *not* a lone hyper-critical catch (Claude independently concurred on the "三分之一" fact), so the guard did not down-grade it — but the guard *did* correctly scope the ❌ to the TL;DR/What-we-don't-know wording rather than the F7 body, since the body already carries the caveat. Recommend the spec add an explicit note that R2's ❌ can be **location-scoped** within a finding when a senior reviewer concedes the body handles the issue — this prevents an over-broad ❌ on an otherwise-strong section.
- **Boundary alignment was trivial here** (§6 fallback B): the draft's 8 explicit Findings gave clean 1:1 canonical IDs and all three reviewers used the same Finding 1–8 numbering, so no topic-cluster fallback was needed. Worth recording as a positive: drafts with explicit numbered Findings make the meta-merge boundary step near-zero-cost.
