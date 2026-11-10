# B01.07 Semantic memory network structure: cross-check and critique

## Method
Re-opened cached full texts (PMC and arXiv, saved earlier under D:/research_scratch/B01.07/) and grepped the numbers behind the ten most important lines. Checked: Kenett 2014 (PMC4051268), Benedek and Neubauer 2013 (PMC3924568), Luchini 2025 (PMC12214691), Skurnik and Kenett 2026 (PMC13027982), Ovando-Tellez 2022 (PMC8816337), Chen and Ding 2023 (arXiv 2310.11158), Abramski 2024 (arXiv 2412.01330), Bellemare-Pepin 2024 (arXiv 2405.13012), Domanti 2026 (dom.html).

## Confirmed
- Kenett 2014: N=139 (47 men, 92 women); ASPL 4.6 vs 3.93; diameter 12 vs 8; Q 0.62 vs 0.58; S 6.86 vs 7.76; CC 0.67 vs 0.66; mean degree 5.88 both. First-10 control: modularity is lower for LSC-10, so it reverses.
- Benedek and Neubauer 2013: ranking x group F(9,882)=0.98 ns; slope b=-.052, t(98)=-0.28; strength 69.5% falling to 21.7%.
- Luchini 2025: r=.33 and .38; day 1 M=19.64, day 2 M=16.34, t(141)=7.51, d=0.31.
- Skurnik and Kenett 2026: N=236, r=.15 (fluency with objective originality).
- Ovando-Tellez 2022: weighted ASPL vs C-Act .276 (p=.007); weighted Q vs C-Ach -.295 (p=.004). Weighted CC with C-Ach .201 (p=.052) is not significant.
- Chen and Ding: GPT-4 89.1, above 96.1% of humans; GPT-3.5-turbo 80.8.
- Bellemare-Pepin: microscope 70%, elephant 60%, car 1.4%, dog 1.2%, tree 1.0%.
- Domanti 2026: ASPL 4.378 vs 3.429 vs 3.325; d 2.32, 2.55, 0.42; percolation GPT 77.9, LCH 85.2; partial eta2 .84.

## Corrections and cautions
1. b13 (Abramski) gives "average degree 26.1, 19.6, 28.1, 8.3" as if for the full networks. Those are the REDUCED networks (Table 2). Full networks are 20.0, 19.9, 14.6, 8.8 (c18). Use the reduced ones only when stated.
2. Domanti ASPL/CC/Q tests use bootstrap of 50% of nodes, df=1998. Significance is inflated; only the effect sizes mean anything. The human gap (d=0.42, 0.41, 0.20) is small and the GPT gap is large because it is a single model with one prompt, not many models.
3. Benedek N is about 100 (df 98) and Luchini N about 142 (df 141); "about" stays.
4. a03 and b02 give LSC 56% negative impact nodes vs 44% positive: consistent, not a conflict.
5. Kenett 2014 reports no standardized effect size. "Small effect" in the brief is the user's wording; the paper gives only group-level differences with bootstrap tests. The 2018 PNAS data are the same 66 people (not a replication). Not re-opened this pass (PNAS blocked): percolation integral values (14.76 vs 15.64) stay as recorded from earlier reading.
6. Olson 2021 numbers (r=.50 vs .32, .13 in N=8,572) were not re-opened (PNAS blocked this pass); treat as read earlier, one source.

## Contradictions between sources
- Group-level (Kenett 2014: clear gaps) vs individual-level (N=106, 236, 479: weak, sign-mixed). The authors themselves say group networks cannot describe individuals (b23).
- Mednick's steep gradient claim: Benedek 2013 refutes the slope part, Kenett 2014 supports a structure part. Both can hold if access, not hierarchy, differs.
- DAT: GPT-4 greedy 89.1 (Chen and Ding) vs 85.6 at temperature 1.5 (Bellemare-Pepin); scoring set-ups differ, do not compare across papers.
- LLM networks: one study says GPT-4o network is more rigid and still more original than low-creative humans (Domanti), another that sampling raises DAT only for weaker models. Together: network shape of the model is not the lever.
- PACE (a12) and CDAT (a13) disagree on how much DAT-type distance means.

## Weak spots
- Almost all human evidence for the structure claim is cross-sectional, with small effects and many metrics (garden of forking paths). No preregistered replication of the 2014 group result exists in our evidence.
- No study here manipulates seed distance on an LLM agent and measures downstream solution quality. Everything on LLMs is output distance (DAT), not use of seeds in problem solving.
- Distance measures novelty, not usefulness; several LLM results show distance without fit.
- Embedding choice changes results (GloVe .529 vs MUSE .757 in PACE).

## Only seen in snippets or abstracts
a13 (Nakajima 2026), a14 (Vintar 2025), a15 (Beaty 2023 review), a16 (forward flow), a17 (Kenett and Faust 2019), a26, a27, b11 (Wang 2025, secondhand), c24, c25, c26. a12 PACE has no named authors in our record. Claims resting only on these are marked single-source.

## GAPS
1. Does choosing seed concepts at controlled graph or embedding distance (O7/S3) raise solution originality AND correctness for an LLM at equal tokens? No study tests this directly.
2. Is the benefit of far seeds caused by distance itself or by simply adding more varied seeds (fluency confound; first-10 control in Kenett 2014 removed only part of it)?
3. Is there a preregistered or independent replication of the group-level 2014 result (shorter paths, smaller diameter) with more than 33 per group?
4. What distance is best? Is there an inverted-U (too far gives irrelevance)? Look for dose-response of seed distance vs usefulness in humans and LLMs.
5. Which distance metric should the agent use (GloVe, fastText, LLM embeddings, forced-choice relatedness)? PACE shows large differences; LLM free association is a noisy readout (RSA .14).
6. Can exclusion lists or persona seeding raise cross-run diversity at equal tokens without lowering task accuracy (microscope/elephant repetition, hivemind)?
7. Does cluster-then-switch seed ordering (Communications Biology 2022) help an LLM more than random order?
8. Are the rising-homogeneity results (68 models, cosine 0.50 to under 0.40) true for the model our agent will run on, and does the scaffold reverse them?
9. Open: Kenett 2014 original PNAS percolation and Olson 2021 numbers to be re-opened from a source that is not blocked.


## Gap search results

Evidence is in evidence_d.jsonl (d01-d20). Claims K26-K33 added; K01 moved to contested, K10 to established; K04, K08, K16, K21 gained evidence.

1. **Seed distance for an LLM at equal tokens: partly closed, still open.** Liu et al. 2026 (d01-d03) give the closest test: only o3 and Claude-Sonnet-4 gained from a far source, and only when it was remote (top 50% beta=.12, top 10% beta=.24; all pairs beta=.02). It is a product-design task with post-hoc distance cuts, not a randomised seed manipulation, no token matching, no correctness measure. Nothing tests O7/S3 on solution correctness.
2. **Distance versus plain variety (fluency confound): partly closed.** Chan 2017 (d04, d05): fluency equal across groups (F(4,239)=0.5), and always-far did not raise novelty (0.64 vs 0.88 with none). So extra count is not what drives gains, and far seeds alone do not either. Human study, other people's ideas as stimuli, not LLM.
3. **Independent or preregistered replication of the 2014 group result: still open.** Found only same-lab or abstract-level items: percolation re-analysis on the same 66 people (d07), Bernard 2019 (d19), Benedek 2017 (d18, method dependent), Luchini 2023 N=477 for convergent thinking (d17, abstract only). Robinson 2024 (d06) shows global path length is not reliable within a person. Verdict: direction repeated, exact result not independently replicated.
4. **Best distance, inverted U: still open.** Liu 2026 rises monotonically to the tested top decile (d03); Chan 2017 says far is harmful when the person is productive (d04). The upper limit was never sampled. The originality-feasibility trade-off (r=-.74, d02) makes an inverted U for usefulness likely but untested.
5. **Which metric: partly closed.** Distance validity is modest and replicates (Olson 2021, r about .3 unscreened, d08). Swapping GloVe for LLM embeddings keeps r=.65 agreement but slightly lowers validity (d09). Global graph metrics are unreliable per person while local pairwise relatedness is reliable (d06). Ensembles (SemDis, d10) and trained judges (Ocsai, up to r=.81, d11) are snippet-level only. Recommendation: pairwise relatedness from one calibrated embedding, judge for scoring.
6. **Exclusion lists and persona seeding at equal tokens: partly closed.** Verbalized sampling (d12, d13) and anchorless diversification with token accounting (d14) show cheap diversity gains (0.04 to 0.06 at 1.1x tokens; direction planning best per token). Quality is proxies and human win-rates; no correctness task, and exclusion lists themselves were not tested.
7. **Cluster-then-switch order: still open.** Nath 2024 (d15) is observational (flexible LLMs score higher originality). No intervention found.
8. **Homogeneity for our model and scaffold reversal: still open.** The 68-model paper was re-read (d20): defaults only, no scaffold arm.
9. **Percolation and Olson numbers: closed.** Percolation integral 14.76 vs 15.64, n=33 per group (d07). Olson Study 1A N=141 r=.50 screened vs .32 full, Study 1B N=285 r=.32, retest .73 (d08). Original PNAS 2014 text was not needed: the 2018 PNAS paper gives the group sizes.

Remaining caveats: d10, d11, d17, d18, d19 are not opened (snippet or abstract page). d09 table text was garbled in extraction. d04 table order was inferred from the text. New evidence also uses far-future model names as printed in the papers (e.g. GPT-5.4), taken at face value.
