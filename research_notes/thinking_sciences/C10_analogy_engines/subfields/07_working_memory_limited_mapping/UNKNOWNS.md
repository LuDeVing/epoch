# Working-memory-limited mapping: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C10.07-U1 | Does clutter shift LLM mapping from relational to attribute answers? | Prune step before O7 map | S1 / O7 | K01, K19; human-only plus LLM proxies (d09, d10) | Cross-mapped items, 60; filler-heavy vs trimmed vs plain; relational share | Trimmed beats filler by 10 points or more | High |
| C10.07-U2 | Does a cap of 3 to 4 correspondences per call help? | Chunked mapping at O7 | O7 | K04, K21; no LLM test | Items needing 2, 4, 6, 8 correspondences; uncapped vs cap 3 vs cap 4; relational accuracy | Cap wins by 5 points or more at 6+ and loses by under 2 at 2 to 3 | High |
| C10.07-U3 | Does an explicit role-filler binding table beat a count cap? | Binding table in code | memory / G | K06 contested; K16, K22 single-source | Same items as U2; table vs cap vs plain; accuracy and one-to-one violations | Table beats plain by 5 points and cap by 2 or more | High |
| C10.07-U4 | Does a code tool for counting and position work generalise beyond letter strings? | Tool offload in O7 | O | K10 single-source | Counterfactual letter strings plus 2 non-counting analogy sets; with vs without code | Gain of 10 points or more on counting set and 3 or more on a non-counting set | High |
| C10.07-U5 | Does a joint mapping prompt raise relational answers in LLMs? | "Map all at once" wording | O7 | K03; human-only (a01, a03) | Cross-mapped pairs; single-pair vs joint; relational share | Joint higher by 8 points or more | Med |
| C10.07-U6 | Is answer-order bias present in our model, and does a two-order check fix it? | Two-order agreement check | G | K20; GPT-4 2023, small n | Story analogies in both orders; single order vs agreement filter; accuracy | Order flips on 10% or more of items and filter lifts accuracy 3 points | Med |
| C10.07-U7 | Does the self-generated analog step survive equal tokens? | Analog recall in O7 | O7 | K13, K23; not token-matched | Hard analogy and math items; analog vs longer plain CoT | Analog wins by 3 points at equal tokens | Med |
| C10.07-U8 | Does our model still fail counterfactual letter strings and symbol binding? | Counterfactual guard in G3 | G3 | K09; older models only | 100 shuffled-alphabet items; plain vs code; accuracy | Plain below 0.6 on shuffled items (guard stays) | Med |
| C10.07-U9 | Do long noisy relational items collapse our agent, and does pruning help? | Distractor control in G | G | K18, K19; early-2025 models | Raven-style long items; plain vs pruning; accuracy | Pruning gains 10 points where plain is under 50% | Med |
| C10.07-U10 | Should valid alternative rules be accepted in scoring and selection? | Structure-based scoring | G | K09 contested (46% vs 39%; 22% vs 38.6%) | Items with several valid rules; key-only vs structure scoring; agreement with human raters | Structure scoring agrees with raters by 10 points more | Low |
| C10.07-U11 | Does a recap or rehearsal cue help long item lists on our model? | Recap cue at S2 | S2 | K12; GPT-3.5 only, gain gone at GPT-4 | Long-list items; recap vs none; accuracy | Gain of 3 points at our model size | Low |
| C10.07-U12 | Does base-item order change accuracy (IAM-style order effect)? | Randomise order and vote | S3 | K17; human, 10 per cell | Shuffle base items, 5 orders; accuracy spread | Spread over 5 points | Low |
## Open questions we cannot test on our bench yet
- Keane and Brayshaw 1988 and the journal text of Keane 1994 were never opened. Unblock: obtain the PDFs.
- Independent human replication of Waltz 2000 or the anxiety effect. Needs human participants or a literature search.
- Whether the human limit is count, binding quality or inhibition. Needs human experiments or model work.
- Internal binding capacity for 4 or more entities in frontier models. Needs open-weight interpretability access.
- An LLM analogue of anxiety has no operational definition.
## Order to run
1. U1 (clutter vs trimmed): cheapest, and it settles whether the human load effect applies to our agent at all.
2. U2 (cap 3 to 4 per call): the central untested claim of this subfield; it shares items with U3.
3. U4 (code offload beyond counting): the strongest single result so far; it needs a generality check.
