# Morphological analysis: deep document

*Subfield E07.04. Key works: Zwicky. Schema hook: S3 open mode, where code enumerates. Evidence ids (a01-a30, b01-b25, c01-c28, d01-d17) and claim ids (K01-K28) refer to the files in this folder. Search was thin: the arXiv, OpenAlex and Semantic Scholar APIs were rate limited, so absence claims mean "not found", not "does not exist".*

## 1. What it is

Morphological analysis builds a list of solutions by table, not by inspiration. You do four things.

1. Split the problem into parameters (also called dimensions or functions). Example for a coffee maker: heat source, water transport, filter, container.
2. List a few values (options) for each parameter.
3. Put them in a grid, the morphological box or Zwicky box. One value from each column is one configuration.
4. Choose configurations, after dropping impossible ones.

The number of configurations is the product of the value counts. Zwicky's telescope example: N = nA x nB x nC ... Six parameters of four values give 4,096 (a12). Zwicky's propulsion box has 4x4x3x3x2x2 = 576 configurations (a06, a12). Zwicky's own small example matches 10 energy forms against 10 in a 10x10 table to list every conversion (a11).

The modern form, general morphological analysis (GMA, Ritchey), adds cross-consistency assessment (CCA). Every pair of values from different parameters is judged once: can these two exist together? A configuration with any incompatible pair is deleted. Pair judgments grow with the square of the parameters, while configurations grow exponentially. Ritchey says a field of about 100,000 configurations needs only a few hundred pair judgments (a02, d12).

Two plain facts matter for our agent.

- The method is decompose-then-recombine. The decomposition is language work. The enumeration is arithmetic, so code can do it. That is why the schema lists it under "code enumerates".
- It targets problems that cannot be put in numbers. It gives no causal or quantitative prediction (b20).

Related schema operators: O3 Decompose, O6 Change representation, O4 Drop a constraint. The box is a structured way to run O3 and then a combinatorial S3.

## 2. History and theories in depth

**Zwicky (1930s to 1974).** Fritz Zwicky was at Caltech from 1927 to 1968 and research director at Aerojet from 1943 to 1961 (a11). He built the method for astrophysics (morphological astronomy, 1948), jet and rocket propulsion (jet-engine work dated 1947 in a06; the 576-configuration box dated 1962 in a12, unresolved) and later space law (a01, a05). His book is Discovery, Invention, Research through the Morphological Approach (1966, 1969) (a05, b22). He used 40 or more dimensions in some studies (a09).

**Zwicky's five steps** (a09): (1) state the problem concisely; (2) locate and analyse all relevant parameters; (3) build the box of all potential solutions; (4) scrutinise and evaluate each solution against the goals; (5) pick and realise the best, iteratively.

**Totality research.** Zwicky wanted all solutions derived without bias (a10). He saw complete coverage as pushing thought to the limits of the conceivable. He claimed the box shows configurations that less structured methods overlook, including "hundreds of unconsidered configurations" in jet engines (b22, second-hand). This is an originator's claim. No one counted (d12, K27).

**Two superimposed tasks.** Zwicky stressed that the method both discards impossible combinations and finds new ones (a12). This is the root of CCA.

**Later engineering use.** Norris (1963) proposed it as an engineering design method with computers (a05, a13). Rhyne (1971, 1981, SRI) used a restricted form for scenarios (a05). Weber and Condor (1989, synergistically compatible matrix), Evbuomwan (1997), Dartnall and Johnston (2005), Jimenez and Mavris (2010) and Zeiler (2009, 2011) are engineering-design uses (a13). Pahl and Beitz teach the morphological chart (called the matrix in engineering design) as a standard step; Bonde 2024 reports their warning that early-phase optimisation over the chart is weak (b24).

**Ritchey and GMA (1995 to 2022).** Tom Ritchey, at the Swedish Defence Research Agency, formalised CCA with three inconsistency types: logical contradiction, empirical implausibility and normative constraint (a03). Normative judgments are kept out of the first pass, to keep "possible" apart from "desirable". He claims more than 100 computer-aided projects since 1995 (a04, b19) and a catalogue of 52 field models from client projects over 22 years (a25). He admits GMA "has been written about and discussed far more than it has actually been used in real client-based projects" (a05). He also applied GMA to itself: five modelling properties give a 64-type field (2x2x2x2x4) (a24).

**Competing theories of why it works.**

- *Coverage theory* (Zwicky): the box makes the whole space visible, so fixation on a favourite is blocked.
- *Combination theory*: new ideas come from recombining parts. Kirjavainen and Holtta-Otto's catalogue lists 25 mechanisms and puts combination in 38 percent of ideation methods and classification in 11 percent (b11).
- *Decomposition theory*: splitting by function makes association easier than free brainstorming (a18).
- *Screening theory* (what students actually do): the matrix is used as a filter against a requirement list, not as a synthesis tool (b06).

**State of the field.** Case reports (about 80 in a 2015 survey, a12) dominate. No controlled study with an effect size shows a box beats free ideation (a30, K04). Human experiments exist only as side comparisons (section 5).

## 3. Core findings with exact numbers

Status: established = two or more independent sources; single-source = one source (advocate, small N or one lab as noted); contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Configurations multiply; pair checks do not | 6 parameters x 4 values = 4,096; 4x4x4x3x3x4 = 2,304; 4x4x3x3x2x2 = 576; 5x5x3 = 75; shelter field of 10 parameters over 500,000 | a02, a06, a12, a01 | established (arithmetic) |
| CCA shrinks fields 90-99 percent | EPR strategy field 34,560 to 480 (98.6 percent removed); scenario field 20,736 with 8 picked to cover every state; 100,000 configs need a few hundred pair judgments | a06, a07, a02 (Ritchey) | single-source, advocate |
| Pair-only CCA misses triple conflicts; groups diverge | Identical fields given to different groups gave diverging CCA; no agreement statistic | a02, a04 | single-source |
| Modern boxes are huge | Student boxes 6,144 to 3.6e13 unconstrained configurations | b02 | established |
| Box users stop at 1-2 combinations, often without a reason | 8 teams (26 people); 5 software teams made 3-64 combinations, 3 traditional teams 1-2; not significant | b01, b03, b21 | single-source (small N) |
| Matrix is used as a screening filter | About 500 students, about 100 projects; 12 of 36 groups answered; majority said it did not help find new solutions | b05, b06 | established (b03, b06, b01) |
| Morphology not better for breadth | N=102: more elaborated concepts than brainstorming, not more concepts or diversity. N=244: fluency /8 morphology 3.58, none 3.90, classification 4.48; flexibility /5 2.54, 2.88, 3.09 (morphology vs none n.s.) | b14, b12 | established (human only) |
| Weak aspects narrow the space | 3x3 table (9 options) flexibility 3/5; 7x7x5 table (245 options) 4/5 | b13 | single-source |
| Combination helps, classification helps as much or more | Exp1 N=61 unique ideas round 2: classify about 3.7 vs combine about 1.8. Exp2 N=57 originality: combine 1.57 to 2.65 (p=0.023), classify 1.89 to 3.22 (p<0.001), no between-group difference (Kruskal-Wallis p=0.445). Quantity fell in all groups (p=0.039, 0.003, <0.001) | b07, b08, b09 | single-source (one lab, 4 experiments) |
| Seeing others' ideas works at least as well as structured stimuli | Exp3 N=35 novelty vs control p=0.001 (building on others), p=0.005 (stimulation); Exp4 N=41 originality p=0.018 | b10 | single-source |
| Morphology loads prefrontal cortex more than TRIZ and brainstorming | N=30; overall F(2,57)=29.5, eta-squared 0.509; vs TRIZ t=7.62; vs brainstorming t=2.94, p=0.013 | a16-a18 | single-source; process proxy, not quality |
| Matrix software output was word strings | First version used by about 500 students; students output auto-generated strings and used them as a filter | b05, b06 | single-source |
| Free LLM ideation saturates | 4,000 seed ideas, dedup at cosine 0.8: about 5 percent (about 200) unique | c06 | established (with c12, a29, c08) |
| LLMs resemble each other | Pairwise similarity over 0.8 in 79 percent of cases; 61.2 percent under min-p; cross-model 71-82 percent | c12 | single-source, large N |
| GPT-4 pools less diverse than human groups | Cosine similarity: human groups 0.243; GPT-4 0.255-0.432; baseline 0.377; chain of thought raised unique ideas from about 3,700 to 4,700 | c08 | established (with d04) |
| Diversity injections (1 minus mean cosine, GPT-4o, 100 ideas) | Humans 0.773; random persona 0.757; random functional constraint 0.735; chain of thought 0.698; plain 0.679; serial "bolder" x2 0.575; independent one-idea sessions 0.452 | d04 | single-source |
| Pooling vendors reaches human diversity | Pool of 4 vendors 0.763 vs humans 0.773; best single model 0.756; o3-mini 0.495; GPT-4o at temperature 0 0.618 vs 0.679 at 1.0 | d05 | single-source |
| Volume closes coverage slowly | Nearest-neighbour distance to human ideas 0.546 (N=100) to 0.478 (N=1,000), no plateau | d06 | single-source |
| Verbalized sampling | 1.6-2.1x creative-writing diversity; human evaluation +25.7 percent; 66.8 percent of base-model diversity | c11 | single-source |
| Attribute prompts beat plain prompts | Matched plain at 5 percent of query cost; plain location bias 68.01 percent North America vs 0.69 percent Africa; all-best-values config worse than random configs | c13, c14 | single-source (data generation, not design) |
| Diversifying the wrong side hurts | Diversify-Y at least +2 F1 (up to +8); Diversify-X lowered F1; self-correction +1-2 | d09 | single-source |
| Many constraints at once break generation | 50 attributes, 3B model: constraint satisfaction 37.40 percent; degradation reported from about 30 | d02 | single-source |
| Code filter around LLM raises validity | Robot hands, 90 designs: validity random 0.16, zero-shot ChatGPT 0.52, Lang2Morph 0.82; diversity 0.64 with cues vs 0.27 without | d01 | single-source |
| Facet-wise judging helps | CSI median 70.5 vs 61.0 (N=22); novelty accuracy 0.78 facet-wise vs 0.47 unstructured prompt | c15, c16 | single-source |
| LLM judges rank ideas near chance | 43-56 percent (chance 50): GPT-4o direct 50.0, pairwise 45.0, authors' ranker 56.1 | c07 | established (with c16) |
| Pairwise judges flip on order | Instability 0.07-0.28 easy, 0.25-0.44 hard; humans 0.33; self-written rubrics cut it 16.1 percent | d03, d16 | single-source |
| Over-generate-and-rank beats experts on novelty | 4.84 human, 5.64 AI, 5.81 AI + rerank, N=49 each; slightly weaker on feasibility | c05 | single-source (large study) |
| AI ideas homogenise writers | N=293 writers; novelty +6.7 percent; stories 5.2 percent more similar to AI idea | c10 | single-source |
| Fixed-method LLM pipelines are unstable | AutoTRIZ: 7 of 10 cases match or half-match in top 3; entropy up to 6.64 over 100 runs | c20, c21 | single-source; supported by d07 |
| LLM taxonomy structure unstable | 324 runs, 9 models: 0.285 of sibling pairs recur in all runs (0.391 at T=0, 0.178 at T=1) with entity F1 0.995 | d07 | single-source |
| LLM on a Zwicky matrix | ChatGPT-4o ranked 4 scenario views over 10 issues: best 35/40 = 88 percent, worst 40 percent; one model, one date | c01, c02 | single-source |
| LLM-built boxes: no numbers retrieved | Chen 2024, Park and Geum 2025, Nomaguchi 2025 claim gains; none read in full | b16, c03, c25, d13, d14 | not assessed |

## 4. Mechanisms and models

### 4.1 The box as a data structure

```
box    = { parameter_i : [value_i1 ... value_ik_i] }    # i = 1..n
config = tuple (v_1j1, ..., v_njn)
|space| = product of k_i
```

Rules an engineer needs:

- Parameters should be distinct in meaning and together cover the problem (Zwicky step 2). Overlapping parameters create duplicate configurations.
- Values inside a parameter should be mutually exclusive.
- Six to ten parameters is the working range for modern fields (a06). Student boxes reach 10^4 to 10^13 and cannot be inspected (b02).
- The choice of aspects matters: a 9-option table scored flexibility 3 of 5, a 245-option table 4 of 5 (b13).

### 4.2 Cross-consistency assessment as code plus pair judgments

```
pairs = all (value_a, value_b) with a, b in different parameters
for each pair: label in {ok, conflict, unknown}     # one question each
keep  = [c for c in product(...) if no pair in c is 'conflict']
```

Count: the sum over parameter pairs of k_i x k_j. For 6 parameters of 4 values this is 15 parameter pairs x 16 = 240 judgments for 4,096 configs. Ritchey's shelter case marked 15 pair relations for a 2,304-config segment (a02).

Design points from Ritchey:

- No causal direction. The question is only "can both hold".
- Separate the three conflict types. Do logical and empirical first, normative later (a03).
- Pair-only checking misses triple conflicts. Verify the survivors (K03).
- Vague parameter definitions fail at CCA. Ritchey calls this "garbage detection" (a04). For our agent, treat a high conflict rate on one parameter as a sign that the LLM's own parameter is badly defined.

### 4.3 When the field is still too large

In Ritchey's EPR case, 480 of 34,560 survived CCA, and 8 configurations were chosen to cover every parameter state (a07). Candidate rules for code:

- Pairwise covering array: the smallest set in which every pair of values appears at least once (d11). The argument is that most effects are low-order. Untested for idea quality (K26).
- Random sampling of cells, as Yu et al. used because full enumeration cost too much (c13, c14).
- Coverage-prior sampling over a taxonomy (d10): 32 percent more attribute coverage, 44 percent more unique profiles (personas, not design).
- Linked fields: do not multiply two fields (over 700 million configurations). Merge one as a placeholder parameter (a07).

### 4.4 The LLM-plus-code split

This matches schema guardrail G5 (code selects).

| Step | Who | Reason |
|---|---|---|
| Choose parameters and values | LLM, repeated 3-5 times; keep majority items | Taxonomy runs share only 0.285 of sibling pairs (d07); a consensus core is recoverable |
| Enumerate the product | code | arithmetic |
| Pair compatibility | LLM, both orders, rubric, "unknown" allowed | Order flips 7-44 percent (d03) |
| Hard validity rules | code | A code filter lifted validity 0.52 to 0.82 (d01) |
| Pick cells to expand | code (random, covering array, diversity-greedy) | LLM judges are near chance at ranking (c07) |
| Expand one cell into a concept | LLM, fresh context, one cell per call | Fixation; 50-attribute prompts degrade (d02) |
| Final check | code or tests on the real task | G8 |

### 4.5 Why this could beat free sampling for an LLM

Free sampling collapses to a few modes (c06, c12). A box moves the variety from sampling noise into the prompt: each call gets a different cell. Yu et al. is the closest published analogue: attribute dimensions run by code beat plain prompts (c13). Terwiesch et al. show a single random functional constraint, close to a one-cell injection, lifted diversity from 0.679 to 0.735 (d04). The risk is that a bad box explores a bad space; no ablation of poor dimension choice was found (c14).

## 5. What holds up

**Holds up (established).**

1. Large unconstrained spaces need a pruning rule (b02, a06, d11).
2. No controlled study shows a box beats free ideation. Several independent searches agree on the absence (a12, a25, a30, b25, c28).
3. In human studies, morphology is not better on breadth. It gave more elaborated concepts than brainstorming (N=102) and no fluency or flexibility gain (N=244) (b14, b12).
4. The matrix is often misused as a filter (b03, b06, b01).
5. Unstructured LLM ideation saturates and homogenises (c06, c12, c08, a29).
6. LLM judges are poor at ranking ideas (c07, c16).

**Contested or in tension.**

- Hu 2020: morphology loads the prefrontal cortex most (a16). Field 2011 and Daly 2016 find no output advantage. Activation is not quality.
- Ritchey says structure does not hurt creativity (a10). The human data show no breadth gain either way.
- Bonde 2024: forcing a reduction made teams build more combinations but develop each less. The same software line produced word strings that students used as a filter (b01, b05). The tool shapes use in both good and bad ways.
- Yu 2023 calls full enumeration too costly. Ritchey calls enumeration after CCA cheap. They fit only if pruning comes first.
- Dating of Zwicky's 576 box: 1947 (a06) or 1962 (a12).

**Failures and null results.**

- Bonde 2024 did not reach significance (8 teams) (b21).
- Combination gave no between-group originality gain in Exp2 (b08) and cost raw quantity (b09).
- A matrix with few options narrows the space (b13).
- AutoTRIZ, the nearest fixed-method LLM pipeline, matched textbook answers in the top 3 only 7 of 10 times (c20).
- ProgGen: diversifying the sentence side lowered F1 (d09). Diversifying the wrong dimension hurts.

**Moderators.**

- Number and quality of aspects (b13).
- Whether people state why they drop options (b03).
- Spatial ability: in Field's uncontrolled data, classification users scored 5.9/10 on a mental cutting test, morphology users 4.3/10 (b13).
- Skill: in Oppenlaender's crowd pilot, open-ended submissions were 12 of 12 unusable. With a pre-made matrix 5 of 12 were rejected, 7 were effortful and only 4 gave a valid idea (a14). A pre-made matrix raises the floor but not by much.

**Interventions that worked.** Facet-wise structure (c15, c16); persona or random-constraint injection (d04); pooling vendors (d05); code filters on hard rules (d01).

**Interventions that did not work or are untested.** Serial "make it bolder" refinement (0.575, below plain, d04); independent one-idea sessions (0.452, d04); the alternatives-forcing prompt (recommended, untested, c19); covering arrays (untested, d11).

## 6. Language models

**There is no direct study.** No controlled study was found that compares an LLM with and without a Zwicky box on idea quality or coverage (c28, d17). Three LLM-box papers are leads without numbers: Chen et al. 2024 (decompose, generate, combine with LLM help, plus a feedback loop; claims better design quality and lower cognitive load, b16, d13), Park and Geum 2025 (matrix built from patents by LDA topics and NuNER entities, c03, d14) and Nomaguchi et al. 2025 (design catalogue from patents, c25). Only McIntosh 2026 puts a model on a Zwicky-style matrix, and the model reads it rather than builds it: ChatGPT-4o ranked four scenario views, best view 88 percent, no agreement test (c01, c02).

**Baseline behaviour in open ideation.**

- Saturation: about 5 percent unique of 4,000 (c06).
- Homogeneity: similarity over 0.8 in 79 percent of cases (c12).
- GPT-3 on 12 design problems: convex-hull volume 0.186 to 0.266 against crowd 0.294. The authors blame repetition after a few outputs and low variance (a28, a29).
- Design fixation on prompt details and early dropping of concepts in a hackathon (c17, c18).
- Even so, over-generate-and-rank beat human experts on novelty (5.64 vs 4.84, N=49) (c05).

**What changed diversity, and by how much (GPT-4o, 1 minus mean cosine).**

| Change | Score | Note |
|---|---|---|
| Plain prompt | 0.679 | baseline |
| Random functional constraint (cell-like) | 0.735 | +0.056 |
| Random persona | 0.757 | +0.078 |
| Chain of thought | 0.698 | +0.019 |
| Serial bolder refinement | 0.575 | worse |
| Independent single-idea sessions | 0.452 | much worse |
| Humans | 0.773 | target |
| Pool of 4 vendors | 0.763 | human level |

Source d04, d05. Quality was not matched across arms; one task.

Verbalized sampling gives 1.6-2.1x diversity in creative writing (c11). Parallel prompts with five different personas gave more diverse design concepts than one no-persona prompt in all three models; updating a set with a new persona did not reliably help (b17). Two-LLM collaboration raised novelty and variety (abstract only, c04).

**Attribute boxes run by code.** Yu et al. matched plain-prompt accuracy at 5 percent of the query cost. An LLM proposed the dimensions and values with human review, and configurations were sampled randomly (c13, c14). Boundary: 50 simultaneous attributes dropped satisfaction to 37.4 percent in a 3B model (d02), so keep one cell per call to a handful of constraints.

**Reproducibility of the box itself.** Two proxies. AutoTRIZ entropy reached 6.64 across 100 runs (c21). Taxonomy generation: only 0.285 of sibling pairs repeat in all 324 runs, even with near-perfect entity coverage (d07). Staged pipelines differ in stability, and generation noise exceeds judge noise (d08). The dimension step is unstable and needs repeats and consensus.

**Pairwise compatibility.** Judge instability is 0.07-0.44 by model and difficulty. Humans reach 0.33. Self-written rubrics cut it 16.1 percent; panels help up to 15 percent (d03, d16). No compatibility-versus-expert study exists (d17).

**Code-side validity.** In Lang2Morph, a code filter on six hard rules raised validity from 0.52 (zero-shot ChatGPT) to 0.82, and diversity cues raised the diversity score from 0.27 to 0.64 (d01). Small N, authors' own metric, no equal-token comparison.

**Model-age caveat.** Ma 2023 (GPT-3) and Meincke 2024 (GPT-4) use old models. Newer models are more diverse but still below humans, and o3-mini fixated at 0.495 (d05).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **S3 open mode: force coverage by structure, not by more samples.** Free resampling saturates and models agree with each other. Give each fresh-context attempt a different assigned cell or constraint. Schema part S3. [E] for the need and for diversity injection in general; the full box is not yet tested. Evidence: c06, c12, c08, d04; K11, K12.
2. **G5 and G8: code selects and filters; the model never picks the best cell.** LLM ranking is at chance (43-56 percent) and pairwise judges flip on order. Code enumerates, samples and applies hard rules. Schema part G. [E]. Evidence: c07, c16, d03; K15.
3. **Log why options are dropped.** Traditional teams stop at 1-2 combinations without a reason. Software that forced a stated reduction gave documented strategies. Schema part S3/G. [E] for the misuse, [S] for the benefit. Evidence: b03, b06, b01; K07.
4. **A pruning rule is required for large boxes.** Count cells before enumerating. Above a cap (suggest 200), sample, do not enumerate. Schema part S3/O. [E]. Evidence: b02, a06, d11, d12; K09.
5. **Do not use serial "bolder" refinement or independent one-idea sessions as diversity methods.** They scored below plain (0.575, 0.452). Schema part S3. [S], cheap to obey. Evidence: d04; K21.
6. **Do not put a whole box in one generation call.** Fifty attributes at once degrade to 37.4 percent satisfaction. One cell per fresh call, few constraints. Schema part S3. [S]. Evidence: d02.

### Test first

| Item | Schema | Status | Evidence |
|---|---|---|---|
| LLM builds box, code enumerates, LLM expands sampled cells, vs free sampling and verbalized sampling at equal tokens | S3, G5 | [S] | c13, d04, d01; K13, K21, K24 |
| Build the box 3-5 times; keep dimensions and values found in a majority | G (repeat, vote), S3 | [S] (instability is supported, the fix is untested) | d07, c21; K20, K25 |
| LLM pairwise CCA in both orders with a rubric, then code enumeration, then a verification pass | S3, G | [S] | a02, d03, d16; K01, K03, K23 |
| Cell selection rule: random vs covering array vs diversity-greedy | S3/O | [S] untested | d11, d10, d04; K26 |
| Category-first (classify the space) before combining | S3, O3/O6 | [C] human data show classification at least equals combination | b07-b09, b11; K06 |
| Facet-wise judging of candidates | S3/S5 | [S] | c15, c16; K14 |
| Alternatives-forcing instruction against fixation | G, S3 | [S] untested | c17-c19; K16 |
| Vary model or persona across cells for cross-run diversity | S3, memory | [S] | d05, b17; K22 |
| Box on non-design tasks (puzzles, planning) | S3 | no study | K28 |

## 8. Concrete tests on our bench

All arms use equal total tokens, counting box construction, pair judgments and expansion (G7). Use at least 3 seeds. Use blind raters, or code checks where a check exists.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Box vs free vs verbalized | Open design prompts with reference solution lists (10-20 problems, in the style of the 12 problems of Ma 2023, or our NoveltyBench items) | A free sampling; B verbalized sampling; C LLM box plus code-sampled cells, one cell per fresh call | Distinct ideas at cosine 0.8; coverage of reference solutions; validity by code or blind rater | C above A on distinct count by at least 20 percent; C vs B uncertain |
| T2 Pair CCA value | Boxes of 4-6 parameters seeded with known conflicts, including 3-way conflicts | A no pruning; B pair CCA, one order; C both orders with rubric and "unknown"; D = C plus survivor verification | Share of known conflicts removed; share of valid configs wrongly removed; survivor validity | C removes at least 70 percent of pair conflicts with under 10 percent false removal; D catches most triple conflicts |
| T3 Box reproducibility | Same problem, 5 repeated builds, 2 models | Single build vs consensus build | Share of values recurring across runs; reference-solution coverage | Single run shares under 50 percent of values; consensus raises coverage and stability |
| T4 Cell selection | Boxes of 10^4 to 10^6 cells | Random; covering array; diversity-greedy, at equal cell count | Coverage of reference solutions; embedding diversity | Greedy at least covering array at least random; margins small |
| T5 Category-first | Open design prompts | Combine-first vs classify-then-combine | Unique ideas; blind originality | Classify at least combine (per Saurabh) |
| T6 Non-design transfer | ARC or BRAINTEASER hypothesis spaces | Box over (object, relation, operation) vs plain attempts | Pass rate | Likely no gain; guards G7 |
| T7 Drop log | Same open prompts | Reason logged per dropped option vs none | Final quality; combinations carried | Small or null; cheap |
| T8 Homogeneity | 3 runs per prompt | Box vs persona vs verbalized | Cross-run pairwise similarity | Box lowers within-run similarity; cross-run effect unknown |

## 9. What does not transfer, and why

- **Human cognitive load (fNIRS).** Prefrontal activation (a16-a18) has no counterpart in a model and is not quality.
- **Student habits (screening misuse, stopping at 1-2).** A model does not get bored. The same failure may appear as early convergence on one cell, so log drops anyway.
- **Group effects of CCA** (shared understanding, "garbage detection" through discussion). One model is not a group, and samples from one model are not independent (G4).
- **Zwicky's 40-dimension totality.** A context window cannot hold such fields. Use sampling.
- **Single-answer problems.** The box is for open mode. G4 forbids persona or strategy voters on single-answer problems, and cell diversity can add wrong answers where one answer is exact.
- **Ritchey's reduction figures.** They are advocate numbers from human CCA on well-defined policy fields. An LLM's pair judgments are noisier (d03), so expect less trusted reduction.
- **Scenario boxes (Rhyne, foresight).** McIntosh's result is about reading a box against the world, not building one.
- **Optimisation over the matrix** (Olvander 2009) needs per-cell performance models, which text tasks lack (b24).
- **Crowd results** (Oppenlaender): a pre-made box helps weak workers; our agent is a different baseline.

## 10. Open questions

1. Does an LLM-built box with code enumeration beat free sampling and verbalized sampling at equal tokens? No direct study.
2. What numbers do Chen 2024 and Park and Geum 2025 report? Not retrieved.
3. How accurate are LLM pair-compatibility judgments against experts? How many triple conflicts slip through?
4. How reproducible is LLM construction of design parameters across runs and models? Only proxies exist.
5. Does anyone besides Ritchey measure how much CCA shrinks a field, or whether survivors are better?
6. Which pruning rule is best at 10^6 cells and above?
7. Category-first vs combine-first for an LLM.
8. Does box generation reduce or raise cross-run homogeneity?
9. Do boxes help outside design tasks?
10. Zwicky's "unconsidered configurations" has not been counted (d12). The 1947 vs 1962 dating is unresolved.
11. Is dimension quality the main cause of box success or failure? No ablation of poor dimensions exists (c14).
12. Has the 2026 Terwiesch result (d04) been replicated by others?

## 11. Sources

[V] opened; [M] snippet or abstract only. Related subfields covered in parallel (links only): Creative problem solving; Search over thoughts; Tree of Thoughts; Analogy and distant sources; TRIZ; Epistemic diversity; Novelty measurement; Priming of orientation.

- [V] Ritchey (2013) General Morphological Analysis. https://www.swemorph.com/pdf/gma.pdf (a01-a04, b19, b20)
- [V] Ritchey (2006) Problem structuring using computer-aided morphological analysis. https://www.swemorph.com/pdf/psm-gma.pdf (a05-a08)
- [V] Ritchey (1998) Fritz Zwicky, Morphologie and Policy Analysis. https://www.swemorph.com/pdf/zwicky-morph.pdf (a09-a11, d12)
- [V] Alvarez and Ritchey (2015) Applications of GMA. https://www.swemorph.com/amg/pdf/amg-4-1-2015.pdf (a12, a13)
- [V] Ritchey (2012) Outline for a Morphology of Modelling Methods. https://www.swemorph.com/amg/pdf/amg-1-1-2012.pdf (a24)
- [V] Ritchey (2022) Morphospaces catalogue. https://www.swemorph.com/amg/pdf/amg-8-1-2022.pdf (a25)
- [V] Wikipedia, Morphological analysis. https://en.wikipedia.org/wiki/Morphological_analysis_(problem-solving) (a26)
- [V] Oppenlaender (2021) Morphological Matrices for Crowdsourced Ideation. https://arxiv.org/abs/2110.04129 (a14, a15)
- [V] Hu, Shealy, Milovanovic, Gero (2020) Concept generation techniques and brain activity. https://doi.org/10.1017/dsj.2020.30 (a16-a18)
- [M] Gero, Jiang, Williams (2012). https://doi.org/10.1115/detc2012-71165 (a19)
- [M] Kannengiesser, Williams, Gero (2013), via Alvarez and Ritchey 2015 (a20)
- [M] Shah, Kulkarni, Vargas-Hernandez (2000). https://doi.org/10.1115/1.1315592 (a21, b23)
- [M] Eftekhari (2021). https://doi.org/10.21606/drs_lxd2021.09.270 (a22)
- [M] Savchenko (2020). https://doi.org/10.1109/saic51296.2020.9239226 (a23)
- [V] McIntosh (2026) Foresight evaluation with GenAI and MA. https://www.emerald.com/fs/article/28/1/66/1342859/Linking-generative-AI-and-morphological-analysis (a27, c01, c02)
- [V] Ma, Grandi, McComb, Goucher-Lambert (2023). https://arxiv.org/abs/2306.01779 (a28, a29)
- [V] Bonde et al. (2024) Specialized software on concept generation. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/123523CFFC4753D070FFD4BCF299EA8C/S2732527X24000695a.pdf (b01-b04, b21)
- [V] Martinsson Bonde et al. (2022) Morpheus. https://cognitive.designsociety.org/publication/45130 (b05, b06)
- [V] Saurabh et al. (2022) Idea generation mechanisms. https://acris.aalto.fi/ws/portalfiles/portal/76056779/ENG_Saurabh_et_al_Idea_Generation_Mechanisms_Journal_of_Mechanical_Design.pdf (b07-b11)
- [V] Field (2011) Fluency and flexibility. https://creativity.designsociety.org/download-publication/30708/FLUENCY+AND+FLEXIBILITY+OF+CONCEPTS+ARISING+FROM+PERSONALISED+IDEATION+TECHNIQUES (b12, b13)
- [V, abstract] Daly et al. (2016) Comparing ideation techniques. https://doi.org/10.1115/1.4034087 (b14)
- [V, no numbers] Sharbafi (2021). https://dl.designresearchsociety.org/learnxdesign/learnxdesign2021/researchpapers/49 (b15)
- [M] Chen, Tsang, Jing, Sun (2024) LLM-augmented morphological analysis. https://doi.org/10.21606/drs.2024.605 and https://dl.designresearchsociety.org/drs-conference-papers/drs2024/researchpapers/152 (b16, d13)
- [V] Feng, Helie, Panchal (2025) Multi-persona prompting. https://doi.org/10.1017/dsj.2025.10037 (b17)
- [V] Jiang and Luo (2024) AutoTRIZ. https://arxiv.org/abs/2403.13002 (b18, c20, c21)
- [M] Zwicky (1969), second-hand (b22)
- [M] Olvander, Lunden, Gavel (2009). https://doi.org/10.1016/j.cad.2008.06.005 (b24, c22)
- [M] Park and Geum (2025). https://doi.org/10.1016/j.cie.2025.111426 (c03, d14)
- [M] Xiao, Zhang, McAdams (2026). https://doi.org/10.1115/1.4072235 (c04)
- [V] Si, Yang, Hashimoto (2024). https://arxiv.org/abs/2409.04109 (c05-c07)
- [V] Meincke, Mollick, Terwiesch (2024). https://arxiv.org/abs/2402.01727 (c08, c09; d15 snippet)
- [V] Doshi and Hauser (2024). https://arxiv.org/abs/2312.00506 (c10)
- [V] Zhang et al. (2025) Verbalized Sampling. https://arxiv.org/abs/2510.01171 (c11)
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954 (c12)
- [V] Yu et al. (2023) Attributed training data generator. https://arxiv.org/abs/2306.15895 (c13, c14)
- [V] Radensky et al. (2026) Scideator. https://arxiv.org/abs/2409.14634 (c15, c16)
- [V] Egea et al. (2025) ChatGPT as an inventor. https://arxiv.org/abs/2404.18479 (c17-c19)
- [M] Ritchey (2006) JORS record. https://doi.org/10.1057/palgrave.jors.2602177 (c23)
- [M] Filippi (2023). https://doi.org/10.3390/electronics12163535 (c24)
- [M] Nomaguchi et al. (2025). https://doi.org/10.1017/pds.2025.10119 (c25)
- [V, negative check] Ren, Ma, Luo (2025) patent concept generation. https://arxiv.org/abs/2409.00092 (c26)
- [M] Ch'ng (2025). https://doi.org/10.21203/rs.3.rs-8274845/v1 (c27)
- [V] Qiao et al. (2025) Lang2Morph. https://arxiv.org/abs/2509.18937 (d01)
- [V] Yun, Peng, Shang (2025) UltraGen. https://arxiv.org/abs/2502.12375 (d02)
- [V] Feng et al. (2025) Sage. https://arxiv.org/abs/2512.16041 (d03, d16)
- [V] Terwiesch et al. (2026) AI and creativity diversity. https://arxiv.org/abs/2607.27553 (d04-d06; id as recorded in the evidence file)
- [V] Yearsley and Kurteva (2026) taxonomy stability. https://ceur-ws.org/Vol-4293/paper38.pdf (d07)
- [V, partial] Nakashima et al. (2026) taxonomies in SE. https://arxiv.org/abs/2608.01592 (d08)
- [V] Li et al. (2024) ProgGen. https://arxiv.org/abs/2403.11103 (d09)
- [V] Wang et al. (2025) DeepPersona. https://arxiv.org/abs/2511.07338 (d10)
- [V] Ackerman et al. (2024) Covering arrays for LLM solution design. https://arxiv.org/abs/2405.13020 (d11)
