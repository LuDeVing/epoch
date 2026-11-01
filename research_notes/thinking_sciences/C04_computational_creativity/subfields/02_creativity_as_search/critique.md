# Critique: C04.02 Creativity as search (cross-check)

## Re-opened sources (this session, PDF text)
Tree of Thoughts, MacGyver, Si et al. 2024, Ideation-Execution Gap, Creative Beam Search, EoH, Bhushan et al. 2026, CreativeBench, AlphaEvolve, RAP.

Confirmed exactly: ToT Game of 24 (7.3/4.0/9.0/45/74/49), creative writing (6.19/6.93/7.56, 41/21/38, 6.19 to 7.67, 7.56 to 7.91), GPT-4/3.5 mixing (64/31/19/74); Si novelty 4.84/5.64/5.81, feasibility -0.29 p=0.36, 71.4/63.5/61.1, 4000 to about 200 at 0.8; Gap study N=43, 19 human and 24 AI ideas, -1.049/-1.760/-1.879; CBS 45%, 217 answers, 31 students, 29% vs 35.3%; EoH table (5.32/4.87/3.78/2.24 and 6.75/2.13, FunSearch about 1M queries); Bhushan 0.744, 1.423, 21.25%, 10.85%, 80/92=87.0%, 53.8%, r=0.732; CreativeBench 89.1% validity, 53.8%/48.2%; AlphaEvolve 75%/20%, 593 vs 592, 48 multiplications; RAP 29.4/46.8/48.6/51.6, 94.2/78.8.

## Corrections made
1. ToT cost (c04, c24, a14 context): earlier notes said ToT cost less than best-of-100 CoT. The paper's Table 7 gives IO best-of-100 $0.13 (33%), CoT best-of-100 $0.47 (49%), ToT $0.74 (74%). ToT used fewer completion tokens (5.5k vs 6.7k) but costs MORE per case. Claim K02 states this. The "tree search saves cost" reading is wrong.
2. MacGyver error labels (c18): c18 lists "unneeded steps 16.9%, unfaithful 9.5%". The paper has five types: wrong tool use 42.4, goal not achieved 17.7, unavailable tools 9.5, (4) 10.8, unfaithful to constraints 16.9 (text: 16.9 + 9.5 = 26.4% hallucination-type errors). a24 is closer to right; c18 mislabels. Treat a24 as correct, with the caveat that the table layout is garbled in extraction.
3. CreativeBench (b07 vs paper): the 53.8% and 48.2% are Gemini-2.5-Pro pass rates; the text order after "100 Explore and 200 Combo" makes the mapping to Combo/Explore ambiguous. Treat the pairing as unverified; claim K14 does not depend on it.
4. a17 (FunSearch bin packing 5.30% on OR1) and c16 (3.78%) differ because they are different test sets/metrics (FunSearch paper vs EoH re-run). Not a contradiction, but they must not be compared across papers.

## Contradictions between sources
- a24 vs c18 on error labels (resolved above).
- Whether search helps creativity: ToT, CBS and AlphaEvolve say yes; Bhushan 2026 says search agents lose novelty over time, and greedy search got the best impact. Reconciled by oracle presence (K20), but not tested directly.
- Bhushan's greedy vs MCTS/evolutionary result (b14) uses 3 tasks and one model, read from a figure.

## Weak spots
- The founding paper (Nair et al., 2405.01453) is a position paper with a tiny experiment; its numbers are mostly in figures. No replication found.
- Many "established" claims rest on one lab's design (Princeton ToT) or on LLM-judge scores. Independent count in claims.jsonl is a judgement: papers that cite each other were not counted as fully independent where possible, but overlap exists.
- Bhushan et al. 2026 (arXiv ID 2608.xxxxx) is very recent, single group, LLM-judge measure (r=0.732 vs humans).
- Theory evidence (Boden, Wiggins, Ventura and Brown, Newell-Shaw-Simon, Ritchie) was not re-opened by me; a07, a08, a09, a26 were marked opened:false by the first agents. a26 has an unverified criteria count.
- c25: the 2025-2026 coverage was thin because search quotas ran out. Likely missing: other reasoning-model creativity studies, test-time search on open-ended tasks, any replication of Creative Beam Search or QDAIF.
- c20 (forbid-technique, 16.1% to 2.1%) was copied from C04.01 and not re-opened.
- Not re-opened: Nair et al. figures, Hu et al. Nova, Meyerson LMX, Bellemare-Pepin DAT, Jiang Artificial Hivemind, Lu AI Scientist, OMNI-EPIC.

## GAPS (most decision-relevant first)
1. At equal total dollars and tokens, does tree search beat best-of-N plus a verifier on tasks WITHOUT an exact oracle (open design, planning with soft criteria)? Corrected cost data (ToT costs more per case) makes this the key question.
2. Does a forced exploration quota or a tried-approach ledger stop the novelty decay seen in Bhushan et al. 2026, and does it raise final score, not just novelty? Any replication of that paper?
3. How reliable is the model as its own scorer for creative candidates when a cheap independent check exists? Need measured agreement rates (self-rank, cross-model rank, execution) beyond the 29% vs 35.3% CBS and 61-71% Si results.
4. Is there any empirical test of transformational creativity (changing the space, e.g. new representation or new operator) in LLM agents? Does a reframe step before search (Nair affordance text, MacGyver divergent-convergent) replicate on newer models and bigger samples?
5. What is the best cheap diversity mechanism at fixed tokens: in-context regeneration, ledger of prior answers, cross-model sampling, or high temperature? NoveltyBench numbers need re-checking on current frontier models, including reasoning models.
6. Do reasoning models with long thinking already do internal search (backtracking, branching) so that an external ToT or MCTS scaffold adds nothing? Look for 2025-2026 studies comparing them at equal tokens.
7. What fraction of proxy-scorer exploitation (ELM Radial, AI Scientist hallucination) appears in text-only reasoning scaffolds, and which guardrail (held-out verifier, execution, second model) catches it cheapest?
8. Which search structure suits which task: greedy, beam, MCTS, evolutionary or quality-diversity? Evidence is a single 3-task figure (b14) and scattered comparisons; need a systematic study.
9. Does Algorithm-of-Thoughts-style in-prompt search hold up on newer models and tasks beyond Game of 24 and crosswords, and what is its token cost vs real tree search?
10. Is there any independent replication of Creative Beam Search (31 raters, one 7B model) or QDAIF's human evaluation (small n)?

## Gap search results (evidence_d.jsonl, d01-d23)

Method note: WebSearch quota was exhausted. I used arXiv full-text PDFs (pdftotext) and arXiv listing search. Search was rate-limited again partway, so 2025-2026 coverage is still incomplete. All 23 lines are opened:true (full text read for the numbers cited).

1. Tree search vs best-of-N at equal cost, soft criteria: STAYED OPEN (new claim K22). On checkable tasks the answer is now clear (K02 rewritten, K21): MCTS lost to sampling at every FLOP budget on MATH (d02), repeated sampling beat all tree variants on ARC-AGI at 128 calls (d06), cheap trees gain only 1-3 points with feedback. No matched-compute study with a soft rubric exists in what I could open.
2. Forced exploration quota or ledger: PARTLY CLOSED. No paper tested a quota against Bhushan's drift, and Bhushan's own appendix lists it as untested (d19). Nearest tests: BASIN visit-count ledger raised accuracy at matched budget (d18, K23, one author, unreplicated); Heuresis exploration gates raised diversity but not top score (d04); sibling memory and UCT constant did nothing in MLE-bench (d03). No replication of Bhushan et al. found.
3. Model as its own scorer: PARTLY CLOSED (K06 extended). Self-check gain near zero without knowledge (d14), self-preference tied to self-recognition (d16), verifiers plateau after about 100 samples (d15), single GPT-4o judge 64.7% vs human 82.7% on 50 MacGyver items, multi-agent judge 84.7% (d17). Still no study of self-pick among creative candidates when a cheap independent check exists.
4. Transformational creativity test and Nair replication: PARTLY CLOSED. Universe of Thoughts (d13) is a first coded transformational operator, effect small and backbone dependent (54.2% vs 50% chance). CreativityBench (d12) is a large neighbour of Nair, not a replication; structured CoT gave -0.012 to +0.039. K15 downgraded to contested; K19 unchanged (no direct replication).
5. Cheap diversity mechanism: PARTLY CLOSED (K24). Verbalized Sampling beat multi-turn, list and direct prompts in a 90-annotator study (d08); cross-model sampling weak (d09); temperature costs quality (d08, d12). Still no equal-token head-to-head of ledger vs VS vs persona, and NoveltyBench has no reasoning models in its text (d10).
6. Reasoning models already search internally: PARTLY CLOSED, then OPEN on the key point (K21, K25). Internal search is real, costly and task dependent (d01, d20, d21). No paper adding external ToT/MCTS to a current reasoning model at equal tokens was found.
7. Proxy exploitation rate and cheapest guard: CLOSED enough to act on (K10, K26). 2.5% fabrication rate in Heuresis; auditor agent catches fabrication, held-out evaluation catches benchmark specialisation, hiding the checker helps (d05, d23). Rates in text-only scaffolds remain unmeasured; all data is from code tasks.
8. Structure by task: PARTLY CLOSED (K13 now established, task dependent). Heuresis (3 tasks, 6 strategies, 3,222 runs), Toledo, AB-MCTS and LFS agree there is no dominant structure and effects are small. No rule for choosing yet beyond: greedy when a recipe exists, archives when the landscape is broad.
9. Algorithm of Thoughts on newer models: STAYED OPEN (K27). Only the original numbers re-read: 1 query and about 6.4k tokens vs ToT 109 queries and about 19.4k tokens on Game of 24.
10. Replication of Creative Beam Search or QDAIF human evaluation: STAYED OPEN (K28). None found; limited by search quota.

Cautions for the next reader:
- Several new sources are single preprints from 2026 (Heuresis, BASIN, UoT, Beyond the Hivemind, CreativityBench); treat their numbers as unreplicated.
- d10: the NoveltyBench source line has no verified first author; use the arXiv ID.
- d05: DGM ablation values were only in a figure; the text confirms direction, not size.
- d20: only abstract, intro and section 4 of the paper were read.
- Claims changed: K02 (to established, rewritten), K06, K08, K10, K12, K13 (to established), K14, K15 (to contested), K18, K19, K20. New: K21-K28 (K22 and K28 use status "open").
