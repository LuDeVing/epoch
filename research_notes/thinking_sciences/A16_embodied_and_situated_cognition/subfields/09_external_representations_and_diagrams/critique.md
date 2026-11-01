# Critique and cross-check: A16.09 External representations and diagrams

Checked 2026-11-01. Sources re-opened (full text via pdftotext or PMC HTML): Wu et al. 2024 VoT (2404.03622), Borazjanizadeh et al. 2025 (2503.11790), Fatemi et al. 2023 (2310.04560), Menon et al. 2024 WoT (2406.14562), Ando and Mineshima 2026 (2607.23513), Hu et al. 2024 Sketchpad (2406.09403), Lawsen 2025 (2506.09250), Zhang and Norman 1994 (UCSD PDF), Sui et al. 2024 (2305.13062), Zhang and Wang 2009 (PMC2714979).

## Corrections and confirmations

Confirmed as stated:
- VoT NL navigation 59.00 / CoT 54.00 / no-viz 35.50; tiling 63.94 / 54.15 / 46.98; state accuracy 24-26%; 65-77%; ring 52.5 vs 49.5 on 200 items (a01-a04, b17, c08, c09). Table 1 is still garbled in extraction, but these cells are consistent with the paper's text. Route planning VoT 40.77 / 14.72 / 55.28 is the best reading, not certain.
- Fatemi: adjacency 19.8 vs incident 53.8 on connected nodes, PaLM 62B zero-shot; range 4.8-61.8 (b15, c14).
- WoT: hexagon 8 to 61; square grid CoT 98 vs WoT 50; overall Direct 33, CoT 42, WoT 52; ASCII 3D 92.1, Bubble 100 to 42.1 (b18, c11, c12).
- Sketchpad: abstract gives +12.7 math and +8.6 vision; body gives +11.2 (GPT-4o) and +23.4 (GPT-4 Turbo) on math; max-flow 66.3 (+41.3); relative depth +12.1 vs +2.4 (b19, c13).
- Ando and Mineshima: all cells in c01-c04 match Table (NL 84.6, Logic 84.6, Linear 81.1, Euler 84.2 for Sonnet; conversion 84.2/84.2/68.4/73.7; neutral NL 63.2, Linear 48.4; symbolic 95.6, incongruent 79.2; mini 82.2 to 56.7). The arXiv id 2607.23513 is real (v1, 26 Jul 2026).
- Zhang and Norman: 24 undergraduates in Exp 1; 18 subjects, 54 games in Exp 2; "none were for external rules"; 16 of 18 smallest-first in II-E23; 52 of 54 finished in three steps (b01-b04).
- Sui et al.: -6.81% question after table, -30.38% zero-shot vs 1-shot with HTML, 65.43% best on seven tasks (b12). The 6.76% HTML figure is from a text line about the benchmark, not TabFact (as b11 notes).
- Zhang and Wang 2009: error rates quoted in b06 match (Exp 2 length 3: 1.1 / 15.9 / 20.5). Added detail not in b06: Exp 2 had 22 participants, not 24; and in Exp 1 length 3 the mixed E-I rate (8.9%) was above I-I (4.2%).
- Lawsen: abstract says impossible River Crossing instances for N >= 6; the body says no solution for N > 5 with boat size 3 (same claim). Function outputs finish under 5,000 tokens; no counts reported (b22).

Corrections:
1. c06 (Borazjanizadeh ablation) had several wrong cells. The paper's prose says: No Diagram (text-only optimized GoT) 90.2 to 58; No Diagram Schema 90.2 to 72 (the table prints 58, garbled); No Code Execution (code only) 90.2 to 24; No Beam Search 90.2 to 62 (c06 said 72, wrong); 2-Branching Factor 70 in the prose but 52 in the table (the paper contradicts itself; c06 said about 70 with a 52 variant). Treat only the three headline ablations (58 / 72 / 24) as reliable. Note too that the extracted main table shows Visual Thinking on Blocksworld hard as 36 with a second value 52, while the text says 78 vs o1-preview 23.65. The 78 figure is quoted in the abstract-level text but the table layout is unresolved.
2. a01 and a02 said "row labels inferred"; the labels are now supported by the text, but cell-to-row mapping in Table 1 remains uncertain for the GPT-4V rows.
3. b06: add that Zhang and Wang is the same lab as Zhang and Norman, so it is not an independent replication of the 1994 result. It tests a related claim (memory-aid view), not the isomorph effect.
4. b03 says Exp 2 "replicates Kotovsky, Hayes and Simon"; this is Zhang and Norman's own claim, known to us only second-hand (b26).

## Contradictions between sources
- Drawing helps (VoT, WoT, Sketchpad, Visual Thinking, MVoT) vs drawing does not help (Ando 2026, VoT ring, WoT square grid, text coordinates winning on simple grids). These are reconcilable by task type (spatial and awkward geometry vs symbolic and simple), but no study varies this on one item set.
- Ando 2026 vs the human diagrammatic literature (Euler diagrams help people) and vs Ando et al. 2024 (reported gains on some patterns). Not resolved.
- Borazjanizadeh code-only collapse (24) vs Sketchpad, where code-generated sketches are the tool. The difference is whether the model sees the rendered image or the code.
- Shojaee 2025 reports Hanoi collapse; Lawsen says it is an output-format artefact. Neither has counts for the function-output claim.
- Sui et al. (HTML best) vs He et al. (JSON/YAML best for GPT-3.5, markdown for GPT-4): best format is model-specific.

## Weak spots
- Almost all human-psychology founding work except Zhang and Norman 1994 and Zhang and Wang 2009 was not opened (a07-a19, b08-b10, b26, b27, c23, c24). Larkin and Simon 1987 was never opened. The two DOIs given for it differ (cog1103_2, cog1101_4, and a Wiley id); the correct one is cog1101_4 (Cognitive Science 11(1), 65-100), so a07/a08 URLs are wrong.
- Zhang and Norman exact means are in figures only; only p values and counts are text-verified. No effect sizes.
- Kotovsky, Hayes, Simon "factor of 16" is unverified recall (a11).
- LLM evidence mixes 2022-2024 models (GPT-3.5, GPT-4, PaLM 62B, Claude 3.5 Sonnet, GPT-4o-mini). No 2025-2026 frontier reasoning models are tested on notation effects except o1-preview as a baseline.
- Most LLM gains come from one paper each (VoT, Visual Thinking, Sketchpad, WoT) without outside replication. Visual Thinking has 50 instances per cell.
- Berney and Betrancourt, Hoffler and Leutner (b09, b10) are title-only pointers; no effect sizes. Treat as unused.
- Snippet-only or abstract-only: a06 (CoT numbers), a22, b24, b25, c18 (Nye et al.), c16 (full tables).
- No replication or failed replication of Zhang and Norman 1994 itself was found (a23); the search budget ran out.

## GAPS

1. Does a representation change of the same task (e.g. state as prose vs position-keyed table vs rendered grid vs generator code) change a modern LLM's solve rate at equal tokens? No study uses true isomorphs of one puzzle, so the direct analogue of Zhang and Norman is untested (K23).
2. Do rule constraints enforced by a checker (external) beat the same rules stated in the prompt (internal) for a modern LLM, and does it remove rule-violation errors as in humans (K01)?
3. Which 2025-2026 studies replicate or contradict VoT, Whiteboard-of-Thought, Visual Sketchpad and Visual Thinking on frontier reasoning models? Is the gain gone once models reason natively?
4. Are there replications or failed replications of Zhang and Norman 1994 and of Larkin and Simon 1987 in humans (isomorph effect sizes, boundary conditions)? What are the exact means and effect sizes?
5. When does a drawn state hurt? Is there a rule (spatial vs symbolic, entity count, geometry shape) that predicts the winner between text coordinates and drawings across studies (K11)?
6. Does verifying the model's own redrawn state by code raise end accuracy (VoT state accuracy was 24-26%)? What is the cost in tokens?
7. Why did diagrams hurt on conversion cases (Ando 2026)? Is it the diagram format or label imbalance and answer bias on small cells (19 items)?
8. What is the best format for lists of linked facts (incident vs adjacency vs edge list vs table) on current models, and does the ordering put-the-question-first hold for them?
9. Is the Lawsen claim (function output removes Hanoi collapse) borne out with counts and under review, and what does it imply for compact vs exhaustive answer notation?
10. Does the translation cost from the human multi-representation literature (Ainsworth DeFT; Ayabe 2022 load rising first) show up as extra tokens and errors when an agent keeps two state formats?

## Gap search results

Run 2026-11-01. Evidence in `evidence_d.jsonl` (d01 to d23). Full texts were opened via arXiv PDFs and pdftotext; WebSearch was out of budget, so papers were found through Semantic Scholar citation lists (VoT, Sketchpad, WoT, Talk-like-a-graph, MVoT, Lawsen, Zhang and Norman, Larkin and Simon). Claims K01, K06, K07, K09 to K15, K17, K18, K20 to K23 were updated; K24 to K29 are new. Status of K14 and K17 stays contested; K14 was narrowed.

**Gap 1 (same task, different notation, modern LLM): partly closed, true isomorphs still missing.** Nearest tests: ARC object encoding vs flat grid, GPT-4 13/50 to 23/50 (d04); SPaRC, same puzzle, Qwen 3.5 397B image 14.4, text 38.0, image with text symbols 48.4 (d06); 85 algebra problems in story/word-equation/symbolic/isomorph forms on five current models, small effects (Cramers V 0.03 to 0.07 between interfaces, d13). Notation moves results by 10 to 34 points when perception is the bottleneck and by single digits for frontier models on algebra. No Hanoi cups-vs-pegs study for LLMs.

**Gap 2 (checker vs rules in prompt): partly closed.** GPT-4 with a sound external critique: Game of 24 5 to 36/38, Graph Colouring 16 to 38/37, Blocksworld 40 to 60/87, versus self-critique 3, 2, 55 (d12). Frontier VLMs lose ground when rule-violation text feedback is removed (VisGym, d14). Not found: a study with rules-in-prompt as the control against a legality checker on one puzzle, and nothing showing "zero rule violations" for an LLM. A 2022 human study adds that a display raises completion but costs moves (d18).

**Gap 3 (VoT, WoT, Sketchpad, Visual Thinking on 2025-26 reasoners): mostly open, evidence is mixed and model-specific.** No paper re-ran VoT or WoT on a reasoning model. Indirect: o4-mini best with text only, vision hurts (d15); Gemini 2.5 Pro uses vision for fewer tokens (d15); GPT-5 gains 11 to 14 points from image tools, Gemini 2.5 Pro gains none (d21); a constraint-checked canvas adds 0, 3, 6 of 112 items for Gemini 3 Flash, Sonnet 4.6, GPT-5.4 on a nearly saturated set (d11); Visual Thinking beats o1-preview on hard planning but not simple Blocksworld (d20). The gain does not vanish, but it is no longer general.

**Gap 4 (human replications of Zhang and Norman, Larkin and Simon): stays open.** No replication or failed replication found in about 800 and 1,000 scanned citing titles; Larkin and Simon full text is behind a bot block and was not opened. Found: Zhang and Wang 2005 (same lab, abstract only, d22), Fansher et al. 2022 on Hanoi mode of presentation (external helps completion, costs moves, abstract only, d18), Chu et al. 2017 diagram benefit in algebra (61 students, d19). No exact means or effect sizes obtained.

**Gap 5 (when does drawing hurt): partly closed with a candidate rule.** Text or ASCII wins for small symbolic grids and entity lists (SpatialEval, d05; VisGym GPT-5 3 to 4 times better with ASCII, d14; o4-mini, d15). Layout or image wins when positional relations grow with size (transpose text 92.7% to 0.8% from 12x12 to 20x20, image 90.8% at 20x20, but fine-tuned small models, d07) or when glyph shape matters (Matchstick, d14). Model-specific. Not tested: a single item set sweeping size and entity count on a frontier model.

**Gap 6 (check the redrawn state by code): closed as to direction, open as to cost.** Text2Space (d08): layouts built from text right 28 to 51% (five of six models), ASCII-first never beat text-only answers (e.g. GPT-4.1 85.8 vs 83.8, Llama-3-70B 71.7 vs 66.9), agreement of layout and answer picks answers that are 88 to 97% correct vs 71 to 94% overall, but 24 to 54% of items disagree. So a check works as a filter with a coverage cost. Token cost was not reported by any source.

**Gap 7 (Ando and Mineshima conversion cell): closed.** All 19 conversion items are neutral; labels are balanced at 95 each; Sonnet loses 2 or 3 items (16/19 to 13/19 Linear, 14/19 Euler); my unpaired Fisher tests give p 0.45 and 0.69. GPT-4o-mini's weak neutral accuracy (24/95 in NL) is answer bias. The drop is not evidence about diagram format (d17).

**Gap 8 (best format for linked facts): partly closed, frontier head-to-head still missing.** Sorted edge list stays close to default; matrices often lose; adjacency lists shift counting tasks; std across four syntaxes 3.45 to 5.41 for gpt-oss and 9.7 to 10.5 for fine-tuned G1 (d09); 3B models prefer adjacency lists for graph metrics (d10). The question-before-data ordering result (Sui et al.) was not re-tested on current models.

**Gap 9 (Lawsen): closed as "not supported".** One prompt at N=15, four models, no counts, author admits too few trials, not peer reviewed (d01). A replication with stepwise prompting still collapsed near 8 disks (10 trials per N, d02); a second comment is anecdotal (d03).

**Gap 10 (translation cost of two representations): stays open.** No study counts extra tokens or errors from keeping two state formats. Proxy only: when a model writes both an ASCII layout and an answer, they disagree on 24 to 54% of items (d08), and a code-executing interface moved failures into protocol violations and execution errors rather than removing them (d13).

### Corrections to earlier files made by this pass
- d17 supersedes the label-imbalance doubt in c03: labels are balanced; the cause is answer bias. c02's "19 items" caveat is confirmed and sharpened to 2 to 3 items.
- c05 text: Visual Thinking beats o1-preview on the new domains but not on Blocksworld simple (97.8 vs 90.2); this is in d20.
- Numbers in d08 depend on a row mapping reconstructed from a garbled table (checked against Table 3 and the paper text).
- Larkin and Simon (a07, a08, c23) is still unopened. d23 records the failed attempt.

### Still open after this pass
1. A Hanoi-style isomorph test on an LLM (gap 1).
2. Rules-in-prompt vs legality checker on a fixed puzzle (gap 2).
3. VoT, WoT or Sketchpad on a 2025-26 reasoning model with its native reasoning on and off (gap 3).
4. Human replications and exact effect sizes for Zhang and Norman and Larkin and Simon (gap 4).
5. Token cost of a state check and of a second state format (gaps 6 and 10).
6. Frontier head-to-head of list formats and the question-first ordering (gap 8).
