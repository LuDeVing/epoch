# Outside view and base rates: deep document

*Subfield E03.04 of forecasting and calibration. Focus: comparison classes as the starting point (Kahneman and Lovallo). Schema link: S0 gate. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K30), critique.md in this folder. Evidence ids (a01 ... d20) point to the evidence files. Today: 2026-10-27.*

**Headline.** The human case for the outside view is strong in direction and weak in measured size. The LLM case is thin: no study isolates a class-lookup step in a strong scaffold. A base-rate prompt line gives at most about 0.01 Brier on frontier models and nothing in the preregistered mixed model. Data-computed class rates are strong. Model-recalled class rates are weak. The "0.17 vs 0.26" line that motivated this row is a standardized, self-tagged, correlational score, not a raw Brier.

---

## 1. What it is

Two ways to forecast one case.

- **Inside view.** Focus on this case. Build a plan or scenario. Extrapolate. Ask "what will happen here?"
- **Outside view.** Ignore the case details at first. Find a class of similar past cases. Take the distribution of outcomes in that class. Then place this case inside it. Ask "what happened in cases like this?" (a01, a08)

Related terms.

| Term | Meaning |
|---|---|
| Base rate | How often the outcome happens in the class. A single number. |
| Reference class | The set of past cases used. Choosing it is the hard step. |
| Reference class forecasting (RCF) | Flyvbjerg's three steps: pick the class, get its outcome distribution, place the project in it. Regress the best guess toward the class mean and widen the interval toward the class interval. (a08) |
| Planning fallacy | Under-estimating own task time, cost and risk while knowing that similar tasks ran late. (d01, a17) |
| Uniqueness bias | Believing the case is so special that the class does not apply. (a16) |
| Base-rate neglect | Using case details and ignoring a known class frequency. (a19, a20) |
| Natural frequency | Counts such as "10 out of 1,000" instead of "1%". |

Why the outside view helps, in one line. The scenario of flawless execution may be more likely than any single failure scenario, yet the many ways to fail add up to more. Picking the most plausible scenario overstates success. The class already contains every way things went wrong, including unknown unknowns. (a25, a17)

For our agent the question is narrow. S0 is the gate that runs before any attempt. Should S0 look up the class of the problem (and a class frequency for the answer), and should the answer then be held near that class? The research below says: probably yes when a real, counted class exists, and no proof that a prompt line alone does it.

---

## 2. History and theories in depth

### 2.1 Founding: Kahneman and Tversky, Kahneman and Lovallo
- **1973 to 1983.** Kahneman and Tversky show that people forecast from the representativeness of case details and under-use known statistics (lawyer-engineer problem, 70/30 vs 30/70). Stated statistics have some effect but less than they should. (a07, a20)
- **1979.** Kahneman and Tversky coin "planning fallacy" and the idea of regressing a forecast toward the class mean (a08, a17).
- **1993. Kahneman and Lovallo, "Timid choices and bold forecasts" (a01-a07, a25).** A theory paper. No experiment. It states the two views and argues the outside view is much more likely to be realistic when both are applied with equal skill. Key pieces:
  - **The curriculum story (Israel, 1976) (a02).** A team estimated 18 to 30 months to a draft. The curriculum expert, asked for similar past teams, said about 40% never finished and none of the rest took under 7 or over 10 years. The project took about 8 years. The expert had known this and had not used it in his own first guess. One team, class recalled from memory, so an anecdote.
  - **Knowing is not using (a03).** The expert's statistical knowledge was not retrieved when he forecast by the inside view. Consensus in the team was not validity. The outside-view facts were demoralising, so the forecast was dropped.
  - **Entrepreneurs (a04, from Cooper et al. 1988).** Over 80% rated their own chance at 70% or better and one third said success was certain. The mean chance for "a business like theirs" was 59%. Real five-year survival was about 33%. Own-venture ratings did not track education, experience or capital. The class estimate was closer, though still optimistic.
  - **Organisational data (a05).** Rand pioneer process plants: almost all construction costs exceeded estimates by over 20%, norm more than double. PIMS: over 80% of start-ups fell short of planned market share.
  - **Why optimism wins contests (a05).** Winner's curse and regression to the mean: the project forecast to be best is the one most likely to fall short.
  - **Class choice (a06).** The class is ambiguous. Try both the firm's own history and the most similar projects elsewhere. Use comparable units such as actual divided by planned. No rule for disagreeing classes. The authors call realism vs morale a real dilemma.
  - **Boundary (a01).** The outside view is conservative. It fails on extreme and exceptional events. It needs a definable class.
- **Calibration oddity (a07).** Item-by-item overconfidence (about 80% correct when "99% sure") coexists with accurate global estimates of total hits. Contested.

### 2.2 Lab: Buehler, Griffin and Ross (1994) (d01-d03)
The experimental base for the planning fallacy. Read in full this session. See sections 3 and 5.

### 2.3 Applied: Flyvbjerg and reference class forecasting (2003 to 2024)
- **2003.** Lovallo and Kahneman, "Delusions of success" (HBR). Practitioner article. The text was not opened by us. A student result is reported second-hand: incoming students expected to beat 84% of peers; a group first asked entrance and peer scores cut its rating by 20%, still overconfident (a11, b08). N and design unknown.
- **2003.** Flyvbjerg comment (a15, d04). Forecast errors stayed the same size for 70 years. Technical, economic, psychological and political explanations were tested; the political one fit best. If forecasts are cooked on purpose, the outside view will be resisted.
- **2006.** Flyvbjerg, "From Nobel Prize to project management" (a08-a11). Defines RCF in three steps and gives the transport overrun data (rail +44.7%, bridges and tunnels +33.8%, roads +20.4%).
- **2004 onward.** UK Department for Transport builds optimism-bias uplifts by class. First live use: Edinburgh tram, October 2004 (a10). Denmark makes RCF mandatory for large rail and road (a24).
- **2016.** Hong Kong roadworks test: local class vs a global benchmark (a12).
- **2016 to 2018.** Hiding Hand debate (a13, a14): are benefit overruns typically larger than cost overruns? Flyvbjerg and Sunstein say only about 1 in 5 projects.
- **2012.** Lovallo, Clarke and Camerer: many similarity-weighted analogies beat a few familiar ones in two field tests (private equity, film revenue). Abstract only; numbers unknown (d05).
- **2024.** Uniqueness bias paper (a16).

### 2.4 Competing theories of why forecasts are optimistic
| Theory | Claim | Evidence |
|---|---|---|
| Psychological (Kahneman and Lovallo) | Inside view and WYSIATI make planners optimistic; learners do not learn from others' failures | Lab planning fallacy (d01), entrepreneur ratings (a04) |
| Political (Flyvbjerg 2003) | Forecasts are cooked under pressure; bias is strategic | Same error size for 70 years; interviews (a15) |
| Case-based judgment (Griffin, Koehler, Brenner) | People weigh evidence for the case and add class data only as far as it looks relevant to the case | Learning study: base rates estimated accurately but not used (a20) |
| Ecological / format (Gigerenzer and Hoffrage) | Minds handle counts from natural sampling, not percentages | Frequency formats raise Bayesian answers (a18) |
| Nested sets (Barbey and Sloman) | Neglect shrinks when set structure is visible, not only when counts are used | Replications of frequency gains are smaller (a19) |

Status: political vs psychological is unresolved and both can hold (K05, contested). For an LLM agent the question that matters is a third one: does the model neglect the class because of its text-prediction nature (it conditions on the prompt, "metacognitive myopia" claim, c24) or because nobody asked? No test separates these.

### 2.5 Base-rate neglect and format (a18-a21, b12-b14)
- Eddy-type medical problems: about 5% (Eddy 1982), 18% (Casscells 1978) and 10% of physicians (Hammerton 1973) gave the Bayesian answer; the usual answer was the test's hit rate (a19).
- Natural frequencies lift this a lot but not to ceiling, and later replications found smaller gains (section 3).

### 2.6 LLM era
- **2023.** GPT-4 with a superforecaster prompt does not beat the crowd (b23).
- **2024.** Halawi et al. retrieval system (a23); Hsieh et al. agent with an explicit "reference classes and base rates" first step (c19); Pratt et al. strategy test (c05); ForecastBench (b17).
- **2025.** Large preregistered prompt test (Schoenegger et al.) finds base-rate wording is at most a small lever (c01-c04, d08). Pitfall paper on base-rate artefacts in evaluation (c11, d20).
- **2026.** Computed class priors (Murphy, d12-d13); Hindcast (d15). Still no isolated S0 ablation (K14).

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single source, **C** contested, **N** note (not a finding about effect).

### 3.1 Human: planning and project data
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Inside-view task-time predictions are too early, even the "worst case" | N=37 honors-thesis students (32 usable). Best guess 33.9 days vs actual 55.5, t(32)=3.43, p<.002. 29.7% finished by best guess. Optimistic scenario 27.4 days (10.8% on time). Pessimistic scenario 48.6 days, still below actual. Best-guess vs actual r=.77 | Buehler et al. 1994, Study 1 (d01) | E (also a22 second-hand; replicated widely in the literature, not re-read here) |
| Recalling past tasks alone does not fix optimism; recall plus an explicit link to the present task does, for the mean only | N=123, 3 conditions x 2 deadlines. Predicted vs actual days: control 5.5 vs 6.8; recall 5.3 vs 6.3; recall-relevant 7.0 vs 7.0. Finished by predicted time: 29.3%, 38.1%, 60.0%, chi2(2)=7.63, p<.01. Absolute error: no effect | Buehler 1994, Study 4 (d02) | S |
| Outsiders over-use the past | N=123 observers. Mentioned the actor's past: 48.0% of observers vs 2.4% of actors, chi2(1,N=164)=48.78. Observer predictions about 8.0 to 8.8 days vs 5.5 predicted and 6.8 actual by actors (columns garbled) | Buehler 1994, Study 5 (d03) | S |
| Task similarity decides whether the past helps | Exp 1 n=40: essay-first group predicted 33.40 min vs actual 30.11; castle-first group predicted 19.70 vs actual 38.14. Told duration: no effect on bias in all 3 experiments | Thomas and Koenig 2018 (b10) | S |
| New firms: own-chance ratings far above class | Over 80% rated own chance 70%+; 1/3 said certain; class mean 59%; real 5-year survival about 33% | Kahneman and Lovallo 1993 citing Cooper 1988 and D&B 1967 (a04) | S (second-hand) |
| Pioneer plants and start-ups | Rand: almost all plants over budget by more than 20%, norm more than double. PIMS: over 80% below planned share | a05, citing Merrow 1981 and Davis 1985 | S (second-hand) |
| PIs over-forecast own trial outcomes | 740 PIs (16.7% response). Brier: trial success 0.25 (CI 0.20-0.30), recruitment 0.38, timeline 0.52. AUC 0.76, 0.64, 0.55. Predictions exceeded observed frequencies | Benjamin et al. 2022 (b11) | S (compared with 50%, not with a class forecast) |
| Experts mispredict AI effect on dev time | 16 developers, 246 tasks. Forecast 24% less time; estimated 20% less after; measured 19% MORE. Economists said 39% less, ML experts 38% less. Per-task forecast vs actual r=.64 and .59 | METR, Becker et al. 2025 (d17) | S |

### 3.2 Human: project classes (the numbers an RCF uses)
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Cost overruns by type (constant prices) | Rail +44.7% (sd 38.4, p<.001); bridges and tunnels +33.8%; roads +20.4%. No improvement over 70 years (cost) and 30 years (demand). Table layout garbled, sd and p uncertain | Flyvbjerg 2006 (a09) | E (large dataset, but one author group; K01, K02) |
| Demand forecasts | Rail passengers -51.4% on average (sd 28.1); 84% off by more than 20%. Roads +9.5% (sd 44.3); half off by more than 20% | a09, b07 | E |
| UK uplifts | Roads (172 projects): 40% overran by at most 10%, 80% by at most 32%. Uplift 15% at 50th percentile, 32% at 80th, 45% at 90th. Rail 40%, 57%, 68%. Fixed links 23% and 55%. Buildings 4-51%, IT 10-200% | a10, b06 | E for the class; no outcome test (see K21) |
| Local vs global class | Hong Kong, 25 roadworks (1993-2011) vs Oxford benchmark of 863 road projects in 34 countries. Cost: benchmark +20%, HK +11% at decision (Cat C), +6% (B), -1% (A). Share overrunning: 9 in 10 vs 7 in 10 (p=.006). Schedule: benchmark +38%, HK +58% (p=.089, ns); late 8 in 10 vs 6 in 10 (p=.048). Duration 8.9 vs 5.5 years (p<.001). Samples 23, 22, 20 per stage | Flyvbjerg, Hon, Fok 2016 (a12) | E that classes differ locally (K03) |
| Costs beat benefits in most projects | 2,062 projects with cost data; 327 with both. Benefit overrun larger than cost overrun in 22% (78% not), p<.0001. By type: dams 18%, rail 17%, tunnels 21%, power 26%, buildings 28%, bridges 38% (p=.22 ns), roads 25%. Cost ratio about 1.39-1.43, benefit ratio 0.83-0.90 | Flyvbjerg and Sunstein 2016; Flyvbjerg 2018 (a13, a14) | E on direction; sample is large public projects, authors are proponents |
| Uniqueness predicts overruns | N=219 IT projects, response 43-64%. +5 points of cost overrun per uniqueness point (robust regression, p=.01). Rating 10: about +45 points. Extreme overrun (76%+): 37% at 10 vs 1% at 1 (p<.001). 19.2% rated highly unique. Tail 23 times Gaussian (16% vs 0.7%) | Flyvbjerg et al. 2024 (a16) | S (correlational, hindsight ratings, working paper) |

### 3.3 Human: tournament and training evidence
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Short probability training (comparison classes, base rates, averaging, models, bias, updating) improves forecasts, randomized | Year 1 standardized Brier: probability-trained n=119 -0.05, scenario-trained n=113 -0.06, control n=152 +0.07, F(2,381)=12.1, p<.001 (about 10% and 11% better). Year 2: trained n=205 -0.10 vs control n=194 +0.05, t(395)=5.95, 12%. Year 3 about 6%, year 4 about 7% | Chang et al. 2016 (b01) | S for the outside view alone (bundle); E for the bundle |
| Comparison-class tag scored best of ten self-tags | Standardized Brier (year 4): comparison classes 0.17 (n=580); math/stat models 0.26 (453); select right questions 0.26 (330); hunt for information 0.38 (2,992); update 0.44 (1,239); post-mortem 1.04 (88); control 0.49 (6,622). ANOVA C: F=12.28, p<.001. Only C, P, O significant | Chang 2016, Tables 5-6 (b02, d06) | S, correlational. Use rank order only |
| Same line as repeated by AI Impacts | "0.17 vs 0.26" as average Brier, outside view 12th of 15 correlates | AI Impacts (b05) | N: drops "standardized"; do not cite as Brier |
| Moderators | Training x ability, motivation, practice interactions unsupported. Practice mediated the effect in 3 of 4 years. Trained 4.1 vs control 3.7 hours/week | Chang 2016 (b04) | S |

### 3.4 Human: format effects on base-rate use
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Natural frequencies raise Bayesian answers | Study 1: 60 students, 15 problems. Bayesian answers 46% and 50% (two menus) with frequencies vs 16% and 28% with probabilities. Mammography: 1%, 80%, 9.6% gives 7.8% | Gigerenzer and Hoffrage 1995 (a18) | E |
| Replications show smaller gains | Cosmides and Tooby 12% (single-event probability) vs 72% (frequencies). Sloman et al. 2003: 51%. Further replication 31%, gain ns. 48 physicians: 10% vs 46% | Barbey and Sloman 2007 (a19) | E (direction), C (size) |
| Same effect in 2023 medical students | N=577. Probabilities 34%; frequencies 68%; probabilities after training 64%; frequencies after training 89% | b13 | E |
| Chaining two tests stays poor | 167 medical + 162 psychology students. One test PPV correct: natural frequencies 36.2% vs odds/LR 21.6% (OR 2.41). Two sequential tests: odds/LR 10.6% vs frequencies 4.9% (OR 2.73) | BMC Med Educ 2025 (b14) | S |
| Knowing is not using | Learners estimated seen base rates accurately; probability judgments and willingness to pay mostly unaffected | Griffin, Koehler, Brenner 2007 (a20) | S (details in papers not opened) |

### 3.5 Language models
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Base-rate-first wording: small gain in t-tests, none in the preregistered mixed model | 100 ForecastBench questions, 4 models. Base Rate First -0.016 (SD .106, N=390, adj p=.036); mixed -0.011 (adj p=.774). Frequency-Based -0.019 (N=370, adj p=.022). Step-Back -0.015. Mean Brier GPT-4o .215, Sonnet .208, Haiku .214, Llama 405B .227 | Schoenegger et al. 2025 (b19, c01) | S |
| Multiple reference classes: nothing | Mixed -0.004 (z=-0.82, adj p=.774); t-test adj p=.233 | same (c02) | S |
| Compound base-rate prompts: nothing, even with o1 and o1-mini | Base Rate First + Frequency -0.012 (N=462, adj p=.162); + CoT 0.000 (adj p=.985); Mandatory Probability + Base Rate Fallback -0.002; mixed-model values -0.004, 0.000, +0.006. Model means: o1 .216, o1-mini .217 | same, Study 2 (c03, b21, d08) | S |
| "Reason as a Bayesian" and Propose-Evaluate-Select hurt | +0.025 (N=388, adj p=.036), +0.028 (N=391); more decisive forecasts (17-20 points from 50% vs about 13) | same (b20, c04) | S |
| Superforecaster conditional odds-ratio prompt hurt | +0.023, adj p=.01 | same (b21) | S |
| Recalled base-rate strategy was the worst of eight | PaLM 2, 351 validation events. Brier: Basic .1221, Human .1334, Base Rates .1562, Both Sides .1553, Breakdown .1895. Weighted: Base Rates .2540 (worst), Human .1746 | Pratt et al. 2024 (c05-c07, d11) | S (one model, mostly-No data) |
| Retrieval system with a late base-rate step | Test Brier .179 vs crowd .149 (accuracy 71.5% vs 77.0%); no fine-tuning .186; no fine-tuning, no retrieval .206 (best zero-shot .208). Crowd between .3 and .7: .199 vs .246. Crowd within .05 of 0 or 1: accuracy +7%, Brier worse by .04 | Halawi et al. 2024 (a23, b15, b16, d09) | S for the step; E for the bundle |
| Agent with reference-class first step and code counting | 201 Manifold questions. Median of 3 .169, mean .170, one run .180, crowd .172, GPT-4o .210. ETH example 80 of 1,003 days = 8% vs another run 30%. Ensemble SD .092 (ReAct) vs .150 (base LMs) | Hsieh et al. 2024 (c19, d10) | S |
| Reference class as step 2 of an 8-step scratchpad | 1,000-question set: GPT-4o scratchpad .147 vs zero-shot .168; Gemini-1.5-Pro .143 vs .147. Superforecasters 0.096 vs best LLM 0.122 (200-question subset) | ForecastBench (b17, d16) | S (bundle) |
| Data-computed class beats recalled class | Empirical prior Brier Index 58.3 vs full search agent 62.7 on dataset questions; paired agent gain +4.5 on data (significant), +2.3 ns on markets. KNN counter (about 270 neighbours, Laplace) 59.1 vs 50.0 always-0.5 on 40 questions | Murphy 2026 (d12, d13) | S |
| Market or crowd anchor helps a lot | GPT-4 .17 to .14 (p=.003); Claude 2 .22 to .15 (p<.001). Market price alone .096 vs best prior LLM system .109; AIA with search and price .075, search without price .085, no search .116 | Silicon Crowd; AIA (c16, c20) | E |
| A scaffold can overwrite a right low base rate | 83% of 3,427 resolved markets are NO. Entertainment net -31 (recoveries minus regressions). R1-Distill-Qwen-7B -19; Qwen3-8B +43 | Hindcast (d15) | S |
| Early GPT-4 with base-rate prompt | Brier .20 (SD .18) vs crowd .07 (SD .08); vs 0.25, t(22)=-1.23, p=.23 (23 questions) | Schoenegger and Park 2023 (b23, c17) | S |
| LLM ensemble | 12-LLM crowd .20 (SD .12) vs 925 humans .19 (SD .19), t(60)=.19, p=.85. Mean forecast 57.35% vs 14 of 31 Yes | Silicon Crowd (c15) | E |
| o3 | 464 Metaculus questions: .1352 vs crowd .149; o3-pro .1307 on hold-out | Lu 2025 (b26) | S |
| Debiasing prompts on bias suites | CogBias, 3 LLMs, 19.8% bias rate; prompt debiasing: judgment accuracy -4.4%, info processing -1.1%, social +5.9%, position independence +40.5%. Steering cut bias score 26-32% | Huang et al. 2026 (c22) | S (pooled, preprint) |
| Humans helped by an assistant even when it ignores base rates | N=991, 6 questions. Mean error: control 0.89, superforecasting assistant 0.68, base-rate-neglecting noisy assistant 0.64; difference between assistants p=.391. Without question 3: 0.40 vs 0.47 vs 0.67, p=.024 | Schoenegger et al. 2024 (d07) | S |
| Given prior and sample in an urn task, new models combine near-optimally | Efficiency: GPT-3.5 12.1% and 21.9% below humans; GPT-4 comparable; GPT-4o 1% and 3.5% above; o1 near 100%. Humans 92.5-96% | Mu et al. 2025 (c23) | S |

### 3.6 Evaluation facts
| Finding | Numbers | Source | Status |
|---|---|---|---|
| Brier is not comparable across base rates | Always-b forecaster has expected Brier b(1-b). 50 questions at 50% + 50 at 5%: baseline on coin flips and perfect on rare gives 0.125; clueless on rare and 0.15 on coin flips gives about 0.10. At a 5% class rate, answering 20% costs 0.070 vs 0.0475 | Paleka et al. 2025 (c11, d20) | E (mathematics) |
| Benchmarks leak priors | Question-text-only DeBERTa: up to 80% on a 4-choice generated set (chance 25%); 55% after re-run; Metaculus 55%, Manifold 59% | c12 | S |

---

## 4. Mechanisms and models

Written so an engineer can build each part.

### 4.1 The outside-view procedure (RCF in code terms)
Input: a question or problem. Output: a class, a class distribution, a position in it, a final answer.

1. **Name the class.** One sentence: "cases of kind X". Keep it specific but not so narrow that the count is tiny. ForecastBench wording: the base rate should be as specific as it can be without losing confidence that the number is correct (c14).
2. **Get the class distribution.** Prefer in this order: (a) count from a data series in code, (b) retrieve a stated frequency with a source, (c) read from the agent's class record (SCHEMA section 5), (d) recall from model memory, marked unverified. Source type is the main quality variable (K11, K25, d11-d13).
3. **Express as counts.** Pass "k out of n" to the model, not a percentage (K09, K28).
4. **Place the case.** Estimate where this case sits (percentile, or an adjustment up or down from the class). Adjustments need a stated reason tied to a feature of the case that differs from the class.
5. **Regress and widen.** Final point estimate = class mean plus a bounded adjustment. Interval = class interval, widened for case uncertainty. (a08)
6. **Output a percentile of risk, not a single number**, when a decision depends on risk acceptance (UK uplift: 15% at P50, 32% at P80 for roads) (a10).

### 4.2 Why the inside view over-estimates (the model)
Scenario thinking picks the single most plausible path. Failure has many paths, each less likely than the success path, but their sum is larger. A planner who can build a smooth success story reads "I can imagine it" as "it is likely". Plus: the forecast that wins a competition is a selected, optimistic one (winner's curse and regression to the mean). (a25, a05)

LLM analogue. A model asked for a probability writes reasons for and against, then picks a number from the story. Reasoning prompts pushed forecasts away from 50% (mean distance from 0.5: Bayesian Reasoning .199, CoT .172, Base Rate First .159, Multiple Reference Classes .139, control about .12-.13) and the more decisive prompts scored worse (c04, b20). So the story-then-number path also inflates confidence in models. This is an inference, not a tested mechanism.

### 4.3 Bayesian view of class plus case
Posterior odds = prior odds (class) times likelihood ratio (case evidence). Neglect = dropping the prior odds. Over-use (Buehler Study 5 observers, d03) = dropping the likelihood ratio. A shrinkage form: answer = w times class rate + (1 - w) times case-specific estimate, with w higher when the class is large, tight and relevant, and lower when the case is truly different. No source gives a tested rule for w (gap 3). A neutral default for testing: logit-average of class and case estimates, with w set by class size n.

### 4.4 Base-rate format and arithmetic
- Natural frequencies make nested-set structure visible (a19). For an LLM: give "of 1,000 cases like this, 80 had the outcome", then "of those 80, ...".
- Arithmetic belongs in code. Chained updates stay poor for humans (5-11%, b14). Frontier LLMs combine a given prior and sample near-optimally in a textbook task (c23), but small models skip count steps (d19) and reasoning models mix formats unevenly (d18). Safer design: code counts, code multiplies, model only chooses the class and judges relevance.

### 4.5 Where the class number comes from (three source types)
| Type | Example | Measured quality |
|---|---|---|
| Computed in code from a series | 80 of 1,003 days above threshold = 8%; KNN seasonal counter | Brier Index 58.3 to 59.1 vs 50 baseline; hard to beat (d12, d13) |
| Retrieved or supplied (market price, crowd, stated statistic) | Freeze value; crowd median | Large gains: .17 to .14, .22 to .15 (c16); price alone .096 (c20) |
| Recalled by the model | "Assume 30% chance"; PaLM 2 base-rate pipeline | Vague, run-to-run unstable; worst strategy in Pratt (d11, b25) |

### 4.6 Extremes and shrinking
If a class rate is near 0 or 1 and the model hedges to the middle, Brier loses. Halawi: crowd 1%, system 20% on a question that resolved NO (d09). A band rule: answer = clip(case estimate, class rate - delta, class rate + delta) with delta shrinking as the rate nears an end. Untested (K16, K27). The Murphy shrinkage toward a prior used run disagreement, not class extremity, and chose no shrinkage without anchors (d14).

### 4.7 Class choice
The weak point. Kahneman and Lovallo say try both the firm's own and the external class (a06). Hong Kong shows how far local and global differ (cost +11% vs +20%, schedule +58% vs +38%, a12). Field work claims many similarity-weighted analogies beat a few familiar ones (d05, abstract only). Implementable test: produce 2 to 3 classes, log each rate and their spread, and check whether spread predicts error.

### 4.8 Uniqueness as a trigger
"This is unique" went with +5 points of overrun per rating point in humans (a16). For an agent: a unique-flag could trigger a class search with a wider, more abstract class (the unique project is still an IT project, still a rail project) rather than skip the class. Untested on LLMs.

---

## 5. What holds up

### 5.1 Holds up
- **Inside-view optimism for own plans.** Founding lab data (d01), large project datasets (a09, a12, a13), PIs (b11), a randomized dev trial where experts missed the sign (d17). Direction is stable across domains. Size varies by domain and sample.
- **Large public projects overrun on average.** Rail +44.7%, bridges and tunnels +33.8%, roads +20.4%; costs exceed benefits in 78% of 327. But about one in five goes the other way, so the class gives a two-sided distribution (K02).
- **Knowing a class is not using it.** (a03, a20, a19.) Neglect shrinks when the rate is salient, causal, counted or nested.
- **Data-computed anchors beat recalled ones** (K11, K25).
- **Brier is not comparable across base rates** (K30). Mathematical fact.
- **Ensembling and human-LLM averaging** (K17).

### 5.2 Replications and failed replications
| Result | What happened |
|---|---|
| Frequency format (Gigerenzer and Hoffrage 46-50% vs 16-28%) | Direction replicates (b13: 34% to 68%). Size shrinks in Sloman replications (51%, then 31% with a non-significant gain). Both stand (critique.md). |
| Base Rate First prompt (-0.016) | Significant in t-tests, not in the preregistered mixed model (-0.011, adj p=.774). Combined versions in Study 2 also null (c03). Internal non-replication. |
| Recall of past tasks (planning fallacy) | Recall alone gave 38.1% on time vs 29.3% control; only recall plus link gave 60.0%, with no gain in absolute error (d02). Thomas and Koenig: told durations did not change bias; similarity of the earlier task did (b10). |
| Hiding Hand | Original sample 11 projects chosen on the outcome (a14). Large sample: 22% of 327. The planning-fallacy side wrote both papers. |
| Planning fallacy vs political explanation | Not resolved (K05). |
| RCF improves real projects | No controlled test (K21). Adoption claims rest on official remarks (a24). |
| LLM base-rate step vs plain | Pratt: worse (+0.034 on validation). Schoenegger: small positive or null. Different models, data and base-rate source (recalled vs prompt line). Unresolved (critique.md). |

### 5.3 Moderators
| Moderator | Effect |
|---|---|
| Format (counts vs percentages) | Large for humans, smaller on replication. |
| Class source (computed, retrieved, recalled) | Large in LLM work (section 4.5). |
| Dataset Yes rate | Can flip a base-rate prompt from good to bad (Pratt weighted vs unweighted; Hindcast 83% NO). |
| Salience and causal link | Neglect shrinks when the rate is causal and salient (a19). |
| Class similarity | Similar past task reduces bias; dissimilar does not (b10). |
| Routine vs non-routine | RCF helps most for non-routine projects but class choice is hardest there (b07). Outside view is conservative and fails on exceptional events (a01). |
| Uniqueness | High uniqueness goes with larger and more extreme overruns (a16). |
| Time of estimate | Later estimates in Hong Kong were more accurate; by the last stage the median was about unbiased (a12). |
| Crowd confidence (LLM) | Halawi system beat the crowd only where the crowd was uncertain (b16). |
| Ability and practice (human) | Ability and concentrated practice predicted accuracy; training did not interact with them (b04). |

### 5.4 Interventions that worked
- Probability training bundle: 6 to 12% Brier gain over 4 years, randomized (b01).
- Natural-frequency format, with and without training (b13).
- Recall linked to the present task (mean bias only, d02).
- Data-computed or retrieved anchors (c16, c20, d12).
- Code counting instead of model recall for seasonal frequencies (d13).
- Ensembles and averaging with a crowd (c15, c16, d10).

### 5.5 Interventions that did not work
- Told durations of earlier tasks (b10).
- Asking for several reference classes (c02).
- "Reason as a Bayesian" (+0.025) and Propose-Evaluate-Select (+0.028) (b20).
- Generic debiasing lines (CogBias judgment accuracy -4.4%, c22).
- Base-rate prompt line added to a strong model (null in mixed model, c03, d08).
- Recalled base rates in a chained pipeline (Pratt, d11).
- A superforecaster-authored odds-ratio prompt (+0.023, b21).

---

## 6. Language models

### 6.1 Zero-shot and prompt-line results
Frontier non-reasoning models with a plain prompt sit near a Brier of 0.21 on ForecastBench-style questions (means .207 to .227, 0.250 random). Best zero-shot across 14 LMs without retrieval was about .246 (c10), near chance. A base-rate prompt line moves this by 0.01 to 0.02 at most (b19), and not at all in the preregistered model. Reasoning models (o1, o1-mini) at .216 and .217 were no better than non-reasoning ones, and no base-rate prompt helped any model (d08).

### 6.2 What helped by how much
| Change | Size | Evidence |
|---|---|---|
| Retrieval + fine-tuned reasoning (bundle with a base-rate step) | .206 to .179 (about 0.03) | b15 |
| Reference-class + scratchpad vs zero-shot (bundle, 8 steps) | GPT-4o .168 to .147; Gemini .147 to .143 | d16 |
| Crowd or market value shown to the model | .17 to .14; .22 to .15; price alone .096 | c16, c20 |
| Search agent over a price anchor | .096 to .075 | c20 |
| Code-computed empirical class rate | 58.3 BI vs 50 always-0.5; agent adds +4.5 on top | d12 |
| Base-rate wording alone | -0.016 (t-test), -0.011 (mixed model, ns) | b19 |
| Several reference classes | -0.004 (ns) | c02 |
| Bayesian-reasoning wording | +0.025 (worse) | b20 |
| Ensemble of 3 (agent) | median .169 vs single run .180 | d10 |

### 6.3 How models behave
- **They already do it.** Agent transcripts begin with "reference classes and base rates" (b25, c19). o3 uses reference class then adjusts without being told (b26). So the marginal value of an explicit S0 prompt on strong models is unknown (K18).
- **Recalled classes are vague and unstable.** "Assume 30%" vs a counted 8% for the same ETH question (c19, b25).
- **Acquiescence above 50%.** Individual LLMs lean Yes: mean forecast 57.35% vs 14 of 31 Yes (c15). A base-rate instruction was in the prompt in all conditions, so this bias survived the instruction (b24).
- **Hedging at extremes.** Halawi system gave 20% where the crowd said 1% (d09). Reasoning prompts make forecasts more decisive in the other direction (c04). Both distort the class rate.
- **A scaffold can overwrite a right default.** Hindcast: fan hype pushed near-always-NO Entertainment questions toward YES (d15).
- **Salient case details beat base rates.** GPT-3.5 was swayed by salient case information over base-rate information (c25, qualitative). Claimed myopia: LLMs condition on the prompt sample and do not track the population frequency (c24, theory only).
- **Arithmetic is no longer the problem.** GPT-4o and o1 combine a given prior and sample near-optimally (c23). Reasoning models do not spontaneously use natural frequencies (d18). Small models skip a count-first step (d19, Llama 3-8B), and a small reasoning model was hurt by the scaffold (d15).
- **Debiasing lines backfire.** CogBias prompt debiasing lowered judgment accuracy 4.4% (c22). Matches the SCHEMA 4b entry on debiasing instructions.
- **Humans helped by LLM assistants may be helped by the number.** A base-rate-neglecting assistant helped almost as much as a base-rate-first one (d07). A gain over a no-number control may be an anchor effect.

### 6.4 What is missing
No study isolates S0 placement (first, late, none) at equal tokens in a strong system (K14, critique GAP 1). Halawi puts base rates last. ForecastBench puts them at step 2 of 8. Hindcast fixes a prior-anchor step first in every run. LLM studies use 23 to 100 questions, so effects of 0.01 to 0.02 are inside noise.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E] established, [S] single-source, [C] contested.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Scoring discipline for any S0 test.** Report Brier skill against an always-class-rate forecaster, and on class-balanced subsets. Never compare raw Brier across sets with different Yes rates. | G7 (evaluation) | [E] | K30, K15; c11, d20, c05-c06, d15 |
| A2 | **Class number from code or retrieval over recall.** When a data series or a tool can give the class frequency, compute or retrieve it and hand it over as a counted "k of n", marked with its source type. Model recall is a fallback and is marked unverified. | S0 | [E] | K11; d12, d13, c16, c20, d11, b25, c19 |
| A3 | **Class record is read by S0.** Per problem class: pass rate, how often agreement was right. Already in SCHEMA section 5 as [D]; this subfield supports the design (counted class frequencies are strong baselines). | M (class record) | [E] for the principle that computed class frequencies are strong baselines | K11, K25 |
| A4 | **A supplied class rate must be a required input to the final step**, and the answer must state its relation to it (inside the band, or a reason for leaving). Knowing a rate is not using it. | G (code-forced use), S0 | [E] for the failure; [S] for this fix | K10; a03, a19, a20, b12 |
| A5 | **No generic "be unbiased" or "think like a Bayesian" lines.** A concrete procedure only (name class, get number, state position). | G / 4b | [E] (already in 4b; this adds LLM-specific numbers) | K19, K13; c22, b20 |
| A6 | **Counts, not percentages, when passing class data; arithmetic in code for chained updates.** | S0 data format; O (code arithmetic) | [E] for humans; no LLM forecasting test | K09; a18, a19, b13, b14 |
| A7 | **Aggregate k samples in code (median or trimmed mean), not one sample.** | S7 / G5 | [E] | K17; c15, d10, d09 |
| A8 | **Log when the class is "none usable".** If no countable class exists, S0 widens the interval and says the class is unverified. This is a design fallback, not evidence. | S0 | [D] | critique GAP 9 |

### 7.2 Test first (do not add yet)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **S0 first vs late vs absent** class-lookup step inside the scaffold. | S0 | [S] (every LLM result bundles it) | K14; a23, b17, d15, d16 |
| T2 | **Order rule: class facts before case details.** Fixation risk: SCHEMA shows lessons after the first attempt to avoid fixation. A class band shown before the first attempt may anchor. Test both. | S0 / S3 | [S] | K06, K23; d02 |
| T3 | **Computed vs retrieved vs recalled class on one question set.** | S0 | [S] for the head-to-head; [E] for direction | K11, K25 |
| T4 | **Hold the answer inside a class band when the class rate is below 10% or above 90%.** | S0 / S7 | [S] | K16, K27; d09, d20 |
| T5 | **Unique-flag triggers a wider class search** instead of skipping S0. | S0 | [S] human-only | K04; a16 |
| T6 | **Rule for combining two or three disagreeing classes** (pick, average, widen). | S0 | [C]/[S] no tested rule | K03, K13; d05, d10, c02 |
| T7 | **Strong vs weak model interaction.** Does S0 help weak models more? | S0 | [S] indirect | K18; d08, d15, d19 |
| T8 | **Class-free numeric anchor arm in every A/B** to rule out an anchoring explanation. | test design | [S] | K24; d07 |
| T9 | **Floor and ceiling check (stated reason required to leave the class band).** | S0 / S5 | [S] | K26; d15 |
| T10 | **S0 on effort and duration estimates** beyond forecasting. | S0 | [S] | K29; d17 |
| T11 | **Count-first (natural frequency) text vs code-side counts** on chained updates. | S0 / O | [S] | K28; d18, d19 |
| T12 | **Separate error source: class choice vs combination arithmetic.** | analysis | [S] | K20; c23 |

Status notes. Items rated [E] in section 7.1 rest on the human literature plus LLM data series; no item in 7.2 should enter SCHEMA.md before its test in UNKNOWNS.md passes. K07 and K08 are not used as effect sizes. Do not cite the Chang "0.17 vs 0.26" as an effect.

---

## 8. Concrete tests on our bench

All arms at equal tokens. Use a mixed-effects model (random intercepts for question and model) as the main analysis, as in the preregistered prompt study. Add a per-class base-rate forecaster as the reference for skill scores. Target at least 100 resolved questions per arm, balanced by class rate.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Resolved binary forecasting questions, class rate 5% to 95%, balanced | (a) S0 class lookup first, (b) base-rate check last (Halawi placement), (c) none | Brier skill vs per-class base-rate forecaster; mixed model | Small: 0.00 to 0.02 Brier from prior LLM work (b19). A win at 0.02 would exceed the prompt-line result. |
| B2 | Same set, with a data series available for half the questions | (a) class computed in code and supplied as k of n, (b) class retrieved from text, (c) model-recalled | Brier; run-to-run SD of the class number | Computed best; recalled worst (d11-d13). Expect a difference of 0.01 to 0.04 on series questions. |
| B3 | Same set, class rate under 10% or over 90% subset | (a) free answer, (b) answer clipped to a band around the class rate, (c) required reason to leave the band | Brier on the extreme subset; regressions per class | Fewer hedging losses; Halawi lost 0.04 on that subset (d09). |
| B4 | Same set | (a) class facts before case details, (b) after, (c) class number not shown (anchor-free) | Brier; distance of answer from class rate | Order effect unknown; Buehler observers over-used the past (d03). |
| B5 | Same set | (a) S0 class lookup, (b) class-free numeric anchor (random but plausible number), (c) none | Brier | Separates class content from anchoring (d07). If (b) ≈ (a), the gain is an anchor effect. |
| B6 | Set where a second class is available | (a) one class, (b) two classes averaged in code, (c) two classes widened (interval from both), (d) two classes with spread logged | Brier; correlation of spread with squared error | Averaging ≈ one class (c02); spread may predict error. |
| B7 | Same set, tagged unique vs routine by a held-out rater | (a) class lookup on all, (b) lookup only if routine, (c) lookup widened if unique | Brier by tag | Unique items worse overall (a16); widening may help. |
| B8 | Same set, one strong reasoning model and one small model | S0 on vs off per model | Interaction term in mixed model | Strong models already do it (b26); weak models skip count steps (d19). Expect an interaction with a bigger gain for weak models, but tool-assisted counting may flip it. |
| B9 | Chained-update problems (two tests in sequence) with known answers | (a) text percentages, (b) text natural frequencies, (c) code arithmetic from counts | Accuracy on exact answer | Code best. Humans get 5-11% on chains (b14). |
| B10 | Effort or duration estimates with known actuals (our own run logs) | S0 class lookup from the class record vs none | Log-ratio error predicted/actual; share on time | Reduced optimism; direction from d01, d17. |
| B11 | Entertainment-style near-always-NO items | Retrieval step with and without a stated class floor | Net recoveries minus regressions | Fewer regressions (d15). |
| B12 | Error audit of B1 failures | Label each wrong answer: class chosen wrong, class number wrong, adjustment wrong, arithmetic wrong | Share per label | Class choice and number dominate, not arithmetic (c23). |

---

## 9. What does not transfer, and why

- **Student and tournament results.** Chang (volunteers, high education, score feedback) and Buehler (students, one task) tell us about human habits. They do not tell us how a scaffolded LLM behaves.
- **The "0.17 vs 0.26" tag score.** Self-tagged, correlational, standardized, unit undefined (all means positive). Reverse causation: some tags are used because a question is going badly (post-mortem 1.04). Do not use as an effect size.
- **Training-package results.** Bundled with averaging, models, bias awareness and updating. The outside view alone is not isolated.
- **Flyvbjerg's project datasets.** Large public projects, not a random sample, built by an advocate group. They support the class numbers, not a universal law. RCF adoption has no controlled outcome test.
- **Political explanation.** Projects are cooked by people with incentives. Our agent has no budget to win. If a user wants a rosy answer, it may act like pressure. That is a user-interface issue, not a property of the model.
- **Morale argument.** Optimism may help persistence (a06). An agent making a forecast does not need morale.
- **Natural-frequency results.** Medical-student diagnostic tasks with given numbers. Our agent builds its own classes. Reasoning LLMs also do not spontaneously use frequency formats (d18).
- **Urn-task Bayesian skill.** Prior given. The agent's hard step is finding the prior (c23).
- **Recalled-class pipelines from 2022-2023 models.** PaLM 2 (Pratt) and GPT-4 era results (b23) may not hold for 2025-2026 models; but frontier results from 2025 still show null prompt effects.
- **Dataset-specific base rates.** Hindcast (83% NO) and Pratt (mostly No) show a base-rate step can win or lose because of the data mix, not the method.
- **Planning-fallacy "inside view" for an LLM.** The agent has no personal plan to be optimistic about; whether its text mimics scenario thinking is an open question (section 4.2).

---

## 10. Open questions

1. Does a first-step class lookup beat a late base-rate check and no step, at equal tokens, in a retrieval scaffold? (Critique GAP 1; no study.)
2. Computed vs retrieved vs recalled class on one question set. Direction is known; sizes and the head-to-head are not.
3. How to combine two or more disagreeing classes. Multiple Reference Classes did nothing; no tested rule exists.
4. Does S0 help weak models more than strong reasoning models that already do it? No interaction test.
5. What is the real size of the Chang comparison-class effect once difficulty and self-selection are removed? Is there a randomized test of the outside-view instruction alone? None found.
6. Does shrinking toward an extreme class rate improve Brier? Suggestive (Halawi, -0.04); no direct test.
7. Does a "this case is unique" signal predict LLM errors the way uniqueness predicts human overruns?
8. Do natural-frequency counts change LLM base-rate use in forecasting? Only one puzzle tested.
9. Which tasks beyond forecasting have a usable class (effort estimates, ARC-style tasks), and what is the fallback when none exists?
10. What did Lovallo and Kahneman 2003 and Lovallo, Clarke and Camerer 2012 report (N, design, effect)? Neither was opened.
11. Is the base-rate effect on LLMs a real null or an underpowered small effect (0.01 to 0.02 Brier on 100 questions)?
12. Why did Pratt find the base-rate strategy worst and Schoenegger slightly positive? Model, data and base-rate source all differ.
13. Does showing a class number fixate the model (SCHEMA keeps lessons after the first attempt for this reason)?
14. Is optimism in LLM forecasts better modelled as political (user pressure, sycophancy) or as a plain text-prediction effect?
15. The run-to-run spread for recalled classes: the quoted "30% vs 8%" is one example (c19); the measured spread is the ensemble SD .092 vs .150 (d10).

---

## 11. Sources

[V] = opened and read this session (full text or substantial part). [M] = snippet or second-hand only.

**Founding and project literature**
- [V] Kahneman and Lovallo (1993) Timid choices and bold forecasts. Management Science 39(1):17-31. https://pdf.stafforini.com/kahneman-1993-timid-choices-bold.pdf
- [V] Flyvbjerg (2006) From Nobel Prize to project management: getting risks right. https://arxiv.org/abs/1302.3642
- [V] Flyvbjerg, Hon and Fok (2016) Reference class forecasting for Hong Kong's major roadworks projects. https://arxiv.org/abs/1710.09419
- [V] Flyvbjerg and Sunstein (2016) The principle of the malevolent hiding hand. https://arxiv.org/abs/1509.01526
- [V] Flyvbjerg (2018) Planning fallacy or hiding hand. https://arxiv.org/abs/1802.09999
- [V] Flyvbjerg (2003) Delusions of success: comment on Lovallo and Kahneman. https://arxiv.org/abs/1305.0741
- [V] Flyvbjerg, Budzier, Christodoulou and Zottoli (2024) Uniqueness bias. https://arxiv.org/abs/2408.07710
- [V] Flyvbjerg (2022) Top ten behavioral biases in project management. https://arxiv.org/abs/2202.00125
- [M] Lovallo and Kahneman (2003) Delusions of success. HBR (via Flyvbjerg, b08)
- [M] Lovallo, Clarke and Camerer (2012) Robust analogizing and the outside view. https://doi.org/10.1002/smj.962 (abstract only)
- [M] Cooper et al. (1988); Merrow et al. (1981); PIMS (Davis 1985); Dun and Bradstreet (1967); Gilovich et al. (2002) (all via a01, a05, a11)

**Planning fallacy and base-rate neglect**
- [V] Buehler, Griffin and Ross (1994) Exploring the planning fallacy. https://bear.warrington.ufl.edu/brenner/mar7588/Papers/buehler-et-al-1994.pdf
- [M] Buehler et al. (1995) It's about time (figures via https://en.wikipedia.org/wiki/Planning_fallacy, a22)
- [V] Thomas and Koenig (2018) Knowledge of previous tasks. https://pmc.ncbi.nlm.nih.gov/articles/PMC5976789/
- [V] Gigerenzer and Hoffrage (1995) How to improve Bayesian reasoning without instruction. http://library.mpib-berlin.mpg.de/ft/gg/GG_How_1995.pdf
- [V] Barbey and Sloman (2007) Base-rate respect (BBS) and Griffin, Koehler and Brenner commentary. http://bear.warrington.ufl.edu/brenner/papers/griffin-bbs-comment07.pdf
- [M] Koehler (1996) The base rate fallacy reconsidered (via a19)
- [V] Bruckmaier et al. (2021) Tversky and Kahneman's cognitive illusions (abstract and introduction). https://pmc.ncbi.nlm.nih.gov/articles/PMC8075297/
- [V] Natural frequencies boosting study, 577 medical students. https://pmc.ncbi.nlm.nih.gov/articles/PMC9903474/
- [V] Odds/LR vs natural frequencies crossover trial (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11980142/
- [V] Benjamin et al. (2022) Principal investigators over-optimistically forecast. https://pmc.ncbi.nlm.nih.gov/articles/PMC8824379/
- [V] Becker, Rush, Barnes and Rein (2025) METR developer trial. https://arxiv.org/abs/2507.09089

**Human forecasting**
- [V] Chang, Chen, Mellers and Tetlock (2016) Developing expert political judgment. http://journal.sjdm.org/16/16511/jdm16511.pdf
- [V] AI Impacts, Evidence on good forecasting practices from the Good Judgment Project (read through a fetch summary). https://aiimpacts.org/evidence-on-good-forecasting-practices-from-the-good-judgment-project/

**LLM studies**
- [V] Halawi, Zhang, Yueh-Han and Steinhardt (2024) Approaching human-level forecasting. https://arxiv.org/abs/2402.18563
- [V] Schoenegger et al. (2025) Prompt engineering LLMs' forecasting capabilities. https://arxiv.org/abs/2506.01578 (author sets differ between ids b19 and c01; cite by first author and title)
- [V] Pratt, Blumberg, Carolino and Morris (2024) Can language models use forecasting strategies? https://arxiv.org/abs/2406.04446
- [V] Karger et al. (2025) ForecastBench. https://arxiv.org/abs/2409.19839
- [V] Hsieh et al. (2024) Reasoning and tools for human-level forecasting. https://arxiv.org/abs/2408.12036
- [V] Schoenegger and Park (2023) LLM prediction capabilities. https://arxiv.org/abs/2310.13014
- [V] Schoenegger et al. (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379
- [V] Schoenegger et al. (2024) AI-augmented predictions. https://arxiv.org/abs/2402.07862
- [V] Lu (2025) Evaluating LLMs on real-world forecasting against expert forecasters. https://arxiv.org/abs/2507.04562
- [V] Alur et al. (2025) AIA Forecaster technical report. https://arxiv.org/abs/2511.07678
- [V] FutureSearch (2025) Bench to the Future. https://arxiv.org/abs/2506.21558
- [V] Paleka et al. (2024) Consistency checks for language model forecasters. https://arxiv.org/abs/2412.18544
- [V] Paleka, Goel, Geiping and Tramer (2025) Pitfalls in evaluating language model forecasters. https://arxiv.org/abs/2506.00723
- [V] Murphy (2026) Agentic forecasting with structured linguistic beliefs. https://arxiv.org/abs/2604.18576
- [V] Ye, Dineen et al. (2026) Hindcast. https://arxiv.org/abs/2607.14051
- [V] Huang et al. (2026) CogBias. https://arxiv.org/abs/2604.01366
- [V] Mu et al. (2025) Who is more Bayesian: humans or ChatGPT? https://arxiv.org/abs/2504.10636
- [V] Araya (2025) Chains-of-thought in Bayesian reasoning. https://arxiv.org/abs/2503.15268
- [V] Huang, Fayek and Zhang (2025) REFER. https://arxiv.org/abs/2509.15723
- [V] Scholten et al. (2024) Metacognitive myopia in LLMs. https://arxiv.org/abs/2408.05568
- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 9 established claims: 6 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E03.04-K03** (reworded: the sources support less). Flyvbjerg et al. state the HK schedule overrun difference (+58% vs +38%) is not statistically significant (p=0.089; only the share of late projects differs, p=0.048); Hsieh's prompt lists weighted/trimmed mean or median, not only a plain average; the Lovallo-Clarke-Camerer field test is not among the opened sources. Corrected claim: Local classes can differ from global ones (HK road cost overrun +11% vs benchmark +20%; HK schedule overrun +58% vs +38% but that mean difference is not significant, though the share of late projects was higher, 8 in 10 vs 6 in 10). Class choice is the weak point and Kahneman and Lovallo only advise trying both classes; no opened source gives a rule for resolving disagreeing classes. In LLM work the Hsieh example simply averages three estimates (30, 35, 40 to 35%) and its prompt suggests a weighted or trimmed mean or median.
- **E03.04-K10** (reworded: the sources support less). The 'estimated seen base rates accurately but did not use them' result is one simulated stock-market learning paradigm (Brenner et al.) reported in the Griffin-Koehler-Brenner commentary; a19 and a20 are the same PDF, and Bruckmaier et al. (2021) says nothing about base-rate use; 'causal' as a shrinking condition is not supported in the opened text (BBS only notes causal base-rate problems differ). Corrected claim: In a simulated stock-market learning paradigm (Brenner and colleagues, reported in Griffin, Koehler and Brenner's commentary), participants estimated the base rates they had experienced accurately but their probability judgments were largely unaffected by them; base-rate use rises with counting or natural-frequency procedures and when the problem makes nested set structure transparent (Barbey and Sloman 2007).
- **E03.04-K11** (reworded: the sources support less). Numbers check out (Silicon Crowd 0.17 to 0.14 and 0.22 to 0.15, AIA 0.096 vs 0.109, BLF 58.3 vs 62.7 and KNN 59.1 vs 50.0, Pratt weighted 0.2540 worst), but in Hsieh the 'ETH 8% by count' is the model's own arithmetic (50+20+10 days of 1003, written in its answer, not a code or data count), the BLF full agent beats the empirical-prior baseline significantly (+4.5 BI), so 'strong baseline' is not 'no better', and the Pratt pipeline lacks a data-anchored control. Corrected claim: Giving LLMs a crowd or market value helped (GPT-4 0.17 to 0.14, Claude 2 0.22 to 0.15 with the human median; market price alone 0.096 vs 0.109 for the best prior LLM system; ForecastBench top LLMs used freeze values), while model-recalled base rates are vague and gave no gain (Hsieh's trace recalls 30% for ETH, then reasons its way to 8% with day counts the model wrote itself; Pratt's recalled-base-rate pipeline had the worst weighted Brier, 0.2540). A code-computed class frequency was a strong baseline (empirical prior Brier Index 58.3 on dataset questions vs 62.7 for the full BLF agent, which still beats it significantly; KNN frequency counter 59.1 vs 50.0 for always-0.5).
- **E03.04-K02** (now single-source: only one opened source, code check).
- **E03.04-K17** (now single-source: only one opened source, code check).
- **E03.04-K21** (now single-source: only one opened source, code check).
