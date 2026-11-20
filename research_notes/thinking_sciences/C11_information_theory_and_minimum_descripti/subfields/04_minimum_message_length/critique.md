# Critique: C11.04 Minimum message length (cross-check)

## Re-opened sources (10 key numbers)
PDFs fetched from arXiv, text extracted, then deleted. All checked numbers were confirmed.

1. Deletang et al. 2024 (2309.10668): ImageNet 43.4%, LibriSpeech 16.4%, PNG 58.5%, FLAC 30.3% confirmed. Table row: Chinchilla 70B raw enwik9 8.3, adjusted 21.9, ImageNet 185.3, LibriSpeech 228.9 confirmed. 38M transformer on gzip/LZMA2 data: 92.2% and 89.1% confirmed. The paper says prequential coding would charge less. CONFIRMED.
2. Huang et al. 2024 (2404.09937): Pearson -0.93, RMSE 3.1% (knowledge), about -0.95 per domain, 31 LLMs, 12 benchmarks, saturation at about 3M characters. CONFIRMED.
3. Blier and Ollivier 2018 (1802.07044): MNIST variational 24.1 kbits, ratio 0.12, 95.5%; CIFAR 89.0 kbits, 0.54, 61.6%; prequential MNIST 4.10 kbits, 0.021, 99.5%. CONFIRMED. Added from the table: prequential CIFAR10 45.3 kbits, ratio 0.27, 93.3% (b10 said "about 93%").
4. Voita and Titov 2020 (2003.12298): layer 0 accuracy 93.7 (linguistic) vs 96.3 (control); accuracy wrong in 8 of 10 settings, MDL always right. CONFIRMED.
5. Wu et al. 2023 (2212.10375): Random 42.78, TopK 58.14, TopK+LocalE 51.36, Majority 50.43, GlobalE 49.75, TopK+MDL 60.16. CONFIRMED. Note: the paper's 40.41% is the relative gain; 60.16/42.78 is +40.6%, a rounding gap only.
6. Hlavackova-Schindler et al. 2024 (2309.02027): F1 table MMLH 0.948, BIC 0.943, AIC 0.850, ADM4 0.773, MLE-ms 0.572. CONFIRMED. Observation: MMLH beats BIC by 0.005 with SD about 0.09, which is not a meaningful margin.
7. Elmoznino et al. 2025 (2410.14086): GPT-4 on Mastermind compared to a naive baseline and a meta-trained transformer is in the text. Exact values are in a figure, not read. Zero MML or Wallace hits in the text. CONFIRMED (qualitative).
8-10. Not re-opened (sources unavailable or rate limited): Dowe-Gardner-Oppy 2007 ESPE 0.1857 vs AIC 15.8055 (a10); Liao and Gu CompressARC 20% / 34.75% (c25); Lester et al. and Yoran et al. figures. These stay as agent-reported, uncorrected.

## Corrections made
- No numeric corrections were needed. Only additions: b10 CIFAR10 prequential figures (45.3 kbits, 93.3%); Wu relative-gain rounding.
- Status choices in claims.jsonl: Huang and Deletang were counted as separate agents (b/c) but are one paper each, so independent_sources counts papers, not agents. This lowers Huang's claim to single-source.

## Contradictions and tensions
- Blier and Ollivier table has an extra variational row (22.2 kbits, 98.2%) that the agents did not discuss. It is a different variational variant; the headline 24.1 kbits row is the one the text cites.
- MML vs MDL: sources disagree on framing (Dowe says MML is more efficient and consistent; Grunwald treats MDL as less assumption-bound) but give no head-to-head numbers. This is rhetoric, not data.
- Dowe's conjectures (a23) that only MML-like methods are both consistent and invariant are contested; no proof or independent test was seen.

## Weak spots
- The founding paper (Wallace and Boulton 1968), Wallace and Freeman 1987, and Baxter and Oliver 1995 were never opened (a01, a19, a33 are opened:false). Facts about them are second-hand.
- Almost every MML-versus-AIC result comes from MML's developers (Dowe, Gardner, Oppy 2007 is a draft with no reproduced tables for a11). No independent replication or failed replication was found.
- No LLM paper read actually uses MML. Related LLM evidence is about MDL, prequential or Kolmogorov coding, so transfer to MML is by lineage only.
- Wu et al. 2023 used GPT2-XL (1.5B) only; Voita used ELMo; Elmoznino's GPT-4 result is one task. No test on current frontier models at equal tokens.
- Wikipedia entries (a22, a27, a28, a31, b06, b07, c01) are secondary and were only read, not cross-validated.
- c26 and c27 are title-only (Crossref); no numbers. a34 and a19 were seen only as listings or reference entries (snippets).

## GAPS
1. Does choosing among sampled candidate answers by model-assigned code length (MDL rank, as in Wu et al.) beat majority vote or self-rating on a frontier LLM at equal tokens?
2. Does prequential scoring (how well earlier reasoning steps predict later ones) track correctness better than a two-part "explanation length plus residual" score in LLM reasoning traces?
3. Is there any independent replication (non-Monash) of MML beating AIC/BIC in order selection, and at what sample sizes does the gap vanish?
4. Does the shortest-rule tie-break help on ARC beyond frequency voting, given CompressARC's 20% eval pass@2 and the Kolmogorov Test's poor frontier results?
5. What does the original Wallace and Boulton 1968 paper report (data, class counts, bit thresholds of 10 bits)? Can the Snob significance thresholds be reused as a stop rule?
6. Does an LLM's stated precision in claims (the MML precision idea) correlate with calibration, and can penalising over-precise claims improve verbal confidence?
7. Where do MML and MDL actually disagree in practice (small samples, mixtures), with numbers from a head-to-head study?
8. How far can an agent compress its own memory (Lester et al. equal-info windows) before it stops being learnable or reusable by later steps?
9. Do 2020-2026 LLM papers use MML under another name (Wallace-Freeman, MML87, MMLD, "two-part code")? A targeted search of full texts is still needed.

## Gap search results

Search limits: the web search budget ran out after one call, and the Semantic Scholar, OpenAlex and arXiv API endpoints returned HTTP 429 all session. Work was done with arXiv listing pages, direct PDF fetches and one blog fetch. Evidence is in evidence_d.jsonl (d01 to d18).

1. Candidate ranking by code length vs majority vote on a frontier LLM: OPEN. Closest are MIDGARD (graph merge, gpt-3.5 and Code-Llama, about +2 points macro F1 over greedy, not majority vote; d06) and Wu et al. from the earlier round. No frontier-model equal-token test found (d14).
2. Prequential versus two-part scoring on reasoning traces: OPEN. Prequential tools exist (EDL, d09) but none was applied to reasoning traces (d18).
3. Independent MML versus AIC/BIC replication: OPEN. One independent MML versus MDL study found (d01); nothing against AIC/BIC; search was incomplete (d17).
4. Shortest-rule tie-break on ARC: PARTLY CLOSED. CompressARC 20% eval and 34.75% train confirmed (d04); MADIL about 7% (d05) show pure compression is weak as a solver. Tie-break against frequency vote still untested.
5. Wallace and Boulton 1968 details: OPEN. Paywalled; abstract only (d15). Snob thresholds cannot be reused.
6. Claim precision and calibration: OPEN. Zero listing hits (d18).
7. Where MML and MDL differ: CLOSED enough. d01 gives numbers: MML wins at 1 to 20 examples and on one-sided data, ties on balanced and noisy data. Single study, logic programs.
8. Limits of compressing agent memory: PARTLY CLOSED. RIMRULE (d07) shows MDL rule consolidation improves accuracy; ReuseRL (d08) shows pure length pressure backfires. Both on small or tool-use settings.
9. MML under another name in LLM papers: MOSTLY CLOSED. Two-part and Kolmogorov language appears (d10, d11) but no MML uses in LLM work; listing recall is imperfect (d13).

Claims changes: K19 extended, K20 gets d03, K21 to K27 added.
