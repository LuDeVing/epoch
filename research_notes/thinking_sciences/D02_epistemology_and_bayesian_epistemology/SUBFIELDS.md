# Epistemology and Bayesian epistemology: subfields

Epistemology asks what knowledge and justified belief are and how evidence should change belief. It divides into traditional epistemology (analysis of knowledge, justification, scepticism), formal epistemology (probability, belief revision, decision), and social and virtue branches. The formal branch is the part that gives procedures. The Stanford entry on Bayesian epistemology is organised as: formalism, coherence norms (synchronic), the problem of the priors, update norms (diachronic), and idealization.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Bayesian conditionalization | Update by setting credence in what the evidence rules out to zero and rescaling the rest | Bayes; Ramsey; de Finetti; SEP "Bayesian Epistemology" | High | Selection (S7): code normalises probabilities over exclusive answers (G5) |
| Coherence norms and Dutch book arguments | Why credences should obey probability | Ramsey; de Finetti | Med | Guardrail: forced sum to 1 over exclusive answers |
| The problem of the priors | Where starting credences come from; subjective versus objective Bayesianism | Jaynes; Principle of Indifference; Bertrand's paradox | Med | Memory: class record gives a measured prior (S0 gate) |
| Uncertain evidence | Updating when evidence is not certain | Jeffrey conditionalization | High | Test (S4): a noisy check shifts but does not zero a candidate |
| Imprecise credences | Intervals instead of a number | Keynes (two urns); Levi | Low | Background only; maybe an "unknown" flag |
| Belief revision (AGM) | Expansion, contraction, revision of a belief set; entrenchment | Alchourron, Gardenfors, Makinson; Darwiche and Pearl for iteration | High | Revise (S5): which belief to give up when a check contradicts; keep best-so-far |
| Formal learning theory | When a procedure converges to the truth | Gold; Kelly | Low | Background only |
| Justification theories | Foundationalism, coherentism, reliabilism, evidentialism | Goldman; Conee and Feldman | Low | Background only (reliabilism hints: weight sources by track record) |
| Social epistemology | Testimony, peer disagreement | Goldman; Christensen | Med | Guardrail G4: samples are not independent peers |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Bayesian conditionalization | | not started |
| Coherence norms and Dutch book arguments | | not started |
| The problem of the priors | | not started |
| Uncertain evidence | | not started |
| Imprecise credences | | not started |
| Belief revision (AGM) | [`subfields/06_belief_revision_agm/DEEP.md`](subfields/06_belief_revision_agm/DEEP.md) | done, batch 5 (2026-10-27) |
| Formal learning theory | | not started |
| Justification theories | | not started |
| Social epistemology | | not started |

## Dig into next

**1. Belief revision.** Questions: (a) Can a candidate set be held as a belief base with an entrenchment order given by test results, so that a failed check drops the least entrenched member? (b) How does iterated revision (Darwiche and Pearl) constrain repeated S5 rounds? (c) Does it beat "rewrite from scratch"? Evidence: logged revision rounds with outcome flips.

**2. Conditionalization and Jeffrey updating.** Questions: (a) What likelihood should a pass or fail of a given check carry, estimated from our own class records? (b) How to treat a test the answer was fitted to (likelihood near 1, so no update)? (c) Does a posterior over candidates select better than "first to pass"? Evidence: per-check hit rates from our runs, calibration plots.

**3. Imprecise and prior-setting work.** Question: can the class record serve as an objective prior for the S0 gate, and does a wide interval trigger more sampling? Evidence: pass rates by class with sample sizes.

## Purely conceptual

The analysis of knowledge (Gettier cases), the regress problem, scepticism, and the internalism versus externalism debate give no step to run. Dutch book and accuracy arguments justify the norms but do not add procedure.

## Sources

1. https://plato.stanford.edu/entries/epistemology-bayesian/ [V]
2. https://plato.stanford.edu/entries/logic-belief-revision/ [V]
3. Alchourron, Gardenfors, Makinson (1985), "On the logic of theory change" [M]
4. Jeffrey, *The Logic of Decision* (1965) [M]
5. https://plato.stanford.edu/entries/abduction/ [V] (for the link between explanation and priors)
