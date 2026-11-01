# Counterexample finding: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C06.10-U1 | Does a code-run differential (run both fit rules on generated inputs) pick the right rule better than the model choosing a test by thought? | S7 step: generate inputs in code, run both rules, send the most splitting input to the oracle | S7 | K33, d14 (random = adaptive LLM tester); single-source, code only | Free-form S7 vs code differential; ARC items with 2+ fit programs; share picking the right program on held-out grid | Gain >= 3 points with paired 95% CI above 0 | High |
| C06.10-U2 | Does the opposite-test (TiO) instruction help on real tasks, not Wason triples? | One line in S7: "pick the input positive under one rule, negative under the other" | S7 | K12, b07, c11; single-source, open Qwen3 models, small for non-thinking | Plain S7 vs TiO S7; ARC two-rule items and hidden-rule items; right-rule rate and I:C | Gain >= 3 points, CI above 0, on our model | Med |
| C06.10-U3 | Is a witness checked by code (hypotheses plus negated conclusion, "none found" allowed) better than a free-form witness? | Formal S7 witness protocol | S7, G3 | K30, d05-d07; established for training, untested as inference scaffold | Free-form vs checked; small claims half true; invalid-witness rate and false refutation of true claims | Invalid witnesses < 5% and no loss in valid refutations | High |
| C06.10-U4 | Does a model finder (Mace4, Nitpick, SMT) raise valid refutation over the unaided model? | Tool call in S7 for formal claims | S7 tools | K29, K16, K32; no direct study; Logic-LM both ways (d16) | LLM alone vs LLM plus finder (30 s); small formal claims, half true; valid refutations, wasted calls | Gain >= 5 points on translatable claims and no loss elsewhere | Med |
| C06.10-U5 | Does a union of falsification strategies beat the best single one? | S7 portfolio (random, boundary, opposite, small search) | S7, O | K04, K34, b05, d13; single-source | Best single vs union; planted-bug code items; union gain | Gain >= 4 points over the best single | Med |
| C06.10-U6 | Does splitting test design from hypothesis update help? | Two calls in S7 | S7 | K14, b11 (19/50 vs 13/50); small N, cross-model | One call vs two calls; WILT-style 50 rules; rules found | Gain >= 4 of 50 over 3 seeds | Med |
| C06.10-U7 | Is a prose critique worse than an executable counterexample critic? | Critic role must emit a runnable input | S7, G5 | K26, d08, d09; code only, false alarms uncounted | Prose critic vs executable critic; wrong-answer items; valid rate and false alarms | False alarms down >= 30% with no loss in valid finds | Med |
| C06.10-U8 | Does a check-intended-hypotheses step cut trivial counterexamples? | Domain check before accepting a refutation | S7, G3 | K22, K36, d10; single-source, same-model review | Accept vs hypothesis-check; textbook claims; share trivial judged by independent model and human sample | Trivial share down >= 20% | Med |
| C06.10-U9 | Does a claim-repair step (Lakatos) after refutation beat discard and retry? | New operator "repair claim" after refutation | O (new), S5 | K28, a13 not opened; d09 code only | Discard vs repair; items with known repair; final answer correct | Gain >= 3 points | Low |
| C06.10-U10 | Is a think-before-test step worth its tokens? | Short reasoning before test choice | S7, G11 | K05, b15; single-source, figure only | Direct test vs think-then-test; planted-bug items; fault exposure | Gain >= 3 points at equal tokens | Low |
| C06.10-U11 | Do generated adversarial tests rank candidates better than majority vote? | Test-based selector at S7 | S7, G4 | K07, K35, c25, d15; single-source, code | Majority vs generated-test selection (trusted tests kept first); best-of-N items; accuracy | Gain >= 3 points | Med |
| C06.10-U12 | Is the verdict-to-witness gap present in our agent? | Score witness quality, gate decisions on witness not verdict | bench, S8 | K08, c08; single-source | Verdict-only vs strict witness scoring; CounterMath-like items; gap in points | Gap >= 10 points (then add witness check) | High |

## Open questions we cannot test on our bench yet

- CASC model-finding track results for MACE, Paradox, Mace4 against provers. The reports were not obtained. Unblock: fetch CASC reports from tptp.org.
- Expert review of LLM-found conjecture counterexamples (non-trivial survival rate). Needs a mathematician; same-family review is not enough.
- Natural-language reasoning refutation by trained critics. No benchmark; code-only evidence. Unblock: build a small set of plausible-wrong reasoning traces with known flaws.
- Cost of a wasted S7 test and false-alarm cost. No data in the literature; we must log them on our own runs.
- Wason-type effects in people versus LLMs as a mechanism question (bias vs rational positive test vs failing to think of falsifiers). Needs a human-model comparison we cannot run.
- Unopened sources: McCune 1994 MACE, Paradox, Kodkod, QuickCheck, Lakatos, Klayman and Ha original. Unblock: read before citing any numbers from them.
- CounterMath out-of-distribution gains with confidence intervals (needs training; we do not train).

## Order to run

1. C06.10-U3 (checked witness protocol): cheap, code-only, targets the biggest known failure (35 percent invalid counterexamples).
2. C06.10-U1 (code-run differential vs thought-chosen test): cheap on ARC, and directly tests whether S7 itself pays for itself.
3. C06.10-U12 (verdict vs witness gap): free to run on existing logs, and decides whether the other tests are needed at all.
