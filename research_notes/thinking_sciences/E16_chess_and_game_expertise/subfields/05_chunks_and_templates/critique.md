# Critique: E16.05 Chunking and template theory (cross-check)

## Re-opened this session (text in D:/research_scratch/E16.05, PDFs deleted)
Confirmed with no change: Chase and Simon 1973 chunk counts (77 chunks, 47 pawn chain, 27 same-colour clusters, 17 unclassified); Gobet and Clarkson 2004 (0.64 s vs 2.43 s gaps, 95% vs 42.6%, 70/45/17% recall, Masters' largest chunk 14.8/12.9 on screen vs 7.5/3.8 on board, 67/41/12%); Gobet and Simon 1996 templates (92.3% / 64.5% one board, +71% and 63% gain, 82.9 and 44.9 pieces); Gobet and Simon 1996 distortions (77.3/49.7/34.5 vs 62.9/38.6/27.5, 10.3 gap, F=291.51); Gobet and Simon 2000 (F=7.74, 14.36, 27.63; chunk counts 2.9 / 4.2 / 3.3); Gobet and Waters 2003 slope 0.052 (SE .016); Karvonen 2024 (99.6 vs 74.7, legal moves 99.8/99.6, win rates 46/64%); Ruoss 2024 (2895 blitz, 2299 tournament, 95.4 and 88.9 puzzles, under 1.41% overlap); Buffer of Thoughts table (82.4, 86.4, 93.6, 12% cost); Dynamic Cheatsheet tables; SoK (16.2 points, 1,200 malicious skills); mapping study (84 families, 45.2%).

## Corrections and clarifications
1. Gobet and Waters 2003 slopes (b18): the table has five rows (game 0.35, 1/3 randomized 0.11, 2/3 randomized 0.063, "random" 0.059, 3/3 truly random 0.052). Row names are confusing. The key point: random vs 3/3 vs 2/3 are not significantly different (F=0.11, 0.25), so only "game vs everything else" is cleanly supported.
2. Dynamic Cheatsheet (c19/c20): the 50.0% on Claude AIME 2024 is the DC-Cu variant (DC-RS gave 46.7). GPT-4o's 40.0% is DC-RS. The Game of 24 jump 10% to 99% is stated by the authors to come from discovering and reusing a Python solver, so it measures code reuse, not pattern cueing.
3. Ruoss (c11): 2895 is Lichess blitz vs humans; 2299 is the Elo against engines in the tournament table. Do not mix them as one figure.
4. a06 "over 75 percent": 60 of 77 chunks (78%) fit the three types; "over half" held a pawn chain (47 of 77, 61%).
5. A file named 2406.04692 in the scratch folder is a different paper (Mixture-of-Agents); the Buffer of Thoughts text is 2406.04271. Evidence lines cite BoT correctly.

## Contradictions and weak spots
- Chunk size and count: Chase and Simon (master median 5, about 7 chunks) vs Gobet and Clarkson (about 3 chunks, 14.8 on screen). Resolved partly by the display-medium artifact, but both labs' numbers depend on the 2 s rule.
- Multi-board "capacity": Gobet and Simon's growth in pieces recalled is partly what guessing from a typical master position gives (Cooke baseline 43.7%). Capacity claims are easily overread.
- Random-position skill effects: small, near the edge of significance in many studies; the dispute between templates, constraint attunement and abstract roles (Linhares) is not settled. The Linhares source was seen only as an abstract.
- Search vs recognition: Gobet 1998 shows no search-size effect, but Chabris and Hearst show blunders rise at speed. The data are not decisive.
- Nearly all human data come from Gobet's group (plus Chase, Simon, Saariluoma, Cooke). Independence is limited. Sample sizes are small (3, 5, 12, 13, 20, 25, 36). Many multi-experiment numbers are model fits tuned to the same data.
- Template theory slots (fixed core plus slots) have no direct LLM test. LLM "templates" (BoT, DC, AWM, ExpeL) are retrieved instructions or code, not slot-filled perceptual chunks. The analogy is by function, not mechanism.
- Hardly any LLM paper here tests "pattern cues the right candidate" as the dependent variable. Most report final accuracy, so retrieval gain and reasoning gain are mixed.
- Token cost: BoT reports 12% of multi-query cost; others do not report equal-token comparisons. Equal-token claims are not established by any source seen.

## Only seen in snippets or not opened
a30 Saariluoma 1991, a31 Saariluoma 1994, a32 CHUMP (no numbers), a33 Kasparov simultaneous (via Gobet 2003 footnote), b19/b20 Sala and Gobet 2017 meta-analysis (abstract page), b21 Linhares and Brum, b28 Schut et al., c05 and the Pleiss et al. 2026 figures (c01-c04). The Pleiss paper could not be located again this session (OpenAlex quota exhausted, arXiv title search returned nothing), so K12 stays single-source and unverified by the checker.

## GAPS
1. Does a slot-filled template (fixed core plus variables) beat a flat list of past solutions or a plain snippet in an LLM agent at equal retrieved tokens, on problems with shared structure?
2. In LLM agents, does retrieval cue the correct first candidate (hit rate in the top 3), and how much of the BoT/DC gain comes from that vs from the extra reasoning it triggers?
3. How far does template transfer reach: what is the gain as a function of distance between the source and target task family (ExpeL, EvoSkill, AWM tested only near neighbours)?
4. What admission rule for templates (held-out validation, repeat count, reuse success) avoids the harm of self-generated skills (-1.3 points in SoK, FH 6.7% in DC)?
5. Do extra thinking tokens help less on unfamiliar problems (Pleiss et al.) in a scaffolded agent, and can retrieval restore the gain? Needs the Pleiss paper reopened and a replication.
6. Is the 3-4 retrieved-item cap (template theory) better than 7-8 small items for an LLM at equal tokens?
7. What does the CHUMP-style pattern-to-move link actually achieve (numbers), and has anyone since built a pattern-to-candidate table and measured it?
8. How much expert recall on random or shuffled material is real skill vs publication bias (Sala and Gobet r=.29 after trim-and-fill)? Open the full meta-analysis and the moderator tables.
9. Does the search-vs-recognition split (Gobet 1998 vs Chabris and Hearst 2003) hold when search is cut, and how would the scaffold show it with a search-off arm?
10. Do abstract role-based patterns (Linhares) transfer better than surface-tied ones for LLM memory? Needs the full paper and a surface-change test.

## Gap search results
Evidence is in evidence_d.jsonl (d01-d22, all opened). Claims K01, K10, K11, K12, K15, K16 updated; K20-K26 added. Web search quota was exhausted, so sources came from arXiv PDFs, PMC, Crossref and Gobet's reply paper.

1. Slot-filled template vs flat list or snippet at equal tokens: STAYS OPEN. Nearest evidence: AWM abstracted vs rule-based workflows (WebArena 35.5 vs 35.6; Mind2Web element accuracy 50.6 vs 49.5) and a SkillsBench granularity study (low vs high abstraction +0.7 / -6.7 pp, CIs cross zero; worked example +0.7 / +1.3). None is equal-token or a typed-slot test (K22, contested).
2. Retrieval hit rate in top 3 and split of gain: PARTLY CLOSED. SRA-Bench gives Recall@1 7.0 to 57.2 and Recall@10 36.1 to 80.7, and shows oracle gain +16.6 pp vs about 30% (top-1) to 70% (selection) captured. Skill Following shows aggregate lift can be positive while same-task effect is negative. No paper gives a top-3 hit rate or splits BoT / DC gain; BoT retrieves one template and does not score it (K21).
3. Transfer vs distance: PARTLY CLOSED. ReasoningBank Mind2Web gains +4.6 / +2.2 / +4.7 (task / website / domain), AWM-offline step SR 45.1 / 33.7 / 32.6 vs MindAct 36.2 / 30.1 / 18.6, MSCE cross-domain mean +3.93. Gains small and not clearly falling; distance is only a coarse label; no far-domain test (K16).
4. Admission rule: CLOSED enough to act. Outcome-based checks beat self-judgment: strict held-out gate (RSEA), randomized block curation (66.9 vs 55.5 whole, 53.8 self-judged), strict-verifier addition, and reuse-count-plus-utility deletion. SkillsBench v4 self-generated is -8.1 to -11.5 pp (the SoK -1.3 is the earlier version) (K20, K24, K15).
5. Thinking tokens on unfamiliar problems (Pleiss): PARTLY CLOSED. Paper reopened (arXiv 2601.16823) and numbers confirmed, plus OOD gain per 1,000 tokens 3.81% and token use 3,426 / 11,800 / 16,953. No replication found and no retrieval arm exists, so K12 stays single-source. The per-token metric is partly confounded by OOD using 5x more tokens, and the total relative drop is not monotone (ND 85.3% > WD 77.25% > OOD 64.69%).
6. Cap of 3-4 rich items vs 7-8 small at equal tokens: STAYS OPEN. Indirect support that fewer is better (ReasoningBank 1 item 49.7 vs 4 items 44.4; SkillsBench 2-3 skills +19.0 vs 4+ +10.1) but tokens grow with k in all of them (K23).
7. CHUMP and pattern-to-move tables: STAYS OPEN. No CHUMP numbers found. Only the SEARCH model output (15% heuristics, 23% chunks, 62% templates) in Gobet's reply (K11).
8. Random-material expertise vs publication bias: CLOSED. Meta-analysis opened: r = .41 -> .29 [.17,.41] after trim-and-fill; 49 of 55 experiments favour experts; domain and exposure time not significant moderators (K01, K25).
9. Search vs recognition: PARTLY CLOSED. Added the machine analogue (policy-only Leela 2292 vs 2858 with search; AlphaZero 1777 vs 2470) and Chabris and Hearst numbers via Gobet's reply (5.02 / 6.85 / 7.63 blunders per 1,000). The original Chabris and Hearst PDF was not retrievable. Still contested (K10).
10. Abstract role-based patterns (Linhares and Brum): STAYS OPEN. Abstract only (publisher 403). Indirect LLM support from ReasoningBank vs AWM at the farthest distance, no surface-change test (K26).

Corrections to my own earlier reading: SkillsBench self-generated deltas differ by version (SoK -1.3 vs v4 -8.1 to -11.5); Ruoss 2299 is the bot-pool Elo and 2895 the human-pool Elo (already noted above).
