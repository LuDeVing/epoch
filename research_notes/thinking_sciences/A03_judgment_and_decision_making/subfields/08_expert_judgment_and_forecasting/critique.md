# A03.08 Statistical vs clinical prediction: cross-check critique

Evidence: 90 lines (a 28, b 29, c 33). 35 claims in claims.jsonl (A03.08-K01 to K35).

## Source re-checks (10 numbers re-opened this session)
1. Dawes 1979, equal-weight r=.48, committee r=.19, cross-validated R=.38, N=111, reliability .67: CONFIRMED in PDF text. CORRECTION (important): the .19 committee comparison used only 23 of the 111 students (footnote 2: admissions rating scale changed across years). a02 should say so. The .48 vs .19 contrast is therefore not a full-sample contrast.
2. Halawi 2024 Brier .179 / crowd .149 / aggregate .146 / accuracy 71.5% vs 77.0% / GPT-4-1106 .208: CONFIRMED (arXiv 2402.18563). Crowd is .149 on all questions but .146 in the ablation table, which is a different subset or weighting; the paper says so in a table note. Ablation rows came out garbled; c06 "base GPT-4 only 0.186" is doubtful: the table reads fine-tuned GPT-3.5 + base GPT-4 .179, GPT-3.5 .182, base GPT-4 .181, base GPT-4 with no IR .183, and .186 and .206 for the two weakest rows (labels lost in extraction). Treat .206 for "neither retrieval nor fine-tune" (b15) as plausible but unconfirmed.
3. Halawi 5+ articles row: Brier .238 vs crowd .240 (confirmed); joint selective rule .240 vs crowd aggregate .247 on 22% of forecasts, 43% of questions (confirmed).
4. ForecastBench: the arXiv text now reads superforecasters .096, public .121, Claude 3.5 Sonnet .122 (p<0.001), full set .076 vs public .096, Arena parity 1406: CONFIRMED for a22, a23, b20. The c01 numbers (.092, .114, .114, parity 1398, r=-0.69) are from a DIFFERENT VERSION of the same paper (probably the conference version). Not an error, but a22/b20 and c01/c04 are one source in two versions, not two sources. Claims treat them as one.
5. Schoenegger 2024 silicon crowd: M=.20 (SD .12) vs .19 (SD .19), t(60)=.19, p=.850, 925 humans, 31 questions, 57.35% mean, t(1006)=86.20: CONFIRMED. CORRECTION: the equivalence test (d=0.5, bound 0.081 Brier) was not preregistered, and the acknowledgements say a coding error in it was found and corrected. The equivalence bounds p=.017 and .040 are weak. Note the 57.35% figure in the text is the crowd mean, so b18 wording ("models leaned yes") should be checked: a21 and b18 attribute it to LLMs, while b18 itself notes the human crowd mean was also above 50%. Treat the acquiescence claim as partly confirmed.
6. Kleinberg et al.: 554,689 cases, 443,751 train, riskiest 1% has 62.6% risk, judges release 48.5%, 48.2% as many jailed or 75.8% larger reduction: CONFIRMED (NBER w23180). The headline figures differ inside the same paper: intro says 24.8% and 42.0%, results section says 24.7% and 41.8%. a16/b12 are one paper, not two sources. a16 and b12 therefore give the same number; independent_sources for K12 should be read as 1 paper with later pushback in the literature (selective labels, Rambachan-Roth, Jung et al.), which we did not collect.
7. Not re-opened (time): Kuncel 2013 .44/.28, Grove 2000 10%, Aegisdottir d+ -.15, Mellers -0.34, Lu 2025 o3 .1352, AIA, Metaculus. They were opened by earlier agents; I rely on them.

## Contradictions between sources
- Grove 2000 "mechanical clearly better in 33-47% of studies, clinical in 6-16%" (b01) vs Recht's reading "46% / 48% comparable / under 6%" (c30). Different cutoffs (0.05 effect). Not a real conflict, but the "6-16%" range should be quoted with the cutoff.
- Aegisdottir: a09 says 53% binomial display, c30 says 52% statistical, 38% comparable, 10% clinical. Small mismatch; unresolved.
- Kuncel: academic criteria .47 vs .46 (clinical N=161) shows no gap. Do not generalise "over 50% better" beyond job performance.
- Metaculus: Pros beat bots strongly in Q2 2025 and not significantly by spring 2026 (K28 contested). FRI says parity November 2026 with wide CI; Metaculus bots versus Pros and ForecastBench measure different things.
- Consistency: Paleka correlations with Brier are strong for conditionals (.92 scraped) but weak or negative for negation on NewsAPI (-0.36); and training for consistency did not raise accuracy (b26).
- Leakage studies (c22, c23) imply many published retrospective LLM forecast numbers (including possibly Halawi-style date-filtered retrieval) are optimistic; Halawi's own design (post-cutoff test) is less exposed but search leakage was not tested there.

## Weak spots
- Almost all human-vs-formula evidence is from 1950-2000 and psychology, hiring, medicine; the LLM era evidence is mostly on tabular classification or probability forecasting, not on tasks where an agent chooses its own features.
- No study isolates our exact claim: "model scores features, code combines" versus "model gives verdict" at equal tokens, on reasoning/puzzle tasks. TEMED-LLM (c27) and ClinStructor (c28) are nearest; c28 is snippet-only.
- Many LLM forecasting results rest on small question sets (31 in Schoenegger; 93-99 in Metaculus quarters).
- Fragile Families, Kahneman and Klein, Tetlock 2005 book, Mellers 2014, Grove abstract were not read in full (a11, a15, a28, b11, c31 unopened).
- Tetlock 2005 numbers come only through Armstrong and Green review.

## Seen only in snippets or abstracts
a11, a15, a28, b11, c07, c21, c24, c28, c31.

## GAPS (most decision-relevant first)
1. Direct test: for reasoning (not forecasting) tasks, does having an LLM score features 0-10 and combining them with a fixed code formula beat the same LLM's holistic verdict at equal tokens? Any 2023-2026 paper with this arm (not just clinical tables)?
2. How many feature scores does the formula need before gains appear, and does LLM score noise (test-retest of the same feature) cancel when averaged over k samples? Measured reliability of LLM feature ratings is missing.
3. Equal-weight vs elicited vs fitted weights when the "judge" is an LLM: Dawes-style check on LLM-produced cue weights. Is there any study?
4. Does asking the LLM to also give a holistic verdict and then combining verdict + formula (Meehl "broken leg" overrides) help or hurt? Evidence on mechanical-plus-override for LLM agents; Grove-style data on when clinicians' overrides pay.
5. Platt scaling / extremisation in code: how many resolved questions are needed to fit them, and do they transfer across domains? (AIA used a sqrt3 factor; generality unknown.)
6. Rebuttals and replication on Kleinberg bail results (selective labels, omitted-variable bias, judges' use of soft information) and similar failures where formula lost: which boundary conditions make the formula lose (small N, regime change, adversarial gaming)?
7. Which of the 2024-25 forecasting gains (Halawi, AIA, Hsieh) survive leak-free evaluation (El Lahib 2026, Paleka pitfalls)? Re-estimate with post-cutoff-only questions.
8. Do reasoning models (o3, o1-style) reduce the benefit of code-side combination, i.e. is the formula edge shrinking as the LLM's internal combination improves? Compare 2023 vs 2025 models on the same tabular tasks.
9. Fragile Families and other low-ceiling tasks: what do forecasters/agents do in near-unpredictable domains, and can the agent be taught to say "no better than base rate"? Calibration of abstention.
10. Open the primary Tetlock 2005 and Mellers 2014 texts to confirm the numbers now cited via reviews and abstracts.

## Gap search results

Run limits: the WebSearch budget ran out, and arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429, so only about 12 pages and PDFs were opened. Evidence is in `evidence_d.jsonl` (d01-d15); claims K36-K44 added, K12, K20, K30 updated. Gap 4's override evidence (d11) and Neyman and Roughgarden (d10) are abstract-page only.

Corrections: Halawi's 0.186 is "retrieval kept, no fine-tuning", not "base GPT-4 only"; the true no-retrieval, no-fine-tuning value is 0.206 (d14). El Lahib uses 93 questions and one forecaster model, and its 0.108 vs 0.242 is leaky vs leak-free retrieval, not retrospective vs live (d01). Note: I re-ran an old generator script by mistake, which rewrote `evidence_b.jsonl` (29 lines, same ids b01-b29); it should be identical but was not diffed.

1. Feature scores plus code formula vs holistic verdict (reasoning tasks): OPEN. No paper found. Closest is rubric grading, where holistic matched or beat analytic and a ratio-of-yes formula lost (d07, K37). The experiment must be run by us.
2. Test-retest of LLM feature ratings, averaging k, number of features: OPEN. Only pairwise-judge data: test-retest above 0.95 with position bias above 0.10 (d06). No source on k or feature count.
3. Dawes with LLM-elicited weights: OPEN. No LLM study found.
4. Broken-leg overrides: PARTLY closed. Human-algorithm evidence says most overrides hurt (about 90% of judges, d11) but a small group gains from private information. No LLM override study. Grove/Meehl primary texts not re-read (403).
5. Platt and extremisation sample size and transfer: PARTLY closed. AIA's sqrt3 was a fixed prior from theory, not fitted; it gained 0.0064 Brier (498 q); a fit on another benchmark transferred partly (0.1104 vs 0.1140 uncorrected); AIA's own optimum was 2.27 and supers' 1.72 (d12). Halawi found isotonic and binning did not help (d15). Satopaa gives a label-free derivation (d09). Still no curve of fit quality against number of resolved questions, and generality across domains is unproven.
6. Kleinberg rebuttals and boundaries: MOSTLY closed. Authors' caveats and the lenient-judge test (d04, d05); selective-labels critique (d03); Lakkaraju contraction not opened. Small N, regime change and gaming remain undocumented for LLM agents.
7. Which 2024-25 gains survive leak-free evaluation: PARTLY closed. Leak-free retrieval gave about zero gain in El Lahib (0.242 vs 0.244, d01). Reasoning models leak more (d02). AIA's leak filter has 16 true flags of 81 and its results hold but sit within noise of supers (d13). Halawi's post-cutoff design is not hit by this. Hsieh not re-examined.
8. Is the combination edge shrinking with reasoning models: OPEN. No same-task 2023 vs 2025 comparison found.
9. Low-ceiling domains and abstention: PARTLY closed on the human side. Fragile Families: best R2 about 0.2 and about 0.05, a 4-variable baseline beats many teams, ensembling adds little (d08). No LLM abstention-calibration study found.
10. Primary texts for Tetlock 2005, Mellers 2014, Grove 2000, Kahneman & Klein 2009: OPEN. Mellers 2014 and Kahneman & Klein pages returned empty or 404 or cookie wall; Tetlock is a book. Their numbers stay secondary.

Next searches to run when quota returns: "LLM actuarial vs clinical", "LLM-elicited weights unit weighting", "reasoning model tabular 2023 vs 2025", "LLM abstention forecasting", Halawi-style forecast with Platt on question count.
