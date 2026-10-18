# agent-long-tasks_harness_today.md

_Shared by luka on 2026-10-18T01:32; part: the whole problem; kind: note; source: agent-long-tasks_harness_today.md._

Shared when describing the problem: Harness fixes for long tasks

## File

- agent-long-tasks_harness_today.md (973 bytes, 12 lines), kept as files/YOcqY0FRy6pl-agent-long-tasks_harness_today.md

## Readable start of the file

```
# The harness as it is now

- One system prompt (about 900 tokens): the role, the tools, "work until the task is done, then summarise".
- Tools: read_file (whole file or a line range), edit_file (search and replace), run_shell, search (grep).
- Step cap: 60 tool calls. At the cap the agent is asked for a final summary and the run ends.
- Context window: 128k tokens. When the conversation passes 100k, the oldest messages are dropped until it is
  under 80k. The task text is the first user message, so it is dropped first.
- No memory between runs. No notes file. The agent keeps nothing outside the conversation.
- No checkpoint: a run that fails is retried from scratch at most once (see what_we_tried.md).
- Verification is left to the agent. The prompt says "run the tests"; nothing checks that it did.
- Cost per long task today: about 65k tokens per run on average, 2 runs with the retry.
- Logs keep every tool call and result, so a run can be replayed and read.

```
