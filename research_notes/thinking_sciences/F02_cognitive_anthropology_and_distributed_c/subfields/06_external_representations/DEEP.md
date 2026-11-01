# External representations: deep document

Subfield F02.06, cognitive anthropology and distributed cognition. Schema parts touched: S2 (restate the problem), O6 (change representation), G2/G3 (checks on real output). Evidence ids (a01 to d16) and claim ids (F02.06-K01 to K22) refer to the jsonl files in this folder. Status marks: [E] established, [S] single-source, [C] contested.

Reading note. Larkin and Simon 1987 was never opened (publisher 403). Kotovsky et al. 1985, Zhang 1997, Kirsh and Maglio 1994, Chuderski 2021 and McDowell and Jacobs 2017 are second-hand. Zhang and Norman 1994 was opened. No 2025-2026 frontier reasoning model appears in the format studies. Every LLM number below comes from 2022-2025 models unless said otherwise.

## 1. What it is

An external representation is any form of a problem that sits outside the head: a diagram, a table, a set of physical tokens, a written list, a grid of symbols, a program. Distributed cognition says the unit of analysis is the whole system of internal and external representations. The task is not "in the head" or "on the page". It is spread across both.

Three ideas run through the field.

1. **Isomorphs differ.** Two problems can have the same abstract logic and still differ greatly in difficulty, because the surface form changes what the solver must remember, search and compute.
2. **Where a rule lives matters.** A rule can be held in memory, stated in text, or enforced by the medium (a physical object that cannot be moved wrongly). Rules in the medium cost no memory and cannot be broken.
3. **Equal information is not equal cost.** A diagram and a sentence can hold the same facts, but the diagram puts related facts side by side, so search is shorter and recognition is easier (Larkin and Simon). This holds only "sometimes": the needed inferences must be easy to see in that form.

For our agent the question is concrete. At S2 and in operator O6 the program may rewrite the problem into another written form: a code-built object list, a ledger, a table, a grid, a rendered image, a natural-frequency restatement. Which form, when, and does it pay at equal tokens? The program (not the model) can build and check the form. That is where the human findings and the LLM findings meet.

Scope boundary. Acting on materials to get new information (epistemic action) belongs to sibling subfield 07. Memory offloading, extended mind and cognitive artefacts have their own documents. Here we cover the written or drawn form of the problem itself.

## 2. History and theories in depth

**Kotovsky, Hayes and Simon 1985 (a08, not opened).** Tower of Hanoi isomorphs (Dish-move versus Peg-move and others) differed greatly in solving time though the problem space was identical. Zhang and Norman say their step and error ordering agrees with this paper's time ordering.

**Larkin and Simon 1987 (a09, b25, not opened).** A computational account. Two representations can be informationally equivalent (every fact derivable from one is derivable from the other) yet not computationally equivalent (the cost of search and recognition differs). Diagrams index facts by location, so related facts sit together, which cuts search and aids recognition. They ran production-system models on a pulley problem and a supply-and-demand problem. The title word "sometimes" is the limit: a diagram helps only if the needed inferences are easy to recognise. This is a model with worked examples, not a human experiment with effect sizes. No LLM replication exists (K16, c26).

**Zhang and Norman 1994 (a01 to a07, opened).** Cognitive Science 18:87-122. Theory: the representational system of a task is a set of internal and external representations that together represent the abstract task structure. Method: split a task into levels (formal structure, rules, dimensions) and vary each level alone. Four experiments on Tower of Hanoi isomorphs. Cover stories (restaurant, oranges) differ across conditions, an uncontrolled confound. Descriptive theory, not a quantitative model.

**Zhang 1997 (a24, not opened).** Extended the idea to tic-tac-toe isomorphs and number scrabble. External representations are not just memory aids: they give perceptual cues, constrain action and change the task.

**Kirsh and Maglio 1994 (a25, not opened).** Tetris players rotate pieces to find the fit, not to place them. Covered in sibling 07.

**Gigerenzer and Hoffrage 1995 (a10, b06).** Natural-frequency formats ("10 of 1000 people have the disease; 8 of those 10 test positive; 95 of the other 990 test positive") raise Bayesian reasoning compared with probabilities. This is the "moving tokens helps Bayes" line in the subfield note. Rival account: the nested-set structure, not the frequency wording, does the work (b07, b08).

**Insight and interaction line (b01 to b04, b26, b27).** Fioratou and Cowley 2009 reported that real rings beat paper on the cheap-necklace problem. Interactivity accounts say action offloads memory or reveals possibilities. Chuderski 2021 ran a large test and found no benefit except on the Eight Coins problem. Spiridonov 2025 and Macchi 2026 also found no action benefit. Macchi 2026 offers a third account: the form can carry a missing fact.

**LLM-era turn (2022-2025).** The same question is asked of models: Program of Thoughts (c18), Mind's Eye (a23), Visualization-of-Thought (a11), Sketchpad (a22), Whiteboard-of-Thought (a14, d04), Talk like a Graph (a21), table-format studies (a17, c01), ARC object lists (b16), IsoBench (c17). Key difference from the human work: the program can build and verify the form with code, which people cannot do.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Moving rules into the medium cut errors (Hanoi isomorphs) | Exp 2, N=18 within-subject: time and steps p<.05, errors p<.005; II23 (all rules internal) vs II-E23 errors p<.001; all errors on internal rules, none on external. Exp 1B: zero errors when rules 2-4 were physical | Zhang and Norman 1994 (a03, a04) | [S] one lab, one task family, cover-story confound |
| Rule count changes difficulty non-linearly | Exp 1A N=24; min steps 2/4/7/8; II < II3 < II234 ~ II23; main effect p<.001 | a02 | [S] |
| Dimension coding matters | Exp 3, nine isomorphs; location beat size (time p<.01) and, nominal, beat size and colour (time p<.003, errors p<.0001); no interactions | a06 | [S] |
| Same logic, different isomorph, different difficulty (people) | Kotovsky 1985 order agrees with Z&N Exp 2 | a08 (not opened) | [E] but second-hand |
| Natural frequencies beat probabilities (people) | G&H Study 1: Bayesian algorithm in 46% (standard menu) and 50% (short menu) of answers with frequencies vs 16% and 28% with probabilities | a10 (as corrected in critique) | [E] |
| Format effect in a large sample | N=577 medical students: 36% (probabilities) vs 68% (frequencies), OR 11.55, 95% CI 7.92-16.87; after 1 h training 64% with probabilities; both together 89%; 173/577 improved vs 8/577 worse | b09 | [E] |
| Meta-analysis of natural frequencies | 35 articles, 226 estimates; about 4% (probability) vs 24% (frequency); visual aids 4 to 26% and 24 to 47% | McDowell and Jacobs 2017 via b07, b08 | [E] (second-hand numbers) |
| Visual aids usually help Bayes, not always | Control error 16% vs 5-7% with table or graph in one study; Khan 2015: only 20% solved even with visuals; representation training about 3x rule training at 2 months | b05 (narrative review) | [E] direction, [C] size |
| Format vs nested sets | Training with chance or frequency wording, both with visual scaffolds: 64-74% correct, about 55% at 1 week, BF01=5 for no wording difference | b08 (second-hand) | [C] |
| Acting on materials does not reliably help insight | Pencil problem 12/44 (27.3%) paper vs 14/43 (32.6%) physical, chi2=0.29, p=.59 | b01 | [C] |
| Matchstick algebra interactivity failed to replicate | N=105, 88, 74; static-sticks baseline about 86% | b04 | [C] |
| Interactive benefit found with weak controls | Cheap necklace 43% vs 6% (chi2=12.42, N=63); Fioratou and Cowley 30% vs 3%; other labs' controls 43% | b03, b26, b02 | [C] |
| Picture content can matter | Realistic matchstick photo 79.3% (23/29) vs stylised 46.7% (14/30), chi2=6.72, p=.010, N=59 | b01, b27 | [S] |
| Text beats image of same problem for LLMs | Claude-3 Opus 28.7 pts worse on images, GPT-4 Turbo 18.7, Gemini Pro 14.9 | IsoBench (c17) | [E] |
| VLMs given text+image often below their LLM backbone | Mixtral-7B text 62.1% vs LLaVA-1.6-Mistral-7B 47.1% on Spatial-Grid; removing the image raised LLaVA-1.6-34B by 20.1% | SpatialEval (a15, critique) | [E] |
| VLMs treat image as noise | Noise or random image gave gains on Maze-Nav (e.g. +6.5% for LLaVA-1.6-Vicuna-13B) | a16 | [S] |
| Models trust text over image on conflict | Open models lost nearly 50% of accuracy under corrupted text; "focus on image" prompt moved text preference only 16.8% to 14.2% | Deng 2025 (b23) | [E] |
| VLMs fail simple diagram facts | 4 VLMs average 58.07% on BlindTest (chance 24%); best Sonnet-3.5 77.84% | b17 | [S] |
| Written state grid (VoT) helps a strong model on spatial tasks | GPT-4 tiling 63.94 vs CoT 54.15 vs no-viz 46.98 vs GPT-4V 49.62; route success 14.72 vs 9.48; next step 55.28 vs 48.61; NL navigation 59.00 vs 54.00 (p<0.16) | Wu 2024 (a11, b10) | [S] |
| VoT fails when task reduces to arithmetic | Ring navigation N=200: CoT 52.5 vs VoT 49.5 | a13 | [S] |
| VoT needs a strong model | NL navigation CoT vs VoT: GPT-3.5 8.50 vs 9.00; Llama3-8B 16.50 vs 15.50; Llama3-70B 26.00 vs 32.50 | b11 | [S] |
| Self-drawn state is often wrong | State accuracy 26.48% (nav) and 24.25% (tiling); constraint compliance 51.14% and 52.01%; correct decision given accurate drawing 65.16% and 77.20% | a12 | [E] with K04 |
| Written state is the failure point in text CoT | FrozenLake: 90.80% of CoT errors were wrong hole coordinates; CoT 0.9401 at 3x3 to 0.3911 at 6x6 | MVoT (b12, d06), fine-tuned 7B | [E] with a12 |
| Rendered image vs text depends on geometry | GPT-4o tile navigation, CoT vs WoT: hexagon 8 vs 61, triangle 26 vs 55, circle 25 vs 41, rhombus 51 vs 52, square 98 vs 50 | Whiteboard-of-Thought (d04) | [S] |
| Most rendered-image errors are perception | 80.8% ceiling on real MNIST images | d05 | [S] |
| Code-built object list beats raw grid | GPT-4 ARC easiest 50: 13 vs 23; full train set 97/400 vs 81/400; Mini-ARC 45/149 vs 35/149; more edge detail lowered scores | Xu 2024 (b16, c09, c10) | [S] for GPT-4; direction consistent with others |
| Executed simulation grounds small models | GPT-3 1.3B + simulation 29.8% vs 175B vanilla 29% zero-shot (about 135x size gap); average gain 18.4% zero-shot and 34.2% few-shot over all sizes; large-model row 27.9 and 46.0 | Mind's Eye (a23, critique) | [E] for tool grounding |
| Executed sketches add accuracy | GPT-4o +11.2% and GPT-4 Turbo +23.4% on math (Table 1); max flow 66.3% (+41.3); V*Bench +14.3 (GPT-4o); tokens 2.2k-3.1k per math or graph sample, 26.6k on V*Bench | Sketchpad (a22, b13, d07) | [S] no matched-token baseline |
| Program-of-thought over CoT | About +12% average across 8 numeric datasets; +8% math, +15% finance few-shot | c18 | [E] numeric |
| Graph encoding changes accuracy a lot | Connected nodes: adjacency 19.8% vs incident 53.8%; encoder boost 4.8% to 61.8%; zero-shot CoT worse on basic tasks (53.8 to 35.2, 68.8 to 39.0) | Fatemi 2023 (a21, c14) | [E] |
| Table serialisation changes accuracy | GPT-4 size detection: HTML 83.43, XML 80.21, Markdown 82.12, NL+sep 73.12; GPT-3.5 HTML 67.00 vs about 42; question-before-table cost 14.33 pts | Sui 2024 (a17, a18) | [E] |
| No single best format | GPT-3.5 reverse lookup best XML 55.00, worst HTML 47.33; GPT-3.5 prefers JSON, GPT-4 prefers Markdown | a17, c15 | [E] |
| Prompt formatting spread | Up to 76 pts (LLaMA-2-13B); median 7.5; 20% of tasks at least 15 pts; GPT-3.5 up to 56, median 6.4; 21 models can fall to random with a poor template | Sclar 2024 (b20), Voronov 2024 (b22) | [E] for older models |
| Bracketed rows help weak models | Gemini Pro WikiTQ 38.4 to 57.3 with brackets and CoT; GPT models barely change (42.7 vs 42.2) | Deng 2024 (c01, c02) | [S] |
| Image tables usually worse than text for GPT-4 | GPT-4 image averages 52.8 to 58.0; Gemini Pro 36.8 to 46.2 | c03, b18 | [C] some long numeric tables favour images |
| Model-picked alternative thought format | AutoForm: +5.4 GPT-3.5, +5.7 Gemini Pro, +3.3 GPT-4; Coin Flip GPT-3.5 22.2 to 38.0 | Chen 2024 (c04) | [S] modest |
| Terse written forms hold accuracy at a fraction of tokens | Sketch-of-Thought: token cut over 74%, accuracy within 1% (GPT-4o 84.55 vs CoT 84.64); Chain of Draft GSM8K GPT-4o 91.1 vs 95.4 at about 40 vs 200 tokens | d08, d09 | [E] for non-reasoning models |
| Output structure can kill reasoning | gpt-4o-mini GSM8K free text 94.57, format-restricting instructions 87.17, JSON-mode 86.95, JSON-schema 91.71; JSON-mode put answer before reason in 100% of GPT-3.5 responses | Tam 2024 (d11) | [S] |
| Gain depends on baseline | Rephrase-and-Respond GPT-4 average 64.95 to 89.77 vs direct zero-shot; near-ceiling tasks +0 to 2; baseline lacked CoT | d15 | [S] |
| Code on a noisy table loses to text | Noisy format: symbolic drops 31.8% vs textual 20.5%; text-guided symbolic reaches 59.1% on calculation questions | TableMaster (d10) | [S] |
| Output form explains part of "reasoning collapse" | Hanoi failures partly due to demanding the full move list; models still stumble from about 8 disks | c22 | [S] |
| Fact position changes accuracy (indirect locality analogue) | GPT-3.5 drops over 20 points mid-context, below closed-book 56.1%; oracle 88.3% | Lost in the Middle (d13) | [E] |

## 4. Mechanisms and models

Each mechanism is stated so a program can use it.

**M1. Rules enforced by the medium (Zhang and Norman).** A legal-move check that rejects an illegal state is an "external rule". The solver spends no memory on the rule and cannot violate it. In Exp 2 all errors fell on internal rules. Engineering form: a validator `legal(state, move)`; the model proposes moves; the program rejects and logs illegal ones. Two proposed reasons for the benefit (a05): external rules are checked by looking rather than by mental load that interferes with planning, and the recursive strategy is easier to find when rules are external. The data do not separate them.

**M2. Computational, not informational, equivalence (Larkin and Simon).** Cost of a form = search cost to find the facts an inference needs + recognition cost to see that an operator applies. Locality cuts both. Engineering form: put the facts one step needs in the same line or row as the step; index facts by the key the next step looks up. Indirect LLM support: answer position moves GPT-3.5 over 20 points (d13). No direct test (K16).

**M3. Dimension binding (Zhang and Norman Exp 3).** Location-coded dimensions beat size and colour codes. Authors link this to location binding separate feature maps (Treisman and Gelade). For text this suggests giving each object an explicit position (row and column index) rather than leaving position implicit in token order. Not tested for LLMs.

**M4. Written state as working memory (VoT).** After each step the model writes the whole state in a fixed grid. The next step reads the grid instead of earlier prose. Works for a strong model (GPT-4) on spatial tasks that do not reduce to arithmetic. Weak point: the written state is right only about a quarter of the time (24-26%), and decisions given a right drawing are right 65-77%. The gain scales with drawing accuracy. Engineering form: after each model-written state, a program recomputes the true state from the move list and compares. A mismatch is reported back (G2: revise from real output). MVoT shows the same failure on FrozenLake (90.80% of text-CoT errors were wrong hole coordinates).

**M5. Code-built representation (ARC objects, Mind's Eye, Sketchpad, Program of Thoughts, Chain-of-Table).** The program computes the better form: connected components with colour, bounding box and position; a physics simulation result; a plot; an executed program output. The model reads it. Engineering form: deterministic extractor, then text. Boundaries: more detail hurt on ARC (edge information lowered scores), and on a noisy raw table code did worse than text (31.8% vs 20.5% drop), so normalise before building. The gain mixes form and tool use; no paper isolates form alone.

**M6. Rendered image from code (Whiteboard-of-Thought).** The model writes drawing code, the program runs it, the image goes back to a multimodal model. Helps when text has no natural coordinate form (hexagon 8 to 61). Hurts where text already has one (square 98 to 50). Remaining error is mostly perception (80.8% ceiling on real MNIST). Rule: render only after a pilot on the item class.

**M7. Frequency and nested-set restatement (Gigerenzer and Hoffrage).** Rewrite "P(D)=1%, P(+|D)=80%, P(+|not D)=9.6%" as counts out of a reference class (say 1000), with positives split into true and false positives. The answer is a ratio of two counts. Engineering form: a program converts probabilities to counts; the model reads counts, or the program does the division (G5). For LLMs this is unmeasured (K11).

**M8. Format selection.** AutoForm: the model picks a non-prose format (table, logic, code, list) before CoT; +3.3 to +5.7 points. Sketch-of-Thought: a DistilBERT router trained once on 14,200 machine-labelled items picks one of three terse forms per question (cost amortised). Few-item per-task pilot selection is untested.

**M9. Format noise floor.** Surface form (separators, casing, HTML vs Markdown vs JSON) shifts accuracy by a median 6 to 8 points and up to 56 to 76 points in 2023 models. Engineering form: run 4 or more meaning-preserving phrasings of each test item; the spread is the noise floor; credit a new representation only above it.

**M10. Do not remove the thinking channel.** Structured-output limits that put the answer before the reasoning remove the reasoning (100% of GPT-3.5 JSON-mode responses). Keep reasoning free-form or reason-first and structure only the final answer.

## 5. What holds up

**Holds up (human).**
- Isomorphs differ in difficulty (Kotovsky 1985 and Z&N agree). [E]
- Natural frequencies beat probabilities for Bayes: G&H Study 1 (16% vs 46/50%), N=577 (36% vs 68%), a 35-article meta-analysis. Training adds. Both together reached 89%. [E]
- Visual aids add on top of frequencies (4 to 26% and 24 to 47% in the meta-analysis). [E]

**Weaker than the headline.**
- Absolute Bayesian accuracy stays low even with the best format: typically 20 to 50% (b07), 20% in Khan 2015 even with visuals. Format helps; it does not solve.
- Mechanism is contested: frequency wording vs nested-set structure vs training and numeracy (b08).
- Zhang and Norman: N=18 to 24, undergraduates, one task family, differing cover stories, fixed start and end positions in Exp 2.

**Failed or contested replications (insight and interaction).**
- Pencil problem: 27.3% paper vs 32.6% physical, no effect (b01).
- Matchstick algebra interactivity: three experiments, N=105/88/74, no benefit; hand movement may interfere with loosening higher-level constraints; baseline about 86% leaves little room (b04).
- Large test of nine insight problems: no difference except Eight Coins (b02, second-hand).
- Positive results (cheap necklace 43% vs 6%; 30% vs 3%) used paper controls far below the 43% other labs got for the same problem. Control rates for the same problem range 3% to 43%, and for triangle of coins 22% to 85%. This is the weak-control pattern (K12).
- What did work in Macchi 2026 was a picture that carried the key fact (79.3% vs 46.7%), not action.

**Moderators that recur.**
- Model strength: VoT and bracket tricks help weaker or mid models, not always the strongest (b11, c02).
- Task reducibility: if the task reduces to arithmetic, drawing does not help (ring 52.5 vs 49.5).
- Natural form of the data: render when text has no coordinate form (hexagon), not when it has (square).
- Verification of the drawn state (three-quarters wrong without it).
- Baseline strength: rewrite gains shrink against a CoT baseline or near ceiling (K19).
- Detail level: more detail can hurt (ARC edges).
- Input noise: code on a messy input is worse than text.

**Interventions that worked.** Code-built object lists (ARC), executed simulation (Mind's Eye), executed code (PoT), executed sketches (Sketchpad), incident-list graph encoding, HTML for tables, written grid state with a strong model on spatial tasks, terse structured reasoning for token savings.

**Interventions that did not.** Pictures added to text for VLMs (often below text-only); zero-shot CoT on basic graph tasks; VoT on weak models and on arithmetic-reducible tasks; JSON-mode that puts the answer first; handling real materials for insight problems in the larger tests; more ARC detail.

## 6. Language models

**Text beats image for the same problem, for models trained on text.** IsoBench: Claude-3 Opus 28.7 pts, GPT-4 Turbo 18.7, Gemini Pro 14.9 worse on images (c17). SpatialEval: a 15-point gap, Mixtral-7B text vs LLaVA-Mistral image on Spatial-Grid; removing the image raised LLaVA-1.6-34B by 20.1% (a15). Models lean on text and mistrust the image: noise images gave gains (Maze-Nav, +6.5% in one model), and when text and image disagree, ten VLMs follow the text (b23). BlindTest: 58.07% average on simple diagram facts (b17). All 2024 open or early closed VLMs.

**Rendering helps when text has no natural coordinates.** Whiteboard-of-Thought (GPT-4o, one model): hexagon 8 to 61, triangle 26 to 55, circle 25 to 41, square 98 to 50 (d04). ASCII word recognition: text 0% on several types, WoT up to 92.1% (d05). Perception limits it.

**Written state helps strong models on spatial tasks, with caveats.** VoT with GPT-4: +9.8 on tiling, +5.3 on route success, but only p<0.16 on NL navigation vs CoT. Route planning stays at 14.7%. Weak models gain nothing (GPT-3.5 8.50 to 9.00). Drawn states are right about a quarter of the time. The written state is also where text CoT breaks (FrozenLake 90.80%). No equal-token comparison exists (K17).

**Tool-built forms help most.** ARC: 13/50 to 23/50 with object lists. Mind's Eye: a 1.3B model with simulation matched a 175B model. PoT: about +12%. Sketchpad: +11.2% (GPT-4o) and +23.4% (GPT-4 Turbo) on math, max flow +41.3. These mix tool and form, and cost tokens (Sketchpad 2.2k-3.1k per sample, V*Bench 26.6k) with no matched baseline.

**Serialisation changes accuracy, task by task.** Graphs: 19.8% vs 53.8%. Tables: HTML 83.43 vs NL+sep 73.12 (GPT-4), GPT-3.5 67 vs 42. For GPT-4, gaps on many table tasks are under 5 points (c11), and for GPT models bracket forms barely matter (c01). Sensitivity falls with model strength in He et al. (GPT-4-1106 most robust, dispersion below 0.036), but Sclar says it persists with size and Tam shows a 7.6-point loss in gpt-4o-mini from JSON-mode on GSM8K. So "spread shrinks for strong models" is [C] (K06, K22). No 2025-2026 reasoning model has a measured spread. Araya 2025 shows reasoning models (o3-mini, R1, Gemini Flash 2.0) did not use natural frequencies unprompted and used them only shallowly when told (d01).

**Frequency formats for LLMs: a hole.** The claim "LLMs show natural-frequency gains" runs through Dasgupta/Lampinen 2022, which contains no Bayes or frequency test (d03), and CogBias 2026, which repeats it without measurement (d02). Only data: one item, three reasoning models (d01). CogBias found prompt-level debiasing backfired on the Judgment family that holds Bayes items.

**Format choice by the model.** AutoForm +3.3 (GPT-4) to +5.7 (Gemini Pro). A trained router keeps accuracy within 1% at about 26% of CoT tokens (d08). Chain of Draft: 91.1 vs 95.4 on GSM8K (GPT-4o) at about a fifth of the tokens (d09). All non-reasoning models.

**Format limits.** Structured-output limits cost reasoning (94.57 vs 86.95). Output form (full move list) explains part of the Hanoi "collapse" (c22). Procedures learned in code or graph form do not reliably transfer to natural language in trained models (c23, training study).

**What changed things, by how much.** Tool-built form +10 to +41 points on selected tasks; written state +5 to +10 for a strong model; model-chosen format +3 to +6; graph encoder choice up to +34 (19.8 to 53.8); format noise median ±7; image instead of text −15 to −29 for text-trained models.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established)

1. **Write the problem state in a code-checked written form: recompute it from the move list and report mismatches.** Part G2/G3. [E] K04. Evidence a12, b12, d06. Self-drawn state is right only about a quarter of the time; the check is the lever.
2. **Where possible, let the program build the representation (object lists, tables, simulation or program output) and give the model that.** Part O6. [E] K05. Evidence b16, c09, c10, a23, a22, b13, c20, c18, d10, d04. Normalise noisy input first. Do not add more detail than needed (ARC edge information hurt).
3. **Keep text-describable states in text for a text-trained model; do not add an image of the same state.** Part O6. [E] K02, K09. Evidence c17, a15, a16, b17, b23, c03.
4. **Treat form as a variable with no universal winner; test form per task class.** Part S2/O6. [E] K07. Evidence a17, c14, a14, c07, b14, d04, d05.
5. **Use terse written forms as the baseline arm for any form change.** Part S2/G7. [E] K08, K17. Evidence c04, c05, c12, c19, c18, d08, d09. Terse forms keep accuracy at 20 to 26% of CoT tokens, so a token-capped CoT is the fair baseline.
6. **Report every format or rewrite gain against plain CoT and terse CoT, with selection tokens counted, and above the format noise floor.** Part G7. Evidence d15, b20, d11, d12. Method rule from the format studies, not a claim of benefit.
7. **Keep the reasoning channel free; structure only the final answer; reason before answer.** Part G2/O6. [S] K20, evidence d11. One paper, but following the rule costs nothing.

### Test first (not yet established)

| Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|
| Rules stated in prose vs enforced by a validator that rejects illegal moves | G2/G3 | [S] K01 | a02-a05 | Human-only, one lab |
| VoT-style state grid, code-checked, vs plain CoT, equal tokens | S2/O6 | [S] K03 | a11, b10, c06, c07, b11, a13 | Strong-model-only, no token control |
| Natural-frequency or nested-set restatement on Bayes items | O6 | [S] K10, K11 | a10, b05, b07, b09, d01-d03 | Human result, never measured for LLMs |
| Four-plus meaning-preserving formats on our model, spread measured | S2/O6 | [C] K06, K22 | b20, d11, d12 | Spread on reasoning models unmeasured |
| Form selection from a few-item pilot | S2/O6 | [S] K07, K08, K18 | c04, d08, d04 | Router needs labelled data; pilot untested |
| Rendered image vs text coordinates, chosen by task feature | O6 | [S] K18 | d04, d05 | One model, one task |
| Adjacent vs scattered relevant facts (Larkin and Simon locality) | O6 | [S] K16 | d13 | No direct test |
| Hidden constraint stated explicitly for insight-type items | S2/O6 | [C] K13, K21 | b01, b27, d14 | Human picture result, no LLM test |
| Answer as program/generator vs explicit list | S2 | [S] K14 | c22 | Part of the Hanoi collapse |
| Same procedure as code vs prose | O6 | [S] K15 | c23 | Training study only |
| Act-on-it step for insight problems | none | [C] K12 | b01-b04, b26 | Evidence says leave out by default; only test against a strong baseline |

## 8. Concrete tests on our bench

All arms get the same total token budget, counting every selection, rendering, checking and correction token. Each item set is run under 4 or more meaning-preserving phrasings so the format noise floor is known. Paired per-item comparison with a significance test; at least 30 items per class, 60 where the expected effect is under 10 points.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Grid spatial items (tiling, FrozenLake-style, route planning) | (a) plain CoT, (b) token-capped terse CoT, (c) free-form written grid state each step, (d) written grid + code check that recomputes the true state and returns mismatches | Final accuracy; state accuracy per step | (d) above (c) above (a) on a strong model; (d) minus (c) at least 5 points; no gain on arithmetic-reducible items |
| T2 | ARC portfolio items | (a) raw row-text grid, (b) code-built object list, (c) object list with edges, (d) grid under rotations/transposes | Solved items, paired | (b) above (a) by about 5 to 15 points; (c) not above (b) |
| T3 | Hanoi-like puzzles with N disks | Rules in prose vs validator rejects illegal moves; also answer as program vs full move list | Rule violations; solve rate | Violations near zero with validator; solve rate up |
| T4 | 30 Bayes items with varied priors | Probability vs natural-frequency vs nested-set restatement (program-made) vs terse CoT; several models | Exact-answer accuracy | Unknown; frequency or nested-set 5+ points above probability if the human result transfers |
| T5 | 30 items per task class, 4+ formats (plain, Markdown, JSON, HTML, YAML) | Each scaffold under each format | Range of pass rate | Spread above 5 points means form must be fixed by pilot; below 3 means ignore form |
| T6 | Tile navigation with natural and awkward coordinates | Text grid vs code-rendered image; pilot of 5 to 10 items picks | Accuracy at equal tokens | Image wins only on awkward geometry; pilot choice at least as good as best fixed form |
| T7 | Relevant facts adjacent vs scattered | Same content, two orderings, plain CoT | Accuracy | Scattered lower by 5+ points |
| T8 | BRAINTEASER-like items | Plain, terse CoT, "constraint stated" restatement | Solve rate | Gain only if baseline is not near ceiling |
| T9 | Any item set | Answer-first JSON vs reason-first vs free text | Accuracy | Answer-first lowest |
| T10 | Table and graph items | Raw vs normalised vs code-built table | Accuracy | Code on noisy input lower than text; normalised above both |

## 9. What does not transfer, and why

- **Physical enforcement.** A physical disc cannot be placed wrongly; text can. Only a program-side validator reproduces the effect. The benefit arrives through the code, not through the model's representation.
- **Acting on materials (insight).** Interactivity results do not generalise even in people. A model has no hands; its "action" is more tokens. Skip as a default step.
- **Human perception of diagrams.** Larkin and Simon's recognition operators assume a visual system that finds adjacency cheaply. A VLM's encoder holds the information but the language model fails to decode it (b17). Text-trained models prefer text.
- **Hanoi and undergraduates.** One task family, N=18 to 24. Not evidence about a general reasoner.
- **Natural-frequency training effects.** A one-hour training in people is a different intervention from rewording a prompt.
- **Fine-tuned gains.** MVoT and the 71.6% ARC result (d16) are fine-tuned; they are not prompt-only gains.
- **Drawing is not free.** Sketchpad uses 2.2k to 26.6k tokens per sample. Under G7 the gain must pay for them.
- **Old-model sensitivity numbers.** 76-point spreads are LLaMA-2-13B few-shot classification; do not expect them on a reasoning model.

## 10. Open questions

1. Does a code-validated written state beat a free-form drawn state and plain CoT at equal total tokens on a 2025-2026 frontier model? (K17)
2. Do 2025-2026 reasoning models still show the format spread of GPT-3.5 and GPT-4? (K22)
3. Do natural-frequency or nested-set restatements help LLMs on Bayes items? (K11)
4. Can rule-in-medium vs rule-in-text (K01) and Larkin and Simon locality (K16) be tested on LLMs directly?
5. What detail level of object list is best on ARC, and does it hold for current models?
6. What task feature predicts that a rendered image beats text? (K18)
7. Can form be selected from a cheap per-task pilot at net-positive tokens?
8. Does making a hidden constraint explicit transfer to LLM insight puzzles? (K21)
9. Does a strong plain-CoT baseline erase rewrite gains? (K19)
10. What are the original Larkin and Simon 1987 and Chuderski 2021 numbers? Unread; re-open if load-bearing.
11. Is the frequency advantage due to wording or to nested sets, and which would a model use?

## 11. Sources

[V] opened this session, [M] snippet or second-hand only.

- [V] Zhang and Norman 1994. https://pages.ucsd.edu/~scoulson/203/zhang.pdf (a01-a07)
- [M] Zhang and Norman 1994 publisher page. https://doi.org/10.1207/s15516709cog1803_3 (b24)
- [M] Kotovsky, Hayes and Simon 1985. https://doi.org/10.1016/0010-0285(85)90009-X (a08)
- [M] Larkin and Simon 1987. https://doi.org/10.1111/j.1551-6708.1987.tb00863.x (a09, b25)
- [V] Gigerenzer and Hoffrage 1995, Study 1 numbers reopened in the critique pass. https://doi.org/10.1037/0033-295X.102.4.684 (a10, b06)
- [M] Zhang 1997. https://doi.org/10.1207/s15516709cog2102_3 (a24)
- [M] Kirsh and Maglio 1994. https://doi.org/10.1207/s15516709cog1804_1 (a25)
- [V] Macchi, Inglese, Caravona 2026. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13208192/ (b01, b27)
- [M] Chuderski et al. 2021 (via Macchi 2026). same URL (b02)
- [M] Fioratou and Cowley 2009 (via Macchi 2026). same URL (b26)
- [V] Incubation and interactivity in insight problem solving 2020. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6994426/ (b03)
- [V] Spiridonov et al. 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12862482/ (b04)
- [V] Cui, Lo, Liu 2023. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10059693/ (b05)
- [M] McDowell and Jacobs 2017 (via b08). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13481750/ (b07)
- [V] Adaptive toolbox and expertise review 2026. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13481750/ (b08)
- [V] Berlin study of 577 medical students 2023. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9903474/ (b09)
- [V] Wu et al. 2024, Visualization-of-Thought. https://arxiv.org/abs/2404.03622 (a11-a13, b10, b11, c06-c08)
- [V] Menon, Zemel, Vondrick 2024, Whiteboard-of-Thought. https://arxiv.org/abs/2406.14562 (a14, d04, d05)
- [V] Wang et al. 2024, SpatialEval. https://arxiv.org/abs/2406.14852 (a15, a16)
- [V] Sui et al. 2024, Table Meets LLM. https://arxiv.org/abs/2305.13062 (a17, a18, b19, c11, c12)
- [V] He et al. 2024, Prompt formatting. https://arxiv.org/abs/2411.10541 (a19, b21, c15)
- [V] Sclar et al. 2024. https://arxiv.org/abs/2310.11324 (a20, b20, c16, d12)
- [V] Fatemi, Halcrow, Perozzi 2023. https://arxiv.org/abs/2310.04560 (a21, b14, c13, c14)
- [V] Hu et al. 2024, Visual Sketchpad. https://arxiv.org/abs/2406.09403 (a22, b13, c20, d07)
- [V] Liu et al. 2022, Mind's Eye. https://arxiv.org/abs/2210.05359 (a23)
- [V] Li et al. 2025, MVoT. https://arxiv.org/abs/2501.07542 (b12, d06)
- [V] Wang et al. 2023, NLGraph. https://arxiv.org/abs/2305.10037 (b15; abstract read closely)
- [V] Xu et al. 2024, ARC object representations. https://arxiv.org/abs/2305.18354 (b16, c09, c10)
- [V] Rahmanzadehgervi et al. 2024, VLMs are blind. https://arxiv.org/abs/2407.06581 (b17)
- [V] Deng et al. 2024, Tables as texts or images. https://arxiv.org/abs/2402.12424 (b18, c01-c03; cell mapping garbled)
- [V] Voronov et al. 2024, Mind your format. https://arxiv.org/abs/2401.06766 (b22)
- [V] Deng et al. 2025, Words or vision. https://arxiv.org/abs/2503.02199 (b23)
- [V] Chen et al. 2024, Beyond natural language (AutoForm). https://arxiv.org/abs/2402.18439 (c04, c05)
- [V] Fu et al. 2024, IsoBench. https://arxiv.org/abs/2404.01266 (c17)
- [V] Chen et al. 2022, Program of Thoughts. https://arxiv.org/abs/2211.12588 (c18)
- [V] Wang et al. 2024, Chain-of-Table. https://arxiv.org/abs/2401.04398 (c19)
- [V] Dasgupta/Lampinen et al. content effects. https://arxiv.org/abs/2207.07051 (c21, d03, c26)
- [V] Rethinking the Illusion of Thinking 2025. https://arxiv.org/abs/2507.01231 (c22)
- [V] Can LLMs generalise procedures across representations 2026. https://arxiv.org/abs/2602.03542 (c23)
- [V] Huang et al. 2026, CogBias. https://arxiv.org/abs/2604.01366 (d02; c24, c25 are snippet only [M])
- [V] Araya 2025. https://arxiv.org/abs/2503.15268 (d01)
- [V] Aytes, Baek, Hwang 2025, Sketch-of-Thought. https://arxiv.org/abs/2503.05179 (d08)
- [V] Xu et al. 2025, Chain of Draft. https://arxiv.org/abs/2502.18600 (d09)
- [V] Cao and Liu 2026, TableMaster. https://arxiv.org/abs/2501.19378 (d10)
- [V] Tam et al. 2024, Let me speak freely. https://arxiv.org/abs/2408.02442 (d11)
- [V] Liu et al. 2024, Lost in the Middle. https://arxiv.org/abs/2307.03172 (d13)
- [V] Jiang et al. 2023, BRAINTEASER. https://arxiv.org/abs/2310.05057 (d14)
- [V] Deng et al. 2024, Rephrase and Respond. https://arxiv.org/abs/2311.04205 (d15)
- [V] Franzen et al. 2025, Product of Experts on ARC. https://arxiv.org/abs/2505.07859 (d16)
