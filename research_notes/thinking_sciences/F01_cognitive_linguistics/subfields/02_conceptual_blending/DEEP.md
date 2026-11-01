# Conceptual blending: deep document

*Subfield F01.02 of cognitive linguistics. Built from evidence_a-d.jsonl (a01-a33, b01-b25, c01-c25, d01-d25), claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids in brackets point to those files. Written 2026-11-01.*

Bottom line up front. Blending theory gives a clean, named list of steps. It has almost no controlled evidence that the steps help anyone solve anything. The human lab work is a few small studies (N=10 to 36). The model work is mostly image and idea-generation tools tested by their own authors. The one strong measurement for language models (KOMBINE) says unaided models fail mostly at one step: finding a valid generic space. No study tests a blend step against plain chain of thought at equal tokens. So blending is a design hypothesis for O7 and S3 open mode, not an established gain.

## 1. What it is

Conceptual blending (also "conceptual integration") is a model of how two mental structures are merged into a third that has new structure. It was set out by Fauconnier and Turner (1998, Cognitive Science 22(2); expanded web version 2001) [a01]. The forerunner is Koestler's "bisociation" (1964): joining two frames of thought that did not belong together into a new matrix of meaning [a14, a13].

The network has four spaces [a01, a15]:
1. Input space 1 and input space 2: the two things being combined.
2. Cross-space mapping: counterparts between the inputs (mountain to mountain, mover to mover).
3. Generic space: what the inputs share, stated abstractly (a mover on a path on a day, with no direction and no date).
4. Blended space: gets selected structure from both inputs and can hold structure that neither input has.

Three operations build the blend [a03]:
- Composition: put elements of the inputs together. This creates relations neither input had.
- Completion: pull in background frames by pattern completion. The blend gets filled out by a known frame.
- Elaboration: run the blend as a mental simulation. It can go on indefinitely.

Projection is selective [a04]. Most input detail is dropped. The calendar date of the monk trip is dropped. In the "debate with Kant" blend, Kant's German, his death and his ignorance of the professor are dropped.

The standard worked example is the Buddhist monk riddle [a02]. A monk walks up a mountain one day and down the same path another day. Is there a spot he passes at the same time of day? Put the two days on one path. Now two walkers must meet. The meeting spot answers the question for the original trip. Composition gives two walkers on one path. Completion supplies the familiar "two people walking toward each other" frame. Elaboration runs it and finds the meeting. The result is then read back onto the inputs.

Network types (simplex, mirror, single-scope, double-scope) have their own sibling subfield. Here only the useful distinction is kept. A single-scope blend takes its frame from one input. A double-scope blend merges both frames [a15, a31].

Why it matters for our agent: SCHEMA O7 ("map an analogue") and S3 open mode (generate attempts far from the typical answer) both combine two sources. Blending offers a step list: find the shared frame, map, choose what to carry over, compose, complete, run, check. This document asks which of those steps have evidence behind them.

## 2. History and theories in depth

### 2.1 Forerunners
Koestler (1964), Goffman (1974), Talmy (1977), Fong (1988), Moser and Hofstadter, and Kunda, Miller and Clare (1990) are named by Fauconnier and Turner as forerunners. They say these authors treated blends as exotic and that blends are in fact central and pervasive [a13]. Only Kunda et al. (1990, combined social categories) is experimental, and it was not opened. Bisociation, as described on its encyclopedia page, says jokes work by a punch line that switches the frame, and discovery fuses two frames [a14]. That page gives no data.

### 2.2 The founding paper (1998/2001)
The paper builds the model from hand-picked cases and runs no experiment [a01]. Cases: the monk riddle, debate with Kant, the 1993 catamaran Great America II against the 1853 clipper Northern Light (a live "race", with a 4.5 day lead as the emergent claim) [a06], the computer desktop, "birth is arrival" with the stork and diaper [a09], and "this surgeon is a butcher" (incompetence, which is in neither input) [a11].

Key ideas in the paper:
- Optimality principles: Integration, Topology, Web, Unpacking, Good reason. They compete with each other. They are qualitative and unscored [a07]. The 2002 book added governing principles in reply to critics [b19].
- Frame networks: when inputs share an organising frame, mapping is easy. Topology splits into shared frame, differing frame values, and incidental features. Features can be promoted or demoted as the network is built [a10].
- Compression of vital relations (time, space, cause, change, identity) into tight relations inside the blend. Blends can be nested: an output feeds another blend as input [a09].
- A claim against structure mapping (Gentner 1983): analogy is not compositional, mapping depends on content, projection comes in gradients. This was argued by example. Structure-mapping researchers dispute it [a11].
- A claim by the authors themselves that blending is not a compositional, algorithmic process and cannot be modelled as one even for rudimentary cases. They compare it to biological evolution [a08]. This is a warning for anyone who wants a coded operator.
- A navigation anecdote: a Micronesian navigator reportedly solved a diagram problem by imagining sailing both directions at once (Hutchins 1995, from Lewis 1972). One anecdote, second-hand [a12].

### 2.3 Criticism
- Gibbs (2000): the framework is not stated so it can be tested or falsified; inferring process from products is shaky; rival theories explain the same cases. Not opened; reported by Ritchie, Glebkin and Wikipedia, which agree [b06, a15].
- Ritchie (2004): the four-space picture comes from "space" and "blend" metaphors. Existing evidence fits blending but does not separate it from rivals. The model needs a stopping rule. Activation and suppression accounts, and ordinary memory use, could explain the examples. Read through a summariser, so exact wording is unverified [b05].
- Glebkin (2013): the flagship examples mostly compress known structure into a form people can hold; the theory "did not rest on any experimental data". Lists five other objectors (Gibbs 2000, Harder 2003, Brandt 2005, Oakley and Hougaard 2008, Ferguson and Sanford 2008) [b03].
- Yin (2026) calls blending "largely descriptive" and offers an interference account. Low weight [b18].
- Fauconnier and Turner's reply (2002) added governing principles. Glebkin notes it is not clear how to apply them in practice [b19].

The common point: the theory names results after the fact. G7 and G8 in our schema already say what to do: demand a measured gain at equal tokens.

### 2.4 Education and physics
Bing and Redish (2006/2007) used blending to describe physics students mixing math and physics. Single-scope blends use the math frame and import little physics. Projecting the result back onto the physical input exposed an error: 47,500 seconds for a 500 ft trip. The same student got about 2 seconds once simple numbers cued the physical input. Blends showed inertia: a student in a single-scope blend tends to stay there until strong new evidence or a prompt moves them. Qualitative video cases, no counts, no inter-rater check [a31, a32]. Dreyfus, Gupta and Redish (2014) describe a professor and one student coordinating two energy metaphors (substance and vertical location) from speech and gesture. Two cases, no counts [a33].

### 2.5 Computational blending
- Shrager (1980s), Guhe et al. (2011, basic mathematics) and Lieto and Pozzato (2019, 2020, typicality logic) are listed on Wikipedia. No quantitative evaluations on that page [b07, a15].
- Divago (Pereira and Cardoso 2003; Pereira 2006): knowledge base, mapper, blender, and a constraint-based factory searching with a genetic algorithm. Horse-bird and boat-house demos. Not opened [b23, c24, d21].
- Eppe et al. (2018, COINVENT): input spaces as logical theories, generic space found by generalising inputs as a search problem (answer set programming), blends pruned by optimality principles and a consistency prover. Proof of concept in mathematics and music. No baseline, no numbers. Abstract and record page only [c23, d21].
- VisiBlends (Chilton, Petridis and Agrawala, CHI 2019): a human-in-the-loop workflow (pick concepts, find symbols, find images with a shared shape, merge). A university press release reports 96% success with the tool against 21% without. Press release only, design unverified [c25, d22].
- Gomez-Ramirez and Turner (2026, CogSci poster): formalises a blend along a generic space as partial mappings plus selective projection; proposes a blend-aware training loss. A proposal with no data and outside our no-training rule [d13].

Takeaway: classical systems are demonstrations judged by example, not controlled tests [K27].

### 2.6 Recent LLM-era use
- Sato (2025) maps prompts to blends and names "prompt-induced transition" and "prompt-induced hallucination". The review itself has no measurements [a30, b16, c07, d20]. The measured version is in 2505.00557 [d05].
- Lynn (2026): in humans a goal selects which features project into the blend; in LLMs the goals come from the prompt and alignment. Conceptual, plus a toy vector-symbolic script, no data [b17, c19, c20, d12].
- KOMBINE (Schapiro et al. 2026): the first large blending benchmark for LLMs [a29, a24].

## 3. Core findings with exact numbers

Status key: established = two or more independent sources or a plain structural fact; single-source; contested; human-only; older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Blend model: inputs, generic space, mapping, blend; composition, completion, elaboration | No experiment, no sample; about 2,300 lines of argument built on hand-picked cases | Fauconnier and Turner 1998 [a01, a03] | Established as a description; no test |
| Selective projection: most detail dropped | Monk: date dropped. Kant: language, death, time dropped. No rule for what to drop | [a04, a05] | Single-source (authors' cases) |
| Blends are not unique | Regatta: several valid readings (different offsets, courses) | [a06] | Single-source |
| Theory is hard to falsify | Named critics: Gibbs 2000, Ritchie 2004, Glebkin 2013 and five others | [b03, b05, b06, a15] | Established (3 critics) |
| N400 grows from literal to literal-mapping to metaphor | N=18 (14 men, 4 women, mean 26); 165 triplets; sentence effect F(2,34)=3.90, p<.05; metaphor vs literal F(1,17)=6.86, p<.02; literal mapping vs either not significant (F=2.03, 2.18). Linear trend over 98% of condition variance; alternative coding (1,1,3) about 40%. Metaphoricity ratings 1.4, 1.9, 4.4 | Coulson and Van Petten 2002 [a16, a17, b01, b02] | Single-source, human-only; fits blending and rival accounts |
| Partial replication of Pynte et al. 1996 (French metaphors) in English | Metaphor-literal N400 gap reproduced; middle condition new | [a18] | Single-source |
| Privative "fake X" phrases cost accuracy | N=36, pre-registered. Privative vs single-word OR -2.61, p=.004; vs subsective OR -4.48, p<.0001; subsective vs baseline p=.20 | MEG/EEG privative study 2026 [b08] | Contested (negation or type-shift rival) |
| Counterfactuals: as-if space held briefly, then suppressed | Exp 1 N=60 (54 analysed): interaction F1(1,53)=8.60, p=.005; Exp 2 N=40; Exp 3 61 analysed, t1(60)=3.25, p=.002 | de Vega et al. 2007 [d09] | Single-source; does not test operation order |
| Real-world knowledge leaks into a counterfactual context at once | 3 eye-tracking experiments, 36 each; first-pass F1(2,35)=5.2, p<.01; counterfactual-consistent vs real-world-inconsistent ts<0.2 | Ferguson and Sanford 2008 [d10] | Single-source |
| Counterfactual studies do not contradict the order composition, completion, elaboration | Neither tests it; the earlier "contradicts" claim was second hand (Glebkin) | [b04, d09, d10] | Established (as "does not contradict") |
| Students' math-physics blend persists until prompted | 47,500 s vs about 2 s once numbers cued physics. Cases only | Bing and Redish 2007 [a31, a32] | Single-source, human-only |
| LLMs: blends harder than analogy or association | 35 models, valid: blend 43.4%, analogy 53.4%, association 59.0%. Cross-task r: assoc-analogy 0.71, analogy-blend 0.70, blend-assoc 0.54. Top blend model 64.8% (analogy 55.4%) | KOMBINE [a24, a25, b13] | Single-source (one preprint, LLM-judged) |
| Humans on the same tasks | N=75 Prolific, 5 items per task, skipped scored zero: association 22.1%, analogy 32.9%, blend 12.8% | KOMBINE [a28] | Single-source, human baseline is weak |
| Abstraction bottleneck | Valid generic space 43.4% of items; coherent blend given a valid one 97.1%. (The two 43.4% figures are one number.) | KOMBINE [a26, b13, b15, b24] | Single-source |
| Bottleneck depends on the model | Valid generic space: gpt-5.6-sol 83.3%, gemini-3.1-pro 83.3, gpt-6-astra 73.3, gemini-3.7-flash 70.0, claude-fable-5 60.0, claude-opus-4.6 56.7, deepseek-r1 43.3, claude-sonnet-5 40.0, deepseek-chat 40.0, gpt-4o-mini 16.7, phi-4 6.7. About 30 blend items per model (inferred). Reasoning variants do not clearly win (deepseek-r1 composite 30.4 vs chat 28.1, v3 20.1) | KOMBINE Table 10 [d01] | Single-source |
| LLM judge reliability on blends | ICC(2,3) over 1,023 artifacts: blend integration 0.67, blend utility G(g) 0.67, V(c) 0.48, analogy 0.56 and 0.55. Human check: 60 items by one author, 66% agreement with majority, 75% on unanimous (n=96). Ranking Spearman 0.945 (n=21 models) | KOMBINE [a24, d02] | Single-source |
| Different LLMs invent the same blends | 19.9% (412/2,070) of concepts reuse another model's property at k=2 (cosine 0.674); blends vs analogies 37.3% vs 2.6% (14.3x); 94.7% vs 36.3% at k=1; same provider 9.3% vs 4.1% (2.3x); DeepSeek +12.2 pp, Anthropic +11.1 pp, OpenAI -1.4 pp | KOMBINE [a27, b14] | Single-source |
| Open-ended homogeneity is general | 26K queries, 70+ models. Same model at T=1.0: 79% of cases above 0.8 similarity. Min-p: 61.2% of pairs above 0.8. Between models 71-82% | Artificial Hivemind [d11] | Single-source; not blend-specific |
| Single LLM blend suggestions are right about 56% of the time; five give a good one 90-97% | Connecting concepts relevant: 56.0 / 55.3 / 58.7% (no / half / full GPT); at least one in five: 90.0 / 96.6 / 93.3%; kappa .43 and .48; scene related 98.3%; product scenes 89.1% vs pop-culture 75.9%; GPT-3 attributes 2.86/5 (57%): adjectives 79%, activities 58%, catchphrases 35% | PopBlends [a19, a20, b10, c01-c03] | Single-source; GPT-3 era |
| LLM blend tool raises idea count and lowers strain | N=10 within-subject: 2.03 (SD 0.84) vs 0.87 (SD 0.56) ideas per pair, Wilcoxon p<0.001; mental demand 2.85 vs 5.80 (p=0.004); effort 3.05 vs 5.00 (p=0.006); frustration 1.65 vs 3.25 (p=0.026); baseline web search | PopBlends [a21, c04] | Established as "tools raise idea counts" (3 tool studies); weak on quality |
| Creative Blends | N=24, SUS t(23)=-2.547, p=0.018, d=0.800; other table cells unreliable (a printed t of -4.861 on the wrong row) | Sun et al. 2025 [b11] | Single-source; only SUS safe |
| Scideator facet recombination | N=22; CSI median 70.50 (Q1 57.50, Q3 79.00) vs 61.00 (Q1 42.25, Q3 71.50), Wilcoxon V=208.5, p<.01; rated newness gain 0.5 on 7 points | Radensky et al. 2026 [c08, c09] | Single-source; self-report |
| Harmony blending tool | N=25; more unexpected harmonies; composers' index fell 5.8 to 4.7 with the tool; no effect survives correction; no independent quality rating | CHAMELEON [b09] | Single-source |
| Misty UI blending | 14 developers; 103 operations (global 36, drag 35, regenerate 19, semantic diff 9, code 4); 36.3 min (SD 7.0); satisfaction 3.2/5 (SD 1.3); no control | [c18] | Single-source |
| Explanation step in visual-mashup prompting | 666 expert mashups; implication winning rate: experts 78.3, GPT-4o 73.5, GPT-4V 71.9, Gemini-1.5-Pro 71.7, Claude-3.5-Sonnet 62.9, average humans 51.0, Claude-3-Opus 39.2, LLaVA-1.5-7B 20.1. Generation rank IEI 1.98 vs II 2.40 (50 raters). IEI won with a shorter prompt in 46.0% of wins. GPT-4o judge agreed with experts 85.1 / 81.6% | CreativeMashup [b12, b24] | Single-source; own-model judge |
| Fusion mashups identified better than replacement | 9 of 11 models, plus people; per-type values only in a figure; figure caption contradicts body text | [b25, d04] | Single-source |
| Schema step in visual metaphor transfer | N=100. Full 4.47/4.56/4.51/4.74/4.76; strong one-shot CBT prompt 3.97/3.69/3.77/3.89/4.09; direct prompt 3.62/2.75/2.96/3.75/3.65; without CBT description 3.88/3.66/3.68/4.04/4.12; without transfer agent 4.01/3.71/3.83/4.33/4.25; without diagnostic 4.26/4.05/3.98/4.61/4.48. Preferred over commercial generators in 64.44-76.22% of pairs. About 8.3k tokens, 4 min 11 s per sample | Beyond Pixels [c16, c17, d06] | Single-source (authors' ablation; not equal compute) |
| Abstraction before mapping in narrative analogy | Mapping on raw text: Qwen 0.17 on 4-way MCQ (chance 0.25), ARN far analogy 0.24 (chance 0.50). With conceptual plus evaluative abstraction: Qwen 0.46, Llama 0.45 (from 0.16). Zero-shot LLM 0.37, chain of thought 0.41 | YARN [c22] | Single-source |
| Step-Back (abstraction before reasoning) | MMLU physics / chemistry: PaLM-2L CoT 65.0/75.3 vs Step-Back 73.2/81.8; GPT-4 CoT 82.9/85.3 vs 84.5/85.6 (gain 1.6 and 0.3, about one SD or less). TimeQA 40.8 vs 66.0. StrategyQA 83.6 vs 82.7 (no gain). Fixes about 40% of base errors, adds at most about 12% new | Zheng et al. 2024 [d07] | Direction supported (with d08); not a cross-input step |
| Self-generated analogies beat zero-shot CoT | Gains on GSM8K, MATH, Codeforces, BIG-Bench; larger for larger models. Cell values not extracted | Yasunaga et al. 2024 [d08] | Single-source |
| Fusing incompatible domains raises judged hallucination | Prompts matched at 29-30 tokens; six models, 3 responses each, scored 5 times by one o3 judge; one-tailed Welch t, HIPn < HIPc p<0.01; order DeepSeek-R1 highest, Gemini-2.5-Pro lowest | Sato 2505.00557 [d05] | Single-source, confounded |
| Image blends peak at the middle of an embedding interpolation | 1,000 images, 9 ratios. Blended-concept depiction 0.621 at midpoint, 0.389 averaged; mixed 0.862 and 0.471; concept A 0.152 to 1.000, concept B 1.000 to 0.265 | Matsuhira et al. 2024 [c10, c11] | Single-source; image side |
| Best diffusion blending method depends on the pair type | 2024, 23 people: mean rank switch 2.26, textual 2.54, alternate 2.61, UNet 2.68; textual best on animals 1.98. 2025, N=100: alternate over textual 0.60, switch over textual 0.61, alternate vs switch 0.51 (p=0.31) | Olearo 2024, 2025 [c12, a23] | Contested |
| IT-Blender | DINO similarity 0.837 vs IP-Adapter 0.812 vs BLIP-Diffusion 0.821; LLM-judge scores | Cho et al. 2025 [c13, c14] | Single-source, proxy metrics |
| Language models beat ConceptNet at the property step (simile data) | Precision at 1000: ConceptNet 5.90 vs best model 66.38; BERT-large P@10/100/1000 = 0.13/7.69/37.33; 66,442 pairs; table garbled | Ge and Parikh 2021 [a22, c05] | Single-source; older models only |
| Image-blend human preference | 20 descriptions; 6 questions x 3 model pairs x 20 descriptions, 9 raters per item; large models beat the GAN baseline | Ge and Parikh [c06, d16] | Single-source |
| LLM judge of blend quality is weak | Vibe Spaces: judge hits human top-1 35.7% and 31.3% (chance 25%), top-2 55.1 / 51.8%; human-human kappa 0.15-0.33. Short stories: LLM-LLM ICC .86-.94, LLM-human .43 | [d18, d19] | Single-source |
| LLMs regress to the mean in ad ideas | Over 1,000 ideas; creative features vanish first on regeneration; effect sizes not extracted | Keon et al. 2025 [c21] | Single-source |
| LLMs struggle with emergent properties of simple noun phrases | Song et al. 2025 (relayed by KOMBINE; "peeled apple" gains "white") | [a29] | Single-source, unopened |
| No large replication, no meta-analysis, no failed replication found | Human N range 10 to 36 (100 in one rating study) | [b20] | Established (as a gap) |
| No solve-rate study for the monk riddle | Nearest: NazoNazo (38 models, 201 riddles; 7.6% non-reasoning, 17.6% reasoning, about 52.9% humans on a 120-item subset; search summary only) | [d14] | Gap |
| No blending versus relevance-theory head-to-head | Sabzevari 2011 chapter is a pointer only; Hilpert 2010 not matched | [b21, b22, d15] | Gap |

## 4. Mechanisms and models

This section turns the theory and the tested pipelines into steps an engineer could code. Checks that code can run are marked CODE.

### 4.1 The blend record
Keep a structured record per blend so every later check has something to read [a01, a04, c09]:
```
inputs:      A (text + slots), B (text + slots)
frame:       shared organising frame if any (else "none": expect a weak blend)
generic:     one sentence true of both A and B (the shared structure)
mapping:     list of (a_i, b_j, role) counterparts
project:     items carried over, each tagged from A, from B, shared, or emergent
dropped:     items explicitly NOT carried over
goal:        the task goal that decides what to carry over
recruited:   background frame pulled in by completion, and where it came from
blend:       the composed scene or structure
run:         what happens when the blend is elaborated (the result)
back:        the result read back onto A and B
checks:      results of the checks below
```
The tag scheme (u, v, uv, emergent) is the one KOMBINE uses to score blends [a24]. The "dropped" list comes from selective projection [a04]. The "goal" line comes from Lynn's goal-driven view [b17, d12] and the optimality principle "good reason" [a07].

### 4.2 Pipeline (one blend attempt)
1. Slot the inputs. Rewrite each input as named parts (roles, relations). Structured inputs make later checks more reliable [c09]. Mapping on raw text embeddings was worse than chance in YARN; abstracting to roles first fixed it [c22].
2. Find the shared frame (shared-frame level in Fauconnier and Turner). If none, flag the blend as far [a10].
3. Propose the generic space: one statement true of both inputs. This is where models fail: 43.4% valid on average, 6.7% to 83.3% by model [a26, d01]. Example failure: a generic space true of bread but not of photosynthesis [a26, b15].
4. Check the generic space. CODE or a separate call: for each input, does it satisfy the statement? Ask for a witness item from each input. Do not let the proposing call grade itself (G5, G8). This check is the proposed intervention; no study tests it (K09, K21).
5. Map counterparts under the generic space (typed list).
6. Choose projection under the goal. Write "carry" and "drop" lists. Give both inputs equal weight: image blends peaked near the midpoint of the mix and one concept dominated at the extremes [c10]. Single-scope blends (one input supplies all structure) are what students fall into [a31], and "replacement" mashups are harder to read than fusion ones [d04].
7. Compose, then complete. Name the recruited frame and its source [a05].
8. Elaborate (run). A stop rule is needed: the founding paper has none and Ritchie flags this [a03, b05]. Use a step cap or a code-run result.
9. Back-project. Read the result onto each input and test it there. This caught the 47,500 second error [a31]. Also check real-world constraints, since real-world knowledge leaks in at once [d10]. Drop the as-if space after the question is settled [d09].
10. Score. CODE where the task has a run or a test. Otherwise count how many dropped items re-entered and whether both inputs are visible in the output (IT-Blender used a separate call to name which input was dropped [c14]).

### 4.3 Optimality principles as a rubric
Topology (do mapped relations survive?), Web (are links back to the inputs kept?) and Unpacking (can the inputs be rebuilt from the blend?) can be tested in code or by a separate call. Integration (is the blend a unit?) and Good reason (does every element have a role?) need a run or a test, not model opinion [a07]. No weights exist; any scoring would be our own design [b19].

### 4.4 Generate many, select in code
Blends are not unique [a06]. A single LLM blend proposal was right about 56% of the time, yet 90-97% of pairs had at least one good one in five [a20, c01]. Cross-model blends repeat each other [a27], and same-model repetition is high everywhere [d11]. So: several blend attempts, each in a fresh context (S3), varied by input framing or input choice rather than by temperature alone, and a selector in code. Image blending also shows order and seed effects [a23], so try both input orders.

### 4.5 Related tested pipelines worth copying
- PopBlends: connecting concept, then scenes on both sides, rank scene pairs by similarity in code [a19].
- Beyond Pixels: perception (extract relational invariant, carrier, violation points), transfer (re-instantiate), generation, diagnosis with backtracking. About 8.3k tokens per sample. Mean calls per stage: perception 1.14, transfer 1.25, generation 2.19, diagnostic 2.19 [c16, d06].
- Scideator: split into facets, recombine across analogous items, check novelty against retrieved literature, swap a facet if not novel [c08].
- IEI prompting: identify the two inputs, explain shared attributes, derive the implication [b12].
- Eppe et al.: generic space by search with pruning and a logic consistency prover [d21].

### 4.6 Why the checks matter
Unaided blends fall back on one input's surface (literal substitution) [c17]. Fusing incompatible domains gives fluent ungrounded text [c07, d05]. Regeneration drops the non-obvious element first [c21]. Each failure is guarded by a named step above (generic-space check, back-projection, "carry-over survived" check).

## 5. What holds up

### 5.1 Replications and failures
- No replication, failed or successful, of a blending-specific prediction was found in two search passes [b20, d15]. This is a limit of reachable sources (web search quota ran out, scholarly APIs rate-limited), not proof of absence.
- The one partial replication is Coulson and Van Petten 2002 of Pynte et al. 1996 (French metaphors), in English; the new middle condition did not differ from either neighbour [a18].
- Ranking of diffusion blending methods flipped between two panels (Olearo 2024 vs 2025) [c12, a23].
- No meta-analysis exists.

### 5.2 Human evidence is thin
Five human studies give N=18, 25, 36, 10 and 24. Coulson and Van Petten's graded N400 is consistent with blending but equally with cloze or salience accounts [b02]. The privative-adjective cost has a negation rival [b08]. Counterfactual studies show leakage and suppression but test no blend order [d09, d10]. The monk riddle has no published solve rate for or against the blend hint [d14].

### 5.3 Moderators and boundary conditions
- Shared frame: easy mapping when inputs share a frame [a10]; far pairs cost more (N400 gradient, N=18) [a17].
- Model strength: valid generic space ranges 6.7% to 83.3% across models [d01]. Abstraction scaffolds help a weak model clearly and a strong model barely: Step-Back on GPT-4 gained 0.3 to 1.6 points over CoT, within about one SD, against 8.2 and 6.5 for PaLM-2L [d07]. Yasunaga et al. report larger gains for larger models, and better results from retrieved examples for small ones [d08].
- Input domain: stage-2 scenes were 89.1% related for product scenes against 75.9% for pop-culture scenes [c03]. Free-text attributes from a model contained invented items, worst for catchphrases (35%) [c02].
- Pair type: best image method varies by category [c12].
- Order and seed matter [a23].
- Expertise: the music tool helped students more than composers [b09]. Strong baselines gain less.
- Blend type: single-scope blends persist [a32]; replacement mashups are harder to read than fusion [d04].
- Distance of domains: fusion of incompatible domains gave higher judged hallucination than comparing them, while a logically sound fusion did not, but task type is confounded [d05].

### 5.4 Interventions that worked
All are the authors' own systems, small samples, mostly subjective measures:
- Tools that show candidate bridges raised idea counts and cut effort (PopBlends 2.03 vs 0.87 per pair, N=10; Creative Blends SUS d=0.80, N=24; Scideator CSI 70.5 vs 61.0, N=22) [a21, b11, c08].
- An explanation level (shared attributes) before generating improved rank (1.98 vs 2.40) without longer prompts [b12].
- A schema with a generic-space description, a transfer step and a diagnostic step beat a single strong CBT prompt on all five scales (for example 4.47 vs 3.97 and 4.56 vs 3.69 on the first two) [d06].
- Abstraction before structural mapping lifted narrative analogy from 0.17 to 0.46 [c22].
- Back-projecting a result to the physical input caught an error [a31] (human case).
- Generate five, keep the best: 93.3% of pairs contained a good concept [a20].

### 5.5 What did not work or did not show
- Reasoning variants of a model did not clearly beat plain ones on blends [d01].
- Scideator's rated newness gain was only 0.5 on a 7-point scale; the gain was mostly breadth [c08].
- The harmony tool gave diversity but no independent quality evidence; with correction no effect survived [b09].
- Misty satisfaction was 3.2/5 with no control [c18].
- Step-Back on StrategyQA: 83.6 vs 82.7 [d07].
- Mapping on raw text was below chance [c22].
- No study repaired blend-induced hallucination [d05].

### 5.6 Competing explanations
Cloze/predictability and salience for the N400 [b02]. Negation for privatives [b08]. Relevance theory and activation networks for the examples [b05, d15]. Ordinary analogy: the authors of KOMBINE note analogy and blending overlap [d03]. Update cancelling for counterfactuals [d09].

## 6. Language models

### 6.1 Unaided behaviour
- Over 35 models: valid blend 43.4%, analogy 53.4%, association 59.0%. The top model differs by task (blend 64.8%) [a25]. Reasoning variants did not clearly win [d01]. One pass per item at T=0.9, no scaffold arm [d03].
- Where blends fail: the generic space. Valid in 43.4% of items; given a valid one the blend was coherent 97.1% [a26]. By model, 6.7% (phi-4) to 83.3% (gpt-5.6-sol, gemini-3.1-pro) [d01]. Humans (Prolific): 12.8% valid blends, so models beat the average crowd worker; the human number is depressed by zeros for skipped items [a28].
- Sameness: 19.9% of invented concepts reuse another model's property; blends repeat 14.3 times more than analogies; same provider 2.3 times more [a27]. This is part of a general hivemind pattern (79% of same-model response pairs above 0.8 similarity) [d11]. The blend prompt was one fixed template, so part of the result may be a prompt artefact [a27].
- Weak at emergent properties of simple noun phrases (Song et al. 2025, second-hand) [a29].
- Regression to the mean on ad ideas [c21]. Surface substitution when asked to transfer a metaphor with a plain instruction [c17].
- Fusing incompatible domains: higher judged hallucination in one design [d05]; the conceptual essays assert it without data [c07, b16].
- Vision-language models: GPT-4o 73.5% against average humans 51.0% and experts 78.3% on implication; Claude-3.5-Sonnet 62.9%; small models 20.1% [b12]. Fusion mashups identified better than replacement in 9 of 11 models [d04].

### 6.2 What changed the result, and by how much
| Change | Effect | Compute matched? | Source |
|---|---|---|---|
| Name shared attributes before implication or generation | Rank 1.98 vs 2.40 (lower better); shorter prompt won in 46.0% of IEI wins | Prompt length not different | [b12] |
| Schema (generic space + transfer + diagnosis + backtracking) vs strong one-shot prompt | +0.50 MR, +0.87 MI, +0.74 VA on 5-point ratings; N=100 | No: about 8.3k tokens and 4 min per sample against one call | [d06] |
| Remove diagnostic step | -0.21, -0.51, -0.53 on MR, MI, VA | No | [c16] |
| Abstraction before structural mapping (stories) | 0.17 to 0.46 (Qwen), 0.16 to 0.45 (Llama) on 4-way MCQ; CoT alone 0.41 | No (extra LLM calls); the mapper is weak | [c22] |
| Step-Back abstraction | PaLM-2L physics +8.2 over CoT; GPT-4 +1.6; StrategyQA -0.9 | No (two calls) | [d07] |
| Generate five and keep any good | 56% single to 90-97% any-of-five | Five samples vs one | [a20] |
| Show candidate bridges to a person | Ideas per pair 0.87 to 2.03 | Baseline was web search | [a21] |
| Facet recombination plus novelty check | CSI 61.0 to 70.5; newness +0.5 of 7 | Same-LLM baseline, own system | [c08] |
| Embedding mix at the midpoint (images) | Blended depiction 0.621 vs 0.389 average over ratios | n/a | [c10] |
| Language model for the property step instead of ConceptNet | Precision at 1000: 66.38 vs 5.90 | Older models | [c05] |

Reading the table honestly: every positive result comes from an authors' system, with compute or workflow not matched to the baseline, in image, ad or narrative domains, usually with subjective ratings. None is a reasoning-accuracy test (K21, d24).

### 6.3 Judging blends
- The KOMBINE judge panel has ICC 0.48 to 0.67 and agreed with one human author 66% (majority) and 75% (unanimous) [d02]. Ranking is robust (Spearman 0.945); absolute rates are not.
- Vibe Spaces: the LLM judge matched the human top blend 35.7% and 31.3% against 25% chance; human-human kappa only 0.15-0.33 [d18].
- Short stories: LLM-LLM ICC .86-.94 but LLM-human .43 [d19].
- Consequence: validity checks for blends need a code run or a human-graded slice (G5, G8).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

Honest reading first. The evidence supports using blend-like steps as a hypothesis for O7 and S3 open mode. It does not yet support changing SCHEMA.md with a new element. Items marked [E] below are mostly guardrail-level (do not over-trust a blend) rather than new operators.

### Add now (established)
1. [E] G7 applied to blending: any blend step enters the schema only after a measured on/off ablation at equal tokens. Theory fit and insightful-looking blends do not count. Part: G7. Evidence: K04, K07, b03, b05, b06, a15, b20.
2. [E] Read a blend's result back onto both inputs and against real-world constraints before accepting it, and drop the as-if space once the question is answered. Part: S4/S8 (check). Evidence: d09, d10 (real-world knowledge enters at once; as-if space suppressed later), a31 (human error caught by back-projection; single case). The practice also follows from G3 and G10, which are established.
3. [E] Do not read diversity or idea count as quality. Measure novelty and usefulness separately, by running or blind grading. Part: G8. Evidence: K22, b09, c18, a21, c08 (count up, rated newness +0.5/7).
4. [E] Do not use a model judge alone for blend validity; report rank order or human-slice kappa. Part: G5/G8 (already there). Evidence: d02, d18, d19. The blend-specific numbers are single-source; the principle is already established in G5.
5. [E] An abstraction or role-rewriting step before mapping helps in several AI settings (narrative analogy, visual metaphor, Step-Back, self-generated analogies), more for weaker models. Keep it as a candidate wording for O7's "typed mapping", not a new state. Part: O7. Evidence: c22, d06, d07, d08 (K10). Caveat: none is compute-matched, and the strong-model gain is near zero (d07). Direction only until the test in section 8.
6. [E] Blend samples from one model are correlated; vary inputs and frames, track directions tried. Part: G4/S3 (already there). Evidence: a27, d11.

### Test first (candidates; none goes into SCHEMA.md until its test passes)
1. [S] Explicit generic-space step plus code or second-call check, against plain CoT at equal tokens. Part: O7/S3. Evidence: a26, b13, d01, b12, d06, c22 (K09, K21). Nobody has run this. See UNKNOWNS F01.02-U1, U2.
2. [S] Generate several blends and select in code (any-of-five is 90-97% in PopBlends). Part: S3 plus selection. Evidence: a20, b10, c01, c02 (K13). GPT-3 era.
3. [S] Selective-projection list ("carry" / "drop") with an explicit goal line. Part: O7. Evidence: a04, b17, d12 (K02). No test of the effect.
4. [S] Back-projection check on blend results. Part: S4. Evidence: a31, d10.
5. [S] Gate the abstraction step by model strength or by earlier failure at an impasse. Part: S6/O7. Evidence: d07, d01 (K10, K08).
6. [S] Vary inputs, not just samples, to avoid cross-model repeat blends. Part: S3. Evidence: a27, d11 (K11).
7. [S] Route far merges through more explicit steps; use single-scope swaps for easy cases. Part: O7. Evidence: d04, a17.
8. [S] Grounding check on new claims in far-domain fusions. Part: G3/G10. Evidence: d05, c07 (K19). Confounded in the source.
9. [S] "Put both on one path" step on monk-style isomorphs. Part: O7/S3. Evidence: a02, a12, d14 (K03). No solve rate exists.
10. [C] Carry image-side findings (midpoint salience, method by pair type) to text. Probably not transferable (K14, K15).

## 8. Concrete tests on our bench

All arms get equal total tokens (setup, intermediate calls and checks counted, per G7). Use several seeds. Grade by code or run wherever possible. If a model judge is unavoidable, it sees no authorship or proposed answer, scores are length-normalised, and it is compared to a human-graded slice (kappa).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Cross-domain puzzle and design items with a checkable answer (monk-style same-path isomorphs, constraint design briefs with a coded checker) | A: plain CoT. B: generic-space step, then blend, then run. C: B plus code or second-call generic-space check | Pass rate on held-out checker; valid generic-space rate on a coded witness test | Small to zero for strong models (Step-Back GPT-4 gain 0.3-1.6); larger on mid and low models. Hypothesis, not established |
| T2 | KOMBINE-style entity pairs (30 pairs, Wikidata entities) | A: single blend prompt. B: propose-then-check generic space. C: B with up to 2 retries | Valid generic-space rate (baseline mean 43.4%); coherent given valid (baseline 97.1%); human-graded 20-item slice with kappa | Lift in valid generic space if the check works. 43.4% is the bar for the model average, not a prediction for our model |
| T3 | Open-mode design tasks (S3 open) | A: n isolated typical-first attempts. B: n blend attempts with varied input pairs. C: B plus code selection | Distinct directions per token; blind expert usefulness; share of attempts repeating another attempt's property (embedding threshold as in KOMBINE) | More distinct directions with input variation; usefulness unknown. Code selection should beat one blend (56% to 90%+ any-of-five) |
| T4 | Same items as T1 | Blend with vs without "carry / drop" lists and a goal line | Rate of incoherent blends (code-checked contradictions between dropped and used items); pass rate | Fewer contradictions; pass-rate effect unknown |
| T5 | Items with an easy wrong blend (math-in-physics word problems, unit traps) | Blend with vs without back-projection to each input | Error-caught rate; final accuracy | Catches single-scope errors as in Bing and Redish; magnitude unknown |
| T6 | Mixed pairs: compatible vs incompatible domains | Fusion prompt with vs without grounding check on new claims | Blind-graded unsupported-claim rate | Fewer unsupported claims with the check; direction from Sato, confounded |
| T7 | Monk riddle and 8 same-path isomorphs (new surface forms) | Plain; "put both on one path" step; full blend record | Solve rate | Unknown; gives the missing rate |
| T8 | Models of small, mid and strong size on T1 | Scaffold on/off per size | Gain by size | Gain falls with strength; sets the gate for the step |
| T9 | Blend judges | LLM judge vs human slice on 60 hard blends | Cohen's kappa; top-1 match | Shows whether any judged blend metric can be used |

## 9. What does not transfer, and why
- Neural findings (N400 gradients, ERP, MEG): describe human reading cost. Nothing to implement; at best a prior that far mappings cost more compute [a17, b01].
- Cognitive-linguistic claims about conventional blends in everyday language (Kant debate, "red-hot with anger"): language analysis, not reasoning gain [a05, a09].
- The claim that blending is not algorithmic [a08] argues against a fixed operator. Our design is generate-many-then-select, not a single deterministic procedure.
- Image-side results: midpoint embedding mix, textual vs alternate vs switch, IT-Blender, Vibe Spaces ranking, fusion vs replacement for images [c10, c12, a23, c13, d18, d04]. They depend on diffusion mechanics and image judgment.
- Human tool studies (PopBlends, Creative Blends, Scideator, CHAMELEON, Misty): the gain came from showing candidates to a person and lowering effort. Our agent has no human in the loop at test time, and ideas per pair is not an accuracy measure [a21, b09, c08, c18].
- Training-time ideas (blend-aware loss, Turner poster): outside the no-training rule [d13].
- Self-reported strain and satisfaction: irrelevant to accuracy.
- Sato and Lynn essays: no measurements; do not cite as effect evidence [K19].
- Classical systems (Divago, COINVENT, VisiBlends): demos with no baselines [K27].
- Blend network typology: left to its own subfield; not tested for effect.

## 10. Open questions
1. Does an explicit generic-space step beat plain chain of thought on a reasoning or design task at equal tokens? No study tests it (K21, d24).
2. Can a scaffold lift KOMBINE's valid generic-space rate above 43.4% by model? The 6.7% to 83.3% spread suggests room for weak models [d01].
3. Does another benchmark reproduce the abstraction bottleneck (43.4% against 97.1%)? Only KOMBINE reports it.
4. Does a human-graded hard slice agree with the KOMBINE judge panel? Only one author checked 60 items [d02].
5. How many samples, or what input variation, escapes cross-model repeat blends? No measure [d11, a27].
6. What are monk-riddle solve rates for people and models with and without a one-path hint? None found [d14].
7. Does "what not to carry over" reduce incoherent blends in a model, without an LLM judge? [K02]
8. Does fusion beat replacement in text-only blends, and by how much? [d04]
9. Does fusing incompatible domains raise hallucination once task type is controlled? Sato's design is confounded [d05].
10. Is there any head-to-head test of blending against relevance theory (Hilpert 2010, Schmid, Sabzevari 2011)? [d15]
11. What do Divago and COINVENT report as measured results? Unopened [c23, c24, d21].
12. Unopened primary sources to read: Gibbs 2000, Fauconnier and Turner 2002, Song et al. 2025, Fritz and Baggio 2020, the VisiBlends paper, Keon et al. effect sizes, Scideator ablation tables.
13. Does the VisiBlends 96% vs 21% claim survive reading the paper? Press release only [d22].
14. When should elaboration stop? No rule exists [a03, b05].

## 11. Sources

[V] opened and read in this series; [M] snippet or summary only.

Primary and founding
- [V] Fauconnier and Turner 1998/2001, Conceptual integration networks. https://www.neurohumanitiestudies.eu/archivio/SSRN-id1292966.pdf
- [V] Wikipedia, Bisociation (Koestler 1964). https://en.wikipedia.org/wiki/Bisociation
- [V] Wikipedia, Conceptual blending. https://en.wikipedia.org/wiki/Conceptual_blending
- [V] Coulson and Van Petten 2002, ERP study, Memory and Cognition 30(6). http://link.springer.com/content/pdf/10.3758/BF03195780.pdf and https://pages.ucsd.edu/~scoulson/CoulsonVanPetten2002.pdf
- [V] Privative-adjective MEG/EEG study 2026, Imaging Neuroscience. https://pmc.ncbi.nlm.nih.gov/articles/PMC12887245/
- [V] de Vega, Urrutia and Riffo 2007, Memory and Cognition 35(6). https://link.springer.com/content/pdf/10.3758/BF03193611.pdf
- [V] Ferguson and Sanford 2008, J Memory and Language 58(3). https://kar.kent.ac.uk/23060/1/count_ET_paper_final.pdf
- [V] Bing and Redish 2007. http://www.physics.umd.edu/perg/papers/redish/BingRedishPERC2006.pdf
- [V] Dreyfus, Gupta and Redish 2014. https://arxiv.org/abs/1412.1693

Critique
- [V] Glebkin 2013. https://escholarship.org/uc/item/95p302sj
- [V, via summariser] Ritchie 2004. https://web.pdx.edu/~cgrd/Metaphors%20of%20Conceptual%20Integration.html
- [V] Yin 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13038881/
- [M] Gibbs 2000 (via Ritchie, Glebkin, Wikipedia). https://en.wikipedia.org/wiki/Conceptual_blending
- [M] Fauconnier and Turner 2002 (via Glebkin, Wikipedia). Same URL.
- [M] Hilpert 2010. https://benjamins.com/online/ebop/publications/54068
- [M] Schmid on blending and relevance. https://www.anglistik.uni-muenchen.de/personen/professoren/schmid/schmid_publ/blending_relevance.pdf
- [M] Sabzevari 2011 chapter (title only). https://www.degruyterbrill.com/

LLM and AI studies
- [V] Schapiro et al. 2026, KOMBINE. https://arxiv.org/abs/2509.21043
- [V] Wang et al. 2023, PopBlends. https://arxiv.org/abs/2111.04920
- [V] Ge and Parikh 2021, Visual conceptual blending. https://arxiv.org/abs/2106.14127
- [V] Olearo et al. 2024. https://arxiv.org/abs/2407.14280
- [V] Olearo et al. 2025. https://arxiv.org/abs/2506.23630
- [V] Sun et al. 2025, Creative Blends. https://arxiv.org/abs/2502.16062
- [V] Peng et al. 2025, CreativeMashup. https://arxiv.org/abs/2504.13120
- [V] Sato 2025, The Way We Prompt. https://arxiv.org/abs/2505.10948
- [V] Sato 2025, prompt-induced hallucination. https://arxiv.org/abs/2505.00557
- [V] Lynn 2026, Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2026.1849083 and https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13461484/fullTextXML
- [V] Radensky et al. 2026, Scideator. https://arxiv.org/abs/2409.14634
- [V] Matsuhira et al. 2024. https://arxiv.org/abs/2411.03595
- [V] Cho et al. 2025, IT-Blender. https://arxiv.org/abs/2506.24085
- [V] Xu et al. 2026, Beyond Pixels. https://arxiv.org/abs/2602.01335
- [V] Misty, CHI 2025. https://arxiv.org/abs/2409.13900
- [V] Keon et al. 2025, Galton's Law of Mediocrity. https://arxiv.org/abs/2509.25767
- [V] Khojasteh et al. 2026, YARN. https://arxiv.org/abs/2603.29997
- [V] Zheng et al. 2024, Step-Back. https://arxiv.org/abs/2310.06117
- [V] Yasunaga et al. 2024, analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Jiang et al. 2025, Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Yang et al. 2025, Vibe Spaces. https://arxiv.org/abs/2512.14884
- [V] Evaluating creative short story generation. https://arxiv.org/abs/2411.02316
- [V] Zacharakis et al. 2021, CHAMELEON. https://pmc.ncbi.nlm.nih.gov/articles/PMC7983946/
- [V, abstract and record page] Eppe et al. 2018. https://tore.tuhh.de/entities/publication/ebc32175-2b53-4ea3-9d9c-8f5a6988a8e3 and https://doi.org/10.1016/j.artint.2017.11.005
- [V] Gomez-Ramirez and Turner 2026 poster. https://markturner.org/CogSci2026BlendingPosterCompressed.pdf
- [M] Pereira 2006, Divago. https://doi.org/10.1016/j.knosys.2006.04.008
- [M] Pereira and Cardoso 2003. https://eden.dei.uc.pt/~amilcar/ftp/ecaspapers/AISBJ2003b.pdf
- [M] Chilton, Petridis and Agrawala 2019, VisiBlends (press release). https://www.engineering.columbia.edu/about/news/visiblends-new-approach-disrupt-visual-messaging
- [M] NazoNazo (2509.14704). https://arxiv.org/abs/2509.14704
- [M] Latent-space ideation (2507.13874). https://arxiv.org/abs/2507.13874
- [M] Judge-reliability snippets (2406.12624, 2411.15560, 2502.03253). https://arxiv.org/abs/2406.12624
- [V] Coverage listing, arXiv "conceptual blending". https://arxiv.org/search/?query=%22conceptual+blending%22
- [M] Song et al. 2025 (noun-phrase emergent properties; relayed by KOMBINE, not opened).

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 8 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

