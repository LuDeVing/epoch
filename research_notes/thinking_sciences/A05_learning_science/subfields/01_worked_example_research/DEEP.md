# Worked-example research: deep document

*Subfield A05.01. Written from evidence_a-d.jsonl (ids a01-a28, b01-b26, c01-c26, d01-d20), claims.jsonl (K01-K29) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. "Opened" means the page or PDF text was read this session. Several late sources were read through a fetch summarizer; their lines say so.*

---

## 1. What it is

A worked example is a problem plus an expert's full, step-by-step solution. The learner studies it instead of solving the problem. The worked-example effect is the finding that, early in learning, studying solved problems beats solving the same problems. The gain is mostly in time and effort, and it shows up on later problems of the same structure.

The research programme grew out of cognitive load theory (Sweller, 1982-85). Core claim: a novice who solves a problem uses means-ends analysis. This search eats working memory and leaves little for learning the solution pattern (a schema). A worked example removes the search. Attention goes to the states and operators instead.

Four findings define the subfield (from the brief):

1. Studying solutions beats problem solving early in skill acquisition.
2. It works best in algorithmic domains (algebra, geometry, statistics, programming).
3. The advantage fades as expertise rises, and examples are faded into problems (completion, backward fading).
4. Self-explanation is needed for learners to use the example well.

Two further claims in the brief were checked and are weaker than stated: "three examples did no better than one" (one categorisation study, second-hand) and "partly completed examples did as well as full ones" (labs disagree).

Why it matters for our agent: our planned subgoal library stores solved subgoals and offers them by similarity. That is a library of worked examples. The human literature says when this should help (novice on this class, multi-step item, example matches structure, example is self-contained) and when it should not (expert, simple item, new structure, split or padded entry). The LLM literature adds two risks that the human one lacks: copying a wrong or mismatched case at the first step, and format effects that look like learning.

The honest size of the evidence: the founding studies are small and from one lab. The pooled maths effect is about half a standard deviation with huge spread. The LLM studies are mostly not human-style study-versus-solve experiments. No study compares a stored-solution library against a stored-skeleton library at equal tokens.

---

## 2. History and theories in depth

### 2.1 Founding work (1982-1990)

- **Sweller and Cooper (1985)**, algebra, Year 9 students, Cognition and Instruction 2(1). Read in full this session (d01, d02). Experiments 2-5 test worked examples. Experiment 1 is a memory study, not a worked-example test.
  - The pre-existing norm was that the best way to teach problem solving is to give lots of problems (a01 quotes this).
  - The robust result is efficiency: studying costs a fraction of the time (Exp 3, ratio 5.8).
  - The test benefit is real in some experiments and absent in others (Exp 2).
  - There is no far-transfer benefit at all in this paper (Exps 4-5). The authors read this as schema specificity.
- **Cooper and Sweller (1987)**, four experiments (three on algebra transformations, one on word problems). Abstract only (d03, not opened). The abstract claims transfer gains after heavy training and rule automation. This differs from the 1985 pattern. Numbers unread.
- **Zhu and Simon (1987)**, factorisation, classroom. Called the first and most cited classroom study (a01, a28). Not opened. Linked to a production-system model: examples become production rules. That is close to what a subgoal library does.
- **Tarmizi and Sweller (1988)**, geometry, Exps 3-5, via Atkinson 2000 (a03). Examples gave no advantage when text and diagram had to be combined mentally. Integrated format restored it. Quote: guidance "actually retarded learning". Split attention.
- **Ward and Sweller (1990)** and later: examples sometimes no better than problems (b07, a25).
- **Chi, Bassok, Lewis, Reimann and Glaser (1989)**, physics: good learners self-explain missing rationale, monitor better, look back less and more narrowly (a09). Correlational. Original scan unread.

### 2.2 The 1990s: contrast, subgoals, self-explanation, completion

- **Reed and Bolstad (1991)**, work-rate word problems (a05, a06). A small formal model of how examples transfer (section 4.1). Two contrasting examples beat one.
- **Catrambone and Holyoak (1990), Catrambone (1994-98)**: subgoal labels or visual grouping help transfer to adapted procedures (a04). The presence of a label mattered more than its wording.
- **Paas (1992)**, statistics: conventional vs worked vs completion problems (d04, a21; abstract only). Worked and completion beat conventional on transfer. Worked was best.
- **Paas and van Merrienboer (1994)**: variability helps only with low-load worked examples (a07).
- **Quilici and Mayer (1996)**: three examples per type no better than one for categorising statistics word problems (a26; second-hand via Wikipedia).
- **Nathan, Mertz and Ryan (1994)**, N=32 (a08): self-explanation and example study interact for story-problem translation, not for plain algebra manipulation.
- **Bielaczyc, Pirolli and Brown (1995); Renkl, Stark, Gruber and Mandl (1998)**: training self-explanation raised explanation quality by about 2 SD and transfer (a10; review figures only).
- **Stark (1999)**: blanks in examples, with feedback, beat complete examples; Paas found no difference (a11).

### 2.3 Theory consolidation (2000-2019)

- **Atkinson, Derry, Renkl and Wortham (2000)**: the standard review (a01). Uses the ACT-R four-stage skill model (a02): analogy to examples, abstract rules, automation, instance retrieval. Examples matter most in stages 1-2.
- **Kalyuga, Chandler, Sweller and others (2000-2003)**: expertise reversal. Advantage shrinks, vanishes, then reverses with expertise (a19, a24).
- **Chandler, Kalyuga, Sweller and Tuovinen (2001)**: apprentices; novices gain, experienced trainees do not (a24; abstract only).
- **Renkl and Atkinson (2003); Atkinson, Renkl and Merrill (2003)**: backward fading. Remove the last step first, then the last two, and so on. Fading helped near transfer. Far transfer needed principle-naming prompts (a22, a23; abstracts only).
- **Pillay (1994)**: three fading stages better than one (b07; Wikipedia only).
- **Schwonke et al. (2009)**, Geometry Cognitive Tutor: less learning time, and in Exp 2 deeper understanding (b08; Wikipedia only).
- **McLaren, Lim and Koedinger (2008)**, stoichiometry, three studies (N=63, 60, 81): alternating examples with tutored problems cut time by 21% with no learning gain (b09; wiki summary).
- **Shareghi Najar and Mitrovic (2014)**, SQL-Tutor, N=34: examples-only was worst; alternating equalled or beat problems-only (a14).
- **Nievelstein et al. (2013)**, law students: effect held for novices and advanced students, no reversal (d05; abstract only).
- **Chen, Kalyuga and Sweller (2015-2017)**: worked-example effect for high element interactivity; generation effect for low (d06, d07, a18). No statistics retrieved.
- **Sweller, van Merrienboer and Paas (2019)**: mechanism review (a17).

### 2.4 Recent human work (2022-2026)

- **Barbieri, Miller-Cotto, Clerjuste and Chawla (2023)**: first maths meta-analysis. g=0.48 (a12, b01).
- **Sweller (2023)**: history of replication failures. Geometry and kinematics failed until split attention was removed; then redundancy was found (b04, b05, b26).
- **Tetzlaff, Simonsmeier, Peters and Brod (2025)**: expertise-reversal meta-analysis, d=0.505 and -0.428 (d08; snippets only).
- **2026 classroom and lab studies**: Miller-Cotto and Medrano (fading wins, N=114, b10, b11); Stone et al. (preschoolers, N=201, b12); Wang, Li and Liu (collaboration, N=134, b13); primary science (N=68, b14); Gonzaga et al. (LLM-made faded examples, N=27 TAs, c17).

### 2.5 The machine line

- **Chain-of-thought prompting** (Wei et al. 2022, c01) is a few-shot worked example for a model. Later work asks what part of it does the work (b15-b19, c07, c08).
- **Agent skill libraries** (Voyager 2023, Agent Workflow Memory 2024, ExpeL 2024, Buffer of Thoughts 2024, Dynamic Cheatsheet 2025/26, SkillsBench 2026) are the machine form of storing solved subgoals for reuse.
- **2025-2026 correction wave**: strong models gain nothing from generic exemplars once parsing is fixed (Cheng, b20); reasoning models are hurt by raw teacher solutions (Wang 2025, c04); wrong memory is followed (d12, d13).

### 2.6 Competing explanations of the effect

1. **Cognitive load (Sweller)**: examples remove search and free working memory for schema building. Weakness: after-the-fact explanations. Every failure is absorbed as a new moderator (b26). Hard to falsify.
2. **Efficiency only**: examples save time but not learning (McLaren, b09). Schwonke found both. Our K22 treats a format/efficiency share as established.
3. **Production-rule compilation (Zhu and Simon; ACT-R)**: examples are turned into rules by analogy and then compiled (a02, a28).
4. **Self-explanation as the active ingredient**: the example is only raw material; the learner's explaining does the work (Chi, Renkl). Contested by the maths meta-analysis (section 5).
5. **Format alignment (LLMs)**: the exemplar tells the model how to answer, not how to solve (b15, b18, c06).
6. **Productive failure** (c19) is the rival pedagogy: let learners struggle first, then instruct. It was not compared head-to-head with worked examples for learning here.

---

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested. Evidence ids refer to the jsonl files. "Claim" ids are in claims.jsonl.

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Studying costs far less time than solving | Exp 2 (N=20): 27.5 s vs 73.3 s per problem. Exp 3 (N=22): 32.0 s vs 185.5 s, ratio 5.8. Exp 5 (N=24, matched time): worked group processed 24.9 problems vs 8 | Sweller and Cooper 1985 (d01, d02), K23 | E (one lab, tiny cells, Mann-Whitney tests) |
| Test benefit on same-structure problems | Exp 3: 43.6 s vs 78.1 s, errors 0.18 vs 1.64. Exp 4: 48.5 vs 207.6 s. Exp 5: 52.4 vs 101.1 s, errors 0.13 vs 0.58. Exp 2: no benefit (105.4 vs 127.1 s; errors 0.13 vs 0.50, p=.10) | d01, d02, K23 | E for efficiency, mixed for accuracy |
| No far transfer in the founding paper | Exp 4 new-structure problems: 62.6 vs 59.8 s. Exp 5: 163.7 vs 183.3 s; errors 1.06 vs 0.88. Dissimilar problems placed first wiped out the gain on similar ones | d02, K24 | S |
| Pooled maths effect is medium but very variable | g=0.48 (RVE, p=0.01); 43 articles, 55 studies, 181 effect sizes; 8,033 abstracts screened. Interim version: g=0.43 (CI 0.31-0.55), 185 effect sizes from -1.80 to 4.66, 41 negative, I2=94.46% | Barbieri 2023 (a12, b01); Clerjuste 2022 poster (a13, b02), K01 | E (one meta-analysis, two versions) |
| Correct examples beat incorrect-only or mixed sets in maths | Direction only from the abstract | a12, b01 | S |
| Self-explanation prompts did not help; the moderator was negative | Journal version: significant negative moderator. Poster version: no moderator significant | a12, a13, K10 | C |
| Self-explanation training helps (older work) | About 2 SD gain in explanation quality, transfer improved | Renkl et al. 1998; Bielaczyc 1995 (a10; review figures only) | C |
| Self-explanation x study interact for concept-heavy items | N=32. Translation: SE F(1,25)=5.9; load F(1,25)=6.76; interaction F(1,25)=7.1. Manipulation: no effects | Nathan, Mertz and Ryan 1994 (a08) | S (conference paper) |
| Two contrasting examples beat one | Exp 1 (N=65): procedures 15%, example 34%, example+procedures 42%; F(2,62)=6.01; fitted m=.96, r=.65, g=.45. Exp 2: procedures 7, complex 32, simple 38, complex+proc 45, simple+proc 47, simple+complex 65% (rescored 70%); F(5,168)=10.96 | Reed and Bolstad 1991 (a05, a06), K08 | S (one lab) |
| Three examples no better than one (categorisation) | No figures obtained | Quilici and Mayer 1996 (a26, b07) | S (second-hand) |
| Variability helps only with worked examples | 2x2 groups, 6 transfer items; interaction, no variability main effect | Paas and van Merrienboer 1994 (a07) | S |
| Split attention cancels the effect | Geometry Exp 3: no difference; conventional faster at posttest. Exps 4-5: integrated format beat conventional and split-source | Tarmizi and Sweller 1988 (a03), Sweller 2023 (b04, b05), K05 | E |
| Subgoal labels or grouping help adapted-procedure transfer | Poisson study: 4 examples, 6 transfer items; highlighted group better on one novel item. Later studies repeat the label advantage | Catrambone 1990-98 (a04) | E-ish (one lab; small first effect) |
| Expertise reversal | Pooled: d=0.505 (low prior knowledge, high assistance); d=-0.428 (high prior knowledge); 176 effects, 60 studies, N=5,924 | Tetzlaff 2025 (d08), Kalyuga 2000-03, Chandler 2001 (a19, a24), K02 | E (pooled number seen only in snippets) |
| Reverse effect at low element interactivity | Direction only. Imported sizes (not worked examples): testing 0.50 and 0.56; generation 0.40 | Chen, Kalyuga, Sweller 2015 (d06); Chen 2018 (d07), K29 | S |
| Fading beat plain examples in a 2026 classroom trial | N=114. Pre-post g: fading 1.08; fading+SE 0.93; WE+SE 0.32; business as usual 0.24. Regression vs BAU: fading beta=.60 p=.03; WE beta=.01 p=.96; fading+SE beta=.50 p=.08. Posttest differences between conditions not significant | Miller-Cotto and Medrano 2026 (b10, b11), K12 | C |
| Fading needs principle prompts for far transfer | Medium to large effects, abstract only | Atkinson, Renkl, Merrill 2003 (a23) | S |
| Fading gave no load advantage for TAs | N=27, no statistics | Gonzaga et al. 2026 (c17) | S |
| Completion vs full: labs disagree | Paas 1992: worked best, completion second, conventional worst (abstract). Stark 1999: incomplete better. Manson and Ayres 2019 (Grade 8, 54 analysed): full about 4.43 vs single-step about 2.46 at post-test (labels ambiguous) | a11, a15, a21, d04, K13 | C |
| Alternating examples and problems matches or beats example-only when problems have feedback | SQL-Tutor N=34 (PO 12, AEP 11, EO 11): group difference p=.02; EO below AEP p=.02, below PO p=.09; AEP vs PO normalised-gain effect 0.04. Stoichiometry studies N=63/60/81: no learning gain, 21% less time | a14, b09, K14 | E |
| Example-first order beats problem-first | Direction only (Schwonke; van Gog, Kester, Paas 2011) | b08, a25, K15 | S |
| Effect extends to less structured tasks | Law students, novice and advanced: examples beat problems, no reversal (abstract). Primary science N=68: WE and question prompts both large (d=1.31 vs 1.32), WE better on one sub-skill (t(66)=-2.54, p=.014, d=0.62) | Nievelstein 2013 (d05); b14, K16 | S |
| Incorrect examples helped preschoolers as much as correct | N=201, ages 4-7. Dissimilar block, large set: F(2,191)=8.95, p<.001, partial eta2=0.09; correct and incorrect better than baseline; not different from each other | Stone et al. 2026 (b12) | S |
| Collaboration helps only with prior knowledge on complex tasks | N=134, 2x2x2. Near transfer three-way F(1,130)=6.07, p<.05; no far-transfer effects | Wang, Li, Liu 2026 (b13) | S |
| Unrestricted solutions harm later unaided performance | Practice grades +48% (GPT Base), +127% (GPT Tutor); later exam without access: Base 17% worse than control; Tutor about equal | Bastani et al. 2025, PNAS (c18), K21 | S (abstract page only) |

### 3.2 Language-model findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Worked reasoning in the prompt lifts large models | PaLM 540B GSM8K 17.9 to 56.9 with 8 exemplars; other sets 69.4 to 79.0, 72.1 to 73.9, 25.2 to 35.8, 79.2 to 93.3. Different annotators and sampled sets all beat standard | Wei et al. 2022 (c01, c23) | E |
| Invalid reasoning in demos keeps most of the gain | text-davinci-002 GSM8K: standard 15.4, CoT 48.5, invalid 39.5 (81%), no coherence 23.1, no relevance 11.0. Bamboogle 20.6 / 45.2 / 39.4 / - / 23.9 | Wang et al. 2023 (b16, b17, c07, c24), K06 | E (old model; one paper counted once) |
| Numbers in demos matter | Wrong values hurt more than wrong order; exact accuracies not extracted | Mishra and Thakkar 2023 (b19), K07 | S (course report) |
| Labels barely matter for classification | 2.6% average absolute drop with random labels, 12 models | Min et al. 2022 (b15, c08) | E for classification only |
| Symbols and patterns drive CoT, not the facts | Counterfactual prompts, 4 tasks, 3 models | Madaan and Yazdanbakhsh 2022 (b18) | S |
| Strong models gain nothing from generic exemplars | Qwen2.5-72B-Instruct GSM8K: 8-shot 95.75, zero-shot 91.58, zero-shot with fixed parser 95.83. MATH 81.30 vs 81.64. Base: 90.52 / 84.69 / 90.27. LSAT-LR: few-shot 41.55 vs zero-shot 84.65 | Cheng et al. 2025/26 (b20, c06, c20), K03 | E |
| One good demo beats eight | code-davinci-002: cutting 7-8 demos to 1 random costs 0-7%. GSM8K: one positive demo about 83% vs about 60% with all 8. Hard items: about 12.5% when at most 1 of 8 demos is positive | Chen et al. 2023 (c02, c03), K08 | C |
| Few-vs-many depends on task | Classification: 10 to 1000 demos +36.8 on average (up to +50.8). MATH500: plain ICL peaks near 125 examples | Bertsch 2025 (c09); Agarwal 2024 (b22), K09 | E |
| At many shots, exemplar details stop mattering | Peak near 50-100 shots; CoT peaks fast then falls | De Wynter 2026 (b21) | S |
| Raw teacher solutions hurt reasoning models | AIME25: one demo -6 to -16 points; three demos up to -35; GPQA -1 to -5 (1-shot), -4 to -8 (3-shot) | Wang et al. 2025 (c04), K04 | S |
| Turning demos into insights repairs it (I2S) | R1-Distill-14B AIME25 50.00 to 54.00 (I2S) to 60.00 (I2S+); Qwen3-1.7B 35.96 to 41.32 to 42.65; 7B 42.00 to 48.00 to 51.33; GPT-4.1 34.0 to 48.0 (+14.0 points) | Wang et al. 2025 (c05), K04 | S |
| Reflect-on-example step needs a strong model | GPT-4 DROP 72.05 to 79.55; GPT-3.5 DROP 63.20 to 63.35; Llama-2-70B GSM8K 52.5 to 50.6 / 47.0, MATH 16.2 to 13.8 | LEAP (c11, c25), K11 | E |
| Wrong/right pairs with no explanation beat CoT | Beats CoT in 85% and explained pairs in 88% of model x dataset x task combos; editing +4.4 / +2.2; solving +1.6 / +1.9; labelling F1 +5.6 / +6.2 | Alazraki et al. 2025 (c10, c22), K19 | S |
| Model-written examples can replace human ones | Reinforced ICL plateaus near 25 examples, about 5 points above ground-truth ICL on MATH500. Self-generated exemplars: GSM8K 75.0 to about 77.8, MATH about 33.0 to 37.3 (GPT-3.5); K=1 gives 76.1 / 34.8 | Agarwal 2024 (b22); Yasunaga 2024 (b23), K20 | E |
| Static prefix examples do nothing for strong small reasoners; in-trace relevant retrieval helps weak ones | AIME25 columns standard / TTS / static k=3 / random / ThinkRetrieve: Qwen3-1.7B 24.4 / 22.2 / 23.3 / 27.8 / 35.6; Qwen3-4B 63.3 / 64.4 / 62.2 / 65.6 / 66.7; Qwen3-8B 67.8 / 68.9 / 66.7 / 66.7 / 71.1. Max gain +13.4 over TTS | Singh et al. 2026 (d11), K25 | C |
| Prefix hint size is monotone for a weak model | Llama-3.2-3B GSM8K at 0/10/30/50/70/90% prefix: 77.5, 81.1, 81.7, 85.4, 89.8, 94.1. HumanEval dips then peaks at 90% (75.6) | LLM Shepherding (d16), K27 | S |
| Wrong hints cost more than right hints gain | MATH 700 items, 11 models: 0.5355 none, 0.5615 correct, 0.4674 adversarial, 0.4628 random. Base models lose even with correct hint | Give me a hint (d17), K28 | S |
| Unverified memory hurts; verified memory helps | GPT-4o-mini fixed / add-all / strict: RegAgent 67.53 / 55.48 / 70.95; EHRAgent 16.75 / 13.05 / 38.50; AgentDriver 40.11 / 32.32 / 51.00; CIC-IoT 71.50 / 59.90 / 85.40 | Memory management study (d13), K18 | E |
| Conflicting memory is followed; damage rises with baseline skill | MemTrapBench (231 tasks): Qwen3.5-9B -9.5, 27B -21.2, Gemma-4-26B -10.8, Gemini-3-Flash -26.0 pp. Helpful memory +25 to +31 pp. Unconditional retrieval on WebArena (684 tasks): -1.9 and +1.7 pp | Compliance Trap (d12), K18 | E (counted with d13, d17) |
| Curated skills help; self-written skills do not | SkillsBench mean pass: none 24.3, curated 40.6, self-generated 21.0. Opus 4.5 22.0 to 45.3; Haiku 4.5 11.0 to 27.7. 16 of 84 tasks negative (worst -39.3). By skill count: 1 skill +17.8, 2-3 +18.6, 4+ +5.9. By length: comprehensive -2.9 | SkillsBench (d09), K17 | C |
| Entry form is second-order | GPT-5.5 / DeepSeek V4-Flash, 30 tasks: skill present +26.7 to +36.0 / +18.0 to +26.0 pp. Low vs high abstraction +0.7 [-10.0, +12.0] and -6.7 [-14.7, +0.7]. One worked example added: +0.7 [-5.3, +6.0] and +1.3 [-6.0, +9.3] | Xu and Wu 2026 (d10), K26 | C |
| Raw retrieved trajectories beat distilled skills (agents) | SkillEvolBench 180 tasks, 10 configs: Raw-Trajectory RSR 48.2, ESR 37.6; curated static vs none: helps 2, ties 1, hurts 7, mean ESR -2.44 pp | Lei et al. 2026 (d15), K26 | C |
| Distilled notes beat full history (math) | Claude 3.5 Sonnet AIME24 23.3 to 50.0 (DC-Cu); full-history append 26.7; GPT-4o full history 13.3 vs baseline 20.0; GPT-4o Game of 24 10.0 to 93.0 / 99.0 | Dynamic Cheatsheet (d14), K26 | C |
| Skill library compounds on deep tasks | Voyager tech tree: diamond tool reached 1/3 (102 iterations); without library 0/3; AutoGPT/ReAct/Reflexion 0/3. Zero-shot unseen tasks (Table 2, 50-iteration cap): diamond pickaxe 19 +-3 (3/3) vs 36 (2/3) without library; golden sword 18 vs 30; lava bucket 21 vs 27; compass 18 vs 26. Wooden tool: Voyager 6 +-2 vs 7 +-2 without; stone 11 +-2 vs 9 +-4 | Voyager (c12, c26), K17 | C |
| Workflow memory helps most at large train-test distance | WebArena 35.5%, +12.0 points, +51.1% relative; Mind2Web +24.6% relative; margin over human-written workflows 7.6% (results text) or 7.9% (intro); gap-widening gain 8.9 to 14.0 points | AWM (b24, c14), K17 | C |
| Thought templates help algorithmic tasks | GPT-4: Game of 24 82.4 vs 3.0 standard, 11.0 CoT, 74.0 ToT; Checkmate-in-One 86.4 vs 36.4; cost about 12% of multi-query methods | Buffer of Thoughts (c13) | S (self-reported) |
| Insights vs trajectories depend on domain | HotpotQA insights 36% vs retrieval 31%; ALFWorld 50% vs 55%; ALFWorld R0-R3 retrieve-only 40.3 to 54.4, with insights 54.5 to 60.4 | ExpeL (c15) | S |
| Diversity matters on hard items, not on GSM8K | Llama-3.1-8B K=4: GSM8K 65.30 to 66.92 (flat); GeoQuery TopK 62.79 vs TopK-Div 71.14 | Xiao et al. 2025 (d18), K08 | S |
| Converting a retrieved trajectory to condition-action-effect steps restores use | ALFWorld 134 tasks: 81.3% (14B), 93.3% (72B) at about one-tenth the tokens | MATE (d19) | S (abstract only) |
| An LLM can write worked-example explanations and grade self-explanations | ChatGPT explanation Fog medians: students 8.02, experts 8.46, simple 8.67, advanced 9.91, extended 11.09. Judge vs expert F1 .91 (N=8 pilot) | c16, d20 | S |

---

## 4. Mechanisms and models

Each mechanism below is written so an engineer can build it.

### 4.1 Reed and Bolstad reuse model (a05)

Model P(success) on a new item from an example with three parameters.

- m = chance of success by matching the example. Fitted m=.96.
- r = chance of success by following a written rule. Fitted r=.65.
- g = chance of success by general knowledge. Fitted g=.45.

Reuse by matching works when the new item needs zero transformations from the example. Each extra transformation (new numbers, new roles, a changed structure) multiplies the matching chance down, so the model falls back to r or g. The model explained 94% of variance on 12 cells with three free parameters, so it is a rough guide.

Implementation: for a new item, compute a distance score to each stored case (count of changed roles, changed operations, added steps). Retrieve by smallest distance. Expect the benefit to decay with distance. Log distance with every use so the decay can be fitted on our own data.

### 4.2 Load and gating

Cognitive load theory says the example helps when the item has many interacting elements for this learner (high element interactivity) and the learner is a novice in that class. Both conditions together give the effect. If either fails, the effect is zero or reverses (a18, a19, b06, d07).

For an agent the two inputs are:

- **Novice in this class**: the class's plain zero-shot pass rate (already kept in S0 and the class record). Low pass rate means novice.
- **High interactivity**: number of dependent steps in the item. Proxy: steps in the reference solution, or number of values each step uses from earlier steps. No agent-side classifier has been tested (K29).

Gate rule to test: show a stored case only if class zero-shot pass rate is below a threshold T and the item has at least N interacting steps. Learn T from the data (section 8).

### 4.3 Backward fading (a22, a23)

Procedure: stage 0 shows the full solution. Stage 1 hides the last step. Stage 2 hides the last two steps. Continue until the learner solves the whole problem. Rationale: late steps are the ones the learner can do soonest, because early steps set them up.

Agent version: library entries keep the solution as an ordered list of steps with subgoal labels. A "fade level" per class is raised when the agent solves the class with a check pass at the current level. At fade level k the prompt shows the first n-k steps. Human data: fading helps near transfer; far transfer needs a principle-naming prompt (a23). LLM data on fading proper: none. The nearest is the prefix curve (d16): for a 3B model, more prefix always helps. So fading is a candidate for weak-model use only.

### 4.4 Subgoal labelling (a04)

Store the solution as grouped steps. Each group has a short label that names the subgoal ("isolate the variable", "find the symmetry"). The label's wording matters less than having one. Grouping alone also worked. The mechanism: labels prompt the learner to explain why steps belong together. Library entry shape: `{class, problem, groups:[{label, steps:[...]}], answer, check_result}`.

### 4.5 Self-explanation and the insight step

Human mechanism: examples leave steps unexplained; the learner must supply the reasons (a09). Training raises this. Pooled maths data say prompting does not help on average (a12).

Machine analogue: I2S (c05). Step 1: turn the retrieved demos into explicit reusable insights (short lines). Step 2: write a target-specific solution using the insights, not the demo text. Step 3 (I2S+): self-refine. Gains were in points on weak and mid models (R1-Distill-14B +4.0 / +10.0). LEAP (c11) is the other form: make the model fail on the examples, reflect, write principles. LEAP works at GPT-4 strength and hurts at Llama-2-70B strength. Gate by model strength.

### 4.6 Retrieval at the point of need (d11)

ThinkRetrieve: at each step in the reasoning trace, embed the current state, retrieve the most similar solved problem from a bank, and inject it into the trace. Static prefix examples did nothing (Qwen3-4B 62.2 vs 63.3). Random per-step retrieval gave part of the gain. Relevance-matched per-step retrieval gave the most (+13.4 at 1.7B, about +2 at 4B and 8B). Implication for the schema: fetch after a stall (S5/S6), not before the first try.

### 4.7 Verify-before-store (c12, d13)

Voyager stores a skill only after self-verification. The memory study (d13) shows why: agents copy the output of the most similar stored record, so a wrong record propagates. Add-all lost 3.7 to 12.1 points against a small fixed memory. A strict evaluator gained 4 to 22.

Implementation: store an entry only if (a) code check passed on an unfitted input (G3), and (b) the entry matches a minimal-form template. Record the check result with the entry. Delete entries by history: those retrieved and followed by a failing attempt (d13 history-based deletion gave EHRAgent 38.67 to 42.06 and CIC-IoT 85.40 to 89.60 with smaller memories).

### 4.8 Why wrong memory hurts more as skill rises (d12)

Compliance rate is about equal across models. Damage scales with the baseline: each compliance event erases more of a higher baseline. So a strong agent is exposed more, in absolute points. A library gate must be on correctness and match, not on a relevance score alone.

### 4.9 Contrast pairs (c10, c22)

Store a wrong attempt next to the right one, with no explanation. Mechanism (authors' reading): explanations cost context and the model overfits to their wording. The pair marks the difference. Human parallel: incorrect examples helped preschoolers as much as correct ones (b12), but the pooled maths result says correct-only beats mixed (a12). So pairs are an LLM-side candidate, single-source.

---

## 5. What holds up

### 5.1 Replications and where they stand

| Claim | Replication record | Verdict |
|---|---|---|
| Studying is faster than solving | Sweller and Cooper 1985 Exps 2, 3, 4, 5; McLaren 21% less time (b09); Schwonke (b08); Najar EO students spent much less time (a14). | Holds. This is the most robust part. |
| Studying improves later accuracy | Found in 1985 Exp 3 and 5; not in Exp 2. Pooled g=0.48 in maths. 41 of 185 interim effect sizes negative. McLaren: no learning gain against tutored problems. 2026 classroom: plain WE+SE g=0.32 vs BAU 0.24 (beta=.01, p=.96). | Holds on average with huge spread. Not guaranteed per class. |
| Transfer to new structure | None in 1985 (d02). Claimed in 1987 abstract (numbers unread). Fading needs principle prompts for far transfer (a23). Collaboration study: no far-transfer effects (b13). | Near transfer only, with one lab claiming more. |
| Geometry, physics | Failed for years until split attention was removed (b04). Redundancy then found (b05). | Holds only with integrated format. Explained after the fact. |
| Alternating beats example-only | SQL-Tutor (a14), stoichiometry (b09), IES guide rating moderate (b03). | Holds. |
| Fading beats plain examples | One 2026 classroom trial (b10), small cells, pre-test imbalance. Gonzaga null on load (c17). Atkinson 2003 (abstract). | Contested. |
| Partial = full | Paas: worked best (abstract). Stark: partial better. Manson and Ayres: full better. | Contested. |
| Three examples no better than one | One study, second-hand (a26). Reed and Bolstad: two contrasting beat one. | Weak. Contrast, not count, may decide. |
| Self-explanation is needed | Training studies: large. Maths meta-analysis and 2026 trial: no benefit or negative. | Contested. |
| Not limited to algorithmic domains | Law (abstract), primary science (N=68), preschool division (N=201). | Thin but consistent. |

### 5.2 Moderators and their stability

- **Prior knowledge** (expertise reversal): most stable. d=0.505 vs -0.428 pooled (d08, snippets). Chandler 2001, Kalyuga 2003. Nievelstein found no reversal in law (the skill takes long to master).
- **Format** (split attention, redundancy): stable in the lab, explained post hoc.
- **Element interactivity**: direction known, no sizes.
- **Self-explanation prompts**: unstable. The poster found no significant moderator; the journal version found self-explanation and example type significant (K01 note, critique). A moderator reported once should not be trusted.
- **Example type** (correct vs incorrect): journal version only.
- **Heterogeneity**: I2 about 94%. The mean says little about any one class.

### 5.3 Interventions that worked and that did not

Worked:
- Integrating text and diagram (a03).
- Subgoal labels or grouping (a04).
- Alternating examples with problems under feedback (a14, b03).
- Two contrasting examples (a06).
- Backward fading in one 2026 classroom (b10).
- Fading plus a principle prompt for far transfer (a23).

Did not work or reversed:
- Examples when the learner is expert (a19, a24).
- Examples on low-interactivity items (d06).
- Example-only study with tutored-problem control (b09, a14).
- Self-explanation prompts on top of examples in maths (a12, b11).
- Collaboration for low prior knowledge (b13).
- Faded LLM-made examples for TAs, load (c17).
- Unrestricted full solutions from a chatbot: later exam 17% worse (c18).

### 5.4 Weak spots in the human record

- Founding papers: only Sweller and Cooper 1985 was read. Cooper and Sweller 1987, Paas 1992, Quilici and Mayer 1996, Nievelstein 2013, Atkinson 2003, Chandler 2001, Renkl and Atkinson 2003 and Zhu and Simon 1987 were not opened (full numbers unread).
- Many a-line numbers are second-hand through Atkinson et al. 2000 (a03, a04, a07, a09, a10, a11, a18, a19): no N, no effect sizes.
- 2026 samples: cells of 21 to 33 (b10); g in b10 is within-condition pre/post, not a between-group size.
- Duplicate counting: a12/b01 and a13/b02 are one meta-analysis; b20/c06/c20 one paper; b16/b17/c07/c24 one paper; b24/c14 one paper; c10/c22 one paper. Independent counts are by paper.
- Tetzlaff pooled numbers were seen only in snippets; Bastani 2025 only in the abstract.

### 5.5 The "efficiency not learning" reading

McLaren and colleagues: 21% less time at equal learning. Najar: example-only students attempted fewer tasks in less time. Sweller and Cooper: the time ratio (5.8) is much larger than the accuracy gap. The most defensible summary: the effect is first an efficiency effect, and an accuracy gain appears on same-structure items. For an agent, report solve cost (tokens, steps) and accuracy separately.

---

## 6. Language models

### 6.1 What a worked example does to a model

Early work (2022-23, old models): few-shot worked reasoning gives large gains at scale (PaLM 17.9 to 56.9 on GSM8K, c01). Then the ablations: the content can be partly wrong (81% of CoT kept with invalid reasoning, b16), labels can be random for classification (2.6% drop, b15), and patterns and symbols drive the effect (b18). What matters is relevance to the query and step order. Irrelevant demos score at or below the no-example baseline (11.0 vs 15.4). Numeric values matter more than operator order (b19, single-source).

So early CoT demos teach format and frame, not skill. This is the machine form of "part of the effect is format/efficiency" (K22).

### 6.2 What changed with strong models

- **Instruction-tuned strong models** (Qwen2.5-72B-Instruct): 8-shot 95.75, zero-shot 91.58, zero-shot after the answer parser was fixed 95.83. The apparent few-shot gain was a parsing artifact. MATH 81.30 vs 81.64. LSAT: few-shot 41.55 vs zero-shot 84.65, an enormous loss from exemplars (b20). Attention analysis: the model mostly ignores exemplar content. Exemplars written by stronger models (Qwen2.5-Max, R1) did not help.
- **Reasoning models**: raw teacher solutions retrieved by similarity lowered accuracy. AIME25: one demo -6 to -16 points, three demos up to -35 (c04). Two causes given: the model copies steps; it fails to transfer the strategy.
- **Small reasoning models**: static prefix examples did nothing (ThinkRetrieve). Per-step relevant retrieval helped, shrinking with size: +13.4 at 1.7B, about +2 at 4B and 8B (d11).
- **Weak models and base models**: examples still help format (Qwen2.5-72B-Base 90.52 vs 84.69; fixed-parser gap only 0.25 points, c20). Base models are hurt by even a correct hint (d17).

This matches expertise reversal in direction. Caveat: the direction is the same as in humans, but whether the mechanism is the same is untested. SkillsBench found the opposite on one axis: gains did not shrink for stronger models (Opus 4.5 22.0 to 45.3 vs Haiku 4.5 11.0 to 27.7, d09). The difference may be that the skills there are expert-written procedures, not solved cases, in a harder, agentic setting.

### 6.3 How many examples

- Fewer is fine for reasoning: 7-8 demos to 1 random demo costs 0-7% (c02). One known-correct demo beat all eight (83% vs 60%).
- More is needed for many-label classification: +36.8 points average for 10 to 1000 demos (c09).
- MATH: plain many-shot peaks near 125 then declines (b22).
- Diversity: flat on GSM8K at K=4 (65.30 to 66.92); helps on harder non-reasoning tasks (GeoQuery +8, d18).
- Skill count in agents: 1 skill +17.8 pp, 2-3 skills +18.6, 4+ skills +5.9 (d09). Comprehensive skills -2.9.

### 6.4 Forms of the stored case

| Form | Result | Source |
|---|---|---|
| Full teacher solution | Hurts reasoning models | c04 |
| Insights distilled from demos (I2S) | Repairs it: R1-14B 50 to 54 | c05 |
| Thought template | Strong on algorithmic tasks (Game of 24 82.4 vs 3.0) | c13 |
| Workflow (induced sub-routine) | WebArena +12.0 points | b24 |
| Raw trajectory (same-family, retrieved) | Beat distilled skills in SkillEvolBench | d15 |
| Distilled cheatsheet | Beat full history (23.3 to 50.0 vs 26.7) | d14 |
| Condition-action-effect conversion | 93.3% on ALFWorld at 1/10 tokens | d19 |
| Wrong/right pair, no explanation | Beat CoT in 85% of combos | c10 |
| Curated skill doc vs one worked example added | +0.7 / +1.3 pp, intervals cross zero | d10 |

The comparisons conflict because the raw forms differ (all history vs same-family retrieved), the tasks differ (reasoning vs action), and the models differ. No study compares full solution, skeleton, insight and pair at equal tokens.

### 6.5 The risk side: wrong or conflicting entries

- Add-all memory loses 3.7 to 12.1 points against a small fixed memory. A strict evaluator gains 4 to 22 (d13).
- Conflicting memory: -9.5 to -26.0 pp across models; helpful memory +25 to +31 pp (d12).
- Wrong hints: about -6.8 vs +2.6 for right ones (d17).
- Agents copy the most similar stored record. Input-output similarity correlated about r=1 on RegAgent (d13).
- Not measured: accuracy as a function of the percent wrong in the library.

### 6.6 Self-explanation and reflection in models

- I2S: helps (c05).
- LEAP: GPT-4 +7.5 on DROP; GPT-3.5 about 0; Llama-2-70B negative (c11). Low-level and high-level principles are within noise (c25).
- LLM judge for student self-explanations: F1 .91 on N=8 pilot (d20). This checks the tutor, not the effect.
- Whether a self-explanation step helps the explainer at agent strength is open.

### 6.7 Tutoring and learners

- Giving a full-answer chatbot to students: practice up 48%, later unaided exam 17% worse. A hint-only tutor removed most of the harm (c18).
- An LLM can write explanations of code examples close to expert ones but harder to read (Fog 11.09 for extended prompts vs 8.46 for experts, c16).
- LLM-generated faded examples for TAs: no load advantage (c17).
- Productive-failure steering of a tutor is possible, but no learning gain was tested (c19).

### 6.8 Honest limits of this section

- Many results are on old models (text-davinci-002, code-davinci-002, GPT-3.5).
- AIME has 30 items; one item is 3.3 points.
- Several 2026 results were read through a fetch summarizer.
- None of the LLM studies is a human-style worked-example experiment (study versus solve, matched tokens, near vs far test).

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory section. Status: [E] established, [S] single-source, [C] contested. Evidence ids are those in the jsonl files.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Verify before store.** A library entry is written only after a code check on an unfitted input passes (G3). Wrong entries are followed at the first step and cost more than right ones gain. | G (new line under G2/G3), memory | [E] | d12, d13, d17, c12, b24, c03; K18 |
| A2 | **Gate the example on need.** Show a stored case only when the class's plain zero-shot pass rate is low. Strong models gain nothing from generic examples; examples can hurt. Use the class record already kept for S0. | S0 / memory | [E] | b20, c06, c20, d11, d12, d14, d08, a19, a24; K02, K03 |
| A3 | **Retrieve by structure, not by topic.** The founding result is specific to structure. Irrelevant demos fall to baseline or below. | memory | [E] for relevance (LLM), [S] for human specificity (d02) | b16, b17, c07, d02, d11; K06, K24 |
| A4 | **Keep entries self-contained and minimal.** No references to figures or text that are not in the prompt (split attention). No padding that restates steps (redundancy). | memory (entry format) | [E] | a03, b04, b05; K05 |
| A5 | **Store numbers exactly.** Do not paraphrase or shuffle values in a stored solution. | memory | [S] (b19) but harmless | b19; K07 |
| A6 | **Do not apply a few-shot cap to label-mapping subtasks.** The one-example rule is for reasoning with worked solutions. | memory | [E] | c09, b22; K09 |
| A7 | **Interleave with a code-checked attempt.** When the agent has a verifier, alternating case and attempt matches or beats case-only. Report tokens to solve. | S (S3-S5 loop) | [E] | a14, b09, b03; K14 |
| A8 | **Always run a format-only control and a fixed parser** in every test of the library. Part of any example effect is format alignment. | G7 (measurement) | [E] | c06, b15, b18, d09; K22 |
| A9 | **Report cost and accuracy separately** for library on/off. The robust human effect is efficiency. | G7, section 6 logging | [E] | d01, b09; K23 |
| A10 | **Use model-written solved cases as the fill, but only verified ones.** Model-written examples match or beat hand-written. Self-written skills without verification give nothing (SkillsBench 21.0 vs 24.3). | memory | [E] for model-written examples; [C] for unverified self-written skills | b22, b23, d09; K20 |

### 7.2 Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Example after a failed attempt versus before.** Attempt first, reveal the case only on failure. | S (order) | [S] | b08, a25, c18, d11; K15, K21, K25 |
| T2 | **Insight line instead of raw demo for reasoning-tuned models** (I2S pattern). | memory / O | [S] | c04, c05; K04 |
| T3 | **One matched case versus two contrasting cases** versus two near-duplicates, at equal tokens. | memory (k) | [C] | a06, a26, c02, d18; K08 |
| T4 | **Backward-faded entries** for classes the agent fails. | memory / S | [C] | b10, a22, a23, c17, d16; K12, K13, K27 |
| T5 | **Wrong/right pair entries**, no explanation. | memory | [S] | c10, c22, b12; K19 |
| T6 | **Self-explain operator** (goal and reason per step) at the agent's strength. | O | [C] | a12, b11, c11, c05; K10, K11 |
| T7 | **Subgoal labels and grouped steps** versus a flat trace. | memory (entry format) | [S] (human; no LLM test) | a04 |
| T8 | **Entry form**: full case, skeleton plus case, abstract insight. | memory | [C] | d10, d14, d15, d19, c13; K26 |
| T9 | **Element-interactivity gate** (skip example on simple items). | S0 | [S] | d06, d07; K29 |
| T10 | **Wrong-entry dose response** (0, 10, 30% wrong). | G | [E] for direction, size unknown | d12, d13, d17; K18, K28 |
| T11 | **Near versus far structure test of every class.** Expect gains only on near. | memory | [S] | d02; K24 |
| T12 | **Ill-structured tasks**: does the library help on open-ended items? | memory scope | [S] | d05, b14; K16 |
| T13 | **Library on/off stratified by task depth** and by train-test distance. | memory | [C] | c12, c26, b24, d15; K17 |

### 7.3 What not to add

- Padding every example with a self-explanation prompt by default (contested, may be wasted tokens).
- A generic block of three solved examples in the prompt prefix (d11: nothing for strong small models; c04: harmful for reasoning models).
- Unverified self-written skills (d09).
- Case-only study with no attempt, when a verifier exists (a14).

---

## 8. Concrete tests on our bench

All tests compare arms at equal total tokens (prompt plus generated), same answer parser, same items, same seeds. Setup cost is counted (G7). Report per-class results, not one average (heterogeneity I2 about 94%). Use at least 3 seeds. With ARC-sized pools the smallest power-able effect is large; report intervals.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| **W1. Library on/off with format control** | ARC items plus word-puzzle and BrainTeaser items | (a) zero-shot, (b) one format-only exemplar (right layout, unrelated content), (c) one retrieved verified case | Pass rate, tokens to first pass, per class | b not far from a; c above b only on classes with low zero-shot pass rate. Expect +0 on easy classes (K03) |
| **W2. Gate on zero-shot success** | Mixed-difficulty pool | (a) always show case, (b) show only when class zero-shot pass rate < T (try 30%, 60%), (c) never | Pass rate, tokens | b matches or beats a at fewer tokens; a below c on easy classes |
| **W3. Case before versus after a failed attempt** | Items the agent fails zero-shot | (a) case in prefix, (b) attempt first, case after failure (S5), (c) no case | Pass rate on initially failing items; copy rate (does the answer reuse the case's outputs) | b >= a; a shows more copy errors on mismatched cases |
| **W4. k sweep** | Reasoning items | k=0, 1, 2, 4 retrieved cases, shorter cases as k grows | Pass rate at equal tokens | Flat or declining past k=1 or 2 (c02, d18). Classification-like subtasks excluded |
| **W5. Contrast versus near-duplicate** | Items where two solution routes exist | (a) one case, (b) two contrasting cases, (c) two near-duplicate cases | Pass rate on near and far items | b > c on far items; b ~ a on near items |
| **W6. Entry form** | Same item pool, same retrieval | (a) full solution, (b) subgoal skeleton plus full solution, (c) abstract insight line only | Pass rate at equal tokens | a ~ b; c better for reasoning-tuned models, worse for non-reasoning (c05 vs d15) |
| **W7. Wrong-entry dose response** | Class with a clean library | 0%, 10%, 30% wrong or conflicting entries, matched retrieval | Pass rate slope; recovery rate after first wrong step | Linear or steeper loss; damage larger for the stronger model arm (d12) |
| **W8. Fading** | Items the agent fails zero-shot | (a) full case, (b) last step blank, (c) last two blank, (d) prefix only | Pass rate; tokens | Expect no gain at agent strength; gain only for a small model arm (d16) |
| **W9. Self-explain operator** | Same as W1(c) | (a) case only, (b) case plus one-line goal and reason per step, equal tokens by shortening the case | Pass rate, per model size | Gain at large model, loss at small (c11) |
| **W10. Near versus far** | Each library class: near-structure and new-structure items | library on vs off | Pass rate, split by distance | Gain on near; none on far (d02) |
| **W11. Contrast pair entries** | Math-like items with known common error | (a) clean solution, (b) wrong/right pair, no explanation | Pass rate, error-type recurrence | b > a by about 1 to 5 points (c10) |
| **W12. Interactivity gate** | Items labelled by number of interacting steps | show vs skip case by label | Pass rate, tokens | Case helps at high label, not at low |

Also log (G6 logging): distance score of the retrieved case, whether the case was followed, which state it was used in.

---

## 9. What does not transfer, and why

| Human finding | Why it may not transfer |
|---|---|
| Working memory frees up when search is removed (cognitive load core) | The model has no working-memory limit of the same kind. Whether in-context search crowds out step content is unknown (a17 says "checkable", not checked). |
| Self-explanation as the active ingredient | Humans must supply missing reasons. A model gets reasons in the entry for free. Model-side data say it helps only above a strength threshold (c11). |
| Fading as load management | It is a device for managing a learner's load. LLM data only show a prefix helps a weak model, not that fading teaches (d16). |
| Expertise grows by practice, so examples are retired | The model's skill is fixed by weights; only the class record changes. The gate is on zero-shot success, not on learning over time. |
| Spacing, forgetting | The model forgets nothing between calls. Library entries do not decay. Schema specificity (d02) was "easily forgotten" by humans; for a model it is retrieval match that decides. |
| Examples teach through schema construction | Strong models ignore exemplar content (Cheng attention analysis). The effect in the model is mostly format and frame (b15, b18). |
| Three examples no better than one (categorisation) | Task-specific. For many-label classification more examples keep helping (c09). |
| Contrast between two examples helps | Evidence is one human lab (Reed and Bolstad) and a non-reasoning diversity study (d18). Not shown for reasoning at equal tokens. |
| A learner with an example will study it | A model follows the most similar stored record at the first step (d12, d13). It does not "study" it. Copying is the main LLM risk, absent from the human case. |
| Collaboration around an example helps those with prior knowledge | Agents sharing one base model are correlated (G4, G9). Do not read b13 as a case for multi-agent review. |
| Student harm from a full-solution chatbot (c18) | The harm is to a human's later unaided skill. Our agent has no later unaided exam; the analogue is losing the attempt-first signal for the class record. |
| Transfer from tutoring studies on children | Samples are 4-year-olds to Grade 8; effects in preschoolers (b12) say little about a model. |

---

## 10. Open questions

1. What are the true Sweller and Cooper 1985 effects against independent replications, and what do Cooper and Sweller 1987 report (N, means, transfer)? Only one lab has produced the founding numbers.
2. Does a retrieved solved case help a current frontier model on hard, non-saturated items at equal tokens, with a format-only arm and a fixed parser? Cheng and Wang 2025 say no or harmful; Voyager and AWM say yes. Candidate separators: model type, task depth, example abstraction.
3. Which entry form is best at equal tokens: full solution, skeleton, insight line, or wrong/right pair?
4. Where is the cross-over point for an agent class (how many unaided successes before the example should stop being shown), and does gating on zero-shot success recover the benefit?
5. How many examples, and what kind of difference between them, for reasoning items?
6. Does backward fading help any LLM, or is it only a human load device?
7. Does a self-explanation step help at the agent's strength, and at which strength does it reverse (LEAP Llama-2 versus GPT-4)? Is the negative moderator in the maths meta-analysis an artifact of prompt quality?
8. How fast does library quality degrade as wrong entries enter? (No slope exists; threshold unknown.)
9. Do human results in ill-structured domains hold with numbers (Nievelstein 2013 N and effect sizes)? This decides whether the library should cover non-algorithmic tasks.
10. How large is the reverse effect at low element interactivity, and can the agent classify an item as low interactivity cheaply?
11. Does the Voyager-style compounding appear on shallow bench items, or only on deep compositional ones? (Early tiers showed no benefit.)
12. Is the apparent copying in reasoning models a trait of RL-trained models or of the specific teacher traces used?
13. The pooled expertise-reversal effect (d=0.505 / -0.428) was seen only in snippets. Does it split by worked example versus other assistance?

---

## 11. Sources

[V] opened and read this session (some through a fetch summarizer, noted). [M] abstract, snippet or secondary summary only.

### Human research

1. [V] Atkinson, Derry, Renkl and Wortham (2000), Review of Educational Research 70(2) - https://assess.ucr.edu/media/741/download (a01-a04, a07, a09-a11, a18, a19; used as a secondary source for many founding studies)
2. [V] Sweller and Cooper (1985), Cognition and Instruction 2(1), 59-89 - https://onderwijs.felienne.nl/vakdidactiek/materiaal/sweller_worked_examples.pdf (d01, d02). The synapsesocial record https://synapsesocial.com/papers/W2046675442 was snippet-only (a20).
3. [V] Reed and Bolstad (1991), JEP:LMC 17(4), 753-766 - https://users.cs.northwestern.edu/~paritosh/research/Bote04/ReedUseOfExamplesInProblemSolving.pdf (a05, a06)
4. [V] Nathan, Mertz and Ryan (1994), AERA paper - https://website.education.wisc.edu/~mnathan/Publications_files/1994_Nathan_AERA94_SExplnCogLoad.pdf (a08)
5. [V] Barbieri, Miller-Cotto, Clerjuste and Chawla (2023), Educational Psychology Review 35 - https://link.springer.com/article/10.1007/s10648-023-09745-1 (abstract page; critique re-confirmed numbers) (a12, b01)
6. [V] Clerjuste, Chawla, Barbieri and Miller-Cotto (2022), conference poster - https://www.cehd.udel.edu/wp-content/uploads/2022/02/Worked-Examples-Meta-Poster_022722_SC.pdf (a13, b02, b03)
7. [V] Shareghi Najar and Mitrovic (2014), RPTEL 9(3) - https://rptel.apsce.net/index.php/RPTEL/article/download/2014-09026/220/649 (a14; table layout garbled)
8. [V] Manson and Ayres (2019), Educational Psychology - https://doi.org/10.1080/01443410.2019.1650895 (a15; means ambiguous)
9. [V] Koedinger interview (2008), IES practice guide video transcript - https://dwwlibrary.wested.org/files/5204143.pdf (a16)
10. [V] Sweller, van Merrienboer and Paas (2019), Educational Psychology Review 31 - https://link.springer.com/article/10.1007/s10648-019-09465-5 (a17-a19)
11. [V] Sweller (2023), The development of cognitive load theory: replication failures and theory integration - https://link.springer.com/doi/10.1007/s10648-023-09817-2 (b04-b06, b26)
12. [V] Wikipedia, Worked-example effect (accessed 2026-10-26; tertiary; map only) - https://en.wikipedia.org/wiki/Worked-example_effect (a25, a26 via, a27 via, b07, b08)
13. [V] LearnLab wiki summary of McLaren, Lim and Koedinger (2008) - https://learnlab.org/wiki/index.php?oldid=8825 (b09)
14. [V] Miller-Cotto and Medrano (2026), Br J Educ Psychol - https://europepmc.org/article/PMC/PMC12879535 (b10, b11)
15. [V] Stone, Fish, Chernyak, Guadalupe and Cordes (2026), J Intell - https://europepmc.org/article/PMC/PMC13608103 (b12)
16. [V] Wang, Li and Liu (2026), Front Psychol - https://europepmc.org/article/PMC/PMC13337871 (b13)
17. [V] Question prompts vs worked examples in primary science (2026), Behav Sci - https://europepmc.org/article/PMC/PMC13024580 (b14)
18. [V] Nievelstein, van Gog, van Dijck and Boshuizen (2013), Contemp Educ Psychol 38 - https://doi.org/10.1016/j.cedpsych.2012.12.004 (d05; repository abstract only; a27 [M])
19. [V] Chen, Castro-Alonso, Paas and Sweller (2018), Front Psychol 9:1483 - https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01483/full (d07; fetch summarizer)
20. [M] Zhu and Simon (1987), Cognition and Instruction 4(3) - https://kilthub.cmu.edu/articles/journal_contribution/Learning_mathematics_from_examples_and_by_doing/6616958/1 (a28)
21. [M] Paas (1992), J Educ Psych 84(4) - https://research.utwente.nl/en/publications/training-strategies-for-transfer-of-statistical-problem-solving-s/ and https://doi.org/10.1037/0022-0663.84.4.429 (a21, d04; abstract only)
22. [M] Renkl and Atkinson (2003), Educational Psychologist 38 - https://asu.elsevierpure.com/en/publications/structuring-the-transition-from-example-study-to-problem-solving--2 (a22)
23. [M] Atkinson, Renkl and Merrill (2003), J Educ Psych 95(4) - https://asu.elsevierpure.com/en/publications/transitioning-from-studying-examples-to-solving-problems-effects-/ (a23)
24. [M] Chandler, Kalyuga, Sweller and Tuovinen (2001), J Educ Psych 93(3) - https://ro.uow.edu.au/edupapers/139/ (a24)
25. [M] Quilici and Mayer (1996), J Educ Psych 88 - second-hand via Wikipedia (a26)
26. [M] Cooper and Sweller (1987), J Educ Psychol 79:347-362 - https://search.worldcat.org/oclc/7129039903 (d03)
27. [M] Chen, Kalyuga and Sweller (2015), J Educ Psychol 107:689-704 - https://doi.org/10.1037/edu0000018 (d06)
28. [M] Tetzlaff, Simonsmeier, Peters and Brod (2025), Learn Instr 98 - https://www.sciencedirect.com/science/article/pii/S0959475225000660 (d08; snippets, 403 on the publisher page)
29. [M] Bastani et al. (2025), PNAS 122(26) - https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html (c18; abstract page)
30. [V] Gonzaga, Vassar and Jiang (2026), SIGCSE TS - https://sigcse2026.sigcse.org/details/sigcse-ts-2026-Papers/101/CS-Teaching-Assistant-Perceptions-on-LLM-Generated-Faded-Worked-Examples-for-Feedback (c17; summary page only)

### Language-model research

31. [V] Wei et al. (2022), Chain-of-Thought Prompting - https://arxiv.org/abs/2201.11903 (c01, c23)
32. [V] Chen et al. (2023), How many demonstrations do you need - https://arxiv.org/abs/2303.08119 (c02, c03)
33. [V] Wang et al. (2025), From Harm to Help - https://arxiv.org/abs/2509.23196 (c04, c05)
34. [V] Cheng et al. (2025/2026), Revisiting CoT: zero-shot can be stronger than few-shot - https://arxiv.org/abs/2506.14641 (b20, c06, c20)
35. [V] Wang et al. (2023), Towards understanding chain-of-thought prompting - https://arxiv.org/abs/2212.10001 (b16, b17, c07, c24)
36. [V] Min et al. (2022), Rethinking the role of demonstrations - https://arxiv.org/abs/2202.12837 (b15, c08)
37. [V] Madaan and Yazdanbakhsh (2022), Text and patterns - https://arxiv.org/abs/2209.07686 (b18; abstract-level)
38. [V] Mishra and Thakkar (2023), Stress testing chain-of-thought prompting - https://arxiv.org/abs/2309.16621 (b19)
39. [V] De Wynter (2026), Is in-context learning learning? - https://arxiv.org/abs/2509.10414 (b21)
40. [V] Agarwal et al. (2024), Many-shot in-context learning - https://arxiv.org/abs/2404.11018 (b22)
41. [V] Yasunaga et al. (2024), Large language models as analogical reasoners - https://arxiv.org/abs/2310.01714 (b23; table partly garbled)
42. [V] Bertsch et al. (2025), In-context learning with long-context models - https://arxiv.org/abs/2405.00200 (c09, c21)
43. [V] Alazraki et al. (2025), No need for explanations - https://arxiv.org/abs/2502.08550 (c10, c22)
44. [V] Zhang et al. (2024), In-context principle learning from mistakes (LEAP) - https://arxiv.org/abs/2402.05403 (c11, c25)
45. [V] Wang et al. (2023), Voyager - https://arxiv.org/abs/2305.16291 (c12, c26; critique re-read Tables 1 and 2)
46. [V] Yang et al. (2024), Buffer of Thoughts - https://arxiv.org/abs/2406.04271 (c13)
47. [V] Wang, Mao, Fried and Neubig (2024), Agent Workflow Memory - https://arxiv.org/abs/2409.07429 (b24, c14)
48. [V] Zhao et al. (2024), ExpeL - https://arxiv.org/abs/2308.10144 (c15)
49. [V] Lekshmi-Narayanan et al. (2024), Explaining code examples: LLM vs humans - https://arxiv.org/abs/2403.05538 (c16)
50. [V] Puech et al. (2025), Pedagogical steering of LLMs, productive failure - https://arxiv.org/abs/2410.03781 (c19)
51. [V] SkillsBench (2026) - https://arxiv.org/abs/2602.12670 (d09; fetch summarizer; paper inconsistent on task count)
52. [V] Xu and Wu (2026), Skill availability and presentation granularity - https://arxiv.org/abs/2605.31408 (d10)
53. [V] Singh et al. (2026), ThinkRetrieve - https://arxiv.org/abs/2608.10928 (d11)
54. [V] Chen, Bai and Yuille (2026), The Compliance Trap - https://arxiv.org/abs/2607.10608 (d12)
55. [V] How memory management impacts LLM agents (2026) - https://arxiv.org/abs/2505.16067 (d13; fetch summarizer)
56. [V] Suzgun et al. (2025/2026), Dynamic Cheatsheet - https://arxiv.org/abs/2504.07952 (d14; fetch summarizer)
57. [V] Lei et al. (2026), SkillEvolBench - https://arxiv.org/abs/2605.24117 (d15)
58. [V] LLM Shepherding (2026) - https://arxiv.org/abs/2601.22132 (d16; fetch summarizer)
59. [V] Give me a hint (2024) - https://arxiv.org/abs/2410.05915 (d17; fetch summarizer; Table 4 has duplicated rows)
60. [V] Xiao et al. (2025), The role of diversity in in-context learning - https://arxiv.org/abs/2505.19426 (d18; fetch summarizer)
61. [M] MATE, When successful memories mislead embodied agents (2026) - https://arxiv.org/abs/2609.35808 (d19; abstract only)
62. [V] Lekshmi-Narayanan et al. (2026), Self-explanation tutor for CS1 worked examples - https://arxiv.org/abs/2608.25180 (d20)

Corrections carried from the cross-check: the Voyager 15.3x speed-up is for the wooden tool, not the deepest tier; the library helps clearly on zero-shot unseen tasks (Table 2). The AWM margin over human-written workflows is 7.6% in the results text and 7.9% in the intro. The I2S GPT-4.1 gain (+14.0) is in absolute points. Sweller and Cooper 1985 shows near transfer only; the earlier note that it failed in geometry and kinematics is from other sources (b04), not the 1985 paper.
