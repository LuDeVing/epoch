# Critique: E03.07 Belief updating (cross-check)

## Numbers re-opened this session (arXiv full text, pdftotext)
Confirmed: Schoenegger 2024 Study 1 (LLM crowd Brier .20 SD .12, t-test), Study 2 (GPT-4 .17 to .14 p=.003; Claude 2 .22 to .15 p<.001; average beats update t(92)=2.58 and 3.53); Halawi 2024 (.179 vs .149, 71.5% vs 77.0%, .199 vs .246 when crowd .3-.7, 7% higher accuracy where crowd near 0/1); Wilie 2024 (Llama-3 70B BU 10.99, BM 92.09, BREU 51.54; GPT-4 Turbo BU 19.65, BM 82.69); Qiu 2025 (624 users, 48 human subset, agreement about 80%); Schoenegger 2025 prompts (Bayesian Reasoning and Propose-Evaluate-Select worse); ForecastBench (.096 / .121 / .122, top no-crowd model .136); Paleka (ExpEvidence 0.20, 0.77, -0.11, 0.06).

## Corrections
1. a21 gave ".240 vs .247" for the crowd-uncertain range 0.3-0.7. The paper says .199 vs .246 there; .240 vs .247 is the selective setting (three conditions, 22% of forecasts). b12 and c10 are right; use those.
2. c06 says Bayesian prompt worse "across all models". The paper reports a pooled mixed-effects model (random intercepts for models and questions): coefficient +0.03 Brier, p<.001. Not shown per model in what we read. Also in Study 2, the raw primary analysis differed from the mixed model for base-rate prompts (c07 already notes).
3. b10 quotes "Opus 5 / Sonnet 5" adoption rates; not re-opened. Treat as unverified model names.
4. Qiu 2025 appears as a17, b01, c01 (also 2026 version v3). These are one source, not three. Counted once in claims.
5. ForecastBench has two human comparisons (0.096 vs 0.121 on the 200-question set; 0.076 vs 0.096 on a dataset-question table). Quote the set with the number.
6. a14: Mobius robot interaction cells are from a text extraction; do not quote.

## Not re-opened (taken on trust)
Atanasov et al. 2020 (a01-a07, a25): the INFORMS PDF returned a page, not a paper, here. Its numbers (N=515, b=0.098, adj R2=0.28, step 0.22 vs 0.19, mediation 29%) rest on one opened-true claim by agent A; b25 says another agent could not reach the primary text. Mark these single-source and unconfirmed by me. Also not reopened: Benjamini/Benjamin 2019 meta-analysis numbers (c-hat 0.20/0.38), Mobius 2011, Filbry 2026, Li 2026, Gupta 2025, AIA, Turtel, Wildman, Sharma, Echterhoff.

## Contradictions and weak spots
- Gupta: LLMs update near-Bayesian on coin flips. Qiu: LLMs stall on multi-round preference inference. Likely task clarity and parametric structure explain it; not tested head to head.
- Filbry: reasoning mode plus code nearly fixes posteriors. Qiu: CoT does not fix updating. Different tasks; reasoning models were not in Qiu's set.
- Atanasov (small steps predict skill) vs Halawi (LLM hedges, loses where crowd is sure). Small steps can be skill in humans but hedging in LLMs; step size alone is not a goal.
- Atanasov: confirmation hurts. Fildes: small adjustments hurt. Contested transfer across domains.
- Training effects (Mellers 2014, Atanasov mediation) are cut by the IRT reanalysis (b24, seen mostly via abstract).
- No study tests the scaffold we plan (a distinct S5 revise step with step-size rules) on an LLM at equal tokens. All LLM work tests prompts or fine-tuning.
- Founding conservatism studies (Edwards 1968, Phillips and Edwards 1966) seen only through Benjamin. Tetlock 2005 numbers from memory.
- Benjamin's meta-analysis covers bookbag tasks; weak link to open-world forecasting.

## GAPS
1. Does an explicit S5 step (list new evidence, direction, size, then move) beat plain CoT on Belief-R, multi-round preference and Metaculus-style pastcasting at equal tokens?
2. What step-size distribution does a frontier LLM show per question (mean absolute update, confirmation rate) next to the human 0.20 and 19%? No one has measured it.
3. Does the Atanasov small-steps pattern hold when the first forecast is made by the same LLM (initial vs final accuracy split)?
4. Do current reasoning models (o1/o3-class, extended thinking) still stall in Qiu's multi-round task and on Belief-R? Evidence is mostly pre-reasoning models.
5. Does a code or calculator tool for posterior arithmetic help on realistic forecasting, not only toy worlds (Filbry)?
6. Does post-hoc extremising (Platt) stack with, or replace, any in-scaffold update rule?
7. How does an LLM resist non-evidence pushback while still retracting on a defeater (sycophancy vs Belief-R trade-off)? Is there a single prompt that improves both?
8. Is the primary Atanasov paper's key set (N=515, b=0.098) reproduced independently, e.g. in later IARPA or Good Judgment Open data?
9. Does the Augenblick-Rabin excess-volatility test work on LLM forecast streams to detect over- or under-reaction without outcomes?
10. Do the IRT reanalysis (b24) and Fildes caveats change which update traits are causal versus markers?

## Gap search results
Search tools were mostly blocked this pass (WebSearch budget used up; arXiv, Semantic Scholar and OpenAlex APIs returned rate-limit errors). Work was done by opening arXiv PDFs directly and reading them with pdftotext. Evidence is in evidence_d.jsonl (d01-d18); claims K23-K29 added, K07/K11/K12/K14/K15/K19/K21 updated with new evidence ids.

Closed or partly closed:
- Gap 7 (sycophancy vs retraction): partly closed. Laban 2024 (46% flip, 17-point drop; tuning cut 60%), Xie 2024 (confirmation bias and easy capture in one model), Wei 2024. Finding: no paper scores hold and retract together, so a single prompt for both stays unproven (K25).
- Gap 6 (extremising stacking): partly. Pratt 2024 shows low-probability bias and that plain Brier on skewed data misleads; no test of Platt extremising together with an in-scaffold rule.
- Gap 5 (code tool): partly. Hsieh 2024 agent with Python matched the crowd (0.169 vs 0.172), but Python was never ablated alone.
- Gap 9 (Augenblick-Rabin on LLMs): closest analogue found, Falck 2024 martingale test on synthetic streams (violations at long horizons). Not run on forecast streams.
- Gap 10 (IRT and Fildes): abstract re-read, no new numbers; publisher page blocked. Stays open.

Still open:
- Gap 1 (explicit S5 vs CoT at equal tokens): no study found. Pratt 2024 shows added strategy prompts did not help plain Brier.
- Gap 2 and 3 (LLM step size, first vs final accuracy): none of the eight papers opened reports it.
- Gap 4 (reasoning models): Qiu 2025 and the current ForecastBench PDF have no reasoning-model results; Qiu names it as future work.
- Gap 8 (Atanasov reproduction): Wharton PDF still a 1-page file; no independent replication found.

Notes: d05's 38.2% figure and d02's per-model cells are approximate (text extraction). d12's 0.86 is my derivation.
