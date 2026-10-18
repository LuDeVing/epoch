# agent-long-tasks_reading_notes_agents.md

_Shared by luka on 2026-10-18T01:32; part: the whole problem; kind: note; source: agent-long-tasks_reading_notes_agents.md._

Shared when describing the problem: Harness fixes for long tasks

## File

- agent-long-tasks_reading_notes_agents.md (1674 bytes, 25 lines), kept as files/sAt3ToYs9ztb-agent-long-tasks_reading_notes_agents.md

## Readable start of the file

```
# Reading notes: what is known about long-horizon agent failures

ReAct (Yao et al., 2022). Interleaving a written thought with each action helps the model keep track of what
it is doing. Their failure analysis names reasoning that drifts from the task and repeated actions as the
main failure kinds. Matches our "lost the goal" and "loop".

Reflexion (Shinn et al., 2023). After a failed attempt the model writes a short reflection on what went wrong,
kept in memory for the next attempt. Big gains on tasks with a clear pass or fail signal. Our retry from scratch
keeps nothing between attempts; a reflection would be cheap to add.

SWE-agent (Yang et al., 2024). The interface the agent works through matters as much as the prompt: a file
viewer that shows a window with line numbers, an edit command that checks syntax, and short tool outputs
raised the solve rate on SWE-bench. Their point: tool results that are long or noisy fill the context with
little information.

Lost in the Middle (Liu et al., 2023). Models use information at the start and end of a long context better
than information in the middle. Our task text starts at the beginning and is trimmed away; while it stays, it
sits in the best position, and then it is gone.

tau-bench (Yao et al., 2024). The same task run several times passes sometimes and fails other times; they
report pass^k, the chance that all k runs pass, which falls fast with k. Our 31 percent is one run; pass^3 is
what a user feels.

Common ground across these: the agent needs the goal, the current state of the world, and a check it cannot
fool, all kept close. Most harness fixes are ways of keeping one of the three in view.

```
