# Problem tree: decomposition with inward and outward search

Status: v0.2, 2026-10-17. Implemented in `nano/tree.py` and wired into `nano/loop.py`. v0.1 (2026-10-11) was a
flat map of parts; fix 8 (commit 7e3b1db) made it a real tree.

## Why

Two kinds of creativity appear in the research (Boden): exploratory, improving inside a frame, and
transformational, replacing the frame. The catalog entries for this are GEN-12 (constraint transformation, which
cites Boden's theory) and REP-13 (frames set what is salient and create blind spots). REP-05 (value-guided
construal) is the basis for decomposing the problem at all, and REP-11 (counterfactual framing) for the outward
direction; neither of those two states the two kinds of creativity. A loop that only asks "how do we improve X"
stays inside the paradigm it was handed. The problem tree makes both directions explicit at every part of the
problem, and keeps the verifier the same for both, so a radical idea is judged on the same metric at the same
budget as a tweak.

## The tree

Before the map is drawn, one reading call (card `preread`) asks the research model how the field splits this
problem; its summary goes to the planner as WHAT THE FIELD SAYS ABOUT THIS PROBLEM (`--no-preread` is the
control arm; it is also off with `--no-research`). A planner call with the strong model then decomposes the goal
into parts (fallback: the profile's default tree). For the nano trainer the default parts are: inputs and
outputs, sequence mixing, per-token computation, state across depth, optimization, data, objective, the whole
recipe (cross-part changes), plus the root.

The tree has up to four levels below the root: parts (depth 1), sub-parts (2), questions (3), helper questions
(4). A deeper node is moved up to its depth-3 ancestor (`enforce_depth`, logged as `tree_depth`). Children come
from the planner (a `parent` field on a sub-part), from `promote_win` (an off-map win hangs under the part its
sketch named) and from failures (`add_failure_question`: a failed check with a reason becomes a question under
its part).

## Node schema

Every node is a dict. `problem_tree.json` adds the computed fields at the end of the table.

| Field | Meaning | Who writes it | Who reads it |
|---|---|---|---|
| `id` | short unique id | profile default tree; planner (`parse_planner`: cleaned, made unique, never root/recipe/offtree); `promote_win` (`win_<cand>`); `add_failure_question` (`q_<cand>`); owner via control.json `add_nodes` | every stage: contexts, clusters and candidates carry it as `node` |
| `name` | the part in a few words; planned names start with the default part's name and a colon | same writers; a question is named `why did <idea> fail?` | idea and build prompts, `resolve_scope`, `find_part`, the question chooser, the report |
| `parent` | the node above; `root` for a part | planner (accepted only when it names a node of the same reply or of the default tree); `promote_win`; `add_failure_question`; owner nodes; `enforce_depth` may move it | `children`, `depth`, `path`, `deal_contexts`, `nested`, the dashboard |
| `kind` | `part` (default when absent), `question` or `win` | `add_failure_question` (question), `promote_win` (win) | `deal_contexts` (a question takes at most 1 context), `find_part` (parts only), `nested` |
| `frame` | how this part works today, one or two sentences | planner, profile; a win's hypothesis; a question's failure reason | idea prompts (`node_prompt`), research prompts and the research cache key (frame hash) |
| `assumptions` | 3 to 5 design choices a different paradigm could remove | planner (at most 5), profile, owner nodes; a win carries its change. Never grows during a run | the outward direction (each sketch must remove or invert one), the inward direction (treated as fixed) |
| `idea_assumptions` | what tested ideas on the part silently assumed, with `from`, `text`, `round`, `kind` (`silent` or `could_not_build`) | interrogation (silent assumptions); a builder's could-not-build note | idea prompts as context only, newest first, at most 8, under the head "not design choices; context only, do not treat as rules to break". Never transform material |
| `boundary` | the code a change at this node may touch | planner, profile; `boundary_all` for wins and owner nodes without one; a question inherits its parent's | build prompts and the rung-0 boundary check; `scope_text` |
| `directions` | `inward` and `outward` for parts; `upward` for the root; `inward` for questions | planner (always inward and outward), profile, `add_failure_question` | `ideate_round` and `deal_contexts` |
| `refines` | the default part this node refines, or `new` | planner; default nodes refine themselves | `resolve_scope` (`--only-nodes`), the re-plan merge |
| `priority` | `low` when a re-plan kept a node it no longer drew | re-plan (`--replan`), except for promoted, owner and implemented nodes; cleared when drawn again | `deal_contexts`: one context per direction instead of `per_node` |
| `origin` | `offtree` (promoted win), `failure` (question), `human` (owner); absent for planned and default nodes | `promote_win`, `add_failure_question`, the control-file hook | the re-plan (keeps these nodes), the report (`promoted_branches`) |
| `disputed` | facts of the map a doubt card disputed, with `round`, `text`, `sketch_id`, `status` | `_record_doubts` | idea prompts, marked "disputed, re-measure before relying on it", at most 3; the re-plan |
| `from` (questions) | the failed candidate ids | `add_failure_question` | the report |
| `test`, `threshold`, `fails_if`, `enterable` (questions) | the metric and rung that would answer the question, the number, the failure condition; `enterable: False` when none can be derived | `add_failure_question` via `failure_test` | the question chooser (`nano/pick.py`): only enterable, unanswered questions are picked |
| `proposals` (root, in problem_tree.json) | upward proposals for a new verifier: `proposal`, `reframing`, `new_measure`, `why`, `cost`, `round` | parsed from upward replies, written by `_write_tree` | people and the dashboard; the question chooser takes upward proposals as pseudo-questions that need a person |
| `depth`, `path` (problem_tree.json) | depth below the root; names from the part down | computed by `_write_tree` (`tree.depth`, `tree.path`) | the dashboard, the report, the question chooser |
| `stats` (problem_tree.json) | per direction: sketches, clusters, implemented, checked; `n_idea_assumptions` | `_write_tree` | the dashboard, the report |

## Directions

- Inward: assumptions are fixed; improve inside them.
- Outward: every sketch must remove or invert at least one assumption and name it on a `REMOVES` line.
- Upward (root only): alternative formulations of what is modeled or measured. Parsed in their own reply format,
  logged to `proposals_upward.jsonl` and shown on the root's `proposals`; never implemented, because they change
  what can be checked.

## Flow per round

1. Ideation. Contexts are dealt by `deal_contexts`: every top-level part gets `per_node` contexts per direction
   (default 1; 1 in later rounds), and a part with children shares that budget with them, so a deeper map costs
   no more contexts than a flat one. Cards cycle over seeded, low_prior, transform, formal and docs; in tree mode
   the transform card becomes formal, because the node's own assumptions are already the outward material. The
   root gets 2 upward contexts per round (`UPWARD_CONTEXTS`); under a test cap `keep_upward` keeps one. On top:
   one research context per part x direction whose brief has literature rows (so every run compares with and
   without research), and in round 1 one analogy, one diagnosis and one adapt context per top-level part when
   their inputs exist. Off-map contexts (blank, gaps, doubt) are added at `--off-tree-share` (default 0.4) of
   all contexts. From round 2 the team's chosen question gets `--focus-contexts` (default 2) extra contexts.
2. Clustering: one blind call per node and direction groups sketches by mechanism (lexical fallback).
3. Selection: `k` implementation slots split by `inward_share` (default 0.6), filled round-robin across nodes
   within each direction, plus the long-shot lane (`--longshot-share`, default 0.2). The selection critique of
   2026-10-17 (research_notes/selection_cost/) found that the sources point to about one fifth reserved and a
   within-part cap instead of a round robin, but recorded "no code change now": no real run has built through
   this selection yet. Two zero-cost measurements (score rank of every winner; rank correlation of 45-step,
   240-step and long-run gains) decide whether the quotas move.
4. Implementation: one complete file per selected cluster, scoped to the node's boundary.
5. Verification: the cheap rungs, the long comparison for the pool, the overnight verdict (docs/VERDICT.md).
6. Later rounds: revisions of near misses, the next clusters, failure questions and promoted wins on the map.

## Outputs

`problem_tree.json` (nodes with the fields above, the nested tree, lens and lens design, origin yields),
`ideas.jsonl`, `idea_clusters.json`, `proposals_upward.jsonl`, `next_questions.json`, and the usual candidate,
verify, pool and graph files. The dashboard shows the tree and the idea map live.

## Cost

The number of contexts depends on the map, the briefs and the off-map share, so there is no fixed count. On the
default LLM tree at `per_node` 1 the card contexts alone are 8 parts x 2 directions + 2 upward = 18; research,
analogy, diagnosis, adapt and off-map contexts come on top. Every planner, repair and re-plan call goes through
the same affordability check as the other stages.

## Not yet

The lemma pool over smoke curves, ledger-driven budget shifts toward the nodes that produce verified wins, and
re-measuring a disputed fact (it stays marked until then). Sub-parts, failure questions and depth up to 4 exist.
</content>
</invoke>
<invoke name="Bash">
<parameter name="command">cd /c/Users/User/Desktop/AGI/.claude/worktrees/agent-adae7c20b0f56c39a && grep -n "REMOVES\|proposals_upward\|next_questions.json" nano/loop.py nano/ideate.py nano/pick.py | head; grep -n "planner\|replan" nano/loop.py | grep -n "_afford" | head -4