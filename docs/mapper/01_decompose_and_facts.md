# Mapper 01: SPLIT and FACTS

Scope: parts (1) SPLIT and (2) FACTS of the mapper. QUESTIONS, RANK AND LINK, MAINTENANCE and PEOPLE are in the sibling documents and are only named here.

Status words: "built" means it is in `nano/tree.py` or a profile today. "proposed" means new.

## The three modes

| Mode | What exists | SPLIT does | FACTS does |
|---|---|---|---|
| 1. Baseline and check | artifact plus objective check (language model, bin packing) | splits the artifact's code and behaviour into parts, with code boundaries | attaches measurements of the baseline |
| 2. Check, no baseline | check only; the team writes first artifacts to an interface the profile gives | splits the interface and the problem, boundaries name interface pieces; re-split after the first artifacts exist | starts empty; the first scores of the first artifacts become facts; best so far is the reference |
| 3. No objective check | a question, hypothesis or plan | splits into components, steps or claims; no code boundary | holds what is known: documents, notes, prior results; measurements may be absent; judges and people replace the verifier |

## 1. SPLIT

### What it does

SPLIT turns the problem into 6 to 9 parts. Each part is a node.

```
  goal + profile + (artifact or brief) + facts text
                      |
                      v
        +-------------+--------------+
        | profile has a hand-written |--no--> planner call (model)
        | tree and no re-plan asked? |           |
        +-------------+--------------+           v
                      | yes               parse_planner
                      v                          |
              profile["tree"]  <-----fallback----+ (fewer than 4 nodes)
                      |                          |
                      +------------+-------------+
                                   v
                    root + parts + cross-part node
```

### Node schema (built)

| Field | Meaning |
|---|---|
| id | short lowercase id, at most 16 characters |
| name | at most 60 characters; the planner is asked to start it with the default part's name and a colon (secondary scope match) |
| refines | the default part id this node refines or splits, or "new"; `--only-nodes` resolves through it first (default trees: their own id) |
| parent | "root" for parts |
| frame | one or two sentences on how this part works today (max 400 characters) |
| assumptions | 3 to 5 choices a different design could remove (max 160 characters each) |
| boundary | what a change may touch (max 200 characters) |
| directions | `["inward","outward"]`, or `["upward"]` for the root |

The root carries the goal. A cross-part node (id `recipe`) holds changes that need two parts. `parse_planner` copies both from the profile tree.

### Lenses

A lens is one sentence that says how to cut the problem. The profile supplies `lenses`, a dict, and `parts` is required. The default set is the five that both profiles use: `parts`, `dataflow`, `dynamics`, `bottlenecks`, `failures`. A profile may add its own, for example `stakeholders` for a design question. The planner prompt says "Draw the map through this lens".

### How many parts

6 to 9 in the prompt. The parser rejects fewer than 4. Fewer than 6 hides weak spots. More than 9 spreads the inventors too thin, because `split_select` shares slots round robin across parts.

### Planner or default tree

Use the hand-written tree when the profile is new, when you want a stable baseline for comparison, or when a run is cheap. Use the planner when the profile gives a lens and an artifact or brief, and the facts text exists. Always keep the hand-written tree as the fallback if parsing fails.

### Re-planning

Proposed. A new lens is tried each round. The old tree is not replaced. The new parts are merged by name: a part whose name starts like an existing one reuses its id, so results and facts stay attached. A part that is new is added. MAINTENANCE decides what is lowered or promoted.

### Mode 3 parts

With no code, a part is a component of a design, a step of a process, or a claim of an argument. The boundary field becomes "what this part is allowed to change" in plain words, for example "the scoring rules, not the prize list". `artifact` is replaced by a brief (proposed key `brief`).

## 2. FACTS

### Rules

1. Every fact has a source. A fact without one is rejected, not stored.
2. A fact attaches to the part it informs. A fact that fits no part goes to the `unexplained` branch (proposed id `unexplained`, a sibling of the parts).
3. A fact can be disputed by an agent or a person. A disputed fact is marked, shown with the mark, and queued for re-measurement if a measurement exists.

### Fact record (proposed)

| Field | Meaning |
|---|---|
| id | stable id |
| text | one plain sentence with the numbers |
| source | one of: `diagnostics`, `scorer`, `document`, `human`, `agent`, `result` |
| ref | file, command, seed list, URL or person |
| part | part id or `unexplained` |
| status | `measured`, `reported`, `disputed`, `remeasured` |
| n_seeds, z | for measured facts; the noise firewall in `nano/anomaly.py` already gives these |

```
  sources                         attach                 tree
  +--------------------+     +---------------+     +------------------+
  | diagnostics hook   |---->|               |---->| part A: facts    |
  | scorer metrics     |---->| match fact to |---->| part B: facts    |
  | documents          |---->| part by name  |     | unexplained      |
  | human notes        |---->| or cell       |---->|                  |
  +--------------------+     +---------------+     +------------------+
                                    ^                        |
                                    |   disputed             |
                                    +--- re-measure <--------+
```

### Where measurements come from

| Source | Built today | How it reaches the mapper |
|---|---|---|
| Diagnostics hook `"module:function"` | language model: `nano.diagnose:text` returns the baseline's `diagnostics.md`, capped at 6000 characters | passed as `diagnostics` to `planner_prompt` and `tree_text` |
| Anomalies | `nano.anomaly.compute`: needs 2 seeds or more, same sign, z at least 2.0, FDR 0.10, at most 5 rows, sometimes a private sham row | rows are facts with `z` and `n_seeds` |
| Scorer metrics | `score`, `cost`, `n` from `metrics.json` (bin packing) | proposed: turned into facts by a generic hook |
| Documents | `docs.digest`, `docs.reference` | proposed: each paragraph a `document` fact with its path |
| Human notes | none yet | proposed, see PEOPLE |

### Attaching a fact

Two steps. First, if the fact names a diagnostic cell, the cell-to-part table (proposed profile key `fact_map`) places it. Second, otherwise a cheap model call matches the fact text against part names and frames and answers a part id or `unexplained`. The first step is exact and the second is a fallback.

### Disputed facts

A dispute stores who disputed and why. The fact keeps its text. The mapper prompts show `[DISPUTED: reason]`. If the profile has a checker, the measurement is repeated on new seeds and the status becomes `remeasured`. The `doubt` card already asks inventors to find a wrong fact; its output feeds the dispute list.

### No measurements

| Case | Behaviour |
|---|---|
| Mode 2, before first artifacts | the facts text is empty; the planner works from the goal and the interface; the profile's `diagnostics` returns "" (as `diagnose.text` does for a profile without diagnostics) |
| Mode 2, after first artifacts | scores of the artifacts become `scorer` facts; the best so far is the reference |
| Mode 3 | facts are known statements with sources; a missing measurement is shown as "not measured", never invented |

## 3. Configuration

### SPLIT

| Knob | Default | Key or flag | Effect |
|---|---|---|---|
| lens | `parts` | `lenses` (profile), lens name arg to `planner_prompt` | changes how the problem is cut |
| lens set | five lenses | `lenses` | add or remove views |
| default tree | profile tree | `tree` | fallback and fixed reference |
| part count | 6 to 9 | proposed `split_parts` | range in the planner prompt |
| minimum accepted | 4 | proposed `split_min` | below this the default tree is used |
| planner use | on | proposed `--no-planner` | off means default tree only |
| planner hint | boundary wording | `vocab.planner_hint` | tells the planner what a boundary names |
| re-plan lens order | none | proposed `replan_lenses` | lens per round |
| brief | none | proposed `brief` | stands in for the artifact in Mode 3 |

### FACTS

| Knob | Default | Key or flag | Effect |
|---|---|---|---|
| diagnostics hook | `""` or `nano.diagnose:text` | `diagnostics` | where measured text comes from |
| cap | 6000 characters | argument of `text` | limits prompt size |
| anomaly floor | z 2.0, FDR 0.10, 5 rows | constants in `anomaly.py` | stricter or looser anomalies |
| sham share | 0.1 | `sham_share` | how often a fake anomaly tests the agents |
| fact map | none | proposed `fact_map` | cell to part table |
| doc sources | digest and reference | `docs` | documents turned into facts |
| re-measure seeds | profile `min_seeds` | `score.min_seeds` | seeds for a disputed fact |
| source required | on | proposed, not switchable | rule 1 above |

## 4. Worked examples

### Language model (Mode 1)

Lens `parts`, planner on. The diagnostics hook returns the table of loss by position, by token frequency and per-layer norms. The planner returns nine parts such as "Sequence mixing: ..." and keeps the default names. A fact "loss on the rarest 9,000-plus tokens is above ln V, z 3.1 on 3 seeds" names the cell `rare`, so it attaches to `io`. A fact "gradient norms differ by 40 times across layers" has no part that owns it, so it goes to `unexplained` until a part or a cross-part node claims it.

### Bin packing (Mode 1, no diagnostics)

The profile sets `diagnostics: ""`, so the planner runs on the goal and `baseline.py` alone. The hand-written tree has 5 parts plus `recipe`. Facts come only from the scorer: "first fit scores 1.07 bins over lower bound on the quick level, 3 seeds, time per item 0.4 ms". They attach to `choice`. A proposed per-size-class breakdown hook would add facts to `stats` and `open`. Until then, the `unexplained` branch is empty and that is honest.

### Hackathon review process (Mode 3)

Brief: "design a fair review process for a hackathon". Lens `stakeholders` (proposed): judges, teams, organisers, time, scoring, appeals. Six parts, boundaries in plain words ("the scoring rubric, not the prize list"). Facts: "last year 3 judges scored 40 projects in 2 hours" (source: organiser note), "scores from different judges differed by 2 points on average" (source: document). The second attaches to scoring. A fact "judges knew team names" fits no part, so it goes to `unexplained`, which prompts a new part on bias. A person disputes the first fact; it shows as disputed and nothing is re-measured because no check exists. A judge panel reviews it instead.

## 5. Open decisions

1. Fact storage: file next to the tree, or the shared space database.
2. Who matches a fact to a part: a rule table, a model call, or both with a person able to override.
3. Whether the part count range should depend on the artifact size.
4. Whether re-planning replaces or only extends the part list.
5. In Mode 2, what the interface is when the profile gives none: ask the profile to supply one, or let the mapper propose it.
6. In Mode 3, how a panel verdict on a disputed fact is stored: as a new fact or as a status change.
7. Whether the sham fact test applies to Modes 2 and 3, where measurements are few.
