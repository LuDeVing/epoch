# Demo runbook: two people, two agents, one shared run

Section 13 of [MULTIPLAYER_DESIGN.md](MULTIPLAYER_DESIGN.md), made concrete. The user guide is [SPACE.md](SPACE.md);
the pitch is [SPACE_PITCH.md](SPACE_PITCH.md). Every beat is a slash command or a Go. No beat waits on a model.

All commands run in the repo folder with the lab Python and the lab root (PowerShell):

```
$env:HTSA_LAB_ROOT = "D:/AGI-lab"
D:\AGI-lab\.venv\Scripts\python.exe -m space.demo --check
```

## 1. Before the slot (one PC)

```
python -m space.demo --check
python -m space.demo --stage
```

`--check` exits non-zero unless all of these hold: port 8766 is free; every file in space/web/vendor has its pinned
size; Chrome and Edge are at their known paths; D:\AGI-lab\spaces exists (it makes it); at least 3 GB of memory is
free (GlobalMemoryStatusEx); the recorded log and its hash file exist and the log holds no private key;
`node --test space/web/tests/replay` passes. It prints the netsh line that opens the port for `--lan`.

`--stage` refuses to start under 3 GB free or with port 8766 taken. Then it starts, in this order, with one log per
process in `D:\AGI-lab\spaces\stage-<HHMM>\logs\`:

1. the server: `python -m space.server --db D:/AGI-lab/spaces/stage-<HHMM>/space.db --memory-dir D:/AGI-lab/memory/_mock/binpack_nobase`
2. the two person-agents: `python -m space.agent --me ana --model mock ...` and `--me ben` (with `--live-agents`:
   `--model sonnet --fallback mock`)
3. the loop: `python -m nano.dry_run --batch stage-<HHMM> --profile binpack_nobase --implement 3 --rounds 2 --space http://127.0.0.1:8766 --me team.loop --step --control-poll-seconds 1`
4. Chrome with `http://127.0.0.1:8766/?me=ana`, Edge with `http://127.0.0.1:8766/?me=ben`, and a Chrome `--app`
   window with its own `--user-data-dir` (stage-<HHMM>/projector-profile) on the projector with `?stage=1&follow=ana`.

The console then takes single keys:

| Key | What it does |
|---|---|
| g | Go: posts run_step (as Ben) for the boundary the loop waits at. Nothing is posted when the loop is not waiting. |
| r | Replay: stops the loop, the agents and the server, then serves the recorded round from the last beat the live run reached, at speed 30, on the same port. The banner reads "Replay of a recorded round". |
| k | the kill-and-restart drill: kills the server and starts it again on the same database |
| s | status: which processes run, and the run's round and stage |
| q | quit: ends every process tree it started (taskkill /T /F) |

The problem is the mock bin-packing profile: parts choice, state, open, stats, ties, recipe, plus the off-map lane.
Both people sit at the one PC (Chrome and Edge keep separate storage). A second laptop over a phone hotspot with
`--lan` and the printed key is used only if it was rehearsed on that hotspot the same day. The recorded log and a
60 s screen capture sit on the PC and on a USB stick.

Do not start a research from the page's Start a research button during the slot: the stage loop already runs, and
the server allows one run at a time. The button starts a free-running loop (no Go), sized small, medium or big
(SPACE.md section 8). Use it after the demo, in Mock, to show a second run.

## 2. The manual browser check (once, the first time after the merge)

No browser was opened while the space was built. Before the first rehearsal with people:

1. `python -m space.demo --stage`. Chrome (Ana), Edge (Ben) and the projector window open.
2. The top bar of all three windows reads "Live #N" with the same N, "Paused: waits for Go (planned r1)", and the
   same layout hash.
3. The tree shows six parts plus the off-map lane; the people chips and the agent rings show.
4. In Ben's My agent tab type `/note warm-up`. Ana's window shows a queued chip within a blink; Ben's agent answers
   within 2 s.
5. Press g in the console. The chip turns "applied in round 1, stage planned"; the bottom strip shows the digest.
6. Reload Ana's window: it comes back at the same N with the same picture.
7. If the stream stalls in either browser, open the page with `?poll=1` and note it here.
8. Press q. Write down what failed and fix it before the slot.

## 3. Three checks at 30 minutes before

1. Ben types `/note warm-up`: a queued chip appears on Ana's screen within 200 ms and Ben's agent acks within 2 s.
2. The layout hash chip reads the same on all three windows.
3. Nothing in the script waits for a live model: both agents on `--model mock`, or on Sonnet with `--fallback mock`
   and only the one optional free-text beat.

## 4. Run of show, 4:00

The ids below come from the rehearsal recording (space/recorded/stage_round.beats.json). The loop assigns them,
and the mock run gives the same structure every time, but always read the ids off the screen if they differ: a
question is also `Q1`, `Q2`, `Q3` (the preview's top 3), and a cluster also takes its exact id from the bubble.

| Time | Who | Does | Both screens show | The other agent | Line to say |
|---|---|---|---|---|---|
| 0:00 | Ana | stands | the tree with six parts and the off-map lane, two person chips, two agent rings, "Paused: waits for Go (planned r1)", the hash chip | | "HTSA is a team of AI researchers. Two of us steer one run, each through our own agent. People steer, tests decide." |
| 0:15 | Ana | `/branch root "item order": how items are sorted before packing --claim` | a dashed blue card "item order" under root, "waits for planned, round 1", the claim ring of Ana's agent | Ben's agent: "Ana added item order. I carry it to the inventors at planned r1." | "Ben's agent already knows. No lock, no refresh, and the claim says who works there." |
| 0:35 | Ben | `/note check tie-breaking before the choice rule` | two queued chips side by side | Ana's agent: "Ben left a note for the team. The team reads it at planned r1." | "Everything a person does is queued first. The screen says so." |
| 0:50 | Ben | Go (planned r1) | item order turns solid, "applied in round 1, stage planned"; the note chip flips; the strip shows the digest; the sketch burst fills the islands, item order too | both agents post their digest line | "That is the other agent being told what changed. The text on the screen is the text the agent saw." |
| 1:15 | Ben | Go (ideated r1) | clusters regroup in three stages; the first island forms under item order; selected rings; the hash chip changes and matches on all windows | | "Same picture on every screen, so we can point at a bubble and mean the same thing." |
| 1:30 | Ben, Ana | `/vote up offtree-in-k04` (Ben), `/vote up choice-ou-k00` (Ana) | vote dots in orange and blue on the two bubbles | | "Votes are shown by name. They do not decide anything. Tests do." |
| 1:45 | Ben | Go (clustered r1) | argument chains grow one exchange at a time: objection chip, reply, mark | | "The critics argue with the authors. Nothing is dropped." |
| 2:05 | Ana | `/reply open-in-k01 2 rebut: the quick check at seed 0 gave bins ratio 0.91 measured` | her reply in blue with a person badge under "a reply never gates a build" | Ben's agent: "Ana rebutted an objection on harmonic classes." | "People argue with evidence tags. A reply never skips a test." |
| 2:20 | Ben | Go (deepened r1), then Go (built r1) when the builds land (seconds) | builder cards; the mock scorer runs 20 to 40 s | | "Real rounds take minutes to hours. This run uses the mock backend with the real scoring code, so the numbers are real checks on mock code." |
| 2:55 | | results land one by one | the winning bubble ripples and reads "won"; Results rows with rung and metrics; a loss stays in grey; hit or miss beside each voter | | "People steer. Tests decide. The vote is scored against the test, by name." |
| 3:10 | | the verified boundary posts the preview | the top 3 for round 2 with scores and bin-packing text | | |
| 3:15 | Ben | `/veto u1bfd800627` (or `/veto Q1`) | Q1 struck through, "acts at the next pick, round 2" | Ana's agent: "Ben vetoed Q1. It acts at the next pick, round 2." | |
| 3:25 | Ana, then Ben within 3 s | `/choose u63d9e403ab` (Ana), `/choose ue6bf5e5143` (Ben) | Ana's screen: "Ben's choice replaced yours" | Ana's agent: "Ben's choice replaced yours at #N. Choose again to override." | "Last writer wins, and nobody loses silently." |
| 3:40 | Ben | Go (verified r1) | round 2 starts: the pick card "chosen by person (Ben), vetoed Q1 (Ben)"; the queued chips read "applied at the pick of round 2" | | |
| 3:50 | Ana | close | | | "Two people, two agents, one shared run. Every change is shown, named, delivered to the other agent at a safe point and receipted. The limits: real rounds are slow, so this run was the mock backend, and the person-agents answered on the canned path." |

What was canned, said out loud at the close: on `--model mock` no agent line comes from a model. Acks, peer lines
and digest lines are templates on every run; a free-text answer would carry "(canned)".

The optional live beat (owner decision: only if the person-agent's golden set passes on the live model, and at most
one): with `--live-agents`, Ana's 0:15 message is typed as free text ("add a part under root for the order the items
are packed in, and claim it"). The ack is immediate; the dashed card appears when Sonnet answers (5 to 15 s); keep
talking; at 20 s the canned reply lands marked "(canned)", and say so.

## 5. The recorded round

`python -m space.demo --rehearse` made space/recorded/stage_round.ndjson (554 events), its hash file and
its beat table. The rehearsal took 232 s. The ids it used and the seq of every beat (for `--seek`):

| Beat | Scripted time | Seq in the recording | Event |
|---|---|---|---|
| open | 0:00 | 10 | stage_entered |
| branch | 0:15 | 17 | node_added |
| note | 0:35 | 23 | note_posted |
| go_planned_1 | 0:50 | 25 | run_step |
| go_ideated_1 | 1:15 | 49 | run_step |
| votes | 1:30 | 78 | vote_cast |
| go_clustered_1 | 1:45 | 80 | run_step |
| reply | 2:05 | 487 | reply_posted |
| go_deepened_1 | 2:20 | 489 | run_step |
| go_built_1 | 2:20 | 496 | run_step |
| win | 2:55 | 505 | test_result |
| preview | 3:10 | 509 | question_preview |
| veto | 3:15 | 517 | question_vetoed |
| choose | 3:25 | 525 | question_chosen |
| drill | 3:30 | 527 | claim_expired |
| go_verified_1 | 3:40 | 530 | run_step |
| pick | 3:40 | 532 | question_picked |

| Id | Value |
|---|---|
| Ben's vote (1:30) | `offtree-in-k04` (best fit) |
| Ana's vote (1:30) | `choice-ou-k00` (worst fit) |
| the reply (2:05) | cluster `open-in-k01` (harmonic classes), objection 2 |
| Q1, vetoed by Ben (3:15) | `u1bfd800627` |
| Q2, chosen by Ana (3:25) | `u63d9e403ab` |
| Q3, chosen by Ben (3:25) | `ue6bf5e5143` |
| item order's node_added | e17 |
| hit or miss on the screen | {"ana": ["miss"], "ben": ["miss", "hit"]} |

## 6. Fallback ladder

1. A boundary takes more than 8 s: keep talking; presence chips and templated lines keep moving.
2. More than 20 s: press r. The server restarts on space/recorded/stage_round.ndjson at speed 30 from the seq of
   the last beat reached (the table above). By hand:
   `python -m space.server --db D:/AGI-lab/spaces/stage-<HHMM>-replay/space.db --memory-dir D:/AGI-lab/memory/_mock/binpack_nobase --replay space/recorded/stage_round.ndjson --speed 30 --seek <seq>`.
   The banner reads "Replay of a recorded round"; say so out loud; the script continues from the same beat.
3. The second laptop or the hotspot fails: both people act from the one PC.
4. The page itself fails: play the 60 s capture and narrate it live.

Never hide a replay. Never debug on stage.

Cut list: a 3-minute slot drops the 2:05 reply and the 1:30 votes; a 2-minute slot stops after 1:15 and closes on the
digest strip.

## 7. The kill-and-restart drill (runbook only, not on stage)

Owner decision: the drill stays in the runbook. It proves the log survives a server crash; run it in rehearsal.

- In the stage console press k, or by hand: close the server, then run the same server command again
  (`python -m space.server --db D:/AGI-lab/spaces/stage-<HHMM>/space.db --memory-dir D:/AGI-lab/memory/_mock/binpack_nobase`).
- Both browsers show Reconnecting, then Live #N with the same number. The agent ring shows "claim ended (restart)".
  No event is lost: the log goes on from the same number with the same epoch.
- `--rehearse` runs the drill at 3:30 by default (`--drill none` skips it) and asserts: a reader that read through
  the kill and a fresh reader after it see the same contiguous log, every open claim got claim_expired with reason
  restart, and both agents' outboxes are empty.

## 8. The rehearsal

```
python -m space.demo --rehearse
```

It runs the same processes as the stage without browsers (agents on `--model mock`), refuses to start under 3 GB
free, waits until the loop waits at planned r1, then drives the script at the scripted seconds (`--pace 0.5` halves
them): every beat goes through the agents' chat as a slash command, and each Go is posted only after the matching
stage_entered. It prints one row per check of section 13.5 and the beat table, and exits non-zero unless every
row passes:

| Row | Check |
|---|---|
| post_200ms | a seq returns within 200 ms of every human POST |
| ack_2s | an ack within 2 s of each chat |
| peer_2s | Ben's agent's peer line within 2 s of Ana's node_added |
| applied_item_order | control_applied for item_order at planned r1, by on the node |
| sketch_item_order | sketch_batch with node item_order in round 1 |
| digests_both | digest_taken by both agents after every boundary |
| preview_before_pick | a question_preview before the round 2 pick |
| overwrote | question_chosen carrying overwrote after the double choose |
| win_and_won | a test_result with status win and one cluster marked won |
| voters_hit_or_miss | hit or miss derived for both voters (the Node reducer, as the screen shows it) |
| vetoed_in_pick | the vetoed id in question_picked.vetoed of round 2 |
| drill_restart | the kill-and-restart drill (section 7) |
| beats_in_order | every beat of the script is in the log, in order |
| time_limit | the whole run under 5 minutes |
| no_claude | no claude process among the child processes |
| free_memory | at least 3 GB free at start |
| no_child_left | no child process left after the stop |

On a pass it writes space/recorded/stage_round.ndjson (dumped with the server's `--dump`), stage_round.hash.json
(the layout hash and the state hash from `node space/web/tests/replay/hash.mjs`) and stage_round.beats.json (the
rows, the beats and the ids). On a failure it leaves them in the rehearsal's space folder and keeps the committed
recording. Then check that the replay reaches the same beats:

```
python -m space.demo --replay --speed 50 --exit-when-done
node --test space/web/tests/replay
```
