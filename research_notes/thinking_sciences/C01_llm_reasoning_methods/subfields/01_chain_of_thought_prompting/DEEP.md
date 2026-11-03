# Chain-of-thought prompting: deep document

*Subfield C01.01. Writing intermediate steps before the answer. Built from evidence_a-d.jsonl (ids a01-d15), claims.jsonl (K01-K33) and critique.md in this folder. Evidence ids are cited in square brackets. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Linked subfields researched in parallel (not covered here): Monte Carlo tree search, Learned termination, Learned refinement and self-verification, Pruning of decision trees, Confidence and metacognition, Surprisingly popular method, Language as a tool for relations.*

## 1. What it is

Chain-of-thought (CoT) means the model writes its intermediate steps in text before it gives the final answer. There are three common forms.

- **Few-shot CoT.** The prompt holds a few worked examples (Wei used eight for math). Each example shows steps, then the answer. The model copies the style on a new question. [a01, b01]
- **Zero-shot CoT.** No examples. A trigger such as "Let's think step by step" is added, and a second prompt then extracts the answer. [a10, b07]
- **Trained CoT.** The model is trained (fine-tuning or reinforcement learning) to write long chains by itself. DeepSeek-R1 is the main example (AIME 2024 pass@1 79.8, GPQA Diamond 71.5). [c27] This is not prompting, but it is where the field went after 2023.

Related tools that build on it: self-consistency (sample many chains, vote) [a17], least-to-most decomposition [c12], complexity-based exemplar choice [c11], program-aided reasoning (the chain is code that an interpreter runs) [d11], scratchpads (the 2021 forerunner) [a14].

Why this matters for our agent. Our schema has two guardrails that come straight from this literature. G11 says think briefly by default. G10 says reasoning text is not evidence. This document checks both against the full record. G10 is firmly supported. G11 is supported but needs a sharper wording: brief, gated by task type and difficulty, and no "think step by step" for models that already reason.

The whole field in five lines:
1. In 2022, steps before the answer gave huge gains on math and symbolic tasks for models of about 100B parameters or more.
2. The gain comes from running serial symbolic steps, not from extra compute or from correct content.
3. For 2024-2026 models the average gain is small outside math and symbolic tasks, and can be negative.
4. The written chain often does not state why the model answered as it did.
5. Longer is not better. Shorter chains, voting over short chains, and giving more budget only to hard items all beat "think long on everything".

## 2. History and theories in depth

### 2.1 Before CoT: scratchpads (2021)

Nye et al. 2021 trained models to emit intermediate state ("scratchpad") for long addition and for tracing Python programs. [a14, a15, c13] Training used 1-8 digit addition (100k examples) and tested on 9 and 10 digits. Few-shot scratchpad for polynomial evaluation went 8.8 to 20.1; fine-tuned 31.8 to 50.7. Synthetic Python execution few-shot 11 to 26.5 (slightly relaxed criterion), fine-tuned 20 to 41.5. [a15] A warning already visible: on MBPP with only 374 tasks, scratchpad scored 5 versus 10 direct. [a16] Scratchpads needed supervised traces. CoT removed that need.

### 2.2 Few-shot CoT (Wei et al. 2022)

Eight hand-written exemplars. Greedy decoding. PaLM 540B on GSM8K: 17.9 standard to 56.9 CoT (+39.0). SVAMP 69.4 to 79.0, ASDiv 72.1 to 73.9, AQuA 25.2 to 35.8, MAWPS 79.2 to 93.3. [a02, b01, c01] This beat a fine-tuned GPT-3 with a verifier on GSM8K. StrategyQA reached 75.6 (prior best 69.4) and Sports 95.4 (human 84). [a08] Commonsense gains were uneven (CSQA minimal). Symbolic tasks (last-letter, coin flip) improved, and also generalised to longer inputs, but only for the largest model. [a08]

The paper offered an informal theory: CoT lets the model split a multi-step problem into steps, give more compute to problems that need it, give an interpretable window into behaviour, and apply to any task humans solve with language. The authors also wrote that chains may not be correct and that whether the model "reasons" was open. [a01, a09]

### 2.3 Zero-shot CoT (Kojima et al. 2022)

text-davinci-002: MultiArith 17.7 to 78.7, GSM8K 10.4 to 40.7, AQuA 22.4 to 33.5, SVAMP 58.8 to 62.1, Last Letter 0.2 to 57.6, Coin Flip 12.8 to 91.4. [a10] PaLM 540B GSM8K: zero-shot 12.5, zero-shot CoT 43.0, few-shot CoT 56.9. [a13] So a trigger phrase gives roughly two thirds of the exemplar gain. Wording was fragile. On MultiArith: "Let's think step by step" 78.7, "First," 77.3, "Let's think" 57.5, "Don't think. Just feel." 18.8, plain 17.7. [a12] Easy sets showed little gain (SingleEq 74.6 vs 78.0; CommonSenseQA 68.8 to 64.6, a drop). [a11]

### 2.4 Self-consistency, the first big add-on (Wang et al. 2022)

Sample 40 chains at temperature, take the majority answer. PaLM 540B GSM8K 56.5 to 74.4 (+17.9); SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-challenge +3.9. [a17, b08, c07] Agreement between chains correlated with accuracy, so vote share is a confidence signal. [a18] Cost is about 40 times the tokens. Note: this paper's own greedy baseline is 56.5, not Wei's 56.9 (a re-run). Do not mix the two in one table. [critique]

### 2.5 Harder suites and human comparison (Suzgun et al. 2022)

BIG-Bench Hard (23 tasks). Average human rater 67.7. PaLM answer-only 52.3 to CoT 65.2; Codex 56.6 to 73.9 (algorithmic tasks 45.9 to 74.4). Tasks above the average human: PaLM 0 to 10 of 23, Codex 5 to 17 of 23. CoT also turned flat scaling curves into rising ones on several tasks. Algorithmic tasks gained far more than NLP tasks. [a19, a20, c08] Some tasks gained nothing or lost.

### 2.6 Why does it work? First wave of mechanism studies (2022)

- **Madaan and Yazdanbakhsh 2022.** Counterfactual prompts on four tasks. Math: direct 10.11, CoT 27.37, abstract-symbol prompts 25.70 and 28.20. Wrong equation patterns: GSM8K 24.39 (about equal to CoT). Removing the text hurt; swapping sport and person on Sports fell 93.67 to 52.96. Conclusion: text carries commonsense and context, symbols help format; exact numbers matter little. [a21, a22, c09]
- **Wang et al. 2022 (Towards understanding).** GSM8K, text-davinci-002: standard 15.4, CoT 48.5, invalid-reasoning exemplars 39.5 (80-90% of the CoT gain kept). Remove coherence (shuffle steps) 23.1. Remove relevance 11.0, below standard. So relevance to the query and step order are the levers; step correctness is not. [b09, b10, c10]
- **Wei ablations.** Equation-only, filler dots of equal length, and reasoning placed after the answer did not reproduce the GSM8K gain. [a05, b04, c03]
- **Complexity-based prompting (Fu et al.).** Exemplars with more steps give +5.3 on average, up to +18. [c11] **Least-to-most (Zhou et al.).** SCAN: at least 99% with 14 exemplars versus 16% for CoT (code-davinci-002). [c12]

### 2.7 Theory of why steps add power

Transformers without intermediate tokens sit near TC0. With log(n) steps they gain little. Linear steps recognise all regular languages. Polynomial steps reach P. [a34, b28, c26] Feng et al. show direct prediction of some arithmetic and equation tasks fails while CoT-trained models succeed. [c25] Practical reading: when a task needs serial depth, written steps add real power. When it is parallel or a lookup, they add nothing. Pfau et al. found trained toy transformers can use meaningless filler (dots) on two hard algorithmic tasks, but only with dense supervision. [b27] Pretrained chat models get no gain from filler. [a26, b14]

### 2.8 The faithfulness wave (2023-2025)

- **Turpin 2023.** Biasing features change answers but the chain never mentions them. [a23-a25]
- **Lanham 2023.** Truncate the chain, add mistakes, insert filler, paraphrase, and see if the answer moves. [a26, a27, b14, b15, c20]
- **Chen 2025, Chua and Evans 2025, Arcuschin 2025.** The same question for reasoning models and, without any hint, for production models. [b16, b17, c21, c22, d13]

### 2.9 The "is it still worth it?" wave (2024-2026)

- **Sprague et al. 2024/2025.** A meta-analysis of 100+ papers plus own tests on 20 datasets and 14 models. [a28-a30, b18-b20, c14, c15]
- **Liu et al. 2024.** Tasks where verbal thinking hurts humans. [b22-b24, c16]
- **Meincke et al. 2025.** GPQA Diamond, many trials, modern chat and reasoning models. [a31, a32, b25, b26]
- **Overthinking and inverse scaling.** [b29, b30, d01, d04, d05, d07]
- **Illusion of thinking and its rebuttal.** [b31, b32, d14, d15]

### 2.10 Competing explanations for the CoT effect

| Explanation | Supports | Against |
|---|---|---|
| Extra compute (more tokens) | Theory: more steps raise expressive power [a34] | Filler tokens give no gain in pretrained models [a26, b14]; reasoning after the answer gives none [a05] |
| Serial symbolic execution | Gain concentrated on math and symbolic; up to 95% of MMLU gain on "=" questions [a28, b19]; tools beat text execution [a30, d11] | Gains also on StrategyQA and MuSR [a29, b19] |
| Planning / decomposition | Least-to-most, complexity prompts [c11, c12] | Sprague: CoT mainly helps execution, not planning [b20] |
| Format and relevance, not correctness | Invalid exemplars keep 80-90% [b09]; wrong-answer samples cost little in fine-tuning [d12] | Fine-tuning evidence only [d12] |
| Latent ability that prompts only reveal | CoT-decoding finds chains in top-k branches (GSM8K PaLM-2 L 34.8 to 63.2) [a33, c24] | Needs decoding access |
| Post-hoc story, not the cause | Faithfulness failures [a23, b16] | Ablations show chains carry the computation on math [a05] |

Synthesis: on math and symbolic tasks the text does computation (serial steps matter, order and relevance matter, filler does not). Elsewhere the text is often a story that follows the answer. Both are true at once, which is why G10 and G11 belong together.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Few-shot CoT lifts large models on multi-step math | PaLM 540B GSM8K 17.9 to 56.9 (+39.0); Codex 19.7 to 63.1; GPT-3 175B 15.6 to 46.9; SVAMP 69.4 to 79.0; MAWPS 79.2 to 93.3 | Wei 2022 [a02, b01, c01] | [E] (K01) |
| Bare trigger gives much of the gain | text-davinci-002 MultiArith 17.7 to 78.7; GSM8K 10.4 to 40.7; PaLM 540B GSM8K 12.5 to 43.0 | Kojima 2022 [a10, a13] | [E] (K02) |
| Needs scale (2022 models) | LaMDA GSM8K standard/CoT: 420M 2.6/0.4; 8B 3.2/1.6; 68B 5.7/8.2; 137B 6.5/14.3. AQuA 137B 25.5 to 20.6 | Wei 2022 [a03, b02] | [E] (K03), historical |
| Gain grows with difficulty; easy items flat or negative | SingleOp negative or tiny; CSQA 68.8 to 64.6; BBH algorithmic +28.5 vs NLP +7.1 to +10.4 | Wei, Kojima, Suzgun [a04, a11, a20, b03] | [E] (K04) |
| Chain must come before the answer and be in words | Dots, equation-only (on GSM8K), after-answer: about baseline | Wei ablations [a05, b04, c03] | [E] (K05) |
| Filler tokens give nothing in pretrained models | No gain at any length on 8 tasks | Lanham 2023 [a26, b14] | [E] (K06) |
| Self-consistency adds large gains | PaLM GSM8K 56.5 to 74.4 (+17.9); SVAMP +11.0; AQuA +12.2; StrategyQA +6.4; ARC-c +3.9; about 40x tokens | Wang 2022 [a17, b08, c07] | [E] (K07) |
| Vote share is a confidence signal | Zero-shot CoT 43.0 to 69.2 with 40 paths. CISC: over 40% fewer samples. Adaptive-Consistency: up to 7.9x fewer at under 0.1% loss | Wang; Taubenfeld; Aggarwal [a18, d09, d10] | [S] (K08) |
| Exemplar correctness is not the main lever | GSM8K standard 15.4, CoT 48.5, invalid 39.5, no coherence 23.1, no relevance 11.0 | Wang 2022b [b09, b10] | [E] (K09) |
| Text matters more than symbols | Math direct 10.11, CoT 27.37, abstract-symbol 25.70/28.20 | Madaan 2022 [a21] | [S] (K10) |
| Trigger wording is fragile | MultiArith 18.8 to 78.7 across triggers | Kojima [a12] | [S] (K11) |
| Complexity and decomposition help | +5.3 average (up to +18); SCAN at least 99% vs 16% | Fu; Zhou [c11, c12] | [S] (K12) |
| CoT is often unfaithful | GPT-3.5 -36.3 points under suggested answer (zero-shot), -24.1 few-shot; Claude 3.7 25% and R1 39% mention used hints; misalignment hints 20% and 29% | Turpin; Chen [a23, b16] | [E] (K13) |
| Faithfulness varies by task and size | Early answering changes answer >60% on AQuA, <10% on ARC/OpenBookQA; 13B more faithful than 175B on 7 of 8 tasks | Lanham [a26, b15] | [S] (K14) |
| Harder questions, longer chains: less faithful | Unfaithful 2064 vs faithful 1439 tokens; GPQA 44% (relative) less faithful than MMLU; RL plateaus 28% MMLU, 20% GPQA | Chen 2025 [b17] | [S] (K15) |
| Reasoning models name hints more, not enough | R1 names professor cue 59%, Gemini reasoning 68%, Qwen reasoning 47%, best non-reasoning 13%; other cue types near 0% | Chua and Evans [d13] | [S] |
| CoT helps mainly math/symbolic/logic | Mean gain symbolic 14.2, math 12.3, logic 6.9; other categories 56.1 to 56.8; up to 95% of MMLU gain on "=" questions | Sprague [a28, b18, b19] | [S] (K16) |
| Gain is mostly symbolic execution | Plan plus tool solver beats CoT on average | Sprague [a30, b20, c15] | [S] (K17) |
| Modern chat models: small mean gain, more variance | Gemini Flash 2.0 +0.135 avg but -0.131 at 25/25; Sonnet 3.5 +0.117; reasoning models +0.029/+0.031/-0.033; time +35-600% / +20-80% | Meincke 2025 [a31, a32] | [S] (K18) |
| CoT lowers instruction following | 13 of 14 models on IFEval; Llama3-8B 75.2 to 59.0; Claude 3.5 Sonnet 86.5 to 79.5; Claude 3.7 90.6 vs 90.2 | Li 2025 [d06] | [S] (K31) |
| CoT can hurt on intuition tasks | GPT-4o grammar 87.5 to 64.4; faces 64.0 to 51.2; exception rounds 2.9 to 12.5 (+331%); Claude 3.5 Sonnet grammar unchanged | Liu 2024 [b22-b24] | [S] (K19) |
| Zero-shot CoT can be pulled off by a wrong hint | GPT-3.5 39.5 to 23.3; few-shot CoT 35.0 to 51.7; GSM-NoOp drops up to 65% | Turpin; Mirzadeh [a24, c18] | [E] (K20) |
| Poor transfer beyond the prompt's problem class | Blocksworld GPT-4: 59.3% with stacking-specific prompt, 3.8% zero-shot; general n-shot 6-16%; universal-algorithm CoT 37-51% | Stechly [b21, c23] | [S] (K21) |
| More thinking is not monotonic | 1,953% more tokens for 2+3; R1 uses at least 5x the tokens of Claude 3.7 for same AIME 25 accuracy; shortest chain beats longest by up to 34.5 points | Chen 2024; Balachandran; Hassid; Wu [b29, b30, d01, d04] | [E] (K22) |
| Short-m@k voting | Matches or beats majority at up to 40% fewer thinking tokens | Hassid [d01] | [S] (K28) |
| Compute by difficulty | Same accuracy as best-of-N with up to 4x less compute; search hurts on easy bins | Snell [d02] | [S] (K29) |
| Inverse scaling with distractors | Claude Opus 4 near 100% to 85-90%; R1 70% to 30% with five distractors; CatAttack error +300% R1, up to +500% reasoning, +700% instruction-tuned | Gema; Rajeev [d05, d07] | [E] (K30) |
| Perturbed items cut CoT accuracy | GPT-3.5 CoT 74.17 on GSM8K to 62.92 on GSM-Plus, 40.83 critical-thinking subset | Li 2024 [d08] | [S] (K33) |
| Tool execution beats written execution | GSM-Hard: CoT 65.6 to 20.1, PAL 72.0 to 61.5; GSM8K majority@40 PAL 80.4 vs Minerva 78.5 | Gao 2023 [d11] | [S] (K32) |
| Collapse at high complexity | Three regimes: low complexity non-thinking better; medium thinking wins; high both collapse. Rebuttal: output cap, impossible River Crossing N>=6 | Shojaee; Opus and Lawsen [b31, b32, d14, d15] | [C] (K23) |
| Zero-shot CoT can raise harmful output | text-davinci-003 refusal 78% direct vs 25% with CoT (one example) | Shaikh [c28] | [S] (K26) |
| Latent chains | PaLM-2 L GSM8K 34.8 to 63.2; Mistral-7B 9.9 to 25.1 | Wang and Zhou [a33, c24] | [S] (K24) |
| Expressive power theory | CoT(poly n) = P; direct near TC0 | Merrill and Sabharwal [a34, b28] | [E] (K25) |

## 4. Mechanisms and models

Written so an engineer can build each piece.

### 4.1 The basic pipeline

1. Build a prompt: instruction, optional exemplars (each: question, steps, "The answer is X"), the new question.
2. Add a trigger for zero-shot ("Let's think step by step") or let the exemplars set the style.
3. Generate. The model writes steps, then an answer line.
4. Extract the answer with a fixed parse rule. Extraction variants moved Kojima's numbers by several points. [a11] Fix the extractor once and use it for every arm.
5. Optionally repeat k times at temperature and vote.

### 4.2 What the chain must contain to help

From the ablations [a05, b09, b10, a21]:
- Steps come before the answer. Reasoning after the answer is worth nothing.
- The steps are in natural language, relevant to this question, and in a coherent order.
- Individual numbers and even whole equations may be wrong with small loss (invalid exemplars keep 80-90%). Format and relevance carry most of the effect.
- Filler (dots) is worthless for a pretrained model.

Rule: if the scaffold contains worked examples, spend effort on relevance and order. Do not polish the arithmetic inside examples.

### 4.3 Self-consistency (voting over chains)

```
answers = [extract(generate(prompt, T=0.7)) for _ in range(k)]
winner = most_common(answers)
confidence = count(winner) / k
```
Cost is k times the tokens. Cheaper variants:
- **Adaptive-Consistency.** Stop sampling when the leading answer is statistically ahead (example: 9 of the first 10 agree gives over 99% chance the majority holds at 40). Budget cut up to 7.9x, accuracy loss under 0.1%, 17 datasets, 3 LLMs. [d10]
- **CISC.** Ask the model for a confidence on each chain and weight votes by it. 9 models, 4 datasets, over 40% fewer samples. Within-question discrimination matters more than overall calibration. [d09]
- **short-m@k.** Run k chains in parallel, stop when the first m finish, vote among those. Shortest chains are right more often for reasoning models. Up to 40% fewer thinking tokens. [d01]

Errors from one model are correlated, so agreement is a hint, not proof (our G4). [a17]

### 4.4 Decomposition and complexity

- **Least-to-most.** Stage 1: ask the model to list sub-questions. Stage 2: answer them in order, each answer feeding the next. [c12]
- **Complexity-based selection.** From a pool of candidate exemplars choose those with the most steps. At inference, vote only among the longest chains. [c11]

### 4.5 Plan, then execute with a tool

Sprague split a task into plan and execute. CoT helped mainly execution. Planning then handing to an interpreter or solver beat CoT on formal tasks. [a30, b20] PAL makes the chain a program:
```
program = llm("Write Python that solves: ...")
answer = run_sandbox(program)
```
It stays robust when numbers get large (GSM-Hard 61.5 versus CoT 20.1). [d11] Planning is still left to the model.

### 4.6 CoT-decoding (needs decoding access)

At the first decoded token, branch on the top-k tokens, continue each greedily, then rank paths by the model's confidence in the answer tokens. A chain exists in the top branches even when greedy decoding skips it. GSM8K PaLM-2 L 34.8 to 63.2. [a33] Not usable with an API-only backbone.

### 4.7 Faithfulness probes

All can be run on any chat API:
- **Early answering (Lanham).** Truncate the chain at step i, ask for the answer, record if it changes. If it never changes, the chain is decoration. [a26]
- **Adding mistakes.** Insert an error in a middle step, regenerate, see if the answer follows. [a26]
- **Hint injection (Turpin, Chen).** Add a cue ("a professor thinks D"). Find cases where the answer switched to the cue. Check whether the chain mentions the cue. Faithfulness = mentions / switches. [a23, b16]
- **Pair comparison (Arcuschin).** Ask "Is X bigger than Y?" and "Is Y bigger than X?". Both "yes" shows rationalisation without any hint. Up to 13% in production models, 0.37% for R1. [c22]

### 4.8 Budget control

Snell's allocation: estimate difficulty per question (verifier score or first-pass agreement), put it in one of five bins, choose the strategy per bin. Same accuracy as best-of-N with up to 4x less compute. Search hurt on easy bins and did little on the hardest. [d02] The overthinking paper says the first solution round usually already holds the right answer; stop there on easy items. [b30]

### 4.9 Why long chains go wrong (working models)

- Inverted U in chain length: error from too few steps falls, error from accumulated slips and distraction rises. Optimal length grows with difficulty and shrinks as models get stronger. [b29]
- Under distractors, longer reasoning gives more room to attend to irrelevant text (Claude Opus 4, R1). [d05]
- For instruction following, CoT shifts attention away from constraint words (attention analysis, correlational). [d06]

## 5. What holds up

### 5.1 Replications

- Wei's PaLM GSM8K 56.9 was re-run by Wang et al. as 56.5 greedy. [critique, a17] Same level.
- Kojima's trigger effect reproduces on PaLM 540B GSM8K (12.5 to 43.0). [a13]
- Suzgun extended CoT to 23 hard BBH tasks; PaLM +12.9, Codex +16.7. [a19]
- Self-consistency gains reproduce across Codex, PaLM and other families. [a17, d09, d10]
- Turpin's finding that chains omit the bias reproduces on newer reasoning models (25% / 39% mention rates) [b16] and, with no hint, in production models (up to 13%). [c22]
- Inverse scaling with distractors appears in models from several vendors. [d05, d07, d08]

### 5.2 Failed or limited replications

- **Small-model CoT.** In 2022 pretrained models below about 100B, CoT scored below standard prompting. [b02, a03] Later small models trained on reasoning data do benefit. [b02] For a strong backbone this is history.
- **Commonsense.** CSQA gains minimal or negative; Kojima's CSQA fell 68.8 to 64.6. [a11] Sprague finds non-math categories 56.1 to 56.8. [b18]
- **Planning.** Blocksworld gains collapse as stack size grows; self-consistency lowered performance there. [b21, c23] A broad algorithm prompt did help (37-51%) but not at larger sizes.
- **Faithfulness trend.** Lanham 2023 saw larger models less faithful; Chen 2025 saw outcome RL raise faithfulness then plateau. Different measures, not directly comparable. [critique]
- **Collapse claim.** Shojaee's high-complexity collapse is disputed (output cap, impossible instances). No larger-budget rerun found. [d14, d15] [C]
- **Meincke vs older results.** Not a true contradiction; model era differs. But the 2022 headline overstates today's benefit. [critique]

### 5.3 Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Task type | Math, symbolic, logic gain; knowledge recall and commonsense flat | [b18, b19] |
| Number of steps / difficulty | More steps, more gain | [a04, b03, a20] |
| Baseline headroom | Near-ceiling sets gain little (easy MAWPS subsets) | [a04] |
| Model scale (2022) | Gain only at about 100B+ | [b02] |
| Model era | Modern chat models already reason by default, so explicit CoT adds little | [a32, b26] |
| Shot count | Few-shot CoT reduces bias sensitivity; zero-shot can increase it | [a23, a24] |
| Trigger wording | 18.8 to 78.7 | [a12] |
| Prompt specificity | Blocksworld: specific prompt 59.3, general 6-16 | [b21, c23] |
| Distractors / perturbation | Longer reasoning hurts | [c18, d05, d07, d08] |
| Instruction constraints | CoT hurts format compliance | [d06] |
| Intuition / statistical learning | Verbal deliberation hurts | [b22-b24] |

### 5.4 Interventions that worked

- Exemplars with natural-language steps before the answer (K01, K05).
- Zero-shot trigger (K02).
- Voting over chains, especially with adaptive stopping or confidence weighting (K07, K08).
- Shortest-first selection among chains of a reasoning model (K28).
- Allocation of compute by difficulty (K29).
- Giving execution to a tool (K17, K32).
- Few-shot CoT rather than zero-shot when a wrong hint is likely (K20).
- One "ignore irrelevant information" line cut attack success 37.5% to 9.9% on one 8B model (not token matched). [d07]
- Classifier-selective reasoning on instruction following recovered most of the lost accuracy. [d06]

### 5.5 Interventions that did not work

- Filler tokens / "variable compute" in pretrained models. [a26, b14, a05]
- Reasoning after the answer. [a05]
- Self-consistency on Blocksworld (it lowered accuracy). [b21]
- Explicit "think step by step" on models that already reason: about zero gain, 20-80% more time. [a32, b26]
- Reading the chain as a record of the cause. [a23, b16, d13]

## 6. Language models

### 6.1 Timeline of behaviour

| Era | Typical behaviour | Numbers |
|---|---|---|
| 2021 | Scratchpad needs supervised training | Polynomial evaluation few-shot 8.8 to 20.1 [a15] |
| 2022 | Prompted CoT emerges at about 100B+; huge math gains | PaLM GSM8K +39.0; GPT-3 175B +31.3; LaMDA 137B +7.8; UL2 20B +0.3 [a02] |
| 2023 | Faithfulness doubts; bias sensitivity | GPT-3.5 -36.3 under suggested answer [a23] |
| 2024 | CoT concentrated on math/symbolic; hurts on some intuition tasks; planning transfer weak | Mean +12.3 math, +14.2 symbolic, +6.9 logic, other +0.7 [b18]; GPT-4o grammar -23.1 [b22] |
| 2025 | Reasoning models (RL-trained long CoT) make the prompt unnecessary; overthinking and inverse scaling become the issue | R1 AIME 24 pass@1 79.8 [c27]; explicit CoT on reasoning models +0.029/+0.031/-0.033 [a32] |

### 6.2 What changed it, by how much

- **Scale.** At 2022 sizes, LaMDA GSM8K CoT-minus-standard went from -2.2 (420M) to +7.8 (137B). PaLM 540B +39.0. [a03, a02]
- **Instruction tuning.** davinci-002-level models gained more than OPT, davinci and davinci-001, which got small to moderate gains on QA and NLI. [b11]
- **Code pretraining.** Codex gained the most in Wei (+43.4 on GSM8K) and in BBH (+16.7). [a02, a19]
- **RL for long chains.** The model writes the chain by default. Explicit prompting then adds about nothing and costs time. [a32] Faithfulness rises with outcome RL but plateaus at 28% (MMLU) and 20% (GPQA) for Claude 3.7. [b17]
- **Long chains cost.** R1 used at least 5x more tokens than Claude 3.7 Sonnet for the same AIME 25 accuracy (within 3%). [d04] Open o1-like models spent 1,953% more tokens on 2+3. [b30]

### 6.3 Behaviour by task family

- **Grade-school and competition math.** Large, reliable gains for non-reasoning models. For reasoning models the shortest sampled chain beats random by +2.2 to +15.7 and the longest by up to 34.5. [d01]
- **Knowledge QA (MMLU etc).** Up to 95% of the MMLU gain on questions with "=". Flat elsewhere. [b19]
- **Instruction following.** Negative. 13 of 14 models lose on IFEval. [d06]
- **Statistical learning, face recognition.** Negative for GPT-4o and several others; Claude 3.5 Sonnet unchanged on grammar but +129% rounds on exception learning. [b22, b23]
- **Planning (Blocksworld).** Gains need prompts specific to the problem size. [b21]
- **Distractor tasks.** Longer reasoning lowers accuracy for Claude Opus 4 (near 100% to 85-90%) and R1 (70% to 30%). o3 is more stable. [d05]
- **Safety and bias.** Zero-shot CoT raised the stereotype-aligned BBQ rate 22.1 to 26.1 (GPT-3.5) [a25]; one example refusal drop 78% to 25% [c28].

### 6.4 Caveats on this evidence base

- Most mechanism evidence is from 2022 models. [critique]
- Meincke is one benchmark (198 questions). Liu has small tasks. Sprague's own tests use zero-shot CoT prompts.
- Equal-token comparisons are rare. Most voting and long-chain gains are not token matched. [critique]
- Faithfulness studies show chains cannot be trusted as explanations. They do not show that unfaithful chains reduce accuracy. [critique]
- Sprague appears in many evidence lines but is one source. That is why several claims are rated single-source.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = stored data about problem classes.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep G10 as written: never read reasoning text as evidence of cause or correctness. Decide from checks and outputs. Add the number: reasoning models name a used hint only 25-39% of the time (47-68% best case, near 0% on some cue types). | G10 | [E] | a23, a25, b12, b16, c19, c21, c22, d13 (K13) |
| A2 | Thinking, if used, comes before the commit and is in words, relevant to the question. "Explain after answering" does not count as reasoning. | G11 / S3 | [E] | a05, b04, c03, b14 (K05, K06) |
| A3 | No filler or padding as "thinking time". Equal tokens must be real steps or nothing. | G11 / G7 | [E] | a26, b14, a05 (K06) |
| A4 | Sharpen G11: think briefly by default; the shortest chains and several short attempts beat one long one; more thinking lowers accuracy on easy items and with distractors. | G11 | [E] | b29, b30, d01, d04, d05, d07 (K22, K30) |
| A5 | S0 gate: easy or one-step items go to direct mode. CoT gain grows with steps and difficulty. | S0 / G12 | [E] | a04, a11, a20, b03 (K04) |
| A6 | In S1 input hygiene, treat misleading hints and irrelevant clauses as real threats. Keep suggestive text in a marked block; check the attempt does not follow it. | S1 / G10 | [E] | a24, b13, c17, c18, d05, d07 (K20, K30) |
| A7 | Voting is done by code over several short chains. Adaptive stopping (stop when the lead is clear) saves tokens. | G5 / S3 | [E] voting; [S] adaptive stop | a17, b08, c07, d10 (K07, K08) |
| A8 | Do not rely on exemplar correctness in scaffold examples; invest in relevance and step order. | S2 / S3 | [E] | b09, b10, c10, d12 (K09) |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Do not add "think step by step" when the backbone is a reasoning model. | G11 | [S] | a32, b26 (K18) |
| T2 | Gate thinking by task type: chains for numeric and symbolic items; none for knowledge recall and format-constrained items. | S0 | [S] | a28, b18, b19, d06 (K16, K31) |
| T3 | Short-m@k: sample k, keep the shortest m, vote. Compare with majority at equal total tokens. | S3 / G11 | [S] | d01 (K28) |
| T4 | Cheap difficulty gate (first-pass vote agreement) choosing no-think, brief, or sample-and-verify. | S0 / G12 | [S] | d02, d09, d10 (K29, K08) |
| T5 | Plan, then execute by code or solver instead of written-out execution. | S4 / O3 | [S] | a30, b20, d11 (K17, K32) |
| T6 | Vote share as a trigger for extra checking. | G1 / S4 | [S] | a18, d09, d10 (K08) |
| T7 | One-line "ignore irrelevant information" plus a short budget on perturbed items. | S1 | [S] | d07, d05 (K30) |
| T8 | Include intuition-type and statistical-learning items where thinking may hurt. | S0 | [S] | b22-b24, d06 (K19) |
| T9 | Hint-injection and early-truncation probes as an audit; a verifier step on cases the chain hides. | G10 / S8 | [S] | b16, d13, a26 (K13, K14) |
| T10 | Decomposition operator (O3) vs plain CoT on length-generalisation items. | O3 | [S] | c12, c11 (K12) |
| T11 | Use a generating program rather than full move lists for long-horizon items. | S3 | [C] | b32, d14 (K23) |
| T12 | Refusal and bias check with and without the thinking step. | G10 | [S] | c28, a25 (K26) |
| T13 | Unanswerable and contradictory items: require "cannot be answered". | S8 | [S] | d08 (K33) |

## 8. Concrete tests on our bench

For all tests: both arms get the same total token budget, counted from the API, setup included. Report accuracy, tokens, and accuracy per 1k tokens. At least three seeds. One fixed answer extractor.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 Direct vs brief vs long chain | Multi-step numeric items in 3 tiers (1-2 steps, 3-5, 6+) | Direct; brief chain (G11 cap); long chain; spend matched by varying k | Accuracy per tier; accuracy per 1k tokens | Direct wins on tier 1; brief wins on tier 2; long no better than brief on tier 3 |
| B2 Real vs filler vs after-answer | Same items | Real steps before; filler of same length; steps after answer | Accuracy | Real > filler about equal to after-answer about equal to none [a05, a26] |
| B3 One long chain vs k short + vote vs short-m@k | Math and logic items | Matched total tokens | Accuracy | k short + vote >= one long; short-m@k >= majority at about 60% tokens [d01] |
| B4 Adaptive stopping | Mix of easy and hard items | Fixed k=10 vs stop when lead is clear | Tokens saved; accuracy loss | Over 40% tokens saved with under 0.5 point loss [d10] |
| B5 Task-type gate | Numeric, knowledge recall, format-constrained | Always-think; never-think; gate by type | Accuracy and tokens | Gate matches always-think on numeric, saves tokens elsewhere; format items lose with always-think [d06] |
| B6 Hint and distractor robustness | Items with a planted wrong hint, an irrelevant clause, or "a professor thinks D" | Plain; brief chain; brief chain with hygiene block and ignore line | Accuracy; rate of following the cue; rate of citing it | Hygiene cuts cue following; citing stays low in all arms [d13] |
| B7 Hidden-cue audit | As B6 | Chain read as evidence vs independent verifier check | Detection of cue-driven wrong answers among unstated cases | Verifier catches more than reading the chain |
| B8 Tool vs written execution | Large-number arithmetic and counting | Plan + code run vs written chain | Accuracy | Tool arm wins when numbers are large [d11] |
| B9 Exemplar corruption | Items with scaffold examples | Clean; wrong digits; shuffled steps; irrelevant examples | Accuracy | Wrong digits small loss; shuffle and irrelevance large loss [b09, b10, d12] |
| B10 Intuition items | Perceptual or statistical-learning items | Direct vs chain | Accuracy | Chain no better, possibly worse [b22] |
| B11 Reasoning-backbone prompt | Mixed tasks on a reasoning backbone | With and without "think step by step" | Mean, variance, perfect-run rate, time | No mean gain; more variance [a31, a32] |
| B12 Trigger fragility | Same items | Three paraphrased triggers | Spread of accuracy | Small spread on a strong model; if large, fix one trigger |

## 9. What does not transfer, and why

- **The scale threshold** (about 100B). Our backbone is far past it. [b02]
- **Exemplar-based CoT headline numbers** (PaLM +39.0). Those baselines were low because 2022 models were not trained to reason. Modern models reach such levels without prompts. [a32, critique]
- **Self-consistency with 40 samples.** About 40x tokens; our G7 needs equal-token wins. Use adaptive stopping or short chains.
- **CoT-decoding.** Needs token-level decoding access. [a33]
- **Scratchpad training.** Needs fine-tuning. Our agent is scaffold-only. [a16]
- **Long-CoT RL results** (DeepSeek-R1). Training effects, not scaffold effects. [c27, d12]
- **Dots-as-compute in trained toy transformers.** Does not apply to pretrained chat models. [b27 vs b14]
- **Faithfulness trends with size.** Measured on specific 2023 internal models; do not extrapolate. [b15]
- **Hand-built adversarial probes** (counting with distractors, CatAttack). Worst case, not average workload. [d05, d07]
- **Blocksworld prompt specificity.** Planning domain. The general lesson is only that worked examples do not extend past their size. [b21]

## 10. Open questions

1. Equal-token test of brief vs long vs k-short-with-vote on a non-reasoning frontier model. (Reasoning-model case partly answered by [d01].)
2. Where is the knee of the budget by difficulty on current reasoning models, and does a cheap gate beat always-think? [d02 is PaLM 2 / MATH]
3. Does "think step by step" harm or help reasoning-style models across many task types beyond GPQA and IFEval?
4. Does an independent verification step catch cases where the chain hides the cue? [d13 measures only the naming rate]
5. How much gain is plan vs execution on current models, and does tool execution beat written execution at equal tokens? [d11 is 2022-era, unmatched]
6. Which tasks show CoT harm on current vendors? Statistical learning and perception rest on Liu 2024 only.
7. Do invalid-exemplar results hold in prompting for current models? [d12 is fine-tuning]
8. Does vote share work as the trigger for a separate verifier, and at what cost?
9. What happens to Shojaee's collapse with larger output budgets and impossible instances removed? [C]
10. Do clean-benchmark CoT gains survive GSM-NoOp-type perturbations on 2026 models, and does an ignore line help at equal tokens?
11. Do unfaithful chains reduce accuracy, or only mislead readers?
12. Wei's symbolic appendix values (49.3 to 98.6 and similar) are unconfirmed because column labels were garbled in extraction. [c04, critique]

## 11. Sources

All urls were opened by first-pass agents (opened:true in the evidence files). The cross-check re-opened the full text of 11 papers (Wei, Kojima, Wang, Sprague, Turpin, Liu, Chen 2025, Wang and Zhou, Meincke, Suzgun, Stechly). The gap search opened 12 more (d01-d15). Not re-opened in the cross-check, so resting on first-pass reading: Nye, Madaan, Lanham, Shi, GSM-Symbolic, Fu, Zhou, Arcuschin, Wu, Chen 2024, Shojaee, Opus and Lawsen, Pfau, Merrill, Feng, DeepSeek-R1, Shaikh.

| Source | Mark | URL |
|---|---|---|
| Wei et al. 2022, Chain-of-thought prompting elicits reasoning in LLMs | [V] | https://arxiv.org/abs/2201.11903 |
| Kojima et al. 2022, LLMs are zero-shot reasoners | [V] | https://arxiv.org/abs/2205.11916 |
| Nye et al. 2021, Show your work: scratchpads | [V] | https://arxiv.org/abs/2112.00114 |
| Wang et al. 2022, Self-consistency | [V] | https://arxiv.org/abs/2203.11171 |
| Suzgun et al. 2022, Challenging BIG-Bench tasks | [V] | https://arxiv.org/abs/2210.09261 |
| Madaan and Yazdanbakhsh 2022, Text and patterns | [V] | https://arxiv.org/abs/2209.07686 |
| Wang et al. 2022, Towards understanding chain-of-thought prompting | [V] | https://arxiv.org/abs/2212.10001 |
| Ye and Durrett 2022, Unreliability of explanations in few-shot prompting | [V] | https://arxiv.org/abs/2205.03401 |
| Fu et al. 2022, Complexity-based prompting | [V] | https://arxiv.org/abs/2210.00720 |
| Zhou et al. 2022, Least-to-most prompting | [V] | https://arxiv.org/abs/2205.10625 |
| Shaikh et al. 2022, On second thought, let's not think step by step | [V] | https://arxiv.org/abs/2212.08061 |
| Turpin et al. 2023, LMs don't always say what they think | [V] | https://arxiv.org/abs/2305.04388 |
| Lanham et al. 2023, Measuring faithfulness in CoT | [V] | https://arxiv.org/abs/2307.13702 |
| Shi et al. 2023, LLMs easily distracted by irrelevant context | [V] | https://arxiv.org/abs/2302.00093 |
| Feng et al. 2023, Towards revealing the mystery behind CoT | [V] | https://arxiv.org/abs/2305.15408 |
| Merrill and Sabharwal 2023/24, Expressive power of transformers with CoT | [V] | https://arxiv.org/abs/2310.07923 |
| Aggarwal et al. 2023, Adaptive-Consistency | [V] | https://arxiv.org/abs/2305.11860 |
| Gao et al. 2023, PAL | [V] | https://arxiv.org/abs/2211.10435 |
| Wang and Zhou 2024, CoT reasoning without prompting | [V] | https://arxiv.org/abs/2402.10200 |
| Li et al. 2024, GSM-Plus | [V] | https://arxiv.org/abs/2402.19255 |
| Stechly et al. 2024, Chain of thoughtlessness | [V] | https://arxiv.org/abs/2405.04776 |
| Pfau et al. 2024, Let's think dot by dot | [V] | https://arxiv.org/abs/2404.15758 |
| Sprague et al. 2024/25, To CoT or not to CoT | [V] | https://arxiv.org/abs/2409.12183 |
| Mirzadeh et al. 2024, GSM-Symbolic | [V] | https://arxiv.org/abs/2410.05229 |
| Liu et al. 2024, Mind your step (by step) | [V] | https://arxiv.org/abs/2410.21333 |
| Chen et al. 2024, Do NOT think that much for 2+3=? | [V] | https://arxiv.org/abs/2412.21187 |
| Snell et al. 2024, Scaling test-time compute optimally | [V] | https://arxiv.org/abs/2408.03314 |
| Wu et al. 2025, Inference scaling laws | [V] | https://arxiv.org/abs/2408.00724 |
| Wu et al. 2025, When more is less (CoT length) | [V] | https://arxiv.org/abs/2502.07266 |
| Balachandran et al. 2025, Inference-time scaling for complex tasks | [V] | https://arxiv.org/abs/2504.00294 |
| Hassid et al. 2025, Don't overthink it | [V] | https://arxiv.org/abs/2505.17813 |
| Gema et al. 2025, Inverse scaling in test-time compute | [V] | https://arxiv.org/abs/2507.14417 |
| Li et al. 2025, When thinking fails (instruction following) | [V] | https://arxiv.org/abs/2505.11423 |
| Rajeev et al. 2025, CatAttack | [V] | https://arxiv.org/abs/2503.01781 |
| Taubenfeld et al. 2025, CISC | [V] | https://arxiv.org/abs/2502.06233 |
| Li et al. 2025, LLMs can easily learn to reason from demonstrations | [V] | https://arxiv.org/abs/2502.07374 |
| Chen et al. 2025, Reasoning models don't always say what they think | [V] | https://arxiv.org/abs/2505.05410 |
| Chua and Evans 2025, Are DeepSeek R1 and other reasoning models more faithful? | [V] | https://arxiv.org/abs/2501.08156 |
| Arcuschin et al. 2025, CoT reasoning in the wild is not always faithful | [V] | https://arxiv.org/abs/2503.08679 |
| Meincke et al. 2025, Prompting Science Report 2 | [V] | https://arxiv.org/abs/2506.07142 |
| DeepSeek-AI 2025, DeepSeek-R1 | [V] | https://arxiv.org/abs/2501.12948 |
| Shojaee et al. 2025, The illusion of thinking | [V] | https://arxiv.org/abs/2506.06941 |
| Opus and Lawsen 2025, The illusion of the illusion of thinking | [V] | https://arxiv.org/abs/2506.09250 |
