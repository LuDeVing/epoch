# SAT solving, DPLL: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C06.02-U1 | Does code-run unit propagation plus a verified decide/backtrack trace beat plain CoT on SAT-like items? | "Propagate" forced-move step before any guess | S4 / new O | K02, K19, a16: single-source, theory and trained models only; no LLM study (d15) | Plain / CoT / best-of-N / scaffold; random 3-SAT n 25-50, alpha 4.27, with one-edit twins; 60 pairs; ADR | scaffold ADR at least +10 points over CoT at equal tokens, 2 seeds | High |
| C06.02-U2 | Does forced assignment substitution cut the satisfiability bias in a fresh run? | Mandatory substitution check before any SAT/valid answer | S8 / G3 | K12, K14: SATBench re-evaluation only (60.4%, selection effect) | With vs without substitution check; SATBench hard plus own items; false-SAT rate, trace validity | false-SAT rate down 30% relative and no accuracy loss on SAT side | High |
| C06.02-U3 | Do current models gain from translate-then-solve per token on our formalisable puzzles? | Tool delegation operator with a solver | O | K07, K08: contested; old-model gain, under 1% on near-ceiling sets for 2025 models, better at depth (76.7 vs 62.2) | Direct / always-solver / routed; depth 10-17 puzzles; accuracy including translation tokens | solver or router beats direct by 5+ points at depth, no loss on easy | High |
| C06.02-U4 | How often does translation to constraints fail or drift on our problems? | Faithfulness check on formalisation (second independent translation, compare solutions) | S2 / O | K07, K25: single-source (d04, d05), legal NLI | Two independent translations; count disagreement; 50 own items; faithful-formalisation rate | disagreement check catches 70%+ of wrong formalisations | High |
| C06.02-U5 | Does requiring executed tool output (no narrated solver run) change answers? | Rule: solver claims need real tool output in the log | G10 / O | K25: single-source, 15.3-52.5% scope laundering | Narrated vs executed prompt on same items; disagreement rate | disagreement 10%+ and executed arm more accurate | Med |
| C06.02-U6 | Is hard-UNSAT loss a budget effect fixable by a stop-and-delegate rule? | Budget-fraction trigger to delegate or answer best-so-far | S6 / G12 | K23: single-source, one model family (d02) | Budgets 8k/16k/32k; plain vs stop at 50% budget; accuracy and cap-hit rate | accuracy at 16k within 5 points of 32k | Med |
| C06.02-U7 | Does naming failure modes (SAT bias, early stop, fake solver call) help in a fresh run? | One-line failure-mode note in scaffold | G | K14: single-source, re-evaluation only | With vs without note, SATBench hard; fresh accuracy | +3 points fresh, no harm on SAT items | Med |
| C06.02-U8 | Can a cheap LBD-like score pick which lessons to keep? | Lesson retention by reuse score | memory | K03: human solver only (a07), no LLM test | Keep-all / LBD-like / random keep at equal context; 30 related problems; accuracy | beats random keep by 3+ points at equal context | Med |
| C06.02-U9 | Do paired-twin items (relabel, one-edit twin) expose shortcuts in our agent? | Twin items as a standing test and log field | S4 test design / S9 | K13, K24: single-source | Plain vs scaffold on twins; accuracy gap and pair accuracy | scaffold gap at most half of plain gap | Med |
| C06.02-U10 | Does a checkable certificate for "no solution" claims raise UNSAT accuracy? | Certificate-or-abstain for negative claims | G3 / S8 | K04: single-source (human-built SAT proof); no LLM study (gap 9) | Proof-style output plus code checker vs plain; hard UNSAT items; accuracy with abstains counted wrong | UNSAT accuracy +10 points | Med |
| C06.02-U11 | Do reasoning models do DPLL or greedy local search, and does that change the scaffold? | Pick propagation scaffold or restart sampling per model | S3 / S4 | K05, K06, d10: qualitative only, older models | Audit 100 traces: count backtracks, propagations, flips | under 20% of traces show real backtracking (then use code propagation) | Low |
| C06.02-U12 | Does extra thinking allocated by difficulty pay (R1 behaviour)? | Difficulty-scaled reasoning cap | G11 / G12 | K06: single-source, R1 only | Fixed cap vs difficulty-scaled cap at equal total tokens | +4 points at equal total | Low |
| C06.02-U13 | Do evolved prompts hold up on held-out families? | Train/validation/test rule in the outer loop | G7 | K20, K27: held-out gain 1-2% vs 36.6% on train | Evolve on A, test on B; add an equal-budget tuning baseline | held-out gain at least half of train gain and above the tuning baseline | Low |

## Open questions we cannot test on our bench yet

- Structured industrial-style instances: no LLM study exists and we have no generator of such items. Unblock: borrow SAT-competition families and encode small ones as puzzles.
- Accuracy per token for SatLM-style pipelines on LSAT, BoardgameQA and GSM-SYS: needs those datasets and token accounting; no paper reports it.
- Size sweep for R1, o4-mini and GPT-5 at a fixed generous budget: needs a large token budget and reasoning-model access.
- Whether the easy-hard-easy shape holds for current models: Hazra and Zhang disagree. Unblock: a search task and a decide task on the same formulas.
- Equal-budget parameter-tuning baseline for LLM-evolved heuristics (AutoSAT, SATLUTION, AESAT): needs solver hardware and competition benchmarks.
- Solution-count shortcut in ZebraLogic or SATBench: needs model counts for those items.

## Order to run

1. C06.02-U1: propagation scaffold vs CoT and best-of-N on twinned random 3-SAT. It is the only direct test of the main S4 idea, and no study exists.
2. C06.02-U2: forced substitution check. Satisfiability bias is the best-replicated LLM failure here, and the check is cheap code.
3. C06.02-U3 (log U4 alongside): translate-then-solve router at depth. The evidence is contested, and the result decides whether tool delegation becomes a standard operator.
