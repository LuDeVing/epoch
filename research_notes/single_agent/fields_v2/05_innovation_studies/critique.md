# Critique: Innovation studies

## What the evidence says in short
Strongest and most useful for us: (1) single-model samples are far too alike, (2) LLM novelty judgments are inflated and LLM judges rank ideas near chance, (3) novelty on paper does not survive execution (one study), (4) LLMs should propose and the program should track, force and select. These match our own results: forced divergence helped open tasks, and selection is the weak link.

## Evidence base problems
- Most LLM evidence is preprints (about 15 of 22 lines in file b). Two lines have no author list captured. Treat effect sizes as soft.
- Heavy double counting. Uzzi 2013 appears four times, Si et al. five times, Wang et al. as a 2016 preprint and a 2017 paper. After merging, several headline claims are single-source: the conventional-core-plus-tail rule, delayed recognition, and the execution flip.
- Memory-only lines: innov-c-14 to c-20 (Uzzi, Wang, Fleming, Mueller, Mullen, Girotra, Doshi). Snippet-only: innov-a-11 to a-18 (Foster, March, Wilden, Getzels, Wu). The brainstorming claim (Mullen, Girotra) is marked established only on unopened memory.
- Human innovation results use citations, journal pairs and patents as outcomes. That measures what the scientific community rewarded, not whether a thought was good. The step from "novel journal pair" to "distant analogy inside one answer" is an analogy, not evidence.

## Contradictions and tensions
- Uzzi says mix mostly conventional with a little novel. Our forced-divergence schema is all novel. Our data (distinct answers 3.18 to 9.63) shows diversity, but the literature says diversity alone is not quality. We have no quality measure for the NoveltyBench win.
- Huang 2023 says self-correction without feedback fails. Our always-doubt schema helped on open tasks. Possible resolution: open tasks reward change, single-answer tasks punish it. Untested.
- Krishnamurthy found GPT-4 can explore when the program supplies a summarised history. Harris and Slivkins found LLMs lose to linear regression. Both back the design (program does bookkeeping) but differ on how much the model can do alone.
- Wu 2019 (small teams disrupt) is contested by disruption-index artefact critiques.

## Missing, would change agent design
- No source on when NOT to diverge. We need a task-type gate (open versus single-answer). This field studies open problems only.
- No evidence on how many ideas to generate versus how to prune: the cost-benefit curve for N. Tian gives one point.
- Little on cheap execution or prior-art retrieval as a measured gain for agents beyond Si 2025.
- A lessons ledger across runs is only inferred from Fleming.
- Analogy quality work (Gentner, Dunbar) and structured methods such as TRIZ are absent.
- Open-ended agent tasks beyond ideation (design, code architecture) are missing. Our architecture-search result has no counterpart here.

## What could be wrong
- Novelty-mirage and time-split studies use LLM judges and small expert pools; both could be noisy.
- Si 2025 had 43 experts and narrow NLP topics. May not generalise.
- Team findings (Wu, Uzzi team claim, Mullen) are weak guides for one model.

## Priority for the schema
Use the claims on sample homogeneity, judge weakness, program-run exploration and external feedback as design rules. Treat the conventional-core mix and the execution flip as hypotheses to test on our own benchmarks.
