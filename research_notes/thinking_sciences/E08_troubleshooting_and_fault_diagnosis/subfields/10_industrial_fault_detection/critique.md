# Critique: Industrial fault detection (E08.10)

## Corrections and confirmations (sources re-opened this session from arXiv PDFs)
Confirmed as written: Kim 2026 (64.67 / 77.43 / 83.33 / 92.76; 140 of 295 missed; 15 of 99 lost; CI -12.0 to -0.7), Gao 2024 (PCA 5.70% on fault 3; AE-FENet 98.66%; 97.55/97.55/96.05), Peng 2017 (fault 3 missed rates 92.0/93.8/96.4/98.4; NCA best in 11, KPCA 7, AE 5, PCA 4), Zhou and Zhu 2023 Table 4 (OEFB 93.9/84.4/91.5), FaultExplainer (GPT-4o 7, o1-preview 9 faults), Chain of Physics (51.98, 50.61, 68.80; 1,314 questions; expert mean about 60%, best 66.19), Hartung 2023 (TCN-S2S-AE 0.9699, Dense-AE 0.9632, Untrained-LSTM-AE 0.9335 rank 9), Kim 2022 (Kendall 0.07 and 0.43; Pearson -0.59 and 0.41), SigLLM (135%, +14.6% vs MAvg, -10.9% vs ARIMA), CoffeeBench (one model over 60%, over 97% longer, over 24% soundness).

Corrections and cautions:
1. Gao 2024 has two figures for plain FENet: Table says average 79.05% (0 layers) in one table, while the text says plain FENet averages 85.73%. Items a12 and b08 therefore disagree (79.05 vs 85.73). Cause not resolved; probably different tables or settings (a table also shows 69.70% in another column block). Treat as "79 to 86%".
2. Peng 2017: wins "11 + 7 + 5 + 4 = 27" exceeds 21 faults. The counts probably pool T2 and SPE statistics across 21 faults, so "best in 11 of 21 faults" (a06) is wrong. Read it as "11 of the compared cases".
3. Zhou and Zhu Table 4 is garbled in text extraction. Row order was reconstructed: SCVA, SAP, OE, OEFB, KF s=0/10/20. a10 values are consistent with that reconstruction; SCVA column (16.3, 11.7, 25.5) was not recorded.
4. Kim 2026 states seven models; one sensitivity analysis used four of them. Do not quote "seven models" for every number.
5. a05 and c23 and b23 (Downs and Vogel) were never opened; numbers come via secondary papers.

## Contradictions between sources
- Detection of faults 3, 9, 15: PCA 3-8% (Gao), 92-98% missed (Peng, consistent), DAE 3.6-7.9% (Xiao), versus 94-98% for AE-FENet. The gap is protocol (window 150 and 2000/2000 split vs 960-sample runs), not a real disagreement.
- TEP near-saturated (Hartung 0.97, Pal 99.9% accuracy) vs only 80-90% in adversarial or SensorSCAN settings. Benchmark variants and metrics differ.
- LLM benefit: FaultExplainer and Chain of Physics show gains with structure; Kim 2026 and Lee 2025 show LLM plus tool at or below the tool. Not strictly contradictory: gains are measured against an unaided LLM, losses against the specialist.

## Weak spots
- Almost all numbers are on the simulated Tennessee Eastman process. Few real-plant validations (Gopaluni survey says so).
- LLM results are mostly single studies with small items (S2S-FDD about 13 items per model; FaultExplainer 11 faults; Lee 2025). No replication of any LLM result.
- Method papers are self-reported (SensorSCAN, AE-FENet, LGF-MLTG, NCA).
- Boonmee 2024 reports two different overall accuracies (85% and 91%) with a placeholder dataset size.
- No token-matched comparison of LLM versus classical detector exists in this evidence.

## Seen only in snippets or not opened
a20, a21, a22 (Peng 2021, Kovalenko 2022, Gravanis 2026), a23 and a24 (search summaries), b23, b24, b25 (cited only; b25 is the same paper as c05, which was opened), b26, c22, c23.

## GAPS
1. Does an LLM given the same compute as a statistical detector plus LLM explainer detect incipient faults (3, 9, 15) better, equal or worse, at equal tokens?
2. Does explicit arbitration (Kim 2026) fix the missed-correction rate, or is a trained selector needed? Replication on a non-TEP set.
3. Which TEP protocol should we adopt (window, train/test split, threshold) so results are comparable, given the 3-8% vs 97% spread?
4. Are the LLM gains from Chain of Physics and FaultExplainer reproducible on real plant data (not simulation or question banks)?
5. How do LLM agents perform on detection delay (time-to-flag), not only accuracy?
6. Do LLMs reading raw numeric windows ever beat a trivial baseline (always-no-fault, moving average) on real industrial series?
7. What is the false-alarm cost of LLM-driven detection at fixed hit rate (no paper reports it)?
8. How does diagnosis accuracy drift over repeated fault cycles and with sensor perturbation (Lee 2025, Pozdnyakov 2024), and does a memory or reset operator help?
9. Why do faults 5 and 10 (and 13) fail for every LLM even with a cause list, and does adding control-loop knowledge fix it?

## Gap search results
Evidence in evidence_d.jsonl (d01-d17). Search budget: 1 WebSearch used (second refused, session budget spent); arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, so papers were found via the one search and via the Kim 2026 reference list. Several 2026 arXiv ids come from that list and were opened as PDFs.

1. Equal-token LLM vs statistical detector on faults 3, 9, 15: STAYED OPEN. No paper compares at equal tokens. New: AgentRCA costs 4,615 tokens, 5 tool calls, 51 s per window (d06) and says it is not a detector; its TEP top-1 is 40.0% (d05). Kim 2026 does not use faults 3 or 9.
2. Does explicit arbitration fix missed corrections: ANSWERED NO for prompt-level arbitration (d01): explicit instruction 76.1% vs 77.4% implicit; harmful acceptances 15 to 6 of 99 but missed corrections 140 to 161 of 295; stored-answer variant 72.2%; random forest specialist same gap. Trained selector and non-TEP replication of the TEP result remain untested (bearing sets show the same pattern, d02).
3. Which TEP protocol: STAYED OPEN, but characterised (d15, K25). LLM studies use incompatible subsets. Recommendation: fix window, split and threshold once and report the incipient set 3, 9, 15 plus 5, 10, 13, with a trivial baseline (d10).
4. Real-plant reproducibility of Chain of Physics and FaultExplainer gains: STAYED OPEN. Partial: AgentRCA on a real rig PRONTO 87.6% top-1 (d04) and survey confirms simulation-level validation (d13). Real-data checks are tiny (Lam 9600, 23 judgments).
5. Detection delay: STAYED OPEN, confirmed as a gap (d08, K24). Alhazmi uses a fixed modelled latency.
6. LLMs on raw windows vs trivial baseline: PARTLY CLOSED. Zhou and Yu (d09): isolation forest beats LLMs on F1, no evidence for subtle anomalies. Wu and Keogh (d10): 86.1% of Yahoo series solved by a one-liner. Nobody tested an LLM against always-normal or moving-std on real industrial series.
7. False-alarm cost at fixed hit rate: PARTLY CLOSED. Kim Appendix M (d03): specialist 56.0% normal-to-fault, unaided LLM 4.6%, integrated 9.7% on 25 normal runs. Not at fixed hit rate, closed-set, post hoc.
8. Drift over repeated fault cycles and memory/reset: STAYED OPEN. Nothing new opened (Lee 2025 only second-hand, d16). One new related failure: revising away from a correct first diagnosis (d08).
9. Why faults 5, 10, 13 fail for every LLM: STAYED OPEN. FailureSensorIQ (d11) shows weak sensor knowledge in general and AgentRCA ablations (d14) show retrieval helps top-1, but no run on faults 5 and 10 with control-loop knowledge. Kim's set has IDV13 but not 5 or 10.

Corrections to earlier notes: Kim 2026 used seven models for the primary analysis; the high-effort check used four (already noted). Alhazmi diagnosis is from a closed 12-item vocabulary, so the 15 of 15 is not open detection. Cause of the Gao 79 vs 86% mismatch (item 1 above) not resolved here.
New sources not fully verified: d16 and d17 are second-hand (opened:false). Not reached: Liang and Sin 2026, KDACL (Yang 2026b), LAPSE MCP agent paper.
