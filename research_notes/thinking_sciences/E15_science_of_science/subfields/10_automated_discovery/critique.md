# Critique: E15.10 Automated discovery (machine scientists, LLM hypothesis search)

## Corrections made (10 headline numbers re-opened in arXiv full text, 2026-11-19)
Confirmed unchanged: Si 2024 novelty 4.84 / 5.64 / 5.81 with N=49 ideas per condition, 79 reviewers (a06, b01, c04); Si 2025 post-execution drops -1.049 / -1.760 / -1.879 for AI, 43 executors, ~103 h (a08, b04, c06); LLM-SRBench 31.5% and 28.1% (a05, b11, c11); AI Feynman 100 vs 71 and bonus 15% to 90% (a01, c19); AlphaEvolve 75% / 20%, kissing number 593 (a16, b16, c12); Beel 42%, +8% code, 5 of 34 citations (a11, b05, c02); Kosmos 79.4 / 85.5 / 82.1 / 57.9 and 4.1 vs 6.14 months (b18, b19, c17); ScienceAgentBench 32.4 / 34.3 / 42.2 (a17, c09); DiscoveryBench 25% (a18, c08); LLM-SR 2.5K vs 2M+ iterations (a04).
Corrections and clarifications:
1. b09 says "36.0% including score 3". The table in the paper (text extraction is misaligned by one row) gives verified 14.0% (score 5), 10.0% (score 4), 8.0% (score 3), so score 3 added gives 32.0%, not 36.0%. The 24.0% headline (scores 4 and 5) is confirmed by the paper text. Treat 36% as wrong.
2. a01 and c19 say "solves all 100 vs 71". The paper says Eureqa solved 71% of the 100 basic equations, and "15%" on the bonus set is Eureqa's rate, so "state of the art" there means Eureqa, not all prior software.
3. a07 says "about 200 of 4000 non-duplicate" and c05 says "about 5%". These agree (200/4000 = 5%); the paper states 5%.
4. The 53.3% in c05 is the LLM ranker accuracy from Table 11, compared against 56.1% for human reviewers; b03 reports the 56.1% but the "71.9% on 1.2K ICLR 2024" figure was not re-checked.
5. a10 and c01 differ on the human reference (c01 mentions 73% human accuracy; b07 says 66%). Not resolved; do not quote 73%.

## Contradictions between sources
- Pre-execution novelty (Si 2024: AI > human by 0.80) vs post-execution (Si 2025: AI drops about 1 point). Same group; both are consistent if judging ideas is easier to fool than judging results. Not contradictory, but any claim "AI ideas are more novel" needs the execution caveat.
- Reviewer quality: Lu et al. say the automated reviewer matches humans (65% vs 66%); Beel et al. say it rejected 9 of 10 papers including 4 humans accepted. Different samples (n=10 vs ICLR-scale); the small-n test is weak.
- Compute: ScienceAgentBench and MLE-bench say more compute helps a lot; PaperBench says o1 plateaus after 1 hour. Boundary condition is unknown (horizon length, tool use).
- Success claims (AlphaEvolve 20% improved) vs failure claims (25-32% benchmarks) are on different task types: scorer-exact search problems vs open-ended data analysis. The decisive variable looks like "is there a cheap exact scorer".

## Weak spots
- Many "established" statuses rest on benchmark papers from related groups; independence is partial. Several evidence lines are duplicates of one paper (a06, b01, c04), so independent_sources counts papers, not lines.
- Memorisation evidence (K06) is indirect: gap between Feynman and transformed forms; no clean contamination test.
- Ideation studies are NLP-only (Si) and prompting-specific; one 2024 model generation.
- The AI Scientist workshop result (K12) has n=3 and a low bar.
- Co-scientist wet-lab numbers are from the developers; n=5 drugs.
- No source tests a scaffold at equal tokens against plain sampling for discovery; every compute comparison is confounded.

## Only seen in snippets or not opened
Not opened: a15 and c13 (FunSearch, Romera-Paredes 2023; cap set numbers recalled only, do not cite), a19/c21 (Langley et al. 1987), a20 (Schmidt and Lipson 2009), a21/c22 (King 2009 Robot Scientist), a22 (Burger 2020), c20 (PySR paper, downloaded not read). c18 (Jr. AI Scientist) lacks exact scores. Founding-era machine-scientist work (BACON, Robot Scientist) therefore has no verified numbers in this folder.

## GAPS
1. At equal tokens, does any generate-test-select loop for discovery beat best-of-N sampling? No source runs this control (decides G7 for the whole schema).
2. How well does code-run outcome predict later human-judged value, versus LLM-judged novelty? Si 2025 shows the gap but only for NLP prompting ideas.
3. What exactly does FunSearch (Nature 2023) report (cap set 512 vs 496, bin packing), and how many LLM calls did it need? Unverified in this folder.
4. Do the memorisation effects (LLM-SRBench) extend to hypothesis generation, i.e. how often is a "novel" hypothesis a retrieved one (Gupta and Pruthi: 24%)? Need a replication on non-NLP fields.
5. Where does extra inference compute stop helping discovery agents (PaperBench plateau at 1 h vs MLE-bench pass@8 doubling)? Need a compute-vs-horizon curve.
6. Which Kosmos or co-scientist claims fail replication in the lab; what fraction of "synthesis" statements (57.9% accurate) are wrong in ways code could catch?
7. Do classical machine-scientist results (BACON-style, Robot Scientist Adam/Eve) have quantitative success rates that LLM systems can be compared against?
8. Does sharing a memory of earlier results (AgentRxiv, +11.4%) survive in a single-agent setting, and does it risk contamination?
9. How reliable are LLM reviewers as proxy outcome in discovery work (Lu 0.18 correlation vs Beel 9/10 rejects)? A larger independent calibration study is needed.
10. Is the noise-fragility of AI Feynman (SRBench) shared by LLM-SR style methods on noisy real data?

## Gap search results
Evidence in evidence_d.jsonl (d01-d16). New claims K18-K23; K02, K07, K08, K10, K13, K17 extended.

- Gap 1 (equal-token control): STAYS OPEN. Nova (d11) matches idea count (100 per method), the 5-architecture study (d12) has only 30 ratings; neither matches tokens or has a plain-sampling arm. Run this control ourselves.
- Gap 2 (outcome vs judged value): PARTLY CLOSED for NLP. Si 2025 appendix D (d07): AI ideas ideation-vs-execution Pearson overall -0.09, excitement -0.32 (N=43 total). Non-NLP still untested.
- Gap 3 (FunSearch): CLOSED mostly (d01, d02). Cap set 512 in n=8 found in 4 of 140 runs; capacity bound 2.2180 to 2.2202; bin packing table; about 10^6 samples, 150 CPU evaluators. NOT verified: prior record 496 and the no-LLM/StarCoder ablation numbers (supplement not opened). Page read via a summariser.
- Gap 4 (retrieved hypotheses beyond NLP): STAYS OPEN. Searches found no overlap-rate study in biology or chemistry; one 85-case benchmark (ScholarStack) was only seen in a snippet.
- Gap 5 (compute vs horizon): PARTLY CLOSED. PaperBench (d09): o1 plateaus after about 1 h, humans overtake after 24 h (41.4% vs 26.6%, 3 papers). Plateau may be a scaffold artefact; still no compute-vs-horizon curve across tasks.
- Gap 6 (Kosmos or co-scientist replication): STAYS OPEN. Only a developer-adjacent anecdote (d13, n=1); no independent audit of Kosmos found. A snippet mentioning a different system with 4% fabricated key results was not opened; do not cite.
- Gap 7 (classical machine scientists): PARTLY CLOSED. Eve numbers (d15): about 14,400 compounds, over 10,000 per day, TNP-470 IC50 0.16 uM vs over 165 uM human. Adam 12 of 20 confirmed is snippet only (d16, not opened). BACON and Schmidt-Lipson not retrieved. No comparable hit rates against LLM benchmarks.
- Gap 8 (shared memory, single agent): PARTLY CLOSED. AgentRxiv (d05): gain is from a single lab reading its own papers (70.2 to 78.2%), but the best method was selected on the MATH-500 test set; transfer is +3.3%. Contamination risk is real; no no-memory equal-cost control seen.
- Gap 9 (reviewer reliability): MOSTLY CLOSED. ReviewerToo (d03, d04): 1,963 ICLR 2025 papers, ensemble 81.8% vs human 83.9%, single prompt about 70%, persona bias, sycophancy after rebuttal. The Lu 0.18 vs Beel 9/10 conflict is explained by ensemble vs single-prompt and sample size; Lu's own reviewer was not retested.
- Gap 10 (noise fragility): PARTLY CLOSED for AI Feynman (d10): 53% exact at zero noise, beaten above 0.01 noise by four methods. LLM-SR noise behaviour not tested in any source found.

Remaining hard gaps: 1, 4, 6, and the LLM-SR half of 10.
