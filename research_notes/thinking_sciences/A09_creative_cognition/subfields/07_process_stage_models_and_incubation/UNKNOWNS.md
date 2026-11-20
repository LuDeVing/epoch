# Process stage models and incubation: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A09.07-U1 | Does restarting a failed item from the bare problem plus a 2-line lesson beat continuing in context? | "Restart with lesson" as the first S6 move | O (S6), G fixation reset | K07 contested, K23 contested, K25 single-source; d13, d14, d16, d17; human d about .2 | Arms: continue / fresh resample / fresh + 2-line lesson. Items: first-failed BRAINTEASER and ARC items. Metric: solve rate, net fixes minus breaks | Lesson arm beats fresh resample by 5+ points on stuck items, no loss on random set | High |
| A09.07-U2 | Does an unrelated filler step before the return add anything over restart alone? | A pause/filler step | O: pause step | K04 single-source (human only), K21 no LLM test; a07 | Arms: restart with 300-token unrelated filler / restart without. Same stuck set. Metric: solve rate | Filler arm beats no-filler by 3+ points with CI excluding 0 on two item types | Low |
| A09.07-U3 | Does a context reset undo misleading-hint fixation in LLMs? | Drop-trace rule when a planted or detected misleading cue exists | G: fixation reset | K25 single-source; c15, c16, d16, d17; a20, a21 interaction n.s. | Arms: continue / reset to problem only / reset + "ignore hint" note. Items: GSM-IC-style planted hints, misleading-frame riddles. Metric: accuracy on hint-failed items | Reset arm recovers 30%+ of the accuracy lost to the hint | High |
| A09.07-U4 | Is offline notebook rewrite worth its tokens for predictable follow-ups? | Idle pass that writes a notebook after a long session | memory | K13 established, K14 and K22 single-source; b24, d01-d06 | Arms: no pass / offline pass / same tokens spent at test time. Items: multi-question contexts binned by predictability. Metric: accuracy at equal total tokens (offline + test) | Offline wins in the top predictability bin by 5+ points at equal total tokens | Med |
| A09.07-U5 | Does Wait-style continuation beat independent restarts on lateral-thinking items? | A single "Wait" nudge after a failing check | O: re-examine | K15 established on math; K16 and K23 against it; d07, d08, d09; no insight test | Arms: Wait / best-of-k vote / restart + lesson at equal tokens. Items: BRAINTEASER, RAT-like. Metric: accuracy | Wait beats vote by 3+ points on insight items | Med |
| A09.07-U6 | Does a decode-level thought-switch penalty (stay on a line) help our agent? | Switch limit inside S3/S5 | G: stay on a line of attack | K17 single-source; c12, c13 (prompt-only failed) | Arms: no penalty / penalty / prompt-only. Items: hard math, ARC. Metric: pass@1, line changes | Penalty arm +2 points pass@1 on two sets, and no loss on easy items | Low |
| A09.07-U7 | Does a pre-attempt pause (plan or other task before the first try) help? | Early planning step in S0 | S0 | K05 single-source, human only; a13, b10 | Arms: plan-first / direct. Items: insight puzzles, open tasks. Metric: solve rate, divergence | Plan-first arm +4 points on insight items, no loss on easy ones | Low |
| A09.07-U8 | Does more preparation before the break raise the gain? | A minimum first-pass budget before S6 fires | O: preparation budget | K03 single-source, correlational across studies (r .40, .60); a06 | Arms: 1k vs 4k tokens of first attempt, then identical restart. Metric: gain on stuck items | 4k arm's restart gain larger by 3+ points than 1k arm's | Low |
| A09.07-U9 | Does an editable scratchpad help on insight items? | A scratchpad state in S3/S5 | memory | K12 single-source, human only (43% vs 6%); b21 | Arms: scratchpad tool / none. Items: insight puzzles, small ARC. Metric: solve rate | Scratchpad arm +5 points | Med |
| A09.07-U10 | Can a cheap non-oracle impasse detector be trusted? | A detector that triggers S6 | G, S6 | K24 established in the negative (no oracle = no gain); d11, d12, d15 | Arms: test-failure trigger / self-doubt trigger / consistency-across-samples trigger. Metric: net fixes minus new breaks | Consistency trigger beats test-only by 2+ points when no test exists, with fewer breaks | High |
| A09.07-U11 | Do distractor instructions and exemplars generalise to our own prompts? | A fixed "ignore irrelevant" line plus distractor exemplar in S1 | S1 input hygiene | c16 (+35.5 points on 0-CoT, 2023 models); newer models unknown | Arms: plain / ignore line / ignore line + exemplar. Items: GSM-IC-style, hint-laden tasks. Metric: accuracy | +3 points on a current model | Med |
| A09.07-U12 | Does a lighter "partial consolidation" (short summary rewrite, not full sleep-time) match the N1 effect in spirit? | A short mid-task summary step | memory | K10 human N1 83% vs 30% single lab; K11 contested; a26, b18, b19 | Arms: summary-then-continue / continue. Items: multi-step puzzles with hidden rules. Metric: solve rate | +5 points at equal tokens | Low |

## Open questions we cannot test on our bench yet

- True Sio and Ormerod weighted d and moderator effects (K26): needs the paywalled APA PDF. Does not block any test.
- A preregistered, outside-lab replication of Smith and Beda (K07): a human study; unblock by finding or running one. Our LLM tests U1 and U3 do not need it.
- Whether any 2024 to 2026 LLM paper tests incubation, aha or Wallas prompts (K21): search was blocked. Re-run literature search with budget.
- A definition of "impasse" for an LLM without a test (U10 tests one proposal).
- Human-style immediate incubation vs delayed incubation for LLMs: needs a design for what the "different task" is.
- Newer-model BRAINTEASER and insight numbers (2023 numbers only): needs a run of current models on our bench.
- N1 sleep replication in humans: no bench route.

## Order to run

1. **U1 (restart with lesson vs continue vs resample).** Cheapest and closest to existing S5/S6 code. It also tests the core "forgetting" idea.
2. **U10 (impasse trigger: test vs doubt vs consistency).** Every retry step depends on it, and the established result says oracle signals decide the gain.
3. **U3 (context reset against planted misleading hints).** Directly tests the Smith/Beda mechanism in LLMs, where no study exists.
