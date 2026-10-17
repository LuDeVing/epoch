# Mapper, parts 5 and 6: maintenance across rounds, and people

Scope: how the tree is kept alive after round 1 (MAINTENANCE), and how humans share it (PEOPLE).
SPLIT and FACTS are in 01; QUESTIONS and RANK AND LINK are in 02. Names below follow
`nano/tree.py` and `nano/loop.py`. "Proposed" means not built.

## Three modes

| | Mode 1: baseline + check | Mode 2: check, no baseline | Mode 3: no check |
|---|---|---|---|
| Reference for "win" | the baseline artifact | best artifact so far (it moves) | none; blind-panel score |
| Maintenance | write back by z vs baseline | write back vs current best; when the best changes, re-label old results "vs old best" and re-rank | write back panel score plus spread; status is "preferred" or "not preferred", never "won" |
| People | steer; tests decide | steer; tests decide | opinions are evidence, entered as extra judges with a capped weight |

## 1. Maintenance

### What a tested idea writes back

Each tested idea leaves a `result` record under the question it answered. Today `_write_tree`
only writes counts per direction. Add:

```
result: {name, candidate_id, round, origin ("tree"|"off"|"human"),
         metrics: {learn_z, learn_gap, long_z, cost_ratio}, status, ref}
status: win | tie | loss | failed_check | not_built
ref:    "baseline" | "best@round2" | "panel"      (what the numbers are against)
```

Win means `_gain(c) < 0` and status "checked", as in `_promote_off_wins`. Tie means the gain is
inside the profile's `score.margin`. Losses and failed checks are kept; they are evidence.

### A failure spawns a child question

Only when the verify record gives a reason (`feedback`, `rung_reached`). Template:

```
Q: "<idea name> failed at <rung name> because <feedback reason>.
    Is the cause <the assumption it relied on>, or <how it was built>?
    What would make <part> work under that limit?"
parent = the question the idea answered; origin = "failure"; depth = parent depth + 1
```

One child per distinct reason. If a child with that reason exists, add the result to it.
A win with a cost (see `contradictions()`) also spawns a child: "keep the gain, remove the cost".

### Merge, split, depth, promotion, lowering

```
 round ends
    |
    v
 write results --> failures -> child questions --> promote off-map wins
    |
    v
 merge duplicates (same parent, similarity >= 0.85)
    |
    v
 split crowded (> 8 children or > 12 hung ideas, two clear groups)
    |
    v
 enforce depth <= 4 --> lower quiet branches --> snapshot + diff
```

- Merge: same parent, name+frame similarity at least 0.85 (the clusterer's measure). Keep the
  older id, move children and results, store the other id in `aliases`. Log it.
- Split: a node with more than 8 children or more than 12 hung ideas where the clusterer finds two
  groups. Make two nodes; each keeps the old name as the head of its own name (this keeps
  `resolve_scope` working).
- Depth: part, sub-part, question, helper question. A fifth level is refused. The mapper opens a
  new tree whose root links back (`subtree_of`).
- Promotion: reuse `promote_win(nodes, cand_id, cluster_name, hypothesis, change)`. It makes a
  `win_<id>` branch with `origin: "offtree"`. Proposed: attach under the nearest existing part when
  similarity is at least 0.6, instead of under root.
- Quiet: no win and no new result in 3 rounds after at least 4 tested ideas, or no sketch at all
  in 3 rounds. Lowered: `priority` times 0.5 (floor 0.1), `status:"lowered"`. It still gets one
  context every 3 rounds. A new win, a vote or a human comment raises it. Nothing is deleted.

### Recorded and to add

Today `problem_tree.json` holds nodes (id, name, parent, frame, assumptions, boundary, directions,
stats per direction, assumptions_added) and `inward_share`. The writer also adds `off_tree_share`
and `origins`, but the sample run's file predates that. Add per node: `rev`, `created_round`,
`origin`, `priority`, `status`, `aliases`, `results[]`, `facts_status`. Add top level: `version`,
`round`, `mode`.

### Versioning

```
 runs/<run>/tree/
   problem_tree.json        current
   round_01.json ...        full snapshot after each round
   tree_changes.jsonl       one line per op: {round, op, node, by, why}
   CHANGES_round_NN.md      readable diff for people
 ops: add | merge | split | lower | raise | promote | fact_disputed | fact_fixed
```

### Knobs

| Knob | Default | Profile key | CLI / control.json | Effect |
|---|---|---|---|---|
| off-map share | 0.4 (moves within 0.2 to 0.6) | none | `--off-tree-share` | share of contexts without a branch |
| skip a part | empty | none | control.json `skip_nodes` | part gets no contexts |
| merge threshold | 0.85 | `tree_merge_sim` (proposed) | proposed `--merge-sim` | lower merges more |
| crowd limit | 8 children / 12 ideas | `tree_crowd` (proposed) | proposed `--crowd` | when to split |
| max depth | 4 | `tree_depth` (proposed) | proposed | deeper opens a new tree |
| quiet rounds | 3 | `quiet_rounds` (proposed) | proposed `--quiet-rounds` | rounds before lowering |
| lowered factor | 0.5, floor 0.1 | `lower_factor` (proposed) | proposed | size of the priority cut |
| failure children | on | none | proposed `--no-fail-children` | child question per failure |

## 2. People

### Data model

```
  Problem 1---* Branch 1---* Fact
                  |
                  *---* Idea 1---* Result

  Comment, Vote, Flag all point at a target (branch, fact or idea).
  Every row has: id, author (person | agent:role), created_at, round, rev.

  Branch:  id, parent, name, origin(map|off|human), priority, status
  Fact:    id, branch, text, source, status(ok|disputed|remeasured|wrong)
  Idea:    id, branch, text, status(open|built|tested|dropped|known)
  Result:  idea, numbers, ref, status, round
  Comment: id, target, text, kind(evidence|question|objection)
  Vote:    id, idea, person, value(+1|-1), outcome(hit|miss|open)
  Flag:    id, idea, person, claim("known"), link, scout_verdict
```

Rows are never overwritten; an edit is a new `rev`. Agents write with `author = agent:<role>`.

### The four actions

| Action | Effect on the next round |
|---|---|
| Add problem or branch | Marked `origin:"human"`. Gets its own contexts next round, like an owner seed. |
| Comment | Critics and the justifier receive the comments on their target as evidence, with the author named. A comment that disputes a fact sets it "disputed". |
| Vote | Adds to idea priority, bounded: shift = clamp(0.1 x net votes, -0.3, +0.3). One vote per person per idea. |
| Flag prior art | The idea goes to the prior-art scout before building. If confirmed, status "known"; the flag is kept. |

A disputed fact is re-measured (FACTS, part 01) before any agent may use it. Until then inventors
see it marked "disputed".

### Tests decide

A voted idea that fails its test is dropped. Its votes get `outcome:"miss"`, shown beside the voter's
name. A voted idea that wins gets "hit". Hit rates are for people to read; in the first version they do
not change vote weight.

### Conflicting people

Votes sum, so opposite votes cancel. Comments are never merged: the justifier sees both sides and
must answer both. Two people disputing a fact are settled by one re-measurement, and both see the
number. Nobody deletes another person's comment; only an owner can hide one.

### What control.json supports today

`note` (every agent reads it), `skip_nodes`, `exclude_clusters`, `pause`, `stop_after_stage`,
`budget_add`, `aux_budget_add`, `k_impl`, `rounds_max`, `longshot_share`, `leap_share`. Changes are
logged in `control_log.jsonl`. Owner seeds (`--seeds-file`, default `memory/owner_seeds.json`, a list
of `{part, text}`) give one context each, in round 1 only. Missing today: votes, comments per idea,
fact disputes, flags, more than one person, adding a branch after round 1.

### Knobs

| Knob | Default | Profile key | CLI / control.json | Effect |
|---|---|---|---|---|
| vote step | 0.1 per net vote | `vote_step` (proposed) | proposed control.json `vote_step` | strength of a vote |
| vote cap | +-0.3 | `vote_cap` (proposed) | proposed | largest priority shift |
| human branch contexts | 2 per branch | `human_ctx` (proposed) | proposed `--human-ctx` | contexts per human branch |
| re-measure disputed facts | on | none | proposed `--no-remeasure` | block use until measured |
| opinion weight, Mode 3 | 0.25 of panel | `opinion_weight` (proposed) | proposed | people vs blind judges |
| owner seeds | file | none | `--seeds-file` | seeds in round 1 |
| skip a part | empty | none | `skip_nodes` | exclude a part |

## Worked examples

Language model (Mode 1). Round 2. Idea "per-token output scale" passes rung 2 with learn_z -2.1: it is
written under "Inputs and outputs" as a win, ref baseline, origin tree. Another idea fails rung 1 (shape
error): child question "failed to build because the head is tied; can a scale live outside the tied
matrix?". A person disputes "row norm encodes frequency (unmeasured)"; it is re-measured first. A
4-vote idea loses its test: dropped, 4 misses recorded. Another person adds branch "data order".

Bin packing (Mode 1, cheap checks). An off-map "blank" idea using the item-size histogram wins
(fewer bins). `promote_win` makes `win_xxxx`; the mapper attaches it under "use of item statistics".
"Tie-breaking" has no win in 3 rounds after 5 tests: lowered to 0.5. A person flags "this is Best
Fit"; the scout agrees; status "known", no build.

Mode 3, "design a fair review process for a hackathon". No check; blind judges score each design on
fairness, effort and clarity. Votes enter as extra judges at 0.25 of panel weight. A design the panel
scores low but people like is marked "split" and kept. A judge's complaint ("reviewers know the team
name") becomes a child question. A person adds branch "conflicts of interest". Two "rubric" nodes merge.

## Open decisions

- Shared space: web app, shared document, or database. Recommend a small database (SQLite behind one writer service) with a thin web page on top. A document cannot enforce the data model; a full web app is too much for version one.
- Identity: names only, or accounts? Recommend named logins, no anonymity, so hit rates mean something.
- Should hit rates ever change vote weight? Recommend not before 20 resolved votes per person.
- Mode 2: when the best so far changes, re-test old wins or only re-label? Recommend re-label, and re-test the top three.
- Mode 3 opinion weight: fixed 0.25, or by agreement with the panel? Recommend fixed at first.
- Who may hide a comment, and who may reopen a dropped idea?
- The thresholds (0.85, 8/12, 3 rounds) are guesses. Set them after one real multi-round run.
