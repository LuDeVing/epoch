# Argument mapping training: deep document

*Subfield D05.08. Sources: evidence_a to d.jsonl (97 lines), claims.jsonl (K01 to K26), critique.md in this folder. Evidence ids (a01, b04, d09 ...) point to those files. Claim ids are D05.08-Kxx. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Argument mapping (AM) means drawing an argument as a diagram. The main claim goes on top. Each reason is a box below it. Arrows show support. Objections get their own boxes and arrows. Rebuttals sit under objections. The idea is that a picture shows the structure that text hides: what rests on what, what is missing, what is only repeated.

Argument mapping training means teaching people to build such maps, usually with software, with many practice exercises and feedback, and then testing whether their general critical thinking improves. The claim under test is a transfer claim: practice on maps raises scores on tests that are not maps.

Three things get called "argument mapping" and they must not be mixed up.

1. **Training effect.** Does a course built on map practice raise critical thinking test scores more than other courses? (Founding studies, Section 3.)
2. **Study aid.** Does reading or building a map help recall or understanding of one argument? (Dwyer experiments, a16.)
3. **LLM scaffold.** Does a model that builds an argument graph reason better, or can people or code use its graph? (Section 6.)

Key people: Tim van Gelder and colleagues (Melbourne, Reason!Able and Rationale software, the "Reason! Project"); Charles Twardy and Butchart et al. (Monash); Harrell (Carnegie Mellon, pencil-and-paper diagramming); Dwyer, Hogan and Stewart (Galway, learning-science tests of maps).

Why this matters for our agent: schema state S2 (Represent) asks for a structured restatement. The question is whether an explicit typed graph of claims, supports and objections is a better S2 representation than plain text, for which task classes, and at what token cost. The human evidence is about human training and cannot be copied over to a model. The LLM evidence is thin and shows parity with chain of thought on accuracy (K12, K18).

## 2. History and theories in depth

**Roots.** Argument diagrams go back to Wigmore (legal evidence charts) and Toulmin (claim, grounds, warrant, rebuttal). Computer tools came in the 1990s and 2000s: Araucaria (annotation), Reason!Able and later Rationale (classroom mapping), Carneades (formal evaluation), Argdown (markup rendered to maps) (c24, not opened). Dung (1995) gave the formal base for argument graphs with attack relations; modern LLM argument systems use it (c23, not opened).

**1999 to 2002: the Reason! Project (Melbourne).** van Gelder and colleagues ran a first-year reasoning course around Reason!Able and measured pre/post gains. The 1999 prototype used the Watson-Glaser test (WGCTA). A traditional semester with 32 students gained nothing (effect .02, p=.44). The mapping semester with 53 students gained effect .41 (a03, b01). Later cohorts used the California Critical Thinking Skills Test (CCTST, multiple choice, alternate forms A and B). Technical Report 2002/1 gives CCTST gains for three cohorts (b01, b02). The course asked for about 10 hours of software practice over a 12-week semester, in pairs, with weekly tutorials.

**2004: the flagship paper.** van Gelder, Bissett and Cumming (2004, Canadian Journal of Experimental Psychology) pooled two cohorts: mean gain 0.80 SD, 95% CI 0.66 to 0.94, CCTST pre 18.82, post 22.40, t(231)=14.08 (b04, re-confirmed in the critique). They argued ordinary college growth is about 0.3 SD per semester (Lehmann 0.34; Hatcher 0.28) so mapping added about 0.5 SD (b05). That discount is an estimate, not a measured control.

**2004: Twardy at Monash.** A sceptical outside group put a novice teacher on the method and got about 0.72 SD, 90% of the founder gain (b06, a05). Twardy also offered two syntactic checks for maps: the Rabbit Rule (every meaningful term in the conclusion must appear in every reason) and the Holding Hands Rule (every meaningful term in one premise must appear in another premise or the conclusion) (a24, blog-level source). These are code-checkable rules and are the one concrete "mechanism" the tradition offers.

**2007: Alvarez-Ortiz meta-analysis.** 52 undergraduate critical thinking studies. Some explicit CT taught: 0.30 SD. No explicit CT: 0.12 SD. Some mapping: 0.68 SD. Lots of mapping practice (LAMP): 0.78 SD (a01, a02, b12). The mapping subgroup is built from a few uncontrolled studies by the same cluster of advocates (Donohue 2002, Butchart 2009, Twardy 2004, van Gelder 2000 and 2001). Count it once, not as independent support. We have it only through the Dwyer thesis.

**2008 and 2011: Harrell.** Harrell tested pencil-and-paper diagramming in Carnegie Mellon introductory philosophy. The 2008 paper (Teaching Philosophy) could not be opened (d04). The 2011 paper (Higher Education Research and Development) gave two quasi-experiments with intact sections (a10, a11, d01 to d03). The author lists her own flaws. Her theory is schema-based (a12): students with no schema for reading arguments (only story or fact schemas) gain from acquiring one. Strong students already have one.

**2009: Butchart et al. (Monash).** A group with its own mapping tool and automated feedback got 0.45 SD with feedback, 0.22 without, 0.19 for the standard course, 0.40 for Peer Instruction (a07, b07, b08). The authors blamed tool flexibility, solo work and fewer hours (5 to 7 vs about 10) but did not test these.

**2011 to 2012: Dwyer, Hogan and Stewart (Galway).** A PhD thesis plus a 2012 paper. Mapping vs hierarchical outline vs control, plus experiments on studying maps. Mapping beat no instruction on some subscales but did not beat a hierarchical outline (a14 to a17, b09 to b11).

**2022 to 2026: reviews and LLMs.** Chang, Lin and Hwang (2025) scoping review of 45 studies (a18, b17). Nesbit and Liu (2025) systematic review of 124 studies, no pooled effect in the abstract (d05). Davies and Calma (2026) chapter claims a large pooled effect; Davies is a method developer and no number was read (b20, d06). From 2024 on there are LLM papers: argument mining, ArgLLMs for claim verification, graph uncertainty, and human trust studies with graphs (Section 6).

**Competing theories of why maps might work.**

| Theory | Claim | Test result |
|---|---|---|
| Practice and feedback | Gains come from many exercises with correction | Hours correlate r=.31 with gain (b04); feedback arm 0.45 vs 0.22 (b07). Both correlational or cross-semester. |
| Schema acquisition (Harrell) | Novices learn a schema of claim, reason, objection | Gain strongest for low pretest students in one of two studies (d02). Post hoc. |
| Cognitive load (Dwyer) | A map places related propositions side by side and cuts working-memory load | Prediction that maps help more under high load failed; advantage was smaller at 50 than 30 propositions (a17, a16). |
| Representation only | The diagram, not the practice, does the work | Outline matched map in recall and most CT scores (a16, b09, b10). |
| Retesting and maturation | Gains are partly or wholly test familiarity and one semester of college | Founders estimate 0.3 SD; no-map control in Dwyer 2012 rose d=.55 (a14, b05). |

## 3. Core findings with exact numbers

Effect sizes are standardised mean gains (pre to post) unless stated. "Developer" means run by authors of the method.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Founding course, CCTST, pooled two cohorts | d=0.80, CI 0.66 to 0.94, t(231)=14.08, pre 18.82, post 22.40 | van Gelder et al. 2004 (b04) | Developer, no control. Gain observed; cause not established |
| Reason! cohorts by year (manual SD 4.457; raw SD in brackets) | 2000 n=50 d=0.89 (0.84); 2001 n=114 d=0.89 (0.82); 2002 n=117 d=0.73 (0.72) | Reason! Technical Report 2002/1 (b01) | Developer. "About 0.8" slightly overstates the 2002 cohort; state which SD is used |
| WGCTA prototype, 1999 to 2000 | Traditional n=46 d=0.02; map n=53 d=0.39 to 0.41 | Reason! report; Donohue 2002 via Dwyer (a03, b01, b02) | Developer, cohorts differ |
| Comparison courses, same tests | Monash philosophy n=61 d=0.32 (CI -0.05 to 0.69); Monash 6+6 weeks n=174 d=0.27; HPS Melbourne n=42 d=0.37 | Reason! report (b02) | Different cohorts, wide CIs |
| Outside replication, novice teacher | d about 0.72 vs founder 0.8 | Twardy 2004 (b06) | Author-teacher, same test, no control |
| Independent replication with feedback | Map with automated feedback n=43 d=0.45 (CI +/-0.29), mean gain 13.7%; standard course n=65 d=0.19; map without feedback n=41 d=0.22; AOMT dispositions n=49 d=0.14; Peer Instruction n=40 d=0.40 | Butchart et al. 2009 (b07, a07) | Different semesters, not randomised. Peer Instruction overlaps the map arm; do not read as "map beats PI" |
| Gap Monash vs Melbourne | 0.35 SD, CI 0.026 to 0.675 | Butchart (b07) | Explanations untested |
| Dose | Practice hours vs gain r=.31; six practice variables explain 20% of gain variance; high users +5.17 vs low users +2.38 CCTST points (median 8.84 h) | van Gelder 2004; Reason! report (b04, b03) | Single source, correlational |
| Starting level | Pretest vs gain r=-0.54 (N=281) | Reason! report (b03) | Contested: regression to the mean |
| Follow-up retention | n=20 self-selected: pre 19.30, post 23.70, follow-up 23.70, d=0.75, over 9 months | Reason! report (b03) | Tiny, self-selected |
| Meta-analysis of CT instruction | Some CT 0.30 (CI .16 to .43); no CT 0.12 (.08 to .17); philosophy 0.26; some mapping 0.68 (.51 to .86); LAMP 0.78 (.67 to .89); computer-supported 0.49 | Alvarez-Ortiz 2007 via Dwyer thesis (a01, a02, b12) | Contested: second-hand, same advocate cluster |
| Harrell Study 1 (Spring 2004) | 35 taught vs 104 not; gain 0.22 vs 0.18; t(53)=1.35 n.s.; post-test ANCOVA F(1,133)=21.1 | Harrell 2011 (d01, a10) | Not randomised; groups differed at pretest; own test |
| Harrell Study 2 (Fall 2004) | 68 vs 62; gain 0.22 vs 0.18; t(126)=1.22 n.s.; posttest t(124)=2.67 p=.01 d=.66; ANCOVA partial eta2 .03 | Harrell 2011 (d01, a11) | Small ANCOVA effect; paper has internal mismatches (d03) |
| Harrell by pretest level | Low: 0.40 vs 0.28 (n=6 vs 32, p=.14) in Study 1; 0.39 vs 0.24 (n=24 vs 22, p=.007) in Study 2. Intermediate: 0.30 vs 0.18 (p<.01) in Study 1; 0.17 vs 0.18 in Study 2 | Harrell 2011 (d02) | Contested. The earlier "d=1.1" is a within-group pre/post figure; do not cite it as a group contrast |
| Mapping vs control, 8 weeks | n=43 vs 31; map d=.81 pre to post; control d=.55; post advantage verbal reasoning d=.61, argument analysis d=.74 | Dwyer et al. 2012 (a14, b11) | Control was no instruction; control also gained |
| Mapping vs hierarchical outline vs control | N=81 of 134; overall CT F(2,77)=1.65 p=.198; analysis F(2,77)=4.74 p=.011 partial eta2 .11; map and outline together beat control F(1,78)=8.74 p=.004 | Dwyer thesis Study 2 (a15, b09) | Control not randomised; heavy attrition |
| Studying a map, recall | Exp 4: map 9.42, outline 7.76, text summarising 4.84; map vs summarising d=1.30; outline vs summarising d=.84; map vs outline no difference; benefit shrank at 50 vs 30 propositions | Dwyer thesis Exp 1 to 4 (a16, b10) | Lab materials; recall is not reasoning |
| Dispositions | Need for cognition and motivation unchanged; reflective judgement follow-up no group effect (n 69 to 40) | Dwyer (a14, a25) | Established across two sources |
| One-group high-school study | N=71, t=7.71, d=0.91 on composite map scores | South Carolina thesis 2020 (b23) | Outcome is the map itself; no control |
| Scoping review | 45 studies; 34 quasi-experimental; 26 had under 50 participants; outcomes: achievement tests 15, map reproduction 9, essays 7; pooling impractical | Chang et al. 2025 (a18, b17, b18) | Descriptive only |
| Systematic review | 124 studies coded, 102 empirical; no pooled effect in the abstract | Nesbit and Liu 2025 (d05) | Abstract only |
| 2026 pooled review | 86 documents; "large" pooled effect; no number read | Davies and Calma 2026 (b20, d06) | Not independent; not read |
| Null result, MANCOVA | No effect of Rationale intervention on CCTST-2000 post-test | Dissertation, author unknown (b16) | Snippet only; a lead |

Two cautions. First, every large number comes from pre/post designs or cross-cohort comparisons. No randomised, actively controlled trial on a standardised critical thinking test was found (K26). Second, the CCTST is multiple choice and the course tasks look like it, so near transfer is likely and far transfer is untested (K10).

## 4. Mechanisms and models

This section turns the human findings into specifications an engineer can build. It marks which parts are supported and which are guesses.

### 4.1 The map as a data structure

A map is a rooted tree or directed graph.

- Node: `{id, text, kind}` with kind in {claim, reason, objection, rebuttal, assumption}.
- Edge: `{from, to, relation}` with relation in {supports, attacks, undercuts}.
- Linked vs convergent premises: a reason is a conjunction of its child claims (Twardy). Several independent reasons converge. Pirozelli et al. had experts rate this distinction and found it mostly handled (c07; mean 2.85 of 3).
- Validate by code: every non-root node has one parent edge; no cycles; every edge has a type; node count is under a cap.

### 4.2 Code-checkable flaw rules (Twardy)

Given nodes as sets of content terms:

- Rabbit Rule: for a reason R with conclusion C, every meaningful term in C must appear in the union of terms of R's premises. A missing term marks a gap or an ungrounded jump.
- Holding Hands Rule: every term in a premise must appear in another premise or in the conclusion. An orphan term marks an irrelevant premise.

Term extraction is the weak part. Have the model list content terms per node under a fixed prompt, then let code do the set checks. These rules come from a blog-level secondary source (a24). No study measures how often they catch real flaws. [S]

### 4.3 Training loop (human protocol)

1. Give an argument in text.
2. The student builds a map with a tool.
3. Automated or tutor feedback marks errors (automated feedback d=0.45, none d=0.22, b07).
4. Repeat for about 10 hours over 12 weeks, in pairs, with tutorials (b01, a08).
5. Test on alternate forms of a standard test.

What the loop might supply: many graded examples, near-immediate located feedback, and an explicit schema. Which of these matters is not isolated. For an agent, "feedback on a located failure" has the best analogue (G2) and the best indirect support (Section 6, Huang et al.).

### 4.4 Moderators found

| Moderator | Direction | Strength of evidence |
|---|---|---|
| Practice hours | more hours, more gain | r=.31, correlational (b04) |
| Feedback | with feedback larger | 0.45 vs 0.22, cross-semester (b07) |
| Starting level | weaker starters gain more | r=-0.54 (b03); Harrell low group in 1 of 2 studies (d02); regression to the mean is a rival |
| Tool flexibility | free editing better | speculation (a08) |
| Collaboration | pairs better | speculation (a08); not a significant moderator in van Gelder 2004 (b04) |
| Map size | bigger maps help less | Dwyer 50 vs 30 propositions (a16); LLM-map users report node overload (c05) |
| Task type | verbal gains, visual does not | Graphionale, human trust (c03) |
| Teacher | no effect shown | Twardy's novice teacher matched the founder (b06) |

### 4.5 Graph-based mechanisms in LLM work

- **Argumentative LLM (ArgLLM).** The model writes one supporting and one attacking argument per claim (depth 1) or seven arguments (depth 2). It scores each. Code aggregates by a formal bipolar semantics (DF-QuAD or QE). The final strength is a function of the graph, so editing a node changes the answer. Faithful for aggregation only, not for how each argument was scored (c09, c10).
- **Argument Graph Uncertainty.** Cut a reasoning trace into segments, link them with an entailment model, then compute graph features as a confidence score (b28).
- **Graph of Verification.** Turn a reasoning chain into a DAG of blocks. Check each block with only its premises. Flag the first wrong block (c18).
- **ArgEval.** Build one argument framework per decision option once. Score each case against it by code (d14).
- **Critical Questions of Thought.** A loop of eight Toulmin-derived questions the plan must pass before answering (d10).

## 5. What holds up

### 5.1 Established

- **Developer-run courses show large gains on the CCTST** (0.7 to 0.9 SD) across three cohorts, N=232 pooled (K01, [E]). One outside group reproduced it with the same materials (Twardy, 0.72).
- **Independent replications give smaller effects.** Butchart 0.45 (feedback), Dwyer null on overall CT vs outlining, Harrell null on overall gain (K03, [E]). Treat 0.8 SD as an upper bound.
- **No disposition change** (K09, [E]).
- **Only near transfer is shown** (K10, [E]).
- **Map size has a ceiling** (K11, [E]).
- **Graph prompting does not beat chain of thought on accuracy** (K12, [E]): GPT-4o MedClaim 0.85 direct, 0.85 CoT, 0.83 ArgLLM depth 1; depth 2 not better.
- **LLM argument mining works by component but not end to end** (K17, [E]): conclusion accuracy 92.50%, relation accuracy 80.57%; full pipeline AbstRCT span F1 59.65 vs 70.93 for a supervised model.
- **A revision step needs a located failure** (K22, [E]): GPT-3.5 CommonSenseQA 75.8 to 41.8 after intrinsic self-critique; GPT-4 GSM8K 95.5 to 89.0; oracle labels GPT-3.5 GSM8K 84.3, GPT-4 HotpotQA 49.0 to 59.0.
- **Graph structure of a trace carries a correctness signal** (K14, [E]): highest PRR in 8 of 9 models on GPQA Diamond, but not for DeepSeek-R1-Distill-Llama-70B (consistency 0.46 vs graph 0.34).

### 5.2 Contested or unproven

- **Causal effect of mapping itself** (K02, [C]). No randomised trial. The founders estimate 0.3 SD anyway. Peer Instruction gave 0.40 vs 0.45. The no-map control in Dwyer 2012 rose d=.55.
- **Mapping beats outlining** (K07, [S]). Dwyer found no consistent advantage.
- **Low starters gain most** (K05, [C]). Harrell Study 1 low group p=.14 with n=6; Study 2 p=.007; intermediate group flipped.
- **Pooled meta-analytic support** (K08, [C]). 0.78 for LAMP is the same advocate cluster. The 2026 "large" pooled effect could not be read.
- **Feedback** (K06, [S]). Cross-semester only.
- **Dose** (K04, [S]). Motivated students practise more.
- **Graph add-ons that beat baselines** (K13, [C]). MArgE up to about 20% and the fact-checking framework +5.39 and +11.10 macro-F1 included a stronger scorer or adversarial retrieval. The graph is not isolated.

### 5.3 Failed or null results

- Harrell overall gain difference not significant: Study 1 t(53)=1.35, Study 2 t(126)=1.22 (d01).
- Dwyer thesis overall CT F(2,77)=1.65, p=.198 (a15).
- Dwyer: no benefit for comprehension in Experiments 1 and 2; benefit faded at delay (a16).
- MANCOVA dissertation: no effect (b16, snippet).
- AOMT disposition exercises d=0.14 (b07).
- Graphionale: visual I-RAVEN calibration got worse with graphs (c03).

### 5.4 Interventions that worked and did not

| Worked (with caveats) | Did not work |
|---|---|
| Heavy, guided map practice with feedback on the CCTST (developer data) | Mapping without feedback (0.22) |
| Pencil-and-paper diagramming for low pretest students in one study | Mapping vs outlining for recall or most CT scores |
| Studying a map vs reading text for immediate recall (d=.34 colour, .28 mono) | Maps for comprehension or delayed recall |
| Graphs of LLM rationales on hard verbal items (human trust calibration) | Graphs on visual items; on easy items |
| Located-failure feedback (LLM) | Intrinsic self-critique (LLM) |

## 6. Language models

**Bottom line.** No study tests an LLM on van Gelder-style mapping training, or measures whether LLM-built maps raise the same LLM's accuracy at equal tokens against a free outline (K18, [S]). The search was thin (rate limits), so this is absence found, not proof. The nearest studies fall into groups.

### 6.1 Graph as a scaffold for the model

| Study | Result | Caveat |
|---|---|---|
| Freedman et al. 2025, ArgLLMs, 3 claim datasets, 8 LLMs (b24, c09) | GPT-4o MedClaim 0.85 direct, 0.82 estimated confidence, 0.85 CoT, 0.74 and 0.76 for 0.5-base depth 1 and 2, 0.83 and 0.80 estimated-base depth 1 and 2. Plain 0.5-base ArgLLM usually 0.03 to 0.10 below CoT | Binary claims. Zero-shot arguments. Claimed benefit is contestability |
| Zhou et al. 2025 (b26) | Direct prompting for argument confidence beat more complex UQ methods | Abstract and intro read |
| Ng et al. 2025, MArgE (b25) | Gains up to about 20% over comparison methods with a stronger GPT-4o mini scorer; vs GPT-4o mini CoT +3.5% and +1.0% on two of three datasets; worse on MedClaim | Gain depends on scorer |
| Chen et al. 2026, ArgCheck (b27) | Macro-F1 +5.39 (MAVEN) and +11.10 (AVeriTeC) over best baseline | Includes adversarial retrieval |
| Miandoab and Sarathy 2024, pro and con generation (d09) | Mean gain over zero-shot CoT: 3.18% small, 2.72% medium, 0.95% large models (9 tasks, 10 models); best single gains 25.95% (Gemma 2B), 23.15% (Llama3 8B); Phi3 3.8B 4.62% | Not a full map; tokens not matched |
| Critical Questions of Thought (d10) | Best in 18 of 20 cells; Llama 3.1 70B reasoning 8.05 standard, 7.5 CoT, 8.4 CQoT; Nemotron 51B CoT won 7.7 vs 7.3 | 40 questions per model; GPT-4o judge; many extra calls |
| ArgEval (d14) | Qwen3-30B label-match 0.8818 vs base 0.8630; gpt-oss-20b best variant 0.8485 vs base 0.8775; variants 0.4432 to 0.8485; 2.4x fewer completion tokens at depth 2 | One medical domain, one run per variant |

Reading: accuracy is at parity, or a small gain on weaker models. Gains shrink with model size. The reliable benefits are cost (one reusable graph) and contestability (edit a node, the answer changes).

### 6.2 Graph used to verify or score a trace

- **Graph of Verification** (c18, c19). ProcessBench F1 holistic to GoV: Qwen2.5-32B OlympiadBench 35.9 to 65.2, GSM8K 59.8 to 78.1, MATH 49.4 to 72.7; Qwen2.5-72B GSM8K 75.6 to 80.3; Llama3.3-70B GSM8K 78.6 to 78.6. Synthetic triangle-sum at N=8: Qwen2.5-7B 51.5 to 70.7, 14B 62.9 to 86.8, 32B 56.3 to 91.4. Gains vary by model. [S]
- **Argument Graph Uncertainty** (b28). Nemotron-3 Nano 30B PRR 0.65 vs consistency 0.24 vs token 0.41; GPT-OSS-120B 0.56 vs 0.36 vs -0.27; blend 0.68 for Nemotron; blend improved PRR by 0.10 on MMLU-Pro and 0.09 on TruthfulQA over the stronger part. Multiple choice only; segmentation is the main variance source.
- **Trace graphs** (c20). Exploration density r=0.68, branching 0.67, convergence 0.68 with accuracy. Prompts forcing linear structure lowered accuracy: Llama-8B 44.5 zero-shot, 41.2 concise, 32.7 explanatory few-shot; Qwen3-32B 56.2/53.7/50.1. Correlational across few conditions.
- **Baseline to beat.** Self-consistency lifted GSM8K by +17.9 over CoT (d13). Any graph hint competes with this.

### 6.3 Building the map is itself unreliable

- Pirozelli et al. 2026 (a21, c06 to c08): conclusion accuracy 92.50%, span F1 75.70 (P 80.31, R 72.87), relation accuracy 80.57% on 42 textbook arguments. On benchmarks the full pipeline fell: AbstRCT span F1 59.65 vs 70.93; AAEC full pipeline component F1 22.70 vs 75.66. With gold components AbstRCT link F1 51.51 (+11.77). One seed per model, large run-to-run variation.
- Anastasiou and De Liddo 2024 (a23, c12): GPT-3.5 gave the weakest map; Gemini Advanced ignored the format and dropped all counter-arguments.
- Buckingham Shum 2024 (c13): Bing Chat wrote Argdown code that rendered a map, with invented argument schemes. Code output was more usable than direct drawing (one anecdote).
- Graphionale quality audit (c04): 180 GPT-5.4 rationale maps. Structure issues 5 (2.8%, kappa 0.94). In wrong-answer rationales, 43% had problematic or hallucinated evidence, 50% incorrect sub-conclusions, 17% missing evidence.

### 6.4 Maps as a human interface for LLM output

Graphionale (c01 to c05): N=204 valid of 223, 2x2 (graph vs text by verbal BBH vs visual I-RAVEN), rationales from GPT-5.4. Hard BBH: over-trust beta=-0.199 (p=.002), error correction +0.182 (p=.002). Collapsed over difficulty: over-trust -0.144 (p=.033), error correction +0.127 (p=.040). Easy items: not significant. Visual I-RAVEN: appropriate trust -0.165, error correction -0.233 (both p<.001). Users liked graphs more on visual items (satisfaction +0.74) and less on verbal ones (-0.76). Co-design wanted 3 to 4 layers and 3 to 5 nodes per layer (c05, 10 participants). This measures human trust, not model accuracy.

### 6.5 Post hoc justification and sycophancy

- A justification written after the verdict used a different argument scheme from the reasoning in about 20% of cases per model (9 frontier models, 200 dilemmas, failure in 18.2% of cells) (d15). A map built after the answer does not show how the answer was reached.
- LFTutor (c15, c16): a scaffolded argument tutor up to 53% above base on average; adversarial student divergence 84.0 vs 38.0; plain tutors conceded the student stance in 85% of pilot dialogues. Human check N=20. This concerns argument coaching, not maps, and links to G9 and sycophancy.
- Socratic chatbot (c17): simulated students only; no gain figures extracted.

### 6.6 Self-critique

Huang et al. (d11, d12): intrinsic self-correction lowers or leaves flat accuracy; oracle labels raise it. A map revision loop with no code-located failure falls in the harmful class.

### 6.7 What changed behaviour, by how much

- Model size: gain of argument generation 3.18% small, 0.95% large.
- Extra components (stronger scorer, adversarial retrieval): large gains, but the map is not isolated.
- Located failure vs none: GPT-3.5 GSM8K 84.3 with oracle vs 74.7 intrinsic.
- Format constraint: code-rendered Argdown beat free drawing in one anecdote.

## 7. What our agent should take

Honest summary: the human data gives no ready-to-add accuracy gain, and the LLM data shows parity with chain of thought. What transfers is a set of design constraints and a few cheap tests.

### Add now (established)

| Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|
| Do not import 0.8 SD (or LAMP 0.78) as a prior for any map step. Treat the human gain as an upper bound. | G7 | [E] | K03, K08; a07, b07, d01, a15 | Process rule for the research log |
| Add to SCHEMA 4b: "Argument-graph prompting (pro and con tree, formal aggregation) as an accuracy booster: parity with chain of thought; use only for contestability or cost" | 4b | [E] | K12; b24, b26, c09, d14 | Stops re-proposal |
| Any map or graph the agent builds is validated by code (types, no cycles, node cap) before use | G5, S2 | [E] | K11, K17; a16, c05, c06, c08 | Constraint on the open tests below |
| A revision of a map or any S2 representation must cite a code-located failing output, never a self-critique | G2 | [E] (already in schema) | K22; d11, d12 | Confirms an existing guardrail |

### Test first (not added until a test passes; see UNKNOWNS.md)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Map-first step (typed claims, supports, objections) in S2 vs plain CoT vs equal-length free outline | S2 | [C] | K02, K18, K20, K21; d09, d10 |
| Gate the map step on difficulty or sample disagreement; skip on easy items | S0, S2, G1, G12 | [C] | K05, K16; c02, d02, d09 |
| Typed graph vs flat bulleted decomposition | S2, O3 | [S] | K07; a16, b09 |
| Build the map before the answer and check by code that the final choice follows from it | S2, S8, G10 | [S] | K25; d15 |
| Located-failure revision of a map vs self-critique | S5, G2 | [S] | K06, K22; b07, d11, d12 |
| Graph features of a trace as a selection hint in S7 vs sample consistency | S7, G4, G10 | [E] signal, [S] as selector | K14, K23; b28, c20, d13 |
| Step-DAG verifier at S8 vs holistic verifier | S8, G3 | [S] | K15; c18, c19 |
| One reusable argument framework per task class, scored by code (cost saver) | memory (class record) | [S] | K24; d14 |
| Twardy-style term-overlap checks (Rabbit, Holding Hands) as code flaw detectors | S4, S8 | [S] | a24 |
| Cap map size and test accuracy as nodes grow | S2 | [E] ceiling in humans, untested in LLMs | K11; a16, c05 |
| Task-class scoping: verbal logic yes, visual or perceptual no | S0, S2 | [S] | K16; c01 to c03 |

## 8. Concrete tests on our bench

All arms use the same total token budget per item (G7). Setup cost counts. Report accuracy, tokens per state, parse-failure rate and flips right to wrong and wrong to right (SCHEMA section 6).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 map-first | Hard verbal reasoning with a code-checkable answer (BBH-style logic, GPQA-style multiple choice, our Brainteaser set) | A plain short CoT; B CoT plus typed map (claims, supports, objections, code-validated); C CoT plus equal-length free outline | Accuracy; B minus C is the map-specific effect | B about equal to A on a strong model (K12); B minus C near zero unless typed structure matters. Small gain only on weaker passes (K20) |
| T2 gate | Mixed easy and hard items from T1 | A map always; B map only when 2 plain samples disagree or the class pass rate is under a threshold; C no map | Accuracy per token | B at least as accurate as A at fewer tokens; map hurts or does nothing on easy items (c02) |
| T3 map before vs after | Items where the answer follows from structure | A map then answer, code checks the answer matches the map's root conclusion; B answer then map | Rate of mismatch between map and answer; accuracy | Mismatch about 20% for B (d15); A lowers it |
| T4 located-failure revision | Items with a test or checker | A revise the map from the failing output; B self-critique the map; C no revision | Accuracy after 2 rounds | A above C; B at or below C (d11) |
| T5 selection hint | N=8 samples, multiple choice | A pick by sample consistency; B pick by graph features of each trace; C blend | Accuracy of the selected sample; PRR | Blend above either alone (b28); B below A for some models |
| T6 step-DAG verifier | Math or logic traces with known first-error step | A holistic check; B DAG check of each step given only premises | First-error F1 | B above A for mid-size models; none for others (c18) |
| T7 reusable framework | A fixed task class with many items | A per-item reasoning; B one class-level argument framework built once with code scoring | Accuracy and tokens over the class | Same accuracy at about 2x fewer tokens (d14) |
| T8 size cap | Long arguments (30, 50, 80 propositions) | Full map vs pruned map at equal tokens | Accuracy by node count | Gain shrinks past a node ceiling (a16) |
| T9 transfer | Tune the map prompt on class X, test on class Y | Tuned prompt vs plain | Accuracy on Y | Near zero transfer (K10) |
| T10 flaw rules | Arguments with planted gaps and planted irrelevant premises | A code term-overlap check; B model critique | Detection rate and false alarms at equal tokens | Unknown; pilot only |

## 9. What does not transfer, and why

- **The 0.8 SD figure.** It is a human pre/post gain on a multiple-choice test with no randomised control. A model has no course, no retest effect, no maturation. Nothing in it predicts an LLM effect.
- **Dose by hours of practice.** A model does not learn from map practice across items. Only in-context examples and the class memory carry anything forward.
- **Schema acquisition (Harrell).** Novices lack an argument-reading schema. A trained model already has one. "Weak starters gain most" may map onto "weaker models gain most" (d09), but that is an analogy.
- **Disposition effects.** None were found in humans (K09). There is nothing to shift in a model.
- **Cognitive load reasoning.** Working-memory limits do not bind a model the same way. The relevant limits are context length, attention dilution and parse errors.
- **Human trust calibration.** Graphionale tests how people read graphs. Our agent does not read its own map as a human does. It matters only for outputs a person reads (K16).
- **Recall benefits of reading a map.** Dwyer's recall gain is for human memory.
- **Peer and group mapping.** Collaboration and tutorials have no single-agent analogue, and G9 rules out debate.

## 10. Open questions

1. Is there any randomised, actively controlled trial of mapping on a standardised test? None found (K26).
2. What is the pooled effect in the 2025 and 2026 reviews, after removing developer-authored and conference studies? Not read.
3. Does a map-first step beat plain CoT and an equal-length outline at equal tokens on a held-out class? Not studied in LLMs (K18).
4. Does the benefit appear only where the plain attempt is inconsistent (a gate)? Human evidence is mixed (K05).
5. Is the harm to maps from size or from parse errors? (K11, K17.)
6. Do graph features of a model's own trace beat sample consistency at S7, across models? (K14, K23.)
7. Is the feedback effect (0.45 vs 0.22) real, and does it translate to located-failure revision? (K06, K22.)
8. How far does transfer go beyond the training task class? (K10.)
9. Harrell 2008 numbers are unread; a review's "180 students" description looks wrong.
10. Have Rationale, Carneades or Argdown been used in deployed agent loops with a measured benefit? None found.

## 11. Sources

[V] opened and read in this study; [M] seen as snippet or abstract only.

**Human studies and reviews**

- [V] Donohue, van Gelder, Cumming, Bissett (2002) Reason! Project Studies 1999-2002, Technical Report 2002/1. https://www.reasoninglab.com/wp-content/uploads/2025/10/ReasonProjectReport2002_1.pdf (b01 to b03)
- [V] van Gelder, Bissett, Cumming (2004) Cultivating expertise in informal reasoning. https://www.reasoninglab.com/wp-content/uploads/2013/10/ (URL is truncated in the evidence file; search the title on reasoninglab.com) (b04, b05)
- [V] Twardy (2004) Argument maps improve critical thinking. https://web-archive.southampton.ac.uk/cogprints.org/3008/1/reasonpaper.pdf (b06)
- [V] Butchart et al. (2009) Improving critical thinking using web based argument mapping exercises with automated feedback. https://ajet.org.au/index.php/AJET/article/download/1154/402 (a07 to a09, b07, b08)
- [V] Harrell (2011) Argument diagramming and critical thinking in introductory philosophy (copy, first 100k of 142k characters). https://ndownloader.figshare.com/files/11932493 ; https://www.slideshare.net/WhitneyAnderson18/argument-diagramming-and-critical-thinking-in (a10 to a13, d01 to d03). Published version [M]: https://doi.org/10.1080/07294360.2010.502559
- [M] Harrell (2008) No computer program required. https://philpapers.org/archive/HARNCP-2.pdf (b14, d04; blocked)
- [V] Dwyer (2011) PhD thesis, The Evaluation of Argument Mapping as a Learning Tool (also gives Alvarez-Ortiz 2007 and Donohue 2002 second-hand). https://researchrepository.universityofgalway.ie/server/api/core/bitstreams/af245e81-93a3-40c9-8543-7d2e54f65dfe/content (a01 to a06, a14 to a17, a25, b09 to b12)
- [M] Dwyer, Hogan, Stewart (2012) Metacognition and Learning. https://eprints.teachingandlearning.ie/id/eprint/4011/ (b13)
- [M] Dwyer 81-student controlled trial summary (snippet, d08)
- [V] Davies, Barnett, van Gelder (2015) Using computer-aided argument mapping to teach reasoning (introduction only). https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/f891a7a2-1bfb-5ba6-8800-b (b21; URL truncated)
- [V] Chang, Lin, Hwang (2025) Charting the field, Frontiers in Education. https://public-pages-files-2025.frontiersin.org/journals/education/articles/10.3389/feduc. (a18, b17, b18; URL truncated)
- [V] Nesbit and Liu (2025) Argument Mapping in Higher Education: a systematic review (abstract via Crossref). https://doi.org/10.1111/hequ.70063 (b19, d05)
- [M] Davies and Calma (2026) Argument mapping improves critical thinking skills, Routledge chapter. https://doi.org/10.4324/9781003540496-15 (b20, d06)
- [M] Doctoral dissertation, Rationale and MANCOVA on CCTST-2000 (author unknown). https://harbor.klnpa.org/iup/islandora/object/iup%3A213/datastream/PDF/view (b16)
- [V] Chen, Wang, Zhai, Li (2022) Argument map-supported online group debate. https://doi.org/10.3389/fpsyg.2022.856462 (a19)
- [V] Frontiers in Psychology (2022) digital concept mapping quasi-experiment. https://www.frontiersin.org/articles/10.3389/fpsyg.2022.882370/full (d07)
- [V] South Carolina thesis (2020) high-school guided mapping. https://scholarcommons.sc.edu/etd/6079 (b23)
- [V] Narra (2026) Pedagogic applications of argument maps. https://aclanthology.org/2026.teachingnlp-1.2.pdf (a20, b22)
- [V] Twardy rules via LessWrong. https://www.lesswrong.com/posts/NJ8k2RTwy3ELmwYZT/argument-maps-improve-critical-thinking (a24)

**LLM and AI studies**

- [V] Freedman et al. (2025) Argumentative LLMs for explainable and contestable claim verification. https://ojs.aaai.org/index.php/AAAI/article/download/33637/35792 ; https://arxiv.org/abs/2405.02079 (b24, c09, c10)
- [V] Ng et al. (2025) MArgE. https://arxiv.org/pdf/2508.02584 (b25)
- [V] Zhou et al. (2025) UQ in Argumentative LLMs. https://aclanthology.org/2025.findings-emnlp.1184.pdf (b26; abstract and intro)
- [V] Chen et al. (2026) ArgCheck. https://aclanthology.org/2026.emnlp-main.1207.pdf (b27; abstract and first figure)
- [V] Baur et al. (2026) Argument Graph Uncertainty. https://arxiv.org/pdf/2610.20328 (b28)
- [V] Wang et al. (2026) Graphionale. https://arxiv.org/abs/2608.27932 (c01 to c05)
- [V] Pirozelli et al. (2026) LLM-based argument mining. https://arxiv.org/pdf/2605.13793 (a21, c06 to c08)
- [V] Li et al. (2025) LLMs in argument mining: a survey. https://arxiv.org/pdf/2506.16383 (a22, b29, c21)
- [V] Anastasiou and De Liddo (2024) Hybrid human-AI argument map creation. https://aclanthology.org/2024.delite-1.6.pdf (a23, c12)
- [V] Crudele and Raffaghelli (2025) Argument mapping and ChatGPT. https://je-lks.org/ojs/index.php/Je-LKS_EN/article/view/1136130 (c11)
- [V] Buckingham Shum (2024) Generative AI for critical analysis. https://ceur-ws.org/Vol-3667/GenAILA-paper4.pdf (c13)
- [M] UMSL thesis (2025) LLM argument maps from essays. https://irl.umsl.edu/thesis/496 (c14)
- [V] Shi et al. (2026) LFTutor. https://arxiv.org/abs/2606.01020 (c15, c16)
- [V] Pal Chowdhury et al. (2024) Socratic chatbot. https://arxiv.org/abs/2409.05511 (c17)
- [V] Fang et al. (2025) Graph of Verification. https://arxiv.org/abs/2506.12509 (c18, c19)
- [V] Wang et al. (2025) Mapping the minds of LLMs. https://arxiv.org/abs/2505.13890 (c20)
- [V] Bhatia et al. (2026) Guided Sensemaking. https://arxiv.org/abs/2606.02260 (c22)
- [V] Miandoab and Sarathy (2024) Let's argue both sides. https://arxiv.org/abs/2410.12997 (d09)
- [V] Critical-Questions-of-Thought. https://arxiv.org/abs/2412.15177 (d10)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d11, d12)
- [V] Wang et al. (2023) Self-consistency. https://arxiv.org/abs/2203.11171 (d13)
- [V] Dejl, Williams, Toni (2026) ArgEval. https://arxiv.org/abs/2603.14643 (d14)
- [V] Henselmans et al. (2026) Measuring AI accountability through argumentation analysis. https://arxiv.org/abs/2609.05088 (d15)
- [V] arXiv search pages for "argument map" LLM (d16). https://arxiv.org/search/?query=%22argument+map%22+LLM&searchtype=all
- [M] DeceptionAnalyser (2026). https://arxiv.org/abs/2609.24369 (d17)
- [M] Dung (1995) On the acceptability of arguments. https://doi.org/10.1016/0004-3702(94)00041-X (c23)
- [M] Argument mapping tools (Araucaria, Rationale, Carneades, Argdown). https://argdown.org (c24)

**Links to other subfields (not covered here):** Argumentation and defeasible rules; Pragma-dialectics; Working-memory-limited mapping; Debiasing; Structured analytic techniques; Novices and education; Forward and backward reasoning.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 8 established claims: 2 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D05.08-K03** (reworded: the sources support less). Harrell's abstract and the split-by-pretest data show gains for low- and intermediate-pretest students (intermediate in Study 1 at least), not only low-pretest students; other numbers (Butchart 0.45/0.19, Dwyer F(2,77)=1.65) verified. Corrected claim: Independent replications give smaller effects than the developers: Butchart (Monash, 2009) 0.45 SD with automated feedback and 0.19 for the standard course; Dwyer (thesis) found no overall CT gain from mapping over hierarchical outlining or controls; Harrell found no significant overall gain difference (0.22 vs 0.18 in both studies; t(53)=1.35; t(126)=1.22) and gains concentrated in low- and intermediate-pretest students; one MANCOVA dissertation (snippet only) found no effect.
- **D05.08-K09** (reworded: the sources support less). Dwyer's data show no mapping effect on need for cognition, motivation or reflective judgement in his own studies, but Butchart's d=0.14 is the CCTST gain of non-mapping AOMT exercises, not evidence about mapping and dispositions; a general 'mapping does not change dispositions' is wider than two small Dwyer samples. Corrected claim: In Dwyer's studies (one lab, small samples) argument mapping did not change need for cognition or motivation, and the six-month reflective-judgement follow-up (N=40) showed no group effect; in Butchart et al. the separate actively-open-minded-thinking exercises (not mapping) produced only d=0.14 on the CCTST.
- **D05.08-K10** (reworded: the sources support less). Chang et al. report outcomes as achievement tests (15 of 45), map reproductions (9) and essays (7), with 26 of 45 studies under 50 participants; they do not say outcomes are mostly perception scores. d=0.91 (N=71, one-group) and follow-up n=20 verified. Corrected claim: Only near transfer is shown: outcomes are the CCTST, map scores themselves (d=0.91, N=71, no control) or recall; follow-up retention rests on a self-selected n=20; a 2025 scoping review of 45 studies finds outcomes are mostly achievement tests (15), map reproductions (9) and essays (7), mostly quasi-experimental, with 26 of 45 studies under 50 participants.
- **D05.08-K11** (reworded: the sources support less). In Dwyer's thesis Experiments 1 and 3 recall was lower for 50- than 30-proposition arguments in both formats, but there was no size x study-material interaction, so the map advantage did not significantly shrink; the 'size ceiling' reading is unsupported. Graphionale formative sessions (10 participants) do report node text overload and navigation cost. Corrected claim: Larger arguments were recalled worse than 30-proposition ones in both map and text formats (Dwyer, no size x format interaction, so no significant shrinkage of the map advantage), and in a formative study with 10 participants, users of LLM rationale graphs reported node text overload and navigation cost on large diagrams.
- **D05.08-K12** (reworded: the sources support less). GPT-4o MedClaim values (0.85 direct, 0.85 CoT, 0.83 ArgLLM D1 est base) and Zhou's direct-prompting result verified, but Freedman Table 1 has cells where est-base ArgLLM beats CoT (e.g. Llama 3 8B StrategyClaim 0.81 vs 0.76), so 'at best equal' is too strong. Corrected claim: Using a pro/con argument graph with DF-QuAD aggregation (ArgLLM) gives accuracy comparable to direct prompting and chain of thought, not reliably better: GPT-4o MedClaim 0.85 direct, 0.85 CoT, 0.83 ArgLLM depth 1 (Freedman et al. Table 1); 0.5-base ArgLLM is usually below CoT; depth 2 is usually no better; a separate study (Zhou et al.) found direct prompting outperformed more complex uncertainty-quantification methods inside ArgLLMs.
- **D05.08-K17** (reworded: the sources support less). Pirozelli numbers (92.50, 80.57, 59.65 vs 70.93) and the exact-span penalty verified, but the evidence is one workshop paper (listed three times) on 42 textbook arguments, and the survey text does not say few studies test quality in downstream pipelines; c21 and a22 are the same survey. Corrected claim: In one LLM argument-mining pipeline (Pirozelli et al. 2026, a workshop paper), component-level results on 42 textbook arguments are good (conclusion detection accuracy 92.50%, relation accuracy 80.57%) but the full pipeline on AbstRCT scores span F1 59.65 vs 70.93 for a supervised model, and exact-span scoring penalises small boundary deviations.
- **D05.08-K22** (now single-source: only one opened source, code check).
