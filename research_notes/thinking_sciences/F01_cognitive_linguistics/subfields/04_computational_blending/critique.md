# Critique: F01.04 Computational blending (cross-check)

## Numbers re-opened this session (all from the source text, pdftotext)
1. Schapiro et al. 2026 (arXiv 2509.21043): 59.0 / 53.4 / 43.4 (LLM) and 22.1 / 32.9 / 12.8 (human) confirmed; 97.1% abstraction-bottleneck figure confirmed; 19.9% (412/2,070) confirmed; 94.7% vs 36.3% and 14.3x confirmed; N=75 retained of 120 recruited, 35 LLMs confirmed; the one model at 64.8% blending (gpt-5.6-sol) confirmed.
2. PopBlends (arXiv 2111.04920): 56.0 / 55.3 / 58.7, 93.3%, 98.3%, 2.03 vs 0.87, 2.86 (57%) confirmed.
3. Cunha et al. 2017 (arXiv 1706.09076): 9 participants, 39 blends, 30 raters, 12 blends confirmed in text. 23 of 39 not re-derived from the table.
4. Misty (arXiv 2409.13900): 14 developers, 103 operations, 36 / 35 / 19 / 9 / 4 split, 3.2 (SD 1.3), 31 below 3, 44 above, 28 neutral confirmed.
5. Ge and Parikh 2021 (arXiv 2106.14127): 96.34%, 9 unique raters per item, P@10/100/1000 values confirmed.
6. Shrager 1987 (Springer PDF): seven undergraduates, mean gap 27.7 s (SD 5.7), SD 12.9, 5,760, about 124 million, up to 6 view applications / 12 interactions confirmed.
7. Lieto and Pozzato (arXiv 1811.02366): EXPTIME-complete, 3.02% scenario, 20.4% trivial scenario confirmed.

## Corrections
- PopBlends reliability: evidence lines (a26, b11, c03) call the 0.41 agreement "kappa". The paper says it is Pearson's correlation. Use "0.41 Pearson", not kappa.
- Ge and Parikh Table 3: the text extraction shows a "ConceptNet" header and row labels (Elmo, BERTBase, BERTLarge, GPT) that do not line up with the five numeric rows. The 1.12 / 2.70 / 5.90 row is read as ConceptNet because the text says ConceptNet was lowest. b13 already flagged label loss; a23 asserts "ConceptNet 1.12/2.70/5.90" and "best LM row", which is probable but the per-model labels for the other rows remain unverified.
- K14 and others: "kappa" removed from claims.

## Contradictions and tensions
- PopBlends 93.3% best-of-5 (GPT-3, 2021, 30 pairs of pop domain by product) vs Schapiro 43.4% single-attempt (35 current LLMs, random Wikidata pairs). Different tasks, not a contradiction, but it shows best-of-k plus a check carries a lot of the success. No source measured the same task both ways.
- Xu 2026 shows a strong one-shot prompt takes most of the gain (MI 2.75 to 3.69) before the full pipeline (4.56). This weakens a simple "staged beats one-shot" story. The authors own the benchmark and Gemini-3-pro is generator and one of the judges.
- Schapiro finds LLMs far above humans (43.4 vs 12.8), but humans were allowed to skip (skips scored zero) and had only 5 items per task. Part of the gap is effort.

## Weak spots
- Single-source almost everywhere. Only K04, K12, K13, K14 reach "established", and K12 and K13 are about absence of evidence.
- Founding programs (Shrager 1987, TCL, Divago) have no benchmark, no baseline and no replication. Divago was read only second-hand (b04). Guhe 2011, Eppe 2018 (87 citations), Veale 2019 and the COINVENT chapters were not opened (a16 to a21: 403 or paywall).
- Almost all LLM blending evidence is images (Ge, Cho, Matsuhira, Peng, Hernandez, Xu). Text-reasoning blend with an LLM is covered only by Schapiro (KOMBINE) and PopBlends. Little tests blending as a reasoning step inside problem solving.
- Judges are LLMs in most 2024 to 2026 work (K14).
- Song et al. 2025 only seen as a citation (c27). c28 and parts of a16 to a21, a04 are snippet or title level.
- Web search quota was exhausted; arXiv/OpenAI-style APIs rate limited (429) at cross-check, so forward citations (who replicated) were not systematically searched.

## GAPS
1. Does an explicit generic-space step plus verifier raise valid-blend rate on text reasoning items for a current model at equal tokens, over a strong one-shot prompt? (decides whether the blend operator is worth adding)
2. Does blending help on any downstream reasoning benchmark (e.g. insight problems, ARC-style, novel-tool tasks) rather than on blend-quality ratings? No study found.
3. What is the failure rate of "coherent but wrong" blends (Shrager's watch-plus-BASIC case) in LLMs, and does a consistency check catch it?
4. Song et al. 2025 (peeled apple still red): what exactly do they measure for combination, and what scaffolds did they test?
5. Are there any independent replications of Divago, Eppe et al. 2018 (COINVENT), or Guhe 2011? Open Eppe 2018 and Pereira and Cardoso 2006 full text for numbers.
6. Does inventive homogeneity (K03) also appear within one model across samples, and does an exclusion-list memory fix it at equal tokens?
7. How well do LLM judges for blend validity agree with humans on current models (the 75% figure is bounded)? Needs a separate-family judge test.
8. Is the Xu 2026 gain (one-shot 3.69 vs staged 4.56) reproducible by someone other than the authors, and at what token cost (about 8.3k tokens and 4 min per sample)?
9. Conceptual combination (noun-noun) and analogical inference subfields run in parallel: do they supply a better-tested alternative to the blend operator? Check overlap before adding O-level machinery.
10. Newer text-only LLM blending studies from 2025 to 2026 beyond Schapiro: any with measured results on creativity or reasoning tasks?

## Gap search results (2026-11-01, evidence_d.jsonl d01 to d18)
Tools: web search quota was gone. Used arxiv.org search pages, Semantic Scholar citation lists, and arXiv PDFs (pdftotext, deleted scratch afterwards). OpenAlex was budget-blocked. Publisher PDFs (Eppe 2018) and a Pereira and Cardoso pdf were not reachable.

1. Generic-space step plus verifier vs strong one-shot at equal tokens: OPEN. No text study found. Nearest: Universe of Thoughts C-UoT (d05): about equal to CoT on HypoArena (19.5 vs 18.8 win rate), best on one of three creative tasks. PRISM (d11, images): refinement wins human choice 57.65%, smaller with stronger models.
2. Downstream benchmark: OPEN, but a test bed found. CresOWLve (d04, 2,061 items, factual subset as control, creative drop up to 17 points) tests no blend scaffold. Still no study with a blend operator and a reasoning score.
3. Coherent-but-wrong rate: PARTLY. Cases documented (KOMBINE subtly wrong generic spaces; Song: parent properties kept, property type right only 56.4%) but no rate and no catch test (d03, d10).
4. Song et al. 2025: CLOSED (d01 to d03). Noun-phrase combination with emergent/canceled/component properties, 12,315 items; scaffolds Base, CoT, spreading activation, oracle best-of-5. GPT-4o: SA +2 to 5 points over CoT, oracle +12 to 17.
5. Independent replications of Divago, Eppe 2018, Guhe 2011: OPEN. Eppe has 87 citers, none a re-implementation by title; texts still unopened (403/404). Donvito and Lieto 2026 (d14) is a rubric by TCL's own author, not a replication.
6. Within-model homogeneity and exclusion list: PARTLY. Within-model similarity above 0.8 confirmed on open prompts (d07). Showing prior answers helps distinctness at extra calls (d08). Equal-token exclusion-list test for blends still OPEN.
7. LLM judge vs human on blend validity: PARTLY. Narrow property judge r=0.85 (d03); item-level creativity r=0.342, novelty n.s. (d06); factuality judge precision 0.52 (d09). Separate-family judge on blend validity still OPEN.
8. Xu 2026 reproducibility and cost: OPEN. Six citers, none re-run (d12).
9. Overlap with parallel subfields: CLOSED as an overlap check (d15). Analogy-then-solve with call-matched baselines and grounding checks already exist in A09.04, A11.02, C10.03, C04.03. The blend operator has to beat that first.
10. Other 2025 to 2026 text-only blending studies: CLOSED as a search (d05, d08, d16, d17, d01): none tests a generic-space step with a verifier on reasoning. Image work is the bulk (d18).

Corrections noted: Song table rows come shifted by one row in the pdf text; mapping fixed using the text statement about the gold score. New claims K16 to K23 added; K12 stays established and now has three sources; K03, K04, K14 extended.
