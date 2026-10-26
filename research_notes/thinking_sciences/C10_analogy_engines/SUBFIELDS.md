# Analogy engines: subfields

Analogy engines are programs that find and use a correspondence between two structured situations. The core theory is Gentner's structure mapping: match relations, not surface features, and prefer systematic matches (connected systems of higher-order relations). The field divides into mapping (SME), retrieval (MAC/FAC), connectionist and hybrid models (LISA, DORA), constraint-based theories, learning of relations, and analogical problem solving. It supplies the machinery behind operator O7, where our schema has a gap: how a mapping is built and scored. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Structure mapping (SME) | Base and target in; correspondences, candidate inferences and a structural score out | Falkenhainer, Forbus, Gentner; QRG page [V] | High | O7 mapping step |
| Systematicity | Prefer mappings of connected higher-order relations | Gentner 1983 [V via Wikipedia and QRG] | High | scoring a mapping |
| Candidate inferences | Surmises about the target that the mapping sanctions | QRG page [V] | High | O7: transfer a step, then test |
| Incremental mapping | Extend a mapping when new facts arrive | QRG page [V] | Med | S6 across rounds |
| Analogical retrieval (MAC/FAC) | Cheap filter then structural match | Forbus, Gentner, Law 1994 [M]; QRG page only links to it [V] | High | memory retrieval |
| Multiconstraint theory | Structure, similarity and purpose together | Holyoak and Thagard 1997 [V via Wikipedia] | Med | choosing among mappings |
| Working-memory-limited mapping | Map a subset serially | Keane and Brayshaw 1988 [V via Wikipedia] | Low | background only |
| Neural analogy and relation learning | LISA; learning relations from examples | Hummel and Holyoak; Doumas et al. 2008 [V via Wikipedia] | Low | background only |
| Vector-space relational similarity | Relational similarity from text statistics | Turney 2006 [V via Wikipedia] | Med | cheap similarity |
| Analogical prompting for LLMs | Model recalls its own related problems | Yasunaga et al., arXiv 2310.01714 [V] | Med | S3 variant, O7 |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Structure mapping (SME) | [`subfields/01_structure_mapping_sme/DEEP.md`](subfields/01_structure_mapping_sme/DEEP.md) | done, batch 5 (2026-10-27) |
| Systematicity | | not started |
| Candidate inferences | | not started |
| Incremental mapping | | not started |
| Analogical retrieval (MAC/FAC) | | not started |
| Multiconstraint theory | | not started |
| Working-memory-limited mapping | | not started |
| Neural analogy and relation learning | | not started |
| Vector-space relational similarity | | not started |
| Analogical prompting for LLMs | | not started |

## Dig into next

1. **Structure mapping and candidate inferences.** Can an LLM write both situations as typed relation lists, with code (a small SME) computing the mapping and score? Does the score predict that a transferred step helps? Evidence: tasks with known analogues; correlation of score with success. Needed reading: the SME algorithm paper (the PDF fetch failed).
2. **MAC/FAC style retrieval.** What cheap first pass (a count vector of relation types) finds far analogues without surface overlap? Does restricting far analogues to impasses hold up? Evidence: retrieval hit rate by distance; effect on mean and spread of results.
3. **Schema induction from two analogues.** What does code store after two solved instances? Evidence: a second-problem transfer test.

## Combined with LLMs

- Emergent analogical reasoning (Webb, Holyoak, Lu; arXiv 2212.09196): tasks include a non-visual matrix-reasoning test built on the rules of Raven's matrices, zero-shot. GPT-3 (text-davinci-003) matched or beat human reasoners in most settings; preliminary GPT-4 tests looked stronger. No numbers on the abstract page [V].
- Analogical prompting (Yasunaga et al., arXiv 2310.01714): the model first writes relevant past examples or knowledge, then solves. Tasks GSM8K, MATH, Codeforces and BIG-Bench reasoning. Reported to beat zero-shot and manual few-shot chain of thought; models and scores not given on the abstract page [V].
- Both test whether LLMs reason by analogy; neither puts an explicit structure mapper in the loop. I found no study of an SME-style mapper with an LLM. The planned LLM-specific searches ("LLM structure mapping analogy", "analogical reasoning large language models benchmark") could not be run (search quota used up), so a gap in my search may remain. A May 2026 paper comparing SME, CogSketch and GPT models appeared only in a search result [M].

## Sources

1. https://www.qrg.northwestern.edu/ideas/smeidea.htm [V] SME overview
2. https://en.wikipedia.org/wiki/Analogy [V] analogy theories (first 100,000 characters)
3. https://arxiv.org/abs/2212.09196 [V] Emergent analogical reasoning in LLMs
4. https://arxiv.org/abs/2310.01714 [V] Large language models as analogical reasoners
5. https://www.emergentmind.com/papers/2605.01359 [M] SME versus LLM comparison
6. https://jair.org/index.php/jair/article/view/10583 [M] Latent Relation Mapping Engine
7. Forbus, Gentner, Law 1994, MAC/FAC; Gick and Holyoak 1980 [M] (no URL)
