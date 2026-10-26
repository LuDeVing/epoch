# A17.02 Crowd within: cross-check and critique

Scope: 29 + 26 + 29 evidence lines (a01-a29, b01-b26, c01-c29), turned into 23 claims (A17.02-K01 to K23 in claims.jsonl).
Status count: established 10, contested 6, single-source 7, refuted 0.

## 1. Numbers re-opened against source text (10 checks)

| # | Number | Source text | Result |
|---|---|---|---|
| 1 | Vul and Pashler: N=428, t(254)=2.25, 6.08; t(172)=3.94, 6.59; CIs [2.5,10.4] and [11.6,20.4]; 1.11 and 1.32 people | vul.txt | Confirmed |
| 2 | Steegen: immediate N=471, MSE 589 / 615 / 541, dz 0.40 / 0.47; delayed N=140, 517? / 589 / 467, dz 0.72 vs guess 2 | steegen.txt | Confirmed. Delayed guess-1 MSE (517) not re-read |
| 3 | Steegen delay comparison: guess 1 t=0.18 p=.858, BF 12.9; guess 2 t=3.14 p=.002; original guess-2 t(426)=1.56 p=.12 | steegen.txt | t, p and the original-data line confirmed. The BF table is scrambled in the PDF text; BF 12.9 is paired to t=0.18 by column order, not certain |
| 4 | Wang et al.: PaLM-540B GSM8K 56.5 to 74.4 (+17.9); AddSub 91.9 to 93.7 (+1.8) | 2203.11171 | Confirmed |
| 5 | Huang et al.: GSM8K single 76.7; self-consistency 82.5 / 85.3 / 88.2 at 3 / 6 / 9; debate 83.2 (6) and 83.0 (9); CommonSenseQA 75.8 to 38.1 | 2310.01798 | Confirmed. Table is interleaved, so debate cells paired by row order |
| 6 | Halawi et al.: baseline 0.1676, trimmed mean 0.1649, USC 0.1691, human crowd 0.1600 | 2402.18563 | Confirmed |
| 7 | Li et al.: Llama2-13B ensemble 59 percent vs Llama2-70B 54 percent on GSM8K | 2402.05120 | Confirmed (text line). Figure caption says parity at ensemble size 15, results table uses size 40 |
| 8 | Brown et al.: coverage 82.9 to 98.44 percent; vote 40.50 to 41.41 percent | 2407.21787 | Confirmed |
| 9 | Fiechter and Kornell: inner crowd BF10 1417 untrained, 0.005 variance term trained | PMC7865038 | Confirmed for BF 1417 and 0.005. BF 0.02 not re-read |
| 10 | Fujisaki 2025 and Van de Calseyde sample sizes | PMC12371095, PMC13428925 | Two corrections, see below |

## 2. Corrections made

1. **a23 is wrong on N.** It says N=64. The paper says 76 undergraduates, 38 per condition (ensemble 38, repeated 38). b10 had it right. The t, p and d values (t=2.51, p=.012, d=0.59) and "1.51 persons at T=5" are confirmed. Use N=76. Claim K10 uses the correct value.
2. **a21 Exp 2 N.** a21 says 501, b07 says 495. Both are right: 501 recruited, 495 analysed after excluding people who looked up answers. Use 495 as the analysed N.
3. **a12 vs a07/b02.** a12 (Fiechter and Kornell) says the delay benefit "replicated in Steegen 2014". Steegen's own result is mixed (no extra gain vs guess 1, extra gain vs guess 2, post hoc). Trust Steegen. Claim K04 is "contested".
4. **c19 vs b17 on task difficulty.** c19 limits say gains are smaller on hard tasks (MATH, Llama2-13B 0.03 to 0.09); b17 and a26 say the gain is larger on hard tasks. Both are true in different units: absolute points are smaller on MATH, relative gain is larger (200 percent vs 16 percent). K07 states the relative gain and keeps the caveat.
5. **a22 vs b09 on Fujisaki 2023 sizes.** N=452 total in a22; n=150 in the other-perspective arm in b09 (confirmed in the paper). Consistent, not a conflict.
6. **Debate cells (c23, b18).** The b18 note that debate cells were unreadable is now settled for the cells that matter: debate 83.2 at 6 responses and 83.0 at 9, against self-consistency 85.3 and 88.2.
7. The b20 note "best single model GPT-4 0.15" and c02 "0.075" refer to different tables (full 31-question set vs a subset). Use 0.15.

## 3. Contradictions between sources

- **Delay helps?** Original yes (vs guess 1), replication yes only vs guess 2, field data yes, 2026 perceptual no. No clean story.
- **Dialectical bootstrapping.** H&H found a gain with 20 percent trimming. Reanalysis (White and Antonakis, not opened) could not reproduce it. Gomilsek 2024: no strategy difference untrimmed, d=0.40 when trimmed. The result depends on the analysis choice.
- **Mixing prompts / models.** Naik (DIV-SE) says varied approaches beat resampling by a lot. Wang et al. found 40 prompt sets worse (58.9) than 40 samples (74.4). Self-MoA says single-model aggregation beats mixed models. Likely explained by the quality of the mixed members, not tested.
- **Debate.** Du et al. (debate 81.8 vs majority 69.0 on arithmetic) vs Huang et al. (equal-response self-consistency wins). The comparison budgets differ.
- **Forecast resampling.** 1.6 percent Brier gain (Halawi, 6 samples, validation set) vs 7 to 35 percent error cut (Jaworski and Alam, 500 draws, abstract only). Different tasks, sample counts and metrics.
- **Size of LLM gains vs human gains.** Human inner crowd: about 8 percent MSE. LLM voting: +10 to +18 points on reasoning. The gap is about task type (discrete answer, varied reasoning paths, weak greedy baseline), not about a stronger "inner crowd". Do not transfer human numbers to the agent.

## 4. Weak spots

- Almost all human work is 8 to 20 percentage or quantity questions; one lab (Fujisaki) supplies the "different perspective" and "flat after 2 estimates" results.
- The main LLM numbers are from 2022 models (PaLM, LaMDA, GPT-3.5) with a weak greedy baseline. Modern models may be near ceiling or give zero spread (K06).
- Lambda is model dependent (interpolation on a fitted curve).
- No LLM study measured lambda, the within-model "equivalent number of independent samples". Closest data: Kim (between models), Lou and Sun (zero spread), Jiang (similarity).
- Halawi's gain (0.0027 Brier) is probably inside noise.
- Schoenegger is a between-model crowd; it is not a test of the inner crowd.

## 5. Only seen in snippets or abstracts (not opened)

Ariely et al. 2000 (via Vul and Pashler and Fiechter); Herzog and Hertwig 2009 and 2014 (abstract); White and Antonakis 2013; Rauhut and Lorenz 2011 (via later papers); van Dolder and van den Assem 2018 (abstract, 1.2 million observations); Litvinova et al.; Jaworski and Alam 2026 (abstract); Hourihan and Benjamin (page summary only). Claims that rest on these alone are marked single-source or carry a caveat.

## GAPS

1. What is the within-model lambda for current LLMs: the equivalent number of independent samples from k same-model samples, at several temperatures, on numeric and discrete tasks? (Decides how many samples are worth paying for; no study found.)
2. At equal tokens, does k-sample voting or averaging beat one longer reasoning pass for recent models (2025-2026) on our task types, and where does the curve flatten?
3. What share of items on our benchmarks have zero sample spread, and does a cheap spread test (2 samples) predict which items gain from more samples? (Tests the expertise boundary, K05/K06, and the G12 routing rule.)
4. Does fresh context (the agent analogue of a delay) lower sample correlation compared with continuing in the same context, and by how much?
5. For same-model forecasts and numeric estimates, which combiner works (mean, median, trimmed mean) and is the 1.6 percent vs 7 to 35 percent difference a task effect or a sample-count effect?
6. Does a forced contrary or other-perspective second sample (dialectical or "what would others say") help modern LLMs when combined by code, since Huang tested only self-revision? (Human evidence is contested.)
7. How much of the voting gain survives when the wrong answer is the modal answer (shared bias)? Need the rate of confident wrong majorities per task.
8. Are the original human findings robust to modern, pre-registered large samples outside percentage questions (Ariely 2000 and White and Antonakis 2013 never opened)? Open these two sources before citing them in the schema.
9. Does prompt-diverse sampling beat temperature sampling once quality of each prompt is controlled (Naik vs Wang conflict)?

## Gap search results

Evidence file: evidence_d.jsonl (d01-d26, all opened this session; two are abstract-only OSF preprints, d03 and d04). Claims file now has 32 claims: established 14, contested 6, single-source 12, refuted 0. New claims K24 to K32; changed K06, K07, K08, K10, K12, K14, K15, K17, K18.

Tools: WebSearch quota was used up and the arXiv/OpenAlex/Semantic Scholar APIs returned 429, so papers were found with the arxiv.org search page, OSF API, Crossref, Europe PMC and direct PDF links. Not opened: Jaworski and Alam 2026 (SSRN 403), Herzog and Hertwig 2009/2014 (paywalled).

| Gap | Status | What closed it, what is left |
|---|---|---|
| 1 Within-model lambda for LLMs | Mostly closed for small open models and discrete tasks | Same-model votes are worth about 1.3 to 2.9 independent votes: GSM8K correctness correlation 0.45 to 0.60, ceiling 1.7 to 2.2, reached by K=8 to 16 (d05); error correlation 0.35 to 0.77 over 5 models x 4 tasks, cap 1/rho (d08); 9 different frontier models gave 2.18 (d17). Temperature moves it (d12: 5-vote gain -0.06 to +2.57 points). Still open: current frontier and reasoning models, numeric tasks, a temperature curve for the same model. |
| 2 Equal tokens: k samples vs one longer pass | Partly closed, contested | Three studies say independent voting is at least as good as debate, sequential revision or one longer chain (d09, d14, d15); one says sequential refinement wins 43 of 45 (d13, with a table/text mismatch and 30-problem sets). Nobody has tested a current reasoning model at matched budget. |
| 3 Zero-spread share and a 2-sample test | Partly closed | The disagreement rate of two calls caps the gain from more votes (d11) and a K=4 pilot sets the budget (d07). Near-unanimous share: 32.7 percent (1.7B, T=1.5, d20); 0.6 percent disagreement (7B, T=0.2, d11); 98 percent single-pass (Gemini 2.5 Pro, d16). Open: per-item routing and the share on our own benchmarks. |
| 4 Fresh context vs same context | Partly open | Code: a retry that sees its failed attempt is near-identical in 33 to 68 percent of cases vs 2 to 14 percent fresh (d21); math self-refine gains 0 to 6.7 points (d25). No study measured lambda for fresh vs continued context on numeric tasks. |
| 5 Combiner and the 1.6 vs 7-35 percent split | Half closed | Mean, median, geometric and trimmed mean are within 0.0007 Brier (d24); asking the model to combine is worse. The 7 to 35 percent study could not be opened, so task effect vs sample-count effect is unresolved. |
| 6 Forced contrary or other-perspective sample, combined by code | Still open for LLMs | No LLM test found. Human side: the dialectical gain in the original data is an artifact of a score tied to identical answers (d02); a 2026 reanalysis found no gain from disagreeing perspectives (d03, abstract only). Persona prompts cost accuracy in 23 small models (d22). |
| 7 Confident wrong majorities | Mostly closed | Nine-model panel: all-wrong on 5.1 percent of items, unanimous answers right 90.9 percent (d17). gpt-4.1 on GPQA: high-agreement answers wrong 48 percent, 28 percent of cases wrong for every runner (d18). Voting drops as samples grow where the right answer is a minority (d19, partly built into the subset choice). Rates for our own tasks still unknown. |
| 8 Ariely 2000 and White and Antonakis 2013 | Closed | Both read first-hand (d01, d02). Ariely: N=64, probability score .252 to .250 within person vs .234 between. White and Antonakis: dialectical and control gain the same (d=0.38 vs 0.39). Large natural experiment (van Dolder) was already opened in sets a and b. |
| 9 Prompt-diverse vs temperature sampling, quality controlled | Partly closed | Prompt templates lower correlation by 38 percent on average (55 of 57 cells) but move accuracy only +-4 points, mixed in sign (d06); prompt variants did not beat temperature on AIMO 3 (d10); personas hurt (d22). No head-to-head with per-variant quality matched; DIV-SE result on GPT-4 is not reproduced. |

### New cautions found while checking

- **AIMO 3 correlation claim (d10) is an artifact.** The per-problem estimator the paper uses simplifies to exactly -1/(N-1) for every problem (checked algebraically and numerically: N=3 gives -0.5, N=8 gives -0.143, N=16 gives -0.067), which is the set of values the paper reports. Do not cite its "negative correlation".
- Sharma and Chopra (d13) text and Table 1 disagree on the Qwen3-235B AIME-2025 6-chain cell (76.7 vs 30.0 in text, 83.3 vs 40.0 in table). Treat as a hypothesis.
- The 2026 reanalysis (d03) comes from the same research tradition as the five-style ensemble paper (K10) and partly contradicts it. K10 stays contested.
- Correctness correlation (d05) mixes shared item difficulty with true dependence; the right quantity for planning is the spread of per-item success rates, which a 4-sample pilot can estimate.
- Operational note: one lookup (Unpaywall) was sent a placeholder address (test@example.org) in the query string by mistake; no real address was sent.
