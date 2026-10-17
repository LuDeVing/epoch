# HTSA v0.3 candidate ideas: owner proposals reviewed

Date: 2026-10-10
Scope: the six owner proposals for the next HTSA revision, reviewed against ARCHITECTURE.md v0.2, SYNTHESIS and the mechanism catalog.

## How the review was done

Each idea was reviewed through three independent lenses, written up separately before anything was merged. Lens 1 looked for evidence inside the project: the mechanism catalog rows (GEN, EVL, CTL, SOC, REP, MEM, MSR, STA, OTH), the SYNTHESIS decisions and the open conflicts already logged. Lens 2 looked at prior art outside the project, with web search, and at what the Claude API and Claude Code actually expose today (no logprobs, no activations, summarized thinking only). Lens 3 checked implementability against ARCHITECTURE.md v0.2: which skill, card, script or file would carry the change, what schema fields would move, how it fits the matched-budget rule and the section 8 keep/drop procedure. The three lens reports were then merged into one verdict per idea with a confidence score from 1 to 5. Every verdict below is "adapt": no idea was rejected outright and no idea could be adopted as written, because in each case v0.2 already contains a large part of it and the literal form either cannot be built on the Claude API or loses to best-of-N at matched cost. The adapted form of each idea is scoped to a delta, with a metric, an ablation arm, a cost and a risk list, so that it can be preregistered in harness/plan.md before any run.

## Summary table

| ID | Idea | Verdict | Confidence | Kind | Where it lives |
|----|------|---------|------------|------|----------------|
| I1 | Mid-solutions: prove verified sub-claims (lemmas) and build on them | adapt | 4/5 | structural | New P1 card (lemma pool), harness/lemma_check.py, runs/<id>/lemmas.jsonl, think.py state.lemma_pool |
| I2 | Decompose the problem, solve each part several times, assemble by script | adapt | 4/5 | structural | New P1 card decompose.yaml, schema foreach step, harness/compose_parts.py, runs/<id>/decomp/ |
| I3 | Idea tree or graph to see connections and convergence | adapt | 4/5 | structural | harness/graph.py, runs/<id>/graph.jsonl and clusters.jsonl, calibration feature flag, tournament pair rule |
| I4 | Keep tree nodes in superposition before deciding | adapt | 4/5 | structural | harness/measure/pruning_regret.py, harness/think/frontier.py, flags.frontier and flags.verify_order |
| I5 | Find out what the agent's subconscious is thinking | adapt | 4/5 | structural | run_card.py thinking capture, harness/harvest.py, cands origin field, prior_map.json, template lint |
| I6 | Different-field professional agents fill the gaps | adapt | 4/5 | structural | memory/domain_packs.jsonl, runs/<id>/gaps.json, card gap_pack.yaml, flags.gap_pack, SOC-02 doc fix |

Reading the table: "adapt" means the idea's core is kept, the literal form is changed, and the change is small enough to ship behind a flag and test in a post-gate ablation slot. Confidence 4 means the three lenses agreed on the verdict and on the shape of the delta, with open questions only on effect size.

Naming note: I1 and I2 both arrived with a card called "decompose". In this document the I1 card is called "lemma" (memory/strategies/lemma.yaml) and the I2 card keeps "decompose" (memory/strategies/decompose.yaml), so that the two can coexist and be ablated separately.

---

## I1. Mid-solutions: prove verified sub-claims and build on them

### The idea in the owner's words

When we have ideas for solving the problem we should not only think of possible solutions but also mid-solutions, everything that will take us forward, and try to prove them.

### Verdict: adapt (confidence 4/5)

Half of this idea is already in v0.2. The revise card builds on near-misses: a program that passes 2 of 3 ARC demos gets fixed, specialized or split into a subproblem, and partial scores already count as progress on graded benchmarks. What v0.2 lacks is a mid-solution stored as an object of its own: a claim about the problem, such as "the output is the input's largest object recoloured", that a script proves on its own and that later generators can build on. We add that as one P1 card, used only where a script can prove the claim (ARC and the formalizable subset). The model never proves its own steps. The literature is consistent on this: externally checked subgoals give large gains (Hilbert, Draft-Sketch-Prove, Parsel), while self-judged or PRM-judged steps do not. We start from a prior of no effect, because a LEGO-Prover replication found that lemma-library gains disappear once compute is matched. The adapted form therefore proves mid-solutions by script, filters trivial ones with a permutation null, and routes at most one build call per round so a shared pool cannot anchor every generator.

### What v0.2 already does

Five pieces already exist.

1. The revise card (GEN-14, P0) gives a fresh child one failed parent plus a deterministic feedback record (ARC failing train-pair diffs, MacGyver failed checklist ids), with the operators fix, specialize and recurse. This covers the "stepping stone from a near-miss" half of I1.
2. A script computes a partial score for whole candidates on graded benchmarks (GEN-02: ARC train-pair fraction, MacGyver checklist fraction). It feeds stop.partial_gain/eps and state.stale (CTL-11), the P1 within-run LP multiplier (CTL-08) and the revise tournament on verifier scores (Pr18, SOC-05).
3. EVL-11 scores checklist coverage item by item, and EVL-10 (P1) checks a candidate's premises one by one, though non-executable premises only reach "checked".
4. The P1 compose card (GEN-13) builds a partial configuration slot by slot.
5. EVL-05 (P2) ablates the components of a winning diff, but only at the end of a run.

What is missing: every row in cands/*.jsonl and verify.jsonl is a whole answer. No artifact type holds a sub-result, no verifier proves a sub-claim on its own, and no pool of verified intermediates is routed to later generators. Subgoal decomposition at /encode (the CTL-07 betweenness proposal) was dropped in SYNTHESIS and is left to I2, not to this idea.

### Proposed change

Add a P1 card "lemma" (memory/strategies/lemma.yaml, templates lemma.claims.txt and lemma.build.txt). It runs from round 2 only, like revise, and only on ARC-style items and the pre-tagged formalizable subset. Gate flag: flags.lemmas.

Step 1 (call 1, fresh generator, shell allowed). It receives the goal, the hard constraints and the train demos, and writes up to 5 lemmas. Each lemma is a short executable predicate over (input, output), or a sub-function with unit tests. The runner writes them to runs/<id>/lemmas.jsonl with fields {id, claim, predicate_path, scope (demo ids), status, vtype, discrim, implied_by, source_call, parent_ids}.

Step 2 (harness/lemma_check.py, pure script, 0 LLM tokens). A lemma becomes status "verified" (vtype execution) only if all of the following hold: (a) it holds on every train pair; (b) it fails on at least 30% of permuted mismatched pairs (input_i, output_j), where 30% is a placeholder swept on dev-tune and the value is logged as discrim; (c) it is not implied by an earlier verified lemma on the demo set; (d) it passes the perturbation checks of EVL-18 where they apply. Unverified, LLM-checked or model-asserted lemmas never enter the pool. Lemma checks on non-executable items are excluded at P1.

Step 3 (driver). think.py keeps state.lemma_pool, which holds verified lemmas only. Each round, at most one fresh "build" call receives the goal, the constraints and up to 3 pool lemmas, chosen by script by highest discrim. It gets predicate source only, with no rationale and no parent candidate text, so a shared pool cannot anchor every generator (Pr5, SOC-01, GEN-10). The call writes whole candidates to cands/<call>.jsonl with parent_ids = the lemma ids. Those candidates then go through the normal /verify. When a reset happens, the pool crosses it as predicates only and goes through the /restructure cosine < 0.8 lint. Sub-flag flags.lemma_progress, default off, lets a new verified discriminative lemma count as progress in the stall counter.

Diagnostic, harness-only and never in the loop (Pr14): after the run, record whether each verified lemma also holds on the test pair. This gives the rate of lemmas that fit the demos but not the test.

Not built: LLM or PRM step scoring (ToT style), and lemmas on BRAINTEASER. A trained PRM stays deferred to the open-weight Stages 4-5 with a prior of no effect.

Add a row to the section 8 ablation table: "Lemma pool (I1; MEM-02, REP-07, CTL-07 motivation) | see metric | P1 | post-gate".

### Metric and ablation

Primary metric: solve rate on ARC dev-ablate and on the formalizable subset, at matched cost against the primary null (the stronger of best-of-N+/verify and seeded best-of-N+/verify). Secondary metrics: (1) solves per 1k tokens; (2) the share of verified final answers whose lineage contains a verified lemma; (3) the rate of lemmas that fit the demos but not the test pair (harness-only); (4) the discrim distribution of accepted lemmas.

H0: scaffold+lemma <= scaffold without lemma at matched B, with the removed share reallocated proportionally to the other cards. Run 3 replicates. Keep/drop rule: Beta(1,1) on discordant pairs, P(helps) > 0.95, fixed batch count.

Arms: (a) lemmas passed to the build call without lemma_check, which tests the "prove" part; (b) placebo verified lemmas from a different item with the same family key, which tests real use against generic anchoring; (c) discrim filter off, which tests whether trivial lemmas pass; (d) flags.lemma_progress on vs off; (e) the lemma card vs the extra share given to revise, which tests whether this is more than revise-with-recurse.

Expected null: BRAINTEASER is out of scope for the card. If it is run there, the result should be no change.

### Cost

Build: about 1-2 days for the card YAML and two templates, lemma_check.py (permutation null, implication check, reuse of the perturbation checks) and the pool routing in think.py. Run: about 2.5-3x plain CoT per instance, roughly 6-9x CoT per item over 2-3 rounds at B = 20x CoT. This spend replaces seeded calls under matched cost and is not added on top. Lemma verification costs 0 LLM tokens. The ablation adds 5 arms x 3 replicates on dev-ablate in the post-gate slot.

### Risks

1. Trivial or degenerate lemmas, such as "output size equals input size", pass verification and look like progress. The discrim permutation null and the implication check mitigate this, and lemma_progress stays off by default.
2. Goodhart on partial structure: lemmas that fit the demos can mislead lineages (deceptive objectives, Snell-style over-optimization). Mitigations are the test-pair diagnostic and the existing leave rule.
3. Anchoring and homogenization from a shared pool. The cap of one build call per round and the absence of rationales limit it.
4. No gain at matched cost, as the LEGO-Prover case study found (arXiv 2504.03048), so the preregistered prior is no effect.
5. Narrow scope: it does not apply to BRAINTEASER, and on MacGyver it yields "checked" at best, which EVL-10 already covers.
6. The generator writes its own predicates, which makes them self-written tests. This is acceptable only because a script executes them and the null filters them.
7. Some prior-art figures (DSP, Parsel, Hypothesis Search) were recalled from memory by one reviewer and must be checked before they are cited in plan.md.

### Related catalog ids

GEN-14, GEN-02, GEN-13, GEN-10, GEN-06, CTL-07, CTL-08, CTL-11, CTL-05, SOC-05, SOC-01, EVL-02, EVL-05, EVL-10, EVL-11, EVL-12, EVL-18, REP-03, REP-07, MEM-02, MEM-10, MSR-07

### Prior art

- Draft, Sketch, and Prove (Jiang et al. 2022), https://arxiv.org/abs/2210.12283 : an informal proof becomes a formal sketch of intermediate conjectures, each closed by an external prover.
- Hilbert (2025), https://arxiv.org/abs/2509.22819 : recursive subgoals validated by Lean; miniF2F 99.2%, PutnamBench 70.0% vs 50.4%.
- DeepSeek-Prover-V2 (2025), https://arxiv.org/abs/2504.21801 : subgoal decomposition, each subgoal proven and then composed (training-time).
- Seed-Prover (2025), https://arxiv.org/abs/2507.23726 : proved conjectures go into a lemma pool used for the main proof.
- Parsel (Zelikman et al. 2022), https://arxiv.org/abs/2212.10561 : decomposed functions, each tested by execution.
- Hypothesis Search on ARC (Wang et al. 2023), https://arxiv.org/abs/2309.05660 : hypotheses verified by execution on the demos.
- LEGO-Prover (Wang et al. 2023), https://arxiv.org/abs/2310.00656 , and the replication "LLM Library Learning Fails" (2025), https://arxiv.org/abs/2504.03048 : no lemma reuse, and gains vanish at matched compute.
- Stechly et al. 2024, https://arxiv.org/abs/2402.08115 ; Huang et al. 2023, https://arxiv.org/abs/2310.01798 : self-verification of steps fails without an external verifier.
- Snell et al. 2024, https://arxiv.org/abs/2408.03314 ; Qwen PRM lessons 2025, https://arxiv.org/abs/2501.07301 ; DeepSeek-R1, https://arxiv.org/abs/2501.12948 : PRM step scoring is noisy, gamed, and below best-of-N at high budget.
- Rule et al. 2024, metaprogram learning, https://pmc.ncbi.nlm.nih.gov/articles/PMC11316799/ : revision operators including Recurse (basis of the existing revise card).
- Correa et al. 2023, https://arxiv.org/abs/2211.03890 : humans pick subgoals at bottleneck states (CTL-07 motivation).
- Greenblatt 2024, ARC-AGI with GPT-4o: revising programs after execution on the train pairs (already v0.2's revise card).

Evidence grade. For: strong, replicated gains whenever every subgoal is checked externally (Hilbert, DSP, DeepSeek-Prover-V2, Parsel). Against: strong evidence that self-judged or PRM-judged steps fail (Stechly, Huang, Snell, R1), plus a replication showing lemma-library gains vanish at matched compute.

---

## I2. Decompose the problem, solve each part several times, assemble by script

### The idea in the owner's words

We should first decompose the problem into its possible parts and run the reasoning steps on all of the parts, so we find the best solutions.

### Verdict: adapt (confidence 4/5)

Splitting a problem into parts helps, but only in one form: each part gets several attempts, a script tries combinations of them, and a combination is accepted only if it passes the check on the whole problem. Parsel, FunCoder, Draft-Sketch-Prove and DeepSeek-Prover all work this way. The literal version would run the whole generate, judge and verify loop on every part and then keep the best part of each. That costs about P times as much, so it loses to best-of-N at equal tokens. Picking the best part by judge also brings back self-scoring errors, and parts that pass one by one often fail once combined (the compositionality gap is about 40%). The plan is to add one "decompose" card that the allocator can choose. It switches on mainly after a first round fails (as in ADaPT). It runs on ARC, MacGyver and code diffs, and never on BRAINTEASER riddles. Part tests written by the model may prune combinations but never accept one; acceptance is only by the whole-problem /verify.

### What v0.2 already does

Partly covered.

1. The revise card's "recurse" operator (P0, 1 parent, GEN-14) has a fresh child work one sub-problem of an existing parent after round 1. It repairs; it does not decompose first.
2. The compose card (P1, GEN-13): a script picks subgoal slots from the physical-property table and makes one fresh call per slot. That is per-part generation, but only for MacGyver resources.
3. The transform card shows a multi-call DAG can count as one card (transformer, solver, revise).
4. On the evaluation side, /verify scores the hard-constraint checklist item by item, and a converter maps each candidate to the items it covers.
5. The formal card's ARC program hypotheses already break into functions inside one call.

Missing: a general decompose-first card, generation over K versions of each part, a combination assembler, a whole-problem acceptance rule for combined candidates, and any logging of where composition fails. CTL-07's subgoal or betweenness design was dropped in SYNTHESIS, and v0.2 has no step anywhere that decomposes the problem itself.

### Proposed change

New P1 card memory/strategies/decompose.yaml, behind flag flags.card_decompose (off in the gate configuration). Steps:

1. plan: one fresh call that sees problem.md and the hard-constraint checklist. It writes runs/<id>/decomp/<call>/plan.json = {parts:[{part_id, goal, inputs, outputs, interface, depends_on[], checklist_ids[], part_tests[]}], mode in {independent, sequential}}. Limits: P_max = 4 and depth 1. Nothing recurses into think() for a part.
2. solve_part: K = 2 fresh calls per part. Each call sees only problem.md, its own part spec and, in sequential mode, the outputs of its parents. Output goes to decomp/<call>/parts/<part_id>.jsonl. This needs one schema change: a step field `foreach: <parsed_list>` in strategies/schema.json, so run_card.py can fan out over plan.parts.
3. assemble: new script harness/compose_parts.py does this on ARC and Stage 4 diffs, at zero LLM tokens. MacGyver prose gets one fresh composer call instead. The script lists combinations, prunes them with part_tests and with checklist_ids coverage, and caps them at 16. It writes decomp/<call>/combos.jsonl = {combo_id, part_cand_ids, part_test_pass, status}. Each combination becomes an ordinary row in cands/<call>.jsonl, with parent_ids = its part candidate ids and a new field decomp_id. It then goes through the normal /verify, which runs the whole-problem check: demo_match plus perturbation on ARC, and the full checklist plus the negative-emergent-property check on MacGyver.

Selection rules (integrity, fixed at 100%): part_tests are written by an LLM, so they may prune or order combinations but never accept anything. No /judge score is ever used to pick a "best part".

Trigger: the card enters the allocator only from round 2, and in the stagnation reset's pool of unused tuples (the ADaPT pattern). At most 1 instance per round. Cost is about 4-5x CoT per instance under B = 20x.

Scope: on for the formalizable ARC subset, MacGyver and Stage 4 multi-hunk diffs. Off for BRAINTEASER, recorded in plan.md the same way the revise exclusion is.

Ledger rows gain n_parts, mode, K, combos_run, combo_pass, and comp_gap (a combination whose parts all passed their part_tests but which failed the whole check).

New section 8 table row: "Decompose (I2) | portfolio with vs without the decompose card; single-context decompose-then-solve rung; on-failure vs always-eligible trigger; on MacGyver 2x2 with compose | P1 | post-gate".

Research-round task: add catalog rows for Parsel, ADaPT, the compositionality gap (Press) and Token Economies. The research base has no evidence yet on LLM decomposition.

Deferred to P2: script-chosen subgoals by betweenness on an /encode state graph (CTL-07), to be built only once some benchmark yields a state graph.

### Metric and ablation

Post-gate, on dev-ablate, at matched tokens, under the MSR-12 keep/drop rule. H0: the solve rate with the card (ground truth, harness-scored) is <= the solve rate without it. Decision by the Beta(1,1) discordant-pair rule, keep if P(helps) > 0.95, with a cluster bootstrap over items, and coverage and selection deltas reported separately. Report the effect against both the scaffold without the card and the stronger best-of-N null.

Required secondary contrasts:
- (a) Pr13 rung: one context told to decompose, then solve, then assemble (least-to-most in one call), with the same /verify and the same tokens. If this rung matches the card, drop the card.
- (b) Trigger: eligible only from round 2 or at stagnation, vs eligible from round 1.
- (c) MacGyver only: a 2x2 of decompose x compose (GEN-13).

Sweeps on dev-tune, not keep/drop: K in {1,2,3} at equal tokens; P_max in {2,4}; script combination selection vs a random pick of part candidates.

Diagnostics stratified by a pre-tagged "compositional" item flag: per-card share of verified wins; the comp_gap rate (combinations whose parts all pass but which fail the whole); the rate at which plans exceed P_max or fail to parse.

### Cost

Build: about 1-2 days. That covers the card YAML and templates, the foreach field in run_card.py, compose_parts.py with ARC and diff composition plus the combination cap, the ledger fields, and the plan.md exclusion. Run cost per instance: decomposer about 1C, plus P x K part calls at about 0.5C each, plus 0C (script) or 1C (prose composer), giving about 4-5x CoT, plus about 7 subagent overheads. That is roughly 20-25% of a 20x scaffold budget for one round. Executing combinations by script is free under the section 8 cost definition. Ablation: one post-gate keep/drop arm plus 3 secondary contrasts, about the same size as the compose (GEN-13) slot.

### Risks

1. Part solutions that pass on their own often fail once combined (Press: about 40% compositionality gap; Faith and Fate: errors pile up with depth). Mitigation: keep K versions per part, try combinations by script, and accept only on the whole-problem check. Log comp_gap so this failure shows up.
2. LLM-written part_tests and judge-picked parts would bring back self-evaluation inflation and let one bad part spoil the rest (Decomposition Dilemmas; QDMR error propagation). The rule "prune only, never accept" must be enforced in code.
3. Matched cost: Token Economies finds that elaborate strategies often lose to self-consistency at equal compute, so the card may never pay back its extra calls. The single-context rung and the on-failure trigger test this directly.
4. A decomposition is itself a frame (REP-13; GEN-03 fixation). Keeping it inside one card, not in /encode, means holistic cards are not forced into the same framing.
5. Gains in the literature come mostly from code and formal proofs, where every part has a real checker. ARC parts have no ground truth of their own, so expect modest gains there.
6. On MacGyver it overlaps with compose, and the two may cancel out, which is why the 2x2 is needed.

### Related catalog ids

CTL-07, GEN-13, GEN-14, GEN-12, EVL-11, EVL-04, CTL-09, REP-01, REP-05, REP-13, GEN-03, GEN-17, OTH-02, MSR-02, MSR-05, MSR-12, CTL-11

### Prior art

- Parsel (Zelikman et al. 2023), https://arxiv.org/abs/2212.10561 : K implementations per function, test-searched combinations; APPS pass rate >75% higher than direct sampling, HumanEval 67% to 85%.
- FunCoder (Chen et al. 2024), https://arxiv.org/abs/2405.20092 : recursive sub-functions picked by behavioural consensus; +9.8% average over 4 benchmarks.
- Draft, Sketch, Prove (Jiang et al. 2023), https://arxiv.org/abs/2210.12283 : subgoal sketches closed by a prover; miniF2F 20.9% to 39.3%.
- DeepSeek-Prover-V2 (2025), https://arxiv.org/abs/2504.21801 : Lean-checked recursive subgoals; miniF2F-test 88.9%.
- ADaPT (Prasad et al. 2024), https://arxiv.org/abs/2311.05772 : decompose only on executor failure; +28.3 ALFWorld, +27 WebShop, +33 TextCraft.
- Least-to-Most (Zhou et al. 2022), https://arxiv.org/abs/2205.10625 : SCAN 99.7% vs 16.2% CoT, small GSM8K gains; single context, not cost-matched.
- Compositionality gap / Self-ask (Press et al. 2022), https://arxiv.org/abs/2210.03350 : about 40% gap, constant across model size.
- Reasoning in Token Economies (Wang et al. 2024), https://arxiv.org/abs/2406.06461 : self-consistency often beats complex strategies at matched compute.
- Decomposition Dilemmas (Hu et al. 2024), https://arxiv.org/abs/2411.02400 : decomposition lowered GPT-4 accuracy; noise grows with the number of sub-claims.
- Chain of Thoughtlessness (Stechly et al. 2024), https://arxiv.org/abs/2405.04776 : decomposition gains brittle beyond the exemplar sizes.
- Correa et al. 2023, https://arxiv.org/abs/2211.03890 : humans decompose to cut planning cost, subgoals at bottlenecks (betweenness), N=806.

Evidence grade. For: strong ML results when each part has an external checker and assembly is searched under a whole-problem check (Parsel, FunCoder, DSP, DeepSeek-Prover-V2), plus ADaPT for decomposing only on failure. Against: none of these is measured against best-of-N at matched cost with the same verifier; Token Economies, the compositionality gap and Decomposition Dilemmas show gains vanish or reverse without per-part checks. The human evidence (Correa 2023) supports decomposing to save cost, not to multiply it.

---

## I3. Idea tree or graph to see connections and convergence

### The idea in the owner's words

We need to represent ideas as a tree or a graph to see how they are interconnected and what comes after what, and to see whether ideas converge.

### Verdict: adapt (confidence 4/5)

Most of this is already built. Every candidate records its parents, lineage and island, so the tree already exists as data. Revise and recombine are the operations that grow it, and the tournament picks which branches to grow. Two pieces are missing. First, nothing writes the graph out or lets you look at it. Second, dedup throws away the record of which candidates landed on the same answer. We add a script that writes both after every cycle, at zero token cost, plus a picture for you to inspect. The one new signal is convergence counted by independent roots: a child agreeing with its own parent is not a second vote. That signal goes into calibration only, and only if it improves held-out Brier. The graph never goes into a generator prompt, because that would anchor the generators. Published tree-search gains mostly disappear once the baseline gets the same budget, so tree or graph structure is kept as a view and a calibration feature, not as a new search procedure.

### What v0.2 already does

cands/<call>.jsonl already stores parent_ids, operator, card, seed, perm, island_id and lineage_id for every candidate (ARCHITECTURE.md lines 129-130). memory/experiments/ledger.jsonl stores lineage_id and parent_ids (line 276). The revise card (fix/specialize/recurse, 1 parent at P0; generalize/recombine, 2 parents at P1) plus the script tournament (Pr18) is verifier-scored tree expansion, so the ToT/GoT search part of I3 already exists. The transform card is an explicit 3-call DAG. dedup.drop merges identical nodes (line 320). agreement(probe, C) with cached probe clusters measures convergence of independent seeded calls (lines 226, 323). The /judge P1 top-k lineages (EVL-04), the MSR-10 lineage-depth metric (line 560) and the GEN-14 descendant-cluster diversity metric are already defined.

What is missing: a persisted edge/cluster file (dedup logs only dup_rate and discards cluster membership), any reader or render of the graph, and agreement that discounts non-independent (shared-ancestor) members. Agreement is computed against probe clusters only, not across lineages.

### Proposed change

1. P0 driver step (structural, 0 tokens). harness/think/dedup.py: dedup.drop also returns cluster membership, and think.py appends it to runs/<id>/clusters.jsonl as {cluster_id, rule, members[cand_id], representative_id, round}. This uses the same benchmark rule as now (exact option, ARC output grid, embedding plus threshold for text).
2. P0 new script harness/graph.py, run by think.py after each cycle. It writes runs/<id>/graph.jsonl with two record types: nodes {cand_id, card, operator, round, island_id, lineage_id, root_ids, status, vtype, cluster_id, matches_default} and edges {src, dst, kind: parent_of | same_cluster | covers_constraint}, where covers_constraint comes from the /verify step 5 constraint mapping. Per cluster it derives n_members, n_independent_roots (distinct root_ids with no shared ancestor) and n_independent_nonseeded (roots from low_prior/transform/formal cards only). `python harness/graph.py --render runs/<id>` writes graph.html (or .dot) for the owner. This is a diagnostic, exempt from ablation, and its metric is 100% node/edge completeness against cands and verify rows.
3. P1 flag flags.lineage_independence_feature. Before calibrate() runs, n_independent_roots and n_independent_nonseeded of the candidate's cluster (pooled with probe clusters) become logistic features in memory/views/<batch>/calibration.json beside agreement and the existing "matches an encode default" covariate. The feature is fit on dev-tune only, with the same >= 300 pair and held-out-Brier gate as p_raw (Pr17, EVL-08). It affects only state.conf and therefore verification order and k. It never touches acceptance or the stop rule (Pr7). A cluster that converges on a /encode default keeps the defaults routing (Pr5) and gets no confidence bonus.
4. P1 optional flag flags.complementary_parents. For the 2-parent recombine operator, tournament.py picks the pair whose covers_constraint sets have the largest union, instead of the plain tournament pair. This is set arithmetic at 0 tokens.
5. Hard rules added to the /generate and run_card.py sandbox lint: graph.jsonl, clusters.jsonl and any lineage view never enter calls/<id>/in/.

Rejected parts: graph in generator prompts (SOC-01 anchoring, Pr18); LLM-labelled depends-on edges between ideas (ungrounded, Pr11; dependency DAGs over sub-problems belong to I2); ToT-style self-evaluated pruning (Pr7); reviving the EVL-11 networkx graph as a scoring signal (already replaced by checklist coverage).

Deferred parts: a "verifier-scored beam over revise children (width 2, depth R_max)" harness arm vs the current scaffold at matched B. This waits until Stage 4 trees are deep enough to matter, and until the next research round adds ToT/GoT/MCTS/quality-diversity prior art to the mechanism catalog.

### Metric and ablation

(a) The graph view is a diagnostic and is exempt from ablation. Its metric is that 100% of cands rows appear as nodes, 100% of parent_ids appear as parent_of edges, and every dedup drop maps to a cluster row. This is checked by `python harness/graph.py --check runs/<id>` in CI.

(b) flags.lineage_independence_feature. H0: adding n_independent_roots and n_independent_nonseeded to the agreement-only calibration model does not improve held-out Brier or AUROC of P(correct) on dev-tune. Arms: agreement-only; agreement + raw cluster size (n_members, which counts parent-child pairs); agreement + n_independent_roots (+ nonseeded). This adds a row to the existing EVL-08 post-gate slot. Evaluation stratified by vtype and difficulty bin, min 50 items per cell, bootstrap CIs. Keep only if it beats both other arms on held-out Brier; beating the raw-size arm shows that counting independence matters. Secondary: verified solve rate and tokens when verification order uses conf with vs without the feature, at matched B, against seeded best-of-N with the same verifier. Timing: run at Stage 3 but expect a null because tree depth is at most about 2 and BRAINTEASER has no revise. Rerun at Stage 4 with islands before dropping.

(c) flags.complementary_parents. H0: complementary-coverage recombine pairs give no higher verified solve rate than tournament pairs at matched tokens on ARC/MacGyver dev-ablate. Post-gate ablation, P1.

### Cost

0 extra LLM tokens per problem (vs plain CoT +0x). The embedding cost is unchanged because dedup already embeds. Engineering: about 200-300 lines of python (graph.py, the dedup persistence change, the calibrate feature hook, a lint rule) and 1-2 days. Calibration reuses the dev-tune pairs already being collected for EVL-08. Storage is a few KB per run.

### Risks

- Same-model convergence can be a shared bias rather than truth (Kim et al. 2025: about 60% same-wrong-answer agreement), so the feature could reward the modal default. Mitigations: count only independent roots, add a separate non-seeded count, keep the default covariate and defaults routing.
- Little signal is expected before Stage 4 because trees are shallow, so an early null must not kill the feature prematurely, and an early positive may be noise.
- The rendered graph invites the owner, or a later design change, to feed it into prompts, which would break isolation; the lint rule prevents that.
- Root definition is ambiguous for recombine children with two parents from different roots: count both roots, but never let one candidate contribute more than one independent vote.
- Adding a feature to calibration risks overfitting on small cells; the minimum cell size and the held-out gate handle this.

### Related catalog ids

GEN-14, GEN-12, SOC-01, SOC-03, SOC-04, SOC-05, EVL-04, EVL-08, EVL-11, EVL-12, CTL-06, CTL-07, CTL-10, CTL-13, REP-03, REP-07, MSR-10, MEM-06

### Prior art

- Tree of Thoughts (Yao et al. 2023), https://arxiv.org/abs/2305.10601 : Game of 24 74% vs CoT 4%, at a large token multiple and with LLM self-evaluation.
- Graph of Thoughts (Besta et al., AAAI 2024), https://arxiv.org/abs/2308.09687 : +62% sorting quality vs ToT, no matched best-of-N.
- Reasoning in Token Economies (Wang et al. 2024), https://arxiv.org/abs/2406.06461 : at equal compute CoT-SC often beats elaborate strategies.
- When is Tree Search Useful for LLM Planning? (Chen et al., ACL 2024), https://aclanthology.org/2024.acl-long.738 : needs about 90% discriminator accuracy.
- Scaling test-time compute optimally (Snell et al. 2024), https://arxiv.org/abs/2408.03314 : beam beats BoN only at low budget on medium items.
- Self-Consistency (Wang et al. 2022), https://arxiv.org/abs/2203.11171 : convergence of independent paths predicts correctness.
- Correlated Errors in LLMs (Kim et al., ICML 2025), https://proceedings.mlr.press/v267/kim25e.html : same-wrong-answer agreement about 60%.
- Language Agent Tree Search (Zhou et al. 2023), https://arxiv.org/abs/2310.04406 : gains come from environment reward.
- Metaprogram search (Rule et al. 2024), https://pmc.ncbi.nlm.nih.gov/articles/PMC11316799/ : lineage of structural edits.
- Atom of Thoughts (Teng et al. 2025), https://arxiv.org/abs/2502.12018 : dependency DAG, relevant to I2.
- Correa et al. 2023, https://arxiv.org/abs/2211.03890 : human subgoal decomposition on graphs, N=806, planning not ideation.

Evidence grade. For: self-consistency (replicated) shows that independent paths converging predicts correctness, and LATS/Snell show that tree expansion helps when an external verifier scores the nodes. Against: budget-matched studies (Wang 2024, Snell 2024, Chen 2024) find no gain from tree or graph structure alone over best-of-N; correlated same-model errors (Kim 2025) undercut convergence as independent evidence; EVL-11's idea graph was already rejected as an analogy-based scoring signal.

---

## I4. Keep tree nodes in superposition before deciding

### The idea in the owner's words

We need to have the tree nodes in a kind of quantum superposition before deciding which one is correct. I think there was an agent that thinks this way, so check what can be done here.

### Verdict: adapt (confidence 4/5)

The idea has merit, but the quantum version cannot be built here. Systems that really hold several answers in one thought (Coconut, Soft Thinking) need model internals or training, which Claude does not expose. Even with that access, a 2026 study found they collapse to one thread. The buildable core is: do not commit early, and keep several weighted branches alive until a verifier decides. v0.2 already does most of this. The gap is that v0.2 still drops branches by unverified confidence: only the top 3 get verified, the population keeps 5, and revise picks 2 parents. First we measure whether a correct answer ever gets dropped this way, which costs nothing. If it does, we test a particle-style resampler that uses verifier scores only, on graded tasks (ARC-style puzzles, MacGyver), against today's tournament at the same token cost. Tree of Thoughts with LLM-scored steps is rejected, and no card text will ever ask the model to "hold hypotheses in superposition".

### What v0.2 already does

Most of I4.

1. No early commitment: the stop rule accepts only an externally verified candidate with calibrated P(correct) >= T. Otherwise the run returns a labelled best guess or abstains (CTL-05, EVL-15, Pr3/Pr15, ARCHITECTURE s4 stop logic).
2. Several branches run in parallel: n0 = 4-5 isolated generators per round, revise lineages with parent_ids and lineage_id (GEN-14), an admitted population state.pop with k_pop = 5 (CTL-09), and revise_queue.
3. Evidence-weighted, stochastic selection: revise parents are chosen by a size-2 script tournament on verifier scores (Pr18), which already works as a crude particle resampler.
4. Develop several, then decide: EVL-04 develop-top-k-then-select (k swept 1/2/3) is a P1 arm.
5. Evidence collapses rivals: the P1 discriminating test (/verify step 6, EVL-02), the P1 abduce-probe card (GEN-15, Stage 4), and agreement-driven verify attempts (CTL-06).
6. Weighted lineage populations: Stage 4 islands plus tournament (SOC-03, SOC-05).
7. The overturn measurement: the MSR-07 transition matrix and net correction above churn.

What v0.2 lacks: a per-lineage weight carried across rounds, resampling over all live lineages, and any metric of the loss from its three hard pruning points. Those points are top(C, by=conf, n=m_verify=3), admit.update eviction at k_pop, and tournament n=2.

### Proposed change

Delta only, in three steps. Step 2 runs only if step 1 shows headroom.

STEP 1 (P0, diagnostic, no new mechanism). Add a pruning-regret block to ARCHITECTURE s8, next to MSR-05 coverage vs selection. A new script, harness/measure/pruning_regret.py, reads the ledger plus runs/<id>/candidates and does the offline, post-hoc check of every generated candidate against the key. It runs on keyed items only, and the result is never fed back into a run. Per benchmark, it reports the share of items where a key-correct candidate existed but the run did not return it, split by cause: (a) never verified (outside top-m_verify by conf), (b) evicted from state.pop by k_pop, (c) never chosen as a revise parent. It also reports a late-winner rate: the share of verified final solves whose lineage was not top-ranked after round 1. Gate: if (a)+(b)+(c) is below 5% of items on dev-tune for ARC-style and MacGyver-labelled items, close I4 and skip step 2.

STEP 2 (P1, post-gate, structural, behind a flag).
- Arm A, flags.frontier in {tournament (v0.2 default), beam_topK (deterministic top-K by partial score), smc}. New module harness/think/frontier.py replaces the tournament(state.revise_queue, n=2) call in s4. It writes runs/<id>/frontier.jsonl with rows {epoch, round, particle_id, lineage_id, cand_id, parent_particle_id, partial_score, log_weight, weight, ess, resample_seed, alive}, and state.json gains {frontier_epoch, ess}. Weights are w proportional to exp(beta x partial_score), where partial_score comes only from the verifier: ARC train-pair match fraction (never the test output), MacGyver checklist fraction. Never conf or p_raw (Pr7, EVL-01). Systematic resampling to K particles when ESS < K/2, with an exploration floor epsilon so that every live lineage keeps nonzero mass. K = 2 (equal to the revise spawn cap), so the spawn count is unchanged. The frontier lives within one Pr8 reset epoch and is wiped on reset. Flag off on BRAINTEASER (no partial score, no revise). New s5 rows: beta, epsilon and K, all placeholders, dev-tune.
- Arm B, flags.verify_order in {top_conf (default), top_conf_plus_explore}. Of the m_verify = 3 slots, 2 go to the top by conf and 1 to a uniform draw from the unverified remainder, logged with its seed. m_verify is unchanged, so the cost is matched. Enable this arm only if cause (a) dominates in step 1. Enable Arm A only if (b) or (c) dominates.

STEP 3 (priority change only). Move the /verify step 6 discriminating test between rival candidates (EVL-02) ahead of other P1 items for ungraded items. On those items, "collapse by a discriminating probe" is the usable form of I4.

Explicitly rejected: latent or continuous-thought superposition (needs internals; REP-01 caveat; Wu 2026); ToT/GoT trees over partial steps scored by LLM value prompts (Chen 2024: needs a discriminator above about 90% accuracy); any card text asking the model to "hold hypotheses in superposition" (Pr13).

Filed separately, not part of I4: a Thought-of-Search variant of the formal card, where the LLM writes the successor function and goal test as code and a script runs classical search.

### Metric and ablation

Diagnostic (step 1, runs first, about 0 tokens): pruning-regret rate per benchmark = (number of keyed items with a key-correct candidate in the pool that was not returned) / (number of keyed items). It is split into causes (a) never-verified, (b) k_pop-evicted and (c) never-revised, with item-cluster bootstrap CIs. Also reported: late-winner rate. Drop rule: if the total is below 5% on dev-tune, stop.

Ablation (step 2): on dev-ablate graded items (ARC-style and the MacGyver labelled subset), run tournament vs smc vs beam_topK, and top_conf vs top_conf_plus_explore, at matched realized tokens. The best-of-N arm with the same verifier stops at the scaffold's spend. H0: solve rate(smc) <= solve rate(tournament). Keep if P(helps) > 0.95 under Beta(1,1) on discordant item pairs, with the cluster bootstrap over items. The beam_topK arm isolates whether deterministic pruning is what hurts. Run at m = 5 and m = 20 (Snell 2024 predicts gains at low budget and on hard items that shrink at high budget).

Secondary: MSR-07 net correction above the churn null, and the change in the pruning-regret rate under each arm (it should fall under smc/explore). Expected null on BRAINTEASER, where the flag is off. Report it as a negative control.

### Cost

Step 1: a ledger script, no LLM tokens, about half a day of engineering. It needs the per-candidate key check, which already exists for MSR-05 oracle pass@pool. Step 2: about 0 added LLM tokens per problem at K = 2 and m_verify = 3, since resampling and the explore slot are script-side and spawn counts do not change. Raising K to 4 unmatched would add about 6-9 plain-CoT units per problem (about +30-45% of the m = 20 budget), so keep K tied to the revise cap. Engineering is about 1-2 days for frontier.py and the jsonl schema. Evaluation uses one post-gate P1 ablation slot on dev-ablate at 2 budgets.

### Risks

- The headroom may be near zero: if the pruning points rarely drop a correct answer, step 2 is wasted. Step 1 gates this.
- Partial scores may be poor weights. An ARC train-pair fraction can reward overfit or degenerate programs (scorer over-optimization, as in Snell 2024), so beta has to stay modest and the exploration floor matters.
- The evidence comes from step-level PRM resampling over token rollouts (Puri 2025), not from whole-candidate revise lineages, so the transfer is unproven.
- Confidence must not creep into the weights. Any use of conf or p_raw as a particle weight breaks Pr7 and EVL-01, so a lint check on frontier.py inputs is needed.
- The explore slot in verify_order could lower the solve rate where conf ordering is already good, and the ablation must detect that.
- A frontier carried across a Pr8 reset would reintroduce failed candidates, so keep it scoped to the epoch.
- The "superposition" framing could later leak into card text as an instruction, which the plan rejects.

### Related catalog ids

CTL-05, CTL-09, CTL-06, CTL-07, CTL-08, CTL-11, EVL-15, EVL-01, EVL-02, EVL-04, EVL-08, GEN-14, GEN-10, GEN-02, GEN-15, GEN-07, MSR-05, MSR-07, SOC-03, SOC-05, SOC-07, REP-01, REP-08

### Prior art

- Tree of Thoughts (Yao et al. 2023), https://arxiv.org/abs/2305.10601 : Game of 24 74% vs best-of-100 CoT 49%, not token-matched.
- Graph of Thoughts (Besta et al. 2023), https://arxiv.org/abs/2308.09687 : +62% sorting vs ToT; baselines are only other prompting schemes.
- When is Tree Search Useful for LLM Planning (Chen et al., ACL 2024), https://arxiv.org/abs/2402.10890 : needs a discriminator above about 90% accuracy to beat reranking; 10-20x slower otherwise.
- Reasoning in Token Economies (Wang et al. 2024), https://arxiv.org/abs/2406.06461 : budget-matched self-consistency often beats complex strategies.
- Rollout Roulette, particle-based Monte Carlo (Puri et al., NeurIPS 2025), https://arxiv.org/abs/2502.01618 : 4-16x better scaling rate than deterministic beam/DVTS with the same PRM.
- Scaling test-time compute optimally (Snell et al. 2024), https://arxiv.org/abs/2408.03314 : beam beats best-of-N at low budget and on hard items, over-optimizes at high budget.
- Coconut (Hao et al. 2024), https://arxiv.org/abs/2412.06769 : trained continuous thoughts encode several frontier nodes; needs training.
- Reasoning by Superposition (Zhu et al., NeurIPS 2025), https://arxiv.org/abs/2505.12514 : theory of continuous CoT holding parallel BFS frontiers.
- Soft Thinking (Zhang et al. 2025), https://arxiv.org/abs/2505.15778 : probability-weighted embedding mixtures; needs logits and embeddings.
- LLMs are Single-threaded Reasoners (Wu et al., ICLR 2026), https://arxiv.org/abs/2508.03440 : soft thinking collapses to the top token without injected randomness.
- Thought of Search / AutoToS (Katz et al. 2024, https://arxiv.org/abs/2404.11833 ; Cao et al. 2024, https://arxiv.org/abs/2408.11326 ): LLM-written successor and goal code plus classical search, 100% on 24 Game, BlocksWorld and others.

Evidence grade. For: Puri 2025 (one strong NeurIPS paper) shows that resampling weighted particles beats hard pruning under a noisy scorer, and Snell 2024 shows step-level search wins at low budget and on hard items. Against: Chen 2024 shows tree search loses to reranking without a discriminator above about 90% accuracy, and Wang 2024 finds budget-matched self-consistency often wins. Latent superposition is unbuildable here and collapses to a single thread anyway (Wu 2026). None of this is in the project's own catalog: it is LLM-search literature, graded as external single papers.

---

## I5. Find out what the agent's subconscious is thinking

### The idea in the owner's words

Somehow find out what the agent's subconscious is thinking.

### Verdict: adapt (confidence 4/5)

v0.2 already does most of the doable part of this idea. It records the model's first answers, measures how spread out its answers are across repeated calls, and logs every candidate, including the ones nobody checks. We cannot read what the model is really thinking. Claude's API gives no logprobs, no activations and no raw chain of thought. When a model says what it considered, that is new text, and studies show these accounts are often unfaithful. The evidence also does not support a "subconscious" that solves problems in the background. What is new and nearly free is a third source of candidates. A script collects options that show up in a generator's visible scratch text or thinking summary but not in its final list. First we measure whether right answers ever appear there. If they do, those candidates compete with everything else for verification, and we test them against the same spend on extra plain samples. We drop the "subconscious" label. Interpretability (lenses, probes, attribution graphs) waits for a separate open-weight study after Stage 5.

### What v0.2 already does

Nearly all of the feasible core is already built.

1. First moves: /encode step 3 (ARCHITECTURE.md line 192, GEN-03, Pr5) makes a separate fresh call that writes 5 default answers to private/defaults.json. It is never routed to generators, and a script uses it for near-default routing.
2. Distribution over candidates: the CTL-06/EVL-08 agreement probe (Pr17) runs 3-5 seeded calls per problem, caches them, clusters them by script, and uses agreement, not self-report, as the P0 confidence signal.
3. First move against final answer: MSR-07 compares the round-0 top candidate with the final answer in a transition matrix against a churn null.
4. Logged but unspoken candidates: each generator emits about 8 candidates (GEN-06), all of them go to cands/<call>.jsonl, and only m_verify=3 are verified. MEM-06 (P2) re-scores dormant candidates after a restructure, as an ordering key only.
5. Self-reported reasons are already stripped (EVL-16 post-check, /generate step 4), and stated confidence never ranks anything (Pr7).

Not covered: candidates that appear in a generator's thinking summary or scratch text but not in its numbered list, the origin of a candidate, and any measure of selection loss inside a generator.

### Proposed change

Delta only.

(A) P1 diagnostic, no effect on the loop.
- harness/run_card.py requests thinking with display:'summarized' on generator calls and writes calls/<id>/thinking.txt. It first checks whether claude -p stream-json exposes thinking events; if not, it uses the direct Messages API fallback already listed as an open question in section 10.
- A new harness/harvest.py extracts candidate-shaped spans from thinking.txt and from any visible non-list text: option letters, grids, code blocks and numbered items. Copying is verbatim. Justification and confidence markers are stripped, as in the EVL-16 post-check. Spans are deduped against the spoken list.
- Output is cands/<call>.unspoken.jsonl with {id, text, origin:'unspoken', source_call, span_hash}.
- The cands schema gains origin in {spoken, unspoken, probe, default}.
- The harness scores two numbers offline with the answer key. unspoken_correct_rate: the share of items whose correct answer appears only in unspoken spans. unverified_correct_rate: the share of items whose correct answer was spoken but never got an m_verify slot. These go into the section 8 coverage/selection decomposition as a third term.
- The routing table gains a row: thinking.txt is private and never copied into any sandbox.

(B) P2 flag flags.harvest_unspoken, post-gate. Enable it only if unspoken_correct_rate is at least 3 points on dev.
- In think.py, after C = collect(): U = harvest(calls); U = dedup.drop(U, C + prior); C += U[:u_max] with u_max=2 per call. Judging and verification are unchanged.
- Harvested candidates compete for the same m_verify slots. Judge calls on U are charged to state.spent.

(C) Cost fold, P1. Replace the separate GEN-03 defaults call with private/prior_map.json {cluster_id, count, sources, exemplar_hash}, built from 5 independent plain-arm samples (SYNTHESIS row 84) and the cached probe clusters. It is script-only, and Pr5 still holds.

(D) Text and lint.
- Remove "subconscious" framing from the design text.
- Add a Pr10 lint rule that fails any template with "subconscious", "free-associate" or "reveal your hidden reasoning" wording. This also avoids reasoning_extraction refusals.
- Asking a generator for its "rejected alternatives" is not a component. It exists only as an instructional control arm.

(E) Deferred. Logprobs, logit or tuned lens, SAEs, attribution graphs, forking-token resampling and TIP go into a separate open-weight-generator study after Stage 5, outside the gate.

### Metric and ablation

Diagnostic (P1, zero loop tokens): unspoken_correct_rate and unverified_correct_rate per benchmark on dev, scored offline with the key. Gate for (B): unspoken_correct_rate is at least 3 points.

Ablation for flags.harvest_unspoken (P2, dev-ablate, post-gate slot). H0: verified solve rate per item at matched token cost is no higher with harvest on than off. Decision: Beta(1,1) on discordant item pairs, P(helps) > 0.95.

Arms: (1) harvest off (v0.2 baseline); (2) harvest on; (3) harvest off, plus extra seeded generator calls with the same tokens as arm 2's judge cost (the real competitor); (4) instructional control: the generator template adds "also list 3 options you considered and set aside", at matched tokens.

Secondary metrics: oracle pass@pool coverage delta; share of verified wins with origin=unspoken, divided by the share of tokens spent on U; dedup rate of U against C; refusal rate (reasoning_extraction). Everything is reported against seeded best-of-N with the same verifier at matched cost.

Prior-map fold (C): check that the near-default routing decisions under prior_map.json match those from defaults.json on at least 90% of items. If they do, keep the fold for the saving of one call.

### Cost

Diagnostic: about 0 extra generation tokens if generators already run with thinking, because thinking is billed the same whatever the display setting. If thinking is not already on, the thinking tokens themselves add cost and must be budgeted. Parsing is script-only. P2 flag: about +1 to +3 plain-CoT units per problem in judge calls on at most 2 harvested candidates per generator (5-15% of B at m=20). Verify cost is unchanged because of the m_verify cap. Prior-map fold: saves 1 call per problem (about -0.3 to -0.5 CoT units). Engineering: about 1-2 days for harvest.py, the schema field, the routing row and the lint rule.

### Risks

- Thinking summaries are model-written and lossy, so they may carry almost no extra correct candidates. The diagnostic gate exists to catch this cheaply.
- It is unverified whether claude -p exposes thinking text. The fallback is direct API calls, which bypass Claude Code primitives.
- Summaries mix proposals with self-critique. A poor span extractor could leak a generator's verdict or confidence to the judge, breaking Pr1/Pr7.
- Harvested candidates are correlated with the spoken list (same context, SOC-07 homogeneity), so the dedup rate may be high and the gain may be no more than arm 3's.
- Prompts that ask for hidden reasoning can trigger reasoning_extraction refusals, which waste tokens and bias the sample. That is why harvest uses the API display flag, not a prompt.
- Owner risk: the "subconscious" label may encourage reading meaning into self-reports. The evidence says they are new samples, not readouts.

### Related catalog ids

GEN-03, GEN-06, GEN-07, CTL-06, CTL-15, CTL-17, EVL-08, EVL-16, EVL-01, EVL-03, MSR-07, MSR-04, MSR-15, MEM-06, STA-03, STA-11, SOC-07, REP-02, OTH-02

### Prior art

- Chen et al. 2025 (Anthropic), Reasoning Models Don't Always Say What They Think, https://arxiv.org/abs/2505.05410 : Claude 3.7 Sonnet's CoT mentioned a hint it had used about 25% of the time, R1's about 39%.
- Turpin et al. 2023, Language Models Don't Always Say What They Think, https://arxiv.org/abs/2305.04388 : CoT hides biasing features.
- Lanham et al. 2023, Measuring Faithfulness in CoT, https://arxiv.org/abs/2307.13702 : larger models were less faithful on most tasks.
- Lindsey et al. 2025, attribution graphs on Claude 3.5 Haiku, https://transformer-circuits.pub/2025/attribution-graphs/biology.html : the stated method differs from the internal mechanism; needs weights.
- Lindsey 2025/2026, Emergent Introspective Awareness, https://arxiv.org/abs/2601.01828 : concept-injection detection is unreliable and context-dependent.
- Wang et al. 2025, Underthinking of o1-like LLMs, https://arxiv.org/abs/2501.18585 : correct early thoughts abandoned in wrong answers; TIP up to +10.7% but needs logits.
- Zhang et al. 2025, Verbalized Sampling, https://arxiv.org/abs/2510.01171 : 1.6-2.1x diversity in creative writing; no keyed solve-rate result.
- Xiong et al. 2024, Can LLMs Express Their Uncertainty?, https://arxiv.org/abs/2306.13063 : consistency beats verbalized confidence.
- Tian et al. 2023, Just Ask for Calibration, https://arxiv.org/abs/2305.14975 .
- Bigelow et al. 2024, Forking Paths, https://arxiv.org/abs/2412.07961 : needs token-level alternatives the Claude API does not expose.
- Li et al. 2023, Inference-Time Intervention; Belrose et al. 2023, Tuned Lens: latent knowledge readable only with open weights.
- Rahbar 2026, LLM ignition index (MSR-15), https://arxiv.org/abs/2608.05160 : activation probes, rejected for HTSA.

Evidence grade. For: Wang 2025 (moderate, open models, LLM-judged) shows reasoning traces often contain correct ideas that get dropped, and GEN-03 default sampling is replicated (N=3,972). Against: strong and replicated faithfulness work (Turpin 2023, Lanham 2023, Chen 2025) shows self-reports are not readouts of the computation; the Claude API exposes only summarized thinking with no logprobs or activations; unconscious-thought advantages fail to replicate (STA-03, GEN-07).

---

## I6. Different-field professional agents fill the gaps

### The idea in the owner's words

Have different-field professional agents look at the ideas and come up with their own ideas, to see if they can fill in the gaps.

### Verdict: adapt (confidence 4/5)

Your instinct is right that other fields can supply what our agents miss. Telling an agent to act as a professional is the wrong way to do it. In tests, profession personas did not raise accuracy and sometimes lowered it. Agents running on the same model also drift back to the same ideas, and an "expert" tends to give the expert's default answer, which v0.2 deliberately keeps away from generators. What does help is what an agent reads. v0.2 already covers most of this: the analogy card brings in far fields, the critics get different evidence documents, and a per-agent document pack was decided in SYNTHESIS but never written into ARCHITECTURE. The new piece is aiming that field knowledge at the gaps. A script finds the constraints no candidate covers yet. It then picks a field pack (that field's methods, standard parts and failure modes) matched to those gaps, and a fresh agent works from the gaps and the pack without seeing the other ideas. This should be tested after the gate, on MacGyver and the design set. No new skill, no new role, no persona.

### What v0.2 already does

About 70% is already covered in structural form.

1. Far fields for generation: the P1 analogy card takes 2 far sources from memory/domains.jsonl (about 200 domain descriptions), chosen by goal-text embedding, with a near-for-repair sub-arm and a typed-triple or code re-encoding mapping (GEN-08, REP-15, Pr9).
2. "Professionals review the ideas": the SOC-09 counterexample check. Each critic gets 2-3 script-seeded web documents as a divergent brief, a fresh tool-using checker confirms each objection, and critics may only demote. A shared-brief vs divergent-brief arm already exists.
3. Agents differ by what they work with, not by who they are: SOC-02. SYNTHESIS line 218 says "A retrieved-document pack is restored as a seed type (P1)", but ARCHITECTURE.md never implements it. /generate takes seeds only from memory/seeds/concepts.txt, and no pack file, card or ablation row exists, so this is documentation drift.
4. Component tables: the GEN-13 compose card uses components.json, physical properties only.
5. The persona ban is enforced by the GEN-11/Pr10 lint, and the MSR-03 diverse-persona result is already recorded as an open conflict with Pr10.
6. Building on existing ideas is legal only through the revise card, after an independent first round (GEN-10, GEN-14).

Not in v0.2: retrieval keyed on what the pool fails to cover, field checklists (methods, standard parts, failure modes) as a corpus type, and a test of whether a profession label adds anything beyond the content.

### Proposed change

Delta only, in this order.

(A) Consistency fix, no new mechanism. Write the SOC-02 retrieved-document pack into ARCHITECTURE.md: add it as a seed type in /generate's Input line, list the file in the section 2 layout, and add a section 8 ablation row. The pack and its arm are already decided in SYNTHESIS.

(B) New corpus memory/domain_packs.jsonl, built offline: about 50 fields, each row {field_id, text <= 1.5k tokens in third person (methods, standard components, failure modes, typical constraints), source_urls, embedding, corpus_hash}. Lint it like the templates: no role or identity phrasing, no "you are". Build cost is one-time and amortized.

(C) New driver step in think.py: after each /verify round, write runs/<id>/gaps.json = {round, uncovered_constraint_ids (from the /verify step 5 constraint coverage, minus those covered by any candidate), dropped_ids (from dropped.json), query_text}. query_text is built by script from the constraint text.

(D) New P1 card memory/strategies/gap_pack.yaml, one step, template gap_pack.gen.txt, inputs [goal, constraints, gap_ids + gap text, pack_text]. It never receives candidates, so it is a fresh generator, not a reviewer (Pr1, Pr8, GEN-10). The script selects the pack: top-k by cosine(query_text, pack embedding), then the least-used field among them, with the id logged. The card runs from round 2 only and is allocated by allocate.reallocate like revise. It does not count toward the directed-card minimum.

(E) Schema fields: cands rows and ledger rows gain pack_id, gap_ids and gap_key_mode. Add flags.gap_pack in {off, goal_keyed, gap_keyed}, default off in the gate configuration.

(F) Optional P1 extension of SOC-09: let the critic brief query also draw from the field-checklist entries of domain_packs.jsonl, so that "a professional finds the gap" is delivered as retrieved checklists to the existing demote-only falsifier. It is tested by the existing shared-brief vs divergent-brief arm plus a new "pack-brief" arm.

(G) Sanctioned diagnostic arm "label_only": the same card with a field name and no pack text, run under a harness-only lint exemption (the same mechanism as the instruction-only control). It never ships. Its purpose is to test the MSR-03 vs Pr10 conflict under our verifier.

### Metric and ablation

Testbed: post-gate only, on MacGyver dev-ablate (human-labelled subset) and the open-ended design set. Do not run on ARC (no fields) or BRAINTEASER (no computable gaps, and REP-02 predicts harm). Matched total budget B against the v0.2 scaffold and against best-of-N with the same verifier.

Primary metrics: verified solve rate or labelled rubric pass (oracle pass@pool), and gap closure = share of round-r uncovered constraint ids covered by a passing candidate in round r+1, per 1k tokens. Secondary metric: functional diversity against the Pr10 permutation null.

Arms, all at equal tokens with the gap_pack calls displacing seeded calls: (1) off vs gap_keyed; (2) gap_keyed vs goal_keyed, the decisive test of the new ingredient over GEN-08 and SOC-02; (3) 2x2 of pack content (gap-matched vs random field of equal length) x gap list (shown vs hidden); (4) pack only vs pack + field label vs label_only.

H0: gap_keyed gives no higher pass@pool or gap closure than goal_keyed or off. Keep/drop by the global Beta(1,1) rule P(helps) > 0.95. The prior is set to no effect because of the Liu 2026 LLM null.

For (F): AUROC of confirmed-objection count on the labelled MacGyver subset, pack-brief vs divergent web-brief vs shared-brief critics at equal tokens.

### Cost

Per call: about 3-4k tokens (pack 1.5k + problem view about 1k + 8 candidates about 0.8k) plus subagent overhead, about 1.5-3x one plain-CoT call. At 2 calls per round from round 2 with R_max 3-4, about 4-12x CoT per problem, all reallocated within matched B rather than added. Offline corpus build (about 50 fields, fetch plus distill): about 0.2-0.5M tokens once. Engineering: about 1-2 days (corpus builder, gaps.json writer, card, schema fields, 4 arms). The step (A) doc fix takes under an hour.

### Risks

- Expected effect is null to small: Liu 2026 found no LLM benefit overall from inspiration sources, and an LLM "outsider" is the same model drawing on another region of its own knowledge.
- Field packs may carry the expert default and act as a mental set (REP-02), reintroducing what Pr5 withholds. Track the "matches an encode default" covariate per arm.
- Gap computation depends on /verify's converter mapping candidates to constraints. If that mapping is noisy, the retrieval key is noise. Check converter agreement on dev first.
- Untestable before Stage 3, so it adds a flag and a corpus that sit idle through the gate.
- The label_only arm needs a lint exemption that must never leak into shipped configurations.
- Packs distilled by an LLM from web sources can contain errors. Third-person facts must not reach the verifier as ground truth.
- Fixation risk if anyone later "improves" the card by showing it the pool.

### Related catalog ids

SOC-02, SOC-09, SOC-07, SOC-01, GEN-08, GEN-13, GEN-11, GEN-10, GEN-14, REP-15, REP-02, EVL-13, OTH-01, MSR-03

### Prior art

- Zheng et al. 2024, When "A Helpful Assistant" Is Not Really Helpful (EMNLP Findings), https://arxiv.org/abs/2311.10054 : 162 personas, no gain over a no-persona control on 2,410 factual questions.
- Hu, Rostami, Thomason 2026, Expert Personas Improve LLM Alignment but Damage Accuracy, https://arxiv.org/abs/2603.18507 : MMLU 71.6% to 68.0%.
- Huang et al. 2025, Human versus Machine Creativity (Nature Human Behaviour): creative-genius personas lowered DAT scores (secondary summaries).
- Deng, Brucks, Toubia 2026, https://arxiv.org/abs/2602.20408 : ordinary personas raise diversity as sampling cues, diversity metric only.
- The Chameleon's Limit 2026, https://www.alphaxiv.org/abs/2604.24698 : persona populations collapse into stereotyped modes.
- Li et al., Self-MoA (TMLR 2026), https://arxiv.org/abs/2502.00674 : mixing agents lowered quality vs one strong model.
- STORM (Shao et al., NAACL 2024), https://arxiv.org/abs/2402.14207 : perspectives mined from retrieved articles; the gain sits mostly in the retrieved content.
- Scideator (Radensky et al. 2024-25), https://arxiv.org/abs/2409.14634 : facets retrieved at near and far distances and recombined by script beat a same-LLM baseline.
- Liu, Dubova, Conklin, Harada, Griffiths 2026, https://arxiv.org/abs/2603.19087 : null overall LLM benefit from inspiration sources.
- Shi and Evans 2023 (Nature Communications), https://europepmc.org/articles/PMC10039062 : outsider advances in human science, bibliometric.
- Wang et al. 2023, Solo Performance Prompting, https://arxiv.org/abs/2307.05300 : GPT-4 only, single-context role-play.

Evidence grade. For: STORM and Scideator show that retrieved-content perspectives help (moderate, n=22 and single-benchmark), plus SOC-02 (meta-analysis, small effect) showing deep-level diversity helps. Against the persona form: Zheng 2024 and Hu 2026 (strong, multi-model) and GEN-11. Against expecting large gains even from the structural form: Liu 2026 (LLM null, preprint) and SOC-07 (homogeneity).

---

## Suggested order for v0.3

Ranked by expected value per token. Items at the top cost no LLM tokens and either gate a later item or fix a known gap; items at the bottom spend real budget and start from a prior of no effect.

1. I4 step 1, pruning-regret diagnostic (harness/measure/pruning_regret.py). 0 tokens, about half a day. It decides whether I4 step 2 is worth building at all, and its late-winner rate is also the first evidence on whether I3's convergence feature can carry signal.
2. I3 items 1-2, persisted clusters.jsonl and graph.py with --render and --check. 0 tokens, 1-2 days. Gives the owner the tree view, makes dedup auditable, and supplies the root counts that I3 item 3 and the I4 diagnostic both read.
3. I6 step A, write the SOC-02 document pack into ARCHITECTURE.md. Under an hour. Pure consistency fix for a decision already taken in SYNTHESIS.
4. I5 part D, template lint for "subconscious" and hidden-reasoning wording, plus removal of the framing from design text. Under an hour, prevents reasoning_extraction refusals.
5. I5 part A, thinking capture and harvest.py diagnostic (unspoken_correct_rate, unverified_correct_rate). About 0 tokens if generators already run with thinking. Gates I5 part B.
6. I5 part C, fold the GEN-03 defaults call into prior_map.json. Saves one call per problem if the 90% routing-agreement check passes.
7. I3 item 3, flags.lineage_independence_feature in calibration. 0 tokens, reuses EVL-08 dev-tune pairs. Expect a null at Stage 3; do not drop before Stage 4.
8. I2, decompose card (plan, K=2 per part, script assembler, whole-problem acceptance). About 4-5x CoT per instance, reallocated within B. Widest scope of the token-spending items (ARC formalizable, MacGyver, Stage 4 diffs) and the strongest external evidence when every part has a checker.
9. I1, lemma card with lemma_check.py and state.lemma_pool. About 2.5-3x CoT per instance, reallocated. Narrower scope than I2 (ARC and formalizable only) and a preregistered prior of no effect at matched compute; run arm (e) against revise-with-recurse first.
10. I4 step 2, frontier.py (smc, beam_topK) and verify_order explore slot. About 0 added tokens, 1-2 days, but only if step 1 shows pruning regret above 5%.
11. I6 steps B-G, domain pack corpus, gaps.json and the gap_pack card. One-time corpus build of 0.2-0.5M tokens plus 4-12x CoT per problem reallocated; post-gate only, MacGyver and design set, prior of no effect (Liu 2026). Run arm (2) gap_keyed vs goal_keyed before anything else.
12. I3 item 4 (flags.complementary_parents) and I5 part B (flags.harvest_unspoken, P2). Both are small flags that only make sense once their upstream data (covers_constraint edges, unspoken_correct_rate >= 3 points) exists.

Across all twelve: nothing here changes the gate configuration. Every token-spending item is off by default, displaces seeded calls under matched B, and is decided by the section 8 Beta(1,1) keep/drop rule against the stronger best-of-N null.
