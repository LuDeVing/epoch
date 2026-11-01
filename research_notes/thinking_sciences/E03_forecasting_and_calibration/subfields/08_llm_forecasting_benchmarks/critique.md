# Critique: E03.08 LLM forecasting benchmarks (cross-check)

## Corrections made
- Re-opened Karger et al. PDF (arXiv 2409.19839): confirmed 0.096 / 0.121 / 0.122 / 0.136, combos 0.076 / 0.096 / 0.130, Arena 1406 (CI 1346-1633), compute 6.49e26 (CI 9.69e25-8.65e28), 7-day 0.093 vs 0.076, Econ & Business 0.126 vs 0.141, 90-day LLM better. All OK.
- Re-opened Halawi et al.: 0.179 / 0.149 / 0.208 / 71.5% / 77.0% / 5,516 / 914 confirmed. The crowd is 0.149 in the main text but 0.146 in the ablation table; 0.146 is also the system+crowd figure, so a09 and the ablation crowd value are easy to mix up.
- Re-opened Lu (2025): 0.1352, 0.1307, median 0.0225, mean 0.1573, "before May 2027" confirmed.
- Re-opened AIA report: 0.1076, 0.1110, 0.0753, 0.0740, 0.1258, 0.1106 confirmed.
- MAJOR: a08, a26, b28, c30 could not verify the "0.017 gap, parity about Nov 2026" claim. Found the FRI post of 2026-07-16 (evidence_x.jsonl x01): several systems are already statistically indistinguishable from superforecasters (Cassi AI one-sided p=0.41, xAI 0.15-0.16, Google DeepMind 0.14); dataset parity since May 2026; first model above supers on market questions. The 0.017 figure matches the 7-day gap in Karger Table 26. The brief row is out of date or mixed up (claim K25, refuted).
- Karger Table 26 rows are garbled in text extraction; the 0.093 vs 0.076 pair is the first row only.

## Contradictions
- Karger: news did not help. AIA and Halawi: retrieval helps a lot. Likely cause: a simple news summarizer vs iterative agentic search.
- Halawi: system beats crowd when the crowd is uncertain (.199 vs .246), but with all favorable conditions .240 vs .247, so the edge is small and subset-sensitive.
- Human-crowd Brier varies by question set (0.121, 0.149, 0.172), so cross-paper LLM comparisons are not like for like.
- Superforecaster-written prompts did not help LLMs.

## Weak spots
- Superforecaster data are from 2024 (39 people, 9 days); all 2026 parity claims extrapolate from them.
- Many headline results are single-source (AIA, Turtel, FutureSearch, Prophet Arena, OpenForecaster).
- Small samples: Schoenegger 31 and 23 questions.
- Early resolution and leakage (3.8%+, 10%+) affect several sets.
- Parity projections (R2 0.41-0.47) were weak and are now overtaken by events.

## Only seen in snippets or not fully opened
- Pratt et al. details, FutureX per-model scores, OpenForecaster numbers, Prophet Arena figures, leaderboard table rows (JS-rendered), methods of Cassi, xAI, DeepMind.

## GAPS
1. What exactly do the parity-reaching systems (Cassi, xAI, Google DeepMind, Torchcast) do, and how many tokens per question? Needed for an equal-token comparison.
2. Which pipeline components (sub-question generation, relevance filter, multi-model ensemble, supervisor, Platt scaling) give the gain at fixed compute?
3. Does parity hold on market (judgment) questions after a fresh superforecaster round (fall 2026)? Parity or outperformance?
4. How much of the market-question edge comes from the crowd or market price input versus own reasoning?
5. Does leakage (post-cutoff search results, early resolution) inflate 2025-26 results; can a pastcasting set with frozen retrieval reproduce them?
6. Which prompting elements (base rate first, frequency framing) survive on 2026 frontier models with agentic search?
7. Can consistency (arbitrage) checks serve as an inner-loop signal to choose among samples, and do they predict Brier on new questions?
8. Does Platt or extremising scaling (sqrt(3)) transfer across models and question mixes?
9. Does model diversity beat more samples of the best model at equal tokens?
10. Does LLM accuracy decay with horizon relative to markets in the newest models?

## Gap search results (evidence_d.jsonl d01-d24; claims K26-K37)

Search tools: WebSearch quota was exhausted and the arXiv, Semantic Scholar and OpenAlex APIs returned 429, so sources were found through the reference lists of opened papers and opened directly (arXiv PDFs, FRI wiki and posts, vendor pages).

Correction to K25: the brief's numbers are real. 0.017 is 0.103 minus 0.086 in the FRI Brier Index post; "November 2026" is the linear parity date in the FRI post of 2025-10-08 (gap then 0.020, CI Dec 2025 to Jan 2028). The Brier Index post later moved parity to March 2027. Both were overtaken by the July 2026 parity statement. K25 is rewritten, not refuted.

Closed or mostly closed
- Gap 7 (consistency as inner-loop signal): mostly answered no for optimising. Patching to pass checks did not generalise to held-out checks or Brier; correlation changes sign between datasets (negation -0.36 on NewsAPI). No study tests it as a sample selector. Use as audit only (K21 contested, K32).
- Gap 4 (market-question edge from price): mostly answered. Price-only scores BI 81.5; the best agent adds +2.3, not significant on 200 events; GPT-4.5 correlated 0.994 with the market (K29).
- Gap 2 (components at fixed compute): partly. Component gains are listed, but none at matched tokens (K28).
- Gap 8 (Platt transfer): partly. Out-of-set fit keeps about 60% of the gain; gain shrinks with a price anchor (K33).

Partly open
- Gap 1: pipeline shape for Cassi and Torchcast known; tokens unknown. ForecastBench does not record them. Reference scale from other agents: 80k-250k tokens, 0.14-1.7 USD per question (K26, K27).
- Gap 5 (leakage): live results are not search-leak inflated; backtest leak rates measured at 1.5-1.65% of results; frozen-corpus fidelity to live is checked on only 20 questions (K30, K31).
- Gap 6 (prompting on 2026 models): one data point, mixed (K36). Base-rate-first and frequency framing untested on 2026 agents.
- Gap 9 (diversity at equal tokens): only equal-sample evidence, N=113, in-sample (K34).

Still open
- Gap 3: no fall-2026 superforecaster round found, and none could be confirmed as planned. Today is 2026-11-01. Cassi's own board still ranks the supers first (69.2 vs 68.8).
- Gap 10: no 2026 horizon-vs-market study. Prophet Arena (2025 models) and Karger Table 26 only (K35).

Source limits to remember: FRI and Cassi pages were read through a summarising fetch tool, with tables as images. The Metaculus "Pros Beat Bots" report and the "nine months of progress" report were not found. Derived figures (tokens per question for BLF, 1.64 USD for the four-agent mean) are marked as this reader's arithmetic.
