# Metacognitive knowledge: declarative, procedural, conditional: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A04.04-U1 | Does a per-class operator record (measured pass rates, code routing) beat the best fixed operator? | Class record table + code router | S6, O1-O8, memory | K24, K25; Select-then-Solve 53.1 vs 50.3, RTR 82.5 vs 80.0; no written-record study; single-source | Random operator vs best fixed vs record router; 4-6 classes, 40+ items each, 3 repeats; pass rate at equal tokens | Router beats best fixed by 2+ points, interval excludes 0, and random is below best fixed | High |
| A04.04-U2 | How big is the per-class oracle gap on our tasks? | Per-class switch: record only where gap is large | G7, S6 | K06 (literature: +12.4 to +24.1; ZebraLogic small); optimistic oracle | Run O1-O8 on 30 items per class; oracle minus best fixed | Add record to a class only if gap is 5+ points after repeating runs | High |
| A04.04-U3 | Is the record better enforced in code than shown in the prompt? | Rule: record is code-side only | G5, G10 | K13, K26; MIRROR 0.605 told vs 0.143 external is for confidence only; confounded for operator choice | Same record: in prompt (model picks) vs in code vs none; same items; pass rate and "ignored" rate | Code beats prompt by 3+ points and prompt is within 1 point of none | High |
| A04.04-U4 | Items per class needed before a measured record beats a prior | Update rule: minimum n per class, bandit warm-up | memory update rule | K29; open; bandit warm-up recipe only | Build record from 5, 10, 20, 40 items; test on 100 held-out; accuracy of choice | Pick smallest n where record beats prior by 2+ points; record the curve | High |
| A04.04-U5 | Does a fixed structure written once per class beat per-instance choice? | Per-class structure cache | S0, O3, memory | K11; Self-Discover GPT-4 BBH 81 vs 75, T4D 85 vs 52; single-source, older models, 1-7 points on MATH | Structure once per class vs per-instance vs plain; structure-heavy and arithmetic classes; pass rate and calls | Beats per-instance at equal tokens by 2+ points on at least 2 classes | Med |
| A04.04-U6 | Do skill-matched hints beat topic-matched and random hints? | Class label as retrieval key for hints | S0 gate, memory | K08; Didolkar MATH 53.88 vs 50.31 topic; GSM8K 94.31 vs 92.87 random; single-source | Skill vs topic vs random vs no hints; one run per arm minimum, 3 repeats | Skill beats topic by 2+ points on a non-saturated class | Med |
| A04.04-U7 | How much of the gain survives random or inverted record content? | Tells us if gain is selection or just extra structure; may drop the record | G7 | K16; MUSE random 68/69 vs true 84/90 vs ReAct 35/35; single-source | True vs random vs inverted vs no record, all code-routed | Keep record only if true beats random by 3+ points | Med |
| A04.04-U8 | At what model strength does model-side self-selection stop losing? | Allow self-routing for our model on classes where it ties | S6 | K28, K05; GPT-5 ties Direct; weaker models lose; older and small models | Model picks from list vs Direct vs best fixed on 3 classes | Self-route within 1 point of best fixed on a class (then skip routing cost there) | Med |
| A04.04-U9 | Does the record transfer to mixed-class items and to a cheaper model? | Cross-model record sharing; mixed-class fallback | S0, record scope | K14, K30, K09; MIRROR transfer 0.019-0.175; Didolkar catalogue transfer to Mixtral; mixed untested | Mixed-class items; record from strong model used by cheap model; pass rate vs best fixed | Transfer arm keeps 60%+ of the in-class gain | Med |
| A04.04-U10 | Is conditional knowledge separable from procedural knowledge in an LLM? | Separate modules for "can run" vs "knows when" | all | K22; no study; KAPRO know vs act is a proxy | A: model told operator; B: model picks from list; C: code picks from record; B-A and C-B | Either difference is 3+ points and stable over repeats | Low |
| A04.04-U11 | Rate of the four Flavell failures with a written record | Targeted fix per failure type; logging | G3, G6, logging | K02, K27; KAPRO Kc/Aw 1.76-45.48%; no record study; single-source | Tag failures in U3 prompt arm: wrong, not retrieved, ignored, unhelpful | Any one type above 25% of failures gets a specific fix | Med |
| A04.04-U12 | Does escalate-on-impasse beat always-long reasoning at equal tokens? | Short path first, escalate on failed check | G11, G12 | K17; AdaptThink -53% length +2.4; Meta-R1; SOFAI-LM; most train weights | Short-then-escalate (code trigger) vs always-long vs always-short | Equal accuracy within 1 point at 25%+ fewer tokens | Med |
| A04.04-U13 | Does a self-reported "done" or confidence need a code-side check? | Replace self-report with code check wherever one exists | G3, G6 | K04 (children), K13, K15 (random retry inside harness interval) | Self-reported done vs code check; always include random retry at matched K | Code check cuts confident failure by 20%+ relative | Med |
| A04.04-U14 | Do own-trace behaviour notes written per class help held-out items? | Per-class behaviour notes in memory | memory | K18; MC2 +6 and +47 on game of 24; Metacognitive Reuse -46% tokens; order effect | Notes written from own solved items vs no notes vs random notes; held-out items; accuracy and tokens | Beats random notes by 2+ points or 15%+ fewer tokens | Med |

## Open questions we cannot test on our bench yet

- Exact figures in Flavell et al. 1970, Markman 1977, Schraw and Dennison 1994, Schraw and Moshman 1995, Paris et al. 1983. Unblock: library copies (ScienceDirect, ResearchGate returned 403).
- Whether "declarative, procedural, conditional" has any causal role in humans beyond a vocabulary. Needs human data; the structure tests so far reject the three-way split (K03).
- Why forced metacognitive prompts help in Metacognitive Prompting but hurt in Think2. Unblock: same-model, same-task comparison with both prompts.
- Whether the negative link between self-awareness and success in model traces (NPMI -0.141) is causal. Unblock: interventions that add or remove self-assessment text at fixed difficulty.
- Whether any of the 2026 preprints (MIRROR, Cao, MC2, KAPRO, Select-then-Solve) replicate. Unblock: independent runs; several have text and table mismatches.
- Whether results hold for frontier models newer than those tested. Most studies used 2023-2025 models.

## Order to run

1. A04.04-U2 (oracle gap): cheapest, and it decides which classes the record can pay in at all.
2. A04.04-U1 (record routing vs best fixed vs random): the core claim; needs U2's class list.
3. A04.04-U3 (record in prompt vs in code): decides where the record lives; can reuse the U1 data and logging.
