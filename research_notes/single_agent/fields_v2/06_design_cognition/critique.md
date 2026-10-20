# Critique: design cognition (cross-check)

## What holds up
- Reframe on real check output, not on a timer. Two fetched sources support it (Huang 2023, Kamoi 2024). It is the best-grounded rule here.
- Longer or forced deliberation can lower accuracy (Liu, Gema, Chen). This matches our puzzle losses. Gate framing steps to open tasks.
- Model outputs are alike across samples (Doshi, Chen, Bruggeman). This matches our NoveltyBench gain from forced divergence.

## Rests on memory or snippets only
- All classic design-cognition findings: Dorst and Cross 2001, Kruger and Cross 2006, Jansson and Smith 1991, Atman 2007, Adams 2003, Cross 2004, Darke 1979, Schon. No agent opened any of them. The three agents copied the earlier brief, so three matching lines are one source.
- Sio et al. 2015 is a snippet. The "meta-analysis" label is doubtful; the earlier brief called it a review.
- Wadinambiarachchi 2024 is a snippet and measures human users of image generators.
- Kokotovich 2015 and ICCC 2026 paper 78 were unreadable.

## Weak or misleading points
- The strongest negative result (Shin 2025, n=280) tests humans using LLMs. It does not show an LLM-only frame step fails. Use it to demand a test, not to kill M1.
- The strongest positive agent result (Xu 2026) is one preprint on one battery-pack problem. The gain could be a prompt effect.
- Credibility scores look high for memory-only lines (Jansson 75, Dorst 70). Cap them near 50 until fetched.
- Human studies use nine experts on one task. Expert versus novice gaps are confounded by years of practice and tools.
- Independent-source counts can mislead. The Atman/Adams/Cross cluster is one line, and the three Shin entries are one paper.

## Missing, and could change agent design
1. How many options to generate and when to stop: diverge-then-converge tests, brainstorming meta-analyses on quantity versus quality.
2. Faithfulness: does the model use its written frame, or ignore it?
3. Evaluation: how to score novelty and usefulness on open tasks, and judge bias toward long, fluent answers. The agent needs an evaluator.
4. Incubation and delay. For an LLM this means a fresh-context call.
5. Constraint relaxation and representation change in insight problems. This is the closest match to M4.
6. Nominal-group effects: independent generation then pooling beats interacting groups in humans. This tests our multi-call design directly.
7. LLM tests of lessons shown before versus after first generation (fixation from memory).
8. Later replications and critiques of Dorst and Cross.

## Risks to the mechanisms
- M2 (bridge cycle) rests on one nine-person study and has no LLM test. Run it only as an experiment arm.
- M6 (external co-regulator) may suffer from sycophancy if it sees the draft as the agent's own. Use a separate context and a "find what is missing" role.
- M5 may clash with the lessons memory. No evidence either way.

## Bottom line
Supported: gate by task type, reframe on external failure, keep divergence for open tasks, use separate-context critics. M1, M2 and M3 are hypotheses to test at equal tokens on our benchmarks, not findings to build on.
