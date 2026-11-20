# Other scenario traditions: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E17.02-U1 | Does a rationale-sharing feedback round beat K independent samples averaged? | One optional feedback round at estimate steps | O (ensemble); G9 interaction | K20; d01-d04; single-source, small gains, no token match | A: K samples averaged by code. B: same K plus one anonymous rationale round. 100+ resolved binary questions; Brier | B beats A by at least 0.01 Brier, paired CI excludes 0, in mixed-model arm | High |
| E17.02-U2 | Does a prescribed severity path plus text-to-number reconciliation cut contradictions? | Code-side reconcile step in scenario output | G5 | K07, K08, K22; b17-b19, d12; single-source | A: free severity. B: severity set by code plus reconcile. 100 scenarios, 5 runs each; contradiction rate, severity variance | Contradiction rate falls by at least 50% with no loss in rated plausibility | High |
| E17.02-U3 | Does an identical evidence package before scenario and estimate steps raise accuracy? | Mandatory evidence-load step before estimates | G (ground) | K03, K18; a22, b10, b24; single-source, no rounds ablation | A: no evidence. B: same evidence package, same tokens. Estimation items with known answers; correlation, MAE | Correlation gain of at least 0.2 or MAE cut of at least 20% | High |
| E17.02-U4 | Does Kahn-style branch-then-probability beat a direct probability? | Branch scenario step for multi-path questions | S0/O1 | K12, K21; d05 (narrative prompt hurt 11 of 12); untested directly | A: direct probability. B: 3-5 weighted branches, code-normalised. Same resolved questions; Brier | B beats A by at least 0.01 Brier on a defined subset (multi-path questions) | Med |
| E17.02-U5 | Can an LLM label pairwise consistency for a morphological box reliably? | Morphological pruning helper | O (enumerate options)/S | K11; a06, a07, c18, c19; mechanism established, no LLM test (d11) | A: free brainstorming. B: box plus pairwise labels (2 runs per pair). 10 design tasks with human-labelled valid sets; coverage, invalid-kept share, label agreement | Coverage of valid configurations up by at least 15 points and agreement with humans at least 0.7 | Med |
| E17.02-U6 | Does model diversity beat persona diversity on accuracy, not only spread? | Rule: diversify by model at estimate steps | O (diversify), G4 | K04, K05; a23, a26; spread evidence only; Csaszar says same-family correlation 0.80-0.97 | A: 5 personas one model. B: 5 models one prompt. C: 5 samples one persona. Forecasting set; Brier and distinct-branch count | B beats A and C by at least 0.01 Brier | Med |
| E17.02-U7 | Does a Futures Wheel consequence tree beat a single-pass list? | Consequence-tree operator | O (enumerate consequences) | K13; b20, b21; single team, GPT-4.1 mini; negative skew | A: single-pass list. B: two-level wheel plus benefits pass. 20 change events; unique risks, expert-rated systemic share | At least 30% more unique valid risks at equal tokens, systemic share not lower | Med |
| E17.02-U8 | Do paired with/without-action counterfactual scenarios improve action choice? | Counterfactual pair step | O4 analogue | K14; b22; perceived severity only | A: plan-only reasoning. B: paired scenarios per action. Decision items with scored outcomes; decision accuracy | B beats A by at least 5 points accuracy | Low |
| E17.02-U9 | Does the Csaszar ranking edge hold for our agent in other domains? | Agent used for pairwise strategy ranking | S0 | K01, K02; a18-a20, d15; single-source, one domain, LLM-only replication | A: plain single call. B: our agent. Fresh pairwise ranking sets (ventures, papers); Spearman with later outcome | B at least 0.05 higher Spearman than A across two domains | Med |
| E17.02-U10 | Does a probability-anchored adverse case improve agent decisions versus baseline-only reasoning? | Baseline plus adverse case with stated anchor | S, memory | K09, K24; a15, a16; human practice only; d16 shows adverse cases set too mild | A: baseline-only. B: baseline plus adverse with anchor. Risk decision items with known loss; decision accuracy, calibration | B beats A by at least 5 points or cuts loss-miss rate by 20% | Low |
| E17.02-U11 | How much run-to-run variance do our scenario steps have? | Run-variance log and a minimum repeat count | G (reproducibility) | K06; a25, b06, b07, b18; established direction, size unknown for our agent | 5 repeats of the scenario step; theme recall per run, aggregate stability | Always run; adopt N repeats at which aggregate theme set stabilises (Jaccard at least 0.8) | High |
| E17.02-U12 | Is two rounds really the optimum, or is it a one-run artefact? | Round-count cap | O (ensemble) | K20; d03, d04; one run, headline 0.178 vs cross-model 0.189 | Rounds 1, 2, 3 on our own model set, 3 seeds; Brier | 2 beats 1 and 3 in at least 2 of 3 seeds by 0.01 Brier | Low |

## Open questions we cannot test on our bench yet

- Primary Delphi numbers (Dalkey and Helmer 1963 error by round; Sackman 1974; full Rowe and Wright 1999). Missing: access to RAND and ScienceDirect PDFs. Unblock: obtain full text through a library or open copy.
- Hit rates of Kahn's Year 2000 list, Shell scenarios and La Prospective. Missing: primary texts and an outcome-scoring rubric. Unblock: read the books, score the 100 innovations.
- Whether the persona-panel UI result (arXiv 2607.28439) is real. Missing: a record in the arXiv API. Unblock: re-fetch and verify.
- Whether stress-test scenarios predicted later crises. Missing: any post-2009 accuracy evaluation. Unblock: read ECB/EBA/Fed retrospective evaluations.
- Long-horizon quantity forecasts. Missing: ground truth. Unblock: wait for outcomes or use hindcast with knowledge cutoff controls.
- La Prospective with LLMs, Kahn stories with LLMs. Missing: any study; searches were low recall. Unblock: a wider literature search once APIs are available.
- Contamination of Lorenz benchmarks (training-data overlap). Unblock: post-cutoff benchmarks.

## Order to run

1. **E17.02-U11 (run variance).** Cheapest, no labels needed, and it sets the repeat count every other test needs.
2. **E17.02-U1 (feedback round vs independent average).** Highest-stakes disagreement in the literature and a direct G9 test at equal tokens.
3. **E17.02-U2 (severity anchor plus reconcile).** Cheap code check, big effect expected on small models, and no model-judge needed.
