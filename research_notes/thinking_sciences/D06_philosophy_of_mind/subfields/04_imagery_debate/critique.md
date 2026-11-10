# Critique: Imagery debate (D06.04)

Cross-check done 2026-11-10. Sources re-opened as PDFs and read: Wu et al. 2024 VoT (2404.03622), Li et al. 2025 MVoT (2501.07542), Hu et al. 2024 Sketchpad (2406.09403), Fu et al. 2024 IsoBench (2404.01266), Wang et al. 2024 SpatialEval (2406.14852). PDFs deleted afterwards. OpenAlex and Semantic Scholar were rate-limited, so McCarty and Morales 2025, SpatiaLite, Zeller 2026, Hayashi and Hirata 2026 and Bainbridge 2021 were NOT re-opened.

## Numbers confirmed
1. VoT Table 1 (GPT-4): CoT 37.02/9.48/48.61/54.15/54.00; no-viz 37.17/10.28/48.49/46.98/35.50; VoT 40.77/14.72/55.28/63.94/59.00; GPT-4V CoT 33.36/5.65/46.59/49.62. Matches c01. p<0.16 vs CoT on NL navigation confirmed.
2. VoT Table 2: accuracy 26.48 and 24.25, compliance 51.14 and 52.01, understanding 65.16 and 77.20. Confirmed.
3. Ring task 52.5% vs 49.5%, 200 instances, size 12. Confirmed.
4. Tiling tracking rate 87.1% VoT vs 57.4% CoT. Confirmed.
5. MVoT: Maze .9295, MiniBehavior .9514, FrozenLake .8560, CoT w/ layout FrozenLake .6148, "90.80%" of CoT FrozenLake errors from wrong coordinates, grid-size decline (.9401 at 3x3). Confirmed.
6. Sketchpad: +11.2% (GPT-4o), +23.4% (GPT-4 Turbo) math average, +41.3 maxflow, 80% same auxiliary line, 92.8% valid plans. Confirmed.
7. IsoBench: 28.7 / 18.7 / 14.9 point gaps, 1,887 samples, IsoCB +9.4, IsoSP +14.4. Confirmed. Note the 28.7 is the largest gap ("as large as"), per model.
8. SpatialEval: +20.1% LLaVA-34B Spatial-Grid without image, +6.5% Maze-Nav with noise, +25.6% GPT-4V text added to image. Confirmed.

## Corrections made
- b24 said removing the word "reasoning" raised tracking by 78.5 points on route planning. Wrong. The paper says the instruction "use ascii-art to visualize" raised complete tracking to 98.5 percent (+78.5) and score to 62.5 percent (+3.5) on natural-language navigation, while removing "reasoning" lowered tracking. c03 had it right. Claim K10 uses the corrected version.
- b22/a20 table cells were garbled in extraction; c01 gives the right row-by-column reading and I adopted it.
- The VoT headline "+23.5%" is over the no-viz arm. Over CoT the gain on NL navigation is +5.0 points with p<0.16 only, and on route planning +3.7 completion. Claims phrase it so.
- b25 says MVoT as plug-in to GPT-4o gives "over +15 points on all three tasks". The garbled MVoT table does not let me confirm this for Maze. Treat as unverified.
- a22 and b27 duplicate c-file entries (a20/b22/c01 are the same VoT paper; a23/b25/c04 the same MVoT; b26/c15 Sketchpad; a25/c10 the same 2026 paper). I counted these as ONE independent source in claim counts.
- a25 says best 62.5%, c10 says GPT-5.2 and gpt-5.4 ranges. Both agree on the 62.5% ceiling. Model name differs (a25 "frontier MLLM", c10 GPT-5.2). Unresolved which exact model.
- Human numbers in a01, a02, a09, a11, a28 are "recalled from memory", so no claim rests on them alone.

## Contradictions between sources
- Pictorial vs propositional: Pearson and Kosslyn 2015 (debate ended, two formats) vs Pylyshyn 2002/2003 and SEP (many say dead, yet not settled). Only reviews opened, no primary neural papers with effect sizes.
- External visual aids: Sketchpad (+11 to +41) and VoT help; SpatialEval, IsoBench, Vision-Models-Are-Blind, Hayashi and Hirata show images hurt or add noise, and a rendered rotation module did not help. Likely reconciled by "who makes the picture": a code-made or text-grid state that the model controls helps; a raw image the model must perceive hurts. This reconciliation is our inference, not tested.
- CoT: wins on Maze with layout text (.98) yet hurts on FrozenLake, VisFactor, Mirage planning. Depends on whether exact coordinates are available.
- VoT helps GPT-4 but not GPT-3.5 or LLaMA3-8B. Model-size limit.
- Imagery as depictive (Kosslyn) vs LLM results that do well without pixels (a22). The LLM data do not decide the human debate; they speak only to which format helps a model.

## Weak spots
- Almost no human primary study was opened this run. The founding numbers (slopes, r=.97, N) are from memory. Replications and failed replications of Kosslyn scanning (e.g. Intons-Peterson, Jolicoeur-Kosslyn) are cited from memory.
- LLM evidence is mostly single papers per task; many are preprints from 2025-2026, not peer-reviewed (a22, a25, a24, c10 to c13).
- VoT's gain over CoT is small and p<0.16 for the main natural-language task; sample sizes (200 maps, 2,520 QA, 796 tiles) fine but one model family (GPT-4).
- No token-equal comparison anywhere. Most LLM papers add tokens (VoT drawing, Sketchpad tool calls) and do not match budgets. This is the key gap for our scaffold.
- Trained approaches (MVoT, VPRL, Mirage) are out of scope for a scaffold-only agent (section 4b).
- Sample sizes in aphantasia are small or online; b18 argues the labels themselves may be invalid.

## Seen only in snippets or abstract
a06 (Pylyshyn 2002, abstract), a27, a01, a02, a07 to a12, a16 to a19, a26, a28, b04 to b09, b15 to b17: not opened or abstract-level only. Also not re-opened this pass: a22, a24, a25, c08 to c12, c16 to c21, b10 to b14.

## GAPS
1. At equal tokens, does a model-drawn text-grid state (VoT) beat plain CoT and a coordinate list on spatial tasks with current frontier models (2025-2026)? No study matches tokens.
2. Which task features predict that a drawn grid helps versus a symbolic or arithmetic recoding (the ring-task loss)? Is there a cheap router rule?
3. Does a self-check of the drawn state (accuracy was only 24-26 percent) raise final accuracy, and at what token cost?
4. Does the Artificial Phantasia result (reasoning LLMs beat humans on imagine-and-name) replicate with other item sets and with Claude models, and is it just symbolic shape assembly?
5. Rotation and transformation tasks: do code-execution tools (not image generators) close the gap for text-only agents? SpatiaLite and Hayashi results suggest rendered views fail but a canonical-view tool works. What is the minimum tool?
6. Primary human data: exact slopes, N, and failed replications for Kosslyn scanning (with naive subjects, Jolicoeur-Kosslyn 1985; Intons-Peterson 1983) and Shepard-Metzler, plus effect sizes of the V1 imagery fMRI/TMS studies. Needed to state the human baseline accurately.
7. Meta-analyses: is there any meta-analysis of mental-rotation or scanning effect sizes, and of V1 activation in imagery? None was found.
8. Are text-to-image gaps (IsoBench, SpatialEval) shrinking in newer models (GPT-5, Gemini 3, Claude 4.x)? Most numbers are 2024 models.
9. Does the "who makes the picture" explanation (self-made text state helps, perceived image hurts) hold in a controlled test with the same model on identical items?
10. For long-horizon plans (6x6 and larger boards), do scaffold-only methods (maps, object lists, ascii) reach the trained visual-planning level, or does the gap (VPRL 82.4 vs 38.8 for Gemini 2.5 Pro at 6x6) need training?

## Gap search results (evidence_d.jsonl d01-d22; claims K26-K34 added, K01-K03, K07-K09, K11, K15, K17, K18, K22 updated)
Search tools were limited: OpenAlex and Semantic Scholar were out of budget, arXiv API rate-limited, WebSearch used 2 of 6 then refused. Papers were found through the Hugging Face paper search, European PMC, PubMed and Crossref, then PDFs were opened.

Closed or mostly closed
- Gap 3 (self-check of drawn state): Text2Space (d01, d02) shows drawn grids are right only 12-50% of the time, and draw-then-answer is below text only. Drawing and answer agreeing gives 89-97% accuracy but only 46-76% of cases agree. A draw-vs-answer agreement check is cheap, but whether it raises final accuracy at equal tokens is still untested. LTD-Bench (d14) agrees that writing is the weak half.
- Gap 5 (rotation tools): Hayashi and Hirata (d05) re-read. The renderer tool stays at 50-62.5%; the canonical-view reset gives 85-97.5% because it makes the task 2D. Minimum tool = canonical frame, not a movie. Only one study, about 40 items, one model. No test of a plain code tool for text-only agents.
- Gap 7 (meta-analyses): found. Spagna 2021 (d15): 27 imagery fMRI experiments, 380 subjects, no early visual cortex activation, BF under 0.33. Rotation meta-analyses (d21) exist for sex differences (d = 0.60) and neural location, but none pools the RT-by-angle slope.
- Gap 8 (gap shrinking): partly. 2026 MazeBench (d03, d22) shows Claude image-vs-text-grid gaps of 74 points (Sonnet 4.6) and 59 (Opus 4.7), so gaps shrink across versions but are far from closed. Sun et al. (d09) show a large part of text-vs-pixel gaps is a rendering and short-output artifact. No GPT-5 or Gemini 3 re-run of IsoBench or SpatialEval was found.

Partly answered
- Gap 2 (router): Whiteboard-of-Thought (d04) gives layout-based evidence (square grid: text wins 98 vs 50; hexagon: drawing wins 8 to 61). SpatialText and SiT-Bench (d07, d11): frame change, rotation and mapping fail in text. A candidate rule is written in K29 but no study tested a router, so status stays contested.
- Gap 4 (Artificial Phantasia): source re-opened (d06). Numbers confirmed; Claude Opus 4.1 matched humans (2.65, p=.590), not beat. Reasoning effort raised GPT-5 from 2.04 to 3.35. Still one group, no independent replication, items solvable with symbolic assembly. Stays open.
- Gap 6 (human primary data): only abstracts of Kosslyn 1978, Kosslyn 1995, 1999, Intons-Peterson 1983, Shepard-Metzler 1971, Borst-Kosslyn 2008 and two scanning follow-ups were read (d16-d20). New: scanning splits into two processes (d20). Exact slopes, r=.97 and Ns are still not verified; Jolicoeur-Kosslyn 1985 has no abstract in PubMed. Open.
- Gap 9 (who makes the picture): MentalThink (d12) holds teacher and supervision fixed and finds SVG 57.8 vs text 42.5 (MindCube), but with training. Unified-model work (d13) shows self-made images can be ignored. Text2Space shows self-drawn text grids do not help without training; MazeBench shows supplied grids help. So the inference is supported by two sides but no same-model, same-item, scaffold-only test exists. Open.
- Gap 10 (6x6 and larger, scaffold-only): MazeBench (d03) shows a supplied text grid gives Opus 4.7 90/100 on mazes up to 20x20 with reasoning tokens, so scaffold-only text can go far. But it is a maze, not FrozenLake, and the grid was handed over. VPRL's 82.4 vs 38.8 comparison was not re-run. Open for the self-built case.

Still open
- Gap 1 (equal tokens, VoT vs CoT vs coordinate list on frontier models): no study found. Closest are Text2Space (negative for self-drawn grids) and MazeBench (tokens fall 4.4-5.8x with a given grid). Highest-value experiment for our agent.

Corrections and cautions for earlier text
- d08: GThinker non-CoT collapse (-23.14) is a format-following failure, not a real CoT gain; use the 6-of-8 count.
- d19, d20, d16-d18: abstract-level only; keep status of K01 and K02 as established-pattern but with unverified numbers.
- K03 downgraded from "neural evidence is the best case" to contested because of the meta-analysis.
