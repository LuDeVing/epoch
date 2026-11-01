# E09.04 Debugging as scientific method: cross-check critique

## Numbers re-opened this session (full PDF text, arXiv)
Confirmed exactly: Alaboudi and LaToza 2020 (11%, 25%, 39% correct hypotheses; 5x odds, p=0.01; potential hypotheses OR 6.24, p=0.03; fault locations p=0.67 for fix rate). Kang et al. 2023 AutoSD (Defects4J v1.2: 87 plain vs 76 AutoSD; v2.0: 110 vs 113; 73% vs 63% plausible runs; DONE +12.4 / -11 points; 89% vs 82% correct; CodeGen-6B few-shot 44). Olausson et al. 2024 (33.30% vs 52.60%, 1.58x; per-difficulty 42.64/19.33/3.67 vs 62.21/45.67/14.67). Huang et al. 2024 (GPT-3.5 CSQA 75.8 to 38.1; GSM8K 75.9/75.1/74.7; GPT-4 GSM8K 91.5/89.0). debug-gym (Claude 3.7 37.2 / 48.4 / 52.1; Llama 2.4 / 4.0 / 4.8). ChatDBG (57%, 67%, 85%; 36% root cause, 55% proximate).

## Corrections
1. **b21 is wrong for GPT-3.5 with oracle labels.** b21 says GPT-3.5 GSM8K 75.9 to 95.5, CSQA 75.8 to 82.0, HotpotQA 26.0 to 49.0. Table 2 of Huang et al. shows those figures (95.5, 82.0, 49.0) are the GPT-4 STANDARD baseline. GPT-3.5 with oracle is 84.3 / 89.7 / 29.0 (as a21 says). GPT-4 oracle 97.5 / 85.5 / 59.0 is right. c14's "oracle GPT-3.5 75.9 to 95.5" has the same error. Use a21.
2. **debug-gym SWE-bench-Lite table (a22).** The PDF text layout is garbled. Reading by row and the paper's prose gives: GPT-4o 19.1 / 17.2 / 23.6 (rewrite / debug / debug(5)); GPT-4o-mini 4.0 / 3.5 / 6.2; o1-preview 10.7 / 30.2 / 30.8; o3-mini 8.5 / 22.1 / 19.8; Claude 3.7 37.2 / 48.4 / 52.1; Llama 2.4 / 4.0 / 4.8. a22 matches this. The paper's prose says debug hurts weaker models including Llama-3.3-70B, but the table has Llama going UP (2.4 to 4.0). Table and prose disagree. Treat the Llama claim as unclear. Note the paper says o3-mini benefits from debug but debug(5) is lower than debug for it (19.8 vs 22.1).
3. **Developer study composition (Kang).** a17 says 8 undergrad, 6 graduate, 6 professional; b12 says 14 students, 6 professionals. These agree (8+6=14). The headline "5 of 6 bugs" (c05) and "7 of 12 cases" (a17) are both used; report as "higher in 7 of 12 problem cases" and say the effect is not significant on time.
4. **CRUXEval (a25 vs b26 vs c17).** Reported with slightly different decimals (75/81 vs 74.8/81.9 for GPT-4 CoT). Use the rounded "about 75% and 81%". Not re-opened.
5. **c15 (Tyen et al.)** reports "52.87" without clear meaning. Do not quote it.
6. a03 (Wason numbers) are from memory and flagged so. Do not cite them.

## Contradictions between sources
- Self-report (Siegmund as cited by Kang) says developers follow hypothesis then verification. Direct observation (Alaboudi and LaToza 2021: 84% manual run-and-observe; few stated hypotheses) shows less formal practice. Claim K04 is contested.
- AutoSD: wins on a self-made benchmark (ARHE, built by the authors) and Defects4J v2.0, loses on v1.2. The authors say it improves with stronger models. Not independent replication.
- Debugger access: helps strong models, hurts weak ones (debug-gym), while ChatDBG and LDB report gains with a single model family. Results depend heavily on model strength.
- Self-correction: Huang says intrinsic correction hurts; Reflexion and Self-Debug report gains, but those use test feedback (an external signal). Not truly contradictory; the difference is the source of the signal.

## Weak spots
- No human controlled trial found that shows the Zeller protocol itself speeds people up. Zeller 2009 was never opened (a01 is from AutoSD's description).
- Most "hypothesis" numbers for humans come from ONE research group (Alaboudi and LaToza), small samples (20 per condition, 60 sessions), and are correlational.
- AutoSD evidence is one paper with one author group. Its benchmark ARHE is self-built. No replication found.
- The classical papers (Gould 1975, Vessey 1985, Gugerty and Olson 1986, Katz and Anderson 1987, Parnin and Orso 2011, Ko and Myers 2008, Zeller and Hildebrandt 2002) have no numbers and opened:false. Do not quote them.
- Several LLM results use old models (GPT-3.5, Codex, GPT-4 Turbo). Little data on 2025-2026 reasoning models with an explicit predict step.
- Ko and Myers 2004 (a13, a14) was not re-opened by me; small N=8 for the user study.

## Only seen in snippets or secondhand
a02 (Siegmund, citation only), a01, a03 to a12 (not opened), c26 (CRITIC: abstract and summaries only), a27 (figure not read), c24, c20 and c21 (BoxingGym) and c22 (Qiu) were not re-opened by me.

## GAPS (most decision-relevant first)
1. Does forcing a written prediction BEFORE each run (not only a hypothesis) raise bug-fix rate at equal tokens for a modern reasoning model? No study isolates the prediction step; AutoSD bundles it with the whole loop.
2. How often is the model's pre-run prediction of program output wrong on realistic bugs, and does prediction error predict a wrong hypothesis? CRUXEval measures isolated functions only.
3. What share of "refuted" hypotheses in LLM agents come from invalid experiments (probe never executed)? Only one count exists (13 of 25 in AutoSD).
4. Does debugger or probe access help current frontier models, and where is the crossover model strength where it turns from harmful to helpful (debug-gym shows a split)?
5. Do agents that test to DISCONFIRM (Wason-style) beat those that test to confirm on debugging tasks? No LLM debugging study varies this.
6. Is the Alaboudi and LaToza result (correct early hypothesis gives about 5x odds) causal? Does a scaffold that supplies candidate hypotheses help (OR 6.24) when the candidates come from an LLM?
7. Is the DONE or confidence token well calibrated for current models, and can it serve as the stop rule (89 vs 82% is a small gap)?
8. Do the classic human findings (Gould, Vessey, Gugerty and Olson, Katz and Anderson: forward vs backward reasoning, expert hypothesis testing) hold up? These were never opened; verify exact numbers.
9. Is there any replication of AutoSD or of Whyline-style why-not questions in an LLM agent?
10. How do results change with bug type (logic vs syntax vs multi-bug) for a predict-observe loop?

## Gap search results (evidence_d.jsonl, d01 to d16; claims K24 to K30)
The web search quota ran out partway. The rest used direct arXiv PDFs (read with pdftotext) and one university PDF. Every d-line was read this session.

**Partly closed**
- Gap 2 (how often is the pre-run prediction wrong): REval (d10) gives mean accuracy 44.4% and consistency score 10.3 across 15 models; GPT-4-Turbo 75.0% and 42.5. LDB (d11): self-simulated traces gave 0 to -0.6 points on StarCoder, real traces +0.6 to +9.1. No study yet links prediction error to a wrong hypothesis on repository bugs.
- Gap 3 (invalid experiments): a second count now exists. DoVer (d03): Inconclusive 66.7 / 57.6 / 28.6% of intervention trials, mostly because the intervention was not carried out. AutoSD's 13 of 25 stays the only code-level count. Straubinger (d02): the model's "cannot be killed" verdicts were often wrong.
- Gap 4 (debugger access): debug-gym table re-read (d06) confirms gains for o1-preview, o3-mini, Claude 3.7 and losses for GPT-4o and GPT-4o-mini. The Llama row still disagrees with the prose (2.4 to 4.0 in the table, near noise). Debug2Fix (d08, d09), 2026 frontier models: gain only when the debugger sits behind a subagent and edits are blocked until it is called. The crossover is about adoption and tool design, not only strength. One group, not replicated.
- Gap 10 (bug type): DebugBench (d16) re-confirms that runtime feedback does not help logic bugs. Only overall pass rates could be read (GPT-4 75.0%, GPT-3.5 62.1%). No predict-observe test by bug type.

**Sharpened**
- Gap 1 stays open, but d01 is the nearest ablation: hypothesis loop equals plain iteration in success (~60%) and costs more tokens. Do not assume a predict step adds accuracy at equal tokens.
- Ko and Myers 2004 (a13, a14) is now opened (d15): 4 vs 4 users, tasks 3.20 vs 2.25, debug time cut 7.8x over six scenarios. Soften the "7.8x" wording.
- Gap 7 (DONE as stop rule): only older evidence (d13, calibration error 0.09 to 0.73). Not tested on current reasoning models. Open.

**Still open**
- Gap 5 (disconfirm vs confirm tests in LLM debugging): nothing found.
- Gap 6 (is the 5x result causal; do LLM-supplied hypotheses help): nothing found. Alaboudi and LaToza stays correlational and single group.
- Gap 8 (classic human findings): Gould, Vessey, Gugerty and Olson, Katz and Anderson, Parnin and Orso could not be obtained (no open copy at the URLs tried; searches blocked). They stay unopened. Do not quote them.
- Gap 9 (replication of AutoSD or Whyline in an LLM agent): Straubinger 2025 reuses the loop for test generation; DoVer tests hypotheses by intervention. Neither is a replication.

**New cautions**
- ForeAgent (d14) predictions are 61.5% vs 50% chance. Use predictions as a filter, not a verdict.
- Earlier corrections 1 and 2 stand. d06 gives the full debug-gym row set.
