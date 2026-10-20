# The single-agent thinking schema

*Living specification. Version 0.1, 2026-10-20. This file says how one agent thinks: the states it moves through,
the code-checked rules that move it, the operators it may apply, and the guardrails it may never break. It changes
only by the rules in section 8. Every element carries its evidence status, so we always know what is backed by
research, what is our own data, and what is still a guess.*

Sources: `00_PLAN.md` (design and our measurements), `fields_v2/00_SYNTHESIS.md` and the twelve briefs
`fields_v2/NN_*/BRIEF.md` (cited as F01 to F12), `fields/08_gap.md` (correlated errors).

**Status marks**

| Mark | Meaning |
|---|---|
| **[E]** | established: two or more independent sources agree (claims.jsonl status "established") |
| **[O]** | our own measurement |
| **[S]** | single source or contested; usable, but test first |
| **[D]** | design choice with no direct evidence; a placeholder to replace |

---

## 1. Who does what

- **The program** decides every transition, counts, compares, runs checks and keeps the budget. It is plain code.
- **The model** only fills a slot: write an attempt, restate a problem, apply one operator, explain one failing
  output. It never decides what happens next, and it never grades its own answer without a check.

Reason: judged steps add noise and counted steps do not; models favour their own text when judging; written
reasoning is not a reliable record of how the model decided. **[E]** (F08, F12, F11)

---

## 2. Guardrails (never broken, whatever the state)

| # | Guardrail | Status |
|---|---|---|
| G1 | **Doubt only on a signal.** Rethink, reframe or search for alternatives only after a check fails, attempts disagree, or the impasse detector fires. Never on a schedule. | **[E]** F07, F10, F11, F12; **[O]** word puzzles 92% plain vs 75% with forced doubt |
| G2 | **Revise only from real output.** A revision must cite the actual failing output, which code locates. No revision from the model's opinion alone. | **[E]** F12, F11, F03; models find errors poorly but fix them well once shown |
| G3 | **A pass must be on something the answer was not fitted to:** a held-out example, a symmetry, a mutated input. Fitting the given examples is not proof. | **[E]** F07, F12; **[O]** two ARC programs fit every example and were wrong |
| G4 | **Samples from one model are not independent.** Agreement is a hint, never proof. No persona or strategy voters on single-answer problems. No extremizing votes. | **[E]** F12, gap brief; **[O]** 92% vs 75% |
| G5 | **Code selects.** Ranking, voting, grouping and probability normalising are done in code. A model judge, if used, sees no authorship. | **[E]** F08, F10 |
| G6 | **Never abstain on the first pass.** If nothing passes, submit the best attempt so far. | **[O]** a scaffold that abstained scored 0% |
| G7 | **The schema must pay for itself.** Every element is kept only if it wins at equal tokens against the plain model. Setup cost is counted. | **[O]** the 0% scaffold spent its budget on setup |
| G8 | **Novelty is judged by running, not by a model's opinion.** | **[E]** F01, F05: model-rated novelty did not survive execution |

---

## 3. The state graph

```
                 ┌──────────────────────────────────────────────────────────────┐
                 │                                                              │
 S0 GATE ─► S1 UNDERSTAND ─► S2 REPRESENT ─► S3 GENERATE ─► S4 TEST ──pass──► S7 SELECT ─► S8 VERIFY ─► S9 LOOK BACK
                                 ▲               ▲              │
                                 │               │            fail
                                 │               │              ▼
                                 │               └──────── S5 REVISE
                                 │                              │ impasse
                                 │                              ▼
                                 └──────────────────────── S6 IMPASSE ─► pick operator ─► SUBGOAL (re-enters S1)
```

| State | What happens | Leaves when (checked by code) | Status |
|---|---|---|---|
| **S0 GATE** | Look up the problem class: is there a check, is the answer small and exact or open, what is this class's plain pass rate. Choose the mode: direct, short reason, step-by-step, checked, or open. | always, to S1 | **[S]** every field asks for it, none supplies one; rests on our data |
| **S1 UNDERSTAND** | Restate the task in its own words; say what makes an answer correct. Keep the original wording beside it. | always, to S2 | **[E]** F03 (representation), F12 (wording changes move accuracy) |
| **S2 REPRESENT** | Study every example: what changes, what stays, how examples differ. Write 1 to 4 candidate rules in plain words. Skipped in direct mode. | always, to S3 | **[E]** F03, F11 (self-explanation) |
| **S3 GENERATE** | Produce attempts: in direct and checked modes, 2 to 4 independent attempts; in open mode, isolated attempts from the bare task, typical answer first, then elsewhere. | always, to S4 | **[E]** F12; open mode **[O]** NoveltyBench 3.18 to 9.63 |
| **S4 TEST** | Run every attempt on the check, including the unfitted part (G3). With no check: keep the first natural answer, go to S7. | pass to S7; fail to S5 | **[E]** G3 |
| **S5 REVISE** | Show the failing output, located by code. The model writes one line naming what is wrong, then fixes it. Keep best-so-far. At most 2 rounds. | pass to S7; impasse to S6; 2 rounds used to S6 | **[E]** G2 |
| **S6 IMPASSE** | Fired by code: no pass, two rounds with no change, the same error twice, or a budget fraction spent. Write one state line. Pick one operator not used yet (section 4) and make it a subgoal. | subgoal solved, back to S2 or S3 with the result; all operators used, to S7 | **[S]** F03, F04 (Ohlsson; impasse may be only about 8% of problems); model's own "stuck" signal unreliable (r = .17) **[E]** |
| **S7 SELECT** | Group candidates by behaviour on fresh inputs; symmetry first, then group size, then shortest. If two rules still fit, run the one input where they differ (discriminating test). | always, to S8 | **[O]** 34 of 36 vs 33 of 36 for the vote; discriminating test **[S]** F03 |
| **S8 VERIFY** | Final check of the chosen answer on the unfitted part. If it fails and budget remains, back to S5 once. Otherwise submit (G6). | to S9 | **[E]** G3, G6 |
| **S9 LOOK BACK** | Code records the outcome; the model writes one lesson line (trick, trap, helper problem, class). The class's plain pass rate and agreement record are updated. | end | **[S]** F11 |

**Routes through the graph, by mode** (set in S0):

| Mode | Path | When |
|---|---|---|
| direct | S0, S1, S3, S4, S7, S8, S9 | the class's plain pass rate is high |
| checked | the full graph | a check exists and the class is not easy |
| no-check | S0 to S3, keep the first natural answer, S7 by agreement, S9 | single answer, nothing to run |
| open | S0 to S3 in open mode, S4 by running where possible, S7 by distinctness and running | no single right answer |

---

## 4. Operators: the idea tree used at an impasse

At S6 the program grows a tree. Each child applies **one** named operator to the current problem and becomes a
subgoal. Code tests each child, then expands the best or prunes. Operators are never applied outside S6 or open mode
(G1).

| # | Operator | What the model writes | Source | Status |
|---|---|---|---|---|
| O1 | **Specialise** | the easiest special case, solved | Polya | **[S]** |
| O2 | **Generalise** | the broader problem this is an instance of | Polya | **[S]** |
| O3 | **Decompose** | 2 to 4 sub-problems whose answers combine into the answer | Newell and Simon; F03 | **[S]** |
| O4 | **Drop a constraint** | the problem without one condition ("what if not?") | Brown and Walter; Ohlsson constraint relaxation | **[S]** F03 |
| O5 | **Work backwards** | from the goal state to what must come before it | Polya; means-ends analysis | **[S]** |
| O6 | **Change representation** | the problem in other terms: objects, counts, regions, symmetry | Ohlsson; F03, F06 | **[S]** |
| O7 | **Map an analogue** | a distant problem and a typed mapping, checked by code | Gick and Holyoak; Gentner | **[E]** that unaided analogy rarely transfers; mapping step **[S]** |
| O8 | **Reframe the goal** | after naming what the failing output says about the framing | Schön; Dorst and Cross; F06 | **[S]**; LLM reframing null in one large test |

**Tree rules [D]:** at most 3 children per expansion, at most depth 2, at most 2 expansions per problem. Children
are ranked by test result in code. An operator that solved a subgoal is recorded with the problem class in S9.

---

## 5. Memory

- **Lessons**: one line each, by problem class. Shown **after** the first attempt, never before, to avoid fixation.
  A lesson becomes trusted only after it helps on two different problems. **[S]** F11, F06
- **Class record**: plain pass rate, how often agreement was right, which operators solved subgoals. Kept in code,
  read by S0. **[D]**
- **Subgoal library** (planned): solved subgoals kept as reusable rules or helper programs, offered by similarity.
  **[D]**, see section 7.

---

## 6. What every run logs

So each element can be judged at equal tokens: the mode chosen, the path taken, tokens per state, every transition
and its trigger, every doubt step and whether it flipped right to wrong or wrong to right, operators tried and which
solved a subgoal, the selector's pick against the best candidate available, and the final result.

---

## 7. Open slots for the next research

| Slot | Question | Where to look |
|---|---|---|
| S0 gate | how to classify a problem before solving it, cheaply | our own data first; resource-rational meta-reasoning (`human_thought/deeper_mechanisms/computational_models_of_thinking.md`) |
| S6 control | when to pick which operator, when to abandon one | Schoenfeld; Soar impasse-driven subgoaling |
| Operator catalogue | the full list and each operator's preconditions | Polya, Brown and Walter, Ohlsson, design cognition |
| Analogy (O7) | how a mapping is built and scored | Structure-Mapping Engine |
| Tree search | how to expand and prune at known cost | Tree of Thoughts, LATS, search over thoughts |
| Subgoal library | turning solved subgoals into reusable tools | Soar chunking, ACT-R production compilation, program library learning |
| Conjecture refinement | improving a rule through its counterexamples | Lakatos, abduction |
| Thinking-mode baseline | does one extended-thinking attempt already beat this graph | our own equal-token test, first |

---

## 8. How this file changes

1. **A research finding** may change an element's text or status only with a source in the research notes (a brief
   and its evidence ids). Moving a mark up to **[E]** needs two independent sources.
2. **A new element** (a state, edge, operator or guardrail) enters marked **[S]** or **[D]**, with its source and the
   equal-token test that would keep it.
3. **Our measurements overrule the literature** for this agent: an element that loses at equal tokens on our suites
   is removed or restricted, whatever its sources say, and the result is recorded in the changelog.
4. **Guardrails** change only on our own measured evidence, not on a new citation alone.
5. Every change bumps the version and adds a changelog line: what changed, why, which source or run.

---

## 9. Changelog

| Version | Date | Change | Source |
|---|---|---|---|
| 0.1 | 2026-10-20 | First version: 8 guardrails, 10 states, 4 routes, 8 operators, memory, logging, open slots. | `00_PLAN.md`, `fields_v2/00_SYNTHESIS.md`, briefs F01 to F12, gap brief |
