# Epoch

A team of AI researchers that works with you.

You give it a folder about a problem: notes, data, what was tried, open questions. It draws a map of the problem,
invents ideas for every part, groups them, argues them out with critics, builds the best into proposals, judges them
blind, and tells you what it found and what to test next. People join the same space, add findings and files, steer
the next round, and each has an agent that explains what the team changed.

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

## Run it on Windows

Needs Python 3.12 or newer and the Claude CLI signed in (or an Anthropic API key in `ANTHROPIC_API_KEY`).
Everything else is in the standard library.

1. Double-click `Epoch.bat`, or run `scripts\install_shortcut.ps1` once for an Epoch shortcut on the Desktop and in
   the Start Menu.
2. The dashboard opens in its own window. Create an account, make a space, press Start a research, pick a folder.
   The two folders in `examples/` are ready to try.
3. Spaces, runs, accounts and the team's memory live in a lab folder: `D:\AGI-lab` when it exists, otherwise
   `AGI-lab` next to this folder, made on first start.

`pip install -r requirements.txt` adds the API backend and the harness tooling; `requirements-ml.txt` is for the
built-in language-model problem (needs a GPU); `requirements-dev.txt` for the tests.

## Where things are

- `space/`: the shared space server, the hub (dashboard), the launcher of research runs, accounts, files, knowledge.
- `space/web/`: the pages.
- `nano/`: the research loop and the problem profiles.
- `harness/`: the model calls, the lab root, the benchmark script.
- `docs/`: how a run works (`HOW_IT_WORKS.md`), the team design (`TEAM_OF_RESEARCHERS.md`), the space and the page
  (`SPACE.md`, `MULTIPLAYER_DESIGN.md`), the model result (`RESULTS_FRONTIER_MODEL.md`), the demo runbook.
- `examples/`: research folders to try, and bundled spaces.
- `research_notes/`: the reading behind the design, twelve fields and their syntheses.
- `llmcandidates/`: the final models of the architecture result.
