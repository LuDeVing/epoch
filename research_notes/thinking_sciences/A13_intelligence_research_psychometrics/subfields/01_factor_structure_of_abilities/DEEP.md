# Factor structure of abilities: deep document

*Subfield A13.01. Sources: evidence_a-d.jsonl (ids a01-a27, b01-b26, c01-c28, d01-d18), claims.jsonl (K01-K24), critique.md, all in this folder. Corrections from critique.md are applied: the parameter analysis uses N = 577 (not 579); b01 and c01 are the same paper (arXiv 2310.11616, v1 and v3), counted once; b08 is dropped (snippet only); a10 and b13 are one Wikipedia chain counted once. Schema parts refer to `research_notes/single_agent/SCHEMA.md` (G1-G12, S0-S9, O1-O8, section 5 memory).*

Status marks: **[E]** established (two or more independent sources), **[S]** single source, **[C]** contested. "Human background" below mostly comes through Wikipedia summaries and McGrew (2023); the original books were not opened. Carroll 1993 is lending-only (HTTP 401).

---

## 1. What it is

Factor structure of abilities asks one question. When people (or models) do many different mental tests, do the scores move together, and if so, how many separate things are behind the pattern?

Key terms an engineer needs.

- **Positive manifold.** Almost every pair of ability tests correlates positively. This is the raw fact. Everything else is a model of it.
- **Factor analysis.** A method that explains a correlation matrix with a few hidden variables (factors). Each test gets a loading on each factor. Loadings are like regression weights from a hidden score to the test.
- **g (general factor).** The hidden variable that loads on every test. In humans it takes about 40-50% of test variance; g loadings run .10 to .90, mean about .60 (a08, b12). Raven's matrices load about .80. Wechsler full-scale IQ correlates above .95 with the g factor score.
- **Three-stratum model (Carroll 1993).** Stratum III is g. Stratum II is about 10 broad abilities. Stratum I is many narrow abilities. Carroll reanalysed over 450 data sets (461 in Wikipedia; "over 450" in the CHC literature, d17) in an 800-page book.
- **Broad abilities (CHC list).** Gc crystallised knowledge, Gf fluid reasoning, Gq quantitative knowledge, Grw reading and writing, Gsm short-term (working) memory, Glr long-term storage and retrieval, Gv visual processing, Ga auditory processing, Gs processing speed, Gt decision/reaction speed (a11, b16). The topic label "nine broad abilities plus speed" matches this.
- **CHC theory.** Cattell-Horn Gf-Gc theory joined with Carroll's model. McGrew expanded it in the late 1990s. Five of seven major intelligence tests are CHC-based (b16).
- **Bifactor vs higher-order model.** Two ways to draw the hierarchy. Higher-order: g sits above the broad factors and acts through them. Bifactor: g and each broad factor load directly on tests, and are uncorrelated.
- **Omega hierarchical.** The share of total score variance due to g alone, under a bifactor model.
- **SLODR (Spearman's law of diminishing returns).** The claim that g explains less at high ability.

Why it matters to us. Our agent is a thinking scaffold, not a trained model. The factor literature gives two things. First, vocabulary for problem classes (knowledge, reasoning, memory, speed). Second, a measurement method (a models-by-tasks matrix and its principal component) that can tell us whether a scaffold raises general performance or only one ability. The literature does not tell us how to think. The schema's own status for this subfield is "background only", and this document confirms that, with a small number of measurement tools worth adopting.

---

## 2. History and theories in depth

### 2.1 Spearman 1904 (a01-a07)

Spearman ran four experimental series on English school children. Series I used the 24 oldest children of a Berkshire village school (light, weight, sound discrimination). Series II used the next 36 oldest children, sound only, tested collectively. Series IV used regular school exams and pitch discrimination (a01).

Main numbers (a02-a03):

- Corrected average correlation of pitch discrimination with four school studies: 0.78 (observed 0.57). By subject: Classics 0.89, French 0.88, English 0.73, Mathematics 0.61.
- Against total school ability: raw 0.68, corrected 0.87. School orders correlated 0.95 with each other.
- Village school: nine cross-correlations averaged 0.38. Intellective gradings correlate 0.55 with each other, discrimination gradings 0.25. The amalgamated lists correlated 0.66, giving a "true" correlation near 1.00 (another check 0.96; a music-school check 0.72 raw, again 1.00).
- "Law of the Universal Unity of the Intellective Function": on twelve random pairs of test groups the mean correlation of the common elements was "precisely 1.00", mean deviation 0.05. For dissimilar groups the commons overlap only 0.86 (74%), leaving 26% specific (a04).
- The "hierarchy of the intelligences": correlations fall in the same rank order moving away from the most g-saturated subject (Classics, French, English, Mathematics, Pitch, Music). Probable errors about 0.01 (school) and 0.03 (music). This is the early form of the tetrad pattern (a05). In Spearman's six-subject example loadings run from .958 (Classics) to .646 (Music) (a08).
- Spearman reviewed Wissler's null result (tests correlated 0.06 with intelligence, 0.09 among themselves) and explained it by low reliability and restricted range (mostly college students). His recomputation of Gilbert's data (about 1,100 children) gave 0.19 (+/-0.04) between general ability and sensory discrimination (a06). His review of 1890s studies (Gilbert about 1,200 children; Seashore about 200; Bagley 160; Kirkpatrick about 500; Binet 11) found weak or no links and blamed poor method (a07).

Method lesson: correct for noise (attenuation), remove nuisance variables (age, sex), then ask what is common. Weakness: N = 24 and 36, assumed reliabilities. Series II raw correlation was -0.25 and flipped after age was removed (a01). Later work did not find a correlation of 1.0 between sensory discrimination and g (a03).

### 2.2 Rivals to a single g (a08, b11, b15)

- **Thurstone 1938:** seven primary mental abilities, no g. The same correlation pattern can arise from several correlated group factors, and the tetrad test is weak at telling them apart (a05).
- **Sampling theory (Thomson):** many small independent processes, each test samples some. It cannot be separated from the single-factor model statistically (b15).
- **Mutualism:** abilities grow together through mutual support, producing a manifold with no single cause (b15).
- **Working-memory accounts:** the WM-g link is considerably lower in meta-analysis than once claimed. Forward and backward digit span correlate only modestly while vocabulary and Raven correlate highly. Brain damage often gives specific deficits (b15).
- **Burt:** the tetrad law fails for some pairs (b15).
- **Stankov:** g factors from different batteries are not unity (b11).

### 2.3 Cattell and Horn: Gf-Gc (a13)

Cattell proposed fluid (Gf, novel reasoning) and crystallised (Gc, learned knowledge). Gf peaks about age 27 and declines. Gc rises and stays stable to about 65. Horn pushed to 9-10 broad abilities by 1991 and rejected a single g. Dates differ by source (1941 or 1943 for Cattell's proposal; 1963 "critical experiment"; Horn and Cattell age differences 1967). Messick (1989) argued low Gf scores may reflect low interest.

### 2.4 Carroll 1993 and CHC (a11, a12, b16, d15, d16, d17)

Carroll re-analysed the factor-analytic literature with hierarchical exploratory factor analysis. Result: three strata. He thought the evidence for g "overwhelming" in 1993. Horn held there is no g. McGrew (2023, d15) reports Carroll's own 2003 analyses of 16- and 29-test WJ-R matrices: 1 g plus 9 broad factors, g loadings .28 to .78. McGrew's 2022 bifactor re-analysis of Carroll's 46-test solution gave 1 g plus 10 broad, g loadings .25 to .86; 35 of 46 (76%) at or above .50 vs 18 of 29 (62%) in Carroll's original.

Carroll himself later doubted g. After 1993 he said it was unproven that g is more than a statistical product; a g "as a true ability independent of specific abilities 'has not been adequately demonstrated and proven'" (1997, 1998, quoted second hand, d16). McGrew advises treating Cattell, Horn and Carroll as a family of CHC theories. Critics (Wasserman 2019; Geisinger 2019) doubt the empirical basis of cross-battery assessment (b16).

So the "g vs several broad abilities" debate was never closed, even inside the Carroll-Horn line.

### 2.5 Time and group stability

- **Flynn effect (b17, b18, b19).** Gains of about 2.93 points per decade (Trahan 2014). Pietschnig and Voracek 2015: annual gains .41 fluid, .30 spatial, .28 full scale, .21 crystallised. WAIS-5 about 1.2 points/decade (Winter 2024). Reversals in Norway and Denmark. Wicherts et al. (2004): gains are mostly not gains on the latent g factor (invariance not tenable across cohorts). Giangrande et al. (2026): N = 1,187 children, 1957-1999, three WISC versions; performance subtests gained more than g loadings predict. Austrian Air Force sample (N = 204, 1992-2012): no consistent change in R2 or omega-h.
- **Cross-group invariance (b23, b24).** The five-factor CHC WISC-V model is strictly invariant across France, Spain and the US. In low-IQ (N = 141, IQ <= 79) vs normal-IQ (N = 222) groups on WISC-IV only bifactor and correlated four-factor models fit; single-factor and higher-order models fit worse; only the correlated four-factor model was invariant.

### 2.6 From people to models (2019-2026)

Starting 2023 several groups ran the same analysis on leaderboards of language models. Section 6 covers them. The human tradition is the method source; the LLM studies are the evidence for us.

---

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested. "Human" rows are background through secondary sources.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Positive manifold in humans; g takes 40-50% of battery variance | loadings .10-.90, mean ~.60, SD ~.15; Raven ~.80; WAIS FSIQ vs g > .95 | a08, a09, b12 (Wikipedia chain) | [E] (K01) |
| g factors from different batteries match | r .95-1.00 for most pairs; .79-.96 when CFIT (matrices only); Stankov disputes unity | a09, b11 | [E] |
| Spearman 1904: sensory discrimination vs school ability | corrected r 0.78 (raw 0.57); total ability corrected 0.87 (raw 0.68); "true" r ~1.00 from N = 24 | a02, a03 | [E] historic, small N |
| Three-stratum structure | Carroll 461 (or "over 450") data sets; 1 g + 9 broad, g loadings .28-.78 (Carroll 2003 WJ-R) | a11, d15, d17 | [E] taxonomy, [C] role of g (K02) |
| Horn: 9-10 broad abilities, no g | Horn 1991 | a11, b16, d15 | [C] |
| SLODR in humans | r .466 (78 normal) vs .782 (22 defective) 1927; r ~.7 (IQ<78) vs ~.4 (IQ>122) 1989; g ~75% (very low IQ) vs ~30% (very high) 2009; sample 2 SD higher gives r ~.15 lower (Blum & Holling) | a10, b13, b14 | [C] (K03) |
| SLODR detection is scale-sensitive | 3 moderated-FA methods cannot separate real data from simulated no-SLODR data with different item difficulty density; only a little over half of studies confirm | d14 | [C] |
| Bifactor beats higher-order on fit | 31 batteries, 58 datasets, 1,712,509 test takers, 166 comparisons; median CFI +.076, TLI +.083, NFI +.078, RMSEA -.028, AIC -1343 | b09 | [C] (fit bias, K04) |
| Fit advantage may be a statistical bias | Murray & Johnson simulations; Gignac blames proportionality violations | b10, b20 | [C] |
| Flynn gains concentrate in fluid/performance tests | +.41 fluid, +.30 spatial, +.28 FSIQ, +.21 crystallised per year; g saturation unchanged in N = 204 pilots | b17, b18, b19 | [C] (K16) |
| CHC WISC-V invariance across countries | strict invariance FR, ES, US | b23 | [E] for Western samples |
| Single-factor models do not hold in low-IQ group | WISC-IV N = 141 vs 222 | b24 | [S] |
| Working-memory training: no far transfer to Gf | six meta-analyses, pooled SMD 0.335 (CI .223-.447) mostly on WM tasks; Jaeggi 2008 (N = 70) not robustly replicated | a13, b21, b22 | [E] (K05) |
| LLM g, 591 de-duplicated models, 12 tests | g 65.6% (7.87/12); mean g loading .81 (.64-.96); omega-h .94; mean inter-test r .73 (.35-.99); KMO .93; human g 40-50% | a14, c01, c02 | [S] (K06) |
| LLM g depends on sample design | same arXiv id v1: 1,232 models, 22 subtests, first factor 85.4% (mean loading ~.92); v3: 591 models, 65.6% | b01, c01 | [C] (K07) |
| No separate Gf in Ilic and Gignac | one combined Gkn/Grw group factor; Hellaswag loading 1.07 in 2-factor solution; factor r .78; second-order model failed (negative residual variances); bifactor needs 3 correlated residuals, RMSEA .089 | a15, c03, d06 | [S] |
| Parameter count predicts LLM g, nonlinearly | N = 577: Pearson .54 [.48,.59], Spearman .62; cubic spline F(2,573) = 27.93, eta2 .063; fast to ~10B, flat 10-20B, slow to 80B; Gkn/Grw r .11 | a16, c04 | [S] (K13) |
| Dominant first factor across other LLM studies | 75% (N = 156, loadings > .76); ~80% PC1 (77 models, 21 families; top 3 PCs ~97%); 79.3% (metabench, > 5000 models, r .938 with grand mean); 90% PC1 on a 5-benchmark core (n = 19) | a22, c09, c11, a24 | [E] (K08) |
| Own check: family covariance moves g little | PC1 73.5% on 4,575 leaderboard models; 73.1% (one per base-model key, n = 3,291); 71.6% (one per organisation, n = 715; interval 70.4-72.6); 73.9% best per organisation | d08 | [S] (K22; own PCA, not FA) |
| LLM structure has several factors on diverse tasks | Burnell: 29 LLMs x 27 tasks, 3 factors .33/.31/.17 (cum .82), mean r .56; fit poor CFI .70, TLI .61, RMSEA .26; Maimon: 60 x 44, 8 factors | a17, b04, a19 | [C] (K10) |
| Reasoning factor separable from size | log size r: comprehension .70 [.46,.85]; language modelling -.50 [-.72,-.17]; reasoning .08 [-.38,.52] | a18, b04, c07 | [S] (K11) |
| Only second axis on open leaderboard | PC2 12.3% (eig .74): IFEval (-.65) vs MUSR (.46) | d10 | [C] (K23) |
| g share falls as models improve (time) | Krakauer 4 benchmarks: PC1 peaks 92-95.5% in 2023-24 and falls to 64%; per epoch n = 3, 8, 7, 4: PC1 79, 92, 80, 64%; eig2 1.24, .28, .49, 1.88 | a24, b03, d03 | [S] (K09) |
| SLODR check on leaderboard | bottom half PC1 55.9%, top half 59.7%; bottom quartile 41.0%, top 54.7%; by size 0-4B 65.1%, 4-9B 60.6%, 9-40B 70.3%, 40B+ 70.4% | d09 | [C] (no clean fall) |
| g direction rotates with reasoning models | 6.4 deg when DeepSeek V3 enters; leave-one-out DeepSeek V3 5.58, GPT-4 3.35, R1 3.16 deg | a25, b26 | [S] |
| Item-level demand profiles predict success | ADeLe: 16,108 instances, 20 benchmarks, 15 LLMs; AUROC ~.84 in distribution (GPT-4o .882); .81 new tasks; .75 new benchmarks; ECE .01/.02/.04 | b06, c26, d02 | [E] (K12; 2 versions of one team, so lean [S]) |
| Many benchmarks lack specificity | extraneous demands (atypicality, volume, unguessability) | c28 | [S] |
| Inference-heavy models raise reasoning demands, not knowledge | o1 and R1-distilled raise QL, MCr, MS scales (even 7B distilled); knowledge follows size; o1 overall accuracy .843 vs Babbage-002 .102 | c27, d01 | [S] (K20) |
| CHC profile of frontier models | AGI score GPT-4 27%, GPT-5 57%; per component GPT-4/GPT-5: K 8/9, RW 6/10, M 4/10, R 0/7, WM 2/4, MS 0/0, MR 4/4, V 0/4, A 0/6, S 3/3 | c15, c16, d12 | [S] (K14) |
| Memory-storage 0% is a protocol effect | new session, tools disabled; both models 0 in all three MS subtests | d11 | [S] |
| Items are redundant | metabench < 3% of items, 1.24% RMSE per benchmark, 0.58% on total; tinyBenchmarks 100 items per scenario ~2% error | c11, c12, c13 | [E] (K19) |
| Aggregates are predictable, single tasks are not | BIG-Bench Hard 6 points mean abs error; single BIG-Bench tasks 18 | c25 | [S] |
| Run-to-run noise depends on setup | 42% of repeated vocabulary items changed answers across sessions; temp-0 rubric scoring ICC >= .92 (Claude >= .99); composite internal consistency median .97 | b25, d13, d07 | [C] (K18) |
| Abstract reasoning gap in LLMs | ConceptARC humans ~84% vs top ARC solver ~40 points lower; RAVEN-text open QA GPT-4 .410, ARCT .119; CoT not higher overall | c22, c23 | [C] (K15) |
| GPT-3 vs humans on matrices | digit matrices OR 1.88 (CI 1.21-2.91) generative, 6.27 (3.28-11.99) multiple choice; N = 40 humans; letter-string OR 1.76 | c20, c21 | [S] |
| Low-rank matrix: 8 skills, stable | k = 6-7 merge skills (43-60 deg); k = 9-10 add redundancy, core rotates <= 26 deg; removing 30% of models leaves factors stable (Tucker congruence >= .90) | a19, a20 | [S] |

Note on K12: the established mark in claims.jsonl counts the arXiv and Nature versions of the same team's study as two sources. Treat it as one team's result until another team reproduces it.

---

## 4. Mechanisms and models

Written so an engineer could build them. None of this is a cognitive mechanism of the agent; these are measurement mechanisms.

### 4.1 The matrix and its first component

Input: a matrix M of models (rows) by tasks (columns), entries are accuracy or IRT ability. Steps.

1. Normalise each column (z-score) so scale does not dominate.
2. Fill missing cells carefully. Mean imputation inflates g (b01). Krakauer's matrix had only 246 populated of 546 cells (42-45%) and non-random gaps (b03).
3. Compute the correlation matrix R. The positive manifold is "all off-diagonal entries > 0". Mean r: .73 (Ilic), .56 (Burnell), .82 (Krakauer 5-benchmark), .67 (own leaderboard check).
4. Principal component 1 share = largest eigenvalue / number of tasks. This is the cheap g index. It over-states common variance a little compared with factor analysis (d08).
5. Factor analysis (principal axis or ML) gives g loadings and uniquenesses. Use parallel analysis to choose factor count. Kaiser's rule plus an 85% cumulative-variance rule forces many factors (b05). Retention tests disagreed in Ilic v1: MAP, scree and Kaiser said 1, parallel analysis said 2 (b02).

### 4.2 Bifactor and higher-order

- Bifactor: each test has a loading on g and on one broad factor. All factors orthogonal. Omega-h = (sum of g loadings)^2 / total variance. Ilic and Gignac got omega-h .94 in LLMs vs high .80s in humans (a27).
- Higher-order: tests load on broad factors, broad factors load on g. This is a proportionality constraint: each test's g loading is a fixed multiple of its broad loading.
- The bifactor wins on fit almost everywhere (b09). The bias is real: a bifactor absorbs unmodelled complexity (b10). Rule for us: never choose between them on fit alone; compare predicted outcomes (does the g score predict held-out tasks?).
- Ilic and Gignac's planned higher-order model failed outright (negative residual variances). Their bifactor needed three correlated residuals added after modification indices, and RMSEA .089 broke their own .08 cutoff (d06). Fit is partly tuned.

### 4.3 SLODR test

Split by ability, fit the factor model in each band, compare g share. Two traps. (1) Splitting on a composite built from the same tests truncates range and creates artefactual correlations; both halves of the leaderboard have lower PC1 than the whole (d09). (2) Item difficulty density and skew can fake or mask the effect (d14). Valid approach: IRT-scaled abilities, bands with n above 30, split on an outside variable.

### 4.4 Sparse item selection with IRT (c11, c12, c13)

Fit an item response model (difficulty and discrimination per item, ability per model). Keep items with high discrimination and spread difficulty. metabench kept under 3% of items and rebuilt benchmark scores with 1.24% RMSE; tinyBenchmarks kept 100 items per scenario for about 2% error. Latent abilities carry information beyond sum scores (c12). Caveat: tested by cross-validation on leaderboard models, so a shift to a different kind of system (a scaffold) is not guaranteed.

### 4.5 Demand annotation (ADeLe, b06, c26, d02)

Label every item on 18-19 demand scales (11 cognitive capabilities, 5 knowledge dimensions, extraneous ones), each rated by a model annotator (agreement rWG above .75, mean .86 vs GPT-4o). Train a random forest from demand levels to per-item success of a fixed model. Calibration error .01. Use: predict where a model fails, and see which benchmarks load on unintended demands.

### 4.6 Observational scaling (c09, c10)

Take PC1-3 of many models' benchmark scores. Within a model family, PC scores are log-linear in compute (R2 > 0.9). Use weak models to predict GPT-4-class results, including agent benchmarks. Interpretation: PC1 general, PC2 reasoning (maths, coding), PC3 programming. PC1 spans five orders of magnitude, unlike saturating single benchmarks. Chain-of-thought and other post-training are named open areas, so this has not been tested on scaffolds.

### 4.7 Hendrycks CHC profile (c15, d11, d12)

Ten components at 10 points each: K, RW, M, R, WM, MS, MR, V, A, S. Manually graded tasks. Most components: text in, text out, tools off, no partial credit; at least one allows search. Memory storage items: run in a new session after information was shown, tools disabled; stateless chat models score 0 by construction. Equal weights are a design choice, the CHC mapping is by the authors, not data-validated.

---

## 5. What holds up

### 5.1 Replicated or strongly supported

- **Positive manifold in humans and in LLMs.** All human batteries; all LLM matrices (Ilic, Burnell mean r .56, Haznitrama, Ruan, Kipnis, Krakauer). K01, K08.
- **A dominant first component in LLM benchmark matrices.** 75% (N = 156), ~80% (77 models), 79.3% (> 5000 models), 90% (5-benchmark core), 73.5% (own, 4,575 models). Different teams, different samples. K08 [E].
- **Family and duplicate covariance is not what drives it.** Own computation: 73.5% on all models, 71.6% with one model per organisation (d08). Ilic's 65.6% vs 85.4% gap is mostly task mix and model range, not family (d05).
- **Working-memory training does not transfer to Gf.** Pooled SMD 0.335 mostly on trained WM tasks (b21). K05 [E].
- **Item redundancy and sparse benchmarks.** K19 [E].
- **Aggregate benchmark scores are predictable from compute; single tasks are not.** c25, c10.

### 5.2 Failures, contradictions and moderators

| Issue | What happened | Source |
|---|---|---|
| Spearman's "r = 1.00" | Rests on correction for attenuation with N = 24; later work did not find 1.0 | a03 |
| Group factors vs g | The same data fit g and several correlated factors; tetrad test cannot tell them apart; sampling theory cannot be separated | a05, b15 |
| Carroll vs Horn | No agreement about g; Carroll himself doubted after 1993 | d15, d16 |
| Bifactor advantage | May be a fit bias | b10, b20, d06 |
| SLODR | Detection is scale-sensitive; only a little over half of studies confirm directly | d14 |
| LLM g share 65.6% vs 85.4% | Same author, same arXiv id; v3 has de-duplication and a smaller battery | b01, c01 |
| Single g vs multiple factors in LLMs | 1 factor (Haznitrama), 1 + combined Grw/Gkn (Ilic), 3 factors (Burnell, poor fit), 8 (Maimon, forced by 85% rule) | a27, b05 |
| Separable reasoning factor | Burnell: size r .08 with reasoning. Not reproduced where tasks are mostly multiple choice; only instruction following shows up as PC2 (d10) | a18, d10 |
| Krakauer's fall of g | Epoch I (n = 3) already has eig2 1.24; epoch n = 3-8; coverage 42%; residual correlations after PC1 are negative by construction | d03, d04 |
| Own leaderboard SLODR check | top half not lower than bottom half (59.7% vs 55.9%) | d09 |
| Haznitrama NeuroCognition | ARC-AGI-2 vs general average r = .09 (N = 6) but RAPM vs ARC-AGI-2 r = .87 (N = 6); N 6-10 | a23 |
| Ilic loadings | Gkn tests correlate .98-.99, so part of the manifold is shared test material | c01 |
| Reliability | 42% of repeated vocabulary items changed (b25) vs ICC >= .92 at temperature 0 (d13) | b25, d13 |

### 5.3 What worked and what did not, as interventions

- **Worked (as measurement or prediction):** IRT item selection; demand annotation to predict item success; per-family log-compute scaling of PCs; few-shot plus chain-of-thought prompting to raise rater agreement with humans (d13, Mistral Large 77%, Claude 71%, GPT-4o 67%).
- **Did not work:** working-memory training for Gf (humans); chain-of-thought on abstract RAVEN-text and ARC tasks (c23: multiple-choice RAVENT scores fell for all models with CoT; GPT-3.5 rose on PVR and RAVENT open QA); scaling for TruthfulQA-like and language-modelling factors (Burnell size r -.50 with language modelling).
- **Moderator:** instruction tuning helps reasoning and hurts language modelling in Burnell, but the only large instruction-tuned models came from one lab (a18).

---

## 6. Language models

### 6.1 One general factor, large but variable

| Study | Sample | Result |
|---|---|---|
| Ilic (2023) v1 | 1,232 Open LLM Leaderboard models, 22 subtests; GLUE 88 models, 10 subtests | first factor 85.4% (87% with 2nd); GLUE ~85%; loadings .57 (TruthfulQA) to .98; mean ~.92; g scores from disjoint batteries r = .99 (b01) |
| Ilic and Gignac (2024) | 591 models (from 3,862), 12 tests | g 65.6%, mean loading .81, omega-h .94; no separate Gf; one Gkn/Grw group factor (a14-a16) |
| Haznitrama et al. (2026) | 156 models, 10 benchmarks | one factor 75%, all loadings > .76 (a22) |
| Ruan et al. (2024) | 77 models, 21 families | PC1 ~80%, top 3 ~97% (c09) |
| Kipnis et al. (2025) | > 5000 models, 6 benchmarks, 28,632 items | one factor on IRT abilities 79.3%, r .938 with grand mean; loadings .771 (GSM8K) to .966 (WinoGrande) (c11) |
| Krakauer (2026) | 39 models, 14 benchmarks, 2019-2025 | PC1 90% (5-benchmark core, n = 19); 77% by 2024 (a24) |
| Own (this session) | 4,575 leaderboard v2 models, 6 benchmarks | PC1 73.5%, 71.6-73.9% one per org/base key (d08) |

Interpretation, as the authors say it: LLM "g" looks like achievement or expertise, not intelligence (c05). Ilic and Gignac give two reasons it is bigger than human g: near-perfect score reliability (median .97 vs WAIS-IV subtests .88) and a narrow, similar test set with no spatial tests (d07). Krakauer argues g means correlation among abilities, not breadth (a26).

### 6.2 More than one factor when tasks differ

- Burnell et al. (2023): 29 LLMs x 27 HELM tasks. Three factors (reasoning, comprehension, language modelling), variance .33, .31, .17, factor correlations .43-.51. Deductive tasks (bAbI, Dyck) loaded only weakly on reasoning; bias tests (BBQ, TruthfulQA) loaded strongly on it; GSM8K loaded strongly on reasoning; HellaSwag on comprehension (c08). Model-size correlations in section 3. InstructGPT davinci-002 scored 3.58 on reasoning (a18, text cut). Bayesian FA matched (LSAT unassigned) (c06).
- Maimon et al. (2026): 60 LLMs (2B-27B plus proprietary) x 44 tasks. 8 skills: General NLU, Token Bias, Document Reading, Truthful Instruction, Domain QA, Social/Ethical, Faithful Summarization, Grad-level Reasoning (b05). Saturated easy tasks (SST-2, MNLI) compress into Factor 1; harder tasks (MedQA, LegalBench) form separate axes (a19). Tasks with wide score spread across models shape factors most; models trained on textbook-quality synthetic math and logic chains lead factor 7 (Phi-4 about +2.5 SD) (a21). Alpha .836 (b05). Labels were written by GPT-4o and DeepSeek-R1.
- Ruan: PC2 = reasoning (maths, coding), PC3 = programming (c09).
- Own leaderboard: PC2 = instruction following vs long-context reasoning (d10). In the top quartile IFEval correlates negatively with MMLU-PRO (-.26 vs +.65 full sample), but selection on the average can create that (Berkson-type).

### 6.3 What changed the structure

- **Model type and date.** Krakauer: 4-benchmark PC1 peaks at 92-95.5% for 2023-24 models, falls to 64% when reasoning models (from Sept 2024) arrive; mean r falls .90 to .43; eig2 1.88 in epoch IV. CUSUM change p = .004 (b26). Hypothesis: models that outsource reasoning to tools or chains break the shared manifold. n per epoch is 3-8 (d03).
- **Reasoning at inference.** ADeLe: o1 and R1-distilled models lift quantitative and logical reasoning, relevance filtering and mind modelling even at 7B; knowledge scales follow size (d01). This is a model comparison, not a scaffold arm.
- **Size.** Params vs g: r .54 (N = 577), plateau 10-20B, only 10 models above 80B. Params vs reading/knowledge factor r .11 (a16).
- **Training data.** Textbook-quality synthetic math training lifts factor 7 (post hoc, a21).

### 6.4 CHC-style profiling of frontier models (c15, c16, d11, d12)

GPT-4 (2023) scored 27% and GPT-5 (2025) 57% of 100 on ten CHC-based components. Gains were in reasoning (0 to 7 of 10), maths (4 to 10), reading/writing (6 to 10), auditory (0 to 6), visual (0 to 4). Long-term memory storage stayed at 0. That 0 is set by the protocol (new session, tools off), so it scores the bare model, not a model with a memory scaffold. The authors call RAG and long context "capability contortions" that create an illusion of generality (c17).

### 6.5 Abstraction and analogy (Gf-type tasks)

- Webb et al. (2023): GPT-3 above human mean on digit matrices, OR 1.88 (generative), 6.27 (multiple choice), humans N = 40. Difficulty profile r(30) = .39 (c20). Letter strings: zero-generalisation OR 1.76 (humans N = 57); performance degraded with more generalisations, as for humans (c21). Later counterfactual studies reported failures (not opened).
- ConceptARC: humans ~84% (over 90% on 11 of 16 concepts); best ARC solver (Kaggle first place) about 40 points lower on ConceptARC (c22).
- Gendron et al. (2023): open-ended RAVEN-text, GPT-4 .410 (symbolic .330), Text-Davinci-3 .343, GPT-3.5-Turbo .226, LLaMA-7B 0; ARCT GPT-4 .119; chain-of-thought not higher overall (c23).
- Chollet (2019) links CHC to generalisation levels: local, broad, extreme generalisation correspond to narrow, broad, g (c24).

### 6.6 Measurement quality

- Internal consistency of composites is about .97 (d07).
- 42% of repeated vocabulary items changed answer across sessions (GPT-3.5 and Bing; b25). At temperature 0 on a rating task Claude ICC >= .99, GPT-4o and Mistral Large >= .97, Mistral 7B >= .88 with kappa .32-.52 (d13). No retest study on factor loadings exists.
- Evaluation position papers (Zhuang et al.; Wang et al.) argue for IRT adaptive testing and construct-oriented evaluation but fit no new factors (c18, c19).

### 6.7 Gaps in the LLM evidence

No study fits a factor model on scaffolded vs unscaffolded arms of the same model (critique GAP 1). All samples are base or tuned models. Leaderboards carry contamination and near-duplicate families. The only open-ended second axis is instruction following. Frontier reasoning models are absent from the 4,575-model leaderboard.

---

## 7. What our agent should take

Overall rule from claims.jsonl: g and CHC are descriptive tools. They go into the bench, not into the agent's control logic. None of the factor findings changes a guardrail.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Tag every bench item with a problem class from the broad-ability list (Gc/knowledge, Gf/reasoning, Gq, Grw, Gsm, Glr, Gv) and log pass rates per class | S0 gate, memory class record (section 5), logging (section 6) | [E] taxonomy as vocabulary; the label-to-behaviour mapping is ours [D] | K02; a11, a12, b16, d15 |
| Use one PC1 (general capability) score of the base model as a covariate when comparing arms | G7 (pay for itself at equal tokens) | [E] that PC1 dominates benchmark matrices | K08; a22, c09, c11, a24, d08 |
| Report any g or factor share together with its sample design (n, family balancing, task mix, imputation); never cite one number | G7, logging | [E] | K07; b01, c01, d05, d08 |
| Measure run-to-run variance of the agent before comparing arms; use repeated seeds | G7, section 6 logging | contested numbers [C], but the need is [E] | K18; b25, d07, d13 |
| Use small IRT-selected item sets for cheap arm comparisons | G7 | [E] | K19; c11, c12, c13 |
| Do not assume drilling one sub-skill in the scaffold lifts general reasoning; test transfer to held-out classes | memory (lessons trusted only after helping on two different problems) | [E] human far-transfer null | K05; a13, b21, b22 |
| Label items by demand dimension (ADeLe-style) so analysis can say which demand each scaffold element helps | section 6 logging | [E] by one team with two versions; treat as a labelling aid, not a result | K12; b06, c26, d02 |
| Keep g as a descriptive index of the benchmark manifold only; do not build routes from it | none | [C] debate unresolved | K24; d15, d16 |

### Test first (see UNKNOWNS.md)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Fit a factor model on our own agent-by-task matrix with scaffold and plain arms, and check whether the scaffold adds a second factor or raises PC1 | G7, S0 | [S] | K09, K20; a24, d01, d03 |
| Per-class scaffold gain: expect gains on reasoning-type classes, none on knowledge-limited ones (the ADeLe model comparison says so; the same-model scaffold arm is untested) | S0 gate (route by class pass rate), O3/O6 use | [S] | K20, K11; d01, a18 |
| Demand-level regression: does per-item scaffold benefit scale with ADeLe-style demand at equal tokens? | S0 gate | [S] | K21; d02 |
| Score the agent on a CHC component profile with and without the memory scaffold (lessons, class record), especially Glr/MS | memory | [S] | K14; c16, d11 |
| Does a reasoning factor stay separate when tasks are open-ended, not multiple choice? | S0 task mix | [C] | K10, K23; a17, d10 |
| Is the g share falling with ability (and with scaffolded arms)? Use IRT scales and n above 30 per band | G12 (spend by difficulty) | [C] | K03, K09; d09, d14, a24 |
| Is the Burnell "instruction tuning helps reasoning" effect a scaffold analogue? | O-operators | [S] | K11; a18 |
| Does ConceptARC-style abstraction benefit from the scaffold beyond chain-of-thought? | O1-O8 at S6 | [C] | K15; c22, c23 |

None of the "Test first" items goes into SCHEMA.md until its test passes.

---

## 8. Concrete tests on our bench

All tests: both arms (plain model, scaffold) at equal tokens including setup cost (G7), at least 3 seeds, fixed items, per-item results logged.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed bench of 6-10 task families (knowledge MC, maths word problems, ARC/ConceptARC grids, riddles, code, instruction-following), >= 30 items each; also run 6+ model sizes through both arms | plain vs scaffold, same base model | PC1 share and eig2 of the (agent x task) matrix per arm; per-class accuracy gain; factor count by parallel analysis | PC1 changes little; gain concentrated in reasoning classes (positive in 1-2 classes, about zero in knowledge classes). Krakauer predicts a second factor appears with reasoning-type arms |
| T2 | Items annotated on 8-11 demand scales (quantitative, logical, abstraction, knowledge, etc.) | plain vs scaffold | Regress per-item gain (scaffold correct minus plain correct, over seeds) on demand levels; AUROC of demand-based predictor of scaffold benefit | Gain rises with reasoning demands, flat with knowledge demands; AUROC for benefit above .65 |
| T3 | Same item set run 5 times at the production temperature and at temperature 0 | plain vs scaffold | Item-level agreement (kappa), ICC of class scores, share of items that change answer | Establishes the noise ceiling on loadings; expected a changing-item share between 10% and 40% at production temperature; scaffold variance should be no higher than plain |
| T4 | Family-balanced pool: one model per family, 15+ families, same bench | plain only (to set the baseline), then scaffold on 5 of them | PC1 share with n = one per family vs all; scaffold gain vs base PC1 score | PC1 within 1-2 points of all-model (own check d08); scaffold gain is larger for lower-PC1 models if search "needs a foothold" (G12) |
| T5 | IRT-selected 100-item subset per class | plain vs scaffold | Rank correlation of arm comparison on the subset vs the full set; RMSE of score | Same winner as full set in >= 95% of arm comparisons; RMSE about 2% |
| T6 | Memory-storage items (information shown, retrieved in a later session over 48 h-equivalent turns) per Hendrycks MS protocol | scaffold with lessons/class record vs without | Score on MS items | Scaffold with memory gets non-zero score; bare model 0 (by protocol) |
| T7 | Open-ended abstraction (ConceptARC, RAVEN-text open QA) | plain vs chain-of-thought vs scaffold | Accuracy at equal tokens | Chain-of-thought not above plain (c23); scaffold above both only where the plain model already has some success (G12) |
| T8 | Bands of ability (IRT-scaled), n >= 30 per band, banded on an outside variable | plain vs scaffold | PC1 share per band | Resolves SLODR for agents; null expected on current evidence (d09) |

---

## 9. What does not transfer, and why

- **g as a causal trait.** In people g has a brain and genetics story (brain volume r about .3-.4, heritability 40-80%, about 50% overall, b12). LLM "g" is covariance among benchmarks of models that share training data, architecture and size. It describes the leaderboard, not an inner capacity (c05, a26).
- **Human percentages.** g 40-50% in people vs 65-90% in LLMs. The difference follows reliability (.97), narrow test sets and range of models (d07). Never read an LLM g share against a human one.
- **Individual vs between-model variance.** Human factor structure is between people. LLM structure is between models (c02). A single agent does not have a factor structure; only a population of agents does.
- **Population hierarchy as an agent architecture.** There is no evidence that an agent needs separate modules per broad ability. Burnell's and Maimon's factors are descriptive. This is why the schema does not add ability modules.
- **Training transfer.** Working-memory training in humans fails to transfer (b21). Whether in-context drilling transfers across tasks in a scaffold is untested; human null is only a prior.
- **SLODR, Flynn, invariance, age curves.** None have an agent analogue (b14, b17, b24).
- **Tests built for people.** Digit matrices, vocabulary tests, WISC subtests measure a different thing in a model: contamination, tokenisation and text conversion (c20, c23, b25).
- **Equal-weight CHC scoring.** Hendrycks's 10% weights are a design choice, not a validated model (c15, d12). It would be wrong to optimise the agent for that score.
- **Anything that would add ability modules or route by g.** Schema section 4b already excludes unvalidated additions; G1 (doubt only on a signal) and G7 (pay for itself) apply.
- **Spearman's own numbers.** N = 24, corrected r near 1.0 is not evidence an agent can use (a03).

---

## 10. Open questions

1. Does a thinking scaffold raise general (g-like) performance, or only one factor such as reasoning? No same-model scaffold-vs-plain factor study exists (critique GAP 1; d01 is a model comparison).
2. Does g share fall as models get better (SLODR in LLMs)? Krakauer's per-epoch n is 3-8; the leaderboard shows no clean fall (d09); detection is scale-sensitive (d14). Frontier reasoning models are missing from large matrices.
3. Is there a stable reasoning factor when tasks are not multiple choice? Burnell and Maimon say yes, Ilic and the leaderboard say not clearly (d10).
4. Is long-term memory storage really the bottleneck, or a protocol artefact (d11)? No test with a memory scaffold.
5. Does ADeLe-style demand annotation predict per-item scaffold benefit at equal tokens (K21)?
6. What is the noise ceiling for loadings? Test-retest of factor loadings is not studied (d07, d13 vs b25).
7. Does the bifactor advantage hold for LLM data without fit bias (d06)? No bias-corrected comparison found.
8. Primary-source numbers for Carroll 1993 (the 461 data-set count) and Horn remain secondary; Carroll 1993 is lending-only (d17).
9. How much of a leaderboard "g" survives if contamination is removed? Not measured in any study.
10. Does the g direction rotate when models use tools (Krakauer a25)? Rotation analysis is on few models.
11. Do skill-latent models (Sloth, Maimon) predict scaffold gains? Sloth predicts benchmark scores across families, not scaffold effects (c14).

---

## 11. Sources

[V] = opened and read this run (full text or page text). [M] = snippet or abstract only, or second hand.

Human background
- [V] Spearman (1904) General intelligence, objectively determined and measured. https://psychclassics.yorku.ca/Spearman/ and https://psychclassics.yorku.ca/Spearman/chap1-4.htm (a01-a07)
- [V, secondary] Wikipedia: G factor (psychometrics). https://en.wikipedia.org/wiki/G_factor_(psychometrics) (a08-a10, b11, b12)
- [V, secondary] Wikipedia: Spearman's law of diminishing returns. https://en.wikipedia.org/wiki/Spearman%27s_law_of_diminishing_returns (b13-b15)
- [V, secondary] Wikipedia: Cattell-Horn-Carroll theory. https://en.wikipedia.org/wiki/Cattell%E2%80%93Horn%E2%80%93Carroll_theory (a11, b16)
- [M] Carroll (1993) Human Cognitive Abilities. Count 461 only through Wikipedia; not opened (a12). https://en.wikipedia.org/wiki/Cattell%E2%80%93Horn%E2%80%93Carroll_theory
- [V, secondary] Wikipedia: Fluid and crystallized intelligence (a13). https://en.wikipedia.org/wiki/Fluid_and_crystallized_intelligence
- [V, secondary] Wikipedia: Flynn effect (b17). https://en.wikipedia.org/wiki/Flynn_effect
- [V] McGrew (2023) Carroll's Three-Stratum Theory at 30 Years, J Intell 11(2):32. https://pmc.ncbi.nlm.nih.gov/articles/PMC9959556/ (d15, d16)
- [V] Cucina and Byle (2017) The Bifactor Model Fits Better Than the Higher-Order Model. https://doi.org/10.3390/jintelligence5030027 (b09, b10, b20; Murray and Johnson read second hand)
- [V] Wilson et al. (2023) Cross-national generalizability of WISC-V and CHC. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10455271/fullTextXML (b23, d17)
- [V] WISC-IV factor structure in low versus normal IQ groups (2026). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12888695/fullTextXML (b24)
- [V] Giangrande et al. (2026) To g or Not to g? https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13738151/fullTextXML (b18)
- [V] Austrian Air Force Flynn effect and positive manifold (2025). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12118355/fullTextXML (b19)
- [V] Syed et al. (2024) Working Memory Training for Healthy Adults. https://doi.org/10.3390/jintelligence12110114 (b21)
- [M] Melby-Lervag, Redick, Hulme (2016) via Syed et al. (b22)
- [V] Sources of Artifacts in SLODR Detection (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC10026998/ (d14; Blum and Holling and Hartung numbers second hand)
- [M] Hernandez-Orallo et al. (2021) generality metric (abstract only). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8613222/fullTextXML (b07)
- [V] ChatGPT and Bing on a computerized adaptive test of verbal intelligence (2024). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11271876/fullTextXML (b25)

Language models and AI
- [V] Ilic and Gignac (2024) Evidence of interrelated cognitive-like capabilities in LLMs (v3), and Ilic (2023) v1/v2 "Unveiling the General Intelligence Factor". https://arxiv.org/abs/2310.11616 and https://arxiv.org/html/2310.11616v2 (a14-a16, b01, b02, c01-c05, d05-d07). One source.
- [M] Ilic and Gignac critic snippet (b08), dropped.
- [V] Burnell, Hao, Conway, Hernandez-Orallo (2023) Revealing the structure of language model capabilities. https://arxiv.org/abs/2306.10062 (a17, a18, b04, c06-c08)
- [V] Maimon et al. (2026) From Benchmarks to Skills (IQ Test for LLMs). https://arxiv.org/abs/2507.20208 and https://arxiv.org/html/2507.20208v1 (a19-a21, b05)
- [V] Haznitrama, Ardi and Oh (2026) A Neuropsychologically Grounded Evaluation of LLM Cognitive Abilities. https://arxiv.org/abs/2603.02540 (a22, a23)
- [V] Krakauer (2026) The Rise and Fall of G in AGI. https://arxiv.org/abs/2604.09911 and https://arxiv.org/html/2604.09911 (a24-a26, b03, b26, d03, d04)
- [V] Ruan, Maddison and Hashimoto (2024) Observational Scaling Laws. https://arxiv.org/abs/2405.10938 (c09, c10; d18 recheck not re-read)
- [V] Kipnis et al. (2025) metabench. https://arxiv.org/abs/2407.12844 (c11, c12)
- [V] Maia Polo et al. (2024) tinyBenchmarks. https://arxiv.org/abs/2402.14992 (c13)
- [V] Maia Polo et al. (2024/2025) Sloth. https://arxiv.org/abs/2412.06540 (c14)
- [V] Hendrycks et al. (2025) A Definition of AGI. https://arxiv.org/abs/2510.18212 (c15-c17, d11, d12)
- [V] Zhuang et al. AI evaluation should learn from how we test humans. https://arxiv.org/abs/2306.10512 (c18)
- [V] Wang et al. (2023) Evaluating General-Purpose AI with Psychometrics. https://arxiv.org/abs/2310.16379 (c19)
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2212.09196 (c20, c21)
- [V] Moskvichev, Odouard and Mitchell (2023) The ConceptARC Benchmark. https://arxiv.org/abs/2305.07141 (c22)
- [V] Gendron et al. (2023) LLMs Are Not Strong Abstract Reasoners. https://arxiv.org/abs/2305.19555 (c23)
- [V] Chollet (2019) On the Measure of Intelligence. https://arxiv.org/abs/1911.01547 (c24)
- [V] Owen (2024) How predictable is language model benchmark performance? https://arxiv.org/abs/2401.04757 (c25)
- [V] Zhou et al. (2025/2026) General Scales Unlock AI Evaluation (ADeLe), arXiv and Nature. https://arxiv.org/abs/2503.06378 and https://pmc.ncbi.nlm.nih.gov/articles/PMC13043289/ (b06, c26-c28, d01, d02)
- [V] Test-retest Reliability of Large Language Models and Their Concordance With Human Experts. https://pmc.ncbi.nlm.nih.gov/articles/PMC13686340/ (d13)
- [V] Own computation on Open LLM Leaderboard v2 contents. https://huggingface.co/datasets/open-llm-leaderboard/contents (d08-d10; script A13.01_run.py in D:/research_scratch/A13.01/tmp; PCA on normalised scores, not peer reviewed)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 1 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A13.01-K01** (reworded: the sources support less). Spearman numbers verified; but the later-battery .95-1.00 figure holds only for most batteries (Johnson et al., via Wikipedia) and was .79-.96 for the matrices-only CFIT, with Stankov arguing the g factors are not unity. Corrected claim: Human tests of intellectual tasks share a positive manifold; Spearman (1904) found a common factor with corrected correlations near 0.78-1.00 in small school samples, and Johnson et al. found g factors from different batteries correlating .95-1.00 for most batteries (.79-.96 for the matrices-only CFIT), though Stankov argues they are not unity.
- **A13.01-K05** (reworded: the sources support less). Syed 2024 abstract (via Crossref; full text 403) reports only a small WM gain (SMD 0.335) and says nothing on fluid-intelligence transfer; the far-transfer null rests on Wikipedia summarising a single 2012 meta-analysis plus Chooi/Redick, and Melby-Lervag 2016 was not opened. Corrected claim: Working-memory training produces small gains on working memory itself (second-order SMD 0.335), while a 2012 meta-analysis (Melby-Lervag and Hulme, as summarised on Wikipedia) found short-term, specific effects that do not generalize to fluid intelligence, and Jaeggi 2008 dual n-back gains were not reproduced in later n-back studies (Chooi and Thompson 2012; Redick et al. 2012).
- **A13.01-K08** (number corrected). The 90% PC1 on the 5-benchmark core is from n=19 models (the 39 models and 14 benchmarks are the full dataset), and Krakauer reports it falling to 77% by 2024; the other three figures (75%/156, ~80%/77, 79.3%/>5000) check out. Corrected claim: Other LLM analyses also find a dominant first factor: 75% (156 models), about 80% PC1 (77 open models), 79.3% (metabench, >5000 models), and 90% PC1 on a 5-benchmark core battery (n=19 of Krakauer's 39 models), which falls to 77% by 2024.
- **A13.01-K19** (reworded: the sources support less). Numbers verified, but both papers test sparse item sets for static LLM benchmark scores; neither tests scaffold-level (agentic) evaluation, so 'scaffold-level' is an extrapolation. Corrected claim: Evaluation cost on static LLM benchmarks can fall by using sparse item sets: tinyBenchmarks 100 items per scenario gives about 2% average estimation error; metabench uses under 3% of items for 1.24% RMSE per benchmark (0.58% on the total). Whether this carries over to scaffold-level evaluation is untested.
- **A13.01-K12** (now single-source: only one opened source, code check).
