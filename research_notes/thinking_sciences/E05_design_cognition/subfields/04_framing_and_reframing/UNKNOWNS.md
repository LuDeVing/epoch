# Framing and reframing: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

All tests: arms at equal tokens (setup and reframe calls counted), at least 3 seeds, plus a same-length unrelated-prompt arm (K27).

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E05.04-U1 | Does an O8 step that changes the goal or strategy beat plain resampling? | O8 as a real operator with a stated precondition | O8 | K01, K24, K29; single-source; human null (Shin); old models | (a) resample; (b) one goal/strategy change then solve; (c) paraphrase-only; ARC + BRAINTEASER; pass rate | (b) beats (a) and (c) by 2+ points over 3 seeds, CI above 0 | High |
| E05.04-U2 | How big is prompt noise on our items? | A standing paraphrase and unrelated-prompt control in every test | G7 | K08, K26, K27; single-source; table read | baseline vs paraphrase vs same-length unrelated prompt; all bench items; pass-rate spread | Spread measured; later bar = 2x spread (about 2 points if it matches d12) | High |
| E05.04-U3 | What trigger should fire O8? | A rule: fire on localised failure after K steps on one line | G1, S6 | K07 (established, direction only), K28, K23; single-source for the exact rule | O8 always / never / generic doubt / localised failure after K steps; ARC with checks; pass rate, tokens, false-trigger rate | Localised trigger beats "never" by 1+ point and beats "always" with fewer tokens; false triggers under 10% on correct items | High |
| E05.04-U4 | Does restart with compacted confirmed facts help on current models? | Restart rule in S6 (K=5, M=3) | S6, O8 | K10; contested; 5 puzzles, no statistics; indirect d06 (15-20% recovery) | continue vs restart with M=3 facts vs restart with all facts vs restart with none; BRAINTEASER + multi-turn ARC probes; pass rate, questions used | Restart-with-facts beats continue by 3+ points and beats restart-with-none | High |
| E05.04-U5 | Is step-back net positive on current reasoning models when gated? | Gated step-back as S1 sub-step for knowledge-heavy classes | O2, S1 | K05; contested; old models plus one 2026 negative (d11) | plain / step-back always / gated by class / spurious; science-style and ARC items; net fixed minus broken | Net fixed minus broken above +3 points on a class, no loss elsewhere | Med |
| E05.04-U6 | Does a rephrase step help only ambiguous items? | Rephrase in S1 behind an ambiguity check | S1 | K06; single-source; GPT-4 2023 | plain / RaR / RaR gated; ambiguous vs clear subsets; pass rate by subset | +3 points on ambiguous subset, within 0.5 point on clear subset | Med |
| E05.04-U7 | Does showing the model's own first frame to later attempts anchor them? | Hide first frame from later attempts; show opposing frames together | G4, S3 | K12, K22 (prompted anchors established); own-frame untested | later attempts see first frame / none / two opposing frames; open and ARC items; feature overlap with first frame, pass rate | Overlap rises 20%+ with one shown frame, or two-frame arm gives +2 points | Med |
| E05.04-U8 | Must a reframe change content, or is a style rule enough? | Require O8 output to name a changed representation or goal | O8, O6 | K29; single-source (30-item rewrite, not equal-token) | content reframe / style rule / plain; brainteasers and ARC; pass rate | Content arm beats style arm by 2+ points | Med |
| E05.04-U9 | Do distinct named strategies beat paraphrased resampling? | S3 prompts for different strategies; group by strategy | S3, O8 | K24; contested; maths only, small models | N same prompt / N paraphrased / N distinct strategies; ARC, maths; best-of-N | Distinct beats paraphrase by 1+ point at equal tokens | Med |
| E05.04-U10 | Is disagreement between self-made frames a good trigger? | Disagreement trigger for S6 | G1, S6 | K24 (d15), K23; single-source | trigger on disagreement / on failure / on agreement-with-outside-check; pass rate and tokens | Beats failure-only trigger by 1+ point, or matches it at fewer tokens | Med |
| E05.04-U11 | Does a pick-a-method step before solving beat fixed CoT? | Method selection at S0 | S0, O8 | K18; single-source; old models; small gain on MATH | fixed CoT vs pick-method-then-solve; mixed bench; pass rate | +2 points at equal tokens, not driven by one class | Med |
| E05.04-U12 | Does longer reasoning hurt the reframe step? | Per-mode cap on O8 reasoning length | G11 | K11; contested; clinical and language tasks | O8 with short / medium / long caps; total tokens equalised with resamples; pass rate | Short cap at least equal to long cap on 80%+ of classes | Med |
| E05.04-U13 | Does a flip rate between two wordings give a useful signal? | Two-wording check at S0 or as trigger | S0, G1 | K16; single-source; one scenario; a debias prompt widened the gap | answer flip rate between wordings with and without O8; all items in two wordings | Flip rate falls 25%+ with O8, pass rate does not drop, and flips predict error | Low |
| E05.04-U14 | Does "invert each assumption" add to O4? | Sub-step in O4/O8 | O4, O8 | K15; single-source; human, one group | plain / invert-assumptions sub-step; insight-type and ARC items; pass rate | +2 points at equal tokens | Low |
| E05.04-U15 | Does a clearer frame cost novelty in open mode? | Separate clarity and novelty scores in open mode | G8 | K19; contested; rubric mismatch; n=32 | open-mode items; blind-rated clarity and novelty; with and without O8 | Clarity up and novelty not down by more than 0.3 on a 5-point scale | Low |
| E05.04-U16 | Do expert-quality reframe instructions beat naive ones? | Better O8 prompt text | O8 | K04; contested; human post hoc subgroup | naive vs expert-written reframe prompt; same items; pass rate | +2 points at equal tokens | Low |

## Open questions we cannot test on our bench yet

- **Human-rated frame quality for open design.** Our bench scores answers, not expert-rated frames. Needs blind expert raters and design briefs. Would show whether Shin's null holds for current models and for our O8.
- **Equivalence for Shin 2025.** Raw ratings, or means and SDs, are needed for a TOST. Ask the authors or find a data release. Until then the null excludes only effects above about 0.45 SD (K25).
- **Foundations in numbers.** Dorst and Cross full text, Sio 2015 effect sizes and Knoblich 1999 solution rates were not reachable. Publisher access is needed.
- **Reasoning-model results for step-back and RaR.** No paper tests them at matched tokens. Our own run (U5, U6) is the only route.
- **Cost of a false trigger in a full agent.** Needs the harness to log fires on items already correct (U3).
- **Own-frame anchoring in agents.** No published show/hide experiment (U7).
- **Single ablation of reframing types** (abstraction, rephrase, inversion, goal change). Needs one design with all four at equal tokens; U1, U5, U6, U8 and U14 are the pieces.
- **Replication of Sood 2026.** n=7, no statistics. Needs more raters and blind rating.

## Order to run

1. **U2 (noise control).** Cheapest, and it sets the bar for every later test: without it a 2-point gain cannot be read.
2. **U3 (trigger).** G1 already says fire only on a signal; this fixes which signal and measures false-trigger cost before O8 is used anywhere.
3. **U1 (goal/strategy reframe vs resample).** The central question for O8. If it fails, O8 stays [S] and gated, and U4 to U9 decide which cheap parts survive.
