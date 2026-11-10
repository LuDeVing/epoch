# E07.03 TRIZ: cross-check critique

## Numbers re-opened this session (PDF text)
Confirmed: TRIZBench Table 3 (matrix 0.67/0.26 and 0.48/0.39; Matrix-Rerank Qwen3-8B 0.71/0.29 and 0.59/0.47; direct prompts 0.25-0.52 case/patent), 1,354 cases, 491 (29.2%) with parameters, 74.0% agreement. Trapp and Warschat: recall 0.71, precision 0.46, F1 0.56, 3.81/2.69/3.19 sentences, 86 of 100 flagged. Ogot and Okudan: 8.94 vs 4.42 feasible concepts, 35 vs 16.3 unique solutions, 21 vs 8 unique concepts, 64 vs 96 students, 16 vs 24 teams. Lee et al. chair table (all mass, stress, deflection percentages). TRIZ-a: 0.8325 to 0.8483, 43 of 45, gate 3.2277%, +2.88/+4.23/+0.15. TRIZ-GPT: 0.675/0.691/0.245/0.247 recall, 85.3% and 88.2%, cosine 0.829/0.823/0.824. AutoTRIZ: 7 of 10, 6.64 bits, battery 206/166, 21.66/13.18, 43%/34%. Duran-Novoa: principle-based methods 54% higher; SCAMPER 89%, KJ 73%, control 54%. IdeaForge: TinyLlama 1.1B, five domains.

## Corrections and qualifications
1. TRIZBench matrix baseline (a18, b12, c03): the principle task input includes the gold improve/worsen pair. The matrix 0.67/0.48 is therefore a lookup given the right pair, not a prediction from the problem. The fair comparison is the end-to-end pipeline (Qwen3-8B ZS-Rerank 0.59/0.46, LoRA 0.65/0.52), which still beats direct prompting (0.25-0.52) but by a smaller margin. Claim K08 records this.
2. Chance baseline: Hit@3 of 40 gives about 7.5% for one gold principle; no random baseline is reported in the paper.
3. c19 (IdeaForge) said the healthcare case had only 1 convergent pair. The garbled table suggests the one-pair row is the dyscalculia tutoring case (score 0.353); sepsis shows 3 pairs and 0.500. Row mapping remains uncertain because the table is garbled.
4. a24 table values and the 52-team choice count were not re-read; only the headline percentages were confirmed.
5. Trapp Table 1 is garbled in extraction; the text lines confirm the figures. The table's "no contradiction" patents show 4.84 sentences per patent vs 5.88 for the annotated set.
6. b19 and c19 agree on setup (legal assistant main case plus four more domains); no conflict.
7. a17/c02: TRIZBench Gemini pair F1 on cases is quoted as 0.36-0.42 (a17, b11) and 0.42-0.45 (the paper text says 0.42-0.45 for best ZS/FS). Treat as 0.36-0.45 depending on the row read; table was garbled.

## Contradictions between sources
- AutoTRIZ authors chose not to majority-vote contradictions (c10); a11 recommends taking the mode. Both fit: use frequency to order trials, keep diversity.
- Ogot 2006 found a doubling in quantity; the 2012 three-site replication found no significant quantity gain and a slight drop. Different designs (course sections vs controlled sessions), so not a pure refutation.
- Text-to-CAD: the paper claims TRIZ "resolves" strength-weight; its table shows only 1 of 4 principles held stress, and vanilla also stayed under 2% of yield. Text says deflection under 0.5 mm but vanilla reached 0.574 mm.

## Weak spots
- Every LLM study is small, single-model, with no matched-token plain baseline and no blind raters (K16).
- TRIZ-RAGNER (K13) looks unreliable: no model names, text that appears pasted from another paper.
- Gold labels in TRIZBench and TRIZ-GPT come from published TRIZ cases, so they reward reproducing the textbook, and may be in training data.
- Embedding similarity (cosine 0.82+) is nearly flat across prompts; it cannot rank solution quality.
- No human replication since 2013 was found; effects are student studies.

## Seen only in snippets or abstracts (not opened in full)
b01 (Hernandez 2013, abstract), b02 (Cok 2026), b20-b24, b26 (abstract), c23-c26 (Springer titles only), a29, Chulvi 2013 and Duran-Novoa 2019 (second hand), PaTRIZ baseline numbers (second hand), TRIZBench appendix and Figure 3 values.

## GAPS
1. At equal tokens, does a typed TRIZ reframe (matrix candidates, model selects) beat free reframing and a no-reframe baseline on answer correctness for our benchmarks? Nobody has measured it.
2. Is the benefit from the principle content, or only from forced problem restatement (Gero 2012 pattern)? Needs an arm "restate problem, no principles".
3. What is the end-to-end principle accuracy when the model must also predict the contradiction pair, against a random top-3 baseline? TRIZBench gives only partial figures.
4. How often does a contradiction-trigger fire on items with no real trade-off (86 of 100 in Trapp), and does gating on a failing check cut this?
5. Does the ideal-final-result prompt alone change LLM output quality or diversity? No study exists.
6. Does relational-reasoning ability (Dumas and Schmidt 2015) or concrete principle examples (Livotov 2019) moderate the effect, and would concrete worked examples help the model? Both papers unopened.
7. Do the 2025-2026 Springer IFIP papers (ARIZ with LLMs, contradiction processing, TRIZ tools as cognitive skills) report any controlled numbers?
8. Is the novelty gain from 2013 (Hernandez) reproduced by an independent lab or on a non-engineering task, and what are its effect sizes?
9. Does the TRIZ-a gain survive an untyped-mutation ablation at equal budget?
10. Do reframes that cite source spans (TRIZBench grounding) predict correct final answers better than label accuracy alone, on non-patent tasks?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d19). Claims K24-K29 added; K03 downgraded to single-source; K07, K13-K17, K20 got extra evidence ids. WebSearch budget was gone and the Semantic Scholar, OpenAlex and arXiv search endpoints rate-limited, so coverage is partial.

1. Typed reframe vs free reframe vs none, at equal tokens: STILL OPEN. The only no-TRIZ arm found is Lee et al. (d06), one chair, N=1, not token-matched. TRIZ-GPT (d14) has no no-TRIZ arm.
2. Principle content vs forced restatement: STILL OPEN. No restate-only arm anywhere. A second-hand note (d18) that random design heuristics helped humans raises the odds that restatement carries the effect.
3. End-to-end principle accuracy: CLOSED for patents and cases. Qwen3-8B zero-shot pair then matrix gives Hit@3 0.59 / 0.46 against 0.71 / 0.59 with the gold pair; TF-IDF gets 0.69 / 0.56 (d01, d03). Chance for one gold principle is 7.5%, 14.6% for two, 21.4% for three (d02). No source reports a random baseline, and a principle-frequency prior was never run. Note also that TRIZBench's LLM baselines (d01) are given the gold pair too.
4. False-fire rate on trade-off-free items: MOSTLY OPEN. TRIZBench detection F1 is 0.75-0.90 but no false-positive rate is reported (d04). Trapp's 86/100 stays the only figure. No gating study.
5. Ideal-final-result prompt alone: STILL OPEN. Two keyword sweeps found no IFR-only LLM study (d19).
6. Relational reasoning and concrete examples: HALF CLOSED. Abstracts only. Relational reasoning predicts the novelty gain (d10); less abstract wording gives more ideas (d11). No numbers; no LLM test.
7. 2025-2026 Springer IFIP chapters: STILL OPEN. Pages need a login; titles and citation counts only (d12). Not opened.
8. Hernandez replication: STILL OPEN. The 2013 paper uses the same UTEP/UMD data as the 2012 paper (d09), so it is not independent. Full 2012 tables re-read (d08): novelty p 0.0004, 0.0145, 0.5786; quantity p 0.2879-0.6291; no effect sizes. Chang et al. 2016 not readable (d13).
9. TRIZ-a vs untyped mutation: CONFIRMED OPEN by the authors themselves (d07).
10. Span-citing reframes vs answer correctness: STILL OPEN. TRIZBench shows a positive link between grounding and Hit@3 but only on patents, and as a correlation (d05).

Net: only gap 3 closed (with caveats), gap 6 half. Biggest finding for the schema: gold-pair numbers in TRIZBench overstate pipeline accuracy, and the best arm is code-supplied candidates with model selection (d01), which matches the O4 design. The decisive experiment (gaps 1, 2, 9 together: typed, restate-only, random-principle and no-reframe arms at equal tokens) has not been run by anyone.
