# Surprisingly popular method: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A17.03-U1 | Does plain SP (answer plus predicted share) beat majority or self-consistency at equal tokens with a current model? | SP as S7 selector for closed-answer items | S7 | K11 contested (9 wins, 9 losses, 1 tie); K21 simulation has SP below MV; K23 no reasoning-model test | Arms: majority of N; SP with N/2 answers + N/2 predictions; single sample. 300+ closed-answer items, 2 models. Paired sign test on accuracy | SP beats majority by 1.0+ points, p<0.05, on both models, prediction tokens counted | Med |
| A17.03-U2 | Does the prediction residual (actual minus predicted share) of a sample carry signal beyond its own vote? | Residual as a feature in S7 | S7 | K24 single-source: predictions mirror votes; no coefficient reported (d03) | Log (answer, predicted share) for 300+ items. Offline: AUC of residual for correctness, controlling for vote share | AUC gain 0.03+ over vote share alone, 95% CI above 0 | High |
| A17.03-U3 | Is meta-prediction better as a weight (extremised MPW) than as the SP selector for LLM samples? | Weighted vote in S7 | S7 | K09 single-source, human (+6.64); K22 single-source, LLM (small gains) | Majority vs MPW vs SP on the same samples, 300+ items, report by difficulty tertile | MPW beats majority by 1.0+ points overall or 3+ on the hard tertile, p<0.05 | Med |
| A17.03-U4 | Does ISP/OW from answer co-occurrence beat majority for our model mix? | ISP/OW weights learned from S9 history | S7, S9 | K13 single-source: +0.5 to +1.5, hard items up to +7.5; best single model beat ISP on MMLU | 3+ models or prompt families; train/test split of items; majority vs ISP vs OW vs best single | Beats majority by 1.0+ points on held-out items and beats the best single model | Med |
| A17.03-U5 | At what error correlation does any second-order rule start to help? | A class-level switch: majority below a correlation level, weights above | S0 gate, S9 | K20 established (agreement 0.42-0.60 across pools); no cutoff known | Compute wrong-answer agreement and top-wrong share per item class; plot SP and ISP gain over majority against it | A threshold exists with a gain of 1.0+ points on one side, replicated on a second half of items | High |
| A17.03-U6 | Does SP help only where wrong answers are diverse, and fail on shared misconceptions? | Rule: SP or weights allowed only when top-wrong share is low | G4, S0 | K11, K12 indirect (d04, d14); no built test | Items with a known common wrong answer vs items with scattered wrong answers; majority, SP, verifier | SP gain over majority is positive on the diverse-error set and absent on the misconception set, difference 2+ points | Med |
| A17.03-U7 | Can an SP-style score serve as a calibration or abstain signal even if accuracy does not improve? | Score as a confidence input for G1 and the impasse detector | G1, S6 | K15 single-source: ECE down 21-32%; d05 warns verbal confidence tracks consensus | Stated confidence vs agreement share vs SP score; ECE and AUROC on 300+ items | AUROC beats agreement share by 0.03+ or ECE falls 20%+ | Med |
| A17.03-U8 | Do persona or prompt-family differences restore enough independence for SP or weights? | Prompt-family diversity in S3 for closed items | S3, G4 | K26 single-source; model mixing did not restore independence (d05); personas untested; G4 currently bans persona voters | Same N samples from one prompt vs 3 prompt families vs 3 models; wrong-answer agreement and accuracy of majority and SP | Agreement drops 0.10+ and majority or SP gains 1.0+ points | Low |
| A17.03-U9 | Does likelihood-ratio rescoring (p(a given q) over p(a given generic prompt)) help with current models? | Rescoring on closed candidate lists | S7 | K14 single-source; 2023 base models, TruthfulQA; COPA 70B flat | Raw vs ratio vs CoT majority on TruthfulQA-style and our multiple-choice items, models with logprobs | Ratio beats raw likelihood by 3+ points and matches majority at lower tokens | Low |
| A17.03-U10 | Does a second pass that sees the tally help, or only cause conformity? | Optional tally-aware second pass | S7 | K27 single-source; R1 0.56 to 0.88, GPT-4o flat; conflicts with G4 and G9 | Independent vote vs tally-aware revote; accuracy and wrong flips to the majority | Accuracy +2 points with wrong-flip rate under 5% on two models | Low |
| A17.03-U11 | Does SP-rank help for ranking or multi-option outputs in LLMs? | Top-k plus predicted top-k aggregation | S7 | K10 established in humans only (one research group) | Ordering items with measurable truth; Borda vs SP-rank, equal tokens; Kendall tau distance | Distance falls 10%+ vs Borda, p<0.05 | Low |
| A17.03-U12 | Can SP-type rules work on open-ended answers (clustering)? | Cluster-then-score pipeline | S7 | K25 single-source: no study handles it | Cluster open answers by normalised form; compare vote over clusters vs SP over clusters | Clustering error under 5% and the SP gain rule of U1 met | Low |

## Open questions we cannot test on our bench yet

- Reasoning-model SP at equal tokens: the bench needs token metering per call, prediction call separate. Unblock by logging tokens per call in harness/bench.py.
- Independent replication of the 21.3%: needs human crowd data. Unblock with the SP-Rank dataset (a15) or a public replication if one appears.
- Items with a known shared misconception: no ready set. Unblock by mining the bench for items where plain accuracy is below chance and the top wrong answer is stable.
- Quality of a model's guess about "other models": does it carry knowledge? Unblock by comparing predicted shares with shares measured from 50+ real samples of other models.
- Open-ended answers: needs a clustering step with a known error rate before any vote rule can be judged.
- Learned aggregators (K16): need labelled history. Unblock by accumulating S9 records over several batches.

## Order to run

1. A17.03-U5 (error correlation and its threshold): cheap, offline from samples we already take, and it decides whether U1 to U4 can ever work.
2. A17.03-U2 (prediction residual signal): one extra call per sample plus an offline analysis. It tells us whether predicted shares carry any information beyond the vote.
3. A17.03-U1 (equal-token SP vs majority): the main open experiment (K23). Run it after U2 so the prediction format is known to be usable.
