# Bayesian conditionalization: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D02.01-U1 | Does code normalisation of an LLM's raw option scores beat its own stated distribution? | Always normalise option scores in code; log the raw sum | G5/S7 | K16; d01, d02: human-only (N=50, one case); no LLM study | Same outputs, two readouts: raw vs divided by sum. 200+ exclusive-answer items. Metric: Brier, accuracy, split by items with sum off 1 by over 0.2 | Brier drops 0.01 or more on off-sum items, no loss elsewhere, paired CI excludes 0 | High |
| D02.01-U2 | Hard zero vs floor for "ruled out" options | Floor (about 0.02) plus revive rule in S7 | S7 | K20; d11, d12: single-source, 2023 models, 2-choice; no head-to-head | Hard zero vs floor 0.02, with 0%, 10%, 20% injected wrong "ruled out" calls. Metric: gold-zeroed rate, accuracy | Floor arm accuracy higher by 2 points or more at 10% noise and no worse at 0% | High |
| D02.01-U3 | Code posterior from model likelihood labels vs model-stated posterior | Model gives likelihood labels; code multiplies and normalises | S7 | K10, K18, K22; b10, d07, d08, b14, d15: contested, small N, mostly 26-35B models | A: model posterior. B: code from labels. C: code from oracle labels. Checkable-likelihood tasks (20Q, forecasts). Metric: accuracy and Brier against truth | B beats A by 3 points accuracy or 0.02 Brier on 2 of 3 task sets | High |
| D02.01-U4 | Does a sequential (per-clue) code posterior beat batch on accuracy? | Per-clue update loop in S7 | S7 | K10; b10, d06, d07: contested (consistency better, accuracy not) | Per-clue vs all-at-once, same code posterior. Metric: accuracy, AUROC, ECE | Sequential accuracy higher by 2 points or more, CI above 0 | Med |
| D02.01-U5 | Position and label bias on the target frontier model; does permutation averaging help? | Cyclic order averaging (or PriDe) in S7 | S7 | K23; d13, d14: 2023 models only | 200 MC items, gold evenly at A-D. Arms: fixed order; mean over 4 cyclic orders; one order with 4x samples. Metric: accuracy by gold position | Position gap over 2 points and permutation arm beats equal-token fixed arm by 1 point or more | Med |
| D02.01-U6 | Are verbalised likelihoods P(E\|H) good enough to update on? | Two-sample elicitation with a disagreement flag | S7 (likelihood step) | K21; d07, d16: single-source; no direct calibration study | Elicit label twice at temperature above 0; compare to oracle labels. Arms: one sample; mean of two; mean of two plus flag. Metric: wrong-direction update rate, final accuracy | Wrong-direction rate falls 20% relative or more at under 1.5x tokens | High |
| D02.01-U7 | Natural-count restatement on 2025-26 models | Count form in S2/O6 for base-rate and test problems | S2/O6 | K06; d03, b19, d05: contested in humans, 2023 LLMs | 60 problems x 3 rewordings; probabilities vs counts out of N. Metric: exact correctness, stability | Counts arm higher by 5 points or more on single-test problems and no worse on sequential | Low |
| D02.01-U8 | Does a numeric prior in the prompt move a frontier model as Bayes predicts? | Rule: keep priors in code, or trust the prompt prior | G5 | K25; d18, b07: models up to 8B only | Coin/die tasks, stated bias, n flips. Prompt prior vs code prior. Metric: total variation distance to Bayes posterior | Prompt arm within 0.05 of code arm (then allow); otherwise keep priors in code | Med |
| D02.01-U9 | Jeffrey update using the model's stated confidence in a check | Reliability-weighted update for noisy checks | G5/S7 | K27; a06: no LLM study | Hard condition vs Jeffrey shift with a flaky tool at 80% accuracy. Metric: Brier, gold-zeroed rate | Jeffrey arm Brier lower by 0.02 or more | Med |
| D02.01-U10 | Vote over N samples vs explicit normalised probability, current models | Choose vote or normalised probability for S7 aggregation | S7 | K13; d10: single 2022 paper; tie within 0.3 on PaLM-540B | 8 samples voted vs 8 verbalised distributions averaged vs one long chain. Metric: accuracy | Differ by 1 point or more with CI above 0; else keep vote (cheaper) | Low |
| D02.01-U11 | Does the agent reseed when the true answer is missing from the candidate set? | Reseed rule when all candidates fail checks (S7 back to S3) | S3/S7 | K02; a08: philosophy only | Items with gold removed from the initial candidates. Renormalise over stale set vs reseed on total failure. Metric: gold-in-set rate, accuracy | Reseed arm recovers gold on 10% or more of such items | Med |
| D02.01-U12 | Is a probability-ranked differential role useful by itself? | A differential-keeping role in S7 | S7 | K26; d17: 81.9% vs 78.6%, not ablated | Same scaffold with and without the role. Metric: accuracy, cost per item | Role adds 2 points or more at equal cost | Low |
| D02.01-U13 | Is the error rate of "ruled out" calls lower when the check is code-run than when the model judges? | Prefer code-run elimination; model-judged elimination only as soft weight | S4/S7 | K20; d11: model-judged only, 2023 models | Same candidates; elimination by code check vs by model judgment. Metric: wrong-zero rate | Model-judged wrong-zero rate at least 2x the code-run rate | Med |

## Open questions we cannot test on our bench yet

- Primary human sources are unread (Edwards 1968, Kahneman and Tversky 1973, Bar-Hillel 1980, Casscells 1978, Ramsey, de Finetti, Lewis, Teller). Unblock: read the originals. This only affects how we quote human numbers.
- Chen et al. 2026 and Filbry et al. 2026 have no independent replication. Unblock: run U3 and U4 on our items and report our own numbers.
- Likelihood quality P(E|H) has no calibration study. Unblock: U6 builds one, but needs an oracle likelihood source (a stronger model or computed ground truth).
- Frontier-model adversarial base-rate rewordings (after Binz and Schulz). Unblock: a rewording item set with computed Bayes answers.
- Whether per-evidence updating holds on real tasks where evidence is graded, not exact. Our bench items have checkable answers. Unblock: a task family with graded evidence.
- Bayesian teaching (fine-tuning) cannot be tested without training; out of scope for the scaffold.
- Whether the Bayesian role in scaffolds like MAI-DxO produces the gain. Unblock: a re-implementation with ablation.
- Open-mode tasks (no single right answer): the rule needs an exclusive candidate set. Unblock: a way to define candidate sets there.

## Order to run

1. D02.01-U1 (normalise vs raw): cheapest, needs only logging the raw sum, and tests the one human result G5 now rests on.
2. D02.01-U3 (code posterior from likelihood labels vs model posterior): largest expected gain, and the main conflict in the literature (consistency vs accuracy).
3. D02.01-U2 (hard zero vs floor with injected noise): decides whether the S7 elimination step is safe; the only data are 2023 models.
