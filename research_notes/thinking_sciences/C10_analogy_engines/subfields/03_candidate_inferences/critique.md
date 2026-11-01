# Critique: C10.03 Candidate inferences

## Numbers re-opened (arXiv full text, this session)
1. Webb et al. 2023: OR=1.88 p=0.005 (CI 1.21-2.91); story far p=0.065; near p=0.0039; pooled p=0.0005; OR=0.37 p=0.0003; 15/54. CONFIRMED. Correction: the human pooled t(53)=21.3, near t(53)=21.5, far t(53)=16.7. Entry a15/b11 are fine; c02 correct.
2. Lewis and Mitchell 2024 Table 2: humans .753, GPT-3 .488, GPT-3.5 .350, GPT-4 .452 (the PDF text layer shuffles the row labels; the order of the four values fits the labels). CONFIRMED, 1,876 human and 6,840 per-model samples.
3. Yasunaga GSM8K 76.7 vs 77.8 (GPT-3.5), davinci-003 54.0 vs 61.0, MATH 34.9 vs 37.3. CONFIRMED.
4. Yasunaga Codeforces: 3-shot CoT 13%/25% (GPT-3.5), 17%/32% (GPT-4); ours 15%/29% and 19%/37%; GPT-3.5 15% vs GPT-4 16%. CONFIRMED. Note a23 calls the baseline "9-13%": loose, use c11.
5. Yu et al. shortest path optimal rate: GPT-3.5 IO .33 to TP .65; GPT-4 IO .78 to TP .88; PaLM-2 IO .14 to TP .36 (CoT .24). CONFIRMED. Abstract: 12%, 13%, 15% CONFIRMED.
6. Qin et al.: GSM8K/MATH relevant 71.5/33.3, N/A 75.5/36.1, random-same 75.1/36.3, random-diff 76.3/34.1. CONFIRMED. Example accuracy 62.0/72.0/86.0 CONFIRMED, but Table 5 caption does not name the dataset in the text layer; c13 says MATH: treat as unverified for the dataset label.
7. Not re-opened: ARN 97.9/94.1/39.6 (arXiv id lookup failed, rate limit), Puranam, Clement and Gentner, Gentner et al. 2003, SCAR, AnaloBench, YARN, Shen et al. These rely on the earlier agents' reading (opened:true) and are not independently confirmed here.

## Contradictions
- Yasunaga says relevance of self-generated analogues helps; Qin et al. say random examples do as well or better on maths (GPT-3.5 only, 500 items, 3 seeds). Different models/prompts; unresolved. Yasunaga's own gain is small (+1 point GSM8K) so it may be noise-level.
- Lewis/Mitchell and Hodel/West say LLM analogy is brittle; Webb et al. 2024 say it is a counting weakness fixed by code. Both fit the data; competing explanations remain.
- a20 reports GPT-4 0.75 total and Webb total 0.78 on stories; b22 says average model accuracy about 57 on ARN while a26 says 75.0 near and 39.6 far: consistent only if the average mixes other conditions.
- Entry a18 says 7 alphabets x 10 x 6 = 420; that count is plausible but not rechecked.

## Weak spots
- Almost all LLM work tests analogy choice or mapping, not the candidate-inference step (projection of unmatched base facts). The core claim for O7 therefore rests on human data from 1991-2003 and a 1988 model.
- Gick and Holyoak 1980/83 and Alfieri 2013 d~0.5 were taken from memory or secondary sources (opened:false). Do not cite numbers.
- Thought Propagation and Yasunaga each have one source; no independent replication of Thought Propagation.
- The 2026 entries (YARN, Shen et al., probing, BioSpark) are from abstracts/skims; the c22 per-model novelty numbers were partly inferred.
- Single-run qualitative GPT-3 radiation-problem result has no counts.
- Failed replication Hodel and West was read via its own text but rebuttal from the authors' side only partly.

## GAPS
1. How often is a step carried from a solved source to a new target by an LLM actually false, and does a test-before-adopt step reduce that at equal tokens? (No direct measurement found.)
2. Does a structure-mapping or alignment check (code-side one-to-one mapping, YARN style) beat plain prompting for choosing which source steps to carry, with matched compute?
3. Do two aligned source cases (comparison) beat one source for LLM transfer, as in Gentner et al. 2003 (48% vs 19%)? No LLM test found.
4. Does the Qin et al. finding (accuracy, not relevance, drives self-generated exemplar gains) hold for stronger models and non-maths tasks?
5. What are the original Gick and Holyoak 1980/83 numbers and the Alfieri 2013 effect size, read from source?
6. Does the ARN far-analogy collapse persist for 2025-2026 frontier and reasoning models?
7. Can an LLM detect and repair skolem-style missing entities (base entity with no target partner), as PHINEAS probe/resolve does?
8. Is the order/paraphrase sensitivity (Lewis and Mitchell 2025) present in reasoning-trained models, and does shuffling sources and voting remove it?
9. Do people (Lassaline, Spellman and Holyoak) show the same causal-connection preference with numbers we can compare to LLM projection rates?
10. Does the cross-domain novelty boost (Shen et al. 2026) survive a correctness check by blind experts?

## Gap search results

Search limits: WebSearch quota was used up at the start; arXiv and Semantic Scholar APIs returned 429 most of the time; OpenAlex needed a key. Work was done by opening known arXiv PDFs directly (evidence_d.jsonl, d01 to d18). Absence of a paper below means not found here, not proven absent.

1. False carried steps and test-before-adopt: OPEN. Proxies only: 21 of 100 hand-checked runs had a relevant but wrong self-made exemplar (Yasunaga, d04); GPT-4 with a hint used the wrong analogue about half the time (Puranam, d16). No equal-token test arm exists. New claim K18.
2. Code-side structure mapping vs prompting: PARTLY. YARN (d12) helps 8B models on a 4-way choice (Llama 0.28 to 0.45, Qwen 0.41 to 0.46) and on Llama far ARN (0.42 to 0.46), but is worse on Qwen far ARN (0.47 vs 0.52). It picks stories, not steps, and compute was not matched. Mapping without abstraction is below chance.
3. Two aligned sources vs one for LLMs: OPEN. Only indirect: one self-made exemplar is worst, 3 to 5 plateau (d03). Human effect size corrected: d=.60 (CI .47 to .72) in the 2011 abstract, d=.50 in the published abstract (snippet only) (d01).
4. Qin finding on stronger models and other tasks: PARTLY CLOSED. Holds for GPT-4o-mini (GSM8K relevant 90.7 vs random-bio 93.2) and Llama models; fails on BBH where relevant wins (63.2 vs 61.9). MATH label confirmed: example accuracy 62% relevant, 72% N/A, 86% random-same (n=50 each) (d06, d07). No reasoning or frontier model tested.
5. Original numbers: PARTLY. Gick and Holyoak 1983 Exp 2 = 29% (8/28) and 50% (14/28), read as a quote in Puranam et al. (d02). The 1980 paper was not opened. Alfieri d: see gap 3.
6. ARN far collapse in 2025-2026 models: OPEN, with one hint. The 39.6 is the all-model mean of 45.3 and 33.9 (GPT-4 alone: 57.1 and 29.1) (d09). GPT-5.2 and Claude Opus 4.5 reach ranking MAP about 0.82 on ARN stories (d10), but the hard far-with-near-distractor cell was not split out. Resolves the critique's 57 vs 75 vs 39.6 puzzle. New claim K19.
7. Skolem-style missing-entity repair by LLMs: OPEN. Nothing found.
8. Order and paraphrase sensitivity in reasoning models: OPEN. GPT-4 numbers re-read (d15). Only brittleness evidence for reasoning models is o3-mini and R1 on I-RAVEN-X (86.6 to 17.0; 80.6 to 23.2) (d11). No shuffle-and-vote test found.
9. Human vs LLM causal-connection numbers: OPEN. Lassaline page did not load; no numbers read.
10. Shen et al. correctness check: ANSWERED NO. Humans (4 raters, 50 pairs, source shown) rated AR more novel 78% but reasonable 67% vs 86% baseline (kappa .155 vs .416). No blind expert correctness test exists in the paper (d13, d14). New claim K20.

Corrections: a26/b22 numbers reconciled (see d09). Alfieri "d~0.5" now has two conflicting values (.60 early, .50 published). New claim K21 (reasoning-model brittleness).
