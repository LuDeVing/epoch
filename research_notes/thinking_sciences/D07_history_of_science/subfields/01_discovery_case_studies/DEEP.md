# Discovery case studies: deep document

*Subfield D07.01. Source files in this folder: evidence_a-d.jsonl (ids a01-a28, b01-b25, c01-c25, d01-d18), claims.jsonl (K01-K27), critique.md. Evidence ids are in square brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

*Honest summary of the evidence base. The stated value of this subfield is "source of operator sequences". The only operator sequence we read first-hand is KEKADA (64 heuristics, two cases, results typed in by a user). The founding case volume (Nickles 1980), the BACON book (Langley et al. 1987), Holmes on Krebs and Gruber on Darwin were never opened. Most hard numbers come from LLM benchmarks on equation discovery. The step from a historical operator to a gain for our agent is a hypothesis, not a finding.*

## 1. What it is

Discovery case studies are detailed accounts of single scientific discoveries. They use notebooks, diaries, letters and papers to rebuild what the scientist did, in what order, and why. Nickles (ed.) 1980, *Scientific Discovery: Case Studies*, is the founding volume. Its companion, *Scientific Discovery, Logic, and Rationality*, holds the logic essays [a01]. Together they revived the claim that discovery can be studied by reasoning, not only the justification of finished theories.

Three kinds of work sit under this heading.

1. **Historical and cognitive-historical reconstructions.** Krebs and the urea cycle (Holmes), Faraday's diary (Tweney), Kepler and Mars (Hanson, Lugg), Darwin's notebooks (Gruber). The unit is one scientist and one problem.
2. **Computational rediscovery.** Production-system programs built from a case: BACON (Kepler's third law, Boyle, Snell), KEKADA (Krebs), and others from Langley et al. 1987 (GLAUBER, STAHL, DALTON). They give "how possibly" accounts [a02, b02, c22].
3. **LLM-era rediscovery and discovery benchmarks.** AI Feynman, LLM-SR, LLM-SRBench, NewtonBench, DiscoveryBench, DiscoveryWorld, ScienceAgentBench, MOOSE-Chem, ResearchBench, Co-Scientist, Kosmos, AI-Newton, AI Scientist.

Why it matters for our agent. The schema has states S0-S9 and operators O1-O8. Case studies are the one place to look for what a real thinker did after an impasse. They hint at what belongs in S6 (impasse), S9 (look-back), O7 (analogy) and memory. They do not prove it. A program that reproduces a history shows that its rules are sufficient, not that they are necessary or that scientists used them [a02, b02, K16].

## 2. History and theories in depth

### 2.1 Philosophy: the logic of discovery

Hanson (1958, *Patterns of Discovery*) took Kepler's finding of the elliptical orbit of Mars as the model of abductive discovery: reasoning from a surprising fact to a hypothesis that would explain it. Lugg (1985) disputes that this reconstruction matches what Kepler did [a09]. No one has measured how far a rational reconstruction differs from a real trace. It stays an argument, not a number [K27].

Nickles and the Reidel volumes brought back the idea that there is a reasoned path to discovery, not only luck [a01]. The case volume itself was not opened [a01, c23].

### 2.2 Simon's programme: discovery as problem solving

Simon, Langley and colleagues recast science as problem solving, so heuristic search could be applied to history [a02]. Two goals exist for such programs: model human cognition, or use computation to get around human limits. The second kind need not be realistic to be useful [a04]. Darden (1997) relays a cognitive-science finding: humans fix on one hypothesis too early and do not search the hypothesis space systematically. Programs search more systematically. Example: MECHEM found reaction pathways chemists had missed [a03]. No effect size is given.

**BACON.** Detects regularities in tables with rules like "if two terms increase together, consider their ratio." It rediscovers Kepler's third law (D^3/P^2 = c), Boyle's law and Snell's law [a10, b02]. The programmers chose the data, so the representation may do much of the work [c22].

**KEKADA.** A production system built from Holmes's reconstruction of the Krebs urea-cycle work (Jul 1931 to Apr 1932) [d01]. It is the only operator-level source we read first-hand (section 4).

### 2.3 Critique

Downes (1990) is the core critique [b01-b03].
- Lab notebooks are not think-aloud protocols. Heuristics read out of them are inferred.
- Published papers give tidy reasons after the fact (Nisbett and Wilson 1977). Millikan's notebooks hold columns of numbers and notes such as "beautiful, publish this", not records of thought.
- Krebs case: the assistant Henseleit did much of the bench work and note-taking, yet KEKADA models one solitary mind.
- Simon claims only sufficiency. No test of necessity exists.
- Discovery is partly social (acceptance; Brannigan 1981), and the programs ignore that.

### 2.4 Cognitive-historical and in-vivo work

- **Tweney on Faraday.** The diary has 16,041 numbered entries (1832-1860). He built retrieval slips and at least 12 types of sheets to reorder entries and draft papers. The notebook was an active tool [b05]. More than 600 surviving specimens from the 1856 gold research were keyed to diary entries, and some experiments were redone to retrace how confusion became lawful relations [b04]. The 16,041 count was not re-confirmed by the checker [critique, K17].
- **Dunbar** (in-vivo lab studies, via SEP). Scientists fixing an experimental problem take analogies from very similar domains. Those building new models use less similar ones. Far analogies are rare [a11].
- **Nersessian** (via SEP). Conceptual innovation uses analogical, visual and simulative modelling, including thought experiment [a12].
- **Thagard and Holyoak 1996.** Analogical transfer is constrained by direct similarity, structural parallels and the investigator's purposes [a13].
- **Grasshoff and May.** The Krebs-Henseleit notebooks survive in full. The project rebuilt the discovery in a program (Urea Modeler) to study how mistakes were found and fixed and where hypotheses came from [a08].
- Other works: Gooding 1990, Gorman 1997, Klahr and Simon 1999, Nersessian 1999, Tweney 2001. All lean on a few richly documented cases [b25]. We read only the citation list.

Dunbar, Nersessian and Thagard claims come from SEP summaries, not the papers [critique].

### 2.5 From history to LLM benchmarks (2020-2026)

The classic test became "rediscover a known law." AI Feynman (Udrescu and Tegmark 2020) solved all 100 basic Feynman-lecture equations [b06]. With LLMs came a worry: the model may have memorised the law. That led to tests built to defeat recall: LLM-SRBench (rewritten and invented equations), NewtonBench (counterfactual law shifts), MOOSE-Chem and ResearchBench (post-cutoff papers), and end-to-end tests (DiscoveryBench, DiscoveryWorld, ScienceAgentBench). Section 3 has the numbers.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Classic rediscovery test | AI Feynman: 100/100 basic equations, Eureqa 71%; 20 bonus equations AI Feynman 90%, Eureqa 15% | Udrescu and Tegmark 2020 [b06] | [E] but clean textbook data |
| Rediscovery of famous laws is inflated by memory | LLM-SR reaches low error on Feynman problems in under 20 iterations; Mixtral perplexity 1.94-2.04 on Feynman items vs 6.24 on a new-benchmark item | LLM-SR appx C [b07] | [E] (K01) |
| Best system on rewritten equations is weak | 31.5% symbolic accuracy (LLM-SR, GPT-4o-mini, LSR-Transform); 239 problems (111 Transform + 128 Synth) | LLM-SRBench [b08, c01] | [E] |
| LLM-SR on LSR-Synth (GPT-4o-mini) | chemistry 11.1, biology 16.7, physics 9.9, material science 20.2. The abstract's "28.1%" is one cell (LaSR GPT-4o-mini, material science), not an average | [c01, critique item 1] | [E] |
| A real fit-and-feedback loop beats no-data prompting | LSR-Transform symbolic accuracy, no data vs LLM-SR: Llama-3.1-8B 3.61 vs 30.63; GPT-3.5 2.10 vs 10.81; GPT-4o-mini 7.21 vs 31.53 | LLM-SRBench Table 1 [d08, b08] | [E] (K03) |
| LLM-SR ablation (Oscillation 2, GPT-3.5) | NMSE without iterative refinement 1.01e-1 in-domain, 1.81e-1 OOD; without skeleton + optimiser 3.78e-1 / 3.75e-1; dropping the natural-language prior hurt considerably | [a22, c16] | [S] one problem |
| LLM-SR vs classic symbolic regression | E. coli growth OOD NMSE about 0.0037 vs >1 for baselines; 2.5K iterations vs 2M+ | [a21, c16] | [S] authors' own problems |
| The memory effect grew with newer models | LSR-Transform no-data symbolic accuracy 2.10-7.21 (GPT-3.5, Llama-3.1-8B, GPT-4o-mini) vs 28.83-35.14 (Nemotron-ultra-253b 28.83, Kimi-K2 30.63, Qwen-3-next 33.33, o4-mini 34.23, GPT-4.1 35.14). On NewtonBench no-data is 0 for 3 models | NewtonBench appx E.1 [d09] | [E] (K01, K20) |
| Original vs transformed gap | Direction stated ("substantially more challenging"); gap in points is in a plot, not read | [d08, b10] | OPEN |
| Metric choice flips rankings | LaSR: Acc0.1 45.94-50.45% but symbolic 5-13% (6.31 for GPT-4o-mini); LLM-SR: Acc0.1 10.81-39.64%, symbolic 11-31% (39.64 and 31.53 for GPT-4o-mini). Symbolic accuracy correlates positively with OOD Acc0.1 | [b09, c02, c03] | [S] (K04) |
| Counterfactual law shifts separate reasoning from recall | NewtonBench, 324 tasks, 12 physics domains, 11 LLMs, 4 runs: GPT-5 75.9, Gemini-2.5-pro 65.4, GPT-5-mini 53.1, o4-mini 47.8, DeepSeek-R1 43.4, Qwen3-235B 30.9, GPT-4.1 5.8, GPT-4.1-mini 5.1. Hardest setting: GPT-5 40.3, Gemini-2.5-pro 16.7, others <6 | [b11, c04] | [S] (K02) |
| Code interpreter helps weak, hurts strong | GPT-4.1 5.8 to 18.9; GPT-4.1-mini 5.1 to 14.7; GPT-5 75.9 to 73.3; GPT-5-mini 53.1 to 48.1; Gemini-2.5-flash 50.6 to 40.9. Exploration keywords fell sharply for Gemini-2.5-flash at code budget 1 | [b12, c05] | [S] (K10); mechanism is the authors' reading |
| Symbolic accuracy is fragile to noise | Noise 0.0001 cuts GPT-5-mini symbolic accuracy 12-16%; keeps falling to noise 0.1; RMSLE stays stable | [b12, c06] | [S] (K11), one model |
| End-to-end agents are weak (DiscoveryBench) | 264 real + 903 synthetic tasks, 6 domains. Best non-oracle HMS 16.3; best with oracle (Reflexion) 24.5 | [a14, b13, d07] | [E] (K05) |
| DiscoveryBench DB-REAL (GPT-4o / GPT-4p / Llama-3-70B) | NoDataGuess 0.0 / 4.7 / 11.5; CodeGen 15.5 / 16.3 / 12.1; ReAct 15.4 / 15.6 / 13.5; DataVoyager 15.4 / 13.9 / 11.5; Reflexion (oracle) 24.5 / 19.5 / 22.5 | [d07] | [E], one run per cell |
| DiscoveryBench DB-SYNTH | CodeGen 14.1 / 8.7 / 10.9; ReAct 11.6 / 7.4 / 12.0; DataVoyager 5.7 / 6.9 / 11.7; Reflexion 15.7 / 12.9 / 23.2 | [d07] | [E], one run per cell |
| Memory share of the code-agent score | No-data guess = 0% (GPT-4o), 29% (GPT-4p), 95% (Llama-3) of CodeGen | [d07] | [E] (K20) |
| DiscoveryBench failure analysis | Best agent by workflow: correlation analysis 55, data selection 18, summary statistics 18; spatial analysis, pollen dating, ecological modelling 0. By domain: biology 0, engineering 7, economics 25, sociology 23. Domain knowledge, archaeology: 9.9 to 17.5 (DataVoyager GPT-4o; garbled text) | [a15, a16] | [S] |
| DiscoveryWorld humans vs agents | 120 tasks (8 topics x 3 levels). 11 scientists, 1 hour: completion 66%, knowledge 55%, 11 of 16 tasks above 60%. Best agent ReAct 38% easy, 18% challenge; Hypothesizer knowledge 34% easy, 8% challenge | [a18-a20, b14, c07] | [E] (K05) |
| DiscoveryWorld agent table | Easy: ReAct procedure 0.59, completion 0.38, knowledge 0.25; Hypothesizer 0.56, 0.28, 0.34. Challenge: ReAct 0.63, 0.18, 0.10; Hypothesizer 0.49, 0.08, 0.08. 5 seeds per cell, GPT-4o | [d12] | [E] |
| Agents act but fail to conclude | Proteomics Easy ReAct procedure 0.87, completion 0.20. Reactor Lab regression completion 0.00 in all 9 cells, procedure 0.38-0.51 | [d12] | [S] location inferred from scores |
| "Parts work, chaining fails" is not supported | The 10 unit tests are generic skills (dialog, doors, pick-and-place). Mean completion 0.60 / 0.44 / 0.64; navigation tests 0.00-0.20 | [d12] | Downgraded (K06) |
| Completion overstates discovery | Humans: knowledge 55% below completion 66%; brute force (all crystal frequencies) instead of a regression | [a20, c08] | [S] (K12) |
| ScienceAgentBench | 102 tasks, 44 papers. Best 32.4%; 34.3% with expert knowledge; o1-preview 42.2% at over 10x cost; Claude-3.5-Sonnet self-debug solved 10.8% more tasks than OpenHands CodeAct at 17x lower cost | [a26, b22, c18] | [E] |
| MLAgentBench | 13 tasks; best (Claude v3 Opus) 37.5%; 100% on old datasets, 0% on recent Kaggle | [a27] | [S] |
| Inspiration retrieval is the strong step | MOOSE-Chem, 51 post-Jan-2024 papers, corpus 300, hit ratio at top 20% / 4% / 0.8%: GPT-4o 96.7 / 83.7 / 60.8; Llama-3.1-70B 95.1 / 83.0 / 59.5; 405B 95.7 / 78.7 / 52.7; 8B 71.6 / 43.5 / 26.8. Corpus 1000 at top 4%: 88.9 | [b15, c09] | [E] (K13) |
| Staged framework beats one-shot | GPT-4o-judged Top Matched Score: MOOSE-Chem 4.020, MOOSE 2.882, Qi et al. 2.686, SciMON 2.549; without multi-step 3.765; without multi-step and evolution 2.863. Average Matched Score barely moves (2.56 vs 2.46). Expert top-score counts over 51: 5:0, 4:2, 3:19, 2:16, 1:8, 0:6 | [c10] | [S] LLM judge |
| ResearchBench | 12 disciplines. Top-20% round about 80% of true inspirations. Final round (top 4%, 3 of 75): above 40%, GPT-4o 45.65. Extraction checked by 5 PhD students: 91.9% (major issues) / 82.3% (all). Strong position bias in pairwise ranking | [b17, c11, c12] | [E] |
| LLM ideas rated more novel, not more feasible | Novelty: human 4.84, AI 5.64, AI + rerank 5.81; 49 ideas per condition; 79 reviewers; 298 reviews; reviewer agreement 56.1% | Si et al. [b18] | [S] (K15) |
| Idea generation collapses | Of 4000 seeds per topic only about 200 non-duplicates (cutoff 0.8) | [b19] | [S] |
| LLM judges of ideas are weak | GPT-4o direct ranking 50.0% balanced accuracy vs human reviewer consistency 56.1% | [b19] | [E] (K14) |
| AI Scientist | Under $15 per paper; reviewer F1 0.57 vs 0.49, AUC 0.65 both; GPT-4o reviewer 70% accuracy, balanced accuracy 0.65 vs 0.66; score correlation 0.18 vs 0.14 between two humans; papers hold hallucinated tables and invented facts | [a25, b21, c19] | [E] (K14); same paper, different metrics |
| GPT-4o as equation judge | 123 of 130 (94.6%) raw agreement with two authors; no kappa | [d10, b08] | [E] narrow task (K24) |
| HypoGeniC | Over few-shot: +31.7% (synthetic), +13.9 / +3.3 / +24.9% (three real sets); +12.1 / +11.6% over supervised on two | [b20] | [S] classification, not laws |
| Outside search separates new from known | Novelty score for already-published ideas 6.14 to 2.38; correctness 7.4 to 8.46 (Co-Scientist, 200-item post-cutoff benchmark) | [c14] | [S] LLM ratings |
| Co-Scientist case | cf-PICI mechanism proposed in about 2 days; n = 1, no repeat, no leak control; Elo rises with compute over 203 goals; AML IC50 as low as 2 nM in 3 of 4 lines | [b23, c13, d14] | [S] (K26) |
| Kosmos | 79.4% of 102 statements accurate (85.5 data analysis, 82.1 literature, 57.9 synthesis); average run 42,000 lines of code, 1,500 papers, 166 data-analysis + 36 literature rollouts; pre-cutoff rerun reproduced findings | [c15, d13] | [E] interpretation weakest (K25); raters are collaborators |
| AI-Newton | 46 mechanics experiments, about 48 h, up to 1200 trials, about 90 concepts and 50 laws per run; rediscovered Newton's second law, energy conservation, gravitation | [b24, c20] | [S] simulated, hand-built concept language |
| Independent sampling vs teamwork | 10 independent vs 1: +0.70 held-out Q (95% CI 0.41-1.03), 86 wins / 11 losses / 3 ties on 100 Qwen problems; ring communication -0.33. Complete minus Independent +0.10 or -0.75 by selection rule | Shi et al. [c21, d15] | [C] (K09) |
| Equal-token studies (not discovery) | Single agent matches or beats multi-agent at equal thinking tokens on multi-hop QA. 260 configurations: change vs single agent from +80.8% (decomposable) to -70.0% (sequential); cross-validated R^2 = 0.373 | [d16, d17] | context only |
| KEKADA structure | 64 heuristics (31 domain-independent, 33 domain-specific); one problem-generator rule | [d01] | [E] first-hand |
| Krebs timeline | About 16 weeks to first surprise (Jul 26 to Nov 15 1931); about 4 weeks re-verifying; about 8.5 weeks of scope tests; about 5 method shifts in 8.5 months | [d05] | [S] second-hand |
| Kepler | At least 70 repetitions of the vicarious-hypothesis routine; about 5.5 years start to manuscript | [d06] | [S] tertiary |

## 4. Mechanisms and models

Written so an engineer can implement them. Each is a hypothesis to ablate, not a proven mechanism (K16, K22).

### 4.1 KEKADA control loop (first-hand, [d01-d04])

**Data structures.**
- A hypothesis list. Each hypothesis has a confidence record with five counters: success, failure, failed-effort, implied-success, implied-failure.
- A task agenda with priorities.
- A knowledge base of past outcomes per experiment type.

**Normal mode: breadth-first.** Loop over hypotheses and their experiments.
1. Pick a problem (problem-choosers PC1-PC7 pick the phenomenon, here urea synthesis).
2. Propose an experiment (experiment-proposers EP1-EP8).
3. **Set an expectation before running it** (ES1): expected value from earlier runs, with lower bound, upper bound and a tolerance.
4. Run it. In KEKADA the user types the outcome (E1). In our agent, code runs it.
5. Compare with the expectation. Inside the bounds: update confidence and continue.

**Surprise mode: depth-first without backtracking.** If the outcome violates the bounds:
1. PG1 turns the puzzling phenomenon into a task.
2. PC8 gives a new puzzle task priority over all others. Earlier goals are dropped.
3. Try explanations in a **fixed order** (DM9): (1) a known factor, such as a stimulant that may be necessary; (2) divide and conquer on subprocesses; (3) scope of the phenomenon (does a whole class do the same); (4) anything else. The authors say the order stands in for Krebs's unknown prior experience.
4. Hypothesis generators: HG1 a class of substances shows the same outcome (scope); HG2 a missing substance causes the low output; HG3 divide and conquer; HG5 an intermediate exists; HG7 mixed versus additive action.
5. A hypothesis goes inactive after a set number of failed experiments or failed effort (HM4, HM5).

**Scope rule.** More than 3 members with the effect generalises the claim. More than 3 without it makes the scope hypothesis inactive.

**Five domain-independent strategies** [d04]:
1. Magnification: vary apparatus variables to enlarge a small effect.
2. Scope: test whether a class shows the effect.
3. Divide and conquer: split the process.
4. Factor analysis: remove one entity at a time.
5. Relate two anomalies that share a variable.

**Run on urea synthesis** [d03]. Test alanine alone, ammonia alone, both. Alanine gave less urea than the lower bound (surprise 1). Three explanations opened. Missing substance (glucose, fructose) failed. The subprocess idea re-confirmed known facts. The class idea led to amino-acid testing until ornithine, which with ammonia gave about double the ammonia-only rate (surprise 2). Scope tests found no other substance with the effect. Then a catalyst test (25 urea per ornithine in simulation, 24.5 in Krebs's Apr 13 experiment). Then the citrulline intermediate.

**Second case, glutamine** [d04]. Magnification failed first. Then scope tests (4 amino acids needed to generalise). Then a glutamic-acid surprise, then an arsenite surprise, then glutamine.

**Caveats.** The user supplies results and some choices (DM10). Rules are hand-written, not learned. "Only minor differences" from Krebs is stated, not measured. No experiment count is given for the simulated run. No run without the surprise rule exists. The authors call surprise-chasing "counterintuitive" but say it "works quite well in the scientific domains we have examined" [d04].

### 4.2 BACON-style data-driven cycle [a10, b02, c02]

Look at a table of values. If two terms increase together, consider their ratio. If a term is constant, record a law. If one rises as the other falls, consider their product. Add the new term to the table and repeat. LLM-SR is the modern form: the LLM proposes forms, code fits constants, the error is fed back.

### 4.3 LLM-SR loop [a21, c16]

1. The LLM writes an equation as a program skeleton, using the scientific context in the prompt.
2. An optimiser fits the constants to data.
3. The score is stored in a multi-island memory of best programs.
4. Best programs go back into the next prompt, and the LLM proposes improvements.
5. Repeat about 2.5K iterations.

Ablations (section 3) show each part adds value: iterative refinement, the skeleton plus separate optimiser, and the natural-language prior.

### 4.4 MOOSE-Chem decomposition [b15, b16, c09, c10]

A hypothesis is background plus inspirations.
1. **Retrieve** inspirations: screen the corpus in windows of 15 papers, keep 3, repeat until the top 4% remain.
2. **Compose** a hypothesis from background plus inspiration, with mutation and multi-step refinement.
3. **Rank** the hypotheses.

The authors call the sufficiency of these three subtasks a bold assumption. The gain is in best-of-many, not in average match.

### 4.5 AI-Newton plausible reasoning [c20]

Keep a base of concepts and laws. If a law holds in many experiments but fails in one, add a simple term to fix it. Concepts appear in order (mass before force; potential energy appears when conservation is extended to springs).

### 4.6 Kosmos world model [c15]

A shared structured store of findings keeps about 200 rollouts and 12 hours coherent. Data-analysis and literature agents write to it and read from it. Reports are built from it.

### 4.7 Faraday's retrieval sheets [b05]

A raw log is not enough. Faraday built indexes and re-ordered entries by topic to draft papers. Mechanism: write the raw log, then build a topic-keyed view of it before reasoning.

## 5. What holds up

### 5.1 Multi-source results

- **Memory inflates rediscovery** [K01]. LLM-SR appendix, LLM-SRBench and the NewtonBench appendix agree in direction [b07, c01, d09]. The size is not stable across models (5.3).
- **A data-fit loop beats no-data prompting** [K03]. LLM-SR ablation and LLM-SRBench tables agree [a22, d08].
- **Interpretation is the weak step** [K25]. Two teams, two systems: Kosmos synthesis 57.9% against 85.5 and 82.1; DiscoveryWorld procedure high, completion low, Reactor Lab regression 0.00 [d12, d13]. Kosmos raters are collaborators; the DiscoveryWorld location is inferred.
- **LLM judges of ideas are poor** [K14]. GPT-4o 50.0% against human 56.1%. The AI Scientist reviewer matches humans on some metrics while its papers carry invented results [b19, b21, c19].
- **End-to-end agents are weak** [K05]. DiscoveryBench, DiscoveryWorld and ScienceAgentBench agree.
- **Inspiration retrieval works** [K13]. MOOSE-Chem and ResearchBench agree on different corpora.
- **Structured shared state for long runs** [K19]. Kosmos, AI-Newton, Co-Scientist. Mostly self-reported.

### 5.2 Failures and null results

- **Heavier reasoning scaffolds did not beat a plain code agent** in DiscoveryBench. ReAct minus CodeGen on DB-REAL: -0.1, -0.7, +1.4. DataVoyager minus CodeGen: -0.1, -2.4, -0.6. On DB-SYNTH DataVoyager GPT-4o scores 5.7 against 14.1 [d07]. Contested because DataVoyager gained from domain knowledge in archaeology (9.9 to 17.5) [a16].
- **Self-debug beat a heavier agent** in ScienceAgentBench: 10.8% more tasks at 17x lower cost [c18].
- **A code tool hurt strong models** in NewtonBench (GPT-5 75.9 to 73.3; Gemini-2.5-flash 50.6 to 40.9) and helped weak ones [c05].
- **"Parts work, chaining fails" was wrong.** The DiscoveryWorld unit tests were generic skills [d12].
- **The "no-data guess equals code agent" reading was a misread table.** The correct values are 0.0 / 4.7 / 11.5 against 15.5 / 16.3 / 12.1 [d07].
- **Teams that talk lost to independent tries** in one preprint (5.3 gives the limits).

### 5.3 Moderators and boundary conditions

- **Model generation.** No-data score on LSR-Transform rose from 2-7% to 29-35% across generations on the same 111 items [d09]. Rewriting no longer blocks recall for strong models. The o4-mini example derives the transformed form from the textbook law: derivation from memory, not string recall.
- **Model strength.** Code helps models under about 40% symbolic accuracy and hurts above that [b12, c05].
- **Task type.** Interactive probing (NewtonBench) against fixed data (ScienceAgentBench, LLM-SR). Code loops help the second more. Not resolved.
- **Metric.** Numeric and symbolic accuracy flip method rankings [b09].
- **Noise.** 0.0001 noise cuts symbolic accuracy 12-16% for one model [c06].
- **Selection rule** (Shi et al.). Complete minus Independent is +0.10 under archive-wide selection and -0.75 under final-round selection [d15]. 9 of 20 prespecified interactions survived Holm correction.
- **Oracle feedback.** Reflexion's gain needs an oracle match signal (24.5 against 15.5 for GPT-4o). No oracle exists in real use [d07].
- **Domain.** DiscoveryBench biology 0%, engineering 7%, economics 25%, sociology 23% [a15].
- **Newer tasks.** MLAgentBench ranges from 100% on old datasets to 0% on recent ones, which may be missing memory rather than missing skill [a27].

### 5.4 Weak points in the evidence

- All KEKADA facts come from tech reports by its builders. Results are typed in. The Krebs fit is stated, not measured [d03, d04].
- Krebs timeline counts are second-hand through Kulkarni and Simon from Holmes [d05]. "Impasse" is our label. The sources describe negative results and a change of line, not a feeling of being stuck.
- Kepler's 70 repetitions come from Wikipedia's summary of Kepler's own words [d06]. It counts one subroutine.
- Most judges are LLMs: GPT-4o in LLM-SRBench and DiscoveryWorld, GPT-4 in DiscoveryBench, LLM judges in MOOSE-Chem. Agreement figures are the authors' own. The 94.6% (123 of 130) has no kappa, and the share of "equivalent" cases is not given, so it could be near chance if one class dominates [d10].
- DiscoveryWorld human knowledge was graded by hand (0 / 0.5 / 1) and agent knowledge by GPT-4o. The gap is not like for like [d11].
- DiscoveryBench has one run per cell and no confidence intervals [d07]. DiscoveryWorld has five seeds per cell and one model [d12].
- DiscoveryBench gold hypotheses come from papers likely in training data [b13].
- Some numbers were seen only in garbled tables or snippets: ResearchBench per-model values, DiscoveryWorld figures beyond the headlines, LLM-SRBench Figure 4 magnitude [critique].

### 5.5 Interventions

| Worked | Did not work or unclear |
|---|---|
| Fit-and-feedback loop with real data [K03] | Reasoning scaffold on top of a code agent (DiscoveryBench) [K07] |
| Outside search to flag known ideas (6.14 to 2.38) [c14] | Same-model judge of ideas (50.0%) [b19] |
| Staged retrieve-compose-rank (4.020 vs 2.882) [c10] | Code tool for strong models in interactive probing [c05] |
| Oracle feedback with up to 3 trials [d07] (needs an oracle) | Ring communication between agents (-0.33) [c21] |
| Domain knowledge in archaeology (9.9 to 17.5) [a16] | Heavy agent framework against self-debug, 17x cost [c18] |
| Independent trajectories, 10 vs 1 (+0.70) [c21] (contested) | More idea generation: 4000 seeds gave about 200 non-duplicates [b19] |

## 6. Language models

### 6.1 How they behave on these tasks

**Rediscovery of textbook laws is mostly recall.** LLM-SR hits low error on Feynman problems within a few iterations, sometimes one pass, and perplexity on Feynman equations is far lower than on new problems [b07]. Rewriting the same laws (LSR-Transform) cuts the best symbolic accuracy to 31.5% [b08].

**Recall gets stronger with each model generation.** On the same 111 items the no-data score went from 2.10-7.21% (GPT-3.5, Llama-3.1-8B, GPT-4o-mini) to 28.83-35.14% for five newer models. That is about 5x to 17x [d09]. Any rewriting trick for historical cases will be weaker on current models than on those in the original paper. Counterfactual shifts hold: on NewtonBench no-data is 0 for three models [d09].

**Data feedback is the main lever.** Same model, GPT-4o-mini: 7.21% blind against 31.53% with the LLM-SR loop. Llama-3.1-8B: 3.61 against 30.63 [d08]. The step from 7 to 31 is more than the gap between model generations on any single mode.

**Strong models explore too little once they have a code tool.** In NewtonBench a code interpreter lifted GPT-4.1 from 5.8 to 18.9 and cut GPT-5 from 75.9 to 73.3 and Gemini-2.5-flash from 50.6 to 40.9. The authors read it as an early shift from exploring to exploiting, based on keyword rates in two models with visible traces [c05]. Not an intervention test.

**Noise breaks form recovery before fit.** Noise 0.0001 cut GPT-5-mini symbolic accuracy 12-16% while fit error stayed stable [c06].

**End to end, agents are far below humans.** DiscoveryWorld: 11 scientists completed 66% (knowledge 55%). Best GPT-4o agent: 38% easy, 18% challenge; knowledge 34% easy, 8% challenge [c07]. DiscoveryBench: best non-oracle 16.3 [d07]. ScienceAgentBench: 32.4% (42.2% with o1-preview at over 10x cost) [b22].

**Scaffolds on top of code did not help in DiscoveryBench.** ReAct and DataVoyager were within about 2 points of CodeGen, and DataVoyager GPT-4o was far below on synthetic tasks (5.7 vs 14.1) [d07]. Model strength interacts: Llama-3 gained +1.4 from ReAct, GPT-4o lost 0.1.

**Retrieval of the key idea is good; composing and ranking are weaker.** MOOSE-Chem GPT-4o keeps 83.7% of true inspirations in the top 4% [c09]. ResearchBench final round is 45.65% for GPT-4o [c11]. Pairwise ranking has position bias [c12].

**Novelty is cheap, feasibility is not.** AI ideas were rated 5.64 against 4.84 for human experts on novelty, with no gain on feasibility [b18]. Generation collapsed to about 200 non-duplicates out of 4000 [b19].

**Interpretation is the weak step.** Kosmos synthesis statements 57.9% accurate against 85.5 and 82.1. The authors read this as confusing statistically significant with scientifically valuable [d13].

**Judges.** GPT-4o equation judge: 94.6% raw agreement on 130 items [d10]. GPT-4o idea ranking: 50.0% balanced accuracy [b19].

### 6.2 What changed performance, by how much

| Change | Effect | Source |
|---|---|---|
| Add data-fit feedback loop | 7.21 to 31.53 (GPT-4o-mini, symbolic) | [d08] |
| Remove iterative refinement from LLM-SR | NMSE up to 1.01e-1 in-domain, 1.81e-1 OOD | [a22] |
| Newer model, no data | 2-7% to 29-35% symbolic | [d09] |
| Code tool, weak model | 5.8 to 18.9 (GPT-4.1) | [c05] |
| Code tool, strong model | 75.9 to 73.3 (GPT-5); 50.6 to 40.9 (Gemini-2.5-flash) | [c05] |
| Oracle feedback, up to 3 trials | 15.5 to 24.5 (GPT-4o, DB-REAL) | [d07] |
| Domain knowledge | 9.9 to 17.5 (archaeology, DataVoyager) | [a16] |
| Staged retrieve-compose-rank | 2.882 to 4.020 top matched score | [c10] |
| Outside search | novelty of known ideas 6.14 to 2.38 | [c14] |
| Ten independent runs vs one | +0.70 held-out Q | [c21] |
| Self-debug vs heavy agent | +10.8% tasks at 17x lower cost | [c18] |
| Noise 0.0001 | -12 to -16% symbolic | [c06] |

### 6.3 Gaps in the LLM evidence

- No study tests an operator sequence mined from a historical case against a plain agent at equal tokens [K27].
- No measured rate of LLMs detecting and acting on an anomaly. One anecdotal NewtonBench trace with "Key Anomaly Identified"; DiscoveryWorld does not measure it [critique].
- Nearly all numbers are equation discovery. Biology and chemistry wet-lab cases appear only through Co-Scientist (n = 1) and Kosmos (self-reported).
- Search quota was exhausted in the last pass, so absence of a replication (for example of cf-PICI) means "not found", not "not there" [d18].

## 7. What our agent should take

Format: item, schema part, status, evidence ids. Status marks: [E] established, [S] single-source, [C] contested. Nothing in "Test first" goes into SCHEMA.md until its test passes (SCHEMA.md section 8).

### Add now (established)

1. **Always run a no-data (blind) baseline beside every rediscovery or case-study item.** Schema: G5 and G7 (the check on our own claims). [E] K01, K20; ids b07, c01, d07, d08, d09. The memory share ranged from 0% to 95% of the score by model, and rose 5x to 17x across generations. Without it a "discovery" may be recall. Cost: one extra call per item.
2. **A real data-fit loop is the core: model proposes a form, code fits and scores it, the residual goes back.** Schema: G2, G3, S4 TEST, S5 REVISE. [E] K03; ids a21, a22, b08, c02, d08. This is already in the schema; the finding adds a size (7.21 to 31.53). No change needed except to cite it.
3. **Score form and extrapolation, not fit alone.** Schema: G3, G5. [E] direction, K04 for the metric flip is [S]; ids b09, c02, c03, c06. Use a held-out extrapolation range as the pass test. Never rank by one metric.
4. **No same-model judge as the only verifier of ideas or conclusions.** Schema: G5, G8. [E] K14; ids b18, b19, b21, c12, c19. GPT-4o idea ranking was 50.0% balanced accuracy; position bias appears in pairwise ranking. Already in G5/G8; this adds more evidence.
5. **Separate "it ran" from "it is explained".** Schema: S7-S8 (verify, interpret). [E] K25 and K12 as a pair; ids d12, d13, a20, c08. Score completion and explanation apart. Add a code-side or checklist step that asks "is this effect large, or only significant" before concluding.
6. **Judge accuracy needs a measured check on our own samples.** Schema: G5. [E] K24; ids d10, d11. Hand-grade a sample of 30 to 50 judge calls and prefer code checks where possible.
7. **Pre-cutoff or counterfactual control on any rediscovery claim we make.** Schema: G5 and logging section 6. [E] for the practice, K26 for the case it fixes; ids d13, d14, b15. Kosmos did this; Co-Scientist did not.
8. **Caution rule for mining operators.** Test each operator by ablation on our own agent, not by its historical credit. Schema: section 8 rule 3. [E] K16; ids a02, b01-b03, d01, d03, d04.

### Test first

Each is a hypothesis from the case studies. None is proved for LLMs.

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | **Expectation bounds before each test, and a surprise trigger that drops other goals.** Code stores an expected range, flags a violation, and puts the puzzle first (KEKADA ES1, PG1, PC8). | S4 TEST, S6 IMPASSE (trigger), G1 | [S] K21, K22 | d01, d02, d03, d04 |
| T2 | **Fixed explanation order after a surprise:** known factor, divide and conquer, scope, other. | S6 operator choice, O3, O1/O2 | [S] K21 | d02, d04 |
| T3 | **Scope rule with a threshold:** if more than 3 members of a class show an effect, generalise; if more than 3 do not, drop the scope idea. | S7 SELECT, O2 | [S] K21 | d04 |
| T4 | **One off-plan probe after N negative sweeps in one line of work** (Krebs's ornithine test; N at 3, 6, 12). | S6 IMPASSE, O6/O8 | [S] K23 | d05, d03 |
| T5 | **Factor analysis (remove one entity at a time) and "relate two anomalies".** | O3, O4 | [S] K21 | d04 |
| T6 | **Written working log plus a topic-keyed view the look-back reads.** | S9, memory | [S] K17 | b05, d05 |
| T7 | **Structured findings store against free-text history in long tasks.** | Memory, S9 | [E] in the systems tested, no equal-token test, so treat as [S] for us K19 | c15, b24, c20 |
| T8 | **Near analogy for debugging, far analogy for new models.** | O7 | [S] K18, secondary source | a11, a12, a13 |
| T9 | **N independent schema runs plus a code-side picker against one long run, at equal tokens.** | O-sample, G11, G4 | [C] K09 | c21, d15, d16, d17 |
| T10 | **Exploration quota before the first fit on strong models.** | S6, S3 | [S] K10 | b12, c05 |
| T11 | **Staged retrieve, compose, rank for open-mode hypotheses.** | O7, S3 open mode | [E] retrieval step, [S] full pipeline K13 | b15, c09, c10, c11 |
| T12 | **Outside search at the verify state to separate known from new.** | G8, S8 | [S] K08 | c14 |
| T13 | **Forced method change after repeated failure (brute force trap).** | S6 | [S] K12 | a20, c08 |
| T14 | **Diversification enforced in code to fight the 4000-to-200 collapse.** | S3 open mode | [S] K15 | b19 |
| T15 | **Noisy-data variant scored on form, not fit.** | G5 | [S] K11 | b12, c06 |

Do not add: reasoning scaffolds on top of a code loop as a default (K07 contested); multi-agent talk (G9 already forbids it, and c21 agrees); KEKADA's rules as a set (K22: sufficiency only).

## 8. Concrete tests on our bench

Rule for all: both arms at equal tokens, setup cost counted (G7). Run each arm over at least 3 seeds. Report the cost-adjusted gain.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Memory share | 20 historical cases (Kepler's third law, Boyle, Snell, Ohm and others) in original form and in an obscured form (variables renamed, law rewritten) | Full schema vs plain model, each on original and obscured; plus a no-data arm | Symbolic accuracy per form; gap = memory share | Gap large for strong models; expect no-data arm 25-35% on rewritten items for recent models [d09] |
| B2 Execute-and-score ablation | LSR-Transform and LSR-Synth items (equation tasks with data) | With fit-and-feedback loop vs without (propose only), equal tokens | Symbolic accuracy and held-out extrapolation error | About 3x to 4x in symbolic accuracy, as in [d08] |
| B3 Surprise trigger | Tasks with a planted anomaly: DiscoveryWorld-style or our own generated tasks where a first experiment contradicts a stated expectation | Expectation bounds + goal-drop vs free-form agent | Rate of detection; rate of acting on it (switch of line within 2 steps); final task success | Higher detection rate; success gain unknown. This also fills gap K27(b) |
| B4 Explanation order | Same anomaly tasks with a known cause class (missing factor, subprocess, class effect) | Fixed order (known factor, divide, scope, other) vs random order vs model-chosen | Steps to the cause; success at equal tokens | Fewer steps than random; vs model-chosen unknown |
| B5 Off-plan probe | Search tasks with many negative sweeps | After N negative sweeps in one line, force one off-plan probe; N = 3, 6, 12; vs none | Success; steps to first success | Gain for N around 6 if any; the Krebs data is one case |
| B6 Sampling vs structure | Equation tasks and DiscoveryBench-style data tasks | 10 independent short schema runs + code picker vs one long run vs full schema; equal tokens, not equal calls | Held-out score | Independent runs ahead of one long run by a modest margin; replicates c21 with a token match |
| B7 Code-tool exploration quota | NewtonBench-style interactive tasks, strong model | Code tool with a forced exploration quota before the first fit vs code tool without vs no code | Symbolic accuracy | Closes the 75.9 to 73.3 style loss; weak models unaffected |
| B8 Log and look-back | Long multi-step discovery tasks | Raw log only vs raw log + topic-keyed view vs no log at S9 | Success; repeated dead ends per run | Fewer repeated dead ends with the keyed view |
| B9 Interpretation check | Tasks with a significant but meaningless result | Add "significant or meaningful" check vs none | Share of conclusions that are wrong or overstated, graded by code plus a hand sample | Fewer overstated conclusions; size unknown |
| B10 Judge audit | 30 to 50 hand-graded judge calls | Same-model judge vs code check vs different-model judge | Agreement with hand grade, with kappa | Same-model judge worse than code check |
| B11 Staged hypotheses | Post-cutoff papers (after the model's cutoff) | Retrieve, compose, rank vs one-shot at equal tokens | Match to the real hypothesis (code or hand), best-of-N | Gain in best-of-many, little in average [c10] |
| B12 Analogy distance | Debug tasks and new-model tasks | Near vs far analogy source, crossed | Success per task type | Near wins debug; far wins new models (low confidence) |

## 9. What does not transfer, and why

- **KEKADA's 64 heuristics as a package.** Hand-written for one lab and one reaction, with domain-specific rules (33 of 64) and user-typed results. The domain-independent 31 are the only candidates. Even those were fit to two cases [d01, d04].
- **The claim "this is how scientists think."** Reproducing a history shows sufficiency only. Notebooks are not protocols; Henseleit did much of the Krebs bench work [b01-b03].
- **Weeks and months as counts.** The Krebs timeline (16 weeks to the first surprise) is about a human with lab constraints and a slow bench. For an LLM the unit is calls, not weeks. Use the shape (long negative stretch, then surprise, then scope), not the numbers [d05].
- **Faraday's physical sheets.** The mechanism (a topic-keyed view of a log) transfers. The 16,041 entries and the paper slips do not [b05].
- **Rediscovery scores as discovery scores.** Memory carries 0% to 95% of a score by model [d07]. Textbook results (AI Feynman 100/100, Eureqa 71%) are clean and recalled [b06].
- **LSR-Transform as a memory barrier.** It worked for 2023-2024 models and not for 2025 models [d09].
- **Equation-discovery gains as proof for all discovery.** The sample is one sub-area. Biology, chemistry wet-lab and theory building are covered by one case (Co-Scientist) and one self-reported system (Kosmos).
- **Oracle feedback.** Reflexion's 24.5 needs an oracle match signal. Not available in real use [d07].
- **Interpersonal and social parts of discovery.** Acceptance, collaboration, funding and the lab's division of labour have no counterpart in a single agent [b01].
- **Code-tool findings across task types.** NewtonBench (interactive probing) and ScienceAgentBench (fixed data) point in different directions [c05, c18].
- **Multi-agent results from Shi et al.** Call-matched, 7B model, five training rows per prompt, symbolic regression only, no seed replication [d15].
- **Simulated worlds.** DiscoveryWorld and NewtonBench are simulated and text-only. No physical experiment cost, no wet-lab delay.

## 10. Open questions

1. What did Kulkarni and Simon's rules do in ablation? No ablation of the surprise rule exists, and no baseline without it [d04].
2. Does an operator sequence mined from a case (surprise check, one-variable change, near analogy, look-back) beat plain sampling at equal tokens on obscured historical cases? No published ablation was found [K27(a)].
3. Can an LLM detect and act on an anomaly, and at what rate? Only one anecdotal trace [K27(b)].
4. How big is the original-versus-transformed gap in LLM-SRBench Figure 4? The plot values were not read [d08].
5. Does sampling many independent runs beat structured scaffolds on discovery at equal tokens? One preprint, call-matched, a 7B model, no seed replication [d15].
6. How often do scientists change method after an impasse, and for how long are they stuck? Krebs gives about 5 shifts in 8.5 months. Faraday and Darwin have no counts. Holmes's book and Gruber's Darwin study were never opened [d05, a28].
7. How much does a rational reconstruction (Hanson on Kepler) differ from the real trace? Argued, never measured [K27(c)].
8. Where do agent failures concentrate: hypothesis, experiment design, interpretation? Two systems point at interpretation, but the evidence is inferred from scores and from collaborator ratings [d12, d13].
9. How good are LLM judges of discovery quality compared with humans? Only a narrow equation check (94.6% raw, no kappa) and no like-for-like DiscoveryWorld knowledge comparison [d10, d11].
10. Does the Co-Scientist cf-PICI rediscovery replicate, and was it in training or public data? n = 1, no leak control [d14].
11. Does the code-tool exploration loss in strong models come from early exploitation? The mechanism is the authors' reading of keyword rates in two models [c05].
12. Is the Faraday 16,041 entry count correct? Single-source [b05].
13. Does the memory effect still allow a fair test on 2026 frontier models? The LSR-Transform no-data score is already 29-35% [d09].

## 11. Sources

[V] = opened this session (full text or raw PDF text as logged in the evidence files). [M] = snippet or description only.

**Founding and historical**
- [M] Nickles (ed.) 1980, *Scientific Discovery: Case Studies*. https://link.springer.com/book/10.1007/978-94-009-8986-3 (SEP page opened [V]: https://plato.stanford.edu/entries/scientific-discovery/)
- [V] Darden 1997, Recent Work in Computational Scientific Discovery, CogSci 19. https://escholarship.org/uc/item/68h6d1p5
- [V] Kulkarni and Simon 1987/1988, The processes of scientific discovery: the strategy of experimentation (tech report AIP-5; Cognitive Science 12(2), DOI 10.1207/s15516709cog1202_1). https://archive.org/details/DTIC_ADA203323 (the DOI in a05 and c24, cog1202_4, belongs to a different paper)
- [V] Kulkarni and Simon 1990, Experimentation in Machine Discovery, NASA tech report FIA-90-09-24-02. https://archive.org/details/NASA_NTRS_Archive_19920016497
- [M] Langley, Simon, Bradshaw and Zytkow 1987, *Scientific Discovery: Computational Explorations of the Creative Process*. https://mitpress.mit.edu/9780262620529/
- [V] Downes 1990, Herbert Simon's Computational Models of Scientific Discovery, PSA 1990. https://collections.lib.utah.edu/dl_files/a7/64/a76445bb3217efefe965f8bb7463f162fef24d11.pdf
- [V] Wikipedia, Hans Adolf Krebs. https://en.wikipedia.org/wiki/Hans_Adolf_Krebs
- [V] Grasshoff and May, Krebs-Henseleit notebooks, MPIWG project page. https://www.mpiwg-berlin.mpg.de/project/urea-cycle
- [M] Holmes 1980/1991 on Krebs; Gruber 1974 *Darwin on Man* (not opened, from background knowledge).
- [V] Wikipedia, Astronomia nova (Kepler's statements). https://en.wikipedia.org/wiki/Astronomia_nova
- [V, via SEP] Hanson 1958; Lugg 1985; Dunbar 1997, 2001 and Dunbar, Fugelsang and Stein 2007; Nersessian 1992-2009; Thagard and Holyoak 1996. https://plato.stanford.edu/entries/scientific-discovery/
- [V] Tweney et al. 2003, Representational, Textual, and Experimental Practices: The Case of Michael Faraday. https://escholarship.org/uc/item/5x77s2m2
- [V] Tweney and Ayala 2003, Artifacts of Memory: Michael Faraday and the Construction of Meaning. https://escholarship.org/uc/item/24d1h1dn
- [M] Schmidt and Lipson 2009, Distilling free-form natural laws from experimental data. https://doi.org/10.1126/science.1165893

**Equation discovery**
- [V] Udrescu and Tegmark 2020, AI Feynman. https://arxiv.org/abs/1905.11481
- [V] Shojaee et al. 2024/2025, LLM-SR. https://arxiv.org/abs/2404.18400
- [V] Shojaee et al. 2025, LLM-SRBench. https://arxiv.org/abs/2504.10415
- [V] Zheng et al. 2026, NewtonBench. https://arxiv.org/abs/2510.07172
- [V] Li et al. 2025 / Ma et al. 2025, AI-Newton. https://arxiv.org/abs/2504.01538

**Discovery agents and benchmarks**
- [V] Majumder et al. 2024, DiscoveryBench. https://arxiv.org/abs/2407.01725
- [V] Jansen et al. 2024, DiscoveryWorld. https://arxiv.org/abs/2406.06769
- [V] Chen et al. 2025, ScienceAgentBench. https://arxiv.org/abs/2410.05080
- [V] Huang et al. 2024, MLAgentBench. https://arxiv.org/abs/2310.03302
- [V] Lu et al. 2024, The AI Scientist. https://arxiv.org/abs/2408.06292
- [V] Gottweis et al. 2025, Towards an AI co-scientist. https://arxiv.org/abs/2502.18864
- [V] Mitchener et al. 2025, Kosmos. https://arxiv.org/abs/2511.02824

**Hypothesis and idea generation**
- [V] Yang et al. 2025, MOOSE-Chem. https://arxiv.org/abs/2410.07076
- [V] Liu et al. 2026, ResearchBench. https://arxiv.org/abs/2503.21248
- [V] Si, Yang and Hashimoto 2024, Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Zhou et al. 2024, HypoGeniC. https://arxiv.org/abs/2404.04326

**Sampling versus teams (context)**
- [V] Shi et al. 2026, The Weight of Teamwork. https://arxiv.org/abs/2610.24131
- [V, abstract only] Tran and Kiela 2026, Single-Agent LLMs Outperform Multi-Agent Systems Under Equal Thinking Token Budgets. https://arxiv.org/abs/2604.02460
- [V, abstract only] Kim et al. 2025/2026, Towards a Science of Scaling Agent Systems. https://arxiv.org/abs/2512.08296

**Internal**
- SCHEMA.md (C:/Users/User/Desktop/AGI/research_notes/single_agent/SCHEMA.md); claims.jsonl, critique.md, evidence_a-d.jsonl in this folder.
