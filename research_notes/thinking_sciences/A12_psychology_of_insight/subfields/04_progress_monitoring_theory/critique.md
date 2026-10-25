# Critique: progress monitoring theory (cross-check)

## What was re-checked
The original PDFs of the human studies (Chronicle 2004, Jones 2003, Chein 2010, Oellinger 2017) could not be re-opened this session: the OpenAlex and Semantic Scholar APIs were rate-limited and Europe PMC held no open copy. So human-study numbers were checked by recomputation from the reported counts, and the LLM numbers were checked against the arXiv full text.

Recomputed and confirmed from counts:
- a03/b02: 20/177 = 11.3%, 6/20 = 30%.
- a06/b04: 4/27 vs 11/27, chi2 = 4.52 (uncorrected, p = .033). Matches.
- a07/b05: 3/11, 3/11, 8/9, 10/11 sum to N = 42; chi2(3) = 16.84. Matches. (Reported p<.015 is loose; exact p = .0008.)
- a08/b06: 10/48 = 20.8%, 36/48 = 75%, 9/48 = 18.75%. Matches.
- a14/b09: 19/30, 8/30, 11/30; chi2(2) = 8.84. Matches.
- a27: 9/26, 5/28, 2/26; chi2(2) = 6.01, p = .049. Matches.
- a28/b14: 3/30, 2/29, 6/28, 21/29 = 10%, 7%, 21%, 72%. Matches. Group sizes sum to 116 (120 recruited).
- a30: 24/64 = 37.5%, 50/64 = 78.1%, overall 37/64 = 57.8%. Matches.
- a23/b07: 7/13 vs 24/26, Fisher p = .0098. Matches the reported .01.

Confirmed against the arXiv full text:
- c22 (Unreliable Progress Bar): 7 models at 93.2-100%, 4 at 0.6-10.1%; 90.6-99.4% pre-action. Confirmed.
- c12: pooled OR 0.77, CI [0.58, 1.02], p = .070, N = 723,200; Math -7.40 pp (high entropy), -22.88 pp (low entropy). Confirmed.
- c11: 6.31% shifted, 2.57% vs 16.44%, N = 723,200. Confirmed, with a correction below.

## Corrections made
1. c11 attributed "2.57% vs 16.44%, N = 723,200" to Qwen-1.5B. The paper gives it as the pooled figure over all models and domains. The Qwen2.5-1.5B all-domains row is different: 7.65% shifted, accuracy 3.95% with a shift vs 20.42% without (-16.47 pp). The claim file uses the pooled wording. The "pooled 6.6% vs 29.0%" figure in c11 was NOT found in the text and should be dropped or re-sourced.
2. a22 vs a24/b07 count of solvers. Jones had 31 unaided solvers (7 + 12 + 12) but 30 solvers among the 37 with usable eye data. Not a contradiction (2 participants lacked eye data), but the evidence lines mix the two bases.
3. a06 sample size (27 per group) is inferred from an equal split, not read. Marked as inferred in the claim.
4. Chronicle 2004 p-values: chi2 = 16.84 for N = 42 gives p < .001, not "p < .015". The paper's exact reported p may differ; use the statistic.

## Contradictions between sources
- Jones 2003 favours representational change (practice and rotation raised solving) while the CSP papers explain the same difficulty by heuristics. Jones himself proposes a merge (a25). Oellinger 2017 supports the merge, but its result (maximisation hint 72% vs constraint relaxation alone 7%) leans toward search criteria in that problem. Oellinger 2006 (matchstick arithmetic, b25) leans the other way, toward representational change. The balance depends on the task type.
- Kershaw and Ohlsson 2001 (training on non-dot turns) and Spiridonov 2019 give a knowledge-and-perception account that a pure lookahead story does not predict. Spiridonov 2019 found dot-turn training lowered solving (37.5% vs 78.1%), while Kershaw found hindering training did not lower it significantly beyond controls (27% vs 37%, not tested alone in the lines read).
- Chein 2010: 0 direct evidence that lookahead equals spatial span. The paper treats span as a proxy.
- LLM side: forced reconsideration helps (c11/c12) but TIP decoding (c14) helps by suppressing switches. These pull in opposite directions; the likely reconciliation is that the right switch timing matters, not switch frequency. Untested.

## Weak spots
- The founding paper (MacGregor 2001) was never opened; all its numbers are second-hand (lookahead mix 32/32/36 comes via Jones 2003).
- Sample sizes are small (N = 19 per cell in the key Chronicle test; N = 39 in the only head-to-head test). Nothing has been replicated by an independent lab on the exact move-statistics test.
- The "independent source" counts for the CSP core are low: the same group (MacGregor, Ormerod, Chronicle) produced the main evidence. Established status was given only where outside groups agree (Jones, Oellinger, Kershaw, Chein).
- The LLM stuck-detection evidence (c17-c20) bundles detectors with other changes, so the detector's own effect is not isolated. The ReflexGrad and Zhang numbers are from preprints we did not independently check.
- The Q-learning study (b21) and the neural model (b18) are indirect.
- 2026 preprint model names and dates could not be sanity-checked beyond the two verified.

## Seen only in snippets or abstracts
a01, a11, a12, a31, a32, a33, b13, b16, b22-b25, b27-b29, c09, c25-c28, c01, c10. Claims K12, K19 rely partly on these. c05, c06, c13-c16 were not re-read this session.

## GAPS
1. Does the CSP ratio (distance left divided by moves left) computed from the agent's own state predict stuck and success better than token-level signals, on a puzzle family with known traps (six-coin, ten-coin, Rush Hour)? No LLM study exists.
2. Does a harness-computed criterion failure, used as the trigger for forced re-representation, beat both a counter-based stuck rule and entropy at equal tokens? This is the main design decision for S5/O4.
3. How much of the human move-choice result is replicable by an independent lab (original N = 19)? Is a replication or a Bayesian reanalysis of Chronicle 2004 available?
4. What is the status of Ormerod 2024 (PRODIGI): does it replace CSP, and does it change what a progress monitor should compute?
5. Does lookahead depth of an LLM (explicit simulate-k-steps budget) change the rate of falling into greedy traps, as human lookahead does (32/32/36 mix)? Sub-question: is lookahead a cost the agent should buy only after criterion failure?
6. What goal does the model infer when the goal is stated abstractly (74% of people pictured a ring)? Does an LLM do the same, and does stating a goal example for the true vs the wrong goal change it as in Chronicle Experiment 3?
7. Which trigger threshold (consecutive low-progress steps, repeat counts) is best across tasks, and does the optimum shift with task difficulty? Current values (3, 4, 5, 6) are hand-chosen.
8. Can mid-run progress be estimated from the model itself at all (self-report fails mid-task)? What separate-call design (residual delta, external critic) gives usable early signal?
9. Is Jones 2003 (representational change wins in an unlimited-move task) generalisable to verbal tasks, and does the matchstick result (Oellinger 2006) reverse the balance for text-only agents?
10. Do spontaneous revisions in frontier (not small GRPO) models help, and does the 6% rate hold? The 2026 shift study covers only small models.

## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d18). Claims K12, K06, K15, K17, K18 and K19 were updated and K21-K25 added. The WebSearch quota ran out partway; OpenAlex and Semantic Scholar were rate-limited; the C: drive was full, so downloads went to D:. Gaps 5 and 6 could not be searched as fully as planned.

Closed or mostly closed:
- Gap 4 (PRODIGI): closed in meaning. PRODIGI extends CSP. It keeps the progress ratio and impasse test and adds "idea discovery" after impasse (d01, d02). Still open: the PRODIGI paper itself is an unpublished manuscript (under review) and was not read.
- Gap 9 (matchstick): mostly closed. Ollinger, Jones and Knoblich 2006 was read in full results: N = 120, no effect of the greedy-solution manipulation (F(1,118) = 1.54 ns), strong effect of constraint depth (F = 37.47), partial-solution move effect F(1,116) = 45.15, 85.46% of moves reduce distance (d04, d05, d06). It reverses the balance for symbolic tasks. It is not a verbal text task, so generalisation to prose is still untested. Jones 2003 is also spatial (car-park) and its unlimited-move design means criterion failure cannot fire (d03).
- Gap 10 (frontier revisions): partly closed. In eight open reasoning models up to DeepSeek-R1-0528, over 90% of reflections are confirmatory and under 2% corrective (d11). No closed frontier model and no non-math task. Still open for those.

Partly answered:
- Gap 8 (progress from the model): hidden-state probes give early signal (AUC 0.84 at 4 tokens vs 0.59 for entropy plus length) but track item difficulty and need open weights (d09, d10). Model-internal horizons are myopic. No API-level separate-call design was found beyond earlier c21/c24 evidence. Mid-run progress should be computed from task state.
- Gap 7 (thresholds): vendor defaults are 2/3/6 repeats and 0.85 similarity, with no ablation anywhere (d15, d16, d17, d12). Open. Needs our own sweep with false-positive logging.
- Gap 3 (Chronicle replication): none found among 30 Europe PMC citing records (d07). Weak evidence; wider citation APIs were rate-limited. Stays open.

Still open, no LLM evidence found (d18):
- Gap 1: CSP ratio against token signals on puzzles with known traps. Related signals exist (CAST uses exact cost-to-go deltas on Rush Hour, d13), but no test of the ratio as a predictor. Frontier models solve 6x6 text Rush Hour at about 92% (d13), and MentisOculi blames early termination and unused budget, not greedy traps (d14). So test traps must be harder than standard Rush Hour boards.
- Gap 2: criterion-failure trigger against counter and entropy triggers at equal tokens. No head-to-head test found. Jones 2003 shows the ratio needs a budget denominator (K22).
- Gap 5: lookahead budget in LLMs, and whether to buy lookahead only after criterion failure.
- Gap 6: goal inference from abstract statements and goal-example effects in LLMs.

Net design effect for S5/O4: compute the CSP ratio in the harness with an explicit budget; on criterion failure force a change of representation first (symbolic evidence favours this), and use the PRODIGI-style step of varying never-varied move properties; keep lookahead as a second, costlier step. These are hypotheses to test, not findings.
