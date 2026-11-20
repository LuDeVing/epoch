# Verbal confidence: deep document

*Subfield E03.10. Stated confidence against actual accuracy. Key work: Kadavath et al. 2022. Built from evidence_a-d.jsonl (a01-a28, b01-b27, c01-c28, d01-d17), claims.jsonl (K01-K22) and critique.md in this folder. Evidence ids below are the ids in those files. "[V]" means a page or PDF was opened; "[M]" means snippet or memory only. Numbers corrected by the critique pass are used in their corrected form.*

## 1. What it is

Verbal confidence is what a model or a person says about how likely their answer is to be right. It can be a number ("70%"), a label ("medium"), or a hedge in the sentence ("I think", "probably", "definitely"). The question is whether the stated level matches the real hit rate (calibration) and whether it separates right answers from wrong ones (discrimination).

These are two different properties and they come apart.

- **Calibration.** Among answers stated at 70%, about 70% are right. Measured by ECE (expected calibration error) or Brier score.
- **Discrimination or resolution.** Right answers get higher confidence than wrong ones. Measured by AUROC (0.5 is chance) or the resolution term of the Brier decomposition.
- **Faithfulness of wording.** The hedge words in the text match the internal confidence. Measured by cMFG (0.5 is chance) in Yona et al. (a14).
- **Reader effect.** What a human or model reader does with the wording. Measured by reliance rates and reader calibration (Zhou a12, Steyvers a16, Band a23).

Four channels carry confidence out of a model. They disagree with each other.

| Channel | Example | Where it is strong |
|---|---|---|
| Token probability | P(A) over lettered options | Base models, closed options (Kadavath a01) |
| Verbalized number or label | "Confidence: 85%" | RLHF chat models (Tian a07); frontier reasoners (d04) |
| Behavioural consistency | agreement over 5 to 10 samples | Failure prediction (Xiong b09; Ghosh d05) |
| Hedge words in free text | "I'm not sure, but..." | Rarely used by models (Zhou a11) |

Why it matters for our agent. The schema already forbids using verbal confidence to stop (SCHEMA 4b, [E]) and forbids abstaining on the first pass (G6). This subfield decides what a confidence guardrail may and may not do: what to log, what to report, whether any decision may hang on a stated number, and how to word the final message.

Companion subfields (researched in parallel, not covered here): Retrieval and ensembles for LLM forecasts; Debiasing; Heuristics and biases; Imprecise credences; Evidence and probability reasoning; Social, organisational and clinical metacognition; Dual-process accounts of judgment; RL on verifiable rewards.

## 2. History and theories in depth

### 2.1 Human verbal probability

- **Kent 1964, Words of Estimative Probability (a20, [V] via Wikipedia summary only).** An intelligence analyst proposed a fixed word-to-number table. Certain 100%; almost certain 93% (plus or minus 6); probable 75% (plus or minus 12); chances about even 50% (plus or minus 10); probably not 30% (plus or minus 10); almost certainly not 7% (plus or minus 5); impossible 0%. Well received, never adopted. Original not read.
- **Wallsten, Budescu, Rapoport, Zwick and Forsyth 1986 (a18, [V]).** Phrases like "doubtful" or "probable" are scaled as fuzzy membership functions over 0 to 1. Experiment 1: 20 graduate students, pairwise comparison of spinner probabilities. Meanings are vague. People differ strongly from each other and are stable within themselves (test-retest of upper and lower limits p<0.0001). Agreement is best near 0, 0.5 and 1 and worst in between. About 67% of functions had a sensible shape. The mid-range spread is later reported as SD 11.4 to 16.6 percentage points across people (a19, snippet only, [M]).
- **Lesson for design.** A word-to-number map is a property of a person, so a reader and a writer do not share one. Fix the map per agent, with numeric anchors.

### 2.2 Human overconfidence

- Adams and Adams 1960; Lichtenstein, Fischhoff and Phillips 1982; Alpert and Raiffa; Oskamp 1965 (a21, [V] via Wikipedia only). People saying 100% are wrong about 20% of the time. 90% intervals contain the truth as little as 50% of the time. In Oskamp, more information raised confidence from 33% to 53% while accuracy stayed under 30%.
- **Hard-easy effect** (Lichtenstein 1982, b25, [M]). Overconfidence is large on hard items and shrinks or reverses on easy ones.
- **Moore and Healy 2008 (d17, [V] abstract).** Overestimation, overplacement and overprecision are three different things. Overestimation and overplacement reverse between hard and easy tasks. Overprecision is the most persistent form.
- **Erev, Wallsten and Budescu 1994 (a22, [M]).** Random error in judgement can produce both over- and underconfidence at once, depending on whether you condition on accuracy or on confidence. This is the main rival to a pure-bias account. It matters for LLMs because ECE binning can show both patterns from noise alone.
- The primary classic papers (Lichtenstein 1982, Wallsten 1986 full set) were not read in this pass (K21, open). Treat the human numbers as background, not as checked facts.

### 2.3 The LLM line, 2020 to 2022

- **Mielke et al. 2022 (b14, c04, [V]).** BlenderBot sounded sure and was mostly wrong. Vanilla 2.7B model: 4.8% accuracy on TriviaQA, answered 29.45% of questions confidently, and only 14% of those confident answers were right. A trained calibrator plus controllable generation (add hedges to match predicted correctness) lifted correctness of confident answers from 13.7% to 38.9%, by answering fewer questions confidently. First calibrator-plus-wording pipeline.
- **Lin, Hilton and Evans 2022 (a05, a06, b05, b06, c03, [V]).** First finetune of GPT-3 175B to say "61%" or "Medium". Task CalibratedMath, 21 arithmetic tasks, trained on Add-subtract (median accuracy 21%) with about 100 questions per sub-task. Tested under shift on Multi-answer (median accuracy 65%) and Multiply-divide. Corrected Table 1 (critique), MSE / MAD, lower is better:

  | Eval | Verbalized | Answer logit | Indirect logit | Constant |
  |---|---|---|---|---|
  | Multi-answer | 22.0 / 16.4 | 37.4 / 33.7 | 33.7 / 38.4 | 34.1 / 31.1 |
  | Multiply-divide | 15.5 / 19.0 | 10.4 / 9.4 | 11.7 / 7.1 | 15.3 / 8.5 |

  Verbalized wins clearly only on Multi-answer. On Multiply-divide it is worst by MAD and ties the constant on MSE. The "generalises well" claim is narrower than first recorded. A linear probe on embeddings also generalised, so the model holds a latent uncertainty signal. Meaningless label words worked slightly better than "low".
- **Kadavath et al. 2022 (a01-a04, b01-b04, c01-c02, [V]).** The founding paper for this subfield, Anthropic models up to 52B.
  - Large models are well calibrated on lettered multiple choice and on True/False. Calibration improves with size and from zero-shot to few-shot.
  - Format breaks it: swapping one option for "none of the above" cuts accuracy and calibration sharply.
  - **P(True).** The model writes an answer, then rates the chance it is true. Works few-shot on TriviaQA, Lambada, GSM8k, HumanEval, arithmetic and function synthesis. Models find their own samples plausible, so self-grading is harder than grading others. Showing many T=1 samples next to the graded one helped. More shots improved calibration, not AUROC.
  - **P(IK).** A value head trained on TriviaQA predicts "do I know this". It ranks answerable from unanswerable on new tasks (math, Lambada, code) but is poorly calibrated there. Ranking transfers better than calibration. P(IK) rose with relevant source text and with hints on GSM8k.
  - **RLHF.** RLHF policies look badly miscalibrated on token probabilities, but one temperature (T=2.5, 5-shot, MMLU, MMLU true/false, TruthfulQA) largely repairs the curves. So the damage is a scale problem, not lost information. This is the token channel only.
  - Exact ECE values are in figures only, not in text.

### 2.4 Verbalized confidence as its own channel, 2023

- **Tian et al. 2023 (a07, a08, b10-b12, c05, [V]).** RLHF chat models (gpt-3.5-turbo, gpt-4, Claude 1 and 2, Llama-2-70B-chat) on TriviaQA (1000), SciQ (1000), TruthfulQA (817). Asking in words beat the model's own token probabilities. Chain of thought did not help. See section 3 for the table and the critique correction (top-1 gain is much smaller than top-4 on SciQ and TruthfulQA).
- **Xiong et al. 2023 / ICLR 2024 (a09, a10, b07-b09, c06, c07, [V]).** Black-box benchmark: prompt strategy by sampling by aggregation, 5 models, 8 tasks. Vanilla verbal confidence clusters at 80 to 100% in multiples of 5, like human talk. Average ECE above 0.377 for GPT-3, GPT-3.5, Vicuna. GPT-4 average AUROC 62.7% (the sentence in the text is the reliable source; the same value appears in an unrelated LLaMA 2 cell). Failure prediction stays near chance for most prompts. Sampling agreement fixes it.
- **Zhou, Jurafsky and Hashimoto 2023 (b13, [V]).** On GPT-3 davinci, putting epistemic markers in the prompt changes accuracy by up to 80% on the same questions. Weakeners averaged 47% accuracy vs 40% for strengtheners; prefix "I think it's" 63% vs 80% as a suffix; 21 of 28 templates with 100% scored lower; accuracy peaked at 70 to 90%. Corpus note: certainty words appear mostly in questions, uncertainty words in answers, so models may copy usage rather than track knowledge. (The critique notes the author lists for this paper family differ between versions; cite by title.)

### 2.5 Wording, readers and the RLHF cause, 2024

- **Zhou et al. 2024, Relying on the Unreliable (a11-a13, c09, [V]).** 9 models, 49 prompts, 284 MMLU questions, 125,244 queries. Models almost never hedge (5% of base-template answers had any epistemic marker; explicit instruction 65%; CoT 16%). When prompted they over-strengthen. RLHF is the proposed cause: reward model scores plain 4.03, strengtheners 0.82, weakeners -1.86; annotators in four preference sets chose uncertain text about 8% to 9% less often.
- **Yona, Aharoni and Geva 2024 (a14, a15, b15, c08, [V]).** Faithful response uncertainty: the hedge should match the model's own consistency-based confidence. Vanilla cMFG 0.52 to 0.57 for all models. Best cell 0.70 (Gemini Ultra, PopQA, Uncertainty prompt). GPT-4-turbo 0.63 on PopQA with Uncertainty+, 0.57 on NQ.
- **Steyvers et al. 2025 (a16, a17, b16, b17, c10, c11, [V]).** Calibration gap and discrimination gap for human readers of LLM answers. N=301 (284 kept).
- **Kim et al. 2024 (c12, [V]).** Pre-registered N=404 (of 656; 38.4% excluded). First-person hedges ("I'm not sure, but...") lowered confidence and agreement and raised accuracy; general hedges did less. Control agreement 80.9% with AI vs 58.4% without AI.
- **Band et al. 2024 (a23, c14, [V]).** Linguistic calibration of long text: a text is calibrated if it lets a reader make calibrated forecasts. SFT then RL against a simulated reader on Llama-2-7B. Reader ECE roughly 0.10 to 0.45 across sets.
- **Belem et al. 2024 (b24, [V]).** 7 of 10 LLMs map "probably" and similar words to numbers like humans do, but the numbers shift with whether the statement is true: for the best 6, mean response 7.0 points lower for false statements; for "possible" the gap was 49.5 points. GPT-4, Llama3-70B and Gemini matched the human modal response at 85% or more.

### 2.6 Training and reasoning, 2024 to 2026

- **Kapoor et al. 2024 (a24, b18-b20, c13, [V]).** Prompting alone is not enough. LoRA finetune on about 1000 graded answers beats zero-shot verbalized and token-probability baselines. It transfers across topics, formats and other models (Mistral 7B reading LLaMA-2 7B outputs had higher AUROC than LLaMA-2 7B on itself), which argues for a general question-answer-fit signal, not special self-knowledge. User study N=181.
- **Leng et al. 2025 (b21, c15, [V]).** RLHF reward models prefer confident-sounding answers regardless of quality. Vanilla PPO worsens calibration; PPO-M and PPO-C, and calibrated DPO (over 50% ECE cut), fix it. Llama3-8B and Mistral-7B.
- **Damani et al. 2026, RLCR (b23, c20, [V]).** See 4.7.
- **Reasoning models** (Yoon b22/c19, Zeng c17, Mei c18, [V]). Disputed; see 6.3.
- **2026 mechanism and measurement-validity papers** (Kumaran a26/c23/d10, Zhao a27/c25, Cacioli c24, Ghosh d05/d08). See sections 4 and 6.

## 3. Core findings with exact numbers

Status key: **established** = two or more independent sources agree (claims.jsonl). **single** = one source. **contested** = sources disagree. **open** = not measured. Numbers are as verified in critique.md where it says so.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Large models are calibrated on lettered multiple choice via token probabilities | improves with size (up to 52B) and with few-shot; exact ECE in figures only | Kadavath 2022 (a01, b01) | established (with Lin) |
| Calibration breaks when format changes | "none of the above" swap cuts accuracy and calibration sharply; True/False stays calibrated | Kadavath (a02, b01) | single |
| RLHF token-probability miscalibration is repaired by one temperature | T=2.5, 52B, 5-shot, MMLU / MMLU T/F / TruthfulQA | Kadavath (b03, c02) | single (K15) |
| P(True) self-evaluation works few-shot; gain is calibration, not AUROC | 5 sampling tasks; P(IK) trained on TriviaQA transfers rank but not calibration | Kadavath (a03, a04, b02, b04) | single |
| Finetuned GPT-3 states calibrated probabilities under shift | Multi-answer MSE 22.0 vs logit 37.4 vs constant 34.1; Multiply-divide MSE 15.5 vs logit 10.4, constant 15.3 (verbalized worst by MAD, 19.0 vs 7.1 to 9.4) | Lin 2022 (a05, c03; corrected) | established for Multi-answer; weak elsewhere |
| Chat-model verbal confidence beats token probability on ECE (top-1) | gpt-3.5 TriviaQA ECE 0.140 vs 0.068; SciQ 0.256 vs 0.234; TruthfulQA 0.451 vs 0.389 | Tian 2023 (a07, c05) | established (K02) |
| Top-k alternatives cut ECE roughly in half | TriviaQA 0.140 vs top-2 0.050 / top-4 0.054; SciQ 0.256 vs top-4 0.065; TruthfulQA 0.451 vs top-4 0.203. The ">50% cut" holds only for top-k prompts | Tian (b11, c05) | established (K02) |
| gpt-4 also gains | TriviaQA ECE 0.078 token vs 0.024 verbal | Tian (c05) | single |
| CoT does not improve verbalized calibration; two-stage CoT worse than top-k | TriviaQA 2S CoT 0.110 vs 1S top-2 0.050 | Tian (b11) | single, see 5.2 |
| Words and numbers calibrate about equally | Ling. 1S-human ECE 0.062, 1S-opt 0.058, vs Verb 1S top-1 0.068; AUC about 0.88 | Tian (a08, b12) | single |
| Discrimination near chance on adversarial data | TruthfulQA AUC 0.38 to 0.55 despite lower ECE | Tian (a08) | single |
| Vanilla verbal confidence is overconfident | ECE above 0.377 for GPT-3, GPT-3.5, Vicuna; values cluster 80 to 100% | Xiong 2024 (a09, b07) | established |
| Low ECE can be a constant | GPT-4 GSM8K 93.6% accuracy, ECE 0.064 with all answers at 100% | Xiong (b08, c06) | established (K03) |
| GPT-4 verbal AUROC near chance | average 62.7% over 8 datasets; about 22.2% gain from GPT-3 to GPT-4 | Xiong (a09, b07) | established |
| White-box only slightly beats black-box | AUROC 0.605 vs 0.522 | Xiong (a10, c06) | single |
| Sampling agreement beats single stated confidence | GPT-4 GSM8K AUROC 54.8 to 92.7 with 5 samples; gains grow to M=13 then flatten; cost linear in M | Xiong (b09, c07) | established (K04) |
| Agreement vs verbal in small models | resolution .0637 vs .0316 (2.02x); Brier .1465 vs .1713; ECE .0704 vs .0366 (verbal ECE is as good or better) | Ghosh 2026 (d05) | single, small open models |
| Trace-geometry score at K=4 beats SC@8 on frontier reasoners | median AUC 0.78 vs 0.71 (+0.075), 6 of 6 settings; cost $0.1379 vs $0.2839 for SC@10 (51.4% saving) | Boubnovski 2026 (d06) | single |
| Frontier verbal AUROC is only fair | 0.751 / 0.787 (MedQA Gemini / Claude), 0.628 / 0.580 (GPQA), 0.633 / 0.738 (MMLU-Pro); 3 of 6 above 0.7 | Boubnovski (d07) | single (K16) |
| Small instruction-tuned models saturate | 91.7% of numeric confidences at 95% or more (range 72.4 to 96.8%), 524 TriviaQA items, 7 models, all 7 "Invalid"; log-prob R2 below 0.01 | Cacioli 2026 (c24) | single |
| Saturation also in open reasoners | fewer than 5% of responses below 0.5 in 3 models; 13,121 of 15,000 at 90+ | Wang 2026 pitfalls (d09); Ghosh (d08) | contested for frontier (K05) |
| Frontier models are not saturated | ConfidenceBench Brier 0.103 (Opus 4.6, Gemini 3.1 Pro) vs calibrated-random 0.1875; Flash-Lite 0.367; 5 of 15 worse than 0.1875; human 0.105 | ffrench-Constant 2026 (d04) | single |
| Formats disagree inside one model | Spearman between three verbal formats -0.069 to +0.247, all below the 0.60 target | Ghosh (d08) | single (K20) |
| Models almost never hedge by default | 5% of base answers; instruction 65%; CoT 16%; strengtheners 20% vs weakeners 14% | Zhou 2024 (a11) | established (K06) |
| Confident wording is often wrong | 53% correct among certainty-marked answers (random 25%); 17% of all errors carry strengtheners; 47% error | Zhou (a11, c09) | established |
| Hedge faithfulness is near chance | cMFG vanilla 0.52 to 0.57; best 0.70 (Gemini Ultra) and 0.63 (GPT-4) | Yona (a14, c08) | established (K06) |
| Prompt markers move accuracy a lot (old models) | up to 80% change; weakeners 47% vs strengtheners 40%; suffix 80% vs prefix 63% | Zhou 2023 (b13) | single, GPT-3 era |
| Users over-rely on confident wording | relied on 81% of strengtheners when 66% were correct; 73% on wrong confident answers; score 76% miscalibrated vs 86% calibrated; underconfident 66% then 98% | Zhou 2024 (a12) | single (n=25 per cell) |
| Humans cannot read LLM confidence from default text | model AUC 0.751 / 0.746 / 0.781 vs human 0.589 / 0.602 / 0.592 | Steyvers 2025 (a16, c10) | established (K07) |
| Longer explanation raises confidence, not discrimination | BF=25 for confidence; human AUC 0.54 long vs 0.57 uncertainty-only (BF 0.23, no gain); wording effect BF>100 | Steyvers (a17, c11) | single |
| First-person hedges lower reliance and improve accuracy | N=404, medical Q; agreement with AI 80.9% control | Kim 2024 (c12) | single |
| Models' word-number maps shift with truth value | 7.0 points lower for false statements; "possible" gap 49.5 | Belem 2024 (b24) | single |
| RLHF reward models penalise hedges | plain 4.03, strengtheners 0.82, weakeners -1.86; annotators 8 to 9% less likely to choose weakeners | Zhou 2024 (a13) | single |
| Binary RL harms calibration; Brier reward repairs it | HotpotQA ECE 0.37 to 0.03 (with analysis), 0.09 without; accuracy 61.7 vs 63.0; math 0.26 to 0.10; tokens 113 vs 92 | Damani 2026 (b23, c20) | established (K08) |
| Training on about 1000 graded answers beats prompting | 1000 enough, 20,000 add little; 2000 held out | Kapoor 2024 (a24, c13) | established (K08) |
| Reasoning models calibrate better | 33 of 36 settings; AIME R1-Distill-32B ECE 0.752 to 0.240, AUROC 0.695 to 0.813 | Yoon 2025 (b22); Zeng 2025 (c17) | contested (K09) |
| Reasoning depth effects depend on task | GPQA low to high depth +10.8% accuracy, -5.5% ECE; StrategyQA unchanged; reasoning models often above 85% stated | Mei 2025 (c18) | contested |
| GPT-5 effort and Brier | Standard 0.117, High 0.121, Low 0.141 | ffrench-Constant (d04) | single |
| Verbal confidence tracks commit decision more than correctness | median AUROC gap +0.16; class-VC 7 of 8 cells; log-prob gap +0.018 | Kumaran 2026 (d10) | single author |
| Models ignore penalties | confidence and accuracy flat across penalties 0 to 100; utility collapses on HLE, GPQA | Wang 2026 RiskEval (a28, c22) | single (K10) |
| Agent confidence as a control signal | AUQ +10.7% (ALFWorld), +13.6% (WebShop); fixes 14.3% of ReAct failures, regresses 3.6%; BrowseConf 90-94% bin only 53.33% accurate; trained step AUROC 0.68 to 0.85 | Zhang 2026, Ou 2025, Hathidara 2026 (c26-c28) | single (K11) |
| Verbal confidence is computed at answer time | log-probs explain 10.0% of variance, cached activation 38.0% (Gemma 3 27B) | Kumaran 2026 (a26, c23) | single (K14) |
| Frontier forecasting is behind the crowd | Brier .179 vs .149; accuracy 71.5% vs 77.0%; zero-shot best .208 | Halawi 2024 (d01) | single; no AUROC of stated confidence anywhere (K16) |
| Human overconfidence classics | 20% wrong at full certainty; 90% intervals hit as low as 50%; Oskamp 33% to 53% | Wikipedia summary (a21) | unverified (K13, K21) |

## 4. Mechanisms and models

Each item says what to compute so an engineer could build it.

### 4.1 Calibration metrics

- **ECE.** Bin answers by stated confidence (10 or 15 equal bins). For each bin, gap = abs(mean confidence minus accuracy). ECE = sum over bins of (bin count / N) times gap.
- **Brier score.** Mean of (confidence minus outcome)^2 where outcome is 1 or 0. Splits as reliability minus resolution plus uncertainty. Reliability is calibration; resolution is discrimination.
- **AUROC.** Chance that a random right answer has higher confidence than a random wrong answer. 0.5 is chance.
- **Constant baseline.** Always state the training-set accuracy (Lin b06) or always say 100% (Xiong b08). Report it beside every ECE. If your ECE does not beat it, the number means nothing.
- **Rule.** ECE alone is gameable. High accuracy plus all-100% scores ECE 0.064 (Xiong). Always report AUROC (or resolution) with ECE and the constant baseline (K03, K22).

### 4.2 Where the confidence signal lives

- Verbal confidence is formed at answer-adjacent positions as the answer is generated, cached, and read out later (Kumaran c23). Log-probability indices explain 10.0% of its variance, the cached activation 38.0% (Gemma 3 27B). It is not a read-out of token probability.
- A small set of mid-to-late MLP blocks and attention heads writes an inflation signal. Top 3,000 edges out of 527,743 (Qwen2.5-3B) and 693,267 (Llama-3.2-3B), under 0.6% of edges, are sufficient (Zhao c25).
- Cacioli (c24): in small quantised models, token log-prob predicts verbalized confidence at cross-validated R2 below 0.01.
- Confidence and accuracy directions are nearly orthogonal in open models; same-prompt reasoning disrupts the confidence direction (cosine +0.26 under a pure-confidence prompt, -0.63 under a joint solve-and-rate prompt; Miao and Ungar d13).
- Engineering meaning. These are interpretability results on 3B to 27B open models. An API agent cannot use them. The useful consequence: confidence is a second, partly independent signal, so a separate pass may add information.

### 4.3 Elicitation recipes that were measured

1. **Single numeric ask.** "Give your answer and a confidence 0 to 100." Cheap, saturates (K05).
2. **Top-k in one reply.** "Give your k best guesses and the probability that each is correct." Best in Tian: ECE 0.140 token vs 0.050 at k=2 on TriviaQA; the gain levels off after about two guesses. Echoes human "consider the opposite" debiasing.
3. **Two-stage.** Answer first, then rate in a second call. Tian found 2-stage CoT worse than top-k. Separate blind rating passes averaged over several passes (Twin-Pass, d12) cut ECE in Gemma-3: TeleQnA 4B 0.400 to 0.108, 12B 0.314 to 0.244, 27B 0.255 to 0.172; ORANBench 4B 0.800 to 0.093, 12B 0.318 to 0.249, 27B 0.252 to 0.208. The gain shrinks with model size.
4. **Linguistic map.** Elicit a phrase from a fixed list; map to a number by a fixed table. Tian: ECE 0.058 to 0.062, same as numbers.
5. **P(True).** After the answer, a second call: "Is this answer true? Yes or no", read as a probability or a rating (Kadavath). Few-shot needed. Show other samples next to the graded one.
6. **Sampling agreement.** Draw M answers (5 to 10, T about 0.8), cluster by answer, confidence = share in the cluster. Optionally weight by verbalized confidence ("Avg-Conf", best AUROC on 5 of 6 datasets, Xiong c07). Pair-Rank (ask which of two answers is more likely) got average ECE 0.028.
7. **Scored feedback prefix (REHEARSE, d14).** Pre-play about 50 rounds of a credence game under a strictly proper score, summarise "you were over/under-confident" in a few lines, put it in the prompt. Average ECE down 58% across 4 LLMs, 3 benchmarks, 5 seeds. AUROC does not lead (FaR edges it). One cell (LLaMA-3.1-8B accuracy 0.128 to 0.822) looks like a format fix, not calibration.
8. **Trace-based fusion (Boubnovski d06).** Embed K=4 reasoning traces, score geometry and coverage, fuse with the verbalized value. Needs an embedder and a judge call.

### 4.4 Recalibration after the fact

Take graded history for a task class. Fit a monotone map from stated value to observed accuracy (isotonic regression or Platt, or one temperature for token logits: T=2.5 in Kadavath's RLHF case). Needs held-out labelled data. It repairs calibration, not discrimination (Kadavath: more shots help calibration, not AUROC). Calibration does not transfer across task types (Lin Multiply-divide; Zong d15; Ghosh format correlations), so the map must be per class (K20).

### 4.5 Linguistic calibration of text

Two routes.
- **Calibrator plus controlled wording (Mielke c04).** Predict P(correct) with a separate model; choose the hedge from bins of that probability.
- **Reader-forecast objective (Band a23).** Train so a simulated reader's forecast from your text is calibrated.

For a prompt-only agent the first route maps to: compute confidence in code (agreement or checks), look up a fixed phrase for the bin, and make the final message use only that phrase. This is untested on frontier models (section 7, Test first).

### 4.6 Decision rule from stated confidence

Expected utility of answering is p times gain minus (1 minus p) times penalty. Answer iff p exceeds penalty / (gain + penalty). Models do not apply this themselves (Wang a28/c22: flat across penalties 0 to 100, almost never abstain). A code-side scaffold that applies the threshold improves utility. Caveat: stated confidence predicts the model's own commit more than correctness (Kumaran d10), so the input p must come from a channel that tracks correctness (agreement, check results).

### 4.7 Training-time fixes (upper bound only)

- **RLCR (Damani).** Reward = correctness minus Brier term on the stated confidence. A bounded proper scoring rule makes accurate and calibrated models optimal (proved). HotpotQA ECE 0.37 to 0.03 with explicit uncertainty reasoning (0.09 without). Confidence can also weight samples at test time.
- **PPO-M / PPO-C / calibrated DPO (Leng).** Fix reward-model bias toward confident text.
- **Outcome-grounded step confidence (Hathidara c28).** Qwen2.5-7B agent, proper-scoring rewards against episode outcome. Offline AUROC 0.68 to 0.85; top 10% most confident steps succeed 4.3x more often; online ALFWorld ECE 0.42 to below 0.12.
- **Hacking risk (Tan d16).** If correct and wrong answers get separate confidence rewards, the model can answer wrong on purpose to look calibrated.
- **Persistence of the prior (d09).** Concentration of confidence on a few high values survives RLCR training; a calibrated prior added by SFT helps exploration.

Out of scope for a scaffold. Use as an upper bound.

## 5. What holds up

### 5.1 Replications and agreement across sources

- Verbalized confidence from RLHF chat models is better calibrated than their token probabilities on factual QA (Tian), and the gains are largest with top-k. Consistent with Xiong's finding that prompt strategies lower ECE. [E]
- Vanilla verbalized confidence is overconfident and discriminates weakly (Xiong, Zhou, Cacioli, Ghosh). [E] for non-frontier models.
- Sampling agreement beats a single stated confidence for failure prediction: Xiong (GPT-4, GSM8K), Ghosh (0.5B-7B), Boubnovski (frontier, with a trace-based variant). [E] (K04)
- Hedge words are rare and not tied to correctness (Zhou, Yona, Mielke). [E] (K06)
- Humans over-trust confident wording and cannot tell right from wrong from default text (Zhou, Steyvers, Kim). [E] (K07)
- Plain correctness-only RL hurts calibration (Leng with PPO, Damani with RLVR). [E] (K08)

### 5.2 Failed, narrowed or conflicting results

- **Lin's generalisation** holds only on Multi-answer; on Multiply-divide verbalized is worst by MAD (critique correction 1). A constant baseline is strong when accuracy barely shifts.
- **Tian's top-1 vs top-k.** The ">50% cut" applies to top-k prompts (SciQ top-1 0.234 vs token 0.256; top-4 0.065). TruthfulQA top-1 0.389, top-4 0.203.
- **ECE vs AUROC.** Prompts that lower ECE leave failure prediction near chance (Xiong). TruthfulQA AUC 0.38 to 0.55 despite lower ECE (Tian). Verbal ECE .0356 equals the best while agreement has twice the resolution (Ghosh).
- **Tian vs Kadavath.** Not a true conflict: RLHF chat model with free text and verbal channel vs base model with lettered options and token channel.
- **Tian vs Xiong on size of overconfidence.** Easy trivia vs hard reasoning, different prompts and metrics (b10 limits).
- **Xiong white-box vs black-box** only 0.605 vs 0.522, and Kumaran shows verbal confidence is not a read-out of log-probs. Both channels are weak.
- **Reasoning and calibration.** Yoon: strictly better in 33 of 36 settings. Mei: no change on easy tasks (StrategyQA), more overconfidence with depth when accuracy does not rise. Zeng: small models' ECE rises beyond about 10,000 tokens, DeepSeek-R1 does not. Reasoning models also say "I don't know" less on factuality sets (Zeng). Contested (K09).
- **Saturation.** Seen in 3-9B and 0.5-8B open models and open reasoners; not seen in 15 frontier models in ConfidenceBench (Brier 0.103) but that is a 200-item private multiple-choice set. Contested (K05).
- **Penalty response.** Wang: no abstention under penalties on API frontier models. Ghosh: a small model passed 26.8% of the time among 13,121 responses stating 90 or more under +1/-2/0 scoring. Different models and set-ups, not reconciled (d11).
- **Format instability.** Three verbal formats on one model correlate -0.069 to +0.247 (all below 0.60).
- **Calibration transfer.** SFT confidence ECE 0.611 in-distribution, 0.625 out; critique training 0.588 in, 0.571 out; AUROC 0.562 to 0.578 (SFT_Soft), 0.593 both (CritiCal). Absolute ECE stays near 0.6. Kapoor found transfer across topics and models, but that is a finetuned classifier on 7B models, not a prompt.
- **Human primary sources unchecked.** Lichtenstein 1982 and Wallsten 1986 numbers beyond a18 were not read (K21).

### 5.3 Moderators

- **Model size.** Large models (70B or more) reach ECE about 0.1 with the best prompt (Yang a25/c16: average deviation 7%). The smallest model's confidence was nearly independent of accuracy. Few-shot and multi-guess help large models and hurt tiny ones. Twin-Pass gain shrinks with size.
- **Model family and tuning.** Claude-1 verbalized far worse than Claude-2; Llama-2-70B mixed (Tian). Claude was best calibrated by a wide margin among reasoners (Mei). Most accurate is not best calibrated (Gemini 3.1 Pro 82.7% accuracy, not best Brier; d04).
- **Task difficulty.** Hard tasks, adversarial sets (TruthfulQA) and professional-knowledge tasks (law, ethics) stay hard for every method (Xiong). Unknowable items sit on a 25% floor in ConfidenceBench.
- **Format.** Option letters vs free text (Kadavath); "none of the above" breaks it; prompt phrasing moves everything (Yang; Tian 1-stage vs 2-stage).
- **Where the confidence is asked.** Same pass as reasoning vs separate pass: contested (K18).
- **Reader.** Wording and length move human confidence strongly (BF over 100 for wording, 25 for length); aligned wording changes belief but not human decision accuracy (Steyvers b17).

### 5.4 Interventions that worked

- Top-k with probabilities in one reply (Tian). Few-shot examples for P(True) calibration (Kadavath). Per-format temperature fit for token logits (Kadavath).
- 5-sample agreement (Xiong, Ghosh); trace fusion at K=4 (Boubnovski).
- Separate blind rating passes (Twin-Pass); scored-feedback prefix (REHEARSE, ECE only).
- A code-side threshold scaffold for abstention (Wang).
- Confidence-triggered rethinking in trained small models (Jang c21: ARC-Challenge Llama +6.3% accuracy and 71% ECE cut; Qwen +9.1% and 33%; trained on GSM8K only) and in agents (AUQ).
- Retry-until-confident (BrowseConf), where confidence has only ordinal value (near-zero accuracy at low stated confidence, over 2x average accuracy above 95%; eliciting confidence did not hurt: 30.49% vs 30.0%).
- Training: RLCR, PPO-M/C, calibrated DPO, 1000-example LoRA.

### 5.5 Interventions that did not work

- Telling the model to be careful (SCHEMA 4b). Chain of thought for verbalized calibration (Tian). Hedge instructions (Yona: punt rate 1% vanilla to 8-10%, cMFG still 0.5 to 0.6). Explicit confidence instructions that the model then ignores (Wang). Verbal confidence as the abstain trigger (K22, SCHEMA 4b). Categorical elicitation in 3-9B models (six of seven fell below 5% accuracy; Cacioli). Longer explanations (raise human confidence only).

## 6. Language models

### 6.1 How models behave by default

- **They sound sure.** Only 5% of default answers carry any epistemic marker. With a confidence request they give 80 to 100% in multiples of 5 (Xiong). Wrong answers also carry strengtheners (17% of all errors).
- **Overconfidence is worst in small and RLHF models.** Average ECE above 0.377 for GPT-3 / GPT-3.5 / Vicuna. GPT-4 has lower ECE but AUROC 62.7%.
- **Verbal beats token on RLHF chat models, token beats verbal on base models with options.** Format and tuning decide.
- **RLHF is the cause of the hedge drought and part of the overconfidence.** Reward models favour plain or confident text (a13, b21).
- **Confidence does not drive action.** Models do not abstain under priced penalties (Wang). Stated confidence tracks the model's own commit more than correctness (Kumaran, median AUROC gap +0.16 over 8 models on 4 benchmarks).

### 6.2 What changed it, by how much

| Change | Effect | Source |
|---|---|---|
| Top-2 guesses instead of top-1 | gpt-3.5 TriviaQA ECE 0.068 to 0.050 | Tian |
| Verbal instead of token | 0.140 to 0.068 (TriviaQA) | Tian |
| GPT-3 to GPT-4 | AUROC about +22.2% | Xiong |
| 1 to 5 samples (agreement) | GSM8K AUROC 54.8 to 92.7 | Xiong |
| Agreement vs verbal, small open | resolution 2.02x | Ghosh |
| Trace fusion K=4 vs SC@8 | median AUC 0.78 vs 0.71 | Boubnovski |
| Reasoning (R1-Distill-32B, AIME) | ECE 0.752 to 0.240 | Zeng |
| GPT-5 effort Low vs Standard | Brier 0.141 vs 0.117 | ffrench-Constant |
| Prompt only, best combined, 70B+ | ECE about 0.1, deviation 7% | Yang |
| Twin-Pass separate pass, Gemma-3 | ECE -17% to -88% | Saenko |
| REHEARSE prefix | ECE -58% average, 12 cells | Fang |
| LoRA on about 1000 graded answers | beats prompting on ECE and AUROC | Kapoor |
| RLCR | HotpotQA ECE 0.37 to 0.03 | Damani |
| Calibrated DPO | ECE cut over 50% | Leng |
| Confidence-triggered rethink (trained) | ARC-C +6.3% to +9.1% accuracy | Jang |
| Agent reflection on low confidence | ALFWorld +10.7%, WebShop +13.6% | Zhang (AUQ) |

### 6.3 Reasoning models

Reasoning raises accuracy and usually improves calibration, but the effect is task-dependent and the evidence conflicts (K09).
- For: Yoon (33 of 36 settings strictly better; slow-thinking behaviours drive it; calibration improves along the chain; GLM-Z1 vs GLM-4 on NonambigQA: accuracy -0.07 but ECE -0.037, AUROC +0.078; a few cases where non-reasoning had better AUROC). Zeng (AIME above).
- Against or mixed: Mei (stated confidence often above 85%, especially on wrong answers; more overconfident with deeper reasoning when accuracy does not rise; GPQA +10.8% accuracy and -5.5% ECE; easy tasks unchanged; introspective self-review cut ECE on three hard sets in o3-mini and DeepSeek R1). Zeng (small models' ECE rises beyond about 10,000 tokens; reasoning models say "I don't know" less).
- Same-prompt contamination (Miao and Ungar): reasoning in the same prompt as the confidence report disrupts the confidence direction in open 7B models.
- Frontier data: GPT-5 effort Low 0.141, Standard 0.117, High 0.121 Brier (one family, 200 items).

### 6.4 Forecasting questions

Almost nothing measures stated-confidence AUROC on questions that resolve later (K16, open). What exists: Halawi 2024 (system Brier .179 vs crowd .149; accuracy 71.5% vs 77.0%; zero-shot best .208; many models near or worse than .25; RMS calibration error .42 vs .38 as printed), ForecastBench (1,000 auto-generated future questions; experts beat top LLM, p<0.001 on N=200), Schoenegger (12 LLMs matched a human crowd on 31 binary questions; single LLMs lean above 50%; showing the human median raised accuracy 17-28%). Forecasts there are probabilities, not confidence in a chosen answer. Closest data on frontier stated confidence is closed-set: AUROC 0.58 to 0.79.

### 6.5 Agents

Confidence as a control signal is promising but single-lab. BrowseConf (gpt-oss-120b, DeepSeek-V3.1 on BrowseComp): near-zero accuracy at low stated confidence, but the 90-94% bin had only 53.33%. AUQ (GPT-5.1, GPT-4.1, Gemini-2.5, Qwen3, DeepSeek-V3.1): memory of confidence plus reflection only when low; corrects 14.3% of ReAct failures and regresses 3.6% of successes. Hathidara: a trained agent knows early which tasks it will fail but cannot rank two attempts at the same task well.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. "Part" is the schema part (G guardrail, S state, O operator, M memory, or L log). Evidence ids are from the evidence files; K ids from claims.jsonl.

### Add now (established)

1. **Report AUROC and a constant baseline beside every ECE or Brier claim.** Part: L (logging), G7. [E]. Evidence: b08, c06, d05, d10, K03, K22. Never accept a calibration claim that cannot beat "always say the base rate" and "always say 100%".
2. **Do not use a single stated confidence as a stopping or abstaining trigger.** Part: G (already in 4b; strengthen G1 and G6 wording). [E]. Evidence: b09, a09, a28, d10, K03, K10, K22. Stated confidence discriminates weakly (GPT-4 AUROC 62.7%) and tracks commitment more than correctness (+0.16 gap).
3. **Where confidence is needed, derive it from agreement of independent attempts, not from the model's word.** Part: S3/S7 (already independent attempts; log agreement share), G4/G5. [E]. Evidence: b09, c07, d05, d06, K04. Caveat from G4: same-model samples are correlated, so agreement is a hint, never proof. 5 samples already fit the schema's "2 to 4 short independent attempts".
4. **Fix the vocabulary: numeric anchors, per-agent map, never per-reader.** Part: G (output wording). [E]. Evidence: a18, a19, a20, b24, K12. Use a small fixed set of levels with numeric anchors and keep it constant for the whole run.
5. **Final-message wording must match the computed confidence; no strengtheners on unchecked answers.** Part: G (output wording). [E] for the harm (a12, a16, a17, c10, c11, K07); the match-rule itself is untested on frontier models (see Test first). Do not pad with long explanations: length raises reader confidence without raising discrimination (BF=25, AUC 0.54).
6. **Calibration is per task class and per format; never reuse a bin map across types.** Part: M (class record in S0). [E]/[S]. Evidence: d15, d08, a05, a02, K20. Keep stated-vs-actual per class in the class record; refit after any format change.
7. **Log the spread of stated values and flag saturation.** Part: L. [E] for small models (c24, d09); frontier [C]. Evidence: K05, K17. Flag if over 80% of answers sit in one bin.
8. **Treat any confidence-based control (retry, verify) as an experiment, not a fixed rule.** Part: G7. Evidence: c26-c28, K11. Single-lab results.

### Test first

| Candidate | Part | Status | Evidence |
|---|---|---|---|
| Top-2 or top-k alternatives with probabilities in the elicitation call | S4/S7 log | [E] for 2023 chat models; untested on 2026 frontier | a07, b11, c05, K02 |
| Confidence rated in a separate blind pass after the answer vs same-pass | operator order, S8 | [S] (Gemma-3, open 7B) | d12, d13, K18 |
| Confidence asked before vs after reasoning | S order | [C] | b22, c17, c18, d04, d13, K09 |
| Low confidence triggers a verify pass (retry-until-confident) vs fixed extra pass | S8, O (verify) | [S] | c26, c27, c28, K11 |
| Code-side abstain threshold from agreement (not from the stated number) | G6 interplay | [S] | a28, c22, d10, K10 |
| Fixed 5-bin numeric-anchored vocabulary | G (wording) | [C] | c24, d08, d04, K05 |
| Scored-feedback prefix (REHEARSE-style) | memory prefix | [C] ECE only | d14, K19 |
| Wording-number match forced in final message, read by a reader model | output wording | [S] human-only | a16, a17, c12, K07 |
| Per-class isotonic recalibration of stated confidence | M class record | [S] for transfer failure | d15, a02, K20 |
| 5-sample agreement vs 1 sample + verification at equal tokens | S3/S8 | open (exact test not in literature) | d05, d06, K04 |

Interplay with G6. G6 says never abstain on the first pass. A confidence-based abstain rule must apply only at the end, after every state has run, and must always output the best attempt when abstention is not priced. Test it only under an explicit penalty arm.

## 8. Concrete tests on our bench

All arms at equal total tokens (counting any extra passes and setup). Report ECE (10 bins), Brier, AUROC (with bootstrap CI) and the constant baseline for every arm. Use at least 200 graded items per arm per class for AUROC differences of 0.05; fewer items only for sanity checks.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Closed-form items with a checker (arithmetic, ARC-style, short QA) | A: 1 sample + stated confidence. B: 5 samples + agreement share, equal tokens (shorter samples). C: 1 sample + a verification pass + stated confidence | AUROC for failure prediction; Brier | B above A by 0.1 or more (Xiong 0.55 to 0.93 on GSM8K, Boubnovski +0.075); C unknown |
| T2 | Same items | A: confidence in the same call as the answer. B: separate blind rating call after the answer | AUROC, ECE | B better on ECE; AUROC unclear; effect should shrink for frontier models (Saenko gain shrinks with size) |
| T3 | Same items | A: confidence stated before the reasoning. B: after the reasoning (same call). C: separate call | ECE, AUROC, by difficulty (easy vs hard) | After helps on hard, no change on easy (Mei: unchanged on easy; Yoon: better) |
| T4 | Factual QA with unique answers | A: top-1 + confidence. B: top-2 with probabilities. C: top-4 | ECE, AUROC | B lower ECE than A (Tian: 0.068 to 0.050); little extra from C |
| T5 | Items where stated confidence is free-form | A: free number. B: fixed 5 bins with numeric anchors | Share of answers in top bin; bin accuracy monotonicity; ECE; AUROC | B lowers saturation (top-bin share) but AUROC change is uncertain; Ghosh formats correlate poorly |
| T6 | Items with a priced error (+1 right, -k wrong, 0 abstain, k = 1, 3, 10) | A: model decides alone. B: code threshold on stated confidence. C: code threshold on agreement share | Mean utility | C above B above A as k rises (Wang: scaffold helps; Kumaran: stated number is weak for abstain) |
| T7 | Final-message wording | A: free wording. B: wording forced to the computed bin (fixed vocabulary). Reader: an LLM reader forecasts correctness from the text only | Reader ECE and AUROC (Band-style) | B improves reader AUROC; human effect not testable here |
| T8 | Mixed classes | A: global recalibration map. B: per-class map. C: no map | ECE on a held-out class | B above A when classes differ (Lin, Zong) |
| T9 | Resolving questions (ForecastBench-like, or our own dated items) | A: 1 sample stated probability. B: 5-sample agreement. Baseline: constant base rate | Brier vs base rate; AUROC of the confidence in the chosen side | Fills gap K16; expect AUROC under 0.7 for stated confidence |
| T10 | Mixed easy and hard | A: no feedback. B: scored-feedback prefix with 20 to 50 graded examples of our own | ECE, AUROC | ECE down (Fang 58%), AUROC flat |
| T11 | Agent episodes | A: fixed extra verify pass. B: verify only when confidence below threshold (agreement-based) | Success rate at equal tokens; regressions (right to wrong) | B higher success; track regressions (AUQ 3.6%) |

## 9. What does not transfer, and why

- **Training results (RLCR, PPO-M/C, DPO, Kapoor LoRA, Hathidara step RL).** They change weights. A scaffold cannot reproduce ECE 0.37 to 0.03. Use as an upper bound. No like-for-like prompt-only match exists (K19).
- **Mechanistic findings (Kumaran, Zhao, Miao and Ungar).** Need weights and probes on 3B to 27B open models. An API agent has no access.
- **Token-probability results (Kadavath, temperature scaling T=2.5).** Apply only if the API gives log-probs and the task is lettered choices. Free-text agents have no such channel.
- **Small-model saturation (Cacioli, Wang pitfalls, Ghosh).** 0.5B to 9B, quantised, greedy, minimal prompt. Frontier models are not saturated in ConfidenceBench. Do not assume our model saturates, measure it.
- **Human overconfidence numbers.** Unverified classic sources and human subjects. They motivate the guardrail but do not predict model behaviour.
- **Human reader studies (Zhou, Steyvers, Kim).** Crowd workers, small cells (n=25 to 60 per cell; N=301, 404, 181 in the larger ones), trivia or medical scripts. The agent's reader is usually code or another model. Reader effects must be tested with model readers.
- **Closed benchmark results (TriviaQA, SciQ, MMLU, GSM8K).** Answers are small and exact; forecasting answers resolve later and are probabilities. Almost nothing here measures real resolution (K16).
- **GPT-3 era marker experiments (Zhou 2023).** Prompt markers changing accuracy by up to 80% may not hold on current models.
- **Agent results (AUQ, BrowseConf, Hathidara).** Single labs, varying baselines, open or small models for the training results.
- **ConfidenceBench.** 200 private multiple-choice items, 3 runs at T=1.0, Brier only, one family for effort. Leads, not facts.
- **Calibration "on average".** Averages across datasets hide per-class failures. Our agent needs per-class numbers.

## 10. Open questions

1. Does stated confidence from a 2026 frontier model, after a scaffold with reasoning, reach AUROC above 0.7 on open forecasting questions that later resolve? (K16, no paper found.)
2. At equal tokens, does 5-sample agreement beat 1 sample plus verification plus stated confidence? (Partly closed: Xiong, Ghosh, Boubnovski; exact test missing.)
3. Does a fixed 5-bin numeric vocabulary avoid saturation and hold for frontier models? (K05 contested.)
4. Does an explicit abstain rule driven by agreement raise utility under error penalties? (K10 single-source.)
5. Confidence before vs after reasoning on frontier reasoners. (K09, K18.)
6. Do hedge words in final answers track correctness in 2026 models, and does forced wording change a model reader's reliance? (No new evidence since Zhou and Kim.)
7. Does calibration on one class transfer to another without training? (Negative evidence for finetuned cases only.)
8. Is there a prompt-only method matching RLCR (ECE 0.37 to 0.03)? (REHEARSE and Twin-Pass cut ECE but not AUROC.)
9. Do the classic human numbers (Lichtenstein 1982, Wallsten 1986, Kent 1964) hold in the primary sources?
10. Is the verbal-confidence commitment effect (Kumaran) specific to the abstain framing, and does it replicate outside a single author?
11. Why does Claude calibrate best among reasoners (Mei) and is that stable across versions?
12. Does the 90-94% bin accuracy of 53.33% in agents (BrowseConf) reflect agent calibration or the benchmark?

## 11. Sources

[V] = opened this session (page or PDF text read, per the evidence files). [M] = snippet or memory only.

1. [V] Kadavath et al. 2022, Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221
2. [V] Lin, Hilton, Evans 2022, Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334
3. [V] Mielke, Szlam, Dinan, Boureau 2022, Reducing conversational agents' overconfidence through linguistic calibration. https://arxiv.org/abs/2012.14983
4. [V] Tian et al. 2023, Just Ask for Calibration. https://arxiv.org/abs/2305.14975
5. [V] Xiong et al. 2024 (ICLR), Can LLMs Express Their Uncertainty? https://arxiv.org/abs/2306.13063
6. [V] Zhou, Jurafsky, Hashimoto 2023, Navigating the Grey Area. https://arxiv.org/abs/2302.13439
7. [V] Zhou et al. 2024, Relying on the Unreliable. https://arxiv.org/abs/2401.06730
8. [V] Yona, Aharoni, Geva 2024, Can LLMs Faithfully Express Their Intrinsic Uncertainty in Words? https://arxiv.org/abs/2405.16908
9. [V] Steyvers et al. 2025, What LLMs Know and What People Think They Know. https://arxiv.org/abs/2401.13835
10. [V] Kim, Liao, Vorvoreanu, Ballard, Vaughan 2024, "I'm Not Sure, But...". https://arxiv.org/abs/2405.00623
11. [V] Band, Li, Ma, Hashimoto 2024, Linguistic Calibration of Long-Form Generations. https://arxiv.org/abs/2404.00474
12. [V] Kapoor et al. 2024, LLMs Must Be Taught to Know What They Don't Know. https://arxiv.org/abs/2406.08391
13. [V] Yang, Tsai, Yamada 2024/2026, On Verbalized Confidence Scores for LLMs. https://arxiv.org/abs/2412.14737
14. [V] Leng et al. 2025 (ICLR), Taming Overconfidence in LLMs: Reward Calibration in RLHF. https://arxiv.org/abs/2410.09724
15. [V] Belem et al. 2024, Perceptions of Linguistic Uncertainty by Language Models and Humans. https://arxiv.org/abs/2407.15814
16. [V] Yoon et al. 2025 (NeurIPS), Reasoning Models Better Express Their Confidence. https://arxiv.org/abs/2505.14489
17. [V] Zeng, Xuan, Cui, Voigt 2025, Thinking Out Loud. https://arxiv.org/abs/2504.06564
18. [V] Mei et al. 2025, Reasoning about Uncertainty. https://arxiv.org/abs/2506.18183
19. [V] Damani et al. 2026 (ICLR), Beyond Binary Rewards (RLCR). https://arxiv.org/abs/2507.16806
20. [V] Jang et al. 2025, Verbalized Confidence Triggers Self-Verification. https://arxiv.org/abs/2506.03723
21. [V] Wang et al. 2026, Are LLM Decisions Faithful to Verbal Confidence? (RiskEval). https://arxiv.org/abs/2601.07767 (cross-read only in d11)
22. [V] Kumaran et al. 2026 (ICML), How do LLMs Compute Verbal Confidence? https://arxiv.org/abs/2603.17839
23. [V] Zhao et al. 2026 (COLM), Wired for Overconfidence. https://arxiv.org/abs/2604.01457 (abstract and introduction only)
24. [V] Cacioli 2026, Verbal Confidence Saturation in 3-9B Open-Weight Instruction-Tuned LLMs. https://arxiv.org/abs/2604.22215
25. [V] Ou et al. 2025, BrowseConf. https://arxiv.org/abs/2510.23458
26. [V] Zhang et al. 2026, Agentic Uncertainty Quantification (AUQ). https://arxiv.org/abs/2601.15703
27. [V] Hathidara 2026, Can an Agent Learn to Predict Its Own Failure? https://arxiv.org/abs/2610.18614
28. [V] Halawi, Zhang, Yueh-Han, Steinhardt 2024, Approaching Human-Level Forecasting. https://arxiv.org/abs/2402.18563
29. [V] Karger et al. 2024, ForecastBench (abstract page). https://arxiv.org/abs/2409.19839
30. [V] Schoenegger et al. 2024, Wisdom of the Silicon Crowd (abstract page). https://arxiv.org/abs/2402.19379
31. [V] ffrench-Constant, Yang, Huang, Kapoor 2026, ConfidenceBench. https://arxiv.org/abs/2607.20526
32. [V] Ghosh, Kumar, Garg 2026, Measurement Validity and Representation Dynamics of Confidence. https://arxiv.org/abs/2610.25846
33. [V] Boubnovski Martell et al. 2026, Measuring Black-Box Confidence via Reasoning Traces. https://arxiv.org/abs/2605.06308
34. [V] Wang et al. 2026, On the Pitfalls of Verbalized Confidence Priors for Calibration. https://arxiv.org/abs/2609.32470
35. [V] Kumaran 2026, Reported Confidence in LLMs Tracks Commitment More Than Correctness. https://arxiv.org/abs/2606.29490
36. [V] Saenko et al. 2026, Twin-Pass CoT-Ensembling for Telco LLMs. https://arxiv.org/abs/2604.13271
37. [V] Miao, Ungar 2026, Closing the Confidence-Faithfulness Gap in LLMs. https://arxiv.org/abs/2603.25052
38. [V] Fang et al. 2026, REHEARSE. https://arxiv.org/abs/2508.14390
39. [V] Zong et al. 2025, CritiCal. https://arxiv.org/abs/2510.24505
40. [V] Tan et al. 2026, On the Effectiveness of Reward Functions in RL for Confidence (abstract and introduction only). https://arxiv.org/abs/2607.04332
41. [V] Wallsten, Budescu, Rapoport, Zwick, Forsyth 1986, Measuring the Vague Meanings of Probability Terms. https://www.gwern.net/doc/statistics/decision/1986-wallsten.pdf
42. [V, abstract] Moore and Healy 2008, The Trouble with Overconfidence. https://doi.org/10.2139/ssrn.1001821
43. [V, secondary summary] Kent 1964, Words of Estimative Probability, via https://en.wikipedia.org/wiki/Words_of_estimative_probability
44. [V, secondary summary] Overconfidence effect (Adams and Adams 1960; Lichtenstein et al. 1982; Alpert and Raiffa; Oskamp 1965), via https://en.wikipedia.org/wiki/Overconfidence_effect
45. [M] Budescu and Wallsten 1985 and a 2025 arXiv follow-up (2502.06241, SD 11.41 to 16.55 points), search snippet only. https://arxiv.org/pdf/1901.09686
46. [M] Erev, Wallsten, Budescu 1994, Simultaneous over- and underconfidence, search summary only. https://synapsesocial.com/papers/W2100105359
47. [M] Lichtenstein, Fischhoff, Phillips 1982, Calibration of probabilities (DTIC ADA101986); PDF blocked, not read.
48. [M] Wallsten et al. 1986 DTIC ADA196944; PDF blocked, not read.
