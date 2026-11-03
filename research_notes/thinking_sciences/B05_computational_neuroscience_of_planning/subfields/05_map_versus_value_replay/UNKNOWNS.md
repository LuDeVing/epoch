# Map versus value replay: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B05.05-U1 | Does ranking stored routes by P(goal) x gain beat recency and current-goal-only memory? | Goal-weighted route store | memory | K01, K10, a02, b01; single-source, no LLM test | 40-task streams over 6 goals, Markov goal switching p11 in {0.05, 0.5, 0.9}; arms: current-goal-only, recency, P x gain, no memory; solved fraction in last 20 tasks | P x gain beats both controls by >= 5 points at p11 <= 0.5, and loses < 2 points at p11 = 0.9, over 3 seeds | High |
| B05.05-U2 | Does in-context hindsight tagging (store each trajectory under every goal it achieved) help a frozen agent? | Hindsight tags on every stored route | memory | K08, K20, d03, d04; ECHO single-source in-context, others are training-time | ECHO-style environments, 16 queries over 4 goals; arms: verified tags, target-goal tag only, no memory; reward per query | Verified tags beat target-only by >= 10% relative on reward, with a CI that excludes 0 | High |
| B05.05-U3 | How much wrong-label noise breaks hindsight tagging, and does a code check fix it? | Mandatory label verification threshold | G2/memory | K09, K20, c18, d04; single-source (85% valid in 40 samples; no sweep) | U2 with 0/10/25/50% wrong labels; verified vs unverified; solve rate | Unverified falls below the no-memory arm at some noise level and verification restores >= 80% of the gain | High |
| B05.05-U4 | Does precomputing routes to unpursued goals pay at equal total tokens? | Idle-budget preplay, gated by predicted reuse | memory/G12 | K13, K19, c10, d01, d02; human and older-model evidence, no agent-scaffold test | 1, 3 and 10 later queries per context; arms: precompute top-k, retrieve at test time, none; accuracy per total token | Precompute wins at >= 5 queries by >= 5 points and does not lose more than 2 points at 1 query | High |
| B05.05-U5 | Does a slow recurrence prior beside the fast current-goal belief help after goal switches? | Two goal trackers (fast and slow) | S0/memory | K03, b04, a05; contested, qualitative model fit | Goals switch in blocks of 10; arms: fast only, fast + slow, uniform; solve rate after switch-back | Fast + slow beats fast-only by >= 5 points on switch-back, no loss elsewhere | Med |
| B05.05-U6 | Are hub/bottleneck routes worth more than random routes? | Hub-first route priority | memory | K16, a04, b03; model-only, untested in animals | Community-graph routing; arms: hub routes first, random, goal tails; reuse rate per stored route | Hub reuse rate exceeds random by >= 15% relative | Med |
| B05.05-U7 | Which eviction rule works when goals drift? | Score eviction P(goal) x gain x success | memory | K22, d08, d09, d10; single-source, no drift test | Bounded store; goal set changes mid-run; 75% distractor variant; arms: LRU, LFU, FIFO, score; Precision@5 and post-drift solve rate | Score beats LRU by >= 5 points after drift and ties on the clean stream | Med |
| B05.05-U8 | Can the model estimate P(goal) from its own history, or should code count? | Model-read goal priors (else keep code counts) | S0/G5 | K10, d17; no study | Model outputs goal distribution vs frequency counter; Brier score and downstream solve rate | Model estimate beats counter on Brier by >= 0.02 and improves solve rate; else code counts stay | Med |
| B05.05-U9 | Does goal-switching-order rehearsal (other goal first when p11 is low) help? | Order rule from switching rate | memory | K16, a07, c03; simulation prediction only | Two-goal stream with blocked route; p11 = 0.5 vs 0.05; arms: current goal first, expected-recurrence order | Expected-recurrence order wins at p11 = 0.05 by >= 5 points and ties at 0.5 | Low |
| B05.05-U10 | Is one authoritative route per goal better than route plus reflection notes? | Single route per goal, no stacked notes | memory | K21, d06; single-source, 51 examples | Same task set; arms: route only, route + reflection; solve rate and tokens | Route-only >= stacked on solve rate with fewer tokens, across 2 benchmarks | Med |
| B05.05-U11 | Does a prompt-only map-building step before planning help on frontier 2026 models? | Map-building sub-step in S2 | S2/O | K12, c13, d11, d12, d13; contested, 2024 negative | Larger mazes and community graphs; arms: adjacency list only, adjacency + explicit map marking, plain; solve rate | Map step beats adjacency-only by >= 10 points at equal tokens | Low |
| B05.05-U12 | Does a cheap heuristic (strength x similarity x inhibition of return) match P x gain? | Cheap rehearsal heuristic in place of the priority rule | memory | b17; single-source, human-free model | U1 stream; add heuristic arm | Heuristic within 2 points of P x gain at lower write cost | Low |

## Open questions we cannot test on our bench yet

- Which neural account is right (map, maintenance, representation protection, adaptation trapping). Needs a rodent experiment that switches the rewarded arm at a known rate and reads replay order (d18). Not testable with LLMs.
- Whether the bottleneck-replay prediction holds in animals. Needs new data with many goals and start states. Mallory 2026 keeps the goal fixed.
- Independent replication of HSL and AgentHER, and at large model scale. Needs fine-tuning access and a second lab.
- Real-world goal statistics (recurrence, p11) for our users. Needs logs from actual use; the bench can only simulate them.
- Whether goal-weighted memory helps at long horizons (hundreds of tasks). Needs a long-stream bench and a larger budget.

## Order to run

1. **U2 (with U3 as its sweep).** Cheapest: ECHO environments exist and the effect is large. It decides whether hindsight tagging and label verification enter memory at all.
2. **U1.** The core of this subfield and a new test with no prior LLM result. Tells us whether P(goal) x gain adds anything over plain tagging, and at which p11.
3. **U4.** Decides whether idle-budget preplay is worth its tokens; sleep-time compute suggests a clear threshold at 5 or more later queries.
