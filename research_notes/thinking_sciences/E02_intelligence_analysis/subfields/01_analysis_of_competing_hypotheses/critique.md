# Critique: ACH (E02.01), cross-check

## Numbers re-checked against the saved source text (D:/research_scratch/E02.01)
Confirmed as recorded:
1. Mandel, Karvetski, Dhami 2018: MAE control 0.21 [0.17,0.26] vs ACH 0.26, t(45.9)=1.49, d=0.43, p=.14 (a06, b05).
2. Dhami 2019: base rates used by 12% (3) of ACH vs 52% (13) of control, chi2(1,N=50)=9.19, p=.002 (b03).
3. Dhami 2019: top hypothesis correct 9/25 (36%) vs 8/25 (33%), chi2(1,N=49)=.04, p=.845 (b01). Note N=49, one analyst missing.
4. Karvetski and Mandel 2020: N=227, judgment-choice match .74 [.70,.77], conservatism d=1.54, t(226)=23.20 (a11, b11).
5. Martin 2025: ACH r=-0.08 with accuracy; ACH code reliability 0.79 [0.32,1.00] (b22). Very wide interval.
6. PRISM: Direct 58.1, CoT 57.2, PRISM 71.3 (+13.2); P1P4 63.8; with MOMA 70.5 (+6.7); with ACH 71.3 (+0.8); text says 89% / 11% (c01-c03).
7. Marozzo and Lio: SIA 79.2 [72.7,83.7]; without structured investigation 72.8; without hypothesis expansion 76.5 (c19, c20).
8. HypoArena: text says +88 to "nearly 60-point decline"; Spearman -0.10 (a27, c06). Figure label shows -58 for the worst model.
9. AgentCDM ablation: full 78.5/65.2/96.0; scaffolding-only 68.1/49.4/84.0 (b27, c09).
10. AgentCDM all-average table: rows are split across lines in the text extraction.

## Corrections and conflicts
- b26 says zero-shot ACH decider +2.3 on all-average; c08 says ACH prompt +2.0 (67.9 vs 66.0 base), Qwen-7B-Instruct +1.6. The source table has both numbers on two different row groups (82.9(+2.3) and 67.9(+2.0)). So "+2.0 to +2.3" is used in claim K10, and the exact base for each is unresolved. Do not quote either to more than one decimal.
- b26 reports unstructured decider -0.7; c08 reports 65.8 (-0.1). Same table, different row groups. Unstructured is about zero in both readings.
- b01 note: the 8/25 in control is out of 25, but chi2 used N=49. Fine, but "fully correct rank order 2 of 16" has a different denominator; keep the denominators when quoting.
- Duplicate lines (a06-a09 vs b05-b07; a11-a13 vs b08-b10; a20/a21 vs b20/b21; a14 vs b15; a27 vs c05/c06; b26/b27 vs c08/c09). Independent_sources in claims counts papers, not lines.
- Wilcox and Mandel review: cited as 2023 (a14) and 2024 (b15). Same paper; the 2024 print year is likely correct, 2023 is the online date. Unchecked.
- SUBFIELDS.md says ACH has "moderate to strong support" in Coulthart 2017; this was not verified (b25) and conflicts with every controlled test found.

## Weak spots
- The main human evidence comes from one research group (Mandel, Dhami, Karvetski). Claims K01, K02, K05 are therefore less independent than their counts suggest. Outside that group: Lehner 2008, Whitesmith, Maegherman, Martin.
- Samples are small (N=50, 24, 39) or non-analysts (students, crowd workers, N=227 on Qualtrics). The 2018 effects (d about 0.43-0.52) are medium but not significant; this is "no evidence of gain", not "evidence of harm".
- Dhami 2024: 90% female students, mean age 20; layout effect might not generalise.
- LLM evidence is from preprints dated 2025-2026, with different tasks (MMLU, MuSR, forum threads, medicine). No study compares plain ACH matrix vs plain prompt on one model at equal tokens. PRISM's ACH stage is the closest (+0.8), single study.
- Token cost is not reported in PRISM, AgentCDM, HypoArena or SIA, so equal-token claims are unsupported. Self-consistency (+5.1) in PRISM may cost as much as the pipeline.
- The first Heuer-based claim of "increases the odds" has never been tested directly by a randomized trial of analysts at scale.

## Only seen in snippets (opened:false, not relied on for numbers)
a16/b17 Lehner 2008, a17/b12-b14 partly (Karvetski, Mandel, Irwin 2020 were opened in b but snippet in a), a18/b18 Whitesmith, a19/b19 Maegherman (the 38% figure is via the review), a24/c24 Cheikes 2004 (PDF blocked), c25 Pirolli and Good, b24 Chang et al. 2018, b25 Coulthart 2017. Claim K07 rests mostly on review text.

## GAPS
1. Does an ACH-matrix prompt beat a plain prompt for a single LLM agent at equal tokens, on tasks with known posteriors (the Mandel 2018 style)? No study has isolated this.
2. Does the one measured human benefit (better cue diagnosticity ratings, r=.68 vs .17) transfer to LLMs, and does a separate diagnosticity step alone beat the full matrix?
3. What does the PRISM ACH stage contribute on tasks other than MuSR, and is the +0.8 inside noise (no confidence interval given)?
4. Is the HypoArena result (-60 to +88) driven by ACH or by the other 11 skills, and why do the strongest models lose (candidate compression)?
5. Do LLMs double count correlated cues and give non-diagnostic evidence about 30% weight, as humans do, and does a matrix make it worse?
6. Does a coherentization or multi-sample aggregation step (human MAE .23 to .09 with 50 analysts) give the same benefit to LLM samples at equal tokens, with groups of 2-3?
7. Does a cheap disconfirm-first rule (Think-in-Opposites) beat full ACH on LLMs, and does it hurt non-thinking models as Dual-Goal did?
8. Is there any real-world, field, accuracy-scored study of ACH use (beyond Martin 2025, n=138, r=-.08), e.g. forecasting tournaments with an ACH arm?
9. What did Lehner 2008 and Cheikes 2004 actually report as numbers (only seen via reviews)?
10. Are there 2026 LLM papers testing ACH as a bias-reduction prompt (anchoring, order effects) with measured effect sizes that our search missed?

## Gap search results (evidence_d.jsonl, d01-d15; run 2026-11-03)
Limits of this pass: the WebSearch quota was used up, the arXiv API, Semantic Scholar and OpenAlex APIs were rate-limited, and journal sites (RAND, MITRE, Taylor and Francis, ResearchGate) returned HTTP 403. I used arXiv listing pages and full PDFs. Absence in this pass is weak evidence of absence.

1. ACH matrix vs plain prompt at equal tokens: STAYED OPEN. No study found (d14). New claim K20 records that this is untested, not refuted.
2. Diagnosticity benefit transfer / diagnosticity-only step: STAYED OPEN. HypoArena has a separate Diagnostic Reasoning skill but never ran it alone (d02). Thinking models do the Bayes arithmetic on independent evidence without a matrix (d04).
3. PRISM ACH stage elsewhere and noise: PARTLY CLOSED. Only MuSR is tested; one temperature-0 run, 250 items, no interval; my rough SE is 1.3 points, so +0.8 is inside noise (d15, derived, not from the paper). Other tasks still untested. K11 updated.
4. HypoArena -60 to +88: PARTLY CLOSED. No per-skill ablation, no skill-use counts, no token cost; the stated mechanism is candidate compression, seen qualitatively (d01, d02). Cannot be assigned to ACH. K12 updated.
5. LLM double counting of correlated cues and 30% weight on non-diagnostic evidence: STAYED OPEN for cues. Related finding: same-model samples are correlated, so more samples are not more evidence (d09, d10). New K19. No test of correlated cue text.
6. Coherentization or aggregation in LLMs at equal tokens: PARTLY CLOSED. One joint elicitation of all related events nearly removes incoherence (d07); same-dialogue elicitation does the same (d03); averaging 5 same-model samples helps little because 95% of answers are identical (d08); heterogeneous panels beat same-model panels by 4.7 to 34.6 points (d10, needs outside models). Groups of 2 or 3 from one model: not tested. K05 updated, K21 new.
7. Think-in-Opposites vs full ACH, harm to non-thinking models: PARTLY CLOSED. TiO helped in 11 of 11, Dual-Goal 8 of 11 and slightly hurt non-thinking models; gains significant only for thinking models; cost 1,000-2,300 tokens per thinking turn (d11, d12). No head-to-head with full ACH. K14, K15 updated.
8. Field or tournament study of ACH use with accuracy: STAYED OPEN. No new study found; the Chang et al. 2018 paper and the RAND report were blocked (403). Martin 2025 (r=-.08, n=138) remains the only one.
9. Lehner 2008 and Cheikes 2004 numbers: STAYED OPEN. MITRE and DTIC copies returned HTML or 403. Claim K07 still rests on review text.
10. 2026 LLM papers testing ACH as a bias-reduction prompt: CLOSED as "none found" in preprints (d14). The only anchoring-in-LLM papers found (e.g. anchoring in LLM-as-judge, 2608.25869) do not use ACH and were not opened.

Side findings: a heavy harness (BED-LLM) no longer beat a plain prompt on current reasoning models (d05, K18); this is the best direct support for schema 4b found. Adversary Brains (d13) is another untested ACH-by-LLM design.
