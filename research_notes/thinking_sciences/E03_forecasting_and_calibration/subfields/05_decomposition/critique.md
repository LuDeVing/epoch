# E03.05 Decomposition (Fermi-ize): critique

## Corrections made (10 numbers re-opened, text in D:/research_scratch/E03.05/)
1. MA94 19.78-fold median error cut (280 subjects, 1078 estimates), 68.3 pooled over nine extreme problems, 458% worse on non-extreme: CONFIRMED (ma94.txt lines 18, 180, 292, 349).
2. Bosse et al. 2026 (c01): Brier 0.141 [0.122,0.161] -> 0.132 [0.115,0.149], 94.4% of 10,000 bootstraps: CONFIRMED. Correction: source is Bosse, Muhlbacher, Wildman, Phillips, Schwarz (FutureSearch), arXiv 2601.22444, not "FutureSearch-style". The "500 questions" is a subset; the two CIs overlap heavily. Abstract names Gemini 3 Pro 0.134, GPT-5 0.149, Gemini 2.5 Flash 0.179; the extracted Table 2 is garbled (it shows 0.179 on a GPT-5 Mini row), so the model label for 0.179 is uncertain; trust the abstract.
3. Schoenegger et al. (b13): Fermi +.008, Event Decomposition +.007, Time Decomposition -.008, all adjusted p=.774: CONFIRMED. Added: Time Decomposition simple t-test -.013, p=.096 unadjusted (borderline, not significant). Event Decomposition second-test row p=.751.
4. Radhakrishnan (a18/b11/c22): CORRECTED. Table 4 "All Tasks (avg)" row prints CoT 87.0 and CoT-decomposition 88.0, factored 81.8, few-shot 79.7, zero-shot 72.8, while the Figure 1 labels give 86.0 and 85.6. The table text is garbled by extraction, so CoT vs CoT-decomposition order is uncertain. HotpotQA 77.0/77.0/83.0/86.7/87.3 confirmed. Factored decomposition is lower than CoT on every task except StrategyQA/HotpotQA tie-ish; TruthfulQA factored 75.3 vs CoT 91.0.
5. Halawi (a17/b10): Brier .179 vs crowd .149, random .25, GPT-4-1106 .208: CONFIRMED.
6. Zhou (a19/c08-c10): SCAN 99.7 vs 16.2, GSM8K 62.39 vs 60.87, 5+ steps 45.23 vs 39.07: CONFIRMED.
7. Press (a20/c11-c13): 42.9% ChatGPT, 23.0% GPT-4, 45.4% two-hop, 81.1% vs 42.6% perplexity bands: CONFIRMED.
8. Liu (a14): 0.398/0.420/0.418, 0.466/0.479/0.500, 0.439/0.469/0.460: CONFIRMED.
9. Epstein (a15): ~65% coverage at nominal 99%; GPT-4o-mini 0.63 at p=0.90: CONFIRMED (the 0.63 is at nominal 0.90, so the "0.63/0.59/0.64" list is by nominal level).
10. Paleka (c06): Cond 0.92 / 0.87 (first dataset), 0.71 / 0.69 (second): CONFIRMED.

## Contradictions
- b13 (prompt-only decomposition: no gain, n=100 questions) vs c01 (blind sub-forecast: small gain, Gemini 3 Pro). Differences: web research tools, blindness to parent, model, question set. Not resolved.
- a16/c04 say sub-question search helps; no ablation exists.
- Radhakrishnan: decomposition buys faithfulness, not accuracy; Zhou/Khot/Wu: it buys accuracy on long tasks. Different tasks and models.
- Press: compositionality gap shrinks with GPT-4 (23%) while gap was flat across GPT-3 sizes.

## Weak spots
- Human evidence is all 1975-1994, almanac quantities, one research group (Armstrong/MacGregor) plus a reanalysis; "extreme" cut-off is post hoc (they changed it from >7 to 7+ digits).
- Henrion et al. 1993 (a09) found no median accuracy effect; only seen via abstract and MA94.
- No human decomposition study on event probabilities (Brier), which is what our agent forecasts.
- LLM forecast decomposition: c01 is one model, 500 questions, overlapping CIs. b13 is 100 questions and 4 models of 2024 vintage.
- a22-a24 are syntheses, not sources. b17 (Chang 2016) was not reopened.
- Merrill et al. 2026 appeared in the scratch dir but concerns tail decomposition of pinball loss, unrelated.

## Only seen in snippets/abstracts
a08 (Ravinder 1988, abstract), a09 (Henrion 1993, abstract), a10 (book, not opened), b17 (not reopened), Khot exact EM values (figures), Dua table layout garbled.

## GAPS
1. Does decomposition improve Brier for a modern LLM on binary forecasting questions at equal tokens, once isolated from retrieval? (b13 vs c01 conflict; decisive for O3.)
2. What trigger (size, self-rated knowledge, answer spread across samples) reliably tells the agent when to decompose vs answer directly, given decomposition hurts familiar quantities?
3. Superforecaster decomposition data: Mellers/Tetlock evidence that decomposition (Fermi-ize) is a causal training ingredient, with effect size.
4. Does blindness of sub-forecasts to the parent question matter (c01 design) vs sub-forecasts made in context?
5. Do independent re-estimation or multiple samples per part reduce correlated-part-error compounding in LLMs (MA94 independence condition)?
6. Is a sub-question search step in Halawi-style pipelines worth its cost? Needs an ablation.
7. Does decomposition change LLM calibration (interval coverage), as it modestly did in humans (28.0 -> 23.6 points)?
8. How well do LLM-written decompositions on real Fermi sets score with strong 2025-2026 models (Kalyan fp_score above 0.5)?
9. Does a recomposition-consistency check (Paleka Cond laws) beat plain decomposition as a gate?
10. Is the Radhakrishnan CoT vs CoT-decomposition ordering as printed (87.0 vs 88.0) or in the figure (86.0 vs 85.6)?


## Gap search results

Search limits: the shared WebSearch quota ran out at the start, and the arXiv, Semantic Scholar and OpenAlex APIs returned rate-limit errors. Work was done by opening papers whose ids were known (new evidence in evidence_d.jsonl, d01-d19) and by Europe PMC. Some 2025-2026 papers will have been missed. Claims K22-K27 added; K02, K04, K06-K08, K10-K13, K18-K21 updated.

Closed
- Gap 10 (Radhakrishnan ordering): CoT 86.0 beats CoT-decomposition 85.6 by 0.4 (the text says 0.4). The 87.0/88.0 pair is a column misread. Fix a18, b11, c22. The HotpotQA "83.0 vs 87.3" line in K18 also needs re-checking (d06).
- Bosse label: 0.179 is Gemini 2.5 Flash (abstract page); the garbled Table 2 should not be used for labels (d02).
- Gap 3 (superforecaster evidence): closed negatively. Chang 2016 does not mention decomposition or Fermi; the training effect is 6-12% as a bundle (d10). A 2025 re-analysis weakens even the bundle (d11, abstract only). The Tetlock book was still not opened.

Partly answered
- Gap 1: still open. Bosse's gain (0.141 to 0.132) comes with extra GPT-5 research and no equal-token arm; the gain is in calibration (0.026 to 0.008) while refinement fell (d01, d02). Schoenegger's null (adj p .774) had no retrieval (d03). The two results are compatible: decomposition without evidence does nothing; with evidence it may correct calibration. No equal-compute test exists.
- Gap 2: the only tested trigger is decompose-on-failure (ADaPT, d14), plus a structure cue (numeric/symbolic, d15). Nothing is tested on forecasting questions. MA94 conditions (d09) give a checklist.
- Gap 4: indirect support for blindness from CoVe (d16); no numeric-forecast test.
- Gap 5: no test of part-level resampling. Self-consistency (d17) and ensemble results (d18) are indirect; ensembling hurt a plain GPT-4o (0.218 vs 0.210).
- Gap 9: the Cond gap is a good model-level diagnostic, but the patching forecaster gave no Brier gain (d05); not compared with decomposition.

Still open
- Gap 6: Halawi never ablated sub-question queries; the whole retrieval stack is worth about 0.02 Brier, which bounds it (d04).
- Gap 7: no study compares decomposed vs direct LLM intervals. Human deliberation stays overconfident (42% vs 10%, 68% vs 90%, d13); LLM 99% intervals cover 59-65% (d08).
- Gap 8: no 2025-2026 frontier score on Kalyan's set found; best remains 0.50 (GPT-4 Turbo, d07).

New finding: Barrera-Lemarchand et al. 2026 (Nature Communications) is the best new causal human test of Fermi decomposition: d=0.26 vs combining numbers, CI includes zero, group beats solo (d12).

Next experiments for us: (1) three-arm equal-token test on forecasting with retrieval (direct, extra research, blind subquestions); (2) a decompose-if-samples-disagree trigger; (3) a Kalyan fp_score run with our agent; (4) a sub-question line ablation in a Halawi-style query prompt.
