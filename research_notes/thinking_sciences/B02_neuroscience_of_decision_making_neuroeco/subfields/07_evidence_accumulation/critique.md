# B02.07 Evidence accumulation: cross-check critique

## Re-opened numbers (10+), result
1. Ratcliff and McKoon 2008 Table 1 (PMC2474742): Exp 2 boundary a = 0.109 (speed) vs 0.152 (accuracy); median RT effect 120-200 ms. CONFIRMED (a02, b01).
2. Hawkins et al. 2015 (PMC6605613): 72 of 85 humans fixed, 9 collapsing, 4 inconclusive; monkeys 4 collapsing, 2 fixed, 2 urgency; >116,000 decisions; replication 91 humans, 64 very strong plus 12 strong for fixed. CONFIRMED. Without between-trial variability 6 of 8 monkeys prefer fixed. CONFIRMED (b08).
3. Roitman and Shadlen 2002 (PMC6758024): RT 824.0 ms at 0 percent coherence (monkey T1 choice); pre-saccade rate 68.6 +/- 0.9 spikes/s. CONFIRMED.
4. Hanks, Kiani, Shadlen 2014 (PMC4054775): RT elongation 176 +/- 4 and 159 +/- 3 ms; excursion 43 +/- 2 percent smaller under speed. CONFIRMED. CORRECTION: the 43 percent hides a large split between animals (monkey D 58 percent, monkey E 23 percent). a10 should carry this.
5. Aggarwal et al. 2023 (arXiv 2305.11860): MATH 73.2 vs 73.1, 40 vs 13.8 samples, 3.3x, -0.1; up to 7.9x, average drop under 0.1 percent. CONFIRMED (abstract and Table).
6. Li et al. 2024 ESC (arXiv 2401.10480): -33.8/-80.1/-76.8/-78.5/-84.2/-67.4 percent confirmed in abstract. Table check: GPT-4 GSM8K 7.98 samples (40 minus 32.02), 89.29 unchanged; GPT-3.5 GSM8K 14.65 samples, 85.67 (-0.02) vs SC at same N 84.82 (-0.85); GPT-4 MATH 42.4 of 64, 60.32 unchanged; Llama-2 7B MATH 62.48 (-1.52). CONFIRMED. The pdf text layout is scrambled, so assigning 7.98 to GPT-4 relies on arithmetic and the 89.29 match.
7. DeepConf (arXiv 2508.15260): 99.9 percent (AIME 2025, GPT-OSS-120B, 512 traces) vs 97.0 majority vs 91.8 pass@1; tokens -84.7 percent. CONFIRMED. Warm-up threshold step confirmed in the method text.
8. ConSol (arXiv 2503.17587): AIME24 o3-mini-low 70.0 to 80.0; token cuts 84.8 (AIME24 o3-mini-medium) and 86.2 (GPQA Diamond o3-mini-low). CONFIRMED. Note: the table shows SC@40 at 70.0 for the 70-to-80 case, so the gain is probably from sampling past 40 on uncertain items; the paper says "beyond the accuracy of Self-Consistency of 40 samples".
9. Arthur 2026 (arXiv 2609.01867): partial r 0.552, 0.41, 0.229; 0.41 to 0.55 with multi-path decoding; 0.22 at high temperature; item accuracy r 0.668. CONFIRMED.
10. Vats 2026 (arXiv 2610.24649): ratio 1.19 (1.02-1.36), 73.0 vs 73.0, AUROC 0.78/0.62/0.60, 0.50 predicted vs 87 percent passed. CONFIRMED. Also: controller cheaper than small LLM (0.81) but 22 percent dearer than a placebo.
11. Abstract-level only: CISC (40+ percent), DSC (65.29/56.04; 24.81/21.86), DEER (19.1-80.1 percent, +0.3 to +5.0) confirmed in abstract; the DSC abstract does not state the percentages, so these come from the earlier agents' full-text reading and were not re-checked.

No numeric corrections needed beyond item 4.

## Duplicates that are not independent
- a17, b13, c01 are the same Aggarwal paper; a19, b15, c05, c06, c07 the same ESC paper; a11, b07, b08 the same Hawkins paper; a01, b01-b03 the same Ratcliff paper; a22, b20, c18 the same DEER paper; a20, b16, c08 the same DSC paper. Claims count independent sources, not lines.
- b26, c26, c27, a24, a25 are syntheses, not evidence.

## Contradictions and tensions
- Fixed vs collapsing bound: humans mostly fixed (Hawkins, Ratcliff 2016 review), monkeys mostly collapsing, and optimal-policy theory (Drugowitsch 2012) says collapse under mixed difficulty. Unresolved; depends on model variability terms and practice.
- LLM stopping rules (adaptive threshold) outperform a fixed N, but the human data say a fixed bound is fine for humans. These are not in conflict: LLM difficulty varies across items while human blocks mixed one difficulty per cue; the b26 note is an analogy only.
- ESC says savings are large on easy sets and small on MATH; DSC claims further savings through priors; they are measured on different model versions.
- Tokens vs samples: Adaptive-Consistency counts samples, DeepConf and ConSol count tokens, DEER counts chain length. Savings percentages are not comparable.

## Weak spots
- Many LLM numbers are on 2022-2023 models (GPT-3.5, code-davinci, Vicuna). Few tests on current reasoning models except DeepConf, DEER, ConSol, Liu and Wang.
- Independence assumption: only one source notes it (a25 is a synthesis, no measured confident-wrong rate was found).
- Hawkins and Ratcliff both rely on diffusion fits; Hato 2025 shows boundary estimates shift with misspecification (R2 .77).
- Most monkey and neural findings (Roitman, Kiani, Hanks) come from 2-4 animals.
- Thinker-DDM (c21) works on translation and did not help commonsense translation by default; weak support for DDM-style decoding.
- Vats (c24) tested one controller on 21 tasks; a null on pass rate, so not evidence that stopping rules fail in general.
- No accuracy-at-equal-tokens comparison between a stopping rule and a verifier-based rule exists in the evidence.

## Seen only in snippets or abstracts (opened:false or not re-opened)
Ratcliff 1978, Wald 1945, Gold and Shadlen 2007 (403), Palmer 2005, Bogacz 2006, Usher and McClelland 2001, Brown and Heathcote 2008, Voskuilen 2016, Evans and Wagenmakers 2020. DSC's "3.8 percent" and the Wang 2023 self-consistency gains were read only in abstract form by agent a (b12 and c04 opened them).

## GAPS
1. Does a sequential agreement bound hold up on current reasoning models (o3-class, 2025-2026) at equal tokens when samples are long chains, and where does the bound fail on hard items? (Few tests: DeepConf, ConSol.)
2. How often does the agreement bound stop on a consistent wrong answer (confident-wrong rate), and does diversifying prompts between samples lower it? No measured rate was found.
3. Is a fixed or a collapsing/cap-limited bound better for LLM agents when item difficulty is mixed? Humans say fixed, theory says collapse; no LLM test.
4. Does a verifier-based bound (tests pass) beat an agreement bound at equal tokens, and by how much, on code and maths?
5. Which difficulty signal is cheapest and best for setting the starting bound (first-two-sample agreement, trace length, confidence)? DSC, CISC, Arthur use different ones; no head-to-head.
6. Do stop rules transfer to open-ended or non-verifiable tasks (writing, planning, research) where answers cannot be matched exactly? All evidence is closed-answer.
7. Does a stopping controller inside an agent loop (not parallel samples) help? Vats found cost up and no pass-rate gain; are there other tests with other controllers or models?
8. Do human-style speed-accuracy instructions ("be careful" vs "be fast") move the effective bound in an LLM as they move boundary a in the diffusion model, and at what token cost per accuracy point?
9. How do the Gold and Shadlen 2007 review and the Ratcliff 1978 founding paper define the bound and the log-likelihood-ratio reading, to check that our Beta/SPRT mapping is faithful? (Not opened this session.)

## Gap search results

Search tools: WebSearch quota ran out after the first call; Semantic Scholar, OpenAlex and arXiv search returned 429. I worked from known arXiv ids, Europe PMC and PMC. New evidence is in evidence_d.jsonl (d01-d20, 18 opened); claims K19-K27 added and K07, K09, K10, K12, K13, K06 extended.

1. Gap 1 (reasoning models, long chains): PARTLY CLOSED. DeepConf (d01, d02) shows the 0.95 agreement stop holds on DeepSeek-8B, Qwen3-32B and GPT-OSS-120B at cap 512 (18-85 percent fewer tokens, accuracy within about 1 point for the conservative variant). It fails in places (Qwen3-8B AIME25 -4.4 points) and needs a 16-trace warmup. Still no test on o3-class closed models and no equal-token comparison on the very hardest items.
2. Gap 2 (confident-wrong rate): STILL OPEN. No source reports a rate. Structural evidence only: consensus is wrong when the right answer is rare (Brown d03, Zhao d05), fixed-N voting gets worse on hard items (Chen d07). Mixed prompt styles separate easy from hard better (Yue d13), the only support for varying prompts.
3. Gap 3 (fixed vs collapsing bound for LLMs): STILL OPEN. Theory (d18) and the hard-item penalty (d07) point to a cap or item-specific bound; no LLM test.
4. Gap 4 (verifier vs agreement): PARTLY CLOSED. At equal sample count the verifier wins (d03, d05: MATH 467 vs 460 of 500, AIME 8 vs 4 of 15, LiveBench Reasoning 97 vs 75 of 140). Not equal tokens (50 verification calls per sample). Verifier stops have false positives of their own (d04: best K about 5 at ratio 4).
5. Gap 5 (best difficulty signal): STILL OPEN. Difficulty-based allocation is supported (d06 up to 4x, d13 40 percent cost), but no head-to-head of first-two agreement, trace length and confidence.
6. Gap 6 (open-ended tasks): MOSTLY OPEN. Universal self-consistency (d14) works as a selector for summaries and free-form QA but gives no confidence, so no stop bound exists there.
7. Gap 7 (in-loop controller): STILL OPEN. Only Vats (d15, not re-opened beyond the abstract). Absence is limited by the search quota.
8. Gap 8 (careful vs fast): STILL OPEN as posed. Proxies exist (Chain of Draft d11, TALE d10, s1 budget forcing d09) showing prompts move chain length with measured accuracy; none maps to a diffusion boundary or gives cost per accuracy point.
9. Gap 9 (definitions): PARTLY CLOSED. Gold and Shadlen 2007 and Ratcliff 1978 were not opened (paywalled). Shadlen and Kiani 2013 (d18) and Ratcliff and McKoon 2008 (d19) say: SPRT accumulates logLR to bounds; flat bounds are optimal only with known stationary reliability; the diffusion boundary is in evidence units, not defined as logLR. So our Beta/SPRT mapping is a heuristic reading, not the original definition; add a cap.
