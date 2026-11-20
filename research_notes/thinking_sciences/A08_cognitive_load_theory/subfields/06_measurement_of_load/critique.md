# A08.06 Measurement of load: cross-check critique

Cross-checker run 2026-11-19. Sources re-opened as full PDF text (pdftotext): Ayres et al. 2021 (Frontiers), Krieglstein et al. 2022 (Springer), David et al. 2024 (Springer), CogniLoad (arXiv 2509.18458), ICE / Adapala (2509.19517), CLAI / Zhang (2507.00653), Hu and Wang (2605.16938), Davidson (2508.20262), GSM-IC / Shi et al. (2302.00093). Claims are in claims.jsonl (24 claims, A08.06-K01 to K24).

## Confirmed (numbers matched the source text)

- Ayres 2021: detection subjective 30/32 (94%), eyes 20/23 (87%), skin 11/13 (85%), heart 15/22 (68%), brain 23/34 (68%); match 78/78/62/64/32%; Kruskal-Wallis chi2=9.67 df=4 p=.046 and chi2=18.52 p<.001; mean 29.2 participants per experiment. (b05, b06 correct.)
- Krieglstein 2022: 53 articles, 67 experiments, N=7413, mean sample 103.3 (SD 68.0), 63.5% women; alpha .776/.798/.734 (Leppink 2013) and ICL .851 (Leppink 2014); ICL-ECL r+=.298 (k=25, CI .221 to .370). (b01 to b03 correct.)
- David 2024: 35 papers, 83 samples, 236 effect sizes, total N=3973 (new detail); monitoring-learning .29; effort-monitoring -.19. (b11 correct.)
- CogniLoad: N=20 to 50 drops, "12 of 22 below 50% at d=5", N=250 gpt-5 .76 and o3 .68, 280 context errors for gemini-2.5-flash, ECL50 values. (a16, a17, c13 to c16 correct.)
- ICE: Gemini 0.85, 0.82, 0.78, 0.72; slope -0.003 (CI -0.004 to -0.002); Long Control 0.82, p=.45; Residue 0.78, p=.12; GPT-4o 0.65 control; about 32% omitted final answers; r=.42 and .35. (c01 to c04 correct.)
- CLAI Table 1 (92.5 at 485 to 92.3 at 310; 53.9 at 812 to 53.5 at 525) and CLAI-Tune 91.5 at 255. (c06, c07 correct as transcribed.)
- Hu and Wang: mean alignment .570/.567/.562; BF10 .41/.43/.42; 16/16, 16/16, 15/16. (b16 correct.)
- GSM-IC: under 30% macro accuracy, 99.7% recall in 20 samples, 45% best macro, text-davinci-003 role overlap macro 0, base CoT accuracy 80.0, GSM8K 59.3 to 60.3. (c09 to c11 correct.)

## Corrections

1. c10 (GSM-IC): the line "self-consistency raised micro accuracy by more than 11 points (35.5 for 0-CoT)" is ambiguous. In the paper 35.5 percentage points is the GAIN on 0-CoT; it is not an accuracy level. The 99.7% recall holds for CoT and LTM; for 0-CoT it is 96.5%.
2. b18 (Davidson): the paper uses SIX reasoning models, not three. Human N=1,854 and 27,810 decisions; analytic sample 27,071 pairs (27,052 for o3). The o3 mean reasoning tokens are 303.5, not 303.3. The overall human-RT to CoT-length correlation is LOW (r=.15 to .19), elasticity 0.09% to 0.28% per 1% of CoT length, and top vs bottom quintile is 26 to 39% longer human time. The line "one SD of CoT length is about 1 s" and "Grok 4 beta=1.245" were NOT found in the text (possibly in a table I did not match); treat as unverified.
3. b03 (Krieglstein): ECL-GCL for Leppink 2013 is r+=-.186 (k=20); the "largest negative -.331" comes from k=2 studies (Leppink 2014), so it is weak.
4. c15/a16: the layout view of the CogniLoad Table 3 misaligns rows; raw text confirms gpt-5 382.8, o3 356.9, gpt-5-mini 164.1, gemini-2.5-pro 153.3. Values stand, but anyone re-extracting should use raw mode.
5. ICE GPT-4o: the 0.60 in the table is the Long Control column, not 20% load. The table has no 20% column for GPT-4o; the 20% figure appears only for Gemini in the text.
6. a20 and c23/c24/c25 are the SAME paper (arXiv 2506.06843, "United Minds or Isolated Agents", Zhou 2025 / Shang 2026 version). Likewise a16 to a19 and c12 to c16 are the same CogniLoad paper. These pairs must not be counted as independent sources. Done in claims.jsonl.
7. David 2024: partial-model direct effort-to-learning beta=-.07 recorded as not significant (CI -.16 to .02); confirmed.

## Contradictions between sources

- Three load types: Klepsch 2017 and Leppink 2013 support three factors; Jiang and Kalyuga 2020 (N=60) fit two; Krieglstein's meta-analysis leans three-factor but shows correlations that contradict theory (ICL-ECL positive; ECL-GCL negative; Eysink GCL negative with learning). Status: contested.
- Eye tracking: Zu 2020 (atlas record) says it replicates DeLeeuw and Mayer; Korbach 2018 found the eye-tracking index did not separate groups. Neither full text was read.
- Effort as a dial: Hu and Wang find effort setting does not change alignment (inconclusive BF); the reasoning-length-as-working-memory paper and CogniLoad suggest budget changes matter. Different tasks and models; unresolved.
- Heart and brain measures: Ayres vote counts show low match, Hughes 2019 meta-analysis (abstract only) says cardiac metrics are sensitive. Detection vs match rates may explain part of the difference.

## Weak spots

- The two anchor papers of the subfield were never read: Hart and Staveland 1988 (a01, a25 placeholder) and DeLeeuw and Mayer 2008 (a10, second-hand). No number about TLX reliability, sensitivity or DeLeeuw and Mayer correlations is recorded. Skulmowski and Rey 2020 (a12) is known only through a later review. Paas 1992 / Paas and van Merrienboer 1993 (a14, a15) were not opened; the efficiency formula is from memory of the literature.
- Ayres 2021 is a vote count over 2016-2020 intrinsic-load studies with about 29 participants each; no effect sizes. "Brain 32% match" mixes EEG sub-measures with very different behaviour (beta 0%).
- The LLM literature here is mostly single-author preprints (ICE, CLAI) or one paper counted twice (CogniLoad). CLAI has an implausible 8B-student GSM8K 90.1 and a baseline mismatch between tables (92.5 vs 90.1).
- Almost no LLM paper measures "load" on the model itself with a validated instrument. Proxies (tokens, attention entropy, junk share) are chosen by the authors.
- Token alignment with human time is correlational, with human time including reading and motor time (Davidson r=.15 to .19). It tells little about accuracy.

## Only seen in snippets or abstract pages

a01, a10, a12, a14, a15, a24, a25 (not opened or second-hand); b20, b21, b22, b23, b24 (abstract or snippet); c17 to c22, c26 to c30 (abstract page only, mostly no numbers); c31 (narrow search, rate-limited). Claims K19, K20 and K24 lean on these and are labelled accordingly.

## GAPS (most decision-relevant first)

1. Does an LLM's own 9-point difficulty or effort rating (given before solving) correlate with its correctness and with output tokens, and does it beat tokens alone as a predictor at the same budget? No paper found testing this.
2. At equal total tokens, does an explicit "ignore irrelevant information" line plus context pruning improve accuracy on distractor-augmented tasks for current reasoning models (GSM-IC was on 2022 models; ICE tested one clean model)?
3. Is the token-to-human-RT link (rho .24 to .91) a predictor of ERROR on the same items, i.e. do items that make a model think longer fail more often, across model families and tasks?
4. What are the actual Hart and Staveland 1988 reliability and sensitivity numbers, and the DeLeeuw and Mayer 2008 correlations among the three measures (which sample sizes)? Both anchor papers are unread.
5. What did Skulmowski and Rey 2020 report (experiment, N, effect sizes) and did the "lab correlations did not hold outside the lab" claim in the subfield row come from them or from field studies (e.g. classroom studies)?
6. Does the CogniLoad "task length is the strongest limit" finding replicate on another benchmark, and does fixed-size decomposition recover the accuracy at equal tokens?
7. Do CLT-inspired structures (multi-agent split, token budgeting) still win when total tokens are matched? Zhou 2025 and CLAI both compare at unequal or unreplicated budgets.
8. Is there a model-internal load signal (attention entropy, logit entropy, hidden-state probe) that tracks difficulty better than token count? ICE and Zhou report only pilots.
9. Is the germane-load budget (S-state or O-operator) ever supported over a two-factor model for LLM agents, or is "reasoning tokens spent productively" indistinguishable from intrinsic load?
10. Does a replication of Eysink-style negative GCL-learning correlations exist, and do human-effort ratings predict later learning when confidence is controlled (David 2024 says only indirectly)?

## Gap search results

Gap-search run 2026-11-20. New evidence in evidence_d.jsonl (d01 to d17); claims.jsonl now has 29 claims (K25 to K29 new; K09, K10, K12, K14, K17, K18, K19, K21, K22, K02, K03, K24 extended; K17 and K18 moved to contested). arXiv and Semantic Scholar APIs were rate limited (HTTP 429), so coverage is narrower than planned.

1. Gap 1 (self-rated difficulty before solving): STAYED OPEN, partly informed. No paper tests a 1 to 9 rating. Closest: Kale 2026 shows pre-solve verbal confidence AUROC .50 to .77 vs .61 to .79 post-solve (d04); Cencerrado 2026 shows verbalised confidence loses to probes and nothing generalises to math (d03). New claim K27.
2. Gap 2 (ignore-irrelevant line plus pruning at equal tokens): PARTLY CLOSED. DNR Bench at a 1000-token cap: instruction line lifts R1 .00 to .76 and Claude-3.7 .40 to 1.00 on redundant items, o3-mini-high unchanged, and it hurts on one category (d08, d09). Not a GSM-IC-style distractor test; context pruning untested. K14 updated.
3. Gap 3 (tokens predict error on same items): CLOSED for math and science. Within-item, longer chains go with lower accuracy (Feng 2025, ten models; Ballon 2026, -3.16/-1.96/-0.81 points per 1000 tokens; DNR Bench). Slope shrinks with capability and failed-step fraction beats length (d05 to d07, d09). New claim K25.
4. Gap 4 (Hart and Staveland, DeLeeuw and Mayer numbers): STAYED OPEN. Only the NASA TLX manual was opened (design, no reliability numbers, weighting adds slight sensitivity; d14). DeLeeuw and Mayer full text blocked (403/HTML); only the Zu 2020 replication listing and the pattern (difficulty to intrinsic, effort to germane) recovered (d16).
5. Gap 5 (Skulmowski and Rey 2020, lab vs field): PARTLY CLOSED. No 2020 paper found; the 2017 mini-review reports mixed significance of TLX and the Paas item (d15). The "did not hold outside the lab" statement is a vote count, not a measured gap. Field-like data: Minkley 2021 N=309, HRV did not predict performance (d11); Zu 2021 shows structure depends on prior knowledge (d12).
6. Gap 6 (CogniLoad replication / decomposition at equal tokens): STAYED OPEN. No replication found (d17).
7. Gap 7 (CLT structures at matched tokens): CLOSED for multi-hop QA, negative. Tran and Kiela 2026: single agent matches or beats five multi-agent designs at equal thinking tokens (d10). K17 and K18 now contested. Math and instruction-following not tested there.
8. Gap 8 (model-internal load signal): PARTLY CLOSED. Probes beat length (Spearman .58 vs .30 at GPT-OSS low; routing at 70 percent lower cost) but degrade with reasoning effort and need hidden states (d01 to d03). New claim K26. Attention or logit entropy specifically: not found.
9. Gap 9 (germane budget vs two-factor model for LLMs): STAYED OPEN. No LLM source. Human side: two-factor structure appears at low prior knowledge (Zu 2021, d12), which weakly supports "indistinguishable for weak learners".
10. Gap 10 (Eysink-style negative GCL, effort predicting later learning): STAYED OPEN, one data point. Minkley: effort beta +.309 and load beta -.326 on performance (d11); no replication of Eysink.

Caveats: some table rows in d02, d04, d10 were garbled in text extraction and are marked as such. Skulmowski and Rey "2020" is not located. Authors of the Frontiers 702616 article were not extracted.
