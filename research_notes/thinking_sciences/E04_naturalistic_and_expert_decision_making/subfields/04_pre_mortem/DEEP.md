# Pre-mortem: deep document

*Subfield E04.04. Sources: evidence_a-d.jsonl (ids a01-a31, b01-b25, c01-c25, d01-d17), claims.jsonl (K01-K24), critique.md. All numbers below were read in a source unless marked "secondhand". Bottom line first: the human evidence for the premortem is thin, and no study of a literal premortem prompt on an LLM, with an accuracy control, exists.*

## 1. What it is

The premortem is a planning technique. The team is told: "Imagine the plan has already failed. Write down why." Gary Klein formalised it (Klein 1998 book; Klein 2007 HBR). The steps are: brief the plan, state the failure as fact, each person lists causes alone (about two minutes), then the group collects the causes and fixes the plan (a03, a04, a05).

Three parts are bundled in the method:
1. **Failure frame.** The failure is stated as certain and past ("it failed"), not possible ("it might fail").
2. **Listing causes.** The person must produce reasons, which counters confirmation of the current plan.
3. **Social safety.** In teams, people who see weaknesses may speak without seeming disloyal. This does not apply to a single agent.

Related ideas that are not the same thing:
- **Post-mortem**: explain a failure after it happened. Used in agents as stored lessons (Reflexion).
- **Devil's advocate**: argue against the plan from a "could fail" stance.
- **Worst-case scenario method**: Peabody's rival prompt.
- **Consider the opposite / list reasons against**: Koriat 1980.
- **Unpacking**: split a hypothesis into parts (Hill 2012).

For our agent the question is narrow. The schema has guardrail G1: doubt only on a signal. A premortem is a doubt step. So the question is whether a premortem, fired by a signal, adds accuracy or calibration beyond a plain "list reasons my answer is wrong" step or a tool check, at equal tokens. Nobody has measured that.

## 2. History and theories in depth

**Roots (1980-1985).**
- Koriat, Lichtenstein and Fischhoff 1980 ("Reasons for confidence"): listing reasons against your chosen answer reduced overconfidence; listing supporting reasons did not (a09, b13; numbers not read, opened:false).
- Hoch 1985: imagining reasons for alternative outcomes and its effect on prediction accuracy (a10; not read).

**Founding study.** Mitchell, Russo and Pennington 1989, "Back to the future" (a01, b01). Two experiments varied temporal perspective (event in the future or past) and certainty (sure or uncertain). Abstract: in experiment 1, temporal perspective had little influence. Certainty had a strong influence. Sure events got longer explanations, more episodic reasons and more past tense. In experiment 2, uncertainty changed the type of explanation, not the time spent. Only the Crossref abstract was readable (Wiley paywall).

**The popular claim.** Klein and many later writers say "imagining the event has happened raises the number of reasons by about 30 percent" (a02, b02, b03, a16). No source we read gives N, design or test. The abstract does not contain it. The abstract points to certainty, not the time shift, as the active ingredient. This is contested (K01).

**Klein's method (1998-2007).** Klein developed the premortem in the 1990s and described it in Sources of Power (1998), The Power of Intuition and the 2007 HBR piece (a03, a16). Klein 2007 cites only Mitchell 1989 as research (a31). Klein 2021's blog cites only Veinott 2010 as empirical support (b05).

**Competing accounts of why it might work.**
1. *Certainty frame* (Mitchell abstract; Posavac 2008 snippet says temporal-frame effects shrink when certainty is primed, a15).
2. *Listing reasons against* (Koriat 1980). Any "why am I wrong" prompt may do the same.
3. *Failure frame beats devil's advocate.* Argument in the 2025 implementation review (a17): "already failed" differs from "could fail". Nemeth, Brown and Rogers 2001 (a14) found role-played devil's advocacy tends to bolster the starting view; authentic dissent did better. No numbers connect this to the premortem.
4. *Different attention.* Peabody found premortem and worst-case prompts spread reasons across different categories (b07).
5. *Social safety.* Klein's stated aim (a03). Not applicable to one agent.

**Human tests (2010-2017).** Veinott, Klein and Wiggins 2010; Gallop and Bischoff 2016; Peabody 2017 thesis; Elizabeth 2020 poster. Section 3 lists them. About five controlled studies in total, none preregistered, none with real plan outcomes (K05, b22).

**Field use is mostly qualitative.** Implementation science papers run premortems and report themes with no comparison: 10 researchers, 6 themes (a18); 23 barbershop participants (b11); 14 professionals, 5 themes (b12). Roose, Lehman and Veinott 2023 (game teams) and Luth et al. 2017 were cited but not read (b18, b19). PreHaz (Aceituna 2019) proposes narrowing the search space; worked examples only (b10). The uniqueness-bias paper (219 projects) lists premortem as a remedy without testing it (a19, c21).

**LLM era (2023-2026).** The word "premortem" is now used by several LLM papers, but they are different methods (section 6). Closest in spirit: anticipatory reflection (Wang 2024), PreFlect (2026), CoMem (2026), InvThink (2025). None is a plain prompted premortem tested against a matched control (K22).

## 3. Core findings with exact numbers

Status key: E established, S single-source, C contested, H human-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Founding study: certainty, not time shift, drove explanation features | Two experiments; abstract only, no N or means | Mitchell et al. 1989 (a01, b01) | C |
| "About 30 percent more reasons" for imagined-as-happened events | About 30%; no N, no stats; secondhand | Mitchell via Klein, Collins (a02, b02, b03) | C |
| Premortem lowered plan confidence more than critique, pros/cons, cons-only | N=178 students, 5 conditions, H1N1 lockdown plan. Means, SDs not seen. Secondhand: about twice the drop of pros/cons or cons-only | Veinott et al. 2010 (a06, b04, d13) | S, H |
| Premortem teams found more quality risks than brainstorming | N=101 managers and engineers, teams of 4-6, 45 min torpedo scenario. No effect size seen | Gallop and Bischoff 2016 (a07, b08) | S, H |
| Behavioural result: fewer fouls, less fixation on first plan | Exp 1: N=52 cadets in teams, 6 timed exercises; no change in planning or execution time; no p-values seen | Peabody 2017 (a08, b23) | S, H |
| Complexity moderator | Exp 2 (N=72, simple plan) no count difference vs Worst-Case; Exp 3 (N=82, complex unfamiliar plan) premortem more reasons; category distributions differed in both | Peabody 2017 (b06, b07, b25) | S, H |
| Group vs individual | Poster: group hypothesis not supported; no numbers | Elizabeth 2020 (b09) | S, H |
| Listing reasons against reduces overconfidence | Numbers not read | Koriat et al. 1980 (a09, b13) | E (classic), numbers unseen |
| Unpacking can inflate probability | N=32; 25 of 32 (78%) subadditive; focal group parts summed 1.07 (SD .33) vs whole .82 (SD .14), t(15)=3.14, p=.007; residual group .72 vs .19, t(15)=3.72, p=.002; change score F(1,28)=4.753, p=.038, partial eta2=.145 | Hill 2012 (a11, a12) | S, H |
| Consider-the-opposite debiasing weak | Technical self-assessment accuracy +1.00% (CI -7.46 to 10.0); communication +5.63% (CI 0.001 to 16.9) | Matern et al. 2025 (b14) | E (weak prior) |
| Debiasing overall mixed | Finance professionals: worked on better-than-average beliefs, weakly on miscalibration; N=90 Indonesian study: a video worked best | Kaustia and Perttula 2012; Rusmana 2020 (b15, b16) | E (weak) |
| Failure-first prompt cut LLM harmfulness | TRIDENT harmfulness 3.22 zero-shot, 2.62 SafetyPrompt, 2.19 InvThink prompt (32.0% lower than zero-shot); 2,652 prompts, 5 seeds | InvThink (c01, a22) | C |
| Matched forward-direction control gave same safety | Qwen-2.5-7B SFT, 23,063 targets: safety 1.000 both; harmfulness 1.23 (failure) vs 1.01 (forward); attack success 0.000 both; XSTest 0.980 both | InvThink B.2 (a23, c04, d10) | C |
| InvThink gain depends on task | SafetyBench: Illegal +15.8 (N=1,767), Physical health +12.5 (1,140), Ethics +10.0 (1,926), Mental health +7.9 (1,561), Offensiveness +2.4 (1,801) | c03 | S |
| Agentic safety | Prompt-only: blackmail rate -90%, murder attempts -44%; SFT+RL: 0 of 100 trials per seed, 5 seeds | c02 | S |
| Over-refusal cost | False-refusal rate 0.361 default, 0.320 with calibration term; correct refusal 0.927 to 0.920 | a24, d10 | S |
| No safety tax | Up to +5.0 GPQA and MATH500, +2.0 MMLU (SFT+RL) | c05 | S |
| Anticipatory reflection in agent loop | WebArena after 7 episodes: 23.5% vs LATS 22.7% vs Plan+Act with post-failure reflection 19.8%; plan revisions 0.64 vs 1.16 vs 2.03; 3.5 points over best zero-shot | Wang et al. 2024 (c11, c24, d12) | S |
| Pre-action critique with distilled error prior | GAIA, GPT-4.1, pass@1: 46.06 to 58.18 (+12.12); Level 3 19.23 to 38.46; w/o planning-error prior 50.30; w/o re-planning 51.52; 74% of plans flagged risky; Gemini 50.30 to 59.39 | PreFlect (a20, a21, d01) | S |
| Forecaster with high pre/post-mortem share beat frontier agents | Brier 0.119 vs Opus 4.6 0.130 (gap 0.011, CI 0.006-0.017); Gemini 3.1 Pro 0.141, GPT-5.4 0.152; cost $1.68 vs $0.55; Pre/Post-mortem top-3 share 37.8% vs 12.1% and 10.8%; N=1,367 scored | BTF-2 (a25, c07, d11) | C |
| Expert review of 130 worst questions | 24 of 130 had strategic errors; main failures were wrong models of actors, not missing premortems | BTF-2 (a26, c09) | S |
| Intrinsic self-correction hurts | GPT-3.5 GSM8K 75.9/75.1/74.7 (calls 1/3/5); CommonSenseQA 75.8/38.1/41.8; HotpotQA 26.0/25.0/25.0; GPT-4 GSM8K 95.5/91.5/89.0; CSQA 82.0/79.5/80.0; HotpotQA 49.0/49.0/43.0. With oracle labels GPT-3.5 GSM8K 95.5, GPT-4 97.5 | Huang et al. 2024 (c13, d04) | E |
| Debate no better than majority vote | Same number of responses; debate gain is self-consistency | Huang (c23) | E |
| Tool-backed critique beats internal | ChatGPT F1: AmbigNQ 64.3 CoT, 74.9 CRITIC, 67.3 without tool; HotpotQA 42.8, 52.9, 46.1; TriviaQA 79.2, 81.7, 79.9 | CRITIC (d02) | E |
| Survey: no general success from prompted feedback alone | Qualitative | Kamoi et al. 2024 (d03) | E |
| Self-Refine gains on easy-to-spot defects | About +20% absolute average over 7 tasks; code optimisation +8.7 over GPT-4 | Madaan 2023 (d15) | S |
| Stored post-mortem lessons help | Reflexion HumanEval 91 vs 80; AlfWorld +22, HotpotQA +20; reflection +8 over episodic memory alone | Shinn 2023 (c15) | S |
| Lessons stack | ExpeL HotpotQA 40% vs Reflexion 39%; insights-only vs retrieval-only HotpotQA 36 vs 31, ALFWorld 50 vs 55; ExpeL+Reflexion ALFWorld 59.0 to 64.2 | ExpeL (d08) | S |
| Retrieved-case failure hypotheses | Qwen3-8B, 3 seeds: HumanEval+ Base 81.19, Reflexion 84.87, DoT-Bank 88.14, ParamMem 93.66, CoMem 95.09; LiveCodeBench 41.00/50.44/53.89/56.44/59.67; MATH 79.38/86.45/90.17/93.76/94.72 | CoMem (d09) | S |
| Trained "pre-mortem" method | +5.01 (Qwen2.5-7B), +4.28 (Llama-3.1-8B), +5.66 (Qwen3-4B-Base) over GRPO | AUGUR (b17) | S, abstract level only |
| Pool answers beats one pass | PaLM-540B, 40 samples: GSM8K 56.5 to 74.4 (+17.9) | Self-consistency (d05) | E |
| Sample agreement as cheap gate | 17 datasets, 3 LLMs: samples cut up to 7.9x, avg 3.3x, accuracy drop under 0.1% | Adaptive-Consistency (d06) | E |
| LLM devil's advocate in human groups | N=48, 12 groups; psychological safety 5.38 to 5.65, p=0.490; satisfaction up; load up | Lee et al. 2025 (c17) | S |
| Devil's advocate in diagnosis | 16 cases, 80 runs: initial correct 0/80; after discussion top differential 57/80 (71.3%), top two 64/80 (80.0%) | Ke et al. 2024 (c16) | S |
| Reverse thinking (trained) | +13.53% avg over zero-shot across 12 datasets; +6.84% over best distillation baseline; +6.69% forward distillation | RevThink (c14) | S |

## 4. Mechanisms and models

Each is described so an engineer can build it.

**M1. Failure-frame prompt (the literal premortem).**
Input: question, draft answer or plan. Prompt: "This answer has been checked and found WRONG. Write the 3 most likely reasons, each as a testable claim." Output: a list of causes. Then each cause is checked (see M2), and the answer is kept or revised. The design question is the frame wording: certain-failure ("it failed") versus uncertain ("it may fail"). Mitchell's abstract suggests certainty matters. This is a one-line change, so it is cheap to test.

**M2. Check each named cause with an external test.**
Turn each cause into something code, a tool or retrieval can verify (a unit test, a re-computation, a lookup). Revise only if a check fails. This is the CRITIC pattern (d02) and respects G1 (doubt on a signal) and the Huang result (no unverified self-critique). Without this step, the premortem is internal-only self-critique, which on current evidence is zero to negative.

**M3. Signal gate.**
Run M1 only when a cheap signal fires. Candidates:
- three quick samples disagree (Adaptive-Consistency logic, d06),
- low P(True) from the model (d07),
- task flagged complex or unfamiliar (Peabody, b25),
- a tool disagrees with the draft.
Never on a schedule. PreFlect flags 74% of plans as risky (d01), so a check that always fires is effectively ungated.

**M4. Stored error priors (post-mortem memory).**
Keep a short library of failure patterns from past runs. Feed the matching ones into the check ("past runs failed this way on this type"). PreFlect's prior was worth 7.88 of 12.12 points (58.18 vs 50.30). CoMem retrieves cases and writes failure hypotheses. On current evidence stored lessons are a stronger candidate than imagination alone.

**M5. Pooled failure lists.**
Sample 3 independent failure lists. Keep causes that recur. Pooling answers works (+17.9 on GSM8K). Pooling failure lists is untested, and costs 3x the tokens.

**M6. Calibration guard.**
Listing many causes can inflate stated failure probability (Hill: parts sum 1.07 vs whole .82). Guard: after the list, compute confidence from external checks, not from how many causes were listed. Measure Brier of the stated failure probability before and after.

**M7. Over-refusal guard.**
InvThink's trained model over-refuses (FRR 0.361). Track false-alarm rate on benign items when a premortem step runs.

**Competing mechanisms to separate in an experiment:** frame (certain vs possible), content (reasons-against vs neutral list), format (structured list vs free text), tokens (extra reasoning length), and tool grounding. A 2x2 on frame and content, plus an equal-length neutral control, separates them.

## 5. What holds up

**Held up.**
- Ungated, internal-only self-critique lowers accuracy on reasoning (Huang: CommonSenseQA 75.8 to 38.1). Kamoi's survey agrees. Established.
- Tool-grounded critique beats internal critique (CRITIC, +6 to +10 F1 on QA vs 0 to +3 without tools). Established.
- Pooled sampling beats one pass for answers. Established.
- Sample agreement is a usable cheap difficulty signal. Established.

**Did not replicate, or never tried.**
- The 30 percent figure: no replication, not in the abstract (contested).
- No preregistered replication, no meta-analysis, no field trial with real plan outcomes of the human premortem (K05, established as an absence).
- No LLM study prompts a literal premortem on a planning or coding task and compares with a no-premortem control (K22, searched arXiv, Crossref, Europe PMC to Nov 2026).
- The failure direction itself: InvThink's matched forward control gave equal safety (K10, K23).

**Moderators.**
- Plan complexity and familiarity (Peabody; single source).
- Task type: InvThink gains large on consequence reasoning (+15.8), small on pattern-style items (+2.4).
- Certainty vs temporal frame (Mitchell).
- Group vs individual: untested properly.
- Tool access: an external check changes the sign of the effect for critique.

**Interventions that worked (with caveats).**
- Failure-first prompts for safety, 32% lower harmfulness (but the forward control was equal when trained).
- Anticipatory reflection, +0.8 over LATS (small), +3.5 over best zero-shot, bundled with two other steps.
- Error-prior-grounded pre-action critique (+12.12), single run, about 165 GAIA tasks so one task is about 0.6 points.

**Did not work or not shown.**
- Consider-the-opposite on technical self-assessment (+1.00, CI -7.46 to 10.0).
- LLM devil's advocate did not change psychological safety in groups (p=0.490).
- Debate no better than majority vote.
- Group premortem hypothesis not supported (poster).

**Weak points in the evidence.** Veinott, Gallop, Mitchell full text, Koriat and Hoch were never opened. All their numbers are secondary. Veinott's outcome is confidence, and a confidence drop is not an accuracy gain. BTF-2's Pre/Post-mortem association is correlational: the winning forecaster had an imposed rationale structure, cost 3x more, and "Pre/Post-mortem" includes post-mortem content (K14, d11). The authors say causal isolation is hard.

## 6. Language models

**There is no clean test.** Nobody has run "this answer failed, why?" versus "this answer may fail, why?" versus a neutral control at equal tokens on LLM accuracy or calibration (gap 1, open).

**Studies that use the name or the idea.**
1. *InvThink (Kim et al. 2025).* Model lists harms, analyses consequences, answers under constraints. Prompt-only: harmfulness 3.22 to 2.19 (SafetyPrompt 2.62). Agentic insider-threat: blackmail -90%, murder attempt -44%. Training versions: zero harmful actions in 5 x 100 trials (upper 95% bound 0.030). The key control: forward-direction (PROTHINK) matched data gave the same safety after SFT. So structure and tokens may explain the gain, not failure imagining. Costs: over-refusal FRR 0.361. Scale: kept top safety from 0.27B to 72B while CoT safety fell beyond 14B. Safety domain only.
2. *Wang et al. 2024 anticipatory reflection ("Devil's Advocate").* Before each action: what could go wrong, write a backup, backtrack on failure, plus whole-plan review. 23.5% vs LATS 22.7% vs 19.8%. No ablation of the anticipatory step alone (d12). The authors note plain sampling in LATS gave homogeneous actions and the devil's question widened options.
3. *PreFlect 2026.* Pre-action plan critique plus distilled error prior plus re-planning. +12.12 on GAIA. The prior is most of it. Not called a premortem.
4. *BTF-2 forecasting.* Pre/Post-mortem content 37.8% vs about 12% of rationales; Brier 0.119 vs 0.130. Correlational and confounded.
5. *CoMem 2026.* Trained memory module writes failure hypotheses from retrieved cases. HumanEval+ 95.09 vs Reflexion 84.87 (Qwen3-8B). Trained, so not a prompt step.
6. *AUGUR 2026 and Zhang 2026 "Prospective Hindsight".* Training methods that share a name. AUGUR +4.28 to +5.66 over GRPO (abstract level only). Zhang's method reweights rollouts by the prediction-evaluation gap. Neither tests the human technique (K16).
7. *Tutorial (Loweimi 2026).* Recommends a premortem prompt (failure story, early signs, most likely and most dangerous failure). No measurement.
8. *Reverse thinking (RevThink).* Trained backward reasoning, +13.53%. A cousin, not a premortem.

**Behaviour of the surrounding methods.**
- Self-critique without ground truth hurts: GPT-4 GSM8K 95.5 to 89.0 by 5 calls. A premortem on the model's own answer carries this risk.
- With oracle labels the same loop looks strong (GPT-3.5 GSM8K 95.5). That gain is not real.
- Tool grounding flips the sign (CRITIC).
- Stored lessons help and stack: ExpeL plus Reflexion 59.0 to 64.2 on ALFWorld.
- Frontier forecasters differ in calibration (0.002 SOTA vs 0.005 Opus 4.6, 0.010 GPT-5.4, 0.012 Gemini 3.1 Pro) and refinement (0.081, 0.075, 0.056, 0.069), which hints a pre/post-mortem step might help calibration more than search (c25).
- Task-type dependence is large (InvThink +15.8 vs +2.4).

**Unmeasured in LLMs.** Failure-probability inflation after listing (Hill's effect). Over-hedging cost on accuracy tasks. Pooling failure lists. Gating by signal.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Parts: G guardrail, S state, O operator, memory.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Any failure-imagining step must be signal-triggered, never scheduled or always on. This confirms G1; no change to wording needed. | G1 | [E] | c13, d04, c23, K09 |
| Any check on a named failure cause must be tied to an external test, tool or retrieval where one exists. Internal-only critique of own answer must not overwrite a draft. | G1 / O-check | [E] | d02, d03, d04, K19 |
| Do not use role-played debate or devil's-advocate agents as a doubt step. Already G9. | G9 | [E] | c23, K09 |
| Do not count "pre-mortem" or "prospective hindsight" named LLM papers as evidence for a prompt step. | none | [E] | K16, K22 |
| Treat ungated debiasing steps as low prior. | G1 | [E] | b14, b15, K17 |

Nothing about the premortem itself reaches "established" for the schema. The human literature is thin and the LLM literature has no control.

### Test first (not yet established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Failure-frame ("has failed") vs possibility-frame wording | G1 / O-check | [C] | a01, b01, a02, d10, K01 |
| Failure frame vs neutral "reasons against" list (2x2) | G1 | [S] | a09, b13, K06 |
| Premortem gated by 3-sample disagreement or low P(True) vs always-on vs never | G1 / S-signal | [S] | d06, d07, b25, K20 |
| Premortem causes turned into external checks vs internal-only | O-check | [E] direction, [S] for premortem | d02, K19 |
| Stored error-pattern memory vs imagined failures vs both | memory | [S] | a21, d01, d08, d09, K13, K21 |
| Pre-action "what could go wrong" before tool calls | O-check | [S] | c11, c24, K12 |
| Pooled failure lists (3 samples, keep recurring causes) | O-check | [S] | d05, K24 |
| Calibration guard: does listing causes inflate stated failure probability | G-calibration | [S] | a12, d16, K08, K23 |
| Over-refusal and over-hedging cost on benign items | G1 | [S] | a24, d10, K11 |
| Complexity gate | S-signal | [S] | b25, K03 |

## 8. Concrete tests on our bench

All arms at equal total tokens (pad control arms with a neutral-length reasoning step or cut samples to match). 3 seeds. Report paired differences with CIs. Items need ground truth so checks are objective.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Reasoning items with known answers (math, logic, ARC-style, brainteasers) | A: no check; B: "has failed" premortem; C: "may fail" list; D: neutral length-matched step | Accuracy; count of valid causes (graded against known bug) | B vs C small or null; B/C vs A null or negative if ungated (Huang) |
| T2 | Same items | 2x2: frame (certain/possible) x content (reasons-against/neutral list) | Accuracy, Brier of stated confidence | Content drives any gain (Koriat); frame effect small |
| T3 | Mixed-difficulty items | Never-on, always-on, gated by 3-sample disagreement, gated by low P(True) | Accuracy per token; fire rate | Gated matches always-on at fewer tokens; always-on <= never-on on easy items |
| T4 | Items with a runnable check (code with tests, arithmetic, retrieval QA) | Internal-only premortem vs premortem causes turned into tests | Accuracy; rate of right-to-wrong flips | External variant gains (CRITIC +6 to +10 F1 expected); internal-only flat or negative |
| T5 | Multi-run agent tasks with recurring failure types | Premortem only; stored error lessons only; both; none | Success rate over 5 episodes | Lessons >= premortem; both stack modestly (ExpeL +5 on ALFWorld) |
| T6 | Tool-use agent tasks (WebArena-like) | Pre-action "what could go wrong" + backup vs post-failure reflection vs none | Success rate; plan revisions | Small gain (+1 to +4 points); revisions down |
| T7 | Items with calibration target | With and without failure listing | Brier of failure probability; stated failure rate vs observed | If Hill transfers, stated failure probability overshoots by 0.05 or more |
| T8 | Benign items that should be answered | Premortem on vs off | Over-hedge/refusal rate; accuracy | Small rise in hedging (a few points) |
| T9 | Hard items | 1 failure list vs 3 pooled lists | Valid causes found; accuracy at equal tokens | Pooling finds more causes but costs 3x tokens; likely loses at equal tokens |
| T10 | Forecasting items with resolved outcomes (if bench has them) | Add pre/post-mortem dimension vs none | Brier at equal cost | Tests whether the BTF-2 association is causal; expect small |

## 9. What does not transfer, and why

- **Psychological safety.** Klein's main stated aim is letting dissenters speak (a03). A single agent has no social cost of dissent. That whole motive drops out.
- **Team dynamics and group brainstorming.** The group-vs-individual question was in human teams. An agent's equivalent is parallel samples, which is a separate method (self-consistency).
- **Human overconfidence calibration.** Veinott's measured outcome is plan confidence of students. LLM confidence has its own calibration profile (SOTA calibration 0.002). A fall in confidence is not an accuracy gain in either species.
- **Hill's subadditivity.** Shown in 32 human search planners. It may or may not occur in LLMs. Untested.
- **Imagination of the future.** Mitchell's abstract says the time shift had little effect. A model with no sense of time need not "simulate the future". Only the certain-failure wording could carry over.
- **Safety results (InvThink).** Harm enumeration helps refusal behaviour. Our task is reasoning accuracy. The same paper's controlled test says the failure direction is not shown to matter.
- **Trained methods (AUGUR, CoMem, InvThink SFT+RL, RevThink).** They change weights. Our agent changes only the scaffold.
- **Behavioural field results (Peabody Exp 1).** Cadet team fouls in physical exercises. No agent equivalent beyond "errors committed in a timed multi-step task".
- **Self-report plan quality in implementation science.** Qualitative themes, no comparison.

## 10. Open questions

1. Does "it has failed" beat "it may fail, list reasons against" on LLM accuracy and calibration at equal tokens? (gap 1; nobody has tested)
2. What do Veinott 2010's means, SDs and effect sizes show? Did plan quality change, or only confidence? (gap 2; paper not reachable)
3. Can a cheap signal gate the step so it fires only when it helps? (partly: mechanism exists, no premortem-specific test)
4. Does an external check make a premortem safe? Direction yes from CRITIC; not tested for premortem.
5. Does listing causes inflate stated failure probability or cause over-hedging in LLMs? (open)
6. Is the BTF-2 Pre/Post-mortem association causal? Authors doubt it can be isolated.
7. Do stored lessons beat imagined failures, and do they combine? (partly closed; no head-to-head)
8. Does pooling several independent failure lists beat one list at equal tokens?
9. Is the 30 percent figure in Mitchell 1989's full text, and which condition does it refer to?
10. Does Wang 2024's anticipatory step add anything alone? No ablation published.
11. Does the premortem effect depend on model size or reasoning-mode models? Untested. Huang's results are on GPT-3.5 and GPT-4, older models, so modern reasoning models may differ.

## 11. Sources

[V] opened (page or PDF text read); [M] snippet or secondhand only.

- [V] Mitchell, Russo, Pennington 1989, abstract only (Crossref). https://doi.org/10.1002/bdm.3960020103 (full text not read)
- [M] Collins, The premortem (blog review). https://corporate.jcx.au/premortem (secondhand claims; a31, b02, b21, b22 read the page, a02 snippet)
- [V] Klein 2007, HBR landing page. https://hbr.org/2007/09/performing-a-project-premortem
- [V] Klein 2015 and 2021 Psychology Today blog. https://www.psychologytoday.com/us/blog/seeing-what-others-dont
- [V] Klein premortem page. https://www.gary-klein.com/premortem
- [M] Veinott, Klein, Wiggins 2010 (ISCRAM). https://researchr.org/publication/VeinottKW10
- [M] Gallop and Bischoff 2016. https://doi.org/10.1080/19488289.2016.1240118
- [V] Peabody 2017 thesis abstract. https://digitalcommons.mtu.edu/etdr/374/
- [M] Koriat, Lichtenstein, Fischhoff 1980. https://doi.org/10.1037/0278-7393.6.2.107
- [M] Hoch 1985. https://doi.org/10.1037/0278-7393.11.1-4.719
- [V] Hill 2012, Cognition in the woods (Cambridge Core). https://www.cambridge.org/core/ (article page as recorded in a11-a13)
- [V] Nemeth, Brown, Rogers 2001. https://doi.org/10.1002/ejsp.58
- [M] Posavac et al. 2008. https://doi.org/10.1086/527342
- [V] Implementation premortem review 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12330140/
- [V] Beidas et al. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9375077/
- [V] Uniqueness bias, arXiv 2408.07710. https://arxiv.org/abs/2408.07710
- [V] PreFlect, arXiv 2602.07187. https://arxiv.org/pdf/2602.07187
- [V] InvThink, arXiv 2510.01569. https://arxiv.org/pdf/2510.01569
- [V] Bench to the Future 2, arXiv 2604.26106. https://arxiv.org/pdf/2604.26106
- [V] Prompt engineering tutorial, arXiv 2609.22249. https://arxiv.org/abs/2609.22249
- [V] Zhang 2026 Prospective Hindsight, arXiv 2610.02740. https://arxiv.org/abs/2610.02740
- [V] Serrat 2017, The Premortem Technique. https://link.springer.com/chapter/10.1007/978-981-10-0983-9_
- [V] Aceituna 2019 PreHaz. https://doi.org/10.4271/2019-01-5066
- [V] Wippold et al. 2024. https://doi.org/10.1093/tbm/ibae060
- [V] Psihogios et al. 2024. https://doi.org/10.1037/cpp0000527
- [M] Elizabeth 2020 SJDM poster. https://dlab.sauder.ubc.ca/sjdm/presentations/
- [M] Roose, Lehman, Veinott 2023 (cited in PMC12330140). https://pmc.ncbi.nlm.nih.gov/articles/PMC12330140/
- [M] Luth, Flinchbaugh, Crawford 2017. https://doi.org/10.5465/ambpp.2017.15818abstract
- [V] Matern et al. 2025. https://doi.org/10.1213/xaa.0000000000001902
- [V] Kaustia and Perttula 2012. https://doi.org/10.1108/19405971211261100
- [V] Rusmana et al. 2020. https://doi.org/10.1163/23641177-bja00001
- [V] AUGUR (Hao, Yu, Lou 2026), abstract-level numbers only. https://doi.org/10.20944/preprints202610.0494.v1
- [V] Wang et al. 2024 Devil's Advocate / anticipatory reflection, arXiv 2405.16334. https://arxiv.org/abs/2405.16334
- [V] Huang et al. 2024, arXiv 2310.01798. https://arxiv.org/pdf/2310.01798
- [V] RevThink, arXiv 2411.19865. https://arxiv.org/abs/2411.19865
- [V] Reflexion, arXiv 2303.11366. https://arxiv.org/abs/2303.11366
- [V] Ke et al. 2024, arXiv 2401.14589. https://arxiv.org/abs/2401.14589
- [V] Lee et al. 2025, arXiv 2503.14263. https://arxiv.org/abs/2503.14263
- [V] CRITIC, arXiv 2305.11738. https://arxiv.org/pdf/2305.11738
- [V] Kamoi et al. 2024, arXiv 2406.01297. https://arxiv.org/pdf/2406.01297
- [V] Self-consistency, arXiv 2203.11171. https://arxiv.org/pdf/2203.11171
- [V] Adaptive-Consistency, arXiv 2305.11860. https://arxiv.org/pdf/2305.11860
- [V] Kadavath et al. 2022, arXiv 2207.05221 (abstract). https://arxiv.org/pdf/2207.05221
- [V] ExpeL, arXiv 2308.10144. https://arxiv.org/pdf/2308.10144
- [V] CoMem, arXiv 2610.25790. https://arxiv.org/pdf/2610.25790
- [V] Self-Refine, arXiv 2303.17651 (abstract). https://arxiv.org/pdf/2303.17651
- [V] arXiv, Crossref, Europe PMC searches for premortem terms (negative result). https://arxiv.org/search/?query=premortem&searchtype=all
