# Active inference decision theory: deep document

*Subfield B03.03. Evidence files: evidence_a-d.jsonl (ids a01-a28, b01-b27, c01-c27, d01-d19). Claims: claims.jsonl (B03.03-K01 to K28). Cross-check: critique.md. Written 2026-11-03. Numbers were checked against the full text in the critique pass unless marked otherwise.*

## 1. What it is

Active inference is a theory of how an agent chooses what to do. The agent holds beliefs about hidden states of the world. It picks the plan (policy) whose predicted future has the lowest **expected free energy (EFE)**, written G.

The key idea for us: G has two parts that are scored in one number.
- **Pragmatic (extrinsic) value.** How close are the predicted outcomes to the outcomes the agent prefers (the goal)? [a01, c04]
- **Epistemic (intrinsic) value.** How much will the agent learn about hidden states (or about model parameters) if it takes this action? This is expected information gain (EIG). [a01, a02, a03]

There is no separate "exploration bonus". Information seeking and goal seeking fall out of one objective. Policy probability is a softmax of minus G. [a01]

Two equivalent ways to write G [a01, c04]:
1. Risk plus ambiguity: KL between predicted and preferred outcomes, plus the expected entropy of outcomes given states.
2. Minus expected information gain, minus expected log preferred outcomes (extrinsic value).

Special cases [b09, a02, a16]:
- Drop the preferences: you get Bayesian optimal experimental design (pick the max-EIG action).
- Drop ambiguity and relative risk: you get expected utility (pure exploitation, RL).
- Keep both: goal-directed information seeking.

**Why it matters for our agent.** Schema state S7 (SELECT) says: if two rules still fit, run the one input where they differ (a discriminating test). That is the epistemic term of EFE applied to a hypothesis set. The goal checker is the pragmatic term. The question for this subfield: does it pay to compute the EIG of candidate tests explicitly, and how do we do it with a language model that cannot give clean likelihoods?

**Honest framing.** Almost no LLM paper in this area calls its method "active inference". They use Bayesian experimental design (BED) or expected information gain. The evidence for EIG-based test choice in LLMs is real. The evidence for the EFE form as such (with a pragmatic term) in LLMs is thin and confounded (K19). We take the EIG part. We treat the pragmatic term as a design choice, not a proven gain.

## 2. History and theories in depth

### 2.1 Roots: information as value
- Lindley-style Bayesian design and active learning give the idea that the best experiment is the one with the highest expected information gain. Active inference papers trace the epistemic value to this line [a20, a02].
- Nelson et al. (2010) is a human behavioural test of which information measure people use. Three experiments, built by computer search to pull four measures apart (information gain, KL distance, probability gain, impact). With experience-based learning, **probability gain** (error minimisation) explained search better than Shannon information gain [d13]. Only the abstract was opened. This is the one direct human challenge to "Shannon EIG is the right measure".

### 2.2 Friston and colleagues: EFE as the single objective
- Friston, Rigoli, Ognibene, Mathys, FitzGerald, Pezzulo (2015) "Active inference and epistemic value" is the founding paper for epistemic value in this scheme. Secondary sources describe it as showing that minimising EFE in a T-maze with a cue gives cue-then-reward behaviour with no separate bonus. **Not opened** (paywalled), so no numbers from it [a04].
- Schwartenbeck et al. (2019, eLife) separate **state exploration** (find out which context you are in; "active inference") from **parameter exploration** (learn reward statistics; "active learning"). In simulated T-maze runs (1000 experiments of 32 trials, Fig 6) each term was needed. Without the state-information term the agent never samples the cue and stays on the safe option. Without the learning term it cannot adapt to new reward statistics [a12, a13, d15]. The model reproduced a primate result (Blanchard et al. 2015): the value of information rises with expected reward, but only with policy precision that varies with reward size [a14, b12].
- Da Costa et al. (2020) "Active inference on discrete state-spaces: a synthesis" is the tutorial. A, B, C, D matrices: likelihood, transitions, preferences, initial state. Dirichlet counts on A add a **novelty** term (reward for visiting poorly known state-outcome pairs) [a01, a03].

### 2.3 Planning depth
- Standard EFE planning is Bellman-optimal only at planning horizon 1 in a POMDP. Sophisticated inference (recursive: beliefs about future beliefs) is optimal at any finite horizon, if inference is exact [a15, b05, b24].
- Friston et al. (2021) "Sophisticated inference" writes the EFE of the next action as risk + ambiguity + expected EFE of the future beliefs (Eq 1.11). Tree search follows only branches with enough predictive probability. It can stop at any depth. A depth-2 agent reproduced the shallow T-maze result (look at cue, then pick arm) [a17, a18].
- Cost: the authors say it needs pruning to be tractable [a16].

### 2.4 Critiques of the theory
- Millidge, Tschantz, Buckley (2021) "Whence the expected free energy?": EFE is **not** "variational free energy in the future". The natural future extension (FEF) has the epistemic term with the **opposite sign**, so it discourages exploration. Exploration is put in by the definition of EFE. They propose the Free Energy of the Expected Future (FEEF): a divergence between predicted and desired futures, which contains the same epistemic term and has a clear bound. EFE is a lower bound on expected model evidence only when information gain exceeds posterior error [a09, a10, b01, c03].
- Millidge, Seth, Buckley (2021): information seeking comes from "divergence objectives" (match expected to desired future), not from "evidence objectives" (reward maximising). Example: with a 90% option and a 10% option, utility maximisation picks the 90% one 100% of the time. People pick the 10% one about 10% of the time. The divergence objective gives that matching [a11, b10].
- Net: the epistemic term is a chosen objective, not a theorem (K02). For us this is fine. We choose it because it works in tests, not because theory demands it.

### 2.5 Link to RL
- Sajid et al. (2021) "Active inference: demystified and compared": reward is just an observation with a prior preference. With preferences set to log reward, active inference maximises reward (RL is a special case) [a05, a16]. Compared with Q-learning and Bayesian model-based RL on FrozenLake (section 3).
- Hafner et al. (2022): reward maximisation, information gain, empowerment and skill discovery sit on one spectrum of divergence minimisation. Information gain is one point on it [a26].
- Sajid et al. (2021, Pepper): an agent that learns its own preferences exploits in a stable world and keeps exploring under constant volatility, because preference uncertainty never falls [a25, b23].
- de Vries et al. (2025): EFE planning recast as variational inference with preference and epistemic priors, solved by message passing. The authors say it is conceptual and simulation validation is not done yet [a24, b11, c07].

### 2.6 Scaling to neural nets
- Ueltzhoeffer (2018) is an early deep implementation [a27]. Tschantz et al. (2019, 2020) report that information gain drives wider exploration and sample-efficient control (section 3) [a19, a21]. Fountas et al. (2020) use Monte-Carlo tree search and report parity with PPO2 on Animal-AI [b08].
- Champion et al. (2023) re-implemented deep active inference and found that every agent with the info-gain term failed (section 5) [a22, b07, a23].

### 2.7 From theory to LLMs (2023-2026)
Nobody ported the full EFE machinery to LLMs. What happened instead:
- BED/EIG for question asking: GATE (Li 2023), UoT (Hu 2024), Piriyakulkij (2024), OPEN (Handa 2024), Mazzaccara (2024), STaR-GATE (Andukuri 2024), Kobalczyk (2025), BED-LLM (Choudhury 2026), Grand (2026).
- Direct EFE framing in LLM agents: Prakki (2024, qualitative), Duraisamy (2025, position), Wen (2025, proposal, snippet only), Dutta (2026), PUMA (Luo 2026).
- Stopping: CaRT (Liu 2025) and Dutta's stop rule.
- Benchmark of asking: QuestBench (Li 2025).
See section 6.

### 2.8 Human and animal data
See section 5.4. Short version: information terms fit human choices, but nothing separates EFE from "reward plus plain EIG" or from heuristic-bonus RL (K21).

## 3. Core findings with exact numbers

Status: E = established (3+ sources or replicated), S = single source, C = contested. "Author-run" means the authors of the method ran the test.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| EFE has risk+ambiguity form and extrinsic+epistemic form; flat preferences give Bayesian optimal design | Eq 13: G = KL[Q(s,A\|pi) \|\| P(s,A)] + E[H[P(o\|s,A)]]; Q(pi)=softmax(-gamma*G) | Da Costa 2020 [a01, a02]; Sajid 2021b [b09]; Millidge 2021 [c04] | E |
| EFE is not the future variational free energy; the FEF has the opposite epistemic sign | Epistemic term positive in FEF, negative in EFE; EFE bounds model evidence from below only if info gain > posterior error | Millidge 2021 [a09, a10] | E (theory) |
| Standard EFE planning is Bellman-optimal only at horizon 1; sophisticated inference at any finite horizon | Proofs, no empirical numbers | Da Costa/Paul [a15, b05]; Friston 2021 [a17] | E (theory) |
| Tabular active inference vs RL on FrozenLake, deterministic | AIF 99.88 [99.64, 100]; Bayesian RL 99.76; Q-learning 97.79 (or 80.44 in another setting); 200 trials x 500 episodes | Sajid 2021 [a05, b03] | S, author-run |
| Same, stochastic | AIF 98.90 [98.00, 99.79]; Q-learning 66.08 and 65.13; Bayesian RL 64.39 | Sajid 2021 [a06] | S, author-run |
| Flat preferences: pure curiosity, no purposeful behaviour | Null AIF score 50.03 (det.), 50.22 (stoch.); goal reached 44.0% | Sajid 2021 [a05, b04] | S |
| Negative-only preference (avoid hole) gives circular behaviour | All three agents learn the same loop; no goal seeking | Sajid 2021 [a07] | S |
| Explore turns into exploit without a switch | Dirichlet-learned agent visits all locations, then settles as uncertainty falls; 10 runs | Sajid 2021 [a08] | S |
| Both state and parameter information needed | Ablations: no state term, never samples cue; no learning term, no adaptation; 1000 sims x 32 trials | Schwartenbeck 2019 [a12, a13, d15] | S, simulation |
| Value of information rises with reward size | Monkeys prefer informative option more when both pay 315 vs 75 microlitres (cited) | Blanchard 2015 via [a14] | S |
| Deep AIF with info gain: wider exploration, sample efficiency | MountainCar 100 epochs; pendulum, hopper strong under 100 epochs vs 1500 for DDPG; 5 seeds | Tschantz 2019 [a19] | C (author-run; see Champion) |
| FEEF solves sparse MountainCar in one trial | 25 episodes of at most 200 steps; beats SAC on HalfCheetah after 100 episodes | Tschantz 2020 [a21, b06] | C |
| Animal-AI: MCTS deep AIF comparable to PPO2, beats DQN and A2C | 2M iterations, lower variance | Fountas 2020 [b08] | C |
| Independent reimplementation: info-gain agents fail dSprites | Only reward-maximising agents solved it; 1% info gain after 200K iterations sharply cut reward; EFE agent chose one action ("down"); 5 EFE definitions x 3 action rules | Champion 2023 [a22, b07] | S (independent), against 3 author-run |
| Stationary bandits: approx. AIF loses long run | K=10, N=1000 agents: beats Bayes-UCB and optimistic Thompson only up to about T=10^4, then regret grows faster than log | Markovic 2021 [c05] | S |
| Switching bandits: AIF does substantially better | Regret-rate minimum stable over a range of lambda | Markovic 2021 [c05, c06] | S |
| Learned preferences exploit when stable, explore under volatility | Volatility 0-100% (map switched every 40, 20, 10, 1 steps); 10 seeds | Sajid 2021c [a25, b23] | S |
| UoT: simulated-EIG question choice vs direct prompting | Avg +38.1% success over 5 datasets and 5 LLMs (relative or points not stated); Llama3-70B +46.6%; vs CoT-SC +33.8%, Reflexion +29.9%, ToT +28.3%, adapted ToT +12.4%; DX 97.0% (GPT-4); troubleshooting 43.7 to 67.3 | Hu 2024 [b17, c19, c20] | E (direction) with caveat |
| UoT per-cell spread | Llama3-70B 20Q Common open-set 34.2 to 36.9 (+2.7); Thing 15.5 to 21.0; DX 26.0 to 35.6; MedDG 25.7 to 50.6. Headlines use closed candidate sets | critique.md item 3 | E |
| One-step lookahead captures most of the UoT gain | Simulation limited to 3 steps; info-gain reward beat ToT self-eval reward | Hu 2024 [b18] | S |
| BED-LLM on 20 Questions | +37.4 percentage points average over direct prompting; more than doubled success in over half the setups; never decreased; 100 targets each of Animals, Celebrities, Things; 6 LLMs; open target space | Choudhury 2026 [c13] | S |
| Static vs updating likelihood in BED-LLM | Animals: Qwen 95 vs 89, GPT-4o 93 vs 86, GPT-4o-mini 88 vs 85; Celebrities Qwen 84 vs 70, Llama-3.3-70B 55 vs 44; Things GPT-4o 64 vs 57; reversed: Llama-3.1-8B Animals 63 vs 67, Llama-3.3-70B Animals 79 vs 80; SE 2-5 | Choudhury 2026 [c16] | S |
| Raw in-context belief update is bad | GPT-4o samples hypotheses that conflict with history; overconfident as history grows | Choudhury 2026 [c14] | S |
| Cheap substitutes work | Predictive entropy is the strongest alternative; LLM picks best of sampled candidates (Implicit Maximization) beats prompt-only | Choudhury [c15]; Piriyakulkij [b26, c25] | E |
| Preference elicitation (web shopping) | Sample 8 candidate questions, pick by expected entropy reduction; 3-question score above baselines' 4-question score; 150 settings | Piriyakulkij 2024 [b14, c25, d08] | S |
| Preference elicitation (movies) | 200 profiles, 5 turns, 10 recs rated 1-5; BED-LLM beat prompt-only and entropy, but prompt-only was a strong baseline | Choudhury 2026 [c17] | S |
| GATE | LM elicitation beat supervised, pool-based active learning and no interaction; significant in 2 of 3 domains | Li 2023 [b16] | S |
| OPEN (human study) | Beat LM-only open and pairwise questioning; exact figures not captured | Handa 2024 [b15, c18] | S |
| Mazzaccara DPO on EIG pairs (LLaMA-2-Chat 7B) | INLG: zero-shot 56.7% S@1, 7.1 q, EIG 0.34; fine-tune 46.6%, 4.6, 0.41; DPO 68.9%, 5.2, 0.45. Things 51.1 to 61.1. Celebrities 71.1 to 72.2 (+1.1, about 2.5 fewer questions) | Mazzaccara 2024 [c10, c11] | S |
| Gains shrink with open or larger sets | INLG16 44.4 to 51.1; BigBench 17.2 to 31.0 but EIG 0.31 to 0.28; concrete 25.0 to 37.5; abstract 7.7 to 23.1, EIG 0.29 to 0.24, questions 9.3 to 10.3 | Mazzaccara [c12]; Hu [c20] | E |
| Code clarification (HumanEval, GPT-3.5, t=10, accuracy %) | EIG-uniform 6.2; EIG-logprobs 4.1; implicit-ToT 5.1; implicit 4.9. GPT-4o-mini: 6.8 vs 6.0, 6.6, 5.5. HumanEval 48 tasks, APPS 47, 3 runs x 3 seeds | Kobalczyk 2025 [b19] | S |
| Battleship: Bayesian strategies | Llama-4-Scout F1 0.367 to 0.764; GPT-4o 0.450 to 0.782; GPT-5 baseline 0.716; win rate vs humans 8% to 82-83%; vs GPT-5 0.67 at about 1% of GPT-5 cost; 42 humans, 126 games | Grand 2026 [b20, c22] | S |
| Battleship: question quality | EIG up to +0.227 bits (94.2% of 0.531 ceiling); zero-EIG questions 18.5% to 0.2% (Scout), 14.6% to 1.2% (GPT-4o); human mean EIG 0.351 | Grand 2026 [c23] | S |
| Battleship: EIG alone barely helps play | QBayes alone +0.021 to +0.026 F1; weak models ask all 15 questions early; humans and GPT-5 ask 8.0-8.2 vs 14.1-14.9 | Grand 2026 [b21] | S |
| Asking correlates with human skill | rho = 0.684; human answer accuracy 92.5%; LM answer accuracy 52.5% (GPT-4o-mini) to 92.8%; code generation +14.7 points | Grand 2026 [c21, c24] | S |
| Hypothesis-level EIG (rules, models, not only states) | Discovery time 28.5 to 19.4 trials; score 89.2 to 150 over 64 games; state-only gain caused one premature commitment (150 to 51); two games undiscoverable without model-level gain | Friston-group 2026 [d17, d15] | E (2 sources, simulation) |
| Planning gap on enumerated tables | Seven frontier LLMs reduce uncertainty every turn but need more questions than the DP optimum; N=25 to 300; 30 targets per tier. Values in figures only | Dutta 2026 [d01, d04] | S |
| Goal-linked information weights and stop threshold | Compliance 0.0417 (about 112 tokens) to 0.375 (about 219 tokens); 48 synthetic tasks; attribute weights hand set (format 1.0, length 0.6, tone 0.25); threshold 0.01, Kmax=2 | Dutta 2026 [d02] | S |
| First measured EFE action selection in an LLM agent | PUMA, Qwen3-8B: Lift 1.62, Prep 75.9%, TrigCov 62.4%, 12.2 turns vs best baseline DIIR 1.07, 52.0%, 34.0%, 13.1 turns. Llama-3.1-8B: 1.76, 83.0%, 63.2%, 10.7 turns vs 1.17, 59.0%, 40.0%, 11.9 | Luo 2026 [d05] | S, confounded |
| PUMA ablations | Lift drops of 0.17 to 0.28 from 1.62; removing world model and EFE planning together: Lift 1.35, Prep 55.2%, TrigCov 54.0%; weights lambda_e 0.4, lambda_p 0.6 fixed, no sweep | Luo 2026 [d06] | S |
| QuestBench: LLMs pick clarifying questions | Over 80% on math (GSM-Q, GSME-Q) vs under 50% on Logic-Q and Planning-Q; CoT and few-shot no consistent help; BFS reaches 39.0% (depth 3), 80.6% (depth 5), 99.8% (depth 10) on Logic-Q; solving the full problem did not predict choosing the question | Li 2025 [d07] | S |
| STaR-GATE | Gold-response log-prob as information signal; win rate 72% vs initial model after 2 iterations (GPT-4 judge); 25,500 prompts; unregularised training degraded results | Andukuri 2024 [d09] | S |
| More chain-of-thought hurts under high meta-uncertainty | Drop 17.3 points, 95% CI [7.7, 25.5]; 7,875 responses; 45-item registered subset of FEH-79; 7 models; control items no cost | Bogdan 2026 [c26] | S, preprint |
| Humans: AIF fits some two-step datasets better than hybrid RL | Magic Carpet n=24 and Spaceship n=21 favour AIF; others about equal; about half of participants show an info-gain weight; AIC and BIC disagree on some variants | Gijsen 2022 [d11] | C |
| Humans: AIF beats RL in an EEG bandit | N=25; EFE linked to frontal pole and middle frontal gyrus | Zhang 2025 [d12] | S |
| Humans: heuristic-bonus RL fits as well | Data 1: 39 men, 300 trials; Data 2: N=100 subsample; perseveration alone as good as the larger model | Mathar 2025 [d16] | C |
| Humans: probability gain beat Shannon gain | 3 experiments (abstract only) | Nelson 2010 [d13] | S |
| fMRI: separate regions encode reward and information value | N=21 recruited, 20 analysed | Cogliati Dezza 2022 [d14] | S |

## 4. Mechanisms and models

Each mechanism is written so an engineer can code it. Notation: H = set of hypotheses h with prior p(h). T = set of candidate tests t. An outcome is o.

### 4.1 Expected free energy of a policy (the reference form)
Discrete model [a01, a03]:
- A: P(o|s), likelihood. B: P(s'|s,u), transitions. C: log preferred outcomes. D: prior over initial state.
- For policy pi: G(pi) = sum over future steps tau of [risk + ambiguity].
  - risk = KL[ Q(o|pi) || P(o|C) ]
  - ambiguity = E_Q(s|pi)[ H[P(o|s)] ]
- Equivalent: G = -(expected information gain about s) - E[log P(o|C)].
- Q(pi) = softmax(-gamma * G). Gamma is policy precision. Action = sample or argmax of Q(pi).
- Learning: Dirichlet counts a on A. Novelty = expected KL between updated and prior Dirichlet. This adds a drive to visit poorly known state-outcome pairs [a03].

### 4.2 The part we can use: EIG over a hypothesis set
For a test t with outcomes o:
```
EIG(t) = H[p(h)] - sum_o p(o|t) * H[p(h|o,t)]
       = sum_o sum_h p(h) p(o|h,t) log( p(o|h,t) / p(o|t) )
p(o|t) = sum_h p(h) p(o|h,t)
```
Pick argmax EIG(t). With deterministic outcomes, EIG(t) is the entropy of the partition that t induces on H. That is "group candidates by behaviour on a fresh input" in S7: the entropy of the group sizes. A test that splits two equal groups gives 1 bit. A test on which all hypotheses agree gives 0 bits (a redundant question) [c23].

### 4.3 Adding the pragmatic term
Score(t) = w_e * EIG(t) + w_p * E_o[utility(o)] - lambda * cost(t).
- Utility is what the final checker rewards. Dutta ties the epistemic weight to attributes the verifier checks. Information about an unchecked attribute (tone) bought nothing [d02].
- Weights are set by hand in every LLM paper found (PUMA 0.4 / 0.6, Dutta 1.0 / 0.6 / 0.25). No sweep exists [d06, d02].
- Two failure modes bracket the weight. Pure epistemic: the agent wanders (null model, goal 44.0%) [b04]. Heavy epistemic in a deep net: even 1% info gain collapsed reward and produced a single-action policy [b07].
- Decay schedule: Dutta's prompt optimizer uses a linearly decaying epistemic weight [d03]. Sajid's learned agent shows explore-then-exploit emerging as uncertainty falls, without a switch [a08].

### 4.4 Estimating likelihoods with an LLM
The hard part. Options measured so far:
1. **Hand-built hypothesis list, LLM simulates answers (UoT).** The LLM lists answer branches and a split is computed; reward is information gain, propagated over up to 3 steps [b17, b18]. Assumes answers split the set cleanly (b25: "no fever" does not remove COVID).
2. **LLM defines a small probabilistic model (Piriyakulkij).** The LLM supplies the conditionals; sample 8 candidate questions; choose the one with the lowest expected posterior entropy [b14, d08]. Expected entropy reduction and expected model change are equivalent here because the expected cross-entropy term is the same across questions [b26].
3. **BED-LLM.** Sample hypotheses from the LLM, filter them for compatibility with the history, keep them diverse, estimate EIG from the LLM's predictive distribution. Use a static likelihood, not one re-conditioned on history [c13, c14, c16].
4. **Logprob EIG vs uniform EIG (Kobalczyk).** Logprob-based estimates were the worst variant in the code cell [b19].
5. **Entropy or LLM-judge picks among sampled candidates.** Cheap, and recovers much of the gain [c15].
6. **Code answers (Battleship).** Answering by generating a program closes much of the answer-quality gap (+14.7 points) and gives exact likelihoods [c24].
7. **Information proxy by gold-answer logprob (STaR-GATE).** Used as a training reward; can degrade results if not regularised [d09].

### 4.5 Using the answer (belief update and conditioning)
After the test result, update p(h) by Bayes (or filter out incompatible hypotheses, which is the deterministic case). Then **use the result in the next decision**. Grand found that EIG-optimal question choice alone moved F1 by only 0.021 to 0.026. The gain came when the answer's implications were marginalised into move choice [b21].

### 4.6 Sophisticated inference and lookahead
Recursive form [a17]:
```
G(a_t | belief b) = risk + ambiguity + E_o[ min_a' G(a' | b' = update(b, a_t, o)) ]
```
Prune branches whose predictive probability is below a threshold. Stop at any depth. Dutta states that greedy one-step EIG is not globally optimal and exact DP is feasible only for small tiers [d04]. UoT reports one step captures most of the benefit [b18]. No LLM test of 2-3 step lookahead against one-step at equal cost exists.

### 4.7 Stopping
Rule from Dutta Prop 3.3: collect more evidence only while I(x; o | a) > lambda * cost. In prompt autocompletion a threshold of 0.01 with at most 2 questions was best on 24 held-out tasks [d02, d04]. CaRT trains a terminator from counterfactual trajectory pairs, because base LLMs overshoot or undershoot [d10]. Bogdan derives that under uncertain precision EFE stops after k high-validity cues (take-the-best) [c26].

### 4.8 Information measure choice
Shannon entropy reduction, expected model change and KL are equivalent in the Piriyakulkij setup [b26]. Probability gain (expected reduction in error probability) differs and fit human search better in Nelson 2010 [d13]. For a deterministic partition they will often rank tests the same; they diverge on skewed splits. It is cheap to compute both and log disagreements.

## 5. What holds up

### 5.1 Replications and failed replications
- **Deep active inference does not replicate cleanly.** Tschantz 2019/2020 and Fountas 2020 are positive and author-run. Champion 2023, an independent reimplementation, found that every agent with the info-gain term failed dSprites, noted discrepancies between the Fountas paper and its code, and that only an MCTS version (DAIMC) solved it [a22, a23, b07]. Unresolved; replication favours caution (K07 vs K08).
- **Tabular active inference beating RL (Sajid 2021)** is one author group, one task family, a small grid (K04). In another regime (stationary bandits at long horizon) approximate AIF loses to UCB and Thompson (Markovic) [c05]. The sign depends on regime.
- **EIG question choice in LLMs** has been shown by 4+ independent groups (K11, K28) in 20 Questions, diagnosis, troubleshooting, preference elicitation and Battleship. This is the one part that holds up.
- **Bogdan's chain-of-thought result** has no replication [c26].
- **Human fits**: no direct replication. Gijsen's re-analysis of four public datasets found support in two of four [d11].

### 5.2 Boundary conditions and moderators
1. **Closed vs open hypothesis sets.** UoT headlines use closed candidate sets; open-set scores are much lower. Mazzaccara BigBench EIG fell 0.31 to 0.28 even as success rose; Celebrities +1.1 points. BED-LLM works in an open target space but needs hypothesis sampling and filtering [c12, c13, c20, K12].
2. **Model strength.** Kobalczyk: the gap shrinks for more capable models [b19]. Prompt-only was strong in movie elicitation [c17].
3. **Estimator.** Logprob EIG was worst in one cell; static beat updating likelihood in most cells [b19, c16].
4. **Answer quality.** In Battleship, weak models answer badly (52.5% accuracy for GPT-4o-mini); EIG over wrong answers is wasted [c21].
5. **Conditioning on the result.** EIG question choice alone: +0.021 to +0.026 F1 [b21].
6. **Task type.** QuestBench: math over 80%, logic and planning under 50%; solving the problem does not predict picking the question [d07].
7. **Regime.** Stationary vs switching bandits [c05]; stable vs volatile worlds [a25].
8. **Weight of the epistemic term.** 1% info gain collapsed a deep agent [b07]. Zero preference gave no purposeful behaviour [b04].
9. **Statistical caution.** UoT does not say whether 38.1% is relative or points. Per-cell gains vary from +2.7 to +24.9 points (critique item 3).

### 5.3 Interventions that worked and did not
Worked:
- EIG-ranked question over LLM-simulated hypotheses (UoT, BED-LLM, Piriyakulkij).
- Filtering sampled hypotheses for compatibility with history; static likelihood [c14, c16].
- Preference optimisation (DPO) on high-EIG vs low-EIG question pairs: +12.2 points INLG, +10 Things [c10, c11].
- Bayesian strategies plus code-based answering in Battleship [c22, c24].
- Hypothesis-level (not state-only) gain in a rule-discovery task [d17].
- Goal-linked weights and a stop threshold [d02].

Did not work or limited:
- Plain fine-tuning on high-EIG dialogues: success 56.7 to 46.6 on INLG [c10].
- Logprob-based EIG in code clarification [b19].
- Updating the likelihood with the full history [c16].
- CoT and few-shot for choosing the clarifying question [d07].
- CoT and PP prompting in 20 Questions did worse than GPT-4 alone [c20].
- Training on a log-prob information reward without regularisation [d09].
- High-EIG question choice alone in Battleship [b21].
- Information about an unchecked attribute [d02].
- More chain-of-thought under high meta-uncertainty (-17.3 points) [c26].

### 5.4 Human and animal evidence
- Information terms fit: Gijsen (two of four datasets, about half of participants with an info-gain weight), Zhang (N=25, EEG, frontal pole), Cogliati Dezza (N=20, separate prefrontal regions for reward and information) [d11, d12, d14].
- But: a hybrid RL model with perseveration and a heuristic directed-exploration bonus fits as well (Mathar 2025, d16); the fMRI result fits any two-term model; Nelson 2010 found probability gain beat Shannon gain [d13].
- No study pits EFE against "reward plus plain EIG" directly (K21, b27). Absence here partly reflects our search limits.

### 5.5 Search limits
In the gap-search phase the arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429 all session [d19]. Equal-token, estimator, lookahead and Bogdan-replication questions could not be searched properly. "Not found" is not "does not exist".

## 6. Language models

### 6.1 How LLMs behave on information-seeking tasks
- **They ask poorly by default.** Open LLMs ask low-information questions in 20 Questions [c10]. Out-of-the-box instruction-tuned LLMs ask uninformative preference questions [c25]. In Battleship many LMs ask redundant questions: 18.5% (Scout) and 14.6% (GPT-4o) had EIG = 0 [c23]. On enumerated tables, seven frontier LLMs reduce uncertainty each turn but need more questions than the DP optimum [d01].
- **They front-load.** Weak models in Battleship ask all 15 questions early; humans and GPT-5 ask 8.0-8.2 [b21].
- **They are good at some pieces.** Math clarifying questions over 80% correct; logic and planning under 50% [d07]. BFS gets 99.8% on depth-10 logic, so explicit search wins where structure is explicit.
- **Their belief updating is unreliable in context.** GPT-4o samples hypotheses incompatible with the history and gets overconfident as history grows [c14].
- **They stop badly.** Overshoot or undershoot in deciding to stop asking or thinking [d10].
- **Answer quality varies.** LM answerer accuracy 52.5% to 92.8% vs humans 92.5% in Battleship; o3, o4-mini, GPT-5 meet or exceed humans [c21].

### 6.2 What changed behaviour, and by how much
| Intervention | Gain | Where |
|---|---|---|
| Simulated-EIG question choice (UoT) | +38.1% avg (basis unclear); +2.7 to +24.9 points per cell | 20Q, DX, MedDG, troubleshooting [b17, critique] |
| BED-LLM (sample, filter, EIG) | +37.4 points avg | 20Q open target [c13] |
| Static likelihood over updating | +3 to +14 points in most cells | 20Q [c16] |
| DPO on high-EIG pairs | +12.2, +10, +1.1 points | 20Q variants [c10, c11] |
| Bayesian strategies (Battleship) | F1 0.367 to 0.764 (Scout), 0.450 to 0.782 (GPT-4o) | Battleship [c22] |
| Code-based answering | +14.7 points answer accuracy | Battleship [c24] |
| EIG-uniform vs implicit (code) | 6.2 vs 4.9 accuracy % (GPT-3.5, t=10), small and low absolute | HumanEval [b19] |
| Goal-weighted info + stop | compliance 0.0417 to 0.375; tokens 112 to 219 | prompt autocompletion [d02] |
| EFE selection + world model (PUMA) | Lift 1.62 vs 1.07 | counselling sim [d05] |
| Scaffold-only EIG on LLM candidate list | beats vanilla and ReAct with fewer questions | shopping [d08] |

### 6.3 Caveats on all of it
- Nearly all gains use a hand-built or LLM-generated hypothesis set with an LLM-simulated likelihood (critique, weak spots).
- Baselines are weak (direct prompting). Very few use an equal-token best-of-N control. Token cost of EIG estimation is rarely reported. This is exactly what our G7 forbids.
- Many are 2025-2026 preprints, several single-group.
- PUMA bundles a world model and a belief module with EFE, so EFE is not isolated [d05, d06]. Dutta's EFE prompt-optimization result is qualitative [d03]. Prakki, Duraisamy and Wen are qualitative, position or proposal papers [c08, c09, b13, c27].
- STaR-GATE, DPO on EIG pairs and CaRT show these behaviours can also be trained, which is outside our no-training rule.

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **S7: when two or more candidate rules or answers still fit, choose the discriminating test by how evenly it splits the surviving candidates (EIG over the candidate set), computed in code from actual outputs. Never run a test that splits nothing.** [E] K01, K11, K28; a01, a02, b09, b17, c13, c23, d08. Honest note: the schema already runs "the one input where they differ". The add is to rank several such inputs by split entropy and skip zero-split ones. Literature gains are against weak prompting baselines, not equal-token controls, so keep this under G7 until test T1 passes.
2. **S7/S4: rank tests at the rule/model level, not only over states or answers.** [E] K26; d17, d15. Two simulated games were undiscoverable without model-level gain.
3. **S7 boundary note: expect smaller gains when hypotheses are open-ended rather than enumerated; report both separately.** [E] K12; c12, c20, c11, d08.
4. **Cheap substitutes before full EIG:** predictive entropy, or an LLM pick among sampled candidate tests, recovers much of the gain. [E] K16; c15, b26, c25. The picker must not be the final selector of ideas (G8) and sees no authorship (G5).
5. **Do not cite active inference / EFE as support for the schema.** Support exists only for the EIG half. [E] K19, K02.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| On logic/planning-like problems, derive the discriminating test by explicit search over candidates in code, not free LLM choice | S7, G5 | [S] K24 | d07 (BFS 99.8% vs LLM under 50%) |
| Filter sampled hypotheses for compatibility with all evidence so far, before scoring tests | G5 / S7 / S8 | [S] K15 | c14, c16 |
| Static likelihood rather than re-conditioning on the whole history | S7 | [S] K15 | c16 |
| Condition the next step on the test result (marginalise), not only choose the test well | S8 | [S] K13 | b21 |
| Stop rule: run another test only if expected information per token exceeds a threshold | S7 / S6 | [S] K27 | d04, d02, d10 |
| Weight candidate tests by relevance to what the final checker checks | S7 | [S] K23 | d02, d06 |
| Pragmatic term: pure EIG vs EIG + utility; sweep the weight | S7 | [S/C] K05, K07 | b04, b07 |
| Likelihood estimator: sampling vs logprob vs LLM-judge | S7 | [S] K17 | b19, c15 |
| One-step EIG vs 2-3 step lookahead | S7 | [E in theory, untested in LLMs] K03 | a15, b18, d04 |
| Probability gain vs Shannon EIG ranking | S7 | [S] K25 | d13 |
| Take-the-best stop for CoT under high meta-uncertainty | G11 | [S] K20 | c26 |
| Explore early, exploit later (decaying epistemic weight) | S6 / memory | [S] K09, K10 | a08, c05, d03 |

Not to take: deep-network active inference [C] K07/K08, FrozenLake superiority over RL [S] K04, human-data claims [C] K21, learned-preference dynamics [S] K10.

## 8. Concrete tests on our bench

All arms get the same total token budget, including setup and EIG estimation (G7). Report accuracy per token as well as accuracy.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 EIG-ranked vs LLM-chosen test | Items where two or more rules fit (ARC-like rule induction) and 3 to 8 candidate discriminating inputs can be generated | A: LLM picks the most discriminating input from the candidates. B: code ranks candidates by split entropy of surviving rules. C: random candidate. D: best-of-N with the freed tokens | Items solved per 1k tokens; tests needed to isolate the right rule | B over A by 3 to 8 points on open sets (smaller than the 20Q gains, because A is already a choice, not direct prompting); B clearly above C |
| T2 Hypothesis filter | Same items | With vs without code compatibility filter on sampled rules before scoring | Share of scored hypotheses that contradict evidence; accuracy | Fewer contradicting rules; +2 to +10 points (BED-LLM-sized) |
| T3 Enumerated vs open | Same items split by whether candidate rules are enumerable | T1 arms | Gain by stratum | Gain larger on enumerated sets (K12) |
| T4 Result conditioning | Multi-step test items | A: choose test by EIG, then continue unchanged. B: EIG, then condition the next generation on the result | Accuracy | B > A (Grand: only +0.02 F1 from question choice alone) |
| T5 Stop rule | Items where tests cost tokens | Fixed budget of 1, 2, 4 tests vs threshold on expected info per token | Accuracy at equal mean tokens | Threshold matches best fixed budget with fewer tokens |
| T6 Pragmatic weight | Items with a checker | w_p in {0, 0.25, 0.5, 1} with EIG | Solve rate; tests spent on irrelevant attributes | Inverted U; w_p = 0 wanders |
| T7 Estimator | Items with LLM-estimated outcome probabilities | Sampling (k=5), logprob, LLM-judge, answer entropy | Rank agreement with an oracle EIG on a table with known answers; accuracy | Sampling or judge at least equals logprob (Kobalczyk) |
| T8 Math/code clarify | Underspecified math/code items with one missing variable | LLM free choice, code BFS over constraints, EIG over candidate solutions | Share of correct clarifying question | Code search above LLM on logic/planning; no gap on math |
| T9 Lookahead | Items where tests interact | 1-step vs 2-step (pruned) at equal tokens | Accuracy | Little to no gain (UoT: 1 step captures most) |
| T10 Gain vs error measure | Same candidate sets | Shannon EIG vs probability gain ranking | Ranking disagreement rate; accuracy | Small differences; gain only where splits are skewed |

## 9. What does not transfer, and why

- **Deep-network active inference.** Scaling failures (Champion) and author-run positives do not apply to a prompt scaffold. We have no policy network.
- **FrozenLake results.** Tabular, grid world, author-run, hand-built generative model. No LLM analogue.
- **Preference vectors C.** In the theory the designer supplies them. In our agent the checker already defines success.
- **Precision and softmax policy sampling.** G4 and G5 say agreement is a hint and code selects. Sampling policies by softmax(-gamma*G) adds randomness the schema does not want. Use argmax with tie-break rules in code.
- **Dirichlet novelty term.** Needs a learned likelihood over many trials. Our items are single problems; cross-problem learning belongs to memory (lessons and class record).
- **Clean likelihood p(o|h,t).** Theory assumes a known A matrix. An LLM's answer distributions are noisy and overconfident [c14]. The size of the gain loss is not measured.
- **Human behavioural claims.** No human data separate EFE from simpler models (K21). Do not justify design by "brains do this".
- **Trained components.** STaR-GATE, DPO on EIG pairs, CaRT work, but we scaffold without training.
- **Preference elicitation from users.** Our benchmark items have no user in the loop; the movie and shopping gains transfer only as evidence that estimator choices matter.
- **FEEF vs EFE theory.** Interesting, but it does not change what we compute.

## 10. Open questions

1. At equal tokens, does EIG-ranked test selection beat an LLM choosing the most discriminating test from the same candidates, on open-ended hypothesis sets? (Partial: Piriyakulkij has no equal-token control.)
2. How much of the EIG gain is lost with noisy LLM likelihoods, and which estimator is best and cheapest?
3. Is there a sweet spot for the pragmatic weight?
4. Does conditioning the next move on the test result matter more than test choice outside games?
5. Is one-step EIG enough, or does 2-3 step lookahead pay at equal cost?
6. Does hypothesis filtering with a static likelihood transfer to math and code where hypotheses are candidate solutions?
7. Is there human or animal data that separates EFE from plain EIG plus reward?
8. Does Bogdan's CoT result replicate, and does it imply a stop rule for S7?
9. Are there measured active-inference LLM agents beyond PUMA and Dutta that isolate EFE?
10. Does Friston 2015 contain numbers that bear on the cue-sampling decision? (not opened)
11. Is the UoT headline relative or in points?

## 11. Sources

[V] = opened and read (as recorded in the evidence files). [M] = snippet or summary only.

- [V] Da Costa, Parr, Sajid, Veselic, Neacsu, Friston (2020) Active inference on discrete state-spaces: a synthesis. https://arxiv.org/abs/2001.07203
- [M] Friston, Rigoli, Ognibene, Mathys, FitzGerald, Pezzulo (2015) Active inference and epistemic value. https://doi.org/10.1080/17588928.2015.1020053
- [V] Sajid, Ball, Parr, Friston (2021) Active inference: demystified and compared. https://arxiv.org/abs/1909.10863
- [V] Millidge, Tschantz, Buckley (2021) Whence the expected free energy? https://arxiv.org/abs/2004.08128
- [V] Millidge, Seth, Buckley (2021) Understanding the origin of information-seeking exploration in probabilistic objectives. https://arxiv.org/abs/2103.06859
- [V] Schwartenbeck et al. (2019) Computational mechanisms of curiosity and goal-directed exploration. https://elifesciences.org/articles/41703
- [V] Da Costa, Sajid, Parr, Friston, Smith (2023) / Paul et al. (2024) Reward maximisation through discrete active inference. https://arxiv.org/abs/2009.08111
- [V] Friston, Da Costa, Hafner, Hesp, Parr (2021) Sophisticated inference. https://arxiv.org/abs/2006.04120
- [V] Tschantz, Baltieri, Seth, Buckley (2019) Scaling active inference. https://arxiv.org/abs/1911.10601
- [V] Tschantz, Millidge, Seth, Buckley (2020) Reinforcement learning through active inference. https://arxiv.org/abs/2002.12636
- [V] Champion, Bowman, Markovic, Grzes (2023) Deconstructing deep active inference. https://arxiv.org/abs/2303.01618
- [V] Fountas et al. (2020) Deep active inference agents using Monte-Carlo methods. https://arxiv.org/abs/2006.04176
- [V] de Vries, Nuijten et al. (2025) Expected free energy-based planning as variational inference. https://arxiv.org/abs/2504.14898
- [V] Sajid, Tigas, Zakharov, Fountas, Friston (2021) Exploration and preference satisfaction trade-off in reward-free learning. https://arxiv.org/abs/2106.04316
- [V] Hafner, Ortega, Ba, Parr, Friston, Heess (2022) Action and perception as divergence minimization. https://arxiv.org/abs/2009.01791
- [V] Ueltzhoeffer (2018) Deep active inference. https://arxiv.org/abs/1709.02341
- [M] Friston, Parr, de Vries (2017) The graphical brain: belief propagation and active inference. https://doi.org/10.1162/NETN_a_00018
- [V] Sajid, Da Costa, Parr, Friston (2021) Active inference, Bayesian optimal design, and expected utility. https://arxiv.org/abs/2110.04074
- [V] Markovic, Stojic, Schwobel, Kiebel (2021) An empirical evaluation of active inference in multi-armed bandits. https://arxiv.org/abs/2101.08699
- [V] Duraisamy (2025) Active inference AI systems for scientific discovery. https://arxiv.org/abs/2506.21329
- [V] Prakki (2024) Active inference for self-organizing multi-LLM systems. https://arxiv.org/abs/2412.10425
- [M] Wen (2025) A framework for inherently safer AGI through language-mediated active inference. https://arxiv.org/abs/2508.05766
- [V] Piriyakulkij, Kuleshov, Ellis (2024) Active preference inference using language models and probabilistic reasoning. https://arxiv.org/abs/2312.12009
- [V] Handa, Gal et al. (2024) Bayesian preference elicitation with language models (OPEN). https://arxiv.org/abs/2403.05534
- [V] Li, Tamkin, Goodman, Andreas (2023) Eliciting human preferences with language models (GATE). https://arxiv.org/abs/2310.11589
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271
- [V] Kobalczyk, Astorga, Liu, van der Schaar (2025) Active task disambiguation with LLMs. https://arxiv.org/abs/2502.04485
- [V] Grand, Pepe, Tenenbaum, Andreas (2026) Shoot first, ask questions later? Building rational agents that explore. https://arxiv.org/abs/2510.20886
- [V] Mazzaccara, Testoni, Bernardi (2024) Learning to ask informative questions: preference optimization and expected information gain. https://arxiv.org/abs/2406.17453
- [V] Choudhury et al. (2026) BED-LLM: intelligent information gathering with LLMs and Bayesian experimental design. https://arxiv.org/abs/2508.21184
- [V] Bogdan (2026) Free energy heuristics: fast-and-frugal cognition as active inference under uncertain precision. https://arxiv.org/abs/2606.15877
- [V] Dutta, Ramachandran, Sra (2026) Active inference as context acquisition for AI agents. https://arxiv.org/abs/2608.19202
- [V] Luo et al. (2026) PUMA: know you before you speak. https://arxiv.org/abs/2605.24647
- [V] Li, Kim, Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674
- [V] Andukuri, Franken, Gerstenberg, Goodman (2024) STaR-GATE. https://arxiv.org/abs/2403.19154
- [V] Liu, Qu, Schneider, Singh, Kumar (2025) CaRT: teaching LLM agents to know when they know enough. https://arxiv.org/abs/2510.08517
- [V] Gijsen, Grundei, Blankenburg (2022) Active inference and the two-step task. https://pmc.ncbi.nlm.nih.gov/articles/PMC9586964/
- [V] Zhang et al. (2025) Neural correlates of novelty and variability in human decision-making under active inference. https://pmc.ncbi.nlm.nih.gov/articles/PMC11928029/
- [V, abstract only] Nelson, McKenzie, Cottrell, Sejnowski (2010) Experience matters: information acquisition optimizes probability gain. https://pubmed.ncbi.nlm.nih.gov/20525915/
- [V] Cogliati Dezza, Cleeremans, Alexander (2022) Independent and interacting value systems for reward and information in the human brain. https://pmc.ncbi.nlm.nih.gov/articles/PMC9064296/
- [V] Mathar, Peters et al. (2025) Signatures of perseveration and heuristic-based directed exploration in two-step sequential decision task behaviour. https://pmc.ncbi.nlm.nih.gov/articles/PMC11827566/
- [V] Active inference and artificial reasoning (2026), Sci Rep. https://pmc.ncbi.nlm.nih.gov/articles/PMC13601584/
- [M] Search status (arXiv, Semantic Scholar, OpenAlex returned HTTP 429). https://export.arxiv.org/api/query
