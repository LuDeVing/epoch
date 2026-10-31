# Scoring rules and calibration: deep document

*Subfield E03.01. Built from evidence_a-d.jsonl (a01-a26, b01-b27, c01-c34, d01-d26), claims.jsonl (K01-K33) and critique.md in this folder. Claim ids are written K01 etc. for E03.01-K01. Status tags: [E] established, [S] single-source, [C] contested.*

*Read this first: the founding texts (Brier 1950, Murphy 1973, Ferro and Fricker 2012) were never opened. Every fact about them comes from later sources that agree (Gneiting and Raftery, Siegert, Dimitriadis et al., Foresight Arena). Most LLM forecasting studies are small or use 2023-2025 models. Preprints dated Jul-Oct 2026 have had little peer review.*

## 1. What it is

A scoring rule turns a probability forecast and the real outcome into one number. A calibration measure asks a second question: when the agent says 70%, is it right about 70% of the time?

The subfield covers four things.

1. **The Brier score.** For a binary event with forecast f and outcome o (0 or 1), the score is (f - o)^2. Lower is better. Always saying 50% scores 0.25. For m classes it is the sum of squared gaps over classes (a01, second-hand).
2. **The Murphy split.** The mean Brier score divides into reliability (calibration error), resolution (how much the hit rate changes between forecast values) and uncertainty (base rate times 1 minus base rate). Brier = REL - RES + UNC (a06, b01, c34).
3. **Calibration measures.** ECE (expected calibration error), reliability diagrams, AUROC (does stated confidence rank right above wrong), and repair methods (temperature scaling, Platt scaling, isotonic regression).
4. **Behaviour of language models** on these measures, from multiple-choice QA to live forecasting tournaments.

Why it matters to our agent. The schema state S9 LOOK BACK records, per problem class, a plain pass rate and an agreement record. A Brier-based record would turn that into a graded forecast log: before checking, the agent states a pass probability; after the check, code scores it. That tells the agent which classes it is calibrated on, and tells us whether any scaffold element improves the honesty of confidence and not only accuracy. It also feeds G5 (code does the arithmetic) and G7 (every element must pay for itself at equal tokens).

Our use differs from the literature in one way that matters throughout. Most studies here forecast real-world events that resolve in weeks. Our agent mostly solves problems with exact answers that resolve in seconds against code checks. The maths transfers. Many of the empirical LLM numbers do not (section 9).

## 2. History and theories in depth

**Brier (1950).** Glenn Brier proposed squared error for probability forecasts of weather so forecasters could be verified on a single number. Not opened (HTTP 403); the definition comes from Gneiting and Raftery and Wikipedia (a01, a02, a05). Worked example (a05): a forecast of 0.70 for rain scores 0.09 if it rains and 0.49 if it does not; a forecast of 0.30 and rain scores 0.49.

**Murphy (1973).** Allan Murphy split the mean score into REL - RES + UNC. UNC = obar(1 - obar), where obar is the base rate. The split is exact only when forecasts take a finite set of values and are grouped by value (a06, K03). Foresight Arena states the condition as: exact only when each bin's forecasts equal the bin mean (d19). Yang et al. 2026 use Stephenson's exact binned version, which carries extra terms (d26). Not opened.

**Proper scoring rules (Savage; Gneiting and Raftery 2007).** A rule is proper if the forecaster's best expected score comes from reporting true belief, and strictly proper if that report is the only best one. The Brier, log, spherical and pseudospherical scores are strictly proper. The zero-one (accuracy) score is not (a02, a04, b05, K01). Each proper rule has an entropy G(p) and a Bregman divergence loss; for Brier the divergence is squared Euclidean distance, for log it is KL divergence (a04).

**Skill scores.** The Brier skill score, 1 - BS/BS_ref, is not strictly proper. Murphy (1973) showed it is only asymptotically proper: hedging gains shrink as independent forecasts grow (a03, K02, [S]). Practical rule: log raw Brier, compute skill only as a derived view.

**Generalised decomposition.** Brocker (2009) extends the split to any strictly proper score for finite-valued forecasts: expected score = uncertainty - resolution + reliability (a07).

**Estimator trouble.** Ferro and Fricker (2012) showed the standard binned estimators are biased: reliability tends to be overestimated, uncertainty underestimated, resolution either way (b03, second-hand). Their correction reduces the bias but never removes it. Siegert (2013) derived sampling variances and showed the corrected versions have larger variance (b01, b02, c34). Dimitriadis, Gneiting and Jordan (2021) proposed CORP: isotonic regression (pool-adjacent-violators) gives a bin-free reliability diagram and a split into MCB (miscalibration), DSC (discrimination) and UNC. In their simulations CORP had the lowest mean squared error at every sample size tested (a08, a09). Their Table 2 example, n = 86 forecast values, S/MCB/DSC/UNC: ENS .266/.066/.044/.244; EPC .234/.022/.032/.244; EMOS .232/.018/.030/.244; Logistic .206/.017/.056/.244.

**Critiques of Brier.** Jewson (2004) shows Brier can prefer a catastrophic forecast: always forecasting 0 beats always forecasting 0.25 by 1/80 (1/16 - 1/20) when the event has frequency 0.1, although the first is wrong with certainty whenever the event happens (b04; the critique re-checked the arithmetic). Hoessly (2025) lists five misconceptions, among them: Brier 0 implies extreme forecasts; lower Brier is comparable across populations (it is only comparable on the same population); a low Brier means good calibration (it does not); a score near base rate times (1 - base rate) means the forecast is useless (not necessarily) (b06).

**Calibration in machine learning.** Guo et al. (2017) showed modern deep networks are overconfident, more so with depth and width, and that one-parameter temperature scaling fitted on a validation set fixes most of it without changing accuracy (a10, b07, b08, c30). They defined ECE with 15 bins.

**Calibration in language models.**
- Kadavath et al. (2022): pretrained models up to 52B are well calibrated on lettered multiple choice and true/false; calibration improves with size and few-shot; RLHF policies look miscalibrated but one fixed temperature (T = 2.5) largely repairs it (a11, a12, b09, b10, c26).
- OpenAI GPT-4 report (2023): MMLU ECE 0.007 pretrained vs 0.074 after post-training (c25).
- Tian et al. (2023): for RLHF chat models, stated probabilities beat token probabilities (a14, a15, b11).
- Xiong et al. (2024): stated confidence is overconfident, AUROC weak, sampling agreement helps (a16, b13, c28).
- Kapoor et al. (2024): prompting alone is not enough; about 1,000 graded examples for a learned estimator (a17, d18).

**From calibration to forecasting.** Autocast (Zou et al. 2022) gave the first dataset of tournament questions: the best retrieval T5 reached 65% binary accuracy vs 92% for the crowd; FiD Static calibration error 40% vs crowd 8% (a24, c29). Halawi et al. (2024) built the first system near the crowd. ForecastBench (Karger et al. 2025) set up a live benchmark with unresolved questions to prevent leakage.

**Brier as a training reward.** Turtel et al. 2025, Damani et al. 2026, Leng et al. 2025 and Turtel et al. 2026 use Brier or other proper rules as RL or reward-model signals (c21-c24, d14). Damani prove any bounded proper rule gives an accurate and calibrated optimum (c22). Our agent does not train, so this is proof that calibration is learnable from a graded record, not a method we can use (K20).

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Brier is strictly proper; accuracy is not | Table 1 of G&R: Brier S(p,1) = -(1-p)^2, S(p,0) = -p^2 | a02, a04, b05, b06 (Gneiting and Raftery 2007; Hoessly 2025) | E (K01) |
| Brier skill score is not strictly proper | gain from hedging vanishes asymptotically | a03 | S (K02) |
| Brier = REL - RES + UNC; UNC = base rate x (1 - base rate) | A useful forecast has Brier below UNC; exact only for finite-valued forecasts | a06, a07, b01, c34, d19 | E (K03); founding paper second-hand |
| Binned estimates depend on bin count and are biased | CORP lowest MSE in simulation; corrected estimators have larger variance | a08, a09, b02, b03 | E (K04) |
| Brier can prefer a certain-and-wrong forecast | f=0 beats f=0.25 by 1/80 at event frequency 0.1 | b04 (Jewson 2004), b06 | C (K05) |
| Temperature scaling repairs deep nets | ECE CIFAR-100 ResNet-110 16.53% to 1.26%; CIFAR-10 ResNet-110 4.6% to 0.83%; ImageNet ResNet-152 5.48% to 1.86%; fails on LeNet5 CIFAR-100 4.85% to 6.48% and Reuters DAN-3 0.85% to 0.91% | a10, b07, b08, c30 (Guo et al. 2017) | E (K07) |
| RLHF breaks LLM token calibration; one temperature fixes most | GPT-4 MMLU ECE 0.007 pretrained vs 0.074 after; Kadavath T = 2.5 | c25, a12, b10 | E (K06) |
| Verbalized confidence beats token probability for chat models by ECE | gpt-3.5 TriviaQA .140 vs .068 (top-1), .050 (top-2), .054 (top-4); SciQ .256 vs .065 (top-4); TruthfulQA .451 vs .203 (top-4). GPT-4 TriviaQA .078 vs .024 (top-1), .041 (top-4); SciQ .219 vs .056 (top-4); TruthfulQA .445 vs .198 (top-4) | a14, a15, b11, c27 (Tian et al. 2023) | C (K08) |
| Verbalized confidence overconfident in other tests | Average ECE above .377 for GPT-3, GPT-3.5, Vicuna; mostly 80-100% in multiples of 5 | a16, b13, c28 (Xiong et al. 2024) | C (K08) |
| Tian vs Xiong conflict is mostly prompt choice | Tian-style top-1 prompt better calibrated, especially for large models; models of at least 70B have ECE about .10; combo prompt GPT-4o .10 to .02, Llama 3 8B .26 to .21 | d22 (Yang et al. 2026) | S |
| ECE can be gamed by constants | GPT-4 GSM8K accuracy 93.6%, ECE .064 by saying 100% | a13, a16 | E (K09) |
| Verbalized confidence discriminates weakly | GPT-4 average AUROC 62.7% over 8 tasks (chance 50%); GPT-3 to GPT-4 +22.2%; white-box .605 vs black-box .522 | a16, c28 | E (K10) |
| Sampling agreement raises AUROC on some tasks | GSM8K AUROC 54.8% to 92.7% (5 samples with consistency) | a16 | E (K10) |
| Chain-of-thought before confidence does not help | gpt-3.5 TriviaQA 2-stage top-1 .131 (also quoted .110) vs 1-stage .068 | a14, c27 | E (K25) |
| Stated confidence nearly unchanged by reasoning (8B forecaster) | Spearman .90 forced vs free on 296 test questions (.87, .78 on later sets); same answer 67%; free reasoning +1.9 points accuracy | d20 (Sarfati et al. 2026) | E for models tested (K25) |
| Plain LLMs forecast near the coin-flip line | Halawi: GPT-4-1106 .208/.209, Llama-2-13B .226/.268, Claude-2.1 .220/.215, Gemini-Pro .243/.230, Mistral-8x7B .238/.238, ensemble .208/.224; S&P: GPT-4 .20 (SD .18) vs .25, t(22) = -1.23, p = .23, N = 23 | a18, a21, c01, c11 | E (K11) |
| Retrieval+reasoning system moves .03 closer to crowd | Halawi system .179 vs crowd .149 (accuracy 71.5% vs 77.0%), N = 914 test questions; Phan ReAct ensemble .169 vs humans .172 (accuracy 73.9% vs 73.8%) | a18, b14, c02, c19 | E (K12) |
| Retrieval mattered more than fine-tuning | Full .179; no fine-tune .186; neither .206; GPT-3.5 swap .182 | a20, b15, c03 | S (K13) |
| System wins where crowd unsure, loses where crowd sure | Crowd .3-.7: .199 vs .246. Crowd within .05 of 0 or 1: accuracy 7% higher, Brier .04 worse | a19, b16, c04, d15 | C (K14); cause is a hypothesis |
| Averaging model with crowd beats either | S&P blend .13 (SD .09) vs LLM .20 vs crowd .07 (N = 23); GPT-4 updated .14 vs average .13; Claude 2 .15 vs .14 | a21, b18, c16 | E (K15) |
| Ensemble of 12 LLMs matched 925 humans on 31 questions | LLM .20 (SD .12) vs .25: t(30) = -2.35, p = .026; vs human .19 (SD .19): t(60) = 0.19, p = .850; equivalence within .081 | a22, b17, c13, c14 | C (K16) |
| LLM mean forecasts above 50% (acquiescence) | mean 57.35 (SD 20.93), t(1006) = 86.20, 1,007 forecasts; outcomes 14 of 31 yes | c15 | C (K14) |
| Superforecasters beat top LLMs on ForecastBench (2025 paper) | 200-question subset: super .096, public .121, Claude 3.5 Sonnet .122, best without crowd values .136. With combination questions: .076, .096, GPT-4o .130 (gap .054 vs GPT-4o-to-GPT-4 gap .026) | b19, b20, c07, c08 (a23 mixed the two sets; corrected) | S (K17) |
| The gap shrank in 2025-26 but models see prices | Oct 2025: super .081, GPT-4.5 .101, GPT-4 .131; Mar 2026: .086 vs .103 (gap .017). Good Judgment: market-question Brier Index 80.3 vs 75.8 | d07, d08, d09 | C (K27) |
| Parity extrapolation is weak | Arena 1406 (CI 1346-1633); 6.49e26 FLOP (CI 9.69e25-8.65e28); R2 .47 and .41, p = .046, about 10 models. FRI later moved parity to Mar 2027 (Brier) / May 2027 (Index) | b21, c09, d07, d08 | S (K18) |
| Consistency violations predict later Brier, but not all checks | Conditional .92/.87 scraped, .71/.69 NewsAPI; negation +.60/+.67 scraped but -.36/-.13 NewsAPI; aggregate .62/.85 scraped, .49/.66 NewsAPI | a25, b22, c31 (Paleka et al.) | S (K19) |
| Brier-style RL reward calibrates verbalized confidence | Damani: HotpotQA ECE .37 to .03, math .26 to .10; accuracy 61.7% vs 63.0%. Turtel: 14B Brier .190 [.178,.203], ECE .062, market still .039 better. Leng: ECE cut over 50% in DPO | c21-c24 | E (K20), needs training |
| More reasoning does not help | Sonnet 4 .1560 vs thinking .1597, p = .53; KalshiBench Opus 4.5 Brier .227 vs GPT-5.2-XHigh .433 (26x tokens); reasoning models above 85% on wrong answers | b23, b25, d11 | E (K21) |
| Scaffold gain came via reliability, not resolution | Decomposition: calibration .026 to .008, refinement .091 to .083, Brier .141 to .132, n = 500 | d01 (Bosse et al. 2026) | S (K26) |
| Likelihood-aggregation scaffold at matched tokens | Monolithic 5,733 tokens Brier .2689 ECE .1840; two-sample 11,753 tokens .2497 / .1471; LEAP 11,508 tokens .2057 / .0876 | d03 (Chen et al. 2026) | S (K26) |
| Odds-multiplier scaffold | Kalshi, GPT-5.4: Think&Search .1028, market-implied .1060, AuditForecast .0870; 831 questions | d04 (Cao et al. 2026) | S |
| Platt scaling helps only when raw calibration is poor | Raw K-sample mean REL .0357 to .0004, Brier .228 to .185 (30% fit, 70% test); Halawi no gain; per-model Platt matched best single model in 7 of 16 groups, best pooled pair in 2 of 16 | d16, d15, d17 | C (K32) |
| Many items are needed | 80% power: edge .005 needs 5,567; .010 1,392; .020 348; .030 155; .050 56; .100 14 (n about 0.139 / delta^2); learned estimator about 1,000 items (benefit falls after about 5,000); 21-case pilot AUC .756 [.471,.980] | d19, d18, d24 | S (K31), E for the 1,000 (K22) |
| Without the price, frontier chat is near coin flip on hard markets | Opus 4.5 soft-Brier .256 on n = 265 (uncertain n = 104: .281 vs crowd .232); KalshiBench best BSS +.057; price visible worth .04-.075 Brier; agents correlate r .97-.99 with market | d10-d13 | E (K28) |
| Brier and log score rank alike; ECE can rank oppositely | Log reward .1653 vs Brier reward .1648 on 965 items (seed spread .0032); Gemini best top-pick ECE .068 but worst Brier | d14, d13 | S (K29) |
| Effort ratings beat confidence for failure prediction | AUROC +10.1 and +8.4 points, 12 LLMs, 38 tasks | d23 | S (K30) |
| Retrieval stream can wreck calibration | Five injected articles flip 69-73% of forecasts across 0.5; Brier .18 to .37; ten flip 89% | d25 | S (K33) |
| Backtests leak | Date-restricted search returns hindsight pages; effective N 178.8 | c32, b24 | E (K23) |
| Long explanations inflate user trust | Model AUC .75-.78 vs participants .54-.60; user ECE .104-.291 | a26 | S (K24) |

## 4. Mechanisms and models

Written so an engineer can build each piece.

### 4.1 Brier score and its split

For each resolved item i with stated probability f_i and outcome o_i (0 or 1):

    BS  = mean((f_i - o_i)^2)
    obar = mean(o_i)
    UNC = obar * (1 - obar)

Group items by forecast value (or bin). For group k with n_k items, mean forecast f_k and hit rate o_k:

    REL = sum_k n_k * (f_k - o_k)^2 / N
    RES = sum_k n_k * (o_k - obar)^2 / N
    BS  = REL - RES + UNC     (exact only when every forecast in a group equals f_k)

Read it as: REL is the cost of misreporting your hit rates. RES is the credit for separating easy cases from hard ones. UNC is the floor you get for free by always stating the base rate. A forecast is useful only if RES exceeds REL. Skill against the base rate: BSS = 1 - BS/UNC (derived view only; not proper).

Which levers move which term:
- Recalibration (temperature, Platt, isotonic) lowers REL and in principle leaves discrimination alone. Guo says temperature scaling does not change accuracy (a10).
- Better evidence or better reasoning raises RES. Only a better method does this.
- The scaffold wins in this folder show up mainly as lower REL: d01 calibration .026 to .008 with refinement .091 to .083.

### 4.2 Proper scores in code

- Brier: (f - o)^2. Bounded in [0,1]. Honest reports are optimal.
- Log score: -log(probability given to the actual outcome). Unbounded, so one certain wrong forecast gives infinite loss. Damani chose Brier because the log score is unbounded; Jewson argues Brier is too mild on certain-and-wrong forecasts. A design choice.
- On a real 965-item record the two ranked forecasters the same within noise (d14).
- Recommendation (K29): log both; treat Brier differences under about .005 as ties.
- Multi-outcome Brier (sum over outcomes) is on a different scale from binary Brier. Forecast-Dojo, World Cup 1X2 and FutureX values must not be compared with the .25 line.

### 4.3 Calibration estimates

Binned ECE: split items into B bins by stated probability; ECE = sum_b (n_b/N) * |mean_conf_b - accuracy_b|. Bin count matters. Kadavath used 10 equal-count bins, Guo 15, Autocast adaptive with 50 per bin. Numbers cannot be compared across papers (critique).

Rules for our log:
1. Report ECE next to AUROC and Brier. A constant predictor can have near-zero ECE (K09).
2. Report counts per bin and bootstrap intervals (K04, K22).
3. For small records prefer the CORP isotonic diagram and its MCB/DSC/UNC split over fixed bins (a08).
4. Use ECE only as a flag; rank by Brier (the World Cup ranking flipped, d13).

### 4.4 Recalibration maps

- **Temperature scaling.** p' = softmax(z / T). One parameter, fitted by minimising NLL on held-out labelled data. Kadavath used T = 2.5 for RLHF models (a12). Needs logits or token probabilities.
- **Platt scaling on stated probabilities.** Fit logit(p') = a * logit(p) + b by log loss on held-out items. Two parameters. Kotawala: 30% fit / 70% test, REL .0357 to .0004, Brier .228 to .185 (d16). Peng: per-model Platt matched the strongest single model in 7 of 16 groups at N > 1,000 (d17).
- **Isotonic regression.** Nonparametric, needs more data. Halawi: no gain for an already calibrated system (RMS error .42 vs crowd .38) (c05, d15).
- **Gate.** Apply a map only if measured REL is above about .01 on at least 100 items and a held-out split confirms the gain (K32 test). Under about 100 resolved items per class, do not recalibrate (K22).

### 4.5 Confidence elicitation

Ways to get a probability from a chat model, and what the evidence says:
- Token probability of a letter option: fine for pretrained models, broken after RLHF (K06).
- Verbalized probability, one stage ("answer, then probability"): Tian's best simple method.
- Top-k verbalized: k answers, each with a probability. Lowest ECE in Tian (gpt-3.5 TruthfulQA .451 to .203).
- Multi-sample agreement: fraction of fresh samples that agree. Higher AUROC on some tasks (GSM8K 54.8% to 92.7%) but the samples are correlated (G4). Agreement moves with temperature (66% to 30% from T = 0.2 to 2.0) while stated confidence does not move (d21).
- Effort or ability rating: on exact-answer tasks, a rating of expected effort predicted failure better than confidence (AUROC +10.1, +8.4, d23). These are scaled ratings, not true probabilities.
- Prompt wording matters more than the method label (d22).

### 4.6 Consistency checks (a pre-resolution signal)

Ask logically related questions and compute violations with no outcome needed:
- Conditional: P(A and B) should equal P(A) * P(B|A).
- Negation: P(A) + P(not A) = 1.
- And/or: P(A and B) <= min(P(A), P(B)); P(A or B) >= max(P(A), P(B)).
- Violation score: frequentist (count of violations beyond a tolerance) or arbitrage (profit a trader could lock in).

Result (Paleka; a25, b22, c31): conditional checks correlate .69-.92 with later Brier on both datasets. Negation changes sign across datasets. A second analysis (d16) finds negation and paraphrase checks carry little and and/or checks carry most; incoherence size predicted which bets lost most (CV AUC .775), but that is regret against a repaired quote, not Brier of the original. Part of the link is that stronger models are both more consistent and more accurate (b22). Use conditional and and/or checks only.

### 4.7 Scaffold structure that lowered Brier

- Sub-question decomposition (3-5 sub-questions researched, then fed to the forecaster): Brier .141 to .132, via calibration (d01).
- Per-evidence likelihoods aggregated in code (LEAP): .2497 to .2057 against a two-sample monolithic arm at about the same tokens (d03).
- Base probability then odds multipliers for a few situation factors, with scope, independence and aggregation checks (AuditForecast): full .0764 vs no scope check .0817, no independence check .0824, narrative aggregation .0815 (d04, 37 events, GPT-5.4).
- Common thread: the arithmetic of combining evidence is in code (G5); the model supplies local judgements.

### 4.8 Sample size and power

n about 0.139 / delta^2 for 80% power at base rate .5 (d19). A .02 edge needs about 350 independent resolved items, .01 needs about 1,400, .05 about 56. Correlated questions need down-weighting (effective N 178.8 in Bench to the Future, b24). So class-level Brier differences can be claimed only after about 350 independent items; coarse flags after about 100 (K31).

## 5. What holds up

### Replicated or multi-source
- Brier is strictly proper and accuracy is not (K01, two sources).
- The REL - RES + UNC split and its estimator bias (K03, K04). Several independent restatements.
- Temperature scaling repairs miscalibration in deep nets (Guo, many datasets) and in RLHF LLMs (Kadavath T = 2.5; GPT-4 report ECE .007 to .074) (K06, K07).
- ECE alone can be gamed (K09, three sources).
- Zero-shot LLMs without retrieval are near the .25 line on real-world forecasting (K11, four sources). Bench to the Future finds them below .25 on its pastcasting mix, so the level depends on the question mix.
- Retrieval plus reasoning scaffolds close part of the gap to the crowd but did not pass it before 2025 (K12).
- Averaging with a crowd or a second source beats either (K15).
- Training on a Brier reward calibrates stated confidence (K20, three groups).
- More reasoning tokens do not help calibration or Brier (K21: Yoon, Bench to the Future, KalshiBench, Sarfati).
- Pastcast backtests leak (K23).

### Contested
- **Verbalized vs token confidence (K08).** Tian: verbalized ECE far lower. Xiong: verbalized overconfident (ECE above .377 on older models). Yang 2026 re-ran both prompts side by side and found Tian's better, so the split is mostly a prompt effect. Both papers use ECE, which constants can game.
- **Direction of LLM bias (K14).** Yes-bias (Schoenegger, mean 57.35%, 14 of 31 yes); low-probability bias (Pratt); hedging toward the middle (Halawi, Prophet Arena, World Cup agents under-confident); over-confidence (KalshiBench: confidence 74-82% vs accuracy 64-69%; LEAP one-shot arm). Direction depends on model, prompt, base rate, and whether a price is shown.
- **Ensembling (K16).** Silicon crowd: 12-model median matched a crowd. Phan: base-LM ensemble .218 vs .210, no gain. Halawi: ensemble of all forecasters beat top-5 to top-30 subsets; trimmed mean was best of 5 aggregators.
- **Superforecaster gap (K27).** .054 in the 2025 paper, about .02 by Oct 2025, .017 in Mar 2026, but models were given market prices and GPT-4.5 correlates .994 with them. Good Judgment sees a wider gap on market questions.
- **Recalibration (K32).** Big win when raw calibration is bad (Kotawala), nothing when already good (Halawi), mixed in pooling comparisons (Peng).
- **Brier blind spots (K05).** An analytic point; no real-record case found where it changed a ranking (d14).

### Failed or weak results
- Fancy forecasting prompts did not beat one plain prompt. Pratt validation Brier: human market .1746, basic .1955, forecaster prompt .2097, breakdown .2053, base rates .2540, both sides .2159, crowd personas .1860, news API .1950 (c17).
- Asking for a rationale first raised predicted probabilities, moving the bias (c18).
- Chain-of-thought before confidence did not help (K25).
- The negation consistency check was not robust (K19).
- A belief notebook across dates lowered Brier for 6 of 12 models (none significant) and raised it significantly for two (Claude Opus 4.8 +.016, Kimi K2.5 +.021) (d05).
- A router that picks a reasoning mechanism by reliability features gave small gains: .1876 to .1846 on one vintage; frozen .1867 vs self-adjusting .1839 over 16 vintages (d06).
- The hedging explanation in Halawi is a stated hypothesis, not a test (d15).
- Extra injected news can make things worse: Brier .18 to .37 (d25).
- Ablation gaps of .003-.007 in Halawi are near the standard errors (.002-.003), each run once (K13).

### Moderators
- Question mix: hard markets sit near .25 without a price.
- Price visible or not: worth .04-.075 Brier; models converge on the price (d12, d13).
- Model era and training: pretrained vs RLHF (ECE .007 vs .074).
- Prompt wording (d22).
- Number of items: tiny N makes intervals useless (21 cases AUC [.471, .980]; 23 questions).
- Bin count for ECE and the decomposition.
- Evidence count: with 5 or more relevant articles Halawi's system scored .175 vs crowd .143 (84% of forecasts).

### Interventions that worked
Retrieval plus structured reasoning (about -.03 Brier vs plain, Halawi); top-k verbalized elicitation (ECE halved or better in Tian); Platt scaling on badly calibrated raw outputs; sub-question decomposition (-.009); per-evidence likelihoods in code (-.044 at matched tokens, one paper); averaging with an independent forecaster; Brier-reward training.

### Interventions that did not
Extra thinking; chain-of-thought before confidence; elaborate forecaster prompts; recalibration of an already calibrated system; belief notebook; routing by reliability features (small gain); persona or strategy prompts.

## 6. Language models

### Multiple-choice QA (calibration)
- Pretrained, up to 52B: well calibrated on lettered options, better with size and few-shot (Kadavath). Weak on none-of-the-above and out-of-distribution; P(IK) calibrates poorly on new tasks (c26).
- GPT-4 MMLU: ECE .007 pretrained, .074 after post-training (c25).
- After RLHF: T = 2.5 repairs most (a12).
- Chat models: verbalized beats label probability by ECE (Tian tables in section 3). Top-4 verbalized gave the lowest ECE on SciQ and TruthfulQA.
- Discrimination: GPT-4 AUC TriviaQA .950 label vs .937 verbalized (no gain), SciQ .820 vs .843, TruthfulQA .462 vs .622 (large gain on the hardest set) (critique correction 3).
- Xiong: GPT-4 average AUROC 62.7% across 8 tasks; vanilla verbalized ECE above .377 on older models; best aggregation ECE .028; consistency raised GSM8K AUROC from 54.8% to 92.7%.
- Prompt design explains much of the Tian vs Xiong gap (Yang 2026). Scores are heavily concentrated in a narrow range, so resolution stays low; models of at least 70B reach ECE about .10; a combo prompt took GPT-4o from .10 to .02 (d22).

### Forecasting real events (Brier)

| Study | Model | Brier | Reference |
|---|---|---|---|
| Halawi 2024 | GPT-4-1106 zero-shot | .208 | crowd .149; N = 914 |
| Halawi 2024 | retrieval + fine-tune + trimmed-mean system | .179 | accuracy 71.5% vs 77.0% |
| Schoenegger and Park 2023 | GPT-4 | .20 (SD .18) | crowd .07 (SD .08), N = 23 |
| Schoenegger 2024 | 12-model median | .20 (SD .12) | human .19, N = 31; GPT-4 alone .15 |
| Phan 2024 | ReAct ensemble | .169 | humans .172 |
| Bench to the Future 2025 | Sonnet 3.5 / 3.7 / 4 / Gemini 2.5 Pro | .1925 / .1712 / .1560 / .1611 | effective N 178.8 |
| ForecastBench 2025 | Claude 3.5 Sonnet / GPT-4o | .122 / .130 | super .096 / .076 |
| ForecastBench Oct 2025 | GPT-4.5 | .101 | super .081 (prices visible) |
| ForecastBench Mar 2026 | best entries | .103 | super .086 |
| Prophet Arena 2025 | GPT-5R, Grok-4R, Sonnet 4R | .184, .189, .194 | market .187 (+/-.006), price in prompt |
| KalshiBench 2025 | Claude Opus 4.5 | .227 | GPT-5.2-XHigh .433 |
| Afifi 2026 | Opus 4.5, no price | .256 soft-Brier | trained Qwen3.5-35B .254 |
| Turtel 2025 | RL-trained 14B | .190 | market .039 better; o1 .202 |
| World Cup 2026 (3-way Brier) | best agent | .471 | market .469 |

Pattern: without evidence or a price, models sit near .25 on hard questions. Retrieval and structure move them to about .17-.20 on mixed questions. With the market price shown, they converge on it (r .97-.99; GPT-4.5 .994) and none beats it reliably. Much of the "gap closing" is price copying.

### Reasoning, effort and calibration
- Reasoning models are overconfident (above 85% on wrong answers) and more so at higher effort (Yoon, b25). Introspection helped o3-Mini and R1 but hurt Claude 3.7 Sonnet.
- Thinking mode did not improve Sonnet 4: .1560 vs .1597, p = .53 (b23).
- GPT-5.2-XHigh used about 26 times more output tokens (2M vs 138K) and scored Brier .433, BSS -.799, ECE .395 vs Opus 4.5 .227 (d11).
- An 8B forecaster's free reasoning added +1.9 accuracy points over forced answers and left confidence nearly unchanged (d20).
- Structured decomposition with code aggregation helps (4.7). More free text does not.

### Training on Brier
Damani: ECE .37 to .03 in-domain, accuracy 61.7% vs 63.0%. Turtel 2026: five strictly proper rewards give different models. On 965 held-out items: Brier reward Brier .1648, ECE .0568, 1089 tokens; log reward .1653, ECE .0434, 454 tokens; base model .1861, ECE .1099, 663 tokens (d14).

### Fragility
Five injected articles flipped 69-73% of forecasts across 0.5 (three 7-8B retrieval forecasters, 500 ForecastBench questions); publisher name had no effect (d25). A class record is only as stable as the evidence pipeline behind it (K33).

### Humans reading LLM confidence
Users trust longer explanations more (model AUC .75-.78, participants .54-.60); matching explanation wording to true confidence narrows the gap (a26, K24).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = the S9 class record. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Score stated probabilities with Brier, never accuracy. [E]** Part S9 / G5. Brier is strictly proper; accuracy rewards rounding. Evidence a02, a04, b05, b06 (K01).
2. **Store REL, RES, UNC next to total Brier per problem class. [E]** Part S9 / memory. A useful forecast has Brier below UNC. Evidence a06, a07, b01, c34, d19 (K03). Compute from discrete-value bins and note the exactness condition.
3. **Report counts and intervals with every class number; do not recalibrate classes under about 100 resolved items. [E]** Part S9 / memory. Bin estimates are biased; learned calibrators need about 1,000. Evidence a08, a09, b02, b03, a17, d18 (K04, K22).
4. **Never rank or flag by ECE alone; log ECE with AUROC and Brier. [E]** Part S9. Constants game ECE. Evidence a13, a16, b11, c27 (K09).
5. **Keep .25 and the class base-rate forecast (UNC) as the two floors for every class; report BSS against the base rate as a derived view only. [E]** Part G7 / S9. Plain LLMs sit near .25. Evidence a18, a21, c01, c19 (K11, K12). Do not optimise BSS (K02, [S]).
6. **Tag each S9 entry with price/crowd-visible or not, and with freeze dates for prompt and tools. [E]** Part G3 / S9. Showing the price moves Brier by .04-.075; backtests leak. Evidence d10-d13, c32, b24 (K23, K28).
7. **Do not add a "think longer before stating confidence" step. [E]** Part G11. Evidence b23, b25, d11, d20, a14, c27 (K21, K25). Consistent with existing G11.
8. **Treat sampling agreement as a hint, not a probability. [E]** Part G4. Verbalized confidence has weak discrimination (AUROC 62.7%); agreement helps on some tasks but samples are correlated. Evidence a16, c28, d21 (K10).
9. **Do not compare Brier across classes with different base rates or across question sources. [E]** Part S9. Evidence b06 and critique.
10. **Do not compare multi-outcome Brier to the .25 line. [E]** Part S9. Critique caveat.

### Test first

Each item is a candidate only; see UNKNOWNS.md for tests and thresholds.

1. **Class-level Platt or temperature map on stated pass probabilities. [C]** Part S9. Evidence d16, d15, d17, a12, c25 (K06, K07, K32). U1.
2. **Top-k verbalized elicitation vs one-stage. [C]** Part G5/S9. Evidence a14, a15, b11, d22 (K08). U2.
3. **Agreement of fresh-context samples as the confidence signal vs a calibrated stated probability. [S]** Part G4/S9. Evidence a16, d21 (K10). U3.
4. **Scaffold effect on REL vs RES at equal tokens. [S]** Part G7/S9. Evidence d01, d03 (K26). U4.
5. **Effort-style rating next to stated confidence. [S]** Part S9/G5. Evidence d23, d24 (K30). U5.
6. **Conditional-consistency violations as a pre-resolution signal. [S]** Part G1/S9. Evidence a25, b22, c31, d16 (K19). U6.
7. **Push-to-extremes recalibration or full-range instruction. [C]** Part S9. Evidence a19, c04, d15, d11, d10 (K14). U7.
8. **Log both Brier and log score; check ranking differences on our record. [S]** Part S9. Evidence d14, d13 (K29). U8.
9. **Per-evidence likelihood aggregation by code (LEAP style). [S]** Part G5/O3. Evidence d03, d04, d01 (K26). U9.
10. **Averaging two different models' pass probabilities. [C]** Part G4. Evidence a22, c19, c06, d17 (K15, K16). U10.
11. **Re-check class calibration after any change to tools or sources. [S]** Part G3/S9. Evidence d25, d05 (K33). U11.
12. **Choice of Brier vs log for rare-event classes. [C]** Part S9. Evidence b04, c22, d14 (K05). U12.

## 8. Concrete tests on our bench

All tests use equal tokens across arms (count setup and extra samples). All report Brier with 95% bootstrap intervals, REL, RES and counts. Freeze prompts; tag freeze dates.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Calibration map | Exact-answer items with code checks, 5+ classes, 100-350 items per class; 30% fit / 70% test | Raw stated pass probability vs Platt vs temperature vs isotonic | Held-out Brier, REL, ECE | If raw REL > .01: Brier down about .02-.04 (Kotawala .228 to .185). If raw REL already low: no change (Halawi) |
| T2 Elicitation form | Same items | Token probability / one-stage verbalized / top-4 verbalized / two-stage with reasoning | ECE, AUROC, Brier | Top-k lowest ECE; two-stage no better than one-stage (K25); AUROC may stay near 63% |
| T3 Agreement vs stated | Same items, 5 fresh-context samples vs one stated number | Stated (calibrated) vs agreement (Platt-calibrated) vs both | AUROC and Brier of pass prediction | Agreement AUROC up to +10 points on arithmetic-like tasks; little on open tasks |
| T4 Scaffold vs plain split | 200+ resolved items per class | Plain vs scaffold (decompose + code aggregate), equal tokens | Brier, REL, RES separately | Brier down about .01 (d01); gain mostly in REL; RES flat |
| T5 Effort rating | Exact-answer task set | Stated confidence vs effort rating vs ability rating, before and after task | AUROC for failure; Brier after scaling | +8 to +10 AUROC points (d23) |
| T6 Consistency signal | 50 conditional pairs per class, then next-batch Brier | Conditional vs and/or vs negation violation | Correlation with next-batch Brier by class | Conditional r above .7; negation unstable |
| T7 Push-to-extremes | Held-out items where base rate is far from .5 | Raw vs full-range instruction vs extremise map fitted on train | Brier; share of forecasts under .1 or over .9 | Gain only if raw output is hedged; none or a loss if already over-confident |
| T8 Score choice | Pooled record | Rank classes by Brier vs log score vs ECE | Rank correlation; ties under .005 | Brier and log agree; ECE disagrees (d13, d14) |
| T9 Per-evidence likelihoods | Items with several evidence snippets | Monolithic vs two-sample mean (same tokens) vs LEAP-style code aggregation | Brier, ECE | Brier down about .04, ECE roughly halved (d03); likely smaller on our items |
| T10 Two-model average | 100+ items | Best single vs mean of 2 different models vs mean of 3 | Brier at equal total tokens | Gain from different models; none from same-model samples (G4) |
| T11 Source-change alarm | Re-run a class after changing retrieval | Before vs after | Change in REL | Detect drifts of about .02 and up |

Minimum sizes: about 350 independent resolved items for a .02 edge, 1,400 for .01 (d19). With fewer items report only coarse flags.

## 9. What does not transfer, and why

- **Absolute Brier numbers.** The literature mixes question sources, base rates, price visibility and models. Our items have exact answers and fast resolution. Only same-item, within-bench comparisons count.
- **The .25 line.** It is the score of always saying 50%. On a class with base rate .9, UNC is .09 and always saying .9 scores .09, so .25 is not the floor. Use UNC per class.
- **Superforecaster and crowd comparisons.** We have no human crowd. ForecastBench shows models copy prices; there is no analogue.
- **Crowd averaging (K15).** The analogue is a second, different model; G4 limits gains from same-model samples.
- **Training on a Brier reward (K20).** We train nothing. It shows only that calibration is learnable from a graded record.
- **Temperature scaling on logits (K06, K07).** Needs token probabilities, which chat APIs often hide. The Platt version on stated numbers is the usable analogue.
- **Consistency checks on real-world event pairs (K19).** On our items we have the real check outcome, which beats a consistency proxy. Consistency may still help in no-check mode.
- **Weeks-long resolution.** Code resolves in seconds, so our records fill faster than any forecasting study. Class sizes in S9 still start small.
- **Human trust effects (K24).** Relevant only if a person reads the agent's stated probabilities.
- **Hedging as a safety-training effect (K14).** The cause is untested; do not build on it.
- **Model age.** Most results come from 2023-2025 or 7-8B models.

## 10. Open questions

1. Does a thinking scaffold change reliability or resolution at equal tokens on resolved questions? One paper says reliability (d01).
2. Break-even number of resolved items before a class-level map beats raw stated probability. A few hundred items worked in one test; per-model Platt matched the best model in 7 of 16 groups (d16, d17).
3. Measured Brier of 2026 frontier models without a price on large resolved sets.
4. Whether hedging toward the middle is real for current chat models, and whether pushing to extremes gains Brier.
5. Which consistency checks predict Brier robustly across sources (only conditional held up).
6. How to map pass/fail checks to probabilities for exact-answer work, and whether Brier of that map tracks real accuracy gain better than raw pass rate.
7. Whether agreement among samples adds resolution beyond a calibrated stated probability.
8. Brier or log score for rare events; no real rare-event comparison exists.
9. Whether confidence before vs after reasoning matters for frontier chat models with long reasoning.
10. The founding texts (Brier 1950, Murphy 1973, Ferro and Fricker 2012) remain unread; exact partition conditions rest on later restatements.
11. How to detect an evidence-stream drift (d25) before Brier shows it.

## 11. Sources

[V] opened (PDF or page text, this run); [M] snippet or second-hand only.

### Founding and theory
- [M] Brier (1950) Verification of forecasts expressed in terms of probability. https://doi.org/10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2 (a01, b27, d26; HTTP 403)
- [M] Murphy (1973) A new vector partition of the probability score. https://doi.org/10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2 (a06, b26, d26; HTTP 403)
- [M] Ferro and Fricker (2012) A bias-corrected decomposition of the Brier score. https://ore.exeter.ac.uk/repository/handle/10871/8503 (b03)
- [V] Gneiting and Raftery (2007) Strictly proper scoring rules, prediction, and estimation. https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf (a02-a04, b05)
- [V] Wikipedia: Brier score. https://en.wikipedia.org/wiki/Brier_score (a05)
- [V] Brocker (2009) Reliability, sufficiency, and the decomposition of proper scores. https://arxiv.org/abs/0806.0813 (a07)
- [V] Dimitriadis, Gneiting and Jordan (2021) Stable reliability diagrams (CORP). https://arxiv.org/abs/2008.03033 (a08, a09)
- [V] Siegert (2013) Variance estimation for Brier Score decomposition. https://arxiv.org/abs/1303.6182 (b01, b02, c34)
- [V] Jewson (2004) The problem with the Brier score. https://arxiv.org/abs/physics/0401046 (b04)
- [V] Hoessly (2025) On misconceptions about the Brier score. https://arxiv.org/abs/2504.04906 (b06)
- [V] Nechepurenko and Shuvalov (2026) Foresight Arena. https://arxiv.org/abs/2605.00420 (d19; its LLM leaderboard is a simulation)
- [V] Guo, Pleiss, Sun and Weinberger (2017) On calibration of modern neural networks. https://arxiv.org/abs/1706.04599 (a10, b07, b08, c30)

### LLM calibration
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (a11-a13, b09, b10, c26)
- [V] OpenAI (2023) GPT-4 Technical Report. https://arxiv.org/abs/2303.08774 (c25)
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (a14, a15, b11, b12, c27)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (a16, b13, c28)
- [V] Kapoor et al. (2024) LLMs must be taught to know what they don't know. https://arxiv.org/abs/2406.08391 (a17, d18)
- [V] Yoon et al. (2025) Reasoning about uncertainty: calibration of reasoning models. https://arxiv.org/abs/2506.18183 (b25)
- [V] Steyvers et al. (2025) What LLMs know and what people think they know. https://arxiv.org/abs/2401.13835 (a26)
- [V] Yang, Tsai and Yamada (2026) On verbalized confidence scores for LLMs. https://arxiv.org/abs/2412.14737 (d22)
- [V] Sarfati et al. (2026) What LLM forecasters know but don't say. https://arxiv.org/abs/2607.08046 (d20, d21)
- [V] Bhattacharyya et al. (2026) Beyond confidence: rethinking self-assessments. https://arxiv.org/abs/2605.07806 (d23)

### LLM forecasting
- [V] Zou et al. (2022) Autocast. https://arxiv.org/abs/2206.15474 (a24, c29)
- [V] Schoenegger and Park (2023) LLM prediction capabilities. https://arxiv.org/abs/2310.13014 (a21, c11, c12)
- [V] Schoenegger et al. (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (a22, b17, b18, c13-c15)
- [V] Schoenegger et al. (2024) AI-augmented predictions. https://arxiv.org/abs/2402.07862 (c16)
- [V] Halawi et al. (2024) Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563 (a18-a20, b14-b16, c01-c06, d15)
- [V] Pratt et al. (2024) Can language models use forecasting strategies? https://arxiv.org/abs/2406.04446 (c17, c18)
- [V] Phan et al. (2024) Reasoning and tools for human-level forecasting. https://arxiv.org/abs/2408.12036 (c19, c20)
- [V] Karger et al. (2025) ForecastBench. https://arxiv.org/abs/2409.19839 (a23, b19-b21, c07-c10)
- [V] Paleka et al. (2025) Consistency checks for language model forecasters. https://arxiv.org/abs/2412.18544 (a25, b22, c31)
- [V] Paleka et al. (2025) Pitfalls in evaluating language model forecasters. https://arxiv.org/abs/2506.00723 (c32)
- [V] Hambly et al. / FutureSearch (2025) Bench to the Future. https://arxiv.org/abs/2506.21558 (b23, b24, c33)
- [V] Turtel et al. (2025) Outcome-based RL to predict the future. https://arxiv.org/abs/2505.17989 (c21)
- [V] Damani et al. (2026) Beyond binary rewards. https://arxiv.org/abs/2507.16806 (c22, c23)
- [V] Leng et al. (2025) Taming overconfidence in LLMs: reward calibration in RLHF. https://arxiv.org/abs/2410.09724 (c24)
- [V] Yang et al. (2025) Prophet Arena. https://arxiv.org/abs/2510.17638 (d10)
- [V] Nel (2025) KalshiBench. https://arxiv.org/abs/2512.16030 (d11)
- [V] Afifi et al. (2026) Do your own research. https://arxiv.org/abs/2610.01955 (d12)
- [V] Ding, Guo and Xu (2026) FIFA World Cup 2026 as a contamination-free benchmark. https://arxiv.org/abs/2607.17765 (d13)
- [V] Turtel et al. (2026) How proper scoring rules shape RL forecasters. https://arxiv.org/abs/2608.28482 (d14)
- [V] Bosse et al. (2026) Automating forecasting question generation and resolution. https://arxiv.org/abs/2601.22444 (d01, d02)
- [V] Chen et al. (2026) LEAP. https://arxiv.org/abs/2609.01337 (d03)
- [V] Cao et al. (2026) AuditForecast. https://arxiv.org/abs/2609.05905 (d04)
- [V] Ye et al. (2026) Forecast-Dojo. https://arxiv.org/abs/2609.28876 (d05)
- [V] Wang (2026) When should forecasting agents reason? https://arxiv.org/abs/2609.28475 (d06)
- [V] Kotawala (2026) Locally coherent, globally incoherent. https://arxiv.org/abs/2605.30335 (d16)
- [V] Peng et al. (2026) Two heads are better than one. https://arxiv.org/abs/2609.33257 (d17)
- [V] Manchuliantsau (2026) From checker to forecaster: RouteCast. https://arxiv.org/abs/2607.10972 (d24)
- [V] Lu and Zhang (2026) The corroboration illusion. https://arxiv.org/abs/2609.22246 (d25)
- [V, page-summarised] Forecasting Research Institute (Oct 2025) ForecastBench update. https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark (d07)
- [V, page-summarised] Forecasting Research Institute (Mar 2026) Introducing the Brier Index. https://forecastingresearch.substack.com/introducing-the-brier-index (d08)
- [V, page-summarised] Good Judgment (2026) What ForecastBench doesn't measure (yet). https://goodjudgment.substack.com/p/what-forecastbench-doesnt-measure (d09)

Seen only as snippets or second-hand, details unverified (critique): Mason 2004, Pratt table column order, Phan numbers beyond those above, Leng, Yoon, Hambly, Kapoor results tables, Hoessly, Steyvers, Paleka Pitfalls counts, the Autocast calibration number, the Silicon-crowd "17 to 28%" accuracy gain.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 15 established claims: 9 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E03.01-K03** (reworded: the sources support less). Siegert confirms Br = REL - RES + UNC (Murphy 1973) with UNC the Brier of the climatological mean. The decomposition in Siegert is defined for any forecast via the calibration function P(y=1|p); Brocker's 'finite-valued' refers to targets (outcomes), not forecasts. Exactness only for finitely-valued forecasts applies to the empirical (binned) estimators, which neither source states as an 'only' condition. Corrected claim: Mean Brier splits as REL - RES + UNC (Murphy 1973), with UNC = base rate x (1 - base rate), the Brier score of the climatological forecast; a useful forecast has Brier below UNC. The population decomposition holds for general forecasts, but sample estimates are exact only when forecasts take a finite set of repeated values; otherwise binning approximates it.
- **E03.01-K04** (reworded: the sources support less). Siegert (bias-corrected Brier-decomposition estimators have larger variance) and Dimitriadis et al. (binned reliability-diagram estimates: squared bias m(n)^-2 vs variance growing with bin count; CORP MSE compared in Fig. 5) are verified, but neither source analyses ECE, and the CORP MSE comparison is for conditional event probability estimates in reliability diagrams, not for ECE or score-decomposition estimates. Corrected claim: Binned reliability-diagram and Brier-decomposition estimates depend on the bin count and are biased (Dimitriadis et al.; Siegert); bias-corrected decomposition estimators reduce bias but have larger variance (Siegert); in the CORP authors' simulations, the bin-free isotonic (CORP) reliability-diagram estimates had the lowest MSE of the binning variants compared. ECE is not analysed in these sources.
- **E03.01-K10** (reworded: the sources support less). Xiong: GPT-4 vanilla avg AUROC 62.7% over 8 tasks verified; GSM8K 54.8 to 92.7 AUROC verified but it is GPT-3.5 with 5 sampled CoT responses + consistency vs a single response (the claim does not name the model). 'Weakly' is not general: Tian et al. report GPT-4 verbalized AUC .937-.950 on TriviaQA. 'Samples are correlated' is an inference, not in the sources. Corrected claim: On Xiong et al.'s eight tasks GPT-4's vanilla verbalized confidence separates right from wrong only weakly (average AUROC 62.7%, chance 50%), though on easy factual QA such as TriviaQA GPT-4 verbalized confidence reaches AUC about .94 (Tian et al.); sampling 5 responses and measuring agreement raised GPT-3.5's GSM8K AUROC from 54.8% to 92.7%.
- **E03.01-K11** (number corrected). Halawi Table 7 zero-shot Brier for the other models ranges from .219 to .353 (Llama-2-7B .353, Llama-2-70B .283, GPT-3.5-1106 .274), not '.215-.268' (.215 and .268 are single scratchpad cells). GPT-4-1106 .208, S&P GPT-4 .20 vs .25 (t(22)=-1.23, p=.23), Hsieh et al. base-LM ensembles (.218 vs .210; GPT-4 .265, GPT-3.5 .261, Llama3 .256) and Bench to the Future (all no-evidence models better than .25) verified. Also the paper cited as 'Phan' is by Hsieh, Fu and Chen (UC Berkeley). Corrected claim: Zero-shot LLMs without retrieval score close to the 0.25 coin-flip line on forecasting questions (Halawi et al.: GPT-4-1106 .208, other models .215-.353 across zero-shot and scratchpad prompts, many at or worse than .25; GPT-4 .20 not distinguishable from .25 in Schoenegger and Park, N=23; Hsieh et al. base-LM ensembles mostly worse than .25). Bench to the Future finds all no-evidence models better than .25, so the level depends on the question mix.
- **E03.01-K15** (reworded: the sources support less). Schoenegger and Park's BMA blend (.13) is better than GPT-4 (.20) but worse than the human crowd (.07), so it does not beat both; Silicon-crowd result is average (.13/.14) vs the models' own updated forecasts (.14/.15), not vs the human crowd; only Halawi (aggregate .146 vs crowd .149 and system .179) shows the average beating both. Corrected claim: Averaging an LLM forecast with the human crowd can beat the LLM alone and sometimes the crowd: Halawi's weighted average of system and crowd scored .146, better than crowd .149 and system .179; in Silicon Crowd, a simple human-machine average (GPT-4 .13, Claude 2 .14) beat the models' own updated forecasts (.14, .15); but in Schoenegger and Park (N=23) the blend (.13) beat GPT-4 (.20) yet not the crowd (.07).
- **E03.01-K21** (reworded: the sources support less). Verified: Yoon et al. (confidence often above 85% on incorrect answers, more overconfident with deeper reasoning, introspection helped o3-Mini/R1 but not Claude 3.7 Sonnet), Bench to the Future (Sonnet 4 .1560 vs Thinking .1597, p=.53), KalshiBench (Brier .433 vs .227; 26x tokens, 2M vs 138K), Sarfati (+1.9 pp free vs forced). But the KalshiBench contrast is between two different models (GPT-5.2-XHigh vs Claude Opus 4.5), not a controlled reasoning-effort comparison, so it cannot show reasoning caused the worse Brier. Corrected claim: More reasoning does not help calibration or forecast Brier in the sources read: reasoning models are overconfident (confidence often above 85% on wrong answers) and more so with deeper reasoning (Yoon et al.); thinking mode did not improve Claude Sonnet 4 on pastcasting (.1560 vs .1597, p=.53); introspection helped o3-Mini and R1 but hurt Claude 3.7 Sonnet. KalshiBench found the extended-reasoning GPT-5.2-XHigh (26 times more tokens) had Brier .433 vs .227 for Claude Opus 4.5, though this compares different models; an 8B forecaster's free reasoning added only +1.9 points accuracy over forced answering.
- **E03.01-K07** (now single-source: only one opened source, code check).
