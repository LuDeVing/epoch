# LLM forecasting benchmarks: deep document

*Subfield E03.08. Writer pass over evidence_a-d.jsonl, evidence_x.jsonl, claims.jsonl (K01-K37) and critique.md. Date: 2026-11-01. Brier score: lower is better; 0.25 = always say 50%. Brier Index (BI) = (1 - sqrt(Brier)) x 100; 50 = always 0.5, higher is better.*

## 1. What it is

This subfield asks one question. How well do language models forecast real future events compared with people, and what makes them better?

The field has four layers.

1. **Benchmarks.** Question sets about events with an unknown answer (live) or a hidden answer (frozen past). Examples: Autocast (2022), ForecastBench (2024-), Halawi's test set, Bench to the Future (pastcasting), Prophet Arena, FutureX, Metaculus AI Benchmark.
2. **Human baselines.** The general public, tournament crowds (Metaculus, Good Judgment Open), hired experts and superforecasters. In ForecastBench the superforecaster line is the median of 39 people surveyed once, in July 2024.
3. **Systems.** Bare models, prompted models, retrieval pipelines, ReAct agents, agent ensembles with a supervisor and Platt scaling, and RL-trained small models.
4. **Validity work.** Leakage audits, early-resolution audits, base-rate effects, consistency checks, benchmark version changes.

Headline for our agent. On 2026-07-16 FRI stated that several search-heavy ensembles (Cassi AI, xAI, Google DeepMind) are statistically indistinguishable from the 2024 superforecaster median (x01). That is parity on one benchmark, not outperformance, and it rests on a human baseline more than two years old. The scaffold ingredients that got there are known in shape (agentic search, several runs, a supervisor, Platt scaling, a market price as input). Their token cost is not known (K26).

Why it matters for us. Forecasting is a field where a scaffold-only agent can be scored on truth nobody knew at submission. That removes training leakage by construction. It also has measured hedging and yes-bias, and it lets us test our guardrails (G4 no extremizing votes, G5 code selects, G7 pay for itself) against hard numbers.

## 2. History and theories in depth

**2022: Autocast (Zou et al.) [a11, b15, c27].** First tournament-question benchmark with a dated news corpus. Questions came from Metaculus, Good Judgment Open and CSET. Best ML model: 65% accuracy on true/false against 92% for the human crowd (random 50%). Calibration error: largest FiD Static 40%, human crowd 8%, FiD Temporal 17% when fed crowd predictions. Retrieval helped: relative gains of 93% over UnifiedQA-v2 and 15% over T5. Models were T5/GPT-2 scale. This is the early form of the hedging and overconfidence problem.

**2023: GPT-4 is no better than a coin (Schoenegger and Park) [a12].** GPT-4 entered a 3-month Metaculus tournament (843 participants). On 23 resolved binary questions its Brier was 0.20 (SD 0.18). The human crowd median was 0.07. GPT-4 versus the 0.25 baseline: t(22) = -1.23, p = 0.23. Tiny N, one model.

**2024: three lines open at once.**
- *Wisdom of the silicon crowd (Schoenegger, Tuminauskaite, Park, Tetlock) [a13, a14, b11-b13].* Median of 12 LLMs versus 925 humans on 31 questions: 0.20 versus 0.19. Equivalence passed only at a wide bound (d = 0.5, 0.081 Brier). Strong yes-bias. Study 2: showing the human median to GPT-4 and Claude 2 improved them 17 to 28%, but a plain average of machine and human beat the model's own update.
- *Halawi et al. [a09, a10, b07-b10, c08-c10].* A full pipeline on 914 post-cutoff test questions: Brier 0.179 versus crowd 0.149, best base model 0.208. First strong evidence that a scaffold, not only a bigger model, moves the number.
- *ForecastBench (Karger et al., ICLR 2025) [a01-a08, b01-b06, c01-c07].* 1,000 auto-generated unresolved questions from nine sources. Humans forecast a random 200-question subset. Superforecasters 0.096, public 0.121, best LLM (Claude 3.5 Sonnet, with crowd value) 0.122, p < 0.001 against superforecasters. Without the crowd value the best LLM was 0.136.
- Others. RTF agents with Python simulation reached the crowd on two-week questions (0.170 vs 0.172) [a16, c23]. Pratt et al. found complex human strategies did not help models; a plain prompt looked good only through a No-bias [a15, c26].

**2025: validity crisis, agents, parity claims.**
- Paleka et al. showed backtests leak: at least 3.8% of Halawi questions resolved early; at least 10% of Tao et al. were trivial; date-filtered search returns later pages [a19, b16-b18, c15, c16].
- Paleka et al. also built consistency checks (arbitrage) as an instant proxy for Brier [a20, b19, c17, d17].
- Pastcasting: Bench to the Future with frozen web corpora. Steady model progress (Sonnet 3.5 0.1925 to Sonnet 4 0.1560, p = 0.0024) [a22, b21, c22].
- AIA Forecaster (Alur et al.): agentic search, supervisor, Platt scaling. 0.1076 versus superforecasters 0.1110 on one snapshot [a23, a24, b22-b25, c20, c21, d11].
- Lu: o3 0.1352 on 464 Metaculus questions, but ten hired experts at median 0.0225 (mean 0.1573) [a17, c18].
- RL on resolved markets (Turtel et al.): a 14B model matches o1 (0.190 vs 0.202) but not the market [a21, b20, c19].
- Prophet Arena: markets lag LLMs at long lead times and overtake them near resolution [c24, d21].
- FRI 2025-10-08: gap 0.020, linear parity November 2026 (CI Dec 2025 to Jan 2028) [d05]. The later Brier Index post: gap 0.017, parity March 2027 [d06].

**2026: parity statement and the audit era.**
- FRI 2026-07-16: several systems indistinguishable from superforecasters; first model above supers on market questions; dataset parity since May 2026 [x01, d01].
- Murphy's BLF: paired tests against a price-and-base-rate baseline. The baseline scores BI 69.9; BLF 73.3. Most of the market-question edge is the supplied price [d07, d09].
- BTF-2 (Liptay et al.): 1,417 questions, 15 million documents, detects 0.004 Brier. Best pipeline 0.119 at 1.68 USD per question; single Opus 4.6 0.130 [d13, d14, d15].
- Diversity across models beat resampling one model at equal sample count (Aitchison et al.), N = 113 [b26, d16].
- Leakage audits: 1.5% (BLF) and 1.65% (AIA) of search results leak; 52% gap when models only pretend to forget; over 40% of generated questions leaked [d10, d12, d18, d20].
- ForecastBench changed repeatedly (difficulty adjustment, combos dropped, Brier Index, horizons cut), so trends mix tests [d03].

**Theories of why models forecast badly or well.**
1. *Hedging and bias.* RLHF-tuned models hug 50% and lean to "yes". Platt/extremizing and base-rate checks target this [b12, b08, b25].
2. *Information, not reasoning.* Gains come from good evidence (agentic search) and a strong prior (market price). Clever prompting adds little [c13, c14, a24].
3. *Aggregation.* Several runs average away noise, but only when runs differ. Model diversity may beat sample count [c23, d16].
4. *Difficulty confound.* Question difficulty explains 62% of score variance in BLF's test [d07]. Brier mixes skill with base rate [b18].

## 3. Core findings with exact numbers

Status: established = two or more independent sources or audited measure; single = one source; contested = sources disagree. K-ids refer to claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Early ML far below human crowd | 65% vs 92% accuracy; calibration error 40% vs 8% | Zou 2022 [a11, b15, c27] | single (K01) |
| GPT-4 no better than 50% (2023) | Brier 0.20 vs crowd 0.07; N = 23; p = 0.23 vs baseline | Schoenegger and Park [a12] | single, small N |
| Base GPT-4-class models near no skill | 0.208 best base model vs crowd 0.149, random 0.25 | Halawi [a09, c08] | established (K02) |
| ForecastBench headline gap | Supers 0.096; public 0.121; best LLM 0.122; p < 0.001 vs supers | Karger [a03, b01, c02] | established (K07) |
| Crowd value is part of LLM edge | Best LLM 0.136 without crowd forecast vs 0.122 with | Karger [b02] | established (K08) |
| News did not help in ForecastBench | Claude 3.5 Sonnet scratchpad + crowd 0.128 vs + news 0.132 | Karger [b03, c04] | original result; contradicted by AIA (section 5) |
| Combo questions widen gap | Supers 0.076, public 0.096, GPT-4o 0.130; gap 0.054 vs 0.026 GPT-4o to GPT-4 | Karger [a05, b04, c03] | established (K10); human combos assume independence |
| Gap varies by slice | Econ and Business (N = 181) LLM 0.126 vs supers 0.141; 30-day (N = 112) 0.151 vs 0.172; 7-day (N = 106) 0.093 vs 0.076 | Karger [a06] | single (K11) |
| Original parity projection | Arena 1406 (CI 1346-1633), R2 0.47; compute 6.49e26 FLOP (CI 9.69e25-8.65e28), R2 0.41, p = 0.046 | Karger [a07, b05, c05] | established but loose (K09) |
| Later parity projections | Gap 0.020, parity Nov 2026 (CI Dec 2025-Jan 2028), slope 0.016/yr; later gap 0.017, parity Mar 2027 | FRI posts [d05, d06] | established as FRI statements (K25) |
| The 0.017 gap | 0.103 best LLMs vs 0.086 supers; BI 67.9 vs 70.6 | FRI Brier Index post [d06] | established (K25) |
| Parity reached | One-sided bootstrap p vs supers: Cassi 0.41, xAI 0.15-0.16, DeepMind 0.14; 17 preliminary submissions above supers | FRI 2026-07-16 [x01, d01] | single (K24) |
| Parity is close, not a win | Cassi board: supers rank 1 (BI 69.2), Cassi rank 2 (68.8; Brier 0.097) | Cassi page [d04] | single, vendor |
| Retrieval pipeline vs crowd | System 0.179, crowd 0.149, system + crowd 0.146; accuracy 71.5% vs 77.0%; N = 914 | Halawi [a09, b07] | single (K03) |
| Halawi ablation | No fine-tuning and no retrieval 0.206; one component removed 0.186 | Halawi [c09, b10] | single |
| Edge only where crowd unsure | Crowd in 0.3-0.7: system 0.199 vs crowd 0.246; all three favourable conditions: 0.240 vs 0.247 | Halawi [b08, c10] | single (K04) |
| LLM crowd matches human crowd | 12 LLMs 0.20 vs 925 humans 0.19; N = 31; equivalence at d = 0.5 | Schoenegger [a13, c11] | single (K05) |
| Yes-bias | Mean forecast 57.35, median 60; only 14 of 31 resolved yes | Schoenegger [b12] | single (K05) |
| Human median as input | GPT-4 0.17 to 0.14; Claude 2 0.22 to 0.15; plain average 0.13 and 0.14 | Schoenegger [a14, c12] | single (K06) |
| Agent ensemble reaches crowd | RTF mean of 3 0.170 vs crowd 0.172; single 0.180; base GPT-4o 0.210 | Hsieh [a16, c23] | single (K16) |
| Ensembling helps agents, not base LMs | Agents 0.169 vs 0.180; base 0.218 vs 0.210 | Hsieh [a16] | single |
| Agentic ensemble vs supers | FB-7-21 AIA 0.1076 vs supers 0.1110 vs public 0.1451 vs o3 0.133; FB-Market 0.0753 vs 0.0740 | Alur [a23, b22, c20] | single (K12) |
| AIA loses on liquid markets | MarketLiquid AIA 0.1258 vs market 0.1106; AIA + market beats market | Alur [a23] | single |
| Search ablation | None 0.1230; agentic A 0.1140; non-agentic A 0.11738; agentic B 0.11824; non-agentic B 0.12168 | Alur [a24, b23] | single (K13) |
| Ensemble size | One forecast 0.1182; mean of 10 0.1140; median 0.1138; trimmed 0.1142 | Alur [d11] | single |
| Supervisor | Agentic 0.1125; non-agentic 0.1168; pick-best-of-k 0.1191; none 0.1199 | Alur [d11, c21] | single |
| Platt scaling | 0.1119 to 0.1076 (in-set); 0.1125 to 0.1104 when fitted on another set | Alur [c21, d11] | single (K13, K33) |
| Price plus search | Price alone 0.096; agentic search 0.085; both 0.075 | Alur [a24, b24] | single (K14, K29) |
| Price baseline is hard to beat | Market BI: price 81.5, BLF 83.8, Cassi 82.0, Grok 79.5; dataset prior 58.3, BLF 62.7; overall 69.9 vs 73.3 | Murphy [d07] | single (K29) |
| Belief state is backbone-dependent | +3.00 BI (Pro), +1.99 (Flash), -0.42 n.s. (GPT-5.4) | Murphy [d09] | single (K28) |
| Pastcasting progress | Sonnet 3.5 0.1925; 3.7 0.1712; 4 0.1560; Gemini 2.5 Pro 0.1611; effective n 178.8 | FutureSearch [a22, b21] | established (K17) |
| Thinking mode no clear gain | Sonnet 4 0.1560 vs 4 thinking 0.1597, p = 0.53 | FutureSearch [b21] | single |
| 2026 frontier agents, frozen corpus | Opus 4.6 0.131, Gemini 3.1 Pro 0.143, GPT-5.4 0.151, Grok 4.20 0.165 | Liptay [d13] | single |
| Pipeline vs single agent | SOTA pipeline 0.119 (1.68 USD) vs Opus 0.130 (0.55 USD); mean of 4 agents 0.125 | Liptay [d14] | single |
| Experts vs o3 | o3 0.1352; experts mean 0.1573, median 0.0225 (157 questions) | Lu [a17, c18] | single (K18) |
| Prompt effects small | Frequency-based -0.014; base-rate-first -0.011; Bayesian +0.030; propose-evaluate-select +0.033; 38 prompts, 4 models, 100 questions | Schoenegger 2025 [c13, c14] | established (K19) |
| Complex strategies do not help | Basic 0.1955 vs Base Rates 0.2540, Breakdown 0.2053, Human 0.1746 | Pratt [c26] | single |
| Outcome RL | ReMax 0.190 (ECE 0.062); o1 0.202 (ECE 0.093); market better by 0.039-0.051 | Turtel [a21, c19] | established (K15); training out of scope |
| Diversity beats resampling | N = 113; 101 allocations; best mix (0.56, 0.26, 0.18) | Aitchison [b26, d16] | provisional (K22) |
| Consistency vs Brier | Up to 0.92 conditional; negation +0.60 on one set, -0.36 on another | Paleka [a20, d17] | contested (K21) |
| Leakage rates | 3.8% early resolved; 1.5% and 1.65% leaking search results; 52% simulated-ignorance gap; 40% generated questions | Paleka, Murphy, Alur, Li, Chandak [d10, d12, d18, d20] | established (K20, K30) |
| Horizon | Markets lag LLMs far out, overtake near resolution (2025 models) | Prophet Arena [c24, d21] | single (K35) |
| Compute scale | 80k-250k tokens and 0.14-1.7 USD per question; Metaculus bots 0.10-3 USD | BLF, BTF-2, Metaculus [d08, d14, d22] | established (K27) |
| Benchmark version churn | Difficulty adjustment 2025-10-07; combos dropped 2025-10-17; Brier Index 2026-03-04; horizons 8 to 5 on 2026-09-30 | FRI changelog [d03] | established (K37) |

## 4. Mechanisms and models

Each mechanism is written as steps an engineer can code.

**4.1 Brier score and Brier Index.**
- Brier = mean over questions of (p - outcome)^2. Perfect 0, coin flip 0.25.
- BI = (1 - sqrt(Brier)) x 100. Coin flip = 50. Superforecasters 0.086 = 70.6. Best LLMs 0.103 = 67.9 [d06].
- ForecastBench ranks by difficulty-adjusted Brier (two-way fixed effects), equal-weight mean of dataset and market scores [d03]. Raw Brier from the 2024 paper is not on this scale [a08, a25].
- Rule. Pair-compare on the same questions. Report per base-rate stratum [b18]. Report mean and median [a17].

**4.2 The retrieval-and-ensemble pipeline (Halawi, AIA, Cassi, BLF share its shape).**
1. Generate sub-questions and search queries from the question.
2. Retrieve. Agentic search = iterative: read results, form the next query. Single-shot is non-agentic.
3. Filter results for relevance and recency. Drop post-cutoff (leaky) results with a classifier plus date clamps.
4. Run k independent forecasts (k about 5 to 10; returns diminish after a handful [d11]). Each writes a reason and a probability.
5. Aggregate in code: mean, trimmed mean or median (within 0.0004 in AIA [d11]). Geometric mean of log odds was slightly best in Karger's appendix (0.194 vs 0.197) [a04, c06].
6. Optional supervisor: an agent reads the k forecasts and the evidence and reconciles. Agentic supervisor 0.1125 vs none 0.1199. Pick-best-of-k 0.1191 gave no gain over none [d11].
7. Post-hoc calibration: Platt scaling on the mean (logistic regression on the logit of the mean forecast, fitted on resolved questions). The sqrt(3) log-odds coefficient is a fixed alternative [b25, d11, K33].
8. Blend with an outside prior if one exists (market price, crowd value), arithmetic or log-odds average, in code [a14, c12].

**4.3 Market-price anchoring.**
- Put the price in the prompt, or blend afterwards in code. Blending in code beat letting the model update (GPT-4 0.13 vs 0.14; Claude 2 0.14 vs 0.15) [c12].
- AIA: price alone 0.096, agentic search alone 0.085, both 0.075 [a24]. Murphy: price-only baseline is hard to beat; the best agent adds +2.3 BI, not significant on 200 events [d07].
- Implement three arms always: price only, agent without price, agent with price (or average).

**4.4 Platt/extremizing as a calibration step.**
- Fit a and b in p_final = sigmoid(a x logit(p_mean) + b) on resolved questions. a above 1 pushes to the extremes.
- Held-out check: fit on set A, score on set B. It keeps about 60% of the in-set gain [d11, K33]. The gain shrinks with a market anchor. Murphy: +0.72 to +1.48 BI, but not resolved for one backbone [d09].
- This differs from G4's ban on extremizing votes. Platt acts on one pooled probability, is fitted on held-out data, and corrects known RLHF hedging. It still has to pass a held-out test before we use it.

**4.5 Consistency (arbitrage) checks.**
- Negation: P(A) + P(not A) should be 1. Violation = |sum - 1|.
- Conditional chain: P(A and B) = P(A) x P(B|A). Violation = the gap.
- Arbitrage profit is the loss a trader could force. It correlates with later Brier up to R = 0.92 (conditional check) [a20, d17]. Negation is +0.60 on one set and -0.36 on another. Patching forecasts to pass trained checks did not generalise to held-out checks or to Brier [d17, K32]. Nobody tested it as a sample selector for one question. Use as audit only.

**4.6 Pastcasting with a frozen corpus.**
- Resolved questions, a corpus frozen at question time (tens of thousands to 15 million documents). Retrieval sees only documents dated before the question date [d13, a22].
- BTF-2: 1,417 questions detect Brier differences of 0.004. Effective question count is below nominal (178.8 of 299 in BTF-1) because questions correlate [a22].
- Weak spot: live-versus-frozen fidelity was checked on 20 questions, by eye [d19, K31]. Validate by rank correlation with a live submission.

**4.7 Leak defence stack (BLF).**
1. Date-filtered search. 2. LLM leak classifier on each result. 3. Clamp tool dates. 4. Block known URLs. Result: classifier recall 93.8% (320 of 341 leaks), 29.9% false positives; 21 of 1,377 results the agent saw leaked (1.5%) [d10]. AIA's judge: precision 20%, recall 64% (derived from 16/81 and 16/25) [d12].
- Telling a model to "forget" after a cutoff leaves a 52% performance gap to true ignorance [d20]. Use models whose cutoff precedes the question date.

**4.8 Belief state (BLF).** Carry a (probability, evidence summary) pair across search steps. +3.00 BI on Gemini 3.1 Pro, +1.99 on Flash, -0.42 (n.s.) on GPT-5.4 [d09]. Backbone dependent.

**4.9 Diversity-weighted ensemble.** Choose the allocation over models to maximise expected score. Diversity measured by pairwise Jensen-Shannon divergence of forecast distributions [d16]. Best three-model mix (0.56, 0.26, 0.18). Chosen on the test set, no CIs. Not tested at equal tokens.

**4.10 Horizon and lead time.** Markets improve as resolution nears. Raw Brier across horizons mixes skill with difficulty [d21, b18]. Score against a market baseline by lead-time bin.

## 5. What holds up

**Replications (agreeing).**
- Reasoning-only prompts barely move a model. Information (retrieval, a prior) does. Halawi's ablation (0.206 when both parts removed, back to baseline), AIA's search ablation (0.1230 to 0.1140) and RTF's tool use point the same way [c09, c21, a16].
- Averaging with an outside prior beats model self-update: Schoenegger (c12) and Halawi's system + crowd 0.146 [a09]. Two papers, different models.
- Agent ensembles reach crowd level on different sets: RTF (0.170 vs 0.172); Halawi pipeline near but behind (0.179 vs 0.149).
- Frontier progress is steady: FutureSearch Sonnet 3.5 to 4 (p = 0.0024); BTF-2 Opus 4.6 over Grok 4.20 (differences 0.012 to 0.033, significant) [b21, d13].
- Hedging toward 50 and yes-bias: Schoenegger (57% mean forecast, 14 of 31 yes), Halawi (system rarely outputs low probabilities), AIA (RLHF hedging fixed by Platt) [b12, b08, a24]. Pratt sees the opposite surface effect, a No-bias [c26]. The flaw is miscalibration, and its sign depends on the set.

**Failed or contradicted results.**
- *News retrieval.* Karger: no gain (0.128 vs 0.132). AIA and Halawi: retrieval helps a lot. Likely cause: a simple news summariser versus iterative agentic search. AIA shows weak search equals no search (0.12168 vs 0.1230) [b03, b23]. Karkar and Chopra: raw news helped finance and sports and hurt politics and geopolitics (392 questions; rumour over-weighting, definition drift, recency bias) [d24].
- *Halawi's edge is narrow.* 0.199 vs 0.246 when the crowd is uncertain, but 0.240 vs 0.247 under all favourable conditions [c10]. The criteria were chosen post hoc.
- *Superforecaster-written prompts.* Did not beat the plain scratchpad (0.150, 0.153 vs 0.147) [c07]. One was significantly worse (mean forecast 50%) [c14].
- *Prompt engineering broadly.* 38 prompts; almost none beat the control after correction [c13]. Bayesian prompts hurt (+0.030).
- *Human forecasting strategies for LLMs.* Pratt: Base Rates prompt 0.2540, worse than Basic 0.1955 [c26].
- *Thinking mode.* No clear gain on pastcasting (p = 0.53) [b21]. Reasoning-optimised models also showed worse fidelity at simulated ignorance [d20].
- *Persona/prompt-diverse ensembles.* 3 models x 3 superforecaster prompts reached 0.194-0.197 against 0.178 for the best single (different table); aggregation formula changed it by 0.003 [a04]. Fits G4 and G9.
- *Consistency as a training target.* Passed trained checks, not held-out ones [d17].
- *Linear parity extrapolation.* R2 0.41-0.47 [a07]. Lu's fit: before May 2027 [a18]. FRI: Nov 2026, then Mar 2027. The actual parity statement came in July 2026 on a different test [x01]. Parity dates are not a planning number.
- *LLM-only crowd claim.* 31 questions, low power; the Bench to the Future team says so [a13, a22].
- *Belief state, supervisor, LLM aggregator.* Backbone dependent. An AIA-style LLM aggregator was worse than a plain mean in Murphy's test [d09, K28].

**Moderators and boundary conditions.**
- *Crowd uncertainty.* LLM edge appears only when the crowd sits at 0.3-0.7.
- *Question type.* Market questions: price dominates. Dataset questions: the base rate is a strong prior (BI 58.3; BLF 62.7) [d07]. Combo questions: wide gap. Liquid markets: market wins [a23].
- *Category.* Finance and sports vs politics for raw news [d24]. Economics and Business favoured the LLM in 2024 [a06].
- *Horizon.* 7-day: supers ahead (0.076 vs 0.093). 30- and 90-day: LLM ahead [a06]. Prophet Arena: markets lag LLMs far out, then overtake [d21].
- *Backbone.* Belief state helps two backbones, not a third. Prompt guidance helped Gemini 3.1 Pro (0.141 to 0.129) and not an Opus 4.6 agent (0.131 both). Giving others' research hurt the Opus agent (0.131 to 0.153) [d09, d15].
- *Mean vs median.* Experts: mean 0.157, median 0.0225 [a17]. Per-event median beats mean for supers (0.1110 vs 0.1123) and public (0.1450 vs 0.1586) [a24].
- *Question set.* Public median Brier: 0.121 (paper subset), 0.1451 (FB-7-21), 0.1510 (FB-8-14) [a25]. Absolute Brier is not comparable across papers.
- *Difficulty.* Explains 62% of score variance [d07].

**Interventions that worked (size).** Agentic search -0.0090 vs no search (0.1230 to 0.1140). Mean of 10 -0.0042. Agentic supervisor -0.0074. Platt -0.0043 in-set. Market price -0.013 (0.116 to 0.103). Blend with human median beats model update by about 0.01. Diverse model mix (in-sample). Model upgrade -0.036 (Sonnet 3.5 to 4). RL -0.012 vs o1.
**Interventions that did not:** news summaries alone, Bayesian/propose-evaluate prompts, superforecaster-written prompts, thinking mode, consistency patching, pick-best-of-k supervisor, shrinkage tuning in BLF (collapsed to plain logit averaging).

**Caveats the whole field shares.**
- Superforecaster line: 39 people, 9 days, shared rationales midway, surveyed July 2024 [a02]. All 2026 parity claims extrapolate from it. Cassi's own board still ranks supers first [d04].
- Parity is not outperformance. Several parity-reaching systems have unpublished methods (K26).
- Single-source headline results: AIA, Turtel, FutureSearch, Prophet Arena, OpenForecaster, BLF.

## 6. Language models

**Bare models.** 2023 GPT-4: 0.20, about a coin. 2024 base GPT-4-class: 0.20-0.21 on crowd questions. Claude 3.5 Sonnet best at 0.122-0.136 depending on crowd value. o3 (2025): 0.1352 on 464 Metaculus questions, better than the Halawi crowd (0.149), worse than the ForecastBench public (0.121), far behind hired experts [a17]. BTF-2 frozen-corpus agents in 2026: Opus 4.6 0.131, Gemini 3.1 Pro 0.143, GPT-5.4 0.151, Grok 4.20 0.165 [d13].

**Progress rate.**
- BI rose 2.4 points from Claude 3.5 Sonnet (Oct 2024) to Grok 4.20 Preview (Oct 2025) [d06].
- Market-question slope 0.015 Brier per year (tournament) or 0.036 per year (baseline without crowd or tools) [d05].
- Pastcasting: 0.036 Brier between Sonnet 3.5 original and Sonnet 4 [b21]. Gemini 3.1 Pro vs 3.0 Pro on the same research: 0.129 vs 0.138 (CI 0.002-0.016) [d13].
- A Metaculus estimate quoted by IBM says agentic search, history simulation and several-model consensus together equal about nine months of base-model progress. The report was not found; treat as a pointer only [d23].

**What changed behaviour, by size.**
1. Model upgrade: the largest single effect (0.036 across two Sonnet generations).
2. Strong outside prior (market price): about 0.013, and it may dominate on market questions.
3. Evidence via agentic search: about 0.009.
4. Supervisor: about 0.007 (agentic only).
5. Averaging runs: about 0.004; more when runs differ (RTF agents 0.169 vs 0.180; base LMs show none).
6. Platt scaling: about 0.004 in-set; about 60% of that held-out.
7. Prompts: -0.014 to +0.033, mostly noise after correction.

**Failure modes.**
- Hedging toward 50 and yes-bias [b12, b08]; Pratt's No-bias in a rare-yes set [c26].
- Copying the crowd or market: GPT-4.5 correlated 0.994 with the market [d07, K29]. Skill and copying are hard to separate.
- Over-strict base-rate extrapolation (human review in BTF-2) [d15].
- Wrong event recall and misread data sources (Prophet Arena); fake web pages and temporal validity (FutureX) [c24, c28].
- Rumour over-weighting, definition drift, recency bias from raw news [d24].
- Poor on joint (combination) events [a05].
- Parametric leakage for models with cutoffs after the question date; "forget" instructions fail [d20, d12].
- Sample sameness: two Opus runs were identical in BTF-2 [d14]. This supports G4.

**Compute.** 80k-200k tokens and 0.14-0.55 USD per frontier ReAct question; best BTF-2 pipeline 1.68 USD; BLF 50-100M tokens for 5 trials x 400 instances (about 125k-250k tokens per question, derived; about 0.6 USD); Metaculus bots 0.10-3 USD [d08, d14, d22]. No public paper compares components at equal tokens (K28).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Score on unresolved questions or a frozen corpus only, and log each forecast for later scoring.** Part: S9, G7. [E] K20, K30. Evidence a01, a19, b16-b18, c15, c16, d10, d12, d18, d20. Use no model whose cutoff follows the question date; never trust date filters alone; audit for early resolution.
2. **Report against baselines every time: price only (or base rate only), no scaffold, and the scaffold.** Part: G7. [E] K29, K02. Evidence d07, a24, b02, a03. A pasted price is not reasoning.
3. **Pair-compare on the same questions; report per-stratum scores, mean and median; pin the benchmark version.** Part: G7, memory. [E] K37. Evidence a25, b18, a17, d03.
4. **Combine with an outside prior by averaging in code, not by asking the model to update.** Part: G5. [E] in direction (two sources). Evidence a09, a14, c12, b09. The full size effect is single-source.
5. **Search iteratively when evidence is needed; weak search equals none.** Part: S3 (grounding), G12. [E] in direction (AIA, Halawi, RTF); size single-source (K13). Evidence a24, b23, c09, a16. Raw news can hurt by category [d24].
6. **Do not rely on prompting tricks or personas.** Superforecaster-written and Bayesian prompts did not help. Part: section 4b. [E] K19. Evidence c13, c14, c07, c26.
7. **Guard against hedging and yes-bias with a base-rate check in code.** Part: S0 and S4 guard, G5. [E] in direction. Evidence b12, b08, c26.
8. **Log tokens, tool calls and USD per question.** Part: G7. [E] K26, K27. Evidence d08, d14, d22.

### Test first (see UNKNOWNS.md)

- **Base rate first with a disruption check.** Part: G (calibration). [C] K19 vs K36: -0.011 on 2024 models, mixed on 2026. Evidence c13, d15, d24. U1.
- **Mean of N diverse runs vs one run at equal tokens.** Part: S3, S7. [S] K12, K16, K28. Evidence d11, a16, c23. U2.
- **Model diversity vs resampling the best model.** Part: S3. [S] K22, K34. Evidence b26, d16. U3.
- **Post-hoc Platt on the pooled forecast, fitted on held-out data.** New calibrate step; G4 stays. [S] K13, K33. Evidence b25, d11, d09. U4.
- **Agentic supervisor over k forecasts.** Part: S7. [S] K28. Evidence d11, c21, d09. An LLM aggregator was worse than the mean in Murphy; G5 requires blind judges. U5.
- **Structured belief state across search steps.** Part: S2, S3. [S] K28. Evidence d09. U6.
- **Consistency checks: audit, then selector.** Part: G5. [C] K21, K32. Evidence a20, d17. U7.
- **Sub-question decomposition.** Part: O3. [S] K28, confounded. Evidence d14. U8.
- **Price anchor in prompt vs blend after.** Part: G5. [S] K14, K29. Evidence a24, d07. U9.
- **Gate search effort on prior uncertainty.** Part: G12. [S] K04. Evidence b08, c10. U10.
- **Lead-time awareness.** Part: S0. [S] K35. Evidence c24, d21. U11.
- **Frozen-corpus score predicts live score.** Test infrastructure. [S] K31. Evidence d13, d19. U12.

## 8. Concrete tests on our bench

All arms get equal total tokens per question. Cap at about 0.5 to 2 USD per question so numbers compare with the field (K27). Items: resolved binary questions inside a frozen corpus, cutoff-filtered models, at least 600 questions (BTF-2 detected 0.004 at 1,417; effective n is lower than nominal), plus a smaller live ForecastBench batch.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Binary forecasts, mixed base rates | A: plain model with scratchpad. B: base-rate-first with disruption check. C: Bayesian-reasoning prompt (control) | Brier, paired, per base-rate stratum | B better than A by about 0.01; C worse by about 0.03 (2024 sizes; may vanish on 2026 agents) |
| T2 | Same set | A: 1 long run. B: mean of 5 short runs. C: median of 5 | Brier, paired bootstrap | B and C better than A by about 0.004; B equals C |
| T3 | Same set | A: N samples of best model. B: N/3 each of three families | Brier with CIs; Jensen-Shannon diversity | B better by 0.003 to 0.01 if the in-sample result is real |
| T4 | Same set, half for fitting | A: no calibration. B: Platt fitted on set 1, scored on set 2. C: fixed sqrt(3) log-odds | Brier, ECE on held-out and market-anchored mixes | B better by about 0.003; C close; gain smaller with a price |
| T5 | Market-style questions with a price | A: price only. B: agent without price. C: agent with price in prompt. D: average of A and B in code | BI, paired against A | D and C better than A by 1 to 3 BI points; B worse than A. A tie with A means the scaffold adds nothing to the price |
| T6 | Same set | A: mean of N. B: mean of N plus blind agentic supervisor. C: pick-best-of-k | Brier | B better by about 0.007; C no better than A |
| T7 | Same set | A: no search. B: single-shot search. C: agentic search | Brier by category | C better than A by about 0.009; B near A |
| T8 | Linked pairs (A, not A, A and B) | A: ignore. B: audit only. C: pick the sample with least violation | Correlation of violation with Brier; Brier of C vs A | B: positive on conditional checks, unstable on negation. C: unknown, probably small |
| T9 | Conjunction/disjunction questions | A: model gives the joint directly. B: model gives parts, code composes with a conditional | Brier on combos | B better than A (the human-model gap was 0.054) |
| T10 | Split by prior in 0.3-0.7 vs outside | A: uniform effort. B: more search when near 0.5 | Brier per bin | Gain in the uncertain bin, none in confident bins |
| T11 | Lead times 0-3 h, 1 day, 1 week, 1 month | Agent vs market baseline | Brier per lead-time bin | Agent competitive far out, market wins near resolution |
| T12 | 100 live ForecastBench questions plus the frozen set | Same arms on both | Rank correlation of arms across the two | Rho above 0.7 means frozen tests can be trusted |

For every test report mean and median, paired-bootstrap CI, base-rate and category strata, tokens and USD per question, and leak audit rate.

## 9. What does not transfer, and why

- **Fine-tuning and RL on forecasts (Halawi, Turtel, OpenForecaster).** Our agent does not train. We keep the idea (calibration is learnable; select against a reference) but only as an in-session check, not as weights. K15.
- **The 2024 superforecaster median as a target.** 39 people, 9 days, shared rationales, July 2024 [a02]. It is a fixed, partly deliberated line. Tying it says little about forecasting skill in general.
- **Brier numbers across papers.** Different sets, base rates, horizons, difficulty adjustment [a25, b18, d03]. Only paired comparisons transfer.
- **Parity dates.** Linear fits on 16 to 17 models, R2 0.4-0.5 [a07]. Overtaken in July 2026.
- **Market-question gains.** Most of the edge is the supplied price [d07]. A reasoner without a price may see none of it.
- **Dataset questions (templated series).** A base rate is already a strong prior; gains are small (+4.4 BI for BLF) [d07]. Not a model of open-ended judgment.
- **Human forecasting strategies (Pratt).** Complex frameworks did not help models. Do not import human checklists without a test.
- **Persona or debate ensembles.** Not supported here either; matches G9 and G4.
- **Consistency patches as a target.** Did not generalise [d17].
- **Extremizing votes.** Platt on a pooled forecast is a different operation from G4's banned extremizing of votes. Do not conflate them.
- **Tournament-bot effort.** 5 of 9 top Metaculus bots spent at least two full-time weeks [d22]. Outside our token-only budget.

## 10. Open questions

1. What do Cassi, xAI, DeepMind and Torchcast actually do, and at what token cost? (K26: no public data.)
2. Which pipeline component gives the gain at matched tokens? (K28: none isolated.)
3. Does parity hold on fresh questions against a new superforecaster round? None found as of 2026-11-01.
4. How much of the market-question edge is price copying versus reasoning beyond +2.3 BI? (K29.)
5. Are 2025-26 backtest claims inflated by leaks? Live results are not; backtest leaks are 1.5-1.65% of search results; the effect on forecasts is unmeasured (K30).
6. Do base-rate-first and frequency framing survive on 2026 agents? One mixed data point (K36).
7. Does consistency choose among samples for one question? Untested (K32).
8. Does Platt transfer across models with different hedging, and to market-anchored mixes? (K33.)
9. Model diversity vs more samples at equal tokens? (K34.)
10. Does LLM accuracy decay with horizon relative to markets in 2026 models? (K35.)
11. Does a frozen-corpus score predict a live ForecastBench rank? Only a 20-question visual check exists (K31).
12. The Metaculus "Pros Beat Bots" and nine-months-of-progress reports were not found; is the IBM paraphrase right? [d22, d23]

## 11. Sources

[V] = opened this session by the research agents (evidence lines opened:true). [M] = snippet or secondhand only. FRI and Cassi pages were read through a summarising fetch tool; result tables were images.

- [V] Karger et al. (2025) ForecastBench, ICLR. https://arxiv.org/abs/2409.19839 (a01-a07, b01-b06, c01-c07; numbers re-verified from the PDF by the cross-checker)
- [V] ForecastBench leaderboard site. https://www.forecastbench.org/leaderboards/ and https://www.forecastbench.org/ (a08, b28, c29; tables not in fetched text)
- [V] ForecastBench wiki, how to submit and FAQ. https://github.com/forecastingresearch/forecastbench/wiki/How-to-submit-to-ForecastBench (d02)
- [V] ForecastBench wiki changelog. https://github.com/forecastingresearch/forecastbench/wiki/Changelog (d03)
- [V] FRI (2026-07-16) AI models have likely reached parity with superforecasters. https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity (x01, d01)
- [V] FRI (2025-10-08) How well can large language models predict the future? https://forecastingresearch.substack.com/p/ai-llm-forecasting-model-forecastbench-benchmark (d05)
- [V] FRI (2026) Introducing the Brier Index. https://forecastingresearch.substack.com/p/introducing-the-brier-index (d06)
- [V] Cassi AI benchmarks page (vendor). https://www.cassi-ai.com/benchmarks/ (d04)
- [V] Halawi, Zhang, Yueh-Han, Steinhardt (2024) Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563 (a09, a10, b07-b10, c08-c10)
- [V] Zou et al. (2022) Autocast. https://arxiv.org/abs/2206.15474 (a11, b15, c27)
- [V] Schoenegger and Park (2023) LLM prediction capabilities. https://arxiv.org/abs/2310.13014 (a12)
- [V] Schoenegger, Tuminauskaite, Park, Tetlock (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379 (a13, a14, b11-b13, c11, c12)
- [V] Schoenegger et al. (2024) AI-augmented predictions. https://arxiv.org/abs/2402.07862 (b14)
- [V] Schoenegger, Jones, Tetlock, Mellers (2025) Prompt engineering LLMs for forecasting. https://arxiv.org/abs/2506.01578 (c13, c14)
- [V] Pratt et al. (2024) Can language models use forecasting strategies? https://arxiv.org/abs/2406.04446 (a15, c26; critique says some details were snippet-level)
- [V] Hsieh, Fu, Chen (2024) Reasoning and tools for forecasting. https://arxiv.org/abs/2408.12036 (a16, c23)
- [V] Lu (2025) Evaluating LLMs on real-world forecasting against expert forecasters. https://arxiv.org/abs/2507.04562 (a17, a18, c18)
- [V] Paleka, Goel, Geiping, Tramer (2025) Pitfalls in evaluating language model forecasters. https://arxiv.org/abs/2506.00723 (a19, b16-b18, c15, c16)
- [V] Paleka et al. (2024/25) Consistency checks for language model forecasters. https://arxiv.org/abs/2412.18544 (a20, b19, c17, d17)
- [V] Turtel, Franklin, Skotheim, Hewitt, Schoenegger (2025) Outcome-based RL to predict the future. https://arxiv.org/abs/2505.17989 (a21, b20, c19)
- [V] FutureSearch, Wildman et al. (2025) Bench to the Future. https://arxiv.org/abs/2506.21558 (a22, b21, c22, d19)
- [V] Alur et al. (2025) AIA Forecaster technical report. https://arxiv.org/abs/2511.07678 (a23-a25, b22-b25, c20, c21, d11, d12)
- [V] Aitchison, Jeen, Shevlane, Day (2026) Diversity is the strength of the AI crowd. https://arxiv.org/abs/2606.29661 (b26, d16)
- [V] Lee et al. (2025) Advancing event forecasting through massive training of LLMs. https://arxiv.org/abs/2507.19477 (b27)
- [V] Yang et al. (2025) LLM-as-a-Prophet: Prophet Arena. https://arxiv.org/abs/2510.17638 (c24, d21; figure values not readable)
- [V] Chandak, Goel, Prabhu, Hardt, Geiping (2026) Scaling open-ended reasoning to predict the future. https://arxiv.org/abs/2512.25070 (c25, d18)
- [V] Zeng et al. (2025) FutureX. https://arxiv.org/abs/2508.11987 (c28; per-model figures not extracted)
- [V] Murphy (2026) Agentic forecasting with structured linguistic beliefs (BLF). https://arxiv.org/abs/2604.18576 (d07-d10)
- [V] Liptay, Schwarz, Poyiadzi, Wildman, Bosse (2026) Bench to the Future 2. https://arxiv.org/abs/2604.26106 (d13-d15)
- [V] Li, Wang, El Lahib, Xia, Pi (2026) Simulated ignorance fails. https://arxiv.org/abs/2601.13717 (d20; abstract and one figure read in full)
- [V] Karkar and Chopra (2025) Future is unevenly distributed. https://arxiv.org/abs/2511.18394 (d24; per-category numbers not read)
- [V] Metaculus Q2 AI Benchmark results notebook. https://www.metaculus.com/notebooks/38928/q2-ai-benchmark-results-pros-maintain-clear-lead/ (d22; secondary summary)
- [M] IBM Think (2026) AI forecasters: hire humans too. https://www.ibm.com/think/news/ai-forecasters-new-opportunity-business-hire-humans-too (d23; journalism; nine-months figure unverified)
- [M] Project index row. C:/Users/User/Desktop/AGI/research_notes/thinking_sciences/E03_forecasting_and_calibration/SUBFIELDS.md (a26; the 0.017 and Nov 2026 claim, traced to d05 and d06)
