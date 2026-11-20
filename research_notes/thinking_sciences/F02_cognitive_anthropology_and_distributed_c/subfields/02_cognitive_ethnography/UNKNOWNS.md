# Cognitive ethnography: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| F02.02-U1 | Does a pre-computed target card, checked by matching, beat plain log notes? | Planning pass writes a card; later passes match against it | memory, S0 | K01, K16; a01, a03, d01-d03; human-only, checklist data mixed | Card vs plain notes vs no notes; multi-step items with computed targets; accuracy and card-read rate | Card beats notes by 3+ points over 3 runs and card-read rate above 80% | High |
| F02.02-U2 | Does splitting work in time (early plan, late compare-only) beat one pass? | Two-phase default for long chains | S0, O | K03; a02, a04; human-only | Two-phase vs single pass; long-chain items; accuracy, late recomputation errors | Two-phase wins by 3+ points on chains of 6+ steps, no loss on short ones | High |
| F02.02-U3 | Does a verification pass anchor on the first answer? | Blind verification (re-solve then compare) as default | O verify, G | K06, K18; c03, d08, d09; single-source, older models | Blind vs shown-first-answer vs none; items with 20-40% first-pass error; accuracy, right-to-wrong flips | Blind beats shown by 2+ points, or shown flips 1.5x more right answers | High |
| F02.02-U4 | Does coding agent traces for state-holder lead to design fixes that raise accuracy? | A trace-review step in development; a state-location rule in S | S | K17; d05, d06, d07; single-source, tokens unmatched | Code 50 own traces, edit design, rerun at equal tokens; pass rate; kappa on 15 shared traces | Pass rate up 5+ points at equal tokens and kappa 0.7+ | High |
| F02.02-U5 | Is verification worth it only on weak task types? | Route verification by task type or confidence | O | K06; c03; single-source (helps on weak tasks, hurts 15-20 HNS on two) | Verify-all vs verify-routed vs none; mixed item types; accuracy and tokens | Routed matches verify-all accuracy at 30%+ fewer tokens | Med |
| F02.02-U6 | Does reflection or a memory filter raise task success, not just ratings? | Reflection step and record filter in memory | memory | K10, K21; b20, d13, d14; single-lab | Memory+reflection vs memory vs filtered; long tasks with unit tests; pass rate, error-copy rate | Reflection +5 points over memory-only; filter cuts error copying | Med |
| F02.02-U7 | Does single-agent role-switching match multi-agent at equal tokens? | Role-switching passes, no multi-agent default | O | K13, K19, K20; d10-d12, c16-c19; contested, varies by task | One agent role-switching vs multi-agent; sequential and decomposable items; accuracy | Single within 2 points on sequential; multi-agent kept only if it wins decomposable by 4+ | Med |
| F02.02-U8 | Does a stay-in-list guardrail cut invented categories without hurting accuracy? | Closed-label guardrail for coding and classification | G | K07, K22; b11, b12, d17; single-source, older models | Guardrail+examples vs none; 30 traces, 15-30 labels; off-list rate, kappa | Off-list rate below 2% and kappa not lower | Med |
| F02.02-U9 | Does majority of k reruns beat one deep pass on coding-like items? | Rerun-consensus operator | O | K08, K09; c06, b17; contested (consistency is not validity) | k reruns vs single run at k times tokens; classification items; accuracy, run kappa | Majority wins by 2+ points on noisy items | Med |
| F02.02-U10 | What is the invented-category rate and kappa of current models on open coding? | A threshold or a human gate for open coding | G | K22; d17, d18; closed codebooks only, older models | Open coding of 30 traces by 2 humans and the model; invented-code rate; kappa | If kappa below 0.6 or invention above 5%, add a human or closed-set gate | Med |
| F02.02-U11 | Does the agent reuse its own helper notes in ways we did not design (opportunistic structure)? | Promote invented notes to designed tools | memory, O | a05, a08; single anecdote, human-only | Log notes written and reused across 50 traces; reuse rate; add promoted tools at equal tokens | A note type reused in 20%+ of traces and promotion lifts accuracy 2+ points | Low |
| F02.02-U12 | Do persona prompts help the agent on behaviour questions? | Persona grounding for behaviour items | none, G | K12; c15, d15, d16; single-source, fails on incentivised games | Persona vs no persona; behaviour-prediction items; accuracy | Gain 3+ points on behaviour items, not only self-report | Low |
| F02.02-U13 | Does a deviation callout rule (stop and re-plan beyond a threshold) cut late errors? | Threshold trigger in S | S, G | a02; human-only, no measure | Threshold trigger vs none; items with drift; error rate, tokens | Errors down 20% relative at equal tokens | Low |

## Open questions we cannot test on our bench yet
- Controlled test of the speed-bug mechanism with pilots. Needs aviation human-factors data or a simulator study. Unblock: search aviation journals; none were reachable here.
- Ship-navigation numbers in Cognition in the Wild. Unblock: open the book.
- Video coding with fieldwork recordings and open codebooks. Our bench has no video items. Unblock: add a small video or screen-recording item set.
- Interview-grounded simulation on incentivised games with newer models. Unblock: a newer-model rerun of the Park or Twin-2K-500 materials.
- MetaGPT at equal tokens. Unblock: rerun with a matched budget.
- Whether LLM trace attribution (who and when) can be made usable. Unblock: annotators better than 53.5% agent-level and 14.2% step-level accuracy.
- Outputs of Hutchins' 2024 generative-AI project. Unblock: publication.

## Order to run
1. F02.02-U3 (blind vs shown verification): cheapest, and it decides how every verify step is built.
2. F02.02-U1 (target card vs plain notes): the core idea of the whole field, and cheap to run.
3. F02.02-U4 (state-holder trace coding): the only test that applies the method itself to our agent and could reveal what else to fix.
