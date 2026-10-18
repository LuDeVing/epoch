# Facts

Numbered so a proposal can cite them, like [F3]. Each one names where it came from.

- **[F1]** Short tasks (under 15 tool calls) pass 78 percent; tasks over 40 tool calls pass 31 percent; the same task can pass and fail on different runs.  
  _source: problem_brief.md, opening paragraph_
- **[F2]** Baseline long tasks: pass 31 percent, pass^3 12 percent, 65k tokens per run. Short tasks: pass 78 percent, pass^3 61 percent, 14k tokens per run.  
  _source: measurement_plan.md, Baseline numbers_
- **[F3]** Of 40 failed long runs read by hand: lost the goal 11, loop 9, stale context 7, wrong verification 6, gave up early 4, tool misuse 3.  
  _source: failure_taxonomy_notes.md, table_
- **[F4]** In 9 of 11 'lost the goal' runs the task text was no longer in the context window; the harness trims oldest messages first and the task text is the oldest.  
  _source: failure_taxonomy_notes.md, Observations_
- **[F5]** The 9 loop runs averaged 2,400 tokens per cycle, and the agent never stated what it expected the fix to change.  
  _source: failure_taxonomy_notes.md, Observations_
- **[F6]** All stale context runs involved files longer than 300 lines that the agent had read in full once.  
  _source: failure_taxonomy_notes.md, Observations_
- **[F7]** A person reading only the summary would have accepted 5 of the 6 wrong-verification runs.  
  _source: failure_taxonomy_notes.md, Observations_
- **[F8]** Passing and failing runs used the same tools in the first 10 steps; the difference shows after step 25.  
  _source: failure_taxonomy_notes.md, Observations_
- **[F9]** Harness: system prompt of about 900 tokens, four tools, step cap of 60 tool calls, 128k window; when over 100k, oldest messages are dropped until under 80k.  
  _source: harness_today.md_
- **[F10]** No memory between runs, no notes file, no checkpoint; a failed run is retried from scratch at most once; verification is left to the agent and nothing checks it.  
  _source: harness_today.md_
- **[F11]** Cost per long task today is about 65k tokens per run, 2 runs with the retry.  
  _source: harness_today.md_
- **[F12]** Raising the step cap from 60 to 100 moved long-task pass from 31 to 33 percent and cost per task up 45 percent; loop runs just looped longer. Not kept.  
  _source: what_we_tried.md, change 1_
- **[F13]** Retry from scratch with a different seed raised the pair's long-task pass rate from 31 to 44 percent and doubles cost of a failed task. Kept.  
  _source: what_we_tried.md, change 2_
- **[F14]** Summarising every 20 steps moved pass from 31 to 34 percent; stale context failures fell but lost-the-goal failures rose; in 6 of 10 read summaries the task text was shortened or dropped. Not kept.  
  _source: what_we_tried.md, change 3_
- **[F15]** Untried: pinned task text, prediction before re-running a test, re-reading a file after editing, harness-run verification, scratch notes file.  
  _source: what_we_tried.md, What nobody has tried_
- **[F16]** Suite is 120 repository tasks, 48 long, with hidden tests run after the agent stops.  
  _source: measurement_plan.md, first paragraph_
- **[F17]** Measurement per change: pass rate over seeds 1, 2, 3 (144 runs), pass^3, tokens and wall time per run, and failure kinds on a 20-run sample.  
  _source: measurement_plan.md, list_
- **[F18]** A change is kept if long-task pass rises 6 points or more (seed spread about 4 points), cost per task rises at most 20 percent, and short-task pass does not fall.  
  _source: measurement_plan.md, keep rule_
- **[F19]** Study budget is 2,500 runs, about 15 full changes, with screening on a 12-task subset first.  
  _source: measurement_plan.md, Budget_
- **[F20]** ReAct names drifting reasoning and repeated actions as main failure kinds; Reflexion's written reflection after a failure is cheap to add to the retry.  
  _source: reading_notes_agents.md, ReAct and Reflexion_
- **[F21]** SWE-agent: a windowed file viewer, syntax-checked edits and short tool outputs raised solve rate; long noisy tool results fill the context.  
  _source: reading_notes_agents.md, SWE-agent_
- **[F22]** Lost in the Middle: models use the start and end of the context better than the middle; the task text sits at the start until it is trimmed away.  
  _source: reading_notes_agents.md, Lost in the Middle_
- **[F23]** The sample CSV has 30 runs on 15 tasks (two runs each) with steps, tokens, outcome, failure kind, task-text-in-context flag, repeated cycles, large files read, and verify step type. It is synthetic.  
  _source: trajectories_sample.csv, header and rows; problem_brief.md file list_
- **[F24]** In the sample CSV, every run marked verify_step 'fake' failed, and all fake-verify runs are labeled wrong verification.  
  _source: trajectories_sample.csv, verify_step column_

## Shared by people during the research

- **[F25]** agent-long-tasks_failure_taxonomy_notes.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_failure_taxonomy_notes.md_
- **[F26]** agent-long-tasks_harness_today.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_harness_today.md_
- **[F27]** agent-long-tasks_measurement_plan.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_measurement_plan.md_
- **[F28]** agent-long-tasks_open_questions.txt: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_open_questions.txt_
- **[F29]** agent-long-tasks_problem_brief.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_problem_brief.md_
- **[F30]** agent-long-tasks_reading_notes_agents.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_reading_notes_agents.md_
- **[F31]** agent-long-tasks_trajectories_sample.csv: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_trajectories_sample.csv_
- **[F32]** agent-long-tasks_what_we_tried.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:31, file agent-long-tasks_what_we_tried.md_
- **[F33]** agent-long-tasks_failure_taxonomy_notes.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_failure_taxonomy_notes.md_
- **[F34]** agent-long-tasks_harness_today.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_harness_today.md_
- **[F35]** agent-long-tasks_measurement_plan.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_measurement_plan.md_
- **[F36]** agent-long-tasks_open_questions.txt: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_open_questions.txt_
- **[F37]** agent-long-tasks_problem_brief.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_problem_brief.md_
- **[F38]** agent-long-tasks_reading_notes_agents.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_reading_notes_agents.md_
- **[F39]** agent-long-tasks_trajectories_sample.csv: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_trajectories_sample.csv_
- **[F40]** agent-long-tasks_what_we_tried.md: Shared when describing the problem: Harness fixes for long tasks  
  _by luka, 2026-10-18T01:32, file agent-long-tasks_what_we_tried.md_
