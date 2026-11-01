# Meta-reasoning: deep document

*Subfield A04.07. Sources: evidence_a-d.jsonl (ids a01-a27, b01-b27, c01-c25, d01-d25), claims.jsonl (K01-K34), critique.md (corrections applied). Written 2026-11-01.*

## 1. What it is

Meta-reasoning is the study of how a thinker watches and steers its own reasoning. Two levels. The object level does the reasoning. The meta level reads signals about it (how fluent, how conflicted, how much progress) and decides: keep going, change approach, or stop and answer. (a01)

Ackerman and Thompson (2017) name the monitoring points (a01, b01):

- Initial Judgment of Solvability: before starting, can I solve this?
- Feeling of Rightness (FOR): right after the first, fast answer.
- Intermediate confidence and feeling of progress: during the work.
- Final confidence: when deciding to submit.
- Feeling of error and Final Judgment of Solvability: for giving up.

Control actions: accept the first answer, rethink, switch strategy, stop, give up.

Why it matters for our agent. Guardrail G1 says doubt only on a signal. Meta-reasoning is the science of which signals exist, how good they are, and how people and models fail in both directions: stopping too early (strong FOR on a wrong answer) and stopping too late (more thinking that adds nothing or hurts). State S6 (impasse) is a stop-and-switch decision, so it falls here too.

Scope. Dual-process work, metamemory, overconfidence, progress monitoring and test-time compute scaling are sibling subfields. This document covers the FOR / rethink / stop loop and its LLM versions.

## 2. History and theories in depth

**Memory roots (1990).** Nelson and Narens built a two-level model for memory: monitoring flows up, control flows down. Ackerman and Thompson extended it to reasoning (a01).

**Dual-process framing (Thompson 2009, a08).** Heuristic (Type 1) answers arrive with a strong FOR. FOR is the reasoner's cue to look no further. FOR is analogous to feeling of knowing and rests on retrieval fluency. It was a theory chapter with no new data.

**Two-response paradigm (Thompson, Prowse Turner and Pennycook 2011; d01, a09).** The participant gives a fast first answer, rates FOR, then rethinks in free time and answers again. Four experiments: conditional reasoning N=60, three-term conditional N=48, base-rate N=128, syllogisms N=64 (total 300; abstract only, effect sizes not seen). Low FOR goes with longer rethinking and more answer changes. FOR was predicted by how fluently the first answer came to mind. Validation steps in the paradigm: ask whether the first answer was the first to come to mind; use deadline or load; check that giving a first answer does not change the second (a02).

**Meta-reasoning framework (Ackerman and Thompson 2017; a01-a07).** Full loop plus cue theory (fluency, familiarity, conflict) and the Diminishing Criterion Model (Ackerman 2014; a04): people start by demanding high confidence and lower the bar as time passes. They stop when confidence passes the bar. Final confidence at stopping can be as low as 20%, even when an "I don't know" option exists (a04, a07).

**Cue theory.** FOR is cue-based, not difficulty-based (a02, a03). Fluency raises FOR whether the answer is right or wrong. Causal test cited in the review: a solution shown 50 ms after an anagram, equation or remote-associates problem was judged correct more often than one shown after 150 or 300 ms, regardless of truth (a03). Conflict between candidate answers lowers FOR and is a valid cue (Thompson and Johnson 2014; Markovits 2015 for unfamiliar terms; a07). Cues are valid or invalid by task (b02).

**Stopping errors.** Premature stopping has three listed causes: strong FOR, FOR weak but above the aspiration level, and low priority on accuracy (a06). Late stopping: people gather more information than needed, even when paying for it, because information raises confidence. Stopping is set by a confidence criterion, not by value of information (a06, b03).

**Rival accounts of the first response.** Bago and De Neys (2017, a11): the first, fast response is often already correct. This challenges the default-interventionist view where slow analysis fixes wrong intuitions. De Neys (2023) offers the hybrid view: two competing Type 1 intuitions (heuristic and logical) of similar strength create the conflict that triggers Type 2 (a27, b05). Trippas, Thompson and Handley (2017, b11) found parallel processing of belief and logic: for the simplest problems (modus ponens) belief judgments were less accurate than validity judgments; at the most complex, belief interfered more with validity. So "fast belief always comes first" is false. The debate is open (b05).

**Move to machines (2022-2026).** Four threads:
1. Calibration and self-knowledge: Kadavath 2022 (a14), Xiong 2024 (a15), Tian 2023 (d10).
2. Self-correction: Madaan 2023 (a26), Huang 2024 (a17), Tyen 2024 (a18), Kamoi 2024 (d11).
3. Overthinking and underthinking in reasoning models: Chen (a19), Wang (a20), Su (d19), Shojaee (c14).
4. Machine FOR: probes, trial-answer confidence, token confidence, answer convergence (c01, c05, c06, c07, d23). Sui et al. (c15) built a bandit meta-controller on the monitor-and-control loop.

## 3. Core findings with exact numbers

Status: Est = established (2+ independent sources), Single = one independent source, Cont = contested. Human = human-only. Old = older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Low FOR gives longer rethinking and more changes | Four experiments N=60, 48, 128, 64; effect sizes not seen | d01, a02, d02 (N=289, same tradition) | Est by tradition; no independent-lab replication; Human |
| FOR driven by answer generation fluency, not output speed | Two experiments; output duration had no effect | d03 | Single; abstract only |
| FOR predicts direction of change | N=289 belief-logic syllogisms; low FOR on a belief answer shifts to logic, high FOR shifts to belief | d02 | Single; abstract only |
| Fluency is a cue to certainty | 50 vs 150 vs 300 ms delay changes judged correctness | a03, b02 | Est; review level |
| Most final correct answers were already correct at first response | 74.8% (base-rate), 87.6% (syllogism); Exp 1 N=101, Exp 2 N=104 (12% deadline misses). Conflict items, base-rate: stayed correct 32.7%, stayed wrong 56.7%, wrong to right 10.1% | a11, a05 | Est; two task types |
| Capacity predicts correct first intuition more than correction | r=.44 vs r=.22; one study N=160 | a12 (b18 snippet) | Single; Human |
| Wrong answers on conflict items keep high confidence | CRT confidence (1-9): correct 8.49, wrong 6.82, N=60; CRT discrimination d=0.47 vs general knowledge d=1.24; overconfidence d=0.61; wrong-conflict as confident as correct GK in Studies 1-2 only | b09, b10 | Est; boundary in Studies 3-4 |
| Many biased reasoners detect conflict | Frey Study 1, 232 biased: confidence 68.6% vs 79.0%, F(1,230)=59.35, partial eta2=.21; 66% lowered confidence (mean -20.8%), 28.9% raised (+11.7%), 5.2% same | a10 | Cont (see b13) |
| Detection effects on invalid inferences vanish when scored by chosen response | N=248, two experiments; no RT or confidence difference | b13, d04 | Cont |
| Giving up is a trait separate from confidence | N=176; with confidence r=.04; with ability r=.26; confidence with ability r=.61 | b14 | Single; Human |
| Screen lowers answer change on conflict items | N=34; interaction F(1,33)=13.09, partial eta2=.284 | b15 | Single; small N |
| LLM self-correction without feedback hurts | GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GSM8K 75.9 to 75.1 to 74.7; GPT-4 GSM8K 95.5 to 91.5 to 89.0; CSQA 82.0 to 79.5 to 80.0 | a17, b22, c12 | Est; Old (2023) |
| With oracle labels the same loop "works" | GPT-3.5 GSM8K 75.9 to 84.3; GPT-4 95.5 to 97.5 (84.3 is GPT-3.5, per critique) | b22 | Est (leakage) |
| Finding the error is the bottleneck | GPT-4 mistake finding about 53% on BIG-Bench Mistake (2,186 PaLM 2 traces, 15% correct / 85% incorrect) | a18 | Single |
| Self-correction blind spot | 64.5% mean over 14 non-reasoning models; "Wait" cuts 89.3%; 5,306 fine-tune traces cut 76.0% | c16 | Single |
| Verbalised confidence overconfident, weak predictor | ECE above 0.377 (GPT-3, 3.5, Vicuna); GPT-4 AUROC 62.7%; white-box 0.605 vs black-box 0.522; 5 task types, 8 tasks | b21, a15, c11 | Est; Old |
| Large models calibrated on MC / true-false | 52B model, 10 equal-count bins; poor out of distribution | a14, b20, c10 | Single lab; Old |
| Reasoning models state confidence better | Strictly better in 33 of 36 settings; GLM-Z1 ECE 0.037 lower despite 0.07 lower accuracy | c08 | Single |
| Hidden-state probe as machine FOR | ROC-AUC above 0.7 everywhere, above 0.9 on AIME (32B); ECE 0.01-0.14; up to 24% fewer tokens | c01, c02, a21 | Single; white-box |
| Trial-answer early exit (DEER) | 11 models, 10 benchmarks; length -19.1% to -80.1%; accuracy +0.3 to +5.0; about 75% of samples have an early-correct point; code -19.9% vs math/science -61.5% | c05, a22 | Est (with d23, c06) |
| Thought Calibration | Up to 60% fewer tokens in distribution, up to 20% out | c06, d24 | Est with c05 |
| DeepConf | AIME25 GPT-OSS-120B 99.9% vs 97.0% majority vs 91.8% pass@1; up to 84.7% fewer tokens; DeepConf-low saves 43-79%; Qwen3-32B BRUMO25 -0.9%; HMMT25 cons 92.9 vs 88.9 | a23, b26, c07 | Single lab; mixed |
| Answer convergence | Final answer reached after about 60% of steps; over 40% tokens saved on NaturalQuestions; 46.2% in one learned setting | d23 | Single |
| Overthinking | 1,953% more tokens on 2+3; first round correct in over 92% (89-97% by model and set); first round under 60% of tokens (287 tokens = 38.7% on ASDIV); trimming cut MATH500 tokens 48.6% | a19, b24, c03, c04 | Est |
| Underthinking | Wrong answers +225% tokens, +418% switches; over 70% of wrong responses hold a correct thought; TIP pass@1 AIME24 38.3 to 44.1; pass@4 43.7 to 51.4 | a20, b25 | Est |
| Length vs correctness | Wrong answers over 6,000 tokens vs under 3,000 (MATH); shortest chain up to 34.5% more accurate than longest, up to 18.8% over random; short-1@k matches majority vote with up to 40% fewer tokens | d19, d20 | Est |
| Inverse scaling in test-time compute | Five failure modes; slopes not extracted | a24 | Single; built to show existence |
| Three complexity regimes | Plain model wins low; thinking wins medium; collapse at high | c14 | Cont (design critiques) |
| Stop on agreement | ESC: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CSQA -78.5%, Coin Flip -84.2%, Last Letters -67.4%; Adaptive-Consistency up to 7.9x fewer samples, under 0.1% mean accuracy loss, 17 datasets | d07, d08 | Est |
| Confidence-weighted voting | CISC over 40% fewer samples (9 models, 4 sets); Gemma2-9B MATH 8 samples beat 30. Within-question discrimination: P(True) 62.3, response prob 59.0, verbalised 0-100 56.1, binary 52.2. Saving at 10 samples: P(True) 46%, binary 10% | c09, d05 | Single group |
| Verifier vs resampling at equal compute | GenRM matches voting only at about 8x compute; 128x for +3.8% | d09 | Single |
| Sound verifier beats LLM verifier | Blocksworld N=100: none 40%, LLM verifier 55%, sound 88%; LLM called 38 of 45 invalid plans valid (84.5%). Graph colouring: base 16%, LLM self-verifier 1/100, sound about 40% | d14, d15 | Est (2 papers, same lab) |
| Feedback content barely matters | Binary, single-error, full-error equal at about 40%; verifier-as-stopper same 40% | d15 | Single |
| Reflexion depends on false positives | HumanEval Python 80 to 91 (1.4% FP); MBPP Python 80 to 77 (16.3% FP) | d13 | Single |
| CRITIC tool gain small on math | GSM8K: tool 72.2 (+2.1), no tool 68.3 (-1.8), oracle 77.4; TabMWP no-tool +20.3 | d12 | Single |
| Self-Refine gains on style tasks | About 20% average, 7 tasks | a26 | Cont vs a17 |
| "Wait" extension | s1-32B AIME24 50.0 to 53.3 (1x, 2x) to 56.7 (4x), 30 items; Ghosal: R1-Distill-1.5B GSM8K -11.8% from 385 to 16,000 tokens, parallel +10.1% | d16, d17 | Cont |
| Removing reflection tokens | Chains -27% to -51%, no utility loss, 10 benchmarks, 5 model series | d18 | Single; abstract level |
| Difficulty-based allocation | About 4x less compute than best-of-N; difficulty estimate costs 2,048 samples, not charged | d21 | Single |
| Overthinking in agents | SWE-bench Verified, 4,018 trajectories; o1 high 29.1% ($1,400) vs low 21.0% ($400); lowest-score of k=2 low runs 27.3% at 43% less cost; k=3 30.3% | d22 | Single |
| Learned when-to-think | AdaptThink length -53.0%, accuracy +2.4% (1.5B); second model -40.1% | c19 | Single; needs RL |
| Bandit meta-controller | Meta-Reasoner GPT-4o-mini SciBench 60.32/73.64/80.23 vs CoT 33.12/55.71/58.10 (column meaning unverified) | c15 | Single; unverified |
| CRT in GPT family | 150 tasks; correct: davinci-003 5%, ChatGPT-3.5 59%, GPT-4 96%, humans 38%; intuitive: 80%, 15%, 0%, 55%; chain of thought in 97% and about 85% | a13, b23, c13 | Single; contamination risk |
| Humans over-trust LLM text | Longer explanations raise confidence, not accuracy; 350 questions, GPT-3.5 55%, PaLM2 50% | a16, b27, c17 | Single; Human users |
| Skill-label exemplars help math | Exact gain not extracted | a25, c22 | Single |

## 4. Mechanisms and models

### 4.1 The two-level loop

```
object level:  produce answer A0 (fast)
meta level:    FOR = f(fluency, conflict, familiarity)
               if FOR >= criterion:  accept A0
               else:                 rethink for time T(FOR); maybe change answer
               at each interval:     intermediate confidence C_t
               stop if C_t >= crit(t)        # criterion decays with t
               or if progress stalls         # give up
```

An engineer reads this as a gate with a signal, a threshold and an action. The human threshold is not fixed: the Diminishing Criterion, `crit(t) = c0 - k*t` with a floor. Humans end as low as 20% confidence (a04). In our agent the floor is a design parameter.

### 4.2 Cue-based FOR and why it fails

FOR is a function of cues, not of correctness. Fluency and familiarity push it up. Conflict pushes it down (a03, a07). Failure modes:
- Fluent wrong answer: high FOR, no rethink. In CRT, wrong answers kept confidence 6.82 of 9 (b09).
- Real conflict missed: 28.9% of biased reasoners raised confidence (a10).
- Fake conflict: reasoners cannot tell real from spurious conflict, so rule use can be over-applied (b06).

Implementation note: do not trigger on "the answer came easily". Trigger on conflict: a second independent method or sample disagrees.

### 4.3 Machine monitoring signals, by access needed

| Signal | Needs | Evidence | Note |
|---|---|---|---|
| Answer agreement across k samples | API only | d07, d08, d23, d25 | Stop when a window agrees; 34-84% fewer samples at under 0.1% mean loss (older models) |
| Relative length of the chain | API only | d19, d20 | Longer than sibling chains means likelier wrong |
| Trial answer plus its token confidence (DEER) | logprobs | c05 | Force an answer at a transition point |
| Token confidence (group or tail) | logprobs | c07 | Can be confidently wrong |
| Self-certainty (distance from uniform) | logits | d06 | Numbers not extracted |
| Hidden-state probe | white box | c01, c06, d24 | AUROC above 0.7; OOD saving falls to 20% |
| P(True) on own sample | prompt | a14, d05 | Best within-question discrimination among prompted signals (62.3) |
| Verbalised 0-100 or binary confidence | prompt | b21, d05 | Overconfident; weak (AUROC about 0.52-0.63) |

CISC lesson (d05): choose the signal by how well it separates right from wrong answers to the same question, not by calibration. Binary verbalised confidence had the best ECE (0.005) and the smallest saving (10%).

### 4.4 Stopping rules to implement

1. Agreement stop (ESC): sample in windows of w; if a whole window gives one answer, stop; else continue to a cap (d07).
2. Adaptive-Consistency: keep Dirichlet counts of answers; stop when the posterior that the leader is the true majority passes a bound (d08).
3. Answer convergence: probe the answer at intervals; stop when it has not changed for m probes (d23).
4. DEER: at each reasoning transition, force a trial answer; if mean token probability of the trial answer exceeds a threshold, stop and use it. Threshold is empirical per task (c05).
5. Certaindex: stability of intermediate answers gates; easy requests exit early, hard ones get more tokens (d25).
6. Thought calibration: conformal risk bound on a probe score; the guarantee holds only if test data match the calibration set (d24).
7. Short-m@k: run k chains in parallel, take the first m finished, vote or pick the shortest (d20).

All were tuned on math. Thresholds shift out of distribution (c06: 60% to 20%).

### 4.5 Control actions beyond stop

Meta-Reasoner (c15): a contextual bandit reads a short progress report and picks continue, backtrack, switch method or restart. TIP (b25) is the opposite control: penalise switching tokens so the model finishes a line. Both are simple to prototype: the progress report is one model call; the bandit is a table.

### 4.6 Why intrinsic review fails and external review works

Same-model review has no new information about correctness. The model cannot find its own errors (a18: about 53%) and changes right answers to wrong more often than wrong to right (a17). The gain of a loop tracks the false-positive rate of its accept test: sound verifier 88% vs LLM verifier 55% (d14); Reflexion gains at 1.4% false positives and loses at 16.3% (d13). Part of the loop gain is resampling: feedback content did not matter in graph colouring (d15). So every review loop must be compared with plain best-of-k at the same tokens.

## 5. What holds up

**Replications and support (human).**
- FOR to rethink link: four experiments in 2011, extended by Thompson and Markovits 2025 (N=289) and the output-vs-generation study (d03). All in one research tradition. No independent-lab replication and no pooled effect size found. Sound but not fully independent (d01, d02, d03).
- Fast, correct first answers: Bago and De Neys 2017 (four experiments), supported by Raoelison 2020 (a12). Two task types only.
- Overconfidence of wrong answerers on conflict items: Mata 2023 (four studies, three countries, lab and online; b09, b10). Boundary: "as confident as correct" holds in Studies 1-2 only.
- Conflict detection: Frey 2018 (three studies) and a 2023 moderate base-rate study found detection common (a10, b12). A 2025 study (N=248) found detection effects vanish once believability and chosen response are controlled (b13). Contested. Detection is less reliable for syllogistic and conditional items than for base-rate and CRT items.

**Failures and tensions.**
- Autism and CRT: no group difference in Morsanyi and Hamilton 2023 (b08) vs more deliberative answers in Brosnan and Ashwin 2023 (74 autistic, 132 control; b16). Minor for us.
- Actively open-minded thinking predicts bias performance but not myside bias (b07).
- The default-interventionist account is weakened by Bago and De Neys, Trippas et al., and the hybrid view (a11, b11, a27).

**Moderators.**
- Cue validity depends on the task (b02).
- Format: screen lowers answer change; meta-reasoning accuracy lower on screen only in multiple choice (b15, N=34).
- Task type for LLM review: style tasks gain (Self-Refine about 20%), verifiable reasoning loses (a26 vs a17). Not tested head to head.
- Domain for early exit: math and science -61.5% length, code -19.9% (c05).
- Distribution: stop savings fall from 60% to 20% out of distribution (c06, d24).
- Model type: blind spot 64.5% in non-reasoning models, smaller in reasoning models (c16). Reasoning models state confidence better (c08).

**Interventions that worked.**
- Agreement-based stopping (d07, d08).
- Trial-answer confidence early exit (c05), probe early exit (c01), thought calibration (c06).
- A sound external verifier or tool (d14, d15, d12).
- Appending "Wait" to cut the blind spot 89.3% (c16, non-reasoning models).
- Shortest-chain preference (d20).
- Thought-switch penalty (b25: 38.3 to 44.1).
- Self-training on first solutions (c04) and AdaptThink RL (c19); both need training.
- Matching explanation wording to model confidence helps human users (a16).

**Interventions that did not work or were weak.**
- Intrinsic "review your answer" (a17).
- Same-model verifier (d14: 84.5% false positives; d15: 1 of 100).
- Verbalised confidence as a failure predictor (b21).
- Blind "Wait" at equal tokens lost to parallel sampling (d17), though s1 gained on 30 AIME items with more tokens (d16).
- Aggressive confidence filtering can hurt: DeepConf Qwen3-32B BRUMO25 -0.9%; HMMT25 88.9 vs 92.9 (b26, a23).
- Calibration (ECE) as the criterion for picking a trigger signal (d05).

**Weak spots in the evidence base** (critique.md). Thompson 2011, 2013 and Thompson and Johnson 2014 were not opened in full. No registered replication of the two-response paradigm. c15 table numbers were not re-checked. Several LLM papers are abstract-level (c18, c21, d18). The search quota ran out during the gap pass, so 2026 coverage is thin.

## 6. Language models

**Calibration and self-knowledge.**
- Pre-RLHF large models (52B) are calibrated on multiple choice and true/false; P(True) on their own samples rises with size and with seeing many samples. Out of distribution it is poor (a14, b20). RLHF models are miscalibrated on logits unless temperature is tuned (b20).
- Black-box verbalised confidence, 2023 models: mostly 80-100%; ECE above 0.377 for GPT-3, GPT-3.5, Vicuna; GPT-4 AUROC 62.7%; GSM8K with GPT-4 (93.6% accurate) reached ECE 0.064 yet AUROC stayed near 0.5 on average (b21, a15). About 22.2% AUROC gain from GPT-3 to GPT-4.
- Tian 2023: for RLHF chat models, stated confidence beat token probability on factual QA, cutting ECE about 50% relative (d10). Factual QA, not reasoning.
- Reasoning models: strictly better verbalised calibration than non-reasoning twins in 33 of 36 settings; the gain comes from slow-thinking behaviours (c08).

**Self-correction.**
- Intrinsic review fails on 2023 models (a17). A retest on current models is missing.
- Kamoi's survey: no prior work shows reliable self-correction from prompting alone on general tasks; it works with reliable external feedback or decomposable output (d11).
- The blind spot: the same error is fixed if attributed to the user, missed if attributed to the model (c16). Cause traced to training data lacking error-correction sequences.

**Machine FOR.** Reasoning models hold a correctness signal and do not use it to stop (c01, c02: "reasoning models do encode a notion of correctness yet fail to exploit it"). Probes: AUROC above 0.7 in distribution; above 0.9 on AIME for the 32B model. Probes do not generalise from logic to math (c01).

**Overthinking.** o1-like models used 1,953% more tokens than conventional models on 2+3; the first round is right in over 92% of cases (a19, b24). Su et al. (d19): per question, accuracy rises with length then falls; wrong answers are longer; models overthink easy items and underthink items beyond reach. Gema et al. (a24): longer reasoning hurts on distractor, spurious-feature and framing tasks. Shojaee et al. (c14): three regimes; near collapse models cut thinking although budget remains. Later critiques question puzzle design and output limits.

**Underthinking.** Wrong answers carry +225% tokens and +418% thought switches; over 70% of wrong responses held a correct thought (a20).

**Agents.** On SWE-bench Verified, overthinking (thinking rather than acting on feedback) goes with fewer resolved issues; reasoning models score about three times higher (d22). The remedy tested was post hoc selection, not a live stop signal.

**What changed the numbers.**

| Intervention | Change | Model and task | Id |
|---|---|---|---|
| Trial-answer early exit | -19.1% to -80.1% length, +0.3 to +5.0 acc | 11 models, 10 benchmarks | c05 |
| Probe early exit | up to -24% tokens, no loss | R1-distill, QwQ | c02 |
| Agreement stop | -34% to -84% samples, under 0.1% loss | 2023 models, 17 sets | d07, d08 |
| Confidence-weighted vote | over 40% fewer samples | 9 models, 4 sets | d05 |
| Short-chain selection | up to +34.5% vs longest | open reasoning models | d20 |
| Thought-switch penalty | pass@1 38.3 to 44.1 | QwQ, AIME24 | b25 |
| Self-trained brevity | -48.6% tokens, same accuracy | QwQ, MATH500 | c04 |
| AdaptThink RL | -53.0% length, +2.4% acc | R1-Distill-1.5B | c19 |
| Sound verifier | 40% to 88% | GPT-4, Blocksworld | d14 |
| "Wait" at equal tokens | -11.8% vs parallel +10.1% | R1-Distill-1.5B, GSM8K | d17 |
| Intrinsic review | CSQA 75.8 to 41.8 | GPT-3.5 | b22 |
| Self-written tests, false positives | 80 to 91 (1.4% FP) vs 80 to 77 (16.3% FP) | GPT-4 Reflexion | d13 |

**Caveats.** Almost all 2025 results are math. Methods differ in models and benchmarks, so savings are not comparable head to head (c25). Open weights dominate; API-only agents lack logits and hidden states.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Doubt only on an external or agreement signal; never on a blind "are you sure".** Part G1 (confirms existing text). [E] K02, K08, K26. Ids a11, a17, b22, c12, d11, d12, d14, d15. A second pass may change an answer only if a check fails or independent samples disagree.
2. **Prefer a sound external accept test; treat same-model review as a weak extra candidate, never a judge.** Part O-review, G2. [E] K26. Ids d11, d12, d14, d15.
3. **Agreement across a few cheap samples is the default trigger and stop signal.** Part G1, S6. [E] K15, K30. Ids d07, d08, d23, d25.
4. **Relative chain length is a free secondary flag: an attempt much longer than its siblings is suspect.** Part G1, S6. [E] K30. Ids d19, d20. A flag, not a verdict (length also tracks difficulty).
5. **Never use self-stated confidence, or how easy an answer felt, as the only trigger.** Part G1. [E] K03, K11. Ids a03, b02, b09, b10, b21, c11.
6. **Cap thinking on easy items; stop after the first verified solution.** Part S6, G11. [E] K16. Ids a19, b24, c03, c04, d19, d22.
7. **Re-tune stopping thresholds per task family; do not carry a math threshold over.** Part S6. [E] K33. Ids c06, d24, d25.
8. **Finish a line of attack before switching operators at S6.** Part S6. [E] K17 for the principle (ids a20, b25, d19); our implementation is untested (see U-list).
9. **Score any trigger by what the agent answered, not by item type.** Part G1, evaluation rule. [C] K05, ids b13, d04. Cheap, so keep.
10. **Compare every rethink step with plain k-sample voting at equal tokens.** Part G7. [E] by design. Ids d09, d15, d17.

### Test first

| Item | Part | Status | Ids |
|---|---|---|---|
| Gated rethink (only when samples disagree or check fails) vs always vs never | G1, S6 | [C]/[S]; no three-way study | K01, K15, d07, d08 |
| Own answer framed as a third party's before review | O-review | [S] | K10, c16 |
| Trial answer plus its confidence at transition points (DEER style) | S6 | [S]; logprobs needed | K15, c05 |
| P(True) on own samples as within-question ranker | G1 | [S] | K12, K29, a14, d05 |
| Diminishing-criterion stop vs fixed threshold | S6 | [E] in humans, untested in LLMs | K07, a04 |
| Initial solvability probe (short first pass, agreement as difficulty) | S0, G12 | [S] | K31, d21, d19 |
| Progress-report controller | S6 | [S], numbers unverified | K19, c15 |
| Blind or gated "Wait" | O-rethink | [C] | K28, d16, d17, d18 |
| Skill-labelled exemplar retrieval | memory | [S] | K22, a25 |
| Location-given vs blind review | O-review | [S] | K09, a18 |
| Act on feedback instead of thinking in agent loops | G1 | [S] | K32, d22 |
| Stop propensity as a tunable parameter | G6 | [S], human only | K06, b14 |

G6 (never abstain on the first pass) stays: the agent submits its best attempt even when it would give up.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (count setup, probes, rethink and every sample). Same items, same seeds. Report accuracy, tokens, and a paired difference with a bootstrap interval. Items: our word puzzles (verifiable), ARC-style items (checkable on held-out examples), BrainTeaser, and an easy-for-model set to expose overthinking.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Verifiable puzzles, mixed difficulty | (a) never rethink, k samples + vote; (b) always rethink once on the vote winner; (c) gated: rethink only if agreement among 3 samples is below 100% | Accuracy at fixed total tokens; flips right-to-wrong vs wrong-to-right | (c) >= (a) > (b), from a17; (b) flips more right-to-wrong than wrong-to-right |
| T2 | Same | (a) k-sample vote; (b) 3 samples, stop on agreement, spend saved tokens on extra samples for disagreeing items | Accuracy at equal mean tokens; tokens saved on agreeing items | 30%+ tokens saved on easy items, under 0.5 point loss (d07, d08) |
| T3 | Items with a code check | (a) k samples; (b) loop with sound check as accept test; (c) loop with model-written check | Accuracy; false-positive rate of the check | (b) > (a) >= (c); (c) hurts when FP above about 10% (d13) |
| T4 | Items with injected errors | (a) plain re-read; (b) "this answer was written by someone else, check it" | Fix rate on wrong items; damage rate on right items | (b) raises fix rate; watch damage (c16) |
| T5 | Mixed difficulty | Signal comparison on one benchmark: sample agreement, relative length, P(True) per sample, verbalised 0-100 | Within-question and overall AUROC for error prediction | Agreement and P(True) top, verbalised lowest (d05, b21); fills the missing one-benchmark table |
| T6 | Easy items | (a) full run; (b) stop after first verified answer; (c) cap by tier | Tokens per item; accuracy | 30-50% fewer tokens, accuracy unchanged (a19, b24) |
| T7 | Mixed | Fixed agreement threshold vs threshold that falls as budget is spent | Accuracy at equal tokens | Small gain if the Diminishing Criterion carries over (a04) |
| T8 | Mixed | (a) uniform spend; (b) 1-sample solvability probe then allocate; both charged | Accuracy at equal tokens | Gain only if probe cost is under about 10% of budget (d21 did not charge it) |
| T9 | Multi-step, stuck-prone | Fixed S6 policy vs progress-report controller | Accuracy; operator-switch count | Better only if the report is informative (c15) |
| T10 | Items with injected distractors | Think-more vs think-less budgets | Accuracy vs budget curve | Non-monotone curve (a24, d19); find the knee |
| T11 | Tool-using agent loop | Act-on-feedback prompt vs reasoning-first | Resolved rate and cost | Fewer overthinking steps (d22) |

## 9. What does not transfer, and why

- **Human FOR as a felt signal.** Humans have fluency. A model has no retrieval-speed feeling, and fluent text is not a cue of correctness (a16: longer explanations raise human confidence, not accuracy). What transfers is the structure: signal, threshold, action.
- **Fluency manipulations (50/150/300 ms).** No analogue in an API agent.
- **Human opt-out trait (b14).** G6 forbids abstaining on the first pass.
- **Personality and group findings** (autism and CRT, screen inferiority, sex and culture): human-only, no mechanism for agents.
- **Probes and token-level confidence methods** (c01, c06, d24, c07, d06): need hidden states or logprobs. Design hints only; our agent is API-only unless a model exposes logprobs.
- **Training-based fixes** (c04, c19, fine-tuned blind-spot cure in c16): we do not train. Only their diagnosis transfers.
- **Math-only stop thresholds.** Savings fall out of distribution (c06) and on code (c05).
- **Self-Refine gains** (a26) come from preference tasks scored by an LLM judge; they do not carry to verifiable reasoning.
- **Human overthinking as information search** (a06) is not the same as chain length.
- **Cross-paper savings numbers** are not comparable or additive (c25).
- **2023 model results** (a17, b21) may not hold for 2026 models.

## 10. Open questions

1. Does a gate that rethinks only on low agreement beat always-rethink and never-rethink at equal tokens for an API-only agent? No three-way study exists.
2. Exact effect sizes in Thompson 2011 and Thompson and Johnson 2014 are unseen; no independent-lab FOR replication found.
3. Which cheap black-box signal predicts wrong answers best on one benchmark? Agreement, P(True), length and verbalised confidence were never put in one AUROC table.
4. Is there a numeric crossover where external feedback helps and blind review hurts? Best statement now: gain tracks the accept test's false-positive rate (d13).
5. Do blind-spot fixes (third-party framing, "Wait") work on reasoning models at equal tokens?
6. What is the accuracy vs token curve by difficulty for 2025-2026 frontier models?
7. Is overthinking caused by low post-answer confidence or by reward shaping? Only correlational evidence.
8. Do agentic and open-ended tasks show the same pattern, and do stop signals transfer from math? Probe stops dropped from 60% to 20% out of distribution.
9. Does a time-decaying confidence criterion improve LLM stopping?
10. Do open-minded-thinking prompts cut myside bias in LLMs, where humans showed no effect (b07)?
11. Do 2026 models still show the 2023 intrinsic-correction failure?
12. Can a solvability probe before solving pay for itself with its cost charged?
13. Do reasoning models' better verbalised calibration (c08) beat sampling agreement in practice?

## 11. Sources

[V] opened and read (per evidence-file flag). [M] snippet or abstract only.

**Human meta-reasoning**
- [V] Ackerman and Thompson (2017) Meta-Reasoning, TiCS 21(8). https://www.psicologia.ulisboa.pt/wp-content/uploads/2020/03/Ackerman-Thompson-2017.pdf (a01-a06, b01-b04)
- [V] Ackerman and Thompson (2017) chapter. https://meta-reasoning.net.technion.ac.il/files/2023/06/Ackerman-Thompson-2017 (a07; URL truncated in the evidence file, see a07 for the full path)
- [V] Thompson (2009) Dual-process theories: a metacognitive perspective. https://meta-reasoning.net.technion.ac.il/files/2017/09/Thompson-2009 (a08; URL truncated in the evidence file)
- [M] Thompson, Prowse Turner and Pennycook (2011). https://pubmed.ncbi.nlm.nih.gov/21798215/ (a09, c24, d01; abstract only)
- [M] Thompson and Markovits (2025). https://pubmed.ncbi.nlm.nih.gov/40063326/ (d02)
- [M] Response generation influences FOR (2023). https://pubmed.ncbi.nlm.nih.gov/36744588/ (d03)
- [V] Frey, Johnson and De Neys (2018). http://www.wdeneys.org/data/QJEP%20preproof.pdf (a10)
- [V] Bago and De Neys (2017). http://www.wdeneys.org/data/Fast_logic%20reprint.pdf (a11)
- [M] Bago and De Neys snippet. https://publications.ut-capitole.fr/id/eprint/44103/ (b19, superseded by a11)
- [V] Raoelison, Thompson and De Neys (2020). http://www.wdeneys.org/data/reprint%20cognition%20smart%20intuitior.pdf (a12)
- [M] Raoelison snippet. https://www.iast.fr/node/102370 (b18)
- [V] Ball and Richardson (2025) editorial. https://pmc.ncbi.nlm.nih.gov/articles/PMC11765846/ (a27, b05-b08; last 13,700 characters unread)
- [V] Mata (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10219213/ (b09, b10)
- [V] Trippas, Thompson and Handley (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5432582/ (b11)
- [V] Moderate base-rate conflict detection (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10136309/ (b12)
- [V] Conflict detection with invalid inferences (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12589286/ (b13); [M] abstract https://pubmed.ncbi.nlm.nih.gov/40244550/ (d04)
- [V] Law, Stankov and Kleitman (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9624363/ (b14)
- [V] Wang et al. (2023) screen inferiority. https://pmc.ncbi.nlm.nih.gov/articles/PMC10033594/ (b15)
- [V] Brosnan and Ashwin (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10291371/ (b16, b17)
- [M] Ackerman and Thompson DOI page. https://doi.org/10.1016/j.tics.2017.05.004 (c23)
- [M] Thompson 2011 DOI page. https://doi.org/10.1016/j.cogpsych.2011.06.001 (c24)

**LLM studies**
- [V] Kadavath et al. (2022). https://arxiv.org/abs/2207.05221 (a14, b20, c10)
- [V] Xiong et al. (2024). https://arxiv.org/abs/2306.13063 (a15, b21, c11)
- [V] Steyvers et al. (2025). https://arxiv.org/abs/2401.13835 (a16, b27, c17)
- [V] Huang et al. (2024). https://arxiv.org/abs/2310.01798 (a17, b22, c12)
- [V] Tyen et al. (2024). https://arxiv.org/abs/2311.08516 (a18)
- [V] Chen et al. (2025). https://arxiv.org/abs/2412.21187 (a19, b24, c03, c04)
- [V] Wang et al. (2025) underthinking. https://arxiv.org/abs/2501.18585 (a20, b25)
- [V] Zhang et al. (2025) probing. https://arxiv.org/abs/2504.05419 (a21, c01, c02, c25)
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895 (a22, c05)
- [V] Fu et al. (2025) DeepConf. https://arxiv.org/abs/2508.15260 (a23, b26, c07)
- [V] Gema et al. (2025) inverse scaling. https://arxiv.org/abs/2507.14417 (a24)
- [V] Didolkar et al. (2024). https://arxiv.org/abs/2405.12205 (a25, c22)
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (a26)
- [V] Hagendorff, Fabi and Kosinski (2023). https://arxiv.org/abs/2212.05206 (a13, b23, c13)
- [V] Shojaee et al. (2025). https://arxiv.org/abs/2506.06941 (c14)
- [V] Sui et al. (2025) Meta-Reasoner. https://arxiv.org/abs/2502.19918 (c15)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (c16)
- [V] Yoon et al. (2025). https://arxiv.org/abs/2505.14489 (c08)
- [V] Taubenfeld et al. (2025) CISC. https://arxiv.org/abs/2502.06233 (c09, d05)
- [V] Kang, Zhao and Song (2025). https://arxiv.org/abs/2502.18581 (c18, d06; numbers not extracted)
- [V] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417 (c19)
- [V] Sui et al. (2025) Stop Overthinking survey. https://arxiv.org/abs/2503.16419 (c20)
- [V] Ji-An et al. (2025). https://arxiv.org/abs/2505.13763 (c21; abstract-level claims)
- [V] Wu et al. (2025) Thought Calibration. https://arxiv.org/abs/2505.18404 (c06, d24)
- [V] Li et al. (2024) ESC. https://arxiv.org/abs/2401.10480 (d07)
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (d08)
- [V] Singhi et al. (2025). https://arxiv.org/abs/2504.01005 (d09)
- [V] Tian et al. (2023). https://arxiv.org/abs/2305.14975 (d10)
- [V] Kamoi et al. (2024). https://arxiv.org/abs/2406.01297 (d11)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (d12)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (d13)
- [V] Valmeekam et al. (2023). https://arxiv.org/abs/2310.08118 (d14)
- [V] Stechly et al. (2023). https://arxiv.org/abs/2310.12397 (d15)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 (d16)
- [V] Ghosal et al. (2025). https://arxiv.org/abs/2506.04210 (d17)
- [V] Wang et al. (2025) NoWait. https://arxiv.org/abs/2506.08343 (d18; abstract-level numbers)
- [V] Su et al. (2025). https://arxiv.org/abs/2505.00127 (d19)
- [V] Hassid et al. (2025). https://arxiv.org/abs/2505.17813 (d20)
- [V] Snell et al. (2024). https://arxiv.org/abs/2408.03314 (d21)
- [V] Cuadron et al. (2025). https://arxiv.org/abs/2502.08235 (d22)
- [V] Liu and Wang (2025). https://arxiv.org/abs/2506.02536 (d23)
- [V] Fu et al. (2024) Certaindex. https://arxiv.org/abs/2412.20993 (d25)

Corrections from critique.md applied: GPT-4 GSM8K oracle is 95.5 to 97.5 (84.3 is GPT-3.5); white-box AUROC 0.605 vs black-box 0.522; Xiong used five task types and eight tasks; the two "74.7%" figures mean different things; GPT-4 chain-of-thought share is "about 85%"; Tsui's arXiv id is 2507 although dated 2026. The critique pass re-opened Xiong, Huang, Hagendorff, DeepConf, Chen, Wang, Zhang, Tsui, Frey and Bago and De Neys. Numbers for a24, a25, c15, c19 and b27 were not re-extracted.
