# Automated discovery: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E15.10-U1 | Does generate-test-select with a code check beat best-of-N plain sampling at equal tokens on discovery-type items? | Keep S3-S5 loop for checked items; justify G7 for discovery | G7, S3-S5 | K22 open; no source runs it (d11, d12 match idea count, not tokens) | Items: ARC programs plus transformed-form equation recovery. Arms: plain N samples vs scaffold with held-out check. Metric: held-out pass rate per 1M tokens, 5+ repeats | Scaffold wins by 5+ points with non-overlapping 95% intervals; else drop discovery-specific loop | High |
| E15.10-U2 | Does picking by executed outcome beat picking by model judge on open idea or design items? | Rule: no selection by judge where a run is possible | G8, S7 | K02, K19 single-source (Si 2025, N=43, NLP only); K03 | Items: open tasks with a runnable outcome. Arms: judge pick vs run pick. Metric: rank correlation of pick with later outcome; mean outcome | Run pick beats judge pick by 0.15+ correlation or 5+ points outcome | High |
| E15.10-U3 | Does a retrieve-then-compare novelty step catch prior art that keyword search misses? | Add retrieval novelty check in S4 for idea tasks | G8, S4 | K14 single-source (24.0% overlap; tools 0%); K11 | Items: ideas with known prior art (planted). Arms: none vs keyword vs retrieve-and-compare. Metric: recall of true prior art, false flags | Recall 2x keyword at false-flag rate under 20% | Med |
| E15.10-U4 | Do operator prompts (O1-O8) with fresh contexts raise unique candidates over plain resampling? | Operator-seeded S3 in open mode | S3, O1-O8, G4 | K04 single-source (about 5% unique of 4000); d11 confounded by cost | Open-mode items. Arms: plain resample vs one operator per fresh attempt. Metric: unique candidates (cosine 0.8) per 100k tokens | 1.5x unique count with no drop in pass rate | Med |
| E15.10-U5 | Does an opposed-persona reviewer ensemble beat a single judge, and does it add anything beyond plain voting? | Persona screen where a model judge is unavoidable (no-check mode) | G5, S4 | K20 single-source (81.8% vs 70.6%); K13 contested; G4 and G9 predict a null vs voting | Review-like items with ground truth. Arms: single judge, 3-persona ensemble, majority of plain samples. Metric: accuracy | Ensemble beats single judge by 5+ points AND is not worse than plain voting | Med |
| E15.10-U6 | Does a retained-notes memory transfer across related items, or only inflate by test-set selection? | Lesson store used in S9 and read after the first attempt | memory | K17 single-source (+11.4% self-read, +3.3% transfer; test-set selection) | Sequence of related items with held-out set. Arms: none, lessons after attempt, lessons before attempt. Metric: pass rate on later held-out items | Gain of 3+ points on held-out items; "before" arm not better than "after" | Med |
| E15.10-U7 | Where does extra compute stop helping, and are several short fresh runs better than one long run? | A token-budget cap and restart rule per class | G11, G12, S6 | K10 contested; K21 single-source (o1 plateau at about 1 h; may be a scaffold artefact) | Mixed-difficulty set. Arms: uniform budget, difficulty-based budget, one long vs several short fresh runs. Metric: pass rate vs tokens | Short fresh runs beat one long run past the plateau by 3+ points | High |
| E15.10-U8 | Does tagging final claims as computed, cited or interpreted, then verifying only interpreted ones, cut wrong claims? | Claim-type check in S8 | S8, G10 | K15 single-source (Kosmos: synthesis 57.9% vs 85.5% data analysis) | Items with explained answers. Arms: none vs tag and verify. Metric: wrong final claims per 100 | 25% fewer wrong claims at under 10% extra tokens | Med |
| E15.10-U9 | Is the LLM-SRBench gap (31.5%, 28.1%) memorisation, and does our agent show the same gap on mutated items? | A standing "original vs mutated" gap report as a gate | G3 | K06 established but indirect; no clean contamination test | Same problems original vs transformed; our agent and plain. Metric: accuracy gap | Gap over 15 points confirms; then require mutated-form pass in S8 | Med |
| E15.10-U10 | Is a decomposition step (O3) or representation change (O6) robust to noise, as AI Feynman was not? | Noise check before trusting O3/O6 results | O3, O6, G3 | K07 established for non-LLM only; LLM-SR noise untested | Equation or pattern items with 0, 0.01, 0.1 noise. Arms: plain vs O3/O6 operator. Metric: exact recovery by noise level | Gain at noise 0 still present at 0.1 (at least half) | Low |
| E15.10-U11 | Are judge scores (LLM symbolic match, DeepReviewer, Elo) moving the published headline numbers? | Rule: score our own bench by code only | G5, G8 | critique.md weak spots; K16 contested; 94.6% match agreement is the only check | Re-score a sample by code and by LLM judge. Metric: disagreement rate | Disagreement over 10% means all judge-scored bench items get a code check | Low |
| E15.10-U12 | Does reporting hit rate across repeated runs change which variant we pick (best-of-run inflates)? | Standing metric: hit rate and samples per success | G7 | K18 single-source (FunSearch 4 of 140) | Any verified-scorer task, 10 repeats per arm. Metric: hit rate vs best run | Ranking of arms changes in at least one comparison | Low |

## Open questions we cannot test on our bench yet

- Non-NLP idea quality over time: needs human judges or real experiments to measure later value; our bench has none. Unblock: a small panel or code-checkable "downstream" outcome per idea.
- Independent audit of Kosmos and co-scientist claims: needs outside labs. Unblock: wait for third-party reports; do not cite developer numbers as established.
- Whether a "novel" hypothesis is a retrieved one outside NLP (K14, gap 4): needs a corpus in biology or chemistry and a source-matching procedure.
- Founding-era numbers (BACON, Adam hit rates): papers not opened. Unblock: read Langley 1987 and King 2009 and extract rates.
- FunSearch prior record (496?) and no-LLM ablation: supplement not opened.
- LLM-based symbolic regression under noise: needs the equation set plus noise generator.
- Multi-hour agent horizons: our bench runs short items; plateau results (PaperBench) cannot be reproduced there.
- Debate vs sampling inside a discovery loop: G9 forbids debate; testing it needs an explicit exception arm.

## Order to run

1. **E15.10-U1** (equal-token control). It decides whether the generate-test-select loop pays for itself on checked items, which is the premise of the whole schema (G7); no published source answers it.
2. **E15.10-U2** (run pick vs judge pick). Cheap, reuses U1 candidates, and directly tests G8 against the strongest evidence (ideation score does not predict execution).
3. **E15.10-U7** (budget by difficulty and fresh short runs). Same items as U1 with extra arms; the answer sets G11 and G12 limits and the restart rule.
