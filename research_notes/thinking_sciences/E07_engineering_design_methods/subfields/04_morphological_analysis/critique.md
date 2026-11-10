# Critique: E07.04 Morphological analysis (cross-check)

## Corrections and confirmations
Re-opened the full text of five LLM papers (arXiv PDFs, pdftotext) and checked the numbers.
- c06 Si et al. 2024: confirmed. 4000 seed ideas, dedup at cosine 0.8, about 5 percent non-duplicates.
- c05 Si et al.: confirmed. Novelty 4.84 (human), 5.64 (AI), 5.81 (AI + human rerank), N=49 each.
- c13 Yu et al. 2023: confirmed. 5 percent of ChatGPT query cost; NYT location bias 68.01 percent vs 0.69 percent.
- c20 AutoTRIZ: confirmed. 7 of 10 cases match or half-match in the top 3; entropy bound 6.64.
- c11 Verbalized sampling: confirmed 25.7 percent human-evaluation gain and 66.8 percent of base diversity. The "1.6-2.1x" range is quoted from the abstract-level text (1.6- seen; upper end not re-checked).
- c12 Hivemind: confirmed 79 percent of cases above 0.8; 61.2 percent under min-p; 71-82 percent cross-model.
- Arithmetic checked by hand: 4x4x4x3x3x4 = 2304; 4x4x3x3x2x2 = 576; 480/34560 = 1.4 percent kept, so 98.6 percent removed; 4^6 = 4096; 12 of 12 and 5 of 12 = 41.67 percent. All correct.
- No evidence line needed a numeric correction.
- Not re-opened (Oppenlaender, Saurabh, Field, Bonde, Hu, Ritchey): the arXiv and API fetches for them failed or returned the wrong paper. They stand on the first agents' reading (marked opened:true).

## Contradictions and tensions
- Dating of Zwicky's 576-configuration propulsion box: 1947 (a06) vs 1962 (a12). Unresolved.
- Ritchey's claim that structure does not hurt creativity (a10) is untested, and the human data (b08, b12, b14) show no breadth gain from the box.
- Hu 2020 finds morphological analysis loads the prefrontal cortex most, but Field 2011 and Daly 2016 find no output advantage. Activation is not quality.
- Bonde 2024 says software forces reduction; the same software gave students strings they used as a filter (b06). The tool shapes use in both good and bad ways.
- Yu 2023 lists enumerating all combinations as too costly, while Ritchey's CCA claim says enumeration after pruning is cheap. These fit only if pruning comes first.

## Weak spots
- All reduction and benefit claims (90-99 percent, audit trail, garbage detection) come from one advocate.
- Human studies are small, student-based, short, and often not randomised. Bonde has 8 teams; Field has self-selected technique use.
- Ma 2023 and Meincke 2024 use older models (GPT-3, GPT-4); results may not hold for current ones.
- Absence claims (K04) rest on thin search; Semantic Scholar, OpenAlex and arXiv were rate-limited.

## Only seen in snippets or abstracts
Gero 2012, Kannengiesser 2013, Shah 2000, Eftekhari 2021, Savchenko 2020, Chen 2024 (no numbers), Sharbafi 2021 (no numbers), Daly 2016 (abstract only), Park and Geum 2025, Xiao 2026, Filippi 2023, Nomaguchi 2025, McIntosh 2026 (abstract plus one reading), Zwicky 1969 (second-hand).

## GAPS
1. Does an LLM-built Zwicky box with code enumeration beat free sampling and verbalized sampling on coverage and validity at equal tokens? (No direct study found; Park and Geum 2025 and Chen 2024 may answer part of it.)
2. What are the actual numbers in Chen et al. 2024 and Park and Geum 2025 (sample, design quality, load)?
3. How accurate are LLM pairwise cross-consistency judgments against human experts, and how many triple-wise conflicts slip through?
4. How reproducible is LLM construction of the parameters and values (dimension choice) across repeated runs and models?
5. Is there any independent (non-Ritchey) measurement of how much CCA shrinks real fields and whether the surviving configurations are better?
6. When the field is too large (10^6 and up), which pruning or sampling rule keeps coverage best (random, rank-based trimming, diversity-greedy)?
7. Does category-first (classify the space) beat combine-first for an LLM, as Saurabh 2022 suggests for humans?
8. Does box-driven generation reduce or increase cross-run homogeneity (hivemind effect) compared with persona or verbalized sampling?
9. Do structured boxes help on non-design tasks the agent faces (reasoning puzzles, planning), or only on open design problems?
10. Does Zwicky's original 1969 text contain empirical claims (the "hundreds of unconsidered configurations") that can be checked?

## Gap search results
Search tools were limited: OpenAlex and Semantic Scholar rate-limited, the arXiv API returned empty, and the web search budget ran out. Sources were opened by direct PDF fetch. New evidence is in evidence_d.jsonl (d01-d17); claims K21-K28 added; K03, K09, K12, K13, K17, K19, K20 updated (K20 now supported).

- Gap 1 (box + code enumeration vs free vs verbalized sampling at equal tokens): OPEN. No direct study. Nearest: random constraints 0.735 vs plain 0.679 diversity (d04); Lang2Morph validity 0.82 vs zero-shot 0.52 (d01); volume baseline (d06).
- Gap 2 (Chen 2024, Park and Geum 2025 numbers): OPEN. Chen PDF blocked (403), Park and Geum page unavailable. Chen's three-arm design noted (d13, d14).
- Gap 3 (LLM pairwise compatibility accuracy, triples): PARTLY. No compatibility-vs-expert study. Order instability of pairwise judges 0.07-0.44 and human 0.33 (d03, d16). Triple conflicts: still no data.
- Gap 4 (reproducibility of dimension choice): PARTLY CLOSED by proxy. Taxonomy generation: 0.285 of sibling pairs repeat across 324 runs (d07, d08). No study on design parameters.
- Gap 5 (independent CCA measurement): OPEN. Nothing found (d17).
- Gap 6 (pruning rule for 10^6+ fields): OPEN, proposals only: covering arrays (d11), coverage-prior sampling (d10); random-constraint injection works for diversity (d04).
- Gap 7 (category-first vs combine-first): OPEN. No head-to-head found (d15, d17).
- Gap 8 (box vs hivemind homogeneity): PARTLY. Homogeneity is cross-model; pooling 4 vendors reaches human diversity 0.763 vs 0.773 (d05). No box-specific test.
- Gap 9 (non-design tasks): OPEN. UltraGen shows many-constraint filling degrades (d02); no reasoning-puzzle or planning study of boxes found.
- Gap 10 (Zwicky 1969 claims): CLOSED as far as possible. The claim is an assertion; second-hand via Ritchey 1998 (d12). The 1947 vs 1962 dating of the 576 box stays unresolved.
