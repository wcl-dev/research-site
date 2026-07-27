# Collection coverage — ai-assistant-disclosure-tw

Candidates: 60 (after URL-dedup from 82 raw hand-curated + Track-1 picks) | Tracks run: T1 (academic, 25 queries) / T3 (WebFetch + WebSearch, seek_direct + supplementary) / T4-MCP (taiwan-legal-db, auto-probe)

Track 2 (curated RSS) skipped — no `sources.yaml` exists for this project (consistent with the sibling `llm-user-side-bias` precedent; this project also has no Interviewer-produced `sources.yaml`, only `brief_expanded.yaml`). Track 4 (twinkle-hub open-data MCP) was not available this session — its tools were not present in this agent's tool allowlist, unlike `taiwan-legal-db` which was. Flagged per Co6/MCP-instructions rather than silently skipped.

## Concept (brief_expanded concept_ontology) × count

| Concept | Label | Candidates |
|---|---|---|
| P | 問題基礎（已證，引用不重驗）| 7 |
| T | 供給側可讀性技術棧 (Q2) | 10 |
| F | 案例B：公民查核可讀化 (Q3) | 7 |
| D | 案例C：對話式供應 (Q4) | 11 |
| S | opt-out vs opt-in (Q5) | 5 |
| G | 治理真空 (Q6) | 17 |
| M | 量測方法 (Q7) | 3 |

## Brief question (Q1–Q7) × candidate tag count

(Some candidates carry two Q-tags where they support both a case cluster and its cross-cutting question; counted once per tag.)

| Q | Topic | Count |
|---|---|---|
| Q1 | 問題陳述整合 / grooming vs data-void | 7 |
| Q2 | 技術棧 (T) | 12 |
| Q3 | 案例B Cofacts/TFC/MyGoPen (F) | 12 |
| Q4 | 案例C 對話式供應 (D) | 11 |
| Q5 | opt-out vs opt-in (S) | 7 |
| Q6 | 治理真空 (G) | 18 |
| Q7 | playbook / 量測 (M) | 5 |

## Language

| Language | count (rough) | note |
|----------|-------|------|
| en | ~54 | includes EU/US/Ukraine comparators, academic literature, GEO/citation-pattern industry material |
| zh-TW | ~6 primary-source records (moda ×2, 全國法規資料庫, 遠見雜誌, NSTC, MyGoPen) | **C5 gap expected**: Track 1 (OpenAlex/Semantic Scholar) returns ~zero zh-TW-native scholarship for zh-TW queries (人工智慧基本法, 台灣事實查核中心 both run as English-translated variants per C5 protocol — see below). zh-TW coverage instead carries through Track 3 direct fetches of moda/NSTC/law.moj.gov.tw/MyGoPen and one MCP statute lookup, not through academic indices. |

Per C5 protocol, the two zh-TW queries in `brief_expanded.yaml` (`台灣事實查核中心 ClaimReview 結構化 開放資料`, `台灣 人工智慧基本法 生成式AI 標示 moda 風險分級 2026`) were run through Track 1 as their English-translated equivalents (`Taiwan FactCheck Center ClaimReview structured open data`, `Taiwan Artificial Intelligence Basic Act generative AI labeling`) — both returned low/no directly-relevant hits, consistent with the expected coverage gap, not evidence of no scholarship. zh-TW-native Cofacts scholarship in fact DOES exist in English-language venues (Internet Policy Review, Journal of Modern Craft [Checking Facts by a Bot]) and was captured that way.

## Blind spots (zero / near-zero cells)

- **M (measurement methods) = 3 candidates, thinnest cluster.** This is partly structural: rigorous LLM-citation-audit / political-bias-asymmetry-measurement methodology papers are a very young academic niche (the two strongest hits are both 2026 preprints). The operator's planned §待決事項 1(b) probe protocol — not yet executed, gated behind operator sign-off per the brief's 閘1/閘2 process — will itself become the primary M-cluster evidence once run; this Collector pass could only gather *methodological precedent* for designing that probe, not the probe's own results. Not a collection miss; a designed-in dependency on a later pipeline stage.
- **S (opt-out vs opt-in) = 5 candidates.** Academic literature on the *media* opt-out/opt-in dilemma specifically (vs. general "AI harms journalism" literature) is thin — most of what exists is trade press (Reuters Institute, TechCrunch, Digiday) rather than peer-reviewed work, because the CMA opt-out mechanism and Google's licensing-vs-training-rights bundling are 2026 developments too recent for the peer-review cycle. Trade-press sourcing here is a deliberate substitution, not an oversight — flagged so Gatekeeper doesn't penalize the news-heavy source mix as low-rigor without this context.
- **F (Cofacts/TFC/MyGoPen) — TFC (Taiwan FactCheck Center) itself returned 403 on direct WebFetch**, and no ClaimReview/API evidence could be independently confirmed or denied for TFC beyond its homepage's absence of visible developer-facing links (see c-records for tfc-taiwan.org.tw and cofacts.tw, both flagged `access_status`). This is a genuine gap for Q3 the Segmenter/Drafter should flag rather than assume either way — recommend a second-route check (e.g. Google cache, IFCN's own TFC profile page) before drafting asserts TFC's ClaimReview status.
- **P (anchor sources)** — Nature 655 (Waight et al.) is paywalled; full-text access mediated only through the companion GitHub site (`state-media-influence-llm.github.io`), which is comprehensive enough to cite confidently, but any operator wanting to quote exact Nature wording verbatim will need institutional access.
- **D (DebunkBot) — integrity caveat**: the flagship Costello/Pennycook/Rand Science 2024 paper carries an Editorial Expression of Concern (data/screening-criteria inconsistencies), captured as two dedicated candidate records (EoC notice + Retraction Watch coverage) so this doesn't get silently dropped when Segmenter/Drafter cite the 20%-belief-reduction headline figure. Authors' corrected-pipeline reproduction and the 2026 Newcomb Cleveland Prize are also captured — net effect is "cite with an integrity footnote," not "downgrade or drop."

## Track notes

- Track 1 (`search_academic.py`): 25 queries run, 374 raw records before curation; Semantic Scholar rate-limited (HTTP 429) on ~22/25 queries mid-run (OpenAlex unaffected) — see per-query `.err` logs (removed in cleanup, counts preserved here). Heavy manual curation was required: most raw OpenAlex hits for broad queries (T/S/G especially) were generic healthcare/education-GenAI noise unrelated to this brief; 27 of 374 raw records were judged genuinely on-topic and retained.
- Track 3: seek_direct URLs from `brief_expanded.yaml` fetched first (priority). 4 of 11 seek_direct URLs hit access barriers: Nature (paywall/cookie-redirect loop), Science.org DebunkBot DOI (403), cofacts.tw (403) — each has a companion/alternate-route record substituted (GitHub for Cofacts, PubMed+PNAS-Nexus follow-up for DebunkBot, companion GitHub site for Nature). WebSearch supplemented for topics without a single canonical URL (GEO citation-pattern studies, C2PA adoption status, EU DSA/AI-Act code of practice details).
- Track 4 (MCP): `taiwan-legal-db.search_regulations` confirmed 人工智慧基本法 as 現行法規 (pcode H0160093) — used to source the primary statute-text candidate. `search_interpretations` probed for 言論自由+人工智慧 constitutional interpretations — 0 hits (expected; topic too recent for 釋字/憲判字). `twinkle-hub` (data.gov.tw open-data MCP) was **not available** in this session's tool allowlist — could not run the Co6 auto-probe for Taiwan open-data portals; flagged in handoff `notes` for operator to enable next run if government-open-data-portal-level Q6 evidence is wanted.
