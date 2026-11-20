# Knowledge-based intrinsic motivation: deep document

Subfield C07.04 of reinforcement-learning exploration. Focus: reward prediction error and learning progress as internal rewards. Key works: Oudeyer and Kaplan 2007/2009; Kaplan and Oudeyer 2004; Schmidhuber 1991 and 2010.
Evidence ids (a01..a25, b01..b25, c01..c25, d01..d16) refer to evidence_a-d.jsonl in this folder. Claim ids K01..K20 refer to claims.jsonl. Weak spots are listed in critique.md.
Priority for the agent: Low (background). The field needs a world model. A prompt-only agent can use it only through an explicit predictor.

## 1. What it is

Intrinsic motivation means doing something for its own sake, not for an outside reward (a01). Oudeyer and Kaplan split computational models into three families: knowledge-based, competence-based and morphological (a01).

Knowledge-based models reward the gap between what the agent expected and what happened. There are two branches (a01, c18):
- Information-theoretic: reward from changes in a distribution (information gain, KL divergence, counts).
- Predictive: reward from the error of a predictor.

Several rewards sit on the same error signal (a02, a03):
- Novelty / prediction error: r = C * Er (Eq 9). High error is rewarded.
- Intermediate novelty: a Gaussian bump around a target error (Eq 10). The target is set by hand.
- Surprise: actual error divided by predicted error (Eq 15).
- Familiarity: r = C / Er (Eq 16).
- Learning progress (LP): the drop in error over time inside a region (Eq 11). r = mean error over the older window minus mean error over the recent window.

The core problem is the "noisy TV". Noise can never be predicted, so raw error rewards the agent forever for staring at it (a02, a16, b04). LP is the designed fix. Noise gives no drop in error. Mastered regions give no drop either. Only learnable regions pay (a03, a08).

What this means for us. Our agent is a prompt scaffold, not a trained policy. It has no weights to update and no world model unless it writes one. So the field matters as a source of selection rules: which subproblem to work on next, when to stop, which self-proposed goal to trust. It does not give us a trainable reward. Very little of it has been tested in a prompt-only agent (c24, d16).

## 2. History and theories in depth

**1991, Schmidhuber.** Adaptive curiosity for model-building controllers. Two versions (d06, a08):
- First: reward proportional to the predictor's error. It drives the agent to high-error places and fails under noise.
- Second: a model of the predictor's improvement (change in mean squared error) gives the reward. Noisy targets give no net improvement, so they bore the agent.
The 2010 review gives no numbers for these systems. It says experiments "showed advantages over random exploration" (d06). The 1991 paper itself was not opened (a11).

**1995.** Reward is the KL distance between predictor beliefs before and after an observation. This is information gain (d06, a08).

**1997-2002.** Zero-sum games between two modules that bet on experiment outcomes (a08).

**2004, Kaplan and Oudeyer.** "Maximizing learning progress: an internal reward system for development". The first LP robot implementation. Reward is the decrease of prediction error over a short window. The paper was not fetched here (a10, b23, d04). Its journal form is Oudeyer, Kaplan and Hafner 2007.

**2007, Oudeyer, Kaplan and Hafner.** Intelligent Adaptive Curiosity (IAC). The robot splits its sensorimotor space into regions. Each region has an expert predictor and a list of recent errors. Reward is the drop in smoothed error. Regions split when the exemplar count passes a threshold, choosing the cut that minimises summed variance. Prediction with 3,000,000 exemplars takes about 17 scalar comparisons (a05).
Experiments:
- Webots simulation, 5,000 steps, three zones (noise, easy, harder). After about 250 steps the robot focuses on the easy zone. At about 3,000 actions it moves to the harder zone and spends 85% of its time there. The noise zone is avoided. Random action puts 33% of examples in the easy zone. IAC error plateaus near 0.09 and sits below random. A "MAX" control (pick highest error) is built in (a06, d04).
- Sony AIBO on a play mat with a bitable and a bashable object. Phases appear in order: random, looking, biting, bashing, then affordant use (a07).
- 200 simulated runs: the structured trajectory appears in 34%. 100% reach repeated biting. 78% reach repeated bashing. Focused bite comes before focused bash in most runs (d05).

**2007, Oudeyer and Kaplan.** Typology paper. Rates models by exploration potential, organisation potential, cost and number of implementations. They rate LP (LPM), information-gain (IGM) and competence-progress (CPM) models as most promising. These are rough author ratings (a01, a04).

**2010, Schmidhuber.** Formal theory of creativity. Reward is the first derivative of compression quality. He claims IAC is a one-step special case of his 1991 system. He also argues free-energy agents prefer predictable states and would sit in a dark room (a08, a09). This is a priority dispute told from one side. The two mechanisms are not identical (a09 limits).

**2012 to 2013.** Lopes and Oudeyer and Baranes and Oudeyer extend LP to goal selection (SAGG-RIAC) (b24, not opened).

**2012 and 2020, human work.** Kidd and colleagues, then Poli and colleagues, test whether infants look away by a Goldilocks rule or by LP (section 3, d01, d02).

**2016, count and information gain.** Bellemare et al. turn a density model into a pseudo-count. Prediction gain (log density after an update minus before) approximates information gain and is a form of compression progress (a12, a25). Their Montezuma figure (2461 then 3439) was not rechecked (critique.md).

**2017, deep RL curiosity.** Four lines:
- ICM (Pathak): forward-model error in a feature space learned by an inverse model (a14).
- Surprisal and k-step LP (Achiam and Sastry): surprisal worked in all nine domains. LP worked on two and faltered elsewhere (a13).
- Teacher-Student Curriculum Learning (Matiisen): pick subtasks by the absolute slope of the learning curve (c13).
- Go-Explore: return to remembered states (b21, not opened).

**2018 to 2019, fixing noise.**
- Large-scale curiosity study across 54 environments (a15).
- RND: error against a fixed random network (a17).
- ECO: reachability from episodic memory (a18).
- Disagreement, MAX, Plan2Explore: ensemble variance (b08, a19, a20).
- CURIOUS: LP over goal modules (a21).
- ALP-GMM: LP teacher over task parameters (b10).

**2022 to 2026, hindsight and LP again.**
- Curiosity in Hindsight (b09).
- Curious Replay (c17).
- LPM (Hou 2025/2026): LP reward in one code base against six baselines (d07, d08).
- Gradient-Momentum Coupling: a parameter-space proxy for LP (d09).

**2023 to 2026, language models.**
- ELLM and OMNI: an LLM supplies goals or interestingness (b12, c04).
- Motif: LLM preferences become reward (c07).
- Voyager: prompt-only curriculum (c10).
- MAGELLAN: an LLM predicts its own LP (c01).
- CDE and IMAGINE: curiosity bonuses in RLVR (d10, d11).

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree; supported = several sources but one lab; single-source; contested; human-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ICM solves sparse VizDoom | Mean (median) success: ICM+A3C 100% (100%); VIME+TRPO 46.1% (27.1%); TRPO 26.0% (0.0%); A3C 0.0% | Pathak 2017 (a14, b01) | established (K01) |
| ICM very sparse VizDoom | Perfect score in 66% of random runs; A3C and pixel ICM never | Pathak 2017 (a14) | established |
| ICM with noise | 40% of the screen replaced by white noise: ICM still succeeds, pixel ICM suffers. Uniform, Gaussian, Laplacian noise as reward never reached the goal | Pathak 2017 (a14, a23) | single paper; noise is fixed, not action-caused |
| Pure curiosity across 54 environments | Inverse-dynamics features beat random features in 55% of Atari games. Curious agent beat a random agent in about 75% of Atari games (random features 70%). Pixel-based dynamics worked poorly | Burda 2018 (a15) | established (K01) |
| Noisy TV in a Unity maze | Drastically slows both IDF and RF agents; long runs sometimes recover. Qualitative curves | Burda 2018 (a16) | established (K02) |
| RND on Montezuma | More than half the rooms found with no extrinsic reward. Best agent often 22 of 24 rooms. Mean return 7,570 (1.6B frames); 10,070 (RNN, 1024 envs); table row 8,152. Pitfall! not solved | Burda 2018 (a17, b05) | established (K01); tuned on Montezuma |
| Non-episodic intrinsic return | gamma_I 0.999 explored more rooms than 0.99; one run 21 rooms | Burda 2018 (a24) | single paper, few runs |
| Bonuses vs epsilon-greedy in Rainbow | 200M frames, 7 hard games. RND and ICM matched epsilon-greedy; pseudo-counts worse on all easy games except Seaquest | Taiga 2019 (b06, b07) | single-source (K05); different agent and budget |
| Surprisal vs learning progress | Surprisal good in 9 of 9 domains (5 continuous control, 4 Atari RAM), 10 runs. LP k=1 good on CartpoleSwingup and HalfCheetah, faltered elsewhere; MountainCar rewards went to zero when the model converged | Achiam and Sastry 2017 (a13) | single paper |
| ECO episodic reachability | DMLab 20M steps, 30 seeds. Very Sparse: PPO 8.6, ICM 11.2, EC 24.7, ECO 40.5, oracle 54.3. Sparse+Doors: 1.5 / 2.7 / 8.5 / 19.8 / 29.4. Dense 1: PPO 22.8, ICM 20.9, ECO 22.9 | Savinov 2019 (a18) | single-source (K07); third-party table garbled (d12) |
| Third-party ECO baseline | DMLab noisy-TV maze, 10 seeds: PPO 7.3 and 4.1; PPO+RND 16.3 and 12.9; PGR(ECO) 21.9. The PPO+ECO cell was not confirmed | Prioritized Generative Replay (d12) | unclear |
| Stickiness hurts prediction bonuses | Sticky actions: BYOL-Explore rooms about 25% lower, returns about 75% lower on Montezuma. BYOL-Hindsight repairs it | Jarrett 2022 (b09) | single-source (K06) |
| IAC zone robot | 5,000 steps. 85% of time in the second zone after about 3,000 actions. Plateau error about 0.09. Random: 33% in easy zone | Oudeyer 2007 (d04) | design precedent (K19); one run |
| IAC structured trajectory | 200 simulated runs: structure in 34%; biting 100%; bashing 78% | Oudeyer 2007 (d05) | design precedent |
| ALP-GMM curriculum | Short walkers at 20M steps: ALP-GMM 14.9%, Covar-GMM 10.6%, RIAC 8.6% (p<0.04). Hexagon Tracks: ALP-GMM 80% vs oracle 68% (p<0.02). All LP teachers beat random (p<0.001). Quadrupeds: random already near 100% | Portelas 2019 (b10) | established (K04); no edge when space is easy |
| CURIOUS LP module choice | After a perturbation: 95% of prior performance in 78k episodes (random) vs 43k (active LP), 45% faster, p<1e-4 | Colas 2019 (b11) | established (K04) |
| Teacher-Student LP | Maze unsolved by direct training was solved; about an order of magnitude faster than uniform subtask sampling | Matiisen 2017 (c13) | single-source |
| LP kept coverage under noise | MiniWorld (2,176 states), 10 seeds: LPM 1,347.6 states; best deterministic baseline EDT 1,276.1; under state noise LPM 1,434.0, action noise 1,340.0. Atari noise action: LPM drops 3.9% and 4.7%, +0.3% on Ms PacMan; EME fell 100%. LPM best in 4 of 6 games | Hou 2025/2026 (d07) | single-source (K16); own authors |
| LP on Montezuma | LPM non-trivial score at 20M steps; RND needed 50M; NGU re-implementation 0 at 50M | Hou (d08) | single-source; figure only |
| LP proxy in supervised noise | Gradient-Momentum Coupling keeps allocation near uniform across noisy task groups; error chases the noisiest. 20 seeds | Gradient-Momentum (2026) (d09) | single-source; preprint |
| Infants: Goldilocks | Exp 1: 42 infants analysed (44 tested), mean 7.9 months, peak interest near 1.25 bits. Exp 2: 30 infants, three-box display, 32 sequences. Only the squared complexity term significant in Exp 1. Effect "relatively small" | Kidd 2012 (d01) | human-only; no independent replication found |
| Infants: LP beats surprise | 43 infants analysed (50 recruited), 16 sequences. Wald chi2 for LP 48.87, surprise 19.38, predictability 21.87 (all P<0.001). Surprise and predictability effects 3 and 5 times weaker | Poli 2020 (d02) | human-only (K15); one lab |
| OMNI in Crafter | Uniform < LP (55 tasks, 9 interesting, success 0.42 all / 0.52 interesting) < OMNI (82 tasks, 14 interesting, 0.56 / 0.78). BabyAI: LP 4, OMNI 8 tasks. All p<1e-3 | Zhang 2023/24 (c04) | contested (K08): vs oracle interest mostly p>0.05 (c05) |
| OMNI-EPIC | 50 participants: 72.7% alignment between human judgement and the automatic success detector | Faldor 2025 (c06) | single-source |
| ELLM goal quality | Suggested goals: 64.9% good, 5% not allowed, 13.6% context-insensitive, 16.4% common-sense violating. Rewarded actions: 66.5% good, 32.4% bad. About 6 achievements vs oracle 9 in Crafter | Du 2023 (b12, c09) | established (K09); keep goal and action columns separate |
| Motif | Staircase levels 3 and 4: extrinsic-only and RND 0% success. Oracle task about 30% with intrinsic plus extrinsic. Prompt modifiers: +106% gold (CI 64-157), +17% descents, +150% kills. A misaligned composition was found | Klissarov 2024 (c07, c08) | single-source (K11) |
| Voyager | 3.3x unique items in 160 iterations; wooden tool 15.3x faster, stone 8.5x, iron 6.4x; 2.3x map distance; only agent to reach diamond (1 of 3). Random curriculum: -93% items | Wang 2023 (c10, c11) | single-source (K10); 3 trials; GPT-4 |
| MAGELLAN | Little-Zoo, 25k goals, 80% impossible, 8 seeds. Held-out competence error 0.11 vs 0.53 for online ALP (expert-grouped 0.09). Only method with no expert groups to reach above 90% on all categories | Gaven 2025 (c01) | single-source (K13); trained LLM |
| CDE on RLVR | Qwen3-4B-Base. GRPO average 48.2 to 50.6; AIME24 Avg@16 20.8 to 23.3; Pass@16 41.9 to 48.5; AIME25 21.0 to 23.5. PPO 46.5 to 47.7 | Dai 2025 (c12, d10) | supported (K12); one base model |
| IMAGINE on RLVR | Qwen2.5-3B: GSM8K 0.8082 to 0.8251; Countdown-34 0.6711 to 0.7132; Countdown-4 0.3872 to 0.4739. 0.5B: 0.0033 to 0.0107; 1.5B: 0.4532 to 0.5068. Abstract: +22.23% on AIME24 | Gao 2025 (d11) | supported; gains largest where baseline is lowest |
| Missing premise token drain | Reasoning models use about 2x to 4x more tokens on questions with a removed premise and cannot abstain | Fan 2025 (d14) | single-source (K17); ratio from the summary |
| Self-prediction | Untrained near majority-answer baseline. Finetuned Llama 70B 48.5% vs GPT-4o predicting it 31.8%. Calibration deviation 23.0 untrained, 8.7 self-trained, 21.3 cross-trained. Fails on long outputs | Binder 2025 (d13) | single-source (K18) |

## 4. Mechanisms and models

Each is written so it can be implemented. Pseudocode is plain.

**4.1 Raw prediction-error bonus (novelty).**
Train a forward model f(s, a) that predicts the next state s'. Bonus r = ||f(s,a) - s'||^2. Problem: if s' is random, error never falls (b04). Burda's point: error equals transition entropy under stochastic dynamics, so the agent seeks the noisiest transitions.

**4.2 ICM (a14).** Encoder phi maps the state to features. An inverse model predicts the action from phi(s), phi(s'). So phi keeps only what the agent can affect. A forward model predicts phi(s') from phi(s) and a. Bonus is the forward error in feature space. Not protected against noise that the agent itself causes (b08).

**4.3 RND (a17).** Two networks on the same state. The target network is fixed and random. The predictor is trained to match it. Bonus is the predictor error. The target is deterministic and inside the predictor's function class, so noise cannot inflate it. Use a non-episodic intrinsic return and a larger intrinsic discount (0.999) (a24). Normalise observations and rewards.

**4.4 Ensemble disagreement (b08, a19, a20).** Train k forward models (k = 5 in Plan2Explore). Bonus is the variance of their predictions. Pure noise gives agreement, so low variance. Only epistemic uncertainty pays. It fails when the agent is the source of the noise (b08).

**4.5 ECO episodic reachability (a18).** Keep an episodic memory of embeddings. A comparator network says whether a new observation can be reached from a memory item within k steps. Reward only observations not reachable. Memory resets each episode. Does not hurt dense-reward tasks.

**4.6 Pseudo-count (a12, a25).** A density model gives probability rho(s) before and rho'(s) after one update on s. Pseudo-count N = rho(1 - rho') / (rho' - rho). Bonus decays as 1/sqrt(N). Prediction gain, log rho' minus log rho, approximates information gain. (The count formula is the standard one from Bellemare 2016; it is written here from background knowledge, not re-read from the evidence files.)

**4.7 Learning progress, region version (IAC, a03, a05).**
1. Keep a set of regions of the sensorimotor space. Each has an expert predictor.
2. For each region keep a list of recent prediction errors.
3. Smoothed progress: LP = mean(errors older window) - mean(errors recent window), using window sizes tau and theta.
4. Choose the action whose region has the highest expected LP (with some random action, 15% in the zone run).
5. Split a region when it holds more than a set number of exemplars, cutting where summed variance drops most.
Needs a low learning rate for the before/after comparison to work (a05, a09).

**4.8 Learning progress for goals (CURIOUS, ALP-GMM, MAGELLAN).**
- CURIOUS (a21): 10% of episodes are self-evaluation rollouts. For each goal module, LP is the derivative of competence over a window. Sample module with probability proportional to absolute LP. Hindsight replay shares data across modules.
- ALP-GMM (b10): fit a Gaussian mixture on (task parameters, absolute LP). Sample new tasks from the components in proportion to their mean absolute LP, with a random fraction kept. (Mixture details from background knowledge.)
- Teacher-Student (c13): for each subtask fit a linear regression to the last K scores. Pick the subtask with the highest absolute slope (progress or forgetting).
- MAGELLAN (c01, c03): an LLM head predicts competence for each language goal from the goal text. LP is read from the change in predicted competence. This transfers to unseen goals. Goals are sampled in proportion to ALP.
Absolute LP is used so that forgetting also attracts attention.

**4.9 Hindsight and surprise (b09, a02).** Feed the predictor a learned code of the unpredictable part of each outcome, so the bonus counts only predictable dynamics. Surprise as ratio Er / predicted Er (a02) is the older version.

**4.10 LPM dual network (d07).** Two networks learn the same target; the gap in their improvement defines LP, so the reward falls to zero for both noise and mastered data. Baselines in the same code base: ICM, Ensemble, RND, AMA, EME, EDT. (Only the outline was captured; check the paper before implementing.)

**4.11 LLM interestingness (OMNI, c04).** A few-shot LLM judges whether each learnable task is interesting. Task choice is weighted by LP times the LLM-judged interest. Runs 33 h in Crafter and 60 h in BabyAI on one A10 with GPT-3 Davinci (b13).

**4.12 LLM goals (ELLM, c09).** Give the LLM a text description of the state. It suggests goals. Reward the agent for actions semantically close to a suggestion. Captioner had about 11% false negatives.

**4.13 LLM preference reward (Motif, c07).** The LLM ranks pairs of captions. Train a reward model on the preferences. Use it as intrinsic reward. Prompt wording steers behaviour (+106% gold).

**4.14 Prompt-only curriculum (Voyager, c10).** GPT-4 proposes the next task from agent state, past successes and failures. Solved tasks go to a skill library. Failed ones return to the queue.

**4.15 Curiosity for RLVR (CDE, d10).** Bonus from the actor's response perplexity plus critic value-head variance (multi-head critic). The bonus weight must decay; a staircase schedule was best. IMAGINE (d11) applies a sequence-level bonus after advantage computation.

**4.16 A scaffold analogue (our design, not tested).**
1. Before each probe the agent writes a predicted verifier result.
2. Code compares it to the real result.
3. Code keeps, per problem class, a list of recent pass rates.
4. LP = recent window mean minus older window mean.
5. Next subproblem = argmax absolute LP, with a random share.
This replaces the forward model with a stated prediction and the error list with verifier pass rates. Step 1 is the weak point (K18). Steps 3 to 5 need no model prediction at all and are the part to test first.

## 5. What holds up

**Holds in more than one source.**
- Prediction-error bonuses help in sparse-reward settings (K01: ICM, RND, large-scale study).
- Raw error is exploitable by noise (K02: Burda noisy TV, Hou, Gradient-Momentum, Fan).
- LP and absolute LP work as curriculum selectors (K04: ALP-GMM, CURIOUS; also Teacher-Student).
- LLM-proposed goals are mostly good, and not all of them (K09).

**Failed or weakened.**
- Taiga 2019: in Rainbow with 200M frames, RND and ICM only matched epsilon-greedy, and pseudo-counts did worse on easy games. This is a boundary condition (different agent, budget, tuned on Montezuma), not a refutation (b06, b07).
- RND was tuned on Montezuma and fails on Pitfall! (b05).
- Achiam and Sastry: LP faltered in most domains, and rewards went to zero on MountainCar when the model converged. Surprisal worked everywhere (a13). So LP is not uniformly better than error. It depends on the estimator.
- LP from Bellman errors (Veeriah 2018) did not beat random goal selection (a21).
- ICM learned to entertain itself by firing until it ran out of ammunition (a18).
- ICM handles noise not caused by the agent. Disagreement and similar designs fail when the agent causes the randomness (a14, b08).
- Quadruped task: random already mastered nearly 100%, so LP gave no edge (b10).
- OMNI beat LP, but against the hand-built oracle the differences were mostly not significant (c05).
- The ECO number is from the authors. A third-party table exists but the ECO cell is not confirmed (d12).
- ELLM, Motif and OMNI depend on the LLM's taste and on a text description of the state.

**Moderators.**
- Noise type: fixed noise region vs agent-caused noise (a14, b08).
- Agent type: PPO with huge frame counts vs Rainbow at 200M (b06).
- Task space: easy spaces show no LP advantage (b10); learnable but boring tasks distract LP (c04).
- Stochastic actions (sticky) cut BYOL-Explore sharply (b09).
- Baseline strength: RLVR gains are largest where the baseline is lowest (d11).
- Learning rate: LP by before/after comparison needs a low rate (a05).

**Human evidence.**
- Kidd 2012 (42 and 30 infants) and Poli 2020 (43 infants) agree that looking depends on learnability, with LP the stronger predictor in Poli. Both rest on the authors' own ideal-learner model. No independent replication was found (d01 to d03). Gaven 2025 cites four more human studies showing metacognitive LP monitoring; they were not opened (c22).
- Kidd 2014 (auditory) is the same group and was not opened (d03).

**Interventions that worked.** A progress or reachability signal in place of raw error; a decaying bonus weight (d10); non-episodic intrinsic return (a24); hindsight under sticky actions (b09); an LLM filter on interest (c04).
**Interventions that did not.** Pixel-space prediction (a15); Bellman-error LP (a21); uniform-noise reward (a23); the reasoning models' failure to abstain on unanswerable items (d14).

**Weak coverage.** Almost all numbers are RL benchmarks. Few head-to-head LP vs error vs RND tests exist beyond the proposing authors (K16). The three founding papers carry almost no numbers (K19).

## 6. Language models

What was measured, by role of the LLM.

**LLM as goal or curriculum proposer (prompt-only).**
- Voyager: 3.3x unique items, up to 15.3x faster tech tree, 2.3x map distance, random curriculum -93%. Three trials, GPT-4 (c10, c11). Part of the gain is the skill library.
- OMNI-EPIC: 72.7% human alignment with its success detector, n=50 (c06).
- ELLM goals: 64.9% good, 5% not allowed, 16.4% common-sense violations (c09).

**LLM as interestingness model.** OMNI: 82 vs 55 tasks in Crafter, success 0.56 vs 0.42 (c04). Near the oracle but not clearly better (c05). Depends on the judge model. This links to schema G8: a model's opinion of novelty is not trusted.

**LLM as reward model.** Motif: success where RND and extrinsic scored 0 on staircase levels 3 and 4; steerable by a single prompt sentence (+106% gold); one misaligned composition (c07, c08).

**LLM as trained agent with LP.** MAGELLAN: competence error on unseen goals 0.11 vs 0.53 for online ALP; weights are trained with online RL (c01). The math-competence case is simulated (c02).

**LLM training with curiosity bonuses.**
- CDE: +2.4 points average and +2.5 AIME24 on one 4B model (d10).
- IMAGINE: +2.09% GSM8K, +22.39% Countdown-4 on Qwen2.5-3B; at 0.5B Countdown-34 0.0033 to 0.0107, a gain near the floor (d11).
- These train weights. They are not scaffold effects.

**Self-prediction and introspection.**
- Untrained models predict their own behaviour close to the majority-answer baseline. Finetuning lifts a 70B model to 48.5%, and calibration deviation falls from 23.0 to 8.7. Long outputs fail (d13).
- So a stated expectation is not a trustworthy surprise signal without training. This is the weak step in any scaffold port (K18).

**Failure mode: token drain.** Reasoning models spend 2x to 4x more tokens on missing-premise questions and do not stop (d14). This is the LLM form of the noisy TV. No test inside a scaffold exists (K17, d16).

**What was not found.** No paper compares an LP ranker with an error ranker for subproblem choice in a prompt-only agent at equal tokens. None tests noisy-TV traps in a scaffold. None accounts for the tokens curiosity operators cost (d16, K20). Coverage of 2025-2026 is thin because search budgets ran out (c25).

## 7. What our agent should take

Schema mapping note. Our schema has guardrails G1-G12, states S0-S9, operators O1-O8 (idea tree) and memory. The field's selection rules map to G (guardrails), S0 (class record), S6 (impasse and operator choice) and memory. None of the O1-O8 operators is a curiosity operator, and nothing here changes them.

### Add now (established)

1. **Do not rank subproblems by raw error or by novelty alone.** Noise or unanswerable items can absorb the budget. Part: G12 (already says spend by difficulty); add one sentence: an item whose error does not change gets no extra tokens. Status [E] (K02; a16, b03, b04, c15, d07, d09, d14).
2. **Cap tokens per item with a no-progress stop.** Part: G11/G12. Status [E] for the noise trap in RL (K02); the token numbers are [S] (K17, d14). The stop rule is cheap and low risk. It must not break G6 (submit best so far).
3. **Validate self-proposed subgoals with a cheap check before spending tokens.** About 35% of LLM-suggested goals were not fully good (5% not allowed, 13.6% context-insensitive, 16.4% common-sense violating) (K09; b12, c09). Part: G, at S6 subgoal creation. [E].
4. **Any curiosity or novelty operator needs an explicit predictor and a random-branch control in its ablation.** Part: G7. Status [E] for the need of a model (K14; a01, a02, c19, d13); the control comes from Taiga [S] (K05; b06).
5. **Read progress from code-checked results, not from the model's opinion of novelty.** Part: G5/G8. [E] (G8 already holds; c05 shows LLM interest only matches a hand oracle).

### Test first

- **LP ranker for choosing the next subproblem or class** ([S]; K03, K04, K16; a03, b10, b11, c13, d07). Part: S0 class record + S6. Test T1.
- **LP per problem class as a router for token budgets** ([S]; K13; c01, c02). Part: S0, memory. T2.
- **Stated prediction before a probe as a surprise signal** ([S]; K18; d13). Part: S4. T3.
- **Repeat detection against own earlier attempts** ([S]; K07; a18). Part: memory + S3. T4.
- **LLM-rated interest as a filter on LP** ([C]; K08; c04, c05). Part: S6. T5. G8 says model judges of novelty are near chance, so this is a check only.
- **Self-curriculum plus skill/lesson library** ([S]; K10; c10). Part: memory subgoal library. T6.
- **No-progress stop rule on unanswerable items** ([S]; K17; d14). Part: G12. T7.
- **Audit LLM-derived progress for proxy gaming** ([S]; K11; c08). Part: G. T8.

## 8. Concrete tests on our bench

All arms get the same total tokens per item, setup cost counted (G7). Report mean and spread over at least 3 seeds. Items come from the bench and have a verifier.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 LP vs error ranker | A session of 40 to 60 subproblems from 4 to 6 problem classes with a verifier. 20% unanswerable by design (missing premise or impossible) | (a) uniform random class choice; (b) highest recent error; (c) highest absolute LP (recent window minus older window of verifier pass rates); (d) plain model, no routing | Solved fraction at the budget; share of tokens on unanswerable items | (c) at least equal to (a) on solved fraction; (b) wastes more tokens on unanswerable items. Expect (b) worse than (a) because of the noisy TV |
| T2 LP router for budgets | Mixed-difficulty set where classes differ in learnability | (a) equal split per class; (b) G12 difficulty-based; (c) absolute LP from past runs | Solved items per 1000 tokens | Small gain over (b) only if classes are learnable; no gain when all are easy (b10) |
| T3 stated prediction | Items with a code check | (a) no prediction; (b) agent states expected pass/fail and a number before each probe; (c) code-only surprise from past pass rate | Brier score of the stated prediction vs a base-rate baseline; solved fraction | Expect Brier near base rate (d13). Add only if Brier beats the base rate by a set margin |
| T4 repeat detection | Impasse-prone items where attempts loop | (a) none; (b) code flags an attempt whose answer or plan is near an earlier attempt and forces a new operator | Distinct candidate answers; solved fraction | Fewer repeated attempts; gain mostly at impasses |
| T5 interest filter | Open-mode idea items | (a) LP only; (b) LP times LLM interest score; (c) LP times code-checked usefulness | Solved fraction; unique valid ideas | Expect (b) not better than (c) (G8). Run as a check |
| T6 self-curriculum | Long sequence of related items | (a) random order; (b) order by agent-proposed next task; (c) order by LP | Final solved fraction; lessons reused | Voyager-like gain only if later items depend on earlier ones |
| T7 stop rule | 30% missing-premise items | (a) no stop; (b) stop after N tokens with no change in best candidate; (c) stop by stated confidence | Tokens on unanswerable items; accuracy on answerable ones | (b) cuts tokens on unanswerable items by about half or more with no accuracy loss; (c) weaker (verbal confidence is in 4b) |
| T8 proxy audit | Items where a cheap proxy of progress exists (shorter answer, more tests) | LP read from verifier vs LP read from model self-report | Rate of accepted wrong answers | Self-report LP is gamed more |

T1 and T7 can share items; run once and read both metrics.

## 9. What does not transfer, and why

- **Trainable reward.** ICM, RND, ECO, ensemble disagreement and CDE update weights. Our agent does not train. Only the selection logic can be copied.
- **Dense state streams.** The RL results use millions of frames (a17: 1.6B frames). Our items give a handful of verifier results per class. LP needs a window of at least a few points, so it will be very noisy at our scale. Oudeyer himself notes noise sensitivity and the need for low learning rates (a05, a09).
- **Forward models of the world.** Our problems are mostly static puzzles, not a changing environment. There is often nothing to predict step to step.
- **Zero-reward settings.** The field optimises exploration with no external reward. Our items have a verifier, so extrinsic signal exists. Taiga (b06) suggests bonuses add little when other signals exist.
- **Infant results.** Goldilocks and LP effects concern looking time in 7-month-olds (d01, d02). They show a design principle, not a measurement of how an LLM should work.
- **LLM-judged interest.** OMNI works near an oracle only in environments where the authors built the oracle (c05), and G8 says model novelty judgement is near chance on research ideas.
- **Voyager.** Minecraft has a code API, a skill library and 3 trials (c10). The gain cannot be assigned to the curriculum alone.
- **Reward hacking from Motif.** Applies to trained policies, though a scaffold can game proxies in a similar way (c08).

## 10. Open questions

1. Does an LP ranker beat an error ranker for subproblem choice in a prompt-only agent at equal tokens? (K20, gap 1)
2. Can a verbal self-prediction act as a calibrated surprise signal without finetuning? (K18, gap 2)
3. How many tokens does a scaffold waste on unanswerable but novel subtasks, and does a stop rule fix it? (K17, gap 3)
4. What are the numbers of Kaplan and Oudeyer 2004 and Schmidhuber 1991? Neither was opened. (K19)
5. Is ECO independently reproduced? Does it transfer to text? (d12 unclear)
6. Has Kidd 2012 or Poli 2020 been replicated by an independent lab? (d03)
7. Do LLM-judged interest signals resist reward hacking at scale? (K11, K08; the last search was refused)
8. Does CDE replicate on other base models? (d10 single base)
9. Do curiosity operators pay for the tokens they use? (d15 snippet only)
10. How large must a per-class window be before LP beats raw error at our small sample sizes?
11. The Bellemare Montezuma numbers (2461 then 3439) are unverified (critique.md).

## 11. Sources

[V] = opened and read this session (full text or substantial text). [M] = snippet or memory only.

- [V] Oudeyer and Kaplan 2007, typology of intrinsic motivation. https://www.frontiersin.org/articles/10.3389/neuro.12.006.2007 (a01-a04, c18)
- [V] Oudeyer, Kaplan, Hafner 2007, IMS for autonomous mental development. https://www.pyoudeyer.com/ims.pdf (a05-a07, d04, d05)
- [V] Schmidhuber 2010, formal theory of creativity. https://people.idsia.ch/~juergen/ieeecreative.pdf (a08, a09, c19, d06)
- [M] Kaplan and Oudeyer 2004, Maximizing learning progress. https://doi.org/10.1007/978-3-540-25940-4_11 (a10, b23)
- [M] Schmidhuber 1991, curiosity and boredom in model-building controllers. https://people.idsia.ch/~juergen/ (a11)
- [V] Bellemare et al. 2016, pseudo-counts. https://arxiv.org/abs/1606.01868 (a12, a25); b20 is [M]
- [V] Achiam and Sastry 2017, surprise-based motivation. https://arxiv.org/abs/1703.01732 (a13)
- [V] Pathak et al. 2017, ICM. https://arxiv.org/abs/1705.05363 (a14, a23, b01, b02, c14)
- [V] Burda et al. 2018, large-scale study. https://arxiv.org/abs/1808.04355 (a15, a16, b03, b04, c15)
- [V] Burda et al. 2018, RND. https://arxiv.org/abs/1810.12894 (a17, a24, b05, c16)
- [V] Savinov et al. 2019, ECO. https://arxiv.org/abs/1810.02274 (a18)
- [V] Shyam et al. 2019, MAX. https://arxiv.org/abs/1810.12162 (a19)
- [V] Sekar et al. 2020, Plan2Explore. https://arxiv.org/abs/2005.05960 (a20)
- [V] Colas et al. 2019, CURIOUS. https://arxiv.org/abs/1810.06284 (a21, b11)
- [V, header only] Forestier et al. 2022, IMGEP. https://arxiv.org/abs/1708.02190 (a22, c20)
- [V] Taiga et al. 2019, bonus-based exploration in ALE. https://arxiv.org/abs/1908.02388 (b06, b07)
- [V] Pathak, Gandhi, Gupta 2019, disagreement. https://arxiv.org/abs/1906.04161 (b08)
- [V] Jarrett et al. 2022, Curiosity in Hindsight. https://arxiv.org/abs/2211.10515 (b09)
- [V] Portelas et al. 2019, teacher algorithms (ALP-GMM). https://arxiv.org/abs/1910.07224 (b10)
- [V] Du et al. 2023, ELLM. https://arxiv.org/abs/2302.06692 (b12, c09)
- [V] Zhang et al. 2023/24, OMNI. https://arxiv.org/abs/2306.01711 (b13, c04, c05)
- [V] Gaven et al. 2025, MAGELLAN. https://arxiv.org/abs/2502.07709 (b14, c01-c03, c21, c22)
- [M] Ecoffet et al., Go-Explore. https://arxiv.org/abs/2004.12919 (b21)
- [M] Aubret et al., survey. https://arxiv.org/abs/1908.06976 (b22)
- [M] Baranes and Oudeyer 2013. https://doi.org/10.1016/j.robot.2012.05.008 (b24)
- [V] Faldor et al. 2025, OMNI-EPIC. https://arxiv.org/abs/2405.15568 (c06)
- [V] Klissarov et al. 2024, Motif. https://arxiv.org/abs/2310.00166 (c07, c08)
- [V] Wang et al. 2023, Voyager. https://arxiv.org/abs/2305.16291 (c10, c11)
- [V] Dai et al. 2025, CDE. https://arxiv.org/abs/2509.09675 (c12, d10)
- [V] Matiisen et al. 2017, Teacher-Student Curriculum Learning. https://arxiv.org/abs/1707.00183 (c13)
- [V, scalars not rechecked] Kauvar et al. 2023, Curious Replay. https://arxiv.org/abs/2306.15934 (c17)
- [V, scalars not rechecked] Ma et al. 2024, Eureka. https://arxiv.org/abs/2310.12931 (c23)
- [V] Kidd, Piantadosi, Aslin 2012, Goldilocks effect. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036399 (d01)
- [V] Poli et al. 2020, infants tailor attention. https://europepmc.org/article/PMC/PMC7531891 (d02)
- [M] Kidd et al. 2014, auditory Goldilocks. https://pmc.ncbi.nlm.nih.gov/articles/PMC4807134/ (d03)
- [V] Hou, An, Du 2025/2026, LPM. https://arxiv.org/abs/2509.25438 (d07, d08)
- [V] Gradient-Momentum Coupling 2026. https://arxiv.org/abs/2605.05856 (d09)
- [V] Gao et al. 2025, IMAGINE. https://arxiv.org/abs/2505.17621 (d11)
- [V, table garbled] Prioritized Generative Replay 2025. https://arxiv.org/abs/2410.18082 (d12)
- [V] Binder et al. 2025, Looking Inward. https://arxiv.org/abs/2410.13787 (d13)
- [V] Fan et al. 2025, Missing Premise. https://arxiv.org/abs/2504.06514 (d14)
- [M] Bougie and Watanabe 2025, language-driven exploration. https://proceedings.mlr.press/v260/bougie25a.html (d15)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 4 established claims: 3 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C07.04-K14** (reworded: the sources support less). Oudeyer and Kaplan 2007 and Schmidhuber 2010 do support that knowledge-based intrinsic motivation needs a predictive model of the environment, but none of the sources (including Binder et al. 2025 on introspection) address prompt-only LLM agents, so the 'can use it only through an explicit predictor' part is the researcher's inference, not a sourced finding. Corrected claim: Knowledge-based intrinsic motivation needs a predictor or model of the environment (Oudeyer and Kaplan 2007; Schmidhuber 2010); inference, not tested in the sources: a prompt-only agent could approximate it through an explicit predictor (a stated expectation compared with the outcome).
- **C07.04-K09** (now single-source: only one opened source, code check).
