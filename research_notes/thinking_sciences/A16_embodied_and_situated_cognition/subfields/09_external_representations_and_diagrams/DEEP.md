# External representations and diagrams: deep document

*Subfield A16.09. Written 2026-11-01 from evidence_a-d.jsonl (a01-a24, b01-b28, c01-c25, d01-d23), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids in brackets. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Core question: does the notation in which a problem is written change how hard it is, when the content is the same?

The classic answer from human work is yes. Two representations can hold the same information (be "informationally equivalent") and still differ in how easy it is to search them, spot what applies, and draw inferences from them (be "computationally different"). Larkin and Simon (1987) made this claim for diagrams. Zhang and Norman (1994) showed it with Tower of Hanoi isomorphs: the same puzzle was much easier when its rules were enforced by the display than when they had to be remembered. [a07, a09, b01-b03]

Three things are bundled under "external representation":
- **A display that holds state** (a diagram, a table, a board). It acts as memory.
- **A display that enforces rules** (a cup cannot sit on a smaller cup). It acts as a checker.
- **A layout that indexes facts by position.** It acts as a search aid.

For a language model the picture is different in three ways. The model has no eyes of its own: a "diagram" is text (ASCII grid, table, edge list, JSON), code that renders an image, or an image fed to a vision encoder. The model writes its own external representation as it reasons (chain of thought, scratchpad). And the model's weak points (misreading images, losing track of coordinates, drifting in long lists) are not human weak points.

Why it matters for our agent: the schema's operator O6 "Change representation" and state S2 "Represent" both assume that rewriting a problem in other terms can help. This document asks how strong that assumption is, which rewrites help, which hurt, and what must be checked.

Scope limits. Nothing here covers the extended-mind debate, cognitive offloading, or epistemic actions (separate subfields). Where they overlap, they are noted only as links.

## 2. History and theories in depth

**Early AI and isomorphs (1959-1985).** Gelernter's geometry machine (1959) used a stored diagram to reject false subgoals. This is an early case of a diagram used as a checker. [c24, recalled only] Hayes and Simon (1977) and Kotovsky, Hayes and Simon (1985) built Tower of Hanoi isomorphs that differ only in surface and in the rule wording (for example "change" vs "transfer" of objects). Solving times differed hugely, reportedly by about a factor of 16. That figure is unverified recall. [a11, b26]

**Larkin and Simon (1987), "Why a diagram is (sometimes) worth ten thousand words."** The core theory. Two production-system programs worked the same pulley and geometry problems, one from a sentential form and one from a diagrammatic form. The diagram program needed less work. The paper names three processes: search for relevant data, recognition of which rule applies, and inference. Diagrams help mainly because they index information by location. Facts that are needed together sit next to each other, so search is short and recognition is easy. [a07, a08, c23] The paper is a formal model with hand-built programs in tiny domains, not a human experiment. We never opened the full text (publisher blocks bots); everything here about it is second-hand via Zhang and Wang and recall. [d23] The correct DOI is cog1101_4 (Cognitive Science 11(1), 65-100); a07 and a08 carry a wrong URL.

**Stenning and Oberlander (1995).** A competing account. Diagrams help because they limit abstraction: a diagram can only show certain cases, so it cuts the set of allowed inferences. The benefit depends on the task and the person. [a14] This predicts that a diagram helps when it forces the right cases into view, and does nothing when it merely decorates.

**Bauer and Johnson-Laird (1993).** Diagrams sped up deduction on disjunctive problems: about 35 s faster and nearly 30% more valid conclusions than verbal premises (abstract only). The first version, with icons for inclusive vs exclusive "or", did nothing. The diagram worked only after it made the alternative possibilities explicit. [a15, b08] This supports Stenning and Oberlander more than Larkin and Simon.

**Zhang and Norman (1994).** "Distributed cognitive tasks." The theory: the representation of a task is one structure with an internal part (in the head) and an external part (on the display). Moving a rule from the internal to the external part changes the task, not just its load. [a09, b01-b05] Follow-ups: Zhang and Norman (1995) on numeral systems (Roman vs Arabic), Zhang (1997) on external representations as anchors that structure behaviour, Zhang and Wang (2005, 2009). [a10, a13, d22, b06]

**Functional taxonomies.** Cheng (1996): diagrams serve as memory, computation or explanation; the role decides the benefit. Scaife and Rogers (1996): computational offloading, re-representation, graphical constraining. Hegarty (2004): internal and external visualisations interact; displays help most when they free working memory and support mental animation. Ainsworth (2006), DeFT: multiple representations help when they complement, constrain or build understanding, and hurt through translation cost. [a16-a19] All known only as titles or recall.

**Competing explanations, in one list.**
1. Memory aid: the display stores state, so working memory is freed.
2. Search and indexing (Larkin and Simon): location groups facts, so search is cheaper.
3. Constraint (Zhang and Norman; Stenning and Oberlander): the display makes illegal states impossible or hard to reach, and limits allowed inferences.
4. Strategy cue: the display suggests a good strategy (smallest object first).
5. Perceptual inference: the eye picks up relations at a glance.
No single study separates these. Zhang and Norman confound 1, 3 and 4 explicitly. [b04]

**LLM era (2021-2026).** Scratchpads and chain of thought made the model's own written steps its external representation. [c18, a06] Then came a family of "draw it" methods: Visualization-of-Thought (VoT), Whiteboard-of-Thought (WoT), Visual Sketchpad, multimodal VoT, and a conceptual-diagram planner. [b17-b20, c05] In parallel, a quieter line of work showed that the plain-text serialisation of structured data (graphs, tables, grids) moves accuracy by tens of points. [b11-b16, d04, d09] From 2025 on, benchmarks such as SpatialEval, VisGym, SPaRC and SpatiaLite compare text, ASCII and image channels on frontier and reasoning models, and the answers are mixed. [d05, d06, d14, d15]

## 3. Core findings with exact numbers

H = human study, L = LLM study. Figures from garbled tables are flagged in the notes.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| H: more rules held in memory make Hanoi isomorphs harder, per minimum step | Exp 1A: 24 undergraduates, 4 games each. Min steps 2, 4, 7, 8. Time main effect p<.001. Order II < II3 < II234 ~ II23 (II234 vs II23 n.s.) | Zhang and Norman 1994 [b01] | S (no independent replication) |
| H: making rules external lowers difficulty | Exp 1B: II vs II-E3 p<.01 on time; II-E23 vs II-E234 small (p<.03 time, p>.4 steps) | Zhang and Norman 1994 [b02] | S |
| H: external rules are error-proof | Exp 2: 18 subjects, 54 games. Main effect p<.05 (time, steps), p<.005 (errors). All errors on internal rules, none on external ones | Zhang and Norman 1994 [b03] | S |
| H: external rules also cue a strategy | Smallest-first in 16 of 18 games (II-E23), 11 of 18 (II23), 10 of 18 (II2-E3). 52 of 54 games finished in exactly 3 more steps | Zhang and Norman 1994 [b04] | S (confounded with load) |
| H: position beats size or colour for carrying a dimension | Ordinal: location beats size, time p<.01, steps p<.05, errors p<.03; location vs colour n.s. Nominal: location beats size and colour, time p<.003/.016, errors p<.0001/.007; steps n.s. | Zhang and Norman 1994, Exp 3 [b05] | S |
| H: external copy helps only if it matches the internal encoding | Exp 1 (N=24) errors at length 2: E-E 0.52%, E-I 5.2%, I-I 5.7%, F(2,44)=6.08, p<.01. Exp 2 (N=22, reversed encoding) length 3: E-E 1.1%, E-I 15.9%, I-I 20.5%, interaction F(2,40)=6.31, p<.01. In Exp 1 length 3 the mixed rate (8.9%) was above I-I (4.2%) | Zhang and Wang 2009 [b06, b28] | S (same lab) |
| H: diagrams help deduction only if they show alternative cases | About 35 s faster, nearly 30% more valid conclusions; icon-only version had no effect | Bauer and Johnson-Laird 1993 [b08] | S (abstract only) |
| H: teaching which diagram fits which problem raises accuracy, but load rises first | N=67 junior-high students, multiple baseline. Line diagram d=0.88 (t(66)=5.11); table d=1.55; graph d=1.09. Load up d=0.49 first, later down | Ayabe et al. 2022 [b07] | S (no control group) |
| H: a diagram beside an algebra equation raises accuracy | N=61 seventh graders, within-subject; no effect size in abstract | Chu et al. 2017 [d19] | S |
| H: a display raises Hanoi completion but costs moves | 4-disk and 5-disk, undergraduates and Prolific workers; abstract only | Fansher et al. 2022 [d18] | S |
| L: serialisation of the same data swings accuracy by tens of points | Graph encoders gain 4.8 to 61.8 points by task; connected nodes: adjacency 19.8% vs incident 53.8% (PaLM 62B) | Fatemi et al. 2023 [b15, c14] | E (K06) for "format matters"; S (K07) for "incident beats adjacency" |
| L: prompt formatting changes accuracy | Up to 76 points on LLaMA-2-13B; GPT-3.5 JSON +42% relative on MMLU law; GPT-4 more stable (consistency above 0.5; GPT-3.5 below 0.5) | Sclar 2024; He 2024 [b13, b14] | E (K06) |
| L: table format and question order matter a little | GPT-3.5 TabFact: HTML 71.33, NL+sep 70.26, markdown 68.40, JSON 68.04, XML 70.00. Question after table -6.81%; best design 65.43% on seven tasks | Sui et al. 2024 [b11, b12] | S (K08) |
| L: flat grid vs object-level encoding on ARC | GPT-4, 50 easiest tasks 13/50 to 23/50; full training set 81/400 to 97/400; Mini-ARC 35/149 to 45/149 | Xu et al. 2024 [d04] | S (K24) |
| L: same puzzle, image vs text vs scaffolded image | SPaRC, Qwen 3.5 397B: image 14.4, text 38.0, image with text symbols 48.4, cell coordinates 47.8. Qwen 3.5 27B 8.2 to 40.0 | Kaesberg et al. 2026 [d06] | S (supports K06) |
| L: model-drawn text grid (VoT) beats CoT on spatial tasks | NL navigation GPT-4: VoT 59.00, CoT 54.00, no-viz 35.50 (p<0.16 vs CoT). Tiling 63.94 / 54.15 / 46.98 | Wu et al. 2024 [a01, a02, c08] | S (K09) |
| L: drawn states are often wrong | State accuracy 24-26%; constraint compliance 51-52%; correct decisions 65-77% when drawing was right | Wu et al. 2024 [a03, c09] | S (K10) |
| L: drawing loses where text is easy | Ring task: CoT 52.5 vs VoT 49.5 (200 items). WoT square grid: CoT 98 vs WoT 50. MVoT simple grids: text coordinates over 95% | Wu; Menon; Li [a04, c12, c19] | E (K11) |
| L: drawing wins where geometry is awkward | WoT hexagon 8 to 61; circle Direct 14, CoT 25, WoT 41. Overall navigation Direct 33, CoT 42, WoT 52. ASCII words in 3D font 0 to 92.1; bubble font 100 to 42.1 | Menon et al. 2024 [b18, c11, c12] | E (K11) |
| L: drawing tools raise math and vision scores | Average +12.7 math, +8.6 vision; GPT-4o max-flow +41.3 to 66.3; relative depth +12.1 (GPT-4o) vs +2.4 (GPT-4 Turbo) | Hu et al. 2024 [b19, c13] | S (K13) |
| L: rendered state diagram inside a search | Blocksworld simple GPT-4o 35.5 to 90.2; no diagram 58; no diagram schema 72; code only 24. Claude 3.5 Sonnet 54.8 to 98. 50 instances per domain | Borazjanizadeh et al. 2025 [c05-c07, d20] | S (K12); other ablation cells garbled |
| L: same method vs a native reasoner | Blocksworld simple: 90.2 vs o1-preview 97.8; new domains: Barman 30% vs 10% | Borazjanizadeh et al. 2025 [d20] | S (K26) |
| L: diagrams did not help on syllogisms | Sonnet: NL 84.6, Logic 84.6, Linear 81.1, Euler 84.2 (N=285). GPT-4o-mini: 68.8, 71.2, 64.9, 67.0. Neutral class Sonnet NL 63.2 vs Linear 48.4 (60/95 vs 46/95, my p=0.057) | Ando and Mineshima 2026 [c01, c03, d17] | C (K14) |
| L: conversion-case drop is not a diagram effect | Sonnet 16/19 (NL), 13/19 (Linear), 14/19 (Euler); Fisher p 0.45 and 0.69 | Ando and Mineshima re-analysis [d17] | Do not quote as an effect |
| L: vision models misread simple diagrams and trust text over the picture | Four VLMs average 58.07% on 7 simple tasks (best 77.84%); grounding below 20%; contradictory text cuts perception (InternVL2.5-8B to 48.4) | BlindTest; Math Blind [b21, c21] | E (K15) |
| L: text channel often equals or beats the image | SpatialEval Spatial-Grid: Llama-3 text 71.9%, LLaVA-Mistral image 47.1%. GPT-4V +25.6% from vision-only to vision plus text | Wang et al. 2024 [d05] | E (K11, K15) |
| L: layout beats flat text when relations scale with size | Transpose, fine-tuned: text 92.7% (12x12) to 0.8% (20x20); image 90.8% at 20x20. Game of Life text 86.5% to 46.6%; image above 99.7% | Lo et al. 2026 [d07] | S (K27; small fine-tuned models) |
| L: writing the layout first did not help; agreement is a filter | Layout right 12.5-50.6%. Text-only vs ASCII-first answers: GPT-4.1 85.8 vs 83.8, Llama-3-70B 71.7 vs 66.9, Qwen3-30B 75.0 vs 66.6. Agreeing items 88-97% correct; 24-54% dropped | Huang et al. 2026 [d08] | S (K28) |
| L: sound external critique beats self-critique | GPT-4, 100 items per domain. Standard / self-critique / sound critique. Game of 24: 5 / 3 / 36; graph colouring 16 / 2 / 38; Blocksworld 40 / 55 / 60 (87 with first-error feedback) | Stechly et al. 2024 [d12] | S (K25) |
| L: removing rule-violation text hurts all frontier VLMs | VisGym, 17 environments; frontier models average 46.6% easy, 26.0% hard. GPT-5 3 to 4 times better in ASCII than image on most | Wang et al. 2026 [d14] | S (K25) |
| L: sorted edge list is stable; matrices lose | Std across four syntaxes: gpt-oss-20B 5.41, 120B 3.45, Qwen 3B 5.98; fine-tuned G1 9.69 and 10.51 | Herbst et al. 2026 [d09] | S (K29) |
| L: Hanoi collapse is only a format artefact | One prompt at N=15, four models, no counts, unreviewed | Lawsen 2025 [d01] | C (K17), not supported |
| L: stepwise Hanoi still collapses | 10 trials per N; collapse near 8 disks; dialogue fails from N=4 | Dellibarda Varela 2025 [d02] | C (K17) |
| L: algebra forms matter little for current models | 85 problems, 4 forms, 5 models; Cramers V 0.03 to 0.07 | Nath et al. 2026 [d13] | S (K20) |
| L: Tab-CoT small gain | +2.2 average, 5 of 6 arithmetic tasks | Jin and Lu 2023 [c17] | S (K18) |
| L: reasoning models; image channel inconsistent | o4-mini best text-only; Gemini 2.5 Pro saves tokens with vision on easy items; GPT-5 loses 11-14 points without image tools; Gemini 2.5 Pro gains 2.7 without | Lian 2025; Guo 2025 [d15, d21] | S (K26) |
| L: constraint-engine drawing loop | OlympiadBench N=112: baseline 100 for all three; with engine 100 (Gemini 3 Flash), 103 (Sonnet 4.6), 106 (GPT-5.4). Negative on saturated sets | Hu et al. 2026 [d11] | S (K13) |

## 4. Mechanisms and models

Each mechanism is stated so it can be coded.

**4.1 Location indexing (Larkin and Simon).** Store facts in a structure where the facts needed for one decision sit next to each other. In a diagram, a point carries every fact about that point. In text, facts about one object are scattered over many sentences, and finding them costs search. Implementation: keep per-entity records (id, attributes, neighbours) rather than a list of relations in the order they appeared. Fatemi's incident list beating the adjacency list (19.8% vs 53.8%) is the one LLM result that matches, but it is old (PaLM 62B) and one source. [b15] Herbst finds sorted edge lists stable on current models, so the mechanism does not obviously transfer to frontier models. [d09]

**4.2 Constraint enforcement (Zhang and Norman).** A rule held in the prompt can be forgotten or broken. A rule held in code cannot be broken: the checker rejects illegal steps and the model never sees an illegal state. Implementation: a function `legal(state, move) -> ok, reason`. Loop: model proposes a move, code checks, on reject the reason goes back, on accept code renders the new state. Human result: zero errors on external rules (54 games). [b03] LLM analogues: a sound external critique lifted GPT-4 by 30 to 50 points over self-critique; rule-violation messages help frontier VLMs. [d12, d14] The exact control (rules in prompt vs rules in checker on one puzzle) is missing. [K25]

**4.3 Separating load from strategy.** An external display might help because it frees memory, or because it cues a strategy. Test with two checkers: (a) rejects illegal moves only; (b) also lists legal moves. If (b) beats (a), the cue matters beyond load. [K02]

**4.4 Match between internal and external copy.** An external list helps only when its format matches how the internal copy is encoded; a mismatch can be worse than doing it all internally (length 3: 15.9% vs 20.5%, against 1.1% for all external). [b06] For an agent, the "internal copy" is whatever the model carries in its own reasoning text. Implementation: render notes in the same order and naming the model will use when it reads them back. Do not change labels between state blocks.

**4.5 Self-drawn state (VoT).** After each reasoning step, the model writes the current state as a text grid. Wu found a one-word change shifted behaviour: dropping "reasoning" from the prompt made the model draw after answering instead of during reasoning (tracking rate 98.5%, +78.5, in one appendix case). [c10] The weakness: the drawn state is right only 24-26% of the time on their tasks. [a03] So the loop needs a state check: code recomputes the true state from the moves and compares. Text2Space shows the same kind of check works as a filter (agreeing items 88-97% correct vs 71-94% overall) but drops 24-54% of items. [d08] Token cost of the check was not measured anywhere.

**4.6 Draw with code, then look (WoT, Sketchpad).** The model writes plotting code, code runs, the rendered image goes back to a vision model. Gains where the structure is hard to write as numbers (hexagon grids, ASCII art, geometry auxiliary lines). Losses where text coordinates are easy (square grid 98 vs 50). Failure source: perception errors in the model's own picture. [b18, b19] Borazjanizadeh adds a twist: handing the model the plotting code instead of the picture was worse than baseline (24 vs 35.5), so the helpful channel is the rendered result, not the code. [c06]

**4.7 Rendered state inside a search.** Each node of a graph-of-thought search carries a rendered diagram plus a schema describing what it shows. Headline ablations: full 90.2, no diagram 58, no diagram schema 72, code only 24. The gain mixes search and representation. Cost over text-only search: +213 s and +$0.71 for +30 points. [c05, c06] Only these three ablation cells are reliable. [critique]

**4.8 Object-level encoding (ARC).** Replace the flat grid by an object list built by external code: id, colour, cells, bounding box. Flat text breaks object cohesion across lines, and the horizontal-vs-vertical gap disappears with objects. GPT-4: 13/50 to 23/50. [d04] Cheap to build: connected-component labelling in code, then print a JSON list beside the grid.

**4.9 Answer notation.** Ask for a compact generator (a function) instead of an exhaustive list when the list is long. A full list at N=15 is 32,767 moves, about 327,670 tokens at 10 tokens per move. [d01] Whether the Hanoi "collapse" is only a format artefact is not shown. [C]

**4.10 Translation cost.** Keeping two state formats means translating between them. Humans pay a load cost first (d=0.49 up). [b07] For LLMs, layout and answer disagree on 24-54% of items, so every second format opens a place for inconsistency. [d08] Rule: do not carry two formats unless a code check keeps them in sync.

**4.11 Rule of thumb for text vs picture.** Text or ASCII for small symbolic grids and entity lists. Layout or image when positional relations grow with size or glyph shape matters. Model-specific. [K11, K27]

## 5. What holds up

**Replications.** None found for Zhang and Norman 1994 or Larkin and Simon 1987 in about 800 and 1,000 scanned citing titles. [d23] The only follow-ups are from the same lab (Zhang and Wang 2005, 2009) and test a related claim, the memory-aid view. [b06, d22] The Hanoi isomorph effect rests on Kotovsky, Hayes and Simon (1985; second-hand, factor of 16 unverified) plus Zhang and Norman's own Exp 2. [a11, b26] It is a classic, large-effect result with small samples (24 and 18 undergraduates) and exact means only in figures. No effect sizes are available. Treat the direction as solid and the size as unknown.

**Meta-analyses.** Animation vs static graphics meta-analyses exist (Hoffler and Leutner 2007; Berney and Betrancourt 2016) but we hold title-only pointers. No effect size is claimed. [b09, b10]

**Failed or null results (human).**
- Icons for inclusive vs exclusive "or" did nothing. [b08]
- Size vs colour not significant in Zhang and Norman Exp 3; step counts rarely reached significance. [b05]
- II234 vs II23 did not differ: difficulty is not strictly monotone in the number of internal rules. [b01]
- Mixed memory-plus-display is not reliably better than all-internal. Exp 2 length 3: mixed 15.9% vs all-internal 20.5% (slightly better) vs all-external 1.1%. Exp 1 length 3: mixed 8.9% vs all-internal 4.2% (worse). The pattern depends on encoding match. [b06, critique]
- A display raised Hanoi completion but cost moves. [d18]
- Learning a new diagram type raised perceived load before it fell. [b07]

**Failed or null results (LLM).**
- VoT vs CoT on NL navigation: p<0.16. VoT lost on the ring task (49.5 vs 52.5). [a01, a04]
- WoT lost on square grid (50 vs 98 CoT) and on bubble-font ASCII (100 to 42.1). [b18, c11]
- MVoT: text coordinates beat it on easy mazes (CoT over 95 vs 92.95). [c19]
- Syllogisms: no diagram condition beat text overall for either model. [c01]
- Text2Space: writing ASCII layouts first did not raise answer accuracy for any of six models. [d08]
- Image alone vs text alone on spatial questions: image rarely wins. [d05]
- Constraint-checked canvas: +0, +3, +6 of 112 on a saturated set; negative on Geo3K and PGPS9K. [d11]
- Gemini 2.5 Pro gained nothing from image tools while GPT-5 gained 11-14 points. [d21]
- Hanoi function-output claim: not supported (one prompt, no counts); stepwise replication still collapsed near 8 disks. [d01, d02]
- Code-only access to the rendered plot: worse than baseline (24 vs 35.5). [c06]

**Moderators that survive.**
1. Task type: spatial or awkward geometry vs symbolic or simple. [K11]
2. Size: layout wins as grid size grows (small fine-tuned models). [K27]
3. Perception: when the picture is the bottleneck, scaffolds that ease perception give large gains. SPaRC start, end and gap cells were found 69%, 48%, 21% of the time on the plain image and 100% with text symbols. [d06]
4. Model: best format and benefit of vision differ by model and vendor. [b13, d15, d21]
5. Base-model strength: weaker models gain more from format fixes (GPT-3.5 vs GPT-4), but GPT-3.5 and LLaMA3-8B gain less from VoT than GPT-4. Saturated benchmarks show no gain. [b13, c09, d11]
6. Reader quality: a sketch helps only if the reader can parse it (relative depth +12.1 vs +2.4). [b19]

**Interventions that worked (with caveats).**
- A sound external checker (large, GPT-4 era). [d12]
- An externally built object list for ARC (13 to 23 of 50). [d04]
- Scaffolded image input on SPaRC. [d06]
- Drawing tools on math and vision, model-dependent. [b19]
- Rendered diagrams inside a search for planning (authors only). [c05]
- Teaching which diagram fits which problem (humans, no control group). [b07]

**Interventions that did not work.**
- Unchecked self-drawn layouts. [d08]
- Self-critique instead of a checker. [d12]
- Giving the Hanoi algorithm in the prompt did not move the collapse point. [b23]
- A diagram next to the text for syllogisms. [c01]
- Extra structure hints in table prompts, which sometimes hurt cell lookup. [b12]

## 6. Language models

**Basic behaviour.**
- Representation sensitivity is real and persistent. Meaning-preserving format changes move few-shot accuracy by up to 76 points on LLaMA-2-13B, and sensitivity persists with scale and instruction tuning. [b14] GPT-4 is steadier than GPT-3.5. [b13] On five current models, equivalent algebra forms change correctness only slightly (Cramers V 0.03 to 0.07). [d13] Sensitivity shrinks with model strength but does not vanish.
- Content effects mirror humans: Sonnet symbolic items 95.6 vs incongruent 79.2 in NL. [c04, b24]
- Linear text traces are weak at global graph structure; chain and clique cases defeat standard prompting; build-a-graph prompting gave +3.07 to +16.85. [b16]

**Reading images.**
- Vision models miss simple relations: 58.07% average on seven line and circle tasks. The encoder holds the information; the language side fails to decode it. [b21]
- Recognition is good, relations are weak: GPT-4o 93.1 recognition, 82.3 reasoning on real diagrams, with background-knowledge shortcuts. [c20]
- Math diagrams: grounding below 20%; contradictory text lowers perception; training on primitive graphs gave +79% grounding and +3-4% on reasoning. [c21]
- The same graph in a different layout is not recognised (humans 88-100%; MLLMs near random except o1). [c22]
- When text and image conflict, the model follows the text. An image is an unreliable channel for fine detail. [K15, E]

**Text vs image vs ASCII.**
- SpatialEval: image-only rarely beats text-only; adding text to the image helps. [d05]
- VisGym: GPT-5 3 to 4 times better with ASCII than image on most symbolic tasks; Matchstick reverses because ASCII distorts glyphs. [d14]
- SpatiaLite: o4-mini best on text only; image alone harms (Wood Slide near 0); Gemini 2.5 Pro saves tokens with vision on easy items. Reasoning models average over 10,000 tokens on hard items and reason mostly in language. [d15]
- SPaRC: the plain image is worst, but a scaffolded image (text symbols 48.4) beats text (38.0) on the 397B model. [d06]
- Fine-tuned small models on transpose, Game of Life, LU: layout survives size growth, flat text collapses. [d07]

**Self-drawn state methods.**
- VoT: +23.5 over no-viz on NL navigation for GPT-4, +5 over CoT (not significant). State accuracy 24-26%. [a01, a03]
- WoT: hexagon 8 to 61; overall 33 / 42 / 52. [b18]
- Sketchpad: +12.7 math, +8.6 vision average; very model-dependent. [b19]
- MVoT (trained): FrozenLake 85.6 where CoT falls below Direct. [b20]
- Visual Planning with RL: VPRL 80.6 average exact match vs Gemini 2.5 Pro (think) 43.7. This is trained, not a scaffold. [d16]
- Borazjanizadeh: Blocksworld 35.5 to 90.2 (GPT-4o), Claude 3.5 Sonnet 54.8 to 98. [c05, c07]
- Text2Space: ASCII-first answers lower than text-only for all six models. [d08]

**Frontier and reasoning models.**
- No paper re-ran VoT or WoT with a 2025-26 reasoning model as base. [critique gap 3]
- Indirect data: o1-preview beats Visual Thinking on simple Blocksworld (97.8 vs 90.2) and loses on harder domains. [d20] GPT-5 gains from image tools, Gemini 2.5 Pro does not. [d21] A constraint engine adds 0-6 items of 112. [d11]
- Reading: the gain from drawing has not vanished, but it is no longer general. It is bounded by the base model and mostly sits where perception or exact state is the missing resource.

**Checkers.**
- GPT-4 with a sound checker: Game of 24 5 to 36/38, graph colouring 16 to 38/37, Blocksworld 40 to 60/87; self-critique 3, 2, 55. The LLM verifier was right on 61 of 100 plans; the sound VAL checker reached 88/100. [d12]
- Removing rule-violation text lowers every model in VisGym. [d14]

**Answer notation.** Tab-CoT +2.2 average. [c17] Hanoi generator-vs-list claim: contested, no counts. [d01, d02, d03]

**Cost.**
- Draw-in-search: +213 s and +$0.71 for +30 points. Average 31% faster and 36% cheaper than a graph-of-thought baseline. [c05, c07]
- Constraint engine: thinking tokens fall 36% (GeoSketch) and 14% (OlympiadBench). [d11]
- No study measured the token cost of a state check or of a second format.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status as in claims.jsonl.

### Add now (established)

1. **A1. Treat notation as a source of variance in every comparison.** Run each scaffold comparison over 3 or more formats of the same state and report the range, not one run. Part: G7. Status [E], K06. Evidence b13, b14, b15, b11, c15, c16, d09, d10, d06.
2. **A2. Isomorphic rewrites in every test set.** Each bench item gets 2 or 3 meaning-preserving surface forms; report the spread. A scaffold tuned on one notation may not transfer. Part: G3. Status [E], K20. Evidence b24, b25, c04, c22, d13, d06, d09.
3. **A3. Prefer structured text state to image state.** Vision models misread simple diagrams and trust text over the picture. If an image is used, add a code check for text-vs-image consistency. Part: G2, O6. Status [E], K15. Evidence b21, c20, c21, c22, d05, d08.
4. **A4. O6 means "choose the representation by task", not "always draw".** Use a text state for simple layouts. Use a table, object list or drawn layout only when geometry or entity count makes text coordinates error-prone. Part: O6. Status [E] for the pattern (K11); the cut-off is model-specific and unmeasured, so the routing threshold is a Test first item (U3). Evidence a04, b18, c12, b20, c19, d05, d06, d07, d14, d15.
5. **A5. Code-enforced rules where rules exist.** When a task has a legality rule, the program rejects illegal steps and returns the reason; the model does not police rules from the prompt. Part: G2/G3. Status [E] (K01: external rules, zero errors in 54 games for humans; sound external critique +30 to 50 points for GPT-4). The exact LLM control (rules in prompt vs checker) is a Test first item (U1). Evidence b01, b02, b03, a09, a11, b26, d12, d14, d18.
6. **A6. Written reasoning is the baseline arm.** Plain chain of thought or scratchpad is the control in every notation test. Part: O1/O6. Status [E], K19. Evidence a06, c18, a05.

### Test first (single-source or contested)

7. **T1. Per-step state redraw (VoT style) with a code check of the redrawn state.** Part: S4/G3, O6. [S] K09, K10, K28. Evidence a01, a03, d08. Use only with the check.
8. **T2. Object list beside the raw grid for grid items (ARC style).** Part: S2/O6. [S] K24. Evidence d04.
9. **T3. Checker with legal-move list vs checker that only rejects.** Separates load from strategy. Part: G2, O6. [S] K02. Evidence b04.
10. **T4. Position-keyed table vs labelled list for the same facts.** Part: O6, memory. [S] K03. Evidence b05.
11. **T5. Question before data.** Part: S1/O6. [S] K08. Evidence b12.
12. **T6. Per-entity incident record vs flat edge list for relational state.** Part: memory, O6. [S] K07, K29. Evidence b15, d09, d10.
13. **T7. Case-split table for disjunctive logic, with a decorative control.** Part: O6. [S] K05. Evidence b08, a14, a15.
14. **T8. Rendered compact state vs generator code vs prose inside a planning loop.** Part: O6/O1. [S] K12. Evidence c05, c06, c07, d20.
15. **T9. Match note order to use order.** Part: memory. [S] K04. Evidence b06.
16. **T10. Compact generator vs exhaustive list for long-output tasks.** Part: O6. [C] K17. Evidence d01, d02, d03.
17. **T11. Logic items: use a countermodel search, not a picture.** Part: O6/S4. [C] K14. Evidence c01, d17.
18. **T12. Cost of a second format.** Part: O6. [S] K21. Evidence b07, d08.
19. **T13. Model-specific on/off for any visual channel.** Part: O6. [S] K26. Evidence d15, d21, d11.
20. **T14. Tabular step log vs prose steps.** Part: O1/O6. [S] K18. Evidence c17.

## 8. Concrete tests on our bench

All arms at equal total tokens (reasoning plus output). Report the range across 3 surface forms and 3 seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Hanoi-like puzzle in 3 isomorphic surface forms (pegs, cups, ordered-list transfer) | Prose only, compared across forms | Solve rate and spread across forms | Spread under 5 points on a frontier model (algebra spread was small); a larger spread marks a fragile scaffold |
| B2 | Same puzzle, 6-8 disks | (a) rules in prompt, (b) prompt plus checker that rejects illegal moves, (c) checker plus legal-move list | Illegal-move rate, solve rate | (b) near-zero illegal moves; (c) over (b) only if the strategy cue matters |
| B3 | Grid navigation, 6x6 to 20x20, plus a hexagonal layout | (a) text coordinates, (b) per-step text-grid redraw, (c) redraw plus code check | Accuracy by size, state accuracy | Crossover size where (b) beats (a); (c) over (b) when state accuracy is below 60% |
| B4 | ARC-like grid tasks (50 easy) | (a) flat grid, (b) grid plus object list from code | Solved items | Several more items solved (13 to 23 of 50 in d04); likely smaller on a modern reasoner |
| B5 | Relational queries on 30-node graphs | Sorted edge list, adjacency list, per-entity incident list, table | Accuracy per query type | Incident list wins on neighbourhood queries by a few points; K29 suggests the gap is small on frontier models |
| B6 | Disjunctive logic (3-premise case splits) | Plain premises, case-split table, decorative diagram | Valid conclusions | Case-split table above plain; decorative equal to plain |
| B7 | Same state, question first vs last | Order only | Accuracy | A few points at most; a null is likely on frontier models |
| B8 | Planning (Blocksworld 4-8 blocks) | Prose state, rendered compact state, generator code | Solve rate, tokens | Rendered above prose if the model reads images well; code-only below baseline (c06) |
| B9 | Long enumeration (Hanoi 12-15) | Exhaustive list vs request for a program | Valid solution by execution | Program arm succeeds more; if the list arm also succeeds, the collapse was only length |
| B10 | Items with notes carried across 5 steps | Notes ordered as used vs scrambled | Error rate | Ordered a few points lower |
| B11 | Any item set with a visual channel | Model's own channel on vs off | Accuracy, tokens | Sign depends on model; do not import vendor results |
| B12 | Agent with two state formats | One format vs two (with and without code sync) | Extra tokens per step, disagreements | Disagreement 24-54% without sync (d08); near 0 with sync |

## 9. What does not transfer, and why

- **Human working-memory relief.** Zhang and Norman's main mechanism is relief of a small working memory. A model re-reads its whole context every step, so there is no equivalent bottleneck of a few items. The cost that remains is attention dilution and drift, which is different. [b01-b03]
- **Perceptual inference from the eye.** Human diagram benefit relies on seeing relations at a glance. Vision encoders miss simple relations (58.07% on easy tasks). [b21]
- **Teaching which diagram fits.** Ayabe's 67-student instruction effect cannot be copied by a prompt; load-first-then-fall is a human learning curve. [b07]
- **Physical constraint.** A cup that cannot be placed is physics. A text rule can be ignored by the model unless code blocks the step. The program must be the display. [b03]
- **Larkin and Simon's production systems.** Hand-built programs in tiny domains with no noise. LLM search is not production-system search. [c23]
- **Fine-tuned layout results.** The 92.7% to 0.8% transpose collapse comes from small fine-tuned models on synthetic tasks. A frontier reasoning model may not collapse. [d07]
- **Trained image-thought results.** MVoT and VPRL change weights; our agent controls only the scaffold. [b20, d16]
- **GPT-4-era gains.** VoT, WoT, Sketchpad and the search planners were measured on 2023-24 models. Reasoning models change the base rate. [critique gap 3]
- **Syllogism null (Ando).** Two models, diagrams placed beside the text; it may not apply where a diagram replaces text. [c01]

## 10. Open questions

1. Does a representation change of the same puzzle (prose, table, rendered grid, generator code) change a modern LLM's solve rate at equal tokens? True isomorphs of one puzzle have not been run. [K23]
2. Does a code legality checker beat the same rules in the prompt, and does it remove rule violations as in humans? [K01, K25]
3. Do VoT, WoT, Sketchpad and Visual Thinking still help a 2025-26 reasoning model with native reasoning on? [K26]
4. What are the exact means and effect sizes of Zhang and Norman 1994? Is there any replication or failed replication of it or of Larkin and Simon 1987? [K22]
5. Is there a rule that predicts text vs drawing across size and entity count on a frontier model? [K11, K27]
6. What does a code check of the redrawn state cost in tokens, and does it raise end accuracy? [K10, K28]
7. Why did diagrams not help on syllogisms when humans benefit? Format, or answer bias? [K14]
8. Which list format is best for linked facts on current frontier models, and does question-first ordering still hold? [K29, K08]
9. Is the Hanoi function-output claim true when counted? [K17]
10. Does keeping two state formats cost extra tokens and errors in an agent? [K21]
11. Is the external-rule effect load relief or a strategy cue? [K02]
12. Larkin and Simon (1987) was never opened by us. Its details here are recall and citation.

## 11. Sources

[V] opened (full text or page), [M] snippet or abstract only, as recorded in the evidence files.

**Human and theory**
- [M] Larkin and Simon (1987), Why a diagram is (sometimes) worth ten thousand words. https://doi.org/10.1207/s15516709cog1101_4 (not opened; publisher blocked; ids cog1103_2 and 10.1111/j.1551-6708.1987.tb00863.x in the evidence files are wrong or unverified)
- [V] Zhang and Norman (1994), Representations in distributed cognitive tasks. https://pages.ucsd.edu/~scoulson/203/zhang.pdf
- [M] Zhang and Norman (1995), A representational analysis of numeration systems. https://doi.org/10.1016/0010-0277(95)00674-3
- [M] Zhang (1997), The nature of external representations in problem solving. https://doi.org/10.1207/s15516709cog2102_3
- [V] Zhang and Wang (2009), PLoS ONE. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2714979/
- [M] Zhang and Wang (2005), QJEP A 58:817-838. https://pubmed.ncbi.nlm.nih.gov/16194937/
- [M] Kotovsky, Hayes and Simon (1985). https://doi.org/10.1016/0010-0285(85)90009-X (second-hand via Zhang and Norman)
- [M] Kotovsky and Simon (1990). https://doi.org/10.1016/0010-0285(90)90015-3
- [M] Stenning and Oberlander (1995). https://doi.org/10.1207/s15516709cog1902_1
- [M] Bauer and Johnson-Laird (1993). https://doi.org/10.1111/j.1467-9280.1993.tb00584.x
- [M] Cheng (1996), Functional roles for the cognitive analysis of diagrams (no DOI)
- [M] Scaife and Rogers (1996). https://doi.org/10.1006/ijhc.1996.0048
- [M] Hegarty (2004). https://doi.org/10.1016/j.tics.2004.07.001
- [M] Ainsworth (2006), DeFT. https://doi.org/10.1016/j.learninstruc.2006.03.001
- [V] Ayabe, Manalo and de Vries (2022). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9574201/
- [V] Fansher, Shah and Helie (2022), Cognition 224:105041 (abstract page only). https://pubmed.ncbi.nlm.nih.gov/35152055/
- [V] Chu, Rittle-Johnson and Fyfe (2017) (abstract only). https://doi.org/10.1111/bjep.12149
- [M] Berney and Betrancourt (2016). https://doi.org/10.1016/j.compedu.2016.06.005
- [M] Hoffler and Leutner (2007). https://doi.org/10.1016/j.learninstruc.2007.09.013
- [M] Gelernter (1959). https://doi.org/10.1145/1460299.1460312
- [M] Citation-list search record (Semantic Scholar). https://api.semanticscholar.org/graph/v1/paper/ee577ea4b36c2d6ed120e4068a05bfb33c00e492/citations

**LLM studies**
- [V] Wu et al. (2024), Visualization-of-Thought. https://arxiv.org/abs/2404.03622
- [V] Menon et al. (2024), Whiteboard-of-Thought. https://arxiv.org/abs/2406.14562
- [V] Hu et al. (2024), Visual Sketchpad. https://arxiv.org/abs/2406.09403
- [V] Li et al. (2025), MVoT. https://arxiv.org/abs/2501.07542
- [V] Borazjanizadeh et al. (2025), Visualizing Thought. https://arxiv.org/abs/2503.11790
- [V] Ando and Mineshima (2026), Do Diagrams Help LLMs Reason? https://arxiv.org/abs/2607.23513
- [V] Fatemi et al. (2023), Talk like a graph. https://arxiv.org/abs/2310.04560
- [V] Wang et al. (2023), NLGraph. https://arxiv.org/abs/2305.10037
- [V] Sui et al. (2024), Table Meets LLM. https://arxiv.org/abs/2305.13062
- [V] He et al. (2024), prompt formatting. https://arxiv.org/abs/2411.10541
- [V] Sclar et al. (2024), FormatSpread. https://arxiv.org/abs/2310.11324
- [V] Jin and Lu (2023), Tab-CoT. https://arxiv.org/abs/2305.17812
- [V] Yao et al. (2023), Tree of Thoughts. https://arxiv.org/pdf/2305.10601
- [V] Wei et al. (2022), chain of thought (abstract-level claims only). https://arxiv.org/pdf/2201.11903
- [V] Nye et al. (2021), Scratchpads (abstract only in effect). https://arxiv.org/abs/2112.00114
- [M] Lampinen et al. (2024), content effects. https://arxiv.org/abs/2207.07051
- [M] Wu et al. (2024), Reasoning or reciting? https://arxiv.org/abs/2307.02477
- [V] Rahmanzadehgervi et al. (2025), Vision language models are blind. https://arxiv.org/abs/2407.06581
- [V] Hou et al. (2025), Do VLMs really understand visual language? https://arxiv.org/abs/2410.00193
- [V] Sun et al. (2026), Math Blind. https://arxiv.org/abs/2503.20745
- [V] Babaiee et al. (2025), Visual Graph Arena. https://arxiv.org/abs/2506.06242
- [V] Shojaee et al. (2025), The illusion of thinking. https://arxiv.org/abs/2506.06941
- [V] Lawsen (2025). https://arxiv.org/abs/2506.09250
- [V] Dellibarda Varela et al. (2025). https://arxiv.org/abs/2507.01231
- [V] Khan et al. (2025). https://arxiv.org/abs/2506.18957
- [V] Xu et al. (2024), LLMs and ARC, object-based representations. https://arxiv.org/abs/2305.18354
- [V] Wang et al. (2024), SpatialEval. https://arxiv.org/abs/2406.14852
- [V] Kaesberg et al. (2026), SPaRC scaffolds. https://arxiv.org/abs/2608.21170
- [V] Lo et al. (2026), Serialization friction. https://arxiv.org/abs/2604.27272
- [V] Huang et al. (2026), Text2Space. https://arxiv.org/abs/2604.14641
- [V] Herbst et al. (2026), Lost in Serialization. https://arxiv.org/abs/2511.10234
- [V] Podstawski (2026), Graph property inference in small LMs. https://arxiv.org/abs/2603.06635
- [V] Hu et al. (2026), Draw2Think. https://arxiv.org/abs/2605.20743
- [V] Stechly et al. (2024), self-verification limits; Valmeekam et al. (2023). https://arxiv.org/abs/2402.08115
- [V] Nath et al. (2026), representation robustness. https://arxiv.org/abs/2607.20520
- [V] Wang et al. (2026), VisGym. https://arxiv.org/abs/2601.16973
- [V] Lian et al. (2025), SpatiaLite. https://arxiv.org/abs/2511.13782
- [V] Xu et al. (2026), Visual Planning. https://arxiv.org/abs/2505.11409
- [V] Guo et al. (2025), VisualToolBench. https://arxiv.org/abs/2510.12712
