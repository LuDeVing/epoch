# Critique: metacognition and learning science

## What is solid
- Self-correction without outside feedback fails (Huang, Kamoi). The fix is a real signal: tests, tools, or a located error (Tyen). This matches our always-doubt loss on single-answer tasks.
- Overthinking is shown by eight groups. Plain answers beat long reasoning on easy items. Parallel paths with a vote beat longer thinking (Ghosal).
- CoT text is an unreliable witness (Turpin, Chen). A model's explanation of why it is confident is weak evidence.

## What rests on memory or snippets only
- All learning-science numbers: Rowland g 0.50, Bisra 0.55, Sinha and Kapur, Barbieri 0.48, Dunlosky, Kalyuga, Chi, Nelson and Narens, Thompson. None was opened. Publisher pages were blocked.
- Sinha and Kapur is a snippet, with a hostile opinion post as the only counterweight.
- MetaCrit (b-14) is abstract only.

## What could be wrong
- Most LLM evidence is preprints from 2024 to 2026. Several are single-author or small (Cacioli n=20 models, Cao harness).
- The Cao harness gain (48.3 to 56.9) is the most useful result for us and the weakest: no cost data, pooled across benchmarks, one model. It may be a gain from extra calls, not from metacognition. Do not build on it before a cost-matched rerun.
- Kadavath (calibrated) and Xiong (overconfident) look opposed. They measure token probability versus stated confidence, on different model generations. No source settles which signal current Claude models should use.
- Kamoi partly reviews Huang's literature, so "established" for self-correction is two views of one body of work.
- Human findings (feeling of rightness, testing effect, productive failure) concern people who forget and have limited memory. An LLM does not forget between calls. Retrieval practice and spacing may not transfer. Self-explanation is already close to CoT.
- Semantic entropy needs samples, and our samples are correlated, so it misses consistent errors. Farquhar says so.

## Missing, would change agent design
- Task-type routing evidence: any study that predicts, before solving, whether a task is open-ended (diverge) or single-answer (trust first). Our data says this split decides everything. The field gives only a weak pre-solve signal (P(IK) generalises partly).
- Cost-matched comparisons: scaffold versus best-of-N at equal tokens.
- Lesson memory: does storing past lessons (Reflexion style) help without external feedback, and does it go stale or mislead?
- Adaptive stopping rules for sampling: when to stop drawing samples.
- Expertise reversal in LLMs: does a worked example hurt a strong model on tasks it already solves? No test found.
- Calibration of the newest Claude models, not 2022 models.

## Bottom line
Safe to build on: use outside verification, scale effort to difficulty, default to the first answer on single-answer tasks, distrust the model's own stated reasons. Treat everything else as a hypothesis to test in our own harness.
