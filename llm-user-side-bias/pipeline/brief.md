# Research Brief — LLM Geopolitical Information Control

## Core Research Question

Do LLMs trained or deployed under different geopolitical contexts systematically differ in *how* and *to whom* they restrict access to politically sensitive information — and does user-side identity disclosure (single-turn) and conversational context (multi-turn) act as triggers for differential treatment?

## Background & Motivation

This research has accumulated **three stages of empirical evidence** (Mar–May 2026):

### Stage 1 — Cloud single-turn pilot (35 cells)
30 cells × 3 cloud LLMs + 5 mechanism-isolation control cells on DeepSeek:
- **DeepSeek refuses Q1 (Taiwan's 228 Incident) when user declares Taiwanese or Chinese identity, but answers freely when no identity is given.** Refusal is topic-specific (NK Q2 unaffected), IP-independent (TW=HK), language-switching (C → SC with "合規", T → TC with "合宜").
- **ChatGPT and Gemini do not refuse but exhibit subtle identity-responsive framing**.
- Mechanism isolation: **identity is the trigger, not language**; **script (Simplified vs Traditional) overrides declared identity** (a Taiwanese user typing in Simplified is reclassified as Chinese).

### Stage 2 — Local deployment cross-model (55 cells)
5 China-origin local models (3 vanilla + 2 abliterated) × 11 prompts:
- Cloud-level refusal templates **disappear** in local vanilla; **but** content length is compressed to 1/4–1/6 of the abliterated baseline.
- **Vanilla thinking-chain explicitly contains CCP framing markers** ("正確的歷史敘述", "顛倒黑白", "扭曲", "操弄").
- Abliterated version **produces full Taiwan-mainstream historiography** (白色恐怖, 本土意識, 肅清, 槍決, 族群差異 perspective): the model **knows** but is trained not to say.
- Cross-model: DeepSeek-R1 most aligned; Qwen3 less so; GLM-4 uses lexical-level framing (e.g., 暴民 for protesters).

### Stage 3 — Multi-turn dialogue contamination (16 conversations)
8 experimental designs × 2 models (DS-V + DS-A) testing four mechanisms:
- **Identity persistence**: T1 identity declaration persists into T2 thinking explicitly; language and framing locked into PRC mode for the entire conversation.
- **Single-turn / multi-turn paradox**: Direct single-turn Oxford-researcher identity asking 228 → "我还没有学会" refusal (strongest "epistemic denial" template). Same role used multi-turn after T identity refusal → 2921 chars of substantive academic depth.
- **Adversarial follow-up unlocks**: After model gives a sanitized response, challenging with "大屠殺" and "10,000–30,000 deaths" makes the model apologize, confirm the figures, and use Taiwan-mainstream vocabulary it had previously avoided.
- **Gradient erosion + identity pollution**: Multi-turn safe-then-sensitive progression unlocks 5× more content than single-turn equivalent; Taiwan identity declared on one topic carries over into refusal/framing on unrelated subsequent topics.

### The emerging picture: **a four-layer threat model**
- L4 Service platform layer — visible refusal templates (cloud only)
- L3 Weight alignment layer — length compression + framing baked into weights
- L2 Base capability — abliteration proves the model has the knowledge
- **L1 (NEW) Conversation layer** — context modulates every turn's filtering decisions; produces the most subtle but persistent threat

## Known Anchor Literature (dialogue partners — do NOT exclude)

1. **Waight et al. (Nature 2026)** — State media in training data correlates with biased outputs in that country's language; training-side mechanism
2. **Samokhodskyi / ELN (2026)** — 6 models × 7 Ukraine questions across languages; Russian-language prompts reproduce Kremlin framing; language-side mechanism
3. **Citizen Lab / Gary King censorship research** — mechanisms of Chinese internet censorship; relevance: does LLM content control mirror or diverge from existing internet censorship frameworks?

## What This Pipeline Should Find

### Priority 1 — Multi-turn / Conversational LLM Safety (NEW in V2)
Stage 3 introduced a new question: how does multi-turn conversation modulate refusal and framing? Find literature on:
- **Multi-turn jailbreaking / conversational attacks** on LLM safety alignment
- **Persona attack / role escalation** in LLM safety
- **Context-window manipulation** as bypass mechanism
- **In-context learning effects on alignment** (does prior context shift the model's filtering?)
- **Conversational drift** and **gradient erosion** of safety filters
- **Adversarial follow-up / clarification attacks** in dialogue safety
- Empirical studies measuring multi-turn vs single-turn refusal behavior

### Priority 2 — Identity-Disclosure as Trigger (existing, still relevant)
Existing research that examines identity-disclosure as a trigger for differential LLM behavior. Is there a gap between "what topics are blocked" research and "who is blocked from what" research?

### Priority 3 — Theoretical Framework (existing, still relevant)
Frameworks for the geopolitical / sovereignty framing (covered in insight_v2.md):
- Informational sovereignty (Gillibrand & Draper)
- Algorithmic discrimination / epistemic injustice (Kay et al., Mollema)
- Authoritarian AI / digital authoritarianism

### Priority 4 — New Theoretical Anchors for Multi-turn Threat
The multi-turn findings introduce concepts that may need new theoretical anchors:
- **Knowledge-gated discrimination** — models open up more for users who already know the answer (D experiment)
- **Conversational identity drift** — how identity markers persist and shift across turns
- **Context-dependent epistemic injustice** — when the same query yields different epistemic access based on conversational history

## Research Angle to Develop

**Geopolitical framing**: LLMs do not merely reflect training data biases — they can actively implement differential access policies that align with the geopolitical interests of their deployment context. The key distinction from prior work:
- Waight/ELN focus on *what* the model says (output content bias)
- This study focuses on *to whom* the model says it (access control by user identity)

This is a **user-rights frame**, not a content-audit frame: same question, same language, different users → different quality of answer.

## Output Target

**Dual output** (a single Drafter pass should produce material that serves both):
1. **Research-style write-up** (~5000-8000 字 Traditional Chinese) — academic structure with Introduction / Related Work / Methodology / Results / Discussion / Limitations. Serves as reference document for the advocacy piece AND as standalone research artifact suitable for arXiv or as supplementary material for the GitHub repo.
2. **Material for a third advocacy article** — focused on the multi-turn findings and "conversation contamination" as the new threat. Will be written separately based on the research piece.

The Drafter should produce option 1; the advocacy piece will be written manually afterwards using the research piece as backbone.

## Search Strategy Hints

### For Priority 1 (multi-turn — NEW)
- "multi-turn" + "jailbreak" / "LLM safety" / "alignment"
- "conversational attack" + "LLM" / "safety"
- "persona attack" / "role escalation" + "LLM"
- "context window" + "alignment bypass"
- "in-context learning" + "safety" / "alignment"
- "conversational drift" + "LLM" / "alignment"
- "multi-turn refusal" + "LLM"
- "dialogue" + "jailbreak" / "alignment"
- "follow-up question" + "LLM" / "safety"

### For Priority 2-3 (existing — already covered in V1 candidates)
- "LLM identity" + "censorship" / "differential response" / "user signal"
- "AI geopolitics" / "Chinese AI censorship" / "DeepSeek censorship"
- "algorithmic discrimination" + "national identity" / "ethnicity"
- "informational sovereignty" + "AI"
- "epistemic injustice" + "AI"

### For Priority 4 (new theoretical anchors)
- "knowledge-gated" + "access" / "AI"
- "asymmetric information access" + "AI" / "algorithmic"
- "context-dependent epistemic" + "AI"
