# Bandit-style exploration: deep document

*Subfield E14.04. Built from evidence_a-d.jsonl, claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids (a01, b13, d05 ...) point to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Bandit-style exploration is the family of rules that decide how much to try new options and how much to repeat the best known one, when each try is costly and the payoff is noisy or rare.

The core pieces:

- **Multi-armed bandit.** K options (arms). Each pull gives a reward. You want the most total reward. You learn an arm's quality only by pulling it.
- **Regret.** Reward lost against always pulling the best arm. Lai and Robbins (1985) showed regret must grow at least like ln n [K19, a01, a03]. Some waste is unavoidable.
- **Simple rules.** Epsilon-greedy (random pull with probability eps), softmax (pull in proportion to value), UCB (mean plus a bonus that shrinks with tries), Thompson sampling (sample a belief for each arm, pull the top sample).
- **Intrinsic rewards.** In reinforcement learning with sparse reward, the agent makes its own bonus: a count of visits, a prediction error, or a distance to known states. This is the UCB idea scaled to huge state spaces.
- **Two named traps.** Sparse reward (no signal, so nothing to learn from) and the noisy TV (a source of endless, useless novelty that pays the bonus for ever).

Why it matters for our agent. The schema grows a tree at S6 and applies operators O1-O8 to children. It must decide, per problem class, how wide to widen and when to stop. That is a bandit problem. G12 already says "spend by difficulty and search only where there is a foothold". G5 says code selects. G8 says novelty is judged by running, not by a model's opinion. This subfield supplies the mechanics of a per-class widen rule and shows what can go wrong.

Scope note. Other subfields in this run cover exploration vs exploitation in humans, optimal stopping, retrieval as a bandit, test-time compute scaling and creativity as search. We only link to them. Here we cover the algorithms, the RL intrinsic-reward literature, and the LLM tests.

## 2. History and theories in depth

**1933. Thompson.** Thompson proposed choosing a treatment with the posterior probability that it is best, for two-sample clinical trials [a04, not opened]. It sat mostly unused for decades.

**1985. Lai and Robbins.** They proved a lower bound: any consistent policy pulls each worse arm at least about (ln n)/KL times. Index policies can reach it [a03, via Auer 2002 eq. 1; not opened].

**2002. Auer, Cesa-Bianchi, Fischer.** UCB1 plays the arm with the highest mean plus sqrt(2 ln n / n_j). Each arm is played once first. The bound is logarithmic for any finite n, with no prior knowledge of reward distributions [a01, a23]. In their simulations (7 Bernoulli problems, 2 and 10 arms) a well-tuned epsilon-greedy "almost always" did best, and UCB1-Tuned was close behind. Epsilon-greedy degraded fast when badly tuned, and tuning needs the gap size, which you do not know in practice [a02]. UCB1-Tuned had no proof [a01].

**2006. Kocsis and Szepesvari.** UCT applies UCB1 at every tree node to choose which child to expand. This is the root of Monte-Carlo tree search and of LATS [a08, not opened].

**2011-2014. Thompson returns.** Chapelle and Li (2011) showed Thompson sampling (TS) beating UCB on simulated and news data [a07, b28, snippet only]. Kaufmann, Korda and Munos (2012) proved TS matches the Lai-Robbins bound for Bernoulli arms with finite-time bounds [a06, b06]. Kuleshov and Precup (2014) ran a large simulation and found epsilon-greedy and softmax beat the provably good algorithms on most settings, but with parameters tuned per setting (eps 0.005 to 0.1) [b01, b02]. Russo et al. (2018/2020) wrote the TS tutorial and the standard greedy lock-in demo [a05, a24, b04, b05].

**Intrinsic motivation, early.** Schmidhuber's formal theory of curiosity is the source of the white-noise TV example. It proposes rewarding learning progress, not error [a20, not opened; known via Pathak 2017]. Sutton and Barto cover the exploration bonus in Dyna-Q+ [a19, not opened].

**2016. Pseudo-counts.** Bellemare et al. defined counts from a density model over pixels, so a UCB-like 1/sqrt(N) bonus works in huge state spaces. Much better exploration on hard Atari games [a09, b14; scores not read].

**2017. ICM.** Pathak et al. reward the error in predicting next-state features, but only features the agent's actions can affect (an inverse model picks them). With 40% of the observation replaced by white noise, ICM still mostly succeeded [a10].

**2018. Large-scale curiosity and RND.** Burda et al. trained pure-curiosity agents on 54 environments. Many games were playable with no extrinsic reward. A literal noisy TV in a Unity maze "drastically slowed" learning [a12, b07, c20, d14]. Their second paper, random network distillation (RND), uses the error at predicting a fixed random network. The target is deterministic, so transition noise cannot inflate the bonus [a11, c19].

**2019. Go-Explore.** Ecoffet et al. named two failures of intrinsic motivation. Detachment: the agent forgets frontiers once their bonus is used up. Derailment: random noise stops it returning to a promising state. Their fix is an archive of states and a return step before exploring [a13, b16, c21].

**2019-2020. Episodic and meta-bandit methods.** Episodic curiosity through reachability rewards states that are far in steps from anything in the episode's memory [b12, b13]. NGU mixes an episodic bonus with a lifelong RND bonus and trains a family of policies from explorative to greedy [a14]. Agent57 added a non-stationary bandit over (bonus strength, discount) pairs, picking one per episode, rewarded by the episode's extrinsic return. It beat the human baseline on all 57 Atari games [a15, a26].

**2017-2022. Curriculum bandits and procedural worlds.** Teacher-student curriculum learning and automated curriculum learning use a bandit over tasks, rewarded by learning progress [d15, d16]. RIDE (2020) and E3B (2022) showed that RND, ICM and counts stall in procedurally generated worlds; episodic bonuses do better [d12, d13].

**2022-2026. Language models.**

- Binz and Schulz: GPT-3 on the horizon task [c17, c18].
- Krishnamurthy et al. (2024): do LLMs explore in context? Mostly no [a16, a17, c01-c05].
- Nie et al. (EVOLvE, 2024/25) [c06-c09].
- Schmied et al. (2025) [c10-c13].
- Pan et al. (2025) [d05]; Harris and Slivkins (2026) [d04].
- Inoue et al. (2025), AB-MCTS: a Thompson rule to widen or deepen [d01, d02].
- Zuo and Zhu (2026): bandit allocation across queries [d03].
- Lu et al. (2025): Intelligent Go-Explore [d21].
- ShinkaEvolve: UCB1 over which model proposes a mutation [d22].

**Competing explanations of the same facts.**

- *Tuned heuristics vs principled rules.* Auer 2002 and Kuleshov 2014 say tuned simple rules win. Kaufmann 2012 and Russo 2018 say TS and UCB are efficient without tuning. Both hold. The difference is whether the gap size is known and whether the setting is stationary (critique.md).
- *Why do LLMs fail to explore?* Candidates: a pre-training pull to repeat what is in context (frequency bias, c11), greedy training (d09), weak use of raw history (a27), label priors (d07). They are not mutually exclusive.
- *Why does the noisy TV hurt?* The simple view is stochastic prediction error. Burda's own note is that other causes were not isolated (a25).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Regret must grow at least logarithmically | E[T_j(n)] >= (1/D + o(1)) ln n | Lai-Robbins via Auer 2002 (a01, a03) | [S] (K19; original not opened) |
| UCB1 has log regret at every finite n | Index = mean + sqrt(2 ln n / n_j); each arm tried once first | Auer 2002 (a01, a23) | [E] |
| Tuned epsilon-greedy usually best in simulation | 7 Bernoulli problems; "almost always"; fails if badly tuned; exceptions on 2 many-arm problems | Auer 2002 (a02) | [E] (K05) |
| Softmax/eps-greedy beat UCB/TS on most settings | eps 0.005-0.1; UCB1-Tuned best only for sigma=1, K=2,5,10 | Kuleshov and Precup 2014 (b01) | [E] (K05) |
| Greedy locks on a bad arm after early luck; TS does not | 3 arms 0.9/0.8/0.7; 10,000 sims x 1,000 periods; TS regret to 0, greedy stays above 0 | Russo 2018 (a05, a24) | [E] (K01) |
| TS reaches the Lai-Robbins bound (Bernoulli) | Regret <= (1+eps) sum (mu*-mu_a)/KL ln T + C | Kaufmann 2012 (b06) | [S] (K06) |
| Plain UCB1 and TS degrade when rates drift | UCB1 slow to switch back after 2nd breakpoint (t=5000); TS high regret under slow/fast change | Garivier-Moulines 2008 (d17); Raj-Kalyani 2017 (d18) | [S] (K22) |
| Discounted TS and SW-UCB fix drift | dTS gamma 0.40 (T=500, window 24), 0.75 (T=2500, window 89), 0.60 (T=1000, window 37); margin gone under abrupt change | Raj-Kalyani 2017 (d18) | [S] |
| Window for SW-UCB | tau = 2B sqrt(T log T / Y_T); regret O(sqrt(Y_T T) log T) | Garivier-Moulines (d17) | [S] |
| Forward-error curiosity hijacked by a noisy TV | Unity maze: "drastically slows" IDF and RF agents; sometimes converge if run long | Burda 2018 (a12, b07, d14) | [E] (K07); no trial count |
| RND helps on sparse games, with exceptions | Montezuma 8,152 vs PPO 2,497; Gravitar 3,906 vs 3,426; PrivateEye 8,666; Venture 1,859; Pitfall -3; 22 of 24 rooms | Burda RND (a11, b08) | [S] (K09) |
| RND is seed-fragile | 5-seed vs 10-seed CNN results disagreed strongly | Burda RND footnote (b09) | [S] |
| Dynamics bonus vs RND | RNN table: Montezuma 400 vs 8,152; PrivateEye 105 vs 8,666; Venture 0 vs 1,859. CNN run: worse on Montezuma, PrivateEye, Solaris; similar on Venture, Pitfall, Gravitar | Burda RND (a25, b10) | [C] (K10) |
| Reachability holds up under injected noise | DMLab: PPO 11.6, ICM 7.7, EC 18.7, ECO 28.2 (Noise); 9.8/7.6/14.8/18.9 (Noise Action); 27.0/23.8/26.2/41.6 (Original) | Savinov 2019 (b13) | [S] (K08) |
| VizDoom MyWayHome | EC 100% success in all 3 settings, at least 2x faster than ICM | Savinov 2019 (b12) | [S] |
| Archive-and-return beats pure novelty | Go-Explore Montezuma 43,763 (no domain knowledge), 666,474 (with; best run over 18M, 1,441 levels); Pitfall mean 59,494, max 107,363 | Ecoffet 2019 (a13, b15) | [S] (K11); budgets not comparable |
| A bandit over exploration modes | Agent57: 57 of 57 Atari games above human; window mean over 50 episodes | Badia 2020 (a15, a26) | [S] (K12) |
| Count/RND/ICM stall in procedural worlds | MultiRoomN10S6: Count, RND, ICM reach room 4, 3, 2; RIDE all rooms | Raileanu 2020 (d12) | [S] (K27) |
| E3B beats RND, ICM, RIDE, NovelD | 16 MiniHack tasks; median, IQM, mean, rliable protocol | Henaff 2022 (d13) | [S] |
| Basic GPT-4 fails to explore | Suffix failure in over 60% of replicates (T=500, N=20); 1 of 32-72 configs explored well | Krishnamurthy 2024 (a16, c02, c03) | [S] (K02) |
| Winning config details | T=200, N=40: SuffFailFreq(T/2) TS 0.00, UCB 0.02, Greedy 0.47, BSRC0 (raw) 0.12, BSSC0 (summary) 0.03; K*MinFrac 0.23/0.12/0.03/0.11/0.29; median reward 0.59/0.70/0.60/0.65/0.54 | Krishnamurthy (c04, c05; confirmed in critique.md) | [S] |
| Summary beats raw history | EVOLvE few-shot win-rate 50.2 (summary) vs 27.5 (raw) | Nie 2024 (b20, c08) | [S] (K03) |
| Code-computed UCB support helps big models, hurts small | MAB win-rate Flash 27.7 to 32.2, Pro 45.5 to 59.6; CB Flash 0.0 to 46.4, Pro 7.1 to 64.3; UCB 90.6 (MAB), 96.4 (CB); Gemma 2B 7.6 to 4.9, 9B 10.5 to 4.1 | Nie 2024 (c07) | [S] (K04) |
| Fine-tuning on UCB traces | Flash 65.6 (hard demos) vs 54.5 (easy); beats Pro raw 45.5. Few-shot reverse: 50.2 easy vs 43.0 hard | Nie 2024 (b21, c08, c09) | [S] |
| Knowing-doing gap | 87% of rationales compute correct UCB values; 58% greedy and 21% optimal actions (intro says 64% greedy) | Schmied 2025 (c12) | [S] (K13) |
| Poor coverage, frequency bias | Gemma2 2B/9B/27B cover 40/65/65% of 10 arms; 45% of 20 arms (27B); 96% repeat share (2B) vs 14% (27B) | Schmied 2025 (c10, c11) | [E] (K14) |
| Prompt-level and RL fixes | Try-all-once the biggest prompt gain; RL on own CoT: coverage +12%, frequent-action share 70% to 35% | Schmied 2025 (c13) | [S] |
| GPT-3 horizon task | Regret equals humans at short horizon (t(5566)=-0.04); lower overall (2.72 vs 3.24); no directed exploration | Binz-Schulz 2022 (c17, c18) | [S] (K15) |
| Reasoning models explore far better in open text | Little Alchemy 2, 500 trials: o1 177, R1 85, humans 42, GPT-4o 35, Llama-70B 25, Llama-8B 9 | Pan 2025 (d05) | [S] (K20) |
| Reasoning models fix "exploit from log" | GPT-5-mini perfect on 5-arm best-empirical-arm task for all gaps and lengths | Harris-Slivkins 2026 (d04) | [S] |
| Labels bias exploration | Meaningful labels cut exploration; misleading labels badly hurt; negative rewards trigger more exploration | Semantic Bandits 2026 (d07) | [S] (K24) |
| LLMs misallocate re-checks | 3 of 5 models re-test 75-94% of slots, one 14%, one 44%; scripted rules 24% and 38%; a replayed final re-test recovers about a quarter of the loss | Wellocate 2026 (d08) | [S] (K23) |
| Compact memory beats free reasoning (35 agents) | 50.0 to 76.9 (Gemini 3.1 Flash Lite); 66.7 to 72.2 (GPT-4.1), as extracted; log-error vs success R2 0.885 / 0.875 | Anonymous 2026 (d06) | [S] (K03; table layout garbled) |
| Trained bandit agents become greedier | SFT/RL give regret near UCB/TS via more early catastrophic failure | Chen 2025 (d09) | [S] |
| In-context RL needs positive-only or stochastic episodes | CLINC150 0.104 naive, 0.648 positive-only, 0.660 stochastic; NLU 0.292/0.836/0.814; TREC-fine 0.412/0.744/0.836; Qwen2.5-7B Banking77 6.2% to 72.2% | Monea 2025 (c16, d20) | [S] (K17) |
| LLM interestingness filter | Crafter tasks learned: uniform 4, LP 55 (9 interesting), OMNI 82 (14); mean success on interesting 0.52 vs 0.78; new-task generation: LP 2, OMNI 13 | Zhang 2024 (c23, d19) | [S] (K18, K26) |
| ELLM goals | 64.9% sensible; about 5% impossible | Du 2023 (c22) | [S] |
| UCT over LLM steps | HumanEval 80.1 to 92.7 (GPT-4); HotPotQA EM: full 0.63, DFS 0.42, no reflection 0.58, no LM heuristic 0.37 | Zhou 2023 LATS (b23, b25, c25) | [S] (K16) |
| LATS exploration weight | HotPotQA, 100 questions: w=0.5 0.55; w=1 0.63; w=2.0 0.63 (corrected; not a gain) | Zhou (d26) | [S] |
| Thompson widen/deepen at equal calls | MLE-Bench avg rank AB-MCTS-M 1.3 vs sequential 2.3, repeated 3.0, MCTS 3.3; ARC-AGI GPT-4o Pass@2 repeated 15.0, AB-MCTS-A Beta 14.0, Gaussian 13.0 | Inoue 2025 (d01) | [S] (K21) |
| Progressive widening matches it at the right (k, alpha) | LiveCodeBench, budget 2^7: PW(5,0.5) 50.7+-1.3; PW(10,0.55) 50.5+-3.1; PW(1,0.45) 48.7+-0.8; AB-MCTS-A Beta 51.8+-1.4 | Inoue Appx C.4 (d02) | [S] |
| Bandit over queries at equal compute | Up to +11.10 (MATH-500), +10.82 (AIME25), +11.23 (LiveCodeBench) points | Zuo and Zhu 2026 (d03) | [S] ("up to") |
| Archive-and-return with an LLM chooser | Game of 24 at 150 steps, 100 seeds: IGE 100% vs classic Go-Explore 38+-22; 70.8% faster than DFS | Lu 2025 (d21) | [S] (K11) |
| UCB1 over which model mutates | Cosine threshold 0.95, 3 novelty tries, UCB1 coefficient 1.0 | ShinkaEvolve (d22) | [S] |
| Entailment clusters as a paraphrase-safe count | AUROC CoQA 0.77 vs 0.66 (distinct answers); TriviaQA 0.83 vs 0.79; clusters 1.27 vs 1.77 (CoQA), 1.89 vs 3.89 (TriviaQA) | Kuhn 2023 (d24) | [S] (K25) |
| Embedding choice can flip a novelty bonus | Playroom efficiency +18 to 70%; ImageNet embeddings hurt on "find" | Tam 2022 (d23) | [S] |

## 4. Mechanisms and models

Each rule is written so it can be coded. "Class" means a problem class from S0. A "pass" means the code check passed on a candidate.

### 4.1 Greedy lock-in (why a rule is needed)

Greedy picks the arm with the best mean so far. After two early wins on a 0.7 arm, untried arms still have a prior mean of 0.5, so greedy never tries the 0.9 arm [a24]. In a tree this is "keep deepening the first branch that scored". Per-period regret stays above zero for ever.

### 4.2 Epsilon-greedy

- With probability eps pick uniformly. Otherwise pick the best mean.
- Decay eps with n (Auer's eps_n) or fix it at 0.005-0.1 [b01].
- It wastes pulls on arms known to be bad [b04].
- It needs the gap size to tune. Tune on held-out data (K05).

### 4.3 Softmax (Boltzmann)

- p(arm) proportional to exp(mean / temperature).
- Lowest regret in most of Kuleshov's tasks [b01]. Same tuning problem.

### 4.4 UCB1

- Pull each arm once. Then pull argmax of `mean_j + c * sqrt(2 ln n / n_j)`.
- n is total pulls, n_j this arm's pulls. Rewards in [0,1], c = 1 in theory.
- The bonus grows slowly with n and shrinks with n_j. Every arm is revisited at a log rate [a23].
- Smaller constants do better in practice (UCB1-Tuned) [a23].
- UCT is the same formula at each tree node: `V(s) + w * sqrt(ln N(parent) / N(s))` [c24].

### 4.5 Thompson sampling (Beta-Bernoulli)

- Keep `(alpha_j, beta_j)` per arm, start at (1,1).
- Each round draw `theta_j ~ Beta(alpha_j, beta_j)`, pull argmax, then add 1 to alpha on a pass or to beta on a fail [a05].
- No exploration constant. Exploration shrinks as certainty grows.
- The guarantee assumes independent pulls from a stationary arm. LLM passes are correlated (SCHEMA G4), so the guarantee is loose [b05].

### 4.6 Non-stationary variants

- **Discounted TS.** Each round, shrink all `(alpha, beta)` toward the prior by gamma before the update. gamma 0.4-0.75 in the tested settings [d18].
- **Sliding-window UCB.** Use only the last tau pulls. `tau = 2B sqrt(T log T / Y_T)`, with Y_T breakpoints [d17].
- **Last-K TS.** Build the Beta from only the last K results of each arm; no exploration constant [d15, via K22].
- **Agent57 bandit.** Window mean over the last 50 episodes, small random-choice probability (0.01 in the text) [a15].

Plain UCB1 and TS are not safe once pass rates drift [d17, d18]. Our class pass rates will drift as the schema and the model change.

### 4.7 Counts, pseudo-counts and intrinsic bonus

- Count bonus: `beta / sqrt(N(s))`. Fine for small tables.
- Pseudo-count: derive N from a density model's probability before and after seeing s [a09].
- ICM: bonus = error predicting next-state features from (state, action); an inverse model picks features, so uncontrollable pixels drop out [a10].
- RND: bonus = error of a trained net matching a fixed random net on the new state. Deterministic target, so no reward for transition noise [a11]. Use a non-episodic intrinsic return (gamma_I = 0.999) so risk-taking for novelty is not cut [a22]. Keep separate value heads for the intrinsic and extrinsic streams [a22].
- Reachability (EC): store embeddings of states seen this episode; bonus is high when a new state is many steps from all stored ones, as predicted by a trained comparator [b12].
- E3B: elliptical episodic bonus on inverse-dynamics features; resets per episode [d13].
- Learning progress: reward = slope of recent scores per task [d15], or a gain estimate averaged over a batch of samples to cut noise [d16].
- Interestingness filter: ask a model whether a learnable task is worth learning, on top of learning progress [d19].

### 4.8 Noisy-TV failure and the four defences

The failure: a stream whose outcome is random gives high prediction error for ever. The agent sits in front of it.

1. Predict only controllable features (ICM) [a10].
2. Predict a deterministic target (RND) [a11].
3. Reward error reduction, not error (Schmidhuber) [a20, d15, d16].
4. Use reachability or episodic memory, so only states far from stored ones pay (EC, E3B) [b12, d13].

Caveats. ICM still fell under a noisy-TV ball in MiniGrid [d12]. Learning progress has its own noisy TV in task space: trivial variations whose success rate fluctuates [d19].

### 4.9 Archive and return (Go-Explore)

- Keep an archive of cells (compressed states), each with its best trajectory.
- Loop: pick a cell (weighted toward new or promising), return to it, explore from it, add new or better cells.
- This fixes detachment and derailment [a13].
- Phase 1 needs a resettable simulator. Phase 2 robustifies into a policy.
- Intelligent Go-Explore lets an LLM choose which cell to resume, which action to try and which states to keep [d21].

### 4.10 Bandit over modes, tasks and children

- Agent57: arms are (bonus strength, discount) pairs; reward is episode return [a26].
- AB-MCTS: at each node, Thompson sampling decides between widening (new child) and deepening (refine a child). No fixed branching factor [d01].
- Progressive widening: allowed children at a node = `k * N^alpha` [d02].
- Query-level allocation: a pure-exploration bandit puts more samples on hard but solvable queries [d03].
- ShinkaEvolve: UCB1 picks which LLM writes the next mutation; reward is exp of the relative gain over the parent [d22].

### 4.11 Visit count for text ideas

Not solved. Options tested somewhere:

- Meaning clusters via bidirectional entailment with a small NLI model (DeBERTa-large), built to ignore paraphrase [d24].
- Code-embedding cosine above 0.95 as a near-duplicate filter [d22].
- Compression ratio, long n-gram self-repetition and Self-BLEU as cheap diversity scores. They correlate little with each other, and diversity scores can be length-confounded [d25].

None has been tested for paraphrase invariance (K25).

## 5. What holds up

**Established with several sources.**

- Greedy choice locks on an early lucky branch. Optimism for untried arms or sampling from belief fixes it (K01; Russo, Kaufmann, Auer, and the LLM failures in Krishnamurthy and Schmied).
- Tuned simple rules are hard to beat in simulation, but tuning needs gap knowledge (K05).
- Forward-prediction-error curiosity is hijacked by noise. Six sources point the same way (K07).
- Code-computed counts of tries and passes switch exploration on where raw history plus reasoning does not (K03; Krishnamurthy, EVOLvE, Semantic Bandits, the 35-agent study).
- LLMs show frequency bias and low action coverage (K14).

**Failed or weak replications and caveats.**

- RND is seed-fragile. The authors' own 5-seed and 10-seed runs disagreed [b09].
- RND fails on Pitfall (-3, same as PPO) and shows no consistent Gravitar gain [b08, a11].
- The dynamics-bonus penalty is game-specific (RNN table vs CNN comparison) [K10, contested].
- RND, ICM and counts stall outside fixed Atari levels [d12, d13]. Both studies come from authors of a competing method. No neutral replication was found.
- ICM hurts on Mario once extrinsic reward is added [d12].
- Go-Explore scores are not comparable with RND's: different budgets, a resettable simulator, and a PDF table that garbled one column (critique.md note 5).
- Krishnamurthy's finding has one source and 2023 models. T=100, N=10-20 is low power, so they used surrogate statistics [c01].
- GPT-3 regret equals or beats humans [c17], which looks like a conflict with later "LLMs do not explore" results. Tasks and model generations differ (critique.md).
- EVOLvE's algorithm-guided support helps large models and hurts the two Gemma models [c07].
- LATS: w=2.0 did not beat default w=1 (0.63 each). An earlier reading "w=2.0 beats w=0.5" was wrong framing. Only 100 questions, one run [d26].
- AB-MCTS is level with plain repeated sampling on ARC-AGI at GPT-4o, and progressive widening with the right (k, alpha) matches it on LiveCodeBench [d01, d02].
- Wellocate: a summary of readings changed re-testing by at most 5 points, so summaries do not always help [d08].
- OMNI and Monea have no independent replication; Monea's base-model sweep is inside one paper [d19, d20].

**Moderators.**

- Model size: UCB support helps Flash and Pro, hurts Gemma 2B and 9B [c07].
- Number of arms: algorithm-guided support helps more with more arms [b22]. Summarising is easy at K=5 and hard with many arms or contexts [c05].
- Horizon: bimodal runs hide failure at short T [c03, b18].
- Reasoning mode: raises exploration in open text and fixes exploit-from-log [d05, d04, d10]. Priors persist [d07].
- Label content: descriptive names change exploration [d07].
- Reward sign: negative reward drives more exploration [d07].
- Drift: plain TS and UCB1 degrade [d17, d18].

**Interventions that worked.**

- Code-computed per-arm summary plus hint plus CoT (the only working GPT-4 config) [c02].
- Try-all-once, the best prompt-level fix [c13].
- Keep positive-reward episodes only, or subsample episodes at random [c15, d20].
- Archive of partial progress with LLM node choice [d21].
- Thompson widen/deepen with the right priors [d01].
- A compact code-built memory over free reasoning for 35 agents [d06].
- A list of untried options (helped more than a summary of readings) [d08].
- Sampling several actions and choosing by log-probability rank (DORA): Qwen-2.5 7B TextWorld 31.43% to 45.5% [d11]. The gain is in action diversity and could be noise.

**Interventions that did not work or backfired.**

- CoT without summarised history [b19].
- Epsilon-greedy and self-consistency prompts were mixed in Schmied's tests [c13].
- Few-shot demos with raw history hurt the larger model (Pro 45.5 to 39.1) [c08].
- RL or SFT training raised greediness and early catastrophic failure [d09]. This is outside our no-training rule.
- Letting the model set the re-check rate (it over- or under-confirms) [d08].
- Model-judged interestingness with no code backstop risks self-preference; the OMNI judge was GPT-3 or GPT-4 only [b26, d19].

## 6. Language models

**Old finding (2022-2024): models did not explore in context.**

- GPT-3 on the two-arm horizon task: random exploration only, no directed exploration. Reward difference changed choice noise (beta=0.18, z=14.48) but did not interact with horizon, so noise was not used strategically [c18].
- Basic GPT-4 prompt, 5-arm bandit: suffix failure in over 60% of replicates [c03]. Two failure kinds: stop choosing the best arm for ever (suffix failure), or pick all arms near-equally (uniform-like, K*MinFrac up to 0.49) [c04]. A fix for the first often produces the second [a17].
- Only one of 32-72 prompt designs per model worked: hint, externally summarised stats, CoT. With raw history in the same prompt, suffix failure rose from 0.03 to 0.12 [c05]. GPT-3.5 was worse than GPT-4, Llama2 worse again [c05].
- Gemma2 2B/9B/27B covered 40/65/65% of 10 arms. The 2B model repeated its most frequent action in 96% of picks once many repeats were in context [c10, c11].
- Knowing-doing gap: 87% of rationales were right about UCB values, but only 21% of actions were optimal and 58% greedy [c12].
- Chen 2025: models trained on bandits (SFT or RL) match UCB/TS regret mostly by exploiting harder, with more early catastrophic failure [d09].

**What changed it, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Code-computed summary (counts, means) | Suffix failure 0.12 to 0.03 (T=200, N=40, GPT-4) | c05 |
| Summary vs raw history in few-shot demos | 27.5 to 50.2 win-rate | b20 |
| UCB values given at inference (large models) | MAB 27.7 to 32.2 (Flash), 45.5 to 59.6 (Pro); CB 0.0 to 46.4, 7.1 to 64.3 | c07 |
| UCB values given at inference (small models) | 7.6 to 4.9, 10.5 to 4.1 (worse) | c07 |
| Fine-tune on UCB traces | 65.6 win-rate; above Pro raw 45.5 | c08 |
| Try-all-once prompt | Biggest prompt-level gain; no single number | c13 |
| RL on own CoT | Coverage +12%; frequent share 70% to 35% | c13 |
| Reasoning mode in Little Alchemy 2 | GPT-4o 35 vs R1 85 vs o1 177 elements (humans 42) | d05 |
| Reasoning model, exploit-from-log | GPT-5-mini perfect on a 5-arm best-arm task | d04 |
| Compact code-built memory (35 agents) | 50.0 to 76.9; 66.7 to 72.2 as extracted | d06 |
| Untried-option list | Helped more than a summary of readings in Wellocate | d08 |
| Positive-only in-context RL | CLINC150 0.104 to 0.648; Banking77 Qwen2.5-7B 6.2% to 72.2% (stochastic) | c16, d20 |
| Thompson widen/deepen tree | MLE-Bench rank 1.3 vs 2.3-3.3; ARC-AGI no gain | d01 |
| Bandit allocation across queries | Up to +11 points at equal compute | d03 |
| LATS UCT vs DFS | HotPotQA EM 0.63 vs 0.42 | c25 |
| Intelligent Go-Explore | Game of 24 100% vs 38+-22 | d21 |

**LLM trees and intrinsic rewards.**

- LATS runs UCT with a model-written value score and reflection. The gains from UCT, LM heuristic and reflection are confounded (removing the LM heuristic gave 0.37 [c25]).
- ELLM and OMNI replace count and prediction-error novelty with a model's goals or interestingness. ELLM: 64.9% of goals sensible [c22]. OMNI: Crafter 82 tasks vs 55 for learning progress [d19].
- ShinkaEvolve uses UCB1 over mutation models and a 0.95 code-embedding novelty filter, ablated on one task [d22].
- Reasoning models: explicit reasoning helps open exploration, yet priors persist [d07], and 35 frontier agents still fail a grid-exploration task, where a memory harness beat free reasoning [d06].

**Gaps that stay open.** No paper re-measures suffix failure on the Krishnamurthy bandit for 2025-2026 frontier models. No paper tests a per-class bandit inside an LLM tree at equal tokens (critique.md gaps 1 and 2). Several 2026 preprints (d06, d07, d08) have model names we could not check. Treat them as single-source.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Never choose a branch or class by greedy mean alone. Give untried or rarely tried children an optimism bonus or a sampled-belief draw, so a lucky first branch cannot lock the tree. | G12 / S6 tree / O-widen | [E] | K01: a05, a24, b04, a16, c03, d01 |
| A2 | Compute per-class tries, passes and coverage in code and show the model the table, not the raw attempt log. The model never counts. | G5 / S0 / S9 | [E] | K03: a27, b19, c05, b20, c07, d06, d07 |
| A3 | Log class coverage per run (share of classes or operators tried at least once) and flag runs below a floor. Models cover only 40-65% of arms. | G5 / S9 | [E] | K14: c10, c11, c17, c18 |
| A4 | Tune the widen threshold or width on held-out pass data and retune on drift. Do not copy a constant from a paper. | O-widen / S0 | [E] | K05: a02, b01, b02, d17, d18 |
| A5 | Gate any "new is good" widen signal on a code check (the candidate runs and the check result reproduces), never on raw diversity, prediction error or a model's "this is novel" opinion. | G8 / S4 / S7 | [E] | K07: a12, b07, c20, a10, b13, a11, d12, d13, d14, d19 |

A1 is the rule (optimism or sampling), not a choice between UCB and Thompson. That choice is a Test-first item (T1).

### Test first (not established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Per-class Thompson sampling with discount (or last-K) to set widen width, vs fixed width and progressive widening. | O-widen / G12 | [S] | K06, K21, K22: a06, b06, d01, d02, d03, d15, d18 |
| T2 | Windowed or discounted statistics for class pass rates, window and gamma from our own history. | S0 / S9 | [S] | K22, K12: d15, d17, d18, a15, a26 |
| T3 | Algorithm-guided widen: decide in code with UCB on class pass counts vs ask the model. Check by model size. | O-widen | [S] | K04: c07, b22, a18 |
| T4 | Forced try-all-once pass across classes or operators before any greedy choice at S6. | S6 / G12 | [S] | K13: c13, c12 |
| T5 | Code sets the re-check rate of noisy checks (fixed share, falling with class count). | G5 / S4 | [S] | K23: d08, d06 |
| T6 | Neutral class ids (letters) in anything the model sees when it makes a widen move. | G5 / S0 | [S] | K24: d07 |
| T7 | Archive of partial solutions with return to the best-scored node vs always from the root. | S6 / memory | [S] | K11: a13, d21 |
| T8 | Thinking mode plus code table vs non-thinking plus code table. | G5 / G12 | [S] | K20: d04, d05, d10, d07 |
| T9 | Keep only successful attempts in the context memory (or subsample) vs all attempts. | memory / S9 | [S] | K17: c15, c16, d20 |
| T10 | Visit-count measure for ideas: entailment clusters vs code-embedding cosine vs compression, checked on paraphrase pairs. | G5 / S3 | [S] | K25: d22, d23, d24, d25 |
| T11 | Paraphrase-noise test of three widen signals (learning progress, re-check agreement, cluster novelty). | G8 / O-widen | [S] | K26: d19, d16, d14, d08, d12 |
| T12 | Sweep UCT exploration weight on our tree; check whether the best weight differs per class. | S6 tree | [S] | K16: b23, d26 |
| T13 | A bandit over modes (direct vs wide search) with a window, per class. | S0 | [S] | K12: a15, a26 |
| T14 | Model-judged interestingness only as a filter on top of a code check. | G8 | [S] | K18: c23, d19, c22 |
| T15 | Episodic-only novelty counts (per item, reset between items). Defensive default, from vision and grid worlds only. | G8 / S3 | [S] | K27: d12, d13 |

No action: K09 (RND numbers), K10 (contested), K15 (old model), K19 (regret bound, sanity check only). Details of each test are in UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms use equal total tokens, including the cost of any extra call an arm adds (node-picking call, judge call, embedding or NLI pass). Use at least 10 seeds or repeats per arm and report the spread, because RND's authors saw 5 and 10 seeds disagree [b09].

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Mixed-class items with a code check; at least 3 classes with different pass rates | Fixed width; progressive widening (k, alpha grid); per-class discounted Thompson | Mean pass rate; variance across classes; share of runs where the solving class never got a second try | Per-class rule at least level, with gains on classes with low but non-zero pass rate. Analogy: AB-MCTS gained on MLE-Bench, level on ARC (d01) |
| B2 (T2) | Offline replay of our logged pass-rate history | Discounted TS (gamma 0.4-0.9), last-K TS (K 5-30), SW-UCB, best fixed class | Cumulative regret vs best fixed class | Windowed rules beat plain TS/UCB1 if rates drift |
| B3 (T3) | Items with 3+ widen choices | Model asked whether to widen; code UCB on class counts | Solved items; widen rate | Code rule better for large models, maybe worse for small (c07) |
| B4 (T4) | Items with 5+ operators or classes | Greedy from S6 start; try-all-once then greedy | Operator coverage; solved items | Higher coverage and some gain, as in Schmied (c13) |
| B5 (T5) | Noisy-check items (flaky tests) | Model decides re-check; code rule with fixed share | Solved items; share of calls spent re-checking | Code rule near the 24-38% scripted level beats 75-94% over-confirming (d08) |
| B6 (T6) | Same items | Descriptive class names vs letters in the widen prompt | Widen rate; solved items | Letters remove prior bias (d07) |
| B7 (T7) | Items where partial progress is possible | Always expand from root; expand from best-scored archived node | Solved items; tokens to first pass | Gain only if failures are lost progress, not wrong ideas (critique gap 6) |
| B8 (T8) | Same items | Thinking vs non-thinking, both with the code table | Widen rate; revisit rate of the solving class; tokens | Thinking raises widening and costs tokens; test net gain at equal tokens |
| B9 (T9) | Items with a retry memory | All attempts vs only passes vs random subsample | Final pass rate | Positive-only best for naive in-context learning (c16) |
| B10 (T10) | 50 same-idea paraphrase pairs and 50 different-idea pairs from our logs | Embedding cosine; entailment clusters; compression distance | AUROC for same vs different | Entailment clusters win (d24); cosine 0.95 acceptable for code |
| B11 (T11) | A failing candidate plus paraphrase-only variants | Widen on learning progress; on re-check agreement; on cluster novelty | Rate of spurious widening; wasted calls | Cluster novelty plus re-check agreement trigger least |
| B12 (T12) | Tree items across 3+ classes | UCT weight w in {0.5, 1, 2} per class | Pass rate per class | Best w differs by class (LATS authors say it depends on the task) |
| B13 (T13) | Items from several classes | Fixed mode vs windowed bandit over modes | Pass rate; regret | Gain if class rates drift |
| B14 (T14) | Open-mode items | "Model says new" vs "code says new and check passes" | Share of wasted children; solved items | Code-backed filter wins (G8) |
| B15 (T15) | Items run in sequence | Carry-over novelty memory vs reset per item | Pass rate; children per item | Reset is level or better (d12, d13) |

## 9. What does not transfer, and why

- **Pixel pseudo-counts, RND and ICM networks.** They train a network on a visual stream over millions of frames. Our trees have a few dozen nodes per item, so there is nothing to fit. Only the idea transfers: a bonus that shrinks with tries.
- **Atari scores as effect sizes.** Montezuma 8,152 vs 2,497 is one game, few seeds, different budgets across papers (critique.md). Not an expected gain for our tasks.
- **Go-Explore numbers.** They need deterministic reset and cell compression. Our tree can reset states for free, so the form transfers. The cost is the node-picking call, not the return, and the numbers do not transfer.
- **Cross-item novelty bonuses.** Procedurally generated worlds break them [d12, d13]. Our items are all different, like procedural levels.
- **Bernoulli independence.** TS and UCB guarantees assume independent pulls on stationary arms. LLM attempts share errors (SCHEMA G4) and class rates drift. The bounds are guidance, not guarantees.
- **Small stationary bandit results for LLMs.** Almost all 2023-2024 LLM evidence uses K=5-10 arms, T=100-200 and older models. Our classes are more numerous and our models newer.
- **Training-based fixes.** SFT/RL on bandit traces (EVOLvE fine-tuning, Schmied RL, Chen 2025) lie outside the no-training rule. In one study they made agents greedier [d09].
- **Model-judged interestingness.** OMNI used GPT-3/4 inside RL training with human examples. G8 says model judges rank ideas near chance. OMNI helps only as a filter on a check.
- **Regret bounds as a budget.** The ln n lower bound is a sanity check only (K19).
- **Overlap with other subfields.** Optimal stopping, retrieval as a bandit, test-time compute scaling, hierarchical planning and creativity as search are covered there.

## 10. Open questions

1. Does a per-class bandit rule (discounted Thompson or windowed UCB on class pass rates) beat fixed width at equal tokens inside an LLM tree? Nothing published. AB-MCTS is nearest, at equal calls and over widen vs deepen [d01].
2. Do 2025-2026 frontier and reasoning models still show suffix failure and the knowing-doing gap? Extended thinking fixes exploit-from-log [d04] and helps open exploration [d05], but no re-measure of the Krishnamurthy bandit exists.
3. What is a visit count for ideas? Entailment clusters are the best candidate [d24]; no paraphrase-invariance test exists.
4. What is the right widen reward: learning progress, reproducibility of the check, or reachability? No head-to-head.
5. Thompson vs UCB with few passes per class and drift: theory only (d17, d18). Window and prior must come from our history.
6. Does archive-and-return help when most failures are wrong ideas, not lost states? Cost at equal tokens unknown.
7. Is the best UCT weight class-dependent? LATS tested one dataset (100 questions, no repeats) [d26].
8. Do Monea (positive-only episodes) and OMNI replicate on other base models, and does the first apply to keeping only successful attempts in memory?
9. Are there neutral replications of RND/ICM outside Atari? Only authors of competing methods were found.
10. Does thinking-mode cost cancel its exploration gain at equal tokens? R1 used far more tokens per trial than GPT-4o [d05].
11. Is the DORA gain (31.43% to 45.5% in TextWorld) directed exploration or action noise [d11]?
12. How much of the 2026 evidence (d06, d07, d08) survives with model names checked and replication?

## 11. Sources

[V] opened (full text or HTML, per the evidence files), [M] snippet only or not opened. Where an evidence line says only the abstract or introduction was read, that limit is stated in the sections above.

- [V] Auer, Cesa-Bianchi, Fischer (2002) Finite-time analysis of the multiarmed bandit problem. https://homes.di.unimi.it/cesa-bianchi/Pubblicazioni/ml-02.pdf
- [M] Auer et al. (2002) journal page. https://doi.org/10.1023/A:1013689704352
- [M] Lai and Robbins (1985) Asymptotically efficient adaptive allocation rules. https://doi.org/10.1016/0196-8858(85)90002-8
- [M] Thompson (1933) On the likelihood that one unknown probability exceeds another. https://doi.org/10.1093/biomet/25.3-4.285
- [V] Russo, Van Roy, Kazerouni, Osband, Wen (2018/2020) A Tutorial on Thompson Sampling. https://arxiv.org/abs/1707.02038
- [V] Kaufmann, Korda, Munos (2012) Thompson Sampling: an asymptotically optimal finite-time analysis. https://arxiv.org/abs/1205.4217
- [M] Chapelle and Li (2011) An empirical evaluation of Thompson sampling. https://papers.nips.cc/paper/2011/hash/e53a0a2978c28872a4505
- [M] Kocsis and Szepesvari (2006) Bandit based Monte-Carlo planning. https://doi.org/10.1007/11871842_29
- [V] Kuleshov and Precup (2014) Algorithms for the multi-armed bandit problem. https://arxiv.org/abs/1402.6028
- [M] Sutton and Barto (2018) Reinforcement Learning: An Introduction. http://incompleteideas.net/book/the-book-2nd.html
- [M] Schmidhuber (2010) Formal theory of creativity, fun, and intrinsic motivation. https://doi.org/10.1109/TAMD.2010.2056368
- [V] Bellemare et al. (2016) Unifying count-based exploration and intrinsic motivation (abstract and introduction only). https://arxiv.org/abs/1606.01868
- [V] Pathak et al. (2017) Curiosity-driven exploration by self-supervised prediction. https://arxiv.org/abs/1705.05363
- [V] Burda et al. (2018) Large-scale study of curiosity-driven learning. https://arxiv.org/abs/1808.04355
- [V] Burda et al. (2019) Exploration by random network distillation. https://arxiv.org/abs/1810.12894
- [V] Savinov et al. (2019) Episodic curiosity through reachability. https://arxiv.org/abs/1810.02274
- [V] Ecoffet et al. (2019/2021) Go-Explore. https://arxiv.org/abs/1901.10995
- [V] Badia et al. (2020) Never Give Up (skimmed; numbers not parsed). https://arxiv.org/abs/2002.06038
- [V] Badia et al. (2020) Agent57. https://arxiv.org/abs/2003.13350
- [V] Krishnamurthy, Harris, Foster, Zhang, Slivkins (2024) Can large language models explore in-context? https://arxiv.org/abs/2403.15371
- [V] Nie et al. (2024/25) EVOLvE. https://arxiv.org/abs/2410.06238
- [V] Schmied et al. (2025) LLMs are greedy agents. https://arxiv.org/abs/2504.16078
- [V] Park et al. (2024/25) Do LLM agents have regret? (skimmed; not cross-checked). https://arxiv.org/abs/2403.16843
- [V] Monea et al. (2025) LLMs are in-context bandit reinforcement learners. https://arxiv.org/abs/2410.05362
- [V] Binz and Schulz (2022/23) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576
- [V] Du et al. (2023) Guiding pretraining in RL with LLMs (ELLM). https://arxiv.org/abs/2302.06692
- [V] Zhang, Lehman, Stanley, Clune (2023/24) OMNI. https://arxiv.org/abs/2306.01711
- [V] Zhou et al. (2023/24) Language Agent Tree Search. https://arxiv.org/abs/2310.04406
- [V] Inoue et al. (2025) Wider or deeper? Adaptive branching MCTS. https://arxiv.org/abs/2503.04412
- [V] Zuo and Zhu (2026) Strategic scaling of test-time compute: a bandit learning approach. https://arxiv.org/abs/2506.12721
- [V] Harris and Slivkins (2026) Should you use your LLM to explore or exploit? https://arxiv.org/abs/2502.00225
- [V] Pan, Xie, Wilson (2025) Large language models think too fast to explore effectively. https://arxiv.org/abs/2501.18009
- [V] Anonymous (2026) Exploration and exploitation errors are measurable for language model agents. https://arxiv.org/abs/2604.13151
- [V] Semantic Bandits authors (2026) Semantic Bandits. https://arxiv.org/abs/2608.16707
- [V] Wellocate authors (2026) Explore or confirm? https://arxiv.org/abs/2610.25111
- [V] Chen et al. (2025) When greedy wins (abstract and introduction only). https://arxiv.org/abs/2509.24923
- [V] Grams et al. (2025) Disentangling exploration of LLMs by optimal exploitation (abstract and introduction only). https://arxiv.org/abs/2501.08925
- [V] Gurjar et al. (2026) DORA Explorer. https://arxiv.org/abs/2604.17244
- [V] Raileanu and Rocktaschel (2020) RIDE. https://arxiv.org/abs/2002.12292
- [V] Henaff, Raileanu, Jiang, Rocktaschel (2022) Exploration via elliptical episodic bonuses. https://arxiv.org/abs/2210.05805
- [V] Matiisen et al. (2017) Teacher-student curriculum learning. https://arxiv.org/abs/1707.00183
- [V] Graves et al. (2017) Automated curriculum learning for neural networks. https://arxiv.org/abs/1704.03003
- [V] Garivier and Moulines (2008/11) UCB policies for non-stationary bandits. https://arxiv.org/abs/0805.3415
- [V] Raj and Kalyani (2017) Taming non-stationary bandits. https://arxiv.org/abs/1707.09727
- [V] Lu et al. (2025) Intelligent Go-Explore. https://arxiv.org/abs/2405.15143
- [V] Lange et al. (2025) ShinkaEvolve. https://arxiv.org/abs/2509.19349
- [V] Tam et al. (2022) Semantic exploration from language abstractions. https://arxiv.org/abs/2204.05080
- [V] Kuhn, Gal, Farquhar (2023) Semantic uncertainty. https://arxiv.org/abs/2302.09664
- [V] Shaib et al. (2024) Standardizing the measurement of text diversity. https://arxiv.org/abs/2403.00553

Cross-check note. The cross-checker re-opened Krishnamurthy, EVOLvE, Schmied, RND, LATS, Savinov and Go-Explore (critique.md). Monea and OMNI were re-opened in the gap search. Park 2024, Binz-Schulz and Du 2023 were not re-opened by the cross-checker.
