# Neural and LLM proof search: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C06.05-U1 | Does a code-owned propose-check-backtrack loop beat best-of-N at equal tokens? | Loop as the default S3-S4-S5 machinery on checkable items | S3, S4, S5 | K01, K10; single-source (COPRA, GPT-4, one benchmark, weak sampler) | Items with code checks, plain pass 10-70%. Arms: one long attempt; best-of-N short; loop with feedback and backtracking. Metric: solve rate, tokens per solve | Loop beats best-of-N by 3+ points with CI excluding 0 on 2 item types | High |
| C06.05-U2 | Is error-only feedback better than showing the failed attempt? | Rule: pass the diagnostic, not the failed text, in S5 | S5, G2 | K17 contested; d07 abstract only (11 problems, 2 models); b15 token-confounded | Items that fail first try. Arms: fresh resample; error-only retry; failed text + error. Metric: 2nd-try solve rate, copy rate | Error-only >= resample and beats failed-text arm by 3+ points | High |
| C06.05-U3 | Does refinement on checker output beat fresh resampling at equal tokens? | Keep S5 refine rounds (max 2); else cut S5 and resample | S5, G2 | K17 contested; Seed-Prover has no matched ablation (d06); Goedel-V2 40k vs 30k tokens | Same items; refine 2 rounds vs 3 fresh samples at same tokens | Refine wins by 3+ points; if resample ties, drop refine for those item types | High |
| C06.05-U4 | Can a code-computed state score rank partial work as well as a learned or model-likelihood score? | Code ranking of open branches (open goals, size, check pass count) at S4/S6 | S4, S6 | K04; BFS-Prover (model likelihood, no head, d12) ; no head-to-head; older trained models only | Branching items at fixed node budget. Arms: code score; model self-rating; random | Code score beats random by 3+ points and beats self-rating | High |
| C06.05-U5 | Is "try the tool first" as good as a model-chosen tool call? | Fixed rule: run solver/executor first at each state | O (tool call), S4 | K06; Thor baseline is a union not a rule (d11); Isabelle only | Items with an available solver. Arms: tool-first; model decides; model only | Tool-first within 2 points of model-decides at lower token cost | Med |
| C06.05-U6 | Does a verified-lemma store help a frozen model across subtasks? | Subgoal library from planned memory into S3 | memory, S3 | K29; LEGO +3.3 (d05); not equal-token; single-source | Item families with shared sub-results. Arms: store on vs off. Metric: solve rate on later items | +2 points or more on later items with CI excluding 0 | High |
| C06.05-U7 | Does truncate-and-resume (keep verified prefix) beat restart? | Resume operator at S5/S6 | S5, S6, O | K14; DeepSeek-Prover-V1.5 only; figure values not read (b24) | Multi-step items with step checks. Arms: restart; resume from last verified step | Resume wins on long items by 3+ points at equal tokens | Med |
| C06.05-U8 | What is the raw pass-rate floor below which a scaffold adds nothing? | A hard S0 rule: skip search below the floor | S0, G12 | K09; COPRA GPT-3.5 gains little; Hilbert fixes a strong prover; no clean sweep | Bin items by raw pass rate (0-5, 5-20, 20-60%); scaffold vs plain per bin | Gain in lowest bin < 1 point and > 3 points in the middle bin; floor set at the crossing | High |
| C06.05-U9 | Does a written plan pay for its tokens when the executor is strong? | Plan-then-fill only for weak executors or hard items | S3 | K08 established with weak executors; K26 single-source (DSP+ drafts add 0-4 points) | Multi-part items. Arms: direct; plan+fill; fill without plan | Plan arm beats no-plan arm by 3+ points after counting plan tokens | Med |
| C06.05-U10 | Is decomposition capped at depth 2-3 right, and does it help at equal tokens for a frozen model? | O3 limit in the tree rules (already depth 2) confirmed or raised | O3, tree rules | K16 established as helps; K28 single-source depth curve; no equal-token run | Multi-step items. Arms: no decomposition; depth 1; 2; 3 | Depth 2 beats none by 3+ points; depth 3 adds < 1 point | Med |
| C06.05-U11 | When no code check exists, what is the false-pass rate of an LLM verifier on our tasks? | A numeric rule for when a verifier may be used as a hint | G2, G5, S4 | K25 established elsewhere (38-75% false pass); not measured on our items | Known-wrong and known-right outputs from our tasks; several differently prompted judgements. Metric: false-pass, false-reject | Use only if false-pass < 10% and stable across 3 prompts; otherwise hint only | High |
| C06.05-U12 | Does parallel independent sampling match a tree that reuses prefixes? | Tree reuse only where it wins | S3 | K13; DS-V1.5 +2.5 to 3.3 at about 200k samples; single-source | N independent attempts vs tree with prefix reuse, equal tokens | Tree wins by 3+ points; otherwise keep independent attempts (G11) | Low |
| C06.05-U13 | Conjecture-and-refute: does cheap refutation of many guessed answers help on answer-search items? | Candidate guess then refute step in S3-S4 | S3, S4 | K21; AlphaProof, single-source; needs a separate LLM and many guesses | Answer-search items. Arms: single answer; many guesses refuted by code | +3 points over single answer at equal tokens | Med |
| C06.05-U14 | How much is contamination inflating our public-set results? | Restated-twin split as standard evaluation | G3, evaluation | K12, K27; unmeasured for frontier LLMs | Old public items vs restated twins, same arms | Accuracy gap above 5 points on old vs twin means twins are mandatory for all tests | High |

## Open questions we cannot test on our bench yet

- **Formal prover access.** We have no Lean or Isabelle environment on the bench. A formal run would give an exact checker and clean error messages. Unblock: install Lean 4 with a small mathlib subset and use 50 to 100 fresh statements.
- **A learned value head.** We cannot train one. U4 only tests a code score against self-rating and random, not against a trained head.
- **Weak-checker domains.** Planning, open-ended reasoning and novelty tasks have no exact checker. Only informal-math verifier papers speak to them. Unblock: build known-wrong item sets for those tasks (U11).
- **Contamination of frontier models.** No paper measured it for miniF2F or PutnamBench. Unblock: our own twin split (U14) gives a rate for our items only.
- **Matched-token formal comparison.** No paper pairs a loop with best-of-N in Lean at equal tokens. Unblock: run U1 on a small Lean set once Lean is available.
- **Test-time training (AlphaProof TTRL).** Changes weights; not possible for a frozen agent. The frozen analogue (solve variants first and keep them as context) is untested.
- **Seed-Prover refinement claim.** No matched ablation exists; the paper is closed. Our U3 is the only way to check it.

## Order to run

1. **U1 (propose-check-backtrack vs best-of-N).** It tests the core S3-S4 design, and no paper answers it at equal tokens.
2. **U8 plus U14 (raw-pass floor and contamination twins).** One item set serves both, and the results decide which later tests are worth running (G12, G7).
3. **U2 and U3 (error-only feedback; refine vs resample).** They share items and decide whether S5 earns its tokens; the literature is contested and the cost is low.
