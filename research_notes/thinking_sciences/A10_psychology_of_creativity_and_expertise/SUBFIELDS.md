# Psychology of creativity and expertise: subfields

This area joins two literatures: the psychology of creativity (how people create, in what conditions) and the psychology of expertise (what experts know, how they got there, where it fails). It divides into process models of creative work, the nature of expert knowledge (chunks, patterns), how expertise is built (deliberate practice and its limits), the costs of expertise (rigidity, Einstellung), and problem finding. The two meet where an expert's strong schemas both speed and block new solutions.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Einstellung (set) effect | Luchins' water jars: after five problems solved by B - A - 2C, most trained subjects kept the long method while nearly all controls used the simple one; telling them "Don't be blind" made over half switch; stress raised rigidity; IQ unrelated [V2] | Luchins (1942); Bilalic, McLeod and Gobet (2008, chess; seen in search only) [M] | High | G1, S6, S4 harvest |
| Expert flexibility and adaptive expertise | Einstellung studied with eye movements in experts; reflection in athletes; heuristic toolboxes [V1] | Bilalic, Ellis, Reingold, Hambrick, Gigerenzer | Med | S6 operator choice |
| Chunking and templates | Chunks of two to six items; experts recall meaningful chess positions but not random ones; digit span from 7 to nearly 80 by using known running times (S.F.); models EPAM and CHREST [V4] | Miller (1956); Chase and Simon (1973); Ericsson et al. (1980) | High | memory: subgoal library as chunks |
| Deliberate practice | Goals, feedback, repetition, rising difficulty; meta-analytic r = 0.40 [V3] | Ericsson | Low | background only (agent does not practice) |
| Limits of deliberate practice | Explains 26% of variance in games, 21% music, 18% sports, 4% education, under 1% professions; about 1% among elite performers [V3] | Macnamara, Hambrick, Oswald (2014); Macnamara, Moreau, Hambrick (2016); Campitelli and Gobet (2011) | Low | does not transfer |
| Expertise research programmes | Cognitive processes, development, general cognition, transfer, frameworks; eye tracking of experts; transfer of skills across domains often absent (video games to attention) [V1] | Campitelli, Connors, Bilalic, Hambrick (2015 editorial) | Med | warning: transfer is narrow |
| Expert versus novice problem representation | Experts classify by deep structure [M] | Chi, Feltovich, Glaser (1981) | High | S2 represent |
| Problem finding | Creative people find and frame the problem [M, no page found; the Creativity page's visible text did not cover it] | Getzels and Csikszentmihalyi (1976) [M] | High if confirmed | S1, O8 reframe, open mode |
| Creative process models | Wallas stages; Csikszentmihalyi five phases; incubation [V5] | Wallas (1926); Csikszentmihalyi | Low | descriptive only |
| Naturalistic decision making | Experts decide by recognition [M] | Klein | Med | S0 quick mode |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Einstellung (set) effect | | not started |
| Expert flexibility and adaptive expertise | | not started |
| Chunking and templates | | not started |
| Deliberate practice | | not started |
| Limits of deliberate practice | | not started |
| Expertise research programmes | | not started |
| Expert versus novice problem representation | | not started |
| Problem finding | [`subfields/08_problem_finding/DEEP.md`](subfields/08_problem_finding/DEEP.md) | done, batch 5 (2026-10-27) |
| Creative process models | | not started |
| Naturalistic decision making | | not started |

## Dig into next

1. **Einstellung.** Questions: (a) How often does our model keep a familiar longer method when a simpler one exists (Luchins items)? (b) Luchins found a short warning ("Don't be blind") worked on people; does an equivalent work on the model, given our note that careful-thinking prompts do not help? Test it. (c) Does forced harvest of dropped candidates or an assigned alternative direction cut the trap? Evidence: Luchins and Bilalic items with known better solutions; trap rate by arm.
2. **Chunking and templates.** Questions: (a) What is the smallest useful chunk for the subgoal library (a rule, a helper function, a worked step)? (b) Do chunks help most where the class is structured, as chess chunks helped only on real positions? Evidence: Chase and Simon design; EPAM/CHREST models; library ablation.
3. **Problem finding.** Questions: (a) Fetch the original art-student study and extract coded problem-finding behaviours. (b) Does a "restate or propose alternative questions" slot raise distinct valid outputs in open mode? Evidence: Getzels and Csikszentmihalyi (1976); open-mode runs.

## Does not transfer

Years of practice, talent versus effort, motivation, flow, domain eminence, stress and anxiety effects on rigidity, ageing and gender differences are about human careers and bodies. Only set effects, deep-structure representation and framing are testable on a model.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only.

1. [V] Psychological perspectives on expertise, Frontiers editorial (PMC4354238): https://pmc.ncbi.nlm.nih.gov/articles/PMC4354238/
2. [V] Einstellung effect, Wikipedia: https://en.wikipedia.org/wiki/Einstellung_effect
3. [V] Deliberate practice, Wikipedia: https://en.wikipedia.org/wiki/Deliberate_practice
4. [V] Chunking (psychology), Wikipedia: https://en.wikipedia.org/wiki/Chunking_(psychology)
5. [V] Creativity, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Creativity
6. [M] Bilalic et al. 2008: https://cognition.aau.at/download/Publikationen/Bilalic/Bilalic_etal_2008b.pdf (search result only)
7. [M] Getzels and Csikszentmihalyi (1976) The Creative Vision; Chi, Feltovich and Glaser (1981); Klein (1998). No URLs. Searches for problem finding were blocked by the search budget.
