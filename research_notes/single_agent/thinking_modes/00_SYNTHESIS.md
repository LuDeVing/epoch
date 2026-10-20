# One method that can both converge and invent: synthesis

Sources: `01_convergent_divergent.md` (psychology), `02_simplicity_logic.md` (philosophy and logic of discovery),
`03_ai_routing.md` (AI strategy selection), `../thinking_schema/00_REPORT.md` (earlier schema research), and our own
measurements from 2026-10-13 to 2026-10-16. [V] = source checked on the web by the research agents; [M] = from memory;
[ours] = our own data; [design] = a choice with no direct evidence, to be tuned.

## What we measured, and why it forces this design

- Open-ended design (improving a language-model architecture): divergent cards produced the winning ideas (delay line,
  signed reads), filtered by an objective evaluator (training runs). Result: 7.0% lower perplexity than the scaled-down
  frontier skeleton. [ours]
- Single-answer puzzles (ARC-AGI-2): a plain direct attempt was right 56% of the time on puzzles plain Haiku solves; the
  divergent cards 12-31%. The method lost to plain Haiku in every version. [ours]
- The literature agrees on the shape: divergence pays off where an automatic evaluator prunes wrong ideas (FunSearch,
  AlphaEvolve, MAP-Elites [V]); on verifiable single-answer tasks, breadth of natural samples plus a verifier is what
  scales (Large Language Monkeys, AlphaCode [V]). No study tests seed-word or assumption-flip prompts on single-answer
  tasks; our ARC numbers are the evidence. [V] gap
- Expert humans first classify a problem by its deep structure (Chi, Feltovich & Glaser 1981 [V]); intuition is
  trustworthy in regular, learnable environments (Kahneman & Klein 2009 [V]); fixation research measures loss of
  variety, not of correctness (Jansson & Smith 1991 [V]).

The conclusion: one method, two modes, and a router in front. Not one fixed procedure for everything.

## The design

### Step 0. Classify the problem (cheap, revisable)

Free signals, no model call: is there an objective check (examples, tests, a training run)? Is the answer space small
and exact (a grid, a letter, a number) or open (a design, an idea)? [03, design]

Probe: four to five natural, direct attempts at normal effort. Measure agreement (how many give the same answer) and,
where a check exists, how many pass it. This is the AI version of the feeling of rightness (Thompson et al. 2011 [V];
Adaptive-Consistency, semantic entropy [V]).

The type is a probability that is updated during the run, not a label fixed at the start (01, rule 9).

### Step 1. Route

| Situation | Mode |
|---|---|
| A probe attempt passes the check | **Converge and finish**: vote among passing attempts, simplest wins ties |
| None pass, but the probes agree | **Converge with revision**: revise the shared reading using the actual check output (Self-Debug, Reflexion [M]); add a small divergent slice (about 20%) [design] |
| None pass and the probes disagree | **Escalate**: ladder below |
| No objective check and the answer is open-ended | **Diverge-then-converge cycles** (Geneplore, Basadur [V/M]), only with an evaluator to prune; keep a plain baseline as a floor |

### Step 2. The escalation ladder (graded, not a mode flip)

From 01 (rules 4-5) and Ohlsson's impasse theory [V, secondary]:

1. Re-check: run the candidates again against the evidence, including cases where they should fail.
2. Resample: more natural attempts.
3. Re-read: restate the problem in other terms (objects, lines, regions, counts, symmetry): a change of
   representation, not a tweak of details.
4. Pose helper problems: a special case, a simpler version, work backwards from the goal, drop one condition
   ("what if not?") (Polya; Silver 1994 [V]; Brown & Walter [M]).
5. Only then diverge strongly: assumption flips, analogies, seed words, plan-level diversity (PlanSearch [V]).

### Step 3. The thinking procedure inside each attempt (convergent mode)

Combining 02 and the earlier schema research; each step with its source:

1. Restate the task in its own words and write what makes an answer correct. (Polya [M]; Chi 1981 [V])
2. Study every example: what changes, what stays, how examples differ from each other. (Chi 1989 [M])
3. Write two to four candidate rules in plain words before any code. (Hypothesis Search [M]; strong inference, Platt 1964 [V])
4. Check the first rule against every example; doubt it only if the check fails. (Klayman & Ha 1987 [V]; 01 rule 2)
5. Write one rival rule that also fits, and the input on which the two disagree; decide with that input.
   (Platt's crucial experiment [V]; consider-the-opposite, Lord, Lepper & Preston 1984 [V])
6. Prefer the simpler rule as a default that clear evidence overrides. (Lombrozo 2007 [V]; size principle,
   Tenenbaum & Griffiths 2001 [V]; MDL [M])
7. Implement, run, revise from the real outputs, not from opinion. (Self-Debug, Reflexion [M]; Huang et al. 2023 on
   self-correction without feedback [M])
8. Stop when good enough. (Simon, satisficing [M])

### Step 4. Selection (both modes)

1. Check every candidate; on tasks where the check is free (examples, tests) there is no reason to skip any. [ours: a bug]
2. Cluster the passing candidates by behaviour on new inputs (augmented copies, generated tests) and take the largest
   cluster (AlphaCode [V]; CodeT [M]; augmentation scoring on ARC, Franzen et al. 2025 [V]).
3. Break ties by the simplest candidate (shortest program, fewest assumptions) (02 step 7).
4. Never take the first passing candidate (no support anywhere; it cost us puzzles). [ours]

### Step 5. Divergent mode, kept for open-ended problems

Unchanged in spirit from the architecture work, which produced the main result: problem map, seeded and low-prior
cards, leaps, interrogation, then an objective evaluator (the ladder of training checks). Additions from this research:
run it in diverge-then-converge cycles with judgment deferred while generating (Basadur [V]); vary breadth and depth
(Nijstad et al. 2010 [V]); log yield per card per problem class so the router learns (01 rule 8).

### Step 6. Problem finding

After each solved or failed problem, record problems worth solving later and helper problems that would have helped
(Getzels & Csikszentmihalyi 1976 [M]; Polya's looking back [M]). In the architecture work this is where the next
round's ideas come from; in puzzles it is where reusable sub-skills come from.

## What is evidence, what is our data, what is a guess

- Strong: verifier plus breadth on verifiable tasks; behaviour clustering; execution feedback over self-critique;
  experts classify by deep structure; consider-the-opposite reduces bias; simplicity as an overridable prior.
- Our data only: distorting cards hurt per-attempt accuracy on single-answer puzzles; the rewriting step (code names
  X1, X2) made small-model attempts worse.
- Guesses to tune: the 20% divergent slice, the probe size of four to five, the escalation thresholds, the cost of
  switching (no verified source).

## How it maps onto the harness

- Router: a new first step using `n_probe` natural attempts and the example check (already in `harness/think.py`).
- Convergent attempts: the plain prompt plus the step-3 procedure (`format_think2.arc.txt` is close; drop the
  starting-point line in convergent mode).
- Escalation: the existing cards, but only from step 5 of the ladder, chosen by the router.
- Selection: `HTSA_SELECT=vote` with `HTSA_SELECT_AUG=1`, plus "verify every candidate when verification is free".
- Divergent mode: the nano loop as it is.
- Validation: compare against plain Haiku at equal tokens on ARC-AGI-2 and on a coding benchmark with hidden tests;
  log per mode, per card, per problem class.
