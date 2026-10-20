# LLM reasoning methods: subfields

This field studies how to make a language model reason better without changing its architecture. It divides by where the gain comes from: the prompt (chain of thought), the amount of compute at test time (sampling, voting, search), the training signal (reinforcement learning on verifiable rewards), and the checking step (verifiers and self-correction). It is mostly empirical, so it is our best source of measured results and a weak source of theory. Marks: [V] = page opened this session; [M] = from memory, or seen only in a search result, so no numbers are quoted from it.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Chain-of-thought prompting | Writing intermediate steps before the answer | Wei et al. 2022, arXiv 2201.11903 [V] | Med | background; G11 (think briefly), G10 (text is not evidence) |
| Sampling and voting (self-consistency) | Sample many paths, take the most frequent answer | Wang et al. 2022, arXiv 2203.11171 [V] | High | S3 GENERATE, S7 SELECT (code selects) |
| Test-time compute scaling | Spending more tokens or samples per problem | Survey arXiv 2501.02497 [M] | High | control: S0 gate, budget by difficulty (G12) |
| Verification design | Verifiers: prompt-based, fine-tuned discriminative or generative; checking steps, outcomes or both | Survey arXiv 2508.16665 [V] | High | S4 TEST, S8 VERIFY |
| Self-correction | Whether a model can fix its own errors | Kamoi et al. critical survey, arXiv 2406.01297 [V] | High | G2 (revise from real output), S5 |
| Learned refinement and self-verification | Training a model to decide when to refine | ReVISE, arXiv 2502.14565 [M] | Med | S5 trigger |
| Search over thoughts | Tree and graph search over steps | Tree of Thoughts (see C05) | Med | S6 idea tree |
| Adaptive stopping, metareasoning | When to stop thinking | arXiv 2410.05563 [V]; CaRT arXiv 2510.08517 [V] | High | S0 gate, S6 trigger (see C12) |
| RL on verifiable rewards | Training for longer, better reasoning | DeepSeek-R1 line [M] | Low | background only (we do not train) |
| Overthinking | Extra tokens lowering accuracy | alphaxiv 2604.10739 [M] | High | G11 |

## Dig into next

1. **Verification design.** Which verifier type (symbolic or executable, generative, prompt-based) has the best true-positive rate per token on our task classes? Does a verifier that sees no authorship and no proposed answer (G5) keep its accuracy? Evidence: per-class verifier precision and recall at equal tokens on our suites.
2. **Self-correction with external feedback.** How much of an S5 gain comes from the located failing output, versus a fresh resample at equal tokens? Evidence: three-arm ablation (located output, generic "try again", fresh resample).
3. **Voting and its limits.** At what number of short attempts does agreement stop adding accuracy for a class? Evidence: accuracy against number of samples on our logs (G4 says samples are correlated).

## Combined with LLMs

This field is the LLM work. Opened papers:
- Chain-of-thought (Wei et al.): exemplars with steps; a 540B-parameter model (name not shown on the page) with eight exemplars reached state of the art on GSM8K, beating a fine-tuned GPT-3 with a verifier. Tasks: arithmetic, commonsense, symbolic [V].
- Self-consistency (Wang et al.): gains over chain of thought of +17.9 (GSM8K), +11.0 (SVAMP), +12.2 (AQuA), +6.4 (StrategyQA), +3.9 (ARC-challenge); the page does not say if absolute or relative, and names no model beyond PaLM and UL2 in later versions [V].
- Self-correction survey: no prior work shows successful self-correction from prompted-LLM feedback except on tasks unusually suited to it; it works with reliable external feedback; large-scale fine-tuning enables it. No numbers on the page [V].
- Verification survey: gives the verifier taxonomy but no measured results on its abstract page [V].
- Rational metareasoning (arXiv 2410.05563): a value-of-computation reward with Expert Iteration gives 20 to 37 percent fewer tokens than few-shot chain of thought and STaR across three unnamed models on unnamed datasets, with performance "maintained" and no accuracy figures on the page [V].
- CaRT: counterfactual stop/continue fine-tuning improves information-gathering efficiency and success on medical diagnosis and math; no numbers or model names on the page [V].
These agree with G2 and G11. I did not read full texts for the tables.

## Sources

1. https://arxiv.org/abs/2201.11903 [V] Chain-of-thought prompting
2. https://arxiv.org/abs/2203.11171 [V] Self-consistency
3. https://arxiv.org/abs/2406.01297 [V] When can LLMs correct their own mistakes
4. https://arxiv.org/abs/2508.16665 [V] Verification design survey (abstract page)
5. https://arxiv.org/abs/2410.05563 [V] Rational metareasoning for LLMs
6. https://arxiv.org/abs/2510.08517 [V] CaRT
7. https://arxiv.org/pdf/2501.02497 [M] Survey of test-time compute
8. https://arxiv.org/html/2502.14565v1 [M] ReVISE
9. https://www.alphaxiv.org/abs/2604.10739.md [M] When More Thinking Hurts
