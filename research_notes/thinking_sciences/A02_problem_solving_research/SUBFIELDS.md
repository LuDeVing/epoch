# Problem-solving research: subfields

This field asks how people find a path from a start to a goal when the path is not known. It divides into the information-processing tradition (problem spaces, search, means-ends analysis), the Gestalt and insight tradition (restructuring, fixation), the study of well- versus ill-defined problems, and work on analogy and transfer. For our schema it is the closest field: states, operators and impasses all come from here.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Problem-space theory | "All goal-oriented behavior can be cast as search through a space of states" [V3]; most problems are solved gradually [V1] | Newell and Simon, Human Problem Solving (1972); Logic Theorist, GPS | High | the whole state graph |
| Means-ends analysis | Pick the action that reduces the difference between current and goal state; GPS used a table of difference-to-operator links; later STRIPS and Prodigy [V2] | Newell, Simon, Shaw (1957, 1961) | High | S6 operator choice; O5 |
| Impasse-driven subgoaling and chunking | In Soar, an impasse creates a substate; solving it can be compiled into a new rule so the impasse does not recur [V3] | Newell, Unified Theories of Cognition; Laird | High | S6 and the subgoal library (memory) |
| Problem solving strategies and the problem-solving cycle | Decomposition (divide and conquer), analogy, abstraction, trial and error, hypothesis testing; well- versus ill-defined problems [V5] | Duncker (1935); Luchins; Maier; Wason; Dorner | High | operators O1 to O8; S0 gate |
| Representational change theory | Wrong initial representation must be restructured; constraint relaxation and chunk decomposition [V1] | Ohlsson (1984, 1992, 2011); Knoblich et al. (1999, 2001) | High | O4 drop a constraint, O6 change representation |
| Gestalt insight and the "sudden insight" debate | Sudden restructuring; Ohlsson suggested suddenness may be an illusion of limited introspection [V1] | Wertheimer (1925); Duncker (1945); Kohler; Sternberg and Davidson three-process theory [V4] | Med | background; treat restructuring as an operator |
| Progress monitoring | Solvers' sense of nearing the solution grows gradually; anagram solvability judgments improve [V1] | Durso et al. (1994); Novick and Sherman (2003); MacGregor, Ormerod, Chronicle [M] | High | S6 trigger: code-set no-progress rule |
| Analogical problem solving | Structure-mapping: find, map, check; prefers relational match over surface match (systematicity) [V6] | Gentner; Holyoak and Thagard (1997); Gick and Holyoak [M] | Med | O7 map an analogue |
| Mathematical problem solving and heuristic method | Specialise, generalise, work backwards, control [M] | Polya; Schoenfeld; Brown and Walter | High | O1 to O5; S6 control |

## Dig into next

1. **Impasse-driven subgoaling (Soar).** Questions: (a) What exactly counts as an impasse in Soar (tie, no-change, conflict) and which of these our detector should copy? (b) How are substate results compiled into rules, and what is the LLM analogue (a stored subgoal with its trigger)? (c) How does Soar avoid reusing a stale chunk? Evidence: Laird's Soar manual and papers; then replay of our logged impasses.
2. **Progress monitoring.** Questions: (a) What count-based rule (distance to goal, repeated states, moves left) predicts failure early on our suites? (b) Does gradual monitoring in people (Durso; Novick and Sherman) suggest a graded trigger rather than a hard one? Evidence: logged attempts with outcomes; compare triggers against "no pass after two rounds".
3. **Representational change.** Questions: (a) Which failed items hide a self-imposed constraint? (b) Does O4 phrased as "which condition did the failing output assume?" beat random operators? Evidence: operator ablation at equal tokens, per class.

## Does not transfer

The "aha" feeling, eye-tracking and brain imaging of insight, incubation (failed to replicate) and the Gestalt claim of true suddenness are about people. Collaboration effects on shared representations are group-level.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only.

1. [V] Tracing cognitive processes in insight problem solving (PMC10219327): https://pmc.ncbi.nlm.nih.gov/articles/PMC10219327/
2. [V] Means-ends analysis, Wikipedia: https://en.wikipedia.org/wiki/Means%E2%80%93ends_analysis
3. [V] Soar (cognitive architecture), Wikipedia: https://en.wikipedia.org/wiki/Soar_(cognitive_architecture)
4. [V] Insight, Wikipedia: https://en.wikipedia.org/wiki/Insight
5. [V] Problem solving, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Problem_solving
6. [V] Analogical reasoning, Wikipedia (Gick and Holyoak not covered): https://en.wikipedia.org/wiki/Analogical_reasoning
7. [M] Knoblich et al. 1999, JEP:LMC 25(6): https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf (fetch returned unreadable PDF; cited via source 1)
8. [M] Newell and Simon (1972); Polya (1945); Schoenfeld (1985); MacGregor, Ormerod and Chronicle (2001); Gick and Holyoak (1980). No URLs.
