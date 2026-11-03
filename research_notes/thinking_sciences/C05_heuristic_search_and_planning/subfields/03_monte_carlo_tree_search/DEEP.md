# Monte Carlo tree search: deep document

*Subfield C05.03 of heuristic search and planning. Built from evidence_a-d.jsonl (a01-a29, b01-b33, c01-c31, d01-d18), claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids are cited in brackets. Where the critique corrected an earlier line, the corrected figure is used here.*

## 1. What it is

Monte Carlo tree search (MCTS) builds a search tree one simulation at a time. Each simulation has four steps.

1. **Select.** Start at the root. At each node pick a child by a counted rule until you reach a node that is not fully expanded.
2. **Expand.** Add one (or a few) new child nodes.
3. **Simulate.** Estimate the value of the new node. Classic MCTS plays a random game to the end (a rollout). Modern versions use a learned value, a checker, or an LLM's opinion instead.
4. **Back up.** Push the result up the path to the root. Each node keeps a visit count and a value estimate.

After the budget is spent, act on the root's best child (most visited, or best value).

The core idea is that the selection rule is a bandit rule. UCT applies UCB1 at every node: choose the child with the highest `mean value + c * sqrt(ln(parent visits) / child visits)`. The first term exploits. The second term explores children that have few visits. The tree grows toward promising lines but never fully drops a line [a01, a03].

Why it matters for our agent:

- It is a **control** pattern. A program (not the model) decides where to spend the next unit of thinking, using counts.
- It puts a number on the **value of exploration**: when is one more try on a new branch worth more than another try on the best branch?
- It is the most-cited search method behind recent scaffold papers (Tree of Thoughts is a cousin; RAP, LATS, rStar, rStar-Math, MCTSr and SWE-Search use MCTS proper).

The honest summary, up front: MCTS is a strong idea when there is a real value signal and a deep problem. For LLM reasoning at equal tokens, it often does **not** beat simple repeated sampling plus a checker. Most published gains compare tree search with 10-50 iterations against one chain.

## 2. History and theories in depth

### 2.1 Bandit roots: Auer, Cesa-Bianchi and Fischer (2002)

UCB1 picks the arm with the best mean reward plus `sqrt(2 ln t / s)`. Theorem 1: the expected number of pulls of a suboptimal arm j is at most `8 ln n / Delta_j^2` plus a constant, for rewards in [0,1], any n, uniform over time (not only in the limit). In their experiments on 8 reward distributions (2, 3, 5 and 10 arms), the variance-aware UCB1-TUNED was best nearly everywhere. Epsilon-greedy was near-best only when its constant was tuned, and it degraded fast when it was not [a01, a02]. Limit: the theorem needs i.i.d. rewards per arm. In a tree the reward below a node drifts as the tree grows, so the theorem does not carry over directly.

### 2.2 UCT: Kocsis and Szepesvari (2006)

UCT puts UCB1 in every internal node of a tree built from rollouts. To handle drift, the bonus is `2 * Cp * sqrt(ln t / s)` with a constant Cp chosen so drift conditions hold (Cp = 1/sqrt(2) in the proof). Theorem 1 generalises the UCB1 bound to drifting payoffs: `16 Cp^2 ln n / (Delta_i/2)^2 + 2 N0 + pi^2/3`, where N0 can be huge. Theorem 6 (finite-horizon MDP, rewards in [0,1]): the bias of the root estimate is O(log n / n) when the bonus is scaled by horizon D. The failure probability at the root falls at a **polynomial** rate, not an exponential one [a03, a04, b03, c01].

Experiments [a05, a06, b01, b02, b04, c01, c02]:

- **P-game** (random minimax trees; move values in [0,127] for MAX, [-127,0] for MIN; win by sign of summed values). Two shapes: branching 2 depth 20, and branching 8 depth 8. Each point is 200 trees x 200 runs. UCT reaches a low failure rate in about the same leaf count as alpha-beta, order B^(D/2). Plain Monte Carlo plateaus at a significant failure rate. Minimax-updated MC (MMMC) is worse than plain MC at small budgets. So the bandit selection, not the tree alone, produces the gain.
- **Sailing** (stochastic shortest path, 7 actions per state, grids 2x2 to 40x40, error target below 0.1, averaged over 1000 random states). UCT needed far fewer simulator samples than ARTDP and PG-ID and scaled better with size. UCT needed a hand-set heuristic bias multiplier of 10, and the paper says this domain lies outside its theory. ARTDP's exploration was also tuned, so tuning is on both sides.
- Caveats: synthetic domains only; the bias term was changed from the proven form to a depth-decayed form for the experiments; one reward model.

### 2.3 The name "Monte-Carlo tree search": Coulom (2006)

Coulom's Crazy Stone (9x9 Go) selected moves by an estimated probability of being best (not UCB). It used a backup that moves from averaging toward max as visits grow [b05, b06].

- Match results (100 games, 95% CI): Crazy Stone (5 min) vs Indigo 2005 (8 min) 61% (+/-4.9). Versus GNU Go 3.6 level 10: 25% (+/-4.3) at 4 min, 32% (+/-4.7) at 8 min, 36% (+/-4.8) at 16 min per game. Win rate vs GNU Go stayed below 50%; neighbouring CIs overlap. It won the 10th KGS computer-Go tournament.
- Backup test (Table 1): mean squared error against the value found with 2x the simulations. At 128 simulations: mean 6.44, max 41.70, robust max 39.60, mix 5.29. At 131,072 simulations: mean 2.84, max 1.83, robust max 1.88, mix 2.05. Mean is better early, max late, and a mix is best across the range. Caveat: the reference value is itself computed with the mix operator, which favours mix.
- The earlier line a07 (not opened) is superseded by b05 and b06, as the critique notes.

### 2.4 Domain knowledge without slowing the search: Chaslot et al. (2008)

Two devices [a08, a09]:

- **Progressive bias.** Add `H_i / (n_i + 1)` to the selection score. The prior dominates when a child is new and fades with visits.
- **Progressive unpruning.** Start with few children and add more as the parent's visits grow.

Results in the Go program Mango (heuristic H from patterns learned on 2,000 professional games, 89,119 patterns; 20,000 simulations per move; opponent GNU Go):

| Setting | None | Bias only | Unpruning only | Both |
|---|---|---|---|---|
| 9x9, level 10 | 33.2% (1000 games) | 37.2% | 58.3% (1000) | 61.7% (2000) |
| 13x13 | 8.5% | 15.6% | 30.0% | 35.1% (500 each) |
| 19x19, level 0 | 0% (200) | 3.1% | 4.8% | 48.2% (500) |

The 19x19 gain is super-additive: each device alone gives little, both together reach near parity. The critique re-checked the 9x9 values. Column alignment for bias-only and 13x13 was not re-checked.

### 2.5 Refinements named but not opened

RAVE (Gelly and Silver; estimate a move's value from all simulations where it appeared later), the Browne et al. (2012) survey, and AlphaGo (policy prior plus value network, 5-0 against Fan Hui) were recorded from memory only [a10, a11, a13]. Treat them as context, not evidence.

### 2.6 The worst case: Coquelin and Munos (2007)

Opened this session [d08]. On a deceptive tree, where a branch that looks better early hides the true best branch, UCT can take a number of rounds that is a tower of exponentials in depth D. Example tree: the decoy branch pays (D-1)/D at every leaf; the optimal branch pays 1. Time to first see the optimal reward is Omega(exp(exp(D))) for a square-root bonus, and D-1 nested exponentials for a log bonus. Asymptotic regret is still O(log n) or O(sqrt n). Their fixes: a modified UCT whose bonus grows with depth (regret exponential in depth, order 2^D, but safe in the worst case) and BAST (uses smoothness). Correction from the critique: use the forms above, not a loose "hyper-exponential". The arXiv id is cs/0703062. No LLM reasoning-tree study checks whether natural trees look like this.

### 2.7 Learned policy and value: AlphaZero and MuZero

- **AlphaZero** (Silver et al. 2017/2018) [a14, a15, b07-b09, c03, c04]: MCTS with a network prior and value, no rollouts, no human data, 800 simulations per move in training. 100-game matches at one minute per move: chess vs Stockfish 28 wins, 72 draws, 0 losses (white 25W/25D/0L; black 3W/47D/0L). Shogi vs Elmo 90-2-8. Go vs the 3-day AlphaGo Zero 60-40 (31-19 as white, 29-21 as black). Search speed: about 80 thousand positions/s (chess) and 40 thousand (shogi) versus 70 million (Stockfish) and 35 million (Elmo). It beat Stockfish after 4 hours (300k steps) of self-play on 5,000 first-gen TPUs. The authors' explanation for why averaging beats minimax with noisy values (errors cancel in the mean; alpha-beta passes the largest error to the root) is an argument, not an ablation. Hardware and time controls were disputed outside the paper.
- **MuZero** (Schrittwieser et al. 2020) [a16, a17, b10, b11, c05]: MCTS inside a learned latent model with no rules given. 800 simulations on boards, 50 on Atari. It beat R2D2 on 42 of 57 Atari games and SimPLe on all 57. Reanalyze reached 731% median human-normalised score vs 192% (IMPALA), 231% (Rainbow), 431% (LASER). In Go, planning scaled about two orders of magnitude beyond training search. In Atari, performance plateaued near 100 simulations. Even 6 simulations per move gave a useful policy on Ms. Pacman (single-game ablation, no CIs), and a model-free Q-learning variant learned slower and ended lower.

### 2.8 Theory versus practice

The guarantees are asymptotic with large constants and polynomial failure rates [b03, d08]. At LLM budgets of 10-50 rollouts they say almost nothing. Use them as design motivation only (claim K02).

## 3. Core findings with exact numbers

Status: E = established (2+ independent sources), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| UCT matches alpha-beta convergence on random trees; beats plain MC and MMMC | order B^(D/2) iterations; B=2 D=20 and B=8 D=8; 200 trees x 200 runs | Kocsis and Szepesvari 2006 [a05, b01, b02, c01] | S (K01) |
| UCT guarantees are asymptotic, polynomial rate | root failure ~ C(1/t)^(rho*(Delta/2)^2) | Kocsis 2006; Coquelin and Munos 2007 [b03, d08] | E (K02) |
| UCT worst case on deceptive trees | Omega(exp(exp(D))) rounds, square-root bonus | Coquelin and Munos [d08] | S (K29) |
| Prior with fading weight plus gradual widening | Go 19x19 0% to 48.2%; 9x9 33.2% to 61.7% | Chaslot 2008 [a08, a09] | S (K03) |
| Backup: mean early, max late, mix best | MSE at 128 sims: mean 6.44, max 41.70, mix 5.29; at 131,072: 2.84, 1.83, 2.05 | Coulom 2006 [b06] | S (K04) |
| Learned policy+value MCTS beats top alpha-beta engine at 1/1000 the positions | 28-72-0 vs Stockfish; 80k vs 70M pos/s | AlphaZero [a14, c03] | S (K05) |
| Returns from search budget saturate | MuZero Atari ~100 sims; rStar-Math by 64 trajectories; RAP-style by ~4 rollouts (LLaMA3-8B-Instruct) | MuZero; rStar-Math; rStar [a16, b27, c14] | E (K06) |
| Planning with explicit state model: MCTS far above CoT | LLaMA-33B 4-step 0.86-0.88 vs 0.02; Llama-2-70B full set Easy 0.65 vs 0.08, Hard 0.51 vs 0.05; 602 cases | RAP [a18, a20, c06, c08] | S (K07); compute not matched |
| Math/logic: edge over self-consistency small or none at equal compute | GSM8K RAP 48.8 vs CoT+SC(10) 46.8; TS-LLM: CoT-SC beats tree search on GSM8K at equal tokens | RAP; TS-LLM; Wu et al. [a19, b15, b20, c21, b24] | E (K08) |
| Compute-matched on MATH, MCTS loses to simpler schemes | MCTS dozens of times more tokens; Mistral-7B MATH500 sampling 256 samples 42.8% (8.70e14 FLOPs) vs REBASE 32 samples 45.0% (1.36e14); about 7x less compute | Wu 2024; Snell 2024 [b24, c18, c17] | E (K09) |
| Search helps hard, hurts easy | beam search worse than best-of-N on levels 1-2 at high budget, better on 3-4; 72B policy: best-of-N wins at every level | Snell; Liu; Chen [b23, d04, d05, d07] | E (K10, K27) |
| Value source decides gain | LATS HotPotQA EM 0.63 vs 0.37 without LM heuristic vs 0.42 DFS; Game24 prompted value 9.2-21.0 vs learned 64.8 | LATS; TS-LLM [a23, c11, c20] | E (K11) |
| With an executable check, tree search over attempts helps | LATS HumanEval 83.8 (GPT-3.5), 92.7 (GPT-4, +1.7 over Reflexion); SWE-Search +23% relative; PG-TD 26.70 vs 25.19 | LATS; SWE-Search; PG-TD [a22, c10, c26, c27] | E (K12) |
| LATS numbers internally inconsistent | k=50 LATS 0.63 vs 0.61; ToT 0.55 vs 0.39 vs 0.49 across tables | LATS [a21, a23, c11] | C (K13) |
| Best-first agent search scales with budget | VWA 18.9 to 26.4; WA 15.0 to 19.2; subset 24.5 to 32.0 (5) to 37.0 (20) | Koh 2024 [b29, b30, c25] | S (K14) |
| Small model + MCTS + independent check | LLaMA2-7B 12.51 to 63.91; Mistral-7B 17.89 to 81.88; LLaMA3-8B-Instruct 74.53 to 91.13; ~167 calls, 367k tokens/question; SC@maj128 reaches 23.05 / 52.84 / 67.55 / 84.69 / 88.68 | rStar [a25, c13] | S (K15) |
| MCTS + trained process model, self-evolved | Qwen2.5-Math-7B 58.8 to 90.0 MATH; AIME 53.3% (8/15); step-reward MCTS 88.2-89.4 vs ORM best-of-N 82.6 | rStar-Math [b26, b27, c24, d12] | S (K16); needs training |
| Process-reward search does not beat SC at first | iteration 1 no; later 48.5 vs 42.5; verifier +3.6 on GSM8K (83.9 to 87.5) | ReST-MCTS* [b28, c15, d13] | S (K17) |
| MCTS is better as teacher than run-time engine | MCTS-DPO +5.9 GSM8K, +5.8 MATH, +15.8 ARC-C; TS-LLM 51.9 to 56.5 | Xie; Feng; AlphaMath [b21, b32, c22] | E (K18) |
| DeepSeek abandoned MCTS for training | no numbers; value model hard to train | DeepSeek-R1 [b31, d06] | S (K19) |
| Repeated sampling + verifier is a strong rival | SWE-bench Lite 15.9% to 56% (250 samples); MATH Llama-3-8B coverage 82.9% (100) to 98.44% (10,000), vote only 40.50% to 41.41% | Large Language Monkeys [b33, c29, d15] | E (K20) |
| Wide action spaces need a prior | VirtualHome: plain UCT poor in all conditions; LLM prior in PUCT won | Zhao 2023 [c28]; cf. Chaslot [a09] | S (K21) |
| Generic reflection adds little | LATS no-reflection 0.58 vs 0.63; WebShop reflections generic | LATS [a23, a24] | S (K22) |
| Self-rated whole-answer MCTS looks strong, not compute-matched | MCTSr LLaMA3-8B GSM8K 74.07 to 93.03 (4 rollouts) / 96.66 (8) | MCTSr [c16] | C (K23) |
| Frontier non-reasoning models, equal 27 calls | LiveCodeBench GPT-4o/DeepSeek-V3: RS 37.8/40.7, MCTS 36.7/43.2; ARC-AGI Pass@2 RS 15.0/18.6, MCTS 9.0/14.0 | AB-MCTS [d01] | S (K24) |
| Reasoning models + executable score | ARC-AGI-2, 120 tasks: o4-mini 23% to 27.5%; multi-model over 30% | AB-MCTS [d02] | S (K25) |
| No UCT-constant sweep exists in LLM MCTS | LATS w=0.5 0.55 vs w=1 and w=2 0.63; width 3/5/10: 0.429/0.432/0.402 | LATS; AB-MCTS; TS-LLM [d03, d09, d10, d11] | E (K26) |
| Internal search in long-CoT models reduces need for external MCTS | 1,953% more tokens on a trivial item; first answer right in over 92%; QwQ 48.6% fewer tokens at equal accuracy | Chen 2024; DeepSeek; s1 [d06, d07, d17] | S (K28) |
| Token overhead of agent MCTS | SWE-Search about 5x API cost (GPT-4o 14x: 40.86 to 576.00 USD) | SWE-Search [d14] | S (K30); table alignment inferred |
| Training on MCTS traces gives small, uneven gain | LLaMA-3-8B-Instruct avg 29.02 vs few-shot 28.99 | ReST-MCTS* [d13] | S (K31) |

## 4. Mechanisms and models

### 4.1 The loop, as an engineer would write it

```
node = {state, parent, children[], visits N, total_value W}
repeat until budget (tokens, calls, or rollouts) is spent:
    # SELECT
    n = root
    while n is fully expanded and not terminal:
        n = argmax over children c of  W_c/N_c + C * sqrt( ln(N_n) / N_c )     # UCT
    # EXPAND
    if not terminal: add child(ren) of n (one action each), pick one -> n
    # SIMULATE / EVALUATE
    v = rollout(n)  OR  value_net(n)  OR  checker(n)  OR  LLM_score(n)
    # BACK UP
    for a in path(n -> root): a.N += 1; a.W += v        # mean backup
act on: argmax child of root by visits (robust) or by W/N
```

Choices that matter, with the evidence for each:

- **Selection constant C.** Classic UCT uses C near sqrt(2) (Cp = 1/sqrt(2) in the proof gives 2*Cp = sqrt(2)); SWE-Search uses 1.41 [d14]. No LLM paper sweeps it [K26]. In LATS, exploration weight 0.5 hurt (0.55 EM) while 1 and 2 were equal at 0.63 on 100 HotPotQA questions, one seed [d10]. In bandit tests an untuned epsilon-greedy degraded fast, so treat C as a tunable [a02].
- **Width (children per node).** Matters more than C. LiveCodeBench with DeepSeek-V3, fixed width: w=3 0.429, w=5 0.432, w=10 0.402 (std 0.015-0.021) [d02, d03]. TS-LLM Game24: larger width almost doubled performance (43.8 to 80.7; which method is uncertain) [d09]. Koh: depth and breadth must grow together; 1/1 24.5%, 5/5 35.5-37.0% [b30].
- **Unbounded children.** AB-MCTS argues UCT cannot be applied to LLM answer trees as-is, since a generate node can always produce one more child and unexpanded children have no score. They use Thompson sampling over a Bayesian score model to choose between going wider and deeper [d03]. Progressive widening (Chaslot's progressive unpruning) is the classic UCT-compatible fix [a08].
- **Prior.** Progressive bias `H/(n+1)` or PUCT (policy prior times sqrt(N)/(1+n)) lets a cheap proposal ranking steer early visits. In wide spaces plain UCT fails [a09, c28]. AlphaMath uses PUCT-style selection with a value head [a27].
- **Backup.** Mean at few simulations, max or a mix at many [b06]. LLM trees run at 4-64 rollouts, which is the mean regime. LATS and RAP use mean-style backup.
- **Value source.** Four kinds appear: (a) random rollout to terminal (classic, Go); (b) learned value network (AlphaZero, TS-LLM 64.8 on Game24); (c) executable check or answer match (LATS tests, rStar-Math round 1, AB-MCTS demonstration-case score); (d) the LLM's own opinion (RAP self-evaluation, LATS LM score, MCTSr self-rating, Marco-o1 token-confidence). Reliability falls roughly in this order, and the evidence says gains follow it [K11].
- **Action set.** rStar uses five human-like actions: propose one step, propose the rest, sub-question, re-answer, rephrase. Growing the action space helped step by step on 200 GSM8K questions with LLaMA3-8B: A3 only (RAP-style) 70.5; adding A5 72.5; A4 73.5; A2+A3+A4+A5 74.0; all five 75.0. Steps of 1-2 points are within about +/-3 points noise [a26]. This is the closest published relative of our operator tree (O1-O8).
- **Final answer choice.** rStar picks by agreement between the generator's trace and a second small model completing a masked prefix [a25, d16]. RAP and LATS pick the highest-reward trace, or aggregate over the tree (RAP-Aggregate about +3 on GSM8K [a19]). AlphaMath and rStar-Math move to step-level beam search or a process model at inference.
- **Reflection.** LATS adds an LLM-written reflection on failed trajectories to later prompts. Ablation: 0.63 to 0.58 without it; reflections on WebShop were often generic [a23, a24].
- **Environment rollback.** LATS, Koh and SWE-Search need to revert to an earlier state. The authors list this as a limitation [a21, c25].

### 4.2 Why counted selection helps

Uniform sampling spreads budget evenly, so it wastes visits on clearly bad branches. A confidence bound shifts visits to branches that look good, but keeps a shrinking bonus on neglected ones. On random trees this took UCT from a plateau (plain MC) to alpha-beta-like convergence [b01]. The same shape appears in Go: a prior that fades (progressive bias) and a width that grows (progressive unpruning) were both needed on 19x19 [a09].

### 4.3 Why it can fail

- **Noisy value over-exploited.** Beam search and lookahead push toward high PRM scores. On easy items at high budget this lowered accuracy below best-of-N [b23, d04]. This is Goodhart's law on a learned verifier.
- **Deceptive early values.** The Coquelin-Munos worst case [d08]. A plausible wrong step scored high early can hold the visits for a very long time.
- **Same-model samples are alike.** Tree search explores fewer distinct sentences than plain sampling. TS-LLM gives this as the cause of CoT-SC beating tree search on GSM8K at equal tokens [b20].
- **Rollout cost.** Each simulation is an LLM generation; MCTS used dozens of times more tokens than sampling in Wu et al. [c18].

## 5. What holds up

### 5.1 Replications and independent confirmations

- **Saturation of budget** (3 sources): MuZero, rStar-Math, rStar on RAP [K06]. Established.
- **Search helps middle difficulty, not easy** (Snell, Liu, Chen) [K10, K27]. Established, but difficulty estimation cost was never charged (Snell used 2048 samples per question to build bins) [d04].
- **Tree search is not clearly better than sampling at equal tokens for arithmetic and logic** (RAP vs SC close; TS-LLM; Wu; Snell) [K08, K09]. Established.
- **Value quality decides gain** (LATS ablation, TS-LLM prompted vs learned, rStar dropped self-reward for small models) [K11]. Established.
- **MCTS as teacher beats MCTS as engine** (MCTS-DPO, TS-LLM, AlphaMath) [K18]. Established.
- **Repeated sampling plus a verifier is a strong rival** (Large Language Monkeys; echoed in AB-MCTS) [K20]. Established.

### 5.2 Failed or weak results, boundary conditions

- **Compute-matched failures.** Wu et al. dropped MCTS after it lost to sampling at every budget on MATH with Llemma-7B and 34B [b24]. Snell found lookahead generally below beam search and best-of-N at equal generation cost (they argue lookahead stands for MCTS and did not run full MCTS) [b22, c17]. AB-MCTS: with GPT-4o and DeepSeek-V3 at 27 calls, fixed-width MCTS was equal to repeated sampling on code (36.7 vs 37.8; 43.2 vs 40.7) and worse on ARC-AGI (9.0 vs 15.0; 14.0 vs 18.6) [d01]. Gains of 1-3 points are about one std (stds 0.3-3.6, 5 runs).
- **DeepSeek-R1 gave up MCTS** for training: the token space is too large, per-node extension caps gave local optima, and a fine-grained value model is hard to train. MCTS with a pre-trained value model still helped at inference. No numbers [b31, d06].
- **ReST-MCTS\*** iteration 1 did not beat self-consistency [b28]. Self-training on its traces gave LLaMA-3-8B-Instruct 29.02 vs few-shot 28.99 average [d13].
- **PG-TD** gain over sampling plus filtering is about 1.5 points (26.70 vs 25.19) on small fine-tuned GPT-2 [c27].
- **LATS WebShop**: still below fine-tuned agents and humans (SR 38.0 vs 45.0 IL+RL and 59.6 expert); reflections generic [a24, c10].
- **RAP saturation conflict.** rStar says RAP-style MCTS saturates after about 4 rollouts. RAP's own paper shows RAP(20) above RAP(10) on Blocksworld (0.42 vs 0.26 at 6 steps). Different models and tasks [c14, c06].
- **Internal inconsistency in LATS** (K13): treat margins of 2-6 points over RAP and ToT as not firm.
- **Baseline errors fixed by the critique.** rStar's abstract "36.46% to 81.88%" for Mistral-7B mixes baselines. 36.46 is SC@maj8; few-shot CoT is 17.89.
- **Small samples.** rStar ablations use 200 questions (about +/-3 points). AIME 53.3% is 8 of 15 problems. AIME in rStar-Math has 30 problems. AlphaZero matches are 100 games.
- **No true replication papers.** Failed replications of LLM-MCTS as such are rare. The negative evidence is compute-matched comparisons, not replication attempts.

### 5.3 Moderators (what changes the result)

| Moderator | Direction | Evidence |
|---|---|---|
| Real check available | gain much larger | LATS code, SWE-Search, AB-MCTS demonstration cases [a22, c26, d02] |
| Value from model opinion | gain small or fragile | LATS ablation; TS-LLM; rStar [a23, c20, a26] |
| Problem depth | tree wins on deep (Game24, chess, Blocksworld), ties or loses on shallow (GSM8K) | TS-LLM; RAP [b19, d09, a20] |
| Difficulty | helps medium, wastes on easy, little on hardest | Snell; Liu; Chen [d04, d05, d07] |
| Model size | 72B policy: best-of-N best at every level; under 7B: best-of-N on easy, beam on hard | Liu [d05] |
| Model type | external gain on non-reasoning models is null at equal calls; small gain on reasoning models with an executable score | AB-MCTS [d01, d02] |
| Action space width | plain UCT fails without a prior | Chaslot; Zhao [a09, c28] |
| Training allowed | the big gains need training (rStar-Math, AlphaMath, ReST-MCTS*, MCTS-DPO) | [K16, K18] |

### 5.4 What worked and what did not (interventions)

Worked: counted selection (vs uniform); a fading prior with gradual widening; a real checker as the value; diversified actions (rStar); an independent second check for the final answer; budget ceilings near the knee; tree search as a data generator.

Did not work or unproven: UCT constant tuning (no data); LLM self-rating as sole value (weak); generic reflection; RAP-style single-action MCTS beyond 4 rollouts; MCTS at equal tokens against sampling on MATH and GSM8K.

## 6. Language models

### 6.1 Evidence by task type

**Planning with an explicit state (RAP, Blocksworld)** [a18, a20, c06, c08, b14]. LLaMA-33B success at 2/4/6 steps: CoT 0.17/0.02/0.00; CoT pass@10 0.23/0.07/0.00; RAP(10) 1.00/0.86/0.26; RAP(20) 1.00/0.88/0.42; GPT-4 CoT 0.50/0.63/0.40. Full 602-case set, Llama-2-70B: Easy CoT 0.08 vs RAP(10) 0.65; Hard 0.05 vs 0.51. By steps (2,4,6,8,10), Easy RAP(10) is 1.00/0.99/0.75/0.61/0.32 and Easy CoT is 0.49/0.18/0.06/0.01/0.01. Hard RAP(10) by steps is 0.67/0.76/0.74/0.48/0.17. The LLM acts as its own world model. The action-likelihood reward is vital for planning but not helpful for math. Not compute-matched (10-20 iterations vs one chain), though CoT pass@10 is also low. GPT-4 CoT at 6 steps (0.40) matches RAP(20) (0.42).

**Math and logic** [a19, b15, c07, b19, b20]. RAP GSM8K: CoT 29.4, CoT+SC(10) 46.8, RAP single trace 48.8 (b15 lists RAP(1) 48.6 and RAP(10) 51.6; unresolved), about +3 with aggregation. ProntoQA: RAP 94.2 prediction / 78.8 proof vs CoT 87.8 / 64.8, CoT+SC 89.8 (20 iterations vs 20 samples). TS-LLM path@1: GSM8K greedy 41.4, BFS-V 52.5, MCTS-alpha 51.9, MCTS-Rollout 47.8, CoT-SC-ORM 52.3. Game24 greedy 12.7, BFS-V 64.8, MCTS-alpha 63.3, MCTS-Rollout 71.3. ProntoQA greedy 48.8 vs 94.4 / 99.4. Chess endgame win rate 57.8 greedy vs 96.9 MCTS. Tree depth reached 64 versus 10 in ToT and 7 in RAP. At equal tokens: Game24 MCTS 69.34 at 649 tokens vs CoT-SC-ORM 50.6 at 684 tokens; GSM8K CoT-SC-ORM 52.3 at 500 tokens vs BFS-V 52.5 at 485 [d18]. Needs a trained value and outcome reward model.

**Tree of Thoughts (breadth-first, no backup)** [b12, b13, c09]. Game of 24, GPT-4, 100 games: IO 7.3%, CoT 4.0%, CoT-SC k=100 9.0%, best-of-100 CoT 49%, ToT b=1 45%, ToT b=5 74%. GPT-3.5 ToT only 19%. GPT-4 generation plus GPT-3.5 evaluation 64%; the reverse 31%, so generation is the bottleneck. Cost: ToT 5.5k completion tokens vs 6.7k for 100 CoT trials. Crosswords: word-level 60% vs under 16%. Note that best-of-100 CoT at 49% is a strong equal-cost rival that ToT only clearly beats at b=5.

**Code** [a22, b16, c10, c27, d01]. LATS HumanEval pass@1 (5 samples per expansion, 8 iterations): GPT-3.5 CoT 46.9, ReAct 56.9, Reflexion 68.1, ToT 54.4, RAP 63.1, LATS 83.8; GPT-4 base 80.1, Reflexion 91.0, LATS 92.7. MBPP (GPT-3.5): LATS 81.1 vs RAP 71.4, Reflexion 70.0. It uses model-written tests (4) as feedback; real tests only for final pass@1. PG-TD: beam 11.95, sampling plus filtering 25.19, SMCG-TD 24.10, PG-TD 26.70.

**Question answering and shopping** [a21, a23, a24, c10, c11, b17, b18, d10]. HotPotQA (GPT-3.5, n=5, k=50, EM): CoT 0.34, CoT-SC 0.38, ToT 0.55 (reasoning table), RAP 0.60, LATS(CoT) 0.62. Acting: ReAct 0.32, Reflexion 0.51, ToT(ReAct) 0.39, RAP(ReAct) 0.54, LATS(ReAct) 0.63, LATS(CoT+ReAct) 0.71. Best-of-250 ReAct 0.42; CoT-SC k=250 0.40; LATS n=1,k=50 0.48. Ablations: no LM heuristic 0.37, DFS 0.42, no reflection 0.58. Tokens upon success only: ToT 210,215, RAP 176,500, LATS about 173-176k (tables disagree on row order). WebShop (50 tasks): ReAct 53.8/28.0, Reflexion 64.2/35.0, LATS 75.9/38.0, fine-tuned 67.5/45.0, expert 82.1/59.6. Game of 24 (GPT-3.5): CoT 0.08, Reflexion 0.12, ToT 0.20, RAP 0.40, LATS(CoT) 0.44.

**Agents in real environments** [b29, b30, c25, c26, d14]. Best-first search (not UCT): VWA 18.9 to 26.4 (+39.7% relative, 910 tasks); WA 15.0 to 19.2 (+28.0%, 812 tasks); Llama-3-70B on WA 7.6 to 10.1. Subset budgets: none 24.5, 5 expansions 32.0, 20 expansions 37.0. Up to 20x more LM calls; depth 5, breadth 5. SWE-Search (UCT with depth bonus and penalty; max 100 iterations, 3-5 expansions per node), SWE-bench Lite: GPT-4o 25.7 to 31.0, GPT-4o-mini 13.0 to 17.0, Qwen-2.5-72B 18.0 to 24.7, DeepSeek-V2.5 16.3 to 21.0, Llama-3.1-70B 13.6 to 17.7. Mean relative gain 23%. Cost about 5x for four models, 14x for GPT-4o (alignment inferred).

**Small models plus rich MCTS (rStar, MCTSr)** [a25, c13, c14, c16]. rStar needs about 167 calls and 367k tokens per GSM8K question, and about 4.5 days on one A100 per model for the full set. The fair rival SC@maj128 is 23.05 / 52.84 / 67.55 / 84.69 / 88.68 against rStar 63.91 / 81.88 / 85.52 / 91.13 / 90.67 (LLaMA2-7B, Mistral-7B, LLaMA3-8B, LLaMA3-8B-Instruct, Phi3-mini). The gap shrinks for strong models (Phi3-mini 88.68 vs 90.67). Generator@maj alone was 27.22 on LLaMA2-7B, so part of the gain is the discriminator. MCTSr on LLaMA3-8B GSM8K (1319 problems): zero-shot CoT 74.07, one-turn self-refine 86.96, 4 rollouts 93.03, 8 rollouts 96.66. GSM-Hard: 25.47 / 33.36 / 39.88 / 45.49. Self-rating by the same model, and no SC match.

**MCTS plus training (not scaffold-only)** [a27, b26, b27, b32, c22, c23, c24, d11, d12]. rStar-Math: Qwen2.5-Math-7B MATH 58.8 to 90.0; Phi3-mini 41.4 to 86.4 (o1-preview 85.5, o1-mini 90.0); AIME 53.3% (8/15) vs o1-preview 44.6 and o1-mini 56.7; Omni-Math 50.5 vs 60.5. By round, MATH: 58.8, 75.2, 86.6, 87.0, 89.4; AIME 0, 10.0, 43.3, 46.7, 50.0. Round 1 had no learned reward (answer match plus code execution). Table 8 (MATH/AIME/AMC/OlympiadBench): ORM best-of-N 82.6/26.7/65.0/55.1; PQM MCTS 88.2/46.7/85.0/62.9; PPM MCTS 89.4/50.0/87.5/65.3. Method and reward type change together, so the table cannot separate them. It needed 747k problems and four rounds. AlphaMath (DeepSeekMath-Base 7B): 2-shot 59.7/33.2 (assumed GSM8K/MATH); greedy 73.5/53.6; SBS B1=1 81.1/62.8; SBS B1=3 84.1/66.3. On MATH: greedy 53.62, maj@5 61.84, SBS B1=1 62.80, B1=2 64.66, B1=3 66.30. MCTS with 40 simulations scored higher than SBS(B1=1) but was slowest. Tian et al.: Llama-2-70B GSM8K 57.8 to 92.0; WizardMath-70B MATH 20.7 to 51.0. MCTS-DPO: Mistral-7B GSM8K 81.8 (+5.9), MATH 34.7 (+5.8), ARC-C 76.4 (+15.8). Marco-o1: MGSM +6.17% English, +5.60% Chinese over base, not compute-matched, reward is token-confidence.

### 6.2 What changed the results, by how much

| Change | Effect |
|---|---|
| Replace MCTS with DFS (LATS) | 0.63 to 0.42 (-0.21) |
| Remove LM heuristic (LATS) | 0.63 to 0.37 |
| Prompted value to learned value (TS-LLM Game24, LLaMA policy) | 9.2 / 21.0 to 64.8 |
| Single action to five actions (rStar, 200 questions) | 70.5 to 75.0 |
| 5 to 20 expansions (Koh) | 32.0 to 37.0 |
| Width 10 to 5 (AB-MCTS) | 0.402 to 0.432 |
| ORM best-of-N to PPM MCTS (rStar-Math) | MATH 82.6 to 89.4 (confounded) |
| Add independent verifier (ReST-MCTS* value on SC) | GSM8K 83.9 to 87.5 |

### 6.3 Reasoning models and internal search

Long-CoT models do their own search. QwQ-32B-Preview and R1 spend 1,953% more tokens than conventional models on "2+3", and the first solution is right in over 92% of cases. A self-training fix cut tokens 48.6% at equal accuracy on MATH500 (about 93%). 76-80% of QwQ cases used 2 to 4 solution rounds [d07]. R1: AIME 2024 Pass@1 79.8%, Pass@64 90.0%, majority vote 86.7%. DeepSeek calls R1 more token-efficient than majority voting or MCTS because it allocates tokens by difficulty [d06]. s1-32B: AIME24 50.0 without budget forcing, 53.3 with 2x Wait, up to 56.7. REBASE with a 34B PRM scaled better than majority voting on AIME24, but the reward-model compute was not counted [d17]. The only external-search gain on reasoning models is AB-MCTS on ARC-AGI-2 (o4-mini 23% to 27.5%, 120 tasks, about 5 tasks) [d02]. No token-matched test of UCT on a frontier reasoning model exists.

## 7. What our agent should take

Format: item | schema part | status | evidence ids. The schema already has the idea tree at S6 (O1-O8; at most 3 children, depth 2, 2 expansions) and G12 (spend by difficulty). The MCTS evidence mostly supports and sharpens these rules. It does not support a general MCTS engine.

### Add now (established)

1. **Search only where there is a real check, and score branches with the check, not the model's opinion.** Schema part: G2/G3, S4, S6 tree. **[E]** K11, K12, K20. Evidence: a23, c11, c20, a22, c26, d15. This already follows from G2 and G3. Add the wording to the S6 tree rules: a child's score is its test result, never its self-rated quality.
2. **Equal-token best-of-N plus checker is the default rival; a tree must beat it.** Schema part: G7. **[E]** K08, K09, K20. Evidence: b24, c18, d01, d15, b33. This is G7 applied to search; log it as the standing arm.
3. **Cap the search budget at the knee.** Schema part: G12 and the S6 tree rules. **[E]** K06. Evidence: a16, b27, c14. Practical range 16-64 rollouts. The existing cap (2 expansions, depth 2, 3 children) is well inside it and should stay.
4. **Gate search on difficulty: skip it on easy items.** Schema part: G12, S0. **[E]** K10, K27. Evidence: b23, d04, d05, d07. Beam and lookahead over-optimise a verifier on easy items. The gate already exists in S0 (plain pass rate); keep search off in "direct" mode. The cost of a better gate is uncharged in the literature, so only the existing cheap signals (plain pass rate, agreement) are justified.
5. **Treat search as a producer of verified traces, not as a run-time engine.** Schema part: memory. **[E]** K18. Evidence: b21, b32, c22. S9 already stores one lesson line. Storing verified solution traces is the same idea, but the training-free version is untested (see Test first).
6. **Do not use UCT guarantees as justification for a design.** Schema part: G12 note. **[E]** K02. Evidence: b03, d08.

### Test first

| Item | Schema part | Status | Evidence | Why not add yet |
|---|---|---|---|---|
| Counted UCB selection among the operator children at S6, versus uniform split | O / S6 | [S] K01 | a05, b01, b02 | Proven on synthetic trees only. With 3 children and 2 expansions the tree is too small for UCB to differ from uniform |
| Fading prior over children (cheap-model ranking, weight decays with visits) | O / S6 | [S] K03, K21 | a08, a09, c28 | Go and VirtualHome only; no LLM-reasoning test |
| Diversified action set (rStar five actions) plus independent second check for the final choice | O, S7 | [S] K15 | a25, a26, c13, d16 | Gain over SC@maj128 is small for strong models; part of the gain is the discriminator |
| Mean vs max vs mixed backup of branch scores | S6 | [S] K04 | b06 | Go-only; at 4-32 rollouts mean should do |
| Depth cap and restart vs uncapped tree under a misleading early score | G, S6 | [S] K29 | d08 | Theory only |
| Explore constant and width sweep | O | [S] K26 | d03, d10 | No data; width matters more than c |
| Executable-score tree search on ARC-style items at equal calls | S4, S6 | [S] K24, K25 | d01, d02 | Gain is about 5 tasks of 120 on reasoning models; null on non-reasoning |
| Search vs longer single thinking on a reasoning model | G11, G12 | [S] K28 | d06, d07, d17 | No token-matched evidence |
| Retrieve verified traces as few-shot memory vs none | memory | [S] K31 | d13 | Only indirect evidence |
| Reflection text in the tree | S5 | [S] K22 | a23, a24 | Generic reflection gave little; G1 and section 4b already warn |
| Whole-answer self-rated MCTS (MCTSr style) | none | [C] K23 | c16, c30 | Self-rating, not compute-matched; conflicts with G5 |

Do not add: a full MCTS engine over the whole problem; self-rated values as the selection signal; trained value or process reward models (need training); RAP-style single-action MCTS beyond 4 rollouts.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (count every generated and prompt token, including setup, scoring calls and failed runs). Report accuracy per 100k tokens. Use at least 5 runs per arm and report std; require a gap above one std. Log per schema section 6.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style items with a demonstration-case check (30-120 items) | (a) repeated sampling plus check, N calls; (b) small tree with check-scored children, same N; (c) current S6 tree | Pass@k vs calls up to 50; solved items | Tree gains a few items on reasoning models (about +4 points); null on non-reasoning models |
| T2 | Code items with executable tests (HumanEval or LiveCodeBench style, 40+) | sample-and-test vs LATS-lite tree vs best-of-N | pass@1 at equal tokens | Within one std; tree a small plus at best |
| T3 | Math/logic subset (GSM8K/MATH, 40-100, mixed difficulty) | best-of-N with checker or vote vs tree with checked value | accuracy at equal tokens; split easy/medium/hard | Tree equal or worse on easy; small gain on medium |
| T4 | Same items, gated vs always-on search | always search vs S0 gate (plain pass rate or 3-sample agreement) | accuracy at equal total tokens including gate cost | Gated better on easy, equal on hard |
| T5 | Planning items with explicit state (Blocksworld-like, 6+ steps) | best-of-N chains vs search with explicit state tracking | success rate by plan length | Large tree gain at 6+ steps where chains collapse |
| T6 | 40 items, fixed 16 rollouts | sweep c in {0.5, 1, 1.41, 2} and width in {3, 5, 8} | accuracy; visits to best branch | Width matters more than c; flat curve in c |
| T7 | S6 branches (O1-O8) on impasse items | counted UCB vs uniform split vs fixed order | solved subgoals per token | Small; tree too small for UCB to matter |
| T8 | Items with a misleading early score (plant a plausible wrong first step scored high) | depth-capped tree vs uncapped vs restart | rollouts to recovery | Cap or restart recovers faster |
| T9 | Reasoning-model items (AIME style, 30) | external tree vs same tokens as longer thinking vs parallel votes | accuracy | External search no better than internal at equal tokens |
| T10 | Memory | 3 retrieved verified traces per class as few-shot vs none | accuracy at equal tokens | Small positive on same-class items |
| T11 | Prior | flat expansion vs cheap-model prior with decay after n visits | solved per 100k tokens on wide-branching items | Gain when branching factor is high; none when 3 |
| T12 | Cost accounting | all arms | tokens on failed runs as well as successes | Reveals hidden overhead (LATS reports tokens only on success) |

## 9. What does not transfer, and why

- **Asymptotic guarantees.** Polynomial failure rate and huge constants. They are useless at 10-50 rollouts [b03, d08].
- **Rollouts to the end.** In Go a random playout is cheap. An LLM rollout is a full generation, and MCTS used dozens of times more tokens [c18].
- **Learned value networks and PRMs.** The big wins (rStar-Math, AlphaMath, ReST-MCTS*, TS-LLM, AlphaZero) need training. A scaffold-only agent cannot use them. Prompted value is much worse (9.2-21.0 vs 64.8 on Game24).
- **Self-play and self-evolution** (747k problems, four rounds). Not available at inference.
- **Perfect simulators.** Go, chess and Atari have exact rules or a trained model. LLM states need a world model that the LLM writes itself (RAP), and it can be wrong.
- **Environment rollback.** LATS, Koh and SWE-Search need to revert state. Many tasks cannot.
- **Unbounded children.** UCT needs a finite action set; LLM answer trees can always add one more child [d03].
- **The mean-vs-max Go result** (Coulom). Go-specific; the reference was computed with the mix operator.
- **Headline "7B beats o1".** It rests on training, small evaluation sets (AIME 15 or 30 problems) and unequal compute.
- **Same-model sample diversity.** Trees over one model's samples explore fewer distinct options, which weakens the exploration idea itself [b20]. This is consistent with G4.

## 10. Open questions

1. Does UCT beat best-of-N plus checker at equal tokens on a frontier reasoning model (2025-2026)? Only AB-MCTS (not UCT) tested it.
2. What C and rollout budget work for LLM trees? No sweep exists.
3. Can a cheap difficulty gate be tested end to end, with its cost charged?
4. Can a non-learned value (executable test, constraint check, independent second-model check) replace a PRM at inference with all else fixed? rStar-Math round 1 (75.2 vs 89.4) confounds fine-tuning.
5. Do reasoning models still gain from external MCTS, or is internal search enough?
6. How do REBASE or step beam compare with MCTS at equal tokens outside MATH (planning, code, agents)?
7. What is the true token overhead of tree bookkeeping (state text, reflections)? Reporting is inconsistent.
8. Does the deceptive-tree worst case appear in LLM trees, and do restarts or depth caps fix it?
9. Does storing MCTS-found verified traces in memory without training match training gains?
10. Unreconciled numbers: RAP GSM8K 48.8 (single trace) vs RAP(1) 48.6 and RAP(10) 51.6; AlphaMath GSM8K 84.1 not verified; LATS Table 11 row order ambiguous.

## 11. Sources

[V] = opened and read as text. [M] = recorded from memory or snippet only.

- [V] Auer, Cesa-Bianchi, Fischer (2002) Finite-time analysis of the multiarmed bandit problem. https://homes.di.unimi.it/cesa-bianchi/Pubblicazioni/ml-02.pdf
- [V] Kocsis and Szepesvari (2006) Bandit based Monte-Carlo planning. http://ggp.stanford.edu/readings/uct.pdf
- [V] Coulom (2006) Efficient selectivity and backup operators in Monte-Carlo tree search. https://www.remi-coulom.fr/CG2006/CG2006.pdf
- [V] Chaslot, Winands, van den Herik, Uiterwijk, Bouzy (2008) Progressive strategies for Monte-Carlo tree search. https://dke.maastrichtuniversity.nl/m.winands/documents/pMCTS.pdf
- [M] Gelly and Silver (2011) Monte-Carlo tree search and rapid action value estimation in computer Go. https://www.cs.utexas.edu/~pstone/Courses/394Rfall16/resources/mogo-rave.pdf
- [M] Browne et al. (2012) A survey of Monte Carlo tree search methods. http://mcts.ai/pubs/mcts-survey-master.pdf
- [V] Coquelin and Munos (2007) Bandit algorithms for tree search. https://arxiv.org/abs/cs/0703062 (opened as d08)
- [M] Silver et al. (2016) Mastering the game of Go with deep neural networks and tree search. https://www.nature.com/articles/nature16961
- [V] Silver et al. (2017/2018) Mastering chess and shogi by self-play with a general RL algorithm (AlphaZero). https://arxiv.org/abs/1712.01815
- [V] Schrittwieser et al. (2020) MuZero. https://arxiv.org/abs/1911.08265
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Hao et al. (2023) Reasoning with language model is planning with world model (RAP). https://arxiv.org/abs/2305.14992
- [V] Zhou et al. (2023) Language Agent Tree Search (LATS). https://arxiv.org/abs/2310.04406
- [V] Feng et al. (2023/2024) AlphaZero-like tree-search can guide LLM decoding and training (TS-LLM). https://arxiv.org/abs/2309.17179
- [V] Zhang et al. (2023) Planning with LLMs for code generation (PG-TD). https://arxiv.org/abs/2303.05510
- [V] Zhao et al. (2023) LLMs as commonsense knowledge for large-scale task planning. https://arxiv.org/abs/2305.14078
- [V] Qi/Wang et al. (2024) Mutual reasoning makes smaller LLMs stronger problem-solvers (rStar). https://arxiv.org/abs/2408.06195
- [V] Chen/Liao et al. (2024) AlphaMath Almost Zero. https://arxiv.org/abs/2405.03553
- [V] Zhang et al. (2024) ReST-MCTS*. https://arxiv.org/abs/2406.03816
- [V] Zhang et al. (2024) MCT Self-Refine (MCTSr). https://arxiv.org/abs/2406.07394
- [V] Tian et al. (2024) Toward self-improvement of LLMs via imagination, searching and criticizing. https://arxiv.org/abs/2404.12253
- [V] Xie et al. (2024) MCTS boosts reasoning via iterative preference learning. https://arxiv.org/abs/2405.00451
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Wu et al. (2024) Inference scaling laws (REBASE). https://arxiv.org/abs/2408.00724
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Koh et al. (2024) Tree search for language model agents. https://arxiv.org/abs/2407.01476
- [V] Antoniades et al. (2024/2025) SWE-Search. https://arxiv.org/abs/2410.20285
- [V] Hu et al. (2024) Marco-o1. https://arxiv.org/abs/2411.14405
- [V] Chen et al. (2024) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187
- [V] Guan et al. (2025) rStar-Math. https://arxiv.org/abs/2501.04519
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948
- [V] Muennighoff et al. (2025) s1: simple test-time scaling. https://arxiv.org/abs/2501.19393
- [V] Liu et al. (2025) Can 1B LLM surpass 405B LLM? https://arxiv.org/abs/2502.06703
- [V] Inoue et al. (2025) Wider or deeper? Adaptive branching MCTS (AB-MCTS). https://arxiv.org/abs/2503.04412

Links to other subfields in this run (not covered here): Pruning of decision trees; MCTS limits; Chain-of-thought prompting; Count-based exploration; Active inference decision theory; Learned refinement and self-verification; Hitting-set tree search; Process models.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 10 established claims: 8 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C05.03-K02** (reworded: the sources support less). Sources show asymptotic polynomial-rate failure and a double-exponential worst case for UCT, but Kocsis-Szepesvari only say 'some constant C' (no huge constants are shown), and the LLM-budget implication is the researcher's inference. Corrected claim: UCT guarantees are asymptotic: root failure probability falls at a polynomial rate with an unspecified constant, and Coquelin and Munos show a worst case needing exp(exp(D)) rounds before the best branch is first seen; the paper does not analyse budgets of tens of rollouts, so treat the theory as design motivation only.
- **C05.03-K26** (reworded: the sources support less). A universal negative contradicted by its own evidence: LATS does report a 3-value exploration-weight ablation (w=0.5, 1, 2); and 'width matters more than c' is unsupported, since the 0.432 vs 0.402 width gap (std ~0.015-0.02, w=3 gives 0.429) was never compared against any c effect. Corrected claim: Few LLM-MCTS papers sweep the UCT constant: LATS ablates the exploration weight at three values on HotPotQA (w=0.5 gave 0.55 EM vs 0.63 at w=1; w=2 gave no gain), TS-LLM chose c_init from only {0.3, 3.0}, and SWE-Search uses c=1.41 with no sweep found. For fixed-width MCTS on LiveCodeBench (DeepSeek-V3) width 5 scored 0.432, width 3 0.429 and width 10 0.402, so performance is sensitive to width at least at the larger setting.
- **C05.03-K20** (now single-source: only one opened source, code check).
