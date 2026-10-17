# Fix pass 2026-10-17: rules for every fix agent

Backlog: C:\Users\User\.claude\projects\C--Users-User-Desktop-AGI\memory\review-findings-2026-10-17.md (134 findings,
sections A-I, line numbers as of commit 8f02ccb; re-verify every line before editing) plus the owner's new items in
this file. Research notes that decide what is allowed: research_notes/ (idea_generation, creative_genius,
thinking_modes, selection_cost, team_gaps, portfolio_improvements, noveltybench) and docs/VERDICT.md, docs/GENERIC_SPEC.md,
docs/TEAM_OF_RESEARCHERS.md, docs/mapper/.

Rules for every agent:
1. Own worktree and branch; edit only the files in your ownership row; never the main checkout.
2. For each finding: re-verify it in the current code; if it is a judgment call, check the web for the current best
   practice (primary sources, numbers) and check research_notes/ for a note that already settles it. Fix what the
   evidence supports. Skip, with one sentence why, anything a research note argues against. Never "fix" by weakening a
   check or a test.
3. Load: the owner's PC crashed when eight agents ran dry runs at once. At most ONE mock dry run at a time
   (`python -m nano.dry_run --profile binpack_nobase --implement 2 --rounds 1 --max-sketch-calls 8`), never a GPU run,
   never a real model call, never the whole harness/tests folder; run only your own test file plus the specific
   failing tests you were given.
4. Environment: Windows; python D:\AGI-lab\.venv\Scripts\python.exe; env HTSA_LAB_ROOT=D:/AGI-lab; tests must not
   write into the real lab root (use tmp_path) and must not need the GPU.
5. Plain English in prompts and docs, short sentences, no em-dashes. Keep diffs focused; no reformatting.
6. Commit on your branch. Report under 350 words: findings fixed (ids), findings skipped (ids + reason), files, tests
   and results, merge notes (which shared lines you touched).

Owner's new items (from the owner, 2026-10-17):
- N1 settings: the problem statement parts (GOAL, PURPOSE, SCOPE OF THIS RUN with the parts that may change and their
  boundaries, BASELINE measured numbers, HARD CONSTRAINTS C1..C7) must all be configurable in the profile, not scattered.
- N3 research before decomposition: a reading round on the whole problem before the planner draws the map, then the
  per-part research as today; decide from the literature on literature-informed decomposition.
- N4 node schema: rework the documented table (frame / assumptions / boundary) to the full current schema.
- N7 seed words: the "seeded" idea card uses a random seed word; make the choice better than random without making it
  near-domain (research_notes/idea_generation/02_analogy.md and 00_SYNTHESIS.md: avoid "farther is always better";
  working labs use near-domain analogies; variety across contexts matters).
- N8 pre-mortem knowledge: (a) free fix: put the research brief's "did not help" entries for the part into the critic's
  default pack; (b) flag: let the critic ask up to three questions of the form "has <mechanism> been reported to fail
  or fade at small scale or under <condition>", answered by the research model with URLs, then write; (c) measure: log
  per run the share of objections the ladder later confirms, so the two can be compared.
- N10 ladder: hedge lane (late-bloomer audit) on by default at the research's 10-15%; long-shot share doc/code mismatch.
