# Segmenter index — willing-partner-tw

**Deep-read budget**: all 27 accepted records prioritized for deep-read (small, tightly-scoped corpus; no qs=2/3 background-only tier exists in this project's gate schema — accept/reject was binary)
**Records accounted for**: 27/27 accepted cids — 22 individual extract files + 1 cluster file (covering 5 cids) = 23 extract files total
**Access outcomes**: 24/27 fully raw-verified (ok or ok-via-Wayback); 3/27 access_blocked despite multi-route recovery attempts (c019, c020, c028)
**Critical-priority verifications (task-assigned)**: c007 resolved via Wayback; c026 resolved via GitHub source (not Wayback HTML — see below); c006 resolved via Wayback, cross-confirmed across two snapshots 8 months apart
**Date**: 2026-07-05

---

## Deep-read — all 27 accepted cids

### A-concept (courtship register), Q1
- **c001**: 2019-06-19 Meta-TFC launch (Alice Budisatrijo + 胡元輝 quotes, re-verified independently of seeds' prior verification) — Taiwan **courtship pole** of the Q4 say-do pair.
- **c002**: 中央社/TechNews independent corroboration of the same 2019-06-19 event; adds Remove/Reduce/Inform mechanism detail + repeat-offender demonetization (new B-mechanism texture).
- **c003**: LINE 2019-07-22 launch, 4-org coalition (TFC/MyGoPen/Cofacts/蘭姆酒吐司) named verbatim; recovered via Wayback (live Cloudflare-blocked).
- **c004**: 2021-08-28 Facebook accelerator — **new named Facebook official quote** (Keren Goldshlager) not in the gate snippet or seeds; recovered via Wayback (live 404s).
- **c005**: NPR 2019-12-06 — confirms TFC's "back-end tool" access from Facebook, the pre-2020-election B-concept baseline for what CrowdTangle/MCL later constrained.

### B-concept (mechanism + defunding), Q2/Q3
- **c006** [CRITICAL]: Meta Transparency Center current wording — **all Q2 mechanism sentences raw-verified**, including exact confirmation of "same or almost exactly the same as that rated by fact checkers"; **confirmed zero occurrences of "train/training"** in the mechanism text (only as an unrelated nav link); cross-confirmed stable across 2025-03 and 2026-01 snapshots.
- **c007** [CRITICAL]: IFCN open letter — TFC + MyGoPen confirmed as Taiwan signatories (raw-verified against Jan-10, 2025 snapshot); Cofacts confirmed absent; Summer Chen/FactLink reconciled via cross-reference to seeds' later-dated check (see below).
- **c009**: 經濟日報 2025-12-13, TFC chairman 羅世宏 — Taiwan **behavioral pole** of the Q4 say-do pair (documented action/inaction via TFC's own account, not a Meta quote).
- **cluster-global-termination** (c010/c012/c013/c014/c015): five reports, one triggering event, five distinct contributions — Global-South reaction + mechanism admission (c010), scale stats + US partner quote (c012), second Zuckerberg-video transcription (c013), 15-month institutional-check follow-through into 2026-04 (c014), explicit Taiwan namecheck + political-rebalancing framing (c015).
- **c016**: TFC's own 2025 donation-report page — **Meta=50% (2025) / 52% (2024)**, explicitly labeled licensing income both years; resolves the brief's dual-attribution mandate.
- **c017**: TFC's own OSF-donation explainer — confirms OSF funding stopped H2-2024; independently confirms "Meta = half of annual revenue" in TFC's own prose (second phrasing, same fact as c016's table).

### C-concept (partner agency/leverage), Q5
- **c018**: Community Notes cross-language dependency study — two-sided finding (cited notes rated more helpful, but overall reliance minimal); genuine Q5 leverage nuance.
- **c019**: **ACCESS BLOCKED** — Cloudflare JS-challenge + zero Wayback snapshots + Semantic Scholar lookup failed. The gate snippet's quote (Q5's flagged sole "label freshness" anchor) **could not be verified**; flagged loudly per protocol.
- **c020**: **ACCESS BLOCKED** — Cloudflare JS-challenge + Wayback's own crawler also 403'd on all 4 attempts across 8 months. Gate summary unverified; thesis independently covered by c021 instead.
- **c021**: Sehat et al. 2024 — **directly-quoted fact-checker interviewee** on claim-lifecycle prioritization (stronger than the gate snippet indicated) + independently verifies the local-context thesis c020 was meant to supply.
- **c022**: 行政院打詐綱領2.0 — confirms "結合民間團體" language; **confirms the Collector's flagged contamination risk was real** ("事實查核資料庫" does not appear in this document).
- **c023**: moda 新聞稿 — re-confirmed documented negative (no 查核 mention); self-built-tooling framing instead.
- **c024**: 高雄市刑事警察大隊 — richest C4 instance found: all 4 Taiwan orgs named + LINE mechanism description independently corroborating c003 seven years later.
- **c025**: 法務部調查局 — central-government instance naming 3 of 4 orgs (Cofacts confirmed absent here — asymmetry vs c024 worth noting precisely).
- **c026** [CRITICAL]: Cofacts about page — resolved via GitHub source component (Wayback HTML structurally cannot capture this page's client-rendered content); found genuine "Free and Open" philosophy text + 2023 NGO-incorporation detail; **confirmed the CC BY-SA license text does NOT live on this page** (it's in a separate LEGAL.md, already in seeds).
- **c027**: Taiwan Insight academic blog — "three musketeers" framing + a new IFCN "best fact-checking report of the decade" award detail (王立強 case).
- **c028**: **ACCESS BLOCKED** (paywall, live + same-day Wayback capture both blocked) — only the one-line og:description confirmed; substance covered by verified c003/c024 instead.
- **c029**: NPOst 2019 — Cofacts founder ("Johnson") origin-story quote, independent of and complementary to c026/seeds.

---

## Actor × register table (引文歸屬表)

This table implements the brief's citation-attribution requirement (Existing knowledge §2(d)): every courtship/exit register entry is tagged by actor so the Reviewer can machine-check that **no say-do pair crosses actors**. Sources not carrying a courtship/exit register (context, technical, partner-account, counter-framing) are included for completeness but are not part of any say-do pair.

| cid / source | actor | register | date | verification |
|---|---|---|---|---|
| seeds: promise-archive-meta.md #1 | Meta (Adam Mosseri) | **courtship** | 2016-12-15 | primary-verified (seeds) |
| seeds: promise-archive-meta.md #3 | Meta (Tessa Lyons) | **courtship** | 2018-06-14 | primary-verified (seeds) |
| seeds: promise-archive-meta.md #4 | Meta (Tessa Lyons) | **courtship** | 2018-09-13 | primary-verified (seeds) |
| c001 | Meta (Alice Budisatrijo) / TFC (胡元輝) | **courtship** | 2019-06-19 | raw-verified (this pass, independently re-confirmed) |
| c002 | Meta (Alice Budisatrijo, via 中央社) | courtship (press-corroborated) | 2019-06-19 | raw-verified |
| c003 | LINE / TFC+MyGoPen+Cofacts+蘭姆酒吐司 | courtship / technical | 2019-07-22 | raw-verified (via Wayback) |
| c004 | Meta (Keren Goldshlager) | **courtship** | 2021-08-28 | raw-verified (via Wayback) |
| seeds: promise-archive-meta.md #5 | Meta (陳奕儒/Chen Yi-Ju, Taiwan PR) | **courtship** | 2020-03-30 | primary-verified (seeds) |
| c005 | Meta / TFC (via NPR) | technical / context | 2019-12-06 | raw-verified |
| c006 | Meta (self-description) | technical | current (2025-03~2026-01, cross-confirmed) | raw-verified (via Wayback ×2) |
| c007 | IFCN/Poynter + 100+ signatories incl. TFC/MyGoPen | counter-framing (partner reaction) | 2025-01-09/10 | raw-verified (via Wayback) |
| seeds: promise-archive-meta.md #6 | Meta (Joel Kaplan) | **exit** | 2025-01-07 | primary-verified (seeds) |
| seeds: promise-archive-meta.md #7 | Meta (Mark Zuckerberg) | **exit** | 2025-01-07 | primary-verified (seeds) |
| c009 | TFC (羅世宏/邱家宜) describing Meta's behavior | **partner-account — this is the Taiwan 行為 pole, NOT a Meta exit quote** | 2025-12-13 | raw-verified |
| cluster c010/c012/c013/c015 | Meta (via press) / press / named partners (Alan Duke, Zainab Husain, AFP's Chetwynd) | exit (re-transcribed) + counter-framing + context | 2025-01-09/10 | raw-verified (mixed; c013 via Wayback) |
| cluster c014 | Meta / Oversight Board / EFCSN / Tech Policy Press | context (institutional-check follow-through) | 2026-04-21 | raw-verified |
| c016 | TFC (self) | partner-account | 2026-06-11 (dateModified) | raw-verified |
| c017 | TFC (self) | partner-account | 2025-02-10 | raw-verified |
| c018 | scholar | context | 2025-12 | raw-verified (pdf) |
| c019 | scholar | context | 2025 | **verification FAILED** — access_blocked |
| c020 | scholar | context | 2024 | **verification FAILED** — access_blocked |
| c021 | scholar (+ anonymized interviewee "P10") | context | 2023-2024 | raw-verified (pdf) |
| c022 | gov (行政院) | context | 2024 | raw-verified (negative confirmed) |
| c023 | gov (moda / 黃彥男) | context | 2024-05-28 | raw-verified (negative confirmed) |
| c024 | gov (高雄市刑事警察大隊) | context | n.d. | raw-verified |
| c025 | gov (法務部調查局) | context | n.d. | raw-verified |
| c026 | Cofacts (self) | partner-account | current (source-current) | raw-verified (via GitHub source, not Wayback) |
| c027 | scholar (Taiwan Insight/Nottingham) | context | 2023-03-31 | raw-verified |
| c028 | LINE/gov (via Foreign Policy) | context | 2020-11-23 | **verification FAILED** — access_blocked (paywall) |
| c029 | Cofacts (Johnson, founder) | partner-account | 2019 | raw-verified |
| seeds: karp-quotes.md (12 quotes) | Alex Karp / Palantir | **discourse specimen — explicitly NOT a courtship/exit register; self-contained "話語章"** | 2024-2026 | primary-verified (seeds); **zero Taiwan/TSMC connection confirmed** |

### Machine-checkable say-do pairs in this evidence base
1. **Global Pair 1 (Meta 3PFC)**: courtship = seeds #1/#3/#4 (Mosseri 2016, Lyons 2018×2) → exit = seeds #6/#7 (Kaplan/Zuckerberg 2025-01-07). Same actor (Meta), same program (3PFC). ✓ same-actor, same-program.
2. **Global Pair 2 (Meta research-access/CrowdTangle)**: courtship = Meta's multi-year free provision of CrowdTangle to researchers/fact-checkers (documented in seeds/extraction-audit-journal.jsonl, "單向鏡" lane) → exit = 2024-08-14 CrowdTangle shutdown + restrictive Meta Content Library gating (same lane). Same actor (Meta), same program (researcher tooling). Not independently re-verified by this Segmenter pass (seeds' own curl-verification already covers it) — cross-referenced, not re-extracted.
3. **Taiwan Pair (語料 vs 行為 — per operator's explicit framing for this run)**: 語料 = c001 (Budisatrijo 2019-06-19) + seeds #5 (陳奕儒 2020-03-30) → 行為 = c009 (TFC's own account of Meta's silence / continued ~50% budget dependency / 2026-01 contract-lapse risk). **This pair is deliberately NOT actor-symmetric in the same way as the global pairs** — there is no recorded Meta exit *quote* specific to Taiwan (Meta has made no Taiwan-specific "biased"/"censorship" statement the way it did for the US). The exit-side evidence is *behavioral*, reported through the partner (TFC), which is exactly the brief's required framing (Existing knowledge §2: "拿到想要的才走" is unprovable motive; what's provable is "走時承諾清零、資產留存" as documented action). **Do not manufacture a Meta Taiwan exit quote that does not exist.**

**Reviewer note**: no candidate pair in this evidence base crosses actors (e.g., no "OpenAI's behavior paired against Meta's promise"). The OpenAI/Anthropic material (seeds/extraction-audit-journal.jsonl's dedicated red-teaming lane) is **mechanism-isomorphism only** — external contributor labor (red-teamers, low-resource-language annotators) feeding into a proprietary internal system, structurally parallel to fact-checker ratings feeding Meta's detection system — and per the brief's explicit and non-negotiable instruction (Existing knowledge §2(b)), **must appear in its own self-contained section with the limitation stated explicitly**, and must never be blended into a courtship→exit narrative for OpenAI/Anthropic, because no such recorded arc exists for either lab.

---

## Cross-reference table: seeds/*.md → brief questions

(Segmenter did not re-extract seeds' content — this table exists so the Drafter has one index spanning both newly-extracted accepted-record material and the pre-existing seed material.)

| Seed file | Covers | Serves | Notes |
|---|---|---|---|
| `promise-archive-meta.md` | 7 courtship/exit quotes (6 primary-verified, 1 flagged UNVERIFIED — the Nov 2016 Zuckerberg NPR-transcribed line) + a "three-line say-do contrast" synthesis | Q1, Q4 (global pair) | Do not cite the UNVERIFIED Zuckerberg 2016-11 line per brief Exclusion §1. The 2019-2020 gap this seed flagged as missing is now filled by this Segmenter pass (c001/c003/c004/seeds#5). |
| `extraction-audit-journal.jsonl` | 40 claims across ~5 adversarial "lanes" + a verdicts/adversarial-check lane; top-20 claims all verdict "holds," zero "refuted." Lanes sampled by this Segmenter pass: (1) "鋼人反方" — durable/irrevocable assets (ThreatExchange/HMA BSD open-source, StopNCII NGO-operated model, IFCN letter's "program was effective" admission w/ hedge, Google.org/LINE/TFC/Cofacts Taiwan capital); (2) "台灣在地價值流" — TFC/MyGoPen/LINE/Cofacts/Google.org/2024-election Taiwan-specific value-flow claims; (3) "單向鏡" — CrowdTangle shutdown, Meta Content Library gating, X API paywall + CCDH lawsuit, Meta Trusted Partner response-time failures, EU DSA Art 40 findings, TikTok Research API audit; (4) OpenAI/Anthropic external-labor→proprietary-system mechanism-isomorphism (red-teaming pay scales, Kenya annotator underpayment, Chatbot Arena "Leaderboard Illusion," low-resource-language data supply models, named resistance case "Pliny the Liberator," institutional critique); (5) a full deep-dive on the "rating = training data?" question, concluding operational-use ("比對基準/種子標註") is documented but literal supervised-training-label use is NOT, plus a detailed cross-org compensation-figure table (Meta ~$100M/115 countries self-claimed; Snopes/Lead Stories/FactCheck.org/Full Fact/TikTok-via-AFP-union figures) and Google/YouTube's different ClaimReview-based architecture (including its June 2025 rollback). | Q2 (core — the "1.8億則警示" figure cited in brief Existing knowledge §1 as one of three load-bearing anchors lives here), Q3, Q5, Q6 background | **This Segmenter pass sampled roughly lines 1-16 of ~29 total lines in this file — additional lane content beyond what is summarized here was not individually read.** The Drafter/operator should consult the file directly for the complete 40-claim inventory rather than relying solely on this summary. My own fresh c006 extract (Meta's *current*, 2025-26 transparency-page wording) independently corroborates this seed's "operational-use, not literal training-label" finding — two independent checks, same conclusion. |
| `agency-archive-tw.md` | Full Q5 leverage inventory (8 items) + per-org (TFC/MyGoPen/Cofacts) response detail + a flagged-gaps list | Q5 (core) | This Segmenter pass's c007/c026/c009/c016/c017/c022-c025/c027/c029 extracts materially extend several items this seed flagged as gaps: IFCN signatory list (was "unconfirmed" here, now resolved via c007), Cofacts licensing (was "cofacts.tw/about 403'd" here, now resolved via c026's GitHub-source route), TFC 2025/2026 donation figures (was "no 2025 figures published" here, now resolved via c016). |
| `karp-quotes.md` | 12 verified Karp quotes + 4 critical reviews + a synthesis on "performative virtue vs value extraction" | **Discourse chapter only (自成一節) — NOT any of Q1-Q6** | Per brief Existing knowledge §5: Karp is "話語標本... 不是證人"; confirmed **zero Taiwan/TSMC connection** across all 7 shareholder letters checked. Do not use Karp material to support any Taiwan-specific or say-do claim. |
| `funding-osf-state-google.md` | OSF/State Dept/Google.org/Ford/Luminate/NED grants to Taiwan orgs, with an explicit correction of an erroneous "$4M/$2.3M" AI-summarized figure (actual OSF total ~$1.34M) | Q6 (background only) | Cross-references c016/c017's OSF figures (TFC-specific); this seed's scope is broader (all Taiwan civil-society OSF/State grantees, not just TFC). D-inflation guardrail applies. |
| `funding-otf.md` | OTF (Open Technology Fund) support — ~$757,785 confirmed to OCF/Doublethink Lab/one fellow; explicitly finds **no OTF support to Cofacts or g0v** | Q6 (background only) | Useful negative: Cofacts' "open, forkable infrastructure" leverage narrative (Q5) is NOT funded by OTF — its resilience comes from its own MIT/CC-BY-SA licensing choice, not this funding stream. |
| `funding-ned-family.md` | NED + core institutes (NDI/IRI/CIPE/Solidarity Center) — finds NED's grantee-level database has been retired/anonymized since ~2015; only concretely-named Taiwan recipient is a Tibet-program grantee (not fact-checking-related) | Q6 (background only, one-line "上下游雙黑箱" context) | Explicitly NOT about fact-checking orgs — TFC/MyGoPen/Cofacts are not NED grantees per any record found. Do not conflate with the OSF/Google.org funding lines that ARE fact-checking-relevant. |

---

## Verification outcomes for the three task-priority items

### c007 (IFCN letter signatories) — RESOLVED
Raw-confirmed via Wayback (poynter.org itself 403s to live curl). **TFC and MyGoPen confirmed as Taiwan signatories** in the Jan-10, 2025 snapshot (~69 total org entries at that point). Cofacts confirmed absent. Summer Chen/FactLink not found in that specific snapshot but reconciled via cross-reference to seeds' own later-dated verification (finding ~125 signatures including her) — almost certainly explained by the letter's continuously-growing signatory list, not a factual conflict. See c007.md Passage 1b for full reconciliation.

### c026 (Cofacts licensing text) — RESOLVED, WITH A CORRECTION
The assumed recovery route (curl the confirmed Wayback HTML snapshot) **structurally cannot work** — confirmed via the snapshot's own embedded `__NEXT_DATA__.apolloState: {}`, proving the page is 100% client-side GraphQL-rendered and Wayback's plain-HTTP crawl only captured an empty shell. **Recovered instead via the page's actual Next.js source component** on GitHub (`cofacts/rumors-site/pages/about.js`), confirmed as the correct file via matching page titles. Found genuine "Free and Open" philosophy text and a 2023 NGO-incorporation detail — **but confirmed the CC BY-SA license text and an explicit "openness protects us" rationale sentence do NOT actually appear on the About page** (they live in a separate LEGAL.md document, already primary-verified in seeds). This corrects the original gap description's assumption about where that content lives.

### c006 (Meta mechanism wording) — RESOLVED
Live fetch and the most-recent (2026-03-06) Wayback snapshot both hit Meta's own intermittent SSR-failure mode (confirmed via an embedded `ssr_disabled_reason` marker — a Meta-side rendering flakiness, not a bot-block). Recovered via a working 2025-03-28 snapshot, **and independently cross-confirmed byte-for-byte against a second snapshot from 2026-01-03**, eight months apart — the load-bearing sentences are stable, current wording. All key sentences raw-verified, including the exact "same or almost exactly the same as that rated by fact checkers" line the brief flagged. **Confirmed zero occurrences of "train/training" in the mechanism text** (only as an unrelated cross-navigation link to a different Transparency Center page about generative-AI training-data disclosures) — directly supports the brief's 措辭地雷 rule against calling ratings "training data."

---

## Quotes downgraded or flagged after verification attempt

| Source | Original claim | Outcome |
|---|---|---|
| c007 | Summer Chen/FactLink individual signature | Not found in the specific snapshot I checked; **not a failure, reconciled** via cross-reference to seeds' later check — see above. |
| c019 | "Misinformation changes rapidly, much more quickly than moderators can annotate at scale..." | **Verification FAILED outright** — could not fetch this source via any of 4 attempted routes (DOI redirect target hit a Cloudflare JS-challenge; zero Wayback snapshots exist; Semantic Scholar lookup returned "not found"). Recommend the Drafter present the "label freshness / platforms take a snapshot not a sensor" claim as this research's own argument, per the brief's own contingency instruction, unless the operator independently re-fetches from a JS-capable environment. |
| c020 | "查核需要在地日常討論與新聞脈絡知識...自動化工具普遍不含在地知識" (Collector paraphrase, not a direct quote) | **Verification FAILED** — Cloudflare JS-challenge; Wayback's own crawler was refused (403) on all 4 attempts spanning 8 months. Thesis independently and successfully covered by c021 instead — no citation gap results. |
| c028 | "LINE×政府×民間查核公私協力生態的國際報導" (topic-level summary) | **Verification FAILED** for body content — confirmed paywalled both live and in the article's own publication-day Wayback capture. Only the one-line og:description confirmed. Substance independently covered by verified c003 (2019) and c024 (2026-era). |
| c022 | "'事實查核資料庫' 之機制描述" | **Confirmed as contamination, not merely unconfirmed** — a full-text search of the actual document found zero occurrences; Collector's own flagged suspicion (bleed-in from an unrelated Join-platform search result) is affirmed. Do not cite this phrase as appearing in 行政院打詐綱領2.0. |

## snippet_status for the 3 access-blocked records (Dr3)

| cid | access_status | snippet_status | Rationale |
|---|---|---|---|
| c019 | network_blocked (Cloudflare JS-challenge; no Wayback fallback) | usable, but capped — Dr3 [contested] tier only, with explicit "verification attempted and failed across 4 routes" annotation (stronger caveat than ordinary unverified) | The gate snippet is a substantive, specific, quotable claim naming a real mechanism (train/inference distribution shift) — meets the mechanical usable-bar — but this Segmenter pass actively disconfirmed reachability, which is a stronger signal than mere "not yet read." |
| c020 | network_blocked (Cloudflare JS-challenge; Wayback itself 403'd 4/4 times) | thin | Gate snippet is Collector's paraphrase, not a direct quote; no specific quotable sentence to anchor a citation; thesis fully covered by verified c021 instead — no reason for Drafter to lean on this record at all. |
| c028 | paywall (confirmed both live and same-day Wayback capture) | thin | Only the one-line og:description confirmed (itself thin, boilerplate-adjacent); substantive claims in the gate snippet unverified; topic fully covered by verified c003/c024. |

## Operator overrides needed
1. **c019** — if the label-freshness academic claim needs to stay peer-reviewed-sourced (rather than self-labeled as this research's own argument), retry `direct.mit.edu/coli/article/52/2/619/134523/...` from a JS-capable browser session or institutional-library proxy.
2. **c020** — lower priority than c019 given c021 already independently covers the same thesis with a verified quote; only worth pursuing if the Drafter specifically wants a second peer-reviewed citation.
3. **c028** — lowest priority; would only add an "international press, US-policy-comparison" framing angle that is not otherwise represented in this evidence base, but the underlying LINE-coalition facts are already well-covered by c003/c024.
4. **Summer Chen/FactLink** — if this specific individual-signatory fact becomes load-bearing in the draft (e.g., named alongside TFC/MyGoPen as a third Taiwan-linked signatory), the operator may want a fresh raw-curl of the *current* live poynter.org letter page (or a mid/late-2025 Wayback snapshot) to independently corroborate seeds' own finding, since this Segmenter pass did not do that specific re-check itself.
5. **extraction-audit-journal.jsonl full read** — this Segmenter pass sampled roughly the first 55% of this 29-line file (5 of what the brief calls "五路" adversarial lanes, plus part of a 6th verdicts lane). If the Drafter needs the complete 40-claim inventory (e.g., additional named compensation figures, additional鋼人 concessions, or content in the unsampled remainder), read the file directly rather than relying solely on this INDEX's summary.
