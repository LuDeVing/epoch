# E02.09 Cross-check critique

## Re-opened sources (full text, this session)
Mandel and Barnes 2014 (PMC), Halawi 2024, Schoenegger 2024, ForecastBench, Turtel 2025, Lu 2025, Hsieh 2024.

Confirmed unchanged: Mandel and Barnes (A 0.940 SE 0.007; Brier 0.074; VI 0.240; DI 0.182; eta2 0.758; CCI -0.076; seniority 0.951 vs 0.909; a=2.2). ForecastBench (0.096 / 0.121 / 0.122; gap 0.054 vs 0.026; Arena 1406). Schoenegger (0.20 SD 0.12; t(30) -2.35; mean 57.35; GPT-4 0.17 to 0.14; Claude 2 0.22 to 0.15). Hsieh (crowd 0.172 and 73.8%; RTF median 0.169 and 72.4%; mean 0.170 and 73.9%). Turtel (0.190 [0.178, 0.203], ECE 0.062; o1 0.202, ECE 0.093; market gap +0.039). Halawi headline numbers and the .199 vs .246 crowd-uncertain result.

## Corrections
1. Lu (2025), b22/c27: the expert "0.0225" is a MEDIAN Brier. The expert MEAN is 0.1573 (N=157, SE 0.0189), worse than o3 0.1352 (different question subsets). The paper says experts "significantly outperform" bots by comparing a median to a mean. Weak (claim K11).
2. Halawi ablation, b18 vs c04: ".206" is the system with NO fine-tuning AND NO retrieval (base GPT-4-1106), not "no retrieval" alone. Removing only one component costs 0.002-0.007 (.181-.186). b18 wording is wrong. The pdftotext table rows are shifted, so exact row labels stay uncertain.
3. Halawi crowd-uncertain: .246 (a13/b18) is the validation-set crowd Brier; c02's ".24 vs .237" is the unweighted-average condition. Different conditions, not a conflict. The ablation table uses crowd .146, not the .149 of the main test.
4. Turtel o1: 0.202 (table) is right; c22's ".201" was implied. Use .202.
5. a09 (GJP "35% to 72%", "30% better than classified") is secondary; do not cite as measured.
6. a14 "RMS calibration error .42 vs .38" is as printed and looks odd (system worse); keep flagged.

## Contradictions
- Mandel and Barnes Brier 0.074 vs LLM Briers 0.12-0.20 are not comparable: different horizons, question selection, base rates (a26, Paleka).
- Coherence: poker experts show a link to accuracy (b16), military analysts do not (b11). LLM consistency correlates with Brier (R up to 0.92) but optimisation did not generalise (c16).
- Ensembles help agentic ReAct (SD 0.092) but hurt base GPT-4o (0.218 vs 0.210).
- Schoenegger "equivalence" with the human crowd was not preregistered; Schoenegger-Park 2023 (N=23) shows a large human lead (0.07 vs 0.20) on a different question set.

## Weak spots
- Mandel and Barnes: one unit, 15 analysts, outcomes coded after the fact, recalibration fitted in-sample, no human-vs-human comparison on identical questions.
- Several LLM pairwise gaps are non-significant (Hambly).
- 2025 frontier numbers date fast; leaderboards not read (c14).
- Not opened (second-hand only): Tetlock 2005, Baron 2014, Mellers 2015, Grove 2000 (a27, a28, b13, b28, b29, b30).
- Snippet-level: a09.

## GAPS
1. Does a reasoning-scaffold agent beat a plain prompt on forecasting at equal tokens (Pratt and Lu say added strategies hurt)? Which parts, if any, help?
2. How do 2025-26 frontier models and retrieval agents score on ForecastBench or live questions vs superforecasters? Is parity reached?
3. Do post-hoc recalibration and extremizing (Mandel-Barnes a=2.2, Satopaa) work for LLM forecasts, and what parameter?
4. What is the best aggregation of N samples from one LLM (median, logit-mean, extremized) vs mixed-model crowds at equal tokens?
5. Is LLM acquiescence bias (mean 57%) removed by negation pairs or base-rate priming, and does it persist in reasoning models?
6. Do verbal-probability (Kent scale) forecasts match numeric accuracy, and how should the agent map words to numbers?
7. Has Mandel and Barnes been replicated in other agencies or countries?
8. How much of the LLM-vs-crowd gap is date leakage or question selection (Paleka)? Which benchmarks are clean?
9. Does showing the agent a crowd prior help or cause over-deference when the prior is wrong?
10. Do consistency checks work as a label-free accuracy proxy on held-out checks?

## Gap search results (evidence_d.jsonl d01-d23; claims K22-K31 added)

Tools: WebSearch quota was used up, arXiv and Semantic Scholar APIs returned 429, OpenAlex asked for an email (not sent). Sources were found by known arXiv ids, Crossref, and the FRI and ForecastBench sites. Wiley and Metaculus index pages were blocked, so two Mandel papers were read as abstracts only.

Status: closed = answered with measured numbers; partly = some evidence, key test missing; open = no evidence found.

1. Scaffold vs plain prompt (PARTLY CLOSED, d01 d02 d08). Strategy prompts move Brier about 0.01 at best. Helped: base rate first, frequency format, step-back. Hurt: explicit Bayesian update (+0.03), propose-then-select. Stacking gave nothing. The parts that help are outside the prompt: agentic search (0.1140 vs 0.1230 none), sampling and pooling, calibration stretch. Still open: no equal-token comparison anywhere.
2. 2025-26 frontier vs superforecasters (PARTLY CLOSED, d03 d04 d07 d12 d13). Early-2025 bots lost to Pros (-17.7, CI -28.3 to -7.0). By July 2026 FRI says scaffolded systems are statistically indistinguishable from superforecasters (p 0.14-0.41), but with human data from July 2024 and wide CIs. Exact Brier values for 2026 not readable. Parity is "not rejected", not shown.
3. Recalibration and extremizing (PARTLY CLOSED, d10 d18 d19 d22). Fixed log-odds stretch with Platt coefficient about 1.73 improved FB-7-21 Brier 0.1140 to 0.1076-0.1085; optimum 2.27 (AIA) and 1.72 (superforecasters); a coefficient fitted on another benchmark kept part of the gain. Baron 2014 and Satopaa 2014 parameters still not read. Gain probably shrinks for newer, better-calibrated models (Prophet Arena ECE about 0.04).
4. Aggregating N samples (PARTLY CLOSED, d05 d09). Mean, trimmed mean, median equal within 0.0004 at 10 samples; geometric mean of log odds equal or slightly better in the mixed-model ensemble (0.194 vs 0.197). LLM-reads-all-samples was worse. Open: single-model sampling vs mixed-model crowd at equal tokens.
5. Acquiescence (STILL OPEN, d02). No negation-pair or priming test found. Evidence now says the 57% mean is not general: reasoning models had means of 41.5-44.8%, Pratt saw low-probability guessing, AIA sees hedging toward 0.5. K13 downgraded to contested.
6. Verbal vs numeric (PARTLY CLOSED, d15 d16 d17). Numbers communicate better than words (N=1,202). LLMs map words to numbers human-like on average but shift 7 points with prior belief. No study scores LLM word forecasts against outcomes. Recommendation: output numbers.
7. Replication of Mandel and Barnes (OPEN, d14 d15 d22). Only an internal extension (3,622 forecasts, 2,013 codable) and UK or other-analyst studies on different questions. No independent agency replication found.
8. Leakage and clean benchmarks (CLOSED enough to act, d11 d03 d04 d12). Leak rate about 1.65% of search results, effect on Brier under 0.001 in that audit, but one model's apparent win was leakage-driven. Clean: live forward-resolving sets (ForecastBench, Metaculus, Prophet Arena); caveats are small samples, sports-heavy mix, and vendor audits.
9. Crowd prior (PARTLY CLOSED, d08 d05). A market price lifts Brier by about 11% but substitutes for search; an earlier LLM scored worse than the price it saw. Over-deference to a wrong prior untested.
10. Consistency as label-free proxy (STILL OPEN for LLMs, d20 d21). For humans, LLM-scored rationale rubric r=.19 per forecast, .51 per forecaster; quick calibration questions r=.27. No new evidence that LLM consistency checks generalise to held-out checks (K07 stays contested).

Changes to claims: K10 and K13 set to contested; K05, K07, K12, K14, K18, K19 got new evidence ids; K22-K31 added.

Remaining weak spots: all AIA numbers come from one vendor report with garbled tables (row labels of the o3 line and the learned-parameter rows are uncertain); the Metaculus result was read through a page summary; FRI parity post gives no Brier values; Tetlock 2005, Mellers 2015, Grove 2000, Satopaa 2014 and Baron 2014 numbers still unopened.
