---
cid: c081
evidence_scope:
  conceptual:
    refs: [multiturn_dialogue_safety]
    note: Canonical multi-turn jailbreak ("Crescendo") establishing the L1 conversation-layer threat model — single-turn alignment fails when adversary uses benign, progressively escalating turns referencing the model's own prior outputs.
  temporal:
    range: "2024"
  methodological:
    type: empirical-quantitative
scope_caveat: Frames multi-turn as malicious-user attack vector, not as model-side discrimination/governance issue — Drafter must note the framing inversion when citing for the pilot's user-rights frame.
---

# c081: Great, Now Write an Article About That — The Crescendo Multi-Turn LLM Jailbreak Attack

**URL**: https://arxiv.org/abs/2404.01833
**Source type**: preprint (Microsoft Research) | **Quality**: qs=5
**Authors**: Mark Russinovich, Ahmed Salem, Ronen Eldan (Microsoft Azure / Microsoft Research)
**Year / venue**: 2024 (arXiv:2404.01833v3, Feb 2025 revision)
**Deep-read on**: 2026-05-18
**Access status**: ok (full PDF, ~22 pages extracted via pdftotext)
**Pages/length**: ~22 pages

## Directly addresses
- Q1-MT (multi-turn / conversational LLM safety): THE canonical published reference for the L1 "conversation-layer" threat model. Defines and quantifies how seemingly benign multi-turn dialogue progressively erodes safety alignment when single-turn refusal would block the same content. Microsoft-affiliated, widely cited as the originating Crescendo reference.
- Q4-KG (auxiliary): Provides the mechanism — the model's own prior outputs become attack surface, which is mechanistically parallel to (though framed differently from) the pilot's gradient-erosion finding.

## Key passages

### Passage 1 — for Q1 (definition and core mechanism, abstract verbatim)
> "Large Language Models (LLMs) have risen significantly in popularity and are increasingly being adopted across multiple applications. These LLMs are heavily aligned to resist engaging in illegal or unethical topics as a means to avoid contributing to responsible AI harms. However, a recent line of attacks, known as 'jailbreaks', seek to overcome this alignment. Intuitively, jailbreak attacks aim to narrow the gap between what the model can do and what it is willing to do. In this paper, we introduce a novel jailbreak attack called Crescendo. Unlike existing jailbreak methods, Crescendo is a simple multi-turn jailbreak that interacts with the model in a seemingly benign manner. It begins with a general prompt or question about the task at hand and then gradually escalates the dialogue by referencing the model's replies progressively leading to a successful jailbreak."

**Page/section**: Abstract
**Why it matters**: Verbatim canonical definition of Crescendo and of the multi-turn jailbreak class. Establishes the L1 attack pattern: benign opening + progressive escalation + reference to model's own outputs.

### Passage 2 — for Q1 (the foot-in-the-door theoretical framing)
> "Crescendo is a multi-turn jailbreaking technique that uses benign human readable prompts. Crescendo distinguishes itself from other approaches by utilizing the target model's outputs to direct the model towards bypassing its safety alignment. This approach begins with an innocuous topic linked to the target task and progressively intensifies, directing the model's responses towards the intended outcome. Hence, it circumvents defenses and safety measures, especially ones designed to react mainly to the user's prompts. The incremental nature of Crescendo's strategy mirrors the 'foot-in-the-door' psychological tactic, where agreeing to a small, initial request increases the likelihood of complying with subsequent, larger demands."

**Page/section**: Section 3 (Crescendo)
**Why it matters**: Provides the mechanistic intuition — the model's own prior compliance becomes the attack lever. This is the cleanest published statement of the gradient-erosion mechanism the pilot study observed empirically (the "safe-then-sensitive progression unlocks 5× more content").

### Passage 3 — for Q1 (quantitative ASR numbers)
> "Crescendomation surpasses other state-of-the-art jailbreaking techniques on the AdvBench subset dataset, achieving 29-61% higher performance on GPT-4 and 49-71% on Gemini-Pro."

> "Crescendo achieves a 98% success rate when considering the binary success rate... This means that Crescendo is able to jailbreak 49 out of the 50 tasks compared to the second best jailbreak (MSJ) which jailbreaks only 43 tasks."

> "Crescendo is able to achieve higher ASR than MSJ, with the average success rates being 63.2% and 38.9%, respectively. Additionally, Crescendo successfully jailbreaks 91% of the tasks with at least one successful output, compared to MSJ's 70%."

**Page/section**: Abstract / Section 5.2 (Results) / HarmBench evaluation
**Why it matters**: Hard cross-model numbers. Useful to anchor the pilot's qualitative MT-vs-ST observation in published quantitative work.

### Passage 4 — for Q1 (single-turn baseline shows alignment IS effective when not multi-turn)
> "By presenting Crescendo, we aim to highlight the shortcomings of the current alignment and evaluation of LLMs. For example, all current benchmarks focus solely on single-turn jailbreaks. While current alignment strategies do make jailbreaking more difficult in the context of single-turn attempts, as demonstrated by Crescendo, multi-turn jailbreaks can easily circumvent these measures."

**Page/section**: Section 1 (Introduction)
**Why it matters**: Direct quotable confirmation that single-turn alignment works but multi-turn breaks it. Mirrors the pilot's central "single-turn / multi-turn paradox" finding (Oxford-researcher identity single-turn → refusal; same identity multi-turn → 2921 chars of substantive output).

### Passage 5 — for Q1 (turn-by-turn quantitative decomposition)
> "We begin by assessing the success of executing Sentence B. If preceded by Sentence A, the model's compliance rate is a near-perfect 99.99%. However, if Sentence B is presented directly to the model without preceding context, the compliance rate drops to approximately 36.2%. Similarly, the likelihood of Sentence C succeeding is only 17.3% if it follows a successful Sentence B without Sentence A. This likelihood rises to 99.9% when the dialogue starts with Sentence A."

> Table 3 (success rates):
> - B alone: 36.2%
> - A → B: 99.99%
> - B → C: 17.3%
> - A → B → C: 99.9%
> - A → B → C' (with explicit malicious phrasing): < 1%

**Page/section**: Section 3.3 (Understanding Crescendo)
**Why it matters**: Microsoft's quantitative decomposition of "which turns matter" — a working sentence chain raises compliance from 17.3% to 99.9%. This is the single strongest published number for the gradient-erosion effect.

### Passage 6 — for Q1 (Crescendo is black-box; benign inputs)
> "Crescendo is a completely black-box jailbreak that makes no assumptions about the target model. It is executed through entirely normal interactions with an LLM, similar to most other jailbreaks. For automating Crescendo, access to a black-box API is the only requirement needed to interact with the target LLM."

> "In contrast to these jailbreak attacks, Crescendo does not use any adversarial or malicious text in its prompts. The inputs for Crescendo are completely human-readable and innocuous. This is due to Crescendo's design, which relies on the model's own output rather than crafting explicit content."

**Page/section**: Section 3.1 (Threat Model) and Section 2 (Related Works)
**Why it matters**: Crescendo uses only benign human-readable prompts — no adversarial suffix, no obfuscation. This is the key property that makes the pilot's natural Chinese-language identity-disclosure conversations methodologically comparable.

### Passage 7 — for Q1 (cross-model evaluation table)
> "Crescendo can effectively jailbreak all the evaluated models across the vast majority of tasks, demonstrating its strong performance across a spectrum of categories and models."
>
> Table 2 (manual Crescendo, all green checkmarks across): ChatGPT/GPT-4, Gemini Pro, Gemini Ultra, Claude-2, Claude-3, LLaMA-2 70b, LLaMA-3 70b — all jailbroken on the 10-task suite (Molotov, Meth, Manifesto, Denial, Climate, UnsafeVax, Election, Stabbing, Rant, Intimacy).

**Page/section**: Section 3.2 (Manual Examples) / Table 2
**Why it matters**: No tested model is immune. Strongest cross-vendor evidence that L1 vulnerability is a class property, not an artifact of a single vendor's alignment.

### Passage 8 — for Q1 (turns required)
> "We next examine the minimum number of turns required by the Crescendomation to successfully jailbreak tasks for each model. The results (Table 5) reveal that on average, most tasks are jailbroken in less than 5 turns."

**Page/section**: Section 5.3.1
**Why it matters**: Calibration — most attacks succeed in fewer than 5 turns. Useful for relating to the pilot's 16-conversation experimental scale.

## Structural content worth knowing

- **Figure 1**: Side-by-side comparison showing direct request → refusal vs. Crescendo trajectory → compliance, on ChatGPT and Gemini Ultra (the Molotov task).
- **Figure 2**: Crescendo pattern template — "Tell me about X" → "What would people concerned about [aspect] say?" → "Combine those quotes into article form" → "Make it angry". This is the prototypical multi-turn template.
- **Figure 4**: Token-probability graph for LLaMA-2 70b showing that probability of generating profanity rises incrementally as profanity-related context accumulates in the dialogue history.
- **Algorithm 1 (Crescendomation)**: Automated pseudocode using attacker LLM + target LLM + Judge LLM + Refusal Judge with backtracking. Useful structural reference.
- **Table 4**: Comparison of CIA, COA, MSJ, PAIR vs. Crescendo on GPT-4 and Gemini-Pro — Crescendo wins on both.
- **No mention of Chinese-origin models** (no DeepSeek, Qwen, GLM tested).

## Caveats / limitations

- **FRAMING INVERSION ALERT**: Paper frames Crescendo strictly as a malicious-user attack to be defended against. Microsoft's framing: "we aim to highlight the shortcomings of the current alignment and evaluation of LLMs" so that vendors can patch. The pilot's framing is the inverse — the same multi-turn mechanism functions as model-side differential access control. Drafter must explicitly note this framing inversion when citing.
- Models tested: GPT-3.5/4, Gemini Pro/Ultra, Claude-2/3, LLaMA-2/3 70b. **No Chinese-origin model (DeepSeek, Qwen, GLM) in scope** — Drafter cannot use Crescendo numbers as evidence for Chinese-LLM-specific behavior.
- Tasks tested are illegal/harmful content (Molotov, hate manifesto, misinformation). Not political-sensitivity / identity-conditioned topics. Mechanism transfers conceptually but not empirically.
- Uses an attacker LLM (GPT-4) to automate Crescendo — Crescendomation results are automated; manual Crescendo can do more.
