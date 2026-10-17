# Changelog, 2026-10-17

One line per merged branch, from `git log --oneline` on master, grouped by area. Ids in brackets are the
review backlog's findings (sections A to I) and the owner's new items (N1 to N10) each branch closed.

## Generic loop and the problem tree (morning)

- c0704c7: the loop runs on any problem with a profile; checkers; modes 1 to 3 (baseline, check only, no check); off-map cards; docs/GENERIC_SPEC.md.
- ae0cb7c: a re-plan carries promoted, owner and implemented nodes instead of dropping them (issue 6).
- b28978b: the planner fills `refines`; `resolve_scope` uses it first; `plan_tree` repairs the scope once before falling back.
- b6dc760: selection deals build slots in the same off-map share that ideation used.
- 5203cd9: design assumptions kept apart from what tested ideas assumed (`idea_assumptions`, issue 2).
- 33a67c8: the lens is a factor separate from the replicate (`parts` by default, `--lens-by-replicate` opt-in, recorded).
- 2328441: doubt cards are dealt only after the team has read; they get the literature; disputed facts are logged.
- 655c30c (fix 7): upward proposals have their own reply format, are parsed, reported, and one is kept under the test cap.
- 7e3b1db (fix 8): a real tree: sub-parts, wins under their part, failure questions, depth at most 4.

## Research and the five team gaps

- 8f02ccb: selection critique, research notes and verdict; no code change.
- 9f1861c: research on the five team gaps (dialogue, memory, generality, problem finding, evidence) and a synthesis.
- f0b7213: docs/TEAM_GAPS_SPEC.md, the contract for the five gap agents.
- 41033c6 (gap A): per-part persistent memory (`nano/memory.py`), curator, `--no-memory` control arm.
- 6ceeb8b (gap B): one anchored reply round between the critic and the idea's author, `--no-dialogue`.
- 9fea4a3 (gap C): the team picks its next question (`nano/pick.py`, failure questions with test, threshold, fails_if), `--no-pick-questions`.
- fa80db8 (gap D): fetch on demand (NEED lines in builder and reviser replies, one fetch per fact with a source, one re-prompt), `--no-fetch-on-demand`.
- 187ce37 (gap E): NoveltyBench IQM, paired bootstrap intervals, rejudge and agreement; pre-registered bin-packing arms with a dry mode.
- 26442c1: the memory test tolerates focus contexts from question picking.
- 73a00ee: the fix-pass spec (docs/FIX_PASS_SPEC.md); gap and fix tests pass together (74).

## Fix pass: ideation, research and knowledge

- 92d7fcf: whole-problem preread before the map, `--no-preread` control (N3); research, analogy and ledger memory for parts only (I4, I5); cache keyed on profile, lens, baseline version and frame (I9); fact-check verdicts kept append-only, unsupported claims load as disputed (F6); research prompts without a persona (E3, I7).
- 96aec70: the seeded card picks seed words by function and distance per part and logs yield per function; `--seeds random` keeps the old draw (N7).
- 2f59cf0: pre-mortem knowledge: the brief's published failures in the critic's pack, `--premortem-web` (three shaped questions, one research call), report.json `premortem` with the confirmed share (N8).
- d04da62: re-plan carry and unique ids, sub-parts follow renamed parents, failure questions kept at low priority (I1, I2, I3); outward sketches must name the removed assumption (I6); planner, repair and re-plan calls checked for budget (I10); planner ids (I11); split_select refills a shortfall (I12); disputed facts marked in prompts and shown to the re-plan (I14); contexts counted after refusals (I15); analogy addendum asks for near and far (E5); "wild and unconventional" dropped (E16); tests compare with c0704c7 (G8, G9).
- 9132a1d: mock sketches carry REMOVES on outward contexts.

## Fix pass: loop execution, verdict and integrity

- bf93479 (F): run id and ledger rows carry the arm; state.json with spend at every stage and build; Mode 2 and 3 resume; resume does not rerun controls or tuning; hash memory keyed on the baseline text; plain and climb arms spend to the budget with the same controls, tuning and rule order; retest updates pool/; builds in flight reserve their estimate; outcome lessons updated by batch_verify; malformed control.json keeps the last good one; utf-8 stdout; Mode 3 refuses a same-model judge (F1-F15).
- 4193eb2 (verdict): sigma fixed from the baseline runs alone as an upper bound; e-BH over every tested candidate; seed pairing by number; warm-up-free step timing; controls and mutants re-anchored to the v2 baseline (QK-norm control retired); compressed-KV cost card; hedge lane on at 12%; long-shot share 0.2 (H4, H5, H7, H8, H10, H11, H13, G1-G3, G10, N10, E6, E7).
- 2c813d9 (integrity, section H): two-process launcher (parent applies the wall cap and writes the audit, child runs the candidate), secrets stripped, Windows job object with one active process, raising stubs for os.system, subprocess, socket and ctypes, read allowlist, train-only data folder verified, train tokens counted by the launcher and compared with the report (2%), exam seal event; boundary check catches constructed val names and computed module access; reach audit classifies forward, optimizer, schedule and untestable changes; the exam reads val and seals it before loading candidate code and recounts non-embedding parameters.

## Fix pass: harness

- 0be14db (A): independent low_prior domain lint on rendered prompts; timeouts charged at the real cap and retried once; sandboxed judge and probe cwd; per-item checklist in verify; hashed test input; env toggles as recorded flags; article-safe BT letter parse; first-sentence rationale strip; visible prompt cut; mid-card lint blocking; lazy lab dirs; creativity lint fails.
- 5965d11 (B): primary null with a superiority gate and TOST; keep or drop; headroom filter and judge validation in score; crash rows; matched-cost reuse after the budget check; final plain failures in the cost median; split-keyed cost and recorded floors; independent v2 baseline; unscored NoveltyBench rows; lite_bt plain reuse; plan-rule best-of-N sizing; clustered pruning-regret intervals and one pool definition (B1-B15).
- 2144004: the budget needs at least one successful plain run; a superseded spawn test retired (B9 follow-up).
- 1bd0466 (C): 2/3 thresholds with tolerance; parsed-only probe denominator; per-item allocator RNG; pooled back-off, per-slot floor and respawn slot; dev-tune views via the stats CLI and a snapshot loader with a split check; judge calibration sample; vote respects clears; EVL-10 fail counts; parent_id in the ledger; run.lock; checklist required for all_items; judge run_dir (C1-C15).
- a2596f2 (D): dedup keeps a later same-grid program that passes the examples; one selection rule (`dedup.vote`); solve and think see only the key-stripped item; CPU-time limit per input grid with a 4x wall guard; `arc_exec.perturbation_detail` as detail only; option regex needs a label delimiter; covers_constraint edges and probe cluster ids; dangling parent ids fail the check; killpg on non-Windows; effort default as the plain arm (D1-D11).
- 7ce2a48: the vote tolerates a missing bar and augmentation; test fixtures aligned across branches.
- 45ab833 (G): hermetic tests: profile and mock restored per test, no real lab or GPU by default, resume and value-stop coverage (G4, G6, G7, G12-G15, G17).

## Still open (from the integrity agent)

- An OS-level network block needs administrator rights; today the launcher blocks network access in-process (raising stubs and audit hooks) only.
- A candidate could still hide its token count by rewriting the memmap class; the launcher's count is not proof against that.
- Two immutable `torch.from_file` paths are covered only by the static check, not at run time.

## Skipped on research grounds

- RAG memory: per-part memory is read whole, with no top-k retrieval. research_notes/team_gaps/02_persistent_expertise.md: blind or retrieved records get copied and replayed; a small curated file read whole is the recommendation.
- A second training seed for the 7% architecture result: not run in this pass (no GPU runs). research_notes/team_gaps/05_evidence.md asks first for an honest claim that says why a second seed was not run, next to a published seed spread.
- The "rewrite each seed to be bolder" step stays in the off-by-default `--staged-sketch` arm, which exists to test that staged method; the "wild and unconventional" wording of `--exclusion-list` was dropped (E16).
- Selection quotas unchanged: research_notes/selection_cost/00_VERDICT.md, "no code change now", until the score rank of winners and the rank correlation of 45-step, 240-step and long-run gains are measured on a real run.

## This branch (docs)

- docs/PROFILE.md (N1), the node schema in docs/PROBLEM_TREE.md and docs/MAPPER.md (N4), the e-value gate in ARCHITECTURE.md, citation fixes (E1, E2, E5, E7, E8, E10-E15, E17), stale-doc fixes (A10, D5, D7, G16, I8, I13, B13 wording), and this changelog.
