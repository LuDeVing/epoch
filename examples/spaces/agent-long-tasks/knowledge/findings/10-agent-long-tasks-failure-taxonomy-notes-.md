# agent-long-tasks_failure_taxonomy_notes.md

_Shared by luka on 2026-10-18T01:32; part: the whole problem; kind: note; source: agent-long-tasks_failure_taxonomy_notes.md._

Shared when describing the problem: Harness fixes for long tasks

## File

- agent-long-tasks_failure_taxonomy_notes.md (1730 bytes, 23 lines), kept as files/T2mzY6WND4Z1-agent-long-tasks_failure_taxonomy_notes.md

## Readable start of the file

```
# Reading 40 failed long-task runs by hand

One person read 40 failed runs (tasks with 40 or more tool calls) end to end. Each run was given one main
failure kind. Counts below. A run often shows two kinds; the first one that doomed the run is counted.

| kind | runs | what it looks like |
|---|---|---|
| lost the goal | 11 | after 30 or more steps the agent works on a sub-problem and never returns to the task; the final message claims success on the sub-problem |
| loop | 9 | the same edit and test cycle three or more times with the same error; no new information between tries |
| stale context | 7 | the agent reasons from a file version it read 20 steps earlier, after its own edit changed it |
| wrong verification | 6 | the agent runs a test that cannot fail (wrong path, skipped test, grep for a word) and stops |
| gave up early | 4 | the agent writes "this would need more investigation" and stops with steps and budget left |
| tool misuse | 3 | malformed edits, wrong working directory, shell quoting; recovered late or never |

Observations
- In 9 of the 11 "lost the goal" runs the original task text was no longer in the context window when the agent
  went astray. The harness trims the oldest messages first and the task text is the oldest message.
- The 9 loop runs averaged 2,400 tokens per cycle. The agent never stated what it expected the fix to change.
- Stale context runs all involved files longer than 300 lines that the agent had read in full once.
- "Wrong verification" runs ended with a confident summary. A person reading only the summary would have
  accepted 5 of the 6.
- Runs that passed and runs that failed used the same tools in the first 10 steps. The difference shows after
  step 25.

```
