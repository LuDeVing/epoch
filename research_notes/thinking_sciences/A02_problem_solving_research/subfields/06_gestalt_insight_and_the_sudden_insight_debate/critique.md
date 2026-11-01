# Critique: Gestalt insight and the "sudden insight" debate (A02.06)

Cross-check of evidence_a, evidence_b, evidence_c (79 lines). Sources re-opened from the saved text in D:/research_scratch/A02.06 and checked against the evidence lines.

## Numbers re-checked

Confirmed against the source text:
- Danek and Wiley 2017: 1778 solutions, 417 of 1124 wrong ones above the correct mean (37%). The paper says 37 tricks were shown and 35 analysed; both a09 and b03 are right.
- Oellinger 2017 ten-penny: maximization group 72%; chi2(1,59)=23.80, phi=.64 (control vs maximization). Confirmed.
- Graf 2023: 34% solved, +11% after the hint, change point near the 90% bin. Confirmed.
- d'Aliberti and Ribeiro 2026: 6.31% pooled shifts, 2.57% vs 16.44% (N=723,200), 1.79% formal Aha, MATH-500 32.2% to 40.6% (+8.41pp, 50,574 vs 23,500). Confirmed.
- Wu 2025/2026: Aha in 8.3% of responses; up to -16.7% for VLAA models. Confirmed.
- Loewe 2024: humans 49/99, networks 46/99. Confirmed.
- Mizumoto 2025: subset human mean 52.9%; non-reasoning 7.6% vs reasoning 17.6%; verification failure 5.23% to 39.34%; Grok 4 29.5% (33/112) vs 48.8% (40/82), p=0.0071. Confirmed.
- Macchi 2025: 57% vs 13% (insight), 30% vs 80% (non-insight). Confirmed.
- Macchi 2026 pencils/matchsticks: 27.3% vs 32.6%; 46.7% (14/30) vs 79.3% (23/29). Confirmed.
- Bilalic 2019: 54% incremental, 27% sudden, 19% unclear; the 54% is "out of 26" Problem B solvers in the first five minutes. Confirmed.
- Schoenauer 2018: incubation F=0.008, sleep F=0.047, initial matchstick solve 45.5%. Confirmed.
- Wiley 2026: 377 students, 1508 trials, F(1,1091)=112.17. Confirmed; exclusions were 223 repeats and 120 missing, so the analysed count is near 1165 (a20 says 1164, fine).
- BRAINTEASER: 53% and 63% vs human 92%. Confirmed.

## Corrections

1. **a08 (Graf 2023) is misleading as written.** It says solvers' dwell "bursts up" as a finding. Footnote 2 says the sudden-shift figure is SIMULATED data and that the original Bilalic 2019 data indicate a gradual shift. b02 already notes this; a08 should be read with it. The claim K02 reflects the corrected reading. The paper is a methods argument, not new evidence for suddenness.
2. **b19 "majority vote 65.5 vs CoT 49.5" is not a verified comparison.** The 65.5 appears as a table cell (BoN with image, MathVista), not a majority-vote figure. Drop that pair. The checked figures are 8.3% aha rate and up to -16.7% for self-verification.
3. **b19 and c15 are the same paper** (Wu et al.), as are a26, b20 and c13 (Liu et al.) and c01 to c06 (d'Aliberti and Ribeiro). Independent source counts in claims.jsonl treat them as one each.
4. **b01 participant counts** ("73 on Problem A, about 61 on B") were not re-found; only "54% of 26 Problem B solvers" is confirmed. Treat the other counts as unverified.
5. **a11 "60.5% likelihood"** is second-hand and unclear; do not quote it.
6. **a09 date:** published online 2016 (Front Psychol), print 2017. Same paper as b03.

## Contradictions between sources

- Suddenness: Metcalfe 1986/87 (sudden warmth), Cushen and Wiley 2012 (68% sudden), Graf 2023 simulated demonstration vs Bilalic 2019 (mostly incremental, 54%), Danek 2018 (only 14% sudden, 10% incremental, rest flat or zigzag), Durso 1994 and Novick and Sherman 2003 (gradual). The answer depends on task, measure and statistic.
- Aha and accuracy: Salvi 2016 and Webb 2016 say insight answers are more accurate; Danek and Wiley say 37% of wrong answers feel like insight; Wiley 2026 says Aha follows cues. Both hold: the link is real on average but weak per item.
- Hints: ten-penny maximization hint 72% vs relaxation hints 7% to 21%; older nine-dot work says key hints do not help. Consistent, but both are one-problem results.
- Verbalisation: Macchi shows overshadowing; Gilhooly and Fleck and Weisberg do not. Contested.
- LLM aha: DeepSeek-R1 paper presents aha as functional; Liu, d'Aliberti, Wu say it is already latent, rare and not linked to accuracy. Yet a forced reconsideration pass helps MATH (+8.41pp) at doubled compute. Reconciled reading: spontaneous shifts are noise, prompted re-looks help, but compute was not matched.
- Mizumoto: GPT-5 is "inside the human CI" while reasoning models average only 17.6% on the subset; the comparison is for one best model, not the class.

## Weak spots

- Almost all classic evidence (Metcalfe, Durso, Novick and Sherman, Knoblich 1999/2001, Ohlsson 1992, Kaplan and Simon, Schooler 1993, Sio and Ormerod) was read through reviews or citing papers. Founding Gestalt works (Wertheimer, Duncker, Kohler) have no primary numbers at all.
- Most human work uses one or two problems (matchstick, ten-penny, magic tricks, CRAs); generality is untested.
- The strongest LLM evidence on spontaneous aha (d'Aliberti) uses small GRPO-tuned models (1.5B-class) and a forced pass that is not compute matched.
- LLM insight benchmarks are public quiz and riddle data with contamination risk (acknowledged by CresOWLve, NazoNazo, BRAINTEASER).
- Several LLM papers count "wait" words; this is a lexical proxy.

## Only seen in snippets or abstracts

a24 (Qiu et al., abstract only), a28 (BRAINTEASER pointer; later read in b23/c19), b10 (Becker 2024: no coefficients), b16 and b17 (from memory), a21 (only abstract and preprocessing), a19 (tables not read), c06 (per-cue appendix not read), c23 (human rows garbled).

## GAPS

1. At equal tokens, does an explicit restructure operator (relax constraint, decompose chunk, re-encode) beat extra independent samples plus voting on reframing items for a current frontier model? No study measures this; d'Aliberti's +8.41pp is not compute matched.
2. What is the best trigger for the operator: stalled focus on the same elements, high trace entropy, sampling disagreement, or a solvability probe? Only entropy has been tested, on small models.
3. How often does a current LLM write the right candidate and then reject it (verification failure), and how much does an endorse-or-reject step recover? Only Mizumoto's four models, by string match.
4. Do classic paradigms (nine-dot, Duncker candle, matchsticks, ten-penny) with human norms show models falling for the same traps and gaining from the same hint types (maximization vs relaxation)? No paper found.
5. Does forced step-by-step reasoning hurt reframing items the way concurrent verbalisation hurts people (57% to 13%)? Untested on LLMs; Haq's n=6 is too small.
6. Is restructuring in LLM traces better described as a sudden jump or a ramp? Nobody has run change-point vs linear models on reasoning-trace step content.
7. Does a gradual latent-progress probe (relatedness of elements to goal) predict later success in LLM traces, as Durso and Novick and Sherman suggest in humans?
8. How much of the gain on riddle and lateral benchmarks survives reworded private twins and post-cutoff items, across current models?
9. Do founding studies (Duncker 1945, Maier 1931 two-string, Metcalfe and Wiebe 1987) replicate with the original numbers? Primary numbers are missing here.
10. Does false insight (confident wrong shortcut) appear at a measurable rate in a verified-scaffold agent, and does a constraint check against the original problem catch it?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d24, all opened this session; d19 is abstract only). Claims K30 to K41 were added and K02, K04, K05, K10, K17, K18, K19, K22, K28 gained evidence ids and notes. K05 moved to contested. Totals now: 18 established, 9 contested, 14 single-source. Search note: the arXiv API and OpenAlex rate-limited every call, and the web search quota ran out for a while, so some leads (Duncker 1945, Maier 1931, Adamson 1952, Glucksberg 1962, Fox 2011) were not opened.

Status per gap:

1. Compute-matched restructure vs samples plus voting: OPEN. No study uses an explicit restructure operator. Related data conflict: self-correction and debate lose to self-consistency at equal responses on 2023 models (d11); voting 8x16K beats 128K sequential for a 1.5B model (d12); refinement chains beat voting in 43 of 45 matched-token cells but with a 4096-token cap and a misprinted headline cell (d13). Re-encoding the problem before sampling beats plain sampling at equal paths on easy math (d14, d15). Claims K31, K32.
2. Best trigger: OPEN. Each candidate has separate evidence (entropy forks d10, confidence d09, switch counts d08, fixed-round restart d16 at n=5) but no head-to-head. Switching a lot goes with failure, so a stall trigger needs a minimum depth. Claim K33.
3. Verification failure: PARTLY CLOSED for the phenomenon, OPEN for the rate. Probes show correctness is encoded (AUC over 0.9; d04), over 70% of wrong responses contain a dropped correct thought (d08), injected truth is ignored (d05), and only 5.4% of rechecks are corrective (d06). No endorse-or-reject recovery figure exists. Claims K30, K36.
4. Classic paradigms with human norms: OPEN. Still no nine-dot, candle or matchstick run on LLMs. Near misses: MacGyver (d20, 2023 models, divergent step +6.5 points for GPT-4) and a children replication of the Duncker pre-use effect (d24) that gives a design. Claims K39, K40, K28.
5. Forced step-by-step hurting reframing: OPEN. CoT hurt 3 of 6 human-deliberation-harms tasks in LLMs, none an insight task (d17). Human verbal insight items showed no overshadowing (d18) and a Bayes reanalysis says some nulls are inconclusive (d19, abstract only). Claim K10 (contested).
6. Sudden jump or ramp in traces: OPEN, with leads. Averages are a ramp (d01); information arrives in bursts at plan and reflection tokens (d02, d03). Nobody fitted change-point vs linear models to single traces. Claim K34.
7. Gradual latent-progress probe: PARTLY CLOSED. Probes and truncated-trace answer distributions predict later correctness (d01, d04). Missing: a test that a flat probe predicts a failure that a restructure then fixes. Claim K35.
8. Reworded private twins: PARTLY CLOSED for older and fine-tuned systems. SemEval-2024 shows over 80% of entries dropping on reworded twins even with 80% training data (d21). Zero-shot results for 2025-26 reasoning models on private twins were not found. Claim K41.
9. Founding studies with original numbers: PARTLY CLOSED. Metcalfe and Wiebe 1987 is now primary (d22): small samples (19 usable of 26; 39 usable of 73 for warmth), correlations .26 and .23. It did not replicate with self-reported insight (d23, N=51). Duncker's pre-use effect replicates in children (d24, 18% vs 89%). Wertheimer, Duncker 1945, Kohler, Maier 1931 original numbers were not obtained. Claims K38, K39.
10. False insight rate with verification: OPEN. No measured rate for a verified agent. Relevant: 30% to 60% of steps are decorative (d07) so a check must gate the answer; confident insight answers in people were not safer and wrong ones were sticky (d23). Claims K19, K36.

Corrections and cautions from this pass:
- d13 (Sequential Edge) text and table disagree: the text calls 76.7% vs 30.0% an AIME-2025 result, the table puts it on GPQA-Diamond (AIME-2025 at 6 chains is 83.3% vs 40.0%). Treat the 46.7 point headline as unverified.
- b01 caveat resolved: in Metcalfe and Wiebe Exp 2 the 73 are recruited students; 48 gave usable feeling-of-knowing data and 39 usable warmth data.
- d12 numbers are read from a garbled table extraction and are marked as a reading.
- Two preprints (d13, d16) are weak (cap on chain length; n=5 puzzles). Do not build schema rules on them alone.

What the schema should take from this: keep the restructure operator, gate it behind a minimum-depth stall, make any verification step able to change the answer, prefer a restart with a verified-facts summary over patching a long wrong prefix, and test each of these at equal tokens against independent samples with confidence-weighted voting.
