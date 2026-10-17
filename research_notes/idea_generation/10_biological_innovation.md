# 10. How biological evolution generates novelty, read as a theory of idea generation

Compiled 2026-10-13 for the HTSA / nano pipeline. Bracketed numbers refer to the Sources list. Evidence labels: **M** measured (organisms, in-vitro evolution, or LLM-agent runs with ablations); **S** simulation or model only; **R** review or theory; **A** analogy, nothing measured in the target domain. Treat every arXiv item as a preprint (peer-review status not checked) unless stated. The web-search quota ran out during the last passes: no controlled study of "exaptation prompts" in LLM ideation was found, no Wagner paper from 2024-26 could be located, and developmental bias is covered only through map-bias theory [21]-[23] and facilitated variation [18]. Absence claims below are therefore weak.

## 1. Bottom line

1. The best-supported lesson is narrow: **what a search finds first is set by the genotype-to-phenotype map, not by fitness.** Selection (our verifier) only chooses among what the map makes reachable. Frequent phenotypes arrive first and can fix even when fitter, rarer ones are reachable (S) [21]; maps are biased toward simple outputs, including in neural networks (R, with network experiments) [22][23]. Treating an LLM proposer as such a map is an analogy (A), but its bias is measured: 4,000 seeded ideas per topic left about 200 non-duplicates (M) [29].
2. Wagner's "robustness enables innovation" is model-supported (RNA, regulatory circuits, metabolism) [1][2], partly experimental [4][5], and **conditional**: robustness can help or hinder depending on population size, mutation rate and landscape [3].
3. The best measured biological mechanisms are potentiation [8][9], recombination [24], and duplication with specialisation, which has a low base rate [15][17]. Exaptation "potential" is common in models [13][14]; how often it drove real innovation is unmeasured.
4. In LLM search the nearest measured analogues are stepping-stone archives, parent choice by descendants, novelty rejection and stall-triggered breadth [30][31][32][36]. Counter-evidence: solution diversity did not predict success, and flat best-of-M matched iterated search [36][37]. Breadth must be gated and measured, not assumed.

## 2. Mechanisms: what was shown, and what is metaphor

| Mechanism | What was actually shown | Label |
|---|---|---|
| Genotype / neutral networks, robustness | Genotypes sharing a phenotype form one connected graph; search along it reaches genotypes as different as random ones while staying viable; robustness may slow short-term innovation but long-term innovation needs it [1]. RNA: sequence robustness opposes evolvability, phenotype robustness promotes it [2]. Helps or hinders by population size, mutation rate, landscape [3]. RNA enzymes carrying cryptic variation adapted faster to a new substrate [4]. In a ribozyme, 60% of the 65,536 variants between two active genotypes were neutral, but other families may lack such networks [5]. Evolvability can itself evolve [6]. Lay account: metabolic genotypes drift to 20-25% shared composition with the same phenotype [7]. | S core; M [4][5]; conditional |
| Potentiation, stepping stones | Replays of an E. coli population showed a potentiating mutation (by about generation 20,000) raised the later rate of a key innovation without hypermutation [8]. Three lineages coexisted over 10,000 generations; the trait arose through a duplication that put a silent transporter under a new promoter [9]. Permissive substitutions for a function switch were extremely rare [10]. In digital organisms some deleterious mutations were stepping stones [11]. | M [8]-[10]; S [11] |
| Exaptation | Defined as features that enhance fitness but were not built by selection for the current role [12]. In 500 model E. coli metabolisms kept viable on glucose, 96% also grew on other carbon sources (about 5 of 49 tested), not explained by chemical proximity [13]; about 95% of glucose-viable variants of a 51-reaction core also grew on another of ten sources [14]. Shows potential, not history. | S |
| Duplication and divergence | Duplicates arise near 0.01 per gene per million years; most are silenced within a few million years; new functions are rare [15]; there is no consensus on how duplicates are fixed and kept [16]. In Salmonella a weakly bifunctional gene was amplified, copies specialised, worse copies were lost, in under 3,000 generations [17]. | M, low base rate |
| Modularity, facilitated variation | Conserved core components plus weak regulatory linkage make viable variation cheap and reduce lethality [18]. Selecting for low connection cost produced more modular, more evolvable networks [19]. | R; S |
| Environmental change | Goals that change while reusing subproblems sped evolution dramatically in some simulations, more so for harder problems [20]. Variation hidden in the old environment sped adaptation to a new one in RNA enzymes [4]. | S; M [4] |
| Developmental bias, map bias ("arrival of the frequent") | Discovery time scales as the inverse of phenotype frequency [21]; simple outputs dominate [22][23]. | S/R |
| Recombination, horizontal transfer | DNA shuffling gave a 32,000-fold gain versus 16-fold for error-prone PCR [24]; horizontal transfer is established in prokaryotes and beyond [25]. Biological and technological innovation share nine features, including horizontal information transfer [26] (A). | M [24]; R |
| Neutral variants in code | Over 30% of random mutations to 22 programs left test-suite behaviour unchanged ("neutral" means passes tests) [27]. | M |

**Metaphor, not mechanism:** "ideas have a genotype network" (nobody has measured connectivity of idea space); "robustness enables innovation in idea loops" (no test found); "exaptation prompts" (no test found); "environment shifts trigger innovation" (simulation [20], RNA enzymes [4] and one LLM case [39] only).

## 3. The 2024-2026 bridge to LLM search

- **LLM mutation is not free neutral drift** (preprint, GECCO'26 workshop; one DSL, genotype-only). With no selection, 87% of chains had over 93% of mutations revisiting a seen structure; 300-step chains ranged from under 10 to over 250 unique programs depending on prompt wording, versus about 270 for subtree GP [28].
- **Stepping stones work in agents.** SWE-bench: 50.0% full Darwin Goedel Machine, 39.7% greedy parent choice, 23.0% always-build-on-latest; some paths pass through worse-than-parent nodes [30]. Parent score is a poor guide to descendants' success (abstract-level) [31].
- **Parent choice and novelty.** Weighted parent sampling beat hill climbing, which plateaus; embedding novelty rejection (cosine 0.95) gave "substantial" gains, an LLM judge only marginal; no islands ablation; ablations on a handful of small tasks [32]. AlphaEvolve: every component mattered, no effect sizes in text [33]. AdaEvolve moves budget to productive populations and generates new tactics when progress stalls (abstract-level, 185 problems) [44]. Promptbreeder also evolves the mutation prompts, the nearest thing to evolving evolvability [6] in prompts (abstract-level) [43].
- **ML-recipe agents.** Five-minute GPT-2 runs, no seed count or variance reported: population plus "semantic crossover" reached 0.97658 bpb versus 0.98232 for single-incumbent hill climbing, which gained nothing in its last two quarters [34]. Specialist agents (1,197 trials) "combine and transfer known techniques"; in a 200-trial ablation, lineage sharing mattered most (1.0731 versus 1.0774 bpb without it) [35]. In 324 runs greedy (0.192) matched tree search (0.193), uniqueness correlated at rho 0.012, and the authors' greedy-then-branch-on-stall variant scored highest (0.208, preliminary) [36]. Flat best-of-M matched or beat iterated search on NanoGPT speedruns; no-hint agents recovered under 20% of human speed-ups [37].
- **Environment and noise.** Co-evolving opponents produced more general programs and less diverse runs [39]. In an image-evolution replication, selection noise 0.25 helped, 0.5 and above hurt; one-step history was best; 100 persona agents raised tree balance from 0.235 to 0.473 [38].
- **ML operators for neutral moves and duplication.** Function-preserving growth starts the larger network at the same function, then noise breaks symmetry [40]. Upcycling copies the dense MLP into identical experts that then diverge [41]. LLM crossover works as a variation operator on bit-strings, sentences, equations, image prompts and Python (abstract-level, no numbers read) [42].

## 4. What would transfer to an LLM-driven idea loop

Common protocol: matched GPU-minutes and tokens; at least 3 search seeds per arm; existing ladder and verdict (Welch p<0.01, 0.005-nat margin, 3+ seeds); control `--arm climb`; report verified wins per 100 GPU-min, rounds to first win, distinct clusters per win. Gate every breadth mechanism on a stall (no verified win in N builds) [36]. Power warning: the whole-population gain in the closest ML-recipe study was 0.0057 bpb [34], about the size of our 0.005-nat verdict margin (units differ), so differences between loop variants will likely sit at or below that margin; compare arms on wins per GPU-minute and rounds to first win, not only final loss, and plan 5 or more search seeds per arm. Already in `nano/`: item 5 (`boundary.py`, `compose.py`), docs-card imports, cluster-coverage selection. New: the rest. Best evidence: 8, 9, 7. Cheapest to test: 9 (no GPU) and 2. Pure biological hypotheses with no LLM-loop evidence: 1, 3, 4, 6.

1. **Plateau archive (neutral variants kept alive).** Basis: S/M [1][3][5]; LLM evidence none. File every valid candidate within noise of the incumbent (|z|<1 at matched steps, which includes `close_call`) in `plateau/`; draw about 20% of parents there; apply a neutral-by-construction edit (zero-init branch, identity layer, replicate-and-halve widening [40]) before one real change; reject cosine 0.95 or closer to the archive [32], else drift collapses [28]. Expect more distinct one-step neighbours, useful late, not early. Measure: neutral share of proposals (code baseline above 30% [27]); distinct masked-AST skeletons per 100 proposals; wins per 100 GPU-min versus climb.
2. **Stabiliser pairing (potentiation).** Basis: M [8][10]. Tag plateau members that change only stability (QK-norm, z-loss, clipping); pair each with ideas that failed by divergence at high LR, depth or width. Expect rescues no single-idea ranking can see. Measure: rescue rate versus pairing with random plateau members.
3. **Duplicate-and-diverge with a grace window.** Basis: M [15][17]; ML analogue [41]. When a module verifies or is `promising`, fork two identical copies into different roles (other layers, parameter group, scale) and judge them leniently for G rounds, then strictly; cap at a small share of builds (my parameter, say 15%) because most duplicates die [15]. Expect low hit rate, high gain when it works. Measure: copy survival curve; best-copy gain over parent in z; yield per GPU-min versus fresh ideas.
4. **Exaptation card.** Basis: S [13][14] plus concept [12]; LLM untested. For each pooled component, including failed-but-sound ones, a blind agent lists at least 3 other roles (stability, speed, data efficiency, eval time); keep a component-by-role table; build the cheapest. Expect cheaper builds and unexpected wins. Measure: hit rate and build-pass rate versus seeded cards at matched tokens; share of changed lines already in the pool.
5. **Module boundaries with weak linkage.** Basis: R/S [18][19]. Keep the conserved core (exam, loader), mutate one module per proposal (`boundary.py`), add on/off flags, compose disjoint winners (`compose.py`). Expect higher build-pass rate and predictable composition. Measure: rung 0-3 pass rate scoped versus unscoped; epistasis z(A+B)-z(A)-z(B); composition success for disjoint versus overlapping pairs.
6. **Environment-shift rounds.** Basis: S [20], M [4], LLM [39]. On a stall, change one variable (tokens 50M to 100M, data mixture, width, sequence length), re-rank archive and plateau there, run the next round there, re-verify in the original; this also releases latent candidates [4]. Expect escape from local optima and removal of scale-fragile ideas; size unknown. Measure: rounds to target versus fixed environment; rank correlation of z across environments; archive members whose rank rises.
7. **Recombination with pair diversity and back-crossing.** Basis: M [24]; LLM [34][42]. Semantic crossover (parent A plus one validated idea of B) with a no-repeat-pair rule; shuffle several compatible winners, then back-cross to the baseline to drop non-essential changes [24]; tag outside imports by source. Expect composite gain below the sum of parts (my assumption; test it). Measure: composite gain versus additive; promotion rate by distinct pairs (GEAR case study, not a controlled test: one pair repeated 28 of 29 times gave 14% elites; 33-35 distinct pairs gave 71-72% [34]); share of composite changes removable without loss.
8. **Parent choice by descendants.** Basis: M [8][9][11]; LLM M [30][31][32]. Lineage score is the best or mean z of a node's descendants (the clade idea of [31]); sample parents with weight lineage score times 1/(1+children), the second factor taken from [32]; admit worse-than-parent nodes that sit in a new cluster. Expect fewer early plateaus (greedy 39.7% versus 50.0% on SWE-bench [30]). Measure: share of final winners with a worse-than-parent ancestor; rounds to plateau; greedy versus lineage sampling at matched tokens.
9. **Proposal-map audit.** Basis: S [21][22]; LLM M [28][29]. Before spending GPU, run no-selection mutation chains (100 steps, my choice; [28] used 300) per card and prompt; count unique skeletons; retire attractor cards; vary persona, model and temperature [28][38]. Expect more distinct clusters per token. Measure: unique skeletons per 100 proposals; duplicate rate; tokens per distinct cluster; win rate per card.

## Sources

[1] Ciliberti, Martin, Wagner 2007, PNAS. https://doi.org/10.1073/pnas.0705396104
[2] Wagner 2008, Robustness and evolvability: a paradox resolved. https://doi.org/10.1098/rspb.2007.1137
[3] Draghi et al. 2010, Nature. https://doi.org/10.1038/nature08694
[4] Hayden, Ferrada, Wagner 2011, Nature. https://doi.org/10.1038/nature10083
[5] Rotrattanadumrong, Yokobayashi 2022, ribozyme neutral network. https://pmc.ncbi.nlm.nih.gov/articles/PMC9385714/
[6] Payne, Wagner 2019, causes of evolvability. https://doi.org/10.1038/s41576-018-0069-z
[7] Review of Wagner, Arrival of the Fittest (secondary). https://pandasthumb.org/archives/2014/11/andreas-wagner.html
[8] Blount, Borland, Lenski 2008, PNAS. https://doi.org/10.1073/pnas.0803151105
[9] Blount et al. 2012, Nature. https://doi.org/10.1038/nature11514
[10] Harms, Thornton 2014, Nature. https://doi.org/10.1038/nature13410
[11] Lenski et al. 2003, Nature. https://doi.org/10.1038/nature01568
[12] Gould, Vrba 1982, Paleobiology. https://doi.org/10.1017/S0094837300004310
[13] Barve, Wagner 2013 as reported by Quanta (paper paywalled). https://www.quantamagazine.org/evolutionary-modeling-study-provides-new-evidence-for-exaptation-20130904/
[14] Hosseini, Wagner 2016, BMC Syst Biol. https://pmc.ncbi.nlm.nih.gov/articles/PMC5073748
[15] Lynch, Conery 2000, Science. https://doi.org/10.1126/science.290.5494.1151
[16] Innan, Kondrashov 2010, Nat Rev Genet. https://doi.org/10.1038/nrg2689
[17] Nasvall et al. 2012, Science. https://doi.org/10.1126/science.1226521
[18] Gerhart, Kirschner 2007, PNAS. https://doi.org/10.1073/pnas.0701035104
[19] Clune, Mouret, Lipson 2013. https://doi.org/10.1098/rspb.2012.2863
[20] Kashtan, Noor, Alon 2007, PNAS. https://doi.org/10.1073/pnas.0611630104
[21] Schaper, Louis 2014, PLoS ONE. https://doi.org/10.1371/journal.pone.0086635
[22] Dingle, Camargo, Louis 2018, Nat Commun. https://doi.org/10.1038/s41467-018-03101-6
[23] Valle-Perez, Camargo, Louis 2018. https://arxiv.org/abs/1805.08522
[24] Stemmer 1994, DNA shuffling. https://doi.org/10.1038/370389a0
[25] Soucy, Huang, Gogarten 2015. https://doi.org/10.1038/nrg3962
[26] Wagner, Rosen 2014, J R Soc Interface. https://doi.org/10.1098/rsif.2013.1190
[27] Schulte et al., Software mutational robustness. https://arxiv.org/abs/1204.4224
[28] Gurkan, Stonedahl, Wilensky 2026, Mutation Without Variation. https://arxiv.org/abs/2606.05408
[29] Si, Yang, Hashimoto 2024, Can LLMs generate novel research ideas. https://arxiv.org/abs/2409.04109
[30] Darwin Godel Machine 2025. https://arxiv.org/abs/2505.22954
[31] Huxley-Godel Machine 2025. https://arxiv.org/abs/2510.21614
[32] ShinkaEvolve 2025. https://arxiv.org/abs/2509.19349
[33] AlphaEvolve 2025. https://arxiv.org/abs/2506.13131
[34] GEAR, Genetic AutoResearch 2026 (preprint). https://arxiv.org/abs/2605.13874
[35] Auto Research with Specialist Agents 2026 (preprint). https://arxiv.org/abs/2605.05724
[36] FML-bench 2026 (preprint). https://arxiv.org/abs/2605.17373
[37] Automated LLM Speedrunning Benchmark 2025. https://arxiv.org/abs/2506.22419
[38] Replicating Picbreeder with vision-language models 2026. https://arxiv.org/abs/2605.23908
[39] Digital Red Queen 2026. https://arxiv.org/abs/2601.03335
[40] Net2Net 2015. https://arxiv.org/abs/1511.05641
[41] Sparse Upcycling 2022. https://arxiv.org/abs/2212.05055
[42] Language Model Crossover 2023. https://arxiv.org/abs/2302.12170
[43] Promptbreeder 2023. https://arxiv.org/abs/2309.16797
[44] AdaEvolve 2026. https://arxiv.org/abs/2602.20133
