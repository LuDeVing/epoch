# Dual-process theory: deep document

*Subfield E01.04, medical diagnostic reasoning. Source files in this folder: evidence_a-d.jsonl (ids a01-a25, b01-b26, c01-c27, d01-d18), claims.jsonl (K01-K29), critique.md. Numbers were cross-checked in critique.md; corrections are applied here. Evidence from abstracts only is marked as such.*

## 1. What it is

Dual-process theory says there are two kinds of thinking. Type 1 (System 1) is fast, automatic, associative and cheap. Type 2 (System 2) is slow, serial, effortful and uses working memory. In medicine, Croskerry (2009) mapped this onto diagnosis: pattern recognition is System 1, hypothetico-deductive analysis is System 2. The usual story is "default-interventionist": System 1 offers a first answer, System 2 may check it. Errors are blamed on System 1 bias that System 2 fails to catch. The practical advice that follows is "slow down", "think about biases", "use forcing strategies".

For our agent the subfield matters at one place: S0, the choice of mode. Should an item get a direct answer, a short pass, or a full slow route with checks? The evidence below says the default-interventionist story is weak as a design basis, and that three better rules exist: (1) mode should depend on task type and model strength, not on a "be careful" instruction; (2) checks should be triggered by code-visible signals (disagreement, failure, a planted cue), not by the model's own doubt; (3) errors in diagnosis come from missing or mis-organised knowledge as much as from fast thinking.

Main findings in one paragraph. In humans, telling clinicians to go fast or to be careful does not change accuracy (N=393, p=.12). Teaching cognitive forcing or bias awareness does not help (N=191, all p>.12). Wrong diagnoses take longer than right ones. Intuition is reliable only in regular environments with feedback. In LLMs, older models behave like System 1 on trap puzzles and chain-of-thought (CoT) rescues them; strong models rarely fall for the traps; CoT helps mainly on math and symbolic tasks; on clinical text 82 of 95 models got worse with CoT. Explicit fast/slow agent designs exist (SwiftSage), but no study tests per-item routing against always-slow and never-slow at equal tokens in medicine (K25).

## 2. History and theories in depth

**Roots.** Wason and Evans (1970s) showed that people give answers by "heuristic" processes and then rationalise them. Evans, Barston and Pollard (1983) found belief bias in syllogisms (people accept believable conclusions regardless of logic; the acceptance rates in the notes were recalled from memory and are not used here, a24). Stanovich and West (2000) named System 1 and System 2. Frederick (2005) built the three-item Cognitive Reflection Test (CRT) as a probe of whether a person overrides a fast wrong answer. The original CRT result is about 41% correct (n=3,428, cross-checked via Hagendorff, a23, c05).

**Kahneman (2003), Nobel lecture (opened, a01-a03).** System 1: fast, automatic, effortless, associative, hard to control. System 2: slower, serial, effortful, rule-governed. System 2 monitors System 1, but "the monitoring is normally quite lax", so many wrong intuitive answers are expressed. Key numbers: bat-and-ball, 50% (47/93) of Princeton and 56% (164/293) of Michigan students gave the intuitive 10 cents. Linda problem: 85% (ranked by representativeness) and 89% (ranked by probability) ranked the conjunction above its part, with a .99 correlation between the two rankings. This supports "attribute substitution": a hard question (probability) is answered by an easy accessible one (similarity). Conditions that weaken System 2: time pressure, concurrent load, off-peak time of day, good mood. Helpers: intelligence, need for cognition, statistical training. Statistically trained graduate students still used representativeness by default; training worked only in the stripped-down version.

**Croskerry (2009) universal model (abstract only, a20).** Proposes the dual-process model for diagnosis, with override routes and calibration. The author cautions that not all reasoning fits in one system. The full figure was not verified here.

**Pelaccia et al. (2011) review (opened, a04, a05).** "Reasoning always starts intuitively." Analytic control is more likely when time permits, stakes are high, or the case is complex. Errors cannot be pinned on one system. Analytic answers are not shown to be better than intuitive ones. Hogarth's kind versus wicked learning environments decide whether intuition can be trusted. Secondhand figure: about 95% chance of a correct final diagnosis if the right hypothesis appears in the first five minutes (Neufeld, not opened; single source).

**Evans and Stanovich (2013) (abstract only, b10).** Replace System 1/2 by Type 1 (autonomous, no working memory) and Type 2 (needs working memory, supports hypothetical thinking). Defining features, not correlated features such as speed, separate the types. They keep default-interventionism: Type 1 gives a default unless Type 2 intervenes. They concede that some critiques hit some versions. For an LLM this suggests defining Type 2 by a written intermediate trace and supposition, not by delay.

**Competing theory 1: conflict detection and "logical intuitions" (b11-b14).** Thompson et al. (2011): a fast Feeling of Rightness predicts how much people rethink (four experiments, n=60, 48, 128, 64). Pennycook, Fugelsang and Koehler (2015): a three-stage model with Type 1 cues, conflict detection, then Type 2 rationalisation or decoupling; detection and decoupling are separate error sources. De Neys: biased reasoners still show signs of detecting the conflict (slower, less confident). Bago and De Neys (2017): with load and deadlines, people often give the correct logical answer first, fast and confident (four experiments, exact percentages unread; abstract only). This runs against "wrong fast, right slow".

**Competing theory 2: knowledge-based view (a16, b03, b04, a21).** Norman, Monteiro, Sherbino et al. (2017, 2020) and Pelaccia et al. (2025): both Type 1 and Type 2 run on stored cases; errors come from both; bias-recognition teaching is ineffective; knowledge reorganisation gives "small but consistent benefits". One school; the authors are the main group arguing it. Zwaan et al. (as cited in b04): physicians could not agree above chance on which biases were present, and found twice as many biases when the case ended in a wrong diagnosis (hindsight).

**Competing theory 3: expertise conditions (b15).** Kahneman and Klein (2009): intuition is trustworthy in regular environments with long practice and feedback; subjective confidence is not a guide to accuracy.

**Neural note (b17).** An ALE meta-analysis (Gronchi 2024) finds dual-process tasks converge on cognitive-control areas (medial and superior frontal, anterior cingulate, insula, left inferior frontal gyrus). This suggests the split may reflect inhibition and control rather than two modules. Low direct relevance.

**AI framings.** Booch et al. (2020, c26): position paper, fast solver, slow solver, metacognitive selector; no experiments. Christakopoulou et al. (2024, c27): Talker-Reasoner agent with a wait flag; case study, no accuracy numbers.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree; single = one source; contested = sources disagree. "abs" means abstract only was read.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Bat-and-ball intuitive trap in students | 50% (47/93) Princeton, 56% (164/293) Michigan said 10 cents | Kahneman 2003 (a01) | established |
| Linda conjunction error | 85% and 89% (two ranking tasks); rank correlation .99 | Kahneman 2003 (a02) | established |
| CRT in people | about 41% correct (n=3,428); 38% human baseline in Hagendorff; medical students 44% all correct, 10% all intuitive (N=128) | a06, a08, a23 | established |
| "Be fast" vs "be careful" does not change accuracy | Residents N=96 vs 108: 44.5% vs 45.0% accuracy; 69 s vs 89 s (p<.001 for time) | Norman 2014 (b01, abs) | established (K01) |
| Same, larger design | N=393; instruction F(1,379)=2.44, p=.12; complexity F=965.2, experience F=39.6 | Ilgen 2013 (b08, abs) | established |
| Cognitive forcing teaching has no effect | N=191 (145 vs 46): 52% vs 48% started second search (p=.91); 45% vs 45% found uncommon dx (p=.98); 64% vs 77% over-search (p=.12) | Sherbino 2014 (b02, abs) | established |
| Wrong diagnoses take longer | 115 s correct vs 129 s incorrect (p<.001), N=117; wrong cases about 17 s longer in Norman 2014 | b05, b01 | established |
| Availability bias induced and fixed by reflection | N=36; second-years 1.55 vs 2.19 (p=.03); reflection 2.03/2.31 (p=.006) | Mamede 2010 (b06, a17, abs) | contested |
| Same bias induction, independent trial | N=46; control scored 0.80 experimental vs 0.59 filler (p<.01); bias group 0.66 vs 0.64 (p=.756); reflection gave no repair | Japanese RCT 2020 (d10) | contested |
| Bias induction fails in larger trial | N=117; no significant availability-bias effect | van den Berg 2021 (b05) | contested |
| Reflection helps learning at one week, hurts at first | N=46: immediate 0.48 vs 0.62 (p=.012); one week 0.66 vs 0.48 (p<.01) | Mamede 2012 (b07, abs) | single |
| Reflection works on complex cases for residents | more than 35% gain on complex cases; none on simple; students reverse | Mamede and Schmidt 2023 (d11) | contested (same group) |
| Guided reflection most often works | 5 of 28 studies; no pooled effect | Lambe 2018 (b09, abs) | contested |
| Short exposure vs long | ECG/X-ray 175-1000 ms accuracy about 0.70-0.83; diagnosis 1-20 s: accuracy flat from 5 to 20 s | Pelaccia 2025 (b04, secondhand) | single |
| Time-pressure intuitive cooperation fails | 21 labs; ITT -0.37 points vs original 8.6; compliant-only 10.37 vs 15.31; non-compliance 65.9% vs 7.5% | Bouwmeester 2017 (b16) | single (replication) |
| CRT, LLMs by model | Correct: davinci-003 5%, ChatGPT-3.5 59%, ChatGPT-4 96%, humans 38%. Intuitive: 80% / 15% / 0% / humans 55% | Hagendorff 2023 (a08, c01) | established |
| CoT rescues weak model | davinci-003 correct 5% to 28%; intuitive 80% to 29% | a09, c02 | established |
| Blocking CoT in strong models | GPT-3.5 change 4 points (p=.49); GPT-4 95% to 88%, intuitive 0% to 10%; CoT share 97% to 0% and 84% to 0% | a09, c03 | established |
| Few examples teach trap avoidance | 2% to 92% after 2 examples; 12% to 92% after 7; 0% to about 78% after 30 (davinci-003) | a10, c04 | single |
| Semantic illusions | davinci-003 fell 72%; correct 18% / 74% / 88% (davinci / 3.5 / 4) | c05 | established |
| GPT-3 on classic vignettes | CRT 3/3 intuitive; 12 vignettes: 6 correct, 12 human-like; cab variant answered 20% | Binz and Schulz (a07, c06, c07) | established |
| CoT helps mainly on math and symbolic | 110 papers, 1,218 comparisons; gains 14.2 symbolic, 12.3 math, 6.9 logic; 56.9 vs 45.5 on those; others 56.8 vs 56.1; up to 95% of MMLU gain on "=" questions | Sprague 2024 (b19, c15) | established |
| CoT hurts where deliberation hurts humans | Grammar learning GPT-4o 87.5 to 64.4 (-23.1); face recognition GPT-4o 64.0 to 51.2, Claude 3 Opus 44.0 to 29.6, Gemini 1.5 Pro 66.0 to 54.6; exceptions +331% rounds | Liu 2024 (a14, b20, c14) | established |
| CoT hurts clinical text tasks | 95 LLMs, 87 tasks: 82 of 95 (86.3%) worse; Gemini-2.5-flash -1.6, R1 -2.1, GPT-4o -3.5 points; drop by quintile -5.8% to -9.9% | Wu 2025 (b24) | established |
| Reasoning length tracks error | 100 MedQA cases, 93% correct; 8,118 vs 3,648 characters (p=.032, 7 errors, 1 coded anchoring) | Moell 2025 (b25, d06) | contested (small sample) |
| Reasoning models overthink | 1,953% more tokens on 2+3; self-training cut tokens 48.6% at equal accuracy | Chen 2025 (c16) | established |
| Optimal medical reasoning budget | about 4K tokens, accuracy falls beyond | Huang 2025 m1 (c25) | single |
| Named clinical reasoning prompts | GPT-4: CoT 76%, intuitive 77, differential 78, analytic 78, Bayesian 72 (all p>.05). GPT-3.5: CoT 46; analytic 40 (p=.001), differential 38 (p<.001), Bayesian 42 (p=.02) | Savage 2023 (c09, c10) | single |
| Planted bias lowers LLM accuracy | GPT-4 0.727 no-bias, mean over 7 cues 0.673 (-5.4 pts); GPT-3.5 0.497 to 0.311 (-18.6 pts = -37.4% relative); false consensus worst (avg -24.9); confirmation least (-8.1) | Schmidgall 2024 (d01, d02) | single |
| Warning or demo restores GPT-4 | gap 5.4 to 1.8 (education) or 0.8 (few-shot, own baseline 0.757); weak models only marginal | d03 | single |
| SwiftSage | ScienceWorld 84.7 vs Reflexion 45.3, ReAct 36.4, SayCan 33.8; tokens per action 757 vs 1,856 / 1,971 / 2,983; GPT-3.5 run: ReAct 36.43 to 19.76, SwiftSage 62.22 | Lin 2023 (a13, c11-c13) | single |
| System 2 Attention | Opinion QA 62.8 baseline, 82.0 oracle, 80.3 S2A, 71.7 debias instruction only; GSM-IC 51.7 to 61.3 | Weston 2023 (a11, b22) | single |
| Distilling System 2 | Last-letter 30.0 to 98.0; coin flip 56.1 to 75.69; TriviaQA bias 51.6 base, 76.0 S2A, 81.3 distilled (56 vs 147-165 tokens); GSM8k direct 9.40, distilled 7.13 vs CoT 52.77 | Yu 2024 (a12, b21, c18) | single |
| Second pass without outside signal | GPT-3.5 GSM8K 75.9 to 74.7; CSQA 75.8 to 41.8; HotpotQA 26.0 to 25.0; with oracle GSM8K 84.3 | Huang 2024 (d13) | established |
| Cost-accuracy on MedQA | GPT-4 0-shot 78.9; GPT-4o 84.4; GPT-4 Turbo Medprompt 90.2; o1-preview 96.0; about 10x cost per 88 / 92 / 96% step | Nori 2024 (d14) | single |
| Document retrieval vs CoT on MedQA-US | GPT-4 83.97 to 82.80; Mixtral 64.10 to 60.02; GPT-3.5 65.04 to 66.61 | Xiong 2024 (d16) | single |
| Verbal confidence as signal | 12 models, n=1,373; only 3 vary confidence; GPT-4o high 83.2% vs medium 45.9% | Griot 2025 (d17) | single |
| Differential recall vs ranking | NEJM 143 cases: dx in list 78.3% (CI 70.7-84.8), first dx 52% (44-61) | Brodeur 2024 (c23, d08) | single |
| Challenge agents on bias-linked cases | 0/80 first answers; top-2 correct 61/80 (76%) vs humans 13/48 (27%), OR 3.49, p=.002 | Ke 2024 (d07) | single |
| AI-assisted clinicians anchor | AMIE alone top-10 59.1%; unassisted 33.6%; with AMIE 51.7% | McDuff 2025 (d09) | single |
| Dual-system pipeline under biased patient | Biased accuracy dual vs alone: GPT-3.5 25.0 to 63.7 (+38.7); Flash-8B 35.5 to 65.8; GPT-4o 73.8 to 72.8 (-1.0). o1-mini alone: 85.1% biased vs best dual 75.5% | Zuo 2026 (d04, d05) | single, confounded |
| AdaptThink | length -53%, accuracy +2.4% (math, 1.5B model) | Zhang 2025 (d18) | single |

## 4. Mechanisms and models

Each model is written so it can be coded.

**4.1 Default-interventionist (DI).** Pipeline: Type 1 produces answer A1 immediately. A monitor decides whether to engage Type 2. If engaged, Type 2 checks A1 and may replace it. Parameters: monitor threshold, Type 2 cost. Failure modes: monitor too lax (Kahneman), or Type 2 only rationalises A1 (Pennycook). Engineering form: generate a direct answer, run a trigger function, run the slow path if triggered. The trigger is the weak point. Data say humans trigger poorly and LLMs trigger poorly (Huang: without an outside signal a second pass does not help; Griot: verbal confidence is nearly always 5).

**4.2 Parallel or logical-intuition model (De Neys, Bago).** Both types run from the start. The fast pass can already contain the logical answer plus a conflict signal. Engineering form: draw several independent fast samples; disagreement among them is the conflict signal; escalate only on disagreement. This is the best-supported candidate for a trigger, but it is untested in medicine at equal tokens (K25, gap 1).

**4.3 Three-stage model (Pennycook 2015).** Stage 1: Type 1 cues. Stage 2: conflict detection. Stage 3: decoupling (suppress the default and think hypothetically) or rationalisation. Two separate bugs: not detecting, and detecting but not overriding. Engineering form: code creates the conflict (a second independent attempt, a checker, a blind comparison) so detection does not depend on the model's own doubt; a separate rule forces the override (the verified result replaces the draft).

**4.4 SwiftSage switch (a13, c12).** Swift acts by default. Switch to Sage when: five consecutive steps with zero reward (stuck); the predicted action is invalid; a critical decision such as the final answer; an exception is suggested. Return to Swift after Sage's actions run. Rules live in code. Result: 84.7 vs 45.3 best baseline, at 757 vs 1,856-2,983 tokens per action. Limits: Swift trained by imitation on the same benchmark; text game; main runs on GPT-4.

**4.5 System 2 Attention (a11).** Step 1: rewrite the input, dropping opinion and irrelevant text. Step 2: answer from the rewrite only. A fixed rewrite beat a "be unbiased" instruction (80.3 vs 71.7). A variant where the original context stays visible scored 74.5 vs 80.3.

**4.6 Distillation (a12).** Run the slow method, filter outputs by self-consistency, train a direct model on them. Works on rephrase, S2A, branch-solve-merge; fails on CoT math. Our agent cannot train. Nearest no-training form: a cache of verified routines or answers (memory).

**4.7 Reflection as structured re-analysis (b06).** Procedure: list findings, list evidence for and against each candidate, re-rank. It differs from "slow down". Human effect is contested (section 5).

**4.8 Challenge agents (d07).** Named roles: devil's advocate for anchoring and confirmation, premature-closure facilitator. Output: second-look differential. Result 76% top-2 from 0% first-answer by case selection; no equal-token control.

**4.9 Learned switch (AdaptThink d18).** A trained policy chooses Thinking or NoThinking. For us only the accounting idea transfers: count response length.

**4.10 Task-type routing (Sprague b19, Liu b20).** Rule: symbolic, math, logic tasks get CoT; recall and pattern tasks get a direct answer. Clinical text tasks: direct (Wu b24).

## 5. What holds up

**Holds (established).**
- Mode instructions do not move human accuracy: Norman 2014 (45.0 vs 44.5), Ilgen 2013 (p=.12). Case complexity and experience dominate.
- Cognitive forcing or bias teaching does not help: Sherbino 2014, with the 2017 and 2020 reviews and the 2011 exploratory study (poor application and retention). Counter-evidence: Lambe 2018 says guided reflection worked in 5 of 28 studies, so reflection and forcing are separate questions.
- Errors come from both types and from knowledge gaps (a05, b03, b04).
- Wrong diagnoses take longer (Norman 2014; van den Berg 2021, N=117).
- Trap rates are model-dependent: weak models fall, strong ones do not (Hagendorff).
- CoT gain is concentrated on math, symbolic and logic; clinical text and recall tasks gain little or lose (Sprague; Wu: 82 of 95 worse).
- A second pass without an outside signal does not help (Huang).
- Reasoning models overthink easy items (Chen).

**Contested or fragile.**
- Reflection (K03, K28). Mamede 2010 (N=36) induced availability bias and fixed it. van den Berg (N=117) could not induce it. A Japanese RCT (N=46) induced it but reflection did not repair it. The supportive follow-ups are from the originating group. No independent success.
- Default-interventionist timeline (K05). Bago and De Neys say correct logic often comes first; classic accounts say it comes second. Exact percentages were not read.
- Knowledge view vs process view (K22). Favours knowledge, but written by one school. Document retrieval did not beat CoT on MedQA-US, so the knowledge view is not yet confirmed for LLMs either.
- Speed effects. The 21-lab replication of time-pressure cooperation found ITT -0.37 against an original 8.6; the effect lived only among compliers. Speed manipulations are weak levers.
- Length as cause. Moell (7 errors, p=.032) says length marks error. Nori says prompting o1 for more reasoning raised accuracy. So length is a symptom of hard items, not shown to be a cause.

**Moderators.** Model strength (CoT gain 5% to 28% for davinci, null for ChatGPT-3.5, -7 points when blocked in GPT-4 on traps; on clinical text the penalty runs -5.8% top quintile to -9.9% bottom). Task type (symbolic gain, pattern and face loss). Knowledge (accuracy about 45% in Norman 2014 means knowledge was the limit). Cue type (planted false consensus costs GPT-4 10.2 points on its own, confirmation about 0).

**Interventions that worked.** CoT on weak models for traps; few-shot trap examples on davinci (2% to 92%); input rewrite S2A (+17.5 on opinion QA); warning or demonstration on GPT-4 for planted bias (gap 5.4 to 1.8 or 0.8); challenge roles on bias-linked cases (single, uncontrolled); structured reflection for some human cohorts (contested).

**Did not work.** "Be careful" instructions; cognitive forcing teaching; named clinical reasoning styles on GPT-4 (all p>.05) and GPT-3.5 (-4 to -8); self-correction without an outside signal; document retrieval on MedQA-US; verbal confidence as a router; self-consistency and reflexion on o1 (-12.8% vs CoT on LancetQA, c24).

## 6. Language models

**Behaviour on trap tasks.** Early GPT-3 behaves like System 1: CRT 3/3 intuitive-wrong, 12 vignettes human-like (Binz and Schulz). Surface changes break it (cab variant 20%; Wason reordered; CRT wording changed still answered $0.10), which suggests memory not analysis. Hagendorff et al. (200 tasks): davinci-003 5% correct, 80% intuitive; ChatGPT-3.5 59% / 15%; ChatGPT-4 96% / 0%. Semantic illusions: 18% / 74% / 88% correct. Caveat: items are famous and may sit in training data; use fresh variants.

**What changed it.** CoT: davinci 5% to 28%. Blocking CoT: GPT-3.5 no change, GPT-4 95% to 88%. Few-shot: 2% to 92%. So newer models internalise the check; the slow-mode gain shrinks with strength. The same model that fails CRT shows model-based behaviour in a two-step task (Binz and Schulz c08), so fast and slow are task-specific, not model-wide.

**When slow mode helps or hurts.** Sprague: gains confined to math, symbolic, logic (14.2, 12.3, 6.9 points); other categories 56.8 vs 56.1. Liu: grammar learning -23.1, face recognition -12.8 (GPT-4o), -14.4 (Claude 3 Opus), exceptions +331% rounds; Claude 3.5 Sonnet showed little loss on grammar (-1.8). Wu: clinical text, 82 of 95 worse; GPT-4o -3.5, R1 -2.1, Gemini-2.5-flash -1.6; drops grow with length. Xie: o1 gains 3.18% from CoT on knowledge QA, but self-consistency and reflexion lowered accuracy by 12.8% on LancetQA. Huang (m1): medical accuracy peaks near 4K reasoning tokens.

**Reasoning models in medicine.** o1-preview on MedQA: 96.0 (Nori) vs GPT-4o 84.4. NEJM: dx in list 78.3%, first dx 52%; exact or close 88.6% vs GPT-4 72.9%. DeepSeek-R1: 93% on 100 MedQA, errors with anchoring (1 of 7), few alternatives, overthinking. Ranking, not recall, is the weak step (K26).

**Prompted clinical styles.** Savage: no gain on GPT-4 (76 vs 72-78), loss on GPT-3.5. Do not add style operators.

**Bias and anchoring.** BiasMedQA: all models lose; GPT-3.5 -37.4% relative. Warnings restore most of GPT-4's loss. Units warning: the "-17.8" style numbers are absolute points, "37.4%" is relative. The pipeline study (Zuo 2026): a conversational plus reasoning model gains up to +38.7 under a planted patient anchor, but o1-mini alone scores 85.1% biased, above every dual result; tokens were not matched; it is a model-swap result. Echterhoff (BiasBuster): GPT-4 admitted 40.5% more students under reject framing; self-rewriting of the prompt beat awareness text on primacy; few-shot debiasing sometimes pushed the admit rate to 0 or 1. McDuff: clinicians anchor on their own first differential even with AMIE (top-10 59.1% alone vs 51.7% assisted).

**Explicit S1/S2 agents.** SwiftSage (rules in code, fewer tokens, higher score). Talker-Reasoner (no numbers). AdaptThink (learned, math). S2A and Distilling (rewrite, compile). None tests per-item routing in medicine at matched tokens.

**Routing signals.** Verbal confidence is weak (most models say 5; GPT-4o 83.2% high vs 45.9% medium). Self-correction without an outside signal fails. Sample agreement and external checks remain untested for routing in medicine.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **No blanket "slow down" or "be careful" mode.** Part: S0, G. [E] Evidence b01, b08, a18, K01. Mode instruction did not change accuracy in N=393 humans; LLM named styles gave no gain (c09).
2. **No bias-lecture or "name your bias" step.** Part: schema section 4b (not to add). [E] b02, a19, b03, a21, a16, K02. Hindsight inflates bias labels (b04), so an LLM judge that "finds" biases in a wrong trace is not evidence (G10).
3. **Treat a long run as a warning sign, not as care.** Part: S0, G (stop rule). [E] b01, b05, b24, K04, K13. Log tokens per item; consider a length-triggered check or restart. Do not push length up.
4. **Mode by model strength and task type.** Part: S0. [E] a08, a09, c03, b19, b20, b24, K08, K11, K12, K13. Direct or short for recall and clinical text; written steps for math, symbolic, logic; none for pattern and similarity tasks. Re-measure per model.
5. **Cheap path for easy items.** Part: S0. [E] c16, b25, K19. Reasoning models used 1,953% more tokens on 2+3; self-training cut tokens 48.6% at equal accuracy.
6. **Trust intuition only where a checkable signal exists or the environment is regular.** Part: G (calibration), S0. [E] b15, a05, K06. Do not trust stated confidence (d17).
7. **Strip social and prior-answer cues from the input; re-derive from findings.** Part: G (re-derive, anchoring guard), S1 input hygiene. [E for trap fragility, S for the fix] a15, b23, a11, b22, K10. The S2A rewrite beat "be unbiased" 80.3 vs 71.7; a short warning helps GPT-4 (K15, single source).
8. **A second pass needs an outside signal.** Part: S0, S5. [E] d13. A plain "check your answer" pass moved GSM8K 75.9 to 74.7 and lost 34 points on CSQA. Triggers must be code-created: disagreement, failed check, invalid output.
9. **Use fresh variants of trap items for any probe.** Part: bench hygiene. [E] c07, a08.

### Test first

- **Router by sample agreement vs always-slow vs never-slow.** S0. [untested] K05, K24, K25, d14. See UNKNOWNS U1.
- **SwiftSage-style code rules (stuck, invalid, critical decision).** S0. [S] a13, c11-c13, K16.
- **Task-type routing (math and symbolic only).** S0. [E for the CoT gain pattern, not yet tested in our loop] K11.
- **Challenge step after the differential.** O, S1-S3. [S] d07, d08, K26, K27.
- **Anchor guard: hide the first draft differential from verify.** G. [S] d09, K29.
- **Input-cleaning rewrite on distractor-laden items.** O. [S] a11, K17.
- **Known-trap case store (2-7 solved examples).** memory. [S] a10, K09, K18.
- **Reflection or compare operator on bias-induced cases.** O. [C] K03, K28, b06, b09, d10. Keep revision tied to located failing evidence (G2); claim no effect size.
- **Retrieval of similar cases vs added deliberation.** S0, memory. [C] K22, d16.
- **Cap reasoning length (about 4K tokens) on clinical items.** S0, G. [S] c25, K13.

## 8. Concrete tests on our bench

Arms get equal total tokens (generated plus reasoning) unless an arm is "single pass". Report accuracy and accuracy per token.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Router | MedQA-US and NEJM-style cases, mixed easy and hard | (a) always-CoT, (b) never-CoT, (c) route by 3-sample agreement, escalate to CoT on disagreement | Accuracy at fixed total tokens | (c) matches (a) at 30-50% fewer tokens; no loss vs (a) |
| T2 Router signal | Same | Route by (i) verbal confidence, (ii) sample agreement, (iii) question-type rule, (iv) external checker | Accuracy at equal tokens; escalation precision | Agreement beats verbal confidence (d17: confidence near constant) |
| T3 Task-type routing | Items tagged symbolic/math vs recall | CoT only on symbolic/math vs always-CoT vs never | Accuracy, tokens | Equal accuracy, fewer tokens; no loss on recall |
| T4 Anchoring | BiasMedQA seven cue types plus open-ended cases with planted self-diagnosis | Plain; warning; S2A rewrite; challenge step; strong reasoning model alone | Accuracy gap vs unbiased, per cue | Challenge or rewrite closes most of the gap (GPT-4-style 5.4 to under 2 points) |
| T5 Rank and challenge | NEJM CPC open-ended | Differential only vs differential plus rank-and-challenge, same tokens | Top-1 accuracy, in-list rate | Top-1 rises from about 52% toward the 78.3% in-list rate |
| T6 Draft hiding | Cases with a first-draft differential | Verify sees draft vs verify blind to draft | Top-1, anchoring rate | Blind arm higher |
| T7 Length cap | Clinical text and MedQA | Uncapped vs capped at 4K | Accuracy, tokens | Small gain or none; large token saving |
| T8 Reflection | Cases with a primer (similar prior case in context) and without | Compare operator on vs off | Accuracy on primed vs unprimed | Effect only on primed items, if any (contested) |
| T9 Known-trap store | CRT-style and clinical trap variants (fresh) | 0, 2, 7 solved examples vs CoT at equal tokens | Trap-avoidance rate | Examples beat CoT on seen trap classes; no transfer to unseen classes |
| T10 Retrieval vs deliberation | MedQA-US | Similar-case retrieval vs extra deliberation, equal tokens | Accuracy | Unknown; document retrieval alone gave no gain (d16) |
| T11 Perturbation | Vignettes with reordered or renumbered facts | Scaffold vs plain | Accuracy drop under perturbation | Scaffold drops less (re-derive vs pattern-match) |

## 9. What does not transfer, and why

- **Time pressure and forced delay.** For humans these manipulate depth of thought, but compliance was poor (non-compliance 65.9%) and the main effect vanished in the 21-lab replication. For an LLM a token cap is a different lever from a time limit.
- **Teaching biases.** Human teaching fails because of poor transfer and retention. An LLM does not learn from a lecture; a prompt warning works slightly for GPT-4 (gap 5.4 to 1.8). The fix is code-level cue stripping, not a bias-awareness step.
- **Feeling of Rightness.** A human signal based on fluency. For LLMs stated confidence is almost constant (5 of 5), so the direct analogue is unreliable. Use sample disagreement.
- **Working-memory definition of Type 2.** Humans have a small working memory; an LLM has a long context. The analogue is written intermediate steps, which cost tokens and can hurt (Wu, Liu).
- **System 1 as error source.** True for older GPT-3 on trap puzzles, false for ChatGPT-4 (0% intuitive). Human error rates do not predict strong-model error rates.
- **Reflection benefits from learning.** Mamede 2012 shows reflection pays through what is learned over a week. Our agent does not train; the analogue is writing verified lessons to memory, untested here.
- **Neural overlap with cognitive control (b17).** No engineering content.
- **Dual-system pipeline gains (Zuo 2026).** Confounded with model strength; o1-mini alone beat every dual setup. Not a transferable result.

## 10. Open questions

1. At equal tokens, does routing by agreement beat always-CoT and never-CoT on MedQA and NEJM cases? (K25: no study.)
2. Do reasoning models show anchoring and premature closure on open-ended diagnosis, and does a forced challenge step help at equal tokens?
3. Does response length cause error or mark difficulty? (Moell: 7 errors; Nori: more reasoning raised accuracy.)
4. Exact Bago and De Neys percentages; is there an LLM first-sample/second-sample analogue beyond Huang 2024?
5. Is similar-case retrieval better than added deliberation? A 2026 Nature rare-disease agent (PMC12999473) using case retrieval was not read.
6. Has Mamede's reflection effect been independently replicated in humans or LLMs? None found.
7. Which strong-model clinical tasks still gain from CoT? Wu shows loss for most; the 13 of 95 that improved gained only 0.1-2.2 points.
8. Do CRT-style traps remain valid probes when likely in training data?
9. Does the dual-system pipeline (Zuo 2026) beat o1-mini at matched tokens? Currently no.
10. Does the 5-minute early-hypothesis figure (about 95%) hold as recall at k for LLMs? Single secondhand source.

## 11. Sources

[V] = opened and read (full text or substantial page text) this run. [M] = abstract or snippet only.

- [V] Kahneman (2003) Maps of bounded rationality. https://www.nobelprize.org/uploads/2018/06/kahnemann-lecture.pdf (a01-a03)
- [V] Pelaccia et al. (2011) An analysis of clinical reasoning through the dual-process theory. https://pmc.ncbi.nlm.nih.gov/articles/PMC3060310/ (a04, a05, a25)
- [V] Tay, Ryan, Ryan (2016) CRT in medical students. https://pmc.ncbi.nlm.nih.gov/articles/PMC5344059/ (a06)
- [V] Binz and Schulz (2022/2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (a07, c06-c08)
- [V] Hagendorff, Fabi, Kosinski (2023) Human-like intuitive behavior and reasoning biases emerged in LLMs but disappeared in ChatGPT. https://arxiv.org/abs/2212.05206 (a08-a10, b18, c01-c05)
- [V] Weston and Sukhbaatar (2023) System 2 Attention. https://arxiv.org/abs/2311.11829 (a11, b22, c17)
- [V] Yu, Xu, Weston, Kulikov (2024) Distilling System 2 into System 1. https://arxiv.org/abs/2407.06023 (a12, b21, c18)
- [V] Lin et al. (2023) SwiftSage. https://arxiv.org/abs/2305.17390 (a13, c11-c13)
- [V] Liu et al. (2024/2025) Mind your step (by step). https://arxiv.org/abs/2410.21333 (a14, b20, c14)
- [V] Schmidgall et al. (2024) Evaluation and mitigation of cognitive biases in medical language models. https://pmc.ncbi.nlm.nih.gov/articles/PMC11494053/ and https://arxiv.org/abs/2402.08113 (a15, b23, c20, c21, d01-d03)
- [V] Pelaccia, Sherbino, Wyer, Norman (2025) Diagnostic reasoning and cognitive error in emergency medicine. https://pmc.ncbi.nlm.nih.gov/articles/PMC11921069/ (b04)
- [V] van den Berg et al. (2021) Time to diagnose and accuracy. https://pmc.ncbi.nlm.nih.gov/articles/PMC8061054/ (b05)
- [V] Bouwmeester et al. (2017) Registered Replication Report: Rand, Greene, Nowak. https://pmc.ncbi.nlm.nih.gov/articles/PMC5453400/ (b16)
- [V] Gronchi et al. (2024) ALE meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC10813498/ (b17)
- [V] Sprague et al. (2024) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (b19, c15)
- [V] Wu et al. (2025) Why chain of thought fails in clinical text understanding. https://arxiv.org/abs/2509.21933 (b24)
- [V] Moell, Aronsson, Akbar (2025) DeepSeek R1 medical reasoning. https://arxiv.org/abs/2504.00016 (b25, d06)
- [V] Savage et al. (2023) Diagnostic reasoning prompts. https://arxiv.org/abs/2308.06834 (c09, c10)
- [V] Chen et al. (2025) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187 (c16)
- [V] Kojima et al. (2022) Large language models are zero-shot reasoners. https://arxiv.org/abs/2205.11916 (c19)
- [V] Echterhoff et al. (2024) BiasBuster. https://arxiv.org/abs/2403.00811 (c22)
- [V] Brodeur et al. (2024) Superhuman performance of a LLM on physician reasoning tasks. https://arxiv.org/abs/2412.10849 (c23, d08)
- [V] Xie et al. (2024) Preliminary study of o1 in medicine. https://arxiv.org/abs/2409.15277 (c24)
- [V] Huang et al. (2025) m1. https://arxiv.org/abs/2504.00869 (c25)
- [V] Booch et al. (2020) Thinking fast and slow in AI. https://arxiv.org/abs/2010.06002 (c26)
- [V] Christakopoulou et al. (2024) Talker-Reasoner. https://arxiv.org/abs/2410.08328 (c27)
- [V] Zuo, Wan, Wang (2026) Patient cognitive bias in LLM-supported consultations, JMIR e85770. https://pmc.ncbi.nlm.nih.gov/articles/PMC13258194/ (d04, d05; supersedes b26 search summary)
- [V] Ke et al. (2024) Multi-agent conversations to mitigate cognitive bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC11615553/ (d07)
- [V] McDuff et al. (2025) Towards accurate differential diagnosis with LLMs, Nature. https://pmc.ncbi.nlm.nih.gov/articles/PMC12158753/ (d09)
- [V] Japanese randomized trial (2020) Availability bias causes misdiagnoses. https://pmc.ncbi.nlm.nih.gov/articles/PMC7807127/ (d10)
- [V] Mamede and Schmidt (2023) Deliberate reflection. https://pmc.ncbi.nlm.nih.gov/articles/PMC10083910/ (d11)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d13)
- [V] Nori, Usuyama, Horvitz (2024) From Medprompt to o1. https://arxiv.org/abs/2411.03590 (d14, d15)
- [V] Xiong et al. (2024) MIRAGE/MedRAG. https://arxiv.org/abs/2402.13178 (d16)
- [V] Griot et al. (2025) LLMs lack essential metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC11733150/ (d17)
- [V] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417 (d18)
- [M] Norman et al. (2014) Etiology of diagnostic errors. https://pubmed.ncbi.nlm.nih.gov/24362377/ (b01)
- [M] Sherbino et al. (2014) Ineffectiveness of cognitive forcing. https://pubmed.ncbi.nlm.nih.gov/24423999/ (b02)
- [M] Norman et al. (2017) Causes of errors in clinical reasoning. https://pubmed.ncbi.nlm.nih.gov/27782919/ (a16, b03)
- [M] Mamede et al. (2010) Availability bias and reflective reasoning. https://pubmed.ncbi.nlm.nih.gov/20841533/ (a17, b06)
- [M] Mamede et al. (2012) Reflection as a strategy to foster diagnostic competence. https://pubmed.ncbi.nlm.nih.gov/22515754/ (b07)
- [M] Ilgen et al. (2013) Automatic vs analytic testing conditions. https://pubmed.ncbi.nlm.nih.gov/23969355/ (a18, b08)
- [M] Lambe et al. (2018) Dual-process cognitive interventions, systematic review. https://pubmed.ncbi.nlm.nih.gov/26873253/ (b09)
- [M] Evans and Stanovich (2013) Dual-process theories of higher cognition. https://pubmed.ncbi.nlm.nih.gov/26172965/ (a22, b10)
- [M] Bago and De Neys (2017) Fast logic? https://pubmed.ncbi.nlm.nih.gov/27816844/ (b11, d12)
- [M] Thompson, Prowse Turner, Pennycook (2011) Intuition, reason, metacognition. https://pubmed.ncbi.nlm.nih.gov/21798215/ (b12)
- [M] Pennycook, Fugelsang, Koehler (2015) Three-stage model. https://pubmed.ncbi.nlm.nih.gov/26091582/ (b13)
- [M] De Neys (2015) Bias and conflict. https://pubmed.ncbi.nlm.nih.gov/26168420/ (b14)
- [M] Kahneman and Klein (2009) Conditions for intuitive expertise. https://pubmed.ncbi.nlm.nih.gov/19739881/ (b15)
- [M] Sherbino et al. (2011) Cognitive forcing strategies. Europe PMC search record (a19)
- [M] Croskerry (2009) A universal model of diagnostic reasoning. Europe PMC search record (a20)
- [M] Monteiro et al. (2020) Enduring myth of generalisable skills. Europe PMC search record (a21)
- [M] Frederick (2005) Cognitive reflection and decision making. https://www.aeaweb.org/articles?id=10.1257/089533005775196732 (a23; 41% cross-checked via Hagendorff)
- [M] Evans, Barston, Pollard (1983). https://link.springer.com/article/10.3758/BF03196976 (a24; figures from memory, not used)
- [M] Neufeld et al. as cited in Pelaccia 2011 (a25; secondhand)
