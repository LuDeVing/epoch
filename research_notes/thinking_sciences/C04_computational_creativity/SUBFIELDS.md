# Computational creativity: subfields

Computational creativity builds systems that make novel and valuable artefacts and studies how to judge them. It divides by domain (language, story, music, visual art, games, problem solving), by theory (Boden's exploratory and transformational creativity, plus combinational), by evaluation method, and by role (autonomous or co-creative). For us the main use is open mode: many distinct ideas, selected without a model judge. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Boden's creativity types | Exploratory, transformational (and combinational) | Boden; Wiggins formalisation [V via Wikipedia] | High | S3 open mode, which generator to use |
| Creativity as search | Exploring a defined space | arXiv 2405.01453 [V] | High | S3 search control |
| Combinational creativity | Joining distant concepts across domains | arXiv 2412.14141 [V] | High | O7 analogue, grounding |
| Transformational creativity | Changing the rules of the space | Boden [V via Wikipedia] | Med | O4, O6, O8 |
| Evaluation of creativity | Criteria (Newell, Shaw, Simon), SPECS (Jordanous and Keller), generate-then-filter (Geneplore) | Wikipedia article [V] | High | G8, S7 |
| Quality-diversity, novelty search | Keep a population of different solutions | Lehman and Stanley; Mouret and Clune (MAP-Elites) [M] | High | S3 history of directions tried |
| Story, music, art, humour systems | TALE-SPIN, MINSTREL, AARON, EMI, JAPE | Wikipedia article [V] | Low | background only |
| Conceptual blending | Merging two input spaces | Fauconnier and Turner [V as name only] | Med | O7 |
| Creative problem solving | Insight, incubation in architectures | Wikipedia article [V] | Med | impasse and restructuring |
| Scientific discovery systems | Automated hypothesis generation | BACON, Langley [V as name only] | Med | open mode with a running check |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding. The field synthesis is [`SYNTHESIS.md`](SYNTHESIS.md).

| Subfield | Deep document | Status |
|---|---|---|
| Boden's creativity types | | not started |
| Creativity as search | | not started |
| Combinational creativity | | not started |
| Transformational creativity | | not started |
| Evaluation of creativity | [`subfields/05_evaluation_of_creativity/DEEP.md`](subfields/05_evaluation_of_creativity/DEEP.md) | done, batch 4 (2026-10-26) |
| Quality-diversity, novelty search | [`subfields/06_quality_diversity_and_novelty_search/DEEP.md`](subfields/06_quality_diversity_and_novelty_search/DEEP.md) | done, batch 4 (2026-10-26) |
| Story, music, art, humour systems | | not started |
| Conceptual blending | | not started |
| Creative problem solving | | not started |
| Scientific discovery systems | | not started |

## Dig into next

1. **Quality-diversity and novelty search.** How can code keep an archive of idea "cells" (direction, method) and send the next attempt to an empty cell? What cheap descriptor of an idea can code compute? Evidence: diversity against quality at equal samples, with our NoveltyBench result (3.18 to 9.63) as baseline. I could not search for LLM quality-diversity papers (quota used).
2. **Evaluation of creativity.** Which novelty tests can be run (distance to retrieved prior art) instead of asked? How well do they agree with human raters? Evidence: a small rated set; the known failure of model judges (G8).
3. **Combinational creativity via retrieved distant concepts.** How distant can a source be before value falls? Evidence: grounded versus ungrounded draws, scored by running or by raters.

## Combined with LLMs

- Combinatorial creativity framework (arXiv 2412.14141): retrieval maps concepts across abstraction levels to link distant domains, then components are decomposed and recombined into research ideas. Evaluated by similarity to later real research on OAG-Bench; reports a 7 to 10 percent gain in similarity scores across several metrics over baselines. LLM not named on the abstract page [V].
- Creative problem solving in LLMs (arXiv 2405.01453, EMNLP 2024 Findings): a position paper arguing that computational creativity principles should be integrated with large language and vision models; "preliminary experiments", no measured results on the abstract page [V].
- A claim that LLM agents reach combinational and exploratory but not transformational creativity came only from a search-result summary of a 2026 paper [M], so I do not rely on it.
- Similarity to later research is not the same as being novel and valuable, so the 7 to 10 percent figure does not settle G8.

## Sources

1. https://arxiv.org/abs/2412.14141 [V] LLMs and combinatorial creativity
2. https://arxiv.org/abs/2405.01453 [V] Creative problem solving in large language and vision models
3. https://en.wikipedia.org/wiki/Computational_creativity [V] overview (first 100,000 characters read)
4. https://www.emergentmind.com/papers/2604.13242 [M] 2026 paper on agent creativity
5. Boden, The Creative Mind (1990); Lehman and Stanley 2011; Mouret and Clune 2015 [M] (no URL)
