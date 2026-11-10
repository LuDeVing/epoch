# Neural and LLM proof search: deep document

*Subfield C06.05. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K29), critique.md in this folder. Evidence ids (a01 ... d19) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

A neural prover splits proof work into two jobs. A language model **proposes** the next step (a tactic, a lemma, a whole proof, a sketch). Plain code **disposes**: it keeps the queue of open goals, ranks them, calls the model again, backtracks, and asks an exact checker (Metamath kernel, Lean, Isabelle) whether the proof is valid. The checker is the only judge of truth.

This is the closest published match to our S3 (generate) plus S4 (test) loop. The model never decides what happens next. Code does. The checker gives a hard pass or fail with an error message.

Four design questions run through the whole literature:

1. **Granularity.** One tactic at a time (GPT-f, HTPS, BFS-Prover), whole proofs (DeepSeek-Prover, Goedel), or lemma sketches with gaps (DSP, Hilbert, Seed-Prover).
2. **Who orders the search.** Model log-probability, a learned value head, an exploration bonus (RMaxTS), or nothing (independent samples).
3. **What flows back from the checker.** Nothing, an error message, the verified prefix, or proved lemmas kept in a library.
4. **Training or frozen.** Most strong results train the model on checker-verified data (expert iteration, RL). A smaller set of results uses frozen models inside a code loop (COPRA, LEGO-Prover, DSP+, Hilbert). Our agent is frozen, so the second set matters most.

A fifth thread, from 2025, is informal proof search where no exact checker exists (Huang and Yang). There the verifier is itself an LLM, and 2025-26 studies show it is too lenient (section 5, K25).

Scope boundary. Interactive theorem proving (human-guided proof assistants), premise selection, lemma conjecturing, proof repair and planning are separate subfields in this run. This document only notes links.

## 2. History and theories in depth

### 2.1 2020 to 2022: the transformer prover appears

**GPT-f (Polu and Sutskever 2020, a01-a03, b01, c01).** A decoder-only transformer pretrained on web math, arXiv and GitHub proposes Metamath tactics. Best-first search keeps a queue of goals ordered by cumulative log-probability of the tactics that led to them. The model is called on the top goal, e=32 tactics per goal, a=32 attempts, depth d=256. A Metamath kernel checks every proof. It closed 56.22% of held-out set.mm theorems against 21.16% for the prior best (MetaGen-IL). It found 23 proofs shorter than the human ones, and the Metamath community accepted them. Size helped then saturated: 160M 34.79%, 400M 39.94%, 700M 42.56%, 1.5B 42.39% on validation. Pretraining on math text beat GitHub-only. A learned value reranker added about 4 points (see critique: 47.21% vs 43.15% at iteration 2, not 42.56%). The attempts curve (Table 12) and Table 9 use different search settings; one value (42.90% at a=2) sits below 47.21% for the same model. This is unresolved.

**PACT (Han et al. 2021, a04).** Extra self-supervised tasks mined from Lean kernel proof terms, trained together with tactic prediction. Held-out mathlib pass rate 32% (tactic only) to 48.4% (co-training). A pretrain-then-finetune model with the same data reached only 33.6%. On future mathlib files (temporal split) the best model got 37.1% against 21.8% for a tidy-bfs baseline.

**Curriculum learning (Polu et al. 2022, a05, a06, a21).** Expert iteration: run search, keep the verified proofs, retrain, repeat. mathlib-valid pass@1 rose from 56.3% to 62.6% over 9 iterations. On synthetic inequalities the loop solved 6 problems at difficulty 6 with no seed proofs, while a sampling-only loop solved 0. miniF2F: 47.3% valid, 36.6% test (previous best about 29.3%). At fixed compute a 774M model with many samples beat larger models. Two IMO-adapted solves were weakened versions of the originals (appendix F).

**HyperTree Proof Search (Lample et al. 2022, a07, b02, b03).** AlphaZero-style search over a hypergraph, since one tactic can create several subgoals that must all be solved (AND-OR structure). Policy and value live in one transformer, trained online from its own search. Metamath: supervised model 65.4% valid and 61.2% test vs GPT-f 56.5% and 56.2%; online training lifted test pass@32 from 55.8% to 65.6% and valid cumulative to 82.6%. miniF2F-test 41.0% pass@64 vs 36.6% for GPT-f. The 82.6% includes training on valid statements.

**Thor (Jiang et al. 2022, a08, a22, b05, d11).** The model emits a hammer token to say "call the symbolic prover here". Sledgehammer then picks premises and closes the goal. PISA: model alone 39.0%, Sledgehammer alone 25.7%, union of the two 48.8%, Thor 57.0%. 8.2% of problems fell to the mix only. Model steps that included premises advanced a proof 1.9% of the time, versus 28.2% without premises (observational). Preprocessing cost 7,400 CPU hours per year of AFP. Variants: model also learns premise picking 55.4%, no proof context 53.6%, temperature 1.0 55.7%.

**Draft, Sketch, Prove (Jiang et al. 2022, a09, b06, b25).** An informal proof is turned into a formal sketch with gaps. Automated provers fill each gap. Isabelle miniF2F-test: Sledgehammer 10.4%, plus heuristics 20.9%, Thor 29.9%, DSP 39.3% (human informal proofs) and 38.9% (model-written ones, Minerva 540B). Ablations on valid: no automated provers 32.8% (-9.8), no informal proofs 38.9% (-3.7), no comments 37.7% (-4.9). The "doubling" is relative to Sledgehammer plus heuristics (20.9%).

### 2.2 2023 to 2024: frozen LLMs and whole-proof generation

**LeanDojo and ReProver (Yang et al. 2023, a10, a23, b04, b22).** Open Lean toolkit, a retrieval-augmented tactic generator, and a new split. Random split pass@1: ReProver 51.2, without retrieval 47.6, GPT-4 29.0, tidy 23.8. On novel_premises (every test proof uses a premise unseen in training): 26.3, 23.2, 7.4, 5.3. Random splits overstate by about 2x. Their wrapper cut false proof-check errors from 21.1% to 1.4%. miniF2F-test 26.5%, ProofNet 13.8%.

**COPRA (Thakur et al. 2024, a11, a25, b07, b20).** No fine-tuning. GPT-4 proposes one tactic at a time inside a program-controlled backtracking search. Checker errors, search history and retrieved lemmas go back into the prompt. miniF2F-test Table 1: few-shot GPT-4 13.52%; 60 samples at T=0.7 15.98%; COPRA without backtracking 24.59%; COPRA 26.63%; plus retrieval 29.09%; plus informal proof 29.92%; 100 queries 30.74%. GPT-3.5 9.02% and CodeLlama 5.73% gained little. This is the only formal-prover paper before 2025 that tests a training-free scaffold against a sampler (and the sampler is weak).

**Baldur (First et al. 2023, c15, c21).** Whole-proof generation with LLM repair. 47.9% whole-proof vs 39.0% for a stepwise search baseline; 65.7% combined with Thor.

**LEGO-Prover (Wang et al. 2023, b11, d05).** Frozen GPT-3.5. Informal proof to lemma-style sketch, prover fills gaps, verified lemmas go into a growing skill library. Isabelle miniF2F 57.0% valid / 50.0% test at 100 attempts vs Thor 42.6 / 39.3. Library ablation at 50 attempts: 50.4% with vs 47.1% without (+3.3, about 8 problems). 24% of valid proofs used retrieved skills.

**DeepSeek-Prover V1 and V1.5 (a12, a13, a24, b08, b09, b24).** About 8M autoformalised statements with proofs, expert iteration, whole-proof generation. V1.5 adds RL on Lean feedback (GRPO) and RMaxTS: truncate a failed proof at the first error, keep the valid prefix as a tree node, resume generation from that tactic state, and add an intrinsic reward for reaching new states. miniF2F-test: V1 50.0%, V1.5-RL 51.6% at 128 samples, 60.2% single pass at 32x6400 samples, 62.7% with RMaxTS (63.5% best mix). ProofNet 22.6% to 25.3% with search. Plain UCT without the intrinsic reward fell to non-search level.

### 2.3 2025 to 2026: scale, decomposition, and the "does search matter" question

- **BFS-Prover (b10, d12).** Best-first search with length-normalised model log-probability, no critic, no MCTS. miniF2F-test 70.83% (pass 2048 x 2 x 600), 72.95% accumulative. SFT+DPO 64.98% at pass@64 to 70.83% at pass@2048.
- **Goedel-Prover V1/V2 (a15, a26, b14, b15).** Pure whole-proof sampling plus expert iteration: 57.6% vs 50.0% at pass@32. V2 adds self-correction on Lean errors: 88.1 to 90.4% on miniF2F, PutnamBench 44 to 86 solved at pass@184, but with 40k vs 30k tokens.
- **Kimina-Prover (a16, b13, b26).** RL on long think blocks mixing informal reasoning and Lean snippets, no tree search. 52.94% pass@1, 68.85% pass@32, 80.7% pass@8192. In the same table Gemini 37.70% and o3 24.59%.
- **DeepSeek-Prover-V2 (a14, b16, d04).** DeepSeek-V3 writes a lemma sketch with sorry gaps, a 7B prover fills each. 88.9% miniF2F at pass@8192, 47 of 658 PutnamBench.
- **AlphaProof (Hubert et al. 2025, a17, a18, a27).** AlphaZero with AND-OR proof trees. About 80M auto-formalised problems from about 1M informal ones. Each statement is attacked for proof or disproof. Main RL about 80,000 TPU-days. Test-time RL (TTRL) trains on variants of the target. miniF2F-test / formal-imo / PutnamBench: 96.3 / 33.2 / 27.9 at 2 TPU-min; 97.7 / 43.7 / 39.4 at 12 TPU-hours; 97.5 / 53.9 / 45.5 at 50 TPU-days; 99.6 / 58.3 / 56.1 at 500 TPU-days. At IMO 2024 with AlphaGeometry 2: 28/42, 2 to 3 days per solved problem.
- **Seed-Prover (b17, d06).** Three tiers: light (8 to 16 whole-proof refinements on Lean errors), medium, heavy (thousands of conjectures proved or refuted, lemma pool). 99.6% miniF2F, 331/657 PutnamBench, 78.1% of past IMO problems, 5/6 IMO 2025 after the contest (4/6 in the contest).
- **Hilbert (Varambally et al. 2026, d01-d03, d18).** A code-owned loop around off-the-shelf models: informal reasoner, Lean prover, verifier, retriever. If the prover fails, the reasoner splits the goal into subgoals, recursing to depth D, with verifier errors fed back. miniF2F-test 99.2% (Gemini 2.5 Pro + Goedel-V2-32B) vs 74.6% for the prover at pass@4. PutnamBench 462/660 (70.0%) with exhaustive retries; 55.9% with strictly one attempt per problem.
- **DSP+ (Cao et al. 2025, d13, d14).** Training-free Lean 4 rebuild of DSP from off-the-shelf models. miniF2F-test 79.5% at 1024 workflow attempts. Earlier Lean re-implementations reached at most 28% and 31%.
- **Huang and Yang (2025, a19, a28).** Informal search with a frozen LLM, a verifier that writes bug reports, repeat until the verifier passes. 5/6 IMO 2025 problems for each of Gemini 2.5 Pro, Grok-4, GPT-5, vs 31.6/21.4/38.1% for best-of-32. IMC 2025: 94.5% (rank 3) vs base Gemini 57.7% (rank 92).

### 2.4 Theories behind the designs

- **Search as hard exploration (a24).** Reward appears only at a complete proof. Search spreads attempts (RMaxTS bonus) so early partial states are not abandoned.
- **AND-OR structure (a07, a17).** A tactic can create several goals and all must close. A flat retry loop cannot represent this.
- **Policy and value (a02, a07).** A value estimate on partial states prunes the queue. Whether a model-free score does as well is open (section 10).
- **Model proposes, tool disposes (a08).** Symbolic tools do what text models do badly: premise selection, closing small goals. Gain comes from complementarity, not scale.
- **Verified self-generated data (a05, a12, a15).** An exact checker gives a noise-free label, so the model can bootstrap. This does not apply to a frozen agent, except as "keep verified lemmas in context".
- **Plan in language, verify in formal code (a09, a14, d01).** Natural language explores, the checker filters.

## 3. Core findings with exact numbers

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| Model-proposes, code-searches, kernel-checks beats prior non-neural prover | Metamath 56.22% vs 21.16% | GPT-f (a01, c01) | [S] |
| More attempts help with shrinking returns | GPT-f +4.39/+3.97/+2.99/+2.45 per doubling a=4..32; BFS-Prover 64.98% (pass@64) to 70.83% (pass@2048) | a06, c01, b10 | [E] |
| Size saturates; many samples from a smaller model beat fewer from a larger one at fixed compute | 700M 42.56 vs 1.5B 42.39; 774M model in curriculum study | a02, a06 | [S] |
| Value/score over states helps (learned) | GPT-f policy+value 47.21 vs 43.15 (iter 2); HTPS Metamath 65.4% vs 56.5% | a02, a07, b02 | [E] |
| Model-likelihood score with no value head is competitive | BFS-Prover 70.83% (alpha 0.5, width 2) | b10, d12 | [S] |
| Tool handoff | Thor 39.0 to 57.0 on PISA; 8.2% solved by neither part alone; union 48.8 vs interleaved 57.0; DSP no automated provers -9.8 valid / -9.0 test | a08, d11, a09 | [E] |
| Premise text in context hurts a small model | 1.9% vs 28.2% steps advancing (observational) | a22 | [S] |
| Informal draft then formal fill | DSP 20.9 to 39.3 (human) / 38.9 (model); DSP+ 79.5% Lean 4 training-free | a09, b25, d13 | [E] |
| With a strong executor the draft adds little | DSP+ pass@128: none 71.7, GPT-4o 71.7, V3 73.0, QwQ 74.2, R1 75.8; BFS-Prover 74.2 vs common tactics 47.5 | d14 | [S] |
| Scaffold multiplies proposer strength | COPRA GPT-4 26.63 vs GPT-3.5 9.02 vs CodeLlama 5.73; Hilbert Putnam one attempt 55.9 (Pro) vs 13.3 (gpt-oss-120b) | a11, d03, d18 | [E] |
| Backtracking with checker feedback | COPRA 24.59 (no backtracking) to 26.63; 60 plain samples 15.98 | b07 | [S] |
| Retrieval and informal hint ablations are tiny | 29.09, 29.92, 30.74 on 244 items | b07, b21 | [S] |
| Random split overstates 2x | ReProver 51.2 to 26.3; GPT-4 29.0 to 7.4 | a10, a23 | [S] |
| Whole-proof sampling is nearly as good as tree search | DS-Prover-V1.5 60.2% vs 62.7% (RMaxTS) at about 200k samples; 51.6% at 128 samples | a13, b08 | [S] |
| Truncate-and-resume with tactic state | code-only resume without tactic state does worse | b24 | [S] |
| Expert iteration scales | mathlib pass@1 56.3 to 62.6 (9 iters); Goedel 57.6 vs 50.0 pass@32 | a05, a15, a12 | [E] |
| Decomposition into lemmas is the strongest recipe | DS-Prover-V2 88.9% miniF2F; Seed-Prover 99.6% / 331 of 657 Putnam; Hilbert 99.2% / 462 of 660; LEGO-Prover 50.0% test with frozen GPT-3.5 | a14, b17, d01, d05 | [E] |
| Decomposition depth saturates fast | Hilbert D=0 about 75%, D=2 98.36%, D=3 98.7% | d02 | [S] |
| Lemma library helps a frozen model | LEGO 50.4 vs 47.1 valid (+3.3) | d05 | [S] |
| Checker-feedback refinement | Seed light 8-16 refinements about pass@64-256; Goedel-V2 88.1 to 90.4 (40k vs 30k tokens); 2026 controlled study: no feedback beats instruction-only resampling | b15, d06, d07 | [C] |
| Test-time compute keeps paying on hard sets | AlphaProof formal-imo 33.2 / 43.7 / 53.9 / 58.3 | a17, a27 | [S] |
| Informal verify-and-refine loop | 5/6 IMO 2025 (85.7%) vs 21.4 to 38.1% best-of-32; IMC 2025 94.5% vs 57.7% | a19 | [S] |
| LLM proof judges are too lenient | QEDBench false-pass 38.0% to 74.8%; GPT-5 passed 7/48 flawed USAMO proofs; balanced accuracy 77-88%; prompt swing 27 points | d08, d09, d10 | [E] |
| Formal pass is for the statement given, not the intended one | 8 mis-formalised miniF2F statements; 97% auto vs 67% expert-checked autoformalisation; withdrawn Putnam solve | d13, d16, a15 | [E] |
| Benchmarks saturate | miniF2F-test 29.6% (2022) to 99.6% (2025); PutnamBench raw GPT-4 1/640 (2024) to 70% (2025) | c16, d15, b17 | [E] |
| Headline depends on budget | DS-V1.5 51.6% at 128 vs 60.2% at 32x6400; Hilbert Putnam 70.0% exhaustive vs 55.9% one attempt | a13, d03 | [E] |
| Checker-format tuning matters | Kimina 68.85 vs Gemini 37.70 vs o3 24.59 pass@32 (2025 baselines) | a16, b26 | [E] |

## 4. Mechanisms and models

### 4.1 Best-first tactic search (GPT-f, BFS-Prover)

Data structure: a priority queue of nodes. Node = (proof state, list of tactics so far). Score = sum of tactic log-probabilities divided by path length^alpha (BFS-Prover alpha 0.5 default; GPT-f used plain cumulative log-prob). Loop:

1. Pop the best node.
2. Ask the model for e candidate tactics (GPT-f e=32, BFS-Prover width 2).
3. Run each tactic through the checker. Discard errors. Push the new states.
4. If a state has no goals, return the proof.
5. Stop at depth d, node cap, or time cap.

The model sets probabilities. Code sets order and stops. For a frozen general LLM, replace log-probs with a code score (section 7, T5).

### 4.2 AND-OR search (HTPS, AlphaProof)

A node is a goal. A tactic is a hyperedge to a set of child goals. The tactic is solved only if every child is solved. Back-propagate "solved" up AND-edges and "failed" up OR-edges. Selection picks the most promising unsolved leaf by policy prior plus value. Implement with a dictionary from goal id to {status, children sets}. Any multi-lemma plan needs this. A flat list of attempts cannot say that one of three lemmas is still open.

### 4.3 Whole-proof generation with truncate-and-resume (DeepSeek-Prover-V1.5)

1. Sample a whole proof.
2. Run it in Lean. Find the first error. Keep the valid prefix, parse it into tactic nodes, attach to the tree.
3. Resume generation from the last good tactic state. The prompt must include the tactic state. Code-only resume without state does worse (b24).
4. Pick which node to resume from with a non-stationary bandit (discounted UCB) and an intrinsic reward for new states (RMaxTS). Plain UCT without the bonus fell to non-search level (b09).

### 4.4 Model-plus-tool loop (Thor)

State machine: at each step the model either writes a tactic or emits a call-tool token. On call, code runs the symbolic prover with a time cap (Sledgehammer 120 s). Success ends the branch. Failure returns to the model. The learned decision is only "when to call". The always-call-first fixed rule was not tested (d11), so the cheap version is an open test.

### 4.5 Draft, sketch, prove, and recursive decomposition (DSP, DSP+, Hilbert, DeepSeek-Prover-V2)

1. A reasoner writes an informal proof.
2. A sketcher turns it into a skeleton: lemma statements with sorry as proof bodies. Sketch fixes that mattered in DSP+: write the hypotheses explicitly and mask error lines (d14).
3. Code checks that the skeleton compiles with the sorrys in place. Then it attacks each sorry with a prover.
4. Failed subgoals are split again by the reasoner, up to depth D (D=2 gets most of the gain, d02). Verifier errors go back for repair.
5. Stitch the solved pieces and re-check the whole.
6. Retrieval of library facts per subgoal added 1.3 points and cut reasoner tokens 4.0M to 2.3M in one Hilbert case (d02).

Compute is long-tailed. Hilbert: at most 4.5K reasoner calls and 11.3K total calls per sample for miniF2F; hardest problems used 22.8M and 27.0M tokens; median 817 calls vs mean 5352 on Putnam (d03). A per-problem budget cap is needed.

### 4.6 Refinement loop (Seed-Prover light, Goedel-V2, Huang and Yang)

Attempt, check, show error, revise, check, up to n rounds. Two variants differ in what the model sees: the full failed attempt plus the error, or the error only. The 2026 study (d07) suggests showing the failed text causes copying and lowers success; the diagnostic alone is the safer design (abstract only, 11 problems, two models).

### 4.7 Skill library (LEGO-Prover)

Store each verified lemma with its statement and proof. Index by embedding of the statement. For a new problem, retrieve the top-k lemmas and put them in the prompt. Add new verified lemmas back. Gain was +3.3 points on valid at 50 attempts. Skill origins: 10.8% prover, 38.2% evolver solve-requests, 51.1% evolver transformations.

### 4.8 Conjecture and refute (AlphaProof, Seed-Prover heavy)

For "find all" problems, generate many candidate answers with an LLM plus code, let the prover refute wrong ones, prove the survivor (a18). Each statement is attacked for both proof and disproof (a27).

### 4.9 Informal verifier loop (Huang and Yang)

Generate, self-improve, verifier lists critical errors and justification gaps, model fixes, repeat until the verifier passes. No formal guarantee. LLM verifiers misjudge flawed proofs often (section 5).

## 5. What holds up

### 5.1 Replications

- **DSP replicated in Lean 4 without training (DSP+, d13).** 79.5% miniF2F-test, so the draft-sketch-prove pattern is real. It also corrects the story: prior Lean copies of DSP failed because Aesop is weaker than Sledgehammer, and with a strong prover the draft adds only 0 to 4 points (d14).
- **Expert iteration replicates across labs (a05, a12, a15, c11).** Four independent groups.
- **Decomposition replicates across labs, frozen and trained (d01, d04, d05, b17).**
- **AND-OR search** is used in HTPS and AlphaProof independently (a07, a17).
- **LLM judge leniency** replicates across three independent studies (d08, d09, d10).

### 5.2 Failures and refuted claims

- **Random-split numbers do not transfer to unseen premises (a10).** Scores halved.
- **Few-shot whole-proof prompting works poorly for frozen general LLMs in 2023.** GPT-4 13.52% (b07), PutnamBench GPT-4 1/640 (d15). In 2025 general reasoning models were also poor at raw Lean output (Gemini 37.70, o3 24.59, b26).
- **"Refinement beats resampling" is not confirmed.** Seed-Prover's claim has no matched ablation (d06); the 2026 controlled study found no feedback condition beat instruction-only resampling (d07). [C]
- **Earlier DSP ports in Lean were weak (28% and 31% of miniF2F, d13).** Execution tools mattered.
- **Plain UCT without intrinsic reward** is no better than no search (b09).
- **Bigger drafter is not worse.** An earlier note said it was; the critique corrected it: Minerva test scores 35.3 (8B), 37.7 (62B), 38.9 (540B).
- **Bigger model does not always win.** 700M to 1.5B no gain (a02).

### 5.3 Moderators

| Moderator | Effect | Source |
|---|---|---|
| Proposer strength | Same loop, weak vs strong planner: Putnam 13.3 vs 55.9% | d03 |
| Prover strength | BFS-Prover 74.2% vs common tactics 47.5% | d14 |
| Budget | 51.6% at 128 samples vs 60.2% at 32x6400 | a13 |
| Split | random vs novel_premises halves score | a10 |
| Decomposition depth | D=0 75%, D=2 98.36%, D=3 98.7% | d02 |
| Benchmark difficulty | miniF2F saturated; PutnamBench not | c17, d15 |
| Checker format | Models not trained for Lean output fail to produce valid text | b26, d15 |
| Prompt wording on judges | up to 27.3 points swing | d10 |

### 5.4 Interventions that worked and did not

Worked: tool handoff (Thor, +8.2 over the union), sketch-and-fill (DSP, +18.4 over Sledgehammer+heuristics), decomposition (Hilbert +24.6 over pass@4 prover), checker feedback with backtracking against a weak-sampling baseline (COPRA +2 over no-backtracking, +10.6 over 60 plain samples), lemma library (+3.3), retrieval (small), expert iteration (training only).

Did not or unclear: model-written informal hints with a strong prover (0 to 4 points); search over strong whole-proof sampling (+2.5 to 3.3); learned value in place of model likelihood (untested head to head); LLM verifier as final gate (fails); retrieval of informal proofs under 1 point (within noise).

### 5.5 Weak spots in the evidence

- miniF2F-test has 244 items. One point is about 2.4 items. Gaps under 1 point are noise (K11).
- Compute differs by orders of magnitude: 1 GPU 5 days (ReProver) to 500 TPU-days.
- pass@1, cumulative, and different time caps are mixed across papers.
- Contamination of GPT-4, DeepSeek and recent models on miniF2F and PutnamBench is argued but not measured (d15, d16, d17).
- No equal-token comparison of a propose-check-backtrack scaffold against best-of-N in a formal prover exists. Hilbert compares with pass@4 and call counts. DSP+ compares to token counts from other papers.
- Seed-Prover, BFS-Prover, STP, Kimina, Lean Copilot, Lean-STaR numbers were not re-checked against the full text in the cross-check.

## 6. Language models

**2020 to 2022: purpose-trained transformers.** GPT-f 700M, HTPS, PACT. Metamath 56.22% to 65.6%; miniF2F-test 29.6% to 41.0%.

**2023: frozen general LLMs without a scaffold are poor.** GPT-4 zero-shot with best-first search 29.0% on LeanDojo random split but 7.4% on novel_premises (a10); few-shot whole-proof 13.52% on miniF2F (b07); 1/640 on PutnamBench 2024 (d15). GPT-4 kept writing Lean 3 syntax in Lean 4. A scaffold changed this. COPRA doubled GPT-4 (13.52 to 26.63, 29.09 with retrieval). Gains were small for GPT-3.5 and CodeLlama (9.02, 5.73).

**2024: RL on checker feedback.** DeepSeek-Prover-V1.5 jumped 50.0 to 60.2% single pass; RMaxTS added 2.5 to 3.3.

**2025: reasoning models.** Kimina 68.85% pass@32 vs Gemini 37.70% and o3 24.59% in the same table, so training for the checker format was the key. Then code loops around general reasoners overtook: Hilbert 99.2%; DSP+ 79.5% training-free. The Hilbert loop moves from 13.3% (gpt-oss-120b) to 55.9% (Gemini 2.5 Pro) on one-attempt Putnam, so planner strength dominates.

**Change per intervention.**

| Change | Size | Evidence |
|---|---|---|
| Scaffold on GPT-4 | 13.52 to 26.63 (+13.1) | b07 |
| Hammer handoff | +18.0 (39.0 to 57.0) | a08 |
| Informal sketch | +18.4 (20.9 to 39.3) | a09 |
| Recursive decomposition (strong planner) | +24.6 over prover pass@4 | d01 |
| RL on Lean feedback | +10.2 (50.0 to 60.2) | a13 |
| Tree search over whole-proof sampling | +2.5 to +3.3 | b08 |
| Self-correction (Goedel-V2) | +2.3 miniF2F (confounded by tokens) | b15 |
| Lemma library | +3.3 | d05 |
| Informal draft with a strong prover | 0 to +4.1 | d14 |

**Informal proving.** An LLM verifier loop took 5/6 IMO 2025 problems on three different models vs 31.6/21.4/38.1% for best-of-32 (a19). But when the judge is an LLM, false-pass rates are 38 to 75% on university-level proofs (d09), and GPT-5 passed 7 of 48 flawed USAMO proofs even given a reference solution (d08). A shortcut classifier (MLP on embeddings, 75.34%) and a keyword rule (65.07%) rival mid-size judges (d08).

**Honesty limits.** Seed-Prover and AlphaProof are RL-trained and not usable by a frozen scaffold. Hilbert's prover and verifier are trained by others, but the loop is code. Hilbert's PutnamBench 70.0% used exhaustive retries; the one-attempt figure is 55.9%.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Never use an LLM verifier as the final gate.** Use code checks, execution, held-out inputs. If only an LLM verifier exists, run it on known-wrong outputs, report the false-pass rate, and treat a pass as a hint (strengthens G2, G3, G5). | G2, G5 | [E] | d08, d09, d10, K25 |
| A2 | **Check the statement, not just the proof.** Add a check that what was verified equals the original question (restated twin). | G3 | [E] | d13, d16, a15, a21, K20 |
| A3 | **Report attempts and tokens per item for every arm.** Headline numbers move 8 points with budget. | G7 | [E] | a13, d03, K24 |
| A4 | **Decomposition belongs at impasses (O3), depth 2 to 3.** Decomposition helps; the depth cap is single-source. | O3 | [E] helps, [S] depth cap | d01, d02, b17, d05, a14 |
| A5 | **Code tracks AND-OR structure** of subgoals (which lemma is open, which solved). A flat retry list is not enough for multi-part problems. | S6 subgoal, S4 | [E] | a07, a17 |
| A6 | **Call a tool or checker when one exists and let its result replace model text** (solver, executor). | S4, O (tool call) | [E] | a08, a09, d11 |
| A7 | **Expect diminishing returns by attempts.** Spend by difficulty (G12); do not add search where the base rate is near zero. | G12, S0 | [E] diminishing returns, [S] floor | a06, b10, d03, d18 |
| A8 | **Held-out evaluation.** Build tests from items novel to the model (post-cutoff or restated twins), not random splits of public sets. | G3, benchmark design | [E] splits matter; contamination size unmeasured | a10, d15, d16 |
| A9 | **Ignore sub-1-point ablation gaps.** Use more items. | G7 | [E] | b21, d02, K11 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Propose-check-backtrack loop vs best-of-N at equal tokens on checkable items | S3, S4 | [S] | b07, K01, K10 |
| T2 | Feed back the error diagnostic only, not the failed text | S5, G2 | [C] | d07, d06, b15, K17 |
| T3 | Truncate-and-resume: keep the verified prefix, regenerate from the last good state | O (resume) | [S] | a13, b24, K14 |
| T4 | Checked-lemma store with retrieval across subgoals | memory (subgoal library, planned) | [S] | d05, d02, K29 |
| T5 | Code-computed state score (open goals, size) vs model self-rating | S4 | [S] | b10, d12, a02, K04 |
| T6 | Fixed rule "try the tool first" vs model-chosen call | O (tool call) | [S] | d11, a08 |
| T7 | Plan-then-fill vs direct attempt, with and without the written plan | S3 | [E] weak executor, [S] strong | d13, d14, a09, K26 |
| T8 | Few cheap attempts vs one deep attempt at equal tokens | S3, G11 | [S] | a06, a02, K03 |
| T9 | Conjecture-and-refute for answer-finding items | S3, S4 | [S] | a18, a27, K21 |
| T10 | Raw-pass-rate floor for scaffold benefit | S0, G12 | [S] | d03, d18, K09 |
| T11 | Parallel independent attempts vs tree reusing prefixes | S3 | [S] | a13, b18, K13 |
| T12 | Informal verify-and-refine loop with an independent verifier vs best-of-N | G2, S4 | [S] | a19, d08-d10, K19 |

## 8. Concrete tests on our bench

All arms get the same total token budget. Every arm logs attempts, tokens, and checker calls. Item sets must have an exact checker (code execution, held-out inputs, Lean if available), a base pass rate between 10% and 70% for the plain model, and a held-out twin split (restated or post-cutoff).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 propose-check-backtrack | ARC-like and BrainTeaser items with code checks; programmatic puzzles | (a) one long free attempt; (b) best-of-N short attempts, code selects by check; (c) loop with checker feedback and backtracking | solve rate with 95% CI; tokens per solve | (c) over (b) by 0 to 5 points; both over (a). Zero gain means the COPRA effect was a sampler artifact |
| T2 diagnostic-only feedback | Items where first try fails | fresh resample vs error-only retry vs failed-text-plus-error retry | solve rate on second try; copying rate (edit distance to failed attempt) | error-only >= resample; failed-text arm lower (anchoring, d07) |
| T3 truncate-and-resume | Multi-step items with step-wise checks | restart vs resume from last verified step | solve rate; tokens per solve | resume wins on long items, ties on short |
| T4 lemma store | Item families sharing sub-results | with vs without a verified-lemma store | solve rate on later items | +2 to +4 points (LEGO +3.3) |
| T5 code score vs self-rating | Branching search items | rank open branches by code score, model self-rating, random | solve rate at fixed node budget | code score >= random > self-rating, small margin |
| T6 fixed tool-first rule | Items with an available solver | tool-first vs model decides when vs model-only | solve rate; tool calls | tool-first within 2 points of model-decides |
| T7 plan then fill | Multi-part items | direct vs plan+fill vs fill without plan | solve rate | plan helps on weak model, 0 to 4 points on strong |
| T8 shallow vs deep | Mixed difficulty | one deep attempt vs 4 or 8 short attempts | solve rate by difficulty tier | many short attempts win on easy and mid items (G11) |
| T9 conjecture and refute | "Find all" or answer-search items | single answer vs many guesses refuted by code | solve rate | gain where cheap refutation exists |
| T10 floor | Items binned by raw pass rate | scaffold vs plain on bins 0-5%, 5-20%, 20-60% | scaffold gain by bin | near-zero gain in the lowest bin (COPRA GPT-3.5 pattern) |
| T11 tree vs parallel | Items needing step state | N independent attempts vs tree reusing verified prefix | solve rate | small gain (2.5 to 3.3 points in DS-V1.5) |
| T12 verifier gate | Natural-language items with known-wrong cases | LLM verifier gate vs code check vs none | false-pass rate; final accuracy | false-pass above 20% means not a gate |
| T13 contamination control | Old public items and restated twins | same arms on both | accuracy gap | gap measures leakage; use twins for later tests |

## 9. What does not transfer, and why

- **Training loops (expert iteration, RL, TTRL, DPO on compiler errors).** Our agent is frozen. Only the idea of keeping verified results in context transfers.
- **Scale.** AlphaProof 80,000 TPU-days; Hilbert 22.8M tokens on the hardest problem. We pay tokens per item (G7).
- **Exact formal checkers.** Lean and Metamath give a perfect pass or fail with error text. Most of our tasks have a weaker checker. Repair and backtracking results depend on a clean error message. Informal tasks lose the guarantee (K25).
- **Whole formal libraries.** Premise retrieval from mathlib is a large external memory problem; ours is a small lemma store.
- **Answer guessing with a second LLM and expert formalisation (AlphaProof IMO 2024).** Humans formalised the problems after release.
- **miniF2F as a yardstick.** 99.6% saturated, 244 items, mis-formalised statements.
- **Search-space size.** Proof search spaces branch hugely; ARC-style tasks have small candidate spaces. The 2.5 to 3.3 point search gain may be smaller or different there.
- **Budgets in calls.** Hilbert counts calls; calls are not tokens (d03).

## 10. Open questions

1. At equal total tokens, does a frozen general LLM with a code-owned propose-check-backtrack loop beat plain best-of-N on checkable proofs? (Only COPRA, one benchmark, weak sampler baseline.)
2. How much of the refinement gain (COPRA, Seed-Prover, Goedel-V2) survives against fresh resampling? (d07 says little; abstract only, 11 problems.)
3. What is the false-pass rate of the Huang and Yang verifier on olympiad proofs? (No clean number.)
4. Does a code-computed state score (open goals, proof length) rank partial proofs as well as a learned value head or model likelihood? (BFS-Prover shows no value head is competitive; no head-to-head.)
5. What is the minimum raw pass rate for a scaffold to help with current frontier models? (Hilbert and DSP+ fix a strong prover.)
6. Does decomposition into verified lemmas help a frozen model at equal tokens? (LEGO, Hilbert work; none matched.)
7. How contaminated are miniF2F and PutnamBench for current frontier LLMs? (PutnamBench went from about 0.2% to 70% in one year; unexplained.)
8. Does any of this transfer to planning or informal reasoning where the checker is weak? (Only informal-math papers speak to it.)
9. Is the learned "when to call the solver" decision needed, or does a fixed rule match? (Thor's baseline is a union, not a rule.)
10. Tree search vs best-of-N at matched budget in informal reasoning is mixed in snippets (d19), not opened.
11. The GPT-f Table 9 vs Table 12 setting mismatch (47.21% vs 42.90%) is unresolved.

## 11. Sources

[V] = opened and read (full text or PMC page). [M] = snippet only. Papers marked "(not re-checked)" were opened by an earlier agent but not re-opened in the cross-check.

| Source | Mark | URL |
|---|---|---|
| Polu and Sutskever 2020, GPT-f | [V] | https://arxiv.org/abs/2009.03393 |
| Han et al. 2021, PACT | [V] (not re-checked) | https://arxiv.org/abs/2102.06203 |
| Polu et al. 2022, Formal Mathematics Statement Curriculum Learning | [V] (not re-checked) | https://arxiv.org/abs/2202.01344 |
| Lample et al. 2022, HyperTree Proof Search | [V] (not re-checked) | https://arxiv.org/abs/2205.11491 |
| Jiang et al. 2022, Thor | [V] | https://arxiv.org/abs/2205.10893 |
| Jiang et al. 2022, Draft, Sketch, and Prove | [V] | https://arxiv.org/abs/2210.12283 |
| Zheng, Han, Polu 2021, miniF2F | [V] (not re-checked) | https://arxiv.org/abs/2109.00110 |
| Yang et al. 2023, LeanDojo | [V] | https://arxiv.org/abs/2306.15626 |
| Thakur et al. 2024, COPRA | [V] | https://arxiv.org/abs/2310.04353 |
| First et al. 2023, Baldur | [V] | https://arxiv.org/abs/2303.04910 |
| Wang et al. 2023, LEGO-Prover | [V] | https://arxiv.org/abs/2310.00656 |
| Xin et al. 2024, DeepSeek-Prover | [V] (not re-checked) | https://arxiv.org/abs/2405.14333 |
| Xin et al. 2024, DeepSeek-Prover-V1.5 | [V] | https://arxiv.org/abs/2408.08152 |
| Ren et al. 2025, DeepSeek-Prover-V2 | [V] | https://arxiv.org/abs/2504.21801 |
| Lin et al. 2025, Goedel-Prover | [V] (not re-checked) | https://arxiv.org/abs/2502.07640 |
| Lin et al. 2025, Goedel-Prover-V2 | [V] | https://arxiv.org/abs/2508.03613 |
| Lin et al. 2025, Lean-STaR | [V] (not re-checked) | https://arxiv.org/abs/2407.10040 |
| Dong and Ma 2025, STP | [V] (not re-checked) | https://arxiv.org/abs/2502.00212 |
| Xin et al. 2025, BFS-Prover | [V] | https://arxiv.org/abs/2502.03438 |
| Wang et al. 2025, Kimina-Prover Preview | [V] (not re-checked) | https://arxiv.org/abs/2504.11354 |
| Hubert et al. 2025, AlphaProof (Nature) | [V] | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12999475/ |
| ByteDance Seed 2025, Seed-Prover | [V] | https://arxiv.org/abs/2507.23726 |
| Huang and Yang 2025, IMO 2025 verification-and-refinement | [V] | https://arxiv.org/abs/2507.15855 |
| Varambally et al. 2026, Hilbert | [V] | https://arxiv.org/abs/2509.22819 |
| Cao et al. 2025, Reviving DSP (DSP+) | [V] | https://arxiv.org/abs/2506.11487 |
| Tsoukalas et al. 2024, PutnamBench | [V] | https://arxiv.org/abs/2407.11214 |
| Song, Yang, Anandkumar 2024, Lean Copilot | [V] (not re-checked) | https://arxiv.org/abs/2404.12534 |
| Mahdavi et al. 2025, Scaling generative verifiers | [V] | https://arxiv.org/abs/2511.13027 |
| Gonzalez et al. 2026, QEDBench | [V] | https://arxiv.org/abs/2602.20629 |
| Naik et al. 2026, Do we need frontier models to verify proofs? | [V] | https://arxiv.org/abs/2604.02450 |
| Yousefzadeh and Cao 2025, complete benchmarks position paper | [V] | https://arxiv.org/abs/2507.04719 |
| Li and Li 2026 (NeurIPS), Repair, Retry, and the Cost of Hindsight | [V] abstract page only | https://neurips.cc/virtual/2026/171436 |
| Pythagoras-Prover 2026, decontamination | [M] | https://arxiv.org/pdf/2606.12594 |
| Snell et al. 2024 and student-project / VG-Search snippets | [M] | https://arxiv.org/abs/2408.03314 |
| DeepMind AlphaProof as cited in DeepSeek-Prover-V2 | [M] | https://arxiv.org/abs/2504.21801 |
