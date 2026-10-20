# Verdict on the selection critique (2026-10-17)

Critique: stacked quotas (direction share, per-part round robin, novelty quota, long-shot lane) override the
measured score, so winners go unbuilt; fix by ranking the pool on measurement and quick-testing the top twenty.

## Decision: no code change now

1. **Not confirmed by data.** No real run has built candidates through the loop's own selection: arch-2 was an
   idea-only run (built 0) and the winning ideas were built by hand; nano-1 and nano-fable-1 predate cluster
   scoring. The one data point (the delay line came from a sketch the automatic selection had not picked)
   was found by a human pass, which the design allows for.
2. **The design is standard practice** (see 01_selection.md): the cheap-then-expensive ladder is successive
   halving; the random long-shot lane is the late-bloomer hedge; structural diversity (islands, cells) is what
   FunSearch and AlphaEvolve do. "Rank by score only" is not what the sources recommend.
3. **One tunable, not a redesign:** quotas take most of the 10-19 build slots instead of a small reserve. The
   sources point to about one fifth reserved, the rest by score, and a within-part cap instead of a round robin.
4. "Quick-test the top twenty" needs those twenty built first; that is the build-cost problem, which the owner
   dropped (no cheaper model for building or testing).

## Zero-cost measurements for the next real run

- Log the score rank of every winner (cluster score order vs measured gain).
- Rank correlation of 45-step, 240-step and long-run gains on built candidates.
These two numbers decide whether the quota share should move.
