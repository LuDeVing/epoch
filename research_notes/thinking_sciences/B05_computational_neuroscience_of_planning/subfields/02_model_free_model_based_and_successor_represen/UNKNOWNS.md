# Model-free, model-based and successor representation: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B05.02-U1 | Does a class-transition memory (discounted next-class counts from past runs) beat no memory and raw traces? | Class-transition table in memory, shown after the first attempt | Memory (section 5) | K28, K32, K33; d08, d09 single-source, tokens not matched; no SR memory found in 42 queries | E1: 3 arms (none, raw trace of 3 runs, table); repeated classes with 2-3 variants; 5+ seeds; pass rate and tokens to first pass | Table beats none by 3+ points with the 95% interval above 0, and beats raw trace by 2+ points | High |
| B05.02-U2 | Does the table go stale and hurt when the operator mix or checker changes, and does a policy tag plus invalidation fix it? | Policy tag and invalidation rule as part of every memory record | Memory | K01, K05 (E in theory); a09, a20; no measured LLM case (K37) | E2: change operator mix mid-run; arms: tagged+invalidating, untagged, none; pass rate after change | Untagged falls 3+ points below tagged after the change | High |
| B05.02-U3 | Is one-step imagination of each candidate worth its tokens against reactive and small tree search? | Imagine-then-commit as a cheap lookahead at S3/S4 for planning items | Operator / S3 | K19, K20, K36; c16, c17 (23.6 vs 26.2 vs 17.6, not budget-matched); d14 trained only | E4: reactive, imagination, tree search at same tokens; Blocksworld and small tool tasks; success and invalid-move rate | Imagination beats reactive by 3+ points at equal tokens, and is within 3 points of search | High |
| B05.02-U4 | Does a code-side validity monitor (reject moves not in the graph) cut invalid moves and raise solves in our scaffold? | Monitor guardrail on planning items | Guardrail G | K18 single-source (31% invalid without monitor, MAP, GPT-4, Hanoi) | E7: scaffold with and without validator; graph and puzzle moves; invalid-move rate and solves | Invalid rate drops by 10+ points and solves rise by 2+ points | High |
| B05.02-U5 | Does surprise-ranked retry (notes ranked by gap between predicted and real check output) beat recency order? | Surprise ranking for retry notes in S5/S6 | S5/S6, memory | K11, K35; a15, a24 (human N=24, p=.049 on one contrast); d10 mixed; prioritised replay only in fine-tuning | E5: retry notes ranked by surprise, recency, none; items failing first attempt; pass rate on attempts 2-3 | Surprise beats recency by 2+ points on 2+ benchmarks | Med |
| B05.02-U6 | Is a payoff-aware plan gate (plan only in classes where planning has paid) better than always-plan or a draft-agreement gate? | Per-class payoff record read by S0; planning skipped where it did not pay | G12 / S0 | K06 (E in humans); K34 (AdaptThink trained, DART best-case, neither payoff-aware) | E6: always, never, payoff-gated, draft-agreement; mixed classes; pass rate and tokens | Gated arm within 1 point of always-plan using 30%+ fewer tokens | High |
| B05.02-U7 | Does step-back (restate structure first) beat plain and CoT on planning items? | Step-back in S1 for planning-type classes | S1 / O6 | K16 single-source (CogBench +118.59% vs CoT +64.59% on a regression index, 2024 models, not accuracy) | E8: plain, CoT, step-back; planning items; pass rate | Step-back beats plain by 2+ points and CoT by 1+ at equal tokens | Med |
| B05.02-U8 | Does explicit graph state in the prompt close the CogEval policy-revaluation gap for current models? | Code-held graph state (edges, visited) shown in S2 for graph-like items | S2 | K17, K30, K37; c07 (policy 0.21 GPT-4, 2023 models); no frontier re-run | E3: plain, graph-state scaffold, scaffold+replay; revaluation types; paired contrast | Policy revaluation up 0.15+ over plain; paired p<.05 | Med |
| B05.02-U9 | Does a cached strategy reused for a new goal help, or does it over-reuse when it should not (policy reuse)? | Strategy cache by class with mismatch check, successor-feature style | Memory | K13 (E in RL), K14 (human, second-hand) | Cached best-old-strategy plus refine, with and without mismatch check, versus fresh start; goal-changed variants; pass rate | Reuse beats fresh by 2+ points and mismatch check removes losses on changed goals | Med |
| B05.02-U10 | Is memory better as soft advice than as a forced plan? | Memory always shown as advice the agent may override | Memory | K33 single-source (ProPlay: hard constraint -4.8 points) | E10: advice vs forced plan, same memory | Advice beats forced by 3+ points | Low |
| B05.02-U11 | Are bottleneck states of the agent's own state graph useful subgoals? | Bottleneck detection (graph Laplacian) feeding O3 | State / O3 | K12; a12, c28 (simulation and small domains only) | Bottleneck vs random subgoals on multi-room or multi-stage tasks; solves | Bottleneck subgoals beat random by 3+ points | Low |
| B05.02-U12 | How stable is a single-run MB/MF label of the agent? | Rule: never route on a single-run mode score (a logging rule) | Logging | K10 (humans ICC .02-.52); K15; d15 rigidity not reliability | E9: 20 repeats of the same two-step prompt; variance of stay regression | Run-to-run SD of the interaction term is 30%+ of its mean; then routing by mode is dropped | Low |

## Open questions we cannot test on our bench yet

- Whether the human reward-over-transition asymmetry exists in LLMs. Needs a paired test on the Momennejad design with current models and enough runs per cell. CogEval's table has no per-cell n (d04).
- Whether a Kalman TD SR beats SR+MB on human data (gap 7). Needs human data; not our bench. Not needed for the schema either.
- Whether current frontier and reasoning models still fail revaluation. Needs access to the CogEval items. Part of U8.
- Exact Momennejad Exp 1 means (0.52 vs 0.45) and Exp 2 statistics. Needs the figures or source data.
- Feher da Silva and Hare numbers on a full-text check. Only the abstract was re-read.
- Whether in-context SR-like features (Demircan, Llama 70B, r=0.62) appear in the models we use. Needs open weights and an autoencoder; not in our bench.
- Whether training-time findings (random-walk training, latent learning, Dyna-Think, AdaptThink) have prompt-only equivalents. Needs matched-budget experiments that compare against trained models; out of scope while the agent is frozen.
- Whether the policy dependence of memory matters in practice for our classes, or whether the operator mix is stable enough that U2 shows nothing. Settled by the U2 result.

## Order to run

1. **B05.02-U1 with U2 (E1 + E2).** The central unmeasured claim; no SR-style memory has been tested in an LLM agent, and the staleness arm costs little on top of the same items.
2. **B05.02-U6 (payoff gate).** Directly saves tokens, matches G7 and G12, and the cost is bookkeeping. Established in humans, untested in LLMs.
3. **B05.02-U3 (imagination vs reactive vs search).** Largest likely accuracy gain on planning items, and the matched-budget comparison is missing in the literature. U4 can share the same items.
