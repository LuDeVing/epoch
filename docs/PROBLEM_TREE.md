# Problem tree: decomposition with inward and outward search

Status: v0.1, 2026-10-11. Implemented in `nano/tree.py` and wired into `nano/loop.py`.

## Why

Two kinds of creativity appear in the research (Boden; catalog GEN-12, REP-11, REP-13, REP-05):
exploratory, improving inside a frame, and transformational, replacing the frame. A loop that only
asks "how do we improve X" stays inside the paradigm it was handed. The problem tree makes both
directions explicit at every part of the problem, and keeps the verifier the same for both, so a
radical idea is judged on the same metric at the same budget as a tweak.

## The tree

A planner call decomposes the goal into 6 to 9 parts (fallback: a hand-written tree). For the nano
trainer the parts are: inputs and outputs, sequence mixing, per-token computation, state across
depth, optimization, data, objective, plus the root. Each node carries:

- `frame`: the current design of that part in one or two sentences
- `assumptions`: 3 to 5 design choices a different paradigm could remove
- `boundary`: the code a change at this node may touch
- `directions`: inward and outward for parts; upward for the root

## Directions

- Inward: assumptions are fixed; improve inside them.
- Outward: every sketch must remove or invert at least one assumption and say which.
- Upward (root only): alternative formulations of what is modeled or measured. Logged to
  `proposals_upward.jsonl` as proposals for a new verifier; not implemented, because they change
  what can be checked.

## Flow per round

1. Ideation: for every node and direction, `per_node` fresh contexts (default 1) write 5 to 8
   sketches: idea, mechanism, prediction, cheapest falsifying test. Cards cycle over seed word,
   comments stripped, plain, and the 2026 architecture digest; the node's assumption list is the
   transform material. Two upward contexts at the root.
2. Clustering: one blind call per node and direction groups sketches by mechanism (lexical
   fallback). Clusters carry node and direction.
3. Selection: `k` implementation slots split by `inward_share` (default 0.6), filled round-robin
   across nodes within each direction, so one part cannot take every slot and outward ideas are
   always tested. Within a node, the usual coverage-first rules: several distinct cards, departure
   cards, cheapest test; never cluster size or eloquence.
4. Implementation: one complete file per selected cluster, scoped to the node's boundary.
5. Verification: the same three cheap rungs, then the full three-seed training for the pool.
6. Later rounds: up to two revisions of near misses plus the next clusters, excluding clusters
   already implemented.

## Outputs

`problem_tree.json` (nodes with per-direction counts: sketches, clusters, implemented, checked),
`ideas.jsonl`, `idea_clusters.json`, `proposals_upward.jsonl`, and the usual candidate, verify,
pool and graph files. The dashboard shows the tree and the idea map live.

## Cost

Seven parts x two directions + two upward = 16 ideation contexts per round at `per_node` 1, plus
one clustering call per node-direction with 4+ sketches (about 14), one planner call, and the
implementation calls. Through the Claude Code CLI with Fable (about 50k overhead tokens per call)
a round is roughly 2 million tokens; through the API it is a fraction of that.

## Not yet

Recursion into sub-parts (depth 2), the lemma pool over smoke curves, and ledger-driven budget
shifts toward the nodes that produce verified wins. All three are designed in SYNTHESIS.md.
