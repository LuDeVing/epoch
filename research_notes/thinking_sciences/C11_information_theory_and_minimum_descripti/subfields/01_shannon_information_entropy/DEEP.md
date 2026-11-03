# Shannon information, entropy: deep document

*Subfield C11.01. Focus: uncertainty and code length. Why it matters for our agent: S7 probe choice (which test or question to run next). Evidence: evidence_a-d.jsonl (ids a01-d16), claims K01-K32 in claims.jsonl, cross-check in critique.md. Marks: [V] page or PDF text opened, [M] snippet or memory only. Status: [E] established, [S] single-source, [C] contested.*

Honest summary up front. The theory is solid and old. The LLM evidence is one small cluster: choosing questions by expected information gain (EIG) helps a lot in closed games (20 Questions, diagnosis, Battleship) and has never been tested at equal tokens on open reasoning. Semantic entropy as a confidence gate comes from one research group. Everything we propose for the schema is therefore a test, not a fact, except a few small items listed in section 7.

## 1. What it is

Entropy is a number for how uncertain you are. For outcomes with probabilities p1..pn, H = -sum p_i log2 p_i bits. Two equal outcomes give 1 bit. Four give 2 bits. A certain outcome gives 0.

Three linked ideas matter here.

- **Uncertainty.** H measures how much choice remains among hypotheses.
- **Code length.** H is the floor on average bits per symbol for any lossless code (source coding theorem). A model that predicts well can compress well, and a model that compresses well predicts well.
- **Information gain.** The expected drop in entropy from running a test is the mutual information between the unknown and the test result. This is the score used to pick the "most informative" question (Lindley 1956 [M]; Cover and Thomas 2006 [M]).

For our agent only the third idea is a direct lever. S7 has to choose a probe: a held-out check, a mutated input, a clarifying question, a candidate program to run. Shannon gives a principled score for "which probe removes the most doubt". The second idea gives two side uses: log-loss as a quality signal, and entropy over answer meanings as a confidence gate (G1, G4).

What it is not. Entropy is about the distribution over a defined set of alternatives. It says nothing about whether the right alternative is in the set. It is silent on meaning unless you cluster by meaning. It does not say what the right answer is.

## 2. History and theories in depth

**Shannon 1948 (a01-a06, b01, b02, all [V]).** Shannon asks for a measure H(p1..pn) of choice. He lists three demands: H is continuous in the p_i; with equal probabilities H grows with n; and if a choice is split into successive choices, H is the weighted sum of the parts. Theorem 2: the only H meeting these is H = -K sum p_i log p_i. The worked split example is H(1/2,1/3,1/6) = H(1/2,1/2) + 1/2 H(2/3,1/3). K sets the unit; log base 2 gives bits. He says himself the theorem is not essential. The real support is that the measure works (coding, channels). The axioms make entropy plausible; they do not prove it is the only sensible measure of uncertainty.
- Relative entropy = H / Hmax is the best possible compression in the same alphabet. Redundancy = 1 - relative entropy.
- He approximates English with six levels over 27 symbols (letters and space), from zero-order to word-level (a03).
- He puts redundancy of ordinary English near 50% for context up to about 8 letters, noting that if half the letters can be deleted and restored, redundancy is above 50% (a04, b01).
- Rate of transmission R = H(x) - H_y(x). Source coding: rate limit C/H symbols per second. Theorem 17 and 20: capacity of a band W with white thermal noise of power N and signal P is C = W log((P+N)/N) (a05, a06, b02).

**Shannon 1951 (a07-a09, b03, b04, [V]).** A direct experiment: show a person text and have them guess the next letter. The number of guesses gives bounds. Worked numbers: F1 = 4.14 bits, F2 = 7.70 - 4.14 = 3.56 bits, and 11.82 / 4.5 = 2.62 bits per letter. Upper bound on bits per letter by context length N = 1,2,3,4: 4.03, 3.42, 3.0, 2.6; at N=100 about 1.3. Lower bound: 3.19, 2.50, 2.1, 1.7; at N=100 about 0.6. In an example passage, 79 of 102 symbols were right on the first guess. The upper bound holds for any predictor; the lower bound only for ideal prediction. So redundancy rises from about 50% (1948, short context) to about 75% (1951, 100 letters). This is not a contradiction. It shows that measured uncertainty falls as more context is allowed.

**Cover and King 1978 (a26, [M]).** Gambling estimate by humans, about 1.3 bits per letter, in line with Shannon's upper bound. Not opened. Treat as unverified (d16 could not open it).

**Brown et al. 1992 (a10, [V]).** A word trigram model trained on 582.755 million words gives 1.75 bits per character on the Brown Corpus (5.96 million characters, 95 printable ASCII). Baselines: 8 bits ASCII, 7 packed, 4.46 Huffman, 4.43 Unix compress, 4.20 adaptive Lempel-Ziv. This is a cross-entropy upper bound, so it is about the model, not the truth.

**Lindley 1956 and Bayesian experimental design (a27, [M]).** Expected information gain of an experiment = expected drop in posterior entropy = mutual information I(X;Y). This is the bridge from Shannon to probe choice. Not opened.

**Human information search (b05-b08, b26, a28; mostly [M]).** Oaksford and Chater 1994 model the Wason selection task as optimal data selection under a rarity assumption. Nelson 2005 compares Bayesian diagnosticity, probability gain, impact and information gain as descriptions of human question choice. Nelson et al. 2010 find behaviour differs between verbal summary statistics and experience-based learning, with probability gain preferred in Experiment 3. Crupi et al. 2018 apply generalised information measures to existing data. Coenen, Nelson and Gureckis 2019 list nine open questions and argue optimal experiment design is not yet a good theory of human inquiry. Net: whether people use Shannon gain, probability gain or impact is unsettled [C]. Only Wikipedia was opened on the Wason task (d16): in Wason's original task fewer than 10% found the correct solution.

**Prediction as compression in the LLM era (a11-a14, c20, c21).** Deletang et al. 2024 and Huang et al. 2024 revive the 1951 link: a language model plus arithmetic coding is a compressor. Hoffmann et al. 2022 fit a loss with an irreducible term read as the entropy of natural text.

**Uncertainty over meaning (a15-a18, b09, b12, c01-c06).** Kuhn, Gal and Farquhar 2023 point out that token entropy mixes wording with meaning. They cluster sampled answers by bidirectional entailment and take entropy over clusters. Farquhar et al. 2024 (Nature) extend it to 30 task-model combinations. Kossen et al. 2024 train probes to predict it from one generation.

**EIG for LLM question asking (a19-a25, b14-b19, c09-c19, d04-d10).** Since 2023 a cluster of papers scores candidate questions by EIG over a hypothesis set: Uncertainty of Thoughts (UoT), BED-LLM, Active Task Disambiguation, OPEN, Loose LIPS, DPO on EIG pairs. Sections 3 and 6 have the numbers.

## 3. Core findings with exact numbers

Status: [E] established, [S] single-source, [C] contested. Claim ids are in claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Entropy is the unique measure under 3 axioms; floor on code length | H(1/2,1/3,1/6) = H(1/2,1/2) + 1/2 H(2/3,1/3); channel C = W log((P+N)/N) | Shannon 1948 (a01-a06) [V] | [E] K01 |
| English redundancy about 50% at ~8 letters | relative entropy H/Hmax; deleting 50% of letters is restorable | Shannon 1948 (a04, b01) [V] | [E] K02 |
| Redundancy about 75% at 100 letters | upper bound 4.03, 3.42, 3.0, 2.6 for N=1-4, about 1.3 at N=100; lower 3.19, 2.50, 2.1, 1.7, about 0.6; 79/102 first-guess hits | Shannon 1951 (a07-a09, b03) [V] | [E] K02 |
| Word trigram gives 1.75 bits/char | 582.755M training words; 5.96M test chars; vs 4.20 adaptive LZ, 4.43 compress, 4.46 Huffman | Brown et al. 1992 (a10) [V] | [E] K02 |
| Gambling estimate about 1.3 bits/letter | not opened | Cover and King 1978 (a26) [M] | [S] K25, unverified |
| LLM + arithmetic coding beats classical compressors | enwik9: gzip 32.3%, LZMA2 23.0, Transformer 3.2M 17.0, Llama 2 7B 8.9, Chinchilla 1B 11.3, 7B 10.2, 70B 8.3; ImageNet patches 43.4% vs PNG 58.5%; LibriSpeech 16.4% vs FLAC 30.3% | Deletang et al. 2024 (a11, c20) [V] | [S] K03 |
| Bigger models lose once parameter bytes are counted (small data) | 2 bytes per parameter (float16); two-part code | Deletang et al. (a12) [V] | [S] K05 |
| Compression tracks benchmark score | Pearson -0.93, RMSE 3.1% (average); HellaSwag -0.881, TriviaQA -0.951, MMLU -0.890 | Huang et al. 2024 (c21) [V] | [S] K04 |
| Loss law with an irreducible term | E=1.69, A=406.4, B=410.7, alpha 0.34, beta 0.28; E probably nats (about 2.44 bits per token, inferred) | Hoffmann et al. 2022 (a14, d12) [V] | [S] K05, K32 |
| Semantic entropy beats distinct-answer count | AUROC 0.77 vs 0.66 (CoQA); 0.83 vs 0.79 (TriviaQA); mean distinct meanings correct vs wrong 1.27 vs 1.77 and 1.89 vs 3.89; OPT 2.7B-30B; 8000 questions per set | Kuhn et al. 2023 (a15, b09, c02) [V] | [S] K06 |
| Entailment check is accurate | about 95% (92.7% TriviaQA, 95.5% or 95.3% CoQA); 300 hand-labelled generations | Kuhn et al. 2023 (a15) [V] | [S] K06 |
| Semantic entropy detects confabulation | AUROC 0.790 vs naive entropy 0.691, P(True) 0.698, embedding regression 0.687; 30 task-model combinations; 0.78-0.81 across LLaMA 2, Falcon, Mistral 7B-70B | Farquhar et al. 2024 (a17, c04) [V] | [S] K07, K08 |
| Temperature trade-off | best 0.5 in Fig 3b; sample accuracy about 61% hot vs over 92% cooler | Kuhn et al. 2023 (a16, c03) [V] | [E] K10 |
| Probes predict semantic entropy cheaply | AUROC 0.7-0.95; SEP minus accuracy probe in-distribution: Mistral-7B +2.8 (se 1.4), Phi-3 +2.1 (0.8), Llama-2-7B -0.5 (2.6), Llama-2-70B +1.3 (0.7); long form -1.9 (7.5), -2.0 (2.1) | Kossen et al. 2024 (a18, b12, c06) [V] | [S] K09 |
| Self-evaluation is a weaker baseline | 52B models calibrated on multiple choice in right format; RLHF policies miscalibrated at T=1; 10-shot reimplementation worse than semantic entropy | Kadavath 2022 (b13, c07, c08) [V] | [E] K11 |
| Verbalised confidence beats token probabilities for chat models | expected calibration error cut by a relative 50%; n=10 samples; n=20 no gain | Tian et al. 2023 (d05) [V] | [S] K30 |
| EIG probe choice roughly doubles 20 Questions | mean +37.4 points; Animals GPT-4o 45 to 93, GPT-4o-mini 44 to 88, Llama-3.1-8B 8 to 63; 100 targets/cell, se 2-5; Celebrities Mistral-Large 19 to 91; Things Llama-8B 10 to 26 | BED-LLM 2026 (a21, b16) [V] | [S] K12 |
| Raw entropy weaker than EIG | Animals 88 vs 79 (mini), 93 vs 88 (4o), 63 vs 54 (Llama-8B); Celebrities Qwen-72B 84 vs 59 | BED-LLM (a22, b17) [V] | [S] K13 |
| Hypothesis filtering is the biggest factor | no filter (ICL Beliefs) Animals GPT-4o 25 vs 93; mini 18 vs 88; Implicit Max 70 | BED-LLM (b17, b25) [V] | [S] K14 |
| Static likelihood beats history-updated | 13 of 15 cells; e.g. Animals GPT-4o 93 vs 86, Qwen 95 vs 89, Celebrities Qwen 84 vs 70 | BED-LLM App. F.3 (d07) [V] | [S] K29 |
| UoT raises success | +38.1% mean over direct prompting; Llama3-70B +46.6%; vs CoT-SC +33.8, Reflexion +29.9, original ToT +28.3, adapted ToT +12.4; pruned UoT vs adapted ToT +7.36 | Hu et al. 2024 (a19, b14, b15, c10) [V] | [S] K17 |
| UoT GPT-4 per dataset | DX 97.0 vs 89.4; MedDG 87.9-88.0 vs 74.9; FloDial 67.3-67.8 vs 42.5 (main table 43.7 on a different row); 20Q Common 70.9 vs 49.0; Thing 36.8 vs 30.8 | Hu et al. (c09, c10) [V] | [S] K17 |
| UoT on Llama 3 | Common 47.7 to 56.5; Thing 14.8 to 24.8; DX 80.1 to 90.1; FloDial 29.9 to 46.4 | Hu et al. (c11) [V] | [S] K17 |
| Unaided LLM questions have low EIG | human mean EIG 1.27 (best 3.61, 97% above 0; N=40, 605 pairs, 18 boards); GPT-4/CodeLlama k=1 about 0.65-0.77; k=5 near human mean; k=10 above; k=50 below best human | Grand et al. 2024 (b21, c14-c16) [V] | [S] K15 |
| DPO on high-EIG questions | success 56.7 to 68.9%, EIG 0.34 to 0.45, turns 7.1 to 5.2; plain fine-tune 46.6%; Things 51.1 to 61.1%; abstract targets 7.7 to 23.1% | Mazzaccara et al. 2024 (c12, c13) [V] | [S] K16 |
| ChatGPT first split good, later weak | 7.24 questions per game on 8 candidates; 73.77% constraint-seeking; optimal agent uses log2(N)-1 constraint questions | Bertolazzi et al. 2023 (a20) [V] | [E] K20 |
| Models weak at choosing the question on logic/planning | best 40-50% on Logic-Q and Planning-Q; near ceiling on arithmetic (GPT-4o GSME-Q 99.34%, GSM-Q 92.01%) | QuestBench 2025 (d10) [V] | [S] K31 |
| Invented hypotheses help on ARC but coverage binds | direct 17%, programs only 23%, hypotheses 30%, human-selected 33%, human-written 45%, Icecuber 43%; correct hypothesis present in 49 of 100 tasks; 28 of 30 solved had one | Wang et al. 2023 (d04) [V] | [S] K28 |
| Answer-agreement stop rules save samples | ESC: MATH -33.8% to Coin Flip -84.2%, GSM8K -80.1%; Adaptive-Consistency 4.4x (GPT-3.5, 76.4 vs 76.2), up to 7.9x; DeepConf up to -84.7% tokens | d02, d03, d14 [V] | [E] K26 |
| Confident-wrong items pass a confidence gate | GPT-OSS-120B AIME25: DeepConf@512 99.9 vs cons@512 97.0 vs pass@1 91.8; overconfident wrong traces reported | Fu et al. 2025 (d14) [V] | [E] K10, K27 |
| Info gain per CoT step separates correct from wrong | toy arithmetic 0.96, 0.98, 0.06 vs outcome reward model 0.77, 0.98, 0.54 | Ton et al. 2024 (c19) [V] | [S] K21 |
| Policy entropy collapses early in RL | over 95% of entropy drop and gain early; Clip-Cov/KL-Cov +15.0% AIME24, +14.6% AIME25 (Qwen2.5-32B) | Cui et al. 2025 (c22) [V] | [S] K22 |
| Preference elicitation: BOED picks, LM words | OPEN beats LM-only pairwise; GATE N=388; avg entropy in p(yes) 0.77 bits | Handa 2024; Li 2023 (b19, c17, a24) [V] | [E] K19 |
| Human choice of tests: Shannon vs probability gain | not separable in past data; probability gain favoured under experience-based learning | Nelson 2005, 2010; Crupi 2018 (b05-b08) [M] | [C] K23 |

## 4. Mechanisms and models

### 4.1 Entropy and its additivity
H(p) = -sum p log2 p. Additivity: a plan of questions can be scored step by step, and the step gains sum to the whole gain. Engineer's check: for a toy hypothesis set, the sum of per-question gains in a chosen order must equal H(prior) - H(posterior after all answers). If it does not, there is a bug (K01).

### 4.2 Expected information gain (EIG) probe score
Given a hypothesis list h_1..h_n with weights w_i summing to 1 (the belief), and a candidate probe q with possible outcomes y:

1. For each h_i and outcome y, get p(y | h_i, q). Either a deterministic check by code, or an LLM-estimated likelihood.
2. Predictive p(y | q) = sum_i w_i p(y | h_i, q).
3. Posterior w_i(y) = w_i p(y | h_i, q) / p(y | q).
4. EIG(q) = H(w) - sum_y p(y | q) H(w(y)). Equivalent form: H(Y|q) - sum_i w_i H(Y | h_i, q), the predictive entropy minus the expected likelihood entropy.
5. Pick q with the highest EIG.

Why the second form matters (BED-LLM, d09, b17): raw predictive entropy H(Y|q) rewards a question whose answer is noisy even given the truth. The ice-cream question in the film-genre example has high predictive entropy but EIG = 0. Subtracting the expected likelihood entropy removes it. Measured effect: EIG beat raw entropy by 9, 5 and 9 points on Animals (mini, 4o, Llama-8B) and by 25 points on Celebrities Qwen-72B (84 vs 59).

### 4.3 The BED-LLM loop (a21, b16, b17, d07-d09)
1. Keep a belief as a set of sampled hypotheses (for example candidate animals), generated by the LLM and then filtered to be consistent with every answer so far.
2. Propose candidate questions with the LLM.
3. Score each by EIG (the likelihood p(y | h, q) comes from LLM prompts).
4. Ask the best. Update. Repeat.

Findings that decide the engineering:
- Filtering is key: without it success falls 93 to 25 (4o), 88 to 18 (mini).
- A static likelihood prompt (no dialogue history) beat a history-conditioned one in 13 of 15 cells. Keep history in the belief set, not in the scoring prompt.
- Cost: extra LLM calls. Wall-clock for Qwen-72B Animals was 2h30m vs 3h10m for the Entropy variant (K12).

### 4.4 Uncertainty of Thoughts (a19, b14, b15, c09-c11)
Builds a tree of candidate questions, simulates the possible answers, computes an information-gain reward for each node, and propagates reward up the tree. Reward variants in Table 3 (GPT-3.5 success %): UR 51.7/44.2/92.1/81.3/67.1; LTS 51.7/40.5/91.3/78.0/65.4; STS 51.3/35.1/89.4/82.3/63.4; PFS 37.9/36.9/89.4/81.3/67.1. Pruned UoT is cheaper and still above adapted ToT by 7.36. It uses more tokens than the baselines, so the comparison is not at equal tokens.

### 4.5 Semantic entropy as a gate (a15, a17, c04, c05)
1. Sample k answers (low temperature; 0.5 was best in one sweep).
2. Cluster answers by bidirectional entailment (A entails B and B entails A). A small model or an LLM judge does the entailment check; accuracy of the check was about 92.7-95.5%.
3. Cluster probability = share of samples (or summed sequence probability).
4. Semantic entropy = -sum over clusters of P(c) log P(c).
5. High value flags a likely wrong or confabulated answer. Metrics: AUROC for correctness; AURAC (accuracy after rejecting the highest-entropy fraction).

Implementation note for our case: G5 says grouping and voting are done by code. For ARC grids or code outputs, "meaning" is exact output equality, so clustering is free and needs no entailment model. Cluster share then equals the majority share, and semantic entropy reduces to the entropy of the vote distribution.

### 4.6 Stop rules on sampling (d02, d03, d13, d14)
- ESC: sample in windows (size 5; 8 for MATH) and stop when a whole window agrees.
- Adaptive-Consistency: stop when a Beta test says the top answer would stay top. The Beta check is about four orders of magnitude faster than Dirichlet or CRP variants and beat entropy and majority-share thresholds at equal cost.
- DeepConf: filter or stop traces by token confidence; online mode cut tokens up to 84.7%.

Sketch of the Beta check: with counts a (top answer) and b (all others), stop when P(p_top > 0.5) under Beta(a+1, b+1) exceeds a threshold such as 0.95. The threshold is a tuning knob. (This sketch is ours; the paper's exact test is not reproduced here.)

### 4.7 Information gain per reasoning step (c19)
Score a CoT step by the change in log p(correct answer | prefix). Needs the gold answer, so it is an offline evaluation tool, not an online control signal.

### 4.8 Compression as a measure (a11, c21)
Log-loss of a model on held-out text is a model-level quality number (Pearson -0.93 with average benchmark score, Huang). It is not shown to work per item. Do not use it as a per-answer correctness test without checking (critique GAP 8).

## 5. What holds up

### Holds up (replicated or definitional)
- Shannon's theory and the source coding bound are textbook. Entropy of English falls with context length. The 1948 and 1951 numbers differ because context lengths differ (K02).
- Token-level confidence is a poor guide to correctness for RLHF chat models. Several independent works agree (Kadavath 2022, Tian 2023, Farquhar 2024) (K11).
- LLMs choose informative questions poorly without help and keep asking after the answer is known (Bertolazzi 2023, Zhang 2024 as cited in BED-LLM; QuestBench) (K20, K31).
- Answer-agreement stopping saves 34-84% of samples at near-equal accuracy, in three independent papers (K26).

### Single-source, treat with care
- All "EIG doubles success" results (BED-LLM, UoT) are on closed, enumerable hypothesis sets: animals, celebrities, diagnoses, board positions, preference options. None on open reasoning.
- Semantic entropy results (K06-K09) are all from the Kuhn, Farquhar, Gal, Kossen group. Independence is low even though there are four evidence lines.
- Compression-tracks-intelligence (Huang) is one paper, at model level.
- BED-LLM authors note their Prompt-Only baseline is weaker than in some earlier work, so "doubling" depends on that baseline.

### Failures, limits and inconsistencies
- Low entropy does not mean right. A model that is consistently wrong has low semantic entropy. Confident-wrong traces pass the filter in DeepConf with GPT-OSS-120B (K10, K27).
- Sampling temperature: accuracy of sampled answers about 61% hot vs over 92% cooler; best 0.5 (K10).
- Semantic entropy probe vs accuracy probe is mixed in distribution (-0.5 to +2.8; long form -1.9 and -2.0), better out of distribution (K09).
- Plain fine-tuning on 20 Questions lowered success (46.6% vs 56.7% zero-shot). DPO on EIG pairs raised it to 68.9% (K16).
- Plain CoT hurt on 20 Questions with GPT-4 (UoT c10). In BED-LLM, CoT gave 55-62 vs Prompt-Only 44-45, far below EIG.
- Updating the likelihood prompt with history hurt in 13 of 15 cells (K29).
- In preference elicitation, raw entropy gave no gain over Prompt-Only (K13).
- UoT paper has an internal conflict: GPT-4 MedDG 88.0 vs 87.9, FloDial 67.3 vs 67.8, baseline 43.7 vs 42.5. Use the range. DX gain is small because the base is near ceiling (97.0 vs 89.4).
- Kuhn entailment accuracy: body 92.7/95.5, appendix 92.7/95.3. Use "about 95".
- Failed replications: none found, but third parties were not clearly seeking them. For Cover-King and Oaksford-Chater, no replication data could be opened (d16). That is a gap, not a result.

### Moderators
- Base model strength: gains are biggest for weak models (Llama-8B 8 to 63; GPT-4o 45 to 93) and shrink for strong ones (Active Task Disambiguation; UoT DX near ceiling) (K17, K18).
- Closed vs open hypothesis space: abstract targets stay hard after DPO (7.7 to 23.1%). On ARC, a correct hypothesis existed for 49 of 100 tasks (K28).
- Hypothesis quality: filtering gives 93 vs 25 (K14).
- Question type: models near ceiling on arithmetic questions but 40-50% on logic and planning (K31).
- Ceiling: Animals reaches 95, so differences among strong methods are inside se of 2-5 points.

### Interventions that worked and that did not
- Worked: EIG over a filtered hypothesis set; sampling k probes and picking by computed EIG (k=10 exceeds the human mean in Battleship); DPO on EIG pairs; Beta stop rule; verbalised probabilities; Semantic Entropy Probes out of distribution.
- Did not work: raw predictive entropy as the probe score in preference elicitation; unfiltered LLM beliefs; history-updated likelihood; plain fine-tune; forced CoT on 20 Questions; n=20 over n=10 samples for label-probability calibration.

## 6. Language models

How they behave on these tasks, what changed it, by how much.

**Choosing probes unaided.**
- 20 Questions, Prompt-Only: GPT-4o 45, GPT-4o-mini 44, Llama-3.1-8B 8 on Animals (a21). Split heuristic 78-83; CoT 55-62; Entropy ablation 79-88; full EIG 88-93. Ablation Implicit Max 70 on GPT-4o.
- Battleship (b21, c14, c15): LLM questions at k=1 have EIG 0.65-0.77 vs human mean 1.27. Valid-program rate 0.40 to 0.88 across rows; translation success about 75% (CodeLlama) and 88% (GPT-4). Sampling and ranking by EIG closes the gap: k=5 near human, k=10 above human mean (p<0.001 CodeLlama, p=0.01 GPT-4), k=50 still under the best human (3.61). The "grammar" row (0.36) is the probabilistic-grammar baseline, not an LLM.
- Candidate-split game (a20): ChatGPT is near-optimal at the first half-split, loses informativeness later, takes 7.24 questions per game on 8 candidates, and asks 73.77% constraint-seeking questions.
- Logic and planning questions (d10): 40-50% for the best models.

**What changed it.**
- Filtered hypothesis list + EIG: +37.4 points on average (BED-LLM). Largest part of the gain is the filtered belief; then EIG over raw entropy (5-25 points).
- UoT: +38.1% average; Llama3-70B +46.6%; GPT-4 20Q Common 49.0 to 70.9; Llama 3 FloDial 29.9 to 46.4.
- DPO with EIG labels: +12.2 points success on the INLG set, EIG +0.11, fewer turns (7.1 to 5.2). Things +10.0; Celebrities only +1.1 (71.1 to 72.2).
- Hypothesis Search on ARC (d04): 17 to 30% with GPT-4, n=100. Compute is not matched across rows.
- Active Task Disambiguation (b18, c18): EIG-based question choice gave higher solution accuracy with fewer test cases; open questions beat binary; the gap shrank for stronger models.

**Confidence and uncertainty.**
- Semantic entropy: AUROC 0.77/0.83 (OPT, 2023), 0.790 mean over 30 combinations (2024). Gap over naive entropy about 0.10 AUROC. P(True) 0.698.
- Tian 2023: verbalised probabilities for ChatGPT, GPT-4, Claude cut expected calibration error by a relative 50% versus token probabilities. Factual QA only.
- Agreement share tracks accuracy on GSM8K (d01, plot only, no coefficient). Imperfect-CoT prompt on LaMDA-137B: greedy 17.1 to 14.9, self-consistency recovers.
- DeepConf (d14): AIME25 with GPT-OSS-120B 99.9 (DeepConf@512) vs 97.0 (cons@512) vs 91.8 (pass@1). DeepSeek-8B AIME25 82.3 to 87.4 and Qwen3-32B AIME24 85.3 to 90.8 with a 10% filter.

**Training signals.**
- Compression: Chinchilla 70B 8.3% on text, 43.4% on image patches, 16.4% on speech, though trained on text.
- Policy entropy collapse in RL for reasoning (c22): R = -a exp(H) + b; Clip-Cov and KL-Cov keep entropy and add +15.0 and +14.6 points on AIME24/25.
- Information gain per step (c19): separates correct from wrong CoT in toy arithmetic.

**What is not shown.** No opened paper tests EIG probe choice on ARC or BrainTeaser at equal tokens. No opened paper tests probability gain for LLM agents. No opened paper tests semantic entropy proper on multi-step reasoning.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Each item has status and evidence ids (claims K, evidence a-d).

### Add now (established, small)
1. **S7 with G5: compute the score in code, not in the model's head.** If a probe is scored, count hypotheses and outcomes in code (entropy, split sizes). [E] K01, K11, K20; a01, b13, a20. LLMs ask well at the first split and then lose informativeness.
2. **S7 stop rule: stop probing when the belief set is resolved.** Stop when one hypothesis holds the weight (or one remains). LLMs keep asking after the answer is known. [E] K20; a20, a23. The exact threshold is a test (see UNKNOWNS); the principle is established.
3. **G4 and G1 refinement: agreement is a hint; low entropy is not proof.** Track the vote distribution per item; never pass an item on agreement alone. Run an independent check (G3) on items that pass the gate. [E] K10, K27; d14, a16, c03. (G4 already says agreement is a hint; this adds the confident-wrong point and the logging.)
4. **G7/G12: stop sampling early when the top answer is stable.** Use a Beta-style or window stop rule instead of fixed N. Saves 34-84% of samples at near-equal accuracy. [E] K26; d02, d03, d14. This is a sampling-cost rule, not a probe-choice rule.
5. **If confidence is needed at all, ask for verbalised multi-guess probabilities, not token probabilities.** [E] for the miscalibration K11 (b13, a17); [S] for the verbalised fix K30 (d05).

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Generate a hypothesis list, filter by consistency with all observed outputs, score candidate probes by EIG, pick the best | S7, memory (belief set) | [S] | K12, K13, K14; a21, b16, b17 |
| T2 | Compute EIG as predictive entropy minus expected likelihood entropy, never raw answer entropy | S7 | [S] | K13; a22, b17, d09 |
| T3 | Keep S-state history in the belief set only; score probes with a static likelihood prompt | S7, memory | [S] | K29; d07 |
| T4 | Sample k candidate probes (k about 5-10) and choose by computed EIG | S7 | [S] | K15; b21, c14-c16 |
| T5 | Measure hypothesis coverage before scoring; skip EIG if coverage is low | S0, S7 | [S] | K14, K28; d04 |
| T6 | Probability gain (expected drop in error) as probe score instead of Shannon EIG | S7 | [C] | K23; b05-b08, b26 |
| T7 | Semantic or cluster entropy as a gate, with exact-output clustering | S7, G1 | [S] | K06-K08; a15, a17, c04 |
| T8 | Verbalised top-3 probabilities as a gate signal | S7, G | [S] | K30; d05 |
| T9 | Log-loss or sample agreement of the agent's own answers as an item-level proxy | S0, S7 | [S], model-level only | K04; c21 |
| T10 | Information gain per CoT step as a step score (offline) | S6 | [S] | K21; c19 |
| T11 | Hypothesis-first probe choice on logic-style items vs unaided choice | S7 | [S] | K31; d10 |

Not to carry over: DPO training (K16), entropy-preserving RL (K22), semantic entropy probes (K09, need hidden states). All are training or open-model only.

## 8. Concrete tests on our bench

All arms get equal total tokens, setup and extra calls included (G7). Seeds fixed. Report mean, 95% interval and item count. Use at least 100 items per arm to see a 10-point effect at se about 4-5.

1. **EIG probe choice vs plain probe choice (T1, T2).** Items: BrainTeaser items needing a clarifying or verification step; ARC items with a choice between candidate checks; a closed 20-Questions-style set as a sanity check. Arm A: the model picks the next probe in one call. Arm B: model lists hypotheses, code filters them against all outputs, model proposes 5 probes, code computes EIG, best is run. Metric: final accuracy; probes to resolution. Expected: +10 to +30 points on the closed sanity set (BED-LLM); unknown on open items; none or negative if coverage is low (K28).
2. **Coverage cliff (T5).** Same as test 1, but bin items by whether the true answer is in the hypothesis list. Metric: arm B minus arm A within each bin. Expected: gain only where the truth is in the list; zero or below otherwise.
3. **Filtering ablation (T1).** Arm B with filtering vs without. Metric: accuracy. Expected: large drop without filtering (93 to 25 on 20 Questions).
4. **EIG vs raw entropy (T2).** Metric: accuracy. Expected: EIG +5 to +10 points; larger on noisy-answer probes.
5. **History in scoring (T3).** Static likelihood vs history-conditioned. Expected: static equal or better (13 of 15 cells).
6. **k-sample probes (T4).** k=1, 5, 10 candidate probes at equal tokens. Metric: mean EIG of chosen probe and accuracy. Expected: gain saturates near k=5-10; at equal tokens k=1 with more sampling elsewhere may win.
7. **Probability gain vs EIG (T6).** Same hypothesis list; score by expected error drop vs expected entropy drop. Metric: accuracy at fixed probe count. Expected: near-equal; probability gain better when the next step is a single final guess.
8. **Stop rule.** Rules: fixed budget; top weight above 0.9; EIG below 0.1 bits; Beta test. Metric: accuracy vs tokens; wasted probes after resolution. Expected: stop rules save 30-80% at equal accuracy.
9. **Gate (T7, T8, K27).** Sample 5-8 attempts per item. Signals: top-answer share, cluster entropy, verbalised top-3 confidence. Metric: AUROC for correctness; AURAC; accuracy among items with share above 0.8 plus a list of confident-wrong items. Expected: AUROC 0.75-0.85 on factual items; lower on ARC; a nonzero share of confident-wrong.
10. **Proxy check (T9).** Per-item answer log-loss vs correctness (open models only). Metric: AUROC. Expected: weak to moderate.

## 9. What does not transfer, and why

- **Shannon's channel theory (capacity, noise).** Our agent is not sending a message over a noisy channel. The channel framing explains nothing about a single answer.
- **English entropy numbers (1.3 bits per letter, 1.75 bits per char).** About text, not puzzle answers. Hoffmann's E=1.69 (nats, inferred) is a floor for web text, not for ARC grids. Do not compare E with Shannon's bits per letter (K32).
- **Compression-intelligence law (Huang).** Model-level across LLMs; not a per-item test.
- **Closed-set wins.** 20 Questions, Battleship and diagnosis have an enumerable hypothesis space where the answer is a member. ARC and open puzzles do not. The filtered beliefs carry the BED-LLM result; on ARC a correct hypothesis existed in 49% of tasks (K14, K28).
- **Semantic entropy on factual QA.** Tested on TriviaQA, CoQA, SQuAD, BioASQ, NQ-Open, SVAMP. Not multi-step reasoning. Not tested where the model is consistently wrong.
- **Semantic Entropy Probes, DPO, entropy-regularised RL.** Need weights or training. Out of scope for a scaffold (K09, K16, K22).
- **Oracle answers.** In many of these papers an oracle answers truthfully. Our probes are code runs and checks, where p(y | h) can be deterministic, which makes EIG cheaper and cleaner than for natural-language answers. This is an inference, not a measured result.
- **Token-level confidence.** Closed chat APIs may not give logprobs, and RLHF policies are miscalibrated anyway (K11).
- **Human inquiry theories (Oaksford-Chater, Nelson).** They describe what people do, not what an agent should do. Their relevance is the open question of EIG vs probability gain (K23).
- **UoT at full cost.** It uses more tokens than its baselines; it fails G7 until shown at equal tokens.

## 10. Open questions

1. At equal tokens, does EIG-over-hypotheses probe choice beat plain self-consistency or a single good prompt on open tasks (ARC, BrainTeaser) where the hypothesis set must be invented?
2. How good must the hypothesis list be? Is there a minimum coverage below which EIG is worse than prompt-only? (Evidence: one cliff on 20 Questions and 49% coverage on ARC.)
3. Does probability gain beat Shannon EIG as a probe score for an LLM agent? No LLM study found.
4. Does semantic entropy (or cluster share) work as a gate on multi-step reasoning, and how many confident-wrong items pass?
5. Which stop rule is best for EIG-based probe selection: entropy threshold, EIG threshold or fixed budget? Answer-sampling stop rules are studied; probe stop rules are not.
6. How accurate must p(y | h) be? The ice-cream case shows noisy answers hurt. No opened paper measures estimation error.
7. Does carrying belief-set history into the probe prompt help or hurt beyond 20 Questions? Only one setting tested.
8. Is item-level log-loss a usable correctness proxy? Only model-level evidence.
9. Are the Cover-King and Oaksford-Chater numbers right as quoted, and were there failed replications of the rarity-assumption model? Not opened.
10. What is the unit of Hoffmann's E? Inferred as nats (about 2.44 bits per token), not stated.
11. Is semantic entropy replicated outside the original group? Not found in what we opened.

## 11. Sources

[V] opened (PDF or page text read), [M] snippet or memory only.

**Shannon and classical**
- [V] Shannon (1948) A Mathematical Theory of Communication. https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf (a01-a06, b01, b02)
- [V] Shannon (1951) Prediction and Entropy of Printed English. https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf ; DOI https://doi.org/10.1002/j.1538-7305.1951.tb01366.x (a07-a09, b03, b04)
- [V] Brown, Della Pietra, deSouza, Lai, Mercer (1992) An estimate of an upper bound for the entropy of English. https://aclanthology.org/J92-1002.pdf (a10)
- [M] Cover and King (1978) A convergent gambling estimate of the entropy of English. https://doi.org/10.1109/TIT.1978.1055912 (a26)
- [M] Lindley (1956) On a measure of the information provided by an experiment. https://doi.org/10.1214/aoms/1177728069 (a27)
- [M] Oaksford and Chater (1994) A rational analysis of the selection task as optimal data selection. https://doi.org/10.1037/0033-295X.101.4.608 (a28)
- [M] Cover and Thomas (2006) Elements of Information Theory, 2nd ed. https://doi.org/10.1002/047174882X (a29)
- [V] Wason selection task (Wikipedia, for the under-10% figure). https://en.wikipedia.org/wiki/Wason_selection_task (d16)

**Human information search**
- [M] Crupi et al. (2018) Generalized information theory meets human cognition. https://pubmed.ncbi.nlm.nih.gov/29911318/ (b05, b26)
- [M] Nelson (2005) Finding useful questions. https://pubmed.ncbi.nlm.nih.gov/16262476/ (b06)
- [M] Nelson et al. (2010) Experience matters. https://pubmed.ncbi.nlm.nih.gov/20525915/ (b07)
- [M] Coenen, Nelson, Gureckis (2019) Asking the right questions about the psychology of human inquiry. https://pubmed.ncbi.nlm.nih.gov/29869025/ (b08)

**Compression and scaling**
- [V] Deletang et al. (2024) Language Modeling Is Compression. https://arxiv.org/abs/2309.10668 (a11-a13, c20)
- [V] Hoffmann et al. (2022) Training compute-optimal large language models. https://arxiv.org/abs/2203.15556 (a14, d12)
- [V] Huang et al. (2024) Compression Represents Intelligence Linearly. https://arxiv.org/abs/2404.09937 (c21)
- [V] Cui et al. (2025) The Entropy Mechanism of RL for Reasoning Language Models. https://arxiv.org/abs/2505.22617 (c22)
- [V] Ton et al. (2024) Understanding CoT in LLMs: an information-theoretic perspective. https://arxiv.org/abs/2411.11984 (c19)

**Uncertainty and confidence**
- [V] Kuhn, Gal, Farquhar (2023) Semantic Uncertainty. https://arxiv.org/abs/2302.09664 (a15, a16, b09, b10, b24, c01-c03, c26)
- [V] Farquhar, Kossen, Kuhn, Gal (2024) Detecting hallucinations in LLMs using semantic entropy. https://www.nature.com/articles/s41586-024-07421-0 (a17, c04, c05, c24, c25); PubMed page [M] https://pubmed.ncbi.nlm.nih.gov/38898292/ (b11)
- [V] Kossen et al. (2024) Semantic Entropy Probes. https://arxiv.org/abs/2406.15927 (a18, b12, c06)
- [V] Kadavath et al. (2022) Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221 (b13, c07, c08, d15)
- [V] Tian et al. (2023) Just Ask for Calibration. https://arxiv.org/abs/2305.14975 (d05, d11)
- [V] Wang et al. (2022) Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171 (d01)
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (d02, d13)
- [V] Li et al. (2024) Escape sky-high cost: early-stopping self-consistency. https://arxiv.org/abs/2401.10480 (d03)
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (d14)

**EIG and question asking with LLMs**
- [V] Choudhury, Williamson et al. (2026) BED-LLM. https://arxiv.org/abs/2508.21184 (a21-a23, b16, b17, b23, b25, d07-d09)
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (a19, b14, b15, c09-c11)
- [V] Bertolazzi, Mazzaccara, Merlo, Bernardi (2023) ChatGPT's information seeking strategy. https://aclanthology.org/2023.inlg-main.11.pdf (a20)
- [V] Mazzaccara, Testoni, Bernardi (2024) Learning to ask informative questions. https://arxiv.org/abs/2406.17453 (c12, c13)
- [V] Grand, Pepe, Andreas, Tenenbaum (2024) Loose LIPS sink ships. https://arxiv.org/abs/2402.19471 (b21, b22, c14-c16, c23)
- [V] Kobalczyk et al. (2025) Active Task Disambiguation with LLMs. https://arxiv.org/abs/2502.04485 (b18, c18)
- [V] Handa et al. (2024) Bayesian Preference Elicitation with Language Models (OPEN). https://arxiv.org/abs/2403.05534 (b19, c17)
- [V] Li, Tamkin, Goodman, Andreas (2023) Eliciting Human Preferences with Language Models (GATE). https://arxiv.org/abs/2310.11589 (a24, a25); abstract page [M] (b20)
- [V] Piriyakulkij, Kuleshov, Ellis (2024) Active preference inference. https://arxiv.org/abs/2312.12009 (d06)
- [V] Wang et al. (2023) Hypothesis Search. https://arxiv.org/abs/2309.05660 (d04)
- [V] Li, Kim, Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674 (d10)

Note: evidence lines b10, c23-c26 are plots or syntheses, not extracted numbers; no figure above rests on them alone.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C11.01-K10** (number corrected). Kuhn et al. App. B: 61% (hot, T=1.5) vs over 92% (cooler) is the accuracy of the semantic-equivalence clustering, not the accuracy of sampled answers. Corrected claim: Entropy signals have limits: a model that is consistently wrong has low semantic entropy (an inference from the definition; Farquhar et al. say it detects only confabulation); sampling temperature trades accuracy against diversity (best AUROC at T=0.5, Kuhn Fig 3b, TriviaQA/OPT-30B); at T=1.5 semantic-equivalence classification accuracy falls to 61% vs over 92% at lower temperatures; tests are mostly factual QA (TriviaQA, CoQA), not multi-step reasoning.
- **C11.01-K01** (now single-source: only one opened source, code check).
