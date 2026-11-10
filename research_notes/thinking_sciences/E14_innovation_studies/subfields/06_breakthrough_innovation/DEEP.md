# Breakthrough innovation: deep document

*Subfield E14.06, innovation studies. Key work: Kaplan and Vakili 2015 [V]. Why it matters for our agent: Selection. Evidence ids (a01..d17) and claim ids (E14.06-K01..K26) refer to evidence_a-d.jsonl and claims.jsonl in this folder. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Numbers were checked against source PDFs in the critique pass unless marked otherwise.*

Related subfields researched in parallel (links only, not covered here): Novelty measurement; Search over thoughts; Creative problem solving; Analogy and distant sources; Epistemic diversity; Methods and measurement; Anomalies and paradigm change; Scientific discovery systems; Methodologies of discovery; Peer review and replication; Tree of Thoughts; Compression at inference time. Earlier deep documents on creativity (A09, A10) and analogy (A11) overlap on distant analogy; see 00_FIELDS.md.

---

## 1. What it is

"Breakthrough" work is rare, high-impact work. Two things are usually mixed up in the word:

1. **Cognitive novelty**: the work starts something new (a new topic, a new combination, a break from the past).
2. **Economic or scientific value**: the work turns out to matter. In practice this is nearly always forward citations (top 5% or top 10%), sometimes firm value or expert interest.

The central finding of the field, from Kaplan and Vakili (2015), is that these are different targets with different best strategies. Novelty is a weak filter for value. Value is a weak filter for novelty. Both are heavy-tailed, so a few outliers carry most of the payoff and averages hide them.

Why this matters for our agent: our open-mode agent generates many candidates and then must **select**. Selection is the hard step. Judges (human and model) are near chance on idea quality (K08), idea quality on paper does not predict quality after execution (K06), and the generator pool saturates (K07). This subfield tells us what makes a rare high-impact item, which proxies for it work, and which look good but fail.

Scope limits. Most evidence is about human science and patents (citation data). The LLM evidence is about NLP research ideas and creative writing, mostly 2024 to early-2025 models, with a few 2026 studies. No study here measures real-world value of an LLM-generated idea in another field.

---

## 2. History and theories in depth

**Recombinant view of invention.** New inventions are new combinations of existing components. Fleming (2001) [M, not opened, from memory] argued that unfamiliar combinations lower the mean usefulness and raise the variance: both the best and the worst outcomes become likelier. Familiar components and combinations raise the mean (a15). Singh and Fleming (2010) [M] linked team invention to fewer failures and more breakthroughs (a16). Trajtenberg, Henderson and Jaffe (1997) [M] gave the originality index (one minus the sum of squared shares of cited patent classes) that became the "diversity" measure (a18, a04).

**Two rival theories of creativity** (a08).
- *Tension view* (Weisberg 1999; Hargadon and Sutton 1997; Ahuja and Lampert 2001): deep knowledge causes lock-in, so breakthroughs need distant, diverse recombination. This dominates management research.
- *Foundational view* (Weisberg 1999; Taylor and Greve 2006; Kuhn): only deep local knowledge shows which rules to break and where the anomalies are. Burden-of-knowledge work (Jones 2009) points the same way.
Kaplan and Vakili argue the two are complementary, each right for a different outcome.

**Kaplan and Vakili 2015 (a01-a08, b01-b03, b18, b20, b28).** The founding study. All US fullerene and nanotube patents granted through 2008 (2,826 patents; 2,384 families; regressions on 1991-2005, 2,276 observations). Novelty is measured by LDA topic modelling of abstracts (100 topics). Value is 5-year forward citations. Path model: recombination (distance, diversity) to novelty (path A), novelty to citations (path B), recombination to citations (path C). Result: a **competing mediation**. Distant and diverse recombination has a small direct citation benefit, but it makes a new topic less likely, so the total effect is near zero. Novelty comes from local, deep search. Their reading: "patents that originate new topics are more likely to be associated with local search, while economic value is the product of broader recombinations" (a01).

**Atypical combinations (Uzzi et al. 2013, a09, a10, b04, b05, b25).** 17.9 million Web of Science papers. Each pair of cited journals gets a z-score against a chance model. The best-cited papers are mostly conventional, with a tail of atypical pairs. This differs in unit and hit definition from Kaplan and Vakili, and nobody has tested both in one dataset (critique).

**Teams, distance and disruption.** Wu, Wang and Evans 2019 [M] (a11): small teams disrupt, large teams develop. Lin, Frey and Wu 2023 [V] (a14, b17): remote teams make fewer disruptive papers and patents. Park, Leahey and Funk 2023 [M] (a12): science and patents are getting less disruptive. Holst et al. 2024 [V] (a13, b06, b21): the decline is a data artefact. Park et al. reply (2025 preprint [V] d01; Nature 2026 reply [M] d02): the decline stands on the critics' own data. Leibel and Bornmann 2023 [V] (b07-b10, b22): review concluding disruption indices should not yet be used in evaluation. The index itself is from Funk and Owen-Smith 2017 [M] (a17).

**Text-based novelty and impact.** Kelly et al. 2021 [V] (b11, b19): a patent that is different from the past and similar to the future gets more citations and has higher firm value.

**Knowledge-graph forecasting.** Gu and Krenn 2024 [V] (a26, b12, b26): network features predict which unseen concept pairs become high impact.

**LLM idea generation, 2023 to 2026.** SciMON (a23, c19, c20), ResearchAgent (c26), Chain of Ideas (c24), AI Scientist (b16, b27, c23), Nova (a24, c25), AI Idea Bench (c27); then the human studies: Si et al. 2024 (a19, a20, b13, b14, b23, c01-c04), Gupta and Pruthi 2025 (a22, c07-c09), Si et al. 2025 on execution (a21, b15, b24, c05); then the 2026 work on diversity and execution grounding (d03, d04, d05, d09, d10, d11, d13, d14).

---

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Novelty raises the chance of a hit, but most novel items are not hits | Topic-originating patents: mean 5-yr citations 22.17 vs 12.77 others (all 13.507; novel range 0-187). Citations x1.4 (coef 0.330, SE 0.094). Odds of top-5% x1.7 (coef 0.538, SE 0.188). Probability 0.072 vs 0.024. Only 20 of 189 novel patents in the top 5% (109 top patents in all); under 1% of sample both. | Kaplan and Vakili 2015 (a06, b02, a01) | [S] K01 |
| Distant and diverse recombination has a direct citation benefit | N=2,276. Distance 0.211 (SE 0.093, p<0.05); diversity 0.065 (SE 0.101, ns). For the top-5% outcome neither is significant. | K&V Tables 2, 3 (a05, b03) | [S] K02 |
| Wide recombination lowers the chance of a new topic | Path A: distance -0.391 (SE 0.184, p<0.05); diversity -0.486 (SE 0.167, p<0.01). | K&V (a07) | [S] K02 |
| Total effect of wide recombination on citations is about zero (competing mediation) | Indirect via novelty: distance -0.129 (SE 0.073, one star, z about 1.8, treat as marginal), diversity -0.158 (SE 0.067). Total: distance 0.082 (SE 0.119, ns); diversity -0.093 (SE 0.118, ns). Sums check. | K&V (a07, critique) | [S] K02 |
| Inventor experience helps both novelty and citations | Positive, significant on both paths; the only such control. | K&V (b20) | [S] K17 |
| Hits are conventional plus a small atypical tail | Hits per 100 (top 5%, 8 yr): conventional core + tail novelty 9.11; conventional only 5.82; tail novelty only 5.33; neither 2.05; background 5. Shares of papers 6.7%, 23%, 26%, 44%. Holds across 243 fields, decades 1950-2000, hit = top 1% or 10%. | Uzzi et al. 2013 (a09, b04, b25) | [S] K03 |
| Most science is conventional; atypical is rare | Under 4% of papers have median z below 0; about 41% have a 10th-percentile z below 0; 40.1% of interdisciplinary journal pairs were novel. | Uzzi (a09, b05) | [S] |
| Teams add atypical combinations to a familiar base | High tail novelty 36.1% solo, 39.8% pairs, 49.7% 3+ authors (legend 36.2 / 39.9); teams 37.7% higher. Median conventionality unchanged (P 0.768, 0.417, 0.164). | Uzzi (a10, b05) | [S] K04 |
| Text score "different from past, like future" predicts impact | Median to 90th percentile: +0.7 citations at 5 yr (median 2) and +1.5 at 10 yr (median 3). One SD higher quality: 0.4 to 1.2 points higher patent value. US patents 1840-2010. | Kelly et al. 2021 (b11, b19); K&V text measure (a03) | [E] K12 |
| Remote teams disrupt less | P(D>0) 28% to 22% (papers, n=14,485,326) and 67% to 55% (patents, n=3,411,366), 0 km to over 600 km. Within-team 20.4% to 19.5% and 58.2% to 56.5%. | Lin et al. 2023 (b17, a14) | [S] human-only |
| Disruption decline is an artefact | 972,161 extra papers and 142,362 patents with CD5=1 hidden by a plotting bug. 97% (SciSciNet, 39,888,199 papers) and 78% (PatentsView) of CD5=1 works have zero references; 93% of papers and 98% of patents flagged do list references in source files. Random citation rewiring reproduces the decline. | Holst et al. 2024 (a13, b06, b21) | [C] K14 |
| Original authors' reply | Papers 1945-2010 N=22,456,096 beta -0.082 (p<0.001); patents 1980-2010 N=2,926,923 beta -0.155. SciSciNet has 2.76x (WoS) and 2.98x (PatentsView) as many zero-backward-citation works. CD=1 works: 4.3% WoS, 4.9% PatentsView, 23.1% SciSciNet. WoS decline in percentile points by variant: CYG5 36, CD5^5 23, CD5^noK 16, binary Is-D5 about 7.5. | Park et al. 2025 preprint (d01); Nature 2026 reply (d02, not read) | [C] K14 |
| Disruption validity is mixed | Percentile ranks of milestone papers: DI1 63.88, DI5 83.59, DI3% 92.72. Nobel papers 69.67 / 86.91 / 92.40. Review letters (should be low) 64.77 / 58.95 / 64.69. No correlation with reviewer ratings. Reference-count effect flips sign (under 10 refs negative, above 10 small positive). | Leibel and Bornmann review (b07-b10, b22) | [S] K15 |
| Atypicality and disruption are negatively linked | 40,935,251 articles, 1965-2024; top-5% thresholds A>22.9, D>0.04. Coefficients not extracted. | Li, Lin and Wu 2025 (d06) | [S] |
| LLM ideas rated more novel than expert ideas, at idea stage | Novelty (1-10): human 4.84, AI 5.64 (SD 1.76), AI+rerank 5.81 (SD 1.66). 49 ideas per arm, 79 reviewers, 298 reviews. Per idea: 4.86 vs 5.62 (p=0.03) vs 5.78 (p<0.01). Feasibility 6.61 / 6.34 / 6.44 (ns). Effectiveness 5.13 / 5.47 / 5.55 (ns). Overall 4.68 / 4.85 (ns) / 5.34 (p=0.04). Excitement 4.55 / 5.19 / 5.46. | Si et al. 2024 (a19, b13, b23, c01, c02) | [S] K05 |
| Novelty advantage vanishes after execution | N=43 projects (19 human, 24 AI), over 100 hours each. Ideation novelty 4.912 vs 5.778 (FDR p=0.035). After execution 4.903 vs 4.729 (p=0.586). Score change AI: novelty -1.049, excitement -1.760, effectiveness -1.879, overall -1.976. Human: -0.010, +0.078, -0.052, -0.628. Gap differences p=0.025, 0.001, 0.003, 0.004. Ideation scores predict execution scores weakly. | Si et al. 2025 (a21, b15, b24, c05) | [S] K06 |
| LLM idea pool saturates | 4,000 seed ideas to about 200 after dedup (cosine 0.8, 5%). LLM vs human proposals separable at 93.9% (Claude) and 92.6% (GPT-4o); cluster spread 0.81 / 0.72. | Si 2024 (a20, b14, c03); Gupta and Pruthi (c09); Artificial Hivemind [M] (c21) | [E] K07 |
| LLM judges near chance on ideas | Expert agreement 56.1% (NeurIPS 2021 66.0%, ICLR 2024 71.9%). LLM vs human mean: GPT-4o direct 50.0%, pairwise 45.0%; Claude-3.5 direct 51.7%, pairwise 53.3%; AI Scientist reviewer 43.3%. On accept/reject: Claude-3.5 ranker 71.4%; AI Scientist reviewer balanced accuracy 65% vs 66% for humans (AUC 0.65 both). GPT-4 review overlap 30.85% vs 28.58% human-human. | Si 2024 (a20, c04); Lu et al. (b16); Liang et al. (c16) | [E] K08 |
| A quarter of LLM "novel" proposals borrow from papers | 50 documents, 13 experts. Verified plagiarism 12/50 = 24.0% (7 direct copy, 5 combined borrowing); with unverified 18/50 = 36%; fully original 2/50 = 4%. Fresh proposals 7/36 (19%); exemplars from Si and AI Scientist 5/14 (36%). | Gupta and Pruthi (a22, c07) | [S] K10 |
| Automated plagiarism checks fail without the source | 480-paper set: Claude 3.5 oracle source 88.8%, parametric only 1.3%, retrieval pipeline 51.3%. GPT-4o 89.0% / 32.7% / 68.5%. OpenScholar 0% and Turnitin 0% on 36 papers. | Gupta and Pruthi (c08) | [S] |
| Facet-aware re-rank makes retrieval novelty checks work | On known not-novel ideas (n=58): full 89.66%; general RankGPT 13.79%; embedding only 10.34%; keyword only 5.17%. Test (32 ideas): accuracy 0.81, F1 0.79, kappa 0.59 (expert kappa 0.68). Other agent checkers 0.78/0.52, 0.56/0.19, 0.47/0.05. | Idea Novelty Checker 2025 (d13) | [S] K23 |
| Retrieve-and-revise raises novelty, not depth | SciMON: 88.9% of updates substantially different; 55.6% more novel after iteration 1; 57.8% after iteration 2 (70 instances, 5 annotators). Original paper idea better in 85% of comparisons. Nova: 3.4x unique ideas; 2.5x more top-rated (LLM judged). | SciMON (a23, c19, c20); Nova (a24, c25) | [C] K11 |
| Impact predicted by network features but experts are unimpressed | 21,165,421 papers, 141 features per pair; AUC above 0.9; top bin over 1,000x average citations. But 4,451 expert ratings (110 leaders): mean 2.403, 24.9% rated 4-5, 36.7% rated 1. High-citation-predicted pairs 2.350 vs random 2.446 vs titles-only 2.414. Interest AUC: net 63.2%, GPT-4o zero-shot 67.4%, GPT-3.5 60.4%. | Gu and Krenn 2024 (a26, b12, c10-c12) | [C] K13 |
| Fine-tuned predictors beat zero-shot at empirical outcomes | 1,585 test pairs: fine-tuned GPT-4.1 with retrieval 77.0%; zero-shot 51.4%; GPT-3.5 45.0%. 45 NLP pairs: tuned 64.4%, 5-expert vote 48.9%, best expert per topic 60.0%. Self-CoT 48.0%, LM-selected CoT 47.8%. Whole-paper summaries 53.0% vs abstract-only 38.8%. | Predicting Empirical AI Research Outcomes 2025 (c13-c15) | [S] K09 |
| AI help: individual creativity up, collective diversity down | 293 writers, 600 evaluators. Novelty +6.7% (b=0.259), usefulness +6.4% (b=0.319). Stories 5.2% closer to the AI idea. With up to 5 AI ideas novelty +8.1%, usefulness +9.0%. Low-creativity writers gain most (+10.7% novelty). | Doshi and Hauser 2024 (a25, c17, c18) | [S] K16 |
| Structure buys diversity cheaply | Plan call of 5 directions, budget split across them: distance gain 0.172 (GPT-5.4), 0.253 (Claude Sonnet 4.6), 0.134 (Gemini 2.5 Pro) at about 1.61x tokens (GPT-5.4). "Be diverse" alone: 0.039 (GPT), 0.062 (Claude) at 1.1x. Multi-agent peer2 3.71x tokens. 12 creative prompts, 64,800 outputs. | Anchorless Diversification 2026 (d04) | [S] K20 |
| Sampled personas plus CoT raise diversity of one LLM | GPT-4o, 10 fitness product ideas each. Combinations: human 197; default 83; CoT 152; persona 193; persona+CoT 248. Bootstrap (10 participants) 65.42 vs 59.66. Between-run spread: ordinary personas 0.635 vs "creative entrepreneur" 0.429. | Barriers to diversity 2026 (d05) | [S] K21 |
| Coherent, unavailable direction sampler | 16,068 LLM papers; 300 ideas per method. Vendi: Alien 225.2 vs Claude independent 56.5. Near-duplicate share 81.7% (Claude batch) vs 51.3%. Human quality 4.03 Alien = 4.03 Claude, Random 3.75, Gemini 3.68. Execution loop: Claude ideas on interpretability 2/10 to 8/10 final reports; Alien 0/10. | Alien Space of Science 2026 (d03) | [S] K19 |
| Cross-domain forcing helps humans, not strong LLMs | 140 humans, 7 LLMs, 1,002 raters, 2,800 ideas. Cross-domain b=0.36 (t=9.05); human-vs-LLM interaction b=0.48. o3 and Claude Sonnet 4 overall b=0.02 (p=.64); top 50% distance b=0.12 (p=.029); top 10% b=0.24 (p=.024). Originality vs feasibility r=-0.74. | Serendipity by Design 2026 (d10) | [S] K22 |
| Execution feedback beats rating | nanoGPT and GRPO tasks. Evolutionary search GRPO 69.4% (human best 68.8%); nanoGPT loss 3.1407 and 19.7 min to 3.28 (human best 2.1 min). RL on one reward: 119 of 128 ideas in two patterns; raised mean, not max. | Execution-grounded AI research 2026 (d09) | [S] K24 |
| Expert ratings drift | 63 researchers, 7,938 ratings, test-retest ICC 0.59-0.74. A selector aligned to wave 1 lost its gain after drift removal. | Zhang et al. 2026 (d11) | [S] K25 |
| Rare outcomes are heavy-tailed | K&V novel patents range 0-187 on mean 22; Gu and Krenn top bin over 1,000x. Selection by mean loses the tail. | a06, b12, d03, d09 | [E] K18 |

---

## 4. Mechanisms and models

Each is written so it can be coded.

### 4.1 Two-outcome path model (K&V)
Variables: R = recombination (distance D, diversity V), N = novelty (binary: new topic), C = citations.
- C = c*R + b*N, N = a*R. Total effect of R on C = c + a*b.
- Observed signs for distance: c = 0.211 (>0), a = -0.391 (<0), b = 0.330 (>0). Indirect a*b is about -0.129. Total about 0.082, not distinguishable from 0.
- Engineering reading: two knobs, two outputs. Search width raises mean value a little and lowers the odds of a new direction. Search depth does the opposite. A scheduler could set width high when it wants value and depth high when it wants a new direction. This is a human observational result, not a law for models.

### 4.2 Novelty as a code-run measure (K&V topic model, Kelly text score)
- K&V: fit LDA with 100 topics to abstracts. A document is topic-originating if its weight on a topic is at least 0.20 and it falls in the first 12 months of that topic. Thresholds 0.15 and 0.25 gave similar results (b03).
- Kelly: compute similarity of each new document to all past documents (backward) and all later documents (forward). Score = forward similarity relative to backward similarity (different from the past, like the future). Rank within year and class.
- For our agent only the backward half exists at generation time. Use backward distance to a prior-art corpus as the novelty test. Use the forward half only as an offline label.

### 4.3 Conventional core plus atypical tail (Uzzi)
- For each cited pair (i, j) compute observed count / expected count under a null that keeps each item's degree. Convert to a z-score (negative z = atypical).
- Per paper: median z (conventionality) and 10th-percentile z (tail novelty). A hit has both a high median and a low tail.
- Engineering reading: a candidate built from sources has a distribution of pairwise distances. Aim for most pairs close and a few far. A single average distance misses this.

### 4.4 Disruption index (CD)
- CD = (n_i - n_j) / (n_i + n_j + n_k): n_i later works citing the focal work but none of its references; n_j citing both; n_k citing only its references. Range -1 to +1.
- Known defects: a work with zero references and at least one citer jumps to CD=1 (a discontinuity that regression cannot fix); results depend on citation window and reference count (b10, b21). Do not use as a label.

### 4.5 Diversity by structure (plan-then-split, d04)
1. One planning call lists K broad directions (K=5 tested).
2. Split the sample budget evenly across directions; each sample is generated for one direction only.
3. Measure mean pairwise embedding distance.
Measured gain 0.13 to 0.25 over independent sampling at about 1.6x tokens; "be diverse" gives 0.04 to 0.06.

### 4.6 Coherence-minus-availability sampler (d03)
Break papers into idea atoms. Score a combination by coherence (atoms fit together) minus availability (how often the authors' communities already use them). Sample high-coherence, low-availability combinations. Result: 225.2 effective distinct ideas vs 56.5 for independent Claude samples, with the same human-rated quality (4.03).

### 4.7 Facet-aware prior-art check (d13)
1. Keyword and snippet retrieval of candidate prior papers.
2. Embedding filter.
3. LLM extracts facets (problem, method, setting) of the idea and of each retrieved paper, then re-ranks by facet match.
4. Judge novel or not novel.
The facet re-rank is the part that matters: 89.66% vs 13.79% for a general re-rank on known not-novel ideas.

### 4.8 Execution-grounded evolutionary search (d09)
Population of ideas, each run by an automated executor. Fitness = real outcome. Select, mutate, repeat. Beat best-of-N. Needs a diversity-preserving step; RL on one reward collapsed to two patterns.

### 4.9 Quality-diversity reserve (d14, d15)
Keep an archive. A new idea competes only against its nearest neighbour (niche); losers go to an archive. MMR-k subset refinement beat ranking-only on proxy ratings (abstract only). No cost versus tail-wins test exists.

---

## 5. What holds up

**Supported by two or more independent sources**
- LLM idea pools saturate and collapse to few distinct ideas (K07): Si 2024, Gupta and Pruthi, Artificial Hivemind (abstract), Doshi and Hauser (individual up, collective down), Alien Space, Anchorless Diversification. Structure pushes the wall back (d03, d04, d05), but refinement loops pull ideas back to one topic (d03).
- LLM judges are near chance on idea quality and humans are only weakly reliable (K08): Si 2024; AI Scientist (human-level on accept/reject only because the human signal is weak); Liang et al.; Zhang 2026 (rating drift).
- Text-based novelty scores relate to later impact (K12): K&V topic model and Kelly text score, different methods, same direction.
- Heavy-tailed outcomes (K18).

**Failed or disputed**
- Park et al. decline in disruption: Holst et al. say artefact; Park et al. say it survives the critics' data (variants differ from 36 to about 7.5 percentile points). Contested. Not design evidence (K14).
- Gu and Krenn: network features predict citations of concept pairs (AUC above 0.9) but experts rated LLM ideas from those pairs no better than random (2.350 vs 2.446). Impact by citation and interest diverge (K13). The forecasting paper (2402.08640) and the idea study (2405.17044) are different papers; do not merge them.
- LLM ideas more novel (Si 2024) vs less technical and weaker than the original paper in 85% of comparisons (SciMON) vs advantage gone after execution (Si 2025). Novelty is judged at idea stage by raters with 56% agreement (K11).
- K&V itself has no replication outside patents (d07). The nearest cousin, Li, Lin and Wu 2025, finds atypicality negatively correlated with disruption in 40.9M papers: related, but a different outcome.

**Moderators and boundary conditions**
- K&V: one general-purpose-technology domain (fullerenes, generality index above 0.6), citations as value, LDA with expert-tuned threshold (3 coders, reliability 0.78; topics correlate with USPTO classes 0.22). The authors attribute the weaker top-5% result to the binary outcome.
- Cross-domain forcing: no average gain for o3 and Claude Sonnet 4 (b=0.02); gain only at the far end (top 10% distance b=0.24); costs feasibility (r=-0.74).
- Doshi and Hauser: low-creativity writers gain more.
- Chan and Schunn 2015 [M, snippet]: the benefit of combination distance depends on how much convergence occurs before validation.
- Disruption: depends on reference counts and time window (b10).

**Interventions that worked**
Plan-then-split sampling (diversity); coherence-minus-availability sampling (diversity at equal rated quality); sampled personas plus CoT (diversity toward human level); facet-aware prior-art check (catching copies); evolutionary search with execution feedback (beat best-of-N on two ML tasks); human re-rank of AI ideas (overall 4.85 to 5.34).

**Interventions that did not work**
Model judges for idea quality (chance). Self-CoT for outcome prediction (48.0% vs 77.0% fine-tuned). "Be diverse" instruction (small gain). "Creative entrepreneur" persona (less spread than ordinary persona). Embedding-only or keyword-only prior-art checks (10.34%, 5.17%). Popularity priors as a selector for interest. Refinement loops (pull ideas to one topic).

---

## 6. Language models

**Idea stage.** A Claude-3.5-Sonnet agent's ideas were rated more novel than 49 expert human ideas: 5.64 vs 4.84 (p<0.01 by review), 5.81 with human re-rank. Feasibility and effectiveness did not differ (a19, c02). Rater agreement is 56.1%.

**After execution.** The advantage disappears. AI ideas fell 1.049 novelty points and 1.879 effectiveness points; human ideas about 0 (N=43, over 100 hours each). After execution novelty is 4.729 AI vs 4.903 human (p=0.586); AI is lower on excitement, effectiveness and overall (a21, c05). Ideation scores weakly predict execution scores; for AI ideas the excitement correlation was moderately negative (b24).

**Diversity.** 4,000 ideas fall to 200 unique. LLM text is separable from human text at 93.9% (Claude) and 92.6% (GPT-4o). Different models answer alike (Artificial Hivemind, abstract only). In a 2026 execution loop, Claude ideas centred on interpretability went from 2/10 ideas to 8/10 final reports (d03). Generative-AI help raised individual story novelty by 6.7% but made outputs 5.2% closer to the AI idea (stories, not research).

**What changed it.**
- Plan-then-split: +0.13 to +0.25 pairwise distance at 1.6x tokens vs +0.04 to +0.06 for "be diverse" at 1.1x (creative writing; GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Pro).
- Coherence-minus-availability sampler: 225.2 effective distinct ideas vs 56.5, equal human-rated quality (4.03). In the loop it stayed at 0/10 on the interpretability cluster; best mean rank 0.633 vs 0.574 Claude vs 0.295 random. GPT-5.5 tournament, 50 ideas per method: Alien wins 55.6% (the GPT-5.5 judge agrees 68% with experts vs 58% among experts; an LLM-judge caution).
- Sampled ordinary personas plus CoT (GPT-4o): 248 vs 197 human combinations; fixation slope 0.876 vs default 1.013 (d05).
- Cross-domain mapping: no average gain for the strongest LLMs (b=0.02); gain only on the most distant pairs (b=0.24).

**Judging and checking.**
- LLM judges are at chance on ideas. The AI Scientist reviewer is human-level on accept/reject (65% vs 66%) only because the human signal is weak (AUC 0.65).
- Ratings drift (ICC 0.59-0.74); a selector tuned to one wave lost its gain.
- Plagiarism: 24.0% verified (36% unverified); automated checkers 0% to 1.3% without the source; with an oracle source 88.8% to 89.0%.
- Retrieval novelty check: facet re-rank 89.66% vs 13.79% general re-rank.
- Fine-tuned predictor of empirical outcomes 77.0% vs zero-shot 51.4%, but it needs training data.

**Execution grounding.** On nanoGPT and GRPO tasks, evolutionary search with execution feedback reached GRPO 69.4% (human best 68.8%). RL on one reward collapsed diversity (119 of 128 ideas in two patterns) and raised the mean, not the maximum. Execution rate over 90% for Claude-4.5 self-execution; the same ideas run by GPT-5 42-78% (d09). ML tasks only.

**Caveats.** Human-study models are mostly mid-2024 to early-2025. Most LLM evidence rests on one group (Si, Yang, Hashimoto). Several 2026 results use LLM judges or proxies. Creative-writing and product tasks are not research ideas. No reasoning-model test of idea quality was found.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | The generating model is not the idea selector. Model judges are near chance on ideas (43% to 53%) and expert agreement is only 56.1%. Already in G8 and G5; add these ids as support. | G8, G5 | [E] | a20, b14, c04, b16, c16, d11 (K08) |
| A2 | In open mode, widen the pool by structure, not by instruction: plan directions then split samples (or sample ordinary personas). "Be diverse" alone is weak. Over-generating from one prompt saturates (4,000 to 200). The saturation is [E]; the specific method is [S] (see T7, T8). | S3 (open mode) | [E] saturation | a20, b14, c03, c09, a25, d03, d04, d05 (K07) |
| A3 | Keep a small reserve of low-rated but atypical candidates through selection. Outcomes are heavy-tailed and mean-based selection loses the tail. Reserve size is a design guess [D]; log it. | S7 | [E] tail; reserve [D] | a06, b02, a09, b12, d03, d09 (K18) |
| A4 | Where a novelty proxy is needed, use a code-computed "different from prior art" score (backward distance to a prior-art corpus). | S4, S7 | [E] signal; our use [S] | b11, b19, a03 (K12) |
| A5 | Do not use disruption-index results or citation-popularity priors as design evidence or selectors. Add to section 4b. | none (4b) | [E] unsafe | a13, b21, b22, c11 (K14, K13) |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Cheap execution or test step before an idea is ranked; compare paper-stage ranking to post-test ranking. | S4, G8 | [S] | a21, b15, b24, d09 (K06, K24) |
| T2 | Facet-aware prior-art check in code at S4 in open mode, dropping candidates that match prior work. | S4, G8 | [S] | a22, c07, c08, d13 (K10, K23) |
| T3 | Separate novelty and expected-value scores; never take the top-novelty pick as the top-value pick (20 of 189 novel patents were hits). | S7 | [S] | a06, b02, b18 (K01) |
| T4 | Two search modes: deep local search for new directions (dig into failing outputs and anomalies in the home domain), far search for value or reach. Far analogies are not the default novelty engine. | O7 vs S5/S6 | [S] | a05, a07, a08, b20 (K02, K17) |
| T5 | Conventional-core-plus-atypical-seed prompts vs all-atypical vs all-conventional. | S3 | [S] | a09, b04, d10, d11 (K03) |
| T6 | Gate analogy (O7) by embedding distance plus a separate feasibility check. | O7 | [S] | d10 (K22) |
| T7 | Distance-from-already-proposed penalty (or coherence-minus-availability) at selection, to stop homogenisation across refine loops. | S3, S7 | [S] | d03, d04 (K19, K20) |
| T8 | Sampled ordinary personas as an open-mode diversity operator (one model, code selection). G4 and G9 still forbid persona voting on single-answer problems. | S3 | [S] | d05 (K21) |
| T9 | Rank candidates by pairwise tournament rather than absolute scores; do not tune selectors on one snapshot of ratings. | S7 | [S] | a20, a24, d11, d16 (K25) |
| T10 | Retrieve-and-revise loop against prior work, scoring depth separately from novelty. | O (revise) | [C] | a23, a24, c19, c25 (K11) |
| T11 | Memory: deep domain retrieval first, then far analogies, vs the reverse order. | memory, S3 | [S] | a08, d12 (K17) |

Not to re-propose: team-size or remote-team results (K04, K14) do not apply to one agent.

---

## 8. Concrete tests on our bench

All arms use equal total tokens per item; report tokens per arm. Item types are open-mode tasks (NoveltyBench-style prompts, our own research-idea prompts) and, where stated, tasks with a runnable check.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | 40 NoveltyBench prompts | (a) N independent samples; (b) plan-then-split into 5 directions; (c) "be diverse" instruction | Distinct items after dedup at cosine 0.8; NoveltyBench distinct count | (b) above (a) by a clear margin; (c) small. Literature: +0.13 to +0.25 distance at 1.6x tokens, so cut N in (b) to match tokens. |
| B2 | 30 research-idea prompts with a prior-art corpus | (a) no prior-art check; (b) facet-aware retrieval check dropping matches, then selecting | Share of selected ideas with a verified prior-art match (oracle source or blind human) | (b) lowers the match rate. Literature baseline 24% verified, 36% unverified. |
| B3 | 30 coding or ARC-like tasks with a runnable check, open-mode generation | (a) rank by model self-score; (b) rank by pairwise tournament in code; (c) rank by cheap execution result | Agreement of pick with held-out outcome; pick equals best candidate available | (c) above (b) above (a); (a) near chance. |
| B4 | 30 prompts | Seeds: (a) all conventional; (b) all atypical (far sources); (c) one conventional anchor plus one atypical source | Novelty (distance to prior art, by code) and value (blind rating or run), separately | (c) at least matches (a) on value and (b) on novelty. No LLM ablation exists. |
| B5 | 30 problems with a home domain | (a) far analogy first (O7); (b) deep dive on failing outputs first; (c) deep then far | Novelty (code distance) and value (run), separately | Per K&V, (b) higher novelty, (a) equal or higher value. Order effect unknown. |
| B6 | 20 problems with a runnable cheap test | (a) top 1 by score; (b) top 1 plus 2 reserved atypical low-rated candidates run through the test | Max outcome over the run (not mean); tokens spent on the reserve | (b) recovers tail wins at small token cost. Pass only if the maximum rises. |
| B7 | 30 prompts, 3-round refine loop | (a) refine only; (b) refine with a distance-from-proposed penalty | Share of ideas in the largest topic cluster before and after the loop; value | (b) lower concentration. Literature: 2/10 to 8/10 without it. |
| B8 | 30 analogy prompts | (a) no source; (b) random source; (c) source in top 10% distance with a feasibility check; (d) any far source | Originality and feasibility, rated separately | (c) above (b) on originality without the feasibility drop; (d) lowers feasibility. |
| B9 | 30 open prompts | (a) default; (b) sampled ordinary personas with short CoT; (c) "creative" personas | Unique idea combinations after dedup; between-run spread | (b) above (c) above (a). |
| B10 | 40 candidate pairs with a runnable outcome | Re-rate the same items after a delay (two snapshots) | Test-retest agreement of model-judged ratings | Expect ICC about 0.6 to 0.75; tells how far to trust a fixed selector. |

---

## 9. What does not transfer, and why

- **Team and distance results** (Uzzi teams, Wu et al., Lin et al.): they describe people with different tacit knowledge. Samples from one model are not independent (G4), so a same-model ensemble will not reproduce a team effect (a10, a25).
- **Disruption index results** (Park et al., Leibel and Bornmann): a contested measure with known artefacts; no design content for a single agent (K14, K15).
- **Citations as value**: a noisy proxy (Bessen 2008, cited in b18). For an agent, value must come from a run or a check.
- **Fullerene patents**: one domain, a general-purpose technology. The K&V direction is a hypothesis for our tasks.
- **Idea-stage LLM novelty** (Si 2024): rated by humans with 56.1% agreement on NLP prompting ideas. Not evidence of real breakthroughs (K05, K06).
- **Fine-tuned outcome predictors** (c13): need training data; not a scaffold-only lever.
- **Network-feature forecasts** (Gu and Krenn): need a citation graph; impact does not equal interest.
- **Creative-writing diversity gains** (d04, d05): not research ideas; the link between diversity and idea value is unknown.
- **Human cross-domain gains** (b=0.36): do not carry to strong LLMs on average (b=0.02).

---

## 10. Open questions

1. Does the K&V finding (deep local search yields new topics; distant recombination does not) replicate outside fullerene patents, for papers, code or LLM ideas? No replication found (d07).
2. Which selector is best for rare high-impact LLM ideas: pairwise tournament, retrieval prior-art check, or past-vs-future novelty score? No head-to-head exists (d17).
3. Does a conventional-core-plus-atypical-seed prompt raise value or novelty at equal tokens? Zhang et al. use such pairs but have no ablation (d11).
4. Does a reserve of low-rated atypical candidates recover tail wins, and at what token cost?
5. Do reasoning models or tree search reduce the diversity wall at equal tokens? RL on one reward collapses diversity (d09).
6. Does retrieval grounding with a prior-art filter lower the plagiarism rate, and does novelty then survive execution?
7. Which order is better: deep first then far, or far then deep? Only a snippet-level hint (d12).
8. Does execution-grounded evaluation of LLM ideas hold in non-ML fields with 2025-2026 models?
9. Which disruption variant, if any, is robust? Variants disagree (36, 23, 16, about 7.5 percentile points); no neutral adjudication read.
10. How much does rating drift (ICC 0.59-0.74) limit any selector tuned on human ratings?
11. Does a sampled-persona or role-mix result reproduce the team effect on atypical combinations (37.7%)? Only diversity has been measured so far.

---

## 11. Sources

[V] opened and read. [M] snippet, abstract, second-hand or not opened.

- [V] Kaplan and Vakili (2015) The double-edged sword of recombination in breakthrough innovation, SMJ 36(10). https://keyvanvakili.github.io/files/recombination_breakthrough_innovation.pdf (author PDF); https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/smj.2294 (a01-a08, b01-b03, b18, b20, b28). Publisher page https://doi.org/10.1002/smj.2294 [M] (403).
- [V] Uzzi, Mukherjee, Stringer and Jones (2013) Atypical combinations and scientific impact, Science 342. https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf
- [M] Wu, Wang and Evans (2019) Large teams develop and small teams disrupt, Nature 566. https://www.nature.com/articles/s41586-019-0941-9 (abstract only)
- [M] Park, Leahey and Funk (2023) Papers and patents are becoming less disruptive, Nature 613. https://www.nature.com/articles/s41586-022-05543-x (abstract only; described via Holst et al.)
- [V] Holst et al. (2024) Dataset artefacts are the hidden drivers of the declining disruptiveness in science, arXiv 2402.14583. https://arxiv.org/abs/2402.14583 ; https://arxiv.org/pdf/2402.14583
- [V] Park, Leahey and Funk (2025 preprint) Robust evidence for declining disruptiveness. https://arxiv.org/html/2503.00184v1
- [M] Park, Leahey and Funk (2026) Reply to: Dataset artefacts can partially drive the measured decline in disruption, Nature 656:14-21. https://www.insead.edu/faculty-research/publications/journal-articles/reply-dataset-artefacts-can-partially-drive-measured (not read)
- [V] Lin, Frey and Wu (2023) Remote collaboration fuses fewer breakthrough ideas, Nature. https://arxiv.org/pdf/2206.01878 (Nature abstract https://www.nature.com/articles/s41586-023-06767-1 is [M])
- [V] Leibel and Bornmann (2023/2024) What do we know about the disruption index in scientometrics? https://arxiv.org/pdf/2308.02383 (studies it reports on, such as Bornmann 2020, Leahey 2023, Shibayama and Wang 2020, Ruan 2021, Sheng 2023, Deng and Zeng 2023, are [M] second-hand)
- [V] Li, Lin and Wu (2025) Can recombination displace dominant scientific ideas? https://export.arxiv.org/pdf/2506.15959
- [V] Kelly, Papanikolaou, Seru and Taddy (2021) Measuring technological innovation over the long run, NBER w25266. https://www.nber.org/system/files/working_papers/w25266/w25266.pdf
- [V] Gu and Krenn (2024/2025) Forecasting high-impact research topics via machine learning on evolving knowledge graphs, arXiv 2402.08640. https://arxiv.org/pdf/2402.08640
- [V] Gu and Krenn (2024) Generating interesting scientific ideas using knowledge graphs and LLMs (SciMuse), arXiv 2405.17044. https://arxiv.org/abs/2405.17044
- [M] Fleming (2001) Recombinant uncertainty in technological search, Management Science 47. https://doi.org/10.1287/mnsc.47.1.117.10671
- [M] Singh and Fleming (2010) Lone inventors as sources of breakthroughs, Management Science 56. https://doi.org/10.1287/mnsc.1090.1072
- [M] Funk and Owen-Smith (2017) A dynamic network measure of technological change, Management Science 63. https://doi.org/10.1287/mnsc.2015.2366
- [M] Trajtenberg, Henderson and Jaffe (1997) University versus corporate patents. https://doi.org/10.1080/10438599700000006
- [M] Chan and Schunn (2015) The importance of iteration in creative conceptual combination, Cognition. https://www.lrdc.pitt.edu/Schunn/papers/Chan-Schunn2015-Cognition.pdf (404; search summary)
- [V] Si, Yang and Hashimoto (2024) Can LLMs generate novel research ideas? arXiv 2409.04109. https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto and Yang (2025; ICLR 2026) The ideation-execution gap, arXiv 2506.20803. https://arxiv.org/pdf/2506.20803
- [V] Gupta and Pruthi (2025) All that glitters is not novel, arXiv 2502.16487. https://arxiv.org/abs/2502.16487
- [V] Wang, Downey, Ji and Hope (2023/2024) SciMON, arXiv 2305.14259. https://arxiv.org/abs/2305.14259
- [V] Hu et al. (2024) Nova, arXiv 2410.14255. https://arxiv.org/abs/2410.14255
- [V] Doshi and Hauser (2024) Generative AI enhances individual creativity but reduces collective diversity, arXiv 2312.00506. https://arxiv.org/abs/2312.00506
- [V] Lu et al. (2024) The AI Scientist, arXiv 2408.06292. https://arxiv.org/abs/2408.06292
- [V] Predicting empirical AI research outcomes with language models (2025), arXiv 2506.00794. https://arxiv.org/abs/2506.00794
- [V] Liang et al. (2023) Can LLMs provide useful feedback on research papers? arXiv 2310.01783. https://arxiv.org/abs/2310.01783
- [M] Artificial Hivemind (2025), arXiv 2510.22954, abstract only. https://arxiv.org/abs/2510.22954
- [M] Li et al. (2024) Chain of Ideas, arXiv 2410.13185, abstract only. https://arxiv.org/abs/2410.13185
- [M] Baek et al. (2024) ResearchAgent, arXiv 2404.07738, abstract only. https://arxiv.org/abs/2404.07738
- [M] AI Idea Bench (2025), arXiv 2504.14191, abstract; tables garbled. https://arxiv.org/abs/2504.14191
- [V] Artiles et al. (2026) The Alien Space of Science. https://arxiv.org/pdf/2603.01092
- [V] Anchorless diversification for parallel LLM ideation (2026). https://arxiv.org/html/2605.30150
- [V] Examining and addressing barriers to diversity in LLM-generated ideas (2026). https://arxiv.org/html/2602.20408v1
- [V] Towards execution-grounded automated AI research (2026). https://arxiv.org/html/2601.14525v1
- [V] Liu et al. (2026) Serendipity by design. https://arxiv.org/html/2603.19087
- [V] Zhang, Wang and Chen (2026) Scientific judgment drifts over time in AI ideation. https://arxiv.org/pdf/2511.04964
- [V] Idea Novelty Checker (2025). https://arxiv.org/html/2506.22026v1
- [M] Budgeted subset refinement for execution-aware LLM research ideation (2026), abstract only. https://arxiv.org/pdf/2607.14118
- [M] IDEAgent (2026), secondary summary. https://pub.towardsai.net/ideagent-agentic-quality-diversity-search-for-research-idea-generation-bcea0b63600a
- [M] SciDER (2026), search summary. https://arxiv.org/pdf/2603.01421
- [M] K&V replication search (this run; London Business School page). https://www.london.edu/faculty-and-research/academic-research/t/the-double-edged-sword-of-recombination-in-breakthrough-innovation
