# Monitoring and control framework: deep document

*Subfield A04.01. Evidence ids (a01 to d23) are in evidence_a-d.jsonl; claim ids (A04.01-K01 to K36) are in claims.jsonl; the cross-check is in critique.md. All in this folder. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The framework says a thinking system has two levels. The object level does the work: it learns, recalls, solves. The meta level holds a model of the object level and steers it.

Two flows join the levels.
- **Monitoring** goes up. The object level informs the meta level: how well is this item learned, do I know this, is this answer right.
- **Control** goes down. The meta level changes the object level: start, continue, or stop an action; choose a strategy; decide whether to output an answer.

Nelson and Narens (1990) gave three principles (a01). Cognition splits into object and meta level. The meta level holds a dynamic model of the object level. Information flows up as monitoring and down as control. Control changes the object level. Monitoring only informs the meta level (a02). Their analogy: control is speaking into a telephone, monitoring is listening.

The framework is laid out in a grid of stages (acquisition, retention, retrieval) by judgments (a04).
- Before learning: ease-of-learning (EOL) judgments.
- During learning: judgments of learning (JOL) on items one can recall.
- At retrieval: feeling of knowing (FOK) on items one cannot recall now; confidence in an answer just given.
- Control types: choice of processing, allocation of study time, termination of study, choice of search strategy, termination of search, and output of the response (answer or withhold).

Why this matters for our agent: state S6 (impasse) and the gates G1, G6, G12 are control decisions made on a monitoring signal. The schema's rule "code monitors, model acts" is a Nelson-Narens split. This document asks what the evidence says about each part of that split: how good the monitor is, how good the control rule is, and whether the split beats letting the model do both.

Three points from the founding chapter shape everything below.
1. Monitoring is a measurement, not a window. Introspective reports are data to be explained, like a telescope's distortions (a03).
2. Monitoring and control can come apart. A good monitor does not make good control; good control needs a valid monitor (Koriat and Goldsmith, a29; Huang, c22).
3. A controller needs a model of what it controls (Conant and Ashby 1970, cited in a01). A spy (monitoring with no control) and a blind actor (control with no feedback) are the two broken designs.

## 2. History and theories in depth

### 2.1 Founding: Nelson and Narens, 1990 (a01 to a19)

The chapter pulls together a decade of lab work. The key results, all read in full text:

- **FOK is reliable but nearly invalid at first.** In 1976 to 1979 experiments with number-word pairs, people ranked items by feeling of knowing the same way on retest, and transitively, yet the rankings barely predicted later recall (a07).
- **Accuracy depends on how well items were learned.** 1979 experiment, 27 or 28 people per group: immediate test after one study trial, 35% recall, 63% of subjects had positive gamma (not significant); one week after one correct recall, 45% recall, 71% positive (marginal) (a08).
- **Overlearning kills monitoring accuracy.** A judgment can only separate items that differ. Leonesio and Nelson (1982): gamma between trials-to-first-recall and later retention was +.02 (criterion of one recall), -.15 (two), -.25 (four) (a09). Leonesio (1985): FOK-recognition G of +.28 fell to +.01 once item difficulty was controlled (a09).
- **The judgments are different signals.** Later recall was predicted by JOL with G = +.31 and by EOL with G = +.12 (Leonesio and Nelson 1990). EOL predicted trials to learn with mean G = -.22 (a10).
- **FOK is blind to new information.** Jameson et al. (1990): a flash of the correct answer raised recall from .10 to .28, but FOK moved only 5.2 to 5.4 (a11).
- **Privileged access is real but modest.** The person beat an outside judge who saw only the question at predicting the person's own later recognition (two experiments, 15 missed items per target) (a12). Own FOK G = +.28 in the normative data.
- **No-Magic hypothesis.** FOK does not read hidden traces. It uses cues: acquisition history, partial information, and rules linking them. Evidence: people who thought they had recalled an item five times (actually once) gave median FOK 16 versus 10 for those who thought once (actually five) (a13).
- **Control follows monitoring, weakly.** EOL vs self-paced study time mean r = -.3. Students told to study until sure of 100% reached only 49% recall in Experiment 1 (a14).
- **Experimenter-set control test.** n = 52 per group, same total study time. Recall: 63.9% (constant 4.3 s per item), 64.5% (random 8 s or 0.5 s), 64.4% (more time to low-FOK items), 56.7% (more time to high-FOK items). Giving time to items already judged known hurt (a15). The random group showed time mattered (G = +.39 between time and recall).
- **FOK controls stopping on failure, not on error.** FOK vs latency of omission errors G = +.60; vs commission-error latency G = +.03. Confidence vs commission latency G = -.40; vs correct-recall latency G = -.55 (a17). So search runs until FOK says give up, but wrong answers come out under a different control rule.
- **A quick preliminary FOK exists.** n = 10, 239 questions: fast FOK ratings at both ends of the scale, slow in the middle, which supports a separate fast counter that decides whether to search at all (a16).
- **Practice does not fix FOK.** Feedback group (58 people) flat across 3 blocks; no-feedback group a small gain, t(57) = 2.69; Experiment 2 (n = 36) no change (a19).
- **Measurement.** Gamma is used because it ignores ties and needs no distribution assumptions. People are often overconfident, including when intoxicated (a18).

Two control rules were drawn as flowcharts.
- **Study termination (a05):** compare judged mastery (from JOL or FOK) with the "norm of study" (wanted ease at test, raised by the person's theory of retention). Stop when mastery reaches the norm. A strategy library stores estimated acquisition rate per strategy and item kind.
- **Retrieval termination (a06):** a fast preliminary FOK decides whether to search. During search an ongoing FOK and a cost-reward rule decide when to quit. They cite Simon (1979) satisficing. Marijuana raised commission errors without changing correct recall; high altitude lowered them.

### 2.2 Delayed JOL: a monitoring fix (a20 to a22, b16, b17)

- Nelson and Dunlosky (1991) found that JOLs made after a delay predict recall far better than JOLs made right after study (a21, snippet only).
- Dunlosky and Nelson (1994) gave numbers. Mean gamma: Experiment 1 (36 students, imagery vs rote) immediate +.10 and +.29 (overall +.18), delayed +.72 and +.93 (overall +.83) (a20).
- Meta-analysis (Rhodes and Tauber 2011; numbers second-hand): 4,554 people, 112 effect sizes, g = 0.93 on relative accuracy; 3,807 people, 98 effect sizes, g = 0.08 on memory itself (b17, a36). Big gain in monitoring, almost none in memory.
- Thiede, Anderson and Therriault (2003): N = 66, three groups of 22, six texts. Writing keywords after a delay raised comprehension-judgment accuracy, F(2, 63) = 4.07. Regulation gamma between judgment and restudy choice: .79 delayed-keyword, .35 immediate, .36 none. Second-test old items .69 vs .53 vs .56 (a22, b16). This is the cleanest human case that better monitoring causes better control and better outcomes.
- Common explanation: delayed JOLs draw on what can actually be retrieved from long-term memory, while immediate JOLs draw on what is still in short-term memory and is misleadingly fluent.

### 2.3 Allocation and stopping (a23 to a26, b15, b24)

The dominant older model was discrepancy reduction: study what is furthest from the goal, stop at a mastery criterion. Metcalfe and Kornell (2003, 2005) tested and mostly rejected it.

- Experiment 1 (12 students, English-Spanish pairs, time limits 5 s, 15 s, unlimited): time on the hardest items rose 0.71, 3.56, 8.61 s with the limit, yet hardest-item recall did not improve (a23).
- Free choice: easiest unlearned items first; most time on medium items. Information-uptake curves explain it: easy items gain quickly in the first 0 to 0.5 s then flatten; medium items gain faster later (Exp 3A, N = 33, t(32) = 2.86; Exp 3B, N = 29) (a24).
- **Region of Proximal Learning (RPL) model**, eight new experiments (a25, b15). Step one: drop items judged already known. Step two: study the rest from nearly-known to hard. Chosen items had higher JOL (36.70) than rejected (25.31), t(47) = 4.24; choice-JOL gamma +.34. In Exp 1 (N = 24), 20 of 24 said they chose items they did not know, and chosen items were harder by norms (180.90 vs 138.64, t(23) = 7.88).
- **Stopping rule (a26):** people do not stop at a learned-enough criterion. They stop when the rate of judged progress falls. Exp 8, 19 people, 283 non-negative JOL changes: JOL change vs study time r = .40, p < .0001. Stop-time JOLs spread over the whole scale.
- Other work: labor-in-vain (Mazzoni and Cornoldi 1993): more study time does not always mean more recall, in five experiments (a35, b23; snippet only). Undorf and Ackerman (2017): time vs JOL is an inverted U; time limits explain it (b24, snippet only).

### 2.4 Output control: withholding and grain size (a27 to a29, b20 to b22)

Koriat and Goldsmith (1996) extended the framework to the report decision.
- Model: each best candidate answer has an assessed probability of being right. The person answers if it clears a criterion set by the payoff for accuracy vs quantity. With no monitoring resolution, free report gives no accuracy gain and only cuts quantity. With good resolution, a higher criterion raises accuracy at small cost in quantity (a27).
- Experiment 1: N = 71, 60-item general-knowledge test, recall or 5-choice recognition, forced then free phase, moderate or high accuracy incentive. Free report lifted accuracy sharply; a stricter payoff made people stricter, at a quantity cost (a28).
- Experiment 2 (about 30 people, 90 recall items: 30 standard, 30 deceptive, 30 difficult): standard items forced accuracy 27.9%, free 75.0%, quantity 22.3%. Deceptive items forced 11.8%, free 21.0%, quantity 7.6% (a29). On deceptive items confidence was uninformative, yet people still used it, so the gain was small. Control only helps when monitoring is valid.
- Grain size (Goldsmith, Koriat and Weinberg-Eliezer 2002; about 40 people): fine-grain answers later volunteered at fine grain were right .50 of the time vs .21 for those later reported coarse; coarse answers .88 vs .67 (b20). A social-feedback extension (Rechdan et al. 2017; N = 87 and 90) found no effect on confidence or detail level (b22).

### 2.5 Framing and cue use (a30, b18, b19)

- Koriat (1997) cue-utilization: JOLs come from intrinsic cues (item difficulty), extrinsic cues (repetition, conditions), and mnemonic cues (ease of retrieval). 16 per condition, 50 Hebrew pairs; recall 67.2 vs JOL 55.5 (underconfidence); JOL-recall gamma rose from about .58 to .67 on a second block (a30).
- Finn (2008): telling people to remember or to forget the same items changed JOL and restudy choices but not recall. Exp 2 (N = 46): recall .37 vs .40 (not significant), JOL .56 vs .46, restudy .45 vs .65, t(44) = 2.22. Exp 3 (N = 42): restudy .36 vs .52 (b18). Control follows the judgment, not the true state. Metcalfe and Finn (2008): same when JOLs were manipulated apart from recall (b19, second-hand).

### 2.6 Rational models (a31, a33, b25, c13, c28)

Callaway, Griffiths, Norman and Zhang (2023) cast retrieval control as a meta-level decision process: continue searching while the expected value of more search beats its cost. Human data (Prolific, N = 612): faster recall of high-confidence targets (B = -0.244, t(516.1) = -9.54) and slower give-up when FOK is high (B = 0.385, t(189.1) = 10.02) (a31). This gives an implementable stopping rule. Oh and Gobet (2025) map the framework onto language-model reasoning as Monitor-Generate-Verify; it is a design paper with no experiments (a33, b11, c12).

### 2.7 Older AI versions (c29)

Cox (2005) reviews the metacognitive loop (notice anomaly, assess, guide response) and MIDCA: a meta-level over an object-level agent, in code. Named from a snippet only (c29, [M]).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Monitoring and control can dissociate (humans) | Framing changed JOL .56 vs .46 and restudy .45 vs .65, recall unchanged .37 vs .40 (N=46) | Finn 2008 (b18) | [E] |
| FOK is reliable but weakly valid at first, and depends on learning state | 63% (immediate) and 71% (1 wk) of subjects positive gamma, neither clearly significant; overlearning drives gamma to +.01 or negative | Nelson & Narens 1990 (a07-a09) | [E] |
| EOL, JOL, FOK are different signals | Recall predicted by JOL G=+.31 vs EOL G=+.12 | Leonesio & Nelson 1990 via a10 | [S] |
| FOK blind to new information | Recall .28 vs .10; FOK 5.4 vs 5.2 | Jameson et al. 1990 via a11 | [E] |
| Monitoring uses inferential cues | Median FOK 16 vs 10 by believed, not true, acquisition history | Nelson & Gillespie via a13; Koriat 1997 (a30) | [E] |
| Person has modest privileged access | Target beat outside Judge on 15 missed items per target; own FOK G=+.28 | a12 | [S] |
| Delayed JOL boosts monitoring accuracy | gamma +.83 delayed vs +.18 immediate (N=36); meta-analysis g=0.93 (112 effects, 4,554 people) but g=0.08 on memory | Dunlosky & Nelson 1994 (a20); Rhodes & Tauber 2011 (b17, second-hand) | [E] |
| Better monitoring gives better regulation and learning | F(2,63)=4.07; regulation gamma .79 vs .35 vs .36; N=66 | Thiede et al. 2003 (a22, b16) | [S] |
| Control quality is imperfect | More time to high-FOK items: 56.7% vs 63.9-64.5% (n=52 per group) | a15 | [E] |
| Allocation is not discrepancy reduction | Easiest-unlearned-first; JOL change vs time r=.40; chosen JOL 36.70 vs 25.31 | Metcalfe & Kornell 2003, 2005 (a23-a26) | [E] |
| Withholding raises accuracy only with valid monitoring | Standard 27.9% to 75.0% (quantity 22.3%); deceptive 11.8% to 21.0% (quantity 7.6%) | Koriat & Goldsmith 1996 (a29) | [S] |
| Practice and feedback do not fix FOK | Feedback group flat (58 people) | a19 | [S] |
| Retrieval stopping follows value of continuing | N=612; B=-0.244 and B=0.385 | Callaway et al. 2023 (a31) | [S] |
| LLMs: confidence predicts correctness, but reasoning length does not rise on doubt | 9 LLMs, Fig. 1; harness attempts fall from low to high confidence | Cao 2026 (b07, c06) | [S] |
| LLM harness with code control on FOK/JOL | Pass@1 48.3 to 56.9 (+8.6), N=1,859, 2.4 attempts, $0.78/q; HLE 48.0 to 60.0; LCB 74.3 to 84.3; R-Bench-V 36.1 to 41.1 | Cao 2026 (a34, b06, c01) | [S] |
| Gain sits on doubted items | JOL low 0.16 to 0.42; medium 0.36 to 0.55; high 0.67 to 0.64 | Cao 2026 (b08) | [S] |
| Confidence ranks problems, not attempts | Within-problem JOL SD 0.048 vs between 0.270 (5.6x) | Cao 2026 (b09, c05) | [S] |
| Monitor quality varies by model | Of 9 models only Sonnet 4.6 passed all checks; Sonnet FOK AUROC .612, JOL .745, joint .757 (ECE .087); Gemini 3 Flash FOK AUROC .818, ECE .465 | Cao 2026 (c04) | [S] |
| Accuracy and monitoring rank are inverted | GLM-5 1st accuracy, 9th monitoring; Haiku 4.5 13th and 2nd; 20 models, 524 items, 10,480 evaluations | Cacioli 2026 (b01, c08) | [S] |
| Most models keep and bet on everything | 17 of 20 scored 0% on six adversarial foils while answering KEEP+BET | Cacioli 2026 (b02, c11) | [S] |
| Retrospective monitoring and prospective regulation weakly linked | r=.17, CI -.29 to +.57, n=20 models | Cacioli 2026 (b03, c09) | [S] |
| Monitoring is domain-specific, no scaling law | Sonnet 4.6 withdraw delta +8.3% to +93.0% by task; Qwen falls with size, GPT-5.4 rises, Gemma flat | Cacioli 2026 (b04, c10) | [S] |
| Domain gap in monitoring | AUROC Applied .742; Formal Reasoning .658; Natural Science .652 (33 models, 1,500 items) | Cacioli 2026b (d12) | [S] |
| Intrinsic self-correction fails | GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle GPT-4 GSM8K 97.5, CSQA 85.5, HotpotQA 59.0 | Huang et al. 2024 (b14, c22) | [E] |
| Fixing is strong, finding is weak | Oracle step location: +23.53, +43.92, +36.86, +18.04, +18.06 on originally wrong traces (2,186 traces, 5 tasks) | Tyen et al. 2024 (c23) | [S] |
| Step-finding depends on model | ProcessBench F1 o1-mini 87.9 vs GPT-4o 61.9 | Zheng et al. 2024 (d20) | [S] |
| Verbal confidence is weak for older models | GPT-4 AUROC 62.7% avg; ECE >.377 for GPT-3/3.5/Vicuna | Xiong et al. 2024 (b13, c16) | [C] |
| Agreement beats verbal confidence on arithmetic | GPT-3.5 GSM8K AUROC 54.8 to 92.7 (5 samples + consistency) | Xiong et al. 2024 (c16) | [C] |
| Verbal confidence better than logits for RLHF models | ECE cut ~50% relative; TriviaQA ECE .068, AUC .879 | Tian et al. 2023 (c17) | [C] |
| Hybrid monitor for reasoning models | Maths AUROC 84.2 at K=2 vs VC 81.4 and SC 79.6 at K=8 | Del et al. 2026 (d01) | [C] |
| Easy facts: verbal beats agreement | AUROC .956/.937 vs 3-sample .765/.790 (99 items, 2 models) | Meyer et al. 2026 (d02) | [S] |
| Agreement-based stopping works | Up to 7.9x fewer samples at <0.1% loss; 33.8% (MATH) to 84.2% (Coin Flip) fewer | Aggarwal 2023; Li 2024 (d03, d04) | [E] |
| Difficulty-aware allocation beats uniform best-of-N | ~4x less compute (Snell); up to 50% less (Damani) | d05, d06 | [E] |
| Abstention worsens with reasoning fine-tuning | 24% average drop in abstention | AbstentionBench (d08) | [C] |
| Prompt wording moves confidence | .043 to .084 average score change; 4 to 9% of threshold decisions flip; marker words moved accuracy up to 80% (GPT-3) | d02, d22 | [S] |
| LLMs fail JOL tasks | GPT-3.5-turbo, GPT-4-turbo, GPT-4o did not predict own later memory | Huff & Ulakci 2025 (d16) | [S] |
| Behavioural metacognition is limited | One model raised team accuracy over best of self/teammate: +5.4 (GPQA), +8.6 (Simple MC) | Ackerman 2026 (c19) | [S] |
| Trained monitoring beats prompted | Self-RAG 7B/13B beat ChatGPT; ~1,000 graded answers train a useful uncertainty probe | Asai 2023; Kapoor 2024 (c26, c18) | [E] |
| Models can estimate P(True), P(IK) | 52B: P(IK) TriviaQA .864 AUROC but GSM8K .624 when trained on TriviaQA only | Kadavath 2022 (a32, c14, c15) | [S] |
| SelfAware: models below humans at unanswerable items | Human F1 84.93 vs GPT-4 75.47 | Yin et al. 2023 (c27) | [S] |

## 4. Mechanisms and models

This section gives each model in a form an engineer can build.

### 4.1 The two-level loop (Nelson and Narens)

```
object level:  does the task, produces output + traces
meta level:    holds a model of the object level (state per item: judged mastery, difficulty, cost so far)
monitor():     object -> meta   (read a signal: FOK before, JOL after, confidence on output)
control():     meta -> object   (start / continue / stop / change strategy / output or withhold)
```

For our agent the object level is the model, the meta level is code. The monitor is a signal from the model (verbalised number, sample agreement, probability) or from code (check result). The control is code that reads the signal.

### 4.2 Pre-solve and post-solve monitors (Cao 2026 harness, c01 to c04)

- Before solving: ask the model for a feeling of knowing (FOK), a number 0 to 1.
- After solving: ask for a judgment of learning (JOL) about the answer just produced.
- A small calibrated controller (an SVM in the paper) turns FOK and JOL into one score, and a rule sets how many attempts to allow.
- Mean attempts fall from low to high confidence. Retries do not see the full earlier reasoning (full previous context: 40.0 vs full harness 47.0 on 100 items, K = 3.09 vs 2.58).
- Ablation on 100 items (Pass@1 44.0, Oracle@4 53.0): full 47.0 [37, 57]; no FOK 45.0; no JOL 42.0; random retry at same K 45.7. All differences sit inside the confidence interval, so they are directional only (critique).
- Calibration is a precondition. Only Sonnet 4.6 of nine models passed every discrimination and calibration check (c04).

### 4.3 Study termination (Fig. 4) as a retry rule

```
state: judged_mastery m (from latest monitor), norm n (target)
loop: act; m = monitor(); if m >= n: stop else continue
```
The human data say a pure criterion rule is wrong. People stop on low rate of progress (a26). Implement as:
```
gain = m_t - m_(t-1)
stop if gain < eps  or  budget_left < cost_of_next
```
Callaway's version: continue iff expected value of another attempt > its cost (a31).

### 4.4 Retrieval termination as search/attempt control

- Fast preliminary FOK: decide at the gate whether to search at all (a06, a16). In code: a cheap difficulty estimate at S0 decides mode.
- Ongoing FOK: during multi-attempt search, track a progress signal and quit when it flattens.

### 4.5 Output control (Koriat and Goldsmith)

```
for each candidate answer a: p = monitor(a)
output a iff p >= t           # t set by payoff: wrong answer costs t/(1-t) times a right one (Kalai et al.)
else: withhold, or give coarser answer (grain control)
```
Value depends on resolution. If AUROC of p is near 0.5, withholding only cuts quantity (a27, a29). Measure resolution before turning this on.

### 4.6 Region of Proximal Learning allocation

```
drop items with high judged mastery
rank the rest from nearly-known to hard
spend effort in that order; stop each when judged progress rate < eps
```
In agent terms: do not retry items the monitor says are solved; among the rest, prefer the ones where one more attempt has the best expected gain.

### 4.7 Timing of the monitor (delayed JOL)

Immediate judgments reflect what is still active; delayed judgments reflect what can be retrieved. Implement as: score the answer after a fresh re-read of the trace in a new context, or after unrelated work. No LLM test exists (d17), so this is a test, not an addition.

### 4.8 Monitor health check (Cacioli, d13, d14)

Cheap online indices: ceiling rate (share of answers at max confidence), variance of confidence, correlation of confidence with correctness on a rolling window. Invalid models: KEEP-correctness r = -.20 vs +.18 for valid ones (d = 2.17, 20 models). Small 3 to 9B models: ceiling rate 91.7%. Switch the gate off when the indices trip.

### 4.9 Step-level monitor and repair (Tyen)

Monitor: find the earliest faulty step. Control: backtrack to it and regenerate. The control half is strong (+18 to +44 points with true location); the monitor half varies by model (ProcessBench F1 61.9 to 87.9). Use code to locate the failing step where a check allows it (this is the schema's G2).

## 5. What holds up

### 5.1 Replications and agreement

- **Held across many labs:** the object/meta split as a modelling frame; FOK and JOL predict outcomes above chance; the delayed-JOL effect (a meta-analysis with g = 0.93 on relative accuracy, but g = 0.08 on memory); the finding that cue use, not direct trace reading, drives monitoring (Koriat 1997, No-Magic).
- **Held for LLMs from independent groups:** intrinsic self-correction does not help without an outside signal (Huang 2024, Kamoi 2024 survey; b14, c22, c24, d21); agreement-based stopping saves samples (Aggarwal 2023, Li 2024); difficulty-aware compute allocation beats uniform best-of-N (Snell 2024, Damani 2024).

### 5.2 Failures, nulls, and contradictions

- **No independent replication of the two key 2026 LLM preprints** (Cao 2026: 3 citing papers, none a replication; Cacioli battery: 4 citing papers, 3 by the same author) (d18). Treat as hypotheses.
- **Verbal confidence: contested.** Xiong 2024 finds it weak (GPT-4 AUROC 62.7%). Tian 2023 finds it better calibrated than token probability for RLHF models. Later work finds strong verbal AUROC on easy facts (.956, .937; d02) and in reasoning models (maths AUROC 71.3 rising to 81.4 with samples; d01). The verdict depends on model, task, and prompt wording. Deeper reasoning also raises overconfidence in some models (d09) and improves calibration along the trace in others (d11: better in 33 of 36 settings).
- **Self-correction: contested.** Madaan 2023 (Self-Refine) reports about 20% absolute gains on preference tasks and up to 13% in code (c25); Huang 2024 and Kamoi 2024 find no reliable gain on general reasoning without oracle signals. The difference is task type and the strength of the first prompt.
- **Cao 2026 vs Cacioli 2026.** Cao finds the model's confidence useful; Cacioli finds most of 20 models cannot report usable confidence. Both fit if the monitor is gated per model: Cao found only one of nine models passed.
- **Grain size:** a social-feedback extension showed no effect (b22).
- **Practice does not improve FOK** (a19).

### 5.3 Moderators and boundary conditions

- **Learning state.** FOK accuracy collapses after overlearning (a08, a09).
- **Item type.** On deceptive items, withholding helps little (a29).
- **Model family and size.** No single scaling law: withdraw delta rises with size in GPT-5.4 (+17.1 nano to +27.7 full), falls in Qwen (+30.1 for 80B to +11.2 for 480B), flat in Gemma (b04, c10).
- **Domain.** Sonnet 4.6 withdraw delta ranges from +8.3% to +93.0% across tasks. Formal reasoning (.658) and natural science (.652) are hardest to monitor (d12).
- **Reasoning models.** DeepSeek R1 withdrew 91 to 99% of items, regardless of correctness (b05, c11). AbstentionBench: reasoning fine-tuning cut abstention by 24% (d08).
- **Prompt wording.** Equivalent confidence prompts change scores by .043 to .084 and flip 4 to 9% of threshold decisions (d02); marker words moved accuracy by up to 80% (d22).
- **Shared misconceptions.** Agreement stops can be fooled: 4 of 9 DeepSeek errors and 2 of 8 Sonnet errors had unanimous 3-sample support (d02).
- **Surface cues.** Longer explanations raise human trust without raising accuracy (d23). Trace length correlated with confidence (beta -.36) in one small model (d14). No cue-stripped test of an LLM's own confidence exists.

### 5.4 Interventions that worked

- Delayed judgment (humans): large monitoring gain (a20, b17).
- Keyword generation after a delay (humans): better monitoring and regulation (a22).
- Free report with accuracy incentive, when resolution is good (a28, a29).
- Code control with a calibrated controller on FOK/JOL (Sonnet 4.6 only; +8.6 pooled) (a34).
- Difficulty-based allocation (d05, d06) and agreement-based stopping (d03, d04).
- Oracle error location plus backtracking (+18 to +44) (c23).
- Training: Self-RAG reflection tokens and uncertainty probes (c26, c18). Out of scope for a scaffold.
- Hybrid monitor: verbalised confidence plus one extra sample, for reasoning models (d01).

### 5.5 Interventions that did not work

- Plain feedback or practice on FOK (a19).
- Giving more study time to items judged known (a15).
- Intrinsic self-revision with no signal (b14, c22).
- Max-JOL or last-answer selection among attempts (b09, c05).
- Full previous reasoning in the retry context (40.0 vs 47.0 on 100 items; c03).
- Fine-tuning a small model to verbalise confidence from sample agreement: first version failed (AUROC2 .554 to .509, accuracy down 7.6 points) (d15).
- Categorical 10-class confidence elicitation in small models: accuracy fell below 5% in 6 of 7 (d14).
- Introspection (re-reading own trace) for Claude 3.7 Sonnet: calibration got worse (d09).

## 6. Language models

### 6.1 Do they have a monitor?

Yes, partly, and it varies.
- **Early large models.** Kadavath 2022 (52B): well calibrated on multiple-choice and true/false when formatted right; P(IK) AUROC .864 on TriviaQA but .624 on GSM8K when trained on TriviaQA alone; P(IK) rose from 18% to 78% with relevant source text; transfer was partial (a32, b12, c14, c15).
- **Black-box verbal confidence.** Xiong 2024: GPT-4 average AUROC 62.7% over eight tasks; GPT-3/3.5/Vicuna ECE above .377. More samples raised performance then levelled off (b13, b26).
- **RLHF chat models.** Tian 2023: asked-for verbal confidence cut ECE about 50% relative to token probability (c17).
- **Reasoning models.** VC AUROC maths 71.3 (K=1) to 81.4 (K=8); hybrid at K=2 gives 84.2 (d01). Calibration rises along the trace in 33 of 36 settings (d11) but self-reported confidence is often above 85% even on wrong answers (d09).
- **Frontier models, 2026.** Cao: Sonnet 4.6 FOK AUROC .612, JOL .745, joint .757, ECE .087 (c04). Cacioli: only 3 of 20 models answered any adversarial foil correctly and 17 of 20 kept everything (c11).
- **Behavioural tests.** In the Delegate Game only one model beat the best of self-or-teammate (+5.4 GPQA, +8.6 Simple MC) (c19). Self-modelling is rarer than confidence assessment (c20).
- **JOL tasks.** GPT-3.5-turbo, GPT-4-turbo, GPT-4o did not predict their own later memory (d16).
- **White box.** Llama 3 and Qwen 2.5 can report and shift activations along a low-dimensional subspace after in-context examples (c21). Not usable by an API agent.

### 6.2 Do they act on it?

Mostly not by themselves. Cao 2026: confidence predicts correctness but reasoning length does not rise on low-confidence items (b07, c06). Retrospective monitoring and prospective regulation correlate r = .17 across 20 models (b03).

### 6.3 What changed it, and by how much

| Change | Effect | Source |
|---|---|---|
| Code-side retry gated on FOK + JOL (Sonnet 4.6) | +8.6 pass@1 pooled; low-JOL group 0.16 to 0.42; high group 0.67 to 0.64 | b06, b08 |
| Cheaper rivals in same table | Self-Refine 52.4 ($0.45); Budget Forcing 51.5 ($0.67); Verifier Reranking 49.8 ($1.32); Aggregator 53.7 ($1.42); Harness 56.9 ($0.78, 2.4 attempts) | c02 |
| Sampling + consistency instead of verbal | GSM8K AUROC 54.8 to 92.7 (GPT-3.5) | c16 |
| One extra sample plus verbal confidence | Maths AUROC 84.2 at K=2 | d01 |
| Oracle label for stopping self-correction | GPT-4 GSM8K 95.5 to 97.5 | c22 |
| Intrinsic self-correction | GPT-3.5 CSQA 75.8 to 41.8; GPT-4 GSM8K 95.5 to 89.0 | c22 |
| Oracle error location | +18 to +44 on originally wrong traces | c23 |
| Agreement stopping | 3.3x fewer samples on maths at 0.1% loss | d03 |
| Difficulty-aware allocation | ~4x less compute (Snell); up to 50% less (Damani) | d05, d06 |
| Meta controller (agentic) | ProgramBench 71.5% vs 58.0% Codex with GPT-5.5; other benchmarks +3.6 to +4.2; overhead hurts at small budgets | d19 |
| Training (probe, Self-RAG) | Beats prompted baselines | c18, c26 |

Reading: gains come when control is in code, uses an external or calibrated signal, and is aimed at doubted items. Gains vanish when the model both monitors and controls itself in one prompt without a signal.

### 6.4 Cost warning

Cao's harness is compared at "matched or lower cost", not at equal tokens against best-of-N. Self-Refine (+4.0 at $0.45) and Budget Forcing (+3.2 at $0.67) were cheaper than the harness (+8.6 at $0.78). The ablation (100 items) has a CI of [37, 57], so small differences are noise.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Revise only when an outside signal (a check, a located failing output) says so. Never let the model judge and fix its own answer in one unaided pass. Already G2 and G10; this confirms them. | G2, G10, S5 | [E] | b14, c22, c24, d21; K05 |
| 2 | Keep monitor and controller separate: code decides, model reports. Monitoring alone is a spy; control without a monitor is blind. | S6 | [E] | a01, a02, c06; K01 |
| 3 | Stop retries on low marginal gain, or on agreement across a window, not on a fixed K or a mastery threshold. | S6 stop | [E] | a26, a25, d03, d04; K15, K29 |
| 4 | Spend retries by estimated difficulty, not uniformly (already G12). | G12, S0 | [E] | d05, d06; K30 |
| 5 | Do not spend extra retries on items already judged solved by a valid check. The "more time on known" rule hurt (56.7 vs 63.9 to 64.5). | S6 gate | [E] | a15, a25; K14 |
| 6 | Do not trust a monitor on cases where it has no resolution; withholding only helps with resolution. Measure before use. | S6, abstain | [E] | a27, a29; K16 |
| 7 | The monitor judges from cues (length, fluency, wording), not from direct reading. Treat its output as a noisy cue and freeze one prompt. | S6 | [E] | a13, a30, d02, d22; K18, K32 |
| 8 | Do not expect the monitor to improve by use or feedback. Calibrate it externally. | S6 | [S] but consistent | a19; K19 |
| 9 | Keep abstention out of the first pass (G6 stays). Where an abstain option is tested, decide it in code. | G6 | [E] for G6 | d08; K36 |

Note: items 1 and 4 already exist in the schema. They are listed because this subfield adds confirmation, not new rules.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-side gate on model-reported FOK/JOL, retries only on doubted items, versus best-of-N and Self-Refine at equal tokens. | S6, O-retry | [S] | a34, b06, b08, c02; K02, K03, K30 |
| T2 | Choose the monitor per model and domain: verbalised, sample agreement, hybrid (verbal + 1 sample), or code check. | S6 monitor | [C] | b13, c17, d01, d02; K07, K08, K31 |
| T3 | Attempt selection by a trace-reading verifier rather than max-confidence. | O-select | [S] | b09, c05; K04 |
| T4 | Delayed or re-read monitoring (judge after fresh re-read or a gap). | S6 timing | [S], human-only [E] | a20, b17, a22; K12, K13, K28 |
| T5 | Monitor health check online (ceiling rate, variance, confidence-correctness correlation) that switches the gate off. | S6 | [S] | d13, d14; K33 |
| T6 | Abstain with an accuracy payoff, decision in code, accuracy-quantity curve. | abstain | [S] | a29, d07, d08; K16, K36 |
| T7 | Step-location monitor plus repair at the located step. | S5/S6 | [S] | c23, d20; K06 |
| T8 | Expected-gain or Region of Proximal Learning stopping versus fixed K. | S6 stop | [S] | a31, a25, a26; K15, K20 |
| T9 | Cue-stripped items to see whether the monitor tracks surface features. | S6 validity | [S] | d14, d23; K34 |
| T10 | Grain control: allow a coarser answer when fine confidence is low. | output control | [C] | b20, b22; K17 |
| T11 | Behavioural monitor probes (delegate, change-answer) beside self-report. | S6 | [S] | c19, c20; K21 |

## 8. Concrete tests on our bench

All tests use the same items for both arms and equal total tokens per item, including the monitor's own tokens and setup. Report accuracy by confidence bucket, not only overall. Run three seeds. Treat gains under about 3 points on 100 items as noise (Cao's CI was [37, 57]).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 gate | Mixed set where the plain pass rate is 30 to 70% (ARC-style, BrainTeaser, a math set) | A: plain, one attempt with leftover tokens as best-of-N. B: Self-Refine with a check-free prompt. C: gate on FOK+JOL, retry only below threshold. D: gate by difficulty class from S0 (no model confidence) | Accuracy at fixed tokens; gain per confidence bucket | C over A by 3 to 8 points on the low bucket, about 0 on the high bucket. If D matches C, drop the model-confidence gate |
| T2 monitor choice | Same items | Monitors: verbal, 2-sample agreement, verbal plus 1 sample, code check | AUROC per domain, equal tokens (count extra samples) | Hybrid best on reasoning items; verbal best on easy facts; agreement best on arithmetic |
| T3 selection | Items with several attempts | Max-confidence vs last vs trace-reading verifier vs code vote | Accuracy of the chosen answer | Verifier or code vote over max-confidence |
| T4 timing | Items with stored answers | Monitor at: immediate, after fresh re-read in a new context, after a gap | AUROC and calibration | Re-read gives higher AUROC (unknown; human effect g = 0.93) |
| T5 health | Rolling window of 50 items | Gate with and without health switch | Accuracy when the monitor goes bad (inject a format change) | Switch avoids losses on invalid windows |
| T6 abstain | Set with 20% unanswerable items | Never abstain; abstain at t = 0.5, 0.75, 0.9 with penalty t/(1-t), decided in code | Accuracy-quantity curve; payoff | Accuracy rises with t at a quantity cost only if monitor AUROC above about 0.7 |
| T7 step repair | Multi-step traces | Regenerate from scratch; revise whole trace; backtrack to monitor-located step; backtrack to code-located step | Accuracy at equal tokens | Code-located best; monitor-located helps only if step F1 above about 70 |
| T8 stopping | Retry tasks | Fixed K; stop on window agreement; stop on gain below eps; expected-gain | Accuracy at fixed tokens; tokens used | Agreement and gain stops save 30%+ tokens at under 1 point loss |
| T9 cue strip | Pairs differing in length or fluency, same content | Confidence on short vs long | Confidence shift vs correctness shift | If confidence shifts by more than 0.1 with no change in correctness, the monitor is cue-driven |
| T10 grain | Estimation tasks | Fine only vs allow coarse | Accuracy per answer, informativeness | Small gain; low priority |
| T11 behavioural | Items with delegate option | Self-report vs delegate or change-answer probe | AUROC of each | Behavioural probe not worse than report |

## 9. What does not transfer, and why

- **Human numbers are on word pairs and general-knowledge questions** (1970s to 1990s, N of 10 to 71 per cell). They give structure, not effect sizes for LLM reasoning (critique).
- **Memory-trace talk.** FOK is about what is stored; a model has no episodic acquisition history to read. The nearest equivalent is the prompt and the log, which code can read better than the model can (No-Magic: monitoring is cue-based anyway).
- **Study-time allocation.** Humans have fixed time; our agent has a token budget and can parallelise. The rate-of-progress stopping rule transfers; the time limits do not.
- **Delayed JOL.** The mechanism depends on short-term vs long-term memory. A model has no such gap. A fresh-context re-read is only an analogue. The only LLM JOL study was negative (d16).
- **Privileged access.** Humans beat an outsider modestly. For an LLM, a separate model or code may monitor as well or better. Kadavath found models predicted their own P(IK) only slightly better than another model's (c15).
- **Training-based monitors** (Self-RAG, probes, activation steering, distillation) are out of scope for a scaffold (c18, c21, c26).
- **Model-reported confidence at scale.** Most frontier models in Cacioli's battery keep and bet on everything (b02). A design that relies on verbalised FOK needs a per-model validity check.
- **Reasoning-model overconfidence and low abstention** (d08, d09) mean the human-style "I don't know" control is weaker; put the abstain rule in code.
- **Formal MGV architecture** has no experiments (b11); use as a design guide only.
- **Self-Refine style loops** gain on style tasks; they do not transfer to reasoning without external signals (c24, b14).

## 10. Open questions

1. Does the gated retry loop beat best-of-N and Self-Refine at equal tokens, and on which confidence bucket? (Only Cao tests it; no equal-token comparison; no replication; d18.)
2. Which monitor wins per model and domain? No source compares a trace-reading verifier or a code check to verbalised and agreement monitors at equal tokens.
3. Does delayed or re-read monitoring help an LLM? No test exists (d17).
4. Which stopping rule is best: fixed K, rate of progress, expected value? Only agreement stops have LLM tests.
5. Does the monitor degrade under domain shift or format change, and can we detect it online? (One author, indices tuned on the same models; d13.)
6. Is LLM confidence driven by surface cues? No cue-stripped test.
7. How large is the loss on the high-confidence bucket (0.67 to 0.64 in Cao)? Can a code gate prevent it?
8. Do the Cao and Cacioli results replicate on other labs and open models?
9. Can the monitor find the faulty step well enough that location-guided repair pays off at equal tokens?
10. What is the accuracy-quantity curve for an LLM with an abstain payoff? Kalai et al. give a design but no measured curve (d07).
11. Does a high-ability model that is a poor monitor (GLM-5: 1st accuracy, 9th monitoring) hurt a gated design that relies on its self-report?
12. Why does introspection help some reasoning models and hurt Claude 3.7 Sonnet (d09)? Does it hold for the model we use?

## 11. Sources

[V] = opened and read this session (full text or at least the abstract and the relevant sections). [M] = snippet or second-hand only.

**Human metamemory**
- [V] Nelson and Narens (1990) Metamemory: a theoretical framework and new findings. https://sites.socsci.uci.edu/~lnarens/1990/Nelson&Narens_Book_Chapter_1990.pdf (a01-a19)
- [V] Dunlosky and Nelson (1994) Does the sensitivity of judgments of learning (JOLs) to the effects of various activities depend on when JOLs occur? https://www.gwern.net/docs/spaced-repetition/1994-dunlosky.pdf (a20)
- [M] Nelson and Dunlosky (1991) When people's judgments of learning are extremely accurate at predicting subsequent recall. https://doi.org/10.1111/j.1467-9280.1991.tb00147.x (a21)
- [V] Thiede, Anderson and Therriault (2003) Accuracy of metacognitive monitoring affects learning of texts. https://wp.stolaf.edu/cila/files/2012/11/thiede_jedp.pdf (a22, b16)
- [V] Metcalfe and Kornell (2003) The dynamics of learning and allocation of study time to a region of proximal learning. https://psychology.columbia.edu/sites/psychology.columbia.edu/files/2016-11/530.pdf (a23, a24)
- [V] Metcalfe and Kornell (2005) A Region of Proximal Learning model of study time allocation. https://psychology.columbia.edu/sites/default/files/2016-11/Metcalfe.Kornell.2005.pdf (a25, a26, b15)
- [V] Koriat and Goldsmith (1996) Monitoring and control processes in the strategic regulation of memory accuracy. https://newiipdm.haifa.ac.il/wp-content/uploads/2015/05/Koriat-Goldsmith-1996-Psych-Rev.pdf (a27-a29)
- [M] Koriat and Goldsmith (1996), numbers via another read (b21)
- [V] Koriat (1997) Monitoring one's own knowledge during study: a cue-utilization approach. https://newiipdm.haifa.ac.il/wp-content/uploads/2015/05/1997-Koriat-CueUtilization.pdf (a30)
- [V] Goldsmith, Koriat and Weinberg-Eliezer (2002) Strategic regulation of grain size in memory reporting. https://newiipdm.haifa.ac.il/wp-content/uploads/2015/05/Goldsmith-et-al-2002-JEP-General.pdf (b20)
- [V] Rechdan et al. (2017) Computer mediated social comparative feedback does not change confidence or grain size. https://doi.org/10.3389/fpsyg.2017.01433 (b22)
- [V] Finn (2008) Framing effects on metacognitive monitoring and control. https://doi.org/10.3758/MC.36.4.813 (b18)
- [M] Metcalfe and Finn (2008), as described in Finn (2008). https://doi.org/10.3758/MC.36.4.813 (b19)
- [M] Mazzoni and Cornoldi (1993) When can people allocate study time effectively (labor in vain). https://doi.org/10.1037/0096-3445.122.1.47 (a35, b23)
- [M] Rhodes and Tauber (2011) The influence of delaying judgments of learning on metacognitive accuracy: a meta-analytic review. https://doi.org/10.1037/a0021705 (a36, b17)
- [M] Undorf and Ackerman (2017) The puzzle of study time allocation for the most challenging video clips. https://cris.haifa.ac.il/en/publications/the-puzzle-of-study-time-allocation-for (b24)
- [V] Callaway, Griffiths, Norman and Zhang (2023) Optimal metacognitive control of memory recall. https://cocosci.princeton.edu/papers/callaway2023optimal.pdf (a31)
- [M] Callaway et al. (2024) as cited in MGV. https://arxiv.org/abs/2511.04341 (b25, c28)
- [M] Cox (2005) Metacognition in computation: a selected research review (c29)

**LLM monitoring and control**
- [V] Cao et al. (2026) LLMs know when they know, but do not act on it: a metacognitive harness. https://arxiv.org/abs/2605.14186 (a34, b06-b10, c01-c06)
- [V] Cacioli (2026) The Metacognitive Monitoring Battery. https://arxiv.org/abs/2604.15702 (b01-b05, c07-c11)
- [V] Cacioli (2026) Domain-level metacognitive monitoring in frontier LLMs. https://arxiv.org/abs/2605.06673 (d12)
- [V] Cacioli (2026) Before you interpret the profile: validity scaling. https://arxiv.org/abs/2604.17707 (d13)
- [V] Cacioli (2026) Verbal confidence saturation in 3-9B open-weight models. https://arxiv.org/abs/2604.22215 (d14)
- [V] Cacioli (2026) Distilling self-consistency into verbal confidence. https://arxiv.org/abs/2604.24070 (d15)
- [V] Oh and Gobet (2025) Monitor-Generate-Verify. https://arxiv.org/abs/2511.04341 (a33, b11, c12, c13)
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (a32, b12, b27, c14, c15)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (b13, b26, c16)
- [V] Tian et al. (2023) Just ask for calibration. https://arxiv.org/abs/2305.14975 (c17)
- [V] Kapoor et al. (2024) Large language models must be taught to know what they don't know. https://arxiv.org/abs/2406.08391 (c18)
- [V] Ackerman (2026) Evidence for limited metacognition in LLMs. https://arxiv.org/abs/2509.21545 (c19, c20)
- [V] Ji-An et al. (2025) Language models are capable of metacognitive monitoring and control of their internal activations. https://arxiv.org/abs/2505.13763 (c21)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b14, c22)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516 (c23)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (c24, d21)
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (c25)
- [V] Asai et al. (2023) Self-RAG. https://arxiv.org/abs/2310.11511 (c26)
- [V] Yin et al. (2023) Do large language models know what they don't know? https://arxiv.org/abs/2305.18153 (c27)
- [M] Steyvers and Peters (2025) review; Dai (2026) scale-format effect, cited in Cacioli (c30)
- [V] Del et al. (2026) How uncertainty estimation scales with sampling in reasoning models. https://arxiv.org/abs/2603.19118 (d01)
- [V] Meyer et al. (2026) An analysis of training-free self-reported confidence. https://arxiv.org/abs/2609.20541 (d02)
- [V] Aggarwal et al. (2023) Let's sample step by step: Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (d03)
- [V] Li et al. (2024) Escape sky-high cost: early-stopping self-consistency. https://arxiv.org/abs/2401.10480 (d04)
- [V] Damani et al. (2024) Learning how hard to think. https://arxiv.org/abs/2410.04707 (d05)
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 (d06)
- [V] Kalai, Nachum, Vempala and Zhang (2025) Why language models hallucinate. https://arxiv.org/abs/2509.04664 (d07)
- [V] Kirichenko et al. (2025) AbstentionBench. https://arxiv.org/abs/2506.09038 (d08)
- [V] Mei et al. (2025) Reasoning about uncertainty. https://arxiv.org/abs/2506.18183 (d09)
- [V] Zeng et al. (2025) Thinking out loud. https://arxiv.org/abs/2504.06564 (d10)
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489 (d11)
- [V] Huff and Ulakci (2025) Judgments of learning distinguish humans from large language models. https://doi.org/10.1038/s41598-025-22290-x (d16; abstract only)
- [V] Liu et al. (2026) Metacognition in LLMs: foundations, progress, and opportunities. https://arxiv.org/abs/2607.11881 (d17)
- [V] Citation check of Cao 2026 and Cacioli 2026 via Semantic Scholar. https://api.semanticscholar.org/graph/v1/paper/arXiv:2605.14186/citations (d18)
- [V] Dahal et al. (2026) Thinking before thinking. https://arxiv.org/abs/2609.38147 (d19)
- [V] Zheng et al. (2024) ProcessBench. https://arxiv.org/abs/2412.06559 (d20)
- [V] Zhou, Jurafsky and Hashimoto (2023) Navigating the grey area. https://arxiv.org/abs/2302.13439 (d22)
- [V] Steyvers et al. (2025) What large language models know and what people think they know. https://arxiv.org/abs/2401.13835 (d23; abstract level)

Links to parallel subfields (not covered here): Metacognition and control; Metacognition of insight; Expected value of sample information; Sampling and voting (self-consistency); Scoring rules and calibration; Exploration versus exploitation; Impasse-driven subgoaling and chunking; Language agents as architectures.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 6 established claims: 5 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A04.01-K18** (reworded: the sources support less). Numbers verified (Nelson & Narens Table I: recall .28 vs .10, FOK 5.4 vs 5.2), but the source says FOK misses small amounts of new information from a brief flash, not that it is blind to new information, and Koriat 1997 finds JOLs rely on intrinsic cues like ease while discounting extrinsic ones like repetition (repetition lifted recall more than JOL). Corrected claim: Monitoring cues are inferential, not direct reads: FOK uses acquisition history and partial information (No-Magic Hypothesis), is insensitive to small amounts of new information (a brief answer flash raised recall .28 vs .10 but FOK only 5.4 vs 5.2), and JOLs are built from cues such as item ease (intrinsic cues) and study conditions, with repetition under-weighted relative to its effect on recall.
- **A04.01-K12** (now single-source: only one opened source, code check).
- **A04.01-K14** (now single-source: only one opened source, code check).
- **A04.01-K15** (now single-source: only one opened source, code check).
