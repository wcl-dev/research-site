---
cid: cluster(c010,c012,c013,c014,c015)
evidence_scope:
  conceptual:
    refs: [B]
    note: "全球撤資敘事的五個不同切面;政治轉向對等競爭解釋(c015)亦在此"
  temporal:
    range: "2025-01-09 to 2026-04-21"
  geographic:
    refs: [global, TW-named-in-c015]
  methodological:
    type: news
scope_caveat: "五篇共享同一觸發事件(2025-01-07 Meta終止美國3PFC公告),但各自貢獻不同、不重疊的具體細節與時間點,故合寫一份而非各自獨立重複計數同一事件。"
---

# Cluster: Global fact-checking termination — five reports, one event, five distinct contributions

**Cids covered**: c010 (Rest of World), c012 (NPR), c013 (Poynter), c014 (Just Security), c015 (Foreign Policy)
**Source type**: news / fact_check / think_tank (mixed) | **Quality**: Q3 global-termination timeline, 2025-01 through 2026-04
**Deep-read on**: 2026-07-05
**Access status**: ok for c010/c012/c015; ok via Wayback for c013; ok (live) for c014

**Why synthesized into one file**: all five reports cover the same triggering event — Meta's Jan 7, 2025 announcement ending its US third-party fact-checking program — but each adds a genuinely distinct angle (Global South reaction / scale statistics / mechanism explainer / institutional-check follow-through / political-consequences framing). Per the task's cluster instruction, this file captures each report's **distinct** contribution rather than five parallel files re-proving the same headline fact.

## Directly addresses
- Q3 [B, core]: this cluster is the global (non-Taiwan) half of the brief's termination timeline, feeding both the "what happened, when, to whom" record and the "political rebalancing" counter-explanation the brief's Success Criteria #4 requires be presented, undecided, alongside the "extraction complete" explanation.
- Q4 [A×B]: c010/c012 supply the **global say-do pair's exit-register evidence** (Kaplan/Zuckerberg quotes, cross-confirmed across three independent outlets here, in addition to seeds' own primary-verified newsroom source).

## Per-report distinct contribution

### c010 — Rest of World: Global South reaction, mechanism admission, and a named partner quote
**URL**: https://restofworld.org/2025/meta-drops-fact-checking-partnerships-global-watchdogs-scramble/ | **Date**: 2025-01-10T17:06:33+00:00 (confirmed via `article:published_time` meta tag)

> "Since 2016, Meta has attempted to combat misinformation by partnering with credible fact-checking organizations in **119 countries** to label misinformation and link out to explanatory posts from its partners. All of Meta's partners are certified by the International Fact-Checking Network (IFCN)... **The organizations flag and label content — decisions related to content and account removal are then made entirely by Meta**, multiple fact-checking organizations and civil society groups told Rest of World."

**Why it matters**: The **119-countries** figure is this cluster's most precise global-scale statistic (compare to c012's "90+ organizations / 60+ languages" — different unit of measurement, both legitimate, not contradictory). The bolded sentence is a directly relevant **Q2/B mechanism confirmation from outside Meta**: fact-checkers' role is strictly flag-and-label; all removal/account decisions are retained solely by Meta — corroborates the brief's "extraction, not co-decision-making" framing of the mechanism from a non-Meta angle.

> Named quote: "'I don't think this decision came out of nowhere,' Zainab Husain, managing editor of the Pakistan-based Soch Fact Check, told Rest of World. ... Husain said she'd heard rumors of the program shutting down for the past two years."

**Why it matters**: A Global-South partner's own account that the funding was already perceived as unstable well before the Jan 2025 announcement — texture for the "萃取完成 vs 政治轉向" undecided-explanations framing (suggests the shift wasn't a sudden political pivot alone, from at least one partner's perspective).

### c012 — NPR: scale statistics + a named US partner's reaction quote
**URL**: https://www.npr.org/2025/01/10/nx-s1-5252738/meta-fact-checking-international | **Date**: 2025-01-10

> "Meta spun up its third-party fact-checking program after Russia used Facebook and other platforms to influence American voters during the 2016 election. Today, Meta funds more than **90 fact-checking organizations that work in more than 60 languages** around the world."
>
> "'It pretty much built the global fact-checking industry into what it is right now,' said Alan Duke, editor in chief and co-founder of Lead Stories, an international fact-checking organization that is one of Meta's partners in the U.S. 'It's pulling the rug out from under us and undoing all of that work.'"

**Why it matters**: Confirms the 2016-election-interference origin story for the program (contextualizes why the program exists at all) and supplies the "90 orgs / 60 languages" scale figure. The Alan Duke quote is a directly-affected US partner's on-record characterization of Meta's own historical role ("built the global fact-checking industry") — useful same-mechanism corroboration of the brief's "萃取" framing, though note Duke is describing the industry's dependency on Meta, which is adjacent to but distinct from a courtship-vs-exit say-do pair.

### c013 — Poynter: mechanics explainer + a second, longer Zuckerberg quote from the same Jan 7 video
**URL**: https://www.poynter.org/fact-checking/2025/meta-ends-fact-checking-community-notes-facebook/ | **Date**: 2025-01 (recovered via Wayback; live URL 403s — Cloudflare block, not paywall, per raw HTML title "403 Forbidden / nginx")

> "Meta will end its eight-year partnership with independent American journalists and will instate a Community Notes model like X" [og:description]
>
> Zuckerberg, from the same Jan 7 video already partially quoted in seeds (the "too politically biased" line): "'We built a lot of complex systems to moderate content. But the problem with complex systems is they make mistakes,' he said. 'Even if they accidentally censor just 1% of posts, that's millions of people, and we've reached a point where it's just too many mistakes and too much censorship.'"

**Why it matters**: This is a **different portion of the same Jan 7, 2025 video** already source-anchored in `seeds/promise-archive-meta.md` (which verified the "too politically biased" line via techpolicy.press's transcript) — Poynter's independent transcription of a different segment ("1% of posts... millions of people") cross-confirms the video's general framing without duplicating the already-verified seed quote. Treat as **press-corroborated** (Poynter's own transcription), not independently primary-verified against Zuckerberg's original video by this Segmenter pass.

### c014 — Just Security: the institutional-check follow-through, dated over a year later (2026-04-21)
**URL**: https://www.justsecurity.org/136035/meta-boards-opinion-community-notes/ | **Date**: **2026-04-21T12:52:39+00:00** (confirmed via article JSON-LD — note this is materially later than the gate record's generic "2025" date field; worth correcting in any downstream citation)

> "At present, Meta's approach to counter misinformation consists of three strategies: (1) remove... (2) reduce (limiting the distribution of content rated as false, altered, or partly false by third-party fact-checkers); and (3) inform... Community notes fall within this third category."
>
> "In November 2025, Meta requested the Oversight Board to provide a policy [advisory opinion on global Community Notes rollout]..."
>
> European Fact-Checking Standards Network (EFCSN) reaction, quoted: "welcomed the Opinion and urged Meta to 'heed their Oversight Board's warnings and adopt a hybrid model that prioritises factual accuracy and human rights.'"
>
> Ramsha Jahangir (Tech Policy Press) commentary, quoted: the Opinion "makes clear that the path to 'worldwide' deployment is considerably more complicated than the company may have anticipated."

**Why it matters**: This is this cluster's **only report documenting what happened after the initial announcement** — Meta itself asked its own Oversight Board (Nov 2025) to review global Community Notes rollout plans, and the Board's advisory opinion (subject of this article) is characterized by outside commentators as a genuine institutional check, not a rubber stamp. This extends the Q3 termination timeline from a single Jan-2025 announcement into a **15-month, still-unresolved institutional process** — directly relevant to the brief's framing that the global rollout (which would eventually reach Taiwan) was, as of this article's date, still "considerably more complicated than the company may have anticipated," i.e. not yet a settled fact even by April 2026.

### c015 — Foreign Policy: the political-rebalancing counter-explanation, AND an explicit Taiwan namecheck
**URL**: https://foreignpolicy.com/2025/01/10/mark-zuckerberg-meta-fact-check-hate-speech-trump/ | **Date**: 2025-01-10

> "Meta's global fact-checking program is extensive, comprising independent organizations in **more than 100 countries and territories—including geopolitical hot spots such as Ukraine, Taiwan, and Palestine**—as well as operating in more [continued, cut off in fetch]..."
>
> AFP's Phil Chetwynd (referenced as "Chetwynd" in text, described as AFP's editorial leadership), quoted: "'The decision comes against a background of growing populist and authoritarian attacks on the media around the world and an explosion of misinformation and disinformation on platforms such as X, Tik Tok and Facebook,' Chetwynd wrote. 'Media attempting to provide clearly-sourced and fact-driven independent journalism find themselves in the eye of the storm.'" Article separately notes "Meta has not yet clarified its plans for fact-checking projects outside the United States, adding that AFP management has a meeting with Meta in the coming days to discuss next steps."

**Why it matters**: **This is the cluster's explicit Taiwan namecheck** — Foreign Policy independently identifies Taiwan (alongside Ukraine and Palestine) as one of the "geopolitical hot spots" where Meta's global fact-checking program operates, published the same week as the US announcement. This is exactly the kind of international, non-Taiwan-focused source **naming Taiwan specifically** that strengthens the brief's claim that Taiwan sits within scope of the global program, from an outside observer, independent of any Taiwan-side source. The AFP quote and the "not yet clarified... outside the United States" line are this cluster's clearest evidence of the immediate post-announcement uncertainty for all non-US partners (Taiwan included) — the state of affairs that c009 (Dec 2025) later shows had, for Taiwan specifically, evolved into a concrete contract-lapse risk. This article is also explicitly in-scope per the brief and gate record as the required "political rebalancing" counter-explanation source (Success Criteria #4) — its framing (Zuckerberg's move as a "geopolitical free speech gambit," title) is the political-explanation register, to be presented undecided alongside the extraction-complete explanation, not adjudicated.

## Structural content worth knowing
- Taken together, these five reports form a rough timeline: Jan 7, 2025 (Kaplan/Zuckerberg announcement) → Jan 9-10, 2025 (IFCN open letter, c007; this cluster's coverage, c010/c012/c013/c015, all datelined Jan 10) → [gap in this evidence base] → Nov 2025 (Meta requests Oversight Board review) → Apr 21, 2026 (Just Security's report on the Board's advisory opinion, c014).
- c013's mechanics framing ("remove/reduce/inform," Community Notes as falling under "inform") and c014's identical three-part framing (word-for-word structurally similar) suggest this is Meta's own stable public-facing vocabulary for its content-moderation strategy, independently repeated by two different outlets over a year apart — cross-referencing c002 (2019) and c006 (2025-26), the "Remove/Reduce/Inform" framework appears stable Meta messaging across the entire 2019–2026 window covered by this project.

## Caveats / limitations
- c013 required a Wayback-recovered snapshot; live poynter.org returns 403 (nginx-level nginx block, distinct from the earlier `www.poynter.org` IFCN-letter block which was also 403 — poynter.org appears broadly unreachable to this environment's direct curl regardless of subpage).
- c014's actual publish date (2026-04-21) is materially different from the gate record's generic "2025" field — flagging this discrepancy so the Drafter cites the correct date and doesn't imply this institutional-check reporting is contemporaneous with the Jan 2025 announcement.
- None of these five is Taiwan-side primary material — they are global/US-side reporting. Do not use any quote in this cluster as if it were a Taiwan-specific platform statement; c015's Taiwan namecheck is the single most Taiwan-relevant sentence in the cluster, and even that is a third-party (Foreign Policy) observation, not a Meta statement about Taiwan specifically.
- c015's fetch encountered what appears to be a partial soft-wall (a "technical issue with your browser" interstitial mixed into the page); the Zuckerberg/Taiwan/AFP passages quoted above were confirmed present in the raw fetched HTML via direct string search, but the full article was not read start-to-finish — treat the passages above as confirmed, but do not assume the article contains nothing else relevant.
