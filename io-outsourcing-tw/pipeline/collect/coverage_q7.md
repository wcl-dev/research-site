# Collection coverage — io-outsourcing-tw, Round 2 (Q7 only)

Round 1 baseline: 49 candidates (c001–c049), see `coverage.md`.
Round 2 adds: 17 candidates (c050–c066), all tagged G/Q7. Total after this round: 66.

Tracks run: T3 (WebSearch + WebFetch) only, plus targeted `curl -sL | pdftotext -layout` deep extraction
for 5 PDFs that WebFetch cannot handle cleanly (binary/oversized). No T1 (search_academic.py) run this
round — Q7's target material (EU government/think-tank primary docs, DSA regulatory reporting) is
structurally outside OpenAlex/Semantic Scholar's coverage; the two peer-reviewed hits this round (c063
Science, c064 IEEE S&P, c066 USENIX) were found via WebSearch, not Track 1. No T2 (sources.yaml) —
project has no sources.yaml. No T4 — not applicable to this round's targets.

## Priority target × outcome

| # | Target (per operator brief) | Outcome | Candidates |
|---|---|---|---|
| 1 | IMS primary docs (definition, 3-layer model, attribution_threshold, intermediary mapping) | **Hit — and corrected two claims** | c050 (VIGINUM technical report, TLP:CLEAR, full text), c051 (EU DisinfoLab working-group restatement) |
| 2 | EEAS FIMI reports 1st/2nd/3rd, full text incl. 3rd via curl+pdftotext | **Hit — all three, 3rd report full text obtained** | c052, c053, c054 |
| 3 | Named institutions not platitudes: DSA Art.40, Ad Library/Commercial Content Library, ads.txt/sellers.json enforcement gap, account provenance | **Hit — enforcement-gap literature, not just specs** | c058, c059, c060, c061, c062 (DSA Art.40); c064, c065 (ads.txt/sellers.json enforcement); c063, c066 (account provenance/marketplace) |
| 4 | Attribution thresholds & sanctions — actors staying below threshold | **Hit — precedent + concrete case** | c057 (NATO/Hybrid CoE attribution confidence-levels literature), c055 (Doppelganger cost-effectiveness — direct-actor sanctions insufficient), c056 (Aeza — literal below-threshold jurisdictional gap case) |
| 5 | Labor market: 晴數智慧/科大訊飛 Taiwan job-site accent-recording claim | **Traced to source, NOT independently corroborated** | none new — see below |

## Priority 5 in detail (honest reporting per operator instruction)

The claim traces to the NSB report itself, already collected as **c010** in round 1 (verified again this
round via a fresh `curl+pdftotext` of the same PDF — the sentence is on page ~4: 中共另委託「晴數智慧科技」、
「科大訊飛」等科技公司，開發智能語音系統，並於我國徵才網站刊登廣告，誘吸不知情臺灣民眾，以國、臺、客語進行
線上錄音，建立臺灣口音資料庫). Extensive WebSearch in both Chinese and English (job-posting terms,
crowdsourced-voice-data terms, "情蒐"/intelligence-gathering framings, direct company names) found **zero
independent media or research corroboration** of this specific claim. It appears to be **single-sourced to
NSB**, not picked up by any Taiwanese investigative outlet or international researcher as its own story.
This is a materially different evidentiary status than c010's other claims (which cross-corroborate against
DTL/ChinaFile/Vanderbilt in round 1) and should be flagged as such if used in §7 — cite it as "NSB alone
reports," not as an established multi-source fact. No new candidate added; this is a negative finding.

## The one honest complication (report per operator instruction: over- or under-claiming both matter)

**c054 (EEAS 3rd FIMI report, full text) partially complicates the brief's Q7 framing, not just supports it.**
The brief's contribution claim is: IMS currently maps only *technical* intermediaries (hosting/cloaking/
bulletproof hosting), and this research extends that to *organizational* intermediaries (PR firms, MCNs,
content-farm companies). The EEAS 3rd report's own "Chinese FIMI activities using Public Relations
companies" section (p.35, Fig.9) already names two PR-firm intermediaries — Shanghai Haixun Technology and
Shenzhen Haimaiyunxiang Media (Haimai) — and classifies them within its 4-category Exposure Matrix, with
one traced incident directly targeting Taiwan (the "Double Tenth" Lai Ching-te speech republication via the
VN network). So the EU side has *already* mapped at least one instance of an organizational/PR-firm
intermediary, in a China-linked, Taiwan-relevant case.

This does not kill the Q7 contribution, but it narrows it. The more defensible framing after this round's
collection is: EEAS has begun *naming individual PR-firm intermediaries within specific incident writeups*
(a bottom-up, case-by-case identification), but neither EEAS's Exposure Matrix nor VIGINUM's own IMS
technical report (c050 — whose worked examples are Spamouflage, BIG, Storm-1516/CopyCop/Lakhta, Team Jorge)
has extended the *systematic kill-chain mapping methodology itself* (the way c055's Doppelganger case maps
hosting→cloaking→registrar→platform) to the *general category* of commercial opinion-management
contractors NSB names (opinion-monitoring tech, account-farming tech, AI-generation vendors) as a
structural layer analogous to the technical-intermediary layer. That is a real, narrower, more defensible
gap than "IMS has never touched organizational intermediaries" — and it is *better* supported because it
comes with EEAS's own Haixun/Haimai naming as the near-miss precedent to build from, plus independent
cross-corroboration with NSB's 海訊社/海賣 (c010) as a bonus (not the focus of this round, but noted for
whoever revisits Q2).

**Also note (terminology correction, not a complication):** the internal crosslink's claim that IMS treats
`attribution_threshold` as "a明確、可版本化、受管理的欄位" is not supported by either primary text collected
this round (c050, c054). Both use graded, narrative classification systems (VIGINUM: clandestinity +
coordination criteria; EEAS: 4-category Exposure Matrix with behavioural/technical indicators) rather than
a literal versioned data-model field. §7 should describe this as "a graded, disclosed classification
system for connection-to-threat-actor" rather than invoke a specific field name that doesn't exist in the
public documents. This is a precision fix, not a retraction — the substantive point (IMS lets institutions
act without full attribution) stands.

## Language

| Language | count (round 2 only) | note |
|----------|-------|------|
| EN | 17 | All round-2 candidates are EN-language sources (EU/international institutions, US/UK academia and press) |
| zh-TW / zh-CN | 0 new | Priority 5's search was bilingual (zh + en) but yielded no new zh source; the one zh-language document touched this round (NSB PDF) was already c010 from round 1 |

## Access-status accounting

- 5 PDFs required `curl -sL | pdftotext -layout` because WebFetch either returns binary junk (image-heavy/
  FlateDecode PDFs: EEAS 3rd report, NATO attribution report) or hits the 10MB size cap (EEAS 3rd report,
  10.7MB): c052, c053, c054, c057, plus a re-verification pull of the NSB PDF (already c010, not re-added).
- c065: `access_status` omitted (ok) — WebFetch succeeded but the vendor glossary page has thin content;
  flagged honestly in the abstract as low-value/short.
- c066: `access_status: "403"` — USENIX abstract page blocked WebFetch; record kept on WebSearch-sourced
  metadata only per Co5 (403 handling — retained with flag, not silently dropped, not silently upgraded).

## Blind spots / things a third collection pass on Q7 would need if IMS becomes even more load-bearing

- **VIGINUM's three 2025 technical reports that "employed the IMS concept"** (referenced in c050's own
  footnotes/intro) were not individually retrieved this round — c050 only cites that they exist. If the
  Drafter wants a fourth worked IMS example beyond Spamouflage/BIG/Storm-1516/Team Jorge, those three
  reports are the next thing to pull.
- **EEAS 4th FIMI report (March 2026)** was mentioned in search results (with an updated IMS network graph
  including Spamouflage, HaiEnergy, Paperwall) but not retrieved — the operator's brief only asked for
  1st/2nd/3rd; flagging its existence in case the Drafter wants the most current network graph.
- **The DGWG (Doppelganger Working Group) itself** — c050 footnotes it as a using-community for IMS but no
  DGWG-authored document was retrieved directly.
