# Resource-rational analysis and rational strategy selection: deep document

*Subfield C03.06. Written from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b09, c14, d03 ...) point to lines in those files. Claim ids (K01 ...) are in claims.jsonl, written C03.06-K01 in full. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. All human evidence on strategy selection comes from one lab (Lieder, Griffiths and co-authors). Read every human number with that in mind.*

---

## 1. What it is

**The question.** A mind has many ways to solve a problem. Some are fast and rough. Some are slow and exact. Which one should it use on this problem, right now? Thinking costs time, and time has a price. So the best strategy is not the most accurate one. It is the one with the best accuracy minus the cost of running it.

**Resource-rational analysis** (Lieder and Griffiths) is a recipe for theories of the mind. (a36, a22; the 2020 BBS paper itself was not opened.)

1. State the function the mind is trying to compute.
2. State the architecture: a set of cheap elementary operations, each with a cost.
3. Derive the best algorithm that fits that architecture. Best means highest utility after paying for the computation.
4. Test the derived algorithm against behaviour.
5. Revise the assumptions and repeat.

**Rational strategy selection** is the special case where the choice is among known strategies. Lieder and Griffiths (2017) wrote it as a contextual bandit (a01):

- The context is a set of cheap, perceivable features of the problem.
- The arms are the strategies.
- The reward of an arm is its expected result quality minus a cost for its run time.
- The cost is an opportunity cost: reward rate times execution time.

Formula (a01, c01): VOC(s, p) = E[utility of the action s picks on p] - lambda * E[time of s on p]. Pick s* = argmax over s of VOC.

The strategy is chosen before running it. The chooser sees only features. It cannot see what the strategy would have produced.

**Why this matters for us.** Our schema has a gate (S0) that picks a mode (direct, short reason, step-by-step, checked, open) and a budget rule (G12, "spend by difficulty"). This field is the closest worked theory for that gate. It says what the gate should compute (predicted pass rate and predicted cost per mode, from cheap class features), how it should learn (per-mode regression updated by logged outcomes, Thompson sampling for exploration), and how it can fail. It also has a small LLM literature on routing effort and mode that tests the idea, mostly in 2026 preprints.

**Scope notes.**
- "Strategy" in the human work means a procedure the person runs by hand (sort by cocktail sort or merge sort; take-the-best or weighted-additive; breadth-first or best-first planning). In the LLM work it means a reasoning mode or effort level, or a model.
- Almost no paper runs the pure form on an LLM. The pure form is: per-strategy reward and time regressions on features, with Thompson sampling. The nearest are bandit routers (Meta-Reasoner, MetaScale) and learned effort routers (ARES). See section 6.

---

## 2. History and theories in depth

### 2.1 Before 2014: the toolbox and cost-benefit view

- **Payne, Bettman and Johnson (1988)** showed that people use fast heuristics under time pressure or when outcome probabilities are spread out. They use slow, accurate rules otherwise. This is the basis for the cost-benefit view. (a33, not opened; described through Lieder and Griffiths 2017.) Lieder and Griffiths later simulated this experiment: the model raised attribute-based processing 29.69% under time pressure and 44.11% under high dispersion (t(1998) = 9.70 and 14.41); the SCADS rival gave effects of about zero (a06). The assignment of the two numbers to the two factors follows the order in the text. The 2015 conference paper repeats the simulation with 10 strategies, 1000 learners, 1 s per elementary operation (b03, c04). This is a simulation of a published human result, not a new human sample.
- **Russell and Wefald (1991)** gave rational metareasoning: choose computations by their expected value of computation, which is the gain in decision quality minus the cost of time. It is intractable in general (Hay et al. 2012), so later work uses myopic or learned approximations. (a34, not opened; cited in opened papers.)
- **Three rival families of strategy-selection theory** (b27):
  1. Cost-benefit contingency (Beach and Mitchell 1978; Payne). People compute each strategy's value from the problem.
  2. Reinforcement of average payoff. SSL (Rieskamp and Otto 2006), RELACS, and SCADS (Shrager and Siegler 1998) learn one value per strategy from experience. SSL and RELACS are context-free. SCADS learns by problem category plus a global association. (a32, a35, b26, none opened first-hand.)
  3. Feature-based rational metareasoning (Lieder and Griffiths).

  Each family fails at least one test (b27). No single study runs all rivals on the same people.

### 2.2 2014 and 2015: the first formal versions

- **Lieder et al. NIPS 2014** applied rational metareasoning to sorting-algorithm selection. It beat the best published selectors (a13-a16), see section 3.
- **Lieder and Griffiths CogSci 2015** ("When to use which heuristic") gave the core recipe: for each strategy, learn to predict expected reward and run time from features; choose the best reward minus time cost; learn by Bayesian linear or logistic regression; explore with Thompson sampling (c01). Simulation over 11 environments: when the share of compensatory problems nears 50/50, SSL and RELACS fall to chance (50%) while metareasoning stays above 70%. In homogeneous environments they tie (c02). One discriminating human experiment (b02, c03).

### 2.3 2017: the Psychological Review paper

The main paper (OSF text read: a01-a12). Four human experiments, three simulations of older data, and model comparison against SSL, RELACS and SCADS. The model has four parts (a02):

1. VOC-based choice.
2. Feature-based learning.
3. Separate time and accuracy models per strategy.
4. Thompson-sampling exploration.

A Gaussian prior on reward rate is worth 60 seconds of experience. Bayesian model selection picks which features matter.

The authors list their own limits (a12): it does not discover new strategies; it presupposes domain-specific features; it assumes a fixed strategy set; it ignores working-memory cost; the exploration mechanism is left open (Thompson, UCB and epsilon-greedy are all candidates).

### 2.4 2018: extensions

- **Learned Value of Control (LVOC)** (a17-a19, b07). Extends the idea to continuous control signals (how much attention or control to apply). The value of a control signal is a linear function of state features, signal intensity and their interactions, minus cost. Weights come from Bayesian regression. It fits published Stroop, Flanker and visual-search learning data far better than Rescorla-Wagner and win-stay-lose-shift rivals by BIC, with no parameters fitted to those data. It underestimates the size of one effect about 4 times and needs change detection, since people unlearn faster than the model.
- **Bayesian Metalevel Policy Search (BMPS)** (Callaway et al., UAI 2018; a20, a21). A metareasoning policy that is a linear mix of three features: myopic value of information (VOI1), value of perfect information (VPI) and cost. It reaches near-optimal behaviour on synthetic metalevel problems. It needs an exact model of the agent's own belief updates, so it is not directly usable for an LLM.
- **Resource-rational anchoring** (a22-a24). Anchoring and adjustment is the optimal stopping of a few adjustment steps when time cost is set against error cost. The optimum is small, so some bias remains. One principle explains ten anchoring phenomena in simulation.
- **Planning** (CogSci 2018, then Nature Human Behaviour 2022; a25-a27, c05, c06). People's planning clicks track the optimal metalevel policy across environments.

### 2.5 2019 to 2025: tutoring, discovery, and LLM use

- **Cognitive tutors** (b09-b16, a31). Teaching people the optimal strategy by feedback on the planning process. This is the applied branch and the best human evidence on what feedback helps.
- **Strategy discovery** (b17-b19). How people learn new strategies, not just choose among old ones. This is the gap the 2017 paper listed.
- **LLM versions** (section 6): Rational Metareasoning for LLMs (RaM, trained), effort routers (ARES, RACER, R2-Router), bandit-over-strategy loops (Meta-Reasoner, MetaScale), and a direct LLM replication-style test of strategy shift with problem size (Hu et al. 2026).

### 2.6 Criticism and boundary of the programme

- Commentators on the 2020 BBS target article argued the method is confused with a claim that people are truly resource-rational (Rahnev), that its normative status is unconvincing (Colombo), and raised a teleology objection (b08). This is second-hand from search summaries. The authors' reply was not read.
- The planning papers themselves report systematic departures from the optimal model: forward-search bias, under-sensitivity to relative value (a26, a27).
- Strategy sets and features are hand-set in every model (critique section 4).

---

## 3. Core findings with exact numbers

Status here follows claims.jsonl. "Single-source" often means "one lab". Where I can, I note whether the claim was re-opened in the critique pass.

### 3.1 Human strategy selection (Lieder and Griffiths lab)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People choose merge sort vs cocktail sort by list features after 11 forced training trials | N=100 MTurk. Merge sort chosen 81.67% on long nearly-inverted lists, 29.83% on long nearly-sorted, 27.00% on short nearly-sorted. 83% of people adaptive (95% CI 74.9 to 89.4). Task time 24.7 +/- 6.7 min | a03, a16, K02 | [S] one lab, one sample (journal and NIPS are the same experiment) |
| Model vs people on that choice | Metareasoning adaptive in 70.5 +/- 3.2% of simulated runs; best SCADS variant 59.0%; people 83.0%; model vs people t(298)=2.34, p=0.01. Critique: people beat the model; model under-predicts adaptivity | a04, critique 1 | [S] |
| Design was picked to separate the models | 104 candidate designs simulated; training set unbalanced; discrimination partly built in | a04 | caveat |
| Thinking drops when it costs too much | Exp 2, N=100. Engagement 37% to 19%. Information acquisitions fall about 1.4 per block (CI -1.60 to -0.68); reward rate d=1.00; reward per decision unchanged (p=0.49) | a07 | [S] |
| Thinking rises when it is too low | Exp 3, N=201, 57 excluded (28.36%), 144 analysed. Reward rate t(143)=2.87, d=0.26. Low-stakes engagement 49.1% to 58.95%. Acquisitions 4.97 to 6.42 | a08 | [S] small effect, high exclusion |
| Mixed environment, one fixed strategy gives chance | Exp 4, N=100, 100 trials. Agreement with right strategy 76.2% (99% HPD 75.1 to 77.3); 70.4% first 10 trials to 80.4% last 10; 73% on trial 1 | a09 | [S] trial-1 success suggests prior skill |
| Same, 2015 version | N=120, 30 trials. Accuracy 64.6% (99% CI 62.5 to 66.6) vs 50% for any fixed or context-free strategy. Learning slope CI [-0.1, 0.2] per trial: no learning seen | b02, c03 | [S] |
| Fit to Rieskamp and Otto (2006) data, homogeneous environment | 2015: MSE 0.0050 (metareasoning) vs 0.0048 (SSL). 2017: BIC 60.70 (SSL) vs 68.94 (RM); MSE 0.0018 vs 0.0043. Metareasoning without features: BIC 70.52 | a10, b01, c02, K03 | [E] that SSL ties or wins on homogeneous data; the two papers disagree on how close |
| Start-up behaviour | People start with the costly full-information strategy (Newell et al. 2003 data, N=24, SSL mean p=.71, SD .05). Against pure cost-benefit | b04, K04 | [E] but reanalysis by the SSL author |
| Slow, asymmetric switching after environment change | Broder and Schiffer data: 79% TTB in non-compensatory phase, 58% WADD in compensatory. After switch only 27% moved to compensatory, 65% to TTB. SSL predicted about 100 extra trials; real switching was faster | b05, K04 | [E] |
| Anchoring: time cost shrinks adjustment, error cost grows it | Self-generated anchors, N=30 (6 excluded): 50.7% to 31.0% (F(1,69)=21.86); 31.6% to 50.1% (F(1,69)=19.49). Provided anchors, N=60 (16 excluded): time cost 37.2% to 28.2%; error cost 31.2% to 34.2% (3 points) | a23, a24, K05 | [C] contradicts Epley and Gilovich 2006 on provided anchors; agrees with Simmons et al. 2010 |
| Planning tracks payoff structure | Exp 1 N=104: 81.5% of clicks expand a max-EV path; 0.92 points below best for their click count. Exp 2 N=298: optimal model best in increasing and decreasing variance (LL 606, 1276); best-first fits best in constant variance (optimal worse by LL 2150). 2018 version: first click on an end state 95.0% vs 0.3% | a25, a26, c05, c06, K06 | [S] one lab; best-first near-optimal in constant condition so models hard to separate |
| Systematic departures from optimal | Backward-lookup rate 7.2% when no revealed parent; 92.4% of lookups followed revealed parents vs 75.5% in noise-free optimal simulations. 28.3% of deviations were stopping early, 6.3% planning too long. Followed best-first 82.1% of the time (N=60, 15% excluded) | a27, c05 | [S] |

### 3.2 Tutoring and feedback on the planning process

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Process feedback lifts planning; action feedback does not | Exp 1, N=151. Relative test score: none 77.0, action 73.5, process (metacognitive) 94.4. Process vs none d=0.59, p=0.005. Action vs none d=-0.09. H=9.71, p=0.008 | b09 | [S] ceiling at 77 in controls; bimodal scores |
| Transfer to a harder task, retained 24 h | Exp 2, N=297. Process 81.2 vs action 49.0 (d=0.88) vs none 57.6 (d=0.69). Other transfer 77.2 vs 63.0 (d=0.42) vs 59.0 (d=0.61). Critique adds Exp 1 transfer 74.6 vs 57.0 vs 57.5 (d=0.48, 0.44) | b10, critique 1 | [S] |
| Far transfer to a road-trip task is weak | Exp 5 (1380 recruited, 112 excluded). Hotel-first 46.3% (process) vs 39.4% (action) vs 39.4% (none), d=0.17, P=0.035; passive video 23.5% (d=0.61 worse). Mediation through backward planning: indirect 12.9 points (CI 7.6 to 18.1), direct -3.8 | b11, b13 | [S] authors call it an upper bound for real use |
| Both parts of the feedback are needed | Exp 6, N=417. Both 87.5 vs none 75.8 (d=0.32, p=0.024); delay only 77.7 (d=0.05); hint only 71.8 (d=-0.09) | b12 | [S] |
| Effect size drift | Workshop 2019: trial-level t(2258)=10.7 treats trials as independent. PNAS: participant-level d 0.59, 0.88, 0.69, 0.42, 0.61, 0.32, 0.17. Effects shrink as design tightens | b14, b28 | warning |
| Tutor must fit task size | Hierarchical tutor 204.48 vs control 177.36 (d=.304, p=.006); feedback tutor vs control d=.104 (p=.45); non-hierarchical vs control d=.045 (p=.67). 42 per group | b15 | [S] |
| Pre-registered tutor in large partially observable task | 330 recruited, 37 excluded. Median resource-rationality score: no tutor 11.46, choice tutor 22.67, model-strategy tutor 22.41 to 22.70. Dummy tutor vs none p<.29 | b16 | [S] |
| Plain-language step lists from the optimal strategy help | Control N=60 (Exp 1), 54 (Exp 2); mean click agreement with instructed strategy 68.8% (median 59.8%) | a31 | [S] effect sizes not recorded |

### 3.3 Discovery and learning mechanisms

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People rarely discover a new planning strategy alone | 420 recruited, 349 analysed. Share using the adaptive strategy 0.79% on trial 1 to 28.57% (CI 27.21 to 29.93) on trial 120. 90% best fit by a learning model; REINFORCE-type 61%, habit 39%, SSL-style under 1% | b17, K08 | [S] |
| Mechanism comparison | 86 models, 382 participants. Non-learners best for 34% of all (25% after dropping some). REINFORCE family 47.41% of learners | b18, K08 | [S] |
| Extra mechanisms fit better | Variants fit 244 people (69.96%) better than plain REINFORCE (102; 30.09%). Same dataset | b19 | [S] not independent |

### 3.4 Algorithm selection (simulation)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Beats best published sorting selector | 99.78% vs 98.5% on Dsort5 test (p<1e-15); nearly sorted 99.99 vs 99.4; inversely sorted 83.37 vs 77.0; random 99.99 vs 85.3 | a13 | [S] |
| Faster than recursive selector | 27.96 s vs 102.5 s over 21 sets; 47.90 s when limited to same algorithms | a14 | [S] |
| Beats nine psychological models | 88.1 +/- 0.7% of maximal speed vs at most 30%; selection time counted | a15, K01 | [S] |
| BMPS near optimal | Planning tree 99.1% of optimal (0.6535 vs 0.6596), meta-greedy 0.60, full deliberation 0.20, DQN 0.58; Bernoulli bandit at most 5.19% below optimal | a21, K18 | [S] |
| Metalevel features | Regression on VOI1, VPI and cost explains 90.8 to 100% of VOC variance. At cost 0.001: 0.76 VPI + 0.46 VOI1 - 4.5 cost. At cost 0.1 and above: 0.00 VPI + 1.00 VOI1 - 1.00 cost | a20 | [S] |

### 3.5 LLM results

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Training with a VOC reward cuts tokens | 35-42% fewer than few-shot, 23-32% fewer than STaR (v3; v1 said 20-37%). Hard-vs-easy length gap 50.3% (RaM) vs 34.4% (STaR) vs 19.0% (few-shot CoT) vs 0.5% (instruct CoT). OOD MMLU-CF 28-36% fewer tokens; 8B accuracy 40.2 to 36.4 | a28, a29, b21, c07-c10, K09 | [S] needs fine-tuning |
| Learned effort router keeps success at less cost | TAU-Bench Retail (gpt-oss-20b): Low 35.0, Medium 47.3, High 54.8, Random 43.5, ARES 54.8; up to 52.7% fewer reasoning tokens. BrowseComp-Plus 41.3 vs 42.7 (41.8% fewer tokens). WebArena 46.5 vs 45.0. gpt-oss-120b Retail: High 67.8 (558k tokens), ARES 65.2 (428k) | c14, d11 | part of [E] K10 |
| More effort can hurt | Airline High 38.0 vs Medium 42.0 (about 50 tasks). RL router Airline 36.0 to 42.0, tokens 678k to 133k (fixed high 873k); Retail 54.8 to 58.5 with 476k vs 1007k tokens | c16 | [E] K11 (with other sources) |
| Model routing and cascades | RouteLLM: MT-Bench 8.8 = 95% of GPT-4 (9.3), over 2x cheaper. FrugalGPT: up to 98% cost cut, or +4% at same cost. R2-Router: 4-5x cheaper at equal quality. Thinkless: 50-90% fewer long chains | b22, b23, c27, b24 | [E] K10, six sources |
| Self-routing fails | Qwen3 chooses reasoning 99.91 / 99.51 / 99.88% (1.7B / 4B / 8B); cost 19.07 / 6.25 / 6.36 times all-instruct; accuracy equals all-reasoning | c26, K12 | [E] |
| LLM as router is weak | GPT-5 as router 40.0 vs ARES 54.8 (Retail); Gemini-3-Pro 46.1. Direct LLM arm selection 82 vs LinUCB 89 (Game of 24) | c14, c19, K12 | [E] |
| Named strategies do not help | Phi-4 TruthQuest none 47.2, strategies 45.1-49.0; R1-Distill 63.4 vs 61.4-63.0; ZebraLogic Phi-4 27.3 vs 25.1-27.0 | c21, d15, K11 | [E] |
| Strategy oracle gap | Phi-4 TruthQuest: oracle 82.9; vote 54.9; vote+prob 57.3; verifier 46.9. R1-Distill: oracle 90.1; verifier 74.1; vote 68.4 | c21, c22, d05, K13 | [S] oracle inflated |
| Any-of-k rises from sampling alone | MATH Llama-3-8B: coverage 82.9% at 100 samples to 98.44% at 10,000; vote or reward model 40.50% to 41.41%. SWE-bench Lite 15.9% to 56% | d07 | primary (not a replication of the above) |
| Bandit over strategies | Game of 24: Meta-Reasoner 89 (GPT-4o-mini), 92 (GPT-4o) vs ToT 65, CoT 4. MetaScale Arena-Hard GPT-4o 93.14 vs CoT 84.72 vs best-of-N 87.42 | c18, c20, K16 | [E] but LLM-judged rewards |
| Cue direction flips | Spearman entropy vs rollout utility from -0.346 to +0.428 across 12 environment-backbone pairs. Learned direction best in 16 of 18 cells; one cell base 37.0, always-trigger 59.8, DIAL 49.8 | c23, c24, K14 | [S] |
| LLM strategy tracks problem size | beta(log size) +1.0212, beta(trials) -0.1466, p<.001; AIC 2727.29; pseudo R2 0.160; judge accuracy 0.86, kappa 0.76 | c11, c12, K15 | [S] |
| Difficulty bins beat uniform allocation | Five bins by pass@1; compute-optimal beats best-of-N at about 4x less compute (MATH). 2048 samples per question to get bins; cost not counted | d03, d14, K20 | [S] |
| Easy bins punish heavy search | Beam search with PRM worsens with budget on MATH levels 1-2; beats best-of-N on 3-4; level 5 little gain from anything | d04 | [S] |
| Overthinking | First solution round correct in over 92% of cases and under 60% of tokens; 1,953% more tokens for 2+3; self-training cuts tokens 48.6% on MATH500 | d08 | [S] |
| Lambda from the budget | RACER primal-dual multiplier rises under tight budgets, goes to zero when loose; at C=4 beats three routers by 0.64, 1.10, 1.06 points | d09, d10, K21 | [S] |
| Forgetting is needed | D-UCB/SW-UCB regret O(sqrt(T) log T) with fixed number of breakpoints; Thompson with Beta decay (gamma=0.01, 10,000 runs) keeps reasonable regret | d01, d02, d13, K19 | [S] theory; two sources |

---

## 4. Mechanisms and models

This section is written so an engineer can build each piece. The agent is a program plus a model (SCHEMA section 1). All of this is program code. No model call decides a mode.

### 4.1 The core: a feature-based VOC table (the Lieder-Griffiths selector)

**Inputs.** A problem p. A fixed list of modes M (for us: direct, short reason, step-by-step, checked, open; maybe with a token cap each). A feature function f(p) returning a few cheap numbers or labels.

**Per mode m, keep two predictors:**
- R_m(f): expected reward. Binary pass or fail from a code check, so logistic regression. If the check returns a score in [0, 1], use linear.
- T_m(f): expected cost in tokens (or seconds). Linear regression on counts such as input length and problem size.

**Choice rule.** For each mode, VOC_m = R_m(f) - lambda * T_m(f). Pick the argmax. The original selects by Thompson sampling: draw one weight vector from each posterior, compute VOC from the draw, pick the best (a02, c01). Exploration comes for free because uncertain modes sometimes draw high.

**Update rule.** After the run, update R_m with the observed pass/fail and T_m with the observed tokens. Bayesian linear or logistic regression. Only the chosen mode is updated (bandit feedback).

**Prior.** The original puts a Gaussian prior on reward rate worth 60 seconds of experience (a02). Our analogue: an initial belief that each mode has pass rate equal to the global average and cost equal to its cap, with the weight of a handful of observations.

**Lambda (the price of a token).** The original sets it as reward rate times time (an opportunity cost; a01). Three ways for us:
1. Fixed by hand and tuned on a dev set.
2. Set from the budget as a dual variable. RACER raises lambda by a primal-dual step when spending runs over the budget, and lowers it toward zero when the budget does not bind (d09, K21).
3. Estimate it from the running ratio of passes per token in the whole stream (the human reward-rate view; a07, a08).

**What the features must satisfy.** They are cheap to compute before running (a few tokens or pure code), and they predict which mode wins. Candidates seen in the literature:
- Problem size (item length, number of options or hypotheses). Used for LLM strategy shift (c12) and in the oracle-gap split (d06).
- The class's running pass rate (difficulty), as in Snell's bins (d03), but learned from the log, not from 2048 samples.
- Structure cues the program can compute, such as the payoff-structure cue in planning (a26) or "does a check exist".
- Do not hard-code the direction of an uncertainty cue (K14).

### 4.2 The simplest version: a class table without regression

The 2017 data say that in a homogeneous stream a context-free running average per mode ties the feature model (a10, b01, K03). So a table keyed by problem class, holding a Beta posterior over pass rate and a running mean of tokens per mode, is the first implementation. Add regression on features only when classes mix inside one key.

Algorithm sketch:

```
state[class][mode] = {alpha, beta, mean_tokens, n}
choose(class):
    for mode in modes:
        p = sample Beta(alpha, beta)
        c = mean_tokens (or sampled)
        score[mode] = p - lambda * c
    return argmax score
update(class, mode, passed, tokens):
    if passed: alpha += 1 else: beta += 1
    mean_tokens += (tokens - mean_tokens) / n
    decay: alpha, beta move toward prior by gamma each step
```

The decay line is from Russo et al. (d02): update Beta so it decays toward the prior with gamma about 0.01 (simulated). Or use a sliding window of the last tau plays (d01, d13). Without forgetting, the table stops exploring and cannot track drift.

### 4.3 When class keys are not enough: what the 2015 and 2017 experiments show

Context-free learners (SSL, RELACS) learn one value per strategy. In a mixed stream where the right strategy flips between problems, they fall to chance (50% in simulation at a 50/50 mix; c02). Metareasoning stays above 70%. Human data: 64.6% (b02) and 76.2% (a09). So the class key must carry the cue that separates problem kinds. If it does not, the table is SSL and will collapse to one mode. Test: run a mixed stream where one fixed mode scores near chance.

SCADS is a middle design: it learns by category plus a global association. The global association swamped the category ones in simulation, so it collapsed to one strategy (a06, a35). Engineering lesson: if you mix a global prior with class-specific values, cap the global term's weight.

### 4.4 Metalevel (inside-the-solve) control: BMPS and VOC features

For choosing the next computation inside one solve, not the mode up front, BMPS uses a linear score of VOI1, VPI and cost (a20). Practical points:
- At high cost, the policy reduces to myopic VOI minus cost (weights 0.00 VPI, 1.00 VOI1, -1.00 cost).
- At low cost, it adds VPI and weights cost heavily (-4.5).
- It needs an exact model of the agent's own belief updates (a metalevel MDP). An LLM has none.
- The practical analogue for us is a two-feature score. For example, an S6 impasse trigger could use "expected gain of one more attempt" (estimated from the class's past gain per extra attempt) minus lambda times attempt cost. This is a design suggestion, not tested by anyone (K18 agent_test).

### 4.5 Process feedback as the learning signal (the tutor result)

The tutor gives the learner two things after each planning step: a delay penalty if the step was a poor use of time, and a hint of what the best step was (b09, b12). Both are needed (87.5 vs 75.8 for both; neither alone beats none). The analogue for the class table is to log not only "pass/fail" but also, per attempt, which step used tokens without changing the outcome, and what the cheaper passing mode would have been. Nobody has tested this on an LLM (critique gap 5).

### 4.6 Learning rule used by people for new strategies

Gradient-style (REINFORCE family) learning won the model comparison (b17, b18). Mechanism unsettled (b19). It matters because it says what real learners do when the set of strategies is open. For us the safe reading: do not rely on online discovery of new modes (K08). Keep a small fixed set.

### 4.7 Non-stationarity (what to do when the problem mix shifts)

- People adapt slowly and unevenly after change (b05). LVOC needs change detection because people unlearn faster than the model (a18).
- Algorithms: discounted or sliding-window UCB (d01), Thompson with decaying Beta (d02). Best window is smaller when change is frequent, and as large as possible when there is no change (d13).
- No sample count for small tables exists (d13). Measure by log replay.

### 4.8 Resource-rational recipe as an agent design rule

The five-step recipe (section 1) applies to the schema itself: for each element ask what it computes, what it costs in tokens, and what the best cheap version is. G7 ("the schema must pay for itself") is this rule.

---

## 5. What holds up

### 5.1 Replications and independent confirmations

- **No independent replication of the 2017 human experiments was found.** The search was blocked (web quota exhausted; K22, d12). Absence of evidence only. Do not cite K02 or K03 as replicated.
- Outside-lab human data are: Rieskamp (2008) reanalyses of Newell et al. and Broder and Schiffer (b04, b05), done by the SSL author with his own theory, not preregistered; and the older Payne et al. (1988) results (a33, not opened).
- The anchoring result is contested: Lieder et al. 2018 find cost effects for provided anchors, Epley and Gilovich 2006 found none, Simmons et al. 2010 agree with Lieder (a24).
- The strategy-selection programme is supported across **different lines** by the same shape of finding (people track cost and structure), but all from the same group.

### 5.2 Where the theory loses or ties

- Homogeneous environments: SSL ties or wins (K03 [E]). Features only pay when classes mix.
- Quantitatively: 2015 tie (MSE 0.0050 vs 0.0048), 2017 clear SSL win (BIC 60.70 vs 68.94; MSE 0.0018 vs 0.0043) on the same Rieskamp and Otto data. The fits differ (2 free parameters on block averages vs choice-level BIC) (critique 3).
- People beat the model in Experiment 1 (83.0% vs 70.5%) and in the Experiment 2 pretest. The model under-predicts adaptivity (a04, a07).
- Start-up behaviour was fitted, not predicted (b27).
- Planning: the optimal model is not best in the constant-variance condition (a26).
- The learning rule in planning is SSL-style in under 1% of people (b17), while SSL is the best fit to older choice data. Different tasks.
- Mixed-environment evidence has a caveat: trial-1 success suggests prior skill, and a single general strategy might do well on both problem kinds (a09). In the 2015 version no learning was seen over 30 trials (b02).
- Experiment 3 effect is small (d 0.26) with 28% excluded (a08).

### 5.3 Moderators and boundary conditions

- Environment mix: context only matters when problems differ in which strategy wins.
- Feature informativeness: with explicit cue validities, features carry no extra information, so context-free models do as well (a10).
- Time pressure, probability dispersion (a06), reward rate (a07, a08), error cost (a23, a24) all move strategy choice in the predicted direction in humans.
- Task size: a tutor must match the real task size (b15).
- Task similarity for transfer: far transfer is weak (d=0.17, b11).

### 5.4 What worked

- Process-level feedback with both a penalty and a hint (b09, b12): d 0.32 to 0.88 depending on design.
- Plain-language procedural instructions derived from the optimal strategy (a31).
- A hierarchical-strategy tutor for large tasks (b15).
- A pre-registered tutor: tutor matched the model-strategy score and beat no tutor (b16).
- LLM side: trained effort routers (ARES), cost-aware training (RaM), bandits over strategies (Meta-Reasoner).

### 5.5 What did not work

- Action feedback (telling the person if the action was right): no gain (b09, d=-0.09; 49.0 vs 57.6 in Exp 2).
- Delay-only or hint-only feedback (b12).
- Passive video demonstration: worse than practice on far transfer (23.5% vs 39.4 to 46.3%; b13).
- Tutors limited to small tasks (b15). Dummy tutor (b16).
- Told the principle only: lost to the tutor (38.0 vs 24.2, workshop; b14).
- Unaided strategy discovery: 28.57% after 120 trials (b17).
- In LLMs: telling the model which named strategy to use (d15); asking the model to pick its own mode (c26, c19); vanilla GRPO router collapsed to one mode (b24); a heavy search method on easy items (d04).

### 5.6 Competing explanations to keep in mind

- Engagement drop in Experiment 2 could be plain disengagement. Experiment 3 was built to separate this (a07, a08).
- Mixed-environment success could be prior expertise or one complex strategy (a09, b02).
- Effects in the tutor work shrank as designs tightened (b28), and the first workshop test treated trials as independent (b14).
- The LLM routing gains may be partly sampling: any-of-k coverage rises log-linearly with k (d07), and part of the gain from voting is noise averaging (G4).

### 5.7 Quality of the LLM evidence

- Mostly 2026 preprints. Several use LLM-judged rewards (Meta-Reasoner, MetaScale, R2-Router quality judging), small test sets (Airline about 50 tasks, Chain of Simulation 50 per set), or routers trained per setting (ARES: fine-tuned Qwen3-1.7B).
- Model routing (RouteLLM, FrugalGPT, R2-Router) is a different decision from choosing a reasoning mode inside one model.
- Small single-author results (Chain of Simulation GSM8K +1.0 with n=50; Monitor-Generate-Verify 75.42% vs 68.44%, 659 items, single run, 27-37% more time) are noise-level or preliminary and not used as support (c28, c29, K17).
- No paper runs the pure Lieder-Griffiths form on an LLM, and no paper runs an LLM through the human paradigms (Mouselab, SSL tasks, sorting selection) against human data (c33; search only).

---

## 6. Language models

### 6.1 Do LLMs select strategies by problem features?

- **Partly, and weakly.** In a variable-attribution task, four models (DeepSeek R1 and V3, Qwen3-Next-80B Thinking and Instruct) move from enumerating pairs to elimination as the hypothesis space grows. Logistic fit: beta(log size) +1.0212, beta(trials) -0.1466, p<.001, pseudo R2 0.160 (c11, c12, b20). Little shift on XOR, where pruning helps little. This is size tracking, not shown to be cost-optimal. Strategy labels come from a Kimi-K2 judge (accuracy 0.86, kappa 0.76 on 100 human-labelled cases). No human data collected. Effort grows linearly with size and trials. Reasoning models stay near-perfect; instruct models fall on XOR/XNOR; direct answers fall to chance (c13). The critique confirmed these values.
- **Named strategies do not help.** Telling the model to use supposition-following, chain construction, compositional or concatenation reasoning gave 45.1 to 49.0 vs 47.2 for no strategy (Phi-4, TruthQuest). Same on R1-Distill and ZebraLogic (c21, d15). The label is not the lever.
- **LLMs do not self-gate.** Asked whether to use reasoning mode, Qwen3 judges say yes 99.5 to 99.9% of the time. Cost is 6.25 to 19.07 times all-instruct. Accuracy is the same as all-reasoning, within 0.01 (c26 and critique 1.8). GPT-5 as an effort router got 40.0 on Retail vs ARES 54.8 (c14); Gemini-3-Pro 46.1. A GPT-5 router was 14.8 points below ARES on the first backbone (d11). Direct LLM arm selection got 82 vs LinUCB 89 on Game of 24 (c19). On TheoremQA direct selection fell near plain CoT (about 39-40 vs 84.13 full; c19, extracted table jumbled). **So the mode choice must be made by code from logged outcomes (G5).**

### 6.2 What changed behaviour, and by how much

| Intervention | Effect | Source | Needs training? |
|---|---|---|---|
| VOC-style reward in expert iteration (RaM) | 35-42% fewer tokens vs few-shot, 23-32% vs STaR; accuracy kept or raised in domain; one OOD 8B row lost 3.8 points (intervals +/-2.4 overlap) | a28, b21, c10 | yes |
| Learned effort router (ARES) | Same success as High on Retail with up to 52.7% fewer reasoning tokens; BrowseComp-Plus 41.3 vs 42.7; WebArena 46.5 vs 45.0 | c14 | yes (router, per setting) |
| ARES with RL and cost penalty | Airline 36.0 to 42.0, tokens 678k to 133k; Retail 54.8 to 58.5, 476k vs 1007k | c16 | yes |
| ARES ablations | Untrained router 41.7 (-13 points); no rationale -3.5 | c15 | yes |
| ARES stronger backbone | gpt-oss-120b Retail High 67.8 (558k), ARES 65.2 (428k), 23% fewer tokens; loses 2.6 points | d11 | yes |
| ARES reward design | Without normalised cost, router uses medium less after about 80 steps in Airline where medium is best | d11 | yes |
| Thinkless | 50-90% fewer long chains; vanilla GRPO collapsed to one mode, loss split fixed it | b24 | yes |
| RouteLLM | 95% of GPT-4 on MT-Bench at 2x lower cost; weak routers only in-distribution; Arena-only data equals random on MMLU | b22 | yes |
| FrugalGPT | Up to 98% cost cut or +4% at same cost | b23 | yes |
| R2-Router | 4-5x cheaper at equal quality; OOD AUDC 0.71 vs 0.67 | c27 | yes |
| RACER (Lagrange lambda) | +0.64 to +1.10 over three routers at C=4 | d09 | yes (neural router) |
| Meta-Reasoner (LinUCB over strategies) | Game of 24: 89 / 92 vs ToT 65, MACM 80, CoT 4 | c18, c19 | no (bandit and prompts), but LLM-scored rewards |
| MetaScale (UCB over meta-thoughts plus genetic step) | Arena-Hard GPT-4o 93.14 vs CoT 84.72 vs best-of-N 87.42; tokens 573 to 699; Llama-3.1-8B 18.94 vanilla, 12.50 CoT, 30.86 MetaScale | c20 | no, but LLM-judged |
| Direction-informed gate (DIAL) | Best success in 16 of 18 cells; one cell 49.8 vs always-trigger 59.8 | c24 | needs counterfactual runs |
| Snell compute-optimal by difficulty bin | About 4x less compute than best-of-N (MATH); bins cost 2048 samples per question | d03, d14 | no (inference), but estimation cost uncounted |
| Overthinking fix (self-training) | 48.6% fewer tokens at same accuracy on MATH500 | d08 | yes |

### 6.3 Where more thinking hurts

- Airline High 38.0 vs Medium 42.0 (c16).
- Judging: reasoning helps with explicit verification, is redundant when surface cues decide, and hurts when it widens the evaluation scope (c25).
- Beam search against a PRM on easy MATH bins (d04).
- First solution round already correct in over 92% of cases and under 60% of tokens (d08).
- RaM saved most on knowledge tasks, least on maths and logic (a29). Chains mainly help on maths and logic (c08).
- Easy items: SCHEMA G11 already says this and K11 adds sources.

### 6.4 Why selection recovers little in logic puzzles (oracle gap)

TruthQuest Phi-4: oracle over strategies 82.9 vs no strategy 47.2. Best post-hoc rule: vote+prob 57.3 (c21, c22). R1-Distill: oracle 90.1, verifier 74.1, vote 68.4. No rule wins everywhere. But the oracle is any-of-five prompts with no same-sample-count control (d05), and any-of-k rises with k alone (d07). The gap shrinks on hard items (d06). So most of 82.9 is not selectable. K13 is [S].

Contrast: in agent tasks (ARES) routers recover nearly all of high-effort success. The likely reason is that ARES targets cost, not accuracy above the best fixed setting (critique 3).

### 6.5 Cue reliability

The sign of the link between token entropy and the benefit of extra compute flips across environments and backbones. Spearman examples (c23): HotpotQA Qwen3 -0.327, Phi-3.5 +0.184, Llama-3.1 -0.346; WebShop +0.133, +0.335, +0.287; FEVER -0.119, -0.156, +0.428; APPS +0.317, -0.024, -0.249. The classic VOC >= 0 assumption fails. **Never hard-code the direction of a cue; estimate it per class.**

---

## 7. What our agent should take

Marks: schema part G (guardrail), S (state), O (operator), memory. Status [E] established, [S] single-source, [C] contested.

### 7.1 Add now (established)

1. **Choose the mode by code, never by asking the model.** (G5, S0.) [E] K12; c26, c19, c14, c21, d15. Self-routing picks reasoning 99.5 to 99.9% of the time; LLM routers lose to learned ones by 8 to 15 points. SCHEMA S0 already says "the program decides"; make explicit that S0 is not an LLM call, and log the share of long mode chosen.
2. **Do not tell the model to use a named strategy as a general prompt.** (S1, S3, 4b.) [E] K11; c21, d15 (named strategies 45.1-49.0 vs 47.2). Add to 4b: "naming a strategy in the prompt does not raise accuracy".
3. **Short mode on easy classes; a fixed high-effort policy is not optimal.** (G11, S0.) [E] K11; c16, c25, d04, d08. Already in G11. Add the specific support (Airline, judge tasks, easy MATH bins, 92% first-round correct) and make S0 route easy classes to direct or short.
4. **Learn the effort or mode from logged outcomes and expect a cost cut at about equal quality.** (S0, G12.) [E] K10; six independent sources (c14, b22, b23, c27, b24, d09, d11). Supports the gate in principle. The exact code-only form is untested (see Test first).
5. **A context-free per-mode average is enough on a homogeneous stream; features matter only when classes mix.** (S0.) [E] K03; a10, b01, c02. Build the class table first, add feature regression only where one key hides different best modes.
6. **Keep a forgetting rule in any running class table.** (S0, memory class record.) [S] K19 (two theory sources, d01, d02). Marked here because it is plain algorithm theory: a stationary bandit stops exploring. Promote to "Add now" only as an engineering safeguard (window or decayed Beta), not as a performance claim. Its value on our streams is a test.
7. **Estimate slow, asymmetric adaptation after a shift as the baseline and log recovery.** (memory.) [E] K04; b04, b05. People adapt slowly. Our class record needs change detection. Log tokens to recover after a new problem family appears.
8. **Do not hard-code the direction of a cue.** (S0, G1.) [S] K14, but the principle (sign flips across 12 environment-backbone pairs) is a safeguard. Estimate any cue's effect from our own paired runs.

Item 8 is [S]. It is listed here as a rule of caution, not as a performance claim.

### 7.2 Test first (single-source or contested)

| Item | Schema part | Status | Evidence | Why test first |
|---|---|---|---|---|
| Code-only class table: Beta posterior over pass rate and mean tokens per (class, mode), Thompson-sampled, choose argmax(pass - lambda * tokens) | S0 | [S] | K01, K10, K16; a01, a02, c01, c14, c18 | No one has run this exact form on an LLM. Human and simulation evidence from one lab; LLM routers are trained neural models |
| Feature regression (size, running pass rate) inside the table | S0 | [S] | K15, K20, K02; c12, d03, a09 | Features win only in mixed streams (K03); size predicts LLM strategy with pseudo R2 0.160 |
| Lambda as a dual variable that targets a token budget | G12 | [S] | K21; d09 | Not compared with best fixed budget |
| Opportunity-cost lambda: long-mode share falls as lambda rises | G12 | [C] | K05; a07, a08, a23, a24 | Human evidence contested and small effects; the LLM analogue has no direct test |
| Class-conditioned token cap (prompt-only analogue of RaM) | G12 | [S] | K09; a28, a29, c09 | RaM is trained; the prompt-only cap is untested |
| Per-class direction of any cue estimated from paired runs | S0 | [S] | K14; c23, c24 | DIAL needs counterfactual runs, and always-trigger sometimes wins |
| Difficulty from running pass rate as the gate feature | S0, G12 | [S] | K20; d03, d04, d14 | Snell's bins cost 2048 samples per question; ours must be free |
| Process-level feedback in the class record (which step wasted tokens) | memory, S9 | [S] | K07; b09, b12, b10 | Human result, one lab, d=0.59 near and 0.17 far |
| Bandit over operators at S6 with code-checked reward | O1-O8, S6 | [E] for bandit-over-strategy gain, but rewards were LLM-scored | K16; c18, c19, c20 | Needs a code-only reward variant |
| Selection value above vote at equal samples | G5, S7 | [S] | K13; c21, c22, d05, d07 | The oracle gap is inflated; only the part above equal-sample vote counts |
| Fixed small mode set; test a fifth mode | S0 | [S] | K08; b17, b18 | Do not rely on online discovery; humans reach 28.57% in 120 trials |
| Shape of a two-feature S6 trigger (expected gain per extra attempt minus lambda * cost) | S6 | [D] | K18; a20, a21 | BMPS is the origin; analogue is our own design |

---

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, with all estimation, exploration and setup tokens counted (G7). Report pass rate per 1000 tokens and absolute pass rate. Use code-checked rewards only (G5, G8). Use repeated runs per item where noted, since a single run mixes selection value with sampling noise.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed-class stream (ARC-like grid items, BRAINTEASER, short exact-answer items) with at least 4 classes, each with a different best mode | (a) always direct; (b) always checked; (c) always step-by-step; (d) code class table, Thompson-sampled argmax(pass - lambda * tokens); (e) LLM-chosen mode | Pass rate per 1000 tokens; share of long mode chosen | (d) beats the best fixed arm by a few points per token; (e) chooses the long mode over 90% of the time and does not beat fixed-long (c26, K12). If (d) does not beat the best fixed arm, the gate is not worth it |
| T2 | Single-class stream (one item family) | (a) feature-free running average per mode; (b) feature table | Same | Tie (K03). If (b) wins, the features carry information; if (a) wins by more than noise, drop the features |
| T3 | Mixed stream where the best mode flips by a cheap cue and one fixed mode scores near chance | (a) per-mode average, context-free; (b) cue-keyed table | Pass rate | (b) above (a), as in a09 and c02. Confirms that class keys matter |
| T4 | Same mixed stream with a mid-log shift (new problem family appears) | no decay; sliding window; Beta decay gamma 0.01 and 0.05; reset on change detection | Tokens and items to recover the pre-shift pass rate | Decay or window recovers faster than none (K19). Log replay is enough; no new model calls |
| T5 | Items at three budgets per class (low, medium, high token caps) | fixed cap uniform; cap by class easy/hard record | Pass rate per class at each cap; accuracy at equal total tokens | Short cap equals or beats long cap on easy and knowledge classes (K11, K09). Gives the missing per-class table (critique gap 7) |
| T6 | Lambda sweep | lambda fixed at 4 values; lambda as dual variable targeting a token budget | Long-mode share vs lambda; pass rate at matched total tokens | Long share falls as lambda rises (K05 analogue); dual lambda matches the best fixed lambda at the same budget (K21) |
| T7 | Cue direction check: for each class, paired runs with and without extra compute | cue-gated trigger (hard-coded direction); learned direction per class; always-trigger | Pass rate at matched tokens | Direction differs by class on at least a third of classes (K14). Learned direction beats hard-coded |
| T8 | Oracle gap with control: three runs per item of one mode vs one run each of three modes | any-of-3 same mode vs any-of-3 across modes; majority vote across both | Coverage and vote accuracy | Part of the "strategy oracle" gap shows up in same-mode any-of-3 (d07). Only the excess is selection value (K13) |
| T9 | Difficulty feature cost | difficulty from running class pass rate (free) vs from 8 to 32 pre-samples per item | Pass rate at matched total tokens including pre-samples | The free feature matches or beats the pre-sample one at equal tokens (K20, d14). Settles whether Snell's 4x holds with cost counted |
| T10 | Process-feedback logging | class record fed only final pass/fail vs class record fed pass/fail plus "tokens spent after the first correct candidate" and "cheapest mode that passed" | Quality of table (regret vs offline best mode) at equal logged runs | Richer log reaches low regret in fewer runs (K07). Replay only |
| T11 | Bandit over S6 operators with code-checked reward | Thompson over O1-O8 using pass on the subgoal; uniform operator choice; LLM-chosen operator | Subgoals solved per 1000 tokens | Bandit above uniform and above LLM-chosen (K16, K12). Needs enough impasses; may be too sparse (UNKNOWNS) |
| T12 | Model-size effect of the gate | Same T1 on two backbones | Whether the winning cue and mode differ by backbone | Differences exist (K14); the table must be relearned per backbone |

Reporting rules: give the pass rate with an interval and N per class. Report the table's regret against the best fixed mode per class chosen after the fact. Report how many logged runs per class the table needed before it beat the global best fixed mode (critique gap 3).

---

## 9. What does not transfer, and why

- **Human strategies are external procedures with known run time.** Sorting steps, loan-choice rules, planning clicks. Our modes are text-generation policies whose cost and quality are noisy and vary by sample. Run-time models (a05, linear in operation counts) do not carry over; token cost per mode is learned from logs.
- **Human reward rate and boredom.** The opportunity-cost story (a07, a08) uses a person's earnings per second. An LLM has no wage. Lambda must be set by budget (d09) or by tuning. The human effects are also small (d 0.16 to 0.26) with high exclusion.
- **Human prior knowledge at trial 1.** 73% correct on trial 1 (a09). An LLM's prior is its training. We cannot assume the model comes in with the right preference, and (c26) it comes in preferring the long mode.
- **Hand-set features.** In every model the features are given. Choosing and computing features for open LLM tasks is unsolved here (critique gap 2).
- **Fixed strategy set.** The 2017 model assumes it (a12). Humans find new strategies in under 30% of cases in 120 trials (b17). Our agent should not rely on discovering modes online.
- **BMPS.** Needs an exact model of the agent's own belief updates (a20). Not available for an LLM.
- **Tutor results.** Process feedback in a 3-step or 5-step click task; transfer to the road-trip task is weak (b11). Mapping to token-level feedback for an LLM is a design guess.
- **Trained routers and RaM.** Need fine-tuning, a gold answer, or per-setting training. This clashes with our no-training scaffold rule. Only the shape (reward minus cost, difficulty-dependent length) carries over, not the method.
- **Model routing papers.** RouteLLM, FrugalGPT and R2-Router choose between models. We have one model. The transferable part is cost-aware selection from logged outcomes, not the model cascade.
- **LLM-judged rewards.** Meta-Reasoner and MetaScale score progress and win rate with an LLM. G5 and G8 forbid model judges as selectors. Their gains give the shape, not the number.
- **Maths and code benchmarks.** Snell, Brown and Chen use MATH, GSM8K and code. Some Chen percentages were read from a figure. They show the per-class shape, not our task mix.
- **Simulated p-values.** LVOC's t(959998) shows significance from simulated N is meaningless (a19).
- **Chain-of-Simulation and Monitor-Generate-Verify.** Within noise or single-run (K17).

---

## 10. Open questions

1. Does a code-only class table (Thompson-sampled pass minus lambda tokens) beat fixed modes and an LLM-chosen mode at equal tokens? No study runs this form. Only our logs can answer (critique gap 1).
2. Which cheap features separate classes well enough to pay? Size predicts strategy (pseudo R2 0.160). The sign of entropy flips. No backbone-stable feature set is known (gap 2).
3. How many logged runs per class are needed before the table beats one global mode? How fast does it go stale after a shift? (gap 3, d13 gives only asymptotic orders.)
4. Is lambda fixed or estimated? What lambda makes the gate match the best fixed budget? (gap 4, d09.)
5. Does process-level feedback improve a class table more than outcome-only logs? Human-only, one lab (gap 5).
6. How much of the strategy oracle gap is selectable and how much is sampling? Needs repeated runs per item (gap 6).
7. When is the short mode better than the long mode on our classes? Needs pass rate per class at three budgets (gap 7).
8. Do the 2017 human results replicate outside the lab? Does the 83% vs 70.5% gap (people beat the model) reflect prior knowledge an LLM also has? (gap 8; K22 on hold.)
9. Can strategy discovery (adding a mode) be done safely online? (gap 9; humans under 30%.)
10. Do LLMs show the human signatures (reward-rate sensitivity, slow asymmetric switching, trial-1 preferences) if run through the actual paradigms? No such study found (c33, search only).
11. The 2020 BBS article, Rieskamp and Otto 2006, Payne 1988, Russell and Wefald 1991 and Scheibehenne 2013 were not opened. Checking them could change the history in section 2.
12. Does tutor-style feedback at a high level (which mode wasted tokens) help a class table, or only a learner who changes habits?

---

## 11. Sources

[V] = opened and read this run (full text or PDF text). [M] = snippet or abstract only, or second-hand.

**Lieder and Griffiths lab, strategy selection and resource-rational analysis**
- [V] Lieder and Griffiths (2017) Strategy selection as rational metareasoning. Psychological Review 124. https://osf.io/6yugk/ (OSF preprint text) (a01-a12; numbers re-opened in critique)
- [M] Same paper, publisher page and abstract. https://is.mpg.de/publications/lieder2017strategy (b06)
- [V] Lieder, Plunkett, Hamrick, Russell, Hay, Griffiths (2014) Algorithm selection by rational metareasoning as a model of human strategy selection. NIPS. https://papers.neurips.cc/paper_files/paper/2014/hash/87b5e7e570f757a0b99f0a370ce2438c-Abstract.html (a13-a16)
- [V] Lieder and Griffiths (2015) When to use which heuristic: a rational solution to the strategy selection problem. CogSci. https://journalpub.escholarship.org/cognitivesciencesociety/article/25608/galley/15232/download (b01-b03, b27, c01-c04)
- [V] Lieder, Shenhav, Musslick, Griffiths (2018) Rational metareasoning and the plasticity of cognitive control. PLOS Comput Biol. https://doi.org/10.1371/journal.pcbi.1006043 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC5937797/ (a17-a19, b07)
- [V] Lieder, Griffiths, Huys, Goodman (2018) The anchoring bias reflects rational use of cognitive resources. Psychon Bull Rev. https://doi.org/10.3758/s13423-017-1286-8 (a22)
- [V] Lieder, Griffiths, Huys, Goodman (2018) Empirical evidence for resource-rational anchoring and adjustment. Psychon Bull Rev. https://doi.org/10.3758/s13423-017-1288-6 (a23, a24)
- [M] Lieder and Griffiths (2020) Resource-rational analysis. Behavioral and Brain Sciences 43. https://doi.org/10.1017/s0140525x1900061x ; https://perception.jhu.edu/files/PDFs/20_ResourceRationality/LiederGriffiths_ResourceRationality_BBS.pdf (a36, b08; PDF blocked, commentaries seen through search summaries)

**Metareasoning and planning**
- [V] Callaway, Gul, Krueger, Griffiths, Lieder (2018) Learning to select computations (BMPS). UAI. https://arxiv.org/abs/1711.06892 (a20, a21)
- [V] Callaway, Lieder, Das, Gul, Krueger, Griffiths (2018) A resource-rational analysis of human planning. CogSci. https://cocosci.princeton.edu/papers/Callaway_CogSci_2018.pdf (c05, c06)
- [V] Callaway et al. (2022) Rational use of cognitive resources in human planning. Nature Human Behaviour. https://doi.org/10.1038/s41562-022-01332-8 (a25-a27; conference version also opened)
- [M] Same article, abstract-level (c32).

**Tutoring, feedback and discovery**
- [V] Callaway, Jain, van Opheusden, et al. (2022) Leveraging AI to improve human planning (PNAS). https://cocosci.princeton.edu/papers/callawayleveraging.pdf (b09-b13, b28)
- [V] Lieder, Callaway, Jain, et al. (2019) A cognitive tutor for helping people overcome present bias. https://cocosci.dreamhosters.com/papers/liedera.pdf (b14)
- [V] Hierarchical planning strategy discovery and tutoring. https://arxiv.org/pdf/2102.00521 (b15)
- [V] Heindrich et al. (2023, v3 2025) An intelligent tutor for planning in large partially observable environments. https://arxiv.org/pdf/2302.02785 (b16)
- [V] Becker, Lieder et al. (2022) Boosting human decision-making with AI-generated decision aids. Comput Brain Behav. https://doi.org/10.1007/s42113-022-00149-y (a31; abstract and parts of method only)
- [V] He and Lieder (2024) Experience-driven discovery of planning strategies. https://arxiv.org/pdf/2412.03111 (b17)
- [V] Jain et al. (2023) What are the mechanisms underlying metacognitive learning? https://arxiv.org/pdf/2302.04840 (b18)
- [V] He and Lieder (2025) Individual differences in the cognitive mechanisms of planning strategy discovery. https://arxiv.org/pdf/2505.23519 (b19)

**Rival theories and older data**
- [V] Rieskamp (2008) The importance of learning when making inferences. Judgment and Decision Making 3(3). https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B10C661EEC4CEDF5216FA41395963DE2/S193029750000245Xa.pdf/the-importance-of-learning-when-making-inferences.pdf (b04, b05)
- [M] Rieskamp and Otto (2006) SSL. https://edoc.unibas.ch/8222 (a32, b26)
- [M] Payne, Bettman, Johnson (1988) Adaptive strategy selection in decision making (a33; no URL recorded)
- [M] Russell and Wefald (1991) Do the right thing (a34; no URL recorded)
- [M] Shrager and Siegler (1998) SCADS; Siegler (1996) (a35; no URL recorded)
- [M] Scheibehenne, Rieskamp, Wagenmakers (2013) Testing adaptive toolbox models. https://edoc.unibas.ch/27295/ (b25)
- [V] Nobandegani et al. (2018) Over-representation of extreme events in decision-making. https://arxiv.org/abs/1801.09848 (a30; not a Lieder paper, do not cite as one)

**Language models**
- [V] De Sabbata, Sumers, AlKhamissi, Bosselut, Griffiths (2025) Rational Metareasoning for Large Language Models. https://arxiv.org/abs/2410.05563 ; https://arxiv.org/pdf/2410.05563 (a28, a29, b21, c07-c10)
- [V] Hu, Roshan, Varma (2026) Are More Tokens Rational? https://arxiv.org/abs/2602.10329 ; https://arxiv.org/pdf/2602.10329 (b20, c11-c13)
- [V] Yang, Hou, Wei, Bao, Chang (2026) ARES. https://arxiv.org/abs/2603.07915 (c14-c17, d11)
- [V] Sui et al. (2026) Meta-Reasoner. https://arxiv.org/abs/2502.19918 (c18, c19)
- [V] Liu et al. (2025) MetaScale. https://arxiv.org/abs/2503.13447 (c20)
- [V] Zhang, Wisniewski, Tomeh, Charnois (2025) Reasoning strategies in LLMs: can they follow, choose, and combine them. https://arxiv.org/abs/2507.11423 (c21, c22, d05, d06, d15)
- [V] Li et al. (2026) Same Signal, Opposite Meaning (DIAL). https://arxiv.org/abs/2605.06908 (c23, c24)
- [V] Zhang, Zhang, Xiang, Cai (2026) Reasoning Is Not Free (RACER). https://arxiv.org/abs/2605.10805 (c25, c26, d09, d10)
- [V] Xue et al. (2026) R2-Router. https://arxiv.org/abs/2602.02823 (c27)
- [V] Ong et al. (2024) RouteLLM. https://arxiv.org/pdf/2406.18665 (b22)
- [V] Chen, Zaharia, Zou (2023) FrugalGPT. https://arxiv.org/pdf/2305.05176 (b23)
- [V] Fang, Ma, Wang (2025) Thinkless. https://arxiv.org/pdf/2505.13379 (b24)
- [V] Sheikhi (2026) Chain of Simulation. https://arxiv.org/abs/2602.02842 (c28; weak)
- [V] Oh (2025) Before you think, monitor. https://arxiv.org/abs/2510.16374 (c29; weak)
- [M] Paglieri et al. (2025) Learning When to Plan. https://arxiv.org/abs/2509.03581 (c30; abstract only)
- [M] Qian et al. (2025) xRouter. https://arxiv.org/abs/2510.08439 (c31; abstract only)
- [V] Snell, Lee, Xu, Kumar (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 (d03, d04, d14)
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (d07)
- [V] Chen, Xu, Liang et al. (2025) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187 (d08)

**Bandit theory**
- [V] Garivier and Moulines (2008) On upper-confidence bound policies for non-stationary bandit problems. https://arxiv.org/abs/0805.3415 (d01, d13)
- [V] Russo, Van Roy, Kazerouni, Osband, Wen (2018) A tutorial on Thompson sampling. https://arxiv.org/abs/1707.02038 (d02)

**Search notes**
- [M] c33: no LLM-on-Mouselab / SSL-paradigm / sorting-selection study found (search only). d12: failed search for independent replications (web quota exhausted).
