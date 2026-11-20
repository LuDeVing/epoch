# Industrial fault detection: deep document

*Subfield E08.10, focus: statistical detection (key work: Isermann). Sources: evidence_a-d.jsonl (ids a01-a26, b01-b26, c01-c25, d01-d17), claims.jsonl (K01-K27), critique.md. Evidence ids are cited in brackets. Marks: [V] opened this session, [M] snippet or second-hand only.*

## 1. What it is

Industrial fault detection answers one question: has the plant or machine left normal behaviour? It is separate from two later questions.

- **Detection**: something changed. The false alarm rate sets the threshold. This is the statistical part.
- **Localisation**: which variables moved. Done by contribution analysis.
- **Diagnosis**: what caused it. Needs a causal model, labels or knowledge.

[a26] Most LLM work so far sits on the last step, on top of a fixed detector. That is the main fact for our agent.

The classical ladder, from Isermann [a01-a03, V]:

1. **Limit and trend checking** of single signals. Simple and reliable. It reacts only after a large or long change and gives no diagnosis.
2. **Signal models** (spectra, features).
3. **Process-model residuals.** Run a model of expected behaviour beside the plant and compare. Three families: parameter estimation, observers, parity equations.
4. **Symptoms, then diagnosis.** Classify symptoms with classifiers or neural nets, or reason over fault trees (cause to symptom) and event trees (symptom to cause).

Isermann lists four requirements: early detection of small abrupt or incipient faults; diagnosis of actuator, component and sensor faults; detection in closed loops; supervision in transient states.

Statistical detection in practice means: build a statistic from normal data (a residual, a T2 or SPE value, a Mahalanobis distance), set a control limit for a chosen false alarm rate (for example 1%), and flag when the statistic crosses it.

The standard testbed is the Tennessee Eastman Process (TEP) [a05, via a04; Downs and Vogel 1993 not opened]. It is a simulated plant with 5 units, 8 components, closed-loop control, 41 measured and 12 manipulated variables, and 21 programmed faults (15 with a known cause). Almost every number in this document comes from TEP, which is a weakness (section 9).

## 2. History and theories in depth

**Limit checking and model-based detection (to 2005).** Isermann's review [a01-a03, b26 M] frames the field. Limit checks are cheap but late. A dynamic model gives residuals that react to small and incipient faults. Parameter estimation suits multiplicative (parametric) faults and needs input excitation. Observers and parity equations model additive faults at input or output. All three need a good process model; a fault the model cannot represent gives misleading residuals [a02]. Examples: electric actuator, car lateral dynamics, combustion engine. The book (Isermann 2006) was not opened [c22 M].

**Multivariate statistical process monitoring (1990s to 2010s).** When plants have 50 or more correlated variables, a first-principles model is too costly. PCA, PLS, dynamic PCA, CVA, ICA take its place [a04]. PCA builds two statistics: T2 (variation inside the principal subspace) and SPE (variation outside it). Limits come from the normal data, often by kernel density estimate with alpha 0.01 [a06].

**Deep learning (2015 to now).** RNN, LSTM, GRU, CNN, autoencoders and transformers. The survey [a04] cites averages of 92.5% (RNN), 95% (LSTM), 95.9% (GRU), 96.2% (CNN with faults 3, 9, 15 excluded). Note the exclusion. Newer lines: neural component analysis [a06], graph networks that learn the sensor graph [a21 M, a19], self-supervised clustering [a11], feature ensembles [a12].

**Benchmark scepticism (2020 to now).** Four strands:

- TEP is saturated: 27 deep detectors reach F1 about 0.97 and an untrained LSTM autoencoder reaches 0.93 [b01, b02]. A real pilot-plant repeat finds a large drop [b04].
- Metrics inflate: point-adjusted F1 lets random scores beat published models [c05].
- Public time-series benchmarks are mostly trivial: a one-liner solves 86.1% of Yahoo series [d10].
- LLM entries (2023 on): zero-shot LLMs are weak detectors [c01, c03]. The 2024-2026 work puts the LLM after the detector, as explainer or diagnoser [a15, c06, d04].

**Competing views.**

- *Statistics are enough for detection, LLMs are for explanation* (Isermann tradition, FaultExplainer, AgentRCA's own claim that it is not a detector [d06]).
- *Deep temporal models solve even incipient faults* (AE-FENet 94-98% on faults 3, 9, 15 [a12]) versus *they do not, protocol is the cause* [a25, K02].
- *LLM above tool adds value* (Wu 2025 [c17], 95.7%) versus *it subtracts value* (Kim 2026 [c06]). Wu is single-author with weak baselines; Kim's design is stronger.

## 3. Core findings with exact numbers

Status: established / single-source / contested, as in claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| PCA-type detectors miss TEP faults 3, 9, 15 almost entirely | PCA FDR 5.70 / 7.70 / 3.05% (window 150, 2000+2000 split, 99% limit); T2 missed 92.0-98.4% on fault 3 across PCA, KPCA, AE, NCA; DAE 3.6 / 3.5 / 7.9% | a07, a11, b07, b09 [V] | established (K01) |
| PCA SPE buys low miss rate with false alarms | Faults 3/9/15 SPE missed 71.9 / 76.9 / 74.4% at FAR 30.0 / 23.8 / 16.9%; faults 1, 2, 4, 7 miss near 0 at FAR 16-24% | a07, a08 [V] | established (K03) |
| Deep temporal ensemble reaches high FDR on incipient faults in one protocol | AE-FENet 98.66% average; faults 3/9/15 97.55 / 97.55 / 96.05%; FENet (PCA features) 2 layers 91.50 / 94.25 / 80.80 on those faults | a12, b08 [V] | contested (K02) |
| Plain FENet average disagrees between tables | 79.05% (0 layers) vs 85.73% | a12 vs b08 | unresolved; read as 79-86% |
| Optimised filter-bank residual beats Kalman residual on hard faults | OEFB 93.9 / 84.4 / 91.5% vs Kalman s=0 26.0 / 44.0 / 56.3%; s=20 91.1 / 74.6 / 86.9%; raising s raises FAR too | a09, a10, b22 [V] | single-source (K17) |
| Detection delay is its own axis | DAE vs T2 vs SPE delay (min): fault 3 159/42/60; fault 13 27/138/108; fault 20 216/21/33; fault 21 819/63/36; fault 1 0/21/6 | b10 [V] | established (K04) |
| TEP saturated, does not transfer | 27 methods F1 up to 0.9699; untrained LSTM-AE F1 0.9335 (rank 9 of 27); TEP mean F1 0.859 vs 0.532 on 3 pilot plants, best 0.718 | b01, b02, b04, b05 [V] | established (K05) |
| Supervised TEP diagnosis is near ceiling | CNN-Transformer 99.92% vs LSTM 99.86% (+0.06) | b14 [V] | single (inflation example) |
| Pilot plant: deep beats shallow but no family wins | Best deep vs shallow F1: butanol 0.624 vs 0.588; OME 0.718 vs 0.666; water 0.531 vs 0.433 | b05 [V] | single-source |
| Metric choice inverts ranking | Point-adjusted vs plain F1 Kendall 0.07 (SWaT), 0.43 (WADI); Pearson -0.59, 0.41; always-no-fault gets 0.71 accuracy and F1 0 | c05, c16, c25 [V] | established (K06) |
| Benchmarks are trivial | 316 of 367 (86.1%) Yahoo series solved by a one-line detector | d10 [V] | single-source (K23) |
| Zero-shot LLM detectors are weak | F1 +14.6% vs moving average, -10.9% vs ARIMA; best deep model AER about 30% better; DETECTOR +135% over PROMPTER; vision input beats text; isolation forest beats LLMs on plain F1 | c01, c03, d09 [V] | established (K07) |
| LLM explains faults a detector flagged | With 15-cause list GPT-4o 7/11, o1-preview 9/11; no list 8/11 related; faults 5 and 10 fail for both; only 11 of 21 faults detected by PCA | a15, a16, b17 [V] | single-source (K08) |
| LLM plus specialist is below the specialist | TEP: LLM 64.67%, integrated 77.43%, specialist 83.33%, oracle 92.76%; missed 140/295 corrections; lost 15/99 correct (14 copied the tool error); gap -5.9 [-12.0,-0.7] | c06, c07 [V] | established (K09) |
| Prompt-level arbitration does not fix it | Explicit instruction 76.1% (missed 161/295, harmful 6/99); prior-label 72.2%; random-forest specialist 84.0% vs 78.2% | c08, d01 [V] | single-source (K19) |
| Tool quality sets the ceiling | Ensemble CNN 73.67% vs 68.04% single; LLM bound about 0.83 at 100% adherence; model size not predictive | b19, b20 [V] | established (K10) |
| LLM layer can cut a noisy detector's false alarms | 25 normal runs: specialist 14/25 = 56.0%, unaided LLM 8/175 = 4.6%, integrated 17/175 = 9.7%; integration kept NORMAL in 80/94 conflicts (85.1%) | d03 [V] | single-source (K22) |
| Statistical evidence layer drives agent accuracy | PRONTO top-1 full 87.6%; no operating-condition match 40.6%; no signed z-scores 43.8%; no AE residuals 83.8% | d14 [V] | single-source (K20) |
| Same agent on TEP is much weaker | TEP top-1 40.0%, top-2 61.5% (21 faults); supervised full-label 78-86%; supervised below 30% with 25 or fewer windows per fault | d05 [V] | single-source |
| Cost of LLM diagnosis | About 4,615 tokens, 5 tool calls, 51 s per window (30B model); LLM inference 500-5000 ms vs PID microseconds | d06, c20 [V] | single-source (K21) |
| Staged physics retrieval helps QA | Chain of Physics 68.80 vs direct 51.98 / RAG 50.61 (Opus 4.7, 1,314 Qs); graph retrieval plus one call 66.36; staging adds 1-5 points; best human expert 66.19 | c11-c13 [V] | single-source (K11) |
| Sensor-failure knowledge is shaky | FailureSensorIQ 2,667 MCQs: models average 53.5%, experts 60.2%; o1 60.4% to 44.2% under perturbation | d11 [V] | single-source |
| Interactive diagnosis is weak | 1 of 12 models above 60%; 3 no better than elimination (expected 5 turns); turns +97% under high initial uncertainty | c14, c15 [V] | single-source (K12) |
| Reasoning models far better on signal-to-semantics | DeepSeek-R1 76.92% vs Qwen2.5-7B 23.08% (about 13 items); Kim +5.2 unaided from high effort | c19, d02 [V] | single-source (K14) |
| Neural diagnosers are fragile | Clean 0.89-0.91; about 0.75-0.78 under FGSM/PGD at eps 0.1; AE defence 0.75-0.77 | a13, b16 [V] | single-source (K15) |
| No LLM study measures time-to-flag | Fixed 0.05 h modelled latency; per-window runtime only | d08, d06 | established gap (K24) |
| No shared TEP protocol for LLM studies | Kim 150 runs 6 classes; AgentRCA 21 faults; Alhazmi 39 scenarios; FaultExplainer 11 faults | d15, d05, d07 | established (K25) |
| Validation is mostly simulation | Survey: "Early/Pilot, Simulation"; real checks tiny (105 windows; 23 judgments) | d13, d04, d02 | established (K27) |

## 4. Mechanisms and models

Each item is written so an engineer can build it.

**4.1 Limit and trend check (Isermann level 1).** For a signal x: flag if x leaves [lo, hi] or if the slope over the last n samples exceeds a bound. Set bounds from normal data. Use as the cheapest first filter. Weakness: late, one signal at a time.

**4.2 Parity or residual with a process model.** Run model M beside the plant: residual r(t) = y(t) minus M(u(t)). Under no fault r is noise. Flag when |r| passes a threshold, or when a windowed mean or CUSUM does. Parameter estimation instead tracks model parameters and flags drift. Needs excitation of inputs [a02]. Faults outside the model give misleading residuals.

**4.3 PCA monitoring (T2 and SPE).**
1. Standardise normal data (about 500 to 4000 samples, 52 variables).
2. Keep k components (90% variance; Xiao used 9 PCs [b09]).
3. T2 = sum of squared scores scaled by their variance. SPE = squared norm of the reconstruction error.
4. Limit per statistic at alpha 0.01 (F-distribution or kernel density).
5. Flag when either crosses. Contribution analysis: rank variables by their share of the statistic. FaultExplainer uses the top 6 [a15].

Trade-off: SPE catches more but at 17-30% FAR on hard faults [a07].

**4.4 Kalman residual and the filter-bank fix.** Kalman residuals are whitening (all-pass) filters. For low-frequency faults (step, drift) a frequency-selective filter is better. The OEFB scheme combines an optimal filter with the output error. Detection on faults 3/9/15 rose from 26-56% to 84-94% [a09, a10]. Tuning parameter s trades detection against false alarms.

**4.5 Window feature ensemble (AE-FENet).** Slide a window of 150 samples. Build base detectors (PCA, DPCA, three Mahalanobis distances). Stack their features, transform in layers, with an autoencoder in the transform layers. Max lag 2 [a12]. The result depends on the window and the 2000 normal + 2000 faulty protocol.

**4.6 Autoencoder or LSTM-AE detector.** Train on normal data. Anomaly score = reconstruction error. Threshold from normal validation data. Note the untrained variant scores F1 0.93 on TEP [b02], so always run it as a baseline.

**4.7 Evidence-grounded LLM diagnosis (AgentRCA-like) [d04, d14].**
1. Digital twin or autoencoder trained once on normal data.
2. Match the current operating condition to normal data.
3. Compute signed z-scores per variable against that matched normal.
4. Put the top deviations into a hypothesis table of candidate faults with fault text.
5. The LLM calls tools (about 5 per window), retrieves technical-report text, and ranks causes.

Ablation shows the evidence steps carry the result (87.6 down to 40.6 or 43.8).

**4.8 Detector-then-explainer (FaultExplainer) [a15].** PCA T2 detects at a 1% false alarm rate. Top 6 contributing variables with percent changes plus a process description go to the LLM. Option: a list of 15 root causes, top 3 requested.

**4.9 LLM arbiter between tool and own judgement [c06, c17].** Two answers (tool label, LLM answer) go to a decision step. Kim's prompt-level arbiter under-corrects (missed corrections 140 to 161 of 295). Untested: a rule or trained selector (oracle 92.76%).

**4.10 LLM detector by forecasting (SigLLM DETECTOR) [c01, c04].** Encode numbers as digit strings with spaces, forecast the next window, score the residual. Beats asking the LLM to point at anomalies (+135%). Breaks on flat windows ("repetitive prompt" error on 23 SMAP and 13 MSL signals [c02]). Shorter windows (300 vs 1000 steps) help text input [d09].

## 5. What holds up

**Replicated across independent sources**
- Classical statistics miss incipient TEP faults 3, 9, 15 (Peng, Gao, Xiao, Zhou; four groups, different protocols, all low) [K01].
- Hit rate and false alarm rise together; reports without FAR mislead [K03].
- Detection delay and detection rate differ by detector and fault [K04].
- TEP saturation and the drop on real pilot data [b01, b04, b14].
- Metric inflation by point adjustment, trivial baselines, flawed benchmarks [c05, d10].
- Zero-shot LLMs are weaker detectors than simple statistics (SigLLM and Zhou-Yu agree) [K07].
- LLM plus tool is below the tool (five datasets in Kim; bearing datasets show the same pattern: 3 of 22 intervals below zero, 18 include zero, 1 above [d02]) [K09].
- Tool quality bounds the LLM [K10].

**Contested**
- Whether incipient faults are detectable: 3-8% (PCA) vs 94-98% (AE-FENet). The gap is protocol, not disagreement [critique].
- Whether more reasoning helps: +5.2 unaided but +2.2 integrated with interval -0.2 to 4.8; one matched pair in Alhazmi, p = 1.0 [K26].
- LLM arbiter: Wu 95.7% (single author, small data) vs Kim (LLM hurts).

**Failures and boundary conditions**
- Deep gains shrink on real data (F1 0.86 to 0.53; best 0.718).
- AgentRCA: 87.6% on a 5-class real rig, 40.0% on 21-class TEP.
- Faults 5 and 10 (and 13) fail for every LLM even with a cause list [a15, a16]. Cause not tested.
- Adversarial perturbation drops accuracy by 12-15 points [a13, b16]; defences cost clean accuracy.
- Continual learning from feedback failed; accuracy drifted down over repeated fault cycles (Hitachi HVAC) [c16].
- Boonmee 2024 reports 85% and 91% with a placeholder dataset size; ignore [c18].

**Interventions that worked**
- Forecast-then-residual over direct prompting (+135%) [c01].
- Summary statistics over raw series as input [c16]; vision over text [c03]; shorter windows [d09].
- Statistical evidence layer (z-scores, operating-condition matching) [d14].
- Graph retrieval of failure-mode to sensor links (+7.8 to +19.6) [c11, c12].
- State tracker prompt cut open-model timeouts; soundness-deliberation loop helped 2 of 3 open models [c15].
- Reasoning models over plain ones on signal-to-semantics [c19].
- LLM layer keeps NORMAL in conflicts, cutting detector false alarms [d03].

**Interventions that did not work**
- Chain of thought for anomaly reading [c03].
- Explicit arbitration instruction [d01].
- Handing the model its stored prior answer (72.2%) [d01].
- Model size as a predictor [b20].
- More stages in Chain of Physics beyond retrieval (1-5 points, sometimes negative) [c12].
- Plain RAG (below direct for two of three models) [c11].

## 6. Language models

**As raw detectors.** Weak. SigLLM [c01]: GPT-3.5 and Mistral-7B, 11 datasets. LLM F1 is 14.6% above a moving average and 10.9% below ARIMA; no top score on any dataset; best deep AER about 30% better. Prompting was fragile and costly: three months of prompt iteration, hours per dataset [c02]. Zhou and Yu [c03, d09] tested GPT-4o-mini, Gemini-1.5-Flash, Qwen, LLaMA with 21 prompt variants: images beat text, chain of thought did not help, and no evidence of subtle anomaly sensing; isolation forest has higher plain F1. Gruver [c04]: digit-string forecasting works for GPT-3 and LLaMA-2; GPT-4 did worse, blamed on tokenisation and calibration. Hitachi HVAC [c16]: GPT-4o detection F1 0.84 at accuracy 0.73 (high recall, poor precision); an always-no-fault rule gets 0.71 accuracy.

**As explainers after a detector.** FaultExplainer [a15, a16]: 7/11 (GPT-4o) and 9/11 (o1-preview) with a cause list; 8/11 related without one; shared failures on faults 5, 10 (and 13 open). Reports hallucinated mechanisms and plausible wrong causes when contributing variables are indirect. 11 faults, one run each, no statistics.

**As diagnosers with computed evidence.** AgentRCA [d04, d05, d14]: Qwen3-30B-A3B-Thinking, zero-shot, normal-only data. PRONTO 87.6% top-1 (96.8% top-2; random 20%); TEP 40.0% / 61.5%. Evidence layer removal drops it to about 41-44%. Supervised baselines need about 20 to 800 labelled windows per class to match. Alhazmi [d07, d08]: reasoning model above regulatory control, 39 of 39 scenarios kept in constraints versus 24 of 39 baseline; diagnosis 15 of 15 safety-critical from a closed 12-item list; US$2.32 per episode high effort vs US$1.31 low effort (38 of 39).

**As arbiters of a tool.** Kim [c06-c08, d01-d03]: seven models, TEP unaided 64.67%, integrated 77.43%, specialist 83.33%. The tool lifts the LLM by 12.8 points (CI 9.7 to 15.9) but integrated stays 5.9 below the specialist. Missed corrections 47.5%; harmful acceptances 15.2%. The advised call adopted the wrong label 16.4 points more often than a paired repeat call (CI 9.5 to 22.6). Fixes tried: explicit arbitration, prior label, random-forest specialist, higher effort. None closed it. Caveat: single author, closed 6-class set, oracle gap selected [d15]. Wu [c17] reports the opposite direction (95.7%) on a small vibration set. Liang and Sin [b19-b21]: an MCP agent calling CNN tools; rule "single model if max probability >= 0.95 else ensemble"; LLM accuracy bounded near 0.83.

**Knowledge benchmarks.** FailureSensorIQ [d11]: average 53.5% vs experts 60.2%; perturbation collapses scores (o1 60.4 to 44.2; llama-4-scout 54.0 to 24.1). Chain of Physics [c11-c13]: 68.80 with Opus 4.7, above the best expert 66.19. FactoryBench [d12]: no frontier model above 50% chance-corrected on structured levels; ranking reshuffles on decision questions. CoffeeBench [c14, c15]: 1 of 12 models over 60%.

**What changed results, by how much.**

| Change | Effect | Id |
|---|---|---|
| Forecast-then-residual vs ask directly | +135% F1 | c01 |
| Statistical evidence layer in agent | +44 to +47 points top-1 | d14 |
| Graph retrieval vs direct | +14 (Opus), +4.4 (Llama), +13 (Qwen) | c12 |
| Reasoning vs plain model | 76.92 vs 23.08% | c19 |
| Higher reasoning effort, unaided | +5.2 | d02 |
| Higher reasoning effort, integrated | +2.2, interval includes 0 | d02 |
| Specialist tool added to LLM | +12.8 | c06 |
| Explicit arbitration | -1.3 (interval includes 0) | d01 |
| Better tool (ensemble CNN) | +5.6 tool accuracy | b19 |
| Summary stats vs raw series | Better (size not recorded) | c16 |

Token cost: about 4,615 tokens per window [d06]. No study compares tokens against a detector at matched cost.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Report false alarm rate with every hit rate; reject recall-only wins.** G (new line under G7 evaluation). [E] K03; a07, a08, a10, b22.
2. **Always run trivial baselines in evaluation (always-normal, moving-std or diff one-liner, random, untrained model).** G7 harness. [E] K05, K06, K23; b02, c05, c16, c25, d10.
3. **Do not read numeric detection from the model's own reading of raw numbers; call a statistic or tool (O1).** O1. [E] K07; c01, c03, c24, d09, d10.
4. **A tool output is a hint, not the answer, and the model under-corrects it. Do not rely on a prompt to arbitrate; arbitrate with a check outside the model (G3, G5).** G5 / O5. [E] K09; c06, c07, d01, d02, d03.
5. **Tool quality sets the ceiling. Spend effort on the tool or its inputs before the model.** O1. [E] K10; b19, b20, d05, d14.
6. **Track time-to-first-correct-flag as well as final accuracy.** S0/O1 and harness. [E] K04, K24; b10, b11, d08.
7. **Do not trust one benchmark number; report two protocols and the spread.** G. [E] K05, K25 (spread 3-8% vs 97%).
8. **Treat simulation gains as unproven on plants; keep one real series.** Harness. [E] K27; d13, d04, d02.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Statistical evidence layer (signed z-score against matched normal) before the model sees data | S2/O3 | [S] | K20; d04, d14 |
| Hypothesis table with candidate faults, filled from computed evidence | S2/O3 | [S] | K20, K08; d04, a15 |
| Candidate-cause list given up front | S2 | [S] | K08; a15 (7/11 vs 8/11 related without) |
| Graph retrieval of failure-mode to sensor links | S2/S4/O4 | [S] | K11; c11-c13 |
| LLM as false-alarm guard on a noisy detector | G | [S] | K22; d03 |
| Rule or trained selector instead of prompt arbitration | O5 | [S] | K19; d01, d17 |
| Summary-statistics input over raw series; short windows | S1 | [S] | c16, d09 |
| Soundness-deliberation loop and state tracker | O2/S3 | [S] | K12; c15 |
| Higher reasoning effort vs extra verifying tool call at equal cost | G11 | [C] | K26; d02, d08 |
| Memory reset for repeated fault cycles | memory | [S] | K13; c16, d16 (M) |
| Perturb sensor inputs and measure answer flips | G | [S] | K15; a13, b16 |

## 8. Concrete tests on our bench

All arms at equal tokens. Item type is a streamed or windowed sensor series with a known fault onset. Fix one protocol first (window, split, threshold) and report on the incipient set 3, 9, 15 plus 5, 10, 13, with one non-TEP set.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | TEP windows, faults 3, 9, 15 plus normal | (a) LLM on raw numbers; (b) LLM calling PCA or filter-bank detector; (c) detector alone | Hit rate at fixed FAR (1%), FAR at fixed hit rate | (b) at or above (c); (a) below both [K07, K01] |
| T2 | Detector label plus conflicting LLM answer | Prompt arbitration; code rule (accept tool when its probability >= 0.95, else vote); trained selector | Missed corrections, harmful acceptances, accuracy | Rule beats prompt by at least 3 points; stays below oracle 92.76% [K19] |
| T3 | Window diagnosis, hidden fault class | With vs without z-score evidence layer | Top-1, top-2 | At least +20 points top-1 [K20] |
| T4 | Same, with and without 15-cause list | List vs open | Top-3 correct | List +1 to +2 faults of 11 [K08] |
| T5 | Normal-only runs plus faults | Detector alone; detector plus LLM guard | FAR at fixed hit rate | FAR falls without hit-rate loss [K22] |
| T6 | Streamed fault onset | Detector, LLM, combined | Time-to-first-correct-flag | Combined no slower than detector; LLM alone slowest [K24] |
| T7 | Failure-mode QA (FailureSensorIQ-style) | Direct; graph retrieval plus one call; full staging | Accuracy | Retrieval gives most of the gain; staging adds 1-5 [K11] |
| T8 | Same item, sensor noise added | Plain agent vs agent with summary stats | Answer flip rate | Summary stats flip less [K15] |
| T9 | Repeated fault cycles (10 cycles) | With vs without memory reset | Accuracy by cycle | Reset prevents drift [K13] |
| T10 | Hard diagnosis items | High effort vs low effort plus one extra tool call | Accuracy at equal cost | Extra tool call wins on integration items [K26] |

## 9. What does not transfer, and why

- **TEP numbers to real plants.** Simulation, no advanced control layers, persistent faults, hyperparameters tuned on a few standard faults [b06]. Pilot data: F1 0.86 to 0.53 [b04].
- **Closed-set diagnosis to open detection.** Kim uses 6 classes; Alhazmi a 12-item vocabulary; PRONTO 5 classes. None test an unknown fault [d15, d07, d04].
- **Latency-bound control to LLM loops.** LLM inference is 500-5000 ms against microseconds for PID [c20]; an agent window costs 51 s [d06]. LLM stays after detection.
- **Univariate benchmark series to plant data.** SigLLM used SMAP, MSL, NAB, Yahoo; Zhou-Yu used synthetic series [c01, c03].
- **Knowledge QA to field diagnosis.** FailureSensorIQ and Chain of Physics are text questions on documented links, not signals [c13, d11].
- **Human expert workflows.** Operators use alarm logs, maintenance records and digital twins; the survey scenario has no measured result [c21].
- **Deep-net accuracy to adversarial settings.** Accuracy 0.89-0.91 clean, 0.75-0.78 perturbed [b16].
- **Isermann's model-based residuals to an LLM agent without a plant model.** Needs input excitation and a good model [a02]; our agent only has data windows.

## 10. Open questions

1. Does an LLM at equal tokens beat a statistical detector plus explainer on faults 3, 9, 15? No paper compares tokens [K21, critique gap 1].
2. Does a rule or trained selector fix missed corrections, and does it replicate off TEP? [K19]
3. Which TEP protocol should be adopted? [K25]
4. Do Chain of Physics and FaultExplainer gains hold on real plant data? [K27]
5. Detection delay for LLM agents [K24].
6. LLMs on raw windows against always-normal and moving-std on real industrial series (Zhou-Yu used isolation forest, not an always-normal baseline) [d09, d10].
7. False alarm cost of LLM detection at a fixed hit rate [K22 is not at fixed hit rate].
8. Drift over repeated fault cycles and whether a memory reset helps [K13].
9. Why faults 5, 10, 13 fail for every LLM, and whether control-loop knowledge fixes it [a15, a16].
10. Gao 2024 plain FENet average 79.05 vs 85.73 mismatch is not resolved.

## 11. Sources

[V] opened, [M] snippet or second-hand only.

- [V] Isermann (2004/2005) Model-based fault detection and diagnosis: status and applications (IFAC version) - https://iiaat.guap.ru/iiaat/main/scien_ach/005.pdf (a01-a03)
- [M] Isermann (2005) Annual Reviews in Control - https://doi.org/10.1016/j.arcontrol.2004.12.002 (b26)
- [M] Isermann (2006) Fault-diagnosis systems (book) - https://link.springer.com/book/10.1007/3-540-30368-5 (c22)
- [M] Downs and Vogel (1993) A plant-wide industrial process control problem - https://doi.org/10.1016/0098-1354(93)80018-I (a05, b23, c23; numbers via secondary papers)
- [M] Rieth et al. (2017) Additional Tennessee Eastman Process Simulation Data - https://doi.org/10.7910/DVN/6C3JR1 (b24)
- [V] Ahang et al. (2024) Intelligent condition monitoring of industrial plants - https://arxiv.org/abs/2401.10266 (a04, a05)
- [V] Peng et al. (2017) Neural component analysis for fault detection - https://arxiv.org/abs/1712.04118 (a06-a08)
- [V] Zhou and Zhu (2023) On the optimality of Kalman filter for fault detection - https://arxiv.org/abs/2301.11573 (a09, a10, b22)
- [V] Gao, Wang, Chen (2024) Autoencoder-assisted Feature Ensemble Net - https://arxiv.org/abs/2404.13941 (a11, a12, b07, b08)
- [V] Pozdnyakov et al. (2024) Adversarial attacks and defenses in fault detection and diagnosis - https://arxiv.org/abs/2403.13502 (a13, a14, b16)
- [V] Khan et al. (2024) FaultExplainer - https://arxiv.org/abs/2412.14492 (a15, a16, b17, b18, c09, c10)
- [V] Golyadkin et al. (2023) SensorSCAN - https://arxiv.org/abs/2208.08879 (a17, b11-b13)
- [V] Agarwal et al. (2020) Hierarchical deep recurrent network for incipient faults - https://arxiv.org/abs/2012.03861 (a18)
- [V] Aryal, Modekwe, Lu (2026) Multi-level temporal graph networks - https://arxiv.org/abs/2604.18765 (a19)
- [M] Peng, Zhao, Hu (2021) Second-order component analysis - https://arxiv.org/abs/2103.07303 (a20)
- [M] Kovalenko et al. (2022) Graph networks with trainable adjacency - https://arxiv.org/abs/2210.11164 (a21)
- [M] Gravanis et al. (2026) Explainability for fault detection in chemical processes - https://arxiv.org/abs/2602.16341 (a22)
- [M] Liang and Sin (2026) search summary - https://psecommunity.org/wp-content/plugins/wpor/includes/file/2606/LAPSE-2026.0424-1v1.pdf (a23; opened as b19-b21 [V])
- [M] Huang et al. (2024) LLM channel selection - https://papers.phmsociety.org/index.php/phmconf/article/download/3881/phmc_24_3881 (a24)
- [V] Hartung et al. (2023) Deep anomaly detection on Tennessee Eastman process data - https://arxiv.org/abs/2303.05904 (b01-b03)
- [V] Hartung et al. (2026) Beyond Tennessee Eastman - https://psecommunity.org/wp-content/plugins/wpor/includes/file/2606/LAPSE-2026.0419-1v1.pdf (b04-b06)
- [V] Xiao, Kordon, Sen (2023) Fault detection and diagnosis in TEP - https://papers.phmsociety.org/index.php/phmconf/article/download/3578/phmc_23_3578 (b09, b10)
- [V] Pal et al. (2025) Compact CNN-Transformer for fault diagnosis - https://papers.phmsociety.org/index.php/ijphm/article/download/4744/2825 (b14, b15)
- [V] Liang and Sin (2026) LLM enhanced fault diagnosis framework - same LAPSE-2026.0424 URL (b19-b21)
- [V] Alnegheimish et al. (2024) SigLLM - https://arxiv.org/abs/2405.14755 (c01, c02)
- [V] Zhou and Yu (2025) Can LLMs understand time series anomalies? - https://arxiv.org/abs/2410.05440 (c03, c24, d09)
- [V] Gruver et al. (2023) LLMs are zero-shot time series forecasters - https://arxiv.org/abs/2310.07820 (c04)
- [V] Kim et al. (2022) Rigorous evaluation of time-series anomaly detection - https://arxiv.org/abs/2109.05257 (c05, c25; b25 is the same paper)
- [V] Kim (2026) When LLMs sit above diagnostic tools - https://arxiv.org/abs/2610.05031 (c06-c08, d01-d03, d15)
- [M] Kim (2026) related work on arbitration (MemToC, TrustMa..) - same URL (d17)
- [V] Zhou et al. (2026) Chain of Physics - https://arxiv.org/abs/2611.14263 (c11-c13)
- [V] McCabe et al. (2026) CoffeeBench - https://arxiv.org/abs/2610.19291 (c14, c15)
- [V] Lee et al. (2025) Exploring LLM-based frameworks for fault diagnosis - https://arxiv.org/abs/2509.23113 (c16); [M] PHM version https://doi.org/10.36001/phmconf.2025.v17i1.4350 (d16)
- [V] Wu (2025) Trustworthy industrial fault diagnosis architecture - https://arxiv.org/abs/2510.03815 (c17)
- [V] Boonmee et al. (2024) Consultation on industrial machine faults with LLMs - https://arxiv.org/abs/2410.03223 (c18; low reliability)
- [V] Li and Zhao (2026) S2S-FDD - https://arxiv.org/abs/2603.08048 (c19)
- [V] Gopaluni et al. (2026) LLMs in process systems engineering - https://arxiv.org/abs/2606.11589 (c20, c21, d13)
- [V] Wei and Fink (2026) AgentRCA - https://arxiv.org/abs/2607.22385 (d04-d06, d14)
- [V] Alhazmi (2026) Large reasoning models for abnormal situation management - https://arxiv.org/abs/2608.19819 (d07, d08)
- [V] Wu and Keogh (2021) Current time series anomaly detection benchmarks are flawed - https://arxiv.org/abs/2009.13807 (d10)
- [V] Constantinides et al. (2025) FailureSensorIQ - https://arxiv.org/abs/2506.03278 (d11)
- [V] Merzouki et al. (2026) FactoryBench - https://arxiv.org/abs/2605.07675 (d12)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 11 established claims: 8 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E08.10-K01** (reworded: the sources support less). Kalman residual does not miss these faults almost entirely: Zhou and Zhu report Kalman detection 26.0/44.0/56.3% at s=0 and 73-91% at s=10-20 on faults 3/9/15. PCA T2 missed 92.0/96.4/95.1% in Peng (96.4 not 'to 95%'), PCA FDR 5.70/7.70/3.05% in Gao, DAE 3.6/3.5/7.9 in Xiao all confirmed. Corrected claim: Statistical detectors (PCA T2, PCA SPE at a high false-alarm cost, DAE) detect incipient TEP faults 3, 9, 15 very poorly: PCA FDR 5.70/7.70/3.05% in the AE-FENet protocol, DAE FDR 3.6/3.5/7.9% in Xiao, PCA T2 missed 92-96% in Peng. Kalman-residual detection is partial (26.0/44.0/56.3% at s=0, rising to 73-91% at s=10-20 with higher false alarms in Zhou and Zhu).
- **E08.10-K05** (reworded: the sources support less). Not all 27 deep methods reach F1 about 0.97; the best is 0.9699 and lowest about 0.907 in the 2023 benchmark, and the 2026 paper reports mean F1 0.859 on TEP across 30 methods; the 0.532 mean, 0.718 best and untrained-LSTM-AE F1 0.933 are confirmed. Corrected claim: Near-saturated TEP scores do not transfer: in a 27-method deep benchmark the best F1 on TEP is about 0.97 (mean 0.859 across 30 methods in the 2026 follow-up), yet mean F1 is 0.532 (best 0.718) on three other pilot plants; an untrained LSTM autoencoder gets F1 about 0.93 on TEP, so TEP is too easy as a benchmark.
- **E08.10-K25** (number corrected). Alhazmi's benchmark has 13 scenarios x 3 noise seeds = 39 episodes, not 39 scenarios; AgentRCA's TEP evaluation uses normal plus 10 fault types (faults 3, 9, 15 and 16-20 excluded), not 21 faults; FaultExplainer's 11 detected faults not checked. Kim 150 runs, 6 classes confirmed. Corrected claim: No common TEP protocol exists for LLM studies: Kim uses 150 runs and 6 classes (IDV1, 4, 6, 13, 15 plus normal); AgentRCA evaluates windows on normal plus 10 TEP fault types (3, 9, 15 and 16-20 excluded); Alhazmi a closed-loop TEP-type kernel with 13 scenarios and 39 episodes (3 noise seeds); FaultExplainer 11 detected faults. Numbers cannot be compared across them.
