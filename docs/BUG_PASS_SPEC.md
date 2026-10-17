# Bug pass 2026-10-17 (night): rules for every bug agent

Context: today 27 branches merged into master (8 fixes, 5 gap additions, 14 fix-pass branches). Merge seams are
where bugs hide: two features touching the same function, a helper renamed on one branch and still called by its
old name on another, a flag added in argparse but never read, a field written under one key and read under another,
a test fixture that passes only because it stubs the thing that is broken. The full suite passes (458), so look
for what tests do not cover.

Rules:
1. Own worktree and branch; edit only the files in your ownership row.
2. Read your files in full first. Then hunt: (a) run `python -m pyflakes <files>` if available, else
   `python -m py_compile` and a grep for names defined on no branch; (b) trace every flag in argparse to a read;
   (c) trace every report.json / state.json / problem_tree.json key written to a reader; (d) check every call site
   of a function changed today (`git log --since="1 day" -p -- <file>` shows the diffs); (e) run the relevant
   existing test file and read what it does NOT assert; (f) exercise the error paths (empty inputs, missing files,
   a failing model call, a mock reply in the wrong format).
3. A bug is: a crash, wrong logic, a silent no-op, a wrong number, a key mismatch, a resource leak, an unsafe
   default. Not a bug: style, naming, a design choice a research note backs (docs/ and research_notes/), or a
   behaviour a test locks on purpose. When unsure, report it instead of changing it.
4. For every bug: a failing test first (in your harness/tests/test_bug_<area>.py), then the smallest fix, then the
   test passes. No refactors, no reformatting, no behaviour changes beyond the fix.
5. Load: at most ONE mock dry run at a time (`python -m nano.dry_run --profile binpack_nobase --implement 2
   --rounds 1 --max-sketch-calls 8`), never GPU, never real model calls, never the whole tests folder; run your
   own test file plus the existing files for your area one at a time.
6. Environment: Windows; python D:\AGI-lab\.venv\Scripts\python.exe; env HTSA_LAB_ROOT=D:/AGI-lab; tests use
   tmp_path, never the real lab root. Plain English, short sentences, no em-dashes.
7. Commit on your branch. Report under 350 words: bugs found (file, function, what was wrong, severity), bugs fixed,
   bugs reported but not fixed (and why), tests and results, merge notes.
