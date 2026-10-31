# Human error and recovery: deep document

*Subfield E13.07 of cognitive systems engineering. Why errors occur and how they are caught. Key works: Reason, Hollnagel CREAM. Schema link: guardrail G2 (revise only from real output) and state S5 (revise). Built from evidence_a-d.jsonl (about 103 lines, many are the same paper read twice), claims.jsonl (K01-K32) and critique.md in this folder. Evidence ids below (a01, b13, d25 ...) point to those files. Duplicate reads are not independent sources.*

**Reading warning.** The founding human-error theory (Reason 1990, Rasmussen 1983, Hollnagel 1998 CREAM) was NOT read at source. Its numbers are recalled or second-hand and are marked unverified. The LLM evidence is far stronger than the human-theory evidence. Almost all LLM self-correction results come from GPT-3.5, GPT-4, PaLM 2 or small open models. Claude-class models are barely tested.

---

## 1. What it is

Human error research asks two linked questions.

1. Why do competent agents make errors? (Causes: slips, lapses, mistakes, violations, bad context.)
2. How are errors caught and repaired before harm? (Detection, identification, recovery.)

Key terms:

- **Slip**: the plan was right, the action went wrong. Execution failure. Example: pouring juice in a mug.
- **Lapse**: a memory or storage failure. A step is forgotten.
- **Mistake**: the plan itself was wrong. Rule-based or knowledge-based failure. Diagnosis errors are mistakes.
- **Violation**: a deliberate deviation from a rule. In aviation line observation, more than half of errors were violations (b16, d19).
- **Active failure**: an error by the front-line operator. **Latent condition**: a hidden weakness in the system (design, schedule, tools) that waits for an active failure.
- **Detect, identify, recover**: three separable steps. You can detect that something is wrong without knowing what, and you can identify the error without recovering from it (a04, Sellen and Norman).
- **Genotype / phenotype** (Hollnagel): the cause behind an error versus the observable error form.

Why it matters for our agent. Our agent is one language model run through a scaffold. It makes errors. The scaffold decides when to look for errors and what to do with a finding. Guardrail G2 says: revise only from real output, located by code, never from the model's opinion. This document tests that rule against 40 years of human work and about 3 years of LLM work. The short answer: G2 stands. The human work explains why (people also cannot see their own diagnosis errors). The LLM work measures it (self-review without a real signal is flat or negative).

The field also gives a design lesson. Errors are routine in expert systems. Safe systems manage errors with layered defences and fast detection. They do not hope to eliminate them (b14, b16, d19).

---

## 2. History and theories in depth

### 2.1 Slips and action schemas (Norman 1981)

Norman (a01, opened) built an action-schema theory from about 1,000 slip incidents, about 200 from his own collection.

- An intention activates a parent schema. It activates child schemas. Each has an activation value and trigger conditions.
- A slip happens when the wrong schema is activated or triggered.
- Three classes: errors in forming the intention (mode errors, description errors); faulty activation (capture, data-driven and associative activation, loss of intention, misordering); faulty triggering (spoonerisms, blends, intrusions, premature triggering).

On detection (a02): a slip is caught only if the monitor becomes aware of a gap between intention and act. Many slips are caught early by the doer. Omission slips (forgot to do something) are hardest to catch because nothing signals them. Limit: the corpus is collected anecdotes. Norman notes that catch information was mostly not recorded, so there is no catch rate.

### 2.2 Skill, rule, knowledge (Rasmussen 1983) and GEMS (Reason 1990)

Rasmussen's SRK framework: behaviour runs at skill, rule or knowledge level. Error types differ by level. Knowledge-based errors arise in unfamiliar situations with no stored rule (a09). Reason's GEMS (generic error-modelling system) builds on this. Slips and lapses are execution or storage failures. Mistakes are planning failures at the rule or knowledge level. Reason adds violations and latent conditions (a03).

Status: a03 and a09 were not opened. The framework is cited here through Blavier et al. (2005), which was opened. Reason's 1979 diary figures (433 slips, 35 people, storage failures about 40%) are from memory and unverified. Do not cite them. A diary replication that was opened (d24) found N=189 healthy volunteers, mean 6.4 slips per person per week (SD 4.9), slips not linked to perceived stress and only weakly to a memory-failures questionnaire. It does not give Reason's original counts.

### 2.3 Detection research (Sellen, Allwood, Blavier)

Sellen (1994, a07) built a diary corpus of nearly 600 slips and mistakes (abstract page only was read). Blavier et al. (2005, a04-a06, opened) review the field:

- Three detection routes (Reason): self-monitoring, the environment (forcing functions, limiting functions), another person.
- Sellen's taxonomy: action-based detection (plan versus executed action), outcome-based detection (expected versus actual outcome), limiting functions (a physical block).
- Slips are mostly caught through the action. Mistakes can be caught only through the outcome. Internal mismatch can only pick out slips.
- Diagnosis errors usually need an outsider, a "new mind" (Woods 1984, Nyssen 1997 as quoted). Operators fixate on their own picture of system state.
- Doireau et al. (1997), as quoted by the review: self-detected errors were recovered in about 90% of cases, third-person detection in about 30%. Outsiders do better if they are domain experts, if the error is a mistake not a slip, and if detection is close in time.
- Allwood (1984, a08, not opened): four types of error-evaluation episode (affirmative evaluation, standard check, direct error hypothesis, error suspicion). Better solvers caught more of their own errors through spontaneous triggers.

The 90% versus 30% pair is second-hand from a French study that was not opened. Treat it as direction only.

### 2.4 System approach and Swiss cheese (Reason 2000)

Reason (a11, b14): the person approach blames individuals. The system approach assumes people are fallible and asks how defences failed. Layered defences each have holes (active failures and latent conditions). Accidents happen when holes line up. About 90% of aviation maintenance quality lapses were judged blameless. The paper is conceptual and gives no error-rate data for medicine.

Critique: Perneger (2005, b15): 85 safety-literate respondents, mean 15.3 of 23 items "correct" (66.5%) against 11.5 by chance. Only 30.6% placed active error as a hole. 20.0% read "hole" as unsafe act. 89.4% chose "plugging a hole" as the remedy, only 31.8% "adding a slice". The model is read inconsistently. Self-selected sample, ad hoc questionnaire.

### 2.5 Error management in the field (Helmreich 2000)

LOSA line observation (b16, d19, full text opened): more than 3,500 flights, on average two threats and two errors per flight. Terrain was a threat on 58% of flights, weather on 28%. More than half of the errors were violations. Crews that violated procedure were 1.4 times as likely to commit other errors. About 70% of aviation accidents are attributed to human error (NASA, as quoted). 30% of ICU staff in one US teaching hospital denied committing errors. No detection or trapping rate and no slip/lapse/mistake split in the text. Lesson: manage errors, do not expect none.

### 2.6 Human reliability analysis: HEART, CREAM, SPAR-H

- **HEART** (Williams 1986, a12, via a secondary page): nominal error probability for a task type, multiplied by error-producing-condition factors. Example: nominal 0.003 with five conditions gives about 0.27. Conditions are assumed independent. Condition data were never fully published.
- **CREAM** (Hollnagel 1998, a10, not opened): four cognitive functions (observation, interpretation, planning, execution); nine common performance conditions; four control modes (scrambled, opportunistic, tactical, strategic); 13 generic failure types. Context drives error. Error is a result of context, not a stable trait. Interval figures per control mode were seen only in secondary summaries (d23): strategic 0.5E-5 to 1E-2, tactical 1E-3 to 1E-1, opportunistic 1E-2 to 0.5, scrambled 0.1 to 1.0. The intervals overlap, so a mode gives only a coarse band. The source tables were images. Unverified.
- Comparison studies: on one lab task of 14 actions with 23 students, CREAM mean HEP was 0.062 (range 0.003-0.196) and SPAR-H 0.384 (0.044-0.867), about six-fold apart (d20). Neither was checked against observed errors. A Bayesian CREAM variant gave 0.03-0.09 against basic CREAM 0.01-0.02 (d21), validated only against CREAM itself, with inconsistent reporting.
- KRAIL (a30) uses LLMs with a knowledge graph to estimate human error probability. That is LLMs serving human reliability analysis, not a test of LLM errors.

### 2.7 Neuroscience of detection (Yeung and Summerfield; Danielmeier and Ullsperger)

Evidence accumulation account (b19, d18): after a wrong choice, later evidence drifts toward the correct option. Detection happens as evidence keeps arriving after the response. Error negativity appears within about 100 ms and a positivity 200 to 400 ms later tracks explicit awareness. In antisaccade tasks people corrected all errors but detected only about half, so detection and correction come apart. Changes of mind go more often from wrong to right than right to wrong.

Post-error slowing (b17, b18): 59 ms at a 200 ms interval, 11 ms at 750, -9 at 1500, -1 at 3000 (n=19, flanker). Accuracy after errors unchanged. Correlation of slowing with accuracy gain r=0.25, p=0.28. Three rival accounts: cognitive control, orienting, motor inhibition. Lorazepam removed the accuracy gain but left slowing intact (second-hand).

### 2.8 The LLM turn (2023 onward)

From 2023 the same questions were asked of language models: can a model find and fix its own errors? The arc:

1. 2022-23: papers (Self-Refine, Reflexion, RCI, debate) reported large gains from self-feedback.
2. Late 2023: Huang, Tyen, Stechly, Valmeekam showed the gains came from oracle labels, weak first prompts, unequal compute, or from the model being handed the answer to "was this wrong?".
3. 2024: Kamoi survey; Liu partial rebuttal; training-based fixes (SCoRe).
4. 2025-26: reasoning models, the self-correction blind spot (Tsui), correlated errors (Kim), failure attribution in multi-agent logs (MAST, Who&When).

---

## 3. Core findings with exact numbers

Status: **established** = at least 2-3 independent sources, opened. **single** = one source. **contested** = sources disagree. **human-only** = not tested on models.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Slips need a plan-vs-act mismatch signal to be caught; omissions are hardest | about 1,000 incidents; no catch rate | Norman 1981 (a01, a02) | single, anecdote corpus, human-only |
| Self-detected errors recovered more often than third-person ones | about 90% vs about 30% | Doireau 1997 via Blavier 2005 (a04, a05) | single, second-hand, human-only |
| Slips caught through action; mistakes only through outcome or an outsider | taxonomy from about 600 diary errors | Sellen 1994 via Blavier (a06, a07) | single, human-only |
| Errors are routine, managed not eliminated | 3,500+ flights; 2 threats and 2 errors per flight; over half of errors violations; violators 1.4x other errors | Helmreich 2000 (b16, d19) | established, human-only |
| Swiss cheese is read inconsistently | 66.5% match (15.3/23, chance 11.5); 30.6% place active error as hole; N=85 | Perneger 2005 (b15) | single, human-only |
| Humans on a paper check miss half the planted errors | 54.28% missed (SD 22.05), 1.84% false alarms; N=148; 10 planted in 12 trials | Roll 2019 (d22) | single, human-only |
| Detection continues after the response; detect and correct separable | antisaccade: all corrected, about half detected | Yeung and Summerfield 2012 (b19, d18) | established, human-only |
| Post-error slowing does not reliably raise next accuracy | 59 ms at 200 ms; r=0.25, p=0.28; n=19 and 15 | Danielmeier and Ullsperger 2011 (b17, b18) | single, human-only |
| Telling doctors to slow down did not raise accuracy | 44.5% (speed, n=96) vs 45.0% (reflect, n=108); 69 s vs 89 s | Norman 2014 (b20) | contested, human-only |
| Cognitive forcing training did not reduce diagnostic bias | second diagnosis 54% vs 48%, p=0.13; 191 students | Sherbino 2014 (b21) | contested, human-only |
| Checklists: before-after drop | death 1.5% to 0.8% (P=0.003); complications 11.0% to 7.0% (P<0.001); 3,733 vs 3,955 patients | Haynes 2009 (b23) | contested |
| Checklists: population study found none | death 0.71% to 0.65% (OR 0.91, 0.80-1.03, P=0.13); complications 3.86% to 3.82% (OR 0.97, P=0.29); 101 hospitals; 109,341 vs 106,370 procedures | Urbach 2014 (b24) | contested (failed replication) |
| ICU bundle effect | IRR 0.62 at 0-3 months, 0.34 at 16-18 months; 103 ICUs; 375,757 catheter-days | Pronovost 2006 (b25) | single, no control group |
| Intrinsic self-correction lowers accuracy, round by round | GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 GSM8K 75.9 to 75.1 to 74.7 | Huang 2024 (a14, c02) | established |
| With oracle stop labels the same loops look good | GPT-3.5 GSM8K 75.9 to 84.3; CSQA 75.8 to 89.7; GPT-4 HotpotQA 49.0 to 59.0 | Huang 2024 (a13, c01) | established (shows the gain is the oracle) |
| Reasoning models still flip correct answers | right-to-wrong: o1-preview 13.2%, o1-mini 15.6%, R1 7.9%, V3 28.5%, GPT-3.5 34.0%, Llama-3.1-8B 58.8%; o1-preview accuracy 78.7 (down 4.9) | Zhang 2025 (d04) | established |
| Naive revision model flips many correct answers | about 38% of correct MATH answers turned wrong (PaLM 2-S*) | Snell 2024 (d03) | established |
| Sound verifier makes revision pay; LLM verifier does not | Blocksworld 40/100 alone, 55/100 LLM+LLM, 88/100 LLM+sound validator | Valmeekam 2023 (c11) | established |
| LLM verifier accepts invalid plans (corrected figure) | accepted 38 of 45 invalid plans (84.45%), rejected 7 of 45 (15.55%); accepted 54 of 55 valid | Valmeekam 2023 (c11, corrected in critique) | established |
| Graph colouring self-critique collapses | baseline 16%; self-critique 1/100 (single reading); sound verifier about 40%; resampling n=15 about 40%; LLM verifier missed all 40 correct colourings, invented adjacent pairs in 39 | Stechly 2023 (b06, c09) | established |
| Models obey error reports even when false | 94% of mentioned edges changed on a false report (1017/1083); 94% on a true one (1004/1066) | Stechly 2023 (c10) | established |
| Tool feedback gives the gain, not the model's critique | CRITIC HotpotQA EM CoT 33.7, CRITIC 38.7, no tool 34.9, oracle 43.1; own critique alone changed F1 by -0.03 and +2.33 | Gou 2024 (a26, b09) | established |
| Self-Refine fails on math because feedback says all is fine | 64.1 to 64.1; "everything looks good" in 94% of math cases | Madaan 2023 (a25, b10) | established |
| Locating the error is the bottleneck | best 52.87 mistake-finding (GPT-4); with true location +18.04 to +43.92 on wrong traces, 0 to -11.43 on right traces | Tyen 2024 (a16, a17, c07, d28) | established |
| Wrong or random location hurts | random: +5.16 to +21.57 gain, -6.67 to -15.91 loss; break-even at about 60-70% locator accuracy | Tyen 2024 (c08, d28) | single |
| Step-level CoT checking invents mistakes | accuracy on correct traces drops from trace-level to CoT step-level | Tyen 2024 (a18) | single |
| Detectors have low recall; wording matters | recall shifts 16.9 +/- 20.3 points between two wordings; 12 LLMs; 900 instances | Kamoi 2024 ReaLMistake (a21, c21) | established |
| Critique output is prompt-sensitive | Vicuna-13b flags 22.04% wrong with direct critique, 4.8% with CoT; true error rate 51.63% | Lin 2024 CriticBench (a27) | single |
| Reasoning models locate first errors far better | F1 o1-mini 87.9, QwQ-32B 71.5, GPT-4o 61.9, Llama-3.3-70B 58.0; open PRMs 47.9/29.5/24.8 | ProcessBench (a20, b08, c22, d09) | established |
| False-flag rate on correct solutions | o1-mini 2.1/4.9/4.4/8.3; QwQ 4.7/20.7/45.4/32.0 (GSM8K/MATH/Olympiad/Omni) | ProcessBench (d09) | single |
| First-error step accuracy in math word problems | GPT-4-Turbo first-error-step 48.8, reason 46.3, TPR 69.5, TNR 91.8; first step right in 823 of 1,573 (GPT-4), 331 (Claude2), 179 (GPT-3.5) | MR-GSM8K (d29) | single |
| Failure attribution in agent logs is poor | agent 53.5%, step 14.2% | Who&When (a29) | single |
| Self-correction blind spot | 64.5% mean over 14 open non-reasoning models; Wait cuts 89.3%; fine-tune on 5,306 traces cuts 76.0% | Tsui 2026 (a22, b13, d01) | single source |
| Wait recovers reasoning-model level | base / +Wait / reasoning: DeepSeek-V3 0.578 / 0.918 / 0.908; phi-4 0.325 / 0.704 / 0.707; Qwen3-14B 0.121 / 0.884 / 0.843 | Tsui v2 (d25) | single source |
| Wait/budget forcing gains small, then flat | s1-32B AIME24 50.0 to 53.3 at 2x, 56.7 at 4x suppressions; MATH500 93.0 flat; GPQA 57.6 to 59.6; 12 of 30 AIME24 items overflowed | Muennighoff 2025 (c19, d16) | established |
| Repeated Wait then falls | R1-Distill-1.5B GSM8K 82.2 to 87.3 (1,100 tokens) then 70.3 at 15,980; parallel ahead by about 22% at 16k | Wait and think more (d37) | single, preprint |
| Debate does not beat vote at equal responses | GSM8K GPT-3.5: self-consistency 82.5 / 85.3 / 88.2 (3/6/9) vs debate 83.2, 83.0 | Huang 2024 (a15, c03) | established |
| Repair at equal sample budget is near break-even | 1.05x pass@20 and 0.97x pass@22 (APPS, GPT-4); repair success 33.3% own vs 52.6% human feedback | Olausson 2024 (c12, d32) | established |
| Execution feedback beats model-only critique | TransCoder GPT-4 77.3 to 90.4; Codex 80.4 baseline, simple 89.3, unit test 91.6; Spider: 8 samples plus debug beat 32 | Chen 2023 (d36) | established, tokens not controlled |
| Training creates intrinsic self-correction | SCoRe MATH 60.0 to 64.4 (+4.4); right-to-wrong 15.8% to 1.4%; base 52.6 to 41.4 (-11.2); STaR base-data -14.2, STaR+ +0.4 | Kumar 2024 (a24, b04, c16) | established, needs training |
| Fair prompts may rescue intrinsic correction | temp 0 and neutral prompt: GPT-4 CSQA 84.11 to 84.60; biased prompts 66.34 and 72.56; GPT-3.5 HotpotQA 31.00 to 47.00 | Liu 2024 (b12, c20) | contested |
| Reflexion helps with a real signal, hurts with a false one | HumanEval 0.80 to 0.91; MBPP 0.80 to 0.77; false-positive tests 0.01 vs 0.16 | Shinn 2023 (b11) | single |
| Models from different firms share errors | agreement when both wrong 0.60 (chance 1/3, HELM); 0.423 (chance 0.12, HF); 350+ LLMs | Kim 2025 (d12) | established |
| Entangled judges over-endorse wrong answers | rho 0.508 / 0.520 (MMLU-Pro), 0.441 / 0.457 (MATH-500); 18 LLMs, 6 families | Kuai 2026 (d13) | single |
| Many weak verifiers help, with shrinking returns | 87.7% vs 72.7% best single vs 72.2% majority; up to +8.5% with 15 verifiers | Weaver (d30) | single |
| Selecting the right sample is the bottleneck | coverage 82.9% at 100 samples to 98.44% at 10,000; best selection 40.50% to 41.41% | Large Language Monkeys (d31) | established |
| Sample disagreement is a cheap error flag | routing 61.3 to 75.8 (Qwen3-8B, cap 6); risk below 1.5% at 76.1% coverage; self-consistency N=5 AUROC 0.823 | d11, d14, d05 | established for math, small models |
| Multi-agent failure rate and verification share | 41% to 86.7% across 7 frameworks; verification group 21.3%; modes 6.2/8.2/9.1% | MAST (a28, c23) | single |
| Early root-cause error cascades | AgentDebug all-correct 24.3% vs 0.3%; step accuracy 45.0% vs 28.0% | AgentDebug (c24) | single |
| Spontaneous "aha" shifts mark wrong traces | shift in 6.31% of traces; Qwen2.5-1.5B 2.57% correct with shift vs 16.44% without; GPT-4o MATH-500 33.8 vs 65.8 | Illusion of Insight (d07) | contested |
| Self-correction in thinking traces is a modest marker | lift +12.4% (LLM) to +20.1% (VLM); 15 models 3B-9B | Amplified (d06) | contested |
| Planted errors stay in the chain but answers are right | 55-78% of R1 cases end correct with the error left; explicit corrections under 6%; natural faulty chains recover 0.0-1.9% | Decoding critique (d10) | single |
| Probes predict wrong answers from step one | Qwen2.5-3B AUROC 0.953 vs verbalised 0.674; steering only +0.03 to +0.04 | Hidden Error Awareness (d05) | single, white-box |
| Trained critics help humans find bugs | preferred over human critiques in 63% of cases | McAleese 2024 (d17) | single |
| Checklists answered per item beat holistic scoring | TICK exact agreement 46.4% vs 52.2%; STICK InFoBench +6.5, WildBench +7.1 | Cook 2024 (d33), RLCF (d35) | contested for agents |
| HRA tools disagree | CREAM 0.062 vs SPAR-H 0.384 | He 2024 (d20) | established that they disagree |
| Longer reasoning can lower accuracy | Opus 4 Misleading Math near 100% to about 85-90%; R1 five distractors 70% to 30% | Inverse scaling (d27) | single |

---

## 4. Mechanisms and models

Written so an engineer could build each piece.

### 4.1 The error-handling chain: detect, identify, recover

Three separate functions. Build them as separate code steps.

1. **Detect**: is something wrong? Signal sources, ranked by reliability for an LLM agent: (a) a program check that failed (test, validator, type check, constraint); (b) disagreement among independent attempts; (c) a mismatch between a predicted and an executed result; (d) a model critic's flag (weakest).
2. **Identify**: where and what? For code tasks, the failing line, assertion text or diff comes from running the code. For text tasks without a checker, identification is the weak link (Tyen best 52.87%; Who&When step 14.2%).
3. **Recover**: regenerate from the earliest suspect step with the located failure shown. Tyen: given the true location, fixing works (+18 to +44 points on wrong traces).

Evidence: K03, K26. Detection and identification are the bottleneck. Recovery is cheap once located.

### 4.2 Sellen's detection routes mapped to an agent

| Human route | Agent equivalent | Works for |
|---|---|---|
| Action-based (plan vs executed action) | Compare the declared plan step with the tool call actually issued | slips: copy errors, wrong argument, wrong variable |
| Outcome-based (expected vs actual outcome) | Predict the result of a step, run it, compare | mistakes: wrong plan, wrong model of the problem |
| Limiting function (physical block) | Type checker, schema validator, forbidden-state guard in code | any error the block covers |
| Another person | Fresh-context reviewer, different model family, or code | diagnosis errors where the doer is fixated |

Humans catch slips internally and mistakes only via outcome or an outsider (a05, a06). Agent analogue: do not ask the same context to find a wrong plan. Test T2 below.

### 4.3 Why self-review fails: four stacked reasons

1. **No signal**: the model re-reads its text and finds it plausible. Self-Refine feedback said "everything looks good" in 94% of math cases (a25).
2. **Obedience**: when told there is an error, models change the named part, true or false (94% change rate on false edge reports, c10). A false alarm does damage.
3. **Correlation and self-preference**: the critic shares the generator's blind spots (Kim 0.60 agreement on joint errors; Kuai rho 0.44-0.52 over-endorsement). Self-recognition is linked to self-preference (d26, abstract only).
4. **Blind spot** (non-reasoning models, Tsui): the same error is fixed when shown as the user's and ignored when shown as the model's own. Accuracy own vs external: SCLI5 0.499 vs 0.910; GSM8K-SC 0.183 vs 0.881; PRM800K-SC 0.200 vs 0.620 (d01).

### 4.4 Net-gain model of a revise trigger

Let p be base accuracy. The trigger fires on wrong drafts with recall r and on right drafts with false-alarm rate a. A revision turns a wrong draft right with probability g and a right draft wrong with probability f.

Net change in accuracy = (1-p)·r·g − p·a·f.

This is our own bookkeeping, not a published formula. It shows why Tyen's worked example (a17) finds that at very high base accuracy the net can be negative: p is large, so the harm term dominates. Break-even locator accuracy was about 60-70% on BIG-Bench Mistake (c08, d28). Measured f and g: Snell's naive revision model f about 0.38 (d03); Zhang f of 7.9-34% on yes/no tasks (d04); base Gemini on MATH f 15.8%, g 9.5%, SCoRe training f 1.4%, g 14.5% (a24).

Engineering rule: measure p, r, a, f, g on a sample from the task class before turning any revise step on, and keep best-so-far so that a bad revision is discarded by a check.

### 4.5 Layered defence and independence

Swiss cheese arithmetic: if layers fail independently with miss rates m1..mk, the joint miss is the product. LLM layers are correlated. Kim: agreement when both models are wrong is 0.60 on HELM against chance 1/3, and 0.423 on HuggingFace against 0.12; the top pair agrees on 0.9987 of questions both get wrong (d12). The real joint miss is far above the product. Code-based layers (tests, validators) are independent of the model by construction. That is why the scaffold gives code the final say (G5, G10).

Weaver (d30): 15 verifiers give up to +8.5% over the top one, with diminishing returns, because errors on hard examples are correlated and the fit assumes conditional independence.

### 4.6 Evidence-accumulation detection (human model, transferable idea)

People detect errors because evidence arrives after the response and drifts to the true answer (b19). Agent version: after answering, gather NEW evidence (run code, re-derive by a different route, retrieve) instead of re-reading the same text. Test T8.

### 4.7 CREAM as vocabulary

Use CREAM's four cognitive functions as a tag set for errors in traces: observation (misread the input), interpretation (misunderstood), planning (wrong plan), execution (slip). Do not use its probabilities (K23). The numbers disagree across tools by six-fold and were never validated.

### 4.8 Hidden signal that cannot be used

Probes on hidden states predict wrong answers early (AUROC 0.953 vs verbalised confidence 0.674, Qwen2.5-3B), yet steering to fix gives +0.03 to +0.04 (d05). The model "knows" more than it uses, which matches Tsui's blind spot (the ability exists but is not activated, a22). Needs weights. Not usable by an API agent.

---

## 5. What holds up

### 5.1 Replicated and robust

- **Intrinsic self-correction does not help without a signal.** Huang (GPT-3.5, GPT-4, Llama-2), the Kamoi survey of work to May 2024, Stechly, Valmeekam, Zhang (including o1 and R1), Snell, SCoRe base rows. Five independent sources. Same direction across tasks (K01).
- **External feedback is what pays.** Blocksworld 40 to 88, colouring 16 to about 40, code repair 33.3 to 52.6 with human feedback, CRITIC tool vs no tool (K02).
- **Detection and location are the bottleneck; fixing is easy once located.** Tyen, MR-GSM8K, Who&When, AgentDebug, ProcessBench (K03).
- **Models obey critique, even false** (K04).
- **Debate and critique rounds do not beat sampling plus vote at equal responses** (K08).
- **Judges are high-precision, low-recall and correlated with the generator** (K09, K18).
- **Prompt wording moves detection** (K10).
- **Errors are routine in expert systems and managed by layers** (K17, human).

### 5.2 Failed or weakened results

- Self-Refine's math result: zero gain (64.1 to 64.1). Its large gains are on style tasks scored by models (a25, b10). Huang showed part of the CommonGen-Hard gain came from a weak first prompt (44.0 to 67.0 as cited; an improved plain prompt scored above the self-corrected number and the loop then lowered it).
- Reflexion: the gain depends on a pass/fail signal. On MBPP it got worse (0.80 to 0.77) because self-written tests had 0.16 false positives against 0.01 on HumanEval (b11).
- Debate: GSM8K 83.2 and 83.0 against vote 82.5/85.3/88.2 (a15).
- Surgical checklists: Haynes before-after win, Urbach population null (death 0.71% to 0.65%, P=0.13; complications 3.86% to 3.82%, P=0.29). A failed replication at scale. Pronovost has no control group.
- Slow-down in humans: 44.5% vs 45.0% (b20). Cognitive forcing: 54% vs 48%, p=0.13 (b21). Both small; abstracts only.
- Post-error slowing does not reliably improve accuracy (b17).
- CREAM/SPAR-H: six-fold disagreement, no validation (d20, d21).

### 5.3 Contested

- **Huang vs Liu.** Liu (b12, c20) says temperature 0 and neutral prompts make intrinsic correction neutral to slightly positive. Gains are mostly inside noise on single datasets (CSQA 75.92 to 76.00). Huang used temperature 1 for GPT. Not resolved. Both agree prompt wording can swing results by many points (GPT-4 CSQA 84.6 vs 66-73 with biased prompts).
- **Spontaneous self-correction in thinking traces.** d06 reports a positive lift (+12.4 to +20.1%); d07 reports shifts go with much lower accuracy (2.57% vs 16.44%). Likely different definitions and models; difficulty confounds d07 (hard items produce more shifts).
- **Checklists and slow-down in humans** (above).
- **Fixed checklist for agents**: no test. TICK-style checklists are written per item by an LLM.

### 5.4 Moderators found

| Moderator | Direction | Source |
|---|---|---|
| Reliable external signal present | large gain | K02 |
| Base accuracy high | revision net harm likely | a17 worked case; Huang GPT-4 GSM8K 95.5 to 89.0 |
| Locator precision above about 60-70% | revision net positive | c08, d28 |
| Task has decomposable response | exception where self-correction can work | Kamoi (c05) |
| Model is a reasoning model | smaller blind spot, better locating (ProcessBench), fewer flips (R1 7.9%) but not zero | d25, d09, d04 |
| Authorship framing (own vs other's) | large effect for non-reasoning models | d01 |
| Temperature and prompt neutrality | swings results by tens of points | b12, c20 |
| Generator-critic entanglement | more over-endorsement | d13 |
| Critique format (direct vs CoT) | flags 22.04% vs 4.8% | a27 |
| Time to detection, expertise of detector | outsiders better if expert and early | a05 |

### 5.5 Interventions that worked and that did not (LLM)

Worked:

- Sound validator or code-run feedback: Blocksworld 88/100; Self-Debugging GPT-4 on TransCoder 77.3 to 90.4 (d36).
- Tool-interactive checking (CRITIC): F1 gains of 5.6 to 12.4 over baselines with tools (b09).
- Appending "Wait" at the review step in non-reasoning open models: blind spot cut 89.3% (d01).
- Disagreement-guided routing: 61.3 to 75.8 on 7 math benchmarks (d11).
- Training: SCoRe +4.4 on MATH; HumanEval +12.2 vs base +3.0 (b04). Fine-tune on 5,306 correction traces cut the blind spot 76.0%.
- A strong verifier deciding WHEN to refine: +14.6% average for small models (b05).
- Targeted debug feedback at the root-cause step (AgentDebug, c24).
- Item-by-item checklists (TICK, per-instance): +5 to +7 points on instruction following (d33).

Did not work:

- Prompted self-review without a signal (Huang, Zhang).
- LLM verifier (Blocksworld LLM+LLM 55 vs 88; colouring self-critique 1/100).
- Debate rounds.
- Self-consistency or majority vote as an error detector on ReaLMistake (a21).
- Steering from probes (+0.03 to +0.04, d05).
- Prompt-level role fixes in multi-agent systems (+9.4% on ChatDev, c23).
- Burst-aware early exit: no better than a plain length cutoff (d08).
- Repeated Wait past a few uses (d37).

---

## 6. Language models

### 6.1 Self-correction without a signal

| Model and task | Before | After | Source |
|---|---|---|---|
| GPT-3.5 CSQA, 1 to 3 calls | 75.8 | 38.1 then 41.8 | Huang (a14) |
| GPT-3.5 GSM8K | 75.9 | 75.1 then 74.7 | Huang (a14) |
| GPT-4 GSM8K | 95.5 | 91.5 then 89.0 | Huang (a14) |
| GPT-4 HotpotQA | 49.0 | 49.0 then 43.0 | Huang (a14) |
| GPT-4 CSQA | 82.0 | 79.5 then 80.0 | Huang (a14) |
| Gemini 1.5 Flash MATH, prompted base | 52.6 | 41.4 | Kumar (a24) |
| Self-Refine on the same model | 52.8 | 51.8 | Kumar (c16) |
| o1-preview yes/no accuracy | down 4.9 to 78.7 | 78.7 | Zhang (d04) |
| o1-mini yes/no accuracy | down 4.2 to 74.1 | 74.1 | Zhang (d04) |

Right-to-wrong flip rates (yes/no task): o1-preview 13.2%, o1-mini 15.6%, GPT-4o 11.3%, GPT-3.5 34.0%, DeepSeek R1 7.9%, DeepSeek V3 28.5%, Llama-3.1-8B 58.8%, Llama-3-8B 58.2%, Llama-2-7B 26.5% (d04). On one decision-making task o1-mini changed 92.3% of its correct answers to wrong; that is one task, not a general rate. On reasoning tasks the o1-mini / GPT-4o / GPT-3.5 flip rates were 9.1 / 17.9 / 19.7%. Repeating the question and a small fine-tune lowered flips (d04). The paper's delta labels disagree with its tables (flagged in the critique), so use the flip rates.

Fair-setting caveat (Liu): temperature 0 and a neutral prompt may make the loop neutral. Treat the loop as unproven, not as proven harmful in every setting.

### 6.2 With a signal

- Blocksworld GPT-4: 40 alone, 55 with an LLM verifier (3.48 iterations), 88 with a sound validator (4.18). The LLM verifier: accuracy 61/100, accepted 54 of 55 valid plans, and also accepted 38 of 45 invalid plans (an earlier note had this backwards).
- Graph colouring GPT-4: 16% baseline, about 40% with a sound verifier, whether feedback was pass/fail, first error or all errors. Resampling at n=15 matched it. Much of the "feedback" gain is extra tries.
- Code: Self-Debugging with unit-test feedback lifts GPT-4 on TransCoder from 77.3 to 90.4. Most of the gain comes in the first one to three turns. Spider greedy plus debug matches 16 samples (d36). But equal-budget repair (Olausson) is 1.05x and 0.97x of pass@k. Nobody controlled for tokens.
- Human feedback beats model feedback on code repair: 52.6% vs 33.3% repair success. By difficulty: intro 62.21 vs 42.64, interview 45.67 vs 19.33, competition 14.67 vs 3.67 (c12).
- CRITIC (text-davinci-003): HotpotQA EM/F1 CoT 33.7/46.1, CRITIC 38.7/50.5, no tool 34.9/46.1, oracle 43.1/54.5.

### 6.3 Finding errors

- BIG-Bench Mistake (PaLM 2 traces, 5 tasks, 300 traces each, 255 wrong and 45 right): GPT-4 best, 52.87 overall. Tracking shuffled objects GPT-4: 62.29 (direct trace), 65.33 (direct step), 90.67 (CoT step); GPT-3.5-Turbo 10.10, 1.67, 19.00. Logical deduction GPT-4 40.67; multistep arithmetic 44.00. A small trained classifier beat a large prompted model on some held-out tasks (Dyck 33.57 vs 10.98).
- ProcessBench (3,400 cases): o1-mini F1 93.2/88.9/87.2/82.4, average 87.9; GPT-4o 79.2/63.6/51.4/53.5, average 61.9; QwQ-32B-Preview 71.5; Llama-3.3-70B 58.0; Qwen2.5-Math-72B 45.5; PRM800K-trained 56.5; Skywork-PRM-7B 42.1; Math-Shepherd 31.5. False-flag rate on correct solutions: o1-mini 2.1/4.9/4.4/8.3, QwQ 4.7/20.7/45.4/32.0.
- MR-GSM8K: GPT-4-Turbo TPR 69.5, TNR 91.8, first-error-step 48.8, reason 46.3, MR-Score 50.5.
- ReaLMistake: expert F1 95.7; strong models (GPT-4, Claude 3 Opus) have high precision and very low recall; higher LMSYS Elo means higher precision, lower recall; self-consistency and majority vote did not help detection.
- Failure attribution (Who&When, 127 systems): agent 53.5%, step 14.2%. o1 and R1 also fell short.
- CriticBench: critique skill rises about linearly with generation skill. Vicuna-13b flagged 22.04% (direct) vs 4.8% (CoT); true error rate 51.63%.

### 6.4 The self-correction blind spot and Wait

Tsui (a22, b13, d01, d25): 14 open non-reasoning models, injected errors. Average blind spot 64.5%. Wait trigger macro accuracy, SCLI5 / GSM8K-SC / PRM800K-SC: 0.957 / 0.796 / 0.504 (gains +91.9% / +335.1% / +152.0%). "But": 0.922 / 0.611 / 0.430. "However": 0.897 / 0.602 / 0.438. Wait cuts the blind spot 89.3% on average. Base / +Wait / reasoning-model macro accuracy: DeepSeek-V3 to R1-0528 0.578 / 0.918 / 0.908; phi-4 0.325 / 0.704 / 0.707; Qwen3-14B 0.121 / 0.884 / 0.843; Qwen3-32B 0.046 / 0.791 / 0.894; Qwen3-30B-A3B 0.102 / 0.869 / 0.845. On natural errors only 4.3-10.8% of misses are caught when shown externally.

Limits: no Claude, no o1 (closed models excluded because prefix injection was needed); injected errors; fixed 1,024-token budget, temperature 0; single author. The earlier report of Claude 3.5 Haiku 52.5% and Sonnet 4 41.4% blind spot (c17) could not be re-found in v2 and is unverified.

Wait with reasoning models (s1): AIME24 50.0 to 53.3 at 2x, 56.7 at 4x suppressions, AIME25 26.7 to 36.7; MATH500 93.0 flat; flattening near 6x; too many suppressions cause loops. Distilled small models fall after a few Waits: GSM8K 82.2 to 87.3 then 70.3 at 15,980 tokens (d37). The "57" in the s1 abstract needs its budget stated; do not quote it bare.

### 6.5 Spontaneous reflection in reasoning models

- Shifts in 6.31% of traces; formal Aha 1.79%; accuracy lower with a shift in every model tried: Qwen2.5-1.5B 2.57% vs 16.44% (N=723,200), Qwen2.5-7B math 28.2 vs 66.1, GPT-4o MATH-500 33.8 vs 65.8, R1 20.4 vs 54.3. Difficulty confound. Forced reconsideration on math 32.21 to 40.62 (+8.41 pp; 50,574 wins vs 23,500 losses), most where entropy is high (d07).
- Self-correction lift +12.4% to +20.1% across 15 open models 3B-9B; thinking models self-correct in 21-55% of responses vs 3-15% for instruct (d06).
- Planted errors: R1-type models keep the error in the chain in 55-78% of cases and still answer right; explicit correction under 6% (d10).
- Backtracking bursts: wrong traces had mean multi-burst count 4.78 vs 1.90 (AIME24, Qwen3-8B). A plain 12k-word cutoff (80.6 / 71.7) beat the burst-aware policy (79.4 / 69.3) (d08).

### 6.6 Correlated errors and judges

Kim (d12): 350+ LLMs; agreement when both wrong 0.60 (HELM), 0.423 (HF); 100% of HF pairs and 97.5% of HELM pairs above chance; same architecture +0.076, same company +0.066 (HF) / +0.022 (HELM). Kuai (d13): over-endorsement correlates with entanglement (rho 0.44-0.52); de-entangled reweighting +3.5 points accuracy over majority vote. Xu (b07): self-bias in all six LLMs tested; larger models and accurate external feedback reduce it; repeated refinement amplifies it while true quality does not rise.

### 6.7 Detecting wrongness cheaply

- Disagreement routing (d11): accept when two agree; vote when a second pair agrees; rewrite only on severe disagreement. Qwen3-8B 61.3 baseline, majority 68.9, best-of-N 63.4, proposed 75.8; AIME24 majority 50.0 vs 66.7. Uses 40-60% of the six-sample cap on Math500, 70% on AIME24. Rewrite can drop conditions and turn right answers wrong.
- Risk-controlled abstention (d14): selective risk below 1.5% on all 15 splits at 76.1% average coverage; abstract only.
- Semantic entropy (d34): AUROC 0.828 vs 0.802 for length-normalised entropy (OPT-30B, TriviaQA). It does not catch samples that agree on the same wrong answer.
- Coverage vs selection (d31): coverage 82.9% to 98.44% over 100 to 10,000 samples, but best selection 40.50% to 41.41%. 11.3% of SWE-bench Lite problems have flaky tests; 35 of 122 CodeContests reference solutions fail their own tests. Even code checks can be wrong.
- Probes (d05): need weights.

### 6.8 Multi-agent failure

MAST (1,600+ traces, 7 frameworks, kappa 0.88 for annotators, 0.77 for the LLM judge): failure rates 41% to 86.7%. Group shares: system design 41.8%, inter-agent misalignment 36.9%, task verification 21.3%. Modes: premature termination 6.2%, no or incomplete verification 8.2%, incorrect verification 9.1%; disobeying task spec 11.8%; not recognising completion 12.4%. Do not mix group shares with per-mode figures; they use different bases. AgentDebug: all-correct 24.3% vs 0.3% for the strongest baseline; step accuracy 45.0% vs 28.0%; GAIA step accuracy 58.0% vs 30.0%; up to 26% relative downstream gain.

### 6.9 Claude-class models

Almost nothing. Tsui tests none. ReaLMistake included Claude 3 Opus (high precision, very low recall). MR-GSM8K included Claude2 (first step right in 331 of 1,573). Inverse scaling work (d27) found Claude models (Sonnet 3.7, Sonnet 4, Opus 4) lose accuracy with longer reasoning on distractor tasks: Misleading Math Opus 4 from near 100% to about 85-90%; Misleading Python to about 80%; few-shot largely fixes zero-shot declines. No Claude self-recognition or false-pass number was found. This is the main gap.

---

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Keep G2 as written.** A revision starts only from a failing output that code located (test result, assertion, validator message, diff). Never from the model's own opinion that something looks wrong. Reasons: models cannot find their own errors well (52.87 best), obey false reports (94%), and approve wrong work. | G2, S5 | [E] | K01-K04; a16, a17, c10, c11, c09 |
| A2 | **Add a line to G2: reviewer approval is not evidence.** "Looks fine" from the same model or family carries no weight; S8 VERIFY must be a run, not a read. | G2, S8 | [E] | K09, K18; a25, c11, d12, d13 |
| A3 | **Keep S5's keep-best-so-far, and accept a revision only if a check passes.** Wrong or false triggers lower accuracy 7-16 points and an unchecked revision flips 8-38% of right answers. (Keep-best itself is untested; the harm it guards against is established.) | S5 | [E] for the harm | K04; a17, c10, d03, d04 |
| A4 | **Revise from the earliest failing step, not by regenerating everything.** Give the located failure plus the prefix. | S5 | [E] for location; the prefix-restart detail [S] | K03, K26; a17, c24 |
| A5 | **Any model-based critic step uses one fixed, neutral wording**, sees no authorship, no majority and no proposed answer, and is not told to find errors (wording and CoT-vs-direct move detection by tens of points). | G5, S5 | [E] | K10; a21, a27, c20 |
| A6 | **Treat disagreement between independent attempts as a trigger for extra work; never treat agreement as proof.** Fits G1 and G4. | G1, G4, S7 | [E] in math with small models | K21; d11, d14 |
| A7 | **Never stack same-family model reviewers and count them as independent layers.** Count only code checks and different-mechanism checks as independent defences. | G4, G9 | [E] | K18; d12, d13, d30 |
| A8 | **Spend equal tokens on more independent samples with a vote before spending them on critique rounds** (already G9/G11). The evidence base is confirmed. | G9, G11 | [E] | K08; a15, c12, d31 |
| A9 | **Log at S9 the earliest failing step and a four-way tag (observation, interpretation, planning, execution) on every failed run.** Cheap data that every later test needs. | S9, M | cascade [E]; tag set [S] | K26, K32; c24, a29 |
| A10 | **Do not use backtracking count or "wait, let me recheck" in a trace as a quality signal.** | G10 | [C] | K20; d06, d07, d08 |

### Test first (not yet established for our setup)

| # | Candidate | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-located error line plus one model fix vs N resamples with vote, at equal tokens | G2, S5 | [E] direction, equal-token edge unproven | K28, K08; d36, d32 |
| T2 | Fresh-context reviewer (never saw the draft) vs same-context review on slip and mistake seeds | S5, S8 | [S] (human analogy plus indirect LLM) | K13, K09; a05, d12 |
| T3 | Present the earlier answer as a colleague's draft, and/or add a Wait cue, at the review step | S5 | [S] (open non-reasoning models only) | K05, K06, K31; d01, d25, d37 |
| T4 | Revise-trigger precision gate (revise only if locator precision is at least 70%) with keep-best | G2, S5 | [S] | K30; c08, d28 |
| T5 | Fixed 5-item code-run checklist before submit | S8 | [C] | K16, K29; b23, b24, d33 |
| T6 | Same-family joint miss rate of two reviewers vs the product of single rates | G4 | [S] | K27; d30, d12 |
| T7 | Disagreement-guided routing and abstention on our items | G1, G6 | [E] in math; ours unknown | K21; d11, d14 |
| T8 | Post-answer second look that gathers new evidence (re-derive by another route, run) vs re-reading | S8 | [S] human analogy | K14; b19, d18 |
| T9 | Generic slow-down prompt vs a specific consider-the-opposite step at equal tokens (slow-down is already in 4b as not to add; this tests only the specific step) | S1, S5 | [C] | K15; b20, b21, b22 |
| T10 | Slip vs mistake tagging: which defence catches which | S5, S9 | [S] | K32; d29, d24 |
| T11 | Forced pause (a one-line state of what failed) after a failed check vs immediate retry | S5 | [S] | K24; b17 |
| T12 | Own-draft approval (false-pass) rate of our model on seeded wrong drafts | G2 | [S] | K31; d26 |

---

## 8. Concrete tests on our bench

All arms get equal total tokens (count prompt plus completion for every call, setup included). Report n, accuracy, flip counts (right-to-wrong and wrong-to-right), tokens, and 95% intervals. Items need a ground-truth check so flips can be counted.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Located fix vs resample | Code and checkable puzzle items with a test or validator | A: one draft, run, show failing line, one fix, up to 2 rounds. B: plain draft, then N resamples with code selecting by test/vote. C: one draft plus model self-review, no tool | Final pass rate; wrong-to-right and right-to-wrong flips | A at least equal to B (Olausson 0.97-1.05x suggests a tie); C below both. A tie would mean S5 adds nothing over G11 at equal tokens |
| T2 Fresh-context reviewer | Items with seeded slips (copy error, wrong arithmetic, wrong variable) and seeded mistakes (wrong plan, wrong rule) | A: same-context self-review. B: fresh-context reviewer given the task and draft but not the reasoning. C: code check. D: no review | Detection rate on seeded errors; false-alarm rate on clean drafts | C best on both. B above A for mistakes (human outsider effect), about equal for slips |
| T3 Colleague framing / Wait | 60 items with an injected wrong step in the agent's own prior output | A: same-voice review. B: "a colleague wrote this" review. C: append Wait before the review. D: B plus C | Fix rate on injected errors; harm on clean drafts | B and C raise fix rate in non-reasoning settings; little or nothing if the base is reasoning-class. Watch harm on clean drafts |
| T4 Trigger precision gate | Any task class with a candidate locator | Measure precision and recall of the locator on 100 drafts; arms: revise always, revise if flagged, revise if flagged and precision at least 70%; each with and without keep-best | Net accuracy change; flips | Gating wins when base accuracy is above 85%; no gate wins when base is below 50% |
| T5 Fixed checklist | Mixed set (reasoning, code, format-constrained) | A: none. B: 5 code-run checks (answer format, units, constraint count, re-run given examples, empty-output guard) | Pass rate; catches per run | Small gain on format and constraint items, none on reasoning. Human evidence is split, so a null on hard items is likely |
| T6 Joint miss rate | 100 seeded wrong drafts | Reviewer X, reviewer X' (same model, new seed), reviewer Y (other family), code | Miss rates; joint miss of X and X' vs product | Joint miss of X and X' above the product (Kim: correlation). Y and code nearer the product |
| T7 Disagreement routing | Math and checkable items | A: fixed 6 samples plus vote. B: 2 samples, accept if they agree, else grow to 6, abstain on severe split | Accuracy at the same average tokens; wrong answers served | B uses fewer tokens at similar accuracy; abstention cuts wrong answers served. Shared-wrong-belief cases remain |
| T8 Evidence-gathering second look | Items where a second route exists (compute vs estimate; code vs by hand) | A: re-read. B: re-derive by another method and compare. C: run | Catch rate on seeded errors | C above B above A |
| T9 Slow vs opposite | Hypothesis or diagnosis-like items with a known trap | A: "be careful". B: "give one reason your answer is wrong and test it" | Accuracy; flips | A null (consistent with 4b); B small plus or null |
| T10 Slip/mistake split | Our own failed traces (at least 100) | Tag each as slip, lapse or mistake; run T1-T2 arms per tag | Catch rate per tag per defence | Code catches slips; fresh reviewer or resample catches mistakes |
| T11 Pause after failure | Items with a failed first check | A: immediate retry. B: retry after a one-line written state of what failed | Retry success | Likely null (post-error slowing evidence is weak); cheap |
| T12 False-pass rate | 100 known-wrong drafts written by the model itself and 100 by another model | Own-model reviewer, cross-family reviewer, code | Approval rate of wrong drafts | Own-model approval above cross-family (self-preference); both far above code |

Order: T12 and T6 first (measurements that size the problem), then T1.

---

## 9. What does not transfer, and why

- **Slips from fatigue, interruptions and attention capture** (Norman's capture and loss-of-activation slips). LLMs have no attention that wanders in time. The analogue is context drift and copy errors, which have different causes.
- **Post-error slowing, error negativity, motor inhibition.** Human neural and timing effects. A model has no timing signal. The only transferable idea is "evidence keeps arriving after the response", which means "gather new evidence after answering" (T8).
- **Diary-study slip rates** (6.4 per week) and the 90% vs 30% recovery figures. Human numbers do not give model rates.
- **CREAM and HEART probabilities.** They score human tasks by expert-weighted conditions. They disagree six-fold with each other and have no validation (K23). Use the vocabulary only.
- **Surgical and ICU checklist effects.** Those checklists carry teamwork, communication and culture effects (the Pronovost bundle included feedback and culture change). A code-run checklist has none of that. Benefit is untested.
- **Blame and just-culture material.** The person versus system approach matters for organisations. An agent has no blame.
- **Violations** (over half of aviation errors). An agent does not choose to violate. The nearest analogue is ignoring instructions (MAST: 11.8% disobey task specification), which is a spec problem.
- **Training results (SCoRe, fine-tune on correction traces, RL critics, probes and steering).** They need weights. Our agent is scaffold-only. Use them as ceilings (SCoRe +4.4), not designs.
- **Older-model results.** Huang's GPT-3.5 CSQA drop to 38.1 is probably larger than a current model would show. Direction transfers; size may not.
- **Injected-error benchmarks.** Tsui's errors are injected, not natural; on natural errors only 4.3-10.8% of misses are caught even when shown externally.

---

## 10. Open questions

1. Equal-token comparison of a code-located error line plus one fix against plain resampling plus vote. Nobody has controlled tokens (K28).
2. How often does a Claude-class model approve a known-wrong draft of its own, versus a fresh-context or cross-family reviewer? No Claude number found (K31).
3. Does the Tsui effect (colleague framing, Wait) help strong reasoning-class models or only non-reasoning ones? Reasoning models show a small or negative blind spot, but Claude is untested.
4. What is the break-even precision of a revise trigger outside BIG-Bench Mistake, and with keep-best?
5. Joint miss rate of two same-family reviewers. Kim measured error agreement between models, not reviewer joint misses.
6. Which defence catches slips and which mistakes in LLM output? No study splits LLM errors by Reason's classes.
7. Does a fixed code-run checklist beat none for an LLM agent? Human data are split; LLM data use per-item generated checklists.
8. What are Reason's 1979 and 1990 numbers and CREAM's control-mode intervals in the sources themselves? Books not opened.
9. Does Wait keep helping after first use for the model we use? Open models flatten then fall; parallel samples beat repeated Wait.
10. Can agreement signals detect errors when all samples share the same wrong belief? Semantic entropy and the vote plateau imply no; no direct test.
11. Huang vs Liu: how much of the "intrinsic self-correction" null is temperature and prompt wording? A rerun at temperature 0 with neutral wording on current models is missing.
12. Is the 90% vs 30% self-vs-third-person recovery pattern real at source (Doireau 1997 not opened)?

---

## 11. Sources

[V] = opened and read this session (full text, or the page marked). [M] = snippet, summary or recalled only. Duplicate reads of one paper are listed once with all ids.

**Human error and reliability**

- [V] Norman (1981) Categorization of action slips. https://ocw.tudelft.nl/wp-content/uploads/385f43617465676f72 (a01, a02)
- [M] Reason (1990) Human Error, Cambridge University Press. https://www.cambridge.org/core/books/human-error/ (a03; recalled, not opened)
- [V] Blavier, Rouy, Nyssen, de Keyser (2005) Prospective issues for error detection, Ergonomics. https://orbi.uliege.be/bitstream/2268/12486/1/ (a04-a06)
- [V] Sellen (1994) Detection of everyday errors, Applied Psychology 43(4). https://www.microsoft.com/en-us/research/publication/ (a07; abstract page only)
- [M] Allwood (1984) Error detection processes in statistical problem solving. https://doi.org/10.1207/s15516709cog0804_5 (a08)
- [M] Rasmussen (1983) Skills, rules and knowledge. https://doi.org/10.1109/TSMC.1983.6313160 (a09)
- [M] Hollnagel (1998) CREAM. https://www.sciencedirect.com/book/9780080428475/ (a10)
- [V] Reason (2000) Human error: models and management, BMJ. https://pmc.ncbi.nlm.nih.gov/articles/PMC1117770/ (a11, b14; read through a summarising fetch tool)
- [V] Williams (1986) HEART, via https://en.wikipedia.org/wiki/Human_error_assessment_and_reduction_technique (a12; secondary page)
- [V] Perneger (2005) The Swiss cheese model of safety incidents. https://pmc.ncbi.nlm.nih.gov/articles/PMC1298298/ (b15)
- [V] Helmreich (2000) On error management: lessons from aviation, BMJ. https://pmc.ncbi.nlm.nih.gov/articles/PMC1117774/ (b16, d19)
- [V] Danielmeier and Ullsperger (2011) Post-error adjustments. https://pmc.ncbi.nlm.nih.gov/articles/PMC3173829/ (b17, b18)
- [V] Yeung and Summerfield (2012) Metacognition in human decision-making. https://pmc.ncbi.nlm.nih.gov/articles/PMC3318764/ (b19, d18; first 100k of 124k characters)
- [V] Norman et al. (2014) Etiology of diagnostic errors, System 1 vs System 2. https://doi.org/10.1097/ACM.0000000000000105 (b20; abstract)
- [V] Sherbino et al. (2014) Cognitive forcing strategies. https://doi.org/10.2310/8000.2013.130860 (b21; abstract only)
- [V] Croskerry, Singhal, Mamede (2013) Cognitive debiasing 2. https://pmc.ncbi.nlm.nih.gov/articles/PMC3786644/ (b22)
- [V] Haynes et al. (2009) Surgical safety checklist. https://doi.org/10.1056/NEJMsa0810119 (b23; abstract, re-checked)
- [V] Urbach et al. (2014) Safety checklists in Ontario. https://doi.org/10.1056/NEJMsa1308261 (b24; abstract, re-checked)
- [V] Pronovost et al. (2006) Catheter-related bloodstream infection. https://doi.org/10.1056/NEJMoa061115 (b25; abstract only, numbers not re-verified)
- [V] He et al. (2024) Human error in university laboratories, CREAM and SPAR-H. https://pmc.ncbi.nlm.nih.gov/articles/PMC11002268/ (d20)
- [V] Shirali et al. (2019) Modified CREAM with Bayesian network. https://pmc.ncbi.nlm.nih.gov/articles/PMC6384312/ (d21)
- [V] Roll et al. (2019) Human error: job insecurity, attention-related cognitive errors. https://pmc.ncbi.nlm.nih.gov/articles/PMC6651186/ (d22; first 100k of 125k characters)
- [V] Radiogram HRA paper summarising CREAM. https://arxiv.org/pdf/2310.14697 (d23; interval tables were images, so the intervals are [M])
- [V] Replication of Reason's 1979 diary study. https://iris.landsbokasafn.is/en/publications/ (d24; abstract page)
- [V] Xiao et al. (2024) KRAIL. https://arxiv.org/abs/2412.18627 (a30; abstract only)

**LLM self-correction, error finding, verification**

- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (a13-a15, b01, c01-c04)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 and https://arxiv.org/html/2311.08516 (a16-a18, b02, c06-c08, d28)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (a19, b03, c05, d02; full paper not read)
- [V] Kamoi et al. (2024) ReaLMistake. https://arxiv.org/abs/2404.03602 (a21, c21)
- [V] Zheng et al. (2025) ProcessBench. https://arxiv.org/abs/2412.06559 and https://arxiv.org/html/2412.06559 (a20, b08, c22, d09)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 and https://arxiv.org/html/2507.02778v2 (a22, a23, b13, c17, c18, d01, d25)
- [V] Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917 (a24, b04, c16)
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (a25, b10, c13)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (a26, b09, c15)
- [V] Lin et al. (2024) CriticBench. https://arxiv.org/abs/2402.14809 (a27)
- [V] Cemri et al. (2025) MAST. https://arxiv.org/abs/2503.13657 (a28, c23)
- [V] Zhang et al. (2025) Who&When. https://arxiv.org/abs/2505.00212 (a29)
- [V] Zhang et al. (2024) Small models need strong verifiers. https://arxiv.org/abs/2404.17140 (b05)
- [V] Stechly, Marquez, Kambhampati (2023) GPT-4 doesn't know it's wrong. https://arxiv.org/abs/2310.12397 (b06, c09, c10)
- [V] Valmeekam, Marquez, Kambhampati (2023) Can LLMs really improve by self-critiquing their own plans? https://arxiv.org/abs/2310.08118 (c11; verifier-table correction in critique.md)
- [V] Xu et al. (2024) Pride and prejudice: self-bias in self-refinement. https://arxiv.org/abs/2402.11436 (b07; abstract, intro, main findings)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (b11, c14)
- [V] Liu et al. (2024) LLMs have intrinsic self-correction ability. https://arxiv.org/abs/2406.15673 (b12, c20)
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/abs/2306.09896 and https://arxiv.org/html/2306.09896 (c12, d32; first 100k characters)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 and https://arxiv.org/html/2501.19393 (c19, d16)
- [V] Zhu et al. (2025) AgentDebug. https://arxiv.org/abs/2509.25370 (c24)
- [V] Shamsujjoha et al. (2025) Swiss cheese model for AI safety. https://arxiv.org/abs/2408.02205 (c25)
- [V] Snell et al. (2024) Scaling test-time compute optimally. https://arxiv.org/html/2408.03314 (d03)
- [V] Zhang et al. (2025) Dark side of intrinsic self-correction. https://arxiv.org/html/2412.14959v2 (d04)
- [V] Hidden Error Awareness in CoT. https://arxiv.org/html/2605.09502 (d05)
- [V] Amplified Does Not Mean Predictive (2026). https://arxiv.org/html/2608.13760 (d06)
- [V] The Illusion of Insight in Reasoning Models (2026). https://arxiv.org/html/2601.00514 (d07)
- [V] The Shape of Overthinking (2026). https://arxiv.org/html/2605.27965 (d08)
- [V] Decoding the critique mechanism in large reasoning models (2026). https://arxiv.org/html/2603.16331 (d10)
- [V] Disagreement-guided strategy routing (2026). https://arxiv.org/html/2604.26644 (d11)
- [V] Kim et al. (2025) Correlated errors in LLMs. https://arxiv.org/html/2506.07962 (d12)
- [V] Kuai et al. (2026) Auditing behavioural dependence. https://arxiv.org/abs/2604.07650 (d13; abstract only)
- [V] Lee et al. (2026) Risk-controlled selective answering. https://arxiv.org/abs/2609.37493 (d14; abstract only)
- [V] UPTURN: Inject a turn, not a token (2026). https://arxiv.org/abs/2610.13672 (d15; abstract only)
- [V] McAleese et al. (2024) LLM critics help catch LLM bugs. https://arxiv.org/abs/2407.00215 (d17; abstract only)
- [V] Panickssery, Bowman, Feng (2024) LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076 (d26; abstract only)
- [V] Gema et al. (2025) Inverse scaling in test-time compute. https://arxiv.org/html/2507.14417 (d27; first 100k characters)
- [V] Zeng et al. (2023) MR-GSM8K. https://arxiv.org/html/2312.17080 (d29)
- [V] Saad-Falcon et al. (2025) Weaver. https://arxiv.org/html/2506.18203 (d30; last 94k characters unread)
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/html/2407.21787 (d31)
- [V] Cook et al. (2024) TICK. https://arxiv.org/html/2410.03608 (d33)
- [V] Kuhn, Gal, Farquhar (2023) Semantic uncertainty. https://arxiv.org/html/2302.09664 (d34)
- [V] Viswanathan et al. (2025) Checklists are better than reward models. https://arxiv.org/html/2507.18624 (d35)
- [V] Chen et al. (2023) Teaching LLMs to self-debug. https://arxiv.org/html/2304.05128 (d36; last 35k characters unread)
- [V] Wait and think more: overthinking in distilled reasoning models. https://arxiv.org/html/2506.04210 (d37; unreviewed preprint)

Note: a few 2026 arXiv items (d05-d08, d10, d11, d13-d15) are single, unreviewed and from unreplicated groups. Several were read at abstract level only (marked above). Treat their numbers as leads.
