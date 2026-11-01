# Gestalt insight and the "sudden insight" debate: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A02.06-U1 | Does an explicit restructure operator beat extra samples plus weighted vote? | Impasse, then relax / decompose / re-encode, before more sampling | O4, O6, S6 | K31, contested. d11, d12, d13 conflict; c05 +8.41pp not compute matched; older or small models | 3 arms: N samples + weighted vote; same-chain extension; restructure then solve. 100+ reframing items (decoy ARC, BRAINTEASER-like), private twins, 3 seeds. Accuracy per 1K tokens, regressions | Restructure arm beats the best other arm by 3+ points on decoy items and is no more than 1 point worse elsewhere | High |
| A02.06-U2 | Which trigger should fire the operator? | One trigger rule with a minimum depth | S6, G1 | K33, single-source. d08, d09, d10, d16 (n=5) | 5 arms: same-element stall, entropy spike, sample disagreement, solvability probe, none. Same items and tokens. Accuracy, fire rate, false-fire rate | Best trigger beats none by 2+ points with false-fire rate under 30% | High |
| A02.06-U3 | How much does an endorse-or-reject step recover of candidates written then dropped? | Candidate-review call before the final answer | S8, G2 | K18, K30, single-source for the rate. c08 (4 models, string match), d04, d05, d08 | With vs without review call on items where a gold answer appears in the trace (judge match). Recovered wrong minus broken right | Net gain 2+ points overall, regressions under 1 point | High |
| A02.06-U4 | Does a gating constraint check catch false insight (confident wrong shortcut)? | Mandatory shortcut check that can block output | G3, S8 | K19, K36, single-source. c18 (77-100% of errors, adversarial set), d07, d23 | Shortcut-inviting items. Arms: no check; non-gating check; gating check. Wrong-but-confident rate | Gating check cuts wrong-but-confident rate by 25% relative, losing under 2 points of correct answers | High |
| A02.06-U5 | Restart with a verified-facts summary vs patching a long wrong prefix | Restart rule after a failed frame | O, memory | K37, single-source. d12, d01, d11; d16 pilot n=5 | Inject wrong prefix of 0/200/800/1600 tokens. Arms: patch, restart with summary, fresh sample. Recovery rate | Restart beats patch by 5+ points at prefix 800 or longer | Med |
| A02.06-U6 | Does forced step-by-step hurt reframing items (human 57% vs 13%)? | Answer-first mode for reframing items | G11, S0 | K10, contested. b08 vs d18; d17 has no insight task; d19 abstract only | Short answer-first vs forced long chain, reframing vs procedural items, equal tokens. Accuracy by class | Interaction p<.05 and reframing class loses 5+ points under forced chain | Med |
| A02.06-U7 | Does a divergent-uses step beat a plain retry on fixedness items? | List alternative uses before solving | O6 | K40, single-source. d20 (+6.5 points, GPT-4, 2023); d24 gives a pre-use design | Pre-use vs none; divergent-first vs plain retry. Candle, two-string, MacGyver subset. Solve rate, infeasible rate | Divergent arm +4 points over plain retry on a 2026 model | Med |
| A02.06-U8 | Is restructuring in a single trace a jump or a ramp? | Jump-aware stall logic and log format | S, logging | K02, K34, contested. b01, b02, d01-d03; no per-trace fit exists | Probe at fixed checkpoints on 100+ items; fit jump vs linear per trace. Share better fit by jump; does jump predict correct | 30%+ of traces fit a jump better and jump traces are more often correct than ramp traces | Med |
| A02.06-U9 | Does a flat latent-progress probe predict failure better than trace length? | Probe-based stall signal and early exit | S (progress monitor), G12 | K35; d01, d04 (white-box); K04 contested | Forced-answer probe every k tokens; predict final failure from flat probe vs length alone. AUC | Probe AUC beats length-only AUC by 0.05 | Med |
| A02.06-U10 | Do relaxation plus a maximization criterion beat either alone for models (ten-penny, nine-dot as text)? | Pair a criterion with every constraint drop | O4, G | K08 established in humans (7-21% vs 72%); no LLM run | Hint arms: none, relax, maximize, both. Solve rate, human norms where available | Both beats relax-only by 15+ points | Med |
| A02.06-U11 | Does a pre-use mention of an object's usual role lower model solve rate (Duncker effect)? | Warning step: re-list non-standard uses | O6 | K39, single-source (d24 children 18% vs 89%) | Pre-use vs no pre-use, then divergent step. 40+ candle-style items | Pre-use drop of 10+ points, recovered by the divergent step | Low |
| A02.06-U12 | Does a cheap probe of a hidden hypothesis tip a stuck run (silent gate)? | Probe step before full restructure | S, O | K14, established in networks (c24, a22); no prompt test | Brief hypothesis probe vs full restructure vs plain retry | Probe arm matches the restructure arm at half the tokens | Low |
| A02.06-U13 | Does naming abduction at impasse beat a generic retry? | Name the inference type at impasse | O8 | K29, single-source; training method only (b21, c16) | Abduction prompt vs generic retry, equal tokens | +3 points on reframing items | Low |
| A02.06-U14 | Does a pause help? | Nothing (no pause operator) unless proven | none | K11, contested. b06 null; Sio and Ormerod unopened | A pause arm is just a fresh pass; fold into U1 | Skip unless U1 shows fresh passes beat the restructure arm | Low |

## Open questions we cannot test on our bench yet

- **Classic paradigms with human norms.** No nine-dot, candle or matchstick run on 2024-2026 LLMs exists, and we have no matched human data. Unblock by building text versions and taking norms from the literature or a small human panel.
- **Founding numbers.** Duncker 1945, Maier 1931, Wertheimer, Kohler: original data were not obtained. Unblock by reading the primary papers or books.
- **White-box probes.** Hidden-state probes (d04) need model access. Unblock by running the probe study on an open model.
- **False-insight rate in a verified agent.** Needs a labelled set of confident wrong shortcuts. Unblock by mining our own bench traces.
- **Private twins for 2025-26 reasoning models.** Needs a fresh item set written after model cutoffs (Mizumoto's open, blind and post-cutoff design, c10).
- **Sternberg and Davidson three-process theory.** Not researched in this pass.
- **Incubation meta-analysis.** Sio and Ormerod (2009) was cited from memory. Open it before any claim.
- **Verbal overshadowing in models.** Needs an insight-type item set where chain of thought can be switched off at equal tokens.

## Order to run

1. **U1 (restructure vs samples plus vote).** The central question. A null result lets us drop the operator from the active loop and save tokens.
2. **U4 (gating shortcut check).** Cheap, uses the same items as U1, and targets the best-documented failure (false insight, decorative checks).
3. **U2 (trigger rule).** Run on the same traces. It decides when U1's operator fires, so a good U1 result is not usable without it.
