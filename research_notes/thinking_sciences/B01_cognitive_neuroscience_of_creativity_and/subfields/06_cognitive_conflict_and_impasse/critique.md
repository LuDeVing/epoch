# B01.06 Cognitive conflict and impasse: cross-check critique

## Numbers re-opened this session
Confirmed against source text or abstract (opened this session):
1. Danek and Flanagin 2019: 0.59 vs 0.26, F(1,570)=58.81, d=0.64; helpfulness 0.72 vs 0.26, F=107.33, d=0.87; 572 valid (285/287); 42.3% / 28.7% / 29.0%. All correct.
2. Fedor 2015: 19/39 solvers (49%) and 8/62 non-solvers (13%) in classic order; chi2(1,N=101)=41.42, phi=0.64. Correct.
3. d'Aliberti and Ribeiro 2026: 6.31% pooled, about 7.6% Qwen2.5-1.5B, 2.57% vs 16.44% (N=723,200), formal detector 1.79%, AME -0.0311 and -0.0615, Pass1 0.3221 to Pass2 0.4062 (+8.41 pp), 50,574 vs 23,500, Xwords 0.0970 to 0.1015, high-entropy raw -7.40 pp, low-entropy -22.88 pp. All correct.
4. Huang et al. 2024: GPT-3.5 CSQA 75.8 / 38.1 / 41.8; GSM8K 75.9 / 75.1 / 74.7; GPT-4 GSM8K 95.5 / 91.5 / 89.0. Correct. The columns are number of model calls (1, 3, 5), i.e. initial answer, round 1, round 2. 74.7% retention is in the text. The correct-to-wrong vs wrong-to-correct figure is only in a garbled chart, so the text claim "more likely to change correct to incorrect" is quoted, not the percentages.
5. Tsui 2026: 64.5%, 62.8%, Haiku 52.5%, Sonnet 4 41.4%, 5,306 traces (Llama-3.1-8B, LoRA, 2 epochs) cut 76.0%, "Wait" cut 89.3% and raised mean accuracy 156%. Correct. New detail: stripping the think traces from the fine-tune data cut only 38.1%, about half the effect.
6. Mizumoto 2025 (abstract): 201 riddles, human 52.9% (n=126), 7.6% vs 17.6%, verification failures 5% to 39%. Correct.
7. Kim 2025 M-ARC (abstract): LLMs poor vs physicians, overconfident. Correct in direction. Exact 50% / 48% / 66% not re-checked.
8. Tyen 2024 (abstract): mistake finding is the bottleneck; location-given backtracking works. Direction correct. The 52.87 and +18.04 to +43.92 figures not re-checked.
9. Kumar 2024 SCoRe (abstract): applies to Gemini 1.0 Pro and 1.5 Flash. Evidence b15 gave only Flash MATH500. Direction correct. Numbers (52.6 to 41.4; 60.0 to 64.4) not re-checked.
10. Luo, Niki and Phillips 2004: 14 subjects, N380 peak 380 ms at Cz, dipole in frontocentral region. Correct.

Corrections and clarifications:
- a14 says "Solution rate 39%". That is 39 of 101 analysed. The paper reports an overall rate of 51% (55% control, 49% impasse-monitoring) over the full sample before excluding 28 fast solvers. Both are right; cite the denominator.
- a14 says "N=129 after exclusions, 101 analysed". The paper's 101 is the analysed set; the 28 exclusions were removed from 129. Read it as 129 recruited, 101 analysed.
- a22 and b11 label the Huang columns "1 / 3 / 5 calls" vs "1 call / round 1 / round 2". They are the same thing.
- Tsui is listed as 2026 (COLM) in b21; the arXiv ID is 2507 (July 2025). Fine, but the year of first appearance is 2025.
- c05 reports "o1 48%", a "Gemini 1.5 Pro 50%". Not re-checked.

## Contradictions between sources
- ACC: Luo 2004 (ACC dipole, N380) and Dietrich and Kanso (ACC most common) vs Danek 2019 (conflict in posterior visual, thalamus, hippocampus; reverse contrast empty) vs Qin 2009 (ACC marks subgoal handling after retrieval). Differences in task (riddles, word puzzles, magic tricks), analysis (ERP source vs block fMRI) explain much of this.
- Sleep: Schonauer 2018 null vs Cai 2009 REM benefit (the latter not opened).
- Reasoning models and fixation: Kim 2025 (best 50%) vs Kim 2026 (0.751, equal to physicians) vs Mizumoto 2025 (reasoning models 17.6% on riddles). Different tasks, different human baselines. Not a real contradiction yet.
- Self-correction: Huang, Kamoi say no; SCoRe says yes after RL; Reflexion says yes with reliable signals; d'Aliberti says cue helps only when added by code. They agree if read as "external signal needed".
- Physical interaction: earlier claim that handling sticks helps vs Spiridonov 2025 null (original study not opened).

## Weak spots
- The human core of this subfield is thin. Cognitive conflict as a distinct construct rests on one fMRI study (N=30, magic tricks) and one tiny ERP study (N=14). No independent replication of either. The Luo and Knoblich (2007) claim that conflict is needed for restructuring was only seen relayed (a06, opened:false).
- Danek's cue is applied after viewing, so it is a contradicting hint, not conflict that arises by itself. It cannot show that conflict is detected on the way to insight.
- Conflict in LLM studies is never the same construct. Knowledge-conflict papers (Xie, Xu survey) test prompt-vs-memory clashes in QA. Self-correction papers test whether the model can notice its own error. Neither tests a solver stuck under a wrong frame, except NazoNazo, Only Connect and M-ARC, which are benchmarks, not tests of a conflict trigger.
- Many LLM results are from 2023-era models (Huang, Tyen, Shi, Naeini). Newer reasoning models may differ (Kim 2026 suggests they do).
- d'Aliberti and Ribeiro: small RL models (1.5B to 8B), shifts labelled by detectors, Pass 2 is a second sample so compute is confounded with cue. Math gain is large, crosswords tiny.
- MedEinst and Tsui are single-lab, and the scaffold comparison in MedEinst is the authors' own method.
- Independence: many evidence lines cite one paper (Huang appears 7 times, Mizumoto 6, Danek 8). Counts of lines are not counts of sources; claims count sources.
- Rival theories (Kaplan and Simon 1990 incomplete-encoding vs Ohlsson 1992 misleading-encoding) were not opened at source (a12, a28 opened:false).

## Only seen in snippets or relayed (not opened)
Luo and Knoblich 2007; Kaplan and Simon 1990; Ohlsson 1992; Wiley and Danek 2024; the Sprugnoli and Dietrich and Kanso meta-analyses (via Danek); Metcalfe and Wiebe 1987; Cai 2009; Weller 2011 (matchstick interactivity). Exact tables of Spiridonov 2025 (Tables 4-6). MedEinst model-by-model table is garbled; only the Gemini value was read with certainty. Tyen per-task cells uncertain.

## GAPS (most decision-relevant first)
1. Does an externally fired conflict cue beat a plain second sample at equal tokens? d'Aliberti's +8.41 pp on MATH-500 mixes cue and extra compute. A clean control (cue vs no cue, same total tokens) on frontier reasoning models is missing.
2. Which code-checkable conflict signal best predicts a wrong frame in LLM runs: failing test, repeated tool call, sample disagreement, token entropy, or output-vs-expected mismatch? No study compares them head to head, and the doom-loop detector (c19) has no measured gain.
3. Does telling a model which constraint may be relaxed (Knoblich Exp 3 analogue) improve LLM performance on matchstick-like or lateral puzzles, and by how much? Never tested in LLMs.
4. Do reasoning-model baselines (o-series, Claude 4, GPT-5 class) still show the self-correction blind spot, fixation on red herrings and verification failure? Tsui, Naeini and Huang mostly used older or non-reasoning models.
5. Does a stored lesson from a solved impasse (assumption X was wrong) transfer to later same-type tasks in an LLM, and does it harm different-type tasks? Human transfer is one-session only (Knoblich 1999).
6. Is cognitive conflict a separate step from restructuring in any independent human replication? Danek 2019 and Luo 2004 are single studies; a replication or a timed (pupillometry, eye-tracking) design is missing.
7. How often does a confident new framing turn out wrong (false insight) in LLM traces? Mizumoto gives only a descriptive account; Hedne gives human evidence that wrong insight answers stick.
8. What is the right phrasing and order for presenting a clash to an LLM (single coherent contradiction, fixed order, user-attributed vs model-attributed)? Xie and Tsui point in this direction but nobody has tested it inside an agent loop.
9. Does a neutral review prompt (no implication of error) remove the bias toward changing right answers (Huang CSQA explanation was untested)?
10. Source accounts: does incomplete encoding (Kaplan and Simon) or misleading encoding (Ohlsson) better describe LLM failures, and do they need different repairs (add information vs change frame)?

## Gap search results

Evidence file: evidence_d.jsonl (d01 to d16; 13 opened, 3 not opened). New claims K26 to K34; K15 moved to contested; K13, K14, K22, K11, K25 got extra evidence. WebSearch budget was exhausted, and OpenAlex, Semantic Scholar and arXiv search APIs were rate-limited, so papers were found from known arXiv ids and Crossref. Coverage is therefore narrower than a full literature search.

Status of each gap:
1. Cue vs plain second sample at equal tokens: STILL OPEN, better framed. Ghosal 2025 (d01) shows blind "Wait" loses to parallel samples at equal tokens in small distilled models. s1 (d02) shows small Wait gains but compares different models. No test of a gated cue on frontier models. K15 now contested, K26 added.
2. Best code-checkable signal: PARTLY ADDRESSED, no head-to-head. Token-confidence filtering has compute-fair gains (DeepConf, d03). A 3-gram repeat detector has measured recall on stalls (d07). Sample agreement fails on wrong frames (d06). Failing test and output-vs-expected mismatch have no new measurement. K27, K28.
3. Relaxation hint in LLMs (Knoblich Exp 3 analogue): STILL OPEN. No study found. Closest: MathSticks (d13, no hints) and hint-faithfulness work (d14). K34 records the absence.
4. Reasoning-model baselines: PARTLY CLOSED. Tsui v3 (d04) shows a small or negative blind spot for open reasoning models and large "Wait" effect on non-thinking mode. Red-herring fixation and verification failure on frontier closed models were not retested; riddles still show a gap (K18). K29.
5. Lesson transfer: PARTLY CLOSED. Three agent-memory studies (d09, d10, d11) show modest same-domain and cross-site transfer with some harm. None stores a single "assumption X was wrong" lesson; none tests different-type tasks directly. K31, K32.
6. Independent human replication of conflict as a separate step: STILL OPEN. Two candidates were found but not opened (Wiley and Danek 2023 review, d15; a 2026 pupil-dilation insight paper, d16). Open them before closing.
7. False insight frequency in LLM traces: STILL OPEN. Liu 2025 (d12) shows self-reflection words are not tied to accuracy; Mehta (d06) shows wrong frames repeat. No rate for "confident new frame was wrong".
8. Phrasing and order of the clash: STILL OPEN. Huang's prompt variants (d08) show wording moves CSQA by up to 7 points for GPT-4-Turbo, but attribution and order inside an agent loop are untested.
9. Neutral review prompt: CLOSED for weaker models. The default Huang prompt was already neutral and still lost accuracy, and two other wordings did not beat the first answer (d08). No result for current reasoning models. K30.
10. Incomplete vs misleading encoding: PARTLY ADDRESSED. Neither Kaplan and Simon nor Ohlsson was opened. MathSticks (d13) shows an add-information repair (+21.5 pp for o3); Mehta (d06) shows repeated misreadings that prompts do not fix. The mapping to the two human theories is a hypothesis. K33.

Corrections to earlier text: none of the earlier numbers were re-checked in this pass. Caveats on new items: Petrova and Vejsiu (d05) was read as abstract only and is theory, so it is not a second source for the "Wait" effect; Trace2Skill numbers mix columns and rows from large tables, read as best cells, not averages.
