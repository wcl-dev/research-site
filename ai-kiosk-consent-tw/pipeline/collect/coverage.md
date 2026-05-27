# Collection coverage — ai-kiosk-consent-tw

Candidates: 107  |  Tracks run: T1 (academic) + T3 (web) + T4 (MCP: taiwan-legal-db + twinkle-hub)
Note: T2 RSS produced 0 substantive records — all 19 entries in `sources.yaml` were scrape-todo placeholders that needed Track 3 URL-level expansion; resolved by replacing each placeholder with one-or-more concrete URLs (PDPC/cpc.ey/wixtar/lebledor/mcs etc.) instead of a single index page.

## Brief question × track  (cell = candidate count)

| Brief Q                                        | T1 academic | T2 curated | T3 web | T4 MCP | total |
|------------------------------------------------|-------------|------------|--------|--------|-------|
| Q1a [A deployment 測繪]                        | 0 ⚠         | 0          | 4      | 0      | 4     |
| Q1b [A 雙月 + 金色三麥 showcase]               | 0           | 0          | 11     | 0      | 11    |
| Q2 [告知層]                                    | 0           | 0          | 3      | 1      | 4     |
| Q3 [選擇/退出層]                               | 0           | 0          | 0 ⚠    | 0 ⚠    | 0 ⚠   |
| Q4 [法律 framing 拆解 — 個資法/PDPC]           | 0 ⚠         | 0          | 13     | 11     | 24    |
| Q5 [國際對照 — GDPR/AI Act/BIPA/CCPA/PDPA]     | 31          | 0          | 14     | 3      | 48    |
| Q6 [執法/申訴實況]                             | 0           | 0          | 8      | 5      | 13    |
| Q7 [業者實體 — wording 落差]                   | 0           | 0          | 3      | 0      | 3     |
| (背景 / 不直接對應單一 Q)                       | 0           | 0          | 0      | 0      | 0     |

Notes on assignment:
- Q5 dominates the T1 row because Track 1 academic queries were intentionally EN-shaped per C5 (zh-TW CJK gap) and Co2 (`high/current` halving). The 31 kept records are international peer-reviewed framing material that the Drafter uses as **comparative anchor**, not as Taiwan-specific evidence.
- Many candidates double-count across Q4 (legal framing) and Q5 (international) — assigned to the dominant Q in this matrix.
- Q1b is well-served (11 records on two showcase brands). Q1a (broad A 部署測繪) is thinner — only 4 explicit pan-vendor records (Partner Tech / Berry AI / 頂呱呱 / TAHR-historical-retail-FR-2014) carry the deployment-breadth load. Drafter may need to deepen at insight stage with structured vendor lookup.

## Language

| Language | count | note |
|----------|-------|------|
| EN       | 38    | Track 1 academic (31) + EU AI Act / EDPB / BIPA / CCPA / Singapore PDPC primary docs (7) |
| zh-TW    | 69    | T3 (45) + T4 (20) + a few EN/zh-TW law firm bilingual newsletters classified as zh-TW |

C5 zh-TW academic gap: as expected, OpenAlex + Semantic Scholar returned ZERO Taiwan-specific zh-TW empirical research on AI Kiosk demographic inference. EN-shaped queries via Co2 budget yielded 31 records — international framing only. **Taiwan-specific empirical scholarship on this exact topic appears not to exist in indexed databases**; T3 (news media + legal blogs) and T4 (PDPC / 法務部 / 司法院) carry the Taiwan empirical weight. This is a structural gap, not a coverage miss.

## Blind spots (every zero / near-zero cell)

- **Q3 × ALL tracks (0 hits)** ⚠ — `選擇/退出層` (人工替代是否可用、退出成本) returned zero direct hits. **This is itself a finding**: no vendor / regulator / news / academic source talks about the opt-out mechanism for kiosk demographic inference in TW. The absence supports the brief's premise that `D selection axis` is structurally empty. Drafter should **report the gap as a finding**, not as a missing source set. Operator may consider scoping a §6c follow-up probe (e.g. "consumer wait staff fallback request" + brand-by-brand) at insight stage.
- **Q1a × T1 (0 hits)** ⚠ — no peer-reviewed Taiwan deployment census; expected per C5. T3+T4 carry it (TAHR historical retail FR + Partner Tech market share + MCS smart cabinet) but the count is thin. If Gatekeeper accepts, Drafter should be cautious about absolute deployment counts.
- **Q4 × T1 (0 hits)** ⚠ — no peer-reviewed academic source on TW PDPA Art.6 + biometric grey zone. Expected per C5; T3 (15 律所/憲政分析 records) + T4 (個資法本文/施行細則/釋字603/111憲判13) more than cover.
- **Q1b × T1/T4 (0)** — case-study showcase relies on news + vendor pages (T3); appropriate match between question type and source type.
- **Q2 × T1 (0)** —告知層 implementation is fact-specific, not academic. Carried by T3 (Co5 head-fetched WiXtar/CIO/CyberLink + 律所 framing analysis) + 1 T4 (PDPC §8 函釋).
- **Q7 × T1/T2/T4 (0)** — vendor-level wording analysis is intrinsically primary-source / news-driven; appropriate that T3 carries it. May need additional vendor privacy-policy direct fetches at Segmenter stage (e.g. 金色三麥 / WiXtar / Berry AI 隱私政策 page fetch).

## Co5 access-status flags (PDPC js_only)

4 PDPC `News_Content` pages returned JS-shell HTML on WebFetch:
- c050 第6條 行政函釋
- c051 第2條 行政函釋
- c052 第8條 行政函釋
- c056 修正案 2025/11/11 官方公告

These are the **official PDPC** primary docs for Q4. Segmenter should route via Dr3 snippet-layer (use the matching summaries from the parallel 法律百科 / 律所 newsletters c044-c049 as evidence; or operator may fetch via a non-CC environment).

## Co1 / Co2 / Co6 actuals

- Co1 (conjunctive A∩D for T1): raw 66 → kept 31 (47% retention). Filter struck a reasonable balance — too tight would have dropped useful methodology records on retail/biometric privacy (no consent-keyword tie-in); too loose would have flooded Gatekeeper.
- Co2 (high/current budget): T1 halved to 5 queries × `--limit 15` (vs default 19 × 25 = 475 raw); T3 doubled in practice via 15 WebSearches + 4 Co5 head-fetches. Per the audit rule, this allocation matched the brief's `high/current` cell expectation.
- Co6 (Taiwan auto-probe): twinkle-hub opendata probed (10 datasets kept); taiwan-legal-db probed (10 records kept incl. interpretations). Both productive; not skipped. `mcp_autoprobe: twinkle-hub +10, taiwan-legal-db +10`.
