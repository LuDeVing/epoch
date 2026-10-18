# What the team found: harness fixes for long agent tasks

Run: small preset, 1 round, Fable inventing, Opus judging, started from the folder `examples/agent-long-tasks`
on 2026-10-18 (space `agent-long-tasks`, batch space-small-1018-053607). About 25 minutes, 94 model calls,
445k of the 600k inventing budget.

The folder describes a coding agent that passes 78 percent of short tasks and 31 percent of long ones, with
40 failed runs read by hand, a synthetic run sample, three changes already tried, and a measurement plan.
The team had no harness to run, so the output is ranked proposals with a test each, not a measured result.

## The funnel

| stage | count |
|---|---|
| map | 8 parts, 25 sub-parts (two-level map) |
| ideas | 50, on the 7 highest-priority sub-parts |
| idea groups | 7 islands |
| ideas taken to the critics | 12, three levels of critique each |
| objections raised | 60, 26 of them marked high |
| answers by the ideas' authors | 51 |
| builds (written proposals) | 2 |
| judged by | a blind panel of three Opus judges, people's votes at a bounded weight |

## The winner: pin the task in the system prompt

Panel score 6.7 of 10 (judges 6.5, 6.8, 6.8). Preferred over the other build.

The claim: move the task text out of the first user message into a labelled TASK block at the end of the
system prompt. Oldest-first trimming and the every-20-steps summariser can only touch history, so the goal
is present at every step by construction. Re-run the summariser with one added line: summarise progress only,
do not restate the task.

Why the team believes it, from the folder's own facts:
- "Lost the goal" is the largest failure kind, 11 of 40 read runs.
- In 9 of those 11 the task text was no longer in the context window.
- The harness trims the oldest messages first once the window passes 100k, and the task is the oldest message.
  So the harness deletes the goal in most of those runs. The model is not forgetting; it is being blinded.
- Passing and failing runs look the same for 10 steps and diverge after step 25, about where a 65k-token
  run approaches the trim threshold.
- The summariser that was tried shortened or dropped the task in 6 of 10 summaries, which is why it hurt
  "lost the goal" while helping "stale context".
- Models use the start of a long context best (Lost in the Middle), and the system prompt is the start for
  the whole run.

Predicted effect: pinning alone +5 to +8 points on the long-task pass rate for 2 to 5 percent more cost;
pinning plus the re-run summariser +8 to +12 points for 0 to 5 percent. Zero effect predicted on short tasks,
which never reach the trim threshold; the study checks that directly.

The test it proposes is the folder's own measurement plan: 48 long tasks, seeds 1 to 3, pass rate, pass^3,
tokens, wall time, failure kinds on a 20-run read sample, plus one new harness log field: "task text present
at the end of the run", so the mechanism can be audited and not just believed.

Weak points the proposal states itself:
- Presence is not influence. 2 of the 11 lost-the-goal runs still had the task in view. If "lost the goal"
  stays near 11 of 40 while the log shows the task present in every run, the mechanism was wrong.
- A task in the system prompt may be read as a standing rule rather than the specific job.
- The system prompt is no longer the same across runs, so provider-side prompt caching loses its hit rate.
- The summariser may still write a conflicting shortened goal; the added line reduces this, it does not
  guarantee it.

## The runner-up: a restatement handshake

Ask the agent to restate the goal at every trim event and every 15 steps. Built and judged, not preferred:
it keeps the goal in the model's own words, which is exactly what the summariser did when it shortened the
task, and it costs a call each time.

## What the critics caught, and what is worth checking

- Prompt caching changes the cost story. Several ideas claimed "cost flat". A critic pointed out that
  anything rewritten near the front of the context invalidates the cached prefix, so every reminder step is
  billed in full. Any harness change that edits early messages should be costed in dollars, not tokens.
- The trimmer story is unmeasured. Nobody logs when the trimmer fires. "The trimmer removes the task before
  the summariser sees it" is a plausible story, not a fact. One log flag per run settles it, and the winner
  adds that flag.
- The noise floor cuts most small ideas. A gain of 2 to 4 points is below the seed-to-seed spread of about 4
  points on 48 long tasks. The team applied the folder's own keep rule (+6 points or more) against its own
  ideas, and several were dropped on that alone.
- A loop detector needs offline validation first. One idea proposed replaying the 40 read runs through a
  "same command, same output, stop and rethink" rule before touching the live harness, to measure false
  positives on runs that would have passed.
- Token-triggered compaction fixes when the summariser fires, not what it keeps. Firing it earlier with an
  unconstrained summariser still drops the task.

## What to do with it

Run the winner's test on the real suite. It is cheap: one harness change, one prompt line, one log field,
144 runs. If "task text present at end" is true in every run and "lost the goal" does not fall, the
diagnosis was wrong and the next suspect is the summariser's own wording.

Where to look on the page: Results (the two proposals with per-criterion scores and Export), Arguments
(every objection and answer), Feed (the team's three proposed next questions for a second run), Knowledge
(87 lines of facts kept for the next run), and the run files (REPORT.md with the funnel and cost).
