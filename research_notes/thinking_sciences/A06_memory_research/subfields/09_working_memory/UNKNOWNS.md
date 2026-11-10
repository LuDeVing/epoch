# Working memory: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A06.09-U1 | Does rewriting state into named chunks (a few units) beat raw history on multi-variable tracking? | S2 step: recode state into at most about 4 named chunks | S2, memory | K02 human-only (Smith); no LLM study | Raw history vs per-step chunked state; 4, 8, 16 live variables over 20 steps; accuracy vs variables | Chunked arm at least 10 pp higher at 8 or more variables, no loss at 4 | High |
| A06.09-U2 | Does overwrite-in-place (stale value deleted) beat append-only at equal tokens, for reasoning models? | Rule: code overwrites superseded values; old value goes to a side log | memory, G | K13, K25, K28 single-source; older and non-reasoning models only | Key-value stream 46 keys, 3 to 400 updates; arms append, overwrite, append plus "ignore", restated current-state block; last-value accuracy | Overwrite at least 15 pp over append at 100 updates, no loss at 3 updates | High |
| A06.09-U3 | Does a focus step (quote the one needed record, code verifies) cut wrong-record errors? | O: restate-before-answer with exact-match check | O, S4 | K05 human-only (Souza); refresh evidence d15 human | Same multi-fact items with vs without quote step; wrong-record error rate | Wrong-record errors down at least 20% relative, accuracy not lower, tokens within 5% | High |
| A06.09-U4 | Does "write the full state after each update" keep its gain at equal total tokens on non-arithmetic tasks? | G: every live variable rewritten each step | G, S | K16 single-source (WMIP, arithmetic) | Hidden-budget vs write-state on our bench items with 10 to 50 updates; final-state accuracy | At least 15 pp gain at 20 or more updates on our items | High |
| A06.09-U5 | Does a demo ladder (easy to hard worked examples) raise rule-tracking accuracy at no extra tokens? | S1 step: staged examples for lag or tracking rules | S1 | K08 single-source (Llama 70B n-back, b05) | n-back and a rule-tracking task, N 2 to 8; zero-shot vs ladder at equal prompt tokens; d' and task accuracy | At least 10 pp at N of 4 or more | Med |
| A06.09-U6 | Is a lure n-back score a valid gate for choosing the model per slot? | S0 gate: probe score used for model choice | S0 | K12 contested; 10 models r .70 to .88 vs 54 models no distinct factor | n-back with lures for 4 or more model/scaffold variants vs our bench score | Rank correlation 0.5 or more with bench accuracy after matching on model size | Low |
| A06.09-U7 | Is a failed probe a memory limit or a task-rule failure, and does rule restatement fix it? | G/S0 check: state the lag or rule first, verify code-side | G, S0 | c04, c22 single-source; older open models | Instructed-rule restatement vs none; fraction of runs with applied rule differing from instructed | Rule drift cut by half | Med |
| A06.09-U8 | What is the agent-level span (live variables before accuracy falls)? | A cap on live variables per step | G | K13 (llama4 about 5% at 46 keys); no clean span measure | Increase live variables 2 to 32 in a tracking task; accuracy curve; locate knee | Clear knee found; cap set at knee minus one | Med |
| A06.09-U9 | Does scaffold weight need to match model size? | Rule: light prompts for small models | G7 | c15, c23 older models, no exact numbers | Small vs large model, heavy vs light scaffold, equal tokens | Heavy scaffold loses at least 5 pp for the small model | Low |
| A06.09-U10 | What does carrying a state block cost the agent (dual-duty cost)? | Budget line: state block counted in token cost | G7 | K30 human; K31 single-source, one paradigm | Same items with and without state block carried; accuracy ratio | Ratio below 0.9 means shrink the state block | Low |
| A06.09-U11 | Does placing the needed fact at the prompt edges help? | Put the item for the next step first or last | memory | c16 older models | Fact at start, middle, end of constant-length context | Middle at least 10 pp worse than edges | Med |
| A06.09-U12 | Does a closed-batch current-state restatement (Mock-QA reset) work as a cheap alternative to overwrite? | Fallback when state cannot be rewritten in code | memory | K25 / d02 partial, no numbers | U2 arm D vs arm B | Within 5 pp of overwrite at lower token cost | Med |
| A06.09-U13 | Does a retire-with-log operator beat a REMOVE line? | O: rewrite without old value plus side log | O, memory | K28 single-source, K29 human | Stale-value reappearance and later recall of retired value | Reappearance under 2%, recall via log above 90% | Med |

## Open questions we cannot test on our bench yet
- Frontier 2026 reasoning model curves on PI-LLM and n-back: published curves are for open and non-reasoning models. Unblocked by running the public PI-LLM keys/updates sweep on our own model.
- Whether any n-back or span score predicts agent task performance after controlling for scale and training compute. Needs many more model variants than our bench holds.
- LLM replication of Daneman-Carpenter and Engle effects: two papers seen only as snippets. Unblocked by opening them.
- Original numbers for Baddeley and Hitch 1974, Daneman and Carpenter 1980, full TBRS: need PDF access.
- Multi-agent load splitting versus one agent with structured notes at equal tokens: no published comparison.
- Residual-stream suppression and attention interventions: need weights access.

## Order to run
1. A06.09-U2 (overwrite vs append): cheapest, changes how memory is stored, and the largest expected effect.
2. A06.09-U4 (write full state each update on our items): tests the strongest published single scaffold effect on our own tasks.
3. A06.09-U3 (focus step with exact-match check): cheap, human evidence is strong, and it is a candidate operator.
