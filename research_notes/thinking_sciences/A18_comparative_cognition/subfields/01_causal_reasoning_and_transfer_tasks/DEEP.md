# Causal reasoning and transfer tasks: deep document

*Subfield A18.01 (comparative cognition). Sources: evidence_a-d.jsonl, claims.jsonl (K01-K29), critique.md in this folder. Written 2026-10-31. Evidence ids (a01, b05, c15, d09 ...) point to the jsonl lines. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The question: does an animal grasp a cause, or has it learned a cue? A cue is a surface feature that was linked to reward during training. A cause is the feature that actually produces the outcome.

The standard tool is the trap-tube. Food sits in a clear tube. The animal must push or pull it out with a tool, away from a trap hole that would swallow it. A learner can succeed by cue (avoid the visible hole) or by cause (the food would fall, so avoid the base). The two accounts give the same answer on the training task. They split only on transfer tasks.

Transfer logic (triangulation, Heyes 1993) has three steps:

1. Train on a task that contains arbitrary cues (coloured discs, a coloured rim).
2. Remove the cues one at a time.
3. Give a visually different task with the same causal structure, then a task where the old surface cue and the true cause point in opposite directions.

Only an account that survives all steps counts. This is the same idea as our guardrail G3: a pass must be on something the answer was not fitted to.

Why it matters for our agent: S4 (test) and G3 need a pass rule that is hard to fake. The crow series is the cleanest worked example of such a rule. It also shows where the rule fails: a pass on a re-skinned task can still hide a wrong rule (a04, b02).

Scope: the founding crow study (Taylor 2009), the ape, rook and other-bird tests, the Aesop's fable line, the critiques, and every LLM or AI study found that tests cue removal, surface swaps or causal discovery. No study gives an LLM the crow tasks directly (c25, K11). The LLM section therefore uses the nearest bridges.

## 2. History and theories in depth

**1994, origin.** Visalberghi and Limongelli gave capuchins a trap-tube. The one monkey that solved it did not change when the tube was inverted. It had only learned to insert the tool at the end far from the food. They read this as no grasp of cause and effect (a12, second-hand; not opened).

**2000, the rival theory.** Povinelli's reinterpretation hypothesis: apes learn regularities between observable events but do not appeal to unobservable forces such as gravity (a14, b15). His group ran about 27 experiments. Chimp Megan solved the tube, then used the far end on 39/40 inverted-trap trials (a08, a14).

**2005, a flaw in the control.** Silva, Page and Silva showed adults fail the inverted-trap control. Adults pass functional traps 40/40 and 10/10, but insert the tool at the far end on 36 of 40 ineffective-trap trials, and still give causal reasons (a08, d16). So failing that control does not show lack of causal knowledge [S, one lab].

**2006, interface confound.** Mulcahy and Call let apes rake instead of push. With raking, 3 of 8 apes solved the tube in 24 to 60 trials and passed the inverted control (a09, a13, second-hand). Raking beat pushing 64.5% vs 18% in one pretest (b06). Earlier ape failures were partly a tool-load effect.

**2006-2007, rooks.** Seed et al.: 7 of 8 rooks passed the tube in 150 trials; one rook may have passed transfers. Tebbich et al. 2007: 3 of 7 non-tool-using rooks solved a modified tube and none passed transfer (a11, d02). Both are second-hand or abstract only.

**2008, apes, two tasks.** Martin-Ordas, Call and Colmenares gave 20 apes a trap-tube and a trap-platform. 12/20 solved the platform, 8/20 the tube, 5 solved both. Cross-task correlation r=0.13, p=0.57. First trials were not above chance (platform 14/20, tube 12/20). No evidence of transfer between functionally equal tasks (a07, b05, b06).

**2009, the crow study.** Taylor, Hunt, Medina and Gray tested 6 wild New Caledonian crows (a01-a05). Three learned the tube. Those three passed two cue-removal transfers and the visually different trap-table at first trial. They failed a transfer with a hole and a functional trap. The authors concluded causal reasoning is a component of crow cognition. A follow-up the same year added 8 naive crows to rule out hole-avoidance and sampling error (d01, b12).

**2014-2018, Aesop's fable.** Jelbert et al. 2014 ran a six-task battery: crows passed intuitive items and failed narrow-vs-wide and the U-tube (a10, b08). Logan et al. 2014 showed the one U-tube success was a colour-cue association (b07, d08). Ghirlanda and Lind 2017 and Hennefield et al. 2018 re-analysed trial-level data and found learning inside the task, not first-trial understanding (d09, d10).

**2020, the author revises.** Taylor (2020) reads the crow result as knowledge of observable features only. He cites Neilands 2016: no preference for heavy over light stones. He asks for a difficulty ladder inside one paradigm: hidden object, hidden agent, unobservable cause (a06, b02-b04). Farrar et al. 2020 add a meta-research warning: median N=7 across 116 physical cognition experiments (a15).

**Competing explanations.** The data do not separate them (critique.md):

| Account | Claim | Main support |
|---|---|---|
| Causal reasoning about observable features | Crows track meat-hole-base relations | Taylor 2009, d01 |
| Associative or perceptual generalisation | Cue or surface rule only | Povinelli, Hennefield; crows fail the decoy (b02) |
| Tool load / action cost | Failure is interface, not knowledge | Voelter and Call, Mulcahy and Call (a09, K05) |
| Analogy tied to action | Knowledge is action-bound, does not cross tasks | Martin-Ordas (a07) |
| Inhibitory control | Solvers switch sides, inhibit pulling | Taylor 2009 (a02), post hoc |

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Only half of crows learned the tube | 3 of 6 crows; mean 103.3 +/- 20.3 trials (s.e.); criterion 17/20 over two 10-trial blocks, stop at 150 | Taylor 2009 (a02) | [S] |
| Solvers switched probing side more | 22.1 +/- 9.0% vs 0%, U=9, p=.0318 one-tailed (3 vs 3 birds) | a02 | [S], low power |
| Cue-removal transfers 1 and 2 passed | 3 of 3 crows above 15/20; first trials pooled over four transfers: trap avoided 10 of 12 | a03 | [S] |
| Trap-table (new look) passed at first trial | 3 of 3 solvers; 3 of 3 non-solvers failed | a05 | [S] |
| Two-hole decoy transfer failed | 3 of 3 failed; latency/switching pattern p=.0156 (binomial, n=3, p0=.25) | a04 | [E] (K02) |
| Naive crows at chance on the trap-table | 8 naive crows at chance; of 14 crows, 3 passed, all tube solvers | d01 | [S] same lab |
| Apes: no cross-task transfer | N=20, r=0.13, p=.57; first trial platform 14/20, tube 12/20 | Martin-Ordas 2008 (a07) | [S] |
| Raking beats pushing | 64.5% vs 18% (pretest); 20/24 apes avoided trap on trial 1 with one tool | b06, a13 | [E] (K05) |
| Adults fail inverted control | far end on 36/40 ineffective-trap trials; 40/40 functional | Silva 2005 (d16) | [S] |
| Outside-lab birds: training yes, transfer rare | rooks 3/7 pass, 0 transfer; Darwin's finches 0 transfers; hooded crows 1/6 first trial, 4 by trial and error; macaws/caiques 1/8 clear transfer; zebra finches N=34 at chance; dogs (25) never 60% | d02-d07 | [E] (K22) |
| Meta-research: tiny samples | 116 experiments, 63 papers; median N=7; 15 of 87 with zero passers; median passers 3; positive claims 44-59% | Farrar 2020 (a15) | [S] |
| Aesop: pass vs fail | water-vs-sand 76.3%, sinking 88.0%, solid 89.0%, narrow-vs-wide 39.3% to narrow; U-tube fail | Jelbert 2014 (b08) | [C] |
| Aesop: learning inside task | slope OR 1.04, 1.05 per insertion (p<.001); first trial OR 0.53, 1.23 (no edge); hollow-vs-solid first trial OR 57.02; task order OR 0.81 p=.22 | Hennefield 2018 (d09) | [E] (K24) |
| Animal-AI: children beat agents | 52 children mean 0.605 vs 30 AIs 0.341; 0% of AIs passed levels 3, 6, 8, 9, 10 | Voudouris 2022 (a16, d12) | [E] |
| Odds of passing vs random | children 47x; ironbar/Trrrrr 19x; Dreamer-v3 6.5x (p=.038); PPO not above chance (p=.61) | Animal-AI 3 (c03) | [S] |
| LLMs in Animal-AI | Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro; 12 trials per level; worse than children at every level; one in-context example mixed | Mecattaf 2024 (d11) | [S] |
| Letter-string counterfactuals | humans 0.753; GPT-3 0.488; GPT-3.5 0.350; GPT-4 0.452 (pooled) | Lewis and Mitchell (b21) | [E] (K12) |
| Transitive inference stripping | 1.00 -> 0.97 -> 0.92 -> 0.78 -> 0.40 as cues removed; chance on novel non-adjacent pairs | Rane 2025 (a19) | [S] |
| CLadder | random 49.27; GPT-4 62.03; CausalCoT 70.40; CausalCoT rungs 83.35 / 67.47 / 62.05; vanilla rungs 63.01 / 62.82 / 60.55 | Jin 2023 (a20, d14) | [S] |
| Corr2Cause | best F1 33.38; fine-tuned drop to 39.29 on paraphrase; graph-first Qwen3-32B 32.71 -> 48.26 | c11, c12 | [E] (K15) |
| Retrieval-driven causal success | Tubingen 97%, counterfactual 92%, actual causality 86%; post-cutoff pairs 80.3% / 98.5% | Kiciman 2024 (c13) | [S] |
| Blicket AND deficit | OR inferred, AND fails; worse 4 -> 8 objects; hypothesis sampling removes gap | GX-Chen 2025 (c15, c16) | [E] (K17) |
| Active vs passive adults | conjunctive object ID: proposers 0.12, observers 0.45, active 0.69 | Samiei 2026 (c17) | [S] |
| Scaffold on shifting-rule blicket | reasoning-eligible accuracy 73.3% -> 93.9% (p=.038); raw easy-rule accuracy 87.3% base, 77.3% CG, 89.1% CG+DB | Alderete 2026 (c18) | [S] vendor preprint |
| CoT hurt in small-model gridworld | CoT 31.9% vs default 46.7%; history 10 26.7% vs history 1 57.0%; 15 trials per cell, about +-25pp | CheeseBench (c21, d13) | [S] noisy |
| Interface alone moves score | k=4 51.9% vs k=16 20.0%; MCP vs CLI diverge in 94.3% of 2,004 episodes; repair up to +9.0 | d17, d18 | [E] (K29) |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it as a test harness or a scaffold step.

### 4.1 Triangulation protocol (the crow design)

Build a family of items sharing one causal rule. Run in this order:

1. **Source item** with arbitrary cues (cues A, B, C all correlated with the right answer). The agent must reach a criterion (the paper used 17/20 over two blocks, alpha .01).
2. **Cue-removal items**: drop cue A, then cue B (a03: transfers 1 and 2). Pass criterion 15/20.
3. **Surface-different item**: same rule, new objects, words, format (the trap-table). Score first trial plus block.
4. **Decoy item**: the old surface cue and the true cause disagree (the two-hole transfer, where one hole has a base). A cue-matcher fails here; a rule-user passes.
5. **Naive control**: a run with no source-item training faces item 3. It must score at chance (d01). If it does not, the item has a built-in answer.

The result is a profile, not a score. A pass at step 3 and a fail at step 4 means a surface regularity, not the deep rule (a04, b02).

### 4.2 First-trial versus learning-slope decomposition

Hennefield 2018 fit a logistic model per task: intercept = first-trial preference, slope = learning across insertions, plus terms for "after a success" and "after a failure" (d09). Implement as a logistic regression of correct ~ trial index + previous outcome. Read the intercept as transfer. A rising slope with an at-chance intercept means learning inside the task. For an LLM, trial index means item order inside one context, so use a fresh context per item when you want a pure first-trial measure.

### 4.3 Cue-removal and counterfactual swaps for LLMs

Keep structure, change surface:

- Letter strings: permuted or symbol alphabet (Lewis and Mitchell, b21).
- Counterfactual worlds: altered arithmetic base or rules (Wu et al., b19).
- Pearl stories: commonsense, anti-commonsense, nonsense (CLadder, a20).
- Renamed novel terms ("zerpdas" for blickets) to block contamination (c09).
- Stripping ladder: remove one supporting element at a time (Rane 2025, a19).

Record accuracy per level and the error type: valid alternative rule vs incorrect rule (humans 38.59% vs 14.67%; GPT-4 22.00% vs 32.67%, b22).

### 4.4 Hypothesis-set scaffold (blicket fix)

From GX-Chen 2025 and Piriyakulkij 2024 (c16, c19):

1. Ask the model for many hypotheses, each as a short function (16 to 96 unique ones in the 8-object world).
2. Code removes duplicates, which flattens the prior.
3. Code picks the action that eliminates the most hypotheses (information gain).
4. After each outcome, code filters or down-weights hypotheses. Use fuzzy rules; do not drop one on a single noisy test (c19).

This is G5 (code selects) in practice. The deficit it fixes: models over-weight OR rules.

### 4.5 Graph-first step

Corr2Cause: have the model first write a graph of the premises, then answer. Qwen3-32B F1 rose 32.71 -> 48.26 (c12). Pattern: explicit intermediate structure held outside the answer.

### 4.6 State machine with a contradiction monitor

Alderete 2026 (c18): a context graph (typed state machine) lifted reasoning-eligible accuracy. Dynamic behaviours (a monitor that fires on contradicting evidence) lifted how often reasoning occurred. Structure without the monitor hurt raw accuracy (combined easy-rule raw 87.3% base vs 77.3% with the graph alone). Matches G1 and G2: fire revision on a signal.

### 4.7 Interface isolation

Fix and log the action format, history length and batch size. Re-run a failed item with the simplest format (K05, K29). Report both rates.

## 5. What holds up

**Replicated, with caveats.**
- Learning the training task is common; transfer is rare. Outside labs: rooks 3 of 7 pass, 0 transfer; Darwin's finches 0 transfers; macaws and caiques 1 of 8 with named confounds; zebra finches transfer at chance with N=34; dogs never reached 60% (d02-d07) [E, K22]. Rooks, finches and hooded crows are abstract-level only; van Horik, Lambert and Muller were read in full text.
- Interface changes the score (apes: raking vs pushing; agents: CheeseBench, MCP vs CLI) [E, K05, K29].
- Aesop's fable passes are mostly learning inside the task [E, K24].
- LLM drop under counterfactual surface swaps: several labs, several tasks [E, K12].
- Blicket OR/AND asymmetry across model families [E, K17]. Reasoning models narrow it but do not close it (d15).

**Not replicated or not independent.**
- The full Taylor 2009 series (cue removal, decoy, trap-table with first-trial data) has no outside replication (K01, K22). The 14-crow follow-up is the same lab (d01).
- The ape null (Martin-Ordas) is one paper, read twice.
- Silva 2005 is one lab, small samples (10, 24, 19 students).
- Mecattaf 2024 is one paper, 12 trials per level, three models.

**Failures and boundary conditions.**
- Crows failed the decoy: 3 of 3 (a04). The transfer reached a new look, not a new cause.
- First-trial success did not predict later success: Tiga pulled into the trap on trial 1 of transfer 2, then avoided it 19 times (a03). Tiga and Slevin avoided the trap on trial 1 of transfer 3, then performed at chance for 19 trials (a04). Judge blocks, not single trials.
- Removing the colour cue broke the U-tube pass: 1 bird passed with colour, 0 passed uncovered (d08).
- Tiny samples: median N=7, 15 of 87 with zero passers (a15).
- Child baseline discrepancy: Voudouris analyses 52 children (44 after outliers); Mecattaf says 59. Unresolved (d12, K26). Do not mix.

**Moderators.** Action type (rake vs push), tool load (finger maze vs stick maze, a09), prior experience (no help in apes, b06), inhibitory control (a02, d07), training length (crows needed about 103 trials), cue visibility (d08).

**Interventions that worked.**
- Fixed-procedure CoT on CLadder: +8.37 (v1.5), +2.36 (v1.0), +9.65 on anti-commonsense, only +1.5 at rung 3 (d14).
- Graph-first on Corr2Cause: +15.55 F1 (c12).
- Hypothesis sampling on blicket (c16).
- Context graph plus monitor (c18, vendor preprint).
- Fine-tuning on towers helped in-domain only (b25).

**Interventions that did not.**
- One in-context expert example in Animal-AI: mixed (b18, c05, d11).
- Few-shot beyond the covered hypothesis space (c10).
- CoT, ReAct, Reflexion did not remove the AND deficit (c15).
- Fine-tuning across causal domains (b25).
- CoT and longer history in CheeseBench (small model, noisy; c21, d13).

## 6. Language models

**No direct test.** No paper gives an LLM the trap-tube, trap-table or Aesop task (c25, K11). The search was limited by quota and API blocks. Read this as "not found", not "does not exist".

**Embodied nearest case: Animal-AI.** Claude 3.5 Sonnet, GPT-4o and Gemini 1.5 Pro, temperature 0, ReAct, 3 runs on 40 tasks = 12 trials per level. Children did better at every level. LLMs never exceeded the top-10 competition agents. LLMs completed some level 1-2 tasks and only sporadic level 5, 6, 8; close to competition agents at L3, L8, L9, L10 only at near-floor rates (a17, d11). There are no per-task trap-tube numbers. One expert example: no reliable change (Claude fell at L1; GPT rose at L2-L3; Gemini fell at L2-L3). Controls were coarse, with one image per turn. The models are 2024; no newer run was found.

**Surface-swap tests (the LLM version of cue removal).**
- Letter strings: humans 0.753 [0.734, 0.773], GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452. GPT-4 is above GPT-3.5 but below GPT-3. Do not say "newer models do worse" from this (critique point 7).
- Wu et al.: 11 tasks, above chance but below default for all; GPT-4 had the best default spatial score and the largest counterfactual drop; PaLM-2 was the most robust (b19, b20). Default and counterfactual accuracy still correlate.
- Transitive inference (GPT-4o): 1.00 on A vs C, 0.40 on n-term trial-based, chance on novel non-adjacent pairs after 60 training trials (a19).
- CLadder (GPT-4, May 2023): plain 62.03; anti-commonsense 60.47 vs commonsense 62.27 (d14). Small story effect. CausalCoT 70.40.

**Causal inference from text.**
- Corr2Cause: 17 LLMs near random, best F1 33.38. Do not quote 29.08 as GPT-4: it is text-davinci-003 (precision 20.92, recall 47.66); the appendix label looks wrong (critique 8).
- Kiciman: 97% Tubingen, 92% counterfactual, 86% actual causality, but these lean on retrieved knowledge. Post-cutoff pairs: 80.3% GPT-3.5, 98.5% GPT-4.

**Active causal discovery.**
- Blicket: OR inferred, AND failed, across gpt-4o, gpt-4o-mini, deepseek-chat, deepseek-reasoner, qwq, gemma3:27b and four prompt styles (default, CoT, ReAct, Reflexion). The info-gain oracle reaches 1.0 (c15).
- Hypothesis sampling closes the gap (c16).
- 2026: gpt-5 and deepseek-reasoner near-perfect on OR; AND still harder; gpt-5 takes about 40 s per test vs about 20 s for humans; per-model AND values unreadable (d15).
- Adults with free interventions do well on AND (active 0.69 vs proposers 0.12). The old conjunctive handicap was a passive-evidence effect (c17).
- LaMDA: causal domain lowest (1.34 vs perception 2.91) (c09). Tool choice: text models near human on association, much worse on innovation (c07).

**Vision and physics.** Models are above chance on 2 of 3 domains, below humans; fine-tuning helps in-domain, not across (b23-b25). GPT-4V responsibility regression 0.16 vs human 0.54. Other models gave constant ratings (b23).

**What changed scores, by how much.**
- Structure held outside the answer: +8.37 (CLadder), +15.55 F1 (Corr2Cause), +20.6pp reasoning-eligible (blicket scaffold, p=.038).
- Code-held hypothesis sampling: removes the AND gap (qualitative).
- Interface: 20% to 57% (CheeseBench), up to +9.0 (MCP repair).
- One exemplar: no reliable change.
- CoT: helps on a fixed procedure, hurt in small-model exploration, untested at equal tokens on cue-removal transfer.

**Limits of this evidence.** Most numbers are GPT-3 to GPT-4 era or 2024 models. 2025-2026 papers are partly preprints. No source here runs an equal-token self-consistency baseline against a scaffold.

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory = lesson store (S9).

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Include a decoy item in every G3 check: the old surface cue and the true cause point apart. Crows passed re-skins and failed the decoy. | G3, S4, S8 | [E] | K02: a04, a06, b02 |
| 2 | Report "passed training" and "passed transfer" as separate rates. Transfer is rare when training is common. | G3, memory (S9) | [E] | K22: d02-d07 |
| 3 | Credit only first-trial accuracy as transfer. Fit the learning slope separately. Accuracy that rises inside a run is not transfer. | G3, memory (S9) | [E] | K24: d09, d10, d08 |
| 4 | Surface-swap check (renamed symbols, permuted alphabet, anti-commonsense story). Report the gap from the default form. | G3 | [E] | K12: b19, b21, a19, a20 |
| 5 | Before reading a failed transfer as missing knowledge, re-run it with the simplest action format. Report both. Pin interface settings before comparing arms. | G3, G7 | [E] | K05, K29: a09, b06, d17, d18 |
| 6 | When discovering a rule by experiment, code holds a hypothesis set, removes duplicates and picks the elimination-maximising test. | G5, S4, O (experiment choice) | [E] on blicket | K17: c15, c16, c19 |
| 7 | Do not rely on one worked example as the transfer fix. | G3 | [E] negative | b18, c05, c10, d11 |
| 8 | Report pass counts out of N with intervals, never one run. Low cost, one source. | G3, G7 | [S] | K07: a15 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 9 | Naive control: a run with no source-item training must score at chance on the transfer item. | G3 | [S] | K23: d01 |
| 10 | Pass rule: correct on functional items plus a written reason naming the causal feature; decoy counted as a separate bias check. | G3, S8 | [S] | K25: d16 |
| 11 | Cue-removal protocol (remove each cue singly, then re-skin) on an agent that solved a cue-rich task. | S4, G3 | [S] | K01: a01-a05 |
| 12 | Two-task correlation: correlate agent success on two surface-different tasks with one structure. Near zero means cue learning. | G3 | [S] | K04: a07, b05 |
| 13 | Error-type analysis: valid alternative rule vs wrong rule. | G10, memory (S9) | [S] | b22 |
| 14 | Graph-first or fixed-procedure structure for causal text questions at equal tokens. | S2, S4 | [E] Corr2Cause, [S] CLadder | K15, K14: c12, d14 |
| 15 | Contradiction monitor firing revision only on conflicting output, with a typed state. | G1, G2, S5 | [S] vendor | K19: c18 |
| 16 | Restate the goal in functional terms before choosing a tool (association vs function). | S1, O6 | [C] | K18: c07, c09 |
| 17 | Fixed-procedure CoT vs scaffold vs plain at equal tokens on the transfer items. | G1, G11 | [C] | K20, K27: c21, d13, d14 |
| 18 | Agent runs its own interventions and sees its own outcomes. | S4, O (experiment choice) | [S] | c17 |

## 8. Concrete tests on our bench

All arms at equal total tokens (prompt plus output plus any code-tool text). Fixed interface across arms. Many items and seeds; report counts with intervals.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Text trap-tube | Short text world: food, tube, trap hole, tool. Source item with 3 arbitrary cues; then cue A removed, cue B removed, re-skinned table, decoy hole-with-base | plain; scaffold (G3 checks + decoy); best-of-N | Pass rate per step; first-trial correct; decoy error vs cue-matching baseline | Plain passes steps 1-3; scaffold fails the decoy less. Gap small if the item is retrieval |
| T2 Naive control | Same transfer item, no source training | plain, scaffold | Accuracy vs chance | Must be at chance; otherwise the item is biased |
| T3 First-trial vs slope | 20 items in one context vs fresh context per item | plain, scaffold | Intercept and slope of logistic fit | Slope positive in-context, intercept near chance on novel structure |
| T4 Surface swap | ARC-like and letter-string items; default vs permuted/renamed | plain, scaffold | Accuracy gap (default minus swapped) | Scaffold gap smaller than plain gap |
| T5 Blicket AND/OR | 4 and 8 objects, OR and AND rules, agent runs its own tests | plain; ReAct; code-held hypothesis sampling | Rule accuracy, tests used | Sampling closes the AND gap on older models; unknown on reasoning models |
| T6 Interface re-run | Failed items from T1 and T5 re-run with the simplest action format | same arm, 2 formats | Pass-rate change | A rise of several points shows interface cost |
| T7 CoT vs fixed procedure | CLadder-style items at three rungs plus anti-commonsense | plain; free CoT; fixed procedure | Accuracy per rung, tokens | Fixed procedure helps rungs 1-2, little at rung 3 |
| T8 Decoy ladder | Items from mild to strong surface-cause conflict | plain, scaffold | Accuracy against conflict strength | Falls with conflict strength; slope shows reliance on surface |
| T9 Pass-rule reasons | Functional items with a written reason; code checks the named feature | plain, scaffold | Correct-with-reason rate | Reason rate lower than correct rate |
| T10 Animal-AI trap items | Mecattaf protocol, newer model, finer action set | plain vs scaffold | Per-task trap-tube success | Unknown; no prior data |

## 9. What does not transfer, and why

- **Embodiment and training length.** Crows needed about 103 trials and only 3 of 6 learned. Our agent has no such long on-line training, so "pass after learning" does not map onto a single prompt.
- **Inhibitory control and tool load.** Side switching and tool constraints (a02, a09) have no direct LLM counterpart. The LLM analogue is interface cost (K29), a different mechanism.
- **Small-N statistics.** Three birds support no inference. Our runs can be hundreds. The 3-of-3 pattern shows design, not effect size.
- **Training-set exposure.** Crows had never seen a trap-tube. An LLM may have read trap-tube and Aesop descriptions. Contamination makes first-trial success hard to read; use renamed or invented entities (c09, c13).
- **Unobservable forces.** Taylor (2020) concludes crows lack gravity-level inference. Text LLMs can recite gravity. Reciting is not using; the decoy test is the check.
- **Non-independent samples.** Crow trials are separate runs of one animal. Samples from one model are not independent (G4).
- **Fine-tuning evidence.** Tower and causal-rationale fine-tuning (b25, c22) need training; our agent is scaffold-only.
- **Verbal reasons from adults.** Silva's adults explained their choice (d16). For an LLM, reasoning text is not evidence (G10); require the reason to name a feature that code can check.
- **Old-model numbers.** GPT-3-era results (Lewis and Mitchell, Corr2Cause) do not predict 2026 models.

## 10. Open questions

1. Has any outside lab reproduced cue removal plus decoy plus trap-table with first-trial data? Not found (K22).
2. How does a current frontier LLM or scaffolded agent do on a text trap-tube at equal tokens? No study (K11).
3. Does a scaffold beat plain on Animal-AI trap items with 2025-2026 models? Mecattaf has no scaffold arm (K26).
4. Does CoT help or hurt on cue-removal transfer at equal tokens? Only task-shape answers exist (K27).
5. Is the blicket AND deficit gone for current reasoning models, and does hypothesis sampling still pay at equal tokens (d15, K28)?
6. Do CLadder rung values hold for 2025-2026 models against self-consistency? No re-run found (d19).
7. Is the child baseline 52 or 59 (d12)?
8. How much of Aesop's success is learning vs first-trial preference in Ghirlanda and Lind's numbers? Only abstract level read.
9. How much of a failed transfer is interface cost for LLM agents? Direction known, no causal-transfer test (K29).
10. What do Neilands 2016, Taylor 2014/2015, Seed 2006 and Tebbich 2007 report in full? Second-hand or abstract only.
11. Does the decoy conflict strength predict LLM errors the way it predicted crow errors?

## 11. Sources

[V] = opened and read. [M] = snippet or abstract only.

**Crow and corvid**
- [V] Taylor, Hunt, Medina, Gray 2009, Proc R Soc B 276:247-254. https://pmc.ncbi.nlm.nih.gov/articles/PMC2674354
- [V] Taylor, Roberts, Hunt, Gray 2009, Commun Integr Biol (spatial analogies, sampling error). https://pmc.ncbi.nlm.nih.gov/articles/PMC2734031 (b12 was [M]; d01 [V])
- [V] Taylor 2020, Folk physics for crows? Anim Behav Cogn 7(3):452-456. https://www.animalbehaviorandcognition.org/uploads/journals/28/AB_C_2020_Vol7(3)_Taylor.pdf
- [M] Seed, Tebbich, Emery, Clayton 2006, Curr Biol 16:697-701. https://doi.org/10.1016/j.cub.2006.02.066
- [M] Tebbich, Seed, Emery, Clayton 2007, Anim Cogn 10:225-231 (Europe PMC abstract). https://doi.org/10.1007/s10071-006-0061-4
- [M] Bagotskaia, Smirnova, Zorina 2013, hooded crows (Europe PMC abstract). https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=Bagotskaia%20hooded%20crows%20trap%20tube&format=json&resultType=core
- [M] Teschke, Tebbich 2011, Darwin's finches (abstract). https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=Teschke%20Tebbich%20finches%20two-trap%20tube&format=json&resultType=core
- [V] van Horik, Emery 2016, parrots. https://pmc.ncbi.nlm.nih.gov/articles/PMC5054051
- [V] Lambert et al. 2025, zebra finches. https://pmc.ncbi.nlm.nih.gov/articles/PMC12602269
- [V] Muller et al. 2016, border collies. https://pmc.ncbi.nlm.nih.gov/articles/PMC4749342
- [M] Taylor et al. 2014, 2015 (causal interventions). https://royalsocietypublishing.org/doi/pdf/10.1098/rspb.2014.0837
- [M] Blaisdell et al. 2006, rats. https://doi.org/10.1126/science.1121872

**Aesop's fable**
- [V] Jelbert et al. 2014, PLoS ONE 9:e92895. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0092895&type=printable
- [V] Logan et al. 2014, PLoS ONE 9:e103049. https://pmc.ncbi.nlm.nih.gov/articles/PMC4108369
- [V] Jelbert, Taylor, Gray 2015 review. https://pmc.ncbi.nlm.nih.gov/articles/PMC4594378
- [V] Hennefield, Hwang, Povinelli 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6181768
- [M] Ghirlanda and Lind 2017, Anim Behav 123:239-247. https://doi.org/10.1016/j.anbehav.2016.10.005

**Apes, humans, meta-research**
- [V] Martin-Ordas, Call, Colmenares 2008. https://pmc.ncbi.nlm.nih.gov/articles/PMC2757606
- [V] Silva, Page, Silva 2005, Learn Behav 33:47-58. https://doi.org/10.3758/BF03196050
- [V] Voelter and Call 2014. https://www.bonobosworld.org/images/zotero/Volter_et_Call-2014-The_cognitive_underpinnings_of_flexible_tool.pdf
- [M] Mulcahy and Call 2006. https://doi.org/10.1007/s10071-006-0019-6
- [M] Visalberghi and Limongelli 1994. https://doi.org/10.1037/0735-7036.108.1.15
- [M] Povinelli 2000, Folk Physics for Apes. https://academic.oup.com/book/34840/chapter/297793849
- [V] Farrar et al. 2020, Anim Behav Cogn 7(3):419-444. https://www.animalbehaviorandcognition.org/uploads/journals/28/AB_C_2020_Vol7(3)_Farrar_et_al.pdf
- [M] Schaffer et al. 2024, ungulates. https://doi.org/10.1038/s41598-024-64396-8

**AI and LLM**
- [V] Voudouris et al. 2022, Front Psychol 13:711821. https://doi.org/10.3389/fpsyg.2022.711821
- [V] Voudouris et al. 2023, Animal-AI Environment. https://arxiv.org/abs/2312.11414
- [V] Mecattaf et al. 2024. https://arxiv.org/abs/2410.23242
- [V] Voudouris, Cheke, Schulz 2025. https://arxiv.org/abs/2503.02882
- [V] Rane et al. 2025, ICML. https://proceedings.mlr.press/v267/rane25a.html
- [M] Choudhary et al. 2025. https://escholarship.org/uc/item/92x8p24r
- [V] Jin et al. 2023, CLadder. https://arxiv.org/abs/2312.04350
- [V] Jin et al. 2024, Corr2Cause. https://arxiv.org/abs/2306.05836
- [V] Sun, Nogueira, Silva 2025. https://arxiv.org/abs/2505.18034
- [V] Kiciman et al. 2024. https://arxiv.org/abs/2305.00050
- [V] Wu et al. 2024, Reasoning or reciting. https://arxiv.org/abs/2307.02477
- [V] Lewis and Mitchell 2024. https://arxiv.org/abs/2402.08955
- [V] Schulze Buschoff et al. 2024. https://arxiv.org/abs/2311.16093
- [V] Schulze Buschoff et al. 2025. https://arxiv.org/abs/2502.15678
- [V] Yiu, Kosoy, Gopnik 2024. https://arxiv.org/abs/2305.07666
- [V] Kosoy et al. 2023, LaMDA. https://arxiv.org/abs/2305.11243
- [V] Kosoy et al. 2022, overhypotheses. https://arxiv.org/abs/2206.08353
- [V] Lampinen et al. 2023. https://arxiv.org/abs/2305.16183
- [V] GX-Chen et al. 2025, COLM. https://arxiv.org/abs/2505.09614
- [V] Samiei et al. 2026. https://arxiv.org/abs/2606.06464
- [V] Alderete et al. 2026. https://arxiv.org/abs/2604.20039
- [V] Piriyakulkij et al. 2024. https://arxiv.org/abs/2402.06025
- [V] Bugaud 2026, CheeseBench. https://arxiv.org/abs/2604.10825
- [V] Tang et al. 2026, CausalPhys. https://arxiv.org/abs/2606.05966
- [V] Shi, Pang, Li 2026, MCP vs CLI. https://arxiv.org/abs/2610.34298
- [M] CausalReasonBench and clinical Pearl-ladder study (Europe PMC records, abstracts). https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CausalReasonBench&format=json&resultType=core
