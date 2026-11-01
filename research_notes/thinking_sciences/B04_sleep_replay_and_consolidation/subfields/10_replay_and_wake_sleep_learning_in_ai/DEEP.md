# Replay and wake-sleep learning in AI: deep document

*Subfield B04.10. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K30), critique.md in this folder. Evidence ids (a01 ... d20) refer to those files. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Overlaps are covered elsewhere: complementary learning systems (B04 subfield 08), replay as offline simulation / Dyna (parallel subfield), prioritised memory access, relevance-based fate of memories, hierarchical planning and subgoal discovery, test-time compute scaling, case-based reasoning. This document links to them and does not repeat them.*

---

## 1. What it is

A wake-sleep loop has three phases that repeat.

1. **Wake.** The system tries to solve tasks. It searches, guided by a model of what usually works.
2. **Abstraction sleep.** It looks at the solutions it found and pulls out the pieces that recur. These become new named building blocks in a **library**. Later search can use one block as a single step.
3. **Dreaming.** It trains its search guide (a recognition network) on two kinds of data: **replays** of tasks it already solved, and **fantasies**, made-up tasks sampled from the current library. The guide learns which blocks to try first.

The best-known system is DreamCoder (Ellis et al. 2021). It works on program synthesis. The library is a set of functions in a typed lambda calculus. The guide is a neural net.

The subfield also covers the older neural wake-sleep algorithm (Hinton et al. 1995), replay in reinforcement learning (experience replay, prioritised replay), generative replay in continual learning, and the 2023-2026 wave of LLM systems that copy the shape of the loop without training anything: LILO, ReGAL, Voyager, TroVE, Agent Workflow Memory, ASI, SkillWeaver, ReasoningBank, Dynamic Cheatsheet, ACE and sleep-time compute.

**Why it matters for our agent.** Our agent is a scaffold with no weight updates. Its schema has a planned **subgoal library** (SCHEMA.md section 5, marked [D]) and a lesson memory written at S9. This subfield asks: can a wake / abstract / practice cycle grow that library, and does it pay for its tokens? The short answer from the research: it pays on structured, checkable domains and often does not on open reasoning. The agent cannot run the "dreaming" phase as written, because it has no net to train. It can run a no-weights analogue.

---

## 2. History and theories in depth

### 2.1 Neural wake-sleep (1995 to 2019)

- **Helmholtz machine** (Dayan, Hinton, Neal, Zemel 1995) [M]. Perception is inference in a generative model. A second network, the recognition model, learns to invert it.
- **Wake-sleep algorithm** (Hinton, Dayan, Frey, Neal 1995) [M]. Wake: the recognition net proposes latent causes for real data and the generative net learns to reproduce the data. Sleep: the generative net "dreams" data from its own latents and the recognition net learns to recover the latents. Two networks train each other with local rules.
- **Known flaw.** The sleep phase minimises a KL divergence in the wrong direction. It is not a bound on likelihood (a08, b21).
- **Reweighted wake-sleep** (Bornschein and Bengio 2015, a08/b21). Reads wake-sleep as importance sampling with the recognition net as the proposal. Original wake-sleep is the case of one sample (K=1). More samples (K=5 in training, K=100,000 for the test estimate) give a less biased gradient. A stronger recognition layer (NADE) beats a sigmoid belief net. The gradient is still biased in log space.
- **Revisiting RWS** (Le et al. 2019, b22). Beats variational objectives for models with discrete branching. It has one failure mode: a local optimum where the model's support (values 0-9 in their test) is never widened, because the model trains only on samples from its own guide. Wake-sleep and wake-wake suffered more than the VIMCO variants. *Analogue for a library:* dreams made only from the current library can never reach beyond what the library already spans.

### 2.2 Replay in reinforcement learning and continual learning

- **Experience replay** (Mnih et al. 2013, a20). Store transitions and update on random minibatches to break correlation. Beat prior methods on 6 of 7 Atari games and a human expert on 3.
- **Prioritised replay** (Schaul et al. 2016, a21/c23). Replay in proportion to TD error. Beats uniform replay on 41 of 49 Atari games. DQN median normalised score 48% to 106%.
- **Generative replay** (Shin et al. 2017, a22/b23). A generator produces pseudo-data of old tasks so the solver keeps them. Replaying random noise did not help. Replaying generated samples did.
- **Three scenarios** (van de Ven and Tolias 2019, b24). On split MNIST with 20 seeds, replay was the only family that worked when task identity is unknown. Regularisation (EWC, LwF) failed there.
- **Biologically inspired sleep** (Krishnan et al. 2019, b26). A spiking sleep phase recovered lost tasks in a toy case. Forward transfer appeared only about half the time.
- **Link to biology.** All of this is inspired by hippocampal replay and complementary learning systems (McClelland et al. 1995 [M], covered in subfield 08).

### 2.3 DreamCoder and program library learning (2018 to 2023)

- **Predecessor** (Ellis et al. 2018, NeurIPS) [M]. Library learning plus neural guidance.
- **DreamCoder** (Ellis et al. 2021, arXiv 2006.08381, a01-a06). The first full three-phase cycle with a growing library. Details in section 4.
- **LAPS** (Wong et al. 2021/2022, b07, c05). Adds natural-language task descriptions to the loop. Preprint 2021, ICML 2022.
- **Stitch** (Bowers et al. 2023 POPL, a10, b04, c09). Replaces DreamCoder's rewrite-based abstraction step with top-down corpus-guided search. 3-4 orders of magnitude faster, 2 orders less memory.

### 2.4 LLM library learners (2023 to 2026)

The LLM replaces the neural guide and often the enumerative search. The dreaming phase disappears (a26: no LLM system read here trains on fantasies).

- **Voyager** (Wang et al. 2023, a14, b16, c15). Minecraft. A skill library of verified code.
- **LILO** (Grand et al. 2024 ICLR, a11-a13, b05, b06, c08, d19, d20). LLM solves, Stitch compresses, AutoDoc has the LLM name and document each abstraction.
- **ReGAL** (Stengel-Eskin et al. 2024, a15, a16, b08, b09, c10, c11, d18). Gradient-free refactoring into verified helper functions.
- **TroVE** (Wang, Neubig, Fried 2024, a17, b10, b11, c12). Training-free toolbox that grows and is trimmed.
- **CRAFT** (Yuan et al. 2023, b27, c20) [M, abstract level]. Tool sets built from validated solutions.
- **Audit** (Berlot-Attwell et al. 2024, a18, a19, b12, b13). Library learning "doesn't": reuse is almost zero in LEGO-Prover and TroVE.
- **Agent memories:** Agent Workflow Memory (b14, b15, c16), ASI (d01, d02), SkillWeaver (d11), ExpeL (c19, d17), ReasoningBank (c17, d03, d04), Dynamic Cheatsheet (c18, d05, d06), ACE (d12, d13), Memento (d16).
- **Offline thinking:** sleep-time compute (Lin et al. 2025, b17, b18, c21, c22, d07, d08). SOAR (Pourcel et al. 2025, b19, b20), which needs weight updates.
- **Skills benchmarks:** SkillsBench (d09, d10), a skill-selection scaling study (Li 2026, d14, d15).

### 2.5 Competing explanations for why these loops help

1. **Real reuse.** Learned blocks shorten later solutions. (Supported in DreamCoder, LOGO, Minecraft.)
2. **Better prompt format only.** The memory carries instructions and examples that would help even if empty. (Dynamic Cheatsheet's empty-memory arm gets about half of Claude's AIME gain, d05.)
3. **More samples and self-correction.** The loop gives the model more tries and feedback. (TroVE, LEGO-Prover audit, a18/b13.)
4. **A better guide, not a better library.** DreamCoder ablations say both parts matter, but all numbers come from one lab.

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| DreamCoder lifts text editing a lot | Trained on 128 generated tasks, tested on 108 SyGuS 2017 problems. 10-min limit: 3.7% solved (mean 235 s) before learning, 79.6% (mean 40 s) after. CVC4 (1 h, 8 CPUs) 82.4%; DreamCoder with same budget 84.3% | a02, b01, c01 | [S] K01 |
| DreamCoder across six domains | Full model best on held-out tasks in every domain. LOGO graphics and towers: no alternative above 60%, DreamCoder near 100%. Mean solve time 54.1 s, median 15.0 s. 5 runs per bar | a04, b02, c02 | [S] K01 |
| Both sleep phases and compression matter | Removing library growth or the recognition net lowers held-out solves. Memorise-whole-solutions baselines do worse. Per-arm bar values not read | a04, b02, c02 | [S] K02 |
| Library depth tracks tasks solved | r = 0.79. List domain: 218 tasks, 50/50 split, 15 examples each, about 20 new routines (filter, max, nth largest, sort, each built on the last) | a03, a04, b02 | [S] K03; correlation, not causal |
| Learning a field from near scratch | 93% of 60 physics laws after 8 cycles. Lisp bootstrap: 20 of 20 tasks after about 5 days on 64 CPUs. Origami basis about one CPU-year | a06, b03, c03, c04 | [S] |
| DreamCoder is expensive | About a day on 20-100 CPUs per domain. Enumeration baseline: 24 h per task, up to 400 million programs | a01, a04, b03, c04 | [S] K04 |
| Dreams become structured | After 20 cycles dreams recombine learned concepts. Recognition-net task similarity matches solution code (p < 1e-4, chi-square). LOGO 160 images, towers 107 tasks | a05 | [S] |
| Stitch replaces DreamCoder's abstraction step | 3-4 orders of magnitude faster, 2 orders less memory. Compression 2.55x-11.57x in 0.19-60.16 s. Under 2% of the compute recovers most gain. Measures compression, not solve rate | a10, b04, c09 | [S] K05 |
| Language helps the loop (LAPS) | Held-out solved, DreamCoder vs LAPS best: strings 33.4 vs 52.2-57.0 (best 54.60); graphics best run 49.55 vs 98.19 (seed mean 42.64 vs 81.98); scenes 67.8-73.9 vs 95.6-95.9. Human-written language: graphics 58.55 vs 89.20 synthetic | b07, c05 | [S] K06; best runs overstate |
| LILO vs DreamCoder vs plain LLM | Mean test solve over 3 seeds (REGEX / CLEVR / LOGO): DreamCoder 43.93 / 94.50 / 28.53; LLM solver 76.13 / 88.67 / 32.13; LLM solver + search 76.60 / 96.44 / 37.84; LILO 77.07 / 96.76 / 48.95. LILO max 93.20 / 99.03 / 73.87; LOGO std 9.46 | a11, b05, d19 | [S] K08 |
| LILO's gain over the matched no-library arm is small | +0.47 REGEX (SD 13.02 vs 1.50), +0.32 CLEVR, +11.11 LOGO (about 1 SD) | d19 | [S]; weakens K08 |
| Unnamed abstractions hurt an LLM | Stitch alone vs plain LLM: -30.60 REGEX, -2.91 CLEVR, -11.11 LOGO. AutoDoc names recover +9.73, +2.27, +0.00 | a12, b06 | [S] K07 |
| LLM-proposed abstractions are mostly invalid | 998 of 5250 valid (19.01%): REGEX 24.93%, CLEVR 24.20%, LOGO 4.93%. Similar direction in ASI: 15.6% of induction turns pass verification | b06, d02 | [S] K09 |
| Libraries learned in the loop beat post-hoc ones | Offline enumeration with the final library vs base DSL: DreamCoder +19.6 REGEX, +62.46 CLEVR, +29.73 LOGO; LILO +42.27, +63.43, +43.24 | c08 | [S] |
| Build cost per LILO round | 0.8M to 1.2M GPT tokens per iteration, no clear difference by condition; one LLM round about 48 CPU-hours of DreamCoder search (authors' estimate) | d20, a12 | [S] K30 |
| ReGAL helps weaker open models | CodeLlama-13B test: LOGO 45.6 to 57.1, Date 42.8 to 68.9, TextCraft 18.8 to 26.9. CodeLlama-13B beats GPT-3.5 without abstractions by 19.2 points on LOGO. CodeLlama-34B TextCraft 22.2 to 30.8. About 200 training examples | a15, b08, c10 | [S] K10 |
| ReGAL gains vanish for strong models and some cases | GPT-3.5 Date 88.9 to 90.2; CodeLlama-7B LOGO 34.5 to 34.5; Lemur-70B MATH 14.0 to 13.1; CodeLlama-13B TabMWP 29.1 to 27.9. Under distribution shift +3.6% | b08, b09 | [S] |
| ReGAL ablations (dev, CodeLlama-13B) | Full / no curriculum: LOGO 55.0 / 36.3, Date 77.0 / 56.6, TextCraft 34.12 / 28.78. No retry 48.3 / 51.9 / 30.43; no prune 52.0 / 65.5 / 25.26; no edit 53.3 / 69.6 / 27.35 | a16, c11, d18 | [S] K11 |
| Voyager's library | 63 unique items (3.3x), 2.3x distance, wood 15.3x, stone 8.5x, iron 6.4x faster, only agent to reach diamond. Random curriculum -93% items; no self-verification -73%; GPT-3.5 gives 5.7x fewer. Without library, plateau later | a14, b16, c15 | [S] K12 |
| Reuse is near zero in math libraries | LEGO-Prover: over 20,000 lemmas, 1,233 (6%) reached the prover, one lemma reused once. TroVE: 15 functions, 3 successful reuses in 3,201 MATH questions | a18, b12, b13 | [S] K13 |
| No-library ablation matches or beats TroVE | Counting 0.236 vs 0.250, geometry 0.058 vs 0.050, intermediate algebra 0.120 vs 0.134, number 0.258 vs 0.290 (TroVE vs no reuse; ablation wins 3 of 4). LEGO-Prover valid+GPT 127, valid+Human 135, test+GPT 111, test+Human 122 | a19, b12, b13, c13 | [S] K13 |
| TroVE's own claim | 11 datasets, toolboxes 79-98% smaller, humans verify 31% faster, 13% more accurately. With GPT-4: TroVE 0.72/16, 0.92/38, 0.44/8 (accuracy/size) vs CRAFT 0.68/282, 0.88/181, 0.45/525 | a17, b10, b11 | [C] |
| Agent Workflow Memory | WebArena +12.0 points absolute (51.1% relative); +7.6% relative over human-written workflows (SteP); Mind2Web step success +24.6% relative; margin over baselines grew from 8.9 to 14.0 as train-test distance widened | b14, c16 | [S] K14 |
| Workflows as callable actions barely help | +1.3 step success; called in only 18.5% of tasks | b15, c16 | [S] K14 |
| Verified skills beat unverified | WebArena shopping, Claude: unverified text 32.6, verified program 36.4, verified text 39.0, verified program as action 40.1. Whole WebArena (812 tasks): vanilla 32.7 (5.6 steps), AWM 36.3 (5.9), ASI 40.4 (5.0). Verification alone +4.2 | d01, d02 | [S] K23 |
| Failures help only as lessons | ReasoningBank 46.5 to 49.7 with failures; AWM 44.4 to 42.2; Synapse 40.6 to 41.7 (Gemini-2.5-flash, shopping; no memory 39.0). Full WebArena 684 tasks: none 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8, +MaTTS 51.8 | c17, d03 | [S] K24 |
| Memory items injected must stay few | ReasoningBank best at the smallest setting 49.7, 45.5 with 3, 44.4 with 4. Memento: K=0 59.9 F1, K=1 63.6, K=4 64.5 (best), K=32 63.9 | d04, d16 | [E] K25 |
| Judge noise is tolerable | ReasoningBank judge accuracy 72.7%; even a random-guess judge gave 47.6 vs 39.0 for no memory | c17, d04 | [S] |
| Memory without weights helps where code or strategy is reusable | Claude AIME 2024 23% to 50%; GPT-4o Game of 24 10% to 99%; Claude Game of 24 12% to 14%; GPQA-Diamond Claude 59.6 to 68.7; GPT-4o GPQA 57.1 to 57.1, MMLU-Pro Engineering 53.2 to 51.2. ExpeL ALFWorld retrieve-only 40.3 to 54.4 | c18, c19, d05, d06 | [E] K15 (three families) |
| Dynamic Cheatsheet's empty arm | Claude BL / empty / RS: AIME 2024 23.3 / 36.7 / 46.7 (Cu 50.0); AIME 2025 6.7 / 23.3 / 30.0; GPT-4o Game of 24 10.0 / 19.0 / 99.0. About half of Claude's AIME 2024 gain comes from the prompt alone | d05 | [S]; AIME is 30 questions, one question = 3.3 points |
| Appending all history is worse than curating | Full-history variant 26.7 on one test; retrieval-only Game of 24 6.0 | d06 | [S] |
| Sleep-time compute | Up to +13% (GSM) and +18% (AIME) with more sleep compute; 2.5x lower cost per query with 10 queries per context (test tokens weighted 10x); beats pass@k at equal test tokens; 60 AIME questions; 5 parallel sleep generations beat 10 on GSM. Abstract-level "about 5x" less test compute, not found in body text | b17, c21, d08 | [S] K16 |
| Sleep-time depends on predictability | Gap grows across 5 log-probability quantile bins. In SWE-Features sleep-time wins at low test budgets and loses at high ones | b18, c22, d07 | [S] K16 |
| SOAR (needs weights) | ARC-test 7B 14.25% to 36.25%; 14B 19.87 to 42.75; 32B 25.25 to 44.37; 72B 25.62 to 44.87; Mistral-Large-2 26.25 to 45.5. Majority vote 52.00%, oracle 57.25%. Search alone plateaus after about 5.2k attempts | b19, b20 | [S] K17 |
| Generative replay stops forgetting | MNIST solvers 98.81, 98.64, 98.58, 98.53, 98.56%. Split MNIST Class-IL: none 19.90, EWC 20.01, LwF 23.85, DGR 90.79, DGR+distill 91.79, upper bound 97.94. Domain-IL none 59.21, EWC 63.95, DGR 95.72 | b23, b24 | [E] K18 (weights only) |
| LLM self-written rehearsal | SSR 63.23 vs none 17.33, 1% real 60.64, 10% real 61.49, upper bound 64.69 (Llama-2-7b, 10 SuperNI tasks) | b25 | [S] K19 (weights only) |
| Prioritised replay | 41 of 49 Atari games; DQN median 48% to 106%; Double DQN median 111% to 128% | a21, c23 | [S] K20 |
| Self-written skills lose | SkillsBench v4, 87 tasks: no skills / self-generated / curated, Opus 4.7 43.0 / 34.9 / 61.2, GPT-5.5 46.8 / 35.5 / 66.5, Gemini 3.1 Pro 36.0 / 24.5 / 60.8. Self-gen deltas -8.1, -11.3, -11.5. Early version said about -1.3 | d09 | [S] K27; quote the version |
| Compact, few skills win | Curated gain: 1 skill +18.0, 2-3 skills +19.0, 4+ +10.1 pp. Compact +19.0, standard +21.5, detailed +14.5, comprehensive +0.7 pp. 13 of 87 tasks negative (worst -7.4) | d10 | [S] K27 |
| Flat skill lists break | Above 90% at 20 skills or fewer, about 20% at 200 (GPT-4o-mini and GPT-4o, 3 seeds, synthetic). At 120 skills flat 45% / 63%; two-stage routing 83-85% / 72% | d14, d15 | [S] K26 |
| SkillWeaver practice loop | 160 exploration iterations per site, GPT-4o. WebArena 22.6 to 29.8 (+31.8% relative); live sites 40.2 to 56.2 (+39.8%), Car site 11.1 to 11.1, Flight 11.7 to 29.4. No equal-token control | d11 | [S] K28 |
| Rewrites collapse memory | AppWorld: 18,282 tokens and 66.7 accuracy at step 60 to 122 tokens and 57.1 next step (baseline 63.7). Itemised updates: +10.6% agents, +14.8% without labels; latency -82.3% to -91.5% | d12, d13 | [S] K29 |
| Insight vs trajectory format | Insights-only vs retrieval-only: HotpotQA 36% vs 31%; ALFWorld 50% vs 55%. Both together higher on both | c19, d17 | [S] |
| Wake-sleep theory | Original objective has wrong-direction KL; RWS with more samples better but can stall where support is never widened | a08, b21, b22 | [E] K21 (2 sources) |

---

## 4. Mechanisms and models

### 4.1 DreamCoder, step by step

State: a library L of typed functions (start: primitives), a recognition net Q(program | task), a training set of tasks with a checker.

**Wake.**
1. For each task, run enumerative search over programs built from L. Order the search by Q's probabilities for this task.
2. A program counts as a solution only if it passes the task's examples.
3. Record the best (smallest, by description length) solutions per task as "frontiers".
4. Wake time limit: 10 min per task in the text domain.

**Abstraction sleep.**
1. Take all frontier programs.
2. Search for refactorings: new function definitions that, when substituted, make the whole set of solutions shorter. The score is how much the library plus rewritten solutions shrink (an MDL objective).
3. Add the winning functions to L. Rewrite the frontiers with them.
4. Original DreamCoder did this with version-space rewriting. Stitch (a10) does it top-down: find the pattern that saves the most across the corpus, add it, repeat.

**Dreaming.**
1. Replays: for each solved task, train Q to predict the solution (rewritten with the new library) from the task.
2. Fantasies: sample programs from L, run them to make a task (input-output pairs, an image), and train Q on that pair. Fantasies are free data with known answers.
3. Result: Q learns which blocks go with which task features. Dreams show learned concepts recombined (a05).

**Loop.** 8 to 20 cycles per domain. Train/test split 50/50 in most domains (a03, a05).

### 4.2 What the engineer should take from the structure

- The **library step is compression**: keep a block only if it shortens the total description of solutions. Reuse is the objective.
- The **guide step is learning where to look** given the task. Without a net, an LLM does this by reading the task and the library listing.
- **Fantasies** give training data when real data is scarce. Without weights, the only analogue is to generate practice problems from the library, solve them, and keep what passes a check (SkillWeaver, d11).

### 4.3 LILO (LLM version)

1. Wake: LLM solver writes programs, given examples plus retrieved library entries; optionally followed by enumerative search.
2. Abstraction: Stitch finds blocks.
3. AutoDoc: LLM names and writes a docstring for each block (gpt-3.5 or gpt-4 for this step).
4. Next wake: the named blocks are in the prompt.
5. Key detail: unnamed blocks hurt (-30.60 REGEX). Names and docs are what let the LLM read the library.
6. Cost: 0.8M-1.2M tokens per iteration (d20).

### 4.4 ReGAL (gradient-free, LLM-only)

1. Cluster training examples. Order clusters shortest query first (the curriculum).
2. LLM refactors a batch of solved programs into helper functions.
3. **Verify by execution** that the rewritten programs give the same output. Keep only passing helpers.
4. Retry failed refactors.
5. Prune helpers that never get used, and edit helpers that fail on new data.
6. The final code bank is given to the solver in the prompt.

Each step has an ablation (a16, d18). Curriculum and retry were the largest effects.

### 4.5 Memory-style variants (no explicit abstraction step)

- **AWM:** induce workflows from episodes (offline from training data or online from the agent's own results), store as text. Online beats offline as the train-test gap widens.
- **ASI:** write the skill as a program, run it on the same task to verify, keep it if it passes. Only 15.6% of turns pass.
- **ReasoningBank:** after each episode an LLM judge labels success or failure and writes a short lesson. Retrieve a small number of items by similarity.
- **Dynamic Cheatsheet:** one text sheet, rewritten after each question (curation), with code snippets.
- **ACE:** playbook as itemised bullets; a reflector proposes small deltas; non-LLM code merges them. No call rewrites the whole playbook.
- **Memento:** case bank of past successes and failures with similarity retrieval, K around 4.
- **Sleep-time compute:** before the question arrives, the model reads the context and writes notes (inferences, likely sub-results). At question time the notes are in the prompt.

### 4.6 Replay for scheduling

Prioritised replay (a21): sample item i with probability proportional to its error |delta_i|^alpha, and correct the bias with importance weights. For our agent: pick which library entries to re-verify or which past failures to revisit by failure rate or surprise.

---

## 5. What holds up

**Replications.** Almost none that are independent.
- DreamCoder's numbers come from one paper. LAPS, LILO and Stitch share authors and code with DreamCoder, so they extend it and do not replicate it (critique.md).
- ReGAL, AWM, ASI and Dynamic Cheatsheet gains are author-reported, on different benchmarks and models.
- **Independent agreement:** generative replay (Shin 2017 and van de Ven 2019 agree on direction, [E]); memory without weights helping on reusable-strategy tasks (Dynamic Cheatsheet, ExpeL, ReasoningBank, [E]); few memory items (ReasoningBank, Memento, [E]); wake-sleep theory (Bornschein and Le, [E]).

**Failures and nulls.**
- **Library learning in math:** LEGO-Prover 1 reuse in over 20,000 lemmas; TroVE 3 reuses in 3,201 questions; no-library ablation equal or better on 3 of 4 splits (a18, a19, b13).
- **LILO vs matched no-library solver:** within 0.5 points on REGEX and CLEVR. Only LOGO shows +11.1, about 1 SD (d19).
- **LAPS vs LILO on LOGO:** LAPS best 92.79 beats LILO best 73.87, so LILO does not beat LAPS there (critique.md).
- **ReGAL on strong models and shifts:** GPT-3.5 Date +1.3; shift gain only +3.6%; 7B LOGO 0; Lemur-70B drop (b08, b09).
- **Self-written skills:** 8 to 11.5 points below no skills (d09). Not a loop with verification, but shows what happens without it.
- **Raw routines from failures:** AWM falls from 44.4 to 42.2 when failures are added (d03).
- **Dynamic Cheatsheet on knowledge tasks:** GPT-4o GPQA unchanged, MMLU-Pro Engineering 53.2 to 51.2; Claude Game of 24 only 12% to 14% (d06).
- **Workflows as actions:** +1.3, called 18.5% of the time (b15).
- **Memory rewrite collapse:** 18,282 tokens to 122 (d12).

**Moderators that seem to matter.**
1. **Shared structure and a verifier.** Gains where tasks share structure and a checker exists (LOGO, REGEX, Minecraft, Game of 24, WebArena). [C] K22: no paper tests the structure claim directly.
2. **Model strength.** Gains shrink for stronger models (ReGAL GPT-3.5 Date). Strong models gain from the prompt format alone (d05).
3. **Verification.** +4.2 points (ASI). But the random-guess judge in ReasoningBank kept most of the gain, so the lesson-writing step may matter more than the check (d04).
4. **Documentation.** Unnamed abstractions hurt an LLM; names recover part (a12).
5. **Entry format.** Verified text beat verified program as memory (39.0 vs 36.4); program wins as callable action (40.1) (d01). Insights vs trajectories split by task (d17).
6. **Library size.** Flat in-prompt lists fall from above 90% at 20 skills to about 20% at 200; near-duplicates are the main cause (d14, d15). Similarity retrieval plateaus rather than collapses (Memento K=32 only 0.6 F1 lower).
7. **Query predictability** (sleep-time compute).
8. **Curriculum.** Short to long order helps in 3 code domains (removing it costs LOGO -18.7, Date -20.4, TextCraft -5.3).

**Interventions that worked:** execution verification before keeping, short-to-long curriculum, retry of failed refactors, pruning, names and docstrings, itemised delta updates, curated focused 1-3 skill packs, abstract lessons from failures, few retrieved items, sleep-time notes when queries are predictable.

**Interventions that did not:** unnamed abstractions, whole-library rewrites, self-written skill packs without a check, raw failed routines, exhaustive long skills, full-history append, workflows offered as actions, more parallel sleep generations beyond about 5.

**Critique-flagged cautions.** The a08 table was garbled (sleep-only vs wake-only nats are unsafe to quote). "Date 45.6 vs 57.1" is wrong: 45.6 to 57.1 is LOGO; Date is 42.8 to 68.9. Test numbers and dev numbers must not be compared. Several sources are preprints from authors of the methods they test. ASI, ReasoningBank and Dynamic Cheatsheet report single runs with no variance.

---

## 6. Language models

**What the LLM does in the loop.** It replaces the neural guide (and sometimes enumeration). It does solving, refactoring, naming and lesson writing. It does not train. So the "dreaming" phase has no LLM test (a26). The nearest analogues are SkillWeaver practice (+31.8% and +39.8% relative, no equal-token control) and sleep-time compute (precomputed notes).

**By how much.**

| Setting | Effect | Source |
|---|---|---|
| LOGO, Codex | +11.11 over matched no-library solver (48.95 vs 37.84), about 1 SD | d19 |
| REGEX, CLEVR, Codex | +0.47, +0.32 over matched no-library solver | d19 |
| CodeLlama-13B refactoring | +11.5 LOGO, +26.1 Date, +8.1 TextCraft | b08 |
| GPT-3.5 refactoring | LOGO 36.9 to 49.3, MATH 43.2 to 55.4, Date 88.9 to 90.2 | b08 |
| Frontier agents, own skills | -8.1 to -11.5 vs none | d09 |
| Frontier agents, curated skills | +18 to +25 | d09 |
| Claude 3.5 Sonnet, cheatsheet | AIME 2024 23.3 to 50.0, but 36.7 with an empty cheatsheet | d05 |
| GPT-4o, cheatsheet | Game of 24 10.0 to 99.0 (empty 19.0) | d05 |
| Web agents | AWM +12.0 absolute; ASI 32.7 to 40.4; ReasoningBank 40.5 to 48.8 | b14, d02, d03 |
| Sleep-time compute | up to +13% GSM, +18% AIME; 2.5x cost per query at 10 queries | b17, d08 |

**What changed results.**
- Adding docstrings: +9.73 on REGEX (LILO).
- Verification: +4.2 (ASI).
- Lesson format: failures as lessons +3.2 (ReasoningBank shopping), as raw routines -2.2 (AWM).
- Curriculum: the biggest ReGAL ablation on LOGO and Date.
- Retrieval count: one item beat four by 5.3 points (49.7 vs 44.4, ReasoningBank).
- Update style: a full rewrite lost 9.6 points (66.7 to 57.1) and collapsed the context; delta updates gained +10.6%.

**Model-strength pattern.** Weak and open models gain from libraries. Strong models gain little from libraries and a good share of what they gain may come from the prompt (d05). Frontier agents writing their own skills do worse than none (d09). No one has run LILO, ReGAL or AWM with a current frontier model against a matched no-library arm.

**Cost.** Build cost is known: about 1M tokens per LILO iteration. The reuse benefit in tokens is reported nowhere (K30). Sleep-time compute is the only study with an amortised cost model, and it assumes test tokens cost 10x.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Inject at most a few library or lesson entries per step (1 to 4; start at 2). Memory text counts in the token budget | memory, G7 | [E] | K25: d04, d16 |
| Memory without weights can help, but test it on the class first: gains are large where reusable strategy or code exists, near zero on knowledge tasks and for strong models on some tasks. Gate by measured class pass rate, not by assumption | memory, S0, G7 | [E] | K15: c17, c18, c19, d05, d06, d03, d12 |
| Always run a plain arm at equal tokens against any library (existing rule G7). Add: log per-entry reuse count so unused entries get pruned | G7, memory | [E] for the rule; reuse logging [S] | K13, K22 |
| Background only: a dream built only from the current library cannot widen its reach. Do not rely on library-only practice problems to find new ground | memory | [E] (theory) | K21: a08, b21, b22 |

K18 (generative replay), K19 and K20 (weights, RL) are background and add nothing to the scaffold. K17 (SOAR) needs weights.

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| **Verify before keeping.** A library entry enters only after the agent re-solves a held-out problem with it, checked by code | memory, G3 | [S] | K09, K23: b06, d01, d02 |
| **Short text rules with a name and a one-line use.** Not raw code, not unnamed compressions | memory | [S] | K07, K23: a12, d01 |
| **Wake-sleep cycle for the subgoal library.** After a batch of solved subgoals, a sleep step compresses recurring solutions into named entries; the library is then offered by similarity | memory, O3, S6, S9 | [S] / [C] | K01, K08, K13, K22 |
| **Dreaming analogue.** Make variants of a library entry's problem, solve, keep those that pass a check; use as practice and as a test of the entry | memory, O | [S] | K28: d11 |
| **Short-to-long ordering** when building the library | memory | [S] | K11: d18 |
| **Itemised updates only.** Add, edit, remove one entry per call; never rewrite the whole library | memory, G7 | [S] | K29: d12, d13 |
| **Failure lessons.** One line per failure: tried, why it failed, what to do instead. No raw traces | memory, S9 | [S] | K24: d03 |
| **Cap and route.** Cap a flat library at a few dozen; merge near-duplicates in sleep; route by group first | memory | [S] | K26: d14, d15 |
| **Sleep-time notes.** Precompute notes on a shared context before the question; count tokens | memory, S1/S2 | [S] | K16: b17, d07, d08 |
| **Hindsight relabelling.** Store a failed attempt as a solution to the problem it actually solved | memory | [S] | K17: b19 |
| **Prioritise rehearsal** of entries by failure rate or surprise | memory | [S] | K20: a21 |
| **Reuse-rate gate.** Switch the library on only for problem classes where measured reuse and pass rate justify it | S0 | [C] | K22, K30 |

The agent should not take: self-written skill packs written before the task (d09), workflows as callable actions as the only route (b15), whole-library rewrites (d12).

---

## 8. Concrete tests on our bench

All arms at equal total tokens, including wake, sleep and practice tokens. Report the mean over at least 3 seeds with SD. Flag any gain smaller than 1 SD.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style and BrainTeaser items with a checker; library built on a train split, tested on a held-out split | (a) plain scaffold; (b) plain scaffold plus extra samples to match tokens; (c) library built by wake-sleep (verified, named entries); (d) library without verification | held-out pass rate; tokens per solved item; per-entry reuse count | (c) over (b) by at least 3 points on structured classes; (d) below (c) by about 4 (ASI +4.2); null on classes with reuse near 0 |
| T2 | Same items | Entry format: name plus one-line rule; worked example; code only; no library | pass rate at equal tokens | name plus rule at least as good as code (d01, d17); size of gap unknown |
| T3 | Same items | Number of injected entries: 0, 1, 2, 4, 8 | pass rate; tokens | peak at 1 to 4, flat or lower beyond (d04, d16) |
| T4 | Mixed classes | Sleep step: delta updates vs full rewrite of the library | pass rate; library size over cycles | rewrite loses 5 or more points once the library is over about 10 entries (d12) |
| T5 | Library-building order | Short-to-long vs random vs long-to-short | held-out pass rate after build | short-to-long better by 5+ points (d18) |
| T6 | Dreaming analogue | (a) library entries only; (b) library plus verified practice variants; (c) matched extra real-task attempts | held-out pass rate at equal tokens | (b) over (c) only if the verifier is reliable (d11 had no such control) |
| T7 | Sleep-time notes | Precompute notes on a shared context vs more test-time thinking; bins of question predictability | pass rate; tokens per query | notes win at low budgets and for predictable questions; lose at high budgets (d07) |
| T8 | Failure memory | No failures; raw failed traces; one-line lessons; hindsight relabelling | pass rate on later items | one-line lessons over no failures by 2 to 3 points; raw traces null or negative (d03) |
| T9 | Break-even | Log tokens spent on wake plus sleep, tokens saved per reuse, number of reuses | break-even number of reuses | no prior number; first measurement |
| T10 | Library size | 10, 20, 40, 80 entries, flat vs group-first routing, with and without near-duplicates | selection accuracy; pass rate | flat drops past 20 to 30; routing restores (d14, d15) |
| T11 | Strong vs weak model | Same T1 on the strongest and a weaker model | gain by model | gain smaller on the strong model (b08) |

---

## 9. What does not transfer, and why

- **The dreaming phase as trained.** It trains a net on replays and fantasies. We have no weights to update. SOAR, SSR and generative replay all train (K17, K18, K19).
- **Catastrophic forgetting.** The reason for replay in continual learning. A scaffold cannot forget weights. Its failure mode is different: a stale or noisy library, or too many entries (d12, d14).
- **Typed DSLs.** DreamCoder and Stitch compress programs in a lambda calculus with a verifier on every task. Open reasoning steps have no formal language and no cheap equality check, so compression by pattern mining does not directly apply.
- **Program-level verification.** ReGAL verifies that refactored code gives the same output. For reasoning steps there is no such check. No verifier for non-code reasoning steps was found (K30).
- **Scale of compute.** DreamCoder needs a day on 20-100 CPUs. LILO needs 1M tokens per round. A single-task scaffold under a token budget cannot afford to build a library per problem. It pays only if entries are reused across many problems (K04, K30).
- **Domains with a fixed vocabulary.** LOGO, towers, regexes and scene queries have natural reusable pieces. Open or one-off problems do not (K22; math libraries showed near-zero reuse).
- **Web agent results.** WebArena tasks repeat site structure. The effect may come from repeated page layout and not from reasoning (K14, K23).
- **Neural wake-sleep as a probabilistic model.** The KL and importance-sampling story concerns latent-variable nets, not scaffolds (K21).
- **Biological sleep.** Subfield 08 covers it. Incubation by "sleeping on it" is already in SCHEMA 4b as not to add.

---

## 10. Open questions

1. Does a no-library arm with equal tokens match library loops for a frontier LLM? Never run for ReGAL, AWM or a frontier-model LILO.
2. What reuse rate per task pays for the wake and sleep tokens? No paper reports tokens saved per reuse.
3. Which entry format is best at read time: name plus docstring, worked example, or code? Not compared directly.
4. Has any unrelated lab replicated DreamCoder-style gains on open-ended reasoning? Nothing found.
5. Can verify-before-keeping fix the 19% valid-abstraction rate, and what is the verifier for reasoning steps? ReasoningBank's random-guess judge result suggests lesson writing may matter more than checking.
6. Does a no-weights dreaming step help at equal tokens? SkillWeaver has no control.
7. Hindsight relabelling vs abstract lessons: which gives more gain per stored item?
8. At what library size does retrieval noise cost accuracy for a reasoning scaffold?
9. Does short-to-long order hold outside code domains?
10. Can the agent predict whether sleep-time notes will help before paying for them? A log-probability scorer is the only measured predictor.
11. Do structure and a verifier really explain when libraries help? No paper tests it directly (K22).
12. Do cheatsheet-style gains for strong models come from the library or from the format prompt? (d05: about half is format for Claude on AIME.)

---

## 11. Sources

[V] = opened and read this session. [M] = snippet or abstract only.

**Wake-sleep theory**
- [M] Hinton, Dayan, Frey, Neal (1995) The wake-sleep algorithm for unsupervised neural networks. https://www.cs.toronto.edu/~hinton/absps/ws.pdf
- [M] Dayan, Hinton, Neal, Zemel (1995) The Helmholtz machine. https://www.cs.toronto.edu/~hinton/absps/helmholtz.pdf
- [V] Bornschein and Bengio (2015) Reweighted wake-sleep. https://arxiv.org/abs/1406.2751
- [V] Le, Kosiorek, Siddharth, Teh, Wood (2019) Revisiting reweighted wake-sleep. https://arxiv.org/abs/1805.10469

**Replay in RL and continual learning**
- [V] Mnih et al. (2013) Playing Atari with deep RL. https://arxiv.org/abs/1312.5602
- [V] Schaul et al. (2016) Prioritized experience replay. https://arxiv.org/abs/1511.05952
- [V] Shin, Lee, Kim, Kim (2017) Continual learning with deep generative replay. https://arxiv.org/abs/1705.08690
- [V] van de Ven and Tolias (2019) Three scenarios for continual learning. https://arxiv.org/abs/1904.07734
- [M] Kirkpatrick et al. (2017) Overcoming catastrophic forgetting (EWC). https://arxiv.org/abs/1612.00796
- [M] McClelland, McNaughton, O'Reilly (1995) Complementary learning systems. https://doi.org/10.1037/0033-295X.102.3.419
- [V] Krishnan, Tadros, Ramyaa, Bazhenov (2019) Biologically inspired sleep algorithm. https://arxiv.org/abs/1908.02240
- [V] Huang et al. (2024) Self-synthesized rehearsal. https://arxiv.org/abs/2403.01244

**Program library learning**
- [M] Ellis et al. (2018) Learning libraries of subroutines for neurally-guided Bayesian program induction. https://papers.nips.cc/paper/2018
- [V] Ellis et al. (2021) DreamCoder. https://arxiv.org/abs/2006.08381
- [V] Wong, Ellis, Tenenbaum, Andreas (2021/2022) LAPS. https://arxiv.org/abs/2106.11053
- [V] Bowers et al. (2023) Stitch, POPL. https://arxiv.org/abs/2211.16605
- [V] Grand et al. (2024) LILO, ICLR. https://arxiv.org/abs/2310.19791
- [V] Stengel-Eskin, Prasad, Bansal (2024) ReGAL. https://arxiv.org/abs/2401.16467
- [V] Wang, Neubig, Fried (2024) TroVE. https://arxiv.org/abs/2401.12869
- [V] Berlot-Attwell, Rudzicz, Si (2024) Library learning doesn't: the curious case of the single-use library. https://arxiv.org/abs/2410.20274
- [M] Yuan et al. (2023) CRAFT (abstract and TroVE's report; critique marks it abstract-only). https://arxiv.org/abs/2309.17428
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291

**Agent memory and skills**
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Wang, Gandhi, Neubig, Fried (2025) Inducing Programmatic Skills (ASI). https://arxiv.org/abs/2504.06821
- [V] Zheng, Fatemi, Jin, Wang et al. (2025) SkillWeaver. https://arxiv.org/abs/2504.07079
- [V] Ouyang et al. (2026) ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Zhang et al. (2026) Agentic Context Engineering. https://arxiv.org/abs/2510.04618
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153
- [V] Zhang et al. (2026) SkillsBench. https://arxiv.org/abs/2602.12670
- [V] Li (2026) When single-agent with skills replace multi-agent systems and when they fail. https://arxiv.org/abs/2601.04748

**Offline compute and self-improvement**
- [V] Lin et al. (2025) Sleep-time compute. https://arxiv.org/abs/2504.13171
- [V] Pourcel, Colas, Oudeyer (2025) SOAR. https://arxiv.org/abs/2507.14172
