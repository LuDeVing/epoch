# Metacognition of insight: deep document

*Subfield B01.05. Source files in this folder: evidence_a.jsonl (a01-a32), evidence_b.jsonl (b01-b28), evidence_c.jsonl (c01-c25), evidence_d.jsonl (d01-d20), claims.jsonl (B01.05-K01 to K28), critique.md. Evidence ids below are those ids. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

*Note on evidence quality. The gap search (evidence_d) ran after the web search quota ran out, so it used arXiv listing pages and a few fetches. A missing paper is not proof that none exists. No LLM study tests human-style warmth ratings by an LLM on insight problems directly. The guardrail rests on analogy. d19 (snippet) and d20 (a search log) are not sources and are not counted as evidence. Hedne 2016 appears under four ids (a09, b03, b04, c12) and counts as one study.*

---

## 1. What it is

Metacognition of insight asks one question. When a person works on an insight problem, can they tell how close they are to the answer?

The classic answer is no. On ordinary step-by-step problems, people feel themselves getting closer. On insight problems they do not. The feeling of "warmth" stays low and flat, then jumps just before the solution (Metcalfe and Wiebe 1987, a01, a02). Feeling-of-knowing ratings given before solving did not predict who would solve an insight problem (gamma .08), while they did predict algebra (gamma .40) (a03).

Three linked questions sit under this:

1. **Warmth.** Does felt closeness rise gradually (continuous) or jump (discontinuous)?
2. **Confidence and Aha.** Does the sudden "Aha!" feeling mean the answer is right? Is it a good signal at all?
3. **False insight.** How often does a strong Aha go with a wrong answer?

Why it matters for our agent. The schema must detect when the agent is stuck (S6) and decide when to rethink. The question is which signal to trust. The human literature says the solver's own sense of progress is a poor signal on insight problems. The LLM literature says the model's own verbal confidence and its own "Wait" or "Aha" shifts are also weak signals, while code-readable signals (token entropy, trace length, checks) work better. That supports guardrail G10 (reasoning text is not evidence) and the S6 rule that code, not the model, detects impasse.

Scope limits. Most human data come from small samples in a few labs. Findings depend on how "insight" is defined: by problem type (Metcalfe and Wiebe) or by the solver's Aha report (Hedne, Danek, Salvi). The two definitions give different answers.

---

## 2. History and theories in depth

### 2.1 The founding studies (1986-1987)

**Metcalfe 1986 (two papers; not opened; a07, a08, b02).** Feeling-of-knowing (FOK) predicted later success on memory questions and on algebra but not on insight problems. In the warmth paper, warmth for correct answers was flat then jumped (as quoted in the 1987 text, on 78 percent of correct solutions warmth rose by no more than 1 point on a 10-point scale across the solving interval). For wrong answers, warmth rose steadily. A sudden feeling of nearness well before an answer tended to mark an error ("premonitions of insight predict impending error"). People also overestimated their ability more on insight problems.

**Metcalfe and Wiebe 1987 (opened; a01-a06).** Two experiments.

- Exp 1: 26 paid volunteers, 19 usable. Five classic insight problems and five multistep problems. Warmth rated every 15 s on a 3 cm scale. Gamma between problem type and incrementalness: angular warmth G = .26, t(18) = 2.02; differential warmth G = .23, t(18) = 1.63 (one-tailed).
- Exp 2: 73 students, algebra as the non-insight class. 48 usable for FOK, 39 for warmth. Warmth G = .35 (t(37) = 3.10) and .32 (t(37) = 2.56).
- FOK gamma: algebra .40, insight .08, F(1,46) = 6.46. Probability estimates: .40 vs .15.
- Calibration: insight predicted .59, actual .34. Algebra predicted .73, actual .55. Interaction F(1,46) = 3.18, one-tailed only.
- The crowd beat the person. Normative difficulty (share of other subjects who solved each problem) gave gamma .77 on insight against .08 for own FOK. On algebra .60 vs .40. Interaction F(1,46) = 10.13.

The authors proposed to define insight by the metacognitive pattern itself: a step-function warmth protocol marks an insight problem for that person (a06). This is circular if warmth is the only test.

### 2.2 Competing process theories

- **Representational change (Ohlsson 1992; a18, not opened).** Impasse triggers spread of activation in memory, which may activate a new representation and produce an Aha. Restructuring is outside conscious control, so the solver cannot see it coming. This predicts flat warmth.
- **Progress monitoring / criterion for satisfactory progress (MacGregor, Ormerod and Chronicle 2001; a17, not opened).** No special insight process. Solvers pick moves that maximise progress with limited lookahead and monitor progress against a criterion. When no move meets it ("criterion failure"), they widen the problem space. Impasse is a criterion check, not a feeling. Chein et al. 2010 support the lookahead part: spatial working memory predicted nine-dot solution (odds ratio 1.16, p = .004; verbal 1.02, p = .52; n = 54) (a16). This is the closest human analogue to our S6: a code-side rule on progress, not a felt signal.
- **Eureka heuristic (Laukkonen et al. 2023; b25, snippet only).** The feeling of insight is a fast metacognitive heuristic that selects which idea reaches awareness. It works when implicit knowledge is sound and fails when it is corrupted.
- **Metacognitive prediction-error account (Becker, Wang and Cabeza 2024; b14).** Aha tracks surprise that the problem turned out solvable, not timing. n = 39, remote associates. Suddenness related negatively.

### 2.3 Critiques and shifts

- **Weisberg 1992 (a14, not opened).** Critique of the warmth method and its analysis.
- **Webb, Little and Cropper 2016 (a19, a20, c13).** "Insight is not in the problem." Insight depends on the solver. Classic insight problems had higher Aha than non-insight problems in all three experiments (10.15 points in Exp 1), but accuracy did not differ (difference .035, p = .81). Aha tracked accuracy inside non-insight problems too (r = .24 Exp 1a, .19 Exp 2). This undermines the problem-type labels used in 1987.
- **Laukkonen and Tangen 2018 (a12, a13, b06).** Warmth-defined and Aha-defined insight agree per person (r = .61, n = 51) but not per problem (r = .08, n = 182). Gradual warmth does not prove no insight: a solver can feel steady progress on a wrong strategy, then switch suddenly.
- **Hedne, Norman and Metcalfe 2016 (a09-a11, b03-b05, b27, c12).** The original group's own re-test with magic tricks.
- **Danek and Wiley 2017, Grimmer et al., Laukkonen et al. 2020.** The "dark side": false insights.
- **Webb, Little and Cropper 2016 as the biggest dataset (d02).** About 400 people over three experiments. It measures post-solution insight ratings, not warmth. Insight rating tracks correctness for insight problems (r = .50, .40, .495 across Exp 1, 1a, 2) and CRAs (.41, .40, .39), and hardly for non-insight problems (.02, .24, .19). It is not a warmth replication.
- **Laukkonen et al. 2022 (d01), the preregistered re-test of spillover.** Same lab as the 2020 original. About 1250 analysed per sample. Effect d = .23 and .25, smaller than the 2020 d = .32. A 10-second delay between the anagram and the statement removes it (6.20 vs 6.02, b = .12, p = .447).

### 2.4 The LLM turn (2022-2026)

- Calibration work (Kadavath 2022; a31) showed larger LMs can estimate P(True) of their own answers, but poorly on new tasks.
- 2023: stumpers and lateral-thinking sets (c10, c11, c17, c18, c22).
- 2025: NazoNazo names "verification failure" (c01-c04); Yang et al. on Aha moments (b19, c07); Self-Correction Bench (c08).
- 2026: d'Aliberti and Ribeiro, "The illusion of insight in reasoning models" (a28, a29, c05, c06), the main direct test of whether LLM "Aha" shifts help and whether code-chosen triggers beat model-chosen ones.
- 2026 (gap search, d03-d18): confidence-signal validity (verbal confidence tracks commitment, not correctness: d03, d04, d05), detector papers on trace dynamics (d06-d09), overthinking and lost correct answers (d10, d11), early stopping and prefix consensus as cheap baselines (d12, d13, d18), and one direct lure study with riddles (Riddle Riddle, d14). None of them uses human-style warmth.

---

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Own FOK does not predict insight solving, does predict algebra | gamma .08 vs .40, F(1,46) = 6.46; probability estimates .15 vs .40 (one-tailed) | Metcalfe and Wiebe 1987 (a03) | [S] (K01); replicates Metcalfe 1986 (second-hand) |
| Crowd difficulty beats own feeling | normative gamma .77 vs own .08 on insight; .60 vs .40 on algebra; F(1,46) = 10.13 | M and W 1987 (a05) | [S] (K01) |
| Overconfidence larger for insight | predicted .59 vs actual .34 (insight); .73 vs .55 (algebra); F(1,46) = 3.18 one-tailed | M and W 1987 (a04) | [S], weak |
| Warmth incremental for non-insight, step-like for insight | Exp 1: G = .26, .23 (N = 19); Exp 2: G = .35, .32 (N = 39) | M and W 1987 (a01, a02) | [C] (K02) |
| Step-like warmth in nine-dot | 25 people, 12 solved; flat for about 3.5 min; group x time F(1,20) = 20.60; last rating t(15) = 7.27 | Chein et al. 2010 (a15) | [S], supports pattern |
| Warmth pattern fails when insight = self-reported Aha | differential warmth 2.92 vs 0.30, t(210) = 0.79, p = .43, d = .12; angular d = .22; N = 51, 971 trials, 29 percent insight | Hedne et al. 2016 (a09, b03) | [S] (K03) |
| Partial support with remote associates | last-step warmth rise 2.59 vs 1.43, t(26) = 4.27, d = .82; interaction F(2,52) = 15.63; N about 36 | Kizilirmak et al. 2018 (b08) | [C] (K05) |
| Warmth and Aha measures agree by person, not by problem | r = .61 (n = 51) vs r = .08 (n = 182); after a warmth jump 75.6 percent reported Aha, after gradual rise 50.8 percent | Laukkonen and Tangen 2018 (a12) | [S] (K04) |
| Insight solutions more accurate and more confident (magic) | .57 vs .37, t(506.9) = 5.78, d = .51; confidence 78.32 vs 68.95, d = .50 | Hedne 2016 (a09, b04) | [S] |
| Confidence tracks correctness only for non-insight | Az insight .56 (vs .5: p = .142); non-insight .64 (p < .001); type difference p = .297 (n = 33) | Hedne 2016 (a10) | [S] (K06), weak: the type difference is not significant |
| Perseveration on wrong insights | chose option like own solution .72 vs .61, d = .23, p = .001; for wrong solutions .63 vs .51, d = .24, p = .017 | Hedne 2016 (b05) | [S] |
| False insights are common | Aha 66.50 vs 52.34, t(69) = 10.21; 37 percent (417 of 1124) of wrong solutions had Aha above the correct mean; N = 70, 35 magic tricks (the abstract says 37, the methods say 35; 2450 trials = 70 x 35, so use 35; the paper is inconsistent), 1778 solutions, 36.8 percent correct | Danek and Wiley 2017 (a21) | [E] (K07) |
| FIAT lures induce false insight | 9.3 percent no false insight; 44.6 percent on at least half of trials; max six per person (quoted from an earlier paper); thinking style and psychosis proneness do not predict | Grimmer et al. 2022 (b11) | [E] (K07) |
| Misleading prime causes intrusion errors | 25 vs 1 and 2; F(2,84) = 15.7; N = 43; FOK 3.05 vs 2.67 after a fast wrong answer | Ammalainen and Moroshkina 2020 (b13) | [S] |
| Aha raises truth ratings of unrelated claims (2020 original) | Aha vs no Aha d = .321 (7.2 vs 6.31); solved vs unsolved d = .609; n = 268 analysed; preregistered | Laukkonen et al. 2020 (b10) | [S] (K09, same lab) |
| Spillover shrinks on re-test and dies with a delay | 7.21 vs 6.35, d = .23 and 7.34 vs 6.52, d = .25 (1250 and 1239 analysed); 10 s delay: 6.20 vs 6.02, p = .447 | Laukkonen et al. 2022 (d01) | [S] (K09), human only |
| Largest insight-monitoring dataset has no warmth | about 400 people; insight-accuracy r: insight problems .50/.40/.495, CRA .41/.40/.39, non-insight .02/.24/.19 | Webb et al. 2016 (d02) | [S] (K26); gap 5 closed as none found |
| Insight more accurate on CRA | 93.7 vs 78.3 percent, t(37) = 5.66, d = .99; last-5-s errors 29.4 vs 4.7 percent; N = 38; same direction in 4 experiments | Salvi et al. 2016 (a23) | [C] (K08) |
| Aha-accuracy depends on convergent vs open task | CRAT within-person OR 1.92 (CI 1.82-2.03); AUT insight vs objective creativity b = .08, between-person n.s.; vs self-rated creativity partial R2 = .17; N = 100 | McGuinness et al. 2026 (b16) | [S], boundary condition |
| Aha tracks drop in perceived difficulty | initial difficulty correct 3.45, wrong 4.63, unsolved 5.54; N = 160 rebus | 2024 rebus study (b15) | [S] |
| Aha reflects surprise at solvability, not suddenness | n = 39, accuracy 51.0 percent | Becker et al. 2024 (b14) | [S] |
| Felt experience varies with item difficulty, not item class | 119 people; easy Raven items feel like insight, hard ones do not | Chuderski et al. 2020 (a24) | [S] |
| LLM: reasoning models beat non-reasoning on insight riddles but trail humans | 7.60 vs 17.59 percent (120-item subset); human 52.9 (CI 46.6-59.2, n = 126); full set 9.42 vs 19.25, OR 2.29 (1.99-2.64); GPT-5 inside the human CI (descriptive, not equivalence) | Mizumoto et al. 2025 (a25, c01) | [S] (K13); the d = .946 in a25 is unverified |
| LLM: verification failure | gold answer in the log but not endorsed: Gemini 2.5 Flash 5.23 percent (9 cases), Claude Opus 4 25.00 (35), DeepSeek-R1 30.57 (48), Grok 4 39.34 (48) of wrong answers | Mizumoto 2025 (c02) | [S] (K11) |
| LLM: false "Oh! I've got it" | more than 100 such phrases in Claude Opus 4 logs; correct outcomes rare | Mizumoto 2025 (a27) | [S] (K12) |
| LLM: spontaneous shifts are rare and hurt | 6.31 percent pooled (about 7.6 for Qwen-1.5B); 2.57 vs 16.44 percent correct with vs without a shift (N = 723,200); formal Aha 1.79 percent; GPT-4o 0.88-2.21 percent; DeepSeek-R1 0.00-0.25 percent | d'Aliberti and Ribeiro 2026 (a28, c05) | [E] (K14), 3 reports but one paper family |
| LLM: riddle form is a lure | 9 frontier LLMs, 30 matched sets: genuine riddles 84.9 vs riddle-form items with literal answer 50.7 percent; humans 50.5 vs 80.5 (permissive coding); 90.8 percent of LLM errors over-inventive; judge-coder kappa .90-.93 | Fascendini et al. 2026 (d14) | [S] (K22) |
| LLM: lose a correct answer by continuing | oracle stop at best point +8 percent accuracy, 72 percent fewer thinking tokens; first-correct-prefix stop beats default by about 10 percent (up to 21); harmful overthinking .11 multiple choice vs .24 free-form; plain early stop raises harm 10.1 to 18.4 (K=5) | Song 2026 ThinkBrake (d10); Caldarella 2026 (d11) | [E] (K23), math only |
| LLM: model-chosen doubt is mostly unneeded | precision 24.4 percent; code-injected minimal doubt cue recovers about 15 percent of failed rollouts (Qwen3-8B/14B-Base; AIME24, AMC23, MATH500) | Kim et al. 2026 (d15) | [S] (K24) |
| LLM: no ranking of impasse detectors | AUROC GSM8K 0.73-0.81 but ProntoQA 0.52-0.80 (d07); instability 0.66-0.74, 0.605 in first 50 steps (d08); repetition 0.80-0.91 full trace, 0.51-0.57 before the answer (d06); length baselines absorb gains (d09) | Grunefeld; Chen; Sourav; Song 2026 | [unresolved] (K25) |
| LLM: verbal confidence reflects commitment | residual verbal AUROC .473 (p = .844) vs residual log-prob .686 (p = .0039); verbal AUROC .51-.68 vs calibrated log-prob .62-.80 (4 non-reasoning models) | Kumaran 2026 (d03) | [S] (K27) |
| LLM: verbal confidence is unstable and clusters near base rate | N = 842; resolution verbal .0316 vs sampling consensus .0637 (2.02x); Brier .1713 vs .1465; consensus costs about 10x inference; 0.5B-7.6B models | Ghosh 2026 (d04) | [S] (K17, K27) |
| LLM: verbal confidence is blind to the trajectory | 78.5 percent of items change confidence by under .02 after cutting hesitation (one VLM) | Yang 2026 (d05) | [S] (K17) |
| LLM: cheap voting baselines | prefix consensus matches or beats SC at up to 60 percent fewer tokens; neuron agreement cuts tokens 99 percent; confidence-dynamics stop cuts tokens 25-50 percent at similar accuracy | d13, d18, d12 | [S] (K28), math only |
| LLM: creative puzzles harder than factual ones | gap up to 17 percent; models retrieve facts but fail to connect them; reasoning effort 9.4 to 17.8 percent (one model, English) | CresOWLve 2026 (d17) | [S] (K20) |
| LLM: shifts hurt on MATH-500, help on cryptic crosswords | with vs without shift: Qwen-7B 28.2 vs 66.1; GPT-4o 33.8 vs 65.8; R1 20.4 vs 54.3; Llama-8B 28.2 vs 45.7; crosswords 20.1 vs 9.6 | c05 | [S] |
| LLM: externally triggered reconsideration helps | MATH-500 32.21 to 40.62 (+8.41 pp); 50,574 wrong-to-right vs 23,500 right-to-wrong; crosswords +0.45; Rush Hour +0.01; intrinsic shifts -7.40 pp in top-20 percent entropy traces vs -22.88 pp at low entropy | a29, c06 | [E] (K15), single small model |
| LLM: self-correction blind spot | 14 open models; average 64.5 percent blind spot; appended "Wait" cut it 89.3 percent and raised accuracy 156.0 percent (relative) | Tsui 2025 (c08) | [E] (K16) |
| LLM: verbal confidence tracks commitment, not correctness | residual verbal confidence AUROC .473 (p = .844); residual log-prob .686 | b22 | [C] (K17) |
| LLM: solving and rating in one prompt corrupts confidence | cosine of confidence and accuracy directions +0.26 pure vs -0.63 joint; verbalised ECE 14.9/35.1/36.0 to 3.7/3.3/10.7 with steering (7-8B models) | Miao and Ungar 2026 (c15) | [S] |
| LLM: larger LMs can predict P(True) | 52B model well calibrated on MC and true/false; P(IK) poor out of distribution | Kadavath 2022 (a31) | [E] (K18) |
| LLM: trace length is an uncertainty signal | complements verbalised confidence; survives difficulty controls | b21 | [E] (K19), AUROC values not extracted |
| LLM: stumpers, solve better than verify | humans 38.15 percent (n = 81); GPT-3.5/4 57.8 original, 43.4 enhanced; two-option verification: humans 100 percent when they could solve, 63.8 when not; most models below chance (mean 41) | EMNLP Findings 2023 (c10) | [S] (K20) |
| LLM: red-herring fixation | removing herrings raises scores | Only Connect Wall (c11) | [S] (K20) |
| LLM: metacognitive prompting beats CoT on lateral thinking | GPT-3.5: +5.00, +10.07, +6.48, +2.65 | Bai et al. 2025 (c21) | [C] (K21), snippet only |
| VLM self-verification no better than voting | Aha in 8.3 percent of responses; best-of-N self-verification down by up to 16.7 percent; majority vote +4.5 percent on GeoQA | Wu et al. 2026 (a30) | [S] |

---

## 4. Mechanisms and models

Each mechanism is explained so an engineer can implement it or its code-side replacement.

### 4.1 Why human warmth is uninformative on insight problems

Model: the solver holds a representation of the problem. In a wrong representation, partial progress is measured against a criterion unrelated to real solution distance. Warmth reflects progress inside the wrong frame, so it carries no information about real distance (Ohlsson's account). When the representation shifts, everything becomes visible at once, so warmth jumps. Alternative (continuous account, Kizilirmak b08): the solver does feel gradual progress but reports it only above an awareness threshold.

Engineer's reading. A signal that measures progress inside a frame cannot detect that the frame is wrong. An agent's self-rated progress has the same weakness. Use a signal from outside the frame: sibling-sample pass rate, checks, entropy.

### 4.2 The crowd statistic (normative difficulty)

Method: for each item, the share of other solvers who solved it. Gamma with individual success: .77 on insight problems (a05). Implementation: keep a per-class and per-item pass rate in the class record (SCHEMA memory). In the agent, the equivalent is the pass rate of sibling samples at S3, or the class pass rate from S0. It is a cheap estimate of difficulty that does not depend on the solver's feeling. Caveat: the 1987 version included the person in the computed rate (each subject contributed 2.1 percent), a small inflation (a05).

### 4.3 Criterion-for-satisfactory-progress as a code rule

Algorithm: at each step compute a numeric progress measure (goal units reached versus steps used). Compare with a criterion (rate needed to finish within the step budget). If no available move meets it, declare criterion failure and widen the move set (try a new operator). The SCHEMA S6 triggers have the same shape: no pass, two rounds without change, same error twice, budget fraction spent. Source: a17 (second-hand), a15, a16.

### 4.4 Aha as a heuristic with spillover

Model (b25, b10, b16): the sudden feeling raises the weight of the idea just reached, and of nearby ideas. Measured: Aha vs no Aha raises truth ratings of unrelated statements by d = .321 (b10); insight inflates self-rated creativity far more than objective creativity (b16). Implementation: treat any felt certainty after a reframe as a bias to cancel, not as evidence. For an agent with long contexts, reset context between items or candidates so the effect cannot carry.

### 4.5 Metacognitive accuracy (Az, area under the confidence ROC)

Definition: the probability that a randomly chosen correct answer got higher confidence than a randomly chosen wrong one. 0.5 is chance. Hedne found .56 for insight and .64 for non-insight (a10). The same measure is the right way to test any agent signal. Implementation: per item record (signal, correct), compute AUROC per item type. Use it in every section 8 test.

### 4.6 Verification failure and false insight in LLMs

Verification failure (c02): scan the thought log for a literal match of the correct candidate. If it appears and the final answer differs, count one failure. Rate = such cases / wrong answers. Code-side fix: harvest all candidates raised in the trace (SCHEMA S4 harvest) and test each by a check, so a correct candidate the model did not endorse is still caught. It needs a code-runnable check. Without one, the harvest has nothing to choose with.

False insight (c03): the model commits to a wrong reinterpretation and stops. No rate has been measured. Fix: independent verification on something the answer was not fitted to (G3).

### 4.7 Entropy-gated reconsideration (d'Aliberti and Ribeiro)

Algorithm (a29, c06):
1. During decoding, track token entropy at each step.
2. Flag the trace when entropy is in the top 20 percent of the historical distribution.
3. At the flag, append a reconsideration cue ("Wait"-style continuation).
4. Continue decoding.

Result: MATH-500 32.21 to 40.62 percent for Qwen2.5-1.5B (+8.41 pp); 50,574 wrong-to-right vs 23,500 right-to-wrong. Spontaneous shifts at the same entropy level did not help (-7.40 pp in the top 20 percent of entropy traces, -22.88 pp in low-entropy traces). Near zero on crosswords (+0.45) and Rush Hour (+0.01), where the base rate is small. So the trigger must come from code, and the gain needs a foothold (consistent with G12).

Caveat from the gap search. The whole gain is against no gate on a 1.5B model. Cheaper rivals exist: prefix consensus matches self-consistency at up to 60 percent fewer tokens (d13), and confidence-dynamics stopping cuts 25-50 percent of tokens (d12). A gate has to beat those, not plain voting (K28). Protocol warning: a snippet (d19, unopened) says entropy verifiers that look like AUROC 0.80+ fall to 0.60-0.75 under within-problem evaluation. Treat any entropy AUROC as inflated until we measure it per problem.

Related detectors: GUARD (c19: errors start at a few early token-entropy spikes); ASAG (c20: attention-state early stop, +3.2 percent accuracy and nearly 40 percent fewer tokens on Qwen3-8B); c23 (action-loop entropy windows, entropy after the think tag; no numbers read).

### 4.8 Trace length and log-probability as monitors

Trace length predicts correctness about as well as verbal confidence and is complementary (b21). Token log-probabilities track correctness (residual AUROC .686) while residual verbal confidence does not (.473) (b22, d03). Sampling agreement has about twice the resolution of verbal confidence but costs about 10x the inference (d04). Implementation: log all of them, compute AUROC on a held-out set, pick the detector with the best AUROC at a fixed false-alarm rate, and always include trace length as the null baseline (d09).

What the detector papers report (all math, logic or SAT, none on insight items):

| Detector | AUROC | Source |
|---|---|---|
| Uncertainty-curve slope, first 300 tokens, logistic regression | GSM8K 0.727-0.807 over five models; ProntoQA 0.519-0.550 for weak cases | d07 |
| Token-probability instability score | GSM8K 0.66 (greedy) to 0.74 (sampled); 0.605 in first 50 steps; one model about 0.52 | d08 |
| Repetition and low transition entropy (SAT) | 0.795-0.905 on full trace; 0.507-0.570 on sentences before the answer | d06 |
| Scalar entropy or verifier score | improves Brier, not AUROC | d09 |

Read: late-trace detectors are strong but too late to act on. Early detectors are weak. That is the S6 trade-off: a flag has to fire while budget remains.

### 4.8b Lost-correct-answer monitor

Reasoning models often reach a right answer and then overwrite it (d10, d11). Algorithm: at each sentence boundary where a candidate answer appears, store it and run the code check; if the check passes, commit (G6 keeps the best-so-far anyway). Oracle stop at the best point gives +8 percent accuracy and 72 percent fewer thinking tokens, but that uses the answer key and is not reachable. Plain fixed early stopping makes harm worse (10.1 to 18.4), so the stop must be tied to a check, not a position. The model-chosen version fails too: only 24.4 percent of proactive doubts were needed (d15). Free-form answers lose more (.24) than multiple choice (.11) (d11), which is why a code-checkable answer format matters.

### 4.9 Self-correction blind spot

Models detect an injected error in a user's text but not in their own output (64.5 percent blind spot). A "Wait" cue cuts it by 89.3 percent (c08). Implementation: a cue appended by code after the model's output, or a fresh-context re-read by a separate call. Which is better at equal tokens is unknown.

---

## 5. What holds up

### 5.1 Replications and failures (humans)

| Claim | Status | Reason |
|---|---|---|
| FOK does not predict insight solving | Single lab (Metcalfe 1986, 1987). No independent large replication found | Small N (44-48); a zero result is not proof of no relation |
| Warmth is step-like for insight | Mixed. Supported in nine-dot (Chein 2010, N = 25), partly in remote associates (Kizilirmak 2018, d = .82), not in magic tricks (Hedne 2016, d = .12) | Insight defined by problem type vs by self-report gives different answers |
| Warmth and self-report Aha pick the same trials | Fails per problem (r = .08), holds per person (r = .61) | Laukkonen and Tangen 2018 |
| Insight is a property of the problem | Contradicted: depends on the solver (Webb 2016) | The 1987 problem-type labels are suspect |
| Insight solutions are more accurate | Holds on convergent tasks (CRA 93.7 vs 78.3; magic .57 vs .37; anagrams .71 vs .50); weaker or reversed elsewhere | Salvi mechanism: insight solvers time out rather than guess. Danek and Wiley: many wrong insights. McGuinness 2026: open tasks show inflation without accuracy |
| Aha makes things feel true | Established (preregistered, N = 268, d = .321) | Anagram-only |
| False insights are common | Established (several labs, several paradigms) | Individual differences do not predict them |
| Aha spillover onto truth ratings | Shrinks on re-test: d .32 (2020) to .23 and .25 (2022, N about 1250 per sample, same lab); gone with a 10 s delay (p = .447). Downgraded to single-source | Not an independent lab; the effect needs closeness in time |
| Large human warmth replication | None found. Largest related sets (Webb 2016, about 400; Laukkonen 2022, about 1250) do not measure warmth | The search ran out of quota; absence is not proof |

The founding data are tiny: 19 and 39 usable subjects, one-tailed tests, only correct solutions analysed, and selection rules removed 34 to 47 percent of the sample. No large preregistered warmth replication exists (critique gap 5). Hedne dropped about 70 percent of trials for warmth because too few ratings were taken (3 to 4 per trial vs up to 40 in 1987).

### 5.2 Moderators

- **How insight is defined** (problem type, warmth shape, Aha report) changes the result.
- **Convergent vs open-ended task** (McGuinness 2026): insight predicts accuracy on CRAT, inflates self-rated creativity on AUT.
- **Error type**: commission errors vs omissions (Salvi: analytic solvers guess in the last seconds).
- **Instruction wording**: earlier instructions told people Aha means confidence, which creates the link by demand (b27). With neutral wording, confidence is still higher for insight (d = .50).
- **Item difficulty**: felt suddenness and certainty fall on hard Raven items (a24).
- **Prime**: misleading primes cause intrusion errors and higher FOK after wrong fast answers (b13).

### 5.3 Interventions

- **Worked (partly).** A detailed explanation of the FIAT trick cut false insight slightly (b12, snippet only). Few-shot demonstrations with reasoning improved all four tested LLMs, significant in two (c04). Crowd difficulty as a predictor beat self-feeling (a05).
- **Did not work.** Simple warnings did not cut false insights (b12). No intervention improved the accuracy of closeness or Aha-based monitoring in humans in the sources opened (b28; absence of evidence in a limited search). Thinking style and psychosis proneness did not predict false insight (b11). For VLMs, self-verification did not beat majority vote (a30).
- **Worked in LLMs (math).** Code-injected doubt cue recovers about 15 percent of failed rollouts (d15); entropy-gated cue +8.41 pp (a29); appended Wait cut the blind spot 89.3 percent (c08). Prefix consensus keeps accuracy at up to 60 percent fewer tokens (d13).
- **Did not work in LLMs.** Plain early stopping (harmful overthinking 10.1 to 18.4, d11); model-chosen doubt (24.4 percent precision, d15); scalar confidence for ranking (d09); calibration training that hides trajectory-blindness (d05); more RL for more Aha (a28).
- **Best-evidenced remedy.** Make the shift observable or check the answer externally (b28; Laukkonen and Tangen propose a handgrip measure).

### 5.4 Weak spots in this evidence base

- Metcalfe 1986, MacGregor 2001, Ohlsson 1992, Weisberg 1992 were not opened.
- Salvi press-release numbers (94 vs 78 percent linguistic; 78 vs 42 percent visual; b09) are unverified. Use the opened numbers (a23).
- Hedne appears as a09, b03, b04, c12: one study, counted once in independent source counts.
- Danek and Wiley: use 35 magic tricks; evidence b07 says 37 and should be read as 35.
- Laukkonen and Tangen use 180 and 182 problems in different places in the paper.
- The Mizumoto d = .946 (a25) was not found in the text and is unverified.
- The LLM studies are mostly single-lab and single-benchmark: NazoNazo in Japanese, d'Aliberti on Qwen-1.5B, the stumpers and ChatGPT insight studies tiny (n = 20 humans; 5 items; r = -.63 on 4 points).
- Detector AUROCs in d06-d09 come from different tasks, models and protocols. Do not compare them across rows.
- d19 is a search snippet and d20 is a log. Neither is evidence.

---

## 6. Language models

### 6.1 Accuracy on insight-style tasks

- **NazoNazo** (Japanese children's riddles, 201 items, 38 LLMs, zero-shot, no retrieval). Non-reasoning models 7.60 percent, reasoning models 17.59 percent on the 120-item subset; humans 52.9 percent (n = 126, CI 46.6-59.2). Full set 9.42 vs 19.25 percent, OR 2.29. Examples: DeepSeek-R1-0528 22.9, Gemini-2.5-flash 10.9, Claude Opus 4 30.3, Grok 4 37.6 percent. GPT-5 fell inside the human CI (not equivalence). Parameter count did not predict accuracy; release date did (a25, c01).
- **Stumpers (2023).** GPT-3.5/4 solved 57.8 percent (original) and 43.4 percent (enhanced) vs humans 38.15 percent. Chat models beat humans at solving but were below chance at two-option verification (mean 41 percent). A hint prompt helped GPT-3 and hurt chat models (interaction F(1,4) = 30.82, p = .005) (c10, c25).
- **Verbal insight problems (Jan 2023 ChatGPT).** 12 of 30 pooled, matching the modal human score; human n = 20 (c17). A second study: GPT-4 4.5 of 5 insight problems, zero on both analytic problems; item accuracy negatively related to human accuracy (r = -.63 on four points; do not weight) (c18).
- **Only Connect Wall.** Removing red herrings raises scores; GPT-4 connection F1 41-45 percent vs human about 80 percent (c11).
- **Riddle Riddle (2026, d14).** Nine frontier LLMs on 30 matched sets. Genuine riddles 84.9 percent. Riddle-form items whose answer is literal: 50.7 percent. Of the errors, 90.8 percent were inappropriate inventive reasoning. Humans show the mirror image (50.5 genuine vs 80.5 riddle-form, permissive coding). A more memorised riddle is easier as itself (OR 1.43) and harder as its lure (OR 0.76). This is the closest LLM analogue of false insight: the model reads cleverness into a plain question. No confidence was measured and no verifier arm was run.
- **CresOWLve (2026, d17).** 2,061 real-world creative puzzles. Up to a 17 percent drop versus factual questions. Models often retrieve the right facts and fail to connect them. Reasoning effort helps (9.4 to 17.8 percent English for one model).
- **BRAINTEASER.** Humans about 92 percent; ChatGPT about 60-63 percent instance accuracy and under 40 percent group accuracy (snippet; c22).

### 6.2 Monitoring failures

- **Verification failure** on 5.23 to 39.34 percent of wrong answers (four models, case counts 9 to 48, literal string match) (c02). The authors tie it to the human "feeling of rightness" and say humans rarely do this.
- **False Aha text** appears more than 100 times in Claude Opus 4 logs but rarely precedes a correct answer (a27).
- **Language effect.** Grok 4: 29.5 percent (33/112) in Japanese thinking vs 48.8 percent (40/82) in English, Fisher p = .0071. Claude Opus 4: 36.7 vs 28.7, p = .356 (b18, c04).
- **Self-correction blind spot**: average 64.5 percent across 14 open models; "Wait" cuts it 89.3 percent (c08).
- **Confidence.** Verbal confidence on hard question sets is overconfident (b23; values not extracted). Verbal confidence tracks commitment more than correctness (b22). Solve-and-rate in one prompt corrupts the signal (c15). Steyvers 2024: people over-trust default LLM explanations; model ECE .104 vs humans .264; AUC model .751 vs humans .589; long explanations raise confidence without better discrimination (AUC .54) (c14). Distillation and RL improve verbalised confidence in reasoning-heavy settings (b20), but small reasoning models may be worse at knowing their limits.
- **Confidence validity, 2026 (d03-d05).** Verbal confidence predicts the later commit decision better than correctness (4 non-reasoning models; residual correctness AUROC .473, p = .844, while residual log-prob is .686, p = .0039). It is unstable across prompt templates and looks calibrated only because it clusters near the base rate (resolution .0316 vs .0637 for sampling agreement; in 9 of 10 cells calibrated verbal confidence never exceeds .50; N = 842, models 0.5B-7.6B). It barely moves when the reasoning trajectory is cut (78.5 percent of items change by under .02, one VLM). None of this used insight items, and none used frontier reasoning models. A separate later call is not a fix: that later stage reflects commitment.
- **Lost correct answers (d10, d11).** On math, reasoning models reach a correct answer and overwrite it. Harmful overthinking is .11 for multiple choice and .24 for free-form. This is the maths relative of NazoNazo verification failure.
- **Models can partly know.** Larger LMs predict P(True) (a31). They can report and control some low-dimensional directions of their own activations (a32). Neither is tested on insight tasks.

### 6.3 Aha and shifts in reasoning traces

- Mid-trace shifts are rare (6.31 percent pooled; Qwen2.5-1.5B about 7.6; GPT-4o 0.88-2.21; DeepSeek-R1 0.00-0.25) and lower accuracy (2.57 vs 16.44 percent). Formal Aha events: 1.79 percent. More training did not help (marginal effects -0.0311 crosswords, p = .027; -0.0615 math, p = 1.6e-4) (a28).
- On MATH-500, with a shift vs without: Qwen-7B 28.2 vs 66.1; GPT-4o 33.8 vs 65.8; DeepSeek-R1 20.4 vs 54.3; Llama-8B 28.2 vs 45.7. Cryptic crosswords are the exception: 20.1 vs 9.6. This is correlational, since shifts occur on harder items (c05).
- Hesitation words grow with difficulty in distilled R1-style models, not in instruct models (c07). Verbalised uncertainty tokens restore information gain: masking them costs about 25 percent (R1-Distill-Qwen-32B) and 19 percent (14B) (c09).
- VLMs: Aha in 8.3 percent of responses; adds little (a30).
- Doubt is mostly unneeded: only 24.4 percent of proactive corrections were on traces that needed them. A code-injected minimal cue still recovers about 15 percent of failed rollouts, and the recovery falls toward zero as the cue comes later (d15).
- Format matters for self-correction: open generation improves in the first one or two rounds and then drifts; multiple choice gains slowly and is capped by the options (d16). Exact deltas were not extracted.
- Unlike the human case, a model-chosen shift is bad and a code-chosen shift is good (a29).

### 6.4 What changed behaviour and by how much

| Change | Effect | Source |
|---|---|---|
| Entropy-gated "reconsider" cue (code-chosen) | +8.41 pp MATH-500 (Qwen-1.5B); about 0 on crosswords, Rush Hour | a29 |
| "Wait" appended after own output | blind spot cut 89.3 percent; accuracy +156.0 percent (relative) | c08 |
| Reasoning training | 7.60 to 17.59 percent on NazoNazo; OR 2.29 | c01 |
| Few-shot with reasoning demonstrations | all 4 models improved, 2 significantly | c04 |
| Metacognitive prompt vs CoT (GPT-3.5) | +2.65 to +10.07 points; hints can hurt chat models | c21, c25 |
| Steering the confidence direction | ECE 14.9/35.1/36.0 to 3.7/3.3/10.7 (needs weights) | c15 |
| Attention-state early stop | +3.2 percent, about 40 percent fewer tokens (Qwen3-8B) | c20 |
| Self-verification best-of-N (VLMs) | down by up to 16.7 percent; majority vote up | a30 |
| More RL training | did not raise Aha shifts or accuracy from shifts | a28 |
| Injected minimal doubt cue at a truncation point | recovers about 15 percent of failed rollouts; falls toward zero when late | d15 |
| Plain early stop at fixed K | harmful overthinking 10.1 to 18.4 (K=5) | d11 |
| Prefix consensus instead of full self-consistency | same or better accuracy, up to 60 percent fewer tokens | d13 |
| Proof-search prompt (SAT, oracle-selected) | Llama3-70B 13.3 to 85 percent; post hoc, not matched in length | d06 |

Limits: single-lab, single-benchmark results; Aha-shift work is mostly on small models; NazoNazo is Japanese; no study tests human-style warmth ratings by an LLM on insight problems.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **G: the agent's own warmth, progress, feeling-of-rightness or "Aha/Wait" text is never evidence of being close or right.** Keep and sharpen G10 and the 4b line on verbal confidence. Part: G. [E]. Evidence: K07, K14, K17; a21, b07, b11, b13, a28, c05, d03, d04, d05. Note: the warmth/FOK result alone (K01) and the spillover result (K09) are single-source, so the rule rests on false insight (several labs), LLM shift evidence and the 2026 confidence-validity results.
2. **S6: impasse is detected by code, never by a felt signal.** Triggers from counts and checks (no pass, same error twice, budget fraction). Part: S6. [E] for the principle (K14, K17: model-reported confidence and shifts are weak: d03, d04, d05, a28). The choice of statistical detector (entropy, length, repetition) is [C] (K19, K25: d06-d09) and goes to Test first, not Add now.
3. **O8/G1: reconsideration is fired by code on a flag, not by the model's own shift.** Part: O (reframe trigger). [E] (K15: a29, c06, a28, c05; supported by d15 on the injected cue, K24 [S]). Caveat: one small model, math. The equal-token baseline is cheap voting (K28), not plain self-consistency.
4. **S4/S8: harvest every candidate seen in the trace, including dropped ones, and test them by code.** Part: S4. [E] for the own-output blind spot (K16: c08, c09); verification failure rate itself is [S] (K11: c02). This is already the S4 harvest rule; this adds support, not machinery.
5. **S6/S8: log the first position where a correct candidate appears and keep it.** Reasoning models lose correct intermediate answers (harmful overthinking .11 to .24; oracle stop +8 percent, -72 percent tokens). Part: S6, O (commit/verify). [E] (K23: d10, d11), math only; riddle version is [S] (K11). Fixed early stopping is not this: it raised harm 10.1 to 18.4. The rule is tied to a code check.
6. **G/S8: independent verification on something the answer was not fitted to (G3), even after a confident reframe.** False insight is common (K07). [E].
7. **Memory/S0: keep the class pass rate as the difficulty prior.** Basis: normative gamma .77 vs own .08 (a05). [S] as evidence; the class record already exists. Also supported by the 2026 result that sampling agreement has about twice the resolution of verbal confidence (d04, [S]).

### Test first (single-source, contested, or human-only)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Sibling-sample pass rate beats the model's own progress rating as predictor of success on insight items | G, S6 | [S] | K01; a03, a05 |
| Entropy gate vs fixed-schedule reframe vs self-consistency at equal tokens, on frontier reasoning models | S6, O8 | [S] | K15; a29, c06 |
| Forced candidate check when a candidate appears in the trace (verification failure recovery) | S4, S8 | [S] | K11; c02, a26 |
| Answers after a reframe: accurate on convergent items, inflated on open items? | S6, S7 | [C] | K08; a23, b16 |
| Separate-call confidence vs same-call vs trace length vs entropy (AUROC); a later-stage rating reflects commitment (d03) | S6 | [C] | K17; b22, c15, b21, d03 |
| Appended cue after own output vs fresh-context re-read | O (verify), S5 | [S] | K16; c08 |
| Spillover of certainty across items in long contexts, and a context reset (cheap insurance; shrinks to d .23-.25 on re-test, gone after 10 s) | G | [S], human only | K09; b10, d01 |
| Metacognitive prompting vs plain CoT vs vote at equal tokens | none | [C] | K21; c21, c25, c17 |
| Best impasse detector: entropy burst, trace length, action loop, repeated candidate, with trace length as the null | S6 | [C] | K19, K25; c19, c23, d06-d09 |
| Gate vs prefix-consensus voting at equal tokens | S6 | [S] | K28; d12, d13, d18 |
| Riddle-form lure items with a literal answer: commit rate with and without an independent verifier | G, O (verify) | [S] | K22; d14 |
| Code-injected doubt cue at an impasse vs no cue vs vote | S6, O8 | [S] | K24; d15 |
| Separate-call confidence vs same-call vs sample agreement vs log-prob | S6 | [S] | K27; d03, d04 |
| Forced two-option verification vs open generation on stumpers | O (verify) | [S] | K20; c10 |

Not to add: any agent warmth rating; "Aha" phrase counts as a reward or stop signal (K12, K14); a metacognitive prompt as a standing step (K21 contested; also 4b, unstructured self-reflection).

---

## 8. Concrete tests on our bench

All arms use equal tokens (G7). Report AUROC with bootstrap CI and accuracy per arm. Run at least 3 seeds. Setup cost counts.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | BRAINTEASER sentence and word puzzles plus our word puzzles | (a) model's own progress/confidence rating mid-trace; (b) sibling-sample pass rate; (c) trace length; (d) token entropy where available | AUROC for eventual success per signal, at 10 percent false alarms | (b)-(d) beat (a) (K01, K17, K19). Gap 0.05 to 0.15 AUROC; uncertain |
| T2 | Insight-style items with a code-checkable answer (fixed-answer riddles, CRA-style) plus math | (a) plain; (b) self-consistency vote; (c) fixed-schedule reframe; (d) entropy-gated reframe by code | Accuracy at equal tokens, per domain | (d) beats (c); (d) vs (b) unknown. Gain largest at mid base rates, near zero when base rate is near zero (K15) |
| T3 | Same riddle set, models with visible thought logs | (a) answer as given; (b) harvest all candidates in the trace and run through the check | Accuracy; share of wrong answers where the gold string was in the log | (b) recovers part of the 5 to 39 percent verification failures (K11) |
| T4 | FIAT-type anagram or lure items we seed | (a) agent alone; (b) agent plus independent code check (G3); (c) agent plus "be careful" warning | Rate of confident commit to the lure | (b) lowers it; (c) does not (K07, K10, 4b) |
| T5 | Convergent items vs open-ended items (AUT-style, scored by running or raters) | answers after a detected reframe vs without | Accuracy on convergent; objective vs self-rated quality on open | More accurate on convergent, inflated self-rating on open (K08, b16) |
| T6 | Errors injected into the agent's earlier step | (a) appended "Wait" cue; (b) fresh-context re-read; (c) no cue | Fraction of injected errors caught; false-fix rate | Both beat (c); order of (a) vs (b) unknown (K16) |
| T7 | Item pairs in one long context | (a) context kept; (b) context reset | Change in stated certainty on item N+1 after a reframe on N | Shift in (a), none in (b), if spillover transfers (K09). Size unknown |
| T8 | BRAINTEASER with consistency checks | metacognitive prompt vs CoT vs vote | Instance and group accuracy | Small or null once vote is the baseline (K21) |
| T9 | Stumper-style items | open generation vs forced two-option verification | Accuracy; verification accuracy when the model could not solve | Verification near or below chance unless a check is attached (c10) |
| T11 | One shared trace set, all detectors | entropy burst, trace length (null), action loop, repeated candidate, prefix agreement | AUROC for failure and false-alarm rate at fixed recall, computed within problem | Several detectors fall to the length null; gate on whichever beats it by 0.05 or more (K25, d09, d19) |
| T12 | Insight-style plus math | (a) entropy-gated cue; (b) prefix-consensus voting; (c) plain self-consistency | Accuracy at equal tokens | (b) matches (c) cheaply; (a) must beat (b) to be worth keeping (K28) |
| T13 | Riddle-form items with a literal answer, plus genuine riddles | (a) agent alone; (b) agent plus forced literal-reading check; (c) agent plus independent verifier | Rate of clever-but-wrong commits; accuracy on genuine riddles (no loss) | (b) or (c) cut over-inventive errors from the 49 percent range (K22, d14) without hurting genuine riddles |
| T14 | Items where the correct candidate shows in the trace | (a) final answer as given; (b) commit at first candidate that passes the check | Accuracy and tokens | (b) recovers part of the lost correct answers (K23). Do not use fixed-K early stopping as an arm; it raised harm |
| T10 | Any item set | count Aha/Wait/"Oh!" phrases per trace vs correctness | AUROC of phrase count | About 0.5 or below; noise (K12, K14) |

---

## 9. What does not transfer, and why

- **Warmth as a measurement.** Warmth is a human report taken every 15 s. A prompted rating from a model is text produced on request, not a continuous felt closeness. No LLM study tests it. We do not build on it.
- **The "sudden jump" shape.** The jump is about when the solver becomes aware of a solution. An LLM writes tokens one at a time, and a reframe is a text event we can see in the log. We need not infer it from a rating.
- **Human Aha as affect.** Pleasure, suddenness and certainty (a22) are affect components. The model has no affect in the sense measured. Its "Oh! I've got it" is a phrase and rarely precedes a correct answer (a27).
- **Time-based findings.** Salvi's last-5-s errors (29.4 vs 4.7 percent) come from a timed window. An agent has a token budget. "Time out rather than guess" pulls against G6 (never abstain on the first pass). Do not copy it.
- **Problem-type labels (insight vs algebra).** Insight is solver-dependent (Webb 2016). Class membership alone must not select the mode; use the class pass rate (S0).
- **Small-model entropy gains.** The +8.41 pp result is Qwen2.5-1.5B on MATH-500. Frontier reasoning models may already re-check themselves. Needs T2.
- **Neuroscience.** Not covered here. This file is behavioural only.
- **Single-language benchmark.** NazoNazo is Japanese, and the thought-log language moved Grok 4 accuracy (29.5 vs 48.8 percent). Rates may differ in English.
- **Spillover.** The human effect needs closeness in time (a 10 s delay removes it) and is d .23-.25 on re-test. An agent's context is not a feeling. Test only a reset (T7).
- **Math results as insight results.** Most LLM detector and overthinking numbers (d06-d13) are on math, logic or SAT. Insight items are rarer, with low base rates, and the gate showed no gain at near-zero base rates (crosswords +0.45, Rush Hour +0.01).
- **Small and non-reasoning models.** Confidence validity findings (d03, d04) are for non-reasoning or 0.5B-7.6B models. Frontier reasoning models may differ.
- **Human interventions (warnings, instructions).** No human intervention worked reliably, so there is nothing validated to port. LLM prompt help depends on the model (c25).

---

## 10. Open questions

1. Does an LLM's self-reported progress, sampled mid-trace, predict success better than token entropy or trace length? No direct study (gap 1). Decides the guardrail.
2. At equal tokens, does code-triggered reconsideration beat self-consistency on insight-style items for frontier reasoning models, not only Qwen-1.5B? (gap 2)
3. How often do frontier models write the correct answer in the trace and not commit, outside Japanese riddles, and does forced candidate check recover it? (gap 3)
4. What is the false-insight rate in LLMs on FIAT-type items, and does an independent verifier reduce it? (gap 4)
5. Is there a large preregistered replication of Metcalfe and Wiebe warmth with solver-defined insight (N > 200)? (gap 5) Answered as none found in a limited search; the decision stays: do not build on warmth.
6. Does the Aha-accuracy advantage survive in LLM traces: more accurate after a reframe on convergent items, less on open items? (gap 6)
7. Does confidence in a separate call beat same-call confidence on insight items? (gap 7)
8. Does Aha spillover (d = .32) have an analogue in long agent contexts? (gap 8)
9. Which impasse detector has the best AUROC at low false-alarm cost? (gap 9) No head-to-head. Reported values are .5 to .9 on different tasks, and length baselines absorb gains.
10. Do metacognitive prompts help beyond CoT at equal tokens once sample-and-vote is the baseline? (gap 10)
11. Is continuous vs discontinuous warmth settled? No shared-protocol experiment exists (b26).
12. Why do cryptic crosswords show shifts helping (20.1 vs 9.6) while MATH-500 shows them hurting? Selection or a real domain effect?
13. Does the riddle-form lure (d14) produce high stated confidence, and does a verifier cut it? No confidence or verifier arm exists.
14. Does a code-injected cue beat voting at equal tokens? d15 has no vote baseline.
15. Unverified items: the d = .946 in a25; the 35 vs 37 magic-trick count; Salvi press-release numbers.

---

## 11. Sources

[V] = opened and read this session (per the evidence files). [M] = snippet, abstract, or second-hand only.

| Source | Mark | URL |
|---|---|---|
| Metcalfe and Wiebe (1987) Intuition in insight and noninsight problem solving, Memory and Cognition 15(3) | [V] | https://link.springer.com/content/pdf/10.3758/BF03197722.pdf |
| Metcalfe (1986) Feeling of knowing in memory and problem solving, JEP:LMC 12, 288-294 | [M] | https://doi.org/10.1037/0278-7393.12.2.288 |
| Metcalfe (1986) Premonitions of insight predict impending error, JEP:LMC 12, 623-634 | [M] | https://link.springer.com/content/pdf/10.3758/BF03197722.pdf (as described in the 1987 paper) |
| Weisberg (1992) Metacognition and insight during problem solving: comment on Metcalfe | [M] | https://www.frontiersin.org/articles/10.3389/fpsyg.2018.00282/full (as cited) |
| Chein, Weisberg, Streeter and Kwok (2010) Working memory and insight in the nine-dot problem | [V] | https://link.springer.com/content/pdf/10.3758/MC.38.7.883.pdf |
| MacGregor, Ormerod and Chronicle (2001) Information processing and insight, JEP:LMC 27(1) | [M] | https://link.springer.com/content/pdf/10.3758/MC.38.7.883.pdf (as described) |
| Ohlsson (1992) Information-processing explanations of insight | [M] | https://link.springer.com/content/pdf/10.3758/MC.38.7.883.pdf (as described) |
| Hedne, Norman and Metcalfe (2016) Warmth and confidence, magic tricks, Frontiers in Psychology 7:1314 | [V] | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5005374/ |
| Laukkonen and Tangen (2018) How to detect insight moments, Frontiers in Psychology 9:282 | [V] | https://www.frontiersin.org/articles/10.3389/fpsyg.2018.00282/full |
| Webb, Little and Cropper (2016) Insight is not in the problem, Frontiers in Psychology 7:1424 | [V] | https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01424/full |
| Danek and Wiley (2017) What about false insights? | [V] | https://www.frontiersin.org/articles/10.3389/fpsyg.2016.02077/full |
| Salvi, Bricolo, Kounios, Bowden and Beeman (2016) Insight solutions are correct more often | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC5035115/ |
| Chuderski et al. (2020) Metacognitive experience on Raven's matrices versus insight problems | [V] | https://link.springer.com/content/pdf/10.1007/s11409-020-09236-6.pdf |
| Kizilirmak et al. (2018) Feelings-of-warmth increase more abruptly for riddles solved with Aha | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC6099077/ |
| Laukkonen, Kaveladze, Tangen and Schooler (2020) The dark side of Eureka | [V] | https://www.gwern.net/doc/psychology/cognitive-bias/illusion-of-depth/2020-laukkonen.pdf |
| Grimmer et al. (2022) Thinking style and psychosis proneness do not predict false insights | [V] | https://www.gwern.net/doc/psychology/cognitive-bias/illusion-of-depth/2022-grimmer.pdf |
| Grimmer et al. (2023) The illusion of insight: detailed warnings reduce but do not prevent false Aha moments | [M] | https://doi.org/10.1080/13546783.2022.2146191 |
| Ammalainen and Moroshkina (2020) When an error leads to confidence | [V] (via web summarizer) | https://cyberleninka.ru/article/n/when-an-error-leads-to-confidence-false-insight-and-feeling-of-knowing-in-anagram-solving |
| Becker, Wang and Cabeza (2024) Surprise! Clarifying the link between insight and prediction error | [V] | https://edoc.hu-berlin.de/bitstreams/39491043-ed53-4074-b147-12b0d5af8522/download |
| Rebus-puzzle study (2024) Aha and perceived difficulty | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC10844378/ |
| McGuinness, Schooler, Gable and Gross (2026) The Aha! Glow | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC13514557/ |
| Webb, Laukkonen, Cropper and Little (2021) commentary on the insight-accuracy link | [M] | https://doi.org/10.1002/jocb.433 |
| Laukkonen, Webb, Salvi, Tangen, Slagter and Schooler (2023) Insight and the selection of ideas | [M] | https://doi.org/10.1016/j.neubiorev.2023.105363 |
| Mizumoto et al. (2025) NazoNazo / The Metacognitive Bottleneck | [V] | https://arxiv.org/abs/2509.14704 |
| d'Aliberti and Horta Ribeiro (2026) The Illusion of Insight in Reasoning Models | [V] | https://arxiv.org/abs/2601.00514 |
| Wu et al. (2026) Aha moment revisited: VLMs and self-verification | [V] | https://arxiv.org/pdf/2506.17417 |
| Yang et al. (2025) Understanding Aha moments | [V] (b19 abstract and headings only; c07 fuller) | https://arxiv.org/abs/2504.02956 |
| Kadavath et al. (2022) Language models (mostly) know what they know | [V] | https://arxiv.org/pdf/2207.05221 |
| Ji-An et al. (2025) LMs can monitor and control their internal activations | [V] | https://arxiv.org/pdf/2505.13763 |
| Thinking Out Loud: do reasoning models know when they are right? (2025) | [V] | https://arxiv.org/abs/2504.06564 |
| Trace length is a simple uncertainty signal in reasoning models (2025) | [V] | https://arxiv.org/abs/2510.10409 |
| Reported confidence in LLMs tracks commitment more than correctness (2026) | [V] | https://arxiv.org/abs/2606.29490 |
| Reasoning about uncertainty: do reasoning models know when they don't know? (2025) | [V] partial | https://arxiv.org/abs/2506.18183 |
| Tsui (2025) Self-Correction Bench | [V] | https://arxiv.org/html/2507.02778v1 |
| Kim et al. (2026) Strategic information allocation under uncertainty | [V] | https://arxiv.org/html/2603.15500v1 |
| LLMs versus humans on stumpers (EMNLP Findings 2023) | [V] | https://aclanthology.org/2023.findings-emnlp.779.pdf |
| Large Language Models are Fixated by Red Herrings (Only Connect Wall) | [V] | https://arxiv.org/pdf/2306.11167v4.pdf |
| Steyvers et al. (2024) What LLMs know and what people think they know | [V] | https://arxiv.org/html/2401.13835v2 |
| Miao and Ungar (2026) Closing the confidence-faithfulness gap | [V] | https://arxiv.org/html/2603.25052v1 |
| Kumaran et al. (2026) How do LLMs compute verbal confidence | [M] | https://arxiv.org/abs/2603.17839 |
| Human-like problem-solving abilities in LLMs using ChatGPT (2023) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC10244637/ |
| Caution against anthropocentrism (2023) | [V] | https://arxiv.org/pdf/2309.07683 |
| Zhu et al. (2026) GUARD, failure dynamics | [V] | https://arxiv.org/pdf/2604.14528 |
| Li et al. (2026) ASAG attention-state adaptive generation | [V] | https://arxiv.org/pdf/2606.15070 |
| Bai, Cao, Ge and Yu (2025) MP: lateral thinking, AAAI | [M] | https://ojs.aaai.org/index.php/AAAI/article/view/34514 |
| Jiang et al. (2023) BRAINTEASER | [M] | https://arxiv.org/pdf/2310.05057 |
| Laukkonen, Ingledew, Grimmer, Schooler and Tangen (2022) Irrelevant insights make worldviews ring true, Sci Rep | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC8826315/ |
| Kumaran (2026) Reported confidence in LLMs tracks commitment more than correctness | [V] | https://arxiv.org/pdf/2606.29490 |
| Ghosh, Kumar and Garg (2026) Measurement validity of confidence signals | [V] | https://arxiv.org/pdf/2610.25846 |
| Yang, Han, Pham and Kim (2026) Mirage of calibrated confidence | [V] | https://arxiv.org/pdf/2609.18453 |
| Sourav and Balwani (2026) The Tell-Tale Trace | [V] | https://arxiv.org/pdf/2608.03291 |
| Grunefeld et al. (2026) Tracing uncertainty in LM reasoning | [V] | https://arxiv.org/pdf/2605.07776 |
| Chen, Cheng, Han and Keselj (2026) Diagnosing dynamic instability | [V] | https://arxiv.org/pdf/2602.02863 |
| Song, Li and Liu (2026) Prefix-safe Bayesian belief tracking | [V] abstract and introduction | https://arxiv.org/pdf/2605.27712 |
| Song et al. (2026) ThinkBrake | [V] | https://arxiv.org/pdf/2510.00546 |
| Caldarella et al. (2026) Thinking past the answer | [V] | https://arxiv.org/pdf/2606.02835 |
| Hosseini et al. (2026) CoDE-Stop | [V] | https://arxiv.org/pdf/2604.04930 |
| Jindal et al. (2026) Path of least resistance (PoLR) | [V] | https://arxiv.org/pdf/2601.21494 |
| Fascendini, McGregor, Gupta and Griffiths (2026) The Riddle Riddle | [V] | https://arxiv.org/pdf/2606.27103 |
| Rahmani et al. (2025) Self-correcting LLMs: generation vs multiple choice | [V] abstract, intro, results scan | https://arxiv.org/pdf/2511.09381 |
| Ismayilzada et al. (2026) CresOWLve | [V] | https://arxiv.org/pdf/2604.03374 |
| Chen et al. (2025) Neuron agreement decoding | [V] abstract and introduction | https://arxiv.org/pdf/2510.26277 |
| Token-level verification mirage (2026, ICML listing) | [M] snippet only | https://icml.cc/virtual/2026/82428 |
| Entropy and loop detectors (2025-2026), arXiv 2509.26522, 2510.08146, 2603.14251, Sotis | [M] | https://arxiv.org/abs/2509.26522 |
