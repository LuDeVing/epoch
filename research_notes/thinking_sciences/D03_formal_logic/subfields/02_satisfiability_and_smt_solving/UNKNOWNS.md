# Satisfiability and SMT solving: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D03.02-U1 | Does spec-then-solve still beat extended thinking for current reasoning models, at equal tokens? | Solver tool offered in S4 for crisp-constraint classes | S4, O (tool) | K26, K27 (d01, d02); single-source, 2026, different task; older models only on ZebraLogic/SATBench | Thinking only vs spec + solver vs thinking + free tool; 60 hard puzzles (ZebraLogic large/x-large, SATBench hard UNSAT); accuracy and cost per correct | Solver arm beats thinking-only by 10+ points at same tokens (McNemar p < 0.05) | High |
| D03.02-U2 | Does a code checker as best-of-N selector close the oracle gap that majority vote leaves? | Checker-filtered selection in S7 instead of voting | S7, G5 | K11 (b13, d09); single-source; oracle used gold answer, not code | Majority of N vs checker-filtered N vs model verify; 100 puzzles with codable clues or witness-checkable SAT items | Checker arm recovers over 50% of the oracle-minus-majority gap | High |
| D03.02-U3 | Which cheap check catches a silently wrong formalisation? | One named check in S8 for solver-based answers | S8, G | K18, K33 (d12, d13, b08); unmeasured for model-written specs | 20 seeded dropped-constraint problems + 20 clean; arms: none, plug-in, round trip, second translation, premise list; detection and false alarm rate | Detects 60%+ of seeded drops with under 10% false alarms, and costs under 30% extra tokens | High |
| D03.02-U4 | Does requiring a code-checked witness cut SAT-bias and wrong SAT claims? | Witness requirement as a guardrail wording | G2, G10, S8 | K29 (d04, d11, a23); gap persists with tools (13-21 pp); no clean A/B | Plain vs reminder prompt vs witness required vs both; 60 SAT/UNSAT items; SAT-bias rate and verified accuracy | Verified accuracy up 5+ points or bias errors down by a third | High |
| D03.02-U5 | Can a three-question crispness gate route items between solver and thinking? | Gate rule in S0 | S0 | K17, K32 (d08, d14, b17); mis-routing costs 50+ points; no gate measured | Always-solver vs always-think vs gate; 40 mixed crisp/fuzzy items; accuracy per type | Gate within 3 points of the better fixed arm on each type | High |
| D03.02-U6 | Does solver counterexample search pick between two fitting rules better than random tests? | Solver step in S7 where rules are solver-readable | S7 | None direct; extrapolated from a27, d04; no source | Random inputs vs enumerated vs solver "A != B"; 30 ARC-like rule pairs; discriminating inputs found per call | Solver finds a discriminating input in 20+ points more pairs than random at same calls | Med |
| D03.02-U7 | Does an unsat core in the repair prompt beat generic retry? | Core-guided repair in S5 | S5 | K08 (c23); 12 queries only | Retry with error vs with core vs core + original; 40 items returning UNSAT first time; repair rate in 2 rounds | Core arm repairs 10+ points more | Med |
| D03.02-U8 | Which tool language does the agent write most reliably: Z3Py, CP-SAT, or brute force? | Fixed tool choice in the O (tool) definition | O (tool) | K19, K31 (c31, d06, d08); no Z3Py comparison; models avoid z3 when free | Same 20 puzzles per language; executable rate and accuracy | One language wins accuracy by 5+ points and has executable rate above 85% | Med |
| D03.02-U9 | What is the best round cap and fall-back for the solver loop? | Round cap (4 or 8) and forced submit in S5 | S5, G6, G7 | K28 (d03); single-source; up to 37 pp swing | 4 vs 8 rounds, with and without forced submit; 60 hard items | Pick the cap with best accuracy per token; add forced submit if it rescues 5+ points | Med |
| D03.02-U10 | Does solver time class work as a coarse budget class? | Budget bucket by solver time in S0/G12 | G12 | K13, K30 (d05, d10); r about -0.15 within hard sets; token link only for o1-class | Fixed budget vs bucketed budget; 100 puzzles; accuracy per token | Bucketed arm beats fixed by 3+ points per token | Low |
| D03.02-U11 | Does the solver stack with 5-way voting in a way that pays for the extra tokens? | Vote over solver outputs in S7 | S7 | K22 (b06); single-source, code-davinci era | Solver x1 vs solver + 5-way vote; 100 items; accuracy per token | Gain over solver x1 exceeds 5 points at under 3x tokens | Low |
| D03.02-U12 | Does propose-and-verify with a sound checker beat model-only or verifier-only? | Model proposes, code verifies, as default for checkable classes | S3, S4 | K15 (a27, b18, c24); single-source, weak baselines | Model-only vs verifier-only vs propose + verify; 40 verification tasks; solved count and proposals per solved | Beats best single arm by 10+ points within 8 proposals | Med |
| D03.02-U13 | Does LLM accuracy fall near clause ratio 4.3 (can ratio set difficulty class)? | Ratio-based difficulty class for test sets | S0, G12 | K01 holds for solvers (a01, a04, a06); untested for LLMs; SATBench varies clauses only | Random 3-SAT at ratios 3.0, 4.3, 6.0, same variable count; accuracy with and without solver tool | LLM accuracy dips at 4.3 by 10+ points in the no-tool arm | Low |
| D03.02-U14 | Does step-level SMT checking of a reasoning trace beat checking the final answer? | Step-checker in S4 for formal traces | S4 | K25 (b19, d13); single-source, tables unclear | End-answer check vs step-level check; 40 traces with seeded step errors; error found rate and tokens | Finds 20+ points more seeded errors at under 2x tokens | Low |

## Open questions we cannot test on our bench yet

- Fine-tuned solver imitation (LoGiPT-style, K23): needs training, out of scope.
- Large equal-budget curves for spec-then-solve vs thinking across many model sizes: needs a wide model sweep and a shared token meter. Unblock with a bench run across at least three models.
- Whether results from MathConstraint (SAT/UNSAT with witness, 329 items) transfer to our tasks: needs the dataset or a close copy.
- Real human-written logic at scale (FOLIO-like) with a paired McNemar test on one fixed split: needs a licensed copy and consistent prompts, to settle K06.
- Correctness of the solver itself (K24, Fuzz4All): a cross-check with a second solver is possible later, but low value now.
- Counterexample search on arbitrary Python rules: program equivalence is undecidable. Unblock only if ARC rules are expressed in a restricted DSL.
- LLM-Modulo style claims: original figures were not found in the position paper; needs the cited primary papers.

## Order to run

1. D03.02-U1 (solver vs thinking at equal tokens): decides whether the whole solver path is worth a place in S4 for modern models.
2. D03.02-U3 plus U4 (wrong-formalisation checks and witness requirement, one shared item set): the main risk of the solver path is a confident wrong answer; this finds the cheap guard.
3. D03.02-U2 (code checker as best-of-N selector): the largest measured gap in the evidence (oracle 60.3 to 69.1 vs vote 38.0) and the cheapest to run.
