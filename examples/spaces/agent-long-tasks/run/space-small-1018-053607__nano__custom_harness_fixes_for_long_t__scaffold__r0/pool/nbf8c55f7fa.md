CLAIM:
Add a restatement handshake to the harness: after every trim event and at steps 15, 30 and 45, the harness asks the agent for a one-line restatement of the goal, splits the original task text into requirement sentences, and re-injects the verbatim task text at the end of the window only when a requirement is missing from the restatement. The agent proves it still holds the goal, injection is gated by that proof instead of a timer, and the restatement log turns "lost the goal" into a per-step measurement. Predicted long-task pass gain is +5 to +8 points at under 5 percent more tokens per run.

FROM THE FACTS TO THE IDEA:
Long tasks pass 31 percent and short ones 78 percent, and the same task passes and fails across runs [F1], so the failures are mostly about what happens late in a run, not about what the model can do.
Lost the goal is the largest failure kind, 11 of 40 read runs [F3].
In 9 of those 11 the task text was no longer in the window, because the harness trims oldest first and the task text is oldest [F4], [F9].
Trimming only happens past 100k tokens [F9], which is why passing and failing runs look alike for 25 steps and split after that [F8]; long runs cross the trim line, short runs never do.
The summariser experiment showed that a model rewriting its own context shortens or drops the task text in 6 of 10 summaries [F14], so any re-statement by the model must be checked against the original, not trusted as the new source.
Lost in the Middle says the model uses the start and end of the window best [F22]; once the start is trimmed, the end is the only strong position left, so an injection should go there.
Pinning the task text is untried [F15], and the open question is whether pinning alone fixes most lost-the-goal runs or whether those runs drift for another reason.
A timer-based or trim-based copy of the task text answers the first half of that question but not the second: it cannot tell a run that forgot the goal from a run that held the goal and drifted anyway.
The handshake answers both: a wrong restatement is a goal-gone run and gets the verbatim text; a correct restatement that still ends in failure is drift for another reason, and that run is logged as a candidate model limit.
The check is cheap: the question is about 40 tokens, the answer about 60, and the full task text is injected only on a miss, so injected volume is lower than a copy on every trim.
Air traffic control uses the same protocol: a short instruction given once over a lossy channel is read back by the actor before the actor acts on it, and the issuer corrects only on a wrong readback.

FROM THE IDEA TO THE RESULT:
Design in words: the task text is parsed once at run start into requirement sentences, each with its key tokens (file names, function names, numbers, named behaviours, test names); a requirement counts as present in the restatement if at least half of its key tokens appear, and the harness also accepts a verbatim quote.
Trigger: a hook after each trim event, and a step hook at tool calls 15, 30 and 45; the harness appends a user-role message asking for one line that states the goal and the checks the agent will run.
Action on a miss: the harness appends the verbatim task text as a new user message at the end of the window, prefixed with the names of the missing requirements; on a hit it appends nothing and the run continues.
Ranked list and gain: the 9 goal-gone runs are 9 of 40 failures, so about 22 percent of long-task failures, which is about 15 points of the 69 percent failure rate; if the injection recovers half of them, that is +7 to +8 points, and a conservative floor of one third gives +5; the 2 lost-the-goal runs with the text still present are not expected to move.
Token cost: four to six checks per long run at about 100 tokens each is under 1k tokens in the window; if prompt tokens are billed on every later step, the checks cost about 3k billed tokens over the rest of the run; one injection of a task text of 300 to 600 tokens adds about the same; total stays under 5 percent of the 65k baseline [F2], well inside the 20 percent cost ceiling [F18].
Short tasks: they end under 15 tool calls and never reach 100k tokens [F1], [F9], so neither trigger fires, and the short-task pass rate cannot fall by construction; the 12 short guard tasks in the screen check this empirically.
Step cap: the restatement is a text turn, not a tool call, so it does not use any of the 60 calls and does not reproduce the step-cap failure where loops ran longer [F12].
Failure link: the change targets lost the goal only; it does not claim to help loop, stale context or wrong verification, and the restatement log will show that directly because failures of those kinds should have correct restatements.
Model limits: runs that fail as lost the goal with a correct final restatement, plus the 2 of 11 runs where the text was present and the goal was still lost [F4], are the candidate set where the goal was in words but not in action; if that set does not shrink with injection, it is the model's limit on this failure kind, and the answer can say so with a count rather than a guess.
Measurement: pass rate over seeds 1 to 3, pass^3, tokens and wall time, and failure kinds on a 20-run sample [F17], plus two new columns per run: number of handshakes, number of misses, and step of first miss.
Budget: the screen uses 12 long tasks times 3 seeds times 3 arms, 108 runs, plus 12 short guard tasks times 3 seeds times 1 arm, 36 runs; the full measurement is 144 long runs plus 216 short runs for the no-drop check; total under 520 runs and one full measurement slot of about 15 [F19].
Combination: the handshake composes with a notes file, with harness-run verification and with any later summariser, because it checks the agent's held goal against the original regardless of what else is in the window; it is the natural guard for the summariser failure in [F14].

WEAK POINTS:
Goal in words but not in action: the agent may restate the goal correctly and still edit the wrong thing, so pass gain can be lower than the goal-gone count suggests; the observe-only arm shows this if most lost-the-goal failures have correct restatements.
Paraphrase: a correct restatement in different words can fail the key-token match and trigger an unneeded injection; the harm is only cost, and a run with more than two injections flags the matcher as too strict.
False hit: the agent can echo key tokens while dropping a constraint such as "do not change the public API"; a requirement sentence with few distinctive tokens is the weak case, and the panel should look at misses on such sentences in the 20-run sample.
Distraction: a mid-edit question can break the agent's flow; the 12 short guard tasks will not show this because the trigger never fires there, so the check must be the tokens-per-step and wall-time columns on the 12 long screen tasks and the loop count in the failure-kind sample.
The injected text sits at the end of the window and can be trimmed again later; each trim fires another handshake, so the text is re-injected on the next miss, but a run that trims three or more times will carry two or three copies, and that cost should be counted in the full measurement.
Synthetic CSV: the task-text-in-context flag in the sample CSV cannot support any of this [C9]; the only evidence is the 9 of 11 count in the hand-read runs [F4], and a sample of 11 has a wide margin, so the predicted +5 to +8 could be +3 on the full 48.
Who can exploit it: nobody outside the run, but the agent itself can learn to answer the question with a safe quote without reading its own state; that is why the question asks for the checks it will run as well as the goal, which cannot be quoted from the task text alone.

PROPOSED TEST:
Screen on the 12-task long subset, seeds 1 to 3, three arms of 36 runs each.
Arm A, observe-only: ask the restatement at every trigger, log and score it, never inject; this measures whether misses precede lost-the-goal failures.
Arm B, handshake: same triggers, inject the verbatim task text on a miss; this measures the pass gain.
Arm C, trim-triggered copy: re-inject the verbatim text after every trim with no question; this is the comparison the handshake must at least match at lower injected volume.
Plus 36 runs of 12 short guard tasks under arm B to confirm the triggers never fire and pass rate does not move.
Record for every run: pass, tokens, wall time, steps, number of handshakes, number of misses, step of first miss, failure kind by hand read for the failures.
Refuted if, in arm A, a restatement miss precedes fewer than 6 of 9 failures labeled lost the goal with the task text gone at the end of the run; then the restatement is not a drift signal and the harness should use the plain trim-triggered copy instead.
Refuted if arm B gains under +3 points over baseline on the screen, or gains less than arm C, or costs more tokens per run than arm C.
Refuted if arm B shows a pass drop on the short guard tasks or a rise in loop failures on the long screen tasks, which would mean the question itself drags the agent off task.
If the screen passes, run the full 48 long tasks on seeds 1 to 3 under arm B, with the full short suite once, and keep the change only if long-task pass rises 6 points or more, cost rises under 20 percent, and short-task pass does not fall [F18].
Whatever the outcome, report the count of long failures with a correct final restatement as the measured size of the part of lost the goal that this harness change cannot fix.
