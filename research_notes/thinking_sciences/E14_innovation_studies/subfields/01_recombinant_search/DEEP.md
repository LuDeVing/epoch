# Recombinant search: deep document

*Subfield E14.01. Written from evidence_a-d.jsonl, claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids (a01..d19) point to those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

---

## 1. What it is

Recombinant search is the idea that new things are mostly new combinations of old parts. An inventor, a scientist or a model picks parts that already exist and puts them together in a way not yet tried.

The core claim comes from Fleming (2001), who tested it on US patents. It has four moving parts.

1. **Familiar parts help.** A patent built from components that were used often before gets more later citations. Citations stand in for "usefulness".
2. **New combinations are a gamble.** A combination with little prior use has a wider spread of outcomes. More total failures, and more breakthroughs.
3. **Refining helps.** Reworking a combination that has been used before raises its average usefulness and cuts its spread.
4. **Over-reuse hurts.** The more often one combination has already been used, the less useful the next invention that uses it.

The slogan "new combinations have lower mean and higher variance" is a compact form of parts 1 to 3. The "lower mean" half is the weak half (see section 5). The "higher variance" half is the strong half.

Why it matters for our agent. Schema operator O7 ("map an analogue") and the open-mode rule in S3 ("some attempts are grounded in retrieved distant analogues") both depend on one question: how far from the known should the agent reach, and how many times should it refine or repeat a blend? This subfield gives numbers for distance, for spread, for refinement depth and for repetition. It also covers whether language models show the same pattern.

What this subfield is not. It does not cover how to score analogies (Structure mapping, SME) or how to judge novelty (Novelty and atypicality). Those are parallel subfields. Here we only note links.

---

## 2. History and theories in depth

### 2.1 Roots before Fleming
- **Combinatorial explosion.** Weitzman (1998, a20) modelled growth as recombination. Pairs grow as C(M,2). All subsets grow as 2^M. The supply of seed ideas explodes. The binding limit is turning seeds into usable form, not generating them. Theory only, no data.
- **Exploration and exploitation.** March (1991) set the frame that Fleming builds on (a01). Search near what you know pays off soon and surely. Search far pays off rarely.
- **Rugged landscapes.** Kauffman, and Levinthal (1997, a27, abstract only). When parts interact, the landscape has many peaks and the start decides which peak you find. Fleming and Sorenson (2001, a22) apply this to patents: more interdependence makes search harder. Not opened.
- **Bounded rationality.** Nelson and Winter, Simon. Searchers look locally because they cannot evaluate everything (a01).

### 2.2 Fleming 2001 (the founding study)
Fleming (a01-a06, b01-b03, d01-d02) argues inventors search locally. Five hypotheses:
- H1 familiar components raise usefulness. Supported.
- H2 familiar components cut uncertainty. Not supported as stated. The effect is U-shaped.
- H3 refining a combination raises usefulness. Supported.
- H4 refining cuts uncertainty. Supported, monotonically.
- H5 cumulative use of one combination lowers usefulness (exhaustion). Supported, but not separable from normal life-cycle decline (author says so).

Strategy advice (a06): organisations that want breakthroughs should try new combinations, even with old parts, and accept more failures. Cheap screening of early inventions raises the value of high-variance trials. Portfolio averaging fails because outcomes are extremely skewed. This advice was not tested in the paper.

### 2.3 Follow-ups on the science side
- **Uzzi et al. 2013 (a07, a08, b04, b05, d03).** Novelty is how unusual each pair of cited journals is, scored against a randomised citation network. Best impact: a conventional core plus a small tail of unusual pairs.
- **Foster, Rzhetsky, Evans 2015 (a12, b20, b21, d04).** Research moves in biomedical chemistry: scientists mostly repeat. Rarer moves pay more on average but not enough to cover the risk.
- **Wang, Veugelers, Stephan 2017 (a09, b06-b08).** First-ever journal pairs. Novel papers have higher mean and spread in the long run but are recognised late.
- **Verhoeven et al. 2016 (a13, b18, b19, d05, d06).** A same-model replication on worldwide patent families.
- **Singh and Fleming 2010 (a26, b23, d08).** Collaboration cuts the poor tail and lifts the good tail. Full text never opened.
- **Li, Lin, Wu 2024/2025 (a16, a17, b10-b12).** Rival view: atypical references go with lower disruption.
- **Ke et al. 2021/2024 (a15, b15, b16) and Mukherjee et al. 2017 (b17).** The age mix of the knowledge used matters.

### 2.4 Growth models
Tria et al. 2014 (a19) built an urn model in which each novelty opens new adjacent possibilities. It fits Heaps' law and Zipf's law. Youn et al. 2015 (a10, a11) found that about 60% of new US patents make a never-seen code combination and about 40% reuse one. Pichler, Lafond, Farmer 2020 (a21) predict patent rates from domain interdependencies. Arthur and Polak 2006 (a28, secondary only) evolved circuits from NAND gates; complex designs need simpler stepping stones first. All of this is about rates, not usefulness.

### 2.5 Measurement critiques
Bornmann et al. 2019 (a18, b14) and Fontana et al. 2020 (b13) test whether journal-pair scores really measure novelty. The Uzzi-style score weakly tracks expert tags. The Wang-style score does not. First-appearance novelty mostly reflects citation-network structure. So the field's key variable is noisy.

### 2.6 The LLM turn (2023 to 2026)
Work from SciMON (2023, c22) onward tests whether language models recombine well, whether distance helps them, and whether their ideas survive execution. Section 6 covers this.

---

## 3. Core findings with exact numbers

Status: E established, S single-source, C contested. Claim ids are K-numbers from claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Component familiarity raises citations | +11.3% per SD; +147% lowest to highest (coef 0.3958 x 2.28 gives e^0.90 = 2.47). n = 17,264 US patents, May-June 1990. Mean cites 3.80, SD 4.88 | Fleming 2001 (a02, a03, d01) | E (K01) |
| Familiar components cut spread only a little, then raise it | Max spread cut 9.6% at the 60th percentile (variance 25.32 vs 28.02); sign flips at the 96th percentile. H2 fails | Fleming 2001 (b02, d01) | E (own paper) |
| Combination familiarity raises citations | +10.3% per SD; +332% at max 11.25 vs 0 | Fleming 2001 (a04, b01) | S (K02) |
| Combination familiarity cuts spread | 2.2% at the average patent; 64% at max | Fleming 2001 (a04, b02) | S (K02) |
| Cumulative reuse of one combination lowers usefulness | At max use 26.76: 37.9% of baseline citations; -5.6% per SD. Cannot be split from life cycle | Fleming 2001 (a04, d02) | S (K03) |
| Novel combinations have wider spread (papers) | Dispersion +14.90%; top-10% odds +16.80%; bottom-10% odds +16.76%; top-1% odds +39.82% (highly novel). 773,311 articles (2001); 1,056,936 field-article observations | Wang et al. 2017 (a09, b06) | E (K04) |
| Novel combinations have wider spread (patents) | 2-SD outlier base rate 3.3%. Observed over expected: any 1.86, NR 2.11, NTO 1.87, NSO 3.82, all three 6.48. 22% of all-three patents are 2-SD outliers | Verhoeven et al. 2016 (b18) | E (K04) |
| Mean for novel work: papers go up | Highly novel +12.04% mean citations; moderately novel +2.78%. Needs window of 4+ years (high) or 9+ years (moderate) | Wang et al. 2017 (a09, b07) | C (K05) |
| Mean for novel work: patents go down after controls | New recombination -0.0957 (about -9.1%); new technological origins -0.127 (about -11.9%); new scientific origins +0.0469 (about +4.8%). N = 2.3 to 3.6 million families | Verhoeven et al. 2016 (d05) | C (K05) |
| Raw patent means go the other way | Any novelty 6.62 vs 6.03; all three 12.96 vs 6.17 (N = 12,471) | Verhoeven et al. 2016 (d06) | C (K05) |
| Conventional core plus novel tail is best | Hit rate per 100: 9.11 core+tail; 5.82 conventional only; 5.33 novel only; 2.05 neither. Shares 6.7 / 23 / 26 / 44%. 17.9M papers; hit = top 5% of 8-year citations | Uzzi et al. 2013 (a07, b04) | E (K06) |
| Peak impact at very high conventionality | 85th to 95th percentile of median conventionality | Uzzi et al. 2013 (a08) | E |
| Recent and age-varied science sources help patents | 12.5% of 3,693,101 patents cite science; +49% 10-yr cites; +117% odds top 5%; +171% top 1%. Recency above avg +14% cites; age variance above avg +16% | Ke et al. 2024 (a15, b15, b16) | E (K10) |
| Knowledge-age "hotspot" | Recent knowledge with wide age spread: 2.2x odds of top 5%; 75% of papers outside it. 28.4M papers, 5.4M patents | Mukherjee et al. 2017 (b17) | E (K06) |
| Scientists mostly repeat | 85.8% repeat vs 14.2% new; mean cites 8.38 repeat, 11.00 new, 12.90 jump. 10x rarer move gives +2.26 cites. Surprisal explains 29.2% of mean variation, 28.6% of SD. 6,455,756 abstracts | Foster et al. 2015 (a12, b20, d04) | S (K09) |
| Teams add the novel tail | Tail novelty 36.2% solo, 39.9% pairs, 49.7% 3+ authors. Core conventionality unchanged by team size | Uzzi et al. 2013 (b05, d03) | E (K12, K31) |
| Large teams: more hits, less disruption | 10-person teams 50% more likely to hit; solo authors 72% more likely to be top-5% disruptive; cross-journal fusion saturates at 8 to 10 members then reverses. 50M+ works | Wu, Wang, Evans 2019 (d07) | E (K31) |
| Atypical references go with lower disruption | Coefficient -0.0009 in 2,461 version pairs; 18.9M papers (1900-2010); 40.9M papers in the 2025 version | Li, Lin, Wu (a16, a17, b10, b12) | S (K08) |
| About 60% of new patents make a new code combination | C = 0.6 P over 1790-2010 | Youn et al. 2015 (a10) | E (K11) |
| Journal-pair novelty is a coarse measure | +7.47% new-finding tags per SD of U score; pseudo R2 0.33% (n = 23,206) | Bornmann et al. 2019 (b14) | E (K07) |
| LLM far-source gain depends on distance | o3 + Claude-Sonnet-4: all pairs b = 0.02 (p = .64); far 50% b = 0.12 (p = .029); far 10% b = 0.24 (p = .024). Distance slope LLM .18, human .1 | Liu et al. 2026 (c02, c03, d15) | S (K13) |
| LLM far ideas keep usefulness, human far ideas do not | Top 10% original: human lower on utility (0.81), investment (0.60), feasibility (0.26) than equally original LLM ideas | Liu et al. 2026 (c04) | S (K14) |
| Structured analogy beats "use another domain" | Domain distance 6.83 to 7.53 vs 2.29 to 3.37 (over 3x); solution Vendi +90 to 173%; binary novelty Claude 1.6 / 21.6 / 50.4%, GPT 8.8 / 27.2 / 58.8% (none / cross-domain / AR) | Shen et al. 2026 (c06, c07) | S (K15) |
| LLMs fixate on the same parts | 56% of GPT-4o recipes use smoked paprika vs 0.375% in corpus; 47% have similarity over 0.85 to a corpus recipe | Mizrahi et al. 2025 (c12) | S (K16) |
| Part-level recombination scaffold raises novelty at some value cost | Novelty 3.53 vs 3.146 (p = .0009); valued 85% vs 98% in Exp 2 | Mizrahi et al. 2025 (c11, d14) | S (K16) |
| LLM-rated novelty does not predict impact | Judge 7.44 vs 7.40 (p = .584); future-paper match 0.297 vs 0.119 (ratio about 2.5); correlation with judged novelty -0.29 | HINDSIGHT 2026 (c26) | E (K19) |
| AI ideas lose their edge once executed | After execution AI ideas -1.049 / -1.760 / -1.879 (novelty / excitement / effectiveness); human -0.010 / +0.078 / -0.052. 43 experts | Si et al. 2025 (c10) | S (K18) |
| AI research ideas rated more novel before execution | 5.64 vs 4.84 (79 reviewers); feasibility 6.34 vs 6.61 n.s.; only about 5% of 4,000 seeds non-duplicates | Si et al. 2024 (c09) | S (K18) |
| AI agents explore less than humans | Distance 0.322 vs 0.410; breadth 0.554 vs 0.599; 219,655 ideas | Tang and Yang 2026 (c15) | E (K20) |
| Hypotheses far in distance but low in direction | ONS 15 to 23% lower than real papers; farthest-paper context raises distance 11 to 16% but not direction | Liu, Butler et al. 2026 (c17, c18) | E (K20) |
| Iteration sweet spot | Entities: turn 1 70.6% new, turn 3 78.3% inherited. SciMON: 55.6% gain round 1, 57.8% round 2. Nova: gains rounds 1 to 3, flat after | Chen and Zhang 2026; Wang 2023; Hu 2024 (c22, c23, d12) | E (K21), LLM-judged |
| Random vs frequency-ranked element triples | distinct-1 0.41 vs 0.21; BLEU 0.05 vs 0.11 | Llull-style 2025 (c24) | S (K22) |
| Purpose-near, mechanism-far inspirations | 46% good (>=2 of 5 judges) vs 37% random vs 30% surface-near; 38 / 22 / 21% at >=3 of 5. 38 workers, 749 ideas | Hope et al. 2017 (d11) | S (K26) |
| Samples are not independent | 79% of prompts: average pairwise similarity over 0.8 at temp 1; cross-model similarity 71 to 82%; 19.9% of invented concepts reuse 2+ properties of another model's | Jiang et al. 2025; Kombine (d09, b26) | E (K27) |
| LLM research ideas already lean on bridging | Bridge framing 47.1 to 64.2% vs 12.1% human; synthesis as main method 22.5 to 38.7% vs 5.1% | Chen, Zhao, Cohan 2026 (d17) | S (K28) |
| Greedy plus small random jump beats greedy | Hit rate 26.3 vs 19.3 (DBLP), 28.1 vs 21.5 (PubMed), 24.6 vs 18.2 (PatSnap); LLM prompting 14.3 to 19.0 | Chen et al. 2025 (d13) | S (K29) |

---

## 4. Mechanisms and models

This section explains each mechanism so it can be coded.

### 4.1 Why familiarity raises the mean
Fleming's model: a combination is a set of components. Each component and each pair has a use count from the past. A familiar part has known behaviour, known interfaces and known failure modes. So the next use is more likely to work. Count-based model: expected citations = exp(b1 x component familiarity + b2 x combination familiarity + b3 x cumulative use + controls). Fleming fits a negative binomial model for the mean and a second model for the dispersion (variance).

Implementation for an agent: keep a table of parts (functions, rules, concepts, operators) with a count of prior successes. Score a candidate blend by the mean familiarity of its parts and of its pairs.

### 4.2 Why novel combinations widen the spread
With little prior use, the outcome has no track record. Interactions between parts are unknown (rugged landscape, Levinthal). So outcomes can be very bad or very good. Verhoeven's data show both tails fatten. Wang's data show both tails fatten (top-10% +16.80%, bottom-10% +16.76%).

Implementation: treat a far pair as a draw from a wider distribution with a similar or slightly lower centre. Use cheap screening before expensive execution. Fleming's own advice: screening raises the value of high-variance trials.

### 4.3 Conventional core plus novel tail (Uzzi)
Per item compute two numbers over all part pairs: the median pair z-score (conventionality) and the 10th-percentile z-score (tail novelty). Target: median in the top conventional band, with a few unusual pairs. Hit rate 9.11 per 100 vs 5.82 for conventional only.

Pair z-score = (observed pair count minus expected under a randomised network) divided by the SD of the randomised count. Needs a reference corpus. For an LLM agent the cheap stand-in is a count of how often two concepts co-occur in a retrieved corpus, versus how often chance predicts.

Caveat: Bornmann (b14) and Fontana (b13) show this measure is coarse at paper level. Do not trust it for item-level decisions without a check.

### 4.4 Rare-move allocation (Foster)
Surprisal of a move = -log(probability of that move under the current mix). Foster finds mean citations rise and spread rises with surprisal. Scientists choose 85.8% repeats. A budget rule follows: spend most moves on near, known pairs; spend a small share on far moves. d13 gives a version for search: take the best-scoring pair, but with small probability accept a random pair. It beat pure greedy by about 7 points of hit rate, but the probability was not given and compute was not matched.

```
for step in range(budget):
    if random() < eps:      # eps untested; sweep 0, 5, 15, 30%
        move = random_far_pair()
    else:
        move = best_scored_pair()
    result = execute_and_check(move)
```

### 4.5 Refinement and lock-in
Fleming: refinement of a used combination raises the mean and cuts the spread. LLM iteration studies: round 1 imports many new parts (70.6% new entities in Chen and Zhang). Later rounds inherit from the last version (78.3% by turn 3). Diversity and novelty peak near round 2. SciMON: gains 55.6% in iteration 1, 57.8% in iteration 2. Nova: gains in rounds 1 to 3, none after; without planned retrieval, no growth between rounds 2 and 3 (42.4 to 44.1 unique novel ideas).

Implementation: refine at most 2 to 3 rounds, each round bringing in new retrieved input, then regenerate from a new pair. Without new input, refinement only polishes.

### 4.6 Exhaustion
Fleming's H5: the more a pair has been used, the less value in the next use. Cumulative use at the maximum gives 37.9% of baseline. This is a population finding and cannot be split from life-cycle. For an agent, the analogue is a repeat-pair counter inside one run. No study tests this inside a run.

### 4.7 Distance and structure (LLM side)
Distance by embedding gap is cheap. Direction matters too (ONS, Liu and Butler et al.): a far hypothesis can still extend known work. Structured analogy (Shen et al.): (1) abstract the problem to a relational structure, (2) find a domain with that structure, (3) solve there, (4) map back. This raised domain distance over 3x. Hope et al.: choose inspirations near in purpose and far in mechanism, spread by a max-min rule (each new pick maximises its minimum distance to those already picked).

### 4.8 Explicit ranked recombination (Cooking Up Creativity, Alien Recombination)
Both treat recombination as ranked search over parts, with a familiarity or value score on each pair. Dish COVER: recipes to trees, edits by cognitively inspired operators, a value threshold (0.3), novelty rank, back to text. Alien Recombination: rank combinations by low probability under an artist-level model; temperature alone does not reach what artists never use. Caveat: Dish COVER kept the top 5 of up to 5,600 trees per pair (about $42 per step), so it is not an equal-token test.

### 4.9 Independence of searchers
Singh and Fleming claim collaboration cuts the poor tail and lifts the good tail. LLM samples are not independent searchers (d09). So in an agent, independence must come from different inputs (different part sets), not from more samples of one prompt.

---

## 5. What holds up

### 5.1 Replications
- **Variance half of Fleming: holds.** Papers (Wang), patents (Verhoeven), science moves (Foster). Three sources, different units, same direction.
- **Familiar parts raise the mean: holds in direction.** Fleming, Uzzi (conventional core), Mukherjee (recent and varied). Note Ke et al.: science sources help only when varied in age.
- **Conventional core plus small novel tail: holds.** Uzzi on 17.9M papers; Mukherjee's hotspot (2.2x); both point the same way.
- **Verhoeven 2016 replicates the mean penalty after controls.** New recombination -9.1%, new technological origins -11.9%. Raw means go the other way (6.62 vs 6.03). Evidence a13/b19 wrongly said the mean was not tested; d05 corrects it.
- **Only the iteration sweet spot has three LLM sources** (Chen-Zhang, SciMON, Nova), but all three judge by LLM or embedding, not by an outcome check.

### 5.2 Failures and contradictions
- **Lower mean for novel work fails for papers.** Wang 2017: +12.04% mean for highly novel papers (long windows). Foster: higher mean for rarer moves. Uzzi: tail novelty adds hits. Only patents, after controls, show the penalty. Status: contested.
- **H2 fails inside Fleming's own paper.** Familiar components cut spread by at most 9.6%, then raise it at the 96th percentile. Later summaries that state the claim cleanly overstate it.
- **Disruption disagrees with hits.** Li, Lin, Wu: atypical references go with lower disruption (-0.0009). Wu 2019: larger teams give more hits, less disruption. Different outcome, and the D index is itself contested.
- **Foster: reward does not cover risk.** Rare moves earn more on average but not enough for the extra chance of going unpublished. Failed projects are invisible, so the bound is a bound.
- **Measurement.** Journal-pair novelty tracks expert tags weakly (pseudo R2 0.33%) and first-appearance novelty mostly reflects network structure.

### 5.3 Moderators and boundary conditions
| Moderator | Effect | Source |
|---|---|---|
| Citation window | Highly novel papers lose under 3 years, win from year 4. Moderately novel need 9+ years | Wang (b07) |
| Home vs foreign field | Foreign-field top-1% odds +62.37% (high novelty); home field not significant | Wang (b07) |
| Controls (family size, field) | Flip the patent mean from up to down | Verhoeven (d05, d06) |
| Source age variance | Low variance offsets the science benefit | Ke (b15) |
| Team size | Novelty inverted-U (turn near 7 authors); fusion saturates at 8 to 10 | Lee (a14); Wu (d07) |
| Outcome type | Hit rate, disruption and new-topic opening have different drivers | Li; Kaplan-Vakili (a25, abstract) |
| Field | Social sciences and psychology score high on novelty; space and physics low | Wang (b08) |
| Distance for LLMs | Gain only in the far 50% (best two models) | Liu (d15) |

### 5.4 Interventions that worked
- Structured analogy step over a plain "use another domain" prompt (distance 3x, Vendi +90 to 173%). LLM-judged. [c06, c07]
- Purpose-near, mechanism-far retrieval over surface-near or random. Humans. [d11]
- Explicit ranking of rare pairs over temperature. [c13, c11]
- Farthest-paper context to push distance up (but not direction). [c18]
- A facet-aware novelty checker against literature (89.66% of not-novel ideas found vs 10.34% for embeddings only). [c20]
- Greedy plus a small random acceptance. [d13]
- Retrieval during iteration (Nova): without it, no growth. [d12]

### 5.5 Interventions that did not work
- Plain "use another domain" prompt: barely helps LLMs (c06).
- Higher temperature: new combinations, but not outside what artists use; at T = 3 over half had zero cognitively unavailable concepts (c13). A second source says temperature has only a weak link to novelty (c29, second-hand).
- More focal papers in context (N = 5 to 100): no change in direction. Larger models: no fix (Gemini ONS win rate 26% to 22%) (c18).
- Persona and judge-dialogue configurations: contraction persists (c19, abstract only).
- Retrieval and persona prompts: marginal gains (c27).
- Cross-domain mapping for pooled LLMs: no average gain over a plain user-need prompt (c02, d15).
- More samples from one model: 79% of prompts give pairs above 0.8 similarity (d09).

---

## 6. Language models

### 6.1 Do LLMs show Fleming's pattern?
Only partly, and no study tests it with an outcome check.
- **Spread and cost side.** Liu et al. 2026 (c04): the top 10% most original human ideas under cross-domain mapping were worse on utility (0.81 lower), investment-worthiness (0.60) and feasibility (0.26) than equally original LLM ideas. The cost of far ideas shows in humans, not LLMs. The tail was selected, and LLMs may be less extreme. Humans copy surface features; LLMs copy structure and function (c05, qualitative).
- **Mean side.** Pooled LLMs gained nothing from a supplied far source over a plain user-need prompt; the gap closed once the nearest 20% of pairs were dropped. The two best models (o3, Claude-Sonnet-4) gained only in the far 50% (b = 0.12) and far 10% (b = 0.24); over all pairs b = 0.02 (c02, c03, d15). Originality rose with distance: slope .18 LLM vs .1 human. Product design only.
- **Reuse.** No LLM study tests over-reuse of one pair inside a run. Only iteration studies touch refinement.

### 6.2 What LLMs do by default
- **They stay near the seeds.** Distance from seed papers 0.322 vs 0.410 for humans; breadth 0.554 vs 0.599; frontier alignment 0.045 lower pooled (c15). Literature search reduced the gap. More of their novelty is method recombination than new problems (c16).
- **Far in distance, short in direction.** Median ONS 15 to 23% lower than real papers; real paper wins in 72 to 82% of random pairs; effect in 86 to 97% of 1,325 topics (c17).
- **They already lean on bridging.** Bridge framing 47.1 to 64.2% across nine LLMs vs 12.1% for human papers. Thinking mode raises it (Qwen3-8B 49.7% to 71.1%) and moves it further from the human distribution (TVD 0.382 to 0.590) (d17).
- **They fixate on parts.** Smoked paprika in 56% of GPT-4o recipes vs 0.375% in the corpus (c12).
- **They share a hivemind.** One model repeats itself; models agree 71 to 82% (d09). 19.9% of invented concepts in Kombine reuse two or more properties of another model's (b26). Only about 5% of 4,000 seed ideas were non-duplicates (c09).
- **They find a shared abstraction less often than an association.** Kombine, 35 LLMs: factual association 59.0%, valid analogy 53.4%, valid blend 43.4%. Given a valid generic space, a coherent blend 97.1%. (75 retained humans were also tested; their figures of 22.1 / 32.9 / 12.8% were recorded without the metric label, so do not compare them with the LLM rates.) At model level, far-association originality predicts analogy originality r = .73 and valid blends r = .48 (d16). The hard step is finding the abstraction, not building the blend.

### 6.3 What changed behaviour, and by how much
| Intervention | Change | Judge | Source |
|---|---|---|---|
| Analogical reasoning prompt vs cross-domain prompt | Domain distance 6.99 / 6.83 / 7.53 vs 2.29 / 3.08 / 3.37; solution Vendi +90 to 173%; binary novelty up to 50 to 69% | LLM (Sonnet 4.5), human agreement 88.6% distance, 75.7% novelty | c06, c07 |
| Same, human check | 78% judged AR more novel (kappa .445); 67% reasonable | humans | c08 |
| Part-level recombination scaffold | Novelty 3.53 vs 3.146; tree distance 132.14 vs 89.35; valued 85% vs 98% (Exp 2) | 48 raters | c11, c12 |
| U2F cross-domain scaffold for software agents | Novelty 2.85 zero-shot to 4.05 (+42.1%); feasibility 4.02/5; expert approval 62% | LLM + 15 experts (kappa .65) | c28 |
| Retrieval of inspirations + novelty loop | 55.6% gain round 1, 57.8% round 2 | LLM / embedding | c22 |
| Retrieve-and-revise in rounds | Unique novel ideas 3.4x; flat after round 3 | LLM / embedding | d12 |
| Graph context + planning | Novelty 0.52 vs 0.45 next best | LLM, proxy | c25 |
| Farthest-paper context | Distance +11 to 16%; direction unchanged | embeddings | c18 |
| Greedy + random acceptance | Hit rate +7 points over greedy | authors' own predictor | d13 |
| Temperature | Cheap new combinations; not alien ones | GPT-4, embeddings | c13 |

### 6.4 The reliability problem
- LLM-rated novelty is not impact. HINDSIGHT: judge 7.44 vs 7.40 (no difference), future matching 0.297 vs 0.119, correlation with judged novelty -0.29.
- Execution erases the gap. Si 2025: AI ideas fell 1.049 / 1.760 / 1.879 points; human ideas did not move.
- Judges are weak: reviewer agreement 56.1%, best LLM judge 53.3% on the task (c09). Distance labels agree with annotators only moderately (kappa .53 to .61, c21).
- Most LLM-side numbers in this section are LLM- or embedding-judged. Treat as direction, not size.

### 6.5 Bottom line for LLMs
Raw LLMs recombine locally and sample alike. Distance helps only past a threshold, and then mostly for the strongest models. The best-supported lifts come from explicit structure (abstract, then map; rank parts; check against prior work), from different inputs rather than more samples, and from checking by execution.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = run-level record kept by code.

### Add now (established)
1. **Never select by LLM-judged novelty.** G8 already says this. This subfield adds a fourth and fifth source: HINDSIGHT judge 7.44 vs 7.40 while matching shows 2.5x; correlation with judged novelty -0.29; Si 2025 execution drop. Keep the generator out of the final selection; select by running. G / S7. [E] c26, c09, c10, K19.
2. **Far analogues belong at impasses and in open mode, not on routine items.** Spread grows with distance; the mean is not reliably higher. Matches O7's existing note. O7 / S6. [E] for spread: a09, b06, b18, d05, K04. [C] for mean: K05.
3. **Mixed policy: mostly near, familiar parts, with one or two far parts.** Uzzi core+tail 9.11 vs 5.82 vs 5.33; Mukherjee hotspot 2.2x. Do not go all-far. O7 / S3. [E] a07, b04, b17, K06. (Human-science evidence; agent effect is a test, see U-table.)
4. **When fetching inspiration, force diversity in the retrieved set, and keep it recent.** Patents citing varied-age, recent science +49% citations; low age variance offsets it. S3 grounding. [E] a15, b15, b16, b17, K10.
5. **Different samples are not different searchers.** Spread must come from different inputs (different part sets or retrieved sources), not more samples of one prompt. G4 / S3. [E] d09, b26, K27. Already in G4 and S3 fresh-context rule; this adds the cross-model figure (71 to 82%).
6. **Track directions and pairs tried; dedupe across samples.** Only about 5% of 4,000 seeds were non-duplicates (c09); GPT-4o fixates on the same parts (c12). Code keeps the history and assigns untried pairs. S3 / memory. [E] on LLM fixation in the schema (F05); this subfield adds the figures. [S] K16.
7. **Cap refinement of a blend at 2 to 3 rounds, each with new input, then regenerate.** Three sources agree on the pattern (c22, c23, d12), but all use LLM or embedding novelty. S5 / O7. [E] K21 (judge caveat).
8. **Pair distance in the agent is not journal-pair distance.** Do not borrow Uzzi's z-score without checking it against a task outcome. none. [E] K07.
9. **Budget for screening, not generation.** The supply of candidate combinations explodes (Weitzman, Tria, Youn: about 60% of new patents are new combinations). The bottleneck is checking. G7 / S4. [E] K24, K11.

### Test first
Each of these is single-source, contested or human-only. Full test design is in section 8 and UNKNOWNS.md.
1. **Explicit recombination step vs plain best-of-N at equal tokens.** Rank part pairs by familiarity; take mostly near pairs plus one far part. O7 / S3. [S] K16, K29, K15. Gap 1 in critique, no study found.
2. **Share of budget on far moves.** Sweep 0, 5, 15, 30%. O7 / G12. [S] K09, K29. Foster's 14.2% new moves is a human rate, not an optimum.
3. **Distance threshold below which a far source adds nothing.** Liu: gain only in the far 50% for the best models. O7. [S] K13, d15.
4. **Structured analogy (abstract the structure, then map) vs plain "use another domain".** O7. [S] K15 (LLM-judged).
5. **Refinement rounds: 1, 2, 4.** O7 / S5. [E] pattern, but never checked against an outcome. K21.
6. **Repeat-pair penalty within a run.** O7 / memory. [S] K03; human population finding.
7. **Purpose-near, mechanism-far part ranking with a max-min spread.** O7. [S] K26 (humans, N = 38).
8. **Several agents on different part sets vs one agent at equal tokens; vary 1, 3, 5, 9.** O7 / G. [C] K12, K31.
9. **Value threshold on blends (Dish COVER used 0.3) to keep feasibility.** S4. [S] K16.
10. **Separate goals: extend into a new topic (far blend) vs replace the current best idea (targeted rework).** O7 / O8. [S] K08.
11. **Facet-aware novelty check against retrieved prior work before expensive evaluation.** S4 / G8. [S] K23.
12. **Keep a branch that reframes the problem instead of blending.** LLMs already lean on bridging (47.1 to 64.2%). O8. [S] K28.

---

## 8. Concrete tests on our bench

Rules for every test: both arms use the same total tokens, setup cost included (G7). Use items with a verified outcome (ARC-style grid tasks with a hidden held-out example, BRAINTEASER with exact answers, code tasks with tests). Open-mode items (NoveltyBench-style) are scored by code-checked distinctness and by the bench's own validity check, never by an LLM judge (G8). Report mean and SD, not only mean; the spread is the point.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hard ARC items and BRAINTEASER items where plain pass rate is above 0 (G12 foothold) | A: plain best-of-N. B: N draws split between "near-pair blends" and "one far part" chosen from a part table, selected by code | Pass on held-out example; distinct verified solutions | B beats A by a few points on hard items only; B's SD of per-item score is wider; no gain on easy items |
| T2 | Same items | Far-move share eps = 0, 5, 15, 30% inside a greedy blend search | Best verified score at fixed tokens; hit rate | Peak at 5 to 15%; 30% falls back (Foster 14.2% is the human anchor; d13 found about +7 points over greedy) |
| T3 | Open-mode idea items with a code check (valid and not a duplicate) | Analogue distance in bins (near, mid, far 50%, far 10%) at equal tokens | Valid-and-distinct count; share valid | Valid share falls with distance; distinct count rises; gain only in far half (Liu) |
| T4 | Open-mode and stuck ARC items at impasse | A: "use another domain" prompt. B: abstract the structure, then map and solve in the analogue (O7 with typed mapping) | Distance (embedding) and verified pass | B raises distance about 3x (Shen); pass gain only if the mapping is checked by code |
| T5 | Items needing revision | Refine one blend for k = 1, 2, 4 rounds vs k fresh blends, each refinement round fed new retrieved input | Verified score mean and SD | k = 2 to 3 best; k = 4 locks in (inherited share above 70%); fresh blends higher SD |
| T6 | Open-mode items | Repeat-pair cap (a pair may be used once) vs no cap; also penalty after use 2 | Distinct verified solutions | Cap raises distinct count with no loss in best score |
| T7 | Items where part ranking is possible | Rank parts by goal similarity then pick one far-mechanism part by max-min vs surface-near vs random | Share of good (verified) blends | Max-min above surface-near and random; surface-near not above random (Hope 46 / 30 / 37%) |
| T8 | Open-mode items | k agents on k different part sets vs k agents on one part set, same total tokens; k = 1, 3, 5, 9 | Distinct verified solutions; pairwise similarity | Different part sets give lower similarity (Jiang: 0.8 within one model); gain saturates by 5 to 9 |
| T9 | Any item with a feasibility check | Blend with a value threshold vs free blending | Share valid; novelty (code distinctness) | Threshold keeps valid share (98% vs 85% in Dish COVER) at a small novelty cost |
| T10 | Open-mode items with prior-work corpus | Facet-aware novelty check (purpose, mechanism) vs embedding-only check before evaluation | Share of not-novel ideas filtered | Facet-aware well above embedding-only (89.66% vs 10.34% in Scideator) |
| T11 | Each LLM arm, any item | Check the Fleming pattern directly: mean and SD of verified score for near-pair vs far-pair blends, controlling for output length | Mean difference, SD ratio | SD ratio above 1 for far pairs; mean difference near zero or small negative. Length control matters (Verhoeven raw vs controlled sign flip) |

Count results as a pass only on a held-out check (G3). Keep per-item results so the mean-and-spread claim can be read directly.

---

## 9. What does not transfer, and why

- **Citations as usefulness.** Every empirical test of the mean-variance pattern uses later citations. A blend by an agent is judged by a check, not by being cited later. The citation lag, field effects and prestige effects do not exist for the agent.
- **The lower-mean penalty.** It appears in patents after controls (-9.1%), reverses in papers (+12.04%) and in raw patent means. It may come from human limits (surface copying, fewer tools), not from the structure of search. Liu 2026 shows the human utility cost is absent in equally original LLM ideas.
- **Exhaustion (H5).** Fleming's 37.9% is a population effect over years across inventors and cannot be split from life cycle. An agent has no life cycle. A within-run repeat penalty is a design idea, not an established result.
- **Collaboration effects.** Team benefits (cutting the poor tail, lifting the good) come from different people with different knowledge. LLM samples are alike (71 to 82% across models), so "more agents" is not "more people". The 8 to 10 member saturation (Wu) is about humans.
- **Journal-pair novelty scores.** Coarse even for papers (pseudo R2 0.33%). An agent works on tasks, not on journals.
- **Population growth models.** Tria, Youn, Pichler, Weitzman describe rates of novelty in whole systems. They give no rule for one agent on one item.
- **Disruption.** The D index and the extension-versus-replacement distinction are about literature structure. Only the conceptual split (extend vs replace) is borrowed.
- **Human-only distance results.** Hope et al. (N = 38 workers) and Foster (scientists) show human behaviour. LLM tests are required before use.
- **Execution cost.** Dish COVER spent about $42 per step and 5,600 candidates per pair; Si et al. had 43 experts working 100+ hours. Our equal-token rule rules both out.
- **Task match.** Product design (Liu), recipes (Mizrahi), NLP prompting ideas (Si), ACL abstracts (SciMON, Chen-Zhang) are not ARC grids or brainteasers. No result transfers in size.

---

## 10. Open questions

1. At equal tokens, does an explicit recombination step beat plain best-of-N on a verified-outcome benchmark? No study found. (Gap 1)
2. Best number of refinement rounds for an LLM blend. Pattern 2 to 3 across three studies, but judged by LLM or embeddings. Stable across tasks and models? (Gap 2)
3. Is the Fleming mean penalty present in LLM output when checked by outcome? Liu 2026 says no human-style cost; HINDSIGHT says judges mislead. (Gap 3)
4. Which distance measure predicts usefulness for an LLM agent? Embedding distance, Uzzi z-score, facet labels (kappa .53 to .61) and ONS disagree. Kombine shows only a model-level link (r = .48 for valid blends). (Gap 4)
5. What share of budget should go to far moves? Human data (14.2%) and a greedy-plus-random result without a stated probability. (Gap 5)
6. Is there a distance below which cross-domain prompting adds nothing, and does it hold for open-weight models and other tasks? Liu: one task, no per-open-weight result. (Gap 6)
7. Does over-reuse of one pair hurt within a run? No study. (Gap 7)
8. Do independent agents with different inputs reproduce Singh and Fleming at equal tokens? Full text of Singh and Fleming still unread. (Gap 8)
9. Direction vs distance: do far LLM blends differ in kind (ONS) or only in distance? Farthest-paper context moved distance, not direction.
10. Why do LLM far ideas keep feasibility? Safer because less extreme, or less truly far? The tail in Liu was selected.
11. Does the extension-versus-replacement split (Li, Lin, Wu) map onto "far blend" vs "targeted rework" for an agent?
12. Unread sources: Fleming-Sorenson 2001, Katila-Ahuja 2002, Kaplan-Vakili 2015 (sample 2,826 vs 2,384), Singh-Fleming 2010, Schilling-Green 2011, Kneeland et al. 2020; Uzzi's supplement. Lee et al. sample size (8,864 vs 9,428) unresolved.

---

## 11. Sources

[V] opened this session (full text or page), [M] snippet or abstract only.

**Founding and patent studies**
- [V] Fleming 2001, Recombinant uncertainty in technological search. https://funginstitute.berkeley.edu/wp-content/uploads/2012/10/Recombinant-Uncertainty-in-Technological-Search.pdf
- [V] AcaWiki summary of Fleming 2001 (not used for numbers). https://acawiki.org/Recombinant_uncertainty_in_technological_search
- [V] Verhoeven, Bakker, Veugelers 2016, Measuring technological novelty with patent-based indicators. https://lirias.kuleuven.be/retrieve/325793
- [V] Ke, Teng, Min 2021/2024, Relying on recent and temporally dispersed science. https://arxiv.org/pdf/2107.09176
- [V] Youn, Bettencourt, Strumsky, Lobo 2015, Invention as a combinatorial process. https://arxiv.org/pdf/1406.2938
- [V] Kaplan and Vakili 2015 abstract page. https://lbsresearch.london.edu/id/eprint/73 (sample size inconsistent; also [M] https://doi.org/10.1002/smj.2294)
- [M] Fleming and Sorenson 2001. https://doi.org/10.1016/S0048-7333(00)00135-9
- [M] Fleming and Sorenson 2004. https://doi.org/10.1002/smj.384
- [M] Katila and Ahuja 2002. https://doi.org/10.5465/3069433 ; https://www.semanticscholar.org/paper/f57a5bb751f2bcce40b64ab86f9ea17470eeda87
- [M] Singh and Fleming 2010. https://pubsonline.informs.org/doi/epdf/10.1287/mnsc.1090.1072
- [M] Kneeland, Schilling, Aharonson 2020. https://pubsonline.informs.org/doi/fpi/10.1287/orsc.2019.1328
- [M] Schilling and Green 2011. https://ideas.repec.org/a/eee/respol/v40y2011i10p1321-1331.html
- [M] Fleming 2007, Breakthroughs and the long tail. https://sloanreview.mit.edu/article/breakthroughs-and-the-long-tail-of-innovation/

**Science-side studies**
- [V] Uzzi, Mukherjee, Stringer, Jones 2013, Atypical combinations and scientific impact. https://www.kellogg.northwestern.edu/faculty/uzzi/htm/papers/Science-2013-Uzzi-468-72.pdf ; https://www.science.org/doi/10.1126/science.1240474 (supplement not opened)
- [V] Wang, Veugelers, Stephan 2017, Bias against novelty in science. https://www.nber.org/papers/w22180.pdf
- [V] Foster, Rzhetsky, Evans 2015, Tradition and innovation in scientists' research strategies. https://arxiv.org/pdf/1302.6906
- [V] Lee, Walsh, Wang 2015, Creativity in scientific teams. https://doi.org/10.1016/j.respol.2014.10.007 ; https://lirias.kuleuven.be/retrieve/289808
- [V] Mukherjee, Romero, Jones, Uzzi 2017, Age of past knowledge and tomorrow's breakthroughs. https://www.kellogg.northwestern.edu/faculty/jones-ben/htm/The_Hotspot_%20Science_Advances_2017.pdf
- [V] Li, Lin, Wu 2024, Can recombination growth lead to scientific breakthroughs? https://arxiv.org/abs/2402.16839v1 (file read for a16, no URL recorded)
- [V] Li, Lin, Wu 2025, Can recombination displace dominant scientific ideas? https://arxiv.org/abs/2506.15959 ; https://arxiv.org/pdf/2506.15959
- [V] Bornmann, Tekles, Zhang, Ye 2019, Do we measure novelty when we analyze unusual combinations of cited references? https://arxiv.org/abs/1910.03233 ; https://arxiv.org/pdf/1910.03233
- [V] Fontana, Iori, Montobbio, Sinatra 2020, New and atypical combinations (publisher summary page only). https://csh.ac.at/publication/new-and-atypical-combinations-an-assessment-of-novelty-and-interdisciplinarity/
- [V] Wu, Wang, Evans 2019, Large teams develop and small teams disrupt (manuscript). Nature; no URL recorded in evidence d07.

**Models and theory**
- [V] Weitzman 1998, Recombinant growth. https://dash.harvard.edu/server/api/core/bitstreams/7312037c-8477-6bd4-e053-0100007fdf3b/content
- [V] Tria, Loreto, Servedio, Strogatz 2014, Dynamics of correlated novelties. https://arxiv.org/pdf/1310.1953
- [V] Pichler, Lafond, Farmer 2020, Technological interdependencies predict innovation dynamics. https://arxiv.org/abs/2003.00580
- [M] Levinthal 1997, Adaptation on rugged landscapes. https://doi.org/10.1287/mnsc.43.7.934
- [M] Arthur and Polak 2006, Evolution of technology within a simple computer model. https://doi.org/10.1002/cplx.20130 (secondary summary only)

**Language-model studies**
- [V] Liu, Dubova, Conklin, Harada, Griffiths 2026, Assessing the effect of cross-domain mapping on creativity in humans and LLMs. https://arxiv.org/abs/2603.19087
- [V] Shen, Druckmann, Zou 2026, Unlocking LLM creativity in science through analogical reasoning. https://arxiv.org/abs/2605.11258
- [V] Si, Yang, Hashimoto 2024, Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto, Yang 2025, The ideation-execution gap. https://arxiv.org/abs/2506.20803
- [V] Mizrahi, Shani, Stanovsky, Jurafsky, Shahaf 2025, Cooking up creativity. https://arxiv.org/abs/2504.20643
- [V] Hernandez et al. 2024, Alien recombination. https://arxiv.org/abs/2411.11494
- [V] Tang and Yang 2026, AI research agents narrow scientific exploration. https://arxiv.org/abs/2605.27905
- [V] Liu, Butler, Machlanski, Bueno, Tsaftaris 2026, LLMs extend known research but do not create. https://arxiv.org/abs/2610.17439 (refinement figures [M])
- [V] Scideator 2024. https://arxiv.org/abs/2409.14634
- [V] Wang et al. 2023, SciMON. https://arxiv.org/abs/2305.14259
- [V] Chen and Zhang 2026, Combinatorial innovation and multi-agent iteration. https://www.alphaxiv.org/abs/2604.20548
- [V] Llull-style combinatorial ideation 2025. https://arxiv.org/html/2508.19200v3
- [V] Li, Tu, Han 2026, Graph2Idea. https://arxiv.org/abs/2606.09105
- [V] Jiang 2026, HINDSIGHT. https://arxiv.org/abs/2603.15164
- [V] Bao, Wu, Liu, Li, Cao, Evans 2026, Contemporary AI lacks the imagination to diverge or negate in science. https://arxiv.org/abs/2606.08251
- [V] Ye and Liu 2025, U2F. https://arxiv.org/abs/2511.03517
- [V] Kombine / Combinatorial Creativity benchmark 2025. https://arxiv.org/abs/2509.21043 ; https://arxiv.org/html/2509.21043
- [V] Jiang et al. 2025, Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Hope, Chan, Kittur, Shahaf 2017, Accelerating innovation through analogy mining. https://arxiv.org/abs/1706.05585
- [V] Hu et al. 2024, Nova. https://arxiv.org/abs/2410.14255
- [V] Chen, Zhang, Li et al. 2025, Structuring scientific innovation. https://arxiv.org/abs/2503.18865
- [V] Chen, Zhao, Cohan 2026, Measuring the gap between human and LLM research ideas. https://arxiv.org/abs/2607.01233
- [V] Sato 2026, ReMIND. https://arxiv.org/abs/2601.07121
- [M] Peeperkorn et al. 2024, cited second-hand in Mizrahi et al. (c29). https://arxiv.org/abs/2504.20643

*Note on the three numbers that differ across sources: Lee et al. sample 8,864 vs 9,428; Kaplan-Vakili 2,826 vs 2,384; Wang 773,311 articles vs 1,056,936 field-article observations (both correct, different units).*

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 13 established claims: 7 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E14.01-K10** (reworded: the sources support less). Ke et al. (+49% 10-year citations, +117% top-5% odds, +171% top-1%) and Mukherjee (2.2x) verified, but the +49%/+117% belong to patents citing science at all; recency adds to this and low age variance offsets the recency gain, so 'only when recent and varied' is wrong. Corrected claim: Patents that cite scientific papers get 49% more 10-year citations and 117% higher odds of being top-5% hits (171% for top 1%) in Ke et al.; among them, citing more recent science adds further impact, but that gain is offset when the cited papers' ages have low variance (Mukherjee et al.: recent and age-varied sources are about 2.2 times as likely to be top 5%).
- **E14.01-K19** (reworded: the sources support less). HINDSIGHT numbers (7.44 vs 7.40, 0.297 vs 0.119, 2.5x, r=-0.29) verified, but Si 2025 does not show novelty rating surviving: AI ideas' novelty scores fell 1.05 points after execution (human -0.01), the human-AI difference at execution is non-significant on novelty simply because the AI advantage vanished. Corrected claim: LLM-rated novelty does not predict real later impact: in HINDSIGHT, LLM-judge scores are equal for grounded and vanilla ideas (7.44 vs 7.40) while matching to future papers shows a 2.5x gap (0.297 vs 0.119), and the HINDSIGHT score correlates -0.29 with LLM-judged novelty. Si et al. 2025 point the same way: AI ideas rated more novel before execution lost 1.05 novelty points and 1.88 effectiveness points after experts ran them, while human ideas lost almost none.
- **E14.01-K21** (reworded: the sources support less). Chen & Zhang (70.6% new at turn 1, 78.3% inherited at turn 3, diversity/novelty peak early near iteration 2) and SciMON (55.6%, 57.8%) numbers verified, but SciMON shows gains still rising at iteration 2, not a sweet spot, and Nova's 3.4x is the framework versus no framework (only 3 rounds run), not growth over rounds; only the no-planning ablation (42.4 to 44.1) is flat. Corrected claim: Iterating recombination appears to have a sweet spot in one study: in Chen and Zhang, diversity and novelty peak near the second iteration while later rounds lock onto the previous version (70.6% new entities at turn 1, 78.3% inherited at turn 3). SciMON's novelty loop still raised novelty on iteration 2 (55.6% of ideas on iteration 1, 57.8% of continuing ideas on iteration 2), and Nova's planned retrieval gives 3.4 times more unique novel ideas than no framework over 3 rounds, with the no-planning ablation flat between rounds 2 and 3 (42.4 to 44.1). All judge novelty with LLMs or embeddings, not outcomes.
- **E14.01-K24** (reworded: the sources support less). Only Weitzman (1998) says the bottleneck is turning ideas into usable form (PDF text not machine-readable here; abstract wording known); Tria 2014 and Pichler 2020 abstracts model rates only and say nothing of a usability bottleneck, and Arthur-Polak 2006 has no evidence line. Corrected claim: Weitzman (1998) models growth as recombination of old ideas, with the supply of possible combinations exploding and the binding limit being the ability to process them into usable form; Tria et al. (2014) and Pichler et al. (2020) model rates of novelty and innovation (Heaps law, network dependencies) and do not address usability. Evidence in this set is about rates, not usefulness.
- **E14.01-K27** (reworded: the sources support less). Numbers confirmed (79%, 71-82%, 19.9%/412 of 2,070), but the 79% comes from 100 queries (Infinity-Chat100) not all 26K prompts, 71-82% is embedding similarity not agreement, and the conclusion that spread must come from different inputs is not tested by either source. Corrected claim: Several LLM samples are not independent: on 100 open-ended queries (50 responses each, top-p 0.9, temperature 1.0) one model gave average pairwise embedding similarity above 0.8 in 79% of cases, and responses from different models had average pairwise similarity of 71% to 82% (Jiang et al. 2025); in Kombine 19.9% (412 of 2,070) of invented concepts reuse two or more properties of another model concept. This suggests that more samples of one prompt or model add little spread; that diversity must come from different inputs is an inference, not a tested result.
- **E14.01-K30** (reworded: the sources support less). Fleming numbers confirmed in full text and Foster 85.8/14.2 found in the arXiv preprint, but the Uzzi paper itself prints both sets: body text says 36.1, 39.8, 49.7% while the Fig. 3 caption says 36.2, 39.9, 49.7%, so the earlier values are not mere transcription slips. Corrected claim: Fleming (2001) full text confirms its core numbers (n = 17,264; +11.3% per SD component familiarity; +10.3% per SD combination familiarity; 37.9% of baseline at max cumulative use). Uzzi et al. print the team shares inconsistently: 36.1, 39.8 and 49.7 percent in the body text and 36.2, 39.9 and 49.7 percent in the Figure 3 caption. Foster et al. report 85.8 vs 14.2 repeat/new (arXiv preprint). Singh-Fleming 2010, Fleming-Sorenson 2001, Katila-Ahuja 2002 and Kaplan-Vakili 2015 are still unread.
