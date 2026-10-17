
## verify

2026-10-10
- verify.run() itself appends rows to runs/<id>/verify.jsonl and evidence.jsonl; the driver must not write them again. surprises.jsonl and VerifyResult.surprise are the driver's job (run() never sees conf, by design).
- verify.run() sets cand.pred (ARC) whenever a valid test grid is produced, also on fail. Train + test run in one subprocess (arc_exec.execute); arc_exec.demo_match/predict remain for arms/probe.
- VerifyResult.attempts = attempts actually used (ARC 1, BT 0); the k budget is in details["attempts_budget"].
- Hash mismatch (REP-03) returns status "unverified", verification_type "none", details["hash_mismatch"] = True.
- verify.build() accepts an encode.Problem (reads .item) or an item dict; it re-applies strip_key.
- arc_exec interpreter: HTSA_EXEC_PYTHON, else config.VENV_PYTHON, else D:\AGI-lab\.venv\Scripts\python.exe, else sys.executable. config.VENV_PYTHON derives from LAB_ROOT, so it does not exist when tests set HTSA_LAB_ROOT to a temp dir.
- Exec sandbox dirs are created under config.LAB_ROOT/tmp and removed after each run.
- feedback.record_for adds "total" and "truncated" to the specified fields.

## memory

2026-10-10
- stats.load_views(batch) returns {"batch", "strategy_stats": <strategy_stats.json>, "calibration": <calibration.json or None>}; strategy_stats.json carries "rows": [{cls, card, round_type, pass, fail, n, n_calls, mean_tokens, mean_verify_tokens, beta_a, beta_b}], the {"rows": [...]} shape think/allocate.stats_rows already accepts. n = pass + fail (verification rows); mean_tokens = mean total_tokens per card-call row (rows with status None).
- stats.rebuild(batch) uses split "train" only by default (section 6); data.py has no train split at P0, so P0 views are empty unless the caller passes splits=("train", "dev-tune").
- pruning_regret needs conf per first-round candidate for the late-winner rate. It reads "conf": {cand_id: c} from state.json decision rows when present, else ledger "agreement" of the run's verify rows (identity calibration at P0), which covers only verified candidates. Request to driver: add "conf": dict(st.conf) to each _decide row.
- pruning_regret reads pop ids from state.json "decisions"[*]["pop"] (also accepts a list, "cycles", "log", "rows"); default arm "scaffold"; probe candidates (card or origin "probe") are excluded from the pool.
- graph.check also verifies that every candidate sharing an exact pred with another non-probe candidate appears in a cluster row (matches dedup grid/option rules when pred is set; pred-less program keys are not checked). It reads flags.dedup from the state.json header.
- matches_default reads runs/<id>/defaults_match.json ({cand_id: bool} or [ids]) if a later module writes one; absent at P0.

## control

2026-10-10
- Name clash: harness/think.py (driver) and the package harness/think/ share a name; the package wins. think/__init__.py forwards think, main, cli, build_parser to harness/think.py loaded as harness._think_driver (load_driver()). `python -m harness.think` needs harness/think/__main__.py calling load_driver().main(); nobody owns that file yet (integrator).
- judge.judge() does not write judgments.jsonl; the driver writes it. Prompts go to log_dir.parent/prompts/<call_id>.txt (log_dir = runs/<id>/calls). Judge prompts include the key-stripped item data (BT question and choices, ARC train pairs and test input) besides problem.md, because a bare option letter cannot be judged without the choices.
- probe.run_probe writes run_dir/prompts/<call_id>.txt and run_dir/cands/probe.jsonl. One fixed template; only the seed word differs per call (replicate-seeded, from strategies/seeds/concepts.txt with a fallback list). ARC answers go through probe._predict -> arc_exec.predict. Unparsed replies count in n but join no cluster.
- calibrate(): identity at P0; with flags.p_raw_validated a placeholder 0.5*agreement + 0.5*p_raw until calibration.json exists.
- allocate: CardSpec is imported from run_card (fallback dataclass with the README fields while run_card.py is missing). initial() order is [seeded, memory_blind, directed...]; allocate.MEMORY_BLIND_INDEX = 1 marks the memory-blind spec because CardSpec has no tag field. spec_tuple(spec) gives (card, operator, seed, perm). fresh_tuples() accepts an optional cards= keyword. RNGs use cls in place of item_id (initial/fresh_tuples get no item_id), so seed words repeat across items of one family per replicate; passing item_id would need a signature change.
- allocate.reallocate at P0 returns the same specs, so round 2 repeats round-1 tuples (same seed, same perm). If fresh seeds per round are wanted, the driver can draw the non-revise specs from fresh_tuples(... cards=[...]) instead.
- est_verify(k, 0.0) returns 0 (script-only checks such as ARC demo_match); None means cold start.
- dedup.drop cluster rows carry extra fields key and dropped beside the README fields; cluster_id = "k" + hash(key), stable across rounds.

## bench

2026-10-10
- DATA: D:\AGI-lab\data\brainteaser\SP.jsonl is byte-identical to WP.jsonl (396 rows, all ids WP-*). The bt item file therefore holds word puzzles; data.py derives family from the id prefix (bt_wp here, bt_sp once a real SP file is in place) and warns. Replace the SP download before the headroom pilot.
- BRAINTEASER selection and splits are by puzzle group (id before "_": original, _SR, _CR together): 40 groups = 120 rows, 48/36/36. Items carry an extra "group" field (ARC: group = id); score.py uses it as the bootstrap cluster.
- Item file folder is read at call time as config.DATA_DIR / name-of(BENCHMARKS[b]["file"]), so tests can repoint config.DATA_DIR. load_items() builds the files from the raw downloads if missing.
- runs.jsonl rows from the bench arms add two fields to the README row: n_calls, budget_tokens.
- bench.py writes results/<batch>/budget.json {benchmark: {backend: {model, cot_median, m, B, n, source}}}; score.py reads B from it. think.cot_median() reads cost.jsonl of the same batch, so with --budget-from <other batch> the scaffold still computes its own B from this batch's plain rows (both are the same when the plain runs share items).
- bench passes strip_key(item) to think.think() and to every arm. Scaffold runs go first; best-of-N arms then get budget_tokens = the scaffold's realized spent_tokens for that item and replicate (else B). bench appends the scaffold runs.jsonl row only if think did not write it.
- Runs already listed in runs.jsonl are skipped (reuse). think._make_run_dir raises on an existing state.json, so a scaffold run that crashed midway needs think --force or a manual move before bench retries it; the failure lands in results/<batch>/errors.jsonl.
- Arms write ledger rows through ledger.append (under a lock; best-of-N calls run in threads); they fall back to appending config.LEDGER_PATH directly if harness.ledger cannot be imported.
- bestofn_verify and seeded_bestofn call arc_exec.demo_match / predict directly (no verify.run), which is the same check as verify's ARC demo_match at P0; BT verify falls back to the vote.
- Candidate rows of the arms: card "bestofn" (seed set for seeded_bestofn), perm = call index + 1 when shuffled, extra.order = presented order, extra.demo = {matched, total} on verify arms.
- Smoke run on real data with the mock backend (2 items per benchmark, all arms): the scaffold failed with "cannot import name 'run_card' from 'harness'" (cards module not present yet); every other arm ran end to end with the real arc_exec.
- Test isolation (found 2026-10-10): tests/conftest.py does not exist and tests/test_bench.py imports harness.config without setting HTSA_LAB_ROOT, so a full `pytest harness/tests` binds config to D:\AGI-lab; test_think then writes tc_* and e2e__* run folders into D:\AGI-lab\runs and the next run fails with FileExistsError. With HTSA_LAB_ROOT set to a fresh temp dir the suite passes (91 passed). Fix: add tests/conftest.py that sets HTSA_LAB_ROOT to a temp dir before any harness import (README "tests/" row); the stale folders in D:\AGI-lab\runs were left in place for the integrator to remove.

## cards

2026-10-10
- encode.Problem has one extra field beyond the README: meta: dict (default {}). It holds shuffled_perm (this replicate's permutation id), low_prior (noun-replaced parts used by the low_prior view), n_domain_nouns, low_prior_lint (domain-noun findings; [] when clean) and encode (call_ids, encode_tokens, cap, cap_hit, disagreement, resolved). Problem.views values are full markdown views: canonical, shuffled, low_prior.
- problem.md carries goal, facts, resources, checklist and solve bar but not the item data (judge and probe already add the stripped item data themselves). Generator prompts put the item data at the top of the facts block.
- encode also writes private/noun_map.json (domain noun -> X token) and encode.json. encode_tokens covers both checklist calls, the optional resolve call and the defaults call. The cap (encode_cap_mult x max_tokens.plain = 8000) only skips the optional resolve call; the two checklist calls and the defaults call always run. On cli_json, with about 3k overhead per call, the cap is reached after the first two calls, so resolve never runs there. The integrator should decide whether the cap should exclude CLI overhead.
- CardSpec.perm: a card whose view is shuffled (seeded) and that gets perm 0 uses problem.meta["shuffled_perm"] while flags.shuffle_facts is on. Any nonzero perm reorders the facts of whichever view is used, with random.Random(f"{item_id}:perm:{perm}"). Candidate.perm records the perm actually used. spec.variant (canonical | shuffled | low_prior) overrides the card's view.
- Seeds and operators: spec.seed and spec.operator are used when they are set and valid for the card. Otherwise run_card draws them from random.Random(f"{item_id}:scaffold:{replicate}:{purpose}"). run_card has no arm argument, so "scaffold" is fixed in that string.
- BT candidates get pred = option letter from the script parser, consistent with dedup.option_of. ARC candidates get program = text and pred = None for the driver or verifier to fill.
- The transform card emits two sets of candidates: the solver's (extra.step = "solver") and the revise step's (extra.step = "revise", parent_ids = the solver ids). Both keep the card's operator (drop | negate | vary | oppose) in Candidate.operator. The revise step is skipped when the solver produced nothing. Two-labeller agreement on deep constraints is not implemented, because it would add a fourth call.
- revise applies to ARC only and raises CardError without a parent. formal applies to ARC only. run_card raises CardError when a card does not apply or problem.item carries the key field, and LintError when template text matches a fail pattern. Persona-like wording inside inlined item or model text (for example a BT question that starts "You are a ...") is logged in prompts/lint.jsonl with in_input = true and does not block.
- Files written per card call: prompts/<call_id>.txt, prompts/lint.jsonl (findings only), routing.jsonl (call_id, template, role, routed input names; skipped steps), calls/<call_id>/in/<input>.txt, calls/<call_id>/out.jsonl and variants/transformed_<call_id>.md for the transformer. Candidates of one card run go to cands/<first call_id>.jsonl. The contract id is that first call id, and CardRun.call_ids also lists converter calls.
- Cards and templates live in harness/strategies (config.STRATEGIES_DIR), not memory/strategies. Template names follow <card>.<step>.txt, and check_card enforces that a template's placeholders equal its step inputs exactly. Encode, defaults, converter and format templates are also in strategies/templates and are linted by lint_templates().

## driver

2026-10-10
- Layout: harness/think/__init__.py (control) makes harness.think a package; think.py is loaded as harness._think_driver and `from harness.think import think, main` forwards to it. think.py sets its own __path__ only when loaded as harness.think, so it also works if that __init__.py is removed. `python -m harness.think` needs harness/think/__main__.py (integrator, not owned): `import sys; from . import load_driver; sys.exit(load_driver().main())`. Until then the /think skill runs `python -c "import sys; from harness.think import main; sys.exit(main())" <args>`.
- ARC pred: run_card leaves pred None, so think.py fills cand.pred via arc_exec.predict(program, P.item["test_input"]) right after collect and before dedup/agreement (0 tokens). Without this, dedup keys on program hashes and probe agreement is always 0 (no early stop, no surprises). cands/*.jsonl rows still carry pred None, so graph.check's ARC dedup completeness (expected_drops) is vacuous; run_card setting pred, or graph reading clusters.jsonl keys, would fix that.
- B: results/<batch>/budget.json[benchmark][backend].cot_median first (covers bench --budget-from), else median of cost.jsonl rows (benchmark, backend, tokens|total_tokens), else cold-start proxy PARAMS.max_tokens.plain x 1.5; B_source logged in the state.json header.
- think.py writes state.json, clusters.jsonl (sole writer), judgments.jsonl, surprises.jsonl, answer.json, results/<batch>/runs.jsonl; it does not write verify.jsonl (verify.run does). Decision rows carry "conf": dict(state.conf) (pruning_regret request).
- Ledger rows: one per run_card call (round_type first|revise|post_reset, tokens = CardRun.usage, call_id = last call id, cand_id None), one per verification (same round_type as the candidate's spawn, status, agreement, p_raw), plus encode/probe/judge spend rows (round_type encode|probe|judge). Sum of ledger tokens per run_id == answer.spent_tokens (tested).
- Verify spend: VerifyResult has no usage field; think charges details["usage"] if present (0 at P0). verify.build usage likewise via .usage or .data["usage"]. est_verify gets mean 0.0 for script-only types (demo_match, agreement) at cold start.
- Reallocated specs whose (card, operator, seed, perm) was already spawned are swapped for allocate.fresh_tuples(..., n=1, cards=[card]) so later rounds do not repeat tuples (control's suggestion).
- End selection: a failed candidate is never returned as "unverified"; it can only be the best_guess of an abstain.
- clears(P.bar, r) = status verified|checked and partial_score >= bar.get("min_partial_score", 0).
- allocate.initial can emit the same tuple twice in round 1 (memory-blind draw equals a directed card, e.g. formal:none::0 twice on ARC).

## integrator

2026-10-10
- Added harness/think/__main__.py (`import sys; from . import load_driver; sys.exit(load_driver().main())`), so `python -m harness.think ...` works; the /think skill now uses it.
- Added tests/conftest.py: sets HTSA_LAB_ROOT to a temp dir and HTSA_BACKEND=mock before any harness import, plus an autouse fixture that repoints every config lab path (LAB_ROOT, RUNS_DIR, MEMORY_DIR, VIEWS_DIR, LEDGER_PATH, DATA_DIR, RESULTS_DIR) at tmp_path/lab and asserts after each test that no path escaped tmp_path. Per-file fixtures that did the same still work on top of it.
- Added tests/test_e2e.py (synthetic items, temp lab root): think CLI main on ARC + BT, graph --check/--render, `python -m harness.think|graph|lint` as subprocesses, and bench main with plain + bestofn_verify + scaffold; asserts run folders, ledger rows (sum == spent_tokens), graph check ok, no key string in any prompts/*.txt, best-of-N budget_tokens == scaffold spend and spent <= budget.
- bench.py: `--arm` is now `action="append"` and each value may be comma-separated, so `--arm plain --arm bestofn_verify --arm scaffold` runs all three (before, repeated flags kept only the last one).
- config.py: VENV_PYTHON no longer derives from LAB_ROOT; it is HTSA_EXEC_PYTHON, else D:\AGI-lab\.venv\Scripts\python.exe if present, else sys.executable (verify's and bench's request). arc_exec's fallback chain is unchanged.
- think.py: graph.write now also runs in _finish (after answer.json), so a run that budget-stops before its first cycle still has graph.jsonl and graph.check passes on its probe candidates. Found when the synthetic e2e items made B smaller than encode + probe spend.
- Not changed, left for the owner: the test pollution already in D:\AGI-lab (ledger batches e2e and tc_*, 176 rows; runs/{e2e__*,tc_*}; results/{e2e,tc_*}) predates the conftest; the full suite now adds nothing there. Also D:\AGI-lab\runs\_smoke.

## review fixes (integrator)

2026-10-10
- Spend accounting: llm.call sums usage over attempts and keeps usage on error (CallError.usage), charges timeouts by estimate (usage_estimated), passes CLAUDE_CODE_MAX_OUTPUT_TOKENS to claude -p, runs the CLI without a shell in its own process group and kills the tree on timeout, parses the last JSON object, and charges max(usage, sum(modelUsage)). run_card returns a partial CardRun (contract["error"]) when a step fails after a call; think._collect charges it (ledger status "card_error", excluded from stats outcomes). Judge rounds are estimated (judge.est_cost) and skipped when they do not fit B.
- Ledger: one row per call with the logged usage (encode via Problem.meta["encode"]["call_ids"], probe via ProbeResult.calls, judge via Judgment.call_ids, cards via CardRun.call_ids); a remainder row named "<group>" keeps the per-run sum equal to spent_tokens. run_instance on every row; stats uses ledger.current_rows. stats mean_tokens is per card run (call rows grouped by spawn key).
- Privacy: the defaults role logs under runs/<id>/private/calls/ (config.PRIVATE_ROLES); problem.md has no item id; judge strips comments and docstrings from ARC programs.
- Measurement: think rewrites cands/*.jsonl with the preds it used (graph.check and score coverage see them); graph.expected_drops also takes clusters.jsonl "dropped" ids; run_card takes the run's flags (shuffle_facts) and encode.perm_order is replicate-seeded; allocate.initial never repeats a tuple; tournament and revise RNGs no longer key on uuids.
- Robustness: schemas.append_jsonl is locked and single-write, read_jsonl tolerant; think() catches crashes (error.json, abstain answer, runs row status error) and _make_run_dir moves crashed folders aside; bench retries errored runs, lints templates before and rendered prompts after a batch (lint.json), computes cot_median over successful plain calls only, refuses to set B without any, and skips best-of-N runs with no scaffold spend (errors.jsonl). best_of_n sizes batches by the largest call and goes one at a time near the budget; runs rows carry overshoot.
- arc_exec: -s -P -B -X utf8 (PYTHONHASHSEED honoured), Windows job object (tree kill), readers use os.read and keep partial output, nonce-marked single result line, os._exit in the runner. A candidate could still read the nonce from the runner's frame during transform(); OS-level sandboxing remains P1.
- Prompts of judge, probe and the plain arms are templates (judge.txt, probe.<b>.txt, plain.<b>.txt) rendered through run_card.render_prompt with lint and routing rows.
- Not verified on a real backend (no tokens spent in this pass): that claude -p honours CLAUDE_CODE_MAX_OUTPUT_TOKENS, the effect of --safe-mode/--strict-mcp-config on the init context, and the usage vs modelUsage totals. Check on one real call before a budgeted run.
