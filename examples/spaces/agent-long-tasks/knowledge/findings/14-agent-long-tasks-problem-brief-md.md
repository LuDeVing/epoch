# agent-long-tasks_problem_brief.md

_Shared by luka on 2026-10-18T01:32; part: the whole problem; kind: note; source: agent-long-tasks_problem_brief.md._

Shared when describing the problem: Harness fixes for long tasks

## File

- agent-long-tasks_problem_brief.md (1729 bytes, 28 lines), kept as files/OzauaRqcs90n-agent-long-tasks_problem_brief.md

## Readable start of the file

```
# Why our coding agent fails on long tasks, and what to change in the harness

We run an LLM coding agent (tool calls: read, edit, run shell, search) on an internal suite of 120 repository
tasks. Short tasks (under 15 tool calls) pass 78 percent of the time. Tasks that need more than 40 tool calls
pass 31 percent of the time, and the same task passes on one run and fails on the next.

The question: which changes to the harness, not the model, raise the pass rate on the long tasks, and by how much?

Scope
- The model is fixed. No fine-tuning, no retraining, no bigger model.
- Changes allowed: the system prompt, the tool set and tool descriptions, how context is trimmed or summarised,
  memory between steps, retries and checkpoints, the step cap, and how the agent is told to verify its work.
- Every change must be measurable on the 120-task suite with the same seeds.
- A change that doubles cost per task is out, even if it passes more.

What a good answer looks like
- A ranked list of harness changes, each with a predicted effect on the long-task pass rate and its cost.
- For each change: the failure kind it addresses (see failure_taxonomy_notes.md), the mechanism, and a test.
- Honest about what cannot be fixed without the model changing.

Files in this folder
- failure_taxonomy_notes.md: what 40 failed runs looked like when a person read them.
- trajectories_sample.csv: 30 runs with steps, outcome and failure kind. SYNTHETIC: shaped like our logs, not real data.
- harness_today.md: how the harness works now.
- what_we_tried.md: three changes already tried and what happened.
- reading_notes_agents.md: notes from the literature.
- measurement_plan.md: how we will measure a change.
- open_questions.txt

```
