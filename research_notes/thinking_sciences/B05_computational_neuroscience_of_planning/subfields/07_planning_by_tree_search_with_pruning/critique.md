# B05.07 Planning by tree search with pruning: cross-check and critique

Cross-checker pass over evidence_a, evidence_b, evidence_c (79 lines). Sources re-opened this session (text read from PDF or PMC HTML): Yao 2023 (ToT), Koh 2024 (tree search for agents), Li 2026 (BAVT), Huang 2026 (UAA), Lally 2017, Faulkner 2022, Huys 2012, Huys 2015, Keramati 2016, Snider 2015.

## Numbers re-checked (confirmed unless noted)

1. ToT Game of 24: IO 7.3, CoT 4.0, CoT-SC 9.0, b=1 45, b=5 74, best-of-100 CoT 49, IO best-of-100 33. Confirmed.
2. ToT cost table: CoT best-of-100 6.7k/2.2k tokens $0.47 49%; ToT 5.5k/1.4k $0.74 74%; IO 1.8k/1.0k $0.13 33%. Confirmed. The PDF text puts "$0.74 74%" on the CoT row, so c03's row-order inference is right.
3. ToT crosswords (Table 3): CORRECTION. Columns are Letter / Word / Game. ToT 78 / 60 / 20; no-prune 65.4 / 41.5 / 5; no-backtrack 54.6 / 20 / 5; CoT 38.7 / 14 / 0. Line b17 labels 78, 65.4, 54.6 and 38.7 as "word-level"; they are letter-level. Lines a23 and c04 are right (word 60 / 41.5 / 20). Also: the no-prune run found a correct solution in 4/20 games but output only 1 through its heuristic; 3 of the 4 were games pruned ToT could not solve. Lines a23, b17, c04 omit "only 1 output".
4. ToT: about 60% of CoT samples fail after the first step. Confirmed.
5. Koh: VWA 18.9 to 26.4 (+39.7%), WebArena 15.0 to 19.2 (+28.0%), 200-task subset c=0 24.5, c=5 32.0 (+30.6%), c=20 37.0 (+51%), value function ground truth 43.5, no self-consistency 28.5. Confirmed.
6. BAVT: 0.338 EM at 5 calls vs 0.334 baseline at 20 calls; baseline at 5 calls 0.194; instruct model flat 0.289 to 0.293. Confirmed.
7. UAA: Llama3.1-8B GSM8K MCTS tokens 8.22k to 5.43k, time 114.75 to 74.58 s; StrategyQA Qwen3-32B beam 64.33 to 72.00% with 2.02k to 1.64k tokens. Confirmed. Accuracy on GSM8K MCTS is 90.14 to 90.45 (not lower).
8. Lally 2017: 41% mean gap (78 vs 37), t(36)=12.51, d=2.06; SGC t(36)=3.87, pSVC=0.004; state anxiety t(37)=2.12 p=0.042. Confirmed. Lally says detailed alternate-strategy analyses are "described previously (Huys 2015a)", which supports the shared-sample note (a29).
9. Faulkner 2022: specific pruning 0.630 healthy vs 0.617 depressed, t(59)=0.32, p=0.75, BF10=0.272; money won BF10=0.274. Confirmed. Faulkner says the BDI link was "not replicated by our subsequent studies (Huys 2015b)".
10. Huys 2012: look-ahead predicts 77% of choices, final model 91%, goal-directed beats SARSA by 314, specific>general 14/15, 12/16, 14/15. Confirmed.
11. Keramati 2016: 2 s vs 700 ms, n=15 per group, P=0.011/0.027 planning, P=0.034 plan-until-habit after reward; habit weights 0.37 vs 0.59. Confirmed. Added detail missing from a09/b04: the plan-until-habit group difference is NOT significant after unrewarded trials (P=0.9).
12. Huys 2015: 3x8=24 vs 10, 9.7 ms delay t(36)=2.17 P=0.037, memoization +43 +- 22 log-likelihood, Spearman 0.44, 35/37. Confirmed.
13. Snider 2015: CORRECTION to a14. The p-values 1.9e-10 and 1.0e-7 are for depth d and replan rate r as predictors of score advantage (chi2 40.6 and 28.3), not for differences in depth between conditions. The "work budget" conclusion (brute-force exploration to a resource-limited depth) is confirmed in the abstract. N=6 including two authors.

## Contradictions between sources

- LATS comparison numbers differ across lines: HotpotQA ToT 0.55 / RAP 0.60 (a26), 0.39 / 0.54 (c08), 0.49 / 0.54 at k=50 (c09), 0.34 (a27). These are different table settings (reasoning-only, acting, k). Not resolved; do not quote a single LATS-vs-ToT gap without naming the table.
- RAP: c06 gives "average 64%" over 2/4/6-step, while a25 lists 1.00 / 0.88 / 0.42 for RAP(20) (average 0.77) or 1.00 / 0.86 / 0.26 for RAP(10) (0.71). The 64% is not reproduced by the listed numbers; not re-opened. Treat as unverified.
- SSDP speedup: b19 says 2.26x vs DPTS (and 5-8x vs others); c18 says "up to 2.3x". Consistent in substance. 85-90% fewer nodes is the authors' claim; node counts for Qwen2.5-1.5B (11.5 vs 53.3) give about 78%, not 85-90%.
- Pruning as separate Pavlovian process (Huys, Lally) versus pruning as a by-product of value-of-information (Sezener 2019, a13). The second is simulation only and untested on new human data; the two accounts are not tested against each other.
- a29 says no independent replication exists. Faulkner 2022 (31 healthy controls, plus 30 depressed) and the 2025 methamphetamine study (49 controls) replicate pruning in new samples, though on the same task and with the same lab family. Lally 2017 and Huys 2015 share the sample. So: replicated across samples, not across labs or tasks.

## Weak spots

- All human pruning evidence uses one 6-state maze task. No test of another reward structure, another domain, or text.
- Human depth/time studies are tiny: Keramati N=30 (15 per group), Snider N=6 with two authors.
- Value-of-information and prioritised-replay accounts (a11, a12, a13, a18) have no new human fit. They are the best recipe for S6, but evidence is simulation.
- Almost all LLM results are 2023-2026 GPT-4, GPT-3.5, 1.5B-32B open models, mostly math or puzzles. Matching is by nodes or calls, rarely by tokens. Several 2026 items (BAVT, UAA, SCULPT, TabTracer) are single preprints.
- ToT 5.5k tokens vs 6.7k for CoT-100 is token-matched in the appendix, but main Table comparisons are by samples.
- Trained-model results (Searchformer, Stream of Search) do not transfer to a scaffold.

## Only seen in snippets, or not opened

- van Opheusden 2023 (a20), Callaway 2022 (a21, b26), de Groot / Newell and Simon (a19), Snell 2024 (c25): not opened (opened:false). Claim K21 is a placeholder for these.
- Not re-opened by me: Hao 2023 RAP, Zhou 2024 LATS, Valmeekam 2023/2024, Katz 2024, Wu 2025, Fang 2026, Luo 2026, Long 2023, Gandhi 2024, Lehnert 2024, Kim 2025, Sezener 2019, Mattar and Daw 2018, the 2025 methamphetamine paper. Their numbers rest on the first-pass agents, who marked them opened.
- PDF table extraction was garbled in several sources (noted in the limits fields).

## GAPS

1. Does resource-rational planning (Callaway et al. 2022) and expert-depth work (van Opheusden et al. 2023) give a concrete rule for choosing depth and pruning that beats a fixed beam? Read both with numbers.
2. At equal total tokens (not equal nodes), how much of tree-search gain survives against best-of-k with a verifier? ToT b=1 gave 45% alone, so checking states may be most of the gain; need a matched-token ablation of breadth vs checking.
3. Do modern LLMs show loss-driven (affective) pruning on a text version of the Huys maze, and does a "evaluate the best continuation before cutting" rule remove it? Search for 2024-2026 papers on this and on LLM-human planning-depth comparisons.
4. How often does a model-judged prune remove the true path, as a function of task type and judge size, and does a revisit list recover it (ToT crosswords: 3 of 4 missed solutions, only 1 output)? Need rates beyond N=20 games.
5. Is value-of-information expansion (Sezener 2019) usable with an LLM proxy such as sibling dispersion (UAA) or relative-progress critics (BAVT), and does it beat fixed width at equal tokens on non-math tasks?
6. Where is the depth at which LLM search collapses (RAP 6-step 0.26-0.42; o1 20-40 step 23.6%), and does decomposition into sub-plans with cached results (Huys 2015) push that limit at equal tokens?
7. Does pruning of near-duplicate siblings (SSDP, UAA) hold up for large closed models and non-math tasks, where branches differ in wording but not in meaning?
8. Is there any independent-lab, different-task replication of aversive pruning (not Huys-lab, not the 6-state maze), and any failed replication?
9. What is the leaf value to give a cut branch in text planning (cached estimate, one-line guess, prior from memory), and does it beat zero at equal tokens (Keramati 2016 predicts yes)?
10. Do gains from tree search vs a single chain peak at medium difficulty outside web agents (Koh: easy +24%, medium +75%, hard +47%), so that a difficulty gate can decide when S6 opens?

## Gap search results

Evidence in evidence_d.jsonl (d01-d20, 19 opened, d20 is a search log). Claims K22-K29 added; K01, K08, K09, K11, K13, K15, K19, K20, K21 updated. WebSearch budget was exhausted; OpenAlex and Semantic Scholar were rate-limited. Sources came from arXiv, Europe PMC and OSF. Downloaded PDFs were deleted.

1. Resource-rational planning and expert depth: CLOSED (preprint versions read). Callaway gives a concrete rule (best-first with a relative-gap stop; strategy flips with where variance sits). van Opheusden gives depth slopes (0.255+-0.061 per session, N=30; 1000 mobile users) and a fixed-beam variant fitted as a rival. Neither is tested against a fixed beam in an LLM. Journal versions not opened. (d01-d04, K21, K25)
2. Equal-token breadth versus checking: PARTLY CLOSED. Evidence says the checker is a large share (Brown, Stechly), rollouts lose per FLOP (Wu, Snell), and a learned-value tree beats CoT-SC with the same reward model by 18.7 points on Game of 24 at equal tokens but not by much on GSM8K (Feng). A clean beam-1 versus beam-3 with-checker ablation is still absent. (d07-d09, d12, d19, K23, K29)
3. LLM loss-driven pruning on a text Huys maze: OPEN. No study found. Closest is Chen 2026, which compares LLM and human depth on four-in-a-row (1.78 vs 4-6 plies). (d05, d06, d20, K19)
4. Prune-removes-true-path rates: PARTLY CLOSED. Per-state judge false-negative rates exist (20.7%, 15.5%, 97.1%; ProcessBench F1 falls to 22.9 on hard sets) but no per-path loss rate by task and judge size. CoT2-Meta reports a false-prune audit only as a figure. Needs our own measurement. (d10-d12, K09, K24)
5. VOI expansion with an LLM proxy: OPEN. Progress-based scores (Setlur: 5x compute efficiency) support the BAVT-style proxy, but no non-math, equal-token test of a sibling-dispersion or progress rule. (d14, K28)
6. Depth where LLM search collapses and sub-plan caching: PARTLY CLOSED, CONTESTED. Apple's collapse is disputed by Lawsen (token limits, unsolvable instances, format). No test of cached sub-plans. (d15, d16, K26)
7. Near-duplicate pruning on closed models and non-math: OPEN. SSDP re-read: four small open models, math only; authors say over-pruning is unquantified. Correction: 85% is generated nodes on MATH500; explored nodes fall about 78%. (d13, K11)
8. Independent-lab, different-task replication of aversive pruning: OPEN, with a new rival account. Only same-task replications (Faulkner, Lavalley d=0.81, Huys co-author). Zorowitz/Daw shows by simulation that pessimism about later choices mimics pruning; not tested on human data. No failed replication of pruning itself found (the failed ones remain the depression link). (d17, d18, K27)
9. Leaf value for a cut branch: OPEN. No LLM test of zero versus a guess or cached value. Indirect support only (learned over prompted values, progress scores). (d09, d14, d20, K28)
10. Difficulty gate beyond web agents: CLOSED for maths. Snell and Wu show the medium-difficulty peak and the easy-item reversal. Not tested on text planning or code. (d07, d08, K13)

Corrections to earlier lines: a Chen 2026 comparison now exists, so claim K19's "no human versus LLM depth comparison" is replaced. Table text for Feng, Stechly, ProcessBench and CoT2-Meta was garbled in extraction; values were matched by row order and should be rechecked in the PDF before they are quoted outside this folder.
