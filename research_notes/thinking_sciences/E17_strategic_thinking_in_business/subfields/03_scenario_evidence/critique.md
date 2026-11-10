# E17.03 Scenario evidence: cross-check critique

## Corrections made
Sources re-opened: Phadnis 2015 PDF, Csaszar 2026, Elbaum 2025, Halawi 2024, Business Arena 2026, KWBench 2026.

Confirmed unchanged: Phadnis 343 pairs / 189 changed (55.1%), chi2=5.65 p=0.13; Study II 285 pairs / 198 (69.5%), confidence 0.811 vs 0.814 p=0.979; 404 pairs / 288 (71.3%); 62.9% and 68.6% shifts; Study III 351 pairs, 65.2% to 50.1%, 12.3% to 23.1%, 7.4% to 11.4% p=0.056. Csaszar 0.74/0.45/0.19/0.04, p=0.063, 870 comparisons, 346 managers, 18.9% random, Prolific 85%. Elbaum -38/-48/-28/-57%, 6.37 to 4.61 and 2.76, additions under 50 words on about 1800. Halawi Brier .179/.149/.208, 71.5 vs 77.0. Business Arena $20,856-$188,488, 51%, $436,195 (2.3x best mean). KWBench 27.9%, 31.7%, 50.7%, 223.

Clarifications:
- a02 mixes designs: Study I 343 pairs / chi2 is the multi-scenario test (Posttest B); a05's Study I 419 pairs / 234 changed is the single-scenario test (Posttest A). Different comparisons, not a conflict.
- Study II has both 285 pairs (multi-scenario, forced yes/no) and 404 pairs (single-scenario). a03 and a04 should say which.
- Phadnis says Studies I and II gave similar results and presents Study II only for the useful/wasteful result.
- XFinBench "12.5% for human experts" typo was not rechecked.

## Contradictions
- Confidence: Schoemaker 1993 (wider ranges) vs Kuhn and Sniezek 1996 (more confident) vs Phadnis (no change). Only Phadnis was read.
- Number of scenarios: about 3 (Wikipedia rule), 2-3 (Shell), 8 vs 4 (Strategy Science, secondary).
- More samples help in DeLLMa but K=3 hurt in K-Level reasoning: not monotone.
- Csaszar: crowd correlation 0.19 (near random) but value capture 85%.

## Weak spots
- No study links scenario use to firm performance with a control. Performance papers (Phelps, Rohrbeck, Zanin, Gokmen) not read in detail.
- de Geus follow-through claim and Diffenbach 68% rest on Wikipedia and HBR excerpts.
- Phadnis has no control group, experts unaccountable, one-shot use.
- Wargame and escalation LLM studies concern escalation, not scenario quality; relevance is indirect.
- Meissner and Wulf 2013, Chermack studies, Healey and Hodgkinson never read: the best direct human tests.

## Snippet-only
a08, a09, a17-a20, a23-a24, a27-a28, b06, b08-b10, b23, b26, c21-c25.

## GAPS
1. Does an LLM scenario operator beat a no-scenario arm at equal tokens on calibration (Brier, interval hit rate)? No study exists.
2. What do Meissner and Wulf 2013 and Schoemaker 1993 report with controls (anchoring, overconfidence, interval width)?
3. What does the Strategy Science 2026 AI-augmented foresight experiment (348 participants) actually find?
4. Do Phelps 2001, Rohrbeck and Kum 2018 and Zanin 2021 show causal performance effects, with what effect sizes?
5. Original Diffenbach 1983 and later adoption surveys: what do they say about use and satisfaction?
6. How many scenarios maximise decision quality (2-3 vs more), in humans and in LLM sampling?
7. Is there any measured version of de Geus' follow-through finding (implementation rate with and without scenarios)?
8. Do LLM-generated scenarios differ in diversity and plausibility from human ones (Kozachek 2026, Spaniol and Rowland 2023 numbers)?
9. Does naming the actor bias LLM scenarios as in CFPD, and does a scaffold remove it?
10. George, Walker, Monster 2019 meta-analysis: effect size and moderators for planning and performance.

## Gap search results
Budget notes: 8 WebSearch calls used; the arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429 for most calls; ScienceDirect, Emerald, MDPI, INFORMS and EBSCO pages returned 403. New evidence is in evidence_d.jsonl (d01-d19).

Closed or mostly closed:
- Gap 10 (George, Walker, Monster 2019): CLOSED. Opened the paper. r=.229 (95% CI .186-.271), 87 correlations from 31 studies, I2=91.6%; r=.255 with one effect per study. Participatory planning weaker; multi-source data lowers effects; Egger test signals publication bias, Begg does not. (d01, d02)
- Gap 4 (performance effects): PARTLY closed. Rohrbeck and Kum 2018 opened: 83 firms (70 profitability, 42 market cap), vigilant firms 63% of outperformers vs 24% of underperformers, profitability 16% vs 12% industry, market cap growth 75% vs 25%; no significance tests; cross-sectional 2008 sign reversed. Phelps 2001 still unread (blocked); Zanin 2021 stays as in b05. (d03, d04, d15)
- Gap 1 (LLM scenario arm vs no-scenario on calibration): PARTLY closed. Schoenegger et al. 2025 tested a hypothetical-scenario prompt: -0.007 Brier, adjusted p=.774. No effect on calibration from a one-prompt scenario step. No multi-step scenario operator at equal tokens has been tested. (d05, d06)
- Gap 3 (Strategy Science 348 participants): IDENTIFIED but not opened in full. Kanis, Mann, Stumpf-Wollersheim 2026: startup evaluation, 2x2, LLM use widened breadth, cut depth and consensus, no accuracy change. It is not a scenario-planning experiment. (d08)
- Gap 2 (Meissner and Wulf 2013): PARTLY closed. Abstract read: N=252 graduate students, framing bias (not anchoring) reduced and decision quality better than traditional tools. No cell numbers. Schoemaker 1993 not reached. (d09)
- Gap 8 (Spaniol and Rowland): CLOSED as a negative: opinion piece, no numbers. Kozachek 2026 stayed unread, so diversity and plausibility numbers are still missing. (d10, d11, d12)

Stayed open:
- Gap 5: Diffenbach 1983 text not obtained (catalogue record only). Klein and Linneman snippet gives about 150 of the Fortune 1000 using multiple scenarios. No satisfaction data found. (d13, d14)
- Gap 6: no experiment on the number of scenarios found. (d19)
- Gap 7: no measured implementation-rate version of de Geus found. (d18)
- Gap 9: no study of a scaffold removing the actor-name bias. (d19)
- Also open: Schoemaker 1993 and Kuhn and Sniezek 1996 numbers; Phelps 2001 sample and effect sizes.

Corrections to earlier lines: b07's 'almost 9,000 organisations' was not found in the paper text; the paper reports 31 studies and 87 correlations. Meissner and Wulf tested framing bias, not anchoring.

Claims changes: K06 set to contested with new numbers; K08 raised to established (effect size known); K07, K20, K21 reworded; K22-K26 added (K26 is the open list).
