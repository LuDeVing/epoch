# Atypicality versus disruption: deep document

*Subfield E14.05. Evidence files: evidence_a.jsonl (a01-a30), evidence_b.jsonl (b01-b26), evidence_c.jsonl (c01-c27), evidence_d.jsonl (d01-d16). Claims: claims.jsonl (E14.05-K01 to K21). Cross-check: critique.md. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Two measures of "new" in science look alike but are not the same.

- **Atypicality (novelty, A-index).** Built from the paper's inputs. Take every pair of journals in the reference list. Compare how often the pair is co-cited with how often chance would give (a z-score). A paper is atypical if some pairs are very rare. This is Uzzi et al. 2013. It looks only at references (a13, d01, a23).
- **Disruption (D, CD index).** Built from the paper's later use. Among later papers that cite the focal paper, count those that cite it but none of its references (they treat it as a replacement) against those that cite both (they treat it as a continuation). D runs from -1 (consolidating) to +1 (disruptive). Funk and Owen-Smith 2017 (a14).

The 2025 paper by Li, Lin and Wu (arXiv 2506.15959, a01, b01, c01) argues that these two capture different processes:

- Atypical work **extends** ideas into new topic areas by joining far-apart parts.
- Disruptive work **replaces a dominant idea inside its own topic**. It does the same job as the incumbent, only better ("functional equivalence", a02).

Their data: about 41 million articles, 1965 to 2024 (OpenAlex). Mean D falls as the A-index rises in every discipline, period and team-size panel (Fig 3, 40,935,251 articles). No coefficient is printed (d04).

Why it matters for our agent. At an impasse or in open mode the agent must choose what kind of attempt to try: a distant combination (analogy, transfer) or a rival to the current best answer in the same frame (displacement). The literature says these are different attempts with different payoffs, and that the usual ways to score novelty (a model's opinion, or a citation score) are unreliable. Schema parts touched: O7 (map an analogue), O2 (generalise), O8 (reframe), S3 (open mode), S7 (select), G8 (novelty judged by running).

Honesty note. This literature is about human papers and citation networks. Almost nothing tests it on LLM agent attempts (b26, d15). Everything for the agent is by analogy.

## 2. History and theories in depth

**2.1 Combinatorial view of novelty.** Innovation as new combination of old parts. Uzzi et al. 2013 (Science 342) made it measurable. Web of Science papers 1990-2000. Hit = top 5% of citations. Hit rate per 100 papers (d01):

| Profile | Hit rate per 100 | Share of papers |
|---|---|---|
| Conventional core + novel tail | 9.11 | 6.7% |
| Conventional only | 5.82 | 23% |
| Novel tail only | 5.33 | 26% |
| Neither | 2.05 | 44% |

Background rate 5. P < 0.00001. Team papers were 37.7% more likely to add novel combinations. No odds ratio is printed in the main text. Only citation impact is measured, not disruption. [E] as a human result; no LLM-measure replication found (critique gap 8).

**2.2 Disruption index.** Funk and Owen-Smith 2017 for patents (a14). Wu, Wang, Evans 2019 (Nature 566) applied it to 65 million papers, patents and software 1954-2014: small teams disrupt, large teams develop. 877 Nobel papers were used for validation (a15, b09). Not opened first-hand.

**2.3 Atypicality and disruption positively linked (2022).** Lin, Evans, Wu 2022 (arXiv 2103.03398; a10, a11, a12, b05, b06, d02, d03). MAG: 87,860,684 articles, 35,431,832 with both measures. Highly atypical papers (top 10% by median z) disrupt 61% against 36% for conventional papers ("nearly two times"). The pooled correlation is tiny: typicality vs D r = -0.05, p < 0.001. Typicality is the reverse of atypicality, so this means atypical goes with disruptive. Only 2.3% of papers are highly atypical, down from 3.9% (1970) to 1.4% (2000). D takes about 10 years to reach 80% of its final value. Atypical papers are late bloomers: sleeping-beauty index vs atypicality r = 0.08. Cohort t-tests on the 2018 disruptive-citation fraction: 23.85 (1970), 33.04 (1980), 52.78 (1990), 88.76 (2000). The effect is stronger in computer science and engineering than in biology, chemistry, physics. Citation impact peaks for mixed typical and atypical references; disruption chance peaks for the highly atypical. Atypicality was also modelled as embedding distance: the journal-pair z-score is a pointwise mutual information; skip-gram embeddings (50 dimensions, window 10, 5 negatives; 2,429 journals in 1970, 8,009 in 2000) correlate r = 0.74 with the z-score.

**2.4 Atypicality and disruption negatively linked (2025).** Li, Lin, Wu 2025 (a01-a05, b01-b04, c01-c04, d04). Same group, opposite headline. Top-5% cut-offs: A > 22.9 and D > 0.04 (40,453,825 articles 1965-2020). Top-5% atypical papers rise over time while top-5% displacing papers fall (Fig 2). H1: A and D negative, supported in Fig 3. H2: theories are harder to displace than methods. Functional-equivalence examples: Turing 1937 displaced Goedel 1931 (6 years); Barabasi-Albert 1999 displaced Erdos-Renyi; Watts-Strogatz 1998 displaced Milgram 1967 (31 years).

**2.5 D reframed as displacement.** Lin, Li, Wu 2025 (arXiv 2504.04677; a06, a07, b16). D = d_p / (1 + b_p). d_p is local displacement (share of citers citing only the paper minus share citing it with its references). b_p is burden: citations of the most-cited reference over the paper's own. Reference citations follow Zipf's law (a = 1.89, b = 0.60). Median b_p = 119, so 1/(1+b_p) is about 0.01. Only 1% of papers have b_p < 1. So D mostly measures displacement of the single most-cited reference.

**2.6 The decline debate.** Park, Leahey, Funk 2023 (Nature 613) reported falling disruption (a16, not opened). Rebuttals: Petersen et al. (citation inflation; a18, b11, b12), Holst et al. (dataset artefacts; a17, b13), Bentley et al. (weighted index flat; a19, b14), Fang and Evans (fixed benchmark shows atypicality rising; a21). Defence: Lin et al. 2025 (a09, b16), Park et al. 2025 (second-hand).

**2.7 Validity and specification critiques.** Bornmann and Tekles 2020 (a22), Leibel and Bornmann 2023 and 2024 (a23, a24, b08-b10, b15), Liang et al. 2020 (a25), Wei 2020 Nobel null (b09), Larregue and Gingras 2026 (b19).

**2.8 The team-size fight.** Wu 2019: small teams disrupt. Petersen: positive with a 5-year window (a18, b12). Lin et al. 2025 (arXiv 2502.00219; a08, b17): reproduce the positive result at 5 years; the negative link returns with longer windows, turning near 10 years. Huang and Xie 2026 (a26, b18, d12): equalise reference counts and the gradient reverses. Lin, Yang, Wu 2026 (a27): reply. Unresolved.

**2.9 Third framing: generalization.** Fang and Evans 2025 (a20, a21, b20, c07, d06): foundation, extension, generalization indices. 73.96% of "disruptive" citations are generalization (the idea is cited alone, in a distant context). D vs G r = 0.37; D vs E r = -0.37; D vs F r = 0.05 (U-shaped); df = 23,448,429.

**2.10 Content and embedding measures.** Wang 2024 (c08), Kim, Kojaku, Ahn 2025 (a28), Semantic Geometry R-P-C (c19), SchNovel (c15), NovBench (c16). Mostly abstract-level.

**2.11 LLM work.** Novelty of generated ideas (Si 2024), execution (Si 2025), borrowed ideas (Gupta and Pruthi), retrieval (Tracing), search strategies (Heuresis), judges (RQ-Bench, ICLR catalyst study). See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hit rate highest for conventional core plus novel tail | 9.11 vs 5.82 vs 5.33 vs 2.05 per 100 (background 5); team papers 37.7% more likely to add novel combos | Uzzi 2013 (d01) | [E] human, one source opened |
| Atypical papers disrupt more (2022) | 61% vs 36%; typicality vs D r = -0.05; 2.3% highly atypical; 3.9% to 1.4% (1970-2000); MAG 35.4M papers | Lin, Evans, Wu 2022 (a10, d02) | [C] (sign flips in 2025) |
| Atypical papers get disruptive credit late | sleeping-beauty r = 0.08; t = 23.85 to 88.76; D 80% settled in ~10 years | a11, d02 | [S] |
| Atypicality as embedding distance | r = 0.74 between z-score and skip-gram inner product | a12 | [S] |
| Higher A means lower D (2025) | 40,935,251 articles; negative in every stratum; no coefficient; cut-offs A > 22.9, D > 0.04 | Li, Lin, Wu 2025 (a01, d04) | [S], [C] vs 2022 |
| D = displacement of top reference | 65% of 22M papers have d_p < 0; 38% of 42M have D > 0; only 1% have b_p < 1; Zipf a = 1.89 | a06 | [S] (authors' own index) |
| Disruptive papers share a field with top reference | 0.52 vs 0.014 model-predicted (37x); 49,077 papers | a07, critique correction 1 | [S] |
| Expert survey agrees with D | 20 scholars, 190 responses; disruptive mean D 0.21 (top 1%); consolidating -0.011 (bottom 13%); AUC 0.83 | a07, b16 | [S] |
| LLM labelling theory vs method | Llama-3.1-70B zero-shot; 50,147 papers; theory probability falls with year gap | a04, d14 | [S], unvalidated |
| Method papers more disruptive; theory dominant longer | Goedel to Turing 6 yr; Milgram to Watts-Strogatz 31 yr; Leahey 2023: methods raise D, theories lower it | a05, a23 | [S] |
| Decline of disruption is partly or fully an artefact | 97% of CD5=1 papers and 78% of patents have zero references; R2 0.15 to 0.95 (papers), 0.10 to 0.52 (patents); 972,161 hidden papers | Holst (a17, b13) | [E] (4 sources); Park defends |
| Citation inflation biases CD | growth 0.051/yr (doubling 13.6 yr); br = -0.0039 (CI -0.0055 to -0.0023); 18,644 PNAS papers; ~35% CD fall from density | Petersen (a18, b12) | [E] |
| Team-size sign depends on window and reference count | positive at 5-yr window; negative again after ~10 yr; 1.7M-paper regression | a08, b17, a26, a27 | [C] |
| D validity is mixed | Wei 2020: Nobel 0.236 vs matched 0.239, p = 0.898; Wu 2019: Nobel mean D 0.10 above 3,372,570 controls; Breakthrough of the Year AUC 0.26 | b09, a26, d12 | [E] mixed |
| Pairwise 1D beats D on prizes | AUC 1D vs D: Nobel 0.981 vs 0.731; Turing 0.942 vs 0.792; Lasker 0.979 vs 0.597; PR Milestones 0.975 vs 0.398; Breakthrough 0.951 vs 0.259; 47,134,871 papers | Huang, Xie (a26, d12) | [C] |
| 1D label flaw | Davis BEC Nobel paper: pairwise D -0.59, -0.04, +0.89, +0.96 vs original D -0.55; Nobel AUC oneD 0.97, D 0.78, abs D 0.89; 107 (21%) of Nobel set negative | Lin, Yang, Wu 2026 (a27) | [C] |
| Generalization is most disruptive citation use | 73.96%; D vs G 0.37; D vs E -0.37; foundation 0.059 to 0.025 (-57.6%); generalization 0.405 to 0.214 (-47.2%) | Fang, Evans (a20, b20) | [S] |
| Semantic atypicality predicts awards | positive and significant in all tested domains; one SD of F index raises Nobel odds ~58% to 104%; non-Nobel sets 4.7M, 5.6M, 3.9M papers | d06, a21 | [S] |
| Fixed benchmark: atypicality rises, not falls | per-period z recomputation caused part of the decline | a21 | [S] |
| LLM use shifts citations to generalizing works | +0.050 SD arXiv (CI 0.030-0.071); +0.117 bioRxiv; +0.081 SSRN; 65,072 treated authors | b21 | [S], detector-based |
| AI ideas rated more novel before execution | 4.84 human, 5.64 AI, 5.81 AI+rerank; N = 49 per arm; 79 reviewers; 298 reviews; feasibility 6.34 vs 6.61 n.s. | Si 2024 (b22, c09) | [S] |
| Novelty lead vanishes after execution | N = 43 experts, 100+ hours; AI change -1.049 novelty, -1.760 excitement, -1.879 effectiveness; human -0.010, +0.078, -0.052 | Si 2025 (b24, c11) | [S] |
| LLM idea diversity is low and borrowed | ~200 of 4000 seed ideas non-duplicate (5%); 24% of 50 documents paraphrased or heavily borrowed (13 experts); 79.3% of ideas dominated by 1-2 papers | b23, c12, c22 | [E] (3 sources) |
| Retrieval cuts local diversity | within-set -5.6% to -17.9%; pooled +10.2% to +18.1%; 45,000 ideas, 15 topics, 10 models | c22, d11 | [S] |
| LLM judges weak | best pairwise 53.3% (chance 50%); 71.4% accepted vs rejected (61.1%, 63.5% for others); human agreement 56.1% | b23, c10 | [E] |
| LLM novelty rater below chance on catalysts | AUC EDM 0.83, CD 0.60, node2vec 0.49, LLM rater 0.42; 36,113 ICLR papers; review score vs disruptiveness abs rho <= 0.005 | c18 | [S] |
| Search strategies do not reach novelty at top quality | 3,222 runs; 0 rated Original; 1 idea both top-10 and novel; 40 fabrications in 1,628 runs (~2.5%) | Heuresis (c23, d07, d09) | [S] |
| Novelty-seeking yields rare ideas | Curiosity nanoGPT 13/300 (appendix) vs 20/200 (text); OMNI unlearning 14.1% novel-side, none beat baseline; surprise vs quality r = -0.11 | d08 | [S] |
| Prefilter plus execution in algorithms | 2 of 8 problems beaten; circle packing n=26 2.636 vs 2.634 human; reward model rejected 151 ideas: 108 true failures, 43 viable | AlphaResearch (d10) | [S] |
| Planned search gives more unique ideas | 3.4x unique novel ideas; 2.5x top-rated; 170 seed papers | Nova (c21) | [S], abstract only |
| Multi-agent LLM teams beat humans on creativity | 4,541 vs 341 ideas; d = 1.50 | c24 | [S], abstract only |
| Open-source model lineage mostly consolidates | 2,556,240 models; mean MDI -0.53; median MDI -0.9636 (<1B), -0.9259 (1-10B), -0.8000 (>10B) | a29 | [S] |
| Patent CD depends on data coverage | non-US advantage falls by 64% to 148% of US baseline mean once international citations are added | Rutzer (d13) | [S] |

## 4. Mechanisms and models

An engineer can implement each of these as a small function.

**4.1 Atypicality score (Uzzi).**
1. For every pair (i, j) of cited journals, count co-citations observed.
2. Build a null: shuffle citations among papers, keeping each journal's citation total and each paper's reference count. Many shuffles.
3. z(i,j) = (observed - mean_null) / sd_null.
4. Per paper: conventionality = median z over its pairs; novelty = 10th percentile z. Low z = atypical.
5. Fix the benchmark period when comparing across years (a21).

Agent analogue: replace "journal pair" by "concept pair" (method family, domain). Atypicality = embedding distance between the parts combined (a12: r = 0.74 with the z-score). Cheap: cosine distance between embeddings of the two source ideas.

**4.2 Disruption (CD).** For focal paper f: n_i = later papers citing f and none of its references; n_j = citing f and at least one reference; n_k = citing a reference but not f. D = (n_i - n_j) / (n_i + n_j + n_k). Needs a citation window (5 to 25 years) and a minimum number of references. Known failure points: zero-reference records, reference-list length, network density (a17, a18).

**4.3 Displacement view.** Per-incumbent: D(f, r) = (share citing f only minus share citing both) over reference r. The paper's D is approximately d_p / (1 + b_p) (a06). The pairwise "1D" version averages D(f, r) over single references (a26). Practical rule: always name the incumbent. A paper can displace one reference and consolidate another (a27, Davis BEC example).

**4.4 Agent version of displacement (design; not in the sources).**
- Incumbent = the current best answer or rule after S4.
- Candidate = a new attempt.
- Displacement test in code: the candidate passes the check where the incumbent fails and still passes everywhere the incumbent passes (S7 already has a discriminating test).
- Atypicality score = embedding distance between the candidate's key idea and the incumbent's, or between the two source ideas of a combination.
- Four cells: (near, replaces), (near, fails), (far, replaces), (far, fails). Record counts per problem class in S9.

No source validates this (critique gaps 3, 5, 9).

**4.5 Generalization (Fang and Evans).** F, E, G come from how later papers cite the focal paper together with its references (F), with its references' neighbours (E), or alone in distant contexts (G). The agent analogue is O2 (generalise): an attempt that subsumes two earlier solutions in one rule. Detect: the new rule reproduces the outputs of both earlier solutions on their cases.

**4.6 LLM as measuring tool (Li, Lin, Wu).** Prompt: given Paper A and its reference Paper B, is A (1) a theory innovation or (2) a method refinement. Read the token probability of option 1 (a04). Robust to few-shot, rewording and a third option. Not validated against humans. If used, calibrate on a labelled set first (G3).

**4.7 Execution gate (Si 2025, Heuresis, AlphaResearch).** Rank ideas by running them. Optional cheap prefilter. Measure its false-reject rate (AlphaResearch: 43 of 151 rejected ideas were viable, 28.5%). Audit for reward hacking (about 2.5% of runs fabricated).

**4.8 Dedup across attempts (Si 2024).** Embed each attempt's idea; cluster at cosine 0.8; count distinct clusters. Only about 5% of 4000 ideas were distinct, so raw sample count overstates diversity.

## 5. What holds up

**Established.**
- Counting-based disruption is sensitive to reference-list length, network density and missing references. Four independent groups: Petersen, Holst, Bentley, Fang and Evans (a17-a21). K05, K06.
- D validity is mixed: Nobel results flip across studies, Science Breakthrough AUC below 0.5, country rankings look wrong (b09, b19, a26). K07.
- Hidden analyst choices change results (a24, a25, b15). K08.
- LLM-generated ideas have low diversity and are often borrowed (b23, c12, c22). K14.
- LLM judges are poor at novelty (b23, c10, c18, c13). K15.
- Conventional core plus novel tail beats pure forms in human citation data (d01). K18.

**Failed or contested replications.**
- Park decline: failed in Holst (zero-reference artefact; random rewiring reproduces the decline), Petersen (inflation), Bentley (flat with weighted index). Defended by Lin et al. and Park 2025. About 85% of the decline survives randomization in null networks per Huang and Xie (a26), so the question is not closed.
- Small teams disrupt: depends on window (5 yr positive for large; 10+ yr negative) and on reference count. Pairwise 1D reverses it. Pairwise D mislabels developmental Nobel work. Open.
- Nobel validation: Wu 2019 positive (mean D 0.10 above controls), Wei 2020 null (p = 0.898), S. Wang 2023 coefficient -6.777 (p = 0.125), Wei 2023 +0.071 (p < 0.001).
- Sign of A vs D: 2022 positive, 2025 negative, same group. Candidate causes (d05): MAG vs OpenAlex; median z vs top-tail A-index; longest D window to 2018 vs unstated; pooled r vs binned means. Never tested on one corpus.

**Moderators and boundary conditions.**
- Field: the atypicality-disruption link is stronger in computer science and engineering than in natural sciences (a11, b06).
- Time: atypical papers need about 10 years to show disruption (d02).
- Contribution type: new methods raise D; new theories and results lower it (Leahey 2023); the reverse for self-rated originality (Shibayama and Wang 2020, r about 0.10 to 0.17) (b08).
- Reference count: effect negative below about 10 references, positive above in five WoS fields (Ruan 2021) (b10).
- Data coverage: patent CD drifts with missing foreign citations (d13).
- Baseline: a moving z-score benchmark hides the atypicality rise (a21).

**Interventions that worked (LLM side).**
- Plan-then-retrieve loop: 3.4x unique novel ideas (c21, abstract only).
- Human re-rank of AI ideas: novelty 5.64 to 5.81 (b22).
- Pooled retrieval over different paper sets: +10.2% to +18.1% diversity (d11).
- Reward-model prefilter plus execution: beat the human best on 2 of 8 problems (d10).

**Interventions that did not work.**
- Retrieval inside one paper set: diversity -5.6% to -17.9% (d11).
- Six search strategies in Heuresis: no widening of the quality-novelty frontier; curiosity signal does not predict quality (r = -0.11) (d07, d08).
- LLM judging by comparison: stronger novelty mirage (c13).
- LLM rater for catalyst papers: below chance (AUC 0.42) (c18).
- Review scores for future disruptiveness: abs rho <= 0.005 (c18).

## 6. Language models

**6.1 LLMs as the thing measured (ideation).**
- Before execution: AI ideas rated more novel (5.64 vs 4.84, N = 49 per arm, 79 reviewers) at similar feasibility (b22, c09). Reviewer agreement was 56.1%, so ratings are noisy.
- After execution: AI ideas drop 1.05 (novelty), 1.76 (excitement), 1.88 (effectiveness) on a 1-10 scale; human ideas barely move. Final excitement 3.90 vs 4.48, effectiveness 4.13 vs 4.78 (not significant, N = 43) (b24).
- Borrowing: 24% of 50 AI documents paraphrased or heavily borrowed, 76% with some overlap, found by 13 experts (c12). Plagiarism detectors miss it.
- Diversity: ~5% non-duplicates of 4000 (b23). 79.3% of ideas dominated by 1-2 retrieved papers (c22).
- Executed agent search: 3,222 runs, six strategies, three ML domains. No idea rated Original. One idea both top-10 on quality and weakly novel. Novel-side ideas cluster in specific edits (residual-stream changes on nanoGPT). Polishing the known recipe won on quality in 2 of 3 domains. 40 fabrications in 1,628 runs (d07-d09).
- Algorithms: 2 of 8 problems beaten, by tiny margins (2.636 vs 2.634); a learned prefilter wrongly rejected 43 of 151 (d10).
- Multi-agent teams: d = 1.50 over human teams on creativity ratings, 4,541 vs 341 ideas (c24). Abstract only; novelty rated, not executed.

**6.2 LLMs as judges of novelty.**
- Pairwise: best 53.3%, others 43.3-51.7% (chance 50%) (c10). Accepted vs rejected: 71.4% best (b23).
- ICLR catalyst papers: LLM rater AUC 0.42 vs EDM 0.83 (c18).
- RQ-Bench: judges rate generated questions as highly novel; comparison strengthens the mirage; experts prefer anchored references (c13, abstract only). LLM agents overestimate originality (c14, abstract only).
- Retrieval-augmented novelty (RAG-Novelty) beats baselines on SchNovel, 15,000 pairs (c15, abstract only). NovBench: limited grasp (c16, abstract only).

**6.3 LLMs as measuring tools in this subfield.**
- Llama-3.1-70B zero-shot labels theory vs method; token probability tracks year gap (a04). Unvalidated.
- LLM topical similarity between paper and top reference (a03). Coefficients not printed.
- Embedding-based disruption (a28) and semantic atypicality (d06) as non-citation alternatives. The latter predicts awards in all tested domains.

**6.4 LLMs as users of science.** After detected LLM use, authors' references shift toward generalizing, cross-field works by +0.050 to +0.117 SD (b21). Detector-based and self-selected.

**6.5 LLMs as nodes in a network.** Model Disruption Index on Hugging Face: mean -0.53; larger models somewhat less consolidating; median MDI rises from -0.9636 (<1B) to -0.8000 (>10B) (a29, c20).

**6.6 What changed what, by how much.** Human re-rank: +0.17 novelty (5.64 to 5.81). Execution: -1.05 to -1.88 points. Retrieval: -5.6% to -17.9% inside a set, +10.2% to +18.1% across sets. Plan and search: 3.4x unique ideas. Nothing compares distant-analogy and in-topic attempts at equal tokens (d15).

## 7. What our agent should take

### Add now (established)

1. **Dedup attempts before counting them.** Cluster attempt ideas; count distinct ones. Schema part: O4 / S4 / S7 (code does it, G5). [E] K14. Evidence b23, c12, c22, d11.
2. **Novelty is judged by running; execution is the first rank.** Reinforces G8. Novelty is at most a tie-break. [E] for the direction (several sources agree LLM novelty falls after execution), though the numbers rest on one RCT (N = 43). Schema part: G8 / S7. Evidence b24, d07, d10, d16, c18. Already in the schema; this adds the numbers.
3. **No model as sole novelty judge.** Reinforces G5 and G8. [E] K15. Evidence b23, c10, c13, c18.
4. **Control for length when scoring any novelty or disruption number.** Reinforces G5 (length-normalise). [E] K05. Evidence a17, a18, b12.
5. **Report spread across metric variants; fix windows and baselines.** Applies to our own bench reports. [E] K06, K08. Evidence a21, a24, a25, b15.
6. **Do not use a citation-style score or a single scalar as reward.** [E] K07. Evidence b09, a26, b19.
7. **Audit the verifier when execution is the judge.** About 2.5% fabrications (40 of 1,628). Schema part: S4 / G3. [S] but cheap; adopt as a harness check. Evidence d09.

### Test first (not established; see UNKNOWNS.md)

1. **Two attempt types in open mode.** Tag each open-mode attempt "distant-mix" (O7, O2 across domains) or "displace-the-leader" (new rule for the same job). Schema part: S3, O7, O3. [C] K01-K03. Evidence a01, a02, a07, d05. Test U1.
2. **Conventional core plus one distant element.** Schema part: O7 / S3. [E] in humans for citation hits (K18), no LLM test. Evidence d01. Test U2.
3. **Embedding displacement and atypicality scores.** Schema part: S7 / S3. [S] K21. Evidence d06, a12, a28. Test U3.
4. **Pairwise incumbent comparison (1D-style) instead of aggregate scoring.** Schema part: S7. [C] K09. Evidence a26, a27, d12. Test U4.
5. **Generalization attempts (unify two solutions).** Schema part: O2. [S] K10. Evidence a20, b20, d06. Test U5.
6. **Method change vs rule change as distinct attempt types.** Schema part: S3 / O6. [S] K11. Evidence a05, a23, b08. Test U6.
7. **Plan-then-retrieve for ideation.** Schema part: O4 / S3. [C] K16. Evidence c21, d07. Test U7.
8. **Cheap prefilter before execution.** Schema part: S4. [S] K20. Evidence d10. Test U8.
9. **LLM theory-vs-method probability as a displacement cue.** Schema part: S3 / S6. [S] K11. Evidence a04, d14. Test U9.
10. **Keep the incumbent after one failed check (delayed credit).** Schema part: S7 / S9. [S]. Evidence a08, a11, a05. Test U10.

Not changed: distant analogues stay at impasse and open mode only (O7 already says so [E]). The atypicality numbers (61% vs 36% in 2022, negative in 2025) do not change that. [C] K02.

## 8. Concrete tests on our bench

All arms get equal tokens. Setup cost counts (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Attempt type | open-mode tasks with a check (ARC variants, BrainTeaser items that failed in direct mode) | A: plain open mode; B: forced half distant-mix and half displace-leader; C: only displace-leader | pass rate of final answer; share of final answers from each type | B or C beats A by a few points where a current best exists; distant-mix alone wins few items but raises spread (matches O7 note) |
| T2 Core plus one distant element | ARC items at impasse | A: standard method; B: standard plus one distant element; C: fully distant | pass rate; distinct-solution count | B >= A > C (extrapolated from Uzzi 9.11 vs 5.82 vs 5.33) |
| T3 Embedding scores | logged attempts from earlier batches | correlate candidate-to-incumbent embedding distance with beating the incumbent under execution | AUC of distance predicting a win | AUC above 0.6 useful; near 0.5 drop (the LLM rater scored 0.42 on a similar task) |
| T4 Pairwise vs aggregate selection | items with several candidate answers | A: current S7 (group size, then shortest); B: add a discriminating test against the single strongest rival | final accuracy | B >= A; headroom small since S7 already scores 34 of 36 |
| T5 Generalization attempts | tasks with two or more partial solutions | A: extend the best partial; B: ask for one rule reproducing both | pass rate on held-out inputs (G3) | B better if generalization tracks correctness |
| T6 Method vs rule change | BrainTeaser and ARC | A: unlabelled attempts; B: attempts forced to change method (same rule) or change rule | which type solves which class | class-specific; log per class in S9 |
| T7 Plan-retrieve vs sampling | open-mode ideation items with execution | A: N samples; B: planned search with retrieval | distinct, executed, passing ideas | B higher distinct count; quality gain uncertain given Heuresis |
| T8 Prefilter | items with costly checks | A: execute all; B: cheap filter then execute | pass rate per token; false-reject rate | B only if false rejects below 10% (AlphaResearch had 28.5%) |
| T9 Theory-vs-method cue | logged attempts | choose operator by LLM theory probability | whether high-theory attempts win at impasse | unknown; validate on 100 labelled pairs first |
| T10 Keep incumbent | items with delayed signals | A: drop after first failed check; B: keep one more round | pass rate | small positive at best |

## 9. What does not transfer, and why

- **Citation graphs.** D needs later papers. An agent has no downstream citers at solve time. Only a proxy (later checks) exists.
- **Journal-pair atypicality.** Needs a co-citation corpus. An embedding of concept pairs replaces it, but r = 0.74 with the z-score shows the proxy is loose (a12).
- **Population base rates.** 38% of papers have D > 0 and 62% have D <= 0 (a09, a06). An agent solving one problem has no such population.
- **The 10-year delay.** Disruption takes about 10 years to show. An agent has seconds. Delayed credit only matters across sessions (S9, memory).
- **Team size.** The team-size debate has no clean agent analogue. Parallel attempts are samples from one model and not independent (G4). Do not map "small teams disrupt" to "few attempts".
- **Prestige rewards (Nobel, Lasker).** Prizes are social outcomes. AUC on prizes says nothing about correctness.
- **LLM novelty edge before execution.** Reviewer ratings at idea stage; they vanish after execution (b24).
- **The sign of the A-D link.** Contested for papers (K02). Do not build a rule on it.
- **Open-mode value in closed tasks.** On routine items, distant analogues lower the average result (O7 note). This literature concerns open-ended science, not ARC-like closed items.
- **Disruption of LLM lineages.** MDI describes the open-source model ecosystem (a29), not one agent's reasoning.

## 10. Open questions

1. Why do the 2022 and 2025 papers have opposite signs for A vs D? Re-run both measures on one corpus (d05).
2. What is the actual A-D coefficient in 2506.15959? No coefficient, window or code (d04).
3. Does the pairwise 1D / displacement measure replicate on patents and independent groups? Papers only so far (d12, d13).
4. Does distant-analogy vs in-topic displacement differ in an LLM agent at equal tokens? No study (d15).
5. Can an embedding or LLM displacement score predict which candidate wins under execution? No study.
6. Does novelty survive execution outside NLP and ML recipes (math, code)? One weak paper (d10).
7. Is generalization detectable in a single agent's attempts, and does it track correctness?
8. Do Uzzi's conventional-plus-novel results hold with LLM-based novelty measures?
9. How do dedup and diversity change with planning vs retrieval at equal budget? Partly answered (d11).
10. Is the Heuresis count 13/300 (appendix) or 20/200 (text)? Unreconciled (d08).
11. Does the Llama theory/method label agree with humans? Not reported (d14). The counts 50,147 vs 52,488 are unreconciled.
12. Is the decline of disruption real once null networks are used? About 85% survives randomization per Huang and Xie, against the artefact camp.

## 11. Sources

[V] = opened this session (full text or page). [M] = snippet, abstract only or second-hand.

- [V] Li, Lin, Wu (2025) Can Recombination Displace Dominant Scientific Ideas? https://arxiv.org/abs/2506.15959 (PDF https://arxiv.org/pdf/2506.15959)
- [V] Lin, Li, Wu (2025) The Disruption Index Measures Displacement Between a Paper and its Most Cited Reference. https://arxiv.org/abs/2504.04677
- [V] Lin, Li, Wu (2025) Team Size and Its Negative Impact on the Disruption Index. https://arxiv.org/abs/2502.00219
- [V] Lin, Evans, Wu (2022) New directions in science emerge from disconnection and discord. https://arxiv.org/abs/2103.03398
- [V] Uzzi, Mukherjee, Stringer, Jones (2013) Atypical combinations and scientific impact. https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf (a13 and b07 were second-hand; d01 opened it)
- [M] Funk, Owen-Smith (2017) A dynamic network measure of technological change. https://doi.org/10.1287/mnsc.2015.2366
- [M] Wu, Wang, Evans (2019) Large teams develop and small teams disrupt science and technology. https://doi.org/10.1038/s41586-019-0941-9
- [M] Park, Leahey, Funk (2023) Papers and patents are becoming less disruptive over time. https://doi.org/10.1038/s41586-022-05543-x
- [V] Holst et al. (2024) Dataset artefacts are the hidden drivers of the declining disruptiveness in science. https://arxiv.org/abs/2402.14583
- [V] Petersen, Arroyave, Pammolli (2023) The disruption index is biased by citation inflation. https://arxiv.org/abs/2306.01949 ; 2024 version https://arxiv.org/abs/2406.15311
- [V] Bentley et al. (2023) Is disruption decreasing, or is it accelerating? https://arxiv.org/abs/2306.14364
- [V] Fang, Evans (2025) Generalization and the rise of system-level creativity in science. https://arxiv.org/abs/2510.03240
- [V] Bornmann, Tekles (2020) Convergent validity of several indicators measuring disruptiveness. https://arxiv.org/abs/2006.10606
- [V] Leibel, Bornmann (2023) What do we know about the disruption index in scientometrics? https://arxiv.org/abs/2308.02383
- [V] Leibel, Bornmann (2024) Specification uncertainty. https://arxiv.org/abs/2406.13367
- [V] Liang, Jiang, Hou (2020) Same data may bring conflict results. https://arxiv.org/abs/2009.06888
- [V] Huang, Xie (2026) Large scientific teams are more, not less, disruptive. https://arxiv.org/abs/2610.07329
- [V] Lin, Yang, Wu (2026) Large teams consistently develop science. https://arxiv.org/abs/2610.27649
- [V] Kim, Kojaku, Ahn (2025) Uncovering simultaneous breakthroughs. https://arxiv.org/abs/2502.16845
- [V] Wei, Kang, Pan, Yang (2026) Identifying disruptive models in the open-source LLM community. https://arxiv.org/abs/2604.11618 (c20 is abstract level)
- [V] James (2025) Measuring the potential of scientific literature. https://arxiv.org/abs/2512.06054
- [V] Larregue, Gingras (2026) The disruption index does not measure scientific innovation. https://arxiv.org/abs/2606.07332
- [V] Rutzer, Filimonovic, Macher, Weder (2026) Towards measuring disruptive innovation. https://arxiv.org/pdf/2603.17881
- [V] Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto, Yang (2025) The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803
- [V] Tracing the Influence of Retrieved Literature on Scientific Ideation in LLMs (2026) https://arxiv.org/pdf/2610.39060
- [V] Antoniades et al. (2026) Heuresis. https://arxiv.org/pdf/2606.25198
- [V] AlphaResearch (2025) https://arxiv.org/pdf/2511.08522
- [M] Gupta, Pruthi (2025) All That Glitters is Not Novel. https://arxiv.org/abs/2502.16487
- [M] RQ-Bench (2026) On the limits of LLM-as-judge for scientific novelty. https://arxiv.org/abs/2606.12071
- [M] Are We Truly Innovating? Originality in AI Research Papers (2026) https://arxiv.org/abs/2602.06054
- [M] SchNovel (2024) https://arxiv.org/abs/2409.16605
- [M] NovBench (2026) https://arxiv.org/abs/2604.11543
- [M] Automated Novelty Evaluation of Academic Paper (2025) https://arxiv.org/abs/2507.11330
- [M] Huang (2026) Catalyst Papers in AI Research. https://arxiv.org/abs/2607.05401
- [M] Semantic Geometry for Uncovering Paradigm Dynamics (2026) https://arxiv.org/abs/2604.15150
- [M] Wang (2024) A Content-Based Novelty Measure. https://arxiv.org/abs/2401.03642
- [M] Li, Lin, Wu (2024) Displacing Science (withdrawn). https://arxiv.org/abs/2402.16839
- [M] Nova (2024) Iterative Planning and Search. https://arxiv.org/abs/2410.14255
- [M] Multi-agent AI systems outperform human teams in creativity (2026) https://arxiv.org/abs/2605.17885
- [M] Cooking Up Creativity (2025) https://arxiv.org/abs/2504.20643
- [M] Enhancing Research Idea Generation through Combinatorial Innovation (2026) https://arxiv.org/abs/2604.20548

Note: several 2026 arXiv records (c13, c14, c16, c17, c19, c21, c24) were read at abstract level only. Treat their numbers as [M] even where the evidence file sets opened:true.
