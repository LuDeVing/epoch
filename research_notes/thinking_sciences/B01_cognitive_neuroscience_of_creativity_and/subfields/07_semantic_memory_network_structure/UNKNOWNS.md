# Semantic memory network structure: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B01.07-U1 | Does seed distance raise originality AND correctness for our agent? | Rule: choose seeds from a set distance band | O7, S3 | K26, K29; d01, d03; single-source, product-design task, no correctness | Seeds in bottom, middle, top-decile bins vs none; 40+ open items with a check; pass rate and originality | Top bin beats none by 5 points or more on pass rate with originality not lower, CI excludes 0 | High |
| B01.07-U2 | Is there an inverted U at the far end? | Cap on seed distance | O7 | K29; d03 monotonic to top decile only | Add an unrelated-domain bin to U1 | Pass rate in the far bin falls 5 points or more below the top-decile bin: add a cap | High |
| B01.07-U3 | Do far seeds help only on an impasse? | Gate far seeds on S6 | S3, S6 | K27; d04, d05; human, contested | Always-far vs near-then-far at impasse vs none; impasse items | Gated arm beats always-far by 4 points or more | High |
| B01.07-U4 | Does a far-seed gain hold only for strong models? | Model-strength gate in S0 | S0, O7 | K26; d01; two models only | U1 on a strong and a weaker model | Gain 5 points or more for strong, under 2 for weak: add gate | Med |
| B01.07-U5 | Does an exclusion list of used seeds raise cross-run variety without hurting accuracy? | Seed history in memory | O7, memory | K13, K15, K31; repetition established, fix untested | 8 runs each: none vs exclusion list vs persona; distinct seeds, pairwise similarity, pass rate | Distinct seeds up 20% or more, pass rate within 2 points | High |
| B01.07-U6 | Does persona-seeded open mode help correctness, not only diversity? | Persona seeds for open mode | S3 | K16; c22, d14; single-source, proxies only | Persona set vs none vs direction planning; checkable items | Pass rate not lower and distinct correct solutions up 15% or more | Med |
| B01.07-U7 | Does cluster-then-switch seed order beat random order? | Ordered seed generation | S3 | K25, K32; b06, d15; observational, contested | k ideas per cluster then forced jump vs random order | Originality up 0.3 SD or more, pass rate not lower | Med |
| B01.07-U8 | Is distance the active ingredient, or only more varied seeds? | Keep distance control only if it beats count-matched variety | O7 | K27; d05; human only | Far seeds vs same number of random-distance seeds vs near seeds | Far beats random-distance by 3 points or more; else drop distance control | Med |
| B01.07-U9 | Which metric picks seeds best: GloVe, LLM embedding, forced choice? | One calibrated distance function | O7 | K08, K19, K30; d06, d09; mixed | Rank seeds by each metric; correlate with downstream pass or originality | Winner correlates 0.1 higher than the others; else use the cheapest | Low |
| B01.07-U10 | Does a fit check after a far-seed idea keep originality and restore feasibility? | Mandatory fit check | S4, G8 | K21, K28; d02 (r=-.74); single-source | Far seed with fit check by code vs without | Feasibility pass up 10 points or more, originality loss under 10% | High |
| B01.07-U11 | Does a pool-distance filter (reject candidates close to earlier ones) help? | Candidate filter | S3, S7 | K23; c16; contested | Filter vs none | Distinct correct answers up 10% or more, no pass-rate loss | Low |
| B01.07-U12 | Can a short remote-association probe pick the model for open mode? | Probe in S0 | S0 | K33; d16; across 35 models only | Probe score vs open-mode pass rate across our models | Spearman 0.5 or more across 5+ models | Low |
| B01.07-U13 | Does the scaffold reverse the homogeneity trend for our model? | Evidence that diversity tools are needed | O7, memory | K15; c12, c13, d20; defaults only | Plain vs scaffold, 8 repeated runs; pairwise similarity | Scaffold cuts similarity by 0.05 or more | Med |

## Open questions we cannot test on our bench yet
- Independent or preregistered replication of Kenett 2014 with more than 33 per group. Needs a human lab. Watch for the full text of Luchini 2023 (N=477).
- Whether human results on far inspiration carry to LLMs on exact-answer tasks. Needs U1 and U3 first.
- Whether DAT-type distance means anything for problem solving. Needs a task set with correctness plus distance scores.
- Whether the usefulness trade-off (r=-.74) holds for our agent. Needs a feasibility rubric run by code, not a model judge (G8).
- Snippet-only sources (Ocsai r=.81, SemDis ensembles, Bernard 2019, Benedek 2017) need full-text reading before they drive a metric choice.
- Whether our final model behaves like the models in Liu 2026. Needs a run on our own model.

## Order to run
1. B01.07-U1 (with the U2 far bin): controlled seed distance on checkable items. It is the central missing test and decides whether distance control in O7 and S3 exists at all.
2. B01.07-U5: exclusion list vs persona seeds across runs. Cheapest, and repetition is the best-established problem.
3. B01.07-U10: fit check after far seeds. Cheap, and it guards against distance without usefulness.
