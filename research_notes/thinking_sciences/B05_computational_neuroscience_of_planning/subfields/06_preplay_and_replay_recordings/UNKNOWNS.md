# Preplay and replay recordings: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B05.06-U1 | Does a pre-answer forward rollout of 2 to 4 candidate plans beat act-then-revise? | A conditional rollout operator before commit | O plan, S3 | K03 contested; a10, c03 (saturates near 15 rollouts, maze net); d15 (under 1% use, up to 5% loss); d16 not isolated | A act-then-revise; B 3 rollouts then act; C equal-token retry. 100+ ARC-like and multi-step items, 5 seeds; pass rate | B beats both A and C by at least 3 points with non-overlapping seed spread | High |
| B05.06-U2 | Does a backward walk from the failing output to the blamed step beat forward re-reading? | Backward-credit pass inside S5 with a replay-with-fix check | S5, G2 | K01 established in rats; K27 single-source; d13 is training-time; d14 blame accuracy about 20% | A forward re-read; B backward walk plus fix check; C retry. Items with a failed first attempt; fix rate in 2 rounds and localisation accuracy | B beats A by at least 3 points fix rate at equal tokens, and localisation above 40% | High |
| B05.06-U3 | Is a retry arm enough to explain memory and review gains in our setup? | A mandatory equal-token retry arm in every future test | G7 | K24 single-source (d12); d10 no-memory at least once in 8 is 73.6% | Rerun any existing memory or review feature against vanilla with extra steps; 3+ seeds | Feature kept only if it beats retry by at least 2 points | High |
| B05.06-U4 | Does idle-time precompute on notes help when the later query is not predictable? | Sleep-time precompute step with a predictability gate | M offline prep | K14 single-source (c07, d09); no zero-gain point measured; human-free, math tasks only | A all tokens at query time; B 30% on precompute. Question sets sharing a context, binned by predictability; accuracy per bin | B wins at equal total tokens in at least the top two bins; gate set where gain crosses zero | High |
| B05.06-U5 | Does a mode switch (plan at decision points, review in idle) beat one mixed pass? | Two separate passes with separate triggers | S, M | K21 single-source (d03: 62.26% vs 52.19%, 8 rats); K22 (d04, N=40); K03/K04 contested; rodent and human only | A mixed pass; B plan pass at decision points plus review pass in idle. Long multi-step tasks; pass rate and confident-error rate | B at least +2 points and confident-error rate not higher | Med |
| B05.06-U6 | Does value-and-recency ordered review beat random review? | Ordered review with age decay | O priority, M | K23 single-source; d05 gridworld; d18 RL training only (plain PER degrades); b12 | A random review; B Need-times-Gain proxy with age decay; C plain priority. Memory of 200+ past items; next-item accuracy | B beats A by at least 2 points, and C is not better than B | Med |
| B05.06-U7 | Does rule-bound cross-attempt merge beat append-only or free rewrite? | Add-and-delete merge with applicability conditions | S5, M | K25 single-source (d10: 72.90 vs 70.10 vs 54.57; one harness) | A append-only; B compare then add-and-delete; C free rewrite; D retry. Repeated tasks over rounds | B beats A and D by at least 2 points, and decay seen in A | Med |
| B05.06-U8 | Does pre-solving nearby problem variants help on language tasks? | Counterfactual pre-solve with reuse | O precompute | K29 single-source (d08: 97.74% vs 5.56% in grid worlds; human reuse 62.39%) | A solve asked variant only; B spend spare tokens on 2 neighbours first. Families of near variants; accuracy and reuse rate | B beats A by at least 3 points when query is a neighbour and does not lose otherwise | Med |
| B05.06-U9 | Does stating the goal first improve rollouts only for goal-relevant branches? | Goal-first framing in S1 for branching tasks | G goal framing | K08 single-source (a14: cued 7.37% vs uncued 4.41%, 4 rats) | A goal last; B goal first. Branching tasks with relevant and irrelevant branches | Gain on relevant branches of at least 3 points and no loss on others | Low |
| B05.06-U10 | Does an idle review that re-reads preferred answers raise confident error? | A guard: idle review must include a challenge item | G entrenchment | K22 single-source (d04, human MEG) | A review of own best answers; B review including a counterexample search. Items with a wrong preferred answer; confident-error rate | B lowers confident error by at least 3 points without lowering accuracy | Low |
| B05.06-U11 | Does relabelling a failed attempt as a solution to the sub-goal it reached help? | Hindsight relabel into memory | O revise | K18 single-source; c10 needs goal-conditioned set-ups, robot tasks | A discard failures; B store failure with reached sub-goal. Decomposable tasks; later success | B beats A by at least 3 points | Low |
| B05.06-U12 | Do chained rollouts with fixed total tokens beat several short independent rollouts? | A rollout-depth rule | O rollout depth | K10 single-source (a03: 19% of events over 250 ms) | A one long chain; B several short rollouts; same tokens. Multi-step planning items | Whichever wins by 3 points sets the default depth | Low |
| B05.06-U13 | Does a shuffled or mutated-input null for candidate scores reduce false selections? | Null-comparison step in S7 | G3, G5 | K06 and K09 (decoder and template choice flip effects, b02, b04, b10); human-free, from neuroscience method | A score alone; B score minus score on mutated input. Candidate sets with known right answer; selection precision | B raises precision by at least 3 points | Med |

## Open questions we cannot test on our bench yet

- Foster and Wilson 2006 and Foster 2017 numbers: need library access to the Nature paper and the Annual Review.
- Independent hippocampal preplay replication (2023-2026): Shin and Jadhav W-track data not opened. A direct test of whether preplay exists is a neuroscience question, not a bench test. Unblock by reading the data papers or contacting the labs.
- Which task features decide plan vs memory replay beyond engagement. Needs more recordings; no bench analogue.
- Whether the Hajimiri equal-token result survives tuned memory baselines. Needs the full paper critique and a rerun.
- CogEval on current models with an explicit edge list. Needs the CogEval task set and our current models.
- Whether the 2025 Dragoi paper's author list and title are one paper. Check the publisher record.
- Blame-assignment ability of current frontier models (AgenTracer numbers are 2025 models). Needs a rerun on the Who&When set.

## Order to run

1. **B05.06-U3 (retry arm control).** Cheapest, and it protects every later result from the equal-token trap.
2. **B05.06-U2 (backward walk vs forward re-read).** Highest expected gain; backward credit has the strongest biological and training-time support and no inference-time test.
3. **B05.06-U1 (forward rollout vs act-then-revise).** The other half of the forward and backward split; tells us whether a rollout operator is worth its tokens given the under-use and misuse seen in d15.
