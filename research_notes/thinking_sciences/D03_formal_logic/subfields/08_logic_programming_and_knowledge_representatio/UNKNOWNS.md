# Logic programming and knowledge representation: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D03.08-U1 | Does a solver route beat CoT for current reasoning models on real-text logic (FOLIO, ProverQA hard, AR-LSAT)? | A solver route in S2 for classes where it wins, with CoT elsewhere | S0, S2, S4 | K27 single-source (puzzle sets only); K05, K26 CoT wins on shallow items; 2023 models for the rest | CoT arm vs solver arm (ASP/Z3, repair, no CoT fallback) vs solver+fallback; same token cap incl. retries; FOLIO clean subset, ProverQA hard, AR-LSAT, 100+ items each; accuracy and tokens per correct | Solver arm beats CoT by 5+ points on a class, 95% CI above 0, at equal tokens | High |
| D03.08-U2 | Does a round-trip equivalence check catch semantic mistranslation better than model self-approval, test cases or a second translator? | Round-trip (or the best of the four) as the S4/S5 semantic check | S4, S5, G5 | K30 single-source (statute rules, 25-rule human check); K29 self-approval false accepts 5-37% | Seed wrong translations into 100 items; four checkers; same token cap; false-accept rate, cost, final accuracy | False-accept at most half of self-approval's and final accuracy up 3+ points | High |
| D03.08-U3 | Does disagreement between solver arm and CoT arm flag wrong answers? | Agree-accept, disagree-escalate rule in S7 | S4, S7, G4 | K23 single-source (mistake overlap 0.14-0.22; no ensemble tested); NSCoT pipeline trailed CoT | Run both arms on U1 items; accept on agreement, escalate on disagreement; compare with either arm and with 2x CoT samples at equal tokens | Accuracy of agreed items 95%+ and total accuracy beats best single arm and 2x-sample CoT | High |
| D03.08-U4 | Can a cheap router (depth, interdependence, constraint count, text features) pick solver vs CoT? | S0 class gate with these features | S0 | K33 single-source; He and Wang pattern; BERT 92.6% routes among solver modes only | Fit router on half of a mixed pool; test vs always-CoT, always-solver at equal total tokens | Router accuracy beats both fixed policies by 2+ points or saves 25%+ tokens at equal accuracy | High |
| D03.08-U5 | Is ASP better than SMT for rules with exceptions and SMT better for plain puzzles for our model? | Fragment choice rule in S2 | S2 | K31 single-source (Ishay and Lee 2026; MultiLogicNMR 92.9 vs 35.8) | SMT vs ASP on 50 default/exception items and 50 plain puzzles; same prompts and token cap; accuracy, time-outs | Winner differs by class with 10+ points margin | Med |
| D03.08-U6 | Does a short target-language guide help our model? | Guide text in the S2 solver prompt | S2 | K31 single-source (compact 73.1 vs none 61.4; manual 22k tokens) | Guide vs none vs full reference, 100 items, token cost of guide counted | Compact guide adds 5+ points net of its token cost | Med |
| D03.08-U7 | Does an "implicit rules first" listing step stop lost rules in translation? | A listing sub-step before S2 translation | S1, S2 | K32 single-source; d20 two worked cases only | EntailmentBank-style items with missing facts; arms: CoT, solver, solver with listing step; accuracy and lost-rule rate | Listing closes at least half the gap to CoT | Med |
| D03.08-U8 | Does retrieving only relevant rules beat putting all rules in the prompt? | Rule retrieval before S2 | S1, S2, memory | K17 established for OWL EL (few ontologies); K16 DL-Lite size collapse; not tested on our items | Items with 1, 10, 50 distractor rules; all vs retrieved; accuracy and tokens | Retrieved arm within 2 points of clean and 10+ points above all-rules at 50 distractors | Med |
| D03.08-U9 | Do meaningful predicate names raise translated-rule accuracy for current models? | Naming rule in S2 | S2 | K15 contested (prompted +13; fine-tuned DeBERTa 95.3 vs 58.5; OWL under 8%) | Same rules with meaningful vs enumerated names; 100 items | 5+ points gain with CI above 0 | Low |
| D03.08-U10 | Does a retry cap or round cap (1, 2, 3) pay for itself? | Cap in S5 | S5, G7, G12 | K28 established for cost shape; plateau after 1-2 rounds on FOLIO (single model) | Rounds 0-3, accuracy per token | Marginal gain per token falls below plain-CoT sampling after round r; set cap at r | Med |
| D03.08-U11 | Does a verified rule-module library (time, space, kinship) transfer to new domains and beat building rules fresh? | Module memory | memory, S2 | K20 single-source (bAbI 99.99; old models; hand-written per domain) | Library vs fresh translation on 3 unseen domains; count build cost | 10+ points gain on 2 of 3 domains and build cost under 20% of per-item tokens | Low |
| D03.08-U12 | Does restricting S2 rules to a decidable fragment (Horn/Datalog) cut time-outs without losing accuracy? | Fragment restriction | S2 | K03 single-source (SHIQ undecidable); no Datalog or DL comparison for LLM translation | Free FOL vs Datalog vs ASP; time-outs, accuracy | Time-outs down 30%+ with accuracy within 2 points | Low |
| D03.08-U13 | Does the written chain actually drive the answer? (edit the chain, answer should change) | Chain-edit check in S8 | G10, S8 | K21 single-source (code-davinci-002 only) | Edit a rule in the chain; check answer change in solver vs CoT arm | Solver answer changes with edit in 90%+ of cases; CoT less | Low |

## Open questions we cannot test on our bench yet

- Tokens per correct answer, solver vs CoT, on real logic exams. No paper reports it. Unblock by logging tokens and calls in our own runs (U1).
- Open-ended tasks with truly missing facts and implicit rules. We have no bench items of this type. Unblock by building 50 items from EntailmentBank or from our own agent logs.
- Whether ASP-Bench-style saturation holds without a tuned prompt and gold validators. Unblock by running the loop with only the agent's own checks.
- Reasoning models with long internal chains on FOLIO direct vs CoT. Needs access to a reasoning model with the thinking budget switched on and off.
- Founding primary sources (van Emden-Kowalski, Clark, Gelfond-Lifschitz, Brachman-Levesque, DL Handbook) were not opened. Unblock by opening them; this changes no schema item.
- Any human data on writing rules in logic. None collected here.
- Label mix of ProverQA hard (is 50-56% near chance?). Unblock by counting labels in the released data.

## Order to run

1. U1 (solver vs CoT at equal tokens on FOLIO, ProverQA hard, AR-LSAT): every other test depends on knowing where the solver route wins for our model, and it yields the first token-per-correct figure.
2. U2 (semantic check shootout): the main risk of the solver route is silent mistranslation, and the schema forbids self-approval (G5), so we need a replacement check.
3. U4 (router) together with U3 (disagreement trigger): both reuse the U1 runs at almost no extra cost, and they decide whether the solver route is used at all.
