# Critique: E18.10 Noise and judgement (cross-check)

## Corrections made (10 numbers re-opened in arXiv PDFs or NBER w23180 this session)
1. Zheng 2023: position consistency GPT-4 65.0, GPT-3.5 46.2, Claude-v1 23.8 (75.0% first-biased); few-shot GPT-4 65.0 to 77.5; GPT-4 vs human 85% vs human-human 81%. CONFIRMED. a16 says "over 80%", b16 gives 85/81. Both fine; prefer 85/81.
2. Wang 2023 (fair evaluators): 66/80 (82.5%) Vicuna wins with ChatGPT judge; GPT-4 judge 51.3% vs 23.8% by position; calibration 52.7% to 62.5% to 73.8%; +9.8%/+14.3%. CONFIRMED. Note a15 wording "66 of 80 = 82.5%" refers to ChatGPT as judge only.
3. Atil: up to 15% accuracy variation, up to 70% best-worst gap. CONFIRMED. Caveat in paper: hand-built answer extraction.
4. Sclar: 76 points (LLaMA-2-13B), ~10 average, median 7.5; GPT-3.5 56 / median 6.4 over 320 formats. CONFIRMED.
5. Self-consistency: +17.9/+11.0/+12.2/+6.4/+3.9. CONFIRMED (74.4 is PaLM-540B GSM8K, +17.9).
6. More Agents: GSM8K +12 to +24, MATH +6 to +10, Llama2-13B 59 vs 70B 54. CONFIRMED (c16 had no numbers; b23 supplies them).
7. Mixture-of-Agents: c18 says 65.1% (open-source MoA abstract); b25 says 65.8% (paper body: 65.8% with a GPT-4o aggregator). BOTH CORRECT, different configurations. Previous best 57.5%.
8. Schoenegger: LLM crowd Brier 0.20 (SD 0.12), t(30)=-2.35 p=.026 vs 0.25; vs humans 0.19, t(60)=0.19 p=.850; equivalence bound 0.081; mean forecast 57.35. CONFIRMED. a21 and b26 agree; a21 omitted that the 0.081 bound is wide.
9. Halawi: test Brier .179 vs crowd .149, accuracy 71.5 vs 77.0 CONFIRMED. Ablation crowd value is 0.160 on the ablation split (b27's 0.1600) and .146 in Table 5: two different splits, do not mix. Ensemble gain ~0.003 Brier.
10. Kleinberg: 758,027 defendants in full data; 554,689 is the NYC training/eval sample (80% = 443,751). a05 and b11 each cite one of these, not a conflict. 24.7%/41.8%, 13.0 points/18.7%, 6.3 points, 32.9%, AUC 0.707 all CONFIRMED in NBER w23180.
11. Stureborg Table 4 ordering was uncertain in a17/b15/c13. Appendix Table 7 gives human inter-annotator avg alpha 0.659 and GPT-4 inter-sample 0.587. Human higher: RESOLVED. The r = 0.979 vs 0.315 pair is also confirmed (multi-attribute anchoring).
12. Rating Roulette: alpha 0.3263/0.6278/0.7883 (SummaC), MT-Bench Llama 0.265, Qwen 61.3% identical on all 3 runs, human-human 0.827 accuracy/0.478 alpha, majority-of-3 61.4/72.3/80.6. CONFIRMED.

## Contradictions between sources
- Chiang and Lee 2023 (b29, LLM ratings stable and in line with experts) vs Stureborg 2024 and Rating Roulette (low self-agreement). Tasks, models and metrics differ; b29 had no numbers. Unresolved.
- Renze (a19): temperature does not change mean accuracy. Atil/Ouyang: run-to-run spread is large. Not a conflict: mean vs variance.
- Lau 2026: temp 0 cuts spread for GPT/Gemini but barely for Claude, Haiku completeness SD higher at temp 0. Rating Roulette: sampling off did not fix. Model-dependent, read from heatmaps.
- Danziger effect: contested (K04).

## Weak spots
- The human noise claims (K01, K04) rest on the Noise book via Wikipedia, never on the primary papers. Beam 1996, Aboraya 2006, Clancy 1981, Huffcutt 2013 figures are second-hand.
- Grove 2000 (136 studies), Goldberg 1970, Galton, Vul and Pashler 2008, the book's decision-hygiene chapter and the 2016 HBR paper were NOT opened. Numbers a06/a07/a24 are memory; do not cite.
- Many LLM numbers are 2022-2024 models (GPT-3.5, GPT-4, Llama-2). Only Lau 2026 and Rating Roulette cover newer judges; no Claude 4+/GPT-5-class result on prompt-format sensitivity.
- Seen only in abstracts/snippets: c09 to c20 (but the main numbers were later confirmed in PDFs above), Shi 2024 position bias (c11), Chiang and Lee (a26), Lau 2026 (figures only), the 85% vendor threshold (c24, blog snippet).
- Atil, Ouyang, Lau used different models and extraction; cause of non-determinism (batching) not isolated.
- Almost no study measures noise reduction at EQUAL TOKENS; self-consistency and More Agents gains are at k-times the cost.
- No source tests whether decision-hygiene steps (structured sub-judgments, delayed intuition) help an LLM.

## GAPS
1. At equal tokens, does sampling N short chains and voting beat one long chain (or one chain plus a verifier) for frontier reasoning models (2025-2026)? Self-consistency evidence is mostly 2022-2024 and at k-times cost.
2. How large is run-to-run and prompt-format noise on current frontier models (Claude 4/5-class, GPT-5-class)? Sclar/Atil figures are from older, mostly open models.
3. Does the Kahneman "mediating assessments protocol" (independent sub-judgments scored separately, holistic call last) reduce variance or raise accuracy for LLM judgments? No direct LLM test found.
4. Are errors of samples from one model correlated enough that diverse prompts or personas beat repeated sampling? Needs measured error correlation and the equal-token comparison.
5. Which verdict-style steps (pairwise, scoring, multiple choice) have the worst self-agreement in an agent loop, and does coded aggregation (both orders, permutations, median) recover accuracy at small cost?
6. Primary verification of Grove 2000 (46/48/6 split?), Goldberg 1970 and the Noise book audit numbers: is the "rules over judgment" effect size as large as claimed, and does it transfer to LLM judges versus coded rules?
7. Do noise audits of LLMs in real professional tasks (medicine, law, finance, insurance underwriting) exist, and what spread do they show relative to human professionals?
8. Is occasion noise in LLMs affected by context length or position in a long agent run (an analogue of the contested hungry-judge effect)?
9. What self-agreement threshold (the informal 85%) is justified, and how many samples are needed to reach a stable majority per item?
10. Is LLM-to-LLM noise reduction by averaging limited by shared bias (acquiescence, verbosity, order) in a way that coded debiasing cannot fix?

## Gap search results (evidence_d.jsonl, d01-d18; claims K19-K26 added, K18 upgraded, K11/K13 extended)
Search note: WebSearch quota was exhausted, OpenAlex and Semantic Scholar returned 429. All finds came from the arXiv listing pages and arXiv PDFs (opened with pdftotext) plus Europe PMC abstracts.

1. Equal-token vote vs long chain vs verifier: PARTLY CLOSED, stays open for frontier closed models. d01: sequential refinement beat parallel vote in 43/45 open-model configs at equal tokens (caveat: 4096-token cap, 30-item AIME). d02: debate and MoA beat self-consistency by 1.3-2.7 points at equal compute on Llama 3.1 70B. No test on Claude or GPT-5 with a verifier arm. K19, single-source.
2. Noise on current frontier models: PARTLY CLOSED. d07: GPT-5.2, Claude-Sonnet-4.6, Gemini-2.5-Pro as judges change 7-17% of verdicts across identical reruns at temperature 0. d10: floors 2.5-23.7% for six models. Prompt-format sensitivity (Sclar-style) on Claude 4/5 still not measured. K22, K24.
3. Mediating-assessments protocol on LLMs: OPEN. No direct test. Closest is d08 (FLASK decomposition did not beat holistic G-Eval), which is not the same protocol. K25 records this as a warning.
4. Diverse prompts vs repeated sampling: PARTLY CLOSED. d04, d05, d06 show errors are correlated across frontier models and diversity beats repetition, but across models, not across prompts or personas of one model. The equal-token prompt-diversity test is still missing. K21.
5. Worst verdict step and coded aggregation: PARTLY CLOSED. Pairwise is worst (d07, up to 98% flips on order swap); rubric scoring also flips top-1 on 15-41% of prompts via criterion order (d11); a few random orderings match full permutation (d11). Disagreement sits in near-tie pairs (d12). Accuracy recovered at what cost was not measured end to end. K22, K23, K26.
6. Grove, Goldberg, Noise-book numbers: PARTLY CLOSED. Grove abstract opened (d17): about 10% more accurate; mechanical substantially better in 33-47% of studies, clinical substantially better in 6-16%. The 46/48/6 split in the old K18 was wrong and is removed; the 136-study count is not in the abstract. Goldberg 1970 not opened; a 2016 meta-analysis (d18) supports the bootstrapping effect. Noise-book audit numbers (insurer 55%, etc.) still unopened. No LLM-versus-coded-rule test. K18 upgraded to established for the human result only.
7. LLM noise audits in professional tasks: PARTLY CLOSED. d10 is a clinical-agent audit (8.7% self-disagreement, synthetic vignettes, no human baseline). No law, finance or underwriting audit found; the insurance search was blocked by a 429 and was not retried.
8. Occasion noise vs context length or run position: OPEN. Two arXiv searches found no relevant study. Only indirect: d14 shows long reasoning chains amplify tiny numerical differences.
9. Self-agreement threshold and sample count: PARTLY CLOSED, negatively. d03 shows agreement is a weak signal (Spearman 0.20-0.59) and worst for the most consistent frontier model; d10 shows 5 draws remove only 39% (CI 18-64) of the floor; d12 shows a flat threshold is misleading. The 85% vendor rule has no support. K20, K26. No principled sample-size rule found.
10. Averaging limited by shared bias: CLOSED in the direction of yes. d03 (shared wrong answers with agreement 0.78-0.85 across GPT and Claude), d04 (cap of 1 minus all-wrong rate). Whether coded debiasing fixes acquiescence or verbosity is not tested; d09 says verbosity bias is now below 0.011 on 21 judges. K13, K20, K21.

Still-open list for the next pass: gap 3 (mediating protocol), gap 8 (context position), gap 4 for prompt/persona diversity at equal tokens, Goldberg 1970 and Noise-book primary numbers, a Claude-class equal-token vote vs long chain vs verifier test. All of 1-5 can be answered by a measurement on our own harness rather than more reading.
