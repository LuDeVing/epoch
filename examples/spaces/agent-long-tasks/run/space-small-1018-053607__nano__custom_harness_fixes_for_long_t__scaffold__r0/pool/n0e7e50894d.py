CLAIM:
Put the task text in the system prompt at run start instead of the first user message, so neither oldest-first trimming nor the 20-step summariser can ever remove or shorten it. With the goal fixed in place, re-run the summariser from the third tried change unchanged. Predicted long-task pass: 31 to 39-43 percent, cost per run up 2 to 5 percent, short tasks unchanged.

FROM THE FACTS TO THE IDEA:
Long tasks pass 31 percent against 78 for short ones, and the same task flips between pass and fail across runs [F1, F2].
The largest failure kind in the 40 read runs is lost the goal, 11 of 40 [F3].
In 9 of those 11 runs the task text was no longer in the context window [F4].
The harness trims oldest messages first once the window passes 100k, and the task text is the oldest message [F9].
So the harness itself deletes the goal in most lost-the-goal runs; the model is not forgetting, it is being blinded.
Passing and failing runs look the same for 10 steps and diverge after step 25 [F8], which is about where a 65k-token run starts to approach the trim threshold.
Summarising every 20 steps helped stale context but hurt lost the goal: in 6 of 10 summaries the model shortened or dropped the task text [F14].
Both the trimmer and the summariser can only touch history. Anything in the system prompt is outside their reach.
Lost in the Middle says models use the start of the context well [F22]; the system prompt is the start, and stays the start for the whole run.
Pinned task text is on the untried list [F15].
So: flip the rule that the task is a user message. The harness writes the task into a labelled TASK block at the end of the system prompt, the history begins empty, and the system prompt is rebuilt per run from a fixed template plus the task.
Then re-run the ungated summariser from [F14] as is, with one line added to its prompt: "The task is in the system prompt; summarise progress only, do not restate the task." This stops a shortened copy competing with the pinned one.

FROM THE IDEA TO THE RESULT:
Ranked list: pinning alone is predicted at +5 to +8 points for 2 to 5 percent cost; pinning plus the re-run summariser at +8 to +12 points for 0 to 5 percent cost. The second is the one to promote.
Failure link: lost the goal was about 19 percent of all long runs (69 percent fail, 11 of 40 of those). Pinning fixes the 9 of 11 where the text was gone [F4]. If a third of those runs then hit a second failure kind, lost the goal falls from about 19 to about 6 percent of runs, giving +5 to +8 points. The summariser's stale-context gain from [F14] adds about +3 on top, now with no offsetting loss.
Mechanism: the trimmer cannot reach the system prompt, so the task is present at every step by construction, and the harness can log that as a per-run flag.
Cost: the task text stays in the window from the step where it would have been trimmed to the end, adding roughly task length times remaining steps. For a 300 to 800 token task that is 2 to 5 percent of a 65k run. The summariser shrinks history, so the pair should land at or below baseline cost. Both sit well inside the 20 percent limit [F18] and nowhere near the doubling ban.
Short tasks: they never reach the trim threshold [F2], so the only change is the task sitting in the system prompt rather than the first message. Predicted effect: zero. The study checks this directly.
Keep rule: pinning alone sits near the +6 bar with a 4-point seed spread, so it might fail the rule on its own. The combination is predicted to clear +6 with margin. The study measures both so the panel can see which earns the keep.
Testable: pass rate on seeds 1-3, pass^3, tokens, wall time, and failure kinds on 20 runs, exactly as the plan lists [F17]. One extra harness log field, task text present at end, is cheap and makes the mechanism auditable.
Model limits: this change touches only lost the goal and, through the summariser, stale context. It does nothing for loop (9), wrong verification (6), gave up early (4) or tool misuse (3) [F3]. Those need their own harness changes or, for part of gave up early and tool misuse, likely a better model.
Hidden tests: untouched; the agent sees nothing new except its own task.

WEAK POINTS:
Presence is not influence. The 2 of 11 lost-the-goal runs still had the task in view [F4], and the open question is whether others drift for another reason. If lost-the-goal stays near 11 of 40 while the log shows the task present in every run, the mechanism is wrong and the fix is the model's attention, not the trimmer.
System-prompt placement may change how the model treats the text. It might read the task as a standing rule rather than the specific job, and over-generalise. The labelled TASK block at the end of the system prompt, right next to the start of history, is the mitigation. A short-task drop would be the signal.
The system prompt is no longer static across runs. Any prompt caching keyed on the system prompt loses its hit rate, which could raise wall time or cost on the provider side. The cost line in the measurement catches this.
The summariser may still write a conflicting shortened goal. The added prompt line reduces this but does not guarantee it. Reading the 20-run sample of summaries shows whether it happens.
The stale-context gain from [F14] may not survive the change. If pinning plus summariser scores no better than pinning alone, the summariser is dead weight and should be dropped from the ranked list.
The gain estimate rests on 40 hand-read runs by one person. The failure-kind split could be off by several runs, which moves the prediction by a few points. The synthetic CSV is not used as evidence here; its column set is only borrowed as the logging schema.

PROPOSED TEST:
Screen on the 12-task subset, seeds 1-3, 36 runs per arm, four arms: baseline (existing numbers), ungated summariser re-run as in [F14], pinning alone, pinning plus summariser. New runs: 108. Log per run: task text present at end, failure kind, tokens.
Promote to the full 48 long tasks, seeds 1-3, 144 runs per arm, the one or two arms that beat the summariser arm by 2 points or more on the screen: at most 288 runs.
Run the 72 short tasks on seeds 1-3 for the promoted arm to check no drop: 216 runs.
Total at most 612 runs and two full measurements, well inside 2,500 runs and 15 measurements [F19].
Pass if the promoted arm shows +6 or more on long tasks, cost per run up 20 percent or less, short-task pass not lower, and lost-the-goal falls to at most 2 of 20 in the read sample.
Refuted if lost-the-goal is unchanged while the log shows the task present in every run; that confirms presence without influence and marks this failure kind as a model limit. Killed if the pinning arms do not beat the summariser arm by 2 points on the screen, or if short-task pass falls by any amount.
