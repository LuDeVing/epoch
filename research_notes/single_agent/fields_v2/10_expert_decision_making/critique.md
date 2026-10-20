# Critique: expert decision making (cross-check)

## What the set supports
Three claims are established with independent sources: self-correction fails without external feedback; multi-agent debate does not reliably beat sampling at matched cost; Einstellung is real but bounded to good-but-not-best first answers. Two minor ones are also established (chess memory, LLM syllogism biases). These back the plan: use checkers and runs, not self-review; gate forced doubt to open tasks.

## Counts are thinner than they look
About 56 evidence lines reduce to 25 claims. Many lines repeat one paper (Hagendorff four times, Turpin twice, Sprague twice, Panickssery three times). Raw line counts overstate support. Only 5 claims have two or more independent sources.

## Weak or memory-level
- Pre-mortem: no study here shows better decisions. The 1989 paper and Veinott 2010 were not opened (snippets only). Marked contested.
- MedEinst and PreFlect are single preprints, abstract only, credibility under 60. The old 60.9% figure is unverified and must not be used.
- Tetlock fox and hedgehog rests on a commentary snippet.
- Klein's recognition-primed model, de Groot's progressive deepening and Johnson-Laird's mental models have no fetched primary source in this round. They stay memory-level from the earlier brief. Mechanisms M1, M3 and M6 rest on them.
- Feeling of rightness and the argumentative theory are each one source, and neither was tested on LLMs.
- The Kahneman and Klein review is a consensus statement, not an experiment.

## Gaps that could change agent design
1. No evidence on whether agreement across samples predicts correctness. Kim 2025 (60% shared wrong answers) suggests it is weaker than hoped. This is the core of the router and it is open.
2. No test that recognize-then-simulate, progressive deepening, or a counterexample step helps an LLM. All three are human-transfer guesses.
3. External verification was not studied directly. Stechly shows a sound verifier gives large gains. The strongest lever is probably "run the code or check the examples".
4. Little on when a second look helps or hurts. Our own ARC and word-puzzle data is the only evidence.
5. Naturalistic decision research outside chess (firefighters, nurses) has no fetched empirical source, and Klein's critics are not covered.
6. Small-model transfer: most LLM studies use GPT-4 class models; we run smaller ones.

## What could be wrong
- Chess findings may not transfer: Einstellung needs trained pattern memory, and the model's version is unknown.
- The chain-of-thought harm result (o1 vs GPT-4o) is one preprint and may be model-specific.
- Debate critiques use older models; newer reasoning models may differ.
- The Macnamara and Sala-Gobet numbers are abstract-level; the numeric r for Sala-Gobet was lost.
- Hagendorff CRT figures differ in wording between b-13 and c-14; re-open the tables before quoting.

## Bottom line
Keep: external checker first, hidden authorship in critics, forced doubt only on open tasks, agreement as a weak signal. Treat pre-mortem, progressive deepening, chunk ledger and counterexample hunt as hypotheses to test in our harness, not as evidenced steps.
