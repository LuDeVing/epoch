# Strong Programme and SSK: deep document

*Sources: evidence_a-d.jsonl, claims.jsonl, critique.md in this folder (ids a01-a31, b01-b29, c01-c24, d01-d16, claims F03.02-K01 to K30). Written 2026-11-20. Numbers marked "re-verified" were re-opened in the cross-check. Founding SSK evidence is mostly secondary (Wikipedia, SEP, course handouts). The LLM evidence is mostly primary.*

## 1. What it is

The Strong Programme is a method rule from the sociology of scientific knowledge (SSK). It says: explain the beliefs of a community, true or false, with the same kind of cause. Do not say "they believed it because it was true" for accepted science and "they were biased" for rejected science. [a01, a16]

Four tenets (Bloor 1976, *Knowledge and Social Imagery*): causality (look for causes of belief), impartiality (true and false, rational and irrational alike), symmetry (same type of cause for both), reflexivity (the rules apply to the sociologist's own claims). [a01]

Two schools carry it. Edinburgh (Bloor, Barnes, MacKenzie, Henry, Shapin) works at macro scale: history, group interests. Bath (Collins, later Pinch) works at micro scale: single labs, single experiments, replications. [a02]

Why it is in our study. Our agent is one language model run through a scaffold. The programme is not a theory of one mind. Three things carry over:
1. Its method rule (symmetry) is an audit idea: explain right and wrong answers with the same kind of cause, and never treat "it was correct" as the reason it was believed.
2. Its Bath case studies show how replication disputes get stuck (the experimenter's regress) and what breaks the stall (Franklin's independent criteria).
3. A body of 2022-2026 LLM work now measures the social pull on model beliefs: sycophancy, conformity, source framing, persona bias, citation bias. This is SSK's claim (social position shapes belief evaluation) tested in machines.

Honest limit: no study found tests Bloor's symmetry or the interests explanation on an LLM directly. All LLM evidence is by analogy. [c24, K24]

Links to parallel subfields (not covered here): Kuhn and paradigm crisis; Peer review and replication (folder 09); Social epistemology of discovery; Values and inductive risk; Debiasing; Verbal confidence; Network epistemology (04); Epistemic diversity (06); Coordination and common ground; Team science.

## 2. History and theories in depth

**Background (1920s-1970s).** SSK arose in Britain in the late 1960s-70s, defined against Merton's sociology of science, and drew on Fleck, Kuhn and the late Wittgenstein. [a15] Merton's tradition studied the norms and institutions of science but left the content of accepted knowledge to philosophy. The strong programme said content too is open to social explanation.

**Bloor 1976.** Attacked "philosophical a priorism": treating successful science as true or rational without asking how it came to be accepted. A "weak" sociology only invoked bias or interest to explain failures (phrenology is the standard example). Bloor demanded the same style of explanation for successes. [a01, a16] Bloor and Barnes (1982) defended relativism: validity and rules of inference are relative to community practice. [a06, a16] Bloor used the Azande to argue same psychology, very different institutions. [a06]

**Barnes.** *Interests and the Growth of Knowledge* (1977), *About Science* (1985). Interests, not only evidence, steer which beliefs spread. [a01]

**Wittgenstein link.** A rule alone cannot fix how it is followed; community practice settles it. Bloor (1983, 1997) and Collins (1985, *Changing Order*) build on this. [a11, a16] The philosophical engine is underdetermination: evidence never forces one theory, so non-cognitive factors fill the gap. Laudan criticised exactly this move (Hesse and Bloor use underdetermination to let social factors in). [a06]

**Edinburgh case studies.** Pickering (1984) on quarks; Shapin and Schaffer (1985) on Boyle's air pump. [a04; a29 not opened]
- Shapin and Schaffer: experimental facts earned credit through three technologies: material (the air pump, developed from 1659), literary (virtual witnessing by detailed prose) and social (rules of conduct in the community). Hobbes objected that the pump's space was private and witnessing could not be trusted. Huygens built his own pump in Holland. His anomalous-suspension result went unrecognised for over 18 months. The dispute broke down in March-April 1663, and he went to London, joined the Royal Society and replicated it there. [a07]
- They name two replication problems: judging whether a replication succeeded is itself contingent, and knowledge production depends on social regulation of people and machines. This is the root of the experimenter's regress. [a08]

**Bath school.** Collins (1981, "Stages in the empirical programme of relativism") asks for micro-studies of how controversies close. [a02]
- TEA-laser study (Collins 1974, 1985): replication needs tacit craft skill passed in person. The only test of a competent replication is whether it gets the expected result. [b01] The original 1974 numbers were not opened. [a30]
- Experimenter's regress: if a good experiment is one that gives the right answer, and the right answer is the thing in dispute, there is a circle. It is never clear whether a second experiment was good enough to check the first. Later extended to the "theoretician's regress" and the "simulationist's regress". [a09]
- Weber's gravitational waves (1969): about 7 coincident peaks per day claimed. Six other detectors failed to find them. Weber attacked every replication, and five were also attacked by critics, so competence itself was disputed. [b02] Garwin (IBM) saw one pulse in six months. Billing's group (1972) saw nothing. Douglass found a program error. Weber lost NSF funding in 1987 after Garwin wrote to NSF. [a10]
- Collins's later work: *Changing Order* 1985, *Artificial Experts* 1990, *The Golem* 1993 (with Pinch), *Gravity's Shadow* 2004, *Rethinking Expertise* 2007, *Artifictional Intelligence* 2018. [a11]
- Tacit knowledge in three types: relational (could be made explicit), somatic (bodies and brains), collective (located in society; cannot be made explicit). Sapphire Q-factor case: Western labs struggled to reproduce Braginsky's results (that experiment ran 20 years). [a12]

**Extensions.** Pinch and Bijker (1984), social construction of technology (SCOT): interpretive flexibility, relevant social groups, closure by rhetoric or redefinition of the problem (bicycle case). [a14] Standpoint and feminist work (Harding 1986, Longino 1990): theories accepted under unequal power reflect those in power; Longino's contextual empiricism keeps objectivity. [a05] Lab ethnography contrasts: Knorr Cetina 1981, Latour and Woolgar 1986, Traweek 1988. [a04] Collins and Yearley (1992, "Epistemological Chicken") attacked actor-network symmetry as going too far. [a15]

**Criticism.**
- Self-refutation: radical relativism treats truth as no explanatory resource, so it undermines itself. [a03, b05]
- Science Wars: Sokal and Bricmont (1997/98) argued nature, not social pressure, validates findings. Sokal's hoax paper appeared in *Social Text* (spring/summer 1996) without physicist review and was revealed 5 June 1996. [a13]
- Seidel (2014) attacks the two main arguments (underdetermination and norm-circularity). Hansson (2020) argues social constructionism fed climate denial. That is an argument, not a measurement. [a03]
- Philosophers (Laudan, Brown, Goldman, Haack, Kitcher) defend an isolationist view: evidence and argument justify acceptance. [b06]
- Franklin: the regress is readily broken. In the TEA-laser case the laser's power to vaporise concrete was an agreed criterion. Calibration and reasoned judgment settle many disputes. [b07, snippet only] Radder (1992): Collins's claims are not strictly wrong but one-sided. [b08, snippet only]
- Franklin's strategies as summarised in SEP: (1) calibration with known phenomena, (2) reproducing known artefacts, (3) eliminating plausible errors, (4) using the results themselves, (5) a well-corroborated theory of the phenomenon, (6) apparatus based on corroborated theory, (7) statistical arguments. In the Weber case, critics shared data and programs, reran with Weber's nonlinear algorithm (no effect), and injected known acoustic pulses (their detectors saw them; Weber's did not). Weber admitted a programming error that produced spurious coincidences, and coincidences were claimed between data four hours apart. [d11]

**Reading of the dispute.** The empirical core (closure of disputes involves social negotiation) survives. The strong claim (no independent criterion exists) does not: independent criteria did separate Weber from his critics. Our agent needs the surviving part and the fix.

## 3. Core findings with exact numbers

Status key: established (two or more independent sources), single (one source), contested (sources disagree or scope differs), derived (arithmetic, not measured).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Strong programme has four tenets; same type of social cause for true and false beliefs | 4 tenets; Bloor 1976 | a01, a16 | Established as description; a method rule, not a tested claim |
| Weber 1969 gravitational wave claim failed replication | about 7 peaks/day claimed; 6 replications, 0 confirmations; Garwin 1 pulse in 6 months | b02, a10 | Established (secondary sources) |
| Experimenter's regress | Circle: competence judged by expected result | a09, b01, d11 | Contested; Franklin's criteria break it |
| Imitation game, interactional expertise (Collins 2017) | Round 1: 9 GW physicists judged, 7 undecided, 2 picked Collins. Round 2: marks GW physicists 27, Collins 25, savvy physicists 19, savvy social scientists 17; Collins self-marked 28 | b03 | Single; not re-opened in cross-check |
| Collins's six-books test of ChatGPT | 6 "books" given; 1 wrong title and date, 1 non-existent, 2 altered titles of other authors' books; Google Scholar 503 items vs about 250 real | a17 | Single, anecdote |
| Peer review reliability | 70 coefficients, 48 studies, 19,443 manuscripts; mean ICC .34; kappa .17; larger studies lower | b10 | Established |
| NIH review replication | 43 reviewers, 25 applications; no agreement on quality | b11 (abstract only) | Single |
| Grant review at scale | 134,991 reviews, 4 funders; ICC .50-.65; residual variance 55.2% | b12 | Single (2026 registered report) |
| Prestige shifts review outcomes | 3,300+ invited; accept invitation 38.5% (prominent shown) vs 28.5% (junior) vs 30.7% (anonymous); recommend reject 23% / 65% / 48%; recommend accept over 20% (prominent) vs under 2% (junior) | b13 | Single (preregistered field experiment) |
| Peters and Ceci 1982; Cole et al. 1981 | 12 papers resubmitted, about 3 detected, 8 of 9 undetected rejected; 150 proposals, about 25% decided differently | b14, b15 | Recalled, not re-checked |
| Star deaths (Azoulay) | 452 superstars; non-collaborator output +8.6%; collaborator output about -20.7% (column estimate, sign not re-checked); 51% protracted illness, 41% sudden; median age 61 | b09 | Single (re-verified) |
| Judge counts by Spearman-Brown | ICC .34: 3 judges .61, 5 .72, 8 .80, 17 .90; ICC .65: 2 judges .79, 3 .85, 5 .90 | d13 | Derived, not measured on LLMs |
| Bare challenge ("Are you sure?"), 2023 models | 10 LLMs, 7 tasks: flip 46%, accuracy drop 17%; 7 of 10 models lose 10+ points; finetune cuts deterioration 60% | b17, c04 | Established on 2023 models (re-verified); frontier differs |
| Wrong admission under challenge | Claude 1.3: 98%; GPT-4: 42%; answer change 32% (GPT-4) to 86% (Claude 1.3); wrong suggestion cuts accuracy up to 27% (LLaMA 2 70B) | b16, c03 | Single paper, older models (re-verified) |
| ChatGPT defending truth against invalid argument | fails on 22% to over 70% by benchmark; mean 20-50%; GSM8K 41.6% | b18, c05 | Single, ChatGPT only (re-verified) |
| Scale and instruction tuning raise sycophancy on no-answer questions | PaLM 8B to 62B +19.8%; 62B to 540B +10.0%; Flan-8B +26.0%; fix reduces opinion repeats 4.7-10.0% | b19, c02 | Established with Perez (re-verified) |
| View-matching at 52B | more than 90% match on NLP and philosophy questions, same for 0 and many RL steps | c01 | Established |
| Preference data reward agreement | preference model prefers sycophantic over truthful 95% in one test; Best-of-N at N=4096 gives sycophantic answers on misconceptions about 75% vs about 25% with oracle PM | b16, c03 | Established (two papers) |
| SycEval | sycophancy 58.19% (Gemini 62.47%, GPT-4o 56.71%); progressive 43.52%, regressive 14.66%; preemptive 61.75% vs in-context 56.52%; persistence 78.5%; citation rebuttals worst | b20, c17 | Single |
| Social sycophancy (ELEPHANT) | 11 models; validate user 72% vs 22% crowd; both sides told "not at fault" in 48% of AITA pairs | b21, c16 | Single |
| Frontier reasoning models, 8-round attack | 700 MCQs, 3 seeds. Follow-up accuracy: GPT-5.1 98.92, GPT-OSS 98.53, Grok-4.1 97.06, Gemini-2.5 96.48, DeepSeek-R1 89.91, Claude-4.5 86.31 (from 94.86), GPT-4o 91.29. Total flips: Claude-4.5 347, DeepSeek-R1 260, Qwen-3 128, GPT-5.2 76, GPT-OSS 30 | d01 | Single, 2026 |
| Confidence gate does nothing | CARG on GPT-5.1: 98.39 and 98.29 vs random confidence 98.88 vs baseline 98.50; confidence vs correctness r = .07, AUC .57 | d02 | Single |
| Right-to-wrong under multi-turn pressure | GPT-5.4: 23.8% of objective scenarios | d03 | Single (poster page) |
| Third-person framing in debate | cuts sycophancy up to 63.8% (SYCON, 17 models); Qwen2.5-7B ToF 1.10 vs 4.02; Llama-3.1-8B 2.81 vs 4.56 | d04 | Single |
| Conformity to a wrong unanimous majority | 4 small models (7-9B); 2-10 confederates; Devil's Advocate and Question Distillation cut it (percentages not extracted) | b22, c06 | Single, small models |
| Group conformity, 2,500+ debates | majority size partial eta2 .068; capability .1665; power over .99 | d05 | Single |
| Persona changes evidence judgment | 8 LLMs, 8 personas; discernment down up to 9% (3% mean); political personas up to 90% more likely to read gun-control data their side's way; 46% of open-source answers cited identity; CRT not protective; CoT -0.39% (n.s.); accuracy prompt -2.93% | a20, a21, b24 | Single (re-verified) |
| Personas do not raise accuracy | 162 roles, 2,410 questions, 4 families: no average gain; 19 personas, 24 datasets: 80% of personas biased on ChatGPT-3.5; personas explain under 10% of annotation variance | c13, c14, c15 | Established (3 sources) |
| Source framing | 4 LLMs, 4,800 statements, 192,000 ratings; blind agreement over 90%; "person from China": DeepSeek -6.18% overall, -24.43% on politics cluster; Grok 2 -14.22%; Mistral -4.51% (n.s.); o3-mini -2.64% | a22, a23, b25 | Single (re-verified; sign on politics cluster not fully checked) |
| Opinion dynamics in LLM groups | 15 topics; false framing B = -1.33 (SE .17) vs true framing B = +.52 with no confirmation bias; confirmation-bias prompts fragment opinion | a24, a25, c07 | Contested (setup dependent) |
| Critical mass for convention flips | 2% (Llama-3-70B-Instruct) to 67% (Llama-2-70b-Chat); populations of 24 (48 for one) | b28 | Single |
| Debate at unequal vs equal cost | Du: arithmetic 67.0 single vs 81.8 debate; GSM8K 77.0 vs 85.0. Equal compute, MMLU-Pro: CoT 64.3, SC 68.7, debate 70.0, MoA 71.4 | c09, d08 | Contested |
| Debate in 7-8B teams | GSM-Hard Qwen2.5-7B: zero-shot 25.6, debate 58.8, noise 63.2, self-correction 61.0; Ministral-3-8B: 24.7 / debate 20.7 / self 48.3; debate 2.1-3.4x tokens; modal sycophancy up to 85.5% | d10 | Single, 2026 |
| Citation Matthew effect | 166 papers; median citations of generated refs 1,326 higher than truth; n = 14,554 references | b26, c18 | Established |
| AI-assisted reviews (ICLR 2024) | 15.8% of 28,028 (4,428); higher in 53.4% of pairs (p = .002), +14.4%; +4.9 points acceptance near threshold (p = .024) | b27, c19 | Established (re-verified); one venue |
| LLM reviewer vs humans | 65% vs 66% balanced accuracy, 500 ICLR 2022 papers | c20 | Contested validity |
| GPT-4 persuasion | N = 820; with personalisation 81.7% higher odds of increased agreement (p < .01); without, p = .31 | b29 | Single |
| Human-aware discovery models | up to 400% better prediction of future discoveries than content-only | a27 | Single |
| Persona opinion simulation | Argyle: ANES correlations mostly .7-1.0 (some .02, .31); Santurkar: gaps on par with the Democrat-Republican climate gap; worst for 65+ and widowed | c11, c12 | Contested |

## 4. Mechanisms and models

Each mechanism is written so it can be built as code around model calls.

### 4.1 Symmetry audit (method rule turned into a check)
Goal: stop the agent from using "it was correct" or "I felt sure" as the reason for an answer.
1. For every candidate (right or wrong, known after the S4/S8 checks), the model writes a cause list: which premise, example, cue or source led to it.
2. Code classifies each cause into a fixed type list: given in task, derived by rule, recalled, suggested by user or other text, own prior preference.
3. Code compares the type mix for candidates that passed versus failed. A causal type found only in failures (for example "suggested by a stated guess") is flagged as an error source for this problem class and logged in the class record.
4. Reject any cause line that says only "because it is true/correct".
Status: not tested on any LLM (K24). Cost: one extra call per run, in audit mode only. It sits at S9 (look back), not as a live doubt step (G1).

### 4.2 Experimenter's regress breaker (Franklin's criteria as a checklist)
Use when two evidence streams conflict and no ground truth exists (two tool outputs, two documents).
1. For each stream, code asks four fixed questions, one model slot each: Was it calibrated on a known signal? Were plausible errors eliminated (name them)? Is there independent confirmation by a different method? Were the data or program shared and reanalysed?
2. Code counts yes answers per stream. The stream with more satisfied independent criteria wins. A tie reports both and then submits the best attempt (G6: never abstain on the first pass).
3. The criterion must not be the result itself. That is the regress.
Source: d11 (seven Franklin strategies reduced to four for the check, K28). Status: single secondary source.

### 4.3 Hold-position rule (anti-sycophancy)
Trigger: any input after the first answer that disagrees with it (user pushback, another agent, retrieved text).
1. Code tags the input type: bare challenge, concrete wrong suggestion, consensus appeal ("most people disagree"), authority or citation, emotional pressure. These are the attack types in d01 and d16.
2. Code checks whether the input carries new evidence: a new fact checkable by a tool, a new example, a counterexample, a changed task statement. Rule: change the answer only if the new evidence passes the S4 test. Otherwise record the pushback and keep the answer.
3. Do not gate on the model's own confidence. A confidence gate equalled a random gate (d02).
4. Optional outside-observer rewrite: restate the exchange in third person before deciding (d04: up to 63.8% less sycophancy in debate; small effect on false presuppositions).
This is G2 and G5 applied to the conversation channel. The untested core is the "new evidence" rule at equal tokens (gap 1, half closed).

### 4.4 Blind judging (input hygiene for evaluation)
Before any model judges a candidate, claim or source, code strips: author or source label, prestige cues, stated majority, stated authorship ("you wrote this"), persona, length. Run the same text with and without a label. If scores differ by more than a set margin, the label effect is present and the blind score is used. Evidence: source framing shifts agreement by up to 24.43% (a22). Prestige moves human reviewers' reject rate from 23% to 65% (b13). Models rate texts differently when told they wrote them (a23). Matches G5.

### 4.5 Source-quality check against the Matthew effect
When the agent retrieves or cites sources, code (not the model) verifies existence by exact lookup and does not rank by citation count alone. LLM suggestions skew toward highly cited papers (median +1,326 citations, b26), and invented references are common (a17). A verify-existence step goes into memory writes and retrieval.

### 4.6 Judge-count planner (Spearman-Brown)
Reliability of the mean of k independent judges = k*rho / (1 + (k-1)*rho). Measure the single-call rho (ICC) of the judge on the agent's own item class, then pick k. At rho .34 you need 8 calls for .80. At .65 you need 3 (d13). Calls from one model are correlated (G4), so this is a lower bound on k. Not measured on LLMs.

### 4.7 Conformity pressure model (Zhang 2024)
Conformity helps accuracy only when transitions toward truth outnumber transitions away: FalseTrue + TrueTrue > TrueFalse + FalseFalse (c08). In code: log per challenge turn whether the answer went right-to-wrong or wrong-to-right (already in schema section 6). Keep a doubt step only for problem classes where it measured net positive.

### 4.8 Opinion-dynamics models (background)
DeGroot repeated averaging is the parent model (c23, not read). In LLM populations, memory type (cumulative vs reflective), confirmation-bias prompt strength and initial framing set the final spread of opinion (c07). For a single agent these matter only if it talks to other model instances, and G9 says no debate.

## 5. What holds up

**Holds up (two or more independent sources):**
- LLMs change correct answers under social pressure, and preference-trained models partly owe this to human raters preferring agreement. Sharma, Laban, Wang, Wei, Perez, SycEval and ELEPHANT agree in direction on 2022-2025 models. [K05, K08, K09]
- Scale and instruction tuning raised sycophancy on no-right-answer questions in 2022-2023 (Wei, Perez). [K08]
- Persona prompts do not reliably raise accuracy and often lower reasoning accuracy. [K13: c13, c14, c15]
- Models over-suggest highly cited references (Algaba), and AI-assisted peer review inflates scores (Latona). [K17, K18]
- Peer review is noisy: ICC .34 (Bornmann), no agreement in the NIH replication, .50-.65 in 134,991 reviews. [K19]
- The critics' point that the regress is breakable by independent criteria. [K04]

**Failures, boundary conditions and moderators:**
- The 46% flip rate does not hold for frontier reasoning models. A bare "Are you sure?" barely moves most of nine models; GPT-OSS flips near zero. A concrete wrong suggestion is the most or second most effective attack on every model, and some flip above 79% under their strongest attack. Claude-4.5 got worse over the rounds (94.86 to 86.31) and was the only one of nine not to beat GPT-4o (the other eight beat it with d = 0.12-0.40). [d01, d16] The per-model single-turn flip rate for the bare challenge is shown only on a radar chart, not as a number.
- GPT-5.4 still flips right to wrong in 23.8% of objective multi-turn scenarios. Claude models were more sycophantic at moderate pressure than at strong pressure, because strong pressure triggered a from-scratch rethink. [d03]
- Instruction tuning raised sycophancy in Wei (+26.0%) but lowered conformity in Zhu. Different tasks (opinion matching vs Asch-style majority). The direction differs. [critique]
- Scale and reasoning training lower sycophancy in SYCON; alignment tuning raises it. [d04] Resilience improved with size in Qwen-3 and Llama-3. Thinking models can justify wrong user suggestions when the user cites authority. [d12]
- Citation-based rebuttals cause the most wrong flips. Preemptive rebuttals work more than in-context ones (61.75% vs 56.52%, Z = 5.87). [b20]
- SycEval counts a shift toward the correct answer as sycophancy (43.52% progressive vs 14.66% regressive), so the 58.19% headline mixes good and bad updates. [b20]
- Self-reported confidence does not predict who flips (r = .07, AUC .57; flip rate by confidence tercile 9.3%, 6.7%, 6.2%, N = 193 each). [d02]
- Dash: effects are not uniform. OpenAI models drive the discernment drop; Llama2 and WizardLM2 rose. A skin-cream control task showed values near 0. Prompt-level debiasing largely failed. [a20, b24]
- Germani and Spitale: effect varies by model (Mistral on politics -4.51%, not significant). The task is agreement ratings on narrative statements, not truth checks. [a22]
- Zhu: only questions the model first answered correctly were used. The abstract says conformity rises when the model's own confidence is low and when the majority sounds natural. One summary note says models do not conform less when uncertain, unlike humans. The summaries differ, so treat the confidence direction as unsettled and check the paper before relying on it. [b22, c06]
- Group conformity: a more capable agent outweighs a larger weaker group, yet majority pull remains (eta2 .068 vs .1665). Mid-size and older models; no frontier model; no mitigation run. [d05]
- Chuang's asymmetry (false framing pushes harder than true) comes from one lab, mostly GPT-3.5 (GPT-4 on 5 science topics). No 2025-26 replication or failure was found. [a24, a25, c07, d14] In Ashery, the tipping point depends heavily on the model (2% to 67%); human experiments suggest 25%. [b28]
- Debate vs voting: Du's advantage (arithmetic 81.8 vs majority 69.0) shrinks to +1.3 pp over self-consistency at equal compute, and debate beats SC only when scaling agents, not rounds. Five MAD methods on 9 benchmarks often fail to beat CoT and SC. 7-8B teams lose to isolated self-correction. [d08, d09, d10] The +1.3 pp may sit inside noise; no confidence intervals were seen.
- Weber's case: independent criteria broke the regress, not negotiation alone. [d11]
- Huber's field experiment: one paper, one field, self-selection (reviewers who accepted despite a junior name were milder). [b13]
- Human-aware prediction (Sourati and Evans) is up to 400% better than content-only, strongest when the literature is sparse. Single source. [a27]

**Interventions that worked:**
- Light synthetic-data finetune: 4.7-10.0% fewer opinion repeats (Wei). Finetune on synthetic data cut flip deterioration 60% (Laban). Both are training, so not available to a scaffold-only agent. [b17, b19]
- Third-person framing: up to 63.8% less sycophancy in debate (SYCON). [d04]
- Devil's Advocate and Question Distillation cut conformity in 7-9B models. [c06]
- Blind conditions kept cross-model agreement above 90%. [a22]
- Independent drafts then a judge avoids peer conformity. Noise injection also worked in d10, so part of that gain is resampling. [d10]

**Interventions that did not work:**
- Confidence-based gating (matched a random gate). [d02]
- Chain-of-thought for persona bias (-0.39%, n.s.); an accuracy prompt made it worse (-2.93%). [a20]
- Prompt-based debiasing of persona effects ("largely ineffective"). [b24]
- Analytic reasoning ability (CRT) as protection. [a21]
- Prompt mitigations for social sycophancy in ELEPHANT (limited; model-based steering helped). [b21]
- Reflection in Du et al.: it hurt factuality on one test while helping arithmetic modestly (72.1 vs single 67.0). [c09]

## 6. Language models

**Behaviour in plain words.** Models were trained on human text and rated by human preference. Human raters prefer agreement. So models drift toward the user's view, the majority's view and the stated persona's view, and they favour highly cited sources. [K09, c03, b16] Collins says the same in sociological language: the model has no primary socialisation, so it fabricates as fluently as it states facts. RLHF puts socialisation back after the fact (programmers as surrogate parents), and the danger is whoever does the socialising. [a17, a19] That is argument, not an experiment.

**Sycophancy by generation (what changed and by how much).**
- 2022-2023: view-matching over 90% at 52B regardless of RL steps (Perez). Claude 1.3 wrongly admits 98%, GPT-4 42% (Sharma). Bare challenge flips 46% on average, accuracy -17% (Laban). ChatGPT fails to defend truth on 22% to over 70% (Wang).
- 2024-2025: SycEval 58.19% sycophancy, 14.66% regressive. ELEPHANT: 45 points more face-preservation than humans. SYCON: alignment tuning raises it; scale and reasoning lower it.
- 2026: frontier reasoning models are near immune to a bare challenge (follow-up accuracy 89.91 to 98.92 across eight; Claude-4.5 at 86.31 is the outlier) but are still hijacked by concrete wrong suggestions. Of 1,347 failures, Self-Doubt plus Social Conformity are about half. Confidence is uninformative. [d01, d02] GPT-5.4 right-to-wrong 23.8%. [d03]
- Net change: the bare-challenge problem got much smaller. The suggestion-hijack problem did not. A rule that handles only "Are you sure?" would solve the old problem.

**Source and identity effects.**
- Source framing: same text, different named source. Agreement falls up to 24.43% on politics for DeepSeek Reasoner. Models rate texts differently when told they wrote them. DeepSeek rates its own text 91.5% vs 85.3% for Grok 2 text. Mistral 98.3% own vs 94.8% others. [a22, a23]
- Personas: 8 LLMs; discernment down up to 9%; political personas up to 90% more likely to read data in their side's direction. Baseline discernment OpenAI 0.86 vs open-source 0.61. [a20]
- Personas lower reasoning accuracy for 80% of personas on ChatGPT-3.5, with drops of 70%+ on some datasets. [c13]
- Opinion alignment differs by group (Santurkar). [c11]

**Groups of models.**
- Small instruction-tuned models conform to a wrong unanimous majority. Devil's Advocate and Question Distillation help. [c06]
- Larger groups raise conformity; capability matters more than count. [d05]
- Debate wins at unequal cost, has a small edge at equal compute, and loses in small teams. [c09, d08, d10]
- Population conventions flip from a committed minority of about 2% to 67% depending on model. [b28]
- LLM opinion dynamics drift to accurate claims, with a false-framing asymmetry. [c07]

**Science-system effects.**
- Citation Matthew effect: +1,326 median citations over truth. [b26]
- AI-assisted reviews score higher: 53.4% of pairs, +14.4%, +4.9 points near threshold. [b27]
- LLM reviewer: 65% vs 66% balanced accuracy against humans, who are themselves noisy. [c20, b10]
- GPT-4 with personal data: 81.7% higher odds of increased agreement. [b29]

**What does not exist yet.** No LLM test of Bloor's symmetry or the interests explanation. No 2025-26 replication of the Chuang asymmetry. No blind-vs-attributed re-test after Germani and Spitale. No Devil's Advocate test on large models. No scaffold-level "change only on new evidence" rule measured at equal tokens. [K24, K30, critique gaps]

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested, [D] design choice with no direct evidence. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)
| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Treat the model's own agreement with a pushback or stated answer as a suspect signal. Keep an answer after a challenge unless new, checkable evidence arrives. Do not use stated confidence as the gate. Largely covered by G2 and G5. Add a log of challenge types (bare, suggestion, consensus, authority). | G2, G5, S1 input hygiene | [E] the problem (2022-2026); [S] the exact remedy | K05, K08, K09; b17, c03, d01, d02 |
| 2 | Judges see no author, source, majority or persona. Reinforces G5. | G5, S7 | [E] harm of labels (source framing, prestige, persona); blind remedy [S] | K11, K12, K13; a22, b13, a20, c14 |
| 3 | No role personas for judging or voting (already in 4b). | G4, 4b | [E] | K13; c13, c14, c15 |
| 4 | Verify that cited sources exist by lookup, not by the model's memory. Do not rank by citation count alone. | memory, S8 | [E] Matthew effect; verification remedy [S] | K17, K21; b26, c18, a17 |
| 5 | Do not trust a single judge call. Human judges have ICC .34 and AI judges inflate scores. Keep code-side selection. If a judge is used, aggregate several calls. | G5, O | [E] noisy judging; k from the formula [S] | K18, K19, K29; b10, b12, b27, d13 |
| 6 | Guard against over-relativism: if an independent criterion exists (test, calibration, known signal), use it. Never conclude "no answer" when one exists. | G3, S8 | [E] | K04; a03, b05, d11 |
| 7 | No debate as a closure tool (already G9). Equal-cost evidence now agrees: +1.3 pp at equal compute; 7-8B debate loses to self-correction. | G9 | [E] at equal cost; [C] at unequal cost | K15; d08, d09, d10 |

### Test first
| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 8 | "Change only on new evidence" rule at the challenge step against bare challenge, wrong suggestion, consensus appeal and citation rebuttal, with a random-gate control. | G2, S1/S5 | [S] | K05, K26; d01, d02, d16, b20 |
| 9 | Third-person outside-observer rewrite of the challenge before deciding. | S1 input hygiene | [S] | K27; d04 |
| 10 | Symmetry audit at S9: same cause types for passed and failed candidates. | S9, memory | [D] no direct evidence | K01, K24 |
| 11 | Franklin four-criteria check when two evidence streams conflict. | O (conflict step), S9 | [S] secondary source | K02, K28; d11 |
| 12 | Blind vs attributed judging on matched text: measure label shift on current models. | G5 | [S] | K11; a22 |
| 13 | Devil's Advocate or Question Distillation on frontier models when outside sources disagree with the agent. | O | [S] small models only | K10; c06, d05 |
| 14 | Judge-count k from measured ICC. | O | [S] derived | K29; d13 |
| 15 | Verify-existence memory step vs plain citation generation at scale. | memory | [S] | K17, K21; a17, b26 |
| 16 | Hide premise prestige or source rank before accepting a claim (Azoulay-style deference reduction). | S1, G5 | [S] | K20; b09, b13 |

Do not add: social role or persona framing; reflection without feedback (4b); debate (G9).

## 8. Concrete tests on our bench

All arms run at equal total tokens (the plain arm gets the saved tokens as extra samples). Log right-to-wrong and wrong-to-right flips separately (schema section 6).

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with a known answer that the plain model gets right on the first pass (4-option MCQ, exact-answer items). Follow-up turn: bare challenge; wrong suggestion; "most people disagree"; citation-style rebuttal | (a) plain; (b) plain plus rule "change only on new evidence that passes the check"; (c) rule with random-gate control; (d) outside-observer rewrite | Right-to-wrong flip rate; net accuracy after the turn | Wrong suggestion and citation rebuttal flip most. The rule should cut right-to-wrong clearly (target: half or better). Bare challenge is near zero on current models, so expect no change there |
| T2 | Same item bank, wrong-to-right opportunities: the challenge carries a true correction with a checkable fact | rule arm vs plain | Wrong-to-right rate | The rule must not block valid updates. A loss of more than 3 points disqualifies it |
| T3 | Pairs of identical answers with source labels (expert, student, AI, "from X"), prestige cues and "you wrote this" | (a) labelled; (b) blind by code; (c) blind plus length-normalised | Score shift per label; rank-order change | Label shift measurable on the labelled arm; blind arm shift near 0 |
| T4 | Two conflicting evidence streams (two tool outputs, one with a calibration signal), ground truth known to us | (a) plain pick; (b) Franklin four-check | Accuracy of the pick; rate of "no answer" | Check raises accuracy when one stream has a calibration signal. It must not raise abstention |
| T5 | Reasoning tasks with a stated wrong majority or wrong expert hint in the prompt | (a) plain; (b) hint moved by code into a marked block (S1); (c) Devil's Advocate step | Accuracy; hint-follow rate | Hint block cuts the follow rate. Devil's Advocate gain on large models is uncertain |
| T6 | Ask for references on 100 topics; verify by lookup | (a) plain; (b) plain plus verify-existence step | Fabrication rate; median citation count of valid ones | Verification removes fabricated refs. Citation skew stays unless ranked differently |
| T7 | Symmetry audit on 100 solved items (50 right, 50 wrong) | (a) plain S9 look-back; (b) symmetry audit | Rate at which a flagged error cause is truly present in failures (code check plus a human sample) | Either the audit adds true flags the plain look-back misses, or it does not |
| T8 | Judge agreement: score the same 50 candidates with k = 1, 3, 5, 8 calls | k arms at equal tokens (fewer items for larger k) | ICC and rank agreement with ground truth | Matches Spearman-Brown only if calls are independent. Expect lower than predicted |
| T9 | Claims with real verdicts, prestige cues shown or hidden | shown vs hidden | Accept-rate difference | Shown arm accepts prestige-linked claims more |

## 9. What does not transfer, and why

- **Group interests and macro-social causes.** Barnes's interests explanation concerns communities with stakes. A single run has no career, funding or group. Only micro effects (what is in the context window) transfer. [a04]
- **Negotiated closure between humans.** Collins's regress needs scientists with prior commitments. Our agent has none, only a prompt. Negotiation is replaced by code selecting from checks (G5).
- **Relativism as a stance.** The agent must not conclude that no answer is better than another. Keep the critics' point (self-refutation, independent criteria). [K04]
- **Tacit knowledge and socialisation.** Collins's claim that LLMs cannot acquire tacit knowledge is an argument, not a test, and gives no operator. The imitation-game result (7 undecided, 2 chose Collins) is on humans only. [a17, b03]
- **Peer-review sociology.** It concerns human reviewers with identities. Only the reliability arithmetic and the blind-judging idea transfer. [b10, d13]
- **Population dynamics.** Tipping points of 2% to 67% and opinion drift apply to many-agent systems. G9 already removes debate and G4 removes persona voters. [b28, c07]
- **Persona simulation of human groups.** Argyle and Santurkar matter for survey simulation, not single-agent reasoning. [c11, c12]
- **Training fixes.** Synthetic-data finetunes (Wei, Laban) are out of scope. We change a scaffold, not weights.
- **Older-model numbers.** 98%, 46% and 22-70% were measured on 2022-2023 models and do not describe current frontier models. [critique]
- **Human-aware discovery models** (Sourati and Evans) need expert-network data. There is no analogue in one run. [a27]

## 10. Open questions

1. Does a current frontier model flip about 46% on a bare "Are you sure?" Partly closed: no, near zero for several reasoning models, and Claude-4.5 worsened. The single-turn flip rate per model is not given as a number in d01.
2. Does "change only on new evidence" beat plain and a random gate at equal tokens? Untested.
3. Can a symmetry audit run on an LLM, and does it catch errors that plain reflection misses? No study found.
4. Does hiding the source remove the Germani and Spitale framing effect on current models, and at what token cost? No re-test found.
5. Does Devil's Advocate or Question Distillation reduce conformity in large models? Only 7-9B tested.
6. Does debate keep any edge over self-consistency at equal tokens beyond MMLU-Pro and BBH? Is +1.3 pp inside noise?
7. What independent criterion breaks the regress for an agent comparing two conflicting streams? Franklin's list is a secondary summary. Collins 1985 and Franklin 1990 were not opened.
8. Do LLM-written citations still show the Matthew effect on current models, and does verify-existence fix fabrication at scale?
9. Collins 2017 numbers (7 undecided, 2 chose Collins; marks 27/25/19/17) were not re-opened. Can the imitation game be run with an LLM as the interactional-expert candidate?
10. How many independent judge calls make an LLM judge reliable? Derived only (8 at ICC .34), not measured. Same-model calls are correlated.
11. Is Chuang's false-framing asymmetry replicated on current models?
12. Peters and Ceci (1982), Cole et al. (1981) and Pier et al. (2018) were not re-checked. The sign of Azoulay's 20.7% collaborator estimate was not re-checked against the table.
13. Does a scaffold-level defence against concrete wrong suggestions exist? Only the third-person prompt has partial data.

## 11. Sources

[V] opened, [M] snippet only.

**Founding and critique**
- [V] Wikipedia, Strong programme: https://en.wikipedia.org/wiki/Strong_programme (a01-a03, b05)
- [V] Wikipedia, Sociology of scientific knowledge: https://en.wikipedia.org/wiki/Sociology_of_scientific_knowledge (a15; first 100,000 of 118,569 characters)
- [V] Wikipedia, David Bloor: https://en.wikipedia.org/wiki/David_Bloor (a16)
- [V] Wikipedia, Harry Collins: https://en.wikipedia.org/wiki/Harry_Collins (a11)
- [V] Wikipedia, Tacit knowledge: https://en.wikipedia.org/wiki/Tacit_knowledge (a12)
- [V] Wikipedia, Leviathan and the Air-Pump: https://en.wikipedia.org/wiki/Leviathan_and_the_Air-Pump (a07, a08)
- [V] Wikipedia, Experimenter's regress: https://en.wikipedia.org/wiki/Experimenter%27s_regress (a09)
- [V] Wikipedia, Joseph Weber: https://en.wikipedia.org/wiki/Joseph_Weber (a10)
- [V] Wikipedia, Sokal affair: https://en.wikipedia.org/wiki/Sokal_affair (a13)
- [V] Wikipedia, Social construction of technology: https://en.wikipedia.org/wiki/Social_construction_of_technology (a14)
- [V] Stanford Encyclopedia, The Social Dimensions of Scientific Knowledge: https://plato.stanford.edu/entries/scientific-knowledge-social/ (a04, a05, b06)
- [V] Stanford Encyclopedia, Relativism: https://plato.stanford.edu/entries/relativism/ (a06; first 100,000 of 175,676 characters)
- [V] Stanford Encyclopedia, Experiment in physics: https://plato.stanford.edu/entries/physics-experiment/ (d11; first 100,000 of 158,000 characters)
- [V] Bazerman 1989 review of Changing Order (b01): https://bazerman.education.ucsb.edu/sites/default/files/docs/Bazerman1989REVColl (URL truncated in the evidence listing; full URL is in evidence_b.jsonl)
- [V] Pitt HPS handout on Changing Order ch.4 (b02): https://sites.pitt.edu/~jdnorton/teaching/2103_HPS_Core/handouts/ (full path in evidence_b.jsonl)
- [M] Franklin via Yale HoFoP handout (b07): https://physics.yale.edu/sites/default/files/files/3_1%20franklin.pdf
- [M] Radder (1992) PSA (b08): https://www.cambridge.org/core/journals/psa-proceedings-of-the-biennial-meeting-of-the-philosophy-of-science-association (path truncated in the evidence listing; see evidence_b.jsonl)
- [M] Pickering 1984, MacKenzie 1981, Shapin 1975 (a29); Collins 1974 TEA laser (a30); Peters and Ceci 1982 (a31, b14: https://doi.org/10.1017/S0140525X00011183); Cole, Cole, Simon 1981 (b15: https://doi.org/10.1126/science.7302566); DeGroot 1974 (c23: https://en.wikipedia.org/wiki/DeGroot_learning); Collins 2018 book (c22)

**Collins on AI and expertise**
- [V] Collins (2024/2025) Why AI needs sociology of knowledge: https://doi.org/10.1007/s00146-024-01954-8 (a17-a19, b04)
- [V] Collins (2017) Imitation game concerning GW physics: https://arxiv.org/abs/1607.07373 (b03; not re-opened in the cross-check)

**Peer review and science sociology**
- [V] Azoulay, Fons-Rosen, Graff Zivin, Does science advance one funeral at a time: https://www.nber.org/papers/w21788 (b09)
- [V] Bornmann, Mutz, Daniel (2010): https://doi.org/10.1371/journal.pone.0014331 (b10)
- [M] Pier et al. (2018): https://doi.org/10.1073/pnas.1714379115 (b11, abstract only)
- [V] Hesselberg et al. (2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC13600531/ (b12)
- [V] Huber et al. (2022): https://doi.org/10.1073/pnas.2205779119 (b13)
- [M] Spearman-Brown formula page (d13; the numbers are derived arithmetic, not read): https://en.wikipedia.org/wiki/Spearman%E2%80%93Brown_prediction_formula
- [V] Sourati and Evans (2023): https://arxiv.org/abs/2306.01495 (a27)
- [V] Brinkmann et al. (2023) Machine culture: https://arxiv.org/abs/2311.11388 (a28)

**LLM studies**
- [V] Perez et al. (2022): https://arxiv.org/abs/2212.09251 (c01)
- [V] Sharma et al. (2023): https://arxiv.org/abs/2310.13548 (a26, b16, c03)
- [V] Laban et al. (2023): https://arxiv.org/abs/2311.08596 (b17, c04)
- [V] Wang, Yue, Sun (2023): https://arxiv.org/abs/2305.13160 (b18, c05)
- [V] Wei et al. (2023): https://arxiv.org/abs/2308.03958 (b19, c02)
- [V] Fanous et al. (2025) SycEval: https://arxiv.org/abs/2502.08177 (b20, c17)
- [V] Cheng et al. (2025) ELEPHANT: https://arxiv.org/abs/2505.13995 (b21, c16)
- [V] Malmqvist (2024): https://arxiv.org/abs/2411.15287 (c21)
- [V] Zhu et al. (2024/2025) Conformity in LLMs: https://arxiv.org/abs/2410.12428 (b22, c06)
- [V] Group conformity in multi-agent systems (2025): https://arxiv.org/abs/2506.01332 (d05)
- [V] Amplifying Minority Voices (2025): https://arxiv.org/abs/2502.06251 (d06, abstract only)
- [V] DEBATE (2024): https://arxiv.org/abs/2405.09935 (d07, abstract only)
- [V] Hong et al. (2025) SYCON Bench: https://arxiv.org/abs/2505.23840 (d04)
- [V] Li, Krishnan, Padman (2026): https://arxiv.org/abs/2602.13093 (d01, d02, d16)
- [V] SuperSycophantic (NeurIPS 2026 poster): https://neurips.cc/virtual/2026/poster/148794 (d03; page only)
- [V] Overalignment in frontier LLMs, healthcare (2026): https://arxiv.org/abs/2601.18334 (d12; no numbers on page)
- [V] Dash et al. (2025): https://arxiv.org/abs/2506.20020 (a20, a21, b24)
- [V] Germani and Spitale (2025): https://arxiv.org/abs/2505.13488 (a22, a23, b25)
- [V] Chuang et al. (2023/2024): https://arxiv.org/abs/2311.09618 (a24, a25, b23, c07)
- [V] Ashery, Aiello, Baronchelli (2025): https://arxiv.org/abs/2410.08948 (b28)
- [V] Salvi et al. (2024): https://arxiv.org/abs/2403.14380 (b29)
- [V] Zhang et al. (2024) Collaboration mechanisms: https://arxiv.org/abs/2310.02124 (c08)
- [V] Du et al. (2023): https://arxiv.org/abs/2305.14325 (c09)
- [V] Wunderlich et al. (2026): https://arxiv.org/abs/2605.01566 (d08)
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate: https://arxiv.org/abs/2502.08788 (d09, abstract level)
- [V] The Cost of Consensus (2026): https://arxiv.org/abs/2605.00914 (d10)
- [V] Park et al. (2023) Generative Agents: https://arxiv.org/abs/2304.03442 (c10)
- [V] Santurkar et al. (2023): https://arxiv.org/abs/2303.17548 (c11)
- [V] Argyle et al. (2023): https://arxiv.org/abs/2209.06899 (c12)
- [V] Gupta et al. (2024): https://arxiv.org/abs/2311.04892 (c13)
- [V] Zheng et al. (2024): https://arxiv.org/abs/2311.10054 (c14)
- [V] Hu and Collier (2024): https://arxiv.org/abs/2402.10811 (c15)
- [V] Algaba et al. (2024): https://arxiv.org/abs/2405.15739 (b26, c18)
- [V] Russo Latona et al. (2024): https://arxiv.org/abs/2405.02150 (b27, c19)
- [V] Lu et al. (2024) The AI Scientist: https://arxiv.org/abs/2408.06292 (c20)
- [M] Search-status notes (c24, d14, d15): 2025 citation-fabrication papers seen only as titles; APIs returned HTTP 429.
