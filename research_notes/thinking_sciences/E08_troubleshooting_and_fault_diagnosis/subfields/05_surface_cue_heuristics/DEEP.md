# Surface-cue heuristics: deep document

*Subfield E08.05. Scope: fast symptom matching and its failures. Built from evidence_a-d.jsonl (a01-a24, b01-b25, c01-c24, d01-d16), claims.jsonl (K01-K32) and critique.md in this folder. Numbers marked "not re-checked" rest on one earlier reading. Items not opened (Chi 1981, Reason 1990, Rouse 1978, Tversky and Kahneman 1974) carry no numbers here on purpose.*

Related subfields researched in parallel (links only, not covered here): Heuristics and biases; Debiasing by training; Debiasing by structure (incentives, nudges, reference class forecasting); Abductive diagnosis; Expertise as chunking; Chain-of-thought prompting; Confidence and metacognition; Learned refinement and self-verification; Consensus and premature agreement; Analyst sensemaking; Failure-driven CBR.

## 1. What it is

A surface cue is a feature of the input that is easy to see and usually correlates with the right answer, but is not what causes the answer. Examples: a word that overlaps between two sentences, a number in a story, a stated guess, the letter of an option, the place of a document, a symptom that looks like a familiar fault.

Fast symptom matching is the use of such cues to jump to a stored answer. In fault diagnosis it means: the first symptom pattern that resembles a known fault becomes the diagnosis, without checking the wider state of the system.

Three facts frame the field.
- It is often right. Cheap cue use can match full regression (Take The Best .691 vs regression .694 at full cue knowledge) [a05].
- It fails when the cue and the truth come apart. Accuracy can then fall far below chance (HANS: most models under 10% where chance is 50%) [a08].
- A model (or a person) cannot tell from the inside which case it is in. Felt confidence is not a guide [b09, d14].

For our agent the topic is stage S1 (input hygiene). The question is how to stop a surface cue from steering the attempts at low token cost, and when to let the fast path stand.

## 2. History and theories in depth

### 2.1 Rasmussen: skill, rule, knowledge (1983)
Source read: a secondary summary only [a01, a02]. The IEEE paper was not opened.
- Skill-based: automated; runs on signals (time-space variables).
- Rule-based: stored if-then routines, triggered by signs. A sign is a cue tied to conditions for action, not to the functional state of the system.
- Knowledge-based: an explicit goal and a mental model. Used for novel problems and fault diagnosis. It is slow, so people fall back on it only when the rule level fails.
- Rasmussen warns the skill/rule boundary "is not quite distinct" [a01].
- Fast symptom matching sits at the rule-based level. Failure mode: a good rule fires on a sign in the wrong situation.

Reason (1990) built on this: rule-based mistakes (a strong rule in the wrong situation, or a bad rule) versus knowledge-based mistakes. Not opened; wording unverified [a21]. Rouse (1978) contrasted topographic search (follow system layout) with symptomatic search (match symptoms to known faults). Not opened [a22]. No error rates by level were found in any open source [d16]. Do not cite SRK error rates (K32).

### 2.2 Expert versus novice cue use
Chi, Feltovich and Glaser (1981): novices sorted physics problems by surface features (inclined plane, pulley); experts by governing principle. Full text not opened; sample sizes are from memory and must not be quoted [a03]. The finding fits the idea that expertise moves attention from surface to deep structure (K21).

### 2.3 Heuristics and biases versus fast and frugal
- Tversky and Kahneman (1974): judgement by similarity to a stereotype ignores base rates. Not opened [a24].
- Gigerenzer and Goldstein (1996): Take The Best looks up cues in order of validity, stops at the first that discriminates, and decides on it alone. Task: which of two German cities is larger; 83 cities; 9 binary cues [a04]. Accuracy averaged over 10-100% cue knowledge: Take The Best .658, weighted tallying .658, regression .657, tallying .656. At 100%: .691 vs .694. It searched about one fifth of the cue values [a05, a06]. Part of the edge comes from built-in recognition. One environment, one task type.
- Gigerenzer and Gaissmaier (2011) review: simple heuristics can win when data are scarce and the world is uncertain. Only the abstract opening was seen [b10].
- Kahneman and Klein (2009): intuition is trustworthy only where the environment is regular enough to learn and the person had practice with feedback. Confidence does not tell which case you are in [a23, b09, d14] (abstract only).
- Net: the camps agree on the condition. The practical question is cue validity in the test distribution.

### 2.4 Shortcut learning in machines
Geirhos et al. (2020) define shortcuts as decision rules that work on training and i.i.d. test data but fail under shift. A toy network learned object location instead of shape; with location controlled, accuracy fell to chance. They argue for out-of-distribution tests [a20].

### 2.5 Adversarial and challenge sets (2017-2019)
- Jia and Liang (2017): one distracting sentence (ADDSENT) cut mean F1 of sixteen SQuAD models from 75.4 to 36.4 (decimals not re-checked). Four models: 75.7 to 31.3, and to 6.7 with ungrammatical words (ADDANY). Humans lost about 3.4 F1 [a07].
- McCoy, Pavlick, Linzen (2019) HANS: three heuristics (lexical overlap, subsequence, constituent). Most MNLI-trained models were under 10% on cases where the heuristic is wrong [a08].

### 2.6 LLM era (2021-2026)
Calibration bias (Zhao 2021), shortcut triggers (Tang 2023), distractors (Shi 2023; Mirzadeh 2025), hints (Turpin 2023; Sharma 2024; Chen 2025), option and position bias (Zheng 2024; Liu 2024), premise order (Chen 2024), probability effects (McCoy 2023), medical bias (Schmidgall 2024; Vishwanath 2025; Singh 2026), agentic clinical reasoning (Braitsch 2026), real-fault agents (Roy 2024; ITBench; AIOpsLab). Details in sections 3 and 6.

## 3. Core findings with exact numbers

Status key: E established (2+ independent sources), S single-source, C contested, H human-only, O older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Rule-based level fires on signs; knowledge-based is the slow fallback | Qualitative, three levels | Rasmussen 1983 via summary [a01, a02] | S (secondary) |
| Cheap one-cue rule matches regression | .691 vs .694 at 100% cue knowledge; .658 vs .657 averaged; about 1/5 of cue values searched | Gigerenzer and Goldstein 1996 [a04-a06] | C (one environment) |
| Models trained on MNLI use lexical overlap | Most under 10% on HANS (chance 50%); BERT 39% conjunction, 0% subject/object swap, 49% conditional subcase | McCoy 2019 [a08, c05] | E, O |
| Extra training data fixes in-distribution, not the cause | 30,000 added examples (about 8% of 392,702); BERT 0% on withheld entailed passives | McCoy 2019 [a09] | S, O |
| Adversarial sentence in reading comprehension | F1 75.4 to 36.4 (16 models); 75.7 to 31.3 and 6.7 (4 models); humans -3.4 | Jia and Liang 2017 [a07] | S, O |
| One irrelevant sentence in math | At most 18% of solved problems stay solved over all distractor types; code-davinci-002 COT+SC micro 88.1 / macro 30.0; LTM+SC 93.4 / 45.0; role-overlap macro 0 for text-davinci-003 on some | Shi 2023 [a10, c01, b12] | E, O |
| Plausible-but-irrelevant clause in newer models | GSM-NoOp up to 65% drop (Phi-3-mini); o1-preview -17.5; Gemma-7b-it -20.6; Mistral-7b-v0.3 -24.0; o1-mini -29.1; GPT-4o -32.0; GPT-4o-mini -40.0 | Mirzadeh 2025 [a12, b11, d11] | E |
| Distractor mitigation is partial | COT 72.4 to 77.8 micro with ignore-instruction; best macro 45%; 20 samples contain the right answer 99.7%; 8 shots of the NoOp question did not fix it; no harm on clean GSM8K | Shi; Mirzadeh [a11, c02, c04, b25] | E |
| Hidden hint shifts answers; CoT does not say so | Suggested answer zero-shot CoT: -36.3 (GPT-3.5), -30.6 (Claude 1.0); few-shot -24.1/-21.5; always-A -18.7 / -4.7 | Turpin 2023 [a13, b15, c12] | E, O |
| User opinion pulls answers | Wrong suggestion: up to -27% (LLaMA 2); are-you-sure: up to -27% (Claude 1.3); answer changed 32% (GPT-4) to 86% (Claude 1.3); admit mistake 42-98% | Sharma 2024 [a14, b23, d06] | E, O |
| Reasoning text hides hint use | Hint verbalised 25% (Claude 3.7 Sonnet), 39% (DeepSeek R1); misaligned hints 20%/29%; reasoning models 3.6x/1.7x more faithful than non-reasoning siblings | Chen 2025 [d12] | E (with K06/K07 sources) |
| CoT effect on cue sensitivity is model-dependent | always-A: Claude 1.0 63.2 to 80.1; GPT-3.5 55.2 to 58.7 (arrow direction lost in extraction) | Turpin [c13] | S |
| Answer-letter preference | llama-30B picks A/B/C/D 34.6/27.3/22.3/15.8% on balanced labels; gpt-3.5-turbo 22.5/25.6/32.3/19.6; answer moved to D: 67.2 to 60.9; PriDe prior from about 5% of samples; debias instruction and CoT did not remove it | Zheng 2024 [a17, b17, c14, c24] | E |
| Calibration bias in few-shot | Up to +30.0 points after calibrating; accuracy 54.3-93.4% by example choice and order; GPT-3 62% Positive on "N/A"; "P P P N" prompt about 90% Positive | Zhao 2021 [a16] | S, O |
| Evidence position | U-shape; worst position can fall below closed-book 56.1% (GPT-3.5-Turbo); drop over 20% from best | Liu 2024 [a18, b16, d03] | E |
| Premise order | Deduction drop over 30%; GPT-4-turbo and PaLM 2-L -20-30%; R-GSM: GPT-4-turbo 94.1 to 85.0, PaLM 2-L 86.4 to 79.5, Gemini 1.0 Pro 80.5 to 69.1, GPT-3.5-turbo 67.3 to 51.8 | Chen 2024 [c15, d04] | E |
| Shortcut triggers in few-shot examples | GPT2-large average drop 33.71% vs GPT2-base 1.04%; MR 63.46 to 22.01 | Tang 2023 [a15, c16, d10] | C (small models) |
| Inverse scaling exists | 11 contest datasets; on one, GPT-4 below random; some trends U-shaped | McKenzie 2023 [d05] | C |
| Output probability acts as a cue | GPT-4 cipher 51% (high-probability answer) vs 13% (low); shift cipher rot-1 0.82, rot-3 0.76, rot-2 0.02; rare linear function 0% | McCoy 2023 [b13, c06, c23] | S |
| Counterfactual variants break LLMs, not humans | GPT-3.5 parseable programs 99% to 62/71/75%; letter-string analogies degrade in GPT-3/3.5/4; 1-shot worse than 0-shot in bases 11 and 16 | Wu 2024; Lewis and Mitchell 2024 [c07-c09] | E |
| Content (belief) effects on logic | Same direction as humans (people accept believable invalid syllogisms 90%, cited from Evans); per-model figures not recorded | Lampinen 2024 [c10, c11] | S |
| GPT-3 gives human-like wrong answers | 12 vignettes: all 12 correct or human-like, 6 correct; all 3 CRT items intuitive wrong; cab problem 20% | Binz and Schulz 2023 [b14] | S, O |
| Medical bias framing | 1,273 USMLE questions, 6 LLMs. Mean drop: false consensus 24.9, frequency 18.2, recency 12.9, confirmation 8.1. GPT-4 72.7 baseline, worst -14.0; GPT-3.5 mean -37.4; per-bias means not re-checked | Schmidgall 2024 [a19, b18, c17] | S |
| Bias education prompt | GPT-4 frequency 0.627 to 0.720; recency 0.679 to 0.742 with one-shot; Mixtral and GPT-3.5 marginal; PaLM-2 refused 94.4% / 99.5% | Schmidgall [c18] | S |
| Medical distractors | Non-literal words -2.2 to -17.8; bystander statements -1.3 to -17.9; open general -10.9 vs proprietary -3.8; RAG and fine-tuning did not fix | Vishwanath 2025 [b19] | S |
| Patient voice | 1,000 MedQA cases x 3 retellings, 12 open models (3B-24B): -9.6 (CI -11.0 to -8.2), 26% more errors, no scale benefit; rewrite-then-reason halves gap (+3.9, 11 models); schema extraction 7.1 worse than rewrite; CoT plus debias removes about a fifth | Singh 2026 [b20, b24] | S (preprint) |
| Agents under-seek information | 32 models, best 68%; data use 57% to 26% in round 3; R=0.69; 212 of 323 (65.6%) wrong first diagnoses stayed wrong; 156 of 307 (50.8%) right first diagnoses became wrong; Opus 4.5 recovered 6/6, one Qwen 1/14 | Braitsch 2026 [b21] | S (preprint) |
| Real incident agents | ReAct 35% correct, hallucination 4% vs CoT 12% vs retrieval 40%; 66% of ReAct wrong were insufficient-info; 10 of 38 retrieval-correct answers hallucinated. RCAgent: -33.54% pass without observation storage | Roy 2024; Wang 2023 [b22, c20, c21] | E |
| Fault diagnosis by agents is weak | ITBench SRE GPT-4o diagnosis 13.81% (+/-1.67), 9.52% no traces, Llama-3.3-70B 3.10%; AIOpsLab RCA 40.9/9.1/45.5/36.4% (GPT-4/GPT-3.5/ReAct/Flash) | Jha 2025; Chen 2025 [d08, d09] | E |
| Rewrite then answer helps | S2A on LLaMA-2-70B-chat: 62.8 baseline, 71.7 instructed, 80.3 S2A, 74.5 S2A with original kept, oracle 82.0; GSM-IC +10 to +12; RaR gains for GPT-4; GPT-3.5 and Vicuna slightly worse on Sports | Weston 2023; Deng 2023 [d01, d02, d15] | E (3 sources), O |
| Self-recheck without new evidence hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; Llama-2 62.0 to 43.5 to 36.5; with oracle labels GPT-3.5 CSQA 75.8 to 89.7 | Huang 2024 [d07] | S |
| Prompt style barely matters | GPT-4 (N=497): CoT 76, intuitive 77, differential 78, analytic 78, Bayesian 72; GPT-3.5 differential 38 (-8), Bayesian 42 (-4) | Savage 2024 [c19] | S |
| Easy items can take the fast path | First solution correct 97% on ASDIV; trimming cut 48.6% of tokens on MATH500 at kept accuracy; 1,953% more tokens on 2+3 | Chen 2025 [d13] | S (math only) |
| Human: bias teaching does not work | Sherbino 2014 N=191 students: 52% vs 48% (p=.91); 54% vs 48% (p=.13); availability 45% both (p=.98); over-search 64% vs 77% (p=.12). O'Sullivan 2019 N=76: 2.8 vs 3.1, CI -0.94 to 0.45, P=0.49. Norman 2017 review: bias-recognition teaching ineffective | [b01, b03, b04, b06] | E, H |
| Human: reflection can help | Mamede 2010 N=36 (18+18): PGY2 1.55 vs 2.19 (P=.03); reflection lifted to 2.03 (PGY2) and 2.31 (PGY1), P=.006; PGY1 showed the reverse pattern. Review: guided reflection effective in 5 of 28 studies | [b02, b05] | C, H |
| Human: speed vs reflect instructions | 71% (EPs) vs 43% (residents) by expertise; fast 55 s vs slow 73 s with no accuracy effect; 44.5 vs 45.0 (snippet only) | Monteiro 2015; Norman 2014 [b07, b08] | E, H (b08 snippet) |

## 4. Mechanisms and models

Each mechanism is written so it can be built or tested.

### 4.1 Cue-validity gate (ecological rationality)
- Model: a decision rule uses cue c for fault f. Validity v = P(f | c) in the deployment environment. The fast path pays off when v is high and stable and feedback exists (Kahneman and Klein) [b09].
- Failure: shift or an adversarial case makes v near 0 for that instance. HANS and GSM-NoOp are cases where v flips [a08, a12].
- Implementation: store per problem class the plain pass rate and the rate at which the first match was right (the S0 class record). Take the fast path if the first-match hit rate exceeds a threshold. No threshold has been measured for diagnosis (K31). The only compute-skipping data are math (97% first-correct on ASDIV) [d13].

### 4.2 Lexical-overlap and role-overlap capture
- The model scores candidates by word overlap with the input. Distractors sharing roles or numbers with the question hurt most; fewer shared words helps; changing numbers inside a distractor matters little [a10, b12].
- Cue words map to operations ("discount" to multiply) whatever the context [c04].
- Implementation: code flags input spans that share tokens with the question but enter no solution step. A relevance filter then removes or quarantines them (S1).

### 4.3 Hint and authority capture, with unverbalised use
- A stated answer or opinion changes the answer; the chain of thought rationalises and omits the cue [a13, d12].
- Consequence: hint use cannot be audited by reading rationale. Audit by structure: produce the answer with the hint removed and compare in code, or generate hypotheses before the hint is shown (K30).

### 4.4 Token and position priors
- Option letters carry a token prior [a17]. Evidence position carries a U-shaped weight [a18]. Premise order matching proof order helps [d04].
- Implementation: permutation vote. Shuffle option and evidence order across K samples, aggregate in code. PriDe estimates the prior from about 5% of samples and subtracts it, label-free [c14]. Caveat (G4): samples from one model are correlated, so the vote reduces order noise but is not proof.

### 4.5 Probability prior
- Familiar inputs and likely outputs get higher accuracy even in deterministic tasks [b13]. A rare fault with the same structure as a common one may be pulled toward the common diagnosis.
- Implementation: matched common/rare pairs with identical logic; measure the gap.

### 4.6 Rewrite-then-reason (S2A, RaR, voice rewrite)
- Step 1 (separate call): restate the task in neutral standard form, keeping only task-relevant facts. Step 2: answer from the restatement alone.
- Hiding the raw input matters: S2A with original kept 74.5% vs 80.3% hidden; baseline 62.8% [d02]. An ignore-instruction alone gave 71.7% on opinion prompts and no consistent gain on GSM-IC [d02].
- Voice rewrite halved a -9.6 gap (+3.9 points in 11 models); rigid schema extraction was 7.1 points worse than free rewrite [b20].
- Risks: rewriting invents plausible details [b20]; weak models can lose accuracy [d15]; the second call costs tokens (not tabulated in either paper).
- Implementation: S1 produces a restatement in a fresh context; code stores raw and restated; attempts at S3 see only the restatement (the quarantined block is not shown to them). The schema says "keep the original wording beside it". The S2A result suggests "beside it" should mean for the checker, not for the attempts. This is a Test-first item.

### 4.7 Information-seeking loop
- Agents under-request data and anchor: utilisation 57% to 26% by round 3; wrong first diagnoses stay wrong 65.6% [b21]. Observation handling matters: removing KV storage cut pass rate by 33.54% [c21]. Raw telemetry overloads context [d09].
- Implementation: after a first hypothesis, code forces one evidence request that could refute it (discriminating test); logs are sorted and summarised by code before the model sees them.

### 4.8 Self-recheck rule
- Intrinsic recheck with no new information lowers accuracy [d07]. Allow a recheck only if it brings new evidence or a different method (G2).

## 5. What holds up

### 5.1 Replicated or multi-source
- Distractor harm: Jia and Liang 2017, Shi 2023, Mirzadeh 2025, Vishwanath 2025 and Singh 2026 all find large drops, from SQuAD to math to medicine [a07, a10, a12, b19, b20].
- Hint and opinion capture: Turpin, Sharma and Chen 2025 agree on direction and on unverbalised use [a13, a14, d12].
- Order and position effects: Zhao 2021, Zheng 2024, Liu 2024, Chen 2024 [a16, a17, a18, c15].
- Counterfactual brittleness: Wu 2024 and Lewis and Mitchell 2024 [c07, c09].
- Human bias teaching fails: Sherbino 2011 and 2014; O'Sullivan 2019; Norman 2017 [b01-b06].

### 5.2 Failures, nulls and contested items
- Scale: larger GPT-2 and OPT models shortcut more [a15], and inverse scaling exists [d05]. Yet in BiasMedQA GPT-4 was most resilient, and Singh found no scale benefit among 3B-24B open models [b20]. The NoOp paper says recent models decline more in one figure caption [c22], while o1-preview was more robust than others [a12]. Contested (K29, K10, K04).
- Human reflection: Mamede helped [b02]; Sherbino and O'Sullivan did not [b03, b06]. Populations differ (residents, students, mixed doctors). Mamede has no main effect, only an interaction with training year, and PGY1 showed the reverse [b02]. Contested (K20).
- Speed versus reflect instruction: no effect [b07, b08].
- Take The Best versus HANS: both hold. Cue use works when validity holds and fails when it does not (K21).
- Correction: the 191 participants in Sherbino 2014 were medical students on an emergency rotation, not doctors (critique).

### 5.3 Moderators
- Overlap with the question (role or number overlap) raises distractor harm [b12].
- Model strength: RaR helps strong models and can hurt weak ones [d15]. Bias-education prompts help GPT-4, not Mixtral or GPT-3.5 [c18]. Differential and Bayesian prompts hurt GPT-3.5 [c19].
- Task: CoT helped Claude 1.0 on always-A, barely GPT-3.5 [c13]. Turpin effects vary a lot by task [a13].
- Position: worst in the middle of 20-30 documents [d03].
- Expertise: experts 71% vs residents 43% in Monteiro [b07].

### 5.4 Interventions that worked
- Neutral restatement with raw input hidden (S2A +10 to +12 on GSM-IC; 80.3 vs 62.8) [d02].
- Voice rewrite (halved the gap) [b20].
- Permutation debiasing (PriDe, 5% sample) [c14].
- Calibration against content-free input (up to +30 points, GPT-3 era) [a16].
- Distractor exemplars and ignore-instruction: modest, consistent gains, no harm on clean data [a11, b25].
- Self-consistency: lifts micro accuracy, but macro stays at or below 45% [c02].
- Structured reanalysis after exposure in residents (Mamede) [b02].
- Observation storage in agents [c21].
- Fine-tuning with 30,000 HANS-like examples (not available for a frozen model) [a09].

### 5.5 Interventions that did not work
- Bias-awareness teaching and cognitive forcing in people [b03, b06].
- Debias instruction and CoT for letter bias [b17]; for patient voice they removed about a fifth [b20]; for hints, small help [a13].
- Eight shots of the same NoOp question [a12].
- RAG and medical fine-tuning against distractors [b19].
- Self-recheck without new evidence [d07].
- Rigid schema extraction (7.1 worse) [b24].

## 6. Language models

### 6.1 Overview
LLMs are strong cue users. They answer from the familiar form, copy suggested answers, and follow irrelevant material that looks topical. The same cue gives the right answer on ordinary items and the wrong one on cue-conflict items.

### 6.2 By task family
- Reading and NLI: ADDSENT halves F1 [a07]; HANS under 10% on conflict cases [a08]. 2017-2019 models.
- Math: GSM-IC and GSM-NoOp. Drops up to 65% [a12]. o1-preview -17.5 [a12]. 2025 models still fall [d11]. Role-overlap distractors push macro accuracy to 0 on some problems [b12].
- Hints and sycophancy: -36.3 points (GPT-3.5), up to -27% (LLaMA 2) [a13, a14]. Reasoning models verbalise hints 25% (Claude 3.7 Sonnet) and 39% (DeepSeek R1) of the time [d12].
- Format cues: letter bias 34.6% vs 15.8% on balanced labels [a17]; document position [a18]; premise order [c15].
- Probability cues: 51% vs 13% [b13].
- Medicine: BiasMedQA drops 8.1-24.9 on average, GPT-4 best [b18]. MedDistractQA up to 17.9 [b19]. Patient voice -9.6 across 12 open models [b20].
- Agentic diagnosis: best of 32 frontier models 68%, with anchoring and under-seeking [b21]. Real incidents: ITBench GPT-4o 13.81%, AIOpsLab RCA 9-45% [d08, d09]. ReAct hallucination 4% vs retrieval 40%, with 66% of ReAct errors "insufficient information" [b22].

### 6.3 What changed behaviour, and by how much
| Change | Effect |
|---|---|
| Regenerate context, hide raw | 62.8 to 80.3 (LLaMA-2-70B); GSM-IC +10-12 [d02] |
| Keep raw alongside | 74.5, i.e. 5.8 points lost vs hiding [d02] |
| Ignore instruction only | 71.7 on opinion QA; no consistent GSM-IC gain [d02]; COT micro 72.4 to 77.8 on GSM-IC [a11] |
| Voice rewrite | gap halved, +3.9 [b20] |
| Schema extraction | 7.1 points below rewrite [b24] |
| Self-consistency | micro up (0-CoT +35.5), macro best 45% [c02] |
| Permutation prior | removes most letter bias [b17] |
| Bias-education prompt | GPT-4 0.627 to 0.720 on one bias; others marginal [c18] |
| CoT | uneven: Claude 1.0 63.2 to 80.1, GPT-3.5 55.2 to 58.7 on always-A [c13] |
| Differential or Bayesian reasoning prompt | no gain for GPT-4; losses for GPT-3.5 [c19] |
| Recheck own answer | large losses (CSQA 75.8 to 38.1) [d07] |
| Tools and observation store | RCAgent: -33.54% pass without the store [c21]; step budget helps ReAct, plateaus for GPT-3.5 beyond 5 steps [d09] |

### 6.4 Caveats on the LLM evidence
- Most models are 2022-2023 (text-davinci-003, GPT-3.5, Claude 1.0, GPT-2). Few current frontier tests with cue-misleading diagnosis.
- Almost no direct study of surface cues in device or software fault diagnosis; evidence is by analogy from math, NLI, QA and medicine (critique).
- Many sets are adversarial by design; real base rates are unknown.
- Singh 2026 notes generation settings differed between voices, so cause is not shown [b20]. Braitsch and Singh are preprints.
- Rewrite-then-reason token cost versus best-of-N was not measured in either paper.
- The fault-diagnosis benchmarks do not isolate cue effects [d08].

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **S1: quarantine suggestive and irrelevant material.** Code moves stated guesses, authority claims and unused numbers into a marked block the attempts do not see. Part S1 (strengthens the existing text). [E] K03, K06, K16, K24, K30. Evidence a10, a12, a13, a14, b12, b19, d02, d06, d12.
2. **S1: neutral restatement before reasoning.** The effect of rewriting is established across three sources (K17: b20, d01, d02). Part S1/S3. [E] Evidence b20, d01, d02. The detail "attempts see only the restatement" is [S] and sits under Test first.
3. **G10 stays: reasoning text is not evidence.** Hint use is unverbalised in 61-75% of cases. Audit by structure. Part G10. [E] K30. Evidence a13, d12.
4. **4b stays: no bare "be careful" or bias-awareness instruction as the only defence.** Human nulls plus partial LLM gains. Part 4b/G. [E] K19, K05. Evidence b03, b06, b01, c18, a11.
5. **S3/S7: shuffle options and evidence order across attempts, aggregate in code** (permutation vote). Part S3/S7/G5. [E] K08, K09, K28. Evidence a17, b17, c14, a18, d03, c15, d04. G4 still applies: agreement is a hint, not proof.
6. **S4/memory: store tool observations in code and summarise before showing.** Part S1/memory. [E] K23. Evidence c21, b22, d08, d09.
7. **G2 citation only:** recheck must bring new evidence (d07, [S]); no new element, G2 and 4b already cover it.
8. **Do not cite or build on SRK error rates** (K32).

### Test first ([S] or [C])
1. Hide-raw rewrite versus keep-raw versus instruction-only [S] K25, K17 (d02, b20).
2. Free rewrite versus schema extraction on diagnosis cases [S] K17 (b20, b24).
3. Cue-validity gate for the fast path (S0) [S] K31, K21 (d13, b09).
4. Forced refutation request after the first hypothesis (S4/S5) [S] K18 (b21).
5. Evidence-order shuffle in agentic loops and a sorted summary (S1/memory) [S] K28 (d03, d04).
6. Hypotheses-before-hint ordering (S1) [S] K30, K24 (d06, d12).
7. Scale check, one cue-conflict set across sizes of one family (S0) [C] K29, K10 (d05, a15).
8. Common versus rare fault with identical logic (S1) [S] K11 (b13).
9. Structural check versus bias-awareness prompt (G) [C] K15, K20 (c18, b02).
10. Believable-but-invalid diagnostic inference with and without a validity check [S] K13 (c10).

## 8. Concrete tests on our bench

All arms get the same token budget (G7); setup and extra calls are counted. Report accuracy, flip rate (right to wrong and wrong to right), and tokens.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Fault cases with a planted misleading symptom (cue points to fault A, truth is B), plus matched cue-aligned controls | plain; plain+ignore-instruction; rewrite with raw hidden; rewrite with raw kept; best-of-N vote | Accuracy on conflict items; accuracy on controls (check no harm) | Hidden-raw rewrite beats plain by 8-18 points as in S2A (62.8 to 80.3); kept-raw about 6 points lower; no loss on controls |
| T2 | Same cases, retold in user or patient voice | plain; free rewrite; schema extraction; CoT+debias | Voice gap (original minus retold accuracy) | Free rewrite halves the gap; schema extraction 5-7 points worse |
| T3 | Cases with a user-stated wrong diagnosis inserted | plain; hint quarantined in code; hypotheses before hint; instruction-only | Accuracy drop vs hint-free | Quarantine and hint-after beat instruction-only; plain drop large (up to 27 points in older models) |
| T4 | Multi-candidate cases with shuffled option or log order | single order; 4-permutation vote; PriDe-style prior from 5% | Accuracy and order variance | Variance falls; gain 2-8 points where letter bias is strong |
| T5 | Agentic tool loop with a plausible wrong first hypothesis | plain loop; forced refutation request; free recheck | Recovery of wrong first diagnosis (baseline 34.4% in b21); evidence-use rate | Forced request raises recovery; free recheck does not (d07) |
| T6 | Common vs rare fault of equal logic | plain; cue-audit step | Accuracy gap common minus rare | A gap exists; audit narrows it only if it adds new evidence |
| T7 | Items stratified by validity of the first cue (0.5, 0.7, 0.9, 0.99) | always fast; always deep; gated by class hit rate | Accuracy per token | Fast wins above a threshold validity; find it |
| T8 | One cue-conflict set across sizes of one model family | plain at each size | Accuracy gap by size | Settles K29: gap grows, shrinks or stays |
| T9 | Believable invalid inference items | plain; code-run validity check | Acceptance of invalid items | Lower acceptance |

## 9. What does not transfer, and why

- **Human teaching results (b03, b06, b01).** They test whether a person learns and applies a rule. An agent can have a step enforced by code. The null says "do not rely on an instruction"; it does not say structural checks fail.
- **Chi 1981 expert sorting.** Experts reorganised knowledge over years. A scaffold cannot acquire that in one run. The idea (sort by deep structure) can be tried as a step, but the human mechanism does not carry over. Numbers were not verified.
- **Take The Best numbers.** One environment, 83 cities, correlated cues. The principle (cue validity decides) transfers; the percentages do not.
- **Fine-tuning fixes (HANS augmentation).** A frozen model gets no such fix [a09].
- **Calibration against content-free input (Zhao).** Needs label probabilities; GPT-3 era [a16].
- **Math distractor sizes (GSM-IC, NoOp).** Arithmetic with exact answers. In diagnosis, "irrelevant" is harder to define, since a distractor may be a true clue. A relevance filter can remove evidence.
- **PriDe for letter bias.** Multiple-choice only. Diagnosis on our bench may be free-form.
- **Exam-style medical sets.** Injected bias text on USMLE items is not a live case.
- **Rasmussen's levels as a pipeline.** SRK is a descriptive human model. Mapping it onto S-states is a design choice, not a measured fit. No level-specific error rates were found [d16].
- **Reasoning-faithfulness numbers (25% and 39%).** Likely upper bounds, on multiple-choice with inserted hints [d12].
- **Overthinking numbers (97% first-correct).** Math only [d13].

## 10. Open questions

1. Does hide-raw rewrite-then-reason cut cue-induced errors in current frontier models, and at what token cost versus best-of-N? (Token cost unmeasured in d01 and d02.)
2. How large are cue failures on current frontier models in real fault diagnosis? ITBench and AIOpsLab do not isolate cues.
3. Which structural check beats a bias instruction at equal tokens: differential reanalysis, cue-validity audit or permutation vote?
4. Is there a cue-validity threshold for skipping the deep path?
5. What are Rasmussen's and Reason's primary error rates? The primary texts are unread.
6. Does forced evidence re-request lift recovery above 34.4%?
7. Do larger or newer models shortcut more or less on diagnosis cues? A matched scale study is missing.
8. Does evidence order matter inside agentic loops, and does a sorted summary fix it?
9. Does separating hypothesis generation from user hints cut hint following?
10. Do null cognitive-forcing results hold for expert clinicians, and is there an LLM analog of Chi's sorting?
11. Does neutral rewriting invent details that become new errors in diagnosis (b20 saw it)? How can code detect this?
12. Is the 61-75% unverbalised hint rate stable in current frontier models?

## 11. Sources

[V] opened this session (page or PDF text); [M] snippet, abstract-only or not opened.

- [V] Rasmussen (1983) via Smith summary (secondary; original not reached). https://www.smithsrisca.co.uk/PSYrasmussen1983.html
- [M] Chi, Feltovich, Glaser (1981), not opened (scanned). https://apps.dtic.mil/sti/pdfs/ADA100301.pdf
- [V] Gigerenzer and Goldstein (1996). https://www.dangoldstein.com/papers/FastFrugalPsychReview.pdf
- [V] Jia and Liang (2017). https://arxiv.org/abs/1707.07328
- [V] McCoy, Pavlick, Linzen (2019) HANS. https://arxiv.org/abs/1902.01007
- [V] Shi et al. (2023) GSM-IC. https://arxiv.org/abs/2302.00093
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229
- [V] Turpin et al. (2023). https://arxiv.org/abs/2305.04388
- [V] Sharma et al. (2024) sycophancy. https://arxiv.org/abs/2310.13548
- [V] Tang et al. (2023) lazy learners. https://arxiv.org/abs/2305.17256
- [V] Zhao et al. (2021) Calibrate before use. https://arxiv.org/abs/2102.09690
- [V] Zheng et al. (2024) multiple-choice selectors. https://arxiv.org/abs/2309.03882
- [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/abs/2307.03172
- [V] Schmidgall et al. (2024) BiasMedQA. https://arxiv.org/abs/2402.08113
- [V] Geirhos et al. (2020) Shortcut learning. https://arxiv.org/abs/2004.07780
- [M] Reason (1990) Human Error, not opened.
- [M] Rouse (1978), not opened.
- [M] Tversky and Kahneman (1974), not opened. https://doi.org/10.1126/science.185.4157.1124
- [V] Norman et al. (2017), abstract page. https://pubmed.ncbi.nlm.nih.gov/27782919/
- [V] Mamede et al. (2010). https://pubmed.ncbi.nlm.nih.gov/20841533/
- [V] Sherbino et al. (2014). https://pubmed.ncbi.nlm.nih.gov/24423999/
- [V] Sherbino et al. (2011). https://pubmed.ncbi.nlm.nih.gov/21240788/
- [V] Lambe et al. (2016). https://pubmed.ncbi.nlm.nih.gov/26873253/
- [V] O'Sullivan and Schofield (2019). https://pubmed.ncbi.nlm.nih.gov/30621679/
- [V] Monteiro et al. (2015). https://pubmed.ncbi.nlm.nih.gov/25565260/
- [M] Norman et al. (2014) reflect vs speed, snippet only. https://experts.mcmaster.ca/scholarly-works/333942
- [V] Kahneman and Klein (2009), abstract page only. https://pubmed.ncbi.nlm.nih.gov/19739881/
- [M] Gigerenzer and Gaissmaier (2011), abstract opening only. https://pubmed.ncbi.nlm.nih.gov/21126183/
- [V] McCoy et al. (2023) Embers of autoregression. https://arxiv.org/abs/2309.13638
- [V] Binz and Schulz (2023). https://arxiv.org/abs/2206.14576
- [V] Wu et al. (2024) Reasoning or reciting. https://arxiv.org/abs/2307.02477
- [V] Lewis and Mitchell (2024). https://arxiv.org/abs/2402.08955
- [V] Lampinen et al. (2024) content effects. https://arxiv.org/abs/2207.07051
- [V] Chen et al. (2024) Premise order. https://arxiv.org/abs/2402.08939
- [V] Savage et al. (2024) diagnostic reasoning prompts. https://arxiv.org/abs/2308.06834
- [V] Vishwanath et al. (2025) MedDistractQA. https://arxiv.org/abs/2504.01201
- [V] Singh, Deka, Chennareddy (2026) patient voice. https://arxiv.org/abs/2607.27384
- [V] Braitsch et al. (2026) OncoRounds. https://arxiv.org/abs/2607.10275
- [V] Roy et al. (2024) RCA agents. https://arxiv.org/abs/2403.04123
- [V] Wang et al. (2023) RCAgent. https://arxiv.org/abs/2310.16340
- [V] Deng et al. (2023) Rephrase and Respond. https://arxiv.org/abs/2311.04205
- [V] Weston and Sukhbaatar (2023) System 2 Attention. https://arxiv.org/abs/2311.11829
- [V] McKenzie et al. (2023) Inverse scaling. https://arxiv.org/abs/2306.09479
- [V] Huang et al. (2024) Cannot self-correct. https://arxiv.org/abs/2310.01798
- [V] Jha et al. (2025) ITBench. https://arxiv.org/abs/2502.05352
- [V] Chen et al. (2025) AIOpsLab. https://arxiv.org/abs/2501.06706
- [V] Chen et al. (2025) Reasoning models don't say what they think. https://arxiv.org/abs/2505.05410
- [V] Chen et al. (2025) Overthinking. https://arxiv.org/abs/2412.21187
- [V] HEART page (negative search for SRK rates). https://en.wikipedia.org/wiki/Human_error_assessment_and_reduction_technique

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 15 established claims: 12 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E08.05-K02** (reworded: the sources support less). HANS numbers are right (accuracy under 10% in most cases, chance 50%; BERT 0% on subject/object swap) but concern fine-tuned NLI models only, not models 'prompted on text', and 'most cases' (model-subset pairs) is not 'most models'; McCoy entries are one paper, Geirhos is only a toy example. Corrected claim: Fine-tuned NLI models (BERT, ESIM, DA, SPINN) trained on MNLI adopt surface heuristics such as lexical overlap and fail almost completely when the heuristic points the wrong way: on HANS they scored under 10% in most cases where chance is 50%, and BERT scored 0% on subject/object swap.
- **E08.05-K23** (number corrected). Roy et al. numbers are right (ReAct S+Q BM25 35%, hallucination 4% vs CoT 12% vs RB 40%, 66% insufficient information), but the RCAgent 33.54% pass-rate drop is from replacing the minimalist tools with SQL/SLS query tools (99.38 to 65.84), not from removing key-value storage (w/o OBSK is 96.89, about -2.5). Corrected claim: LLM agents for root-cause analysis struggle with evidence: in Roy et al., ReAct (S+Q BM25) was 35% correct against 39% for CoT and retrieval baselines, with 4% hallucination (vs 12% CoT, 40% retrieval), and 66% of its wrong answers reported insufficient information; the RCAgent ablation shows tool and observation handling matters (swapping to SQL query tools cut pass rate by 33.54%, removing the observation key-value snapshot cut it from 99.38 to 96.89).
- **E08.05-K27** (number corrected). The 36% easy vs 5% hard diagnosis split in ITBench is for SRE scenarios (GPT-4o), not the CISO split; other numbers (13.81%, 9.52% without traces, AIOpsLab RCA 9.09-45.45% over four agents, raw telemetry overloading context) check out. Corrected claim: Real fault diagnosis by LLM agents is still weak and noise-sensitive: ITBench SRE diagnosis pass@1 is 13.81% for GPT-4o (9.52% without traces; 36% on easy vs 5% on hard SRE scenarios), AIOpsLab RCA accuracy is 9-45% across four agents, and telemetry dumped raw into context can overwhelm the agent. Cue-conflict effects are not isolated in either.
- **E08.05-K24** (now single-source: only one opened source, code check).
