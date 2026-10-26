# Embodied and situated cognition: subfields

This field holds that thinking is not only in the head. The Stanford Encyclopedia entry organises it around three themes (conceptualization, replacement, constitution) and the "four Es": embodied, embedded, extended, enactive. Much of it concerns bodies and brains a model lacks. The useful core is that people think better by acting on an external workspace, which maps onto a model using code, notes and tests.

Marks: (V) = confirmed in a source opened this session; (M) = from memory.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Conceptualization (grounded cognition) | Body shape constrains which concepts are acquired; perceptual symbols | Lakoff and Johnson; Barsalou 1999, 2008 (V via SEP) | Low | Background only |
| Embedded cognition | Environment and social setting reduce cognitive load | Martin and Schwartz 2005; Hutchins 1996 (V via SEP) | High | Design view: the program as the environment |
| Epistemic action | Acting on the world to ease thinking | Kirsh and Maglio 1994, cited in Pouw et al. (V) | High | S2/S4: write, sketch, run code to think |
| Extended mind | Tools and notes as constituents of cognition; critics say this is tool use | Clark and Chalmers 1998; Clark 2008; Wilson 2004; critics Adams and Aizawa, Rupert (V via SEP) | High | Memory: notes and the library |
| Distributed cognition | Cognition spread across people and artefacts | Hutchins (V via SEP) | Med | Design view |
| Gesture and thinking | Gestures as external tools that support the gesturer's thinking | Pouw et al. 2014 (V); Wheeler 2013 (V) | Low | Background only |
| Enactivism | Cognition arises from sensorimotor activity; three strands | Varela, Thompson, Rosch; O'Regan and Noe; Hutto and Myin (V via SEP) | Low | Background only |
| Replacement / dynamical approaches | Dropping representations for dynamics and robots | Brooks 1991; Van Gelder; Thelen and Smith (V via SEP) | Low | Background only; conflicts with a fixed procedure |
| External representations and diagrams | How notation changes problem difficulty | Zhang and Norman 1994; Larkin and Simon 1987 (M) | High | Operator O6 |

Corrections from the first draft: "situated action" (Suchman, Lave) was listed as its own row from memory; the SEP entry has no separate situated section, so it is folded into embedded. SEP adds an explicit caveat list: replicability concerns for well-cited priming findings, interpretation disputes over mirror neurons, and doubts about scaling up.

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Conceptualization (grounded cognition) | | not started |
| Embedded cognition | | not started |
| Epistemic action | [`subfields/03_epistemic_action/DEEP.md`](subfields/03_epistemic_action/DEEP.md) | done, batch 5 (2026-10-27) |
| Extended mind | | not started |
| Distributed cognition | | not started |
| Gesture and thinking | | not started |
| Enactivism | | not started |
| Replacement / dynamical approaches | | not started |
| External representations and diagrams | | not started |

## Dig into next

**1. External representations.**
- Questions: Which representations (table, grid, diagram, case list) make a given problem class cheaper for a model? Can code convert a problem into a second format and keep the one with the higher plain pass rate?
- Evidence needed: Zhang and Norman, Larkin and Simon (to be opened); our runs of ARC and puzzles in two formats.

**2. Epistemic action as a design rule.**
- Questions: Does letting the model run small exploratory code to learn about the problem (not only to check an answer) help? When does external recording beat holding it in the prompt?
- Evidence needed: Kirsh and Maglio on Tetris (to be opened); our exploratory-run test at equal tokens.

**3. Extended mind and memory design.**
- Questions: What is the smallest reliable external store, and when is a note trusted?
- Evidence needed: Clark and Chalmers conditions; our lesson-use logs.

## Does not transfer

Grip and word meaning, posture and judgement, gesture, sensorimotor grounding, mirror neurons and emotion in the body need a body. SEP itself flags replication concerns. Radical enactivism rejects mental content, which clashes with a program that tracks explicit states.

## Sources

[V] = opened this session. [S] = seen in search results only. [M] = from memory. Opened count: 3. The extra searches could not be run (search budget used up).

1. [V] Stanford Encyclopedia, Embodied Cognition: https://plato.stanford.edu/entries/embodied-cognition/
2. [V] Pouw et al. 2014, Frontiers in Psychology (PDF text read): https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00359/pdf
3. [V] Wheeler 2013, Is cognition embedded or extended? The case of gestures: https://storre.stir.ac.uk/bitstream/1893/13054/1/wheeler_cognition_embedded_extended_gestures_STORRE.pdf
4. [S] Clark, Supersizing the Mind: https://academic.oup.com/book/6746
5. [M] Kirsh and Maglio 1994; Clark and Chalmers 1998; Larkin and Simon 1987; Zhang and Norman 1994
