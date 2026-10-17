# Bug pass 2026-10-17 (night): seams report

Scope: bugs where two areas meet. No product code was changed. Every finding below has a test in
`harness/tests/test_bug_seams.py` that fails on master (13 fail, none xfail). The owner fixes the code and the
test then passes.

Method: functions touched by more than one branch in the last two days (`ideate_round` 16 commits, `_one` 13,
`_finish` 13, `_write_tree` 10, `plan_tree` 7, `_rounds` 7, `replan_tree` 6, `load_state` 6, `run_card` 6); every
output file traced to a reader; changed signatures traced to call sites; CLI flags traced to reads; one mock dry
run (`--profile binpack_nobase --implement 3 --rounds 2 --max-sketch-calls 10`) with every output file read.

## Ideation half of loop.py

| Test | Severity | Bug |
|---|---|---|
| S3 `test_origin_stats_count_idea_contexts_not_interrogation_calls` | medium | `deepen_round` writes offshoot sketches with no `origin` and no `round`. `_origin_stats` defaults a missing origin to "tree", so each interrogation call counts as a tree context and offshoots of off-map ideas count as tree sketches. The dry run's source_yield.json said 83 tree contexts; discovery.json counted 27. The rule-3 share shift compares unlike numbers. |
| S1 `test_max_sketch_calls_cap_holds_with_memory_free_contexts` | medium | `_pick_memory_free` runs after the `--max-sketch-calls` cap and adds one context per part with a single context. With cap 10 the dry run ran 12 and 15 idea contexts. |
| S2 `test_memory_free_copy_keeps_the_context_text[owner, contradiction]` | medium | For owner and contradiction contexts the seed slot holds the prompt text. The memory-free copy gets a random seed word there, so its prompt says "apple" instead of the owner's mechanism or the measured trade-off. |
| S6 `test_selection_rows_are_written_once_per_round` | medium | `_select_with_lanes` runs before the interrogation and after each generation. Each call appends a full set of selection.jsonl rows and a `slots_by_origin` decision. report.json "selection" counts every row: the dry run reported 15 picks for 5 builds. Fix in the writer, or make `report.collect` keep the last call per round (modules). |
| S9 `test_off_tree_decision_matches_the_contexts_dealt` | low | The `off_tree` and `doubt_cards` decisions are logged before the cap. Dry run: "off_map 20, doubt dealt 6", one off-map context ran. |

## Execution half of loop.py

| Test | Severity | Bug |
|---|---|---|
| S4 `test_hedge_lane_fires_for_a_script_checker_gap_failure` | medium | `_hedge` only matches feedback rung 3 with a reason starting "at step" (nano/check.py, LLM checker). The script checker reports the score gap at rung 2 ("the quick score is ..."). On every generic profile `--hedge-share` is a silent no-op. Needs a checker-neutral signal (checks owner to agree). |
| S5 `test_revise_move_for_a_script_checker_learning_failure_is_fix` | medium | `_rounds` maps feedback rung 2 to "specialize" (a resource failure). In the script checker rung 2 is the learning gap, so learning failures are narrowed, not fixed. Same rung-meaning seam as S4. |
| S7a `test_resume_keeps_the_moved_off_tree_share` | medium | `load_state` does not read `off_tree_share` back from problem_tree.json. A resumed run returns to the CLI share. |
| S7b `test_resume_keeps_source_yield_and_discovery_history` | medium | `source_yield`, `seed_yield` and `discovery` live only in memory and are rewritten whole. After a resume the first write drops every earlier round (report.json "discovery" reads that file). `seed_info`, `seeds_by_part`, `retired_cards` and `promoted` are not restored either. |
| S8 `test_commitments_hash_is_stable_across_a_resume` | medium | `run()` calls `_write_commitments` on every start. The hashed record holds `ts`, so a resume gets a new hash and overwrites commitments.json and state.json. The registered record no longer shows what the run committed to first. |
| S11 `test_answer_n_checked_counts_checked_candidates_only` | low | `answer["n_checked"]` is `len(pool)`, and the pool includes hedged failures. report.json "checked" counts verify status only. |

## Modules (report, dashboard)

| Test | Severity | Bug |
|---|---|---|
| S10 `test_report_briefs_are_parts_not_analogy_files` | low | `report.collect` and `dashboard.snapshot` read every research/*.json as a brief, so each part also shows an empty `<part>_analogy` brief (dry run: 12 briefs for 6 parts). |

## Reported without a test

- seed_yield.json lags one round (ideation, low). `_assign_seeds` records the yield before the round's seeded
  sketches exist, and nothing records it after. The last round is never written; the dry run file is all empty
  although round 2 had 5 seeded sketches. source_yield.json has the same lag. No test: the fix decides where
  the record belongs.
- source_yield.json, seed_yield.json, next_questions.json and memory_log.jsonl have no code reader (owner logs).
- report.json `reference.metrics` is a copy taken before `_relabel_all`, so it shows `learn_z` null while
  verify.jsonl shows 0.0 for the same candidate (execution, low).
- `report.collect` finds a verified winner's cluster by name; names repeat across parts, so the novelty tag can
  come from another cluster (modules, low).
- `_doubt_ready` counts failure-question nodes as parts that need a brief ("6 of 7 parts" in round 2). No effect
  today, since round 2 is ready on any brief (ideation, low).
- Bench: with `HTSA_FIXED_B` set, `--budget-from` is ignored without a warning and plain never runs, against the
  `--arm` help "(plain always runs)" (bench, low; a documented mode, so not tested).
- The dry run mock has no reply for the "preread" card, so preread.json is never written in a dry run (test
  tooling, not product).

## Checked and clean

All changed signatures (exam, audit, launch, think, allocate, bench, arc_think, portfolio_arc, graph, score,
judge, stats) are called with the new arguments. ARC answer keys stay out of `think` and `solve`. Every flag in
nano/loop.py main() and harness/bench.py reaches a read. `tree.OFF_TREE_NODE["id"]` and `tree.OFF_TREE_ID` agree.

## Merge notes

Only new files: harness/tests/test_bug_seams.py and this report. The 13 tests fail until the owners fix the
bugs. S4 and S5 share one cause (rung numbers differ between checkers); one fix can close both.
