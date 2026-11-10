# Imagery debate: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D06.04-U1 | Does a model-drawn text-grid state (VoT) beat plain CoT and a coordinate list on spatial items with current frontier models? | "Draw state after each step" rule for grid-like tasks | O6 | K07, K27; single-source, GPT-4 only; Text2Space negative (GPT-4.1 66.9 vs 71.7) | Arms: CoT, CoT+coordinate list, VoT. 60+ grid navigation items (4x4 to 8x8), 5 runs each; accuracy at equal tokens | VoT beats both by 3+ points, same sign in 4 of 5 runs | High |
| D06.04-U2 | Does draw-vs-answer agreement work as a cheap verifier that raises final accuracy? | Agreement check, re-derive on disagreement | G (verifier), O6 | K28, K08; single-source; 89-97% accuracy when agreeing, only 46-76% agree | VoT with and without agreement check; U1 items; final accuracy, trigger rate, extra tokens | +2 points overall at equal tokens, trigger rate under 40% | High |
| D06.04-U3 | Is "who makes the picture" the real moderator: given or code-made text state helps, raw image or self-drawn grid does not? | Rule: supply the state in code; never ask the model to perceive a raw image | O6, S | K11, K26, K27, K30; contested; two sides from different papers, no same-model test | Same items, same model: image, self-drawn grid, code-made grid, text coordinates; accuracy and tokens | Code-made grid beats self-drawn by 5+ points and image by 10+ | High |
| D06.04-U4 | Can a cheap router pick form by task layout (text for square grid and lookup; draw or recode for hex, rotation, irregular)? | Router rule in O6 | O6 | K29, K09; contested; Whiteboard-of-Thought square 98 vs 50, hexagon 8 vs 61; ring loses | Mixed layout set; arms: always-text, always-draw, router; accuracy by class | Router beats best fixed arm by 3+ points overall | High |
| D06.04-U5 | Does a canonical-frame code tool close the rotation gap for a text-only agent? | Tool in the toolbox for rotation and 3D matching | O6, tools | K15, K32; contested; one study, about 40 items, 85-97.5% | 40+ rotation items; arms: free text, plain code, canonical-frame tool; accuracy | Tool arm 20+ points above free text on 2 item sets | High |
| D06.04-U6 | Does a symbolic restatement beside a spatial form (or image-to-text first) recover the image gap? | Always restate any image-given spatial input as text | O6 | K12, K11; IsoBench single source (+14.4, +9.4); 2024 models | Image only, image+text, text only; length-matched; maze, map, graph items | Restatement recovers 50%+ of image-to-text gap | Med |
| D06.04-U7 | Does map-then-reason (cognitive map as text first) help layout questions without training? | Map step in layout tasks | O6 | K20; single-source, MindCube 37.8 to 57.8 | Direct, CoT, map-then-reason on 100+ layout items; accuracy | +10 points over CoT | Med |
| D06.04-U8 | Is a drawn state ever used? Does requiring the answer to cite a cell show that drawing is decoration? | Drop draw step when citation rate is low | G10, O6 | K31; single-source, trained models only | Test U1 items; cite-cell requirement; citation rate and accuracy | Drop drawing if cited under 20% or accuracy unchanged | Med |
| D06.04-U9 | Does image input shorten reasoning for our agent, and does a length-matched prompt remove the text-image gap? | Length floor for image-given items | G11 | K30; single-source, 5-19x shorter, font swings 47 points | Image items with and without length-matched instruction; accuracy, output tokens | Gap shrinks 50%+ with length matched | Med |
| D06.04-U10 | Does reasoning budget matter more than the drawn form on symbolic spatial assembly? | Budget rule per item type | G11, G12 | K22, K34; single-source; GPT-5 2.04 to 3.35; generator hurt o3 | 60 imagine-and-name items; low vs high budget x with vs without drawn grid; mean score 0-5 | Budget effect 0.5+ points; grid effect under 0.2 | Med |
| D06.04-U11 | Does the format-instruction wording ("use ascii-art to visualize") move state tracking on our agent? | Fixed wording in O6 prompt | O6 | K10; single-source, tracking +78.5 but score +3.5 | 3 wordings, same items; tracking rate and accuracy | Accuracy +3 points, not only tracking | Low |
| D06.04-U12 | Does object or edge encoding beat raw grids for our ARC-like and graph items? | Encoding choice step in O6 | O6 | K13; established elsewhere (2 sources); needs our model and items | Raw grid, object list, edge list; solve count | Beats raw by 5+ points on our bench | Med |
| D06.04-U13 | Does Sketchpad-style code-drawn diagram help at equal cost? | Diagram tool | tools | K19; single-source, GPT-4o only; GPT-4 Turbo parity fell 80.5 to 71.5 | Plot/aux-line tool vs none; geometry and graph items; accuracy per token | +5 points at equal tokens | Low |
| D06.04-U14 | Does the scaffold-only text form scale to boards of 6x6 and larger, or does the trained gap (VPRL 82.4 vs 38.8) remain? | Large-board rule (coordinate list plus verified state) | O6, S | K16, K17; trained results only; MazeBench shows given grid reaches 90/100 to 20x20 | FrozenLake 6x6 to 10x10; CoT vs coordinate list vs code-made grid; accuracy by size | Accuracy flat (within 10 points) from 4x4 to 8x8 | Med |

## Open questions we cannot test on our bench yet

- **Human slopes and replications.** Exact Shepard-Metzler and Kosslyn slopes, Ns, and failed replications (Jolicoeur-Kosslyn 1985, Intons-Peterson 1983) are unverified. Needs full-text access. No bearing on the agent unless we want a human baseline.
- **Pooled RT-slope meta-analysis.** None exists. Would need someone to run it; not agent-relevant.
- **Aphantasia label validity.** Online samples, criterion confounds (b18). Not testable by us.
- **Whether LLMs "image".** Artificial Phantasia is one group and symbolic items. Replication needs the 60 items and a Claude run; the bench lacks an imagine-and-name item type.
- **Newer-model gaps.** IsoBench and SpatialEval have no 2025-26 re-run. Would need a re-run harness for image items; our bench has few image items.
- **Image generators as thinking aids.** Evidence is negative or mixed (o3 3.13 to 2.77). We have no generator in the loop and the schema excludes training.
- **Trained image thoughts (MVoT, VPRL, Mirage, MentalThink).** Need fine-tuning. Out of scope under 4b.
- **Which tasks on our bench are layout-dependent.** We need a labelled item set by layout class before U4 can run.

## Order to run

1. **U1 with U3 arms (VoT vs CoT vs coordinate list vs code-made grid at equal tokens).** Highest value, no study has this; decides whether any draw step enters O6.
2. **U4 router on mixed layouts.** The literature splits exactly by layout, so one run tells us when to draw and when not.
3. **U5 canonical-frame tool for rotation.** Rotation is the largest unsolved gap; a tool is cheap and the one positive result needs a second source.
