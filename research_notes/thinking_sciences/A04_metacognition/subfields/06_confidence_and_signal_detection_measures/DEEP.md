# Confidence and signal-detection measures: deep document

*Subfield A04.06. Written 2026-11-01 from evidence_a-d.jsonl (a01-a25, b01-b30, c01-c27, d01-d20), claims.jsonl (K01-K30) and critique.md. No new searching. Items marked opened:false in the evidence files are treated as unverified. Several papers appear in two or three evidence files (Xiong, Tian, Kuhn, Wang, Kadavath, Fleming and Lau); they count as one source each.*

## 1. What it is

Confidence is the agent's sense of how likely its answer is right. This subfield asks how to measure the quality of that sense. It also asks how to compute it from something we can count.

Fleming and Lau (2014) split confidence quality into three separate things (a01, b01):

- **Bias**: the overall level of confidence. Does the agent say "sure" too often or too rarely?
- **Sensitivity**: does confidence separate correct trials from wrong ones? High when right, low when wrong.
- **Efficiency**: sensitivity relative to how good the task performance is. The same monitor looks better on an easy task, so we need a way to correct for that.

One calibration number mixes all three. That is the first lesson (K01, established).

Two vocabulary points.

- **Type 1 task**: the main decision (is the answer A or B?). Type 1 sensitivity is d'.
- **Type 2 task**: judging whether the type 1 decision was right. Type 2 sensitivity is how well confidence tracks correctness.

For our agent the question is practical. We want a number that says "this answer is probably right". The number should come from code, not from the model's own words (schema G4, G5, G10). The natural candidate is agreement among independent samples. This is the machine version of Koriat's self-consistency model of human confidence (a12, c02).

Where this plugs into the schema:

- S0 gate: class-level pass rate and agreement record.
- S3/S4: sampling and harvesting.
- S7: selecting among candidates.
- S9: updating the class record.
- G1: doubt only on a signal. Low agreement is that signal.
- G4: samples from one model are not independent.
- Section 4b: "using a model's verbal confidence to stop" is already on the not-to-add list.

## 2. History and theories in depth

### 2.1 Human metamemory and the gamma era (1970s to 2000s)

- **Koriat (1976)**, phonetic symbolism and feeling of knowing, is the earliest hint of the consensus effect. For items with a consensually correct response, accuracy rose with confidence. For items with a consensually wrong response, accuracy fell with confidence (d04, abstract only).
- **Koriat (1997)**, cue-utilisation. Judgments of learning rely on cues such as ease of processing, not on direct access to memory strength (a14, not opened). People infer confidence from cues.
- **Nelson (1984)** argued for the Goodman-Kruskal gamma correlation. He wanted a metacognition measure with no assumed distributions and no built-in link to memory ability, which he called logical independence (a10, not opened; known via a02 and b02).
- **Masson and Rotello (2009)** showed gamma is biased: it depends on response bias and on the shape of the evidence distributions (a11, not opened). Phi has the same problem (a02). Gamma cannot tell a good monitor from one that just says "high" often. This is claim K02, single-source because the original studies were not opened.

### 2.2 Signal detection theory enters (2003 to 2014)

- **Galvin et al. (2003)** showed that if type 1 evidence is equal-variance Gaussian, the type 2 distributions (correct vs incorrect trials) have unequal variance and are not Gaussian (a08, not opened). So a simple type-2 d' is wrong.
- **Maniscalco and Lau (2012)** introduced **meta-d'** and the **M-ratio** = meta-d'/d' (a09, not opened). Fit the type 1 SDT model to the type 2 data. Ask: what d' would an ideal observer need to produce this confidence behaviour? That value is meta-d', in the same units as d'.
- **Fleming and Lau (2014)** is the review that organised the field (a01-a07, b01, b02, opened). Its points:
  - Bias, sensitivity and efficiency are separate.
  - Type-2 AUROC is bias-free and needs no Gaussian assumption, but it rises with accuracy (a03).
  - Efficiency = meta-d'/d'. A value of 1 is ideal. A value of 0.7 means 30 percent of the evidence is lost at the confidence step (a04).
  - The log of the ratio is recommended when d' is small.
  - Alternative: the Stochastic Detection and Retrieval Model draws two correlated evidence samples, one for the decision and one for confidence (a05). If the two samples share the same errors, confidence cannot help. This maps onto G4.
  - The Dunning-Kruger pattern has two readings: noisy rating from low d', or shared resources for skill and monitoring. One-shot self ratings cannot separate them (a06).
  - Efficiency lets us compare groups and domains with unmatched accuracy (a07).

### 2.3 Koriat's self-consistency model (2008 to 2025)

This is the main human precedent for "confidence from consistency of samples".

- **The model (Koriat 2012, d01, abstract read only):**
  - A person samples a few representations of the answer.
  - Confidence is how consistently the chosen answer is supported across the sample. It behaves like a statistical confidence level: the chance that a new sample gives the same choice.
  - Confidence and accuracy are linked only because consistency and correctness are linked.
  - The link is positive when consistently chosen answers are usually right, and negative when wrong answers are favoured.
  - Overconfidence arises because confidence tracks reliability while calibration is scored against correctness.
  - Response speed is a cheap cue for consistency. Accessibility (how much comes to mind) adds an independent contribution.
- **Consensuality principle (Koriat 2008, d02, abstract only):** the within-person confidence-accuracy correlation is positive for consensually correct items and negative for consensually wrong items. Consensual answers are reached faster and chosen more consistently on different occasions. This argues against direct access to correctness. Consensually wrong items are picked on purpose, so the negative correlation is partly a design result.
- **Perceptual domain (Koriat 2011, d03, abstract only):** same lab. The pattern held for perceptual judgments. Confidence tracked how consensual the choice was, not whether it was correct.
- **Koriat (2025 synthesis, d05, full text opened):**
  - Items are split into consensually correct (CC) and consensually wrong (CW).
  - CC items show the usual positive confidence-accuracy link. CW items show a negative one.
  - This held in 16 different tasks.
  - Other labs saw it: Brewer and colleagues (deceptive vs non-deceptive sentences), Sampaio 2017 (faces), Bajsanski 2019 (syllogisms), Litvinova 2022 (mammograms).
  - Koriat now says confidence tracks replicability: how likely the same choice is to recur. In 10 studies the confidence-replicability correlation was significant within and between individuals, for both CC and CW items. Partialling out replicability explained both the positive and negative confidence-accuracy correlations.
  - Exact r and N sit in supplementary tables S2-S6, which were not read.
- **Amplification (Koriat 2015, d06, abstract only):** in human pairs, picking the more confident member beat the better member on CC items. It was worse than the worse member on CW items. Group discussion amplified this. This is a warning for confidence-weighted voting.

Honest limit: the founding Koriat papers were not read in full. We have no exact effect sizes or N for the 2012 paper. The mechanism and direction are confirmed by the 2025 open review and by other labs. We found no failed replication, but nobody (including us) looked hard for one.

### 2.4 Calibration for neural nets (2017)

Guo et al. (2017) showed modern deep nets are overconfident. One scalar (temperature scaling), fitted on held-out data, fixes most of it (a25, b11). ECE before and after:

| Model | ECE before | ECE after |
|---|---|---|
| CIFAR-100 ResNet-110 | 16.53% | 1.26% |
| ImageNet ResNet-152 | 5.48% | 1.86% |
| ImageNet DenseNet-161 | 6.28% | 1.99% |

Lesson: calibration (bias) is cheap to repair. Discrimination (sensitivity) is not.

### 2.5 LLM uncertainty (2021 to 2026)

In rough order:

- **2021:** TruthfulQA (d13). Imitative falsehoods are wrong answers that appear often in training text, so a model gives them consistently. This is the LLM version of the consensually wrong item.
- **2022:**
  - Kadavath: large models are calibrated on lettered multiple choice. Seeing several own samples before judging helps P(True) (a16, b12, c08).
  - Lin, Hilton, Evans: fine-tuned GPT-3 can say calibrated confidence in words (a17, b20, c23).
  - Wang: self-consistency; the agreement share correlates with accuracy (a15, b17, c24).
- **2023:**
  - Kuhn: semantic entropy (a20, b18, c11).
  - Xiong: confidence elicitation, black-box (a18, b14-b16, c04-c07).
  - Tian: "just ask for calibration" (a19, b13, c10).
  - Aggarwal: Adaptive-Consistency (d10).
- **2024:**
  - Kapoor: calibration needs training (a22, b21, c22).
  - Yona: faithful expression fails (b22).
  - Farquhar: semantic entropy in Nature (d07).
  - Spiess: code calibration (d14).
  - Brown: Large Language Monkeys (d12).
  - Kim: hedge wording (d18).
- **2025:**
  - CISC: confidence-weighted voting (c18, c19, d08).
  - DeepConf (c20, c21, d09).
  - Self-certainty (d11).
  - Steyvers (a21, c14, c15, d19) and the Steyvers and Peters review (c01-c03).
  - Sun: overconfidence and human bias (c16, c17).
  - Yoon and Mei on reasoning models (d16, d17).
  - Leng: reward calibration (a23).
  - Ji-An: activation self-report (a24).
- **2026:**
  - Cacioli: type-2 SDT on token confidence (b23-b25, d20).
  - Servajean and Servajean: AUROC2 vs M-ratio (b26, b27).
  - Dai and Wang: confidence scale design (d15).

## 3. Core findings with exact numbers

Status key: E established (two or more independent sources), S single source, C contested. Human or LLM is named in the finding.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Confidence quality splits into bias, sensitivity, efficiency | Efficiency = meta-d'/d'; 1 is ideal; 0.7 means 30% of evidence lost | Fleming and Lau 2014 (a01, a04, b01) | E (K01) |
| Gamma and phi are contaminated by response bias | No pooled numbers; original simulations not opened | Fleming and Lau citing Nelson 1984, Masson and Rotello 2009 (a02, a10, a11) | S (K02) |
| AUROC2 is bias-free but rises with accuracy | AUROC2 0.5 = chance | Fleming and Lau; Guggenmos; Steyvers and Peters (a03, b04, c01) | E (K03) |
| No metacognitive measure is independent of accuracy (human) | Hierarchical M-ratio vs d' beta -0.19 +/- 0.05, p<.001. Log M-ratio beta 0.01 +/- 0.02 (p=.581). Pooled log M-ratio rs -0.073, p=.003. Total pool N=6,912; main analyses 1,757 subjects (at least 400 trials, d' above 0.5) | Guggenmos 2021 (b04) | S (K04) |
| M-ratio needs about 400 or more trials | Test-retest r at most 0.6 under 400 trials; about 0.7 at 400-600; 0.85 at 600-800. Simulation: at 60% correct r about 0.4 even at 400-600 trials; at 80% correct about 0.8; 250 trials at 60% correct r=0.2 | Guggenmos 2021; Fleming 2017 HMeta-d (b05, b06, b07) | E (K05) |
| Extreme M-ratio values are common at low trial counts | 2.4% negative, 4% above 1.5 overall; under 200 trials 4% negative and 10% above 1.5 | Guggenmos 2021 (b06) | S |
| Negative confidence sensitivity in people is partly noise | Confidence Database: 145 datasets, 8,787 participants, 3,955,802 trials. Accuracy-confidence analysis: 71 datasets, 4,768 participants, 293 negative beta; 9.9% of negative cases had under 50 trials | Rahnev et al. 2020 (b03) | S |
| Metacognitive efficiency correlates across tasks in people | N=181, four 2AFC tasks, 5 of 6 cross-task correlations significant. Type 1 d': executive 2.58, episodic 1.84, semantic 1.19 | Mazancieux 2020 (b08) | E with Fleming (K18) |
| Human confidence is suboptimal; hard-easy effect | Overconfident on hard tasks, underconfident on easy; leans on positive evidence | Rahnev and Denison 2018 (b09, b10) | S (review) |
| Confidence follows consistency: positive on CC, negative on CW (human) | At least 16 tasks; also Brewer, Sampaio 2017, Bajsanski 2019, Litvinova 2022. Exact r and N not obtained | Koriat 2008, 2011, 2012, 2025 (d01-d05) | E (K22) |
| Confidence tracks replicability of the response (human) | 10 studies, significant within and between individuals for CC and CW | Koriat 2025 (d05) | S (author's synthesis) |
| Confidence-weighted human pairs amplify the majority tendency | More confident member beats better member on CC; worse than worse member on CW. Numbers not obtained | Koriat 2015 (d06) | S (K29) |
| Agreement among samples gives gains and a confidence signal | GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-c +3.9 points. Agreement-accuracy link shown as a figure only | Wang 2022 (a15, b17, c24) | E as gain |
| Agreement beats verbalised confidence for failure prediction, mostly on arithmetic | GPT-3.5 GSM8K AUROC 54.8 to 92.7 (5 samples). Five-dataset average only 69.2 (CoT single) to 69.6 (self-random M=5) or 73.0 (prompt-varied M=5). Professional Law AUROC 59-66 with M=5 | Xiong 2024 (a18, b14, c05) | E (K06) |
| Verbalised confidence from chat models is overconfident | Average ECE above 0.377 (GPT-3, GPT-3.5, Vicuna); GPT-4 mean AUROC 62.7 (chance 50); about 22.2 AUROC gain GPT-3 to GPT-4; mass at 80-100% | Xiong 2024 (a18, c04) | C (K09) |
| Verbalised confidence can be better calibrated than token probabilities | ChatGPT TriviaQA: label prob ECE 0.140 AUC 0.869; verbal top-1 ECE 0.068 AUC 0.879; top-2 ECE 0.050 AUC 0.894. SciQ: label prob ECE 0.256 vs verbal top-4 0.065. TruthfulQA: verbal top-1 ECE 0.389 AUC 0.545 vs label prob AUC 0.418 | Tian 2023 (a19, b13, c10) | C (K09) |
| Low ECE can hide useless confidence | GPT-4 GSM8K accuracy 93.6%, ECE 0.064 by saying 100% always | Xiong 2024 (b15, c06) | S (K10) |
| Black-box vs white-box gap is small | AUROC 0.522 vs 0.605 | Xiong 2024 (a18, c07) | S |
| Pair-Rank aggregation gives best calibration | ECE as low as 0.028 | Xiong 2024 (b16, c07) | S |
| Consistency confidence improves quickly with samples, then flattens | M=1 to 13 tested; about 5 samples capture most of it | Xiong 2024 (b16) | S |
| Semantic entropy beats counting distinct answers | AUROC 0.77 vs 0.66 (CoQA), 0.83 vs 0.79 (TriviaQA). Distinct answers per question, correct vs wrong: 1.27 vs 1.77 and 1.89 vs 3.89 (OPT up to 30B) | Kuhn 2023 (a20, b18, c11) | E with Farquhar (K08) |
| Semantic entropy in a large model sweep | 30 model-task combinations, 10 generations: AUROC 0.790 vs naive entropy 0.691, P(True) 0.698, embedding regression 0.687; 0.78-0.81 across 7B-70B | Farquhar 2024 (d07) | E (K08) |
| Semantic entropy fails on systematic errors | Authors' own statement | Farquhar 2024 (d07) | S |
| Confidence-weighted voting saves samples | Cost cut at budget 10: P(True) 46%, response probability 31%, verbal 1-100 30%, verbal binary 10%. Budget 5, P(True) 41%. Accuracy gain 0.2-1.6 points. Plain SC needed 18.6 samples to match CISC at 10 | Taubenfeld 2025 (c18, d08) | S (K11) |
| Within-question discrimination is weak | WQD: verbal binary 52.2%, verbal 0-100 56.1%, response probability 59.0%, P(True) 62.3%. ECE-t 0.005, 0.046, 0.090, 0.030 (lowest ECE, near-chance WQD) | Taubenfeld 2025 (c19) | S (K12) |
| Sliding-window token confidence filters weak traces | Offline, 512 traces: DeepSeek-8B AIME25 82.3 to 87.4; Qwen3-32B AIME24 85.3 to 90.8; GPT-OSS-120B AIME25 97.0 to 99.9 (single sample 91.8). Online token saving 43.8-84.7% (low), 18.8-59.0% (high); 84.7% is the best of 12 cells | Fu 2025 (c20, c21, d09) | S (K13) |
| Logprob-free agreement stopping rule | 17 datasets, 3 LLMs: up to 7.9x, average 3.3x fewer samples, 0.04% accuracy drop. GPT-3.5-turbo 4.4x, Code-davinci-002 3.4x, Vicuna-13B 1.9x | Aggarwal 2023 (d10) | S (K27) |
| Voting plateaus while coverage rises | Llama-3-8B MATH: coverage 82.9 to 98.44% (100 to 10,000 samples); majority vote 40.50 to 41.41%. SWE-bench Lite 15.9% to 56% with tests | Brown 2024 (d12) | S (K28) |
| Imitative falsehoods: consistent wrong answers exist in LLMs | 817 questions, 38 categories; best model truthful 58%, humans 94% (2021 models) | Lin 2021 TruthfulQA (d13) | E as a class (K07) |
| Prompting alone cannot calibrate; about 1000 graded examples with LoRA can | 1000 examples beat baselines; 20,000 only slightly better | Kapoor 2024 (a22, b21, c22) | E (K14) |
| RLHF reward models favour stated confidence | PPO-M on Llama3-8B: ECE down 6.44, accuracy up 2.73 on GSM8K | Leng 2025 (a23) | E (K14) |
| Faithful hedging fails by default | cMFG near 0.5 for all models; no uncertainty expressions under default decoding | Yona 2024 (b22) | S |
| LLMs can report only a small subset of activations | Reportable space far lower-dimensional than full space | Ji-An 2025 (a24) | S (K21) |
| A calibration map for code transfers only within kind | Skill 0.14 to 0.12 (same kind); 0.12 to -1.28 (repair to synthesis); more than 64 labelled points needed. Token prob above 90% passed tests only 52% | Spiess 2024 (d14) | S (K24) |
| Confidence efficiency differs across LLMs and by domain | 4 models (8-9B), 224,000 trials: 1.98-fold range in meta-I2r; rank correlation with accuracy -0.80 (TriviaQA), 0.00 (NQ). z-ROC slopes 0.78-1.18 | Cacioli 2026 (b23) | S (K16) |
| Scorer error can fake an efficiency result | Scorer missed 53% and 26% of two models' correct answers; agreement with humans 0.76 to 0.86 after fix; residual 18.4% rejected-but-correct, varying 2.4-fold | Cacioli 2026 (b24, d20) | S (K16) |
| Metacognitive information tracks gain from abstaining | Rank correlation +1.00 across 4 models; seven temperatures tested | Cacioli 2026 (b25) | S |
| AUROC2 and M-ratio can disagree on LLMs | Across tasks AUC2 vs d' rs=0.9, p<0.002. Mistral higher M-ratio but lower AUC2 than DeepSeek across tasks; GPT-5 above DeepSeek by 0.16 M-ratio in task A. LLM M-ratios about 0.65 to 0.90 | Servajean 2026 (b26) | C (K17) |
| Verbal scale design changes measured efficiency | 0-100 M-ratio 0.62 (Qwen3-30B) to 0.92 (GPT-5.2); 0-20 scale higher (GPT-5.2 0.95; Maverick 0.89 vs 0.82); raising the scale floor lowers it (GPT-5.2 0.92 to 0.69). Three values cover 78.2-92.1% of answers; 15-28 of 101 values used. Gemini 3.1 Pro says 100 on 68.4% of items, right on 79% | Dai and Wang 2026 (d15) | S (K25) |
| Reasoning models better at verbalised confidence (32B open) | Better calibrated in 33 of 36 settings; GLM-Z1 0.07 lower accuracy yet 0.037 lower ECE and 0.078 higher AUROC | Yoon 2025 (d16) | C (K26) |
| API reasoning models are overconfident | Often above 85% even when wrong; worse with more effort; reflection helped o3-Mini and R1, hurt Claude 3.7 | Mei 2025 (d17) | C (K26) |
| LLM overconfidence vs humans | LLMs overestimate correctness by 20% (o1) to 60% (GPT-3.5); humans 66% accurate, think 70%; humans sure at 100% were 81% accurate. Human overconfidence +7.0 points with LLM answer shown, +4.2 to +7.6 with confidence display | Sun 2025 (c16, c17) | S |
| People over-trust default LLM explanations | 301 participants (284 retained). Model AUC 0.751/0.746/0.781; human AUC 0.589/0.602/0.592; long/short explanation human AUC 0.54/0.57; matched wording narrows both gaps | Steyvers 2025 (a21, c14, c15, d19) | E with Kim (K19) |
| First-person hedges change human reliance | N=404 (of 656). Accuracy: control 63.9%, first-person 72.8%, general 67.9% (n.s.), no AI 74.2%. Agreement 80.9% / 74.8% / 77.6% / 58.4% | Kim 2024 (d18) | S (K19) |
| Stated risk shifts the decision criterion | Normalised c' below -0.6 under one setting, above 0.6 under the other, all models and tasks | Servajean 2026 (b27) | S |

## 4. Mechanisms and models

Each item is written so an engineer can code it.

### 4.1 The scores, computed from logs

Log, per item: `correct` (0/1 from a trusted checker), `conf` (number in [0,1]), `task_id`.

- **Bias (level).** Mean confidence minus mean accuracy. Positive means overconfident. Also report the histogram of `conf`. If three values cover most answers, the signal is coarse (d15).
- **ECE (calibration).** Bin `conf` into 10 or 15 bins. ECE = sum over bins of (n_bin / N) * |mean_acc_bin - mean_conf_bin|. A constant guesser at the base rate can score a perfect ECE (a19 quote; b15 GPT-4 case). Never report ECE alone.
- **Type-2 AUROC (sensitivity).**
  1. Take all correct items and all incorrect items.
  2. AUROC2 = probability that a randomly chosen correct item has higher `conf` than a randomly chosen incorrect item. Ties count half.
  3. Use a many-level score. Two-bin confidence inflates AUROC (d16).
  4. It rises with accuracy (a03, K03), so always report accuracy beside it.
- **Within-question discrimination (WQD).** For each question with at least two distinct candidate answers where one is right and one wrong, check whether the higher-confidence one is the correct one. Average over pairs (c19). Use it to test whether confidence helps select among candidates.
- **Efficiency (meta-d' / d').** Needs a binary type 1 decision, multi-level confidence, and ideally 400 or more trials (b05). Fit with a library, preferably the hierarchical version (HMeta-d, b07). Report log M-ratio if d' is small. Open QA has no two-choice decision, so meta-d' is undefined (b23); use a model-free proxy or frame items as binary.
- **Do not use** gamma or phi (K02). Do not compare AUROC2 across tasks of different accuracy (K03, K04).

### 4.2 Confidence from agreement (the Koriat-style signal, by code)

1. Draw k independent samples. Each sees only the bare task, no other sample (S3, G4). Use a moderate temperature: very low gives no diversity, very high lowers accuracy, and the best AUROC is at a middle value (c12, b19).
2. Extract the final answer from each sample.
3. Normalise answers so equal answers match:
   - Numbers: parse and compare as numbers.
   - Multiple choice: the letter.
   - Free text: cluster by meaning. Semantic entropy uses bidirectional entailment judged by a small model (d07). Cost: extra judge calls.
   - Code: there is no shared answer string (d11). Define equivalence by behaviour: run each program on the same probe inputs and compare outputs, or use the tests.
4. Agreement score = size of the largest cluster divided by k. Alternative: 1 minus normalised entropy over clusters (semantic entropy).
5. Optional blend: average agreement with the model's verbal confidence. Avg-Conf gave the best failure prediction and Pair-Rank the best calibration, ECE 0.028 (b16, c07).
6. Calibrate (4.5). The raw share is not a probability.

About 5 samples capture most of the benefit (b16). Gains are largest where answers are easy to match (arithmetic) and small where they are not (Professional Law, AUROC 59-66; c05).

### 4.3 Adaptive stopping on agreement (no logprobs needed)

Adaptive-Consistency (d10): after each new sample, compute the chance that the current leading answer stays the leader.

- Model the answer counts with a Dirichlet.
- Stop when that chance is above a threshold (for example 0.95).
- Average 3.3x fewer samples for a 0.04% accuracy drop on 2023 models.
- It is a pure-code, black-box rule. It fits G12 (spend by difficulty).

### 4.4 Confidence-weighted voting (CISC)

For each sample i with answer a_i and confidence c_i:

1. Get c_i from a cheap second step. The best was a P(True) self-check appended to the same prefix (about 20 input tokens, one output token; d08).
2. Normalise c_i within the question with a softmax, temperature tuned per method.
3. Score each distinct answer as the sum of its normalised weights.
4. Pick the highest.

Result: about 40% fewer samples than plain majority to match accuracy, with 0.2-1.6 point gains (c18). Caveat: the cost claim assumes a cached prefix (d08). Koriat's amplification result (d06) says weighting by confidence can hurt where the majority is wrong. Test on a consensually wrong slice.

### 4.5 Post-hoc calibration map

- Collect held-out items with a trusted checker. Fit a monotone map (isotonic, or Platt: sigmoid(a * logit(s) + b)) from agreement share to accuracy.
- Guo's temperature scaling is the one-parameter version (b11).
- For code, a map transfers only between tasks of similar kind and base rate. It failed across kinds (skill 0.12 to -1.28). More than 64 labelled points are needed before skill turns positive (d14). So fit one map per task family and check the base rate before reuse.
- This repairs bias. It cannot repair sensitivity (b11).

### 4.6 Token-level confidence (needs logprobs)

- **Mean token confidence**: mean negative log-probability of the top-k tokens (d09).
- **Sliding group confidence (DeepConf)**: score windows of 2,048 tokens. Trace score = lowest group, mean of lowest 10% of groups, or the last 2,048 tokens (tail). Online: warm up with 16 traces, set a threshold from them, cut any trace whose current group score falls below it, and stop at 95% consensus.
- **Self-certainty** (d11): KL divergence of the next-token distribution from uniform, averaged over the response. Length-insensitive. Needs full logits.
- Hazard: overconfident wrong traces. Filtering to the top 10% lowered accuracy in a few cells (Qwen3-32B BRUMO25 -0.9 points; d09).

### 4.7 Why samples from one model can mislead (SDRM view)

The SDRM idea (a05) is that the decision sample and the confidence sample are correlated with coefficient rho. If rho is near 1, the second sample adds nothing. In LLM terms, k samples from one model share its biases, so agreement measures the reliability of the output, not correctness. This is Koriat's point exactly (d01). Agreement is a good proxy only while the modal answer is usually right.

## 5. What holds up

### 5.1 Replications and agreement

- **Consistency drives human confidence.** Positive on CC items and negative on CW items in at least 16 tasks. Replicated by at least four other groups (Brewer et al., Sampaio 2017, Bajsanski 2019, Litvinova 2022) and in a new domain by the original lab (Koriat 2011) (d03, d05). Established, but our notes have no exact effect sizes.
- **Sample agreement predicts LLM correctness.** Wang (figure), Xiong (AUROC), Kuhn and Farquhar (semantic entropy), Aggarwal (stopping). Independent labs, different models, same direction. Established.
- **Semantic grouping beats surface counting.** Kuhn 2023 (OPT, 2 datasets) and Farquhar 2024 (30 model-task pairs). The gain over counting distinct answers is 4-11 AUROC points, not huge (critique item 6).
- **Calibration without training is limited.** Kapoor, Yona, Xiong and Leng agree that prompting alone is not enough and that RLHF pushes stated confidence up.
- **Wording moves human reliance.** Steyvers and Kim agree on direction (matched or first-person wording helps), though neither uses agreement counts.

### 5.2 Failures, contradictions, boundary conditions

- **Consensually wrong items.** Agreement inverts. Koriat shows it in people. Farquhar says plainly that semantic entropy "does not help when LLM outputs are systematically bad" (d07). TruthfulQA shows the class in LLMs (d13). Large Language Monkeys shows voting plateaus (40.50 to 41.41% on MATH) while coverage reaches 98.44% (d12). Nobody measured how often this hits current frontier models. That is claim K23, an open gap.
- **The big Xiong number is the best case.** GSM8K 54.8 to 92.7 is arithmetic with GPT-3.5. The five-dataset average goes only from 69.2 to 69.6 (self-random M=5) or 73.0 (prompt-varied M=5). Table labels also differ between main text and appendix (critique item 1). Read it as "largest on arithmetic".
- **Calibration ranking is contested.** Xiong finds verbalised confidence overconfident (ECE above 0.377, GPT-4 AUROC 62.7). Tian finds it better calibrated than token probabilities (ECE halved). The studies differ in metric (ECE vs AUROC), models and prompts. On discrimination both say modest. Even in Tian, verbal ECE on TruthfulQA was 0.389 (c10). Kapoor says sampling calibrates decently but discriminates weakly, while verbal elicitation discriminates fairly but calibrates badly (c22).
- **Reasoning models: split.** Yoon: reasoning models better calibrated in 33 of 36 settings (32B open). Mei: API reasoning models overconfident above 85% when wrong, more so with more effort. Neither tested agreement vs verbal at equal tokens.
- **No metric is neutral.** M-ratio falls with accuracy (Guggenmos beta -0.19). Log M-ratio removes the hierarchical slope but a pooled rs of -0.073 remains, and the author says more data are needed. AUROC2 rises with accuracy. AUROC2 and M-ratio can rank two LLMs oppositely (Servajean). Cacioli finds weak or negative accuracy-efficiency coupling (rank -0.80 / 0.00) in 8-9B models, but only after a scorer fix, and he withdrew an earlier stronger claim.
- **Reliability.** M-ratio needs about 400 trials. Under 200 trials, 10% of subjects have values above 1.5.
- **Scale artefacts.** On a 0-100 verbal scale models use only 15-28 values; three values cover up to 92% of answers (Dai). Two-bin use inflates AUROC (Yoon). A scale change moved M-ratio for GPT-5.2 from 0.92 to 0.69.
- **Grader error.** A length-biased scorer missed 53% and 26% of correct answers for two models and nearly produced a false efficiency result (Cacioli). Even after the fix, 18.4% of rejected answers are correct, and this varies 2.4-fold by model.
- **Human cross-domain generality depends on power.** Small samples found nulls; N=181 with a hierarchical model found 5 of 6 pairs significant (Mazancieux). For LLMs, Cacioli's weakest area for all four models was Science and Technology: domain-specific.
- **Weak spots in the base.** The Koriat papers (a12-a14, b29, c26, d01-d04, d06), Maniscalco and Lau, Galvin, Nelson, Masson and Rotello, the Dai second-hand mention (b28), Cash 2025 (c03) and Griot 2025 (c27) were not opened in full. Most LLM studies use small or 2023-era models. Cacioli, DeepConf, CISC and Dai are preprints.

### 5.3 Interventions

| Intervention | Result | Verdict |
|---|---|---|
| Sample k answers and count agreement | AUROC 54.8 to 92.7 on GSM8K; modest elsewhere | Worked, mostly on arithmetic |
| Semantic clustering before counting | AUROC +4 to +11 over distinct-answer count | Worked, modest, costs judge calls |
| Mix verbal confidence into agreement | Best failure prediction (Avg-Conf), best ECE 0.028 (Pair-Rank) | Worked; no single winner |
| List top-k guesses before rating | ECE cut 50% or more often (Tian) | Worked for calibration; no discrimination proof |
| Weight votes by P(True) | 46% fewer samples at budget 10 | Worked on open models; not tested on reasoning models |
| Weight votes by binary verbal confidence | 10% saving, WQD 52.2% | Barely worked |
| Adaptive stop on agreement | 3.3x fewer samples, 0.04% drop | Worked on 2023 models |
| Window token confidence (DeepConf) | 43.8-84.7% tokens saved | Worked with logprobs only |
| Platt or temperature scaling | ECE 16.53 to 1.26 (vision); code skill 0.14 to 0.12 within kind | Worked within kind; failed across kinds |
| Prompting for calibration | Not sufficient (Kapoor, Yona) | Did not work alone |
| LoRA on about 1000 graded examples | Beats baselines | Worked; needs training |
| Reasoning mode for verbal confidence | Better in 32B open (33/36); worse with effort in API models | Contested |
| Reflection on own trace | Helped o3-Mini and R1; hurt Claude 3.7 | Mixed |
| Long explanations | Raise human confidence, no discrimination gain (AUC 0.54) | Hurt |
| First-person hedge wording | Human accuracy 63.9 to 72.8% | Worked (human readers) |
| Confidence-weighting in human pairs | Fails on CW items (Koriat 2015) | Failed where the majority is wrong |
| Run tests (code) | SWE-bench Lite 15.9 to 56% | Worked; tests do not vote |

## 6. Language models

### 6.1 Verbalised confidence

- RLHF chat models are overconfident and cluster at 80-100% (Xiong, a18, b14). A reward-model cause is plausible: reward models favour high stated confidence (Leng).
- GPT-4 vanilla verbal confidence: mean AUROC 62.7 across eight tasks. GPT-3 to GPT-4 gain: about 22.2 AUROC points.
- Models answer decisively even when their own sample agreement is low; hedge faithfulness sits near 0.5 (Yona, b22).
- Scale matters: 0-100 uses only 15-28 distinct values (Dai). Gemini 3.1 Pro says 100 on 68.4% of items and is right on 79%. GPT-5.2 says 95 on 42.1% and is right on 85%.
- Frontier verbal efficiency can be high: M-ratio 0.92 for GPT-5.2, and about 0.65-0.90 in Servajean (GPT-5, DeepSeek-V3.2-Exp, Mistral-Medium). These used a single binarised threshold and short tasks.
- Reasoning models: better in 33 of 36 settings in 32B open models (Yoon); overconfident and worse with effort in API models (Mei). Sun: five LLMs overestimate correctness by 20% (o1) to 60% (GPT-3.5); a 10% drop in confidence goes with about a 25% drop in accuracy for GPT-4o and o1, about 13% for Llama 3.1.
- Fine-tuning: about 1000 graded examples with LoRA beat prompting (Kapoor).

### 6.2 Token-level confidence

- Older base models are calibrated on multiple choice (Kadavath, up to 52B). RLHF worsens token-probability calibration (Tian).
- Token-likelihood confidence tracked accuracy trial by trial better than verbalised confidence in at least one comparison (Steyvers and Peters citing Xiong).
- GPT-3.5 token-likelihood on MMLU: AUC 0.778. Fine-tuned GPT-4.1-mini verbal on TriviaQA: AUC 0.83 (c01).
- Code: average token probability above 90% passed tests only 52% of the time (Spiess).
- Cacioli: four 8-9B models differ 1.98-fold in token-confidence information; temperature changes accuracy but leaves information flat in three of four.

### 6.3 Agreement

- Best evidence for black-box confidence. Numbers are in section 3.
- Behaviour with model size: semantic entropy's advantage grows with model size and number of samples (Kuhn); AUROC 0.78-0.81 across 7B-70B (Farquhar).
- Black-box vs white-box gap is small (0.522 vs 0.605).
- It does not exist for open-ended code without a behavioural equivalence rule (Kang).
- It fails on systematic errors and misconceptions (Farquhar, TruthfulQA).
- Voting plateaus (Brown).

### 6.4 Readers (humans)

- With default explanations people overrate LLM accuracy and barely discriminate right from wrong (human AUC about 0.59-0.60 vs model 0.75-0.78). Explanation length drives confidence. Matching wording to model confidence narrows both gaps.
- Showing LLM answers raises human accuracy but also overconfidence (Sun: +7.0 points; a confidence display adds 4.2-7.6).
- First-person hedges: human accuracy 63.9 to 72.8%, agreement with the system 80.9 to 74.8% (Kim, N=404). The hedge was set by the experimenters, not computed from the model.
- No study yet uses confidence computed from sample agreement.

### 6.5 What we do not know about current models

No source runs agreement vs verbalised vs token confidence on a current frontier reasoning model, open-ended or code, at equal tokens (gap 1). Dai gives a verbalised data point, Mei and Yoon give two views of reasoning-model calibration, and Cacioli covers only 8-9B models and says frontier scale is unknown.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. "Schema part" says where it attaches (G guardrail, S state, O operator, memory).

### Add now (established)

| # | Item | Schema part | Status and claim | Evidence ids |
|---|---|---|---|---|
| 1 | Report confidence quality as separate numbers: bias (mean conf minus accuracy, plus ECE), sensitivity (AUROC2 with many-level scores), and accuracy beside both. Never grade a confidence signal on one number. Add to the section 6 log. | metric, S9 log | [E] K01, K03 | a01, a03, b01, b26, c01 |
| 2 | Count agreement in code, not in the model's words. Confidence for single-answer problems = share of independent samples (about 5) that match after normalisation. This is the confidence input to G1, S7 and the S0 class record. Consistent with G4 (a hint, never proof) and 4b. | G1, G4, G5, S4, S7 | [E] K06 (largest on arithmetic, modest elsewhere) | a15, a18, b14, b17, c05, c24 |
| 3 | Treat agreement as a consensus, not truth. Valid on typical items, inverted on consensually wrong items. Keep G4 as written (no confidence-weighted extremising). Report CC and CW slices separately. | G4 | [E] K07, K22 | a13, d02, d03, d05, d07, d13 |
| 4 | Cluster by meaning for free-text answers; by test behaviour for code. | S4, S7 | [E] K08 | a20, b18, c11, d07, d11 |
| 5 | Never score confidence with gamma or a bare correlation; never trust ECE alone. | metric | [E] K01; ECE caveat K10 is single-source but follows from the maths | a02, b15, c06, a19 |
| 6 | Do not rely on prompting for calibration; do not use verbal confidence as the stop signal. Already in 4b; this adds Kapoor, Yona, Leng, Xiong. | 4b (confirm) | [E] K14 | a22, a23, b21, b22, c22 |
| 7 | Use at least 400 items per arm, or a hierarchical estimate, for any efficiency (M-ratio) comparison. Otherwise use AUROC2 plus ECE with bootstrap intervals. | metric | [E] K05 | b05, b06, b07 |
| 8 | Verify the grader against human labels before reading any confidence score. | metric | [S] K16 (the logic is general) | b24, d20 |
| 9 | Keep reader-facing text short. Long explanations raise human trust without raising discrimination. | output wording | [E] K19 | a21, c14, c15, d18, d19 |

### Test first

| # | Item | Schema part | Status and claim | Evidence ids |
|---|---|---|---|---|
| T1 | Agreement vs verbalised vs token confidence, equal tokens, on the agent's own model. | G1, S0 | [C] K06, K09, K26 | a18, d15, d16, d17 |
| T2 | High-agreement-wrong rate and a cheap breaker (different framing, tool call, test run). | G4 | [S] open gap K23, K28 | d12, d13, d07 |
| T3 | Adaptive stop on agreement (Dirichlet rule) instead of fixed k. | G12, S3 | [S] K27 | d10 |
| T4 | CISC-style confidence-weighted vote (P(True) self-check on a cached prefix) vs plain majority, counting check cost. | S7 | [S] K11, K12, K29 | c18, c19, d08, d06 |
| T5 | Per-task-family calibration map from agreement share to accuracy. | memory, S0 class record | [S] K15, K24 | a25, b11, d14 |
| T6 | Low agreement as a trigger into S6 (impasse). | S6, G1 | [S] extension of K06 | a15, c21 |
| T7 | Window or tail token confidence to prune samples, when logprobs exist. | S3, S4 | [S] K13 | c20, d09 |
| T8 | Reader-facing wording: "k of n independent attempts agreed" in first-person wording. | output | [S] K19 | d18, d19 |
| T9 | WQD check before any confidence-based selection among candidates. | S7 | [S] K12 | c19 |
| T10 | Blend agreement with verbal confidence (Avg-Conf or Pair-Rank style). | S7 | [S] | b16, c07 |

## 8. Concrete tests on our bench

General setup:

- Both arms use the same total token budget, including self-check, judge and clustering calls and setup (G7).
- At least 400 items per arm when the metric is M-ratio. At least 200 with bootstrap CIs for AUROC2 or ECE. Rough cost at 400 items x 10 samples x 3,000 tokens is about 12 million tokens per arm (my estimate, K30), so run few arms.
- Report accuracy, AUROC2 (many-level), ECE, WQD where relevant, and results split by easy/hard and CC/CW slices.
- Trusted graders only; spot-check 100 labels by hand (b24).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 head to head | Arithmetic and word problems with exact answers; short factual QA; a code slice with tests | (a) 1 sample + verbalised confidence; (b) k=5 samples + agreement share; (c) 1 sample + token confidence if logprobs exist; (d) blend of a and b | AUROC2, ECE after a held-out map, WQD | Arithmetic: b above a by 15+ AUROC points on an older model (Xiong 54.8 to 92.7), less for a modern model. Other sets: 0 to 5 points. With a reasoning model, a may close most of the gap (Yoon). |
| B2 consensually wrong slice | 60+ items where the plausible answer is a known misconception or a plausible buggy program, matched with 60+ ordinary items | Agreement alone; agreement + second framing; agreement + tool or test | Rate of (agreement at least 0.8 and wrong); sign of the agreement-accuracy slope on the slice | Slope near zero or negative on the slice (Koriat, Farquhar). Framing or test arm should lower the high-agreement-wrong rate; size unknown. |
| B3 adaptive stop | Mixed-difficulty arithmetic and QA | (a) fixed k=5; (b) Dirichlet stop at 0.95, max 8; (c) fixed k equal to b's mean | Accuracy at equal mean tokens | b beats c by 0.5-2 points, or matches a with about 3x fewer samples (Aggarwal, 2023 models). |
| B4 CISC | Short-answer arithmetic and QA | (a) plain majority, budget 10; (b) P(True)-weighted vote, budget 10 plus check tokens; (c) plain majority at b's total tokens | Accuracy; WQD | b minus c about 0 to 1.6 points. WQD near 62% for P(True); if near 52%, abandon. Check the CW slice separately (Koriat 2015). |
| B5 calibration map | Two task families with different base rates | (a) raw agreement share; (b) map fitted on same family; (c) map fitted on the other family | ECE, Brier skill | b halves ECE or better. c is worse than b and may be worse than a (Spiess). Use 64+ labelled points. |
| B6 impasse trigger | Items with a check | (a) S6 fires on failed check only; (b) S6 also fires when agreement is below threshold; (c) random trigger at b's rate | Accuracy at equal tokens; right-to-wrong and wrong-to-right flips | b above c; b at least equal to a on items with no check. Small effect expected. |
| B7 metric agreement | Same runs as B1 | Score the same arms with AUROC2, WQD, and log M-ratio on a binary-framed subset | Rank of arms under each metric | Ranks mostly agree for a fixed model. Disagreements (Servajean) flag a difficulty confound. |
| B8 reader wording (small human panel) | 40 items shown to 30+ readers | (a) bare answer; (b) answer + "k of n attempts agreed" in first person; (c) answer + long explanation | Human accuracy; human AUC | b above a by a few points (Kim: +8.9 for a hand-set hedge); c shows lower AUC (Steyvers). |
| B9 token filter (only if logprobs) | Hard math | (a) majority of k; (b) drop bottom 10% of window-confidence traces, then majority | Accuracy at equal tokens | 0-5 point gain; small drops possible from overconfident wrong traces. |

## 9. What does not transfer, and why

- **One decision-maker with a memory trace vs resampling from one distribution.** Samples from one model share errors (G4, SDRM rho). A person's repeated sampling also shares errors, which is Koriat's consensually wrong effect. This transfers as a warning, not as a guarantee.
- **The mapping from Koriat's model to LLM agreement is an analogy.** The Steyvers and Peters review asserts the link (c02). No source tests the mechanism on an LLM. Koriat's own papers were not opened for numbers.
- **M-ratio and meta-d' assume a binary type 1 decision and an equal-variance Gaussian model.** Open QA has no two-choice decision (b23). Using it on LLMs needs a binary framing. Cacioli used a model-free substitute. Dai used a single binarised threshold.
- **M-ratio needs hundreds of trials.** Agent trials are cheaper than human trials, but each costs tokens. See the budget in section 8.
- **Fine-tuning results (Lin, Kapoor, Leng) do not apply.** The agent is a scaffold with no training.
- **DeepConf and self-certainty need logprobs.** A plain chat API has none. Only the consensus-stop part transfers (d09, d10).
- **Human-pair amplification.** Pairs of people differ from voting over samples, but the lesson (weighting by confidence amplifies the majority) is the same. Check it, do not assume it.
- **Human domain generality (5 of 6 correlations) does not guarantee it in models.** Cacioli found weakest efficiency in Science and Technology for all four models and no stable accuracy link. Calibrate per task family.
- **Older-model results.** Wang, Xiong, Kuhn and Aggarwal used 2022-2023 models; Kuhn used OPT. Gains may be smaller for current models that are better at verbal confidence.
- **Human rating scales vs a 0-100 verbal scale vs 0..k agreement.** A natural 0..k scale avoids the discretisation problem of the verbal scale (Dai).
- **Dunning-Kruger reading.** The low-performer pattern is partly a type 1 noise effect (a06). Weak confidence on hard items is expected from the maths and is not proof of poor self-knowledge.

## 10. Open questions

1. Does agreement across k samples of a current frontier reasoning model beat verbalised and token confidence at equal tokens, on open-ended and code tasks (gap 1, K26)?
2. How often is high agreement wrong for current LLMs, and which cheap check (different framing, tool, test) breaks false consensus best (gap 2, K23)?
3. What are the original Koriat 2012 effect sizes and N, and were there failed replications? We found none but did not search hard (gap 3).
4. Is the agreement-to-accuracy map stable across tasks and models? Only a code token-confidence map has been tested, and it failed across kinds (K24).
5. Which metric should grade the agent: AUROC2, log M-ratio or WQD, given type 1 dependence and AUROC2/M-ratio disagreement (gap 5, K30)?
6. Does P(True) weighting still pay on reasoning models once check cost is counted without prefix caching (gap 6)?
7. Can agreement among partial traces replace token-window confidence on API models (gap 7)?
8. Do Cacioli's efficiency results hold for large instruction-tuned and reasoning models, and is the accuracy independence real after the scorer fix (gap 8)?
9. Does showing agreement-derived confidence to a human change accuracy and overconfidence (gap 10)?
10. How does sampling temperature affect agreement confidence for modern models? Cacioli found token information flat across temperature; Kuhn found an intermediate optimum for semantic entropy.
11. Can a reworded-problem resample serve as a cheap, less correlated sample (relevant to G4, S1, O6), or does it only add noise?
12. Does Koriat's replicability account give a better score than raw agreement, such as the chance that a fresh sample repeats the choice, estimated by the Dirichlet model in 4.3?

## 11. Sources

[V] = opened and read (as recorded in the evidence files). [M] = snippet, abstract only, or second-hand.

**Measurement**

- [V] Fleming and Lau (2014) How to measure metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4097944/ (also https://doi.org/10.3389/fnhum.2014.00443)
- [V] Guggenmos (2021) Measuring metacognitive performance: type 1 performance dependence and test-retest reliability. https://pmc.ncbi.nlm.nih.gov/articles/PMC8633424/
- [V] Fleming (2017) HMeta-d: hierarchical Bayesian estimation of metacognitive efficiency. https://pmc.ncbi.nlm.nih.gov/articles/PMC5858026/
- [V] Rahnev et al. (2020) The Confidence Database. https://pmc.ncbi.nlm.nih.gov/articles/PMC7565481/
- [V] Mazancieux et al. (2020) Is there a G factor for metacognition? https://pmc.ncbi.nlm.nih.gov/articles/PMC7397761/
- [V] Rahnev and Denison (2018) Suboptimality in perceptual decision making. https://pmc.ncbi.nlm.nih.gov/articles/PMC6110994/
- [V] Guo et al. (2017) On calibration of modern neural networks. https://arxiv.org/abs/1706.04599
- [M] Galvin, Podd, Drga, Whitmore (2003) Type 2 tasks in the theory of signal detectability. No URL recorded.
- [M] Maniscalco and Lau (2012) A signal detection theoretic approach for estimating metacognitive sensitivity from confidence ratings. https://doi.org/10.1016/j.concog.2011.09.021
- [M] Nelson (1984) A comparison of current measures of the accuracy of feeling-of-knowing predictions. https://doi.org/10.1037/0033-2909.95.1.109
- [M] Masson and Rotello (2009) Sources of bias in the Goodman-Kruskal gamma coefficient. https://doi.org/10.1037/a0014876

**Koriat and human consensus**

- [V] Koriat (2025) Subjective confidence as a monitor of the replicability of the response. https://pmc.ncbi.nlm.nih.gov/articles/PMC12231820/
- [M] Koriat (2012) The self-consistency model of subjective confidence. https://pubmed.ncbi.nlm.nih.gov/22022833/ (also https://doi.org/10.1037/a0025648)
- [M] Koriat (2008) Subjective confidence in one's answers: the consensuality principle. https://pubmed.ncbi.nlm.nih.gov/18605880/ (also https://doi.org/10.1037/0278-7393.34.4.945)
- [M] Koriat (2011) Subjective confidence in perceptual judgments. https://pubmed.ncbi.nlm.nih.gov/21299320/
- [M] Koriat (1976) Another look at the relationship between phonetic symbolism and the feeling of knowing. https://pubmed.ncbi.nlm.nih.gov/21287029/
- [M] Koriat (1997) Monitoring one's own knowledge during study: a cue-utilization approach. https://doi.org/10.1037/0096-3445.126.4.349
- [M] Koriat (2015) When two heads are better than one and when they can be worse: the amplification hypothesis. https://pubmed.ncbi.nlm.nih.gov/26168039/

**LLM confidence and uncertainty**

- [V] Wang et al. (2022/2023) Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221
- [V] Lin, Hilton, Evans (2022) Teaching models to express their uncertainty in words. https://arxiv.org/abs/2205.14334
- [V] Lin, Hilton, Evans (2021) TruthfulQA. https://arxiv.org/abs/2109.07958
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975
- [V] Kuhn, Gal, Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664
- [V] Farquhar et al. (2024) Detecting hallucinations in large language models using semantic entropy. https://www.nature.com/articles/s41586-024-07421-0
- [V] Kapoor et al. (2024) Large language models must be taught to know what they don't know. https://arxiv.org/abs/2406.08391
- [V] Yona et al. (2024) Can LLMs faithfully express their intrinsic uncertainty in words? https://arxiv.org/abs/2405.16908
- [V] Leng et al. (2025) Taming overconfidence in LLMs: reward calibration in RLHF. https://arxiv.org/abs/2410.09724
- [V] Ji-An et al. (2025) Language models are capable of metacognitive monitoring and control of their internal activations. https://arxiv.org/abs/2505.13763
- [V] Taubenfeld et al. (2025) Confidence improves self-consistency in LLMs (CISC). https://arxiv.org/abs/2502.06233
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260
- [V] Aggarwal et al. (2023) Let's sample step by step: Adaptive-Consistency. https://arxiv.org/abs/2305.11860
- [V] Kang et al. (2025) Scalable best-of-N selection for LLMs via self-certainty. https://arxiv.org/abs/2502.18581
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Spiess et al. (2024) Calibration and correctness of language models for code. https://arxiv.org/abs/2402.02047
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489
- [V] Mei et al. (2025) Reasoning about uncertainty: do reasoning models know when they don't know? https://arxiv.org/abs/2506.18183
- [V] Dai and Wang (2026) Beyond 0-100: how confidence scale design shapes verbalized confidence and LLM metacognition. https://arxiv.org/abs/2603.09309
- [V] Cacioli (2026) Do LLMs know what they know? Measuring metacognitive efficiency with signal detection theory. https://arxiv.org/abs/2603.25112
- [V] Servajean and Servajean (2026) Measuring (some aspects of) the metacognition of AI. https://arxiv.org/abs/2603.29693
- [V] Steyvers and Peters (2025) Metacognition and uncertainty communication in humans and LLMs. https://arxiv.org/abs/2504.14045
- [M] Cash et al. (2025), cited in Steyvers and Peters; no URL recorded.
- [M] Griot et al. (2025) Large language models lack essential metacognition for reliable medical reasoning. https://doi.org/10.1038/s41467-024-55628-6

**Readers (humans)**

- [V] Steyvers et al. (2025) What large language models know and what people think they know. https://arxiv.org/abs/2401.13835
- [V] Sun, Li, Wang, Goette (2025) Large language models are overconfident and amplify human bias. https://arxiv.org/abs/2505.02151
- [V] Kim et al. (2024) "I'm not sure, but...": uncertainty expression, user reliance and trust. https://arxiv.org/abs/2405.00623
