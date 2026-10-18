# Ranked proposals: Harness fixes for long tasks

There is no objective check. Each proposal was read blind by a panel of judges; people's opinions count at a bounded weight. Higher panel score is better.

## 1. n0e7e50894d: panel score 6.722 (sd 0.192) [reference]

Judges: [6.5, 6.83, 6.83]; by criterion: Ranked list 4.33, Failure link 7.33, Testable 7.67, Keep rule 7.33, Model limits 5.0, Fits budget 8.67.

**Claim.** Put the task text in the system prompt at run start instead of the first user message, so neither oldest-first trimming nor the 20-step summariser can ever remove or shorten it. With the goal fixed in place, re-run the summariser from the third tried change unchanged. Predicted long-task pass: 31 to 39-43 percent, cost per run up 2 to 5 percent, short tasks unchanged.

**From the facts to the idea.** Long tasks pass 31 percent against 78 for short ones, and the same task flips between pass and fail across runs [F1, F2].
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

**From the idea to the result.** Ranked list: pinning alone is predicted at +5 to +8 points for 2 to 5 percent cost; pinning plus the re-run summariser at +8 to +12 points for 0 to 5 percent cost. The second is the one to promote.
Failure link: lost the goal was about 19 percent of all long runs (69 percent fail, 11 of 40 of those). Pinning fixes the 9 of 11 where the text was gone [F4]. If a third of those runs then hit a second failure kind, lost the goal falls from about 19 to about 6 percent of runs, giving +5 to +8 points. The summariser's stale-context gain from [F14] adds about +3 on top, now with no offsetting loss.
Mechanism: the trimmer cannot reach the system prompt, so the task is present at every step by construction, and the harness can log that as a per-run flag.
Cost: the task text stays in the window from the step where it would have been trimmed to the end, adding roughly task length times remaining steps. For a 300 to 800 token task that is 2 to 5 percent of a 65k run. The summariser shrinks history, so the pair should land at or below baseline cost. Both sit well inside the 20 percent limit [F18] and nowhere near the doubling ban.
Short tasks: they never reach the trim threshold [F2], so the only change is the task sitting in the system prompt rather than the first message. Predicted effect: zero. The study checks this directly.
Keep rule: pinning alone sits near the +6 bar with a 4-point seed spread, so it might fail the rule on its own. The combination is predicted to clear +6 with margin. The study measures both so the panel can see which earns the keep.
Testable: pass rate on seeds 1-3, pass^3, tokens, wall time, and failure kinds on 20 runs, exactly as the plan lists [F17]. One extra harness log field, task text present at end, is cheap and makes the mechanism auditable.
Model limits: this change touches only lost the goal and, through the summariser, stale context. It does nothing for loop (9), wrong verification (6), gave up early (4) or tool misuse (3) [F3]. Those need their own harness changes or, for part of gave up early and tool misuse, likely a better model.
Hidden tests: untouched; the agent sees nothing new except its own task.

**Weak points.** Presence is not influence. The 2 of 11 lost-the-goal runs still had the task in view [F4], and the open question is whether others drift for another reason. If lost-the-goal stays near 11 of 40 while the log shows the task present in every run, the mechanism is wrong and the fix is the model's attention, not the trimmer.
System-prompt placement may change how the model treats the text. It might read the task as a standing rule rather than the specific job, and over-generalise. The labelled TASK block at the end of the system prompt, right next to the start of history, is the mitigation. A short-task drop would be the signal.
The system prompt is no longer static across runs. Any prompt caching keyed on the system prompt loses its hit rate, which could raise wall time or cost on the provider side. The cost line in the measurement catches this.
The summariser may still write a conflicting shortened goal. The added prompt line reduces this but does not guarantee it. Reading the 20-run sample of summaries shows whether it happens.
The stale-context gain from [F14] may not survive the change. If pinning plus summariser scores no better than pinning alone, the summariser is dead weight and should be dropped from the ranked list.
The gain estimate rests on 40 hand-read runs by one person. The failure-kind split could be off by several runs, which moves the prediction by a few points. The synthetic CSV is not used as evidence here; its column set is only borrowed as the logging schema.

**Proposed test.** Screen on the 12-task subset, seeds 1-3, 36 runs per arm, four arms: baseline (existing numbers), ungated summariser re-run as in [F14], pinning alone, pinning plus summariser. New runs: 108. Log per run: task text present at end, failure kind, tokens.
Promote to the full 48 long tasks, seeds 1-3, 144 runs per arm, the one or two arms that beat the summariser arm by 2 points or more on the screen: at most 288 runs.
Run the 72 short tasks on seeds 1-3 for the promoted arm to check no drop: 216 runs.
Total at most 612 runs and two full measurements, well inside 2,500 runs and 15 measurements [F19].
Pass if the promoted arm shows +6 or more on long tasks, cost per run up 20 percent or less, short-task pass not lower, and lost-the-goal falls to at most 2 of 20 in the read sample.
Refuted if lost-the-goal is unchanged while the log shows the task present in every run; that confirms presence without influence and marks this failure kind as a model limit. Killed if the pinning arms do not beat the summariser arm by 2 points on the screen, or if short-task pass falls by any amount.

**Panel notes.**
- The strongest point is the mechanism: the trimmer and summariser can only touch history, so putting the task in the system prompt fixes the cause, and the test can check this per run. The weakest point is scope: it covers only about 18 of the 40 failures, and its gain arithmetic is internally incons
- The strongest point is the clean mechanism: the harness, not the model, deletes the goal in 9 of 11 runs, and that can be checked directly with a presence log and a refutation test. The weakest point is scope: this is a single change rather than a ranked list across failure kinds, and it never squar
- Strongest: a clean mechanism (the trimmer cannot reach the system prompt) with an auditable presence flag and a falsification test that separates presence from influence. Weakest: the scope is narrow, and the claim that 65k-token runs reach the 100k trim threshold around step 25 is not reconciled wi

## 2. nbf8c55f7fa: panel score 6.278 (sd 0.536)

Judges: [5.67, 6.67, 6.5]; by criterion: Ranked list 2.67, Failure link 8.0, Testable 7.67, Keep rule 6.33, Model limits 5.0, Fits budget 8.0.

**Claim.** Add a restatement handshake to the harness: after every trim event and at steps 15, 30 and 45, the harness asks the agent for a one-line restatement of the goal, splits the original task text into requirement sentences, and re-injects the verbatim task text at the end of the window only when a requirement is missing from the restatement. The agent proves it still holds the goal, injection is gated by that proof instead of a timer, and the restatement log turns "lost the goal" into a per-step measurement. Predicted long-task pass gain is +5 to +8 points at under 5 percent more tokens per run.

**From the facts to the idea.** Long tasks pass 31 percent and short ones 78 percent, and the same task passes and fails across runs [F1], so the failures are mostly about what happens late in a run, not about what the model can do.
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

**From the idea to the result.** Design in words: the task text is parsed once at run start into requirement sentences, each with its key tokens (file names, function names, numbers, named behaviours, test names); a requirement counts as present in the restatement if at least half of its key tokens appear, and the harness also accepts a verbatim quote.
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

**Weak points.** Goal in words but not in action: the agent may restate the goal correctly and still edit the wrong thing, so pass gain can be lower than the goal-gone count suggests; the observe-only arm shows this if most lost-the-goal failures have correct restatements.
Paraphrase: a correct restatement in different words can fail the key-token match and trigger an unneeded injection; the harm is only cost, and a run with more than two injections flags the matcher as too strict.
False hit: the agent can echo key tokens while dropping a constraint such as "do not change the public API"; a requirement sentence with few distinctive tokens is the weak case, and the panel should look at misses on such sentences in the 20-run sample.
Distraction: a mid-edit question can break the agent's flow; the 12 short guard tasks will not show this because the trigger never fires there, so the check must be the tokens-per-step and wall-time columns on the 12 long screen tasks and the loop count in the failure-kind sample.
The injected text sits at the end of the window and can be trimmed again later; each trim fires another handshake, so the text is re-injected on the next miss, but a run that trims three or more times will carry two or three copies, and that cost should be counted in the full measurement.
Synthetic CSV: the task-text-in-context flag in the sample CSV cannot support any of this [C9]; the only evidence is the 9 of 11 count in the hand-read runs [F4], and a sample of 11 has a wide margin, so the predicted +5 to +8 could be +3 on the full 48.
Who can exploit it: nobody outside the run, but the agent itself can learn to answer the question with a safe quote without reading its own state; that is why the question asks for the checks it will run as well as the goal, which cannot be quoted from the task text alone.

**Proposed test.** Screen on the 12-task long subset, seeds 1 to 3, three arms of 36 runs each.
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

**Panel notes.**
- The strongest point is the gated readback with an observe-only arm, which both tests the mechanism and measures the model-limit residue for lost the goal. The weakest point is that it covers one failure kind with a borderline predicted gain instead of the ranked, cross-taxonomy list the question ask
- The strongest point is the readback design: arm A doubles as a diagnostic that answers the "pinning alone vs. drift" open question with counts, not guesses. The weakest point is that it is a single change whose predicted gain barely reaches the keep threshold, and it is not the ranked multi-change l
- Strongest point: the readback design turns "pinning alone vs. drift for another reason" into a measurable observe-only arm with clean refutation rules. Weakest point: it covers one change for one failure kind, so it is not the ranked list the question asks for.


# Run report: space-small-1018-053607__nano__custom_harness_fixes_for_long_t__scaffold__r0

arm **scaffold** · model fable via cli_json · baseline v2 · map lens parts · 2026-10-18T06:08:09

## Read this first

**Result.** 2 of 2 builds passed the cheap checks; 0 verified overnight so far. Best projected gap: `n0e7e50894d` (task_text_pinnin, impl:deepen+research), extrapolated z None: Moving the task text from the first user message into the system prompt makes it immune to trimming and summarising, so  Cost: 505,534 tokens of the inventing model (the budgeted part) plus 7,313,236 of the cheap model's retrieval and clerical work, $42.7, 745 s.
**Can I trust this?** commitments hash e0992bef611d, 1 control-file changes.
**What it needs from you.** Run the overnight verdict on the 2 pooled scripts: `python -m nano.batch_verify --run D:\AGI-lab\runs\space-small-1018-053607__nano__custom_harness_fixes_for_long_t__scaffold__r0 --baseline-seeds 5`; about 5.7 GPU hours if every candidate goes to three seeds. You can seed the ambitious lane yourself: a JSON list of {part, text} at memory/owner_seeds.json.
**Glossary.** *learn z*: the loss gap to the original at 45 training steps, in units of the seed-to-seed spread; negative is better; *long z*: the same gap at 240 steps; *extrap z*: the long gap projected forward along its trend; the pool is ranked by it; *step ratio*: candidate step time over the original's; the cap is 2; *lane*: main = chosen by score; longshot = the ambitious lane; family = a variant of a near miss; tune = a scripted constant change; *rung*: the ladder of cheap checks: 0 boundary, 1 build and reach, 2 timing, 3 learning, 4 long comparison; 5 is the overnight exam.

## The funnel

| stage | count | of previous |
|---|---|---|
| model calls | 94 | |
| sketches | 86 | own 52 / web 34 |
| clusters | 36 | 42% |
| tagged new | 29 | 81% |
| tagged known / known failure | 6 / 1 | |
| matching the private obvious answers | 1 | 3% |
| interrogation calls | 6 | gens {0: 6}; 36 new ideas, 60 facts, 0 unsourced numbers dropped |
| built | 2 | parse failures 0 |
| checked (rungs 0-3) | 2 | 100%; failures {'checked': 2} |
| verified overnight | 0 | of 0 examined |

## Cost

inventing model 505,534 tokens of budget 600000; cheap model 7,313,236 more for retrieval and clerical calls, outside the budget (a web search re-reads its pages on every turn); cost $42.7; $21.35 per checked candidate; wall 745 s

## By card and by part

| card | built | checked |
|---|---|---|
| impl | 2 | 2 |

| part | built | checked |
|---|---|---|
| task_text_pinnin | 2 | 2 |

## Pool (ranked by the extrapolated long-run gap in seed spreads; negative is better)

| id | part | card | learn z | long z | trend | extrap z | step ratio | params | hypothesis |
|---|---|---|---|---|---|---|---|---|---|
| n0e7e50894d | task_text_pinnin | impl:deepen+research | 0.0 | None | None | None | None | None | Moving the task text from the first user message into the system prompt makes it immune to trimming  |
| nbf8c55f7fa | task_text_pinnin | impl:deepen+research | 0.89 | None | None | None | None | None | Asking the agent to restate the goal at each trim event and every 15 steps, and re-injecting the ver |

## Lanes

| lane | pooled | verified | stackable |
|---|---|---|---|
| main | 1 | 0 | 0 |
| longshot | 1 | 0 | 0 |

## Commitments (fixed before any idea existed)

hash e0992bef611d; baseline d25cf10d3373; budget 600,000 tokens; win rule {'margin_nats': 0.5, 'alpha': 0.05, 'min_seeds': 1}; slots {'k_impl': 2, 'rounds': 1, 'per_node': 1, 'inward_share': 0.6, 'longshot_share': 0.2, 'leap_share': 0.25, 'family_variants': 2}; models {'model': 'fable', 'cheap': 'sonnet', 'research': 'sonnet'}; control-file changes during the run: 1.

## Selection (why groups were chosen or dropped)

| reason | groups |
|---|---|
| below the cut | 34 |
| picked_main | 1 |
| picked_lane | 1 |
Per-group rows with scores, cuts and lane propensities are in selection.jsonl.

## Critique (pre-mortem objections, resolved by the ladder)

60 objections raised, 31 with a measurable test; on built ideas 0 confirmed, 0 refuted, 0 pending, 0 untestable.

## Leaps (the ambitious lane, by counts)

30 of 86 sketches were leaps; 16 leap clusters; built 2, checked 2, verified or stackable 0.

| operator | sketches | built | checked | verified |
|---|---|---|---|---|
| ? | 9 | 1 | 1 | 0 |
| limit | 6 | 0 | 0 | 0 |
| subtract | 6 | 0 | 0 | 0 |
| existence | 3 | 1 | 1 | 0 |
| import | 3 | 0 | 0 | 0 |
| rerepresent | 3 | 0 | 0 | 0 |

## Discovery curve

| round | contexts | sketches | new clusters | per context | top-2 share |
|---|---|---|---|---|---|
| 1 | 7 | 50 | 28 | 4.0 | 0.28 |

Built ideas whose benefit lies outside this exam (metric-blind): 1


## Proposals for a new verifier (upward)

Logged, not acted on: adopting a new success measure is a human decision, so the loop builds and checks nothing here. Each proposal reframes the whole problem; the same list is under the root node of problem_tree.json ("proposals") for reading and voting.

- **Measure the harness as a packing scheme: how much of the goal stays readable as the context condenses, not whether the run passed.** (round 1, u24414d2aa7)
  - Reframing: DNA is compressed thousands of times yet promoters stay accessible; the harness compresses history too (trim at 100k, drop to 80k [F9]), but accessibility is never measured. Instead of six post-hoc failure labels [F3], model each run as a channel and measure, at fixed steps, whether the task text, acceptance criteria, and the last edit's intent are still present and still used. Lost-the-goal [F4], stale context [F6], and the summaries that shortened the task [F14] become one quantity: goal and state accessibility over time.
  - New measure: Goal-recall curve. At steps 20, 30, 40, 50 the harness injects a side probe (not shown to the agent's main trajectory, or run on a forked copy): "restate the task and the acceptance criteria in two lines." Score against the original with exact-span match plus a rubric. Report area under the recall curve per harness variant, and the step at which recall first drops below 0.8. A harness change is good if it raises area under the curve; pass rate becomes a secondary check. Also log "live fraction": share of context tokens referenced by any later tool call.
  - Why: Pass rate at 31 percent with a 4-point seed spread [F18] needs 144 runs to detect a change; a recall curve shifts on every run and shows which step the harness loses the goal, so pinning, notes file, and summaries can be compared on 12 tasks. It also separates "task text gone" from "task text present but ignored," which decides whether pinning alone fixes lost-the-goal, a listed open question.
  - Cost: Forked probe calls, about 400 tokens each, 4 per run, so under 5 percent extra. Code: a fork-and-probe hook in the harness and a scorer. Data: the original task texts. People: one person to write the rubric and spot-check 20 probes.
- **Study continuations from a shared checkpoint, not whole runs, because the first 25 steps carry no signal.** (round 1, ued74553d53)
  - Reframing: Passing and failing runs are indistinguishable until step 25 [F8], so most of a 65k-token run [F2] is a prefix that varies nothing. Like replication from a stored template, store the state at step 25 (context, repo snapshot, notes) and branch many continuations with different harness settings. The unit of study becomes the continuation, and harness changes are compared on the same prefix, which removes prefix noise from the comparison.
  - New measure: Continuation pass rate: for each of the 48 long tasks, one shared prefix per seed, then k continuations per harness variant. Report pass rate over continuations, paired difference per prefix (variant A minus variant B on the same prefix), and tokens spent after the branch point. The keep rule maps to a paired difference of 6 points or more with confidence interval excluding zero.
  - Why: The current plan spends 144 full runs per change [F17] and allows about 15 changes [F19]. Branching reuses the prefix, so the post-branch cost is roughly 40 percent of a run, and paired comparison on identical prefixes cuts the seed spread, so 3 to 4 times as many variants fit the 2,500-run budget. It also exposes whether a late-stage change (verification step, loop breaker) helps at all, since pr
  - Cost: Harness support for snapshot and restore of repo plus context (a tarball and a JSON message log). Prompt cache hits on the shared prefix lower token cost further. People: none beyond the existing failure-kind reader.
- **Replace pass rate under a keep rule with passes per fixed token budget, and compare every change at matched spend.** (round 1, ud978cc2b8a)
  - Reframing: The retry lifts the pair to 44 percent but doubles failed-task cost [F13]; the step cap to 100 gains 2 points for 45 percent more cost [F12]. Both are rejected or accepted by two separate thresholds [F18] that do not say which is the better use of 130k tokens. DNA packing is judged by information per unit volume; judge the harness by expected passes per 100k tokens, and let each change pick its own mix of retries, caps, and checkpoint restarts within that budget.
  - New measure: Pass-per-budget curve: for budgets B in 65k, 100k, 130k, 200k tokens per task, the pass rate achievable by the best policy under that budget (single run, run plus retry, run plus checkpoint resume, two short runs with a notes handoff). Compute by running each variant and recording cumulative tokens at the moment of stop, then reading pass rate at each budget cut. Rank changes by area between their curve and the baseline curve across the 65k to 130k band.
  - Why: The current framing cannot say whether a loop breaker that saves 15k tokens and gains 3 points beats a verification step that costs 8k tokens and gains 7 points, because cost and pass are separate gates. Budget-matched curves make the two commensurable and show which changes combine (notes handoff plus checkpoint resume) and which cancel (summaries plus pinning), another listed open question. It a
  - Cost: Only logging: cumulative tokens per step and stop point, already collected [F17]. Code: a curve script. Runs: the same 144 per variant, so no budget change, but variants that stop early return runs to the pool.
