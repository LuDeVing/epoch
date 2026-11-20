# Critique: C05.10 Constraint satisfaction (cross-check)

## Re-opened this session (full PDF text, arXiv)
1. ZebraLogic (2502.01100): confirmed o1-full 81.0, R1 78.7, o1-preview 71.4, o1-mini 59.7, Sonnet 3.5 36.2; GPT-4o 31.7; voting N=32 38.0; RM best-of-32 34.8; oracle 60.3 (N=32) and 69.1 (N=128); hidden tokens 5,144.6 vs 543.7; self-verify 32.1.
2. Stechly et al. 2023 (2310.12397): confirmed 16 percent baseline, 1 of 100 with self-critique, about 40 percent with a sound verifier.
3. Tree of Thoughts (2305.10601): confirmed IO/CoT under 16 percent, ToT 60 percent word level, 4 of 20 games, best-state 7 of 20, no-backtrack 20 percent.
4. Sudoku-Bench (2505.16135): confirmed o3-mini-high 14.0, Gemini 2.5 Pro 11.0, o3-mini 9x9 2.9.
Not re-opened (time and rate limits): Zhang and Yap, LR2Bench, Amonkar, CP-Agent, DCP-Bench, GenCP, SatLM, He and Wang, Hazra. They stay as the earlier agents recorded them.

## Corrections
- c01 mislabels the ZebraLogic rows (R1 81.0, o1-preview 78.7, o1-mini 71.4). Correct: o1-full 81.0, R1 78.7, o1-preview 71.4, o1-mini 59.7 (a19, b01 are right). c01 also drops o1-full. Do not use c01's model-to-number mapping.
- ZebraLogic X-Large bound: a19/a21 say over 10^10; the paper's text says >=10^10 in the size list but its Table 1 header says >10^9 and Large <10^9. The paper is internally inconsistent. Cite as "about 10^9 to 10^10".
- b04 says GPT-4o self-verify about 32-33; paper table gives 32.1 (c02 is right).
- a18 and b25, b26, c24-c27 are unopened; a18's Model RB threshold is from memory and must not be cited. c27 is a snippet only.
- c09 reports Game of 24 numbers (5, 3, 36-38); from the 2024 paper text as read earlier, not re-opened.

## Contradictions and tensions
- Solver help (b10, c10, b12) versus formalizer faithfulness (b07-b09): solvers fix search but move the error to translating constraints. Both hold.
- Code vs CoT: code wins on logic puzzles, loses on GSM8K (b10). Gate by task.
- Task management scaffold (b18) hurt hard problems while CP-Agent overall reached 100 percent (b17): more steps are not monotonic.
- Voting is weak on large puzzles (b03) but oracle best-of-128 beats o1-mini: the picker, not the sampler, is the bottleneck.

## Weak spots
- GenCP evidence (a24, a25, b24, c13, c14) is one team and small counts (3 vs 10 solutions); status single-source.
- Classic CSP numbers (Grant thesis a12-a17) are via a thesis summary, not the original papers. Cheeseman 1991 not opened.
- Nearly all LLM results are 2025-26 preprints; model versions differ and mix reasoning and non-reasoning models, so equal-token comparisons are rare. Token budgets are mostly not matched.
- Dechter's book was never opened (b25, c24).
- No study tests a propagation-first prompt scaffold at equal tokens on a general model.

## GAPS
1. Does an explicit propagation loop (prune domains, then guess) in a prompt beat plain long reasoning at equal tokens on ZebraLogic Large and X-Large?
2. Does a programmatic constraint checker alone (no solver) recover most of the sound-verifier gain (16 to about 40 percent) on non-colouring tasks?
3. How often does an LLM mistranslate constraints (wrong-constraint rate) and does round-trip back-translation catch it?
4. At what constraint density or conflict count do solver tools stop paying for their overhead versus direct reasoning?
5. Does dynamic backtracking (retract one assignment, keep independent work) help an LLM agent, as in Ginsberg 1993 crosswords?
6. Does smallest-domain-first variable choice help an LLM, given classical evidence that fail-first is not reliably explained?
7. Can an agent be trained or prompted to say "unsatisfiable" reliably (SATBench hard UNSAT 65 percent, near random)?
8. Is GenCP-style propagation during decoding replicated by an independent group?
9. Do the Amonkar, LR2Bench and CP-Agent numbers hold when opened and re-checked, especially CP-Agent's task-management ablation (52/60 to 45/60)?
10. Does Dechter's tree-decomposition or width bound give a usable ordering rule for natural-language constraint lists?

## Gap search results (gap searcher, evidence_d.jsonl d01-d21)
Search tools: Semantic Scholar, OpenAlex and the arXiv API were rate limited or out of budget, so papers were opened as arXiv PDFs and found with 6 web searches.

Closed or mostly closed
- Gap 9 CLOSED. CP-Agent (d01, d02): 52/60 to 45/60 on 20 hard problems confirmed (Haiku 4.5, 3 runs); easy tokens +191 percent. Amonkar (d03, d04): 15 of 24 and the 95 percent confirmed, but the 95 percent is from an 80-case audit (5 per cell). LR2Bench (d05): 23.6 (o1-preview) and 20.0 (R1) confirmed; redundancy link is a figure only.
- Gap 7 CLOSED with a correction (d06, d07). SATBench hard UNSAT is near random only for o4-mini (65.0). R1 is 83.6 and V3 74.3; the average over models is 39.3, below chance. Main error: satisfiability bias (68.7 percent of o4-mini errors). An error-aware prompt fixed 60.4 and 73.2 percent of known failures (not a clean accuracy test). K22 reworded.
- Gap 2 MOSTLY CLOSED (d17). Hand-written programmatic critics with back-prompts lifted TravelPlanner GPT-4-Turbo from 4.4 to 20.6 percent. No matched-token comparison, so the size of the checker-only share of the Stechly gain is still unmeasured.
- Gap 3 PARTLY CLOSED (d04, d08, d09, d11). Wrong-constraint rate is high in scheduling (95 percent of semantic errors, small audit), 86 percent of tool-pipeline failures in Zebra, but only about 3 percent for templated SAT clauses. Round-trip equivalence checking predicts drift (28.7 vs 16.2 percent) but only on legal text.

Partly answered
- Gap 4 (d03, d10, d11, d12, d16). Direct reasoning wins on small puzzles; tools win on large; solver pipelines still lose half their accuracy on the most-constrained fifth. No conflict-count threshold has been measured.
- Gap 5 (d14, d15, d19). Chronological backtracking is task-dependent (helps Sudoku, hurts CountDown) in trained models. Dynamic backtracking (Ginsberg) for LLMs: no study.

Stayed open
- Gap 1: no equal-token test of a prompted propagation loop. Indirect: longer natural reasoning hurts on Zebra puzzles (d13); trained propagate-then-one-guess hits 99 percent on Sudoku (d14).
- Gap 6: no in-context test of smallest-domain-first. Only code-generation evidence (d16).
- Gap 8: no replication of GenCP found (d20, weak absence evidence).
- Gap 10: not searched (Dechter width bound on natural-language constraint lists; no LLM study expected). Dechter's book still unopened.

Other notes
- Berman et al. (d10) 166 percent is GPT-4 27 to 72 of 114 at variable temperature; 63 percent is below o1-class direct reasoning.
- Exact-cover solver agent with a 24B model reached 97.9 percent on ZebraLogic vs 91.7 for o3-mini-high plain (d12); authors' own comparison, preprint.
- LogicPuzzleRL (d21) and GenCP (d20) are unopened. Not re-opened this pass: SatLM, He and Wang, Hazra, DCP-Bench, Zhang and Yap.
- New claims K23-K29 added to claims.jsonl; K16, K22, K13, K12, K17 revised (K17 kept single-source).
