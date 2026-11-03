# ACT-R: production selection: deep document

*Folder: C02_cognitive_architectures/subfields/05_act_r_production_selection. Built from evidence_a-d.jsonl (a01-a28, b01-b26, c01-c25, d01-d17), claims.jsonl (K01-K26) and critique.md. Ids in brackets are evidence ids or claim ids. Status marks: [E] established, [S] single-source, [C] contested.*

*Links to other subfields in this run (not covered here): Soar: other memories and RL; MDPs and POMDPs; Chain-of-thought prompting; Monte Carlo tree search; Active inference versus reinforcement learning; Metacognition models; Executive function, exploration vs exploitation; Learned termination; Count-based exploration; Pruning of decision trees.*

## 1. What it is

ACT-R is a cognitive architecture. Its procedural part is a set of if-then rules called productions. At each cycle many productions may match the current goal and state. Exactly one fires. The choice is made by a learned number called utility. This is "production selection" or "conflict resolution".

Two versions of the rule exist.

- **Classic (ACT-R 4/5, Anderson and Lebiere 1998):** U = P*G - C. P is the learned chance that the goal is reached if the rule fires. G is the value of the goal (default 20 s in the reference code). C is the learned cost, usually time. [a01, a02, b01, c01]
- **Reward-difference (ACT-R 6):** U(n) = U(n-1) + alpha*(R(n) - U(n-1)). R is the external reward minus the time since the rule fired. This is a Rescorla-Wagner / delta rule. [a06, a14]

Choice among matching rules is noisy. The highest noisy utility fires. In the softmax form P(i) = exp(U_i/t) / sum_j exp(U_j/t), with t about 0.5 by convention. [a02, a14]

Why this matters for our agent: the schema picks reasoning operators (O1-O8: specialise, generalise, decompose, drop a constraint, work backwards, change representation, map an analogue, reframe) at an impasse. "Operator choice by success rate" is exactly the ACT-R rule with operators as productions. The question is whether keeping counts of success and cost per operator, in code, and choosing by noisy utility beats fixed order or random choice at equal tokens. This is untested anywhere (see section 5). What is established is a human base (people do shift strategy by success history) and a strong LLM-side reason to keep the counts in code, not in the model (LLMs explore badly and are over-optimistic about their own success).

## 2. History and theories in depth

**1993-1998: the founding model.** Lovett (1993) built the first ACT-R model of the Building Sticks Task. Among rule instances it picked the highest PG-C. P and C came from built-in functions of the rule's success history and the instance's distance to the goal. File parameters: G = 20, CostScale = 2.5, EffortScale = 2.5 (half the average path length), v = 2 so effort so far affects the success estimate more; parameter learning on, strength learning off. [a11] Anderson and Lebiere (1998) published the theory in The Atomic Components of Thought. A review praised its scope and flagged poor parsimony: many mechanisms and many parameters. [a24]

**The Building Sticks Task (BST).** People build a target stick length by adding or subtracting three given sticks. Two strategies compete: overshoot (take the big stick first, then subtract) and undershoot. Hill climbing (pick the stick closest to the goal) is the default bias. In Lovett's 15-problem set, both strategies work on problems 1 and 15, only overshoot on 2-8 and 12-14, only undershoot on 9-11. Over 80% of people chose overshoot first on problem 5, where hill climbing also favoured it. By problem 7 overshoot was chosen always, and on 9-11 people adapted almost at once. The model used four rules (always overshoot, always undershoot, and two hill-climbing context rules) that started slightly higher, then shifted with experience. [a04, a05, b02, c02] This is a secondary description of Lovett and Anderson (1996), which no one on this team opened. [a26, c03]

**1995 precursor.** Lovett and Anderson (1995, CogSci): N = 68 CMU undergraduates (67 analysed), 90 problems each, four conditions (complementary high 80/20, complementary low 60/40, non-complementary high and low). Most chose the better strategy and often overmatched (chose it more than its success rate). An ACT-R model treating each strategy's success chance as a Bayesian posterior over past successes and failures, plus Gaussian noise (variance 0.052), fit R2 = .99 in aggregate and .66 for individuals. Extreme preferrers were 6 to 18% per condition. [d01]

**1998-2006: breadth.** Utility learning was one of five modelling paradigms. Instance learning (declarative) improves behaviour without an evaluation signal; utility learning is needed when there is an evaluation. In the Sugar Factory control task, people went from 8 to 15 on-target decisions of 40 between blocks 1 and 2; an instance model got 9 and 14. That fit does not separate instances from utility. [a22, b03] Production compilation merges two rules into one faster rule that then competes by utility, so a new rule must earn its place. [a23] Gray et al. (2006) tested the soft-constraints hypothesis: people trade look-again vs remember by time cost, as utility predicts. [b11-b13]

**2004-2011: reinforcement learning bridge.** Fu and Anderson (2004) replaced yes/no feedback with a temporal-difference (TD) rule with hyperbolic discounting. Learning rate a = 0.1 and discount K = 1.0 fixed. Fits: R2 = .98 on Friedman et al. probability learning (over 1,000 trials over 3 days); R2 = .97 on a second reward condition; R2 = .94 on Busemeyer and Myung (9 blocks of 50 trials, G fitted to 1.76). It also fits reward-size effects the old rule cannot. [d03] The 2006 follow-up (recurrent choice to skill learning) and the 2006/2008 credit-assignment paper were never opened. [a27, b14, c05, d04] Walsh and Anderson (2011) found in an ERP study that feedback-related negativity follows both final and intermediate negative feedback, so people value intermediate states by expected future reward. TD with eligibility traces gave lower BIC than actor-critic, Q-learning and SARSA for all but 2 participants. [a20] Their 2012 review does not mention ACT-R; the link is inferred. [a21]

**2013-2014: critique and re-implementation.** Whitehill (2013) read the 1998 conflict-resolution theory critically. A matched production fires only if the expected gain from waiting for a better rule does not exceed a waiting cost. The success term p is split: q (the action works, learned by Beta update) and r (the goal is reached given the action works, set by heuristics tied to effort spent, falling as "hopelessness" grows). He says the exact process is hard to infer from the book, and the production-strength power law link is weak. [a08-a10] Gall and Fruehwirth (2014) re-implemented ACT-R in Constraint Handling Rules and found the two utility rules could not both run in one ACT-R version. Tie-breaking between equal utilities is undocumented and changed between ACT-R 5.0 and 6.0. [a06, a07, a25, b09, b10]

**2020-2026: bridge to ML and LLMs.** Brasoveanu and Dotlacil (2020, 2021) replaced hand-coded rule order with Q-learning and (2021, snippet only) deep Q-networks that beat ACT-R utility learning on complex tasks. [a17, a18, a19, b05-b08, b15] Stocco et al. (2024) gave a likelihood-fitting primer for utility learning. [a13, a14, c07, c08] Sumers et al. (2023, CoALA) mapped LLM agents onto production-system architectures (propose, evaluate, select, execute). [c11, c12, b26] Laird (2021) contrasted ACT-R (one rule by match and utility) with Soar (propose and evaluate operators; a tie gives an impasse and a substate). [a16] Fan and Lan (2026) review maps ACT-R to language agents and lists LLM-agent work that rebuilds utility selection (GraSP, Utility-Guided Agent Orchestration, UALA, KnowNo, Calibrate-Then-Act). [a15]

**Competing accounts.** (1) Declarative / instance accounts explain the Sugar Factory without utility. (2) Rational metareasoning without discrete strategy representations is also compatible with Xie and Moss. [d02] (3) TD models with traces fit neural data better than plain RL. [a20] (4) The utility rule assumes reward seeking and fits non-reward-seekers poorly. [c07, c08]

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Production choice is a noisy softmax over U = P*G - C | t about 0.5 by convention; G = 20 s default | a01, a02, c01 | [E] as theory, no replication of the rule itself |
| P is learned from success and failure counts with a prior | succ = prior*V + m, fail = (1-prior)*V + n; C = sum effort / (succ + fail) | a03 | [E] as formula |
| People shift to the strategy that worked (BST, 1995) | N = 67, 90 problems, 4 conditions; model R2 .99 aggregate, .66 individual; noise var 0.052; extreme preferrers 6-18% | d01 | [E] (human, one lab plus replication of related study) |
| BST 15-problem sequence: people drop overshoot when it fails | >80% overshoot on problem 5; always overshoot by problem 7; adapted almost at once on 9-11 | a04, a05, b02, c02 | [S] secondary report of Lovett and Anderson 1996 |
| Related Lovett and Schunn (1999) result replicated | 144 recruited, 100 analysed, 2x2; posttest biased group chose successful strategy more b = 0.46, p = .009; cue slope in unpredictive-biased group stayed positive b = 0.49, p < .001 | d02 | [E] (replicates the related study, not the 1996 one) |
| People pick the cheaper strategy in proportion to time cost | 3 experiments, 16-18 per cell; linear trend explained 98% (accesses) and 87% (another measure) of condition variance; t = 0.491; 88.5% pick faster at 1 s difference | b11, b13 | [S] |
| Higher cost shifts people to memory | first look 1179 / 1241 / 2334 ms (low/med/high); blocks after first look 1.7 / 1.9 / 2.9; accesses 6.8 / 6.4 / 4.1 | b12, critique | [S] |
| TD-extended rule fits single-step human choice | a = 0.1, K = 1.0; R2 .98, .97, .94; G = 1.76 in one fit | d03 | [S] |
| TD with traces beats plain RL for human sequential feedback | lowest BIC for all but 2 participants; behaviour predicted for 13 | a20 | [S] |
| Likelihood fit of utility learning, one participant | procedural LL -30.11 (alpha .759, noise .440) vs declarative -35.65 vs chance -44.36; BF 254.68; 64 trials | a13, c07 | [S] one participant |
| Fit is poor for people who stay after punishment | joint fit L .028 vs .007 | c08 | [S] |
| Tabular RL of rule order scales badly | 12 steps ok by ~5,000 episodes; 18 steps by ~9,000; 34 steps ~22,000, 6 of 24 states nonsense | b05-b07, a17 | [S] |
| Reward shape controls the learned policy | +1 goal, -0.15 per firing; no time penalty lets agent stall on "do nothing" up to 2 s | b08 | [S] |
| The two ACT-R rules differ | rock-paper-scissors vs always-rock: final U (0, 1.87, -0.02); success/cost with noise off gets stuck | a07, b09, b10 | [S] |
| LLM agent using ACT-R style utility matches action-only LLM | 15/15 vs 14/15 find; 15/15 slice and clear; steps p = .446, .347; gamma = .95 | a12, c09, c10 | [S] 15 trials, simulated kitchen |
| Bayesian success selection beats similarity-only retrieval | ALFWorld seen/unseen 87.2/90.3 vs 79.4/81.2 (-7.8/-9.1); reuse 78% vs 62% | d05 | [S] control is similarity |
| MACLA learning curve | 20% data 45%, 50% data 82%; pruned posterior mean .42 vs retained .79; 100 slots best | d06 | [S] |
| Per-step choice of reasoning depth beats fixed depth (trained) | 92.5% at 1,739 tokens vs fixed L1 76.5% at 357 and fixed L4 86.5% at 4,641; FreeForm 81.5% | d09 | [S] trained router |
| Failure penalties collapse a router | reweighting failures: 83.0%, collapse to L1 83.1%; no balanced cold start 86.0% | d10 | [S] |
| Plain LLMs fail to explore in bandits | GPT-4 basic prompt: >60% suffix failure; 1 of 72 configurations worked (summary, suggestive hint, CoT) | b20, b21, c13, c14 | [E] |
| External summaries help big models, not small | Pro 45.5 raw, 60.0 summarised, 59.6 guided, UCB 90.6; Flash 27.7/34.8/32.2; Gemma-9B 10.5 / 5.3 / 4.1; contextual Flash 0.0 vs 46.4, Pro 7.1 vs 64.3, LinUCB 96.4 | b24, b25 | [S] |
| LLMs learn with an optimism bias | alpha+ 0.87 +/- .01 vs alpha- 0.10 +/- .04, t(49) = 20.1 (Claude v1.3, 50 runs) | c16, c17 | [E] with d11, d12 |
| LLM self-estimates of success are inflated | predicted 77% vs 22% true (Gemini, SWE-bench Pro, N = 100); GPT 73 vs 35; Claude 61 vs 27; 62% of predictions on failures >= 0.7 | d12, d11 | [E] |
| Bandit routing beats random in LLM pipelines | 76.7% vs 49.0% (30 queries per mode, no CI); +7.20% and +7.27% net reward | c18, c19, d07 | [S] weak |
| Forgetting tracks operator drift | factor .997; recovered .8630 [.8572, .8684] vs .8850; new arm adopted in 142 steps; 20 seeds | d13 | [S] arms are models |
| Whole-task skill sharing hurts, subtask helps | whole -1.2 (text) / -4.1 (code) points; subtask +1.9 / +0.5; one run 27.3% to 1.0% | d14 | [S] |
| Training an LLM on ACT-R traces | acc .6576 vs chance .4826 vs Llama .3564; multi-facet .42 | b16-b18, c23 | [C] gains called minuscule |

## 4. Mechanisms and models

**4.1 Classic utility.** For each production i keep: successes s_i, failures f_i, total effort E_i. Start s_i = prior*V, f_i = (1-prior)*V (V is prior strength). P_i = s_i / (s_i + f_i). C_i = E_i / (s_i + f_i). U_i = P_i*G - C_i. Pick among matching rules by softmax(U/t). [a01-a03] Older code started with successes = 1, failures = 0, effort 0.05 s. [a06]

**4.2 Reward-difference.** After a reward R, every rule that fired since the last reward updates: U <- U + alpha*(R - elapsed - U), where elapsed is the time since that rule fired. Rewards are shared by all rules fired since the last reward, so earlier rules get a smaller effective reward. [a06, a14] Note: the LLM-ACTR paper prints a plus sign, U(n-1)+0.2[R(n)+U(n-1)]. Its own traces use the minus sign. The plus is a typo; its -1.02 worked example is unreliable. [critique, b19]

**4.3 Credit assignment.** ACT-R shares the end reward along the chain with time discounting, which is heuristic. TD extension: U_after = U + a*(gamma^t*R - U) with hyperbolic discounting (a = 0.1, K = 1.0). [d03] Zhu and Simmons use U_after = (N*U_before + gamma^t)/(N+1), gamma = 0.95, a count-averaged variant; choice P proportional to exp(U); no update at all when a subtask ends in "quit". [a12, c09, c10]

**4.4 Waiting rule (Whitehill).** Fire a matched rule only if the expected gain from waiting for a better one does not exceed the waiting cost; V = p*G - C, p = q*r. [a08, a09] Not used in practice by most models.

**4.5 Engineer's recipe for the agent (design, not yet tested).**

1. Context = problem class (coarse: a few classes; fine contexts need thousands of episodes [K06]).
2. For each (class, operator) store s, f, token cost. Prior: pseudo-counts, for example 2 successes and 2 failures (strength V untested [K22]).
3. Score = P*G - C, where G is a token-equivalent value of a solved problem and C is mean tokens spent.
4. Choose by softmax with a temperature set by the program, decayed over time [d17]. Keep a minimum probability for every operator [d10].
5. Update from a code-checked outcome only (guardrails G2, G3, G10). Never from the model's self-rating [d11, d12].
6. Use decayed counts (gamma .95 to .997) so a broken operator is dropped [d13, d08].
7. Cap negative updates. Do not update on abandon or quit [c10, d10].
8. Break ties randomly and say so explicitly [a25].

## 5. What holds up

**Holds (human side).**
- People move toward the more successful strategy and often overmatch. One lab, N = 67 (1995) and a replication of a related 1999 study at N = 100 (2025). [d01, d02] The effect is robust but the evidence for the specific utility equation is thin: no direct replication or failed replication of the 1996 paper or the utility equation exists in our evidence. [critique]
- People trade strategies by time cost, with a high noise parameter (0.491). [b11-b13]
- TD with discounting and traces fits human sequential and neural data at least as well as the simple rule and sometimes much better. [d03, a20]

**Moderators and failures.**
- Noise is a free parameter, not a constant: 0.5 by convention, 0.491 (Gray), 0.440 (one-participant fit), 0.75 (joint stay fit), variance 0.052 (Lovett). [K04]
- Individual fit is much weaker than aggregate (R2 .66 vs .99). [d01]
- Non-reward-seekers fit poorly. [c08]
- The utility rule and instance learning can both explain a dataset (Sugar Factory). [a22, b04] In Dienes and Fahey's rival model, 86% of the first ten inputs were explained by three simple rules and a loose target (9000 +/- 1000) was needed. [b04]
- Rational metareasoning is a compatible rival to discrete strategy representations. [d02]
- Two ACT-R formulations differ in tie-breaking and in stuck states with noise off. [a07, a25, b10]
- Tabular learning of long rule chains is slow and leaves nonsense states. [b05-b07]
- Evidence base is thinner than it looks: a01, b01, c01 and a02, b02, c02, a04 are the SAME chapter. The central claim rests on one secondary description of Lovett and Anderson (1996) and the 1995 precursor.

**Interventions that worked (LLM side).**
- Externally computed per-arm summaries and counts. GPT-4 needed summary + hint + CoT; only 1 of 72 configurations worked. [c13, b20]
- Algorithm-guided or summarised history helped Gemini Pro (+14.5 and +14.1 win-rate points) and Flash (+7.1, +4.5), but not Gemma. [b24]
- Decayed temperature schedule beat fixed temperature in LLM-enhanced Thompson sampling (abstract-level). [d17]
- Forgetting on counts recovers from silent quality drops. [d13]
- Informed priors / warm start: removing a 5-query warm start cost 5.5 points (71.2 vs 76.7, 30 queries). [d07]

**Interventions that did not work.**
- Raw history in the prompt. [b24]
- Few-shot demos hurt Pro in some setups (39.1 raw-history few-shot vs 56.4 with algorithm support, so the support did the work). [b25]
- Letting the model rate its own success: no recovery after failure. [d11, d12]
- Whole-task skill sharing (-1.2 / -4.1 points). [d14]
- Reweighting failed trajectories in a trained router (collapse to the cheapest level). [d10]
- Full ACT-R trace embeddings added to an LLM: no significant gain (0.71 for both). [b18]

**Missing.** No ablation of utility choice vs random vs fixed order among reasoning operators at equal tokens, in any LLM agent. Nearest: MACLA (control is similarity), life-sciences bandit (30 queries, no CI), CogRouter (trained). [critique gaps 1-10]

## 6. Language models

**Exploration behaviour (bandits).**
- GPT-4 basic prompt: suffix failure in >60% of replicates (T = 500, N = 20); the best arm is never chosen again. Second failure mode: uniform-like choosing that never narrows. [b21, c14] 72 configurations, 32 prompt designs, about 50K queries; one configuration matched Thompson sampling (summary, suggestive framing, reinforced CoT, T = 200, N = 40). [b20, c13]
- EVOLvE MAB win-rate: raw 7.6 (Gemma-2B), 10.5 (Gemma-9B), 27.7 (Flash), 45.5 (Pro). Summarised 10.5, 5.3, 34.8, 60.0. Algorithm-guided 4.9, 4.1, 32.2, 59.6. UCB 90.6. Contextual bandit: Flash 0.0 raw vs 46.4 guided; Pro 7.1 vs 64.3; LinUCB 96.4. Fine-tuning on UCB trajectories: Flash 65.6 (hard-task data) vs 54.5 (easy). [b24, b25] Do not confuse with arXiv 2412.06438 (a different paper).
- TextBandit best-arm rate: Qwen3-4B 89.2, Qwen3-8B 37.5, Llama-3.1-8B 31.6, Phi-2 25.4, Thompson 51.1, UCB 47.6, epsilon-greedy 38.1, random 31.8 (500 runs of 25 steps). Not explained or replicated. [d15]
- Choice-model fits: plain LLMs show more random and less directed exploration than humans; CoT moves them toward the human mix; in changing tasks they fail at directed exploration, even with thinking. [d16]
- GPT-3 (2022): lower regret than humans in the horizon task (2.72, SD 5.98 vs 3.24, SD 10.26; t(38878) = -5.03) yet no directed exploration; short horizon indistinguishable (t(5566) = -0.043). Descriptions task: above chance (t = -16.85) but below humans (t = -11.50). [b22, c15]
- Claude v1.3: alpha+ .87, alpha- .10; the bias reverses for foregone outcomes and vanishes when another agent chooses. [c16, c17]

**Self-estimates.** Predicted success 77% vs true 22% (Gemini 3 Pro, 100 SWE-bench Pro tasks); GPT-5.2-Codex post-run 73% vs 35% base; Claude Opus 4.5 61% vs 27%; Gemini pre-run mean 99%. Only 11% of passing tasks were rated below 0.3. Asking for bugs cut overconfidence. [d12] In contract sequences (512 sequences of 9 contracts, 50% solvable) all models stayed above 0.5 predicted success; Sonnet 3.5 reached 50% acceptance by contract 5; GPT-4.1 barely changed. [d11] Caveat: N = 100, wide CIs.

**ACT-R-like selection inside LLM agents.**
- Zhu and Simmons: 15/15 vs 14-15/15, no step difference, 15 trials per task, simulated kitchen. The paper argues utility aggregation damps hallucinated rules; no ablation. [a12, c10]
- MACLA: success-posterior selection +7.8 / +9.1 points over similarity-only; LLM calls per episode 6.2 vs 8.4; reuse 78% vs 62%. Component ablations: no contrastive refinement 83.6 / 85.7; no meta-procedures 81.2 / 78.4; no ontology 82.8 / 84.1. [d05, d06]
- CogRouter (ACT-R-inspired four-level depth, trained): see section 3. The 82.3% headline and the 92.5% ALFWorld figure were not reconciled. Confidence signal: average log-prob 92.5, max-prob 89.0, entropy 79.0, min-prob 81.5. [d09, d10]
- Life-sciences Thompson sampling: strategy 23/30 vs 15/30 random, tool 24/30 vs 14/30, domain 22/30 vs 15/30. Learned: direct answer for simple factoid 85%, CoT for complex mechanism 90%. Ablations: no context features 58.3%, epsilon-greedy 68.1%, no warm start 71.2%. [c19, d07]
- Model-routing bandits: +7.20% (medical, 10 runs), +7.27% (TeleQnA, 5 runs; best baseline there was random). [c18]
- SkillCraft: skill reuse cut tokens up to 80%; skill execution vs task success r = .65; errors compound when skills nest. [c21]
- Feng 2026: success rose across 10 utility bins 14.0 to 24.5% (task level) and 22.8 to 31.0% (subtask level), Spearman .98 and .95; utility there is similarity-based, correlational. [c20, d14]
- LLM-ACTR (training): see section 3. [b16-b18]
- Drift: ParetoBandit, 1,824 prompts, 3 models, silent 18% quality drop; share fell 71% to 50% then 54%. [d13]
- Reviews: CoALA says ReAct has no evaluation or selection stage; Tree of Thoughts has propose, evaluate, select. [c11] Fan and Lan list recent utility-style orchestration papers. [a15]

**What changed behaviour and by how much.** Moving counts out of the model into code: +14.5 win-rate points for Pro; contextual bandits +46.4 (Flash) and +57.2 (Pro). Small models did not benefit. Moving selection to a bandit: +27.7 points over random (30 queries, no CI). Success-posterior vs similarity: +7.8 to +9.1.

## 7. What our agent should take

### Add now (established)

1. **Keep operator statistics in code, never in the model's head.** Schema part: O and memory (class record). Status [E]. Evidence: b20, b21, c13, c14, c16, d11, d12 (K10, K13, K23).
2. **Do not let the model rate its own success or the operator's success; use code-checked outcomes only.** Schema part: G (reinforces G2, G10). [E]. Evidence: d11, d12, c16.
3. **Selector lives outside the model, and the program owns the exploration rule** (temperature, minimum probability, uncertainty bonus). Schema part: O. [E] that LLMs explore badly (b20-b22, d15, d16); the specific selector is not yet tested.
4. **Treat noise or temperature as a free parameter and log it.** Schema part: O. [E]. Evidence: a02, a13, b13, c08, d01 (K04).
5. **Break ties randomly and write the tie rule in the spec.** Schema part: O. [E] that implementations differ (a25, b10); trivial cost.

### Test first (not established, see UNKNOWNS.md)

1. **Utility choice (P*G - C, softmax) over operators vs fixed order and random at equal tokens.** O. [S]. Evidence: a01-a03, d05, d07, d09 (K01, K08, K12, K18, K19). No ablation exists.
2. **Per-operator cost term (tokens) in the score.** G/O. [S]. Evidence: b11, b13 (K03), d09.
3. **Decayed counts to follow operator drift.** O. [S]. Evidence: d13, d08 (K21).
4. **Prior strength and warm start.** O/memory. [S]. Evidence: a03, d06, d07 (K22).
5. **Credit assignment for operator chains (end-of-episode share vs discounted TD).** O. [S]/[C]. Evidence: d03, a20, d10 (K05, K25).
6. **Cap on negative updates and a minimum probability per operator.** O/G. [S]. Evidence: d10, c10 (K09, K20).
7. **Coarse contexts (problem class) rather than fine ones.** memory. [S]. Evidence: b05-b07 (K06).
8. **Share operator statistics at subtask grain only.** memory. [S]. Evidence: d14 (K24).
9. **Per-operator summary table in the prompt for strong models only.** O. [S]. Evidence: b24, b25 (K11).
10. **Decaying temperature schedule.** O. [S]. Evidence: d17, d16 (K26).

## 8. Concrete tests on our bench

All arms get the same token budget per item. Report the 95% CI over at least 100 items per cell. Use the bench harness (skill: bench).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Utility vs controls | ARC and BRAINTEASER items with a failed first attempt (impasse) | (a) fixed order O1..O8; (b) random operator; (c) softmax(P*G - C) from running counts per problem class | solve rate on held-out checks; tokens per solve | (c) beats (a) and (b) by 2 to 5 points; if under 1 point, drop |
| T2 Cost term | same | (c) with and without C | solve rate per 1k tokens | cost term lowers tokens at flat accuracy |
| T3 Drift | stream of 100 items where operator X stops working at item 50 | no decay, gamma .95, gamma .99 | trials to switch; accuracy after the break | decay switches in fewer than 10 trials |
| T4 Cold start | fresh store | prior pseudo-counts 0, 2, 5, 20, 255 | accuracy after 5, 20, 50 observations per class | moderate prior wins; extremes lose |
| T5 Temperature | same as T1 | t = 0.1, 0.25, 0.5, 1.0, decayed | solve rate | flat curve around 0.25 to 0.5 |
| T6 Credit | 3-step operator chains | end-of-episode equal credit vs discounted TD (gamma .95) | solve rate; operator rank accuracy | TD at least not worse |
| T7 Self-rating | same as T1 | scaffold counts vs model-rated success | solve rate; calibration gap | counts win; model rating inflated |
| T8 Table in prompt | strong vs weak model | raw log vs summary table | solve rate | strong model gains, weak does not (EVOLvE pattern) |
| T9 Negative update | same | no negative update on abandon vs full vs capped | solve rate; operator diversity | capped is safest |

## 9. What does not transfer, and why

- **Human timing costs (seconds) vs token costs.** Gray's cost trend is about time in a motor-visual task. Token cost is a proxy only. [b11-b13]
- **Production rules are fast, symbolic and tiny; operators here are long LLM calls with noisy, rare outcomes.** Tabular learning needed thousands of episodes for 12-34 steps. [b05-b07] Our budget gives tens of outcomes per class.
- **ACT-R assumes a reward signal at the goal.** Our checks (G3) give a pass/fail only for some items. [c07, c08]
- **Sugar-Factory-style instance learning is not utility learning** and should not be used as support. [a22, b04]
- **LLM-ACTR trains a model.** Our agent is scaffold-only. [K14]
- **Bandit studies are about the model's own exploration**, not reasoning operators. They justify keeping counts outside, but they test no operators. [critique]
- **Similarity-based utility (Feng) and similarity-ranked controls (MACLA) are not success-based ACT-R utility.** [c20, d05]
- **The 2023-24 model results** (GPT-3, GPT-4, Claude v1.3, Gemma, Flash) may not hold for current reasoning models; self-estimate studies of 2026 models (d12) show the overconfidence persists.
- **ACT-R's noise is a model of human variability**, not a design for exploration. For an agent, exploration noise is a tunable policy. [K04]

## 10. Open questions

1. Does scaffold-kept success/cost utility beat random and fixed order among reasoning operators at equal tokens? No ablation exists anywhere.
2. What were the original Lovett and Anderson (1996) data (N, fit, how many stayed with overshoot)? Only the 1995 precursor was read.
3. Which temperature and goal value G work, and how sensitive is accuracy?
4. How much credit assignment is needed for operator chains?
5. How many observations per context before learned rates beat a uniform prior (prior strength V)?
6. Do LLMs show the 0.87 vs 0.10 bias when asked to self-estimate operator success, compared with scaffold counts?
7. Are there 2024-26 ICCM or MathPsych papers using ACT-R utility in LLM agents that we missed? (Search tools were rate limited.)
8. What did Fu and Anderson (2006) show on recurrent choice and credit assignment? Full text blocked.
9. Does outcome-based shared utility transfer across tasks?
10. How to handle non-stationary operator success: decay of counts or a change detector?
11. Why did Qwen3-4B reach 89.2% in TextBandit when 8B did 37.5%? [d15]
12. Do the two ACT-R formulations produce different operator choices in our setting? [a25]

## 11. Sources

[V] opened this session (text read), [M] snippet or abstract only.

- [V] Taatgen, Lebiere and Anderson (2005/2006) Modeling paradigms in ACT-R. https://www.ai.rug.nl/~niels/publications/taatgenLebiereAnderson.pdf (a01-a05, a22, b01-b03, c01, c02, c04)
- [V] Lovett and Anderson (1995) Making heads or tails out of how people select problem-solving strategies. https://www.andrew.cmu.edu/user/lovett/cogsci95.html (d01)
- [V] Lovett (1993) Initial ACT-R production system for the Stick Building Task. https://www.andrew.cmu.edu/user/lovett/bst-model.txt (a11)
- [M] Lovett and Anderson (1996) History of success and current context in problem solving. https://doi.org/10.1006/cogp.1996.0016 (a26, c03)
- [V] Xie and Moss (2025) Task representation and individual differences affect strategy selection. https://pmc.ncbi.nlm.nih.gov/articles/PMC11958946/ (d02; first 100,000 of 123,767 characters)
- [V] Gray, Sims, Fu and Schoelles (2006) The soft constraints hypothesis. https://home.cs.colorado.edu/~mozer/Teaching/syllabi/3702/ (b11-b13)
- [V] Fu and Anderson (2004) Extending the computational abilities of the procedural learning mechanism in ACT-R. https://escholarship.org/uc/item/7zw5g0xj (d03)
- [M] Fu and Anderson (2006) From recurrent choice to skill learning. https://doi.org/10.1037/0096-3445.135.2.184 (a27, b14, c05)
- [M] Fu and Anderson (2006/2008) Solving the credit assignment problem. https://apps.dtic.mil/sti/html/tr/ADA459074/index.html (d04)
- [V] Walsh and Anderson (2011) Learning from delayed feedback. https://pmc.ncbi.nlm.nih.gov/articles/PMC3208325 (a20)
- [V] Walsh and Anderson (2012) Learning from experience: ERP correlates of reward. https://pmc.ncbi.nlm.nih.gov/articles/PMC3432149 (a21)
- [V] Gall and Fruehwirth (2014) Exchanging conflict resolution in an adaptable implementation of ACT-R. https://arxiv.org/pdf/1405.3570 (a06, a07, a25, b09, b10)
- [V] Whitehill (2013) Understanding ACT-R, an outsider's perspective. https://arxiv.org/pdf/1306.0125 (a08-a10)
- [V] Stocco et al. (2024) Fitting, evaluating, and comparing cognitive architecture models using likelihood: a primer. https://arxiv.org/pdf/2410.18055 (a13, a14, c07, c08)
- [V] Brasoveanu and Dotlacil (2020) Reinforcement learning for production-based cognitive models (ICCM paper and CUNY poster). https://people.ucsc.edu/~abrsvn/brasoveanu_dotlacil_RL_CUNY_2020.pdf (a17, a18, b05-b08, c06)
- [M] Brasoveanu and Dotlacil (2021) production-system RL vs ACT-R utility learning. https://research-portal.uu.nl/en/publications/reinforcement- (a19, b15)
- [V] Lebiere, Wallach and Taatgen (1998) ACT-R symposium: implicit and explicit learning. https://www.ai.rug.nl/~niels/publications/ECCM97.pdf (b04)
- [V] Anderson and Lebiere (1998) book review. https://www.ai.rug.nl/~niels/publications/tics.pdf (a24)
- [V] Zhu and Simmons (2024) Bootstrapping cognitive agents with a large language model. https://arxiv.org/pdf/2403.00810 (a12, a28, c09, c10)
- [V] Sumers, Yao, Narasimhan and Griffiths (2023) Cognitive architectures for language agents. https://arxiv.org/pdf/2309.02427 (b26, c11, c12)
- [V] Laird (2021) An analysis and comparison of ACT-R and Soar. https://arxiv.org/pdf/2201.09305 (a16)
- [V] Fan and Lan (2026) From cognitive architectures to language agents. https://arxiv.org/pdf/2607.23942 (a15)
- [V] Wu et al. (2024) Cognitive LLMs (LLM-ACTR). https://arxiv.org/pdf/2408.09176 (b16-b19)
- [M] Wu et al. (2025) Cognitive LLMs, journal review page. https://neurosymbolic-ai-journal.com/node/819 (c23; review page only)
- [V] Krishnamurthy et al. (2024) Can large language models explore in-context? https://arxiv.org/pdf/2403.15371 (b20, b21, c13, c14)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/pdf/2206.14576 (b22, b23, c15)
- [V] Nie et al. (2024) EVOLvE. https://arxiv.org/pdf/2410.06238 (b24, b25)
- [V] Schubert et al. (2024) In-context learning agents are asymmetric belief updaters. https://arxiv.org/pdf/2402.03969 (c16, c17)
- [V] Atalar, Zhang and Joe-Wong (2025) Neural bandit based optimal LLM selection. https://arxiv.org/pdf/2508.09958 (c18)
- [V] Life sciences agents with Thompson sampling (2025). https://arxiv.org/pdf/2512.03065 (c19, d07, d08)
- [V] Feng et al. (2026) Break it down, pass it on. https://arxiv.org/pdf/2608.20274 (c20, d14)
- [V] Chen et al. (2026) SkillCraft. https://arxiv.org/pdf/2603.00718 (c21)
- [V] Jiang et al. (2026) SoK: agentic skills. https://arxiv.org/html/2602.20867 (c22)
- [V] Wei et al. (2026) FadeMem. https://arxiv.org/pdf/2601.18642 (c24; declarative memory, not production selection)
- [V] Forouzandeh et al. (2025/2026) MACLA. https://arxiv.org/pdf/2512.18950 (d05, d06)
- [V] Yang et al. (2026) Think fast and slow (CogRouter). https://arxiv.org/pdf/2602.12662 (d09, d10)
- [V] Barkan, Black and Sourbut (2025) Do large language models know what they are capable of? https://arxiv.org/pdf/2512.24661 (d11)
- [V] Kaddour et al. (2026) Agentic uncertainty reveals agentic overconfidence. https://arxiv.org/pdf/2602.06948 (d12)
- [V] Taberner-Miller (2026) ParetoBandit. https://arxiv.org/pdf/2604.00136 (d13)
- [V] Lim et al. (2025) TextBandit. https://arxiv.org/pdf/2510.13878 (d15)
- [V] Zhang et al. (2025/2026) Comparing exploration-exploitation strategies of LLMs and humans. https://arxiv.org/pdf/2505.09901 (d16)
- [V] Sun et al. (2025) LLM-enhanced multi-armed bandits. https://arxiv.org/pdf/2502.01118 (d17; abstract and introduction only)
- [M] Search note: the arXiv, Semantic Scholar and OpenAlex APIs returned 429; no ICCM/MathPsych 2024-26 sweep (c25).
