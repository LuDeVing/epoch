# The mapper: overview

The mapper is the agent that turns a problem into a problem tree, and keeps that tree honest across
rounds. It never invents. It organises facts, names weak spots, poses questions, ranks branches, and
records what happened. Inventors, critics, builders and testers work from the tree; people edit it.

This folder is the design for making the mapper configurable per problem. Read in order:

| File | Parts of the mapper | Status |
|---|---|---|
| `01_decompose_and_facts.md` | SPLIT (parts through a lens), FACTS (every measurement to a part, with a source) | design, partly built |
| `02_questions_rank_link.md` | QUESTIONS (does, weak spot, ask), RANK AND LINK (priority, contexts, slots, links) | design, partly built |
| `03_maintenance_and_people.md` | MAINTENANCE (write-back, child questions, merge, split, promote, lower), PEOPLE (shared space) | design, mostly proposed |

## The six parts in one drawing

```
  problem + profile            measurements / documents / notes
        |                                  |
        v                                  v
  [1 SPLIT] ---- parts ---------> [2 FACTS] ---- facts with sources
        |                                  |      (+ "unexplained" branch)
        +------------------+---------------+
                           v
                    [3 QUESTIONS]   does / weak spot / ask   (ask = a problem, never a solution)
                           |
                           v
                    [4 RANK AND LINK]   priority = unused capacity x evidence
                           |            -> idea contexts per part, build slots, links
                           v
              inventors -> critics -> builders -> testers -> results
                           |
                           v
                    [5 MAINTENANCE]   results written back, failures -> child questions,
                           |          off-map wins -> branches, quiet branches lowered,
                           |          merge / split, depth <= 4, versions per round
                           v
                    [6 PEOPLE]   add a problem or branch, dispute a fact, comment, vote, flag
                                 rule: people steer, tests decide
```

## Three modes, one mapper

| Mode | What exists | What changes for the mapper |
|---|---|---|
| 1. Baseline and check | an artifact to modify, an objective score | today's case; facts come from measurements of the baseline |
| 2. Check, no baseline | a scorer and an interface, nothing solved yet | parts come from the interface and the profile; first facts arrive after the first artifacts; the best so far is the reference and may change |
| 3. No objective check | a question, a design, a plan | parts are components, steps or claims; facts are what is known; evidence is weaker, so priority leans on critics and on people's votes with a bounded weight |

## Configuration at a glance

| Knob | Today | Where |
|---|---|---|
| lenses | five, language-model wording | profile `lenses` (built) |
| default tree | per profile | profile `tree` (built) |
| planner model on/off | on | `--plan-with-model` (built), `--no-planner` (proposed) |
| parts per tree | 6 to 9 | `split_parts` (proposed) |
| measurements source | `diagnostics` hook | profile `diagnostics` (built) |
| fact to part matching | none; facts are text | `fact_map` (proposed) |
| contexts per part | `per_node` | CLI (built) |
| inward share of slots | 0.6 | `--inward-share` (built) |
| off-map share | 0.4, moves 0.2 to 0.6 by yield | `--off-tree-share` (built) |
| directions | inward, outward, upward | node `directions` (built), profile-added (proposed) |
| helper questions | none from the mapper | `helpers_per_part` (proposed) |
| depth limit | none enforced | 4 (proposed) |
| merge, split, quiet thresholds | none | 0.85, 8 / 12, 3 rounds (proposed guesses) |
| human steering | skip parts, owner seeds | `control.json` (built) |
| people's votes, comments, flags | none | shared space (proposed) |

## Decisions for the owner

The three files end with their own open decisions. The ones that change the build the most:

1. **Where the shared space lives.** Recommendation from file 03: a small database with one writer
   service and a thin web page. A document cannot enforce the data model; a full app is too much for
   version one.
2. **Who matches facts to parts.** A rule table, a model call, or both with a person able to override.
3. **Whether the question lint blocks a plan or only repairs it.** Repair with one retry is the safer default.
4. **How much a vote weighs.** File 02 proposes a capped term; file 03 proposes a fixed 0.25 weight in
   Mode 3. Both are guesses until real voters use it.
5. **Mode 2 reference changes.** When the best artifact changes, re-label old results and re-test the top three.

## Build order

1. Mode 2 and Mode 3 in the loop (baseline optional; panel verdicts), since every part above depends on the mode.
2. Fact records with sources and the `unexplained` branch (file 01), the question lint (file 02).
3. Write-back, child questions, versions per round (file 03).
4. The shared space, with the four people actions wired to the next round.
