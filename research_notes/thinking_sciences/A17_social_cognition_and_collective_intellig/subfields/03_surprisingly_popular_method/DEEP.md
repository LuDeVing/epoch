# Surprisingly popular method: deep document

*Folder: A17 social cognition and collective intelligence, subfield 03. Built from evidence_a-d.jsonl (ids a01-a28, b01-b26, c01-c26, d01-d19), claims.jsonl (A17.03-K01 to K27) and critique.md. Evidence ids are quoted as a02, b19 and so on. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The surprisingly popular (SP) method picks one answer from a crowd. It does not pick the most common answer. It picks the answer that is more common than the crowd predicted.

Each respondent gives two things:
1. Their own answer to the question.
2. A prediction of what share of the other respondents will give each answer.

Code then compares, for each answer, the actual vote share with the average predicted share. The answer with the largest positive gap wins. (a01, a11)

Worked example (Wikipedia, a11): "Is Philadelphia the capital of Pennsylvania?" Yes gets 65% of votes but was predicted at 75%, so the gap is -10. No gets 35% but was predicted at 25%, so the gap is +10. No wins, and No is correct.

Why it was proposed: majority vote fails when most people hold a common wrong belief and a few hold the right, rarer knowledge. Voters with the rare right view know the majority is probably wrong, so they predict a small share for their own answer. Naive voters predict a large share for theirs. The gap exposes who knows more. (a01, a03, a04)

Headline result: in the founding Nature paper, SP cut errors by 21.3% against majority vote over 490 mostly human items (a02, b01). The gain comes mostly from the state-capital items (48%). Trivia gave 14% (b03). It is one paper. No independent same-design replication was found (d19, K19).

What this means for our agent: SP is a selection rule (schema S7). It needs a second elicitation per question (a prediction of other samples). The evidence says it works for humans with diverse private knowledge and fails for samples drawn from one language model, because the samples share errors (K11, K20). The more useful relatives are weaker: predictions used as weights, and a learned inverse-SP score (K13, K22).

## 2. History and theories in depth

**Bayesian truth serum (BTS), Prelec 2004 (a23, snippet only).** BTS scores answers by the log-ratio of actual to predicted vote share. It was built to reward honest reporting in surveys with no ground truth. It is the base of SP. We did not read it. What we know comes from the 2017 paper.

**Prelec, Seung and McCoy 2017, Nature 541:532-535 (a01-a10, a25, a26, b01-b08).** The paper turns the BTS idea into a decision rule for single questions. It gives a theory (a07, a08, b08) and nine studies.

Theory in plain terms:
- Respondents share a common prior over the world.
- Each respondent gets a private signal. Signals are conditionally independent given the true state.
- Each answer has a signal type that makes its holder give that answer the highest probability.
- Respondents report honestly.
- Under these conditions, with an infinite sample, the answer with the highest "actual minus predicted" gap is the true state.
- Toy proof (a01): two worlds with coin biases. Yes is 60% in the real world and 90% in the counterfactual. The majority says Yes in both worlds, so majority cannot tell them apart. The predicted Yes share lies between 60% and 90%. The actual share converges to 60%, so No is surprisingly popular.
- The authors state limits (b08): if the evidence is misleading, the answer that fits it may be wrong. A BTS-like reward can be manipulated. The proof is for ideal Bayesians and infinite samples (a01, a07).

Empirical studies (b01-b06): capitals (1a, 1b, 1c), trivia (2), dermatology (3), art prices (4a, 4b). Details are in section 3.

**Behaviour of predictions (a03, a04, a05).** The prediction data support the mechanism. In the capitals studies voters for False predicted that 49% would say True. Voters for True predicted 73%. In the trivia study the two groups predicted 45% and 59%. The Spearman correlation between predicted vote share and the respondent's own implied belief was 0.48 (trivia, a04) and 0.87 (dermatologists, a05). Predictions are anchored on one's own view, but not fully.

**Follow-up work on rankings and weighting.**
- Hosseini, Mandal, Shah and Shi 2021 (a12, b14, c16, d17) extended SP to rankings. Votes and predictions each sit near random, but together they recover the ranking.
- Hosseini, Mandal and Puhan 2024 and 2025 (a13-a15, b15, b16) added partial preferences, a concentric rank-order model and a dataset (SP-Rank).
- Martinie, Wilkening and Howe 2020 (a20, b13) used meta-predictions to weight respondents (extremised meta-prediction weighting, MPW).
- Palley and Soll 2019 (a22, b25) and Wilkening et al. 2022 (a21) addressed the shared-information problem. Only abstracts seen.
- Shinitzky et al. 2022 (b24, c15) and Luo and Liu 2019 (b23, c13) learned aggregators from confidence and meta-prediction features.

**Field tests.**
- Lee, Danileiko and Vi 2018 (a16, b12): college football, 256 games. SP 68%.
- Rutchick et al. 2020 (a17-a19, a24, b09-b11): football, midterm elections, NBA. Mixed results, small differences.

**LLM turn, 2023-2026.**
- Goel et al. (b20, b21, c10, d12) used an SP-like likelihood ratio inside one model to rank candidate answers.
- Ai et al. 2025 (b18, b19, c07-c09, c22, d06-d09) proposed inverse surprising popularity (ISP) and optimal weighting (OW) for ensembles of different models.
- Consensus is Not Verification 2026 (c01-c06, c24, d01-d05) is the most direct test of plain SP on LLM sample crowds. It found no reliable gain.
- Liu 2026 (b22) tested BTS-style voting among LLM judges on code review.
- Mytsyk et al. 2026 (c11, c12) used honest group-frequency prediction as an RL reward against sycophancy.
- Han et al. 2025 (b17, d13) studied two-round voting, which contains SP as a special case.

**Competing explanations of why SP sometimes works.**
1. The expert-signal account (Prelec): the gap reveals who holds rare correct knowledge.
2. The predictions-as-weights account (Martinie, Wilkening): meta-predictions mark who is an expert. The signal is better used to weight people than to flip the winner (critique.md).
3. The failure-of-independence account (Ai, Kim): with correlated errors the gap measures shared bias, not truth (d08, d10).
4. The two-round-voting account (Han): SP is one instance of seeing the tally and revising (d13).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| SP cuts errors vs majority, pooled human studies | 21.3% fewer errors, 490 items, two-sided matched-pair sign test P<0.0005 | Prelec et al. 2017 (a02, b01) | single-source (K01) |
| Gain by study set | State capitals: 48% fewer errors (1a n=51 MBA, 1b n=32 Princeton, 1c n=33 MIT; 50 items each). Trivia: 14% (P=.031; 80 items; 39 MTurk workers) | b03, a03, a04 | single-source (K01) |
| SP vs other rules, 290 items (Studies 1c, 2, 3) | vs majority 35.8% (P<0.001); vs confidence-weighted vote 24.2% (P=0.0107); vs max-confidence 22.2% (P<0.13, not significant) | b02, a26 | single-source (K02) |
| Predictions near 50/50 limit SP | Trivia: predictions fell in the 40-60% band for 81% of items vs 22% in other studies (b04, confirmed in critique.md). a10 lists 56% for trivia on a different count; treat as a discrepancy. Other studies: art professionals 19%, MIT 29%, states 36% | a10, b04 | single-source (K04) |
| Art study | 90 artworks. For a $100,000 piece the average professional is right 30% of the time but a professional majority only 10%. SP lowers the needed share for "expensive" from 50% to about 25% | a06, b05 | single-source |
| Dermatology | 80 lesions, 25 dermatologists (mean 10.5 years). Prediction-belief Spearman 0.87. In the 490 pool | a05, b06 | single-source |
| Power is low | 50 items, n=30: SP beats majority at P<0.05 in only about 40% of simulated studies (392 of 1000). Biased-coin model: individuals 75% right, majority 86% | a09, b07 | single-source (K05) |
| Theory conditions | Shared prior, conditionally independent signals, honest reports | a07, a08, b08 | established as theory (K03) |
| Mechanism check | Voters for False predicted 49% True; voters for True 73% (capitals). Trivia 45% vs 59% | a03, a04 | established (K03) |
| Football, student crowd (Rutchick Study 1) | N=227, 216 games. Individual 52.8%, majority 53.9%, confidence-weighted 55.6%, SP 51.4%, fivethirtyeight 62.0%. 6 of 227 self-rated experts | b09, a17, a24 | contested (K06) |
| Football, objective experts | 46 people. Majority 59.0%, confidence 59.7%, SP 60.2% | b09 | contested |
| Midterm elections (Study 2) | Individual 60.8%, majority 79.1% (87/110), confidence 79.6%, SP 80.0%. Objective experts: majority 79.6%, SP 82.7% (91/110). Self-assessed experts: majority 77.3%, SP 71.8% | b10, a18 | contested (K06, K07) |
| NBA (Study 3) | 465 games, N=130. Individual 61.8%, majority 65.9% (306.5), confidence 65.5%, SP 67.3% (313), fivethirtyeight 68.2% (317) | b11, a19 | contested |
| Lee et al. football | 256 games, 100 MTurk, 94 media experts. SP 174 (68%), mode 172.5, confidence-weighted 166. Combining five methods 178 | a16, b12 | single-source (K08) |
| Meta-prediction weighting | 500 science true/false items, 459 analysed. Extremised MPW +6.64 points over simple average (95% CI 5.61-7.63), +4.21 over minimal pivoting, +14.22 over mean individual. About +9 on hardest level, none on easiest | a20, b13 | single-source (K09) |
| Rankings | 720 MTurk workers; countries (230), movies (15,743), paintings (80). Random top-of-4 error 0.75. Votes and predictions alone near random; the SP combination far better and beat Borda, Copeland, IRV | a12, b14, c16 | established (K10) |
| Partial-preference SP | 432 MTurk; 36 alternatives per domain; fitted share of experts under 20%. Partial-SP beat Aggregated-SP | a13, b15 | established (K10) |
| Learned aggregation with a wrong crowd | 2,490 responses, 22 problems, only 28% correct. Learned aggregator 64% (RCR-Agg), 55% (ACR-Agg). Beat SP, p<0.0014 and p<0.0265 | b24, c15 | established (K16) |
| Machine Truth Serum | High-disagreement splits: Spambase fixed 48 of 149 (+32.2%), Breast cancer 8 of 51 (+15.7%), Hill Valley 1 of 64 | b23, c13 | established (K16) |
| LLM sample crowds, plain SP | 5 models, 4 binary sets, 375,000 responses. Over 19 model-benchmark cells at T=1.0: SP vs majority 9 wins, 9 losses, 1 tie | c01, d01, d02 | contested (K11) |
| HLE (35 q) at T=1.0, single / majority / SP | Qwen3-235B 21.4/20.2/25.4; Qwen3-32B 28.2/25.1/22.8; GPT-oss-120B 11.7/8.7/8.4; GPT-oss-20B 10.1/11.7/11.2; Gemma-3-4B 27.3/28.7/28.7. One question is 2.9 points | c02, d01 | contested |
| BoolQ (100 q), majority vs SP | GPT-oss-20B 79.9 vs 80.0; GPT-oss-120B 80.0 vs 82.0; Qwen3-32B 77.0 vs 75.9; Qwen3-235B 69.9 vs 72.1; Gemma-3-4B 61.0 vs 60.1 | c03 | contested |
| Com2Sense (100 q), single / majority / SP | GPT-oss-20B 62.5/38.9/45.0; GPT-oss-120B 65.0/41.2/45.8; Qwen3-32B 51.7/28.3/32.8; Qwen3-235B 75.6/77.1/75.3. Majority and SP far below single sample for three models | c05 | contested |
| Predict-the-Future (100 q) | All methods 45-54%. GPT-oss-120B SP 50.4 vs majority 45.4; GPT-oss-20B 47.7 vs 49.3 | c04 | contested |
| Why LLM crowds fail | MATH: top wrong answer is 65-87% of wrong responses. Several models converge on the same wrong answer on 53% of questions where several err. Plurality flips in only 2.9% of 1,575 (question, model) pairs across temperature | c06, d04, d02 | established (K12, K20) |
| Error correlation across models | 349 HuggingFace models, 12,032 q: agreement when both wrong 0.423 vs about 0.12 by chance; 100% of pairs above chance. 71 HELM models, 14,042 q: 0.60 vs 1/3. Same provider adds +0.066 (HF) and +0.022 (HELM) | d10 | established (K20) |
| Popularity bias | 22 open LLMs (0.5B-32B): popular wrong answer chosen 66% of the time when all distractors are more popular than the right answer. PopDebias up to +54.1 points under strong pressure | b26, d14 | established (K12) |
| ISP vs MV vs SP, simulation | 4 agents, accuracy 0.6-0.9. K=2: MV 85.13, SP 79.94, ISP 90.48 (OPT 91.37). K=4: MV 92.64, SP 90.52, ISP 94.45 (OPT 94.94). K=10: MV 95.54, SP 94.40. SP below MV at every K from 2 to 10. (b18 reports 91.37 as the ISP figure; d06 separates ISP 90.48 from the optimal 91.37.) | b18, d06, c07 | single-source (K13, K21) |
| ISP on real LLM ensembles | Four strong models. UltraFeedback MV 72.21, ISP 73.26, OW 73.66. MMLU MV 89.32, ISP 90.01, OW 90.37 (best single 91.02). ARMMAN MV 85.24, ISP 85.78, OW 85.78. t = 12.53, 23.39, 3.22. Eight models: MV 70.23/87.19/84.40 vs ISP 71.18/87.92/84.79. ISP top in only 12.5% of 16 ensembles | b19, c08, c09, d07 | single-source (K13) |
| Hard items | MMLU-hard (13,886 q): MV 17.23 vs OW 24.79. Largest gain 7.7 points (OW-I 83.97 vs MV 76.27, ARMMAN, correlated set) | c09, d07, d08 | single-source (K22) |
| Likelihood ratio inside one model | TruthfulQA 817 q. MaxPost to MaxRatio: GPT-2 XL 0.36 to 0.52; LLaMA-2 7B 0.34 to 0.58 (+24); 13B 0.43 to 0.59; 70B (4-bit) 0.37 to 0.58 (+21). Better in 28 of 38 categories for 7B. Up to +70 on one category. COPA 70B 0.88 to 0.88 | b20, b21, c10, d12 | single-source (K14) |
| BTS voting among LLM judges | 871 code-review items, 4 judges: every variant about 1 point below majority (significant after correction). ECE down 21-32% | b22 | single-source (K15) |
| Confidence weighting in LLM crowds | HLE: Qwen3-32B majority 25.1 vs weighted 17.3; Qwen3-235B 20.2 vs 14.6. BoolQ GPT-oss-120B 80.0 to 84.0 | c24 | single-source (K18) |
| Prediction as RL reward | 64 samples per prompt. SmolLM3-3B, 1,000 synthetic items: flip rate under pressure 23% to 4%, accuracy under pressure 80% to 93% | c11, c12 | single-source (K17) |
| Two-round voting | 40 agents. DeepSeek R1 informed-majority rate 0.56 to 0.88 (accurate description), 0.52 to 0.78 (vague). GPT-4o 0.50 to 0.48 | b17, d13 | single-source (K27) |
| Model diversity | 113 Metaculus questions, 5 forecasters, budget of 5 samples. Best mix: 2 x FT-gpt-oss-120b, 1 each Gemini 3 Pro, GPT-5, Grok 4 (weights 0.56/0.26/0.18) | c18, d11 | single-source (K26) |
| Baseline for scale | Self-consistency over greedy CoT (2022 models): GSM8K +17.9, AQuA +12.2, SVAMP +11.0, StrategyQA +6.4, ARC-c +3.9 | d15 | established (context for K23) |

Notes on data quality (critique.md): the Ai et al. Table 3 labels for MMLU and ARMMAN were swapped in entry c08; the correct reading is MMLU 90.37 OW, 90.01 ISP, 89.32 MV and ARMMAN 85.78, 85.78, 85.24. The Goel paper text and table disagree (text says +24 on 70B; table gives +24 on 7B and +21 on 70B). The Rutchick NFL media figure is ambiguous. The HLE set has 35 questions, so confidence intervals are about +-14 points.

## 4. Mechanisms and models

### 4.1 Plain SP (what to implement)

Inputs per question: N samples. For each sample i, an answer a_i from a closed set of K options, and a predicted share vector q_i over the options (sums to 1).

```
actual[k]    = count(a_i == k) / N
predicted[k] = mean_i q_i[k]
gap[k]       = actual[k] - predicted[k]
choose argmax_k gap[k]
```

Notes for an engineer:
- With K=2 the rule flips the majority only when the majority's actual share is below its average predicted share.
- BTS-style variant: score by log(actual/predicted). Add a small constant to avoid log of zero.
- Missing predictions: the Consensus paper defaulted missing values to 0.5 (d03). That hides parse failures. Log them.
- Free-form answers need clustering to a normalised form first (K25). No SP study handles this.

### 4.2 Why it can work (the information model)

Each respondent has a signal. A person with the rare right signal reasons: "Most people lack this signal, so my answer will be rare, and the majority will be wrong." Their predicted share for their own answer is lower than a naive voter's. If the actual share of the true answer is higher than the average prediction, the true answer is surprisingly popular. This needs:
1. A population where some members hold information the majority lacks.
2. Predictions that carry that knowledge. The prediction-belief correlation was 0.48 to 0.87 in the human data (a04, a05). Predictions are not pure noise.
3. Predictions that are spread out. If 81% of predictions sit at 40-60% (trivia, b04), SP cannot separate answers and reduces to the majority rule.

### 4.3 Why it fails for same-model samples

Mechanism for LLM crowds (K11, K12, K20, K24):
- Samples share training data, bias to popular options and wrong answers. On MATH the top wrong answer is 65-87% of wrong responses (d04).
- When a model is asked "what share of language models will say yes", its answer tracks its own vote share (d03, K24). The prediction mirrors the vote. The gap then measures noise.
- A model predicts what other models say better than it detects truth (c01, K12). The signal SP uses is then consensus, not knowledge.
- Where the popular answer is wrong, models prefer it (66% in the hardest setting, b26). SP needs a minority holding the rare right answer. A same-model crowd rarely has one.
- Theory for correlated agents (d08): expected advantage ordering ISP >= MV >= SP. Plain SP is not better than majority in expectation when difficulty varies across questions.

### 4.4 Inverse SP and weights (Ai et al. 2025)

ISP uses second-order information (how often model j answers l when model i answers k) to compute a posterior for each option. For the engineer (d09, c22):
```
P_hat(A_i = s_k | A_j = s_l) = count(A_i=s_k, A_j=s_l) / count(A_j=s_l)
```
The counts come from the historical co-occurrence of answers across questions, not from asked-for predictions. Then:
- ISP picks the option with the best score under these conditional frequencies.
- OW (optimal weighting) learns a weight per model from the same data.
- It needs many questions to estimate co-occurrence.
- Gains over majority were 0.5-1.5 points on real ensembles, up to 7.7 on a correlated set and about 7.5 on MMLU-hard (c09, d08). It needs different models, not one model's samples.

### 4.5 Meta-prediction weighting (Martinie et al.)

Weight each respondent by how well their predictions match the group. Extremise the weights. Compute a weighted mean. +6.64 points on the simple average (b13). In an LLM scaffold the closest analogue is to weight samples by how well each predicts the other samples' answers. Not tested for LLMs.

### 4.6 Likelihood ratio inside one model (Goel et al.)

Score each candidate answer c by p(c | question) / p(c | generic prompt). It cancels the prior popularity of the string. This is the "surprisingly likely" idea inside one model. It needs token-level likelihoods and a fixed candidate list (3 to 25, mean 7.6). Gains on TruthfulQA were large on 2023-era base models (b20, c10). It is a correction for popularity bias, not an aggregation across samples. Not shown to carry over to reasoning models.

### 4.7 Ranking SP (Hosseini et al.)

Elicit a ranking (or top choice) plus a prediction of others' rankings. Combine with a model of voter behaviour (Mallows, Plackett-Luce, concentric mixtures). It recovers a ranking when each signal alone is near random (b14). It works with under 20% experts (b15).

### 4.8 Learned aggregation

Features: answer, confidence, prediction of others. A model maps these to a decision. It beats SP and majority when the crowd is mostly wrong (28% correct, 64% aggregate, b24). It needs labels to train.

### 4.9 Two-round voting

Round 1 vote. Show the tally. Round 2 vote. SP is a special case (d13). In LLM simulations the gain was model-dependent: R1 rose from 0.56 to 0.88, GPT-4o stayed flat. The second round is not independent, so it conflicts with guardrails G4 and G9.

## 5. What holds up

**Holds up.**
- The mechanism in human data. Predictions differ by answer and relate to own belief (a03-a05). [E]
- Rankings: votes plus predictions beat either alone (K10; one research group plus a dataset, so independence is partial).
- Learned aggregators help when most of the crowd is wrong (K16).
- LLM errors are strongly correlated (K20, two large studies).
- Popularity bias in LLMs (K12).
- Meta-predictions as weights give a measurable gain in a human crowd (K09, single study, 459 people).

**Does not hold up, or untested.**
- The 21.3% number. One paper, pooled sign test, driven by capitals (48%). Trivia was 14%. The authors' own power analysis says a single study reaches P<0.05 only about 40% of the time (a09). The independent field tests (Lee 2018, Rutchick 2020) are different designs and show small or negative differences (K06, K19).
- Rutchick et al.: SP was the worst rule for football (51.4% vs 53.9% majority, 55.6% confidence). For NBA SP was best (67.3% vs 65.9%) and elections about even (80.0% vs 79.1%). None of the differences was shown significant.
- Lee et al.: SP edged the mode by 1.5 games out of 256 (174 vs 172.5). Within noise.
- LLM sample crowds: SP vs majority 9 wins, 9 losses, 1 tie (d01). No reliable gain (K11).
- BTS votes among LLM judges: about 1 point worse than majority on 871 items (b22).
- Plain SP in simulation is below majority at every K from 2 to 10 (d06).

**Moderators.**
- Expertise. With few real experts the gain vanishes (football: 6 of 227 self-rated experts). Self-assessed experts did worse under SP (71.8%) than under majority (77.3%) in elections. Objective experts did better (82.7% vs 79.6%) (K07, a24, b10). Self-rating is not a safe expertise signal.
- Spread of predictions. Narrow predictions (40-60%) cut the gain (K04).
- Item difficulty. Weighted rules gain most on hard items (about +9 for MPW, +7.5 for OW on MMLU-hard) and nothing on easy items (K09, K22).
- Diversity of wrong answers. Indirect evidence only. No study built items with a shared misconception (critique gap 3).
- Number of options. The ISP edge shrinks about as 1/K. Plain SP stays below majority up to K=10 (d06).
- Sample and item count. Use hundreds of items.
- Model diversity. Mixing three families did not restore independence for SP (d05). Same provider adds only +0.02 to +0.07 agreement, so model name is a weak diversity proxy (d10). Mixed forecasters helped weighted forecasting (d11).

**Interventions that worked.**
- Asking for a ranking plus a prediction in ranking tasks (b14).
- Learned aggregators on hard crowds (b24, b23), but Hill Valley fixed only 1 of 64.
- Likelihood-ratio rescoring inside a model (b20).
- Honest prediction as an RL reward cut the sycophancy flip rate from 23% to 4% (c11).
- Model mixing for forecasting (d11).

**Interventions that did not work.**
- Plain SP on same-model sample crowds (c01).
- Verbalised confidence weighting on hard LLM items (HLE, c24). Verbal confidence tracks consensus almost as much as correctness (d05).
- Model-name diversity alone (d05, d10).

**Weak spots in the evidence base (critique.md).** Almost every positive human number traces to one paper. LLM studies are few, mostly 2026 workshop or preprint level, with small item sets (HLE 35, BoolQ 100, Com2Sense 100). The Ai et al. gains are 0.5-1.5 points. No study tested SP with a frontier reasoning model at equal token cost.

## 6. Language models

**Direct tests of SP on LLM sample crowds.**
- Consensus is Not Verification (c01-c06, d01-d05): five models (Gemma-3-4B, GPT-oss-20B and 120B, Qwen3-32B and 235B), 50 samples per question and model, temperatures 0.7 and 1.0, 375,000 responses. The prediction prompt asked "what percentage of language models will answer YES". No consistent gain. HLE: SP above majority for Qwen3-235B (25.4 vs 20.2) and below for Qwen3-32B (22.8 vs 25.1). BoolQ: SP within about +-2 points of majority for every model. Com2Sense: majority and SP both far below single sample for three models (GPT-oss-20B 62.5 single, 38.9 majority, 45.0 SP). A control with 10,000 random-string prompts is in the paper. Limits: 35 to 100 questions per set, binary only, reasoning mode not stated, a pooled crowd of 125 votes per question (d05).
- Liu 2026 (b22): BTS-style variants among four LLM judges were about 1 point below majority on 871 code-review items. Calibration (ECE) improved by 21-32%.

**Why LLM crowds break SP (K20, K12, K24).** Errors are correlated across 349 and 71 model pools. Models favour popular options. Verbal predictions mirror the vote.

**Methods that work somewhat better.**
- ISP/OW (Ai et al.): +0.5 to +1.5 points on real ensembles of different models (GPT-4o/3.5, Qwen2.5, Llama 3.x, Phi-4). Big gains only on hard items and on a correlated set. The best single model (91.02 on MMLU) beat ISP (90.01). Second-order data came from co-occurrence, not asked-for predictions. Not tested against self-consistency at equal tokens (K22, K23).
- Likelihood ratio (Goel): up to +24 points on TruthfulQA with 2023 base models. Larger models gained more. COPA 70B did not move (0.88 to 0.88). StoryCloze 70B rose 0.77 to 0.85.
- Prediction as reward (Mytsyk): training only. 3B model, synthetic data.
- Two-round voting (Han): R1 0.56 to 0.88, GPT-4o flat. Model-dependent.
- Model diversity (Aitchison et al.): mixing four models beat a same-model sample for forecasts.
- Self-consistency (Wang 2022, d15): +3.9 to +17.9 points over greedy CoT on 2022 models. This is the scale against which an SP gain of about one point should be judged.

**Not done yet.** No published test of SP or ISP with a current reasoning model against self-consistency at equal token cost (K23). No study checks whether verbalised predictions carry information beyond the sample's own vote (K24). No study built items with a known shared misconception. No persona arm. No open-ended answers (K25).

**Related but different.** Trott 2024 (c17): GPT-4 ratings correlate 0.75-0.80 with gold on some norm tasks, so a small LLM crowd can match human norms. Schoenegger 2024 (c19, d16): LLM forecasters were competitive with human crowds, and exposure to the human median improved GPT-4 and Claude 2 by 17-28%. Amiri-Margavi 2025 (c25, d18): agreement of two or three models predicts reliability (Claude 100% when two or three agree, LLaMA 92%). These are consensus signals, not SP.

## 7. What our agent should take

Legend: part = schema part (G guardrail, S state, O operator, memory = S9 record). Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| N1 | Keep G4 and add one line: plain SP is not a selector for samples from one model. Samples share wrong answers, and a model's predicted share mirrors its own vote. Add it to section 4b "not to add". | G4, 4b | [E] | K12, K20; c06, d04, d10, b26 |
| N2 | Cluster answers into a normalised form in code before any count or vote. | S7 | [E] by current practice; no SP study handles it (K25 is [S]) | d06, d12 |
| N3 | Log, per item, the share of the top wrong answer and pairwise wrong-answer agreement among the scaffold's own attempts. Keep a class-level record in S9. This is the number that tells us whether any second-order trick can help. | S9 memory, G4 | [E] that error correlation is the key variable (K20) | d10, d04 |
| N4 | A vote never overrules a check. If a minority answer passes the unfitted check and the majority fails, the check wins. | G3, S7 | [E] | G3; K12 |

### Test first (not added until a test passes)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Equal-token SP vs majority (self-consistency) with the scaffold's own samples and a current model. | S7 | [C] | K11, K23 |
| T2 | Prediction residual as a score: does a sample whose predicted share is below its actual share more often hold the right answer? | S7 | [S] | K03, K24 |
| T3 | Weight samples by how well they predict the others (extremised MPW). | S7 | [S] | K09, K22 |
| T4 | ISP/OW from answer co-occurrence on the bench's own history, as a weighted vote. Needs several models or prompt families. | S7, S9 | [S] | K13, K22 |
| T5 | SP only on items with high disagreement and low plain pass rate (hard items). | S0 gate, G12 | [S] | K09, K16, K22 |
| T6 | Likelihood-ratio rescoring of a closed candidate list (needs logprobs). | S7 | [S] | K14 |
| T7 | SP-style score as a calibration or abstention signal, not as a selector. | G1, S6 | [S] | K15 |
| T8 | Model or prompt-family diversity as the source of independent signals. | G4, S3 | [S] | K26 |
| T9 | A second pass that sees the tally. Likely conflicts with G4 and G9; run only as a counter-test. | S7 | [S] | K27 |
| T10 | For multi-option or ranking outputs, top-k plus predicted top-k vs Borda. | S7 | [E] in humans (K10), untested in LLMs | K10 |

## 8. Concrete tests on our bench

All arms get the same total token budget per item (G7). Count the prediction call in the tokens. Report setup cost. Use at least 300 items per cell (K05). Use a paired test (sign test or McNemar) on per-item correctness.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Closed-set questions with exact answers (BoolQ-type, multiple choice, short-answer maths) from the HTSA benchmarks | (a) N samples + majority; (b) N/2 samples + N/2 prediction calls + SP; (c) single sample; (d) confidence-weighted vote | Accuracy, paired difference with 95% CI | SP at or below majority; gain under 1 point |
| T2 | Same items; per-sample log of (answer, predicted share) | Single arm, offline analysis | AUC of the prediction residual for correctness, beyond own-vote share | Near 0.5 (K24 expects mirroring) |
| T3 | Same items | Majority vs extremised MPW vs plain SP | Accuracy; split by difficulty tertile | Gain on the hard tertile only, up to a few points |
| T4 | Items answered by 3+ models or prompt families | Majority vs ISP vs OW from co-occurrence (train/test split of items) | Accuracy; hard-item accuracy | +0.5 to +1.5 overall, more on hard items |
| T5 | Items with plain pass rate under 40% and disagreeing attempts | Majority vs SP vs verifier (check) | Accuracy on these items | Verifier wins; SP no better than majority |
| T6 | TruthfulQA-style multiple choice with logprobs | Raw likelihood vs likelihood ratio vs CoT majority | Accuracy | Gain on base models; small or none on reasoning models |
| T7 | Items with known answers | Stated confidence vs SP score vs agreement share | ECE, AUROC for correctness, abstain-and-cover curve | SP score improves ECE (Liu: -21 to -32%) but not accuracy |
| T8 | Same as T4 | One model with N samples vs mixed models or personas at the same N | Wrong-answer agreement; accuracy of majority and SP | Mixed lowers agreement a little; SP still not above majority |
| T9 | Same as T1 | Independent votes vs a second pass with the tally | Accuracy; rate of wrong flips to the majority | Model-dependent; sycophancy risk |
| T10 | Ranking items (order items by a measurable quantity) | Borda vs SP-rank | Kendall tau distance | Gain, as in humans, if predictions are informative |
| Misconception probe | Items where the common answer is wrong | Majority vs SP vs verifier | Accuracy; share of items where the top answer is the misconception | Majority and SP both fail; verifier wins |

## 9. What does not transfer, and why

- **Independence.** Humans bring different private information. Samples from one model do not. Wrong-answer agreement is 0.42 to 0.60 across model pools against 0.12 to 0.33 by chance (d10). Model-name diversity adds little.
- **The prediction signal.** A person predicts the crowd from their own view plus knowledge of how others differ. A model's "what share of models will say yes" mirrors its own vote (d03, K24).
- **Honest reporting.** BTS-style scoring pays for honesty. A model sample gets no payment. At inference time the prediction is just another generated number.
- **Incentive compatibility.** The human theory needs a scoring rule people respond to. Using it needs training (Mytsyk uses RL, c11).
- **The 21.3% figure.** One paper, mostly capitals plus a trivia set. It should not be a prior for LLM gains.
- **Crowd size.** The human studies used 30 to 100 respondents per item. Our budget allows 3 to 8 samples per item. Shares from 4 votes are coarse and the gap is noisy.
- **Closed answer sets.** Studies used true/false, 4 options or rankings. Open-ended problems need clustering first (K25).
- **Reasoning models.** The LLM SP studies used non-reasoning models or did not state the mode. A reasoning trace may carry its own check, but G10 says treat the text as non-evidence.
- **Second rounds.** G9 bars debate. Two-round voting is related and carries sycophancy risk.

## 10. Open questions

1. At equal tokens, does SP beat self-consistency with a current reasoning model? No study (K23).
2. At what error correlation does SP start to help? No cutoff exists (critique gap 2).
3. Does the predicted share of a sample carry signal beyond its own vote? Not measured (K24).
4. What is the independent replication status of the 21.3%? The search was incomplete (K19).
5. Do persona or prompt-family differences restore enough independence? Untested (K26).
6. How should SP/ISP work for open-ended answers? Unsolved (K25).
7. Can SP-style scores work as an abstention or calibration signal on accuracy-neutral tasks? One study (K15).
8. Are the Consensus-is-Not-Verification results stable on larger item sets and in reasoning mode? (critique gap 10)
9. Does ISP from co-occurrence beat majority when the "models" are one model under different prompts?
10. Can learned aggregators (K16) be trained on the scaffold's own S9 history cheaply enough to pay under G7?

## 11. Sources

[V] = opened and read this run. [M] = snippet or listing only.

**Founding**
- [V] Prelec, Seung, McCoy 2017, Nature 541:532-535. https://gwern.net/doc/statistics/prediction/2017-prelec.pdf
- [M] Same paper, Nature page (second-hand figures). https://www.nature.com/articles/nature21054
- [M] Prelec 2004, A Bayesian truth serum for subjective data, Science 306:462-466. https://doi.org/10.1126/science.1102081
- [V] Wikipedia, Surprisingly popular. https://en.wikipedia.org/wiki/Surprisingly_popular
- [M] Princeton news 2017 (search note d19). https://www.princeton.edu/news/2017/02/06/crowd-wisdom-surprisingly-popular-answer

**Human field tests and extensions**
- [V] Lee, Danileiko, Vi 2018, Judgment and Decision Making. https://doi.org/10.1017/S1930297500009207
- [V] Rutchick, Ross, Calvillo, Mesick 2020, Cognitive Research. https://doi.org/10.1186/s41235-020-00256-z ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7658271
- [V] Martinie, Wilkening, Howe 2020, PLOS ONE. https://doi.org/10.1371/journal.pone.0232058
- [M] Wilkening, Martinie, Howe 2022, Management Science 68(1). https://doi.org/10.1287/mnsc.2020.3919
- [M] Palley, Soll 2019, Management Science. https://doi.org/10.1287/mnsc.2018.3047
- [V] Hosseini, Mandal, Shah, Shi 2021, SP voting recovers rankings. https://arxiv.org/abs/2105.09386 ; https://faculty.ist.psu.edu/hadi/papers/spvoting.pdf
- [V] Hosseini, Mandal, Puhan 2024, partial preferences. https://arxiv.org/abs/2406.00870
- [V] Hosseini, Mandal, Puhan 2024, concentric rank-order model. https://arxiv.org/abs/2411.08367
- [V] Hosseini, Mandal, Puhan 2025, SP-Rank dataset. https://arxiv.org/abs/2601.05253
- [V] Shinitzky et al. 2022, meta-cognitive features for one-shot group decisions. https://arxiv.org/abs/2201.08247
- [V] Luo, Liu 2019, Machine Truth Serum. https://arxiv.org/abs/1909.13004 ; [M] journal version https://link.springer.com/article/10.1007/s10994-022-06183-y
- [V] Han, Schoenebeck, Tao, Xia 2025, The art of two-round voting. https://arxiv.org/abs/2505.10377

**Language models**
- [V] Consensus is Not Verification 2026. https://arxiv.org/html/2603.06612v1
- [V] Ai, Pan, Simchi-Levi, Tambe, Xu 2025, Beyond majority voting. https://arxiv.org/abs/2510.01499 ; https://arxiv.org/html/2510.01499
- [V] Goel et al. 2023 (v2 2025), truthfulness of surprisingly likely responses. https://arxiv.org/abs/2311.07692
- [V] Liu 2026, Bayesian truth serum for LLMs? ICML 2026 workshop. https://icml.cc/virtual/2026/74483
- [V] Mytsyk, Zhang, Krishnamurthy 2026, sycophancy and RL. https://arxiv.org/html/2608.25267v1
- [V] Large Language Models Systematically Favor Popular Options 2026. https://arxiv.org/abs/2608.29257
- [V] Kim, Garg, Peng, Garg 2025, Correlated errors in LLMs, ICML. https://arxiv.org/html/2506.07962
- [V] Aitchison, Jeen, Shevlane, Day 2026, Diversity is the strength of the AI crowd. https://www.alphaxiv.org/abs/2606.29661
- [V] Wang et al. 2022, Self-consistency. https://arxiv.org/abs/2203.11171
- [V] Trott 2024, LLMs and the wisdom of small crowds. https://pmc.ncbi.nlm.nih.gov/articles/PMC11142632/
- [V] Schoenegger et al. 2024, Wisdom of the silicon crowd (opened in d16; listing only in c19). https://arxiv.org/abs/2402.19379
- [V] Amiri-Margavi et al. 2025, inter-model consensus. https://arxiv.org/abs/2411.16797
- [M] Generative Self-Aggregation (listing only). https://www.researchgate.net/publication/389648493_LLMs_Can_Generate_a_Better_An
- [V] arXiv listing for "surprisingly popular", 2026-11-01. https://arxiv.org/search/?query=%22surprisingly+popular%22
