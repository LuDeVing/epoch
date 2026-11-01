# F02.06 External representations: cross-check critique

## Corrections made (sources re-opened this session; PDF or page text read)
1. Gigerenzer and Hoffrage 1995 (a10, b06). Opened the paper. Study 1: Bayesian algorithms in 46% (standard menu) and 50% (short menu) of answers with frequency formats vs 16% and 28% with probability formats, stable across 15 problems. This is the share of answers using a Bayesian algorithm (process plus outcome), not plain "correct". a10 (16 vs 46, from memory) is right in substance. b06 (48% vs 22%, as quoted by Cui et al. 2023) is not in the Study 1 text. Use 16 vs 46/50.
2. Mind's Eye (a23). The abstract says 27.9% zero-shot and 46.0% few-shot "on average". The body gives the average gain across all sizes as 18.4% zero-shot and 34.2% few-shot; 27.9/46.0 is the large-model grounding-gain row (text compares 46.0% for 175B with 10.3% for 1.3B). "36.4 to 38.2 vs 46.7 to 84.2" is not one task: it is the few-shot average going 1.3B to 175B, vanilla vs with simulation. "68.6 to 99.1" is the Instruct-GPT few-shot average. 29.8 (1.3B + simulation) vs 29 (175B vanilla), zero-shot, confirmed; size ratio about 135x.
3. SpatialEval (a15, a16). 62.1% is the LLM Mixtral-7B on Spatial-Grid; its VLM counterpart LLaVA-1.6-Mistral-7B got 47.1% (15 points lower). Text-only Llama-3 71.9%, Mistral-7B-Instruct 62.1%. Removing the image raised LLaVA-1.6-34B by 20.1% on Spatial-Grid. Noise image: the 6.5% gain is LLaVA-1.6-Vicuna-13B on Maze-Nav. The random-image gain is shown for Maze-Nav only, so a16 over-generalised.
4. VoT Table 1 (a11, b10). Interleaved rows resolve to: CoT 37.02/9.48/48.61/54.15/54.00; no-viz 37.17/10.28/48.49/46.98/35.50; GPT-4V 33.36/5.65/46.59/49.62/none; VoT 40.77/14.72/55.28/63.94/59.00. Ring task 52.5 vs 49.5 (N=200) confirmed.
5. Confirmed unchanged: Xu et al. ARC 13/50 to 23/50, 97 vs 81 of 400, 45 vs 35 of 149; IsoBench 28.7/18.7/14.9, IsoCB +9.4, IsoSP +14.4; Fatemi 19.8 vs 53.8 and 4.8-61.8%; Sketchpad 11.2 (GPT-4o) and 23.4 (GPT-4 Turbo) in Table 1, 12.7 and 8.6 are the abstract averages, max flow 66.3 (+41.3); Zhang and Norman N=24 (Exp 1A) and N=18 (Exp 2); Berlin study 36% vs 68% pretest (abstract says 34%), N=577; Macchi 12/44 vs 14/43 (Exp 1) and 14/30 vs 23/29 (Exp 2).

## Contradictions between sources
- Gigerenzer and Hoffrage numbers (item 1) and Mind's Eye abstract vs body (item 2).
- Interactive insight: Fioratou and Cowley (3% to 30%) and the 2020 chains study (43% vs 6%) vs Chuderski 2021, Macchi 2026, Spiridonov 2025 (no effect). Control rates range 3% to 43% across labs for the same problem, so positive effects may come from weak controls.
- Text vs image: Wu, IsoBench, SpatialEval agree text wins for text-trained models; Deng (image tables sometimes better for long numeric tables) and Whiteboard-of-Thought (hexagon grid 8% to 61%) disagree. Reconcile: a render helps when the text description is the weak link.
- Best wrapper format differs by model (GPT-3.5 prefers JSON, GPT-4 Markdown in He et al.).

## Weak spots
- Larkin and Simon (a09, b25) never opened (403). Kotovsky 1985, Zhang 1997, Kirsh and Maglio, Chuderski 2021, McDowell and Jacobs 2017 are second-hand.
- Zhang and Norman: undergraduates, N 18 to 24, one task family, cover stories differ by condition.
- Most LLM format evidence is 2023-2024 (GPT-3.5/4, PaLM, LLaMA-2); no 2025-2026 frontier reasoning models. Format sensitivity falls with model strength, so effects may be smaller now.
- VoT gains are modest; NL navigation VoT vs CoT only p<0.16.
- Sketchpad and Mind's Eye mix the representation with tool use; they do not isolate form.
- No LLM study here compares at equal tokens; drawing and sketching cost extra tokens.
- Only seen as abstract or snippet: NLGraph (b15), Deng table cells (b18, garbled), Macmillan-Scott (c25), the 2604.01366 citation chain (c21, c24).

## GAPS
1. Does a code-validated written state (grid, ledger, table) beat a free-form drawn state and plain CoT at equal total tokens on a 2025-2026 frontier model? (VoT and Sketchpad never controlled tokens.)
2. Do 2025-2026 reasoning models still show the format spread seen in GPT-3.5/GPT-4 (He, Sui, Sclar)? Needs a measured spread on our model.
3. Do natural-frequency or nested-set restatements help LLMs on Bayes items? Is there a primary paper with a format manipulation and numbers?
4. Is there any direct LLM test of Zhang and Norman (rules enforced by the medium vs stated in text) or of Larkin and Simon (needed facts adjacent vs scattered)?
5. Does a code-built object list beat a raw grid on ARC for current models, and what detail level is best (edge info hurt in Xu et al.)?
6. When should the agent choose a rendered image over text (Whiteboard-of-Thought hexagons vs square grids)? Which task features predict it?
7. Can form selection (AutoForm style) be done from a cheap pilot on a few items, then fixed, at net-positive tokens?
8. Does making the hidden constraint explicit in the problem statement (Macchi picture result) transfer to LLM insight-type puzzles?
9. Does a strong plain-text baseline erase reported gains from rewriting (the weak-control problem seen in insight studies)?
10. Original Larkin and Simon 1987 and Chuderski 2021 numbers: unread; re-open if either becomes load-bearing.

## Gap search results
Evidence is in evidence_d.jsonl (d01-d16). Web search quota and the arXiv, Semantic Scholar and OpenAlex search APIs were rate-limited during this pass, so papers were opened by arXiv ID only. No new paper discovery by keyword was possible; this limits every "no paper found" statement below.

- Gap 1 (code-validated state vs drawn state vs CoT at equal tokens, 2025-2026 frontier): STILL OPEN. Sketchpad costs 2.2k-3.1k tokens per math or graph sample with no matched baseline (d07). MVoT shows the written state is the failure point (90.8% of FrozenLake CoT errors were wrong hole coordinates) but is fine-tuned 7B (d06). Terse forms hold accuracy at 20-26% of CoT tokens (d08, d09), so the fair baseline is a token-capped CoT. New claim K17.
- Gap 2 (format spread on 2025-2026 reasoning models): STILL OPEN. Only 2023-2024 data: spread persists with size (Sclar, d12) and in gpt-4o-mini (Tam, d11: GSM8K 94.57 free text vs 86.95 JSON-mode). K06 changed to contested because "spread shrinks for the strongest models" is not supported. New claim K22. Needs a measurement on our model.
- Gap 3 (frequency or nested-set restatement for LLMs): STILL OPEN, but the Dasgupta chain is CLOSED as false: Lampinen/Dasgupta 2022 has no Bayes or frequency test (d03) and CogBias 2026 repeats the line without a measurement (d02). Only data: Araya 2025, one item, three reasoning models, none used natural frequencies unprompted (d01). K11 rewritten.
- Gap 4 (direct test of Zhang-Norman or Larkin-Simon): STILL OPEN. Closest indirect analogue is Lost in the Middle (d13): fact position cost GPT-3.5 over 20 points. No test of rules enforced by the medium vs stated.
- Gap 5 (code-built object list vs raw grid on ARC, detail level): STILL OPEN. Only a related 2025 result: viewing the same grid under rotations and transposes with pooled scoring reached 71.6% on public eval with a fine-tuned 8B model (d16), which does not address detail level.
- Gap 6 (when to pick a rendered image): PARTLY CLOSED. Whiteboard-of-Thought Table 3 read in full (d04): hexagon CoT 8 vs WoT 61, triangle 26 vs 55, circle 25 vs 41, square 98 vs 50, rhombus 51 vs 52. Rule of thumb: render when text has no natural coordinate form. Perception, not drawing, is the main remaining error (d05). Single model (GPT-4o); claim K18 single-source.
- Gap 7 (cheap pilot form selection with net-positive tokens): PARTLY OPEN. Sketch-of-Thought uses a router trained once on 14,200 labelled items, cost amortised, accuracy within 1% (d08). A few-item per-task pilot was not found.
- Gap 8 (hidden constraint stated, LLM insight puzzles): STILL OPEN. BRAINTEASER has rephrase and context-swap variants, not constraint reveal (d14). K21.
- Gap 9 (strong baseline erasing rewrite gains): PARTLY CLOSED. Rephrase-and-Respond (d15) gained 64.95 to 89.77 against direct zero-shot but only 0-2 points on near-ceiling tasks, and its baseline lacked CoT. Suggests gains shrink with a strong baseline; no paper was found that reruns it against CoT on a current model. K19.
- Gap 10 (Larkin and Simon 1987, Chuderski 2021 originals): NOT RETRIED this pass; both remain unread.

New side findings: forcing JSON before reasoning removes the reasoning (K20, d11); code on a noisy table does worse than text, so normalise first (d10, added to K05).

Status changes: K06 established to contested. K11 rewritten (chain false). K04, K05, K07, K08, K16 gained evidence ids. New claims K17-K22.
