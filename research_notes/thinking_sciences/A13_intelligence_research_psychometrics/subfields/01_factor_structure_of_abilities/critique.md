# Critique: A13.01 Factor structure of abilities (cross-check)

## Re-opened sources (this session) and results
Re-checked from the paper text (pdftotext): Ilic & Gignac (arXiv 2310.11616 v1 and v3), Burnell et al. (2306.10062), Hendrycks et al. (2510.18212 v3), Krakauer (2604.09911).

Confirmed:
1. Ilic & Gignac 2024: N = 591, g 65.6%, omega hierarchical 0.94, mean g loading 0.81 (0.64-0.96), mean inter-test r 0.73 (0.35-0.99), 3862 -> 2415 -> 591 models, parameters vs g r = .54 [.48,.59], F(2,573) = 27.93, eta2 = .063.
2. Ilic v1 (2023): 1,232 models, first factor 85.4%.
3. Burnell et al.: mean r = .56, 3 factors .33/.31/.17 (cum .82), CFI .70, TLI .61, RMSEA .26, log size correlations .70 / -.50 / .08.
4. Hendrycks et al.: Table 1 GPT-4 8,6,4,0,2,0,4,0,0,3 = 27%; GPT-5 9,10,10,7,4,0,4,4,6,3 = 57%. Ten components, 10 points each.
5. Krakauer: PC1 90.0% (5 benchmarks, n = 19), 77% by 2024, 4-benchmark peak 95.5%, second eigenvalue 1.88 (Epoch IV), 6.4 degree rotation, leave-one-out 5.58/3.35/3.16.

## Corrections
- c04 gave n = 579 for the parameter analysis; the paper says N = 577 after outlier removal (a16 had it right). Claims use 577.
- b01 and c01 look like two papers but are the same arXiv id (2310.11616): v1 (Ilic 2023, 1,232 models, 85.4%) and the published v3 (Ilic & Gignac 2024, 591 models, 65.6%). Treat as ONE source with a sample-design effect, not two agreeing sources. Evidence ids b08 should be dropped (snippet only, "Not verified").
- Krakauer: b03 and the paper disagree internally. b03 says 246 of 546 cells filled; the paper says 246 populated and 42% coverage (246/546 is 45%). Also the 4-benchmark PC1 is reported as 92% (a24), about 93% (paper summary) and a 95.5% peak; these are different slices (epoch, full, rolling window). Cite with the slice named.
- a10 and b13 are the same Wikipedia-sourced SLODR numbers counted twice; K03 counts them as one chain plus Blum & Holling.
- c17 has no number; c14, c19 are restatements of other studies and are not independent.

## Contradictions between sources
- g share in LLMs ranges 65.6% (Ilic & Gignac) to 85.4% (same author, no de-duplication), 75% (Haznitrama, N=156), 80% (Ruan), 79% (Kipnis), 90% (Krakauer 5-benchmark), but only 33/31/17 across three oblique factors in Burnell (poor fit). Differences follow the task mix and model sample, not a clean disagreement.
- Ilic & Gignac find no separate Gf factor; Burnell and Maimon find reasoning separable (Burnell: size r .08 with reasoning). Ilic's 12 tests were mostly multiple-choice knowledge tests; Burnell included many task types.
- Krakauer sees g falling with reasoning models; Ilic & Gignac (older models) see it high. Consistent with a time trend but not tested jointly.
- Haznitrama: ARC-AGI-2 vs general average r = .09 (N = 6), against RAPM r = .87 with ARC-AGI-2. Tiny N.

## Weak spots
- Human background (Spearman, Carroll, Horn, Flynn, SLODR) comes mostly via Wikipedia summaries. Carroll's 461/800 pages and CHC lists were not opened in the primary text (a12 opened:false).
- Spearman 1904 numbers (0.78, 0.87, 1.00) were opened by the first searcher but not re-opened by me; they are as reported there.
- LLM factor studies use small models counts (29, 39, 60), leaderboard scores with contamination, heavy near-duplicate families, and non-independent observations (fine-tunes of the same base). Factor loadings from these samples measure model-family covariance as much as ability.
- No study tests a scaffold, only base models. Nothing here links factor structure to scaffold gains.
- Snippet-only items: b08 (not verified). b07 and b22 read only through abstract or secondary citation.
- Burnell's Hull-method 3-factor solution rests on poor fit indices.

## GAPS
1. Does a thinking scaffold raise g-like (general) performance or only one factor (e.g. reasoning)? No study fits factors on scaffolded vs unscaffolded arms of the same model.
2. How much of the reported LLM g is family/duplicate covariance? Need g share on one-model-per-family samples.
3. Does the g share fall as models improve (SLODR in LLMs)? Krakauer's per-epoch n is 3-8; need a larger matrix with per-model scores.
4. Is there a stable separable reasoning factor when tests are not multiple-choice knowledge tests (Burnell vs Ilic conflict)?
5. Do per-CHC-component profiles (Hendrycks) predict where a scaffold helps; and is long-term memory storage (0% for both models) really the bottleneck or an artefact of scoring?
6. Test-retest reliability of LLM scores (42% of items changed answers): what is the noise ceiling for factor loadings?
7. Does the bifactor vs higher-order fit advantage (Cucina & Byle) hold for LLM data, or is it the known fit bias?
8. Primary-source numbers for Carroll 1993 (461 sets) and Horn (9-10 broad abilities, no g) are still only secondary.
9. Does ADeLe-style demand annotation predict scaffold benefit item by item at equal tokens?

## Gap search results
Search tools were limited this pass (WebSearch budget spent; arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429). Sources came from Europe PMC full text, the local PDF text of Ilic and Gignac, Krakauer and Hendrycks, and one own computation on the Open LLM Leaderboard v2 contents (4,575 models; script A13.01_run.py in D:/research_scratch/A13.01/tmp). Evidence is in evidence_d.jsonl (d01-d18); claims K20-K24 added; K02, K03, K04, K07, K08, K09, K10, K11, K12, K14, K18 updated.

1. Scaffold effect on g or on one factor: PARTLY CLOSED, still open for the exact test. ADeLe (d01) shows reasoning-heavy models (o1, R1-distilled) gain on quantitative and logical reasoning, relevance filtering and mind modelling, while knowledge follows size. That is a model comparison, not a same-model scaffold arm. Krakauer's epoch IV second factor (eig2 1.88, n=4) points the same way but is not testable.
2. Family covariance: CLOSED (own computation, d08). PC1 73.5% on all models, 71.6% (95% 70.4-72.6) with one random model per organisation, 73.1% with one per base-model key. Family clustering shifts the g share by 1-2 points. Ilic's 591 sample is only name-and-parameter de-duplicated (d05), so the 65.6% vs 85.4% gap is mostly task mix, not family.
3. g falling with ability (SLODR in LLMs): STILL OPEN. Leaderboard halves show no fall (55.9% bottom, 59.7% top); splits on the composite are range-restricted (d09). Krakauer epochs are n=3-8 and epoch I also has eig2 above 1 (d03). SLODR detection itself is scale-sensitive (d14). The leaderboard has no frontier reasoning models.
4. Separable reasoning factor beyond multiple choice: STILL OPEN. The only second axis on the leaderboard is instruction following (d10), and almost all tasks are multiple choice. Burnell and Ilic differ by task mix; no new open-ended battery was found.
5. CHC profiles and the 0% in memory storage: PARTLY CLOSED. The 0% is a protocol effect (new session, tools disabled; d11, d12). Whether profile gaps predict scaffold gains is untested.
6. Test-retest reliability: PARTLY CLOSED. Composite internal consistency about .97 (d07); temperature-0 reruns ICC .92 or more for large models (d13) but on a rating task, versus 42% changed items in a vocabulary test (b25). No retest study on factor loadings.
7. Bifactor versus higher-order in LLM data: PARTLY CLOSED. The higher-order model failed (negative residual variances) and the bifactor model needed three correlated residuals, RMSEA .089 (d06). A bias-corrected comparison was not found.
8. Carroll and Horn primary numbers: PARTLY CLOSED. McGrew 2023 gives Carroll 2003 numbers (1 g + 9 broad, g loadings .28-.78) and Carroll's doubts on g (d15, d16). The 461 data-set count could not be verified; Carroll 1993 is lending-only (HTTP 401). Use "over 450" in agent text.
9. Demand annotation and per-item scaffold benefit: STILL OPEN. ADeLe predicts success of a fixed model (AUROC 0.84; 0.81 new tasks; 0.75 new benchmarks, d02) but no scaffold-benefit study at equal tokens exists.

Caveats on this pass: d08-d10 are own computations on normalised leaderboard scores, not peer reviewed, and use PCA not factor analysis; d18 is not re-read. No Wikipedia source was added.
