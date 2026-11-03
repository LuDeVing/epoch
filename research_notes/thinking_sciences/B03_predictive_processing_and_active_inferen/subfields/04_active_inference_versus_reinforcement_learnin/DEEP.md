# Active inference versus reinforcement learning: deep document

*Subfield B03.04. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K30), critique.md in this folder. Evidence ids a01-d17 refer to those files. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested.*

## 1. What it is

Reinforcement learning (RL) says an agent learns a value for each state or action from a scalar reward, then acts to collect reward. Active inference says an agent holds a generative model of the world. Reward is not special. It is one more observation, and the agent holds a prior preference over it. The agent picks policies that minimise expected free energy (EFE). EFE has two parts: a pragmatic part (reach preferred outcomes) and an epistemic part (reduce uncertainty about states and model parameters).

Two consequences matter for us.
1. Flatten the preference and the agent still acts. It explores, because the epistemic term remains. Q-learning with no reward learns nothing.
2. Exploration and exploitation come from one objective, not a bolted-on bonus.

The anchor paper is Sajid, Ball, Parr, Friston (arXiv 1909.10863) on a 3x3 FrozenLake from OpenAI Gym. Later work tests the idea in deep RL (Tschantz, Millidge, Fountas, Champion) and, recently, in LLM agents (BED-LLM, PUMA, Voyager-style curricula).

Why it matters for our agent: open mode needs exploration without a reward signal. The question is what to borrow: the full EFE machinery, or only the small pieces that survive testing (a code-kept hypothesis list, an information-gain probe, a stop rule).

## 2. History and theories in depth

**Control as inference (pre-2019).** RL can be written as inference: reward becomes the likelihood of an "optimality" variable. Active inference differs in where value enters (the prior over outcomes, not the likelihood) and in which information terms are kept (Millidge et al. 2020, a21, c12). Control as inference has an observation-ambiguity term that active inference lacks. Active inference has expected information gain on parameters.

**Scaling active inference (2019).** Tschantz, Baltieri, Seth, Buckley (a23, b09, c10, c11) used a learned model with the extrinsic term only, on shaped continuous control. Active inference converged in under 100 epochs. DDPG was shown over 1500 epochs. Five seeds. The gain is a model-based gain, not proof for the epistemic term.

**Deep active inference as policy gradients (Millidge 2019, b10, b11).** 20 trials x 15000 episodes. Most of the gain on CartPole came from the entropy term (reward 500). Epistemic value had no measurable effect on CartPole, Acrobot or Lunar Lander. On Lunar Lander it underperformed direct policy gradients; the author blamed an inaccurate EFE value network.

**Sajid et al. 2021 (a01-a10, c01-c07).** "Demystified and compared." Five agents on FrozenLake: Q-learning (eps 0.1), Q-learning (eps decaying 1 to 0), Bayesian model-based RL (Thompson sampling, Dyna-style, Beta counts start at 1, k=50 sampled MDPs, discount 0.9), active inference, and a null active inference agent with a flat preference. Q-learning: rate 0.5, discount 0.99. Details in section 3.

**Tschantz et al. 2020, FEEF (a11-a14, b06-b08, c08, c09).** A "free energy of the expected future" agent with an ensemble model, on sparse Mountain Car, Cup Catch, shaped Half Cheetah, and reward-free Ant Maze.

**Theory papers.**
- Millidge, Tschantz, Buckley, "Whence the EFE" (a22, b12): EFE equals the free energy of the future minus expected information gain. The natural "free energy of the future" discourages information seeking. So EFE is not derived cleanly from first principles. FEEF keeps the information term.
- Da Costa et al. 2022/2023 (a15, b13, c13): standard discrete active inference is Bellman-optimal only at horizon 1 with known MDP and zero temperature. Sophisticated inference (recursive) recovers backward induction at any finite horizon, for known finite-horizon POMDPs with exact state estimation.
- Hafner et al. 2022 (a24, b20; abstract only): active inference maximises the probability of inputs under the model, giving smaller niches in noisy worlds.
- Wei 2024 (b14): regret gap to Bayes-optimal RL linear in horizon and quadratic in information gain, under a density-ratio bound; reward and information gain must be balanced by a temperature. Not turned into a usable rule.

**Deep active inference with MCTS (Fountas 2020, a17, a18, b15, c14).** Compared three EFE forms with a reward-maximising baseline. Similar reward per round, more positions visited, lower reward reconstruction error. Beat DQN and A2C and matched PPO2 on Animal-AI at 2M iterations. The authors call these illustrations, not state-of-the-art claims; baselines were default OpenAI baselines.

**Champion et al. 2024 (b16-b18), a contrarian view.** On dSprites, only variants that behave like reward maximisers solve the task. EFE agents choose nearly a single action. Adding 1% information gain after 200K steps drastically cuts reward. This contests the mechanism claimed in earlier reports.

**Exploration vs preference (Sajid 2021b, a19, a20).** Reward-free FrozenLake with changing maps. Exploration (Hausdorff distance of trajectories) peaks at 50% volatility. At 100% volatility, agents learn bimodal preferences: a noisy-TV collapse.

**Contrastive active inference (Mazzaglia 2021, b19).** No pixel likelihood. About 16% faster than Dreamer on Reacher; likelihood-based active inference was 224% slower and failed on Reacher.

**LLM era (2023-2026).** See section 6.

## 3. Core findings with exact numbers

Scores are average reward per episode, scaled to 100 for a goal. 95% CIs in brackets.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Null agent with flat preference scores chance | 50.03 [49.70, 50.35] deterministic; 50.22 stochastic (upper CI prints as 50.22, likely a typo) | Sajid 2021, a03, c02 | [S] |
| Deterministic FrozenLake: active inference equals Bayesian RL | AI 99.88 [99.64, 100]; BRL 99.76 [99.45, 100]; Q-learning eps 0.1 97.79 [97.41, 98.16]; Q-learning eps decaying 80.44 [78.96, 81.93]. 200 trials x 500 episodes | Sajid 2021 Table 1, a03 | [S] |
| Stochastic FrozenLake: active inference far above RL | AI 98.90 [98.00, 99.79]; BRL 64.39 [60.33, 68.44]; Q eps 0.1 66.08 [63.28, 68.88]; Q decaying 65.13 [62.57, 67.68] | Sajid 2021, a04 | [S] one paper, naive baselines |
| Hidden goal swap (episodes 21, 121, 141, 251, 451) | Active inference recovers in 1 episode; Q-learning and BRL need about 40; BRL gets slower with each swap; Q eps 0.1 adapts fairly quickly | Sajid 2021, a05, b03, c03 | [S] built-in context state |
| No reward at all | Q-learning 0.00 (15.00 moves, circular policy); BRL 39.94 (9.17 moves); AI 44.00 (8.67 moves). 100 episodes x 100 agents | Sajid Table 2 row 1, a07, c04 | [S] |
| Reward shaping (goal 100) | Goal only: Q 95.32 (3.58), BRL 99.74 (3.00), AI 99.50 (3.07). Goal 100, hole -100: Q 95.56 (3.53), BRL 99.77, AI 99.52. Goal 100, step -10: Q 96.00 (3.48), BRL 99.89, AI 99.47. All three: Q 96.47 (3.42), BRL 99.79, AI 99.58 | Sajid Table 2, a06, c07 (corrected in critique) | [S]; Q spread only about 1.2 points |
| Negative preference only | Hole -100 and nothing else: all three agents score 0.00 and use 15 moves (avoid both tiles, never reach goal) | Sajid Table 2, a08 | [S] |
| Preference learning can lock in a bad goal | Agent that hits the hole first comes to prefer holes (about 5 trials); 10 simulations per case; null model with no learning ended at goal 44.0% | Sajid, a10, b05, c06 | [S] |
| Sparse Mountain Car | FEEF reaches optimal return after trial 1; reward-only baselines on average unable to reach goal; FEEF visited nearly all state space in 20 episodes. 25 episodes, 5 seeds | Tschantz 2020, a11, a12, b06 | [S] |
| Cup Catch boundary | All agents converge in about 20 episodes; SAC is a fixed reference | Tschantz 2020, a12, b07 | [S] |
| Reward-free Ant Maze | FEEF coverage above random; 35 episodes, 4 seeds; exact percent only in a figure | Tschantz 2020, a13, b08 | [S] |
| Shaped continuous control sample efficiency | Active inference under 100 epochs vs DDPG 1500; about 10x; extrinsic term only; 5 seeds | Tschantz 2019, a23, b09 | [E] 2 sources, model-based gain |
| Entropy, not epistemic term, drives CartPole gain | CartPole reward 500 with entropy; epistemic no effect on CartPole, Acrobot, Lunar Lander | Millidge 2019, b10, b11 | [S] |
| dSprites does not reproduce as EFE minimiser | Reward-only variants solve it; EFE picks nearly one action; 1% information gain after 200K steps cuts reward | Champion 2024, b16-b18 | [C] |
| Fountas MCTS agent | Matches reward-only agents on reward, explores more; beats DQN and A2C, matches PPO2 on Animal-AI at 2M iterations | Fountas 2020, a17, c14 | [C] |
| Backward induction theorem | Optimal at horizon 1 (standard); recursive scheme recovers it at any finite horizon | Da Costa 2022, a15, c13 | [S] theory |
| EFE is not the free energy of the future; AI and control-as-inference differ | Sign of information gain term differs; ambiguity term differs | Millidge 2020, a21, a22 | [E] 3 papers, theory |
| Regret bound | Linear in horizon, quadratic in information gain | Wei 2024, b14 | [S] |
| Volatility inverted U | Exploration peaks at 50% volatility; bimodal preferences at 100% | Sajid 2021b, a19, a20 | [S] |
| Contrastive active inference | About 16% faster than Dreamer on Reacher; likelihood AIF 224% slower | Mazzaglia 2021, b19 | [S] |
| GPT-4 bandit exploration | Works in one scaffolded config only (suggestive framing, summarised history, reinforced chain of thought, T=0); basic prompt: suffix failures in over 60% of 20 replicates at T=500; hard instance K=5, gap 0.2 | Krishnamurthy 2024, c15, c16 | [E] with EVOLvE |
| Code-computed statistics help LLM bandits | Gemini Pro MAB win rate 45.5 (raw history) to 59.6-60.0; contextual 7.1 to 64.3; Gemma-2B/9B gain nothing | EVOLvE 2025, d10 | [E] with c15 |
| GPT-3 explores randomly, not directedly | Random exploration beta=0.18+-0.01 (p<.001); horizon effect beta=-0.15+-0.27, p=.58; regret 2.72 vs humans 3.24 | Binz and Schulz 2023, c17, c18 | [S] |
| Voyager | Wooden tool 6+-2 vs AutoGPT 92+-72 iterations; iron 21+-7 vs 135+-103; diamond 1/3; ReAct and Reflexion 0/3 at every level. Ablation: random curriculum -93% items, no self-verification -73%, GPT-3.5 5.7x fewer items | Wang 2023, c19, c20, d16 | [S] 3 runs each |
| Perplexity bonus in LLM RL | Qwen3-4B GRPO AIME24 20.8 to 23.3; AIME25 21.0 to 23.5; average 48.2 to 50.6; PPO 46.5 | CDE 2025, c21 | [E] with c22 |
| EIG question choice, 20 Questions | Animals: Mistral-Large 33 to 95; Llama-3.1-8B 8 to 63; GPT-4o 45 to 93; GPT-4o-mini 44 to 88; Qwen2.5-72B Prompt-Only 45, CoT 51, Split 87, Entropy 85, BED-LLM 95. 100 targets per set | BED-LLM 2026, d01, d02 | [S] not token-matched |
| Information-gain benefit shrinks when target is vague | Film elicitation: Prompt-Only strong; history-updated likelihood did not help (GPT-4o 93 vs 86) | BED-LLM, d03 | [S] |
| User-state tracking by information gain | CAMI next-state accuracy 0.717 vs 0.231; Stage Lift 1.62 vs 1.07; Prep 75.9% vs 52.0%; TrigCov 62.4% vs 34.0%; turns 12.2 vs 13.1; AnnoMI Qwen3-8B 0.639/0.532 vs Qwen3-32B long prompt 0.602/0.430 | PUMA 2026, c26, c27 | [S] simulator |
| Token-aware stop rule for questions | Threshold 0.01, max 2 questions: 0.375 compliance at about 219 tokens vs 0.0417 at about 112 tokens with no questions; 48 tasks, simulated | Dutta 2026, d05, d06 | [S] |
| Noisy-TV defence | Stochastic MountainCar coverage drops 12.4% for learning-progress monitoring vs 33-86% for others; MiniWorld 1,347.6 states, 95.3 more than second best | Hou 2026, d08 | [S] deep RL only |
| LLMs perseverate after reversal | 7.2-10.9 trials (Gemini-3, GPT-5.2), 19.6-27.4 (DeepSeek-V3.2), humans 2.9; N=200 runs per cell; lose-shift 0.035 to 0.241 vs humans 0.495 | Wang 2026, d11 | [S] |
| Self-judged objectives drift | Judge scores rise while human ratings stall; better specification does not stop in-context reward hacking | Pan 2024 x2, d14, d15 | [S] indirect |

## 4. Mechanisms and models

**4.1 The discrete active inference agent (what Sajid ran).**
- Model: likelihood A (state to observation), transitions B (state, action to next state), prior preferences C (over observations, including reward), initial prior D.
- Beliefs: infer a posterior over hidden states from observations.
- Policy score: for each policy pi, G(pi) = sum over future steps of [risk: KL between predicted and preferred outcomes] + [ambiguity: expected observation entropy] - [expected information gain about parameters].
- Choice: softmax over -G(pi) with a precision (temperature). At zero temperature and horizon 1 this is greedy on expected reward (Da Costa theorem).
- Learning: Dirichlet counts on A and B (and optionally C). Counts start at 5 for likelihoods and 1 for preferences in the paper. Each observation increments a count. Low counts mean parameter uncertainty, which gives the epistemic pull.
- Reward as observation: C puts high log-probability on the goal observation and low on the hole. Flat C is the null agent.
- Sophisticated inference: score G recursively over action-observation trees, like backward induction, so later beliefs inform earlier choices.

**4.2 The RL baselines (Sajid).** Q-learning: tabular, learning rate 0.5, discount 0.99, eps 0.1 or decaying 1 to 0. Bayesian model-based RL: Beta pseudo-counts start at 1, sample k=50 MDPs by Thompson sampling, solve each by value iteration, discount 0.9. It has no explicit "context switched" state. That is why it is slow after a goal swap. It is a naive baseline, and the authors say a richer agent might match.

**4.3 FEEF (Tschantz).** Ensemble of learned dynamics models. Score each candidate action sequence by expected reward plus ensemble disagreement (information gain), plan by sampling. Bound: FEEF >= KL[p(o|pi) || p(o)] (a14). Needed for sparse reward, where reward-only agents never see a signal.

**4.4 What an engineer can build for an LLM scaffold (distilled from the evidence).**
- Keep a hypothesis list in code (BED-LLM): candidates for the target or rule. The LLM proposes candidates and answers likelihood queries; code holds the list.
- Score each candidate probe by expected information gain: entropy of the hypothesis distribution minus expected entropy after the answer. The LLM estimates P(answer | hypothesis, probe); code does the sums.
- Filter hypotheses inconsistent with observed answers. Most of the gain comes from this (even-split alone gets 85-87 vs 95).
- Add a pragmatic term only where a goal check exists.
- Stop rule: stop when the last K answers did not change the hypothesis set (learning-progress analogue), or when information per token falls under a threshold (Dutta: 0.01, max 2 questions).
- Context-switch hypothesis: keep "the rule changed" as an explicit hypothesis with its own prior; update it after a surprise. This produced one-episode recovery in Sajid.
- Code-kept history: compute counts and summaries in code, do not leave raw history to the LLM (EVOLvE).

## 5. What holds up

**Holds (two or more sources).**
- LLMs explore poorly by default and code-computed history and statistics help (Krishnamurthy c15/c16; EVOLvE d10). Small models gain nothing.
- Exploration bonuses help even when reward exists in LLM training (CDE c21; personalisation curiosity reward c22).
- Model-based active inference is about 10x more sample efficient than model-free DDPG on shaped tasks (a23, c11), but that is the model, not the epistemic term.
- Theory: EFE is not the free energy of the future; active inference and control-as-inference differ (a21, a22, c12).

**Does not hold, or is contested.**
- Deep active inference as EFE minimiser: Champion 2024 (dSprites) and Millidge 2019 find the epistemic term useless or harmful on easy dense tasks. Fountas 2020 reports exploration without reward cost. Different scales and objectives, so not a strict conflict, but the epistemic benefit is clean only in tiny or sparse tasks.
- Tschantz (epistemic term wins on sparse Mountain Car) vs Millidge/Champion (no benefit). Difference: a learned ensemble and a task where reward-only agents never see reward.
- The Sajid headline (99 vs 64 stochastic) has no independent replication. Hashash 2026 (d12) uses another weak Bayesian RL baseline. Stays single-source.

**Boundary conditions.**
- Easy tasks: no gain from directed exploration (Cup Catch, K08).
- Vague targets: information-gain probes help less (BED-LLM film task, K25).
- High volatility: exploration collapses to noise (Sajid 2021b, 100% volatility).
- Negative-only preferences: the agent avoids but never reaches the goal.
- Learned preferences can drift to a bad attractor (hole preference).

**Moderators.** Model size (EVOLvE: small models gain nothing from summaries), crispness of the hypothesis space, whether reward is sparse, whether a context state exists.

**Interventions that worked.** Code-side statistics (EVOLvE), hypothesis filtering plus EIG (BED-LLM), exploration curriculum with skill library (Voyager), perplexity bonus (CDE), token-capped asking (Dutta).

**Did not work.** Plain prompting to "be exploratory" (Krishnamurthy basic prompt); history-updated likelihoods in BED-LLM; 1% information gain added late in dSprites; likelihood-based active inference on Reacher.

**Limits on the evidence.** Some evidence lines mislabelled Sajid's Q-learning rows; corrected in critique items 1 and 2 (eps 0.1 row is 97.79 deterministic and 66.08 stochastic; decaying row is 80.44 and 65.13). Tschantz gives no text numbers for Ant Maze coverage. Voyager had 3 runs per method. BED-LLM baselines are not token-matched.

## 6. Language models

**Default exploration is weak.** GPT-3.5/GPT-4 on a K=5, gap 0.2 bandit: only one scaffolded configuration explored well. The basic prompt had suffix failures (stop pulling the best arm, never recover) in over 60% of 20 replicates at T=500 (c15, c16). GPT-3 shows random exploration (beta=0.18) but no directed exploration (horizon effect beta=-0.15+-0.27, p=.58) while beating humans on regret (2.72 vs 3.24; c17, c18). A good score can hide missing information seeking, so measure distinctness separately.

**What changed it.** Code-computed summaries and exploration statistics: Gemini Pro 45.5 to 59.6-60.0 (MAB), 7.1 to 64.3 (contextual). Gemma 2B/9B: no gain (d10).

**Adapting to change.** After a hidden reversal, Gemini-3 and GPT-5.2 perseverate 7.2-10.9 trials, DeepSeek-V3.2 19.6-27.4, humans 2.9 (N=200 per cell; d11). No scaffold fix tested.

**Information-gain question asking.** BED-LLM (d01-d03), Animals, Prompt-Only vs BED-LLM: GPT-4o-mini 44 to 88, GPT-4o 45 to 93, Llama-3.1-8B 8 to 63, Mistral-Large 33 to 95. Ablations (Qwen2.5-72B Animals): CoT 51, Split 87, Entropy 85, in-context beliefs 46, implicit max 61, full 95. Mazzaccara (d04) trained questioning: INLG zero-shot 56.7%, DPO 68.9%, EIG 0.34 to 0.45. Boundary: smaller gain on vague film preferences.

**Active inference in LLM agents.** Prakki 2025 (a26, b21, c23): qualitative, no baseline. Wen 2025 (a25, b22, c24, c25): position papers, no experiments. Dutta 2026 (d05-d07): framework, oracle gap, small simulated gains (0.375 vs 0.0417 compliance), no plain-prompt baseline. PUMA 2026 (c26, c27): Stage Lift 1.62 vs 1.07; CAMI next-state accuracy 0.717 vs 0.231; an 8B model beat a long-prompt 32B on AnnoMI. Simulator only.

**Reward-free exploration in agents.** Voyager (c19, c20, d16): wooden tool 6+-2 vs 92+-72; a random curriculum cuts items by 93%, no self-verification by 73%. Not token-matched, not active inference.

**Training time.** CDE perplexity bonus: AIME24 20.8 to 23.3 (Qwen3-4B-Base, GRPO, Avg@16).

**Drift.** Self-judged objectives drift: judge scores rise while humans stall; larger models drift more with shared context (d14, d15).

No study tests reward-as-observation inside an LLM scaffold against a reward-driven baseline at equal tokens.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Keep exploration history and summary statistics (what was tried, counts) in code, not as raw context; use for open mode and probe selection. Helps frontier models, not small ones | S3 open mode, memory | [E] | c15, c16, d10 (K18) |
| Do not read exploration quality from score. Track distinct valid attempts separately from accuracy | G12 / bench metric | [E] indirect | c17, c18, d10 |
| Treat "EFE as one principled objective" as theory only. Do not copy EFE formulas into the schema | none | [E] | a21, a22, c12 (K14) |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Code-kept hypothesis list with EIG-ranked probe and consistency filter | S3 probe | [S] | d01, d02, d04 (K24) |
| Apply the probe only when the hypothesis space is crisp | G12 | [S] | d03 (K25) |
| Coverage tracker for reward-free open mode | S3 open mode | [S] | a07, a11-a13 (K04, K07) |
| Skip diversity machinery on easy items | G12 | [S] | a12, b07 (K08) |
| Explicit "rule may have changed" hypothesis tested after surprise | S9 / memory | [S] | a05, d11 (K03, K28) |
| Stop a probe direction when the last K answers did not change the hypothesis set | open mode stop | [S] | d08 (K26) |
| Cap probes per item; stop on information per token | G12 budget | [S] | d05, d06 (K27) |
| Fixed success criterion, not agent-edited | G5 / G8 | [S] | a10, d14, d15 (K06, K29) |
| Positive goal check at S8 (avoid-errors-only stalls) | S8 | [S] | a08 (K05) |
| Recursive step-by-step planning vs whole-plan choice | S6 | [S] | a15 (K13) |
| Code-driven curriculum of untried directions | S3 open mode | [S] | c19, d16 (K20) |
| Exploration weight scaled by difficulty | G12 | [S] | b14 (K15) |
| Mixing information-gain weight into a goal-driven loop | G12 | [C] | b16-b18 (K11) |

## 8. Concrete tests on our bench

All arms at equal tokens. Report accuracy, tokens, and distinct valid outputs.

1. **EIG probe vs "try something different".** Items: hidden-target text game (crisp set of 100+ targets) and underspecified bench items. Arms: A plain prompt; B code-kept hypothesis list with consistency filter and EIG ranking. Metric: success within N probes. Expected: B well above A (BED-LLM roughly 2x, not token-matched, so expect less).
2. **Filter alone vs full EIG.** Arms: filter plus random probe; filter plus even-split; full EIG. Metric: success. Expected: most gain from the filter (85-87 vs 95).
3. **Hidden-switch text world.** Rule changes mid-session. Arms: plain memory vs explicit "rule changed" hypothesis. Metric: steps to recover. Expected: faster recovery (Sajid's 1 vs 40 episodes is an upper bound).
4. **Open-mode coverage.** Reward-free generation task. Arms: isolated attempts with a code-kept coverage tracker vs free self-prompting. Metric: distinct valid outputs. Expected: more distinct outputs, larger on sparse-success tasks.
5. **Easy-item skip.** Easy items. Arms: probe machinery on vs off. Metric: accuracy and tokens. Expected: same accuracy, fewer tokens when off.
6. **Stop rule.** Task with a random-answer source. Arms: surprise-seeking probes vs stop when K answers do not change the hypothesis set. Metric: tokens wasted, accuracy. Expected: tokens saved, accuracy held.
7. **Criterion drift.** 10 refinement rounds. Arms: fixed written criterion with separate-context judge vs agent-edited criterion. Metric: drift, gold accuracy. Expected: fixed drifts less.
8. **Probe cap.** Arms: no cap, cap 2, entropy-per-token threshold 0.01. Metric: success per token.
9. **Information-gain weight sweep.** Weights 0, 1%, 10%, 50% in a goal-driven loop. Metric: accuracy. Expected: inverted U or monotone loss (Champion).
10. **Whole-plan vs recursive planning.** Multi-step items. Metric: accuracy at equal tokens.

## 9. What does not transfer, and why

- **Tabular belief updates.** The FrozenLake agent knows the goal is at position 6 or 8. Our tasks have open hypothesis spaces.
- **One-episode recovery.** It comes from a built-in context state, not from "reward as observation". A richer RL agent could match it.
- **Dirichlet learning and EFE gradients.** Deep-RL results (Tschantz, Millidge, Champion, Fountas) need gradient learning. We train nothing.
- **Sample-efficiency gains over DDPG.** Model-based vs model-free is a different axis.
- **Training-time bonuses (CDE, curiosity rewards).** Need weight updates; at most a hint that bonuses help.
- **Voyager.** Gains mix curriculum, verification and skill library; it is not active inference.
- **The EFE formula itself.** Not a clean derivation (Millidge 2020). Implementing it adds nothing the EIG probe lacks.
- **LLM likelihoods.** LLM probabilities inside EIG are noisy; small models do not benefit from code-side statistics.

## 10. Open questions

1. Does Sajid's FrozenLake result survive a stronger RL baseline with an explicit context belief? No replication found.
2. Does an EIG probe beat a plain prompt at equal tokens in open mode? BED-LLM is not token-matched and not open mode.
3. What information-gain weight stops hurting accuracy in goal-driven loops? Only Dutta's tuned threshold exists.
4. Is there a code-side stop rule that works for LLMs against noisy-TV? Only deep RL evidence (Hou 2026).
5. Does an explicit context-switch hypothesis fix LLM perseveration (7-27 trials vs 2.9 for humans)?
6. Do self-written preferences drift in LLM agents as the hole preference did? No fixed-versus-self comparison.
7. Voyager: curriculum or skill library? Needs an equal-token ablation.
8. Can Wei's regret bound become a rule for exploration budget by difficulty?
9. Does Dutta 2026 (2608.19202) beat a plain-prompt baseline?
10. Are there other 2026 expected-free-energy question-asking papers beyond BED-LLM and PUMA? None found.

## 11. Sources

[V] opened (PDF or HTML text read); [M] snippet only.

- [V] Sajid, Ball, Parr, Friston (2021) Active inference: demystified and compared. https://arxiv.org/abs/1909.10863
- [V] Tschantz, Millidge, Seth, Buckley (2020) Reinforcement learning through active inference. https://arxiv.org/abs/2002.12636
- [V] Tschantz, Baltieri, Seth, Buckley (2019/2020) Scaling active inference. https://arxiv.org/abs/1911.10601
- [V] Millidge (2019) Deep active inference as variational policy gradients. https://arxiv.org/abs/1907.03876
- [V] Millidge, Tschantz, Buckley (2020/2021) Whence the expected free energy? https://arxiv.org/abs/2004.08128
- [V] Millidge, Tschantz, Seth, Buckley (2020) On the relationship between active inference and control as inference. https://arxiv.org/abs/2006.12964
- [V] Da Costa, Sajid, Parr, Friston, Smith (2022/2023) Reward maximisation through discrete active inference. https://arxiv.org/abs/2009.08111
- [V] Fountas, Sajid, Mediano, Friston (2020) Deep active inference agents using Monte-Carlo methods. https://arxiv.org/abs/2006.04176
- [V] Sajid, Tigas, Zakharov, Fountas, Friston (2021) Exploration and preference satisfaction trade-off in reward-free learning. https://arxiv.org/abs/2106.04316
- [V] Champion, Grzes, Bonheme, Bowman (2024) Deconstructing deep active inference. https://cs.kent.ac.uk/people/staff/mg483/documents/champion24deconstructing_DAI.pdf (read in part)
- [V] Mazzaglia, Verbelen, Dhoedt (2021) Contrastive active inference. https://arxiv.org/abs/2110.10083
- [V] Wei (2024) Value of information and reward specification in active inference and POMDPs. https://arxiv.org/abs/2408.06542
- [M] Hafner, Ortega, Ba, Parr, Friston, Heess (2022) Action and perception as divergence minimization. https://arxiv.org/abs/2009.01791
- [V] Krishnamurthy, Harris, Foster, Zhang, Slivkins (2024) Can large language models explore in-context? https://arxiv.org/abs/2403.15371
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] CDE (2025) Curiosity-driven exploration for efficient RL in large language models. https://arxiv.org/abs/2509.09675
- [V] Enhancing personalized multi-turn dialogue with curiosity reward (2025). https://arxiv.org/abs/2504.03206
- [V] Prakki (2024/2025) Active inference for self-organizing multi-LLM systems. https://arxiv.org/abs/2412.10425
- [V] Wen (2025) The missing reward: active inference in the era of experience. https://arxiv.org/abs/2508.05619
- [V] Wen (2025) A framework for inherently safer AGI through language-mediated active inference. https://arxiv.org/abs/2508.05766
- [V] Know You Before You Speak (PUMA/CAMI, 2026). https://arxiv.org/abs/2605.24647
- [V] Choudhury et al. (2026, ICLR) BED-LLM. https://arxiv.org/abs/2508.21184
- [V] Mazzaccara, Testoni, Bernardi (2024) Learning to ask informative questions. https://arxiv.org/abs/2406.17453
- [V] Dutta, Ramachandran, Sra (2026) Active inference as context acquisition for AI agents. https://arxiv.org/abs/2608.19202
- [V] Hou, An, Du (2026, ICLR) Beyond noisy-TVs: learning progress. https://arxiv.org/abs/2509.25438
- [M] Mavor-Parker et al. (2022) How to stay curious while avoiding noisy TVs. https://arxiv.org/abs/2102.04399
- [V] Nie et al. (2025) EVOLvE. https://arxiv.org/abs/2410.06238
- [V] Wang, Ward, Zhang (2026) Comparative reversal learning in LLMs. https://arxiv.org/abs/2604.04182
- [V] Hashash et al. (2026) Active inference as the test-time scaling. https://arxiv.org/abs/2606.22813
- [V] Pan, Jones, Jagadeesan, Steinhardt (2024) Feedback loops drive in-context reward hacking. https://arxiv.org/abs/2402.06627
- [V] Pan, He, Bowman, Feng (2024) Spontaneous reward hacking in iterative self-refinement. https://arxiv.org/abs/2407.04549
- [M] APEX agent forum post. https://discuss.google.dev/t/apex-agent-beyond-react-autogpt-active-inference-hierarchical-world-models-meta-cognition-for-agi-level-agency/336867
- [M] Cullen et al. (2018), second hand via Da Costa 2022 (a28).
