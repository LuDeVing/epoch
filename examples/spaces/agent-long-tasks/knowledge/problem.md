# Harness fixes for long tasks

_Described on 2026-10-18 05:36._

## Goal

Find which changes to the harness, not the model, raise the pass rate of the coding agent on long tasks (40 or more tool calls), and by how much. Long tasks pass 31 percent of the time against 78 percent for short ones, and the same task often passes on one run and fails on the next. The team wants a ranked list of harness changes, each with a predicted effect on long-task pass rate and its cost, the failure kind it addresses, the mechanism, and a test. The answer should also say honestly which failures cannot be fixed without a model change. Today only a retry from scratch is kept, and it lifts the pair of runs to 44 percent but doubles the cost of a failed task. Situation: An LLM coding agent with read_file, edit_file, run_shell and search tools runs on an internal suite of 120 repository tasks, 48 of them long. One person read 40 failed long runs by hand and sorted them into six failure kinds. Three changes were tried: raising the step cap to 100, retrying once from scratch, and summarising every 20 steps. Only the retry was kept. The folder holds the taxonomy notes, the harness description, the measurement plan, the tried-changes list, literature notes (ReAct, Reflexion, SWE-agent, Lost in the Middle, tau-bench), open questions, and a 30-run sample CSV that is synthetic, not real data. Scope: In: harness changes (prompt, tools, context handling, memory, retries, step cap, verification) judged on the 48 long tasks of the 120-task suite; out: any change to the model, fine-tuning, or a bigger model. Open questions: Does pinning the task text alone remove most 'lost the goal' failures, or do those runs drift for another reason?; Is a loop best broken by a rule (same command twice with the same output means stop and rethink) or by asking for a prediction first?; Should verification be a harness step the agent cannot skip, and what does it cost in runs that would have passed anyway?; Is a notes file better than a summary, given that summaries dropped the task text?; Which changes combine and which cancel out (for example, notes file plus pinning plus summaries)?; Which failures are the model's limit, where no harness change helps (guess: part of gave up early and tool misuse)? Situation: An LLM coding agent with read_file, edit_file, run_shell and search tools runs on an internal suite of 120 repository tasks, 48 of them long. One person read 40 failed long runs by hand and sorted them into six failure kinds. Three changes were tried: raising the step cap to 100, retrying once from scratch, and summarising every 20 steps. Only the retry was kept. The folder holds the taxonomy notes, the harness description, the measurement plan, the tried-changes list, literature notes (ReAct, Reflexion, SWE-agent, Lost in the Middle, tau-bench), open questions, and a 30-run sample CSV that is synthetic, not real data. Scope: In: harness changes (prompt, tools, context handling, memory, retries, step cap, verification) judged on the 48 long tasks of the 120-task suite; out: any change to the model, fine-tuning, or a bigger model. Open questions: Does pinning the task text alone remove most 'lost the goal' failures, or do those runs drift for another reason?; Is a loop best broken by a rule (same command twice with the same output means stop and rethink) or by asking for a prediction first?; Should verification be a harness step the agent cannot skip, and what does it cost in runs that would have passed anyway?; Is a notes file better than a summary, given that summaries dropped the task text?; Which changes combine and which cancel out (for example, notes file plus pinning plus summaries)?; Which failures are the model's limit, where no harness change helps (guess: part of gave up early and tool misuse)?

## Situation

An LLM coding agent with read_file, edit_file, run_shell and search tools runs on an internal suite of 120 repository tasks, 48 of them long. One person read 40 failed long runs by hand and sorted them into six failure kinds. Three changes were tried: raising the step cap to 100, retrying once from scratch, and summarising every 20 steps. Only the retry was kept. The folder holds the taxonomy notes, the harness description, the measurement plan, the tried-changes list, literature notes (ReAct, Reflexion, SWE-agent, Lost in the Middle, tau-bench), open questions, and a 30-run sample CSV that is synthetic, not real data.

## What a good answer looks like

- **Ranked list**: The answer gives harness changes in ranked order, each with a predicted long-task pass-rate gain and a token cost per run.
- **Failure link**: Each change names the failure kind from the 40-run taxonomy it targets and the mechanism by which it helps, tied to counts or observations in the files.
- **Testable**: Each change has a test that fits the measurement plan: 48 long tasks, seeds 1-3, with pass rate, pass^3, tokens, and failure kinds.
- **Keep rule**: Predicted results are judged against the keep rule: at least +6 points on long tasks, cost rise at most 20 percent, no drop on short tasks.
- **Model limits**: The answer separates failures a harness change can fix from those that likely need a better model, with reasons.
- **Fits budget**: The proposed study order (cheap screen on 12 tasks, then full 48) stays within about 2,500 runs and about 15 full measurements.

## Limits

- The model is fixed: no fine-tuning, no retraining, no bigger model.
- Allowed changes are the system prompt, tools and tool descriptions, context trimming or summarising, memory between steps, retries and checkpoints, step cap, and how the agent is told to verify.
- Every change must be measurable on the 120-task suite with the same seeds.
- A change that doubles cost per task is out, even if it passes more.
- Keep rule: long-task pass up 6 points or more, cost up at most 20 percent, short-task pass not lower.
- Study budget is 2,500 runs in total, about 15 full measurements, with a 12-task screen first.
- The agent must not see or change the hidden tests.
- The trajectories CSV is synthetic and must not be treated as real evidence.

## Parts

- task text pinning
- loop breaking
- file freshness
- verification step
- notes and memory
- retry and checkpoint
- step cap and giving up
- measurement and combining

## Field and scope

- Field: LLM agent harness
- Scope: In: harness changes (prompt, tools, context handling, memory, retries, step cap, verification) judged on the 48 long tasks of the 120-task suite; out: any change to the model, fine-tuning, or a bigger model.

## Material shared with the team

- agent-long-tasks_failure_taxonomy_notes.md
- agent-long-tasks_harness_today.md
- agent-long-tasks_measurement_plan.md
- agent-long-tasks_open_questions.txt
- agent-long-tasks_problem_brief.md
- agent-long-tasks_reading_notes_agents.md
- agent-long-tasks_trajectories_sample.csv
- agent-long-tasks_what_we_tried.md
