# 07. Anomalies, serendipity and problem finding: engineering noticing in the loop (2026-10-13)

Evidence labels as in 05: **H** large controlled or independently replicated; **M** peer-reviewed or documented, single study or small n; **L** self-report, preprint, case study or press. "(inference)" marks my reasoning. [L1], [L4], [L5] are local files. Not repeated: Peirce, Platt, Lakatos, Dunbar's analogy counts (05); QK-norm, gating, mHC origins (12); loop ideas already planned (00_IDEAS #26-29, 02 #5-7), which section 2 extends.

## Bottom line

1. **Surprise is common and mostly artifact; conversion is the scarce step.** Dunbar's coded meetings held 18 unexpected, 22 expected and 30 exploratory findings [1]; a press account says over 50% of data was unexpected, often explained away or forgotten in a notebook [2]. Only 8.3% of 205 Citation Classics commentaries [5] and 5.8% of 1,437 marketed drugs [6] report serendipity. Inference: serendipity is a minority route, so anomaly-seeded ideation is a lane, not the main line.
2. **What converted surprises:** a prior expectation (Merton's "unanticipated"), surprise on a core assumption, a narrowed question, an analogy from a colleague's experiments, and elimination of artifact explanations until a residual survived: Penzias and Wilson's 3.5 K outlasted helium cooling, interference removal and cleared pigeon nests; Bell's pulsar "scruff" came from hand-inspecting chart output [1][4][41][42].
3. **Observers protect the incumbent; LLM agents more so.** Incongruous cards needed 4x the exposure [8]; six of seven responses to anomalies preserve the core theory [9]; a familiar solution cut chess experts to players 3 SD weaker while their eyes stayed on it as they believed they searched [23][24]; agents ignored evidence in 68% of 25,000+ runs and revised after refutation in 26% [32].
4. **Structure beats exhortation.** ReASearch inserts a stagnation advisory after 3 and 7 flat evaluations; diagnosing and relaxing a binding constraint ended one 120-turn plateau [34]. Yet the base model explained 41.4% of variance and the scaffold 1.5% in [32], so measure any scaffold.
5. **Raw prediction error is a trap; progress and replication are filters.** Error-driven curiosity seeks irreducible entropy (noisy TV) [21]; reward progress [19][20] or Bayesian surprise [17][18].
6. **For the loop:** nine mechanisms (section 2) turn diagnostics, failed builds, contradictions and prediction misses into anchored long shots, tested on planted pathologies and matched anomaly-seeded vs control arms. Expected (inference): modest gains, concentrated in plateau exits.

## 1. Evidence by topic

- **Dunbar, in vivo (M; press L).** One meeting turned a surprise (both B-cell types entered heart and joints) into conceptual change. The director narrowed the question to what the two types shared that let them in, a postdoc drew an analogy to a colleague's experiments (methylation), others chained inductions and deductions, and one mechanism became two [1]. Scientists analysing data gave anomalies more immediate and lasting attention than expected phenomena (n=3) [3]. *Failure:* most surprises are method errors (inference), yet even recurring anomalies were often dropped [2].
- **Merton and Barber (L; counts M).** The pattern is an "unanticipated, anomalous and strategic datum"; chance favours "prepared minds" (Pasteur); fertile settings are "serendipitous sociocognitive microenvironments"; van Andel: serendipity cannot be programmed, but a system can alert and incite abduction [4]. Counts: 17 of 205 [5]; 84 of 1,437 drugs (24.1% with derivatives), 31 of 88 anticancer drugs [6]. *Failure:* "strategic" is assigned after success (survivorship); sought findings reached by accident are pseudo-serendipity.
- **Kuhn (L-M).** Discoveries follow anomalies; normal science ignores or explains them away; only accumulated troublesome ones cause crisis; "only" is contested (double helix) [7]. Bruner and Postman (n=28): 28 ms normal vs 114 ms incongruous cards; threshold 84 ms after two or three incongruous cards vs 360-420 ms after none or normal ones [8]. Chinn and Brewer's responses: ignore, reject, exclude, abeyance, reinterpret, reinterpret with peripheral change, change theory [9]. *Failure:* every theory carries anomalies (inference); revolting at each is as bad as ignoring all. Platt (L): see 05 (the "bad lot" problem).
- **Adjacent possible (M).** An urn where each novel draw adds ν+1 new elements (reinforcement ρ) gives Heaps exponent ν/ρ and fits words, songs, Wikipedia edits and tags (β 0.45-0.78) [10]. Component usefulness shifts as others are acquired: greedy leads early (2x recipes, 10x software), far-sighted wins later [11]. *Failure:* statistical, not causal; adjacency is the graph you assume. Inference: in a one-day run, mostly greedy plus a small far-sighted reserve.
- **Problem finding (M-L).** Art students who handled more objects and kept the problem open longer drew more original work (Getzels) [12]; problem-construction ability predicted solution quality and originality (Reiter-Palmon, Mumford, Runco et al.; 195 students, six problems), especially with inconsistent cues [13]; a dissertation snippet reports meta-analytic r=.22 (k=40), unopened [14]. *Failure:* proxies are crude and effects modest (inference).
- **Question quality (M).** People write varied but rarely best questions yet prefer the best when shown them [15]; LLM questions chosen by simulated information gain raised success 38.1% on average over direct prompting [16]. I found no controlled link from question quality to creative output beyond problem construction. *Failure:* needs an explicit hypothesis space; simulated scenarios inherit the model's priors.
- **Surprise and progress (M).** Bayesian surprise (KL, prior to posterior) drew 72% of gaze shifts to above-average locations [17]; AUC about 0.7 vs 0.8 between observers, 0.5 chance, falling roughly as 1/N once a regularity is learned [18]. Compression progress is "the steepness of the learning curve" [19]; reward the decrease of prediction error within comparable situations [20]; adults' choices tracked learning progress (n=382) [22]. *Failure:* raw error seeks maximum-entropy transitions; a noisy TV slows learning drastically [21]; surprise is not correctness (05).
- **Einstellung (M).** With a familiar mate available, International Masters found the shorter line 50%, Masters 18%, Candidate Masters 0%; all found it when the familiar line was disabled; 12 experts had predicted 86/74/59% [23]. Gaze stayed on the familiar line while players said they sought alternatives [24]. LLMs too: red herrings fixate models [26]; 17 LLMs showed severe bias-trap rates [25]. *Failure:* forced switching wastes budget (inference); top experts resisted.
- **Negative capability (L-M).** Keats: "capable of being in uncertainties, mysteries, doubts, without any irritable reaching after fact and reason" [27]. High need-for-closure groups were less fluent, elaborate and creative [28]; paradoxical frames raised creativity in four lab studies [29], in teams only with epistemic motivation (n=950) [30]; Janusian thinking in Nobel laureates is interview-based [31]. *Failure:* tolerance becomes anomaly hoarding (05).
- **LLM agents 2024-26 (L-M, mostly preprints).** Evidence ignored 68%, refutation-driven revision 26%, unchanged given successful trajectories [32]. Ding and Li, as summarised in [33]: models extend known results but miss anomalies demanding abandonment. ReASearch (14 tasks, +2% to +40%): a plateau near 0.21 for 120+ turns ended when a "donor" constraint was temporarily relaxed; "an agent on a plateau is unlikely to realize that it should call a diagnostic tool"; it traced an EMA failure to batch-norm statistics [34]. AIRA_2 names fixed single-turn operators a ceiling [35]. A constraint-model reformulation agent won 21 of 27 instances (an AI review questions objective equivalence) [36]. A model trained on failed reactions beat chemists, 89% vs 78% (press numbers) [37]. AutoDiscovery: see 05. No controlled test of anomaly-seeded vs prior-seeded ideation found. *Failure:* reformulation can change the problem.
- **ML precedents (M, survivorship).** ViT registers (high-norm background tokens) [38], LLM.int8 (systematic outlier features) [39] and sigma-Reparam (attention-entropy collapse with instability) [40] each began as a measured internal pathology.

## 2. Engineering noticing in the loop

Today `diagnose.py` measures nine cells on one seed at 100 steps and prints plain statements; `fidelity` checks whether a sketch's named cell moved; `predict.py` scores outcome claims; a long-shot lane exists [L4]. Missing: noise models on cells, recorded expectations, mismatches used as seeds, mined failures and contradictions.

**N1. Residual map with a null.** Compute: instrumented baseline on 3 seeds; smooth expectations (loss vs log frequency rank and log position, layer trends, per-head spread of entropy and first-token mass); residuals in seed-SD units; Benjamini-Hochberg across the dozens of per-layer and per-bucket cells; one sign on all seeds. Show: top 5 with concrete rows (layer, head, token band), not the table. Ask: one-sentence restatement, three rival causes including an artifact, a 5-minute probe on a saved checkpoint. Basis: [38]-[40], [17][18], [1]. Measure: false flags per table on untouched copies (aim at most 1); recall on planted pathologies; seed-robust wins per 10 builds and new-cluster share, residual-seeded vs plain-table sketches.

**N2. Predict-then-reveal on diagnostics.** Before the table, each context states direction and rough size for 6-8 cells. Surprise = miss in SD units; a cell family earns follow-up only while misses replicate and the team's miss shrinks across rounds; chronic irreproducible misses are tagged noisy-TV. Basis: [4], [17], [19][20]; agents otherwise ignore evidence [32][34]. Measure: coverage of stated ranges rising (learning progress); share of surprises that change a belief. Extends 02 #5 from outcome misses to diagnostic misses.

**N3. Mechanism-outcome matrix per checked build** (uses `fidelity`). Cross "named cell moved as stated" with "verdict improved". Moved, no gain: that cell does not bind; log a falsified assumption. Gain, no move: the Merton pattern; diff all cells, show the three biggest movers, ask "what did this accidentally do; design the intentional version", replicate on a second seed. Neither: check the intervention first. Basis: [4]; 8 of 10 inconsistent surprises produced hypotheses, and a missing QK-norm scale was found in autoresearch [L1]. Measure: follow-up win rate from off-diagonal vs diagonal builds; drop if ratio under 1.2.

**N4. Failure atlas.** Triage failed builds by script: bug (exception, shape, neutralised patch differs from baseline), optimisation failure (NaN, spike, collapse), null. For optimisation failures, diagnose at the last healthy and the failing step; log the first cell to leave its seed envelope (e.g., max attention logit before a spike). Ask for a causal story, a rival, and the smallest stabiliser that lets the idea live. Basis: [34] (failures traced to causes redirected search), [37], [40]; about 60% of failed DeepScientist trials were implementation errors [L1], so triage first. Measure: rescue rate (failures passing a rung after one stabiliser); stabiliser hypotheses per 10 failures.

**N5. Contradiction ledger.** Each kept belief stores mechanism, supporting runs and a quarantine counter. Contradictions: two cells the belief says co-move do not (sign test across seeds); a win survives ablation of its stated mechanism; a ladder inversion (wins at 45 steps, loses at 240); transfer fails across scale. Ask for a reconciling hypothesis making both observations true plus the cheapest discriminating run; quarantine three rounds, then promote or drop. Basis: [9] (people discount, so force the record), [29], [1]. Measure: contradictions per 10 runs; share resolved by a hypothesis whose later prediction held; wins from resolved ones.

**N6. Question ledger before ideas.** One call writes 10 questions the residuals raise, no solutions, each with a named measurement on existing checkpoints and an expected answer. A second call scores them (decision relevance x prior uncertainty / cost); scripts answer the top 3 (5 minutes each) and answers enter ideation as facts. Basis: [12][13][15][16][1]. Measure: share of answers that move a prior; win rate and novelty of ideas citing an answered question vs not.

**N7. Plateau protocol** (extends 02 #6). Trigger: 3 and 7 flat evaluations in a lineage, or a stuck cell. Forced steps: a diagnostic call listing which constraint binds (+10% parameters, 2x step time, memory) and which assumption near-misses share; a labelled non-eligible relaxation probe (e.g., +30% parameters) testing whether the plateau is constraint-bound; then a request for a design that gets the probe's gain inside the rules. Basis: [34][35][23][24]. Measure: plateau exits within 2 rounds vs a plain extra context; drop if ratio under 1.2 after 10 triggers.

**N8. Anchored long-shot quota with an unlock log.** Each agent owes k long shots per round; each cites one residual, contradiction or atlas row and one unlock (something newly cheap after a win, anomaly or stabiliser), states a 5-minute probe and a kill criterion, and uses the lenient lane. One cheap call after each confirmed win or resolved anomaly lists unlocks. Basis: a novelty enlarges the adjacent possible [10][11]; hit rates 1-3% [L1]. Noise: cap 20-30%, random draws as holdout (00_IDEAS #26). Measure: hit rate per 10 builds vs main lane (expect low); new unlocks or falsified assumptions per long shot; unanchored long shots dropped.

**N9. Noise firewall with sham anomalies.** Every anomaly replicates on a fresh seed and passes the FDR filter before reaching a prompt. About 10% of anomaly prompts carry a sham (a residual from a placebo-recipe table or shuffled labels) to measure chasing. Anomaly-seeded slots stay at or below 30% until conversion beats control. Basis: [1][2][21], placebo logic in [L4]. Measure: sham-chase rate under 5%; replication rate; false flags per table.

**Validation.** Plant 4 known pathologies in copies of the baseline (no warmup, unscaled residual init, attention logits scaled 4x, 10x Adam learning rate on embeddings), each mapped to a cell. Check recall of N1, time to a fix at the planted site, and false flags on untouched copies. Arms: A plain table (today), B = N1+N2, C = full stack; 3 loop seeds, equal tokens. Disable a mechanism at ratio under 1.2 after 50 ideas.

## 3. Caveats

Base rates are self-coded and I found no cross-field survey of anomaly-initiated discoveries. At 20M parameters seed noise is large [L5], so most raw residuals may be noise (hence N9). Unopened or secondhand: [14], [33], [37] numbers, [31]. The shared search quota ran out mid-task; later checks were direct fetches.

## Sources

[1] Dunbar, How scientists think. https://sites.cc.gatech.edu/classes/AY2013/cs7601_spring/papers/Dunbar.pdf
[2] Press account of Dunbar's labs. https://events.foresight.org/learning-from-science/
[3] Trickett, Trafton, Schunn 2001. https://conferences.inf.ed.ac.uk/cogsci2001/pdf-files/1054.pdf
[4] Corneli et al. (quotes Merton 1948). https://arxiv.org/abs/1411.0440
[5] Campanario 1996. https://doi.org/10.1007/BF02093482
[6] Hargrave-Thomas et al. 2012. https://wjgnet.com/2218-4333/abstract/v3/i1/1.htm
[7] SEP, Thomas Kuhn. https://plato.stanford.edu/entries/thomas-kuhn/
[8] Bruner and Postman 1949. https://psychclassics.yorku.ca/Bruner/Cards/
[9] Chinn and Brewer 1992. https://escholarship.org/uc/item/0d65f9gt
[10] Tria et al. 2014. https://arxiv.org/abs/1310.1953
[11] Fink et al. 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5722871/
[12] Getzels and Csikszentmihalyi 1976, via a UvA thesis. https://pure.uva.nl/ws/files/1856164/105340_06.pdf
[13] Reiter-Palmon et al. 1997. https://digitalcommons.unomaha.edu/psychfacpub/52
[14] Abdulla 2016 dissertation. https://openscholar.uga.edu/record/21269/files/abdulla_ahmed_m_201612_phd.pdf
[15] Rothe, Lake, Gureckis 2018. https://www.gureckislab.org/papers/ref/rothe2018people
[16] Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271
[17] Itti and Baldi 2009. https://ilab.usc.edu/publications/Itti_Baldi09vr.html
[18] Baldi and Itti 2010. https://pmc.ncbi.nlm.nih.gov/articles/PMC2860069
[19] Schmidhuber, Driven by compression progress. https://arxiv.org/abs/0812.4360
[20] Oudeyer and Kaplan 2007. https://www.frontiersin.org/articles/10.3389/neuro.12.006.2007/full
[21] Burda et al. 2018. https://arxiv.org/abs/1808.04355
[22] Ten et al. 2021. https://doi.org/10.1038/s41467-021-26196-w
[23] Bilalic, McLeod, Gobet 2008. https://bura.brunel.ac.uk/handle/2438/641
[24] Bilalic, McLeod, Gobet 2010. https://cognition.aau.at/download/Publikationen/Bilalic/Bilalic_etal_2010b.pdf
[25] MedEinst. https://arxiv.org/abs/2601.06636
[26] Only Connect red herrings. https://arxiv.org/abs/2306.11167
[27] Negative capability. https://en.wikipedia.org/wiki/Negative_capability
[28] Chirumbolo et al. 2005. https://journals.sagepub.com/doi/10.1177/1046496404268535
[29] Miron-Spektor et al. 2011. https://ideas.repec.org/a/eee/jobhdp/v116y2011i2p229-240.html
[30] Miron-Spektor et al. 2022. https://ideas.repec.org/a/eee/jobhdp/v171y2022ics0749597822000371.html
[31] Rothenberg, Flight from Wonder. https://academic.oup.com/book/11385
[32] Rios-Garcia et al. 2026. https://arxiv.org/abs/2604.18805
[33] Agentic AI Scientists Are Not Built For Autonomous Scientific Discovery (cites Ding and Li 2025). https://arxiv.org/abs/2605.08956
[34] ReASearch. https://arxiv.org/abs/2608.06714
[35] AIRA_2. https://arxiv.org/abs/2603.26499
[36] Voboril and Szeider. https://arxiv.org/abs/2608.08127
[37] Raccuglia et al. 2016. https://doi.org/10.1038/nature17439
[38] Darcet et al. 2023. https://arxiv.org/abs/2309.16588
[39] Dettmers et al. 2022. https://arxiv.org/abs/2208.07339
[40] Zhai et al. 2023. https://arxiv.org/abs/2303.06296
[41] Penzias and Wilson. https://en.wikipedia.org/wiki/Discovery_of_cosmic_microwave_background_radiation
[42] Bell Burnell. https://en.wikipedia.org/wiki/Jocelyn_Bell_Burnell
[L1] 05_scientific_discovery.md ; 12 = 12_ml_research_practice.md ; 00_IDEAS, 02 = thinking_parts/00_IDEAS.md, 02_attention_framing.md
[L4] nano/diagnose.py, predict.py, loop.py, controls.py ; [L5] EXPERIMENT_PLAN.md
