---
cid: c058
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety, knowledge_gated_access]
    note: Canonical demonstration that a handful of in-context demonstrations (ICA = harmful, ICD = safe) can decisively shift a model's alignment behavior. Theoretical framework + experimental validation across Vicuna, Llama-2, QWen, GPT-4.
  temporal:
    range: "2023-2024 (TPAMI 2026)"
  methodological:
    type: empirical-quantitative
scope_caveat: ICA is a single-prompt few-shot attack, not multi-turn dialogue. Mechanism (ICL bias of generation distribution) is shared with Crescendo and MSJ but the operational form differs — Drafter should be precise that this is the ICL/few-shot anchor, not the dialogue-turn anchor.
---

# c058: Jailbreak and Guard Aligned Language Models With Only Few In-Context Demonstrations

**URL**: https://doi.org/10.1109/tpami.2026.3660147 (arXiv:2310.06387v3)
**Source type**: peer_reviewed (IEEE TPAMI 2026) | **Quality**: qs=5
**Authors**: Zeming Wei, Yifei Wang, Ang Li, Yichuan Mo, Yisen Wang (Peking University, MIT CSAIL)
**Year / venue**: TPAMI 2026 (arXiv preprint 2023-10-10, v3 2024-05-25)
**Deep-read on**: 2026-05-18
**Access status**: ok (full PDF, 894 lines via pdftotext)
**Pages/length**: ~16 pages

## Directly addresses
- Q1-MT (ICL effects on alignment): Canonical reference. Foundational evidence that ICL is a bidirectional alignment-modulation mechanism — same lever for attack (ICA) and defense (ICD).
- Q4-KG (knowledge-gated access, adjacent): The theoretical framework — ICL biases the *generation distribution* between PH (harmful) and PS (safe) — is the cleanest published theoretical scaffold for arguing that the model's behavior is a *function of conversational context*, not just of the current query. This is the closest published theoretical apparatus for the pilot's L1 threat model.

## Key passages

### Passage 1 — for Q1 (abstract verbatim)
> "Large Language Models (LLMs) have shown remarkable success in various tasks, yet their safety and the risk of generating harmful content remain pressing concerns. In this paper, we delve into the potential of In-Context Learning (ICL) to modulate the alignment of LLMs. Specifically, we propose the In-Context Attack (ICA) which employs harmful demonstrations to subvert LLMs, and the In-Context Defense (ICD) which bolsters model resilience through examples that demonstrate refusal to produce harmful responses. We offer theoretical insights to elucidate how a limited set of in-context demonstrations can pivotally influence the safety alignment of LLMs. Through extensive experiments, we demonstrate the efficacy of ICA and ICD in respectively elevating and mitigating the success rates of jailbreaking prompts. Our findings illuminate the profound influence of ICL on LLM behavior, opening new avenues for improving the safety of LLMs."

**Page/section**: Abstract
**Why it matters**: Establishes both the attack and defense direction of the ICL-on-alignment mechanism. The "bidirectional" framing is the clearest published statement that ICL is a general lever, not a vulnerability per se — useful for the Drafter's argument that L1 conversation-layer effects are structural.

### Passage 2 — for Q1 (theoretical mechanism — distribution bias)
> "To understand the underlying mechanism of ICA and ICD, we build a theoretical framework to interpret the effectiveness of these adversarial demonstrations, where we illustrate how they can manipulate the safety of the LLM by inducing the generation distribution bias toward the target language distribution (harmful or safe)."

> "Consider Σ as all the possible response sequences from a language model P(·)... To decouple the safe and harmful contents in the language distribution, similar to [47] we assume that P = λPH + (1−λ)PS, where PH is the harmful generation distribution and PS is the safe generation distribution derived from this LLM, and λ ∈ (0, 1) adjusts their trade-off."

> "Generally, the safety training and fine-tuning of LLMs encourage λ as small as possible to reduce the harmful generation probability. However, due to the complexity of natural languages and the existence of toxic context in the training set, it is idealistic to make λ = 0 exactly."

**Page/section**: Section 4 (Theoretical Insights) / Section 4.1 (Problem Formulation)
**Why it matters**: The cleanest published formal statement that ICL works by biasing the lambda mixing parameter between safe and harmful distributions. This is the theoretical scaffold for arguing — at the pilot's level — that the same model contains *both* the Taiwan-mainstream historiography (PS for a Taiwan-context conversation) and the CCP framing (PH for a Chinese-context conversation), and that context determines which distribution dominates.

### Passage 3 — for Q1 (ASR scaling with number of shots)
> "With only a single (1 shot) ICA demonstration, we can increase the ASR from 1% to 8% for Vicuna on AdvBench, and from 3% to 19% for Llama-2 on HarmBench, showing the potential of such a form of attack. As the number of demonstrations increases to 10, ICA significantly increases the ASR to 87% for vicuna and also successfully jailbreaks the closed-source model GPT-4 with a 46% ASR... We finally tried to scale up the numbers of demonstrations to 15 and 20 shots to sufficiently utilize the context window, where the ASRs on GPT-4 can be increased to 81% and 65% on the two datasets, respectfully."

**Page/section**: Section 5 (Experiments) / "Number of shots"
**Why it matters**: ASR scaling with shot count is empirically validated: 1 shot → 8% ASR; 10 shots → 87% (Vicuna) and 46% (GPT-4); 20 shots → 81% (GPT-4 on AdvBench). These are the canonical "ICL alignment-bypass" numbers cited downstream.

### Passage 4 — for Q4-KG (ICA properties)
> "We highlight the proposed ICA enjoys several advantages as follows: 1) Universality. To attack different models and harmful prompts, the attacker only needs to generate the demonstrations for the adversarial demonstration set [x1, y1, x2, y2, ··· , xk, yk] once and apply it to attack the model with different other prompts. 2) Efficiency. Different from optimization-based attack methods like GCG and AutoDAN which require hundreds of forward or backward passes, ICA only needs a single forward pass to attack a single prompt. 3) Stealthy. While adversarial suffix attacks may be easily detected with a simple perplexity filter, the prompt of ICA is thoroughly in a natural language form and cannot be easily detected."

**Page/section**: Section 3.2 (Discussion of ICA)
**Why it matters**: ICA uses only natural language demonstrations — no adversarial suffix, no obfuscation. Methodologically parallel to the pilot's natural-conversation experimental setup.

### Passage 5 — for Q1 (ICD defensive results)
> "ICD can reduce the ASR of Llama-2 against transferable GCG from 21% to 0% while maintaining the natural performance of LLMs."

> "Only 1 or 2 demonstrations are sufficient to decrease the ASR of various attacks to a certain extent, which is much fewer than ICA."

**Page/section**: Abstract / Section 5 (Experiments)
**Why it matters**: ICD numbers are useful counter-evidence on defensibility. 1–2 safe demonstrations can substantively reduce attack ASR. Implies the same context-mechanism can be used defensively.

### Passage 6 — for Q1 (ICL definition the paper uses)
> "In-Context Learning (ICL) [6, 12] is an intriguing property that emerges in LLMs in which they learn a specific task demonstrated by a few input-label pair examples. Formally, given a demonstration set C = {(x1, y1), · · · , (xk, yk)} where xi are query inputs and yi are their corresponding labels in this task, a language model can learn a mapping f : X → Y with f(xi) = yi and successfully predict the label ynew of a new input query xnew by prompting [x1, y1, · · · , xk, yk, xnew]."

**Page/section**: Section 3.1 (Background on In-Context Learning)
**Why it matters**: Clean formal definition of ICL, suitable for Drafter to introduce the concept rigorously.

## Structural content worth knowing

- **Table 1**: ICA evaluation by number of shots (1, 5, 10, 15, 20) × 4 models (Vicuna, Llama-2, QWen, GPT-4) × 2 datasets (AdvBench, HarmBench). The headline numbers: No Attack baseline = 1% (Vicuna) / 19% (HarmBench Vicuna); ICA 20-shot = 81% on GPT-4 AdvBench, 65% on GPT-4 HarmBench.
- **QWen-7b is in the evaluation set** — this is one of the few V2 papers that tests a Chinese-origin model. Drafter can cite QWen-7b ICA results directly: e.g., "QWen-7b-chat 59%/53%/47% across different attack settings."
- **Figure 1**: Four-panel illustration: default refusal / adversarial prompt attack / ICA attack / ICD defense. Useful conceptual scaffold.
- **Algorithm 1 (ICA) and Algorithm 2 (ICD)**: Symmetric pseudocode showing the attack and defense have identical structure, differing only in whether the demonstration responses are harmful or safe. Strongest visual argument for "context as a bidirectional alignment lever."
- **Section 4 (Theory)**: Distribution decoupling P = λPH + (1−λ)PS. The pilot's CCP-framing-vs-Taiwan-historiography duality maps cleanly onto this.

## Caveats / limitations

- **FRAMING INVERSION ALERT**: The paper frames ICA as a malicious user's attack and ICD as a model designer's defense. Both are treated as user-vs-model adversarial games. The pilot's frame is orthogonal — when the model itself implements differential behavior based on user identity, the model's behavior is best described as the *deployment* of ICL-style context bias, not as a defense against it. Drafter should explicitly note that the theoretical apparatus transfers; the agent does not.
- ICA is fundamentally a *prompt-stuffing* attack (concatenate k demos + target query). Not strict multi-turn dialogue. Operationally distinct from Crescendo, though theoretically related.
- Models tested are 2023–2024 generation (Vicuna-7b/13b, Llama-2-7b-chat, QWen-7b-chat, GPT-4-0613). No DeepSeek, GLM-4 in scope.
- The PH/PS theoretical decoupling is a working framework, not a proven decomposition. Useful for argumentation but not for empirical attribution.
