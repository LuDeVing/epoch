# Critique: Language of thought (D06.02)

## Numbers re-opened and checked (arXiv PDFs, text extracted this session)
All confirmed against the paper text unless noted.
1. SCAN (1711.00350): random split 99.8%; 2% coverage about 54%, 4% about 93%; length split 20.8% (best) and 13.8% (overall-best), 60.2% with oracle length; add-jump 1.2% / 0.08%; turn-left 90.3%; jump with 8 / 32 composed commands 38.3% / 88.4%; length by action count 95.76% to 22.8%; attention SRN 59.7%. Confirmed.
2. Least-to-most (2205.10625): code-davinci-002 16.7 / 16.2 / 99.7; text-davinci-002 6.0 / 0.0 / 76.0; 13 failures. Confirmed.
3. CFQ (1912.09713): 97.4 vs 14.9, 98.5 vs 17.9, 98.0 vs 18.9; SCAN MCD 6.1, 1.1, 1.2; R2 0.81-0.88 vs 0.11-0.22. Confirmed.
4. Hupkes (1908.08351): task accuracy 0.79 / 0.85 / 0.92; systematicity 0.53 / 0.56 / 0.72; productivity 0.30 / 0.31 / 0.50; drops 62 / 64 / 46%. Confirmed.
5. Csordas (2108.12284): PCFG productivity 50 to 85, systematicity 72 to 96, COGS 35 to 81, SCAN length 100%. Confirmed.
6. Reversal Curse (2309.12288): GPT-4 79% vs 33%; 96.7% vs 50.0% (matched order); Llama-1 above 80% / below 7%. Confirmed.
7. Dziri (2305.18654): 55% / 59% on 3x3 multiplication, 82.3% hidden errors. Confirmed.
8. PAL (2211.10435): GSM-HARD 65.6 to 20.1, PAL 61.5 (down 14.3), object counting 96.7 (+23.7). Confirmed.
9. Press (2210.03350): gap about 40%; 42.9% ChatGPT, 23.0% GPT-4; 79.6/54.2 vs 45.7/1.1. Confirmed.
10. COGS (2010.05465): Transformer 0.35, uni-LSTM 0.32, bi-LSTM 0.16. Confirmed. Also Wu et al. 99% to 62% confirmed.

## Corrections and cleanups
- Evidence c01-c06, c07-c09, c11-c13 are tagged type llm-study but test RNNs and Transformers trained from scratch, not LLMs. Treat them as primary model studies.
- Records a07/a08/a09, b01, c01-c03 all describe one source (Lake and Baroni 2018). Records a10/b03/c05/c06, a12/b02/c07-c09, a16/b09/c16/c17, a14/b07/c12/c13, a17/b11/c25 are likewise duplicates. The 78 lines hold about 40 distinct sources. Claims therefore count independent sources, not lines.
- c25: the "Llama-1 above 80% / below 7%" figure is the question-answer experiment, not the name-description one; the lines mix them. b12 year 2024 (venue) vs a18 2023 (arXiv): same paper.
- Fodor and McLaughlin 1990 DOI differs between a22 (90032-8) and b21 (90032-6); neither was opened. Do not cite the DOI until checked.
- b25, b26 are syntheses, not sources. b26 "MLC 99.78% or more" was not re-opened.
- c26 Coconut and c24 numbers not re-opened; c26 GSM8k shows Coconut loses to CoT.

## Contradictions
- Early reading "Transformers cannot do systematicity" (a10, a11) vs Csordas/Ontanon (a13, b05, b06): setup artifacts explain much of the gap. COGS 35% to 81% still leaves structural cases weak.
- Dziri says LLMs match subgraphs; Webb et al. (b15) says GPT-3 does abstract relational reasoning above humans. Different tasks, not reconciled.
- Press gap shrinks with GPT-4 (23.0%) but not with GPT-3 size; scale effect unclear.

## Weak spots
- Not opened (a20-a26, b19-b24 except as noted): Fodor 1975, Fodor and Pylyshyn 1988, Fodor-McLaughlin, Smolensky, Marcus, Piantadosi, Quilty-Dunn, Newman, Dehaene. The founding human-side claims have no numbers.
- No human-subject evidence for systematicity or productivity (infants, animals) was gathered; Marcus 1999 infants, Gallistel are only cited.
- Almost no 2024-2026 frontier-model results: tested models are GPT-3/3.5/4-era and Llama-1. Current reasoning models are untested here.
- Least-to-most evidence is one paper on a retired model. Grokking, binding and Coconut are single-source.
- Several records carry "numbers not extracted" (b06, b12, b14, c15).

## GAPS
1. Do current reasoning models (o1/o3-style, Claude, Gemini 2.5+) still show a compositionality gap on CFQ, COGS, Compositional Celebrities and SCAN length, and does decomposition still help them at equal tokens?
2. Does least-to-most or self-ask decomposition beat plain chain of thought at equal token cost on 2025-2026 models, outside SCAN?
3. Does the Reversal Curse persist in frontier models and in agents with a memory store, and does storing inverse facts fix it?
4. How much of the "hidden wrong step" rate (82.3%) remains in reasoning models with tools, and does step verification (G-type check) reduce it?
5. Does code-as-thought (PAL, program-of-thoughts) still outperform CoT on 2025 models, and on which tasks does it lose?
6. What does the human evidence (infants, animals, Fodor-Pylyshyn replies, Marcus rule learning) show with exact numbers, and has any been replicated or failed?
7. Do counterfactual and low-probability variants (Wu, McCoy) still cut accuracy in reasoning models, and how large is the drop?
8. Are there replications of MLC (Lake and Baroni 2023) on structural splits, and does any prompt-only version reach comparable systematicity?
9. Do latent-thought methods (Coconut) replicate, and is there a prompt-level analogue for our scaffold?
10. Is there any LLM study that tests variable binding or role-filler independence directly and with benchmark numbers (beyond Feng and Steinhardt)?


## Gap search results (evidence_d.jsonl, d01-d16)
Search budget: 3 of 8 WebSearch calls got through before the shared budget ran out; arXiv API and OpenAlex/Semantic Scholar were rate-limited or empty, so I used direct arXiv pdfs and Europe PMC. Full text opened for d01-d06, d08-d11; abstracts only for d12-d15; d07 and d16 are search snippets (opened false).

Closed or mostly closed:
- Gap 5 (code-as-thought vs CoT): mostly closed. Sprague 2025 (d05): CoT gains concentrate on symbolic, math, logic (+14.2, +12.3, +6.9); Plan + Tool solver beats Plan + CoT solver. Not a 2025-reasoning-model head-to-head.
- Gap 7 (counterfactual and low-probability variants): closed for o1-era. McCoy o1 (d01): 47% to 92% by output probability, rare-variant gap mostly gone on accuracy; GSM-Symbolic (d03): NoOp clause still hurts o1-preview. Reasoning models beyond o1 remain untested.
- Gap 10 (variable binding): mostly closed. Yang et al. (d08) give mechanistic evidence, 95% on 2-shot rule induction for Llama-3.1 70B; no benchmark of role-filler independence on compositional tasks.
- Gap 4 (hidden wrong steps): partly closed. ProcessBench (d09): 3.5% to 51.8% of correct-answer solutions hide a wrong step, rising with difficulty; best critic o1-mini. Nothing on tool-using agents, and the 82.3% multiplication figure was not re-measured on reasoning models.
- Gap 6 (human evidence): partly closed. Infant meta-analysis g 0.25, CI [0.09, 0.40], 63 experiments (d11); Marcus 1999 and 2007 and rats 2008 abstracts only (d12-d14). Marcus 1999 sample sizes, Fodor-Pylyshyn replies and animal replications are still unread.

Stayed open:
- Gap 1 (compositionality gap on CFQ, COGS, Compositional Celebrities, SCAN length for o1/o3/Claude/Gemini 2.5+): only indirect evidence. Apple (d04) shows depth collapse in reasoning models on puzzles; no CFQ or COGS numbers for current models found. d07 (nine frontier LLMs, two-hop) is an unopened lead.
- Gap 2 (least-to-most or self-ask vs CoT at equal tokens): no direct study found. Apple's low-complexity regime (non-thinking beats thinking at equal compute) is the only related datum.
- Gap 3 (reversal curse in frontier models, agents with memory): Wang and Sun (d06) is architectural, small models; no frontier or memory-store test found.
- Gap 8 (MLC replications, prompt-only systematicity): Nature full text not retrievable; no replication found.
- Gap 9 (Coconut replication): numbers re-read (d10) but no independent replication found; no prompt-level test.

Corrections to earlier notes: Coconut GSM8k 34.1 vs CoT 42.9 confirmed; the Wu et al. arithmetic table has three column groups and the header for the third was not verified, so quote only the base-10 100.0 vs base-9 23.4 pair.
