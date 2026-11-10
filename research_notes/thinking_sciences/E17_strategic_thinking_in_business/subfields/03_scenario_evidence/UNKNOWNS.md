# Scenario evidence: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E17.03-U1 | Does a multi-step scenario operator (3 stratified worlds, branch probabilities normalised by code) beat no-scenario on forecast calibration? | Scenario operator in S3 for forecast-type items | O3 / S3-S4 | K22, d05, d06: one-prompt step null (-0.007 Brier); single-source; no multi-step test | Arms: plain, plain + extra samples, base rate, base rate + scenarios. 100+ resolved binary questions. Metric: Brier, 80% interval hit rate | Beats the best other arm by at least 0.01 Brier with bootstrap 95% interval excluding 0, on 2 models | High |
| E17.03-U2 | Does "base rate first" alone improve our agent's forecasts? | Base-rate-first step in S1/S2 for forecasting items | S1/S2 | K22, d05: adjusted-significant in one 4-model study; single-source | Arms: plain vs base rate first, same tokens. Same 100 questions. Metric: Brier | Brier down at least 0.01, interval excludes 0 | High |
| E17.03-U3 | Does a robust-option rule over several worlds (sign per world, count by code) improve choices when worlds disagree? | Robust-option selector at S7 | O3 / S7 | K01, K04, a04, a06: human direction shifts, no control; single-source | 40 decisions with payoff tables over 3 worlds; arms: plain vs sign table + robust pick. Metric: expected regret | Regret down at least 10% where worlds disagree, no loss where one option dominates | High |
| E17.03-U4 | Optimal number of scenarios (1, 2-3, 5)? | Fix the number of worlds at S3 | O3 | K16, K26, c09, c11: contested; no experiment varying number | Same items as U1/U3; 1, 2, 3, 5 worlds at equal tokens. Metric: accuracy per token | One setting beats the others by at least 3 points with interval excluding 0; otherwise default to 2-3 only if not worse than 1 | Med |
| E17.03-U5 | Does a problem-recognition step (name the strategic structure) before scenario work raise quality? | Recognition sub-step in S0/S1 for business-type items | S0 / O1 | K17, c16: gate pass 27.9%; single-source | KWBench-style 100+ tasks; arms: plain vs name-the-structure first. Metric: gate pass rate, rubric score | Gate pass up at least 10 points and rubric score not lower | High |
| E17.03-U6 | Does a scenario pass fix overconfidence or only change answers? Do high-confidence answers resist revision as in experts? | Nothing if it only changes answers (confirms: use a code calibration check instead) | G (calibration) | K02, K03, K05, a02, a05: human-only; Schoemaker and Kuhn contested, unread | 100 questions with confidence; plain vs scenario pass. Metrics: Brier, interval width, change rate by confidence | Add scenario pass for calibration only if interval hit rate moves toward nominal by at least 5 points; else record as null | Med |
| E17.03-U7 | Does a framing-invariance check (gain vs loss frame must agree) with a scenario pass cut framing errors? | Frame-swap check in S8 | G / S8 | K23, d09: abstract only, 252 students; single-source | 60 paired frames; plain vs scenario pass vs code frame-swap check. Metric: answer disagreement rate | Disagreement down at least 30% relative, accuracy not lower | Med |
| E17.03-U8 | Does swapping actor names (neutral labels) and comparing outputs remove actor bias in scenario answers? | Neutral-label rewrite in S1 input hygiene plus swap check | S1 / G | K15, c06: single-source; no scaffold test | 100 scenarios; arms: named, neutral, neutral + swap-compare. Metric: disagreement under swap | Disagreement down at least 30% relative, accuracy unchanged | Med |
| E17.03-U9 | Does diverge-then-converge (stratified worlds, code selector) convert breadth into accuracy? | Diverge then converge pattern at S3 to S7 | S3-S7 | K25, K19, d08, c17, c18: single-source on breadth with no accuracy gain | Arms: single prompt, stratified K=4 + code selector, stratified K=4 + model judge. Metrics: diversity (embedding plus approach judge), accuracy | Stratified + code beats single prompt in accuracy by at least 3 points; model-judge arm not better than code arm | High |
| E17.03-U10 | Does a short reflection line (de-escalation style) lower unstable or extreme outputs in scenario answers? | One-line reflection for high-stakes items | G | K13, c05: Mistral-7B, 10 runs per cell; single-source | Arms: plain vs reflection line vs lower temperature, equal tokens. Metric: variance of answers across 10 seeds, accuracy | Variance down at least 30% with accuracy not lower | Low |
| E17.03-U11 | Do LLM-made scenarios mislead through detail (conjunction and imagination inflation)? | Short-branch rule and frequency format if it does | G5 | b11, b15: human-only; no LLM test | Items with logically nested events; arms: rich narrative vs terse branches vs frequency format. Metric: share of conjunction violations (P(A and B) > P(A)) | Violations fall at least 30% relative with terse or frequency format | Med |
| E17.03-U12 | Is there an LLM version of the Phadnis direction-of-evidence effect, and does it help? | Scenario-conditioned re-judgment of options | O3 | K01, a04: human, no control | Give each option a verdict under a world; measure move toward verdict vs plain re-asking; compare final accuracy | Moves toward correct verdict and accuracy up at least 3 points vs plain re-ask at equal tokens | Low |

## Open questions we cannot test on our bench yet

- Firm performance effect of scenario use (Phelps 2001, Zanin 2021). Needs firm data and full texts; our bench has neither.
- Implementation rate with and without scenarios (de Geus). Needs organisational follow-through; no agent analogue. A long-horizon multi-session task with stored plans might approximate it.
- Original Diffenbach 1983 numbers and satisfaction surveys. Needs the paper; unblock by interlibrary access.
- Meissner and Wulf 2013, Schoemaker 1993, Kuhn and Sniezek 1996 cell values. Needs full text; would sharpen U6 and U7.
- Kanis et al. 2026 effect sizes. Needs the paper; the task is startup evaluation, not scenarios.
- Kozachek 2026 and Time Machine: LLM vs human scenario diversity and plausibility. Needs full text and a plausibility rubric.
- Whether human results from one-time workshops transfer to a persistent-memory agent. Needs a memory-enabled arm across sessions.
- Long-horizon validity of scenarios (graded against outcomes years later). Backtests on dated reports (as in McIntosh 2026) may approximate it.

## Order to run

1. U1 with U2: scenario operator vs base rate vs plain on resolved forecasts. It is the missing direct test, and a null protects the schema from an unneeded operator.
2. U5: problem-recognition step. Cheap, a large measured headroom (27.9% gate pass), and it gates every other business-type operator.
3. U9: diverge-then-converge with a code selector. Reusable across all generation states, and it tests G4/G5 together.
