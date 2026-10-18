# agent-long-tasks_measurement_plan.md

_Shared by luka on 2026-10-18T01:32; part: the whole problem; kind: note; source: agent-long-tasks_measurement_plan.md._

Shared when describing the problem: Harness fixes for long tasks

## File

- agent-long-tasks_measurement_plan.md (1087 bytes, 20 lines), kept as files/BZ1sXdkTruap-agent-long-tasks_measurement_plan.md

## Readable start of the file

```
# How a harness change is measured

Suite: 120 repository tasks, 48 of them long (40 or more tool calls in the median passing run). Each task has
hidden tests the harness runs after the agent stops; the agent cannot see or change them.

For every change, on the 48 long tasks:
- pass rate over 3 runs with seeds 1, 2, 3 (144 runs)
- pass^3: the share of tasks that pass on all three runs
- tokens per run and wall time per run
- failure kinds, by the taxonomy, on every failed run (a person reads a 20-run sample)

A change is kept when the long-task pass rate rises by 6 points or more (the seed-to-seed spread is about 4
points), cost per task does not rise by more than 20 percent, and the short-task pass rate does not fall.

Budget for this study: 2,500 runs in total, so about 15 changes can be measured in full. Cheap screening on
a 12-task subset first, then the full 48 for the promising ones.

Baseline numbers (3 seeds, current harness)
- long tasks: pass 31 percent, pass^3 12 percent, 65k tokens per run
- short tasks: pass 78 percent, pass^3 61 percent, 14k tokens per run

```
