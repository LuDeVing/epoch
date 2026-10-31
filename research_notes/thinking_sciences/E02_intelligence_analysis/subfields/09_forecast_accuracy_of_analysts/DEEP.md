# Forecast accuracy of analysts: deep document

*Subfield E02.09. Writer pass over evidence_a-d.jsonl (a01-a28, b01-b30, c01-c28, d01-d23), claims.jsonl (K01-K31) and critique.md. Evidence ids in brackets. Status: [E] established, [S] single-source, [C] contested.*

## 1. What it is

This subfield asks one measurable question: when intelligence analysts give probability forecasts about real events, how accurate are they, and what raises or lowers that accuracy?

Three things sit inside it.

- **Field audits of real analyst forecasts.** The key work is Mandel and Barnes (2014, PNAS). It scored 1,514 forecasts from one Canadian strategic intelligence unit against outcomes coded later [a01, b01].
- **Tournament science on how to improve forecasts.** The Good Judgment Project and the IARPA ACE tournaments tested training, teaming, tracking and aggregation [a08, b12]. This links to E03.
- **Machine forecasters.** Since 2022, many papers score language models on the same kind of question and compare them with human crowds and superforecasters [a12, a15, a20, d07].

Why it matters for our agent. Forecasting is a domain where the answer is a probability, and a probability can be scored exactly once the event resolves. That gives a hard, label-based test of calibration and of aggregation rules. Both are scaffold questions: how to pool several samples, whether to stretch the pooled answer, whether to show an outside prior, and whether added reasoning steps help.

Scope notes.

- Scoring terms. Brier score: mean squared error of the probability; 0 is perfect, 0.25 is always saying 50%. ROC area (A or AUC): chance that a random event-that-happened got a higher probability than a random event-that-did-not. ECE: expected calibration error.
- Brier scores from different question sets cannot be put on one scale [a26, K02]. Every number below carries its question set.
- Subfields researched in parallel and not covered here: scoring rules and calibration, wisdom of crowds, sampling and voting (self-consistency), language agents as architectures, expected value of sample information. Only links are noted.

## 2. History and theories in depth

### 2.1 Kent and the problem of words (1964)

Sherman Kent showed that colleagues read "serious possibility" as anywhere from 1 in 4 to 4 to 1 odds [a07]. Intelligence products used words, not numbers. The cost persists: in Mandel and Barnes follow-up work, 44% of Canadian analyst forecasts could not be coded to a number because the wording was vague [d15, K29]. In the 2014 pool, about 16% of numeric-era forecasts were verbal only [a05].

### 2.2 Tetlock 2005: the baseline of poor expert forecasts

Tetlock's Expert Political Judgment is the founding long-run study. Second-hand figures, as quoted by Mandel and Barnes: the best forecasters explained about 20% of outcome variance; experts were overconfident; experience did not help [a27, b29]. The book itself was not opened. Horizons were long, often five years or more [a06].

### 2.3 Mandel and Barnes 2014: a different picture

Setting. 15 analysts in one Canadian unit, Middle East and Africa topics, March 2005 to December 2011. 3,881 coded judgments, 2,315 unconditional forecasts, 1,943 with a numeric probability, 1,562 with a clear outcome (80.4%), 1,514 kept [a01]. Outcomes were coded afterwards by two outside experts with 90% agreement on 50 overlap items [a05]. 7 of 15 analysts were senior and wrote about 68% of the forecasts [a01].

Headline. ROC area 0.940 (SE 0.007), mean Brier 0.074, about 94% of forecasts on the correct side of 50%, 76% of outcome variance explained, calibration index 0.016 [a02, b01]. The authors set this against Tetlock's about 20% and a calibration deviation about 25% smaller [a05, b06].

The error that remained was underconfidence, not overconfidence: signed deviation -0.076 (99% CI -0.082 to -0.070) [b03]. Experience did not change it (P > 0.15) [a04].

### 2.4 Tetlock and Mellers 2014: the reply

The Good Judgment Project leaders accepted the data and disputed the reading [a06, b07, b08].

- 59% of questions resolved within 6 months and 96% within one year. Tetlock's poor results were long range.
- Over half of forecasts scored Brier 0 or 0.01. 55% of questions were rated "harder" only in hindsight.
- Best GJP teams reached Brier scores similar to the Canadian analysts on similar horizons.
- Brier treats over- and under-prediction alike, but real costs are asymmetric; agencies tend to shift thresholds after a visible miss.

The cost contrast (about $5 million a year for the tournament against over $5 billion for the intelligence community) is rhetorical and was not measured.

### 2.5 The tournament line: training, teaming, tracking, aggregation

IARPA ACE ran from 2011. The Good Judgment Project won both seasons and was the only funded team from 2013 [a09, secondary only]. Mellers et al. 2014 named three interventions, training, teaming and tracking, plus statistical aggregation [a08, abstract only]. The 2024 review gives numbers: training raised accuracy 6% to 11% per year; teams of 10 to 15 beat independent forecasters in each of 4 years; more than 50% of the gain from the interventions was noise reduction (BIN model) [b12]. Statistical rules beat human intuition by a small margin in the Grove et al. 2000 meta-analysis, d = 0.12 (cited, not opened) [b28, K21].

### 2.6 Aggregation theory: why averaging is not enough

Averaging many noisy probabilities pulls the result toward 0.5. Two separate reasons to push it back out [d18, abstract only for numbers]:

1. Averaging noisy probabilities shrinks toward the middle (not so for the median or mean log odds).
2. Forecasters hold different information and each ignores that others know other things.

Satopaa and Ungar (2015) show that a weighted average of forecasts with non-trivial weights is never optimal and should be extremized. The stretch is justified when forecasters hold partly different information, not when they share it or have correlated errors [a10]. A stylised example: the group jointly knows 80% of the information, while the revealed aggregate captures about 32% [a11]. Neyman and Roughgarden (2022) prove guarantees for average-then-extremize by a constant when information has diminishing returns [d19].

### 2.7 Critiques of analyst tradecraft

Mandel and Tetlock (2018) argue that structured analytic techniques were built without accuracy tests, may add noise, and that overconfidence warnings can create the mirror bias, underconfidence. They recommend outside testing, recalibration, aggregation and accuracy tracking [a07, b09]. Controlled tests back this: ACH did not improve probability accuracy with 50 UK analysts [d14]; ACH matrix layout did not reduce confirmation bias in 62 Dutch military analysts (putting hypotheses in rows did) [b11].

### 2.8 The machine line, 2022 to 2026

- 2022: Autocast. Best retrieval model 65% on true/false against 92% for the crowd; 40% calibration error against 8% [a19, c21].
- 2023: GPT-4 in a live Metaculus tournament, 23 questions, Brier 0.20 against crowd 0.07, not better than always saying 50% [c09].
- 2024: Halawi et al. (retrieval plus tuned reasoning plus ensemble, 0.179 against crowd 0.149) [a12]; Schoenegger silicon crowd (12-model median matches 925 humans) [a15]; Hsieh agent loop matches a market crowd [b27]; ForecastBench launched [a20].
- 2025: reasoning models reach the old crowd benchmark (o3 0.1352) [c27]; outcome-based RL [a24]; Prophet Arena and FutureX live tests [d12, d13]; AIA Forecaster report [d07]; Metaculus bots vs Pros [d03].
- July 2026: ForecastBench organisers report scaffolded systems statistically indistinguishable from superforecasters [d04].

## 3. Core findings with exact numbers

Question sets differ in every row. Do not compare Briers across rows.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Real analyst forecasts are highly discriminating and calibrated | ROC area 0.940 (SE 0.007); Brier 0.074; variance index 0.240; discrimination index 0.182; eta2 0.758; calibration index 0.016; N=1,514 | Mandel and Barnes 2014 [a02, b01] | [E] for the unit studied; one unit |
| Result survives pessimistic coding | Ambiguous outcomes at partial credit: Brier 0.090. Verbal-only forecasts set to 0.50: Brier 0.097 | [a05, b02] | [E] |
| High score partly question mix | 59% of questions under 6 months, 96% under 1 year; over half scored Brier 0 or 0.01; 55% "harder" | Tetlock and Mellers 2014 [a06, b07] | [E] |
| Analysts are underconfident | Signed deviation -0.076; harder -0.106 vs easier -0.044 (Z=-13.39); more important -0.071 vs -0.044 (Z=-4.49); experience no effect | [b03, b04] | [S] |
| One-parameter recalibration fixes most of it | a=2.2: calibration index 0.016 to 0.0018; mean absolute deviation 12.7% to 4.2% (-66.9%). Fitted in-sample | [b05] | [S] |
| Seniority and ease raise discrimination | Senior 0.951 vs junior 0.909 (Z=2.24, p=0.025); easier 0.966 vs harder 0.913 (Z=3.57, p<0.001); importance, time frame p>0.25 | [a04, b04] | [S] |
| Same unit, larger sample, same pattern | 3,622 forecasts, 2,013 codable; high discrimination, underconfidence held; extreme forecasts (p<=.05 or >=.95) discriminated worse | Mandel and Barnes 2018 [d15] | [S] internal replication |
| Calibration training moves bias, not monitoring | 70 analysts; shift toward less confidence; gains on two tasks uncorrelated | Mandel et al. 2024 [d22] | [S] |
| ACH does not help probability accuracy | 50 UK analysts; MAE ACH 0.26 vs control 0.21 (p=.14, d=0.43); coherentising cut MAE 0.23 to 0.15 (35%, d=0.96); simple normalising 0.13 | Mandel, Karvetski, Dhami 2018 [d14] | [S] |
| Natural-frequency tutorial improves Bayesian answers | 43 analysts pre/post; mean absolute bias for P(H given D) 0.144 vs 0.009 for P(not-H given D); over four fifths additive on all 8 problems after | Mandel 2015 [b10] | [S] |
| Training, teams, tracking, aggregation help | Training +6% to 11% per year; teams beat independents in 4 of 4 years; over 50% of gain was noise reduction | Mellers et al. 2024 [b12] | [E] |
| Finer probabilities are more accurate | 888,328 forecasts; coarse rounding lost accuracy; at least 4 categories helped | Friedman et al. 2018 [b14, b13] | [E] |
| Persuasive rationales are not more accurate | Forecast level beta 0.007 (BF10 0.024); forecaster level beta 0.04; confident style r=-0.02; insistent r=-0.38; 153 forecasters, 474 raters | Shemesh et al. 2025 [b15] | [S] |
| Coherence links to accuracy only conditionally | Poker experts r=0.37 (N=186), novices 0.28, amateurs 0.06; no separation in military analysts | Zhu et al. 2022 [b16]; Dhami 2024 [b11] | [C] |
| Early LLMs trail the crowd | Halawi: system 0.179, crowd 0.149, random 0.250; accuracy 71.5% vs 77.0%; best no-retrieval GPT-4-1106 0.208. Autocast 65% vs 92%. GPT-4 0.20 vs crowd 0.07 (N=23) | [a12, a19, c09] | [E] |
| LLM median crowd matches human crowd | 12 LLMs, 31 questions: 0.20 (SD 0.12) vs humans 0.19 (SD 0.19), p=0.85; vs 0.25 baseline t(30)=-2.35, p=0.026. Equivalence test not preregistered | Schoenegger 2024 [a15, c06] | [E] with low power |
| Best single model near human crowd | GPT-4 0.15, GPT-4+Bing 0.16, Bard 0.19, Falcon 0.21, Claude 2 0.21, Mistral-7B 0.24, GPT-3.5-Instruct 0.25, Llama-2-70B 0.25 | [a16] | [S] |
| Retrieval and tuning close most of the gap | Neither retrieval nor tuning: 0.206; full 0.179; removing one costs only 0.002 to 0.007 (0.181 to 0.186) | Halawi [b18, c04, critique] | [S] |
| Averaging model with crowd beats both | 4x crowd weight: 0.149 to 0.146 (Halawi); GPT-4 0.13 and Claude 2 0.14 with simple average vs updated model 0.14 to 0.17 | [c03, b20] | [E] |
| Model wins only where crowd is unsure | Crowd .3-.7: system .199 vs crowd .246 (validation); crowd near 0 or 1: system accuracy +7% but Brier 0.04 worse | [a13, b18] | [S] |
| Showing the human median helps the model | GPT-4 0.17 to 0.14 (p=0.003); Claude 2 0.22 to 0.15 (p<0.001); update size tracks gap r=0.88, 0.87 | [a17, b20] | [S] |
| LLM assistants raise human accuracy | N=991, 6 questions: +24% to 28% vs control; without outlier: +41% (good assistant), +29% (noisy) | Schoenegger 2024 [a18, b21] | [E] |
| Reasoning LLMs reach the old crowd benchmark | o3 0.1352, o3-pro 0.1386, GPT-4.1 0.1542, o4-mini 0.1589, DeepSeek-v3 0.1798, GPT-4o 0.1883; 464 Metaculus questions | Lu 2025 [c27] | [C] |
| Lu "experts beat o3" is a mean-vs-median comparison | Expert median 0.0225, expert mean 0.1573 (N=157), o3 mean 0.1352 (different subsets) | Critique correction 1 [b22, c27] | [C] |
| Superforecasters led LLMs on ForecastBench (2024-25) | Supers 0.096, public 0.121, best LLM (Claude 3.5 Sonnet) 0.122 on 200 questions; with combination questions supers 0.076 vs GPT-4o 0.130; gap 0.054 vs GPT-4 to GPT-4o 0.026 | Karger 2025 [a20, c11] | [E] for that date |
| Trend projection to parity | Brier vs Arena r=-0.68 (p=0.003, R2=0.47), crossing near Arena 1406 (CI 1346-1633); vs log compute r=-0.67 (p=0.046) | [a21, c13] | [C] small N |
| Bots lost to Pros in 2024-25 | Head-to-head -17.7, CI [-28.3, -7.0], p=0.0014; 424 bot questions, 10 Pros, 96 scorable | Metaculus [d03] | [S] |
| Parity claimed July 2026 | One-sided p vs supers: Cassi AI 0.41, xAI 0.15-0.16, DeepMind 0.14. Human data from July 2024 | FRI / ForecastBench [d04, d06] | [C] non-rejection, not a win |
| AIA Forecaster vs supers | FB-7-21: AIA 0.1076 vs supers 0.1110 vs public 0.1451; FB-Market: 0.0753 vs 0.0740 vs market 0.0965 | Alur 2025 [d07] | [S] vendor report |
| Agentic search helps | No search 0.1230; Search-A non-agentic 0.11738, agentic 0.1140; Search-B 0.12168 / 0.11824 | [d08] | [S] |
| Averaging samples is a strong baseline | 10 samples: mean 0.1140, trimmed 0.1142, median 0.1138, single 0.1182; most gain by 5 samples; LLM synthesiser worse; agentic supervisor 0.1125 | [d09] | [S] |
| Pooling rule barely matters | Mixed ensemble: median 0.197, trimmed 0.197, geometric mean 0.194, geometric mean of log odds 0.194 | Karger ICLR [d05] | [S] |
| Post-hoc stretch helps | 0.1140 to 0.1085 (fixed d=3) and 0.1076 (Platt, coefficient about 1.73); out-of-distribution fit 0.1104 vs 0.1125 unstretched; optimum 2.27 (AIA), 1.72 (supers) | [d10, d18, d19] | [S] |
| Market price in prompt | No search 0.116 to 0.103; best config 0.085 to 0.075 (about 11%); overlaps with search; earlier LLM with price 0.109 vs price alone 0.096 | [d08, d05] | [S] |
| Prompt strategies barely help | 38 prompts x 4 models, 100 questions: control Briers 0.208 to 0.227; best prompts about -0.004 to -0.014 (frequency-based -0.014, base rate first); compound prompts did not stack; superforecaster-written prompt worse | Schoenegger 2025 [d01, d02] | [E] |
| Plain prompt beat added strategies | Every strategy variant scored worse than the single plain prompt (GPT-4 class) | Pratt 2024 [c19, c20] | [E] |
| Narrative framing hurts | Narrative Briers: Qwen3-32B .2218, Claude 3.6 Sonnet .2267, DeepSeek-v3 .2633, GPT-4o-mini .2942; direct better for all | Lu 2025 [c28] | [S] |
| Outcome-based RL improves calibration | 14B model Brier 0.190 [0.178, 0.203], ECE 0.062 vs o1 0.202, ECE 0.093; market still 0.039 better. Self-play fine-tune: Phi-4 0.200 vs base 0.221 vs control 0.214 | Turtel 2025 [a24, b26] | [E], but training |
| Frontier models match market on live Kalshi | GPT-5 0.184 (CI 0.006) vs market 0.187, 1,367 events, 76% sports; ECE about 0.04 vs 0.067; lost money (return 0.943) | Prophet Arena [d12] | [S] |
| Benchmarks leak | At least 3.8% of Halawi questions resolve early; at least 10% of another trivial; date-restricted search leaks. AIA audit: 1.65% of results leak, Brier shift under 0.001; gpt-oss-120b's 0.1076 came from leaks | Paleka 2025 [b24]; Alur [d11] | [E] |
| Consistency tracks Brier but does not transfer | Correlation 0.85 (aggregate), 0.49, 0.69, about 0.92 (conditional); optimising checks did not improve Brier or held-out checks | Paleka 2024 [b25, c15, c16] | [C] |
| Numbers beat words | N=1,202: numeric and combined beat verbal on all three agreement measures | Mandel and Irwin 2021 [d16] | [S] |
| Rationale quality is a weak label-free signal | LLM-scored rubric: forecast level r=.19 (pre-LLM .06); forecaster level r=.51 (.39); 55,000 pairs, about $0.007 each. Nine calibration questions r=0.267 | FRI [d20, d21] | [S] |

## 4. Mechanisms and models

Each mechanism is written so it can be built.

### 4.1 Scoring and decomposition

Brier = mean of (p - o)^2 where o is 0 or 1. Mandel and Barnes use the Yates decomposition: variance index (how much outcomes vary), discrimination index (how far forecasts separate yes from no), calibration index (how far stated probabilities sit from observed frequencies) [a02]. Implementation: store every forecast with its outcome; report Brier, AUC, calibration index and ECE separately. Add a skill score against a base-rate forecaster, 1 - Brier / (b(1-b)), because raw Brier rewards easy mixes [a22, K02]. Paleka's example: 50 questions at 50% base rate plus 50 at 5%; a forecaster perfect on rare events scores about 0.125, while one who only improves the coin-flips from 0.25 to 0.15 scores about 0.10 and looks better [a22].

### 4.2 Underconfidence correction (recalibration map)

Mandel and Barnes fitted a Karmarkar-style one-parameter transform with a = 2.2 [b05]. An equivalent form in log odds: p' = sigmoid(a * logit(p)), with a > 1 stretching away from 0.5. Procedure for an agent:

1. Collect resolved forecasts (pooled outputs, not single samples).
2. Fit a on one half, test on the other half (the human paper fitted and judged on the same data, which is its weak point).
3. Clip p to [0.01, 0.99] before the logit.
4. Apply only if a > 1 holds out of sample.

AIA's numbers: optimum 2.27 for their system, 1.72 for superforecasters; fixed d=3 gave 0.1085 and Platt 0.1076 (coefficient about 1.73); a coefficient fitted on another benchmark kept part of the gain (0.1104 vs 0.1125) [d10, K25]. The stretch only helps if the call is on the right side of 0.5, and the gain is likely smaller for newer, better-calibrated models (ECE about 0.04) [d12].

### 4.3 Aggregating several forecasts

Pool N independent forecasts p_1..p_N. Options measured:

- Mean, trimmed mean, median: equal within 0.0004 at 10 samples [d09].
- Geometric mean of log odds: 0.194 vs 0.197 for median in a mixed-model ensemble [d05]. Slight edge at the same cost.
- Then optionally extremize in log odds (4.2).

Most gain arrives by 5 samples (single 0.1182, mean of 10 0.1140) [d09]. Reading all samples with an LLM and writing one forecast was worse than the mean [d09]. A supervisor agent with its own search and a confidence gate was slightly better (0.1125) [d09].

Why extremizing is needed after averaging: shrinkage toward 0.5 from averaging noisy values, plus partly different information held by members [d18, a10]. For samples from one model the information is the same, so the second reason is weak; only the shrinkage and the model's own hedging remain. This matters for G4 (samples from one model are not independent).

### 4.4 Ensemble caveat for base models

Ensembles helped ReAct agents (SD 0.092 across runs vs 0.150 for base models; median of 3 0.169, mean 0.170, sampled single 0.180) but hurt base GPT-4o (ensemble 0.218 vs single 0.210) [b27, c18]. The benefit depends on members having independent search and error, not on resampling alone.

### 4.5 Outside prior combination

Two ways to use a crowd or market number x:

- Average: p = w * x + (1 - w) * model. Halawi weight 4:1 toward the crowd, 0.149 to 0.146 [c03]. Schoenegger: simple average GPT-4 0.13, Claude 2 0.14, both better than the model updating on x (0.14 and 0.15) [b20].
- Show x in the prompt: Brier 0.116 to 0.103 without search; 0.085 to 0.075 for the best config [d08]. This largely replaces search. The earlier ForecastBench LLM with the price scored worse (0.109) than the price alone (0.096) [d05].

Code should do the average; the model should not be asked to update on the number. The model moved toward the median by an amount that tracked the gap (r = 0.88 and 0.87), which is conformity as well as learning [a17].

### 4.6 Selective forecasting

Halawi found the system beats the crowd only when the crowd is unsure (0.3 to 0.7), the question is early, and at least 5 relevant articles are found: by more than 1.5 standard errors [c02]. Where the crowd is certain, the system is less extreme and loses 0.04 Brier despite 7% higher accuracy [a13]. Implementation: a gate that defers to the outside prior when it is near 0 or 1, and uses the model's own forecast otherwise. The rules were found on validation and applied to test [a13]; category-level gaps are noisy.

### 4.7 Label-free quality signals

- Consistency arbitrage: correlated with Brier up to R about 0.92 on some checks; optimisation on checks did not generalise [c15, c16].
- LLM-scored rationale rubric: r=.19 per forecast, .51 per forecaster [d20]. Rationale length correlates with human ratings (r=.62) but not with accuracy.
- Nine quick calibration questions before a hard forecast: r=.267 [d21].

Treat all as weak proxies for ranking sources, not as a replacement for resolved outcomes.

## 5. What holds up

### 5.1 Replications and consistency

- **Mandel and Barnes 2014.** No independent agency replication found [d15, d14, d22, K28]. The nearest is internal: the same organisation, 3,622 forecasts, 2,013 codable, same discrimination and underconfidence, and forecasts at p<=0.05 or >=0.95 discriminated worse [d15]. Other analyst groups show related patterns (UK analysts, 70 analysts in calibration training), but on different tasks.
- **Wisdom of crowds for LLMs.** The 12-model median matched humans, and individual models differed (F(12,354)=2.64, p=0.002) [a16]. Only 31 questions; later work says the study likely lacked power to detect real gaps [a15 limits]. Aggregation helps in other sets: ForecastBench ensemble 0.194-0.197, RTF agents, AIA 10 samples.
- **Aggregation and extremizing.** Established in humans through the IARPA line [b12, d18]; shown on LLM outputs by AIA (single source) [d10].

### 5.2 Failures and contradictions

- **Lu 2025 expert comparison** set a median against a mean; the expert mean (0.1573) was worse than o3 (0.1352) [critique, K11].
- **Acquiescence bias** (mean 57.35%, t(1006)=86.2) [c07] is not general. Pratt found low-probability guessing; AIA found hedging toward 0.5; reasoning models averaged 41.5% to 44.8% [c19, d02, d07, K13].
- **Schoenegger-Park 2023** (N=23, GPT-4 0.20 vs crowd 0.07) contradicts the 2024 near-parity result; the question sets differ [c09].
- **Coherence.** Poker experts r=0.37; amateurs 0.06; military analysts no separation [b16, b11].
- **Ensembling.** Helps agents, hurts base GPT-4o [b27].
- **Consistency optimisation** improved its own checks but not held-out checks or Brier [c16].
- **Parity.** ForecastBench 2025: supers 0.096 vs LLM 0.122. July 2026: statistical parity not rejected (p 0.14 to 0.41). Different eras, different systems, human data from July 2024 [a20, d04, d06].
- **Halawi ablation wording.** The 0.206 figure is for no fine-tuning AND no retrieval, not no retrieval alone [critique correction 2].

### 5.3 Moderators

- Horizon and question mix (Brier 0.074 with 96% under a year vs Tetlock's long range) [a06].
- Difficulty (AUC 0.966 vs 0.913) and seniority (0.951 vs 0.909) [a04].
- Crowd certainty, retrieval date and number of articles (LLM only) [c02].
- Topic: models do better on politics than on economics and finance [c28]. Prophet Arena was 76% sports [d12].
- Base rate: Brier overweights high-base-rate questions [c25].

### 5.4 Interventions that worked

- Training, teaming, tracking (humans) [b12].
- Pooling and extremizing [a10, d10].
- Finer-grained probabilities [b14].
- Natural-frequency tutorial (43 analysts) [b10].
- Coherentising then averaging analyst probabilities: MAE down 35% from coherentising [d14].
- For LLMs: agentic search (0.1230 to 0.1140), averaging samples, log-odds stretch, outside prior, frequency format, base rate first, step-back [d08, d09, d10, d01].
- Outcome-based RL with an accuracy-plus-Brier reward; an accuracy-only reward damaged calibration [a24, d23]. Outside the scaffold.

### 5.5 Interventions that did not work

- ACH on probability accuracy [d14].
- Calibration training as a monitoring gain (it only shifted bias) [d22].
- Written persuasion as a signal [b15].
- Prompt strategies in general: base rate, decomposition, personas, news (Pratt); an explicit Bayesian-update prompt hurt (about +0.03) and propose-then-select hurt [c19, d01, d02].
- Stacking the best prompts [d02].
- Superforecaster-written prompts: the only one significantly worse [d02].
- Asking an LLM to synthesise samples [d09].
- News access on ForecastBench; scratchpad plus crowd input was best [c12].
- Reasoning models vs non-reasoning on the 100-question set: o1 0.216 vs GPT-4o 0.208 [d02].

## 6. Language models

### 6.1 Level, over time

| Date | System | Brier | Reference | Source |
|---|---|---|---|---|
| 2023 | GPT-4, live Metaculus (N=23) | 0.20 | crowd 0.07 | [c09] |
| 2024 | GPT-4-1106 no retrieval | 0.208 | crowd 0.149 | [a12] |
| 2024 | Halawi full system | 0.179 | crowd 0.149 | [a12] |
| 2024 | 12-LLM median | 0.20 | humans 0.19 | [a15] |
| 2024 | RTF agent mean-of-3 | 0.170 | Manifold crowd 0.172 | [b27] |
| 2024-25 | Claude 3.5 Sonnet (ForecastBench subset) | 0.122 | supers 0.096, public 0.121 | [a20] |
| 2025 | Sonnet 3.5 to Sonnet 4, pastcasting | 0.1925 to 0.1560 | no human baseline | [a25] |
| 2025 | o3 on 464 Metaculus questions | 0.1352 | crowd 0.149 / 0.121 | [c27] |
| 2025 | RL 14B | 0.190 | o1 0.202; market better by 0.039 | [a24] |
| 2025 | GPT-5 on Kalshi | 0.184 | market 0.187 | [d12] |
| 2025 | AIA Forecaster FB-7-21 | 0.1076 | supers 0.1110, public 0.1451 | [d07] |
| Jul 2026 | Scaffolded systems | not readable | indistinguishable from supers (p 0.14 to 0.41) | [d04] |

The Mandel and Barnes Brier of 0.074 cannot join this table (different horizon, selection and base rate) [a26].

### 6.2 What changed performance, and by how much

- Retrieval plus tuned reasoning: 0.208 to 0.179 (Halawi) [a12]. Removing one component costs only 0.002 to 0.007 [critique].
- Agentic search: 0.1230 to 0.1140 on ForecastBench [d08].
- Sampling and averaging 10 runs: 0.1182 to 0.1140 [d09]. Mixed-model ensemble: 0.194 to 0.197 depending on rule [d05].
- Log-odds stretch: 0.1140 to 0.1076 [d10].
- Outside prior: about 11% Brier reduction [d08].
- Prompt strategies: at best about 0.01 [d01]. Often worse [c19, c28].
- Model generation: GPT-4 to GPT-4o gap 0.026 on ForecastBench [a20]; Sonnet 3.5 to Sonnet 4 -0.0365 in pastcasting (p=0.0024) [c23]. Sonnet 4 vs Sonnet 4 thinking, p=0.53 (no difference) [c23].
- Outcome RL: 0.215 (R1-14B base) to 0.190 (RL ensemble) [a24].
- Brier tracks Arena score (r=-0.68) and log compute (r=-0.67) [a21].

### 6.3 Behaviours

- **Hedging or acquiescence.** Mixed evidence (see 5.2). Reasoning models averaged 41.5% to 44.8% on a 100-question set; one other set showed a 57.35% mean [d02, c07].
- **Under-extremity.** LLMs rarely output extreme probabilities, so they lose when the crowd is certain [a13]. This is the LLM form of Mandel-Barnes underconfidence.
- **Conformity.** A model shown the human median moved by an amount that tracked the gap (r about 0.88) [a17].
- **Leakage.** At least 3.8% of one dataset resolves early; date filters leak; one model's best score was leakage-driven [b24, d11].
- **Verbal probabilities.** LLMs map words to numbers like humans on average (85% or more agreement for GPT-4 class) but shift by 7.0 points with prior belief [d17]. No study scores LLM word forecasts against outcomes [K29].
- **Topic.** Better on politics than economics and finance [c28].
- **As aids.** LLM assistants raise human accuracy 24% to 28% even when noisy; humans did not tell good advice from bad [a18, K16].
- **Against professionals.** Agents trail sell-side analysts on earnings (best models beat consensus on 37.5% of revenue and 32.3% of EPS forecasts) [d13]. They matched the market's Brier on Kalshi and still lost money [d12].

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Schema G4 says "no extremizing votes" for single-answer problems. That rule stays. Forecasting is a different output type (a probability), where the stretch is a calibration step on the pooled number, applied by code. Keep the two apart.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Output numbers at 1% grain, not verbal bands or 5 buckets. For forecast items, code parses a probability and rejects word-only answers. | G (granular probabilities) | [E] | b14, b13, d16, K20, K29 |
| 2 | Do not stack forecasting-strategy prompts or verbal Bayesian-update steps. A plain prompt is the baseline every added step must beat (G7). | G7 / S | [E] | c19, d01, d02, c28, K14, K23 |
| 3 | Compare forecasts by Brier skill against a base-rate forecaster, with AUC and calibration shown separately; never compare raw Brier across question sets. | G (evaluation hygiene) | [E] | a22, a26, b07, K02 |
| 4 | Use only clean tests: live forward-resolving or frozen-retrieval pastcasting; log the date of every retrieved document. | memory / bench | [E] | b24, d11, a25, K18, K27 |
| 5 | When pooling several samples or models, pool in code; do not have the model re-synthesise them. | G5 (code selects) / O | [E] | d09, d05, b27, K05, K12, K24 |
| 6 | Mix an outside prior by a code-side weighted average, not by asking the model to update on it. | S (prior step) / G5 | [E] that averaging beats updating; weights [S] | b20, c03, K12 |
| 7 | When the agent advises a human, label its confidence; humans do not tell good advice from bad. | G | [E] | a18, b21, K16 |
| 8 | Do not read persuasive or confident rationale text as evidence of accuracy. Matches G10. | G10 | [S] here; G10 itself [E] | b15, K17 |
| 9 | For a forecast over exclusive outcomes, normalise to sum to 1 in code (coherentising cut analyst MAE 35%). | G5 | [S] here; G5 [E] | d14 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 10 | Log-odds stretch on the pooled forecast, coefficient fitted on the agent's own resolved questions (start near 1.7). | G (calibration) / O | [S] for LLMs; [E] for humans | b05, d10, d18, K03, K25 |
| 11 | Sample 5 to 10 independent forecasts and pool by median or logit mean; test mixed-prompt vs same-prompt voters at equal tokens. | O (sample and pool) | [S]; diversity [C] | d09, d05, b27, K24 |
| 12 | Base-rate-first and frequency-format paragraphs in the plain prompt. | S1 / S2 | [S] | d01, d02, K23 |
| 13 | Agentic search with stated queries before the first number, only where there is a foothold (G12). | S3 / S4 | [S] | d08, K23 |
| 14 | Selective deferral: when the outside prior is within 0.05 of 0 or 1, use it; otherwise use the model. | S0 / G | [S] | a13, c02, K09 |
| 15 | Wrong-prior robustness: show a prior known to be wrong and measure the harm. | G (prior check) | untested | d08, K26 |
| 16 | Rationale rubric or quick calibration items as a label-free self-check. | G | [S] | d20, d21, K30 |
| 17 | Consistency checks as a no-label proxy (only with a held-out check). | G | [C] | c15, c16, K07 |
| 18 | Negation-pair testing for acquiescence. | G | [C] | c07, d02, K13 |

## 8. Concrete tests on our bench

All arms at equal total tokens, including search and setup cost (G7). Use frozen post-cutoff or pastcasting sets with retrieval dates logged. Minimum 300 resolved binary questions; report Brier, Brier skill, AUC and ECE with bootstrap CIs. Many LLM pairwise gaps are not significant at small N [a25], so power each test.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Binary forecast questions, frozen retrieval | A: plain prompt, 1 sample (extra tokens spent on length). B: 5 samples pooled by median. C: 10 samples pooled by logit mean | Brier | B and C better than A by about 0.004 (0.1182 to 0.1140 in AIA); C vs B within 0.001 [d09] |
| T2 | Same | Pooled forecast with (a) no stretch, (b) fixed 1.7, (c) coefficient fitted on half the agent's own resolved forecasts | Brier and ECE on held-out half | (b) and (c) 0.003 to 0.006 better [d10]; smaller for calibrated models [d12] |
| T3 | Same | Plain prompt vs base-rate-first vs frequency format vs both vs explicit-Bayes prompt | Brier | Base-rate and frequency about -0.004 to -0.014; Bayes about +0.03 worse [d01, d02] |
| T4 | Same | No search vs fixed 3-query search vs agentic search (same token budget) | Brier | Agentic about -0.009 vs none [d08]; fixed search barely helps |
| T5 | Questions with a crowd or market prior | Model alone; model shown prior; code average (weight 0.8 on prior); gated deferral at prior within 0.05 of 0 or 1 | Brier | Average beats shown-prior [b20]; gated deferral recovers the 0.04 loss on near-certain questions [a13] |
| T6 | Same, 20% of priors deliberately wrong (set to 1 minus the true outcome rate for that item) | Model alone vs shown prior vs code average vs gated | Brier on the wrong-prior subset | Unknown; expect shown-prior to degrade most. First test of over-deference |
| T7 | Questions in negated pairs (Q, not-Q) | Plain prompt | p(Q) + p(not-Q) minus 1; mean forecast vs base rate | Tests acquiescence directly; bias expected small for reasoning models [d02] |
| T8 | Same set | Word-first vs number-first output; Kent-scale words mapped by a fixed table | Brier | Number-first no worse; word mapping adds noise [d16, d17] |
| T9 | Held-out resolved items | Rank 100 agent runs by consistency arbitrage score; by rationale rubric; by 9 calibration items | Correlation with Brier on held-out checks | r about 0.2 to 0.5 for the rubric [d20]; consistency uncertain [c16] |
| T10 | Base-rate-stratified set (50% and 5%) | Same arms as T1 | Brier skill vs base-rate forecaster | Shows whether gains come from easy mixes [a22] |
| T11 | Hard vs easy questions | Plain agent | AUC split by difficulty | Human gap 0.966 vs 0.913 [a04]; shows whether the agent mirrors it |

## 9. What does not transfer, and why

- **Mandel and Barnes' accuracy level (Brier 0.074, AUC 0.940).** It reflects a short-horizon, low-variance question mix and organisational review [a05, a06]. It sets no target for an agent on prediction-site questions chosen to be uncertain.
- **Training, teaming, tracking.** Human social interventions. The analogue of teaming (several agents arguing) is excluded by G9; only sampling and pooling carries over.
- **Seniority and experience effects.** No analogue in an agent. Experience gave no calibration gain even in humans [a04].
- **Outcome-based RL and self-play fine-tuning.** Real gains (ECE 0.093 to 0.062) but they are training, not scaffold [a24, b26, d23].
- **The "different information" case for extremizing.** For samples from one model that reason is weak; only the shrinkage reason holds. It also conflicts with G4 for single-answer items. Use only on probability outputs, with a fitted coefficient [a10, d18].
- **Persuasion and rationale style.** Humans judge arguments by style; the agent should not (G10) [b15].
- **Calibration training.** It moved human bias but not monitoring [d22]; an agent has no such monitoring to train.
- **Trading edge.** LLMs matched the market Brier and still lost money [d12].
- **Sell-side analyst comparison.** Earnings only, domain specific [d13].

## 10. Open questions

1. Does a reasoning scaffold beat a plain prompt at equal tokens on forecasting, and which parts help? No equal-token study exists [d01, d08, K23].
2. Is parity with superforecasters real? The July 2026 claim is a non-rejection with 2024 human data and wide CIs; exact 2026 Briers were not readable [d04].
3. Does the stretch (a about 1.7 to 2.3) hold for newer, better-calibrated models? [d10, d12]
4. Is single-model sampling better or worse than a mixed-model crowd at equal tokens? [d09, d05]
5. Does acquiescence persist in reasoning models, and do negation pairs remove it? [d02]
6. How should word forecasts be mapped to numbers? No study scores LLM word forecasts [K29].
7. Has Mandel and Barnes been replicated in another agency or country? Not found [K28].
8. How much of the LLM-vs-crowd gap is date leakage or question selection? [b24, d11]
9. Does an outside prior cause over-deference when it is wrong? [K26]
10. Do consistency checks work as a proxy on held-out checks? [c16, K07]
11. Numbers not opened: Tetlock 2005, Mellers 2015, Grove 2000, Satopaa 2014, Baron 2014 (a27, a28, b13, b28-b30).

## 11. Sources

[V] = opened and read in the research passes; [M] = snippet or second-hand only.

- [V] Mandel and Barnes 2014, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC4121776/
- [V] Tetlock and Mellers 2014, reply. https://pmc.ncbi.nlm.nih.gov/articles/PMC4136586/
- [V] Mandel and Tetlock 2018, Front Psychol. https://pmc.ncbi.nlm.nih.gov/articles/PMC6309046/
- [V, abstract only] Mellers et al. 2014. https://pubmed.ncbi.nlm.nih.gov/24659192/
- [M] Good Judgment Project overview (Wikipedia, secondary). https://en.wikipedia.org/wiki/The_Good_Judgment_Project
- [V] Satopaa and Ungar 2015. https://arxiv.org/abs/1506.06405
- [V] Halawi et al. 2024. https://arxiv.org/abs/2402.18563
- [V] Schoenegger et al. 2024, silicon crowd. https://arxiv.org/abs/2402.19379
- [V] Schoenegger et al. 2024, AI-augmented predictions. https://arxiv.org/abs/2402.07862
- [V] Schoenegger and Park 2023. https://arxiv.org/abs/2310.13014
- [V] Zou et al. 2022, Autocast. https://arxiv.org/abs/2206.15474
- [V] Karger et al. 2025, ForecastBench. https://arxiv.org/abs/2409.19839 ; site https://www.forecastbench.org/ and https://www.forecastbench.org/leaderboards/
- [V] Paleka et al. 2025, pitfalls. https://arxiv.org/abs/2506.00723
- [V] Paleka et al. 2024, consistency checks. https://arxiv.org/abs/2412.18544
- [V] Turtel et al. 2025, outcome-based RL. https://arxiv.org/abs/2505.17989
- [V] Turtel et al. 2025, self-teaching. https://arxiv.org/abs/2502.05253
- [V] Hambly et al. 2025, Bench to the Future. https://arxiv.org/abs/2506.21558
- [V] Hsieh et al. 2024, RTF. https://arxiv.org/abs/2408.12036
- [V] Lu 2025. https://arxiv.org/abs/2507.04562
- [V] Pratt et al. 2024. https://arxiv.org/abs/2406.04446
- [V] Schoenegger et al. 2025, prompt engineering. https://arxiv.org/abs/2506.01578
- [V] Metaculus 2025, AI benchmark results. https://www.metaculus.com/notebooks/38673/q2-ai-benchmark-results/
- [V] Forecasting Research Institute 2026, parity. https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity
- [V] Alur et al. 2025, AIA Forecaster. https://arxiv.org/abs/2511.07678
- [V] Yang et al. 2025, Prophet Arena. https://arxiv.org/abs/2510.17638
- [V] Zeng et al. 2025, FutureX. https://arxiv.org/abs/2508.11987
- [V] Mandel, Karvetski, Dhami 2018, JDM. https://doi.org/10.1017/s1930297500006628
- [V, abstract level] Mandel and Barnes 2018, JBDM. https://doi.org/10.1002/bdm.2055
- [V, abstract level] Mandel and Irwin 2021, JDM. https://doi.org/10.1017/s1930297500008603
- [V] Belem et al. 2024. https://arxiv.org/abs/2407.15814
- [V, abstract only] Baron et al. 2014. https://doi.org/10.1287/deca.2014.0293
- [V, abstract only] Neyman and Roughgarden 2022. https://arxiv.org/abs/2111.03153
- [V] FRI 2026, rationale. https://forecastingresearch.substack.com/p/can-you-judge-a-forecast-by-its-rationale
- [V] FRI 2026, calibration questions. https://forecastingresearch.substack.com/p/can-we-identify-better-and-worse
- [V] Mandel et al. 2024, calibration training. https://doi.org/10.1002/acp.4236
- [V] Chandak et al. 2026, OpenForecaster. https://arxiv.org/abs/2512.25070
- [V] Mandel 2015, information structuring. https://pmc.ncbi.nlm.nih.gov/articles/PMC4389401/
- [V] Dhami et al. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11169332/
- [V] Mellers et al. 2024, human and algorithmic. https://pmc.ncbi.nlm.nih.gov/articles/PMC11373164/
- [V] Friedman et al. 2018. https://academic.oup.com/isq/article/62/2/410/4952224
- [V] Shemesh et al. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC13507494/
- [V] Zhu et al. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8987733/
- [M] Tetlock 2005, Expert Political Judgment. https://press.princeton.edu/books/paperback/9780691128719/expert-political-judgment
- [M] Mellers et al. 2015, superforecasters. https://stafforini.com/works/mellers-2015-identifying-cultivating-superforecasters/
- [M] Grove et al. 2000, via Mellers 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11373164/

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 5 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E02.09-K02** (reworded: the sources support less). Tetlock and Mellers (a06/b07 are the same reply) only argue that the analyst questions were short-range and mostly near-certain (59% under 6 months, over half Brier 0 or 0.01); Mandel and Barnes themselves found time frame had no significant effect on discrimination, so stating it as an established question-mix effect is too strong. Paleka (worked example, Brier not comparable across base rates) is verified. Corrected claim: Tetlock and Mellers (2014) argue that the analysts' strong Brier scores partly reflect an easy question mix: short horizons (59% under 6 months) and many near-certain questions (over half scored Brier 0 or 0.01), whereas Tetlock's weak results were mostly long-range; Mandel and Barnes found no significant effect of time frame on discrimination. Raw Brier is not comparable across question sets with different base rates (Paleka et al. 2025).
- **E02.09-K08** (reworded: the sources support less). Numbers verified (Halawi .179 vs .149 N=914, best baseline .208; Autocast 65% vs 92%, Halawi cites 65.4 vs 92.8; Schoenegger-Park .20 vs .07 N=23, GPT-4 not distinct from .25). But the Halawi 'system' is retrieval-augmented and fine-tuned, and Autocast models are fine-tuned retrieval-based T5/FiD, so they are not 'un-augmented LLM forecasters'; only the .208 baseline and S&P GPT-4 are un-augmented. Corrected claim: LLM forecasters trail the human crowd on real-question sets: Halawi's retrieval-augmented, fine-tuned system scored Brier 0.179 vs crowd 0.149 (N=914 test questions) and its best no-retrieval baseline 0.208; the best Autocast model reached 65% accuracy vs 92% for the crowd; in Schoenegger and Park (2023) GPT-4 scored 0.20 vs crowd 0.07 (N=23 questions, GPT-4 not statistically different from 0.25).
- **E02.09-K23** (reworded: the sources support less). Numbers verified (Schoenegger et al.: best prompts about -0.014 to -0.011, Bayesian Reasoning and Propose-Evaluate-Select significantly worse; Alur et al.: agentic search 0.1140 vs 0.1230 no-news, single forecast 0.1182 vs 10-sample mean 0.1140). But 'only through search, sampling and aggregation' is a universal claim; the sources test prompts and search/aggregation, not other routes, and Halawi's fine-tuning also lowered Brier (.206 to .186). Corrected claim: In the studies read, single-paragraph strategy prompts moved Brier by about 0.01 at best (frequency-based, base-rate-first, chain-of-thought, step-back), Bayesian-reasoning and propose-evaluate-select prompts hurt, and compound prompts gave no robust gain (Schoenegger et al. 2025); the gains from scaffolds came mainly from search (agentic search 0.1140 vs 0.1230 without news), sampling and aggregation (10-sample mean 0.1140 vs single 0.1182; Alur et al. 2025), and fine-tuning in Halawi et al.; no equal-token comparison exists.
- **E02.09-K15** (now single-source: only one opened source, code check).
- **E02.09-K16** (now single-source: only one opened source, code check).
- **E02.09-K20** (now single-source: only one opened source, code check).
