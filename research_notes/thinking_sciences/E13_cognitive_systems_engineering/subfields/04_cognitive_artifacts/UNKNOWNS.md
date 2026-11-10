# Cognitive artifacts: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E13.04-U1 | Does re-rendering active rules and open checks in every state prompt cut violations? | Rule block rendered by code in each S prompt | G / S | K26, K29; b01 human-only, d04 indirect; single-source | A: rules in system prompt only; B: rules re-rendered each state. Constraint-heavy puzzles, 100+ items, 3 seeds. Violations per run, solve rate | Violations down 20% relative or more, solve rate not lower, CI excludes 0 | High |
| E13.04-U2 | Does a code validator with the error shown at the point of failure beat no validator? | Validator step on every model output | G2 / G7 | K02; a17 single run, 1-3 points near noise; older model | A: no validator; B: validator plus error feedback. Code and grid items, same total tokens including retries. Invalid-output rate, pass rate | Pass rate +3 points or more at equal tokens | High |
| E13.04-U3 | Is reason-then-format better than inline structured output on our model? | Two-step answer: free reasoning, then formatted answer | output format | K08; contested; d11-d13, not token-equal | A: inline JSON; B: free reasoning then reformat (second call or code parse). Mixed reasoning items. Accuracy | B better by 2 points or more, or equal at fewer tokens | High |
| E13.04-U4 | Are wrong tool returns adopted, and does a verification instruction or code cross-check cut it? | Verification instruction and second independent check on disagreement | G2 / G10 | K27, K32; d06, d08; single-source, other models | Inject wrong returns at 20%. Arms: none, instruction, instruction plus code cross-check. Adoption rate, final accuracy | Adoption down 30% relative or more, accuracy not lower | High |
| E13.04-U5 | Does state display size matter (summary vs window vs full; last-k vs full history)? | Fixed display budget per tool and last-k history | S | K03, K14; a17 single-source, 2024 model; memory part contested | Vary window and history length on long-state items. Pass rate, tokens | A setting beats full by 3 points or more at fewer tokens | Med |
| E13.04-U6 | Does a capped cheap probe before commit save tokens or only add steps? | One probe step (run check, inspect value) before each commit | O probe | K25, K30; d10 web agent only, a01 human timings | A: no probe; B: one probe per state, capped at 2. Code and puzzle items. Tokens to solve, pass rate | Pass rate up, or tokens down 15% or more at same pass rate | High |
| E13.04-U7 | Does showing only state-relevant tools beat a fixed small set? | Per-state tool exposure | O tools | K12; b09, d17 single-source; no equal-prompt control | A: fixed small set; B: per-state set of equal prompt size; C: all tools. Tool-selection accuracy, pass rate | B beats A by 3 points or more | Med |
| E13.04-U8 | Can a prompted model calibrate tool-vs-recall with predictions and feedback? | Predict-then-choose step with hit-rate feedback | G calibration | K18, K28; humans [E], models only by training (d09) | A: free tool use; B: predict whether a tool is needed, running hit rate shown. Items answerable unaided. Unneeded calls, accuracy | Unneeded calls down 20%, accuracy not lower | Med |
| E13.04-U9 | Does position of goals and checks in the state matter on current models? | State ordering rule (goals first and last) | S ordering | K10; contested; a24 2023 models, d02, d03 length only | Same state with checks at start/end vs middle, at 8K and 32K. Pass rate | Position gap of 3 points or more | Med |
| E13.04-U10 | Do O1-O8 work better as separate code-called steps than as one prompt? | Operators as callable tools | O | K15; c15 single-source, math only | A: operators in one prompt; B: each operator a separate call. Equal tokens. Impasse items. Pass rate | B +3 points at equal tokens | Med |
| E13.04-U11 | Does a bare scaffold (no or random model) score high on our items? | Scaffold-only control arm in the bench | Bench | K31; d14 single-source | Run scaffold with a random model on every bench item. Score | Any item where control exceeds chance by 10 points is fixed or dropped | High |
| E13.04-U12 | Does stored reflection or paged memory beat recent-only context? | Reflection buffer or paged retrieval | memory | K13, K14; contested | A: recent-only; B: reflections; C: retrieved memory, equal tokens. Multi-attempt items | B or C +3 points at equal tokens | Low |
| E13.04-U13 | Does a scripted pipeline beat a free agent loop at equal cost? | Fixed pipeline as default control flow | Architecture | K16; b04, d01; contested | A: scripted localise/repair/validate; B: free loop. Equal cost. Pass rate | A within 2 points of B at lower cost | Low |
| E13.04-U14 | Is there a tool-complacency effect when tools are always right? | Periodic independent check on an always-correct tool | G | K19; human only (a14) | Tool correct for N steps, then wrong once. Detection rate with and without a periodic check prompt | Detection drops over steps and the check restores it | Low |

## Open questions we cannot test on our bench yet

- Founding numbers (Larkin and Simon 1987, Norman 1991, Hutchins 1995) are unread. Unblock: get the full texts through a library.
- Equal-token comparisons do not exist in the literature; every LLM result here has a cost confound. Unblock: our own token-matched harness runs (U1-U9).
- Why a tool layer hurt GPT-5-Nano (44 to 14): needs a model-size sweep on our own models.
- Dependence or skill loss from long scaffold use: needs fine-tuning, which we do not do.
- Human epistemic-action timings do not map to tokens; only the principle is testable.
- Reliability labels on tools: partial effect in d06; needs a labelled-reliability arm with graded reliability.

## Order to run

1. **U11, scaffold-only control.** Cheapest; needs no real model calls; protects every other test from a scaffold artifact.
2. **U1, rules re-rendered each state.** Highest expected gain; direct transfer of the best human result (Zhang and Norman); costs only prompt text.
3. **U4, injected wrong tool returns.** Large measured effect elsewhere (35-68% adoption), and the fix is cheap (an instruction plus a code cross-check).
