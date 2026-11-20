# Novices and education: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E09.08-U1 | Does a stated hypothesis before the first edit raise fix rate? | "State the suspected cause before editing" in S1-S5 | S1-S5 | K06, K09 (c13, b03); human-only; non-randomised n=13 vs 15 | Free-form vs hypothesis-then-test-then-edit; 60+ seeded novice-style bugs with tests; fix pass rate on held-out tests | Gain of 5 points or more with a 95% CI above 0 on at least one model class, no loss on the other | High |
| E09.08-U2 | Does a cheap independent validator raise precision of diagnoses without large coverage loss? | Validator pass on any diagnosis or hint before it is used | G2 / S6 | K04, K21 (c09, c10, d09); single group; 2023 models; simulated students | One model vs generate plus weaker-model validator; help-request items with known issues; precision at coverage 70% or more | Precision up 15 points or more at coverage 70% or more, tokens equal | High |
| E09.08-U3 | Does naming the false belief behind a bug raise localisation? | "What wrong belief produces this bug?" step | S2 | K12, K11 (a08, a09, a05, d19); diagnosis measured, localisation gain not; LLM judge | Plain vs misconception-naming step; seeded misconception bugs (syntax, concept, strategy); Top-1 and fix rate | Top-1 up 5 points or more, and the named belief is correct on 70% or more of cases | High |
| E09.08-U4 | Does a code-computed counterexample step help diagnosis? | Counterexample operator at S5/S6 | O (disconfirm) / S5 | K11 (a05, a06); single source; LLM judge; no accuracy outcome | Plain vs counterexample step; semantic bugs (grouping, off-by-one); localisation accuracy | Gain of 5 points or more, strongest on semantic bugs | Med |
| E09.08-U5 | Does an explain-before-apply gate keep skill on held-out unaided items? | "Say why the patch works" check before applying | G / S9 | K20 (d10, d11); one randomised human study, one session; humans not agents | Fix freely vs gated; follow-up held-out bugs with the explainer removed; pass rate and token cost | Held-out pass rate up 10 points or more for cost under 25% extra tokens | Med |
| E09.08-U6 | Is question-first better than answer-first for diagnosis? | A question-first mode | O | K10 (b13, c20, d12); contested; simulated students; one RCT null | Question-first vs answer-first on seeded student bugs; fix rate and wasted turns | Fix rate no lower and tokens equal or lower; otherwise do not add | Low |
| E09.08-U7 | Is a failure- or uncertainty-triggered reflection better than always-on? | Keep S9/G1 as is (trigger on signal) and name the trigger | G1 / S9 | K14 (b17, b24, d11); contested, no replication, human physiology trigger | Always-on vs triggered reflection at equal tokens; items with uncertain first answers | Triggered at least equal pass rate with fewer tokens, over 3 seeds | Med |
| E09.08-U8 | Does staged structure help only non-reasoning models? | A mode rule in S0: staged scaffold only for non-reasoning models | S0 gate | K18 (d06); 50 programs per set; no equal-token control | Staged vs free-form on a reasoning and a non-reasoning model; seeded bugs | Gain for the non-reasoning model of 5 points or more and no gain (within 2 points) for the reasoning model | High |
| E09.08-U9 | Are conditional-logic faults better solved by execution than by reading? | Route branch faults to S4 execution | S4 | K01 (c03); GPT-3.5, all-issues 35% vs 73% for loops; single source | Read-only diagnosis vs run-first, split by fault type; fault-type accuracy | Run-first beats read-only by 10 points or more on conditional faults | Med |
| E09.08-U10 | Does the agent raise false alarms on correct code, and does a verification step cut them? | A false-alarm check for "no bug here" cases | G | K13, K22 (b15, d17); 59.3% on clean bags; older models | Plain vs verify-before-claim on correct programs mixed with buggy; false-alarm rate | False alarms fall by 20 points or more at no loss of detection above 2 points | High |
| E09.08-U11 | Do current models still give 40% false issues on help requests? | Updates the baseline rate (no schema change unless high) | G2 | K01, K22 (c01, c02, d17); only 2022-23 models | Re-run Hellas-style items with our model; false-issue and all-issues rates | Rate above 20% means U2 and U10 stay High | Med |
| E09.08-U12 | Is error-type description in the prompt a general gain? | Short list of fault types shown in S2 | S2 | K18 (d19); GPT-3.5, 86 programs; classification only | Plain vs fault-type list; classification and fix rate | Fix rate up 5 points or more on a current model | Low |
| E09.08-U13 | Does a confidence-vs-outcome check cut overconfidence on hard bugs? | Per-class calibration in memory | S9 / memory | K07 (b12, b22); human, correlational, N=21 | Log stated confidence vs pass; with and without a per-class calibration line | Brier score improves by 10% or more | Low |

## Open questions we cannot test on our bench yet

- Murphy 2008 and Fitzgerald 2008 strategy counts: need library copies. Until then we cannot build a list of human bad strategies to block.
- Per-misconception counts from Qian and Lehman 2017 and McCauley 2008: needed to build a seeded misconception set with realistic frequencies.
- Long-term retention with current tools: our bench has no learner, so only the agent analogue (scaffold-off regression) is testable.
- Human learning outcomes of any scaffold: need real novices.
- A trusted judge for Socratic or explanation quality: LLM judges agreed with a human 76.7% (trajectories) and 96.6% (turns); need a code-checked outcome instead.
- Leakage control: Codeflaws (19.7%) versus Condefects (62.0%) suggests contamination or difficulty; need a closed, freshly made bug set.
- Replication of the scaffold-initiation effect in agents: needs an uncertainty signal we trust.

## Order to run

1. U8 (staged vs free-form by model class): cheapest, decides whether any staged scaffold is worth its tokens for our model.
2. U2 (independent validator): the strongest prior effect (precision about 60% to about 95%) and the easiest to implement with code.
3. U10 (false alarms on correct code): one extra arm on the same items, and false alarms are the most repeated LLM failure in this subfield.
