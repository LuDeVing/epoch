# Design-space exploration: deep document

*Subfield E07.08. Key works named in the brief: Papalambros; Deb. Schema link: S7 SELECT. Evidence: evidence_a-d.jsonl (ids a01-a26, b01-b27, c01-c26, d01-d21), claims.jsonl (K01-K25), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

*Honest scope note. The human-side classics (Papalambros and Wilde, Deb's 2001 book, the Marler-Arora survey, Wolpert-Macready, Ishibuchi on many-objective) were not opened. Only Deb et al. 2002 (NSGA-II) was read as full text. Nothing about human designers is cited from memory. Almost all the LLM evidence is machine-side: numeric design vectors or code, not an LLM choosing among its own text candidates.*

## 1. What it is

Design-space exploration (DSE) is the search for good designs when there is no single best one. A design has several goals that pull against each other (speed, area, power, cost, weight). A design is **Pareto-optimal** if no other design is at least as good on every goal and better on one. The set of such designs is the **Pareto front**. The job of DSE is to find a spread of points near that front using few expensive evaluations, then let a decision-maker pick one.

Three sub-problems matter.

1. **Search.** Which designs to evaluate next. Methods: genetic algorithms (NSGA-II), decomposition (MOEA/D), Bayesian optimisation (qEHVI), ant colony, simulated annealing, MAP-Elites.
2. **Quality measurement.** How good is a set of trade-off points. Hypervolume (HV), IGD, ADRS, all computed by code.
3. **Selection.** Which points survive, and which one to pick. Rules: feasibility first, then non-domination rank, then spread.

Why it matters for our agent. Schema state S7 SELECT picks one candidate from several. That is a trade-off step: candidates differ on correctness, simplicity, symmetry, robustness. DSE is the mature field that says how to rank candidates on several criteria without a single weight, and it now has a body of work on LLMs inside the search loop. The field supplies rules for code (dominance, constraint-first ordering, crowding) and warnings about where an LLM fails (size, near-ties, bias, weak baselines).

## 2. History and theories in depth

**Foundations (before our evidence).** Pareto dominance is the basic order. A decision-maker problem sits on top: no single optimum exists, the best choice depends on preference, so an optimiser should deliver a finite representative subset of the front (a07, Guerreiro and Fonseca 2020). The pick-one step lies outside the optimiser. Marler and Arora (2004) classify methods by when the decision-maker states preferences (a25; bibliographic record only, not read). Papalambros and Wilde (Principles of Optimal Design) and Deb's 2001 book are named key works but were not opened (a26).

**NSGA-II (Deb, Pratap, Agarwal, Meyarivan 2002; a01-a05, d18; opened).** The founding computational model. It fixed three faults of the first NSGA: slow sorting, no elitism, and a sharing parameter. Fast non-dominated sort costs O(MN^2) against O(MN^3) before. Parents and children are merged, ranked into fronts, and ties inside a front are broken by crowding distance (a cheap spread estimate, exact only for two objectives). Constraint handling by dominance: a feasible design always beats an infeasible one, and among infeasible designs the smaller violation wins. No penalty weights are needed (a05).

**Quality indicators.** Hypervolume is the most used set-quality indicator and is strictly monotone with respect to set dominance (a06). It depends on a reference point, so it bakes in preference. Cost: 2D in O(n log n), 3D in O(n log n), exact contribution is #P-hard, and subset selection is NP-hard for three or more objectives.

**Bayesian multi-objective search (2020-21).** qEHVI gives exact joint expected hypervolume improvement for a batch with autodiff gradients (a08). qNEHVI extends it to noisy observations (a09). Both are authors' own benchmarks.

**Quality-diversity.** MAP-Elites keeps the best solution in each cell of a user-chosen feature space. It maps how performance varies across the space instead of returning one winner (a10, Mouret and Clune 2015).

**No free lunch.** Averaged over all problems no search beats another, so an edge comes from fit to a problem class (b27; not opened). This is the frame for the 2023-26 mixed results below.

**LLMs enter (2023 on).** Four lines.
- *LLM as optimiser from a scored history* (OPRO; a11, a12, b01-b04). Works on small TSP and on prompt optimisation, degrades with size.
- *LLM as evolutionary operator* (LMEA, MOEA/D-LLM, MOEA/D-LO; a13-a15). The LLM writes crossover or mutation children inside a classic loop.
- *LLM evolves heuristics, not points* (EoH, FunSearch, MEoH; a16, a17, d05, d06, d07).
- *LLM-guided hardware DSE with domain rules* (iDSE, Lumina, MicroEvo, MPM-LLM4DSE, Intelligent4DSE, driving agents; a18-a23, b18-b20, c03-c09, c21).

**The 2026 correction.** Independent groups with strong, tuned baselines report that the LLM edge shrinks or vanishes: tuned CMA-ES, TPE and SMAC beat frontier LLM agents on HPO (d01), a plain (1+1) loop is competitive with FunSearch, EoH and ReEvo (d05), simple BestOfN matches some agents in CO-Bench (d07), and the OPRO size cliff persists in DeepSeek V3.2 and GPT-5.1 (d09).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| NSGA-II beats PAES and SPEA on convergence except ZDT3, ZDT6; best diversity on all 9 | 25,000 evaluations, pop 100, 10 runs, 9 synthetic problems; NSGA-II params untuned; paper itself inconsistent about SPEA on ZDT6 | a01-a05, d18 (Deb 2002) | [E] for that paper; single-source |
| Hard multimodal case defeats all: ZDT4 | 7.94e11 local fronts; NSGA-II and PAES stuck at pop 100; 500 generations helped POL, KUR, ZDT3, ZDT4, ZDT6 | a04 | [E] |
| Constrained dominance needs no penalty weight | feasible beats infeasible; smaller violation wins; tested on a 5-objective, 7-constraint problem | a05 | [S] |
| Hypervolume cost | 2D and 3D O(n log n); contribution #P-hard; subset selection NP-hard for d>=3 | a06 (Guerreiro, Fonseca 2020) | [S] |
| OPRO TSP gap grows with size | gap % (text-bison / gpt-3.5 / gpt-4), n=10 0/0/0; n=15 4.4/1.2/0.2; n=20 30.4/4.4/1.4; n=50 219.8/133.0/11.0; farthest insertion 9.8 at n=50; 5 instances per n | a12, b01, c11 (Yang 2023) | [E] (replicated d10) |
| Model strength dominates | steps to optimum at n=10: 40.4 / 46.8 / 9.6; n=15 successes 0/5, 4/5, 4/5 | b02 | [E] |
| Independent replication of size trend | GPT-4 gap 0.00 (n=10), 0.28 (15), 0.88 (20), 3.38 (25), 11.01 (30); GPT-3.5 0, 6.01, 30.69, 31.20 | d10 (Huang 2024) | [E] |
| Size cliff persists in 2025-26 models | text-only reasoning degrades with size in DeepSeek V3.2 and GPT-5.1; switches to nearest-neighbour and cheapest-insertion; exact n not in text | d09 (OPT-Engine) | [E] qualitative |
| LLM genetic operators beat LLM-proposes-new | gap LMEA vs OPRO: rue-15 0.06 vs 5.23; rue-20 3.94 vs 26.30; rue-25 18.72 vs 53.59; clu-20 4.05 vs 19.83; clu-25 10.06 vs 48.25 | a13, b05, b06 (Liu 2024) | [S] |
| ...but still lose to cheap heuristics at 25 nodes | rue-25 LMEA 18.72 vs farthest insertion 2.33, nearest neighbour 10.71, best heuristic 1.41 | b05, c12; critique item 2 | [S] |
| Temperature on stall helps | LMEA rue-20 3.94 +/- 1.54 vs 11.82 +/- 2.21 without; OPRO temperature 1.0 best of {0, 0.5, 1, 1.5, 2} | b07, b03 | [E] (two papers, different tasks) |
| LLM operator matches GA operator on synthetic RE21-RE25 | HV GA vs LLM: 0.781/0.7936; 0.7221/0.6853; 1.1491/1.1561; 1.1574/1.153; 1.0812/1.0812. 2 LLM, 2 GA, 1 tie. Row order is an inference | a14, c01 | [S] |
| Distilled linear operator robust, rarely best | LO vs NSGA-II: LO better on 11, worse on 2, 1 tie (14 HV problems); vs MOEA/D better on 9, worse on 3; vs MOEA/D-DE worse on 7, better on 5; UF1 HV DE 0.720, LO 0.656, NSGA-II 0.609; ZDT4 DE collapses to 0.301 vs LO 0.721 | a15, b08, b09, c02; critique item 4 | [E] on "no method wins everywhere" |
| iDSE hardware DSE | ADRS gain 16.6x vs NSGA-II, 12.7x ACO, 9.9x MOEA/D, 15.3x Lattice, 5.1x HGBO-DSE (a learning-based method); under 50 designs; matches NSGA-II (about 108 designs) at 4.6%; 12 benchmarks, 5 runs | a18, c05, a19 | [C] |
| iDSE ablation | baseline 12.4% invalid; pruning removes 89.9% of invalid; reflection +20.5%; domain knowledge +45.0% | a19, c06, d20 | [S] |
| iDSE warm start | ADRS ratio to random start, geo mean: NSGA-II LLM seeds 3.17x (about 2.3x over LHS); MOEA/D 3.41x; autocorr NSGA-II ADRS 0.7458 (warm) vs 0.0883 (random), much worse | d20, c06, a20 | [E] on average; exception noted |
| Lumina GPU DSE | 4.7M-point space; 6 designs beat A100 in 20 steps; 32.9% higher PHV; 17.5x sample efficiency; 421 superior designs vs ACO 24 in 1,000 samples; BO 4th; GA and grid failed | b18, c04, c25, d19 | [C] |
| Rules lift LLM trade-off accuracy | Qwen3: bottleneck 0.73 to 0.80; perf/area 0.59 to 0.82; tuning 0.40 to 0.63. Phi-4 tuning 0.30 to 0.48. Llama-3.1 tuning 0.26 to 0.46. Benchmark 308 / 127 / 30 questions | b19, c03, d19 | [S]; rules written after seeing the test errors |
| MicroEvo microarchitecture | budget 20 HV 0.5826 (NSGA-II) vs 0.7936 (+36.22%); budget 45 0.663 vs 0.821 (+23.94%); ADRS 0.1666 vs 0.0716; 5 trials; gain shrinks with budget | a23 | [C] |
| Driving multi-agent | 15 iterations: 6 Pareto points vs 0 for GA; GA first at iteration 20; 280-point space | a22, c09 | [S] |
| MPM-LLM4DSE and Intelligent4DSE | 32.66% ADRS reduction vs GNN-DSE, equal time; 87.47% over metaheuristics; LLM variants cost 2-6x wall-clock (347-839 s vs 132-213 s) | c07, c08, c21 | [C] |
| EoH idea+code evolution | 0.962 to 0.993 in 20 generations; about 2,000 queries vs about 1M for FunSearch; capacity 500: FunSearch 6.75%, best fit 4.50%, first fit 4.97%, EoH 2.13% | a17, b13, b14 | [S] |
| MEoH two-objective heuristic search | bin packing: FunSearch 3.319% gap 195.7 s; EoH 0.391% 502.9 s; MEoH 0.080% 59.1 s; 100k C100 MEoH 1.387% vs EoH 0.753% | a16 | [S] |
| LLM-evolved MOBO | normalised HV 0.971 vs qParEGO 0.869, NSGA-II 0.691, random 0.600; Friedman chi2 49.91, ranks 1.83 vs 2.58; about 60x lower wall-clock; real problems 0.985 vs 0.971; test called underpowered | b21, b22 | [S] |
| POET: LLM mutation + non-dominated sort + verifier | functional correctness 40/40 vs 29/40 (I/O prompting), 33/40 (CoT), 36/40; raw DeepSeek-R1 errors in over 25% of attempts | b24 | [S] |
| LLM material ratings too generous, too flat | 136 experts, 10,544 scores; MAE about 3 of 10 for all prompt types; SD experts 3.346 vs GPT-4 2.486; Mixtral gave titanium 9 regardless of scenario | c13 | [S] |
| LLEMA chemistry | hit rate plain LLM 4.4, with memory 15.1, islands 29.8, LLEMA 30.2; memorisation 95.3% to 16.6%; 1.5x tokens per iteration | c14, c15 | [S] |
| Independent HPO test, tuned baselines | val_bpb: Centaur 0.9763, TPE 0.9768, SMAC 0.9778, CMA-ES 0.9785, best LLM agent (code) 0.9814; default 0.991; 3 seeds, one task, 24 h | d01 | [S] |
| Hybrid ratio matters | Centaur 0.8B r=0.1 0.9744, r=0.3 0.9766, r=0.8 0.9849; 27B r=0.5 0.9746, r=0.8 0.9902 | d02 | [S] |
| Earlier positive result at 10 evaluations | GPT-4 Turbo beats random search in 81.25% of 32 tasks; median +13.70% | d04 | [S]; not vs tuned baselines |
| Plain (1+1) loop is competitive | 4 problems, 5 runs, 10,000 evaluations; loses only on online bin packing (Weibull) | d05 | [E] with d06, d07 |
| Seeding a (1+1) loop with known algorithms | best average rank in 5 of 6 settings; +23% and +22% mean normalised AUC on bbob (GPT, Qwen) | d06 | [S] |
| CO-Bench | classical solver 0.797; best one-shot Claude-3.7 Sonnet 0.65; o3-mini 0.615; DeepSeek-R1 0.525; FunSearch 0.842; agents beat the solver within about 10 steps; saturate near 50 | d07 | [S] |
| HeuriGym | best models QYI about 0.6 vs expert 1.0 | d08 | [S] |
| EngDesign | o3 34.38%; o3-high 33.57%; GPT-4o and Gemini-2.0-Flash about 15%; analog IC 0% for all | d17 | [S] |
| One-pass choice is weaker than staged choice with code aggregation | DeLLMa 73.3% vs 33.3% (o1-preview) on agriculture; 64.2% vs 35.0% stocks; gain grows with action count; cost $0.09-0.37 vs $0.21 | d12 | [S] |
| Judge position bias strongest at small quality gaps | 15 judges, 22 tasks, over 150,000 instances | d13 | [E] with d14, d15 |
| Judge preferences non-transitive | share rises about 2.6% to about 40% as items get closer (bins read from a chart); round-robin plus Bradley-Terry: Spearman 95.0-96.4% | d14 | [S] |
| Judge panels are not independent | 9 judges, 7 families: MNLI 72.0% vs best judge 71.8% | d15 | [S] |
| LLAMBO warm start less diverse | lower generalised variance than random; helps early only; uncertainty calibration worse than GP | b10, b11, c10, d21 | [S] |
| Strong BO baselines get mis-tuned | Matern kernel with length-scale init 1.0 worked to d=600; SE failed from d=400 | b12 | [S] |
| Set-based LLM template | 100 to 64 to 50 designs by utility and CVaR; no baseline | d16 | [S] |

## 4. Mechanisms and models

Each is written so an engineer can code it.

**4.1 Dominance and the selection order (NSGA-II).** For candidates with criteria vectors:
1. If one is feasible and the other is not, feasible wins. If both are infeasible, the smaller total constraint violation wins.
2. Else if one dominates the other (at least as good on all criteria, strictly better on one), it wins.
3. Else put it in a non-dominated front by repeated peeling (front 1 = nobody dominates it; remove; repeat).
4. Inside a front, rank by crowding distance: for each criterion sort the points, give boundary points infinite distance, add the normalised gap between each point's two neighbours. Larger is preferred (keeps spread).
Fill the survivor list front by front, cut the last front by crowding. No weights. Valid as written for 2 or 3 criteria. Beyond about four criteria dominance rarely separates points (b26, not opened), so aggregate or cap the active criteria.

**4.2 Hypervolume as one-number quality.** Pick a reference point worse than every candidate. HV is the volume dominated by the set. Larger is better. In 2 criteria sort by one criterion and sum rectangles. Use it to compare two search methods, not to pick one design. The reference point encodes preference (a06, a07).

**4.3 ADRS.** Average distance of each reference-front point to the nearest point found. Lower is better. Used for HLS (a18, a23, c07, c08). Needs a reference front, which in iDSE was built by sampling and was exhaustive for only three small benchmarks (c05).

**4.4 OPRO loop.** Keep a code-held list of (candidate, score) pairs, top K (default 20) sorted ascending. Prompt: task, the list, ask for new candidates. Sample 8 per step, default temperature 1.0, up to 200 steps (a11, b03, c23). Code scores every candidate. Failure: context grows with problem size, stalls on bumpy landscapes (b04), overfits train vs test by 5-20% in prompt optimisation (c23).

**4.5 LMEA loop.** Population N=16, G=250. The LLM picks parents and writes children by crossover and mutation. Code scores. Self-adaptation: when the best score has not improved for some rounds, raise the sampling temperature (b07). Cost: a small run took about half a day (c12).

**4.6 MOEA/D-LLM.** Decompose the problem into 50 weighted subproblems. For each, give the LLM 10 parent designs, ask for 2 children, zero-shot (a14). Distilling: regress child on parents from 14,000 prompt-response pairs to get a weighted linear operator plus noise, no LLM calls at run time (a15, b08).

**4.7 iDSE recipe (hardware).** (1) Prune the space by feature rules, removing about 89.9% of invalid designs. (2) The LLM writes a warm-start batch of seeds (12 initial samples, population 12, 3 generations). (3) Reflect on the trajectory and the bottleneck, refine. (4) Inject domain knowledge (how each pragma affects speed and area). Ablation gains: pruning, then reflection +20.5%, then domain knowledge +45.0% (a19, c06). All baselines got the same pruned space (d20), so pruning is not the lead.

**4.8 Lumina recipe.** An LLM with sensitivity-based bottleneck rules. Write failure patterns as rules after observing errors: change one thing at a time, state the baseline, adjust only the least critical resource when relieving the dominant stall, account for negative side effects (b19, b20, c22).

**4.9 MicroEvo.** LLM inside Monte Carlo tree search with a Pareto-aware tree policy and a memory of insights (a23).

**4.10 EoH.** Each individual is a short natural-language thought plus code. Operators: new thought, mutate thought, recombine thoughts, then the LLM writes code from the thought. Population keeps the best by score (a17).

**4.11 Hybrid with code-held state (Centaur).** CMA-ES keeps mean, step size and covariance in code. A minority of trials (10-50%) come from an LLM that sees this state. The majority come from CMA-ES. A ratio of 0.8 degrades (d02).

**4.12 DeLLMa.** (1) List the unknown states of the world. (2) Forecast their probabilities. (3) Elicit a utility function by pairwise ranking of outcomes, in small batches. (4) Compute expected utility per action in code. (5) Pick the maximum. Tuning: per-action sample size 64, overlap 25% (d12).

**4.13 Round-robin plus Bradley-Terry.** To rank many near-equal candidates with an LLM judge: compare every pair (or a sampled design, SWIM), both orders, fit Bradley-Terry in code. Removes most non-transitivity (d14). Shuffle order and aggregate across passes (d13).

**4.14 Staged narrowing (set-based design).** Compute utility and risk (CVaR) in tools. Prune 100 to 64 to 50 by code filters. A human picks last (d16). There is no ablation, so it is a template, not a result.

**4.15 MAP-Elites.** Grid over 2-3 descriptor features. Draw a random elite, mutate, put the child in its cell if empty or better. Returns a map of the trade-off space (a10).

## 5. What holds up

**Replications and agreement across independent groups.**
- The OPRO size trend replicates. Huang et al. 2024 (independent of the OPRO and LMEA authors) found GPT-4 gap 0.00 at n=10, 3.38 at n=25, 11.01 at n=30 (d10). OPT-Engine 2026 finds a size cliff for DeepSeek V3.2 and GPT-5.1 and gives no precise n (d09). [E]
- Weak baselines inflate LLM gains. Xu et al. 2025 show plain BO fails in high dimensions mostly through kernel and initialisation choices (b12). Ferreira et al. 2026 (AutoML group) show tuned TPE, SMAC and CMA-ES beat the best pure LLM agent (d01). Zhang et al. 2024 show a plain (1+1) loop is competitive with FunSearch, EoH, ReEvo (d05). Sun et al. 2025 show BestOfN beats some complex agents (d07). [E]
- No search method wins everywhere. MOEA/D-DE wins hard UF problems and collapses on ZDT4; the linear operator is robust (b09). FunSearch wins some bin-packing sets and loses others (b13). EPS wins on three of four problems (d05). This is consistent with no free lunch.
- Position bias, non-transitivity and correlated panels are replicated across three independent groups (d13, d14, d15). [E]

**Failures and nulls.**
- LLM operator equals GA on RE21-RE25 (2 wins, 2 losses, 1 tie; c01).
- LLM-evolved MOBO sits in the same Friedman top group as qParEGO (b21).
- LLEMA: some end-to-end baselines still beat it on single tasks (c14).
- Warm start much worse on autocorr (0.7458 vs 0.0883; d20).
- LLMize authors conclude it is not competitive with classical solvers on simple problems (d11; four-page demo, weak).
- MEoH loses to EoH on one set (a16). MicroEvo's gain falls from 36.22% to 23.94% as budget grows (a23).
- Cost: LLM variants take 2-6x wall-clock (c08); LLM inference is far above classical BO (b10).

**Moderators.**
- *Budget.* The LLM edge is at tiny budgets (10-50 evaluations) against random or default-setting baselines (d04, a18, b18, a23). At a 24-hour budget with tuned baselines it reverses (d01).
- *Domain text.* Wins sit in rule-rich hardware spaces with a knowledge-heavy prompt (K08). Parity on cheap synthetic benchmarks without domain text (c01).
- *Model strength and size.* gpt-4 vs weaker models (b02); LLEMA hit rate climbs 7B to 14B to 32B (c15, non-monotone on SAW/BAW).
- *Problem size.* The cliff (K01, K20).
- *Prior in the prompt.* Example code and strategy text in the prompt influence output most (d06).
- *LLM share of the work.* In Centaur, too many LLM trials hurt (d02).

**Interventions that worked.**
- Code-held score table plus LLM proposals (OPRO, LMEA, Centaur).
- Raise temperature when stuck (b07).
- Domain rules for failure patterns (b19; +0.12 to +0.23 absolute on trade-off accuracy, d19), with the caveat that rules were written after seeing test errors.
- One-change-at-a-time and state-the-baseline rules (b20).
- Verifier plus non-dominated sorting (POET 40/40; b24).
- Staged elicitation with code aggregation (d12).
- Round-robin plus Bradley-Terry for judges (d14).
- Memory of successes and failures (LLEMA hit rate 4.4 to 15.1; c14).
- Seeding a simple loop with known good algorithms (d06).

**Interventions that did not work or are untested.**
- Letting the LLM rate options by opinion (too generous, too flat; c13).
- Fine-tuning for DSE judged too costly (c21).
- A panel of judges as a way to remove error (d15).
- Too many LLM trials in a hybrid (d02).
- Diversity as a predictor of quality (not supported in HPO; d03). Whether lost warm-start diversity hurts Pareto spread is untested (K10).

## 6. Language models

**On small search problems with a scored history (OPRO).** GPT-4 reaches the TSP optimum at n=10 in 9.6 steps; weaker models need 40-47. At n=50 the gap is 11.0% for gpt-4 and 133-220% for gpt-3.5 and text-bison, against 9.8% for farthest insertion (a12, b02). The best single LLM never beat the cheap heuristic at the largest size.

**As an evolutionary operator.** LMEA improves on OPRO at every size (rue-20 3.94 vs 26.30) yet loses to classic insertion at 25 nodes (b05). In MOEA/D the zero-shot GPT-3.5 operator ties a GA (a14, c01).

**On hardware spaces.** With domain rules and low budgets, LLM-guided search beats the authors' baselines by factors of 5 to 17 on ADRS (a18), or +36% HV at budget 20 (a23), or 6 vs 0 Pareto points in 15 iterations (a22). Backends: DeepSeek-R1 (iDSE), Gemini and DeepSeek (MicroEvo), Qwen3-235B and GPT-4o (MPM-LLM4DSE). Cost is 2-6x wall-clock (c08). No independent replication. Baselines are author-run, run counts 3-5, default settings (c20).

**Against tuned classical baselines.** On HPO with Claude Opus 4.6 and Gemini 3.1 Pro, the best pure LLM agent scored 0.9814 against CMA-ES 0.9785 and TPE 0.9768. A hybrid with CMA-ES state shared with a small LLM was best (0.9763; 0.8B at r=0.1 gave 0.9744). A 0.8B model at r=0.8 gave 0.9849 (d01, d02). Single task, 3 seeds.

**On problem size with 2025-26 models.** Text-only reasoning degrades with size. Models fall back to nearest-neighbour and cheapest-insertion and use fewer tokens near the cliff. Delegating to solver code keeps accuracy (d09). One-shot Claude-3.7 Sonnet scored 0.65 vs classical solver 0.797 on CO-Bench; agent search (FunSearch on o3-mini) 0.842 (d07). HeuriGym best about 0.6 of expert (d08). EngDesign best 34.38% (d17).

**On judging trade-offs.** Unaided accuracy on parameter tuning was 0.26-0.40 for three open LLMs; rules raised it to 0.46-0.63 (d19). Recurring errors: many simultaneous changes, wrong baseline for deltas, ignoring negative side effects (b20, c22). In material selection, MAE about 3 of 10 against 136 experts, LLM spread narrower than experts', one model gave the same top answer regardless of scenario (c13). Prompt style changed agreement little (c13).

**On choosing among options.** One-pass choice gets worse as the action count grows. A staged procedure with code aggregation reached 73.3% against 33.3% for o1-preview (d12). Judge reliability collapses where selection is hardest, near ties (d13, d14), and a panel of nine frontier judges holds about two independent votes (d15).

**Other LLM behaviours seen.**
- Generated code may quietly fix its random seed (b23).
- LLM warm-start points are less diverse than random (b11, d21).
- LLM warm start is worse on at least one benchmark (d20).
- LLM output follows exemplar algorithms in the prompt (d06).
- Memorisation is large for a plain LLM in materials (95.3%), falling to 16.6% with the full scaffold (c14).
- Training accuracy exceeds test accuracy by 5-20% in prompt optimisation (c23).

**What changed by how much (summary).** Model strength: about 4x fewer steps (b02). Domain rules: +0.12 to +0.23 accuracy (d19), +45.0% effectiveness (a19). Memory: hit rate 4.4 to 15.1 (c14). Structure around the LLM (islands, rules, memory): 4.4 to 30.2 (c14). Staged choice with code aggregation: +40 points (d12). Temperature self-adaptation: gap cut by about two thirds (b07). Tuned baseline instead of default: the LLM edge disappears in HPO (d01).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status as in SCHEMA.md.

### Add now (established)

1. **Selection order in code: feasibility first, then dominance rank, then spread.** Part S7 / G5. [E] as a method on the paper's tests; transfer to text candidates is untested, so use it only for criteria code can compute (passes check, passes held-out part, size, symmetry). Evidence a01, a05, d18, K25.
2. **Compute scores and aggregation in code; the LLM does not rate by opinion.** S7 / G5. [E]. Evidence c13, c26, d12, d13, d14, d15 (K12). Every successful paper computes the trade-off measure by code.
3. **Shuffle option order and aggregate across passes when an LLM comparison is unavoidable; use pairwise comparisons in both orders with a code-fitted ranking.** S7 / G5. [E]. Evidence d13, d14, d15 (K23).
4. **Do not count a model panel as independent votes.** G4. [E]. Evidence d15; matches the existing guardrail.
5. **Always run a cheap non-LLM or best-of-N control arm at equal tokens, tuned equally.** G7. [E]. Evidence d01, d05, d07, b12 (K16, K21).
6. **Raise sampling temperature or force a new framing only when a stall is detected, never on a schedule.** G1 / S3. [E] as a dial (K04: b07, b03). The evidence is on TSP and prompt optimisation, not text answers, so the exact trigger needs the B11 test.
7. **Hold the score table in code; show the LLM at most a short sorted list.** S3 / G5. [E] as common practice across OPRO, LMEA, Centaur (a11, a13, d02).
8. **Know the size cliff: offload enumeration and scoring to code when options exceed what the model handles in text.** S7 / S4. [E]. Evidence a12, d10, d09, d07 (K01, K20). Locate the cliff for the current backbone first.
9. **Keep a small portfolio of selection rules rather than one.** S7. [E] that no single method wins (K06; b09, b13, d05).

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Staged pairwise scoring with code aggregation vs one-pass "pick the best" | S7 | [S] | d12 (K22) |
| T2 | Recombine two candidates then select (LMEA) vs propose-from-history (OPRO), at equal tokens | S3/S7 | [S] | a13, b06 (K03); no reasoning-model test |
| T3 | Hybrid: code-held scores with a minority (10-50%) of LLM proposals vs LLM-only loop | S3/S7 | [S] | d01, d02 (K19) |
| T4 | Short list of domain failure rules in the prompt, with a no-LLM rules-only control | memory / S7 | [C] for hardware; rules help LLM accuracy 0.12-0.23 | b19, d19, a19 (K08) |
| T5 | One change per candidate, state the baseline | S7 / G | [S] | b20, c22 (K09) |
| T6 | Diverse-first generation vs LLM best-guess seeding; track diversity and final spread | S3 | [C] | d20, b11, d21 (K10) |
| T7 | Criteria-count limit: 2 vs 4 vs 8 criteria with and without a code Pareto filter | S7 | [S] | a06, b26, K13; no test exists |
| T8 | Candidate carries a one-line rationale plus answer, compared with answer-only | S3 | [S] | a17, b13 (K11) |
| T9 | Staged narrowing by code filters vs one-shot choice | S7 | [S] | d16 (K24) |
| T10 | Memory of successes and failures added to the generator | memory | [S] | c14 |
| T11 | Held-out set for selection scores (selection fitted on train overfits) | G3 | [S] | c23 (K17) |
| T12 | Minimal tool menu vs full | S7 | [S] | c16 (abstract only; K18) |

Thresholds are in UNKNOWNS.md.

## 8. Concrete tests on our bench

The bench has code-checkable items (ARC-style, brainteaser with checks) and open items (NoveltyBench-style). All arms use the same token budget. Report tokens per state. Use 3 or more runs and a paired comparison.

| # | Item type | Arm A | Arm B | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 | ARC-style tasks, pool of 3, 6 and 10 candidate programs with a code scorer on held-out inputs | one-pass LLM "pick the best" | pairwise scoring in both orders, code-aggregated (Bradley-Terry) | accuracy of the pick vs best available; self-agreement across order shuffles | B beats A by a growing margin with option count (d12 suggests +20 to +40 points at the large end) |
| B2 | Same pool | LLM picks | code rule: feasibility, dominance on (held-out pass, symmetry, size), crowding | pick vs best available | code at least equal to LLM at lower token cost |
| B3 | Same pool, criteria count 2, 4, 8 | code Pareto filter then LLM tie-break | LLM sees all criteria raw | pick quality by criteria count | filter helps more as criteria rise; locates the limit |
| B4 | Brainteasers with a check | OPRO-style: scored history, propose new | LMEA-style: pick two, recombine, then code selects | pass rate at equal tokens | B beats A (K03); effect smaller with reasoning models |
| B5 | ARC-style | LLM-only loop with scored table | Centaur-style: code mutates known good programs, LLM proposes 10-50% | pass rate at equal evaluations | hybrid at least equal; LLM share above 0.8 degrades (d02) |
| B6 | Items with a known failure pattern list | S7 with no domain text | S7 with 5-10 hand-written failure rules; plus a rules-only code-filter arm | accuracy of trade-off judgments; final pass rate | rules raise judgment accuracy 0.1-0.2; rules-only arm decides whether the LLM adds anything |
| B7 | Items where options differ in several ways | candidates changed freely | one-change-per-candidate and state-the-baseline | error rate of delta judgments on a labelled set | fewer wrong-baseline errors (b20) |
| B8 | Open items (NoveltyBench) | best-guess seeds first | diverse-first seeds, tracked diversity | distinct-answer count; quality of the best | diverse-first at least equal; checks the K10 caveat |
| B9 | All | selection fitted on all given examples | selection on train, scored on held-out | train minus test gap | shows overfit size (c23: 5-20%) |
| B10 | Option count 10, 20, 50 with a code scorer | LLM picks in text | LLM with a code enumerator and scorer | gap to best by option count | cliff for the current backbone; code offload flat (d09) |
| B11 | Stall detector | fixed temperature | temperature up after k non-improving rounds | pass rate at equal tokens | gain (b07: gap cut by two thirds on TSP) may be smaller on text |
| B12 | All | plain best-of-N with code scorer | scaffold with S7 structure | pass rate at equal tokens | scaffold wins only if it beats this control (d05, d07) |

## 9. What does not transfer, and why

- **Numeric design vectors.** Nearly every DSE result is on points in a numeric or pragma space with a simulator. Our candidates are text answers with a check. The search methods (NSGA-II crowding, hypervolume) assume a distance in objective space. Only the selection ordering carries over.
- **Hardware domain-rule gains (iDSE, Lumina, MicroEvo).** The lead depends on injected domain knowledge, expensive evaluations and tiny budgets (K07, K08). Our evaluations are cheap. Cheap evaluations favour best-of-N and classical search, where tuned baselines win (d01).
- **Large option counts.** DSE spaces hold millions of points. S7 handles 3-10 candidates. The size cliff matters at the large end only; at n=10 every tested LLM matched the optimum on TSP (a12).
- **Many criteria.** Dominance loses power beyond about four objectives (b26, not opened). S7 should stay at 2-4 criteria.
- **Genetic operators on text.** LMEA's crossover works on tours. Recombining two reasoning chains is not shown to work; G9 warns that agent debate adds no value.
- **Training-based gains.** e-SimFT needs fine-tuning (c19, out of scope).
- **Human evidence.** No human DSE study was read (gap 8). Papalambros-style practice is not backed here.
- **Wall-clock and cost claims.** The papers use queries, seconds or designs. None compares at equal tokens (critique).
- **Obsolete models.** OPRO, LMEA, LLAMBO, MOEA/D-LLM and EoH used GPT-3.5, text-bison, gpt-4 (2023). The direction is probably still right (d09), but the sizes are not.
- **Judge studies are on other tasks.** Position bias, non-transitivity and panel correlation were measured on chat quality and NLI (d13-d15), not on multi-criterion design choice. Treat the mechanism as likely and the sizes as unknown.

## 10. Open questions

1. Does an LLM choosing among its own text candidates by trade-off beat random or single-score selection at equal tokens? No paper tests this (gap 1).
2. Do the hardware low-budget gains survive tuned independent baselines (gap 2)? Partly closed for HPO, not for iDSE, Lumina or MicroEvo.
3. How much of the gain is the rules and how much the LLM? No rules-only no-LLM control exists (gap 3).
4. What do 2025-26 reasoning models do on an OPRO-style n=20-50 TSP table? Only qualitative evidence (gap 4).
5. At equal tokens, does recombine-then-select still beat propose-from-history with reasoning models (gap 5)?
6. Where is the criteria-count limit (2 vs 4 vs 8), and does a code Pareto filter help (gap 6)?
7. What does Deb's 2001 book say on convergence, diversity and the many-objective limit? Not opened (gap 7).
8. What do human designers do that beats algorithmic search (set-based design, Papalambros-style trade-off practice)? Publisher pages returned 403 (gap 8).
9. Does lost warm-start diversity hurt final Pareto spread (gap 9)?
10. Publication bias: nulls exist (d01, d05, d07, d11, c01) but the hardware papers are all wins (gap 10).
11. Gideoni et al. 2025 (random baselines competitive with code evolution) is cited in d06 but not opened.
12. Is HV or any indicator a good proxy for quality of a text-candidate pool? Untested.

## 11. Sources

[V] = opened and read this session; [M] = snippet or bibliographic record only.

- [V] Deb, Pratap, Agarwal, Meyarivan (2002) A fast and elitist multiobjective genetic algorithm: NSGA-II. https://www.cse.unr.edu/~sushil/class/gas/papers/nsga2.pdf (a01-a05; re-read as d18 via a sci2s.ugr.es mirror; DOI https://doi.org/10.1109/4235.996017 is [M], b25)
- [V] Guerreiro, Fonseca (2020) The Hypervolume Indicator: Problems and Algorithms. https://arxiv.org/abs/2005.00515 (a06, a07)
- [V] Daulton, Balandat, Bakshy (2020) Differentiable Expected Hypervolume Improvement. https://arxiv.org/abs/2006.05078 (a08)
- [V] Daulton, Balandat, Bakshy (2021) Parallel Bayesian Optimization of Multiple Noisy Objectives (qNEHVI). https://arxiv.org/abs/2105.08195 (a09)
- [V] Mouret, Clune (2015) Illuminating search spaces by mapping elites. https://arxiv.org/abs/1504.04909 (a10)
- [V] Yang et al. (2023) Large Language Models as Optimizers (OPRO). https://arxiv.org/abs/2309.03409 (a11, a12, b01-b04, c11, c23)
- [V] Liu et al. (2024) Large Language Models as Evolutionary Optimizers (LMEA). https://arxiv.org/abs/2310.19046 (a13, b05-b07, c12)
- [V] Liu et al. (2024) Large Language Model for Multi-objective Evolutionary Optimization (MOEA/D-LLM, MOEA/D-LO). https://arxiv.org/abs/2310.12541 and https://arxiv.org/html/2310.12541v3 (a14, a15, b08, b09, c01, c02)
- [V] Yao et al. (2025) Multi-objective Evolution of Heuristic Using LLM (MEoH). https://arxiv.org/abs/2409.16867 (a16)
- [V] Liu et al. (2024) Evolution of Heuristics (EoH). https://arxiv.org/abs/2401.02051 (a17, b13-b15; c18 abstract only, [M])
- [V] Li, Xiong, Wang (2025) iDSE. https://arxiv.org/abs/2505.22086 and https://arxiv.org/html/2505.22086v1 (a18-a20, c05, c06, c20, d20)
- [V] Sharma, Fu, Haris, Cano (2026) LLM-Driven DSE of FPGA-based Accelerators. https://arxiv.org/abs/2605.05920 (a21)
- [V] Shih et al. (2025) Multi-Agent LLM Framework for DSE in Autonomous Driving Systems. https://arxiv.org/abs/2512.08476 and https://arxiv.org/html/2512.08476v1 (a22, c09)
- [V] Xiong et al. (2026) MicroEvo. https://arxiv.org/abs/2608.06183 (a23)
- [V] Wong et al. (2025) LLM2TEA. https://arxiv.org/abs/2406.14917 (a24)
- [M] Marler, Arora (2004) Survey of multi-objective optimization methods for engineering. https://doi.org/10.1007/s00158-003-0368-6 (a25)
- [M] Papalambros, Wilde, Principles of Optimal Design; Deb (2001) Multi-objective optimization using evolutionary algorithms (a26; no URL)
- [V] Liu et al. (2024) LLAMBO. https://arxiv.org/abs/2402.03921 and https://arxiv.org/html/2402.03921v2 (b10, b11, c10, c24, d21)
- [V] Xu et al. (2025) Standard Gaussian Process is All You Need for High-Dimensional BO. https://arxiv.org/abs/2402.02746 (b12)
- [V] Fu et al. (2023) GPT4AIGChip. https://arxiv.org/abs/2309.10730 (b16, b17)
- [V] Zhang et al. (2026) LUMINA. https://arxiv.org/abs/2603.05904 and https://arxiv.org/html/2603.05904v2 (b18-b20, c03, c04, c22, c25, d19)
- [V] LLM-Driven Evolutionary Generation of Multi-Objective BO Algorithms (2026). https://arxiv.org/abs/2607.08791 (b21-b23)
- [V] Ping et al. (2026) POET. https://arxiv.org/abs/2603.19333 (b24)
- [M] Ishibuchi, Tsukamoto, Nojima (2008) Evolutionary many-objective optimization: a short review. https://doi.org/10.1109/CEC.2008.4631121 (b26)
- [M] Wolpert, Macready (1997) No free lunch theorems for optimization. https://doi.org/10.1109/4235.585893 (b27)
- [V] Evaluating LLMs for material selection (2024). https://arxiv.org/html/2405.03695v1 (c13)
- [V] Xu et al. (2026) MPM-LLM4DSE. https://arxiv.org/pdf/2601.04801 (c07)
- [V] Xu et al. (2025) Intelligent4DSE. https://arxiv.org/pdf/2504.19649 (c08, c21)
- [V] Abhyankar et al. (2026) LLEMA. https://arxiv.org/pdf/2510.22503 (c14, c15)
- [M] AutoCircuit (2026, ICML), abstract only. https://icml.cc/virtual/2026/74815 (c16)
- [M] Multidisciplinary design and optimization agent driven by LLMs (2025), abstract only. https://arxiv.org/abs/2511.17511 (c17)
- [V] e-SimFT (2025) Alignment with simulation feedback for Pareto-front design. https://arxiv.org/html/2502.02628v1 (c19)
- [V] Ferreira, Wobbe, Krishnakumar, Hutter, Zela (2026) Can LLMs Beat Classical Hyperparameter Optimization. https://arxiv.org/abs/2603.24647 (d01-d03)
- [V] Zhang, Desai, Bae, Lorraine, Ba (2024) Using LLMs for Hyperparameter Optimization. https://arxiv.org/abs/2312.04528 (d04)
- [V] Zhang et al. (2024) Understanding the Importance of Evolutionary Search in Automated Heuristic Design with LLMs. https://arxiv.org/abs/2407.10873 (d05)
- [V] Huang, Ye, Shahane, Back, van Stein (2026) From Heuristic Selection to Automated Algorithm Design. https://arxiv.org/abs/2603.02792 (d06; cites Gideoni et al. 2025, [M])
- [V] Sun, Feng, Li, Yang (2025) CO-Bench. https://arxiv.org/abs/2504.04310 (d07)
- [V] Chen et al. (2026) HeuriGym. https://arxiv.org/abs/2506.07972 (d08; abstract and intro)
- [V] Chen, Cheng, Sun, Ling, Ge (2026) OPT-Engine. https://arxiv.org/abs/2601.19924 (d09)
- [V] Huang et al. (2024) Exploring the True Potential: Evaluating the Black-box Optimization Capability of LLMs. https://arxiv.org/abs/2404.06290 (d10)
- [V] LLMize (2026). https://arxiv.org/abs/2601.00874 (d11; weak)
- [V] Liu, Fu, Yogatama, Neiswanger (2024) DeLLMa. https://arxiv.org/abs/2402.02392 (d12)
- [V] Shi et al. (2025) Judging the Judges: position bias. https://arxiv.org/abs/2406.07791 (d13)
- [V] Xu et al. (2025) Investigating Non-Transitivity in LLM-as-a-Judge. https://arxiv.org/abs/2502.14074 (d14)
- [V] Kohli (2026) Nine Judges, Two Effective Votes. https://arxiv.org/abs/2605.29800 (d15)
- [V] Kumar, Karniadakis (2026) Agentic Risk-Aware Set-Based Engineering Design. https://arxiv.org/abs/2604.16687 (d16)
- [V] Guo et al. (2025) Toward Engineering AGI (EngDesign). https://arxiv.org/abs/2509.16204 (d17)
