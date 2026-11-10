# Tree of Thoughts: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C05.05-U1 | Does an operator tree at S6 beat k samples plus a vote on our items? | Keep S6 tree as designed; set tree size | S6, O1-O8 | K01 (single-source, GPT-4 2023, one task); K07, K24 (task-bound) | Tree (3 children, depth 2) vs 3 samples + code vote; hard checkable items; pass rate on unfitted check; 3 seeds | Tree wins by 5+ points on items the plain model fails, with no loss on the rest | High |
| C05.05-U2 | Can the first-pass-fail gate save tokens at no loss? | Hard gate: open the tree only after a failed first pass | S0, S6, G12 | K09, K24 (established direction; our gate not tested) | Gated vs always-on tree; mixed easy/hard items; tokens per solved item and pass rate | Equal pass rate (within 1 point) and 30%+ fewer tokens | High |
| C05.05-U3 | Does agreement among 3-5 samples work as a width signal? | Unanimous: stop; split: widen tree | S0, S6, G12 | K29 (single-source; d09 tests voting only, not trees) | Fixed width vs agreement-routed width; mixed difficulty; pass rate at equal total tokens | Same pass rate (within 1 point) with 25%+ fewer tokens, or +3 points at equal tokens | High |
| C05.05-U4 | Does a code checker or simulator in the tree beat an LLM scorer? | Make a code check the default node scorer; LLM scorer only where no check exists | S4, S6, G5 | K25 (established); K10 (scorer FP 10.4%, FN 20.7%, Game of 24 only) | LLM-scored tree vs code-checked tree; items with a coded check; pass rate; scorer FP/FN per node | Code tree ahead by 5+ points, or equal at 30%+ fewer tokens | High |
| C05.05-U5 | Can the agent write a successor and goal test (or simulator) and run plain search? What share of items qualify? | A "formalise first" step at S6 with fallback to the LLM tree | S6, S4 | K12, K30 (single-source; formal domains only) | Per-node LLM tree vs LLM-written search program; first count items that can be formalised; pass rate, tokens | Program route solves 80%+ of formalisable items and 30%+ of all items qualify; else keep only as an optional tool | Med |
| C05.05-U6 | Does an external tree add anything on a reasoning-model base? | Skip the tree in reasoning mode, or add it | S6, G11 | K21, K26 (hints only: o3-mini HLE n=100; o1-mini +0.5; QwQ +0.6) | Reasoning model with short-chain vote vs plus tree; hard items; pass rate at equal tokens | Tree adds 3+ points; otherwise forbid the tree in reasoning mode | High |
| C05.05-U7 | Does state rewrite after each accepted subgoal help, apart from branching? | Rewrite state at each accepted step | S6, S2 | K15 (single-source; no ablation, d19) | Tree with rewrite vs tree without; same branching; items with 4+ steps; pass rate | +3 points on 4+ step items | Med |
| C05.05-U8 | Does a scorer from a different model or prompt beat self-scoring inside a tree? | Cross-model blind scorer at S6 and S7 | S6, S7, G5 | K28 (single-source; not tested in trees); d13 self-preference | Same-model scorer vs different-model scorer vs random; blind, order-randomised; pass rate or blind external rating | Different scorer beats same-model by 3+ points and random by a clear margin | Med |
| C05.05-U9 | Is a cheap evaluator enough? | Use a small model for node values | S6 | K08 (single-source; Game of 24: 68 vs 74 at 1/5 cost) | Full-model scorer vs small-model scorer at equal total tokens; pass rate | Loss under 3 points at 40%+ lower cost | Med |
| C05.05-U10 | Do prune and backtrack each earn their cost? | Keep both, or drop one | S6 | K04 (single-source; 20 crosswords) | Tree with both vs no prune vs no backtrack; items with dead ends; pass rate | Each removal costs 5+ points; otherwise drop that part | Med |
| C05.05-U11 | Is a one-pass search trace in the prompt as good as an external tree? | A cheap "trace" mode | S6, mode | K13 (single-source; authors ran ToT) | Prompt with worked search trace vs external tree; checkable items; pass rate and tokens | Within 2 points at 50%+ fewer tokens | Med |
| C05.05-U12 | Does branching only at the first decision capture most of the gain? | Branch early only | S6 | K03 (single-source; 60% of CoT fails at step 1) | Branch at first step vs every step; log step where wrong ideas die; pass rate | First-step-only within 2 points at 40%+ fewer tokens | Med |
| C05.05-U13 | Is the open-mode idea tree real with an independent judge? | Tree for idea generation in open mode | S3 open, S7, G8 | K23 (single-source, self-judged); K27, d15, d16 (judges near chance) | Tree with different-model scorer vs plain many-draw + dedup; NoveltyBench-style items; distinct ideas and blind rating | Tree gives +10% distinct or rated ideas at equal tokens | Low |
| C05.05-U14 | Does merging partial ideas help on decomposable items? | A merge operator | O3 plus merge | K14 (single-source; sorting) | Tree vs tree with merge; decomposable items; error rate | Merge cuts errors 20%+ on decomposable items with no loss elsewhere | Low |
| C05.05-U15 | Two small trees vs one big tree? | Multiple trees | S6 | K18 (contested; authors-only) | One tree of size 2N vs two of size N with vote; pass rate | Two trees win by 3+ points | Low |

## Open questions we cannot test on our bench yet
- Frontier models in 2026 on non-toy tasks: we need a set of items where the plain model scores 20-70% and a check exists. This unblocks U1 and U6.
- The false-positive rate of an LLM scorer on idea tasks has never been measured. We need human-labelled idea quality or run-based truth for open items (blocks U8, U13).
- Reasoning-model access with a controllable thinking budget, to run U6 at truly equal tokens.
- Independent replication of FoT and of ToT creative writing: no third party found. We would have to run it ourselves with a blinded judge.
- The share of our tasks that can be formalised (U5) needs a task audit first.
- Why b=1 Game of 24 ranges from 34% to 65% across groups: no data on prompts. Low value for us; skip unless U1 shows an odd result.
- Unread leads: the Stanford CS224N project (evaluation matters more than search algorithm) and Meta-CoT. Only snippets seen.

## Order to run
1. U1 (tree vs samples plus vote at equal tokens): it decides whether S6 as designed is worth its cost at all.
2. U4 (code check vs LLM scorer): the best-supported way to make the tree pay, and cheap to build.
3. U2 with U3 (gate and agreement-routed width): cheap, can share the same runs, and they cut token cost for every later test.
