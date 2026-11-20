# Search theory: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C12.10-U1 | Does ordering checks by p*a/c beat a fixed order when check costs differ? | Index-ordered check selection, computed in code | O (what to check next) | K01; a03, d01; single-source, simulation only; no LLM-agent test | Synthetic hypothesis tasks (30 items, 6-10 hypotheses, cost spread 1x-10x); fixed vs random vs p*a/c order; mean tokens to find target, success within budget | Mean cost down by 15% or more with success not lower, on at least 2 task types | High |
| C12.10-U2 | Does window-agreement stopping replace fixed-N voting on our items at equal accuracy? | Agreement stop with minimum sample count | G12 / O sample-and-vote | K07; a20, d08; established on math, older models | 100+ single-answer items; fixed N vs window (w 4-8) vs Bayesian stop; accuracy per 1,000 tokens | Accuracy within 1 point of fixed N at 25% or more fewer tokens | High |
| C12.10-U3 | Does a pilot-agreement signal predict who benefits from extra samples, net of pilot cost? | Adaptive per-item budget in S0 | S0 / G12 | K09, K20; d10, d11; probe needs hidden states, Snell bins lose gains at high budgets | Mixed-difficulty items; uniform vs pilot-adaptive budget; accuracy at equal total tokens with pilot charged | Beats uniform by 2 points or more, pilot included | High |
| C12.10-U4 | Do external per-option summaries plus an explicit explore line fix lock-in on our agent and model? | Code-built option summaries in the prompt | O / external state | K05; a18, c10, d04; older models only | Bandit and search tasks (5-20 options); raw history vs summary vs summary plus explore; regret, suffix-failure rate | Suffix failures halved and regret not worse | High |
| C12.10-U5 | Is agreement stopping safer than confidence stopping where the model is confidently wrong? | Rule: agreement first, confidence only with a checker | G10 / G4 | K16; d06-d08; established on math only | Items with a known confidently-wrong subset; agreement vs token-confidence vs trial-answer stop; accuracy per token, error on wrong-confident items | Agreement loses less than 1 point and confidence rule loses 2 or more on wrong-confident items | Med |
| C12.10-U6 | Does a Pandora-style stopper beat a tuned fixed N when a verifier exists? | Weitzman stopper for verifiable sampling | G12 | K07; b18, c04, d14; single-source, small open models, reward-model proxy | Verifier-checked items; tuned best N vs stopper; verified accuracy at equal tokens | 10% or more fewer tokens at equal accuracy over the tuned N | Med |
| C12.10-U7 | Does a marginal-yield rule for abandoning a branch beat fixed depth? | Abandon rule using code-checked progress | G1 / S control | K12, K17; a17, d02; no LLM test; Gittins on PRM failed | Multi-branch reasoning items; fixed depth vs yield rule (progress measured by checks passed, not self-score); accuracy per token | Beats fixed depth by 2 points or more at equal tokens | Med |
| C12.10-U8 | Does early exit by trial answer (DEER style) work at equal tokens against a hard cap? | Trial-answer check at transitions | G11 | K07, K16; d09; baseline was unrestricted reasoning | Reasoning items; fixed cap vs trial-answer exit at same mean tokens; accuracy | Accuracy up 1 point or more at equal mean tokens | Med |
| C12.10-U9 | Does forcing "explain why this is optimal" fix stop and switch timing? | Explain-then-decide step for stop decisions | G | K06; b17, c03; single preliminary workshop paper, numbers unverified | Fuse-or-extract game (4 conditions); direct vs formula plus example vs forced explain; distance of switch step from optimum | Mean distance down by one step or more in 3 of 4 conditions | Med |
| C12.10-U10 | Does memory of past stopping thresholds help across tasks? | Threshold memory in the agent log | memory | K03; b11, b12; human-only, single source | Repeated search tasks with fixed hidden distribution; no memory vs memory; win rate over games 1-10 | Win rate within 10 points of optimum by game 4, and above no-memory | Low |
| C12.10-U11 | How much does the independence assumption cost on real hypothesis sets? | A rule for when to switch to fixed order | O | K18; d12, d13; theory only | Hypothesis sets with known correlation (0, 0.3, 0.6); independent index vs fixed order plus adaptive stop; cost to find target | Switch rule added only if the index loses at correlation 0.3 or more | Low |
| C12.10-U12 | Does threshold escalation from cheap to expensive model beat fixed routing? | Escalation threshold | G | K15; c13, c14; small real-LLM tests | Items answerable by both models; always-cheap vs fixed routing vs threshold; accuracy per cost | 10% or more better accuracy per cost than fixed routing | Low |
| C12.10-U13 | Do LLMs show human-like under-search on McCall tasks, and in which direction? | A calibration correction to stop decisions | G | K19; d15; no study exists | McCall job-search task, LLM subjects; direct play vs reservation rule shown; regret against optimum | Same-sign bias in 3 of 4 settings, correctable by a fixed offset | Low |
| C12.10-U14 | Does progressive stopping beat a single-threshold rule for committing to a candidate? | Progressive commit rule | G | K04; b13, b14; contested, simulation only | Candidate-sequence tasks with several thresholds; single vs progressive; success rate | Progressive wins by 5 points or more | Low |

## Open questions we cannot test on our bench yet

- Stopping with no reward model on open-ended tasks. Missing: a task type with an acceptance signal that is not a checker. Unblock: a human-rated or rubric-graded set of 50 open items.
- Zhang and Zhao replication on current frontier models. Missing: the paper was not located again and its numbers are unverified. Unblock: re-find the PDF or rebuild the game from its description (U9 does this).
- Hidden-state difficulty probes. Missing: hidden-state access for API-only models. Unblock: an open-weight model run.
- Length-incentivised RL for exploration. Missing: training, outside scope.
- Primary texts for Koopman, Weitzman, Schotter and Braunstein, Brown et al. (2011). Missing: opened sources. Unblock: library access; low value for the schema.
- Effect of correlated hypotheses in real LLM use. Missing: a measure of correlation for LLM hypothesis sets. Unblock: U11 with synthetic sets first.

## Order to run

1. C12.10-U2 (agreement stop vs fixed N): cheapest, best-supported, and gives the baseline for U5, U6 and U8.
2. C12.10-U4 (external option summaries plus explore line): known failure mode, cheap to build in code, and gives a clear regret metric.
3. C12.10-U1 (p*a/c check ordering): the only direct use of Koopman-style search, untested on LLM agents, and a synthetic task is cheap.
