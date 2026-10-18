# agent-long-tasks_what_we_tried.md

_Shared by luka on 2026-10-18T01:32; part: the whole problem; kind: note; source: agent-long-tasks_what_we_tried.md._

Shared when describing the problem: Harness fixes for long tasks

## File

- agent-long-tasks_what_we_tried.md (1113 bytes, 21 lines), kept as files/vXvAvbklFx06-agent-long-tasks_what_we_tried.md

## Readable start of the file

```
# Three changes already tried

1. Raise the step cap from 60 to 100.
   Long-task pass rate 31 to 33 percent. Cost per task up 45 percent. The loop runs just looped longer.
   Not kept.

2. Retry a failed run from scratch once, with a different seed.
   Pass rate for the pair of runs 31 to 44 percent on long tasks. Doubles the cost of a failed task.
   Kept, as the current default. It shows the model can do these tasks; it does not do them reliably.

3. Summarise the conversation every 20 steps (the model writes a summary, old messages are replaced by it).
   Pass rate 31 to 34 percent. "Stale context" failures fell. "Lost the goal" failures rose: in 6 of 10 read
   summaries the task text was shortened or dropped by the summary itself.
   Not kept.

What nobody has tried
- Keeping the task text pinned so trimming never drops it.
- Making the agent write what it expects a change to do before it runs the test again.
- Re-reading a file after editing it, by rule.
- A verification step the harness runs, not the agent.
- A scratch notes file the agent is told to keep, with the plan and what is done.

```
