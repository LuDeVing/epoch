# Cognitive psychology of thinking and reasoning: subfields

This field studies how people draw conclusions, test ideas and judge arguments. It is split by kind of inference (deduction, induction, probabilistic reasoning), by theory of mechanism (mental models, mental logic, probability heuristics, dual process) and by the role of content and belief. Much of it is lab work on small puzzles with right answers, which is close to the tasks our agent faces.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Mental models theory | Reasoning by building models of possibilities. Applied to relational, propositional, quantified and meta-deductive inference; later to probability and counterfactuals [V4] | Johnson-Laird and Byrne; How We Reason (2006); The Rational Imagination (2005) | High | S2 represent, S7 select: force a search for the model that breaks the conclusion |
| Wason selection task and hypothesis testing | People pick confirming cards; under 10% give the logical answer in the original task [V1] | Wason (1966); Oaksford and Chater (1994, optimal data selection) | High | S7 select: code-run discriminating test, counterexample search |
| Content effects | Performance rises when the rule is a social exchange or deontic rule [V1] | Cosmides and Tooby; von Sydow (2006); Cheng and Holyoak [M] | High | S1 input hygiene: separate content from logical core |
| Belief bias | Believable conclusions accepted 80% of the time versus 33% for unbelievable ones; time pressure and weak instructions raise it, logical-necessity instructions lower it [V3] | Evans, Barston and Pollard (1983); Evans and Curtis-Holmes (2005) | High | S1; S4 test on content-swapped items |
| Dual-process theories | Fast heuristic versus slow analytic reasoning; critiqued as too crude: Evans's five fallacies, single-continuum views (Osman; Cleeremans and Jimenez) [V2] | Wason and Evans (1974); Stanovich and West; Sloman; Kahneman | Med | S0 gate, with caution: the split is contested |
| Single-process versus two-process induction and deduction | Whether the two share one process with separate thresholds | Stephens, Dunn and Hayes (2018) [M, seen in search only] | Low | background only |
| Dual-strategy model of deduction | Counterexample strategy (mental models) versus statistical strategy (probability heuristics) | Beeson et al. (2019) [M, seen in search only]; Chater and Oaksford | Med | S2: which strategy for which item class |
| Syllogistic and conditional reasoning | Quantifiers, "if", atmosphere and matching effects [M] | Evans (1982) | Med | test items for S4 |
| Inductive and category-based reasoning; probabilistic reasoning | Generalising from cases [M] | Osherson et al.; Heit; Oaksford and Chater | Med | S2: candidate rules; G5 probability handled in code |

## Dig into next

1. **Wason task and hypothesis testing.** Questions: (a) Which prompt forms make a model choose a disconfirming test over a confirming one, on rule-discovery tasks? (b) Can code build the single input where two surviving rules differ, and does running it beat a vote at equal tokens? (c) Does the effect depend on abstract versus social-exchange content? Evidence: rule-discovery suites, baseline versus counterexample arm, token counts. Maps to S7 and its [E] counterexample result.
2. **Belief bias and content effects.** Questions: (a) How large is the believable-conclusion bias in our model on matched syllogism pairs? (b) Does a logical-necessity instruction help, as it did for people (it conflicts with our "do not add careful-thinking prompts" note, so test it), or does S1 isolation work better? (c) Is it worse for small models? Evidence: Evans-style 2x2 sets (valid/invalid by believable/unbelievable); accuracy deltas.
3. **Mental models theory.** Questions: (a) Does code-enumerated possibility tables fix errors that step-by-step reasoning leaves? (b) Which task classes show illusory-inference patterns in models? Evidence: Johnson-Laird's item sets, plain versus enumerated arms.

## Does not transfer

Evolved cheater-detection modules, working-memory limits as the cause of omitted models, ability and thinking-disposition differences, and neuroimaging of reasoning (fMRI localisation) are about people. The debate of mental logic versus mental models is about human mechanism; for an LLM only the task effects matter.

## Sources

[V] = opened this session with WebFetch. [M] = from memory or seen only in search snippets, not opened.

1. [V] Wason selection task, Wikipedia: https://en.wikipedia.org/wiki/Wason_selection_task
2. [V] Dual process theory, Wikipedia (first 100k characters read): https://en.wikipedia.org/wiki/Dual_process_theory
3. [V] Belief bias, Wikipedia: https://en.wikipedia.org/wiki/Belief_bias
4. [V] Mental model theory of reasoning, Wikipedia (stub): https://en.wikipedia.org/wiki/Mental_model_theory_of_reasoning
5. [M] Stephens, Dunn and Hayes, "Are there two processes in reasoning?" https://digital.library.adelaide.edu.au/items/0650dbc6-287a-4c36-b391-356f7d78c8a0 (page would not render)
6. [M] Beeson et al., Psychological Topics 2019: https://doaj.org/article/758b6a9bdfcb4282a34988d7d828e63a (403 on fetch)
7. [M] Evans, The Psychology of Deductive Reasoning (1982); Johnson-Laird, Mental Models (1983). No URLs.
