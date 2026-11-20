# Hybrid and connectionist (CLARION, Sigma): deep document

Scope: explicit plus implicit knowledge in cognitive architectures (Sun's CLARION, Rosenbloom's Sigma, the Standard Model of the Mind), and every measured LLM study that uses the same split (fast/slow agents, solver hybrids, verifier loops, rule libraries). Priority for our agent: Low, background plus a few reusable patterns. Evidence ids (a01, b05, c14, d06 ...) refer to evidence_a-d.jsonl in this folder; claim ids (K01 ...) refer to claims.jsonl.

Honest headline: the cognitive-architecture side (CLARION, Sigma) is almost all single-group model fitting with no independent replication. The useful, measured evidence comes from the LLM side. It is mostly about when a fast default plus a sound external check beats slow reasoning, and when forcing explicit reasoning hurts.

## 1. What it is

A hybrid architecture keeps two kinds of knowledge side by side.
- Explicit knowledge: symbols, rules, chunks. One-shot learnable, inspectable, slow, exact when right.
- Implicit knowledge: distributed, numeric, learned gradually, fast, hard to state.

CLARION (Ron Sun) has four subsystems: action-centered (ACS), non-action-centered (NACS), motivational, and metacognitive. Each has two levels. The top level is localist chunks and rules. The bottom level is distributed micro-feature nodes in neural networks. Chunks link the levels. Implicit learning is Q-learning. Explicit learning is one-shot hypothesis testing. Bottom-up learning uses Rule-Extraction-Refinement (RER). [a01]

Sigma (Rosenbloom) is the opposite design. It has one uniform substrate: factor graphs with summary-product message passing and gradient-descent learning. Symbolic, probabilistic and neural behaviour are idioms of that one mechanism. [a15, a16]

The Standard Model of the Mind (Laird, Lebiere, Rosenbloom 2017) is the consensus of ACT-R, Soar and Sigma. Key point for us: computation is hybrid. Symbols carry numeric metadata (frequency, recency, utility, activation). Processing is parallel inside modules with a serial bottleneck, around a 50 ms cycle. [a13]

Why it matters to our agent: our scaffold already has a program layer (explicit, checkable) and a model layer (implicit, fluent). This subfield gives (a) a vocabulary for that split, (b) a human-data argument about when explicit rule search helps or hurts, (c) a body of 2023-2026 LLM work that tests the split with numbers.

## 2. History and theories in depth

Human implicit learning roots. Berry and Broadbent (1988) and Stanley et al. (1989) showed in dynamic control tasks that skill improves before people can state rules. Reber (1989; artificial grammar learning, AGL) argued implicit knowledge is rich and tacit. Berry and Broadbent also found that asking people to search for rules helps when the rule is salient and hurts when it is not. [a12, a29, b02, b26 (snippet only)]

Critics. Shanks and St John (1994) and Newell and Shanks (2014) argue awareness tests are too insensitive, so "implicit" is often just "unmeasured explicit". Not opened this session; treat as a known rival view. [b26, b27 M]

CLARION development.
- Sun and Peterson (1998) named the sources of synergy: discrete rules vs continuous values, one-shot rule learning vs gradual Q-value learning, and a bottom-up rule-extraction criterion. [b03]
- Slusarz and Sun (2001) fitted process-control data. [b01, b02]
- Sun, Slusarz and Terry (2005, Psychological Review) is the main skill-learning paper. It argues bottom-up learning and synergy. Only the abstract was read. [a02, b28]
- Domangue et al. (2004) gave human AGL data. Model-based training is slow and accurate. Memory-based training is fast and less accurate. People prefer memory-based when both are trained. Accuracy from model-based training fades over a retention interval. [a04]
- Wilson, Sun, Mathews (2009) modelled choking under pressure as a motivation-driven shift in the balance of implicit and explicit processing. [a05]
- Helie and Sun (2010) built Explicit-Implicit Interaction (EII) theory for incubation, insight and creativity. [a06]

Tasks CLARION has been fitted to (about 11): process control, serial reaction time (SRT), artificial grammar, letter counting, alphabetic arithmetic, categorical inference, discovery tasks, Tower of Hanoi, minefield navigation, metacognitive monitoring. No count of failed fits and no fit statistics are reported. [a03, b05, c11]

Sigma development. Rosenbloom's 2013 overview, the 2016 JAGI monograph (Rosenbloom, Demski, Ustun), and Ustun et al. (2018) on synthetic characters. Aim: "functionally elegant grand unification". Evaluation is qualitative against its own desiderata. [a15, a18, b21, c18]

Standard Model empirical test. Stocco et al. (2018): dynamic causal modelling on fMRI, combined N=103, four tasks (Flanker, Stroop, Raven, rapid instructed task learning). The Standard Model connectivity beat a structural-only and a fully connected alternative. [a19]

Critiques of architectures. Chella, Frixione, Lieto (2018): knowledge bases are small and homogeneous; typicality reasoning is weak. LLMs now supply the large varied knowledge, which was the main gap. [b22] Rosenbloom (2017) mapping: self-monitoring, memory/learning and symbols remain open; the symbol/vector line is soft. [a20]

Competing account of explicit knowledge emergence. The Unexpected Event Hypothesis (2022 review): conscious knowledge appears when a surprise triggers attention and top-down amplification, not by smooth bottom-up strengthening. This challenges CLARION's gradual RER and matches our G1 (revise on a signal). [a28]

Metacognition designs. CLARION has a separate metacognitive subsystem ("on top"). Laird, Lebiere, Rosenbloom, Stocco (2025) propose instead that metacognition is ordinary reasoning over self-facts held in working memory, with impasse-created substates as in Soar and Sigma. Proposal only. [a21, d16]

The LLM turn (2021-2026).
- SOFAI (Ganapini et al. 2021): fast solvers use experience, slow solvers are triggered by need, a metacognitive agent arbitrates using resources, skill, experience and expected reward. [c07]
- CoALA (Sumers et al. 2023/2024): treats LLM weights as implicit procedural memory and code/prompts as explicit procedural memory. [b20, a27 M]
- Romero et al. (2023): four integration routes (modular, agency, neuro-symbolic, CLARION-style). Exploratory, no benchmark. [b18, c12, c13]
- Sun (2024, 2025): LLMs approximate the implicit level. Explicit rules, motivation and metacognition must be added. The explicit level prompts, verifies, refines, explains or vetoes. Position papers, no measurements. [a23, a24, b06, b07, b08, c08, c10]
- Rosenbloom (2025): qualitative comparison. LLM theories win on lawfulness and usability, cognitive theories on content. [a22]

## 3. Core findings with exact numbers

Status key: E = established (3+ sources or replicated), S = single source or single group, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CLARION fits human process-control data; verbalising and instructions raise human scores | Stanley 1989 data, 12-31 per group, 200 trials; verbalise vs control F(1,73)=5.20, p<.05; model matched by t tests p<.01 | Slusarz and Sun 2001 [b01] | S (own group, qualitative ordering fit) |
| Explicit search hurts on non-salient tasks, helps on salient; instructions help always | Salient search > control p<.01; non-salient search < control p<.05; instructed > control p<.01. Model needed rule-deletion threshold 0.1 to 0.5 by hand | Berry and Broadbent 1988 via Slusarz and Sun [b02] | E (human plus LLM analogue d01-d03) |
| Letter-counting ablation: full model fits best | Human means sugar/person: control 1.97/2.85, original 2.57/3.75, memory training 4.63/5.33, simple rule 4.00/5.91. MSE full 0.113; IDN+RER 1.231; IDN+IRL 0.384 | Sun 2005 slides [b04] | S (slides, group means, no held-out test) |
| Verbal overshadowing of insight | Humans 45.8% vs 35.6% (t(74)=2.13, p<.05, about 30% relative drop); model 45.3% vs 35.3%, 5000 runs | Schooler 1993 via Helie and Sun [a11] | S (no larger-N replication found) |
| Face verbal overshadowing replicates but smaller and timing dependent | Original 22% / 25% fewer correct. RRR1: 31 labs, -4.01% [-7.15, -0.87]. RRR2: 22 labs, -16.31% [-20.47, -12.14] | Alogna et al. 2014 [d04, d05] | E for faces; insight version unreplicated |
| Incubation effect on reminiscence | Reminiscence 2.90, 3.15, 3.72, 5.00 at 0/1/5/10 min; F(3,209)=9.40 | Smith and Vela 1991 via H&S [a09] | S (mixed elsewhere) |
| Noise helps insight solving then saturates | 8 noise levels x 1000 runs; steps from 10^-2 to 10^0 each help (p<.01), beyond none | Helie and Sun 2010 [a10] | S (model only, no human stats) |
| Priming after failed rare-word association, only if feeling-of-knowing high | Human t(2100)=8.5 correct vs t(2100)=0.7 incorrect (ns); model t(2976)=6.87 vs t(2221)=1.91 ns | Yaniv and Meyer 1987 via H&S [a08] | S |
| AGL implicit learning is real but inflated | Pooled g=1.069 [.813, 1.326], 66 articles, 78 studies, 3,559 subjects; Peters bias p=.023; adults g=1.252; log training length b=-.188 p=.0006; item repetition at test +1.051 p=.0002 | Trotter et al. 2020 [b23, b24] | S (one meta-analysis; bias detected) |
| Trust in intuition does not track implicit-learning performance | r=-.05 [-.17,.08], BF01=6.02; self vs actual r=.24 | Leach and Weick 2018 [b25] | S |
| Standard Model connectivity best fit fMRI | N=103; posterior >=0.99; d>124 vs structural, d>=30 vs fully connected | Stocco et al. 2018 [a19] | S (preliminary, 2 rivals) |
| Sigma modest accuracy | WSD 78% (Senseval-3), 70.3% (Semcor); POS 90.3% = most-common-tag baseline; digits 99.2% | Rosenbloom et al. 2016 [a16] | S |
| Sigma graph speedups | about 100x at 100 words, about 1000x at 1000 words; 15-20% on loopy graphs | [a17] | S |
| Sigma frozen-lake style test | Reached goal 79% of test runs | Ustun et al. 2018 [c18] | S |
| Fast small model plus slow GPT-4 planner on ScienceWorld | SwiftSage 84.68 vs Reflexion 45.34, ReAct 36.43, SayCan 33.82, DRRN 15.56. Tokens/action 757.07 vs 1855.84 / 1971.03 / 2983.46. GPT-3.5: 62.22 vs ReAct 19.76 | Lin et al. 2023 [a25, b11-b13, c14] | S (one paper, fine-tuned fast module, no token-matched control) |
| Small LLM plus metacognitive loop beats reasoning model | Graph colouring size 25: 42% vs 2%. DebugBench Python 70% vs 37%, C++ 73% vs 40% | SOFAI-LM, Khandelwal 2025 [c01] | S (one group, 8B models) |
| Feedback rounds: most gain in first 5 | LLM, @5, @10, @15; biggest jump LLM to @5. Graph colouring n=5 about 20% to about 80% over 5 iterations | [c02, c05] | S (read from plots) |
| What history to pass depends on task | Graph colouring: problem only best, negative examples harmful. Debugging: best attempt / full history help. Multi-line feedback plus minimal memory 42% at about 27 s | [c03] | S |
| SOFAI-v2 on hard graph colouring | n=50 unsolvable: 53.85% vs 3.85% (v1 and S1). Mixed 27.72% vs 2.11%. Edge sweep: about 94% vs v1 74%, S1 68%, S2 51% | Khandelwal et al. 2025 [c04, c23] | S |
| Plan-SOFAI | 700 instances: 671 solved vs 587 random memory, 593 Jaccard; about 19% faster than Fast Downward | Fabiano 2023 [c06] | S |
| LLM plus symbolic solver (Logic-LM), GPT-4 standard / CoT / Logic-LM | ProofWriter 52.67/68.11/79.66; FOLIO 69.11/70.58/78.92; LogicalDeduction 71.33/75.25/87.63; AR-LSAT 33.33/35.06/43.04; PrOntoQA 77.40/98.79/83.20 | Pan et al. 2023 [a26, c22] | C (loses to CoT on PrOntoQA) |
| Logic-LM translation dependence | ChatGPT avg +39.2% over standard, +18.4% over CoT (ChatGPT, not GPT-4). Executable rate PrOntoQA 99.4%/100%; FOLIO 66.7% to 84.3% with refinement; AR-LSAT executable 11.3% before refinement | [a26, c24] | S |
| Sound verifier needed | GPT-4 about 12% plans; Blocks World 82% (VAL, 15 rounds); Logistics 70%; Mystery BW about 10% | Kambhampati 2024 [b19, c20] | E |
| Self-verification fails | Game of 24: 5% standard, 3% LLM+LLM, 36-38% sound. Graph colouring 16/2/34-38. Blocksworld 40/55/60-87. LLM verifier false negatives 95.8%, 97.09% | Stechly et al. 2024 [d10, d18] | E |
| Intrinsic self-correction lowers accuracy | GPT-4 GSM8K 95.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1; with oracle labels GSM8K 75.9 to 95.5 | Huang et al. 2024 [d11] | E |
| Critique content matters little with a sound check | Binary vs first-error vs all-error: Game of 24 36/38; graph colour 38/37/34; Blocksworld 60/87/83. Resample k=25: 42/44/72 | [d18] | S |
| Rule library with filter helps, random rules hurt | CLUTRR GPT-4 50.6 to 64.3 (+13.7); base-16 57.4 to 78.4 (+21.0); random conclusions 9.9 (-40.7) and 23.7 (-33.7). GPT-3.5 21.2 to 37.6 | Zhu et al. 2024 HtT [d12] | S (2 task families) |
| Trajectory feedback corrects wrong LLM specs | Craftax diamond 88.2% vs 46.9%; without trajectory analysis 67%; after rule change 5.4% vs above 86% | SCALAR 2026 [d13] | S |
| LLM writes Soar rules with critic | Water jugs: Gemini-2.5-pro 55% to 86%; qwen-max 66% to 91%; manual rules 84%; zero-shot 0% | NL2GenSym 2025 [d14] | S |
| Forced CoT hurts where verbalising hurts humans | AGL GPT-4o 87.50 to 64.40 (p<.0001); Claude 3 Opus 70.7 to 62.7; Claude 3.5 Sonnet 65.9 to 67.7 (no drop). o1-preview 57.7 vs GPT-4o direct 94.0 on 440-item subset. Exceptions task GPT-4o 2.9 to 12.5 passes (+331%). Faces GPT-4o 64.0 to 51.2 | Liu et al. 2025 [d01-d03] | S (one paper, model dependent) |
| Correct hint does not repair CoT loss | Bigram steering 68.43 vs zero-shot 87.50, CoT 64.40; ToT 64.55 | [d02] | S |
| CoT gain is concentrated | Symbolic +14.2, math +12.3, logic +6.9, other about +0.7; about 95% of MMLU gain on items with "="; plan plus tool solver beats CoT on GSM8K-Hard, ContextHub, FOLIO | Sprague et al. 2025 [d09] | E (meta-analysis over 100+ papers) |
| Draft-agreement routing | Qwen3-8B MATH-500 DART 88.2 vs always-think 85.6 vs no-think 76.6 (35% fewer total tokens); HumanEval 78.7 vs 59.1; matches always-think on 13 of 14 pairs with 32-73% fewer thinking tokens | Lee et al. 2026 DART [d06] | S (independent group, not equal-token) |
| Self-reported confidence is a poor router | MC-Conf Qwen3-8B Olympiad 54.9 vs DART 69.8 | [d07] | S |
| Difficulty router beats proportion-matched random | +8.3 macro points at same 41/35/24% path mix; 89.6% vs self-consistency 83.6%; cost 0.42 vs 0.75 | ODAR 2026 [d08] | S |
| Selection without exact verifier saturates | MATH Llama-3-8B coverage 82.9% to 98.44% (100 to 10,000 samples); vote/reward pick 40.50% to 41.41%. SWE-bench Lite 15.9% to 56% at 250 samples with tests | Brown et al. 2024 [d17] | E |
| Distilling System 2 into System 1 | Last letter 30.0 to 98.0%; coin flip 56.1 to 75.69%; GSM8k 9.40 / 52.77 / 7.13 (fails) | Yu et al. 2024 [b15-b17, c15] | S (needs training) |
| Talker-Reasoner failure modes | Qualitative only: stale-belief talker, snap-judgement talker | Christakopoulou 2024 [b14, c16] | S |
| DPT-Agent real-time collaboration | Overcooked human study N=71: Map 1 111.53 vs ReAct 99.03; Map 2 160.63 vs 115.00. ToM module did not always help | Zhang et al. 2025 [c17] | S |
| LLM cognitive reflection | CRT correct: davinci-003 5%, ChatGPT-3.5 59%, GPT-4 96%, humans 38% | Hagendorff 2023 [c21, c25] | S |
| No Sigma plus LLM quantitative test | Three 2024-25 Rosenbloom-group papers are conceptual | [d15, d16, a30] | n/a |

## 4. Mechanisms and models

Written so an engineer could build each one. Each is a program around model calls.

### 4.1 CLARION two-level action selection and learning
State: top level = list of rules (condition chunks to action chunk, with weights). Bottom level = function approximator (neural net) from state features to Q-values per action.
Per step:
1. Compute bottom-level action probabilities from Q-values (Boltzmann).
2. Match top-level rules. Get rule-recommended actions.
3. Combine by stochastic selection weighted by each level's recent performance (performance-weighted arbitration). [b10]
4. Act. Get reward.
5. Implicit update: Q-learning on the bottom net.
6. Bottom-up (RER): if an action succeeded, create or generalise a rule from the state-action pair. Keep generalising while information gain holds. Specialise (add dimensions or remove values) if a rule starts to fail. Delete rules below a threshold. Rule choice by information gain or Boltzmann over utility. [a01, b10, c12]
7. Top-down: give explicit rules and instructions as extra reinforcement or direct inputs to the bottom net.
Parameters that mattered in fits: rule deletion threshold (0.1 vs 0.5) and level weights (0.5/0.5), changed by hand per task. [b02]

### 4.2 EII loop for insight and incubation (Helie and Sun)
Bottom level: bidirectional associative network (NDRAM) that settles. Each settle step ("spin") is about 350 ms. [a07]
Loop:
1. Implicit settle (several spins). Temperature or noise is the creativity knob.
2. Send result bottom-up (explicitation) to chunks.
3. Explicit level runs its rules in parallel.
4. Integrate both results, form a Boltzmann distribution, take the mode, set internal confidence level (ICL).
5. If ICL is above threshold, output. Else send the answer back down (abductive step) and iterate.
Findings: noise helps then saturates [a10]. Verbal processing dominating the explicit side reproduces overshadowing [a11]. 20,571 spins is about 2 hours of simulated time [a07].

### 4.3 Four-step creative loop (Sun 2025 proposal)
Explicit prep (set goal, constraints), implicit work (LLM generates), explicit validate, if wrong send back with feedback. Same as generate, verify, return-with-feedback. Untested. [b07]

### 4.4 SwiftSage (fast/slow agent)
Fast module: small seq2seq (Flan-T5 770M) fine-tuned by imitating oracle trajectories. Slow module: GPT-4 prompted for subgoal planning and action grounding (grounding questions Q1-Q3, about +2 points on short tasks). Switch to slow when any of: five consecutive steps with zero reward; invalid predicted action; critical decision; unexpected observation. Hand-written rules. [a25, b13]

### 4.5 SOFAI and SOFAI-LM (metacognitive controller)
Controller (code, not model) arbitrates using resources left, solver skill from past experience, expected reward. Two phases: cheap fast attempt first, careful phase after. [c07]
SOFAI-LM loop:
1. Fast LLM proposes (for example a graph colouring).
2. Code checks it.
3. Failing constraints are fed back as structured text.
4. Repeat up to N rounds (about 5 gets most of the gain).
5. On failure call the slow reasoning model. History passed to it is task dependent (PO, BA, FH).
SOFAI-v2 adds episodic memory of past solved instances as in-context examples. [c01-c05, c23]
Plan-SOFAI: case-based fast solver, classical planner as slow solver. Experience lets the fast solver take over repeated problems. [c06]

### 4.6 DART draft-agreement routing (training-free)
Sample two cheap no-think drafts. If they agree, accept. Else switch to thinking with a budget set from draft entropy. Matches always-think with 32-73% fewer thinking tokens. For code, agreement must be execution-based (text agreement collapsed to about 10% on HumanEval). [d06, d07]

### 4.7 ODAR difficulty router
Learned router picks fast (512 tokens), medium, or slow (1024 tokens) agent per item (path mix 41/35/24%), then a fusion step. Beat random routing at the same mix by 8.3 macro points. [d08]

### 4.8 Logic-LM (translate, solve, refine)
LLM translates the problem to a formal language (Prover9, Z3, python-constraint, Pyke). Solver runs. If the program errors, error text goes back to the LLM for repair. Count unexecutable as fail or fall back to CoT. The execution check is code. [a26, c24]

### 4.9 LLM-Modulo generate-test
Generator LLM proposes a plan. Sound external verifiers (for example VAL) return critiques or pass/fail. Repeat up to 15 rounds. Binary feedback gets most of the gain. Resampling with the exact check but no critique text also works. [b19, d10, d18]

### 4.10 Hypotheses-to-Theories rule library (HtT)
Induction stage: on about 2,000 training examples the LLM proposes rules while solving. Count how often each rule appears (coverage) and how often the answer was right when it was used (confidence). Keep rules above thresholds in a library. Deduction stage: put the library in context for new items. Wrong rules were 65% (CLUTRR) and 81% (base-16) of remaining CoT errors. The library must fit in context. [d12]

### 4.11 SCALAR (explicit spec, implicit policy, trajectory correction)
LLM writes skill specs (preconditions and effects). RL trains policies per skill. RL trajectories are fed back to the LLM to correct the specs. Without the trajectory step, a changed crafting rule leaves success at 5.4%. [d13]

### 4.12 Sigma in brief
Factor graph. Each function is a factor. Inference by summary-product message passing. Learning by gradient descent on factor functions. 50 ms cognitive cycle with perception, graph-solution and graph-modification phases. Cost grows with treewidth and the number of nonzero regions. [a15-a18]

### 4.13 Standard Model structure
Modules (perception, motor, working memory, declarative long-term, procedural long-term), one working memory, symbols with quantitative metadata, relations may not be defined over the numeric metadata, serial bottleneck at the deliberate-act level, learning both Bayesian/statistical and reinforcement. [a13]

## 5. What holds up

Holds up (replicated or several independent sources):
- Explicit search or verbalisation hurts when structure is hard to state. Seen in humans (Berry and Broadbent; AGL; face overshadowing registered replication across 53 lab runs) and LLMs (Liu 2025). The effect is real but moderated: RRR1 -4.01% vs RRR2 -16.31% depended on task order. [b02, d01-d05]
- Self-verification by the same model does not work. Sound external verifiers do. At least three independent groups (Kambhampati, Stechly, Huang). [b19, d10, d11, d18]
- CoT helps mainly on symbolic, math and logic items. Meta-analysis of 100+ papers. [d09]
- Without an exact verifier, vote and reward-model selection stalls near 41% while coverage reaches 98%. [d17]
- Wrong stored rules are worse than no rules. [d12, d13, c13]

Fragile or single-source:
- All CLARION human-data fits are by Sun's own group. No independent replication, no fit statistics, no failed-fit list found. Parameters were changed by hand between phases. [b02, b05, d19]
- Schooler 1993 insight narration (45.8% vs 35.6%): no larger-N replication found. The 2010 CLARION paper does not discuss mixed replications. [a11]
- Reminiscence and incubation effects have mixed results outside the model paper. [a09]
- Human implicit learning is inflated by publication bias (Peters p=.023), training length and item repetition. The implicit vs explicit split itself is disputed (Newell and Shanks, not read). [b23, b24, b27]
- SwiftSage: the gain may come from the fine-tuned fast module (imitation of oracle trajectories), not from the dual-process idea. The GPT-3.5 result shows the fast module carries much of the score. No token-matched ablation. [a25, b12]
- SOFAI and SOFAI-LM: one group, graph colouring and debugging, 8B models, compared to a reasoning model under fixed time limits. [c01, c04]
- Logic-LM is not a clean win. It loses to CoT on PrOntoQA (83.20 vs 98.79). The "+39.2%" figure is the ChatGPT average, not GPT-4. [a26]
- Papers counted twice: b11/b12/b13/c14/a25 are one paper; b15/b16/b17/c15 one paper; b19/c20 one paper. Independent source counts are mostly 1. [critique.md]

Moderators found:
- Salient vs non-salient structure (humans, LLMs).
- Task type: symbolic vs non-symbolic (Sprague).
- Model: Claude 3.5 Sonnet shows no CoT drop on AGL (65.9 to 67.7). Small Llamas drop only -1.8 to -2.2. [d01]
- Delay between description and test (face overshadowing). [d04]
- Soundness of the verifier. [d10]
- Obfuscation: when the generator cannot produce candidates, the verifier loop stalls (Mystery BW about 10%). [b19]
- Task type decides what to carry into retries (graph colouring: nothing; debugging: best attempt). [c03]

Interventions that worked: sound external check plus resampling; fast-default routing with agreement or difficulty triggers; filtered rule libraries; trajectory feedback to correct specs; solver offload on symbolic tasks.

Interventions that did not work: LLM self-verification; unfiltered or random rules; telling the model the right strategy (bigram hint) under forced CoT; tree-of-thought on AGL; passing failed attempts to the retry on graph colouring; distilling CoT math into direct answers; self-reported-confidence routing.

## 6. Language models

How LLMs behave on the tasks central to this subfield.
- Intuitive responding. Older GPT-3 models answer cognitive-reflection and semantic-illusion items intuitively: intuitive wrong answers 70-90% vs humans 55%. Correct on CRT: davinci-003 5%, ChatGPT-3.5 59%, GPT-4 96%, humans 38%. Telling davinci-003 to reason step by step moved chain-of-thought responses from 0% to 100%. Blocking it in ChatGPT dropped them from 97% to 0. CoT is the System 2 switch. Caveat: items may be in training data. [c21, c25]
- Implicit-learning tasks with CoT. AGL GPT-4o 87.50 direct vs 64.40 CoT (-23.1, p<.0001), stable across temperature 0 to 0.7 (direct 87.5-88.3, CoT 63.6-64.4). Claude 3.5 Sonnet 65.9 vs 67.7 (no drop). o1-preview 57.70 vs GPT-4o direct 94.00 on a 440-item subset. Exceptions task: GPT-4o 2.9 passes to 12.5; Claude 3.5 Sonnet 2.3 to 6.4. Faces: GPT-4o 64.0 to 51.2, Claude 3 Opus 44.0 to 29.6, Claude 3.5 Sonnet 97.8 to 94.8. The direct comparison is not token matched. [d01-d03]
- Hybrid fast/slow agents. SwiftSage 84.68 vs ReAct 36.43 (GPT-4). With GPT-3.5, 62.22 vs 19.76. About 757 tokens per action vs about 1,971 (ReAct). [a25]
- Metacognitive wrapper. Granite 3.3 8B plus loop: 42% vs 2% (graph colouring, size 25); Python debugging 70% vs 37%. [c01]
- Routing. DART matches always-thinking on 13 of 14 pairs with 32-73% fewer thinking tokens. ODAR +8.3 macro points over proportion-matched random routing. [d06, d08]
- Solver offload. Logic-LM GPT-4 gains of +8.4 to +12.4 over CoT on four datasets, but -15.6 on PrOntoQA. Sprague: solver beats CoT on symbolic items; parse failures counted as guesses. [a26, d09]
- Verification. A sound verifier turns 5% into 36-38% (Game of 24). An LLM self-verifier gives 3%. GPT-4 self-correction on GSM8K 95.5 to 89.0. These are 2023-24 models. Reasoning models are untested. [d10, d11]
- Rule memory. HtT +13.7 to +21.0 with filtering. Random rules -33.7 to -40.7. [d12]
- Cognitive-architecture couplings. NL2GenSym on Soar: 55% to 86% (Gemini-2.5-pro); zero-shot rule writing 0%. SCALAR 88.2% vs 46.9%. No Sigma plus LLM measurement exists in the sources opened. [d13-d16]
- The claim "LLM = implicit level" (Sun 2024, 2025) is untested. No paper compares LLM output against implicit-learning signatures beyond the Liu 2025 CoT effect. [a23, b06]
- Anecdote only: Sun's tetrahedron prompt hint (N=1; the hint also says the answer is short). [b08]

What changed performance, by how much: external sound checks (+31 to +33 points on Game of 24), routing by disagreement (up to 73% fewer thinking tokens at similar accuracy), filtered rules (+13.7 to +21.0), solver offload on symbolic items (about +8 to +12 on GPT-4), forced CoT on pattern tasks (-12.8 to -23.1 for the models that drop).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = stored knowledge. The architecture detail is background only. The useful part is the measured LLM patterns.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Every veto, validate or revise step uses a sound external signal (code run, solver, test, retrieved fact). No same-model self-veto without ground truth. Extends G2 and G5. | G2/G5 | [E] | d10, d11, d18, b19, K08, K18 |
| Verifier loop: generate, check by code, return pass/fail (or first error), retry. Resample with the exact check rather than writing long critiques. Cap rounds (about 5 to 15). | O / S4 | [E] for the loop; [S] for the round cap | b19, d10, d18, c02 |
| Do not force a "state the rule" or step-by-step narration on pattern or perceptual items whose structure is hard to state. Keep a direct-answer path. Model dependent. | G11 / S0 | [E] for humans; [S] for LLM size (one paper) | b02, a29, d01-d04, K02 |
| CoT only where symbolic, math, or logic. Route at S0 by task type. | S0 / G12 | [E] | d09, K21 |
| Validate before committing anything to rule memory. Unfiltered wrong rules cost more than no rules. | memory / G | [E] for the harm; [S] for the filter design | d12, d13, c13, b18, K17 |
| Use disagreement or an executable check, not the model's stated confidence, as the escalation trigger. | G1 / G12 | [E] that self-checks fail; [S] for DART | b25, d07, d17 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Fast-default plus escalate-on-failure vs always-slow at equal total tokens (SwiftSage, SOFAI-LM, DART, ODAR all lack a strict equal-token test). | S0 / S6 / G11 / G12 | [S] | a25, c01, d06, d08, K05, K06 |
| Per-task formalise-and-solve vs CoT router; check solver execution rate. | O (offload) | [C] | a26, d09, K04 |
| Bottom-up rule extraction from successful outputs with coverage/confidence filter and trajectory correction. Open-ended tasks untested. | memory / G | [S] | d12, d13, K19 |
| Retry context: problem only vs best attempt vs full history, by task type. | O / S6 | [S] | c03, K07 |
| Direct-answer path for pattern items: route to no-CoT and compare, per model. | G11 | [S] | d01-d03, K20 |
| Four-step creative loop (prep, generate, validate, send back). | S3 / S4 | [S] | b07, K14 |
| Wait gate between fast and slow answerer (avoid snap-judgement and stale-belief answers). | S6 | [S] | b14, K10 |
| Temperature sweep on stuck problems with a saturation point. | O / G12 | [S] (model only) | a10 |
| Keep failed attempts in context as primes rather than only errors. | memory | [S] (model only) | a08 |
| Surprise-triggered rule revision (revise only when a check fails) vs smooth continuous updating. | G1 | [C] | a28 |

## 8. Concrete tests on our bench

All arms at equal total tokens (input plus output, setup included, per G7).

1. Fast-default vs always-slow.
 - Items: mixed easy and hard items (math, logic, puzzles, code) with exact checkers.
 - Arms: (A) plain model, single long reasoning call; (B) two cheap drafts, accept on agreement or passed check, else one thinking call with the remaining budget; (C) B with proportion-matched random escalation.
 - Metric: accuracy at fixed token budget; tokens to reach accuracy X.
 - Expected: B >= A at equal tokens. B beats C by several points (ODAR saw +8.3 macro points).
2. Forced rule-finding vs direct.
 - Items: AGL-like grammar judgements, exceptions-learning lists, face or pattern matching, against salient-rule items (arithmetic sequences).
 - Arms: direct answer; forced "state the rule then answer". Run on each of our models.
 - Metric: accuracy per model, with a CI on any CoT drop.
 - Expected: drop of 10-23 points on non-salient items for some models; none or a gain on salient items (Liu 2025: GPT-4o -23.1; Claude 3.5 Sonnet about 0).
3. Self-veto vs sound veto.
 - Items: Game of 24, graph colouring, Blocksworld-style planning (verifier available as code).
 - Arms: no veto; LLM veto; code veto with binary feedback; resample with exact check.
 - Metric: accuracy; false-negative rate of the LLM veto.
 - Expected: LLM veto at or below baseline; code veto about +30 points. Retest on a reasoning model, because the old numbers are 2023-24 GPT-4.
4. Formalise-and-solve vs CoT router.
 - Items: logic sets (ProofWriter, FOLIO, LogicalDeduction, AR-LSAT, PrOntoQA).
 - Arms: CoT; solver pipeline with repair; router by task type; router by draft agreement.
 - Metric: accuracy and solver executable rate.
 - Expected: solver wins on constraint-style items; the router recovers the PrOntoQA loss.
5. Rule memory with a filter.
 - Items: tasks with changing rules (kinship relations, base-n arithmetic, a game with a mid-run rule change).
 - Arms: no memory; unfiltered LLM-extracted rules; coverage and confidence filter; filter plus trajectory correction.
 - Metric: accuracy before and after the rule change; harm from wrong rules.
 - Expected: filter +10 to +20; unfiltered below no-memory.
6. Retry context.
 - Items: global-consistency (graph colouring) vs local-fix (code debugging).
 - Arms: problem only; best attempt; full history; at 1, 5, 10 rounds.
 - Metric: success at equal tokens.
 - Expected: problem-only best on global tasks; best attempt or history on local tasks.
7. Confidence vs verifier selection.
 - Items: math and code with exact checkers, k samples.
 - Arms: model-stated confidence weighting; majority vote; exact check; reward-model pick.
 - Metric: accuracy as k grows.
 - Expected: all but the exact check plateau.
8. Verbal overshadowing of insight (low priority).
 - Items: about 30 insight puzzles with an interruption.
 - Arms: silent retry; forced narration; unrelated task between attempts.
 - Metric: solve rate.
 - Expected: small or null. The human insight result lacks a larger-N replication.

## 9. What does not transfer, and why

- CLARION's neural bottom level is a small backprop net trained online. We cannot update an LLM (no training). Bottom-up learning from reinforcement has no equivalent unless we store rules or examples. Under LLMs it needs a success signal that is often missing. [c09]
- Time mapping (350 ms per spin, incubation over minutes) means nothing for a stateless model. A pause does nothing unless sampling or re-prompting supplies the spins. [a07, a09]
- Human implicit learning is not the same as LLM "intuition". The match (CoT hurts) is behavioural. The mechanism is untested. [a23]
- SwiftSage's fast module is fine-tuned on oracle trajectories. We cannot train. Distillation (Yu et al.) is out of scope and fails for CoT math. [a25, b16]
- Sigma's one-substrate design is deliberately not copied. We keep code and model separate. Unification costs speed (50 ms target, virtual humans 250 ms). [a15]
- Sigma and the Standard Model have no LLM measurement. Sigma accuracy is baseline level (POS 90.3%). Expect no accuracy gain from adopting the architecture itself. [a16, d15]
- Real-time latency designs (Talker-Reasoner, DPT-Agent) matter in games and voice. For batch items they add only the wait-gate lesson. [b14, c17]
- Fit to human data says little about benchmark gains. CLARION fits group means with hand-tuned parameters. [a14, b02]
- The Standard Model fMRI result concerns cognitive-control tasks with two rival models. It says nothing about scaffold value. [a19]
- Position papers (Sun, Romero, CoALA, Rosenbloom 2025) give design vocabulary but no measurement. [b18, a22]

## 10. Open questions

- Does the CLARION synergy (rules plus implicit learner beat either alone) hold for LLM plus rule layer at equal tokens? No test exists. [K01, K14]
- Independent replication and fit statistics of CLARION fits (process control, SRT). Search was cut short by rate limits, so absence is not proof. [d19]
- Schooler 1993 insight narration at larger N, and its LLM analogue with forced narration. [a11]
- Does the CoT penalty on pattern tasks hold for reasoning models? o1-preview looked worse than GPT-4o direct (57.7 vs 94.0 on a subset) but cannot have reasoning turned off. [d01]
- Do the sound-verifier and self-verifier results hold for reasoning models? [d10, d11]
- Is a fast-default router better than always-slow at a strictly equal total token budget, outside the SOFAI group? [c01, d06]
- Can the PrOntoQA loss of formalise-and-solve be predicted per item? [a26, d09]
- Does rule extraction on open-ended tasks, with rules stored in memory, avoid cascading harm? [d12, d13]
- Does an explicit "impasse" substate (Soar/Sigma style) help an LLM agent more than a program-controlled retry? [a21, d16]
- Sigma or Standard Model plus LLM quantitative results (none found for 2024-2026). [a30, d15]
- Is CLARION's performance-weighted arbitration between a fast answer and a rule answer better than a fixed rule? [b10]
- Does the Unexpected Event Hypothesis (explicit rule only after surprise) beat smooth rule updating? [a28]

## 11. Sources

[V] = opened and read this session (full text or substantive pages). [M] = snippet, abstract only, or cited by another source.

- [V] Wikipedia, CLARION (cognitive architecture), 2026 fetch. https://en.wikipedia.org/wiki/CLARION_(cognitive_architecture) (a01, a03)
- [M] Sun, Slusarz, Terry (2005) Psychological Review 112(1):159-192, abstract only. https://pubmed.ncbi.nlm.nih.gov/15631592 ; https://doi.org/10.1037/0033-295X.112.1.159 (a02, b28)
- [M] Domangue, Mathews, Sun et al. (2004) JEP:LMC 30(5), abstract only. https://pubmed.ncbi.nlm.nih.gov/15355132 (a04)
- [M] Wilson, Sun, Mathews (2009) Neural Networks 22, abstract only. https://pubmed.ncbi.nlm.nih.gov/19608380 (a05)
- [V] Helie and Sun (2010) Psychological Review 117(3). http://matt.colorado.edu/teaching/highcog/readings/hs10.pdf (a06-a12, a29)
- [V] Laird, Lebiere, Rosenbloom (2017) A Standard Model of the Mind. https://sites.usc.edu/rosenbloom/recent-publications/ (a13, a14, a30)
- [V] Rosenbloom, Demski, Ustun (2016) Sigma, JAGI 7(1). https://doi.org/10.1515/jagi-2016-0001 (a15-a17)
- [V] Rosenbloom (2013) Sigma overview. https://www.dropbox.com/s/iyfm9fet0fivb37/Sigma%20AISBQ%20D.pdf?dl=1 (a18)
- [V] Stocco et al. (2018) Standard Model neuroimaging, CogSci. https://www.dropbox.com/s/fhejn2xesujvbxx/stocco_laird_lebiere_rosenbloom_2018_empirical.pdf?dl=1 (a19; not re-opened in the critique pass)
- [V] Rosenbloom (2017) Lessons from mapping Sigma onto the Standard Model. https://www.dropbox.com/s/bsfsyot89xl28zo/SM%20Symp%20Sigma%202017%20Revised%20D.pdf?dl=1 (a20)
- [V] Laird et al. (2025) Metacognition and the Common Model. https://arxiv.org/abs/2506.07807 (a21, d16)
- [V] Rosenbloom (2025) Qualitative comparative evaluation of cognitive and generative theories. http://www.cogsys.org/proceedings/2025/paper-2025-5.pdf (a22)
- [V] Sun (2024) Can a cognitive architecture fundamentally enhance LLMs? https://arxiv.org/abs/2401.10444 (a23, a24, b08, b09, c10)
- [V] Lin et al. (2023) SwiftSage. https://arxiv.org/abs/2305.17390 (a25, b11-b13, c14)
- [V] Pan et al. (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (a26, c22, c24)
- [M] Sumers et al. (2023/2024) CoALA, title page only in a27 (b20 gives a framework summary). https://arxiv.org/abs/2309.02427
- [V] PMC9177494 (2022) What triggers explicit awareness in implicit sequence learning, skimmed. https://pmc.ncbi.nlm.nih.gov/articles/PMC9177494/ (a28)
- [V] Slusarz and Sun (2001) CogSci 23. https://escholarship.org/uc/item/0fp857zf (b01-b03)
- [V] Sun (2005) NeSy05 slides. https://people.cs.ksu.edu/~hitzler/nesy/NeSy05/sun.pdf (b04, b05)
- [V] Sun (2025) CLARION plus LLMs case study. https://arxiv.org/abs/2509.10972 (b06, b07, b10, c08, c09)
- [V] Christakopoulou et al. (2024) Talker-Reasoner. https://arxiv.org/abs/2410.08328 (b14, c16)
- [V] Yu et al. (2024) Distilling System 2 into System 1. https://arxiv.org/abs/2407.06023 (b15-b17, c15)
- [V] Romero et al. (2023) Synergistic integration of LLMs and cognitive architectures. https://arxiv.org/abs/2308.09830 (b18, c12, c13)
- [V] Kambhampati et al. (2024) LLM-Modulo. https://arxiv.org/abs/2402.01817 (b19, c20)
- [V] Ustun et al. (2021/2018) Controlling synthetic characters, Sigma. https://arxiv.org/abs/2101.02231 (b21, c18)
- [V] Chella, Frixione, Lieto (2018) Standard Model representational issues. https://arxiv.org/abs/1804.08299 (b22)
- [V] Trotter et al. (2020) AGL meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC7496870/ (b23, b24)
- [V] Leach and Weick (2018) Veracity of intuitions. https://pmc.ncbi.nlm.nih.gov/articles/PMC5753840/ (b25)
- [M] Reber (1989) Implicit learning and tacit knowledge, quote via Sun. https://doi.org/10.1037/0096-3445.118.3.219 (b26)
- [M] Newell and Shanks (2014) Unconscious influences on decision making, claim from memory. https://doi.org/10.1017/S0140525X12003214 (b27)
- [V] Khandelwal, Rossi et al. (2025) SOFAI-LM. https://arxiv.org/abs/2508.17959 (c01-c03)
- [V] Khandelwal et al. (2025) SOFAI-v2 graph colouring. https://arxiv.org/abs/2412.01752 (c04, c05, c23)
- [V] Fabiano et al. (2023) Fast and Slow Planning. https://arxiv.org/abs/2303.04283 (c06)
- [V] Ganapini et al. (2021) Thinking Fast and Slow in AI. https://arxiv.org/abs/2110.01834 (c07)
- [M] Sun CLARION page (pointer, not the exact slide file). https://sites.google.com/site/drronsun/clarion (c11)
- [V] Zhang et al. (2025) DPT-Agent, column order not verified. https://arxiv.org/abs/2502.11882 (c17)
- [M] Rosenbloom et al. Sigma neural extensions, cited in Ustun 2018. https://arxiv.org/abs/2101.02231 (c19)
- [V] Hagendorff (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206 (c21, c25)
- [V] Liu et al. (2025) Mind Your Step (by Step). https://arxiv.org/abs/2410.21333 (d01-d03)
- [V] Alogna et al. (2014) Registered Replication Report, Schooler and Engstler-Schooler. https://doi.org/10.1177/1745691614545653 ; manuscript https://eprints.whiterose.ac.uk/id/eprint/81917/ (d04, d05)
- [V] Lee et al. (2026) DART. https://aclanthology.org/2026.findings-emnlp.1347.pdf (d06, d07)
- [V] Ma et al. (2026) ODAR. https://arxiv.org/abs/2602.23681 (d08)
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (d09)
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-verification limitations. https://arxiv.org/abs/2402.08115 (d10, d18)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d11)
- [V] Zhu et al. (2024) Hypotheses-to-Theories. https://arxiv.org/abs/2310.07064 (d12)
- [V] Zabounidis et al. (2026) SCALAR. https://arxiv.org/abs/2603.09036 (d13)
- [V] Yuan et al. (2025) NL2GenSym. https://arxiv.org/abs/2510.09355 (d14)
- [V] Rosenbloom et al. (2025) Neural theories of consciousness on the Common Model, https://arxiv.org/abs/2506.12224 (d15); Rosenbloom et al. (2024) emotion, https://arxiv.org/abs/2412.16231 (d16)
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d17)
- Search note (d19), no source: no independent CLARION fit replication found; APIs were rate limited.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 4 established claims: 1 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C02.08-K02** (now single-source: the sources are not independent). Slusarz and Sun 2001 does report the Berry and Broadbent 1988 simulation (salient experimental > control, non-salient experimental < control, instructions help in all conditions, p<.01), but Helie and Sun 2010 is by the same lab and only restates the 'hard to extract' half in passing, and the primary Berry and Broadbent paper is not among the sources; Liu 2025 tests LLM chain-of-thought on artificial grammar, a different phenomenon. So the claim rests on one lab's secondary account.
- **C02.08-K17** (reworded: the sources support less). Romero 2023 (a position paper with no experiments, the three evidence lines are the same paper) says the tightly integrated design relies heavily on LLM outputs and is 'susceptible to cascading failures, including hallucinations and biases'; Chella 2018 is about knowledge-base limits, not LLMs. Only HtT gives measured support (incorrect rules are 65% and 81% of CoT errors). 'Inherits ... as cascading errors' is stated as established fact. Corrected claim: A tightly integrated LLM-plus-cognitive-architecture design is, according to the Romero et al. 2023 position paper, susceptible to cascading failures from LLM hallucinations and biases (no experiments reported); in rule-induction work, wrong induced rules account for 65% and 81% of chain-of-thought errors (HtT, Zhu 2024).
- **C02.08-K18** (reworded: the sources support less). Table 1 shows GPT-4 as its own verifier lowers accuracy in Game of 24 (5 to 3), graph colouring (16 to 2) and mystery blocksworld (4 to 0), but raises it in Blocksworld (40 to 55), which the paper calls a modest improvement; so 'lowers accuracy' is not universal. Numbers 5/3/36-38 are right. Corrected claim: An LLM used as its own verifier usually lowers accuracy (GPT-4: Game of 24 5% to 3%, graph colouring 16% to 2%, mystery Blocksworld 4% to 0%), though in Blocksworld it rose modestly (40% to 55%); a sound external verifier (solver, tests, tool) gives much larger gains (Game of 24 36-38%, Blocksworld 60-87%).
