# Philosophy and logic of scientific discovery: subfields

This field asks how new hypotheses are found, refined and kept or dropped. For most of the twentieth century it was split by the "context distinction": discovery (how an idea arises) was called psychology, and justification (how it is tested) was called logic. The split is now contested. The field today divides into logics of discovery (abduction, heuristics), theories of refinement by anomaly and counterexample (Kuhn, Lakatos), cognitive and computational accounts (analogy, model-based reasoning, machine discovery), and social accounts. The Stanford Encyclopedia entry on scientific discovery has twelve sections that follow this shape.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Abduction and inference to the best explanation | Generating a hypothesis, and choosing the best of the candidates by explanatory virtues | Peirce; Hanson; Harman; Lipton; Douven (SEP "Abduction") | High | Selection (S7) and generation (S3); the "bad lot" problem argues for a "good enough" threshold checked by code |
| Proofs and refutations (conjecture refinement) | How a claim and its proof are repaired by counterexamples: strengthen a lemma, restrict the claim, or refine a concept | Lakatos, *Proofs and Refutations* | High | Revise (S5) and selection by counterexample (S7); a missing slot in SCHEMA section 7 |
| Research programmes | Hard core, protective belt, progressive versus degenerating | Lakatos | Med | Guardrail: when to stop patching (a degenerating signal); impasse detector (S6) |
| Falsificationism | Bold conjecture, severe test, refutation | Popper | Med | Test (S4): prefer tests that could fail; G3 already matches this |
| Anomalies and paradigm change | Discovery starts with an anomaly that resists the current frame | Kuhn (oxygen case) | Med | Impasse (S6) trigger; reframe (O8) |
| Heuristic programming and machine discovery | Discovery as search with heuristics; programs that find laws | Simon, Langley et al.; BACON, KEKADA; King et al. robot scientists | High | Generate and test loop; operators as heuristics; subgoal library |
| Methodologies of discovery | Discoverability, preliminary appraisal, heuristic strategies, schema instantiation | Nickles; Schaffner; Darden; Laudan (pursuit) | Med | Pursuit decision (which idea to spend budget on); S0 gate |
| Cognitive approaches | Analogy, creativity, mental models | Hesse; Holyoak and Thagard; Nersessian; Boden | Med | Operators O7 and O6 |
| Social epistemology of discovery | Cognitive diversity, standpoint | Longino; Weisberg and Muldoon | Low | Background only (single agent) |
| Pragmatic logics (early) | Analysis from effects to causes; the "happy thought", colligation, verification | Newton, Whewell, Dewey | Low | Background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding. The field synthesis is [`SYNTHESIS.md`](SYNTHESIS.md).

| Subfield | Deep document | Status |
|---|---|---|
| Abduction and inference to the best explanation | [`subfields/01_abduction_and_ibe/DEEP.md`](subfields/01_abduction_and_ibe/DEEP.md) | done, batch 4 (2026-10-26) |
| Proofs and refutations (conjecture refinement) | [`subfields/02_proofs_and_refutations/DEEP.md`](subfields/02_proofs_and_refutations/DEEP.md) | done, batch 4 (2026-10-26) |
| Research programmes | | not started |
| Falsificationism | | not started |
| Anomalies and paradigm change | | not started |
| Heuristic programming and machine discovery | | not started |
| Methodologies of discovery | | not started |
| Cognitive approaches | | not started |
| Social epistemology of discovery | | not started |
| Pragmatic logics (early) | | not started |

## Dig into next

**1. Proofs and refutations.** Questions: (a) Can the three counterexample types (hits the conclusion only, a premise only, both) be classified by code from a failing test? (b) Which repair follows each type: add a hidden lemma, replace the premise, or add a condition to the claim? (c) Does a counterexample-driven repair loop beat plain resampling on rule-induction items? Evidence needed: a set of rules with known counterexamples, repair logs, and an equal-token comparison.

**2. Abduction and inference to the best explanation.** Questions: (a) Which explanatory virtues (simplicity, scope, fit) can code compute on candidate programs? (b) How do we guard against the "bad lot" (the best of a poor set)? (c) Does a "good enough" threshold with a discriminating test beat picking by vote? Evidence: ranked candidate pools with ground truth, ablation of each virtue.

**3. Heuristic programming and machine discovery.** Questions: (a) Which BACON-style heuristics map onto our operators? (b) How were search and pruning budgets set in these programs? Evidence: the original program descriptions and reported discovery rates.

## Purely conceptual

The context distinction debate, the question of whether a "logic" of discovery can exist at all, and realism versus anti-realism about explanation give no runnable step. Social epistemology of discovery concerns groups, not one agent.

## Sources

1. https://plato.stanford.edu/entries/scientific-discovery/ [V]
2. https://plato.stanford.edu/entries/abduction/ [V]
3. https://plato.stanford.edu/entries/lakatos/ [V]
4. Lakatos, *Proofs and Refutations* (1976) [M]
5. Langley, Simon, Bradshaw, Zytkow, *Scientific Discovery* (1987) [M]
6. Kuhn, *The Structure of Scientific Revolutions* (1962) [M]
