# Expected value of sample information: deep document

*Subfield C12.02. Scope: value of imperfect information, the quality of a noisy test, and how a language-model agent should decide whether a test, question or tool call is worth its cost. Built from evidence_a-d.jsonl, claims.jsonl (K01-K33) and critique.md in this folder. Evidence ids (a01, b09, d17 ...) point to those files.*

**Honest limits up front.** The founding books (Raiffa and Schlaifer 1961, Howard 1966) were never opened. All classic content comes through later papers that were opened. The human behavioural line is one paper family (Bastardi and Shafir 1998). Most LLM evidence is 20 Questions or simulated-patient dialogue with an LLM as the answerer. No study was found that prices a noisy test with known sensitivity and specificity in an LLM and compares it with the exact Bayes value. WebSearch quota ran out, so 2025-2026 LLM coverage is thinner than intended.

## 1. What it is

A test, a question, a tool call or a lookup is a noisy signal about the world. It costs something (tokens, time, money, user patience). It is worth buying only if its result could change what you do, and only if the expected gain from that change beats the cost.

Key terms:

- **EVPI** (expected value of perfect information): the most any test could be worth. You learn the truth for free, then pick the best action. EVPI is the value with truth known minus the value now.
- **EVSI** (expected value of sample information): the expected gain from a real, imperfect test. It is computed before the result is seen (preposterior analysis). EVSI is never above EVPI. [a01, a11, K01]
- **ENBS** (expected net benefit of sampling): EVSI minus the cost of the test. Buy only if ENBS > 0. [b19, b22]
- **EIG** (expected information gain): the entropy-based cousin used in AI. Value is the expected drop in uncertainty about the answer, not the gain in utility. Equal to EVSI only under a log-score utility. [a24, a14]
- **Quality of a noisy test**: sensitivity (true-positive rate) and specificity (true-negative rate), or in general the likelihood of each result under each state. A test is useless if no result can push belief across the act threshold. [d17, b21]

Core logic for a binary act/not-act decision with gain B for acting when the state is present and loss C for acting when absent: the act threshold is C/(B+C). A test is worth anything only if its most favourable result moves belief across that threshold. [K31, d17]

Why it matters for our agent: every extra attempt, check, retrieval, clarifying question or escalation is a noisy test with a cost. The schema has no rule for pricing them. The nearest guardrails are G1 (doubt only on a signal), G6, G7 (the schema must pay for itself) and G12 (spend by difficulty).

## 2. History and theories in depth

**Founding (1959-1966).** Schlaifer (1959) is credited with the first statement of EVSI (a02, snippet). Raiffa and Schlaifer (1961), *Applied Statistical Decision Theory*, introduced preposterior analysis and EVSI as a decision tool and gave closed forms for conjugate pairs. [a02, c25, book not opened] Per a 2023 citing paper: the closed-form EVSI under quadratic loss for a Bernoulli process with Beta prior is in Table 6.2 (p.191); three desiderata for a value-of-information formula (tractable, rich, interpretable) are on p.44. Page numbers may differ by edition. Howard (1966), *Information Value Theory*, is the second root; Dong et al. 2026 cite both. [c26]

**Conjugate cases.** Fleischhacker et al. 2023 list the processes with known closed-form EVSI: Bernoulli with Beta, Poisson with Gamma, Normal with known or unknown variance, Multinomial with Dirichlet. Most formulas trace to the 1961 book. They extend the Beta-Binomial case to Dirichlet-Multinomial and give the best sample size, which depends on prior strength, the ratio of loss scale to unit sampling cost, and data variance. Zero sample is optimal if the fixed cost cannot be recovered. They quote Lindley that sample size is "embarrassingly difficult to answer". They also note that value of information need not be monotone in action flexibility, risk aversion or wealth. [a11, a12]

**Computation era (1994-2025).** Exact EVSI needs a nested simulation: an outer loop over possible data, an inner loop for each posterior. That is slow.

- Chavez and Henrion 1994: treat the value gap z between best and second-best decision as normal, fit by regression, integrate the negative tail. They introduced the Relative Information Multiple (RIM = prior variance / posterior variance) to place a partial test between no information (k=1) and perfect information. Nine perfect-information values took 1 min 53 s on a 1994 Macintosh in a 27-action evacuation model. [a03, a04]
- Heath, Manolopoulou and Baio 2017: moment matching on the preposterior mean; 207,595 s (2.4 days) for nested Monte Carlo against seconds for the new method. Upward bias for future samples under about 20. [a05, a06]
- Heath, Kunst et al. 2019: four approximation methods compared on three health models; minutes or hours against weeks. [a07, a08]
- Hironaka et al. 2020: nested cost O(eps^(-2-1/alpha)); multilevel Monte Carlo reaches the optimal O(eps^-2). [a09]
- Heath 2021: EVSI with imperfect implementation; methods agree within 6%; 6 to 60 times faster. [a10]
- Li, Jalal and Heath 2024: the Gaussian shortcut can badly overestimate EVSI on nonlinear models; a Taylor-series fix overlaps the analytic result. [b17]
- Applications: Sadatsafavi 2024 (validation study size), Pei 2023 (HIV tests), Breeze 2025 (24 trial designs), Vervaart 2024 (follow-up length), Chen 2026 (minimum accuracy of a noisy test). [a13, b19, b20, b21, b22]

**Behavioural line (1998-2024).** Bastardi and Shafir 1998 showed that people pursue information that cannot change the choice, and that pursuing it changes the choice. The authors argue people rarely know they do this; having sought the information, they treat it as decisive. [b01-b06, b25] Later work: Kleinberg and Marsh 2023 (extra information lowers accuracy; related, not the same task); a 2024 reward-learning study (people pay points for advance information they cannot use). [d14, d16] A sister Shafir effect failed a preregistered replication (Chandrashekar 2021, N=1,026). [d15]

**AI line (mostly 2023-2026).** Information-gain question selection and cost-aware asking with LLMs:

- Uncertainty of Thoughts (Hu 2024). [a14, a15, b15, b16]
- Active preference inference (Piriyakulkij 2024) and OPEN (Handa 2024). [a17, a18, a24]
- GATE human study (Li 2023). [a20, c22]
- Question learning by DPO (Mazzaccara 2024) and STaR-GATE (Andukuri 2024). [a16, c12, c23]
- Active task disambiguation for code (Kobalczyk 2025). [a19, c20]
- BED-LLM (Choudhury 2025/2026). [c06-c08, d01-d04]
- Explicit value-of-information controller (Dong 2026). [c01-c05, b08-b11, d05, d06]
- Cost-aware exploration (Ding 2026, Calibrate-Then-Act). [b12-b14, c14-c16, d10]
- Battleship (Grand 2026). [d08, d09]
- EVPI clarification (Suri 2026). [a23]
- Conformal asking (Ren 2023). [a21, d18]
- Deferral (ReDAct 2026). [c17]
- Question asking that hurts (MediQ 2024). [c18, c19]
- Cost and tool use (CostBench 2025, Budget-aware tool use 2026, SMART 2025). [c24, d11, d12]

Competing accounts of why information is over- or under-bought:

1. Normative EVSI: buy iff EVSI > cost. [K01]
2. Heuristic confidence threshold: ask if confidence < tau. Needs tuning per task and cost. [b10]
3. Information gain (entropy) as a proxy for value: ignores stakes. [a24]
4. Instrumentality illusion / self-perception: pursuit makes the information look decisive. [b25]
5. Curiosity: information has direct value even if non-instrumental. [d16]

## 3. Core findings with exact numbers

Status: established, single-source, contested, human-only, older-models-only. "Cr" = number corrected by critique.md.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| EVSI is expected gain from a test computed before data; capped by EVPI; run only if EVSI exceeds cost | formula in a01; closed forms for 6 conjugate cases | a01, a11, a12, c25 | established (K01); books not opened |
| Exact EVSI is slow; approximations cut cost 6x to 1000x with small error | nested MC 207,595 s (2.4 days) vs 3.8-6.1 s moment matching; about 6 h vs 1.86 s (nonlinear case); weeks vs minutes/hours; max 6% difference; 6-60x faster | a05, a07, a10, b17 | established (K02) |
| Gaussian EVSI shortcut can overestimate on nonlinear models | GA 354.85 s vs spline-Taylor 16.86 s; GA "largely overestimates" | b17 | single-source (K03) |
| EVSI is zero when the decision is not close | Beta(44,458): EVPI 0.00037 / 0.00125 / 0 / 0 at thresholds 0.01 / 0.02 / 0.05 / 0.10; EVSI 0.00101 (about 81% of EVPI, derived) at N=1,000, threshold 0.02; little gain beyond N=4,000. HIV: EVSI $900,000 at $780/YLS but $0 at $3,000/YLS | a13, b20 | established (K04) |
| Value diminishes and plateaus near EVPI | same case; finite optimal sample size | a13, a11 | established (K05) |
| Much extra information is not worth buying | 12 of 24 trial designs had negative ENBS; EVSI per person 6.84 to 29.39 GBP vs trial cost 1.54m to 2.57m GBP | b19 | established (K06) |
| Test accuracy needed rises with cost; rare classes need near-perfect accuracy | with equal accuracies bound above 50%; 4 classes at prevalence 0.1/0.2/0.3/0.4; 200 random scenarios | b21 | single-source theory |
| Exact binary-test rule: EVSI = max(0, p*sens*B - (1-p)*(1-spec)*C) for prior below C/(B+C); EVSI <= EVPI = p*B | B=C=1, sens=spec=0.9: EVSI 0 at p=0.10, 0.100 at p=0.20 (50% of EVPI), 0.200 at p=0.30 (67%), 0.400 at p=0.50 (80%); p=0.30 with sens=spec 0.6 or 0.7: 0; 0.8: 0.100; 0.99 at p=0.50: 0.490 (98%) | d17 (own calculation) | established (K31); our arithmetic, not a book table |
| People wait for useless information and it changes choice (course) | simple n=140: 82% register; uncertain n=149: 56% waited, total 71% registered | b01 | human-only, single-source (K07) |
| Same in admissions and mortgage | admissions: simple n=261, 43% reject; uncertain n=278, 74% waited, 54% reject (chi2(1,539)=6.15). Mortgage: simple 29% approve; uncertain 75% waited, 56% approve (chi2=17.65, N=233); waiters approved 72% at $5,000 debt | b02 | human-only |
| Pursuit itself, not mention of uncertainty, causes the shift | CD player: simple 91% buy; uncertain with option to wait 55% buy, 69% waited; uncertainty resolved without pursuit (n=161) 75% buy; 91 vs 74, chi2(1,336)=12.57; wait rate 69% vs 70% | b03, b25 | human-only |
| People wait even when logic says waiting is useless | repair cost $0 or $90: 70% wait; $90 or $180 (both above buy threshold): 92% wait; other variants 66% and 60% | b04 | human-only |
| Effect with real stakes | tape-player raffle: simple 57% enter; uncertain 14% at once, 23% total (chi2(1,45)=5.35, p<.03); over 70% of waiters declined at $30 | b05 | human-only, N=45 |
| People do not foresee the effect | 70% predicted approval after waiting at $5,000 (observed 72%); only 20% predicted approval in simple version (observed 29%) | b06 | human-only |
| Replication and extension of the useless-information effect | cross-cultural (144 US, Iran, Japan) from a snippet only; Kleinberg and Marsh Exp 5 accuracy none 0.64/0.59, simple 0.80/0.73, simple-plus 0.76/0.69, complex 0.69/0.59 (women/men), 14% chose complex; sister Shafir effect: pooled d=-0.01 [-0.06, 0.03] at N=1,026, same direction in 2 of 8, opposite in 2, null in 4 | b07, d14, d15, d16 | contested (K08); no large-N replication of the 1998 task found |
| LLM asked to ask questions without a value rule does worse | MediQ: 11.3% relative accuracy drop (average over models and datasets, wide spread); most samples got no question | c18 | single-source (K09) |
| Abstention module for asking helps, does not close the gap | +22.3% from abstention; 10.3% gap remains; best closes 51.2% of the gap | c19 | single-source |
| EIG question choice beats plain prompting | BED-LLM Animals GPT-4o 45 to 93 (entropy 88, split 83); Mistral-Large 33/85/95/83 (prompt/split/BED/entropy); Llama-3.1-8B 8/49/63/54; Celebrities GPT-4o 45/63/86/64; Things GPT-4o-mini 26/38/49/37; average +37.4 pts. UoT +38.1% average over 5 datasets and 5 LLMs, +46.6% Llama3-70B. DPO on EIG pairs: INLG 56.7 to 68.9%, 7.1 to 5.2 questions | c06, a14, a16, c12, d08, a19 | established (K10); simulated answerers |
| UoT per-task (Cr) | GPT-4: troubleshooting 43.7 to 67.3 (main table; appendix 42.5 to 67.8); DX 89.4 to 97.0; MedDG 74.9 to 87.9 (appendix) or 88.0 (main); FloDial 42.5 to 67.8; Common 49.0 to 70.9; Thing 30.8 to 36.8; Gemini-1.5-Pro MedDG 81.4. "+38.1%" may be relative or points; not resolved | a14, b15, c10 | single-source; two tables for one result |
| Gain is not only more compute | UoT beats CoT-SC (k=33, 4.6k tokens: 32.6 / 37.6 / 42.5) by 33.8 pts, Reflexion by 29.9, ToT by 28.3, adapted ToT by 12.4; swapping ToT reward to information gain adds about 5.9%; adapted ToT at depth 4 still below UoT depth 3 | a15, b16, c11 | single-source (K11); only equal-token test in the set |
| Bad belief building can wreck EIG | GPT-4o-mini Animals: BED-LLM 88, Entropy 79, Data-Estimation 64, Implicit Maximization 47 (LLM picks by feel), ICL Beliefs 18 (no hypothesis filtering; a belief ablation, not a bad EIG formula) | c07, d01 | single-source (K12, K28) |
| Value-of-information controller vs tuned baselines (Cr) | Dong: matches or exceeds best tuned baseline in 18 of 20 conditions, up to +1.36 utility. Gemini Mixed 20Q sweep, VoI vs best baseline: c=0.01 8.64 vs 8.30 (+0.34); 0.02 7.72 vs 6.88 (+0.84); 0.05 5.01 vs 3.65 (+1.36); 0.10 1.38 vs 2.28 (-0.90, Confidence 0.5); 0.20 -0.96 vs 0 (-0.96, No Question). Main-text 14.14 vs 11.49 at c=0.01 is another run | c02, b09, c03, d05 | single-source (K13); loses at 2 of 5 costs |
| Fixed rounds give an inverted U; thresholds need per-task tuning | best threshold varies 0.5 to 0.9 across costs; a fixed Round (k=15) baseline scored 8.10 at c=0.01 | b10, c04 | single-source (K14) |
| LLM belief quality caps value; isotonic calibration helps | calibration fair on animals, worse on medical; retrieval ECE 0.618 to 0.029 | b11, c05, b13, d06 | established (K15); calibration only checked by argmax accuracy |
| Priors plus cost nearly give the optimal explore-or-commit policy, only with thinking | Qwen3-8B, 100 items, K=3: oracle reward 0.649; prompted non-think 11% match, 0.441; prompted thinking 23%, 0.476; priors non-think 20%, 0.436; priors plus thinking 94%, 0.625 | b12, c14, d10 | single-source (K16); on/off only |
| Retrieval as a costly noisy test | 1,000 PopQA: never 0.226; always 0.213 (acc 0.578); prompted non-think 0.244 (97.7% retrieve); prompted thinking 0.283 (61.4%); CTA 0.293 (65.3%, acc 0.512) | b13, c15 | single-source (K17); margin 0.01 |
| Imperfect priors decay smoothly; adversarial hurts most | reward: BERT 67% 0.382; noisy 52% 0.365; uniform 46% 0.349; adversarial 33% 0.299 (column assignment partly inferred). Code task: prompted 0.229, CTA-prompted 0.240, RL 0.259, CTA-RL 0.268; RL chose guess-and-go 0% | c16, b14 | single-source (K18) |
| LLMs update beliefs poorly over rounds | flight task: Bayesian assistant 81%, random 37%, off-the-shelf mostly 36 to 58%; CoT, 30 rounds, numeric format, base models did not fix; Bayesian-tuned agree about 80%; human-user flight 37.0% to +38.5 pts | a22, a25, c21 | single-source (K19); fix is fine-tuning |
| Uncertainty-based deferral | about 15% of steps deferred to large model matched large-model quality (ALFWorld, MiniGrid); beat random deferral in every combination | c17 | single-source (K20) |
| Cost-aware tool choice is weak | GPT-5 near perfect at length 5, about 75% at length 8; others under 60% at length 5; about 40% drop under dynamic conditions; a cost change drops GPT-5 by about 20 pts | c24 | single-source (K21) |
| EVPI-based clarification | coverage 59.73% vs 55.70% / 54.12% / 52.34%; 1.39 questions, 45.7% fewer; penalty 0 to 0.5 cut questions 18.1% with under 3% coverage change | a23 | single-source (K22); simulated answers |
| Conformal asking | KnowNo help 0.58 vs 0.72 per step, task success 0.74 vs 0.72; no-help 0.38; 50 hardware trials | a21 | single-source (K23) |
| LM-generated questions beat user-written prompts for humans | 388 participants; GATE beat prompts in 6 of 10 (absolute) and 7 of 10 (AUC); email validation: prompts slightly hurt; OPEN beats LM-only and BOED-only | a20, c22, a18 | established (K24) |
| Myopic search keeps most of the gain | UoT depth 1/2/3: 20Q 82.6/86.7/92.5; other series 66.1/67.0/75.2 and 63.5/64.7/67.3 (labels inferred); Battleship one-step ask-or-act +0.023 to +0.029 F1 | d07, d08 | single-source (K26) |
| Cheap estimator budget | ranking stable at 10 hypotheses vs 85; N>=15 hypotheses, M=15 questions (N=5, M=8 for preferences); full EIG about same wall-clock as entropy; Data-Estimation more than 10x slower | d02, d03 | single-source (K27); one game, one turn |
| Strong models gain little from the scaffold | Battleship Captain F1: GPT-5 0.716 to 0.722 (+0.006); Llama-4-Scout 0.367 to 0.741 (QM); GPT-4o 0.450 to 0.753; weak models at 1% / 35% of GPT-5 cost reached 0.67 win rate vs GPT-5 | d08 | single-source (K33) |
| Answerer is the weak link | human spotter 92.5% (931 gold questions); 15 LMs 52.5% to 92.8%; GPT-4o 72.8% simple to 60.4% complex; model noise epsilon=0.1 assumed | d09, d18, d04 | single-source (K32) |
| Tool overuse | Llama-3.1-8B over 50% overuse on GSM8K; over 30% generally; training cut calls 24%, performance +37.1% (macro) | d12 | single-source (K29); training fix |
| A bare budget line is a strong baseline | coding agent at budget 50: 55.4% vs 36.8% with near-equal calls (45.7 vs 46.0); search agent at budget 10 matched budget 100 with 40.4% fewer calls, 31.3% lower cost (12.8 vs 12.6% BrowseComp) | d11 | single-source (K30); no value gate compared |

## 4. Mechanisms and models

Everything here can be coded. The program computes values; the model fills slots (hypotheses, answer likelihoods), as in the schema's division of labour.

### 4.1 Binary test with known quality (exact rule)

Inputs: prior p that the state is present; sensitivity sens; specificity spec; gain B if act and present; loss C if act and absent; test cost c.

1. Threshold t = C/(B+C).
2. Post-test beliefs: P(present | +) = p*sens / (p*sens + (1-p)*(1-spec)). P(present | -) = p*(1-sens) / (p*(1-sens) + (1-p)*spec).
3. If the prior is below t and P(present | +) < t, no result can change the action. EVSI = 0. Skip the test.
4. Otherwise, for prior below t: EVSI = p*sens*B - (1-p)*(1-spec)*C (floor at 0). EVPI = p*B.
5. Run the test iff EVSI > c. [d17, K31]

Worked check (B=C=1): p=0.2, sens=spec=0.9 gives 0.18 - 0.08 = 0.10. At p=0.10 the result is 0.09 - 0.09 = 0. A weak test (0.6 or 0.7) at p=0.30 gives 0.

### 4.2 General preposterior analysis

For states s, results z, actions a, utility U(a,s):
EVSI = sum over z of P(z) * max_a E[U(a,s) | z]  minus  max_a E[U(a,s)].
P(z) = sum over s of P(s) P(z|s). The posterior comes from Bayes. This is the whole algorithm for a discrete problem. Cost is |S| x |Z| x |A| operations, trivial in code. The hard part is getting P(z|s) (test quality) and P(s) (calibrated belief).

### 4.3 Information-gain scoring of a question (UoT, BED-LLM, Battleship)

1. Sample N candidate hypotheses (answers) from the model; filter those inconsistent with the evidence so far. Filtering is essential: skipping it gave 18 in BED-LLM. [d01]
2. Generate M candidate questions (or tests).
3. For each question, have the model give the answer likelihood P(y | hypothesis, question) for every hypothesis (or sample imagined answers).
4. EIG(q) = H(answer) - E over hypotheses of H(answer | hypothesis), where H(answer) is the entropy of the mixture. Compute in code.
5. Ask the argmax question. Stop when EIG falls below cost.

Budgets seen: N>=15 hypotheses with up to 3 sample-then-filter rounds and M=15 for 20 Questions; N=5, M=8 for preferences. [d02] The question ranking was stable from about 10 hypotheses (one game, one turn). Do not let the model choose the "most informative" question by judgement (47 vs 88). [d01, K28]

Relation to EVSI: EIG is EVSI under a log-score utility. With real stakes use EVSI directly; EIG ignores which hypotheses matter for the action. [a24]

### 4.4 Value-of-information controller (Dong 2026)

NetVoI(q) = VoI(q) - c. Ask the best q only if max NetVoI > 0, else commit to the current best answer. VoI(q) is the expected gain in best-action utility after the answer, using the LLM's own belief over latent states. [c01] Needs: an enumerable answer space, a predefined question set, a per-question cost in utility units, and a belief. Failure mode: at high cost it lost to a tuned threshold and to asking nothing (c=0.10 and 0.20). [d05]

### 4.5 Myopic versus deeper search

One-step EVSI scores each test as if it were the last. Depth-3 simulation in UoT gained +9.9, +9.1, +3.8 points over depth 1. [d07] Myopic rules fail when two tests are worth something only together (interacting tests). No test of that case exists. [Gap 6]

### 4.6 Cheap EVSI estimators

For continuous Monte Carlo models: moment matching, regression on one probabilistic run, or multilevel Monte Carlo. Rules: more than 30 outer samples for moment matching; give effort to outer data simulations, not inner posterior draws (50,000 total / 1,000 inner = 50 outer). [a05, a06, a09] The Gaussian shortcut can overestimate on nonlinear models. [b17] For an LLM agent these matter little; use the discrete enumeration in 4.2.

### 4.7 Partial information scale

RIM = prior variance / posterior variance: k=1 is no information, k to infinity is perfect. [a04] A noisy test with likelihood ratios LR+ and LR- moves odds by those factors. The test is informative only if at least one result can move belief to the other side of the threshold.

### 4.8 Calibration as gate

VoI is only as good as P(s) and P(z|s). Calibrate before use: isotonic regression cut ECE from 0.618 to 0.029 in retrieval. [b13] Dong checked calibration by argmax accuracy only. [d06]

### 4.9 Conformal asking

Collect a calibration set; set a score threshold so the prediction set covers the true option with probability 1-eps; ask only if the set has more than one option. Needs no explicit utility. [a21]

### 4.10 Deferral

A cheap model defers a step to a stronger model when its own uncertainty is above a threshold. Model uncertainty acts as a noisy test of "this step is wrong". About 15% of steps deferred matched the large model. [c17]

### 4.11 Minimum test accuracy

For K classes with prevalences and a test cost, there is a minimum accuracy (local and global bound) below which the test is not worth using; rare classes need near-1 accuracy; the bound rises with cost. [b21]

## 5. What holds up

**Holds up (several sources).**

- EVSI logic and bounds (EVSI <= EVPI; zero value when the decision is not close). Mathematical result plus consistent applied cases. [K01, K04, K05]
- Approximate EVSI computing is fast and accurate enough for health models. Five sources. [K02]
- Net value can be negative; half of 24 trial designs lost money. [K06]
- Scoring candidate questions by information gain beats unscored prompting in 20 Questions and diagnosis: five or more independent papers and several models. [K10]
- Calibration limits the value of any VoI rule. [K15]
- Model-generated questions help humans in preregistered studies (388 participants), but not in every setting. [K24]

**Single-source or fragile.**

- Value controller beats tuned thresholds: one paper, one model for the cost sweep, losses at 2 of 5 costs. [K13]
- Equal-token advantage of information gain: only UoT. [K11]
- Priors plus thinking give the optimal policy: one 8B model, 100 items. [K16]
- Human useless-information effect: one paper family from 1998. The cross-cultural replication was seen only as a snippet. No preregistered large-N replication found. A sister Shafir effect failed to replicate (N=1,026, pooled d=-0.01), so a 1990s Shafir effect cannot be assumed to hold; the original author disputes how close that replication was. [K08, d15]

**Failures and negative findings.**

- MediQ: unscored asking lowered accuracy by 11.3% relative. [c18]
- Dong: VoI lost to a tuned threshold at c=0.10 (-0.90) and to No Question at c=0.20 (-0.96). The "18 of 20" headline hides this. [d05]
- BED-LLM: a belief built without hypothesis filtering scored 18, below prompt-only 44. Judgement-picked questions scored 47. [d01]
- Chain-of-thought, more rounds, numeric formats and base models did not repair weak belief updating. [a25]
- RL alone never learned to skip tests (0% guess-and-go). [b14]
- CostBench: frontier models fail at cost-optimal tool sequences at length 8 and under cost changes. [c24]
- Kobalczyk: EIG estimated from logprobs underperformed. [c20]
- DPO on BigBench (29 candidates): success rose but EIG did not (0.31 to 0.28). Plain supervised fine-tuning lowered success. [c12, a16]
- STaR-GATE: one variant drifted back to 50% win rate. [c23]

**Moderators.**

- Cost: the gate wins at low and mid cost, loses at the two highest in this sweep. [d05]
- Model strength: gap shrinks for stronger models (GPT-5 +0.006 F1 vs GPT-4o +0.303). [d08, a19]
- Reasoning budget: priors help only with thinking on (20% vs 94%). [d10]
- Answerer quality: LLM answerers range 52.5% to 92.8% accurate; the gains assume faithful answers. [d09, d18]
- Questioner-answerer mismatch: BED-LLM helps most when they differ, so same-model simulations may flatter the scheme. [c08, d04]
- Task type: closed hypothesis sets help (UoT DX 97.0); open-set performance is lower; abstract targets stay hard (7.7% to 23.1% after DPO). [c10, c12]
- Threshold closeness: zero value when the decision is far from the threshold. [a13, b20]

**Interventions that worked.** Scored question choice (EIG); stating prior and cost with thinking on; isotonic calibration; conformal asking; deferral on uncertainty; a budget line; training on Bayesian traces (not a scaffold); DPO on EIG pairs (training).

**Interventions that did not.** Plain "ask if needed" prompts (MediQ, Dong); LLM-judged "most informative" (47); CoT for belief updating; fixed-round asking beyond its peak; RL without priors.

## 6. Language models

**Without a value rule, LLMs misprice information.**

- They ask too little: in MediQ most samples got no question; 11.3% relative accuracy drop when prompted to ask. [c18]
- They ask or call too much: tool overuse over 50% on GSM8K for Llama-3.1-8B, over 30% generally. [d12] Prompted non-thinking retrieval fetched 97.7% of the time and scored 0.244 against 0.293 for calibrated. [c15]
- They ask low-value questions: LLaMA-2-chat-7B EIG was about 0.3 per question against 1.0 for a perfect half split. [c12] ChatGPT 20 Questions questions were low in informativeness (Bertolazzi 2023, via citing papers only). [c28]
- They do not trade cost against uncertainty on their own: 11% to 23% optimal match on Pandora's Box. [c14]

**What changed behaviour, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Score candidate questions by EIG (sampled hypotheses, likelihoods, in code) | Animals GPT-4o 45 to 93; average +37.4 points over prompt-only (BED-LLM); +38.1% (UoT); Llama-3.1-8B 8 to 63 | c06, a14 |
| Same, versus entropy alone | 93 vs 88 (GPT-4o); 88 vs 79 (GPT-4o-mini); entropy is a strong cheap baseline | c06, d01 |
| Same, versus CoT-SC at about equal tokens | UoT +33.8 points over CoT-SC k=33 | a15, b16 |
| Information-gain reward inside ToT | about +5.9% | c11 |
| Explicit prior and cost, thinking on | 23% to 94% optimal match; reward 0.476 to 0.625 | d10 |
| Same, thinking off | 11% to 20% match; reward 0.441 to 0.436 (no gain) | d10 |
| Calibrated retrieval choice | reward 0.213 (always) / 0.226 (never) to 0.293 | c15 |
| Isotonic calibration | ECE 0.618 to 0.029 | b13 |
| Value controller vs tuned baseline | +0.34 to +1.36 utility at low cost; -0.90 and -0.96 at high cost | d05 |
| EVPI-selected clarifying questions | coverage +4.03 points (59.73 vs 55.70) with 45.7% fewer questions | a23 |
| Conformal asking | help 0.58 vs 0.72 per step at similar success | a21 |
| Uncertainty deferral | 15% of steps deferred matches large model | c17 |
| Budget line in prompt | SWE 36.8% to 55.4% at equal calls | d11 |
| Fine-tune on Bayesian traces | about 80% agreement with Bayesian; human-user flight +38.5 points | c21 |
| Fine-tune to avoid unneeded tools | calls -24%, performance +37.1% | d12 |
| Bayesian question and move selection (Battleship) | weak models F1 0.367 to 0.741; GPT-5 0.716 to 0.722 | d08 |

**Model strength.** The more capable the model, the smaller the scaffold gain. GPT-5 gained +0.006 F1 from Bayes-QM. Kobalczyk reports the gap shrinks for stronger models. Weak models with the full Bayesian scaffold reached 0.67 win rate against GPT-5 at 1% (Llama-4-Scout) and 35% (GPT-4o) of its cost. [d08, a19] Scaffold value depends on the base model; test on ours.

**Belief updating.** Off-the-shelf models plateau after the first round and do not update like a Bayesian; simple prompt remedies failed. [a22, a25] So the program should keep the probability table and do the Bayes step in code, not ask the model to update.

**Human parallels.** MediQ-style under-asking and tool overuse are opposite errors; the human useless-information effect is the over-seeking side. No LLM test of the Bastardi-Shafir shift exists. [K29]

**Caveats on all LLM evidence.** Answerers are mostly LLMs; hypothesis sets are closed; questions are yes/no or multiple choice; run counts are small; Dong, BED-LLM and CTA do not equalise tokens against baselines; belief inputs are the model's own, only partly calibrated probabilities; most are preprints.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Skip a test that cannot change the action.** Before any extra attempt, check, retrieval or question, compute in code whether any possible result would move belief across the act threshold. If not, skip. Schema part: G (sharpens G1 and G12), S0/S4 gate. [E] K01, K04, K31; ids a01, a11, a13, b20, d17. The exact binary case is our own arithmetic; the agent's belief and the test's quality must come from data (see Test first).
2. **Value is capped by EVPI and falls with each extra test.** Stop testing when the marginal gain is below the cost; never run a fixed number of rounds. Schema part: G7 and S6 stop. [E] K05, K06; a13, a11, b19, b22. Fixed-round asking gave an inverted U in Dong. [b10]
3. **Score candidate tests in code; never ask the model which is most informative.** Enumerate hypotheses and answer likelihoods; compute information gain in code. Schema part: O (information-seeking operator, extends G5 "code selects"). [E] K10 (five papers); c06, a14, a16, a17, a19. The "judgement is worse" part (47 vs 88) is single-source, K28.
4. **Measure calibration before using the agent's own probabilities to price anything.** Schema part: G (calibration) and memory (class record read by S0). [E] K15; b11, c05, b13, d06. Keep calibration per problem class in the class record.

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Value-gated test rule (EVSI > cost) vs always-test, never-test, tuned confidence threshold, at equal tokens | S4/S5 gate, G7 | [S] K13 | c02, d05 |
| Plain budget-left line as equal-cost baseline against the gate | G7/G12 | [S] K30 | d11 |
| Necessity check ("could any result change my decision?") before a tool call or extra attempt | G (info-seeking guard) | [S] K29; human effect [C] K08, K07 | b01-b05, d12, d15 |
| Keep Bayes update in code with an explicit probability table, vs free-form updating | S2 / S7 | [S] K19, K31 | a22, a25, d17 |
| Ask-if-needed prompts are worse than structured asking (candidate for 4b) | 4b | [S] K09, K14 | c18, c04 |
| Ask-first vs noisy answerer sweep (10%, 30% wrong) | G (answer noise) | [S] K32 | d09, d18 |
| Depth 1 vs depth 3 simulation at equal tokens, including interacting tests | O | [S] K26 | d07, d08 |
| Sample counts for EIG (3, 5, 10, 15) on non-game tasks | O | [S] K27 | d02, d03 |
| Conformal or set-size gating for escalation or extra sampling | S6 trigger | [S] K23 | a21 |
| Uncertainty deferral of hard steps to a deeper mode | S0/S6 | [S] K20 | c17 |
| Priors and cost in prompt; smallest thinking budget that works | S0 | [S] K16 | d10 |
| Scaffold gain by base-model strength | S0 (when to scaffold) | [S] K33 | d08, a19 |
| Cost-change robustness of the gate | G | [S] K21 | c24 |
| EVPI-based clarification when the task is ambiguous | S1 | [S] K22 | a23 |
| Corrupted-prior decay | G (calibration) | [S] K18 | c16 |

## 8. Concrete tests on our bench

All arms get equal total tokens (setup, prior estimation and extra calls counted, per G7). Report wins and losses at each cost level, not only the best.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Coding or reasoning items with an optional extra check (run tests, self-check, extra attempt) priced at c | (a) always check, (b) never check, (c) tuned confidence threshold, (d) EVSI gate (belief from agreement across attempts, calibrated on a held-out set), (e) plain "budget left" line | accuracy minus c times checks; checks per item; tokens | (d) >= (c) at low cost; (d) loses at very high cost; (e) may be close. Margins small (+0.3 to +1.4 utility in Dong). |
| T2 | Synthetic binary decisions with stated prior, sens, spec, B, C and answer key from 4.1 | (a) free-form reasoning, (b) reasoning plus a written probability table, (c) code computes Bayes from model-stated numbers | error of post-test probability; accuracy of "test worth buying?" sign; EVSI absolute error | table narrows error; free-form mispredicts near threshold (p=0.10, sens=spec=0.9 should give EVSI 0). |
| T3 | Items where an extra tool call or retrieval cannot change the answer (both outcomes lead to the same action) | (a) plain tool access, (b) necessity-check prompt, (c) code-side threshold check, (d) no tool | useless-call rate; accuracy; flip rate of the final answer after the useless result | fewer useless calls with no accuracy loss. Also shows whether a pursued irrelevant result moves the answer (Bastardi-Shafir analogue). |
| T4 | Clarifying-question tasks with an underspecified input and a hidden fact, closed hypothesis set first | (a) ask-if-needed prompt, (b) fixed k questions, (c) EIG scoring in code, (d) EIG plus cost gate, (e) entropy only | success; questions per success; tokens | (c) and (d) beat (a); entropy within about 5 to 10 points of EIG (79 vs 88 earlier). |
| T5 | T4 with a noisy answerer: 0, 10, 30% wrong answers | ask-first rule vs no-ask | accuracy; break-even noise | find the noise at which ask-first loses. |
| T6 | Two-test interaction items (each test alone changes nothing; both together flip the action) | one-step EVSI vs depth-3 simulation | success at equal tokens | one-step fails; depth 3 wins. Size unknown. |
| T7 | Calibration sweep: corrupt the agent's probabilities by known amounts | gate with raw, isotonic-calibrated and adversarial belief | utility; decay curve | smooth decay; adversarial worst (0.382 to 0.299 in CTA). |
| T8 | Escalation: plain mode vs deeper mode triggered by low agreement or set size over 1 | always deep, never deep, uncertainty-gated | accuracy at equal tokens | gated matches always-deep with about 15% of the deep calls if the signal is good. |
| T9 | Model-strength sweep (smallest, middle, strongest model we run) on T1 and T4 | scaffold vs plain | scaffold gain per model | gain falls with strength (GPT-5 +0.006). |
| T10 | Thinking-budget sweep on T2 with priors and costs in the prompt | 0, small, medium, large reasoning budget | optimal-match rate | find the smallest budget that unlocks the effect (only on/off known: 20% vs 94%). |

## 9. What does not transfer, and why

- **Health-economics EVSI machinery** (nested Monte Carlo, moment matching, regression, multilevel MC, RIM): built for continuous model parameters and trial design. Our agent has a handful of discrete hypotheses; enumeration (4.2) is enough. [K02]
- **Absolute EVSI values from health cases** (0.00101, GBP 6.84 to 29.39 per person, $900,000): domain units, no meaning for a reasoning agent.
- **The human useless-information effect**: all human data are hypothetical scenarios or a small raffle (N=45) with students; there is no LLM test; the nearest replication (a sister effect) failed. Treat it as a hypothesis about LLMs, not a fact. [K07, K08]
- **20 Questions numbers**: closed hypothesis set, answers eliminate candidates, the answerer is an LLM, questions are yes/no or multiple choice. Real reasoning problems have open hypothesis sets and answers that do not eliminate. [a14 limits, c09]
- **Simulated-user results** (preferences, MediQ, WebShop): the simulated answerer may share the questioner's blind spots; gains differ with questioner-answerer mismatch. [c08, d04]
- **Training-based fixes** (Bayesian teaching, DPO, STaR-GATE, SMART, RL): outside the no-training scope. Use only as evidence of what failure exists. [K25]
- **Tool-call costs in domain units** (CostBench travel, search-call counts): our cost is tokens. The principle holds; the numbers do not.
- **EIG as value**: ignores stakes. It is a proxy and fits when the goal is to identify the answer, not to choose an action with asymmetric loss. [a24]
- **Conjugate closed forms**: our test likelihoods are not known or conjugate; the model must supply them.
- **KnowNo conformal guarantee**: needs an exchangeable calibration set from the same distribution; our item mix may drift. [a21]

## 10. Open questions

1. Does a value-gated test rule beat always-test, never-test and a tuned threshold at equal tokens on reasoning or coding tasks (not 20 Questions)? (Gap 1)
2. How accurately can an LLM estimate post-test probability and the EVSI sign for a given sensitivity and specificity? Does an explicit table fix it? (Gap 2; answer key in d17.)
3. Do LLM agents show the Bastardi-Shafir shift? Does "could this change my decision?" remove it? (Gap 3)
4. At what cost range and calibration level is "never ask" best? Dong swept only cost. (Gap 4)
5. Smallest imagined-answer count that keeps the ranking stable on non-game tasks. (Gap 5; 10 hypotheses known, answers not swept.)
6. Does one-step EVSI fail on interacting tests; depth 1 vs depth 3 at equal tokens. (Gap 6)
7. Did the 1998 effect hold in large-N or preregistered replications 2010-2025? (Gap 7)
8. How big is the gap between simulated and real noisy answerers (real users, real retrieval, real tests)? (Gap 8)
9. What exact results do Raiffa and Schlaifer 1961 and Howard 1966 give that could become rules of thumb? Books unopened. (Gap 9; the numeric rule is closed by d17.)
10. Smallest reasoning budget that unlocks prior-and-cost use. (Gap 10)
11. Can agreement across attempts serve as a calibrated belief for pricing a test, given that same-model samples are correlated (schema G4)?
12. When the agent's belief is wrong but confident, does the gate skip tests it should run?

## 11. Sources

[V] = opened and read this session. [M] = snippet or citation only.

| Source | Mark | URL |
|---|---|---|
| Wikipedia, Expected value of sample information | [V] | https://en.wikipedia.org/wiki/Expected_value_of_sample_information |
| Raiffa and Schlaifer (1961) Applied Statistical Decision Theory | [M] | https://en.wikipedia.org/wiki/Expected_value_of_sample_information |
| Howard (1966) Information Value Theory | [M] | cited in https://arxiv.org/abs/2601.06407 |
| Heckerman, Horvitz, Nathwani (1992) Pathfinder | [M] | none opened |
| Strong, Oakley, Brennan (2014) partial EVPI by regression | [M] | none opened |
| Chavez and Henrion (1994) Efficient estimation of the value of information | [V] | https://arxiv.org/pdf/1302.6794 |
| Heath, Manolopoulou, Baio (2017) EVSI by moment matching | [V] | https://arxiv.org/pdf/1611.01373 |
| Heath and Baio (2017) Efficient nested Monte Carlo tutorial | [V] | https://arxiv.org/pdf/1709.02319 |
| Heath, Kunst et al. (2019) EVSI in practice | [V] | https://arxiv.org/pdf/1905.12013 |
| Kunst et al. (2019) Computing EVSI efficiently | [V] | https://arxiv.org/pdf/1910.03368 |
| Hironaka, Giles, Goda, Thom (2020) Multilevel Monte Carlo EVSI | [V] | https://arxiv.org/pdf/1909.00549 |
| Heath (2021) EVSI adjusting for imperfect implementation | [V] | https://arxiv.org/pdf/2105.05901 |
| Fleischhacker, Fok, Madiman, Wu (2023) Closed-form EVSI, multinomial | [V] | https://arxiv.org/pdf/2301.00729 |
| Sadatsafavi et al. (2024) EVSI for external validation | [V] | https://arxiv.org/pdf/2401.01849 |
| Li, Jalal, Heath (2024) EVSI for nonlinear models | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC11492544/ |
| Li et al. (2025) Effective sample size, Gaussian approximation | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC11992650/ |
| Breeze et al. (2025) 24 trial designs for weight management | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC12396955/ |
| Pei et al. (2023) Value of information and implementation, HIV | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC10517616/ |
| Chen et al. (2026) How accurate should a precision medical test be | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC13312563/ |
| Vervaart (2024) ENBS for survival data | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC11490075/ |
| Bastardi and Shafir (1998) On the pursuit and misuse of useless information | [V] | https://bear.warrington.ufl.edu/brenner/mar7588/Papers/bastardi-jpsp1998.pdf |
| Brunswik Society newsletter (2003) cross-cultural replication | [M] | https://brunswiksociety.org/wp-content/uploads/2022/06/2003news.pdf |
| Kleinberg and Marsh (2023) Less is more | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC10469135/ |
| Chandrashekar et al. (2021) Accentuation and compatibility, preregistered replication | [V] | https://www.cambridge.org/core/product/BB2D0F7C7B9BC46BD65F1512868C8D6F/core-reader |
| Effect of noninstrumental information on reward learning (2024) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC11315740/ |
| Hu et al. (2024) Uncertainty of Thoughts | [V] | https://arxiv.org/abs/2402.03271 |
| Mazzaccara, Testoni, Bernardi (2024) Learning to ask informative questions | [V] | https://arxiv.org/abs/2406.17453 |
| Piriyakulkij, Kuleshov, Ellis (2024) Active preference inference | [V] | https://arxiv.org/pdf/2312.12009 |
| Handa et al. (2024) OPEN, Bayesian preference elicitation | [V] | https://arxiv.org/pdf/2403.05534 |
| Kobalczyk et al. (2025) Active task disambiguation | [V] | https://arxiv.org/abs/2502.04485 |
| Li, Tamkin, Goodman, Andreas (2023) GATE | [V] | https://arxiv.org/abs/2310.11589 |
| Ren et al. (2023) KnowNo | [V] | https://arxiv.org/pdf/2307.01928 |
| Qiu et al. (2026) Bayesian teaching | [V] | https://arxiv.org/abs/2503.17523 |
| Suri et al. (2026) Structured uncertainty guided clarification | [V] | https://arxiv.org/pdf/2511.08798 |
| Dong et al. (2026) Value of Information: human-agent communication | [V] | https://arxiv.org/abs/2601.06407 |
| Choudhury et al. (2025/2026) BED-LLM | [V] | https://arxiv.org/abs/2508.21184 |
| Ding, Tomlin, Durrett (2026) Calibrate-Then-Act | [V] | https://arxiv.org/abs/2602.16699 |
| Piatrashyn et al. (2026) ReDAct | [V] | https://arxiv.org/abs/2604.07036 |
| Li et al. (2024) MediQ | [V] | https://arxiv.org/abs/2406.00922 |
| Andukuri et al. (2024) STaR-GATE | [V] | https://arxiv.org/abs/2403.19154 |
| Liu et al. (2025) CostBench | [V] | https://arxiv.org/abs/2511.02734 |
| Bertolazzi et al. (2023) ChatGPT's information seeking strategy | [M] | cited in 2406.17453 and 2402.03271 |
| Grand, Pepe, Tenenbaum, Andreas (2026) Shoot first, ask questions later | [V] | https://arxiv.org/pdf/2510.20886 |
| Liu et al. (2026) Budget-aware tool use | [V] | https://arxiv.org/pdf/2511.17006 |
| Qian et al. (2025) SMART tool overuse | [V] | https://arxiv.org/pdf/2502.11435 |
| Wang et al. (2026) Agents should invoke tools only when epistemically necessary | [V] first pages only | https://arxiv.org/pdf/2506.00886 |
| Own calculation: exact binary EVSI table (not a source) | n/a | D:/research_scratch/C12.02/tmp/C12.02_evsi_calc.py |

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 9 established claims: 6 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C12.02-K04** (reworded: the sources support less). Sadatsafavi shows EVSI/EVPI zero only at thresholds 0.05 and 0.10; at 0.01 EVPI was 0.00037 (EVSI nonzero, not given), so 'at others 0' is wrong. 81% is computed (0.00101/0.00125), not stated. Pei 2023 supports threshold dependence (EVSI 0 at WTP 3000, nonzero near 780). Corrected claim: EVSI is zero when current evidence already settles the decision, and its value depends on the decision threshold. In the Sadatsafavi 2024 validation case study, at the 0.02 threshold EVSI was 0.00101 at N=1000 (about 81% of EVPI 0.00125), while EVPI, and so EVSI, was 0 at thresholds 0.05 and 0.10 (EVPI was 0.00037 at 0.01). In Pei 2023, EVSI was 0 at WTP 3000/YLS and nonzero near 780/YLS.
- **C12.02-K05** (reworded: the sources support less). Only Sadatsafavi (one case study) shows the steep rise and plateau toward EVPI; Fleischhacker 2023 does not report a plateau (it gives closed forms and an optimal sample size). Corrected claim: In one external-validation case study (Sadatsafavi 2024), EVSI rose steeply for small samples and plateaued toward EVPI, with little gain beyond N=4,000; generality is not shown by the other listed source.
- **C12.02-K31** (now contested: a source does not say this). Neither the Wikipedia EVSI page nor Fleischhacker 2023 contains the binary sensitivity/specificity formula or the example; I checked the algebra myself and the formula and the four example values (0, 0.100, 0.200, 0.400) are correct, so it is the agent's own derivation, not a sourced claim.
