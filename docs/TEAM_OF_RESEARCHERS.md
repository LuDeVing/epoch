# HTSA: a team of AI researchers

A short map of who does what, so we can change it as we go.
Legend: **[built]** works today, **[planned]** designed but not built yet.

## The idea in one picture

```
                 +----------------------------------------------+
                 |            SHARED RESEARCH SPACE             |
                 |  problem tree . ideas . results . opinions   |
                 +----------------------------------------------+
                    ^        ^         ^          ^         ^
                    |        |         |          |         |
               Mapper   Inventors   Critics    Builders   People
                                                (+ tests)  (many, any time)
```

Everyone reads and writes the same space. Agents do the work; people watch, comment and steer.

## The team

| Role | What it does | Model today | Status |
|---|---|---|---|
| **Reader** | Before the map: one whole-problem reading call, how the field splits the problem and where it is weak (`--no-preread` control) | Sonnet (research model) | [built] |
| **Mapper** | Reads the problem, the reading and the measurements, draws the problem tree: parts, sub-parts, weak spots | the strong model | [built] |
| **Inventors** | Many separate idea sessions, each pushed a different way (see "idea cards") | Fable / Opus | [built] |
| **Clusterer** | Groups similar ideas so each real idea is counted once | Sonnet | [built] |
| **Critics** | Question the best ideas three levels deep, imagine how each could fail, with the published failures for the part in hand; the idea's author answers once (reply round) | Opus | [built] |
| **Curator** | After each round, proposes additions to each part's memory; a script keeps only cited, new entries (`--no-memory` control) | the cheap model | [built] |
| **Justifier** | Checks the logic: start -> idea -> result, and whether the idea fits facts elsewhere in the tree | Opus | [planned] |
| **Prior-art scout** | Searches the web: is this idea already known? | Sonnet | [built] |
| **Builders** | Turn chosen ideas into working code | Opus | [built] |
| **Testers** | Run the objective check: quick test, then full test | the machine | [built] |
| **Router** | Decides per problem: converge (one right answer) or diverge (invent) | rules + probes | [planned] |
| **People** | Read everything, add opinions, vote, add problems | humans | [partly built: control.json adds nodes, skips parts, seeds mechanisms, vetoes or chooses the next question, adds opinions in Mode 3; no shared space yet] |

## How one research round flows

```
  problem
     |
     v
  [Mapper] ---> problem tree (parts, weak spots, questions)
     |
     v
  [Inventors x many] ---> 200+ idea sketches
     |                    (each session uses a different idea card)
     v
  [Clusterer] ---> ~100 distinct ideas
     |
     v
  [Critics] ---> top ideas questioned, failure modes listed
     |
     v
  [Justifier] ---> can we reason from the facts to this idea,     [planned]
     |             and from the idea to a result? does it fit
     |             the rest of the tree?
     v
  [Builders] ---> code for the chosen ideas
     |
     v
  [Testers] ---> quick test (minutes) ---> full test (hours)
     |                 |                         |
     |            drop losers               keep winners
     v
  [Prior-art scout] ---> new or known?
     |
     v
  results + new problems found ---> back into the problem tree
```

The loop never ends: every round leaves new problems in the tree for the next round.

## Idea cards (how inventors are pushed apart)

```
  same problem ---+--> card: "change the main choice"
                  +--> card: "flip an assumption"
                  +--> card: "unusual but valid angle"
                  +--> card: "borrow from a distant field" (seed word)
                  +--> card: "different viewpoint or form"
```

Each inventor first writes the obvious answer down, then is asked to go somewhere else.
NoveltyBench result (100 prompts, Haiku): 9.63 distinct answers of 10 against 3.18 for plain sampling and
8.28 for the paper's best prompting baseline; utility 5.90 against 3.13 and 6.16.

## The tree is a map, not a fence

A tree of named weak spots pulls every inventor toward the same spots, and a wrong fact in it
steers everyone into a dead end. Guards:

```
  inventors per round
  +---------------------------+----------------------------+
  |  ON THE TREE (about 60%)  |  OFF THE TREE (about 40%)  |
  |  one branch + idea card   |  blank: no tree at all     |
  |  "the tree is a map,      |  gaps: what did it miss?   |
  |   not an order"           |  doubt: which fact is wrong|
  +---------------------------+----------------------------+
                    |                         |
                    v                         v
                 ideas                     ideas + new branches,
                                           disputed facts
                              |
                              v
              yield logged per source -> next round shifts the share
```

1. Every inventor is told the tree is one reader's notes: ignore it, dispute it, or add to it.
2. A fixed share of inventors work off the tree (blank, gaps, doubt cards).
3. Wins are logged by source; if off-tree wins keep coming, the tree gets less weight next round.
4. Off-tree wins become new branches. A quiet branch is lowered in priority, never deleted.

The tree has up to four levels: parts, sub-parts, questions, helper questions [built, fix 8]. A failed
check with a reason becomes a question under its part, with the test that would answer it; an off-map
win hangs under the part it named. A node deeper than four is moved up to its depth-3 ancestor. The
full node schema is in docs/PROBLEM_TREE.md.

## What landed on 2026-10-17

Every addition is behind a flag with a control arm, because the research says each one helps only under
conditions and must be measured (research_notes/team_gaps/00_SYNTHESIS.md, docs/TEAM_GAPS_SPEC.md).

| Addition | What it does | Flag (default) and control arm | Status |
|---|---|---|---|
| Per-part memory (gap A) | One markdown file per part, read whole, kept across runs: facts, tried, priors, cues, open questions, failed framings. A curator proposes a delta after each round; a script keeps an entry only if it cites an artefact that exists and is not a near-duplicate. One context per part and round ignores the memory | on; `--no-memory` | [built] |
| Reply round (gap B) | The idea's author answers the pre-mortem once: concede and change, rebut with a quoted and tagged fact, or propose a measurement. The critic marks each objection resolved, revised or standing. At most two exchanges; nothing is dropped | on; `--no-dialogue` | [built] |
| Question picking (gap C) | From round 2 the team scores open questions (chance to resolve x gain x novelty / cost, with a learning-progress bonus; every few rounds the most novel wins) and gives the chosen question's part 2 extra contexts. Top 3 in next_questions.json; a person may veto or choose | on; `--no-pick-questions` | [built] |
| Fetch on demand (gap D) | A builder or reviser missing one fact writes a NEED line (at most 2) instead of code; the loop fetches each with a source and re-prompts once; a run never fetches the same question twice | on when the web is on; `--no-fetch-on-demand` | [built] |
| Evidence tooling (gap E) | NoveltyBench: interquartile mean per arm, paired bootstrap 95% intervals, re-judging with a second judge and an agreement check. A pre-registered bin-packing experiment: profile only, full loop, best-of-N, at an equal cap of scorer calls, with a dry mode | `python -m harness.noveltybench summary / rejudge / agreement`; `python -m nano.experiments.binpack_arms prereg / dry / run / report` | [built] |
| Preread (N3) | One reading call on the whole problem before the map | on; `--no-preread` | [built] |
| Seed words by function (N7) | Each seeded context on a part gets a different abstract function; distances mixed (about half far, a quarter mid, a quarter near); functions that led to new clusters are drawn more often; yield logged per function | `--seeds function` (default); `--seeds random` | [built] |
| Pre-mortem knowledge (N8) | The brief's published failures (with URLs) go into the critic's default pack. Optionally the critic asks up to three "has this failed or faded at small scale" questions, answered in one research call. report.json logs the share of objections the ladder later confirms | pack always on; `--premortem-web` (off) | [built] |
| Integrity layer (fix pass H) | The candidate trains in a child process under a Windows job object with one active process, secrets stripped, network and process calls refused, a read allowlist; the launcher counts the training tokens it reads and compares them with the report (2%); the exam reads the validation data and seals it before loading candidate code, and recounts non-embedding parameters from the weights | always on | [built] |
| Budget-matched plain arm (fix pass F) | The plain and climb arms build until the same token budget is spent, run the same controls and tuning sweep, and see the rules in canonical order | `--arm plain`, `--arm climb`; `--n-builds` 0 = spend to the budget | [built] |

The reply round in one drawing:

```
  critic: objections 1..n, each with "if true: <metric> <op> <number>"
     |
     v
  author (fresh call, sees the idea, its chain, the objections)
     |   per objection, exactly one move:
     |   concede -> CHANGE      rebut -> FACT [script|measured|web|belief]      measure -> TEST
     v
  critic marks each: resolved (a non-belief fact settles it) | revised (conceded) | standing
     |
     +--> standing with no test and something changed: one more exchange (at most 2)
     v
  builder gets every objection (revised or tested, never dropped); the ladder settles the tests
```

## Two modes, chosen per problem  [planned router]

```
                       problem
                          |
               a few quick plain attempts
                          |
            +-------------+--------------+
            |                            |
   attempts agree and pass       open-ended, or
   the check                     attempts fail / disagree
            |                            |
       CONVERGE                       DIVERGE
   (vote, simplest wins)     (idea cards, critics, tests)
```

Why: on single-answer puzzles (ARC) divergence did not help; on open problems
(model architecture, NoveltyBench) it is what wins.

## Where people come in  [planned]

```
   +-----------------------------------------------------------+
   |  SHARED SPACE                                             |
   |                                                           |
   |  Problem tree    Ideas board     Test results   Log       |
   |    + add a         + comment       + see           + see  |
   |      problem       + vote          numbers          who   |
   |                    + flag "known"                   did   |
   |                                                    what   |
   +-----------------------------------------------------------+
        ^         ^          ^
     person A  person B   person C   (any number, any time)
```

What a person can do:
1. **Add a problem** to the tree; the next round picks it up.
2. **Comment on an idea**; critics and the justifier read comments as evidence.
3. **Vote** to push an idea to the builders, or to drop it.
4. **Flag prior art** ("this is known, see paper X").

Rule: people steer and add knowledge; **tests decide**. A popular idea that loses its test is dropped.

## Results so far

| What | Result |
|---|---|
| Language-model architecture (21M model, same data and size) | 7.0% lower perplexity than the scaled-down frontier skeleton (1 training run) |
| NoveltyBench (Haiku, 100 prompts, same model both sides, Opus judges) | distinct answers of 10: method 9.63, paper's best baseline 8.28, plain 3.18; utility: 5.90 / 6.16 / 3.13 (each of our answers is about one point less polished; variety is what the team needs) |
| ARC puzzles (single right answer) | ties strong plain sampling: the honest limit, and why the router exists |

## Any problem, not only language models

The language-model loop was one test case. For the team to work on anything, each problem brings a profile
and the loop reads it:

```
  PROBLEM PROFILE
  +----------------------------------------------------------+
  | goal and success measure   (what number, which direction) |
  | parts                      (modules, steps, components)   |
  | may touch / fixed          (the boundary of an idea)      |
  | objective check            (a command that returns a score)|
  | measurements               (what is known about it now)   |
  +----------------------------------------------------------+
            |
            v
   mapper -> tree -> inventors -> critics -> builders -> testers
   (the same team; only the profile changes)
```

Status [built]: the loop reads a profile (`nano/profiles/<name>.py`, docs/GENERIC_SPEC.md). The
language-model profile is the first instance; bin packing (with and without a baseline) and a review-process
design question (no objective check, a blind judge panel) run through the same loop. Which profile key fills
which part of the problem statement is in docs/PROFILE.md.

## Things to decide next

- Which roles get which model (cost vs quality).
- How many inventors per round, and how many ideas reach the builders.
- How much weight people's votes get before tests run.
- What the shared space is built on (web app, shared document, database).
