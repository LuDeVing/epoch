# Fixation, functional fixedness and structured imagination: deep document

*Subfield A09.06. Built from 95 + 20 evidence lines (a01-a33, b01-b31, c01-c31, d01-d20), 40 claims (A09.06-K01 to K40) and a cross-check (critique.md). Evidence ids in brackets, for example [a14]. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Where a number was corrected by the cross-check, the corrected value is used here.*

---

## 1. What it is

Fixation is the pull of what is already in mind on what comes next. Three related things carry the name.

1. **Functional fixedness.** An object seen in its usual role is hard to use in a new role. Duncker's candle problem is the standard case. A box that holds the tacks is harder to see as a platform than an empty box.
2. **Design fixation.** A person who sees an example solution copies its features into their own design. This includes features that are flawed. The count of ideas often does not fall. The overlap with the example rises.
3. **Structured imagination.** When people invent something new in a known category (an alien, a tool, a fruit), the new thing keeps the category's standard properties. It starts from the most easily recalled members. It adapts them. It rarely drops them.

A fourth strand is **knowledge-based set (Einstellung)**. A strong, correct-looking habit blocks a better answer. Experts are hit hardest.

Why it matters for our agent. Our agent is one language model run through a scaffold. Its failure modes line up with each strand.

- It reads a task and locks onto the usual use of an object or the usual reading of a phrase (functional fixedness, BrainTeaser, MacGyver).
- Its open-mode attempts come from one shared mode, so ten attempts are one idea (structured imagination, mode collapse, G4).
- Anything in its context, such as a shown example, a prior draft or a failed attempt, pulls the next attempt toward itself (design fixation, self-conditioning).
- A strong prior (a familiar diagnosis, a familiar puzzle) wins over the evidence on the page (Einstellung).

The subfield asks four things. What is the human evidence and how big is it? Which defixation methods work, with effect sizes? Do language models show the same fixation? What reduces it at equal compute?

The honest answer to the last question is: nobody has measured it. No source compares defixation procedures at equal tokens on the quality of the best final pick (critique, gap 1). Section 8 builds that test.

Links to subfields run in parallel (not covered here): Geneplore (generate then explore), analogical access, schema induction, quality-diversity and novelty search, evaluation of creativity, anytime search and restarts, heuristic design by relaxation, CDCL no-goods, Go-Explore archives, bandits for operator choice, chunking and template theory.

---

## 2. History and theories in depth

### 2.1 Duncker and the candle problem (1945 to 1966)

Duncker (1945) showed that people are slower and less likely to use a box as a platform when it holds the tacks than when tacks and box are separate. Adamson (1952) repeated it. Neither original was opened here; we rely on Glucksberg and on German and Defeyter, who cite them [a33].

Glucksberg (1962, 1964) gives the figures we can check [a01]. With sight, full box (container function shown): N=32, mean 11.08 min (SD 4.84), 16 of 32 failed at the 15 minute cap. Empty box: N=32, mean 3.67 min (SD 4.52), 2 of 32 failed. A touch-only version (blindfolded, N=10) took 5.47 min with 2 failures. The touch group came from a different study, so the comparison is not randomised.

An important detail [a02]. In the touch study, 7 of 8 solvers solved on an accidental later contact with the box. None solved on first touch. Glucksberg reads this as the box cue meeting the problem formulation by contiguity. It was not a planned search for a platform. That reading is compatible with the data, not proven.

Without any manipulation, only about 25% of students find the box solution. Fleck and Weisberg (2004) found 23.5% when thinking aloud and 27.7% silent, p=.736, overall 25% (n=13 of 52 analysed; 58 took part), mean solve time 5.72 min, 10 min limit [a03, b19]. This matches 25% from Weisberg and Suls (1973) and Glucksberg and Weisberg (1966).

What people try first [a04]: about 75% build around the tacks, 14% the wax, 6% matches, 4% the box. The box is not even in the first frame.

### 2.2 Competing explanations of why people stay stuck

| Account | Claim | Key evidence | Verdict |
|---|---|---|---|
| Retrieval failure (Keane) | The right plan is not retrieved. | Glucksberg: solutions came by accidental contact. | Compatible. [a07] |
| Representation / restructuring (Ohlsson 1984, 1992; Knoblich et al. 1999) | The problem is encoded in a way that blocks the answer. It must be re-encoded. Constraints are held (numbers cannot change). Chunks are tight. Relax the constraint or break the chunk. | Matchstick arithmetic; difficulty follows how broad the constraint is [a31, not read, scan]. | Influential. Not required for all solutions (see 2.3). |
| Activation / strength of features | Features of shown examples gain strength and are reused. | Dose response with number of examples [a08]. | Compatible. |
| Retrieval blocking (Smith) | Activated exemplars block recall of others. | Smith 1993 [b01-b03]. | Not separated from activation. [a11] |
| Structured imagination (Ward) | New ideas start from the best-recalled category member and keep category properties. | Ward 1994, 2002 [a13-a17]. | Strong for imagined categories. |
| Category abstraction | People infer a category from the examples and judge their design against it. | Marsh 1996 discussion. | Authors say data do not decide. [a11] |
| Source monitoring failure (cryptomnesia) | People do not know they are copying, so "do not copy" fails. | Marsh Exp 3: delay raised copying, and told-not-to-copy people still copied [a10]. | Plausible. |
| Domain knowledge set | Expertise supplies a strong wrong candidate. | Baseball experts on remote associates [a26]. | Replicated. |
| Developmental (German and Defeyter) | Older children hold a tighter idea of what an object's function is. | 5-year-olds immune [a06]. | Interesting; tiny cells. |

German and Johnson, cited in [a07]: adults judge the original function as the "true" function 86% of the time, 5-year-olds 61%.

### 2.3 Is impasse required? (Fleck and Weisberg 2004)

The impasse and restructuring view says: you hit a wall, then you re-encode. Fleck and Weisberg tested it with 34 analysed protocols [a05]. 44% showed some impasse. Box solution came in 7 of 19 without impasse (37%) and 1 of 15 with impasse (7%); 0 of 3 with a true impasse. Of 213 failures, 128 (60%) were followed by impasse or restructuring. So restructuring was common, but impasse was not needed and did not predict solving. The 10 minute limit may have been too short. Impasse coding is subjective.

Link to SCHEMA S6: the impasse detector is a design choice. The human evidence does not say impasse is a good trigger for restructuring. It says people often solve without it.

### 2.4 Design fixation (Jansson and Smith 1991 onwards)

Jansson and Smith (1991) had student designers draw a car-mounted bicycle rack, a measuring cup for the blind and a spill-proof coffee cup. Those shown an example copied its features, including flawed ones, even when told to avoid them. We only have this through reviews [a21, a32; not opened].

Purcell, Williams, Gero and Colbron (1993) reported largely unsuccessful attempts to replicate. Apparent fixation tracked familiarity and discipline [b12, snippet only].

Vasconcelos and Crilly (2016) reviewed 25 studies and found 14 manipulated variables and no trustworthy single effect size [a21]. Wang, Okada and Takagi (2023) reviewed 53 studies [b06].

### 2.5 Example conformity in a lab paradigm (Smith, Ward and Schumacher 1993)

People who saw example creatures or toys copied the examples' critical features (four legs, tail, antennae) more than controls. The number of ideas did not fall. Exp 1, N=94 (44 control, 50 examples). Overall conformity, toys .22 vs .35, F(1,92)=8.13. Creatures .11 vs .24, F(1,92)=12.50. Ideas per person about 2.8 to 3.1 in both arms [b01].

Exp 2, N=91: conformity did not fade when testing came later in the session [b02].

Exp 3, N=80, 20 per arm, creatures [b03]. Overall conformity: control .16, standard examples .25, "diverge" instruction .33, "conform" instruction .44. ANOVA F(3,76)=8.69. Standard vs diverge t(76)=1.33, not different. The diverge arm was numerically higher. So telling people to differ did nothing here. Telling them to resemble raised copying. So copying is not mainly politeness toward the experimenter.

### 2.6 Structured imagination (Ward 1994, 2002)

Ward (1994) asked people to draw creatures on a distant planet. They gave creatures with Earth-animal properties. Under a lava planet constraint they added wings, not non-animal parts. "Wildest imagination" instructions did not remove the pattern. Only seen through citing papers [a13].

Ward et al. (2002), checked in the paper [a14-a17, b21]:
- Exp 1: 30 people listed animals; 71 imagined alien animals. Imagination frequency correlated with output dominance r=.486 over 150 animals (.674 without "human"). Rank correlated negatively (earlier listed, more used). Typicality and familiarity predicted less well.
- Nearly all imagined aliens had standard features: sense organ 99%, appendage 97%, bilateral symmetry 91% (N=71). People who said they relied on a specific Earth animal were less original: M=3.18 vs 4.34, t(69)=2.81, p<.01. Reliance was self-reported after the task.
- Exp 2: tools for a creature with no appendages. N=135. People adapted Earth tools instead of dropping them. Handles 23% (constrained) vs 73% (control), chi-square(1)=33.20. Mouthpieces 39% vs 1%. Harnesses 20% vs 3%.
- Exp 4: imaginary fruit, N=203. Reliance on at least one Earth fruit: control 66%, "be creative" 62% (n.s.), "not bound by Earth fruit" 48% (p<.05). Almost half still relied on Earth fruit.

A classroom replication [a18]: 25 usable students. Legs were 72% of appendages. Eyes 88% of sense organs. 75% had two eyes. About 20% idiosyncratic. Descriptive only.

Model: the path of least resistance. Imagination samples a starting exemplar by retrievability, keeps its structure, and edits at the margin.

### 2.7 Knowledge-driven set

Wiley (1998) and Ricks, Turley-Ames and Wiley (2007) [a26, b16]. Baseball experts did worse on Remote Associates items whose obvious baseball answer was wrong. Replicated: Exp 1 N=58 analysed, knowledge by problem type F(1,52)=5.58, p=.02, eta2=.10. Exp 2 N=101 analysed. More working memory helps generally. It does not help when a strong wrong candidate is active. It may add focus on the wrong answer. Exp 1 participants may have guessed the aim (demand effect).

Purcell and Gero (1996): an example built on mechanical engineering knowledge fixated only students who knew mechanical engineering [b11, second-hand].

Practising wrong answers worsens later fixation. Remote associate items, N about 136 in Exp 1. Solved .44 (reinstated context, no practice), .38 (two retrievals of red herrings), .42 (new context, no practice). Repetition F(1,132)=5.17, p=.025, partial eta2=.038. Context reinstatement did not matter in Exp 1 [a27].

### 2.8 Defixation methods

- **Generic parts technique (GPT), McCaffrey 2012.** Build a parts tree. For each part ask: can it be broken down further? Does my description imply a use? Redescribe in material and shape words (a wick becomes a piece of string, then cotton strands). See 5.3 for numbers.
- **Abstraction and function-level presentation.** Show examples as functions, not drawings (Atilola 2016, Ezzat 2020, Agogue 2014). Only seen through a review [b09, d11].
- **Expansive examples (Agogue et al. 2011).** In the hen's-egg drop task, 81% of answers sit in one restrictive path (inert device: damp the shock 33%, protect 26%, slow the fall 22%; living device 4%; change the egg 3%) [a19]. A restrictive example lowered originality (p<.005). Expansive examples raised it only marginally (p=.07). Restrictive plus expansive beat restrictive alone (p<.0005). Group effect F(4,129)=11.219. Conference paper. Authors state 132 students; df imply 134.
- **Avoid instructions.** Mixed. See 5.2.
- **Minimal per-idea executive feedback (Ezzat et al. 2017).** See 5.4.
- **Incubation.** Small effect. See 5.5.
- **Education about association.** A short lecture on how the brain associates cut copied flaws. See 5.6.

---

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested. Counts of independent sources follow claims.jsonl, where duplicate papers are merged.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Container cue slows box-as-platform | Full box 11.08 min, 16 of 32 failed; empty box 3.67 min, 2 of 32 failed (N=32 per cell) | Glucksberg 1964 [a01] | E (K01) |
| Base rate of candle solution | About 25% (23.5% vs 27.7%, p=.736; N=52 analysed) | Fleck and Weisberg 2004 [a03, b19] | E |
| First frame in candle problem | Tacks 75%, wax 14%, matches 6%, box 4% | [a04] | S |
| Fixedness grows with age | 7-year-olds 40% vs 89% solve, 115.3 vs 28.9 s; 5-year-olds 60% vs 80%, 44.5 vs 55.8 s (n.s.); N=10 per cell | German and Defeyter 2000 [a06] | S (K02). Paper text gives different percentages (18% vs 89%; 64% vs 65%) than its table; use table. |
| Examples cause copying, not fewer ideas | Creatures .11 vs .24, toys .22 vs .35 (N=94); ideas per person 2.8 to 3.1 in both | Smith et al. 1993 [b01] | E (K03) |
| Dose response with number of examples | 0 to 9 examples; F(4,75)=5.91; critical features 4.4% of features (control) vs 12.1% (nine examples) | Marsh et al. 1996 [a08] | S (K04). Trend statistic inconsistent in paper (4.75 vs 3.25). |
| Feature transfer with fMRI sample | 23% vs 15% (n=85 designs per condition), chi-square 3.6, p=.05; quality n.s.; novelty .71 vs .74, p=.07 | Fu et al. 2019 [a24] | S, borderline |
| "Diverge" instruction does not help | Control .16, standard .25, diverge .33, conform .44 (N=80) | Smith et al. 1993 Exp 3 [b03] | C (K05) |
| Avoid list plus examples lifts originality | 2.65 vs 1.90 original ideas (examples), 2.68 vs 1.88 (avoid); planned d=0.58; examples alone share repeating examples .27 vs .06 (d=1.17); N=144 | George and Wiley 2020 Exp 1 [a25, b07] | C (K05). Interaction not significant (F=2.16, p=.14). Whole gain is in the Examples+Avoid cell. |
| Visual examples hurt; avoid only restores | Original proportion .38 vs .55 (d=.51); Examples+Avoid .59 vs .47 for rest, p=.072, d=.35 | George and Wiley Exp 2 [d12] | C |
| Imagined aliens keep Earth features | Sense organ 99%, appendage 97%, symmetry 91% (N=71) | Ward et al. 2002 [a15] | E (K06) |
| Constrained tool design adapts, not drops | Handles 23% vs 73%; mouthpieces 39% vs 1% (N=135) | Ward et al. 2002 [a16] | E |
| "Be creative" does little | Earth fruit reliance 66% vs 62% (n.s.); "not bound" 48% | Ward et al. 2002 Exp 4 [a17] | E (K19) |
| Starting points follow recall order | r=.486 (150 animals); .674 without "human" | Ward et al. 2002 [a14] | S (K07) |
| Expert knowledge produces set | Knowledge x problem type F(1,52)=5.58, p=.02, eta2=.10 | Ricks et al. 2007 [a26] | E (K08) |
| Practising red herrings worsens fixation | F(1,132)=5.17, p=.025, partial eta2=.038 | [a27] | S |
| Delay does not reduce copying | Smith 1993 Exp 2 N=91 no fade; Marsh Exp 3 N=74 F(1,73)=4.74 (more copying after a day) | [b02, a10] | E (K30) |
| Incubation helps a little | Mean d=0.29, 117 studies | Sio and Ormerod 2009 via Gilhooly [a28, b15] | S (K10). Second-hand. |
| Examples: variety down, novelty and quality up? | 43 studies; abstract only | Sio et al. 2015 [b13, d15] | C (K11). Not opened. Do not cite numbers. |
| Brain-association lecture cut copied flaws | Fixation ratio .88 to .53, p=.025, 12 teams | Howard et al. 2013 [b20] | S (K12). No control group; fixed order. |
| Generic parts technique | 83% vs 49%, N=14 per group, 8 problems, t(26)=4.23, p<.001; d about 1.6 (our calculation) | McCaffrey and Spector 2012 [d01] | S (K13). Inventor's report, no placebo, no replication. |
| Hen's egg: restrictive example hurts | F(4,129)=11.219; restrictive vs control p<.005; expansive vs control p=.07 | Agogue et al. 2011 [a19] | S |
| Per-idea feedback: right direction helps a little, wrong direction hurts more | Expansion ideas: congruent 6.75, control 4.7 (d=.49, p=.05), incongruent 2.75 (d=.79); N=60 | Ezzat et al. 2017 [d08] | S |
| LLM within-run fixation matches people | Category slope 1.013 vs 1.035 (p=.51), ceiling 3.0; within-person categories 12.46 vs 12.68 | Deng et al. 2026 [b22, c15] | S (K14). One model, one task. |
| LLM groups less diverse across runs | Unique categories 22 vs 28; combinations 88 vs 206; bootstrapped groups of 10: 18.45 vs 26.29 | Deng et al. 2026 [c15] | S |
| LLM idea pools less diverse than human pools | GPT-4 pool cosine .255 to .432 vs .243 human; Ma 2024 all 4 metrics; same-prompt pairwise similarity above 0.8 over 70+ models | [c17, c06, c19] | E (K15) |
| Models share one semantic region | Cross-model distance about .21 to .34 | [c11, c19] | E (K16) |
| Seeding with a human first idea | No meaningful gain (N=99 per arm) | Deng Study 2 [c16] | S (K17) |
| Ordinary personas | Between-run distance .635 vs .241 default (2.6 times), but within-run slope .876 vs 1.013 (more fixation) | Deng Study 3 [b24] | S |
| Title-revise-expand CoT on LLM | Slope 1.013 to 1.363; categories 18.45 to 24.84; combinations 39.15 to 55.49; none for humans | Deng Study 4 [b23] | E for "structured prompts raise pool diversity" (K18); the specific chain is S. Not token-matched. |
| 25 method-inspired prompts beat control on novelty | About +10% to +41% (read from figures); short "think outside the box" prompts did as well as long method prompts | IDEAFix [b28, c10] | S |
| Verbalized sampling | 1.6 to 2.1 times diversity; +25.7% human score; recovers 66.8% vs 23.8% direct | Zhang et al. 2025 [b25, c18] | S (K20) |
| Listing k answers in one call | Jokes 1.83 to 2.93 (VS 3.01); poems 1.90 to 2.07 (VS 2.39); stories 2.74 to 2.76 (VS 3.06) | [d03] | S (K37) |
| In-context regeneration with "differ" request | Best of 4 methods in NoveltyBench; frontier models near human-writer diversity over 8 generations | Zhang et al. 2025 [d02] | S (K31) |
| Errors in context raise later errors | Accuracy at turn 100 falls as injected error share rises; thinking mode removes it; sliding window helps | Sinha et al. 2026 [d05, d06] | E (K32), tasks with one key |
| Multi-turn lock-in | 39% average drop; 20 to 300% longer answers | Laban et al. 2025 [d17] | E (K32) |
| Same-model self-critique without a check | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 after two rounds | Huang et al. 2024 [d18] | S (K33) |
| Temperature is weak | 22 to 23 categories at T=1.5 vs 28 human; garbled at T=2.0 | [d16, d19] | E (K38) |
| MacGyver | LLM 35% to 42% vs human 65.1% | Tian et al. 2024 [c04] | E (K22) |
| BrainTeaser | ChatGPT 63% (sentence), 53% (word) vs human 92% | [c25] | E |
| CreativityBench | Part-level correctness .19 vs entity-level .51 | [c24] | E |
| Tool substitution with CoT | GPT-4o with CoT 85% vs human 85.8%; other settings 12 to 14 points below | Gjerde et al. 2025 [c23] | S |
| Einstellung in LLMs | MedEinst trap rate 43% to 66% (5,383 pairs, 17 models); mARC-QA R1 52%, V3 50%, o1 48%, humans 66% | [c26, d07] | E (K34). Preprints and a small physician baseline. |
| Random fact injection | Creativity 88.1 vs 69.6 (LLM-judged, 2,880 responses) | Wong et al. 2026 [c22] | E-ish (K26). LLM judge. |
| Denial prompting | Forbid last technique, ask again; single-path self-correction and planning lost divergent score | Lu et al. 2025 [c21] | S (K25) |
| AI examples fix people too | GenAI fixation +0.32, 89% CI [.11, .55], Bayes factor 124 (N=60) | Wadinambiarachchi 2024 [b26, c13] | E (K21) |

---

## 4. Mechanisms and models

This section is for an engineer. Each mechanism is stated as a process we could build or measure.

### 4.1 Activation-by-retrievability sampler (Ward)

Process.
1. Given a category C (such as "tool" or "alien animal"), the mind samples a starting exemplar E. The probability of picking E follows output dominance: how early and often it comes to mind when the category is listed. [a14]
2. It copies E's structure. Standard properties of C (sense organ, appendage, symmetry) are kept by default.
3. It edits at the margin: adds, swaps or adapts a part. Under a constraint it adapts rather than removes (handles to mouthpieces and harnesses). [a16]
4. It stops when the result passes a plausibility test.

Predictions an engineer can test.
- The first-recalled members of a category predict which exemplars the model builds from. Measure by listing the category first, then asking for a novel item, then checking overlap by code.
- Properties common to all members (the "category-invariant list") are kept at 90% or more unless a rule bans them.
- A generic "be creative" instruction changes little (66% to 62% reliance) [a17]. A specific "do not rely on X" changes more (48%) but not to zero.

Implementation hook. For open mode, S3 can build the invariant list in code from a first call ("list ten typical members, then the properties all of them share"), then request attempts that each violate a named property. This is a code-held constraint, not a free instruction.

### 4.2 Contiguity / cue-meets-formulation (Glucksberg)

An object cue fixed on its usual function becomes available for a new function only when it happens to co-occur with the current problem formulation. Accidental contact solved 7 of 8 [a02]. Engineering reading: the new use appears when the object description enters the context together with the goal, not when the system "decides" to look for it. For a model, this means the object description in the prompt decides what is reachable. A neutral redescription (shape, material, size) changes what it can retrieve. This is the logic of the generic parts technique.

### 4.3 Representation-change and constraint relaxation (Ohlsson; Knoblich)

Process: state the problem with implicit constraints (numbers cannot change; the box is a container). A search under those constraints fails. Relax or break the chunk that carries the constraint. Re-search.

Operator mapping: this is SCHEMA O4 (drop a constraint) and O6 (change representation). The human evidence says difficulty follows how broad the dropped constraint is [a31, not read]. For a program, the constraint list can be extracted in S1/S2 and each item can be relaxed in turn, with code scoring the result.

### 4.4 Generic parts technique as a procedure

From the description [a30, d01]:
1. List the objects in the problem.
2. For each, ask: can it be broken into parts? If yes, break it. Build a tree.
3. For each part, ask: does my description of this part imply a use?
4. If yes, redescribe it with a material or shape word that does not imply the use.
5. Re-read the goal against the redescribed parts.

An LLM version: one call produces the parts tree and redescriptions. A second call, which sees only the goal and the redescribed parts (not the original object names), proposes uses. Code checks each proposal against the task's constraints or against a key. The ordering matters, because step 5 is the one where the usage word is gone from the context.

MacGyver's "divergent-convergent" prompt (list affordances of each object, then pick and plan) is a close prompt relative [c05].

### 4.5 Example exposure: copy, abstraction, blocking

A shown example E adds features F(E) to the pool the next idea draws from. Copy probability rises with the number of examples and with their similarity [a08]. Presenting the example as a function (what it does) rather than a form (what it looks like) removes the feature-level pull while keeping the idea-level help [b09, d11]. Adding a sketch back removed the benefit.

Implementation: if the agent must be shown prior solutions (retrieved analogues, lessons), pass a function-level summary produced by a separate call that strips forms, names and surface features. Then measure overlap by code. This is untested for LLMs (gap 5).

### 4.6 Context as a fixation source for a language model

Three channels.
1. **Shown examples.** Few-shot examples bind behaviour. Chang et al.'s semantic anchoring theory gives S = rho_d - d_r - log k and predicts threshold flips, not smooth drift (two bad examples flipped "2 - 3" from -1 to 23). Abstract and intro only [c29].
2. **Own earlier output.** Errors left in history raise later errors, beyond long-context effects [d05]. Models rely on first attempts, and answers bloat by 20 to 300% [d17]. Thinking models showed no self-conditioning in Qwen3 [d06]. A sliding window helped non-thinking models.
3. **Own earlier ideas.** Deng's sequential generation has the model see its earlier ideas. Category accumulation is one third of the possible rate, like people [b22]. But NoveltyBench found the opposite sign when the prompt says "give a different answer" and keeps all earlier answers [d02].

The reconciliation: earlier output pulls later output toward itself unless the instruction turns the history into an avoid list. The same text, the same context, opposite effect. The instruction decides. Code-held avoid lists are the safest form (see 4.8).

### 4.7 Mode collapse as across-run fixation

Alignment shifts the output distribution toward typical answers (typicality bias in preference data, per Zhang et al.) [c18]. Result: independent runs repeat. Across 70+ models, same-prompt similarity is above 0.8; random pairs sit at 0.1 to 0.2 [c19]. Different vendors sit in one semantic region (distance .21 to .34) [c11]. Chat-template tokens themselves reduce diversity [b30].

Two kinds of fixation are therefore separate.
- **Within-run.** Later ideas in one sequence are pulled by earlier ones. Equal to humans in Deng.
- **Across-run.** Independent runs are alike because they share a distribution. Worse than humans.

The first needs context control. The second needs a source of variation that is not the same distribution: personas, remote-fact injection, retrieved material, sampling a list in one call.

### 4.8 Banned-feature list (code-checked)

Process: code (not the model) tracks the features or categories already used. Each new attempt gets the list. Code scans the output for the banned items by string or category match. On a hit, regenerate.

Support. Human: George and Wiley's explicit avoid list was the only form that lifted originality (d=0.58) [a25]. Human per-idea feedback "search for another path" gave borderline gain (d=.49, N=60) and the wrong signal hurt (d=.79) [d08]. Model: free "do not mention X" lines are unreliable (GPT-4 mentioned X at about 0.13 vs base 0.33; weaker chat models as often or more often) [d09, table partly garbled]. Conclusion: the dependable form is the code check plus regeneration. Nobody has run this against a free instruction on an LLM (gap 2).

Risk: naming the banned feature can re-activate it (review note [b06]). A category label instead of the exact text may be safer. Untested.

### 4.9 Plateau trigger

In a hackathon, ChatGPT kept refining one concept after returns shrank, and pivoted when told performance had plateaued [d14]. Implementation: code watches the score of the best candidate. If it shows no gain over n rounds, code forces a return to an earlier branch or a fresh-context restart. Qualitative, one run.

---

## 5. What holds up

### 5.1 Core phenomena: robust

- **Candle fixedness.** Direction replicated over decades; about 25% base rate matches across 1966, 1973, 2004 [a03]. Effect size from Glucksberg: 11.08 vs 3.67 min [a01].
- **Example copying (Smith).** Replicated by Marsh et al. with the same control and three-example numbers; extended to a dose response [a08, b04]. Fu et al. (2019) shows feature transfer with a within-subject design: 23% vs 15%, p=.05 (borderline) [a24].
- **Structured imagination (Ward).** Replicated in the same paper across tools, fruit, animals; a small classroom replication reproduces it descriptively [a18].
- **Knowledge-based set.** Wiley (1998) replicated by Ricks et al. 2007 [a26].
- **Child functional fixedness.** Replicated in 2025 (N=112, abstract only) [b18].

### 5.2 Avoid instructions: contested

For (works): Chrysikou and Weisberg 2005; George and Wiley 2020 Exp 1 (only with examples plus an explicit list). Against (no effect): Smith 1993 Exp 3, Jansson and Smith 1991, Viswanathan and Linsey 2013 a/b, Viswanathan 2014, Yilmaz 2010 [a22, b06].

Candidate explanations: group vs individual testing, psychology vs engineering students [b06, d10]. Neither has been tested in one design. Wang et al. note naming the example can re-activate it.

Cross-check correction on George and Wiley [critique §1]: the interaction was not significant (F=2.16, p=.14). The planned comparison puts the whole gain in the single Examples+Avoid cell. Examples alone and warnings alone did nothing. Exp 2 shows the avoid line restored the no-example level and did not exceed it [d12].

### 5.3 Generic parts technique: promising, thin

Only the inventors report it. Press release: "67% more often", trained solved more than 8 of 10 [a30, b14]. The paper by the same authors reports 14 trained vs 14 untrained, 8 insight problems, 83% vs 49%, t(26)=4.23, p<.001 [d01]. The 67% is the relative gain (83/49 = 1.69), not 67 points. d about 1.6 is our own calculation from t. No placebo training, so attention and effort are not matched. Two software pilots solved 8 of 8 (N=2). A secondary write-up of "50% vs 83%" matches within rounding.

No replication found. No LLM test found. Treat as a single-source lead.

### 5.4 Per-idea feedback

Ezzat et al. 2017, N=60 [d08]. Direction matters. The gain came from more expansion ideas (6.75 vs 4.7, d=.49, corrected p=.05), not from fewer fixation ideas (congruent vs control n.s., d=.52, p=.12). Wrong-direction feedback hurt more (2.75, d=.79) than right-direction helped. A trained human coded each idea. The code-side analogue is plausible but the cost of a wrong classification is larger than the benefit of a right one. That asymmetry matters for any agent that classifies ideas and steers on the label.

### 5.5 Incubation

Mean d=0.29 over 117 studies, bigger with undemanding gap tasks and for divergent tasks [a28, b15]. It helps against misleading-cue fixation, not against domain-knowledge fixation [b10]. Switching before an impasse helped (Lu et al. 2017); early interruption helped (Youmans 2011). Marsh Exp 3 saw copying rise after a day [a10]. These are different manipulations (a gap after examples vs a break after getting stuck); nobody has put them in one design [critique §2].

SCHEMA 4b says "incubation by distraction not to add" because unconscious-thought-theory effects failed to replicate. d=0.29 for delayed incubation is compatible only if 4b is read as about unconscious-thought claims. The schema owner should check wording. In any case, no LLM operation corresponds to "sleep on it". The nearest agent analogue is a fresh-context restart (anytime-search subfield).

### 5.6 Education about association

Howard et al. 2013: fixation ratio .88 to .53 after a short lecture, p=.025, 12 teams [b20]. Bad-ideas session did not help (74% flawed) and cost ideas. Fixed session order, so lecture, order and fatigue are confounded. Not usable as evidence for the schema.

### 5.7 Examples: harm or help?

The Sio et al. meta-analysis (43 studies) reportedly finds narrower variety but more novel and higher quality ideas, with gains larger for fewer and less common examples [b13]. Not opened; an unverified machine summary [d15] says solution quality correlated positively with copying. Other support: Hernandez et al. 2010 (novelty and variety up, quantity and quality marginally worse) [a20]; Marsh Exp 2 (examples that bundled unusual feature pairs were rated more creative: 3.51 vs 3.07 and 3.08, F(2,72)=4.15) [b05]; Fu 2019 (transfer without quality loss) [a24]; Linsey 2010 (experienced designers made more novel solutions after an example) [a23].

Lesson: "fixation" is a statement about overlap. It does not prove a worse final result. Our tests must score both variety and the quality of the picked answer.

### 5.8 Failed or weak replications and boundary conditions

- Purcell et al. 1993 largely failed to replicate Jansson and Smith [b12, snippet].
- Picture vs text (Cardoso and Badke-Schaub): found once (text beats picture), not replicated in 2009b [b09].
- Verbal overshadowing did not appear in Fleck and Weisberg [a03].
- Function tree benefit vanished when a sketch was added [b09].
- Expansive examples effect in Agogue 2011 only p=.07 [a19].
- Marsh 1996 linear trend inconsistent (F=4.75 vs 3.25) [critique].
- German and Defeyter text and table disagree [critique].
- Child studies have N=10 per cell. The 2025 replication was seen only in an abstract.
- Domain-knowledge fixation is not reduced by incubation or by more working memory [b10, a26].

### 5.9 Moderators that recur

- **Task complexity.** An LLM partner helped on a simple task and hurt on a complex one (N=204 each) [a29]. Constraining the LLM answer to fewer ideas per reply reduced fixation on the complex task and cost inspiration on the simple one.
- **Domain knowledge.** Fixation depends on what the person already knows [b11, a26].
- **Presentation format.** Pictures fix more than text or function trees [b08, b09].
- **Abstraction level of the problem statement.** Abstract statements give divergence; concrete ones convergence (Zahner 2010) [a23].
- **Expertise.** Experienced designers got more from examples than novices [a23].
- **Individual vs group.** Candidate moderator for avoid-instruction results; untested [b06].

---

## 6. Language models

### 6.1 How they behave

**On functional-fixedness style items they fall below people.**
- MacGyver: 1,600+ problems. LLM single-attempt 35% to 42% vs human 65.1%. GPT-4 error analysis on 200 infeasible solutions: wrong tool usage 42.4% (reliable). The other two error shares in the paper (17.7% and 9.5%) did not parse cleanly and are not used [c04, critique]. Models also rarely say a problem is unsolvable.
- BrainTeaser: ChatGPT 63% (sentence) and 53% (word) vs human 92%. It answers "eagle" for "no wings but flies". ChatGPT failed 45% of originals it solved in the reconstruction [c25]. 2023 models.
- CreativityBench: models pick a plausible object and miss the part. Entity correctness .5149 average vs part-level (gold) .1910 (a relative fall of over 60%). Scaling saturates (Qwen3 4B .1882, 14B .2483, 32B .2588). GPT-5.2 gold .1819 [c24].
- Tool-substitution multiple choice: GPT-4o with CoT 85% vs humans 85.8%. Without CoT it fell 12 to 14 points short. GPT-3.5 about 47 points below. Distractors hurt humans and models alike [c23]. Choosing among given objects is easier than generating the use.

**On Einstellung they fall too, and thinking does not clearly fix it.** MedEinst trap rate 43% (Sonnet-4.5) to 66% (Baichuan); GPT-5 52%, Gemini-2.5-pro 61% [c26]. mARC-QA: R1 52%, V3 50%, o1 48%, humans 66%, with high confidence on wrong answers [d07]. The R1 vs V3 gap is two points and untested. A structured agent that forced evidence-by-evidence checks cut the trap rate (Qwen3-32B to 33.75%) but was a multi-part system with no compute-matched control.

**On mental set (order effects) the evidence is too thin.** Haq et al. had 6 problems per cell and results like 0.16/0/0/0. Few-shot examples did not change step counts [c03, b29]. Do not rely.

**Within-run fixation matches humans.** Deng: slope 1.013 vs 1.035 [b22].

**Across-run diversity is worse.** Section 3 rows. Plus Ma et al. 2024: GPT-4's 4,000 solutions less diverse than crowd on all four metrics and five topics; temperature and top-p gave no clean rise [c06]. Anderson et al.: group-level overlap higher with ChatGPT (.24 vs .28 distance, d=.47, p=.038), individual-level not different (.65 vs .66, p=.352) [c14].

**Image models fix too.** CLIP distance differences were tiny (global 16.25 vs 16.05) and the p values rest on non-independent pairs [c02]. GPT-4o chair text had 67.4% unique words vs 78.2% for award entries, N=10 novice designers [c01]. Weak.

### 6.2 What changed it, and by how much

Interpretation rule: most comparisons below used different token costs. None held tokens equal and scored the best pick [critique §3]. Treat sizes as upper bounds for equal compute.

| Method | Effect | Task and source | Caveat |
|---|---|---|---|
| Title, revise, expand (CoT) | Slope 1.013 to 1.363; categories 18.45 to 24.84 | GPT-4o, fitness ideas [b23] | Multi-step, more tokens. LLM coder, no agreement figure [d16]. |
| Persona + CoT | 26% above humans in diversity | Deng Study 4 [c16] | Personas raise within-run fixation (.876). |
| Ordinary personas alone | Between-run .635 vs .241 | [b24] | Within-run worse. Famous-entrepreneur personas did nothing (.985, p=.40). |
| Seed with human first idea | No gain | [c16] | |
| Critique-and-edit | Largest gain of 8 prompt methods | Ma 2024 [c07] | Extra call; no outside check; "unique" worded prompt lowered diversity. |
| 25 defixation-method prompts | +10% to +41% novelty vs control | IDEAFix [b28, c10] | Embedding novelty vs control; same-metric top-5 selection; short "wild" prompts did as well as long method prompts. Authors: gain follows how explicit the divergence instruction is. |
| Verbalized sampling | 1.6 to 2.1 times diversity; +25.7% human score; 66.8% of base diversity | [b25, c18] | Token cost per call higher. Small models can lose quality. Embedding and Claude-judge quality. |
| k answers in one call | Jokes 1.83 to 2.93 | [d03] | Most of the VS gain on jokes. |
| Many personas in one prompt | Least diverse of the persona strategies | [d13] | Parallel calls did better. |
| In-context regeneration with "differ from all" | Best of four; near human-writer diversity at 8 generations | NoveltyBench [d02] | Context grows. No equal-token run. |
| Paraphrased prompts, "unique" system prompt | Marginal | [d02] | |
| Temperature | 22 to 23 categories (T 1.0 to 1.5); garbled at 2.0 | [d16, d19] | Weak lever. |
| Random unrelated fact in prompt | Creativity 88.1 vs 69.6; flexibility 12.4 vs 9.4 | [c22] | Judged by an LLM; short paper. |
| Surprising keywords | Higher novelty, lower diversity | IDEAFix [c09] | Embedding distance counts off-topic text as novel. |
| Novel in-context examples | OLMo-7B +15.5% CoPoet, +5.5% MacGyver; OLMo-2 slightly down | [c20] | Small open models. |
| Denial prompting | Raises originality, lowers quality | [c20, c21] | Extra rounds; code tasks. |
| Self-reflection per step (affordance check) | Infeasible solutions down 9.7% (GPT-4) vs 4.3% for div-conv; efficient solutions up 6.5% (div-conv) vs 2.2% | MacGyver [c05] | Only a vanilla comparison. No CoT arm [d20]. |
| Chain of thought alone | GPT-4o to human level on tool choice | [c23] | Multiple choice. |
| Same-model critique with no check | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 after two rounds | [d18] | One-key tasks. |
| Thinking mode | Removes self-conditioning on errors | Qwen3 [d06] | One-key task. No effect on Einstellung (R1 vs V3 +2) [d07]. |
| Sliding window | Improves accuracy for non-thinking models | [d06] | Only for tasks with no long-range dependency. |
| Plateau signal | Model pivoted | [d14] | One run, qualitative. |
| Fragment, abstract, recombine (NexusAI) | Depth 1.01 vs 0.47; coverage .407 vs .079 | N=14 humans using the tool [c12] | Interface and method mixed; no quality test. |
| Structured affordance CoT | Better grounding, not creativity | CreativityBench [c24] | Authors say it may constrain divergence. |
| Restrict LLM to fewer ideas per reply | Less fixation on a complex task, less inspiration on a simple one | N=204 + 204 (humans using LLM) [a29] | |

### 6.3 When LLMs fixate people

- GenAI image support: fixation +0.32 (89% CI [.11, .55], BF 124); image search +0.27 (BF 42.5). Fluency effect near zero after adjusting for time on task. N=60 [c13].
- LLM partner: help on simple tasks, harm on complex tasks [a29].
- After LLM exposure, unassisted originality did not improve and sometimes fell (1,100 people) [c27].
- ChatGPT groups converge more (d=.47), individuals do not [c14].

These matter if our agent is ever a partner in a team (multiplayer). They do not bear on the single-agent schema.

### 6.4 Measurement problems specific to this field

- Several LLM diversity studies use an LLM to code categories (Deng uses one GPT-4o coder, same model family as the generator; no agreement figure [d16]). G8 warns against model judges.
- Human agreement on diversity ranged 0.54 (poem) to 0.87 (story); on quality 0.49 (story) to 0.79 (joke) [d04].
- Embedding novelty counts any unusual text, including off-topic [c09].
- Keyed probes (counterfactual pair, tool-choice multiple choice) have no judge noise.
- Diversity is not quality. Several studies score the pool, not the pick.

---

## 7. What our agent should take

Format: item. Schema part. Status. Evidence ids. Plain statement. Nothing here goes into SCHEMA.md unless its status is [E] and the item is listed under "Add now". Everything else is "Test first" and flows into UNKNOWNS.md.

### Add now (established)

1. **Keep suggestive or example material out of the first attempt.** S1 input hygiene and S3 / memory. [E]. K03, K30, K08, K21. Evidence [b01, b04, a10, a26, d05, d17]. Copying of shown material is robust in humans (Smith, Marsh, Fu) and does not fade with time. Lessons stay "after the first attempt" (already in SCHEMA section 5). This confirms that rule. Measure copying by code.

2. **Do not append raw failed drafts to the retry context.** S5/S6 and G1. [E]. K32. Evidence [d05, d06, d17]. Errors in context raise later errors; models rely on first attempts and bloat. Rebuild the retry context from the task plus a short code-held list of what failed, or use a sliding window. Scope: one-key tasks. The idea-generation case is a "Test first" item.

3. **Fresh context per attempt stays.** S3. [E]. K14, K15, K32 (consistent with the existing S3 text). Evidence [b22, c15, d05]. Within-run, an LLM is pulled by its own earlier ideas as much as a person. Isolated attempts remove that pull. They do not remove across-run sameness (G4).

4. **Do not add generic "be creative", "think outside the box" or "unique" text, or temperature sweeps, as defixation.** 4b candidates. [E]. K19, K38. Evidence [a17, c17, c10, d16, d19, c07]. "Be creative" 66% vs 62% (n.s.). Temperature 22 to 23 categories vs 28 human. If IDEAFix is right, explicit divergence instruction helps some, but must win at equal tokens (G7).

5. **Treat samples from one model, and from several vendors, as correlated.** G4. [E]. K15, K16. Evidence [c06, c14, c17, c19, c11]. This is already G4. It extends it: mixing vendors is not a free fix (cross-model distance .21 to .34).

6. **Pool diversity and final-pick quality must both be measured. Variety alone is not harm.** G7, section 6 logging. [E for the lesson, C for the effect size of examples]. K11. Evidence [b13, a24, b05, d15]. Because "examples narrow variety but raise novelty and quality" is plausible and unverified, never judge a defixation step by variety alone.

7. **Any critique-and-edit or reflection step needs an outside check that can say "no change".** G2, S5. [E for G2; K33 is single-source for the numbers]. Evidence [d18, c05]. Same-model critique without a check lowered accuracy. MacGyver's reflection worked because it was tied to what objects afford. This agrees with 4b ("unstructured self-reflection").

8. **Use a keyed fixation probe as a standing test, not a judge.** G7, section 6. [E on judge noise; S on which probe]. K36, K28, K34. Evidence [d04, d16, c26, d07, c23]. Counterfactual pairs or tool-choice multiple choice have no judge noise. Category slope needs a fixed category list and a second coder.

9. **Extra thinking should not be assumed to fix knowledge-driven set.** S0 (mode choice) and G11. [E]. K08, K34. Evidence [a26, b10, c26, d07]. Humans do not benefit from more working memory when a strong wrong candidate is active. Reasoning models stayed near 50% on Einstellung items. So the agent should not spend its budget on longer thinking when the failure is a wrong prior; it should use a held-out variant (G3) or a different path.

### Test first (single-source, contested, or human-only)

| # | Item | Schema part | Status | Evidence ids | Why not yet |
|---|---|---|---|---|---|
| T1 | Code-checked banned-feature or banned-category list for repeated attempts (open mode and impasses) | S3, G5, O4 | [C] | K05, K35, K25 / [a25, b07, d08, d09, c21] | Human support exists only for an explicit list with examples (d=0.58). Free instructions fail for LLMs. No LLM run of a code-checked list vs free text. |
| T2 | Denial prompting: after a correct or best candidate, ban its technique and regenerate | O4, S6 | [S] | K25 / [c21] | Code tasks, GPT-4 era. Closest operator to "drop a constraint". |
| T3 | Generic parts operator: parts tree, usage-free redescription, re-read the goal | O3, O6 | [S] | K13, K27, K23 / [d01, c05, c12, c24] | Inventors' report only; no placebo; no replication; no LLM test. |
| T4 | Affordance-grounded reflection at S4 for physical or tool items | G2, S4 | [C] | K23, K40 / [c05, c23, d20] | No chain-of-thought arm in MacGyver. GPT-4o with CoT already matched humans on multiple choice. |
| T5 | Function-level summary of prior solutions in place of the solution text | O2, O6, S3 | [S] | K09 / [b09, a19, d11] | Primary effect sizes unavailable; sketches cancelled the effect; no LLM test. |
| T6 | k answers in one call as the default open-mode generator | S3 | [S] | K37, K20, K31 / [d03, b25, d02] | Pool diversity measured, not best-pick quality; tokens not equal. |
| T7 | Running list of earlier answers with "differ from all of these" (explicit exclusion) | S3 | [S] | K31, K29 / [d02] | NoveltyBench has no equal-token run; context grows. |
| T8 | Title-revise-expand chain for open mode | S3, O2 | [S] for the exact chain; [E] that structured prompts raise pool diversity | K18 / [b23, c07, c17, b28] | Not token-matched; no pick-quality score; the same chain did nothing for humans. |
| T9 | Ordinary personas / remote-fact injection as a source of across-run variety | S3, O7 | [S] | K17, K26 / [b24, c22, c16] | Personas increase within-run fixation. LLM-judged creativity. Allowed only for open ideation, not for single-answer voting (G4). |
| T10 | Plateau detector forcing a return to an earlier branch or fresh-context restart | S6, O4 | [S] | K39 / [d14] | One qualitative run. |
| T11 | Part-level decomposition before choosing a tool or approach | O3, O6 | [S] | K27, K22 / [c24, c12] | Structured CoT improved grounding, not creativity. |
| T12 | Shuffle list order in prompts to avoid last-item fixation | S1 | [S] | K39 / [d14] | Anecdote. Cheap. |
| T13 | Sliding window or restart in place of appended history for idea generation | S3, S6 | [S] | K32, K29 / [d05, d06] | Shown on one-key tasks only. |
| T14 | Counterexample / held-out variant for knowledge-driven traps | G3, S7 | [S] | K28, K34 / [c26, d07] | Detected by a probe, but the cure (ECR-Agent) had no compute-matched control. |

Schema notes for the owner.
- 4b incubation row: see 5.5. K10 recommends re-checking its wording.
- O6 and O4 (change representation; drop a constraint) now have a candidate concrete procedure (GPT, T3). Status stays [S].
- O8 (reframe the goal): "LLM reframing null in one large test" already in SCHEMA. Nothing here changes it.

---

## 8. Concrete tests on our bench

General rules. Both arms get the same total tokens (prompt plus output plus any helper calls, counted by the harness). Setup cost is counted (G7). Select by code (G5). Run each arm on at least 3 seeds. Report the delta with a bootstrap interval. Score the final pick, not only the pool.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 | Example pull | Open-mode design or ideation items with a shown prior solution; MacGyver-style problems | (a) no example; (b) 1 example; (c) 3 example; (d) 3 examples as function-level summaries | Feature overlap with the examples by code (string or category match); best-pick quality by running or key | Overlap (a)<(b)<(c); (d) below (c). Best-pick quality: no loss for (b), unknown for (c). |
| B2 | Defixation at equal tokens, the main gap | Open ideation (NoveltyBench-style) plus MacGyver | (a) plain best-of-n; (b) k answers in one call; (c) title-revise-expand then code select; (d) critique-edit with a code check; (e) verbalized sampling | Best-pick quality by key or run; pool category count with fixed categories and a second coder | (b) at least matches (a) on pool diversity. (c) gains diversity but may lose on pick per token. Expect no more than a few points on best pick. |
| B3 | Banned list vs free instruction vs none | Repeated-attempt open items; design briefs | (a) "avoid these" free text; (b) code-held banned list with regeneration on a string or category hit; (c) no list; same total tokens including regenerations | Rate of banned features in output; category accumulation slope; best-pick quality | (b) cuts banned-feature rate to near zero by construction. (a) cuts it little. Net pick quality unknown. Count extra calls. |
| B4 | Context carry-over in idea sequences | Sequential 10-idea generation | (a) model sees all earlier ideas, no instruction; (b) sees earlier ideas plus "differ from all of these"; (c) fresh context each idea, code removes duplicates; (d) sliding window of last 3 | Category accumulation slope (ceiling 3.0, human 1.035); duplicates | (a) near 1.0 as in Deng. (b) above (a), per NoveltyBench. (c) highest on slope but across-run sameness remains. |
| B5 | Retry context | One-key tasks with a check (ARC-style, code) | (a) append failed drafts; (b) task plus code-held no-good list; (c) sliding window | Pass rate on retry; tokens per solve | (b) at least equals (a), cheaper. Thinking-mode models: no difference. |
| B6 | Generic parts operator | Tool-substitution and MacGyver items; BrainTeaser | (a) plain; (b) zero-shot CoT; (c) parts tree + usage-free redescription + re-read; (d) affordance-checklist reflection | Accuracy on keyed items; feasibility by code or key | Plain model starts well above the 49% human control on easy items (K13). Expect (b) already near the human level on multiple choice. Gain from (c) over (b) 0 to a few points; if none, drop. |
| B7 | Affordance reflection vs CoT | MacGyver | vanilla, zero-shot CoT, free reflection, affordance reflection | Infeasible-solution rate; success | Closes gap 7. Prior: affordance reflection beats vanilla; vs CoT unknown. |
| B8 | Knowledge-driven trap | Counterfactual pairs (control and trap), any domain with a key; remote-associate items with a wrong strong answer | (a) plain; (b) extended thinking; (c) n sampled attempts + vote; (d) n sampled attempts + code harvest of candidates + held-out check | Trap rate; control accuracy | (b) no gain (K34). (c) small. (d) larger. Closes gap 8. |
| B9 | Order and neutral redescription | Candle-style items where the usual use is pre-framed vs listed neutrally | (a) pre-framed; (b) neutral; (c) pre-framed + usage-free redescription | Solve rate | (a) below (b). (c) between or equal to (b) if redescription works. |
| B10 | Category-invariant list (Ward) | Novel object in a category | (a) plain; (b) free "violate typical properties"; (c) code lists invariants from the model's own typical-member listing, attempts must break a named one | Share of outputs keeping the base properties (Ward-style: 99% sense organ etc.) by code; pick quality | (a) 90%+ inherit. (b) small drop. (c) larger drop; pick quality unknown. |
| B11 | Plateau restart | Multi-round optimization items | (a) continue; (b) fresh-context restart at plateau; (c) return to earlier branch | Best score at equal tokens | (b) or (c) above (a) if the lock-in is real. |
| B12 | Standing probe | Fixed set of 40 counterfactual pairs plus 20 tool-choice items | Run for every schema version | Trap rate, accuracy | Used as a regression probe, not as an experiment. |

---

## 9. What does not transfer, and why

- **Age effects.** 5-year-olds are not fixated [a06]. No LLM analogue of age. The useful reading is that fixation comes from learned usage knowledge, so a model with more usage knowledge may be more fixed. Not tested.
- **Incubation and time.** Human forgetting and mind wandering have no direct LLM counterpart. A fresh context is not "forgetting"; it is a restart. Test restart, not sleep (anytime-search subfield). K10.
- **Unconscious plagiarism and source monitoring.** The reason "do not copy" fails in people. A model does see its context. Its failure is different: an instruction to avoid can raise mention of the item (Pink Elephant) [d09]. Mechanism differs.
- **Education about association.** A lecture changes a team's habit. An agent has no habit to change in-session [b20].
- **Fixation from expertise via working memory.** The Ricks result concerns attention breadth in people [a26]. Models have no working-memory span in that sense. The transferable part is only that strong priors beat evidence, and more effort does not fix it.
- **Group vs individual testing.** Human explanation for avoid-instruction splits. A single agent has no group, unless we run several attempts; those share a model (G4).
- **Human-in-the-loop tools.** NexusAI (N=14) and HAICo (N=24) mix interface and method [c12, c28]. Not evidence for an autonomous agent.
- **Effects of AI examples on people.** Fixation by Midjourney images, homogenization of groups [c13, c14, c27]. Relevant to a product that partners with people, not to the single-agent schema.
- **One-key reasoning results used for ideation.** Self-conditioning (Sinha), multi-turn lock-in (Laban), self-correction failure (Huang) are measured on tasks with one answer [d05, d17, d18]. Direction likely carries over; size does not.
- **Humans as the diversity target.** Human crowds are many people. One agent is one person. "Human-level diversity" only makes sense for the pool across runs.
- **Idea-novelty scoring.** Embedding novelty counts off-topic text. G8 says novelty is judged by running. For ideas without a runnable check, we have no clean metric (evaluation-of-creativity subfield).
- **Old model results.** MacGyver (GPT-4, Claude 2), BrainTeaser (2023), Pink Elephant (2023), Huang (2023) are older models. Current models may differ. GPT-4o with CoT already matched humans on multiple choice [c23].

---

## 10. Open questions

1. At equal total tokens, which defixation procedure gives the best final-pick quality: title-revise-expand, critique-and-edit with a check, verbalized sampling, k-in-one-call, or plain best-of-n? No source ran it. (Gap 1.)
2. Does a code-checked banned list beat a free avoid instruction for LLMs, and does it cost more than it returns? Does naming the item re-activate it? (Gap 2.)
3. Does showing an agent its own earlier drafts cause measurable copying in idea generation, and does a no-good summary remove it? The two directions in the literature (Deng, Sinha pull; NoveltyBench help) are separated only by the instruction. (Gap 3.)
4. What is the real effect size of the generic parts technique, and does a prompt version help at equal tokens? (Gap 4.)
5. Does function-level presentation reduce LLM copying as it does in people? Primary effect sizes (Atilola 2016, Ezzat 2020, Agogue 2014) are missing. (Gap 5.)
6. Is the Sio et al. 2015 result correct, and how large? Need the full text and moderator effects (number and commonality of examples). (Gap 6.)
7. Does affordance-grounded reflection beat plain chain of thought on current models? (Gap 7.)
8. Is domain-knowledge fixation in LLMs reduced by extra thinking, by sampling, or by neither? (Gap 8.)
9. Do the human avoid-instruction nulls replicate, and does group vs individual or discipline explain the split? (Gap 9.)
10. What is the cheapest standing fixation probe with the least judge noise? Proposed: counterfactual pair plus tool-choice items. (Gap 10, closed for design.)
11. Does fixation in LLMs rise with usage knowledge, as the child data suggest it does in people? Untested.
12. Is the within-run fixation slope in Deng a property of the model, the task, or the single GPT-4o coder? Needs a second model and a second coder.
13. Does an LLM keep category-invariant properties when asked for novel members (Ward's finding on an LLM)? The one source found [c31] was a snippet and no study measured it.
14. Does the wrong-direction asymmetry (d=.79 harm vs d=.49 help) in Ezzat carry over to a code classifier steering an LLM? A misclassified "fixation" label could cost more than a correct one gains.
15. Does delay after examples interact with incubation after an impasse? Nobody put these in one design.

---

## 11. Sources

[V] = opened and read this session (full text, or the sections named). [M] = snippet, abstract only, or second-hand only.

**Classic and human**
- [V] Glucksberg (1964) Functional fixedness: problem solution as a function of observing responses. https://link.springer.com/content/pdf/10.3758/BF03342819.pdf
- [V] Fleck and Weisberg (2004) The use of verbal protocols as data: an analysis of insight in the candle problem. https://link.springer.com/content/pdf/10.3758/BF03196876.pdf ; https://doi.org/10.3758/BF03196869
- [V] German and Defeyter (2000) Immunity to functional fixedness in young children. https://link.springer.com/content/pdf/10.3758/BF03213010.pdf
- [M] Duncker (1945) On problem-solving; Adamson (1952) Functional fixedness as related to problem solving. Read only through citing papers (URL points to the citing paper). https://link.springer.com/content/pdf/10.3758/BF03213010.pdf
- [V] Marsh, Landau and Hicks (1996) How examples may (and may not) constrain creativity. https://link.springer.com/content/pdf/10.3758/BF03201091.pdf ; https://doi.org/10.3758/BF03213269
- [V] Smith, Ward and Schumacher (1993) Constraining effects of examples in a creative generation task (Exps 1 to 3 read). https://link.springer.com/content/pdf/10.3758/BF03202751.pdf
- [M] Smith, Ward and Schumacher (1993), DOI form, via citing papers. https://doi.org/10.3758/BF03211419
- [M] Ward (1994) Structured imagination: the role of category structure in exemplar generation. https://doi.org/10.1006/cogp.1994.1010
- [V] Ward, Patterson, Sifonis, Dodds and Saunders (2002) The role of graded category structure in imaginative thought. https://link.springer.com/content/pdf/10.3758/BF03195281.pdf ; https://doi.org/10.3758/BF03195282
- [V] Birdsell (2019) Creative cognition: conceptual blending and expansion in a generative exemplar task. http://iafor.org/archives/journals/iafor-journal-of-psychology-and-the-behavioral-sciences/10.22492.ijpbs.5.si.03.pdf
- [V] Agogue, Poirel, Pineau, Houde and Cassotti (2011) The impact of examples on creative design (ICED11). https://designsociety.org/download-publication/30477/the_impact_of_examples_on_creative_design_explaining_fixation_and_stimulation_effects
- [V] Howard, Maier, Onarheim and Friis-Olivarius (2013) Overcoming design fixation through education and creativity methods. https://backend.orbit.dtu.dk/ws/files/56233712/ICED13_Design_Fixation_HowardMaierOnarheimFriis_Olivarius.pdf
- [V] Vasconcelos and Crilly (2016) Inspiration and fixation: questions, methods, findings, and challenges. https://www.repository.cam.ac.uk/bitstreams/415817b1-1a98-4f8b-bb23-56bb4a84cc9f/download
- [V] Fu, Sylcott and Das (2019) Using fMRI to deepen our understanding of design fixation. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2DD81FEE8ED682F6DFF415BF2948EFA6/S2053470119000210a.pdf/div-class-title-using-fmri-to-deepen-our-understanding-of-design-fixation-div.pdf
- [V] George and Wiley (2020) Need something different? Here's what's been done. https://link.springer.com/content/pdf/10.3758/s13421-019-01005-4.pdf
- [V] Ricks, Turley-Ames and Wiley (2007) Effects of working memory capacity on mental set due to domain knowledge. https://link.springer.com/content/pdf/10.3758/BF03193615.pdf
- [V] Chasing red herrings: memory of distractors causes fixation in creative problem solving (2018). https://link.springer.com/content/pdf/10.3758/s13421-018-0799-3.pdf
- [V] Gilhooly (2016) Incubation and intuition in creative problem solving (reports Sio and Ormerod 2009). https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01076/pdf
- [V] Wang, Okada and Takagi (2023) How to effectively overcome fixation: a systematic review. https://doi.org/10.3389/feduc.2023.1183025
- [V] Ezzat et al. (2017) How minimal executive feedback influences creative idea generation. https://doi.org/10.1371/journal.pone.0180458
- [V] McCaffrey and Spector (2012) Behind every innovative solution lies an obscure feature. http://www.kmel-journal.org/ojs/index.php/online-publication/article/download/161/164
- [V] APS press release on McCaffrey (2012), generic parts technique. https://www.sciencedaily.com/releases/2012/03/120307112749.htm ; https://www.psychologicalscience.org/news/releases/stumped-by-a-problem-this-technique-unsticks-you.html
- [M] Purcell and Gero (1996) Design and other types of fixation, second-hand from Wang et al. https://doi.org/10.1016/S0142-694X(96)00023-3
- [M] Purcell, Williams, Gero and Colbron (1993), search snippet. https://ideas.repec.org/a/sae/envirb/v20y1993i3p333-345.html
- [M] Sio, Kotovsky and Cagan (2015) Fixation or inspiration? A meta-analytic review. Publisher blocked; machine summary only. https://doi.org/10.1016/j.destud.2015.04.004
- [M] Sio and Ormerod (2009) Does incubation enhance problem solving? Read through Gilhooly. https://doi.org/10.3389/fpsyg.2016.01076
- [M] Jansson and Smith (1991) Design fixation. Via reviews. https://doi.org/10.1016/0142-694X(91)90003-F
- [M] Knoblich, Ohlsson, Haider and Rhenius (1999) Constraint relaxation and chunk decomposition in insight problem solving. PDF is a scan; search summary only. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf
- [M] Functional fixedness and cooties (2025), replication of Defeyter and German (2003); abstract only. https://doi.org/10.48448/w7qp-0h95
- [M] Cheng and Zhang (2025) record of the Humanities and Social Sciences Communications abstract (c30); the full text was opened as a29. https://www.nature.com/articles/s41599-025-05867-9
- [V] Cheng and Zhang (2025) Inspiration booster or creative fixation? https://www.nature.com/articles/s41599-025-05867-9.pdf
- [M] Atilola 2016, Ezzat 2020, Agogue 2014, Cardoso and Badke-Schaub 2009, Chrysikou and Weisberg 2005, Viswanathan and Linsey 2013, Hernandez 2010, Linsey 2010, Zahner 2010, Lu 2017, Smith 2017, Youmans 2011: cited only through the reviews above (no URLs opened).

**Language models**
- [V] Deng, Brucks and Toubia (2026) Examining and addressing barriers to diversity in LLM-generated ideas. https://arxiv.org/abs/2602.20408
- [V] Zhang et al. (2025/2026) Verbalized Sampling. https://arxiv.org/abs/2510.01171
- [V] Zhang et al. (2025) NoveltyBench. https://arxiv.org/abs/2504.05228
- [V] Wadinambiarachchi et al. (2024) The effects of generative AI on design fixation and divergent thinking. https://arxiv.org/abs/2403.11164
- [V] Anderson, Shah and Kreminski (2024) Homogenization effects of LLMs on human creative ideation. https://arxiv.org/abs/2402.01536
- [V] Carichon et al. (2026) IDEAFix. https://arxiv.org/abs/2606.00875
- [V] Haq et al. (2025) Is your LLM trapped in a mental set? https://arxiv.org/abs/2501.11833
- [V] Yun et al. (2025) The price of format: diversity collapse in LLMs. https://arxiv.org/abs/2505.18949
- [V] Chen et al. (2025) Understanding design fixation in generative AI. https://arxiv.org/abs/2502.05870
- [V] Tian et al. (2024) MacGyver. https://arxiv.org/abs/2311.09682
- [V] Ma, Grandi, McComb and Goucher-Lambert (2024) Exploring the capabilities of LLMs for generating diverse design solutions. https://arxiv.org/abs/2405.02345
- [V] Wang et al. (2026) NexusAI. https://arxiv.org/abs/2604.10575
- [V] Meincke, Mollick and Terwiesch (2024) Prompting diverse ideas. https://arxiv.org/abs/2402.01727
- [V] Jiang, Chai, Choi et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Padmakumar et al. (2025) Measuring LLM novelty as the frontier of original and high-quality output. https://arxiv.org/abs/2504.09389
- [V] Lu et al. (2025) Benchmarking language model creativity: a case study on code generation. https://arxiv.org/abs/2407.09007
- [V] Wong et al. (2026) How context injection shapes creativity in LLM-generated alternative uses. https://computationalcreativity.net/iccc26/papers/ICCC26_paper_171.pdf
- [V] Gjerde, Cheung and Lagnado (2025) Reasoning about affordances. https://arxiv.org/abs/2502.16606
- [V] Qian et al. (2026) CreativityBench. https://arxiv.org/abs/2605.02910
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/abs/2310.05057
- [V] Chen et al. (2026) MedEinst. https://arxiv.org/abs/2601.06636
- [V] Kumar et al. (2025) Human creativity in the age of LLMs (abstract, intro, related work). https://arxiv.org/abs/2410.03703
- [V] Wen et al. (2026) Exploration vs. fixation (HAICo) (results tables not read). https://arxiv.org/abs/2512.18388
- [V] Chang, Chang and Kaya (2025) Semantic anchoring in LLMs (abstract and intro). https://arxiv.org/abs/2506.02139
- [M] Open role-playing with Delta-Engines (2024), snippet only. https://arxiv.org/abs/2408.05842
- [V] Sinha et al. (2026) The illusion of diminishing returns. https://arxiv.org/abs/2509.09677
- [V] Kim et al. (2025) Limitations of LLMs in clinical problem-solving (mARC-QA). https://www.nature.com/articles/s41598-025-22940-0
- [V] Castricato et al. (2024) Suppressing pink elephants with direct principle feedback. https://arxiv.org/abs/2402.07896
- [V] Feng, Helie and Panchal (2025) Enhancing design concept diversity: multi-persona prompting. https://doi.org/10.1017/dsj.2025.10037
- [V] Ege et al. (2025) ChatGPT as an inventor. https://doi.org/10.1017/S0890060425000010
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Peeperkorn et al. (2024) Is temperature the creativity parameter of LLMs? https://arxiv.org/abs/2405.00492

*Cross-check notes carried into this document: MacGyver error shares beyond 42.4% not used; the German and Defeyter text-vs-table mismatch; the Marsh trend inconsistency; the George and Wiley interaction not significant; duplicate papers (b22/c15, b25/c18, b26/c13, a29/c30, b19/a03) counted once. Press-release and secondary figures are marked. Web search quota ran out during the gap search; the Sio 2015 paper, Jansson and Smith 1991, Chrysikou and Weisberg 2005, Atilola 2016, Ezzat 2020 and Agogue 2014 remain unread.*
