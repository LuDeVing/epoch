# Active inference decision theory: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B03.03-U1 | Does code-ranked EIG (split entropy) beat the LLM simply choosing the most discriminating test from the same candidates? | Rank candidate tests by split entropy in code; skip zero-split tests | S7 | K11, K28 established vs weak baselines only; no equal-token control (b14, d08, c13) | A: LLM picks; B: code ranks; C: random; D: best-of-N. Rule-induction items with 3-8 candidate tests; solved per 1k tokens | B beats A by >= 3 points at equal tokens, CI excludes 0, and beats C | High |
| B03.03-U2 | Does filtering sampled hypotheses for consistency with all evidence help? | Code filter before any scoring or voting | G5 / S7 / S8 | K15 single-source (c14, c16), 20 Questions only | With vs without filter; same items as U1; accuracy and share of contradicting hypotheses | Accuracy +2 points or more and contradicting share falls by half | High |
| B03.03-U3 | Does conditioning the next step on the test result matter more than the test choice? | Make S8/S5 consume the test result explicitly (marginalise over remaining hypotheses) | S8 / S5 | K13 single-source (b21): question choice alone +0.021 to +0.026 F1 | EIG test then continue unchanged vs EIG test then condition on the result; multi-step items | Conditioned arm >= 3 points higher | High |
| B03.03-U4 | Does a prompt-only stop rule (test only if expected info per token > threshold) beat fixed test budgets? | Information-per-token stop rule | S7 / S6 | K27 (d04 theory, d02 threshold 0.01 and Kmax=2 on synthetic tasks, d10 trained) | Fixed 1/2/4 tests vs threshold; equal mean tokens; accuracy | Threshold arm matches the best fixed arm with >= 15% fewer tokens | High |
| B03.03-U5 | Is a free LLM choice of the discriminating test worse than explicit search on logic/planning-like items? | Derive the test by search over constraints in code | S7 / G5 | K24 single-source (d07): LLM under 50% vs BFS 99.8% at depth 10 | LLM free choice vs code BFS vs EIG over candidates; underspecified logic/planning items; share correct | Code arm >= 15 points higher on logic/planning | Med |
| B03.03-U6 | Which likelihood estimator is best: sampling, logprob, LLM judge, answer entropy? | Use the best cheap estimator | S7 | K17 single-source (b19: logprob worst); K16 (c15) | Tables with known answers; rank agreement with oracle EIG; downstream accuracy at equal tokens | An estimator within 90% of oracle gain at <= half the tokens of the next best | Med |
| B03.03-U7 | Does weighting tests by relevance to the final checker help, and what is the pragmatic weight? | w_p term in test score; weight default | S7 | K23 (d02, hand-set weights, synthetic), K05, K07 (b04, b07) | w_p in {0, 0.25, 0.5, 1}; items with a checker; solve rate and share of tests on unchecked aspects | Inverted-U with the best w_p beating w_p = 0 by >= 3 points | Med |
| B03.03-U8 | Do gains differ for enumerated vs open hypothesis sets? | A mode switch in S0: use EIG for enumerated sets, plain choice for open ones | S0 / S7 | K12 established (c12, c20), but mixed with set size | Stratify U1 items by enumerability; compare gains | Stratum gaps of >= 5 points either way | Med |
| B03.03-U9 | Is one-step EIG enough, or does 2-3 step pruned lookahead pay? | Two-step lookahead at S7 for interacting tests | S7 | K03: theory (a15), UoT says one step captures most (b18); no LLM test | 1-step vs 2-step (pruned) at equal tokens; items with interacting tests | 2-step beats 1-step by >= 3 points at equal tokens | Low |
| B03.03-U10 | Does probability gain rank tests better than Shannon EIG? | Switch the ranking measure | S7 | K25 single-source, human, abstract only (d13) | Same candidate sets; ranking disagreement rate; accuracy for each | Disagreement above 10% and one measure wins by >= 3 points | Low |
| B03.03-U11 | Does more chain-of-thought hurt under high meta-uncertainty, and does a take-the-best stop help? | Cue-count cap on thinking when uncertainty is high | G11 | K20 single-source preprint (c26): -17.3 points, CI [7.7, 25.5] | Replicate on our items: short vs long reasoning split by estimated meta-uncertainty | Long arm loses >= 5 points on the high-uncertainty stratum | Med |
| B03.03-U12 | Does a decaying epistemic weight (explore early, exploit later) help across a stream of problems? | Epistemic weight schedule in memory / class record | S6 / memory | K09, K10 single-source (c05, a08, a25, d03); simulation only | Fixed vs decaying weight over a stream of classes with a mid-stream shift | Decaying arm better after the shift by >= 3 points without loss before it | Low |
| B03.03-U13 | Does hypothesis-level gain (rules, not only answers) beat answer-level ranking in LLM tasks? | Rank by split of rules rather than of outputs | S7 | K26 (d17, d15) simulation only | Rank by rule-set split vs by answer split; ARC-like items | Rule-level arm >= 3 points higher | Med |

## Open questions we cannot test on our bench yet

- Human or animal data that separates EFE from "reward plus plain EIG": needs a purpose-built behavioural experiment. Existing studies fit any two-term model. Not testable by us.
- Whether the EFE form itself (not just EIG) adds anything in LLM agents: PUMA and Dutta are confounded. Needs a paper that holds the world model fixed and swaps EFE for plain EIG; we could run a small version with U7 once U1 passes.
- Friston 2015 numbers: the paper was not opened. Unblock by obtaining the full text; low value for the schema.
- Replication of Bogdan 2026 by an independent group: we can only run U11 on our own items.
- UoT headline basis (relative vs points): unblock by reading its tables or contacting the authors.
- Gap searches for equal-token comparisons, estimator comparisons and lookahead were blocked by API rate limits (HTTP 429). Re-run the search when the APIs recover; papers may already exist.
- Deep-network active inference: contested (Champion vs Tschantz/Fountas); irrelevant to a scaffold, so no test planned.

## Order to run

1. **U1 (EIG-ranked vs LLM-chosen test, with random and best-of-N controls).** It decides whether the core S7 idea pays at equal tokens. Everything else builds on it.
2. **U2 (hypothesis filter).** Cheap code-only change, and the most likely estimator problem (c14, c16) to damage U1.
3. **U3 (condition the next step on the result).** Cheap to run on the same items; Grand's result suggests choice alone gives little.
