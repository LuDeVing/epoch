# Simulation vs theory accounts: deep document

*Subfield A14.05. Source files in this folder: evidence_a-d.jsonl (a01-a29, b01-b28, c01-c26, d01-d16), claims.jsonl (K01-K25), critique.md. Status of the subfield for our agent: background, with a few usable operators. Almost no study varies simulation against theory while holding everything else fixed. Most "tests" are the authors' own mapping of a method onto one camp.*

## 1. What it is

The question: how do people understand other minds?

- **Theory-theory (TT).** We hold a tacit folk theory of minds (beliefs, desires, perception) and apply it by inference. Mindreading is information-rich and theory-driven. Developmental form (Gopnik and Wellman 1992): the child is a small scientist who builds and revises a causal theory. Errors reflect a wrong theory. [a01, a27]
- **Simulation theory (ST).** We run our own mind offline on the other person's inputs and read off the result. Mindreading is information-poor and process-driven (Gordon 1986; Heal 1986; Goldman 1989, 2006). [a01, a02]
- **Hybrids.** Both camps converged on mixes. Heal (2003): simulate rational transitions, theorise causal ones. Perner also defended a hybrid. The SEP conclusion says a combined account is likely, form unclear. [a28]

Why it is only background for us. An LLM has no separate "own mind" to reuse. It runs the same next-token machinery for every role. So simulation and theory are not separable by architecture (a03). What carries over is the design vocabulary:

- TT maps to explicit rules and revisable hypotheses about the other party.
- ST maps to role-taking prompts: filter what the other knows, then answer from that view.
- Bayesian inverse planning (Baker et al. 2017) is a formal theory-theory with a planner inside. It blurs the camps. [a29, a17]

Hu, Sosa and Ullman (2025) say the field must first pick a target: match behaviour, or match the computation. Rival computations they list: theory inversion, simulation through one's own decision process, bottom-up feature mapping. [b23]

## 2. History and theories in depth

**Founding (1983-1992).**
- Wimmer and Perner (1983): the Maxi and chocolate task. Children of about 3 name the true location. Success rises to about 6. Not opened; no verified numbers. [a24]
- Baron-Cohen, Leslie and Frith (1985): Sally-Anne. Autistic children mostly fail, Down syndrome and typical 4-year-olds mostly pass. Used for a specific theory-of-mind deficit. Not opened; numbers recalled only (about 61 children). [a23]
- Gordon (1986) radical simulationism with "ascent routines": to ask whether X believes p, ask whether p. Carruthers' scope problem: this seems to work only for belief, not goals or fear. [a02]
- Gopnik and Wellman (1992): the child's theory of mind really is a theory. [a27]
- Perner and Howes (1992) on the TT side. [a01]

**Objections to simulation.** [a03]
- Dennett's collapse argument: simulation needs theory about the target, so ST collapses into TT.
- Anti-constitution arguments: judging "X believes p" is not given by simulating.
- Mechanism problem (Heal 1994).
- Mirror neurons: correlational, about actions not beliefs. Hickok (2009): human action-understanding evidence inconclusive.

**Egocentric error.** ST predicts we fail to quarantine our own knowledge (Goldman 2006; Birch and Bloom 2007 curse of knowledge). Critics (Saxe 2005; de Vignemont and Mercier 2016) say TT plus a processing bias fits too. [a04]

**Neural bridge.** Gallese and Goldman (1998): macaque F5 mirror neurons as low-level simulation. Wicker et al. (2003): anterior insula active for smelling disgust and for watching disgusted faces. Singer et al. (2004): pain empathy used affective regions, not sensory pain regions, when only a cue was shown, which limits pure mirroring. [a26, a07]

**The infant puzzle.** Verbal false-belief: fail at 3, pass at 4. Looking-time tasks suggest sensitivity at 15 months (Onishi and Baillargeon 2005) and maybe 7 months. Goldman and Jordan (2013): ST explains the gap, since infants imagine the scene from the other's view while the verbal task needs full mindreading plus inhibition. Rivals: Perner and Ruffman 2005, Apperly and Butterfill 2009 (success need not mean belief representation). [a05, a08]

**Machine era.**
- ToMnet (Rabinowitz 2018): a meta-learned observer. Passes a gridworld Sally-Anne test. It cites both camps and implements neither. A third path: ToM as a prior over agent types. [a20, c14]
- 2022-2023: Sap et al. say GPT-3 lacks social intelligence. Kosinski says GPT-4 solves 75% of false-belief tasks. Ullman and Shapira show it breaks on small alterations. [a15, a12, a13, a14]
- 2023-2025: prompt-level simulation (SimToM), belief trackers (SymbolicToM), Bayesian inverse planning (BIP-ALM), hypothesis loops (ThoughtTracing, Hypothetical Minds), and the SimpleToM finding that inference is not applied.
- 2025-2026: reasoning models do not reliably beat non-reasoning twins; independent SimToM runs disagree with the original; first mechanistic test of ST in LLMs (Aoki and Kawahara). [d01, d05, b12]

## 3. Core findings with exact numbers

Status: established, single-source, contested, or human-only.

### 3a. Human development

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Children go from below to above chance on verbal false belief | 178 studies. Below chance at about 41 months, above at about 48. Age alone R2=.39 (362 primary conditions). Age + country + 4 task factors R=.74, R2=.55. Odds of correct x2.94 per year. About 50% at 44 months, 74.6% at 56 months | Wellman et al. 2001 [b01, b02] | established, human-only. Curve fits both camps |
| Task features help even young children | Motive to deceive, active participation, salience of reality, protagonist present. Do not remove the age trend | Wellman 2001 [b02] | established |
| Early competence reading disputed | Scholl and Leslie reply: the curve is compatible with early-competence accounts | [b27] snippet only | contested |
| Executive function links to false belief | 102 studies, 9,994 children aged 3-6. Early EF predicts later false belief, not the reverse. Same across cultures | Devine and Hughes 2014 [b03] | established, abstract only |
| Language links to false belief | 104 studies, N=8,891, under 7. Moderate to large, survives age control. Earlier language predicts later false belief | Milligan et al. 2007 [b04] | established, abstract only |
| ToM training works | 32 papers, 45 studies, 1,529 children, mean age 63 months. Hedges g=0.75, CI 0.60-0.89 | Hofmann et al. 2016 [b05] | established, abstract only |
| Cross-culture unity of false belief tasks | Namibia (Hai\|\|om N=65, Khwe N=35, ages 3-9), Leipzig N=66. Tasks linked within child. Format mattered for Hai\|\|om | 2026 preprint [d15] | single-source, abstract only |

### 3b. Infant replications

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Anticipatory-looking false belief fails in 24-26-month-olds | 160 tested, 70 excluded, 90 analysed. 49 of 90 (54%) anticipated in familiarisation trial 2 (original 20 of 31, 65%). 22 of 49 correct at test, p=.568. Mean looking score 0.47, CI [0.36, 0.57], t(47)=-0.63, p=.532 | Kampis et al. 2021 [a09, b07] | established (replication) |
| Same paradigm, 2-3 y and 25 months | Exp 1 N=48 fail. Preregistered Exp 2 N=78 fail. Adults N=115 succeed | Schuwerk et al. 2018 [b06] | established |
| 1 of 4 anticipatory-looking tasks replicated; that one failed once confounds were removed | Sample sizes not read | Kulke et al. 2018 [d12] | single-source, abstract only |
| Looking-time false-belief updating replicates only with closer procedure; also appears for uninformative statements | Two studies failed conceptual replication | Song 2008 replication [d13] | single-source, abstract only |
| Infant ToM disunity across paradigms | Not recorded | Poulin-Dubois and Yott 2018 [a10] | single-source, unopened |
| Onishi and Baillargeon 2005 (15 months, looking time) | Not verified. Replication status not checked | [a08] | unverified |

### 3c. Adult simulation biases

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Perspective-taking is anchor-and-adjust, with too little adjustment | Five studies. Time pressure raises egocentric bias. Accuracy incentives lower it. Adjustment stops at plausibility. N not read | Epley et al. 2004 [b08] | established, abstract only |
| Mirror and mentalizing systems split by input | More than 200 fMRI studies. Mirror for body-part actions, mentalizing (TPJ, mPFC, precuneus) for abstract cues. Rarely co-active | Van Overwalle and Baetens 2009 [b09] | established, abstract only |
| Pupil mimicry changes judged emotion | Pupils at 180% made sad faces rated less negative | Harrison 2006 via Wikipedia [a07] | single-source |

### 3d. LLM findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Classic false-belief solved by strong LLMs with strict scoring | 40 tasks, 16 prompts each, all must pass. davinci-002 5%. davinci-003 and GPT-3.5-turbo 20%. GPT-4 (June 2023) 75% (CI 66-84). GPT-4 90% contents vs 60% transfer (chi2=8.07, P=.01). davinci-003 90 to 60 to 20 as controls added | Kosinski 2024 [a12, c04] | established |
| Trivial alterations break models | Ullman: GPT-3.5, few anecdotal cases. Shapira: GPT-4 97% original, transparent-access 66.7% (davinci-002) to 0% (GPT-4), "inon" 71.4% to 0%, other-person 93.8% to 68.8% | [a13, a14, c06] | contested (humans also fail about half, N=757, Strachan) |
| Part of the failure is response bias | GPT faux pas hyperconservatism. o1-preview false belief 100 vs true belief 36. o1 high-effort 97/49. GPT-4o 38.5/80.5. R1 77/59.5 | Strachan 2024; ThoughtTracing [a11, d16, c17] | established |
| Battery vs humans | 1,907 humans, 15 sessions per LLM. Irony GPT-4 above (P=.040, r=.32). Faux pas GPT-4 below (P=5.42e-5, r=.55). Strange stories above (P=1.04e-5, r=.60). False belief at ceiling | Strachan 2024 [d16] | established |
| SimToM raises false belief for weaker models | GPT-3.5 BigToM FB 41.0 to 70.5 (+29.5 vs 0-shot, +14.2 vs CoT 56.25). ToMI 67.25 to 81.0. Llama2-7b BigToM 47.5 to 70.5. GPT-4 ToMI 25.5 (0-shot) and 74.25 (CoT) to 87.75. GPT-4 BigToM 89.0 / 93.25 CoT / 92.0 SimToM | Wilf et al. 2023/2024 [a16, c01, b10] | contested |
| Independent SimToM runs disagree | BigToM belief acc SimToM vs plain: Qwen3-32B 0.355 vs 0.900; Qwen3-8B 0.615 vs 0.830; Llama-3-70B 0.530 vs 0.812; R1 0.740 vs 0.890. SimpleToM action acc SimToM higher: Llama-3-8B 0.900 vs 0.505; Qwen3-32B 0.950 vs 0.767 | Chen et al. 2026 [d05] | contested |
| SimToM needs separate call and good filter | GPT-3.5 FB (ToMI/BigToM): SimToM 81.0/70.5; Single 58.75/50.75; Multi 31.75/37.25; domain-specific 85.5/90.5; oracle 96/96 | Wilf ablation [b11, c02] | single-source (GPT-3.5 only) |
| SimToM does not transfer to harder or multi-agent items | MMToM-QA text: GPT-4 48.0 to 52.5; false-belief item 12.0 to 15.0. UniToMBench: hurt Llama 3 8B and Gemma 2 27B on evolving stories | [a17, b20, c23] | established |
| Belief tracker beats prompting | SymbolicToM on ToMi: GPT-3.5 gains +51 to +99, GPT-4 +4 to +42 (column to question-type mapping not done). MMToM text: SymbolicToM 63.0, false-belief item 61.0 | Sclar 2023 [c10, b20] | established (template benchmark) |
| Theory-style generative model beats prompting | MMToM-QA multimodal: humans 93.0, GPT-4V 44.0, BIP-ALM LLaMA2 76.7, GPT-J 75.3. Text: humans 82.5, GPT-4 48.0, GPT-3.5 38.3, BIP-ALM 71.7. False-belief item: GPT-4 12.0, BIP-ALM 69.0 | Jin 2024 [a17, b19, c15] | established |
| Hypothesis generate-and-weight | GPT-4o ParaphrasedToMi 59.5 to 76.0 (+CoT 74.3). FANToM AllQs 11.1, CoT 40.7, TT 41.5, TT+CoT 54.7. MMToM avg 56.5 to 60.0 (69.0 with CoT); goal sub-score 56.1 (CoT) to 37.8 (TT) | Kim 2025 ThoughtTracing [c16] | established, uneven |
| Foresee and Reflect | T4D: GPT-4 50% to 71%; up to +50 over CoT, Self-Ask, ToT | Zhou 2023 [c12] | single-source |
| Inference fine, application poor | SimpleToM, 1147 items per type. Mental state: GPT-4o 95.6, Llama-405B 97.8, Claude-3.5 97.9. Behaviour: 49.5 / 58.2 / 67.0. Judgment: 15.3 / 10.0 / 24.9. GPT-3.5 36.5/7.6/29.1 | Gu et al. 2026 [b18, c19] | established |
| Reminder closes the gap | Behaviour: GPT-4o 49.5 to 82.8, Claude 67.0 to 96.9. Judgment: GPT-4o 15.3 to 42.2, Llama 10.0 to 25.8, Claude 24.9 to 84.1. System prompt and generic CoT: GPT-4o 47.3 and 62.8 | Gu 2026 [c20] | established |
| Consistency across question types | FANToM ALL: human 87.5, GPT-4 CoT 26.6 / 14.8, ChatGPT 3.7, Llama-2 0.4, fine-tuned Flan-T5 53.7 | Kim 2023 [a19, c11] | established |
| Backward belief hardest | BigToM: humans 82% (TB), 72% (FB). GPT-4 0-shot .53 FB. Forward action FB .81 (no initial belief) to .98 (1-shot) | Gandhi 2023 [a18, c07] | established |
| Higher-order belief | Street: GPT-4 100% vs humans 96% at order 2, 95% vs 82% at order 4; human-GPT-4 diff chi2=0.41 p=.522; humans better only at order 5 (p=.0126). Hi-ToM: near zero at order 4; CoT GPT-4 58.11 to 59.88, GPT-3.5 27.50 to 35.50 | [b21, c08, c09] | contested (formats differ) |
| Reasoning models not reliably better | HiToM: GPT-4o .607, o3 .747, R1 .549, Qwen3-8B .558, Qwen3-8B reasoning .481. o3 .838 at lowest effort to .693 at highest. Qwen3-8B reasoning capped 1,500 tokens .706 | Gong 2026 [d01, d02] | single-source |
| Option matching inflates scores | HiToM without options: R1 .549 to .691. Slow-to-Fast: R1-Distill-32B .571 to .701 | [d03] | single-source |
| Model-written ledger is unreliable | 895 stories, 22,343 propositions. Best story-macro F1 61.63. Knowledge-access accuracy 56.13-74.59%. Judge swap shifts F1 14-19 points | OmniToM [d04] | single-source |
| Theory-like coherence is weak | GPT-4o cross-domain rho: beliefs .78 (CI .68-.85), desires .39 (.2-.57), costs .18 (.09-.27) | Muchovej 2025 [b22] | contested |
| Literal ToM does not give functional ToM | RPS vs single-action partner: tabular regret 0.083 (ToM 97.4%); Llama-2 70B 0.857 (92.1%); Mixtral 0.542. Oracle inputs still worse. Social prompt 0.643, CoT 0.648, QA 0.881 | Riemer 2025 [d08, c21] | established |
| Hypothesis list scored by outcomes | Hypothetical Minds beats ReAct, PlanReAct, Reflexion in Melting Pot; best in 5 of 10 scenarios. 3+k calls per step. k above 3 diminishing | Cross 2025 [c25, d09] | single-source, no token match |
| First-order ToM tracks success | Hanabi, about 14 models: r=0.76 first-order vs 0.58 second-order (LLM judge) | Liang 2025 [d07] | single-source |
| Benchmark score without simulation | 7B RL: Hi-ToM 84.50% vs GPT-4o 69.00%, DeepSeek-V3 70.17%. SFT often matches RL | Lu 2025 [d10] | single-source |
| First-person framing recovers belief structure | Wildfire survey domain. Pairwise corr .6643 vs .4071 (third person); CoT .4036. Final action .9157 vs .8383 | Chen 2026 [d06] | single-source, other domain |
| Self and other belief decodable | Linear probes, 7B models. Steering lifts FB accuracy; row mapping inferred | Zhu 2024 [a22, b13, d11] | single-source |
| First-person linear map flips answers weakly | Llama-3.1-70B 198/200, Qwen2.5-72B 196/200 items kept; net effect up to about 0.2 vs ideal 1 | Aoki and Kawahara 2025 [b12, c22] | single-source |
| Old baselines | GPT-3: SocialIQa 55%, ToMi 60%, over 30 points below humans; 10 to 35 examples gave about +1 | Sap 2022 [a15, c13] | established, older models only |
| ToMBench | Human 85.4% vs GPT-4-1106 75.3%; GPT-4 above humans on false belief only | Chen 2024 [c18] | single-source |
| Agent simulation | 200 simulations, 5 tasks; actions often not chosen from attributed beliefs | Lombardi and Lenci 2025 [b25] | single-source, abstract skimmed |

## 4. Mechanisms and models

Each is described by what the program does and what the LLM does, so it can be built.

### 4.1 Role-taking filter (SimToM)
Two separate model calls, code in between.
1. Call A. Input: full story, character name. Output: only the events the character witnessed or was told. Prompt: "Which events does X know about?"
2. Code replaces the story with Call A's output. The original is not shown to Call B.
3. Call B. Input: filtered story and the question. Output: answer.

Rules from the ablation: keep A and B as separate calls (single-prompt version lost about 20 points on GPT-3.5, [b11]). Filter quality is the bottleneck (oracle filter 96 vs about 70-81 model-made). Gain was large on GPT-3.5 and Llama2-7b, small or mixed on GPT-4, absent on harder or multi-agent items, and negative for belief questions in an independent run [d05].

### 4.2 Who-knows-what ledger (SymbolicToM style)
Code holds, per character, a set of facts they know, and per character pair, what A thinks B knows (depth set by design).
- Update rule: when an event occurs, add it to every character present. Characters who leave do not receive later events.
- Question time: code builds the filtered story for the target character (or nested for second order) and the model answers over that view only.
- On ToMi the tracker gave +4 to +99. Caveat: templates make entity-event extraction easy. With free text the extraction is the weak step: OmniToM best F1 61.63, knowledge-access accuracy 56-75% [d04]. So a model-written ledger needs a cross-check by code or a second pass.

### 4.3 Bayesian inverse planning (BIP-ALM)
Theory-style. A symbolic state (goal, belief, world) is extracted. The LLM scores how likely the observed actions are under each hypothesised goal-belief pair. Code normalises across hypotheses and picks the most probable. It beat GPT-4 on MMToM-QA (false-belief item 69.0 vs 12.0) but needs structured state. For a text agent: enumerate 2 to 4 candidate (goal, belief) hypotheses, ask the model per hypothesis "how likely is this action given it", normalise in code (this fits G5).

### 4.4 Hypothesis generate-and-weight (ThoughtTracing, Hypothetical Minds)
Loop per observation:
1. Model proposes hypotheses about the other party's mental state or strategy.
2. Code weights each by how well it predicts the next observation (real outcome, not the model's opinion).
3. Keep top-k (k about 3; above 3 diminishing, above 5 may hurt).
4. Refine the losers, repeat.

Gains uneven: Qwen 2.5 did not improve on FANToM with TT alone; MMToM goal sub-score fell [c16].

### 4.5 Apply-the-belief step (SimpleToM reminder)
After the model states what X knows, code writes that answer back into the prompt immediately before the action or judgment question. One line. Gains +33 (GPT-4o behaviour) and +30 (Claude). A generic system prompt did nothing [c20]. It is a code-controlled hand-off, which matches our rule that the program decides steps.

### 4.6 Foresee and Reflect (FaR)
Two-step zero-shot. Foresee: predict the others' likely next actions and what they will need. Reflect: choose own action given that. GPT-4 50% to 71% on T4D [c12].

### 4.7 Anchor-and-adjust with several passes
Human simulation starts from own view and under-adjusts; accuracy incentives and time reduce the bias [b08]. Implementation idea: draft from own view, then in a later call list which facts the other lacks and redo. Untested in LLMs.

### 4.8 Consistency probe (FANToM)
Ask 6 question types about the same hidden fact (belief, answerability, info access, and so on). Score "ALL" only if every one agrees. A single question hides illusory ToM [c11].

### 4.9 Control pairing
Every false-belief item gets a true-belief twin and a perturbed variant. Strict score needs all to pass (Kosinski). This detects both "always suspects false belief" and "pattern-matches the textbook case" [a12, c17].

## 5. What holds up

**Holds up.**
- The age curve for verbal false belief (178 studies, R2=.39 from age alone). It does not separate the camps. [b01]
- Strict scoring matters: Kosinski davinci-003 fell 90 to 20% as controls were added. [a12]
- LLMs infer knowledge states well but do not apply them (SimpleToM, above 95% inference vs 49.5-67.0 behaviour). A reminder fixes much of it. [c19, c20]
- Explicit belief tracking or a generative model beats prompting alone on harder items (MMToM-QA, ToMi). [c10, a17]
- Perspective filter quality limits any role-taking gain. [b11, d04]
- Literal ToM accuracy does not give functional adaptation. [d08]

**Fails or weak.**
- Infant implicit belief tracking from anticipatory-looking: Kampis 2021 (160 infants), Schuwerk 2018 (N=48, N=78), Kulke 2018 (1 of 4). The authors say this does not show infants lack ToM, only that the paradigm is unreliable. [a09, b06, d12]
- SimToM as a general gain. Original lab: large on weak models. Independent lab: large losses on BigToM belief for 2025 backbones (Qwen3-32B 0.355 vs 0.900). Gains on SimpleToM action accuracy. Net: a tested option, not a default. [d05, a16]
- SimToM on MMToM-QA (+4.5) and on multi-agent evolving stories (harm). [b20, c23]
- Reasoning models and more thinking: no reliable ToM gain; o3 worse at high effort on HiToM (.838 to .693). [d01, d02]
- CoT on higher-order items: +1.77 for GPT-4 on Hi-ToM. [c09]
- In-context examples: about +1 point for GPT-3 (Sap). [a15]
- Generic system prompts on SimpleToM: -2.2 to +6.3. [b18]

**Moderators.**
- Model strength: SimToM helps weaker models, not GPT-4 on BigToM (near ceiling 89-93).
- Benchmark structure: template (ToMi, BigToM) vs free text; BigToM was written by GPT-4.
- Question type: forward action vs backward belief; behaviour vs judgment vs mental state.
- Answer format: multiple choice options let reasoning models match options (R1 .549 to .691 without options). [d03]
- Scoring: all-controls strict vs lenient.
- Human baseline: humans also fail about half of perturbed items (N=757). [d16]

**Interventions that worked.** Reminder line (+33 / +30). Hypothesis weighting (ThoughtTracing +16.5 on ParaphrasedToMi for GPT-4o). Belief tracker (+4 to +99). Capped reasoning (Qwen3-8B capped at 1,500 tokens .706 above both uncapped modes). Child ToM training (g=0.75).

**Interventions that did not.** Generic CoT on Hi-ToM. Generic system prompt. Single-prompt SimToM. Domain-specific multi-step SimToM (31.75). Extra in-context examples. High effort reasoning.

**Not resolved.** Whether any of this is simulation or theory. First-person vs third-person framing (d06) is the closest proxy and it is from one model in another domain.

## 6. Language models

**Trend.** Davinci-002 5% to GPT-4 75% on Kosinski's strict set in about one year of model releases. Instruction tuning and RLHF did most of this, not prompt format (Sap found examples gave +1; van Duijn 2023 found instruction-tuned models beat base models and often children aged 7-10, with 37 and 36 children per age group; per-model scores not extracted). [a15, a21]

**Where they pass.** Classic false belief with strict scoring (strong models). Higher-order true/false statements (GPT-4 matches adults, orders 2-6; chi2=0.41). Irony, hinting, strange stories.

**Where they fail.**
- Perturbed or adversarial variants (Shapira; Ullman). Humans also drop.
- Faux pas (GPT-4 below humans, r=.55), but the cause is hedging.
- FANToM consistency: GPT-4 CoT 14.8-26.6 vs human 87.5.
- Backward belief (GPT-4 0-shot .53 FB).
- MMToM false-belief item (GPT-4 12.0).
- Applying belief to behaviour (SimpleToM).
- Adapting to a partner over repeated play (Riemer).
- Cross-domain consistency of inferred desires and costs (rho .39, .18).
- Free-text who-knows-what extraction (F1 61.63).

**What changed scores, by how much.**

| Change | Effect | Model | Source |
|---|---|---|---|
| Strict scoring with controls | 90 to 20 | davinci-003 | a12 |
| SimToM (two calls) | +29.5 BigToM FB | GPT-3.5 | a16 |
| SimToM, independent lab | -54.5 BigToM belief (0.355 vs 0.900), +18.3 SimpleToM action | Qwen3-32B | d05 |
| Oracle perspective filter | 70.5 to 96 | GPT-3.5 | b11 |
| Belief tracker | +4 to +99 | GPT-4, GPT-3.5 | c10 |
| BIP-ALM vs plain | 48.0 to 71.7 text | GPT-4 vs GPT-J based | a17 |
| ThoughtTracing | 59.5 to 76.0 ParaphrasedToMi; 11.1 to 41.5 FANToM | GPT-4o | c16 |
| Awareness reminder | 49.5 to 82.8 behaviour | GPT-4o | c20 |
| FaR | 50 to 71 | GPT-4 | c12 |
| More reasoning effort | .838 to .693 HiToM | o3 | d02 |
| Remove answer options | .549 to .691 | R1 | d03 |
| First-person framing | pairwise .41 to .66 | one model, wildfire survey | d06 |
| Steering (+TpFo) | forward-belief FB 0.98 (row inferred) | Mistral-7B | d11 |

**Internal evidence.** Self and other belief are linearly decodable (Zhu). A linear map from third-person to first-person representations flips answers a little (Aoki and Kawahara; net effect up to about 0.2 of an ideal 1). Perturbing about 0.001% of ToM-sensitive parameters hurts ToM and also hurts context localisation and language understanding (Wu 2025), so social reasoning leans on general context tracking. [a22, b12, b14]

**Caveat on shortcuts.** A 7B model trained with RL reached Hi-ToM 84.50% vs GPT-4o 69.00%, sometimes with collapsed short reasoning. Template benchmark scores say little about human-like simulation. [d10]

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Code passes the model's own "what does X know" answer into the next step that predicts or judges X's action. One line, inserted by code. Do not rely on a generic "think about their mind" system prompt or generic CoT. | S (state hand-off) and O | [E] | b18, c19, c20, d08 |
| A2 | Every belief or perspective check uses a control pair: false-belief, true-belief twin, and a perturbed variant. Strict score needs all. Flag asymmetric accuracy. | G4 (eval rule) | [E] | a12, c04, c17, a11, d16 |
| A3 | Evaluate on consistency across question types about the same hidden fact, not on one question. | G4 | [E] | a19, c11 |
| A4 | Where several parties know different things, hold a who-knows-what ledger in code and answer over the filtered view. Cross-check model-written ledger entries by code or a second pass. | memory / S | [E] for the ledger, [S] for model-written entries | c10, a17, b20, d04 |
| A5 | Never score belief tracking with one paradigm or one benchmark. Use at least two formats and a human or plain-model baseline. | G7 (eval rule) | [E] | a09, b06, b07, d12, a11 |
| A6 | Include backward-inference items (infer what a user wants from what they did) in agent evals; this is the weak slot. | eval | [E] | a18, c07 |
| A7 | Score free-form, not multiple choice, when judging reasoning on ToM-like items. | eval | [S] but cheap | d03 |

A1-A6 are eval design and a hand-off line. None changes the schema graph. A1 and A4 are the only ones with an agent-side form. Caution on A4: the ledger evidence is from template benchmarks.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Separate perspective-filter call before answering any question about what another party believes or would do. | O (role-taking operator, S1/S2) | [C] | a16, b10, c01, c02, d05, b20, c23 |
| T2 | Hypothesis list about another party, scored by real outcomes, k=3. | O, G2 | [E] on benchmarks, [S] on token parity | c16, c25, d09, c12 |
| T3 | Anchor-and-adjust: second pass listing facts the other party lacks. | O | [S] | b08, a04 |
| T4 | Explicit rule list (theory) plus role-taking (simulation) vs either alone. | O, memory | [C] | a28, b09, a17 |
| T5 | Capped reasoning per social-inference step. | G11 | [S] | d01, d02 |
| T6 | Scoring of goal-belief hypotheses by model likelihoods, normalised in code. | O, G5 | [S] | a17, b19 |
| T7 | Foresee and Reflect before acting around another party. | O | [S] | c12 |
| T8 | Multi-agent filter: check that distinct agents get distinct knowledge. | O | [S] | c23 |

## 8. Concrete tests on our bench

All arms at equal total tokens. Setup cost counted (G7). Report the strict control-paired score where noted.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 (T1) | BigToM and ToMI false-belief plus true-belief twins; 100 items each | plain; CoT; CoT x2 self-consistency (code vote); two-call filter then answer | strict pair accuracy (false and true both right) | Weak model: +10 to +30 points vs CoT. Strong model: -3 to +3. Independent lab saw losses on belief |
| E2 (A1) | SimpleToM-style behaviour and judgment items, 200 each | plain; generic CoT; code-inserted awareness line | accuracy | +25 to +35 behaviour (GPT-4o effect was +33.3) |
| E3 (A1+A4) | Perturbed items (transparent container, informed protagonist, second-person move) | plain; reminder; ledger; reminder + ledger | accuracy on perturbed and original | Reminder and ledger stack; perturbed accuracy up 10+ points. No published test |
| E4 (T2) | FANToM-style conversations; ALL score | CoT; hypothesis list k=3; token-matched CoT x N | ALL score | +15 to +30 for a mid-size model. Partly from extra tokens, so match tokens |
| E5 (T1, T8) | Multi-agent evolving stories where three agents differ in knowledge | plain; filter per agent; ledger | accuracy; count of items where all agents got the same knowledge set | Filter alone may collapse agents; ledger should not |
| E6 (T4) | Items about a user's intent from their actions (backward inference) | role-taking only; rule list only; both; plain | accuracy; strict pair | Both beats either by 3-8 points if the hybrid helps |
| E7 (T5) | HiToM-style order 2-4 items, free-form | uncapped thinking; thinking capped at 1,000 and 1,500 tokens; CoT | accuracy | Cap equals or beats uncapped on hard items |
| E8 (T3) | Items where own knowledge differs from the other's (curse of knowledge) | one-pass role-taking; two-pass adjust | accuracy | +2 to +6 if egocentric leak is the cause |
| E9 (A2) | True-belief twin check on each model we use | false-belief and true-belief scored separately | asymmetry (FB minus TB) | Shows if the o1-style 100/36 pattern persists |
| E10 (T6) | Goal-belief inference from action traces, 4 hypotheses | model direct answer; model likelihoods normalised by code | accuracy | +10 to +30 over direct on false-belief-type items |

## 9. What does not transfer, and why

- **Infant looking-time and neural evidence.** No text analogue. Mirror neurons, pupil mimicry, insula overlap are body-based. [a07, a26]
- **The simulation vs theory dispute itself.** In an LLM the "own mind" and the "theory" are the same weights. The dispute cannot be settled by prompt design. What we use are two prompt shapes, not two minds. [a03]
- **Age curve.** Human development of false belief says nothing about what an agent scaffold should add. It also fits both camps. [b01, b27]
- **Template benchmark gains.** ToMi and BigToM are templated; BigToM was written by GPT-4. SymbolicToM and SimToM gains are probably inflated by this. A 7B model trained on Hi-ToM-style data beats GPT-4o without human-like reasoning. [d10]
- **Mirror/mentalizing split.** Interesting for brains, no direct agent rule. [b09]
- **Mechanistic steering.** Needs weight access; Zhu's rows are inferred from garbled tables; Aoki's flip rate is small. Not a prompt-level tool. [b13, c22]
- **ToM training in children (g=0.75).** Shows explicit concepts help children. Does not show that adding concept rules helps an LLM. [b05]
- **Deep nesting.** First-order tracking tracks success more than second-order in Hanabi (r=.76 vs .58). Deep recursion is low priority for an agent. [d07]
- **Pure Bayesian inverse planning.** Needs structured symbolic input. Works for household simulators, not for open text without extraction, and the extraction is the weak step. [a17, d04]

## 10. Open questions

1. At equal tokens, does a separate perspective-filter call beat CoT plus self-consistency on current frontier models (BigToM, ToMI, SimpleToM, FANToM)? No paper matches tokens. (Gap 1.)
2. Do a code-inserted awareness line and a code-held ledger stack on perturbed items? (Gap 2.)
3. How often does the model-written filter collapse agents or leak, and at what error rate does the gain vanish? Oracle 96 vs about 70-81; OmniToM suggests F1 under 0.62. (Gap 3.)
4. Do 2025-2026 reasoning models still over-suspect false belief (o1-preview 100 FB / 36 TB)? Untested split. (Gap 4.)
5. Is there any experiment that varies role-taking against an explicit rule list on one model and one item set? Not found. (Gap 5.)
6. Independent replication of SymbolicToM, ThoughtTracing, Hypothetical Minds. (Gap 6.)
7. Does Onishi and Baillargeon 2005 (looking time) replicate at ManyBabies scale? (Gap 7.)
8. Does the application gap persist in interactive agent loops, and does an outcome-scored hypothesis list close it at equal tokens? (Gap 8.)
9. Are Zhu's steering numbers and Aoki's flip rates reproducible, and do they predict prompt-level benefit? (Gap 9.)
10. Which perturbations are fair for humans too? Per-item table of Strachan N=757 not opened. (Gap 10.)
11. Why does SimToM drop belief accuracy so much on Qwen3-32B in the independent run? Prompt wording, reasoning mode, or format? Not diagnosed.

## 11. Sources

[V] = opened and read (per the opened flag in the evidence files; some are abstract pages, noted). [M] = snippet or abstract only, not opened in full.

**Reviews and encyclopaedia**
- [V] Stanford Encyclopedia, Folk Psychology as Mental Simulation. https://plato.stanford.edu/entries/folkpsych-simulation/ (a01-a05, a28)
- [V] Wikipedia, Theory-theory. https://en.wikipedia.org/wiki/Theory-theory (a06)
- [V] Wikipedia, Simulation theory of empathy (fetch-tool summary). https://en.wikipedia.org/wiki/Simulation_theory_of_empathy (a07)
- [M] Barlassina and Gordon 2017 (SEP, definition source). https://plato.stanford.edu/entries/folk-psych-simulation/ (c26)
- [V] Hu, Sosa and Ullman 2025, Re-evaluating ToM evaluation. https://arxiv.org/pdf/2502.21098 (b23)
- [V] Riemer et al. 2025, Position: ToM benchmarks are broken. https://arxiv.org/abs/2412.19726 (b24, c21, d08)

**Founding and developmental**
- [M] Onishi and Baillargeon 2005. https://pmc.ncbi.nlm.nih.gov/articles/PMC3357322/ (a08, abstract only)
- [M] Baron-Cohen, Leslie and Frith 1985. https://doi.org/10.1016/0010-0277(85)90022-8 (a23, numbers from memory)
- [M] Wimmer and Perner 1983. https://doi.org/10.1016/0010-0277(83)90004-5 (a24)
- [M] Gopnik and Wellman 1992. https://doi.org/10.1111/j.1468-0017.1992.tb00202.x (a27)
- [M] Gallese and Goldman 1998. https://doi.org/10.1016/S1364-6613(98)01262-5 (a26)
- [M] Baker et al. 2017. https://doi.org/10.1038/s41562-017-0064 (a29)
- [V] Wellman, Cross and Watson 2001. https://home.cs.colorado.edu/~mozer/Teaching/syllabi/3702/readings/WellmanCrossWatson2001.pdf (a25 unopened, b01, b02 opened)
- [M] Scholl and Leslie 2001. https://pubmed.ncbi.nlm.nih.gov/11405571/ (b27, snippet)
- [V] Devine and Hughes 2014 (abstract page). https://pubmed.ncbi.nlm.nih.gov/24605760/ (b03)
- [V] Milligan, Astington and Dack 2007 (abstract page). https://pubmed.ncbi.nlm.nih.gov/17381794/ (b04)
- [V] Hofmann et al. 2016 (abstract page). https://pubmed.ncbi.nlm.nih.gov/26901235/ (b05)
- [V] Epley et al. 2004 (abstract page). https://pubmed.ncbi.nlm.nih.gov/15382983/ (b08)
- [V] Van Overwalle and Baetens 2009 (abstract page). https://pubmed.ncbi.nlm.nih.gov/19524046/ (b09)
- [V] Kampis et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8386515/ (a09, b07)
- [V] Schuwerk et al. 2018. https://pubmed.ncbi.nlm.nih.gov/29892412/ (b06)
- [M] Poulin-Dubois and Yott 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5871541/ (a10)
- [M] Kulke et al. 2018, how robust (snippet). https://www.sciencegate.app/document/10.1016/j.cogdev.2017.09.001 (b28)
- [M] Kulke et al. 2018, Psych Science (abstract metadata). https://doi.org/10.1177/0956797617747090 (d12)
- [M] Song et al. 2008 replication preprint. https://osf.io/preprints/psyarxiv/kfgr8 (d13)
- [M] Infants and failed communication preprint. https://osf.io/preprints/psyarxiv/hmtvs (d14)
- [M] Developmental unity across cultures, 2026. https://osf.io/preprints/psyarxiv/5ef9v_v1 (d15)

**LLM studies**
- [V] Kosinski 2024. https://arxiv.org/abs/2302.02083 (a12, b15, c04)
- [V] Ullman 2023. https://arxiv.org/abs/2302.08399 (a13, b16, c05)
- [V] Shapira et al. 2023. https://arxiv.org/abs/2305.14763 (a14, b17, c06)
- [V] Sap et al. 2022. https://arxiv.org/abs/2210.13312 (a15, c13)
- [V] Wilf et al. 2023/2024, SimToM. https://arxiv.org/abs/2311.10227 and https://aclanthology.org/2024.acl-long.451.pdf (a16, b10, b11, c01-c03)
- [V] Jin et al. 2024, MMToM-QA. https://arxiv.org/abs/2401.08743 (a17, b19, b20, c15)
- [V] Gandhi et al. 2023, BigToM. https://arxiv.org/abs/2306.15448 (a18, c07)
- [V] Kim et al. 2023, FANToM. https://arxiv.org/abs/2310.15421 (a19, c11)
- [V] Rabinowitz et al. 2018, ToMnet. https://arxiv.org/abs/1802.07740 (a20, c14)
- [V] van Duijn et al. 2023 (partial). https://arxiv.org/abs/2310.20320 (a21)
- [V] Zhu, Zhang and Wang 2024. https://arxiv.org/abs/2402.18496 (a22, b13, d11)
- [V] Strachan et al. 2024. https://www.nature.com/articles/s41562-024-01882-z and https://pmc.ncbi.nlm.nih.gov/articles/PMC11272575/ (a11, d16; c24 marked unopened)
- [V] Aoki and Kawahara 2025. https://aclanthology.org/2025.ijcnlp-srw.9 (b12, c22)
- [V] Wu et al. 2025, Sensitivity Meets Sparsity (abstract and intro). https://arxiv.org/pdf/2504.04238 (b14)
- [V] Gu et al. 2026, SimpleToM. https://arxiv.org/abs/2410.13648 (b18, c19, c20)
- [V] Street et al. 2024. https://arxiv.org/abs/2405.18870 (b21, c08)
- [V] Muchovej et al. 2025. https://arxiv.org/pdf/2602.12150 (b22)
- [V] Lombardi and Lenci 2025 (abstract and method skimmed). https://arxiv.org/pdf/2510.13395 (b25)
- [M] Babarczy et al. 2026, Strange Stories. https://arxiv.org/pdf/2603.18007 (b26, not evaluated)
- [V] Wu et al. 2023, Hi-ToM. https://arxiv.org/abs/2310.16755 (c09)
- [V] Sclar et al. 2023, SymbolicToM. https://arxiv.org/abs/2306.00924 (c10)
- [V] Zhou et al. 2023, T4D and FaR. https://arxiv.org/abs/2310.03051 (c12)
- [V] Kim et al. 2025, ThoughtTracing. https://arxiv.org/abs/2502.11881 (c16, c17)
- [V] Chen et al. 2024, ToMBench. https://arxiv.org/abs/2402.15052 (c18)
- [V] Thiyagarajan et al. 2025, UniToMBench. https://arxiv.org/abs/2506.09450 (c23)
- [V] Cross et al. 2025, Hypothetical Minds. https://arxiv.org/abs/2407.07086 (c25, d09)
- [V] Gong et al. 2026. https://arxiv.org/abs/2602.10625 (d01-d03)
- [V] Bawatneh et al. 2026, OmniToM. https://arxiv.org/abs/2605.26322 (d04)
- [V] Chen et al. 2026, Dynamic Belief Graphs. https://arxiv.org/abs/2603.20170 (d05, d06)
- [V] Liang et al. 2025, LLM-Hanabi. https://arxiv.org/abs/2510.04980 (d07)
- [V] Lu et al. 2025, ToM-RL. https://arxiv.org/abs/2504.01698 (d10)

**Corrections from critique.md applied above:** GPT-4 BigToM SimToM effect is mixed in sign (+3.0 vs 0-shot, -1.2 vs CoT); the c03 "Tree-of-Thoughts 33.50" is probably SC-CoT and not cited; Llama-405B SimpleToM baseline is 58.2; a09 original sample is 20 of 31 anticipating; Strachan human N is 1,907 for the battery and 757 for perturbation; SymbolicToM gains cited as ranges only.
