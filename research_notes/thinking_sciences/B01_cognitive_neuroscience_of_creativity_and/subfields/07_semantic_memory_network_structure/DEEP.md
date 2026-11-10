# Semantic memory network structure: deep document

*Subfield B01.07. Evidence files: evidence_a-d.jsonl (ids a01-a27, b01-b27, c01-c26, d01-d20), claims.jsonl (K01-K33), critique.md. Status tags: [E] established (several independent sources), [S] single-source, [C] contested. [V] = page or PDF text opened, [M] = snippet or abstract only.*

## 1. What it is

Semantic memory is the store of word and concept meaning. Network science models it as a graph. Nodes are words. Edges link words that people associate or judge as related. Researchers ask whether the shape of this graph differs between more and less creative people.

Three shape measures matter:
- **Average shortest path length (ASPL):** steps between two random words. Short means any idea is near any other.
- **Modularity (Q):** how strongly the graph splits into tight clusters. High Q means walled-off topics.
- **Clustering (CC) and small-world index (S):** how many neighbours of a word are also neighbours of each other, compared with a random graph.

The core claim, from Mednick (1962) and Kenett, Anaki and Faust (2014): creative people have a shorter-path, less-modular, more spread-out network, so remote ideas are easier to reach. A related line measures distance directly. The Divergent Association Task (DAT) asks for 10 unrelated words and scores the mean embedding distance. Semantic distance (SemDis) scores how far an answer is from its prompt.

For our agent this matters at O7 (map an analogue) and S3 open mode. They need a rule for how far seed concepts should be from the problem. The human literature gives a hypothesis (far helps), a measure (embedding distance) and warnings (far costs feasibility; group results do not describe individuals).

Honest summary, from critique.md: the group effect is real in one lab with 33 people per group. Individual-level effects are weak and metric-dependent. No independent or preregistered replication of the 2014 group result exists in our evidence. No study manipulates seed distance for an LLM agent and measures correctness.

## 2. History and theories in depth

**Mednick 1962 (a01, [M]).** Creativity is forming new combinations from remote associative elements. Creative people have a flat associative hierarchy: many weak links to a cue. Less creative people have a steep hierarchy: a few strong common links. The Remote Associates Test (RAT) was built to measure this. The theory was verbal, with no network model and no direct test of the gradient. We know it only through later papers.

**Benedek and Neubauer 2013 (a04, [V]).** First direct test of the gradient. N about 100 (df=98), free association, 60 s per cue. Strength of the top 10 associates falls from 69.5% to 21.7% (ranking F(9,882)=83.33, eta2p=.46). The ranking x group interaction is not significant (F=0.98). Slope difference between groups: b=-.052, t(98)=-0.28. The steepness claim fails. Creative people did give more uncommon associates and were more fluent.

**Kenett, Anaki and Faust 2014 (a02, a03, a18, b01, b02, [V]).** First network-science test. 144 recruited, 139 analysed (47 men, 92 women, mean age 23). The free-association subsample was 33 low (LSC) and 33 high (HSC) creative people (lower and upper tertile from a decision tree on RAT, TACT and metaphor tasks). 96 cue words in 24 categories, one minute each. RAT was 7.0 (SD 2.7) vs 13.2 (SD 3). Group networks were compared with bootstrap tests. The paper gives no standardised effect size. "Small effect" is the brief's wording.

**Kenett et al. 2018 (a05, b03, d07, [V]).** Percolation re-analysis of the same 66 people. Remove the weakest links step by step. The HSC network stays connected longer. Not an independent replication.

**Individual-level era (2017-2026).** Benedek 2017 (d18, [M]) found creativity linked to path length and clustering only under one filtering method. Bernard 2019 (d19, [M]) reports agreement, as proceedings. Ovando-Tellez 2022 (N=101) used pairwise relatedness ratings. Larger studies (N=236, 106, 479, 126) found weak, mixed links. Robinson 2024 (d06, [V]) showed global graph measures are not stable within one person across tasks.

**Distance as a measure (2021 onward).** Olson 2021 introduced the DAT. Beaty and Johnson 2021 built SemDis. Organisciak 2023 (d11, [M]) trained scorers (Ocsai) that beat raw distance.

**LLM era (2023-2026).** The same measures were applied to LLMs: DAT scores (Chen and Ding; Bellemare-Pepin), network comparisons (Domanti 2026; Abramski 2024), homogeneity studies (Patel 2026; Jiang 2025), and far sources in idea generation (Liu 2026).

**Competing accounts.**
- Structure account: network shape (path, modularity) causes remote association.
- Process account: search differs (clustering, switching, executive control, path-dependent search; b06, b26, c20). A structure gap could be a by-product.
- Fluency account: creative people give more unique responses, which changes graph metrics (a03: eta2=.614).
- Instruction account (LLMs): distance is mostly what the prompt asks for (a22, c07).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| HSC group network has shorter paths, smaller diameter | N=139 recruited; 33 vs 33 in networks. ASPL 4.6 (LSC) vs 3.93 (HSC); diameter 12 vs 8; Q 0.62 vs 0.58; S 6.86 vs 7.76; CC 0.67 vs 0.66 (no gap); mean degree 5.88 both | Kenett 2014 (a02, b01) | [C] one lab, no independent replication |
| Fluency confound | HSC more unique responses per cue: F(1,191)=310.9, eta2=.614; higher for 60% of words. First 10 responses only: path gap stays, modularity direction reverses | Kenett 2014 (a03, b02) | [S] |
| Node impact | LSC 56% negative-impact nodes; HSC 65% positive (U(192)=3523, p<.005) | Kenett 2014 (a03) | [S] |
| Mednick steep gradient not supported | Top-10 strength 69.5% to 21.7%; group x rank F(9,882)=0.98; slope t(98)=-0.28 | Benedek and Neubauer 2013 (a04) | [C] |
| Percolation robustness | Integral 14.76 (LSC) vs 15.64 (HSC), n=33 each; shuffled links reverse sign (21.45 vs 20.55) | Kenett 2018 (a05, b03, d07) | [S] same data |
| Individual relatedness networks | N=101, 595 pair ratings. C-Act vs weighted ASPL rs=-.276 (p=.007); C-Ach vs weighted Q rs=-.295 (p=.004); weighted CC vs C-Ach .201 (p=.052, ns) | Ovando-Tellez 2022 (a06, b04) | [S] |
| Larger samples: weak, mixed | N=236 fluency vs objective originality r=.15; N=106 only fluency predicts (R2=.503); N=479 AUT R2=.03; N=126 omnibus p=.050-.055 | a07, b18, b19, b20 | [E] weak |
| Metric redundancy | Global efficiency vs modularity r=-.75; CC vs efficiency r=.78 (N=236) | Skurnik and Kenett 2026 (a20) | [S] |
| Global metrics unstable per person | Path length cross-task r from -.08 to .53, mostly ns; 4 experiments x n=70; local pairwise relatedness reliable | Robinson 2024 (d06) | [S] |
| Method dependence | Path/clustering link only under threshold filtering | Benedek 2017 (d18) | [S] [M] |
| Education effect tiny | Montessori 36 vs traditional 31: path d=0.24, Q d=0.32, divergent creativity d=0.58 | b08 | [S] |
| DAT validity modest | Study 1A N=141: r=.50 screened (n=57), .32 full; 1B N=285 r=.32; retest .73 (N=50); preregistered N=8,572 r=.13 | Olson 2021 (b15, b21, d08) | [E] |
| Embedding distance tracks human ratings | Latent r .91, .75, .45, .49 (novelty .73, appropriateness -.81), .73, .85 over 5 studies; GloVe r=.61 | Beaty and Johnson 2021 (b16, a08) | [S] |
| Metric swap | LLM-embedding S-DAT agrees with DAT r=.65; slightly lower AUT validity | Haase 2025 (d09) | [S] |
| Distance predicts word learning | r=.33 (day 1), .38 (day 2), N about 142; d=0.31 for the day drop | Luchini 2025 (a09) | [S] |
| Search structure | N=86: clustering vs AUT fluency and uniqueness p<.001; switching tied to executive tasks | Comm. Biol. 2022 (b06, b26) | [C] |
| GPT-4 beats humans on DAT | GPT-4 89.1 (above 96.1% of humans); GPT-3.5-turbo 80.8; GPT-4 at T=1.5 85.6 (above 72% of 100,000 humans) | a10, a11, c10 | [E] |
| Random sampler beats most humans | Naive random WordNet noun sampler above most humans and models | Chen and Ding (a10) | [E] |
| Repetition across runs | microscope in 70%, elephant in 60% of GPT-4 sets; ocean over 90% for GPT-4-turbo; humans' top words car 1.4%, dog 1.2%, tree 1.0% | a11, c09 | [E] |
| LLM network vs human | GPT-4o ASPL 4.378 vs LCH 3.429 vs HCH 3.325 (d 2.32, 2.55; human gap d=0.42); Q .692/.666/.662; percolation 77.9/85.2/85.8; originality above LCH (B=0.03, p=.048), below HCH (B=-0.12) | Domanti 2026 (b09, c01-c04) | [S] |
| LLM free-association world differs | Unique responses: humans 116,640, Mistral 41,369, Llama3 105,367, Haiku 15,275; edge overlap 13-23%; under half of nodes shared | Abramski 2024/25 (b13, c18, c19) | [E] |
| Free association is a noisy readout | RSA r=.14 (free association) vs .35-.46 (forced choice) | Schiekiera 2026 (b14) | [S] |
| Rising homogeneity | AUT cross-family cosine distance about 0.50 to under 0.40 over 68 models (slope -0.01385 per bin); same-prompt similarity above 0.8 in 79% of cases | Patel 2026 (c12); Jiang 2025 (c13) | [E] |
| Far source helps only strong LLMs, only when far | o3 and Claude-Sonnet-4: all pairs beta=.02 ns; top 50% .12; top 10% .24. Humans gain at nearly every cut | Liu 2026 (d01, d03) | [S] |
| Originality vs feasibility | r=-.74; top 10% human ideas equal in originality to LLM (beta=.02) but less useful (.81), less feasible (.26) | Liu 2026 (d02) | [S] |
| Always-far for humans | N=245, 1,574 ideas. Best-idea novelty 0.64 (always-far) vs 0.88 (none), F(4,239)=2.5, p=.04; fluency equal F=0.5, p=.77 | Chan 2017 (d04, d05) | [C] |
| Cheap diversity gains | Verbalized sampling 1.6-2.1x semantic diversity (human-rated poem 1.90 to 2.39); instruction lifts diversity +0.039 to +0.062 at 1.1x tokens | Zhang 2026 (d12); Ibrahim 2026 (d14) | [E] diversity only; no correctness |
| Persona sets | AUT diversity +78.8%, homogeneity 0.946 to 0.798; DAT 89.13 to 89.48 | Moon 2026 (c22) | [S] |
| Flexible LLMs more original | Observational; humans show no link; jump test-retest r=.22 LLM vs .42 human | Nath 2024 (d15) | [S] |
| Association skill predicts other skills | 35 LLMs: association vs analogy originality r=.73; vs blend originality .42; humans (N=75) below nearly every LLM | Schapiro 2026 (d16) | [S] |
| Weight steering | Up to 14 human percentile points on DAT; originality d=+0.40 (N=720) | Schapiro 2026 (c14, c15) | [S] needs weights |

## 4. Mechanisms and models

**4.1 Group network construction (Kenett 2014).** Collect free associations per cue per participant. Build a cue-by-response count matrix per group. Compute cosine similarity between cue vectors. Keep edges above a threshold chosen to fix density. Compute ASPL, diameter, CC, Q and S against random graphs of equal size. The bootstrap on node subsets inflates significance (critique caution 2), so use effect sizes. Equalise response counts (first N responses) before comparing.

**4.2 Individual relatedness network (Ovando-Tellez 2022).** Pick 35 words. Rate all 595 pairs on 0-100. Weighted network: edge weight is the rating. Unweighted: keep ratings above 50. Compute weighted ASPL (distance = inverse weight) and Q. For an agent this is a pairwise-relatedness matrix over its own concept set. Use only local pairwise values; global statistics are unreliable per person (Robinson 2024).

**4.3 Percolation.** Delete edges below a rising threshold. Track the largest connected component. Integrate over thresholds. A higher integral means the network stays connected under weak-link loss. Check with a shuffled-link control.

**4.4 Embedding distance (DAT, SemDis).** Embed each word (GloVe in the DAT). Distance = 1 minus cosine similarity. DAT = mean pairwise distance over the first valid words, scaled by 100. SemDis for an answer = distance from prompt to answer. Multiplicative composition of word vectors works for multi-word answers (latent r .91 vs -.37 additive, b16). Spell-check first (missing words cost 4.1% of data in one study, b22). Pick one embedding and calibrate. S-DAT keeps r=.65 with GloVe DAT, slightly lower validity (d09).

**4.5 Distance and usefulness.** Distance measures novelty only. In Beaty and Johnson Study 4 distance correlated .73 with novelty and -.81 with appropriateness. Liu 2026 gives originality vs feasibility r=-.74. Any distance rule needs a fit check.

**4.6 Cross-domain seed (Liu 2026).** Give target problem plus a random source concept. Compute source-target distance with sentence embeddings. Bin pairs by distance. Compare originality by bin. Observed: strong LLMs gain only in the top 50% and top 10% bins.

**4.7 Search-process models.** Clustering means staying in a semantic category; switching means jumping. Heineman 2024 (c20): human fluency lists fit a path-dependent model with a category bias better than a random walk. Nath 2024 (d15) counts jumps between sentence-embedding clusters. Agent version: generate k ideas per cluster, then force a switch to a cluster far from all used ones.

**4.8 Diversity tools.** Verbalized sampling: one call returns k answers with stated probabilities; take the low-probability end. Anchorless diversification: a population-referential instruction ("stand out from other responses") or one planning call that splits the idea space into semantic directions. Cost about 1.1x tokens (d12, d14).

**4.9 What an LLM "network" is.** It is a readout from prompting, not internal geometry. It differs from the human one in size, degree and edges (c17-c19). Forced-choice relatedness tracks hidden geometry better than free association (b14). Use an external graph or embedding for distance.

## 5. What holds up

**Holds (direction, small size).**
- Creative people produce more unique and more distant responses. Embedding distance tracks human originality ratings; sample-dependent (K08, K10).
- Individual-level links to structure are weak, mostly in the predicted direction (K06, four sources).
- Distance buys novelty at a cost to feasibility (K28, K21).
- LLM DAT scores are high and instruction-driven (K11, K12).
- LLM output is repetitive across runs and models (K13, K15).

**Does not hold or is contested.**
- Mednick's steep gradient fails at response-strength level (a04).
- No independent or preregistered replication of the 2014 group result. The 2018 percolation paper reuses the same 66 people. Direction repeated by related studies, exact result not replicated (K01).
- Part of the group gap is fluency: modularity reverses on first-10 responses (b02).
- Global per-person metrics are unreliable (d06) and depend on thresholding (d18).
- DAT-AUT originality correlation: .50 screened, .32 full, .13 in the preregistered N=8,572 study (K10).
- The LLM mapping fails. GPT-4o has longer paths, higher modularity and a more fragile network than both human groups, yet beats low-creative humans (K17). Bootstrap inflates the human gap.
- Always-far seeds do not help humans (0.64 vs 0.88 novelty, Chan 2017), while Liu 2026 finds humans do gain from a far source in another task. Task and delivery matter (K27).

**Moderators found.**
- Model strength: only the strongest LLMs gained from far sources (K26).
- Task state: far helps at impasse, near while productive (Chan 2017; d05).
- Instruction: naming opposites lowers DAT because opposites are close in embedding space; strategy hints (etymology, thesaurus) raise it (K12). Thesaurus beat the DAT prompt for GPT-4 (a23).
- Sampling: temperature or top-p raises DAT only for weaker models; GPT-4 gains nothing; stability drops (K14).
- Embedding: GloVe .529 vs MUSE .757 in PACE (a12).
- Screening inflates DAT validity (b21).

**Interventions.**
- Worked (diversity measures): verbalized sampling, population-referential instruction, direction planning, persona sets (K16, K31). Weight steering raised DAT but needs weights (K22).
- Did not work: higher temperature for GPT-4; diversity decoding against homogeneity (c13: under min-p 81% of pairs still exceed 0.7); activation steering did not transfer from DAT to AUT (c15).
- Not tested: exclusion lists, cluster-then-switch order, controlled seed distance with correctness.

## 6. Language models

**DAT.** GPT-4 greedy 89.1, above 96.1% of humans. GPT-3.5-turbo 80.8, above the human mean. Smaller open models fall below the human mean, roughly with size (a10, b12). GPT-4 at T=1.5 scored 85.6, above 72% of 100,000 humans (c10); scoring set-ups differ, so the two papers cannot be compared. GPT-4-turbo scored below GPT-4 (c08). A random WordNet sampler also beat most humans, so DAT rewards rarity (a10). GPT-4's lead shrinks after controlling for token surprisal (c07).

**Instruction dependence.** Without the DAT prompt, models give related words. With it, they jump to rare words. Strategy hints help.

**Repetition.** microscope 70%, elephant 60%, ocean over 90% (GPT-4-turbo). Humans' top word sits at 1.4%. High distance, low variety.

**Homogeneity.** 68 models, March 2023 to July 2026: cross-family cosine distance 0.50 to under 0.40 (c12, d20). 70+ models: same-prompt similarity above 0.8 in 79% of cases (c13). Both used defaults with no scaffold arm, so we do not know whether our scaffold reverses it.

**Network shape.** GPT-4o is more rigid (ASPL 4.378) than both human groups yet more original than low-creative humans (b09, c02). Fluency was 43.8 vs 19.1 (HCH) and 12.2 (LCH) (c01). LLM free-association networks have fewer unique responses, lower degree for Haiku (8.8 vs 20.0 for humans), and 13-23% edge overlap (c18). Priming effects are similar.

**Readout.** Free association RSA r=.14 against hidden geometry; forced choice .35-.46 (b14).

**Far sources in problem tasks.** Liu 2026: seven LLMs, 140 humans, 1,002 raters. Overall cross-domain beta=0.36. For the best two models all-pairs beta=.02; top 50% .12; top 10% .24. LLMs transfer structure and function, so their top ideas keep utility. Humans copy surface features and lose utility.

**What moves LLM diversity.** Persona sets: diversity +78.8%, homogeneity 0.946 to 0.798, DAT 89.13 to 89.48 (c22). Verbalized sampling 1.6-2.1x. Direction planning gives the best gain per token (0.21 to 0.38 per 100k tokens). Gains are on diversity proxies and human win-rates, not on correctness.

**Model skill.** Association originality predicts analogy originality r=.73 across 35 LLMs; humans (N=75) score below nearly every LLM (d16). PACE chain distance correlates .739 with creative-writing rank (30 models; source anonymous, a12). LLM alignment with default-mode brain activity rises with idea originality, N=170 (c21).

## 7. What our agent should take

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Do not tune the agent on graph shape. Treat network metrics as at most a weak predictor. | G7 | [E] | K06; a07, b18, b19, b20 |
| Do not use DAT score alone as a creativity target. Use it only as a cheap novelty meter beside a fit check. | G8, O7 | [E] | K10, K21; b15, d08 |
| Do not use the model's free association as the distance readout. Use pairwise embedding or forced-choice relatedness from one calibrated external embedding. | O7 | [E] on the warning (K18); [S] on embedding choice | K18, K19, K30; b14, c18, d06 |
| Give distance as an explicit instruction with a named strategy (etymology, thesaurus, unrelated domain). Do not name opposites. Do not rely on higher temperature. | O7, S3 | [E] | K12, K14; a22, a23, c07 |
| Expect low across-run variety. Keep a used-seed list in memory and count distinct seeds. | O7, memory | [E] on repetition; fix untested | K13, K15; a11, c09, c12, c13 |
| Pair every far-seed idea with a fit check run by code. | S4, G8 | [E] on trade-off direction | K21, K28; d02, b16 |
| One-call diversity tools (verbalized sampling, direction planning) are cheap options in S3 open mode when diversity is wanted. | S3 | [E] diversity only | K31; d12, d14 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Graded seed distance (bottom, middle, top decile, unrelated-domain bin) in open mode, scored on originality and correctness. | O7, S3 | [S] | K26, K29; d01, d03 |
| Far seeds only on impasse versus always on. | S3, S6 | [C] | K27; d04, d05 |
| Cluster-then-switch seed order versus random. | S3 | [C] | K25, K32; b06, d15 |
| Exclusion list of used seeds across runs. | O7, memory | [S] | K13, K15, K31 |
| Persona-seeded open mode. | S3 | [S] | K16; c22, d14 |
| Pool-distance filter: reject candidates too close to earlier ones. | S3, S7 | [C] | K23; c16 |
| Remote-association probe to choose the model for open mode. | S0 | [S] | K33; d16 |
| Model-strength gate: far seeds only for strong models. | S0, O7 | [S] | K26; d01 |

Do not add: weight steering (needs weights, K22), graph-shape targets (K17), LLM-side network analysis.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup, seeds and checks counted, G7). Report originality and correctness separately, with bootstrap intervals over items.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Open-mode items with a checkable answer (ARC variants, riddles with a hidden rule) | Seeds at bottom, middle, top-decile distance, plus an unrelated-domain bin, vs no seeds | Pass rate; distinct correct solutions | Small gain in top bin for a strong model only; possible drop in the unrelated bin |
| T2 | Same items, one strong and one weaker model | Far seeds vs none, each model | Pass-rate gap between models | Liu 2026 direction: only the stronger model gains |
| T3 | Impasse items (plain attempt fails once) | Always-far vs near-then-far at impasse vs none | Pass rate after S6 | Gate beats always-far (Chan 2017) |
| T4 | Open idea items with a fit rubric by code or tests | Plain "be far" vs strategy-named seeds | DAT or SemDis of seed sets; fit pass rate | Hints raise distance; fit may drop |
| T5 | 8 independent runs per item | None vs exclusion list vs persona seeds vs verbalized sampling vs direction planning | Distinct seeds; pairwise similarity; pass rate | Diversity up about 0.04-0.06 at 1.1x tokens; correctness neutral |
| T6 | Open mode | Cluster-then-switch (k ideas per cluster, forced jump) vs random order | Originality; pass rate | Small plus; uncertain |
| T7 | Seed pairs | GloVe vs LLM embedding vs forced choice for distance | Correlation with downstream pass or originality | Pairwise measures agree near r=.65 |
| T8 | Far-seed ideas | Fit check by code vs none | Feasibility pass; originality loss | Check removes infeasible ideas at small originality cost |

## 9. What does not transfer, and why

- **Group graph shape of humans.** The 2014 result describes a group of 33. The authors say group networks cannot describe individuals (b23). The agent has no group.
- **LLM graph shape as a target.** GPT-4o is more rigid than both human groups and still more original than low-creative humans (b09). Shape is not the lever.
- **Mednick's steepness.** Refuted at response-strength level (a04). Sampling many associations is a fluency effect.
- **Human surface-feature copying.** Humans lose utility on top cross-domain ideas because they copy surface features; LLMs copy structure and function (d02). The human feasibility penalty may be smaller for LLMs.
- **LLM free association as a memory probe.** Noisy readout (RSA r=.14).
- **Weight and activation steering.** Need model internals.
- **Schooling and word-learning effects.** Montessori d=0.24-0.32 and learning r=.33-.38 have no agent analogue.
- **Creativity groups.** Built from RAT and TACT scores; the agent has no such label.
- **DAT as target.** A random sampler beats most humans. Rarity is not creativity.
- **Brain-imaging links** (b07: tau=-0.56 rating vs distance; tau=0.24 default-mode activity). No agent counterpart.

## 10. Open questions

1. Does controlled seed distance raise originality and correctness at equal tokens? No study tests it (K29).
2. Is the far-seed benefit due to distance or only to variety? Chan 2017: fluency equal, always-far did not help humans. No LLM test.
3. Is there an inverted U? Liu 2026 rises to the top decile only; the far end was never sampled.
4. Is there an independent or preregistered replication of Kenett 2014 with more than 33 per group? Luchini 2023 (N=477, abstract only) points the same way for convergent thinking.
5. Which distance metric should the agent use? Ensembles and trained judges (Ocsai up to r=.81) are snippet-level.
6. Do exclusion lists and persona seeds raise cross-run diversity at equal tokens without hurting accuracy?
7. Does cluster-then-switch ordering help an LLM? Only observational data exist.
8. Is rising homogeneity true for our model, and does the scaffold reverse it?
9. Does the strong-model threshold for benefiting from far sources hold for our model?
10. Do far seeds behave differently on exact-answer problems than on open idea tasks?

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [M] Mednick (1962) The associative basis of the creative process. https://doi.org/10.1037/h0048850
- [V] Kenett, Anaki and Faust (2014) Semantic networks in low and high creative persons. https://pmc.ncbi.nlm.nih.gov/articles/PMC4051268/ and https://www.frontiersin.org/articles/10.3389/fnhum.2014.00407/full
- [V] Benedek and Neubauer (2013) Revisiting Mednick's model. https://pmc.ncbi.nlm.nih.gov/articles/PMC3924568/
- [V] Kenett, Levy, Kenett and Stanley (2018) Flexibility of thought (percolation). https://pmc.ncbi.nlm.nih.gov/articles/PMC5798367/
- [V] Ovando-Tellez, Kenett, Benedek et al. (2022) Brain connectivity-based prediction of real-life creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC8816337/
- [V] Skurnik and Kenett (2026) Semantic memory structure and self-evaluation of creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC13027982/
- [V] Beaty and Johnson (2021) SemDis. https://pmc.ncbi.nlm.nih.gov/articles/PMC8062332/
- [V] Luchini et al. (2025) Semantic distance and word learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC12214691/
- [V] Chen and Ding (2023) Probing the creativity of LLMs. https://arxiv.org/abs/2310.11158
- [V] Bellemare-Pepin et al. (2024) Divergent creativity in humans and LLMs. https://arxiv.org/abs/2405.13012
- [V] PACE (2025, anonymous authors). https://arxiv.org/html/2510.12110v1
- [M] Nakajima, Zuiderveld and Pezzelle (2026). https://arxiv.org/abs/2601.20546
- [M] Vintar and Javorsek (2025). https://arxiv.org/abs/2511.04077
- [M] Beaty, Kenett, Hass and Schacter (2023) Semantic memory and creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC10128864/
- [M] Gray et al. (2019) Forward flow. https://doi.org/10.1037/amp0000391
- [M] Kenett and Faust (2019) A semantic network cartography of the creative mind. https://doi.org/10.1016/j.tics.2019.01.007
- [M] Moonlight review, semantic networks and idea originality. https://www.themoonlight.io/review/are-semantic-networks-ass
- [M] Scientific Reports 2025 benchmark of LLMs. https://www.nature.com/articles/s41598-025-25157-3
- [V] Cognitive and neural correlates of semantic search (Comm. Biol. 2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9203494/
- [V] Creative connections: neural correlates of semantic relatedness (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11222432/
- [V] Education shapes semantic memory structure (Montessori, 2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8660875/
- [V] Domanti, Campidelli, Agnoli and De Angeli (2026). https://arxiv.org/abs/2602.02048
- [M] Wang et al. (2025), cited second-hand in Domanti 2026.
- [V] Abramski et al. (2024/2025) LLM World of Words. https://arxiv.org/abs/2412.01330 and https://pmc.ncbi.nlm.nih.gov/articles/PMC12084308
- [V] Schiekiera et al. (2026) From associations to activations. https://arxiv.org/html/2602.00628v1
- [V] Olson et al. (2021) Naming unrelated words predicts creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC8237676 (PNAS DOI https://doi.org/10.1073/pnas.2022340118)
- [V] Creative Connections: computational semantic distance (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8826533/
- [V] Semantic memory and creative evaluation (BMC Psychology 2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12288250/
- [V] Cognitive multiplex network approach (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12378698/
- [V] Knowledge structure and scientific divergent thinking (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13413292/
- [V] Patel et al. (2026) Are LLMs becoming similarly creative? https://arxiv.org/abs/2608.19437
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Schapiro et al. (2026) CreativityNeuro. https://arxiv.org/abs/2607.01433
- [V] Moon, Johnson et al. (2026) Thinking Outside the Bots. https://arxiv.org/abs/2610.17324
- [V] Zhang and Ma (2026) Psychometric comparability of LLM digital twins. https://arxiv.org/abs/2601.14264
- [V] Heineman, Koenen, Varma (2024) Path dependent account of category fluency. https://arxiv.org/abs/2405.06714
- [V] Ismayilzada et al. (2026) LLMs align with the human brain. https://arxiv.org/abs/2604.03480
- [V] Moon, Cho et al. (2026) Breaking homogeneity. https://arxiv.org/abs/2609.30492
- [M] Hubert, Awa, Zabelina (2024). https://doi.org/10.1038/s41598-024-53303-w
- [V] Liu, Dubova, Conklin, Harada, Griffiths (2026) Cross-domain effects. https://arxiv.org/abs/2603.19087
- [V] Chan et al. (2017) Semantically far inspirations. https://iis.seas.harvard.edu/papers/chan17semantically.pdf
- [V] Robinson, DeStefano, Vul, Brady (2024) Local but not global graph theoretic measures. https://doi.org/10.3758/s13428-023-02271-6
- [V] Haase, Hanel, Pokutta (2025) S-DAT. https://arxiv.org/abs/2505.09068
- [M] Organisciak et al. (2023) Beyond semantic distance. https://openscoring.du.edu/research
- [V] Zhang et al. (2026) Verbalized sampling. https://arxiv.org/abs/2510.01171
- [V] Ibrahim, Azad, Baten (2026) Anchorless diversification. https://arxiv.org/abs/2605.30150
- [V] Nath, Dayan, Stevenson (2024) Creative process in humans and LLMs. https://arxiv.org/abs/2405.00899
- [V] Schapiro et al. (2026) Combinatorial creativity. https://arxiv.org/abs/2509.21043
- [M] Luchini et al. (2023) Convergent thinking and semantic networks. https://cris.technion.ac.il/en/publications/convergent-think
- [M] Benedek et al. (2017) How semantic memory structure and intelligence contribute to creative thought. https://cris.biu.ac.il/en/publications/how-semantic-memory-s
- [M] Bernard, Kenett et al. (2019). https://cris.iucc.ac.il/en/publications/building-individual-
