# Attention and framing: what gets looked at, in what order, and how the frame moves

*Part 2 of the thinking decomposition, 2026-10-13. Grades: strong = replicated or several controlled studies; medium = one controlled study or multi-model benchmark; weak = authors' own preprint numbers, single run, vendor post, opinion or abstract only. The shared search quota ran out after 14 queries; later sources were checked by fetching the page itself ("snippet" = seen only in a search result). Code claims are checked in the code, not the docs.*

## 1. What the loop does today

- **Ideation is equal; card choice is positional.** `ideate_round` gives each part x direction one generic and one research context, plus analogy, diagnosis and adapt contexts in round 1: about 56 contexts, up to 7 per part. The generic card is `IDEA_CARDS[len(specs) % 5]`, so card is confounded with list position.
- **Conversion to builds is not equal.** `tree.split_select` round-robins parts in map order (`parse_planner` appends `recipe` last). I simulated it with the default slots (10 builds = 2 long-shot + 8 main, 60% inward; round 2: 3; interrogation 12, then 6). Round-1 main builds: io 2, mix 2, ffn 2, depth 1, opt 1, **data, recipe, objective 0** (the 2 random long-shot slots can reach any part). Round 2: io 2, mix 1. Interrogation never reaches `objective` (round 1) or `opt` onward (round 2). The `mocktree` run folder shows the same shape. The documented fix (docs/IMPROVEMENTS.md 1d, headroom weights) was never built.
- **The discovery curve acts on cards only.** `attractor_cards` swaps a card for `formal`; the docstring's "fewer contexts when yield is low" is not wired (`n_ctx` is unused).
- **The frame is fixed.** Lens = `replicate % 5`, map drawn once, `--replan` off by default, upward proposals logged and unused, `history_text` says "build on a success".

## 2. Evidence, newest first

### 2.1 Allocating the next look in research agents
- **AIM (Sep 2026).** LLM "surrogate" ranks idea clusters, LLM "acquisition" sets explore/exploit, a planner splits branches. One-task ablation (90.5): no surrogate -4.6, fixed schedule instead of planner -2.4, no explicit explore/exploit -1.3, no variance. It loses on a smooth landscape (IFEval 61.8 vs 82.7 for AdaEvolve). [S1, weak]
- **Recursive self-improvement of research agents (Sep 2026):** UCB1 over five drafting strategies plus forking; the paper cannot say which part helps. [S2, weak] **DeepScientist (ICLR 2026):** LLM-scored UCB; 5,000 ideas, 1,100 implemented, 21 advances (1.9%); the scorer's accuracy is not reported. [S3, weak]
- **AB-MCTS (NeurIPS 2025):** Thompson sampling picks wider or deeper. Gains of 1-3 points over repeated sampling on code, modest against the spread; on ARC-AGI (GPT-4o) repeated sampling beat every variant (15.0 vs 14.0). [S4, medium-weak]
- **MLE-STAR (NeurIPS 2025):** an ablation run finds the block with the largest effect and only that block is refined; 43.9% any-medal vs 25.8% for AIDE; no ablation of the targeting step in the text I read. [S5, weak for the step] **AIRA-dojo (NeurIPS 2025):** with AIDE's operators, MCTS and evolution gave marginal differences; a better operator set lifted greedy search 39.8 to 45.5%; memory on/off was "nearly identical". [S6, medium]
- **Matched uniform controls, where they exist.** SEC (bandit over problem categories) vs a random curriculum: 3B AIME24 .075 to .100, Zebra-OOD .285 to .345, but 7B loses on 3 of 9 cells; seeds not reported. [S7, medium] DAPO's dynamic sampling (drop prompts that are all right or all wrong) is the last +8 points (42 to 50 AIME24) of a cumulative ablation. [S8, medium]

### 2.2 Curiosity, learning progress, information gain
- MAGELLAN (ICML 2025): an LLM agent predicts its own competence and progress across related goals; the authors call it the only method that fully mastered a large evolving goal space (one environment). [S9, weak-medium] OMNI-EPIC wants tasks both learnable and interesting [S10, weak]. Intelligent Go-Explore (ICLR 2025): a model judges which archived state to revisit; beats RL, graph-search and Reflexion baselines. [S11, medium-weak] A 2026 note frames context acquisition as information gain per token cost [S12, weak].
- **Raw surprise is a trap.** Prediction-error curiosity has documented limits in stochastic setups. [S13, medium] Infants look away from both the too-predictable and the too-surprising (n = 42 and 30; small effect). [S14, weak-medium] Use learning progress, never raw error.

### 2.3 Where leverage is, and where experts look
- Experts fixate more on task-relevant regions, less on irrelevant ones, with shorter fixations (2023 and 2025 reviews; correlational, mostly visual tasks, snippet). [S15, S16, medium]
- The same attention locks: chess players who found the familiar advantageous-but-suboptimal move kept fixating its region; blunders were dropped (n = 34; one suboptimal-case problem). [S17, weak-medium] A good-enough incumbent holds attention better than a failed one.
- Leverage is non-uniform and counterintuitive (Meadows; conceptual). [S18, weak] The Theory of Constraints has not shown effectiveness in the academic literature (Gupta and Snyder 2009, secondary summary). [S19, weak] I found no controlled test of "find the constraint first" as a thinking strategy. In an LLM trace, planning and uncertainty-management sentences carry outsized counterfactual weight. [S20, medium]

### 2.4 Framing, reframing, being stuck
- **Null result.** 280 participants, GPT-4o, four conditions including one scripted from Dorst's nine steps: no gain in expert-rated novelty or usefulness (all p > 0.05); experts gained more than novices. [S21, medium] Dorst's base is case studies. [S36, weak] I found no controlled study of reframing in research ideation.
- Wording alone is a large frame effect: up to 76 accuracy points from formatting (LLaMA-2-13B). [S22, strong]
- **Reflection without an outside signal fails.** No intrinsic self-correction of reasoning [S23, strong]; R1-Zero reflection is "not positively correlated" with accuracy [S24, medium]; 38 LLMs produced the right riddle answer without endorsing it in 5-39% of their wrong answers [S25, medium].
- **Too many switches hurt.** Wrong answers show 418% more thought switches; a switch penalty gave +0.6 to +5.8 Pass@1. [S26, medium]
- **Humans.** Explicit hints reorient attention in the matchstick problem (n = 61; hints added 11% more solvers), but the "abrupt" claim rests on simulated data [S27, weak]; Aha and restructuring do not always co-occur (2024 review, abstract only) [S28, medium].
- **Where reframing helps:** abstraction before solving (step-back), +7% to +27% on STEM and QA; verifiable tasks. [S29, medium]

### 2.5 Focus versus breadth in LLM agents
- Irrelevant context hurts [S30, strong]; length alone costs 13.9-85% even with masked distractors [S31, medium]; 18 models do better on a ~300-token focused prompt than on ~113k tokens [S32, medium]; regenerating context to its relevant part helps [S33, medium]; masking old observations matches LLM summarisation at about half the raw cost [S34, medium].
- Parallel sub-agents with separate contexts beat one agent by 90.2% on an internal eval at ~15x tokens, but vague briefs caused duplicated searches and shared-context work fits badly [S35, weak].

## 3. Reading of the evidence

- Evidence-driven allocation is now the default design, but its isolated value shows only where a matched uniform arm exists (SEC, AIM's one task), and there it is mixed. Run it as an arm.
- Leverage must be measured; the one agent that does (MLE-STAR) has no isolating ablation.
- Reframing works when an outside failure signal triggers it and the frame is built from evidence; free-form LLM reframing and self-reflection show nothing, and frequent switching hurts. Rate-limit it.
- No idea below adds instruction wording (synthesis C9): they change inputs, schedule and triggers.

## 4. Improvement ideas for this part

Effects are predictions; no real tree-run exists yet (the two real runs predate the tree). Test each as an arm against uniform, plain and climb at matched tokens.

1. **Rotate the round-robin (have, defective).** In `tree.split_select`, start each pass from the part with the fewest builds so far (counts carried across directions and rounds, seeded shuffle on ties), for the build lane and the interrogation pick; log per-part allocation in `decisions`. Effect (simulated): every part gets a main-lane build in round 1 and about 1.4 over two rounds, against 0 for three parts today; removes the part = map-position confound. Cost: ~15 lines. Measure: the simulation as a unit test; parts with zero builds per run = 0.
2. **Balanced, logged schedule (partial).** Replace `IDEA_CARDS[len(specs) % 5]` with a seeded assignment: each card at most once per part per round, equal across parts; draw the lens from a seeded permutation, not `replicate % 5`; write (part, direction, card, lens, family, seed) per context to `schedule.json`. Effect: none directly; per-card, per-part and per-lens yields become separable and ideas 3-5 can be replayed offline. Cost: ~40 lines. Measure: balance table; after 6 runs, share of new-cluster variance by part, card, lens.
3. **Close the discovery loop per cell (partial).** After each round compute new clusters per context for each (part, direction) with `novelty.Index` against earlier clusters and ledger texts. Cells under a floor lose their extra context; freed contexts go to the best cells and to idea 6; a retired card is replaced by that cell's best card, not `formal`; wire the docstring's rule (round yield under 0.5 skips next-round ideation); keep a 20% random floor; let `inward_share` follow measured yield after 3 runs. Evidence S1, S7, S8. Effect: fewer redundant sketches per token; risk: lock-in on early noise. Cost: ~60 lines. Measure: new clusters and checked builds per 100k tokens vs a fixed schedule.
4. **Leverage table from the baseline (new).** Once per baseline version, cached with the baseline profile (`refresh_profile`): build +/-25% variants of each part's main knob with the `controls.py` string-edit machinery (n_layer, n_head, d_ff, lr, seq_len), run 45 steps as measurement only, record loss change per +10% step time; map diagnostic cells to parts (position and frequency loss to io, data, objective; entropy and max logit to mix; gradient and update spread to opt, depth). Use: +1-2 contexts and a build-slot weight for the top two parts (floor 1, cap 35%), the diagnosis card sliced per part, a planner instruction to split high-leverage parts. Effect: more looks where marginal capacity buys most; sensitivity is not improvability, so idea 3 corrects it. Cost: ~15 short runs once. Measure: Spearman of leverage vs best learn_z per part over 3+ runs; drop if <= 0.
5. **Anomaly cards from prediction misses, with a noise floor (partial).** For each checked build, z = (measured - predicted gap) / SD from `predict.py`. A part is surprising if over 30% of its builds have |z| > 2, and shows progress if its mean |z| falls between rounds. Round 2 adds an anomaly context for the two most surprising parts (sketch, prediction, outcome: "which assumption did this break; five sketches that explain or exploit it"); a part surprising without progress is marked noisy and gets none (S9, S13). Effect: repairs the part model where it fails. Cost: 2-4 contexts. Measure: anomaly vs `formal` contexts in one part: new-cluster share, checked rate.
6. **Scripted, rate-limited reframe at cell level (partial).** A cell is stuck when 60% or more of its sketches sit in 2 clusters or fewer, or 3 builds failed at one rung for one reason, or its yield is under the floor two rounds running. Its next context is a scripted reframe: a second lens chosen by failure type (learning failures: dynamics; time failures: bottlenecks; repeated family: dataflow), the failure reasons and pre-mortem objections as the hint, the failing assumption pre-negated as an OUTWARD instruction. No free-form "reframe this problem" prompt (S21, S23); one reframe per cell per round (S26). Half of stuck cells (random) are reframed, the rest get an extra plain context. Effect: fewer repeated families in round 2. Cost: at most 4 cheap-model calls per round. Measure: reframed vs control cells on new-cluster yield and checked rate.
7. **Lock-in alarm (partial).** After round 1, count round-2 sketches within cosine 0.45 of a round-1 winner. Above 50%, make a quarter of that part's contexts incumbent-blind: winner family names in the exclusion list, no "build on a success" line. Only 25%, because most gains are adapted ports (synthesis C5). Evidence S17. Effect: guards the good-enough trap. Cost: ~30 lines. Measure: blind vs aware contexts: share with a new mechanism, rung-3 pass, best learn_z.
8. **Test the upward reframings (new).** Parse each upward proposal's "new success measure" into a metric the harness can compute (rare-token, late-position, recall-token loss; `diagnose.py` has the buckets) and score all checked candidates. A reframing earns a part or lens in round 2 only if it reorders them (Kendall tau under 0.6 against validation loss) or shows the baseline far from its best slice. Effect: turns a dead log into a tested frame. Cost: small. Measure: share passing; yield of spawned vs default parts.
9. **Scoped-context arm (new, low prior).** A part's contexts see only the symbols in its `boundary`, the constraints, its diagnostic cells and its history rows; `recipe` keeps the full script. Evidence S30-S35; counter: train.py is ~5k tokens and scoped memory showed no isolated effect (S6). Cost: small (`_symbol_text` exists). Measure: share of sketches whose TARGET cell belongs to the part; new-cluster yield; cross-part merge rate.

Order: 1 and 2 first (hours, before any real tree run); then 3, 5, 6, 7 as arms; 4 when the card is free; 8-9 last. Brief 03 #8's (part, card) bandit and brief 11 M8's stage allocation become testable once 2 has logged propensities and the ledger holds ~100 builds.

## 5. Gaps

Springer and Nature pages returned authentication redirects (S15, S16, S28 are snippet or abstract level). Not retrievable: a framing-effect replication (Many Labs 2), Dunbar on unexpected results in science, Chi, Feltovich and Glaser on expert problem representation. One stray PubMed query after the quota returned nothing.

## Sources

- S1 AIM. https://arxiv.org/html/2609.38445 (weak)
- S2 Recursive self-improvement of AI research agents. https://arxiv.org/html/2609.26457v1 (weak)
- S3 DeepScientist. https://arxiv.org/html/2509.26603v1 (weak)
- S4 AB-MCTS. https://arxiv.org/html/2503.04412v5 (medium-weak)
- S5 MLE-STAR. https://arxiv.org/html/2506.15692v3 (weak for the step)
- S6 AIRA-dojo. https://arxiv.org/html/2507.02554v2 (medium)
- S7 Self-Evolving Curriculum. https://arxiv.org/html/2505.14970v4 (medium)
- S8 DAPO. https://arxiv.org/html/2503.14476 (medium)
- S9 MAGELLAN. https://arxiv.org/abs/2502.07709 (weak-medium)
- S10 OMNI-EPIC. https://arxiv.org/abs/2405.15568 (weak)
- S11 Intelligent Go-Explore. https://arxiv.org/abs/2405.15143 (medium-weak)
- S12 Active inference as context acquisition. https://arxiv.org/abs/2608.19202 (weak)
- S13 Burda et al., large-scale curiosity. https://pathak22.github.io/large-scale-curiosity/ (medium)
- S14 Kidd et al. 2012, Goldilocks effect. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036399 (weak-medium)
- S15 Eye tracking in problem solving, scoping review 2023. https://link.springer.com/article/10.1186/s40461-023-00140-2 (medium; snippet)
- S16 Eye tracking in science education, review 2025. https://link.springer.com/article/10.1007/s11191-025-00644-1 (medium; snippet)
- S17 Sheridan and Reingold 2013, Einstellung in chess. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0075796 (weak-medium)
- S18 Meadows, leverage points. https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/ (weak)
- S19 Theory of constraints (cites Gupta and Snyder 2009). https://en.wikipedia.org/wiki/Theory_of_constraints (weak)
- S20 Thought Anchors. https://arxiv.org/abs/2506.19143 (medium)
- S21 Shin et al., CHI 2025, LLMs in problem reframing. https://arxiv.org/html/2503.01631 (medium)
- S22 Sclar et al., prompt formatting. https://arxiv.org/abs/2310.11324 (strong)
- S23 Huang et al., no intrinsic self-correction. https://arxiv.org/abs/2310.01798 (strong)
- S24 Liu et al., R1-Zero critical perspective. https://arxiv.org/html/2503.20783v2 (medium)
- S25 Metacognitive bottleneck, riddles. https://arxiv.org/abs/2509.14704 (medium)
- S26 Underthinking of o1-like LLMs. https://arxiv.org/html/2501.18585v2 (medium)
- S27 Tracing cognitive processes in insight problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219327/ (weak)
- S28 Wiley and Danek 2024, restructuring and Aha (abstract only). https://doi.org/10.1038/s44159-023-00257-x (medium)
- S29 Step-back prompting. https://arxiv.org/abs/2310.06117 (medium)
- S30 Shi et al., irrelevant context. https://arxiv.org/abs/2302.00093 (strong)
- S31 Du et al., context length alone hurts. https://arxiv.org/abs/2510.05381 (medium)
- S32 Chroma, context rot. https://www.trychroma.com/research/context-rot (medium)
- S33 System 2 Attention. https://arxiv.org/abs/2311.11829 (medium)
- S34 The Complexity Trap. https://arxiv.org/abs/2508.21433 (medium)
- S35 Anthropic, multi-agent research system. https://www.anthropic.com/engineering/built-multi-agent-research-system (weak)
- S36 Dorst, Frame Innovation (not fetched). https://direct.mit.edu/books/book/2239/Frame-InnovationCreate-New-Thinking-by-Design (weak)
