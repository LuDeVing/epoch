# Argumentation theory and informal logic: subfields

This field studies how real arguments are built, read and judged. It began with the informal logic movement of the 1970s (Johnson and Blair) and merged with argumentation theory from rhetoric and communication. The Stanford entry on informal logic is divided into systems, standardising arguments, testing arguments (criteria, fallacies, schemes) and contexts. It also has strong ties to artificial intelligence (formal argumentation frameworks). Much of it gives procedures: standardise, diagram, test with named questions.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Argument standardisation and diagramming | Find premises, conclusion, hidden premises; linked versus convergent support | Johnson and Blair; Toulmin | Med | Understand (S1) and represent (S2): restate a claim with its grounds |
| Argument schemes and critical questions | Named patterns (authority, analogy, cause) with questions that test each | Walton, Reed, Macagno, *Argumentation Schemes* (2008) | High | Test (S4): a question list per scheme, run by code for a given type |
| Fallacy theory | Recognised error types | Hamblin; Walton | Med | Input hygiene (S1): appeals to authority or stated guesses go in a marked block |
| Pragma-dialectics | Argument as a critical discussion with rules | van Eemeren and Grootendorst | Low | Background only (multi-party) |
| Argument evaluation criteria | Acceptable, relevant, sufficient premises (ARS) | Johnson and Blair; Govier | Med | Verify (S8) checklist for open answers |
| Formal argumentation frameworks (AI) | Attack graphs, which arguments survive | Dung (1995); Prakken | Med | Select (S7): code computes which candidates survive attacks |
| Informal logic of natural-language deduction | Reading arguments as deductive with added premises | Groarke | Low | Background only |
| Rhetoric and multimodal argument | Persuasion, emotion, images | Gilbert; Tindale | Low | Background only |
| Dialogue types | Persuasion, inquiry, negotiation | Walton | Low | Background; conflicts with G9 (no debate) |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Argument standardisation and diagramming | | not started |
| Argument schemes and critical questions | [`subfields/02_argument_schemes_and_critical_questions/DEEP.md`](subfields/02_argument_schemes_and_critical_questions/DEEP.md) | done, batch 5 (2026-10-27) |
| Fallacy theory | | not started |
| Pragma-dialectics | | not started |
| Argument evaluation criteria | | not started |
| Formal argumentation frameworks (AI) | | not started |
| Informal logic of natural-language deduction | | not started |
| Rhetoric and multimodal argument | | not started |
| Dialogue types | | not started |

## Dig into next

**1. Schemes and critical questions.** Questions: (a) Which five or six schemes (authority, analogy, cause to effect, example, sign) appear in our tasks, and what are their questions? (b) Can a failed critical question be located by code and fed to S5 as the failing output? (c) Does this beat an unstructured "check your reasoning" prompt (SCHEMA 4b says that fails)? Evidence: a scheme catalogue, per-scheme error rates.

**2. Formal argumentation frameworks.** Questions: (a) Can candidates and counterexamples form an attack graph whose accepted set code computes? (b) Does it differ from plain voting? Evidence: examples with conflicting candidates, comparison with the S7 rule.

**3. Standardisation.** Question: does rewriting the task into premises and conclusion improve S1 over plain restatement? Evidence: paired runs on reasoning items.

## Purely conceptual

Pragma-dialectical rules for human discussion, rhetorical theory and theories of persuasion offer no step for one agent, and they bear on debate, which G9 rules out.

## Sources

1. https://plato.stanford.edu/entries/logic-informal/ [V]
2. Walton, Reed, Macagno, *Argumentation Schemes* (2008) [M]
3. Dung (1995), "On the acceptability of arguments..." Artificial Intelligence [M]
4. Toulmin, *The Uses of Argument* (1958) [M]
5. Search result on Walton's schemes and Lumer's 2022 critique, https://erudit.org/en/journals/informallogic/2022-v42-n1-informallogic06950/1088463ar [M] (seen in a search listing only)
