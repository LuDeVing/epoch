# Intelligence research (psychometrics): subfields

Psychometric intelligence research measures differences between people and asks what predicts them. It divides into structure (g, broad abilities, the Cattell-Horn-Carroll model), mechanism (working memory, attention, speed), tests and task analysis (matrices, item difficulty), and prediction, development, biology and genetics. Most of it is about differences between people, so little transfers. The useful parts are task-level: which problem features make reasoning hard, and what limits relational reasoning.

Marks: (V) = confirmed in a source opened this session; (M) = from memory.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Factor structure of abilities | g and a three-stratum hierarchy; nine broad abilities plus speed | Spearman; Cattell; Horn; Carroll 1993 (461 data sets); McGrew (all V via Wikipedia) | Low | Background only; vocabulary for problem classes |
| Fluid reasoning (Gf) | Reasoning, forming concepts and solving problems with unfamiliar information or novel procedures | Cattell 1943; Horn and Cattell 1967 (V via Wikipedia) | Med | S0 gate: sort problems by novelty |
| Working memory and Gf | Whether capacity explains reasoning; Kyllonen and Christal 1990 is the usual cite | Kyllonen and Christal 1990 (V via Wikipedia); Dokic, Koso-Drljevic, Bilalic 2025 (V) | Med | Limits on holding many rules |
| Capacity hypothesis test | If capacity causes Gf, the link should grow with task demand; most studies and a new N=543 study did not find that, using item difficulty and rule counts | Dokic et al. 2025, Intelligence 108 (V) | High | Corrects my first draft: do not assume rule count alone drives difficulty; measure it |
| Working memory training transfer | Training on memory tasks to raise Gf | Jaeggi 2008; null results by Redick, Chooi and Thompson, Melby-Lervag and Hulme (V via Wikipedia) | Low | Negative result: no training-style shortcut |
| Matrix tests and task analysis | Raven, Woodcock-Johnson concept formation and analysis-synthesis | Raven; Carpenter, Just, Shell 1990 (M) | Med | S0 gate; rule taxonomy |
| Item difficulty modelling | Predicting difficulty from item features | Embretson (M) | High | S0 cheap difficulty estimate; G12 |
| Strategy on matrices | Constructive matching vs response elimination | Bethell-Fox, Lohman, Snow 1984 (M) | Med | S3/S4: build then check vs eliminate |
| Motivation and test performance | Low scores may reflect low interest in the task | Messick 1989 (V via Wikipedia) | Low | Background only |
| Processing speed, executive function, prediction, genetics | Speed, inhibition; later life outcomes; heritability | Many | Low | Background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Factor structure of abilities | | not started |
| Fluid reasoning (Gf) | | not started |
| Working memory and Gf | | not started |
| Capacity hypothesis test | | not started |
| Working memory training transfer | | not started |
| Matrix tests and task analysis | | not started |
| Item difficulty modelling | [`subfields/07_item_difficulty_modelling/DEEP.md`](subfields/07_item_difficulty_modelling/DEEP.md) | done, batch 5 (2026-10-27) |
| Strategy on matrices | | not started |
| Motivation and test performance | | not started |
| Processing speed, executive function, prediction, genetics | | not started |

## Dig into next

**1. Item difficulty models.**
- Questions: Which coded features (objects, rules, relations per rule, distractors) predict the plain pass rate on our items? Can a feature count replace a model call in the S0 gate?
- Evidence needed: Embretson-style regression on our logged items; Carpenter et al. rule taxonomy (to be opened).

**2. Capacity versus load in models.**
- Questions: Does failure grow with relations held at once, or with distractors? Dokic et al. found the human capacity account fails on rule tokens; is that true for a model?
- Evidence needed: a sweep of our items by relation and distractor count, at fixed tokens.

**3. Matrix-solving strategy.**
- Questions: Does "build the answer, then match" beat "compare the choices" for a model? Should code force one route?
- Evidence needed: Bethell-Fox and Carpenter strategy data; our ARC and puzzle runs split by route.

## Does not transfer

Rank differences between people, group differences, heritability, brain correlates, ageing and g itself describe human populations. A model has no stable ability profile across calls. Working memory training results concern human brains.

## Sources

[V] = opened this session. [S] = seen in search results only. [M] = from memory. Opened count: 3. The extra searches could not be run (search budget used up).

1. [V] Dokic, Koso-Drljevic, Bilalic 2025, Intelligence 108 (record): https://researchportal.northumbria.ac.uk/en/publications/past-reflections-present-insights-a-systematic-review-and-new-emp/
2. [V] Wikipedia, Cattell-Horn-Carroll theory: https://en.wikipedia.org/wiki/Cattell%E2%80%93Horn%E2%80%93Carroll_theory
3. [V] Wikipedia, Fluid and crystallized intelligence: https://en.wikipedia.org/wiki/Fluid_and_crystallized_intelligence
4. [S] Chuderski and Necka 2012 (capacity and control; figures such as 62% come from the search snippet only): https://researchgate.net/profile/Adam-Chuderski/publication/225051454_The_Contribution_of_Working_Memory_to_Fluid_Reasoning_Capacity_Control_or_Both/links/00b4951f2861dafc04000000/The-Contribution-of-Working-Memory-to-Fluid-Reasoning-Capacity-Control-or-Both.pdf
5. [S] Rzhanova et al. 2018 fluid intelligence review; fetch blocked (403): https://doaj.org/article/1d01738f3c5249438e5371243b9871aa
6. [M] Carpenter, Just, Shell 1990; Embretson; Bethell-Fox, Lohman, Snow 1984
