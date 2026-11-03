# Critique: E05.01 Design as problem solving (search in ill-structured spaces)

Cross-checker pass. Evidence files a, b, c (76 lines) read in full. 25 claims written to claims.jsonl (K01-K25).

## 1. Re-opened this session (PDF text via pdftotext, arXiv)
Opened again: Tree of Thoughts (2305.10601), Huang et al. self-correction (2310.01798), Si et al. ideation study (2409.04109). Numbers checked:

| Number | Result |
|---|---|
| Game of 24 IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74, CoT best of 100 49 | Confirmed (a13, b16, c01 agree) |
| About 60% of CoT samples wrong after step 1 | Confirmed |
| Crosswords: IO 38.7/14/0, CoT 40.6/15.6/1, ToT 78/60/20, best state 82.4/67.5/35, no prune 65.4/41.5/5, no backtrack 54.6/20/5 (letter %, word %, games solved %) | Confirmed. The "games" column is a percent (20% = 4 of 20). |
| Creative writing 6.19 / 6.93 / 7.56; humans 41 vs 21, 38 similar; refine 7.67 and 7.91 | Confirmed |
| Cost: ToT 5.5k completion tokens vs 6.7k for 100 CoT trials | Confirmed. This is the one near-equal-token comparison in the set (74% vs 49%). |
| GPT-3.5 + ToT on Game of 24 is 19%; GPT-4 generation + GPT-3.5 evaluation 64%; GPT-3.5 generation + GPT-4 evaluation 31% | New. Generation, not evaluation, is the bottleneck. Add to the record. |
| Huang oracle table: GPT-3.5 84.3 / 89.7 / 29.0; GPT-4 97.5 / 85.5 / 59.0 (GSM8K / CSQA / HotpotQA) | Confirmed. Standard prompting: GPT-3.5 75.9 / 75.8 / 26.0, GPT-4 95.5 / 82.0 / 49.0. |
| Huang intrinsic GPT-3.5 CSQA 75.8 -> 38.1 -> 41.8; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0 | Confirmed |
| Si: novelty 4.84 / 5.64 / 5.81; reviewer agreement 56.1% vs 66.0 (NeurIPS 2021) and 71.9 (ICLR 2024); 200 of 4000 non-duplicate; best ranker 71.4% | Confirmed |

## 2. Corrections
1. a21: the columns labelled "round 1 / round 2" are really call counts 1 / 3 / 5 in Huang Table 3. Values were right, labels wrong. Huang also sampled only 200 questions (100 for HotpotQA) for every model except GPT-3.5, and used temperature 1 for GPT-3.5 and GPT-4.
2. Huang also shows that multi-agent debate is no better than self-consistency at an equal number of responses, and that some "self-correction gains" come from a weak initial prompt. Not in a21 or b19. This supports G7 (compare at equal cost).
3. a15 / c02: the "no pruning 5% (1 of 20)" figure is a success rate on 20 games. The ToT text notes the no-prune variant still reached the right answer in some games, so treat the ablation as noisy.
4. a25 said the 2024-2026 design literature was unsurveyed. Angles B and C did cover it (b09-b15, c06-c15), so a25 is partly superseded. The core gap still holds (see K25).
5. c14 (Shin et al. 2025, N=280) and c06 (EngDesign) could not be re-opened: the arXiv, OpenAlex and Semantic Scholar queries returned empty or rate-limited results. Their numbers stay as the evidence agents wrote them and are not independently confirmed.

## 3. Contradictions between sources
- GPT-4 plain Blocksworld: 34.3% (PlanBench, a18) vs about 12% (Kambhampati, b21). Different prompts and dates. Do not quote one number as the GPT-4 figure.
- LLM creativity: Si (b23) says LLM ideas are more novel than experts. Chakrabarty (b26) says LLM stories pass creativity tests 3 to 10 times less often. Doshi (b13) says AI raises novelty but lowers group diversity. These may reconcile by measure: single-item novelty ratings vs group diversity vs expert test batteries. K17 is marked contested.
- Shin et al. (c14) found no benefit from LLM help in problem reframing, while Egea (b09) found strong concept generation. Different tasks (framing vs building) and measures.
- Simon 1973 (no special process for ill-structured problems) vs Rittel and Webber, Goel and Pirolli, Dorst and Cross (design is a different kind of space). Neither side has a direct LLM test. K01 stays single-source; a11 and a12 are abstract-only.
- LATS and RAP report gains at higher test-time budgets than their baselines (a20, a19). Only the ToT paper gives a token-matched figure.

## 4. Weak spots
- Almost all search gains are on tasks with a crisp checker (Game of 24, crosswords, Sudoku, Blocksworld, HumanEval). No opened study shows tree search helping on an ill-structured task judged by an outside verdict. This is the main risk to the S6 claim (K25).
- Small samples: 20 crossword games, 10 Sudoku puzzles per size, N=36 in the fixation study, N=9 designers.
- Judge problem: the open-ended wins (ToT writing, Si ideas) rest on model or noisy human ratings. Reviewer agreement in Si was 56.1%.
- Old models: ToT, PlanBench and Huang use GPT-3.5 and GPT-4 from 2023. Nothing opened tests a 2025-2026 reasoning model with a search scaffold against that model with its own long chain of thought at equal tokens.
- Human design fixation evidence is thin: one study opened in full (Neroni, b01-b04). The meta-analysis (b05) and Kruger and Cross (b06) were seen only as summaries.

## 5. Only seen in snippets or secondary text (opened:false)
a08 (Newell and Simon 1972), a09 (Reitman), a10 (Rittel and Webber; scanned PDF with no text layer), a11 (Goel and Pirolli), a12 and b07 (Dorst and Cross), b05 (Sio et al. meta-analysis; effect sizes not seen), b06 (Kruger and Cross), c21-c25 (background from memory). Claims K01, K12 and K19 lean on these. The c-lines on Shin, EngDesign, EngiBench and GraphicBench were read by the evidence agent and not re-opened by me.

## GAPS (most decision-relevant first)
1. At equal tokens, does a code-held search tree (S6) beat a strong reasoning model's own long chain of thought, and best-of-N with a verifier, on 2025-2026 models? ToT's 74% vs 49% was GPT-4 in 2023.
2. Does S6 help at all on a task with no crisp checker but with a delayed external verdict (for example a design brief scored by blind experts or a simulator)? Which sub-steps can be given a code check?
3. Which operator carries the gain in a design-style task: branching at the first decision, reframing the problem, relaxing a constraint, or backtracking? Ablate at equal tokens (ToT ablated only pruning and backtracking, on 20 games).
4. How much does a weak model evaluator cost in pruned-correct branches, and does a code or held-out check remove the loss? ToT lost 3 of 7 solvable crosswords to its output heuristic.
5. Does a constraint ledger checked by code reduce forgotten or violated constraints and order-dependence in multi-step design (Simon 1973's predicted failure; Egea's observed one)? No direct test exists.
6. Does a forced diversity step (name different families first, critique-critique pass) raise group-level diversity without lowering quality, and does it help or hurt on a verified task?
7. Does example-induced fixation transfer to LLMs in the controlled Jansson and Smith sense (flawed example, effect on repeated features), with an effect size, and does an alternatives operator remove it?
8. What are the effect sizes and moderators in the Sio et al. meta-analysis and the Goel and Pirolli / Dorst and Cross protocols (sample sizes, percentages)? Currently abstract-level only.
9. Can an LLM formulate the problem space (states, operators, goal test) reliably on non-toy tasks, as in Wray et al. beyond water jugs, and what share of failures come from the formulation step?
10. Is the gain from search at planning confounded by pattern recall? Mystery Blocksworld suggests so. Run obfuscated versions of every item in our test set.

## Gap search results
Evidence in evidence_d.jsonl (d01-d17, all opened as arXiv PDF text this session). claims.jsonl now has 32 claims (K04, K06, K09, K14, K15, K20, K24, K25 updated; K26-K32 added). arXiv listing search, Semantic Scholar and OpenAlex were rate-limited, so papers were fetched by known arXiv id only. This limits coverage: no 2025-2026 head-to-head paper was found by search.

| Gap | Status | What was found |
|---|---|---|
| 1 Equal tokens vs reasoning model and best-of-N | Partly closed | Stechly (d10): 150 plain queries with a sound verifier reach 70% vs ToT 74% at equal cost, so ToT's edge over verified sampling is about 4 points (K04 now contested). Wu (d03): MCTS needs dozens of times more tokens than voting. Shojaee (d05): at matched tokens non-thinking equals thinking at low complexity, thinking wins at medium, both collapse at high. Still open: a direct S6-vs-own-long-CoT test on 2025-2026 models. |
| 2 Open task with delayed verdict | Partly closed | Koh (d12): +39.7% and +28.0% relative on web tasks with an exact final check. Brown (d04): without a verifier, gains plateau. Still open: expert-judged design briefs (K25 stays). |
| 3 Which operator carries the gain | Open | Snell (d01) shows the best method depends on difficulty; Koh needs both depth and breadth; Shojaee (d06) shows early fixation. No equal-token ablation of branching, reframing, relaxing and backtracking was found. |
| 4 Weak evaluator cost | Closed enough | Stechly (d11): 20.7% of correct Game of 24 answers rejected. Koh (d13): scorer quality 28.5% to 37.0% to 43.5% (ground truth). Snell (d02): over-optimised verifier. A code check is the upper bound; no study yet measures the pruned-correct loss with and without it on the same items. |
| 5 Constraint ledger | Open | TravelPlanner (d14) quantifies the failure (63.3% per-item vs 2.0% per-plan commonsense pass; 0.6% final) but no ledger test was found. |
| 6 Forced diversity step | Mostly open | Artificial Hivemind (d15, d16): knobs do not help, sibling models are 71-82% similar. No test of a forced-family step on a verified task. |
| 7 Example-induced fixation in LLMs | Open | Nothing new found. |
| 8 Sio meta-analysis and protocol sizes | Open | Paywalled; OpenAlex and Semantic Scholar blocked. Still abstract level. |
| 9 Problem formulation reliability | Partly closed | Oswald (d17): 94% valid PDDL, 25% functionally equivalent, toy domains and old models. K24 now contested. No design-scale formulation test. |
| 10 Pattern-recall confound | Closed (as a risk) | PlanBench (d07, d08): obfuscation drops pre-reasoning models from 8-63% to 0-4.3%; o1-preview 97.8% to 52.8% to 37.3%. Action: obfuscate every test item. |

Corrections found while reading: the GPT-4 Blocksworld figure of 34.3% is one-shot; zero-shot is 34.6% in the same table. The earlier 12% figure is not in PlanBench Table 1. Table columns in Stechly's PDF text were partly garbled, so only the Game of 24 verifier row was quoted.
