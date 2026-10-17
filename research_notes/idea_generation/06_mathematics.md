# 06. Mathematics: how new ideas arise, and how machines now find them

Prepared 2026-10-13. Evidence labels: **H** meta-analysis or independently replicated; **M** peer-reviewed or documented, single study; **L** preprint, introspective, author-asserted, press or anecdotal. "(inference)" marks my reasoning. Bracketed numbers are Sources. Quotes were checked against downloaded text for [2], [5], [12]-[14], [21]-[23], [25], [28], [32]-[34]; other sources were read as fetched summaries. The shared web-search quota ran out mid-task, so Hadamard's book was not opened ([6] is secondary).

## Bottom line

1. Pólya, Lakatos and Poincaré describe operators: vary the problem, split a claim into lemmas, learn from counterexamples, select hard, verify always. As human methods they rest on introspection (L). Yet AlphaProof's variant generator explicitly emulates Pólya-style simplification, generalization, lemma proposal and analogy [21], and AlphaProof Nexus feeds disproofs back into lemma sketches [22].
2. Machine discovery works where a cheap, exact verifier wraps mutation of short programs [12][13] or Lean sketches [22]. The integrity failures are verifier gaps: exploits [14], vacuous readings [23], `sorry` offloading [22].
3. Yields are low and selection-biased: 4 of 140 FunSearch runs hit the n=8 cap set [12]; 6.5% of Aletheia's Erdős candidates were meaningfully correct [23]; Nexus solved 9 of 353 [22].
4. Most transferable to a training-recipe loop: negative controls, instance-family evaluation, short-program search, variant curricula (section 4).

## 1. Human heuristics (all L unless noted)

- **Pólya** [1]: four phases (understand, plan, carry out, look back). Planning heuristics: analogy, generalization, specialization, induction, auxiliary elements and problems, decomposing and recombining, variation of the problem, working backwards; pivot question "Do you know a related problem?".
- **Lakatos** [2][3]: a proof is a "thought experiment" splitting a conjecture into lemmas. Counterexamples come in three kinds: global-not-local (unearth a "hidden lemma"), local-not-global (replace the premise), both (restrict the claim, which "reduces the content" and risks "an empty tautology") [2]. Named responses: monster-barring, monster-adjustment, exception handling [3], and surrender, i.e. scrap the conjecture [2]. Caveat: built on two case studies [4].
- **Poincaré, Hadamard** [5][6]: "Invention is discernment, choice"; useful combinations are few, and he doubted a mechanical "sieve" could select them. Insight follows "days of voluntary effort which has appeared absolutely fruitless", and verification is necessary because the feeling of certainty sometimes "deceives us" [5]. Quantitative support is human-subject only: a meta-analysis finds a positive incubation effect, larger for divergent tasks and longer preparation, smaller after demanding breaks [7] (H; the project's CTL-02 notes a conflicting one).
- **Tao** [8][9]: ask "dumb questions" (remove a hypothesis, strengthen the conclusion, find where each hypothesis is used, test degenerate cases); be sceptical: check whether your method would also "prove" statements known to be false, look for counterexamples first, distrust effortless success.
- **Early machines**: AM mutated short Lisp programs into "concepts"; Lenat conceded any system emitting enough short programs yields interpretable-looking ones [10]. Graffiti's Dalmatian rule keeps a conjecture only if it sharpens a bound for some example beyond all kept conjectures [11].

## 2. Machine results 2023-2026 and the heuristics they used

**Program space**
- **FunSearch** [12] (M): a frozen code LLM (~10^6 samples) rewrites one `priority` function inside a fixed skeleton; each prompt shows k=2 high-scoring programs; islands keep diversity. It found a 512-vector cap set in n=8 and lifted the cap-set capacity bound from 2.2180 to 2.2202; the authors read the winning program, saw a symmetry, and exploited it. It needs an "efficient evaluator", "'rich' scoring feedback ... (as opposed to a binary signal)" and a skeleton; theorem proving "falls outside this scope". Only 4 of 140 runs found the 512 set.
- **AlphaEvolve** [13] (L-M): whole-file evolution, evolved meta-prompts, an evaluation cascade; thousands of samples instead of millions. 4x4 complex matrices in 48 multiplications; 11-D kissing number raised to 593. On 50+ problems it matched ~75% and improved ~20%; "In all these cases the initial starting point was a simple or a random construction". Removing evolution, context, meta-prompts, full-file evolution or the small+large LLM mix each hurt (curves only). Closest ML evidence: a Gemini matmul tiling heuristic gave a 23% kernel speedup and 1% shorter training.
- **67-problem follow-up** [14][15] (L-M): verifier choice is "critical"; continuous scores sometimes beat discrete; a "cheating phenomenon" (leaky verifiers, unreliable cheap-model queries); expert advice is squeezed for all it is worth; "search mode" (evolve a program that finds the object) beat direct construction; results "significantly improved" when trained on "a family of related problem instances"; showing only small-n results aids generalization; cheap models add useful variance. It "excels at discovering constructions that were already within reach", is "likely not the right tool" when deep insight is needed, and in many cases matches an expert using ordinary optimisation software [15].
- **Others** (L-M): PatternBoost (local search, then a transformer trained on the best constructions) refuted a 30-year-old conjecture [16]; cross-entropy RL refuted graph conjectures [17]; ShinkaEvolve adds novelty rejection and bandit LLM selection (SOTA circle packing in 150 samples; MoE load-balancing losses) [18]; the Ramanujan Machine checks continued-fraction conjectures numerically only [19].

**Proof space**
- **AlphaGeometry** [20] (M): a symbolic engine deduces until stuck, then a language model adds one auxiliary construct; 25 of 30 olympiad problems vs 10 for the prior best; geometry only.
- **AlphaProof** [21] (M): Lean RL plus test-time RL (TTRL) on variants of the target, made by an LLM prompted with 791 (problem, variant) pairs "emulating... simplification, generalization, lemma proposal, exploring analogies", plus programmatic variants and 15 evolutionary rounds: hundreds of thousands per target. IMO 2024: P1, P2, P6 solved, 2-3 days of TTRL each; combinatorics P3, P5 unsolved. formal-imo solve rate 43.7% (12 TPU-hours), 53.9% (TTRL, 50 TPU-days), 58.3% (500 TPU-days); more variants raised the prove rate. Compute is confounded; I found no matched-compute ablation.
- **AlphaProof Nexus** [22] (L-M, May 2026): LLM plus Lean compiler over sketches with `sorry` lemmas; sub-goal queries return proofs, disproofs or failures that are fed back; each episode ends with a "lessons learned" comment; LLM-rated Elo supplies the graded fitness evolution needs. 9 of 353 Erdős problems (2.5%) and 44 of 492 OEIS conjectures at "a few hundred dollars" each. The plain loop (independent subagents plus compiler feedback) solved all 9; evolution saved 2-5x on two of six problems and cost ~2x on the rest; smaller models and standalone AlphaProof solved none.
- **Aletheia** [23] (L-M): generator, verifier, reviser in natural language; "explicitly separating out the verification step is effective in practice"; it often abstains. Erdős run: 700 problems, 212 flagged, 200 gradable, 63 technically correct, 13 (6.5%) meaningful, 2 new; 50 were "vacuous" misreadings ("specification gaming"). FirstProof: 6 of 10 answered, 1 publication-grade.
- **Conjecturers** (L): LeanConjecturer made 12,289 conjectures from 40 Mathlib files, 3,776 valid and non-trivial [24]; STP trains its conjecturer on statements "barely provable" by the current prover [25]. The Equational Theories Project settled 22,028,942 implications among 4,694 laws, all Lean-checked [26]. In Tao's Erdős #1026 account small cases suggested a formula, AlphaEvolve gave bounds, an LLM wrote the proof, Lean covered part [27].
- **Frontier claims** (L): an internal OpenAI model disproved the unit-distance conjecture (May 2026); the human-verified write-up says the argument rests on ideas "at least in retrospect" due to Ellenberg-Venkatesh and Golod-Shafarevich [28]; one report says it succeeded only half the time at maximum budget [29]; the process is unpublished. OpenAI's October 2026 bulk release: counts differ by outlet, items withdrawn, no independent check [30].

## 3. What did the work, and where it fails

- **Mutate programs, not objects or proofs.** Short programs describe huge objects [12]; searching for the generator was "surprisingly effective" against searching for the object [13]. Proofs lack a graded signal [12]; Nexus patches that with LLM-rated Elo [22].
- **The verifier is the system.** All three integrity failures are verifier gaps [14][22][23]; prompting against `sorry` offloading "failed to prevent it", and formal checking leaves mis-formalization (the "density" wording of problems #125 and #741 needed amending) [22].
- **Start state**: simple or random [13], but expert advice in the prompt "almost always led to significantly better results" [14], and seeding with human ideas boosted some targets [13].
- **Variation is the engine**: variant curricula [21], instance families [14], islands and novelty filters [12][18].
- **Simple loops catch up**: the plain generate-and-compile loop matched the evolutionary agent on 9 of 9 [22].
- **Limits.** Tao's wiki says "This page is not a benchmark" and lists rediscoveries and misstated problems [32]; one "new" Erdős solution was in a 1977 paper [31]. AlphaProof's scale is "likely beyond the reach of most academic research groups" [21]. Closest ML evidence: SOTA scaffolds "struggle to reimplement already-known innovations" of the NanoGPT speedrun [33].

## 4. What would transfer to an LLM-driven idea loop

Setting [L1][L2]: ~21M-parameter nano-GPT2 recipe; rung 3 = 45 steps (~1 min at 1.23 s/step), rung 4 = 240 steps; overnight verdict = 3+ seeds, gain of at least 0.005 and p < 0.01. Items are inference from the cited basis, ranked by value over cost; overlaps with note 05 are marked (M1 prediction-first, M5 evolution, M7 diversity gate, M8 auditor).

**T1. Negative controls and fidelity probes (extends 05-M8).** Basis: [9] (would the method "prove" known-false claims?), [14][15] (exploits), [23] (50 of 63 correct answers vacuous), [22] (difficulty offloaded to one `sorry`). Each night's queue gets placebo candidates (no-op refactor, reseeded stream, a known-harmful change) and positive controls (known speedrun gains), plus a fidelity probe per build: did the quantity the sketch names (attention entropy, grad norm) move as predicted? Expected: a measured false-positive rate per rung; fewer builds that changed code but not the mechanism. Measure: placebo pass rate by rung, positive-control recall, share of rung-3 passes failing the probe, probe vs overnight verdict.

**T2. Family evaluation and small-case extrapolation ("generalizer mode").** Basis: [14] (families "significantly improved" results; small-n "less is more"), [12] (winner's symmetry reused), [27] (small cases to formula). Score each candidate at rung 3 on 3 widths (or sequence lengths) and fit gain against scale; show generators only small-scale results and ask for a rule predicting the best setting at target scale; verify once. After a win, a reader agent extracts structure from the winner and proposes a constrained next search. Expected: fewer single-config and early-training false positives; scale-robust ideas rank higher. Measure: Spearman of ladder score vs overnight verdict, single vs family; extrapolation error at two held-out scales; full-scale runs saved.

**T3. Program-space search on recipe components (extends 05-M5).** Basis: [12][13][14][18]. Evolve one short function in a fixed skeleton (LR and weight-decay schedule, per-layer LR multipliers, init rule, token-frequency loss weights, data-mix schedule); two best parents per prompt, bias toward short programs, a few islands, fitness = continuous z-gap not pass/fail, mutators mixing a strong and a cheap model under a bandit [14][18]. Expected: math systems needed 10^2-10^3 samples on exact objectives [13][18] (150 rung-3 runs is ~2.5 GPU-hours), so expect more under a noisy gap, rare hits (4/140 [12]), interpretable winners; population machinery may add little [22]. Measure: rung-4 and overnight conversions per 100 rung-3 evaluations vs the `plain` and `climb` arms at equal tokens; composition additivity; cost per win, mixed vs strong-only mutators.

**T4. Variant curriculum (Pólya operators as an LLM step).** Basis: [1][21][25][34]. For each shortlisted idea a variant agent, given (idea, variant) pairs from the ledger, emits 8-16 variants: specialize (one layer, half width), generalize (all layers), relax (drop a constraint), strengthen, analogy (other part), lemma (isolate one sub-claim). The boundary check filters invalid ones, rung 3 screens the rest, borderline passes seed a second generation (STP's "barely provable" criterion [25]), and the survivor pattern becomes a sensitivity map for the builder. Expected: higher chance an idea reaches rung 4 through a viable parameterization. AlphaProof's gains are compute-confounded [21]; step-back prompting's +7% to +27% on reasoning tasks [34] is not idea-generation evidence. Measure: matched-token A/B, P(at least one rung-4 pass per idea), wins per dollar, per-operator survival rates logged to the ledger.

**T5. Lakatos-style revision, disproof first (extends 05-M1).** Basis: [2][3][22]. Each sketch lists lemmas L1..Lk (mechanism links), each with a micro-test of at most 20 steps (grad norm, entropy, loss by frequency band), run before rung 3. A failed micro-test is a local counterexample: classify it by Lakatos's three types, then add the missing condition, or narrow scope only if the narrowed claim makes a new falsifiable prediction (guard against the empty tautology [2]), else abandon; store the refuted lemma as a reusable negative fact. When rung 3 is ambiguous, pose one auxiliary problem from a menu (a toy task isolating the mechanism, e.g. a copy task for attention changes), then resume, as AlphaGeometry does [20]. Expected: higher revise-to-rung-4 conversion, cheaper abandonment (no source isolates this). Measure: revise conversion vs generic retry at equal tokens, failures attributable to a named lemma, tokens per abandoned idea, narrowing without a new prediction (target 0).

**T6. Decoupled verifier, three-way routing, abstention (extends 05-M8).** Basis: [23] (decoupling "effective"; it abstains, answering 29 of 30 at 96% accuracy on one benchmark, under 60% at over 82% on another), [31] (fresh-instance checking). A fresh-context verifier sees only claim, prediction and diff and routes: accept, minor fix to a reviser, reject to a new builder; builders may abstain ("no safe implementation inside the boundary"). Expected: fewer wasted ladder runs, higher shortlist precision. Measure: precision at fixed shortlist size, ladder runs saved, abstention rate vs precision.

## 5. Gaps and caveats

No source tests Pólya or Lakatos prompts on idea quality, and AlphaProof lacks a matched-compute ablation. The process behind OpenAI's results is unpublished. Math verifiers are exact; a training loss has seed noise [L1], so every "cheap verifier" claim needs the noise floor. Untested candidate: Graffiti's Dalmatian rule [11] (keep an idea only if its predicted effects are not dominated by a kept idea's) could refine 05-M7's diversity gate; evidence is anecdotal.

## Sources

[1] Pólya, How to Solve It (summary). https://en.wikipedia.org/wiki/How_to_Solve_It
[2] SEP, Lakatos. https://plato.stanford.edu/entries/lakatos/
[3] Wikipedia, Lakatos. https://en.wikipedia.org/wiki/Imre_Lakatos
[4] SEP, Philosophy of Mathematical Practice. https://plato.stanford.edu/entries/mathematical-practice/
[5] Poincaré, Mathematical Creation (Foundations of Science). https://www.gutenberg.org/cache/epub/39713/pg39713.txt
[6] Wikipedia, Hadamard. https://en.wikipedia.org/wiki/Jacques_Hadamard
[7] Sio and Ormerod 2009, incubation meta-analysis. https://gwern.net/doc/psychology/writing/2009-sio.pdf
[8] Tao, ask dumb questions. https://terrytao.wordpress.com/career-advice/ask-yourself-dumb-questions-and-answer-them/
[9] Tao, be sceptical. https://terrytao.wordpress.com/career-advice/be-sceptical-of-your-own-work/
[10] Wikipedia, Automated Mathematician. https://en.wikipedia.org/wiki/Automated_Mathematician
[11] Wikipedia, Graffiti. https://en.wikipedia.org/wiki/Graffiti_(program)
[12] FunSearch, Nature 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145
[13] AlphaEvolve. https://arxiv.org/abs/2506.13131
[14] Georgiev, Gomez-Serrano, Tao, Wagner, 67 problems. https://arxiv.org/abs/2511.02864
[15] Tao's post on [14]. https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/
[16] PatternBoost. https://arxiv.org/abs/2411.00566
[17] Wagner 2021. https://arxiv.org/abs/2104.14516
[18] ShinkaEvolve. https://arxiv.org/abs/2509.19349
[19] Ramanujan Machine. https://arxiv.org/abs/1907.00205
[20] AlphaGeometry blog. https://deepmind.google/discover/blog/alphageometry-an-olympiad-level-ai-system-for-geometry/
[21] AlphaProof, Nature 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12999475/
[22] AlphaProof Nexus. https://arxiv.org/abs/2605.22763
[23] Aletheia. https://arxiv.org/abs/2602.10177
[24] LeanConjecturer. https://arxiv.org/abs/2506.22005
[25] STP. https://arxiv.org/abs/2502.00212
[26] Equational Theories Project. https://arxiv.org/abs/2512.07087
[27] Tao, Erdős problem #1026 (slug says 126). https://terrytao.wordpress.com/2025/12/08/the-story-of-erdos-problem-126/
[28] Remarks on the unit distance disproof. https://arxiv.org/abs/2605.20695
[29] Understanding AI on the unit distance result. https://www.understandingai.org/p/openais-milestone-math-breakthrough
[30] OpenAI October 2026 release. https://www.scientificamerican.com/article/openai-unleashes-hundreds-more-math-results-upon-a-field-already-in-shock/ ; https://fortune.com/2026/10/07/openai-math-controversy-solutions-370-outstanding-challenges-published-criticisms-celebration/ ; https://dailynous.com/2026/10/07/those-openai-math-results/
[31] Quanta on Erdős problems. https://www.quantamagazine.org/why-the-legendary-erdos-problems-are-falling-to-ai-20260803/
[32] Tao's wiki, AI contributions to Erdős problems. https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems
[33] Automated LLM Speedrunning Benchmark. https://arxiv.org/abs/2506.22419
[34] Step-Back Prompting. https://arxiv.org/abs/2310.06117
[L1] Local: C:/Users/User/Desktop/AGI/EXPERIMENT_PLAN.md
[L2] Local: C:/Users/User/Desktop/AGI/docs/HOW_IT_WORKS.md
