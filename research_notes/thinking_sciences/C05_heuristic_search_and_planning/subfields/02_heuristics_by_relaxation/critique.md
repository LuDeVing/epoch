# Critique: C05.02 Heuristic design by relaxation

Cross-checker pass, 2026-10-26. Claims are in `claims.jsonl` (C05.02-K01 to K24).

## 1. Numbers re-opened and checked (PDF text read this session)

| # | Number | Source | Result |
|---|---|---|---|
| 1 | hFF 234 vs 243 solved (Pyperplan, 720 tasks) | Correa et al. 2025, arXiv 2503.18809 | Text says 234, Table 2 sum row says 243. Both appear in the paper. Correction: use 243 (table); the 234 in the prose is an internal typo. LLM heuristics (305 to 373) beat both. |
| 2 | R1 373, V3 343, Flash Thinking 305; end-to-end R1 174, Flash 19, Thinking 202, V3 48; Fast Downward hFF 295, hadd 324, hcg 318, learned 371 | same | Confirmed in Table 2 and the FD table. |
| 3 | "423 is 38.7% higher than the next best ablation" (a21) | same | CORRECTED. The paper compares 423 with the heuristic chosen by training performance (305 = 423/1.387), not with the next best ablation. 423 is a best-of-25 picked on the test set. The meaning: selection by training score loses about a quarter of what was available. Claim K12 uses the corrected reading. |
| 4 | LM-cut 450 vs h_LA 422 vs Gamer 312 | Helmert and Domshlak 2009 | 450 and 422 confirmed (Table total). The text says Gamer solved 312, but the table total row reads 321 for Gamer. The paper is inconsistent. The "more than 400" in a17 is the paper's prose. With 321 the lead of LM-cut over Gamer is 129 tasks, with 312 it is 138. Either way the ranking holds. Other totals: merge-and-shrink 314, hmax 294, blind 273, HSPF 279. |
| 5 | Hoffmann 2005: 24 of 30 no unrecognised dead ends; 17 of 24 bounded exit from minima; 12 of 17 bounded from benches; 100 states sampled per instance; 230 groups, 5.0% and 2.2% exceptions, Grid and Hanoi | arXiv 1109.5713 | Confirmed (lines 167 to 176, 1809 to 1830). |
| 6 | Korf 1997: 8.764 expected (corners), 8.878 (max of three), 82 MB total, depth 17 about 122 billion nodes, median optimal length 18 | AAAI-97 PDF | Confirmed. |
| 7 | FF: 7663 helpful successors of 523030 over 637 states; Group A distinguished performance | arXiv 1106.0675 | Confirmed. |
| 8 | Step-back: PaLM-2L Physics 66.4 to 73.2, Chemistry 70.9 to 81.8, TimeQA 41.5 to 66.0 (68.7 with RAG); GPT-4+CoT 82.9 vs step-back 84.5 | arXiv 2310.06117 | Confirmed. |
| 9 | Thought of Search: 24 game D = 1362 | arXiv 2404.11833v3 | Dataset size confirmed. The ToT "75% on 100 problems" comparison was not re-read here (ToT paper reports 74% at breadth 5 in b22, and 75% is the figure Katz et al. quote). Small mismatch 74 vs 75; harmless. |
| 10 | Stein et al.: best LLM 194, BFS 258, A*+LM-cut 240, GBFS+hFF 260 of 260 | arXiv 2311.09830 | Confirmed in the results row. |
| 11 | Semantic Partial Grounding: 161 vs 139 of 175, PLOI 90 of 100, 36 of 175 not solvable for the original | arXiv 2602.22067 | Confirmed. Wording fix: 161 and 139 are "within time and memory limits", full grounding is the baseline (FG), not an LLM method. |

Not re-opened (carried as reported): Valmeekam 2023/2024 figures, Hirsch et al., Silver et al., Tuisov et al. (extension to Rust, column mapping unclear in extracted text, a Tuisov check only on the abstract of arXiv 2501.18784), AutoCO, Unpuzzles, Helmert 2006, Helmert and Roger 2008, Richter and Westphal 2010, Metric-FF.

## 2. Contradictions and tensions

- Accuracy of the relaxed score vs usefulness (K07). Helmert and Domshlak show more accurate relaxation (LM-cut) solves more optimal tasks. Helmert and Roger prove that even an almost perfect heuristic leaves exponential search in Gripper and Miconic. Not a strict contradiction, but it caps how much a better relaxed score is worth. Marked contested.
- LLM heuristics beat C++ hFF (373 vs 295) yet are not relaxations, and the win narrows to parity on a new domain (Rod-Rings 58 vs 59) and under renaming (66 to 40 in Blocksworld). So "LLM writes a heuristic" is evidence for the pattern "model writes scorer, code searches", not for relaxation.
- Least-to-most (99.7% on SCAN) vs the Chain of Thoughtlessness result (gains fade beyond the example class). Marked contested, with no direct head-to-head.
- Step-back helps PaLM-2L by 7 to 27 points but GPT-4 with plain chain-of-thought is already at 82.9 to 85.3. The gain depends on the base model.

## 3. Weak spots

- Many ids are the same paper read three times (a, b, c). Independent source counts in `claims.jsonl` count papers, not lines. FF 2001, Hoffmann 2005 and Hoffmann 2003 share an author and a framework.
- Almost all LLM evidence is on classical benchmark domains (Blocksworld, Gripper). None of it is on open-ended reasoning questions, which is our setting.
- Cost is not equal-token anywhere. Correa uses 25 sampled heuristics plus training runs; the headline 373 vs 174 does not charge that. API cost reported ($0.25 for V3/R1) is small but token counts are not matched to the end-to-end arm.
- LM-Landmarks (c13) is known only from a conference listing; no arXiv text was found. Treat as unverified.
- Step-back and least-to-most are abstraction and decomposition, not relaxation; they are included as the nearest measured LLM relatives.
- New forward citations found but not entered in evidence files (abstracts only): HTN planning with LLM-generated heuristics (arXiv 2605.07707: nearly matches the best HTN planner, less search effort on 83% of shared problems), and LeanPlan (arXiv 2610.08246: LLM heuristics with machine-checked admissibility proofs for optimal planning, up to 57 times more objects than training). Both extend the code-as-heuristic pattern; neither is a relaxation test.
- Pearl 1984, Culberson and Schaeffer, Bonet and Geffner, and the landmarks paper (Hoffmann et al. 2004) were never opened.

## GAPS

1. Does the rank of a model-made relaxed solve (drop one constraint, solve the easy version) predict the real test result of the full candidate, at equal tokens, on our problem classes? (No paper measures it; K22.)
2. Which constraint should be dropped, and does choosing it by code (for example, drop each stated constraint in turn) beat letting the model choose? AutoCO suggests the amount of relaxation matters; no test for text problems.
3. How often does a relaxed solve give a high score to a child that fails the real test, because the dropped constraint was the one that mattered (the dead-end failure of FF)? Which problem classes are like Mystery/Mprime?
4. At equal total tokens, does "model writes a scoring function, code ranks all children" beat the model rating children directly, once writing, testing and 25-sample selection costs are charged?
5. How much of the LLM-heuristic gain survives renamed or never-seen domains, across more models than o3 and R1? (K13 rests on one paper.)
6. Can the helpful-actions idea (use the relaxed solution to restrict which branches are expanded) cut tokens in S3 without lowering pass rate?
7. Does generating several different relaxations (a portfolio) help beyond one, given that samples from one model are correlated (G4)?
8. Does a code-verified model proposal (propose a must-do subgoal, check by relaxed reachability) improve over unverified proposals, outside PDDL (LM-Landmarks is the only evidence, and unverified)?
9. When does solving the simplified version first hurt, by pulling the model to a memorised answer (the unpuzzle effect)? Is a renamed-variant check enough to catch it?
10. Is there a cheap selection rule for generated scorers better than training-set performance (the 305 vs 423 gap)?

## Gap search results (2026-10-26)

Evidence in `evidence_d.jsonl` (d01 to d16, all opened this session). Claims K25 to K31 added; K02, K05, K09, K12, K13, K20, K21, K22 extended. WebSearch quota was used up, so papers were found through the arXiv site and direct links. Semantic Scholar and OpenAlex were rate limited, so forward-citation search was incomplete. The LM-Landmarks PDF was not reachable (OpenReview check page).

New papers opened: LeanPlan (2610.08246), HTN heuristics (2605.07707), LLM-evolved domain-independent heuristics (2605.29649), property-guided synthesis (2605.16142), structure vs semantics in planning difficulty (2610.26964), ToT as heuristic search (2605.28566). Re-opened: Correa 2025, AutoCO, Unpuzzles.

| Gap | Status | What was found |
|---|---|---|
| 1. Relaxed-solve rank vs real test result | OPEN | No paper measures it. Nearest: h_add ranks held-out instances by optimal plan length at Spearman 0.931 (d07), but a good rank still needed 140 real outcomes for calibration to route well (d09). A survey finds no ToT work with self-made relaxations (d10). |
| 2. Which constraint to drop; code vs model | OPEN | AutoCO has the model weight and relax constraints (SFL-8 52% to 80%, d11). No arm enumerates constraints by code. Text problems untested. |
| 3. High relaxed score, fails real test (dead ends) | PARTLY CLOSED | Evidence that it costs: a dead-end test was the largest single gain in LeanPlan (Spanner), and interaction-blind heuristics lose in Sokoban (d02). No measured rate for our problem classes. Treat tasks with one-way commitments as Mystery-like. |
| 4. Code scorer vs model rating, equal tokens | OPEN for children; PARTLY for full plans | Code scorer was cheaper than end-to-end plans ($0.25 vs $2.79 V3; $6.12 vs $13.62 R1; 200 vs 720 calls, d13). Selection cost is large in CPU (206.25 CPU-hours per domain), and a property-guided loop cut it about 1000x (d06). No test against a model rating children. |
| 5. Gain on renamed or new domains, more models | PARTLY CLOSED | New domains with other models agree (LeanPlan, d01; Gestrin and Seipp, d05; nine LLMs on HTN, d03). Renaming evidence is still one run (d14) plus Qwen direct-plan drop 67.5% to 40.0% (d08). K13 text updated; K25 added. |
| 6. Helpful actions in S3 | OPEN | Nothing new in text settings. |
| 7. Several relaxations beyond one | PARTLY | Five-model virtual best equalled the best single model on HTN coverage (d03). Diverse seeds helped evolution (d05). Not measured for relaxations of one problem. K27 single-source. |
| 8. Verified vs unverified proposals | OPEN | LM-Landmarks abstract only; no unverified arm reported (d15). LeanPlan shows verification can hold with a proof (d01). |
| 9. Memory pull; is a renamed check enough | PARTLY CLOSED | Context-shifted copies recovered accuracy for every model in 64 items (d12). Detector, not proof. |
| 10. Cheap rule for choosing scorers | PARTLY CLOSED | Two rules used: fewest expansions on the smallest training instance (HTN, d04) and a property counterexample loop (d06). No direct comparison to training-set coverage on the same pool. The 305 vs 423 gap is unchanged. |

Corrections noted while reading:
- LeanPlan Table 1 comes out of the PDF scrambled. Per-domain cells were not trusted; sums were used. Spanner: LeanPlan 72 vs SCP 30 (derived from the printed sums).
- HTN paper: "LLM" coverage is a virtual best over three search algorithms and five models; that favours the LLM columns.
- Gestrin and Seipp is a workshop paper; the 16-task margin over 720 is small.
- LM-Landmarks is a workshop poster abstract. Do not count it as a verified source.
- Not run in this pass: the HTN-planning and LeanPlan arXiv numbers (26xx) are 2026 preprints and have not been replicated.

Suggested tests that follow from the gaps (all at equal tokens): relaxed-solve rank vs full-candidate result per problem class (gap 1); drop each stated constraint by code vs model pick (gap 2); scorer-writing vs direct child rating, charging write, test and selection (gap 4); renamed-copy check on each relaxed solve (gap 9).
