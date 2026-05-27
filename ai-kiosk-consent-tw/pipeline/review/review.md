# Review of ai-kiosk-consent-tw insight_v1 — Meta-merged (multi-model)

**Reviewed on**: 2026-05-27
**Draft**: projects/ai-kiosk-consent-tw/pipeline/draft/insight_v1.md
**Reviewed by**: Claude (`multi_model/r_claude.md`, schema-aware senior — L6/L7/L8 + Dr1/Dr2 lead) + Codex (`multi_model/r_codex.md`, causal-overreach hunter senior — L1–L5 + paragraph L8 lead)
**Gemini**: ABSENT — MCP provider-side timeout 3× consecutively at 210 s (server pings alive). Per `backlog/multi-model-reviewer.md` §2 Gemini is junior parity-check; absence does NOT invalidate the meta-merge. Operating in **2-senior-reviewer fallback mode**.
**Meta-merger**: Claude Opus 4.7 (this agent). Aware of schema-aware blind-spot overlap with r_claude — defaulted to Codex on divergent verdicts per spec §6 + operator instruction.

---

## Source-pool integrity

Per operator-provided `integrity_report.json` summary (file not persisted to disk this run; values reproduced from prompt):

```
any_hard_error:         false
any_count_mismatch:     false
lens_multipliers:       none triggered (all clean)

Claude reviewer:        92/92 records accepted, 27/27 extracts, 48 cids cited, usable=true
Codex reviewer:         92/92 records accepted, 27/27 extracts, 43 cids cited, usable=true
Gemini reviewer:        absent (timeout, not integrity failure)
```

No fabricated cids, no rejected-pool leakage, no record-count mismatch in either senior review. Both seniors weighted at full strength (no per-lens multiplier penalties).

**Operator note**: integrity_report.json was referenced in prompt but not on disk — recommend persisting future runs to `pipeline/review/integrity_report.json` for the audit trail. This does not block the merge; the operator vouched for the values.

---

## Verdict table (per spec §8 verdict integration formula)

Severity scale: ✅ (0) < ⚠️ (1) < ❌ (2) < 🚨 (3). Per-finding verdict = `max(claude, codex)` (stricter wins on divergence per spec §6, R2-extended for senior-reviewer L2/L4 ❌). Both seniors agree on overall publishability tier.

| Finding | Claude | Codex | **Merged** | Convergence | Primary blocker |
|---|---|---|---|---|---|
| F1 Q1a 雙端規模 | ✅ | ⚠️ | **⚠️** | Divergent | Codex: 「一手確認」wording overreach + TL;DR/標題把 vendor fleet upper bound 寫成 A 區上界 [c033] |
| F2 Q1b 雙 showcase | ⚠️ | ⚠️ | **⚠️** | Convergent | Both: Showcase A 「跨境傳輸」推論 + 表格現場流程 claim 沒 audit 證據;Claude 加 RAM/inference 機制 hedge [c032/c033] |
| F3 Q2+Q7 wording vacuum | ✅ | ✅ | **✅** | Convergent | None — both seniors call this the draft's most solid finding [c032/c037/c038/c041/c042/c045] |
| F4 Q4 法律+憲法 spine | ⚠️ | ❌ | **❌** | Divergent (severity) | **Both:** 釋字 603 transferability over-stated;Codex 嚴格降為「強類比 + 水平效力中介」;Claude: 「RAM/cache 短暫留存」mechanism claim 無 cite 卻夾在 [strong] 段 [c097/c098] |
| F5 Q4+Q7 vendor split | ✅ | ⚠️ | **⚠️** | Divergent | Codex: 「同樣賣 demographic inference SDK / kiosk」把 CyberLink SDK 與 WiXtar 整合商視為同類層 — 需 caveat;「直接打掉」改為「削弱」[c045] |
| F6 D 軸三層對照表 | ⚠️ | ⚠️ | **⚠️** | Convergent | Both: c044 vs c045 一致性 + SDK / 終端 / 中游廠商「責任層級」未拆;Codex: ✗「無人工替代」是 absence-of-evidence → evidence-of-absence overreach;表格 §8 對照 missing c053 [c044/c045/c053] |
| F7 Q3+Q6 四重結構性零 | ❌ | ❌ | **❌** | Convergent (load-bearing) | **Both:** 「3,058 件/年 inference 隱形池下界 proxy」over-claim — 應為 invisible-ceiling 而非 inference-floor;Claude: cherry-picked omission c079 全國消保會統計 + c095 高雄高行政 profiling 判決;Codex: cherry-picked omission c105 business_others 3,074 (與 services_others 並選未說明) [c079/c080/c095/c105/c106] |
| F8 Q5 國際對照 | ⚠️ | ⚠️ | **⚠️** | Convergent | **Both:** Home Depot c073 scope mismatch (B 區 identification vs A 區 inference) 未複述 caveat;Claude: c070 EC Feb 2025 prohibited AI practices guidelines 未引;Codex: EDPB Opinion 11/2024 寫成「真正涵蓋商業 demographic inference 的 spine」過強;CCPA 段 0 source [c067/c070/c073/c077] |

**Merged F-tally**: 1 ✅ / 5 ⚠️ / 2 ❌ / 0 🚨

**Overall verdict**: 🟡 **publishable with edits** — both seniors converge. Two ❌ findings (F4 + F7) are publication-blocker class修整, not rewrite-class; F4 + F7 share a common failure mode (Drafter pushing extract beyond its declared scope_caveat). 6 of 8 findings are publishable as-is or with surface tightening. F3 is the draft's教科書 strongest finding — do not touch.

---

## Model consensus / conflict

### Where both seniors converge (high-confidence meta-findings)

1. **F7 is the load-bearing weakness** (Claude L2+L5 ❌ + Codex L1/L2 ❌). The「新北 services_others 2,235 + 桃園「其他」823 = 3,058 件/年 inference 隱形池下界 proxy」is a Drafter inference: residual buckets are mathematically summed (arithmetic correct), but inference-proportion within is unconfirmed at row-level. Claude frames as「應為 invisible-ceiling 而非 inference-floor」;Codex independently arrives at「residual-pool visibility proxy, not lower-bound for A∩D complaints」— different wording, identical mechanical correction. **TL;DR 第 3 點直接 inherit 此 over-claim,連動必修。**

2. **F4 釋字 603 transferability over-reach** (Claude L2 ⚠️ + Codex L1/L2/L5 ❌). Both seniors flag that 釋字 603 是國家強制捺指紋的原因案件,c097 extract scope_caveat 明示 state action vs private actor + identification vs categorisation 差距,Drafter 將其 transferability 推到「私部門商業 inference 連起點門檻都未滿足」過強。Codex 嚴格 ❌:「私部門個資法架構未必要求每一商業蒐集目的有單一法律明確授權」。Claude additionally flags F4 [strong] 段內夾帶「實際上多數 edge inference 系統都會在 RAM/cache 短暫留存原始畫面」mechanism claim 無 cite — strong-tier 段不應夾 unverified mechanism inference。

3. **F8 Home Depot c073 scope mismatch + EU AI Act spine over-stretch** (both seniors ⚠️). Home Depot 案技術屬性 c073 extract scope_caveat 明示為「loss prevention surveillance」(B 區 identification),F8 未複述 caveat,將其框架為「最接近 A 區單一國際先例」。Both seniors additionally flag:Claude — c070 EC Feb 2025 prohibited AI practices guidelines (Art. 5 商業/職場界線權威解析) accepted-but-uncited;Codex — c077 EDPB Opinion 11/2024 是「真正涵蓋商業 demographic inference 的 spine」措辭過強 (extract caveat 明示是 reduced-intrusiveness design pattern, 不是 mandatory standard)。

4. **「公開資料無提及」滑成「現場沒有」是 cross-cutting overreach** (Codex L2 系統性提出 — Claude 未獨立 flag, 但對 F2 表格的 RAM/inference 機制 claim 是同類 issue)。F2/F6/F7 三處皆有:「無告示」「無人工替代」「站到前瞬間被掃描」應寫為「公開資料未揭露,需現場查核」或降 tier。Codex 提出此 systemic pattern — meta-merge 視為 ⚠️ 全 draft cross-cutting tightening。

5. **F6 entity-layer scope mismatch** (Codex L4/L8 ⚠️ + Claude L4 ⚠️)。對照表混合 SDK 供應商 (CyberLink c045)、kiosk 整合商 (WiXtar)、部署終端 (雙月/金色三麥)。Both seniors flag responsibility-layer 拆解不足;Codex 提出加「責任層級」欄,Claude 提出 c044 vs c045 是否同一致 framing 確認。

### Where two seniors diverge (stricter-wins applied per spec §6)

- **F1**: Claude ✅ (only [speculative] tier 用法存疑) vs Codex ⚠️ (「一手確認」wording 把 c041 CIO Taiwan case-study 升成 vendor primary;TL;DR 把 vendor fleet upper bound 寫成 A 區規模上界)。**Merged ⚠️** — Codex catches an operator-facing communication risk (TL;DR misread risk) that Claude's schema-internal check missed. Operator should default to Codex here per "not under-flagging publication blockers" bias.
- **F5**: Claude ✅ (Dr7 partial_counter_framing 處理為合約典範) vs Codex ⚠️ (「同類 vendor、同類技術」太平,SDK/整合商/終端責任層未拆;「直接打掉 defence」過強)。**Merged ⚠️** — Claude's schema-fit verdict is right but Codex's rhetorical-load critique is independent and correct. Both can be true simultaneously: Dr7 contract is 合規 + rhetorical wording over-stretches.
- **F4 severity**: Claude ⚠️ vs Codex ❌. **Merged ❌** — when senior reviewer hits ❌ on L2 (claim-vs-source fidelity, Codex's lead lens), spec §7 + §8 R2 require deference to lens lead. Claude's ⚠️ stands as supporting characterization but does not down-grade.

### What Claude saw that Codex didn't (or weighted lower)

- **L4 cherry-picked omissions catalog** (Claude lead):
  - c079 (行政院消保會全國申訴統計) + c080 (線上申訴系統) — F7 全國層 silence, 削弱「申訴 schema 零」窮盡性
  - c095 (高雄高等行政法院 114 年度簡字第 216 號 profiling 判決) — F7「司法零」邊界判例 omission;雖屬兒少領域已論述 profiling/特徵分析監控風險
  - c070 (EC Feb 2025 prohibited AI practices guidelines) — F8 Art. 5 商業界線權威 omission
  - c057–c060 / c088 (修法跨律所分析 + 個資法施行細則 primary doc) — F4 [contested]→[strong] upgrade 機會 (not blocker)
- **L8 conceptual A∩D vs schema mismatch**: `{conceptual:A∩D}` (F2/F3/F4/F5/F6/F7 多處) 與 themes evidence_scope_distribution.conceptual 結構 `{A:n, D:m}` 兩 key 不對齊。Lint 嚴格可 flag。建議改為 `{conceptual:A,D}` multi-value 形式。
- **scope tag form**: 全 8 個 Finding 使用 `<!-- ... -->` HTML comment 而非 Dr2 推薦 visible bold `**{...}**`。若 lint 只認 bold pattern,draft 全段都將 fail。Operator 應確認 lint regex。

### What Codex saw that Claude didn't (or weighted lower)

- **F2 hedge fading**: 「雙 showcase 共同特徵:消費者站到機器前的瞬間就被掃描」對金色三麥不完全適用 — c042 是「拍一張照片」主動互動而非自動掃描。Drafter 從「拍照互動」滑成「瞬間掃描」。
- **F4 horizontal-effect framing**: Codex 提出更精確的修正 wording —「釋字 603 提供比例原則與資訊自決的強類比;直接套用『法律明定目的』到私部門商業 inference 需經水平效力與個資法中介論證」。Claude 提出方向但 Codex 給出 actionable replacement language。
- **F4 hedge fading**:「幾乎不可能站得住」「結構性瓦解」「直接打掉」「站不住」一連串硬語應限縮 — c098 能打掉的是「仍可間接識別卻稱非個資」這個特定子命題,不能自動處理所有 no-storage/no-identification implementations。
- **F6 absence-of-evidence overreach**: 表格中「無人工替代描述」標 ✗ — 這只能說「公開資料未描述人工替代」,不能說「無人工替代」。這是 F6 表格的核心 L2 weakness, Claude 未獨立 flag (只 flag c044/c045 一致性)。
- **F6 citation format**: 表格 source 欄是裸 cid 串,未用 `[cNNN]` 格式 — 若 integrity checker 只抓 cid 可能過,但正式 citation density 不如其他段。
- **F7 cherry-pick within c105**: c105 另有 business_others 3,074 件,Drafter 選 services_others 而排除 business_others 的理由未交代 — 加倍坐實 over-claim 嫌疑。Codex 獨立 catch。
- **F7 c105 extract 內部矛盾**: c105 Passage 1 把 113 年 residual 寫成 714+432=1,146 (那是 103 年列),Passage 2 給 113 年 2,235/3,074。Drafter 採 Passage 2 但應註明 — 否則讀者抓 extract 內部矛盾。

### Where neither senior flagged (potential meta-merger blind spots to operator)

- **Q3「人工替代退出成本」具體實況**: Claude 提及 Q3 處理略單薄 (主要靠 F8 Home Depot 間接對照),Codex 未獨立 flag。若 Gemini 在場可能會作為 junior checklist catch — 待 operator 自行判斷是否影響 brief §8 success criteria 第 5 條 (執法現況)。
- **TL;DR per-bullet L8 scope tag**: Codex 提及 TL;DR / Context / Counter-framing / What we don't know / 政策建議 sections 缺 paragraph-level scope tag。若 L8 paragraph-level audit 是 hard requirement, TL;DR 5 個 bullet 必須各帶 scope tag。Claude 提及 8 Finding scope tag coverage 但未獨立檢查 TL;DR。

---

## Per-finding analysis (meta-merged)

### F1 (Q1a 雙端規模) — **⚠️**

Convergent on L1/L2 fidelity (citation density solid). Divergent on whether tier-tagging hits operator-facing risk threshold.

**Required edits**:
- [Codex L2] TL;DR 第 1 點 + Finding 1 標題:把「vendor-claimed 上界 30+/1000+」固定附「WiXtar fleet claim; inference-enabled subset unknown」,所有出現「30+/1000+」處皆同 — 避免讀者讀成 A 區規模上界 [c033]
- [Codex L1] F1 「2 brand 一手確認」wording:c041 是 CIO Taiwan case-study (媒體記錄), 不是 vendor 一手稿。改成「2 brand confirmed by deep-read sources (vendor primary c032 + media case-study c041)」[c032/c041]
- [Claude L5] 第 4 段 B/C callout 從 [speculative] 改為 [strong 為 B] / [strong 為 C] — 內容是「明確證實 B/C 而非 A」的 firewall 主張,方向相反 [c046/c047/c049]
- [Codex L8] F1 第 4 段 `conceptual:B,C` 把 Berry AI 營運分析硬塞入 C 過粗。改為 `conceptual:B,C,ops` 或寫「B/C/ops contrast」

**Not required (informational)**:
- [Claude L4] c034-c036/c039-c040/c043/c048 vendor adjacent records 未進入,屬可加強但非 blocker — 若 F1 想 surface 多層 vendor 確認可加

---

### F2 (Q1b 雙 showcase) — **⚠️**

Convergent ⚠️;both seniors target the same artifact-flow over-claims and confidence-self-rating over-stated.

**Required edits**:
- [Codex L1/L2 + Claude L2] Showcase A 表格 t₀-t₂ 「進店看到 kiosk + 攝影鏡頭, 無告示、無同意提示」「站到機器前瞬間就被掃描」「即時臉部畫面進入 RAM/cache」「持續 inference + 推薦策略運算」標 `inferred from public materials; no on-site audit`,不能放在 [strong] 時間軸 — 改為「公開資料未揭露; 需現場查核」或降 tier [c032/c033]
- [Claude L2] Showcase A t₃「藉由雲端運算將資料完整回傳台灣總部」(逐字 c032) + 「外籍遊客語音通過 OpenAI/微軟 API 跨境傳輸 [c033]」— 後者「跨境」是 Drafter 推論而非 c033 verbatim, 加 hedge:「推論為跨境傳輸 — vendor 未明文說明 OpenAI/Azure API 是否經境外節點」
- [Codex L2 hedge fading] 「雙 showcase 共同特徵:消費者站到機器前的瞬間就被掃描」對金色三麥不適用 — c042 是「拍照」主動互動。改為「Showcase A 站到 kiosk 前自動掃描 + Showcase B 拍照互動觸發推算」,不要 collapse 為單一機制
- [Codex L3] Counter-evidence 段加處理:「公開報導 0 字提同意 ≠ 店面現場 0 告示」替代解釋 — 分開「無公開資料顯示告示/同意介面」與「現場無告示」
- [Claude L5 + Codex L5] F2 結尾 Confidence: high → 改 medium-high。理由:部署事實 high,consumer journey artifact 流向 medium/contested,留存/傳輸 unknown
- [Claude/Codex L8] 表格內 OpenAI/微軟語音跨境資料流已觸及 C/third-party processing,scope tag 未反映 — 加 `conceptual:A,C` 或 `application_scope:A; data_processor_scope:C`

---

### F3 (Q2+Q7 wording vacuum) — **✅**

Convergent ✅ — this is the draft's most solid finding by unanimous senior verdict. Five-source cross-confirmed wording vacuum (c032/c037/c038/c041/c042) + CyberLink internal-split self-counter (c045) handled cleanly.

**Optional polish (not required)**:
- [Codex L1/L2] c038 是 partial access (snippet-layer),整段標 [strong] 略偏高 — 若保留 strong,寫「c032/c037/c041/c042 strong + c038 partial corroboration」
- [Codex L2] 「不是 vendor 沒空寫、是 framing 性地不認為需要寫」是 mechanism inference, tier 應為 contested interpretation 而非 strong factual claim
- [Codex L3] 加一句「媒體報導 zero wording 不等於店內實作 zero」,避免把 publication vocabulary 等同現場法遵
- [Codex L4] c052 js_only blocked 在 gap 提醒中應出現,避免看似已完整查核 PDPC §8 函釋

**Do not touch**: 5-源 cross-confirmation + CyberLink internal-split framing 結構是教科書級,Drafter 不要在 v2 動它。

---

### F4 (Q4 法律+憲法 spine) — **❌**

Codex ❌, Claude ⚠️ — merged ❌ per spec §8 R2 extension (senior reviewer ❌ on L2 lens-lead = finding ≥ ❌ unless senior counter-evidence). Claude 未提供 counter-evidence,僅補 mechanism inference 額外問題。

**Required edits (publication blocker)**:
- [Codex L2 — "Major causal/legal overreach"] 「餐飲業 AI Kiosk 即時 demographic inference 沒有任何單一條法律對『為了即時 inference』明確授權,以釋字 603 標準衡量連起點門檻都未滿足」— **必修**改為:「釋字 603 提供比例原則與資訊自決的強類比;直接套用『法律明定目的』到私部門商業 inference 需經水平效力與個資法中介論證」[c097]
- [Codex L2 — hedge fading] 「幾乎不可能站得住」「結構性瓦解」「直接打掉」「站不住」全段 — 改為「大幅削弱」「不能僅憑不識別/不留存即豁免」。c098 能打掉的是「仍可間接識別卻稱非個資」這個特定子命題,不能 generalize [c098]
- [Claude L2] F4 [strong] 第 4 段「實際上多數 edge inference 系統都會在 RAM/cache 短暫留存原始畫面」是 Drafter 自引技術 mechanism claim, **無 cite** — 必修:cite 或標 [speculative-mechanism],strong 段不應夾 unverified claim;同步在 What we don't know 列為「需技術驗證的 mechanism claim」gap [c098]
- [Claude L2] F4 [strong] 段加 state-action vs horizontal-effect hedge 句:「釋字 603 原因案件為強制蒐集 (state action),餐飲 kiosk 為私部門商業行為,doctrine 適用上有 horizontal effect 中介;但本研究援引其資訊隱私權定義 + 比例原則邏輯,屬通說可承載之 transferable scope」[c097 scope_caveat]
- [Codex L3] 加 counter-evidence 處理:「金色三麥拍照互動屬消費者主動提供」與「私部門非強制」兩個反論 — 目前 F4 未完整處理 [c042]

**Suggested upgrade (not blocker)**:
- [Claude L4] c057/c058/c060 三家律所對 2025 修法的並行分析 + c088 個資法施行細則 primary doc + c061 PDPC 施行細則修正案及子法草案 — 加入後 [contested] 可升 [strong]
- [Claude L4] c066「虹膜雖非特種但高識別」摘要層 — Codex 提及可降低從憲法判決直接跳到餐飲 inference 的壓力
- [Codex L8] paragraph 應標 `source_scope: state/health/identification; application_scope: A∩D by analogy`,否則 L8 scope transfer 太隱形
- [Codex L5] Tier:條文/判決 existence strong,「inference framing 在現行法下站不住」應為 contested legal analysis

---

### F5 (Q4+Q7 vendor internal-split) — **⚠️**

Claude ✅ (Dr7 partial_counter_framing 教科書合規), Codex ⚠️ (rhetorical load over-stretch)。Merged ⚠️ per stricter-wins, both critiques can co-exist.

**Required edits**:
- [Codex L2] 「同樣賣 demographic inference SDK / kiosk」把 CyberLink SDK (c045) 與 WiXtar/星益欣 kiosk 整合商視為同類層 — 加 caveat。CyberLink c045 是 restaurant facial recognition marketing, 不必然是同一產品責任層或同一部署端 [c044/c045]
- [Codex L3] 「直接打掉 defence」→「削弱『業界不能寫/不會寫』defence」。CyberLink 證明 vendor 可以公開談知情同意, 不證明 WiXtar/星益欣有義務在新聞稿揭露全部 §8 要素
- [Codex L8] CyberLink temporal=2023 vs WiXtar thought leadership=2026 跨時比較 — 加「不同年份」caveat;Claude 同向建議「2023 (c045) → 2026 (c037)」逐源 anchor
- [Claude L8] `temporal:2023-2026` superset framing 邊緣 — 改逐源 anchor 更精準

**Do not touch**: Dr7 partial_counter_framing.value=true caveat-tier 處理是全 draft 教科書級合規 — Drafter 不要因 v2 修整動到此結構。

---

### F6 (D 軸三層對照表) — **⚠️**

Convergent ⚠️。Both seniors identify structural mismatch (responsibility-layer + format + L4 missing source);Codex adds absence-of-evidence overreach which Claude missed.

**Required edits**:
- [Codex L2 — load-bearing] 表格「無人工替代描述」標 ✗:absence-of-evidence → evidence-of-absence overreach。改成「公開資料未描述人工替代」或標 「未揭露」而非 ✗
- [Codex L5] CyberLink ✓「framing wording ✓」而非「實作 ✓」— 表格視覺易讓讀者誤讀。表格內加 footnote 或欄位拆分
- [Codex L1] 表格 source 欄裸 cid 串改成 `[c032, c033, c042]` 格式 — 對齊全文 citation density
- [Codex L4] §8 對照標準應直接 cite c053 (個資法 §8 primary doc),目前只 cite c098 — citation gap
- [Codex L8] 表格混合 SDK 供應商 (CyberLink c045) / 中游 vendor (WiXtar) / 部署終端 (雙月/金色三麥) — 加「責任層級」欄, 否則 vendor × 同意機制比較有 scope mismatch
- [Claude L4] c044 (CyberLink FaceMe SDK 產品頁) 在表格中未獨立佔列 — 若 c044 純 SDK marketing 與 c045 thought leadership framing 是否一致應 surface;c044 在 F1 標「依摘要層 sourcing,未經 deep-read 一手驗證」, 一致性未確認

---

### F7 (Q3+Q6 四重結構性零) — **❌** (load-bearing)

Convergent ❌ — both seniors. F7 + F4 同屬「Drafter 拿 extract 力道做超出 scope_caveat 推論」failure mode。**This is the single biggest publication blocker.**

**Required edits (publication blocker)**:
- [Codex L2 + Claude L2] **3,058 件/年 inference 隱形池下界 proxy 必修重寫**:現有 wording 把 residual buckets 加總 framing 為「A∩D 灰區隱形池下界 proxy」是 over-claim。c105/c106 extract 明確 caveat「『結構性零』≠『實質零』」「『其他』buckets 中可能含 biometric 相關投訴但無法獨立辨識」「桃園與新北 schema 結構不對齊,Drafter 不應 naive 加總跨縣市『其他』bucket 數字」。修改為:**「residual buckets 113 年新北 services_others 2,235 件 + 桃園『其他』823 件;若 inference 投訴存在則皆 absorbed 進此 opaque pool — 但 bucket 內 inference 比例完全 unknown。此 3,058 不能作為 inference 投訴量下界,只能作為『若有 inference 投訴 = invisible 的容量上界 proxy』」**。即 **invisible-ceiling 而非 inference-floor** [c105/c106]
- [Codex L2 — cherry-pick within c105] c105 另有 business_others 3,074 件,選 services_others 而排除 business_others 理由未交代 — 必修:或加入 business_others 並重述 proxy 計算,或明示為何 services_others 為主要 inference-relevant bucket
- [Codex L2 — extract 內部矛盾] c105 Passage 1 把 113 年 residual 寫成 714+432=1,146 (那是 103 年列), Passage 2 給 113 年 2,235/3,074。Drafter 採 Passage 2 應明示「以 full time-series analysis 為準」, 避免讀者抓 extract 內部矛盾
- [Codex L3 — hedge fading] 結尾「實質零假說站不住」太強。現有證據只能說「實質零不能被確認且有反向風險訊號」,不能說站不住 — 改為「實質零假說現有證據不能確認;反向風險訊號 (vendor framing vacuum + 律所 silence + NGO 立場) 三方匯流, 但無 row-level complaint / 消費者調查 / 現場觀察直接證據」
- [Claude L4 — cherry-picked omission] **c079 行政院消保會全國申訴統計 + c080 線上申訴系統** 都在 accepted,why_relevant 直接寫「Q6:全國消費者申訴統計 — Drafter 查『生物特徵類』申訴是否列項」。F7 只用 c105/c106 縣市層,**對全國層官方 source 完全 silent** — 必修:加 c079/c080 cite 或在 What we don't know 明確承認「全國層 schema access status / 結論未取得」[c079/c080]
- [Claude L4 — cherry-picked omission] **c095 高雄高等行政法院 114 年度簡字第 216 號判決** abstract 明示「自動化資料處理、特徵分析、行為定位、強制身份核實、資訊過濾和大規模監視等對兒童造成的風險」— 台灣行政法院唯一直接論述 profiling/特徵分析監控風險的判決。「司法零」claim 邊界判例 omission — 加註:「司法零僅限餐飲 inference 場景;高雄高等行政法院 114 年簡 216 雖屬兒少領域, 已論述 profiling/特徵分析監控風險 — 顯示行政法院已有 doctrine 萌芽 [c095]」

**TL;DR 連動修整**:
- [Both seniors] TL;DR 第 3 點 直接 inherit F7 over-claim — F7 修整後 TL;DR 必須同步:「3,058 件/年隱形池 lower-bound proxy」改為「3,058 件/年 visibility-blind residual pool capacity proxy (兩縣市 schema-design 容量, 不是投訴量下界)」

**Suggested**:
- [Claude L5] 量化 claim tier 從 [contested] 降為 [speculative]
- [Claude L8] F7 段引入 BIPA (US-IL) geographic scope = cross-theme blending — 建議拆段或明示「此段引入 Q5 國際比較 t09 source [c073]」

---

### F8 (Q5 國際對照) — **⚠️**

Convergent ⚠️。Claude L4 + Codex L2 共同指向「F8 對 Art. 5 解讀 + Home Depot 案性質」兩個 hedge gap。

**Required edits**:
- [Claude L2 + Codex L1/L2] **Home Depot c073 加 B vs A 區 scope_caveat hedge**: c073 extract scope_caveat 明示「Home Depot 案件性質為 loss prevention surveillance (防盜識別), 與 brief A 區 demographic inference 非完全同類:Home Depot 可能更接近 B 區身分比對而非 A 區 demographic categorisation」。F8 完全沒有複述。改為:「Home Depot 案技術屬性可能更接近 B 區 identification (loss prevention), 但訴狀的『無告示 + 無同意 + 無人工替代』邏輯對 A 區 inference 直接適用 — 援引的是其告知層失敗結構而非 case categorisation 一致性」[c073]
- [Claude L4] **加 c070 EC Feb 2025 prohibited AI practices guidelines** 作為 Art. 5 商業/職場界線權威解析。F8 對 Art. 5 商業/職場界線論述基於 c067 條文本身, 缺 c070 是 cherry-picking。若 F8 想 strong-tier 主張「emotion recognition 禁令僅及於職場/教育」,c070 必引 [c070]
- [Codex L2] 「GDPR Art. 9 + EDPB Opinion 11/2024 才是真正涵蓋商業 demographic inference 的 spine」過強。c077 是機場 FR/biometric identification,extract caveat 明示 airport scenario 非餐飲 inference,核心原則可轉用但不是直接涵蓋商業 demographic inference。改為「提供 biometric consent/withdrawal 的高標準參照」[c077]
- [Codex L2] EDPB「biometric template sole control 原則」extract caveat 說是 reduced intrusiveness design pattern, 不是 mandatory standard — 降語氣
- [Codex L4] CCPA 段 0 source: F8 第 1 段「BIPA / CCPA / SG PDPA / EU AI Act」對照 framing 但 CCPA 段未引 c074/c075 — citation gap

**Suggested**:
- [Claude L4] c071/c072 BIPA litigation trend 兩源也未引;F8 BIPA enforcement infrastructure 論述可加強 (僅 c073 單案略單薄)
- [Codex L4] 若維持 [strong] tier, 加 c068/c069 支撐 AI Act 範圍解讀
- [Codex L8] 段落 conceptual `A∩D` 對 c077 機場 identification source 是 application scope 而非 source scope — 加 transferability caveat

---

## Cross-cutting concerns

### 1. 「公開資料無提及」滑成「現場沒有」(Codex L2 systemic catch)
F2 / F6 / F7 三處皆有 absence-of-evidence → evidence-of-absence overreach。「無告示」「無人工替代」「站到前瞬間被掃描」應寫「公開資料未揭露;需現場查核」或降 tier。**Drafter v2 應全 draft grep 此 pattern**。

### 2. Causal language 太硬 (Codex L2 + Claude L2 同向)
「直接打掉」「結構性瓦解」「站不住」「幾乎不可能」「直接套用」「結構性瓦解」一連串硬語應限縮到 source 真正支持的子命題。c098 能打掉的是「仍可間接識別卻稱非個資」,不能 generalize 到所有 no-storage/no-identification implementations。F4 / F5 / F7 三處集中。

### 3. Paragraph-level L8 scope tag 形式 + coverage 兩問
- [Claude] HTML comment `<!-- {...} -->` vs Dr2 推薦 visible bold `**{...}**` — 若 lint regex 只認 visible bold, draft 全 8 個 Finding 將 fail。Operator 確認 lint 認哪一形式
- [Codex] Context / TL;DR / Counter-framing / What we don't know / 政策建議 sections 缺 paragraph-level scope tag。若 L8 paragraph-level audit 是 hard requirement, TL;DR 5 個 bullet 必須各帶 scope
- [Claude] `conceptual:A∩D` 在 themes evidence_scope_distribution 結構中無對應 key — 改為 `conceptual:A,D` multi-value 形式對齊 schema

### 4. Tier-tagging 一致性 (Dr1)
- F1 第 4 段 [speculative] tier 誤用 (內容為 strong B/C firewall)
- F4 第 4 段 [strong] 內夾「RAM/cache 短暫留存」無 cite mechanism inference
- F7 「3,058 件/年隱形池下界 proxy」標 [contested] 但實際應為 [speculative]
- F3 整段 [strong] 包含 c038 partial-access source — 細化為「c032/c037/c041/c042 strong + c038 partial」

### 5. Single-source/vendor self-claim handling — 標題/TL;DR 還需同步 (Codex)
F1 正文有把 c033 30+/1000+ 標 contested;TL;DR 與 Finding title 仍可能讓讀者讀成 A 區上界。所有出現「30+/1000+」處都固定附「WiXtar fleet claim; inference-enabled subset unknown」。

### 6. Brief failure-condition self-check (Claude L6 進行)
6 條 failure conditions 中:
- ❌ 倫理通論 / A-B 混為一談 / inference hand-wave / 無對照表 / GDPR 當台灣結論 — 5 條皆未發生
- ⚠️ supply-side vs demand-side 分離 — F1 supply-side OK, F2 demand-side 部分 OK, F7 試圖補 demand-side 結構性 invisibility 但 over-claim 為 inference proxy。分離意圖好, F7 執行不嚴謹

---

## Actionable edits for Drafter v2 (priority-ordered)

### 必修 P0 (publication blocker — 兩個 ❌ findings)

1. **F7 「3,058 件/年隱形池下界 proxy」over-claim 重寫** [c105/c106]
   - 改為「invisible-ceiling 而非 inference-floor」/「visibility-blind residual pool capacity proxy」
   - 處理 c105 內含 business_others 3,074 cherry-pick 疑慮
   - 處理 c105 extract Passage 1 vs Passage 2 內部矛盾
   - **TL;DR 第 3 點連動修整**
2. **F7 加 c079 行政院消保會全國申訴 + c080 線上申訴系統** 或 What we don't know 明確承認「全國層 schema access status 未取得」[c079/c080]
3. **F7 加 c095 高雄高等行政法院 profiling 判決** 作為「司法零」邊界判例 [c095]
4. **F4 釋字 603 transferability 必修降溫**:「以釋字 603 標準衡量連起點門檻都未滿足」→「提供比例原則與資訊自決強類比;直接套用需經水平效力 + 個資法中介論證」[c097]
5. **F4 「RAM/cache 短暫留存原始畫面」mechanism inference 無 cite — 必修** cite 或標 [speculative-mechanism] + What we don't know 列為 mechanism gap [c098]
6. **F4 / F7 全段 hedge fading**:「直接打掉」「結構性瓦解」「站不住」「幾乎不可能」全部降語氣為「大幅削弱」「不能僅憑...即豁免」

### 必修 P1 (publication tightening — 5 個 ⚠️ findings)

7. **F1 TL;DR + 標題**:固定附「WiXtar fleet claim; inference-enabled subset unknown」 [c033]
8. **F1 「2 brand 一手確認」wording** → 「2 brand confirmed by deep-read sources (vendor primary + media case-study)」[c032/c041]
9. **F2 表格 t₀-t₂ 現場流程 claim** 標 `inferred from public materials; no on-site audit` 或降 tier [c032/c033]
10. **F2 Showcase A「跨境傳輸」**加 hedge:「推論為跨境 — vendor 未明文確認 OpenAI/Azure API 是否經境外節點」[c033]
11. **F2 共同特徵段「站到前瞬間被掃描」**對金色三麥不適用 — 拆分 Showcase A (自動掃描) vs Showcase B (拍照觸發) [c042]
12. **F2 Confidence high → medium-high**
13. **F5 「同樣賣 demographic inference SDK / kiosk」**加責任層 caveat;「直接打掉 defence」→「削弱 defence」[c044/c045]
14. **F6 表格「無人工替代」✗** 改為「未揭露」(absence-of-evidence overreach fix) [c032/c033/c041/c042]
15. **F6 表格加「責任層級」欄** (SDK / 中游 vendor / 部署終端) [c044/c045]
16. **F6 表格 §8 對照 cite c053** (citation gap) [c053]
17. **F8 Home Depot c073 加 B vs A 區 scope_caveat hedge** [c073]
18. **F8 加 c070 EC Feb 2025 prohibited AI practices guidelines** [c070]
19. **F8 「EDPB Opinion 11/2024 才是真正涵蓋商業 demographic inference 的 spine」** 降語氣 [c077]
20. **F8 CCPA 段 cite c074/c075** [c074/c075]

### 建議 P2 (polish, not blocker)
- F1 第 4 段 [speculative] → [strong 為 B/C firewall]
- F4 [contested] → [strong] upgrade via c057-c060 / c088 / c061 (cross-律所 + primary doc 加入)
- F2 表格 OpenAI/微軟資料流 scope tag 加 `conceptual:A,C`
- 全 draft `conceptual:A∩D` → `conceptual:A,D` (schema alignment)
- Operator 確認 L8 lint regex 認 HTML comment vs visible bold
- TL;DR / Context / Counter-framing / What we don't know / 政策建議 sections 加 paragraph-level scope tag
- F3 [strong] 細化為「c032/c037/c041/c042 strong + c038 partial」
- F5 temporal 2023-2026 改逐源 anchor

### 不需修整 (合約典範,Drafter v2 不要動)
- F3 五源 cross-confirmed wording vacuum + CyberLink internal-split self-counter 框架
- F5 Dr7 partial_counter_framing caveat-tier 處理
- F1 雙端展開 + B/C firewall callout 結構
- F8 EU AI Act Art. 5 主動防誤讀 (workplace/education only)
- Counter-framing engagement section + 政策建議 section 結構

---

## What we don't know (per Reviewer)

繼承 draft 8 條 gap, **新增 2 條** (Reviewer 識別):
- **edge inference 系統實際是否在 RAM/cache 短暫留存原始畫面** (F4 Drafter 自引技術 claim 無 cite) — 屬「需技術驗證的關鍵 mechanism claim」,應 surface 為 gap
- **全國層消費爭議申訴 schema 是否含 biometric/inference category** (c079/c080 accepted 但 F7 未引) — 若 Drafter 嘗試過 c079/c080 但無 row-level data, 應主動承認

---

## Overall verdict

🟡 **publishable with edits** (2-senior consensus)

整體 architecture 合約合規且論證骨幹紮實。Dr1 tier-tagging、Dr2 scope tagging、Dr7 partial_counter_framing 處理在多數 finding 為合約典範;A/B/C firewall 嚴格、釋字 603 + 111 憲判 13 憲法 spine 援引精彩、CyberLink internal-split partial counter rescue 為教科書範例 (Claude 評)。Source discipline 大致可用 (Codex 評), 不是推倒重寫 — 核心架構與 9 themes synthesis 不需重做。

但 F4 + F7 兩個 ❌ 屬 publication-blocker 等級, 兩者共享同一 failure mode (Drafter 推 extract 過 scope_caveat)。F7 + TL;DR 第 3 點是最 visible 對外風險 — 媒體易把「3,058 件/年隱形池下界」誤讀為投訴量, 必修。F4 釋字 603 transferability + RAM/cache mechanism 兩處是法律論述硬語 + unverified mechanism, 必修。

**Recommendation for operator**: 走 v1 + hand-edits patch (而非 trigger v2 Drafter pass)。理由:
1. 兩個 ❌ findings 的修整是 **wording-level 重寫 + cite 補充**, 不涉及 finding 結構重設計或新 evidence 收集
2. P0 共 6 條 + P1 共 14 條, 估計 Drafter 手動編輯 2-3 小時可完成 — 比 v2 full pass (4-6 小時 + 重 review) 更快
3. F3 / F5 / F1 / F8 / F6 / F2 六個 finding 的 evidence 結構與 framing 不需動, v2 重寫風險為意外退化已合規部分

但建議走 v2 的條件:
- 若 operator 認為 F4 + F7 需要重新組織 (e.g. F7 拆出獨立的「invisible-ceiling vs inference-floor」方法論段, F4 加入 c057-c060 跨律所升 strong)
- 若 lint 對 HTML comment scope tag 不認, 需全 draft scope tag 重寫 (這項本身就接近 v2 工作量)

**Meta-merger recommendation**: ship v1 with P0+P1 hand-edits patch + clarify lint regex with operator。觸發 v2 only if operator 想升 F4 + F7 為 [strong] tier (需要新 source 加入)。

---

## Reviewer schema/spec feedback (audit log)

1. **integrity_report.json 未持久化到 disk**: 操作者於 prompt 提供值, 但 `pipeline/review/integrity_report.json` 不存在。建議 multi-model spec §10 補:「integrity_check.py 必須 write `pipeline/review/integrity_report.json` 而非僅返回 stdout」, 以便 meta-merger 與後續 audit 有 file 可追。本次 merge 信任 operator 提供值。
2. **Gemini absence 處理 in spec**: spec §2 + §9 提到 Gemini 為 junior parity-check, 但沒有明示「3× timeout 後 graceful degrade to 2-senior fallback」流程。建議 spec §9.5 補:「若 Gemini 連續 3 次 timeout / unreachable, meta-merger 應在 review.md 顯式宣告 fallback mode, 並對所有 Gemini-default 場景套用『N/A; Gemini 缺席, lens 由 2 seniors 載重』」。本次採用此做法。
3. **stricter-wins on divergent verdicts**: spec §6 提到 weighted score for ordering, 但 R1-R6 verdict 規則對「兩個 senior 在同一 finding 上 ✅ vs ⚠️ 的中間情境」未明示 default。Operator 在 prompt 中提供「stricter wins for safety」bias — 建議寫入 spec §8 作為 default tie-break, 而非 per-run operator instruction。
4. **R2 extension**: prompt 明示「senior reviewer ❌ on L2 / L4 / L6 / L7 / L8 → finding ≥ ❌ unless senior counter-evidence」— 本次 audit 已套用 (F4)。建議寫入 spec §8 永久化。
5. **L8 scope tag form ambiguity**: Dr2 spec 建議 visible bold `**{...}**`, 但 Dr-a default position 推 HTML comment `<!-- {...} -->`。Drafter 採 Dr-a, lint 認哪個未明示。建議 brief_expanded.yaml 或 sources.yaml 加 `review.scope_tag_form` 欄位, 由 operator 在 §1 framing 階段聲明。
6. **A∩D 合法 conceptual key**: brief_expanded.yaml ontology 定義 A/B/C/D 單值, 但 brief research_focus 是 A∩D。Drafter 多處用 `conceptual:A∩D`, L8 lint 對 themes evidence_scope_distribution `{A:n, D:m}` 結構不對齊。建議 brief_expanded 加入「合成 conceptual key 是否合法 + scope tag 寫法 (A∩D vs A,D)」明確規定。

---

*Meta-merge by Claude Opus 4.7. Source reviews: r_claude.md + r_codex.md (multi_model/). Gemini absent (3× MCP timeout). Integrity clean. No findings invented — every catch traces to at least one named senior reviewer with lens attribution.*
