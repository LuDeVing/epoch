# Tree of Thoughts: deep document

*Subfield C05.05. Evidence ids (a01..d20) are in evidence_a-d.jsonl. Claim ids (C05.05-K01..K30) are in claims.jsonl. Re-open checks are in critique.md. Date: 2026-11-10.*

## 1. What it is

Tree of Thoughts (ToT) treats a problem as a search over a tree. Each node is a partial solution, called a "thought". The language model does three jobs: it proposes next thoughts, it scores the states, and a small outer program runs a search (breadth-first or depth-first) with lookahead and backtracking. Yao et al. (2023, arXiv 2305.10601) is the founding paper [a01, a21].

Four design choices define any ToT system [a01, a02]:
1. How to cut the problem into thoughts. A thought is a few words (crosswords), one equation (Game of 24) or a paragraph plan (writing).
2. How to generate thoughts. Either i.i.d. samples from a CoT prompt (rich space, many duplicates) or a sequential "propose" prompt (small space, no duplicates).
3. How to evaluate states. Either value each state alone (sure / maybe / impossible, or a 1-10 score) or vote across states.
4. Which search to run. BFS (keep the best b states per step) or DFS (go deep, prune under a threshold, backtrack).

Yao et al. note that input-output prompting (IO), chain of thought (CoT), self-consistency (CoT-SC) and self-refine are special cases of this frame [a01]. That is why ToT matters for our agent: S6 (impasse) already grows a small idea tree, and ToT is the main published design for it. Our schema fixes at most 3 children, depth 2, at most 2 expansions [D]. This document tests that design against the evidence.

Short summary. ToT is a large win on one kind of task: checkable, multi-step puzzles with early dead ends, with a strong generator model (Game of 24, GPT-4). It is a small win, no win or a loss on most other tasks at equal tokens. Its value step is only as good as the scorer. When a code check exists, a tree bound to that check wins [K25]. When the scorer is the model itself on an open task, the evidence says the pick step is the weak link [K27]. Almost all ToT evidence is toy tasks with 2023 models.

## 2. History and theories in depth

**Roots.** Search over a problem space is the oldest model of problem solving: Newell and Simon's problem-space theory, A*, minimax, MCTS. Yao et al. say so directly: they bring "deliberate" System-2 search to an LM that otherwise decodes left to right (token by token, no lookahead, no backtracking) [a01]. Their error analysis gives the motive: about 60% of CoT samples on Game of 24 already fail after the first step (the first three words, such as "4 + 9") [a04, b02, c02]. A left-to-right decoder commits early and cannot recover.

**May 2023: a cluster of near-simultaneous papers.**
- Yao et al. ToT (tests ran May 5-16 with GPT-4) [a01, a03].
- Long (2305.08291), independent and concurrent: a "prompter agent", a rule-based checker, a memory module and a ToT controller that backtracks when the checker rejects a board or after 5 children. Sudoku with gpt-3.5-turbo: all ten 3x3 solved, 9 of 10 4x4, 8 of 10 5x5, against about 0.5 for one-shot and few-shot on the larger sizes [a09, b08, c06]. The key difference: a code checker, not the model, detects dead ends.
- RAP (Hao et al., 2305.14992): MCTS where the LLM is also the world model. The state is rewritten after each step [a10].
- Self-evaluation guided beam search (Xie et al., 2305.00633): step-level self-evaluation prunes a stochastic beam [a11].
- Adaptive-Consistency (Aggarwal et al., 2305.11860): stop sampling when answers already agree [d09].

**Second half of 2023: variants.**
- Graph of Thoughts (Besta et al., 2308.09687): allow merging of thoughts. Wins on decomposable tasks (sorting, set intersection) [a17].
- Algorithm of Thoughts (Sel et al., 2308.10379): put a worked DFS trace, with false starts, into one prompt, so one query imitates the search [a12, a24].
- Tree of Uncertain Thoughts (Mo and Xin, 2309.07694): add sampling variance to the value estimate [a16].
- LATS (Zhou et al., 2310.04406): MCTS with LLM value and self-reflection, using real environment feedback [c14].
- Everything of Thoughts (XoT, Ding et al., 2311.04254): an MCTS-trained policy gives thoughts to the LLM [b19].
- A survey (Besta et al., 2401.14295) gives a taxonomy of chains, trees and graphs [a20, c25].

**2024: the critique phase.**
- Budget-aware evaluation (Wang et al., 2406.06461): re-run ToT against self-consistency at matched cost [a13].
- Thought of Search (Katz et al., 2404.11833): have the LLM write the successor function and goal test as code, then run plain BFS. 100% on Game of 24 [b15, c17].
- Self-verification limits (Stechly et al., 2402.08115) and "cannot self-correct" (Huang et al., 2310.01798): the self-evaluator is weak when checking is hard [a14, a15].
- Test-time compute work (Snell et al., 2408.03314; Wu et al., 2408.00724): tree search against a trained process reward model helps at low budget, loses its edge later; MCTS was a poor trade [b16, b17].
- Training instead of prompting: Searchformer (Lehnert et al.) and Stream of Search (Gandhi et al.) train on search traces [a19, b23].

**2025-26: reasoning models change the picture.** o1 and R1 do backtracking inside one chain. DeepSeek dropped MCTS as impractical [b24]. Plain o1 beats ToT on GPT-4o on most tasks [d02]. Search wrappers still help when a hard evaluator exists [d03, d04, d05]. Short chains beat long ones [d10, d11]. Sys2Bench (Parashar et al., 2502.12521) is the first independent multi-task benchmark with ToT and shows that it wins only on Game of 24 [d01].

**Competing explanations of the gain.**
1. Pruning early dead ends (the authors' account) [K03].
2. More compute: ToT on Game of 24 uses about 5.5k completion tokens, close to 100 CoT trials [a05]. Equal-token tests partly support this (GPT-3.5: sampling wins) [K07].
3. State rewrite (RAP): the world model holds the current state, so later steps are easier [a23]. No ablation separates this from branching [d19].
4. A formal-search effect: code can do the same search at 100% [K12].
5. Scorer quality: a random scorer kills the gain; a cheap scorer nearly keeps it [K08].

## 3. Core findings with exact numbers

Status uses the claims.jsonl labels. "Single-source" means one independent group.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ToT beats IO, CoT, CoT-SC on Game of 24 (GPT-4) | IO 7.3, CoT 4.0, CoT-SC(100) 9.0, IO+Refine(10) 27, ToT b=1 45, ToT b=5 74 (%). 100 hard games, indices 901-1000 of 1,362. Oracle best-of-100: IO 33, CoT 49 | Yao 2023 [a03, b01, c01] K01 | single-source; re-open confirmed |
| Independent ToT re-runs disagree with 74% | 69 (AoT, b=5, 109 queries); 60.6 (b=3) and 34.3 (b=1) in XoT; 77 (b=3) and 65 (b=1) in Token Economies | [a12, b09, b19, b13] K02 | contested |
| Early commitment is the CoT failure | About 60% of CoT samples fail at step 1 | Yao [a04] K03 | single-source |
| Crosswords: pruning and backtracking matter | ToT letters/words/games 78/60/20; IO 38.7/14/0; CoT 40.6/15.6/1; oracle best state 82.4/67.5/35; no prune 65.4/41.5/5; no backtrack 54.6/20/5. 20 games | Yao [a07, b04, c04] K04 | single-source |
| Creative Writing (self-judged) | GPT-4 coherence IO 6.19, CoT 6.93, ToT 7.56; refine 7.67/7.91. Humans: ToT 41, CoT 21, similar 38 (100 pairs) | Yao [a06, b03] K23 | single-source, weakened |
| Strong generator needed | GPT-3.5 ToT 19 vs GPT-4 74; GPT-4 gen + GPT-3.5 eval 64; GPT-3.5 gen + GPT-4 eval 31. GPT-3.5 writing: 4.47/5.16/6.62 | Yao [a08, b05, c05] K05 | established |
| Easy tasks: no gain | GSM8K IO 51, CoT 86, ToT 90; StrategyQA 73/82/83 (n=100). GPT-4o: GSM8K CoT 94.7 vs ToT 93.5; ProntoQA 91.8 vs 32.8 | Yao [b06]; Sys2Bench [d01] K09 | established |
| Cost | ToT 5.5k completion tokens, $0.74 per case; CoT best-of-100 6.7k, $0.47, 49%; IO best-of-100 1.8k, $0.13, 33%. Writing about 5x CoT. Authors: 5-100x | Yao appendix [a05, b07] K06 | single-source |
| Matched budget depends on model | GPT-4: ToT b=5 top-1 74 (best-of-all 76) vs CoT-100 top-1 17 (best-of-all 56). GPT-3.5: ToT top-1 25 (best-of-all 35) vs CoT-100 top-1 4 (best-of-all 46) | Wang 2024 [a13, b13, c08] K07 | established; metric-dependent |
| The evaluator carries signal | Random evaluator: GPT-4 top-1 0.0 (best-of-all 0.04). GPT-3.5 evaluator 68 top-1 (72 best-of-all), cost about 1/5 ($33.53 vs $159.87). Evaluate-once 73 | Wang [a25, b14, c08] K08 | single-source |
| Self-verifier is imperfect | GPT-4 on Game of 24: accuracy 87.0% (3567/4100), false positive 10.4% (320/3071), false negative 20.7% (213/1029). Self-critique lowered accuracy; sound verifier raised it (5% to 36-38%) | Stechly [a14, c12] K10 | established |
| Self-correction without oracle hurts | CommonsenseQA 75.8 to 38.1 to 41.8; GSM8K 75.9 to 75.1 to 74.7; kept first answer 74.7% | Huang [a15, b21] K11 | single-source |
| Code successor and goal test | 1362/1362 Game of 24 solved, 1.92-6.83 s total; crosswords 20/20 with given candidates. LLM+P Blocksworld 90 vs ToT 0 | Katz [b15, c17]; Liu [d17] K12, K30 | single-source |
| Search trace in one prompt (AoT) | 71% with 1 query vs ToT 69% with 109.1 queries (5,450 vs 13,900 prompt tokens). Crossword words 52 vs 46.5 | Sel [a12, a24] K13 | single-source |
| Graph merge | GoT sorting 128 numbers: median error 62% below ToT, over 31% cheaper (GPT-3.5); at 64 numbers 65% below CoT, 83% below IO | Besta [a17, c09] K14 | single-source |
| World-model search | Blocksworld LLaMA-33B RAP(10) 100/86/26 at 2/4/6 steps vs GPT-4 CoT 50/63/40. GSM8K: CoT+SC(10) 46.8, RAP(1) 40.0, RAP(10) 48.6 | Hao [a10, b11, d19] K15 | single-source |
| Self-eval beam search | Codex GSM8K 85.5 vs 80.4; AQuA 64.2 vs 58.6; StrategyQA 77.2 vs 73.2. Equal cost Llama-2 13B 46.1 (12.6k tokens) vs SC 41.8 (13.9k). Short commonsense: 70.6 vs 71.0 | Xie [a11, b12] K16 | single-source |
| Tree with PRM | Beam beats best-of-N at low budget, medium-hard items; loses on easy items, high budget. Compute-optimal matches best-of-N with up to 4x less compute. REBASE: Llemma-7B 46.8 at 1.48e14 FLOPs vs Llemma-34B 46.7 at 12.1e14; MCTS below sampling | Snell, Wu [b16, b17, d07, d08] K17 | established; needs trained PRM |
| Multi-tree (FoT) | Game of 24: FoT 96.84 at 25.64 calls vs ToT 74.00 at 13.74 calls (about 1.9x). XoT 85.40. Llama3-8B ablation: base 10.58, +self-correction 60.24, +input enhancement 77.98 | Bi [a18, b18, d20] K18 | contested; authors-only |
| Web agent tree search | VisualWebArena 18.9 to 26.4%; WebArena +28% relative to 19.2% | Koh [c22] K19 | single-source |
| Training on search traces | Countdown: 51.27 vs 25.73 (optimal-path); Searchformer 93.7% Sokoban | Gandhi; Lehnert [a19, b23] K20 | established; training only |
| Reasoning models | o1-preview Blocksworld 97.8 vs best LLM 62.6; 23.6% on 20-40 step plans. Plain o1 Blocksworld 99.2 vs GPT-4o ToT 12.4 | Valmeekam; Sys2Bench [b22, c19, d02] K21, K26 | established / single-source |
| Task-type split on GPT-4o | ToT beats SC@5 on Game of 24 (62 vs 18); loses on GSM8K 93.5 vs 94.9, ProntoQA 32.8 vs 91.4, HotPotQA 38.2 vs 52.6, Blocksworld 12.4 vs 37.5 (CoT). SC@5 not token-matched | Parashar [d01] K24 | established |
| Search plus hard evaluator | Mind Evolution TravelPlanner 95.6 vs BoN 55.6 at 800 candidates, $0.29 vs $0.47 per problem. PlanSearch pass@200 77.0 vs 55.6 (Claude 3.5 Sonnet) | Lee; Wang [d04, d05] K25 | established |
| Pick step is the bottleneck | Coverage 82.9% to 98.44% (100 to 10,000 samples); majority vote and reward model only 40.50% to 41.41%. LLM judge of research ideas 53.3% vs chance 50; human reviewers 56.1% | Brown; Si [d06, d15] K27 | established |
| Panel of judges | 3 small models: kappa NQ 0.763 vs GPT-4 0.627, 7-8x cheaper. Self-preference: GPT-4 recognises itself 73.5% | Verga; Panickssery [d13, d14] K28 | single-source |
| Width by agreement | 3.2x fewer samples at -0.07% accuracy (17 datasets); up to 7.9x | Aggarwal [d09]; Snell [d08] K29 | single-source |

## 4. Mechanisms and models

This section gives enough detail to implement each piece.

### 4.1 The base loop (Yao)

```
frontier = [root_state]
for step in 1..T:                      # T = 3 for Game of 24
    candidates = []
    for s in frontier:
        candidates += propose(s)       # LM call, k thoughts
    scores = [value(c) for c in candidates]   # LM call(s) per candidate
    frontier = top_b(candidates, scores)      # b = 5 (BFS)
answer = best(frontier)
```

Settings reported [a02, a21, b25]:
- Game of 24: BFS, 3 steps, b=5. The propose prompt lists next-equation options. Each state is valued 3 times with the labels sure / maybe / impossible, and the labels are mapped to numbers and summed. "Impossible" states are dropped.
- Creative Writing: depth 2. Sample 5 plans, vote (5 votes), then 5 passages from the best plan, vote (5 votes). b=1.
- Crosswords: DFS, cap 100 steps. 5 proposal prompts per node. Never overwrite a filled word, so depth is at most 10. Prune a state when the evaluator says a clue cannot be filled; backtrack to the parent. The prune step wrongly cut valid but rare words [K04].

Call count. With b=5, 3 steps and 3 value samples per state, Game of 24 needs about 100 calls and 5.5k completion tokens per game [a05]. Independent counts: 109.1 queries [a12]; 39.8 calls for b=3 and 23.5 for b=1 [b19].

### 4.2 Sources of the gain, with levers

- Breadth: b=1 gives 45%, b=5 gives 74% [a22]. Token Economies finds b=3 about equal to b=5 (77 vs 74) and b=1 at 65 [c08]. Breadth saturates fast. FoT says widening to 32 leaves gives nothing more [b18].
- Prune and backtrack: remove either and crossword word success falls from 60% to 41.5% or 20% [a07].
- Scorer: a random scorer gives 0%; a GPT-3.5 scorer gives 68% (GPT-4 proposer). The proposer matters more (GPT-3.5 proposer with GPT-4 evaluator: 31-38%) [b14, c05].

### 4.3 Code-checked tree (Long; our natural fit)

Replace the LM scorer with a program. The checker returns valid / invalid / complete for a partial state. A controller issues backtrack when the checker rejects a state or after a fixed number of children without progress [a09, b26]. Limit: a checker that only tests validity cannot tell whether a valid partial board is completable; this wasted rounds (4x4: 1 failure of 10; 5x5: 2 of 10) [b26].

### 4.4 Formalised search (Thought of Search)

Ask the model once for `successors(state)` and `is_goal(state)` as code, then run BFS or DFS in plain code. Game of 24: all 1362 instances, 1.92-6.83 s total, 1.2 interactions on average for the successor function [b15, c17]. Cost estimate for GPT-4-turbo: $40 for IO/CoT, $14,000 for RAP, $16,000 for LATS. Condition: a formal domain model must exist and names must be meaningful. LLM+P without a worked example scores 0 everywhere [d17]; Silver's GPT-4 programs solved 0.90 on 3 of 7 domains but 0.01-0.10 on two, and debugging loops were essential (Delivery 0.10 without debugging) [d18].

### 4.5 State rewrite (RAP)

After each accepted step, restate the problem state, so the next step judges only the remainder. The reward mixes likelihood, self-evaluation and task heuristics. More search budget goes to early steps [a23]. Blocksworld LLaMA-33B RAP(10) 100/86/26%, but it loses to GPT-4 CoT at 6 steps with 10 iterations (26 vs 40) [b11]. There is no ablation of rewrite against branching [d19].

### 4.6 One-pass imitation (AoT)

Write DFS traces, with false starts and backtracking, as the few-shot examples. The model imitates the search at temperature 0 in one pass [a24]. Game of 24: 71% with 1 query, 998 completion tokens. Crossword: about 25x fewer tokens than ToT. Caveat: the authors ran ToT themselves (69%), and prompted examples are example-bound in planning [c18].

### 4.7 Merge and parallel trees

- Graph of Thoughts adds an aggregate operation. It works where parts can be solved separately and recombined (sorting 128 numbers) [a17].
- Forest-of-Thought runs several independent trees with sparse activation, self-correction and input enhancement. The gain is mixed with self-correction and prompt rewriting [d20].

### 4.8 Width and depth by difficulty (no trained scorer)

- Sample 3-5 attempts. If they agree, stop. If they split, widen. Adaptive-Consistency: 3.2x fewer samples at -0.07% accuracy [d09].
- Snell: easy items revise one answer sequentially; medium-hard items branch; level-5 items see no method progress [d08]. Their difficulty signal needs a PRM or a pass rate.

### 4.9 Value step design

- Value each state alone for short checkable states; vote across states for open text [a02].
- Use a scorer that is not the generator where possible: models favour their own output [d13]; a panel of three diverse small models beat one GPT-4 judge [d14].
- Mind Evolution and PlanSearch bind the tree to a programmatic evaluator or unit tests and gain strongly [d04, d05].

## 5. What holds up

**Holds up (several sources).**
1. A strong generator is needed. Yao (GPT-3.5 19% vs GPT-4 74%), Token Economies (GPT-3.5 ToT top-1 25%), FoT (Llama3-8B ToT 10.58%), XoT (GPT-3.5 b=3 10.22%) agree in direction [K05].
2. On easy tasks where CoT works, the tree adds nothing: Yao (GSM8K 86 to 90, StrategyQA 82 to 83, n=100), Xie (short commonsense slightly below CoT), Sys2Bench (GSM8K 93.5 vs 94.7) [K09].
3. Matched-budget results depend on model and task, not on the method name [K07, K24].
4. A hard external evaluator makes search pay: Mind Evolution, PlanSearch, Long's Sudoku checker [K25].
5. Intrinsic self-evaluation is weak where checking is hard [K10, K11, K27].
6. Reasoning models absorb the search internally [K21].

**Replications and failed replications.**
- Game of 24 with GPT-4: no independent group got exactly 74%. Re-runs: 69, 60.6 (b=3), 77 (b=3 Token Economies), and at b=1: 34.3 vs 45 vs 65. The spread at b=1 is 31 points. Prompt and test set differ [K02]. We must measure our own baseline.
- The FoT table copies ToT's 74% (GPT-4) next to its own Llama3-8B numbers, so rows mix models [critique]. FoT 96.84% has no independent run [K18].
- No peer-reviewed replication of prompt-only ToT on a non-puzzle task was found. LATS, RAP and FoT are by authors of the new method [critique].
- Creative writing: only the original. The judge is GPT-4 and the human raters were the authors. Independent work shows LLM judges of creative writing do not correlate with experts [d16, K23].

**Moderators.**
- Task: checkable puzzle (wins), easy reasoning (no gain), formal logic (ProntoQA 32.8 vs 91.8, large loss), planning (mixed) [d01].
- Model: weak generator loses; reasoning model does not need it [d02].
- Budget: the tree wins at low budget with a trained scorer, and loses its edge at high budget and on easy items [d08].
- Metric: GPT-3.5 shows ToT ahead at top-1 (25 vs 4) and behind at best-of-all (35 vs 46) [critique correction 2].
- Evaluator: random kills the gain; a weaker but non-random one is enough on Game of 24 [K08].

**Interventions that worked.**
- Code checker or simulator in place of the model scorer (Long; Mind Evolution; PlanSearch; Katz).
- Backtracking and pruning on crosswords (single source).
- A cheaper evaluator (68% for one fifth of the cost).
- Early stop when samples agree (3.2x savings).
- Training on traces with dead ends (training, not scaffold).

**Interventions that did not work or are unproven.**
- MCTS: Wu found it below plain sampling at every budget with dozens of times more tokens; DeepSeek dropped it [b17, b24].
- Lookahead search under a PRM underperformed beam at equal generation budget [c20].
- Majority vote and reward-model picking plateau when coverage keeps growing [d06].
- LLM-judge picking of ideas: 53.3% vs 50% chance [d15].
- Self-correction without oracle feedback [K11].
- Prompted CoT or search examples decay with problem size beyond the examples [c18].
- Long reasoning chains: shortest chains are more accurate [d10, d11].

## 6. Language models

**GPT-4 (2023).** Game of 24: 74% for ToT against 4-9% for CoT and CoT-SC. The same model with a code search solves 100% [K01, K12]. On Sys2Bench (GPT-4o, 2025), ToT gets 62 vs SC@5 18 on Game of 24, but 93.5 vs 94.9 on GSM8K, 32.8 vs 91.4 on ProntoQA, 38.2 vs 52.6 on HotPotQA, 12.4 vs 37.5 (CoT) on Blocksworld. Llama 405B: Game of 24 ToT 69; Blocksworld ToT 19.9 vs CoT 48.7. SC@5 is not token-matched [d01].

**GPT-3.5.** The ToT gain shrinks and flips under matched budget. Yao: ToT 19 vs IO 6, CoT 3 (still ahead of those baselines). Token Economies: top-1 ToT 25 vs CoT-100 4, but best-of-all 35 vs 46, and the text says SC wins [K07]. Long's Sudoku (GPT-3.5) works because a code checker does the scoring [a09].

**Small open models.** Llama3-8B base ToT on Game of 24 is 10.58%; self-correction plus input enhancement gets 77.98% [d20]. So a tree alone does not help small models; added correction does. This is a method-author result.

**Reasoning models.** Plain o1 / o1-mini: Game of 24 73 / 77; Blocksworld 99.2 / 48.3; GSM8K 98 / 98; against GPT-4o ToT 62, 12.4, 93.5 [d02]. o1-preview Blocksworld 97.8, but 23.6% on 20-40 step plans [c19]. Wrappers: o3-mini high on 100 HLE questions 13.0, with SC(5) 18, MCTS(2) 28, Best-of-N(3) 37 (n=100) [d03]; o1-mini PlanSearch +0.5 (90.8 to 91.3 pass@200) [d05]; QwQ with FoT +0.6 on MATH500 (90.6 to 91.2), AIME 50.0 to 53.3 [d20]. Inside the reasoning model, shortest-chain voting short-3@k beats majority by about 2% (QwQ) and 4% (R1-670B) [d10]. There is no clean test of an external ToT on a reasoning model.

**What changed the result, and by how much.**
- Model strength: 19 to 74 points (GPT-3.5 to GPT-4) on Game of 24.
- A code checker in the loop: 55.6 to 95.6 (TravelPlanner) at the same 800 candidates; 55.6 to 77.0 (LiveCodeBench pass@200).
- Formal code replacing the LM: 74 to 100.
- A reasoning model replacing the tree: 12.4 to 99.2 on Blocksworld.
- Breadth b=1 to b=5: 45 to 74 (Yao); 65 to 74-77 (Token Economies).

## 7. What our agent should take

Schema part key: G guardrail, S state, O operator, M memory. Status: [E] established (2+ independent sources), [S] single-source, [C] contested.

### Add now (established)

| # | Take | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep the tree inside S6 only. Open it for items that fail the cheap first pass; do not use it where a plain attempt already works. Agrees with G1 and G12. | S6, G12 | [E] | K09, K24; b06, d01, a11 |
| A2 | Bind every tree node to a code check where one exists (checker, unit test, constraint test). Code, not the model, ranks and prunes. | S4, S6, G5 | [E] | K25, K10; d04, d05, a09, a14 |
| A3 | Do not let the model score its own answers as the final pick on uncheckable tasks. Dedup, then pick by code or a blind pairwise ranking with a different model; keep G8. | S7, G5, G8 | [E] | K27, K10; d06, d15, d16, a14 |
| A4 | Never revise on the model's opinion alone; a revision needs real output. | S5, G2 | [E] | K11, K10; a15, b21, a14 |
| A5 | Report accuracy at matched tokens against sampling plus vote, with a plain baseline and the metric named (top-1, not best-of-all). | G7, logging | [E] | K07, K06; a13, a05 |
| A6 | Do not quote 74% as our expected gain. Measure our own baseline on the same split. | G7 | [E] | K02; a12, b19, b13 |
| A7 | If the base model is a reasoning model, try parallel short samples with a short-chain preference before any external tree. | G11, S3 | [E] | K21, K26; d02, d10, d11 |
| A8 | Search only where the class shows some success. Weak generators gain little from a tree. | G12 | [E] | K05; a08, c05, d20 |
| A9 | Keep the schema's small tree (3 children, depth 2): breadth beyond b=3 gives little, and large trees cost 5-100x. | S6 | [S] on exact size, [E] on direction | K06, K02, K29; c08, b18 |

### Test first

| # | Take | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | At S6, compare a tree of operator-children (O1-O8) against 3 samples plus a vote, equal tokens. | S6, O1-O8 | [S] | K01, K07; d01 |
| T2 | Try writing a small program for successor and goal test (or a checker or simulator) first; use an LLM tree only if none can be coded. | S6, S4 | [S] | K12, K30; b15, d17, d18 |
| T3 | Use agreement among 3-5 samples as the difficulty signal: unanimous, stop; split, widen the tree. | S0, S6, G12 | [S] | K29; d09, d08 |
| T4 | Rewrite the problem state after each accepted subgoal and judge only the remainder. | S6, S2 | [S] | K15; a23, d19 |
| T5 | Score thoughts with a different model or prompt than the generator, blind, order-randomised. | S6, G5 | [S] | K28; d13, d14 |
| T6 | Cheap scorer: compare a small or cheap evaluator against the full model. | S6 | [S] | K08; b14 |
| T7 | One-pass search trace in the prompt instead of an external tree (AoT). | S6, mode | [S] | K13; a12 |
| T8 | Ablate prune and backtrack on an item set with dead ends. | S6 | [S] | K04; a07 |
| T9 | Allow merging of partial ideas on decomposable items. | O3 plus merge | [S] | K14; a17 |
| T10 | Two small trees against one big tree at equal tokens. | S6 | [C] | K18; b18, d20 |
| T11 | Branch only at the first decision against late branching. | S6 | [S] | K03; a04 |
| T12 | Open-mode idea tree with independent blind judge. | S3 open, S7 | [C] | K23, K27; a06, d16 |

## 8. Concrete tests on our bench

All tests run both arms at equal total tokens, same model, same items, setup cost counted (G7). Use at least 3 seeds. Report top-1 only.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Checkable puzzles with early dead ends (word puzzles, small arithmetic search, ARC subproblems with a held-out check) | Operator tree at S6 (3 children, depth 2) vs 3 independent samples plus code vote | Pass rate on unfitted check | Tree ahead only on items the plain model fails; near zero on easy items. Expect +5 to +20 points on the hard strata, by analogy with Game of 24 [K01, K24], with a wide discount since results are task-bound |
| B2 | Same set, plus easy items | Tree gated on first-pass failure vs tree always on | Tokens per solved item; pass rate | Gate saves a large share of tokens with equal pass rate [K09] |
| B3 | Items with a codeable checker | LLM scorer tree vs code-checker tree | Pass rate; false-positive rate of the scorer | Code tree higher; LLM scorer false positive about 10%, false negative about 20% on arithmetic [K10, K25] |
| B4 | Items where a simulator or successor function can be written | Per-node LLM tree vs LLM-written search program | Pass rate; tokens | Program equal or better at a fraction of tokens on formal items; no help on the rest [K12, K30] |
| B5 | Mixed difficulty | Fixed width vs agreement-routed width (unanimous stop; split widen) | Pass rate at equal total tokens | Same accuracy with about 2-3x fewer samples [K29] |
| B6 | Open idea items (NoveltyBench style) | Tree with generator self-scoring vs tree with different-model blind scorer vs random pick | Distinct-idea count, blind external rating | Self-scorer close to random [K27]; different model small gain [K28] |
| B7 | Multi-step items beyond example length | Tree vs plain, on instances larger than the prompt examples | Pass rate by size | Gain decays with size [K22] |
| B8 | Items with a dead-end structure | Tree with and without backtrack; with and without prune | Pass rate | Removing backtrack costs the most (crossword 60 to 20) [K04] |
| B9 | Reasoning-model base (if used) | Model alone with short-chain preference vs plus external tree | Pass rate at equal tokens | Little gain from the tree [K26] |
| B10 | Decomposable items | Tree vs tree with merge | Error, tokens | Merge ahead on decomposable only [K14] |
| B11 | Any | State rewrite per accepted step vs none | Pass rate on long items | Larger gain at 4+ steps [K15] |

Logging for all: which depth the winning branch came from, at which step wrong ideas died (K03), scorer verdict vs code verdict per node.

## 9. What does not transfer, and why

- **The 74% figure.** It is for one model (GPT-4, May 2023), one task, one prompt, 100 games [K01]. Re-runs give 34 to 77.
- **Training on search traces** (Stream of Search, Searchformer): needs training; our agent is a scaffold only [K20].
- **Trained reward models** (Snell, Wu): the gain needs a PRM; we have none [K17].
- **MCTS-heavy schemes** (RAP, LATS): too costly; MCTS lost to plain sampling and DeepSeek dropped it [b17, b24].
- **Tree search over real environment states** (Koh): needs a reversible environment; ours is text only [K19].
- **Crossword and Game of 24 results** are puzzles with exact checks and dead ends visible after one step. Open reasoning does not have these.
- **Creative Writing gain**: the judge was GPT-4 and the raters were the authors. Independent work says LLM judges miss creativity [d16]. Do not use it to justify an open-mode tree.
- **FoT 96.84%**: no independent run; rows mix models; gain partly from self-correction [K18].
- **LLM+P and Silver**: need a formal domain model; not available for open tasks [K30].
- **Reasoning-model internal search**: this is trained behaviour, not a prompt. We can only use the model, not copy it [K21].
- **Human parallels**: none used here. ToT is an engineering design, not a model of human thought. Human search findings are in the earlier C05 documents.

## 10. Open questions

1. Does a prompt-only tree at S6 beat self-consistency at equal tokens for a 2025-26 frontier model on non-toy tasks (math, code, open reasoning)? Sys2Bench says only Game of 24, with unmatched SC. No clean test.
2. Does an external ToT add anything on top of a reasoning model's own chain? Only hints (o3-mini HLE n=100; o1-mini +0.5; QwQ +0.6).
3. What is the false-positive rate of a prompt-only scorer on idea-generation tasks? Not measured by anyone found. Game of 24 gives 10.4% only.
4. What width and depth rule works without a trained reward model? Agreement-based early stop and Snell's difficulty rule exist, but not as a prompt-only tree rule.
5. What share of our tasks can be formalised enough for the code route? Not measured.
6. Is there an independent creative-writing ToT replication with a blinded independent judge? Not found.
7. Is the multi-tree gain real at equal tokens outside the method authors?
8. How much of the gain is state rewrite and how much is branching? No ablation.
9. Does scorer diversity help inside a tree? Indirect support only.
10. Why do independent GPT-4 results at b=1 range from 34% to 65%? Prompt details, test set and sampling settings are not controlled.
11. Not opened: c26 (CS224N project) and c27 (Meta-CoT) are snippet-only leads. Tree of Uncertain Thoughts tables were not read. Snell, Wu and Koh numbers were not re-opened in the critique pass.
12. The search for a third-party ToT-on-reasoning-model study and an FoT replication was cut short by budget. "Not found" does not mean absent.

## 11. Sources

[V] = opened and read in full or in the relevant sections. [M] = snippet only.

1. [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (a01-a08, a21, a22, b01-b07, b25, c01-c05)
2. [V] Long (2023) Large Language Model Guided Tree-of-Thought. https://arxiv.org/abs/2305.08291 (a09, b08, b26, c06)
3. [V] Hao et al. (2023) RAP. https://arxiv.org/abs/2305.14992 (a10, a23, b11, c15, d19)
4. [V] Xie et al. (2023) Self-Evaluation Guided Beam Search. https://arxiv.org/abs/2305.00633 (a11, b12, c16)
5. [V] Sel et al. (2023) Algorithm of Thoughts. https://arxiv.org/abs/2308.10379 (a12, a24, b09, c07)
6. [V] Wang et al. (2024) Reasoning in Token Economies. https://arxiv.org/abs/2406.06461 and https://aclanthology.org/2024.emnlp-main.1112.pdf (a13, a25, b13, b14, c08)
7. [V] Stechly, Valmeekam, Kambhampati (2024) On the Self-Verification Limitations of LLMs. https://arxiv.org/abs/2402.08115 (a14, a26, c12)
8. [V] Huang et al. (2024) LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (a15, b21, c13)
9. [V] Mo and Xin (2023) Tree of Uncertain Thoughts. https://arxiv.org/abs/2309.07694 (a16, c10; table cells not read)
10. [V] Besta et al. (2024) Graph of Thoughts. https://arxiv.org/abs/2308.09687 (a17, b10, c09)
11. [V] Bi et al. (2024) Forest-of-Thought. https://arxiv.org/abs/2412.09078 (a18, b18, c11, d20)
12. [V] Lehnert et al. (2024) Searchformer. https://arxiv.org/abs/2402.14083 (a19)
13. [V] Besta et al. (2024) Demystifying Chains, Trees, and Graphs of Thoughts. https://arxiv.org/abs/2401.14295 (a20, c25; intro only)
14. [V] Ding et al. (2023) Everything of Thoughts. https://arxiv.org/abs/2311.04254 (b19)
15. [V] Katz et al. (2024) Thought of Search. https://arxiv.org/abs/2404.11833 (b15, c17)
16. [V] Snell et al. (2024) Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314 (b16, c20, d08)
17. [V] Wu et al. (2024) Inference Scaling Laws. https://arxiv.org/abs/2408.00724 (b17, c21, d07)
18. [V] Stechly et al. (2023) GPT-4 Doesn't Know It's Wrong. https://arxiv.org/abs/2310.12397 (b20)
19. [V] Valmeekam et al. (2024) LLMs Still Can't Plan; Can LRMs? https://arxiv.org/abs/2409.13373 (b22, c19)
20. [V] Gandhi et al. (2024) Stream of Search. https://arxiv.org/abs/2404.03683 (b23, c23)
21. [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948 (b24, c24; negative result in prose only)
22. [V] Zhou et al. (2024) Language Agent Tree Search. https://arxiv.org/abs/2310.04406 (c14)
23. [V] Stechly et al. (2024) Chain of Thoughtlessness? https://arxiv.org/abs/2405.04776 (c18)
24. [V] Koh et al. (2024) Tree Search for Language Model Agents. https://arxiv.org/abs/2407.01476 (c22)
25. [V] Parashar et al. (2025) Sys2Bench / Inference-Time Computations for LLM Reasoning and Planning. https://arxiv.org/abs/2502.12521 (d01, d02)
26. [V] Drori et al. (2025) Diverse Inference and Verification. https://arxiv.org/abs/2502.09955 (d03)
27. [V] Lee et al. (2025) Mind Evolution. https://arxiv.org/abs/2501.09891 (d04)
28. [V] Wang et al. (2024) PlanSearch. https://arxiv.org/abs/2409.03733 (d05)
29. [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d06)
30. [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (d09)
31. [V] Hassid et al. (2025) Don't Overthink It. https://arxiv.org/abs/2505.17813 (d10)
32. [V] Zeng et al. (2025) Revisiting Test-Time Scaling of o1-like Models. https://arxiv.org/abs/2502.12215 (d11)
33. [V] Naik et al. (2023) Diversity of Thought. https://arxiv.org/abs/2310.07088 (d12)
34. [V] Panickssery et al. (2024) LLM Evaluators Recognize and Favor Their Own Generations. https://arxiv.org/abs/2404.13076 (d13)
35. [V] Verga et al. (2024) Replacing Judges with Juries. https://arxiv.org/abs/2404.18796 (d14)
36. [V] Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? https://arxiv.org/abs/2409.04109 (d15)
37. [V] Chakrabarty et al. (2024) Art or Artifice? https://arxiv.org/abs/2309.14556 (d16)
38. [V] Liu et al. (2023) LLM+P. https://arxiv.org/abs/2304.11477 (d17)
39. [V] Silver et al. (2024) Generalized Planning in PDDL Domains. https://arxiv.org/abs/2305.11014 (d18)
40. [M] Salahi et al., Stanford CS224N project. https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/final-projects/KamyarJohnSalahiPranavGurusankarSathyaEdamadaka.pdf (c26; snippet only)
41. [M] Xiang et al. (2025) Towards System 2 Reasoning in LLMs (Meta-CoT). https://arxiv.org/pdf/2501.04682 (c27; snippet only)

Cross-links to parallel subfields in this run (not covered here): Search over thoughts; Language Agent Tree Search; Neural and LLM proof search; Automated planning (STRIPS, PDDL); Compression at inference time; Metacognition and higher-order representation; Calibration and overconfidence.
