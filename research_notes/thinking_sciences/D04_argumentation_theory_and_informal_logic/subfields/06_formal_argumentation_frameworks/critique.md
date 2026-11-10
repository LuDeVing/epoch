# Critique: D04.06 Formal argumentation frameworks (cross-check)

## Re-opened this session (full PDF text)
Cramer and Guillaume 2019 (1902.10552); Li et al. 2025 (2412.16725); Craandijk and Bex 2020 (2007.07629); Freedman et al. ArgLLMs (2405.02079); Ng et al. MArgE (2508.02584); Zhou et al. UQ (2510.02339); Zhu et al. ArgRAG (2508.20131).

## Confirmed
- Cramer and Guillaume: grounded 74.97, preferred 68.42, semi-stable 62.84, CF2 75.46, stage 62.79, stage2 68.36; 86.7% coherent responses, 49 of 61 participants; coherent grounded 82.79, preferred 75.17; t(5)=12.38; chance 33%; 61 undergraduates, mean age 20.8.
- Li et al. zero-shot grounded: Llama3-8B 0.18, Llama3-70B 0.37, Qwen2.5-7B 0.31, GPT-3.5 0.15, GPT-4o 0.54; SFT Qwen 0.97, Llama 0.95; CFP 1.00 after SFT.
- Craandijk and Bex: AGNN MCC 0.997 to 1.0; plain GCN 0.16 to 0.39; complete recall 0.41 before verification, 0.91 after.
- ArgLLMs Table 1: GPT-4o MedClaim direct 0.54, CoT 0.58, ArgLLM variants 0.51 to 0.53.
- MArgE: up to 8.4 points over debate, at most 2.6 worse; gains up to about 20% with stronger scorer; 3.5% and 1.0% over CoT on two datasets.
- UQ paper: 0.130 and 0.028 differences, 180 intervals, 74 significant, 44 direct, 24 LUQ, 6 Semantic Entropy; LUQ best 10 times.
- ArgRAG: PubHealth 0.838 / 0.670 / 0.647 / 0.898; RAGuard 0.768 / 0.804; GPT-4o-mini 0.840 / 0.855.

## Corrections
1. a10 says 0.5-base variants are "0.03 to 0.10" below CoT; Table 1 shows gaps up to 0.16 to 0.17 (Mixtral 0.56 vs 0.72). c02 range (0.03 to 0.17) is right. Use c02.
2. c02/a10 say estimated-base variants are within about 0.03 of CoT "in most cells". True for most, but not all (Gemma 2 9B 0.53 vs 0.61; Mixtral Truthful-type rows differ by up to 0.08). Claim K11 states this.
3. Li et al. 0.97/0.95 are SFT accuracy on the test set in the paper's main table; generalisation to above 25 arguments is lower (0.85 grounded for Qwen with full explanation). Do not quote 0.97 as general ability.
4. The ArgLLMs PDF fetched contained very long text; the Table 1 column layout is partly scrambled by pdftotext. Cell values quoted above were read by row order and are reliable for the rows checked, not for model-to-row assignment of every cell.
5. b01 and a05 duplicate the same source; they count as one source in independence tallies.

## Contradictions and weak spots
- Human data come from one study (61 students, small AFs, group discussion before the individual answer). Answers within a group are not independent. Grounded vs CF2 difference is not significant (p=.212). Rahwan et al. 2010 and Polberg and Hunter 2018 were never read, so there is no second source on human match.
- The ArgLLM family (Freedman, Zhou, Ng, Dejl, ART) is one research group; the "independent" count is mostly 1. Gains over CoT are absent or tiny at equal model; claimed gains come from contestability, not accuracy.
- Most ArgLLM work uses trees (acyclic), where grounded, preferred and stable coincide. It does not test Dung semantics on cyclic graphs at all. That is the central caveat for S7.
- Token cost is not equated in any LLM study read. Depth 2 uses about 7 LLM calls per claim vs 1 for CoT.
- Dung 1995 and Prakken 2010 were not opened (paywall); claims about them rest on the tutorial. Complexity classes are from memory.
- Several 2026 entries (a18, a19, a20, a22, c16 to c18) are recent arXiv preprints, not peer reviewed; a20 numbers are from a scrambled table.

## Only seen in snippets or abstracts
a07, a08, a23, a25, a26, c20 to c25, b22 (per-dataset numbers not extracted), b13 (demo, no numbers).

## GAPS
1. Does code-computed grounded survival (S7) beat plain CoT or majority voting at equal tokens on reasoning benchmarks, when the edges are LLM-judged? No study reports a token-matched test.
2. How accurate are LLM attack-edge judgements between candidate answers (not between debate claims)? Gorur et al. covers argument mining, not candidate solutions.
3. How often do candidate attack graphs from an LLM contain cycles, and does the semantics choice (grounded, preferred, CF2) change the survivor set in practice?
4. Do LLM-estimated base scores help or add noise relative to uniform scores, and are they calibrated (Brier/ECE)? Freedman et al. did not measure calibration.
5. Does attack-graph filtering help for open-ended or creative tasks (NoveltyBench-like), where "fails the test the other passes" is hard to define?
6. What do the unread human studies (Rahwan et al. 2010, Polberg and Hunter 2018) show, and do they agree with the 75% grounded match?
7. Order and position bias: how much does the order in which candidates are presented to the edge judge change the survivor set?
8. Is there any replication of Cramer and Guillaume with non-student participants or larger AFs?
9. What is the cost-benefit of ASPIC+-style structured arguments (undercut, preference) versus plain attack edges for a scaffold, with measured error rates?

## Gap search results
Evidence file: evidence_d.jsonl (d01 to d18). Claims K03, K04, K05, K25 revised; K26 to K36 added.

1. Token-matched test of grounded survival vs CoT or voting: STAYED OPEN. Nearest: ARGORA (d08) vs a compute-matched vote of 3 (trees, DF-QuAD, not Dung): MMLU-Pro 0.638 vs 0.618, MedQA equal 0.812. Choi et al. (d10): voting beats debate (0.7691 vs 0.7377 avg). The bar is voting.
2. Accuracy of LLM attack edges between candidate answers: STAYED OPEN. Only corpus-level relation tasks (ArgBench d15, mining 0.31 to 0.60) and human edge judgments (d01, d02: about 80% on good items, 17% to 44% for one-way direction).
3. Cycle rate in LLM candidate graphs and semantics effect: PARTLY CLOSED by simulation only (d17, random graphs; not measured LLM output). Cycles 25% to 56% at density 0.2; empty grounded 5.6% to 9.1%. MQArgEng (d07) falls back from grounded to preferred, which implies empty sets occur, but reports no rate.
4. LLM base scores vs uniform, calibration: PARTLY CLOSED. ARGORA ablation (d09): LLM scores better than 0.5 (MMLU-Pro 0.638 vs 0.618, GPQA 0.523 vs 0.419). Calibration still unmeasured (d12 says so explicitly).
5. Open-ended or creative tasks: STAYED OPEN. No attack-graph study. Adjacent: Creative-MAD (d14) shows debate lowers diversity.
6. Rahwan 2010 and Polberg and Hunter 2018: CLOSED in part. Polberg and Hunter read in full (d03): graded beliefs, AMT sample, no 75% grounded replication. Rahwan 2010 read as abstract only (d04) plus a 2024 replication abstract (d05). Both point away from grounded on floating reinstatement.
7. Order and position bias: PARTLY CLOSED for answer-quality judges (d11: pairwise consistency 0.57 to 0.82). Not measured for attack-edge labels.
8. Replication with non-students or larger AFs: STAYED OPEN for the 75% match. Only Polberg and Hunter used non-students, on a different task. The 2022 study (d01, 130 young adults) is the same lab and still students; no study used AFs above 6 arguments.
9. ASPIC+ cost-benefit: STAYED OPEN. No measured error rates; d12 reports 21% of graphs with a bad free-text scheme field.

Main new finding: K03/K04's "grounded is a good default" must be softened. The same lab's earlier and later studies (d01, d02) show grounded the worst predictor of human answers on floating reinstatement and 3-cycles (candidate ties). Not yet read in full: Rahwan 2010, the 2024 reinstatement paper (abstracts only). Table text in ARGORA and ArgBench was scrambled by pdftotext, so only rows named in the evidence lines are reliable.
