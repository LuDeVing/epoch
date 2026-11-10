# Critique: E03.06 Aggregation and extremizing (cross-check)

## Numbers re-opened this session (full PDF text)
1. Satopaa, Pemantle, Ungar 2015 (arXiv 1406.2148): extremized aggregate Brier 0.123, reliability 0.020, resolution 0.049, uncertainty 0.152. CONFIRMED (a06/b03).
2. Satopaa and Ungar 2015 (arXiv 1506.06405): fitted factor 1.6950; extremized loss 133.23; best single model 185.74. CONFIRMED. **CORRECTION: b01 says "extremized 155.69 vs 185.74". 155.69 is the plain mean (a11 is right). Extremized is 133.23.**
3. Halawi et al. 2024 ensemble table (Table 14): mean 0.1656, median 0.1651, geo 0.1655, trimmed 0.1649, USC 0.1691, none 0.1676, crowd 0.1600. CONFIRMED. Added caveat: their "trimmed mean" is nonstandard (halves the weight of the one forecast furthest from the median; only 6 forecasts). These are validation numbers; test Brier is 0.179 vs crowd 0.149.
4. Halawi test Brier 0.149 crowd (text seen); the 0.179 / 0.146 values were taken from earlier lines, not re-seen in full.
5. Schoenegger 2024 Study 1: LLM crowd 0.20 (SD 0.12), t(30)=-2.35, p=0.026; human 0.19 (SD 0.19), t(60)=0.19, p=0.850. CONFIRMED.
6. Schoenegger Study 2: GPT-4 0.17 to 0.14 after seeing human median; machine-human average GPT-4 0.13 t(92)=2.58, Claude 2 0.14 t(92)=3.53. CONFIRMED. Note: the paper also reports a pooled improvement 0.22 to 0.15 (p<0.001) for another set; "17% to 28%" accuracy is a different summary.
7. Neyman and Roughgarden (arXiv 2111.03153): averaging ratio 0.706 tight; 0.760 with prior; extremized guarantee about 2.598/k (that is 3 sqrt3 / 2 over k); factor tops out near sqrt3 = 1.732. CONFIRMED.
Not re-opened: ForecastBench tables (0.197/0.194), AIA Forecaster (0.1076, sqrt3, 2.27), Lu 2025, Hsieh 2024, Turtel 2025, Prophet Arena. arXiv search by title did not return AIA or Hsieh, so their numbers stay single-read.

## Contradictions and tensions
- b01 vs a11 (above). Fix b01.
- Schoenegger: a28 gives mean-of-medians 0.52/0.41/0.55 (outlier included); c08 gives 0.11/0.28/0.15 (outlier dropped). Different datasets of the same study, not a conflict, but must not be mixed.
- Single-model GPT-4 Brier: 0.15 (c02, b11) vs 0.075 calibration index (a22). Different measures; do not compare.
- ForecastBench (a26): ensemble 0.197 is worse than best single model 0.178. Halawi: ensembling helps within one system. So gains depend on whether samples come from one strong model or a mixed pool. Contested.
- Platt/extremizing helps in AIA (c15) but isotonic/binning did not help in Halawi (c07); the two systems differ.
- Source SCHEMA says extremizing is controversial. Evidence: in theory it is justified only when information is diverse and forecasts are calibrated; with correlated samples the factor is near 1 or below. Support for G4 holds.

## Weak spots
- Baron et al. 2014, Mellers 2014, Satopaa 2014 (a16, a17, b19-b21), Ranjan-Gneiting, Lichtendahl 2022, Palley-Soll, Sevilla were never opened. The founding GJP numbers are therefore second-hand (via Satopaa 2015). Large hole for a "founding studies" brief.
- Only one real-data extremizing result (GJP supers, 123 events, 23 positives) is first-hand; small.
- AIA coefficient evidence comes from one team's benchmark, no replication.
- No test of extremizing LLM sample ensembles against equal-token baselines exists in the evidence.
- Evidence a30/c20 etc. (self-consistency) are reasoning tasks, not probability forecasting.

## GAPS
1. Does extremizing the mean of K same-model LLM forecasts improve Brier at equal tokens, and what is the fitted slope by shared-context level? (Core test for G4.)
2. What did Baron et al. 2014 report: exact extremizing factors, the two stated reasons, and Brier gains in GJP year 1-2?
3. What is the Mellers/Satopaa 2014 GJP effect (percent Brier reduction from extremizing, by team size)?
4. What is the measured error correlation between samples from one LLM on forecasting questions, and how does it change with temperature, prompt variation or retrieval differences?
5. Does the AIA Platt/sqrt(3) result replicate on another benchmark or model (ForecastBench, Prophet Arena)?
6. When should the factor drop below 1 (anti-extremizing; Lichtendahl 2022 conditions) and can the agent detect that online?
7. How does acquiescence (yes) bias interact with extremizing; does debiasing first help?
8. Are there failed replications of extremizing in human data (e.g., Palley-Soll shared-information results, Sevilla critique), and what boundary conditions did they find?
9. Does a model-based merge (supervisor/USC) beat numeric mean when samples differ by evidence rather than by noise?
10. Does extremizing hurt near 0/1 where LLMs are already overconfident (Halawi tails: accuracy up, Brier worse)?

## Gap search results (evidence_d.jsonl d01-d21; claims K19-K27 added)
Search budget: WebSearch ran out; Semantic Scholar, OpenAlex and the arXiv API were rate limited. Sources came from direct PDF fetches.

1. **Partly closed (still no equal-token test).** AIA (d10, d11): 10 same-model samples, mean 0.1140; fixed sqrt3 push 0.1076 (-5.6%). BLF (d14): logit mean gives only a small gain; Platt gain not resolved (d15). Turtel (d18): median of 5 from a base model gains 0.0079, less than a trained single pass. Nobody compares push vs more samples at equal tokens, and no slope was reported by shared-context level.
2. **Closed.** Baron et al. 2014 opened (d01, d02): two reasons (bounded-scale noise; forecasters regress for missing information). Year-1 GJP fitted a = 2.43 / 1.78 (experts, mean / median) and 3.08 / 2.34 (non-experts); Brier gains 9-29%, in-sample.
3. **Partly closed.** Mellers 2014 could not be parsed (d20) and Mellers 2015 has no extremizing (d21). Instead Powell 2022 (d03) gives a first-hand out-of-sample figure on all GJP: Brier 0.098 to 0.061 (-38%). Breakdown by team size is still open; BIN (d05, d06) shows teams and superforecasters gain little from push.
4. **Partly closed.** Between-model correlation is measured (0.943 on football, d17; JS divergences on Metaculus, d16). Within-model error correlation by temperature, prompt variation or retrieval is still unmeasured. OPEN for the exact question.
5. **Open, leaning contested.** BLF (d15) found no resolved Platt gain on its Pro backbone and small gains on Kimi. No run on Prophet Arena or ForecastBench with a push.
6. **Partly closed.** Conditions from Lichtendahl (d08, d09): shared information lowers the push, and the ensemble pulled toward the base rate in about 20% of cases on same-data ML models. Online detection: nothing found; BLF dispersion shrinkage was never selected. OPEN.
7. **Open.** No LLM study of yes bias x push. Human GK data (d04) fit an intercept with the slope; AIA says LLMs hedge toward 0.5 (d13).
8. **Mostly open.** Palley-Soll PDF blocked (d19, snippet only). Sevilla not found. Boundary conditions found: partial beats full push (d03, d04), per-question negative optimal a (d01), wrong-side forecasts are pushed the wrong way (d11).
9. **Partly closed, contested.** AIA agentic supervisor 0.1125 vs non-agentic 0.1168 vs none 0.1199 (d12); BLF found an LLM merge worse than a mean (d14). Model merge helps only when it adds searched evidence. No test where samples differ by evidence versus noise.
10. **Partly closed.** AIA (d11): gains come from the 0.2-0.4 and 0.6-0.8 bins; near 0/1 gain is mechanically tiny (0.995 to 0.999 moves Brier 2.4e-5). Halawi tail loss from earlier evidence stands. Clip and cap.

Corrections found while reading: d11 table text was garbled in the PDF extraction, so its row mapping is a best reading; AIA Table 9 mean 0.1140 and Table 10 'none' 0.1199 are different bases.
