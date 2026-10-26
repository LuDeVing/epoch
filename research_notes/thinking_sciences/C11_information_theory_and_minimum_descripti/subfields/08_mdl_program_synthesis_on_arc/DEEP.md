# MDL program synthesis on ARC: deep document

*Subfield C11.08. Source files in this folder: evidence_a-d.jsonl, claims.jsonl, critique.md. Ids such as a04, K02 point to those files. Status tags: [E] established (two or more independent sources), [S] single-source, [C] contested. All 2026 sources are preprints, mostly single-author, tuned on public sets. Treat their numbers as optimistic.*

## 1. What it is

The idea: the best explanation of a few examples is the shortest one. Applied to ARC, a puzzle gives about 3.3 input-output grid pairs. The solver looks for the shortest program (or model) that reproduces all the pairs, then applies it to the test input.

Formally this is two-part Minimum Description Length (MDL). Pick the hypothesis H that minimises L(H) + L(D|H), in bits (a32). L(H) is the cost of writing the rule down. L(D|H) is the cost of the examples once the rule is known. A rule that is too simple leaves a large residual. A rule that is too complex memorises the data. The sum balances them.

Chollet (2019) gives this a theory base. He defines the difficulty of a task through the length of its shortest solution program on a fixed universal machine (a31). Kolmogorov complexity is not computable, so it is a yardstick, not a score.

Three families use the idea on ARC.

1. **MADIL (Ferre, 2020 to 2025).** A symbolic system, no neural net, no LLM. A program is a pair of grid models: an input model that splits the input into parts, and an output model that rebuilds the output from those parts. Search is guided by description length. Code in OCaml on GitHub (b22). This is the subfield's key work (arXiv 2505.01081).
2. **CompressARC (Liao and Gu, 2025).** A 76K-parameter network with no pretraining, trained for 2000 steps on one puzzle at test time. The loss is a variational estimate of description length: reconstruction error plus the KL cost of a latent code. Code-golf framing (a18).
3. **LLM systems that use a length-like score.** Product of Experts scores candidates by summed log-probability across augmented views (c16). A Solomonoff-style ranking was tried on 3 tasks (d10). A prompt-only "compress to a rule first" scaffold was tried (d11). No LLM study uses code length as the selector at matched cost (K23).

Why it matters to our agent: S2 (represent: write candidate rules) and S7 (select: which rule to submit). MDL offers a concrete answer to "which of several rules that fit all examples is best". The evidence says it is a useful but limited answer. Its main value for us is as a tie-break and a warning label, not as a solver.

## 2. History and theories in depth

**Theory base.**
- Solomonoff and Kolmogorov: prior probability of a program falls with its length. Occam's razor in code.
- Rissanen's MDL and Grunwald's tutorial (a32). Crude two-part MDL needs a hand-chosen code for H. Refined MDL uses universal codes (NML) that remove that arbitrariness. MADIL and its 2021 predecessor use crude two-part MDL. They inherit its weakness: the result is only as good as the code. That is why the hand-set priors in MADIL matter (d15).
- DreamCoder (Ellis et al.): wake-sleep program learning where the prior favours short programs, and a library of abstractions is grown by compressing solved programs (a33). MADIL's author names learned primitives as open work.
- Chollet 2019: skill as efficient acquisition of short programs (a31).

**Timeline on ARC.**
- 2020: Kaggle ARC. Icecuber wins with brute-force search in a DSL, 20% private. All entries pooled solve 49% of private tasks (a29, b19). Organisers read this as a sign that ARC-AGI-1 is partly shallow.
- 2020 to 2021: Ferre's first paper, "descriptive grid models and MDL". Over one year, training tasks solved went from 5 to 29 of 400 (7.25%), with 30 s per task. Evaluation: 6 of 400 (1.5%) (a14, a15). Gains came from hand-added models, not new principles (c06).
- 2022: ARCathon. Hodel's DSL search scores 6% private (c27). MADIL scores 2% (a01).
- 2023: Hypothesis Search (Wang et al.) puts an LLM in front of program synthesis (a28). Graph search ARGA reaches 35.6% on 160 object tasks (c20).
- 2024: ARC Prize 2024. Winners combine induction and transduction, and test-time training. BARC (a23), Akyurek (a26), CodeIt (c18). MADIL v3.5 gets about 7% on the private set (a05). The 2024 technical report does not mention MDL (b18).
- 2025: MADIL paper (arXiv 2505.01081). CompressARC (arXiv 2512.06104) shows 20% on ARC-AGI-1 evaluation with no pretraining. ARC-AGI-2 launches and is built to resist brute force (a30, c23). Product of Experts reaches 71.6% on public eval with an 8B model (c16).
- 2025 to 2026: ARC Prize 2025. The theme is refinement loops. Top Kaggle ARC-AGI-2 score is 24.03% (NVARC). No winner is described as using MDL or code length. CompressARC wins third paper award, scores about 4% on ARC-AGI-2 (d01, d02). Later non-competition preprints: Land 72.9% semi-private (d08), Zhu 87.8% pass@2 (d11). They use refinement and judging, not length.

**Competing views.**
- *Compression as the core of intelligence* (Chollet, Liao and Gu). Support: CompressARC beats a same-data U-Net 20% vs 0.75% (c08). Limit: the U-Net is the authors' own baseline and only one is tested.
- *Scale and data win* (Akyurek, Franzen, Cole and Osman). Neural test-time training plus augmented voting reach 53 to 72% on ARC-AGI-1. No MDL term in the method (c25).
- *Brute-force search is enough on ARC-1* (organisers' reading). Pooled search solves about half of private tasks (b19).
- *Hybrid.* Every top 2024 entry mixes transduction and induction (b18).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| MADIL fit-then-generalise on public evaluation (400 tasks, not used in design) | 69 tasks fit all training pairs. 57 correct on all test inputs (82%). 12 fit but wrong (about 18%). 53 of 57 correct on first attempt. 2 more right from a model that misread one training pair | MADIL (a04, b01) | [S] |
| MADIL overall score | Micro-accuracy: train 32.1%, public eval about 15.1% (cell inferred from garbled table; 57 to 59 of 400 is 14.25 to 14.75%), private 7.0%. One CPU thread, 180 s per task | MADIL Table 6 (a05, c01) | [S] |
| Greedy compression finds the answer early | 54 of 69 solutions on first greedy rollout. 80% of solutions in first 20 s of 180 s. Best-model mean rank 1.3 (solved), 1.6 (all). Mean models visited 177 (all) vs 45 (solved). Depth 17 vs 11 | MADIL Table 8 (a07, b03) | [S] |
| Length score reaches depth brute force cannot | Correct models have size 3 to 46, mean 15.2. Only 4 tasks have a correct model of size 4 or less. Brute-force DSL search is limited to depth 3 to 4 | MADIL (a06, b02) | [S] |
| Several descriptions per input matter most | Of 71 tasks solved by some version: Np=1 loses 19, Se=1 loses 27, Kp=1 loses 6. Np=10 vs 100 loses 1. Se=5 vs 9 loses 0. Greedy only loses 4. No rehearsal factor loses 6. No test-input check or pruning loses 6 | MADIL ablation (a08, b04) | [S] |
| Fit-but-wrong is common in MDL fits | 21 of 400 training tasks: model found, wrong on test. Cause: contrived expressions that patch a wrong decomposition. Worse with fewer examples and larger expression budget. 2021 versions: gap of 7 to 12 tasks (12 of 41 at v2.2 on train) | MADIL (a10, a15, a16, c03) | [E] (also BARC, K03) |
| Search failures | 62 training tasks solvable but not found: 21 need a non-compressive step first, 15 lack diverse top descriptions, 13 other | MADIL (a10) | [S] |
| Rehearsal weight is a free knob | Data term x10 (2021), x100 (2025). Chosen by hand. Removing it loses 6 of 71 | MADIL (a03, a17) | [S] |
| MDL and brute force are complementary | Evaluation, all test outputs right: MADIL 59, Icecuber 117, overlap 43, MADIL-only 16 | MADIL (a09, b06) | [S] |
| Pure MDL is far below LLM systems | MADIL 7% private. CompressARC 20% public eval. Icecuber 17 to 20%. BARC + TTT ensemble 56.75 to 61.9%. Product of Experts 71.6% (public eval, heavy sampler) | multiple (K07) | [E] |
| CompressARC with no pretraining | 76K params, 2000 steps, about 20 min on RTX 4070. Eval pass@2 20.0% (peak 21.5% at 1500 steps), pass@1 18.5%, pass@1000 33.75%. Train pass@2 34.75%, pass@1 30.25%, pass@10 41.5%, pass@1000 52.75%. Full eval set about 138 h GPU | CompressARC (a18, a20, b10, b11, c09) | [S] |
| MDL objective vs plain test-time fitting | U-Net trained on the same puzzle only: 0.75% vs CompressARC 20%. Augmentation hurt the U-Net on train (2.5% to 1%) | CompressARC Table 1 (a19, c08) | [S] (authors' own baseline) |
| CompressARC accuracy by steps (eval pass@2) | 100: 1.25. 300: 10.75. 500: 15.0. 1000: 19.25. 2000: 20.0 | CompressARC (a20, c09) | [S] |
| CompressARC blind spots | Cannot map two colours to each other, repeat in series, count, translate/rotate/reflect/rescale, detect connectivity, plan, or extend patterns over long range. Joint compression across puzzles tried, did not work | CompressARC App. H, K (a21, b13, c11) | [S] |
| Induction and transduction solve different tasks | Stable across seeds. ARC-Heavy: induction 30.5% (2 tries), transduction with TTT 43.25%. ARC-Potpourri: 38.0% vs 43.0% | BARC (a23, b14, b16) | [E] |
| Ensemble of the two | 56.75% on 400 validation tasks (2 tries) vs average human 60.2%. Needs 10k to 20k programs per task. Scaled-down: 19% Kaggle private, 36.5% validation | BARC (a24) | [E] |
| False-positive rate in LLM programs | About 9% of fitting programs fail the test. About half of those sit in problems where majority vote still gives the right answer | BARC (b15, c13) | [S] |
| Test-time training | 8B model: 18.3% to 47.1%; on BARC base 53.0%; with synthesizer 61.9%. Semi-private only 47.5% | Akyurek (a26, c15) | [E] |
| TTT narrows the gap to programs | Neural model solves 73.5% of tasks BARC's program model solves, up from 42.2% | Akyurek (a27) | [S] |
| Likelihood across views as selector | Llama-3.2-3B: 14.9, 40.9, 52.9, 59.5, 61.4. NeMo-Minitron-8B: 18.3, 44.5, 62.5, 67.6, 71.6 (base, TTT, +16 augmented samples, +PoE selection, +DFS sampling). About $0.02 per task | Franzen PoE (c16) | [S] |
| Hypothesis first, code second | GPT-4 on 100 tasks: direct 17%, program 23%, summarised hypotheses 30%, human-picked 33%. Only 49 tasks had a correct hypothesis; 33 of 49 (67%) gave correct programs with human selection. Icecuber 43% on the same 100 | Wang (a28, c17) | [S] |
| Self-improving program search | CodeIt 15% eval. Shorter program found later for 53% of solved tasks, with no MDL term. Fails beyond 11 lines | CodeIt (c18) | [S] |
| Learned prior vs length prior | GridCoder 5.75% eval at 15 min, 79.3% of the 29 DSL-solvable tasks. DSL coverage is the ceiling. Hidden test 0 to 1% | Ouellette (c19) | [S] |
| Human accuracy | H-ARC: 76.2% train, 64.2% eval after 3 attempts; 72.6% / 60.2% after 2; 59.9% / 47.8% after 1. 784 and 948 participants. Older figure 83.8% came from 40 tasks (95 participants) | H-ARC, Johnson (c21, c22) | [E] |
| Short rule wording predicts human success | Description length b = -0.17, 95% CI [-0.315, -0.020], p = 0.03, 40 tasks, 95 participants. Descriptions written after the attempt | Johnson 2021 (c21) | [S] |
| Search collapses on ARC-AGI-2 | ARC-AGI-1 vs 2, semi-private: Icecuber 17.0 vs 1.6; o3 medium 53.0 vs 3.0; ARChitects 56.0 vs 2.5; Claude 3.7 (8K) 21.2 vs 0.9. Scores under 5% are noise. CompressARC about 4% | ARC-AGI-2 paper, Prize 2025 (b20, c23, d02) | [E] |
| Selection is a smaller bottleneck than generation | DeepSeek V3.2, 5 candidates: selecting by training accuracy recovers about 95% of the candidate ceiling. Pipeline pass@2 57.5%; orchestrator 67.25% (lift +9.75 pp, CI +6.50 to +13.25) | Moghe and Chin (d06) | [E] with Land, SOAR |
| Oracle gap in other systems | SOAR: voting 9.5 points below oracle. Land (ARC-AGI-2, 167 instances): 22 had no correct candidate, 17 had one not picked; judge beat majority vote by 7 instances, all minority answers | SOAR, Land (d04, d08) | [E] |
| Consensus fails on hard tasks | One task: 12 candidates agree on a wrong output, 8 on another, 1 is correct | Land (d09) | [E] (K19) |
| Prompt-only compression scaffold | ARC-AGI-2 public, 120 tasks, pass@1 / pass@5: GPT-5.5 51.9/62.8 to 60.6/76.8; Gemini 3.1 Pro 54.4/76.9 to 62.4/86.7. Same structured rule in one context: 41.5/59.9 and 31.6/62.8, below baseline | Zhu (d11, d12) | [S] |
| Length-weighted LLM hypothesis ranking | 3 Mini-ARC tasks: Solomonoff-weighted vs accuracy-only 64 vs 48, 100 vs 100, 60 vs 64 (%) | Barber (d10) | [S], no result either way |
| Independent MADIL replication | None found. Survey of 82 approaches: none. CompressARC has 4 citers, none a re-run. MADIL citer list not retrieved | b24, d13, d14 | no evidence found |

## 4. Mechanisms and models

### 4.1 Two-part MDL score (MADIL)
- Task model M = (input model, output model). Total length L(M) + L(E|M).
- Code lengths are Shannon lengths, L(v|V) = -log2 f_V(v), taken from explicit value distributions (a02). Value types: sprites, masks, vectors, objects, colours, motifs. Priors are hand-set. Uniform over intervals for integers and motif lists. Colour split: background black is likely, object black is unlikely (d15).
- Data term is multiplied by a rehearsal factor (10 in 2021, 100 in 2025) because 3.3 pairs stand in for many valid pairs. Too low stops search early. Too high favours overfitting. Normalised DL gives inputs and outputs equal weight, range [0, 2] (a03).
- Bitmap cost in the early version: height x width bits (a17).
- Implementer note: the weight and priors are design choices. No ablation swaps a flat prior for the hand prior (d15).

### 4.2 Search (MADIL)
- State = task model. Action = transition (add a pattern, refine a value, add an expression). Value = 1 - 0.5 x normalised DL. UCB1 with c = 2. Rollout is greedy to the end. Stop when a model is correct on all training pairs or time runs out (a13).
- Defaults (Table 3): Np=100 sampled descriptions per grid, Kp=3 kept, Ng=Kg=3, Se=6 expression size, Ne=1000, Kt=100, K=3 attempts (2 at ArcPrize) (a13).
- Pure decomposition patterns are not compressive on their own, so an extended lookahead tries them (a13).
- Several candidate parses of each grid are sampled, and the best by DL is kept. This is the most important ingredient (Np=1 loses 19 of 71).

### 4.3 Post-processing
- Pruning: after search, replace constants and patterns in the input model by unknowns if accuracy does not drop. Example: task 47c1f68c, black background becomes an unknown. Not applied to the output model, since it would add predicted outputs and cut accuracy (a11).
- Parse-check of the test input against the input model. Removing both loses 6 of 71.

### 4.4 Test-time MDL by gradient (CompressARC)
- Train a small equivariant network on all demonstration grids plus the test input (output hidden). Loss = reconstruction error + KL of the latent code. Weights are counted in bits (a18).
- Output is the decoded test output after the last step. Several samples (pass@k) give guesses.
- Learned latents separate into pieces: for puzzle 272f95fa, a colour-to-direction table plus row and column divider positions. Top principal component 829 times the next (a22). When a needed tensor collapsed to zero information the run usually failed (c10). A length score can delete a necessary rule part.

### 4.5 Likelihood across views (Product of Experts)
- Generate candidate outputs. Re-pose the task under several augmentations (rotation, transposition, colour permutation). Score each candidate by the sum of negative log-probability across all views. Pick the lowest. This is a code-length-like score under the model (c16).
- Gain from selection alone: 62.5% to 67.6% on the 8B model. Sampler change adds 4 more points.

### 4.6 LLM pipelines that use fit and compression
- **Hypothesis Search (a28).** 64 hypotheses proposed, 8 kept after summarising, 8 programs per hypothesis, 3 rounds of execution feedback. Top-1 scoring. Direct 17% to 30%.
- **SOAR (d04).** 6k programs per task (3k sampled, 3k refined). Vote weight = count + 1000 x mean training accuracy. Rejects programs that contain a training output as a literal (d05).
- **Moghe and Chin (d06, d07).** Several independent definers each write a rule. Exact fit on all training pairs required. Convergent test outputs count as one vote. Tie on training score broken by index.
- **Hourglass (d11, d12).** Stage 1 induces a schema and rule. Later stages see only that compressed state, in fresh contexts. An anti-patching rule forbids `if color == 3` branches.

### 4.7 Fit-but-wrong checklist (from MADIL 2021, a16)
- Wrong constant-versus-variable choice and accidental arithmetic equalities (0962bcdd).
- Wrong segmentation, preferring a full rectangle (1caeab9d).
- The transform should repeat more times in test (29c11459).
- Invariance to rotation or transposition missed (4522001f).
- Contrived expressions compensating for a wrong decomposition (21 tasks, c03).
- Hard-coded outputs by grid size (d05).
- Colour-keyed if-else patches (d12).

## 5. What holds up

**Replications.** None for MADIL. All its numbers are one author's. The CompressARC citers contain no re-run (d14). The MADIL citer list could not be pulled (rate limits), so "none" is weak evidence (K17). Partial checks inside this series: the critique re-opened MADIL, CompressARC and Product of Experts PDFs and confirmed ten key numbers. BARC, TTT and hypothesis-search numbers were not re-checked.

**Held up.**
- Fit-but-wrong is real in every system that was measured: MADIL 18% of fits (a04), 2021 versions 7 to 12 tasks, BARC about 9% (b15), LLM programs on ARC-AGI-2 (d05, d09, d12). Four independent sources. [E]
- Induction and transduction are complementary, across BARC, Akyurek, ARC Prize 2024 and the ARC Prize 2025 report. [E]
- Selection is not where most is lost. Three sources (Moghe and Chin, Land, SOAR) put the oracle gap at 10 points or less, and generation failure is of the same order or larger. [E]
- Consensus is a poor selector on hard tasks. [E] (Land, SOAR, Moghe and Chin).
- Search-style and compression-only methods collapse on ARC-AGI-2. [E]

**Failed or weak.**
- CompressARC eval accuracy peaks at 1500 steps (21.5%) and dips to 20.0% at 2000 (a20).
- Joint compression across puzzles did not work (c11).
- Random augmentation hurt the U-Net control (b12).
- Adding primitives to MADIL is unlikely to solve ARC (b05). Version 1 to 3 of GridCoder's DSL went 5.75%, 7.75%, 8.25% on eval but 0%, 1%, 1% on the hidden test (c19).
- Structured rule output inside one context was worse than plain self-refine (d12).
- Length-weighted ranking: win, tie, loss on 3 tasks (d10).
- MADIL evaluation 1.5% (2021) rose to about 15% (2025). The gains came from hand-added patterns (c06).

**Moderators.**
- Number of examples. Fewer examples, more fit-but-wrong (c03).
- Expression budget. Larger Se, more contrived fits (c03).
- Benchmark generation. ARC-AGI-1 vs ARC-AGI-2 changes scores by 2.5 to 3 times (d13).
- Split. Public eval, semi-private and private differ. TTT 53.0% on public validation became 47.5% semi-private (a26). Icecuber 30.8% eval became 20.6% private (a05).
- Number of samples. BARC solve rate rises nearly monotonically from 0 to 2000 samples (c13).
- Context isolation. Hourglass gains vanish when stages share a context (d12).

**Competing explanations.**
- The 82% in MADIL may reflect a hand-built DSL of core-knowledge primitives, not the MDL principle. A flat-prior ablation would separate the two. Not run (d15).
- The CompressARC win over the U-Net may reflect the network's built-in symmetries as much as the MDL loss (c08).
- Short wording predicting human success (Johnson) may be reverse causation. Descriptions were written after the attempt (c21).
- The ablation uses only the 71 tasks some version solved, which biases toward the final system's strengths (a08).

**Human baseline contradictions.** 83.8% (40 tasks) vs 64.2% eval and 76.2% train (H-ARC, full) vs 60.2% (average human used by BARC) vs 75% (ARC-AGI-2 paper, a different benchmark). Different samples and attempt counts (critique). Use 60.2% eval at two tries as the reference for ARC-AGI-1.

**Interventions that worked.**
- Keep several parses of each example (MADIL).
- Pruning unneeded constants, and test-input parse check (MADIL, 6 of 71 each way).
- Program path first, direct-answer fallback when no program fits (c14).
- Hypothesis before code (+7 to +13 points, GPT-4).
- Orchestrator that spawns fresh exploration when the current rule fails: +9.75 points (d06).
- Context-isolated rule hand-off (+8 to +14 on ARC-AGI-2, single author).
- Dedup of convergent outputs to protect dissenters (qualitative, d07).

**Interventions that did not work, or are unproven.**
- Consistency-judging as a selector: rewarded the wrong majority (d09).
- Majority vote on hard tasks (d08).
- Forcing a structured rule in the same context (d12).
- Adding primitives alone (b05).
- Length-based selection at matched cost: untested (K23).

## 6. Language models

**What the LLM studies show.**
1. *Direct prompting is weak, programs help.* GPT-4: direct 17%, program 23%, hypothesis-then-program 30% (a28). Chain of thought without programs: 19%.
2. *Fine-tuned LLMs can write programs.* BARC induction 30.5% (ARC-Heavy) and 38.0% (Potpourri). A fit-on-examples check removes most bad programs. About 9% of fitting samples still fail (b15).
3. *Transduction with TTT beats induction alone* on these sets (43.25% vs 30.5%), and the ensemble reaches 56.75% (a23, a24).
4. *Test-time training is the largest lever.* 18.3% to 47.1% (a26). TTT closes much of the gap to programs: 42.2% to 73.5% overlap (a27).
5. *Likelihood across augmented views is a selector.* Plus 5 points on an 8B model (c16). This is the nearest thing to an MDL selector in an LLM loop, and it is not stated as MDL.
6. *Frontier models in 2025 to 2026.* ARC-AGI-2 scores under 5% for 2025 base models (c23). With refinement loops they reach 54% (Poetiq on Gemini 3 Pro, self-reported, $31 per task), 72.9 to 76.1% (Land), 87.8% pass@2 in competition mode (Zhu). Cost per task ranges from $0.20 (NVARC) to $39 (Land) (d01, d03, d08, d11). All are preprints.
7. *Reasoning length does not signal truth.* One task: 96 reasoning tokens (Gemini 3 Pro) vs 138,000 (Deep Think) (d03). No correlation study exists. (This fits G10 and G11.)
8. *Where the loss is.* On ARC-AGI-1 with DeepSeek V3.2 at 5 candidates, 95% of the ceiling is reached by train-accuracy selection (d06). On ARC-AGI-2 with 8 to 29 candidates, 13% of instances had no correct candidate and 10% had one not picked (d08).
9. *How LLM programs go wrong.* Hard-coding training outputs (d05). Colour-keyed branches (d12). Several samples converge on the same wrong rule (d07, d09).

**What changed performance and by how much.**
- Hypothesis step before code: +13 points over direct (GPT-4, a28).
- Execution feedback on summarised hypotheses: 24, 28, 28, 30% for 0 to 3 rounds (c17).
- TTT: +29 points (c15).
- Augmented-view voting: from 44.5% to 62.5% (c16).
- Product-of-experts selection: +5.1 points (c16).
- Orchestrator vs pipeline: +9.75 points, CI +6.50 to +13.25 (d06).
- Context-isolated hand-off: +8.0 to +14.0 points (d11).
- Trace-reading judge over majority vote: +7 solved instances out of 167 (d08).

**What no one has measured.** Length or MDL selection among fitting LLM programs at matched sampling cost. Flat-prior vs hand-prior MDL. Length of reasoning trace vs correctness. Human vs model description length (K23).

## 7. What our agent should take

Current S7 reads: group candidates by behaviour on fresh inputs, symmetry first, then group size, then shortest. The word "shortest" there is the MDL part. This subfield says: keep it as the last tie-break, state what "shortest" means in code, and do not expect it to carry the result.

### Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | A fit on the given examples is not proof. Keep G3 as is. Cite the measured rates: about 9% to 18% of fitting programs fail the test. | G3 | [E] | a04, a15, b15, c03, d05, d09, K03 |
| A2 | Add a code guard to S4: reject any program that contains a training output as a literal. Reject colour-keyed if-else branches that only patch examples. The guards exist in three systems. Their effect is not ablated, so ship them as cheap hygiene, not as a claimed gain. | S4, G3, G5 | [E] that the failure exists, effect unmeasured | d05, d07, d12, K24 |
| A3 | Keep a direct-answer fallback when no program fits all examples ("rule first, guess second"). Program and direct answers solve different items. | S3, S8, G6 | [E] | a23, a24, b16, c14, K08 |
| A4 | Never treat agreement as truth. On hard items the modal answer is often wrong. Dedup by output before counting group size, so a lone correct rule is not crowded out. Already in G4 and G5. This adds the evidence and the dedup step. | G4, G5, S7 | [E] | d07, d08, d09, d04, K19 |
| A5 | Before building any new selector, log the oracle gap (any candidate right vs chosen candidate right). Selection is a smaller loss than generation on ARC-AGI-1. | G7, S9 | [E] | d06, d08, d04, K18 |
| A6 | Report ARC-AGI-1 and ARC-AGI-2 separately, and use 60.2% (eval, two tries) as the human reference. | bench | [E] | b20, c22, K14, K15 |
| A7 | Put the final rule check in a fresh context that sees only the stated rule, not the earlier reasoning. This is already the S3 isolation rule. This subfield gives one more reason (the Hourglass ablation). Mark as support, not as proof. | S3, G4 | [S] on size, [E] for the isolation idea | d12 |
| A8 | Use the fit-but-wrong checklist (section 4.7) as the content of the S8 verify prompt for grid tasks: accidental equalities, wrong segmentation, wrong repeat count, orientation invariance. | S8, G3 | [S] (one author's list) | a16 |

### Test first

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Among candidates that pass all examples, pick the shortest under a stated coding scheme, vs random pick, vs vote. The 82% generalisation is MADIL's own and has no random-pick arm. | S7 | [C] (K02 is called established, but the "shorter beats random" part rests on MADIL and BARC) | a04, b15, d06, K02, K22 |
| T2 | Penalise complexity harder when few examples exist (rehearsal weight analogue). | S7 | [S] | a03, a17, K04 |
| T3 | Hold two or more parses of the examples in S2 before choosing (MADIL Np). | S2, S3 | [S] | a08, b04, K05 |
| T4 | Pruning step: drop every detail from the rule that the answer does not need, if accuracy holds. | S7, G3 | [S] | a11 |
| T5 | Rising rule complexity with no fit is a signal to stop and switch operator. | S6, G1 | [S] | b03, a07 |
| T6 | At an impasse allow a non-shortest move (detour). 21 of 62 MADIL search failures needed one. | S6, O3, O6 | [E] that the blind spot exists, [S] for the fix | a10, d06, d17, K13 |
| T7 | Rule-first with context reset. Compress the examples to a short rule and schema, then pass only that to later stages. | S2, S3 | [S] | d11, d12, K21 |
| T8 | Likelihood across rephrased views as a selector (needs token log-probs). | S7 | [S] | c16, K10 |
| T9 | Hypothesis first, code second, run each, then select. | S2, S7 | [S] | a28, c17, K11 |
| T10 | Run a symbolic helper (small DSL search) beside the LLM. Complementary solvers. | S3 | [S] | a09, b06, K06 |
| T11 | Reject-the-hard-coder guard effect size (A2 is hygiene, this measures it). | G3 | [S] | K24 |

**Not added anywhere:** training, test-time gradient updates, a learned prior, CompressARC networks, TTT. They need weights (K09, K12). Not usable by a prompt-only agent.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, setup cost counted (G7). Items: ARC-AGI-1 public evaluation 100-task sample, plus ARC-AGI-2 public 60-task sample, fixed seeds. Metric: exact match on all test outputs (pass@2), with a paired bootstrap CI. A gain counts only if the lower CI bound is above 0.

| Test | Item type | Arm A (control) | Arm B (change) | Metric | Expected effect |
|---|---|---|---|---|---|
| B1. Length selector | ARC items where at least 2 sampled programs fit all examples and give different test outputs (about 20 to 30 of 100) | Pick among fitting programs by dedup-then-vote | Pick the shortest by token count of code (stripped of comments and names), or by AST node count, ties by vote | Accuracy on the contested subset | 0 to +3 points over vote. Headroom is small (d06). If it loses, drop "shortest" from S7 |
| B2. Oracle gap audit | All 100 items from a standard S3 to S7 run | none | Log any-right vs chosen-right | Gap in points | Gap under 5 points means no selector work is worth it |
| B3. Guard ablation | Same 100 items | No guards | Reject literal-output programs, colour-keyed branches | Fit-but-wrong rate (fits all examples, wrong on test), and final accuracy | Fit-but-wrong rate down by a third or more |
| B4. Held-out example | Items with 3 or more examples | Fit on all examples | Fit on n-1, check on the held-out one, then refit | Fit-but-wrong rate | Lower false positives; cost is one example of fitting data |
| B5. Rule-first with context reset | ARC-AGI-2 items | Self-refine in one context | Stage 1 writes rule and schema. Stages 2 to 3 see only that, in fresh contexts | pass@1 | +5 to +10 points (Zhu: +8 to +14, single author) |
| B6. Same structure in one context | Same items | Arm B6 above | Same stages, one context | pass@1 | No gain or a loss (Zhu: below baseline). Tests whether isolation is the cause |
| B7. Hypothesis first | ARC-AGI-1 items | Direct program | 6 hypotheses, run each, keep fitters | pass@2 | +3 to +8 points |
| B8. Parse count | Items | One reading of the examples | Three readings, pick best by fit then length | pass@2 | +2 to +5 points |
| B9. Fallback | Items where no program fits | Return nothing or best program | Return a direct-answer guess | pass@2 on those items | Small gain; the arm cannot lose by G6 |
| B10. Dedup | Items where modal wrong output exists | Vote | Vote after dedup by output | Accuracy on those items | +1 to +3 items per 100 |
| B11. Impasse detour | Items where the first 2 rounds fail | Repeat S5 | Fire an operator from O3 or O6 | Solve rate after impasse | +3 to +6 points (Moghe and Chin: +9.75 for fresh exploration) |
| B12. Trace length | Logged runs | none | Correlate reasoning tokens with correctness within difficulty bands | Spearman rho | Near 0. Confirms G10 and G11 |

## 9. What does not transfer, and why

- **MADIL's DSL and priors.** Hand-built core-knowledge primitives and hand-set code lengths. An LLM has no such fixed code. Description length of LLM-written code is a different quantity (token or AST count), and no one has shown it tracks MDL.
- **The 82% generalisation rate.** One author, ARC-AGI-1, a DSL that cannot express conditionals. In an LLM loop, programs can be arbitrary Python and the false-positive structure differs (BARC 9%, MADIL 18%).
- **CompressARC.** Needs gradient descent per puzzle (about 20 min on a GPU). A prompt-only agent has no weights to compress. Only the idea of the objective transfers.
- **TTT and PoE gains.** Need weights or log-probs. TTT needs gradient steps per task (c15).
- **Large sample budgets.** BARC uses 10k to 20k programs per task. Our budget is a few attempts (G11).
- **ARC-AGI-1 results on ARC-AGI-2.** Search and compression collapse by 2.5 to 3 times (d13). Do not read ARC-1 MDL numbers as general.
- **Human description length.** Johnson's link is on 40 tasks and may be reverse-causal (c21).
- **2026 LLM numbers.** Single-author preprints tuned on the public sets, with a model-family judge in Land's case (d08). Treat as upper bounds.
- **Non-ARC tasks.** Nothing here tests MDL selection outside grid puzzles. A length score for a word problem or an open design question has no coding scheme and no measured effect.
- **Scale of the effect on selection.** Where selection loses little (d06), an MDL selector cannot add much, however good it is.

## 10. Open questions

1. Does a length selector beat vote and train-accuracy among fitting LLM programs at matched cost? No one has run it (K23).
2. Does MADIL replicate? Is there any fork, re-run or extension? The citer list was not retrieved.
3. How does false-positive rate scale with number of examples and rule length in LLM programs? No curve exists (only qualitative reports).
4. Would a flat or learned prior match MADIL's hand-set code lengths? Tests whether the idea or the hand DSL carries the result.
5. Do reasoning-trace length and correctness correlate on ARC-AGI-2? One task example only (d03).
6. How do human rule-description length and model description length correlate? H-ARC collected descriptions and never analysed length (d16).
7. Can an LLM propose useful detours when greedy shortest search stalls (the 21 non-compressive MADIL tasks)? Related results exist (d06, d17) but not on those tasks.
8. What did the ARC Prize 2025 team write-ups use for selection? The report was a summary (d01); team write-ups were not opened.
9. Does a prompt-only analogue of CompressARC ("shortest rule that explains every grid") help when measured by length rather than by structure? Hourglass did not measure length (d11).
10. Does the 2026 gain from refinement loops hold on a private set and under independent re-run?

## 11. Sources

[V] = opened this session (full text or PDF text). [M] = snippet, abstract or summary only. For b23 and a33 on DreamCoder the files disagree, so it is listed [M].

**Core MDL on ARC**
- [V] Ferre (2025) MADIL. https://arxiv.org/abs/2505.01081
- [V] Ferre (2021) First Steps of an Approach to the ARC Challenge based on Descriptive Grid Models and MDL. https://arxiv.org/abs/2112.00848
- [V] Ferre, ARC-MDL repository README (fetched by a summarising tool). https://github.com/sebferre/ARC-MDL
- [V] Liao and Gu (2025) ARC-AGI Without Pretraining (CompressARC). https://arxiv.org/abs/2512.06104

**LLM and neural studies**
- [V] Li et al. (2024) Combining Induction and Transduction for Abstract Reasoning (BARC). https://arxiv.org/abs/2411.02272
- [V] Akyurek et al. (2024) The Surprising Effectiveness of Test-Time Training for Few-Shot Learning. https://arxiv.org/abs/2411.07279
- [V] Franzen et al. (2025) Product of Experts with LLMs. https://arxiv.org/abs/2505.07859
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660
- [V] Butt et al. (2024) CodeIt. https://arxiv.org/abs/2402.04858
- [V] Ouellette (2024) Towards Efficient Neurally-Guided Program Induction for ARC-AGI (GridCoder). https://arxiv.org/abs/2411.17708
- [V] Ouellette (2025) Out-of-Distribution Generalization in the ARC-AGI Domain. https://arxiv.org/abs/2507.15877
- [V] Xu, Khalil, Sanner (2023) ARGA. https://arxiv.org/abs/2210.09880
- [V] Pourcel, Colas, Oudeyer (2025) SOAR. https://arxiv.org/abs/2507.14172
- [V] Moghe and Chin (2026) Cost-Effective Agent Harnesses for Abstract Reasoning on ARC-AGI-1. https://arxiv.org/abs/2607.06764
- [V] Land (2026) Modality-Driven Search with Holistic Trace Judging for ARC-AGI-2. https://arxiv.org/abs/2606.31543
- [V] Barber et al. (2025) Solomonoff-Inspired Hypothesis Ranking with LLMs. https://arxiv.org/abs/2512.17145
- [V] Zhu (2026) Think Through a Bottleneck: Hourglass Reasoning. https://arxiv.org/abs/2607.11696
- [M] Jolicoeur-Martineau (2025) Less is More: Tiny Recursive Models (abstract and intro). https://arxiv.org/abs/2510.04871
- [M] Cole and Osman (2025) Don't Throw the Baby Out with the Bathwater (abstract). https://arxiv.org/abs/2506.14276
- [M] Macfarlane and Bonnet (2024) Searching Latent Program Spaces (grep lines). https://arxiv.org/abs/2411.08706
- [M] ARCANA 2607.09059 and Combining LLMs and Genetic Search for ARC-AGI-2 2609.27242 (titles and gists). https://arxiv.org/abs/2607.09059

**Humans and benchmark**
- [V] Johnson, Vong, Lake, Gureckis (2021) Fast and flexible: Human program induction in abstract reasoning tasks. https://arxiv.org/abs/2103.05823
- [V] LeGris et al. (2024) H-ARC. https://arxiv.org/abs/2409.01374
- [V] Chollet et al. (2025) ARC Prize 2024 Technical Report. https://arxiv.org/abs/2412.04604
- [V] Chollet et al. (2026) ARC Prize 2025 Technical Report. https://arxiv.org/abs/2601.10904
- [V] ARC-AGI-2 (2025/2026). https://arxiv.org/abs/2505.11831
- [V] Vahdati et al. (2026) The ARC of Progress towards AGI: A Living Survey. https://arxiv.org/abs/2603.13372
- [V] Semantic Scholar citation listing for CompressARC. https://api.semanticscholar.org/graph/v1/paper/arXiv:2512.06104/citations

**Theory**
- [V] Chollet (2019) On the Measure of Intelligence. https://arxiv.org/abs/1911.01547
- [V] Grunwald (2004) A tutorial introduction to the MDL principle. https://arxiv.org/abs/math/0406077
- [M] Ellis et al. (2020) DreamCoder. https://arxiv.org/abs/2006.08381
- [M] Hodel (2024) Addressing the ARC via Procedural Example Generation (re-arc; opening and abstract only). https://arxiv.org/abs/2404.07353

**Overlaps with other documents.** Wrong-but-fitting programs and held-out checks overlap with the series documents behind G3. Selection and voting overlap with the series on voting and sampling behind G4 and G5. Do not repeat them. Parallel subfields in this run with links: Generation versus evaluation, Plans and schemas, Structure mapping (SME), Functional decomposition, Planning by tree search with pruning, Diagnosticity of evidence.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 11 established claims: 8 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C11.08-K08** (number corrected). 56.75% is the ARC-Potpourri ensemble (TTT+reranking), not ARC-Heavy; on ARC-Potpourri the best single method is 43.00% (transduction TTT+reranking), and on ARC-Heavy the ensemble is 43.25% vs 30.50% best single (induction); the 43.25% in the claim is the ARC-Heavy ensemble, not a best single. Corrected claim: Induction (program) and transduction (direct output) solve different tasks, with solved sets stable across seeds; ensembling beats either: on ARC-Potpourri validation the BARC ensemble reaches 56.75% vs 43.00% for the best single method (transduction with TTT and reranking), and on ARC-Heavy 43.25% vs 30.50% for the best single (induction).
- **C11.08-K14** (reworded: the sources support less). Numbers match (Icecuber 17.0 to 1.6, o3 medium 53.0 to 3.0, ARChitects 56.0 to 2.5; pooled 2020 entries 49%), but only Icecuber is a brute-force DSL search system; o3 and ARChitects are LLM-based, so the sentence 'search-over-DSL approaches collapse' is wider than the evidence. Corrected claim: On ARC-AGI-2 the 2020 brute-force program-search winner Icecuber fell from 17.0% (ARC-AGI-1 semi-private) to 1.6%, and the LLM-based systems fell as well (o3 medium 53.0% to 3.0%, ARChitects 56.0% to 2.5%); ARC-AGI-2 was designed to be less brute-forcible, and the pooled 2020 Kaggle entries solved 49% of the private ARC-AGI-1 set.
- **C11.08-K24** (reworded: the sources support less). SOAR (filter programs whose outputs appear as literals) and Hourglass (anti-patching, no colour special cases in prompts) match, but Moghe and Chin do not require all training pairs exact; they rank by partial training exact-match score (full accuracy is only an exit condition) and dedup by test output. Corrected claim: Guards against fit-but-wrong in LLM programs that are in use (the existence of the guards is established; their effect is not): filter programs whose training outputs appear as literals in the code (SOAR); forbid colour-keyed special cases and if-else patches in repair prompts (Hourglass); rank candidates by training-pair exact-match score and dedup by predicted test output (Moghe and Chin). None is ablated alone, so effect sizes are unknown.
