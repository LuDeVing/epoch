# E18.01 Bounded rationality and satisficing: cross-check

Checker re-opened the PDF text (this session) for: Chen et al. 2024 (a22/b17/c01-c04), Gigerenzer and Goldstein 1996 (a08), Reutskaja et al. 2011 (a12/a13), Chen et al. 2023 GARP (a19/c08), Liu et al. 2024/ICLR 2025 (b19/c05), Hagendorff 2023 (c12), Aggarwal et al. 2023 (c17), Tree of Thoughts (c20), Snell et al. 2024 (c21), Brown et al. 2024 (c22), Chehade et al. 2025 (a21/b15).

## Confirmed
- Chen 2024: 1,953% more tokens on "2+3"; 38.7% / 287 tokens first round on ASDIV; SimPO -22.3% on MATH500. Confirmed.
- G&G 1996: .658 TTB, .657 regression, .623 weighted linear, .621 unit-weight, 858 million tests, 26-student pilot. Confirmed. (Note: the table in the text gives regression .657; a08 says .657 in one place and TTB/WT/regression ordering is right.)
- Reutskaja 2011: best seen item chosen 76/73/69% (N=4/9/16); stop-probability slopes 6.4/4.8/4.3%. Confirmed.
- Chen 2023 GARP: no violations 95/89/81/92 of 100; mean CCEI .998/.997/.997/.999 vs humans .980/.985/.967/.963; invalid rate 4.7% (T=0.5) and 9.8% (T=1). Confirmed.
- Hagendorff: ChatGPT-3.5 59% and ChatGPT-4 96% correct; intuitive wrong 15% and 0%; humans 38% correct vs 41% in the original (n=3,428). Confirmed.
- Aggarwal: up to 7.9x fewer samples, under 0.1% average drop. Confirmed. Tree of Thoughts 7.3/4.0/45/74/49 confirmed. Brown 15.9% to 56%, SOTA 43% confirmed. Snell 4x and 14x confirmed. Chehade +22.3% win-tie confirmed, and the "over 90% harmless at reward >= -12" statement confirmed.

## Corrections
1. b19 (Liu): "GPT-4o CoT MSE 0.0278 vs humans 0.2580" is the MSE of CoT predictions against the maximum-expected-value rule (Table 2), not against human choices. Humans' own correlation with EV is 0.48. Also the zero-shot correlation with EV is low (GPT-4-Turbo 0.41, GPT-4o 0.28), so "LLMs are rational" holds for CoT, not zero-shot. The Spearman values in b19 for CoT vs human choices (0.639 etc.) could not be placed: the extracted Table 1 has scrambled row labels, and 0.6393 appears next to MSE-like values. Treat the per-model human-choice correlations in b19 as unverified. c05 values for CoT vs EV (0.94/0.93/0.80/0.76/0.57) are confirmed by the paper text.
2. b17 vs a22 vs c04: the 48.6% token cut on MATH500 is the abstract/Figure 1 headline. Table 4 shows QwQ MATH500 2407.9 to 1330.7 tokens (-44.7%) for SimPO FCS+Reflection. b17 itself notes ASDIV also shows 48.6%. Quote 44.7% from the table and the headline as "up to 48.6%". a22 and c04 should not be cited as MATH500 48.6% without that qualifier.
3. a22/b17/c01-c04 are one paper counted six times. Independent sources for the overthinking claim: one (plus a survey that only frames it). K05 downgraded to single-source.
4. a19 and c08 are one paper; b19, c05, c06, c07 are one paper. Do not count them as separate.
5. a21/b15/b16 are one paper (Chehade 2025).
6. b24 (Czerlinski 1999 numbers) comes from Wikipedia with "citation needed"; original not opened. K04 therefore single-source.
7. c21 Snell: ">4x efficiency" means about 4x less test-time compute than best-of-N at the same performance, only on some difficulty bins.

## Contradictions between sources
- Satisficing as stopping rule: Simon (a01) says threshold. Reutskaja (a13) rejects a sharp threshold; a soft/hybrid rule fits. Gigerenzer (a11) and Stigler-style readings (a11 limits) disagree on whether bounded rationality is "optimisation under search cost" or something different. Simon's own Nobel text says adaptive aspiration may approach optimal choice (a01).
- Choice overload: Iyengar and Lepper (b02, b03) large effects vs meta-analysis (b04) mean effect near zero. Moderators (b05, b06) are second-hand.
- Maximizing: unhappy-maximizer story (a16, b07, b09) vs positive time-lagged results (b10). Salary advantage (a18, b07) only from memory or second-hand.
- LLM rationality: GPT-3 shows human-like biases (a20, c10, b20) vs GPT-4-class models that look rational (a19, b19, c12). The difference is model generation and prompting, not a contradiction, but it means pre-2024 bias papers should not be used for our agent.
- Early stopping helps (c17, b18, a22) vs CoT/deliberation hurts or helps by task (c16) vs more compute helps on hard items (c21, c22). Resolved only by a difficulty-conditional stop rule, which nobody has tested at equal tokens.

## Weak spots
- Founding studies are thin: Simon 1955/1956 were not opened (403). The 97% of 628 used-car dealers figure (a07) is from Wikipedia only and the source was not found.
- No source here measures a satisficing stop rule inside an LLM agent loop at equal total tokens against a fixed-budget baseline, with a label-free stop signal. Chen's oracle needs the ground truth.
- Judge dependence: Chehade is GPT-4 judged.
- Human-evidence samples are mostly students (N=17 to 552) and Western or Chinese university samples.

## Seen only in snippets or abstracts (not opened in full)
a06, a07, a18, a24, a25, a26, b04 (numeric d missing), b18, b20, b21, b22, b23; c13 and c15 partly. Iyengar 2000 and 2006, Chernev 2015 and Scheibehenne 2010 were not read; I tried a Crossref abstract fetch and a Semantic Scholar lookup (rate limited), both without usable text.

## GAPS
1. Does a label-free first-good-enough stop (verifier pass, or consistency of two independent samples) cut tokens at equal accuracy against a fixed-budget baseline, across easy and hard items? Is there any published equal-token comparison?
2. What is the best difficulty probe for deciding how much to deliberate (cheap pilot sample, logprob, question features), and what does its error cost on hard items where first-correct stopping loses accuracy?
3. What is the numeric overall effect size (mean d with CI) of choice overload (Scheibehenne 2010, Chernev 2015) and does it carry over to LLM option lists? Is there an LLM study varying candidate-set size 3 to 24 for a selector?
4. Do LLMs show position or first-seen bias in selecting among candidates (Reutskaja found attention, not value, drives what gets seen), and how big is it for current models?
5. What are Simon 1955/1956 and Todd and Miller 1999 results with exact numbers (aspiration adjustment, 37% rule, human stopping earlier than optimal)? Opened sources needed.
6. Do any 2024-2026 papers test adaptive aspiration levels (raise after success, lower after failure) in LLM agents or search, as opposed to fixed thresholds?
7. Which reasoning-model overthinking papers beyond Chen 2024 replicate the "first solution correct in over 92%" figure on non-math tasks (code, planning, open QA), and on current models (post-2025)?
8. Is satisficing vs optimising decided by uncertainty versus risk (Artinger 2022) in a way we can detect in a task, and do any LLM tasks under genuine uncertainty favour simple stop rules?
9. Do verifier-free confidence stops (Beta test, early exit) hold up when samples are correlated (G4), measured as calibration error of the stop signal?
10. Does satisficing alignment (threshold on secondary objectives) hold with human judges and with a best-of-N baseline at equal samples?


## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d19; d05 and d16 are abstract only, the rest opened). Claims K05, K07, K08, K12, K16 and K20 were updated; K26-K31 were added. Search was limited: WebSearch quota ran out, Semantic Scholar and OpenAlex returned 429, and arXiv was rate limited intermittently. Several gaps are therefore "not found", not "disproved".

1. Label-free stop vs fixed budget (mostly closed, one part open). DeepConf (consensus 0.95, K=512) used 18 to 85% fewer tokens than majority voting with accuracy mostly kept (d07). ESC cut samples 34 to 84% (d08). DEER cut chains 19 to 80% on math and code (d10). Still open: all are Pareto comparisons against a longer fixed baseline, none at strictly equal tokens, and no head-to-head of verifier pass vs two-sample agreement.
2. Difficulty probe (mostly closed). A learned probe on hidden states ranks easy vs hard at 72 to 84% and saves up to 50% compute (d06). Prompt-only gating at zero steps is unreliable (d13). Cost of a wrong stop: 42.4% of confidence-stop failures and 54.8% of consistency-stop failures were recoverable by continuing (d12). Still open: no pilot sample vs logprob vs question-feature comparison on one benchmark.
3. Choice overload size (half closed). Scheibehenne: D = 0.02, CI about -0.09 to 0.12, I-squared 68% (d04). Chernev: significant once moderated, 99 observations, N=7,202, but no numeric d obtained (d05, abstract only). LLM set size 3 to 24: not found. Only indirect: accuracy falls as documents go from 10 to 30 (d03).
4. Position and first-seen bias (closed for 2023-24 models, open for current ones). Yes, measured in three studies (d01-d03, d19). No 2025-26 model was measured in an opened source.
5. Simon 1955/56 and Todd and Miller 1999 (still open). Nobel PDF 403, JSTOR not served, Sage mirror 403. The secretary-problem page gives the 37% rule and "people stop too soon" without numbers (d17). Needs library access.
6. Adaptive aspiration in LLM agents (not found, d18). Treat as an untested design choice.
7. Overthinking beyond math (partly closed). Open QA converges at about step 0 (d09); code keeps pass@1 with 34 to 80% of the tokens (d10, d12). The "over 92% first solution correct" figure itself was not reproduced, and there is no planning data.
8. Risk vs uncertainty (open). Artinger 2022 abstract only (d16); no LLM test found.
9. Calibration under correlated samples (open). Only within-chain probe calibration (ECE below 0.1 in distribution, worse on AIME, d11) and an overconfidence note in DeepConf (d07). No paper measures stop-signal calibration under same-model sample correlation.
10. Satisficing alignment with human judges and best-of-N (open). Re-read confirms GPT-4 judge only, no human raters, no best-of-N arm (d15).
