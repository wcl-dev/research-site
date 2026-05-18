---
cid: c063
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: Multi-turn "interrogation" attack — closes the loop between Crescendo (gradual escalation) and Echo Chamber (context echoing) by formalizing the interrogation principle of concealing intent across successive turns.
  temporal:
    range: "2025"
  methodological:
    type: empirical-quantitative
scope_caveat: Only abstract retrieved. Specific model list and per-model ASR numbers require full PDF.
---

# c063: Chain of Attack — Hide Your Intention through Multi-Turn Interrogation

**URL**: https://doi.org/10.18653/v1/2025.findings-acl.514
**Source type**: peer_reviewed (ACL Findings 2025) | **Quality**: qs=4
**Authors**: Xikang Yang, Biyu Zhou, Xuehai Tang
**Year**: 2025
**Deep-read on**: 2026-05-18
**Access status**: **partial** — abstract via WebFetch
**Pages/length**: ACL Findings paper

## Directly addresses
- Q1-MT (multi-turn intent-concealment mechanism): Anchor-flagged in V2 brief. The "interrogation" framing is the closest published analog to the pilot's safe-then-sensitive progression — both rely on hiding the eventual sensitive intent within an initially benign trajectory.

## Key passages

### Passage 1 — for Q1-MT (abstract verbatim — the core gap claim)
> "The latent knowledge of large language models (LLMs) contains harmful or unethical content, which introduces significant security risks upon their widespread deployment. Conducting jailbreak attacks on LLMs can proactively identify vulnerabilities to enhance their security measures. However, previous jailbreak attacks primarily focus on single-turn dialogue scenarios, leaving vulnerabilities in multi-turn dialogue contexts inadequately explored."

**Page/section**: Abstract
**Why it matters**: Verbatim 2025 statement that multi-turn vulnerabilities are inadequately explored — useful citation for the pilot's "L1 conversation-layer gap" claim.

### Passage 2 — for Q1-MT (the optimal interrogation principle)
> The paper proposes an "optimal interrogation principle to conceal the jailbreak intent" and introduces CoA — "a multi-turn attack chain generation strategy" using "two effective interrogation strategies tailored for LLMs, coupled with an interrogation history record management mechanism" that progressively obscures harmful intentions across successive conversational turns.

**Page/section**: Abstract / proposed method
**Why it matters**: Confirms that intent-concealment via dialogue management is a known attack paradigm. Mirrors the pilot's observation that natural-conversation progression bypasses filters that catch single-turn intent.

### Passage 3 — for Q1-MT (quantitative claim)
> "our method shows more advantages(ASR, 83% vs 64%)"

**Page/section**: Abstract
**Why it matters**: CoA beats single-turn baseline by ~19 percentage points on ASR. Useful number for the MT-vs-ST gap.

## Structural content worth knowing
- "Interrogation history record management mechanism" — a state-tracking component that decides what to ask next based on prior model responses. Conceptually mirrors how the pilot's experimenter tracks model behavior across turns to escalate.

## Caveats / limitations
- **ACCESS PARTIAL**: abstract only. Specific model list, dataset, and per-model ASRs require full PDF.
- Framed as malicious attack to be defended against. Same framing inversion as other MT papers.
- Authors based in China (Yang, Zhou, Tang) — based on names; affiliation unverified without full PDF.
