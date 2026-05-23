# Collection coverage — scam-fake-website-tw

Candidates: 63  |  Tracks run: T1 (academic), T2 (curated), T3 (web), T4 (MCP: taiwan-legal-db + twinkle-hub)

Track 4 is the spine of this brief — the proxy denominators the operator named
(165 dashboard scam-type breakdown, RPZ blocking volume, moda takedown counts,
Whoscall malicious-link composition) all live in government open data, court
findings, or industry reports, not academic literature.

## Brief question × track  (cell = candidate count; a record can serve >1 Q)

| Brief Q | T1 academic | T2 curated | T3 web | T4 MCP | total |
|---------|-------------|------------|--------|--------|-------|
| Q1 (佔比方法論／多分母) | 4 | 0 | 3 | 3 | 10 |
| Q2 (A — 冒名型) | 7 | 5 | 1 | 4 | 17 |
| Q3 (B — 非冒名型) | 5 | 1 | 0 | 4 | 10 |
| Q4 (媒介角色／生命週期) | 5 | 1 | 1 | 1 | 8 |
| Q5 (攔阻成效 supply-side) | 1 | 3 | 3 | 2 | 9 |
| Q6 (2023–2026 趨勢) | 2 | 0 | 1 | 1 | 4 |
| Q7 (資料缺口／替代估計) | 1 | 1 | 0 | 2 | 4 |

(Counts assign each candidate to its primary Q tag in `why_relevant`; secondary
coverage is broader — e.g. the 165 dashboard c046 touches Q1 and the C-axis,
the moda 3.0 release c041 touches Q5 and Q6.)

## Language

| Language | count | note |
|----------|-------|------|
| zh-TW    | 42    | T2/T3/T4 carry the topic; all proxy-denominator primary docs are zh-TW |
| EN       | 21    | C5: all Track 1 academic — zh-TW academic queries returned 0 (see blind spots) |

## Track budget actually used (Co2 — fidelity:high, horizon:current)

- Track 1: 5 EN queries × `--limit 15` (halved per Co2). 78 raw → 71 unique by
  URL → 21 retained after relevance selection (dropped clearly off-topic 6G /
  metaverse / IoT / financial-literacy papers — not quality filtering, these are
  different topics that the broad phishing-detection queries dragged in).
- Track 2: 17 curated `scrape` placeholders emitted → all resolved (WebFetched or
  superseded by a more specific URL) → 0 `[TODO scrape]` records remain. Several
  curated pages were JS-only or 403; resolved via alternate URLs / secondary
  citation (fetch_fallback: secondary_citation_acceptable honored).
- Track 3: doubled per Co2 — ~18 WebFetch calls; surfaced the TWNIC 2025
  transparency report (c037, primary), CNA moda figures (c040), NPA statistical
  bulletins (c043–c045).
- Track 4 MCP: taiwan-legal-db → 7 judgments + 1 statute; twinkle-hub → 8
  datasets. 16 candidates total, well under the 25/portal cap.

## A∪B note (Co1 — NOT conjunctive-filtered)

`research_focus = A∪B` is a UNION: A (impersonation) and B (purpose-built) are
mutually exclusive and jointly the target universe. The Co1 cross-product /
conjunctive filter applies to `∩` briefs, where it tightens noise. Here a
conjunctive A-AND-B filter would WRONGLY drop A-only and B-only records — both
are in scope. Queries were left OR-shaped; concept_target tags (A=30, B=12,
none=21) preserve the A/B split the Drafter must report separately.

## Blind spots (every zero / near-zero cell)

- **Q1–Q7 × T1, zh-TW: 0** — expected C5 coverage gap. zh-TW academic queries on
  search_academic.py return 0 (OpenAlex/S2 index Traditional-Chinese scholarship
  weakly). EN-translated variants were run instead and carry T1. NOT a collection
  miss — but the Gatekeeper/Drafter must read T1 as *comparable-context* phishing
  scholarship (international), never as Taiwan empirics. Q7 explicitly asks
  whether 學界/調查局 have Taiwan quantitative studies — that gap is itself a
  finding, not a failure to collect.
- **Q1 × T2: 0** — curated sources are agency/industry portals, not methodology
  essays; the "why no single number" methodology argument is carried by T1
  (c001, c009) + T3/T4 showing the C-axis classification mismatch (c025, c046).
  Expected, not a miss.
- **Q3 × T3: 0** — no general-web record tagged B-primary. B coverage is strong
  via T1 (c004 SCAMMAGNIFIER, c008, c012, c014, c020) + T4 (datasets 160055/
  165027, judgments c030/c032/c033). Acceptable.
- **Q6 (趨勢): 4 total — thinnest cell.** 2023–2026 trend evidence is partly
  embedded in longitudinal datasets (RPZ 2021→2025 in c037/c039; dataset 165027
  carries creation dates 2023+; 160055 has weekly series) rather than dedicated
  "trend" records. Gatekeeper should note the Segmenter will need to derive the
  trend line from the dated rows inside c022/c024/c037, not expect a ready-made
  trend report. A targeted retry for a moda/NPA year-over-year comparison would
  strengthen this — flagged for operator.
- **Q7 (資料缺口): 4 total — also thin, but partly intrinsic.** The data-gap
  question is answered by *demonstrating* the gap (165 has no medium-cross-tab —
  shown by c025/c046; 調查局 quantitative data sparse — c060/c062). Few records
  *directly* propose alternative estimators; c021 (academic) and c027 (Chiayi
  channel-dimension dataset) are the closest. Expected — the gap is the finding.

## Access-flagged records (Gatekeeper / Segmenter input)

- `js_only` (3): c038 RPZ governance portal, c046 165 dashboard, c047 Whoscall
  blog — JS SPAs; metadata + secondary citations supplied. Segmenter routes via
  snippet layer or the open-data equivalent (c022/c024 replace c046's data).
- `403` (4): c042 fraudbuster stats page, c049 Trend Micro threat-report page,
  c050/c051 DTA reports (iThome host). Anti-bot blocks; accepted on metadata +
  secondary citation per sources.yaml `fetch_fallback: secondary_citation_acceptable`.
  c040/c048/c063 are clean secondary citations that recover the same figures.
