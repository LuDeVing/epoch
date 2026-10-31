# Heuristic search (A*, best-first): deep document

*Subfield C05.01. Written 2026-10-31 from evidence_a-d.jsonl, claims.jsonl (K01-K32) and critique.md in this folder. Ids like a07 or d11 point to evidence lines. Statuses: [E] established, [S] single-source, [C] contested.*

## 1. What it is

A heuristic is a cheap estimate that ranks the options at a branch point. Best-first search keeps a list of open states and always expands the one with the best score. A* is the best-known form. It scores a state by f = g + h. g is the cost paid so far. h is the estimated cost still to go.

Two properties matter.
- Admissible: h never overestimates the true remaining cost. A* with an admissible h finds an optimal path (a02).
- Consistent: h(n) is at most the step cost to a neighbour plus h(neighbour). Consistency implies admissibility. With it, A* never reopens a node. The 1968 optimality theorems are stated under consistency (d16).

Special cases. h = 0 gives Dijkstra (a02). Ignoring g gives greedy best-first, which is fast but gives no cost guarantee. Multiplying h by a weight above 1 gives weighted A*, with cost at most that weight times the optimum (a04).

Why it matters for our agent. At S6 the agent has several candidate children (operators, subgoals, partial solutions). Something must rank them. A* says what a good ranking score looks like (cost so far plus an optimistic estimate of what remains) and what goes wrong when the score is wrong. The 2023-2026 LLM literature tests this directly: tree-of-thoughts methods use the model itself as h.

Scope limit. Classical theory assumes a known state graph, exact step costs and a numeric h. An LLM agent has none of these. The theory gives design vocabulary and failure modes more than guarantees (K01).

## 2. History and theories in depth

**Newell and Simon, 1950s-1976.** Problem solving is search through a space of states using heuristics to cut the search. Their 1976 Turing lecture "Computer science as empirical inquiry" states the physical symbol system and heuristic search hypotheses (a06). It is a hypothesis, not an experiment. Newell and Simon 1972 (Human Problem Solving) was not opened. We have no measured human heuristic error rates (K32).

**Graph Traverser and A*, 1960s.** Nilsson's Graph Traverser ranked by h alone. Raphael added the path cost g. Hart added admissibility and consistency. The result, Hart, Nilsson and Raphael 1968, was built for the Shakey robot at SRI (a01). The original was read (d16). Theorems 2 and 3 and their corollaries assume the consistency assumption and arc costs bounded below by a positive number. The paper gives an example where inconsistent estimates (h(s)=8, h(n2)=1) make A* expand the wrong node. The 1968 optimal-efficiency claim was later found shaky (a01).

**Optimal efficiency, 1985.** Dechter and Pearl showed A* with a consistent h expands no more nodes than any admissible algorithm no more informed than it, up to ties. For admissible but inconsistent h, other algorithms can expand arbitrarily fewer nodes (a03). Source: Wikipedia only; the 1985 paper was not opened.

**Pearl 1984.** Heuristics: Intelligent Search Strategies for Computer Problem Solving. The standard textbook treatment, including relaxation as a source of heuristics (a05). Not opened; the claim rests on citations.

**Complexity.** Worst case O(b^d). Refined bound O(C*/epsilon), with C* the optimal cost and epsilon the smallest gap between f values (a04, b17). The exponent hides a lot: heuristic quality decides whether real problems are solvable.

**Heuristic quality theory.**
- Korf 1997 (a25, a26): pattern databases made optimal Rubik's Cube solving feasible. Tables of 42 MB (corner) and 82 MB (three tables) with about 700,000 nodes per second. The old heuristic reached depth 14 in about 3 days; depth 18 would have needed over 250 years. Conjecture: time times space is about the size of the state space.
- Helmert and Roger 2008 (d18): even an almost perfect heuristic (absolute error 1) leaves A* exponential on GRIPPER and MICONIC. About half of all reachable states must be considered on GRIPPER.
- Wilt and Ruml 2012 (d17): greedy and weighted search fail or work depending on the correlation between h and distance-to-go, not on percent error.

**Relaxation.** The FF heuristic solves a relaxed problem with delete effects ignored (a27). It is informative but not admissible. Covered in 02_heuristics_by_relaxation; not repeated here.

**LLM era.** Since 2023 papers use an LLM as h: Tree of Thoughts (a07), RAP (a11), LATS (a12), tree search for web agents (a24), Q* (d19). A parallel line trains transformers to imitate A* (Searchformer, a13). A third line asks the LLM to write heuristic code once and run sound search (Correa et al., c14; Thought of Search, a23).

**Links to other subfields in this run (not covered here).** Impasse-driven subgoaling and chunking; Sampling and voting (self-consistency); Exploration versus exploitation; Model-based versus model-free control; Premise selection; Expected value of sample information; Scoring rules and calibration.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A* with consistent h never reopens nodes and is optimal-efficient up to ties; theorems need consistency and positive arc costs | Theorems 2-3 read in the original | Hart, Nilsson, Raphael 1968 (d16); Dechter-Pearl via Wikipedia (a03) | [E] |
| Heuristic strength depends on correlation with distance-to-go, not percent error | Greedy works at Spearman 0.94, 0.97, 0.96, 0.997, 0.71, 0.52; fails at 0.39, 0.34, -0.03, 0.16 | Wilt and Ruml 2012 (d17) | [S] |
| Error 1 still gives exponential A* work on some domains | GRIPPER: about half of reachable states considered; exponential on MICONIC too | Helmert and Roger 2008 (d18) | [S] |
| Pattern databases made Rubik's Cube solvable | 42 MB / 82 MB tables; about 700k nodes/s; depth 18 over 250 years without them | Korf 1997 (a25) | [S] |
| ToT beats sampled CoT on Game of 24 (GPT-4, 100 puzzles) | IO 7.3, CoT 4.0, CoT-SC k=100 9.0, CoT best-of-100 49, ToT b=1 45, ToT b=5 74 | Yao et al. 2023 (a07, c01) | [C] |
| Cost of that gain | IO best-of-100 $0.13 at 33%; CoT best-of-100 $0.47 at 49%; ToT $0.74 at 74% (a10 is wrong, corrected on the PDF image). ToT 5.5k completion tokens vs 6.7k for 100 CoT trials | ToT Table 7 (c03, critique) | [C] |
| About 60% of CoT samples already fail at step one | Game of 24, GPT-4 | Yao et al. 2023 (c01) | [S] |
| Crossword ToT: pruning and backtracking both matter | Word level: ToT 60, no prune 41.5, no backtrack 20, IO 14, CoT 15.6; games solved 4/20; oracle state picker 67.5 word level, 7/20 games | Yao et al. 2023 (b05, c02) | [S] |
| Generation is the bottleneck, not evaluation | GPT-4 both 74; GPT-4 generates, GPT-3.5 judges 64; GPT-3.5 generates, GPT-4 judges 31; GPT-3.5 both 19 | Yao et al. 2023 (a09, c03) | [S] |
| ToT depends on base model; loses to self-consistency with GPT-3.5 at equal budget | Cheap evaluator: GPT-3.5 judge 72% for $33.53 vs GPT-4 judge 76% for $159.87 (4.8x) | Wang et al. 2024 (d01, d02) | [C] |
| Model self-scoring of answers is weak | GPT-3.5 direct evaluation on 160 balanced answers 50.6% (chance), GPT-4 78.75% | Wang et al. 2024 (d02) | [E] with d03, d09, d15 |
| GPT-4 as binary verifier rejects true answers | Graph colouring FN 95.8%, FP 6.5%; Mystery Blocksworld FN 97.09%, FP 0.5%; Blocksworld FP 18.55%; Game of 24 FN 20.7%, FP 10.4% | Stechly et al. 2024 (d15) | [E] direction |
| MCTS over a world model lifts a mid model | RAP Blocksworld LLaMA-33B at 2/4/6 steps: CoT 0.17/0.02/0.00; RAP(10) 1.00/0.86/0.26; RAP(20) 1.00/0.88/0.42; GPT-4 CoT 0.50/0.63/0.40 | Hao et al. 2023 (a11, c06) | [E] direction; shrinks with strong base |
| Self-reward of small models is near random | RAP GSM8K LLaMA2-7B 24.34 self-reward vs 22.90 / 22.67 random reward; Mistral-7B 56.25 vs 55.50 / 49.66 | rStar (d09) | [E] with d01, d02 |
| LATS: LM heuristic matters | HotPotQA EM: full 0.63, no LM heuristic 0.37, DFS 0.42, ToT 0.39, RAP 0.54, no reflection 0.58. HumanEval GPT-3.5: LATS 83.8, ToT 54.4, RAP 63.1; GPT-4 LATS 92.7 vs Reflexion 91.0 | Zhou et al. (a12, c07) | [E] direction |
| Search for web agents grows with budget | VWA (910 tasks) 18.9 to 26.4 (+39.7%); WA (812 tasks) 15.0 to 19.2 (+28.0%). 200-task VWA subset 24.5 to 32.0 at c=5 and 37.0 at c=20 | Koh et al. 2024 (a24, c08, c09) | [S] |
| Search-free agents can be far better | AgentOccam without search 43.1% on WebArena vs 19.2% | Koh et al. (c08) | [S] |
| Process scorers beat voting | MATH best-of-1860: PRM 78.2, ORM 72.4, majority 69.6. ReST-MCTS MATH500: SC 35.1, ORM 36.4, MS 37.3, value 39.0; GSM8K SC 83.9 to 87.5 | Lightman 2023 (d06); ReST-MCTS (d10) | [E] |
| Learned Q-value beats best-of-N by small margins | GSM8K base 65.2, best-of-N(QVM) 74.5, Q*(QVM) 78.8, Q*(PRM+QVM) 80.8; MATH 46.8 to 49.1; MBPP 77.0. One run, no variance | Q* (d19) | [S] |
| PRM beam search loses at high budget and on easy items | Compute-optimal search matches best-of-N at 64 with 16 samples at low budget; advantage shrinks with budget | Snell et al. 2024 (d04) | [E] with d05 |
| Search saturates near 64 trajectories | rStar-Math MATH 7B: 58.8 to 89.4 at 8 trajectories, 90.0 at 64 | Guan et al. 2025 (d08) | [S] |
| Plain repeated sampling matches standard MCTS at equal calls | LiveCodeBench GPT-4o: sampling 37.8, MCTS 36.7, AB-MCTS-M 38.9; ARC-AGI sampling above MCTS (15.0/18.6 vs 9.0/14.0, K22) | Inoue et al. 2025 (d11) | [C] |
| Stopping rules save most samples | ESC saves 33.8% (MATH) to 84.2% (Coin Flip); Adaptive-Consistency up to 7.9x with under 0.1% accuracy loss | Li et al. 2024 (d13) | [E] |
| Where an exact check exists, coverage becomes accuracy | SWE-bench Lite 15.9% (1 sample) to 56% (250 samples); voting and reward models plateau | Brown et al. 2024 (d14) | [E] |
| LLMs alone plan poorly | GPT-4 Blocksworld 34.3-35.6% (humans 78%); o1-preview 97.8 plain, 52.8 Mystery, 37.3 randomised, 23.63 on 110 plans of 20-40 steps, 12.7 Sokoban (55 items); Fast Downward 100% at 0.12 s vs 40-167 s for o1 | Valmeekam et al. (a19, b13, b14, a21) | [E] (one lab) |
| External verifier loop helps | VAL back-prompting: Blocksworld 82% in 15 rounds, Logistics 70%, Mystery about 10% | Kambhampati et al. 2024 (b15, c19) | [S] |
| LLM writes heuristic code, sound search runs it | 720 tasks, 8 domains: R1 373, V3 343, Gemini 305, hFF 234, blind 120, best end-to-end LLM 174; cost $0.25 (V3) to $6.12 (R1). On the eight IPC 2023 domains the best of three LLM heuristics solves 354, 19 fewer than R1 | Correa et al. 2025 (c14, c15, critique 7) | [E] |
| Code-only search solves Game of 24 | 1361 of 1362 solvable, the one unsolvable reported; 1.92-6.83 s; about 1.2 LLM interactions for the successor function; ToT 75% on 100 medium puzzles | Katz et al. 2024 (b06, c20) | [E] |
| Per-node LLM calls cost a lot | 50,143 expanded Blocksworld states: about 14 days, over $1000 at GPT-4 | Katz et al. (c21) | [S] (estimate) |
| Heuristic errors near the goal hurt most | Sokoban IID optimal %: All 73.94, End 80.28, Initial 82.04, Middle 56.69 (ILR 9.74); planner-aware sampling 9.5% fewer expansions | Gupta and Li 2024 (b01, b02) | [S] |
| Learned LLM heuristic pays only on hard problems | Inverse time ratio: Sokoban OOD 2.4-2.7, IID 0.26, maze 0.002 | Gupta and Li (b03) | [S] |
| Training on search traces helps | Searchformer Sokoban 93.7% optimal, up to 26.8% fewer steps than the A* teacher; solution-only 86.8% optimal. Stream of Search Countdown 51.27 vs 25.73 | Lehnert 2024 (c04); Gandhi 2024 (c05) | [E], needs training |
| LLM waypoints cut A* work a little | 50x30 grid GPT-3.5: operations 57.39%, storage 74.96% of A*, path +2.44%. Other paper: 352 vs 372 nodes, paths 34 vs 27 | Meng 2024 (a15); Xiao 2023 (c13) | [E], small |
| Diverse plans before code predict search gain | LiveCodeBench Claude 3.5 Sonnet: pass@1 41.4, repeated sampling pass@200 60.6, PlanSearch 77.0 | Wang et al. 2024 (c23) | [S] |
| Environment feedback beats plain CoT on grid paths | ReAct 96.1% success; CoT loses 7% with 4+ obstacles | Aghzal et al. (c24) | [S] |

## 4. Mechanisms and models

### 4.1 Classical best-first loop
1. Open list (priority queue) with the start state. Closed set empty.
2. Pop the state with lowest f = g + w*h. w = 1 for A*, w > 1 for weighted A*, and g dropped for greedy.
3. If it passes the goal test, return it.
4. Expand: generate children with a successor function. Skip children already in closed with a lower g (with consistent h no reopen is needed).
5. Push children. Repeat until the budget ends.

Design rules from the theory:
- Optimism: when optimality matters, use an estimate that errs low. Overestimates can prune the right branch (a02).
- Correlation with distance-to-go is what makes greedy ranking work (d17). Check it on dev data before using greedy.
- Keep g in the score unless correlation is high. Dropping g speeds search and costs solution quality (b24, c13).
- Near-perfect scoring does not rescue tasks with many independent interleavable subproblems (d18). Use decomposition or symmetry pruning there.

### 4.2 LLM-scored breadth-limited search (ToT, a07)
- Proposer: the LLM writes k children from a state.
- Value: the LLM labels each child (Game of 24: sure / maybe / impossible), sampled several times and combined.
- Keep the b best children per level (b = 5 gave 74%, b = 1 gave 45%).
- Prune "impossible" children; backtrack when a branch dies (crosswords: no backtrack drops word-level success from 60 to 20).
- Depth was 3 steps on Game of 24, longer on crosswords.
- Failure mode: the value call prunes real solutions (b05; GPT-4 false negatives of 20.7% on Game of 24, d15).

### 4.3 MCTS variants over thoughts (RAP, LATS)
- Selection by UCT. Expansion by LLM proposals. Value by LLM self-evaluation plus rollouts, plus (LATS) reflections on failures and environment feedback.
- RAP adds an LLM-simulated world model that predicts the next state after an action (a11). Reward mixes action likelihood and self-evaluation.
- LATS ablation: removing the LM heuristic drops HotPotQA EM 0.63 to 0.37 (c07). With a weak scorer, MCTS adds cost and little gain (d09 random-reward result).

### 4.4 Learned scorer (Q*, TS-LLM, PRM)
- Train a Q-value or step-reward model from rollouts or labels. Rank children by Q plus step utility. Q* ran A* with a learned Q (d19). Gains over best-of-N are 1-4 points.
- A learned scorer beats prompted self-scoring (TS-LLM Game24 path@1 19.1 vs 15.5 with a GPT-3.5 policy, c11) but needs training data. Out of scope for a scaffold.

### 4.5 Heuristic as code (Correa et al., Thought of Search)
- Ask the LLM once per domain for a Python h(state), or for successor and goal-test functions. Check the code on small instances.
- Run greedy best-first search with that code. No LLM call per node.
- Result: 373 of 720 tasks with R1, beating hFF (234) and end-to-end LLM planning (174), at $0.25-$6.12 total (c14).
- A model-written heuristic is faster per node, so it can win even when less informed (Rovers, Sokoban, c15).

### 4.6 Budget control
- Stop expansion when top candidates agree (ESC window rule, d13).
- Cap breadth and depth: gains saturate near 64 trajectories (d08); beam search can fall below best-of-N at high budget (d04).
- Spend search on hard items only (d04, b03).

## 5. What holds up

**Holds up.**
- Classical A* theory with consistent h (d16), read from the original.
- Search plus a good scorer beats sampling when the base model is strong enough to propose good children and the task has early detectable dead ends (ToT GPT-4, RAP, LATS).
- Step-level scorers beat outcome scorers and majority vote by about 4 points on math (d06, d07, d10). Gaps among step scorers are small (0.4 to 1.7 points).
- Sound, code-based checks beat LLM judgement. Code-only search solves Game of 24 and Blocksworld sets at 100% (c20). LLM-written heuristic code beats hFF (c14). Exact checks turn coverage into accuracy (d14).
- Prompted self-scoring is weak at small scale (d02, d09, d15).
- Stopping rules save samples with little loss (d13).

**Failed, null or narrowed results.**
- ToT versus self-consistency at equal budget: ToT wins with GPT-4, loses with GPT-3.5 (d01). The original comparison was against CoT best-of-100, which is a budget comparison but not equal-token (b26: tokens per node differ).
- Standard MCTS does not beat repeated sampling at equal calls on ARC-AGI and LiveCodeBench for GPT-4o (d11). AB-MCTS gains are 1-3 points with SDs from 0.5 to 3.6.
- Beam search over a PRM loses to best-of-N at high budget and hurts on easy questions (d04).
- Q* reports one run and no variance (d19).
- Web-agent search lifts GPT-4o but the result stays far below agents without search (AgentOccam 43.1% vs 19.2%, c08).
- LATS gain over a strong GPT-4 baseline on HumanEval is 1.7 points (91.0 to 92.7).
- LLM waypoints: one paper cuts nodes (352 vs 372), the other finds longer, less smooth paths; greedy LLM beats LLM A* on search size but gives worse paths (c13).
- Shorter search can mean worse answers: the Gupta and Li "Middle" split has ILR 9.74 and only 56.69% optimal (b02, b24).

**Moderators.**
- Base-model strength: the RAP gain on LLaMA-33B shrinks against GPT-4 CoT (0.40 at 6 steps vs RAP 0.42, a11).
- Task depth and early failure: ToT works where 60% of CoT fails at step one.
- Difficulty: learned LLM heuristics pay only out of distribution (b03); PRM beam search helps on hard questions only (d04).
- Obfuscation: o1 falls from 97.8% to 52.8% and 37.3% on Mystery and randomised Blocksworld (b13).
- Length: o1 drops to 23.63% on 20-40 step plans (b13). CoT hints collapse as size grows past the examples (c22).
- Availability of an exact check (d14).

**Interventions that worked.** Step-level scorers; trace training (needs training); LLM-written heuristic code; verifier back-prompting (up to 82% Blocksworld); early stopping; a cheap evaluator (72% for $33.53 vs 76% for $159.87).

**Interventions that did not.** LLM self-rating without a check; MCTS with a poor scorer; deeper beams at large budget; domain-specific CoT beyond the sizes in the prompt; percent error as a measure of heuristic quality.

**Source quality notes (critique).** Nearly all numbers are single-lab and small (ToT 100 puzzles, crossword 20 games, o1 Sokoban 55). Lines a16, b12, c13 are one paper. The o1 lines (a21, b13, b14, c18) are one paper family. Pearl 1984, Dechter-Pearl 1985 and Newell and Simon 1972 were not opened. Q* cells were checked on the page image (d19). No failed replication of ToT with 2025-26 reasoning models was found.

## 6. Language models

**Raw behaviour.**
- Planning without search is weak. GPT-3 solved 6/600 Blocksworld (1%), Instruct-GPT3 41/600 (6.8%) (c17). GPT-4 reached 34.3-35.6% (a19). LLaMA 3.1 405B 62.6% (c18). o1-preview reached 97.8% on plain Blocksworld but 52.8% obfuscated, 37.3% randomised, 23.63% on long plans (b13). A classical planner is 100% at 0.12 s.
- The collapse under obfuscation suggests reliance on surface patterns, not a faithful search.
- CoT hints help only if matched to the problem class: Blocksworld stacking 3.8% zero-shot vs 59.3% with a specific prompt, and the gain falls as block counts grow (b16, c22).

**What changed it, by how much.**
- Breadth-limited search with self-scoring: Game of 24 GPT-4 4.0% to 74% (b=5), versus 49% for CoT best-of-100 (c01, c03). With GPT-3.5, 19% (c03) and below SC (d01).
- RAP: LLaMA-33B 6-step Blocksworld 0.00 to 0.42; Llama-2 70B full Blocksworld Easy 0.08 to 0.65, Hard 0.05 to 0.51 (c06).
- LATS: HotPotQA EM 0.37 (no LM heuristic) to 0.63 (c07).
- Web agent search: +28.0% to +39.7% relative with GPT-4o; Llama-3-70B VWA 7.6 to 16.7 (c08).
- Process scorers: +3.6 to +8.6 points over majority or SC on math depending on setup (d06, d10).
- Code as heuristic: 373 solved vs 174 for end-to-end LLM planning (c14). Tuisov et al.: heuristics from GPT-4.1, GPT-5.1 and Claude Sonnet 4.5 range 188 to 281 of 400 tasks against 234 for the best domain-independent portfolio (c16; table layout uncertain).
- Verifier loops: Blocksworld 82% in 15 rounds (b15).

**Scorer quality.**
- Prompted evaluators are near chance when asked to separate right from wrong (GPT-3.5 50.6%, GPT-4 78.75%, d02) and throw out right answers as verifiers (FN up to 97%, d15). False accepts are rarer (0.5-18.55%). So model scores err pessimistic in these tests, the opposite of the inadmissibility worry. Both hurt: pessimistic pruning drops real solutions (b05).
- No study reports rank correlation or top-1 agreement of LLM state scores with ground truth (critique gap 2).

**Cost.**
- ToT uses about 5x the tokens of CoT on creative writing (a10) and up to 200 calls per crossword game (a23).
- Per-node calls on large graphs are out of reach (c21).
- A weak judge keeps most of the gain: 72% at $33.53 vs 76% at $159.87 (d02).

**Gap.** No test of ToT-style search against self-consistency with 2025-26 reasoning models. Inference-scaling work with newer models (d12) points to best-of-n plus verifiers, but it does not test tree search.

## 7. What our agent should take

### Add now (established)

1. **Rank children with a code-checked score where one exists; prefer a sound check over an LLM score.** Part: G5/S6/S4. [E]. Evidence: K03, K12, K30; c14, c20, d14, d15.
2. **Never prune a candidate on an LLM self-critique alone.** Verifier false-reject rates reach 97%. Keep rejected candidates in a low-priority list; prune only on a sound check (G3). Part: G/S6. [E]. Evidence: K25; d02, d15, b05.
3. **Score steps, not only final answers.** Part: S6. [E]. Evidence: K24; d06, d07, d10. (The cheap-evaluator saving is [S], K28, so it stays a test.)
4. **Always run a plain best-of-N or self-consistency arm at equal tokens against any ranked-children search.** Part: G7. [E] as method rule because gains are contested (K22; d01, d11).
5. **Spend search by difficulty; stop when top candidates agree; cap breadth and depth.** Part: G12/S6. [E]. Evidence: K23, K29; d04, d08, d13.
6. **Have the model write the scoring function as code once, then run it, where states are checkable.** Part: S6/tools. [E]. Evidence: K12; c14, c15, c16.
7. **Keep G1: search only after a signal.** Search is the response to an impasse at S6, not a default. Evidence: K13 (cost), K15 (hard only).
8. **Report answer quality together with cost when comparing rankers.** Part: S6 metric. [S] (K14) but free; adopt as measurement rule.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| LLM-scored ranking of children beats sampling at equal tokens with our model | S6 | [C] | K02, K22; a07, d01, d11 |
| Strong generator, weak cheap ranker | S6 | [S] | K04, K28; a09, d02 |
| Gate: rank children only above a difficulty threshold | S6/G12 | [S] | K15; b03, d04 |
| Backtrack and prune ablation in our scaffold | S6 | [S] | K06; c02 |
| Rank correlation of child scores with outcome before greedy selection; keep width above 1 | S6 | [S] | K26; d17 |
| Yes/no vs 1-10 vs logprob scorer | S6 | not studied | gap 7 |
| Diversity of candidate plans before ranking | S3/S6 | [S] | K19; c23 |
| Decomposition or symmetry pruning on combinatorial items | S2/O | [S] | K27; d18 |
| Environment feedback loop vs none | S4/S5 | [S] | K21; c24, b15 |
| Traces shown in context (not trained) | S6 | training evidence only | K16 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (generation plus scoring), at least 3 seeds, code-checked items where possible. Report quality and cost.

1. **Rank vs resample.** Items: puzzle items with early dead ends and a check (ARC-style tasks, brainteasers). Arm A: N attempts, code select. Arm B: k children per step, a scoring call ranks, keep b. Metric: pass rate. Expected: B wins where plain attempts fail early; ties or loses on easy items and with a weak model.
2. **Ranker strength split.** Strong generator with strong ranker vs strong generator with weak ranker. Metric: pass rate, tokens. Expected: weak ranker keeps most of the gain (72 vs 76 in d02).
3. **Scorer type.** LLM 1-10, yes/no, sure/maybe/impossible, logprob, code score. Metric: Spearman with eventual child success on a dev set, plus top-1 agreement. Expected: code score best; prompted scores middling (unknown, see UNKNOWNS).
4. **Admissibility proxy.** Count false rejects (low score, later passes) and false accepts (high score, dead child). Expected: false rejects are the larger problem, as in d15.
5. **Prune and backtrack ablation.** Remove prune, backtrack, both. Metric: pass rate. Expected: backtrack removal costs more (60 to 20 on crosswords).
6. **Soft vs hard prune.** Demote low scores vs delete them. Metric: pass rate where the right branch is low-scored. Expected: soft prune recovers solutions (3 of 4 crossword solutions pruned ToT missed, b05).
7. **Width and depth curve.** Breadth 1, 2, 3, 5; depth cap 2, 3, 5. Metric: pass rate per token. Expected: saturation at modest width; b=1 gave 45 of the 74 points on Game of 24.
8. **Difficulty gate.** Search only when plain attempts disagree or fail. Metric: pass rate per token on a mixed set. Expected: better than always searching because easy items can be hurt (d04).
9. **Stopping rule.** Stop when the top 2 candidates agree. Metric: tokens saved at equal accuracy. Expected: 30-80% saving.
10. **Greedy vs g + h.** Estimate-only vs cost-so-far plus estimate. Metric: pass rate and solution length. Expected: greedy cheaper, worse answers when correlation is low.
11. **Heuristic as code.** One-time scoring function vs per-node LLM scoring. Metric: pass rate and calls per item. Expected: code wins on checkable states.
12. **Plain vs obfuscated items.** Rename entities. Metric: drop in pass rate for best-of-N vs ranked search. Expected: search with a sound check drops less.

## 9. What does not transfer, and why

- **Optimality guarantees.** They need a numeric lower-bound h and positive arc costs (a02, d16). LLM scores have neither and no study has measured admissibility. We keep the vocabulary: score optimistically, keep cost-so-far, do not prune on one noisy estimate.
- **Node counts as the cost.** Classical work counts expansions. For an LLM each node is several calls (c21). Cost must be tokens.
- **Pattern databases and relaxations.** Korf's tables (a25) need a fixed, enumerable state space.
- **Trace training.** Searchformer, Stream of Search and Q* train weights (K16, K07). Our agent is a scaffold.
- **Maze and Sokoban speed-ups.** Tiny synthetic grids (b01, c13). Gains of 9.5% fewer steps or 352 vs 372 nodes are too small to matter.
- **Game of 24 results.** Three-step depth, a clean value signal, 100 puzzles. Unlikely to carry to open tasks without a sound scorer.
- **Math PRM results.** They need a trained PRM (d06, d10). A prompted scorer is the closest we have and is weak at small scale.
- **Human cognition.** Humans plan with heuristic best-first search and deeper with expertise (d20, abstract only). No measured human heuristic error rates, so no calibration.

## 10. Open questions

1. Do ToT, LATS and RAP gains survive at equal tokens against best-of-N and self-consistency with 2025-26 reasoning models? Not found.
2. How accurate are LLM state scores as rankers (rank correlation, top-1 agreement)? Unmeasured.
3. How often does a model score overestimate? Only binary-verifier false accepts exist (0.5% to 18.55%).
4. Is there a failed replication of ToT with other models or tasks? One partial hit (d01).
5. What breadth, depth and stopping rule are best on agent and open tasks? Only math curves exist.
6. Can a cheap scorer (small model, logprob, code) replace a full LLM score beyond Game of 24?
7. How do humans use admissible-like heuristics? Newell and Simon 1972 and Pearl 1984 unread.
8. Does soft pruning recover solutions that hard pruning loses?
9. Does the rank-correlation predictor of greedy failure (Wilt and Ruml) hold for LLM scores?
10. Many recent gains are 1 to 4 points with no variance (Q*, ReST-MCTS, AB-MCTS). Do they replicate?

## 11. Sources

[V] opened, [M] snippet only or not opened.

- [V] Hart, Nilsson, Raphael 1968. https://www.cs.auckland.ac.nz/courses/compsci709s2c/resources/Mike.d/astarNilsson.pdf
- [V] Wikipedia, A* search algorithm. https://en.wikipedia.org/wiki/A*_search_algorithm
- [V] Wikipedia, Heuristic (computer science). https://en.wikipedia.org/wiki/Heuristic_(computer_science)
- [M] Newell and Simon 1976, Computer science as empirical inquiry (via Wikipedia only), CACM 19(3):113-126
- [M] Pearl 1984, Heuristics (via Wikipedia citation only)
- [M] Dechter and Pearl 1985. https://doi.org/10.1145/3828.3830
- [V] Korf 1997. https://cdn.aaai.org/AAAI/1997/AAAI97-109.pdf
- [V] Helmert and Roger 2008. https://ai.dmi.unibas.ch/papers/helmert-roeger-aaai2008.pdf
- [V] Wilt and Ruml 2012. https://www.cs.unh.edu/~ruml/papers/wted-astar-socs-12.pdf
- [V] Hoffmann 2003, Metric-FF. https://arxiv.org/abs/1106.5271
- [V] Yao et al. 2023, Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Hao et al. 2023, RAP. https://arxiv.org/abs/2305.14992
- [V] Zhou et al. 2023, LATS. https://arxiv.org/abs/2310.04406
- [V] Koh et al. 2024, Tree search for language model agents. https://arxiv.org/abs/2407.01476
- [V] Wang/Li et al. 2024, Q*. https://arxiv.org/abs/2406.14283
- [V] Feng et al. 2024, TS-LLM. https://arxiv.org/abs/2309.17179
- [V] Zhao et al. 2023, LLM-MCTS. https://arxiv.org/abs/2305.14078 (one evidence line abstract-only)
- [V] Lehnert et al. 2024, Searchformer. https://arxiv.org/abs/2402.14083
- [V] Gandhi et al. 2024, Stream of Search. https://arxiv.org/abs/2404.03683
- [V] Gupta and Li 2024. https://arxiv.org/abs/2407.09985
- [V] Meng et al. 2024, LLM-A*. https://arxiv.org/abs/2407.02511
- [V] Xiao et al. 2023, LLM A*. https://arxiv.org/abs/2312.01797
- [V] Lu et al. 2021, NeuroLogic A*esque. https://arxiv.org/abs/2112.08726
- [V] Valmeekam et al. 2023, PlanBench. https://arxiv.org/abs/2302.06706
- [V] Valmeekam et al. 2023, planning abilities. https://arxiv.org/abs/2305.15771
- [V] Valmeekam et al. 2024, can LRMs plan. https://arxiv.org/abs/2409.13373
- [V] Valmeekam et al. 2024, strawberry fields. https://arxiv.org/abs/2410.02162
- [V] Kambhampati et al. 2024, LLM-Modulo. https://arxiv.org/abs/2402.01817
- [V] Stechly et al. 2024, chain of thoughtlessness. https://arxiv.org/abs/2405.04776
- [V] Stechly et al. 2024, self-verification. https://arxiv.org/abs/2402.08115
- [V] Katz et al. 2024, Thought of Search. https://arxiv.org/abs/2404.11833
- [V] Hao et al. 2025, formal verification planning. https://arxiv.org/abs/2404.11891
- [V] Correa, Pereira, Seipp 2025. https://arxiv.org/abs/2503.18809
- [V] Tuisov, Vernik, Shleyfman 2025. https://arxiv.org/abs/2501.18784
- [V] Bomer et al. 2026. https://arxiv.org/abs/2601.19622
- [V] Aghzal, Plaku, Yao 2023. https://arxiv.org/abs/2310.03249
- [V] Wang et al. 2024, PlanSearch. https://arxiv.org/abs/2409.03733
- [V] Wang et al. 2024, Reasoning in token economies. https://arxiv.org/abs/2406.06461
- [V] Snell et al. 2024. https://arxiv.org/abs/2408.03314
- [V] Wu et al. 2024, inference scaling laws. https://arxiv.org/abs/2408.00724
- [V] Lightman et al. 2023. https://arxiv.org/abs/2305.20050
- [V] Wang et al. 2024, Math-Shepherd. https://arxiv.org/abs/2312.08935
- [V] Guan et al. 2025, rStar-Math. https://arxiv.org/abs/2501.04519
- [V] Liu et al. 2024, rStar. https://arxiv.org/abs/2408.06195
- [V] Zhang et al. 2024, ReST-MCTS*. https://arxiv.org/abs/2406.03816
- [V] Inoue et al. 2025, AB-MCTS. https://arxiv.org/abs/2503.04412
- [V] Balachandran et al. 2025. https://arxiv.org/abs/2504.00294
- [V] Li et al. 2024, ESC / Adaptive-Consistency. https://arxiv.org/abs/2401.10480
- [V] Brown et al. 2024, Large language monkeys. https://arxiv.org/abs/2407.21787
- [M] van Opheusden et al. 2023 (abstract only). https://doi.org/10.1038/s41586-023-06124-2

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 9 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C05.01-K07** (number corrected). Table cells match (GSM8K 74.5 vs 78.8/80.8, MATH 46.8 vs 49.1 and 54.3 vs 55.4, MBPP 75.0 vs 77.0; RAP random-reward 24.34 vs 22.90/22.67), but those numbers give Q* gains of 1.1 to 6.3 points (GSM8K PRM+QVM +6.3), not 'only 1 to 4'. Corrected claim: A learned scorer beats prompting the model to score itself (TS-LLM; Q* real table cells: GSM8K best-of-N(QVM) 74.5 vs Q* 78.8 and 80.8, MATH 46.8 vs 49.1 and 54.3 vs 55.4, MBPP 75.0 vs 77.0). Small models' self-reward is near random (RAP with random reward on LLaMA2-7B GSM8K: 24.34 vs 22.67 to 22.90). Q* gains over best-of-N are about 1 to 6 points.
- **C05.01-K08** (reworded: the sources support less). Numbers match (RAP LLaMA-33B 6-step CoT 0.00 vs RAP(20) 0.42, GPT-4 CoT 0.40; LATS no-LM-heuristic 0.37 vs 0.63), but neither paper compares search gains across base-model strength, so 'gain shrinks for strong base models' is an inference from comparing RAP on a 33B model with GPT-4 CoT. Corrected claim: Model value plus search helps: RAP lifts LLaMA-33B on 6-step Blocksworld from 0.00 (CoT) to 0.42, matching GPT-4 CoT at 0.40; removing the LM heuristic from LATS drops HotPotQA EM from 0.63 to 0.37. Whether the gain shrinks for stronger base models was not tested in these papers.
- **C05.01-K24** (number corrected). Lightman (78.2/72.4/69.6) and the 0.4-1.7 step-scorer gap match, but in ReST-MCTS Table 3 Math-Shepherd beats SC by only 3.2 (GSM8K) and 2.2 (MATH500); the ReST-MCTS value model beats SC by 3.6 and 3.9. Corrected claim: Step-level (process) scorers beat outcome scorers and majority voting: MATH best-of-1860 PRM 78.2, ORM 72.4, majority 69.6; at 256 outputs (Mistral-7B MetaMATH) the ReST-MCTS value model beats self-consistency by 3.6 (GSM8K) and 3.9 (MATH500) points and Math-Shepherd by 3.2 and 2.2. Gaps among step scorers are small (0.4 to 1.7).
- **C05.01-K03** (now single-source: only one opened source, code check).
- **C05.01-K09** (now single-source: only one opened source, code check).
