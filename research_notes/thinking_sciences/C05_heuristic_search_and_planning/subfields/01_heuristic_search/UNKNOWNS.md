# Heuristic search (A*, best-first): what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C05.01-U1 | Does ranking children with a scoring call beat resampling with our model? | Rank-then-keep-b step at S6 | S6 | K02, K22; contested; GPT-4 only, loses with GPT-3.5, MCTS ties sampling | A: N attempts, code select. B: k children, score, keep b. Same total tokens. Puzzle items with checks, 3 seeds. Metric: pass rate | B beats A by 3+ points, CI excludes 0, on 2 item types | High |
| C05.01-U2 | Can a weaker, cheaper model rank children without losing the gain? | Cheap ranker (small model or yes/no prompt) | S6 | K04, K28; single-source, Game of 24 (72% at $33.53 vs 76% at $159.87) | Strong generator + strong ranker vs strong + weak ranker, equal tokens. Metric: pass rate, tokens | Weak ranker within 3 points at under half the cost | High |
| C05.01-U3 | How well do prompted child scores rank true outcomes (rank correlation, top-1 agreement)? | A measured ranker-quality gate for ranked search | S6/G | K26, K25; unmeasured for LLMs; Wilt-Ruml is classical only | Dev set of 100 items, 4 children each, run each to the end, correlate score with success. Compare 1-10, yes/no, logprob | Spearman >= 0.5 and top-1 agreement 15+ points above chance | High |
| C05.01-U4 | Does pruning on a model score drop true solutions, and does demoting instead of deleting help? | Soft prune (demote, revisit if budget remains) | S6/G | K06, K25; single-source (3 of 4 crossword solutions missed); false reject up to 97% | Hard vs soft vs no prune at equal tokens. Metric: pass rate, true solutions lost | Soft beats hard by 2+ points and recovers 30%+ of lost solutions | High |
| C05.01-U5 | Is backtracking the bigger ingredient? | Forced backtrack to the next sibling after a dead end | S5/S6 | K06; crosswords only (no backtrack 20 vs 60) | Ablate backtrack, prune, both. Metric: pass rate | Backtrack removal costs 5+ points | Med |
| C05.01-U6 | Do gains exist only on harder items? | Difficulty gate: search only if plain attempts disagree or fail | S0/S6/G12 | K15, K23; Gupta-Li, Snell; math and synthetic only | Always search vs gated search on a mixed-difficulty set. Metric: pass rate per token | Gated within 1 point of always-search at 30%+ fewer tokens | High |
| C05.01-U7 | Does an early-stop rule save tokens in tree search? | Stop expansion when top 2 children agree | S6 | K29; established for voting, untested for trees | Fixed budget vs stop rule. Metric: tokens at equal accuracy | 25%+ saving with at most 1 point loss | Med |
| C05.01-U8 | Does adding cost-so-far (g) to the score beat estimate-only? | Score = steps used + estimated remaining | S6 | K14, K26; classical and Sokoban; single-source | Greedy vs g + h. Metric: pass rate and solution length | g + h better by 2+ points or shorter at equal pass rate | Med |
| C05.01-U9 | Can the model write a scoring function in code that replaces per-node scoring? | Heuristic-as-code step for checkable classes | S6/tools | K12, K03; established for planning domains, not for our item types | Per-node LLM score vs one-time code heuristic. Metric: pass rate, calls per item | Code arm matches or beats at half the calls on 2 item types | Med |
| C05.01-U10 | Does diversity of candidate plans before ranking raise gains? | Plan-level sampling before code | S3/S6 | K19; single-source (77.0 vs 60.6 pass@200) | Plain draws vs plan-first draws, equal tokens, diversity measured. Metric: pass rate vs diversity | Plan-first beats plain by 3+ points | Med |
| C05.01-U11 | Does decomposition or symmetry pruning beat better scoring on combinatorial items? | Decompose-first operator for items with independent parts | S2/O | K27; classical worst case, one paper | Better ranker vs decomposition on items with many independent subparts | Decomposition wins by 5+ points | Low |
| C05.01-U12 | Do search gains survive on obfuscated items? | Keep search arm for renamed-entity items | S6 | K09; one lab (o1 97.8 plain vs 37.3 randomised) | Plain vs renamed items, rank arm vs best-of-N | Search arm loses under two thirds of what best-of-N loses | Low |
| C05.01-U13 | Do tree-search gains hold with a reasoning model (long thinking)? | Keep or drop ranked search for reasoning models | S6/G11 | K22; no test found with 2025-26 reasoning models; d12 is not tree search | Ranked search vs parallel samples + vote on our strongest model | Search wins by 3+ points; otherwise drop it | High |

## Open questions we cannot test on our bench yet

- Admissibility of LLM scores. Needs items with known true remaining cost. Unblock: a small set of puzzle items with known optimal solution length.
- Human heuristic error rates (Newell and Simon 1972, Pearl 1984 unread). Unblock: read the books and the 2023 Nature expertise paper in full.
- Trained scorers (PRM, Q-value). Gains of 1-4 points over best-of-N, but training is outside the scaffold. Unblock: a small trained ranker for one item type.
- Agent tasks with undo or reset (Koh et al. need it). Unblock: a resettable environment bench.
- Variance of 1-4 point gains (Q*, ReST-MCTS, AB-MCTS). Unblock: 5+ seeds on a shared item set.
- Failed replications of ToT. Unblock: rerun Game of 24 with newer models on the same 100 puzzles.

## Order to run

1. C05.01-U13 with U1: does ranked search beat parallel samples at equal tokens with our strongest model? This decides whether S6 ranking is worth keeping.
2. C05.01-U3: measure scorer rank correlation on a dev set. Cheap, needs no new arm, and gates every other ranking test.
3. C05.01-U4: hard vs soft prune. Cheap, and false rejects are the best-supported failure of model scoring.
