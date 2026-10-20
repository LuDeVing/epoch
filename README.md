# Epoch

A team of AI researchers that works with you.

You give it a folder about a problem: notes, data, what was tried, open questions. It draws a map of the problem,
invents ideas for every part, groups them, argues them out with critics, builds the best into proposals, judges them
blind, and tells you what it found and what to test next. People join the same space, add findings and files, steer
the next round, and each has an agent that explains what the team changed.

## Run it on Windows

> **You need two things on the PC:**
> 1. **Python 3.12 or newer** from [python.org](https://www.python.org/downloads/), installed with **"Add Python to PATH"** ticked.
> 2. **The Claude CLI signed in** (`claude` on the PATH), or an Anthropic API key in the environment variable
>    `ANTHROPIC_API_KEY`. This is only for starting new research; opening the bundled example needs no model at all.
>
> Everything else is in the Python standard library. Edge or Chrome, which Windows has, draws the window.

1. Download and unzip, or clone.
2. Double-click `Epoch.bat`. The hub starts, a lab folder named `AGI-lab` appears next to the unzipped folder, the
   example space installs into it, and the dashboard opens in its own window. Or run `scripts\install_shortcut.ps1`
   once for an Epoch shortcut on the Desktop and in the Start Menu.
3. Create an account, open the example space `agent-long-tasks`, or make a space, press Start a research and pick
   a folder. The two folders in `examples/` are ready to try.

Spaces, runs, accounts and the team's memory live in that lab folder (`D:\AGI-lab` is used instead when it already
exists). `pip install -r requirements.txt` adds the API backend and the harness tooling; `requirements-ml.txt` is
for the built-in language-model problem (needs a GPU); `requirements-dev.txt` for the tests.

## The idea in short

AI agents know a great deal and come up with very little. Ask one for ideas and you get the obvious ones; ask again
and you get the same ones in different words. In one 2024 study a model produced four thousand research ideas that
collapsed to about two hundred distinct ones. Our working explanation: a model thinks in a line, one token after the
next, and the likely continuation of an idea is the obvious idea.

People who invent well do not think in a line. They have schemas, habits of directing thought that the sciences of
invention have studied for decades: experts represent a problem by its deep structure (Chi, Feltovich and Glaser,
1981); an example seen first narrows what you produce (Jansson and Smith, 1991); mapping two analogues explicitly
doubles transfer (Gick and Holyoak, 1983); people who invent alone and pool afterwards beat a group talking (Diehl
and Stroebe, 1987); and the returns on ideas are fat-tailed, so the job is to find the best, not the average.

So we read twelve fields that study how new ideas arise, took what held across them, and built that schema as a
fixed script. Many separate agents, each with a narrow job; a plain program decides every step, the agents only fill
in the pieces:

1. **Measure, then read.** The baseline is measured before any idea exists; a reading call reports how the field
   splits the problem and where it is weak, never fixes.
2. **Map.** One call draws a tree of parts, each with how it works today and the assumptions a different approach
   could remove.
3. **Invent alone.** Each part gets its own idea agents, each pushed in a different direction by a card: change the
   main choice, flip an assumption, take an unusual angle, borrow from a distant field through an explicit mapping,
   port a known technique, remove something, doubt the map. They never see each other's output. About 40 percent
   work off the map, so a wrong fact in it gets disputed instead of steering everyone into one dead end.
4. **Group.** Ideas are clustered by mechanism, not wording.
5. **Argue.** Critics attack the chosen ideas three levels deep; the author answers once with a fact, a change or a
   test. An answer never blocks a build. The test decides.
6. **Build and test.** A ladder of cheap tests, pre-registered rules, placebo candidates and known winners through the
   same ladder, so the verifier cannot be gamed and a false positive has a measured rate.
7. **Remember.** What each part taught is written down and read first by the next run.

The research behind each rule, with sources, is in `research_notes/`.

## How the ideas are made

We read twelve fields that study where new ideas come from and kept what held across them. Six findings shaped the
idea step more than anything else.

- **One model is one voice in many costumes.** Four thousand research ideas from a model collapsed to about two
  hundred distinct ones, and asking it to "be creative" barely moves the count
  ([Si, Yang and Hashimoto, 2024](https://arxiv.org/abs/2409.04109); [Peeperkorn et al., 2024](https://arxiv.org/abs/2405.00492)).
  So no inventor sees another's output, each gets its own part and its own card, and ideas are grouped by mechanism
  before anyone counts them.
- **Invent alone, pool later.** People who generate ideas on their own and pool them afterwards beat a group
  talking, every time it has been measured ([Diehl and Stroebe, 1987](https://doi.org/10.1037/0022-3514.53.3.497);
  [Mullen, Johnson and Salas, 1991](https://doi.org/10.1207/s15324834basp1201_1)). Exposure to others' ideas comes late,
  and only as measured outcomes.
- **An example seen first is a cage.** Designers shown a sample solution copied its features, flaws included
  ([Jansson and Smith, 1991](https://scholarhub.vn/publication/Design-fixation/7e0675c7-19b8-42c9-96c3-7bcb6e636812)).
  So the reading step reports structure and weak spots, never fixes, and 40 percent of inventors work with no map at
  all, so a wrong fact in it gets disputed instead of followed.
- **Analogy works only when the mapping is written down.** Unaided, people notice a far analogy about a third of the
  time; comparing two analogues and writing the shared schema doubles transfer
  ([Gick and Holyoak, 1983](https://www.gwern.net/doc/psychology/1983-gick.pdf); [Gentner, 1983](https://groups.psych.northwestern.edu/gentner/papers/Gentner83.pdf)).
  The analogy card assigns a distant source and demands a typed mapping that a script checks.
- **Nobody can rank ideas from their text.** The best model judge agreed with human reviewers 53 percent of the
  time, against 56 percent between the humans, and ideation scores barely predict what happens when the idea is
  executed ([Si et al., 2025](https://arxiv.org/abs/2506.20803)). So tests rank; where no test exists, a blind panel
  does, and every proposal must name the test that would settle it.
- **Returns are fat-tailed, and the verifier will be gamed.** At Bing, 2 percent of ideas produced 75 percent of
  the gains ([Kohavi et al., 2014](https://www.exp-platform.com/Documents/2014%20experimentersRulesOfThumb.pdf)), and
  every automated search that reports its failures reports verifier exploits
  ([AlphaEvolve, 2025](https://arxiv.org/abs/2506.13131)). So ideas climb a ladder of cheap tests, many get few samples
  each, and placebo candidates and known winners go through the same ladder so a false positive has a measured rate.

One more thing the field agrees on: clever prompting does not beat plain prompting
([Hernandez et al., 2012](https://peer.asee.org/experimental-assessment-of-triz-effectiveness-in-idea-generation.pdf)).
So the structure went into what the agents are given and how their output is tested, not into the wording of their
instructions. Each card is one short push, and every inventor writes the obvious answer first, then is asked to go
somewhere else.

## Does it work?

**The thinking alone.** On NoveltyBench, a public benchmark where a model answers each creative prompt ten times and
judges count how many answers are genuinely distinct and how good they are, the same small model (Claude Haiku) went
from 3.18 distinct answers of 10 to 9.63, and from 3.13 to 5.90 in judged usefulness, for about 13 percent more
tokens. Paired over the 100 prompts it was better on 98 and worse on none.

**As a research team.** We pointed it at the dense skeleton of the strongest open language models of 2026
(DeepSeek-V4 and Kimi K3) scaled down to 21 million parameters, trained from scratch on one laptop GPU, and asked
for a better architecture at the same parameters, data and training. The team produced 275 sketches, grouped them
into 139 clusters, argued 10 three levels deep and chose 19 to build. People built and quick-tested them; the winners
combined lowered the held-out loss from 4.0939 to 4.0212: **1.8 percent lower loss, 7 percent lower perplexity**,
about twenty times the seed spread. Four of the winning ideas are the team's own variants of published mechanisms,
written for this skeleton's four-stream design; the largest, a depth delay line, came from a sketch the automatic
selection had not even picked. One seed, one scale: a reason to try more, not a proof.

The complete record of that run, every sketch, prompt, critic chain, candidate file, quick test and reference run,
is its own repository: **[epoch-architecture-run](https://github.com/LuDeVing/epoch-architecture-run)**.

**On a folder of notes.** The space `agent-long-tasks` comes bundled with this repository: a finished run on why
coding agents fail on long tasks, from eight files of notes. Its map, 50 ideas, 60 objections and two judged
proposals are there to click through; what the team found is in `examples/RESULTS-agent-long-tasks-2026-10-18.md`.

## Where things are

- `space/`: the shared space server, the hub (dashboard), the launcher of research runs, accounts, files, knowledge.
- `space/web/`: the pages.
- `nano/`: the research loop and the problem profiles.
- `harness/`: the model calls, the lab root, the benchmark script.
- `docs/`: how a run works (`HOW_IT_WORKS.md`), the team design (`TEAM_OF_RESEARCHERS.md`), the space and the page
  (`SPACE.md`, `MULTIPLAYER_DESIGN.md`), the model result (`RESULTS_FRONTIER_MODEL.md`), the demo runbook.
- `examples/`: research folders to try, and bundled spaces.
- `research_notes/`: the reading behind the design, grouped by topic; `research_notes/README.md` is the index.
- `llmcandidates/`: the final models of the architecture result.
