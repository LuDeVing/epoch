# The HTSA shared research space: the pitch

Track: multiplayer agentic experiences. Two people work on one thing together, each through their own agent.
The stage script is [DEMO_RUNBOOK.md](DEMO_RUNBOOK.md). How it works is [SPACE.md](SPACE.md).

## The opening line

"HTSA is a team of AI researchers. Two of us steer one run, each through our own agent. People steer, tests decide."

## The one sentence for a judge to repeat

"Every change a person makes is shown on every screen at once, delivered to the other person's agent at a safe
point, and receipted with the exact text that agent was told."

## What the judges see, in four minutes

1. Ana adds a part to the problem tree. Both screens show it at once, marked "waits for planned, round 1". Ben's
   agent says so within 2 s.
2. Ben presses Go. The chip flips to "applied in round 1, stage planned". The strip shows the digest text the
   agents were given. A second later the inventors fill the new part with ideas.
3. The idea clusters regroup. The layout hash is the same on every screen, so both people point at the same bubble.
4. Both people vote, by name. Critics argue with authors; Ana answers one objection with a measured fact.
5. The real scoring code tests the builds. The winner ripples and reads "won". Each vote reads hit or miss.
6. The loop previews the next round's top 3 questions. Ben vetoes one; Ana and Ben both choose; Ana's screen says
   "Ben's choice replaced yours". On the next Go the pick card shows the person's choice and the veto.

## The five asks of the track, and where they are on screen

| Ask | The visible moment | Time |
|---|---|---|
| Each agent knows what the other agent changed | Ben's agent: "Ana added item order. I carry it to the inventors at planned r1."; the digest strip after the Go; the Feed line "told to Ben's agent at planned r1" with the receipt | 0:15, 0:50 |
| No conflicts, always up to date | one log with one number per change; queued then applied chips; "Ben's choice replaced yours at #N" for the one slot where people can collide; the same layout hash on every window | 0:35, 0:50, 3:25 |
| Smooth to use | slash commands with a 2 s answer; chips that say when a change acts; presence rings and "last heard"; nothing waits on a model | every beat |
| Each person has their own agent | the My agent tab; agent rings in the person's colour; each agent's own digest line at every boundary | 0:15, 0:50 |
| The tree and the idea clusters look smooth, animated and modern | a new card slides from its parent while its edge grows; clusters regroup in three stages; the winner ripple | 0:15, 1:15, 2:55 |

The track also asks for a live demo with two people on stage: that is the run of show itself, with a recorded
replay as the fallback (shown under a banner, never hidden).

## The honest limits (say them)

- One loop, two people. Two research loops on one map is designed but not built.
- The run on stage is the mock backend with the real bin-packing scoring code. Real rounds take minutes to hours,
  so the numbers are real checks on mock code.
- The person-agents answer slash commands with no model. Free text uses Sonnet with a canned fallback after 20 s,
  and every canned line says "(canned)". The live model path was never run before the demo; on stage it is at most
  one optional beat.
- Votes are shown by name and scored against the tests. They do not change what the loop selects.
- Names are typed at join. There is no login.
- The page was built and tested in Node; the check in Chrome and Edge is by hand before the slot.
- If a beat stalls for more than 20 s we switch to the recorded replay of the same round and say so.

## The closing line

"Two people, two agents, one shared run. Every change is shown, named, delivered to the other agent at a safe point
and receipted. The limits: real rounds are slow, so this run was the mock backend, and the person-agents answered on
the canned path."
