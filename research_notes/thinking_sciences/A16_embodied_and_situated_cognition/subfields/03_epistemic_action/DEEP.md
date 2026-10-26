# Epistemic action: deep document

*Subfield A16.03 (embodied and situated cognition). Written 2026-10-27 from evidence_a-d.jsonl (a01-a30, b01-b25, c01-c25, d01-d22), claims.jsonl (K01-K36) and critique.md in this folder. Evidence ids in brackets. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single-source, [C] contested.*

---

## 1. What it is

An epistemic action is an action done to learn something, not to get closer to the goal. Kirsh and Maglio (1994) defined it as an action that uncovers information that is hidden or hard to compute in the head. A pragmatic action moves the world toward the goal. The standard example is Tetris: a player rotates a falling piece an extra time, then rotates it back, to see its shape or to check a fit. The rotation does not help the score. It helps the decision. [a01, a02, d02]

The idea in one line: some thinking is cheaper to do in the world than in the head. The step is not removed. It is moved to somewhere it is faster, more stable or more exact. [a02, a08]

Three working types, from Kirsh (1995) and the 2026 position paper by Liu, Padmanabhan and Viswanathan: [a04, d12]
- **Acquire.** Get evidence you lack (look up, ask, search, run an experiment).
- **Transform.** Re-express evidence you have (sort it, tabulate it, draw it, write it as code) so it is easier to read.
- **Probe.** Make a small, reversible change to see what happens (rotate the piece, run a test input, mutate a case).

For our agent, the machine versions are: write intermediate state (scratchpad, notes), run code, run a simulator, draw a sketch or grid, call a tool, ask a clarifying question. Schema places: S2 (represent), S4 (test), O6 (change representation), memory. The core design rule that comes out of this field: **judge a write, sketch or run step by what it reveals, not by whether it moves the answer forward.** [a01]

Two cautions frame everything below.
1. The human evidence is thin. The founding paper is mostly argument plus a 3-player pilot. The 4/5/7% skill numbers come from a 2-player follow-up. [d02, b01]
2. The bridge from the human theory to LLM tool use is an analogy. The LLM studies measure functional cousins (scratchpad, code, sketch). No study found tests the Kirsh-Maglio signature in an agent. [c21, d12, K23]

---

## 2. History and theories in depth

### 2.1 Founding work (Kirsh and Maglio)

**Kirsh and Maglio 1994** (Cognitive Science 18:513-549). Full text was read in the gap search. [d02]
- Setup: Tetris. Argument that a standard model (plan, then act) cannot explain the data. Extra rotations come very early in an episode (in earnest 400-600 ms in, sometimes at the outset), and pieces are rotated more than half of their possible rotations, above the 1.5 expected if rotation only followed a finished plan.
- Timing: physical rotation takes as little as 100 ms. Mental rotation of 90 degrees is *estimated* at 800-1200 ms from a pilot of three players (one intermediate, one advanced, one expert), plus 200 ms allowed for a key press. Early rotation shows the full shape 150-300 ms sooner than waiting for it to fall into view. Keystroke gaps: shortest about 75 ms, mean about 250 ms.
- The paper says plainly that epistemic and pragmatic purpose are hard to separate by behaviour. It also says extra rotations serve other aims (memory retrieval, matching the contour).
- It contains **no per-skill percentages and no stated player count** in the text. Earlier summaries (150/200/300 ms; 1000-1800 ms) mixed three separate quantities and should not be used. [d02, K02]

**Kirsh 1995, "The intelligent use of space"** (AI 73). [a02-a05]
- Gives a burst of rotations about 800-1800 ms after the piece enters; external rotation as fast as 150 ms; mental rotation of a tetrazoid 1000-1800 ms (five to ten times slower). These are Kirsh's summary, not raw data.
- Three classes of spatial use: arrangements that simplify choice, arrangements that simplify perception, and spatial dynamics that simplify internal computation. Data: videos of cooking, assembly, packing, supermarket and workshop work. Example: a cook lines sliced vegetables in rows so length encodes number; length is easier to judge than area.
- Process model: internal modules request motor output directly and the changed world feeds back. "Just in time inventory control, only here the inventory is informational." Qualitative, no fitted parameters. [a03]
- Reports Reisberg's result that subjects could not find the second reading of an ambiguous figure in an image but all could in their own drawing. See 5.6: this is too strong.

**Maglio and Kirsh 1996, "Epistemic action increases with skill."** [b01-b03]
- 2 Tetris learners, about 20 hours each, about 40,000 keystrokes. Extra rotations in 4% (beginner), 5% (intermediate), 7% (expert) of episodes for player LA (p<.01). Slow-speed episodes only, to remove the speed confound.
- Extra rotations came 400-500 ms before the final orientation, not after errors. Time to reach target orientation: 676 ms (SD 149) and 754 ms (SD 296) with extra rotations, against 1127 and 1122 ms without.
- Speed still followed the power law of practice (power r2 .91 and .96 vs linear .77 and .81).
- The surprising claim: better players backtrack *more*, not less.

**Kirsh 2010, "Thinking with external representations."** [a06-a09] A list of what external representations add: they change the cost structure of the inferential landscape, give a shareable object, create persistent referents, allow re-representation, suit structure better, allow more explicit encoding, allow arbitrarily complex structure, lower the cost of controlling thought. Saving memory and computation is "only part of the story." Mental structure degrades as it grows ("swap-space thrashing": trying a move in the head can destroy the structure you hold). A built model is an existence proof of consistency.

### 2.2 Rival and adjacent human accounts

- **Preview account (Berry 2023).** In a tournament with the Next Box hidden, 11 elite players could not score a Tetris (paired t all >4.5, p<.001). The author argues experts rely on sampling the world (the preview), not on rotate-to-see. One-off, observational; hiding the preview changes strategy too. [b04, K03]
- **Cost-flow view (Pouw et al. 2014).** Gestures are an external tool; "cognitive processes flow to wherever it is cheaper to perform them." Review, almost no effect sizes. [b08]
- **Active inference (Pezzulo et al. 2019).** Score a policy by expected free energy = extrinsic value + epistemic value (expected information gain about hidden states). Epistemic value dominates under high uncertainty; pragmatic value takes over once context is known. In a T-maze simulation the agent switches policy at trial 18. Toy simulations. [a15] This is the cleanest formal rule we can code.
- **Observers can see it (Croom, Zhou, Firestone 2023).** Observers tell from shaking motion whether a person is trying to learn the number or the shape of objects in a box. See table. [a14]
- **Gesture as offloading (Cook 2012; Dargue 2019; Overoye and Wilson 2020).** Section 5.3. [b05-b07]
- **Interactivity effect (Weller, Villejoubert, Vallee-Tourangeau 2011 and later).** Physically moving problem parts raises insight-task success. Later work is null or mixed. Section 5.2. [a10-a13]

### 2.3 The machine line (what the LLM literature built)

1. **Write the working.** Scratchpads (Nye 2021), chain of thought (Wei 2022). [c01, c02]
2. **Move computation out of the model.** PAL, Program of Thoughts, Chain of Code, Think-and-Execute, code interpreter, tool-integrated reasoning (ToRA, ReTool). [a17, a18, a22, a23, a30, c20, d13]
3. **Act and read back.** ReAct, Reflexion, Toolformer. [a20, c07, a21]
4. **Draw.** Visualization-of-Thought, Visual Sketchpad, MVoT. [a24, a25, a29]
5. **Structure the notes.** SLEUTH typed working memory; Iris interventional vs epistemic actions. [c16, c17]
6. **Search outside the head.** Tree of Thoughts. [a19]
7. **Theory of why it works.** Transformers without intermediate tokens sit in small circuit classes; T intermediate steps give circuits of size T. [a27, b15, b16, b17]
8. **Doubts.** Faithfulness (Lanham; Chen 2025), filler tokens (Pfau), over-use of tools (Zeng; SMART), decreasing value of CoT on reasoning models (Meincke). [b19, b18, d07, b24, d09, d01]
9. **Position paper naming the link** (Oct 2026): acquire / transform / probe, with a value-of-information rule. No data. [d12]

---

## 3. Core findings with exact numbers

Status uses the claims.jsonl file: established / single-source / contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Extra undone Tetris rotations rise with skill | 4% / 5% / 7% of episodes (beginner / intermediate / expert), player LA, p<.01; 2 players, ~20 h each | Maglio and Kirsh 1996 [b01] | single-source (K01) |
| Extra rotations are early, not after errors | Target orientation at 676 ms (SD 149) and 754 ms (SD 296) with extra rotations vs 1127 and 1122 ms without; t198=2.82 for one type | Maglio and Kirsh 1996 [b03] | single-source (K01) |
| Physical vs mental rotation timing | Physical as low as 100 ms; mental 90 degrees estimated 800-1200 ms (3-player pilot) + 200 ms key; early rotation shows shape 150-300 ms sooner | Kirsh and Maglio 1994 [d02] | single-source; older 150/200/300 ms figures unreliable (K02) |
| Elite Tetris depends on the preview | 11 players, all paired t>4.5, p<.001; no Tetris with Next Box hidden | Berry 2023 [b04] | contested (K03) |
| Observers read epistemic intent | Exp 1: 16 players, 76.2% observer accuracy, d=2.12. Exp 2: 18 players, only 4/18 correct, 65.9%, d=1.53. Exp 3 (same box contents): 63.69%, d=0.86. Exp 4 (minimal instruction): 63.72%, d=0.85 | Croom et al. 2023 [a14] | single-source (K04) |
| Meaningful gesture lightens working memory | N=115 after 16 exclusions (and one non-native speaker); meaningless vs meaningful beta=-.17, z=3.23; no movement vs meaningful beta=-.13, z=2.61. First-condition-only: p=.057 and p=.02 | Cook et al. 2012 [b05] | contested (K19) |
| Gesture helps comprehension (meta-analysis) | 83 samples; d=.61 [.50,.72]; production d=.91, observation d=.54; I2 about 67-69%; no benefit in adolescents | Dargue et al. 2019 [b07] | part of K19 |
| Gesture hurts on verbal analogies | 0.42 (no gesture) vs 0.39 (gesture), d=0.34, N=40; Exp 1b 0.38 vs 0.33, d=0.47 | Overoye and Wilson 2020 [b06] | part of K19 (contested) |
| Physical interactivity has no reliable edge | Words 18.35 vs 17.02, F(2,78)=1.94, p=.146, N=40. Matchsticks Exp 1 N=105: interactive .91 vs static .94 on problem A. Only VR interactive sticks +0.67 log-odds [.22,1.15] | Ross and Vallee-Tourangeau 2021; Spiridonov et al. 2025 [a10, a11, a12] | established null (K21) |
| Scratchpad lets models compute | Polynomial evaluation 137B few-shot 8.8% vs 20.1%; 8B fine-tuned 31.8% vs 50.7%. Python execution few-shot 11% vs 26.5%; fine-tuned 20% vs 41.5% | Nye et al. 2021 [c01] | established (K05) |
| CoT at scale | PaLM 540B GSM8K 17.9% vs 56.9% (+39.0); AQuA 25.2 vs 35.8; MAWPS 79.2 vs 93.3 | Wei et al. 2022 [c02] | established (K05) |
| Theory: written steps are serial compute | Without CoT: AC0/TC0 limits; T steps give circuits of size T; linear steps reach finite-state simulation | Li 2024; Merrill and Sabharwal 2024; Feng 2023 [a27, b15, b17] | established (K05) |
| Real code execution beats written reasoning | PAL GSM8K 72.0% vs CoT 65.6% (PaLM CoT 56.9%); GSM-Hard CoT about 20-23% vs PAL about 61%; Object Counting 96.7% vs 73.0%; PoT +12% average over 8 datasets | Gao 2022; Chen 2022 [a17, c03, c04] | established (K06) |
| Active ingredient is execution | PAL with model simulating runtime 23.2% vs real execution 72.0% vs direct 19.7%; single-line code 47.8% | PAL ablation (critique) [K06] | established (K06) |
| PoT failures move to value grounding | Of 198 failures: 47% wrong values taken from problem, 33% logic, 15% both, 5% other | Chen et al. 2022 [c04] | part of K06 |
| Execution on top of hidden thinking | Qwen3-8B Omni-MATH-512 pass@256 82.0% vs 68.4%; 15.4% newly solved vs 1.8% lost; about +9 points on non-algorithmic problems | Lin and Xu 2025 [d14] | established (K26), trained models |
| Tool RL vs text RL | Qwen2.5-32B AIME 2024 67.0% (400 steps) vs 40.0% (1,080 steps); AIME 2025 49.3 vs 36.7; response length down about 40% | Feng et al. 2025 ReTool [d13] | established (K26), trained models |
| Code + text + summary is best | 14 tasks, 6 models: question-only 72.8, all-text 73.9, all-code 77.2, code+text+summary 79.5. o1-preview 88.2 / 81.9 / 93.3 / 90.2 | Chen et al. 2025 [d05] | established (K27) |
| Written reasoning helps symbolic tasks only | Mean CoT gain symbolic +14.2, math +12.3, logic +6.9, other +0.7; up to 95% of MMLU gain from questions with "=" | Sprague et al. 2025 [a28] | established (K07) |
| Writing hurts implicit/perceptual tasks | Implicit statistical learning GPT-4o 87.5% vs 64.4% (-23.1, p<.0001); Opus 70.7 vs 62.7; Gemini 1.5 Pro 68.0 vs 61.95; Llama 70B 65.9 vs 57.1; Sonnet 3.5 65.9 vs 67.7 (ns). Faces GPT-4o 64.0 vs 51.2. Exceptions: up to 331% more trials | Liu et al. 2025 [d08, b23] | established (K07) |
| Always-think helps math, can hurt code | Qwen3-8B Olympiad 49.8 vs 71.5; MATH-500 76.6 vs 85.6; HumanEval 60.4 vs 59.1; Qwen3-14B HumanEval 71.3 vs 66.5; 32B 79.9 vs 72.6 | Lee et al. 2026 DART [d20] | part of K07/K25 |
| Thinking mode on hard math | Qwen3-235B AIME'24 85.7 vs 40.1; MATH-500 98.0 vs 91.2 | Qwen team 2025 [d21] | established (K25), builder-reported |
| Extra "step by step" prompt on reasoning models | GPQA Diamond: o3-mini +2.9 (p=.024), o4-mini +3.1 (p=.003), Flash 2.5 -3.3 (p=.005); time +20-80%. Non-reasoning vs forced direct +4.4 to +13.5; vs default -1.9 to +6.9 | Meincke et al. 2025 [d01] | single-source (K24) |
| Filler tokens do not help off-the-shelf models | No gain at any length (Lanham); Claude 2/GPT-3.5 no gain (Pfau). Trained 34M model: 3SUM 100%, 2SUM-Transform 94% with filler, fail without | Lanham 2023; Pfau 2024 [b19, b18] | established (K08) |
| Chain often is not what drives the answer | Answer changes <10% of the time when chain truncated (ARC, OpenBookQA) to >60% (AQuA, which has the least post-hoc reasoning); hint admitted 25% (Claude 3.7) and 39% (R1) | Lanham 2023; Chen 2025 [c14, d07] | established (K09, K29) |
| Science agents ignore what actions return | 25,000+ runs: evidence ignored in 68% of traces; beliefs never updated 71%; refutation-driven revision 26%; base model explains 41.4% of variance vs scaffold 1.5% | Rios-Garcia 2026 [b25] | preprint, not re-opened |
| Self-review without outside information hurts | GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; GPT-3.5 CommonsenseQA 75.8 -> 38.1; Reflexion with real signal +11% HumanEval, +22% ALFWorld | Huang 2023; Shinn 2023 [c08, c07] | established (K10) |
| ReAct helps interactive tasks, not uniformly | ALFWorld 71 / Act 45 / BUTLER 37; worst ReAct 48; hallucination 56% of CoT failures vs 0% ReAct; HotpotQA ReAct 27.4 < CoT 29.4 < CoT-SC 33.4; best 35.1 combined | Yao 2022 [c06] | contested (K11) |
| Unneeded tool calls cost accuracy | 0.93 unnecessary calls per query; accuracy down 3.29-14.48 points; Qwen3-8B averages 2.2 calls where avg@1024>0.8; DPO cut overuse 82.8% (32B) | Zeng 2026 [b24] | contested as to fix (K12) |
| Prompt-only gate carries some signal | Llama-3-8B decision accuracy 61.9% vs 50% always-call; clarification F1 +0.28 but task success 28.6% -> 27.0%; REAL 32.1% -> 19.2% | Li 2025 MeCo; Matsnev 2026 [d10, d11] | contested (K12) |
| Naming the missing unknown is weak | >80% on GSM-Q, 40-50% on Logic-Q and Planning-Q; o1-preview 49.91% / 42.31% | QuestBench [d19] | single-source (K32) |
| Drawing helps when it is right | Sketchpad +12.7% math, +8.6% vision (abstract); max flow 66.3% (+41.3); VoT GPT-4 navigation 59.0 vs CoT 54.0 vs no-viz 35.5, but drawn state accurate only 24-26%; ring task CoT 52.5 > VoT 49.5 | Hu 2024; Wu 2024 [a25, c12] | established (K14) |
| Simulator feedback | Mind's Eye UTOPIA, GPT-3 175B 24% zero-shot vs 38.2% few-shot vanilla; gain +27.9/+46.0 (table) or +18.4/+34.2 (average over sizes); 1.3B + simulator 29.8% vs vanilla 175B 29% (zero-shot only) | Liu 2022 [c10] | single-source (K13) |
| Simulating unrunnable code still helps | BBH: direct 55, CoT 72, Chain of Code 84 (text-davinci-003); Python-only 48 | Li 2023 [c05] | established (K15), author-run baselines |
| Typed state beats free notes | 4-hop MuSiQue SLEUTH 53.1 vs ReAct 42.0 vs Notes 41.7 vs Facts-only 49.9; HotpotQA 66.1 vs 61.4 vs 60.2; token overhead 29-42% | Liu 2026 [c17] | single-source (K16) |
| Structure needs enforcement | GLM-5 adherence 15% -> 99%; 4-hop 29.9 -> 48.9; nudge at 70% budget 49.1 -> 53.1, ReAct +0.2 | Liu 2026 [c18] | single-source (K17) |
| Many code calls only confirm | Answer written before call in 81% of trajectories (Qwen3-235B-Instruct, MATH500), cost 1.77x; wrong trajectories cost more at every difficulty | Su et al. 2026 [d18] | single-source (K30) |
| Which steps matter, by resampling | 20 MATH problems, 14B distilled model, 144.2 sentences per trace, 100 resamples each: planning and uncertainty sentences matter most | Bogdan et al. 2025 [d06] | single-source (K28) |
| Two-draft agreement as router | Accept if two no-think drafts agree; saves 32-73% thinking tokens, accuracy equal or higher in most settings | Lee et al. 2026 [d20] | single-source (K31) |
| Models do not probe by default | Bandits: only 1 of 48/72 configurations explored well (GPT-4 + CoT + summarised history); >60% suffix failure otherwise | Krishnamurthy et al. 2024 [d15] | single-source (K36) |
| Thinking models ask better questions | Win 0.93 vs 0.10; 14.88 vs 29.13 turns; IG/turn 0.42 vs 0.14 (Qwen3-30B thinking vs instruct) | Pedrozo et al. 2026 [d16] | single-source (K36) |
| Pre-answer data exploration | Spreadsheet tasks: GPT 15/20 -> 16/20 (own) -> 17/20 (oracle); Claude 6/9 -> 7/9 -> 9/9 | Yuan et al. 2026 [d17] | single-source (K34), tiny N |
| Epistemic actions in an agent loop | Iris ablation, 15 tasks, one run: any-medal 66.7 -> 60.0 (-6.7 = one task) without epistemic actions | Fu et al. 2026 [c16] | single-source |
| Terse notes match prose | Qwen-2.5-32B 82.30 vs CoT 82.24 with 74.36% fewer tokens; up to 84% fewer across 15 datasets | Sketch-of-Thought [c22] | single-source (K18), partial read |

---

## 4. Mechanisms and models

Each mechanism is written so it can be coded or tested.

### 4.1 Cost-structure rule (Kirsh 1995, 2010; Pouw 2014)
Do a step outside the head when `cost_external + cost_readback < cost_internal`, and the external result is more reliable. In Tetris: physical rotation about 100-300 ms against an estimated 800-1200 ms mental. For an LLM:
- internal cost = tokens of in-text simulation plus the chance the simulation is wrong;
- external cost = tokens to write the program or table, plus the call, plus reading the result.

Implement: for each S4 sub-step that is computable (arithmetic, counting, simulation, sorting, grid update), the harness runs code. The model writes the program, not the answer. Evidence the rule holds: PAL, PoT, Lin and Xu. Evidence the cost side matters: Zeng 0.93 unneeded calls, SMART >50% overuse. [a17, c04, d14, b24, d09]

### 4.2 Execution is the active ingredient
The PAL ablation is decisive: code written but its result predicted by the model scores 23.2%, real execution 72.0%, direct 19.7%. So the gain comes from a reliable process outside the model returning a result the model cannot fake. Implement: the interpreter output enters context as a tool message; the model never writes the "output" itself. Where code cannot run (semantic steps), Chain of Code lets the model emulate only those lines (BBH 84 vs CoT 72). Flag emulated lines as unchecked. [K06, c05]

### 4.3 Serial depth rule (circuit theory)
Without intermediate tokens a constant-depth transformer cannot do inherently serial problems; with T steps it can do circuits of size T. Parallel tasks (modular addition) are solved without CoT; serial ones (permutation composition, iterated squaring, circuit value) need it. Implement: estimate serial depth (number of dependent steps) at S0 or S1; write steps when depth is more than a few; skip for shallow lookups. Caveat: this is expressiveness, not learnability. [a27, b15, b16, b17]

### 4.4 Persistent external state beats rewriting state (swap-space argument)
Kirsh: mental structure degrades as it grows and trying a move can destroy it. A physical (or file) state is stable. The LLM analogue is a long text chain in which state is re-narrated at every step. Implement: keep state in a variable table, grid or typed block in code; each step reads it, changes one thing, writes it back; code, not model, holds the truth. Evidence: SLEUTH typed state (4-hop 53.1 vs 41.7 for notes), VoT with a code-side grid (drawn state only 24-26% accurate when model-drawn). [c17, c12, a08]

### 4.5 Typed state with enforced format (SLEUTH)
Three blocks: confirmed facts, ranked hypotheses, open questions. Facts-only already gives +7.9 over ReAct at 4-hop; the triple adds +3.2 more. Code validates the block every turn (adherence 15% -> 99% on GLM-5 with an adapted prompt plus runtime check) and forces a commit at a counted fraction of budget (turn 14 of 20 = 70%). A nudge on unstructured ReAct gave +0.2. Single author, two model families. [c17, c18, d22]

### 4.6 Expected-information-gain rule (active inference; Liu et al. 2026)
Score an action e by `E[V(I_e)] - c(e)`, with commit-now as the null action. Probe while uncertainty over the state is high; commit when remaining expected gain is near zero. In T-maze simulation the policy switches at trial 18. Implement as a counted proxy: number of live candidates and disagreement among attempts as the uncertainty; stop probing when the next probe cannot split the live candidates. No LLM measurement yet. [a15, d12]

### 4.7 Gate on epistemic necessity
Before an external action, state in one line: which unknown it resolves and why context cannot resolve it. Use a short yes/no with a one-line reason, not a long chain (MeCo: chain prompts did worse as the final decision contradicted the reasoning). Evidence for a signal: 61.9% vs 50% decision accuracy on an 8B model. Evidence for a cost: capability dilution (success 28.6 -> 27.0; REAL 32.1 -> 19.2). Evidence that naming the unknown is weak: 40-50% on logic and planning. So the gate is a candidate, not an addition. [d10, d11, d19, c15]

### 4.8 Router for when not to write
Harm concentrates where the answer rests on a fast statistical or perceptual impression learned from many examples (implicit learning, face description, exception-laden rules). Help concentrates where the task has a stated rule and an equals sign. Two cheap routers: (a) item-type heuristic (rule stated vs feel over examples); (b) two-draft agreement (DART: saves 32-73% thinking tokens). Neither has been tested on the items where notes hurt. [d08, a28, d20]

### 4.9 Trace ablation (which written steps were epistemic)
A step is epistemic only if removing or changing it changes later steps or the answer. Method (Thought Anchors): replace sentence k with a different sampled sentence, continue 100 times, compare answer distributions. Planning and uncertainty-management sentences carry the answer; arithmetic sentences do not; a forced-answer test ranks computation highest, which is wrong. Chain text alone cannot certify a step (hint admitted 25% / 39%). Cost: 100 rollouts per step, so use on samples offline. [d06, d07, K09]

### 4.10 Confirmatory vs discovering calls
Detector: the answer string appears in the reasoning before the code call. In one setting 81% of trajectories did this, at 1.77x cost. Implement: log it; if high, move the code run to a single final check (S8) instead of a mid-reasoning call. A confirmatory call can still catch an error, so test before removing. [d18]

### 4.11 Reconcile when channels disagree
Run text and code, then a summary/reconcile step. Mean 79.5 against 77.2 (all code) and 73.9 (all text). Multi-turn refinement helped code-heavy methods and hurt text-heavy ones. Implement: if code result and text answer differ, show both outputs to a fresh context and take the code-backed one unless code failed. [d05]

### 4.12 Read-back step
Epistemic action only helps if the result is read. Science agents ignore evidence in 68% of traces. Implement: after every external action, force one line "what did this return, what does it change", checked by code for presence; add a fallback when the result is empty (23% of ReAct failures are empty or useless search). [b25, c06]

---

## 5. What holds up

### 5.1 Tetris and the human founding claim
- **Holds (weakly):** early extra rotations that are later undone, with a rise in rate by skill. Source: one lab, 2 players. [b01, b03]
- **Not shown:** 1994 paper has no skill rates and no player count; mental-rotation time is a 3-player pilot estimate. [d02]
- **Rival:** elite play depends on the preview, not on rotation. [b04]
- **No independent replication** of the 4/5/7% result was found. Treat the skill-increase claim as one lab's finding.

### 5.2 Physical interactivity (replications and nulls)
- Ross and Vallee-Tourangeau: no aggregate effect (p=.146); effect only for those who used the tiles more (post hoc). [a10]
- Spiridonov et al. 2025: Exp 1 N=105 null (.91 vs .94 on problem A); Exp 2 N=88 and Exp 3 N=73, only VR interactive sticks +0.67 log-odds; total movements -0.015 [-0.042, 0.014]; movement hindered relaxing constraints. [a11, a12]
- Others cited as null or mixed: Chuderski 2020, Ross and Vallee-Tourangeau 2020, Spiridonov 2021, Wang and van Leeuwen 2022. Second-hand. [a13]
- Moderators: problem type (gain on harder types B, C, D in the original), whether people actually use the affordance, whether the movement matches the source of difficulty.

### 5.3 Gesture
- Helps: Cook N=115, but first-condition-only p=.057 and .02; 12% excluded as a researcher choice. Meta-analysis d=.61, production > observation. [b05, b07]
- Hurts: verbal analogies (d=.34, N=40; p near .04). [b06]
- Second-hand moderators (via Pouw 2014): capacity (lower working memory or spatial ability, more gesture and more harm if blocked); problem size (4x4 vs 3x3 grid). Originals not opened. [b09-b12]

### 5.4 Written intermediate steps in LLMs
- **Holds:** big gains on serial and symbolic work: Nye, Wei, and a formal basis. Sprague meta-analysis over 100 papers: gain concentrated in math, symbolic, logic. [c01, c02, a28]
- **Does not hold for soft tasks:** gain +0.7 outside the top three categories. [a28]
- **Does not hold for implicit tasks:** GPT-4o 87.5 -> 64.4. [d08]
- **Decays on reasoning-trained models:** "step by step" adds +2.9, +3.1, -3.3 at 20-80% more time. [d01]
- **Not obsolete either:** thinking mode doubles hard-math scores for Qwen3 (85.7 vs 40.1; 71.5 vs 49.8). [d21, d20]
- **Open:** nobody ran a token-matched test of "model's own thinking" vs "thinking plus a visible scratchpad". [critique gap 1]

### 5.5 Code and tools
- **Holds:** PAL, PoT, ToRA, ReTool, Lin and Xu all show gains. The cleanest controlled evidence: PAL simulate-runtime ablation (23.2 vs 72.0) and the six-model 14-task study (77.2 code vs 73.9 text vs 72.8 question-only). [a17, d05]
- **Fails or costs:** unneeded calls cost 3.29-14.48 points (Zeng); on MATH offering tools gave Mistral-7B -4.0 (17.25 -> 13.25) and Llama-3.1-8B -2.0 (53.0 -> 51.0). [b24, d09]
- **Failure modes:** wrong values from the problem (47% of PoT failures); empty tool output; format collapse; 81% confirmatory calls in one setting. [c04, d18]
- **Model choice of code is unreliable:** models do not reliably choose code when code would win; GPT-3.5 beat GPT-4o with the interpreter on Game 24 because it chose code more often. [d05]
- **Caveat:** most of this is Codex, PaLM, GPT-3.5/4 era. Trained-regime results (ReTool, Lin and Xu) are not prompt-only evidence.

### 5.6 Drawing and imagery
- **Holds:** Sketchpad (+12.7 math, +8.6 vision; max flow +41.3), VoT (59.0 vs 35.5 no-viz). [a25, c12]
- **Boundary:** drawn state is right only 24-26% of the time in VoT; correct move 65-77% when the drawing was accurate; Sketchpad plan errors mostly come from failed vision tools; Visprog fell below base on all single-image tasks; weaker models gain less. [c12, c11, c23]
- **Reisberg claim (images cannot be reinterpreted, drawings can, 0% vs 100%) is too strong:** Mast and Kosslyn (N=44): 8 found the alternate reading while memorising, 16 after mental rotation, 20 could not (24/44 = 55%). Peterson et al.: reconstruals are common; reference-frame reversals mainly after a hint. Abstract-level only; Chambers and Reisberg 1985 not opened. [d03, d04, a05]

### 5.7 Failed or weak pieces, listed
- Dot-by-dot filler: works only in trained small transformers with dense supervision; not in Claude 2 or GPT-3.5. [b18, b19]
- Self-review without outside information. [c08]
- ReAct on HotpotQA alone. [c06]
- Prompt-only ask-vs-act gate: capability dilution. [d11]
- Physical interactivity: null in most tests. [a10-a13]
- Forced text on o1-preview: 88.2 -> 81.9. [d05]
- Mind's Eye "small matches big" holds in zero-shot only; few-shot gain for 1.3B is 10.3% vs 46.0% for 175B. [critique 4]

### 5.8 Interventions that worked, with size
| Intervention | Size | Where |
|---|---|---|
| Scratchpad / CoT | +11 to +39 on symbolic tasks at scale | [c01, c02] |
| Run code (PAL) | +6.4 on GSM8K; about +40 on GSM-Hard | [a17] |
| Typed state + enforcement | +11 on 4-hop vs ReAct; +19 for GLM-5 with enforcement | [c17, c18] |
| Code + text + reconcile | +6.7 over question-only (6-model mean) | [d05] |
| Real feedback in a retry loop | +11 HumanEval, +22 ALFWorld | [c07] |
| Summarised history for probing | only successful bandit configuration | [d15] |
| Two-draft routing | -32 to -73% thinking tokens at equal or higher accuracy | [d20] |

### 5.9 What did not work, with size
| Intervention | Result | Where |
|---|---|---|
| Re-read and self-correct | GPT-4 GSM8K -6.5 in two rounds | [c08] |
| Forced write-out on implicit tasks | -23.1 GPT-4o | [d08] |
| "Step by step" on a reasoning model | -3.3 to +3.1 | [d01] |
| Unprompted tool offers on math | -4.0 Mistral-7B | [d09] |
| Prompt-only clarification gate | -1.6 mean success; -12.9 REAL | [d11] |
| Filler tokens | 0 | [b19] |
| Nudge without structured state | +0.2 | [c18] |

---

## 6. Language models

### 6.1 How they behave on these tasks, by action type

**Write intermediate steps.** Large, scale-dependent gains on serial, symbolic work (Nye 8.8 -> 20.1; Wei 17.9 -> 56.9). Almost nothing on commonsense or perceptual work (Sprague other +0.7). Harmful on implicit statistical learning and face description. On modern reasoning-trained models the added prompt is worth about 0-3 points for 20-80% more time. [c01, c02, a28, d08, d01]

**Run code.** Strongest single lever on computation: PAL GSM-Hard 61% vs about 20-23%. Execution, not code-shaped text, is the cause (23.2 vs 72.0). In the trained regime execution still adds problems solved on top of long thinking (+13.6 net points at pass@256 for Qwen3-8B; ReTool 67.0 vs 40.0). Models misjudge when to use code. [a17, d14, d13, d05]

**Call tools / look things up.** Helps interactive and fresh-fact tasks (ALFWorld 71 vs 45; FreshQA Llama-3.1-8B 26 -> 67 with tools). Overused: 0.93 unneeded calls per query; Qwen3-8B 2.2 calls per query even on easy items. Hurts on math for small models. [c06, d09, b24]

**Draw.** Helps spatial and geometric tasks when the drawing is right, in strong models only. Model-drawn state is mostly wrong (24-26% accurate in VoT). Ring-navigation reversal (CoT 52.5 > VoT 49.5). [c12, a25]

**Typed memory.** SLEUTH +11 at 4-hop vs ReAct; unstructured notes +0 (41.7 vs 42.0). Only with enforcement. [c17, c18]

**Probe / explore.** Not spontaneous in 2023-era models (1 of 48/72 bandit configurations explored well, and it needed a code-built summary). In 20 questions, thinking models gather more information per turn, earlier (IG/turn 0.42 vs 0.14; 0.93 vs 0.10 win). Science agents ignore results in 68% of traces. [d15, d16, b25]

**Ask for missing information.** Models solve the full problem but pick the right question only 40-50% on logic and planning, even though they exceed 80% on math. [d19]

### 6.2 What changed behaviour, and by how much
- **Execution instead of simulation:** 23.2 -> 72.0 (PAL ablation).
- **Real feedback instead of self-review:** -6.5 (self-review) vs +11 / +22 (Reflexion with signal).
- **Harness-built summary of history:** bandit exploration from failing to working (single configuration).
- **Runtime protocol check:** adherence 15% -> 99%, 4-hop 29.9 -> 48.9.
- **Commit trigger at 70% budget:** +4.0 with typed state, +0.2 without.
- **Reasoning training:** thinking-mode Qwen3 AIME 85.7 vs 40.1; a step-by-step prompt on top adds 0-3.
- **Reconcile step:** best mean score (79.5).
- **Training against overuse:** 82.8% fewer unneeded calls in a 32B model (+3% accuracy); prompt-only equivalents were not found.
- **Task type routing:** two-draft agreement saves 32-73% thinking tokens.

### 6.3 What is not known for current models
- Prompt-only, equal-token value of a visible scratchpad on top of native thinking. (Largest gap.)
- Whether current agents show early, reversible, information-seeking probes. No trace analysis was found. [critique gap 6]
- Whether Kirsh-Maglio-style skill-dependent probing exists in LLMs.
- Independent replication of typed-state gains.
- Most LLM gains are on Codex / PaLM / GPT-3.5 / GPT-4 era models; none of the "established" claims K05-K09, K13, K14, K20 control tokens. [critique weak spots]

---

## 7. What our agent should take

Mark: part of schema; status; evidence ids.

### Add now (established)

Only items whose evidence is two or more independent sources. Each is also checked against SCHEMA.md 4b so it is not a repeat.

1. **Offload exact computation to real execution; never let the model "predict the output".** Schema: S4. [E] K06, K26, K27. Evidence a17, c03, c04, b21, a22, d05, d13, d14. Rule: if a sub-step is arithmetic, counting, sorting, grid update or simulation, code runs it and the tool output enters context. Code written but not run, with the model predicting the result, is banned (23.2 vs 72.0).
2. **Write intermediate state for serial symbolic work; skip it for soft and perceptual items.** Schema: S2/S4 and S0 routing. [E] K05, K07. Evidence c01, c02, a28, b20, a27, b15, b16, b17, d08, b23, d20. Rule: gate the write-out on serial depth and task type (rule stated, equals sign, many dependent steps). This extends G11 (think briefly by default).
3. **Do not make S2 notes mandatory on every item.** Schema: S0/S2. [E] K27, K07. Evidence d05, d01, d08. Forced text lowered o1-preview 88.2 -> 81.9 and GPT-4o on implicit learning 87.5 -> 64.4.
4. **Do not use filler or length as the active ingredient.** Schema: G7 control. [E] K08. Evidence b18, b19, c13. Any scratch step must beat a same-length filler control on the model we use.
5. **A revision step needs real external output; self-review does not count as epistemic action.** Schema: G2 (already there; this adds sources). [E] K10. Evidence c08, c07, c25.
6. **Do not use chain text as proof that a step mattered.** Schema: G10 (already there; adds sources). [E] K09, K29. Evidence b19, c14, d07, c24, d06.
7. **Drawn or sketched state is trusted only when code checks it.** Schema: S4, O6. [E] K14. Evidence c12, a25, c11, a24. Keep a code-side ground truth grid; score the model's drawing against it.
8. **Fallback ladder for steps code cannot run: real execution first, then pseudocode traced line by line, flagged as unchecked.** Schema: S4. [E] K15. Evidence c05, c20, a23. Treat emulated lines as unverified (G3).
9. **Log every external action with an outcome line.** Schema: section 6 logging, S4. Read-back is supported by [E] K10/K11-adjacent evidence (a20, c06, b25) but the "forced read-back line" itself is [S]; so only the logging is added now.

Not added now because they are already in 4b or contradict it: reflection prompts, "be careful" instructions, debate.

### Test first

| # | Candidate | Schema | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | A visible S2/S4 scratchpad on top of the model's own thinking, at equal total tokens | S2 | [C] | d01, d21, d20, K24, K25 | Gap 1; value may be 0-3 points on reasoning-trained bases |
| T2 | Typed state (facts, hypotheses, open questions) with code-enforced format vs free notes | S2, memory | [S] | c17, c18, d22, K16, K17 | One author, no replication |
| T3 | Late commit trigger at a counted budget fraction (about 70%) | G1/S6 | [S] | c18, K17 | Works only with typed state in one paper |
| T4 | Epistemic gate: "what unknown does this resolve, why not in context" before a tool or code call | G1, S4 | [C] | b24, d10, d11, d19, K12, K32 | Prompt-only gating shown to dilute capability |
| T5 | Router for when not to write: two-draft agreement or item-type heuristic | S0 | [S] | d20, d08, K31 | Untested on items where notes hurt |
| T6 | Pre-answer exploration note (structured account of the data) | S2 | [S] | d17, K34 | Tiny N, own-artifact vs given-artifact effect |
| T7 | Information-gain scoring of clarifying questions and probes | S2, S6 | [S] | d16, d15, K36 | Question game, not a world |
| T8 | Defer confirmatory code calls to a single final check | S4/S8 | [S] | d18, K30 | Detector heuristic; confirmatory call may catch errors |
| T9 | Trace ablation of own S2/S4 traces (share of steps that change the answer) | analysis, G10 | [S] | d06, K28 | Measurement, not a feature |
| T10 | Reconcile step when code and text disagree | S4/S7 | [S] for our setting | d05, K27 | Gain shown at 2024 model level |
| T11 | Visible plan / next-steps block kept in context | S2 | [C] | b04, K03 | Preview account vs rotation account |
| T12 | Acquire / transform / probe labels per step | logging | [S] | d12, K33 | Position paper only |
| T13 | Small-model-plus-exact-tool vs larger model alone at equal cost | S4 | [S] | c10, d09, K13 | 2022 zero-shot, or trained-model evidence |
| T14 | Scale externalisation with problem size and base-model weakness | S2 | [S] | b11, b10, K20 | Second-hand human evidence |
| T15 | Terse typed notes vs prose at matched accuracy | S2 | [S] | c22, K18 | Partial read |
| T16 | Re-frame step when rereading own representation (not just a re-read) | O6 | [C] | d03, d04, a05, K35 | Image/drawing contrast overstated |

---

## 8. Concrete tests on our bench

All tests: both (or all) arms at equal total tokens (input plus output plus tool output), same items, same base model, 3 or more seeds, report accuracy with a confidence interval and tokens per correct answer. Setup cost counts (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 (T1) | ARC items with a check; BrainTeaser-style riddles | (a) model's own thinking only; (b) own thinking + typed S2 notes; (c) own thinking + same-length filler | Accuracy at equal tokens; extra tokens for (b) taken from a second sample in (a) | 0 to +3 points for (b); filler = 0. If (b) <= (a) then drop S2 notes on reasoning-trained bases |
| E2 (K05, T9) | Items split by serial depth (1-2 vs 6+ dependent steps) | direct vs typed trace | Accuracy by depth | No gain at depth 1-2; large gain at depth 6+ |
| E3 (K06) | Computational items (counting, grids, arithmetic with large numbers) | (a) CoT; (b) code written and run; (c) code written, model predicts result | Accuracy | (b) > (a) > (c) roughly equal to direct; (c) collapses |
| E4 (T4) | Mixed items: half answerable from context, half need a lookup/run | no gate vs one-line gate (unknown + why not in context) vs always-call | Calls, accuracy, tokens | Fewer calls; accuracy within -1 point, else drop (watch for dilution) |
| E5 (T5) | Soft/commonsense and implicit-pattern items | forced notes vs two-draft agreement router vs direct | Accuracy, tokens | Notes give 0 or negative on these; router saves tokens with no loss |
| E6 (T2, T3) | Multi-hop items with a check | free notes vs typed blocks (code-validated) vs typed + commit at 70% | EM; format adherence by code | Typed > free by 5+ points; commit adds +2 to +4 only with typed |
| E7 (T9) | Our own logged S2/S4 traces | resample step k 20-100 times | Share of steps that change the answer; which types | Plans and revisions change answers; restated facts do not |
| E8 (T8) | Code-using items | call mid-reasoning vs single final check | Accuracy; cost; answer-before-call rate | Same accuracy at lower cost if rate is high |
| E9 (K14) | Spatial / grid items | model-drawn sketch vs code-rendered state vs none | Accuracy; drawing accuracy scored separately | Code-rendered >= model-drawn > none; model drawing accuracy well under 100% |
| E10 (T10) | Items where code and text can disagree | code only vs text only vs both + reconcile | Accuracy | Both + reconcile best by 2 or more points |
| E11 (T6) | Data-heavy items (tables, multi-sheet) | exploration note vs none vs given artifact | Accuracy | Gain on mid and hard items; own note close to given |
| E12 (K01, T12) | Agent traces over easy/hard items and weak/strong bases | label steps acquire/transform/probe; count undone, early probes | Rate of early reversible probes by base strength | Prediction from theory: more early probes in strong runs. If flat, drop the human-signature framing |
| E13 (T7) | Open clarification and 20-questions style items | questions chosen freely vs scored by information gain (code over candidate set) | Turns to solution | Fewer turns with information-gain scoring |
| E14 (T13) | Computable domains with an exact simulator | small model + tool vs larger model alone | Accuracy at equal cost | Small + tool matches larger if tool domain fits |

---

## 9. What does not transfer, and why

1. **The Tetris timing advantage.** Physical rotation is 100-300 ms against 800-1200 ms mental. An LLM has no motor delay; its external step costs tokens and a call, not a speedup. Use cost in tokens instead. [K02]
2. **Physical interactivity.** Moving matchsticks or tiles has no stable effect even in people (p=.146; ns in most cells). There is no body in our agent. The only analogue that holds is real execution, not "acting for its own sake". [a10-a13]
3. **Gesture.** Gesture lightens working memory only when tied to content, and hurts on verbal analogies. The nearest analogue (content-bearing notes) is already in the table; meaningless writing does not help. [b05, b06]
4. **Perceptual read-back.** In Tetris the result is read by fast vision. In an LLM the read-back is more tokens, which cost attention and can carry the same errors. VoT shows the model often misreads its own drawing (24-26% accurate). [c12]
5. **Expertise as more probing.** The skill claim rests on 2 players. No test in LLMs. Do not penalise or reward extra steps on this basis. [b01, K23]
6. **Observer perception of epistemic intent.** Croom et al. show people read intent from motion; it says nothing about whether the action helps. Useful at most for logging. [a14, K04]
7. **Imagery vs drawing contrast.** The 0% vs 100% figure should not be written into the schema. [K35]
8. **Trained-regime tool results.** ReTool, Lin and Xu, ToRA, SMART, Toolformer train the model. We do not train. They show the ceiling, not what a prompt gets. [d13, d14, a30, d09]
9. **Old-model gains.** PAL, PoT, Nye, ReAct, Wei were measured on Codex, PaLM, GPT-3 era models. A current model that already writes long traces gains less from the same prompts. [critique weak spots, d01]
10. **Dot-by-dot filler.** Applies to trained small transformers, not to the model we use. [b18]
11. **Theory results.** Circuit-complexity bounds are expressiveness limits for idealised transformers. They support the direction (write for serial depth) but give no number for a real model. [a27, b15]

---

## 10. Open questions

1. At equal tokens, does a visible S2/S4 scratchpad add anything to a model that already thinks at length? (Largest gap; no token-matched test exists.)
2. Does a prompt-only epistemic gate cut unneeded calls and keep accuracy? Only the clarification case was tested, with a cost.
3. What share of our own S2/S4 steps pass a trace-ablation test?
4. Is the active ingredient of run-code-to-think the execution result or the planning discipline when the task cannot become code? (PAL says execution; Chain of Code says simulation still helps.)
5. Which features route an item away from notes? Is there a cheap router that works on implicit and perceptual items?
6. Do LLM agents show early, reversible, information-seeking probes that rise with strength? No trace analysis found.
7. Does typed state beat free notes in independent hands, on other model families?
8. Is there an agent analogue to the physical-interactivity null: task types where acting on the structure gives no gain over thinking? Nearest leads: code-only 80.3 vs question-only 80.6 for GPT-4o; tool offers -4.0 on Mistral-7B MATH.
9. Chambers and Reisberg 1985 and the Kirsh and Maglio 1994 figures should be checked from primary text beyond the author PDF.
10. Can a small model plus an exact tool match a larger model alone at equal cost with current small models, prompt-only?
11. Is the 81% confirmatory-call rate general, and do confirmatory calls catch enough errors to justify their 1.77x cost?
12. Does the Next Box (visible look-ahead) result have an LLM counterpart: does a visible plan block help more than extra probes?
13. Does the reconcile step still help on reasoning-trained models (o1-preview was the only one tested, and its gain was 90.2 vs 93.3 for all-code, i.e. negative)?

---

## 11. Sources

[V] = opened this session by the research or cross-check agents (full text or enough page text to read the numbers). [M] = snippet or abstract only. Where critique.md marks a source as abstract-level, it is marked [M] here.

**Human work**
- [M] a01. Kirsh and Maglio 1994, abstract via Crossref. https://doi.org/10.1207/s15516709cog1804_1
- [V] d02. Kirsh and Maglio 1994, author PDF, full text. https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf
- [V] a02-a05. Kirsh 1995, The intelligent use of space. https://cogsci.ucsd.edu/~kirsh/Articles/Space/AIJ1.html
- [V] a06-a09. Kirsh 2010, Thinking with external representations. https://link.springer.com/article/10.1007/s00146-010-0272-8
- [V] b01-b03. Maglio and Kirsh 1996, Epistemic action increases with skill. https://interactivity.ucsd.edu/articles/Cogsci96/cogsci96.pdf
- [V] b04. Berry 2023, No Next Box, No Experts. https://www.journalofexpertise.org/articles/volume6_issue2/JoE_6_2_Berry.pdf
- [V] a14. Croom, Zhou and Firestone 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10710017/
- [V] a15. Pezzulo et al. 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC7514834/
- [V] a10. Ross and Vallee-Tourangeau 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC7899957/
- [V] a11-a13. Spiridonov et al. 2025 (a13 is the second-hand summary of Weller 2011 and others). https://pmc.ncbi.nlm.nih.gov/articles/PMC12862482/
- [V] b05. Cook, Yip and Goldin-Meadow 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3658147
- [V] b06. Overoye and Wilson 2020. https://www.frontiersin.org/articles/10.3389/fpsyg.2020.571109/pdf
- [V] b07. Dargue, Sweller and Jones 2019. https://humintell.com/wp-content/uploads/2019/09/Dargue-et-al.-2019.pdf
- [V] b08. Pouw et al. 2014. https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00359/full
- [M] b09-b12. Delgado et al. 2011; Chu et al. 2013 and Marstaller and Burianova 2013; Kirsh 2009; Martin and Schwartz 2005 and Warburton et al. 2013, all via Pouw 2014 (same URL). Second-hand.
- [M] b13. Kirsh and Maglio 1994 timing summary (superseded by d02). https://escholarship.org/content/qt44k7g3vm/qt44k7g3vm.pdf
- [M] d03. Mast and Kosslyn 2002, abstract. https://pubmed.ncbi.nlm.nih.gov/12208651/
- [M] d04. Peterson et al. 1992, abstract. https://pubmed.ncbi.nlm.nih.gov/1565009/

**LLM studies and theory**
- [V] a16, b14, c01. Nye et al. 2021. https://arxiv.org/abs/2112.00114
- [V] c02. Wei et al. 2022. https://arxiv.org/abs/2201.11903
- [V] a17, b21, c03. Gao et al. 2022, PAL. https://arxiv.org/abs/2211.10435
- [V] a18, b22, c04. Chen et al. 2022, Program of Thoughts. https://arxiv.org/abs/2211.12588
- [V] a19. Yao et al. 2023, Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] a20, c06. Yao et al. 2022, ReAct. https://arxiv.org/abs/2210.03629
- [M] a21, c09. Toolformer (abstract level; c09 table assigned by row order). https://arxiv.org/abs/2302.04761
- [M] a22. Zhou et al. 2023, code interpreter with self-verification (abstract numbers). https://arxiv.org/abs/2308.07921
- [M] a23. Chain of Code (abstract numbers); [V] c05 gives the table. https://arxiv.org/abs/2312.04474
- [V] a24, c12. Wu et al. 2024, Visualization-of-Thought (tables interleaved in extraction). https://arxiv.org/abs/2404.03622
- [V] a25, c11, c23. Hu et al. 2024, Visual Sketchpad. https://arxiv.org/abs/2406.09403
- [V] a26, b18, c13. Pfau et al. 2024, dot by dot. https://arxiv.org/abs/2404.15758
- [V] a27, b16, c19. Li et al. 2024 (listed as Feng et al. in c19), CoT for serial problems. https://arxiv.org/abs/2402.12875
- [V] a28, b20. Sprague et al. 2025. https://arxiv.org/abs/2409.12183 (numbers from A/B agents' reading; not re-opened)
- [M] a29. Zhang et al. 2025, MVoT (abstract). https://arxiv.org/abs/2501.07542
- [M] a30. Gou et al. 2023, ToRA (abstract). https://arxiv.org/abs/2309.17452
- [V] b15. Merrill and Sabharwal 2024. https://arxiv.org/pdf/2310.07923
- [V] b17. Feng et al. 2023. https://arxiv.org/pdf/2305.15408
- [V] b19, c14, c24. Lanham et al. 2023 (c24 corrected in critique). https://arxiv.org/abs/2307.13702
- [V] b23, d08. Liu et al. 2025, Mind your step. https://arxiv.org/abs/2410.21333
- [V] b24. Zeng et al. 2026, tool-overuse illusion. https://arxiv.org/pdf/2604.19749
- [V] b25. Rios-Garcia et al. 2026 (not re-opened). https://arxiv.org/pdf/2604.18805
- [V] c07. Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366
- [V] c08, c25. Huang et al. 2023. https://arxiv.org/abs/2310.01798
- [V] c10. Liu et al. 2022, Mind's Eye. https://arxiv.org/abs/2210.05359
- [M] c15. Wang et al. 2025, position paper on epistemic necessity (abstract page). https://arxiv.org/abs/2506.00886
- [V] c16. Fu et al. 2026, Iris. https://arxiv.org/abs/2608.02143
- [V] c17, c18, d22. Liu 2026, SLEUTH. https://arxiv.org/abs/2607.12267
- [V] c20. Chae et al. 2024, Think-and-Execute. https://arxiv.org/abs/2404.02575
- [M] c21. Gap note, no LLM replication found (search-limited).
- [M] c22. Aytes et al. 2025, Sketch-of-Thought (partial read). https://arxiv.org/abs/2503.05179
- [V] d01. Meincke et al. 2025. https://arxiv.org/abs/2506.07142
- [V] d05. Chen et al. 2025, code vs text. https://arxiv.org/abs/2410.03524
- [V] d06. Bogdan et al. 2025, Thought Anchors. https://arxiv.org/abs/2506.19143
- [V] d07. Chen et al. 2025, Anthropic faithfulness. https://arxiv.org/abs/2505.05410
- [V] d09. Qian et al. 2025, SMART. https://arxiv.org/abs/2502.11435
- [V] d10. Li et al. 2025, MeCo. https://arxiv.org/abs/2502.12961
- [V] d11. Matsnev 2026. https://arxiv.org/abs/2606.19559
- [V] d12. Liu, Padmanabhan and Viswanathan 2026. https://arxiv.org/abs/2610.00511
- [V] d13. Feng et al. 2025, ReTool. https://arxiv.org/abs/2504.11536
- [V] d14. Lin and Xu 2025. https://arxiv.org/abs/2508.19201
- [V] d15. Krishnamurthy et al. 2024. https://arxiv.org/abs/2403.15371
- [V] d16. Pedrozo et al. 2026. https://arxiv.org/abs/2601.17716
- [V] d17. Yuan et al. 2026. https://arxiv.org/abs/2608.16045
- [V] d18. Su et al. 2026. https://arxiv.org/abs/2604.05404
- [V] d19. Li, Kim and Wang 2025, QuestBench. https://arxiv.org/abs/2503.22674
- [V] d20. Lee et al. 2026, DART. https://arxiv.org/abs/2606.23181
- [V] d21. Qwen Team 2025. https://arxiv.org/abs/2505.09388

**Cautions carried from critique.md.** PAL text and table disagree on CoT GSM-Hard (20.1% vs 23.1%); use "about 20-23% vs about 61%". Mind's Eye has two gain figures (27.9/46.0 table; 18.4/34.2 average over sizes). The Lanham AQuA -4.69 figure is HellaSwag, and AQuA has the least post-hoc reasoning. ReAct comparison should include CoT-SC alone (33.4 on HotpotQA). SLEUTH per-hop gains are +11.9, +10.4, +10.9. Some table rows (Chen cost table, DART Table 1, QuestBench, Pedrozo Qwen3-8B rows) were garbled in extraction; only readable cells were used. Qwen3 figures are builder-reported.
