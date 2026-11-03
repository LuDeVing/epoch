# Critique: Kolmogorov complexity (C11.02)

## Numbers re-checked against the PDFs (10 of 10 confirmed, 3 with notes)
1. Deletang 2024: ImageNet 43.4%, LibriSpeech 16.4%, PNG 58.5%, FLAC 30.3%, Chinchilla enwik9 raw 8.3% and adjusted 21.9%, Llama 2 7B 8.9%. Confirmed.
2. Huang 2024: 31 LLMs, 12 benchmarks, Pearson -0.93 overall, RMSE 3.1%. Confirmed in text.
3. Yoran 2025: 78% and 40% failure on natural data; GPT-4o accuracy 35.6/15.0/29.6/24.8/6.5/33.3; SeqCoder synthetic 84.5 and 92.5 with precision 0.57, 0.56; natural near zero (<=0.1); >99% errors in first 16 chars; >95% repetition. Confirmed. The synthetic failure figures differ between the intro (66%/45%) and Section 5.1 (65%/55%); keep flagged.
4. Opitz 2023: up to -9 points realistic, +1.4 (K=2), +1.1 (K=1), 6 of 7 sets. Confirmed. The optimistic table gives +1.5; do not mix them.
5. Gauvrit 2014: mean 21.74 (SD .52), F(2,65)=0.68, p=0.41, eta2=0.11. Confirmed. The t(67)=4.35 line was not found by grep (text layer flagged binary); it rests on the earlier agent's reading.
6. Cilibrasi 2005: 24 species, S(T)=0.996, six errors. Confirmed. Correction of meaning: S(T)=0.996 says the tree fits the distance matrix, not that the phylogeny is correct.
7. Zenil 2026: 177,591 programs, 3.32 bits, 4.5 / 36.5 / 128 bits at 24 symbols. Confirmed in abstract.
8. CompressARC: 20% eval, 34.75% train. Confirmed. The baseline table is scrambled by pdftotext, so the "U-Net 0.75%" figure in c16 is plausible but not verified.
9. Soler-Toscano 2013: r=0.83 and r=0.41 confirmed. The "99,608 strings" count was not found by grep; the paper builds D(5,2) from 9,658,153,742 reduced machines. Treat 99,608 as unverified (a13 and K05 omit it).
10. MADIL: 69 solved, 57 correct on test (82%), 53 first attempt, 7% in abstract. Confirmed.

## Contradictions and tensions
- Wan & Mei (b23, LLMs as computable approximations to Solomonoff induction) versus Zenil 2026 (c19, Shannon compressors, not Solomonoff). Different tests; only c19 has verified numbers.
- Compression predicts intelligence (Huang, r about -0.95) versus LLMs failing to write short programs (Yoran, 6.5-35.6% accuracy). Compression by probability code is not compression by program; do not merge them.
- Deletang raw rates look strong; adjusted rates for non-text are 185-229%, worse than raw data.
- Humans: complexity vs subjective randomness r=.52 but natural statistics r=.75 (b13); the children effect is small. Human simplicity preference is not cleanly algorithmic.

## Weak spots
- No study tests "tell the agent to pick the shortest rule" as a scaffold step at equal tokens. Closest: Sun & Saparov (b22) and Yoran CoT results, both single source.
- Many claims are single-source (K05, K06, K12-K17, K19, K21).
- Founding texts (Solomonoff 1964, Kolmogorov 1965, Chaitin, Li & Vitanyi) were not opened; a06, a07, a26, b25 rest on secondary text. Feldman 2000, Lafond 2007, Griffiths & Tenenbaum 2003 (b14-b16) were not opened, so human concept-learning complexity evidence is thin.
- Pass 2026 (c21) and Shportko 2026 (c22): small illustrations (12 GSM8K problems; 300 samples), not turned into claims.
- Legg & Hutter (a04, a05, c26): definitions only, no experiments.

## Seen only in snippets or not opened
a06, a07, a26, b14, b15, b16, b25, c26 (header only); b23 and b24 (no figures extracted).

## GAPS
1. Does an explicit "state the shortest consistent rule, then check it on all examples" step beat plain chain-of-thought at equal tokens on rule-induction items (ARC subset, list functions)?
2. Which cheap length proxy for a candidate rule (token count, exception count, model log-loss) best ranks rules against held-out correctness for an LLM agent?
3. Does MDL ranking of several sampled candidate programs beat majority vote or self-consistency on ARC-style tasks at equal tokens? CompressARC and MADIL use MDL search, but no equal-token comparison against LLM sampling exists.
4. Does prompting for parsimony close the Sun & Saparov Occam's-razor failure, and is that failure replicated elsewhere?
5. Do LLMs satisfy Solomonoff-like predictions (Wan & Mei versus Zenil 2026)? Need the numbers behind Wan & Mei.
6. How much does the ranking of candidate rules change between description languages (natural language vs Python vs a small DSL)? This is the invariance constant in practice.
7. Does the compressibility or length of a reasoning trace predict its correctness (2024-2026 studies)?
8. Feldman 2000 and later human concept-learning work: exact effect sizes and failed replications of Boolean complexity predicting learning difficulty (not opened).
9. Primary founding sources (Solomonoff 1964, Chaitin 1966, Levin) with exact theorem statements, and 2020-2026 critiques of the coding-theorem method.

## Gap search results (gap searcher, evidence_d.jsonl d01-d16)
Search tools were rate-limited (arXiv API, Semantic Scholar, OpenAlex returned 429 or budget errors); papers were read from arXiv PDFs and PubMed abstracts. Claims K22-K27 added; K18, K19, K20, K07 updated.

1. Explicit shortest-rule step vs chain-of-thought at equal tokens: STILL OPEN. Nearest: Hypothesis Search (d08): ARC 100 problems, GPT-4, direct 17%, program 23%, summarised 30%, human-selected 33%, but compute unequal and no length arm.
2. Best cheap length proxy: STILL OPEN as a head-to-head. Separate proxies each work in their own setting (d02 proof length, d03 trace tokens, d05 operator count, d09 held-out validation error). Interim: validation error first, trace length second (d16).
3. MDL ranking vs majority vote at equal tokens on ARC: STILL OPEN. No paper found (d10, d14); Greenblatt-style filter-then-vote is the baseline. Closest length selector: short-m@k (d04) beats majority voting at equal thinking-token budgets, on math.
4. Parsimony prompt and Occam failure: PARTLY CLOSED. Full text (d02): CoT, buffer-of-thought and 8 demos do not close the weak/strong gap (accuracy <50% from height 2; SFT +11.0 to +1.5 strong accuracy). No plain 'be simplest' arm and no replication found. Wang et al. (d05) show a length-difficulty correlation in a different setting.
5. Wan & Mei vs Zenil 2026: CLOSED toward Zenil. Wan & Mei's only experiment is low-confidence few-shot selection (SMS: Qwen 3B 76.62 to 90.07, gains 0.1-0.4 points at 7-8B; no random baseline); it does not test Solomonoff predictions (d01). Wan & Mei is theory plus a weak test.
6. Description-language invariance in practice: STILL OPEN; no study found (d15). Must be run as our own K01 test.
7. Trace length predicts correctness: CLOSED (for reasoning models on math/GPQA). Shortest vs longest chain 63.4 vs 28.9, 60.0 vs 37.8, 71.1 vs 56.7, 83.3 vs 58.9 (d03). Limits: excludes unfinished chains, correlational, not rule induction.
8. Feldman 2000 and later work: PARTLY OPEN. Abstracts opened (d06: 41 concept types, difficulty proportional to Boolean complexity; d07: Vigo 2013 GIST claims better prediction). Exact effect sizes and Lafond 2007 not obtained (page behind bot check). Status of K24: contested.
9. Founding sources and critiques: PARTLY OPEN. Theorem statements read in the BDM paper (d11), not in Solomonoff/Kolmogorov/Chaitin/Levin originals. No independent 2020-2026 critique of the coding-theorem method located (d12, d13 are snippets).

New against the agent plan: LLM-PV (d09) shows held-out error as selector; any length rule needs an ablation against it.
