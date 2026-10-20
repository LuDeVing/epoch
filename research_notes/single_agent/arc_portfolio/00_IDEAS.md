# Improvement ideas for the portfolio method (before web search)

Context: ARC-AGI-1, 36 mid-difficulty puzzles, Haiku medium effort. Method 33/36, plain one answer 31/36, any attempt
right 34/36. Method won 3 (two by extra attempts + example check, one by revision), lost 1 (popular wrong reading
outvoted the right one), won 1 on a tie-break. 4 puzzles had programs passing every example but wrong on the test.
Tokens: about 50k per puzzle vs about 22k for one plain answer.

## Generation
1. Adaptive budget: stop as soon as any two passing attempts agree; add attempts only while passing groups disagree
   (Adaptive-Consistency style).
2. Vary the presentation per attempt: rotate/transpose/recolour the whole puzzle, reorder examples, then map the
   answer back (augmentation at prompt time, as ARC Prize winners do).
3. Escalate effort, not just count: medium first, high only on puzzles where attempts disagree or fail.
4. Rule in words first, then code (Hypothesis Search): several natural-language rules, code only the best.
5. Revision also when passing programs disagree, not only when none pass; more than one round on near misses.
6. Evolution-style refinement: keep the best programs, mutate and recombine them over several rounds.

## Checking
7. Leave-one-out: give the model all examples but one, check the program on the held-out one. Rules that generalise
   to an unseen example are more likely to generalise to the test.
8. Symmetry consistency: if the examples are unchanged in form under rotation/mirroring, a correct program should
   commute with it: transform(rot(x)) == rot(transform(x)) on the examples and the test.
9. Discriminating inputs: when rival programs disagree, construct inputs where they differ and ask which output fits
   the examples' pattern (Platt's crucial experiment; CodeT-style generated tests).
10. Direct prediction as a second witness: also ask for the test output directly (transduction) and prefer programs
    whose output agrees with it (induction + transduction).

## Selection
11. Justification check (user's idea): derive each rival rule from the examples and the test answer from the rule,
    compare rivals at the point of disagreement; weaker chain loses.
12. Problem-tree / consilience check (user's idea): list every detail of the examples; the rule that explains the most
    with no contradictions wins.
13. Weighted vote: plain attempts count more than inventive ones; inventive attempts only fill in when no plain passes.
14. Simplicity score beyond program length (description length, number of special cases).
15. Two answers: ARC's official scoring allows two attempts per test; submit the top two groups (baseline gets two
    samples too, for fairness).
16. Group by test answer first, use augmented outputs only as a tie-break.

## Fairness of the comparison
17. Equal-token baseline: plain best-of-n with the same example check at the same token budget.
