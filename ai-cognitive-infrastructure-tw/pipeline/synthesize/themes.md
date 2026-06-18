# Synthesizer themes — ai-cognitive-infrastructure-tw

**9 themes** organized around the **four-link causal chain** (spine, link-by-link) + the **break-point** (centerpiece) + the **counter-evidence / §6** cluster. This is an EVIDENCE AUDIT, not a topic survey: every theme carries an explicit per-link strength verdict so the Drafter can write the report's load-bearing conclusion — *the chain is only as strong as its weakest load-bearing link, and it most likely breaks at L4b→L4c.*

theme_type breakdown: `evidence_cluster` ×5 (t01 L1, t02 L2, t04 L4a, t06 L4c, t08 FW), `narrative_anchor` ×3 (t03 L3 strong, t05 L4b bounded, t09 counter-§6), `mixed` ×1 (t07 break-point — narrative_anchor + the boundary it asserts spans L4b/L4c/CE axes).

## How brief questions map to themes

This brief has **no numbered `## Key questions` section** — its question structure is the **chain links L1–L4c + FW + CE**, as the Gatekeeper and Segmenter both confirmed (coverage is by-LINK, not by-Q). The schema's `linked_brief_questions` field requires `Q<n>` form, so the six auditable links + the two cross-cutting clusters are mapped to Q-ids as follows. Drafter should read the Q-id purely as the link tag:

| Q-id | Chain link / cluster | Expected strength (brief) |
|---|---|---|
| **Q1** | L1 — price → adoption | contested (causal arrow) |
| **Q2** | L2 — AI as information entry | contested-trending |
| **Q3** | L3 — stable measurable framing | strong |
| **Q4** | L4a — output homogenization | contested |
| **Q5** | L4b — individual belief shift | weak / bounded |
| **Q6** | L4c — societal aggregation | speculative (near-empty) |
| **Q7** | FW — cognitive-infrastructure frameworks (conditional policy) | framework-only |
| **Q8** | CE — counter-evidence / §6 anti-alarmism | n/a (breaks the chain) |

Every Q1–Q8 is covered by ≥1 theme. No uncovered questions.

---

## Rewrite warnings for Drafter

Three load-bearing framing revisions surfaced once the evidence was in hand. The brief's pre-research wording must NOT be written back into the report on these points.

### Warning 1 — claim_collapse / framing_shift: the chain breaks at L4b→L4c (and the evidence says so explicitly)
- **what_changed**: The brief states "the chain most likely breaks between L4b and L4c" as a *hypothesis to test*. The evidence converts it from hypothesis to **established finding**: bounded individual-level persuasion is well-evidenced (Q5), while single-dominant-model population-scale cognitive shift has ZERO direct evidence (Q6 = framework + simulation + analogy only). Write L4c-collapse as the report's load-bearing conclusion, not as a tentative guess.
- **original_phrasing**: "the chain most likely breaks between L4b and L4c. Mark speculative plainly."
- **evidence_anchor**: c026, c027, c028 (bounded individual) vs c032, c033, c034 (no direct L4c) + c044 (LLM output ≠ population opinion).
- **drafter_action**: Frame the conditional policy conclusion firmly — "model governance becomes a sovereignty/cognitive-security issue ONLY IF L4c holds, and the evidence shows it does not yet hold." Do not soft-pedal into "more research needed on whether the chain holds"; the break location is itself the finding.

### Warning 2 — term_revision: the −43% / −33% referral figures are Chartbeat (c015), NOT Reuters (c014)
- **what_changed**: An upstream candidate snippet bundled the "-43% projected referral decline / -33% Google organic traffic" figures with the Reuters DNR 2025 record. WebFetch of the Reuters executive summary did NOT contain those numbers — they trace to Chartbeat data restated by Search Engine Land. Reuters DNR's actual contribution is the 7% chat-LLM vs 4% AI-Overviews separation.
- **original_phrasing**: Brief L2 task cites "Google Zero / referral-traffic decline" generically without attributing the specific figures.
- **evidence_anchor**: c014 (Reuters — owns the 7%/4% mechanism separation, NOT the referral numbers), c015 (Chartbeat/SEL — owns −43%/−33%, fast-skip / Dr3 secondary tier).
- **drafter_action**: Attribute −43%/−33% to Chartbeat/c015 explicitly and tag it Dr3 snippet-layer (trade-press restatement, possibly AI-Overviews-driven not chat-LLM substitution). Attribute the 7%/4% chat-vs-Overviews separation to Reuters/c014. Never blend them.

### Warning 3 — framing_shift / unexpected_finding: the intermediation channel has a STRUCTURAL (paywall-asymmetry) explanation, not an intentional-amplification one
- **what_changed**: The brief frames "AI as information intermediary" as a channel through which framing flows. The strongest intermediation evidence (FDD c041: state-aligned propaganda in 57% of LLM responses across ~180 questions incl. Taiwan-China) comes WITH its own non-conspiratorial mechanism: democratic premium press is paywalled / blocks AI crawlers, while state media flows freely. This is a §6-anti-alarmism datapoint embedded inside the most alarming-sounding source.
- **original_phrasing**: "operationalizes 'AI as information intermediary' by auditing the citation channel" (treats it as channel evidence without the access-economics caveat).
- **evidence_anchor**: c041 (FDD — both the 57% figure AND the paywall-asymmetry mechanism).
- **drafter_action**: When citing the 57% propaganda-citation figure, pair it immediately with the paywall-asymmetry explanation. Do NOT present the FDD finding as evidence of intentional cognitive warfare; it is consistent with access economics. This keeps the report inside the governance-under-uncertainty frame.

---

## Theme t01 — L1: Price→adoption — supported, but the causal arrow is the contested part

- **theme_type**: evidence_cluster | **cluster_source**: l1_price_adoption | **linked Q**: Q1
- **PER-LINK STRENGTH VERDICT**: **SUPPORTED (dated primary snapshot)** — adoption-rising is well-evidenced by primary market data as-of 2026-06-08; the price→adoption causal arrow (vs capability / openness / licensing) is the genuinely contestable part.
- **Members**: c010, c011, c012, c036
- **Definition**: Primary market-data snapshot (as-of 2026-06-08) documenting rapid penetration of cheap Chinese open-weight models: OpenRouter price-per-Mtok spread ~51–460× (c010), HuggingFace download dominance of Qwen/DeepSeek (c011), token-share rising from 1.2%→~13% in a year (c012), and population-representative usage showing concentration AND diversity coexisting (c036). CONTAINMENT: these numbers prove L1 (adoption) ONLY — they must never be smuggled into L4 (cognition shaped). The causal-identification literature (price vs capability) lives in the Dr3 snippet pool (c008, c009).

## Theme t02 — L2: AI as information entry — thin, contested-trending ceiling

- **theme_type**: evidence_cluster | **cluster_source**: l2_ai_information_entry | **linked Q**: Q2
- **PER-LINK STRENGTH VERDICT**: **CONTESTED-TRENDING (ceiling)** — only 3 sources total, 0 peer-reviewed; tier cannot rise above contested-trending. The chat-LLM vs AI-Overviews mechanism separation is the load-bearing guard.
- **Members**: c014, c041
- **Definition**: Reuters DNR 2025 (c014) is the strongest L2 anchor precisely because it SEPARATES chat-LLM news use (7%; under-25 15%, India 18%) from in-search AI Overviews (4%) — two distinct mechanisms the brief warns against conflating. c041 (FDD) operationalizes the intermediation channel by measuring which SOURCES the AI routes users to (57% state-aligned-propaganda citation rate, incl. a Taiwan-China arm). The −43%/−33% referral-decline figures belong to Chartbeat/c015 (Dr3 secondary, trade-press restatement), NOT to Reuters — see Rewrite Warning 2.

## Theme t03 — L3: Stable measurable framing — the STRONG link

- **theme_type**: narrative_anchor | **cluster_source**: cross_cluster (anchor_literature + repo-internal; no dedicated L3 cluster) | **linked Q**: Q3
- **PER-LINK STRENGTH VERDICT**: **STRONG.**
- **Members**: c001, c002, c003, c004
- **Definition**: The chain's strongest link, anchored by (1) Waight Nature 2026 (c002) — STRICTLY correlational cross-national audit + causal claim ONLY at model-OUTPUT level via continued-pretraining; NO user-belief claim (load-bearing scope boundary); (2) Buyl c003 + Samokhodskyi c004 — symmetric Western-model framing tests ("false balance" / "bothsidesism") that guard against directional artifact / anti-China reading; (3) the repo's own abliteration killer-mechanism (c001) — same model, de-aligned, produces Taiwan-mainstream framing → bias is post-training/RLHF, NOT corpus absence; "all models, regardless of origin, remarkably similar." LOAD-BEARING BOUNDARY: L3 (output) ≠ L4b (user belief). Drafter must not let L3 strength leak into L4 claims.

## Theme t04 — L4a: Output homogenization — healthy, including disconfirming evidence

- **theme_type**: evidence_cluster | **cluster_source**: l4_amplification_decomposed | **linked Q**: Q4
- **PER-LINK STRENGTH VERDICT**: **HEALTHY (with disconfirming evidence preserved).**
- **Members**: c017, c018, c035, c036
- **Definition**: Kleinberg & Raghavan algorithmic-monoculture anchor (c017 — SCOPE NOTE: object is hiring/lending decision systems, NOT LLM info-output; extension to LLMs is an open question) + the LLM-specific generative-monoculture demonstration (c018 — output-diversity narrowing, root cause "embedded within alignment processes," converging with c001/c043). DISCONFIRMING evidence is deliberately kept inside the theme: users run MANY models (c035 — note: % overlap inference, not a verbatim claim) and population-representative data shows concentration AND diversity coexisting (c036). The theme does NOT straw-man L4a as settled homogenization.

## Theme t05 — L4b: Individual belief shift — RICH but BOUNDED

- **theme_type**: narrative_anchor | **cluster_source**: l4_amplification_decomposed | **linked Q**: Q5
- **PER-LINK STRENGTH VERDICT**: **RICH at individual level, but BOUNDED — capability established, scale NOT.** This is the load-bearing boundedness the whole report rests on.
- **Members**: c023, c024, c026, c027, c028, c031
- **partial_counter_framing**: TRUE — the boundedness here IS the counter-position to the chain's amplification claim, rescued via the studies' own scope qualifications (no direct quote rebuts "AI shifts society"; instead each RCT bounds its own effect). See JSONL.
- **Definition**: Seven human-subject persuasion sources (incl. rescued c028) establishing that LLM framing CAN move individual belief — but every one foregrounds BOUNDEDNESS: Hackenburg (c026) frontier models "barely more persuasive than models smaller by an order of magnitude"; Chen/Kalla/Le (c027) "not a substantially greater threat to democratic societies than existing human-driven methods," "constrained by scale"; Salvi (c024) non-significant WITHOUT personalization (p=0.31); Shu/c028 small default d=0.14, conservative effect (d=−0.13) ONLY in the already-conservative subgroup → latent framing AMPLIFIES pre-existing leanings, does not move everyone; Costello/c023 durable ~20% but debunking-direction; c031 valence-symmetric (channel is neutral). LOAD-BEARING: this bounded individual capability is NOT L4c population shift. c027 and c028 carry the HIGHEST over-read risk (c027 title "democratic societies"; c028 must not scale to society).

## Theme t06 — L4c: Societal aggregation — the EMPTY CELL is the finding

- **theme_type**: evidence_cluster | **cluster_source**: l4_amplification_decomposed | **linked Q**: Q6
- **PER-LINK STRENGTH VERDICT**: **SPECULATIVE / EMPTY of direct evidence.** The empty cell is itself THE finding.
- **Members**: c032, c033
- **Definition**: There is NO direct evidence linking a single dominant information intermediary's framing to population-scale cognitive shift. The only adjacent material is: a framework that merely "defines this emerging area / lays out a program of research" (c032, Carley social cybersecurity); an LLM-AGENT simulation, not real humans, that even needs prompt-induced confirmation bias to look human-like (c033, Chuang opinion dynamics); and an agenda-setting ANALOGY from social media (c034 — fast-skip / Dr3, MUST be labelled analogy, NEVER LLM L4c direct evidence per brief handling_protocol). Drafter writes this gap AS a research agenda: what longitudinal / large-N study would close L4c.

## Theme t07 — THE BREAK POINT: L4b→L4c (centerpiece, load-bearing conclusion)

- **theme_type**: mixed (narrative_anchor spanning L4b / L4c / CE axes) | **cluster_source**: cross_cluster | **linked Q**: Q5, Q6
- **PER-LINK STRENGTH VERDICT**: **THIS IS WHERE THE CHAIN BREAKS.** Bounded individual persuasion capability (L4b) is well-established; single-dominant-model population-scale cognitive shift (L4c) is unproven. The step between them does NOT hold on current evidence.
- **Members**: c026, c027, c028, c032, c033, c044
- **partial_counter_framing**: TRUE — the break itself is the counter to the chain's landing claim, rescued via scope qualification (L4b sources bound their own scale) + the c044 methodological caution (LLM output ≠ population opinion). See JSONL.
- **Definition**: The report's centerpiece. Assembles, on one side, the bounding L4b evidence (c026 log-scaling cap; c027 "constrained by scale," not a greater threat than humans; c028 small subgroup-limited effect) and, on the other, the empty L4c cell (c032 framework-only, c033 simulation-only) plus the explicit methodological caution that LLM output must be used "alongside conventional methodologies" and is NOT population opinion (c044). The synthesis: individual-level bounded persuasion is established; population-scale cognitive restructuring from a single dominant model is unproven — therefore the spec's policy claim is CONDITIONAL on an L4c that the evidence does not support. This theme also carries the "what study would close L4c" research-agenda material.

## Theme t08 — Cognitive-infrastructure frameworks (conditional-policy grounding)

- **theme_type**: evidence_cluster | **cluster_source**: cognitive_infra_frameworks | **linked Q**: Q7
- **PER-LINK STRENGTH VERDICT**: **FRAMEWORK-ONLY** — grounds the borrowed labels; supplies the conditional policy vocabulary; does NOT itself evidence any chain link.
- **Members**: c032, c041
- **Definition**: Grounds the spec's borrowed labels (cognitive security / information sovereignty / gatekeeper) in real literature so the framing rests on sources, not labels. Deep-read members are thin: c032 (Carley social-cybersecurity vocabulary) and c041 (FDD intermediation-channel audit, the FW/L2-L3 bridge, incl. the paywall-asymmetry structural mechanism — Rewrite Warning 3). The substantive sovereignty / DMA-gatekeeper / cognitive-sovereignty anchors (c037 Pohle, c038 Brcic, c039 Li, c040 Abiade) are all fast-skip / Dr3 snippet-layer — Drafter should cite them at contested-tier ceiling with snippet-sourcing annotation. HANDOFF NOTE: this theme is structurally thin at deep-read depth; see handoff.

## Theme t09 — Counter-evidence / §6 — anti-alarmism, its OWN theme

- **theme_type**: narrative_anchor | **cluster_source**: counter_evidence_section6 | **linked Q**: Q8
- **PER-LINK STRENGTH VERDICT**: **STRONG ENOUGH that the report cannot be read as anti-China alarmism.** (Not a chain link — the chain-breaking cluster.)
- **Members**: c035, c036, c042, c043, c044
- **partial_counter_framing**: TRUE — these are the §6 incorrect-inference rebuttals, rescued via mechanism inference (bias from RLHF/safety/commercial, not political intent) + disconfirming evidence + scope qualification. See JSONL.
- **Definition**: Operationalizes the spec's §6 so the report stays inside the governance-under-uncertainty frame: bias/framing originates in RLHF/safety/alignment design choices, NOT necessarily political intent (c042); framing is prompt/language-contingent and mutable, all origins converge "remarkably similar," undercutting baked-in-political-intent reads (c043); disconfirming homogenization evidence — users run many models, diversity coexists with concentration (c035, c036); and the methodological caution that one cannot infer real population opinion from LLM output (c044). Drafter must surface this as its own section, not bury it. NOTE: the adoption-is-capability-not-price causal-arrow counter (c008, c009) lives in the Dr3 snippet pool, not at deep-read depth.

---

## Summary for Drafter

- **Spine** (link-by-link, with strength verdicts): t01 L1 supported / t02 L2 contested-trending / t03 L3 STRONG / t04 L4a healthy+disconfirming / t05 L4b rich-but-BOUNDED / t06 L4c EMPTY.
- **Break point** (centerpiece, t07): the chain breaks at **L4b→L4c**. Bounded individual capability established; population-scale shift unproven. The policy claim is conditional on an L4c the evidence does not support.
- **Counter-evidence** (t09) is its own theme; the report cannot be read as alarmism.
- **Under-evidenced — Drafter must hedge HARD**: t06 (L4c, empty of direct evidence — write as research agenda, not as a finding) and t08 (frameworks — deep-read thin; substantive anchors are Dr3 snippet-layer, cap at contested tier with snippet annotation). t02 (L2 — only 2 deep-read members, 0 peer-reviewed; contested-trending ceiling). c027 and c028 carry the highest over-read risk and must be quoted with their boundedness intact.
