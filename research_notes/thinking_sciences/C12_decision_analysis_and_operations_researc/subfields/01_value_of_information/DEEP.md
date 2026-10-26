# Value of information: deep document

*Subfield C12.01. Built from evidence_a-d.jsonl (a01-a31, b01-b33, c01-c27, d01-d25), claims.jsonl (K01-K34) and critique.md in this folder. Evidence ids are cited as a07, d05 and so on; claim ids as K06. Status marks: [E] established, [S] single-source, [C] contested. Source marks: [V] opened this session, [M] snippet or abstract only.*

*Scope note. Most "value of information" results on language models are really information gain results. Only a few use payoff or cost. This document keeps the two apart.*

---

## 1. What it is

Value of information (VoI) is the most a decision maker should pay to learn something before choosing. It is a price tag on a test, a question, a lookup or a thinking step.

**Expected value of perfect information (EVPI).**
- Take the best action now. Its expected payoff is EMV = max_i sum_j p_j R_ij.
- Imagine a clairvoyant who tells you the true state j before you act. You then pick the best action for that state. Expected payoff with perfect information is EV|PI = sum_j p_j max_i R_ij.
- EVPI = EV|PI - EMV. (a01, c01)

**Properties.**
- EVPI is never negative. The decision maker can ignore the information. (a03, a04)
- It is an upper bound. No real test, however good, can be worth more than EVPI. A test that costs more than EVPI is never worth running. (a03, K01)
- With two actions and two states, EVPI cannot exceed half the largest reward gap between the actions. (a03)
- Values of several tests are not additive. The second test is valued after updating on the first. The order of observing does not change the total gain in maximum expected utility. (a04, K02)
- All of this assumes a risk-neutral decision maker, a known payoff table and known priors. For risk-averse or risk-seeking agents the simple subtraction can fail and iterative calculation is needed (a04, d25). We did not open the primary sources that prove this (K34).

**Worked example (unit test for code).** (a02)
- Actions: stock (1500, 300, -800), fund (900, 600, -200), CD (500, 500, 500). States have p = (0.5, 0.3, 0.2).
- EV: stock 680, fund 590, CD 500. EMV = 680.
- Best action per state: 1500, 600, 500. EV|PI = 0.5*1500 + 0.3*600 + 0.2*500 = 750 + 180 + 100 = 1030.
- EVPI = 350. The critique recomputed this by hand and confirmed it.

**Related quantities.**
- EVPPI: value of learning a subset of the uncertain inputs. This is the usable form in health economics (b01).
- EVSI: value of imperfect (sample) information. Not covered on the page opened; belongs to a separate row in SUBFIELDS.md.
- Expected information gain (EIG): expected drop in Shannon entropy of the quantity of interest. Lindley (1956) showed that with a KL utility, expected utility equals mutual information between parameter and observation (a13, a15). EIG values reduced uncertainty, not improved payoff. The two agree only when the payoff depends on the uncertainty being reduced.
- Probability gain: expected reduction in the chance of a wrong classification. Humans follow this one (b09, d22).
- Value of computation (VOC): VoI applied to a thinking step. Expected gain in the best action's value after the computation, minus its cost (a16, a07).

**Why it matters to our agent.** The schema has a test state (S4) and a stop and select state (S7). Both need to answer: which test next, and is another test worth its cost. VoI gives a principled bound (EVPI) for the second question and a ranking score (information gain per cost) for the first.

---

## 2. History and theories in depth

**Founding (1950s-1960s).**
- Lindley (1956) defined the information value of an experiment by Shannon information, which is the origin of Bayesian experimental design (a13, a15).
- Raiffa and Schlaifer (1961), *Applied Statistical Decision Theory*, set out expected value of sample and perfect information (c26). Not opened.
- Howard (1966), "Information value theory", IEEE Trans. Systems Science and Cybernetics 2(1):22-26, named the clairvoyant bound and the value of information in decision analysis (a06). Not opened. The IEEE page returned nothing; the APIs were rate-limited (d25). Everything below attributed to Howard is second-hand.

**Value of computation: VoI turned on thinking (1968-2012).** (a07)
- Matheson (1968) borrowed the idea from Howard.
- I. J. Good (1968) proposed using it to control chess search and defined Type II rationality: rationality that counts the cost of its own deliberation.
- Russell and Wefald (1988, 1991) built a metalevel model with sequential computations and used it in Othello.
- Hay, Russell, Tolpin and Shimony (2012) recast selecting computations as Bayesian metalevel selection (a07-a12). Their results are the nearest thing to proofs about stopping a test sequence:
  - Theorem 5: expected number of computations of the optimal policy is at most EVPI/c, c being cost per computation (a08).
  - Theorem 7: if the myopic (one-step) policy continues, the optimal policy continues (a10). So a one-step rule stops too early, never too late, in that model.
  - Theorem 10: for the one-armed Bernoulli problem the optimal policy takes at most about 1/(4c) - 3 computations (a09). With c = 0.001 that is at most 247.
  - Example 3: the optimal policy stops with probability one, yet a run can be arbitrarily long with tiny probability (a12). So a hard cap is still needed.
  - Optimal metalevel policies are not index policies. The best computation can flip from one arm to another as the context value changes (a10).
  - UCT, the bandit rule used in Go, applies bandit theory to a problem that is not a bandit problem, because simulations cost the same whatever the utility of the action simulated (a10).

**Bayesian experimental design (BED).** A parallel statistics line: choose the experiment that maximises expected utility of the data, usually EIG (Rainforth et al. 2024, a13). The hard part is estimation: EIG needs a nested expectation, and nested Monte Carlo estimators are biased at any finite inner sample size (a14).

**Health economics: EVPI in daily use.** (b01-b07)
- NICE and others use EVPI and EVPPI to decide whether more research is worth funding (c01, c27).
- Barriers are interpretation and compute (b03). VoI numbers have no natural scale, so they only mean something against a cost or threshold.
- Of 86 applied EVPI articles, 66 recommended further research, 13 none, 7 gave no recommendation. EVPI above research cost was necessary but not sufficient. No covariate (funder, location, disease, year, outcome) predicted the recommendation (b04). Authors seemed to use a rough threshold of about 1.48 million (currency garbled) (b05). Abstract only.
- Naive Monte Carlo EVPI is biased upward at small samples because it takes a maximum over noisy estimates (b07).

**Human information search: a rival theory.** (b08-b13, d22)
- Nelson (2005): five rival measures (diagnosticity, information gain, KL distance, probability gain, impact) could not be separated by older human data. Computer search found cases where they disagree. A new experiment contradicted diagnosticity (b08).
- Nelson, McKenzie, Cottrell, Sejnowski (2010): three experiments with test environments built to separate the theories. Probability gain explained human search best after experience-based learning. Verbal summary statistics gave a different pattern. Within-subject consistency between the two formats was not significant (all four comparisons) (b09, d22).
- Wu, Meder, Filimon, Nelson (2017): 4 experiments, N = 2,858, 14 formats. Posterior-probability icon arrays and bar graphs gave the best query choices. Accuracy of probability judgments did not predict search performance (b10).
- Meder, Nelson et al. (2018): greedy one-step value is not optimal for sequences of tests in the Person Game (a 20-questions task); simulation, no human sample (b11).
- Bastardi and Shafir (1998): people seek non-instrumental information and then let it change the choice (b12).
- Golman, Hagmann, Loewenstein (2017): people sometimes avoid useful free information, which breaks the never-negative rule because information enters utility directly (b13).

**LLM era (2023-2026).** Three strands, covered in section 6:
1. Information-gain question selection (UoT, LIPS, OPEN, Kobalczyk, BED-LLM, CA-BED, MedClarify).
2. Net-value gates that charge a cost per question, retrieval or critique (Dong 2026, Di Gioia 2026, Fang 2026, SAG).
3. Value of computation as a reward or a stop rule for reasoning length and sample count (De Sabbata 2025, Adaptive-Consistency, ESC, CGES, Certified SC).

**Competing views to keep in mind.**
- Information gain vs probability gain vs payoff-based value: humans favour probability gain; every LLM paper uses information gain; only a few use payoff. No LLM study compares them (K20, critique).
- Is the VoI idea carrying the gain, or is the machinery around it? BED-LLM's "Split" rule (pick the question that halves the sampled hypotheses) gets most of the gain with an explicit candidate set (d10). The gain may come from the explicit hypothesis set and code-side selection, with true EIG adding a smaller part.

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single-source, [C] contested. "Indep." counts independent sources after merging duplicate records.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| EVPI = EV with perfect info minus best EV; never negative; caps any test | Example: EMV 680, EV given PI 1030, EVPI 350 | Wikipedia a01-a04 [V]; Howard 1966 not opened | [E] K01 |
| Values of tests are not additive; value each test after updating on the others | no numbers | a04, b11, d25 | [E] K02 |
| One-step (myopic) rule can stop too early; if it continues, optimal continues | Hay Thm 7 | Hay et al. 2012 a10 [V] | [E] K03 |
| Expected number of tests of the optimal policy is at most EVPI/c; stopping is certain but run length is unbounded | E[N] <= EVPI/c; one-armed Bernoulli <= 1/(4c)-3 (247 at c=0.001) | Hay 2012 a08, a09, a12 [V] | [S] K04 |
| Value-per-cost selection of samples beat a fixed plan in 9x9 Go | 64% win vs UCT at 10,000 samples per ply, c = 1e-6; 1000 repeats | Hay 2012 a11 [V] | [S] K05 |
| Code ranks questions by EIG, model only proposes and words them: beats model-chosen questions | UoT +38.1% avg success over direct (5 datasets, 5 LLMs, 3 repeats); BED-LLM +37.4 points on 20 Questions; Kobalczyk +8 to +15 points after 4 rounds for weaker models | Hu 2024 a19; Choudhury 2026 b16; Kobalczyk 2025 a27 [V] | [E] K06, K07 (7 and 3 independent sources) |
| UoT per cell | GPT-4: DX 97.0, MedDG 88.0, FloDial 67.3 (direct 43.7). Gemini-1.5-Pro MedDG closed 51.4 to 81.4. Claude-3-Opus Common open 45.0 to 63.1. Llama3-70B +46.6 avg | Hu 2024 a19, a20 [V] | [E] |
| UoT beats other planners | beats CoT-SC by 33.8, Reflexion 29.9, original ToT 28.3, adapted ToT 12.4 | Hu 2024 a19 [V] | [E] |
| UoT at matched tokens (20Q / medical / troubleshooting) | Adapted-ToT D=4 about 9.3k tokens: 40.9/86.7/63.7; UoT D=3 9.2k: 54.4/92.5/66.0. Pruned UoT 4.7k: 48.1/88.4/63.2. CoT-SC 4.6k: 32.6/37.6/42.5 | Hu 2024 b15, c08 [V]; critique corrected token count to 4.7k | [E] |
| Uncertainty reward is the working part | Adding it to plain ToT: +5.9 avg; swapping UoT reward for self-evaluation lowers success. UoT vs UoT-Max, GPT-4: 79.3/71.2/97.0/88.0/67.3 vs 79.3/63.7/95.1/83.1/62.6 | Hu 2024 a21, c09 [V] | [E] |
| UoT results are fragile to tuning | UoT on 20 Questions swings 60.4 to 90.1 with two hyper-parameters; CA-BED 82.9 sits inside that range | Arnould 2026 d08 [V] | [S] |
| Gain shrinks for strong models and open sets | GPT-4o-mini HumanEval binary at round 4: 79.6 vs 81.5 (gap 1.9, SE about 2.0); GPT-3.5: 70.8 vs 85.6. Mistral-Large Thing open set 12.5 to 15.0 | Kobalczyk a28; Hu a21 [V] | [E] K08 |
| EIG training gain falls with model size | Qwen2.5-7B Animals 7.6 to 21.0 (x2.8); 14B Animals 35.0 to 39.2 (+4.2); 14B Plants 11.8 to 13.6 (+1.8). BED-LLM reimplementation on 14B Animals 26.4 vs base 35.0 | Hartmann 2026 d06 [V]; 5 episodes per setting, SE 0.9-4.8 | [E] K08 (workshop paper) |
| Gain shrinks across medical backbones | MedClarify on MediQ: GPT-5.1 48.1 to 50.4 (+2.3); Llama-3.3-70B 41.2 to 46.1 (+4.9); DeepSeek-R1 33.3 to 41.1 (+7.8). Overall NEJM 28.0 to 36.1, MedQA 44.3 to 48.4; 469 cases | MedClarify 2026 d09 [V] | [E] K08 |
| How EIG is estimated matters | Kobalczyk 20Q after 10 questions, GPT-3.5: uniform 6.2, logprobs 4.1, implicit 4.9. BED-LLM GPT-4o Celebrities: full 86, entropy-only 64, Split 63, CoT 63, prompt-only 45 | Kobalczyk b19; Choudhury b17 [V] | [E] K09 |
| Computing EIG beats asking the model to judge the best question | Animals GPT-4o: prompt-only 45, Split 83, BED-LLM 93, implicit max 70. Celebrities Mistral-Large: 19, 63, 91, 36. Llama-3.1-8B Things: 10, 12, 26, 10 | Choudhury 2026 d10 [V] | [E] |
| Open hypothesis space needs machinery | ICL belief tracking instead of sampled, filtered hypotheses: Animals GPT-4o 25 vs 93; GPT-4o-mini 18 vs 88; Mistral-Large 53 vs 95 | Choudhury d11 [V] | [S] K28 |
| Raw LLM test proposals are often useless | Battleship: 33% (GPT-4) and about 40% (CodeLlama) of valid programs had EIG 0. Single LLM question EIG 0.65-0.66 bits vs human mean 1.27 (N=40, 605 question-board pairs), best human 3.61, grammar 0.36. Best-of-5 near human mean, best-of-10 above it (p<0.001 CodeLlama, p=0.01 GPT-4) | Grand 2024 a22, a23, c23 [V] | [S] K10 (one paper) |
| EIG reranking in rule discovery | Zendo: humans 5.26/8, ReAct-style agent 4.60/8, best model 6.55/8; swapping InfoGain for LLM-only or random experiments hurt significantly | Piriyakulkij 2024 a29 [V] | [S] |
| Models do not know what is missing | QuestBench Logic-Q and Planning-Q under 50%; Planning-Q "not sure" 0.7-4.6% when 41.8% truly underspecified; at most 5 points above random. Filtering to solvable items changed Logic-Q by 0.0-1.1 | Li 2025 b20, c13, d20 [V] | [S] K11 |
| Models answer early instead of asking | -39% avg across six tasks, 15 LLMs, 200,000+ simulated conversations, N=10 per cell | Laban 2025 a31 [V] | [S] K12 |
| Free asking can hurt; a gate fixes it | MediQ: direct asking -11.3% relative; best gate +22.3% over BASIC, +12.1% over Initial, still 10.3% below full information. GPT-4 iMEDQA: Full 79.7, Initial 54.5, BASIC 55.4, best 66.1 | Li 2024 b22 [V] | [E] K13 |
| Net-value rule beats tuned confidence threshold without tuning | VoI won or tied in 18 of 20 conditions; up to +1.36 utility; Mixed 20Q at c=0.01: 14.14 vs 11.49 (threshold 0.90). The 1.36 is 5.01 vs 3.65 at c=0.05 | Dong 2026 c02, c03 [V] | [S] K14 |
| Stake-sensitivity (one instance each) | VoI asked longer at reward 10 than reward 1 (c = 0.05); verifier benefit flips with assigned liability | Dong d21; Zhang 2026 d23 [V] | [E] K33 (illustrations) |
| Simulation: cost-aware selection plus net-value stop | Greedy ReAct viability 56.76 vs net-VOI controller 93.03 (N=200); entropy-threshold stop with greedy selection 60.17 (+3.4); fixed K=3 tests 50.92. Time 114.5 vs 14.5 | Di Gioia 2026 d01 [V] | [S] |
| Real-LLM version of that stop rule lost to always-test | GPT-4.1, 60 questions: AlwaysRetrieve U=+5.33 (EM 0.817); net-VOI U=+2.20 (EM 0.500, 0.63 retrievals); NeverRetrieve U=-10.00. All 5 zero-entropy act-without-retrieve cases were wrong | Di Gioia d02 [V] | [S] K14, K32 |
| Value-per-budget action scorer under hard caps | Qwen3-32B: best F1 in 7 of 16 cells, tied 2; beat AFlow, BATS, Search-o1, BAVT in 14, 10, 16, 15 of 16 cells; mean wall time -27.2% vs BAVT. Removing the budget penalty hurt most. Qwen3-32B upper-mid budget F1: HotpotQA 0.47 vs BAVT 0.41; 2Wiki 0.63 vs 0.45; MuSiQue 0.43 vs 0.34; Bamboogle 0.56 vs 0.42 | Fang 2026 d03, d04 [V] | [S] |
| Gating a critic by an uncertainty proxy | ALFWorld: gated 78.3% at 56k tokens; always-on critic 74.2% at 341k; no critic 33.0%; ReAct+SFT 30.2%; always (no gating) 62.0% at 282k; remove entropy 77.6, remove margin 74.6; critic calls 2.85 to 1.10 as success 71.0 to 83.0 | Park 2026 SAG c15, c16 [V] | [S] K16 |
| Confidence is not VoI | Calibrated confidence: committed-answer accuracy up to +41 points, overall +15 (HotpotQA) and -17 (MuSiQue); map worse than raw confidence at retrieval depth 3 on all three models | Chhikara 2026 c18, d24 [V, abstract page] | [C] K15 |
| Training a questioner with EIG reward | tau-bench avg success: none 23.6, trained 1.7B clarifier 27.3 (+3.7), untrained Qwen3-8B clarifier 23.0; DeepSeek-R1 agent 35.7 to 40.0; trained clarifier asked 1.3 questions vs 3.9-5.1; INLG 20Q DPO 56.7 to 68.9% (EIG 0.34 to 0.45); BigBench success 17.2 to 31.0 while EIG fell 0.31 to 0.28; STaR-GATE preferred on 72% of tasks | Deng 2026 d05; Mazzaccara 2024 b23; Andukuri 2024 b30, c22 [V] | [E] K22 |
| Look-ahead beats one-step only when tests complement each other | Cube-NM after 5 tests: 75.0 (two-step) vs 30.2 (one-step), Qwen3-0.6B. Natural target prediction at turn 5: 32.7 (K=3), 30.8 (K=2), 29.7 (K=1). CA-BED depth 2: +21.8 points at +1.8 turns; Detective Cases 46.0 vs direct 27.6 | AR-BED d07; CA-BED d08 [V] | [S] K27 |
| Sample-stopping rules save a lot on easy and medium items | Adaptive-Consistency up to 7.9x (avg 3.3x) fewer samples, under 0.1% loss, 17 datasets, 3 LLMs; ESC: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CommonsenseQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%; CGES 16.0 to 6.7 calls for -0.4 points (GPQA -2.1 with little saving); Certified SC 61-86 of 100 samples, MATH-500 81.0 vs 81.2; CoT+PoT agreement 9.3x fewer samples, 78.6% done with 2, drop 0.1%; ReASC up to -70% cost (GSM8K Qwen-2.5-3B 5.70 vs 18.70 samples) | b26, b27, d14-d18 [V] | [E] K17, K29 |
| Cost per token on reasoning shortens it | RaM: 23-45% fewer tokens at similar accuracy; up to 50.3% shorter on easy items (Llama-3.2-3B); out of domain 28-36% fewer than STaR. Training required | De Sabbata 2025 a17, b25 [V] | [E] K17 |
| Interior optimum in number of questions | tau-bench clarification peaked at a middle budget; forced fixed K=3 tests worse than greedy (50.92 vs 56.76); hard caps near 10 turns in MedClarify | Deng d05; Di Gioia d01; d09 [V] | [S] K30 |
| Estimating VoI is costly and biased | Case study: nested MC about 55 minutes, GAM negligible, GP regression 2-4 s; GP cost grows with N^3; naive MC EVPI biased upward at small samples | Heath 2015 b01, b02 [V]; Brennan 2007 b07 [M] | [E] K18 |
| LLM belief inputs are weak | Off-the-shelf LLMs show little improvement after round 1 in a 5-round flight task (624 simulated users); only GPT-4 + CoT + externally summarised history explored bandits well | Qiu 2026 b28; Krishnamurthy 2024 b29 [V] | [E] K19 |
| Humans use probability gain, not info gain | Probability gain best in experiment 1; preference robust in experiment 3 | Nelson 2010 b09, d22 | [C] K20 |
| LLM-elicited payoffs are noisy but usable | Utility rankings agreed with human labels 65.3-70.4%; DeLLMa 73.3% (agriculture) and 64.2% (stocks) vs o1-preview 33.3% and 35.0%; up to 40% accuracy gain over direct and CoT | Liu 2024 c25, d19 [V] | [S] K23, K32 |
| Conformal ask-or-act | Human help cut 10-24% at epsilon = 0.15 | Ren 2023 a30 [V]; critique: PDF did not parse in re-check | [S] K24 |
| Role split in preference elicitation | GATE: 388 participants; beat user-written prompts in 6 of 10 settings (absolute), 7 of 10 (AUC); OPEN: 39-48 users per condition, beat LM-only and design-only | Li 2023 a24, b31; Handa 2024 a25 [V] | [S] |
| Health-economics decisions | EVPI above cost necessary, not sufficient; 66 of 86 recommended research | Thorn 2016 b04 [M] | [S] K25 |

**Duplicate records.** a19, b14 and c07 are one paper (UoT). a22, a23, b24 and c23 are one paper (LIPS). a24, b31 and c20 are one paper (GATE). a17 and b25 are one paper (RaM). Count independent sources, not records.

---

## 4. Mechanisms and models

This section gives each model in a form an engineer can code.

### 4.1 EVPI routine (pure code, runs in S4/S7)

Inputs: actions A, states S, prior p(s), payoff R[a][s].

```
EMV   = max_a sum_s p[s] * R[a][s]
EVPI  = sum_s p[s] * max_a R[a][s]  -  EMV
```

- Unit test: the investment example must return EVPI = 350 (a02).
- Gate: if EVPI <= cost of the cheapest available test, skip all tests and act.
- Cap: expected number of further steps <= EVPI / c (Hay Theorem 5, a08). Use this as a soft guide and keep a hard cap (a12).
- Where an agent has no payoff table (coding, ARC-style puzzles), use a proxy payoff: R = 1 if the final answer is right, 0 if wrong. Then EVPI = 1 - max_h p(h), where h ranges over the candidate answers. This is our arithmetic, not a result from a paper. With this proxy, EVPI is the current error probability, and a test with cost above that error probability is never worth running. The stake term (section 4.6) scales it.

### 4.2 Value of one specific test (EVSI-style, in code)

For test t with outcomes o and likelihoods p(o | h):
```
for each outcome o:  p(o) = sum_h p(h) p(o|h);  posterior p(h|o) = p(h)p(o|h)/p(o)
value(t) = sum_o p(o) * max_a E[R(a) | o]  -  EMV
net(t)   = value(t) - cost(t)
```
- Choose the test with the highest net(t). Stop if max net(t) <= 0.
- Do one test at a time. After each result, update the posterior in code and recompute (K02, a04).
- Dong 2026 uses exactly this rule with a cost per question, with beliefs elicited from the LLM, and no tuned threshold (c02).

### 4.3 EIG ranker over an explicit hypothesis set (the working LLM recipe)

Used by UoT, BED-LLM, Kobalczyk, LIPS, OPEN.

1. Build a hypothesis set H (candidate answers, rules, diagnoses, solutions). Closed set: given. Open set: sample from the LLM, reject any that conflict with past answers, keep survivors between turns, add new ones in diverse batches (BED-LLM, d11).
2. Weights: uniform over survivors. Model log-probability weights did worse than uniform in Kobalczyk (b19: GPT-3.5 4.1 vs 6.2). BED-LLM also imposes uniform weights (d11). Keep belief state in code, not in the prompt: in-context belief tracking scored 25 vs 93 on Animals with GPT-4o (d11).
3. Candidates: the LLM proposes k candidate tests or questions (k = 5 to 10; LIPS: best-of-5 near human mean, best-of-10 above it, a22).
4. For each candidate q, ask the LLM (or run code) for the answer under each hypothesis: a(q, h). Group hypotheses by answer.
5. EIG(q) = H(prior over H) - sum_answers p(answer) H(posterior | answer). For a yes/no question the maximum is 1 bit at an equal split; for n options the maximum is log n (a26). With uniform weights and deterministic answers, EIG reduces to the entropy of the answer partition. This is the "Split" rule in BED-LLM, which halves the sampled hypotheses (d10).
6. Drop candidates with EIG = 0 before ranking (a23: 33-40% of valid sampled programs).
7. Rank by EIG - c(q) (a26 states this utility; its experiments rank by EIG alone).
8. Ask the best. Update the hypothesis set from the answer by rejecting conflicting hypotheses. Repeat.
9. When one hypothesis is left, ask a confirming question ("Is it X?") (d11).

**Failure checks.** Estimators of EIG are biased at finite samples (a14). Compare candidates using the same sample size and seeds. Check rank stability across resamples (K18).

### 4.4 UoT tree (look-ahead variant)

(a18, a19, c08)
- Build a small tree: candidate questions at each node, simulated yes/no answers as branches, depth 3.
- Leaf reward is the information gain over the live candidate set. Binary: IG = -pA log pA - pN log pN. Scaled to [0,1] so it peaks at an even split.
- Propagate reward up the tree: expected reward over answer branches, accumulated along the path.
- Prune low-reward branches. Pruned UoT at 4.7k tokens reached 48.1/88.4/63.2 on 20Q/MD/TB; unpruned at 9.2k reached 54.4/92.5/66.0 (c08).
- Cost: the simulation uses many LLM calls. Depth was limited to 3 for budget reasons. No cost term in the reward (a18).

### 4.5 Metalevel selection of thinking steps

(a07-a12, a16)
- Treat each possible computation (a sample, a verification, a search expansion) as a test. Its value is the expected improvement of the final choice. Its cost is tokens.
- Myopic rule: do the computation with the highest one-step net value. It stops early (Thm 7 says: if it continues, optimal continues; the converse fails).
- Blinkered rule: look 2-3 computations along one option, then decide to stop. Beats myopic in the theory (a10). Practical default: before concluding "stop", score a bundle of 2-3 tests (K03).
- Go result: allocate samples by value of information, stop when the value falls below c = 1e-6; 64% win rate at 10,000 samples per ply (a11).
- ExTS (2026) treats tree expansion as a VOI decision: a virtual child competes with the best real child. Removing the virtual child cut HotpotQA prompt-optimisation accuracy by 3.2 points (64.89 to 61.67) (d13).

### 4.6 Stake-weighted gate

(Dong d21; Zhang d23; K33)
- Gate: run the check when stake x P(error) > cost of the check. Stake = loss from a wrong answer.
- Verifier example: a read-only final-answer verifier rejected 61% of invalid Retail episodes and withheld 17% of valid ones at under one cent per episode; at high liability it captured almost all the benefit of the full stack (d23).
- Dong's case study: at c = 0.05 the same rule asked longer at reward 10 than at reward 1. A single confidence threshold cannot do this (c04, d21). One instance, not a rate.

### 4.7 Proxy gates for expensive checks (SAG)

(c15, c16)
- Proxy for VoI of a critic call: action-distribution entropy and top-2 margin. Call the critic only if both signal ambiguity. A Bayes-optimal threshold lemma says call the critic when expected gain exceeds cost.
- Results: ALFWorld 78.3% at 56k tokens, always-on 74.2% at 341k, always (no gating) 62.0% at 282k (critique). Always-on critique can be worse than gated, not only costlier.
- Margin matters more than entropy: removing margin 74.6, removing entropy 77.6.
- Caveat: the actor was also fine-tuned online. The gate is only part of the gain.

### 4.8 Stopping a run of repeated samples

(b26, b27, d14-d18)
- Adaptive-Consistency: Beta/Dirichlet posterior over the top answer, stop at 0.95.
- ESC: sample in windows of 5, stop when a window agrees, with a maximum size L.
- CGES: stop when the posterior of the top answer reaches gamma (0.7-0.9999 swept), hard budget 16.
- Certified SC: e-value martingale and Ville's inequality; the guarantee holds at the random stopping time; assumes conditionally independent samples.
- ReASC: weight each sample by its own confidence, so a single confident sample can end the run.
- CoT + program agreement: two different reasoning modes agreeing is a stronger stop signal than two same-mode samples.
- All of these stop on agreement, not on expected gain. None is compared to an EVPI/c cap (critique gap 8).
- Guardrail link. G4 says samples from one model are not independent. These rules assume exchangeable draws (b26 limits), so a confident wrong stop is possible. The Di Gioia test found 5 of 5 zero-entropy cases wrong (d02).

### 4.9 Cheap VoI estimation

(b01, b02, b07)
- Nested Monte Carlo is exact in theory and too slow. Regression shortcuts give similar answers in seconds on one parameter.
- They break when the parameter set is large, inputs are correlated or net benefit is nonlinear.
- Rule for the agent: score tests over a few named unknowns, with a small sampled hypothesis set. Scoring must cost far less than the test.
- Report VoI to one or two decimals only (b01) and show it as a range (K32).

### 4.10 Decision-theory scaffold

(c25, d19)
- DeLLMa: list states, forecast their probabilities, elicit utilities by pairwise ranking, choose the action with the highest expected utility.
- The state-forecast ablation (GPT-4) gave uniform 58.3, underspecified 55.0, overspecified 56.7, full 60.0 (d19).
- It has no question-asking step. It is the payoff-table half of a VoI calculation.

---

## 5. What holds up

### 5.1 Robust (several independent sources)

- **Code-side EIG selection beats model-chosen questions** on closed hypothesis sets. Seven independent sources; gains of 8 to 38 points across tasks, with the largest gains for weaker models and explicit candidate lists (K06, K07).
- **Explicit hypothesis-set machinery matters.** Plain in-context belief tracking collapsed (25 vs 93, d11). Entropy-only or model-judged "most informative" questions fell well below full EIG on harder sets (b17, d10).
- **Gain shrinks with model strength** (K08): Kobalczyk GPT-4o-mini gap 1.9 (about 1 SE); Hartmann 14B +4.2 and +1.8; MedClarify GPT-5.1 +2.3 vs R1 +7.8. Four independent sources.
- **Ungated asking can hurt; gated asking helps** (K13): MediQ -11.3% relative for free asking; gate +22.3%. Dong 2026 shows an inverted-U against fixed round counts.
- **Cheap agreement-based stopping of repeated samples** saves 33% to 84% of samples on easy and medium items with under 1 point loss (K17, K29, five sources).
- **Estimators of VoI are costly and biased** (K18).
- **LLM beliefs are weak inputs** (K19).

### 5.2 Failures, tensions and boundary conditions

| Tension | What each side found | Reading |
|---|---|---|
| Stronger model, smaller gain vs large UoT gains on GPT-4 | Kobalczyk a28 vs Hu a19 | Probably closed vs open sets and dataset. No single study tests it (critique). |
| Log-prob weighted EIG hurt; uniform helped | Kobalczyk b19 | Estimator differences. BED-LLM says Kobalczyk's EIG implementation was weaker (b19 limits). |
| BED-LLM reimplemented by others fell below baseline | Hartmann d06: 14B Animals 26.4 vs base 35.0; original paper reports large gains (d10) | Reimplementation risk is real. Small samples (5 episodes, SE up to 4.8). |
| Free asking hurts (MediQ) vs asking helps (UoT, Kobalczyk) | b22 vs a19, a27 | Structured selector or gate vs ungated prompting. Nobody ran all arms together. |
| Reasoning mode vs question quality | Reasoning on lowered the base questioner's solve rate in every category (d07); an R1 agent still gained +4.3 from a trained clarifier (d05) | Reasoning does not replace a selector. No clean test with 2026 reasoning models. |
| Calibrated confidence vs VoI | Calibration does not give the benefit of retrieval (c18, d24); confidence-weighted agreement stops earlier at equal accuracy (d17); sampled agreement missed 5 of 5 confident errors (d02) | Confidence helps to stop repeats of the same test; it does not price a new kind of test. Contested (K15). |
| Info gain vs probability gain | Humans: probability gain (b09, d22). LLM papers: info gain only. | Not tested for LLMs (K20). |
| Simulation vs real LLM for the same stop rule | Simulation: +33 points over greedy (d01). Real GPT-4.1: net-VOI U 2.20 vs always-retrieve 5.33 (d02) | The real-LLM belief proxy was weak; the author calls it illustrative. |
| Tuned baselines decide who wins | UoT 60.4 to 90.1 on 20Q with two hyper-parameters (d08) | Report tuned and untuned baselines. |
| More tests vs interior optimum | tau-bench plateau (d05); fixed K=3 worse than greedy (d01) | Use a hard cap (K30). |
| Look-ahead | 75.0 vs 30.2 on a built test; 32.7 vs 29.7 on a natural one (d07) | Depth pays only when tests complement each other (K27). |

### 5.3 Moderators

- **Model strength**: weaker models gain more.
- **Hypothesis set**: closed or nameable beats open (a20, d11).
- **Task difficulty**: stopping rules save least on hard items (MATH -33.8%, GPQA -2.1 points with little saving; d14, d18). Token-cost training cuts easy items more than hard ones (a17).
- **Domain**: RaM savings are smaller on physics and engineering (b25 limits).
- **Number of candidates**: EIG max is log n; gain needs variety in answers.
- **Answerer noise**: all LLM studies use simulated answerers (GPT-4 in UoT, LLM oracles in Kobalczyk, LLM patients in MediQ). Real users or real tools may differ.
- **Cost level**: VoI beats a tuned threshold at some cost levels and is comparable on GPT-4 for some tasks (c03 limits).

### 5.4 What worked and what did not (interventions)

Worked:
- Code ranks, model proposes (UoT, LIPS, OPEN, Kobalczyk, BED-LLM, CA-BED, MedClarify).
- Explicit candidate list with rejection by past answers (d11).
- Confidence gate on asking (b22).
- Net-value stop with cost per question (c02, c03).
- Entropy plus margin gate on an expensive critic (c16).
- Pruned tree at lower tokens (c08).
- Value-per-budget action scoring under hard caps (d03, d04).
- Agreement-based stopping of repeated samples (b26, b27, d14-d18).
- A read-only verifier with a stake term (d23).
- Training for questions (EIG rewards, DPO), though outside the scaffold (K22).

Did not work or hurt:
- Letting the model ask whenever it likes (b22).
- Chain of thought or planning prompts around the test choice (UoT text, a21; QuestBench, c11, d20).
- Asking the model which question is most informative (implicit max; d10).
- Log-probability weighting of hypotheses (b19).
- Plain in-context belief tracking (d11).
- A sampled-agreement proxy for VoI of retrieval (d02).
- Entropy-threshold stopping with greedy selection: +3.4 only (d01).
- Fixed number of tests (d01, d05).
- Plain fine-tuning that raised EIG but lowered success (b23).
- Visual input in Battleship (GPT-4V, a23).

---

## 6. Language models

### 6.1 How models behave without a selector

- **They do not know what is missing.** QuestBench (Li, Kim, Wang 2025; models up to o1-preview and Gemini 2.0 Flash Thinking): Logic-Q and Planning-Q under 50%. On Planning-Q, models said "not sure" in 0.7% (GPT-4o), 1.4% (Gemini Flash Thinking) and 4.6% (Claude 3.5) of cases when the true share was 41.8%. At most 5 points above random. CoT and few-shot gave no significant gain. Restricting to problems the model could solve fully specified did not fix it (b20, b21, c11-c14, d20). Models do arithmetic well (GSM-Q, GSME-Q above 80%) but not the "what is the one missing fact" step.
- **They answer early.** Laban et al. 2025: -39% average, 15 LLMs, 200,000+ simulated conversations (a31). They rely on early assumptions and do not weigh one more question.
- **They propose uninformative tests.** In Battleship, 33-40% of valid sampled programs had zero EIG; single samples averaged 0.65-0.66 bits against a human mean of 1.27 (a22, a23).
- **Their beliefs drift.** Off-the-shelf LLMs show little belief improvement after round 1 (b28). Stated probabilities were only fairly calibrated and worse in medical (c06). Bandit exploration failed without outside summaries (b29).
- **Free asking is unreliable.** MediQ direct asking cut accuracy 11.3% relative (b22).

### 6.2 What changed behaviour, and by how much

| Intervention | Task | Result | Source |
|---|---|---|---|
| UoT (EIG tree, depth 3) | 20Q, DX, MedDG, FloDial, troubleshooting | +38.1% avg success vs direct; Llama3-70B +46.6; GPT-4 FloDial 43.7 to 67.3 | a19, a20 |
| BED-LLM (sample, filter, EIG) | 20Q, 6 models, 100 targets per set | +37.4 points avg; never decreased in any setup; GPT-4o Animals 45 to 93; Mistral-Large Celebrities 19 to 91 | b16, d10 |
| Split rule (halve hypotheses) | same | Animals GPT-4o 83, Mistral-Large Celebrities 63; BED-LLM 5 to 30 points above it | d10 |
| Kobalczyk EIG over sampled solutions | HumanEval (48 tasks), APPS (47 tasks) | GPT-3.5 binary round 4: 70.8 to 85.6; open 75.9 to 85.0; Llama3-8B open 64.8 to 75.5 (this cell is APPS table per critique); GPT-4o-mini binary 79.6 to 81.5; open 83.5 to 83.8 | a27, a28, b18, critique |
| LIPS best-of-k by EIG | Battleship, 18 boards | k=5 near human mean; k=10 above (p<0.001, p=0.01) | a22 |
| OPEN (BED chooses, LM words) | preference elicitation, 39-48 users per condition | beat LM-only and design-only | a25 |
| GATE (LM asks, no EIG) | 388 participants | beat user prompts in 6 of 10 (absolute) and 7 of 10 (AUC) settings | a24 |
| MedClarify (LLM-simulated EIG) | 469 cases | top-1 +4 to +8 over naive; +26.9 over single-shot; questions per case 8.96 vs 9.81; ECE 0.37 to 0.16 | d09 |
| CA-BED (EIG through depth-2 conversation tree) | Detective Cases, 20Q | +21.8 points avg over direct at +1.8 turns | d08 |
| Trained clarifier (EIG belief-shift reward) | tau-bench, 5 agents | +3.7 avg; R1 +4.3; asked 1.3 questions | d05 |
| Amortised EIG training | 20Q Qwen2.5 | 7B x2.8; 14B +4.2 and +1.8 | d06 |
| AR-BED training | MediQ dermatology, Cube-NM | 90.5% to 94.7% dermatology; 75.0 vs 30.2 two-step vs one-step | d07 |
| Confidence gate on asking | MediQ | +22.3% over BASIC | b22 |
| Dong VoI gate | 4 domains, GPT-4.1, Gemini-2.5-Flash | 18 of 20 conditions won or tied vs tuned baselines | c02 |
| SAG critic gate | ALFWorld | 78.3% at 56k tokens vs 74.2% at 341k always-on | c16 |
| Value-per-budget action scorer | multi-hop QA, 3 backbones | best F1 in 7 of 16 cells (Qwen3-32B); -27.2% wall time vs BAVT | d03 |
| RaM token cost | 3 models | -23 to -45% tokens, similar accuracy; training needed | b25 |
| Agreement stopping | many datasets | -33% to -84% samples, under 1 point loss | b26, b27, d14-d18 |
| DeLLMa scaffold | agriculture, stocks | 73.3% / 64.2% vs o1-preview 33.3% / 35.0% | d19 |
| KnowNo conformal ask | robot planning | -10 to -24% human help | a30 |

### 6.3 Trends by model generation

- Most models are 2023-2024 vintage. Claim: QuestBench-type failures may be weaker with 2026 reasoning models, but no scored model after o1-preview exists in that benchmark (d20).
- MedClarify with GPT-5.1: +2.3 only. Fang 2026 gains smaller on GPT-5.4-Mini than on Qwen3-32B (K08).
- Turning reasoning on in the base model made the base questioner worse (d07).
- A DeepSeek-R1 agent still gained from clarification (+4.3, d05).
- Best reading: gains shrink but do not vanish for stronger models. The size for 2026 frontier reasoning models on QuestBench-type tasks is unmeasured.

### 6.4 Cost of using the method

- UoT: pruned version about half the tokens of the full tree for 5 to 6 points less on the first two tasks (c08).
- BED-LLM: 25x to 36x slower than base in wall clock (d06); AR-BED reports 2376 s per game for BED-LLM vs 38.9 s for the amortised policy (d07).
- CA-BED: +1.8 turns; token cost "substantial", not reported (d08).
- A 4.7k-token pruned UoT beats a 4.5k-token CoT-SC by 15.5 points on 20Q (48.1 vs 32.6) (c08).

---

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory. Status [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Code computes the bound.** Before any test, code computes EVPI (or its proxy, current error probability) and skips tests that cost more than it. Unit-test the routine on the 350 example. | G5, S4/S7 | [E] | a01-a04, c01, d25; K01 |
| A2 | **One test at a time, recompute after each result.** Never add the values of two tests. | S4/S7 | [E] | a04, b11, d25; K02 |
| A3 | **Code selects, model proposes.** For test or question choice over an explicit hypothesis set: the model proposes 5 to 10 candidates and words them; code ranks by information gain (or the cheap halving rule) and picks. Do not ask the model which test is most informative. | G5, S4 | [E] | a19, a22, a25, a27, a29, b14, b16, b18, c07, c21, c24, d10; K06 |
| A4 | **Keep the hypothesis set and beliefs outside the model.** Candidate list in code; reject candidates that conflict with observed results; uniform weights; not model log-probabilities; not in-context belief tracking. | G5, memory | [E] | b17, b19, d10, d11, b28, c06, b29; K09, K19 |
| A5 | **Filter zero-information tests in code** before ranking. | G5, S4 | [S] on the 33-40% rate (one paper); the principle follows from A3 | a22, a23, c23; K10 |
| A6 | **Gate asking and extra tests; never free-run them.** Ungated asking hurt (-11.3% relative); gated recovered it. Add a hard cap (about 1 to 3 clarifying questions; test 2, 4, 8 for evidence checks). | S4/S7, G7 | [E] for gating; cap value [S] | b22, c05, d05; K13, K30 |
| A7 | **Include a cost term and a stake term in the gate.** Run a check when stake x error probability exceeds its cost. | S4/S7 | [E] for the principle (K21, K33); the threshold rule is [S] (K14) | a13, a18, a26, c02, d21, d23; K21, K33 |
| A8 | **Do not trust the model to say what is missing.** Code enumerates required slots or unknowns and counts unfilled ones. Model self-report of "not sure" is not a signal. | G1, S0/S1 | [E] direction (consistent with G1); the numbers [S] | b20, c13, d20, a31; K11, K12, K31 |
| A9 | **Stop repeated samples on agreement with a hard cap.** Posterior >= threshold or window agreement, hard cap 16. Use for same-test repeats only. Save least on hard items. | S7, G7 | [E] | b26, b27, d14-d18; K17, K29 |
| A10 | **Do not use model confidence as the value of a new test.** It may stop repeats; it does not price a new kind of test. Already in 4b ("verbal confidence to stop"); extend with the retrieval result. | G1, 4b | [C] for the full claim; [E] for "stated confidence is not enough" | c18, d02, d24; K15 |
| A11 | **Keep scoring cheap.** Few named unknowns, small sampled set, same samples across candidates; scoring cost far below test cost. | S4 | [E] | a14, b01, b02, b07; K18 |
| A12 | **State the risk-neutral assumption** in the schema; make no claim for risk-averse payoffs. | S4 note | [E] (as a limit) | a04, d25; K34 |

### Test first (not yet established; see UNKNOWNS.md)

| # | Item | Schema part | Status | Evidence | Why not add now |
|---|---|---|---|---|---|
| T1 | EVPI-based cap on number of tests: min(hard cap, EVPI/c) | S4/S7 | [S] | a08, a12, K04 | Theory only; no LLM test |
| T2 | Payoff gate (net VoI > 0) beats information-gain ranker alone and a tuned confidence threshold, at equal tokens | S4/S7 | [S] | c02, c03, d01, d02 | No study runs all three arms; the real-LLM proxy lost to always-test |
| T3 | Look-ahead of depth 2 only for complementary tests | S4/S7 | [S] | d07, d08; K27 | No natural-task depth ablation; no token price |
| T4 | Uncertainty-proxy gate (entropy + margin) for the critic or verifier at S8 | G1, S8 | [S] | c15, c16, d23; K16 | One benchmark; actor also fine-tuned |
| T5 | Probability gain as an alternative score | S4 | [C] | b09, d22; K20 | Humans only |
| T6 | Explicit "none of these" hypothesis and a broadening move when the fit check fails | S2/S4 | [S] | d11, d12; K28 | Nobody measured how often the true answer is missing |
| T7 | Predicted-gain vs realized-gain log per test, to learn which VoI estimates are trustworthy | memory, S9 | [S] | d02, d19; K32 | LLM-elicited EVPI never validated |
| T8 | Forced ask-or-answer decision step at S0/S1 on underspecified tasks | S0/S4 | [S] | a31, b20; K12 | Observed failure; no tested fix |
| T9 | EIG ranker by model strength (apply only when the base asker is weak or stakes high) | S0/S4 | [S] | a28, d06, d09; K08 | Interaction not measured on our models |
| T10 | Stop rule for noisy tests: agreement vs EVPI/c cap | S7, G7 | [S] | K29, K04 | No comparison exists |
| T11 | Value-per-budget action scorer for choosing retrieve/decompose/answer | S4/S7 | [S] | d03, d04 | Heuristic features; one budget level in ablation |
| T12 | Two-stage design: cheap EIG ranker plus payoff gate | S4+S7 | [E] in principle (K21), untested in a scaffold | a13, a18, a26 | No test of the combined design inside a token budget |

**Fit with the schema.**
- S4 currently says "run every candidate on the check". VoI adds: when tests are costly or choices are about what to ask, rank and gate them. Where candidates are cheap to run, run all (existing rule). VoI applies to expensive checks, clarifying questions and external lookups.
- S7 already has a "counterexample search": run the one input where two rules differ. That is a VoI-maximising test (an even split between the two rules). Note this link; it explains why the schema's discriminating test is the right move and gives a way to rank several discriminating inputs by split size.
- G7 (the schema must pay for itself): VoI is the formal version. Every test pays only if its net value is positive.
- G12 (spend by difficulty): the EVPI proxy (current error probability) is a per-problem budget signal. Problems with high current error get more tests.
- 4b "verbal confidence to stop": the retrieval results (c18, d02, d24) strengthen the entry.

---

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup, scoring and test calls all counted, per G7). Report with 95% confidence intervals; at least 3 seeds; at least 100 items per cell where possible (UoT used 3 repeats and no intervals; the critique flags this). Use a tuned and an untuned baseline.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Hypothesis-elimination tasks (20-Questions style, diagnosis-style, rule discovery) with a closed candidate list | A: model picks next question. B: model proposes 5, code ranks by EIG. C: model proposes 5, code ranks by halving rule (Split) | success at 20 turns (or fewer); turns to solve | B and C beat A by 10 to 40 points for small models; B vs C within about 5 points (d10) |
| B2 | Same, with a strong model | Same arms | success; gain per model size | Gain under 5 points for the strongest model (K08) |
| B3 | Open-target version: no list | A: in-context belief. B: sampled, filtered, uniform-weight set. C: B with an added "none of these" hypothesis and broaden-on-failed-fit | success; log whether the final answer was ever in the set | B beats A by 30+ points (d11); C beats B when the true answer is outside the model's prior |
| B4 | Underspecified task prompts (coding, planning, QuestBench-style) | A: free-form. B: forced ask-or-answer step. C: code-enumerated required slots, ask for any unfilled | accuracy; fraction asked when truly underspecified; false-ask rate | C detects missing info well above the 0.7-4.6% rate of self-report (K11) |
| B5 | Tasks with two stake levels and a per-question cost | A: ask until confident (threshold tuned on held-out). B: ask while net VoI > 0. C: B with EVPI cap | utility = reward - cost; questions asked per stake level | B matches or beats A on utility without tuning; B asks more at high stake (K14) |
| B6 | Mixed test lists on our bench (e.g., ARC-style programs, multi-step QA) | A: run all tests. B: run tests in EIG per cost order, stop when net value < 0. C: B with cap = min(16, EVPI/c) | accuracy at equal tokens; tests run per solved item | B and C match A at 20 to 50% fewer tests; C avoids runaway runs |
| B7 | Test choice where steps are complementary | A: one-step. B: depth-2 look-ahead | accuracy and tokens per point gained | B wins only on complementary tasks (K27) |
| B8 | Repeated-sample items of mixed difficulty | A: fixed N. B: agreement stop with cap 16. C: B plus EVPI/c cap | accuracy; tokens; per-difficulty split | B saves 30 to 80% on easy items, little on hard (K29); C no worse than B |
| B9 | Items with an expensive critic or verifier | A: always-on. B: gated by entropy + margin. C: never | success; tokens; critic calls | B matches A at a fraction of tokens (K16) |
| B10 | Any bench task using VoI estimates | log predicted gain and realized gain per test | rank correlation between the two | Positive but modest; if near zero, VoI estimates are not usable (K32) |
| B11 | Compare ranking scores | A: info gain. B: probability gain. C: payoff-based net value | final accuracy; tests per solved item | Differences on the cases where they disagree; unknown size (K20) |
| B12 | Zero-information filter | A: rank all proposals. B: drop EIG = 0 first, k = 1, 5, 10 | accuracy; tests wasted | B better at fixed tokens; 33-40% of proposals dropped (K10) |

For B1, B3, B5 and B10 also record how many proposals had zero EIG and whether any run exceeded the hard cap.

---

## 9. What does not transfer, and why

- **Information avoidance and non-instrumental curiosity** (b12, b13). These rest on emotions and utility from information itself. An LLM agent has no such stakes. The never-negative rule is safe for the agent.
- **Human probability-gain preference** (b09, d22). It arises with human learning from experience and from classification-accuracy goals, which favour probability gain by design. Its use for LLMs is untested.
- **Health-economics EVPI practice** (b04-b07). The population size, willingness-to-pay and funder context do not exist in our tasks. Only the form "EVPI above cost is necessary, not sufficient" carries over.
- **Closed 20-Questions results.** They need an explicit hypothesis list and a clean yes/no elimination. UoT notes that incomplete elimination is not handled (c07). Open tasks and free-form tests (writing, design) lack both.
- **Exact payoff tables.** EVPI needs a payoff matrix and priors. For coding or ARC the table is "right or wrong", and priors come from the model. Elicited priors are weak (b28, c06) and the sampled-agreement proxy failed on confident errors (d02).
- **Training-based gains** (RaM, EIG rewards, STaR-GATE, DPO, AR-BED). We do not train. Use them only as an upper reference for what a prompt-only ranker should reach (K22). Training rewards also use the ground-truth goal, which an agent at run time lacks (d05).
- **Simulated answerers.** Results with GPT-4 as answerer or patient may flatter the method (UoT checked 10% of answers). A real tool or real user may answer differently.
- **Go and bandit models** (a09, a11). Proven only for one-armed Bernoulli and 9x9 Go. Language tests have uneven costs and dependent outcomes.
- **Conformal guarantees** (a30). Need exchangeable calibration data; fail under shift and in multi-step planning.
- **Multi-LLM Bayesian orchestration** (c17). Single author, one task, attribution percentages over 100. Do not use.
- **Risk-averse case.** Not opened (K34). We assume risk neutrality.

---

## 10. Open questions

1. Does a payoff-based gate (EVPI cap plus net value minus cost) beat an information-gain-only ranker and a tuned confidence threshold at equal tokens, on closed and open tasks? No paper runs all three (critique gap 1).
2. How much of the EIG gain survives with 2026 reasoning models on QuestBench-type tasks? Partly closed: gains shrink (d06, d09), but no score exists for any post-o1-preview model (d20).
3. For open hypothesis sets, how often is the true answer missing from the set, and how wrong can the set be before EIG ranking turns harmful? Nobody has measured (K28).
4. Can an agent build a usable payoff table and prior in free-form tasks? Does an LLM-elicited EVPI predict the realized gain of one more test? Never tested (K32).
5. Information gain vs probability gain vs impact for LLM test choice. Humans favour probability gain; no LLM study compares them (K20).
6. How much does a 2- to 3-test look-ahead beat one-step in natural LLM tasks, and what does it cost in tokens? Only a constructed test and a small natural gap exist (K27).
7. Does stated or sampled uncertainty predict, item by item, which cases gain from another test? Contested (K15).
8. Best stopping rule for noisy tests: agreement vs EVPI/c, and what hard cap prevents unbounded runs? None compared (K29, K04).
9. What do Howard (1966) and Raiffa-Schlaifer (1961) prove about nonadditivity and the risk-averse case, and does it matter for an agent? Not opened (K34).
10. How does a gain measured with an LLM answerer carry over to real tools? Everything is simulated.
11. Can a true EIG beat the Split (halving) rule enough to justify its cost on our tasks? In BED-LLM the Split baseline already gets much of the gain (d10).
12. Does the gate need a separate component per decision type (ask, retrieve, critique, stop)? Different papers use different proxies (c16, d03, c02).

---

## 11. Sources

[V] = opened and read this session (full text, HTML or abstract page as noted). [M] = snippet, abstract or secondary mention only.

**Theory and history**
- [V] Wikipedia, Expected value of perfect information. https://en.wikipedia.org/wiki/Expected_value_of_perfect_information (a01-a03, c01, d25)
- [V] Wikipedia, Value of information. https://en.wikipedia.org/wiki/Value_of_information (a04, a05, d25)
- [V] Wikipedia, Bayesian experimental design. https://en.wikipedia.org/wiki/Bayesian_experimental_design (a15)
- [M] Howard (1966), Information value theory, IEEE Trans. Systems Science and Cybernetics 2(1):22-26. https://ieeexplore.ieee.org/document/4082064 (page returned empty)
- [M] Raiffa and Schlaifer (1961), Applied Statistical Decision Theory (no URL; cited via c26)
- [M] Claxton et al. (2002), A rational framework for decision making by NICE, Lancet. https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(02)09832-X/abstract (paywalled)
- [V] Hay, Russell, Tolpin, Shimony (2012), Selecting Computations: Theory and Applications. https://arxiv.org/abs/1207.5879 (a07-a12; re-opened by the checker)
- [V] Rainforth, Foster, Ivanova, Bickford Smith (2024), Modern Bayesian Experimental Design. https://arxiv.org/abs/2302.14545 (selected passages)

**Health economics and estimation**
- [V] Heath, Manolopoulou, Baio (2015), A review of methods for the analysis of the expected value of information. https://arxiv.org/abs/1507.02513
- [M] Thorn, Coast, Andronis (2016), Interpretation of the EVPI in health economic evaluations. https://pubmed.ncbi.nlm.nih.gov/25986471/
- [M] Tuffaha, Gordon, Scuffham (2014), Value of information analysis in healthcare. https://pubmed.ncbi.nlm.nih.gov/24650041/
- [M] Brennan, Kharroubi, O'Hagan, Chilcott (2007), Calculating partial EVPI. https://pubmed.ncbi.nlm.nih.gov/17761960/

**Human information search**
- [M] Nelson (2005), Finding useful questions. https://pubmed.ncbi.nlm.nih.gov/16262476/
- [M] Nelson, McKenzie, Cottrell, Sejnowski (2010), Experience matters (abstract: https://pubmed.ncbi.nlm.nih.gov/20525915/); [V] full text in d22 via PMC (https://pmc.ncbi.nlm.nih.gov/)
- [M] Wu, Meder, Filimon, Nelson (2017), Asking better questions. https://pubmed.ncbi.nlm.nih.gov/28318286/
- [M] Meder, Nelson et al. (2018), Towards a theory of heuristic and optimal planning for sequential information search. https://europepmc.org/search?query=Towards%20a%20theory%20of%20heuristic%20and%20optimal%20planning%20for%20sequential%20information%20search
- [M] Bastardi and Shafir (1998), On the pursuit and misuse of useless information. https://pubmed.ncbi.nlm.nih.gov/9686449/
- [M] Golman, Hagmann, Loewenstein (2017), Information avoidance. https://doi.org/10.1257/jel.20151245

**LLM studies (information gain and question asking)**
- [V] Hu et al. (2024), Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (re-opened by the checker)
- [V] Grand, Pepe, Andreas, Tenenbaum (2024), Loose LIPS Sink Ships. https://arxiv.org/abs/2402.19471 (re-opened)
- [V] Li, Tamkin, Goodman, Andreas (2023), Eliciting Human Preferences with Language Models. https://arxiv.org/abs/2310.11589
- [V] Handa et al. (2024), Bayesian Preference Elicitation with Language Models. https://arxiv.org/abs/2403.05534
- [V] Kobalczyk, Astorga, Liu, van der Schaar (2025), Active Task Disambiguation with LLMs. https://arxiv.org/abs/2502.04485 (re-opened)
- [V] Piriyakulkij, Langenfeld, Le, Ellis (2024), Doing Experiments and Revising Rules. https://arxiv.org/abs/2402.06025
- [V, abstract-level record] Piriyakulkij, Kuleshov, Ellis (2023), Active Preference Inference. https://arxiv.org/abs/2312.12009
- [V] Choudhury et al. (2026), BED-LLM. https://arxiv.org/abs/2508.21184 (tables partly garbled)
- [V] Li et al. (2024), MediQ. https://arxiv.org/abs/2406.00922
- [V] Li, Kim, Wang (2025), QuestBench. https://arxiv.org/abs/2503.22674
- [V] Laban, Hayashi, Zhou, Neville (2025), LLMs Get Lost in Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (re-opened)
- [V] Mazzaccara, Testoni, Bernardi (2024), Learning to ask informative questions. https://arxiv.org/abs/2406.17453
- [V] Andukuri et al. (2024), STaR-GATE. https://arxiv.org/abs/2403.19154
- [V] Zhang, Knox, Choi (2025), Modeling future conversation turns. https://arxiv.org/abs/2410.13788
- [M] Wang, Zollo, Zemel, Namkoong (2025), Adaptive elicitation of latent information. https://arxiv.org/abs/2504.04204 (abstract only)
- [V, abstract page] Ding et al. (2026), Whom to Query for What. https://arxiv.org/abs/2602.14279
- [V] Deng et al. (2026), Uncertainty-Aware Clarification in LLM Agents with Information Gain. https://proceedings.mlr.press/v306/deng26l.html
- [V] Hartmann et al. (2026), Amortising Bayesian Experimental Design. https://arxiv.org/abs/2607.03426
- [V] AR-BED (2026), Amortizing Sequential Experimental Design in Reasoning LLMs. https://arxiv.org/abs/2610.20832 (first 100,000 characters)
- [V] Arnould et al. (2026), CA-BED. https://arxiv.org/abs/2606.01182
- [V] MedClarify (2026). https://arxiv.org/abs/2602.17308 (first 100,000 characters)
- [V] Model Discovery Agent (2026). https://arxiv.org/abs/2608.09696 (results tables unread)
- [V] Ren et al. (2023), KnowNo. https://arxiv.org/abs/2307.01928 (critique: PDF did not parse in re-check)

**LLM studies (net-value gates and metareasoning)**
- [V] Dong et al. (2026), Value of Information: A Framework for Human-Agent Communication. https://arxiv.org/abs/2601.06407 (re-opened)
- [V] Di Gioia (2026), Cognitive Friction. https://arxiv.org/abs/2603.30031
- [V] Fang et al. (2026), Inference-Time Budget Control for LLM Search Agents. https://arxiv.org/abs/2605.05701
- [V] Park, Im, Kwon (2026), Selective Critique (SAG). https://arxiv.org/abs/2610.07335 (re-opened)
- [V, abstract page] Chhikara (2026), Evaluating Confidence-Gated Retrieval with Matched Trajectory Replay. https://arxiv.org/abs/2608.26846
- [V, abstract page] Amin (2026), Bayesian Orchestration of Multi-LLM Agents. https://arxiv.org/abs/2601.01522
- [V] Zhang, Xu, Chen (2026), How Do Agent Harnesses Create Value? https://arxiv.org/abs/2609.20474 (abstract and layout)
- [V] Exploit More, Explore Smarter (ExTS) (2026). https://arxiv.org/abs/2608.23848
- [V] De Sabbata et al. (2025), Rational Metareasoning for LLMs. https://arxiv.org/abs/2410.05563
- [V] Liu et al. (2024), DeLLMa. https://arxiv.org/abs/2402.02392
- [V] Qiu et al. (2026), Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523
- [V] Krishnamurthy et al. (2024), Can large language models explore in-context? https://arxiv.org/abs/2403.15371

**Stopping rules for repeated samples**
- [V] Aggarwal et al. (2023), Adaptive-Consistency. https://arxiv.org/abs/2305.11860
- [V] Li et al. (2024), ESC. https://arxiv.org/abs/2401.10480
- [V] CGES (2025). https://arxiv.org/abs/2511.02603
- [V] Certified Self-Consistency (2025). https://arxiv.org/abs/2510.17472
- [V] Saparkhan et al. (2026), Self-Consistency from Only Two Samples. https://arxiv.org/abs/2604.17433
- [V] Kim et al. (2026), ReASC. https://arxiv.org/abs/2601.02970

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 13 established claims: 9 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C12.01-K06** (reworded: the sources support less). UoT, BED-LLM, Kobalczyk, Piriyakulkij and Handa mostly show information-driven questioning beating prompted questions, but in these systems the LLM also supplies the answer likelihoods or probabilities that EIG is computed from (BED-LLM uses LLM predictive probabilities; Kobalczyk EIG-logprobs did worse than plain prompting in some models), and the gain is not universal (GPT-4o-mini HumanEval binary +1.9 within noise; BED-LLM below baseline on Qwen-14B Animals). Corrected claim: Choosing questions by an expected-information-gain criterion (with the LLM proposing candidate questions and supplying the answer probabilities the criterion is computed from) usually beats letting the model pick its own question in 20 Questions, diagnosis, code clarification and preference elicitation, but the gain shrinks or disappears for stronger models and depends on how EIG is estimated.
- **C12.01-K08** (reworded: the sources support less). Kobalczyk GPT-4o-mini gap (79.6 vs 81.5, SE about 2), UoT open-set cells (12.5 to 15.0, 34.2 to 36.9), Hartmann (14B +4.2 and +1.8, BED-LLM 26.4 vs 35.0) and MedClarify (+2.3, +7.8, +4.9) all match, but the budget-control paper says VOI gains are smaller 'in some cells' on GPT-5.4-Mini than Qwen3-32B, not overall, and the Hartmann reward is EIG plus an outcome term. Corrected claim: The gain shrinks or vanishes with stronger models and in open-ended settings: GPT-4o-mini HumanEval binary gap 1.9 points (about 1 standard error); several UoT open-set cells under 3 points; an EIG-plus-outcome-reward-trained questioner gave about x2 on Qwen2.5-7B but +4.2 and +1.8 points on 14B, and inference-time BED-LLM fell below the 14B baseline on Animals (26.4 vs 35.0); MedClarify gained +2.3 on GPT-5.1 versus +7.8 on DeepSeek-R1 and +4.9 on Llama-3.3-70B; the budget-control VOI gain was smaller in some cells on GPT-5.4-Mini than on Qwen3-32B.
- **C12.01-K18** (reworded: the sources support less). Heath et al. concern EVPPI (not EVPI): the 55-minute figure is nested Monte Carlo for a single-parameter EVPPI versus seconds for GP/GAM; the upward-bias remark is about the Strong-Oakley subset method; failure with correlated inputs applies to the restrictive linear/independence shortcuts, GAM is unstable for 6+ parameters and GP slows with more parameters. Corrected claim: Estimating value of information costs compute and is biased: nested Monte Carlo EVPPI took about 55 minutes for one single-parameter estimate versus seconds for GP/GAM regression; nested Monte Carlo EIG estimators are biased for any finite inner sample size (Rainforth); the fast shortcuts are restricted (independence/linearity assumptions deteriorate with correlated inputs, GAM is unstable for larger parameter subsets, GP cost grows with parameters).
- **C12.01-K31** (reworded: the sources support less). AR-BED shows reasoning lowered final solve rate in every category, but only for one small base model (Gemma-4-E4B); QuestBench's 'not sure' rates (1.4, 4.6, 0.7 percent vs 41.8 true) are for Gemini Flash Thinking, Claude 3.5 Sonnet and GPT-4o in the zero-shot no-CoT setting, not o1-preview, and do not compare reasoning on versus off. Corrected claim: Turning on reasoning in the base model did not make it a better questioner in AR-BED (Gemma-4-E4B base: final 20 Questions solve rate fell in every category with reasoning on). In QuestBench, Gemini 2.0 Flash Thinking, Claude 3.5 Sonnet and GPT-4o said 'not sure' on only 1.4%, 4.6% and 0.7% of Planning-Q cases (zero-shot, no chain of thought) where the true rate was 41.8%. Evidence is from one small reasoning base model and 2024-25 frontier models; Gemini 2.5 Pro appears only in qualitative traces; no clean test with 2026 frontier reasoning models.
- **C12.01-K01** (now single-source: only one opened source, code check).
- **C12.01-K02** (now single-source: only one opened source, code check).
- **C12.01-K03** (now single-source: only one opened source, code check).
