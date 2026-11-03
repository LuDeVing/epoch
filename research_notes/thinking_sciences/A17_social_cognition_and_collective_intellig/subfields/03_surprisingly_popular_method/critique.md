# Critique and cross-check: Surprisingly popular method (A17.03)

## Corrections made (sources re-opened this session)
1. Prelec et al. 2017 (gwern PDF, text read): 21.3% (490 items), 35.8% / 24.2% (P=0.0107) / 22.2% (P<0.13) on 290 items, 48% on the capitals studies, 14% (P=.031) on trivia, 81% vs 22% of items with predictions in 40-60%, 40% power (392 of 1000), art-professional/MIT/trivia/state shares 19/29/56/36%: all CONFIRMED.
2. Ai et al. 2025 (arXiv 2510.01499) Table 3: the extraction shows rows 73.66 / 90.37 / 85.78 with MV 72.21 / 89.32 / 85.24. Entries b19 (UltraFeedback, MMLU, ARMMAN in that order) and c08 (which swaps MMLU and ARMMAN) disagree. Correct reading: MMLU 90.37 (OW), 90.01 (ISP), MV 89.32; ARMMAN 85.78, 85.78, MV 85.24. This matches the t-statistic order (12.53, 23.39, 3.22) and the eight-model table where MMLU > ARMMAN. c08 is WRONG on those two labels; b19 is right. Simulation numbers (85.13 / 79.94 / 91.37; 92.64 / 90.52 / 94.94; 95.54 / 94.40 / 96.81), 12.53 and 97.92% / 95.83% confirmed.
3. Consensus is Not Verification (arXiv 2603.06612): 375,000 responses confirmed. The table text extraction shifts model labels by one row; the values in c02-c05 (as assigned there) are consistent with the paper, but a reader of the raw PDF text would mis-assign them. The "2.9%" flip rate is of (question, model) pairs, not of "cases"; the 53% figure is MATH questions where several models err. The HLE set is only 35 questions with CIs of about +-14 points, so SP-vs-majority differences there (e.g. 25.4 vs 20.2) are inside noise.
4. Goel et al. 2023 (arXiv 2311.07692): text says the MaxRatio gain is 16 points for GPT-2 XL and LLaMA-2 13B and 24 points for "LLaMA-2 70B". The table (extracted, garbled) gives 7B 0.34 to 0.58 (+24) and 70B 0.37 to 0.58 (+21). So the paper's text and table disagree; b20 repeats the text, c10 the table. Safest wording: "up to about +24 points".
5. Rutchick et al. 2020 (PMC7658271): 52.8 / 53.9 / 55.6 / 51.4%, 60.2%, 67.3% (313), 62.0% (fivethirtyeight) CONFIRMED. a17 lists NFL media at 65.0% while the page shows "NFLpickwatch 62.3% (140.5), 65.0%" in a table row that mixes columns; treat the media figure as ambiguous.
6. Hosseini et al. 2021 (arXiv 2105.09386): random top-of-4 error 0.75 and "a third of the samples" confirmed in text.

## Contradictions between sources
- Human crowds vs LLM crowds: Prelec (21.3% gain) vs Rutchick (SP worst in football) vs Consensus-is-not-Verification (no consistent gain) vs Liu 2026 (BTS about 1 point worse than majority). Ai et al. report plain SP below majority in simulation (79.94 vs 85.13) yet a variant (ISP) above it. Reading: plain SP only wins when a minority holds correct private information and errors are diverse; LLM samples share errors.
- Goel (SP-like ratio helps, +24) vs Consensus (SP no help): different objects. Goel rescales one model's likelihoods over candidate completions; Consensus polls full samples from several models.
- Wilkening/Martinie meta-prediction weighting works but SP selection alone does not in many replications: the signal is better used as a weight than a selector.

## Weak spots
- Almost every positive human number traces to one paper (Prelec 2017) and its pooled sign test. The pooled 21.3% is driven by state-capital items (48%); trivia gave 14%.
- No independent large replication of the 21.3% figure exists in the evidence. Rutchick is a replication of the idea in a new domain, not of the same design.
- LLM studies are few, many are workshop or preprint level (Liu 2026, Consensus 2026, Mytsyk 2026), and several use small item sets (HLE 35, BoolQ 100).
- Ai et al. gains over majority are 0.5-1.5 points; practical value at equal tokens is untested.
- No study tested SP with a frontier reasoning model at equal token cost against majority/self-consistency.

## Seen only in snippets (not opened)
a21 Wilkening 2022, a22/b25 Palley and Soll 2019, a23 Prelec 2004 BTS, c14 MTS journal version, c19 Schoenegger 2024 (silicon crowd), c20 second-hand, c23 Generative Self-Aggregation listing. Claims depending on them are not used as support.

## GAPS
1. At equal tokens, does SP (answers plus predicted share) beat plain majority / self-consistency on the HTSA benchmarks with a current reasoning model?
2. How correlated are the scaffold's own sampled errors, and below what correlation does SP start to help?
3. Does SP help only when wrong answers are diverse? Test on items where the majority answer is a known shared misconception.
4. Is meta-prediction better used as a weight (extremised MPW, ISP) than as the SP selector for LLM samples?
5. Do LLM predictions of other samples' answer shares carry any signal beyond the sample's own vote (the Prelec 0.48-0.87 prediction-belief correlation)?
6. What is the independent replication status of the 21.3% figure, and what was the size of the effect outside capitals and art?
7. Do persona or model diversity restore the independence assumption enough for SP?
8. Can SP-style scores serve as a calibration or abstention signal (Liu 2026: ECE down 21-32%) even where accuracy does not improve?
9. How do SP and ISP behave with more than two options and open-ended answers (clustering needed)?
10. Are the Consensus-is-Not-Verification results robust to larger item sets and to reasoning-mode sampling?

## Gap search results (A17.03, evidence_d.jsonl d01-d19)
Limits of this run: arXiv, OpenAlex and Semantic Scholar APIs were rate-limited and the WebSearch budget ran out after two calls, so some gaps could only be answered from papers already in hand. Several pages were summarised by the fetch tool rather than read as raw text (noted in limits).

1. Equal-token SP vs majority with a reasoning model: STAYS OPEN. No study found (d15, d02). Consensus paper does not state reasoning mode; Ai et al. use one answer per model and no token comparison. New claim K23.
2. Correlation of the scaffold's own errors and the threshold for SP: PARTLY CLOSED. Across models, wrong-answer agreement is 0.42 to 0.60 against 0.12 to 0.33 by chance (d10); top wrong answer is 65 to 87% of errors on MATH (d04). No numeric cutoff exists; theory gives only the ordering ISP >= MV >= SP (d08). Needs our own measurement.
3. SP only when wrong answers are diverse: PARTLY CLOSED, indirect. Evidence is consistent (d04, d14) but no study built items with a known shared misconception.
4. Meta-prediction as weight vs selector: CLOSED in direction (d07, d06). Weighted and inverse-SP rules beat plain SP; gains over majority are small except on hard items (OW 24.79 vs 17.23 on MMLU-hard). Cost-matched value untested. ISP was top in only 12.5% of ensembles.
5. Signal in predicted shares beyond own vote: STAYS OPEN. Consensus elicits predictions (d03) but reports no coefficient; Ai et al. do not elicit them (d09).
6. Independent replication of 21.3%: STAYS OPEN, search incomplete (d19). Nothing found beyond Lee 2018 and Rutchick 2020. Effect outside capitals and art is still the 14% on trivia from Prelec's own paper.
7. Persona or model diversity: PARTLY CLOSED. Model mixing alone did not restore independence for SP (d05); diversity helps weighted forecasting (d11, d10). Personas untested (K26).
8. SP-style scores as calibration or abstention signal: STAYS OPEN. Only Liu 2026 (ECE down 21 to 32%) from earlier; Consensus says verbalised confidence tracks consensus nearly as much as correctness (d05), a warning.
9. More than two options and open-ended answers: PARTLY CLOSED. ISP edge shrinks about as 1/K and plain SP stays below majority up to K=10 (d06); open-ended answers and clustering are unhandled (d06, d12). K25.
10. Robustness of Consensus is Not Verification: STAYS OPEN. Still 35 to 100 items per benchmark, reasoning mode unstated, plurality flips 2.9% across temperature (d02). SP vs majority over 19 cells: 9 wins, 9 losses, 1 tie (d01).

Corrections noted: the Goel +24 point gain belongs to the 7B row; the 70B row is +21 (d12). The Consensus abstract says five benchmarks, the body four plus a control (d02).
New claims K19 to K27 added to claims.jsonl; K11, K13, K14 and K01 got extra evidence ids.
