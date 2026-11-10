# Imagery debate: deep document

*Subfield D06.04. Scope: pictorial versus propositional mental images (Kosslyn, Pylyshyn, Tye), and every 2020-2026 LLM study that tests or uses the idea of a drawn, spatial state versus a symbolic one. Evidence ids (a01, b22, c01, d03 ...) point to evidence_a-d.jsonl; claim ids (K01 ...) point to claims.jsonl. Human numbers marked "recalled" were not re-read this run. See critique.md for the cross-check.*

## 1. What it is

The imagery debate asks one question: when a person "sees" a picture in the mind, what is stored? Two answers.

- **Pictorial (depictive) view** (Kosslyn). The image is a spatial array. Parts of the array map to parts of the object. Distance in the array stands for distance in the object. The mind then scans, rotates and zooms it, much like a display.
- **Propositional (descriptive) view** (Pylyshyn, Anderson). There is no picture. There are symbol structures, like trees of facts about parts and relations. The feeling of a picture is a by-product (epiphenomenal). Scan and rotation times come from what people know about the world, not from the medium.
- **Middle views** (Tye 1991). Images are symbolic but have a special spatial-array format, not unstructured pictures.

Why this matters for us. Our schema has one representation operator, O6 "Change representation: the problem in other terms: objects, counts, regions, symmetry". The debate gives us two testable forms of O6: a spatial form (a drawn text grid, a map, a sketch) and a symbolic form (a coordinate list, an object list, a graph, an equation). The LLM literature now measures which form helps which model on which task. The human debate is not settled by these results (section 9). The engineering question is: does it pay to draw the state, and when?

Headline answer from the evidence: it depends on who makes the picture, how accurate it is, and what the task needs. A correct, given text grid often beats an image of the same problem. A model-drawn grid is wrong most of the time and often does not help at equal effort. Tasks that need real transformation (mental rotation) stay hard for every tested model unless the task is recoded to 2D.

## 2. History and theories in depth

### 2.1 Founding chronometric work (pictorial side)

- **Shepard and Metzler (1971)**, Science 171:701-703 (a01, b06; not opened). People judged whether two 3D block figures were the same shape. Reaction time (RT) rose linearly with the angle between them. Rotation in the picture plane and in depth gave the same slope. Recalled values: about 1 s near 0 degrees to 4-5 s near 180 degrees, about 60 degrees per second, about 8 observers. Cooper and Shepard (1973, a26) found the same for letters: RT peaks near 180 degrees and returns to baseline at 360. That fits rotation better than lookup of stored views.
- **Kosslyn (1973)** (b05) and **Kosslyn, Ball and Reiser (1978)** (a02, d19). Subjects memorised a fictional island map with 7 landmarks, then imagined a dot moving between landmarks. Scan time grew linearly with real map distance (21 landmark pairs; r about .97, recalled). The 1978 paper reports four experiments, larger images took longer, and with no instruction to image, distance had no effect (abstract read, d19).
- **Finke and Pinker (1982)** (a09). Time rose with the distance from an arrow to a remembered dot, even when no scanning was requested. Recalled.
- **Kosslyn's theory** (a17, Image and Mind 1980; Image and Brain 1994). A surface-matrix "visual buffer" (a CRT-like 2D array), long-term memory with propositional files, and processes that generate, inspect, rotate, zoom and scan the image. This is the model engineers can implement (section 4).

### 2.2 Descriptivist challenge

- **Anderson (1978)** (a12). Any result explained by a pictorial representation plus a process can be matched by a propositional representation plus a different process. Behaviour alone cannot fix the format. Formal argument, no data.
- **Pylyshyn (1973, 1981, 2002, 2003)** (a07, a06, a27, b04). Scan and rotation effects come from tacit knowledge of how real objects behave and from subjects' wish to act as if scanning. He separates effects of the cognitive architecture from effects of knowledge. He argues retinotopic activation in imagery does not show a pictorial representation either. The 2002 BBS target article has 368 citations (a06).
- **Intons-Peterson (1983)** (a08, b09, d19). Four experiments (acuity, map scanning, rotated-hands priming, observer probe). Different experimenters told subjects different expected outcomes. Performance followed the experimenter's belief in all four. Observers named the belief. This is the demand-characteristics attack (abstract read).
- **Jolicoeur and Kosslyn (1985)** (b08). Recalled reply: the scan-time effect persists in naive subjects. Not verified; no abstract available.

### 2.3 Does imagery reinterpret? (boundary between image and description)

- **Chambers and Reisberg (1985)** (a11). Subjects imaged the duck-rabbit and almost none reversed it, though they could when drawing from memory. Images look interpreted, not raw pictures. Recalled, roughly none of 15.
- **Finke, Pinker and Farah (1989)** (a10). Subjects followed spoken instructions to build and transform an imagined figure (a D rotated 90 degrees left with a J below gives an umbrella) and named the result. Many succeeded. 12 items. So construction works where reinspection fails. K25 (contested).

### 2.4 Neural turn

- **Kosslyn et al. (1995)** PET (a28, d16). Imagining at small size activated posterior V1, large size anterior V1. The effect appeared only against an auditory-cue baseline with the same cues; a resting baseline hid it (abstract read).
- **Kosslyn et al. (1999)** (b07, d17). rTMS over medial occipital cortex impaired imagery relative to sham, and impaired the same task done by looking (abstract read).
- **Kosslyn, Thompson and Ganis (2006)** *The Case for Mental Imagery* (a16): the book-length reply.
- **Pearson and Kosslyn (2015)** (a13, b01, b02, b03). Claim the debate is over: humans use at least two formats. Evidence they cite: at least 20 studies (1993-2010) of early visual activity in imagery; V1 decoding trained on perception transferring to imagery; a Gabor-wavelet encoding model predicting which pictures are imagined; binocular rivalry priming (an imagined orientation biases later rivalry in a graded, orientation-specific way; Pearson, Clifford and Tong 2008). Four reasons for a depictive format: wiring economy, least commitment, simulation, language-perception bridging.
- **Spagna, Hajhajate, Liu and Bartolomeo (2021)** (d15). The counter-weight. A meta-analysis of 46 experiments in 41 studies. 27 imagery-vs-control experiments (376 foci, 380 subjects) showed no consistent early visual cortex activation (Bayes factor under 0.33). The hotspot was a left fusiform area. Four imagery-vs-perception experiments (52 subjects); 15 motor imagery (239 subjects). This reads against the V1 claim. K03 is contested.

### 2.5 Aphantasia and dissociations

- **Zeman et al. (2015)** (a19, b17): lifelong absence of imagery in otherwise high-functioning people; prevalence about 1-4% (as quoted in a22).
- **Bridge et al. (2012)** (a14): patient SBR, near-complete cortical blindness from calcarine damage, yet vivid imagery behaviourally and in fMRI. VVIQ (1 vivid to 5 none): SBR 1.9 vs controls 2.3 (SD 0.6). N=1.
- **Bainbridge et al. (2021)** (b10-b12): 61 aphantasic (VVIQ 25 or less) vs 52 controls (VVIQ 40 or more), 2,795 online scorers. Share of objects drawn from memory 0.261 vs 0.369 (Z=4.09, r=.39, p=4.2e-5). Location error under 10% of image size in both groups. OSIQ object scale d=3.80; spatial scale t(103)=-0.33, p=.742. In a matched copy-in-view task, no group difference. Aphantasic participants leaned on words.
- **Milton et al. (2021)** (b13): 24 aphantasia, 25 hyperphantasia, 20 controls. Mental rotation at ceiling (over 90%) in all three groups.
- **Keogh and Pearson (2018)** (b16): weaker rivalry priming in aphantasia (not opened). **Thorudottir et al. (2020)** (b14): acquired aphantasia in one architect. **Chang et al. (2025)** (d18): V1 decodes imagery content equally in aphantasia and controls, but ipsilateral and without cross-decoding to perception (abstract).
- **2026 PBR paper** (b18): vividness ratings and aphantasia labels may be criterion confounds, since the axis between image and non-image thought is undefined. Argument only.

Reading: spatial layout and object detail can dissociate (K05), and function can survive without reported experience (K04). Format and experience are not the same thing.

### 2.6 Status of the debate

SEP (Nanay 2021, a05): many say it is dead, including some of the originals. Pearson and Kosslyn say it is ended with two formats. Pylyshyn says it is not. Our reading: no one has a decisive test; neural evidence is mixed (K03); RT evidence fits both with auxiliary assumptions (K02). Do not borrow certainty from either side.

## 3. Core findings with exact numbers

Status: established (E), single-source (S), contested (C). "Human, recalled" = number from memory, not verified.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| RT rises linearly with rotation angle | about 1 s to 4-5 s, 0 to 180 deg, about 60 deg/s; N about 8 (human, recalled) | Shepard and Metzler 1971 (a01) | E for pattern; slopes unverified |
| Scan time rises with map distance | 21 landmark pairs, r about .97 (recalled); 4 experiments, abstract read | Kosslyn et al. 1978 (a02, d19) | E for pattern |
| Experimenter expectation shifts imagery results | 4 experiments, all followed expectation | Intons-Peterson 1983 (d19) | E (abstract) |
| Imagery V1 activation depends on baseline | auditory-cue baseline yes, rest baseline no | Kosslyn et al. 1995 (d16) | C |
| No early visual cortex in imagery meta-analysis | 27 experiments, 380 subjects, BF under 0.33 | Spagna et al. 2021 (d15) | E as a meta-analysis; C overall |
| Aphantasia: fewer objects, same layout | 0.261 vs 0.369 objects; location error under 10%; spatial OSIQ p=.742 | Bainbridge et al. 2021 (b10, b11) | E (2 sources) |
| VoT (draw text grid per step) vs CoT, GPT-4 | NL nav 59.00 vs 54.00 (p<0.16) vs no-viz 35.50; tiling 63.94 vs 54.15; route completion 40.77 vs 37.02, success 14.72 vs 9.48 | Wu et al. 2024 (c01) | S |
| Drawn state is mostly wrong | accuracy 26.48 and 24.25%; compliance 51.14 and 52.01%; correct decisions 65.16 and 77.20% when the drawing was accurate | Wu et al. 2024 (c03) | S, backed by d02 |
| VoT loses on modular-arithmetic ring task | 200 items, size 12: CoT 52.5% vs VoT 49.5% | Wu et al. 2024 (c03) | S |
| VoT depends on model size | LLaMA3-70B 19.90 to 30.24; LLaMA3-8B 4.65 vs 4.97; GPT-3.5 16.10 vs 19.02 | Wu et al. 2024 (c02) | S |
| Wording "use ascii-art to visualize" | complete tracking 98.5% (+78.5), score 62.5% (+3.5) | Wu et al. 2024 (c03) | S |
| Model-drawn ASCII before answering did not help | GPT-4.1 66.9 vs text 71.7 vs given ASCII 75.3 vs both 78.4; own ASCII accuracy 41.7%; GPT-OSS-20B 83.8 vs 85.8 | Huang et al. 2026 Text2Space (d01) | S |
| Draw-answer agreement predicts accuracy | consistent in 46-76% of cases; accuracy 89-97% there (Qwen3-235B 95.0, GPT-OSS-20B 97.0) | d02 | S |
| Text beats image of the same problem | IsoBench gaps 28.7 (Claude-3 Opus), 18.7 (GPT-4 Turbo), 14.9 (Gemini Pro), 1,887 samples | Fu et al. 2024 (b20) | E |
| Removing or noising the image can raise VLM score | LLaVA-1.6-34B Spatial-Grid +20.1%; Maze-Nav noise +6.5%; GPT-4V text added to image +25.6% | Wang et al. 2024 (c07) | E |
| Maze 2026: image vs given text grid | Sonnet 4.6 6 vs 80 of 100; Opus 4.7 31 vs 90; tokens per solve 14,313 vs 3,222 (Sonnet); 4.4x and 5.8x fewer | Rodriguez Salgado 2026 (d03) | S |
| Image input suppresses reasoning effort | 5-19x shorter outputs; font alone swings accuracy up to 47 points; GSM8K gaps over 60 points | Sun et al. 2026 (d09) | S |
| CoT hurts perceived spatial tasks | about 3% average loss over 17 models, 13 benchmarks; GPT-5 +0.65 without CoT | Kancheti et al. 2026 (d08) | E (several sources) |
| Translating image to text recovers part of the gap | IsoSP up to +14.4 (science); IsoCB up to +9.4 (graph algorithms) | Fu et al. 2024 (b21) | S |
| Text encoding matters | ARC raw grid 12-13 vs object JSON 23 of 50 easy tasks; PaLM-62B connected nodes 19.8% to 53.8% | Xu et al. 2023; Fatemi et al. 2023 (c17, c18) | E (2 sources) |
| Symbolic spatial tasks solved, rotation fails | Cube Rolling o1 97.5, o4-mini 98.3; Mental Rotation Gemini 2.5 Pro 20.5, o1 7.5, GPT-4o 4.7, human 100 | Wu et al. 2025 SpatiaLite (c08) | E (5 sources) |
| Mental rotation, 3,744 trials | human 79.6%; models 56.7-58.1%; o3 with tools 88.8% vs 47.8% on 400 hard trials | c11 | S |
| 3D rotation with renderer tool | human 79.16; GPT-5.2 50.0; with renderer 50-62.5% over 10 runs; reset-to-canonical view 85-97.5% | Hayashi and Hirata 2026 (c10, d05) | C (one study, about 40 items) |
| VisFactor psychometric battery | best model 55.9% vs 78.8% (31 students); CoT hurt four tests | c12 | E |
| Trained image thoughts (MVoT) | FrozenLake 85.60% vs CoT 61.48%; CoT 3x3 .940 to 6x6 .391, MVoT .862 to .888; 90.8% of CoT errors wrong coordinates; Maze CoT .979 vs MVoT .930 | Li et al. 2025 (c04, c05) | E, needs training |
| Visual planning with training | VPRL 80.6 vs SFT 53.6; FrozenLake 6x6 82.4 vs Gemini 2.5 Pro 38.8 | c13 | E, needs training |
| Mirage latent visual tokens | VSP .87 vs CoT SFT .84; planning CoT .58 vs direct .76 | c14 | E, small gain |
| Sketchpad | GPT-4o math +11.2%, vision +14.3%, maxflow 25.0 to 66.3; GPT-4 Turbo math +23.4%; humans draw the same line 80%; GPT-4 Turbo parity 80.5 to 71.5 | Hu et al. 2024 (b26, c15) | S |
| Whiteboard-of-Thought (GPT-4o) | square grid CoT 98 vs WoT 50; hexagon CoT 8 vs WoT 61; ASCII 3D CoT 0 vs 92.1 | Menon et al. 2024 (d04) | C |
| Map first, then reason | MindCube 37.8% to 57.8% (+20.0) | Wang et al. 2025 (c20) | S |
| Graph planning in text fails | CogEval GPT-4 0 of 30 shortest path one cluster away; 3-step 0.55 | Momennejad et al. 2023 (c19) | S |
| Imagine-and-name by reasoning LLMs | human 2.85 (SD 1.51, N=100); Gemini 3 Pro 3.65, GPT-5 3.35, o3-Pro 3.31, o3 3.13; Claude Opus 4.1 2.65 (p=.590); GPT-5 minimal 2.04 | McCarty and Morales 2025-26 (d06) | S |
| VLM accuracy tracks human RT | r=-0.88 rotation, -0.73 Geoclidean, -0.97 numerosity | c11 | S, correlational |
| Colour structure in text-only models | Kendall tau .25-.33, 18 colours | Abdou et al. 2021 (c21) | S |
| SiT-Bench text-only spatial | best 59.46 (Gemini-3-Flash thinking) vs human 74.42; random 27.30 | Guo et al. 2026 (d07) | S |

## 4. Mechanisms and models

### 4.1 Kosslyn's model as a program

State: a 2D array B (the visual buffer) with a resolution and a limited extent. Long-term memory holds propositional "files" per object (parts, positions, sizes).

Processes:
1. **Generate**: read the file, write marks into B at coordinates. Cost grows with detail. Parts are drawn one at a time.
2. **Inspect**: look at a region of B at a chosen scale. Small details need zoom. A larger image lets you resolve parts but can overflow the buffer.
3. **Scan**: shift the attention window across B. Time is proportional to distance (the RT signature).
4. **Rotate / transform**: move cells in small steps along a path. Time is proportional to angle.
5. **Fade**: marks decay, so refresh is needed.

Key point for an engineer: the buffer has no meaning attached. Meaning comes from the files. That is why reinterpretation is hard (Chambers and Reisberg) but construction from parts works (Finke et al.).

### 4.2 Pylyshyn's alternative as a program

State: a structured fact base: objects, parts, relations, attributes (a graph or tree). Processes: lookup and inference rules that carry tacit knowledge such as "moving from A to B passes the points between". Time effects arise because the inference chain over intermediate facts is longer for far points. In LLM terms this is a coordinate or relation list plus a procedure.

### 4.3 What each is in an LLM scaffold

| Form | Implementation | Strength | Weakness |
|---|---|---|---|
| Depictive-like | Model writes a text grid (VoT) or code draws a plot (Sketchpad, Whiteboard-of-Thought) after each step | Keeps implicit relations (adjacency, blocking); later steps can "read" the state | Often wrong (24-26% accurate in VoT; 12-50% in Text2Space); more tokens |
| Propositional | Coordinate list, object JSON, graph edges, cognitive map as text | Exact lookup, easy to check in code | Fails when relations are many and implicit (FrozenLake large boards: 90.8% of CoT errors were wrong coordinates) |
| Hybrid | Both, with an agreement check | Draw-answer agreement gives 89-97% accuracy where it holds | Agreement in only 46-76% of cases; extra tokens |
| Tool-made canonical view | Code reorients a 3D model to a standard view | Turns 3D rotation into 2D matching, 85-97.5% | One study; about 40 items |

### 4.4 VoT procedure (implementable)

1. Instruction: "After each step, draw the current state as a text grid, then write the next step."
2. Each step appends a grid. The grid is the working memory.
3. Optional check (not in the original paper; proposed from d02): compare the final drawn grid with the stated answer. If they disagree, re-derive.

State-tracking quality is the bottleneck, not the reasoning after it (accuracy given a correct drawing 65-77%).

### 4.5 Why the form matters: three mechanisms with some support

- **Serialisation breaks structure.** Row-by-row text hides vertical adjacency (ARC, c17). Object lists restore it. Support: GPT-4 12-13 to 23 of 50.
- **Coordinates drift on long boards.** Most CoT errors were wrong coordinates (MVoT, 90.8%).
- **Image input suppresses reasoning.** Models produce 5-19x shorter outputs on images (d09). Part of the text-vs-image gap is effort, not perception. Frontier models also convert an image to a text grid first and then search in prose (d03).

## 5. What holds up

### 5.1 Human side

- **Holds**: linear RT with angle and distance, replicated across decades and in children and adults with autism (a15). Scanning splits into two processes; memory-based images scan more slowly than just-seen patterns (d20).
- **Contested**: whether the slopes show a depictive format. Experimenter expectation changes results (four of four experiments). The Jolicoeur-Kosslyn reply is recalled only.
- **Neural**: V1 PET and rTMS support depiction but are baseline-dependent (d16), and the one imagery fMRI meta-analysis finds no early visual activation (d15). Contested.
- **No pooled slope meta-analysis exists** (d21). Rotation meta-analyses pool sex differences (d=0.60, 95% CI 0.54-0.67, 41 studies, 59 effects, 2026) and neural location.
- **Aphantasia**: the spatial versus object-detail dissociation held in two samples. Label validity is questioned (b18).

### 5.2 LLM side: what replicated

- Text beats image of the same problem: IsoBench, SpatialEval, MazeBench (2026), Vision-Models-Are-Blind (GPT-4o mean 50.23%, chance 24%; c16). Gaps shrank across Claude versions on mazes (74 to 59 points) but are not closed. Part is a rendering and short-output artifact (d09).
- CoT is not a free win on spatial tasks: VisFactor, Mirage planning, Talk like a Graph, Kancheti. CoT does win where exact coordinates are given as text (Maze CoT about .98).
- Text recoding helps: object lists, incident encoding, cognitive maps (K13, K20).
- Rotation fails except when recast: Cube Rolling 97.5-98.3% against Mental Rotation 4.7-20.5%.
- Training helps image thoughts (MVoT, VPRL, MentalThink 57.8 vs 42.5). Out of scope for us.

### 5.3 LLM side: failures and moderators

- **VoT's gain over CoT is small**: +5.0 points on NL navigation with p<0.16 only; +3.7 route completion. The "+23.5%" is over no-viz. One model family (GPT-4).
- **Model size**: no gain for GPT-3.5 and LLaMA3-8B.
- **Task**: loses on the modular ring task; loses on square grids in Whiteboard-of-Thought (98 vs 50) but wins on hexagons (8 to 61).
- **Self-drawn grids** did not help in the one direct test (Text2Space, GPT-4.1 66.9 vs 71.7).
- **Rendered rotation module** did not help (50-62.5%).
- **Unified models**: the model's own thinking-image is often ignored (d13).
- **Sketchpad** is not uniform: GPT-4 Turbo parity fell 80.5 to 71.5.
- **Tool help** depends on what is returned: Gemini-2.5-Pro +18.00 on 2D relations, Gemini-3-Flash -8.06 on 3D distance (d10).

### 5.4 Interventions that worked or not

| Intervention | Result | Verdict |
|---|---|---|
| Give a correct text grid | Opus 4.7 90/100 vs 31 on image, 5.8x fewer tokens | Worked |
| Translate image to text first | up to +14.4 | Worked |
| Map first, then reason | +20.0 | Worked (one source) |
| Object list for ARC | 12-13 to 23 of 50 | Worked |
| Canonical-view reset for rotation | 85-97.5% | Worked (one study) |
| Draw grid then answer (self-made) | GPT-4.1 66.9 vs 71.7 (-4.8) | Did not help |
| Rendered rotating 3D view | 50-62.5% | Did not help |
| Text CoT on perceived images | about -3% average | Hurt |
| Raise reasoning effort on symbolic assembly | GPT-5 2.04 to 3.35 | Worked |
| Add image generator to o3 | 3.13 to 2.77 | Hurt |

Reconciliation we propose (our inference, untested): the picture helps when a correct, model-controlled, text-form state is in context, and hurts when the model must perceive a raw image or draw one it cannot get right. See U1-U3 in UNKNOWNS.md.

## 6. Language models

1. **Text-form spatial state with a given grid**: strong. Opus 4.7 gets 90/100 and Sonnet 4.6 80/100 on mazes up to 20x20 when handed the text grid, with reasoning tokens (d03; 110 mazes, 19 model configs; GPT-5.5 96/100 on images, GPT-5.4 91, Gemini 3.1 Pro 79).
2. **Image form**: much worse for most models: Sonnet 4.6 6/100, Opus 4.7 31/100. Image input cut output length 5-19x (d09).
3. **Drawing their own state**: weak. Text2Space: drawn grids right 12-50% of the time. VoT: 24-26%. LTD-Bench (d14): only DeepSeek-R1 averages above 70%; writing drawings is the weak half, reading them is easier.
4. **Rotation and transformation**: near floor for most models (Mental Rotation 4.7-20.5%; 3D rotation 20-50% vs human 79.16). Claude-3.7-Sonnet, Claude-Opus-4.5 and Gemini-3.5-Pro each 37.5 on 3D rotation (d05; table rows partly shifted in extraction).
5. **Symbolic recoding**: strong (cube rolling 97.5-98.3%).
6. **Reasoning budget**: GPT-5 2.04 (minimal) to 3.35 (high) on imagine-and-name (d06). SiT-Bench thinking helps (Qwen3-VL-32B 45.9 to 51.06; Qwen3-8B 37.91 to 45.04). But text CoT on perceived images hurts about 3%.
7. **Model dependence of VoT**: needs a strong model. GPT-4 yes; GPT-3.5 and LLaMA3-8B no.
8. **Claude specifics**: Claude 3 Opus had the largest IsoBench image gap (28.7). Claude-3.5 Sonnet was best on Vision-Models-Are-Blind (77.84%). Claude Opus 4.1 matched but did not beat humans on imagine-and-name (2.65, p=.590). Claude Sonnet 4.6 on image mazes ignored a ban on converting to text.
9. **Does the model "image"?** The Artificial Phantasia authors argue reasoning models do imagery-type tasks with propositional reasoning alone. Items are symbolic shape assembly; one group; no replication. This is evidence about format for models, not about human minds.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory, tools. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | When a spatial problem arrives as an image, first restate it as text (grid, coordinates, object list), then reason on the text. Prefer symbolic encoding over a raw picture. | O6 | [E] | K11, K12, K26; b19, b20, c06, c07, d03, d09, d22 |
| A2 | Choose the text encoding on purpose: object list and edge or incident list beat raw row-by-row grids on structure tasks. Do not feed row-serialised grids for 2D structure without an object view. | O6 | [E] | K13; c17, c18 |
| A3 | Do not force long chain-of-thought on perceived spatial items or on rotation. A direct-answer arm is the baseline; keep CoT only where it wins. | G11, O6 | [E] | K18; c12, c14, c18, d08, d13 |
| A4 | Send true transformation subtasks (rotation, 3D) to code or tools, not to free-text thinking. Keep recodable ones (cube rolling, counts, adjacency) in text. | O6, tools | [E] | K14; c08, c10, c11, c12, c22, a25 |
| A5 | Log which representation each solve used (grid, list, map, prose) so memory can learn the task-to-form pairing. | memory | [E] as practice; value untested | K05, K09 |

### Test first (not yet established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Self-drawn text-grid state (VoT) vs plain CoT vs coordinate list at equal tokens | O6 | [S] | K07, K27; c01, d01, d04 |
| T2 | Draw-vs-answer agreement as a trust signal; re-derive on disagreement | G, O6 | [S] | K28, K08; d02 |
| T3 | Router: standard text layout stays text; frame change or irregular geometry recoded to global coordinates or canonical view, or drawn | O6 | [C] | K29; d04, d07, d11 |
| T4 | Map-then-reason (cognitive map first, as text) on layout questions | O6 | [S] | K20; c20 |
| T5 | Canonical-frame tool (code returns the object in a standard orientation) for rotation items | tools, O6 | [C] | K15, K32; d05, c11 |
| T6 | Symbolic restatement beside any spatial form (IsoCombination style) | O6 | [S] | K12; b21 |
| T7 | "Cite the cell" check: the answer must name the drawn cell or fact it used; drop drawing if never cited | G10, O6 | [S] | K31; d12, d13 |
| T8 | Reasoning-effort split: same items at two thinking budgets, with and without a drawn grid | G11, G12 | [S] | K22, K34; d06 |
| T9 | Wording of the format instruction (e.g. "use ascii-art to visualize") | O6 | [S] | K10; c03 |
| T10 | Code-drawn diagram tool (Sketchpad style) with per-sample cost | tools | [S] | K19; b26, c15 |
| T11 | Length-matched output when the input is an image (image input shortens reasoning 5-19x) | G11 | [S] | K30; d09 |

Not for the agent (training): MVoT, VPRL, Mirage, MentalThink (SCHEMA.md section 4b; see section 9).

## 8. Concrete tests on our bench

All arms at equal total tokens (count drawing and checks). Report against plain CoT, not only against no-viz. Items need exact answers so code can score. At least 5 runs per arm, because several reference effects are small (VoT +5.0 over CoT, p<0.16).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| 1 | Grid navigation (FrozenLake-style 4x4 to 8x8, mazes) | (a) plain CoT, (b) CoT with coordinate list, (c) VoT draw per step, (d) given verified grid | Exact-match accuracy; tokens per solve | Given grid wins; VoT near CoT; coordinate list beats CoT on boards over 5x5 |
| 2 | Same items with mixed layouts (square, hexagon, ring, modular) | always-text, always-draw, router (T3) | Accuracy by layout class | Router beats both fixed arms by 3 or more points; draw loses on square grid and ring |
| 3 | Test 1 items | VoT with vs without draw-vs-answer agreement check | Final accuracy; fraction triggered; extra tokens | Accuracy on agreeing cases 89% or higher; re-derive on disagreement lifts overall by 2+ points |
| 4 | Image-given spatial items (maze, map, graph) | image only; image then text restatement; text only; output length matched | Accuracy; tokens | Restatement closes most of the gap; text only highest |
| 5 | Rotation items (cube, 3D block matching), 40 or more | free text; plain code tool with coordinates; canonical-frame tool | Accuracy | Canonical tool 85%+ vs free text near 50%; plain code tool unknown |
| 6 | Layout questions from limited views (MindCube-like) | direct; CoT; map-then-reason | Accuracy | Map-then-reason +10 or more over direct |
| 7 | Imagine-and-name items (60, Finke-Pinker-Farah style) | low vs high thinking budget x with vs without drawn grid | Mean score 0-5 | Budget raises score; drawn grid adds nothing |
| 8 | Test 1 items | Answer must cite a cell vs no citation | Accuracy; share of drawn steps cited | If under 20% of drawn grids are cited, drawing is decoration |
| 9 | Structure tasks (ARC-like, graphs) | raw grid; object list; edge list | Solve count | Object or edge list beats raw by 5+ points |

## 9. What does not transfer, and why

- **Human RT slopes.** An LLM has no buffer with spatial metric; linear RT by angle does not apply to token output. VLM accuracy falls as human RT rises (r=-0.88 to -0.97) but this is correlational (K24).
- **Verdict on the human debate.** LLM success without pixels (Artificial Phantasia) does not show humans use propositions. LLM failure with images does not show humans use pictures.
- **V1, TMS, PET, fMRI results.** No analogue in a scaffold.
- **Aphantasia samples.** Online, small, label validity questioned. Useful only as a hint that layout and object detail are separate codes (K05).
- **Trained approaches** (MVoT 85.60 vs 61.48 on FrozenLake, VPRL 82.4 vs 38.8, Mirage, MentalThink) need weight updates. Excluded by the no-training design. We may borrow the failure mode (coordinate drift on large boards) as a test, not the fix.
- **Image generators.** A rendered view or image generator did not help or lowered results (o3 with generator 2.77 vs 3.13; renderer 50-62.5%).
- **2024 model numbers.** IsoBench and SpatialEval used older models; gaps are directional.
- **VoT gains as quoted.** "+23.5%" is over no-viz, not CoT. Do not plan on it.
- **"Imagery" for the agent.** The agent writes text. A drawn grid is a text scratchpad, not an image. The word is a metaphor.

## 10. Open questions

1. At equal tokens, does a self-drawn state beat CoT and a coordinate list on frontier 2025-26 models? No token-matched study exists.
2. Which task features predict that drawing helps (hexagon, ASCII art) vs hurts (square grid, ring)? Is there a cheap router rule? Only layout evidence (d04, d07, d11).
3. Does draw-vs-answer agreement raise final accuracy at equal tokens? The signal exists; the gain is untested.
4. Does Artificial Phantasia replicate with other item sets and with Claude models? Is it just symbolic assembly?
5. Does a plain code tool (not a renderer) close the rotation gap for text-only agents? The minimum tool seems to be a canonical frame.
6. Are the IsoBench and SpatialEval gaps shrinking in GPT-5, Gemini 3 and Claude 4.x? Only mazes show it (74 to 59 points).
7. Is the "who makes the picture" explanation true? No same-model, same-item, scaffold-only test exists.
8. On boards of 6x6 and larger, do scaffold-only text forms reach trained image-thought levels (VPRL 82.4)?
9. Human primary data: exact slopes, Ns and failed replications for Kosslyn scanning and Shepard-Metzler are unverified; no meta-analysis of slope exists.
10. Is the image-input effort suppression (d09) general, and does a length-matched prompt remove the gap?

## 11. Sources

[V] = opened this run (page, PDF text, or abstract where marked); [M] = snippet or recalled only.

Human work
- [M] Shepard and Metzler 1971. https://doi.org/10.1126/science.171.3972.701 (a01, b06)
- [M] Cooper and Shepard 1973, via Wikipedia. https://en.wikipedia.org/wiki/Imagery_debate (a26)
- [M] Kosslyn 1973. https://doi.org/10.3758/BF03198623 (b05)
- [V, abstract] Kosslyn, Ball and Reiser 1978. https://pubmed.ncbi.nlm.nih.gov/6223979/ (d19; a02 recalled)
- [M] Finke and Pinker 1982. https://doi.org/10.1037/0278-7393.8.2.142 (a09)
- [M] Chambers and Reisberg 1985. https://doi.org/10.1037/0096-1523.11.3.317 (a11)
- [M] Finke, Pinker and Farah 1989. https://doi.org/10.1207/s15516709cog1301_2 (a10)
- [M] Anderson 1978. https://doi.org/10.1037/0033-295X.85.4.249 (a12)
- [M] Pylyshyn 1981. https://doi.org/10.1037/0033-295X.88.1.16 (a07)
- [V, abstract] Pylyshyn 2002. https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/mental-imagery-in-search-of-a-theory/3B3066B53A4AC8347F6167503E6C7744 (a06)
- [M] Pylyshyn 2003. https://doi.org/10.1016/S1364-6613(03)00003-2 (a27)
- [M] Intons-Peterson 1983 (abstract read via d19). https://doi.org/10.1037/0096-1523.9.3.394 (a08, b09)
- [M] Jolicoeur and Kosslyn 1985. https://doi.org/10.3758/BF03202939 (b08)
- [V, abstract] Kosslyn et al. 1995. https://pubmed.ncbi.nlm.nih.gov/7477406/ (d16, a28)
- [V, abstract] Kosslyn et al. 1999. https://pubmed.ncbi.nlm.nih.gov/10102821/ (d17, b07)
- [M] Kosslyn, Thompson and Ganis 2006. https://doi.org/10.1093/acprof:oso/9780195179088.001.0001 (a16)
- [M] Kosslyn 1980, 1994. https://doi.org/10.4159/harvard.9780674184978 (a17)
- [M] Tye 1991. https://mitpress.mit.edu/9780262700603/the-imagery-debate/ (a18)
- [V] Pearson, Naselaris, Holmes and Kosslyn 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4595480/ (a13)
- [V] Pearson and Kosslyn 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4547292/ (b01-b03, b28)
- [V] Wikipedia: Imagery debate; Mental rotation. https://en.wikipedia.org/wiki/Mental_rotation (a03, a04)
- [V] SEP Mental Imagery (Nanay). https://plato.stanford.edu/entries/mental-imagery/ (a05)
- [V] Wimmer et al. 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5313171/ (a15)
- [V] Borst and Kosslyn 2008 and related (Europe PMC). https://europepmc.org/search?query=mental%20scanning%20images (d20)
- [V] Spagna et al. 2021. https://hal.sorbonne-universite.fr/hal-03241602/document (d15)
- [V] Rotation meta-analyses (Europe PMC). https://europepmc.org/search?query=%22mental%20rotation%22%20meta-analysis (d21)
- [V] Bridge et al. 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3366182/ (a14)
- [M] Zeman et al. 2015. https://doi.org/10.1016/j.cortex.2015.05.019 (a19, b17)
- [V] Bainbridge et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC7856239/ (b10-b12; not re-opened in the cross-check)
- [V] Milton et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8186241/ (b13)
- [V] Thorudottir et al. 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7071355/ (b14)
- [M] Keogh and Pearson 2018. https://doi.org/10.1016/j.cortex.2017.10.012 (b16); Jacobs et al. 2018 via Bainbridge (b15)
- [V, abstract] Chang et al. 2025. https://pubmed.ncbi.nlm.nih.gov/39798565/ (d18)
- [V] Psychonomic Bulletin and Review 2026, vividness. https://pmc.ncbi.nlm.nih.gov/articles/PMC13260255/ (b18)

LLM and AI work
- [V] Wu et al. 2024, Visualization-of-Thought. https://arxiv.org/abs/2404.03622 (a20, a21, b22-b24, c01-c03; PDF re-checked)
- [V] McCarty and Morales 2025-26, Artificial Phantasia. https://arxiv.org/abs/2509.23108 (a22, d06)
- [V] Li et al. 2025, MVoT. https://arxiv.org/abs/2501.07542 (a23, b25, c04, c05; PDF re-checked)
- [V] Zeller et al. 2026. https://arxiv.org/abs/2602.02465 (a24; not re-opened)
- [V] Hayashi and Hirata 2026. https://arxiv.org/abs/2603.26779 (a25, c10, d05)
- [V] Wang et al. 2024, SpatialEval. https://arxiv.org/abs/2406.14852 (b19, c06, c07)
- [V] Fu et al. 2024, IsoBench. https://arxiv.org/abs/2404.01266 (b20, b21)
- [V] Hu et al. 2024, Visual Sketchpad. https://arxiv.org/abs/2406.09403 (b26, c15)
- [V] Yang et al. 2025, Mirage. https://arxiv.org/abs/2506.17218 (b27, c14)
- [V] Wu et al. 2025, SpatiaLite. https://arxiv.org/html/2511.13782 (c08, c09)
- [V] Visual serial processing deficits. https://arxiv.org/html/2509.25142 (c11)
- [V] VisFactor. https://arxiv.org/html/2502.16435 (c12)
- [V] Visual Planning (VPRL). https://arxiv.org/html/2505.11409 (c13)
- [V] Rahmanzadehgervi et al. 2024, Vision language models are blind. https://arxiv.org/html/2407.06581 (c16)
- [V] Xu et al. 2023, ARC object representations. https://arxiv.org/html/2305.18354 (c17)
- [V] Fatemi et al. 2023, Talk like a Graph. https://arxiv.org/html/2310.04560 (c18)
- [V] Momennejad et al. 2023, CogEval. https://arxiv.org/html/2309.15129 (c19)
- [V] Wang et al. 2025, MindCube. https://arxiv.org/abs/2506.21458 (c20)
- [V] Abdou et al. 2021, colour structure. https://arxiv.org/html/2109.06129 (c21)
- [V] Huang et al. 2026, Text2Space. https://arxiv.org/abs/2604.14641 (d01, d02)
- [V] Rodriguez Salgado 2026, MazeBench. https://arxiv.org/abs/2603.26839 (d03, d22)
- [V] Menon, Zemel and Vondrick 2024, Whiteboard-of-Thought. https://arxiv.org/abs/2406.14562 (d04)
- [V] Guo et al. 2026, SiT-Bench. https://arxiv.org/abs/2601.03590 (d07)
- [V] Kancheti et al. 2026. https://arxiv.org/abs/2604.16060 (d08)
- [V] Sun et al. 2026, Reading, Not Thinking. https://arxiv.org/abs/2603.09095 (d09)
- [V] Tian et al. 2026, LAST. https://arxiv.org/abs/2604.09712 (d10)
- [V] Jiang, Qin and Li 2026, SpatialText. https://arxiv.org/abs/2603.03002 (d11; headline numbers not extracted)
- [V] Lin et al. 2026, MentalThink. https://arxiv.org/abs/2607.03530 (d12)
- [V] Yang et al. 2026, unified multimodal thinking. https://arxiv.org/abs/2605.27310 (d13)
- [V] LTD-Bench 2025. https://arxiv.org/abs/2511.02347 (d14)
