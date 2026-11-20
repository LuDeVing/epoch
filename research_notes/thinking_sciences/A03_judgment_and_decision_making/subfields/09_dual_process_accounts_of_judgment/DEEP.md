# Dual-process accounts of judgment: deep document

*Subfield A03.09. Scope: System 1 and System 2 (Kahneman 2011) and the wider family of dual-process theories of judgment and reasoning, plus every LLM study that tests or uses the idea. Evidence ids (a01 to d16) refer to evidence_a-d.jsonl in this folder; claim ids (K01 to K22) refer to claims.jsonl. Overlaps with Debiasing, Heuristics and biases, Prospect theory, Naturalistic decision making, Verbal confidence and Dual-process and three-process accounts (insight) are only linked, not covered.*

**Reading note on evidence quality.** The human founding studies (a01 to a13) were recalled from memory and are not verified; this is stated again wherever such a number appears. The 2011 to 2025 human items and all LLM items were opened. Several papers appear in many evidence lines (Hagendorff 2023 in a19, a20, b12 to b14, c01 to c03, c25; Liu 2025 in a23, b21 to b23, c10, c11; Chen in a24, b18, c17; Yu in a26, b19, c14; Weston in a25, b20, c13; Dualformer in a28, b25, c15). Count papers, not lines.

## 1. What it is

Dual-process accounts say that judgment and reasoning come from two kinds of process. One kind is fast, automatic, associative and effortless. The other is slow, deliberate, rule-based and effortful. Kahneman (2011) made the popular form: "System 1" and "System 2". System 1 produces impressions and intuitions. System 2 is lazy, monitors System 1 and often just endorses its output (a07, a09). Errors in the heuristics-and-biases tradition (Linda, base-rate neglect, the bat and ball) are explained as System 1 output that System 2 failed to correct.

Three things need to be kept apart.

1. **The theory of human cognition.** Is there a real split into two kinds of process, and does speed or effort mark the split? This is contested. Evans and Stanovich (2013) say speed, bias and consciousness are only correlates; the defining features are that Type 1 is autonomous and needs no working memory, while Type 2 needs working memory and supports hypothetical thinking (a10). Critics say the dichotomy is not coherent or not falsifiable (a10 limits; b05, b08). Kahneman himself calls the two systems "fictions" of convenience (a09).
2. **The design heuristic.** "Answer fast when the problem is easy, slow down when it is hard." This is useful as a compute-allocation rule whatever the theory says (b26, K14, K20).
3. **The LLM label.** Many LLM papers call chain-of-thought (CoT) or long reasoning "System 2" and direct answers "System 1". This is a naming choice. It is not an independent test of the human theory (critique.md, weak spots). Sprague and Liu show the label does not predict when slow reasoning helps (b16, c12, a23).

Why it matters for our agent: the schema already has a gate (S0) that picks direct, short, step-by-step or checked modes, and guardrails G1, G11 and G12 that say think briefly, doubt only on a signal and spend by difficulty. This subfield asks what evidence supports those choices, what a fast/slow router really buys, and which "System 2" additions (verify, reflect, slow down) are known to fail.

Main result in one paragraph: the human evidence for a speed or load manipulation switching between two processes is weak (a registered replication null, a meta-analysis near zero). The best-supported practical lessons are about task type, not about speed. Slow reasoning in LLMs helps mainly on math, symbolic and logic tasks, can hurt on pattern, perception and exception tasks, and wastes tokens on easy items. Same-model self-verification does not reliably fix answers. Routing saves tokens but nobody has shown it wins at equal total tokens.

## 2. History and theories in depth

### 2.1 Origins (human, from memory unless noted)

- **Wason and Evans (1975), "Dual processes in reasoning?"** (a02, unverified). On the selection task, people pick the matching cards (P and Q), and the reasons they state afterwards rationalise a choice made on other grounds. This is the first use of the dual-process idea in reasoning. Samples were tiny and the rationalisation reading was later contested.
- **Evans, Barston and Pollard (1983)** (a01, unverified numbers). Belief bias in syllogisms. Approximate acceptance rates recalled from memory: valid and believable 89%, invalid and believable 71%, valid and unbelievable 56%, invalid and unbelievable 10%. Logic matters more when the conclusion is unbelievable (an interaction). Dube, Rotello and Heit (2010) argue the interaction is a response-bias artefact, not a process difference.
- **Epstein (1994), CEST** (a04). Experiential system (fast, affective) versus rational system. Source of the Rational-Experiential Inventory.
- **Sloman (1996)** (a03). Associative versus rule-based system. Main argument is Criterion S: you can hold two contradictory beliefs at once (Linda: the representativeness pull stays while you know the conjunction rule). Weak, because one system with conflicting cues could do the same.
- **Evans and Over (1996)** (a05). Heuristic-analytic framework; implicit versus explicit processes; rationality1 (reaching goals) versus rationality2 (following rules).
- **Stanovich and West (2000)** (a06). Coined "System 1" and "System 2". Across tasks, cognitive ability correlates with normative answers (about r = .25 to .40, recalled from memory), and thinking dispositions add independent variance. Some tasks show none or a reversal.
- **Kahneman and Frederick (2002)** (a07). Attribute substitution: when the target attribute is hard, System 1 answers an easier related question; System 2 monitors lazily. Linda conjunction error about 85% in the 1983 direct test (memory). Substitution is a description, not a measured process.
- **Frederick (2005), Cognitive Reflection Test** (a08). Three items, each with a fast wrong answer (10 cents, 100 minutes, 24 days). N = 3,428 across sites, 41% correct overall (verified second-hand through Hagendorff, c25). Per-site means (MIT about 2.18 of 3, Toledo about 0.57) are memory only.
- **Kahneman (2011)** (a09). Popular synthesis. Several priming and ego-depletion results it cites failed to replicate (ego depletion multi-lab: d about 0.04, memory, unverified).

### 2.2 Architectures

- **Default-interventionist (DI).** Type 1 produces a default answer; Type 2 may or may not intervene. Kahneman's account and Evans and Over's heuristic-analytic framework are DI (a05, a10). Prediction: correct logic takes extra time and effort.
- **Parallel-competitive.** Both types run at once and compete (Sloman; a18 notes the two groups). Prediction: logic can be fast and can conflict with heuristics from the start.
- **Three-stage model, Pennycook, Fugelsang and Koehler (2015)** (a12). Adds a conflict-detection stage: the intuition is checked for conflict; if conflict is detected the person either rationalises the first answer or decouples and replaces it. Rationalisation is common. Detection and rationalisation are hard to separate by behaviour alone.
- **Two-response paradigm with feeling of rightness (Thompson, Prowse Turner and Pennycook 2011)** (a11). First answer fast, then a rating, then a free second answer. A low feeling of rightness predicts more rethinking and more answer change. The rating may track fluency, not correctness.
- **Logical intuition, De Neys and Bago.** Intuitive responders already carry some logical sensitivity: conflict is detected even when the biased answer is given (a14), and in two-response data most final correct answers were already correct at the first stage (a13, about 90%, memory) and about 74% of moral response pairs were utilitarian-utilitarian (b06, second-hand). This weakens DI: the fast answer is not always the wrong one.
- **Default-disruptive view, Mega and Volz (2014)** (b09). Putting intuition into words can damage it (verbal overshadowing, reasons analysis). Cited: Schooler and Engstler-Schooler 1990, Wilson and Schooler 1991. Editorial, not a test. It anticipated Liu et al. (2025) for LLMs (b21).
- **Applied models.** Croskerry (2013) applies DI to clinical diagnosis: most errors start in Type 1, so debias by detecting Type 1 output and sending it to Type 2 verification (a17). Djulbegovic et al. (2012) give a threshold model: decide by Type 1 when confident, escalate otherwise (a18). Thresholds are not empirically calibrated.
- **AI position papers.** Booch et al. (2021): build AI from a fast learned system, a slow deliberate one and a metacognitive controller (a29, c23). Goyal and Bengio (2022): System 2 is sequential, verbalisable, low-bandwidth through a global workspace, and relies on System 1 to sample candidates; skills migrate from explicit to implicit with practice (a30). Neither tests anything.

### 2.3 Criticism of the theory

- Unfalsifiable (Keren and Schul 2009); not coherent as a dichotomy (Melnikoff and Bargh 2018) (named in a10 limits, from memory).
- Speed does not identify the process type (b06).
- Rival single-process or response-bias accounts: parallel comparison (Gurcay and Baron), Dube et al. for belief bias (b08, a01).
- Evans and Stanovich (2013) reply: list five misconceptions and say Type 1 is not simply "biased" and Type 2 is not simply "correct" (a10).

## 3. Core findings with exact numbers

Status key: **established** = two or more independent opened sources agree; **single-source** = one paper; **contested** = sources disagree or rely on second-hand reports; **unverified** = recalled from memory.

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CRT human baseline | N = 3,428, 41% correct (original); 38% correct and 55% intuitive in a Prolific sample of 500 (45 excluded); difference p = .06 | a08, c25, c01 | established (via Hagendorff) |
| Conflict detection without correction | Base-rate, N = 247: conflict items correct about 20%, no-conflict about 95%, confidence about 10 points lower on conflict items (F(1,246) = 54), same drop for wrong answers. Conjunction, N = 147: correct about 24% vs about 96%, same 10-point drop. Drop absent in the youngest group | De Neys, Cromheeke and Osman 2011 (a14) | established |
| Conflict items are slow, bias items mixed | N = 158. CRT: alignment and heuristic variants faster, neutral slower than conflict originals. Base-rate items had medians above 30 s | Alos-Ferrer et al. 2016 (a16) | single-source |
| CRT measures calculation more than reflection | N = 1,413 US adults: reflection added no unique power over calculation and numeracy for framing and conjunction; replicated in study 2 | Sinayev and Peters 2015 (a15) | single-source (b10, b11 give related support) |
| CRT sex gap | 77 documents; numerical 112 effects, N = 66,109, d = 0.39, delta = 0.47 (CI 0.44 to 0.50); verbal N = 9,916, delta = 0.13; artifacts explain about 37% of numerical variance | Otero et al. 2024 (b10) | established (meta-analysis) |
| CRT predicts work outcomes | Job performance: 7 coefficients, N = 1,508, r = .28, rho = .36 (CI .26 to .46). Training: 15 coefficients, N = 3,705, rho = .37. Incremental over intelligence small | Otero et al. 2021 (b11) | established (meta-analysis) |
| Time pressure raises cooperation: not replicated | 3,596 students, 21 labs, 12 countries. Time pressure minus delay = -0.37 points (CI -2.60 to 1.86); original +8.6 (49.4% vs 40.8%). Heterogeneity I2 = 2.72%. Compliance 34.1% (pressure) vs 92.5% (delay); compliant-only gap 10.37 (original 15.31), likely selection | Bouwmeester et al. 2017 RRR (b01, b02) | established (failed replication) |
| Load, time and depletion on moral judgment | 44 articles, 68 studies, N = 14,003. g = 0.06 (CI 0.00 to 0.12, p = .057). Personal dilemmas g = 0.03. Egger p = .001; trim-and-fill (17 imputed) g = -0.02; PET-PEESE g = -0.11 (over-corrects). Student and European samples g = 0.15 | Rehren 2024 (b03, b04) | established (meta-analysis) |
| Moral dual-process is item and design dependent | Philosophers judged only 45% (impersonal) and 48% (personal) items real conflicts; dropping items with under 5% inappropriate answers removed the effect (McGuire 2009); deontological choice 34% hypothetical vs 16% real (Bostyn 2018); load effect at 1:5 kill ratio, none at 1:500; Tinghog 2016 (>1,400) null; Gawronski and Beer reanalysis opposite sign | Review (b05, b07, b08) | contested (one secondary review) |
| Fast answers are often already right | About 74% utilitarian-utilitarian pairs, about 11% deontological then utilitarian, about 10% deontological-deontological (moral, second-hand); about 90% of final correct answers already correct at stage one (memory) | b06, a13 | contested / unverified |
| Belief bias | Valid-believable 89%, invalid-believable 71%, valid-unbelievable 56%, invalid-unbelievable 10% (memory) | Evans et al. 1983 (a01) | unverified |
| Ego depletion | d about 0.04 in a 23-lab replication, N about 2,100 (memory) | Hagger et al. 2016 (a09 note) | unverified |

### 3.2 LLM findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CRT trap rates fell with model generation | Trap (intuitive wrong) answers: davinci-003 80%, ChatGPT-3.5 15%, ChatGPT-4 0%, humans 55%. Correct: 5%, 59%, 96%, humans 38%. 150 tasks (50 per type) | Hagendorff et al. 2023 (a19, b12, c01) | single-source |
| CoT as a System 2 switch, weak models | davinci-003 with algebra prompt: CoT 0% to 100%, correct 5% to 28%, intuitive 80% to 29% | a20, c02 | single-source |
| Blocking CoT in strong models costs little | ChatGPT-3.5: CoT 97% to 0%, correct change -4% (p = .49). ChatGPT-4: CoT 84% to 0%, correct 95% to 88% (p < .05), intuitive 0% to 10%. ChatGPT-4 solved 24% of CRT without CoT in study 1 | a20, b13, c02 | single-source |
| Few-shot teaches the intuition | davinci-003: 2% to 92% after 2 examples (type 2); 12% to 92% after 7; 0% to about 78% after 30 on hardest type. Semantic illusions: 72% fell for it; careful-thinking prompt 18% to 54% correct; ChatGPT-3.5 74%, ChatGPT-4 88% correct | a20, b14, c03 | single-source |
| CoT helps mainly math, symbolic, logic | Mean gain symbolic +14.2, math +12.3, logical +6.9 points. Other categories 56.8 with CoT vs 56.1 without. Top three categories 56.9 vs 45.5. Up to 95% of MMLU CoT gain on questions with an equals sign. Over 100 papers plus 20 datasets by 14 models | Sprague et al. 2024 (b16, c12) | established (meta-analysis plus own tests) |
| CoT hurts where deliberation hurts humans | Implicit statistical learning: GPT-4o 87.5 to 64.4 (-23.1, p < .0001); Claude 3 Opus 70.7 to 62.7; Gemini 1.5 Pro -6.05; Claude 3.5 Sonnet +1.8 (n.s.). Face recognition: GPT-4o 64.0 to 51.2 (-12.8; -20% relative); Claude 3 Opus 44.0 to 29.6; Claude 3.5 Sonnet 97.8 to 94.8. Exceptions: GPT-4o 2.9 passes direct vs 12.5 with CoT (+331%); Claude 3.5 Sonnet 2.3 vs 6.4 (+178%). Three of six tasks showed harm; others mixed or neutral | Liu et al. 2025 (a23, b21, b22, c10, c11) | single-source (one paper) |
| Note on the 36.3 figure | o1-preview 57.7% vs GPT-4o 94.0% on a subset is a cross-model comparison, not a controlled CoT effect. The matched same-model drop is -23.1 | critique.md | correction recorded |
| Longer reasoning lowers accuracy | Claude Opus 4 from near 100% to about 85-90% as reasoning lengthens; DeepSeek R1 70% to 30% with five distractors; o3 more stable | Gema et al. 2025 (b24) | single-source |
| Overthinking on trivial items | o1-like models used 1,953% more tokens on "2+3"; first solution round correct in over 92% of cases; self-training fix cut tokens 48.6% on MATH500 at kept accuracy | Chen et al. (a24, b18, c17) | single-source |
| Reasoning models rarely need thought on easy items | 28 reasoning models: outputs 13.8x longer than small LLMs; a 1.7B model without thinking over 98% on easy set; steering speed +1.3% accuracy at -8.6% tokens; 80.52% of GSM8K samples solved more efficiently in normal mode | S1-Bench (c18), Lin 2025 (c21), DynamicMind (c22) | single-source each |
| System 2 Attention (rewrite context) | LLaMA-2-70B-chat: 62.8 to 80.3 (oracle 82.0); GSM-IC 51.7 to 61.3; long-form objectivity +57.4%; single-pass variants 71.7 | Weston and Sukhbaatar 2023 (a25, b20, c13) | single-source |
| Single instruction versus S2A | One line "ignore irrelevant information" matched distractor-example prompting on GSM-IC (code-davinci-002); clean GSM8K unharmed (59.3 vs 60.3). Self-consistency (20 samples) +11 points overall; correct answer in the 20 samples 99.7% (CoT), but best macro accuracy 45% | Shi et al. 2023 (d07, d14) | single-source |
| Distillation of slow into fast | Last letter 30.0 to 98.0 (25.5 vs 106.6 tokens); coin flip 56.1 to 75.69 (1-step RaR 77.2); S2A bias 51.6 to 81.3; GSM8K CoT 52.77 vs 7.13, not distillable | Yu et al. 2024 (a26, b19, c14) | single-source |
| Fast/slow agents | SwiftSage 84.7 vs SayCan 33.8, ReAct 36.4, Reflexion 45.3 on 30 ScienceWorld types; 757.07 tokens per action vs 1,855.84 / 1,971.03 / 2,983.46. Dualformer: slow 97.6% vs 93.3%, 45.5% fewer steps; fast 80% vs 30%; auto 96.6%, 59.9% fewer steps | Lin 2023 (a27, c16); Su 2025 (a28, b25, c15) | established as system wins; not matched ablations |
| Routing keeps accuracy at lower cost | ThinkSwitcher 14B: 66.9 at 5,603 tokens vs BERT router 65.0 at 5,983; 20-30% fewer tokens for 1-2 points; SynapseRoute 0.8390 vs thinking 0.8272 vs non-thinking 0.5774, tokens -39.66%, about 58% of medical questions need no thinking; Adaptive Dual Reasoner length -49.5 to -59.3%, up to +6.1% (abstract only) | d09, d10, d11 | single-source each; none at equal total tokens |
| Interpolating S1 and S2 alignment | Monotonic accuracy change; entropy-based dynamic combination beat base on 11 to 12 of 13 benchmarks (w = 0.4) | Ziabari et al. 2025 (c20) | single-source |
| Self-correction without feedback | GPT-4 GSM8K 95.5 to 91.5 to 89.0; CommonSenseQA 82.0 to 79.5 to 80.0; HotpotQA 49.0 to 49.0 to 43.0; GPT-3.5 CommonSenseQA 75.8 to 38.1. Game of 24: 5 to 3 with LLM verifier, 38 with sound verifier; Graph Coloring 16 to 2 vs 38 to 44 | Huang et al. 2024 (d01, d02); Stechly et al. 2024 (d03, d15); Kamoi et al. 2024 (d04) | established |
| Verbalised confidence is a weak trigger | GPT-4 average AUROC 62.7% (GSM8K 54.8%); 5-sample consistency GSM8K 92.7%. RLHF models: verbalised confidence beats logits, ECE cut by over 50% relative (trivia tasks) | Xiong 2024 (d05, d13); Tian 2023 (d06) | contested |
| Token budget in the prompt | TALE: 67% token cut with under 3% accuracy loss; 50-token budget gave 157 tokens | Han et al. 2025 (d12) | single-source |
| Bias battery on LLMs | Correct with correct reasoning: GPT-4 69.2%, Claude 2 55.0%, Bard 35.8%, GPT-3.5 29.2%, Llama 2 70b 15.0%, 13b 5.0%, 7b 2.5%; human-like bias GPT-3.5 21.7%, GPT-4 4.2%; 12 tasks, 10 runs each | Macmillan-Scott and Musolesi 2024 (c08) | single-source |
| Debias prompts | GPT-4 framing gap: baseline -0.405, awareness -0.470 (worse), counterfactual -0.570, self-help -0.010. 13,465 prompts | Echterhoff et al. 2024 (c09) | contested (table text garbled) |
| Anchoring in LLMs | GPT-3.5 anchoring t(58) = 8.78 vs humans t(58) = 5.55 | Suri et al. 2023 (c07) | single-source |
| Perturbation breaks LLM answers | One changed number in CRT-like maths: 86.8% average to 68.5% (-18.3); three numbers 53.1%; algebraic letters 20.9%, GPT-4 best 29.3%; human accuracy did not drop significantly. GPT-3 still answered $0.10 with a nonsense premise | Ma et al. 2025 (c19); Binz and Schulz (b15, c04, d08) | established (3 sources) |
| GPT-3 on classic tasks | Reproduces Linda, framing, certainty effect; avoids cab-problem base-rate neglect; fails causal tasks; horizon regret lower than humans (t(5550) = -4.07) | Binz and Schulz 2023 (a21, c05) | single-source |

## 4. Mechanisms and models

Each model below is stated so it can be coded. None is a claim that the mechanism is the true human process.

### 4.1 Default-interventionist loop (human model, adapted to an agent)

```
answer = fast_pass(task)                   # Type 1 default
conflict = detect_conflict(task, answer)   # cue clash, low confidence, disagreement
if conflict:
    answer = slow_pass(task, answer)       # may decouple or just rationalise
return answer
```

Evidence on each step:
- Fast pass is often right already (a13 about 90%, unverified; b06 for moral items; Chen over 92% first round correct, a24).
- Detection: humans lower confidence about 10 points on conflict items even when wrong (a14). No LLM replication found (K19, d05, d06).
- Slow pass: in humans it often rationalises (a12). In LLMs same-model review flips right answers to wrong at least as often as the reverse without outside feedback (d01, d03).

Implementation lesson: the conflict detector must come from something the model does not control: a code check, sample disagreement, or a task-class rule. Stated confidence is a weak detector (62.7% AUROC, d05).

### 4.2 Three-stage model as a pipeline

1. Fast pass produces answer A1 and records metadata (stated confidence, length, a code check result).
2. Detection stage: triggers if any of: check fails, 2 to 5 short samples disagree, task class is flagged slow-eligible. Else stop.
3. If triggered: the slow pass is shown the actual failing output (G2), not asked to "reflect".
4. Outcome logged: A1 correct to A2 wrong (harm), A1 wrong to A2 correct (fix). The harm and fix rates per class decide whether the trigger is kept. This is the missing data in K11 and K18.

### 4.3 Threshold model (Djulbegovic et al.)

Decide with the fast path if the probability of being right exceeds a threshold t; escalate otherwise. In code: t comes from a held-out calibration set per task class (S0 stores the plain pass rate). A fixed threshold from theory is not available (a18 limits).

### 4.4 Routers in the LLM literature

- **ThinkSwitcher** (d09): a small trained head picks short or long CoT per question; thresholds trade 1 to 2 points for 20 to 30% fewer tokens. A BERT router on the 1.5B model saved more tokens but lost more accuracy.
- **SynapseRoute** (d10): learned router between thinking and non-thinking mode; 39.66% fewer tokens, +1.2 points.
- **Adaptive Dual Reasoner** (d11): switches inside one chain after SFT plus RL (abstract only read).
- **Dualformer** (a28): one transformer, traces randomly dropped in training, three inference modes; auto mode picks slow more as mazes grow.
- **SwiftSage** (a27): small fine-tuned T5 acts; GPT-4 takes over when a hand-written heuristic detects trouble.
- **DynamicMind** (c22): three modes (fast, normal, slow) via a Mind Router; 80.52% of GSM8K samples best in normal mode; router transfer to another base lost about 2.78 points.
- **Controlling thinking speed** (c21): steering vector on activations plus real-time difficulty estimation; +1.3% accuracy at -8.6% tokens; needs activation access.
- **Entropy-based combination** (c20): mix the outputs of S1-aligned and S2-aligned models by token entropy.

What transfers to a scaffold with no training: the routing decision (feature, threshold, cost report) and the mis-route cost report. What does not: weights, steering, trained routers.

### 4.5 System 2 Attention (S2A) as an operator

Step 1: ask the model to rewrite the context keeping only what is relevant and non-opinionated. Step 2: answer from the rewrite only. Gain 62.8 to 80.3 (oracle 82.0) on LLaMA-2-70B-chat (a25). Rival: a single-pass instruction "ignore irrelevant information" (d07). In the schema this is the S1 input-hygiene step, where code (not the model) can move suggestive material to a marked block.

### 4.6 Self-consistency as a trigger

Five samples with agreement: AUROC 92.7% on GSM8K (d13) against 54.8% for stated confidence. Cost is 5 times the tokens. As a trigger for slow mode, it works only if the cost is charged to the budget (G7). Even then G4 applies: agreement among samples of one model is a hint, not proof.

### 4.7 Token budget as time pressure

TALE (d12): a prompted budget is overshot (50 requested, 157 used) and a per-question estimated budget cut tokens 67% at under 3% accuracy loss. A hard max-token cap is the closer analogue to human time pressure; it is untested against the human null.

## 5. What holds up

### 5.1 Human side

Holds up:
- Conflict detection under biased answers (a14, N = 247 and 147).
- The CRT as a measure that mixes calculation, numeracy and reflection (a15, b10, b11).
- The existence of belief bias and matching bias as phenomena (memory only; the explanation is disputed).

Failed or weak:
- Time pressure or forced delay as a switch between intuitive and deliberate behaviour (b01: -0.37 points, N = 3,596). The original positive result was likely selection bias from uneven compliance (34.1% vs 92.5%).
- Load, depletion and time restriction on moral judgment: g = 0.06; after publication-bias correction -0.02 (b03, b04).
- Ego depletion (d about 0.04, memory).
- The assumption that fast means intuitive and wrong (b06, a13).

Moderators found: student and European samples gave larger moral effects (g = 0.15); kill ratio mattered (1:5 vs 1:500); real versus hypothetical choice shifts the base rate (34% vs 16%, b07); item selection can erase the effect (McGuire 2009).

Interventions: "slow down" instructions and bias checklists did not reliably help in controlled studies (see Debiasing subfield, SCHEMA 4b).

### 5.2 LLM side

Holds up (two or more sources):
- Explicit reasoning helps on math, symbolic and logic tasks and about nothing elsewhere (b16, c12; consistent with Kojima's large old-model gain MultiArith 17.7 to 78.7, a22, which reflects older models).
- Answers on classic bias items are brittle to wording and numbers (b15, c04, c19, a21, d08).
- Extra reasoning past the first correct answer wastes tokens and can lower accuracy (a24, b24, c18).
- Same-model self-verification does not reliably help; outside signals do (d01 to d04, d15).

Single-source, treat with care:
- CoT harm on implicit learning, faces and exceptions (Liu et al.). Model-specific: Claude 3.5 Sonnet had no significant drop.
- Routing at lower cost (three papers, none at equal total tokens).
- S2A and distillation (older models, training needed).

Failures and boundary conditions:
- CoT could not be distilled into a fast pass on GSM8K (52.77 vs 7.13, a26).
- Prompted debiasing: the awareness prompt worsened the GPT-4 framing gap (-0.405 to -0.470); the counterfactual prompt gave -0.570 (c09). Table text was garbled, so the reading is approximate.
- Verbalised confidence: average calibration after RLHF is fine, but separation of right from wrong is poor (d05, d06).
- Prompted token budgets overshoot (d12).
- Router transfer to a new base model lost about 2.78 points (c22).

Moderators: model generation (CoT gain large on 2022 models, near zero on frontier models outside math), task class, presence of distractors, whether an exact verifier exists, whether reasoning can be switched off (o1 could not, c10).

## 6. Language models

### 6.1 Do LLMs show System 1 errors?

Early yes, later no. GPT-3 (davinci) answered all three original CRT items intuitively wrong (b15, c04); across 150 bespoke tasks davinci-003 was 80% intuitive and 5% correct against humans at 55% and 38% (c01). ChatGPT-3.5 was 59% correct, 15% intuitive; ChatGPT-4 was 96% correct, 0% intuitive (c01). The authors call this "hyperrational". Contamination is likely, and Ma et al. (c19) show that one changed number cut a CRT-like set from 86.8% to 68.5% and algebraic letters left 20.9%, while humans did not drop significantly. So high CRT scores of frontier models do not show reflection. K08 and K22 say the original CRT is a weak test.

LLMs also show some classic effects (anchoring t(58) = 8.78 vs human 5.55 for GPT-3.5, c07; framing and certainty effects for GPT-3, c05), but wrong answers are mostly not the human-like bias: GPT-4 had 4.2% human-like bias and 69.2% correct with correct reasoning; Llama 2 7b only 2.5% correct (c08). Binz and Schulz also found GPT-3 avoids the cab base-rate error and fails a causal task (a21).

### 6.2 What does "System 2" do for LLMs?

- Gains concentrate where there are symbolic steps to execute: +14.2 symbolic, +12.3 math, +6.9 logic; +0.7 elsewhere (56.8 vs 56.1); a symbolic solver beats CoT on the symbolic steps (b16, b17, c12).
- Blocking CoT in strong models cost little on the CRT (95 to 88, a20).
- Harm: implicit learning -23.1 (GPT-4o), face recognition -12.8 (GPT-4o) and -14.4 (Claude 3 Opus), exceptions +331% passes needed (a23, b21, b22). Task- and model-dependent; Claude 3.5 Sonnet showed none significant; o1 reasoning cannot be turned off.
- Longer thinking: Claude Opus 4 about 85-90% from near 100%; R1 70% to 30% with five distractors (b24).
- Overthinking: 1,953% more tokens on 2+3 (a24); S1-Bench 13.8x output length; a 1.7B model without thinking over 98% on easy items (c18).

### 6.3 Fast/slow systems and routers

See 3.2 and 4.4. System-level wins (SwiftSage 84.7 vs 36.4 ReAct at 757 vs 1,971 tokens per action; Dualformer) show that mixing a cheap path and an expensive path saves tokens on bespoke tasks. They are not matched ablations of dual-process theory (K14). Routing papers report 20 to 60% token savings at about equal accuracy (K20), but none fixes the total tokens across arms. Mis-routing cost is visible only indirectly (BERT router loses accuracy, d09; transfer loses 2.78 points, c22).

### 6.4 Verification and confidence

- Same-model verify lowers accuracy (GPT-4 GSM8K 95.5 to 89.0 after two rounds; Game of 24 5 to 3; Graph Coloring 16 to 2) and a sound verifier gives 38 to 44 (d01, d03). Survey: no demonstrated prompted self-correction except on suited tasks (d04). This is 2023-24 evidence; RL-trained reasoning models are untested here.
- Verbalised confidence: AUROC 62.7% average; sample agreement 92.7% on GSM8K at 5 times the cost (d05, d13).
- Recall versus selection: in 20 samples the right answer was present 99.7% of the time, yet the best method scored 45% macro (d14). Selection, not generation, is the weak step. This supports G5 (code selects) and S4 harvesting.

### 6.5 Debiasing prompts

Plain debiasing prompts are inconsistent (c09). A one-line "ignore irrelevant information" works about as well as showing examples on old models (d07), and S2A beats single-pass variants on LLaMA-2-70B (80.3 vs 71.7, a25). Whether S2A beats a one-line instruction on frontier models at equal tokens is unknown (K06).

### 6.6 Distillation

Training a model on its own slow-method outputs moves accuracy into a fast pass for rewrite-style methods (98.0% vs 30.0% last-letter; 81.3 vs 51.6 bias) but not for CoT math (a26). Our agent does not train. The analogue is caching verified templates in memory.

## 7. What our agent should take

Legend: schema part G (guardrail), S (state), O (operator), memory. Status [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | Gate by task class, not by a fast/slow label. Use CoT or step-by-step mainly on calculation, symbolic and logic items; plain or short answers elsewhere. Check by held-out calibration, not by assumption | S0 (mode choice), G11, G12 | [E] | b16, c12, K01 |
| A2 | Cap reasoning per mode; stop after the first verified answer. Extra thinking past it wastes tokens and can lower accuracy | G11 | [E] | a24, b18, c17, b24, c18, K03 |
| A3 | Do not use same-model "review your answer" as verification. Any verify step must use an independent signal: tool, test, held-out example, mutated input | G2, G3, S8 | [E] | d01 to d04, d15, K18 |
| A4 | Do not rely on stated confidence as the stop or escalate signal; prefer code checks and sample disagreement, charged to the budget | G1, G11, 4b | [E] for "stated confidence is weak"; trigger comparison is [C] | d05, d13, K19 |
| A5 | Robustness probe: re-ask under paraphrase and one number changed; send answers that flip to a slower check | G3, S4/S8 | [E] that answers are brittle; the probe itself is untested | b15, c04, c19, a21, d08, K09 |
| A6 | Evaluation hygiene: do not use the original CRT or famous bias vignettes as evidence of reasoning for frontier models; use fresh or perturbed items | evaluation design | [E] for the contamination and brittleness concern | c01, c19, d08, K08, K22 |
| A7 | Do not design rules from time-pressure or load theory; judge design choices by accuracy at equal tokens | G7 | [E] | b01 to b05, K10 |
| A8 | Record per class the first answer and what later steps change (first-answer correctness, flips) | S9 log, memory | [E] as a logging step; the harm rate itself is unmeasured | a24, a13, K11 |

These match what SCHEMA already says in G1, G2, G3, G7, G10, G11, G12 and 4b. This subfield adds supporting evidence for A1 and A6 and the "no stated confidence" line.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Direct-answer path for implicit-pattern, perception and exception-heavy tasks; CoT only when it does not lose to direct on a calibration set | S0, S1 direct path, G11 | [S] | a23, b21, b22, c10, c11, K02 |
| T2 | Routed fast/slow versus always-fast and always-slow at equal total tokens, with a mis-route cost report | S0 router | [S] | d09, d10, d11, a27, a28, K14, K20 |
| T3 | Cheap trigger for going slow: compare stated confidence, 3 to 5 sample disagreement, task-class rule; metric AUROC for "slow beats fast" | S6 trigger, G1 | [C] | d05, d13, a14, K19, K12 |
| T4 | Clean-restate step (S2A style) versus a one-line single-pass instruction at equal tokens | S1 input hygiene | [S] | a25, d07, K06 |
| T5 | Verify-flip rate: how often a verify pass turns right into wrong, with and without a tool check, on modern reasoning models | S8 | [C] for modern models | d01, d03, a13, K11, K18 |
| T6 | Hard token cap versus prompted budget (human time-pressure analogue) | G11 | [S] | d12, b01, K21 |
| T7 | Difficulty probe for easy items (short mode) with mis-route cost | S0 | [S] | c18, c21, c22, K04 |
| T8 | Cache verified rewrite or decomposition routines in memory (analogue of distillation) | memory | [S] | a26, b19, c14, K05 |
| T9 | Confidence drop on conflict twin items as an LLM conflict detector | S6 trigger | [C] | a14, d05, d06, K12 |
| T10 | Debias prompt family (awareness, counterfactual, self-help) with a no-prompt baseline | G | [C]; schema 4b currently says not to add | c09, K07 |

### Do not add

- The label "System 1 / System 2" as a mechanism (no gain beyond task type, K01).
- A fixed "slow down and be careful" instruction (already in 4b; a20 shows little effect when direct answers are already good).
- Moral dual-process rules (K16).
- Trained routers, steering vectors, distillation and Dualformer-style training: out of scope for a scaffold (section 9).

## 8. Concrete tests on our bench

All arms at equal total tokens (setup, routing and any verify tokens counted, G7). Report mean and spread over at least 10 draws per item (c08 used 10 runs). Use fresh items (A6).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (K01, T1) | Mixed battery: calculation, symbolic, logic items; knowledge items; implicit pattern (artificial-grammar style), perceptual match, exception-heavy classification | Direct vs forced CoT vs routed by task class | Accuracy by class; paired difference | CoT gain about +12 to +14 on calculation or symbolic, near 0 on knowledge, negative on implicit pattern and exception classes. Claim fails if CoT loses on none |
| B2 (T2) | Same mixed set as B1 | Always-fast, always-slow, routed by task-class rule, routed by learned difficulty probe, total tokens fixed per item set | Accuracy at the fixed token total; mis-route rate; accuracy on routed-wrong items | Routed arm at least equal to the best fixed arm; mis-route cost reported in points |
| B3 (T3) | 300 items with known slow-vs-fast outcome from B1 | Triggers: stated confidence, 5-sample disagreement, task-class rule | AUROC for predicting that slow beats fast; tokens charged | Verbalised about 0.55 to 0.63 (d05); sample agreement much higher but costs 5x; task rule cheapest |
| B4 (T4) | Opinion-laden prompts (user states a wrong guess) and arithmetic with irrelevant sentences | No intervention; single-pass "ignore irrelevant" instruction; two-step clean-restate | Accuracy; sycophancy rate | S2A-style gain 8 to 17 points on old models (62.8 to 80.3, 51.7 to 61.3); expect smaller on frontier; test whether two-step beats one line |
| B5 (T5) | Reasoning items with exact checks | First answer only; first answer plus same-model verify; first answer plus tool check | Wrong-to-correct and correct-to-wrong flip counts; net accuracy | Same-model verify net zero or negative (GPT-4 GSM8K -6.5 over two rounds, d01); tool check net positive |
| B6 (T6) | Mixed set | Hard max-token cap at 3 levels vs prompted budget at the same levels | Accuracy curve against actual tokens used | Prompted budgets overshoot (d12); cap gives sharper loss on calculation items, little on knowledge |
| B7 (A5, K09) | CRT-style and bias items, fresh, with perturbed twins (changed numbers, nonsense premise, reordered options) | Plain answer | Flip rate between twins; accuracy on twins | One changed number about -18 points on older models (c19); smaller on frontier; flips mark items for slower check |
| B8 (T9, K12) | Conflict and no-conflict twin items (base-rate and conjunction types) | Verbalised confidence, logit confidence | Confidence difference conflict minus no-conflict; correct vs incorrect | Human drop about 10 points (a14); if the LLM drop is absent the trigger fails |
| B9 (T10) | Framing and anchoring items | No prompt; awareness; counterfactual; self-help; 10 draws | Framing gap, anchoring slope | Prompts inconsistent (c09); keep none unless the gap shrinks with a CI excluding 0 |
| B10 (T7) | Easy and hard items (S1-Bench-like easy set plus hard set) | Short mode for all; long for all; routed by difficulty probe | Accuracy and tokens | Easy items near 98% without thinking (c18); long mode costs about 10x tokens |
| B11 (K03) | Items with 0, 2, 5 distractors | CoT length buckets; cap at k | Accuracy against length | Inverse scaling visible on distractor-heavy items (b24) |

## 9. What does not transfer, and why

- **Human time-pressure and load results.** Null or near zero (b01, b03). They tell us nothing about how to allocate tokens. A token budget is not a clock; the closest analogue is a hard cap, and the human null has not been compared with it (K21).
- **Moral dual-process findings.** One secondary source, item problems, hypothetical vs real choice differences (b05, b07). No mechanism for our agent.
- **CRT results on frontier models.** Contaminated and brittle (c19, d08). High scores do not equal reflection.
- **"Fast = wrong, slow = right."** False for humans in two-response data (a13, b06; unverified or second-hand) and false for LLMs on easy items (c18, a24).
- **Feeling of rightness and conflict-detection confidence.** Human findings (a11, a14); no LLM test, and stated confidence is a poor failure detector (d05).
- **Trained systems** (Dualformer a28, SwiftSage T5 a27, DynamicMind router c22, ThinkSwitcher d09, steering c21, distillation a26). They need training, labelled data or activation access. The scaffold can copy the routing logic and its cost report only.
- **Old-model numbers** (Kojima 2022 a22, GPT-3 studies, Llama-2 S2A). Gaps shrink on newer models (Sprague, c12). Do not carry the magnitudes.
- **Cost shape of SwiftSage and Dualformer.** Bespoke tasks and trained components; the lesson is the architecture, not the numbers.
- **Human debiasing training.** Not tested here; see the Debiasing subfield.

## 10. Open questions

1. At equal total tokens, does a routed scheme beat always-fast and always-slow, and what does mis-routing cost? (gap 1, K20; no study)
2. Which cheap signal predicts that slow reasoning will hurt: model confidence, task class, direct-vs-CoT disagreement? (gap 2, K19; partly closed)
3. Do modern RL-trained reasoning models flip right answers to wrong during verification, and how often does verification fix wrong first answers? Is the human "90% already correct" figure real? (gap 3, K11, K18)
4. Is the De Neys confidence drop on conflict items reproduced in LLMs and is it usable as a trigger? (gap 4, open)
5. Does a single-pass instruction match S2A at equal tokens on frontier models? (gap 5, K06)
6. How do perturbed CRT and bias items score on current models? (gap 6, K22)
7. Founding human numbers (Evans 1983, Frederick 2005 per-site, Hagger 2016, Bago and De Neys 2017) are unverified. (gap 7, K17)
8. Does a hard token cap behave like human time pressure, and does it show the same near-null effect? (gap 8, K21)
9. Which architecture (default-interventionist, parallel-competitive, three-stage) predicts LLM error patterns on the same items as humans? (gap 9, open)
10. Does a reasoning model's early difficulty awareness (c18: lower confidence early on) give a usable difficulty probe?
11. Why did Claude 3.5 Sonnet resist CoT harm while GPT-4o and Claude 3 Opus did not (b21, b22)? Training or scale?

## 11. Sources

[V] = opened this session (full text or PDF text), [M] = snippet or memory only. Notes in brackets say where the critique did not re-open a source.

**Human, founding (all [M])**
- [M] Wason and Evans (1975), Dual processes in reasoning? https://doi.org/10.1016/0010-0277(75)90001-9
- [M] Evans, Barston and Pollard (1983) https://doi.org/10.3758/BF03196976
- [M] Epstein (1994) https://doi.org/10.1037/0003-066X.49.8.709
- [M] Sloman (1996) https://doi.org/10.1037/0033-2909.119.1.3
- [M] Evans and Over (1996) https://doi.org/10.4324/9780203027707
- [M] Stanovich and West (2000) https://doi.org/10.1017/S0140525X00003435
- [M] Kahneman and Frederick (2002) https://doi.org/10.1017/CBO9780511808098.004
- [M] Frederick (2005) https://doi.org/10.1257/089533005775196732 (download failed, d16)
- [M] Kahneman (2011) Thinking, Fast and Slow https://us.macmillan.com/books/9780374533557/thinkingfastandslow/
- [M] Evans and Stanovich (2013) https://doi.org/10.1177/1745691612460685
- [M] Thompson, Prowse Turner and Pennycook (2011) https://doi.org/10.1016/j.cogpsych.2011.06.001
- [M] Pennycook, Fugelsang and Koehler (2015) https://doi.org/10.3758/s13423-015-0814-3
- [M] Bago and De Neys (2017) https://doi.org/10.1016/j.cognition.2016.12.006

**Human, opened**
- [V] De Neys, Cromheeke and Osman (2011) https://pmc.ncbi.nlm.nih.gov/articles/PMC3026795/
- [V] Sinayev and Peters (2015) https://pmc.ncbi.nlm.nih.gov/articles/PMC4423343/
- [V] Alos-Ferrer, Garagnani and Huegelschaefer (2016) https://pmc.ncbi.nlm.nih.gov/articles/PMC5031706/
- [V] Croskerry (2013) https://pmc.ncbi.nlm.nih.gov/articles/PMC3786658/
- [V] Djulbegovic et al. (2012) https://pmc.ncbi.nlm.nih.gov/articles/PMC3471048/
- [V] Bouwmeester et al. (2017) RRR https://pmc.ncbi.nlm.nih.gov/articles/PMC5453400/ (not re-opened in the critique)
- [V] Rehren (2024) meta-analysis https://pmc.ncbi.nlm.nih.gov/articles/PMC11097977/ (not re-opened)
- [V] Untested Assumptions and Tenuous Evidence (2025) https://pmc.ncbi.nlm.nih.gov/articles/PMC12838211/
- [V] Mega and Volz (2014) https://pmc.ncbi.nlm.nih.gov/articles/PMC4124263/
- [V] Otero et al. (2024) https://pmc.ncbi.nlm.nih.gov/articles/PMC11051326/ (not re-opened)
- [V] Otero et al. (2021) https://pmc.ncbi.nlm.nih.gov/articles/PMC8200478/ (not re-opened)

**LLM, opened**
- [V] Hagendorff, Fabi and Kosinski (2023) https://arxiv.org/abs/2212.05206
- [V] Binz and Schulz (2023) https://arxiv.org/abs/2206.14576
- [V] Kojima et al. (2022) https://arxiv.org/abs/2205.11916
- [V] Liu et al. (2025) Mind your step https://arxiv.org/abs/2410.21333
- [V] Chen et al. (2025) overthinking https://arxiv.org/abs/2412.21187
- [V] Weston and Sukhbaatar (2023) https://arxiv.org/abs/2311.11829
- [V] Yu et al. (2024) https://arxiv.org/abs/2407.06023
- [V] Lin et al. (2023) SwiftSage https://arxiv.org/abs/2305.17390
- [V] Su et al. (2025) Dualformer https://arxiv.org/abs/2410.09918
- [V] Booch et al. (2021) https://arxiv.org/abs/2010.06002 (abstract and intro only)
- [V] Goyal and Bengio (2022) https://arxiv.org/abs/2011.15091
- [V] Sprague et al. (2024) https://arxiv.org/abs/2409.12183
- [V] Gema et al. (2025) https://arxiv.org/abs/2507.14417
- [V] Jones and Steinhardt (2022) https://arxiv.org/abs/2202.12299 (abstract, intro and framework only)
- [V] Suri et al. (2023) https://arxiv.org/abs/2305.04400
- [V] Macmillan-Scott and Musolesi (2024) https://arxiv.org/abs/2402.09193
- [V] Echterhoff et al. (2024) https://arxiv.org/abs/2403.00811
- [V] Zhang et al. (2026) S1-Bench https://arxiv.org/abs/2504.10368 (not re-opened)
- [V] Ma et al. (2025) https://arxiv.org/abs/2410.14979
- [V] Ziabari et al. (2025) https://arxiv.org/abs/2502.12470 (not re-opened)
- [V] Lin et al. (2025) Controlling thinking speed https://arxiv.org/abs/2507.03704 (not re-opened)
- [V] Li et al. (2025) DynamicMind https://arxiv.org/abs/2506.05936 (not re-opened)
- [V] Xu et al. (2025) survey https://arxiv.org/abs/2502.17419 (abstract and intro only)
- [V] Huang et al. (2024) https://arxiv.org/abs/2310.01798
- [V] Stechly, Valmeekam and Kambhampati (2024) https://arxiv.org/abs/2402.08115
- [V] Kamoi et al. (2024) https://arxiv.org/abs/2406.01297
- [V] Xiong et al. (2024) https://arxiv.org/abs/2306.13063
- [V] Tian et al. (2023) https://arxiv.org/abs/2305.14975
- [V] Shi et al. (2023) https://arxiv.org/abs/2302.00093
- [V] Liang et al. (2025) ThinkSwitcher https://arxiv.org/abs/2505.14183
- [V] Zhang et al. (2025) SynapseRoute https://arxiv.org/abs/2507.02822
- [V] Zhang et al. (2025) Adaptive Dual Reasoner https://arxiv.org/abs/2510.10207 (abstract and intro only)
- [V] Han et al. (2025) TALE https://arxiv.org/abs/2412.18547
