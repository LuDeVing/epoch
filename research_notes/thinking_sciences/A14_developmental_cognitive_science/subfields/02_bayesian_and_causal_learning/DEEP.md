# Bayesian and causal learning: deep document

*Subfield A14.02 of developmental cognitive science. Built from evidence_a-d.jsonl (a01-a30, b01-b27, c01-c26, d01-d16), claims.jsonl (K01-K31) and critique.md in this folder. Ids like a07 are evidence lines; K05 is a claim. Many lines are the same paper entered more than once (critique.md, point 4), so counts of independent sources count papers, not lines.*

## 1. What it is

This subfield asks how children (and adults) weigh what they already believe against what they see, and how they work out what causes what from patterns of data and from their own actions.

The core idea is the "child as scientist" or "theory theory" (Gopnik and Wellman 2012, a01, b04). Children hold abstract causal theories that work like causal Bayes nets. They update them by Bayesian rules. They can tell seeing from doing, because an intervention fixes a variable and cuts the arrows into it (graph surgery).

The signature task is the blicket detector. A box lights up and plays music when certain objects ("blickets") are put on it. Children see a few trials and must say which objects are blickets, or act to make the box go or stop. Variants test screening off, backward blocking, conjunctive versus disjunctive rules, base rates, and self-chosen tests.

Why it matters for our agent. The schema state S4 TEST is where the agent chooses tests and reads results. This literature gives (a) a model of how to pick the most informative test, (b) a measured bias that LLMs share with adults (collapse to the default "any one cause" rule), (c) a measured gap in how LLMs update beliefs over rounds, and (d) LLM scaffolds (hypothesis lists, code-computed information gain, falsifying tests) with first numbers.

Honest summary of the strength of evidence. The human findings are real but narrower than the headline "preschoolers are Bayesian". The LLM findings are mostly 2025-2026 preprints from one research circle. Almost none are matched on tokens. So most scaffold ideas here are "test first", not "add now".

## 2. History and theories in depth

**Causal Bayes nets as psychology.** Gopnik, Glymour, Sobel, Schulz, Kushnir and Danks (2004, a04) proposed that children's learning matches causal graphical models: they combine conditional-probability data and interventions to infer structure, including arrow direction. Gopnik and Wellman (2012, a01) review the case: theories are abstract and causal, learning is Bayesian updating over structured hypotheses, and "intervention = graph surgery". The authors name the main drawback themselves: Bayes scores given hypotheses but does not say which hypotheses to generate.

**Founding blicket studies (second-hand).** Gopnik, Sobel, Schulz and Glymour (2001, a02): 2-, 3- and 4-year-olds see A alone work, B alone fail, A+B work, and then pick A to start or stop the box. Sobel, Tenenbaum and Gopnik (2004, a03, d01, d05): backward blocking. A alone works, then A+B works. Children rate B as less likely to be a blicket, though B was never alone. Kushnir and Gopnik (2005, a05): 4-year-olds treat a block that works 2 of 3 times as stronger than one that works 2 of 6. Schulz and Somerville (2006) and Schulz, Gopnik and Glymour (2007) extended this to hidden causes and chains. The original pass rates of Gopnik 2001, Kushnir and Gopnik 2005 and Schulz 2007 were not obtained (critique.md, gap 4).

**Priors versus evidence.** Schulz and Gopnik (2004) and Schulz, Bonawitz and Griffiths (2007, a06): children's inferences shift with domain knowledge and base rates. Griffiths, Sobel, Tenenbaum and Gopnik (2011, d02) tie adult blicket judgments to a Bayesian model with a base-rate prior. Adults fit the model very closely (r=0.97 and 0.98, N=60 and N=20). Four-year-olds (N=16) match it only in direction.

**The algorithm problem and "rational randomness".** Full Bayes needs every hypothesis scored. Bonawitz, Gopnik, Denison and Griffiths (2012, a11) proposed that children sample a few hypotheses from the posterior (a Monte Carlo view). Denison, Bonawitz, Gopnik and Griffiths (2013, a07-a10) showed probability matching in guesses. Bonawitz, Denison, Gopnik and Griffiths (2014, a12) proposed "win-stay, lose-sample": keep a hypothesis while data fit, resample with a probability tied to the likelihood of the latest datum.

**Theories and evidence together.** Bonawitz, van Schijndel, Friel and Schulz (2012, b01-b03): children with a stable belief explore more when evidence contradicts it. Children with no stable belief act as novelty seekers.

**Flexible priors that fade with age.** Lucas, Bridgers, Griffiths and Gopnik (2014, a13-a15) and Gopnik et al. (2017, a16, b05): four-year-olds accept the unusual conjunctive rule more readily than adults. The idea: young learners have a flatter prior, adults a sharper one. The cost is breadth of search; the benefit is speed in familiar worlds.

**Active learning and overhypotheses.** Kosoy et al. (2022, a18, a19): telling children the possible rule types makes their exploration far more informative. Jiang and Lucas (2024, b22, b23, d14): adults learning to learn causal forms only partly transfer them.

**Critiques.** Kloos and Sloutsky (2005, d03): blocking in preschoolers does not need causal understanding. Beaton and Benton (2024, d04): four-year-olds block only after additivity training, fitting an associative model better. Bayesian-brain critics (b25, summarising Bowers and Davis) say Bayesian models are flexible enough to fit post hoc. Denison 2013 itself (a30) weighs noisy maximising and social-pragmatic switching.

**Machines.** From 2022 the same tasks were turned on AI: Kosoy et al. 2022 (a19, c09, c10), Binz and Schulz 2023 (a20), Jin et al. 2023-24 (a21, a22), Kiciman et al. (a23). Then came the 2025-26 wave: GX-Chen (a26), Qiu (a25), Samiei (a28), Jhaveri (b20), Alderete (a27), plus related experiment-design work (Piriyakulkij c19, Hu c20, Gandhi c21).

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree; single = one source; contested = credible conflict.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Children's guesses match outcome probabilities (probability matching) | 4:1 bag, 40 children aged 4-5: 28 of 40 (70%) chose the likely colour, binomial p=.017 against chance | Denison et al. 2013 Exp 1 (a07) | contested (alternative explanations) |
| Guesses scale with the ratio | 75 children, 25 per bag. 95:5 bag: majority colour on 21/25 (84%), not different from 95%. 75:25 and 50:50 groups also tested | Denison 2013 Exp 2 (a08) | contested |
| Three-colour version | 100 children. 82:9:9: 36/50 (72%), above 33% chance, not different from 82% (p=.11). 64:18:18: 24/50 (48%), undershoots | Denison 2013 Exp 3 (a09) | contested |
| Combining two priors | 33 children. Separate-distributions: 26/38 trials (68%) chose the less numerous colour; posterior predicted 65%, frequency matching 36% | Denison 2013 Exp 4 (a10, a30) | contested |
| Noise cannot explain the matching alone | Noisy-max model needed 58% pure random responses, called implausible | Denison 2013 (a30) | contested |
| Win-stay, lose-sample fits sequential guesses | Red 5/6, green 3/6, blue 1/6 machine; aggregate guesses tracked the posterior | Bonawitz et al. 2014 (a12) | single |
| Preschoolers prefer the unusual conjunctive rule more than older people | Share calling ambiguous D a blicket, conjunctive condition: 4y 0.92, 6-7y 0.56, 9-11y 0.60, 12-14y 0.28, adults 0.25 (4y vs 6-7y P<.01; 6-7y vs 12-14y P<.05) | Gopnik 2017 (b05, a16); confirmed in PMC text | established (4y and adult data reused from Lucas 2014) |
| Original conjunctive effect | 32 children (16 per condition); 88 conjunctive and 55 disjunctive adults. Conjunctive group chose interventions including D in 20 of 25 (p=.002), multiple objects 21 of 25 (p<.001); disjunctive group 3 of 25 chose D, none multiple | Lucas 2014 Exp 1-2 (a13, a14) | established |
| Adult bias is not a wording artefact | Tulver flowers: 25 of 27 adults called F a tulver flower, none called D one; 21 of 27 would remove only F | Lucas 2014 Exp 3 (a15) | single |
| Original screening-off and backward blocking | n=16 per age cell. Screening-off B: 100% (3y), 100% (4y Exp 1), 94% (4y Exp 2). Backward blocking: 50% (3y), 88% (4y Exp 1), 63% (4y Exp 2) | Sobel 2004 as printed in the 2018 replication (d01, K25) | established |
| Replication of the above | N=90 (23, 23, 23, 21 for ages 2 to 5). 5 of 6 comparable cells matched; the 4y Exp 2 backward-blocking cell was 96% vs 63% (p=.03) | PLoS ONE 2018 (b07, d01) | contested (children split into strategies) |
| Strategy subgroups hide behind group means | Latent classes: Strategy 1 (N=51, mostly older) succeeded on nearly all trials; Strategy 2 mostly 2-year-olds | PLoS ONE 2018 (b07) | single |
| Blocking does not prove causal knowledge | Preschoolers (N=33 and N=25) blocked equally for causes and effects; adults differed, F(1,56)=6.37 | Kloos and Sloutsky 2005 (d03) | contested |
| 4-year-old blocking needs additivity training | 26 four-year-olds: condition x trial chi2(2)=8.14, p=.02; blocking in Additive chi2(1)=7.22, p=.01; 33 five-year-olds also tested | Beaton and Benton 2024 (d04) | contested |
| Diagnostic blicket inference is modest | Exp 1 N=242; blicket / butterfly percent correct: youngest 38.5/26.2, middle 41.0/38.1, oldest 55.3/59.5 (chance about 33%). Exp 2 N=103 analysed (112 enrolled): blicket by age 23.5 / 42.9 / 70.6; butterfly 29.4 / 37.1 / 58.8; pooled 46% / 42%. Only 8-10 year-olds above chance | Weisberg, Choi, Sobel 2020 (b08, critique correction 1) | single |
| Surprise raises exploration when a belief is stable | Playtime theory x evidence F(1,59)=6.02, p<.05. Magnet cited 71% vs 14% (N=28, p<.01). Only 63% of 6-7 year-olds balanced consistently; No-Theory group (n=31) preferred the novel toy, F(1,29)=9.43 | Bonawitz et al. 2012 (b01-b03) | single |
| Telling the hypothesis space makes exploration informative | N=85 aged 4-5. Data sufficient to disambiguate: 71% (hypotheses given) vs 32% (not given), p=.002 | Kosoy et al. 2022 (a18) | single |
| Learning agents fail the blicket overhypothesis task | Decision transformer reward 0.16 (random data), 2.06 (5 forced exploration steps), 2.37 (15 steps, sd 0.63); accuracy 0.67 / 0.71 / 0.77. Behaviour cloning reward 0.04-0.12 | Kosoy et al. 2022b (a19, b09, c09; critique point 3) | established |
| Adults infer conjunctive rules better when they act | Object identification: Active 0.69, Passive Observer 0.45, Passive Proposer 0.12. Rule selection 0.82 / 0.69 / 0.57. N=306 (102 per arm). Tests used 9.6 (conjunctive) vs 6.4 (disjunctive) | Samiei et al. 2026 (a28, b18, c05) | single |
| Information gain tracks accuracy | Spearman about 0.76 between information gain and final accuracy; response length correlates negatively | GX-Chen 2025 (b15), Samiei 2026 (c07) | established |
| Adults transfer rule form only partly | Exp 1 N=212 (181 after filter), Exp 2 N=250. Disjunctive transfer matched vs mismatched p=.017 to .051; no-transfer model predicts as well (.059 vs .055 mean predictive likelihood) | Jiang and Lucas 2024 (b22, d14) | single |
| Children beat LLMs at novel tool use | Novel: children 85.2%, adults 95.7%, GPT-4 75.9%, gpt-3.5-turbo 58.9%, text-davinci 8.87%. Familiar: children 88.4%, adults 84.9%, GPT-4 83.3% | Yiu, Kosoy, Gopnik 2024 (b24) | single |
| LLM agents show the adult disjunctive bias | All tested LMs worse on AND than OR, and worse at 8 objects than 4. Info-gain oracle scores 1.0 | GX-Chen 2025 (a26, b15, c01) | established |
| Bias has two causes | With oracle exploration data all LMs improved on conjunctive Q&A, but only deepseek-reasoner reached near-perfect; gpt-4o still worse on AND | GX-Chen 2025 (c02) | single |
| Hypothesis sampling removes the gap (gpt-4o) | 16, 32, 64, 96 unique hypotheses; with enough, no conjunctive/disjunctive gap at 8 objects. The prompt also names the two rule forms | GX-Chen 2025 (b16, d06, d07) | single (confounded) |
| 2026 reasoning models mostly close the gap but explore more | 6 LLMs, 24 trials per rule per model, temperature 0. gpt-5 and deepseek-reasoner near perfect on disjunctive. Tests conj vs disj: humans 9.6 vs 6.4, top human 8.5 vs 3.8, gpt-5 10.2 vs 7.7 | Samiei et al. 2026 (c08, d08) | single |
| More reasoning effort does not remove the bias | o3-mini / o4-mini at three effort levels explore worse in the conjunctive case at higher effort | GX-Chen 2025 (d06, c26) | single |
| Confirmation bias in rule discovery | 11 LLMs, success 6% to 78% in 45 turns. Falsification prompts raised discovery 42% to 56% on average. Human baseline N=29, 21 found the rule | Jhaveri et al. 2026 (b20, d09) | single |
| Falsify prompt on blicket | Qwen3-8B success 0.32 to 0.40 (I:C ratio 0.44 to 0.57); Qwen3-32B 0.57 to 0.86; 192 episodes per cell | Jhaveri 2026 (b21, d09) | single |
| Falsify prompt costs tokens | Thinking models +12-58% per turn (Qwen3-8B 1088 to 1716, Qwen3-32B 1030 to 1450) | Jhaveri 2026 (d09, K28) | single |
| Plain strong model with forms named does well | Sonnet 4.5 base 96/110 (87.3%); context graphs only 85/110 (77.3%); both 98/110 (89.1%); both vs context-graph-only Fisher p=0.015 one-tailed (post hoc); base vs both not significant | Alderete et al. 2026 (a27, d12) | single |
| LLMs do not update beliefs across rounds | 624 simulated users, 5 rounds; Bayesian assistant 81% final round; off-the-shelf LLMs roughly 36-51% and flat after round 1 (the 58% bar is the human subset, critique point 2); CoT, numeric encoding and 30 rounds all failed; fine-tuning on Bayesian predictions helped | Qiu et al. 2026 (a25, b14, c13, c14) | single |
| Verbalised belief plus external decision beats direct choice | Helps without fine-tuning but stays below fine-tuned; models were Gemini 1.5 Pro, GPT-4.1 Mini | Qiu appendix B (d10) | single |
| CausalCoT staged prompt | GPT-4 62.03 to 70.40 (+8.37) on CLadder v1.5; earlier run 63.95 to 66.64 (+2.36); anti-commonsense subset +9.65; rung 1 63.01 to 83.35, rung 2 62.82 to 67.47, rung 3 60.55 to 62.05 (rung rows from a garbled table) | Jin et al. CLadder (a22, d15) | single (gain unstable) |
| Correlation to causation fails | 207,972 samples, 18.57% positive. Best zero-shot F1 33.38 vs random 20.38; fine-tuned 94.74 F1 but drops up to 39.29 (paraphrase) and 62.30 (variable refactoring) | Jin et al. Corr2Cause (a21, c16) | single |
| Knowledge-based causal tasks go well | Pairwise direction 97% (previous best 83%), counterfactual 92%, necessary/sufficient vignettes 86%, normality 70%; unpredictable failures; data not used | Kiciman et al. (a23) | single |
| GPT-3 seeing versus doing | Passes blicket and intervention vignette, 6 of 12 vignettes correct; fails seeing/doing in causal chain | Binz and Schulz 2023 (a20, b10) | established (older model) |
| LaMDA on child tasks | Mean score (0 to 5): Social and Moral 4.33; Perception 2.91; Theory of Mind 2.86; Causal 1.34; blicket induction 0.98 and 1.06 | Kosoy et al. 2023 (c11) | single |
| Code-scored experiment choice beats LLM-chosen | Zendo, 8 test scenes, 5 seeds: human 5.26; ReAct agent 4.60; strongest 6.55 (+/-0.13); code information gain 6.55 vs LLM-chosen 4.72 vs random 5.84 | Piriyakulkij et al. 2024 (c19, d13) | single |
| Uncertainty-aware question choice | +38.1% success over direct prompting (5 datasets, 5 LLMs); +46.6% Llama3-70B; beats CoT-SC by 33.8% | Hu et al. 2024 UoT (c20) | single |
| Prior information often does not help experiment design | 6 LLMs, 5 runs; models often better with no prior after 10 experiments; cause named: strong early assumption not revised | Gandhi et al. 2025 BoxingGym (c21, d11) | single |
| Passive learning of active strategies | 70B LM with a four-shot prompt generalised to a held-out causal dimension only with explanations and/or CoT | Lampinen et al. 2023 (c15) | single |
| In-context learning as latent-concept inference | Synthetic GINC data; accuracy rises with number of examples | Xie et al. 2022 (c22) | single (theory) |

## 4. Mechanisms and models

Each model below is written so an engineer can build it.

**4.1 Causal Bayes net with interventions (the base model).**
- State: a set of hypotheses H. Each is a graph plus link strengths, or a rule like "any one blicket" or "two blickets".
- Observing x: score each h by P(data | h) times P(h). Normalise.
- Doing x (an intervention): set the variable, delete its incoming arrows, then score. Observation and action give different likelihoods. This is why "seeing vs doing" is a real test (GPT-3 failed it in chains, a20).
- Blicket example. Hypotheses: for each object subset S and rule R in {OR, AND}, "box fires iff rule R is met by blickets in S". With 4 objects the Samiei task has 32 hypotheses (c07). Each trial removes the hypotheses that disagree with the outcome (deterministic case).

**4.2 Information gain per test.** For a test t (a set of objects) and consistent hypotheses N_before, N_after is the number left after the outcome. Information gain = log2(N_before / N_after) (c07). Choose the t with the best expected value over the possible outcomes. In code: enumerate hypotheses, split them by the predicted outcome of t, compute the entropy of the split. Max-elimination is the simple form: pick the t whose worst-case remaining set is smallest.
- Measured link: higher gain per test goes with accuracy (Spearman about 0.76; b15, c07).
- Piriyakulkij (d13): when code computed this score, the agent scored 6.55 of 8; letting the LLM choose scored 4.72.

**4.3 Probability matching = sampling from the posterior.** Instead of picking argmax, draw one hypothesis in proportion to its posterior (a07, a11). Gain: diversity across attempts, cheap compute, and (in theory) near-Bayesian behaviour over many learners. Cost: any single draw is worse than argmax. Contested for humans (a30).

**4.4 Win-stay, lose-sample (a12).** Keep hypothesis h while the data fit. When a datum arrives that has low likelihood under h, resample h from the posterior with probability tied to that likelihood. One hypothesis in memory at a time. Shown to approximate Bayes. This is a cheap sequential rule an LLM loop could use: keep a current rule, test it, replace it only on a failed prediction (fits G1 "doubt only on a signal").

**4.5 Sequential Monte Carlo over language hypotheses (Piriyakulkij; c19, d13).** Particles are natural-language rules. An LLM proposes and revises them. Each particle has a weight updated by whether it explains the data (hard or fuzzy match, checked by code). The next experiment is chosen to split the weighted particles. Fuzzy weights explained R2=.57 of human accuracy by rule; hard rules R2=.10 (c19).

**4.6 Hypothesis flattening (GX-Chen; b16, d07).** Ask the model for N distinct hypotheses as Python functions. Reject duplicates. Delete any that fail past observations (exact match f(x_i)=y_i). Ask for an action that eliminates the most. Repeat. Equal weights. No sampling temperature or token counts in the appendix text read. The generation prompt names the rule forms, so listing and sampling are confounded.

**4.7 Overhypotheses (hierarchical Bayes).** A higher-level variable ("rules in this world are conjunctive") shared across tasks. Learn it from a few tasks. It sets the prior for the next one (a13, b22). In code: store the last rule form as a soft prior over forms. The cost when forms differ is mostly on disjunctive transfer (d14). A no-transfer model matched the transfer model at group level (.059 vs .055).

**4.8 Surprise-triggered exploration.** Needs a stored prediction. If observation contradicts it and the belief is stable, explore more or invoke a hidden cause (b01-b03). Without a stated prior prediction there is nothing to be surprised against.

**4.9 Bayesian teaching (Qiu; a25).** Train a model to imitate the predictions of a Bayesian assistant. Works and transfers to new domains, but needs fine-tuning, which our project does not do. A cheaper variant in the same paper: have the LLM verbalise beliefs and let an external step decide (d10). It beats direct choice but stays below fine-tuned.

**4.10 CausalCoT (a22, c17).** Four stages: extract the causal graph, classify the query type (rung), formalise the estimand, compute. Gain depends on the model version (+8.37 vs +2.36).

**4.11 Falsifying tests (Think-in-Opposites; b20, b21).** Prompt: "propose a test your current guess says should fail". Measure the incompatible-to-compatible ratio (I:C). More falsification goes with more success in LLMs (correlation positive for thinking and non-thinking models).

## 5. What holds up

**Holds up well.**
- Younger children accept unusual rules from evidence more than adults do (conjunctive 0.92 at 4y vs 0.25 adults). The same child and adult data appear in two papers, so the independent base is narrow (critique point 5).
- Screening off and backward blocking replicate in most cells (5 of 6 in N=90).
- Information gain tracks accuracy (humans and LLMs).
- LLMs on text blicket tasks lean disjunctive, like adults (GX-Chen 2025; consistent with Samiei 2026 on more models).
- Learning-only agents (RL, behaviour cloning, decision transformers) fail overhypothesis tasks without forced exploration.

**Failures, caveats, competing explanations.**
- One 4-year-old backward-blocking cell failed to replicate (96% vs 63%, p=.03; d01).
- Children split into strategy subgroups; group means hide this (b07).
- Weisberg 2020: 4- to 7-year-olds at chance on diagnostic inference; only 8- to 10-year-olds above chance (b08). The strong "preschoolers are Bayesian" reading is weaker than the review implies.
- Kloos and Sloutsky (d03) and Beaton and Benton (d04): blocking can come from associative learning; it does not need causal knowledge, and it appears in 4-year-olds only after additivity training. Kloos and Sloutsky is a lab outside the Gopnik group and found no cause/effect asymmetry in preschoolers.
- Probability matching has rivals: noisy maximising (ruled out only in its pure form), reinforcement-style matching, social-pragmatic switching (a30).
- Bayesian models are flexible enough to fit post hoc (b25, a thin secondary source).
- Surprise-driven exploration needs a stable belief (b03; only 63% of 6-7-year-olds were stable).

**Moderators.**
- Task type: choosing your own tests removes most of the adult conjunctive handicap (0.69 vs 0.45 vs 0.12; b18).
- Telling the hypothesis space: 71% vs 32% informative exploration (a18).
- Training: matched rule-form training helps disjunctive transfer (d14).
- Model class: reasoning models (gpt-5, deepseek-reasoner) nearly close the disjunctive gap and approach adult conjunctive accuracy but run 30-45% more tests (d08).
- Reasoning effort: more effort did not help and sometimes hurt conjunctive exploration (d06).
- Prior information: often did not help LLM experiment design (d11).
- Model version: CausalCoT's lift shrank from +8.37 to +2.36 across runs (a22).

**Interventions that worked.**
- Forced early exploration in decision transformers (0.16 to 2.06 and 2.37).
- Hypothesis sampling plus max-elimination (gpt-4o; confounded by naming rule forms).
- Code-scored information gain over an explicit hypothesis list (Zendo 6.55 vs 4.72).
- Falsification prompt in thinking models (Qwen3-32B blicket 0.57 to 0.86).
- Bayesian-teaching fine-tuning (Qiu).
- Verbalised beliefs plus external decision (partial).
- Context graph plus dynamic behaviours (89.1%, but not significantly above base 87.3%).

**Interventions that did not work.**
- Chain-of-thought, numeric encoding of beliefs, and 30 rounds instead of 5 for belief updating (Qiu, c14).
- More reasoning effort for the conjunctive case (d06).
- Domain context in BoxingGym (d11).
- Context graphs alone (77.3% vs base 87.3%; d12).
- Falsification prompts in non-thinking models: small or mixed (d09).

**Independence of the LLM evidence.** GX-Chen, Samiei and Jhaveri share authors. Alderete is a separate group with a different aim. A literature index check found one blicket-LLM hit in 15 results (d16). No independent reproduction was found (K30, unsupported).

## 6. Language models

**Model families tested.**
- 2022-23: GPT-3, PaLM, LaMDA, Chinchilla 70B, GPT-3.5, GPT-4.
- 2024: GPT-4 variants, Llama 3, ReAct agents.
- 2025: gpt-4o, gpt-4o-mini, deepseek-V3/R1, QwQ, Gemma3, Llama 3.x, o3-mini, o4-mini, Sonnet 4.5.
- 2026: gpt-5, gpt-5-mini, gemini-2.5-flash, deepseek-reasoner, Qwen3.

**Blicket and rule discovery.**
- 2022: GPT-3 and PaLM named the right causal structure when hypotheses were given, but picked wrong blickets; GPT-3 named too many objects (c10). LaMDA scored 0.98 and 1.06 on blicket induction (0-5 scale; c11).
- 2025: all tested LMs worse on conjunctive than disjunctive, and worse at 8 than 4 objects. An information-gain oracle scores 1.0 everywhere. LMs behave like adults, not 4-year-olds (b17, c03). Their exploration depends more on rule type than children's does.
- Oracle test: given perfect exploration data, all LMs improved, but only deepseek-reasoner was near perfect. So reading the evidence is a second weakness (c02).
- Flattening fix: sample 16 to 96 hypotheses as code, equal weight, max-elimination test. The gap closes for gpt-4o. The prompt also lists the rule forms.
- 2026: gpt-5 and deepseek-reasoner near perfect on disjunctive; gpt-5 near adult level on conjunctive; both use 30-45% more tests than needed (d08). Sonnet 4.5 with forms named: 87.3% (96/110) (d12).
- So the handicap is smaller in frontier reasoning models, but the mechanism (exploration vs reading) is still unsplit for them (K04).

**Active versus passive.** Adults do far better when acting (0.69 vs 0.45 vs 0.12). LLM agents in the same task test less efficiently and keep an adult-like bias. Seeing the outcome of your own chosen test matters (b18, c06).

**Belief updating over rounds.** Off-the-shelf LLMs flat-line after round 1 (flight task). Prompt-level fixes failed. Fine-tuning on Bayesian predictions worked. A hybrid with an external decision step helped partly. No 2025-26 reasoning model was tested (d10).

**Causal statistics and knowledge.**
- Corr2Cause: near or below random; best F1 33.38 vs random 20.38; fine-tuned models collapse on paraphrase.
- CLadder: GPT-4 about 62 overall, rungs roughly equal (63.01, 62.82, 60.55). CausalCoT 70.40, with most of the lift at rung 1 (83.35) and little at rung 2 (67.47) or rung 3 (62.05). Rung rows came from a garbled table; check the PDF before quoting.
- Kiciman: strong on knowledge-based tasks (97%, 92%, 86%), does not use the numbers.
- Reading: LLMs are good at the prior (what usually causes what) and poor at the likelihood (what these data say).

**Seeing versus doing.** GPT-3 failed in chains (a20). No 2025-26 test was found (K17, critique gap 7).

**Experiment design.**
- Piriyakulkij (2024): SMC over language hypotheses plus code information gain beat a ReAct agent on Zendo, 6.55 vs 4.60 of 8; code-chosen experiments 6.55, LLM-chosen 4.72, random 5.84.
- Hu (UoT, 2024): +38.1% success on information-seeking dialogues.
- Gandhi (BoxingGym, 2025): prior information often did not help and sometimes hurt, via an early assumption not revised.

**Confirmation bias.** 11 LLMs, success 6% to 78%, falsification prompt 42% to 56% on average; blicket Qwen3-32B 0.57 to 0.86; costs 12-58% more tokens per turn in thinking mode.

**Children's strengths.** Children invent novel tool uses at 85.2%; GPT-4 75.9%; weaker models far lower. On familiar uses GPT-4 matches children (b24).

**Training-free scaffolding as a whole.** Sparse, mostly from 2024-2026 preprints, and almost never matched on tokens. See section 8.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **S4 TEST: choose tests by information, scored in code over an explicit candidate list.** Part S4 (S2/S3 supply the list), G5. [E] Evidence: a26, b15, c07 (information gain tracks accuracy); c19, c20, d13 (code-scored or uncertainty-aware test choice beats free LLM choice). The 6.55 vs 4.72 contrast itself is single-source (K29); the class of methods has two sources (K19).
2. **Logging: record expected information gain per test** (log2 of candidates before over after). Part: schema logging section, a diagnostic for G7. [E] Evidence: K06, b15, c07.
3. **S3/S7: agreement with the default rule is a hint, not a result.** LLMs lean to the common "any one cause" reading, like adults (K03). Keep at least one non-default candidate in the list until a test removes it. Part: G (diversity of candidates). [E] on the bias (K02, K03); the exact fix is under "Test first". Evidence: a13, a14, b05, a26, b15, c03.

Nothing else in this literature is established for LLM scaffolds. Two points are noted but not added. Forced early exploration is established only for trained RL agents (K11); we do not train. "Run the test and show the model the result" (adults who only proposed tests scored 0.12 vs 0.69) is single-source (K07), and the schema already runs candidates and shows real output (G2), so it adds no step.

### Test first

| Idea | Schema part | Status | Evidence ids |
|---|---|---|---|
| List the possible rule forms before testing | S2 to S3 | [S] | a18, c09, d07, d12; K10, K27 |
| Sample N distinct hypotheses at equal weight, pick the max-elimination test | S3 + S4 | [S] | b16, d06, d07; K05 |
| One forced falsifying test per cycle | G (falsify) / S4 | [S] | b20, b21, d09; K09, K28 |
| Externalised numeric belief table updated by code, not text | G (explicit belief state) / S5 | [S] | a25, c13, c14, d10; K13 |
| Win-stay, lose-sample: keep one rule until a prediction fails | S4/S5, G1 | [S] | a12; no LLM test |
| Surprise trigger: record a prediction before each test; extra test only when it fails | S5 | [S] | b01-b03, a17; K12 |
| Store the last rule form as a soft prior that a surprise resets | memory (overhypothesis) | [S] | b22, d14; K08, K31 |
| Code (conditional-independence test) for statistical structure, LLM only for priors | S2/S3 prior, S5 | [S] | a21, a23, c16, c18; K15, K16 |
| Staged causal prompt (graph, query type, formalise, solve) | S2 | [S] | a22, d15; K14 (gain unstable) |
| State no strong prior (stated priors may anchor) | G | [S] | c21, d11; K20 |
| Posterior sampling for diverse attempts vs top-1 | G4 | [C] | a07, a30, d13; K01 |
| Seeing-versus-doing vignette check on a current model | S5 | [S] | a20, d15; K17 |
| Forced early exploration steps in an LLM loop | S4 | [S] (established only for RL) | a19, b09; K11 |

Cautions from the evidence.
- Sampling is confounded with form-listing, so do not credit sampling until the A/B separates them.
- Falsify prompts cost 12-58% more tokens; only an equal-token comparison counts (G7).
- The CausalCoT lift moved from +8.37 to +2.36; require a lift on our own model.
- Context graphs alone were worse than base in one test (77.3% vs 87.3%); a scaffold can hurt.
- G4 says samples from one model are not independent; do not treat sampled hypotheses as independent evidence.

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (prompt plus output, plus setup). The plain arm is the model with the same budget and a plain "reason, then answer" prompt. Report per-item variance, not only means (lesson of b07). Run on the current model first (K30: no independent reproduction exists).

1. **Form-listing A/B (U1).**
   - Items: text blicket game, 4 and 8 objects, OR and AND rules, 24 trials per cell.
   - Arms: plain; plain plus "the rule is one of: any one blicket, or at least two blickets"; sampling scaffold without listing forms.
   - Metric: object identification accuracy and tests used.
   - Expected effect: listing closes most of the AND gap; sampling alone closes less.
2. **Hypothesis sampling plus max-elimination (U2).**
   - Items: the same game plus two non-blicket tasks: a code bug with five suspect lines, and a diagnosis puzzle with an answer key.
   - Arms: plain; N=16 hypotheses with code elimination.
   - Metric: accuracy and tests-to-solve.
   - Expected effect: a gain on blicket if the 2025 result holds; unknown elsewhere (no non-blicket test exists, K05).
3. **Code-scored versus LLM-chosen test (U3).**
   - Items: Zendo-like rule tasks and 20-questions with a hidden object.
   - Arms: the LLM chooses from a candidate list; code ranks by information gain and the LLM only writes candidates.
   - Metric: accuracy at the same token total.
   - Expected effect: code ranking higher by a margin like Zendo's (6.55 vs 4.72 of 8); check it holds with current models.
4. **Falsify step (U4).**
   - Items: Wason 2-4-6 variants, blicket AND, debugging.
   - Arms: plain; plus "propose a test your current guess says should fail".
   - Metric: success, I:C ratio, tokens per cycle.
   - Expected effect: a gain in thinking mode, small in direct mode; the token cost is part of the comparison.
5. **Belief table (U5).**
   - Items: multi-round preference or hypothesis tracking (flight-style, 5 rounds).
   - Arms: free-text belief tracking; a code-held numeric table per hypothesis, with the LLM only judging each datum's fit.
   - Metric: final-round accuracy against a Bayesian reference (81% in Qiu).
   - Expected effect: closes part of the gap; Qiu's text prompts did not.
6. **Surprise trigger (U6).**
   - Items: blicket games with a mid-task rule change; debugging with a misleading first clue.
   - Arms: uniform extra tests; extra test only after a stated prediction fails.
   - Metric: success and tests spent.
   - Expected effect: same success with fewer tests.
7. **Rule-form memory (U7).**
   - Items: a sequence of 6 blicket tasks, form switching mid-sequence.
   - Arms: no memory; last form stored as a soft prior reset by surprise.
   - Metric: accuracy on matched and mismatched tasks.
   - Expected effect: gain on matched, loss on mismatched (d14: loss mostly on disjunctive).
8. **Stats via code (U8).**
   - Items: Corr2Cause-style and CLadder-style questions.
   - Arms: plain model; model plus a conditional-independence tool for structure questions.
   - Metric: accuracy and F1.
   - Expected effect: large on Corr2Cause (best baseline F1 33.38); small on CLadder.
9. **Seeing versus doing check (U10).**
   - Items: Waldmann-style chain and common-cause vignettes in standard and adversarial wording.
   - Arm: plain model only (diagnostic).
   - Metric: correct separation rate.
   - Expected effect: tells whether the old failure still exists.
10. **Stated-prior anchoring (U9).**
    - Items: BoxingGym-like or blicket tasks with and without a stated prior.
    - Metric: test diversity (distinct tests) and error.
    - Expected effect: fewer distinct tests with strong stated priors.

## 9. What does not transfer, and why

- **Preschooler age effects.** "Young children are more flexible" concerns a developing brain in a world of few strong priors. Our model has a fixed, adult-like prior from text. A flatter prior might be imitated with prompts, but that is untested.
- **Probability matching as a policy.** In humans it is read as a sampling approximation. For our agent, sampling lowers single-draw accuracy and helps only where diversity is rewarded (best-of-N, voting). It conflicts with G4 and G5 for single-answer problems unless code selects.
- **Blocking as proof of causal knowledge.** The evidence says blocking may be associative (d03, d04). We should not build a "causal reasoning" claim on it.
- **Fine-tuning remedies.** Bayesian teaching (Qiu) and trained decision transformers need training. Out of scope.
- **Physical interaction.** Children act on a physical machine; adults who act do better partly through seeing their own outcomes. Our S4 already runs and shows results, so only the discipline carries over.
- **Static datasets.** Corr2Cause and CLadder measure verbal causal reading in short question formats. They say little about test choice.
- **Old-model failures.** GPT-3, LaMDA and PaLM results (a20, c10, c11) may not apply in 2026.
- **Human samples.** Online adults (N=306, cells of 102) are a weak comparison group.
- **Domain size.** The blicket game has 32 hypotheses. Open-ended tasks have unbounded hypothesis spaces; the Bayes step needs a way to generate hypotheses, which the Gopnik and Wellman review itself names as the main drawback (a01).

## 10. Open questions

1. Does hypothesis sampling plus max-elimination beat plain reasoning at equal tokens on a current model, and outside blicket? (K05; no source tests it.)
2. How much of the conjunctive handicap in 2026 reasoning models is exploration, and how much is reading evidence? (K04.)
3. Does listing rule forms beat not listing? Nobody has isolated it for LLMs (K10, K27).
4. Does a forced falsifying test help at equal tokens outside Wason-style tasks? (K09, K28.)
5. Can a code-updated belief table close the Qiu gap? (K13.)
6. Does posterior sampling beat the top hypothesis in agent search outside diversity-rewarded settings? (K01.)
7. Do 2025-26 LLMs still fail seeing versus doing? (K17.)
8. Is overhypothesis transfer usable as agent memory, and what does a mismatch cost? (K08, K31.)
9. When do stated priors anchor? BoxingGym measures error, not test diversity (K20).
10. Who outside the Gopnik circle has reproduced the 2025-26 LLM blicket results? (K30.)
11. What were the original pass rates of Gopnik 2001, Kushnir and Gopnik 2005, Schulz 2007? Not obtained.
12. Does Samiei's active/passive effect come from running the test or from planning? Only one study (K07).

## 11. Sources

[V] = opened (full or substantial text) in the research passes for this folder. [M] = snippet or second-hand only. URLs as recorded in evidence_*.jsonl; some are truncated in the working listing and are given here in their canonical form.

- [V] Gopnik and Wellman (2012) Reconstructing constructivism. Psych Bull 138(6):1085-1108. https://pmc.ncbi.nlm.nih.gov/articles/PMC3422420/ (a01, b04, a29)
- [M] Gopnik, Sobel, Schulz, Glymour (2001) Causal learning mechanisms in very young children (via review) (a02)
- [M] Sobel, Tenenbaum, Gopnik (2004) Children's causal inferences from indirect evidence. https://doi.org/10.1207/s15516709cog2803_1 (a03, b26)
- [M] Gopnik et al. (2004) A theory of causal learning in children (via review) (a04)
- [M] Kushnir and Gopnik (2005); Schulz and Somerville (2006) (via review) (a05)
- [M] Schulz and Gopnik (2004); Schulz, Bonawitz, Griffiths (2007) (via chapter) https://cocosci.dreamhosters.com/Liz/BonawitzGDGChapterInPress.pdf (a06)
- [V] Denison, Bonawitz, Gopnik, Griffiths (2013) Rational variability in children's causal inferences. Cognition. https://sites.socsci.uci.edu/~lpearl/courses/readings/DenisonEtAl2013_RationalVariability.pdf (a07-a10, a30)
- [V] Bonawitz, Gopnik, Denison, Griffiths (2012) Rational randomness; Bonawitz et al. (2014) Win-stay, lose-sample. https://cocosci.dreamhosters.com/Liz/BonawitzGDGChapterInPress.pdf (a11, a12)
- [V] Lucas, Bridgers, Griffiths, Gopnik (2014) When children are better (or at least more open-minded) learners. Cognition. https://lucaslab-uoe.github.io/assets/pdf/kvaPreprint.pdf (a13-a15); [M] https://doi.org/10.1016/j.cognition.2013.12.008 (b27)
- [V] Gopnik et al. (2017) Changes in cognitive flexibility and hypothesis search across human life history. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC5544286 (a16, b05, b06); [M] https://doi.org/10.1073/pnas.1700811114 (c24)
- [M] Schulz and Bonawitz (2007); Cook, Goodman, Schulz (2011) (via review) (a17)
- [V] Kosoy et al. (2022) Learning causal overhypotheses through exploration in children and computational models. https://arxiv.org/abs/2202.10430 (a18)
- [V] Kosoy et al. (2022) Towards understanding how machines can learn causal overhypotheses. https://arxiv.org/abs/2206.08353 (a19, b09, c09, c10)
- [V] Kosoy et al. (2023) Comparing machines and children. https://arxiv.org/abs/2305.11243 (c11)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. PNAS. https://arxiv.org/abs/2206.14576 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9963545/ (a20, b10, c12)
- [V] Jin et al. (2024) Can large language models infer causation from correlation? https://arxiv.org/abs/2306.05836 (a21, b11, c16)
- [V] Jin et al. (2024) CLadder. https://arxiv.org/abs/2312.04350 (a22, b12, c17, d15)
- [V] Kiciman, Ness, Sharma, Tan (2024) Causal reasoning and large language models. https://arxiv.org/abs/2305.00050 (a23, b13, c18)
- [V] Yiu, Kosoy, Gopnik (2023/2024) Imitation versus innovation. https://arxiv.org/abs/2305.07666 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC11373165/ (a24, b24)
- [V] Qiu, Sha, Allen, Kim, Linzen, van Steenkiste (2026) Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523 (a25, b14, c13, c14, d10)
- [V] GX-Chen, Lin, Samiei, Precup, Richards, Fergus, Marino (2025) Language agents mirror human causal reasoning biases. https://arxiv.org/abs/2505.09614 (a26, b15-b17, c01-c03, c26, d06, d07)
- [V] Alderete, Benthall, Xu, Xing (2026) Separable pathways for causal reasoning. https://arxiv.org/abs/2604.20039 (a27, d12)
- [V] Samiei et al. (2026) Human adults and LLMs as scientists. https://arxiv.org/abs/2606.06464 (a28, b18, b19, c05-c08, d08)
- [V] Bonawitz, van Schijndel, Friel, Schulz (2012) Children balance theories and evidence in exploration, explanation, and learning. https://cocosci.princeton.edu/Liz/BonawitzetalBalance12.pdf (b01-b03)
- [V] Variability in 2- to 5-year-olds' causal inference behavior (PLoS ONE 2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5880367/ (b07, d01)
- [V] Weisberg, Choi, Sobel (2020) Of blickets, butterflies, and baby dinosaurs. https://pmc.ncbi.nlm.nih.gov/articles/PMC7477103/ (b08)
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to falsify. https://arxiv.org/abs/2604.02485 (b20, b21, d09)
- [V] Jiang and Lucas (2024) Actively learning to learn causal relationships. https://pmc.ncbi.nlm.nih.gov/articles/PMC13292816/ (b22, b23, d14)
- [V] Is the Bayesian brain a myth? (2025) https://pmc.ncbi.nlm.nih.gov/articles/PMC12479598/ (b25)
- [V] Lampinen et al. (2023) Passive learning of active causal strategies. https://arxiv.org/abs/2305.16183 (c15)
- [V] Piriyakulkij, Langenfeld, Le, Ellis (2024) Doing experiments and revising rules with natural language and probabilistic reasoning. https://arxiv.org/abs/2402.06025 (c19, d13)
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (c20)
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540 (c21, d11)
- [V] Xie et al. (2022) An explanation of in-context learning as implicit Bayesian inference. https://arxiv.org/abs/2111.02080 (c22)
- [V] Yiu, Allen, Ginosar, Gopnik (2025) Empowerment gain and causal model construction. https://arxiv.org/abs/2512.08230 (c23; position paper, human effect sizes not extracted)
- [V] Griffiths, Sobel, Tenenbaum, Gopnik (2011) Bayes and blickets. https://pmc.ncbi.nlm.nih.gov/articles/PMC3208735 (d02)
- [V] Kloos and Sloutsky (2005) Do preschoolers understand causality? https://escholarship.org/uc/item/8bh2f76z (d03)
- [V] Beaton and Benton (2024) Dancing on the ceiling. https://escholarship.org/uc/item/56j2v353 (d04)
- [V] Sobel and Munro (2006) When Mr. Blicket wants it, children are Bayesian. https://escholarship.org/uc/item/7fk9h80q (d05)
- [M] Schulz, Gopnik, Glymour (2007) Preschool children learn about causal structure from conditional interventions. https://doi.org/10.1037/0012-1649.43.5.1150 (c25, as cited by Samiei)
- [V] Semantic Scholar index check for "blicket detector language models" (d16) https://api.semanticscholar.org/graph/v1/paper/search

Notes on opened status. Several pages were read through a fetch tool that summarises (d01, d02, d14); table values there should be rechecked in the PDF. Figure-derived values (Samiei per-model accuracy, b19, some CLadder rows, Qiu per-model bars) are approximate and are not used as hard numbers above.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 6 established claims: 5 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A14.02-K03** (number corrected). GX-Chen et al. and Samiei et al. support the adult-like disjunctive bias, AND harder than OR, and near-perfect disjunctive accuracy for gpt-5 and deepseek-reasoner, but Samiei Table 1 shows gpt-5 using 10.2 vs 7.7 tests (conj vs disj) against average adults 9.6 vs 6.4, i.e. about 6% and 20% more, not 30-45% (the 40-44 s figure is seconds per test). Corrected claim: Frozen LLMs show the adult disjunctive bias, not the child flexible prior, on conjunctive blicket tasks; AND rules are harder than OR rules across the 8+ models tested (GX-Chen et al. 2025). In 2026 active-exploration data (Samiei et al.), gpt-5 and deepseek-reasoner reach near-perfect disjunctive accuracy and gpt-5 approaches adult conjunctive accuracy, but gpt-5 uses somewhat more tests than average adults (10.2 vs 9.6 conjunctive, 7.7 vs 6.4 disjunctive) and about 40 s per test versus about 30 s for adults.
- **A14.02-K11** (now single-source: only one opened source, code check).
