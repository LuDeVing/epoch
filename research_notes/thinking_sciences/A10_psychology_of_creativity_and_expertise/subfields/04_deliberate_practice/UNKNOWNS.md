# Deliberate practice: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A10.04-U1 | Does retry-with-rewrite against an external checker beat best-of-N at equal tokens? | Fixed S5 loop: located failure, one-line lesson, retry | S5 / S4 | K26, d10, d13; established but never token-matched; older models and games | (a) 4 independent attempts + code select; (b) attempt, rewrite, retry, same budget; ARC and BRAINTEASER items with a held-out check; pass rate on unfitted check | (b) beats (a) by 3+ points over 3 seeds, no loss on items with no gain | High |
| A10.04-U2 | At what checker false-positive rate does a retry loop fall below no loop? | A checker-quality gate: skip retries if checker is noisy | G3 / G7 | K27, d11 (16.3% FP on MBPP gave 0.80 to 0.77); single task family | Same items, checker verdicts flipped 0, 5, 15, 30%; retry loop vs best-of-N | Loop loses to best-of-N at some noise level below 30%; set gate at that level minus 5 | High |
| A10.04-U3 | Do distilled one-line lessons help beyond an instructions-only control? | Keep lessons memory (already planned) with a measured benefit | memory | K29, d08 (23.3 to 36.7 to 50.0); single run, 30-question sets; contested | Streams of 30-60 same-class items; arms none / rewritten instructions only / one-line lessons / raw trajectories; accuracy on items 20+ | Lessons beat instructions-only by 3+ points and beat raw trajectories | High |
| A10.04-U4 | Does memory plus extra samples compound where samples alone do not? | Use samples only with memory on same-class streams | memory / G12 | K28, d15 (WebArena 49.7 to 55.1 vs 39.0-42.2); single-source, web tasks | Same k, memory vs no memory vs vote aggregate on our items | Memory arm gains 3+ points more per added sample than no-memory arm | Med |
| A10.04-U5 | Does sub-goal order matter: easy-first, hard-first or random? | An ordering rule in the subgoal library | S6 / memory | K17, c08 (random curriculum -93%) vs d16 (hard-to-easy 0.81 vs 0.77); contested, different settings | Decomposable items with 3-4 sub-goals; four orderings; pass rate | One ordering beats random by 3+ points on two item sets | Med |
| A10.04-U6 | Does picking helper problems at mid solve rate help at inference time? | Probe-then-pick rule for helper problems at impasse | S6 | K15, c02, c03, d06; RL training only, not inference | Impasse items; helper at 0.3-0.7 solve rate vs random vs easiest; probe tokens counted | Net gain after probe cost of 3+ points | Med |
| A10.04-U7 | Does a step-level check beat a final-answer check as selector? | Step check in S4 or S7 when steps are code-verifiable | S4 / S7 | K19, c12 (78.2 vs 72.4 vs 69.6, human step labels); single-source, math | Multi-step items; step check, final check, both; pass rate and false-accept rate | Step check gains 3+ points at equal tokens with code-run steps | Med |
| A10.04-U8 | Should loop budget be routed by task predictability? | S0 field: stable or open; loops only on stable | S0 / G12 | K03, a13 (r .49 vs .21, human), d08, d16 (indirect); human-only | Mixed bench; loop always on vs loop only on stable; pass rate and tokens | Routing cuts tokens 20%+ with no loss, or gains 2+ points | Med |
| A10.04-U9 | Is there a memory size sweet spot? | A cap on lesson count | memory | d17 (abstract-level); single-source | Same stream, memory caps 5, 10, 20, all; accuracy | Intermediate cap beats full by 2+ points | Low |
| A10.04-U10 | Does mid-pass selection beat random selection with the same rollouts? | Evidence for U6; also tells us whether K15 is a selection effect | S6 | K15, d07 (argued not run; figures not inspected) | Controlled run: mid-pass items vs random items, same rollouts, same verifier (training-side or sampled stream) | Mid-pass wins by 2+ points | Low |
| A10.04-U11 | Do gains from loops hold on small models? | A model-size gate for loops | G7 / S0 | K27, d09, d14 (small models: little or negative); contested for ours | Run T1 on small and large model | Gain on large, none on small; then gate by model | Low |

## Open questions we cannot test on our bench yet
- Full-career reliability of recalled practice: needs long diary data nobody has. Human-only and not a schema issue.
- Range restriction at the elite level: needs an elite-only sample and a correction method. Not relevant to the agent.
- A fair token-matched comparison against published loops (EvoTest, Reflexion): needs their code run on our budget. Unblock by re-implementing the loops on our items (this is U1).
- Whether LLM tutor gains survive blinded outcomes: needs a human trial. Out of scope.
- Predictability as a moderator in LLM agents, tested directly: needs items labelled for predictability by someone other than us.
- Exact 2014 corrigendum figures: paywalled. No effect on the agent.

## Order to run
1. U1 (retry-with-rewrite vs best-of-N at equal tokens): the one gap that decides whether any within-session loop belongs in S5 beyond what we have.
2. U2 (checker-noise sweep): cheap, reuses U1 items, and sets the safety gate if U1 passes.
3. U3 (lessons vs instructions-only control): cheap, and settles whether memory gains are memory or better instructions.
