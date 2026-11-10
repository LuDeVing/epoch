# Interactive theorem proving: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C06.04-U1 | Does check-then-repair beat k independent samples outside proofs (code with tests, ARC held-out check)? | A repair round in S5 with a fixed budget split | S5, S8 | K04, contested: COPRA 26.63 vs 15.98 and Goedel-V2 92.7 vs 92.2 (formal only); Olausson 1.05x and 0.97x (code) | k samples + select vs 1 sample + 2 repairs with raw output, rest on first attempts; ARC and code items, 3 seeds; pass rate on unfitted part | repair at least 1.10x resampling with a 95% interval above 1.0 | High |
| C06.04-U2 | Raw checker output vs model-written critique in the repair step | Rule: repair prompt gets raw located output only, no self-critique | S5 | K20: 33.3% vs 52.6% repaired (small, code, human expert vs own); d05, d06 | same failing attempts, two repair prompts; equal tokens; repaired rate and right-to-wrong flips | raw beats critique by at least 5 points, flips not higher | High |
| C06.04-U3 | Verifier hygiene: how often do vacuous or fitted passes occur in our own bench? | Verifier rules: reject empty or always-true checks, second independent check | G3, S8 | K10, K17: lean-gym 21.1% false rejects, sorry bug, 398 certified faults; formal domain only | 50 known-good, 50 known-bad, 20 vacuous answers through our verifier; false-reject and vacuous-pass rates | any vacuous pass above 0, or false rejects above 2%, then add the rule | High |
| C06.04-U4 | Does lemma decomposition with a verified library beat flat prompting at equal tokens? | O3 as a standing step with a subgoal library | O3, memory | K13: Hilbert D=0 75 vs D=3 98.7, not token-matched; reasoner dominates (70.0 vs 13.3); single lab family | flat vs decompose + library, long multi-step items, equal tokens; pass rate and tokens per solve | at least +5 points on long items with no loss on short | High |
| C06.04-U5 | Do retrieved verified prior cases help non-formal tasks? | Verified-case retrieval in memory, shown after the first attempt | memory | K22: Rango +47% rel., LEGO +3.3, Hilbert tokens 4.0M to 2.3M; formal only, human-curated names | none vs verified vs unverified retrieval; repeated problem classes; pass rate and tokens | verified beats none by at least 3 points and beats unverified | High |
| C06.04-U6 | Does a statement or restatement guard cut passes on the wrong problem? | S1 restatement check before S8 accepts | S1, S8 | K24, d10, d08: 20% to 31.8% flawed statements; LLM audit precision 0.24-0.30; single-source | perturbed or reworded items, guard vs none; rate of passes on the wrong target; token cost | wrong-target passes cut by at least half at under 10% tokens | Med |
| C06.04-U7 | Plan in prose then convert to checkable steps (DSP style) with 2025 models | S3 plan-then-check path for long items | S3, O3 | K07: DSP 20.9 to 39.3, Lyra replicates (38.9/39.7); older models; informal draft adds +0.83 over retrieval in COPRA | plan-then-check vs direct, equal tokens, long items | at least +4 points on long items and no loss on short | Med |
| C06.04-U8 | One long CoT vs several short attempts in the generator under a verifier | A mode rule: CoT for hard items when a check exists | G11, S3 | d02, d03: 671B CoT pass@32 82.4 at about 216k tokens vs non-CoT pass@1024 76.7 at about 780k (our arithmetic, not clean); G11 says short wins elsewhere | n short vs n/8 long at equal tokens, split by difficulty | long wins on hard items by at least 5 points; then a difficulty-conditioned mode | Med |
| C06.04-U9 | Which failure categories can a scaffold fix without training? | Category-specific repair rules (bad reference, wrong rule, unfinished goal) | S5, S6 | K21: PALM categories, 49.6% wrong theorem application; backtracking 6.5 to 40.4; GPT-3.5, Coq only | tag 100 of our failures by category; test one rule per top category | any category covering above 20% of failures where a rule gives at least +3 points | Med |
| C06.04-U10 | Does a hammer-style tool call (solver, code run) as a model action beat model-only steps at equal tokens in our tasks? | A "call tool" action inside S3/S4 | O, S4 | K03 established in formal domain: Thor 39.0 to 57.0; hybrid wins; effect size outside proofs unknown | model-only vs model + tool action; numeric and algebra items | at least +5 points at equal tokens | Med |
| C06.04-U11 | Do spec-first planning and low open-error counts help an LLM loop? | Rule: plan first, keep unresolved failures under 5 | S5 | K25: N=8 human experts, no LLM; single-source | plan-first vs reactive loops on multi-step items; pass rate and time | at least +3 points, no extra tokens | Low |
| C06.04-U12 | Contamination of our own bench items by public provers or models | Post-cutoff or perturbed variants as standard evaluation | G | K23, contested: Putnam-AXIOM -19.6 points; Rango 30.1 vs 28.3 | original vs perturbed variants, per arm | score drop above 5 points means we drop the item set from headline results | Low |

## Open questions we cannot test on our bench yet

- User studies of humans using proof assistants with LLM copilots (time, error rate, trust). No study exists in our evidence set. Unblock: run a small study ourselves, or find 2025-26 reports.
- Output audit of Seed-Prover and Hilbert for flawed statements and loopholes. Needs their released outputs and a Lean toolchain.
- Whether a kernel exists for our task families. Most of our tasks have only partial checks. Unblock: build a partial checker for one family (algebra, small programs) and use it as a proxy.
- Matched-token ablation of decomposition inside provers. Needs a Lean setup and prover access; out of scope for the bench.
- Independent re-run of IMO 2025 results and variant tests for Lean provers.
- Whether a kernel bug (July 2026 snippet, unopened) changes the trust claim. Unblock: read the Lean release notes.

## Order to run

1. **U3 verifier audit.** Cheapest (no model calls beyond a fixed set), and every other test is only valid if the verifier is sound.
2. **U1 plus U2 together.** Same failing attempts feed both; they decide whether the S5 repair step earns its tokens at all (the one contested claim with the most weight).
3. **U5 verified-case retrieval.** Strongest in-domain effect (+47% relative in Rango) and a direct memory-design decision; test it on repeated problem classes.
