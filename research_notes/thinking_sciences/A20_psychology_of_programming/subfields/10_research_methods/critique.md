# A20.10 Research methods: cross-check critique

## Corrections and confirmations (sources re-opened this session)
1. METR RCT (arXiv 2507.09089): abstract confirms 16 developers, 246 tasks, 5 years prior experience, forecast 24% faster, post-hoc 20% faster, measured +19% time. NEW detail missing from a/b files: expert forecasts were economists 39% and ML experts 38% shorter. b21 should cite these.
2. Peng et al. (arXiv 2302.06590): 55.8% faster confirmed. The abstract does not give N=95 or the CI; those stay from the earlier read (b04).
3. Turpin et al. (2305.04388): "as much as 36%" accuracy drop, 13 BBH tasks, GPT-3.5 and Claude 1.0 confirmed.
4. Chen et al. (2505.05410): reveal rate "often below 20%", RL plateau and reward-hack non-verbalisation confirmed. The 25% and 39% overall faithfulness figures are from the paper body in c11, not re-checked here.
5. Binder et al. (2410.13787): design (self vs other model predicting M1) confirmed. Specific percentages (32.6 to 49.4, 48.5 vs 31.8) not re-checked.
6. Ahmed et al. (arXiv 2408.05534): six LLMs, ten annotation tasks, five datasets, model-model agreement and confidence as selectors confirmed. Specific alphas not re-checked.
No number was found to be wrong. Not re-opened (rate limits on Semantic Scholar and OpenAlex): Fox et al. 2011 r=-0.03, Nisbett and Wilson 1977, Lindsey 2026, Park 2024.

## Contradictions and tensions
- Duplicate entries: a12/a13/b14/b22/c23/c24 are all Ahmed et al. Counted as ONE independent source in claims (hence "established" for K09 rests on Ahmed plus separate qualitative-coding papers).
- Same for METR (a16, a17, b01, b02, b03, b21) and Turpin/Chen families.
- Recording counts in METR differ by subset: 128 labelled (a17), 74 usable (b02), 44 AI-allowed valid. Not a conflict, different filters.
- c18 text mixes "GPT-5" with R2 for o3; treat as unclear.
- AI productivity: +55.8% (Peng), +26% PRs (Cui), -19% (METR). Differences are plausibly task type (greenfield vs own mature repo) and outcome measure, not resolved.
- Introspection: Binder shows a self-advantage, Song et al. and Lindsey show failure or about 20% success. Status contested.

## Weak spots
- a05, a06, a07, a08 (Nisbett and Wilson, Ericsson and Simon, Fox meta-analysis) were recalled, not opened. Foundations of the method claim K01 rest on b12/b13 (b13 opened).
- b11 (Fucci replications) from a search snippet only; c28 (Montes) second-hand through Ernst and Treude; c32 no numbers.
- Wikipedia pages (a01-a04) give almost no data.
- Few direct tests of think-aloud or protocol analysis on LLM agents; the link from human methods to the agent is by analogy.
- Many LLM-as-annotator results are single-lab 2024-2026 preprints with fast-changing models.

## GAPS
1. Does plain think-aloud style prompting change LLM accuracy (reactivity analogue of Fox et al.), versus explain-style prompting, at equal tokens?
2. How faithful are traces of coding agents (not QA models) to what drives their code edits? No coding-specific faithfulness number yet.
3. Does model-model disagreement predict agent errors well enough to trigger a verification operator (O-level) at equal tokens?
4. What explains the sign difference between METR (-19%) and Peng/Cui (+26 to +56%): task familiarity, codebase size, or outcome metric? Any 2026 follow-up RCT?
5. Do LLM judges favour their own outputs or models of the same family when annotating code artifacts (self-preference bias)?
6. Do the Binder self-prediction gains survive prompting-only (no finetuning) on frontier models?
7. Are there replications of TDD and of student vs professional gaps using LLM agents as the "participants"?
8. Which reporting items (temperature, seeds, versions) change measured agent gains most when varied?
9. Full-text check of Fox et al. 2011 and Nisbett and Wilson 1977 numbers (unopened).

## Gap search results (evidence_d.jsonl, d01-d18)
Search budget: 8 WebSearch calls used; arXiv, Semantic Scholar and OpenAlex APIs were rate-limited (429) for most of the session.

1. Think-aloud vs explain prompting on LLMs: STAYS OPEN. No equal-token study found (d18). Human baseline from Fox et al. only via summary (d01, d02).
2. Coding-agent trace faithfulness: STAYS OPEN. Only failure-analysis papers, none measuring trace-vs-edit (d16, d17). Note non-mention may understate faithfulness (d17).
3. Disagreement as an error signal: PARTLY CLOSED. Yes for code at task level (66-69% detection, d09) and for agent runs (d08); weak at ceiling and blind to shared errors (d10). Equal-token trigger test not found.
4. METR vs Peng/Cui: PARTLY CLOSED. METR 2026 follow-up exists (d06): 18% and 4% speedups, CIs include zero, selection effects, design retired. Task familiarity vs outcome metric still not separated.
5. Judge self-preference on code: PARTLY CLOSED. Small and model-specific (d05), mostly legitimate on verifiable tasks and cut by reasoning (d03); human-vs-judge bias in code is about length and position (d04). Only 2023-24 judges in d05.
6. Binder gains prompting-only: STAYS OPEN. Song et al. find no self-access by prompting in 21 open models (d13); injection detection is content-agnostic (d14). No frontier-model prompting-only replication found.
7. TDD / student-professional replication with LLM participants: STAYS OPEN. Only tests-in-prompt help (d15).
8. Reporting items that matter most: PARTLY CLOSED. Top-p (about 12 points) and T=0 non-determinism (18-44% of problems differ) shown (d11, d12); seeds and version drift not isolated.
9. Fox 2011 and Nisbett and Wilson full text: STAYS OPEN. r=-.03 and 94 studies only via summaries; secondary page confirms 94 studies and direction but not r (d02). Nisbett and Wilson not retrieved.

Claims: K01, K03, K04, K13, K15 got new evidence ids and notes; K16-K19 added (K19 lists the open gaps).
