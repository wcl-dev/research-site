# Collection coverage — io-outsourcing-tw

Candidates: 49 | Tracks run: T1 (academic, OpenAlex+S2), T3 (WebSearch+WebFetch incl. two pdftotext deep-extractions), T4 (MCP, taiwan-legal-db probe — 0 relevant hits, see below). **Track 2 skipped** — no `sources.yaml` exists for this project (same as sibling `geo-public-good-tw`/`llm-user-side-bias` when curated feeds aren't configured).

## Brief question × track (cell = candidate count)

| Brief Q | T1 academic | T3 web/PDF | T4 MCP | total | note |
|---|---|---|---|---|---|
| Q1 (責任稀釋架構) | 8 | 7 | 0 | 15 | strongest-covered cluster; theory anchors (Callon/Nadler/Lazar) + proxy-warfare/attribution-law lit + Cambridge Elements counter-framing |
| Q2 (外包棧分層) | 2 | 5 | 0 | 7 | NSB spine doc (full text via pdftotext) + IRSEM Baybridge (full text) cross-validate against 2 independent networks (Haixun/Haimai) |
| Q3 (買方類型學) | 0 ⚠ | 4 | 0 | 4 | see blind-spot note — expected C5 gap, not a miss |
| Q4 (賣方集團還原) | 0 ⚠ | 5 | 0 | 5 | 王宏恩/林雨蒼/CNA relay chain + IRSEM's independent 3rd network |
| Q5 (兩種能力持有型態) | 1 | 3 | 0 | 4 | thin — DTL anchor already in brief_expanded, Collector supplied ad-market-scale context (NBER, NewsGuard) not PRC-specific op evidence |
| Q6 (外包比較優勢) | 2 | 4 | 0 | 6 | ASPI overt-shift, Graphika deepfake, Recorded Future 2020 baseline give some TTP-iteration evidence, but productization (GoLaxy/GoPro) still outweighs innovation-speed evidence |
| Q7 (民主國家意涵) | 2 | 1 | 0 | 3 | thinnest cluster — ads.txt/sellers.json standard found, but governance-lever literature is light |
| surveillance-capped (一段話) | 0 | 4 | 0 | 4 | ADLINK/Geedge (InterSecLab MADLink + New Bloom) + ASPI "party's AI" (403) — deliberately capped, not under-collected |

Totals sum to 48 tagged + 1 "other" (an Oxford OII report tagged loosely to Q6 professionalization, counted separately in the raw file).

## Language

| Language (by candidate title script) | count | note |
|---|---|---|
| EN | 43 | includes DOI-indexed academic literature (Track 1) and most think-tank/gov reports |
| zh (TW/CN) | 6 | NSB PDF, 王宏恩 column, 林雨蒼/epochtimes relay, DSET (403), CNA, GoPro/RTI relay |

**C5 confirmed as predicted**: all CJK-language Track 1 queries (S and B clusters) returned near-zero relevant hits — see raw files `collect/tmp/t1_19..24_*_cjk.jsonl` before cleanup (noise: unrelated Chinese-language OpenAlex records on e-commerce livestreaming, TB drug resistance, etc.). This is the expected OpenAlex/Semantic-Scholar zh-TW/zh-CN coverage gap, not evidence that no scholarship exists. Track 3 (WebSearch on Taiwanese news/think-tank sites) carried the load for Q3/Q4 instead, consistent with the C5 workaround protocol.

**Provider failures**: Semantic Scholar returned HTTP 429/500 on the large majority of Track 1 queries this session (OpenAlex was unaffected and supplied ~all Track 1 results). Track 1 numbers above should be read as "OpenAlex-only" coverage.

## Track 4 (MCP) auto-probe

Per Co6, ran a light `taiwan-legal-db` probe (`search_regulations`) for `認知作戰` and `境外勢力影響透明法` since the brief is Taiwan-scoped. **0 hits both queries** — Taiwan has no dedicated cognitive-warfare or foreign-influence-transparency statute, consistent with the brief's own framing (this is a policy gap, not a search failure). Did not expand the probe further: `taiwan_domestic_excluded` hard_rule means TW statutory reform is out of scope for this brief regardless, so a deeper legal-db dig would have produced material the brief cannot use. `twinkle-hub` (open-data portal) tools were not available this session — not probed, noted here rather than silently skipped.

## Blind spots (every zero / near-zero cell)

- **Q3 × T1 = 0**: Expected C5 gap (see above). Buy-side evidence instead comes entirely from Track 3: ChinaFile (Message Control + Methodology + Key Takeaways + 1 primary-source procurement notice) and the newly-surfaced Cambridge Elements academic monograph (Ong/Nie/Lee, 2026) which independently re-ran a similar 3,000+-notice procurement analysis. **This monograph is a genuine collection win, not a gap** — but flagged below as argumentatively load-bearing in the opposite direction from the brief's thesis.
- **Q4 × T1 = 0**: Same C5 gap — no academic-database coverage of the specific Yishan/Borderless/Laixiu corporate chains exists (these are investigative-journalism/think-tank discoveries, not yet in the peer-reviewed literature). IRSEM's Haixun/Haimai reconstruction is the one Q4-relevant item that IS a rigorous methodology (OSINT + Chinese corporate registries) even though it isn't in an academic index.
- **Q5 is thin (4 total, only 1 from T1)**: The brief's own `anchor_dtl_borderless` and `anchor_internal_fimi` already carry most of the Q5 evidentiary weight and are **established, not to be re-collected** per hard_rule `internal_reports_are_established`. What the Collector could add is generic ad-market-subsidizes-misinformation context (NBER Ahmad et al., NewsGuard/Comscore) — useful as background magnitude but NOT PRC-specific, so it cannot by itself thicken the 徵用型/專營型 case comparison. **This is a structural ceiling, not a search failure**: the two-case comparison is inherently n=2 by the brief's own design, and no amount of Track 3 search turns up a third fully-documented ad-funded PRC-linked case.
- **Q7 is thinnest (3 total)**: found the核心 IAB ads.txt/sellers.json technical standard directly, but broader "how do you operationalize a supply-chain-completeness governance strategy" literature (platform account-provenance transparency specifically, labor-market/gig-platform whistleblowing channels) came up sparse in Track 3. **Worth a second collection pass** if Q7 becomes a load-bearing section rather than a closing gesture — try queries anchored on specific existing regimes (EU DSA Art. 40 researcher-data-access, Meta Ad Library, X's now-defunct ads transparency) rather than generic "platform governance" terms.
- **Surveillance-capped cluster (4 items, by design)**: NOT under-collected — hard_rule `surveillance_capped` limits this to one paragraph, so 4 candidates (InterSecLab Internet Coup + MADLink, New Bloom, ASPI "party's AI") is already more than needed. Flagged here only so the operator can confirm this wasn't accidentally starved.

## Fetch failures / access-blocked (honest accounting)

| Source | Status | What was tried | Substitute used |
|---|---|---|---|
| DSET 靠北系列粉專報告 (dset.tw/media-report/359/) | `403` | Direct WebFetch, twice-checked | epochtimes secondary relay of the same findings (flagged as second-hand, not equivalent) |
| ASPI "The party's AI" (aspi.org.au) | `403` | Direct WebFetch | WebSearch snippet only — candidate record notes the gap explicitly |
| EEAS 3rd FIMI Threat Report direct PDF | tool limit (>10MB) | WebFetch on the PDF URL | EEAS landing/summary page substituted; **Segmenter should retry the PDF with a tool that isn't capped at 10MB** — URL is in the candidate record |
| ChinaFile Primary Source PDF (court procurement notice) | metadata-only | WebFetch returned page chrome, not embedded PDF body | WebSearch snippet confirms the 10,000/20,000-account figures; record kept as `primary_doc` with the caveat noted in its `abstract_or_snippet` |
| RTI original reporting on GoLaxy (pid=207050 "四類台灣人") | not fetched | Time-budget triage — GoPro/311基地 detail was already captured via a second RTI URL (pid=211949) | none needed; noted for completeness |
| 中科天璣 GoLaxy GoPro product catalog | never located directly | Multiple WebSearches | Only secondary (RTI) reporting found; Vanderbilt's own primary-document archive is the correct place to verify GoPro-branding directly — flagged for Segmenter to check inside the 400-page document archive rather than the landing page |

## Notable un-planned finding (flag for Gatekeeper/Drafter)

**Ong, Nie & Lee, "Outsourcing Surveillance: Online Opinion Management in China" (Cambridge Elements, 2026)** — an independently-assembled ~3,000-procurement-document dataset that reaches a **different conclusion than this brief's Q1 thesis**: it argues outsourcing serves state-capacity augmentation, not primarily plausible-deniability. This surfaced only through a generic Track 3 WebSearch (not anticipated by `brief_expanded.yaml`'s query list) and is exactly the kind of counter-framing evidence the brief's own rigor standard should welcome rather than omit. Recommend the Gatekeeper accept it and route it to the Drafter as a dialogue partner for Q1, not a rejection candidate — declining to engage with it would look like cherry-picking.

## Query budget used

Track 1: ran all 22 `brief_expanded.yaml` queries (18 EN + 4 CJK) plus the 2 extra CJK variants for S/B clusters explicitly called out in the brief_expanded query list = 24 total academic queries. No Co2 budget-halving applied (`brief_type.horizon: established_pattern_underframed` does not map cleanly onto the Co2 matrix's `current`/`emerging`/`retrospective` categories, and no `review.fidelity_level` field was set in `brief_expanded.yaml`, so default full-budget behavior was used).

Track 3: not query-counted in the same way — used a mix of the seek_direct/must_include direct-fetch list (5+9 URLs) and ~20 follow-on WebSearches chasing specific named entities (王宏恩, 林雨蒼, ChinaFile sub-pages, IRSEM, InterSecLab MADLink, Vanderbilt, ASPI, Cambridge Elements, NBER, etc.) surfaced by the must_include list and the operator's explicit S-cluster lead.
