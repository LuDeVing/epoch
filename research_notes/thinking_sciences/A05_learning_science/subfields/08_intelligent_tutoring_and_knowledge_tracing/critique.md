# Critique and cross-check: A05.08 Intelligent tutoring and knowledge tracing

## Re-opened this session (texts in D:/research_scratch/A05.08/)
Confirmed against the paper text:
1. Khajah et al. (2016): 31.6% of the DKT-BKT gap from biased AUC for BKT; another 50.6% gone when BKT gets forgetting; classic BKT 0.73, BKT+F 0.83 on ASSISTments; Statics BKT+FSA 0.75 vs DKT 0.76; Spanish 0.846 vs 0.836; Synthetic BKT 0.80 vs reported DKT 0.75. All match (a03, b01-b03).
2. Wilson et al. (2016): duplicate rows about 25% of ASSISTments rows; KDD 3,679,198 interactions after preprocessing. Match (b04, b05).
3. Worden et al. (2026): baseline 51.3%; GPT-OSS-120B 56.2%/0.559; Llama-3.3-70B 52.3%/0.512; 85.4% vs 12.6%; N=27,715. Match (c01, c02).
4. Hooshyar et al. (2025): DKT AUC 0.83, zero-shot 0.69, fine-tuned 0.77. Match (c06).
5. Bhattacharyya et al. (2026): 72.8 / 72.7 / 71.8 accuracy; Gemini 128 s, Qwen 3,299 s; 600-12,000x. Match (c08, c09).
6. Norris et al. (2025): 90.32 AUC full text, 84.59 with tags. Match (c11, c12).
7. Kestin et al. (2025): N=194, 4.5 (N=142) vs 3.5 (N=174), 0.73-1.3 SD quantile effect. Match (a16, b13, c24). The 0.63 figure was not re-grepped.
8. Scarlatos et al. (LAK25) and Lee et al. (LKT) tables: see corrections.

## Corrections
- c13 (LKT) mislabelled table rows. In the LKT table, DKT on XES3G5M-T is AUC 0.8480 (ACC 0.8407), SAKT 0.7852, AKT 0.8207, DKVMN 0.8513, DeBERTa-v3 0.8468 (ERNIE 0.8508). So "DKT 0.7852" and "DeBERTa 0.8513" in c13 are wrong; a11 and b17 are right. LKT therefore ties DKT on the large set, rather than beating it by about 7 points.
- b19 (Scarlatos v1 numbers) mislabels columns. In the LAK25 table: CoMTA BKT 52.50, DKT 53.20, DKT-Sem 61.82, LLMKT 65.79; MathDial LLMKT 76.71 and the next-best (DKT-Sem) 66.18. b19's "LLMKT 61.82 / 66.18" belong to the DKT-Sem baseline. Use c19. The row was garbled in text extraction, so DKT-Sem values are approximate.
- "+20.0% on Synthetic" (a03, b03) is a relative number; in AUC it is 0.05.
- a02, a21-a24, a26, b22-b28 were never opened. K14, K15, K16 rest on recalled values.

## Contradictions between sources
- DKT on Eedi: 71.8% accuracy (Bhattacharyya) vs AUC 72.37 (Norris). Different metrics and splits, not a direct conflict. But Norris's 90.32 is far above anything in the other Eedi paper; the two cannot be compared directly.
- LLM tracing is "better" (NTKT, CLST, CIKT, Scarlatos) or "worse" (Worden, Hooshyar, Bhattacharyya, LKT small set) depending on fine-tuning, use of item text, and baseline. K07 is marked contested.
- Kestin (large positive) vs Pardos and Bhandari (negative for ChatGPT hints) vs Bastani (harm without guardrails): differences in model, prompt design, outcome timing and population (Harvard undergraduates, MTurk adults, high school).

## Weak spots
- LLM-KT papers use ASSISTments or Eedi with different splits; AUC is not comparable across papers.
- The 2015-2016 DKT story shows baselines and leaks drive results. The same may hold for 2024-2026 LLM-KT claims (CIKT, NTKT), each from one group.
- The learning RCTs (Kestin, Bastani, Tutor CoPilot) test tutors, not knowledge tracing. Nothing shows a better student model causes better learning.
- Nothing tests knowledge tracing on an LLM agent's own per-skill competence. All transfer is by analogy.
- Seen only in snippets: Eedi blog (c10), systematic review abstract (a15).
- Schwonke 2009, Pane 2014, VanLehn 2011 could not be verified: OpenAlex searches returned only related abstracts (Salden et al. 2009: adaptive fading gives higher delayed transfer; Koedinger et al. 1997: 470 students, 15% better on standardized tests, 100% on objective-targeted tests).

## GAPS
1. Does a tracked per-skill competence estimate (count-based or logistic) for the agent's own sub-skills improve routing or stopping at equal tokens versus no tracker? No direct study found.
2. Do LLM tracers with item text beat a logistic regression with recency features (not just DKT) on the same split? No paper has run this.
3. Can the LLM optimistic bias (85.4% vs 12.6%) be removed by calibration or a verifier, and does it map to the agent's weak detection of its own errors?
4. Do the Norris (90.32 AUC) and CIKT gains replicate by independent groups on other data, with pyKT-style leakage checks?
5. What are Schwonke et al. (2009) exact numbers (N, time saved, procedural and conceptual scores)? Open the paper.
6. Pane et al. (2014) effect sizes by year and school level, and VanLehn (2011) d values: verify from source.
7. How sensitive are outcomes to the mastery threshold (0.95) and BKT non-identifiability?
8. Does the guardrail effect (own step before help; Kestin, Bastani) hold for non-math tasks and for delayed tests?
9. Does tracing in open dialogue scale (MathDial 76.71 AUC) with noisy LLM labels, and what does label noise cost?

## Gap search results
Tool limits this session: OpenAlex budget exhausted, Semantic Scholar and arXiv API returned 429, and the shared web search budget was used up. Work used direct arXiv PDFs, Europe PMC, ERIC API (abstracts), Crossref and an own simulation. Evidence is in evidence_d.jsonl (d01-d23). Publisher full texts (Pane, VanLehn, Schwonke) were blocked.

1. Tracker for the agent's own sub-skills, routing or stopping at equal tokens: STAYS OPEN. No direct study. Indirect: a per-question average gets 66.5% on Eedi against 71.8-72.8% for DKT and LLM tracers (d13), so a count-based tracker likely captures most of the signal (new claim K20).
2. LLM tracer vs logistic with recency: STAYS OPEN. NTKT baselines were DKT, AKT, AKT-text and DTransformer only (d14). Claim K21.
3. Optimistic bias: PARTLY CLOSED. Bias is model-specific (Qwen3-Instruct 56.5 vs 51.0) and a shifted threshold (0.8789 vs 0.5782 for DKT) or fine-tuning (low-performer recall 20% to 64%) reduces it; AUC remains weak. No verifier tested (d11, d12; K06 updated).
4. Replication of NTKT/CIKT: STAYS OPEN. No independent replication found; leakage should be small on single-skill Eedi-type data (under 1 AUC point in pyKT) so it does not explain the gap (d14-d16; K22).
5. Schwonke 2009 numbers: STAYS OPEN. Paper paywalled. Correction: evidence b28 has the wrong DOI (it is an animation-speed paper); right one is 10.1016/j.chb.2008.12.011. Related abstracts only (d10; K15 reworded).
6. Pane and VanLehn: PARTLY CLOSED at abstract level. Pane: none in year 1, +0.21 SD high school year 2, middle school not significant. VanLehn: human 0.79, ITS 0.76. The answer-based 0.31 and per-year per-level effect sizes remain unverified. Extra meta-analyses added (Ma 2014, Kulik 2016, Steenbergen-Hu 2013, 2026 K-12). K14 now established, with that caveat (d01-d07).
7. Threshold and identifiability: CLOSED, with a correction. BKT is identifiable under mild conditions; the true issue is semantic degeneracy (d08). Own simulation: with a correct model near-best fits move the 0.95 pass point by about one attempt, and 74% of them pass a C,C,I,C,C window (d09). K16 rewritten and marked contested.
8. Guardrail effect beyond maths and delayed tests: PARTLY CLOSED. Coding (Lehmann, d19), concept learning with delayed follow-up (ChatTutor, d20) and a child reading RCT (d21) point the same way. Correction: Bastani's GPT Tutor removed harm but gave no positive unaided gain (d18). Still thin: abstracts only for d20, d21.
9. Dialogue tracing with noisy LLM labels: PARTLY OPEN. Label accuracy is measured (75.82% vs human 85.56%; over 90% positive labels) but no study measured the cost of noise (d17; K23).

Not verified this session: d01-d07, d20, d21, d23 are abstracts only (opened:false). d09 is my own simulation, not literature.
