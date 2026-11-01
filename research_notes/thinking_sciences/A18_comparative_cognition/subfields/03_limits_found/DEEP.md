# Limits found: deep document

*Subfield A18.03 (comparative cognition). Built from evidence_a-d.jsonl (a01-a28, b01-b27, c01-c27, d01-d22), claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids are in brackets. [V] = page or PDF text read; [M] = snippet or abstract only. Search quota ran out early in the research, so "not found" means "not found", not "does not exist".*

## 1. What it is

This subfield is about what happens when an animal passes a test and then fails a close variant. The founding case is the trap-tube study with New Caledonian crows (Taylor, Hunt, Medina, Gray 2009). Three crows learned to push food out of a tube and avoid a trap hole. They passed tests that removed visual cues. They failed one test where the trap base stopped being a usable feature (the two-hole transfer). The authors first left open causal reasoning. Later work, including by Taylor himself (2020), reads the same data as a cheaper rule tied to the hole, not to gravity or the trap base [a01, a03, a06, c01].

The point for our work is general. One pass on one test is weak evidence of a deep rule. A pass is worth something only if the rule survives a near variant where the surface cue and the true cause come apart.

Three layers:

1. **The animal data.** The two-hole result, its low-level explanations, and the same pass-then-fail shape in rooks, finches, apes and hooded crows [a01-a05, a12, d15-d19].
2. **Method lessons.** Small samples, format effects, controls that fail on humans, and checklists for AI cognition tests [a16, a20, b26, b27, a19].
3. **The LLM mirror.** Models that pass the default form of a task and drop on a counterfactual or altered twin. Also the reverse worry: some reported drops are test artefacts [b16, b17, d01, d03, b23, b24].

Why it matters for our agent: it is a warning against over-reading transfer. Every scaffold gain we measure needs a twin test. Every limit we record needs a check that the probe was fair.

## 2. History and theories in depth

### 2.1 The trap-tube tradition

The trap-tube task comes from primate work in the 1990s (Visalberghi and Limongelli 1994; Povinelli 2000). An animal pushes food along a tube with a stick. A trap hole sits on one side. If the food goes the wrong way, it falls into the trap. The question is whether the animal understands that the food will fall (gravity and support) or has learned "avoid the hole".

Results across species stayed mixed. Capuchins and tamarins failed the trap-table version. Vervets still failed 35% of trials [a14, M, from Taylor 2009 text]. 28 dogs showed no learning in 50 trials (Muller et al. 2014, quoted in Farrar 2020) [a28].

### 2.2 The 2009 crow study

Design: one initial task, three cue-removal transfers, and one visually different transfer (the trap-table) [a24]. Pass rules were strict: 17 of 20 correct over two 10-trial blocks for the initial task (binomial alpha 0.01), and 15 of 20, or 9 of 10 in the first block, for transfers [a01, a02].

The transfers removed features step by step. Transfer 1 kept a blue rim and removed discs. Transfer 2 made discs black and removed the rim. Transfer 3 is the two-hole test, where only one hole had a trap base [c01, a02, a03].

### 2.3 Competing readings

| Reading | Claim | Support | Against |
|---|---|---|---|
| Causal reasoning (analogical) | Crows grasp that food falls and avoid the trap by inference | Pass on cue-removal transfers and the table; trap avoided on 10 of 12 first trials across transfers [a04] | Failed transfer 3; first trial did not predict later trials [a04] |
| Hole avoidance / contact rule | Crows learned "do not pull toward the hole" | Failure when the base stopped being a feature; 91.2% of trials were pulls [a01]; side-switching 22.1% vs 0% [a27] | A hole-avoidance habit was not excluded in the founding study [a05, a27] |
| Proximate cause only (Taylor 2020) | Same data, cheaper mechanism | The author changed his reading; the data did not change [critique] | Taylor 2020 lists cases where a task change flipped results, so the cheap reading is not clean either [a06] |
| Trial and error / reward learning | Success is learned from rewarded outcomes | Corvid Aesop's-fable meta-analysis [a10, d20] | A different paradigm from the trap tube |

### 2.4 Rooks, finches, apes, hooded crows

The same shape recurs. Most sources here are abstract-only.

- Rooks (Seed et al. 2006): 7 of 8 solved the initial task; all 7 transferred across a stimulus change; 6 of 7 failed the two further transfer tasks; one female solved them [d15, M]. Non-tool-using rooks (Tebbich 2007): 3 of 7 solved; 0 passed the transfer tasks [d16, M].
- Darwin's finches (Tebbich et al. 2012): 0 small tree finches and 2 non-tool-using woodpecker finches solved the initial task; none transferred [d17, M].
- Hooded crows (2013): 8 tested, 6 learned the non-trap tube; 1 of those passed the trap task on the first trial and 4 learned it by trial and error; 2 transfer tasks solved with "rather concrete rules" [d19, M].
- Chimpanzees (Seed et al. 2009): 8 of 8 learned in 40-100 trials; 1 of 8 transferred to two tasks with no shared visual cue [b06, M].
- Great apes (Martin-Ordas et al. 2008, 20 apes): platform easier than tube (F1,16 = 3.46, p = 0.04 one-tailed); 12 solved the platform, 8 the tube, 5 both, 7 platform only, 3 tube only, 5 neither; correlation between tasks r = 0.13, p = 0.57 [a12, V].

### 2.5 Format effects: the main rival to "capacity limit"

Task format changes results in both directions.

- Apes with a single tool: about 80% solved on the first trial (20 chimpanzees, 7 orangutans, 5 bonobos, 5 gorillas) [b07, M]; 20 of 24 apes avoided the trap on trial 1 with a single tool [a14, M].
- Apes prefer raking to pushing (z = 1.98, p = 0.024) [a12]. Two orangutans and one chimpanzee avoided the functional trap in the rake task but failed the push task [d18, M].
- Crows: stone dropping shows no weight preference in the innovators; breeze-based weight inference works [a07, b04].
- Looking-time tasks can show competence where action tasks fail: rooks look longer at impossible support events (F(1,80) = 8.13, 8.08, 13.64, 13.75 in four experiments, all p <= 0.006) [a23], yet rooks fail trap transfers.

### 2.6 Weight in stone dropping

Neilands et al. (2016) tested 12 crows. Only 2 invented block dropping. One innovator (D4R) dropped heavy blocks 12 times and light 22 times (p = 0.062). The other (D3B) dropped light in 18 of 24 contacts (p = 0.012) [a07, as corrected in critique]. Pre-test: light block pulled out in 128 of 240 trials (p = 0.167). Ten other birds were trained to stone-drop and then preferred heavy blocks (p < 0.001); the 125 of 140 figure is unverified [critique].

So the weight-inattention case rests on one significant bird. The signature is still useful: a bird using a rich rule would pick heavy; a bird using a cheap rule would ignore weight.

### 2.7 The Aesop's-fable line

Jelbert et al. (2014): 76.3% of drops went to water over sand (p = 0.001). High level 86.8% (p < 0.001). Sinking and solid cases about 90%. Narrow-vs-wide first drop: narrow first on 56% (p = 0.27). U-tube: 48.9% (p = 0.79), at chance [a08].

Logan et al. (2014) changed the apparatus. Three of six birds passed narrow-vs-wide with equal levels and switched to wide when its level was higher. In the U-tube only one crow (Kitty) passed the coloured version; all failed the uncovered one [a09]. So the width failure was partly an apparatus artefact, and the U-tube pass was a colour cue.

Hennefield et al. (2018) meta-analysis: 5 articles, 28 birds (rooks, Eurasian jays, NC crows), insertions per subject 1-150. Water vs sand (N = 22): after an inefficient choice OR 0.67 [0.43, 1.05], p = .08; after an efficient choice OR 5.00 [2.66, 9.38], p < .001; difference p < .001. Float vs sink: OR 2.43 after efficient. Slopes per insertion OR 1.04 (water/sand) and 1.05 (float/sink); hollow vs solid slope 1.01 (p = .67) with a large initial bias, intercept OR 57.02 [10.18, 319.33] [a10, d20]. Birds learn from rewarded choices, not from errors, with no transfer between variants.

### 2.8 Meta-research

Farrar, Boeckle and Clayton (2020) coded 116 experiments from 63 papers. Median sample 7 animals (range 1-56). Of 87 experiments with pass counts, 15 had zero passers and 25 had all pass. Median share passing 0.6; median 3 passers (max 17). Positive claims 44-59% depending on definition [a16, critique]. An N = 3 pass story is a hypothesis.

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested, P provisional, O open.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Only half the crows learned the trap tube | 3 of 6; mean 103.3 +/- 20.3 trials; criterion 17/20; cap 150 | Taylor 2009 [a01, V] | S |
| Learners pulled, almost never pushed | 91.2% +/- 2.7 pulls | [a01] | S |
| Cue-removal transfers passed | 3 of 3 crows passed transfers 1 and 2 | [a02] | S |
| Two-hole transfer failed | 3 of 3 failed; highest latency and side-switching, binomial p = 0.0156 (n = 3, chance 0.25 each) | [a03] | S |
| Trial-1 avoidance did not predict | Avoided trap on 10 of 12 first trials across transfers; Tiga and Slevin avoided on trial 1 of transfer 3 then sat at chance for 19 trials | [a03, a04] | S |
| Trap-table passed by the same 3 only | 3 solvers passed; the 3 tube failers also failed the table; 8 naive crows none above chance | [a04, a05] | S |
| Solvers pause and switch sides | Side-switching 22.1% +/- 9.0 vs 0% (U = 9, p = 0.0318) | [a27] | S |
| Pass-then-fail shape in other species | Rooks 7/8 solved, 6/7 failed far transfer; rooks 3/7 solved, 0 transferred; finches 0 transferred; chimps 8/8 learned, 1/8 transferred | [d15, d16, d17, b06] (all M) | E (pattern) |
| Two-hole item not replicated | No independent replication found | K23 | O |
| Apes: two equivalent tasks, no correlation | r = 0.13, p = 0.57; platform 12/20 vs tube 8/20 | Martin-Ordas 2008 [a12, V] | E |
| Tool constraint masks ability | About 80% first-trial success with a single tool, 37 apes | Girndt 2008 [b07, M] | E |
| Crow stone dropping ignores weight | D4R 12 heavy vs 22 light, p = 0.062; D3B light 18/24, p = 0.012; trained birds prefer heavy (p < 0.001) | Neilands 2016 [a07, b03] | C |
| Crows infer weight from wind | 35/48 (72.9%) fan on vs 23/48 (47.9%) fan off, p = 0.01; first test per bird 11/12 vs 6/12 | Jelbert 2019 [b04, V] | S |
| Kea fail the breeze task | 24/48 (50%) fan on vs 19/48 (40%) off; chi2 = 1.775, p = 0.187; 8 kea, 480 trials, 96 sessions; final drops correct 47/48 and 46/48 | Kea 2024 [a11, V] | S (failed replication of a variant) |
| Aesop's fable: water vs sand | 76.3% water, p = 0.001; U-tube 48.9%, p = 0.79 | Jelbert 2014 [a08] | E |
| Aesop's meta-analysis: reward learning | OR 5.00 after efficient vs 0.67 after inefficient; N = 22 | Hennefield 2018 [a10, d20] | E |
| Physical-cognition studies are tiny | Median 7 animals; 15/87 zero passers; 25/87 all pass | Farrar 2020 [a16] | S |
| LLMs drop on altered alphabets | Overall: humans 0.753 (1,876 samples), GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (6,840 each); comprehension checks mostly high | Lewis and Mitchell 2024 [b17, critique] | E |
| LLMs drop on counterfactual tasks | GPT-4 0-shot CoT "consistently and substantially" worse on 11 tasks; gap persists to 16-shot, gain plateaus | Wu 2024 [b16, c24] | E |
| GSM-NoOp drop | GPT-4o 94.9 -> 63.1; GPT-4o-mini 91.7 -> 54.1; Phi-3-medium 82.5 -> 29.4; Gemma2-9b 79.1 -> 22.3; o1-preview -17.5, o1-mini -29.1 | Mirzadeh 2025 [d01] | C |
| Much of that drop is ambiguity | 117 of 945 (12.4%) distractors passed audit; after audit drop 0-2 points; auditor kappa 0.32 | LessWrong post [d03], not peer-reviewed | C |
| Query-agnostic suffix attack | R1 4.50% vs 1.50% random (3x); R1-distill-Qwen-32B 8.00%; 60% of modified problems kept original meaning | CatAttack [d04, d05] | P |
| GSM-Plus twin set | GPT-4 93.25 -> 85.58 (PDR 8.23%); GPT-3.5 73.62 -> 61.19 (PDR 16.88%) | Li 2024 [d06] | E |
| Prompt scaffold keeps absolute gain, gap stays | GPT-3.5 CoT 74.17 -> 62.92; COMP+SC 80.00 -> 69.47 | GSM-Plus [d07] | P |
| Self-consistency lifts micro more than macro | GSM-IC micro 72.4 -> 88.1 (CoT+SC); macro 6.0 -> 30.0; best LTM+SC 93.4 / 45.0 | Shi 2023 [d08] | P |
| Misleading hint adoption | CodeCrash -23.2% direct, -13.8% with CoT; reasoning models use 2-3x tokens on a plausible wrong hint | Lam 2025 [d13] | P |
| Multi-turn drop | 15 LLMs, 200,000+ conversations, average -39%; aptitude -15%, unreliability +112% | Laban 2025 [d11] | P |
| Self-correction blind spot | 64.5% average (14 open non-reasoning models); "Wait" cuts it 89.3% | Tsui 2026 [d12] | P |
| Physical-world VLMs far below humans | WM-ABench best transitive navigation 43.8% vs human 90.0%; collision 40.2% vs 84.0%; manipulation 51.3% vs 88.0% | Gao 2025 [c12] | E |
| Fine-tuning does not transfer | GRPO in-task 0.943, SFT 0.969; real towers GRPO 0.6/0.57/0.52/0.31 across four training conditions | Schulze Buschoff 2026 [c10] | S |
| Right answer, wrong chain | TRIP accuracy up to 78.3%; verifiability up to 11% | Storks 2021 [c14] | E |
| Embodied LLM tests near floor | 12 trials per level; 59 children; LLMs matched competition agents only on levels 3, 8, 9, 10 at very low rates | Mecattaf 2024 [a18, d21] | E |
| Causal benchmarks split | CRASS 87.95% (3.5) / 92.44% (GPT-4); pairwise 97%; post-cutoff 80.3% / 98.5%; Corr2Cause best 33.38% F1 | Kiciman 2023, Jin 2024 [c20, c21, c19] | C |
| Unconventional tool use | LLMs 35-42% vs humans 65.1%; GPT-4 errors 42.4% wrong tool use | MacGyver [c25] | S |
| CoT collapses out of distribution (controlled setting) | ID exact match 100%; partly OOD 0.00%; fully OOD 0.00% | Zhao 2026 [d09] | S |

## 4. Mechanisms and models

Each mechanism is described so an engineer can build it. The animal results give the test shape. The LLM results give the measurement method.

### 4.1 The twin test (core mechanism)

Goal: separate a deep rule from a surface cue.

1. Take a test the agent passes. Call it the seed.
2. Name the surface cue the agent could be using (the hole, the colour, the famous wording, the default alphabet).
3. Build a near-structure twin where the cue and the true cause split. In the crow study the twin kept the hole but removed the trap base as a usable feature.
4. Build a far-surface twin that changes the look but keeps the structure (the trap-table).
5. Require pass on both. The crows passed the far twin and failed the near-structure twin, so a far pass alone proved little [K02].
6. Add a rule-comprehension control: ask the agent to restate the new rule or apply it to a trivial case. In the LLM studies comprehension checks mostly passed, so the drop was not a failure to read [b16, b17]. Hodel and West found comprehension reaching "at least 30%" on some alphabets, so the control is not always clean [b18].
7. Audit the twin: two independent checkers confirm the correct answer is unchanged. The 2026 audit kept only 12.4% of generated distractors [d03]. Without this step a "drop" may be a changed question.

Scoring: report seed score, twin score, the gap, and macro accuracy (all twins of one seed right) [d08].

### 4.2 Error-signature test

A cheap rule and a rich rule often give the same final answer but differ on one signature. Crow example: a rich weight rule chooses heavy; a cheap rule ignores weight [a07]. For a code agent the signature should be countable by running code.

- Plant a wrong claim next to the code (a comment or print message). Run the program. Count answers equal to the planted claim and not equal to the executed output (CodeCrash method) [d13].
- Count outputs that apply an operation to a quantity the problem marks as irrelevant (GSM-NoOp style) [d01, d02].
- Compare planted-claim adoption with the rate of other wrong answers. No paper reports this ratio; the signature is proposed, not validated [K24].

### 4.3 Learning-from-success log

Hennefield's method: for each attempt, record whether the choice was efficient. Fit the odds of choosing efficiently next time as a function of the previous outcome [d20]. Learning from success only gives OR well above 1 after success and OR near or below 1 after failure.

Implementation: a log table `(attempt, strategy, outcome, next_strategy)`; a logistic regression of `next == efficient` on `prev_efficient`; run per problem class. No LLM retry-loop study applies this [K28]. Chimpanzees and young children also gained little from watching errors (5-6 year-olds mastered the task with no benefit; Horner and Whiten 2007) [b09, d22, both M].

### 4.4 Format ladder

Before logging "the agent cannot do X":

1. Rerun with different wording.
2. Rerun with a different output budget.
3. Rerun with a tool or code interface.
4. Rerun on a recognition form and on a generation form.

Log all runs. Apes pushed badly and raked well [a12, d18]. Mecattaf's LLMs may have hit the action-script interface and the 30-script cap, not a reasoning limit [d21]. Hanoi collapse at large N was tied to output limits, and a generating-function request fixed it in preliminary tests [b24]. Gate: record a limit only if it holds in at least two formats.

### 4.5 Control validation

Run each control on a known good reasoner first. The inverted-tube control fails on humans too (Silva et al. 2005) [a15, M]. The hidden-agent crow result was disputed for unbalanced controls [b14, b15, M]. Implementation: run the control on an oracle (a human, a program, or a model given the answer). If the oracle fails, the control is broken.

### 4.6 Check the chain, not the answer

TRIP: accuracy reached 78.3% but only up to 11% of items had correct physical states plus the conflict identified [c14]. Implementation: the agent emits intermediate claims in a structured field; code checks each against ground truth or execution. A large gap between end accuracy and chain validity signals a surface rule.

### 4.7 Test-first (run an intervention before answering)

Samiei 2026 let six LLMs run experiments on blicket-like rules. Conjunctive rules stayed harder than disjunctive; gpt-5 and deepseek-reasoner were near-perfect on disjunctive [c17, d14]. There was no passive LLM arm, so the benefit of testing is unmeasured [K26]. Lampinen 2023 found passively learned strategies transfer only when explanations are present [c18].

## 5. What holds up

### 5.1 Replications and near-replications

- Pass-then-fail transfer in trap tubes: shown in rooks, finches, chimps and hooded crows. All abstract-only here. The pattern is established; the two-hole item has no independent replication [K23].
- Breeze weight inference in kea failed (50% vs 40%, p = 0.187) where crows passed [a11, b04]. Whether this is capacity or task design is open.
- Aesop's fable: the narrow-vs-wide failure was reversed by changing the apparatus [a09]; the U-tube pass was a colour cue.
- Apes: a second equivalent task did not predict success on the first (r = 0.13) [a12].
- Magpies passed water/sand, heavy/light, solid/hollow; failed diameter, water level, U-tube [b12, M].
- Hornbills in string pulling: 5 of 6 solved both versions on first encounter (mean 18.13 s and 17.78 s) [a21]. This speaks to format and species spread, not transfer.

### 5.2 Failed or contradictory results

- Crows fail weight in stone dropping but infer weight in the breeze task [K04].
- Taylor 2009 read crows as analogical reasoners; Taylor 2020 reads them as proximate-cause only [a06, critique].
- Kiciman 2023 shows strong text causal scores; Zecevic 2023 and Jin 2024 show near-random performance on new structures [c19-c22]. Retrieval of famous vignettes is a rival explanation.
- Illusion of Thinking reports collapse at high complexity [b23]; Lawsen reports an output-limit artefact [b24]. Lawsen's rebuttal is preliminary and AI-co-authored.
- GSM-NoOp drops of 17.5 and 29.1 points for o1 [d01] against a 2026 audit with 0-2 point drops after filtering [d03]. The audit is a blog post and its auditors agreed at kappa 0.32. Contested.

### 5.3 Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Pull vs push, rake vs push | Easier when the action is natural | [a12, d18] |
| Single tool vs two tools | About 80% first-trial success with a single tool | [b07] |
| Looking time vs action | Competence in looking, failure in action | [a23] |
| Prior tube experience | Only learners passed the table | [a04, a05] |
| Harder counterfactual world | Drops may reflect harder worlds, not missing generality (Wu 2024 say so) | [b16] |
| Number of clauses | Accuracy falls and variance rises as clauses grow | [b22] |
| Model generation | Drop shrinks with stronger models but does not vanish: GPT-4 PDR 8.23% vs GPT-3.5 16.88% | [d06] |
| Interface | Action-script cap; images vs text | [d21] |
| Training | Fine-tuning raises in-task accuracy, not transfer | [c09, c10] |

### 5.4 Interventions that worked

- Single-tool design raised ape success [b07]; removing the tool constraint raised chimp success [b06].
- A step-wise feasibility self-check helped GPT-4 on unconventional tool use, not Llama 2 [c25].
- Appending "Wait" cut the self-correction blind spot by 89.3% (non-reasoning models, injected errors) [d12].
- Asking for a generating function instead of every move rescued Hanoi at large N (preliminary) [b24].
- Compositional prompting on the GSM-Plus critical-thinking subset: CoT 40.83 vs COMP 54.17 (GPT-3.5) [d07].
- Self-consistency raised GSM-IC micro accuracy to 88.1-93.4% [d08].

### 5.5 Interventions that did not work

- Few-shot CoT on Corr2Cause did not change the near-random picture [c19].
- More shots on counterfactual tasks: the gap shrinks and plateaus by 16 shots [b16, c24].
- Math fine-tuning did not cut GSM-Plus drop rate (MetaMath-Mistral-7B PDR 33.86%) [d06].
- An in-context expert example in Animal-AI gave no notable change [a18, c05].
- CoT and expert-example prompting did not rescue VLMs on physics [c11, c12].
- Temperature 0 did not restore reliability in multi-turn tasks [d11].
- Task-specific RL did not transfer to related tasks or styles [c09, c10].
- Scaffolds on twins kept the absolute lead but the seed-twin gap barely moved (10.53 vs 11.25 points) [d07].

## 6. Language models

### 6.1 Counterfactual and altered-rule twins

- **Counterfactual tasks (Wu et al. 2024).** Eleven tasks with altered default assumptions (for example number bases). GPT-4 0-shot CoT is above chance but "consistently and substantially" below default. The gap shrinks with up to 16-shot CoT for bases 9, 11 and 16, then plateaus. Comprehension checks mostly passed [b16, c24].
- **Letter-string analogies (Lewis and Mitchell 2024).** Humans 0.753 vs GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 on altered forms. Row order Humans, GPT-3, GPT-3.5, GPT-4 follows b17; GPT-3.5 below GPT-3 is as printed [b17, critique]. Hodel and West: GPT-3 generative accuracy below 0.1 on four synthetic-alphabet tasks; only remove-redundant and sort stayed in range [b18]. Webb et al. (2023) had claimed GPT-3 matched or surpassed humans on default forms [b19, M].
- **Animal-style principles (Rane et al. 2025).** GPT-4o accuracy: A vs C 1.00, B vs D 1.00, ranked animals 0.97, random strings 0.92, reverse-ranked animals 0.78, n-term trial-based 0.40 (SD 0.50, about chance). After 60 training trials on adjacent pairs, novel non-adjacent pairs were at chance in that format [a19].
- **Abstraction (ConceptARC).** Humans 91%, best Kaggle program 52%, GPT-4 25% zero-shot; with a detailed one-shot prompt GPT-4 0.33. On 48 minimal tasks humans 0.95, GPT-4 0.69 and 0.65 [b20].
- **Theory of mind.** Under Ullman's alterations model outputs became inconsistent [b21]. Shapira: Adv-CSFB "other person" accuracy fell from 93.8% (davinci-002) to 68.8% (GPT-4); "inon" from 71.4% to 0%; probing method shifted GPT-4 SocialIQa by 7 points [c27].

### 6.2 Math twins: how much of the drop is real

| Study | Model | Seed -> twin | Drop |
|---|---|---|---|
| GSM-Symbolic NoOp [d01] | GPT-4o | 94.9 -> 63.1 | -31.8 |
| | GPT-4o-mini | 91.7 -> 54.1 | -37.6 |
| | Phi-3-medium | 82.5 -> 29.4 | -53.1 |
| | Gemma2-9b-it | 79.1 -> 22.3 | -56.8 |
| | o1-preview | not recorded | -17.5 |
| | o1-mini | not recorded | -29.1 |
| GSM-Plus [d06] | GPT-4 | 93.25 -> 85.58 | PDR 8.23% |
| | GPT-3.5-Turbo | 73.62 -> 61.19 | PDR 16.88% |

The point drops for the first four rows are computed from the printed pairs. The GSM-Symbolic paper also reports up to 65% drop from one added clause [b22].

The 2026 audit [d03] checked 945 generated distractors and kept 117 (12.4%). Claude Opus and GPT-5.5 as auditors agreed at kappa 0.32 and kept 12% and 36%. After audit, drops were 0-2 points (exact per-model values only in charts). CatAttack found that only 60% of its modified problems kept the original meaning, and about 80% of those showed a real wrong answer [d05]. Lesson: report drops on audited twins only.

CatAttack numbers: R1 combined attack success 4.50% vs 1.50% for random suffixes (3x); R1-distill-Qwen-32B 8.00% (2.83x), on 225 problems with 6 runs. A proxy attack on DeepSeek V3 reached 35% and transferred to R1 at about 20% (114 prompts). Slowdown (response at least 1.5x / 2x / 4x longer): o1 26.4 / 9.9 / 1.3% [d04, d05].

### 6.3 Do scaffolds help on twins?

Partly answered, with old models. GPT-3.5 on GSM-Plus, seed -> twin: CoT 74.17 -> 62.92; Least-to-most 74.17 -> 62.60; COMP 76.67 -> 65.52; CoT+SC 76.67 -> 66.88; COMP+SC 80.00 -> 69.47. Gaps: 10.53 for COMP+SC vs 11.25 for CoT. The scaffold keeps its absolute lead but does not shrink the gap [d07]. On the critical-thinking subset, CoT+SC is 40.00 vs COMP+SC 55.83 [d07]. In GSM-IC, LTM+SC reached macro 45.0 against CoT 6.0; the correct answer was present in the 20 samples for 99.7% of problems, so selection is the weak link [d08]. No source tests a scaffold at equal tokens on its own counterfactual twin [critique, gap 1].

### 6.4 Code and multi-turn

- CodeCrash: 1,279 questions, 17 LLMs plus o3-mini, DeepSeek-R1, QwQ-32B. Output prediction direct -23.2%, with CoT -13.8%. Reasoning models lose little under structure changes but a plausible wrong hint triggers 2-3x tokens [d13].
- Laban: 15 LLMs, 200,000+ simulated conversations, 6 tasks. Average -39% (top models about -35%); aptitude -15%, unreliability +112%. Temperature 0 did not help. Recap and snowball turns recovered only part [d11].
- Tsui: 14 open non-reasoning models; blind spot 64.5% (62.8% on logic and object tracking); 41.4% for Sonnet 4 and 52.5% for Haiku. Natural own errors caught when shown externally: 4.3-10.8%. "Wait" lowers the blind spot 89.3% [d12].

### 6.5 Physical and causal worlds

- Tower stability: humans 65.6% correct; GPT-4V OR 2.597, p = 0.028; Claude-3 OR 2.016, p = 0.078. Human-human regression coefficient 1.46 (R2 0.354) vs GPT-4V-human 1.15 (R2 0.066). Michotte causal perception: human-human 0.85 (R2 0.556); Claude-3 -0.22 (95% CI -0.39 to -0.06) [c07, c08].
- Fine-tuned 11B VLMs reach 0.6-0.92 on trained block sizes; humans 0.72; below chance on some Cubeworld sizes [c09]. Qwen3-VL-8B in-task GRPO 0.943, SFT 0.969; real tower images GRPO 0.6/0.57/0.52/0.31, SFT 0.59/0.53/0.55/0.57 across four training conditions [c10].
- Probing: Gemini 2.0 Flash Thinking 53.7% on GRASP; Qwen 2.5 VL 72B 99.7% on basic visual understanding; probe accuracy up to 85%. The vision encoder holds plausibility information the language model fails to use [c11].
- WM-ABench: best prediction average 47.5%; frontier models reach 92-100% on static size comparison [c12]. V-JEPA: 98% IntPhys, 66% GRASP, 62% InfLevel-lab [c13].
- Text causal benchmarks: CRASS 87.95% and 92.44%, pairwise 97%, post-cutoff 80.3% and 98.5% [c20, c21]. Corr2Cause (207,972 samples, 18.57% positive): best BART MNLI 33.38% F1; fine-tuned models fell up to 39.29 F1 under paraphrase and 62.30 F1 under variable refactoring [c19]. Binz and Schulz: 12 of 12 vignettes correct or human-like, 6 of 12 correct; GPT-3 did not reduce its prediction after the intervention B = 0 [c15]. Kosoy 2022 tested GPT-3 and PaLM on causal overhypotheses; exact figures not recorded [c16].

### 6.6 Animal-AI and RL agents

Odds of passing vs a random agent: children 47x, competition winners 19x, Dreamer-v3 6x; PPO not above chance [c06]. Mecattaf's LLM floor effect is partly interface [d21]. The a17 figures (52 children, medians 0.63 vs 0.35) are unverified and not used.

### 6.7 What changed it, by how much

| Change | Effect | Source |
|---|---|---|
| Stronger model (GPT-3.5 to GPT-4) | GSM-Plus drop rate 16.88% to 8.23% | [d06] |
| Reasoning model vs non-reasoning | NoOp drop -17.5 (o1-preview) vs -40.0 (GPT-4o-mini) | [d01] |
| Self-consistency | Micro +15.7 (72.4 to 88.1); macro +24 (6.0 to 30.0) | [d08] |
| Compositional prompt | Critical-thinking subset +13.3 vs CoT | [d07] |
| "Wait" token | Blind spot -89.3% | [d12] |
| 16-shot CoT | Gap shrinks, then plateaus | [b16] |
| Audit of twins | Reported drop from tens of points to 0-2 | [d03] |
| Fine-tuning | In-task up, transfer flat | [c09, c10] |

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested, [P] provisional, [O] open. Schema parts from SCHEMA.md: G guardrails, S states, O operators, memory. Test-first maps to S4 TEST, since O3 is Decompose.

### Add now (established)

1. **Twin gate for every pass (G3, strengthen).** A scaffold gain counts only if it holds on a near-structure twin and a far-surface twin. One far pass is not enough. [E] K02, K08; a04, a05, d15-d19, b16, b17.
2. **Rerun a failed probe in a second format before logging a limit (G3).** At least one differently built format (wording, budget, tool). Log both. [E] K03, K06, K11; a06, a12, b07, d18, d21.
3. **Check the interface before blaming reasoning (G3).** Log whether each failure is perception, control or reasoning. [E] K11; a18, c04, d21.
4. **Pair twins with a rule-comprehension control (G3).** Comprehension passes and the twin fails: the rule did not transfer. Comprehension fails: the twin is not a test. [E] K08; b16, b17, b18.
5. **Grade chains, not just answers (G10).** Check intermediate claims in code. [E] K12; c14, c11.
6. **Many items and several seeds per probe; report per-item pass counts (G7, G3).** An N = 3 pass is a hypothesis. [S for the numbers, method is sound] K07; a16, a28.
7. **For physical-world questions give a tool or simulator (G12).** Prompting alone did not rescue models. [E] K10; c07, c08, c11, c12, c13.
8. **Methods checklist as an audit gate (G3).** Avoid over- and under-claiming, test alternative strategies, strip cues. [E] K20; a20, b26, b27, a19.
9. **Validate controls on a known good reasoner (G3).** [C] K18; a15, b14, b15. Cheap, so adopt as a gate even though the evidence is contested.
10. **Report drops only on audited twins (G3).** [C] K21; d03, d05. Adopt the audit step because it is cheap and the alternative is recording noise.
11. **Check output budget, solvability and scorer before recording a limit curve (G12).** [C] K13; b23, b24.

### Test first

12. **Error-signature counter (G3, S4).** Plant a wrong claim; count adoption by running code. [P] K24; d02, d13.
13. **Forced recheck turn after the first answer (S4).** A cheap "Wait"-style gate. [P] K25; d11, d12. Evidence is non-reasoning models with injected errors.
14. **Test-first vs answer-first on conjunctive rules (S4).** [O] K26; d14, c17, c18.
15. **Learning-from-success log in retry loops (S8, memory).** Odds of repeating the efficient choice by previous outcome. [O] K28; d20, d22.
16. **Step-wise feasibility check per tool step (S4).** Helped GPT-4, not Llama 2. [S] K16; c25.
17. **Scaffold vs plain on audited twins at equal tokens (G7).** [P] K22; d07, d08.
18. **Tool API vs free text for causal tasks (G3).** [O] K27; d21.
19. **Generating program instead of full enumeration for long outputs (G12).** [C] K13; b24.
20. **Memory lessons need a twin check before they become rules (memory, S9).** A lesson from one class may not carry to a near class. Inference from K09; c09, c10. [S]

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (output plus reasoning), same seeds, at least 5 seeds per item, items with a code-checkable answer. Report means with intervals over seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style and BRAINTEASER items with a mutated twin (relabelled colours, swapped alphabet, reversed order), audited by two checkers | Plain vs scaffold | Seed score, twin score, gap, macro accuracy | Scaffold keeps its absolute lead; gap shrinks by under 3 points (baseline gap about 10-11 from d07) |
| T2 | Same items with an added distractor clause (audited, answer unchanged) | Plain vs scaffold with S1 input hygiene | Drop on audited twins | Small drop (0-5 points) once audited; a larger drop is scaffold-specific |
| T3 | Code-output items with a planted wrong comment or print | Plain vs scaffold with S4 execute-and-compare | Share of answers equal to the planted claim | Plain arm adopts at CodeCrash-like rates (accuracy -14 to -23%); execution arm near 0 |
| T4 | Any item with a first answer | Single pass vs single pass plus forced recheck turn | Fix rate on matched own-vs-other injected errors | Blind spot cut (Tsui -89.3% on non-reasoning models); smaller on reasoning models |
| T5 | Conjunctive-rule blicket-style items | Answer-first vs test-first with a code-counted test budget | Exact rule and objects correct | Test-first better on conjunctive items; size unknown |
| T6 | Retry loops on one problem class | Log only vs log plus show failed attempt with reason | Odds of repeating the correct strategy after success vs after failure | OR after success above 1, after failure near 1 or below; showing the reason moves the failure OR up |
| T7 | Physical or spatial questions | Prompt only vs code simulator tool | Accuracy | Tool arm clearly above prompt-only |
| T8 | Same task in two interfaces (free text vs tool API) | Same model, same budget | Pass rate by interface | Interface effect measured; over 10 points means the "limit" is the interface |
| T9 | Comprehension probe per twin | Restate rule, then apply | Comprehension rate vs twin accuracy | Comprehension over 90% with lower twin accuracy means the rule did not transfer |
| T10 | Items with an irrelevant quantity | Plain vs scaffold | Count of irrelevant-quantity uses | Rich-rule arm lower; mirrors the weight-inattention signature |
| T11 | Long-output items (enumerate vs generate a program) | Full enumeration vs generating program | Accuracy at large N | Program arm avoids output-limit collapse |
| T12 | Memory lesson transfer | Lesson from class A applied to near class B vs no lesson | Pass rate on B | Flat or negative if lessons are surface-tied |

## 9. What does not transfer, and why

- **The two-hole item itself.** It tests a physical rule with visible geometry. Our items are symbolic. Take the test shape (pass, then split cue from cause), not the apparatus.
- **Crow sample sizes and criteria.** 3 birds, 17 of 20 criterion. We can run hundreds of items and seeds. Use their discipline, not their numbers.
- **Trial counts for learning.** Crows needed about 103 trials. LLMs learn in context in a few shots or not at all. The reward-learning odds ratio is a measurement method, not a prediction [d20].
- **Inhibition.** The crows had to stop pulling. LLMs have no motor habit. The nearest analogue is premature commit and non-recovery [d11, d12]. That is an analogy, not the same thing.
- **Looking time vs action.** Passive tests worked for rooks [a23]. The only LLM map is recognition vs generation, which is weak [K17].
- **Species comparisons.** Kea failing the breeze task (p = 0.187) says nothing about our model. It warns us to run one capacity probe on several models and not generalise from one [K19].
- **Old-model LLM drops.** GPT-3 and GPT-4 twin drops may not carry to current reasoning models [critique]. Only the audit method transfers.
- **Fine-tuning findings.** We do not train. Use them only as a warning that a prompt tuned on one probe family may not carry [K09].
- **Embodied agent scores.** LLMs in Animal-AI were limited by the action-script interface [d21]. Do not cite them as reasoning limits.

## 10. Open questions

1. Does a scaffolded agent keep its gain on a counterfactual twin of each test at equal tokens? No source tests this directly.
2. Do 2025-2026 reasoning models still drop on altered-alphabet and counterfactual twins? No run found; d10 is still GPT-3/4.
3. How much of any drop is a lost rule and how much is a changed question? The audit suggests much is ambiguity, but the audit is a blog post.
4. Which error signature separates a shallow rule from a mechanism in an LLM code or physics task, and at what rate? Hint-adoption rate is not reported.
5. Has anyone outside Taylor's lab replicated the two-hole transfer with crows? Not found.
6. Does test-first beat answer-first at equal tokens on conjunctive rules in strong models?
7. Would a tool API lift LLM causal-level scores in Animal-AI? Exact per-level numbers are only in figures.
8. Do LLM retry loops show learning only from success?
9. Do inhibition-type failures have a code gate? "Wait" works on injected errors only.
10. Is the corvid reward-learning result partly an artefact of small N and few insertions? Hennefield's cut-off median was 63 insertions.
11. Why is GPT-3.5 below GPT-3 on altered alphabets (0.350 vs 0.488)? The table is "as printed".
12. Why do crows ignore weight in stone dropping but use it in the breeze task: format, species, or inference style?

## 11. Sources

[V] = opened and read. [M] = snippet or abstract only. Duplicates counted once; evidence ids in brackets.

### Animal studies

- [V] Taylor, Hunt, Medina, Gray (2009) Do New Caledonian crows solve physical problems through causal reasoning? https://pmc.ncbi.nlm.nih.gov/articles/PMC2674354/ (a01-a04, a24, a27, b01)
- [V] Taylor, Hunt, Medina, Gray (2009) Causal reasoning in New Caledonian crows: ruling out spatial analogies and sampling error. https://pmc.ncbi.nlm.nih.gov/articles/PMC2734031/ (a05)
- [V] Taylor (2020) Folk physics for crows? Animal Behavior and Cognition 7(3):452-456. https://www.animalbehaviorandcognition.org/ (a06, a25, a26, b02, c01-c03)
- [V] Neilands, Jelbert, Breen, Schiestl, Taylor (2016) How insightful is insight? https://pmc.ncbi.nlm.nih.gov/articles/PMC5156351/ (a07, b03)
- [V] Jelbert, Taylor, Cheke, Clayton, Gray (2014) Using the Aesop's fable paradigm. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3966847/ (a08)
- [V] Logan, Jelbert, Breen, Gray, Taylor (2014) Modifications to the Aesop's Fable paradigm. https://pmc.ncbi.nlm.nih.gov/articles/PMC4108369/ (a09)
- [V] Hennefield, Hwang, Weston, Povinelli (2018) Meta-analytic techniques reveal that corvid causal reasoning in the Aesop's Fable paradigm is driven by trial-and-error learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC6181768/ (a10, b11, d20; counted once)
- [V] Kea weight-inference study (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11537761/ (a11)
- [V] Jelbert et al. (2019) NC crows infer the weight of objects from observing their movements in a breeze. https://pmc.ncbi.nlm.nih.gov/articles/PMC6367178 (b04)
- [V] Martin-Ordas, Call, Colmenares (2008) Tubes, tables and traps. https://pmc.ncbi.nlm.nih.gov/articles/PMC2757606/ (a12, b08)
- [V] Farrar, Boeckle, Clayton (2020) Trialling meta-research in comparative cognition. https://www.animalbehaviorandcognition.org/ (a16, a28)
- [V] Oriental pied hornbill string-pulling (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12364582/ (a21)
- [V] NC crows learn functional properties of novel tool types (PLoS One). https://pmc.ncbi.nlm.nih.gov/articles/PMC3237408/ (a22)
- [V] Rooks perceive support relations (Proc R Soc B). https://pmc.ncbi.nlm.nih.gov/articles/PMC2842627/ (a23)
- [M] Seed, Tebbich, Emery, Clayton (2006) Investigating physical cognition in rooks. https://doi.org/10.1016/j.cub.2006.02.066 (a13, d15)
- [M] Tebbich, Seed, Emery, Clayton (2007) Non-tool-using rooks solve the trap-tube problem. https://doi.org/10.1007/s10071-006-0061-4 (b05, d16)
- [M] Tebbich et al. (2012) Darwin's finches physical cognition. https://doi.org/10.1007/s10071-011-0390-9 (d17)
- [M] Seed, Call, Emery, Clayton (2009) Chimpanzees solve the trap problem when the confound of tool-use is removed. https://doi.org/10.1037/a0012925 (b06)
- [M] Girndt, Meier, Call (2008) Task constraints mask great apes' ability. https://doi.org/10.1037/0097-7403.34.1.54 (b07)
- [M] Mulcahy and Call (2006) Modified trap-tube. https://doi.org/10.1007/s10071-006-0019-6 (d18)
- [M] Hooded crows trap tube (2013, Russian). https://europepmc.org/search?query=hooded%20crows%20trap%20tube (d19)
- [M] Horner and Whiten (2007) Learning from others' mistakes. https://doi.org/10.1037/0735-7036.121.1.12 (b09, d22)
- [M] Penn, Holyoak, Povinelli (2008) Darwin's mistake. https://doi.org/10.1017/s0140525x08003543 (b10)
- [M] Zhang et al. (2021) Azure-winged magpies in Aesop's fable. https://pmc.ncbi.nlm.nih.gov/articles/PMC7804021 (b12)
- [M] Gruber et al. (2019) NC crows use mental representations to plan metatool use. https://pmc.ncbi.nlm.nih.gov/articles/PMC6384166 (b13)
- [M] Taylor, Miller, Gray (2012) Hidden causal agents. https://doi.org/10.1073/pnas.1208724109 (b14)
- [M] Boogert et al. (2013) Do crows reason about causes or agents? https://doi.org/10.1073/pnas.1219664110 (b15)
- [M] Silva, Page, Silva (2005) Methodological-conceptual problems. https://doi.org/10.3758/BF03196050 (a15)
- [M] Visalberghi and Limongelli (1994), Povinelli (2000), Mulcahy and Call (2006), Girndt (2008), as reported in Taylor 2009. https://pmc.ncbi.nlm.nih.gov/articles/PMC2674354/ (a14)
- [M] Voudouris et al. (2022) Direct comparison of children and AI agents on causal tasks. https://www.frontiersin.org/ (a17; figures unverified, not used)

### LLM and AI studies

- [V] Mecattaf et al. (2024) A little less conversation, a little more action, please. https://arxiv.org/abs/2410.23242 (a18, c04, c05, d21)
- [V] Rane et al. (2025) Principles of animal cognition to improve LLM evaluations. https://proceedings.mlr.press/v267/rane25a.html (a19)
- [V] Voudouris, Cheke, Schulz (2025) Bringing comparative cognition to computers. https://arxiv.org/abs/2503.02882 (a20)
- [V] Voudouris et al. (2023) The Animal-AI Environment. https://arxiv.org/abs/2312.11414 (c06)
- [V] Wu et al. (2024) Reasoning or reciting? https://arxiv.org/abs/2307.02477 (b16, c24)
- [V] Lewis and Mitchell (2024) Counterfactual tasks and analogical reasoning. https://arxiv.org/abs/2402.08955 (b17); https://arxiv.org/abs/2411.14215 (d10)
- [V] Hodel and West (2024) Response: Emergent analogical reasoning. https://arxiv.org/abs/2308.16118 (b18)
- [M] Webb, Holyoak, Lu (2023) Emergent analogical reasoning. https://arxiv.org/abs/2212.09196 (b19)
- [V] Mitchell, Palmarini, Moskvichev (2023) Humans, GPT-4 and GPT-4V on abstraction. https://arxiv.org/abs/2311.09247 (b20)
- [V] Ullman (2023) LLMs fail on trivial alterations to theory-of-mind tasks. https://arxiv.org/abs/2302.08399 (b21; c26 is an [M] duplicate)
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229 (b22, d01, d02)
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941 (b23)
- [V] Lawsen (2025) The illusion of the illusion of thinking. https://arxiv.org/abs/2506.09250 (b24)
- [M] Gendron et al. (2023) LLMs are not strong abstract reasoners. https://arxiv.org/abs/2305.19555 (b25)
- [V] Ivanova (2024) Toward best research practices in AI psychology. https://arxiv.org/abs/2312.01276 (b26)
- [V] Milliere and Rathkopf (2025) Anthropocentric bias in language model evaluation. https://arxiv.org/abs/2407.03859 (b27)
- [V] Schulze Buschoff et al. (2023/2025) Visual cognition in multimodal LLMs. https://arxiv.org/abs/2311.16093 (c07, c08)
- [V] Schulze Buschoff, Voudouris et al. (2025) Testing the limits of fine-tuning. https://arxiv.org/abs/2502.15678 (c09)
- [V] Schulze Buschoff et al. (2026) Can VLMs learn intuitive physics. https://arxiv.org/abs/2602.06033 (c10)
- [V] Ballout, Jassim, Bruni (2025) Pixels to Principles. https://arxiv.org/abs/2507.16572 (c11)
- [V] Gao et al. (2025) WM-ABench. https://arxiv.org/abs/2506.21876 (c12)
- [V] Garrido et al. (2025) Intuitive physics from self-supervised video pretraining. https://arxiv.org/abs/2502.11831 (c13)
- [V] Storks et al. (2021) TRIP. https://arxiv.org/abs/2109.04947 (c14)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (c15)
- [V] Kosoy et al. (2022) Causal overhypotheses. https://arxiv.org/abs/2206.08353 (c16)
- [V] Samiei et al. (2026) Human adults and LLMs as scientists. https://arxiv.org/abs/2606.06464 (c17, d14)
- [V] Lampinen et al. (2023) Passive learning of active causal strategies. https://arxiv.org/abs/2305.16183 (c18)
- [V] Jin et al. (2024) Corr2Cause. https://arxiv.org/abs/2306.05836 (c19)
- [V] Kiciman et al. (2023/2024) Causal reasoning and LLMs. https://arxiv.org/abs/2305.00050 (c20, c21)
- [V] Zecevic et al. (2023) Causal parrots. https://arxiv.org/abs/2308.13067 (c22)
- [V] Yang et al. (2024) Critical review of causal reasoning benchmarks. https://arxiv.org/abs/2407.08029 (c23)
- [V] Tian et al. (2024/2025) MacGyver. https://arxiv.org/abs/2311.09682 (c25)
- [V] Shapira et al. (2024) Clever Hans or neural theory of mind. https://arxiv.org/abs/2305.14763 (c27)
- [V] Sturb (2026) Revisiting GSM-Symbolic (LessWrong post, not peer-reviewed). https://www.lesswrong.com/posts/Ze4C99Dasj74YKCFh/revisiting (d03)
- [V] Rajeev et al. (2025) Cats confuse reasoning LLM. https://arxiv.org/abs/2503.01781 (d04, d05)
- [V] Li et al. (2024) GSM-Plus. https://arxiv.org/abs/2402.19255 (d06, d07)
- [V] Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (d08)
- [V] Zhao et al. (2026) Is chain-of-thought reasoning of LLMs a mirage? https://arxiv.org/abs/2508.01191 (d09)
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (d11)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (d12)
- [V] Lam et al. (2025) CodeCrash. https://arxiv.org/abs/2504.14119 (d13)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 7 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A18.03-K11** (now single-source: the sources are not independent). The interface/floor-effect interpretation rests only on one paper (Mecattaf et al., listed three times) whose authors overlap with the Voudouris platform paper (same Animal-AI lab); the authors themselves only say control 'might' dominate.
- **A18.03-K02** (now single-source: only one opened source, code check).
- **A18.03-K06** (now single-source: only one opened source, code check).
- **A18.03-K23** (now single-source: only one opened source, code check).
