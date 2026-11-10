# Critique and cross-check: D05.04 Assessment and tests

Checked against the full PDF text (re-opened this session): LogiQA, GPT-4 report, Hagendorff et al., Friedman et al., AGIEval, Logic-LM, ReClor, Liu et al. 2023, Bangert-Drowns and Bankert, CCTST Technical Report 1, and the Sebokova PMC page (alpha and omega only).

## Numbers confirmed (10)
1. a04 CCTST pretest 16.09 (SD 4.65), posttest 16.83 (SD 4.68), gain 0.74, t=2.44, KR-20 .69/.68. Confirmed.
2. a18 Bangert-Drowns: 250 studies, 20 usable (19 dissertations), 0.37 SD (50th to 64th percentile), 0.47 / 0.15, 0.50 / 0.21, 0.03 / 0.55. Confirmed.
3. a21/a22/c14 GPT-4 LSAT 163 (~88th), 161 (~83rd), 149 (~40th); contamination row 40 items, 25.00% flagged, -0.85%. Confirmed.
4. a23/c07 AGIEval GPT-4 zero-shot LSAT-AR 35.2, LR 80.6, RC 85.9; CoT 34.4 / 80.6 / 85.1; human 56 / top 91. Confirmed.
5. a28/b14/c18 Hagendorff CRT: 38% humans, 59% and 96% for ChatGPT-3.5/4, 80% to 29% lure with algebra suffix. Confirmed.
6. c01/c02 Friedman Table 1: 0.245, 0.542, 0.307 (LLM wrong); 0.715, 0.811, 0.795 (LLM right). Confirmed.
7. c10 Logic-LM AR-LSAT GPT-4 33.33 / 35.06 / 43.04; self-refinement raises executable rate 5.01 on average; AR-LSAT GPT-4 39.8% row in Table 3. Confirmed.
8. b01 Sebokova WGCTA-II alpha .691, omega .846. Confirmed (subscale values taken from the earlier read, not re-checked).
9. c04 Liu 2023: GPT-4 API 72.25 (LogiQA 2.0), 87.20 (ReClor dev), 33.48 (AR-LSAT); ChatGPT 52.37 and 20.42. Confirmed.
10. a25/c12 ReClor 91.22% from real exams; RoBERTa EASY/HARD 75.5/40.0. Confirmed.

## Corrections
- c04: the ReClor row was mixed up. ChatGPT scores 57.38 on ReClor and RoBERTa 55.01 (paper text). The "ceiling 100" is a table-extraction error: no human ceiling is given for ReClor. The 87.20 figure for GPT-4 is on 500 items; the 92/100 in the table is a 100-item subsample.
- a24 vs c13: LogiQA ceiling is given as 95.00 in one place and 96.00 in another inside the same paper (Table 3 lists 95.00 and 96.00 in different columns; the abstract says 96.00). Human 86.00 and 88.00 likewise. Use "human 86, ceiling 95-96".
- a26 vs c04: AR-LSAT human 59.7% (Zhong 2021, original) vs 56% (AGIEval/Liu 2023, which use a different version). Not a contradiction; different item sets.
- a04: the pretest is dated Feb 1990 and the posttest Nov 1989 in the report. The ordering is odd in the source; the numbers match but dating should not be relied on.
- c26 and a-level synthesis lines should not state AR-LSAT as "close to human"; GPT-4 is 33-43% vs human 56-60%.

## Duplicates (do not count as independent)
- a28, b14, c18, a29, b15, b16, b17, c19 are all Hagendorff et al. (2023): one source.
- a23, c07, c08 are all AGIEval: one source. c26 and c27 are syntheses.
- b20, c01, c02, c28 are all Friedman et al. (2026): one source.
- b01, b02, b03, b27 are all Sebokova et al. (2026). b04, b05 are one meta-analysis.
- b23 and b24 are one paper.

## Contradictions and tensions
- Subscale versus total reliability: Facione and the Delphi report want skill-level scores; every psychometric source (a11, b01) shows subscales are unreliable. The tests sell scores they cannot support.
- Instruction effects: 0.37 SD (a18, 1990) vs g=1.34 (b10, 2026) vs recalled ~0.3 (b11, b12). Differences come from control type, test type and publication bias (b04 shows dissertations score lowest). Unresolved.
- CoT: helps LogiQA (49.3 to 57.8), neutral on LSAT-LR/RC, slightly negative on AR-LSAT (-3.2 in Logic-LM). Task-dependent.
- Hagendorff: ChatGPT-4 answers CRT at 96% even without reasoning (88% forced short), so lure rates differ between "reasoning induced" and "reasoning native" models. Old-model prompt gains may not transfer.

## Weak spots
- Gap a32/c25: no LLM study on Watson-Glaser, Cornell or CCTST was found, but only Crossref and arXiv worked; OpenAlex and Semantic Scholar were rate-limited. The absence claim is weak.
- b11, b12, b13 were recalled, not opened (Huber and Kuncel, Abrami, Arum and Roksa). a12 (Bernard et al.) and a13 (Jacobs, Bondy) not opened.
- Most 2026 sources (b01-b10, b20-b25, c01) are single studies without replication; Friedman N=24.
- Test publishers' own technical reports (a04-a09) have no independent replication except Bycio and Allen (a10).
- GPT-4 era results (2023) are old; no 2025-26 frontier model numbers for LSAT/AR-LSAT/LogiQA beyond o1 (b18, b19).
- b18/b19 (o1 evaluation) were seen in HTML; Ennis-Weir scoring reliability is not known.
- c24 (Tak et al.) has no numbers read.

## Only seen in snippets or partly read
- b08 Appendix B (LLM coding of evidence units) not read.
- c03 qualitative results of Friedman not quantified.
- b01 subscale CFA values were not re-verified this session.

## GAPS
1. Do current frontier models (2025-26, with built-in reasoning) still show a gap between plain and scaffold on AR-LSAT, LogiQA 2.0 and ReClor HARD, or are they saturated except for AR-LSAT? (Need post-2024 measured numbers.)
2. What are the best contamination-free, post-cutoff logic items (new LSAT, LogiQA 2.0 ood 2022+, new Bebras) for an S0 gate, and how large must N be to detect a 3-point scaffold gain?
3. Has any study run Watson-Glaser, Cornell, CCTST, HCTA or the Halpern assessment on an LLM (OpenAlex, Semantic Scholar, Google Scholar, SSRN)?
4. What is the noise floor of repeated runs on these tests for LLMs at temperature 0 vs 1 (run-to-run SD, option-order effects)?
5. What are the verified effect sizes of Huber and Kuncel (2016), Abrami et al. (2015) and the CLA longitudinal results, so human effect sizes can serve as a reference scale for scaffold gains?
6. Are LLM judges reliable enough for open-ended CT tasks (Ennis-Weir, CLA+ performance task) when compared with 2 human raters? Any 2025-26 numbers beyond b23?
7. Do belief-revision and staged-evidence tasks (b07) transfer to agents, and what is the LLM score on them?
8. Does critique-style prompting (CQoT, critical questions) hold up against equal-token CoT on LSAT/ReClor HARD, with significance tests?
9. Do the Delphi six skills map to our operators (interpretation, analysis, evaluation, inference, explanation, self-regulation to O1-O8), and is there any evidence that skill-labelled checks predict outcomes better than unlabelled ones?
10. Which dispositional measures (CCTDI, Need for Cognition) have been run on LLMs, and do they correlate with task accuracy?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d20); claims.jsonl now has K25-K30 and edits to K04, K08, K12, K15, K20, K22.

1. Gap 1 (frontier plain vs scaffold): PARTLY CLOSED. 2025 reasoning models are far above old GPT-4 numbers: AR-LSAT 79.2 (o1-mini), 90.0 (DeepSeek-R1), 92.4 (QwQ-32B) vs human 56 (d01); LogiEval totals 78.7-81.4% over 6,235 items (d03). K12 (AR-LSAT hard) is now contested. Still open: no plain-vs-scaffold comparison at equal tokens for these models, and no 2026 frontier numbers.
2. Gap 2 (contamination-free items, N): PARTLY CLOSED. LogiQA22 (2022 items) drops GPT-4 from 72.25 to 58.49 (d02). LogiEval-Hard (1,617 items, mean 37.97%) is the best unsaturated set (d04). N: about 970 paired items for a 3-point gain (Miller, d06); clustered items up to 3x wider errors (d08). New LSAT/Bebras items not found.
3. Gap 3 (Watson-Glaser/Cornell/CCTST on LLMs): STAYED OPEN, absence re-confirmed by three more queries (d19), still weak evidence of absence.
4. Gap 4 (noise floor): CLOSED for general evals, not for CT tests. Up to 15% run-to-run accuracy variation at temperature 0 (d09); option-order swings large (d10); repeats cut variance only by the (1+2/K)/3 rule (d07). No CT-test-specific run-to-run SD found.
5. Gap 5 (human effect sizes): MOSTLY CLOSED. Abrami g+=0.30 over 341 effects (d11); Huber and Kuncel 71 reports, 50th to 72nd percentile (d12); CLA 45% no gain (d13). Huber and Kuncel per-year d and Abrami full tables not opened.
6. Gap 6 (LLM judges for open CT tasks): PARTLY CLOSED. Peczuh 2025 best alpha .606 (d14, already in K08); GPT-4 judge 85% vs human 81% on chat preferences with 65% position consistency (d15). No Ennis-Weir or CLA+ judge-vs-two-raters number found.
7. Gap 7 (belief-revision tasks on agents): STAYED OPEN. Not searched successfully; no LLM score found.
8. Gap 8 (CQoT vs equal-token CoT): STAYED OPEN. CQoT paper checked (d16): +4.6% / +5.4% on MT-Bench, GPT-4o judge, no significance test, no token control, not LSAT.
9. Gap 9 (Delphi skills to operators; labelled vs unlabelled checks): STAYED OPEN. No evidence found; remains a design test (K01 agent_test).
10. Gap 10 (CCTDI/Need for Cognition on LLMs): STAYED OPEN, no study found; LLM self-report scales are unstable (d17); personality-persona studies exist (d18).

Duplicates: d14 is the same Peczuh source as K08; d16 is the CQoT source already in K20; d17 and d18 are single studies.
