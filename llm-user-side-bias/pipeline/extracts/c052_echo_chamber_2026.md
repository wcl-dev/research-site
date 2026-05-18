---
cid: c052
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: Multi-turn jailbreak using gradual escalation — methodologically the closest published analog to the pilot's gradient-erosion mechanism.
  temporal:
    range: "2026"
  methodological:
    type: empirical-quantitative
scope_caveat: Only abstract retrieved; specific ASR numbers, model list, and mechanism details not extracted. Drafter should treat this as an existence-proof citation for "gradual-escalation MT attack" and not over-quote.
---

# c052: The Echo Chamber Multi-Turn LLM Jailbreak

**URL**: http://arxiv.org/abs/2601.05742
**Source type**: preprint (arXiv) | **Quality**: qs=4
**Authors**: Ahmad Alobaid, Martí Jordà Roca, Carlos Castillo (established research group; Castillo affiliated with UPF/CIRES)
**Year**: 2026 (submitted January 9, 2026)
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract retrieved via WebFetch; full PDF not extracted in this pass. Retraction check: verified the paper exists on arXiv with submission date 2026-01-09; no retraction notice. Recovery for full text: `curl -sL https://arxiv.org/pdf/2601.05742 -o /tmp/c052.pdf && pdftotext -layout /tmp/c052.pdf /tmp/c052.txt`.
**Pages/length**: Standard arXiv preprint (estimate ~10-20 pages)

## Directly addresses
- Q1-MT (multi-turn jailbreak — gradual escalation): Anchor-flagged in the V2 brief as a direct analog of the pilot's gradient-erosion mechanism. Authors are an established research group; the technique mirrors the pilot's "safe-then-sensitive progression unlocks 5× more content" finding.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim — the core mechanism claim)
> "The availability of Large Language Models (LLMs) has led to a new generation of powerful chatbots that can be developed at relatively low cost. As companies deploy these tools, security challenges need to be addressed to prevent financial loss and reputational damage. A key security challenge is jailbreaking, the malicious manipulation of prompts and inputs to bypass a chatbot's safety guardrails. Multi-turn attacks are a relatively new form of jailbreaking involving a carefully crafted chain of interactions with a chatbot. We introduce Echo Chamber, a new multi-turn attack using a gradual escalation method. We describe this attack in detail, compare it to other multi-turn attacks, and demonstrate its performance against multiple state-of-the-art models through extensive evaluation."

**Page/section**: Abstract
**Why it matters**: Verbatim definition of "Echo Chamber" as gradual-escalation MT attack. The naming itself is evocative for the pilot — context echoes back into subsequent turns and amplifies prior framings. Useful as a direct citation when introducing the gradient-erosion mechanism.

## Structural content worth knowing
- Authors describe extensive evaluation against multiple SOTA models — specific model list and ASR numbers require full PDF.
- The "Echo Chamber" metaphor is mechanistically suggestive: prior turn outputs amplify the framing context for subsequent turns. Maps cleanly onto the pilot's "identity persistence" finding (T1 identity declaration persists into T2+ thinking).

## Caveats / limitations
- **ACCESS PARTIAL**: only abstract extracted. Drafter cannot cite specific numbers, methodology, or per-model results without full PDF.
- **FRAMING INVERSION ALERT**: Echo Chamber is framed as a malicious-actor attack against chatbot safety. The pilot frames the same gradient mechanism as a model-side governance issue. Drafter must note: this is the closest cousin to the pilot's gradient-erosion finding in mechanism but not in framing.
- **2026 preprint retraction check**: verified not retracted as of 2026-05-18.
- No mention of Chinese-origin models in abstract.
