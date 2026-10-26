# Creative cognition: subfields

Creative cognition applies the methods of cognitive psychology to the making of new ideas. Its premise is that creativity uses ordinary processes (memory, analogy, combination, imagery) in a particular way. It divides into process models (generate then explore), studies of how ideas are built from existing knowledge (conceptual combination and blending, analogy), studies of what blocks novelty (fixation), and work on divergent thinking and evaluation. This is the closest field to our open mode.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Geneplore model | Generative phase builds "preinventive" structures; exploratory phase interprets them [V3]. A replication that added physical synthesis did not find the preinventive phase raised creativity, only originality at a cost to practicality [M, search snippet] | Finke, Ward and Smith (1992, 1996) | High | S3 open mode, S4 test: generate widely, then run |
| Dual-process view of creativity | Creative thinking shifts between generative and evaluative modes; both draw on fast and slow processes [V1] | Review in arXiv 1409.2207 | Med | mode switch by code, not by model |
| Conceptual blending and integration | Input spaces, generic space, blended space; emergent structure by composition, completion, elaboration; forerunner: Koestler's bisociation; critics: no testable hypotheses, simpler processes may explain blends [V2] | Fauconnier and Turner (1993, 2002); Gibbs; Ritchie | High | open-mode operator: combine two sources |
| Conceptual combination (noun-noun) | How two concepts merge [M] | Hampton; Wisniewski | High | seed pairs from distant domains |
| Structured imagination | New ideas inherit properties of known examples [M] | Ward (1994) | High | S3 fresh contexts |
| Fixation and functional fixedness | Duncker candle problem; filled box halves solutions (Adamson 1952); Maier and Birch and Rabinowitz two-cord problem; prior use biases object choice; wording underlining nouns raised success from 23% to 47 to 55% (Frank and Ramscar); example designs cause design fixation, instructions on what to avoid reduce it (Chrysikou and Weisberg 2005); breaking objects into components helps [V4] | Duncker (1945); Jansson and Smith (1991) [M] | High | memory: lessons after first attempt; wording of S1 |
| Process stage models and incubation | Wallas five stages; Ward: incubation may help by forgetting misleading clues [V5] | Wallas (1926); Csikszentmihalyi | Low | incubation unreliable |
| Divergent thinking | Convergent versus divergent; Runco: divergent thinking is not all of creative thinking [V5] | Guilford; Runco | Med | open-mode metrics |
| Ordinary-cognition and implicit-explicit theories | Ordinary processes produce extraordinary results; honing theory [V5] | Weisberg; Helie and Sun; Gabora | Med | supports engineering variation |
| Analogy and distant sources | See A02 [M] | Gentner; Dunbar | Med | O7 |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding. The field synthesis is [`SYNTHESIS.md`](SYNTHESIS.md).

| Subfield | Deep document | Status |
|---|---|---|
| Geneplore model | [`subfields/01_geneplore/DEEP.md`](subfields/01_geneplore/DEEP.md) | done, batch 4 (2026-10-26) |
| Dual-process view of creativity | | not started |
| Conceptual blending and integration | | not started |
| Conceptual combination (noun-noun) | | not started |
| Structured imagination | covered in [`subfields/06_fixation_and_structured_imagination/DEEP.md`](subfields/06_fixation_and_structured_imagination/DEEP.md) | done, batch 4 (2026-10-26) |
| Fixation and functional fixedness | [`subfields/06_fixation_and_structured_imagination/DEEP.md`](subfields/06_fixation_and_structured_imagination/DEEP.md) | done, batch 4 (2026-10-26) |
| Process stage models and incubation | | not started |
| Divergent thinking | | not started |
| Ordinary-cognition and implicit-explicit theories | | not started |
| Analogy and distant sources | | not started |

## Dig into next

1. **Fixation and structured imagination.** Questions: (a) How strongly do shown examples copy into model outputs, by distance of the example? (b) Do "what to avoid" instructions reduce copying, as Chrysikou and Weisberg found in people? (c) Does code-forced diversity beat prompting? Evidence: Smith, Ward and Schumacher design with example and no-example arms; our NoveltyBench data (3.18 to 9.63).
2. **Geneplore.** Questions: (a) What is the LLM analogue of a preinventive structure, and how should S4 interpret it (run, constrain)? (b) Does generating before the constraint is shown raise novelty at equal practicality? Evidence: Finke's mental-synthesis design, with and without the category first.
3. **Conceptual blending.** Questions: (a) Which blend types (simplex, mirror, single-scope, double-scope) produce ideas that survive a run? (b) Can code choose input spaces from distant domains? Evidence: blend libraries; selection by running (G8).

## Does not transfer

Personality, mood, sleep, the "aha" feeling, brain networks and creativity training (small effects after bias correction) are about people. Incubation effects are unreliable. The model already fixates on typical answers, so the lesson is to engineer variation, not to teach it to be creative.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only.

1. [V] Shifting Sands of Creative Thinking: Connections to Dual Process Theory (abstract): https://arxiv.org/abs/1409.2207
2. [V] Conceptual blending, Wikipedia: https://en.wikipedia.org/wiki/Conceptual_blending
3. [V] Creativity, Wikipedia (first 100k characters; Geneplore section): https://en.wikipedia.org/wiki/Creativity
4. [V] Functional fixedness, Wikipedia: https://en.wikipedia.org/wiki/Functional_fixedness
5. [M] Geneplore replication discussion: https://creativeit.cs.colorado.edu/CreativeIT/188 (search snippet only)
6. [M] Finke, Ward and Smith (1992); Ward (1994); Smith, Ward and Schumacher (1993). No URLs. The design-fixation and conceptual-combination search was blocked by the search budget.
