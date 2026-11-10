# Cross-check: Critiques of the story model (E11.03)

## Numbers re-opened this session and confirmed
1. Pennington & Hastie 1993 order study (a06): pdftotext of the chapter. Cells 59/78/31/63, row means 69/47, column means 45/70, N=130, 100 statements. Confirmed. (Table layout is garbled in the scan, but the text states 78 and 31.) Also 85% causally linked, 55%/45% testimony vs inferred, 16 of 26, N=414 confirmed.
2. Verdict-system meta-analysis (a21/b08), Europe PMC full text: 1778 jurors, 10 trials, OR 0.625 [0.51, 0.77], 259/901=28.7% vs 344/877=39.2%, RR 0.732, Q(9)=12.28, p=.198, I2=22.2%. Confirmed.
3. Davenport & Winet (b01): n=1,960, 17% exactly 10 to convict, fewer than 1% at 9, chi2=91.18 df=1 p<.001. Confirmed.
4. Neal et al. (b07): 70/161, 72/155, 58/156, 68/152; chi2(3)=3.14, p=.371; package vs instruction OR 1.47, one-tailed p=.049, two-tailed .098. Confirmed.
5. Cullen et al. (a20/b04): Study 1 N=275, Study 2 N=339, 11 participants (6.5%) reported the warning. Confirmed.
6. Cohen & Berryessa (a14/b13): 34 paired, 28 (82.4%) guilty and 6 (17.6%) not guilty before, all guilty after, exact McNemar p=0.031. Confirmed.
7. Ersoz (a16/c01): abstract confirms 17 of 18 hung, N=3 per cell, GPT-4o 1.0 mean changes, Llama 2.0 to 6.0, one Not Guilty run. (Per-model 9/9 hung from earlier agent reading; consistent with 17/18.)
8. Bertalanic & Fortuna (c08): abstract confirms N=10 agents, 3 rounds, modal adoption up to 85.5%, oracle gap up to 32.3 points, debate uses 2.1-3.4x tokens. Per-model accuracies (20.7 vs 48.3) were not re-checked (abstract only).
9. Kumarappan & Mujoo (c10): abstract confirms 47.5-point gap, dissenter cut yield 54-73 points. Cell values (80.25, 12.75) not re-checked.
10. Hao et al. (c09): abstract confirms 37%, 29.3%, 57% more tokens. The 77.35% majority-vote figure not re-checked.

## Corrections
- b13 is the same paper as a14 (Cohen & Berryessa 2026, labelled "Rutgers" in b13; I did not verify the affiliation). Count them as one source.
- a20, b04, b05 are one paper (Cullen et al. 2024); a21 and b08 are one paper (verdict system meta-analysis); a16, c01, c02, c03, c15, c23 are one paper (Ersoz); a19, c04-c06, c21 are one paper (Wu). Evidence counts overstate independence; claims use independent_sources accordingly.
- b02 is typed "replication" but is a set of new experiments, not a replication.
- b07 typed "primary" is better described as a failed replication of the inadmissible-evidence effect (no direct effect, OR=1.05).
- a21 says conviction odds "about 40% lower": the odds ratio 0.625 is 37.5% lower; risk is 26.8% lower (RR 0.732).
- b04 says pro-prosecution misinformation was more misattributed in Study 1; not re-verified.
- a13 (Simon, "Thin empirics") is from an abstract only; year and venue unconfirmed.

## Contradictions and tensions
- Human juries: deliberation can move 11-1 to 12-0 (OpenLearn illustration) while LLM juries almost never move (Ersoz) and the human pilot (Cohen) moved the minority toward the majority. The "flip" direction is not stable; none is a measured base rate.
- Debate evidence is mixed: Bertalanic and Wynn show debate hurts, Hao shows no majority-vote gain, but CyberJurors (c19) reports gains from a 17-juror simulation with precedent. Differences: structure and precedent versus free chat; task and models differ.
- Ersoz attributes anchoring to RLHF, while Kumarappan finds base models show the same or higher yield. These point to different causes (one is a hypothesis in a persona setup, one is a mechanistic test in a different task).
- Misinformation: direction of bias flipped between Cullen Study 1 and Study 2.

## Weak spots
- The central claim (story form matters) has one causal test, the P&H order study, from 1986-1992 student samples, and its replication (Smith 1988) was not opened.
- Most "critique" evidence is indirect (verdict procedures, conformity), not tests of the story model.
- LLM evidence is small N (Ersoz, N=3 per cell) or on non-legal tasks (MMLU, GSM).
- Three recalled items (b18, b19, b20) were never opened. Kalven & Zeisel and Devine 2001 numbers are unverified.

## Only seen in snippets/abstracts
a13, b16, b17 (abstract only), a22, a23 (not opened), b18-b20 (recalled), Wynn et al. tables, Jagged Judges, Choi, Sachdeva, Ni & Zou details beyond abstract, McKenzie et al. 2002.

## GAPS
1. Does any LLM experiment manipulate evidence order (story vs source order) and measure verdict or answer changes? None found; run it on our own logs at equal tokens.
2. What fraction of real jury verdicts matches the first-ballot majority (Kalven & Zeisel 1966; Devine et al. 2001; Hastie et al. 1983)? Open and verify the numbers.
3. Do story-completeness or coverage checks (Urbaniak criteria; VeriScene audit) improve LLM accuracy at equal tokens on non-legal reasoning tasks?
4. What exactly did Smith 1988 and later replications of the order effect find (cell sizes, effect size), and has it failed to replicate anywhere?
5. Is the 17/18 hung-jury result in Ersoz due to persona anchoring, temperature, or RLHF? Needs a larger N with unanchored starting votes.
6. How much of the story model's explanatory power survives when story form is replaced by an equally structured non-story format (causal list, table)?
7. Per-cell values for Bertalanic (20.7% vs 48.3%), Kumarappan (80.25/12.75) and Hao (77.35%): confirm from full text.
8. Do coherence-shift effects (evidence re-rated toward the favoured answer) appear in LLMs, and does rating evidence before showing a candidate answer remove them?
9. Is a protected dissent slot better than a code-triggered recheck for stopping bad flips in an equal-token panel?
10. What does the McKenzie, Lee & Chen 2002 "weak defense story strengthens the prosecution" effect look like with exact numbers, and does it appear when an LLM generates a weak rival?

## Gap search results (2026-11-10)
Evidence is in evidence_d.jsonl (d01-d17). Claims K11, K17, K19, K22, K23 updated; K24-K28 added.

1. Gap 1 (LLM order test): PARTLY CLOSED. No story-versus-source order test on LLMs. Two close studies found: Bessis et al. 2026 (GPT-4o and GPT-5.2, N=720 trials each, recency of incriminating evidence, prompts did not fix it, d04/d05) and Liu et al. 2025 (six LLMs, 657 civil cases, last-listed side favoured, d06). Story order itself remains open.
2. Gap 2 (first-ballot majority): CLOSED as a secondary report. 90% in 225 retrospective juror reports; weak because immediate votes are rare (d01-d03). Kalven & Zeisel and Devine 2001 were not opened directly.
3. Gap 3 (coverage checks at equal tokens): OPEN. Only a non-legal analog (list-then-verify, d15); no equal-token accuracy test.
4. Gap 4 (Smith 1988 and replications): OPEN. Not located; the story-order effect remains single-study (d17). A dissertation snippet suggesting direction reversal by sample was not verified.
5. Gap 5 (why 17/18 hung): OPEN. Full text shows fixed temperature 0.9, two models, persona kept in the no-vote arm (d09).
6. Gap 6 (story versus structured non-story format): OPEN. Nothing found.
7. Gap 7 (per-cell values): CLOSED. Bertalanic 20.7 vs 48.3, Kumarappan 80.25 and 12.75, Hao 77.35 confirmed in full text (d10-d12).
8. Gap 8 (coherence shifts in LLMs): PARTLY CLOSED by analogy. Choice-supportive bias (32.5% vs 13.1% change of mind, d07) and post-decision reversibility (49%, d08). Evidence-rating shifts not directly tested.
9. Gap 9 (protected dissent vs recheck): OPEN. Matched-ceiling and diversity studies exist (d13, d14); the head-to-head was not found.
10. Gap 10 (McKenzie et al. 2002): OPEN. Abstract only (d16); no numbers, no LLM test.

Notes: arXiv and Semantic Scholar APIs were rate-limited; web search used 6 of 8 calls. Two source pages returned 403.
