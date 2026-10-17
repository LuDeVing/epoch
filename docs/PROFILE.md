# Where the problem statement comes from

Every agent reads `problem.md`. The loop writes it once per run in `NanoLoop.encode()` (nano/loop.py) from the
active profile (`nano/profiles/<name>.py`, loaded by `nano/profile.py`) and a few command-line flags. This page
says, part by part, which profile key or flag fills it. Checked against the code on 2026-10-17.

## The table

| Problem statement part | Profile key or flag | Where it is rendered |
|---|---|---|
| Heading | `title` (optional; falls back to vocab `score_phrase`, then `name`) | `# Problem: <title>`, first line of problem.md |
| GOAL | `goal` (required) | `GOAL: <goal>` |
| PURPOSE | `aim` (required, may be ""); the flag `--aim` overrides it for one run | `PURPOSE: <aim>`; the line is left out when both are empty |
| SCOPE OF THIS RUN: the parts that may change | flag `--only-nodes id1,id2` (ids of the default tree); no profile key | `SCOPE OF THIS RUN: only these parts may change ...` (`tree.scope_text`); left out when the flag is empty |
| SCOPE: each part's boundary | `tree[*].boundary` of the profile's default tree | one line per allowed part: `- <name>: <boundary>` |
| SCOPE: the parts that stay as they are | the other nodes of `tree`, named by `tree[*].name`; the word for the whole comes from vocab `recipe` | `the rest of the <recipe> (<names>) stays exactly as it is` |
| BASELINE, measured numbers (Mode 1) | `baseline_summary` (optional callable: baseline measurement -> line); without it the loop's own `_baseline_line` prints the quick and full score means and seed SD with vocab `score_name` | `BASELINE (measured): ...`. The numbers are measured by the checker (`checker`, `checker_args`) and cached under the folders named in `baseline_cache`; they are never typed into the profile |
| BASELINE, no baseline (Modes 2 and 3) | `mode` (or derived from `artifact.path` and `checker`), `artifact.interface`; Mode 3 also `checker_args.criteria`, `checker_args.judges`, `facts` | `BASELINE: none ...`, then `INTERFACE` (Mode 2) or `CRITERIA`, `FORM OF A PROPOSAL`, `KNOWN FACTS` (Mode 3) |
| HARD CONSTRAINTS C1..C7 | `constraints` (required list of strings, printed as written) | `HARD CONSTRAINTS:` then one line per item. The same list goes into every prompt built by `_common`, shuffled per call where the caller asks for it (idea contexts) and in canonical order otherwise |
| The verdict bar | `score` (`margin`, `alpha`, `min_seeds`, `unit`, `direction`, `stackable_margin`, `stackable_alpha`) | not in problem.md: `constraints.json` `bar.rung_full`, which the builders and the report read |

Related keys that agents read next to problem.md, not inside it: `assumptions` (transform material),
`tree` (frame, assumptions, boundary per part; see docs/PROBLEM_TREE.md for the node schema), `boundary_all`
(the boundary of the root and of promoted wins), `lenses`, `directions`, `off_map`, `vocab`, `docs` (digest and
reference file), `diagnostics`, `memory_dir` (per-part memory folder) and `judge_model` (Mode 3).

## Not yet configurable

- **Scope has no profile key.** It is set only by `--only-nodes`, per run. A profile cannot declare a default
  scope. `scope_text` reads the profile's default tree, not the planner's map, so a renamed or split part is
  named as the default part.
- **The measured baseline numbers inside the constraint text are typed by hand.** The LLM profile's C3 says
  "21.24M" in the string; nothing recomputes it from the baseline measurement.
- **The constraints are free text.** The loop does not check that the C7 text matches `score`. Today the LLM
  profile's C7 still describes the retired rule ("a one-sided Welch test at p < 0.01"), while the verdict uses
  the e-value rule (docs/VERDICT.md). The bar in `constraints.json` is built from `score` and is correct.
- **The PURPOSE has no per-run file.** It is the profile's `aim` or the `--aim` string; there is no
  `--aim-file`.
</content>
</invoke>
