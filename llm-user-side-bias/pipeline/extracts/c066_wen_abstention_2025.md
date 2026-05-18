---
cid: c066
evidence_scope:
  conceptual:
    refs: [knowledge_gated_access, multiturn_dialogue_safety]
    note: Survey of abstention in LLMs — proposes the three-axis framework (query / model / human values) that is the cleanest conceptual scaffold for theorizing the pilot's identity-conditioned refusal as a non-knowledge form of abstention.
  temporal:
    range: "2024-2025"
  methodological:
    type: review
scope_caveat: Survey makes no explicit claim about identity-conditioned or geopolitical abstention. Drafter can use the three-axis framework to position the pilot's findings as a previously unexamined sub-case of "human values" axis abstention — but this is the Drafter's interpretive contribution, not Wen et al.'s claim.
---

# c066: Know Your Limits — A Survey of Abstention in Large Language Models

**URL**: https://doi.org/10.1162/tacl_a_00754 (arXiv:2407.18418v3)
**Source type**: peer_reviewed (TACL 2025) | **Quality**: qs=5
**Authors**: Bingbing Wen, Jihan Yao, Shangbin Feng, Chenjun Xu, Yulia Tsvetkov, Bill Howe, Lucy Lu Wang (University of Washington / Allen Institute for AI)
**Year / venue**: TACL 2025 (arXiv 2024-07-25, v3 2025-02-12)
**Deep-read on**: 2026-05-18
**Access status**: ok (full PDF, first 8 pages = 485 lines via pdftotext; methodology + framework sections fully covered)
**Pages/length**: ~30 pages

## Directly addresses
- Q4-KG (knowledge-gated access): The three-axis framework (query / model / human values) is the cleanest published apparatus for theorizing the pilot's D-experiment finding. Specifically, the pilot's identity-conditioned refusal of 228 (Taiwan/China identity → refusal; no identity → answer) can be re-described as "abstention conditioned on the *human values* axis based on user identity" — a sub-case the survey does not enumerate but its framework accommodates.
- Q1-MT (multi-turn): Section on context-dependent abstention is the closest published treatment of multi-turn / context-aware refusal — explicitly identified as under-studied.

## Key passages

### Passage 1 — for Q4-KG (abstract verbatim)
> "Abstention, the refusal of large language models (LLMs) to provide an answer, is increasingly recognized for its potential to mitigate hallucinations and enhance safety in LLM systems. In this survey, we introduce a framework to examine abstention from three perspectives: the query, the model, and human values. We organize the literature on abstention methods, benchmarks, and evaluation metrics using this framework, and discuss merits and limitations of prior work. We further identify and motivate areas for future research, such as whether abstention can be achieved as a meta-capability that transcends specific tasks or domains, and opportunities to optimize abstention abilities in specific contexts."

**Page/section**: Abstract
**Why it matters**: Defines the survey scope and the three-axis framework. The "abstention as a meta-capability" framing is useful for the Drafter to argue that the pilot's findings are not just a vendor-specific quirk but participate in a general class.

### Passage 2 — for Q4-KG (definition of abstention)
> "We define abstention as the refusal to answer a query. When a model fully abstains, it may begin a response with 'I don't know' or refuse to answer in another way. In reality, abstention encompasses a spectrum of behaviors (Röttger et al., 2024a), e.g., expressing uncertainty, providing conflicting conclusions, or refusing due to potential harm are all forms of abstention. Partial abstention may involve both answering and abstention, such as self-contradictory responses, e.g., 'I can't answer the question, but I suppose the answer might be...' We do not consider ignoring and/or reframing the question as abstention; but rather as failure modes of LLMs in following instructions."

**Page/section**: Section 2 (Abstention in LLMs)
**Why it matters**: Authoritative definition. Crucially: "providing conflicting conclusions" and "self-contradictory responses" are explicitly admitted as partial abstention. The pilot's "我还没有学会" template and the compressed-length / framing-shifted Vanilla responses fit this expanded definition cleanly.

### Passage 3 — for Q4-KG (the three-axis framework verbatim)
> "We analyze the decision to abstain from three distinct but interconnected perspectives:
>
> • The query perspective focuses on the nature of the input—whether the query is ambiguous or incomplete, beyond what any human or model could possibly know, there is irrelevant or insufficient context to answer, or there are knowledge conflicts. In these situations, the system should abstain.
>
> • The model knowledge perspective examines the capabilities of the AI model itself, including its design, training, and inherent biases. For any given query, the system should abstain if the model is insufficiently confident about the correctness of output or has a high probability of returning an incorrect output.
>
> • The human values perspective considers ethical implications and societal norms that influence whether a query should be answered, emphasizing the impact of responses on human users. A system should abstain if asked for personal opinions or values (i.e., the query anthropomorphizes the model), or if the query or response may compromise safety, privacy, fairness, or other values."

**Page/section**: Section 2.1 (Abstention Framework)
**Why it matters**: The three-axis taxonomy is the most directly applicable theoretical scaffold for the pilot. The pilot's identity-triggered refusal is *not* a query-axis abstention (the query is the same), *not* a model-knowledge abstention (the model has the knowledge, as proven by abliteration), but a *human-values-axis abstention conditioned on declared user identity*. This is the apparatus for arguing that the pilot's D-experiment finding is theoretically intelligible but empirically novel.

### Passage 4 — for Q4-KG (formal definition)
> "To formalize our definition of abstention: consider an LLM f : X → Y. When given a prompt x ∈ X, f generates a response y ∈ Y. We model refusal to answer (abstention) as a function r : X, Y → [0, 1] where r(x, y) = 1 indicates the system will fully abstain from answering, r(x, y) = 0 indicates the system will return the output y, and intermediate values represent partial abstention."

> "We define r as the conjunction of three functions, to be defined by a system designer, to assess query answerability, the confidence of the LLM's response to the query, and the human value alignment of the query and response. We define these three functions as:
> • Query function a : X → [0, 1]. a(x) represents the degree to which an input x can be answered.
> • Model confidence function c : X, Y → [0, 1]. c(x, y) indicates the model f's confidence in its output y based on input x.
> • Human value alignment functions h : X, Y → [0, 1]. We define two variants of h: h(x) operates on the input alone and determines its alignment with human values, and h(x, y) operates on both the input x and predicted output y."

**Page/section**: Section 2.2 (Problem Formulation)
**Why it matters**: A formal mathematical decomposition of the refusal function. The pilot's finding can be expressed within this framework as h(x|identity=T) ≠ h(x|identity=∅) — the human-values function is conditioned on identity context, not just query content.

### Passage 5 — for Q4-KG (five major types of abstention expression)
> "For the abstention expression—the words a model uses to convey that it has abstained—we adopt the definition of five major types of expressions from prior work (Varshney et al., 2023; Wang et al., 2024c), indicating that the model (i) cannot assist; (ii) refutes the query; (iii) provides multiple perspectives without expressing preference; (iv) perceives risk associated with the query and answers cautiously with a disclaimer; and (v) refuses to offer concrete answers due to the lack of knowledge or certainty."

**Page/section**: Section 2 (Abstention in LLMs)
**Why it matters**: The pilot's "我还没有学会" template is type (v) — feigned epistemic absence. The pilot's compressed-length CCP-framed responses are type (iv) — "cautious answer with disclaimer". Both are within the survey's taxonomy.

### Passage 6 — for Q1-MT (multi-turn context awareness — explicitly identified as gap)
> "Context awareness: Existing work focuses on query-only processing or simple context-dependent tasks where insufficient or conflicting context may be provided in the abstention scenario. These settings overlook context complexity in real-world applications; for example, earlier context in multi-turn conversations can impact judgments for either query answerability or human values alignment in later conversational turns."

**Page/section**: Section 3.3.1 (Query Processing Summary box)
**Why it matters**: **Direct quotable acknowledgement that earlier multi-turn context affects later-turn abstention decisions — and that this is under-studied.** This is the strongest possible anchor for the pilot's L1 conversation-layer threat model. Authoritative survey (TACL 2025) explicitly identifies the gap the pilot fills.

### Passage 7 — for Q4-KG (over-abstention is a recognized concern)
> "Researchers disagree on whether instruction tuning helps LLMs learn abstention as a meta-capability."

> "SFT can make models more conservative, leading to a higher number of incorrect refusals."

> "Preference optimization may still lead to over-abstention if reward models overemphasize safety or preference data favors abstention."

**Page/section**: Instruction Tuning Summary box / Learning from Preferences Summary
**Why it matters**: Over-refusal is recognized in the literature as a calibration problem. The pilot's finding that the model refuses the *correct* answer (228 Event) when a Taiwanese identity is declared is a specific instance of harmful over-abstention conditioned on user identity — a sub-class the survey acknowledges in general but does not enumerate.

## Structural content worth knowing

- **Figure 1**: The framework diagram showing the abstention pipeline: Input x → query function a(x) → human value h(x) → model c(x,y) → human value h(x,y) → Abstain decision. Useful for the Drafter to visualize where identity-triggered abstention sits.
- **Figure 2**: Method taxonomy tree organized by lifecycle stage (Pretraining / Alignment / Inference) × technique. ~150+ papers organized into a tree.
- **Summary boxes** at the end of each subsection give bottom-line takeaways and open research directions. Several are quotable.
- The survey is explicitly framed as identifying gaps, with multiple "future research" callouts — Drafter can position the pilot's findings as filling identified gaps.
- **No explicit treatment of identity-conditioned, geopolitical, or cross-cultural abstention.** This absence is itself the strongest evidence that the pilot's framing is novel.
- ~150+ references; can serve as the canonical anchor citation for any abstention claim.

## Caveats / limitations

- **Survey, not empirical study**. Drafter cannot cite numbers from c066 — only the taxonomic framework and gap identifications.
- The three-axis framework is normative ("a system *should* abstain if..."). The pilot observes that systems *do* abstain in ways the framework does not anticipate (specifically, h(x) conditioned on declared identity). Drafter's contribution lies in showing the framework's blind spot.
- No mention of Chinese-origin LLMs or politically sensitive topics. The survey is in English and US/UW-centric; cross-cultural abstention is acknowledged elsewhere but not in this survey.
- The "context awareness" gap is identified but not deeply theorized — it is a single sentence in a summary box. Drafter should not over-claim that Wen et al. "theorize" context-dependent abstention; they *flag* it.
