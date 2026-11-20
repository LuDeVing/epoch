# Critique: B03.01 Hierarchical predictive coding (cross-check)

## Numbers re-opened this session (full text or PDF)
Confirmed exactly:
1. Pinchetti 2025 (arXiv 2407.01163): VGG-5 CIFAR-10 PC-CE 86.61, BP-CE 88.11, centered nudging 89.47; VGG-9 78.12 vs 89.18; ResNet-18 43.19 vs 92.83, iPC 70.44; Tiny ImageNet 9.52 vs 58.00; first-layer energy about 6 orders lower at rate 0.01; 5.5 s vs 110 s per CIFAR-100 epoch.
2. ePC (arXiv 2505.20137): ResNet-18 CIFAR-10 92.17+-0.26 vs BP 92.36+-0.12; CIFAR-100 68.52 vs 69.94. Its "sPC 53.74" is the MSE column of Pinchetti, while 43.19 is the CE column (not a conflict).
3. Millidge 2020 (2006.04182): about 100x compute for the PC CNN, inference rate 0.1.
4. Lotter 2017 (1605.08104): MSE 0.0152/SSIM 0.937 vs 0.0180/0.907; 74% variance, 35% better than CNN-LSTM, 2.14 deg^2 at 25K.
5. Salvatori 2024 (2212.00720): masked LM 120.02 (BP, 7/10 converge), 523.08 (PC, 3/10), 106.19 (iPC, 10/10). Conditional LM: iPC 142.54 is WORSE than BP 113.32 and only 7/10 converged. Evidence b12 reported only the masked-LM win; this is a cherry-pick to avoid.
6. Pinchetti 2022 (2211.03481): 162.64 / 175.90 / 590.08. Row labels are lost in the text extraction; the order is inferred from the text (KL-PC beats Gaussian PC).
7. Caucheteux 2023 (PMC10038805): R=0.23 STS, 60% of noise ceiling, d=8 words (3.15 s), 23% +-9%, 304 listeners.
8. Antonello and Huth (PMC11025645): r=0.847 vs r=0.864, 97 representations.
9. Bhatt 2026 (2601.15652): AUROC 0.8017 / 0.8274 / 0.8669, N=200.
10. Xie 2026 (2604.03263): 12.630 vs 12.413 vs 15.127.
11. Ma 2024 (2410.17195): "around 60% of examples myopic", 76.5% of GSM8K errors myopic, +7.2% GSM8K, +25.3% AlfWorld, about 50% FLOPs.

## Corrections
- c01 says "70 min of stories". Wrong. The paper says 27 stories, 7 to 56 min each, 4.6 h unique stimulus (26 min average per participant). b15 is right.
- c10 / evidence says "76.5% of GSM8K errors myopic vs 57.3% for correct". The text only gives 76.5% for errors. The 57.3 is not confirmed as the correct-sample rate (57.3 also appears as Predictive-Decoding's table score). Treat the 57.3 as unverified.
- c09: "+4.95%" is the paper's own figure for 0.8274 to 0.8669; arithmetic gives +3.95 points or +4.8% relative. The paper also says "stacked 0.8414 (+5%)" elsewhere. The gain figure is loosely stated.
- a14 notes 20 inference steps on MNIST for Whittington and Bogacz; not re-opened.

## Contradictions and tensions
- Salvatori 2024 shows iPC beating BP in masked LM but losing in conditional LM; Pinchetti 2025 shows iPC best only on small nets. "iPC fixes it" is not general.
- c14 (LPC-SM) finds the predictive-coding block did not help base loss, while c09 finds PC-style signals help detection. Different uses, both single preprints.
- Caucheteux (forecasting evidence) vs Antonello and Huth (transfer explains the same data equally). Unresolved.
- Walsh 2020 says a significant contingent of expectation studies failed to replicate; Millidge says adaptation explains the same data. Both reviews agree the process theory is not cleanly confirmed.

## Weak spots
- Original founding sources were NOT opened: Mumford 1992 (a01), Rao and Ballard 1999 (a03, b21: abstract or memory only), Murray 2004 (a05), Kok 2012 (b22), Summerfield 2008 (a07 via review), Kaliukhovich and Vogels 2011 (a08 via Walsh). Founding exact numbers are therefore missing.
- b25, b26, b27, c25 (Keller, Feuerriegel, Alink and Blank, Barenholtz) were snippet or memory only. Claims that depend on them are marked contested, not established.
- c20 and c21 (HTTP 403 / login). Use b17 and b15 instead.
- Most "evidence" for K06 to K08 is relayed through two reviews (Walsh, Millidge), so independence is partly illusory.
- The Caucheteux evidence lines a20, a21, b15, c01 are one study repeated four times.
- No LLM study was found that implements a PC scaffold for reasoning. c19 (a search of 50 arXiv results) found only small 2025-2026 preprints; all with small N or single seeds.
- The relevance to our agent is background only; the nearest operational idea is residual-only passing (K09) and foresight reweighting (K17), neither of which is PC-specific.

## GAPS
1. Does passing only the residual (delta between a draft and critic, not the whole draft) beat full re-reading at equal tokens in a scaffold loop? (No LLM study found.)
2. Does foresight resampling (Ma 2024) hold on non-math tasks and against best-of-N at equal tokens? Only GSM8K, MATH, AlfWorld seen.
3. Does a surprise-against-context signal (Bhatt 2026) detect hallucinations at N well above 200 and on other benchmarks, with CIs?
4. What do Rao and Ballard 1999 and Murray 2004 actually report in numbers (receptive fields, endstopping, V1/LOC effects)? Primary texts unread.
5. Where is the independent replication of Kok 2012 sharpening, and does Alink and Blank 2021 explain expectation suppression by attention?
6. Is there a multi-level (more than two level) test in language models that separates syntax, semantics and discourse prediction errors (beyond Heilbron 2022, Caucheteux 2023)?
7. Do the Feuerriegel 2021 review conclusions on expectation suppression hold up after 2021 (any pre-registered replications)?
8. Does the 2025-2026 PC-for-transformers line (Pinchetti 2022, Innocenti 2025) scale past 100M parameters, or is it settled that it does not?
9. Can a PC-style step (prediction, residual, update) be implemented as an operator in a prompt loop, and is the effect separable from simple self-refinement baselines?
10. Antonello and Huth versus Caucheteux: is there a test that separates forecast-specific from transfer-general brain alignment?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d18). Search tools were limited: the shared WebSearch budget ran out after 3 calls, and arXiv, Semantic Scholar and OpenAlex were rate limited. Europe PMC and direct arXiv PDF fetches worked.

1. Residual-only passing vs full re-read: STAYS OPEN. No study found. Closest: Olausson 2024 (equal-budget self-repair 0.97x to 1.05x; feedback quality is the bottleneck) and Huang 2024 (intrinsic self-correction lowers GSM8K 75.9 to 74.7). New claims K20, K21.
2. Foresight resampling beyond math: PARTLY CLOSED. Ma 2024 also tests HumanEval (57.3 vs 44.3 plain, 53.5 beam), MBPP, AlfWorld, PDDL. Still no non-verifiable tasks, and the edge over equal-budget self-consistency is only about 0.4 points in the readable row (tables garbled in text extraction). K17 updated.
3. Surprise-against-context detection at larger N: STAYS OPEN. Full text of Bhatt 2026 read: n=200, no CIs, no second benchmark, AUROC vs accuracy comparison with Lynx. K15 updated.
4. Rao and Ballard 1999, Murray (the V1/LOC paper is 2002, not 2004): STAYS OPEN for numbers. Only abstracts were reachable (paywalled or scanned). Do not quote their methods numbers.
5. Kok 2012 replication and Alink and Blank 2021: PARTLY CLOSED. No close independent replication of sharpening found; Alink and Blank list four studies with better decoding for unexpected stimuli (relayed, not opened), and Rideaux 2026 (preprint) favours dampening. Alink and Blank is a perspective piece with no data; its attention case rests on Richter and de Lange 2019 (N=34, interaction F=7.7 to 17.0). Attention is an open rival, not shown to explain suppression (predictive coding can absorb it via precision). K13, K24.
6. Multi-level (3+) language test: STAYS OPEN. Heilbron 2022 re-opened (EEG N=19, MEG N=3; syntax category, phonemes, semantics, no discourse). Nothing newer found, but search coverage was poor.
7. Feuerriegel 2021 after 2021: PARTLY CLOSED. Abstract: genuine suppression mainly after weeks of learning. Post-2021 items found: Yan 2023 (N=34, suppression only for whole learned displays in LOC), Rideaux 2026 preprint. No pre-registered direct replication found. K06 updated.
8. PC for transformers past 100M parameters: STAYS OPEN, leaning no. muPC reaches 128 layers on simple classification; no LM result. K22.
9. PC-style step as operator, separable from self-refinement: STAYS OPEN. No direct test; null baselines (K20) show the bar: beat self-consistency at equal calls with an external signal.
10. Antonello and Huth vs Caucheteux: STAYS OPEN. PMC text fetch for Antonello and Huth returned empty this session; no discriminating test found.

Corrections to earlier lines: none needed beyond those listed in the critique above. Bhatt "+4.95%" re-confirmed as the paper's own figure (arithmetic +3.95 points).
