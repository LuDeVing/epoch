# Naturalistic decision making: deep document

*Subfield A10.10. Written from evidence_a-d.jsonl, claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids (a01, b09, d04 ...) point to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Naturalistic decision making (NDM) studies how skilled people decide in the field. The settings are messy: time pressure, high stakes, vague goals, changing conditions, teams. The founding claim is that experts rarely compare options. They recognise the situation as a typical one, and the typical situation brings a typical action. They then check that action, usually by imagining it play out, and act.

The core model is Recognition-Primed Decision making (RPD), from Klein and colleagues. What it gives our agent:

- A quick path exists: recognise, then act. This is our S0 "direct" mode.
- The quick path is checked by a short mental simulation. It is not blind.
- When recognition fails or the simulation finds a flaw, the person drops to slower work: diagnose, or adjust the plan.
- Quick recognition is only trustworthy in regular environments with feedback (Kahneman and Klein 2009).

Why it matters for us: the schema's S0 gate must decide when a fast answer is enough and when to escalate. NDM gives the human account of that decision. It also gives the best-known warnings: speed costs accuracy even in elite experts, and the first recognised option can block a better one.

Honesty note. Almost all NDM evidence is human, descriptive, and coded by the model's own authors. Only one study (Kopka and Feufel 2026) tests an NDM-style prompt on a language model. The LLM evidence that is useful for S0 comes from dual-process agents and overthinking research, not from NDM itself.

## 2. History and theories in depth

**Origins.** A 1989 workshop in Dayton, Ohio (about 30 researchers) launched the NDM community. The book *Decision making in action* followed in 1993 (a15, b26). By 2016 there had been 12 NDM conferences (b02). The field was a reaction against lab decision research, which used students, gambles and abstract tasks.

**The fireground study (Klein, Calderwood and Clinton-Cirocco 1985/86/88, reissued 2010).** 26 experienced fireground commanders, mean 23 years of experience. 156 decision points probed by interview. Fewer than 12% showed simultaneous comparison of two or more options. Over 80% were direct identification of a typical situation and action (d01, d02). Second-hand sources give "80-90%" (a15, b02); that range is not in the primary abstract. "Comparison" means side-by-side relative evaluation. Testing one option at a time does not count. Up to about 8% is unaccounted for. The full report (DTIC ADA199492) and the 2010 postscript returned HTTP 403, so K01 stays single-source. Coding was done by the original authors; we found no independent rater study.

**RPD variants** (a20, c03):

- V1 simple match: situation known, response known (if-then).
- V2 diagnose: response known, situation needs diagnosis (gather more cues).
- V3 evaluate by simulation: situation known, response unknown; imagine each candidate in turn until one fits. Options are tested one at a time, not compared.

Recognition supplies four things: relevant cues, expectancies, plausible goals, typical action. Violated expectancies trigger re-diagnosis. The claim that simulation rarely uses more than about three variables and six transitions is secondary-source (c27) and was never tested directly.

**Macrocognition (Klein and Wright 2016).** The field moved from one model to a toolbox: macrocognitive functions (sensemaking, planning, replanning, detecting problems, coordinating) and methods such as cognitive task analysis (a15, a16, b02). Klein states that RPD needs 10-20 years of experience to build the pattern base, so student labs cannot show it (b22).

**Critics.**

- Lipshitz, Klein, Orasanu and Salas (2001), 16 commentaries: wanted controlled tests and clearer definitions (b04, K19).
- Kahneman and Klein (2009) "Conditions for intuitive expertise: a failure to disagree": the two schools agree on one rule. Intuition is trustworthy only when (1) the environment is regular enough to be predictable and (2) the person had prolonged practice with honest feedback. Confidence is not a valid signal of accuracy (b05, a26). Only the abstract-level conditions are verified; full text unopened.
- Grove et al. (2000): across clinical-judgment studies, mechanical prediction was about 10% more accurate on average. It was substantially better in 33-47% of studies and clinicians substantially better in only 6-16% (d04). The "136 studies" count is unverified.

**Rival account: take-the-first vs long-term working memory.** Johnson and Raab (2003) "Take the first" and Raab and Johnson (2007) report that in handball and basketball the first option generated is better than later ones. A competing model (long-term working memory, LTWM) predicts the opposite sign: more options, better decisions (b06-b08, a27). Both camps cite data. Primary papers are closed access; effect sizes are unread (K02, [C]).

**Expert limits.** Einstellung work (Bilalic, McLeod and Gobet 2008) shows a familiar solution blocks a better one even in experts. Speed studies show experts blunder more when forced to rely on fast moves (Vidulich and Tsang 2026). These are NDM's strongest counterweights. See also the sibling documents in subfields/01_einstellung_effect and 03_chunking_and_templates; they are not repeated here.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Fireground commanders rarely compare options | 26 commanders, mean 23 yrs; 156 decision points; under 12% simultaneous comparison; over 80% direct identification | Klein et al. 1985/86/2010 (d01, d02, a22; report unread) | [S] K01 |
| RPD "accounts for 80-90%" of firefighter decisions | figure as quoted by the model's authors | Klein and Wright 2016 (a15, b02) | [S] secondary |
| Goalkeeper RPD path mix | 26 shot sequences, 83 accounts, 419 units; simple match 46% (38), simulation 34% (28), diagnosis 20% (17) | Le Menn et al. 2019 (a10) | [E] K10, one athlete |
| Sport review path mix | simple match 60-81%, diagnosis 13-28%, course-of-action evaluation 3-24% | Macquet 2020 via Frontiers 2022 review (a12) | [E] K10, secondary |
| Elite handball players choose differently from amateurs | 44 players (22 elite). Left breakthrough: forward/tackling chi2(14)=25.06, p=.033, OR 2.76 (1.54-4.95) | Hinz et al. 2022 (a14) | [S] |
| Speed costs accuracy in grandmasters | 20 GMs within-subject: blunder proportion 0.20 to 0.27, d=1.39; blunder size 0.98 to 1.45 pawns, d=0.96; expected blunder per move 0.20 to 0.38, d=1.30; worse for 18 of 20 | Vidulich and Tsang 2026 Study 1 (a04) | [E] K07 |
| Kasparov in simultaneous play | Elo 2750 to 2646 | cited in Vidulich and Tsang (a06) | [E] K07 |
| Familiar solution blocks better one in experts | Candidate Masters 0% found shorter mate with familiar line present, 100% without | Bilalic et al. 2008 (b09, b23) | [E] K08 |
| Einstellung holds with other problems and a "best solution" instruction | stated, no figures | Bilalic et al. 2008 (b24) | [E] |
| Experts detect cues sooner but do not look longer | first fixation 407 vs 719 ms; dwells 27 vs 18; total dwell no difference; 17 experts, 17 novices, 3 min per problem | Sheridan and Reingold 2013 (b10, b11) | [S] K09 |
| Crossword experts retrieve fast with high recovery | experts 77.2 of 78 correct in 5.3 min; novices none finished in 25 min (23.1 correct); with 3 or fewer letters missing experts guess above 80%, novices 40-50% | Thanasuan and Mueller 2014 (a17-a19) | [S] |
| Intuition needs regularity and feedback | two conditions; confidence not a validity signal | Kahneman and Klein 2009 (b05; abstract only) | [E] K06 |
| Mechanical prediction beats clinical | about 10% more accurate; 33-47% vs 6-16% of studies | Grove et al. 2000 (d04) | [E] K22 (count unverified) |
| First options less unique than later ones in a knowledge-free task | 44 healthy, 53 MDD; medians 122.7 vs 374.5 (healthy), 155.7 vs 542.0 (MDD), p<0.001 | Chen et al. 2025 (d06) | [C] K02 |
| NDM prompt raises LLM triage accuracy | 45 vignettes x 10 models x 3 prompts x 10 runs. Default 63.3%, recognition-primed 67.6%, data-frame 66.7%; OR 2.26 and 2.05 | Kopka and Feufel 2026 (a01) | [S] K03 |
| Gain sits in the hardest low-urgency class | self-care 13.4% to 29.8% (RP), 24.6% (DF); GPT-4.1 0% to 43.8% / 39.2% | Kopka and Feufel (a02) | [S] K04 |
| Gain larger with reasoning models, absent in newest family | RP interaction OR 2.15; GPT-5.2 Instant 57.8/56.4/55.3; GPT-5.2 Thinking 52.0/53.1/51.8 | Kopka and Feufel (a03) | [S] K05 |
| Dual-process agent beats single-system agents | ScienceWorld 84.7 vs ReAct 36.4, Reflexion 45.3, SayCan 33.8, fast-only 49.22; tokens per action 757 vs 2,983 (Reflexion) | Lin et al. 2023 SwiftSage (c04-c07) | [E] K12 |
| Checker beats episodic memory in a dual-process agent | success 23.99% to 41.33% (checker) vs 26.94% (memory) | Meneses dos Santos and Oliveira 2026 (c08, c09) | [S] K13 |
| Reasoning models overthink easy items | first round correct in over 92% (QwQ-32B, R1; ASDIV, MATH500 only); 1,953% more tokens; 48.6% token cut possible | Chen et al. 2025 (b17) | [E] K14 |
| Early exit works | DEER 0.95 threshold: chains cut 19.1-80.1%, accuracy +0.3 to +5.0 (11 models, 10 benchmarks); probe saves 24% | Yang 2025, Zhang 2025 (d09, d11) | [E] K23 |
| Past a budget, more thinking hurts | easy problems peak about 1.5K tokens, hardest about 8K (R1-32B); marginal utility negative beyond about 12K; past about 7K flips net harmful | Zhou et al. 2026 (d12) | [S] K14 |
| Reasoning models form a quick guess first and overthink when later reasoning conflicts | removing the question after step 1 cut length 31.1-53.5% | Dang et al. 2026 (d13) | [S] K28 |
| LLM intuition is trainable by examples | 2% to 92% after 2 examples (one task); 12% to 92% after 7; 0% to about 78% after 30 | Hagendorff et al. 2023 (b16) | [E] K15 |
| Stated confidence moves behaviour but tracks competence poorly | median swing 20.6 points (9 open models), 53-70 on larger served models; well-targeted flips beat chance by only +2 | Saxena and Upadhyay 2026 (d16) | [C] K26 |
| Red herrings fixate LLMs | GPT-4 0-shot 6 walls solved vs about 59 with herrings removed (OnlyConnect, 2023 models) | Naeini et al. 2023 (d18) | [S] K25 |
| Pure pattern recognition can reach expert level with enough data | 270M transformer, Lichess blitz Elo 2895, no search | Ruoss et al. 2024 (c16) | [S] K16 |
| Dynamic tasks hurt LLMs | over 50% drop dynamic vs static; hierarchical prompts up to +4.6% | Zhu et al. 2025 FD-Bench (b18) | [S] K17 |
| Escalation trigger length matters | ReflexGrad GPT-5 ALFWorld: m=3 84.3%, m=5 88.1%, m=7 86.6% | Kadu and Krishnan 2025 (d14) | [S] K24 |

## 4. Mechanisms and models

Each model is written so it can be coded.

**4.1 RPD as a control loop.**

```
situation = observe()
match = recognise(situation)          # returns goals, cues, expectancies, action
if match is None: return diagnose(situation)      # V2: get more cues, retry
action = match.action
sim = simulate(action, situation)     # V3-style check, one option at a time
if sim.finds_flaw: action = modify(action) or next_candidate(match)
elif expectancies_violated(match):    return diagnose(situation)
return act(action)
```

Key properties: options are tested serially, not ranked side by side. The check is a simulation, not a vote. Violated expectancies, not a timer, trigger re-diagnosis.

**4.2 Dual-process escalation (SwiftSage, the best-tested analogue).** A fast module acts by default. A slow module is called when a trigger fires. SwiftSage triggers (c05, d15):

1. K=5 consecutive steps with zero reward.
2. The fast module's action is invalid.
3. The action is a critical decision (such as submitting a final answer).
4. An unexpected observation or exception appears.

It returns to fast mode when the action buffer empties. There is no per-trigger ablation, so we do not know which trigger carries the gain. ReflexGrad uses a stall rule (m low-progress scores); a false slow activation costs 5 calls and a 5-step cooldown (d14).

**4.3 Early exit for the quick path.**

- Threshold exit (DEER): at reasoning boundaries, ask for a trial answer and its confidence. Stop at 0.95 or higher (d09).
- Answer-repeat exit: stop when the answer is unchanged across checkpoints (d10). Works on easy tasks; unstable on MATH-500 and GPQA.
- Probe exit: a hidden-state probe predicts correctness (ROC-AUC above 0.7; saves 24%) but needs weights (d11).
- Difficulty-aware budget: easy about 1.5K tokens, hard about 8K (d12).

**4.4 Einstellung as competing activations.** A familiar pattern wins the first match. Search continues around it, so the better option is never fixated. Eye data show experts keep looking at the familiar region while reporting they searched (b10, b23). Implication: a re-look must be forced and must point away from the first answer. Saying "look again" is not enough in humans.

**4.5 Conditions-of-validity model (Kahneman and Klein).** Trust in the quick path = f(regularity of the task class, amount of feedback-backed practice). In code: S0 keeps a per-class record of quick-path pass rate against ground truth. Trust is read from that record, not from stated confidence (d16, d17).

**4.6 Data-frame vs recognition-primed prompting (Kopka and Feufel).** Plain prompt: "Please give a triage classification for the following vignette." The RP prompt names the recognition-primed model and asks the model to match typical cases, then simulate (d08). The DF prompt asks it to build a frame from the data, then test it. Effects are small, probably partly extra reasoning, and absent on GPT-5.2.

**4.7 Mechanical-versus-clinical rule.** Where a scored formula exists, code computes it and the model receives the number, rather than judging alone (Grove). Compare: model alone, model plus formula, formula alone.

## 5. What holds up

**Holds up (several sources).**

- Intuition is trustworthy only in regular, feedback-rich environments; confidence is a poor guide (K06, [E]).
- Speed costs accuracy in elite experts: GM blunder d=1.39, plus earlier Kasparov and Chabris and Hearst results (K07, [E]).
- Einstellung in experts, independently extended by Sheridan and Reingold (K08, [E]).
- Experts use a mix of RPD paths, with simple match dominant in sport (K10, [E]).
- Fast default plus triggered slow module wins on agents: SwiftSage, DPT-Agent, Dualformer (K12, [E]).
- Reasoning models overthink easy items; early exit works on open reasoning models (K14, K23, [E]).
- LLM wargame agents ignore persona text and escalate (K21, [E]).

**Weak or untested.**

- The headline RPD number rests on one original report we could not read, coded by the model's authors. Replications are listed by Klein and Wright (Schmitt and Klein 1999, Keren 2013, Skriver 1998) but not described and not independent (b02, critique).
- Take-the-first is contested: LTWM predicts the opposite sign, a 2025 non-sport task found later options more unique, and time pressure restores take-the-first behaviour (Belling 2015, secondary) (K02, [C]).
- Klein's "10-20 years" boundary has not been tested for agents (K19, [C]).
- NDM training tools (ShadowBox Marines n=59, +28% expert alignment; CTA training g=0.871) are second-hand with self-defined measures (K20).
- Code review and ICU resident studies show an RPD-like fit, not a benefit, and no rival model was tested (K11).

**Failures and caveats.**

- Kopka and Feufel: the published gain (63.3 to 67.6) is smaller than the preprint (64.7 to 70.2, six models). Two emergency cases only. No chain-of-thought arm, no token matching, no gain on GPT-5.2 (a03, a28, b13).
- Stated confidence: a 2026 judge study finds verbalized confidence useful on newest proprietary models, so the negative finding may be model-dependent (K26, [C]).
- ReflexGrad is one benchmark, author-built.
- Samples are small: one goalkeeper, 44 players, 20 grandmasters. Chess is not field work.

**Moderators.** Environment regularity and feedback; time pressure (raises error, may restore take-the-first); task difficulty (early exit safe on easy items, harmful on hard); model type (reasoning vs non-reasoning for NDM prompts; open reasoning models for early exit); presence of a familiar-but-worse option.

**Interventions that worked.** Dual-process triggers; execution-time validation; confidence-threshold early exit; few-shot examples for fast patterns; goal-oriented planning training for fire commanders, which changed behaviour without slowing response (Cohen-Hatton and Honey 2015, cited in a07). **Did not work or unproven.** Persona text; stated-confidence gating (mostly); "be analytic" prompting (schema 4b); forced re-look (never tested on LLMs).

## 6. Language models

**Direct NDM test (one study).** Kopka and Feufel 2026: recognition-primed prompt +4.3 points overall, data-frame +3.4, across 10 ChatGPT models. Gains concentrate in the self-care class (13.4% to 29.8%), which suggests the frame removes a default over-triage bias. Reasoning models gained more (OR 2.15 interaction). GPT-5.2 showed no gain (a01-a03).

**LLM intuition and deliberation.** Hagendorff et al. (2023): CRT-type tasks, GPT-4 96% correct, ChatGPT-3.5 59%, davinci-003 5%, humans 38%. Intuitive errors: davinci 80%, humans 55%, ChatGPT-3.5 15%, GPT-4 0% (c18). Chain of thought raised davinci from 5% to 28% correct. Blocking chain of thought in GPT-4 cost little: 95% to 88% correct, intuitive errors 0% to 10% (c19). Examples build fast patterns quickly (b16). Binz and Schulz found GPT-3 answered all 3 CRT items intuitively and wrongly (b19). For strong models the quick path is already good, so a "slow" mode adds less than for weak ones.

**Overthinking.** Over 92% first-round correct on easy math (Chen). Up to 1,953% more tokens on trivial items. Early exit cut chains 19.1-80.1% with accuracy +0.3 to +5.0 (DEER). All on open reasoning models; frontier API models untested.

**Agents.** SwiftSage 84.7 vs 36.4 (ReAct) at about a quarter of Reflexion's tokens (c04-c06). DPT-Agent beat ReAct and Reflexion in real-time games (c24). Dualformer: maze fast mode 80% vs 30% for solution-only; auto mode 96.6% optimal with 59.9% fewer steps (c25). An execution checker raised success 23.99% to 41.33% (c08).

**Failure patterns.** Red-herring fixation (GPT-4: 6 vs about 59 walls). Dynamic-environment drop over 50% (FD-Bench). Wargame escalation with no persona effect (Rivera 2024; Lamparth 2024, N=214 experts). Working-memory-like limits: recall falls log-linearly with interference (d20); N-back accuracy falls with load across 15 models (d21). No direct measure of a 3-variable, 6-transition cap.

**Pattern recognition at scale.** A 270M transformer reached blitz Elo 2895 with no search; ablations show dependence on data and scale (c16, c17).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Per-class record of quick-path accuracy against ground truth; trust the quick path only where the class is regular and feedback has been seen. Do not read trust from stated confidence. | S0, S9, memory | [E] | K06; b05, d16, d17 |
| Cap thinking by mode and difficulty; allow early stop on easy items by answer-repeat or threshold; longer budget on hard ones. | S0, G11, G12 | [E] | K14, K23; b17, d09-d12 |
| Escalation triggers from fast to slow path: repeated no-progress, invalid output, a critical decision (final answer), unexpected observation. Log which trigger fired. | S0 to S4/S6 | [E] pattern, [S] each trigger | K12, K24; c04-c07, d14, d15 |
| Worked examples on the quick path build fast patterns cheaply. | S0, memory | [E] | K15; b16 |
| Where a scored formula exists, code computes it and the model receives the result. | G5, S4 | [E] abstract level | K22; d04 |
| No persona text to change fast-path behaviour. | G | [E] | K21; c12, c14, c15 |
| Treat speed as an accuracy cost: route hard cases to more compute, not a flat budget. | S0, G12 | [E] | K07; a04-a06 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Recognition-primed prompt (match typical cases, simulate one option) vs plain vs plain chain of thought at equal tokens. | S0, S1 | [S] | K03-K05; a01-a03 |
| Log first answer vs final answer; use agreement rate per class as the S0 gate. | S0, S9 | [S] | K01, K28; d13 |
| Forced re-look operator when a familiar solution is present (look for an option unlike the first). | G, S6 | [E] human, untested on LLM | K08, K25; b09, d18 |
| Execution-time checker on the quick path. | S4 | [S] | K13; c08 |
| First option vs best-of-k quality (take-the-first). | S3, O1 | [C] | K02; a27, d06 |
| Stall-length sweep (3, 5, 7) for the impasse trigger. | S6 | [S] | K24; d14 |
| Simulate branch: find the break point in variables and transitions. | S3/S4 | [S] | K27; d20-d22 |
| Pre-mortem step vs extra sampling (hand off to the pre-mortem subfield). | O | [S] analogy | K18; c20-c22 |
| Mid-run re-check of state when the task changes. | G | [S] | K17; b18 |

Do not add (already in SCHEMA 4b or unsupported): verbal-confidence stopping, "be analytic" prompting, debiasing checklists, NDM training tools as agent evidence.

## 8. Concrete tests on our bench

All arms at equal total tokens (G7). Report per-class accuracy and tokens.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Ill-defined classification with a default bias (triage-style) | plain; plain + CoT; RP frame; DF frame | accuracy per class, confusion matrix | RP beats plain by 2-5 points; gain over CoT near zero on strong models |
| T2 | Mixed easy/hard items from our banks | fixed budget; answer-repeat stop; 0.95 threshold stop; difficulty-routed budget | accuracy at tokens spent | 20-50% fewer tokens at equal accuracy on easy items |
| T3 | Same tasks | direct vs CoT | accuracy by class | little loss on regular classes, large loss on novel ones; defines the S0 gate |
| T4 | Tasks with a planted familiar-but-worse solution | plain; forced re-look (option unlike the first); extra sample | rate of finding the better solution | forced re-look beats extra sampling |
| T5 | Multi-step agent task | always-slow; fast only; fast with triggers (stalled, invalid, critical, surprise) | success, tokens per action | triggers beat both; one trigger carries most of the gain |
| T6 | Stall-length sweep | m = 3, 5, 7 | success, false activations | peak near 5 |
| T7 | Options generated in order (k=5) | take first; best of k by code check | accuracy of option 1 vs best | shows whether first options are good on our tasks |
| T8 | Tasks with a scored formula | model alone; model + formula; formula alone | accuracy | formula alone at least matches model alone; model + formula best |
| T9 | Simulate tasks, vary variables 2-8 and transitions 2-12 | one model | break point | finds our own cap |
| T10 | Regular vs irregular class split | S0 answer | accuracy and calibration per split | calibration worse on irregular classes; stated confidence weak in both |

## 9. What does not transfer, and why

- **Time pressure.** Fireground decisions take seconds. Our constraint is tokens. Speed-accuracy effects map to token budgets only by analogy.
- **Years of feedback.** Klein's 10-20 years builds the pattern base. Ours comes from pretraining, which we cannot control. Per-class records in memory are the nearest thing and are tiny.
- **Embodied cues and team talk.** RPD rests partly on perception, felt wrongness and team coordination. A text agent has none.
- **Interview coding.** Commander reports are retrospective accounts. G10 says reasoning text is not evidence. Einstellung work shows experts misreport their own search.
- **Sport base rates.** 46% / 34% / 20% is one goalkeeper. Do not borrow it.
- **Stakes.** Real-world loss shapes human caution. A scaffold has none.
- **Wargame and forecasting results.** They link to NDM only by analogy.
- **Training tools.** ShadowBox and similar train humans; they do not map to agent changes.
- **Open-model results.** Early exit and probes were measured on open reasoning models; the probe needs weights.

## 10. Open questions

1. What do the fireground report and its 2010 postscript say about the comparison definition and the unaccounted 8%? Needs full text.
2. Do NDM frames beat plain chain of thought at equal tokens, on tasks other than triage, and on frontier models where GPT-5.2 showed no gain?
3. What are the effect sizes for take-the-first (Johnson and Raab 2003; Raab and Johnson 2007), and has it replicated outside sport?
4. Can an agent detect a regular, feedback-rich zone better than its own confidence does? No test exists.
5. How often is a reasoning model's first-round answer final-correct by difficulty, on frontier API models?
6. Which escalation triggers carry the gain for a text-only agent, and what is the false-alarm cost?
7. How large is the Einstellung penalty for LLM agents, and does a forced re-look fix it?
8. Is there an LLM analogue of the 3-variable, 6-transition cap?
9. Do LLM judges follow Grove's pattern against simple formulas? Only one small 2026 comparison exists (logistic regression 84.1% vs prompted LLMs 60-80%; LLM test set about 30 cases).
10. Is "136 studies" in Grove et al. correct?

## 11. Sources

[V] opened this session; [M] snippet or abstract only.

- [V] Kopka and Feufel (2026) NDM prompts for care-seeking advice. https://pmc.ncbi.nlm.nih.gov/articles/PMC13061108/ (a01-a03, a28, d08)
- [V] Kopka and Feufel press release. https://www.eurekalert.org/news-releases/1127513 (b12)
- [M] Kopka and Feufel preprint and journal page. https://preprints.jmir.org/preprint/88053 ; https://biomedeng.jmir.org/2026/1/e88053 (b13, c10, c11)
- [V] Vidulich and Tsang (2026) Intuition and deliberation in elite expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC13100097/ (a04-a07)
- [V] Norwegian military decision-making assumptions (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13113691/ (a08)
- [V] Resident physician cognitive task analysis (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12712819/ (a09)
- [V] Le Menn et al. (2019) Handball goalkeeper intuition. https://pmc.ncbi.nlm.nih.gov/articles/PMC6942481/ (a10, a11)
- [V] NDM in sport, Frontiers (2022). https://www.frontiersin.org/articles/10.3389/fpsyg.2022.936140/full (a12, a13)
- [V] Hinz et al. (2022) Elite vs amateur handball decisions, Frontiers in Psychology (a14; URL in evidence_a.jsonl)
- [V] Klein and Wright (2016) Macrocognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4731510/ ; https://www.frontiersin.org/articles/10.3389/fpsyg.2016.00054/pdf (a15, a16, b02, b03, b22)
- [V] Thanasuan and Mueller (2014) Crossword expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC4161049/ (a17-a19)
- [V] Wikipedia: Recognition primed decision; Naturalistic decision-making. https://en.wikipedia.org/wiki/Recognition_primed_decision (a20, b26)
- [V] Gary Klein site, RPD page. https://www.gary-klein.com/rpd (a21, b25)
- [V] Instructional-design blog on RPD. https://idtips.substack.com/p/the-recognition-primed-decision-model (a22, a23)
- [M] Klein, Calderwood and Clinton-Cirocco report. https://apps.dtic.mil/sti/pdfs/ADA199492.pdf ; https://doi.org/10.1518/155534310X12844000801041 (a24, a25, b01, d03)
- [V] Klein et al. 2010 and 1986 abstracts. https://doi.org/10.1518/155534310X12844000801203 ; https://doi.org/10.1177/154193128603000616 (d01, d02)
- [M] Kahneman and Klein (2009). https://pubmed.ncbi.nlm.nih.gov/19739881/ ; https://doi.org/10.1037/a0016755 (a26, b05, b28, d05)
- [M] Johnson and Raab (2003) Take the first. https://ideas.repec.org/a/eee/jobhdp/v91y2003i2p215-229.html ; https://doi.org/10.1016/s0749-5978(03)00027-x (a27, b06, b21, d07)
- [M] Lipshitz et al. (2001), via Klein and Wright (b04)
- [V] Raab and Gigerenzer (2015) The power of simplicity. https://frontiersin.org/articles/10.3389/fpsyg.2015.01672/pdf (b07, b08)
- [V] Bilalic, McLeod and Gobet (2008). https://bura.brunel.ac.uk/bitstream/2438/5777/1/Fulltext.pdf (b09, b23, b24)
- [V] Sheridan and Reingold (2013). https://pmc.ncbi.nlm.nih.gov/articles/PMC3790829/ (b10, b11); [M] summary (b27)
- [V] Hagendorff, Fabi and Kosinski (2023). https://arxiv.org/abs/2212.05206 (b14-b16, c18, c19)
- [V] Chen et al. (2025) Overthinking. https://arxiv.org/abs/2412.21187 (b17)
- [V] Zhu, Zheng and Jin (2025) FD-Bench. https://journalpub.escholarship.org/cognitivesciencesociety/article/49274/g (b18)
- [V] Binz and Schulz (2023). https://arxiv.org/abs/2206.14576 (b19)
- [V] Grove et al. (2000) abstract. https://pubmed.ncbi.nlm.nih.gov/10752360/ (d04); [M] https://doi.org/10.1037/1040-3590.12.1.19 (b20)
- [M] Blog summary of Sources of Power. https://www.jasoncollins.blog/posts/gary-kleins-sources-of-power-how-people (c27); [M] skill page (c28)
- [V] Heander et al. (2025) Code review as decision-making. https://arxiv.org/abs/2507.09637 (c01-c03)
- [V] Lin et al. (2023) SwiftSage. https://arxiv.org/abs/2305.17390 (c04-c07, d15)
- [V] Meneses dos Santos and Oliveira (2026). https://arxiv.org/abs/2609.19128 (c08, c09)
- [V] Rivera et al. (2024). https://arxiv.org/abs/2401.03408 (c12, c13)
- [V] Lamparth et al. (2024). https://arxiv.org/abs/2403.03407 (c14, c15)
- [V] Ruoss et al. (2024). https://arxiv.org/abs/2402.04494 (c16, c17)
- [V] Kim et al. (2026) InvThink. https://arxiv.org/abs/2510.01569 (c20, c21)
- [V] Liptay et al. (2026) forecasting agents. https://arxiv.org/abs/2604.26106 (c22, c23)
- [V] Zhang et al. (2025) DPT-Agent. https://arxiv.org/abs/2502.11882 (c24)
- [V] Dualformer. https://arxiv.org/abs/2410.09918 (c25)
- [V] Mainali et al. (2025). https://arxiv.org/abs/2510.06093 (c26)
- [V] Chen et al. (2025) path generation task. https://pmc.ncbi.nlm.nih.gov/articles/PMC13400725/ (d06)
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895 (d09)
- [V] Liu and Wang (2025). https://arxiv.org/abs/2506.02536 (d10)
- [V] Zhang et al. (2025). https://arxiv.org/abs/2504.05419 (d11)
- [V] Zhou et al. (2026). https://arxiv.org/abs/2604.10739 (d12)
- [V] Dang et al. (2026). https://arxiv.org/abs/2505.16448 (d13)
- [V] Kadu and Krishnan (2025) ReflexGrad. https://arxiv.org/abs/2511.14584 (d14)
- [V] Saxena and Upadhyay (2026) Nudgeability. https://arxiv.org/abs/2609.34572 (d16)
- [V] Hsiao (2026). https://arxiv.org/abs/2609.10996 (d17)
- [V] Naeini et al. (2023). https://arxiv.org/abs/2306.11167 (d18)
- [V] Haq et al. (2025). https://arxiv.org/abs/2501.11833 (d19)
- [V] Wang and Sun (2025). https://arxiv.org/abs/2506.08184 (d20)
- [V] Gong (2026). https://arxiv.org/abs/2610.21176 (d21)
- [V] Kim and Schuster (2023). https://arxiv.org/abs/2305.02363 (d22)
- [V] Maliha and Kabir (2026). https://arxiv.org/abs/2606.00031 (d23)

*Corrections carried forward from critique.md: Kopka and Feufel published version used 10 models (six was the preprint). Hagendorff CRT GPT-4 is 96% in Study 1; 95% is the Study 2 baseline (b14, b15 say 95%). Chen "over 92%" applies to QwQ-32B and R1 on ASDIV and MATH500 only. GPT-4.1 mini DF gain is +12.6 (a03 rounds to 13).*
