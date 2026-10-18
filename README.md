# Epoch

A team of AI researchers that works with you. You give it a folder about a problem: notes, data, what was tried,
open questions. It draws a map of the problem, invents ideas for each part, groups them, argues them out with
critics, builds the best into proposals, judges them blind, and tells you what it found and what to test next.
People join the same space, add findings and files, steer the next round, and talk to their own agent.

## Run it on Windows

Needs Python 3.12 or newer and the Claude CLI signed in (or an Anthropic API key in `ANTHROPIC_API_KEY`).
Everything else is in the standard library.

1. Double-click `Epoch.bat`, or run `scripts\install_shortcut.ps1` once for an Epoch shortcut on the Desktop and in
   the Start Menu.
2. The dashboard opens in its own window. Create an account, make a space, press Start a research, pick the folder.
3. Spaces, runs, accounts and the team's memory live in a lab folder: `D:\AGI-lab` when it exists, otherwise
   `AGI-lab` next to this folder, made on first start.

The space `agent-long-tasks` comes with the repository as an example: a finished run on why coding agents fail on
long tasks, with its map, ideas, arguments, two judged proposals and the report. Its folder of inputs is
`examples/agent-long-tasks`; what the team found is in `examples/RESULTS-agent-long-tasks-2026-10-18.md`.

## Where things are

- `space/`: the shared space server, the hub (dashboard), the launcher of research runs, accounts, files, knowledge.
- `space/web/`: the pages.
- `nano/`: the research loop and the problem profiles.
- `docs/`: the design notes (`docs/SPACE.md` for the space, `docs/MULTIPLAYER_DESIGN.md` for the page).
- `examples/`: research folders to try, and bundled spaces.
