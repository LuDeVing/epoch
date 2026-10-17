# ARC-AGI-3 adapter: spec

Status: draft v0.1, 2026-10-11. Owner decision: ARC-AGI-3 is the test for Opus 5.5 (no published
score; Claude Opus 5 at 30.2 percent, humans at 100). This adds an interactive benchmark to the
harness without changing the loop of ARCHITECTURE.md section 4.

**Not built (checked 2026-10-17).** This is a spec only. `harness/arc3/` does not exist, there is no `arc3`
entry in `config.BENCHMARKS`, `score.is_correct` and `verify.run` know no such benchmark, and
`harness/think/dedup.py` has no `trace` rule: an unknown `dedup_rule` falls back to text hashing silently.
Every file and command below describes what would be built.

## What ARC-AGI-3 is (measured locally 2026-10-11)

- `pip install arc-agi` gives `arc_agi.Arcade()`; `arc.make(game_id)` downloads the game once and
  runs it LOCALLY (`LocalEnvironmentWrapper`). 25 environments are listed with an anonymous key.
  Register a key at three.arcprize.org for official scorecards.
- A game is a sequence of levels (ls20: 7). The agent sees a 64x64 int8 frame (about 16 colours),
  no instructions, and must discover the controls and the goal. Actions: ACTION1-5 (keyboard-like,
  per game subset), ACTION6 (click with x, y), ACTION7, RESET. Tags per game: keyboard, click,
  keyboard_click.
- `env.reset()` and `env.step(action[, data])` return `FrameDataRaw` with `frame` (list of
  64x64 layers), `state` (NOT_FINISHED | WIN | GAME_OVER), `levels_completed`, `win_levels`,
  `available_actions`. `arc.get_scorecard()` aggregates runs.
- The reference LLM agent in `arc-agi-3` templates sends the whole frame as numbers every step
  and allows 80 actions: roughly 10k tokens per step, up to 800k per game. Too expensive to be our
  baseline at scale; we keep its structure but compress observations.

## Mapping onto HTSA

| Loop step | ARC-2 (grid in, grid out) | ARC-3 (interactive) |
|---|---|---|
| item | task with demo pairs | game id; run from reset; score = levels completed / win levels |
| encode | restate, facts, checklist, defaults | scripted exploration (0 tokens): from reset, each available action once (clicks on a coarse grid), record frame diffs; one model call writes `problem.md`: controls hypothesis, goal hypothesis, objects, constraints; `private/defaults.json` = 5 first-guess strategies |
| candidate | python `transform(grid)` | a policy program `policy(obs, mem) -> (action, data, mem)` OR an action script (list of actions); both run locally |
| verifier | demo pairs (demo_match) | the environment: run the candidate from reset for <= K steps in a fresh env; `partial_score` = levels_completed / win_levels; verified iff all levels won; "progress" also tracks new levels and novel frames |
| feedback record | failing pair diffs | trace summary: actions taken, level reached, last 3 frame diffs (compact), termination cause, exception tail; <= 1.5k tokens |
| dedup rule | predicted test grid | trace signature: (levels_completed, hash of the action sequence) |
| probe / agreement | 3 plain calls, cluster by answer | none at P0 (no single "answer" to agree on); confidence = partial_score only; documented deviation, revisit at P1 |
| judge | blind score of candidate text | blind score of policy code plus its one-line stated hypothesis; p_raw steers nothing |
| plain arm | one CoT call | step-wise agent: one call per action with the compact observation, running notes, action cap A_max = 80, episode budget in tokens |
| best-of-N arm | N programs, pick by verifier | repeated plain episodes within the token budget; score = best episode (the environment is the verifier, so this is legitimate) |
| scaffold | cards -> judge -> verify -> revise -> reset | same loop; cards write policies or action scripts; revise gets the trace record; stagnation reset = fresh generators with new seeds and the base exploration summary |

## Observation compression (the cost lever)

`harness/arc3/env.py` renders a frame three ways, all script-computed:
1. `rle`: run-length encoded rows with one character per colour (about 1-2k tokens for a typical
   frame; worst case 4k). Always available.
2. `objects`: connected components per colour: {colour, bbox, size, count}, top 30 by size, plus
   background colour. About 300-600 tokens.
3. `diff`: cells changed since the previous frame as bboxes with before/after colours, plus
   "levels_completed" and "state". About 100-300 tokens.
The plain agent sends `objects + diff` every step and `rle` only on reset, on level change, and
every 10th step. Generators get the exploration summary (controls hypothesis plus the diffs each
action produced) and the reset frame as `rle`.

## Budget

- B per game = m x median plain-episode tokens on dev (m = 20 primary, as everywhere).
- Action caps: A_max = 80 per plain episode; K = 200 steps per candidate policy run; wall-clock
  cap 60 s per policy run (policies are pure python, no model calls inside).
- Best-of-N episodes stop when the next episode's expected cost exceeds the remaining budget.

## Metrics

- Primary: mean fraction of levels completed per game (0..1), paired across arms, cluster
  bootstrap over games. Secondary: games won; games with >= 1 level; actions to first level;
  realized tokens per game beside B. ARC Prize's weighted score is reported for reference only.
- Integrity: the policy run never sees anything but the environment; the model never receives
  the game source; `private/defaults.json` never routed; decision log per cycle; graph check 100%.

## Files

```
harness/arc3/__init__.py
harness/arc3/env.py          # Arcade/LocalEnvironment wrapper: reset, step, frame renderers (rle,
                             #   objects, diff), scripted exploration, safe policy runner (K steps,
                             #   timeout, exception capture), trace records
harness/arc3/plain_agent.py  # plain and bestofn_env arms (step-wise agent with compact observations)
harness/arc3/encode.py       # exploration + one model call -> problem.md, constraints.json, defaults
harness/arc3/verify.py       # run a policy or action script in a fresh env -> VerifyResult + feedback
harness/strategies/templates/*.arc3.txt   # seeded, low_prior, transform, formal (policy), revise
harness/tests/test_arc3.py   # uses a tiny fake environment class (no download) + mock backend
config.BENCHMARKS["arc3"]: {dedup_rule: "trace", verification_type: "env_levels",
                            revise_allowed: True, graded: True, cands_per_generator: 2, n0: 5}
data.py: items = the 25 game ids, splits dev-tune 10 / dev-ablate 7 / test 8 by seed 7
score.py: is_correct(item, answer) = answer["levels_completed"] == answer["win_levels"];
          partial = levels_completed / win_levels
```

## Build order

1. `env.py` with renderers and the safe policy runner; unit tests on a fake env and on ls20 locally.
2. `plain_agent.py` (plain + bestofn_env) and `data.py`/`score.py`/`config` entries; measure the
   plain episode cost on 3 games with Sonnet (headroom and budget).
3. `encode.py`, templates, `verify.py`; wire into think.py through the benchmark config (the driver
   is generic; arc3 modules are selected by `config.BENCHMARKS["arc3"]["module"]`).
4. Mock end-to-end test; then a 3-game pilot: plain vs bestofn_env vs scaffold with Sonnet.
5. Opus 5.5 run on the dev split once Sonnet shows the loop works.

## Risks

- Policies as code may be the wrong candidate shape for games needing long reactive play; the
  action-script shape is the fallback, and the revise card operates on traces either way.
- Clicking games (ACTION6) have a 64x64 target space; exploration samples a coarse 8x8 grid of
  clicks and refines around cells whose click changed the frame.
- Scores on local runs are not official; an API key and online scorecards are needed for any
  claim against the leaderboard.
