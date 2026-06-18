# Collection coverage — ai-cognitive-infrastructure-tw

Candidates: 44  |  Tracks run: T1 (academic), T3 (web + primary dashboards). T2/T4 skipped (no sources.yaml; non-TW-law/data brief, MCP auto-probe not warranted).

This brief is an EVIDENCE AUDIT of a 4-link causal chain. Cells below = candidate count by chain LINK (not by brief-Q index), since the audit is organized link-by-link.

## Chain link × track  (cell = candidate count)

| Link | T1 academic | T3 web/primary | repo-internal | total |
|------|-------------|----------------|---------------|-------|
| L1 price->adoption        | 2 | 4 (3 primary-data snapshot) | 0 | 6 |
| L2 AI-as-entry            | 0 ⚠ | 3 | 0 | 3 |
| L3 stable framing         | 4 | 2 | 1 (PRIMARY) | 7 |
| L4a homogenization        | 6 | 2 (disconfirming) | 0 | 8 |
| L4b individual belief shift | 7 | 2 | 0 | 9 |
| L4c societal aggregation  | 2 | 1 (analogy) | 0 | 3 |
| Frameworks                | 4 | 1 | 0 | 5 |
| Counter-evidence §6       | 3 | 0 | 0 | 3 |

## Language

| Language | count | note |
|----------|-------|------|
| EN | 43 | all academic + web sources English |
| zh-TW | 1 | repo-internal llm-user-side-bias (c001). C5: T1 returns ~0 zh-TW academic on this topic; the empirical zh-TW base IS the repo's own work, cited as primary. Expected gap, not a miss. |

## Blind spots (every zero / near-zero cell)
- **L2 × T1 academic: 0** — search-behavior/zero-click empirics live in industry reports (Reuters Institute, Chartbeat) not peer-reviewed venues yet. Expected gap; T3 carries L2 well (Reuters DNR 2025 separates chat-LLM 7% vs AI-Overviews 4% — exactly the brief's guard). Not a miss.
- **L4c: 3, all indirect** — DELIBERATE finding, not a miss. Direct population-scale empirics linking one model's framing to societal cognition do NOT exist. What exists: a SIMULATION (LLM agents, c032), a population framework (social cybersecurity, c031), and an ANALOGY (social-media agenda-setting, c033, labelled analogy-only). This emptiness is itself the key L4c result — the chain most likely breaks here.
- **L4b human-subject: NOT empty (9 records)** — contrary to the brief's "expect thin", rigorous pre/post human-subject persuasion RCTs DO exist (Costello/Pennycook/Rand Science 2024 N=2,190 durable 2-mo; Salvi Nat Hum Behav 2025; Argyle PNAS 2025; Chen/Kalla/Le N=10,417; Shu/Karell 2026 latent historical-narrative framing; Hackenburg PNAS 2025 bounding). KEY NUANCE for Drafter: these prove generic LLM persuasion CAPABILITY exists and is bounded — they do NOT show a single DOMINANT model's framing producing population-scale shift (that is L4c, still empty). The L3->L4b link is supported; the L4b->L4c link is where it breaks.
- **GitHub SDK star/dependency signal: not fetched as primary** — HF downloads + OpenRouter token-share cover open-weight adoption adequately this run. Flagged in handoff wanted_sources.
