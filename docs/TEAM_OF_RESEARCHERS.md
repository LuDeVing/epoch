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
| **Mapper** | Reads the problem and its measurements, draws the problem tree: parts, weak spots, open questions | Sonnet | [built] |
| **Inventors** | Many separate idea sessions, each pushed a different way (see "idea cards") | Fable / Opus | [built] |
| **Clusterer** | Groups similar ideas so each real idea is counted once | Sonnet | [built] |
| **Critics** | Question the best ideas three levels deep, imagine how each could fail | Opus | [built] |
| **Justifier** | Checks the logic: start -> idea -> result, and whether the idea fits facts elsewhere in the tree | Opus | [planned] |
| **Prior-art scout** | Searches the web: is this idea already known? | Sonnet | [built] |
| **Builders** | Turn chosen ideas into working code | Opus | [built] |
| **Testers** | Run the objective check: quick test, then full test | the machine | [built] |
| **Router** | Decides per problem: converge (one right answer) or diverge (invent) | rules + probes | [planned] |
| **People** | Read everything, add opinions, vote, add problems | humans | [planned] |

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

The tree has up to four levels: parts, sub-parts, questions, helper questions; tested ideas and
their results hang under the question they answered. Deeper than four starts a new tree.

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

Status: the cards, clustering, critics, selection, scout, budget and logs are general or nearly so;
the tree, lenses, planner, direction texts, builders and testers are written for a training script
and need the profile version. The language-model profile becomes the first instance.

## Things to decide next

- Which roles get which model (cost vs quality).
- How many inventors per round, and how many ideas reach the builders.
- How much weight people's votes get before tests run.
- What the shared space is built on (web app, shared document, database).
