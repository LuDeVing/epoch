# Psychology of programming: subfields

The psychology of programming studies how people read, plan, write and fix code. Wikipedia lists programmer cognition, tools and methods, language design, programming education and cognitive biases in software work. Its communities are the Workshop on Empirical Studies of Programmers (US) and PPIG (Europe). The core topics are program comprehension, debugging, expertise and learning. This field is the nearest match to our task: the model writes and runs programs, and we want a debugging procedure driven by real output.

Marks: (V) = confirmed in a source opened this session; (M) = from memory.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Debugging strategies | Strategic, tactical and operational goals in debugging: determine the problem, understand function and structure, locate the error, repair and confirm | Vessey 1985, Int. J. Man-Machine Studies 23 (V) | High | S5 REVISE: locate before fixing |
| Expertise as chunking | Expertise defined by ability to chunk programs; Vessey proposed experts use breadth-first with a system view, novices depth-first (stated as propositions for further testing) | Vessey 1985 (V) | Med | Hypothesis, not established |
| Program comprehension models | Bottom-up control and data flow building (von Mayrhauser and Vans); reconstructive debugging (Gilmore); as-needed strategy | Ko and Uttl 2003 (V); Brooks, Letovsky (M) | Med | S1/S2: reading code |
| Strategy vs success | Three strategies found; none was best; domain knowledge of specific bugs and attitude predicted success | Ko and Uttl 2003 (V) | High | Corrects my first draft: strategy choice matters less than relevant knowledge |
| Gugerty and Olson findings | Experts form better hypotheses from less reading; novices add bugs | Gugerty and Olson 1986 (S, from search snippet) | High | Keep best-so-far; limit edits per round |
| Plans and schemas | Stereotyped code plans and their composition | Soloway and Ehrlich 1984 (M) | High | Memory: solved subgoals |
| Notional machine, mental models | The learner's model of how the machine runs code | du Boulay; Sorva (M) | Med | S2: trace on a concrete input (code-run) |
| Cognitive biases in software work | Anchoring, optimism, availability, confirmation; logic training reduced confirmation bias | Mohanani, Salman, Turhan, Rodriguez, Ralph 2020 (V via Wikipedia, thinly sourced) | Med | G3: tests meant to fail, not pass |
| Language design, tools, education | Usability of languages and tools; teaching | Shneiderman; Weinberg 1998; Sajaniemi 2008 (V via Wikipedia) | Low | Background only |
| Research methods | Introspection, observation, experiment, qualitative work | Wikipedia (V) | Low | Background only |

Correction from the first draft: Vessey's depth-first versus breadth-first claim is a proposition, not a settled finding, and Ko and Uttl note that expert-novice results may not hold in unfamiliar systems.

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Debugging strategies | | not started |
| Expertise as chunking | | not started |
| Program comprehension models | | not started |
| Strategy vs success | | not started |
| Gugerty and Olson findings | | not started |
| Plans and schemas | [`subfields/06_plans_and_schemas/DEEP.md`](subfields/06_plans_and_schemas/DEEP.md) | done, batch 5 (2026-10-27) |
| Notional machine, mental models | | not started |
| Cognitive biases in software work | | not started |
| Language design, tools, education | | not started |
| Research methods | | not started |

## Dig into next

**1. Debugging strategy.**
- Questions: Which strategy (forward trace, backward from bad output, print search, diff against a known good case) finds faults fastest, and can code choose it from the failure type? Does a located failing line plus actual and expected values beat a general "fix it" prompt?
- Evidence needed: Vessey's strategy diagrams (opened); Gugerty and Olson (to be opened); our S5 logs by strategy.

**2. Plans and schemas.**
- Questions: Which stereotyped plans recur in our problem classes, and can they be stored and offered as library entries? What errors appear when plans are merged?
- Evidence needed: Soloway and Ehrlich (to be found); our library tests.

**3. Tracing with a notional machine.**
- Questions: Does a code-run trace on a concrete input catch faults that reading does not?
- Evidence needed: notional machine literature (to be found); our read-only versus run-trace comparison.

## Does not transfer

Novice anxiety, motivation, gender, team factors and child learning environments are about people. Reading printed code under time limits describes human reading, not a model with an executor. Programmer bias lists from a thinly sourced page need checking before use.

## Sources

[V] = opened this session. [S] = seen in search results only. [M] = from memory. Opened count: 3. The extra searches could not be run (search budget used up).

1. [V] Vessey 1985, Expertise in debugging computer programs (scanned PDF, text extracted): https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/vessey85.pdf
2. [V] Ko and Uttl 2003, Individual differences in program comprehension strategies: https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/Ko'03.pdf
3. [V] Wikipedia, Psychology of programming: https://en.wikipedia.org/wiki/Psychology_of_programming
4. [S] Davies 2000, PPIG 12th workshop: https://ppig.org:443/files/2000-PPIG-12th-davies.pdf
5. [S] Gugerty and Olson 1986 (copy): https://www.academia.edu/102488941/Debugging_by_skilled_and_novice_programmers
6. [M] Soloway and Ehrlich 1984
