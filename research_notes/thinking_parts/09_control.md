# 09. Control and planning: when to stop, where to spend, how to re-plan

*2026-10-13. Part 9: rounds, stage budgets, stop rules, reallocation, re-planning (nano/loop.py `_rounds`, `_stage`, control.json). Grades: A peer-reviewed or theorem; B accepted venue or preprint with ablations; C abstract-only, blog, single run; D my arithmetic or inference. "(abs)" = only the abstract was read. WebSearch quota ran out twice, so most sources are direct fetches.*

## 1. Findings

1. The loop has a schedule, not a plan. In our one complete two-round dry run (mock backend, so token counts are length estimates; B = 1.5M) ideation took 40% of tokens, interrogation 46%, judging 6%, building 6%. Round 1 used 81.5% of B; round 2 spent 18% more and built nothing (6 interrogation chains and all 5 build specs skipped for budget) [33].
2. Reasoning models do not ration a shared budget by value or difficulty. Allocation belongs to a script, with the model as adviser [3][5][9].
3. Patience rules are blind: "no new best in m builds" fires with probability (n-m)/n in an exchangeable search (50% at n=12, m=6) [D]. Use expected gain against cost [24]. Diminishing returns are loop-specific (97% of one autoresearch run's gain came in its first 25 of 100 experiments; another system reports linear gains to 20 cycles), so calibrate on our own logs [16][20].
4. The best-supported control move in research agents is to switch from exploiting to broader search when progress flattens, on thin evidence [15].
5. Strong human researchers decide in advance what would make them stop, order work by information per unit time, and ring-fence about 10% for exploration [31]. Sunk cost keeps failing lines alive [32].

## 2. What the loop does today

- `_rounds` is a fixed `for rnd in range(...)`, default 2. Round 2 gets `max(2, k_impl//3)` build slots. `n_ctx` is passed to `ideate_round` and never used, so "half the contexts in round 2" is dead code.
- One token pool B. Four checks (`spent + est > B`: sketch, interrogation, pre-mortem, build) skip the call, logged only in `decisions`; the loop ends if `spent >= B` after a round. No stage shares, no build floor, no GPU or wall-clock budget. Ideation specs are part-major, so a budget stop starves the last parts.
- control.json is read at five boundaries per round (ideated, clustered, deepened, built, verified): pause, stop_after_stage (any truthy value), skip_nodes, exclude_clusters, note. No budget, round, slot or lane keys; the loop never writes it.
- Yield signals exist but steer nothing: the discovery curve (new_per_context, top2_share, card yield) only retires cards, and novelty.py's promised "fewer contexts on low yield" is not implemented. Prediction misses trigger nothing. `--replan` runs unconditionally when flagged.
- Already have: staged seeds, futility stop, anytime-valid e-process and `--hours` in batch_verify; in harness/think.py Thompson card allocation, a stagnation reset and the value stop `all(p_s * V_tokens < est_cost(s))`, none wired into nano [33].

## 3. Evidence

**3.1 Metareasoning and allocation of computation**
- Choose computations by expected value; Bayesian selection heuristics beat bandit heuristics on one-shot decisions and in Go [1] B (abs).
- LLM uses: a value-of-computation reward cuts tokens 20-37% at equal performance [2] B (abs). A contextual-bandit meta-controller (continue, backtrack, switch, restart) gives +9-12% accuracy and -28-35% time at the same budget [4] B (abs). Difficulty-adaptive allocation gives over 4x best-of-N efficiency; predicting reward distributions saves up to 50% compute at equal quality [6] B (abs). Budget-conditioned search (broad early, refine late) beats budget-agnostic MCTS at equal budgets [7] B (abs).
- NEG: under a shared budget reasoning models act as greedy sequential solvers: effort-value correlation 0.00-0.11, coverage 80% to 40% as questions go 5 to 20, 16-19 point losses when order is reversed; planning prompts spread effort but are not value-aware [3] C (full). More tool calls alone do not help without budget awareness [5] B (abs). Longer reasoning can lower accuracy [8] C (abs). Early orchestrators spawned 50 subagents for trivial queries; tokens explain 80% of BrowseComp variance [9] C.

**3.2 Planning and re-planning**
- Planner/executor with dynamic re-planning: 57.6% on WebArena-Lite [10] B (abs). Decompose only when the executor fails: up to +28% ALFWorld, +27% WebShop, +33% TextCraft [10] B (abs). NEG: o1 is a "quantum improvement" on PlanBench yet far from saturating it [11] B (abs).
- AI Scientist v2 fixes its plan: four stages with stop rules (prototype runs; curves converge on 2+ datasets; budget exhausted, twice), 21/12/12/12 nodes, debug depth 3, 1 h per node, no ablation of tree versus linear search [12] B. The co-scientist supervisor re-weights agents from run statistics but publishes no rule or convergence criterion; its Elo is not independently grounded [13] B. NEG: neither allocation is validated.
- Operators beat policy. With AIDE operators MCTS and evolution add nothing; the best pairing lifts medals 39.6% to 47.7%; policy rankings change with horizon (differ at 3 h, equal at 10 h, diverge after about 15 h); choosing the final node by validation score recovers 9-13 points [14] B. A greedy hill-climber nearly matches the best tree search on 18 tasks. An agent that starts greedy and, once the slope flattens (W=50 steps, epsilon=0.0005), forks the top-N and runs branches round-robin ranks first (0.208 vs 0.193; 3 rounds, no CIs). Early convergence and directional focus predict score; diversity and compute cost do not [15] C (full).
- Loops drift toward local refinement of their metric; an immutable prediction/outcome card kept them honest, and a taste oracle changed direction, not score [18] C (abs). Karpathy's loop has no stop rule: "LOOP FOREVER", "if you run out of ideas, think harder" [19] C. An outer loop tuning only parameters gained nothing reliable; injecting mechanisms gave -0.045 vs -0.009 val_bpb [18] C (abs).

**3.3 Stopping and diminishing returns**
- Baseline autoresearch: 15.24 of 15.69 mbpb (97%) in experiments 1-25, 0.45 in 26-50, nothing after (n=1 per method) [16] C. A no-lineage specialist loop ran 125 trials without a valid improvement; its supervisor stops on a 48 h deadline and a 4 h no-keep grace period [17] C. Counter-evidence: findings linear in cycles to 20 (self-reported) [20] C; greedy AIRA gains 6 more points beyond 24 h [14] B.
- Ideas saturate: 4,000 ideas per topic held about 200 non-duplicates, and each new batch's non-duplicate share keeps falling [23] B.
- Formal rules: Pandora/UCB stopping matches best-of-N with 15-35% fewer generations [24] B (abs); window-based early stopping cuts 34-84% of samples at comparable accuracy [25] B (abs); stop Bayesian optimisation when optimisation error falls below statistical error [25] B (abs). The secretary rule assumes no recall and rank-only payoffs [26] A (secondary), and people stop too soon [26] C; our setting has recall and costly inspection, which is Pandora.
- Good-Turing: the chance the next draw is new is about N1/N [26] A (secondary). D arithmetic: P(new best in next k | n built) = k/(n+k); round 2's 3 builds on top of 10 give a 23% chance and about 0.13 sigma if exchangeable (best of 12 unit-normal gains is 1.63 sigma). Resampling observed gains cannot predict a new best; use a parametric predictive.

**3.4 Budget across stages**
- Successive halving and Hyperband run over 10x faster than BO baselines [27] A (abs), valid only when early rank predicts final rank (Spearman 0.8 as working bar, brief 11). Allocation pays most at short budgets: 10 minutes of Auto-sklearn 2.0 beat an hour of 1.0 [27] B (abs). NEG: random search with early stopping matched ENAS [27] B (abs).
- Coverage rises log-linearly with samples over four orders of magnitude (15.9% to 56% on SWE-bench Lite at 250 samples) but becomes accuracy only with a verifier; without one, voting plateaus after several hundred [28] B (abs). LLM verification needed up to 8x compute to match plain voting [28] B (abs). Our verifier is execution on one serial GPU, so the scarce stage is evaluation.
- Refine a diversity-aware subset, not every candidate (MMR-k best yield per cost) [29] C (abs). NEG: LLM pre-execution preference is only 61.5% accurate [29] C (abs).
- Practitioners spend most time on exploration, one goal per round [30] C. Humans beat agents on returns to time (agents 4x at 2 h, humans 2x at 32 h) [21] B (abs). FunSearch wipes the worst half of islands every 4 h [22] A.

**3.5 Human project control**
- Steinhardt: order work by failure rate per unit time, lambda = ln(1/p)/t (claimed 2-3x); give up only with "a solid argument" the approach is doomed [31] C. Hamming: about 10% of time on big questions; "important" means a reasonable attack exists [31] C.
- Escalation of commitment (meta-analysis, read through a secondary summary): sunk costs, time invested, personal responsibility and closeness to completion raise it; opportunity-cost information and anticipated regret lower it [32] B. NEG: no source I could open gives a validated abandon rule for research lines; all are heuristics.

## 4. Improvement ideas for this part

Principle: every rule below runs first in shadow mode (logs `would_*` to control_log.jsonl, acts on nothing), is calibrated by replay on logged runs, then enabled. Thresholds are placeholders (D).

**C1. Stage envelopes with a protected build floor. Partial.** Mechanism: plan.json holds shares of B (initial guess: research and plan 5%, ideation 20%, judging 5%, interrogation 20%, build/revise/compose 40%, reserve 10%). `_afford(stage, est)` replaces the four checks and requires `spent + est + build_floor_left <= B`; unused shares roll forward; a round starts only if its builds are affordable; ideation specs interleave across parts; prompts carry a one-line budget tracker [5]. Effect: no idea-only rounds (the dry run wasted 18% of B). Cost: small. Measure: share per stage; `budget_skip` by stage (build must be 0); share of sketches whose cluster is never built.

**C2. Ideation in waves with a front-end stop. Partial.** Mechanism: waves of 6 contexts interleaved across parts; after each wave compute the lexical new-rate (novelty.Index cosine under 0.45, ledger included) and Good-Turing N1/N; stop when the new-rate stays under a floor for two waves after every part has had one. Evidence [23][24][25]. Effect: 10-30% fewer ideation calls at equal distinct clusters (D). Cost: small to medium. Measure: replay ideas.jsonl: distinct and eventually-selected clusters against contexts used.

**C3. Value-of-computation gate and adaptive rounds. New.** Mechanism: `rounds_max` 4; after `verified`, expected gain of the next k builds from a Student-t predictive of rung-3 z (n at least 8, else shadow only) against cost in one currency (tokens + lambda x GPU-minutes; until the ledger holds about 30 overnight pairs, a relative rule: continue only if gain per cost is at least 0.25 x round 1's). Log `stopped_by`. Evidence [1][24][15][16]. Effect: ends poor runs early, extends rich ones. Cost: small. Measure: cost-to-best curve; 1 vs 2 vs 3 rounds at equal B.

**C4. Stagnation- and surprise-triggered re-framing. Partial** (levers exist, trigger is new). Mechanism: act when two hold: new-rate low, top2_share above 0.4, checked-rate low, prediction hit-rate low, repeated same-reason rung-3 failures. One action per round: `replan` from the ledger and falsified assumptions, lens switch, exclusion list, cross-family share 0.25, or fork from top-N archive parents; never "think harder". Evidence [15][18][16]. Effect: fewer repeats of one idea family. Cost: small (wire existing flags). Measure: yield per spend after the trigger against a replicate with it off.

**C5. Plan the funnel backward from the night. New.** Mechanism: night capacity (hours over about 31 min per seed, staged seeds) fixes rung-4 and rung-3 slots; build slots follow from logged pass rates (priors until data); `k_impl` becomes derived; GPU minutes get their own budget beside tokens. Evidence [27][28], brief 11 M1 and M4. Effect: pools sized to what the night can verify. Cost: medium. Measure: pool size against capacity, idle GPU, GPU-minutes per stackable or verified.

**C6. Control file v2 and decision log. Partial.** Add keys `budget_add`, `stage_shares`, `rounds_max`, `k_impl`, `longshot_share`, `focus` ({part: hunch}), `shadow`, `stop_after` (a stage name), `proceed` (overrides a pause). The loop writes control_log.jsonl and, at a gate that wants the owner, control_proposals.json plus a pause. Evidence [19][18][32]. Effect: cheap owner steering, auditable controllers. Cost: small. Measure: interventions per run, gates auto-resolved, regret of overridden proposals.

**C7. Value-scaled interrogation. Partial, as an arm.** Depth 0 for clusters outside the diverse top set (MMR-k), depth 2 for the top; generation 1 runs only if generation 0's offshoots reach the build shortlist, otherwise its share (about a fifth of B in the dry run) goes to builds. Evidence [29][28]. Effect: shifts spend from text to execution. Cost: small. Measure at matched B: checked and stackable per token, offshoot-selected rate.

**C8. Part-level reweighting with floors. Later; log propensities now.** After round 1, round-2 contexts per part = 1 + delta from a Beta posterior of checked-rate with a ledger prior, floor of one per part and direction, long-shot lane untouched. Evidence weak and mixed [15][29][13]; with 1-2 builds per part it only learns across runs (about 100 builds). Effect: attention follows measured yield without starving parts. Cost: small. Measure: per-part yield against allocation.

**C9. Pre-registered kill and pause criteria. New.** Before the run, plan.json lists script-evaluated rules: 0 of the first 8 builds with positive z pauses for the owner; a part failing 3 consecutive stage-1 overnight verdicts is frozen for the next night; no keep in 4 h of the night ends it. The script, not the builder, owns continue decisions. Evidence [31][32][17]. Effect: fewer sunk-cost continuations. Cost: small. Measure: triggers fired, owner overrides, whether frozen lines later produced wins.

Order: C1 and C6 first, then C2-C4 in shadow, then C5, C7 as an arm, C8-C9 once the ledger exists. Only runs can settle three questions: whether round 2 pays, whether interrogation generation 1 beats more builds, and the exchange rate lambda.

## Sources

[1] Hay, Russell, Tolpin, Shimony 2012. https://arxiv.org/abs/1207.5879
[2] De Sabbata, Sumers, Griffiths 2024. https://arxiv.org/abs/2410.05563
[3] Fan et al. 2026, Thinking Hard, Not Smart. https://arxiv.org/abs/2608.07968
[4] Meta-Reasoner (ACL 2026). https://arxiv.org/abs/2502.19918
[5] BATS (COLM 2026). https://arxiv.org/abs/2511.17006
[6] Snell et al. 2024. https://arxiv.org/abs/2408.03314 ; Damani et al. 2024. https://arxiv.org/abs/2410.04707
[7] BG-MCTS (ICML 2026). https://arxiv.org/abs/2602.09574
[8] Gema et al. 2025. https://arxiv.org/abs/2507.14417
[9] Anthropic multi-agent research system. https://www.anthropic.com/engineering/multi-agent-research-system
[10] Plan-and-Act. https://arxiv.org/abs/2503.09572 ; ADaPT. https://arxiv.org/abs/2311.05772
[11] Valmeekam et al. 2024. https://arxiv.org/abs/2409.13373
[12] AI Scientist v2 (3.2.1, Table 3). https://arxiv.org/abs/2504.08066
[13] AI co-scientist (3.2-3.3, 4.2). https://arxiv.org/abs/2502.18864
[14] AIRA-dojo (section 5, App. C). https://arxiv.org/abs/2507.02554
[15] FML-bench controlled study (Table 3, App. D). https://arxiv.org/abs/2605.17373
[16] GEAR. https://arxiv.org/abs/2605.13874
[17] Specialist Agents auto research. https://arxiv.org/abs/2605.05724
[18] Doesn't Drift. https://arxiv.org/abs/2608.07542 ; Bilevel Autoresearch. https://arxiv.org/abs/2603.23420
[19] Karpathy autoresearch program.md. https://raw.githubusercontent.com/karpathy/autoresearch/master/program.md
[20] Kosmos. https://arxiv.org/abs/2511.02824
[21] RE-Bench. https://arxiv.org/abs/2411.15114
[22] FunSearch. https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/
[23] Si et al. 2024 (3.2, 7.1). https://arxiv.org/abs/2409.04109
[24] Optimal Stopping vs Best-of-N. https://arxiv.org/abs/2510.01394
[25] ESC. https://arxiv.org/abs/2401.10480 ; Makarova et al. https://arxiv.org/abs/2104.08166
[26] Secretary problem. https://en.wikipedia.org/wiki/Secretary_problem ; Good-Turing. https://en.wikipedia.org/wiki/Good%E2%80%93Turing_frequency_estimation (secondary)
[27] Hyperband. https://arxiv.org/abs/1603.06560 ; Auto-sklearn 2.0. https://arxiv.org/abs/2007.04074 ; Li and Talwalkar. https://arxiv.org/abs/1902.07638
[28] Large Language Monkeys. https://arxiv.org/abs/2407.21787 ; Singhi et al. https://arxiv.org/abs/2504.01005
[29] Budgeted Subset Refinement. https://arxiv.org/abs/2607.14118 ; ForeAgent. https://arxiv.org/abs/2601.05930
[30] Google Tuning Playbook. https://github.com/google-research/tuning_playbook
[31] Steinhardt. https://cs.stanford.edu/~jsteinhardt/ResearchasaStochasticDecisionProcess.html ; Hamming. https://www.cs.virginia.edu/~robins/YouAndYourResearch.html
[32] Escalation of commitment (Staw 1976; Sleesman 2012, via summary). https://en.wikipedia.org/wiki/Escalation_of_commitment
[33] Internal: nano/loop.py, novelty.py, batch_verify.py, harness/think.py, ARCHITECTURE.md 4-5, D:/AGI-lab/runs/mock-dry14, briefs 04, 09, 11.

Unopened: Russell-Wefald 1991, Gershman 2015, Sleesman 2012, Callaway 2022, R&D-Agent scheduler, Franco 2014, Paul 2010, Schulman, Alon. The nine ideas are mine and untested.
