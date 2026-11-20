# Critique: E07.08 Design-space exploration (cross-check)

## Numbers re-opened this session (PDF text read)
All confirmed against the source text unless marked.
1. OPRO TSP table (a12, b01, b02, c11): n=10 gaps 0.0 for all LLMs; n=15 text-bison 4.4, gpt-3.5 1.2, gpt-4 0.2 (FI 1.2); n=20 30.4 / 4.4 / 1.4 (FI 0.2); n=50 219.8 / 133.0 / 11.0 (FI 9.8). Steps to optimum at n=10: 40.4, 46.8, 9.6. Confirmed.
2. LMEA (a13, b05-b07): rue-20 3.94 vs OPRO 26.30; rue-25 18.72 vs 53.59; self-adaptation 3.94 vs 11.82. Confirmed. Classic heuristics at rue-25 are 10.71 (NN), 2.33 (FI), 1.41, 2.41. So c12's "best heuristic 1.41%" and b05's "FI 2.33%" are both right; they name different heuristics.
3. MOEA/D-LLM vs GA hypervolume on RE21-RE25 (c01, a14): table row values confirmed (0.781/0.7936, 0.7221/0.6853, 1.1491/1.1561, 1.1574/1.153, 1.0812 both). The two rows are unlabelled in the extracted text; the reading "first row GA, second row LLM" is the natural one but is an inference.
4. MOEA/D-LO win/loss ambiguity (a15, b08, c02): RESOLVED. In the paper's table the +/-/= symbols compare each baseline against MOEA/D-LO. "-" means the baseline is worse than LO. So NSGA-II is worse than LO on 11 and better on 2; MOEA/D worse on 9, better on 3; MOEA/D-DE better on 7, worse on 5. b08's reading is correct; a15's "other method against LO" is also correct; c02's "ambiguous" can be dropped. The IGD table has a different count (2/12/0, 4/10/0, 6/4/4), which no evidence line recorded.
5. iDSE (a18, c05, a19, c06): 16.6x over NSGA-II, 12.7x ACO, 9.9x MOEA/D, 15.3x Lattice, 5.1x HGBO-DSE; NSGA-II 108 designs; 89.9% invalid designs removed, +20.5%, +45.0%; baseline 12.4% invalid. Confirmed. Correction: the abstract calls the 5.1-16.6x range "heuristic-based", but 5.1x is against HGBO-DSE, a learning-based method.
6. Lumina (b18, c04): 6 designs better than A100 in 20 steps, 4.7M space, 32.9% higher PHV, 17.5x efficiency, 421 superior designs vs ACO 24 in 1,000 samples, ACO PHV ratio 1.82x. Confirmed.
7. Driving multi-agent (a22, c09): 6 Pareto points vs 0 for GA in 15 iterations; GA first Pareto point at iteration 20; 400 s limit. Confirmed.
8. EoH (a17, b13, b14): 0.962 to 0.993 in 20 generations, 2,000 queries vs about 1 million for FunSearch; capacity 500: FunSearch 6.75%, best fit 4.50%, first fit 4.97%, EoH 2.13%. Confirmed.
9. MicroEvo (a23): budget 20 HV 0.5826 vs 0.7936 (+36.22%), budget 45 0.663 vs 0.821 (+23.94%), ADRS 0.1666 vs 0.0716. Confirmed (NSGA-II reported with std 0.0439).
10. NSGA-II paper numbers (a01-a05): NOT re-opened. Both public PDF mirrors tried returned HTML, not the paper. One internal tension remains: a03 says PAES is better on ZDT3 and ZDT6 and also that SPEA converged better than NSGA-II on ZDT6. Treat the 7-of-9 convergence count as unconfirmed until re-read.

## Contradictions and tensions between sources
- LLM wins (a18, a23, b18, c07, c08) versus LLM parity (c01, b09): the wins are on expensive, rule-rich hardware spaces at tiny budgets; parity is on cheap synthetic benchmarks with no domain text. The two are not in conflict, but they mean the effect is conditional on a knowledge-rich prompt.
- c08 reports 2-6x higher wall-clock for LLM variants, while a16 and b21 report speed gains. Cost is measured in different units across papers (queries, wall-clock, designs). No paper compares at equal tokens.
- b12 says strong BO baselines were mostly mis-tuned in the literature; the LLM-DSE papers use default-setting metaheuristics (c20). This could explain part of the 5-16x gaps.

## Weak spots
- Every LLM-DSE win is author-run against author-run baselines, small run counts (3-5), no independent replication found.
- OPRO and LMEA use 5 instances per size; error bars overlap at some sizes.
- Obsolete models: GPT-3.5, text-bison, gpt-4 (2023). No 2025-26 frontier model tested on TSP or MOEA operators.
- No paper tests the schema-relevant case: an LLM selecting among its own text candidates by trade-offs (S7). Everything is numeric design vectors or code.
- Foundational human-side work (Papalambros, Marler-Arora survey, Deb 2001 book) not opened: a25, a26, b25-b27 are bibliographic or from memory.

## Seen only in snippets or not at all
c16 (AutoCircuit), c17 (MDO agent), c18 (EoH abstract only), a25, a26, b25, b26, b27. c19 e-SimFT was read but needs training, out of scope.

## GAPS
1. Does an LLM selecting among its own text candidates by multi-criteria trade-off beat random or single-score selection at equal tokens? No paper tests this.
2. Do the low-budget LLM-DSE gains survive against well-tuned, independently run baselines (b12 suggests baselines are often weak)?
3. How much of the gain comes from the injected domain rules versus the LLM itself (rules-only heuristic baseline, no LLM)?
4. What do 2025-26 frontier and reasoning models do on OPRO/LMEA-style scaling (n=20-50 options)? Is the size cliff still there?
5. At equal tokens, does recombine-then-select (LMEA) still beat propose-from-history (OPRO) once reasoning models are used?
6. Where is the criteria-count limit for LLM trade-off judgment (2 vs 4 vs 8 criteria), and does a code-computed Pareto filter help?
7. Re-read the NSGA-II paper and Deb's 2001 book for the exact convergence and diversity claims and the many-objective limit.
8. Human design-space exploration studies (set-based design, Papalambros-style trade-off practice): what do designers do that beats algorithmic search?
9. Does the diversity loss seen in LLM warm starts (b11) hurt final Pareto spread in any paper?
10. Are there any negative or null results for LLM-DSE (publication bias)?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d21, all opened). Web search budget was exhausted by other agents and the arXiv, Semantic Scholar and OpenAlex APIs returned 429, so candidates were found through the Hugging Face papers search API and then read as PDFs.

1. LLM choosing among its own text candidates by trade-off vs random or single-score at equal tokens: STAYS OPEN. No direct test found. Indirect evidence (d12, d13, d14, d15): one-pass LLM picking is weaker than staged pairwise scoring with code aggregation (DeLLMa 73.3% vs 33.3% for o1-preview), position bias and non-transitivity grow as options get closer, and a 9-judge panel is about 2 independent votes. Design implication: shuffle order, aggregate in code.
2. Do low-budget gains survive tuned independent baselines: PARTLY CLOSED, answer is mostly no for standalone LLMs. d01 (independent AutoML group, frontier Opus 4.6 and Gemini 3.1 Pro): TPE 0.9768, CMA-ES 0.9785 beat the best pure LLM agent 0.9814; hybrid best. d04 shows the earlier gain was against random search at 10 evaluations. d05 shows a plain (1+1) loop is competitive. Hardware DSE wins (iDSE, Lumina, MicroEvo) still have no independent replication. K07 stays contested.
3. Domain rules vs LLM: PARTLY CLOSED. d20: all iDSE baselines shared the same rule pruning, so pruning is not the lead; d19: rules raise LLM trade-off accuracy by 0.12 to 0.23 absolute; d06: priors (exemplar algorithms) drive LLM output. The rules-only no-LLM control is still not run by anyone. Stays open for that control.
4. 2025-26 reasoning models on size scaling: CLOSED qualitatively. d09: cliff persists for DeepSeek V3.2 and GPT-5.1 (text-only), models shift to nearest-neighbour and cheapest-insertion; d07, d08, d17: reasoning models help but stay below classical solvers or expert code (CO-Bench 0.65 vs 0.797; HeuriGym QYI about 0.6; EngDesign best 34.4%). No OPRO-style n=20-50 TSP table for a 2025-26 model exists in what we found.
5. Recombine-then-select vs propose-from-history with reasoning models at equal tokens: STAYS OPEN. Only indirect: d07 shows simple BestOfN matches some complex agents, d05 shows a plain elitist loop is competitive.
6. Criteria-count limit and code Pareto filter: STAYS OPEN. No study varied 2 vs 4 vs 8 criteria. Weak signals: d19 unaided parameter-tuning accuracy 0.26-0.40, d12 gain grows with option count, d16 uses code-computed utility and CVaR filters with no ablation.
7. NSGA-II re-read: CLOSED for the 2002 paper (d18). Convergence better except ZDT3 and ZDT6 (PAES), diversity best on all nine, and the paper is itself inconsistent about SPEA on ZDT6. Resolves the earlier tension. Deb 2001 book and the many-objective limit still not opened.
8. Human designer studies of design-space exploration: STAYS OPEN. Publisher pages (ACM, ScienceDirect) returned 403 and no open-access human study was found; only the machine-side set-based template d16 was read. Do not cite human results from memory.
9. Diversity loss and final Pareto spread: STAYS OPEN. d21 measures lower warm-start diversity; d20 shows one benchmark (autocorr) where warm start is much worse; d03 finds diversity did not predict quality in HPO. No paper links the two for a Pareto front.
10. Negative or null results: CLOSED (they exist). d10, d05, d01, d11 and CO-Bench (d07, simple BestOfN beats some agents) report no LLM advantage or a loss; Gideoni et al. 2025 (random baselines competitive with code evolution) is cited in d06 but was not opened. Publication bias toward wins is still likely in the hardware DSE papers.

### Corrections to earlier lines
- K10 said NSGA-II warm start was 2.5x over random start. Table 3 of iDSE gives 3.17x (geo mean) over random and about 2.3x over LHS. Claim text fixed.
- b12/K16 now has independent support (d01, d05).
- OPRO-era size trend now replicated independently (d10).

### Still open after this pass
Gaps 1, 5, 6, 8, 9 and the rules-only control inside gap 3. Cheapest next experiment for gaps 1, 5 and 6: our own S7 test with a code scorer, equal tokens, shuffled order, 3 vs 6 vs 10 options and 2 vs 4 vs 8 criteria.
