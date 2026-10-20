# 00. Artifact map: what the research loop writes, when, and who reads it

Task U1. Read-only. Checked on 2026-10-17.

## How this was done

I read `nano/loop.py` and the modules it calls: `tree`, `ideate`, `deepen`, `memory`, `pick`, `research`, `report`,
`dashboard`, `checks/*`, plus the small modules that write shared files (`lessons`, `harness/ledger`, `harness/graph`,
`harness/llm`). I opened every file in one real mock run folder. I ran one small CPU-only script that prints key names
and types. I started no model call, no GPU run and no loop.

Code version: commit `74abcaf` on `master`, clean tree. Line numbers such as `L1932` are for `nano/loop.py` unless
another file is named. They will drift after later commits.

Tags. [code] means I read it in the code. [mock] means I saw it in the mock run folder. [doc] means a repo doc says it
and I did not check it in code. Web facts: none used. Nothing here comes from the web.

## The run used

`D:\AGI-lab\runs\mock-after-bugpass__nano__binpack_nobase__scaffold__r0`. It is the only folder whose name starts with
`mock-after-bugpass`, so it is also the newest.

| Item | Value [mock] |
|---|---|
| Profile | `binpack_nobase`, Mode 2 (`check_only`). There is no baseline. The best checked candidate so far is the "reference". |
| Backend and model | `mock`. Logical model name `fable`. |
| Arm, replicate, rounds | `scaffold`, 0, 2 |
| Budget | 3,000,000 tokens for the inventing model. 30,000,000 for the cheap model. |
| Time | 19:33:18 to 19:34:35 on 2026-10-17 (UTC+4), 77 s. Most of it was scorer runs in verification. |
| Size | 1,778 files, 11 MB. 823 model-call records (`calls/` 3.4 MB, `prompts/` 5.7 MB). |
| Content | 739 sketches, 135 clusters, 108 interrogation nodes, 180 dialogue rows, 9 builds (6 checked), 16 verify rows, 81 decisions. |

Mode 1 (profile `llm`, a baseline exists) adds files this run does not have. Mode 3 (profile `review_process`, a panel
of judges) adds others. Section 4 marks every entry as seen in the mock run or only in code.

## 1. Short answer

1. **State lives in memory.** The loop keeps the tree, sketches, clusters, interrogation nodes and results in Python
   objects. The files are outputs. It does not re-read those objects from disk, except on `--resume`. What it reads
   live is `control.json`, a few shared lab files and a few bookkeeping files of its own (section 9.4). If someone
   edits `problem_tree.json` by hand, the next `_write_tree` overwrites it. [code]
2. **33 entries in the mock run, 9 more in code only.** Most are rewritten whole with a plain `write_text`. Only
   `state.json`, `graph.jsonl` and `memory/experiments/verified_by_hash.json` are replaced atomically. [code]
3. **Five `_stage` calls per round:** `ideated`, `clustered`, `deepened`, `built`, `verified` (L3273, L3292, L3344,
   L3374, L3422). There is no `_stage` for the plan step and none at finish. [code]
4. **`control.json` is the only live human input.** It sits in the run folder. It is read in three places: `_stage`
   (L1938), `_pick_question` (L850) and `_opinions_for` (L3027). No code writes it. People edit it by hand. [code]
5. **Key names differ from the brief.** `owner_seeds` is not a `control.json` key. It is the file
   `memory/owner_seeds.json`, read once at start (L4445). `stop` is `stop_after_stage`. `budget` is `budget_add` and
   `aux_budget_add`. [code]
6. **The one "tell every agent" channel is narrow.** `note` (600 characters) reaches idea agents only from round 2 and
   only after a first result exists. It also reaches interrogation and the re-plan. It never reaches builders. [code]
7. **Ids.** Sketch, candidate, call and interrogation ids are random and unique. Node ids come from the planner or a
   person and can clash. Cluster ids such as `choice-in-k03` are positional and can shift when clusters are rebuilt.
   Track a cluster by its member sketch ids. [code]
8. **The current dashboard** shows state, live calls, candidates, tree counts, the idea map, interrogation Q and A and
   the pool. It does not show objections, author replies, selection reasons, questions, memory, the reference or
   control. It re-reads everything every 2 s. [code]
9. **Sharing.** Two loops with different run folders already share `memory/` and the ledger. One run folder needs one
   writer: the nano loop has no run lock. Per-part memory files have only a thread lock. [code]
10. **The hook.** `_stage` runs on the main thread while worker threads are idle. It writes `state.json` first, then
    merges `control.json` into live state. A shared space can push before that merge and pull inside it. It needs the
    additions in section 11. [code]

## 2. Where things live

| Place | Path | What | Shared by two loop processes? |
|---|---|---|---|
| Code | `C:\Users\User\Desktop\AGI\nano`, `...\harness` | the loop and its modules | yes, read only |
| Lab root | `D:\AGI-lab`. Set by env `HTSA_LAB_ROOT` (`harness/config.py` L17) | parent of `runs/`, `memory/`, `data/`, `results/` | yes, if both processes use the same value |
| Run folder | `D:\AGI-lab\runs\<run_id>\` with `run_id = <batch>__nano__<spec_id>__<arm>__r<replicate>` (L322) | everything one loop process writes | only if the four parts match, and then it is unsafe (section 10) |
| Baseline cache (Mode 1) | `runs\<profile>_baseline_profile` and `..._mock` | baseline measurements | yes, any run of that profile |
| Memory folder | `D:\AGI-lab\memory\` (`config.MEMORY_DIR`) | shared stores, section 7 | yes |
| Per-part memory | `memory\<profile>\<part>.md`. With the mock backend: `memory\_mock\<profile>\` (L1712-1722) | what the team knows about each part | yes, same profile and same part ids |

## 3. The stage clock

`NanoLoop.run` (L3203) builds the header, then `_rounds` (L3230) loops over rounds. The stage labels below are the ones
used in the tables. Only the rows with a boundary call can read `control.json`.

| Stage label | What runs | Boundary call | Reads `control.json` |
|---|---|---|---|
| start | `run` L3203: state header, `_write_commitments`, `_load_profile`, `encode` | none | no |
| plan (round 1 only) | inside `ideate_round` L1092-1099: `plan_tree` (reading call + planner call), `research_round` | none | no |
| ideated | rest of `ideate_round`: question pick (round 2 up), deal contexts, idea agents in parallel (6 threads), append sketches, write tree | `_stage(rnd, "ideated")` L3273 | yes |
| clustered | `cluster_sketches` (blind clustering, cross-part merge, prior-art tags), `_discovery`, `_select_with_lanes`, write clusters and tree | L3292 | yes |
| deepened | `deepen_round` per generation (interrogation, pre-mortem, author reply), re-cluster, re-select, novelty filter | L3344 | yes |
| built | revise queue, builders in parallel (6 threads), dedup | L3374 | yes |
| verify span | Mode 1 round 1: controls and tuning. Then serial `verify` per candidate, same-round fixes, composites, failure questions, hedge lane, families, tree write, memory curation, cycle decision, state write, graph write | none inside | no |
| round end | the end of the verify span | `_stage(rnd, "verified")` L3422 (sets `completed_rounds`) | yes |
| finish | `_finish` L4010: final yields, long runs, answer, reports, lessons | none | no |

In the mock run, the ideate, cluster and deepen work of round 2 took about one second (mock agents answer at once).
Verification took 20 to 40 s per round. With real agents the agent stages become the slow ones. [mock]

The control arms `plain` and `climb` (`run_control` L3915) never call `_stage`, so they ignore `control.json`. [code]

## 4. Inventory of the run folder

Short names for readers. **resume** = `load_state` (L2017), used by `--resume`. **dash** = `nano/dashboard.py`.
**report** = `nano/report.py` `collect`. **graph** = `harness/graph.py`. **people** = humans opening the file.
"Mock" says whether the file or folder exists in the mock run [mock]. "No" means it only exists on some code paths [code].

Write modes. **append** = one line added, nothing rewritten. **whole** = the full file is written again with a plain
`write_text` (not atomic: a reader can see a cut file). **atomic whole** = written to a temp file, then replaced.

Who writes. `loop.py` writes almost every file. The exceptions: `research.py` (`facts_fetched.jsonl`, the shared
research cache), `memory.py` (per-part memory), `report.py` (`report.json`, `REPORT.md`), `checks/script.py` with
`launch.py` and the scorer (the `verify/` and `reference/` folders), `harness/llm.py` (`calls/`), `harness/graph.py`
(`graph.jsonl`), `harness/ledger.py` (`memory/ledger.jsonl`), `lessons.py` (`memory/lessons.jsonl`). `tree.py`, `ideate.py`,
`deepen.py`, `pick.py` and `dashboard.py` write nothing: the loop writes what they compute. [code]

### 4a. Header and inputs

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `state.json` | start L3209; every `_stage` L1937; after every build L2744; `_write_commitments` L2416; round end L3416; finish L4072 and L4103 | atomic whole (`state.json.tmp`, L4199-4203). Read-modify-write under `_state_lock` | resume, dash, report, graph (header flags) | yes, 13.6 KB |
| `commitments.json` | start, `_write_commitments` L2376-2411 | once. On resume kept, or rewritten if the settings changed | report, the resume check | yes |
| `constraints.json` | start, `encode` L2582 | once | nothing in `nano/` (`harness/encode.py` has its own for ARC) | yes |
| `problem.md` | start, `encode` L2566 | once | every prompt (`_common` L2608), `research_round` L497, `plan_tree` L666, people | yes |
| `private/defaults.json` | start, `encode` L2594 | once | resume L2057, to tag clusters "obvious". Never routed to a generator | yes |
| `control.json` | by people, any time | by hand. No code writes it | `_stage`, `_pick_question`, `_opinions_for` (section 6) | no |
| `control_log.jsonl` | `_stage` L1953 (unreadable file) and L1959 (control changed) | append | report (counts the rows) | no |

### 4b. The map

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `problem_tree.json` | plan L708; ideated L1316; clustered L3291; deepened L3337 (each generation); any boundary when a person adds a node L2015; verify span end L3411; re-plan L3746 | whole. Current snapshot only. No per-round history | resume (`nodes`, `off_tree_share`; drops `stats`, L2038-2041), dash (`nodes`), `nano/experiments/binpack_arms.py`, people | yes, 14.9 KB, 9 nodes |
| `preread.json` | plan L644, only if the reading call returned text | once | nothing (audit) | no (source was `none`) |
| `research/<node>.json` | plan: `research_round` L536 (round 1). `inject_ledger` L585 rewrites it when ledger rows exist | whole | resume L2051, dash, report; in memory for prompts | yes, 6 files |
| `research/<node>_analogy.json` | plan: L542 | once | resume, prompts | yes, 6 files |
| `proposals_upward.jsonl` | ideated L1311 | append | resume L2075, dash, report | yes, 8 rows |
| `disputed_facts.jsonl` | ideated L1082 (doubt cards on the off-map node) | append | `_disputed_rows` L1037, then `_apply_disputes` L1050 puts them on the node as `disputed` from round 2. Re-plan prompt L3708 | no (needs `DOUBT:` lines in a reply) |

### 4c. Ideas

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `ideas.jsonl` | ideated L1314 (one batch per round); deepened L1679 (offshoot sketches, one write per interrogation node) | append | resume L2059, dash, report | yes, 739 rows, 460 KB |
| `idea_clusters.json` | clustered L3289; deepened L3335 (each generation) and L3342 (final: adds `selected`, `novelty_gate`) | whole. Latest snapshot over the sketches of all rounds. `round` is the latest round | resume L2064 (rebuilds the cluster and tag caches), dash, report, `nano/calibrate.py` | yes, 84 KB, 135 clusters |
| `selection.jsonl` | clustered: `_log_selection` L2446, one row per cluster. A re-selection after an interrogation generation first removes the rows of that round by rewriting the file (`_drop_selection_rows` L1427), then appends again | append, plus a partial rewrite | `_drop_selection_rows`, report (counts by reason) | yes, 254 rows |
| `discovery.json` | clustered: `_discovery` L1347 | whole `{rounds: [...]}` | resume L2043, `answer.json`, report | yes |
| `source_yield.json` | ideated, start of round 2 up: `_shift_off_share` L769. Finish: `_close_yields` L1455 adds a `final: true` row | whole | resume, `answer.json` | yes |
| `seed_yield.json` | ideated: `_assign_seeds` L1764. Finish: `_close_yields` L1460 | whole | resume | yes |

### 4d. Arguments and facts

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `deepen.json` | deepened: L1682 after every interrogation node; L2374 after a web fact check | whole, every time. It grows (428 KB) | resume L2080, dash, report | yes, 108 nodes |
| `dialogue.jsonl` | deepened: `_dialogue` L3625 (author reply and critic mark) | append | `_report_dialogue` L3643 only | yes, 180 rows |
| `facts_fetched.jsonl` | built: a builder wrote `NEED:`, `research.fetch_fact` (research.py L652-682). Also a per-run cache by normalised question | append, "not found" included | `research.fetch_fact` (skips a repeat question) | yes, 1 row |

### 4e. Builds and tests

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `cands/<call_id>.jsonl` | built L2813. Also `control_<id>` L3502, `tune_<id>` L3453, `compose_<id>` L3904 | once per builder call, one row (a parse failure also writes a row) | resume L2093 on, dash, report, lessons, calibrate, graph | yes, 9 files |
| `cands/src/<cand_id>.py` | built L2808 (and tune, control, compose) | once | the checker scores this file; resume; people | yes, 9 files |
| `verify.jsonl` | verify span L2939 (each candidate); relabel L3106; retest L3142; finish L3181 (long run, rung 4) | append. Several rows per id. The last row wins for every reader | resume L2086, `_memory_artefacts` L1844, dash, report, lessons, calibrate, graph, binpack_arms | yes, 16 rows |
| `verify/<cand_id>/<level>/metrics.json` and `audit.json` | verify span: checker `_score` (`nano/checks/script.py` L123). Levels `build`, `quick`, `full`, sometimes `quick2`. Mode 3 adds `panel.json` | once per scorer run. `metrics.json` becomes `metrics.rejected.json` after an unclean run | checker `long_run` (reuses `full/metrics.json`), people | yes, 9 folders |
| `pool/<cand_id>.py` and `.json` (`.md` in Mode 3) | verify span L2944-2947 when `checked`; hedge lane L3526. Rewritten by relabel L3100, retest L3130, long run L3174. Deleted for tune-pruned (L3469) and failed retests (L3137) | whole | dash, report, `batch_verify`, people | yes, 7 pairs |
| `reference.json` | verify span, Mode 2 and 3: `_set_reference` L3076, each time the reference moves | whole | resume L2029. Copies sit in `answer.json` and `report.json` | yes |
| `reference/<cand_id>/...` | same moment: `measure_reference` runs the scorer on the new reference (`base_build`, `base_quick_s<seed>`, `base_full_s<seed>`) and writes `baseline_profile.json` | cached by a key (script.py L218) | checker cache | yes |
| `graph.jsonl` | round end L3419 (`harness.graph.write`) | atomic whole. Rows of kind `node`, `edge`, `cluster` | `harness.graph` check and render; dash links `graph.html` if it exists | yes, 13 rows |
| `clusters.jsonl` | built: `dedup` L3200, only when two builds have the same source hash | append | report, dash, graph | no |
| `controls.json`, `tuning.json` | verify span, round 1, Mode 1 only (L3375-3378, L3512, L3472) | whole, once | `_finish` L4037, report, resume L2133 (tuning prunes) | no |
| `anomalies.json`, `private/anomaly_sham.json` | start, Mode 1 with the LLM profile only (L2205-2207) | once | report | no |

### 4f. Team questions and memory

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `next_questions.json` | ideated, round 2 up: `_pick_question` L860 | whole. Only the latest pick | nothing in code. It is for people | yes |
| `questions.json` | ideated L861 (each pick); finish L889 (`_report_questions` sets `answered`) | whole `{picks: [...]}` | resume L2073, `_report_questions` | yes |
| `memory_log.jsonl` | round end: `_curate_memory` L1912, one row per curated part | append | nothing in code | yes, 4 rows |
| `D:\AGI-lab\memory\[_mock\]<profile>\<part>.md` | round end: `_curate_memory` L1871, then `Memory.curate` and `Memory.archive` | read-modify-write of the whole file. Non-atomic. The lock is per process | `Memory.block` in every idea context that has memory (L1208), `_pick_memory_free` L1792, the curator L1902 | yes, 5 files, shared with older mock runs |

### 4g. Live view and final reports

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `live.json` | any time: `_live` L2150 runs on every phase change and before and after every model call (L2265, L2274). Final "done" L4104 | whole, non-atomic. Retries on `PermissionError` | dash only | yes |
| `answer.json` | finish L4071 | once | dash, report (`wall_s`, upward), binpack_arms, people | yes, 12 KB |
| `report.json` | finish: `report.write` L4084 first. Then each section re-reads and rewrites it: `_report_modes` L4172, `_report_dialogue` L3651, `_report_premortem` L3591, fetched facts L4080, `_report_memory` L1930, `_report_questions` L905 | whole, read-modify-write. `report.write` keeps keys it did not compute (report.py L403-405). `batch_verify` rewrites it later | people, batch_verify | yes, 18 KB, 60 keys |
| `REPORT.md` | finish: `report.write` overwrites (report.py L407). `_report_modes` prepends (L4175). `_report_questions` appends (L920) | whole | people | yes, 10 KB |

### 4h. Audit trail

| File | Written at (stage, code) | Mode | Read by | Mock |
|---|---|---|---|---|
| `calls/<call_id>.json` | every model call: `harness/llm.py` L441 | once | dash (re-reads all of them at every poll), report (tokens, cost), `_build_tokens` L813 | yes, 823 files |
| `prompts/<call_id>.txt` | every model call: `_call` L2260 (research calls L509) | once | people; `binpack_arms` checks that no prompt names the language-model problem | yes, 823 files |

Reading note. Mode 3 (`no_check`, the panel) also writes `pool/<id>.md` (the proposal text), `verify/<id>/panel.json`
and puts `proposals` in `answer.json` and `report.json`. Mode 2 and 3 write `reference.json`. Only Mode 1 writes
`controls.json`, `tuning.json`, `anomalies.json`, diagnostics and the baseline cache. [code]

## 5. Schemas

Key lists come from the writing code [code] and were checked against the mock run [mock].

### 5.1 state.json (19 keys)

| Key | Meaning |
|---|---|
| `run_id`, `item_id`, `benchmark`, `arm`, `backend`, `model` | run identity. `item_id` is the profile spec id. `benchmark` is `nano`. |
| `B`, `aux_budget`, `rounds`, `lens`, `lens_design`, `baseline_version` | settings, written once at start. A `budget_add` or `rounds_max` in control.json changes memory only and shows up in `decisions`, not here. |
| `decisions` | list of events. Each has `step` and usually `round` and `ts`. See 5.2. |
| `spent`, `spent_aux` | tokens used so far: inventing model, cheap model |
| `spent_by_stage` | tokens per budget stage (mock: research, ideation, interrogation, build, other) |
| `completed_rounds` | set at the `verified` boundary. A resume starts at the next round. |
| `commitments_hash` | 12-hex hash of `commitments.json` |
| `stage` | `{round, step, ts}` of the last `_stage` call. Only the latest is kept. A resume reads `step == "built"` to skip the builds of that round (L3294-3299). |

### 5.2 decisions: the loop event log

Three cautions. The list is rewritten whole at every state write. `_drop_selection_rows` can delete entries (L1429), so
list positions are not stable. Not every entry has `ts` or `round`. Use `ts` plus content, not an index, as a cursor.

| `step` | When | Keys besides `step` |
|---|---|---|
| `baseline`, `preread`, `seeds` | start, plan, ideated | mode and note; source and counts; part, tag, picked `[[word, function, band]]` |
| `off_tree`, `doubt_cards`, `contexts_ran`, `memory_free`, `slots_by_origin`, `retire_cards` | ideated, clustered | counts for the round (dealt, ran, short, on_map, off_map, tree, off) |
| `pick_question` | ideated, round 2 up | chosen, kind, score, top3, vetoed, by, explore, path, requires_human |
| `off_tree_share` | ideated, round 2 up | from, to, by |
| `human_node` | any boundary | round, node, name |
| `promote_off_win`, `fail_question`, `tree_depth`, `replan`, `replan_carry` | map changes | node, parent, name, kept, merged, dropped |
| `merge`, `novelty_skip` | clustered | groups; cluster, nearest |
| `deepen`, `dialogue`, `fact_check`, `need` | deepened, built | round, gen, chains, nodes, offshoots; idea, exchanges, stop; counts |
| `reference`, `relabel`, `retest`, `hedge`, `families`, `fidelity` | verify span | action, from, to, reason, gap; candidates |
| `memory`, `cycle` | round end | part, added, rejected, archived; spawned, n_raw, n_kept, checked, failed, spent |
| `control`, `resume`, `stopped`, `budget` | any | set and value, or warning; completed_rounds; after; refused and why |

The mock run has 22 of these steps (81 entries). [mock]

### 5.3 problem_tree.json

Top-level keys: 

| Key | Meaning |
|---|---|
| `nodes` | list of node rows (below). One row per node, parent before children is not guaranteed. |
| `tree` | nested view `{id, name, kind, children[]}` from the root. `kind` is `root`, `part`, `question` or `win`. Use it for layout, then join `nodes` by `id` for details. |
| `inward_share` | share of build slots for inward ideas (0.6) |
| `off_tree_share` | share of idea contexts that work off the map. It moves between 0.2 and 0.6 with yield |
| `origins` | `tree` and `off`: contexts, sketches, clusters, built, checked, wins, clusters_per_context, wins_per_context, slot_share, context_share |
| `lens`, `lens_design` | how the planner drew the map |
| `stats` | `{n_idea_assumptions}` |

Node row keys:

| Key | Meaning |
|---|---|
| `id` | unique id. Planner ids are cut to 16 characters. `win_<cand8>` and `q_<cand8>` come from candidate ids. A person id is lower-cased and cleaned to `a-z0-9_`, 16 characters (L2000) |
| `name`, `parent` | name (60 characters). Parent id: `root` for parts, `null` for the root |
| `kind` | absent means part. Or `question` or `win` |
| `origin` | absent means planned. Or `human` (control.json), `failure` (a question from a failed check), `offtree` (an off-map win turned into a branch) |
| `frame`, `assumptions`, `boundary` | how the part works today (400 characters); design choices (5 at most, never grow in a run); the code region a change may touch |
| `idea_assumptions` | `[{from, text, round, kind}]`, kind is `silent` or `could_not_build`. What tested ideas assumed |
| `directions` | `["inward","outward"]` for parts, `["upward"]` for the root, `["inward"]` for questions |
| `refines` | the default part this node refines, or `new` |
| `priority` | `low` when a re-plan kept a node it no longer drew |
| `disputed` | `[{round, text, sketch_id, status}]`. Facts of the map that a doubt card disputed. Idea agents see them marked "disputed, re-measure before relying on it" (3 at most). Absent in the mock run |
| `from`, `test`, `threshold`, `fails_if`, `enterable` | questions only: failed candidate ids; `{metric, rung, op, what}` that would answer it; the number; the failure condition; false when no test can be derived |
| `stats` | per direction `{sketches, clusters, implemented, checked}`, plus `n_idea_assumptions` |
| `proposals` | root only. Upward proposals `{id, proposal, reframing, new_measure, why, cost, round, call_id}`. They are never built: a new success measure is a human decision |
| `depth`, `path` | depth below the root (0 root, 1 part, 2 sub-part, 3 question, 4 helper, max 4). Names from the top part down |

### 5.4 ideas.jsonl: one sketch per line (28 or 29 keys)

| Key | Meaning |
|---|---|
| `id` | `s` plus 10 hex characters. Unique. Safe as a key across processes |
| `idea`, `mechanism`, `prediction`, `test` | the sketch: name (120 characters), what changes and why (600), the observable effect, the cheapest check that could kill it |
| `source` | `own`, or the URL it builds on |
| `target`, `scope`, `metric_blind` | the measured quantity it should move; what the benefit is about; true when that is not the exam metric |
| `kind` | `leap`, `port`, `tune` or empty. Leaps also carry `breaks`, `keeps`, `p_success` (0.2 at most), `kill`, and `leap_op` (which rule-break operator) |
| `removes` | outward sketches only: the assumption removed. An outward sketch without it is dropped |
| `mapping`, `adaptation`, `part`, `slot` | analogy, adapt and port cards: typed mapping, the move applied, the part named, a short move label |
| `card` | which context made it: seeded, low_prior, formal, docs, research, analogy, diagnosis, adapt, owner, contradiction, blank, gaps, doubt, focus, deepen |
| `operator` | the direction: inward or outward |
| `seed` | the seed word, or the owner or contradiction text |
| `call_id`, `family` | the model call and the model that made it |
| `node`, `direction`, `origin`, `round` | the part, the direction, `tree` or `off` (off the map), the round |
| `parent_cluster`, `filed_from` | interrogation offshoots only: the cluster it was born from; the part it came from when re-filed under another part |
| `doubt` | doubt-card sketches only: the DOUBT line (the fact of the map that is disputed) |

### 5.5 idea_clusters.json

`{round, clusters[], n_sketches}`. One cluster per group of sketches that say the same thing, per part and direction.

| Key | Meaning |
|---|---|
| `cluster_id` | `<node>-<in or ou>-k<NN>`, for example `choice-in-k03`. **Positional**: it is the index in the grouping returned for that part and direction. A new grouping can reuse an id for a different cluster |
| `name` | short name from the clustering call |
| `members`, `n`, `representative` | sketch ids, their count, the sketch shown for the cluster (cheapest test first) |
| `cards`, `n_angles` | which cards reached it; how many distinct ways in (offshoots count by the idea they were born from) |
| `leap_share`, `leap_ops` | share of members that are leaps; their operators |
| `node`, `direction` | where it lives |
| `prior`, `prior_match`, `prior_source` | `new`, `known`, `failed` or `unknown` against the research brief; the matching entry; `model` or `lexical` |
| `obvious`, `obvious_match` | matches the private "first answers" list. `obvious_match` copies text from `private/defaults.json` |
| `score`, `rank` | selection score (angles, prior, departure, cheap test, size) and rank among the open clusters of the same part and direction (0 is best) |
| `selected`, `lane`, `lane_propensity` | chosen to be built; `main` or `longshot` (only chosen clusters); draw probability in the long-shot lane. A cluster taken to fill a slot the other direction could not fill also has `refill: true` |
| `novelty_gate` | `{nearest, audit, built, refill?}` from the near-duplicate gate |
| `merged_from` | `[{cluster_id, node, name}]` when the same idea filed under several parts was merged |

### 5.6 selection.jsonl

One row per cluster per round (the last selection of the round): `round`, `cluster_id`, `name`, `node`, `direction`,
`score`, `rank`, `kind_share` (leap share), `reason`, `lane_propensity`, `cut` (lowest main score in that direction).
`reason` is one of `picked_main`, `picked_lane`, `already built or excluded`, `slots exhausted (scored at or above the
cut; the turn went to another part)`, `below the cut`.

### 5.7 deepen.json: the arguments

`{nodes: [...]}`. A **root** node (`parent` null) is the first interrogation of an idea. Children follow its open
questions, down to depth 2. 36 roots and 72 children in the mock run, in two generations. [mock]

| Key | Meaning |
|---|---|
| `id`, `cluster_id`, `cluster_name`, `members` | `d` plus hex; the idea interrogated (cluster id is positional; `members` are stable sketch ids) |
| `gen`, `depth`, `parent`, `root`, `focus` | generation (0 first, 1 for ideas born in the interrogation); depth; parent node; root node; the open question followed |
| `qa` | `[{q, a, decides}]` the questions asked and the answers |
| `known`, `known_tagged` | facts the builder must know; same with `prov` (`script`, `web` or `belief`), and `check`, `check_quote` after a web fact check |
| `assumes`, `inherited`, `dropped_unsourced` | silent assumptions found; facts passed down; numbers dropped for having no source |
| `open` | `[{q, build, decides}]` questions still open; `build` says a build could answer it |
| `chain`, `chain_root`, `weakest`, `link_status`, `unknown_share` | the causal chain from the change to the score `[{id, text, quantity, baseline, expect, breaks_if}]`; the weakest link; each link marked after the answers |
| `offshoots` | sketch ids born here (they also appear in `ideas.jsonl` with card `deepen`) |
| `stop`, `call_id`, `node`, `direction` | why the chain stopped (or null); the call; the part; the direction |
| `objections`, `premortem_verdict`, `dialogue`, `revised_idea` | **roots only.** The critic's objections, a one-line verdict, `{exchanges, stop}`, and the idea text after the author conceded |

Objection: `{text, severity (high, medium, low), cls, link, if_true, cite, idea, dialogue}`.
`cls` is one of `breaks_constraint`, `hidden_cost`, `interaction_cancels`, `early_only`, `below_noise`, `impl_slip`,
`metric_blind`, `scale_only`. `if_true` is `{metric, op (above or below), threshold}` or null, the test that would
confirm it. `dialogue` is the author reply: `{reply (concede, rebut, measure), verdict (resolved, revised, standing),
fact, source, test, change, reason, exchange, idea}`. After a build the ladder adds `status` (`confirmed`, `refuted`,
`pending`, `untestable`) and `measured`; those copies live in `verify.jsonl` under `details.metrics.objections`, not in
`deepen.json`. [code]

`dialogue.jsonl` has the same replies flat: `idea` (cluster id), `round`, `objection` (1-based index), `cls`, `reply`,
`fact`, `source`, `test`, `change`, `verdict`, `reason`, `exchange` (1 or 2), `revised_idea`.

### 5.8 Builds and tests

`cands/<call_id>.jsonl` row (a `Candidate` plus `ts` and `t`, the creation time used to order a resume):

| Key | Meaning |
|---|---|
| `id` | `n` plus 10 hex characters. Also `tune_<knob>`, `ctl_<name>` for scripted candidates |
| `text`, `card`, `operator`, `seed` | the hypothesis and the change joined by a bar; `impl:<cards joined by +>`, `revise`, `fix`, `compose`, `tune`; the cluster id (or the revise move); seed |
| `round`, `call_id`, `parent_ids`, `lineage_id`, `program` | round; the builder call; parents; first ancestor; path `cands/src/<id>.py` |
| `extra` | `hypothesis`, `change`, `src_hash` (12 hex of the normalised source), `node`, `direction`, `cluster` (the cluster **name**), `members` (sketch ids), `prediction`, `lane` (`main`, `longshot`, `family`, `tune`, `program`), `target`, `scope`, `kind`, `leap_op`, `kill`, `fidelity` (`exact`, `partial`, `substituted`, `cannot`) with `fidelity_note`, and `manifest` (what the builder saw: members, cards, score, rank, prior, number of facts and objections, chain links) |

`verify.jsonl` row: `id`, `status` (`checked` or `fail`), `verification_type` (`execution`), `attempts`, `partial_score`
(rung reached over 4; 0.75 when three rungs pass), `feedback_record` (empty when checked; else `{rung, reason, ...}` with
the scorer stderr), `details.rung_reached` (script checker: 0 static, 1 build, 2 quick, 3 full, 4 long run; the LLM checker uses boundary, build, timing, learning, long), `details.metrics`,
`prediction_check`, `reused_from`, `round`, `ts`. Extra row kinds, same shape: `relabelled_against` (the reference
moved), `retested_against`, and a `long` block from the finish step.

Metrics (`details.metrics`; negative gap means better): `learn_score`, `learn_base`, `learn_gap`, `learn_sd`,
`learn_z` (quick check against the baseline or reference); `long_*` (full check); `half_gap`, `half_z`; `trend` (long gap
minus quick gap); `extrap_gap`, `extrap_z` (the pool is ranked by `extrap_z`, lowest first); `cost_ratio`,
`long_cost_ratio`, `cost`, `n_quick`, `build_score`, `changed_symbols`; `objections` (the critic list with `status` and
`measured`). Mode 3 adds `panel_score`, `panel_sd`, `judge_scores`, `criteria`, `people_score`, `people_n`,
`people_weight`, `panel_notes`.

`pool/<id>.json`: `id`, `card`, `operator`, `seed`, `lineage_id`, `parent_ids`, `hypothesis`, `change`, `node`,
`direction`, `src_hash`, `arm`, `baseline_version`, `lane`, `target`, `metrics`, `kind`, `leap_op`, `manifest`; later
also `long` and `retested_against`.

`reference.json`: `{reference: {cand_id, path, metrics, round, reason, hypothesis, set_at}, log: [{round, action (set or
moved), from, to, reason, gap, ts}], profile}`. `graph.jsonl` rows: `node` (`cand_id`, `card`, `operator`, `round`,
`lineage_id`, `root_ids`, `parent_ids`, `status`, `partial_score`, `origin`, `cluster_id`), `edge` (`src`, `dst`,
`kind2`: `parent_of`, `same_cluster`, `covers_constraint`), `cluster`.

### 5.9 Questions and yields

`next_questions.json`: `{round, top3[], explore, n_candidates, chosen, vetoed[], by, focus_contexts, requires_human,
answered, ts}`. `by` is `default`, `person`, `default after veto` or `none left`. A candidate question has: `id`
(`q_<cand8>` for a failure question, `u<hex>` for an upward proposal), `kind` (`question` or `upward`), `text`, `node`,
`parent`, `branch`, `test {metric, rung, op, what}`, `threshold`, `fails_if`, `requires_human`, `path`, `path_ids`,
`open_children`, and the score parts `p_resolve`, `gain`, `novelty`, `cost`, `lp_bonus`, `score`, `reason`, `rank`,
`slot` (`score` or `explore`). `questions.json` is `{picks: [one such record per round]}` plus `answered` and
`answered_by` once a build answered it.

`discovery.json`: per round `{round, contexts, sketches, new_clusters, new_per_context, top2_share, by_card: {card:
{sketches, distinct_clusters, yield}}}`. `source_yield.json`: per round `{round, by, tree, off, share_before,
share_next}`, with `final: true` on the last. `tree` and `off` hold contexts, sketches, clusters, built, checked, wins,
and per-context rates and shares. `seed_yield.json`: `{rounds: [{round, function: {name: {sketches, clusters}}, seed:
{word: {...}}}], mode}`.

### 5.10 Memory, facts, live view, reports

Per-part memory file `memory/[_mock/]<profile>/<part>.md`:

```
# Memory: <part>
CLOCK: 15
## FACTS            (then TRIED, PRIORS, CUES, OPEN QUESTIONS, FAILED FRAMINGS, ARCHIVE)
- [m666c0c] 2026-10-17 | <run> r1 | measured | <text> | <evidence> | used 15
```

Entry id is `m` plus 6 hex. Source is `script`, `measured`, `web` or `belief`. `CLOCK` counts curations of the part.
`used N` is the clock when the entry was last confirmed; five curations without it moves the entry to `ARCHIVE`. An entry
is kept only if it cites a candidate id, sketch id, measured number or URL that exists in the writing run, and is not a
near-duplicate (Jaccard above 0.6). Priors need a number. Cues need `when ... -> ...`. The text an agent sees is
capped at 4,000 tokens (`memory.py`). `memory_log.jsonl` row: `round`, `part`, `call_id`, `file`, `proposed`,
`added [{id, section, source, text}]`, `rejected [{section, text, reason}]`, `bumped`, `archived`, `ts`.

| File | Row or shape |
|---|---|
| `facts_fetched.jsonl` | `{key (normalised question), ts, node, question, answer, source_url, confidence (high, medium, low), tag}`; or `answer: null` with `reason` |
| `disputed_facts.jsonl` | `{round, node, text, sketch_id}` |
| `live.json` | `{phase, note, spent, spent_aux, inflight: [{call_id, role, card, operator, seed, started, note}], ts}` (`ts` in epoch seconds) |
| `research/<node>.json` | `{node, ts, queries, known [{name, mechanism, effect, where, url}], failed [{name, why, url}], open [{direction, why, url}], backend, source}`, plus `tried` after a ledger merge |
| `calls/<id>.json` | `{call_id, role, backend, model, text, usage {input_tokens, output_tokens, cache_*, total_tokens}, cost_usd, duration_ms, stop_reason, error, attempts, meta {card, operator, seed, note, node, memory, ...}, prompt_chars, flags}` |
| `answer.json` (30 keys) | `status`, `n_candidates`, `n_checked`, `lanes`, `origins`, `source_yield`, `ranked [{id, card, node, hypothesis, change, long_z, extrap_z, trend, learn_z, step_s}]`, `generations`, `upward_proposals`, `spent_tokens`, `budget`, `wall_s`, `next`, and for Mode 2 and 3 `mode`, `reference`, `reference_changes` (Mode 3 adds `proposals`) |
| `report.json` (60 keys) | funnel counts, cost, `pool`, `lanes`, `critique`, `commitments`, `selection`, `upward`, `briefs`, then the late sections `mode`, `reference`, `dialogue`, `premortem`, `fetched_facts`, `memory`, `questions` |
| `REPORT.md` | reference block (Mode 2 or 3), then "Run report": Read this first, funnel, cost, by card and part, pool, lanes, commitments, selection, critique, leaps, discovery, upward proposals; last "Questions the team chose" |

## 6. control.json: every key the loop reads

The file is `<run folder>\control.json`. It is per run, not per lab. It is one JSON object. Three functions read it.
`_stage` reads it at the five boundaries and keeps the last good copy if the file is cut or malformed (L1947-1954).
`_pick_question` and `_opinions_for` read it straight from disk and fall back to nothing on an error, with no warning.
Changes are logged in `control_log.jsonl` (when the file changes) but the log has no author field. [code]

"Level" means the loop sets its state from the file at every boundary, so removing a key clears it. "Edge" means a new
value is applied once.

| Key | Shape | Read at | When | Effect | Trigger |
|---|---|---|---|---|---|
| `pause` | bool | `_stage` L1985 | every boundary. While true the loop sleeps 10 s and re-reads the file (loop L1939-1988) | holds the run at that boundary and sets a note in `live.json` (L1987) | level |
| `stop_after_stage` | any true value | `_stage` L1983 | every boundary | raises `StopRun`. `run` catches it (L3226) and calls `_finish`, so answer and reports are written. The CLI `--stop-after <stage>` does the same for one stage | level |
| `note` | string, cut to 600 characters | `_stage` L1979 | every boundary | becomes `control_note`, printed as "NOTE FROM THE OWNER" at the end of `history_text` (L2253). Reaches idea agents only in round 2 up (L1241), interrogation (L1583) and the re-plan (L3703). `history_text` is empty until a candidate has been verified (L2245), so round 1 never shows it. Builders, critics, author replies, clustering and the question pick never see it | level |
| `skip_nodes` | list of node ids | `_stage` L1980 | every boundary | `_skipped` (L950). The part and its sub-parts, questions and wins get no idea contexts (L1108-1110), no research brief (L487), no owner seed (L1144), no focus contexts (L1190), and their clusters count as done, so they are not selected or interrogated (L3283, L3330) | level |
| `exclude_clusters` | list of cluster **names** | `_stage` L1981 | every boundary | clusters with those names count as done (L3283, L3330). Names can change when clusters are rebuilt. Not in the brief, but real | level |
| `add_nodes` | list of node specs `{id, name, parent, frame, assumptions, boundary, directions}`. Extra keys are kept | `_stage` L1982, then `_add_human_nodes` L1990 | every boundary. The first boundary comes after the map exists, so no spec is lost for lack of a map | adds each node once, `origin: "human"`, writes `problem_tree.json` at once (L2015), logs a `human_node` decision. See the cautions below | edge, by id |
| `budget_add` | int tokens | `_stage` L1964 | every boundary | `B += n` | edge |
| `aux_budget_add` | int tokens | L1966 | every boundary | `aux_budget += n` | edge |
| `k_impl` | int, 1 or more | L1968 | every boundary | build slots in round 1 (a third of it later) | edge |
| `rounds_max` | int, 1 or more | L1970 | every boundary | number of rounds | edge |
| `longshot_share` | float, cut to 0..0.6 | L1972 | every boundary | share of build slots for the long-shot lane | edge |
| `leap_share` | float, 0..1 | L1974 | every boundary | share of each idea agent's sketches that must be leaps | edge |
| `veto` | list of question ids | `_pick_question` L850, then `PK.apply_veto` (pick.py L206) | start of `ideate_round` for round 2 up: after the previous `verified` boundary, before any idea agent | removes those ids from the top 3 | level |
| `choose` | one question id | same | same | takes that question if it is still in the top 3 after the vetoes (`by: "person"`) | level |
| `opinions` | list of `{candidate or cluster, score 1-10, note, who}` | `_opinions_for` L3024. Called at L2913 (`verify`), L3055 (`_set_reference`), L3125 (`_retest_top`) | the moment each candidate is verified, Mode 2 and 3 only | `candidate` matches a candidate id. `cluster` matches the candidate operator (a cluster id) or the cluster name (L3030). Only the panel checker uses them (Mode 3): people mean mixed into the panel score with weight 0.25 x min(1, n/3), never above 0.5 (`checks/panel.py`). Other checkers ignore them | level, but read once per candidate. An opinion added later is not applied unless the candidate is checked again |

**Not control.json keys, although the brief lists them:**

| Name in the brief | What the code does |
|---|---|
| `owner_seeds` | A file, `memory/owner_seeds.json` (a list of `{part, text}`), or `--seeds-file`. Read once in `main` (L4445-4452), never again. Each seed becomes one idea context on the named part, **round 1 only** (L1139-1146). [doc] `docs/TEAM_GAPS_SPEC.md` L13 lists it as a control.json key; the code does not |
| `stop` | The key is `stop_after_stage` |
| `budget` | The keys are `budget_add` and `aux_budget_add` |

**Cautions for people steering together:**

1. One file, last writer wins. Two people editing `control.json` lose each other's changes, and `skip_nodes` from one
   person is erased by an empty list from the other. No code writes the file, so there is no merge and no lock.
2. `add_nodes`: an id that is already on the map (or was seen) is dropped without a log line (L2001-2005). Two people
   choosing the same id lose one node silently. The spec is copied with `**sp` (L2007), so an extra key such as `by`
   survives onto the node and into `problem_tree.json`.
3. A node added after round 1 gets idea contexts, but research briefs, analogy, diagnosis and adapt contexts are dealt in
   round 1 only (L1095, L1130-1137). A node also waits for the next boundary. In round 1 the first one is `ideated`,
   which comes after the first ideation, so the first contexts for a new node run in round 2.
4. `veto` and `choose` cannot be used to look first. `_pick_question` computes the top 3, applies the file as it is
   now, writes `next_questions.json` and runs the focus contexts in one call. A person sees the top 3 after the
   choice was made. A veto helps the next pick. [code]
5. `_control_applied` and `human_nodes_seen` live in memory only. After `--resume`, a `budget_add` still in the file is
   added again. (A re-added node is protected, because it is already in `problem_tree.json`.) [code]
6. `pause` is the only way to hold the run for a person, and it works at the boundaries only. There is none inside the
   interrogation stage, which is the longest model-bound stage. [code]

## 7. Lab-level files that runs share

These live outside the run folder, under `D:\AGI-lab`. Two loop processes on the same lab root already use them.

| Path | Written when, by whom | Mode | Safe for two processes? | Read by |
|---|---|---|---|---|
| `memory/ledger.jsonl` (15.6 MB) | every model call (`_ledger` L2506, then `harness/ledger.append`) and every verify (a zero-token row, L2940) | append, one write per row, thread lock only | in practice yes on local NTFS. The module says there is no cross-process lock | harness stats, people, `binpack_arms` (spend per reference move) |
| `memory/[_mock/]<profile>/<part>.md` | round end, `_curate_memory` | read-modify-write of the whole file | **no.** Thread lock only (`memory.py` `_LOCK`), plain `write_text` | every idea context that has memory (L1208) |
| `memory/research/<key>.json` | plan, round 1, real backend only (`save_cache`) | one write per key (key = part id + hash of profile, lens, version, frame). Reused for 7 days | mostly yes | `research_round` cache, `load_cached` |
| `memory/research/<key>.facts.jsonl` (+ `.lock`) | finish, real backend only (`merge_facts` L4022) | append under an `O_EXCL` lock file (stale after 60 s) | yes | `load_cached` merges them into the brief as known or disputed facts |
| `memory/experiments/verified_by_hash.json` (+ `.lock`) | verify span, real backend only (`_remember_hash` L2970, lock at L2985) | read, merge one key, write a temp file, replace, under `_file_lock` | yes. The code comment names "replicates and batch_verify writing at once" | loaded once at start (L473). A verdict another process writes later is not seen |
| `memory/experiments/ledger.jsonl` | after the overnight exam (`batch_verify.py` L401) | append | n/a | `_rounds` start (L3233), `inject_ledger` (L572) |
| `memory/lessons.jsonl` | finish, real backend only (`LS.update_from_run` L4099) | read all, merge, write all. No lock | **no** | `knowledge_for` (L1556), builder prompts |
| `memory/owner_seeds.json` | by people | by hand | n/a | `main` L4445, once at start |
| `runs/<profile>_baseline_profile[_mock]/` | start, Mode 1 only | cached under a key | yes (same key, same content) | the checker |

The mock backend writes the ledger and its own memory folder (`_mock`). It skips the research cache, the hash store and
the lessons. [code]

On this PC the only per-part memory folder is `memory/_mock/binpack_nobase/` with five files (`choice`, `open`, `state`,
`stats`, `ties`; CLOCK 15, 4, 6, 2, 1). Their entries come from four different mock runs, which shows the cross-run
sharing at work. No real-backend part memory exists yet, and `memory/lessons.jsonl` is empty. [mock]

## 8. What reaches an agent prompt today

Agents read the loop memory, not the files. This is the list of slots, so that a peer digest knows where to go.

| Agent | Built in | What goes into the prompt |
|---|---|---|
| Planner | `plan_tree` L650, `tree.planner_prompt` | problem text, the reading summary, baseline source, lens, measurements. A re-plan adds history, objections and disputed facts (L3703-3712) |
| Idea agent | `ideate_round._one` (L1199 on) | problem head with constraints, the part (path, parent frame, frame, boundary, assumptions, 8 idea assumptions, 3 disputed facts) or the whole map as text for off-map cards, **the part memory block** (L1208), card text, digest, **`history_text` from round 2** (L1241), leap and web notes |
| Clustering, merge, prior tag | `cluster_sketches` L1470 | sketch text only, blind to author and card; cluster names; the research brief |
| Interrogation | `deepen_round._call_node` L1575 | the idea brief, part name and frame, constraints, baseline code, research text, **`history_text`** (L1583), the chain and facts of the parent node |
| Pre-mortem critic, author reply | `deepen.premortem_prompt`, `deepen.reply_prompt` | the idea brief, constraints, baseline source, a fact pack, the chain, published failures; the objections. No history, no note |
| Builder, reviser | `spec_prompt` L2613 | problem head, the part boundary, the idea brief, interrogation facts and resolved objections (`knowledge_for` L1536), pitfalls from lessons, output format; for a revise the old source and the failure record. **No note, no history, no memory block** |
| Memory curator | `_curate_memory` L1871 | this round's results on one part, its memory text, brief URLs |
| Panel judge (Mode 3) | `checks/panel.py` | one proposal under a random alias, criteria, known facts |

There is no slot for "what another person or agent changed". The three nearest are the part memory block (updated at
round end only), `history_text` (own results plus `note`) and the map text (own tree). [code]

## 9. What a live view can and cannot rely on

Read this before designing the tree and cluster views.

### 9.1 When a file can be read

| Case | Files |
|---|---|
| Safe to read at any moment | `state.json` (atomic replace), `graph.jsonl` (atomic replace). JSONL files by whole lines: `append_jsonl` writes one blob per call under a lock. `deepen_round` and `_dialogue` open the file and write one line per call. A torn last line can still happen, so readers skip a line that does not parse (as `harness.schemas.read_jsonl` does) |
| Can be cut in the middle | everything written with `write_json` or `write_text`: `problem_tree.json`, `idea_clusters.json`, `deepen.json`, `live.json`, `reference.json`, `report.json`, `pool/*.json`, the memory `.md` files. The dashboard returns its default for that poll and the panel blanks |
| Windows file locks | a writer can get `PermissionError` while a reader has the file open. `_live` and `state.json` retry. The other writers do not |

### 9.2 Which ids hold still

| Kind | Examples | Holds still? |
|---|---|---|
| Random 10-hex ids | sketch `s...`, candidate `n...`, model call `c...`, interrogation node `d...`, upward proposal `u...` | yes, unique across processes in practice |
| Derived from a candidate id | question `q_<cand8>`, win `win_<cand8>` | yes |
| Content hash | memory entry `m<6hex>` (part, section, text, run, round) | yes, but two runs can make the same text with different ids |
| Chosen by the planner or a person | tree node ids (`choice`, `state`, a person id) | no. The planner picks different ids in different runs. Two planner ids that clash get a `_2` suffix. When two people pick the same id, the second node is dropped |
| Positional | cluster ids `<node>-<in or ou>-kNN`; the objection number in `dialogue.jsonl` | **no.** A cluster id is the index in one grouping. Any new sketch in a part and direction triggers a new grouping call (the cache key is the set of sketch ids, L1470 on). In the mock run 119 ids kept their names between rounds, but the mock clusterer is deterministic. [mock] With a real model, expect ids to move |
| Names used as keys | `exclude_clusters`, `extra.cluster` on a candidate, `cluster` in an opinion | no. Names come from the clustering call |

To follow a cluster over time, match on `members` (sketch ids). The loop does the same: it marks an idea as built through
the sketch ids in `implemented`, not through cluster ids (L3282). [code]

### 9.3 How often things change

| Cadence | Files |
|---|---|
| During a stage | `live.json` (at least twice per model call), `deepen.json` and offshoot lines in `ideas.jsonl` (per interrogation node), `dialogue.jsonl`, `verify.jsonl` (per candidate, serial), `cands/*.jsonl` (per builder call), `facts_fetched.jsonl`, `calls/`, `prompts/` |
| End of a stage | `problem_tree.json`, `idea_clusters.json`, `selection.jsonl`, `discovery.json`, the idea batch in `ideas.jsonl`, `proposals_upward.jsonl`, `source_yield.json`, `seed_yield.json`, `next_questions.json` |
| Round end | memory files, `memory_log.jsonl`, `graph.jsonl`, the `cycle` decision, the final `problem_tree.json` of the round |
| Finish | `answer.json`, `report.json`, `REPORT.md`, `questions.json` (`answered`), final yield rows |

Sizes in the mock run: `ideas.jsonl` 460 KB, `deepen.json` 428 KB (rewritten whole at least 108 times), `idea_clusters.json` 84 KB,
`selection.jsonl` 59 KB, `dialogue.jsonl` 54 KB, `problem_tree.json` 15 KB, `state.json` 14 KB. A view should read
deltas, not whole files. [mock]

### 9.4 Other cautions

1. **The disk is output.** The loop does not re-read the tree, sketches, clusters or interrogation nodes. Writing into
   those files from outside changes nothing and is overwritten. The inputs are `control.json`, memory, ledgers and
   caches (sections 6 and 7). It also re-reads some files it wrote itself, for bookkeeping: `problem.md`, `state.json`,
   `disputed_facts.jsonl`, `verify.jsonl`, `selection.jsonl`, `pool/*.json`, `report.json`, `calls/*.json`.
2. **Privacy.** `private/defaults.json` is never routed to a generator, but the call record `calls/<id>.json` and the
   prompt `prompts/<id>.txt` of that call sit in the ordinary folders (the id is in `private/defaults.json`). Also
   `obvious_match` in `idea_clusters.json` copies text from that private list. A shared space must not mirror
   those, and a peer digest must not carry `obvious` or `obvious_match` into an agent prompt. [mock]
3. **No tree history.** `problem_tree.json` is a snapshot. There are no round snapshots and no change log
   (`tree_changes.jsonl` is proposed in `docs/mapper/03_maintenance_and_people.md` and is not built). The only trace of
   map edits is in `decisions` (`human_node`, `fail_question`, `promote_off_win`, `replan`, `replan_carry`,
   `tree_depth`). [code]
4. **No author.** No artifact records which person or which agent role made a change, except `origin` on a node,
   `who` on an opinion and `family` (model name) on a sketch. [code]
5. **The current dashboard** (`nano/dashboard.py`, port 8765, 127.0.0.1, stdlib `ThreadingHTTPServer`) is read only. It
   polls `/api/state` every 2 s. Each poll re-reads all of `calls/` (823 files, 3.4 MB in the mock run) plus the big
   files, about 4.5 MB. It has no write path to `control.json`. It shows: state and spend, live calls, candidates and
   rungs, tree counts per part and direction, the idea map, interrogation Q and A, the pool, the decision log. It does
   not show: objections or author replies, selection reasons, question picks, memory, the reference, control. [code]

### 9.5 Which files feed which view

| View | Read | Fields to use | Changes |
|---|---|---|---|
| Problem tree | `problem_tree.json` | `tree` for layout. In `nodes[]`: `id`, `name`, `parent`, `kind`, `origin`, `depth`, `path`, `directions`, `stats.<direction>.{sketches, clusters, implemented, checked}`, `priority`, `disputed`; on the root `proposals`; on questions `test`, `threshold`, `fails_if` | end of ideated, clustered, deepened and round end; at once when a node is added |
| Idea clusters | `idea_clusters.json`, with `ideas.jsonl` and `selection.jsonl` | cluster: `name`, `members`, `node`, `direction`, `score`, `rank`, `selected`, `lane`, `prior`, `n_angles`, `leap_share`. The sketch text comes from `representative` in `ideas.jsonl`. The reason comes from `selection.jsonl` | up to three snapshots per round. New offshoot sketches stream into `ideas.jsonl` during the deepened stage |
| Arguments | `deepen.json`, with `dialogue.jsonl` | on a root node: `objections[].{text, severity, cls, if_true, dialogue.{reply, verdict, fact, source, test, change}}`, `premortem_verdict`, `revised_idea`, `chain`, `weakest`, `known_tagged`. On children: `qa`, `open` | per interrogation node, live in the deepened stage. The `status` of an objection arrives later in `verify.jsonl` |
| Test results | `verify.jsonl`, with `cands/`, `pool/*.json`, `reference.json` | `status`, `details.rung_reached`, `feedback_record.reason`, `details.metrics.{learn_gap, learn_z, long_z, extrap_z, trend, cost_ratio, objections}`; the idea text from `cands/` | per candidate in the verify span (serial). Long-run rows at finish |
| Team question | `next_questions.json`, `questions.json` | `top3[]`, `chosen`, `by`, `requires_human`, `answered` | start of each round from round 2 |
| Presence and progress | `live.json`, `state.json` (`stage`), `calls/` | `phase`, `note`, `inflight[]`, `stage`, `spent` | at every model call |
| Team memory | `memory/.../<part>.md`, `memory_log.jsonl` | entries per section, with source and evidence | round end |

## 10. How a second loop process could share a problem

What a "problem" is for the loop: the profile (goal, constraints, default map), `problem.md`, the tree, and everything
built on the tree. The profile and `problem.md` come from the code and a flag, so two processes with the same
`--profile`, `--aim` and `--only-nodes` start from the same problem. The tree is the part that differs: each process
plans its own map in round 1 (L1092) and the planner picks different ids each time. [code]

| Option | Where the second process works | What it sees of the first | What breaks | Verdict |
|---|---|---|---|---|
| **A. Same run folder** | same `--batch`, `--replicate`, `--arm` and profile, so the same `run_dir` | files, but the loop never re-reads them. Without `--resume` it rewrites the `state.json` header (L3208) and wipes the other's state. With `--resume` it loads the folder once, then both go their own way | no run lock in the nano loop (`run.lock` exists only in `harness/think.py`). `state.json` `decisions` is replaced by each process's own list. `write_json` files race (`problem_tree.json`, `idea_clusters.json`, `deepen.json`). `selection.jsonl` is rewritten. Each process keeps its own in-memory tree, so the two maps drift | **Unsafe.** Fine for one writer and many readers (the dashboard does this) |
| **B. Own run folders, shared memory folder** | different `--batch`, same `HTSA_LAB_ROOT` and profile | per-part memory entries, from the end of the other process's round (one round late), the research cache (real backend, 7 days), lessons, overnight verdicts, source-hash verdicts written before this process started. Not the tree, ideas, arguments or results of the current run | `Memory.curate` and `archive` take only a thread lock and rewrite the whole file: two processes on one part can lose an entry, and a reader can see a cut file. `lessons.jsonl` is rewritten without a lock. Part ids must match: the planner ids differ per run, the default ids (`choice`, `state`, ...) hold only when the planner keeps them | **Works today for runs one after another.** For live work it is too coarse. Needs a lock and an atomic save on the memory file |
| **C. Own run folders plus a new shared-space folder** | e.g. `D:\AGI-lab\spaces\<space_id>\` with an append-only event file, a snapshot per object kind, and one steering file per person | everything the other process publishes, at the cursor you choose | nothing new, if the loop stays the only writer of its own folder and the space is written by append and by temp-and-replace. The code base already has all three patterns (ledger append, `O_EXCL` lock file in `_file_lock` and `research._facts_lock`, `state.json` replace) | **Recommended.** Needs the hook in section 11 and a way to start the second process on the shared map |
| **D. One loop process, several people** | one run folder; each person steers it | everything, because there is one in-memory state | none from sharing. Costs: one budget, one set of agents; no field says which person made a change; `note` is one string | **Simplest and safe.** Per-person lanes and notes would be new |

Facts that decide between them:

1. The loop already runs as parallel processes on one lab root: replicates. The comment above `_file_lock` (L4225)
   says "replicates and batch_verify write it from separate processes". Options B and C extend that pattern. [code]
2. A second process can only adopt a shared map through code that does not exist yet. `ideate_round` plans only when
   `self.tree is None` (L1092), and `research_round` sits in the same `if`, so presetting the tree skips the research
   briefs too. `load_state` is the only reader of `problem_tree.json` and it reads the process's own folder. [code]
3. Problem identity for the space can come from `commitments.json`: `rules`, `baseline_hash`, `lens`, `aim`, `scope`,
   and `profile` (present only when it is not `llm`). The existing `commitments_hash` also includes budget, slots and models, so two people with different
   budgets get different hashes. A space needs its own hash over the problem fields only. [code]
4. Never put in the space: `private/`, the call and prompt files of the defaults call, `state.json` (spend and
   decisions of one process), `obvious` and `obvious_match`. [code]
5. Same machine versus two machines: the lab root is a disk path. Two processes on one PC share it. Two PCs need a
   service in front of the space. See `00_environment.md` for the server options on this PC. [doc]

## 11. `_stage` as the hook where a shared space is read and written

### 11.1 What `_stage` does today (L1932-1988)

1. At `verified` it sets `completed_rounds`.
2. It writes `state.json` with the stage marker, the spend and the decisions. The stage's artifacts are on disk.
3. It reads `control.json`, or keeps the last good copy.
4. It logs a change in `control_log.jsonl`.
5. It applies the edge keys once (`budget_add`, `k_impl`, ...).
6. It sets `note`, `skip_nodes`, `exclude_clusters` and adds `add_nodes` to the tree.
7. It raises `StopRun` on `stop_after_stage`.
8. It returns, or sleeps 10 s and starts again from step 3 while `pause` is set.

### 11.2 Why it fits

- It runs on the main thread with no worker pool open. Every `ThreadPoolExecutor` block has closed before the call.
  So changing `self.tree`, `self.skip_nodes` or `self.control_note` there cannot race with an agent thread.
  `_add_human_nodes` already does exactly this. [code]
- It is the only place where outside input enters live state, and it is already idempotent for nodes (by id).
- It saves state before it reads input, so a push placed right after the save publishes a consistent view.
- The `pause` loop re-reads every 10 s, so a pull inside it keeps steering alive while the run waits for people.
- The mock run called it 10 times in 77 s (5 per round). With real agents the gaps are long. [mock]

### 11.3 Proposed shape (additions only)

```
def _stage(self, round_no, name):
    if name == "verified": self.completed_rounds = ...      # L1935, unchanged
    self._write_state(stage={...})                          # L1937, unchanged
    self._space_push(round_no, name)       # NEW 1: publish what this stage produced
    while True:
        ctl = <read control.json as today>                  # L1940-1959
        ctl = self._space_pull(ctl, round_no, name)  # NEW 2: fold other members into ctl
        <apply block, unchanged>                            # L1960-1984
        <pause check, unchanged>                            # L1985-1988
```

`_space_push` appends one event per object that changed since the last push. `_space_pull` reads the events of the
other members after a cursor and turns them into the control shape: `add_nodes`, `skip_nodes`, `note`, `opinions`,
`veto`, `choose`, `pause`. Because the result goes through the same apply block, the level and edge rules stay the same.
The push half can also run as a sidecar that tails the files in section 4 with no change to the loop. The pull half
cannot: only code inside the loop can change its memory.

### 11.4 What to publish at each boundary

| Boundary | Publish (changes since the last push) | Source |
|---|---|---|
| `planned` (new, see gap 2) | tree nodes; brief counts per part | `self.tree`, `self.briefs`, `problem_tree.json`, `research/` |
| `ideated` | new sketches (id, idea, mechanism, node, direction, card, kind); upward proposals; disputed facts; the question pick (top 3, chosen, by) | tail of `ideas.jsonl`, `proposals_upward.jsonl`, `disputed_facts.jsonl`; `next_questions.json` |
| `clustered` | clusters (name, members, node, direction, score, rank, selected, lane, prior); selection reasons; discovery curve | `idea_clusters.json`, `selection.jsonl`, `discovery.json` |
| `deepened` | interrogation chains; facts with provenance; objections with author replies and verdicts; revised ideas; the final build picks | `deepen.json`, `dialogue.jsonl`, `idea_clusters.json` |
| `built` | candidates (id, cluster, hypothesis, change, lane, fidelity); fetched facts | `cands/*.jsonl`, `facts_fetched.jsonl` |
| `verified` | test results (status, rung, key metrics, reason); pool changes; reference moves; failure questions and wins on the tree; memory entries added; spend | tail of `verify.jsonl`, `pool/`, `reference.json`, `problem_tree.json`, `memory_log.jsonl`, `state.json` |
| finish | answer and report | `answer.json`, `report.json` |

Cursors: use the byte offset for JSONL files and a content hash (or `ts`) for rewritten files. Do not use list
position in `decisions` (section 5.2). Do not key clusters by `cluster_id` (section 9.2).

### 11.5 Gaps to close, in order

1. **`veto`, `choose` and `opinions` bypass `_stage`.** They re-read the disk file (L850, L3027). Make both read the
   merged control kept in `self._last_control`, or a merged copy, so shared steering reaches them.
2. **No boundary after the plan.** `plan_tree` and `research_round` run inside `ideate_round` (L1092-1099) with no
   `_stage`. Add `_stage(round_no, "planned")` after them, and add the name to the `--stop-after` choices (L4359). Then a
   second member can add parts before the first idea contexts are dealt.
3. **A slot for peer changes in the prompts.** Add `self.peer_digest` with its own cap (the note cap is 600 characters).
   Set it in `_space_pull`. Append it wherever `history_text()` is used (L1241, L1583, L3703) and to the builder prompts
   in `spec_prompt` for `implement` and `revise` (L2628-2711), and to the critic and the author reply. Today the note
   misses builders and round 1. Keep `obvious` and `obvious_match` out of it.
4. **Steering per member.** Replace the single `control.json` with one input per member, merged by rule: `skip_nodes`
   as a union, `note` joined with names, `opinions` keyed by member and target, `add_nodes` deduped by id with the
   author kept. Log a line when an `add_nodes` id is dropped (L2001-2005 drops it silently).
5. **Idempotence across a resume.** Persist `_control_applied` and `human_nodes_seen`. Today a resume adds `budget_add`
   again.
6. **A way to start a second process on the shared map** (section 10, fact 2): load nodes and briefs from the space, and
   skip `plan_tree` and `research_round` on purpose.
7. **Progress inside long stages.** `_stage` runs five times per round, and nothing runs inside interrogation, builds
   or verification. Add a cheap `_space_tick()` after each interrogation chain, build and verification. It may push (it
   only reads loop state, under `self.lock`) and it may queue pulled edits. The queue is applied at the next `_stage`.
   Never change `self.tree` outside `_stage`: worker threads read it.
8. **Authors and revisions.** Put `by` and `rev` on events, on nodes (a node spec keeps extra keys, L2007) and in
   `control_log.jsonl`. Merge rule: adding a node by a unique id commutes. A "set" of a field is last writer wins per
   (member, field). The loop never deletes a node (a re-plan carries them), so deletes need a new rule.

Suggested event envelope: `{space, member, seq, ts, round, stage, kind, target, payload, rev}`. `kind` examples:
`node_added`, `node_skipped`, `note`, `opinion`, `question_chosen`, `sketch_batch`, `cluster_snapshot`, `objection`,
`candidate_built`, `test_result`, `memory_added`, `applied`.

For a Figma-like feel the space shows a person's edit at once as pending. The loop writes an `applied` event from
`_space_pull` and the edit turns solid. The cost is that an edit reaches the agents at the next boundary only. This is
a design from reading the code. It was not tested. [code analysis]

### 11.6 Related repo docs [doc]

- `docs/mapper/03_maintenance_and_people.md`: a data model for people (Problem, Branch, Fact, Idea, Result, Comment,
  Vote, Flag), four actions (add a branch, comment, vote, flag prior art) and a recommendation of SQLite behind one
  writer service. It lists "more than one person" and "adding a branch after round 1" as missing. The code path for a
  late branch exists (`_add_human_nodes` runs at every boundary). What is missing is research for the new branch
  (section 6, caution 3).
- `docs/TEAM_OF_RESEARCHERS.md` line 36: people are "partly built ... no shared space yet".
- `docs/PROBLEM_TREE.md`: the node schema table. It agrees with section 5.3.
- `research_notes/product/multiplayer/00_environment.md`: server options on this PC.

## 12. Not verified

- Real (non-mock) behaviour. The mock backend answers at once with fixed text. I did not see a real doubt card write
  `disputed_facts.jsonl`, a real clusterer move cluster ids between rounds, or real wall times of the agent stages.
- Mode 1 files (`controls.json`, `tuning.json`, `anomalies.json`, diagnostics) and the `clusters.jsonl` duplicate rows
  are described from code only.
- The Mode 3 panel files were checked in one other mock run (`mock-mode3__nano__review_process__scaffold__r0`) for
  `pool/*.md`, `proposals` and the `control.json` opinions. I did not trace `people_*` metrics through a verify row.
- Line numbers are for commit `74abcaf`. Another note in this folder (`00_environment.md`) was written in parallel by a
  different task. I read it only for the server options.
- No web facts were used, so there is nothing tagged verified or memory.
