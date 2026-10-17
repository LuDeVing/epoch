# Team gaps: what to build (contract for five parallel agents)

Source: research_notes/team_gaps/00_SYNTHESIS.md (and 01-05). Every feature is behind a flag with a control
arm, because the research says each helps only under conditions and must be measured. Git worktrees, one
agent per branch; loop.py edits are additive hooks at the named points, so merges stay simple. Load rule:
at most one mock dry run at a time per agent, smallest settings, prefer `--profile binpack_nobase` (CPU, fast),
only your own test file with pytest.

Shared facts: profiles in nano/profiles, `from nano import profile as PF`, tree helpers in nano/tree.py
(children, depth, path, leaves, add_failure_question, promote_win, OFF_TREE_NODE), the loop in nano/loop.py
(ideate_round builds `specs`, `_one(spec)` builds each prompt, `_stage(round, name)` marks stage ends and
reads control.json, `_write_tree`, `deepen_round`, `run_card` for builds, `report.py` for REPORT.md).
control.json is the human channel (skip_nodes, owner_seeds, add_nodes, opinions).

| Agent | Owns | Hook in loop.py (additive only) |
|---|---|---|
| A memory | nano/memory.py (new), nano/profiles/* only to add a `memory_dir` default | in `_one`: append a MEMORY block after the node prompt; at each `_stage(..., "verified")`: propose + curate deltas; flag `--no-memory` |
| B dialogue | nano/deepen.py | in `deepen_round` where premortem objections are produced: call the reply round; flag `--no-dialogue` |
| C question picking | nano/pick.py (new), nano/tree.py only `add_failure_question` (add test/threshold/fail fields) | at the start of `ideate_round` for round > 1: read the pick, give the picked node extra contexts; flag `--pick-questions` (default on), control.json `veto` |
| D fetch on demand | nano/research.py (`fetch_fact`), the build/revise path in loop.py (`run_card` reply parsing) | parse `NEED: <fact>` lines in builder replies, fetch (cap 2 per call), re-prompt once; flag `--fetch-on-demand` (default on when web is on) |
| E evidence | harness/noveltybench.py, nano/experiments/binpack_arms.py (new) | none |

Every agent: plain English prompts, short sentences, no em-dashes; a test file harness/tests/test_gap_<letter>.py;
commit on the branch; report under 300 words with files, flags, what the control arm is, and merge notes.
