# Computer chess and game AI: deep document

Scope: alpha-beta search, Monte Carlo tree search (MCTS), self-play, and the 2020-2026 work that moves these ideas to language models (LLMs). Schema target: S6 (impasse and tree search). Evidence ids (a01-a25, b01-b28, c01-c27, d01-d24) and claim ids (E16.09-K01 to K33) refer to the jsonl files in this folder. Status marks: [E] established, [S] single-source, [C] contested.

Overlap note: progressive deepening and the human thought process are in subfield 01; pattern-recognition theory of search in 06; chunks and templates in 05. Not repeated here. Linked parallel subfields (not covered here): test-time compute scaling, hierarchical planning, resource-rational and value-of-computation work, replay as offline simulation (Dyna), bandit-style exploration, overthinking, self-correction.

## 1. What it is

Computer game AI is the study of programs that choose moves by looking ahead through a tree of positions. Three families matter for us.

1. **Alpha-beta minimax** (Deep Blue, Stockfish). Exhaustive search to a fixed depth with exact pruning. It needs a fast, hand-built or learned evaluation at the leaves.
2. **Monte Carlo tree search** (Go programs, AlphaGo, AlphaZero, MuZero). Grow a tree selectively. Pick the next branch with a bandit rule (UCT). Score leaves by random rollouts or by a learned value net. Back the score up the tree.
3. **Self-play learning** (AlphaGo Zero, AlphaZero, MuZero, KataGo). The program plays itself, search produces better move targets than the raw network, the network is trained on those targets, and the loop repeats.

Why it matters to our agent. S6 of the schema opens a small idea tree at an impasse (at most 3 children, depth 2, 2 expansions). Game AI is the largest body of evidence about when a tree beats plain sampling, how much it costs, how it fails, and what makes it work: a cheap guide (policy), a good evaluator (value), and, above all, a trustworthy outcome check. The 2020-2026 LLM work (Tree of Thoughts, RAP, LATS, rStar-Math, Snell, Koh and others) tests the same ideas on frozen or lightly trained language models. The result is mixed, and the mix is the lesson: search helps when the model has a foothold and the evaluator is trustworthy, and it often loses to best-of-N at equal tokens when it is not.

What the agent cannot copy: training loops, perfect simulators, millions of rollouts. What it can copy: search shape, budget allocation, move ordering (try likely children first), pruning rules that stay exact, and an adversarial check on searched answers.

## 2. History and theories in depth

**Alpha-beta (1950s-1975).** Invented several times (McCarthy, Brudno 1963; Newell and Simon noted it was "reinvented a number of times"). Knuth and Moore (1975) gave the analysis. It returns exactly the minimax value. Worst case is the same as minimax, O(b^d). With perfect move ordering the best case is about O(b^(d/2)): twice the depth for the same work (a01; the paper itself was not opened). All the engineering is move ordering: captures first, killer moves, iterative deepening, transposition tables.

**Deep Blue (1996-1997).** Lost 2-4 in 1996, won 3.5-2.5 in 1997 (2 wins, 3 draws, 1 loss). About 200 million positions per second, about double 1996. 30 PowerPC processors plus 480 custom chess chips, an evaluation with about 8,000 parts, an opening book of over 4,000 positions drawn from 700,000 grandmaster games. Typical depth 6 to 8 moves, 20 or more on some lines (a02, Wikipedia summary; the 2002 paper was blocked). Lesson: brute force plus human-built knowledge. No learning.

**UCT and the Go problem (2006-2015).** Kocsis and Szepesvari (2006) put a bandit rule (UCB1) at every tree node. On synthetic P-game trees (B=2, D=20 and B=8, D=8; 200 trees, 200 runs each) UCT reached near-zero failure in about as many leaf nodes as alpha-beta, and was faster if a small error rate was accepted. Iterations needed grow about like B^(D/2), the same as alpha-beta (a03). So MCTS is not a free lunch on small trees. Go was different: branching about 250, no good hand evaluation. MoGo (Gelly et al., 2006) applied UCT to Go; by 2008 it reached dan level on 9x9; by 2011 all top programs used MCTS and played like a good amateur on 19x19 (a04, a22). Browne et al. (2012) also note trap states, where a single refuting reply is missed by averaging, which hurts UCT in chess-like tactics (d21).

**AlphaGo (2015-2017).** 5-0 over Fan Hui (Oct 2015), 4-1 over Lee Sedol (March 2016) (a07). In game 4 the value estimate stood near 70% at move 79 after Lee's move 78, collapsed at move 87, and bad moves followed until resignation under 20% (a24; Wikipedia only). AlphaGo Zero used no human games: it beat AlphaGo Lee 100-0 and AlphaGo Master 89-11, passing Lee in 3 days (about 4.9M self-play games) (a07).

**AlphaZero (2017-2018).** One algorithm for chess, shogi, Go from the rules only. 100-game match vs Stockfish at 1 min/move: 28 wins, 72 draws, 0 losses (25W 25D 0L as White; 3W 47D 0L as Black). It passed Stockfish after about 4 hours (300k steps). It searched about 80,000 positions per second against 70 million for Stockfish (c01, a05, b02). Shogi vs Elmo: 90W 2D 8L. Go vs 3-day AlphaGo Zero: 60W 40L. Critics: Stockfish ran with 64 threads, 1 GB hash and no opening book at fixed time. The 2018 Science rematch (1,000 games, 3 h + 15 s per move, Stockfish 9 with 44 cores, Syzygy tables, 32 GB hash) gave 155 wins, 6 losses, 839 draws; the report said Stockfish needed about 10-to-1 time odds to match (a06). The margin shrank, the direction held.

**MuZero (2019-2020).** Learns its own model instead of using the rules. Matched AlphaZero in chess, shogi and Go with 800 simulations per move (50 in Atari). Atari, 57 games: Reanalyze variant 731% median human-normalised score against 192%, 231%, 431% for prior methods (a08, b04).

**KataGo and its blind spot (2019-2025).** KataGo cut compute about 50x versus comparable methods (about 1.4 GPU-years to pass ELF OpenGo, which took about 74) (a21). Wang et al. (2023) trained adversaries that beat it more than 97% of the time with superhuman search and more than 99% with no search, using under 14% of KataGo's training compute. The cyclic adversary won 95.7% at 4,096 visits and 72% at 10 million visits (only 50 games at that setting). The exploit transferred zero-shot to Leela Zero, ELF OpenGo, Sai and Golaxy (a19, a20, b23, c04). Tseng et al. (2025): defences held against the original adversary (47% for a fine-tuned version), but new adversaries won again (92% after fine-tuning; 42% at 65,536 visits against the strongest defended victim, with the adversary using 26% of the victim's compute; a ViT victim 78%) (b24, d23).

**Searchless distillation (2024).** Ruoss et al. trained transformers on 15.3 billion Stockfish action-values (about 530 million board states, 10M games). The 270M model has tournament Elo 2299 and Lichess blitz 2895 against humans (a10). This showed that most of search's output can be cached in weights, with limits (section 5).

**Language models enter (2022-2026).** First, chess as a state-tracking test (Toshniwal 2022; Karvonen 2024; ChessGPT 2023). Then search wrapped around LLMs: Tree of Thoughts (2023), RAP (2023), LATS (2023-24), AlphaZero-like tree search (TS-LLM, 2023), rStar-Math (2025), ReST-MCTS* (2024), Searchformer (2024). Then the corrective wave: Snell et al. (2024), Wu et al. (2025), Liu et al. (2025), Brown et al. (2024), Koh et al. (2024/26), and the reasoning-model era (R1, Illusion of Thinking, Yue et al.). Section 6 covers all of it.

**Competing explanations of why MCTS won in Go but not in chess until learned evaluation.** (1) Branching factor: huge branching defeats exhaustive alpha-beta. (2) Evaluation: chess had cheap material-based evaluation that works at shallow depth; Go did not. (3) Tactical trap states favour exact search in chess (d21). All three fit; none was isolated in a controlled experiment (K22).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Alpha-beta is exact minimax with pruning | Best case about b^(d/2) vs b^d; twice the depth at equal work | Knuth-Moore 1975 via a01 | [S] (paper not opened) |
| Deep Blue beat Kasparov by brute force | 3.5-2.5 in 1997 (2W 3D 1L); 1996 lost 2-4; about 200M positions/s; about 8,000 eval parts | a02 (Wikipedia) | [S] |
| UCT matches alpha-beta in nodes on P-games | B=2 D=20 and B=8 D=8; 200 trees x 200 runs; iterations grow about B^(D/2) | Kocsis and Szepesvari 2006 (a03) | [E] (with Browne survey a04) |
| AlphaZero beat Stockfish with 1000x fewer nodes | 28W 72D 0L in 100 games; 80k vs 70M positions/s; beat Stockfish after about 4 h | Silver 2017 (c01, b02) | [E] |
| Fairer rematch still a clear win | 155W 6L 839D in 1,000 games; 3 h + 15 s/move | AlphaZero 2018 via a06 | [E] (secondary source) |
| AlphaZero scaled better with thinking time than alpha-beta | Figure 2, Elo vs time, relative to 40 ms engine; no per-doubling number | c02, a23 | [S] read from figure |
| Pure self-play suffices | AlphaGo Zero 100-0 over Lee, 89-11 over Master; MuZero matches AlphaZero with 800 sims, no rules | a07, a08, b04 | [E] |
| Search adds large Elo on top of a strong net | Leela 2292 policy-only, 2418 value-only, 2858 with 400 sims; AlphaZero 1777, 1992, 2470; puzzles AZ 56.1/82.0/95.6%, Leela 88.6/95.9/99.6% | Ruoss 2024 (a11, b07) | [S] |
| Train-time and test-time compute trade off | Each 10x train compute allows about 15x less test compute at equal strength (Hex); 2,800 snapshots | Jones 2021 (a09, b12) | [S] one game |
| Searchless 270M transformer | Tournament 2299; blitz 2895 vs humans; 2299 vs bots; puzzles 95.4% (136M: 2259, 94.5%; 9M: 2025, 88.9%); oracle 2713; GPT-3.5-turbo-instruct 1755 vs bots, 66.5% puzzles | Ruoss 2024 (a10, b06-b08, c17) | [S] |
| Distilled model fails off-distribution | Fischer random 1539 vs bots against 2054 standard (9M model): minus 515 | Ruoss 2024 (a12, d22) | [S] |
| LLM as policy, value and world model in MCTS | MAV alone 2923 (mean) / 2875 (max); MAV+MCTS 500 sims 3170, 1000 sims 3191; 100 sims = +68 internal Elo; Connect Four up to +244; 14,689 chess games | Schultz 2025 (a13, b09, b11, c18) | [S] |
| LLM-written internal search (breadth up to 4, depth 2) | Elo about 2870 to 2930 with more tokens; shape correct in 99.6% of 5,980 positions; games stopped at +1200 cp because the model shuffled pieces | Schultz 2025 (a14, b10) | [S] |
| Tree of Thoughts, Game of 24 (GPT-4, 100 games) | IO 7.3, CoT 4.0, CoT-SC k=100 9.0, IO best-of-100 33, CoT best-of-100 49, ToT b=1 45, b=5 74 (%) | Yao 2023 (a15, b16, c06) | [S] |
| Generator vs evaluator strength | GPT-4/GPT-4 74%; GPT-4 gen + GPT-3.5 eval 64%; GPT-3.5 gen + GPT-4 eval 31%; GPT-3.5 both 19% | Yao 2023 App. B (b17, c07) | [S] |
| RAP on Blocksworld (LLaMA-33B) | 2/4/6 steps: CoT 0.17/0.02/0.00; RAP(20) 1.00/0.88/0.42; GPT-4 CoT 0.50/0.63/0.40 | Hao 2023 (a16, c08) | [C] |
| LATS on HumanEval | GPT-3.5: CoT 46.9, ReAct 56.9, Reflexion 68.1, ToT 54.4, RAP 63.1, LATS 83.8; GPT-4: base 80.1, Reflexion 91.0, LATS 92.7 | Zhou 2023 (c09, b20) | [C] |
| rStar-Math | MATH Qwen2.5-Math-7B 58.8 to 90.0; Phi3-mini 41.4 to 86.4 (o1-preview 85.5); AIME24 53.3 | Guan 2025 (b21) | [C] needs training |
| Learned value beats prompted value | LLaMA-SFT policy: prompted LLaMA 9.2, prompted GPT-3.5 21.0, learned value 64.8 (one task) | Feng 2023 (a17, b18) | [S] |
| Equal-token edge of tree search is small vs CoT-SC with ORM vote on GSM8K | "largely decrease"; tree search still ahead on other four tasks | Feng 2023 (b19) | [S] |
| Lookahead/MCTS-like search lost to best-of-N at equal budget; compute-optimal allocation gives about 4x efficiency | Budgets 4-256; beam search degrades on easy MATH items; small model beats 14x larger where base success is non-trivial | Snell 2024 (b13, b15, c12, d07) | [E] (with d06, d08) |
| Best test-time method depends on policy size and difficulty | 72B policy: best-of-N best at every level; 7B-32B: beam/diverse tree better on hard items | Liu 2025 (d06) | [E] |
| Rollout-free reward-balanced tree beats classic MCTS | 7B + REBASE matches 34B at about 2x fewer FLOPs | Wu 2025 (d08) | [S] |
| Tree search beats re-ranking in resettable web tasks | GPT-4o VWA subset: d1/b1 24.5; d2 b5 32.0 (+31%); d5 b5 35.0 (+43%); budget 20 37.0 (+51%); re-ranking about 30 and plateaus near 7 runs; Llama-3-70B 7.6 to 16.7; GPT-4o 18.9 to 26.4 | Koh 2026 (d09, d10) | [S] |
| Selection, not generation, is the bottleneck without a verifier | Coverage 82.9% to 98.44% (100 to 10,000 samples); vote/reward-model selection 40.50% to 41.41%; SWE-bench Lite with verifier 15.9% to 56% at 250 samples | Brown 2024 (d11) | [E] |
| Plan diversity beats repeated sampling | PlanSearch pass@200 77.0% vs 60.6% | Wang 2024 (d12) | [S] |
| Optimising against a learned evaluator eventually hurts | Best-of-n gold reward follows d(alpha - beta d) in sqrt(KL) | Gao 2023 (d13); Snell (d07) | [E] |
| RL reasoning does not make wide sampling redundant | R1 AIME24 pass@1 79.8, pass@64 90.0, majority vote 86.7 (%); RL models win at small k, base models at large k (k up to 256) | R1 (d02); Yue 2025 (d03) | [E] |
| Thinking models overthink easy items | Win at medium, lose at low, collapse at high complexity; collapse disputed as token-limit and impossible-instance artefact (River Crossing impossible for N>5) | Shojaee 2025 (d04); Lawsen 2025 (d05) | [C] |
| Reasoning models still fail long-horizon planning | o1: 600 Blocksworld 97.8%; Mystery (randomised names) 52.8%; 110 larger problems (20-40 steps) 23.63%; classical planner solves all | Valmeekam 2024 (d15) | [S] |
| Superhuman search has blind spots | >97% adversary win with search, >99% without; 72% at 10^7 visits over 50 games; defences fail on re-attack | Wang 2023; Tseng 2025 (a19, d23) | [E] |
| Value collapse in game 4 | About 70% at move 79, drop at 87, resign below 20% | a24 | [S] |
| Strong engines do not predict human moves | Stockfish 33-41%; Maia 46-52%; 10 MCTS rollouts lowered matching | McIlroy-Young 2020 (b25) | [S] |
| Chess-trained GPT builds a linear board code | Probe 99.6%; legal moves 99.8% (16 layer), 99.6% (8 layer); win vs Stockfish level 0 (about 1300 Elo) 64% / 46% | Karvonen 2024 (c15, b26) | [E] with c14, c16 |
| Chess fine-tuning lifts state tracking | LLaMA-7B 29.5/39.3/53.0 vs ChessGPT-Base 99.5/97.7/98.1 (real, short/med/long) | Feng 2023 (c16) | [S] |
| Frontier LLMs play chess badly in a harness | Best o3 (low) about 758 Elo vs Dragon levels; random agent -122; 71.1% of 76 models had abnormal finishes; 64.79% of failures wrong actions (62.1% format/tool, 37.9% illegal) | LLM Chess 2025 (d16, d17) | [S] |
| Searchless trace training | Searchformer: 93.7% unseen Sokoban solved, up to 26.8% fewer steps than A*; 5-10x smaller model | Lehnert 2024 (a18, b27) | [S] |
| Token-level MCTS did not scale | Qualitative; no win rates given | R1 appendix (d01) | [S] |

## 4. Mechanisms and models

### 4.1 Minimax and alpha-beta (exact)
- Value of a node: max over children for the mover, min for the opponent. Leaves scored by an evaluation.
- Keep two bounds (alpha: best the maximiser can already force; beta: best the minimiser can already force). When alpha >= beta, stop exploring that node. The value is unchanged.
- Move ordering sets the gain. Try the move most likely to be best first. Iterative deepening gives the order for free: the best move at depth d is tried first at depth d+1.
- Pruning is exact only if the leaf scores are exact. With a noisy LLM evaluator a hard cut can discard the true best branch (a01 agent note). Use soft pruning: drop a branch only on a code-counted check, never on a model's opinion of it.

### 4.2 UCT and MCTS
Four steps per iteration.
1. **Select.** From the root, at each node choose the child maximising mean_value + c * sqrt(ln(N_parent) / n_child). The second term is the exploration bonus. Unvisited children are tried first.
2. **Expand.** Add one or more children at the leaf reached.
3. **Evaluate.** Random rollout to the end (classic), or a value net (AlphaZero), or an LLM judging the state.
4. **Back up.** Add the result to every node on the path (flip sign for the opponent).

Final move: most-visited child at the root. AlphaZero's variant adds a prior from a policy net: the bonus is c * P(child) * sqrt(N_parent) / (1 + n_child). The prior is what lets 80k positions/s beat 70M: the net directs visits to a few promising moves (c01: "compensates for the lower number of evaluations by using its deep neural network to focus much more selectively").
Known weaknesses: averaging hides single refutations (trap states, d21); a rollout on a task with no end state yields unfinished solutions (Wu, d08). The formulas above are the standard published forms; the exact constants were not extracted from the sources read.

### 4.3 Self-play loop (training, for reference)
Play games with search; store (position, visit-count distribution, final result); train the net to predict both; repeat with the new net. Search is the policy-improvement operator, the game result is the evaluation target. MuZero replaces the simulator with a learned model of reward, value and policy (800 simulations in board games, K=5 unroll steps). Our agent cannot run this loop; it can use the shape of it: propose (policy), look ahead (search), judge (value), and record outcomes (memory, S9).

### 4.4 The test-time and train-time exchange (Hex)
Jones (2021) fits Elo-versus-compute frontiers on small boards and predicts larger boards; the error falls exponentially as more board sizes are included. Each 10x of training compute lets test-time compute fall about 15x at equal performance, down to a floor of a one-node search (a09, a25). Reading: a stronger base model needs less search. One game, one algorithm (K07).

### 4.5 Search around an LLM: designs that were measured
1. **Tree of Thoughts.** Generate b candidate next thoughts; have the model score each (value or vote); keep the best b; go to depth 3 (Game of 24). Cost grows with b. b=5 gave 74% against 45% at b=1 (b16).
2. **RAP.** The LLM is both world model (predict the next state after an action) and policy; MCTS with rewards from likelihood and self-evaluation. 20 iterations lifted Blocksworld 6-step from 0.00 to 0.42 on LLaMA-33B (c08).
3. **LATS.** Expand n=5 children per node, run 8 iterations (code) or 50 trajectories (HotpotQA), score by value prompt plus self-reflection plus real feedback (unit tests, environment) (c09).
4. **TS-LLM (AlphaZero-like).** A learned value (and policy) network inside BFS, DFS or MCTS over LLM decoding; trees up to depth 64. A learned LLaMA2-7B value beat a prompted GPT-3.5 value (b18).
5. **Schultz MAV-MCTS.** One transformer is policy, value and world model for board games; run MCTS with it outside the model (external) or have the model write a small tree in its answer (internal: breadth up to 4, depth 2) (a13, a14).
6. **Koh agent tree search.** Best-first search over web-agent states with a model-based value; needs resettable environments; depth 5 and branch 5 gave +43% relative (d09).
7. **REBASE (rollout-free tree).** Share a fixed sampling budget across tree nodes in proportion to a reward-balanced weight, with no rollouts. Better than classic MCTS on GSM8K and MATH (d08).
8. **PlanSearch.** Search over plans in natural language before code; diversity of plans raises pass@200 from 60.6% to 77.0% (d12).

### 4.6 What the evaluator does
Search converts evaluator quality into answer quality, up to a point. Gao et al. fit gold reward against sqrt(KL) as d(alpha - beta d): it rises then falls. Beam search against a process reward model degrades on easy MATH questions as budget grows (Snell). The agent consequence: more search against a self-judged score is not free; there is an optimum and it moves earlier when the evaluator is weak.

### 4.7 Allocation by difficulty
Snell: choose the method per prompt by estimated difficulty; this matched best-of-N with up to 4x less compute. Liu: bands by pass@1 (easy 50-100%, medium 10-50%, hard 0-10%). Policy: easy items, one or few samples; medium, wide sampling plus verifier; hard but non-zero, structured search; zero-success items, search does not help much (b15).

## 5. What holds up

**Replicated or multi-source ([E]).**
- Learned guidance cuts nodes by orders of magnitude and beats brute force: AlphaZero 2017, the 2018 rematch with fairer conditions, Leela. K04. (Stockfish NNUE was not opened, c25.)
- Self-play from scratch reaches superhuman level in three games, and MuZero without the rules. K06.
- UCT converges and has alpha-beta-like cost on small trees (Kocsis; Browne). K03.
- At equal compute on math reasoning, tree search is not reliably better than best-of-N with a verifier: Snell, Liu, Feng, Wu agree in direction. K13, K24.
- The evaluator can be exploited, so more search can lower true quality (Snell, Gao). K26.
- Selection is the bottleneck when no verifier exists (Brown). K30.
- Explicit wide sampling stays useful on RL-trained reasoning models (R1, Yue). K27.
- Search does not remove blind spots; defences are weak (Wang, Tseng). K17.
- Classic rollout MCTS fits LLM reasoning poorly (Wu, R1, Browne). K29.
- Chess-trained transformers represent board state linearly (Karvonen, Toshniwal, ChessGPT). K19.

**Failures, contradictions and moderators.**
- *Search value at equal compute.* ToT, RAP, LATS, rStar-Math report big gains, but against weak baselines (single CoT, not best-of-N at equal tokens). ToT's fairest line is CoT best-of-100 at 49% vs ToT b=5 at 74%. Snell and Feng show the gap shrinks or reverses when the baseline is strong (K13, K15).
- *Base-model strength.* LATS GPT-3.5 gap over Reflexion is 15.7 points (83.8 vs 68.1); GPT-4 gap is 1.7 (92.7 vs 91.0). Liu: at 72B, best-of-N wins at all difficulty levels. Koh does not show shrinkage in absolute terms: gains of about 9 and 7.5 points for the weaker and stronger model (7.6 to 16.7, and 18.9 to 26.4), larger in relative terms for the weaker. No threshold measured on 2025-26 frontier models (K15, K24, K25).
- *Source of the gain.* LATS and RAP use real feedback (tests, environment) or training; with feedback removed the gain is untested (K16). rStar-Math needs trained policy and process-reward models.
- *Generator vs evaluator.* A weak evaluator costs 10 points (74 to 64); a weak generator costs 43 (74 to 31) in ToT (K12). Single paper.
- *Chess/Go Elo anchors differ.* Ruoss 2895 (Lichess blitz vs humans), 2299 (vs bots), Schultz 2923 (CCRL-anchored), LLM Chess 758 (Dragon levels). "Grandmaster level" is not one number (c26). Many Elo values are model-estimated.
- *Match conditions.* AlphaZero 2017 gave Stockfish 1 GB hash and fixed 1 min/move; the 2018 match was fairer (155W 6L 839D) and the margin shrank, though the direction held.
- *Distribution shift.* Searchless distillation lost 515 Elo on Fischer random (K32).
- *Thinking-model collapse.* The Illusion of Thinking collapse is disputed (Lawsen): some instances were unsolvable and outputs hit the token cap (K28).
- *Human matching.* Engines optimal for play predict humans worse than human-trained nets; extra rollouts hurt matching (K18). Not our problem, but it warns that searched answers can be unexplainable.
- *Interventions that worked.* Real unit-test feedback (LATS); compute-optimal allocation (about 4x); plan diversity (PlanSearch); a verifier (SWE-bench Lite 15.9% to 56% at 250 samples); learned value over prompted value (Feng); resettable environments for agent search (Koh); chess fine-tuning for state tracking.
- *Interventions that did not.* Token-level MCTS (R1); classic rollouts (Wu); lookahead MCTS-like search at equal budget (Snell); beam search on easy items; voting or reward-model selection at scale without a verifier (40.50% to 41.41%); patching a Go net against adversaries (Tseng).
- *Not opened or weak.* Deep Blue paper, AlphaGo 2016, UCT journal paper, Knuth-Moore, Carlini's Elo figure (the page has no Elo; the "about 1750" in earlier notes could not be found), Kaggle Game Arena numbers (announcement only), ReST-MCTS* table, PG-TD figures.

## 6. Language models

**Playing the games.**
- GPT-3.5-turbo-instruct: 1755 Elo vs bots and 66.5% puzzle accuracy (a10). Chat-tuned models were much weaker (Dynomight d18: one model won 10 of 10, chat models lost; illegal moves handled by up to 10 retries then a random legal move).
- LLM Chess (Dec 2025, 76 models): best o3 (low) about 758 Elo against Dragon levels (skill 1 about 250, +125 per level; at least 30 games per estimate); random agent -122. 71.1% of models had abnormal finishes; 64.79% of failures were wrong actions: 62.1% format or tool errors, 37.9% illegal moves. More reasoning effort raised win/loss by up to 20%. Wide sampling with mixture-of-agents (3x, 5x, o4-mini) was also tested (d16, d17). This is a different Elo scale from Ruoss or Schultz.
- GTBench (10 tasks): GPT-4 and Llama-3-70B lead open models; LLMs fail deterministic complete-information games and are more competitive in probabilistic ones (c13). Status [C]: only GTBench was opened for this claim; Kaggle Game Arena (8 models, more than 100 matches per pair) gave no numbers (d20).
- Board-state tracking: a GPT trained only on chess text has a linear board code (probe 99.6%) and 99.8% legal moves (c15). Fine-tuning lifts general LLM state tracking from 29.5-53.0% to 92-99% (c16).
- A transformer trained on search values (no search at play), 270M, reaches blitz 2895 vs humans (a10).

**Search wrapped around LLMs.** Numbers in section 3. Pattern across studies:
1. Largest gains: tasks that need lookahead and have cheap local checks (Game of 24: 4.0 to 74; Blocksworld 6-step 0 to 0.42; HumanEval with tests 68.1 to 83.8 for GPT-3.5).
2. Gains shrink with stronger base models and stronger baselines (LATS 15.7 to 1.7 points; Liu 72B; Feng GSM8K).
3. Gains depend on the evaluator. Learned value beats prompted value (Feng). Real feedback beats self-judgment (LATS). Self-evaluation can be exploited (Snell, Gao).
4. Without a verifier, extra samples raise coverage but not selected accuracy (Brown: 82.9 to 98.44 coverage vs 40.50 to 41.41 selected).
5. Search that fits the medium works: whole-thought nodes, rollout-free allocation (REBASE), shallow depth (Koh depth 5 and branch 5 was best of those tested; ToT depth 3; Schultz depth 2).
6. Resettable environments make search beat re-ranking (Koh: 37.0% vs about 30%).

**What changed with reasoning models (2025-26).** R1: pass@1 79.8, pass@64 90.0, majority 86.7 on AIME24 (d02). Yue: RL sharpens pass@1 but base models win at large k, so RL does not add new reasoning capacity (d03). R1's team reported that token-level MCTS did not scale (d01). Illusion of Thinking: low complexity, non-thinking wins; medium, thinking wins; high, both collapse (d04); Lawsen attributes much of the collapse to output limits and impossible instances (d05). Valmeekam: o1 97.8% on 600 standard Blocksworld, 52.8% on randomised names, 23.63% on 110 larger problems; a classical planner solves all (d15). Net: long-chain training puts some search inside the chain, but explicit breadth and external checking are still useful. A head-to-head of an external tree against a reasoning model on one task was not found (open).

**Costs.** ToT uses many calls per problem (b=5 and a 3-step tree). MAV-MCTS gains are roughly logarithmic in simulations: +68 internal Elo at 100 sims, external 3170 at 500 and 3191 at 1000 (about 21 Elo from 500 to 1000) against 2923 alone. Koh: c=5, n=5 spends about equal inference to the baseline.

## 7. What our agent should take

### Add now (established)
1. **Compare any tree against best-of-N with a checker at equal tokens.** Schema G7 plus S6. [E] K13, K24, K26. Evidence b13, b14, b19, d06, d07, d08. The tree stays only if it wins.
2. **Build the checker before the tree.** Schema G3, G2, S4. [E] K30 (K16 is [S]). Evidence d11, d12, c09. Code-run tests are the cheapest lever; selection without a verifier plateaus (40.50% to 41.41%).
3. **Route search by difficulty; no search on easy items; little on zero-success items.** Schema S0 and G12. [E] K24, K26 (the 4x figure, K14, is [S]). Evidence d06, d07, b13, b15. This matches G12 as written; add the easy-item brake: more search on an already-likely-right answer can lower accuracy. Evidence ids to add to G12: d06, d07.
4. **Keep the tree shallow, over whole thoughts, rollout-free.** Schema S6 tree rules (at most 3 children, depth 2). [E] K29. Evidence d01, d08, d21, d24. No token-level MCTS; no random-rollout scoring. This supports the existing rule.
5. **Keep a breadth step even with reasoning models** (several independent attempts plus a code selector). Schema S3, S7, G11. [E] K27. Evidence d02, d03.
6. **Probe searched answers with an adversarial check by an independent agent.** Schema G3 (unfitted part), S8. [E] K17. Evidence a19, a20, b23, d23. Deep search left blind spots, and patching failed.
7. **Prune only on code-counted checks, never on a model's score.** Schema S6, G5. [E] for the principle: alpha-beta is exact only with exact leaf scores (a01), and evaluators are exploitable (K26: d07, d13).

### Test first
1. **Child ordering by the model's prior ("move ordering").** S6. [S] K01 (a01); no LLM test. U1.
2. **Self-value vs real-check value for ranking children.** G, S4. [S] K16, K12. U2.
3. **Value-collapse trigger.** G (calibration). [S] K23. U3.
4. **Plan-level diversity before depth.** S3. [S] K30 (d12). U4.
5. **Generator vs evaluator budget split.** S3/S4. [S] K12. U5.
6. **Difficulty-routed allocation with a threshold.** S0/G12. [S] K14. U6.
7. **UCB-style branch selection vs uniform branch sampling.** S6. [E] in games (K03), untested on LLMs. U7.
8. **Cached answers under shifted formats.** Memory. [S] K08, K32. U8.
9. **Written state ledger vs implicit tracking.** S2, memory. [E] for trained transformers (K19), untested for scaffolds. U9.
10. **Reasoning model vs external tree at equal tokens.** S6 gate. [C] K28. U10.
11. **Reset-and-search for agentic tasks.** S6, O. [S] K25. U11.
12. **Rule and format check before each search call.** G, S4. [S] K31 (d16, d17). U12.
13. **Early-stop rule when the first answer is already likely right.** S6 gate, G11. [E] in direction (K26), threshold unknown. U13.

## 8. Concrete tests on our bench

Rules for all tests: both arms at equal total tokens (count setup, evaluator calls and search calls); same item set; same model; at least three seeds; report the plain best-of-N control in every table (G7).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Lookahead items with cheap checks (Game of 24 style, small planning puzzles, ARC subtasks with a code check) | (a) best-of-N with checker; (b) depth-2 breadth-3 tree, children ranked by checker; (c) same tree ranked by model self-score | Exact-match accuracy; tokens per solved item | (b) at or above (a) on medium items; (c) at or below (b); a (b)-(c) gap of 5+ points supports "real feedback over self-value" |
| T2 | Same items, bands by plain pass rate (0%, 1-10%, 10-50%, 50-100%) | Uniform allocation vs allocation routed by band (no search on top band, tree on 1-50% bands, little on 0%) | Accuracy per token by band | Routing wins on tokens by about 2 to 4x (Snell); tree helps the 1-50% bands; tree equal or worse on the top band |
| T3 | Medium-hard checkable items | 3 distinct plans then solve each, vs 3 repeats of the same prompt, vs a depth-2 tree | pass@k at equal tokens | Plan diversity beats repeats by about 5+ points (PlanSearch 77.0 vs 60.6 at pass@200) |
| T4 | Items with a checker | Generator vs evaluator budget split (80/20, 50/50, 20/80) | Accuracy | Generator-heavy split wins (ToT App. B: weak generator costs more than weak evaluator) |
| T5 | Items with self-rated confidence | Log confidence per search step; re-plan on a drop of 30+ points between steps vs no trigger | Accuracy; false triggers per item | Re-plan on a drop recovers some failures without hurting correct runs |
| T6 | Rule-bound tasks (legal-move puzzles, tool-call formats) | Plain vs code legality and format check before each search call | Share of wasted calls; accuracy | Fewer wasted calls (62.1% of LLM Chess failures were format); accuracy up |
| T7 | Multi-step tasks with resettable state | Search with state resets vs re-ranking of full trajectories | Success rate | Search +5 to 10 points at depth 5 branch 5 (Koh +43% relative) |
| T8 | Reworded or format-shifted copies of solved items | Cached answer vs live solve vs cached + verify | Accuracy on shifted copies | Cached-only drops on shifts (Ruoss minus 515 Elo); cached + verify holds |
| T9 | Long state-tracking tasks (grid moves, inventory) | Free-form tracking vs a written state table updated each step | Final-state accuracy | Written state wins on long tasks |
| T10 | Hard items | One long reasoning chain vs wide sampling of short chains + selector vs external tree | Accuracy | Wide-sampling arm at or above the long chain (G11); tree competitive only on the 1-50% band |
| T11 | Easy items | First answer vs added search | Accuracy | Added search at or below first answer (beam degrades on easy items) |
| T12 | Any step that prunes children | Hard cut by model score vs soft pruning by code check | Rate of dropping the true best child | Hard model-score cuts lose the best child at a measurable rate; soft pruning does not |
| T13 | Branch selection | UCB-style (value + exploration bonus) vs uniform branch sampling | Accuracy at equal tokens | Small edge (K03 is from games; expect a few points at most) |

## 9. What does not transfer, and why

- **Training-time self-play.** Needs a perfect simulator, a game result and huge compute (5,000 TPUs for self-play in AlphaZero). Our agent has no weights loop. Use only as a ceiling and as a design shape.
- **Alpha-beta's exactness.** Requires exact leaf scores and a fixed-depth full-width tree. Our leaves are noisy model judgments and our trees are 3 wide and 2 deep. Hard cuts are unsafe.
- **Millions of rollouts.** MCTS statistics need thousands of visits. An LLM tree gets tens. UCT's convergence guarantee is asymptotic. At 10-50 evaluations the exploration bonus mostly adds noise (our inference, not a measured result).
- **Cheap, exact terminal outcome.** Games end in win, draw or loss. Open tasks end in judgment calls. Many of the big LLM gains need unit tests or an environment (LATS, RAP's reward, rStar-Math's trained PRM).
- **Opponent modelling and zero-sum structure.** Minimax assumes an adversary. Most of our tasks are single-agent. Only adversarial checking (G3, S8) borrows the idea.
- **Elo numbers.** Anchored to different opponent pools; not comparable across Ruoss, Schultz and LLM Chess.
- **Searchless distillation.** Needs 15 billion labelled states from an engine. Our memory holds hundreds of lessons. The off-distribution drop (515 Elo) is the part that transfers.
- **Human-move prediction (Maia).** Relevant to people, not to correctness.
- **Hex scaling law.** One game, one algorithm; usable only as a prior that stronger models need less search.
- **Token-level MCTS.** Reported as not scaling (d01).

## 10. Open questions

1. At equal tokens, does ToT-style or MCTS-style search beat best-of-N with a verifier on 2025-26 frontier models, and on which task types does it lose? No single-shot equal-token test found.
2. Is there a model strength above which tree search is not worth the tokens? Liu (72B) and LATS (GPT-4) hint yes; no threshold measured.
3. How well does an LLM's own value estimate predict real outcomes across search states (calibration curve, AlphaGo game-4 style collapse)? Not measured.
4. Do reasoning-model chains already contain implicit search that makes an external tree redundant? No direct comparison.
5. What branching factor and evaluation cost make MCTS beat alpha-beta-style exhaustive pruning on LLM tasks? Only a rule of thumb (K22, K29).
6. Do KataGo-style cyclic attacks have LLM tree-search analogues, and do verifier checks catch them? No study.
7. True Elo and illegal-move rates for Carlini's 2023 setup and Kaggle Game Arena; neither page gave numbers.
8. Cost-optimal split between generating branches and evaluating them at fixed budget.
9. Does searchless distillation generalise under shift when the "net" is an agent's memory?
10. Does the Hex 10x-to-15x exchange rate hold for LLMs?
11. Which of the AlphaZero-vs-Stockfish differences came from MCTS and which from the learned evaluation? Not separated.
12. Is the Illusion of Thinking collapse real once token limits and unsolvable instances are removed?

## 11. Sources

[V] opened this session (full text or page); [M] snippet only or from memory. Some [V] items are Wikipedia summaries of the primary paper (noted).

- [V] Knuth and Moore (1975) via Wikipedia, alpha-beta pruning. https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning ; original [M] https://doi.org/10.1016/0004-3702(75)90019-3
- [V] Deep Blue, Wikipedia summary. https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)
- [M] Campbell, Hoane, Hsu (2002) Deep Blue. https://doi.org/10.1016/S0004-3702(01)00129-1
- [V] Kocsis and Szepesvari (2006) UCT. http://ggp.stanford.edu/readings/uct.pdf ; journal version [M] https://doi.org/10.1007/11871842_29
- [V] Browne et al. (2012) A survey of Monte Carlo tree search methods. http://www.incompleteideas.net/609%20dropbox/other%20readings%20and%20resources/MCTS-survey.pdf ; https://ieeexplore.ieee.org/document/6145622
- [V] Silver et al. (2017) AlphaZero. https://arxiv.org/abs/1712.01815
- [V] AlphaZero 2018 match, Wikipedia. https://en.wikipedia.org/wiki/AlphaZero
- [V] AlphaGo Zero, Wikipedia. https://en.wikipedia.org/wiki/AlphaGo_Zero
- [V] AlphaGo vs Lee Sedol, Wikipedia. https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol
- [M] Silver et al. (2016) AlphaGo. https://doi.org/10.1038/nature16961
- [V] Schrittwieser et al. (2019/2020) MuZero. https://arxiv.org/abs/1911.08265
- [V] Jones (2021) Scaling scaling laws with board games. https://arxiv.org/abs/2104.03113
- [V] Wu (2019) KataGo. https://arxiv.org/abs/1902.10565
- [V] Wang et al. (2023) Adversarial policies beat superhuman Go AIs. https://arxiv.org/abs/2211.00241
- [V] Tseng et al. (2025) Can Go AIs be adversarially robust? https://arxiv.org/abs/2406.12843
- [V] Ruoss et al. (2024) Grandmaster-level chess without search. https://arxiv.org/abs/2402.04494
- [V] Schultz et al. (2025) Mastering board games by external and internal planning with language models. https://arxiv.org/abs/2412.12119
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Hao et al. (2023) Reasoning with language model is planning with world model (RAP). https://arxiv.org/abs/2305.14992 (one abstract-page line, b28, was [M])
- [V] Feng et al. (2024) AlphaZero-like tree search can guide LLM decoding and training. https://arxiv.org/abs/2309.17179
- [V] Zhou et al. (2024) Language Agent Tree Search. https://arxiv.org/abs/2310.04406
- [V] Guan et al. (2025) rStar-Math. https://arxiv.org/abs/2501.04519
- [M] Zhang et al. (2024) ReST-MCTS*. https://arxiv.org/abs/2406.03816
- [V] Zhang et al. (2023) Planning with LLMs for code generation (PG-TD), abstract only. https://arxiv.org/abs/2303.05510
- [V] Lehnert et al. (2024) Searchformer. https://arxiv.org/abs/2402.14083
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Liu et al. (2025) Can 1B LLM surpass 405B LLM? https://arxiv.org/abs/2502.06703
- [V] Wu et al. (2025) Inference scaling laws. https://arxiv.org/abs/2408.00724
- [V] Koh et al. (2026) Tree search for language model agents. https://arxiv.org/abs/2407.01476
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787
- [V] Wang et al. / Scale AI (2024) Planning in natural language improves LLM search for code generation. https://arxiv.org/abs/2409.03733
- [V] Gao, Schulman, Hilton (2023) Scaling laws for reward model overoptimization. https://arxiv.org/abs/2210.10760
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948
- [V] Yue et al. (2025) Does reinforcement learning really incentivize reasoning capacity? https://arxiv.org/abs/2504.13837
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941
- [V] Lawsen (2025) Comment on The illusion of thinking. https://arxiv.org/abs/2506.09250
- [V] Valmeekam et al. (2024) LLMs still can't plan; can LRMs? https://arxiv.org/abs/2409.13373
- [V] Kolasani, Saplin et al. (2025) LLM CHESS. https://arxiv.org/abs/2512.01992
- [V] Dynomight (2024) Something weird is happening with LLMs and chess. https://dynomight.net/chess/
- [V] Carlini (2023) Playing chess with large language models, page read (no Elo found). https://nicholas.carlini.com/writing/2023/chess-llm.html
- [V] Google DeepMind and Kaggle (2025) Game Arena announcement (no numbers). https://blog.google/technology/ai/kaggle-game-arena/
- [M] Kaggle Game Arena. https://www.kaggle.com/game-arena
- [V] McIlroy-Young et al. (2020) Aligning superhuman AI with human behavior (Maia). https://arxiv.org/abs/2006.01855
- [V] Karvonen (2024) Emergent world models and latent variable estimation in chess-playing language models. https://arxiv.org/abs/2403.15498
- [V] Toshniwal et al. (2022) Chess as a testbed for language model state tracking. https://arxiv.org/abs/2102.13249
- [V] Feng et al. (2023) ChessGPT. https://arxiv.org/abs/2306.09200
- [V] Gao et al. (2024) GTBench. https://arxiv.org/abs/2402.12348
- [M] Stockfish NNUE and Leela Chess Zero. https://stockfishchess.org
