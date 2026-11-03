# Critique: E11.02 Other acceptance principles (cross-check)

## Re-opened sources and corrections
Re-opened this session (pdftotext): Holyoak & Simon 1999, Engel & Gloeckner 2013, Dalal et al. 2024 (arXiv 2402.10767), de Langis et al. 2025 (2512.07777), the 12 Angry AI Agents paper (2605.01986), Thagard 2003 (OJ.pdf), Huntsman & Thomas 2025 (2502.13953).

Confirmed: HS99 Exp1 F(1,44)=35.3; Exp2 F(1,17)=7.71; recalled Smith-supporter pretest -1.32 vs actual -0.30; Exp3 78% vs 28%, chi2(1,64)=16.1, t(62)=8.98. Engel & Gloeckner: 64% vs 50% (n 73/76), 56% vs 40% (50/42), indirect .31 CI [.19,.44], plea offers 70.0 vs 18.4 t(27)=5.00, and the "transient" remark. IBE-Eval: 77%, +17.5%, human agreement 96/91%, kappa .68, Spearman .64 vs .31, 14% parsimony, under 0.1%. de Langis probe and rating table values. Jury paper: 17 of 18 hung, one acquittal in 64 turns with 6 changes. Thagard 2003: .72/.29/.99. Huntsman & Thomas: 76 graphs, density F=369.50.

Corrections:
- a14 gives "pretest Q-scores -.34 vs -.30" beside the memory result. Those are the ACTUAL pretest scores. Recalled scores were -0.36 (Quest) and -1.32 (Smith); F(1,16)=3.66, p=.07; verdict predicts recall r(16)=.43, p=.07. b06 is correct; use it.
- Not re-verified: Thagard's "60 conditional probabilities" (string not found in the text). Treat as unverified.
- IBE-Eval Table 1 text extraction is garbled by columns; the GPT-3.5/COPA column (.59 judge, .95 human, .51/.67/.67/.66/.70, composed .77) reads consistently with c02 and a22.

## Contradictions and weak spots
- Simon et al. 2001 values were not re-opened. Baseline alpha is -0.25 (Exp1, b02) but 0.08 (Exp2, a17/b03): different experiments, not a conflict.
- Engel & Gloeckner Exp2 is borderline (p=.07 one-sided, .028 after excluding 7). Exp3 has N=29.
- The founding story-model experiments (Pennington & Hastie 1986/1988/1992) were never opened (a27, a28, a29, b27). The claim that coverage and uniqueness drive verdicts and confidence has no opened empirical test here, only the authors' 1996 restatement.
- The coherence-shift evidence concerns coherence, not coverage or uniqueness.
- Nearly all human data are student samples on vignettes; effects are reported as transient.
- IBE-Eval covers only COPA and E-CARE (two-option items), GPT-3.5 and Llama 2; nothing on frontier models or open-ended tasks. Hedging as a predictor may be model-specific.
- Snippet-only: c21 (story-model coding, precision 72.7%), c22 (mock jury replication with GPT-4o and Claude 3.5). Unopened: b26 Simon 2004.
- The jury papers (a26/c20, b24) are 2026 preprints; the 18-run study has N=3 per cell.
- Thagard 2003: coherence and Bayesian models predicted guilt where the real jury acquitted, so they do not predict outcomes without an emotion term.

## GAPS
1. Does an LLM's choice and confidence follow planted differences in story coverage, coherence and uniqueness? No direct test found; run it.
2. What exactly do Pennington & Hastie 1986/1988/1992 report (order effects, confidence by uniqueness)? Open full text and get the numbers.
3. Does code-computed selection (coverage count, contradiction count, uniqueness gap) beat majority vote and LLM-judge at equal tokens on a frontier model and on open-ended tasks?
4. Do IBE-Eval criteria (parsimony, hedging) generalise beyond COPA/E-CARE and Llama 2/GPT-3.5 to current models?
5. How large is the LLM coherence shift on evidence ratings (rate items before vs after choosing an answer), and does storing initial ratings externally remove it?
6. Does a MAX-SAT / MAX-CUT acceptance step over extracted claims beat self-consistency voting, given noisy LLM edge weights?
7. Does uniqueness (runner-up gap) predict correctness of LLM answers better than the model's stated confidence?
8. What are the duration and moderators of coherence shift (the "transient" and slow-decider boundary conditions, Simon et al. 2008)?
9. What did the story-model coding (c21) and GPT-4o/Claude mock-jury replication (c22) papers actually measure?
10. Can adversarial or self-evident stories game coverage or parsimony scoring in LLM pipelines?

## Gap search results (2026-11-03)
Evidence in evidence_d.jsonl (d01-d17); claims K21-K26 added, K01, K09, K12, K15, K17, K19, K20 amended. WebSearch budget was exhausted early, and the OpenAlex, Semantic Scholar and arXiv APIs were rate limited, so work used arXiv PDFs and the arXiv search page.

1. LLM choice and confidence vs planted coverage, coherence, uniqueness: STAYS OPEN. arXiv searches for story model + jury + LLM and mock jury LLM returned nothing (d17). No direct test exists; it must be run by us.
2. Pennington & Hastie 1986/1988/1992 numbers: STAYS OPEN. Could not open any of the three (d03). Only the authors' later restatements were read (d01, d02): five confidence determinants, narrative-order advantage, uniqueness defined by stories the juror entertains.
3. Code selection vs majority vote and LLM judge: PARTLY CLOSED. Cross-model agreement beat voting and self-verifier on seven closed-answer benchmarks (d06); USC is the open-ended baseline (d08); self-correction without an outside signal fails (d14). No test of a coverage/contradiction score at equal tokens on a frontier model or open-ended tasks.
4. IBE-Eval generalisation: STAYS OPEN. No follow-up found (d17).
5. Size of LLM coherence shift and external storage: PARTLY CLOSED. Effect sizes are large (d15, d=1.8 to 2.2 vs control), model-dependent revision (d16), but no study stores initial ratings externally or compares to the model's own earlier rating. Untested.
6. MAX-SAT acceptance vs voting with noisy edges: PARTLY CLOSED. ConCoRD shows noisy NLI edges still help small models (d09). No comparison with voting, no frontier model.
7. Uniqueness vs stated confidence: CLOSED for sample agreement (d10, d11, d07): 54.8% vs 92.7% AUROC on GSM8K, unanimous panel 99.5%. Not tested for a runner-up gap over generated stories, and weak on professional-knowledge tasks.
8. Duration and moderators of coherence shift: PARTLY CLOSED. Slow deciders show less bias (d04, d05; Exp2 p=.003 vs .23, interaction not significant), money does not remove it. Simon et al. 2008 was not opened, so the actual duration is unknown.
9. c21 and c22 (story-model coding and GPT-4o/Claude mock-jury replication): STAYS OPEN. Neither could be opened; the search that listed them was not repeatable (budget gone).
10. Gaming coverage or parsimony scoring: PARTLY CLOSED. Padding fooled Claude-v1 and GPT-3.5 judges in 91.3% of 23 cases but GPT-4 in 8.7% (d13); position bias (d12). Nothing on current models or on parsimony scoring specifically.

Caution: 2026 arXiv preprints (d06, d16) are unreviewed; d08 and d14 table columns were read from garbled text extraction.
