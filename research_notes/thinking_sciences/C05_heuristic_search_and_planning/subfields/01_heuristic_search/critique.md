# Critique, C05.01 Heuristic search (cross-check)

## Re-opened numbers (arXiv PDFs via pdftotext, this session)
Confirmed against the full text: ToT Game of 24 (IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74, CoT best-of-100 49), GPT-3.5 19%, mixed 64% and 31%, crossword oracle 7/20; Searchformer 93.7% optimal and 26.8% fewer steps, A* traces 34.3% longer; Koh et al. 26.4/39.7/19.2/28.0 with baselines 18.9/15.0; Correa et al. 373/343/305/234/174 of 720, $0.25 and $6.12; Katz et al. 1361 of 1362, ToT 75% on 100 problems, 14 days and over $1000; Gupta and Li Sokoban rows 73.94/80.28/82.04/56.69 and 9.5%; Valmeekam o1 97.8/52.8/37.3/23.63/12.7 and 0.12 s for Fast Downward; RAP table 0.17/1.00/0.86/0.88/0.42; LATS 83.8/92.7/54.4/63.1; LLM-A* 57.39, 74.96, 2.44.

## Corrections
1. a10 (ToT cost). The extracted table reads: IO best-of-100 $0.13 at 33%; CoT best-of-100 (6.7k/2.2k tokens) $0.47 at 49%; ToT (5.5k/1.4k) $0.74 at 74%. Line a10 gives $0.74 to CoT best-of-100. That is a mis-read. Row alignment comes from text extraction, so recheck on the PDF image before quoting costs.
2. a17, b09, c10 (Q*). The extracted tables are misaligned. The paper text says Q* reaches 80.8% GSM8K, 55.4% MATH and 77.0% MBPP, but the same numbers also sit on PPO(QVM) and Best-of-N rows in the raw table, and the Q* cells were lost. The GSM8K base is 65.2% in the text and 74.5% in the table (the paper disagrees with itself). Treat Q* numbers as "paper text claims", not verified table cells.
3. c02: the oracle crossword "35" is a percentage of games (7/20), matching the text.
4. a16, b12 and c13 are the same paper (arXiv 2312.01797; the author name differs between lines). a15 is a different paper (Meng et al., 2407.02511). Do not count these as three sources.
5. a21, b13, b14 and c18 share the o1 PlanBench numbers (2410.02162 and 2409.13373). Count as one independent source.
6. Hart, Nilsson and Raphael (1968, c25, a01), Dechter and Pearl (b20) and Pearl 1984 were not read from the original. The theory claims rest on Wikipedia.
7. Correa et al. footnote 5: on the eight IPC 2023 domains the best of three LLM heuristics solves 354 tasks, 19 fewer than R1 (373). The headline is somewhat narrower than it looks.

## Contradictions between sources
- Self-scoring helps (ToT, LATS, RAP). Learned scorers beat self-scoring (TS-LLM, Q*). Code-only search needs no scorer (Thought of Search, Correa). The right design depends on the task.
- Shorter search versus better answers (Gupta and Li): speed numbers alone mislead.
- RAP lifts LLaMA-33B, but GPT-4 CoT already gets 0.40 at 6 steps. Gains shrink with a stronger base model.
- LLM-A*: fewer nodes in one paper, but longer and less smooth paths in the other. Greedy LLM beats LLM A* on search size.

## Weak spots
- Nearly all numbers are single-lab and small (ToT 100 puzzles, crossword 20 games, o1 Sokoban 55).
- Most tree-search papers have no equal-token comparison; ToT compares only with best-of-100.
- No LLM study measures admissibility directly (how often a model score overestimates).
- Newell and Simon 1976 and the A* theorems come via Wikipedia only.
- No failed replication of ToT-style gains with newer reasoning models was found.
- b20 Dechter-Pearl, b21 Helmert-Roger, b22 Wilt-Ruml were not opened (opened:false). Their content is memory, not evidence.
- c12 (LLM-MCTS) column mapping is uncertain.

## GAPS
1. Do tree-search gains (ToT, LATS, RAP, Koh) survive at equal total tokens against best-of-N and self-consistency with 2025-26 reasoning models?
2. How accurate are LLM state-value scores as rankers (rank correlation, top-1 agreement with ground truth), and how often do they overestimate (an admissibility proxy)?
3. When does weighted or greedy ranking fail under heuristic error (Wilt and Ruml 2012, Helmert and Roger 2008)? Open both and extract numbers.
4. Are there failed or null replications of Tree of Thoughts (other models, other tasks) where ToT loses to plain CoT or best-of-N?
5. What breadth, depth and stopping rule are best, with measured curves on math, code and agent tasks, not only puzzles?
6. Do process-reward-guided searches (Math-Shepherd, rStar, ReST-MCTS, Let's Verify) beat self-scored search? Extract matched numbers.
7. Can a cheap scorer (small model, logprob, code heuristic) replace full LLM scoring with little loss, and at what token saving?
8. Read the originals: Hart-Nilsson-Raphael 1968, Dechter-Pearl 1985, Pearl 1984, for exact theorems and the pathological-case limit.
9. Re-extract Q* Tables 2-4 from the PDF image to settle correction 2.
10. Do people use admissible-like heuristics in problem solving, with measured error rates (Newell and Simon 1972)?

## Gap search results (gap searcher, new evidence in evidence_d.jsonl, claims K22-K32)

Search note: the WebSearch quota was used up, and OpenAlex and Semantic Scholar were rate-limited. Sources were found through arXiv PDFs by known ID, the UNH author page and the Basel institute page. The Hart-Nilsson-Raphael PDF and the Q* and ToT tables were read from rendered page images.

Closed
- Gap 9 (Q* tables): closed. Real cells in d19: GSM8K 65.2 base, best-of-N(QVM) 74.5, Q*(QVM) 78.8, Q*(PRM+QVM) 80.8; MATH 49.1 and 55.4; MBPP 77.0. Correction 2 is withdrawn: 74.5 is a best-of-N cell, not a base. Gain over best-of-N is only 1 to 4 points.
- Correction 1 (ToT cost): confirmed on the PDF image (ToT paper Table 7): IO best-of-100 $0.13 at 33%, CoT best-of-100 $0.47 at 49%, ToT $0.74 at 74%. Line a10 is wrong and should be fixed.
- Gap 3 (when ranking fails): closed for classical search, d17 and d18. Greedy works only when h tracks distance-to-go (Spearman 0.52 to 0.997 works; 0.39 to -0.03 fails). Percent error and h-h* rank correlation do not predict it. Even error-1 heuristics cause exponential A* work on GRIPPER and MICONIC.
- Gap 6 (PRM vs self-scored): mostly closed, d04 to d10. Step-level scorers beat voting by about 4 points (MATH best-of-1860: 78.2 vs 69.6; ReST-MCTS value 39.0 vs SC 35.1 on MATH500). Small models' self-reward is near random (rStar). The numbers come from different setups, so the ranking among PRMs is weak.
- Gap 8 (originals): partly closed. Hart-Nilsson-Raphael 1968 was read; the optimality theorems need consistency. Dechter-Pearl 1985 and Pearl 1984 were not found openly and remain unread.

Partly closed
- Gap 1 (equal tokens): ToT beats SC only with a strong base model (GPT-4) and loses with GPT-3.5 (d01); standard MCTS does not beat repeated sampling at equal calls on ARC-AGI or LiveCodeBench (d11). Still open: no test of ToT or LATS against SC with 2025-26 reasoning models was found.
- Gap 2 (ranker accuracy): no study reports rank correlation or top-1 agreement of LLM state scores. Proxies: GPT-3.5 direct evaluation at chance (50.6%), GPT-4 78.75%, binary verifier false positive 0.5 to 18.55% and false negative up to 97% (d02, d15). Admissibility itself is still unmeasured.
- Gap 4 (null replications of ToT): one partial hit, ToT below SC with GPT-3.5 (d01). No dedicated failed replication found.
- Gap 5 (breadth, depth, stopping): evidence from math. Beam search loses to best-of-N at high budget and on easy items (d04); saturation near 64 trajectories (d08); stopping rules save 34% to 84% of samples (d13). Agent-task curves not found.
- Gap 7 (cheap scorer): a GPT-3.5 evaluator keeps 72% vs 76% at about one fifth of the cost (d02); trained 7B PRMs are strong (d08) but need training.

Still open
- Gap 10 (humans and admissible-like heuristics): only an abstract (d20, opened:false). No error-rate data; Newell and Simon 1972 unread.

Other notes
- The corrections about a16/b12/c13 and the o1 family still stand.
- New caveat: many new gains are 1 to 4 points with no variance reported (Q*, ReST-MCTS, AB-MCTS), so treat them as direction only.
- Statuses changed in claims.jsonl: K01 and K20 and K07 to established, K02 to contested; K22 to K32 added.
