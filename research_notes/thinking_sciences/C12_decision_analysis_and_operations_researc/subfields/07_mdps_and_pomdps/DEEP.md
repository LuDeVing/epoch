# MDPs and POMDPs: deep document

*Subfield C12.07. Sequential decisions under uncertainty and belief states. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K27), critique.md in this folder. Evidence ids (a01, b09, d04 ...) point to lines in the evidence files. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. No search was run for this step.*

## 1. What it is

A Markov decision process (MDP) is a model of choosing actions over time. There is a set of states, a set of actions, a rule for how an action moves the state (with chance), and a reward. The agent sees the state. The best policy maps each state to an action. Value iteration and policy iteration find it (Bellman; Puterman 1994 is the standard book [b25, not opened]). In the discounted model an optimal deterministic stationary policy exists (a07). Value iteration can stop when two successive value functions differ by less than epsilon; the greedy policy is then within 2*epsilon*gamma/(1-gamma) of optimal (a07).

A partially observable MDP (POMDP) adds one fact: the agent does not see the state. It sees an observation that is a noisy function of the state. The agent keeps a belief state, a probability distribution over hidden states. The belief is a sufficient statistic for the whole history and the starting belief (a01, quote: "comprise a sufficient statistic for the past history and initial belief state of the agent"). So a POMDP is an MDP whose "state" is the belief. The optimal t-step value function over beliefs is the max over policy trees of linear functions of the belief. It is piecewise linear and convex (a02, b01). Values are high where the belief is lopsided (low entropy) and low where it is mixed.

Why this matters for our agent. Every hard task the agent sees is a POMDP in disguise. The true answer, the true rule or the true fault is hidden. The agent gets clues (test outputs, examples, replies). It chooses actions: gather more evidence, test a candidate, commit, revise. The POMDP view gives us three things the schema needs:

1. A state to carry: a posterior over hypotheses, not the raw transcript (K01).
2. A reason to gather evidence only when it pays, and a rule for when to commit (K03).
3. A reason to keep competing hypotheses apart instead of collapsing to the most likely one (K06).

It also gives a warning. Exact solving is intractable (K02). The agent must plan on a few sampled beliefs, with a bounded budget (K04).

Important limit: the evidence base for LLMs on true POMDPs is thin. Only one preprint (BSE, N=40) tests a chat LLM on a classic POMDP (K23). Most LLM evidence comes from bandits, planning domains, games and twenty-questions tasks.

## 2. History and theories in depth

**1950s-60s: MDPs.** Bellman's dynamic programming gives the optimality equation. Value iteration and policy iteration follow. Puterman (1994) collects the theory for finite and infinite horizons, discounted, average and total reward. We did not open Puterman (b25). Statements about it here rest on the Kaelbling survey (a07).

**1987: complexity.** Papadimitriou and Tsitsiklis show the finite-horizon MDP decision problem is P-complete and the finite-horizon POMDP decision problem is PSPACE-complete. We confirmed this only through a restatement in Bernstein, Givan, Immerman and Zilberstein 2002 (d18). The 1987 paper was not opened (a10, b23). Worst-case result only. Structured instances can be easy.

**1996: the RL survey.** Kaelbling, Littman and Moore (a07, a08) name the hidden-state problem "perceptual aliasing". Treating observations as states fails when different states look alike but need different actions. Their office-to-printer example shows it.

**1998: the founding POMDP paper.** Kaelbling, Littman and Cassandra (a01-a06, b01, b02):
- The belief update is Bayes' rule. Worked example: 4 states, start belief [0.333 0.333 0 0.333]. After an action with no goal seen, non-goal states never reach zero.
- Value over beliefs is piecewise linear and convex (a02).
- Tiger problem (a03): two doors. LISTEN costs -1. Correct door +10. Tiger door -100. Listening is 85% accurate. Opening a door resets the belief to (0.5, 0.5). Opening at random is worth (-100+10)/2 = -45. Listening is worth -1.
- Finite horizon (a04): at t=1 all three actions are optimal for some belief. At t=2 and t=3 from the uniform belief, the optimal policy only listens ("it never chooses to act, only to listen"). The 2-step value function has five linear regions.
- Infinite horizon (b01): keep listening until the tiger was heard twice more on one side than the other.
- Exact value iteration makes vector sets that can grow exponentially each step. The witness algorithm is polynomial in output size, not in the worst case (a05). Infinite-horizon value functions can have infinitely many segments unless the policy is finitely transient.
- Plan graphs (a06): the optimal Tiger policy can be drawn as a finite graph that picks actions with no explicit belief. Graph position stands in for the belief.
- Fragility of memory (b02): lowering listen accuracy from 0.85 to 0.65 makes the optimal plan graph much larger.

**1999-2003: undecidability.** Madani, Hanks and Condon prove that policy existence for infinite-horizon POMDPs is undecidable under discounted, undiscounted total, average reward and state-avoidance criteria (a09, d19). Only the abstract and a 2026 restatement were read. Decidable subclasses exist (posterior-deterministic POMDPs, which include all MDPs and Tiger, per a 2026 restatement). Chatterjee, Chmelik and Tracol (d20): quantitative analysis for omega-regular objectives is undecidable; qualitative analysis is EXPTIME-complete with finite-memory strategies.

**2003-2013: approximate planners.**
- PBVI (Pineau, Gordon, Thrun 2003; a11, a12): back up only a fixed set of reachable belief points, one vector per point, and grow the set over time. Claim: history size, not state count, drives cost.
- Perseus (Spaan and Vlassis 2005; a13, a14): back up a random subset of beliefs. This can still improve the value of every belief in the set. Much smaller value functions.
- SARSOP (Kurniawati, Hsu, Lee 2008; a18): sample near the optimally reachable belief space, a small subset of reachable space.
- POMCP (Silver and Veness 2010; a15-a17, b03, b04): Monte Carlo tree search over histories with an unweighted particle filter belief and a black-box simulator. One set of simulations serves search and belief update.
- DESPOT (Somani, Ye, Hsu, Lee 2013; a19, a20, d16): search a tree built from K sampled scenarios and penalise policy size to avoid overfitting to the samples.

**2015-2022: deep RL with memory.** Hausknecht and Stone (a21, a22, b05): an LSTM replaces the frame stack. No systematic gain on standard Atari (they are MDPs given 4 frames). Gains appear when observations go missing. Ni, Eysenbach, Salakhutdinov (b06, b07): a re-tuned plain recurrent model-free agent matches specialised POMDP methods. Earlier weakness was an implementation effect.

**2022-2025: transformers as belief trackers.** Algorithm Distillation (b17) and Decision-Pretrained Transformer (b16, c06) show in-context RL. DPT acts like posterior sampling. Shai et al. (b18, c07) find a linear encoding of the Bayes belief state in a transformer's residual stream trained on hidden Markov data. These are training-time facts. They do not say a prompted chat model keeps a belief.

**2023-2026: LLMs in the POMDP frame.**
- Reasoning as planning in an MDP: RAP (c01, b14), LLM-MCTS (b12, c02), Tree of Thoughts (b15).
- Belief plus information gain for asking questions: GATE (c10), OPEN (c11), UoT (b21, c12, d01-d03).
- Belief as particles: Tru-POMDP (a23, a24, d14, d15).
- External posterior: Belief-State Engine, BSE (a26, a27, d04-d06).
- Bandit exploration in context: Krishnamurthy et al. (b09, c04), EVOLvE (c05).
- Belief-update quality: Qiu et al. (b10, b11, c09, d07), Imran et al. (a29), BayesBench (a30).
- Verification: Valmeekam (c14), Kambhampati (c13), Stechly (d08-d10).
- History compaction: PABU (a25, d13), Lindenbauer et al. (d11, d12).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Belief is a sufficient statistic; POMDP is an MDP over beliefs; value is piecewise linear convex | 4-state worked example; Tiger 2-step value has 5 linear regions | a01, a02, a04, b01 | [E] |
| Tiger optimal behaviour: listen first, commit when lopsided | Rewards +10 / -100 / -1, accuracy 0.85; random open = -45 vs listen = -1; infinite horizon: commit at 2 net hearings | a03, a04, b01 | [E] |
| Exact POMDP solving is intractable | Finite horizon PSPACE-complete; MDP P-complete; infinite-horizon policy existence undecidable | a09, a10, b23, d18-d20 | [E] (1987 paper and Puterman not opened) |
| Ignoring hidden state loses value | Tag (870 states): QMDP -16.77, PBVI -9.18, Perseus -6.17 | a12, a13 | [E] |
| Sampled-belief planners match full planners at far lower cost | Hallway: Perseus 0.51 reward, 55 vectors, 35 s; PBVI 0.53, 86, 288 s; HSVI 0.52, 1341, 10,836 s. Hallway2: Perseus 0.35 in 10 s; HSVI 0.35 in 10,010 s; PBVI 0.34 in 360 s | a14 | [E] (timings from different machines) |
| Tag: Perseus 280 vectors in 1,670 s vs PBVI 940 vectors in 59,772 s | One PDF table garbled the PBVI time; use ratios only | a13, a12 | [E] ratio only |
| POMCP scales with 1 s per action | RockSample(11,11): POMCP 20.01 +- 0.23 vs SARSOP 21.56 +- 0.11 (SARSOP ~1000 s offline). (7,8): 20.71 vs 21.39. (15,15), 7.37M states: 15.32 vs rollout 7.56 | a16, b03 | [E] |
| POMCP battleship, 10^18 states | Sank all ships >50 moves faster than random, >25 faster than random among preferred actions; tree added little over rollouts | a17, b04 | [S] |
| POMCP numbers were not reproduced | DESPOT authors ran public POMCP code and got poorer scores; both sets printed | a20, d16 | [S] |
| Seed noise makes identical setups look different | TRPO, two 5-seed sets: t = -9.09, p = 0.0016 | b08, d17 | [S] |
| Recurrence helps only when observations are missing | DRQN ~ DQN on 9 Atari games; better on Frostbite, Double Dunk; worse on Beam Rider; flicker p=0.5 | a21, a22, b05 | [E] |
| Tuned plain recurrent RL matches POMDP methods | Better or equal on 18 of 21 environments; beats VRM on 6 of 8 occlusion tasks (not re-checked); worse on Ant-Dir, Humanoid-Dir | b06, b07 | [E] |
| Recurrent RL tuning knobs | Past rewards in input Walker-P 981.6 to 1345.0; TD3 to SAC on Ant-P 310.7 to 2123.5; context 64 to 5 on Walker-V 2.2x; 64 to 400 on Cheetah-Vel 0.292 to 0.415 | b07 | [S] |
| GPT-4 does not explore in bandits with raw history | Basic prompt: suffix failure in >60% of replicates (T=500, N=20). 1 of 32 designs worked (T=100 scan): hint + external summary + CoT + temp 0. BSSC0 median reward 0.47 (TS 0.47, UCB 0.55) | b09, c04, critique 2 | [S] |
| Summary beats raw history in prompting (bandits) | Gemini 1.5 Flash MAB few-shot: 50.2 vs 27.5 win-rate. For fine-tuning raw 65.6 is above summary | c05, c22, critique 3 | [E] for prompting only |
| LLM summary of history does not beat masking on code | SWE-bench Verified, 500 instances: Qwen3-Coder 480B raw 53.4, masking 54.8, summary 53.8; Gemini 2.5 Flash 36.0 vs 35.6; both about -50% cost; summaries +13 to +15% turns | d11, d12 | [S] |
| LLMs update beliefs poorly over rounds | Flight task, 624 simulated users, 5 rounds: Bayesian assistant 81% final, random 37%, LLMs 36-58%, humans ~58%; most plateau after round 1; CoT, numeric formats, 30 rounds did not fix it | b10, c09 (corrected), critique 1 | [E] |
| Bayesian teaching (fine-tuning) fixes much of it and transfers | Bayesian teaching beat oracle teaching for all three small models, p<0.001; ~80% agreement with Bayesian assistant | b10, b11, c09 | [S] |
| Stated belief and action disagree | Untuned LLMs: <50% alignment; external rule on stated belief more accurate than direct choice; Qwen 2.5 exception | b11, d07 | [S] |
| Scale improves direction of belief updates | 6,460 tuples, 5 families; BCC vs log params r = 0.906, p < 1e-6 | a29 | [E] with a30 |
| Scale gain does not reliably reach downstream prediction | 7 open models 3B-70B, 4 environments | a30 | [E] with a29 |
| UoT: belief + information gain for asking | +38.1% average success over direct prompting, 5 datasets x 5 LLMs. This is a RELATIVE gain; Llama3-70B 46.6 rebuilt exactly; absolute +8.7 (closed) / +11.5 (open) points | b21, c12, d01 | [E] |
| UoT at equal tokens | CoT-SC k=33 (4.6k tokens): 20Q 32.6, MD 37.6, TB 42.5. Pruned UoT D=3 (4.7k): 48.1 / 88.4 / 63.2. At ~9k tokens Adapted-ToT D=4 40.9 / 86.7 / 63.7 vs UoT 54.4 / 92.5 / 66.0 | d02 | [S] (n=3, authors' baselines) |
| UoT significance | GPT-4 DP vs UoT: Common 49.0 vs 70.9, Thing 30.8 vs 36.8 (p=0.036, weakest), DX 89.4 vs 97.0, MedDG 74.9 vs 87.9, FloDial 42.5 vs 67.8 | d03 | [S] |
| UoT vs other methods | Beats CoT-SC by 33.8, Reflexion 29.9, Original-ToT 28.3, Adapted-ToT 12.4 (unit not stated per method) | b21, c12 | [S] |
| Sound verifier beats self-critique | Blocksworld (100 inst.): GPT-4 40%, LLM+LLM 55%, LLM+VAL 88%; LLM verifier right on 61/100 | c14 | [E] |
| Weak verifier is harmful | Game of 24: standard 5%, LLM+LLM 3%, sound 36%. Graph colouring 16 / 2 / 38. Mystery BW 4 / 0 / 10. Mystery BW verifier FNR 97.09% (100/103); graph colouring FNR 95.8% | d08, d09 | [E] |
| A 99%-accurate CoT verifier still trails | Game of 24 verifier 87% to 99% with CoT; 6-point gap to sound verifier remains at 17x output tokens | d10 | [S] |
| LLM as world model in MCTS beats LLM as policy | VirtualHome seen: Simple 91.4 vs 83.4 (fine-tuned GPT2 81.3); Compositional 71.2 vs 47.0 (GPT2 59.0). Unseen: Simple 82.9 vs 74.3; Comp 71.9 vs 43.3. UCT alone 0.0. NovelComp3 33.6 vs 5.4 | b12, c02 | [E] |
| RAP: reasoning as MDP | Blocksworld LLaMA-33B: RAP(20) 1.00 / 0.88 / 0.42 on 2/4/6 steps, average 64%; beats GPT-4 CoT by 33% relative. GSM8k: CoT 29.4, CoT+SC(10) 46.8, RAP(1) 48.6, RAP(10) 51.6. ProntoQA proof accuracy 78.8 vs 64.8 | c01, b14 | [E] with b12 |
| Tree of Thoughts | Game of 24 GPT-4: CoT 4% vs ToT 74% | b15 | [S] |
| Search needs a foothold | Mystery BW stays ~10% even with a verifier (one-shot GPT-4o 28.3, Claude-3-Opus 48.2, Gemini Pro 11.3); Blocksworld 82%, Logistics 70% with VAL, up to 15 rounds; autonomous GPT-4 ~12% executable | c13, c25 | [E] |
| Tru-POMDP | 300 tasks, 5 kitchens, GPT-4.1, step limits 25/30/35; ReAct, Reflexion <20% with 3+ unknown targets; prompt-augmented ~40%; LLM-MCTS timed out (>600 s) on all tasks. Flat hypothesis list worse than single hypothesis | a23, a24, d14, d15 | [S] |
| BSE on Tiger | gpt-4o, N=40, T=20: BSE 38/40 (95%), 1.45 listens, return 3.06 [-4.41, 8.24]; Reactive and NL-Tracker 32/40 (80%), return -12.00 [-25.75, 1.75], 0 listens; 2.45x LLM calls. Intervals overlap | a26, d04 | [C] |
| BSE attack graph | 64 states, N=40, T=30: Reactive -5.40, BSE -2.80, NL-Tracker 7.87; coverage 42.1% vs 32.5%; not significant | a27, d06 | [C] |
| BSE ablation | No observation update: belief stays at ln 2, 23/25 episodes time out listening (return -16.08) | a27, d05 | [S] |
| Models state the structure and fail to use it | CogEval GPT-4: 0/30 on shortest path one cluster away; never >10% at temp 0.5 or 1. BALROG NetHack best 1.5%; BALROG average Claude 3.5 Sonnet 32.64, GPT-4o 32.34, Llama 3.1 70B 27.88; images lowered GPT-4o to 22.56. RAGEN Echo Trap in 3 of 4 environments | b22, c15, c16, c26 | [E] |
| Belief compaction by training | PABU: 81.0% completion, 9.5 steps, +23.9% relative success, -26.9% steps; GPT-4-turbo 55.9% / 14.2 steps; ATLAS 65.4; AgentEvol 60.8 | a25, d13 | [S] (fine-tuned) |
| Hidden-Markov belief geometry in transformers | Mess3 R2 = 0.95; RRXOR vs next-token geometry R2 = 0.31 | b18, c07 | [E] with DPT; not prompt-time |
| Othello-GPT | Illegal-move error 0.01% vs 93.29% untrained; nonlinear probe 1.7% error (synthetic) | c08 | [S]; fully observed board |
| InfoSeeker | 11 tasks, 100 steps; mix-color 84% (+8); miscalibrated arm 80% while best baseline fell from 100% to 6% | a28 | [S] (under review) |
| Belief State Transformer | Story writing: judge prefers BST 64%, CI [54%, 74%] | b19, b20 | [S] |
| GATE and OPEN | GATE: elicitation more informative than user-written prompts, significant in all domain comparisons but one. OPEN beat LM-only and BOED-only; no numeric TIDA read | c10, c11 | [S] |

## 4. Mechanisms and models

### 4.1 The MDP loop (what to compute)

An MDP is (S, A, T, R, gamma). Bellman equation: V(s) = max_a [ R(s,a) + gamma * sum_s' T(s'|s,a) V(s') ]. Value iteration: repeat the update until the largest change is below epsilon. Stop rule from a07: greedy policy is within 2*epsilon*gamma/(1-gamma) of optimal. Cost per iteration is quadratic in states and linear in actions.

How the schema maps: states S0-S9 are the controller's own MDP. Code decides every transition. Rewards are code-checked (test passed, check passed). No model-judged reward. This matches G2 and G5. RAP's model-judged reward lost accuracy with more iterations (c01 limits), which is the failure we avoid.

### 4.2 The belief update (about 15 lines of code)

State: hypotheses h_1..h_n with weights b(h), sum 1.
For action a, observation o:
- Predict (only if the world can change): b'(h') = sum_h T(h'|h,a) b(h).
- Update: b''(h') = O(o|h',a) * b'(h') / Z, where Z normalises.

In a reasoning task the world is static (the answer does not change), so the predict step is the identity. BSE found dropping the prediction step changed little (a27). Dropping the observation update broke everything: belief stayed at ln 2, 23/25 episodes timed out listening (a27, d05).

Where do likelihoods O(o|h,a) come from? Three options, in increasing risk:
1. Hard check: the test either passes or fails for h. O is 0 or 1 (or a small epsilon for noisy tests). Code-computed. Safe.
2. Fixed table by test type (for example a noisy probe with 0.85 accuracy), set from our own calibration data.
3. Model-elicited likelihoods. Weak. Qiu shows LLM updating is poor, and stated beliefs do not match actions (b10, d07).

Rule from the evidence: use 1 or 2 where possible; code does the normalising (G5).

### 4.3 Commit rule from Tiger

The optimal infinite-horizon Tiger rule is a threshold on net evidence: commit at 2 net hearings. With listen accuracy p, the log-odds per hearing is ln(p/(1-p)); at 0.85 that is about 1.73. After k net hearings the posterior is p^k / (p^k + (1-p)^k). Two net hearings give about 0.97. The threshold comes from the payoff ratio: -100 for wrong vs +10 for right vs -1 per listen. In general, commit when the expected loss of acting now (posterior of the worst case times its cost) is less than the cost of one more look. This is the value-of-information gate. The agent can compute it in code if each test has a known cost and a known diagnosticity. (The 1.73 and 0.97 figures are our arithmetic from the stated accuracy, not numbers from the paper.)

With budget left, the optimum at short horizons is to gather first (a04: t=2 and t=3 from the uniform belief only listen). Do not commit early when the belief is flat and looks are cheap.

Caveat: BSE saw the model listen 1.45 times with no stated threshold (d04), so a stated rule may add little. No rule-vs-no-rule arm exists (critique gap 2).

### 4.4 Point-based planning: plan on few beliefs

PBVI, Perseus, SARSOP: keep a small set B of belief points. For each, keep one alpha-vector (a linear function). Back up only at those points. Perseus: pick random beliefs from B, back up, and keep the new vector if it raises value at that belief; otherwise keep the old best. Repeat until every belief in B is improved. Result: 280 vectors versus 940 on Tag, with better reward (-6.17 vs -9.18).

Agent analogue: do not enumerate all hypotheses. Keep K sampled hypotheses and update only those.

### 4.5 Particle belief and tree search (POMCP, DESPOT)

POMCP: belief is K particles (sampled hidden states). For each simulation: sample a particle, run the simulator down a tree keyed by action-observation history, use UCT to pick actions, and a rollout at the leaf. After the real action and observation, keep the subtree and keep only particles that match the observation. Reinvigorate particles when too few remain. Discount 0.95 in RockSample and PocMan.

DESPOT: build the tree from K fixed sampled scenarios; penalise policy size to avoid overfitting to the K scenarios. Regularisation did not help on RockSample, which is nearly deterministic (a19).

Agent analogue (Tru-POMDP): the LLM proposes hypotheses as particles; code does Bayesian filtering; search runs over the belief tree. The structure that worked: 3 candidates per level, two levels (C1=C2=3), a tree rather than a flat list (d14). A flat one-shot list was worse than one best guess. No K sweep exists.

### 4.6 Belief-state engine (external posterior)

BSE: code holds the posterior. The LLM sees only the posterior, not the log, and chooses an action. Cost: 2.45 LLM calls per episode vs 1.00 (d04). Result on Tiger: 38/40 vs 32/40. Evidence is weak (intervals overlap). Missing arms: free-text posterior (AB6), RockSample, larger N.

### 4.7 Sufficient statistics for exploration (bandits)

State is per-arm counts and means. Code maintains it. The prompt shows the summary, a hint to explore, chain of thought and temperature 0. This was the single working design of 32 (b09). Summary beats raw history for prompting (50.2 vs 27.5), reverses for fine-tuning (65.6 raw; c05, critique 3). Not shown to help beyond bandits: on SWE-bench masking equals summary (d11).

### 4.8 Expected-information-gain question selection (UoT, OPEN)

Keep a set of possible hypotheses H with weights. For each candidate question q, simulate answer branches, compute the information gain (entropy of H before minus expected entropy after), propagate reward back through a depth-3 tree, pick the best q. Prune. UoT limited depth to three for cost. The answerer was GPT-4 simulating the environment. The prior was uniform. Implementation needs the set H given; real tasks need H generated first (see Tru-POMDP structure).

### 4.9 Verifier-in-the-loop (LLM-Modulo)

Generate with the model; verify with a sound external check; back-prompt with the failing output; repeat up to R rounds. Feedback detail on Blocksworld (n=50): binary only 74%, plus first error 86%, plus all errors 86% (c14). Cap the rounds (the sound runs used up to 15 rounds, so compute was not matched, d09).

### 4.10 Recurrent memory as learned belief

DRQN and Ni et al.: a recurrent policy trained end to end. Needed: past rewards and actions in the input; algorithm choice and context length tuned per task; LSTM vs GRU no general difference (b07). Not available to a no-training scaffold. The lesson that transfers: inputs must let the agent infer the hidden state (past actions and rewards must be visible).

## 5. What holds up

**Holds up (replicated or multi-source).**
- Belief sufficiency and the convex value function (theory, textbook-level).
- Treating hidden state as observed loses value (Tag: QMDP -16.8 vs -6 to -9; also perceptual aliasing in a08).
- Sampled-belief planners reach near-equal quality at a fraction of cost (PBVI, Perseus, SARSOP, POMCP, DESPOT; several independent groups).
- Recurrence helps only where observations go missing (Hausknecht and Stone; Ni et al. agree after tuning).
- Models can write the structure but not act on it (CogEval, BALROG, RAGEN).
- A sound verifier beats self-critique (Valmeekam; Stechly; Kambhampati).
- LLM as world model inside search beats LLM as policy alone, with UCT alone at 0.0 (LLM-MCTS; RAP; Tru-POMDP).
- LLMs update beliefs poorly over rounds (Qiu; Imran; BayesBench agree on direction).

**Failures and contradictions.**
- POMCP reproduction failure (a20, d16). Scores depend on code and machine.
- Seed variance: t = -9.09 for the same configuration (b08).
- Recurrent RL: Hausknecht and Stone found mixed results; Ni et al. found it strong once tuned. The difference is tuning, not nature (critique).
- Qiu: line c09 said 68%; corrected to 81% (critique 1).
- Summary vs raw history: helps prompting on bandits, hurts fine-tuning (EVOLvE), and does not beat masking on SWE-bench (d11).
- BSE: belief helps on Tiger (weakly), no effect on the larger task; NL-Tracker acted like no belief (d05, d06).
- UoT 38.1% was easy to misread as absolute; it is relative (d01).
- Tru-POMDP flat hypothesis list was worse than one guess (d14).

**Moderators.**
- Task type: fully observed tasks gain nothing from belief or memory (a21, b05). Hidden-state or missing-observation tasks gain.
- Foothold: search lifts results only when the model proposes plausible actions (Mystery BW ~10% even with verifier; c13).
- Verifier quality: a verifier with FNR 97% is worse than none (d08, d09).
- Compute: RAP, LLM-MCTS and Tru-POMDP baselines use very different budgets (LLM-MCTS timed out on all Tru-POMDP tasks). No cross-method equal-token comparison exists; only UoT Table 2 does one, against authors' own baselines.
- Prompt vs fine-tune: Bayesian teaching, PABU and DPT need training. Prompt-only repair of belief updating gave no meaningful improvement in Qiu's follow-ups (c09).

**Interventions that worked.**
- External summary into sufficient statistics (bandits, prompting).
- External sound verifier with back-prompting (Blocksworld 40 to 88).
- Belief plus information-gain lookahead for question asking (equal-token check passed in UoT Table 2).
- Deriving the action from the stated belief with an external rule (Qiu appendix; one task).
- Structured hypothesis tree with Bayesian filtering (Tru-POMDP; single source).
- Observation masking for long agent runs (-50% cost, equal solve rate).

**Interventions that did not work.**
- Chain of thought, numeric formats, 30 rounds and base models for belief updating (Qiu).
- Natural-language belief tracker (acted like no belief; BSE).
- LLM self-verification on Mystery Blocksworld and graph colouring.
- LLM summaries of history on code tasks (+13 to +15% turns, no gain).
- Images on BALROG (GPT-4o fell from 32.34 to 22.56).
- Self-evaluation as MCTS reward with more iterations (RAP ablation).

## 6. Language models

**As exploration agents.** GPT-4 with a basic bandit prompt shows suffix failure (never pulls the best arm in the second half) in over 60% of replicates at T=500, N=20. The T=100 scan of 32 designs found one that works: suggestive hint, externally summarised history, zero-shot chain of thought, temperature 0 (BSSC0: suffix-failure frequency 0.00, median reward 0.47 vs Thompson 0.47, UCB 0.55). Three GPT-4 configs showed no suffix failure but two of them chose near-uniformly (critique 2). GPT-3.5 and Llama2 failed in all configs. EVOLvE: summarised history 50.2% vs raw 27.5% on Gemini 1.5 Flash few-shot. Small models trained on UCB traces beat larger ones on several tasks (c05).

**As belief updaters.** Off-the-shelf LLMs reach 36-58% final-round accuracy against 81% for the Bayesian assistant (random 37%) on a 5-round flight task with 624 simulated users. Humans: about 58%, improved significantly (p=0.002, 48 users). Most models plateau after round 1. Chain of thought and numeric formats did not help. Fine-tuning on the Bayesian assistant's guesses beat fine-tuning on oracle answers (p<0.001 for all three small models) and transferred to hotels and web shopping. Verbalised beliefs and direct choices agree under 50% in untuned models. An external rule on the stated belief beat the direct choice. Scale helps direction: BCC correlates with log parameters at r = 0.906 across 6,460 tuples. But BayesBench (7 open models 3B-70B) finds the gain does not reliably reach downstream prediction.

**As planners.**
- Autonomous GPT-4 plans reach the goal in about 12% of PlanBench cases. GPT-3 got 1% where humans got 78% (second-hand, c19, not opened).
- Mystery Blocksworld one-shot: GPT-4o 28.3, Claude-3-Opus 48.2, Gemini Pro 11.3.
- With a sound verifier and back-prompting (up to 15 rounds): Blocksworld 82-88%, Logistics 70%, Mystery BW ~10%.
- CogEval: 0/30 for GPT-4 on shortest path in an unseen graph. It lists the edges correctly and cannot use them.
- BALROG: best NetHack progress 1.5% (o1-preview).

**With search over states.**
- RAP with a 33B model: 64% average on Blocksworld versus near-total CoT failure; 42% on 6-step problems.
- LLM-MCTS with GPT-3.5: compositional seen 71.2 vs 47.0 policy-only; UCT alone 0.0.
- ToT on Game of 24: 4% to 74%.
- All of these use many more calls than one chain. Costs were not matched in the sources read.

**With explicit belief.**
- UoT: +38.1% relative average; absolute +8.7 to +11.5 points for Llama3-70B. At matched tokens (~4.6k) GPT-4 UoT 48.1 / 88.4 / 63.2 vs CoT-SC k=33 32.6 / 37.6 / 42.5. n=3 runs.
- BSE on Tiger: 95% vs 80%, CI overlap, 2.45x calls.
- Tru-POMDP: beats ReAct and Reflexion, uses the fewest LLM tokens among planners compared, no equal-token test against one long chain.
- InfoSeeker: large gains when dynamics are perturbed (80% vs a baseline falling from 100% to 6%), small in the basic setting.

**With compaction.**
- PABU (fine-tuned, 1B and 8B Llama): 81.0% completion, 26.9% fewer steps.
- Zero-shot, SWE-bench: masking 54.8 vs summary 53.8 vs raw 53.4 (Qwen3-Coder 480B). Observation tokens are about 84% of a turn. Summary generation costs up to 7.2% of the total.

**Inside the model.** Transformers trained on hidden-Markov data encode the Bayes belief state linearly (R2 = 0.95 on Mess3). DPT behaves as posterior sampling. This shows belief tracking can emerge in weights. It does not show that a prompted chat model tracks a belief in context.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Carry a structured hypothesis table (hypothesis, weight, last evidence) as working state instead of the raw transcript, in tasks with hidden state. Code owns the weights and normalising. The theory is established; the benefit over a transcript at equal tokens is untested, so run T1/T3 as a check. | S2/S4 state, memory | [E] theory only | K01; a01, a02, b01 |
| Never treat a surface cue as the state when states alias. Keep competing hypotheses distinct until a test separates them. | G (state tracking) | [E] | K06; a08, a12, a13 |
| A sound external check beats the model's self-check. Where no sound check exists, do not use a self-verifier with a high false-negative rate as a gate. | G2/G3/S8 | [E] | K14; c14, c13, d08, d09 |
| Search over states only where the model proposes plausible actions; gate search by a first-pass success rate. | G12, S6 operators | [E] | K15, K16; b12, c02, c13, c25 |
| Bound the budget. Exact belief planning is intractable. Plan on a few sampled hypotheses. | G7/G12 | [E] | K02, K04; a05, a13, a14, d18-d20 |
| Code holds sufficient statistics (counts, means) for repeated-choice sub-tasks and shows them in the prompt. | memory | [E] for prompting on bandits only | K10; b09, c05, c22 |
| Use at least 3 sampling seeds and N>=200 per arm for any arm comparison. Gaps of a few points at N=20-40 cannot be resolved. | measurement (G7) | [E] | K27, K08; b08, d16, d17, d03, d05 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Code-held posterior over hypotheses shown to the model, vs free-text belief, at equal tokens | S4/S7 state | [C] | K17, K23; a26, d04, d05 |
| Stated commit rule (act when top posterior >= threshold or net evidence >= 2) vs no rule | G1/S0 stop rule | [S] | K03, K17; a03, a04, b01, d04 |
| Ask for the posterior table first, then pick the action by a fixed rule in code | O (commit) | [S] | K24; d07 |
| Expected-information-gain test selection over the hypothesis table (UoT style, depth up to 3) | O (ask/probe) | [S] on equal tokens (established on question tasks vs weaker baselines) | K13; b21, c12, d01, d02 |
| Hypothesis generation as a tree (3 per level, 2 levels) vs flat list; K sweep 1, 3, 9 | S3 generate | [S] | K18, K25; a23, a24, d14 |
| Particle-style search over K sampled hypotheses vs one long chain at equal tokens | O search | [S] | K04, K18; a15, a19, d15 |
| Masking vs LLM summary vs structured table for history on a debugging task. Default to masking, not summary, until shown otherwise. | memory | [S] | K21, K26; d11, d12, d13 |
| Force the action to follow the stated belief | G10 link | [S] | K20, K24; b22, c26, d07 |

## 8. Concrete tests on our bench

All arms get the same token budget, set by the most expensive arm and counted with setup cost (G7). Use N>=200 items per arm and 3 sampling seeds. Paired tests per item. Report the 95% interval, not only the mean.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Tiger and RockSample-small in text form, exact optimal policy known; 200 episodes each | (a) plain LLM, (b) LLM + free-text belief, (c) LLM + code-computed posterior table | Mean return vs optimal; success; listens before commit | (c) beats (a) and (b); (b) ~ (a) as in BSE |
| T2 | Same as T1 | Posterior table with no rule, with stated threshold (net evidence 2), with code-forced commit | Return; premature commits; extra listens | A rule or forced commit lowers premature commits; gain over no rule small |
| T3 | Diagnosis or fault-finding with 5-20 candidate hypotheses and noisy tests | (a) CoT-SC, (b) hypothesis table + EIG test choice, (c) hypothesis table + random test choice | Correct diagnosis rate; tests used | (b) > (c) > (a); (b)-(c) isolates the information-gain part |
| T4 | Same as T3 | Flat list of 9 vs tree 3x3 vs single best guess; K = 1, 3, 9 | Correct rate | Tree > single > flat (Tru-POMDP); find the K where gain stops |
| T5 | Multi-round hidden-preference task (Qiu style, prompts only) | Free-text belief vs numeric posterior in code vs action derived by code from stated posterior | Final-round accuracy; belief-action agreement | Code-derived action beats direct action; closes part of the 81% vs 36-58% gap |
| T6 | Long debugging runs (>=30 turns) | Raw transcript, masking old observations, LLM summary, structured table (hypotheses, tried fixes, failing output) | Solve rate; turns; cost | Masking ~ summary on solve rate; table lowers turns if failure signals stay visible |
| T7 | Repeated-choice sub-tasks (which tool, which hint to try) | Raw history vs code-held counts and means | Regret; suffix failure rate | Summary lowers suffix failure (prompting) |
| T8 | Tasks with a sound check vs tasks with only a model judge | Self-check gate vs code check gate vs no gate | Accuracy; false-reject rate | Self-check with FNR above 20% loses to no gate |
| T9 | Hard planning items (Blocksworld style) in 3 difficulty bands | One long chain vs search over K sampled thoughts with code check | Success by band | Search wins only in the band where plain success is above a foothold (about 10-20%) |
| T10 | Any of the above | Seed audit: same arm run on 2 sets of seeds | Between-set difference | Quantifies implementation and sampling variance (critique gap 9) |

## 9. What does not transfer, and why

- **Known model.** Classic POMDP theory assumes known T and O. Our agent has no such model. Likelihoods must come from checks or tables. Model-elicited likelihoods are weak.
- **Exact solving.** PSPACE-complete and undecidable results mean no optimal policy in general. Only a bounded approximation transfers.
- **Reward and discounting.** Our tasks have a single terminal reward. Discount 0.95 and per-step rewards from RockSample do not map. The horizon is the token budget.
- **Learned belief in weights.** DPT, Algorithm Distillation, PABU, Bayesian teaching and Belief State Transformer need training. The agent is a scaffold with no training. Qiu found prompt-only repair gave no meaningful improvement.
- **Bandit results.** Bandits have no transitions. The summary trick tests only the update half of POMDP control. In a real task the belief is large; the summary design is unsolved (c22).
- **Fine-tune vs prompt split.** Raw history was better for fine-tuning (65.6) but worse for prompting (27.5). Do not carry fine-tuning results over.
- **Simulation settings.** VirtualHome, RoboCasa kitchens, Atari and MuJoCo are far from text reasoning. Continuous control results (Ni et al.) say nothing about language.
- **Planner timings.** Machines differ; only ratios are usable.
- **Model-judged reward.** RAP's self-evaluation reward degrades. Our G5 forbids it.
- **Toy transfer.** Tiger has 2 states. It shows the shape of the gather-then-commit rule, not its size in open tasks.
- **Verbalised belief as a window into the model.** Stated beliefs do not match actions (under 50% alignment), so reading a model's belief from its words is unreliable (G10).

## 10. Open questions

1. Does a code posterior beat a free-text belief at equal tokens on Tiger and RockSample-small at N>=200? (BSE skipped AB6 and RockSample.)
2. What commit threshold suits an LLM agent, and does a stated rule change behaviour?
3. At equal tokens, does particle-style search over K hypotheses beat one long chain? What K is best?
4. Where does summary-over-raw-history stop helping outside bandits and code? Diagnosis is untested.
5. Does belief compaction help zero-shot agents, or only trained ones? PABU had no prompt-only arm.
6. How to build a sound verifier for open-ended tasks.
7. How big is implementation variance between LLM planners? No quantitative measure exists.
8. Does forcing the action from the stated belief help beyond the flight task and beyond Qwen 2.5's exception?
9. Does UoT's equal-token advantage survive more than 3 runs and a neutral implementation?
10. Puterman and the 1987 complexity paper were never opened. The classes come from restatements.
11. Do the BSE results hold for models other than gpt-4o, and for the 64-state task with a stronger setup?
12. Does the Tru-POMDP structure (tree of 3x3) carry over from embodied scenes to text diagnosis?

## 11. Sources

[V] opened this session; [M] snippet or memory only. Where only an abstract or a restatement was read, it is noted.

- [V] Kaelbling, Littman, Cassandra (1998) Planning and acting in partially observable stochastic domains. https://people.csail.mit.edu/lpk/papers/aij98-pomdp.pdf (a01-a06, b01, b02). Journal DOI [M]: https://doi.org/10.1016/S0004-3702(98)00023-X (c17).
- [V] Kaelbling, Littman, Moore (1996) Reinforcement learning: a survey. https://arxiv.org/pdf/cs/9605103 (a07, a08).
- [V, abstract only] Madani, Hanks, Condon (1999/2003) On the undecidability of probabilistic planning and infinite-horizon POMDPs. https://mlanthology.org/aaai/1999/madani1999aaai-undecidability (d19; a09 was a snippet). Journal: https://doi.org/10.1016/S0004-3702(02)00378-8 [M] (b24).
- [M] Papadimitriou, Tsitsiklis (1987) The complexity of Markov decision processes. https://pubsonline.informs.org/doi/10.1287/moor.12.3.441 (a10, b23).
- [V] Bernstein, Givan, Immerman, Zilberstein (2002), restating the 1987 result. https://people.cs.umass.edu/~immerman/pub/bgiz.pdf (d18).
- [V] Chatterjee, Chmelik, Tracol (2013/2016) What is decidable about POMDPs with omega-regular objectives. https://arxiv.org/pdf/1309.2802 (d20).
- [M] Puterman (1994) Markov Decision Processes. https://doi.org/10.1002/9780470316887 (b25).
- [V] Pineau, Gordon, Thrun (2003) Point-based value iteration. https://www.ri.cmu.edu/pub_files/pub4/pineau_joelle_2003_3/pineau_joelle_2003_3.pdf (a11, a12).
- [V] Spaan, Vlassis (2005) Perseus. https://arxiv.org/pdf/1109.2145 (a13, a14).
- [V] Silver, Veness (2010) POMCP. https://papers.nips.cc/paper_files/paper/2010/file/edfbe1afcf9246bb0d40eb4d8027d90f-Paper.pdf (a15-a17, b03, b04).
- [V] Kurniawati, Hsu, Lee (2008) SARSOP. https://www.roboticsproceedings.org/rss04/p9.pdf (a18).
- [V] Somani, Ye, Hsu, Lee (2013) DESPOT. https://papers.nips.cc/paper_files/paper/2013/file/c2aee86157b4a40b78132f1e71a9e6f1-Paper.pdf (a19, a20, d16; b26 was [M]).
- [V] Hausknecht, Stone (2015) Deep recurrent Q-learning for POMDPs. https://arxiv.org/pdf/1507.06527 (a21, a22, b05).
- [V] Ni, Eysenbach, Salakhutdinov (2022) Recurrent model-free RL can be a strong baseline for many POMDPs. https://arxiv.org/abs/2110.05038 (b06, b07).
- [V] Henderson et al. (2018) Deep reinforcement learning that matters. https://arxiv.org/abs/1709.06560 (b08, d17).
- [V] Tang et al. (2026) Tru-POMDP. https://arxiv.org/pdf/2506.02860 (a23, a24, d14, d15).
- [V] Jiang, Ge, Cai, Song (2026) PABU. https://arxiv.org/pdf/2602.09138 (a25, d13).
- [V] Chattopadhayay, Halder (2026) Belief-State Engine. https://arxiv.org/pdf/2609.10036 (a26, a27, d04-d06).
- [V] Fang, Ke (2025) InfoSeeker. https://arxiv.org/pdf/2510.01531 (a28).
- [V] Imran et al. (2025) Are LLM belief updates consistent with Bayes' theorem? https://arxiv.org/pdf/2507.17951 (a29).
- [V] Samanta et al. (2026) BayesBench. https://arxiv.org/pdf/2606.30850 (a30).
- [M] AAAI-26, LLM as belief module (snippet only, details unverified). https://ojs.aaai.org/index.php/AAAI/article/view/39465/43426 (a31).
- [V] Krishnamurthy et al. (2024) Can large language models explore in-context? https://arxiv.org/abs/2403.15371 (b09, c04).
- [V] Nie et al. (2024) EVOLvE. https://arxiv.org/abs/2410.06238 (c05).
- [V] Qiu et al. (2025) Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523 (b10, b11, c09, d07).
- [V] Zhao, Lee, Hsu (2023) LLM-MCTS. https://arxiv.org/abs/2305.14078 (b12, b13, c02).
- [V] Hao et al. (2023) RAP. https://arxiv.org/abs/2305.14992 (b14, c01).
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (b15; c20 listed it as [M]).
- [V] Lee et al. (2023) Decision-Pretrained Transformer. https://arxiv.org/abs/2306.14892 (b16, c06).
- [V] Laskin et al. (2022) Algorithm Distillation. https://arxiv.org/abs/2210.14215 (b17; numbers not extracted).
- [V] Shai et al. (2024) Transformers represent belief state geometry. https://arxiv.org/abs/2405.15943 (b18, c07).
- [V] Hu et al. (2025) The Belief State Transformer. https://arxiv.org/abs/2410.23506 (b19, b20).
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/pdf/2402.03271 (b21, c12, d01-d03).
- [V] Momennejad et al. (2023) CogEval. https://arxiv.org/abs/2309.15129 (b22).
- [V] Li et al. (2023) Emergent world representations (Othello-GPT). https://arxiv.org/abs/2210.13382 (c08).
- [V] Li, Tamkin, Goodman, Andreas (2023) GATE. https://arxiv.org/abs/2310.11589 (c10).
- [V] Handa et al. (2024) OPEN. https://arxiv.org/abs/2403.05534 (c11).
- [V] Kambhampati et al. (2024) LLM-Modulo. https://arxiv.org/abs/2402.01817 (c13).
- [V] Valmeekam, Marquez, Kambhampati (2023) Self-critiquing plans. https://arxiv.org/abs/2310.08118 (c14).
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/pdf/2402.08115 (d08-d10).
- [V] Paglieri et al. (2025) BALROG. https://arxiv.org/abs/2411.13543 (c15).
- [V] Wang et al. (2025) RAGEN. https://arxiv.org/abs/2504.20073 (c16).
- [V] Lindenbauer et al. (2025) The Complexity Trap. https://arxiv.org/pdf/2508.21433 (d11, d12).
- [M] Feng et al. (2023) TS-LLM. https://arxiv.org/abs/2309.17179 (c03, title only).
- [M] Valmeekam et al. (2022) PlanBench. https://arxiv.org/abs/2206.10498 (c18).
- [M] Valmeekam et al. (2023) On the planning abilities of LLMs. https://arxiv.org/abs/2302.06706 (c19, second-hand).
- [M] Chen et al. (2021) Decision Transformer. https://arxiv.org/abs/2106.01345 (c21).
