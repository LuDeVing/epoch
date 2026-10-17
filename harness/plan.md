# HTSA measurement plan (preregistration draft)

Status: DRAFT, 2026-10-10. Spec: `../ARCHITECTURE.md` v0.3, sections 3 (/bench), 8 and 9 step 1.
Fields marked TBD are fixed after the headroom pilot and before any arm other than plain runs on
the final item set. Once fixed, this file is frozen for the batch; changes need a dated changelog
entry below and apply to later batches only.

## 1. Cost

- Cost unit: `Usage.total_tokens` = input + cache_read + cache_creation + output tokens of every
  model call, read per call from the backend usage record (CLI JSON or Messages API).
- Counted: every generator, encode, defaults, judge, verifier, converter, probe and embedding call;
  CLI system-prompt overhead (about 3k tokens per call with tools off); cached input at full price;
  offline tokens amortized per item. Orchestrator-side scripts (dedup, arc_exec, scoring) cost 0.
- Per call: `runs/<run_id>/calls/<call_id>.json`. Per plain run: `results/<batch>/cost.jsonl`.
- Realized spend per item is reported beside the cap for every arm (summary.md, spend/B column).

## 2. Budget

- B = m x median plain-CoT tokens per item, per benchmark and per backend, measured on dev-tune
  with the plain arm (`results/<batch>/budget.json`: cot_median, m, B, n).
- m in {5, 10, 20, 40}; m = 20 primary. The m sweep runs for the scaffold and the primary null only.
- Best-of-N arms stop at the scaffold's realized spend on the same item and replicate (MSR-02);
  without a scaffold run they stop at B. Stop rule: the first call always runs; further calls are
  spawned while realized spend plus the mean call cost so far stays within the budget; hard cap
  N <= 4 x m.
- Driver estimators checked before each spawn and verification (section 5, implemented in
  `harness/think/allocate.py`): est_cost = the strategy_stats cell mean tokens per call of that
  card and round type, cold start = steps x (role max_tokens + routed-input estimate + CLI
  overhead); est_verify = k x the run's mean tokens per verify attempt (0 for ARC demo_match,
  a script-only check), cold start = k x (verify max_tokens + input estimate + CLI overhead).

## 3. Items

| Benchmark | Source | Selection | Items | dev-tune | dev-ablate | test |
|---|---|---|---|---|---|---|
| arc | ARC-AGI-1 public evaluation | <= 600 cells in all grids, exactly 1 test pair; sorted by file name, shuffled with seed 7, first 40 | 40 | 16 | 12 | 12 |
| bt | BRAINTEASER raw file `brainteaser/SP.jsonl` | 40 puzzle groups (original + SR + CR) sampled with seed 7 | 120 | 48 | 36 | 36 |

- Splits are assigned by fixed seed (7) over units: ARC task, BRAINTEASER group, so reconstruction
  variants never cross splits. Bootstrap clusters for BRAINTEASER are the groups.
- Data issue (open): the raw `SP.jsonl` is byte-identical to `WP.jsonl` and holds word puzzles
  only (ids WP-*); the current bt items carry family `bt_wp`. Replace the SP download before the
  pilot or record that the gate uses word puzzles.
- Chance level: ARC 0% (exact grid), BRAINTEASER 25% (4-way).
- Final item set: TBD after the headroom pilot (n_arc = TBD, n_bt = TBD; dev subset target about
  150 items stratified by difficulty).

## 4. Headroom pilot (section 3 /bench step 2)

- Plain arm on dev-tune and dev-ablate, 3 replicates, primary backend and model.
- Keep items with plain accuracy between 20% and 80% across replicates; substitute BRAINTEASER
  reconstruction variants or fresh paraphrases and ARC-AGI-2 public eval items where the pilot
  shows ceiling or floor. Report chance level and the plain noise floor (replicate SD).
- Power calculation: TBD from the pilot (paired design, item-cluster bootstrap; target
  detectable difference TBD points at 80% power, one-sided alpha 0.05).

## 5. Arms (matched cost)

| Arm | Definition | Selection |
|---|---|---|
| plain | one call, step-by-step prompt, fixed final format (ARC: one `transform(grid)` code block run by arc_exec; BT: `ANSWER: <letter>`) | the parsed answer |
| bestofn_vote | N independent plain calls | majority pred, ties to the first seen |
| bestofn_verify | N independent plain calls, same verifier | ARC: first program passing all train pairs (demo_match), else majority; BT: majority |
| seeded_bestofn | plain calls each with a seed word (strategies/seeds/concepts.txt) and a shuffled fact order (ARC train order, BT option order mapped back) | as bestofn_verify |
| scaffold | harness.think.think with the gate flags (section 4) | the driver's answer |
| instruction-only, ladder L1, pressure wrapper | Stage 2 arms (section 8) | TBD, built in section 9 step 2-4 |

- Primary null: the stronger of bestofn_verify and seeded_bestofn, chosen per benchmark on
  dev-tune before the comparison batch.
- Every prompt is built from `strip_key(item)`; keys are read only by `harness/score.py`.

## 6. Replicates and seeds

- Replicate r seeds every random choice through
  `random.Random(f"{item_id}:{arm}:{r}:{purpose}")` (seed words, permutations, probe).
  Model nondeterminism is noise.
- 3 replicates on dev, 5-10 on test (TBD after the pilot). Replicates are averaged within item.

## 7. Metrics

- Primary: ground-truth solve rate on keyed benchmarks; paired difference vs the stronger null;
  95% cluster-bootstrap CI over items (2000 resamples), replicates averaged within item.
  Abstentions count as wrong; forced-choice solve rate (best guess) reported beside it.
- Secondary (summary.md): coverage (oracle pass@pool) vs selection accuracy for pool arms;
  pass@R from replicates; realized tokens per item beside B; abstention rate.
- Further section 8 metrics (calibration, transition matrix, diversity, integrity counts, graph
  completeness, pruning regret) are produced by their owning modules.

## 8. Decision rules

- Gate (Stage 3 go/no-go, test split, used once): scaffold vs the primary null at m = 20,
  one-sided superiority, lower 95% CI bound > 0 points. Equivalence claims require TOST within
  3 points (placeholder margin).
- Keep/drop (pre-gate, dev-ablate, 1x cost, R_max fixed, 3 replicates): a card or flag stays only
  if leave-one-out gives P(helps) > 0.95 under a Beta(1,1) prior on discordant item pairs, helps =
  ground-truth solve rate per item at matched cost vs the full stack minus the flag; accumulated
  only across batches sharing one memory and calibration snapshot; number of batches fixed in
  advance (TBD); pairs stay only if they beat each component (MSR-12, MSR-18).
- Fidelity to the brain is never a reason.

## 9. Ablation schedule (P0 rows of ARCHITECTURE section 8; post-gate and P1 rows live there)

| Mechanism | Ablation or arm | Slot |
|---|---|---|
| low_prior card (REP-02) | portfolio minus low_prior at equal tokens | pre-gate (card) |
| transform card (GEN-12) | portfolio minus transform | pre-gate (card) |
| formal card (REP-03) | formal plus prose vs prose only, formalizable subset | pre-gate (card) |
| revise card (GEN-14) | scaffold minus revise | pre-gate (card) |
| seeded card (GEN-17) | never ablated; seeded best-of-N is its contrast | Stage 2 arm |
| Stagnation reset (CTL-11) | fresh reset without failures vs no reset | pre-gate flag 1 |
| Stop rule (CTL-05) | stop rule vs no early stop | pre-gate flag 2 |
| Dedup (CTL-10) | dedup off; threshold sweep | pre-gate flag 3 |
| Fact shuffle (REP-08) | shuffled vs canonical order | pre-gate flag 4 |
| Pressure lint (STA-02) | neutral vs high-pressure wrapper | Stage 2 arm, first dev batch |
| Best-of-N nulls, instruction-only, ladder L1 | arms | Stage 2 arms |
| Budget and round cap (CTL-03, CTL-04) | m sweep; R_max sweep at the largest m | sweep (Stage 3) |
| Candidates per generator (GEN-06) | 4/8/16 at fixed tokens | sweep |
| Graph, pruning regret, lint, ledger rules | diagnostics and integrity metrics | exempt |

## 10. Result and cost schemas

- `results/<batch>/runs.jsonl`: {batch, benchmark, item_id, arm, replicate, run_id, status,
  answer, spent_tokens, rounds, ts} (+ n_calls, budget_tokens from the bench arms).
- `results/<batch>/cost.jsonl`: {benchmark, backend, model, item_id, replicate, tokens}.
- `results/<batch>/budget.json`: {benchmark: {backend: {model, cot_median, m, B, n, source}}}.
- `results/<batch>/summary.json`, `summary.md`: written by `harness/score.py`.

## 11. Run count and token budget

- Runs: TBD after the pilot (items x replicates x arms x m values).
- Tokens: TBD (B x runs per arm, plus plain measurement and probes), with a hard ceiling TBD.

## Changelog

- 2026-10-10: first draft (bench owner).
