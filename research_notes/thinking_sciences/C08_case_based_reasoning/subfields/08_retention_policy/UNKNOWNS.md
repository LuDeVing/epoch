# Retention policy: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C08.08-U1 | Which write gate wins for a frozen model: add-all, success-only, novelty-only, success plus failure lessons | The winning gate as the S9 write rule | S9 / memory | K03, K24, d20; pairwise only (Xiong, ReMe) | 300-item checked stream; 4 gates plus no bank; fixed top-4 retrieval; equal tokens; final-100 pass rate | Best gate beats success-only by >= 2 points, or ties it with <= half the bank | High |
| C08.08-U2 | Does a novelty gate (store only if nearest case fails to solve) match success-only at far smaller bank | Novelty check before write | S9 | K05, a07, a08; single-source, synthetic, pre-LLM | Same stream; novelty vs success-only; bank-size matched | Within 1 point of success-only at <= 50% of the bank size | High |
| C08.08-U3 | One-line failure lessons on top of success-only | A failure-lesson line per failed item | S9 / memory | K04, K23; contested; +0.7 to +3.2; raw failures hurt | Success-only vs success + one-line lesson vs success + raw failure trace; equal prompt tokens | Lesson arm >= +2 points over success-only at equal tokens | Med |
| C08.08-U4 | Per-case retrieval-outcome counter prunes harmful cases | Counter in code; prune at count >= 5 and success < 0.5 | memory / G5 | K07, K22, d13-d15; works with embeddings, other papers | Plant 5 wrong cases in 100; counter-prune vs none; copy rate and pass rate | Planted-case copy rate drops by half and pass rate does not fall | High |
| C08.08-U5 | Append-only lesson store vs in-place rewrite at our scale | Rule: append, dedup, delete; no in-place edits | memory | K09, Zhang 2026, ACE; no independent replication | 200-item stream; rewrite every 20 vs append vs append + delete | Append arm >= rewrite +5 points at end, or rewrite falls below no-memory | High |
| C08.08-U6 | Break-even gate accuracy for raw traces vs one-line lessons | Policy: lessons only if gate accuracy is low | G5 / S9 | K17, K21; contested (Xiong vs ReasoningBank) | Flip gate labels at 50/70/90/100%; raw vs lessons; same stream | Lessons stay above no bank at 70% while raw falls below it | Med |
| C08.08-U7 | Paired-replay admission (with vs without candidate) | Replay check before write for borderline cases | G7 / S9 | K22, d12; single source; confounded with retrieval | Verified candidates: admit all vs admit if replay gains net of tokens | >= 30% fewer admitted, accuracy equal or better, total tokens (incl. replays) not higher | Med |
| C08.08-U8 | Memory-off switch by similarity to the bank | Similarity threshold to skip memory | S0 / memory | K11, c19, d12; correlations 0.563 to 0.717 | Memory always on vs gated by similarity; items split by similarity | Pass-to-fail flips fall >= 50% with no loss on high-similarity items | Med |
| C08.08-U9 | Decay of a success-only bank over a long stream with a task shift | Cap and delete rule; shift reset | memory | K24, d04, d11; longest stream 400 steps | 600+ items, shift at item 300; uncapped vs cap 100 (utility / random / age) | Capped utility arm beats uncapped by >= 2 points on items 301-600 | High |
| C08.08-U10 | Competence (footprint) deletion with embedding retrieval | Footprint-like deletion at cap | memory | K06, K18, a03, a09; toy domain, human CBR; noise concern | Cap 50; footprint vs later-use utility vs random | Footprint beats utility by >= 2 points; else drop it | Low |
| C08.08-U11 | Second check before retaining a verified success (right answer, wrong reason) | Held-out/mutation re-check before write | G3 / S9 | K11, b08, c08; strict history deletion beat error-free memory once | Verified-only vs verified + mutated-input re-check; equal tokens | Re-check arm >= +2 points or removes >= 20% of later-harmful cases | Med |
| C08.08-U12 | Does the bank help at all for our model strength | Per-model switch: bank on or off | S0 / G7 | K10, d17; strong models gain little | Bank vs no bank across 2 to 3 model sizes, same stream | Bank gain >= 3 points on the target model, else keep memory off | High |
| C08.08-U13 | Size of the random same-task control gap on our items | Method rule only | G7 | K20, d08; ExpeL 42.5 vs 59.0 | Random same-task examples vs task-similar retrieval at equal count | Task-similar beats random by >= 5 points (otherwise gain is just examples) | Low |

## Open questions we cannot test on our bench yet
- Independent replication of Zhang 2026 (rewriting decay): needs ARC-AGI Stream code and a GPT-5-class backbone; check the authors' release.
- Break-even judge accuracy in percent for Xiong's raw-trace stores: needs exact judge error rates; rerun with simulated flips (U6).
- What "20.9%" means in the CASCADE abstract, and the 4 multi-turn tasks of the 16: needs the paper's per-task figures.
- Streams over 1000 tasks with true distribution shift: we have none with a checker; needs a generated task family with shift.
- Token-controlled comparison of failure lessons: no paper controls tokens; our bench must (U3).
- Open reasoning items with no checker: no code gate exists; needs a proxy (mutated input, held-out example) validated against labels.
- Aha 1991, Minton 1990, Racine and Yang, Leake and Wilson were not opened; open them before citing any number.

## Order to run
1. C08.08-U12 (bank on or off for our model): cheapest, and decides whether the rest matters at all.
2. C08.08-U1 with U2 as an arm (four write gates incl. novelty at equal tokens): the central unknown in this subfield.
3. C08.08-U5 (append-only vs in-place rewrite): fast, and the clearest negative result in the literature (decay toward no-memory).
