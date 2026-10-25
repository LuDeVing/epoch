# Critique and cross-check: Hypotheses in debugging (E09.02)

Method: re-opened primary PDF text for Alaboudi and LaToza 2020 (arXiv 2005.13652), AutoSD (2304.02195), Olausson (2306.09896), Huang (2310.01798), ChatDBG (2403.16354), debug-gym (2503.21557), Debugging Decay Index (2506.18403), Jhaveri (2604.02485) and FalsifyBench. Numbers were checked against the text and tables.

## Confirmed
- Alaboudi 2020: 11% / 25% / 39% correct hypotheses (3/27, 9/35, 15/38); OR 6.24 (SE 0.88, p=0.03; text p=0.0388); fault locations OR 1.4 p=0.64; p=0.4125, 0.1320, 0.6710; 20 of 60 failed, 6 of those had the correct stage-2 hypothesis; 5x odds for a correct stage-2 hypothesis; time f=0.51 p=0.61.
- AutoSD: 73% vs 63% plausible, DONE +12.4 / -11 points, 89% vs 82%, about 5x longer, 7 of 12 and 2 worse in human study.
- Olausson: 33.3 to 52.6 (GPT-4 vs human feedback), per-difficulty table, 32/80 vs 7/80 inaccurate.
- Huang: GSM8K 75.9 to 75.1 to 74.7; CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0. Columns are labelled "# calls" 1, 3, 5, so "round 1 / round 2" is a loose reading of calls 3 and 5.
- ChatDBG 57/67/85% and 36%/55%; debug-gym 37.2 / 48.4 / 52.1 (column inferred by position, Claude 3.7); Debugging Decay 72.56 to 82.82 and 84.1 to 92.1; FalsifyBench 41/75/68/12/21 and OR 0.016; Jhaveri 29 people, 6 right first, 21 eventually.

## Corrections made
1. "Six times" is an odds ratio from an ordinal logistic model with wide uncertainty and N=20. Raw success is 16/20 (80%) for hypotheses vs 11/20 (55%) control vs 13/20 for fault locations (all three sum to 40 of 60, matching 20 failures). The raw risk ratio is about 1.45, not 6. Any claim that "hypotheses give six-fold gain" should say "odds ratio 6.2".
2. b01 attributes "2/6, 4/6, 7/8" to the hypotheses group. The PDF layout is interleaved, but the sums only work if 5/6, 5/8, 6/6 is the hypotheses group (16/20) and 2/6, 4/6, 7/8 is fault locations (13/20); 4/8, 2/6, 5/6 is control (11/20). Treat b01's per-task numbers as misassigned. The table layout is still ambiguous in pdftotext.
3. b07 says years of experience was not significant. Table IV gives experience OR 1.14 per year, p=0.04 (significant); technology knowledge OR 2.19 p=0.07. The paper says supplied hypotheses are a stronger predictor, but the scales differ (binary vs per year), so the comparison is loose.
4. a02/b03: 11/25/39% are shares of hypotheses. At participant level, control had a correct hypothesis in 45% (stage 2) and 75% (stage 3). So "developers rarely hold a correct hypothesis" is true early and not true by the last stage. Median hypotheses per defect was 1 at stages 1-2 and 2 at stage 3 (not 2 throughout).
5. AutoSD repair counts (a18, c01): ARHE LLM-Base 179 plausible / 177 correct; AutoSD 189 / 187. Defects4J 1.2: LLM-Base 87, AutoSD 76 (AutoSD worse by 11). Defects4J 2.0: 110 vs 113. Net is parity with mixed sign, not a win.
6. c14: the human I:C 1.79 vs 0.24 is based on 6 first-correct people vs the rest; small groups.
7. a20/c03: participant split is 8 undergraduates, 6 graduates, 6 professionals (14 students).

## Contradictions between sources
- Hypothesis-driven view (Alaboudi, Katz and Anderson, AutoSD) vs observational view (Li and Coblenz 2026: no formal hypotheses; Bohme-style data: stating and testing a hypothesis 79 vs 832 code inspection instances). The two can both hold: speculation is informal, and outside hypotheses help anyway.
- Supplied hypotheses help (Alaboudi) but supplied locations do not; Whyline (asking why) helps strongly. Common thread is explanation of cause, not location.
- AutoSD parity with plain sampling vs Olausson (self-repair barely beats resampling at equal budget) agree; ChatDBG and debug-gym report gains but use different baselines and no equal-token control.
- Debugger helps strong models and hurts weak ones (debug-gym) vs ChatDBG's strong gains; model strength and task type explain it.

## Weak spots
- The only direct test of "hypotheses help" is one lab study: N=20, 3 small tasks, graduate students, median 2 years experience, Stack Overflow API-misuse bugs, supplied hypotheses written from the accepted answer (one is always right). No replication found.
- Supplied-hypothesis condition always contained the correct answer plus one wrong one; this is closer to a multiple-choice than to "a hypothesis".
- Whyline numbers are from the authors' own tests, small.
- LLM results mostly lack equal-token controls; AutoSD costs 5x time.
- FalsifyBench and Jhaveri use rule-discovery games, not debugging.

## Seen only in snippets (opened:false)
Gould 1975, Vessey 1985, Katz and Anderson 1987, Gilmore 1991, Bohme DbgBench 2017, Zeller, Shapiro, Banatt. Also Parnin and Orso 2011, Li and Coblenz 2026, Alaboudi episodes 2021 and the Whyline papers were not re-opened in this cross-check (earlier agents marked them opened). The famous "novices hold early hypotheses" claim (Vessey) rests on an abstract.

## GAPS
1. Does supplying a correct, a wrong, or no hypothesis to an LLM change repair rate at equal tokens (the direct replay of Alaboudi, including wrong-hypothesis harm)?
2. Does a wrong supplied hypothesis cause fixation in LLMs, and how much (Alaboudi never tested wrong-only)?
3. What is the repair gain of the scientific-debugging loop vs best-of-N resampling at equal tokens, on current models and on SWE-bench-style tasks?
4. Can an agent generate diagnoses as good as human ones (Olausson gap 33% to 53%)? Does generate-many then evaluate (Xiong: evaluation beats generation) close it?
5. How many hypotheses should be held, and when should the agent switch (links to Hypothesis limits in troubleshooting)? Alaboudi shows median 1-2; no dose-response is known.
6. Does the Alaboudi effect replicate with professionals, real bugs and larger N? Is the six-fold odds ratio stable?
7. Do the primary classics (Gould, Vessey, Katz and Anderson, Gilmore) say what the secondary summaries say about early-hypothesis fixation? Need full-text reading.
8. When is a forced written hypothesis harmful (Li and Coblenz: premature commitment avoided deliberately)? Does a hypothesis template hurt on easy bugs?
9. Do disconfirming-test rules (Think-in-Opposites, Dual-Goal) transfer from rule-discovery games to code debugging?
10. After a failed hypothesis test, does restarting context with only rejected hypotheses beat keeping history (Debugging Decay Index used small local models only)?

## Gap search results (evidence_d.jsonl, d01 to d16)

Search note: the web-search quota ran out mid-run, OpenAlex and Semantic Scholar returned rate-limit errors, and the disk was full for a while. All sources below were opened as arXiv full text this session.

Closed or partly closed:
- Gap 2 (wrong hint in LLMs): partly closed. XYEval (d01 to d03) injected a wrong cause into SWE-bench Verified; pass@1 fell 77.2 to 68.8, 78.0 to 70.8, 79.8 to 71.4 (about 9 to 11% relative), and up to 46.7% on terminal tasks. Real test runs recovered part of the loss. Still missing: a hint written by the agent itself, and matched tokens.
- Gap 10 (restart vs keep history): partly closed for small models. Verma (d04, d05) found re-showing the failed attempt cost 6.1 to 6.9 points at 1.5B and 3B vs a blind redraw, with anchoring as the mechanism. Can (d06) agrees on the code-re-exposure harm but finds executed facts help. Frontier models and rejected-hypothesis-only restarts are untested.
- Gap 6 (is the six-fold stable): re-read of Alaboudi (d13). The odds ratio is 6.24 with an approximate 95% CI of 1.1 to 35; raw 16/20 vs 11/20 is p about 0.18 by Fisher exact (my calculation). Time did not improve. No replication found. The claim stays single-source.

Still open:
- Gap 1 (correct vs wrong vs none hint on LLMs at equal tokens): no study found. XYEval has only the wrong arm.
- Gap 3 (loop vs best-of-N at equal tokens): no current-model equal-token SWE-bench test found. Evidence is older (Olausson, d08) or small-model (Verma, d04) or unmatched cost (SWE-Doctor 1.9x, AutoSD about 5x; d10, d12). Claim K21 records this.
- Gap 4 (can generate-many-then-pick close the human gap): Olausson numbers re-confirmed (d09: 33.3 to 52.6, 32/80 vs 7/80 wrong), but no test of generating many diagnoses.
- Gap 5 (how many hypotheses): CogniGent (d11) ablates the module, not the count. No dose-response.
- Gap 7 (classics full text): not reached. OpenAlex and Semantic Scholar were rate-limited and no open PDF was found. Gould, Vessey, Katz and Anderson, Gilmore stay at opened:false.
- Gap 8 (forced hypothesis harm on easy bugs): nothing new found.
- Gap 9 (disconfirming-test rules on code): FalsifyBench (d15) has no code task. Its useful addition is the Klayman and Ha scope condition (K24).

New caveats found:
- Alaboudi's supplied locations also held a wrong item (listed first), so no human wrong-only arm exists either.
- Human data on wrong LLM output: hallucination loops (d14, N=24 recordings, no test) and AutoSD wrong reasoning accepted in 1 of 12 review items (d10).
- Small-model preprints (Verma, Can, Arimbur) are single-author and disagree on whether feedback content matters; treat as hypothesis-generating.
