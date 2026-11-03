# A08.08 Critique: Working-memory limits and chunking

## Numbers re-opened this session (all confirmed unless noted)
1. Miller (1956), psychclassics HTML: mean 2.6 bits, about 6.5 categories; Smith spans 9 binary and 7 octal, 12 octal recalled = 24 binary (2:1) and about 40 (4:1, 5:1). Confirmed (a01-a03, b01-b03).
2. Chase and Simon (1973), PDF text: "no relation at all" for random positions; chunks per trial 7.7 / 5.7 / 5.3 (middle games); "linear list of seven or so unrelated chunk slots". Confirmed (a04, a06).
3. Gobet et al. (2017) meta-analysis: confirmed from the abstract (overall correlation significant, effect in nearly every study; random-material advantage supports many small chunks). Exact r = .41 and trim-and-fill r = .29 were NOT re-verified (formula hidden in abstract).
4. Levy et al. (2024): 0.92 to 0.68 by 3000 tokens confirmed (a20, b21).
5. RULER (2024): GPT-4 96.6/96.3/95.2/93.2/87.0/81.2, effective 64K; Llama2-7B 4K baseline 85.6; Mistral-v0.2 7B 75.4 at 32K, 13.8 at 128K confirmed (a21, c18).
6. HiAgent (2024): overall success 21 to 42 (+21) confirmed in Table 1. Correction: the text says progress +23.94% and context -35.02%, but in Table 1 those exact figures are the Jericho row; the "overall" wording is the authors' claim. Treat 23.94 and 35 as the paper's headline, not a clean average (c21 has the 42 vs 21 and these figures; b/c entries should carry this caveat).
7. Laban et al. (2025): average degradation -39% and "-15% aptitude, +112% unreliability" confirmed (a22).
8. Wang and Sun (2025): t = 3.03, p = 0.005, N = 30, 26.1% variance confirmed; log-linear decline and two-plateau step shape confirmed (c13-c15).
9. Gong et al. (2024): d' about 1 at n = 3 "apart from the noise variant" confirmed (a17, b14, c01). Note: a17 says "three of four verbal variants"; the paper lists base, noise, feedback, reasoning, so this is consistent.
10. Crossref/OpenAlex confirmed existence and abstract of Gobet et al. (2017); DOI 10.3758/s13421-016-0663-2.

## Contradictions and corrections
- Chase and Simon found no skill effect on random positions; Gobet et al. (2017) found one (r about .41, smaller after publication-bias adjustment). b09 says Chase and Simon is "not in the meta-analysis" yet "appears with N = 3"; that line is internally inconsistent and unverified. Treat the original as an N = 3 study later qualified.
- Chase and Simon's "seven slots" versus Cowan's 3 to 5: both hold (strategy vs core store), but Gobet and Clarkson (2004, b29) argue about 2 chunks in expert recall; only seen by title.
- Gong et al.: GPT-3.5 d' collapses at n = 3, but Hu and Lewis (2025) show Llama 3.1 70B at 84.75% task accuracy for 10-back and that weak-model errors are task misunderstanding. So "LLM n-back capacity of about 3" is model- and prompt-specific, not a law.
- de Langis et al.: forward span 50 digits but backward about 15 contradicts treating n-back drop as a simple capacity.
- Wang and Sun read the limit as hard capacity (step function) under sequential updates but log-linear decay under shuffled order; the shape depends on presentation order.
- Ericsson digit span: a15 says "almost 80" from Wikipedia; the original was not opened.

## Weak spots
- Many LLM numbers come from 2023 to 2024 models (GPT-3.5, Claude-1.3); newer frontier models may differ.
- Most agent-chunking evidence is single paper (HiAgent, ReadAgent, MemGPT); none replicated at equal tokens.
- Cowan 2010 and Luck and Vogel 2013 are reviews by paradigm owners; slots vs resources remains contested.
- Gong and Zhang (c04) is small transformers trained from scratch; not evidence for deployed LLMs.

## Seen only in snippets or not opened
a23 (Baddeley and Hitch 1974), a24, a25 (Gobet), b26-b29 (Thalmann 2019, Norris and Kalm 2021, Ma 2014, Gobet and Clarkson 2004), c25 note; a12 Chen and Cowan via secondary; a15 via Wikipedia; c23, c24 via Wikipedia; b23 exact GSM-IC drops not extracted; b18 per-task numbers not extracted. Zhang et al. (EMNLP 2024) n-back numbers (b16) were read from pages but human d' ranges not independently re-checked.

## GAPS
1. At equal tokens, does replacing raw history with named subgoal summaries (HiAgent style) raise accuracy on our scaffold, and at what compression ratio does it start to lose needed detail?
2. What is the usable working-set size (items tracked, n-back or state-update) of our actual backbone model, and how does it change with scaffold prompts versus bare prompts?
3. Does the 3-to-5 item human limit have any measurable analogue in modern frontier models, or does the proactive-interference threshold (Wang and Sun) depend only on parameter count?
4. Is the chunking prompt gain (+35.4 points, Zhang et al.) reproducible on current models, or is it an artifact of weak 2022 models?
5. Do stored reusable chunks (pattern library, template slots per Gobet and Simon) beat a larger context at equal tokens, as the expertise literature implies?
6. Does placing the current subgoal at the start and end of the prompt remove the lost-in-the-middle loss in recent models?
7. What are the exact Baddeley and Hitch (1974) dual-task numbers and the Thalmann et al. (2019) result on whether chunking frees capacity or only aids retrieval?
8. Is the interference effect from stale state removable by pruning (deleting superseded facts) rather than by telling the model to ignore them?
9. How do Gobet and Clarkson (2004) justify about 2 chunks in expert recall, and does it change the recommended per-step item cap?
10. Does a code-held state ledger (program holds state, restates each step) beat model-held state across multi-turn degradation (Laban) on our tasks?

## Gap search results
Evidence in evidence_d.jsonl (d01-d16). Claims K06, K14, K15, K16, K19 updated; K26-K34 added. WebSearch budget was already used up by other agents; arXiv search pages, Semantic Scholar and OpenAlex returned 429 or empty, so discovery was limited to papers whose ids were known plus Europe PMC, Crossref and PMC.
Correction: the 2017 meta-analysis is Sala and Gobet (PMC5323477). r = .41 [.29,.51] and trim-and-fill r = .29 [.17,.41] are now verified. Chase and Simon is in the binomial table (N = 3) but not in the meta-analysis, which settles the b09 inconsistency.

1. Subgoal summaries vs raw history at equal tokens: PARTLY CLOSED. d06 (masking matches summaries, halves cost), d07 (untuned summaries lose 12.5 points, failure-tuned rules recover; moderate threshold best), d09. No equal-token test of HiAgent-style named subgoal summaries on our scaffold; HiAgent still unreplicated (d15). Compression ratio where detail is lost: only ACON threshold sweep, not a ratio curve.
2. Working-set size of our backbone: OPEN. Needs our own n-back/state-update sweep; no new public number for a frontier model found.
3. Human 3-5 limit analogue in frontier models: PARTLY CLOSED. d05, d04, d03 show degradation in frontier models with input length, and d03 shows it persists with perfect retrieval, so it is not only retrieval or distractors. No clean item-count analogue; Wang and Sun parameter-count claim not re-tested.
4. Chunking prompt gain on current models: OPEN. No replication found with the tools available.
5. Stored chunks vs larger context at equal tokens: OPEN. d11 shows a large gain but with no equal-token control.
6. Subgoal at start and end of prompt: PARTLY CLOSED. d01: lost-in-the-middle is strongest below about 50% window fill and fades near the limit, replaced by a bias toward the end; so place the subgoal last. Start+end duplication untested.
7. Baddeley and Hitch numbers and Thalmann: SPLIT. Thalmann (d13) closed at abstract level (chunking frees capacity for other items, when retrieved from LTM and early). Baddeley and Hitch (d16) OPEN: paywalled, not opened.
8. Pruning vs telling the model to ignore: PARTLY CLOSED. d06 shows deleting old observations works; d03 shows masking does not remove the length cost. No direct test of delete vs ignore-instruction on superseded facts.
9. Gobet and Clarkson about 2 chunks: CLOSED at abstract level (d14): at most about three chunks replaced; masters chunks up to 15 pieces; template theory. Implication: cap counts large structures. Full paper not opened.
10. Code-held ledger vs model-held state: PARTLY CLOSED. d10: restating each turn recovers only 15-20% of loss; d08 shows a bounded rewritten state helps after RL. A code-held ledger itself is still untested.

Still open after this pass: 2, 4, 5, Baddeley and Hitch numbers, delete-vs-ignore direct test, start+end duplication, and all agent-side equal-token tests (these need our own runs).
