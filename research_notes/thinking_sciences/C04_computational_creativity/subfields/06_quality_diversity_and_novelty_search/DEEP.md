# Quality-diversity and novelty search: deep document

*Subfield 06 of C04 Computational creativity. Built from evidence_a-d.jsonl (ids a01-a33, b01-b28, c01-c28, d01-d17), claims.jsonl (C04.06-K01 to K23) and critique.md in this folder. Written for the single-agent thinking schema (SCHEMA.md v0.2). Links to parallel subfields are notes only: Go-Explore and archives, Bandits and Thompson sampling for operator selection, Library learning, Evaluation of creativity, Anytime search and restarts, Fixation, Geneplore.*

*Reading note on trust. The critique pass re-opened 9 of the key papers and confirmed 10 sets of numbers. It did not re-open Pugh et al. 2016 (download failed), Cully et al. 2015, CodeEvolve, LEVI, Lim et al., NoveltyBench, Artificial Hivemind and LLMatic. Those rest on first-pass notes. Many LLM numbers exist only in figures. Where a number is figure-only, this document says so.*

---

## 1. What it is

Two linked ideas from evolutionary computation.

**Novelty search.** Do not score a candidate by how close it is to the goal. Score it by how different its behaviour is from what has been seen. Novelty is the mean distance to the k nearest neighbours in a behaviour space, counting both the current population and an archive of past novel behaviours. A candidate that passes a novelty threshold enters the archive. The goal is never used to select. (Lehman and Stanley 2011; a01.)

**Quality-diversity (QD).** Return a whole set of solutions, one per niche, each as good as it can be. Diversity comes first and quality second. Pugh, Soros and Stanley (2016) named the field and gave its metrics (a14):
- QD-score: sum of the best quality in each niche.
- Coverage: share of niches filled.
- Reliability and precision: how consistently runs reach good cells.
- Alignment: whether the behaviour descriptor relates to quality.

The simplest QD algorithm is **MAP-Elites** (Mouret and Clune 2015; a08). The designer picks two or more descriptor dimensions and cuts them into a grid. Each cell keeps only its best occupant. The loop is: pick a random filled cell, mutate its elite, measure descriptor and quality, put the child in its cell if the cell is empty or the child is better.

**Why it matters for us.** Our agent has a known weakness: samples from one model are alike (G4), and early output fixes later output. QD is the best-developed body of method for forcing a search to cover a space and to keep weak-looking stepping stones. The open question is whether any of it pays on tasks with one right answer, at equal tokens. The honest summary after this study: the machinery is proven on code, maths constructions, robot control, red-teaming and creative writing. It is untested on reasoning items with a single answer (K16). Several cheap pieces transfer without the whole archive.

**Parts of a QD system, in plain words**

| Part | Job | Who does it in an LLM loop |
|---|---|---|
| Variation operator | make a new candidate from parents | the model |
| Descriptor | place the candidate in a cell | code (computed) or the model (labelled) |
| Quality score | rate the candidate | code check, or a model judge (risky) |
| Archive | store one elite per cell | code |
| Parent selection | choose which elite to vary | code (uniform random works well) |
| Dedup / filter | refuse near-copies | code (embedding or text similarity) |

---

## 2. History and theories in depth

### 2.1 The deception argument (2008-2011)
Lehman and Stanley's argument: for hard problems the objective is deceptive. Steps that improve the score lead into dead ends, and the real path goes through steps that look worse. A search that follows the score gets stuck. A search that rewards only difference keeps finding new stepping stones, and some lead to the goal. Their popular book (Stanley and Lehman 2015, a32) states the stepping-stone rationale. It was seen only in a listing, not read, so it is not used as evidence.

The key experiment (a01-a07, b01-b04) used NEAT-evolved robots in mazes. The behaviour descriptor was the final position. Results are in section 3. The summary: on a hand-built deceptive maze, fitness search was no better than random and novelty solved 39 of 40 runs. On an easy maze both worked but novelty was about 3x faster. With walls removed (unbounded behaviour space) novelty lost its edge.

The authors named the limit themselves (a07, b04): "novelty search effectively finds approximate solutions, while objective optimization is good for tuning approximate solutions." They proposed combining the two. This is the root of every later hybrid.

### 2.2 Local competition and illumination (2011-2015)
Novelty search with local competition (NSLC; Lehman and Stanley 2011 GECCO, a33, not read) added a quality rule: rank quality only against behavioural neighbours. MAP-Elites (a08-a11, b05-b07) made the same idea simpler: a grid, one elite per cell, random parent. It was called an illumination algorithm because it shows how performance varies across a feature space.

Mouret and Clune's lineage analysis (a10, b07) gave the stepping-stone evidence: most elites descend from nearby cells, but many high performers descend from a good neighbour a medium distance away, and whole lineages cross many regions. No sampled organism had a parent more than halfway across the map. Biasing parent choice toward cells with empty neighbours or near high performers did not beat uniform random parent choice in preliminary tests.

### 2.3 Critiques and boundary conditions (2011-2016)
- **Kistemaker and Whiteson 2011** (a17, a18, b10, b11): novelty search depends strongly on the behaviour function. They conclude it moves the prior from the fitness function into the descriptor, and that finding a good descriptor "may be as difficult as solving the optimization problem itself." Removing irrelevant or over-discriminating behaviour dimensions sped search a lot. A secondhand report in the same paper says a high-dimensional descriptor did not break novelty search on one maze, so dimension count is not the whole story.
- **Pugh et al. 2016** (a14-a16, b08, b09): the descriptor must align with quality. An unaligned descriptor was worse than plain fitness. A blend of aligned and unaligned descriptors balanced both aims.
- **Mouret and Clune's own negative result** (b06): on soft robots MAP-Elites did not beat controls on the best single solution and was worse on precision.

### 2.4 QD gets a stronger engine (2015-2020)
- **Robots that adapt like animals** (Cully et al. 2015; a19, a20): a 13,000-entry map of hexapod gaits built in simulation served as a prior. After damage, a Bayesian optimiser searched the map and recovered in about 8 trials. The map cost about two weeks.
- **CMA-ME** (Fontaine et al. 2020; a12, a13): replace random mutation with adaptive CMA-ES emitters that are rewarded for filling new cells or improving cells. Large gains on continuous problems.

### 2.5 Competing explanations and rival fixes (2018-2023)
- **Hybrid with a switch rule** (Conti et al. 2018, NSRA-ES; d13, d14): reward-first, add novelty on stagnation.
- **Fixed hand-off** (Colas et al. 2018, GEP-PG; d15): explore first, then give the buffer to an exploiter.
- **No explicit diversity at all** (Boldi, Ding, Spector 2023; d16): lexicase selection over many sub-objectives beat MAP-Elites on deceptive domains. This is the main rival explanation. Diversity can come for free from scoring on many separate sub-checks.
- **Smoothness** (Chenu et al. 2021; d17): diversity search explores well only if similar policies give similar descriptors.

### 2.6 The LLM turn (2022-2026)
Language models changed what the variation operator can do. An LLM can make several coupled edits at once and can rewrite in meaningful ways.

| Year | System | Role of the model | What it showed |
|---|---|---|---|
| 2022 | ELM (Lehman et al.) | code-diff mutation inside MAP-Elites | fills a 1,728-niche map from one seed (a21-a23) |
| 2023 | LMX (Meyerson et al.) | few-shot crossover | validity depends on size, parent count, order (c06, c07) |
| 2023 | QDAIF (Bradley et al.) | mutate, rate quality, label descriptor | beats baselines by AI judge; ties a fixed prompt by human judge (a24-a27) |
| 2023 | OMNI (Zhang, Lehman, Stanley, Clune) | model of interestingness | filters tasks; 82 tasks learned vs 55 (a28, b27) |
| 2024 | Rainbow Teaming (Samvelyan et al.) | mutator + judge in a 2-D archive | stepping stones matter; beats PAIR (b18-b20, d01) |
| 2024 | In-context QD (Lim et al.) | whole archive in the prompt | works on synthetic tasks (b21, b22, c15) |
| 2024 | FunSearch (Romera-Paredes et al.) | program variants, islands | cap set 512; low per-run success (a29, c24) |
| 2025 | AlphaEvolve (Novikov et al.) | whole-file evolution, MAP-Elites + islands | 75% match, 20% improve on 50+ problems (a30, a31) |
| 2025 | Mind Evolution (Lee et al.) | islands over plans with critic | 95.6% vs 55.6% best-of-N on TravelPlanner (c22-c23, d03) |
| 2025 | ShinkaEvolve, CodeEvolve | open code evolution with ablations | embedding dedup helps (b24, b25, d09) |
| 2025 | NoveltyBench, Artificial Hivemind | measure LLM diversity | low diversity, models agree (c18-c20) |
| 2026 | LEVI, DEI, Land, PRM stress test | small-team preprints | seeding, model mix, ARC channels, judge hacking (b26, d06, d07, d12) |

### 2.7 Theories in one list
1. **Deception theory**: objectives mislead; stepping stones come from difference. Strongest evidence is a hand-built maze (K01).
2. **Descriptor-as-prior theory**: novelty is not free; the prior sits in the descriptor (K03).
3. **Illumination theory**: knowing the whole performance landscape is valuable in itself. Gains show up in coverage and reliability, not in the best single answer (K04).
4. **Multi-objective rival**: many sub-checks give diversity without an archive (K21).
5. **Operator theory for LLMs**: the model's meaningful rewrite, not the archive, may carry most of the gain (b12).

---

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree (claims.jsonl); single-source; contested = sources disagree or rival explanation exists. "Source" gives evidence ids and the claim id.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Novelty beats fitness on a deceptive maze | Hard maze, 40 runs: fitness 3/40, random 4/40, novelty 39/40 (35,109 evals, sd 30,236, cap 250,000) | a03, b02; K01 | established (but hand-built maze; Pugh uses same family) |
| Novelty is about 3x faster on a mild maze | Medium maze, 40 runs: novelty 18,274 evals (sd 20,447) vs fitness 56,334 (sd 48,705), p<0.001; random solved 21/40 | a02, b01; K01 | established |
| Novelty loses its edge when behaviour space is unbounded | Unenclosed maze, 100 runs: novelty 5/100, fitness 2/100, not significant | b03; K02 | established |
| Novelty helps the tail in walking | Biped, 50 runs: 4.04 m (sd 2.57) vs 2.88 m (sd 1.04), p<0.01; best 13.7 m vs 6.8 m; 80% of novelty runs found oscillatory gaits | a06, b04; K02 | single paper, see K02 for hybrid evidence |
| Pure novelty loses where the objective is not deceptive | Humanoid: ES beat NS-ES and NSR-ES, p<0.05 each, after 600 generations; in many Atari games novelty alone gave no higher reward; ES truly stuck in 5 of 12 Atari games | d14, d13; K02, K21 | established |
| Coarse descriptors are enough | Discretised maze end point: 960 runs, 4 failed in 500,000 evals; 4x4 grid (16 behaviours) about 3x slower (117,107 evals) but still better than fitness | a05; K03 | single-source |
| Bounded archive does not hurt | Archive limited to 250: 40/40 solved, 38,324 evals (sd 42,229), no significant difference | a04 | single-source |
| Aligned descriptor beats fitness; unaligned is worse | Endpoint descriptors beat fitness p<0.001; direction descriptor worse than fitness p<0.05; symmetric gauntlet only 2 of 20 runs solved by any direction variant; 15 treatments x 20 runs x 3 mazes | a15, b08; K03 | established |
| Over-fine or irrelevant behaviour dimensions slow search | Evals 63,440 to 27,427 when over-discrimination removed; 21 of 70 runs failed with 3 behaviour points, 29 of 70 with 4 | a17, b10; K03 | established |
| MAP-Elites wins on coverage, reliability | Retina, 20 runs, equal evals: p<1e-7 on all four criteria vs EA, NSLC, random; random second on coverage. Soft robots: reliability and coverage p<0.002, global performance p>0.05, precision worse p<0.01 | a09, b05, b06; K04 | single-source |
| Blend of aligned and unaligned descriptors | MEPGD (30% acceptance of worse in a second slot) beat plain MAP-Elites on both gauntlets; NS_eNSLC_d tied NSLC_e on QD-score (p=0.163) | a16, b09 | single-source (Pugh not re-verified) |
| Adaptive emitters inside the archive | Sphere n=20 cells filled: CMA-ES 3.46%, MAP-Elites 56.22%, ME(line) 68.99%, CMA-ME(rd) 90.32%, CMA-ME(imp) 87.75%. n=100: 3.74 / 26.97 / 31.75 / 77.12 / 61.98%. Hearthstone QD-score 16,024.8 / 25,936.0 / 28,132.7 / 63,295.6; win rate 44.8 / 45.2 / 50.5 / 65.9% | a12, a13; K05 | single-source |
| Archive as prior for repair | Hexapod 13,000 gaits, 240 experiments: leg missing 0.21 vs 0.04 m/s; median 66 s, 8 trials; 20-trial cap hit in 2 of 240; map cost about 2 weeks | a19, a20; K15 | single-source |
| LLM mutation handles coupled edits | 4-Parity, 1-5 bugs, 300M model: GP mutation success falls exponentially to zero at five bugs; diff model degrades only at five. ELM: 1,728 niches, 1,024,000 evals per run, 3 runs per seed | a21, a22, b12, b13; K06 | established (figure-only) |
| LMX order sensitivity | About 30% valid with the 6B model in Sodarace; single parent gave no valid offspring; validity varied over 50% with parent order | c06, c07; K06 | established |
| QDAIF: AI-judged win, human-judged tie | Human QD: QDAIF 0.772, Fixed-Few-Shot 0.767, Shuffling 0.696, LMX quality-only 0.650, Random 0.606. Quality: 3.900 vs 4.133 (fixed higher). Agreement 0.833 vs human-human 0.800. One median-QD run per method | a25, b15, c02; K07 | established |
| Judge-hacking at the top of the scale | AI-human quality correlation breaks at AI scores 0.995-1; annotators differed by 2-3 units in 15% and 5% of cases | a26, b17, c04; K07 | established (cause is suspicion) |
| Poetry with GPT-4 | 200 iterations: QDAIF QD 130 (CI 118-145), Random-Poems 76 (67-85), Fixed Seed Rewrite 99 (72-117); targeted baseline naming a genre matched the guided variant | a27, c05; K07 | single-source |
| Stepping stones matter | Rainbow Teaming Q&A: fitness 0.91, coverage 0.97, self-BLEU 0.50 vs 0.79, 0.90, 0.60 without stepping stones | b18, c13; K08 | established (authors' own systems) |
| Similarity filter trades success for diversity | Filter on vs off (3 runs): ASR 0.92 vs 0.99; self-BLEU 0.42 vs 0.79; ROUGE-L 0.15 vs 0.39; gzip 3.10 vs 6.35; threshold 0.6 drops about 24% of mutants | b19, c13; K12 | established |
| Embedding dedup improves sample efficiency | Cosine over 0.95 rejected; LLM novelty judge marginal; 150 samples to reach 2.635983 on circle packing; run count unstated | b25, c26, d09; K09 | established (figure-only) |
| Over-generation is mostly duplicates | 4,000 seed ideas per topic, cosine over 0.8: about 200 unique (about 5%) | c16; K09 | single paper |
| Rainbow Teaming vs PAIR (corrected) | Llama Guard: 66 jailbreaks over 41 behaviours vs 14/11 for PAIR with same mutator; JBB classifier 8/7 vs 1/1; self-BLEU 0.51 vs 0.74. PAIR got 2,000 prompts, RT 1,000; no restarts | d01; K18 | single-source |
| Judge dominates cost | 7 calls per iteration (2 mutator, 1 target, 4 judge): judge 57%; 14,000 batched calls per run; about two days on 128-256 A100s; judge agreement 78-83% | d02; K19 | single-source |
| Island structure on planning | TravelPlanner (Gemini 1.5 Flash): 1-pass 5.6%, Best-of-N 100/180 = 55.6%, Sequential-Revision+ 149/180 = 82.8%, Mind Evolution 172/180 = 95.6%. Trip Planning 308/320 = 96.2% (vs 77.2 / 74.4). Meeting 425/500 = 85.0% (vs 69.4 / 62.0). Islands 87.5% vs 77.4% (4x5 vs 1x20) | c22, c23, d03; K11 | established, needs programmatic checker |
| Where Mind Evolution's gain comes from | Ablation columns 46.1% to 95.6% as critic, strategy prompts, textual feedback and island reset are added. Critic and evaluator feedback matter most. Table columns garbled; only end points safe | d03; K11 | single-source on split |
| Token parity in Mind Evolution | TravelPlanner input tokens: best-of-N 3.10M vs ME about 3.02-3.05M (two readable cells) | d04 | single-source |
| Plain sampling fails on rare conjunctions | StegPoet: 1-pass 0/101, Best-of-N 1/101 | d04 | single-source |
| FunSearch is high variance | Cap set 512 in 4 of 140 experiments; capacity bound 2.2202 (prev 2.2180); bin packing Weibull 100k 0.03% excess vs best-fit 3.79% | a29, c24; K11 | single-source (ablations in supplement unread) |
| AlphaEvolve | 50+ open problems: matched 75%, improved 20%; rank-48 for 4x4 complex matrices; 0.7% fleet compute; evolution ablation = no database, 3 seeds, figure only | a30, a31, b23, d08; K11 | established that evolution helps; archive share unknown |
| CodeEvolve / ShinkaEvolve / LEVI ablations | All favour the diverse variant (3-10 runs, authors' own). Heavy island migration hurt. LEVI: removing diverse seeds Transaction Scheduling 68.3 to 62.8, Spot 50.2 to 42.3; no-large-models beat full on one task 67.4 vs 64.7. CodeEvolve lost to EoH on one benchmark | b24-b26, b28; K08 | established in direction, weak in size |
| LLM sampling diversity is low | 20 models, 1,100 prompts, 10 samples at temp 1: most models under 3 distinct of 10; cross-model similarity 71-82%; within-model similarity over 0.8 for 79% of queries | c18, c20; K10 | established |
| Show prior answers to lift diversity | In-context regeneration reaches about human diversity (8 human authors); paraphrase and system prompt marginal; figure-only | c19, d05; K10 | established |
| Heterogeneous model mix can widen an archive | Core War, equal calls: diverse 4-model merged QD 45.90, coverage 80.6%; solo 20.46 / 63.0%; same-model 4 nodes 29.85 / 59.0% | d06; K10 | single-source, company preprint |
| Coverage is easy; selection is the bottleneck | MATH, Llama-3-8B: coverage 82.9% to 98.44% (100 to 10,000 samples); majority vote or reward model 40.50% to 41.41%; SWE-bench Lite 15.9% to 56% with tests | d10; K17 | established |
| Optimising a proxy judge lowers true score | Gold score rises then falls; best-of-n form R = d(alpha - beta d) | d11; K17 | established |
| Learned PRM is hackable | Mean pooling 44 strict exploits vs min readout 1; max gain 0.294; problem-level exploit rate 0.232 [0.146, 0.329] | d12; K17 | single-source (preprint) |
| Switch rule from control | NSRA-ES: start reward-only, cut reward weight 0.05 after 50 generations without a new best; beat ES on 8/12 Atari games, best on 5/12; weight change every 50 generations stayed trapped in Seaquest, every 10 escaped. GEP-PG stable over 100-600 exploration episodes; Half-Cheetah 5,740 (std 573) vs DDPG 4,961 (1,288), GEP alone 2,105; Mountain Car DDPG reached goal in 42% or 22% of trials | d13, d15; K20 | supported in control only |
| Lexicase rival | Lexicase over 16 and 64 sub-objectives beat MAP-Elites on deceptive maze and tour, 10 replicates; on non-deceptive maze all reached optimum | d16; K21 | contested (workshop paper) |
| ARC, closest diversity-first loop | Independent text, image, code candidates (up to 29 per task) + one judge reading all traces: 76.1% public ($19.69/task), 72.9% semi-private ($38.99/task); judge beat majority vote by net +7 tasks, all minority recoveries; synthesis +1 | d07; K22 | single-source, no ablations |
| OMNI | Crafter 100M steps, 10 seeds: tasks learned uniform 4, learning progress 55, OMNI 82; interesting tasks 3 / 9 / 14 of 15; success 0.103 / 0.52 / 0.78; BabyAI 1 / 4 / 8; AI2-THOR 0 / 2 / 13 | a28, b27; K13 | single-source (c27 is the same paper) |
| LLMatic | CIFAR-10 94.26 vs random search 93.70, GENIUS 93.79, optimum 94.47; CIFAR-100 71.62 vs 71.04; larger variance (SD 1.73 vs 0.72) | c11 | single-source; gain over random is small |
| Si et al. ideas | N=49 per condition, 79 reviewers, 298 reviews: novelty 4.84 human, 5.64 AI, 5.81 AI reranked | c17 | single-source (mixed-effects tests) |
| Archive in prompt | Fitness-only prompt finds best solution but poor coverage; features-plus-fitness templates best; sorting by distance to target descriptor most consistent; coverage about equal on BBOB | b21, b22, c15; K14 | single-source (Mistral-7B, figure-only) |
| Descriptor labeller agreement | Judge agreement with humans 78-83% (100 pairs) vs human-human 83%; QDAIF diversity labels 0.833 vs 0.800 | d02, a25; K13, K23 | single-source; no reasoning-method study |

---

## 4. Mechanisms and models

Each recipe is code-first. The model fills a slot only.

### 4.1 Novelty score (Lehman and Stanley)
```
novelty(x) = mean distance from b(x) to its k nearest neighbours
             in (current population U archive)
k = 15 in the paper. Archive entry if novelty(x) > threshold.
Threshold started at 6.0 (maze), 1.0 (biped), adjusted during the run.
Selection uses novelty only. The goal is checked, never selected on.
```
Cost note: neighbour search grows with archive size (a07). Bounding the archive to the population size (250) did not hurt on the hard maze (a04).

For an agent: b(x) is a vector or label for the attempt (method class, first step, answer cluster). Distance can be 0/1 on labels or embedding distance. Solve detection stays an outside check.

### 4.2 MAP-Elites (Mouret and Clune)
```
archive = {}                      # key: descriptor cell, value: (candidate, quality)
seed archive with several structurally different starts   # b13, b26: seeding matters
loop until budget:
    parent = uniform random filled cell                   # b07: fancy selection did not help
    child  = vary(parent)                                  # model slot
    cell   = descriptor(child)                             # code or labelled
    q      = quality(child)                                # code check where possible
    if cell empty or q > archive[cell].quality: archive[cell] = (child, q)
```
Variants:
- **Second slot per cell** accepting worse individuals 30% of the time (MEPGD; a16): helped on both gauntlets.
- **Bounded cells**: 2 or more dimensions; cell count grows exponentially with dimensions (a08).
- **Quality dial**: keep entries above a percentage of the cell best (ELM: 80% cut gave 95K examples, higher quality, less diverse; 50% gave 280K; a23).

### 4.3 QD-score and coverage
QD-score = sum over filled cells of the cell's best quality (QDAIF maximum is 20 for 1-D and 100 for 2-D archives; a24). Coverage = filled cells / total cells. Report both with best-single-answer accuracy, because QD gains are mostly in the first two (K04).

### 4.4 Descriptor design (the main lever)
Rules distilled from a05, a15, a17, b08, b10, d17:
1. Aligned with success: cells should differ in the way that predicts a right answer. An unaligned axis is worse than none (p<0.05).
2. Merge ideas with the same prospects: coarse cells that group items with similar future outcomes cut cost by more than 2x; cells that merge unlike items hurt (b10).
3. Smooth: small edits should give small descriptor changes (d17).
4. Small is fine: 16 cells still worked in the maze (a05).
5. Bounded: an unbounded behaviour space removed the novelty edge (b03).
6. Optional two-descriptor design: one tied to success, one for style (a16).

Candidate descriptors for reasoning items (all untested): method class (algebra, enumeration, analogy, construction), first-step choice, representation used, answer cluster.

### 4.5 LLM operators
- **Diff or rewrite mutation (ELM, QDAIF)**: one parent in, one child out.
- **Few-shot crossover (LMX)**: 2-3 parents in the prompt. Shuffle and record parent order; validity swung over 50% with order (c06). Nearest-neighbour parents (LMX-Near) beat random pairs (c07). Validity checked by code before archive insert.
- **Archive in context (Lim et al.)**: show each stored solution with descriptor and score; sort by distance to the target descriptor. Fitness-only prompts lose coverage (b22).
- **Name the empty cell**: code picks an empty cell and says it in the prompt. In poetry this matched evolution toward the cell (a27, c05).

### 4.6 Filters
- **Embedding gate**: reject a proposal with cosine similarity over 0.95 to an existing program (ShinkaEvolve). The extra LLM novelty judge added little (b25, d09). For idea text, Si et al. used 0.8 on sentence embeddings (c16). Thresholds depend on the encoder and domain; sweep them.
- **Parent-child similarity gate**: threshold 0.6 dropped about 24% of mutants; success 0.92 vs 0.99, self-BLEU 0.42 vs 0.79 (b19).

### 4.7 Islands and resets
FunSearch: several islands that do not share; every 4 hours the worst half are reset from a survivor; prompts hold k=2 programs (a29). Mind Evolution: 4 islands x 5 conversations, with a critic and evaluator feedback (c23). CodeEvolve: heavy migration between islands reduced diversity and hurt; cycle topology was the one that passed AlphaEvolve (b24).

For an agent: an island is a line of attempts that does not see the others' text. This is the same as S3's fresh-context-per-attempt rule, extended over several rounds.

### 4.8 Emitters (CMA-ME style)
A parent chooser rewarded for what it produces: filling an empty cell or improving a cell (a12). Ties to the bandits subfield. In Mouret and Clune, uniform random choice was as good in the retina task (b07), so start uniform and add adaptation only if a test shows gain.

### 4.9 Explore-then-exploit switch
- **Stagnation counter (NSRA-ES; d13)**: weight on reward starts at 1.0; after 50 generations without a new best, lower it by 0.05; raise when a new best appears. Window length mattered: 50 stayed trapped, 10 escaped.
- **Fixed hand-off (GEP-PG; d15)**: exploration fills the buffer, then the exploiter takes over; stable over 100-600 exploration episodes.
- Our translation (untested): after k failed attempts with no improvement, force a different method; after a check passes, refine only from the failing output (G2).

### 4.10 Verifier-based selection
Coverage is easy and selection is hard (d10). With a hard check, repeated diverse sampling turns coverage into success (SWE-bench Lite 15.9% to 56%). With a model judge or reward model, selection plateaus near 41% on MATH while coverage reaches 98%. Judges can be hacked: min-style readout of step scores had 1 exploit where mean pooling had 44 (d12). Gao et al. give the shape of over-optimisation (d11).

### 4.11 Per-case selection (rival)
Lexicase: score each candidate on each test case, pick by random case order. Diversity arises without a descriptor (d16). Implementable in a few lines when items have several test cases.

---

## 5. What holds up

### 5.1 Holds up (two or more sources, or large effects)
- **Deception is real and novelty can fix it** on built-to-deceive domains (K01). Caveat: the maze family is shared by Lehman and Stanley and Pugh.
- **Descriptor alignment decides the sign of the effect** (K03; a15, a17).
- **Novelty has costs when the objective works** (K02, K21; d14).
- **Repeated sampling from one model is not diverse** (K10; c16, c18, c20). Only about 5% of 4,000 ideas survived dedup.
- **Showing the model its previous answers lifts distinct output** (c19, d05). Temperature, paraphrase and creativity prompts do not.
- **Embedding dedup in code beats an LLM novelty judge** (K09; b25, d09).
- **A model judge cannot be the selector** at the top of its scale (K07, K17): QDAIF judge hacking, MATH selection plateau, PRM exploits.
- **Reusing earlier attempts beats resampling from the start** (K08; b18, b24, b25, a31).
- **Quality and diversity trade off with a dial that code can set** (K12).

### 5.2 Failures, nulls and negative results
| Result | Source |
|---|---|
| Unenclosed maze: novelty 5/100 vs fitness 2/100 (n.s.) | b03 |
| Unaligned descriptor worse than fitness (p<0.05); 2 of 20 solved on the symmetric gauntlet | a15, b08 |
| MAP-Elites no better on best single solution (soft robots, p>0.05); precision worse (p<0.01) | b06 |
| Plain MAP-Elites outlier runs (791K, 680K, 421K vs 950K-1000K QD) | b09 |
| QDAIF ties a fixed few-shot prompt under human judgement; lower human quality (3.90 vs 4.13) | a25, c02 |
| QDAIF mutator size 13B/30B/70B unrelated to QD score; more diversity-judge examples raised human quality but increased human-AI genre disagreement | c04 |
| QDAIF poetry: targeted-prompt baseline matched guided variant | a27, c05 |
| Pure novelty lost to ES on humanoid (p<0.05) and most Atari games | d14 |
| In-context QD: coverage about equal on BBOB; struggles when fitness-descriptor patterns are unclear | b21, c15 |
| CMA-ME(opt) emitter did badly (12.5% and 2.7% cells) | a12 |
| ELM downstream RL brittle; another distillation approach "did not work" (appendix unread) | b14, b13 |
| LLMatic: gain over random search small (94.26 vs 93.70) | c11 |
| CodeEvolve lost to EoH on one bin-packing benchmark (gap 4.18% to 3.38% vs 2.24% to 0.61%) | b24 |
| LEVI: no-large-models beat full on Transaction Scheduling (67.4 vs 64.7) | b26 |
| FunSearch: only 4 of 140 runs found the 512 cap set | a29, c24 |
| No source found that failed to replicate the Lehman-Stanley maze | critique, gap 9 |

### 5.3 Moderators
- **Deceptiveness of the objective**: the larger the trap, the larger the gain (b09: easy maze QD close; hardest maze aligned descriptor clearly better).
- **Descriptor alignment, smoothness, boundedness** (section 4.4).
- **Evaluator quality**: Mind Evolution's gain depends on a programmatic evaluator and textual feedback (d03). Brown et al.: selection quality bounds the gain (d10).
- **Seed diversity**: seed choice shaped the archive (ELM b13; LEVI largest single loss b26).
- **Model size**: LMX validity rises with size (c06); in QDAIF mutator size did not move QD score but raised human quality (c04, b17).
- **Task type**: archive helps on illumination tasks, not on best-single-answer tasks (b06).
- **Budget**: effects were measured at equal evaluations, not equal tokens (critique weak spot).

### 5.4 Interventions that worked / did not
| Worked | Did not work (or not shown) |
|---|---|
| Aligned descriptor | Unaligned descriptor |
| Reusing archive entries as parents | Biasing parent choice toward empty-neighbour cells (b07) |
| Embedding dedup | LLM novelty judge (marginal) |
| Showing earlier answers | Temperature, paraphrase, creativity system prompt |
| Seeds from several families | Heavy island migration (b24) |
| Stagnation-triggered weight change (every 10 gens) | Same rule with a 50-generation window (stuck in Seaquest) |
| Min-style readout of step scores | Mean pooling of PRM scores |
| Judge that reads all traces (ARC, +7 over majority vote) | Majority vote or reward model selection on MATH (plateau) |

### 5.5 What is still not tested
Per the critique's ten gaps: an archive vs best-of-N at equal tokens on reasoning (gap 1, open), cheapest aligned descriptor and labeller agreement (gap 3, open), give-a-different-one vs archive (gap 6, open), archive share of AlphaEvolve and FunSearch (gap 8, open), PAIR with restarts (gap 7, closed on numbers but restarts missing).

---

## 6. Language models

### 6.1 Baseline behaviour on diversity tasks
- **Few distinct answers**: 20 models, 1,100 prompts, 10 samples at temperature 1. Most models gave under 3 distinct answers out of 10. Claude 3, Gemini and GPT-4o scored below 4 of 10 on cumulative utility. Smaller models (Gemma 2 2B, Llama 3.2 1B) were the most diverse (c18). Classifier agreement with humans 79%; the human reference (8 authors) is a lower bound.
- **Cross-model collapse**: 70+ models, 26,070 queries; average pairwise similarity across models 71-82%; DeepSeek-V3 vs qwen-max 0.82; within-model similarity above 0.8 for 79% of queries at top-p 0.9 temp 1.0; min-p at temp 2.0 still 61.2% of pairs above 0.8 (c20).
- **Idea over-generation**: 4,000 seed ideas per topic; about 200 (5%) after dedup at cosine 0.8; new non-duplicates per batch fall and the cumulative count plateaus (c16).
- **Our own number**: NoveltyBench 3.18 to 9.63 with the open-mode scaffold (SCHEMA.md S3).

### 6.2 What changed it, and by how much
| Intervention | Effect | Source | Caveat |
|---|---|---|---|
| Show previous answers, ask for a different one | about human-level distinct count; GPT-4o and Gemini 2.0 Pro above human cumulative utility | c19, d05 | figure-only; no cost; no solve rate |
| Paraphrase prompt, creativity system prompt | marginal | c19 | |
| Temperature up | little | c20 | |
| Name the target cell in the prompt | matched evolution toward the cell (poetry QD 130 vs targeted baseline equal) | a27, c05 | one task |
| Embedding dedup, cosine 0.95 | "strongly" better than none | b25, c26 | figure-only; seeds unstated |
| Parent-child similarity gate 0.6 | self-BLEU 0.79 to 0.42; ASR 0.99 to 0.92 | b19 | 3 runs |
| Stepping stones | fitness 0.79 to 0.91; self-BLEU 0.60 to 0.50 | b18 | one family |
| Islands, same budget | 77.4% to 87.5% on 10-city trip planning | c23 | single subset |
| Critic and textual evaluator feedback | most of 46.1% to 95.6% on TravelPlanner | d03 | needs programmatic evaluator |
| Heterogeneous models | Core War coverage 59.0% to 80.6% | d06 | preprint; contrasts with c20 |
| Diverse seeds | LEVI: 68.3 to 62.8 and 50.2 to 42.3 when removed | b26 | single author |
| Larger mutator | no QD-score effect; higher human quality | c04, b17 | |

### 6.3 Search structure on language-model reasoning
Mind Evolution is the only structural test on natural-language planning. At Gemini 1.5 Flash: 95.6% vs 55.6% (best-of-N) and 82.8% (sequential revision+). The authors say best-of-N fails because it cannot learn implicit constraints from evaluator feedback (d03). Token use was about equal on TravelPlanner (3.0M vs 3.1M input tokens, two readable cells; d04). StegPoet showed plain sampling collapses on rare conjunctions (1/101). A model-only verifier was not tested.

### 6.4 The judge problem
- QDAIF: AI-judged win, human-judged tie.
- Rainbow Teaming: judge is 4 of 7 calls (57%); human agreement 78-83%.
- Artificial Hivemind: judges and reward models track humans worse when human ratings are close (c21).
- Brown et al.: MATH selection 40.50% to 41.41% while coverage 82.9% to 98.44%.
- PRM stress test: 44 exploits (mean) vs 1 (min).
This is the argument behind G5 and G8 and it is consistent with them.

### 6.5 ARC
Land (2026; d07): independent candidates in text, image and code channels, then one judge reading all traces. 76.1% public at $19.69 per task and 72.9% semi-private at $38.99. The judge gained net +7 tasks over majority vote, all minority recoveries (in one task 12 candidates gave one wrong answer, 8 another, 1 the right one). The author did not run independent-vs-sequential, candidate scaling, modality or judge-count ablations, and there are no confidence intervals. The descriptor is the modality, a hand-chosen coarse label. No archive. This supports "diversify the method channel, then judge by reading", and it does not test an archive.

### 6.6 Compute reality
Rainbow Teaming: 14,000 batched calls, about two days on 128-256 A100s, judged "substantial." FunSearch: about 1e6 samples, 15 samplers, 150 evaluators. AlphaEvolve: strong closed models. Our agent has a token budget and no cheap evaluator on open items. Only the lightweight parts transfer.

---

## 7. What our agent should take

Status marks follow SCHEMA.md. [E] = established (claims.jsonl). [S] = single-source. [C] = contested. "Part" names the schema part: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | **Code-side duplicate filter before spending tokens.** Embed each new attempt or idea; drop it if cosine similarity to a kept one is above a threshold (start 0.95 for code-like text, 0.8 for idea text; sweep). Use no LLM novelty judge. | G5 extension; S3 | [E] K09 | b25, c26, c16, d09 |
| A2 | **In open mode, show the model its earlier answers and ask for a different one** (history is already in S3; this fixes its form). Do not rely on temperature, paraphrase or "be creative." | S3, G4 | [E] K10 | c18, c19, c20, d05 |
| A3 | **Do not diversify by default.** Keep objective pressure first; add exploration only on a signal. Pure novelty loses where the objective works. Confirms G1 and G12. | G1, G12 | [E] K02, K21 | b03, d14, a03 |
| A4 | **Any descriptor or diversity axis must be tied to what makes answers right.** An unaligned axis is worse than none. No style or length axes. | O (axis choice); design rule | [E] K03 | a15, b08, a17, b10 |
| A5 | **A hard check, not a model judge, selects among diverse attempts.** Distrust self-scores at the top of the scale. If a step-score aggregate is used, take the minimum. | G5, G8 (reinforces) | [E] K07, K17 | a26, c04, d10, d11, d12 |
| A6 | **Fixed, recorded order for any multi-attempt prompt** (shown parent or exemplar order); if order is varied, vary it deliberately. Validity swung over 50% with parent order. | G (order robustness); log | [E] K06 | c06, b16 |
| A7 | **Mixed starts, not one seed**: the first round should hold structurally different approaches, since the first idea shapes the archive. | S3 | [E] directionally K08, seed effect in a22, b13, b26 | a22, b13, b26 |
| A8 | **Log distinct-approach count, duplicates dropped, and judge tokens per run.** The judge share was 57% of calls in a QD loop; scoring tokens count inside the equal-token budget. | section 6 logging, G7 | [S] K19 (principle already in G7) | d02, d09 |

### Test first (not yet in the schema)

| # | Item | Part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | **Stagnation counter then forced method change** ("no improvement in k attempts, use a method not yet used"). Sweep k = 2, 4, 8. Measured only in control tasks; the window length decided success. | S6, O | [S] K20 | d13, d15, a07 |
| T2 | **Archive of attempts keyed by a method-class descriptor, parent drawn uniformly from the archive, vs best-of-N at equal tokens.** The central untested claim for reasoning tasks. Expect coverage gain, little or no best-answer gain. | memory, S3, S6 | [S] K04, K16; stepping-stone direction [E] in code domains K08 | a08, b06, b18, b28 |
| T3 | **Island split of attempts** (4 lines x n vs 1 line x 4n) on a verifiable task. | S3 | [E] on planning with checker K11, untested on our items | c23, d03 |
| T4 | **Method-diverse independent attempts, then a judge that reads all traces, vs majority vote.** | S3, S7 | [S] K22 | d07 |
| T5 | **Name the empty cell**: code picks an unused method class and names it in the prompt. Cheapest archive-like design. | S3, O | [S] (poetry only) K13/a27 | a27, c05 |
| T6 | **Per-case selection (lexicase) vs archive**: pick on per-test-case profile. | S7 | [E] that rival exists K21; untested for us | d16 |
| T7 | **Similarity-threshold dial**: sweep the filter threshold, plot solve rate against distinct approaches to find the knee. | G (dial) | [E] K12 trade-off; knee unknown | b19, a23 |
| T8 | **Model labels the approach class of its own attempts; check against a second labeller.** | O | [S] K13, K23 | d02, a25 |
| T9 | **Archive in context with descriptors and scores; sort by distance to the target cell.** | memory | [S] K14 | b22, c15 |
| T10 | **Reuse of earlier attempts as parents (stepping stones) vs restart from the original problem.** | memory | [E] direction, K08; domain mismatch | b18, b25 |
| T11 | **Stored strategy library tried in order after a check fails** vs resampling. | memory, O | [S] K15 | a19 |
| T12 | **Cross-model or cross-persona mix as diversity source.** Against G4 and c20; Core War says otherwise. | S3 | [C] K10 | d06, c20 |

---

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, including judge, labeller and embedding calls (G7). Report solve rate, distinct-approach count, duplicates dropped, tokens per role. Use at least two seeds per item and paired comparison per item. Bench items are the project's ARC and BrainTeaser sets (see `harness/bench.py`), plus NoveltyBench for open mode.

| # | Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|---|
| 1 | Duplicate filter in best-of-N (K09) | ARC, BrainTeaser | (a) plain best-of-N; (b) best-of-N with embedding duplicate filter that skips near-copies and spends the saved tokens on new attempts | solve rate; unique approaches per item; tokens spent on duplicates | small gain in unique count; solve-rate gain only where attempts collapse. Positive if tokens on duplicates are a real share |
| 2 | Archive vs best-of-N (K16, gap 1) | ARC, BrainTeaser | (a) best-of-N; (b) archive keyed by method class, uniform parent, mutation by model; (c) best-of-N with dedup | solve rate; coverage of method classes; solve rate on items where plain pass rate is low but nonzero (G12 foothold) | coverage gain; best-answer gain uncertain. Archive wins only if (c) is beaten |
| 3 | Aligned vs unaligned vs no descriptor (K03) | one family, 40 items | descriptor = method class / answer length or style / none | solve rate | aligned > none > unaligned |
| 4 | Stagnation counter (K20) | ARC items with plain pass rate under 50% | k = 2, 4, 8 versus never switch versus fixed-schedule switch | solve rate; tokens to first pass | k between 2 and 4 wins; fixed schedule loses to signal (G1) |
| 5 | Islands (K11) | verifiable items | 4 lines x 5 vs 1 line x 20 sharing context | solve rate | about +5 to +10 points if the Mind Evolution effect transfers; requires a checker |
| 6 | Judge reads all traces vs vote (K22) | ARC | method-diverse attempts with (a) majority vote, (b) judge reading traces with no authorship or majority shown (G5), (c) code check on held-out part | solve rate; minority-answer recoveries | judge recovers a few minority answers; check on held-out part (G3) beats judge where available |
| 7 | Name-the-empty-cell vs show-prior-answers (K10, gap 6) | NoveltyBench, ARC | (a) independent samples; (b) prior answers shown; (c) code names unused method class; (d) full archive loop | distinct count; solve rate; tokens | (b) and (c) capture most of (d)'s distinct-count gain at lower cost |
| 8 | Lexicase-style per-case selection (K21) | items with multiple test cases | (a) archive loop; (b) per-case selection at same budget | solve rate | similar; if (b) matches (a), skip the archive |
| 9 | Judge vs verifier (K17, gap 5) | code or maths items | model judge picks vs held-out test picks, same diverse pool | solved count; AI-true quality gap | verifier beats judge; report gap size |
| 10 | Labeller agreement (K23, gap 3) | 100 attempts | two labelling prompts plus a human sample | agreement; correlation of class with success | agreement near 80% would be usable; below 70% means descriptor is too noisy |
| 11 | Threshold dial (K12) | ARC | filter thresholds 0.6, 0.8, 0.95 | solve rate vs distinct approaches | knee near 0.8-0.95 |
| 12 | Strategy library on failure (K15) | ARC | try stored strategy list in order after a failed check vs resample | solve rate | gain when classes repeat |

Run 1, 2 and 4 first (see UNKNOWNS.md).

---

## 9. What does not transfer, and why

1. **Hand-built deception.** The decisive maze was built to deceive. Real reasoning items rarely announce deception, and only 5 of 12 Atari games were truly deceptive (d14). Pure novelty lost on non-deceptive tasks.
2. **Cheap code descriptors.** Robot position, gait contact pattern or program size are computed. A reasoning attempt has no such descriptor; the model must label it, at 78-83% agreement in the best case seen (d02), and nobody measured it for reasoning methods.
3. **Illumination goals.** MAP-Elites optimises coverage of a map. Our agent is paid on one correct answer. Mouret and Clune said directly that for a single high-performing solution there would be no statistical difference (b06).
4. **Compute scale.** Cully's map took two weeks. Rainbow Teaming ran about two days on 128-256 A100s. FunSearch used about 1e6 samples. We have a token budget per item.
5. **Cheap automatic scorers.** Code, circle packing, jailbreak classifiers and Core War all have one. Open reasoning questions usually do not. The one natural-language planning gain (Mind Evolution) needs a programmatic evaluator and most of its gain came from the critic and feedback (d03).
6. **Training steps.** ELM fine-tuning, Rainbow Teaming SFT (92% to 0.3% ASR) and CMA-ME emitter learning are training or inner-optimiser steps. We do not train. Only the dataset-as-demonstrations idea carries over as few-shot memory.
7. **Model mixing.** DEI got coverage from a 4-model mix (80.6% vs 59.0%). We have one model. Artificial Hivemind says models agree with each other (71-82%), so a mix may not give independence anyway.
8. **Equal evaluations are not equal tokens.** Nearly all comparisons are at equal evaluations. Judge, labeller and embedding calls add cost not counted in those results.
9. **Authors' own systems with few seeds.** CodeEvolve, ShinkaEvolve, LEVI, AlphaEvolve ablations have 3 seeds or unstated counts. Direction transfers; sizes do not.
10. **Interestingness.** OMNI's gains came from synthetic boring tasks and a built oracle; the LM's agreement with humans was never measured (b27). Do not use a model's "is it interesting" as a selector (G8).
11. **Debate-like island sharing.** Heavy migration hurt (b24). G9 already bans debate.

---

## 10. Open questions

1. At equal tokens, does an archive-and-descriptor loop beat best-of-N, and best-of-N with a duplicate filter, on reasoning items with one right answer? (gap 1)
2. How much of Mind Evolution's gain over best-of-N comes from islands, from the critic and feedback, and from recombination, with a model-only verifier? (gap 2; most of the gain looks like feedback)
3. What is the cheapest descriptor for reasoning attempts that is aligned with success, and how reliable is model labelling? (gap 3)
4. Is there a measured explore-then-exploit switch for a token-limited agent? (gap 4; only control-task rules exist)
5. How big is the judge-vs-verifier gap for diversity scores on code or maths, as opposed to reward-model selection? (gap 5)
6. Does "show the previous answers" match a full archive loop in distinct approaches and solve rate at lower token cost? (gap 6)
7. Does the QD gain over PAIR survive when PAIR gets restarts at the same budget? (gap 7; RT had half the prompts but PAIR had no restarts)
8. How much of AlphaEvolve and FunSearch is the MAP-Elites or island database? (gap 8)
9. Are there failed replications of novelty search on real, non-hand-built deceptive domains? None found. (gap 9)
10. What share of a QD loop's tokens goes to descriptor labelling, judging and embedding? (gap 10; judge is 4 of 7 calls; the rest unreported)
11. Is the lexicase explanation (many sub-objectives give diversity for free) the real mechanism for LLM loops with several test cases?
12. Does model heterogeneity matter inside one model via personas or strategies? NoveltyBench and Artificial Hivemind say no; Core War says yes.
13. Do QD archives raise accuracy at all when the task has one answer, or only the number of distinct valid answers?

---

## 11. Sources

[V] = opened and read this session (full PDF, HTML or fetched text; some read through a fetch summary of the first 100k characters, noted). [M] = snippet, listing or citation only.

| Source | Mark | URL | Notes |
|---|---|---|---|
| Lehman and Stanley (2011) Abandoning objectives: evolution through the search for novelty alone | [V] | https://www.cs.swarthmore.edu/~meeden/cs81/f17/papers/lehman_ecj11.pdf | numbers re-checked in critique |
| Mouret and Clune (2015) Illuminating search spaces by mapping elites | [V] | https://arxiv.org/pdf/1504.04909 | re-checked |
| Fontaine, Togelius, Nikolaidis, Hoover (2020) CMA-ME | [V] | https://arxiv.org/pdf/1912.02400 | re-checked |
| Pugh, Soros, Stanley (2016) Quality diversity: a new frontier | [V] | https://www.frontiersin.org/articles/10.3389/frobt.2016.00040/full | first pass only, first 100k of 145k characters; not re-verified |
| Kistemaker and Whiteson (2011) Critical factors in the performance of novelty search | [V] | https://groups.csail.mit.edu/EVO-DesignOpt/gecco2011Proceedings/proceedings/p965.pdf | |
| Cully, Clune, Tarapore, Mouret (2015) Robots that can adapt like animals | [V] | https://arxiv.org/abs/1407.3501 | first 100k of 169k characters; not re-verified |
| Lehman et al. (2022) Evolution through Large Models | [V] | https://arxiv.org/pdf/2206.08896 | figure-only numbers |
| Meyerson et al. (2023) Language Model Crossover | [V] | https://arxiv.org/abs/2302.12170 | not re-opened by cross-check |
| Bradley et al. (2024) QDAIF | [V] | https://arxiv.org/pdf/2310.13032 | re-checked |
| Zhang, Lehman, Stanley, Clune (2023) OMNI | [V] | https://ar5iv.labs.arxiv.org/html/2306.01711 | c27's "Faldor et al. 2025" label was wrong; same paper as b27. Faldor et al. (OMNI-EPIC) is a different paper, not opened |
| Samvelyan et al. (2024) Rainbow Teaming | [V] | https://arxiv.org/abs/2402.16822 | Table 1 corrected in d01 |
| Lim, Flageat, Cully (2024) LLMs as in-context AI generators for QD | [V] | https://arxiv.org/abs/2404.15794 | not re-opened |
| Nasir et al. (2024) LLMatic | [V] | https://arxiv.org/abs/2306.01102 | not re-opened |
| Romera-Paredes et al. (2024) FunSearch, Nature | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/ | supplement ablations unread |
| Novikov et al. (2025) AlphaEvolve | [V] | https://arxiv.org/pdf/2506.13131 | ablations figure-only |
| CodeEvolve (2025) | [V] | https://arxiv.org/abs/2510.14150 | not re-opened |
| Lange, Imajuku, Cetin (2025) ShinkaEvolve | [V] | https://arxiv.org/abs/2509.19349 | re-checked |
| Tanveer (2026) LEVI | [V] | https://arxiv.org/abs/2605.09764 | single-author preprint; not re-opened |
| Lee et al. (2025) Evolving Deeper LLM Thinking (Mind Evolution) | [V] | https://arxiv.org/abs/2501.09891 | re-checked; ablation table garbled |
| Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? | [V] | https://arxiv.org/abs/2409.04109 | re-checked |
| NoveltyBench (2025) (c18 lists Zhang et al.; d05 lists Vijayakumar et al.; author list not settled) | [V] | https://arxiv.org/abs/2504.05228 | not re-opened |
| Jiang et al. (2025) Artificial Hivemind | [V] | https://arxiv.org/abs/2510.22954 | page-text summary |
| Donaghy and Rastogi (2026) DEI | [V] | https://arxiv.org/abs/2605.27130 | company preprint |
| Land (2026) Modality-driven search with holistic trace judging for ARC-AGI-2 | [V] | https://arxiv.org/abs/2606.31543 | single run |
| Brown et al. (2024) Large Language Monkeys | [V] | https://arxiv.org/abs/2407.21787 | |
| Gao, Schulman, Hilton (2023) Scaling laws for reward model overoptimization | [V] | https://arxiv.org/abs/2210.10760 | |
| Shihab and Afrin (2026) QD stress tests for process reward models | [V] | https://arxiv.org/abs/2608.08008 | preprint |
| Conti et al. (2018) Improving exploration in ES via novelty-seeking agents | [V] | https://arxiv.org/abs/1712.06560 | |
| Colas, Sigaud, Oudeyer (2018) GEP-PG | [V] | https://arxiv.org/abs/1802.05054 | |
| Boldi, Ding, Spector (2023) Objectives are all you need | [V] | https://arxiv.org/abs/2311.02283 | workshop paper |
| Chenu et al. (2021) Selection-Expansion | [V] | https://arxiv.org/abs/2104.04768 | |
| Stanley and Lehman (2015) Why greatness cannot be planned (book) | [M] | https://www.goodreads.com/book/show/25670869-why-greatness-cannot-be-planned | listing only |
| Lehman and Stanley (2011) Evolving a diversity of virtual creatures (NSLC) | [M] | https://doi.org/10.1145/2001576.2001606 | cited by others only |
| Guo et al. (2026) Parameter-efficient neuroevolution for diverse LLM generation | [M] | https://arxiv.org/abs/2605.09781 | title and keywords only |
