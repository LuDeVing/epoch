# agent-long-tasks_open_questions.txt

_Shared by luka on 2026-10-18T01:32; part: the whole problem; kind: note; source: agent-long-tasks_open_questions.txt._

Shared when describing the problem: Harness fixes for long tasks

## File

- agent-long-tasks_open_questions.txt (572 bytes, 6 lines), kept as files/Mudy9a5hQa4o-agent-long-tasks_open_questions.txt

## Readable start of the file

```
Does pinning the task text alone remove most "lost the goal" failures, or do those runs drift for another reason?
Is a loop best broken by rule (same command twice with the same output means stop and rethink) or by asking for a prediction first?
Should verification be a harness step the agent cannot skip, and what does it cost in runs that would have passed anyway?
Is a notes file better than a summary, given that summaries dropped the task text?
Which of the changes combine, and which cancel out?
Which failures are the model's limit, where no harness change helps?

```
