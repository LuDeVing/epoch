# Working memory training transfer: deep document

*Subfield A13.05. Sources: evidence_a-d.jsonl (ids a01-a25, b01-b25, c01-c28, d01-d21), claims.jsonl (K01-K24), critique.md. Status marks: [E] established, [S] single-source, [C] contested. [V] = opened and read, [M] = snippet or abstract only.*

## 1. What it is

Working memory (WM) training asks people to practise memory tasks, mostly adaptive n-back, complex span or Cogmed-style batteries. The hope is that this raises general reasoning (fluid intelligence, Gf), measured by matrix tests such as Raven's APM, BOMAT or Matrix Reasoning.

The idea rests on one correlation: WM capacity and Gf correlate strongly. If WM is a cause of Gf, then training WM should lift Gf. Many people read the 2008 PNAS paper by Jaeggi and colleagues as showing this. It started a large training industry and a large replication literature.

Three kinds of transfer matter:

- Near transfer: gain on untrained tasks that share structure with the trained task (other WM tasks).
- Intermediate transfer: gain on other WM tasks with different materials.
- Far transfer: gain on Gf, reading, maths, attention control.

The verdict after 15 years: near transfer is real, far transfer is about zero once the control group is active and bias is handled. The training mostly improves the trained task and tasks that share its components.

For our project this is a negative result. Our agent is a scaffold around a fixed language model, with no weight training. The human literature says no "practise a memory game, get smarter" shortcut exists. The nearest LLM analogue is RL training on games, which does transfer in some papers (section 6), but that is out of scope for a scaffold-only agent. The useful parts for us are (a) the evaluation lessons (placebo and active controls), (b) the mechanism lessons (efficiency not capacity, strategy), and (c) the LLM work that probes WM and shows which external scaffolds help.

## 2. History and theories in depth

**Background (pre-2008).** WM capacity and Gf correlated strongly in individual-differences work. Raven solving was linked to holding many goals in WM (Carpenter, Just and Shell 1990, cited in a03). Cogmed (Klingberg) reported gains in children with attention problems. Optimism ran high: Shipstead, Redick and Engle (2012, a10 [V]) quote Klingberg 2010, Sternberg 2008, Jaeggi 2011 and Morrison and Chein 2011.

**Jaeggi et al. 2008 (a01-a03, b01 [V]).** Healthy young adults trained on dual n-back (spatial squares plus spoken letters). Four experiments with 8, 12, 17 and 19 sessions. Trained group gain d=0.65 (t(33)=5.53); controls d=0.25 from retest (t(34)=2.08). Group x session F(1,67)=5.27, p<.05, partial eta2=0.07. Gain grew with training time: F(3,30)=9.25, p<.001, partial eta2=0.48. The authors read this as a dose effect. Their theory (a03): dual n-back loads executive processes (inhibition, monitoring, dual-task management, updating, binding) that Gf tests also need. Capacity itself may not be what changes.

**Early cracks (Redick 2013, b03 [V]).** Redick's critique of the 2008 data: four studies pooled with different tests and different session counts; two of four showed matrix transfer and two did not; trained subgroups had n=7, 8 or 11; each dose level used a single Gf test; control groups were passive. Jaeggi 2010 (a04, b03): dual n-back RAPM d=.98 vs control d=.10, but BOMAT d=.49 vs control d=.29, and the BOMAT gain did not differ reliably from control.

**Failed replications 2012-2015.**
- Chooi and Thompson 2012 (a05 [V]): N=93 completers, passive and active controls, 8 or 20 days. No Gf gain. Cells were small (n=4 to 21), so the null is weaker than Redick's.
- Redick et al. 2013 (b02 [V]): 75 completers, 20 sessions, dual n-back vs adaptive visual search placebo vs no contact. Trained groups improved on their own tasks (n-back practice F(19,437)=18.77, partial eta2=.45) but no group improved on any Gf, multitasking, WM capacity or perceptual speed measure. Power above .99 for a medium effect.
- Thompson et al. 2013 (b08 [V]): about 58 people, dual n-back vs multiple-object-tracking vs none, 20 sessions. n-back d' 1.23 to 2.92, 2.60 at about 187-day follow-up. No transfer to Raven.
- Sprenger et al. 2013 (a08 [V]): N=253 across two experiments, transfer limited to tasks sharing stimuli or features.
- Kuepper and Karbach 2015 (a09 [V]): five short sessions, no matrix gain.
- Brehmer 2012 (b15 [V]): Cogmed in young and old, N=100, active low-level control. Reasoning gains equal in both groups.
- Harrison 2013 (b16 [M]): complex-span training improved similar span tasks, not Gf.
- Richey 2014 (b17 [V]): spatial complex WM d=3.16, verbal analogy d=0.10, visual analogy d=0.05. WM change vs analogy change r<=.17.

**Meta-analyses 2012-2017.** Shipstead 2012 (b18 [M]) was a critical review and meta-analysis. Melby-Lervag and Hulme 2013 (a11 [M]) found near gains, no durable far gains. Au et al. 2015 (a13, b11 [M]) was the pro-transfer meta-analysis: 20 n-back studies, healthy adults 18 to 50, Gf g=0.24 (later 0.13 in Au 2016). Soveri 2017 (a14, b09 [V]) re-did n-back with a multilevel model: 203 effect sizes, 33 RCTs. Melby-Lervag, Redick and Hulme 2016 (b05 [V]) was the largest: 87 publications, 145 comparisons.

**Design critique.** Shipstead et al. 2012 named four problems: tasks used singly to define change, invalid WM tasks, no-contact controls, subjective outcomes. Foroughi et al. 2016 (b04 [V]) showed expectation alone: N=50, flyer promising intelligence gains, RAPM 14.72 to 15.76 (d=0.50), control flat.

**Second-order and later work (2017-2025).** Sala and Gobet 2017/2020, Gobet and Sala 2022 (d03-d05 [V]) pooled first-order meta-analyses. Post-2017 trials: Blacker 2017 (d07), Pahor 2022 (d06). Mechanism reviews: von Bastian 2022 (d09 [V]), Traut 2021 (d08 [V]).

**Competing explanations of why transfer fails.**
1. Process overlap (Jaeggi 2008): shared executive processes should transfer. Not borne out.
2. Component overlap (PRIMs, Taatgen 2013, c21 [V]): transfer happens only through shared production elements. Fits the near-only pattern.
3. Efficiency not capacity (von Bastian 2022): training raises strategy use and routines, not the capacity limit. Example: a person trained on digit span for two years went from span 7 to 79 using running-time chunks, with no gain on letter span (d09).
4. Expectation and control artefact (Foroughi, Shipstead): gains come from placebo effects and passive controls in small cells.
5. Retest effect: controls also improve on retest (d=0.25 in Jaeggi 2008).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Founding result: dual n-back raised Gf more than no training | trained d=0.65 (t(33)=5.53); control d=0.25 (t(34)=2.08); F(1,67)=5.27, p<.05, partial eta2=.07; trained subgroups n=7 to 11 | a01, b01, d06 (Jaeggi 2008, V) | [E] it was reported; weak design [E] |
| Dose dependence in 2008 | F(3,30)=9.25, p<.001, partial eta2=.48; 8 vs 19 days p<.001 | a02 | [C] not replicated |
| Gf gain tied to the test used | Jaeggi 2010: RAPM d=.98 vs .10; BOMAT d=.49 vs .29, not reliably different from control | b03 | [E] |
| Large replication, active placebo | N=75 completers; no Gf transfer; power >.99 for medium effect | b02 Redick 2013 | [E] |
| Other replications | Thompson N~58; Chooi and Thompson N=93; Sprenger N=253; Blacker 73 completers, BOMAT group x session F(2,70)=0.77, p=.47 | b08, a05, a08, d07 | [E] |
| Near transfer is real | n-back g=0.62 [0.44,0.81]; other WM g=0.24 [0.16,0.32]; nearest tasks g=0.468 (children, k=76); near 0.44 to 0.46 | b09, d04, b12 | [E] |
| Far transfer to Gf small, shrinks with controls | Soveri Gf g=0.16 [0.08,0.24], 0.11 after control analysis (p>.05); Sala and Gobet Gf 0.11 [-0.02,0.24]; Au 0.24 | b09, a15, a13 | [E] |
| Active vs passive controls (nonverbal ability) | 0.05 [-0.02,0.13] (k=67) vs 0.20 [0.11,0.28] (k=53); Q(1)=6.09, p=.01 | d01 Melby-Lervag 2016 | [C] Soveri found 0.03 diff, p=.429 |
| Sala and Gobet control contrast | passive 0.18 (k=34) vs active 0.05 [-0.05,0.15] (k=40) | d03, b13 | [C] |
| Children, active controls | m=41, k=393, N=2,375; far g=0.001, SE=0.055, p=.982 | d04 Sala and Gobet 2020 | [E] |
| Second-order analysis | 14 meta-analyses, 332 samples, 1,555 effects, 21,968 people; grand mean 0.12 naive, 0.00 active-only; WM training first-order means 0.12 to 0.13 | b14, d05 | [C] same authors produced data |
| Not durable | nonverbal at about 5 months g=-0.05 [-0.21,0.11] (k=12) | d02, b05 | [S] |
| No moderator rescue (Soveri) | single 0.27 vs dual 0.18, diff p=.139; age p=.794; dose none | b10 | [E] |
| Moderators in Melby-Lervag are small-study artefacts | n-back vs treated controls g=0.15 (p=.02), 0.10 without one study; five largest n-back effects had <20 per group, one Gf test, controls fell in 4 of 5 | d02 | [S] |
| Publication bias | p-curve treated z(11)=-2.19, p=.01 (no evidential value); untreated z(16)=-3.41, p<.01 | b07 | [S] |
| Mediation absent | verbal beta=.11, p=.19 (k=29); nonverbal beta=.13, p=.10 (k=38) | b07 | [S] |
| Expectation effect | RAPM d=0.50 (N=50, p<.0001), BOMAT d=0.39; group x time RAPM d=0.98, p=.0013 | b04 | [C] |
| Trained gain decouples from reasoning | spatial CWM d=3.16 vs visual analogy d=0.05; r<=.17 | b17 | [S] |
| Pahor 2022: replication failure within one team | retrospective B=0.23 [0.03,0.43], p=.022; replication B=0.07 [-0.12,0.29], p=.50; 460 people; indirect effect via untrained n-back 0.19 [0.09,0.31] | d06 | [S] |
| Baseline compensation (low gets more) | pooled |r|=0.449, 82 coefficients, 25 papers, I2=91% | d08 | [C] inconclusive; trained-task gain only |
| Cogmed with active control | N=100; far gain only on PASAT and self-rated function | b15 | [S] |

## 4. Mechanisms and models

An engineer wants rules, so here are the mechanisms as procedures.

**4.1 The training loop.** Adaptive n-back: show a stream of stimuli (letters, positions). The user says "match" when the current item equals the item n steps back. Level n goes up when accuracy passes a threshold (for example above 90%) and down below a lower one (for example below 70%). Dual form runs two streams at once. Trained-task score = level reached. Gains are large and fit a linear function in the 2008 data (R2 0.73 to 0.81).

**4.2 Why near transfer happens (PRIMs, c21).** A skill is a set of primitive production rules (read item, compare to buffer, shift buffer). A new task transfers only to the extent it re-uses the same primitives. Implementation: represent each task as a set of components; predicted transfer = overlap of component sets. Sprenger 2013 and Pahor 2022 fit this: tasks with shared stimuli or an untrained n-back mediate gains, while matrix tests share little.

**4.3 Efficiency, not capacity (von Bastian 2022, d09).** Model capacity as a fixed slot count K. Training changes strategy: chunking, mnemonic routines, better use of the K slots. Effective span = K x chunk size. Chunking raises performance on the trained material only. Test for it: transfer to new material (letter span after digit span) should be zero.

**4.4 The expectation channel (Foroughi, b04).** Observed gain = true effect + retest + expectation. Retest estimate from controls (d=0.25 in 2008). Expectation estimate from a placebo arm (d=0.50 on RAPM with a promising flyer). Design rule: compare against an active control with equal contact and equal expected benefit.

**4.5 Attention entropy as a capacity mechanism (Gong and Zhang, c04).** A 1-layer 1-head transformer without FFN trained on n-back: accuracy falls as n rises (Kruskal-Wallis H=38.517, p<.001, eps2=0.248; N=1 vs 3 r=-0.68). Attention entropy rises with n, because attention must pick one earlier token among more distractors. Larger models stay above 95% with slight decline. Implementation: measure attention entropy at the retrieval position; high entropy predicts errors.

**4.6 Proactive interference (Wang and Sun, c10).** Stream key-value updates (46 keys, 3 to 400 updates). Ask for the latest value of a key. Retrieval accuracy falls log-linearly with updates and errors are old values. Model size predicts resistance (rho2=0.673, p=0.0016 within the 128k-131k context band).

**4.7 CoT as serial computation (Li 2024, c18).** A constant-depth transformer without CoT sits in AC0. With T CoT steps it solves any problem a size-T circuit solves. So written steps act as external working memory and extra serial depth, not as a memory store alone.

**4.8 Transfer in RL (ViGaL, SPIRAL).** Reward from a verifiable game, update the policy, test on held-out math. Gain depends on the game mix, opponent quality and base model (section 6).

## 5. What holds up

**Holds up [E].**
- Trained tasks improve a lot. n-back g=0.62.
- Near transfer to similar tasks is real (0.44 to 0.47).
- Far transfer to Gf is small at best (0.11 to 0.16) and about zero with active controls and bias handling (0.00 to 0.05).
- Large, well-powered replications (Redick N=75 power >.99; Sprenger N=253; Chooi and Thompson N=93; Blacker) found no Gf gain.
- The 2008 result rested on small cells and a single test per dose level.
- Post-2017 pooled data agree (children N=2,375, g=0.001). I found no large multi-site RCT after 2017 that reverses the null (limited search, d21).

**Contested [C].**
- Whether the active-control gap is real. Melby-Lervag 2016 finds it for nonverbal ability (Q(1)=6.09, p=.01); Soveri finds 0.03 (p=.429). The spread of Gf estimates (Au 0.24, Soveri 0.16, Sala and Gobet 0.11) follows inclusion rules and control type.
- How much of the Gf gain is expectation. Foroughi is one N=50 study.
- Second-order meta-analyses share authors (Sala, Gobet), so they are not fully independent.

**Moderators.** Age, dose and single vs dual form do not rescue transfer (Soveri). Children and older adults gain more on verbal WM; learning-disorder samples gain more; Cogmed beat other programs on near gains (b06). Those near gains fade at follow-up: verbal WM treated k=10 g=0.28 [-0.004,0.56] (ns). Low-baseline people gain more on trained tasks (|r|=0.449, I2=91%), inconclusive for far transfer.

**Interventions that worked.** Adaptive n-back and complex-span practice on trained and similar tasks. Cogmed on near WM tasks, especially in LD samples. Placebo expectation, which itself lifted RAPM (b04).

**Interventions that did not.** Dual n-back, single n-back, complex span, Cogmed, visual search placebo, tracking, five-session variants, 20-session variants on Gf, reading, attention control. Dose increases and dual form did not help.

**Weak spots in our own evidence base (critique.md).** No numbers read for Harrison 2013 (b16), Shipstead 2012 (b18), Simons 2016 (a17), Au 2015 (a13, b11). Redick 2013 and Chooi and Thompson numbers were read; Chooi cells are small. Sala and Gobet printed CI [-0.09,0.26] around 0.18 looks like a typo (d03).

## 6. Language models

No study was found that trains an LLM on WM tasks to raise reasoning (a22, d19, K10; negative search, 3 to 4 web searches). All LLM work either probes WM or trains with RL on games. So the human question "does training transfer" has no direct LLM answer.

**6.1 n-back probes.**
- Gong, Wan and Wang 2024 (b19, c01-c03 [V]): gpt-3.5-turbo, n=1-3, 50 blocks per n, 24 trials per block (8 matches). Verbal d' above 1 at 1-back (p=8.9e-16) and 2-back (p=1.9e-5), marginal at 3-back (p=0.048, r=0.27). Spatial base grid: 2-back p=0.94, 3-back p=0.97. 7x7 grid stays above d'=1 at 2-back (p=1.4e-6). GPT-4 above d'=1 at 1, 2, 3-back (p=9.3e-10 each); GPT-3.5 and seven open models not at higher n. Noise symbols removed the n effect (H=3.92, p=0.14). Feedback helped at 1-back only. CoT helped at 1 and 2-back (2-back p=1.5e-8), not 3-back (p=0.22). Capacity about 3 in almost all variants (d11), including answer-then-reason.
- Hu and Lewis 2025 (a18, a25, b22, c05, c06 [V]): the weak result partly means the model does the wrong task. Retrieval accuracy at 1/2/3-back (50 trials, 24 letters): Qwen1.5-14B 1.00/0.09/0.08; Llama 3.1 8B 1.00/0.14/0.17; Gemma2-9B 1.00/0.15/0.20; Gemma2-27B 1.00/0.57/0.36; GPT-3.5 1.00/0.51/0.43; Qwen2 72B 1.00/0.81/0.84; Llama 3.1 70B 1.00/0.99/0.93. Weak models answer as if it were 1-back (log-probability analysis). Interactive demos raised the mid-tier model slightly (Gemma 27B 2-back 0.61, +.04). An in-context curriculum raised Llama 70B at n=8/9/10: retrieval 79.83/80.17/71.67% vs 75.25/66.08/57.1% without; task accuracy 90.08/90.08/84.75% vs 83.33/78.25/71.92%. Reciting the last n letters lifted even weak models.
- The two papers differ in prompt (m/- labels vs retrieved letter plus a 24-letter demo), metric (d' vs retrieval accuracy and log-probabilities) and models (d10). Not run on one model at equal tokens, so the disagreement over capacity vs task understanding is [C].
- Zhang et al. 2024 (b21, c07, c08, c26 [V]): n-back across text-ada-001 to GPT-4, U-shape over size. Human-inspired prompt tweaks: text-ada-001 on Tracking Shuffled Objects 25.4% (+15.8 over CoT); text-davinci-002 code-style rewrite 96.4% (+4.8); rehearsal prompt about +18 points on Object Counting. On BBH, GPT-3.5 answer-only 57.1% vs 62.93% mean of five prompt methods.
- Liang et al. 2026 (a21 [V]): Qwen2.5 spatial n-back, text input beat vision grids at matched content; log-probability analysis shows nominal 2-back behaves like lower-n.
- Gong and Zhang 2024 (b20, c04 [V]): small transformers trained from scratch on n-back lose accuracy as n grows, and attention entropy rises with n.
- Executive function study (b23 [V]): forward span of 50 digits 0.99 to 1.00 for open LLMs; backward span of 15 weak (Gemma-9B 0.21, Llama-8B 0.18, Qwen2-7B 0.00); reasoning models fix flanker but not WM or card sorting.

**6.2 Hidden-state tests.** Huang et al. 2025 (a20, c09 [V]): n-back lets models read answers from context, so they built tasks needing a silent value. Number Guessing (ideal Yes-sum 1.0): seven models 0, LLaMA-405B 1.195, GPT-4o 1.085, DeepSeek-R1 0.640. Yes-No Deduction (200 trials): GPT-4o-mini 200/200 failures, GPT-4o 173/200. Math Magic without CoT 0 to 26%, o3-mini with CoT 96.7%. [S] one paper.

**6.3 Interference and context.** Wang and Sun 2025 (c10-c12, d16 [V]): llama4-maverick near 100% at 2 tracked keys, under 5% at 46. Value length: under 40% at 10 words, under 5% at 40 words for every model. "Forget" prompts changed under 10 points at 100 updates and hurt gpt-4.1-mini. A mock-QA reset (a fake earlier question and answer) helped: Gemini Flash 2.0 at 150 updates matched its 30-45-update baseline. RULER (c19 [V]): of 17 models claiming 32K context, only about half keep satisfactory performance at 32K.

**6.4 RL training on games: the nearest analogue to Jaeggi.**
- ViGaL (c13, d17 [V]): Qwen2.5-VL-7B, Snake plus Rotation RL. Math avg 47.7 to 50.6; MathVista 68.0 to 71.9; MathVerse 49.0 to 52.4; MMMU val 54.3 to 58.0. Controls: random-label RL 49.4 vs base 49.1 (no gain); SFT on the same Snake data 47.2 (math 38.0, below base). Full average 49.1 base to 62.3 with Snake RL.
- SPIRAL (c14, c15, d18 [V]): Qwen3-4B-Base 34.0 to 44.5 (+10.5; SFT-Multi 39.7); Qwen3-8B 39.5 to 49.6; Octothinker-8B 25.8 to 33.8; Llama-3.1-8B-Instruct 23.9 to 25.9 (+2.0); DeepSeek-R1-Distill-7B 60.4 to 61.8 (+1.4). Single games 40.0 to 43.4; trained against a fixed Mistral opponent 29.6, below base.
- Reasoning Gym (c16 [V]): Qwen2.5-3B-Instruct Algebra 23.83 to 52.89 (+29.1, trained on Algorithmic); Cognition +13.3 from Logic; MATH 48.5 to 58.2 (+9.7); ARC 6.49, no transfer helped (-2.3).
- Gandhi 2025 (c17 [V]): same Countdown RL, Qwen-2.5-3B about 60% vs Llama-3.2-3B about 30%. Priming Llama with four reasoning behaviours closed much of the gap. Gains depend on whether the base model already has the behaviours.
- Pattern [C]: unlike humans, models trained by RL on games transfer, but unevenly, shrink for already-tuned models, and none was tested on ARC. This is training, so it does not apply to a scaffold-only agent.

**6.5 Equal-token controls for LLM scaffolds.**
- Can 2026 (d14, d15 [V]): on a 0.5B code model, best-of-8, length-matched placebo recovered +19.5 vs structured +22.0 points; placebo trails full skill by 2.4 (p=0.60). Claude Sonnet 4.6 at ceiling: V 95.1%, F 95.7%, L 95.7%, placebo 96.9% (N=163, none significant). Blind resampling at equal budget matched content-bearing feedback (26 vs 26 unlocks pooled). Single-source.
- Levy 2024 (d13 [V]): irrelevant padding lowers accuracy 0.92 to 0.68 at about 3,000 tokens (600 samples per point). So padding is not neutral.
- Pfau 2024 (d12 [V]): meaningless filler tokens can add compute, but only with dense supervision in training. So an equal-token control can still carry hidden compute.

**6.6 What changed LLM performance, by how much.** External structure helped: CoT (Math Magic 0-26% to 96.7%), rehearsal prompt (+18 on Object Counting), in-context curriculum (+8 to +14 retrieval points at n=8-10), mock-QA reset (about 120 fewer effective updates of damage), larger grids (less interference). Instructions to forget, labels and feedback did not help at higher n. Model size changes the failure mode.

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Do not build a "practice stage" (warm-up drills on memory-like tasks before the real item) expecting general reasoning gains. Human far transfer is about zero with active controls. Keep any such stage as a control arm only. | G7 (pay for itself) | [E] | K01, K02, K06, K19; b02, d04, d05 |
| 2 | Judge every scaffold element at equal tokens against the plain model, using several test items and enough items per arm. Small cells and one test produced the 2008 effect. | G7 | [E] | K03; a01, b03, d06 |
| 3 | Report which padding was used in equal-token controls: neutral text (can hurt) or content-free scaffold (may add compute). | G7 | [E] | K22; d12, d13 |
| 4 | Put explicit intermediate state in a visible record (steps, rehearsal of the last n items) for tracking-style subtasks. Externalised steps lift LLM results on WM-bound tasks. | S/O (scratchpad, rehearsal) | [E] | K13; c08, c09, c18, d11, d12 |
| 5 | Treat long context as not usable working memory: use an explicit external buffer or summary for state beyond a few updates. | memory | [E] | K11, K16; a18, c05, c19, c10 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 6 | Equal-length placebo scaffold arm, in addition to a bare-prompt arm, for every scaffold claim. | G | [C] | K04, K21; b04, d14, d15 |
| 7 | Decompose raw n-back-like items into retrieve-then-compare steps (task understanding over capacity). | O (decomposition) | [C] | K12; c06, c27, d10 |
| 8 | Write hidden state (a chosen number, a held value) into a visible note before use. | O (explicit state record) | [S] | K14; a20, c09 |
| 9 | Structured memory reset (mock-QA turn, pruning) when many updates to the same keys. Forget instructions do not work. | memory | [S] | K15; c10, c11, d16 |
| 10 | Scale scaffold strength to model baseline and item class: gains shrink as the base model gets stronger (SPIRAL +10.5 vs +1.4). | O (per-item scaffold choice) | [C] | K23, K17; d08, d09, d18 |
| 11 | External scratchpad vs same tokens of free chain of thought on tracking. No head-to-head exists. | S/O | [S] | K24; d11, d20 |
| 12 | Probe-based transfer: does a gain on an n-back-like probe predict a gain on matched matrix-style items? | G (evaluation) | [S] | K20, K07; d06, b17 |

Items outside scope: any fine-tuning or RL on games (K17, K10), and human-only moderators (age, dose).

## 8. Concrete tests on our bench

All arms at equal total tokens (output plus scaffold), same model, same item set, at least three seeds. Padding for placebo arms is stated.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 60 held-out matrix or ARC-style reasoning items | (a) plain, (b) warm-up stage of n-back-like drills then item, (c) equal-token neutral-text prefix | accuracy, paired difference with McNemar | (b) minus (a) within 2 points; (b) may be below (a) because of padding cost |
| T2 | 60 scaffold-claim items (our current best scaffold) | (a) plain, (b) scaffold, (c) length-matched placebo scaffold, (d) labels-only, (e) blind resampling at equal budget | accuracy; share of scaffold gain recovered by placebo | placebo recovers over half of the gain on a small model, little on a strong one |
| T3 | n-back and tracking items, n=1 to 8, 24 letters | (a) raw m/- prompt, (b) retrieve-then-compare decomposition, (c) same, with demos | retrieval accuracy and d' per n | (b) lifts 2-back and 3-back on mid and small models by 20 or more points; strong models near ceiling |
| T4 | Hidden-state items (Number Guessing, Yes-No Deduction) | (a) plain, (b) forced visible note of the chosen value, (c) free reasoning at equal tokens | Yes-sum deviation from 1.0; failure rate over 200 trials | (b) cuts failure rate sharply; (c) partial |
| T5 | Key-value update streams, 46 keys, 3 to 400 updates | (a) none, (b) forget instruction, (c) mock-QA reset, (d) external buffer of current values | retrieval accuracy vs update count | (c) and (d) help; (b) under 10 points; (d) best |
| T6 | Tracking tasks (shuffled objects, counting) | (a) free CoT, (b) rehearsal prompt, (c) structured scratchpad, equal tokens | accuracy | (b),(c) above (a) by 5 to 18 points on weak models |
| T7 | Items stratified by plain pass rate (low, mid, high) | (a) plain, (b) scaffold | gain by stratum | gain shrinks as plain pass rate rises, as in SPIRAL |
| T8 | n-back-like probe plus 40 matrix items | probe score before and after scaffold; matrix score before and after | correlation of probe change with matrix change | r near 0 (decoupling, as in Richey r<=.17) |
| T9 | Same prompt sets from Gong and Hu and Lewis, one model | (a) Gong prompt, (b) Hu and Lewis prompt, equal tokens | d' and retrieval accuracy | shows how much of the disagreement is wording |

## 9. What does not transfer, and why

- **Practice effects on one task.** In humans, the trained task rises (d up to 3.16) and reasoning does not (d=0.05). The gain is task-specific skill and strategy. For our agent, a warm-up on a memory drill gives skill only inside that context window.
- **Capacity.** Training raises efficiency, not capacity (von Bastian). Our model has no slot count to train. External memory, not rehearsal of memory games, adds capacity.
- **Moderator rescues.** More sessions, dual form, and age targeting did not raise far transfer. Do not expect "more warm-up" to fix it.
- **Human individual-difference results.** Low-baseline compensation (|r|=0.449) concerns trained-task gain in people.
- **Expectation effect as written.** Humans respond to promise flyers. A language model has no such expectation, but prompts that sound confident may still shift outputs; this is untested.
- **RL game transfer.** It works in some models, but needs weight training, a good opponent, a base model with the right behaviours, and it gave no ARC gain in papers that tested it (Reasoning Gym ARC -2.3). It does not port to a prompt scaffold.
- **Human WM capacity limits.** Not the same mechanism: models fail at n-back partly from task misunderstanding (Hu and Lewis), partly from attention dispersal (Gong and Zhang), partly from interference (Wang and Sun). Each has a different remedy.

## 10. Open questions

1. Does any LLM trained or fine-tuned on n-back or span tasks improve on matrix or ARC reasoning against an equal-compute control? (Gap 1; searches found none.)
2. How large is the expectation effect in a prompt scaffold, against an equal-token placebo prompt on our scaffold? Analogue evidence only (d14, d15).
3. How much of the Gong vs Hu and Lewis disagreement is prompt wording? No one-model equal-token test.
4. Does an external scratchpad beat free CoT at equal tokens on n-back and tracking? No head-to-head exists (d20).
5. Do human boundary conditions (dose, age, single vs dual) have LLM analogues (demos, context length, model size)? No study varies all three.
6. Does proactive interference respond to a structured reset across model sizes at equal tokens? Only four models, no size-tier analysis.
7. Do RL game gains survive format and pretraining controls, and why does ARC not benefit?
8. Is the active-control gap real? Two meta-analyses say yes for nonverbal ability; Soveri says no.
9. Is the 2025 preregistered trial mentioned in search output real? Not identified.
10. Is an n-back-like probe a valid predictor of matrix-reasoning gain for scaffolds (Pahor mediation)?

## 11. Sources

All evidence ids are in evidence_a-d.jsonl in this folder.

[V] opened:
- Jaeggi et al. 2008, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC2383308/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC2383929/ (a01-a03, b01)
- Jaeggi et al. 2010, relationship between n-back and Gf. https://gwern.net/doc/dual-n-back/2010-jaeggi.pdf (a04)
- Chooi and Thompson 2012. https://gwern.net/doc/dual-n-back/2012-chooi.pdf (a05)
- Redick et al. 2013 (via PubMed, text read in b02, b03, b25). https://pubmed.ncbi.nlm.nih.gov/22708717/ [critique notes: power figures not re-opened]
- Thompson et al. 2013, PLoS ONE (b08). https://journals.plos.org/plosone/
- Sprenger et al. 2013. https://gwern.net/doc/dual-n-back/2013-sprenger.pdf (a08)
- Kuepper and Karbach 2015. https://gwern.net/doc/dual-n-back/2015-kuper.pdf (a09)
- Shipstead, Redick, Engle 2012 review. https://gwern.net/doc/dual-n-back/2012-shipstead.pdf (a10)
- Soveri et al. 2017, Psychon Bull Rev. https://doi.org/10.3758/s13423-016-1217-0 (a14, a24, b09, b10)
- Sala and Gobet 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5724589 (a15, b12, b13, d03)
- Gobet and Sala 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9903001/ (a16, b14, d05)
- Melby-Lervag, Redick, Hulme 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4968033/ (b05-b07, d01, d02)
- Sala and Gobet 2020, children. https://link.springer.com/content/pdf/10.3758/s13423-019-016 (stem as logged; see d04) (d04)
- Foroughi et al. 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4941515/ (b04)
- Brehmer et al. 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3313479/ (b15)
- Richey et al. 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4154731 (b17)
- Pahor, Seitz, Jaeggi 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC12305750/ (d06)
- Blacker et al. 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5805159/ (d07)
- Traut, Guild, Munakata 2021. https://www.frontiersin.org/articles/10.3389/fpsyg.2021.6621 (stem as logged; see d08) (d08)
- von Bastian et al. 2022. https://eprints.whiterose.ac.uk/178761/ (d09)
- Taatgen 2013 (PRIMs). https://www.ai.rug.nl/~niels/actransfer.html (c21)
- Gong, Wan, Wang 2024, ChatGPT working memory. https://arxiv.org/abs/2305.03731 (b19, c01-c03, d11)
- Gong and Zhang 2024, self-attention. https://arxiv.org/abs/2409.10715 (b20, c04)
- Hu and Lewis 2025. https://arxiv.org/abs/2412.18120 (a18, a25, b22, c05, c06, d10)
- Zhang et al. 2024, EMNLP. https://aclanthology.org/2024.emnlp-main.938 (b21, c07, c08, c26)
- Huang, Sun, Wang, Dredze 2025. https://arxiv.org/abs/2505.10571 (a20, c09)
- Liang et al. 2026. https://arxiv.org/abs/2602.04355 (a21)
- Strong memory, weak control. https://arxiv.org/abs/2504.02789 (b23)
- Wang and Sun 2025. https://arxiv.org/abs/2506.08184 (c10-c12, d16)
- Xie et al. 2025 (ViGaL). https://arxiv.org/abs/2506.08011 (c13, d17)
- SPIRAL. https://arxiv.org/abs/2506.24119 (c14, c15, d18)
- Reasoning Gym. https://arxiv.org/abs/2505.24760 (c16)
- Gandhi et al. 2025. https://arxiv.org/abs/2503.01307 (c17)
- Li et al. 2024, CoT. https://arxiv.org/abs/2402.12875 (c18)
- Hsieh et al. 2024, RULER. https://arxiv.org/abs/2404.06654 (c19)
- MemGPT. https://arxiv.org/abs/2310.08560 (c20)
- Schmidt et al. 2023. https://arxiv.org/pdf/2303.11944 (c22)
- Pfau, Merrill, Bowman 2024. https://arxiv.org/abs/2404.15758 (d12)
- Levy, Jacoby, Goldberg 2024. https://arxiv.org/abs/2402.14848 (d13)
- Can 2026, scaffold placebo studies. https://arxiv.org/pdf/2606.06454 and https://arxiv.org/pdf/2606.31511 (d14, d15)

[M] snippet or abstract only:
- Thompson et al. 2013 earlier note a07. https://knowledge.uchicago.edu/record/10823/
- Redick 2013 abstract a06 (later opened via b02).
- Melby-Lervag and Hulme 2013. https://doi.org/10.1037/a0028228 (a11)
- Au et al. 2015. https://doi.org/10.3758/s13423-014-0699-x (a13, b11)
- Simons et al. 2016. https://www.psychologicalscience.org/ (a17)
- Harrison et al. 2013. https://pubmed.ncbi.nlm.nih.gov/24091548/ (b16)
- Shipstead et al. 2012 meta-analysis. https://pubmed.ncbi.nlm.nih.gov/22612437/ (b18)
- Backward digit span benchmark. https://escholarship.org/content/qt28m3k4g4/qt28m3k4g4.pdf (a23)
- Aichberger and Hochreiter 2026. https://arxiv.org/abs/2605.30343 (b24)
- Jaeggi 2010 concurrent validity. https://doi.org/10.1080/09658211003702171 (c25)
- Sala et al. 2019 older-adult meta-analysis (search text only, d21).
- Negative searches a22, d19, d20.
