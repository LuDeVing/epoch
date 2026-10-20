# One agent, as intelligent as possible: what we can do now

*2026-10-20. Plan for the next phase: one agent, made smarter by thinking schemas, before any team. Built from the
notes in this folder (`thinking_schema/`, `thinking_modes/`, `thinking_parts/`, `arc_portfolio/`), the team research in
`../team/`, the human-thought reports in `../human_thought/`, and our own measurements from 2026-10-13 to 2026-10-17.*

Marks: **[ours]** our measurement; **[V]** source checked on the web; **[M]** cited from memory, numbers to re-check;
**[design]** a choice with no direct evidence, to be tuned.

---

## 1. Where we start: what the schemas did to one model

| Test | Plain model | With a thinking schema | Verdict |
|---|---|---|---|
| NoveltyBench, 100 open creative prompts, Haiku | 3.18 distinct of 10, utility 3.13 | 9.63 distinct, utility 5.90, +13% tokens | **schema wins** [ours] |
| Language-model architecture, 21M skeleton | baseline loss 4.0939 | 4.0212, 7% lower perplexity | **schema wins**, with a training run as judge [ours] |
| ARC-AGI-2 puzzles, Haiku | 4 of 10 at about 56k tokens | small scaffold 2 of 8 at 83k to 148k; abstained on 4; fooled twice by a program that fit every example | **plain wins** [ours] |
| ARC-AGI-2, per attempt | direct attempt right 56% | divergent cards 12% to 31% | **plain wins** [ours] |
| BrainTeaser word puzzles, Haiku | about 92% | four strategy thinkers plus a judge, about 75%; forced doubt hurt most | **plain wins** [ours] |
| BrainTeaser, full scaffold | 81.2% | 0%: setup ate the budget, it abstained everywhere | **plain wins** [ours] |
| ARC-1, portfolio v2 | 36 of 37, 13 of 16 | 36 of 37, 13 of 16 | **tie**: both stop early on easy puzzles [ours] |

**The lesson.** A schema made one model better where variety is the goal and something objective prunes the ideas:
open prompts, architecture search. The same schema made it worse where the first natural answer is usually right:
puzzles, multiple choice. Forcing a contrarian move on a problem that did not need one cost accuracy every time.

So the next agent should not run one fixed procedure. It should **notice what kind of problem it faces and think
accordingly**, as expert humans do (Chi, Feltovich and Glaser 1981 [V]; Kahneman and Klein 2009 [V]).

---

## 2. Nine principles the evidence supports

1. **Classify before solving.** Is there an objective check (examples, tests, a run)? Is the answer small and exact,
   or open? Experts sort problems by deep structure first (Chi 1981 [V]). *Source: `thinking_modes/00_SYNTHESIS.md`.*
2. **Trust the first answer until a check fails.** Doubt and reframing should start at an impasse, not on a schedule
   (Ohlsson 1992 [M]; Metcalfe and Wiebe 1987 [M]). Our BrainTeaser and ARC results show the cost of doubting always.
3. **Feedback from running, not from opinion.** Revising with real outputs helps (Self-Debug, Reflexion [M];
   Greenblatt 2024: 37% to 50% on ARC with one round [V]). Self-critique with no external signal often makes answers
   worse (Huang et al. 2023 [M]).
4. **Keep the problem's own words.** Formatting changes alone move accuracy by tens of points (Sclar et al. 2023 [M]);
   our rewriting of names into codes (X1, X2) made the small model worse [ours].
5. **Name a rival, then test where they differ.** Two hypotheses and the input that separates them carry more
   information than confirming one (Platt 1964 [V]; Klayman and Ha 1987 [V]).
6. **Prefer the simpler explanation, but let evidence override it.** (Lombrozo 2007 [V]; size principle, Tenenbaum
   and Griffiths 2001 [V]; CompressARC, a tiny model trained only on description length, solves about 20% of ARC-1
   [V].)
7. **Spend effort where it is needed.** Stop when attempts agree; spend more when they split. Adaptive allocation
   beat best-of-N by more than 4x in efficiency (Snell et al. 2024 [M]); Adaptive-Consistency used up to 7.9x fewer
   samples for under 0.1% loss [V].
8. **The schema must cost less than it saves.** Our full scaffold scored 0% because its setup spent the budget [ours].
   Every added step has to pay for itself at equal tokens.
9. **Learn across problems.** What one problem teaches (a trick, a trap, a helper sub-problem) should be written down
   and offered on the next similar one (Polya's "looking back" [M]; lessons ledger, `thinking_parts/10_learning.md`).

---

## 3. The single-agent design

```
 problem
    |
 0. PROBE   4-5 natural attempts at normal effort; measure agreement and, if a check exists, how many pass
    |
 1. ROUTE
    |-- an attempt passes the check ............... CONVERGE: vote among passing, simplest wins ties, stop
    |-- none pass, attempts agree .................. REVISE: fix from the real check output, 1-2 rounds
    |-- none pass, attempts disagree ............... ESCALATE: the ladder below
    |-- no check, open-ended answer ................ DIVERGE THEN CONVERGE: cards, then an evaluator prunes
    |
 2. SELECT  verify every candidate; group by behaviour on new inputs; simplest breaks ties; never "first that passed"
    |
 3. LOOK BACK  write the lesson, the trap and any helper problem to the agent's memory
```

### Step 0: the probe
A few plain attempts tell the agent how hard the problem is, for the price of the attempts it would make anyway.
Agreement and pass rate are the machine version of a feeling of rightness (Thompson et al. 2011 [V]; semantic
entropy [V]). The problem type is a probability updated during the run, not a label fixed at the start.

### Step 1, converge: the procedure inside one attempt
1. Restate the task in its own words and say what makes an answer correct. (Polya [M]; Chi 1981 [V])
2. Study every example: what changes, what stays, how the examples differ from each other. (Chi et al. 1989 [M])
3. Write two to four candidate rules in plain words before any code. (Hypothesis Search [M]; Platt 1964 [V])
4. Check the first rule against every example. Doubt it only if the check fails.
5. Write one rival rule that also fits, and the input on which they disagree; decide with that input.
6. Prefer the simpler rule unless the evidence says otherwise.
7. Implement, run, and revise from the real outputs.
8. Stop when good enough. (Simon, satisficing [M])

### Step 1, escalate: the ladder, used only at an impasse
1. **Re-check:** run the candidates again, including cases where they should fail.
2. **Resample:** more natural attempts.
3. **Re-read:** describe the problem in other terms (objects, lines, regions, counts, symmetry). This is a change of
   representation, not a tweak of details. (Ohlsson's impasse theory [M])
4. **Helper problems:** a special case, a simpler version, work backwards, drop one condition. (Polya [M];
   Brown and Walter, "what if not" [M])
5. **Only then diverge hard:** flip an assumption, borrow by analogy with a written mapping, seed words, plan-level
   diversity. (PlanSearch [V]; Gick and Holyoak 1983 [V])

### Step 1, diverge: kept for open problems
The method that won NoveltyBench and the architecture run: isolated attempts with different pushes, the obvious
answer written first, then elsewhere, then an evaluator or a judge prunes. For one agent this means several
independent calls from the same agent, not a team. Deferred judgement while generating (Basadur [V]).

### Step 2: selection
On ARC-1, replaying the same candidates offline (`arc_portfolio/03_SYNTHESIS.md`):
- the recorded vote solved 33 of 36;
- **symmetry consistency first**, then group size, then the shortest program, solved **34 of 36**, the best any
  selector could do with those candidates.

Symmetry consistency asks whether a program's outputs rotate and mirror along with its inputs. Right programs passed
3.4 of 6 symmetries on average, wrong ones 1.5. When rivals still tie, find the input where they disagree and derive
the expected output from the examples *before* seeing the candidates' outputs (anchored tie-break). Judging without
that anchor is unreliable (Huang et al. 2023 [M]).

### Step 3: look back, the agent's memory
After each problem the agent writes, in the same disciplined format as the team's part memory:
- the trick that worked;
- the trap it fell into;
- a helper problem that would have helped;
- the problem's class.

On a new problem it receives only lessons from the same class, at most a handful, one line each. A lesson becomes
"supported" only after it helps twice on different problems (`thinking_parts/10_learning.md`, ideas 32 and 35 in
`thinking_parts/00_IDEAS.md`).

---

## 4. What to build first, ranked

| # | Piece | Evidence | Cost | Already exists |
|---|---|---|---|---|
| 1 | **Equal-token harness**: the agent against plain best-of-N with the same checker, on three suites | needed for every claim | small | `harness/bench.py`, `harness/arms/` (on disk, off GitHub) |
| 2 | **Probe and router** | strong for the parts, the router itself untested | small | `n_probe` in `harness/think.py` |
| 3 | **Convergent procedure**, doubt only on a failed check | strong | small | `format_think2.arc.txt` is close; drop the starting-point line |
| 4 | **Revision from real outputs**, 1-2 rounds, near misses only for round 2 | strong | small | in `harness/think.py` |
| 5 | **Selection**: verify all, symmetry first, then groups, then simplest; anchored tie-break | strong for code and ARC | free | `harness/portfolio_v2.py` |
| 6 | **Adaptive effort**: early stop when two passing attempts agree; cheap setup | strong | free | `portfolio_v2.py` |
| 7 | **Escalation ladder**, only from an impasse | moderate | medium | the cards exist; wire them to the router |
| 8 | **Diverge mode for open problems** | strong on our data | done | `harness/noveltybench.py` method arm |
| 9 | **Look-back memory across problems** | moderate; needs many problems to show | medium | the format exists in `nano/memory.py` |

Build 1 to 6 together; they are small and share code. Then measure before adding 7 to 9.

---

## 5. How we will know it works

Every comparison at **equal tokens** against plain best-of-N with the same checker and the same number of submissions.

| Suite | Kind | Gate |
|---|---|---|
| ARC-1 fresh puzzles and ARC-AGI-2 | verifiable, single answer | must beat plain |
| A coding set with hidden tests | verifiable, single answer | must beat plain |
| BrainTeaser | single answer, no check | **must not lose** to plain by more than 1 point |
| NoveltyBench | open-ended | must keep at least 9 distinct answers of 10 |

Log per problem: the route chosen, the mode, the tokens, the ladder step reached, and the selector's choice against
the best available candidate. These numbers tell us which piece pays and which to drop.

---

## 6. What is still a guess

- The probe size (4 or 5), the agreement thresholds, and the 20% divergent slice in the revise route. **[design]**
- Whether the router classifies correctly often enough to be worth its cost. No study tests this directly.
- Whether a small model follows an eight-step procedure, or whether the steps should be split across calls.
- Whether lessons from one problem help on the next, or only add noise. Needs a held-out test.
- Most LLM evidence comes from larger models; each step is a hypothesis to measure on ours.

---

## 7. Where the evidence lives

- `thinking_schema/00_REPORT.md`: how expert humans and the best AI systems think on novel problems; the first schema.
- `thinking_modes/00_SYNTHESIS.md`: converging and diverging, the router, the escalation ladder.
- `thinking_parts/`: thinking split into twelve faculties (representation, attention, memory, generation,
  abstraction, reasoning, critique, selection, control, learning, metacognition, communication), with 42 ranked ideas.
- `arc_portfolio/`: the portfolio method on ARC, selection by symmetry, the offline replay.
- `../human_thought/`: what neuroscience and psychology say about insight, memory and mind wandering.
- `../team/`: the idea-generation research behind the team, which the diverge mode reuses.
