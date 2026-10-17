# Portfolio method v2: what to change (ideas + web research + offline replay)

Sources: 00_IDEAS.md, 01_arc_methods.md, 02_selection_verification.md, offline replay (harness/portfolio_offline.py) of
the arc1mid-portfolio batch (36 ARC-1 puzzles) and arc2-portfolio (2 ARC-2 puzzles). No model calls in the replay.

## Offline replay on the same candidates (36 ARC-1 puzzles)

| Selection rule | Solved |
|---|---|
| Recorded method (largest group on test + augmented outputs) | 33 |
| Group by test answer / plain-weighted / plain only | 33 |
| Symmetry consistency first, then votes, then shortest | 34 (= upper bound, any attempt right) |
| Plain one answer / plain two answers | 31 / 33 |

Symmetry consistency: run the program on rotated/mirrored copies of the example and test inputs; count the symmetries
under which its outputs rotate/mirror along (f(s(x)) == s(f(x)) on every input). Passing right programs: mean 3.4 of 6;
passing wrong: mean 1.5, six of eight at 0. It fixed all three observed vote failures (ARC-1 1da012fc, 94be5b80 tie,
ARC-2 7b5033c1) and broke none. Found by looking at failures: needs fresh puzzles to confirm.
Closest literature: augmentation scoring (Franzen et al., Product of Experts: top-2 62.5% -> 67.6%), behaviour
clustering (AlphaCode, MBR-exec, CodeT).

## v2 changes, ranked by evidence and cost

1. Selection: symmetry consistency first, then group size, then shortest program; reject outputs equal to the test
   input (Greenblatt). Free.
2. Two answers, as the official ARC rules allow: submit the top two groups. Free. Baseline gets two answers too.
3. Early stop when any two passing attempts agree (Adaptive-Consistency: up to 7.9x fewer samples, <0.1% loss).
4. Anchored justification check (user's idea, in the form research supports): only when top groups are still tied,
   find the test feature where rival programs disagree, have the model derive the expected output there from the
   examples before seeing the candidates' outputs, then pick the group that matches. Unanchored judging is unreliable
   (Huang et al. 2023); anchored to a discriminating input it is the best-supported form.
5. Keep revision from real diffs when nothing passes (Greenblatt: 37% -> 50% with one round); add a second round only
   for near misses.
6. Inventive attempts stay as a safety net; with symmetry-first selection they no longer outvote right answers.

## Validation plan
Fresh ARC-1 mid puzzles (not the 40 used here), v2 against plain at equal tokens (plain best-of-n with the same
example check and two answers), report every puzzle.
