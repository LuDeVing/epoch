# Critique: reasoning and problem solving (field 03)

## What is solid
- Correct first answers are common in human two-response studies (Bago and De Neys, Ghasemi, Raoelison). This matches our data: first natural answers are mostly right on puzzles. It argues for trust by default, with a trigger to check.
- Long reasoning is not free. A meta-analysis (Sprague) and the overthinking results say: gate deliberation by task type and difficulty.
- Two replication failures (disfluent fonts, unconscious thought) warn against folk tricks.

## What is weak
- Only 8 of 25 claims are marked established (two or more credible sources), and some of those are one lab. Most lines are snippet level. Credibility scores on snippet lines are guesses.
- Several "independent" counts are one lab: Bago and De Neys (three lines), Valmeekam and Stechly (planning), Stanovich and West, Klahr and Schunn. Real independence is lower than the count.
- The 36.3 point chain-of-thought harm rests on one paper, and it compares two different models.
- The two 2026 calibration preprints have no known authors. Do not rely on them.
- Many LLM results are preprints. The Illusion of Thinking collapse is disputed.

## Contested, and why it matters
- Dual process: the strict two-system split is under attack. Use "check when signals conflict", not "fast module then slow module".
- Insight as sudden restructuring, and the claim that talking hurts insight, are both mixed. Do not add a "stop and incubate" step.
- Mental-model theory has no direct LLM test of a counterexample step. The REFUTE result says models are poor at building counterexamples unaided.

## Human data that may not transfer
- Student samples, trap items built to fool people, time pressure. Trap items make the intuitive answer wrong on purpose (about 20% correct), which says nothing about real base rates.
- Klahr and Dunbar had 20 and 10 adults.
- Feeling of rightness has no direct machine twin. Our proxies (agreement across samples, token probability) are correlated within one model, and one preprint says self-consistency amplifies systematic errors.

## Missing, and it would change the design
1. Direct LLM tests of check-when-conflict routing: does agreement or low confidence decide when to spend effort, and does it beat always-check at equal tokens? This is our central router question. No source here answers it.
2. Verifier-gated revision versus self-review across domains (code, math), not only planning.
3. Decomposition and subgoaling in LLMs (least-to-most, plan-then-solve) with equal-token controls. Only Tree of Thoughts appears, on one task.
4. Analogy and transfer from past solved problems (Gentner, Holyoak). Bears on our lesson ledger.
5. Expert problem representation (Chi: physics experts versus novices). Likely relevant to a restate-the-problem step.
6. Worked examples and self-explanation (Chi, Renkl).
7. Metacognition and abstention: can a model know it does not know.

## Memory or snippet only
Claims 3 to 7, 9 to 11, 16 to 25 include snippet or memory lines. Line a-22 is memory. Treat these as leads to open before use.

## Risk for the project
This field leans toward "trust first, doubt on conflict". Our open-ended wins came from forced divergence, which this field does not directly support. Keep the router split: single-answer puzzles trust first and let a real check decide; open tasks diverge.
