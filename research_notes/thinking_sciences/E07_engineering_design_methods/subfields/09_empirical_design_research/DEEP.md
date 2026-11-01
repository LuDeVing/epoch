# Empirical design research: deep document

*Subfield E07.09, "Metrics of ideation" (key work: Shah, Smith and Vargas-Hernandez 2003). Why it matters for our agent: it tells us what to measure when the agent generates ideas, and which measures can be trusted. Built from evidence_a-d.jsonl, claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids (a01, b09, d07 ...) point to those files. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. The 2024-2026 preprints cited here use arXiv ids as given in the evidence files; several are single-group results.*

## 1. What it is

Ideation metrics are the numbers researchers use to say how good a set of ideas is. The field started in engineering design, where a team brainstorms many concepts for one brief and someone has to score the session.

Shah, Smith and Vargas-Hernandez (2003, Design Studies 24(2):111-134) proposed four measures. We opened the full paper (d01-d03).

- **Quantity.** The raw count of ideas. Each idea counts separately, because variety already catches trivial variants.
- **Quality.** A task-specific score against the design specification, M2, on a scale of 10.
- **Novelty.** How unusual one idea is. Two forms: a priori (against an expert scale of known solution types) and a posteriori (against the other ideas in the same session).
- **Variety.** How far apart the ideas are, scored on a genealogy tree.

Quantity and variety score a set. Quality and novelty score single ideas (b01).

Since 2023 the same words are used for language-model output. Researchers swap the human-rated tree for text embeddings and measure pairwise distance, cluster count or distance to a control pool. This document covers both lines: the human design-research metrics and the LLM studies that use or test them.

For our agent the question is practical. The schema's open mode (S3, S4, S7) generates many candidates and lets code select. Code needs a score for "are these candidates really different" and "is this one rare". The metrics literature says which scores are cheap, which are trustworthy and which are traps.

## 2. History and theories in depth

**Background (not opened this session, general knowledge).** Brainstorming (Osborn) and divergent-thinking tests (Guilford, Torrance) scored fluency, flexibility, originality and elaboration. Design fixation work (Jansson and Smith 1991) showed that showing a designer an example makes the designer copy its features. Girotra, Terwiesch and Ulrich (2010) argued that the best idea in a set improves with the number of ideas, the average quality and the variance. The last is restated in Terwiesch et al. 2026 (d08). We could not read Girotra 2010 itself.

**Shah, Kulkarni and Vargas-Hernandez (2000).** An earlier ASME paper that compared idea-generation methods with measures that became the 2003 set (a03). Reference line only. The 2000 numbers are unread. This is a known gap.

**Shah et al. 2003, the keystone (opened, d01-d03).**

- *Novelty.* M1 = sum over functions j and stages k of f_j * S1_jk * p_k. The weights f_j (function importance) and p_k (stage importance) are chosen by the rater. The a posteriori score is S1 = (T - C)/T * 10, where T is the number of ideas for that function and C is how many used the same solution. The a priori score uses an expert-built scale (in the worked example only the values 3, 7 and 10).
- *Variety.* Ideas are sorted into a genealogy tree per function. Four levels with fixed weights: physical principle 10, working principle 6, embodiment 3, detail 1. M3 = sum_j f_j sum_k S_k * b_k / n, where b_k is the number of branches at level k and n the number of ideas. A level with only one branch scores zero. The weights were "assigned" so a split at a high level always beats splits below. There is no empirical fit and no sensitivity test.
- *Worked examples.* Variety: n = 11 ideas, branches 2/5/6/4 across the four levels, M3 = (2*10 + 5*6 + 6*3 + 4*1)/11 = 72/11 = 6.54. A two-function example gave a low-variety set 2.6 and a high-variety set 8.7. Novelty: 46 aircraft-like entries, attribute weights thrust 0.35, medium 0.35, motion 0.20, pieces 0.10. Entry 1 scored 3.00 a priori and 3.28 a posteriori.
- *Validation.* Correlation between the two novelty versions: 0.944. Correlation of each with peer ratings: 0.624 (a posteriori) and 0.591 (a priori). The raters were the competing students, not experts. The paper gives no inter-rater number for tree placement.
- *The quantity-to-quality belief.* The authors state it with citations. They do not test it.

**Later human-side work (mostly unread).** Nelson et al. 2009 merged novelty and variety into one design-space measure (d21, second-hand). Linsey 2011, Sarkar and Chakrabarti 2011, Verhaegen 2013 and Oman 2013 are only names in reference lists (a29). Sio, Kotovsky and Cagan (2015) meta-analysed over 40 fixation studies (d20, second-hand). Two citing papers describe its headline in conflicting ways, so we use neither.

**The usage review (opened, b01-b05).** Fiorineschi and Rotini (2023, Design Science 9:e11) read the 739 papers that cite Shah 2003 (Scopus, March 2021; 686 retrievable). Only 61 (about 9%) used the original novelty metric. Another 72 used a modified version. Of the 61, 63.9% used the a posteriori form, 8.2% a priori, 3.3% both, 24.6% did not say. Inter-rater tests were rare with no trend over years. Most papers did not say how they chose attributes and weights. All use found was academic; none in industry. The authors call the lack of inter-rater tests "a disappointing surprise". They also separate two ideas: a posteriori novelty is psychological novelty (new to this group), a priori is historical novelty (new to the field).

**Known weaknesses of the a posteriori score (b04, second-hand through the review).** It has no historical novelty. It can be too high when similar solutions are common. It changes when attributes are missing or extra. Fiorineschi's 2019-2021 series proposed variants and a refined metric (a05, titles only).

**Moving to embeddings (2023-2026).** Ma et al. (2023) used convex-hull volume and cosine similarity to a crowd set for GPT-3 designs. Sankar and Sen (2024-2025) clustered embeddings with UMAP and DBSCAN to replace rated variety. Terwiesch et al. use 1 minus mean pairwise cosine. Carichon et al. (2026) use distance to a control pool. These are programmatic cousins of Shah's variety and a posteriori novelty. Almost none has been checked against genealogy-tree variety (section 5).

**Competing explanations for the main LLM result (AI sets are less varied than human sets).**

1. Real homogeneity: models share training data, so samples are alike (Jiang et al., a14).
2. Measurement artefact: the embedding or threshold exaggerates it (Schaeffer et al., a15).
3. Style artefact: LLM text is uniform, so embeddings see sameness (Terwiesch: a style-neutral rewrite kept 80-90% of the gap, d09).
4. Workflow: it matters whether everyone sees the same AI output (Wan and Kalman, Ashkinaze).

Explanations 2 and 3 explain a part. Explanation 1 survives both (section 5).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Shah 2003 variety formula, level weights 10/6/3/1 | Fig. 4 example n=11, branches 2/5/6/4, M3 = 72/11 = 6.54 | Shah et al. 2003 (d02) | [E] formula; weights are a design choice |
| A posteriori novelty (T-C)/T*10; two novelty versions agree | r = 0.944 between versions; each vs peer rating 0.624 (post) and 0.591 (prior) | Shah et al. 2003 (d01) | single paper; raters were students |
| Original Shah novelty metric is rarely used faithfully | 61 of 686 retrievable citing papers (about 9%); 72 modified; 24.6% of the 61 name no novelty concept | Fiorineschi and Rotini 2023 (b02, b03) | [S] one review |
| LLM research ideas rated more novel than expert ideas, blind | novelty 5.64 (AI) and 5.81 (AI + human rerank) vs 4.84; 79 reviewers; 119/109/109 reviews; 49 ideas per condition; excitement 5.19/5.46 vs 4.55; feasibility 6.34/6.44 vs 6.61 (n.s.) | Si et al. 2024 (b06, c10) | [S] |
| Reviewers barely agree on idea quality | human balanced accuracy 56.1% (chance 50); NeurIPS 2021 66.0, ICLR 2024 71.9; LLM judges 43.3-53.3 | Si et al. 2024 (b07, c12) | [S] |
| Over-generation hits a diversity wall | 4000 seeds per topic, all-MiniLM-L6-v2, duplicate = cosine > 0.8; about 200 non-duplicates (about 5%) | Si et al. 2024 (b08, c11) | [E] with Jiang |
| AI novelty advantage vanishes after execution | N=43 (19 human, 24 AI ideas); gap in score drop: novelty 1.039, excitement 1.835, effectiveness 1.827, overall 1.348; FDR p .025/.001/.003/.004. AI ideas dropped 1.049/1.760/1.879; human ideas -0.010/+0.078/-0.052 | Si et al. 2025 (b09, c13) | [S] |
| Ideation scores barely predict execution scores | Pearson r from -0.321 to 0.205 across metrics, AI and human ideas (N=24 and 19) | Si et al. 2025 (b10) | [S], very imprecise |
| Same-prompt answers are highly alike | pairwise similarity typically > 0.8 at top-p 0.9, temp 1.0; min-p: 81% of pairs > 0.7, 61.2% > 0.8; 100 queries x 50 samples | Jiang et al. 2025 (a14, c16) | [E] direction, size contested |
| Different models also answer alike | cross-model similarity 0.71-0.82; DeepSeek-V3 vs qwen-max 0.82, vs gpt-4o 0.81; 31,250 annotations, 25 raters per item | Jiang et al. 2025 (c17) | [C] size |
| Harder null removes much of the headline | same prompt, truly distinct ideas: 20-32% of pairs already > 0.8; different-cluster pairs > 0.7 in 61% and > 0.8 in 32% | Schaeffer et al. 2026 (a15) | reanalysis, preprint |
| Human pools beat LLM pools on diversity | GPT-4 zero-shot gap B = 0.193 (CI 0.182-0.204), few-shot 0.207; 32 of 32 alternative measures lower for AI; 400 ideas (200/100/100) | Terwiesch et al. 2026 (b13) | [E] |
| Gap is not only a style artefact | gap 0.193 to 0.154 (80% kept) zero-shot; 0.207 to 0.186 (90% kept) few-shot after neutral rewrite | Terwiesch et al. 2026 (d09) | [E] with d10 |
| Category-based measure confirms the gap | 28 (human) vs 22 (GPT-4o) categories; 206 vs 88 unique combinations (990 ideas each) | arXiv 2602.20408 (d10) | [S] |
| Diversity ranking by intervention (1 - pairwise cosine, USE) | humans 0.773; random personas 0.757; random constraints 0.735; CoT 0.698; GPT-4o zero-shot 0.679; GPT-4 zero-shot 0.585; refine twice 0.575; GPT-4o independent single-idea sessions 0.452; CIs about +-0.009 | Terwiesch et al. 2026 (b14, d07) | [E] across study families |
| Chain-of-thought lowers pairwise similarity | human 0.243; CoT 0.255; base about 0.38; 35 prompts, 10 sessions of 100 ideas; unique ideas about 3700 (base) vs 4700 (CoT) | Meincke et al. 2024 (c14, c15) | [S] working paper |
| Self-refinement lowers pool diversity | 0.679 to 0.575 (-0.104, GPT-4o); duplicate rate 0.022 to 0.238 under uniform refinement; Self-Refine on Claude 25/56 vs base 30/56 | b14, d05, a16 | [E] |
| Refining only a few chosen candidates is enough | strong non-duplicate yield: refine all 21.80; random-4 22.18; MMR-4 23.70; tokens 115.4k / 105.0k / 105.2k; duplicate rate 0.238 / 0.186 / 0.172; raw and rerank 0.00 | Budgeted Subset Refinement 2026 (d05) | [S] LLM-rated proxy |
| Structured divergence raises path discovery | GPT-5.4 27/56 to 38/56 (48.2 to 67.9%); Claude Sonnet 4.6 30/56 to 41/56 (53.6 to 73.2%); Llama 4 Maverick 13/56 to 29/56; Qwen3-235B 22/56 to 36/56 | MUTATE, Park et al. 2026 (a16) | [S] |
| Theme-first chain of thought | combinations 39.15 to 55.49; categories 18.45 to 24.84; persona + CoT 56.97 to 65.42 combinations | arXiv 2602.20408 (d12) | [S] |
| Recoding-decoding keeps finding new clusters | 250 ideas gave 244 clusters vs 35 ordinary; all 5 outputs distinct for 95.0% of prompts vs 85.0% Verbalized Sampling, 82.0% human, 15.0% ordinary | arXiv 2603.19519 (d06) | [S], no equal-token control |
| Method prompts: simple beats elaborate | 567 conditions, 25 prompts, 5 models, 14,350 prompts; every method beat control; short "think outside the box" beat long method prompts; cross-model distance only 0.206-0.341; top-5 novelty gain up to about +41% | IDEAFix, Carichon et al. 2026 (a13, a24) | [S] |
| Context-aware avoidance beats blind resampling | one session writing many ideas 0.679; independent one-idea sessions 0.452 | Terwiesch et al. 2026 (d07) | [E] direction |
| Diversity forcing does not buy executed success | 3,222 executed runs; MAP-Elites and Go-Explore most diverse; no idea rated Original; 1 of top-10 by quality is also near-novel; best novel idea 3.2% and 6.0% behind best overall | Heuresis 2026 (d04) | [S] |
| Coverage grows slowly with N, no plateau by 1,000 | mean nearest distance 0.546 (N=100) to 0.478 (N=1,000); max 0.762 to 0.711 | Terwiesch et al. 2026 (d08, b15) | [S] |
| Embedding vs experts: coarse yes, mechanism no | whole-text cosine 0.511-0.562 accuracy (chance 0.5), BERTScore 0.481, structure graph 0.871 (233 triples, 12 engineers); coarse same/near/far clusters matched 30 experts in 10 of 12 | StructSim (d13); Sankar and Sen (d14) | [S] each; together a clear pattern |
| LLM novelty judges are unstable | one prompt sentence shifts pairwise accuracy by 52.6 points (gpt-5.4); tie rate up to 35%; five novelty scorers range 2.28-3.83 on a 5-point scale | Sternlicht et al. 2026 (c24); Sankar and Sen (c07) | [E] |
| Novelty metrics disagree across tasks | Pearson r as low as -0.25; diversity and quality metrics agree (within-task r >= 0.84 for TTCT) | CreativityPrism (c18, c19) | [S] |
| Calibrated VLM judge reaches expert level on some dimensions | expert-expert kappa: uniqueness 0.54, creativity 0.26, usefulness 0.59, drawing quality 0.33; best judge met 0.80 of that on uniqueness and drawing quality; about 875 sketches | Edwards et al. 2025 (d15) | [S] |
| Experts disagree on exact scores, agree on top half | Krippendorff alpha for innovativeness 0.33/0.47/0.46; Jaccard of above-median sets 0.71/0.43/0.54; about 3,000 scores on 300 ideas | Hirota et al. 2026 (d16) | [S] |
| Individual rating up, collective diversity down (humans using AI) | Doshi and Hauser: novelty +5.4% (b=.207, p=.021) and +8.1% (b=.311), similarity b=.871 and .718; 500 writers, 293 stories, 3,519 ratings. Anderson: ideas 8.39 vs 7.32 (+15%), categories +27%, group distance .24 vs .28 (p=.038, d=.47), individual p=.352 | b16, b18 | [E] direction, [C] size |
| Homogenization not always replicated | Wan and Kalman N=97, F(2,94)=0.573, p=.57, power 55.4%, about 165 needed; Ashkinaze 844 people, diversity up, Cliff's delta .31 (disclosed) and .26 (undisclosed) | b17, d17 | [C] |
| AI as editor, not source, spares diversity | AI ideation b=0.036 (p<.001); AI refinement b=0.007 (p=.516); 644 writers; best simulated pool (Claude Sonnet 4.6) recovered 75.3% of human diversity | Dong and Yakura 2026 (b23) | [S] preprint |
| LLM session fixates like a human session | categories per 10 ideas 12.68 vs 12.46 (p=.45); slope 1.035 vs 1.013 (p=.51); human seed did not help (18.35 vs 18.34) | arXiv 2602.20408 (d11) | [S] |
| Human fixation rises with AI images | N=60, fixation .32 (GenAI) and .27 (image search); BF 124 for GenAI | Wadinambiarachchi et al. 2024 (b20) | [S], humans not LLMs |
| LLM-led build team did well but fixated | ranked 2nd of 6; 14.8 m vs winner 37 m; 97 prompts, 116 prototypes; built only 3 common concepts and dropped pneumatics after one iteration | Egea et al. 2024 (a06, b22) | [S] n=1 |
| Creativity prompts move variability only part way | variability 0.459 base, 0.576 "very creative" with reward line, human 0.738; originality 0.711 vs 0.696 human | Wenger and Kenett 2025 (c20, c21) | [S] |
| More critic agents or rounds give diminishing returns | non-duplicate ratio 0.69 single pass, 0.77 self-critique, 0.80 three critics; gain stops after 3 turns; another study: after about 3 agents or 8 rounds | c27, b25 | [E] shape |

## 4. Mechanisms and models

All items below can be coded. They need no judge model.

**4.1 A posteriori novelty on tagged attributes.**
1. Fix the attribute list and weights before the run. Example: purpose, mechanism, implementation. Freeze them and log them. Changing them changes the score (b04).
2. A model fills each candidate's tags in a fixed vocabulary or short free text, normalised by code.
3. For each attribute i, T = number of candidates, C = number sharing this candidate's tag. S_i = (T - C)/T * 10.
4. Novelty = sum_i f_i * S_i.
5. It means "rare inside this pool". It does not mean new to the world. It can be inflated when the pool is full of copies of outside ideas, so check it against the pool's duplicates (b04).

**4.2 Genealogy-tree variety, agent version.**
1. Tag each candidate at four levels: physical principle, working principle, embodiment, detail.
2. Build the tree by code from the tags.
3. M3 = sum_k S_k * b_k / n, with S = 10/6/3/1 and b_k the branch count at level k. A level with one branch scores zero.
4. The paper has no sensitivity test of the weights, so also log raw branch counts per level.
5. Worked check: n = 11, branches 2/5/6/4 gives 6.54. Use this to unit-test the code.

**4.3 Embedding set metrics.**
- Pool diversity = 1 minus mean pairwise cosine. Fix one embedding model (Terwiesch used the Universal Sentence Encoder).
- Cluster count: cluster candidates by a fixed rule and count clusters. Sankar and Sen used UMAP + DBSCAN. Dedup cuts used cosine 0.8 (Si), 0.82 (Budgeted Subset Refinement), 0.73 and 0.83 (recoding-decoding). The thresholds are choices.
- Convex hull volume (Ma et al.): sensitive to outliers and dimension. Low trust.
- Coverage of a reference set: mean nearest distance from each reference idea to the closest sample (Terwiesch, d08).
- Non-duplicate yield: count of candidates that are not above the cut to any earlier one. Stop sampling when its rate stops rising (c11, c27).
- Calibrate with a matched null (Schaeffer): same prompt, truly distinct ideas. Report your score for the null beside your score for the real pool.

**4.4 Mechanism-level comparison.** Whole-text cosine is near chance on "same mechanism" calls (0.51-0.56; d13). Tag purpose, mechanism and implementation, build a small graph, compare tags (StructSim got 0.871). Use cosine only as a pre-filter that proposes pairs.

**4.5 Path-level divergence (MUTATE).** Define the target set of mechanism-distinct ways to reach one goal. Count how many the agent found (path discovery, 56 scenarios). This is the agent-native version of the working-principle level. Separately count action-level divergence (first moves). Breadth of candidates and discovery of a new mechanism are different skills (a25: Claude Sonnet 4.6 and Qwen3-235B give many candidates but rotate inside one mechanism).

**4.6 Set-level reward.** A reward on single-answer quality pushes toward sameness (Dong and Yakura: individual ratings rose while the pool shrank). If ideation is ever optimised, include a set term. Use it as a diagnostic first (Heuresis: spread did not predict executed quality).

**4.7 Novelty gated by a pass.** Padmakumar et al. define novelty as the harmonic mean of unseen n-gram fraction and a quality score. The idea carries over: a candidate counts as novel only if it also passes the check. In our schema this is S4 (run it) before S7 (select).

**4.8 Process metrics from the trace.** Cheap ones from Egea: share of turns spent generating vs iterating, number of concepts built, concept switches, how long a concept is tested before abandonment. Fixation score from Wadinambiarachchi: share of an example's features copied by an output.

## 5. What holds up

**Replicates well.**
- Same-prompt LLM output is highly redundant. Si (about 5% non-duplicates at 0.8), Jiang (>0.8 typical), Meincke (base 0.38 vs human 0.243) and Terwiesch (gap 0.193, 32 of 32 measures) agree in direction. Several measures and embeddings are used. [E]
- The human-LLM gap is not just style. The style-neutral rewrite (80-90% kept) and a non-embedding category count (22 vs 28; 88 vs 206) both keep it.
- Self-refinement of a pool lowers diversity: Terwiesch (-0.104), Budgeted Subset Refinement (duplicate rate 0.022 to 0.238) and MUTATE's Self-Refine (25/56 vs 30/56). Counter-case: refining a person's own idea (Dong and Yakura) preserves diversity. The cases differ in what is refined.
- LLM novelty judges are unreliable. Five separate papers (Si, Sternlicht, Sankar and Sen, CreativityPrism, Hirota) point the same way. Human experts also agree poorly on fine-grained novelty (alpha 0.33-0.47).

**Contested.**
- Size of cross-model homogeneity. Jiang 0.71-0.82; Schaeffer shows a harder null reproduces 20-32% of pairs above 0.8. Schaeffer is a reanalysis, not a rerun with new human data. The embedding model is a free parameter.
- Whether AI use homogenises human work. Four of six designs read show lower variety (Doshi and Hauser, Anderson, Terwiesch, Dong and Yakura). One null at 55% power (Wan and Kalman). One reversal (Ashkinaze). This is our own tally, not a formal meta-analysis (b28). Likely moderator: whether everyone sees the same AI output. Anderson's comparison arm was a card deck, not no-aid. Doshi and Hauser's own text does not contain the "10.7% and 8.9%" similarity rises. That wording is Wan and Kalman's (critique correction). The Doshi numbers are b=.871 and .718.
- Novelty of AI ideas. Si: AI more novel (expert raters, paper ideas). Terwiesch: human ideas more novel (40.6% vs 36.7% and 36.1%; crowd raters, product ideas). The execution study: AI edge gone after execution. Judges, domains and model years differ.
- Persona benefit. Raises diversity in LLM-only pools (87.41 vs 82.93, d=1.43; 0.757 vs 0.679; ordinary persona matched humans at 210 combinations). Eccentric prompts lose the gain (non-monotonic, p<.001). Did not reliably change human outputs. Dong and Yakura: simulated persona pools stayed below all human pools. Doudkin's +5.69 gain comes from an LLM judge that scored humans 10.22 on a 1-10 scale, so we do not trust it.

**Failures and weak spots.**
- No peer-reviewed meta-analysis of the homogenization claim was found.
- Shah metric reliability is rarely checked (b03). We found no study that correlates embedding variety with genealogy-tree variety, even where both families were used (Ma et al.). This is the central unmeasured link.
- The ideation-to-execution link is weak: r between -0.32 and 0.21 (N=43), and Heuresis found spread did not predict quality or novelty over 3,222 executed runs. But both are research or ML ideas, not engineering artefacts.
- ALIA-style pilots (b27, c28) rely on self-rating, six groups, no inferential test. Not evidence.
- Human baselines unread: Sio 2015, Nelson 2009, Shah 2000, Girotra 2010, Linsey. We cannot say how well the Shah quantity-quality belief replicates in human design studies.
- Egea (n=1 LLM team), Wadinambiarachchi (N=60, Midjourney), Diamond of Thought (6 raters, p=.89 for DoT vs human total) are small.

**Interventions that worked** (single group unless noted): context-aware avoidance (0.679 vs 0.452); random personas or constraints (0.757, 0.735); theme-first chain of thought (combinations +42% on GPT-4o; similarity 0.255 vs about 0.38 for Meincke's CoT); diversity-aware choice of 4 candidates to refine; code-tracked forced divergence (MUTATE ReDNA, recoding-decoding); short explicit divergence words over long method prompts.

**Interventions that did not work:** raising temperature or using min-p (Jiang; saturates, degenerate text at high temperature per Dong and Yakura); a fixed "be diverse" word (Ma: 0.627 to 0.805 on one problem, 0.738 to 0.675 on another); creativity wording alone (variability 0.459 to 0.576 vs human 0.738); few-shot examples in GPT-3 (narrower hull, 0.2 vs crowd 0.294); refine-all; more than about 3 critics, 8 rounds or a fourth turn; seeding an LLM with a human first idea (no gain). Pooling vendors is mixed: cross-model similarity is still 0.71-0.82, yet the Terwiesch composite of four vendors did approach human level.

**Embedding choices.** Accuracy on mechanism-level calls: text-embedding-3-small 0.524 (0.562 with keyphrase concat), MiniLM 0.511 (0.524), BERTScore 0.481, structure graph 0.871. No study gives an error rate for a cosine threshold like 0.8.

## 6. Language models

**Single answers look fine, sets do not.** On divergent-thinking tests LLM answers are as original as human ones (0.711 vs 0.696) but the population of answers is much less varied (0.459 vs 0.738; Wenger and Kenett, 22 LLMs vs 102 humans). CreativityPrism (17 LLMs, 8 tasks): big models win on quality, with no significant lead in divergent thinking.

**Quality up, novelty down, variety down (early models).** Ma 2023 (GPT-3): more feasible, less novel than crowd, convex hull 0.186-0.266 vs 0.294. Terwiesch Study 1 (GPT-4, March 2023): purchase intent 46.4% and 49.3% vs 40.4%; top-10% share 15 and 20 of 40 vs 5 human; novelty 36.7% and 36.1% vs 40.6%; novelty vs intent r = -0.078. Quality and novelty move apart, so score them separately.

**Repetition inside a model.** At temperature 1.0, same-prompt similarity is above 0.8. Within one long generation GPT-3 repeats the same idea with small wording changes. For 4000 seeds Si got about 200 non-duplicates. Newer models are somewhat more diverse than March 2023 GPT-4 (except o3-mini, fixated on desk organizers) but none matched humans (Terwiesch, b15).

**Cross-model.** IDEAFix: cross-model pairwise distance only 0.206-0.341. Jiang: 0.71-0.82. Mixing vendors helps a pool but does not make samples independent (G4).

**What changed it, by how much (diversity = 1 - pairwise cosine, GPT-4o unless noted; humans 0.773).**

| Change | Result |
|---|---|
| zero-shot (base) | 0.679 |
| independent one-idea sessions | 0.452 (-0.227) |
| refine each idea twice to be bolder | 0.575 (-0.104) |
| random sonnets | 0.686 |
| chain of thought | 0.698 |
| random constraints | 0.735 |
| human-picked problem agent | 0.739 |
| random personas | 0.757 (+0.078) |

Separate task (fitness products, GPT-4o, 990 ideas per arm): default 88 unique combinations; ordinary persona 210; creative-entrepreneur persona 164; human 206; theme-first CoT 55.49 per group of 10 vs 39.15 (default); persona + CoT 65.42. First ideas are where an LLM loses most: 8.37 vs 14.51 categories per ten first ideas, and between-participant variation of first ideas 0.241 vs human 0.545 and ordinary persona 0.635.

**Scaffolds on agents.** MUTATE: structured open candidate generation followed by constraint selection (ReDNA) raised path discovery by 19.7 points (GPT-5.4), 19.6 (Claude Sonnet 4.6), 28.6 (Llama 4 Maverick), 25.0 (Qwen3-235B). Self-Refine on Claude lowered it. IDEAFix: short divergence words beat long method prompts. Recoding-decoding: 244 clusters from 250 ideas vs 35. Diamond of Thought (wearable design, 6 raters): staged scaffold with a case database beat IO and CoT on rationality (p=.025) and completeness (p=.039) but humans stayed ahead on innovation (p=.017); judges guessed "human" for DoT 62.5% vs humans 70.8%.

**Search strategies (Heuresis, Gemini-3.1-Pro, 3 ML tasks).** Diversity-forcing archives top diversity, but diversity did not predict quality, no idea was rated Original and the running best flattens after 50-100 valid solutions. 40 confirmed reward-hacking fabrications in 1,628 scored runs. No best-of-N control.

**LLM as inventor.** Egea (GPT-4, hackathon): 2nd of 6; strong on concept generation; dropped a promising concept after one failed iteration; fixated on details in prompts. The authors' recommendations (ask for alternatives, ask to avoid fixation) are untested.

**LLMs as judges.** Zero-shot: at or below chance on research-idea quality (43.3-53.3% vs human 56.1%); one sentence of prompt moves accuracy by 52.6 points; scorers disagree (2.28 to 3.83 mean novelty). With worked expert-scored examples plus reasoning, a VLM judge hit expert level on uniqueness and drawing quality (sketches). Personalised judges conditioned on one evaluator's past scores aligned better than pooled judges (5 of 6 dimensions). Nobody has tested ensembles or pairwise-with-reference novelty judging.

**Fixation in LLMs.** Within a session GPT-4o fixates as much as humans over 10 ideas. This is not an example-exposure test. No study we opened runs the Jansson-Smith paradigm on an LLM.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids refer to the jsonl files. Note on operators: the claims file used "O1" for a diverge step. In SCHEMA.md O1 is Specialise. Divergence belongs to S3 open mode, not to an impasse operator, so it is placed at S3 below.

### Add now (established)

1. **Measure sets, not answers.** Log, per open-mode run: raw count, non-duplicate count, cluster count, pool diversity (1 - mean pairwise cosine), and the four Shah dimensions separately. Part: section 6 logging, S3, S7. [E] K05, K07, K13, K16, K20; b13, b14, c11, c20.
2. **Stop sampling on the non-duplicate rate, not on a fixed count.** Si's wall (about 5% non-duplicates at 4000) and Meincke's exhaustion curves (3700 vs 4700) both make a raw count a poor quantity measure. Part: S3 open-mode stop rule; links to G12. [E] K05; the slope of returns is [S] K25; b08, c11, c15, d08.
3. **Code decides what is covered; the model gets a list of covered directions, not the full earlier text.** Blind independent one-idea sessions collapse (0.452). A session that sees its own earlier ideas does much better (0.679). Part: S3 (history of directions tried, untried assigned by code). [E] direction, K22; d07, d12, b14. Caution: the exact form we use (fresh context plus a code-written covered list) is untested. See U2 in UNKNOWNS.md.
4. **Assign the first move before generation, from varied but ordinary personas or constraints.** First ideas lose the most diversity; random personas 0.757, random constraints 0.735, ordinary personas matched human combinations. Do not use eccentric personas (non-monotonic). Part: S3 open mode (direction assignment). [E] for LLM-only pools K08; [C] for humans K19; the first-move detail is [S] K21; b14, d12, a09.
5. **Do not refine the whole pool. Cap critique and refine passes in open mode at about 3, and log cluster count before and after each pass.** Pool-wide refinement lowered diversity (-0.104; duplicate rate 0.022 to 0.238). Part: S5 in open mode, S7. [E] K09, K17; b14, d05, a16, c27, b25. This supports the existing 2-round cap in S5.
6. **Never let the generating model, or any zero-shot LLM judge, pick the winner on novelty. Rarity and distinctness come from code; the winner comes from running (S4) or a human.** Reinforces G8. [E] K15; b07, c12, c24, c07, c19, d16. Five independent sources now back G8.
7. **Calibrate every embedding score with a matched null (same prompt, truly different ideas), and fix one embedding model, one threshold and one attribute list before the run.** Part: measurement rules for the bench, G7. [E] K06 (size contested), K16, K26; a15, d09, d10, b03, b04.
8. **Report novelty and quality separately.** A candidate that fails S4 is not counted as a novel success. Part: S4, S7. [E] that the two axes diverge (c18, b12, c01); [S] on the size (K20); the pass gate itself is [D] with Padmakumar (c25) as a single source.
9. **Use the same model's plain-prompt answer as the novelty reference inside a run.** Part: S3 open mode ("typical answer first, then elsewhere"). [S] a28, b05, a13.

### Test first (single-source, contested, or untested for our setup)

- **Forced-divergence operator vs best-of-N at equal tokens.** [S] K10; a16, a13, d04, d06, d12. Part: S3. The sources are single-group and none equalises tokens.
- **Tagged-mechanism dedup instead of a cosine cut.** [S] K27; d13, d14. Part: S3/S7 dedup.
- **A posteriori rarity score (T-C)/T*10 on tags as a tie-breaker in S7.** [E] for the formula (K01), [S] for its use on LLM pools. Part: S7 (distinctness). Risk: inflated when the pool is full of copies of outside ideas (b04).
- **Genealogy-tree variety vs embedding variety on one idea set.** No data exist (gap 2). Part: measurement choice.
- **Theme-first chain of thought before writing ideas.** [S] d12 (GPT-4o, about +42% combinations), c14 (working paper). Part: S3 open mode.
- **Diversity-aware subset refinement (maximal marginal relevance, 4 candidates).** [S] K24, d05. Part: S5/S7 budget rule.
- **Fixation probe: give the agent an example solution and measure features copied; compare a lesson shown before vs after the first attempt.** [C] K14, K21; b20, d11. Part: memory (lessons shown after first attempt, section 5), S1 input hygiene.
- **Seeding the generator with distant stored ideas (an idea bank) vs none.** [C]: Ashkinaze delta .31 raised human pool diversity; Wadinambiarachchi saw human fixation rise with AI images; d11 saw no help from a human seed. Part: S3 grounding, memory.
- **Does ideation spread or novelty predict test result on our items?** [S] K04, K23; b09, b10, d04. Part: G8, S7.
- **Persistence rule for a lead concept (test a concept more than one iteration before dropping it).** [S] n=1, Egea (a06, b22). Part: S5/S6.
- **Calibrated LLM judge (worked examples with expert scores plus reasoning) as a filter, never the final selector.** [S] d15, d16. Part: G8, G5.

## 8. Concrete tests on our bench

All arms get the same total token budget, counted including setup (G7). Use at least 3 independent seeds. Pre-register the embedding model, threshold, attribute list and cluster rule. Compute pool diversity, cluster count and non-duplicate count for every arm. Report a matched null score beside them.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Open-ended brief items (NoveltyBench-style prompts; design briefs with a stated goal) | (a) N plain independent samples; (b) schema S3 open mode with code-assigned untried directions; (c) one long list in one context | cluster count and non-duplicate count at the equal budget | (b) beats (a) on clusters (literature: 0.679 vs 0.452, MUTATE +20-29 points). Unknown whether the gain survives equal tokens. |
| T2 | Same items | blind fresh contexts vs fresh context plus code-written covered-direction list vs full prior text shown | pool diversity; cluster count | covered list at least matches full-text context and beats blind (from d07). |
| T3 | Same items with tagged outputs | cosine cut 0.8 vs tagged-mechanism equality | agreement with two human raters on 100 sampled pairs "same idea" | tags well above cosine's 0.51-0.56; accept tags if accuracy >= 0.75. |
| T4 | One idea set (200 ideas) | two raters build genealogy trees (10/6/3/1); compare M3 to cluster count and mean pairwise cosine | rank correlation across 20 sub-sets | unknown. A correlation >= 0.7 would let us use the cheap measure. |
| T5 | Open items with a check (puzzles with several valid solution families; ARC-style items with multiple valid programs) | (a) plain model, N samples then run; (b) divergence operator then run | distinct valid solution families found; pass rate of the best | tests the Heuresis result (spread without executed gain). Expect more families, equal pass rate; a pass-rate gain would be new evidence. |
| T6 | Open items | refine-all vs no refine vs refine 4 chosen by MMR | strong non-duplicate yield (rubric by two humans); duplicate rate; tokens | MMR-4 >= refine-all at lower duplicate rate (d05: 23.70 vs 21.80; 0.172 vs 0.238). |
| T7 | Open items | direct writing vs theme-first (10 short themes, then write) | unique category combinations per 10 ideas; cluster count | +30-40% combinations (d12). |
| T8 | Open items, fixation probe | brief + example solution first vs not; lessons shown before vs after the first attempt | share of example features copied; cluster count of outputs | copying rises with the example; "after first attempt" lowers it. Needs a feature list per item. |
| T9 | Items with a test (code tasks, ARC-like) | spread-first selection vs quality-first selection vs random pick, over 50 candidates | executed pass rate; rarity of the passing solution | Heuresis predicts no gain from spread. Pass if quality-first >= spread-first. |
| T10 | Open items with human ratings | LLM judge zero-shot vs LLM judge with 5 worked expert examples vs human pairs | agreement with a 3-rater human consensus on top half | zero-shot near chance; worked examples better (d15). Use only as a filter if agreement >= human-human. |
| T11 | Design-style items with a lead concept that fails once | drop on first failure vs persistence budget of 2 iterations | share of items where the lead concept is eventually built or passes | single-source (Egea). Test cost is low. |
| T12 | Open items | sweep N = 10, 25, 50, 100, 250 on fixed arms | cluster count and non-dup rate vs N | returns slow, log-like (d08); find the break-even per item class for G12. |

For T1 and T2 add a style-neutral rewrite check (d09) on a 10% subset, so the gain is not a wording artefact.

## 9. What does not transfer, and why

- **Human collective homogenization findings (K11-K13).** They describe people who use an AI. Our agent is one model. They matter only if humans use the agent. For the agent the relevant version is: does seeing its own earlier ideas narrow later ones.
- **Human sketch fixation (Wadinambiarachchi, N=60).** Humans copied features of a seen image. It says nothing yet about an LLM's reaction to an exemplar (d22).
- **Shah's genealogy tree as a human-rated method.** Tree placement needs a rater. The paper gives no inter-rater number. For an agent the tree must be rebuilt from tags, which is a different measurement.
- **Peer ratings and crowd ratings of novelty.** In Shah 2003 the raters were competing students. In Terwiesch they were Prolific raters. They are not evidence for what an expert panel or a test would say.
- **Research-idea results (Si).** NLP prompting ideas, judged on paper, executed by experts. Engineering artefacts need a physical or simulated test. The execution gap may differ there.
- **Persona simulations of people (Dong and Yakura, Doudkin).** They try to simulate varied humans. We use personas only to assign different starting directions to one agent.
- **Multi-agent critics and discussion (Chen et al.; c27).** The gains are small (0.80 vs 0.77) and G9 says no debate. We take the stopping shape (about 3), not the multi-agent design.
- **Hackathon and wearable-design results (Egea, Diamond of Thought).** n=1 LLM team; 6 raters. Direction only.
- **Embedding diversity as quality.** Diversity says nothing about merit. Heuresis: diversity did not predict executed quality.
- **Brainstorming-session mechanics** (blocking, evaluation apprehension, group size). Not covered by our evidence and mostly about people.

## 10. Open questions

1. Exact Shah, Kulkarni and Vargas-Hernandez 2000 method-comparison numbers.
2. Does an embedding or cluster score agree with genealogy-tree variety and with expert ratings on LLM ideas? Nobody has published the check.
3. Does a forced-divergence operator beat best-of-N at equal tokens on 2025-2026 models? Only single-group tests exist, none at equal tokens.
4. Does ideation variety predict tested prototype performance in engineering design? Only research-idea evidence (N=43; 3,222 runs).
5. Human baselines for fixation and for the quantity-quality link (Sio 2015, Nelson 2009, Girotra 2010, Linsey 2011) are unread.
6. Do LLMs fixate on a provided design exemplar (Jansson-Smith paradigm run on a model)?
7. Which embedding model and threshold best match human "same idea" judgements, and how do conclusions change across them? Schaeffer shows high sensitivity.
8. Can LLM novelty judges be made reliable by ensembles or pairwise-with-reference prompts? Not tested.
9. Does self-refinement still lower diversity on frontier 2026 models at equal tokens? Evidence is GPT-4o, one Claude data point, and pool-level refinement.
10. Where is the break-even N for an agent at fixed tokens (saturation curve)?
11. How should set scores be aggregated from per-idea Shah scores? Sorensen et al. (2026) argue common aggregations are flawed (c29, not opened).
12. Why do homogenization results conflict? Task, embedding model, comparison arm and whether people share one AI output are all candidate moderators. No design separates them.

## 11. Sources

[V] opened and read this session; [M] snippet, metadata or second-hand only.

**Metrics and design research**
1. [V] Shah, Smith, Vargas-Hernandez (2003) Metrics for measuring ideation effectiveness. Design Studies 24(2):111-134. https://ecologylab.github.io/research/publications/ShahVargas-HernandezSmith2002.pdf (DOI https://doi.org/10.1016/S0142-694X(02)00034-0)
2. [M] Shah, Kulkarni, Vargas-Hernandez (2000) Evaluation of idea generation methods for conceptual design. Reference line only (seen in arXiv 2409.07578).
3. [V] Fiorineschi and Rotini (2023) Uses of the novelty metrics proposed by Shah et al. Design Science 9:e11. https://doi.org/10.1017/dsj.2023.9
4. [M] Fiorineschi et al. (2019-2021) variants of Shah's a posteriori novelty metric (three papers). https://doi.org/10.1017/DSI.2019.238
5. [M] Nelson, Wilson, Rosen, Yen (2009) Refined metrics for measuring ideation effectiveness. https://doi.org/10.1016/j.destud.2009.07.002
6. [M] Sio, Kotovsky, Cagan (2015) Fixation or inspiration? A meta-analytic review. https://doi.org/10.1016/j.destud.2015.04.004
7. [M] Linsey 2011; Sarkar and Chakrabarti 2011; Verhaegen 2013; Oman 2013 (names in reference lists only, via https://arxiv.org/abs/2409.07578)
8. [M] Sorensen et al. (2026) Axiom-based aggregation functions for ideation metrics. https://www.design.byu.edu/axiom-based-aggregation-functions-for-ideation-metrics
9. [M] Semantic Scholar citation graph for Shah 2003 (1,159 citing papers). https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/S0142-694X(02)00034-0/citations

**LLM and AI ideation studies**
10. [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
11. [V] Si, Hashimoto, Yang (2025) The ideation-execution gap. https://arxiv.org/abs/2506.20803
12. [V] Terwiesch, Meincke, Girotra, Mollick, Nave, Ulrich (2026) AI and its impact on creativity and diversity. https://arxiv.org/abs/2607.27553
13. [V] Meincke, Mollick, Terwiesch (2024) Prompting diverse ideas: increasing AI idea variance. https://arxiv.org/abs/2402.01727
14. [V] Doshi and Hauser (2024) Generative AI enhances creativity but reduces the diversity of novel content. https://arxiv.org/abs/2312.00506 (published: https://doi.org/10.1126/sciadv.adn5290)
15. [V] Anderson, Shah, Kreminski (2024) Homogenization effects of LLMs on human creative ideation. https://arxiv.org/abs/2402.01536
16. [V] Wan and Kalman (2025) Diverse AI personas can mitigate the homogenization effect. https://arxiv.org/abs/2504.13868
17. [V] Ashkinaze et al. (2025) How AI ideas affect the creativity, diversity, and evolution of human ideas. https://arxiv.org/abs/2401.13481
18. [V] Dong and Yakura (2026) Human diversity fuels collective creativity that LLMs cannot simulate or sustain. https://arxiv.org/abs/2607.26899
19. [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
20. [V] Schaeffer et al. (2026) How strong is the evidence for the Artificial Hivemind? https://arxiv.org/abs/2609.33936
21. [V] Carichon et al. (2026) IDEAFix. https://arxiv.org/abs/2606.00875
22. [V] Park et al. (2026) Beyond One Path: MUTATE. https://arxiv.org/abs/2605.28465
23. [V] Heuresis (2026) Search strategies for autonomous AI research agents. https://arxiv.org/abs/2606.25198
24. [V] Budgeted Subset Refinement (2026). https://arxiv.org/abs/2607.14118
25. [V] Recoding-Decoding for sustained creativity and diversity in LLMs (2026). https://arxiv.org/abs/2603.19519
26. [V] Examining and Addressing Barriers to Diversity in LLM-Generated Ideas (2026). https://arxiv.org/abs/2602.20408
27. [V] StructSim: measuring idea similarity at scale through structural representation (2026). https://arxiv.org/abs/2609.34046
28. [V] Sankar and Sen (2024-2025) A novel mathematical framework for objective characterization of ideas. https://arxiv.org/abs/2409.07578
29. [V] Sankar and Sen (2024) A novel idea generation tool using a structured conversational AI system. https://arxiv.org/abs/2409.05747
30. [V] Ma, Grandi, Ahmed et al. (2023) Conceptual design generation using large language models. https://arxiv.org/abs/2306.01779
31. [V] Egea et al. (2024/2025) ChatGPT as an inventor. https://arxiv.org/abs/2404.18479 (dataset https://doi.org/10.5281/zenodo.10495102)
32. [V] Wadinambiarachchi et al. (2024) The effects of generative AI on design fixation and divergent thinking. https://arxiv.org/abs/2403.11164
33. [V] Miao et al. (2024) Diamond of Thought. https://arxiv.org/abs/2410.06972
34. [V] Hou et al. (2026) CreativityPrism. https://arxiv.org/abs/2510.20091
35. [V] Wenger and Kenett (2025) We're different, we're the same. https://arxiv.org/abs/2501.19361
36. [V] Sternlicht et al. (2026) Old ideas, novel problems: instability of LLM-based novelty evaluation. https://arxiv.org/abs/2610.02022
37. [V] Padmakumar et al. (2026) Measuring LLM novelty as the frontier of original and high-quality output. https://arxiv.org/abs/2504.09389
38. [V] Doudkin et al. (2025) The Spark Effect. https://arxiv.org/abs/2510.15568
39. [V] Exploring design of multi-agent LLM dialogues for research ideation (2025). https://arxiv.org/abs/2507.08350
40. [V] Chen et al. (2025) Beyond brainstorming: what drives high-quality scientific ideas? https://arxiv.org/abs/2508.04575
41. [V] Edwards, Tehranchi, Miller, Ahmed (2025) AI judges in design. https://arxiv.org/abs/2504.00938
42. [V] Hirota et al. (2026) Aggregate vs personalized judges in business idea evaluation. https://arxiv.org/abs/2604.22517
43. [V, weak] Kokate, Kompella, Onkar (2025) ALIA, leveraging LLMs for design ideation (abstract and introduction only). https://arxiv.org/abs/2512.00010

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 11 established claims: 10 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E07.09-K09** (reworded: the sources support less). Terwiesch 0.575 vs GPT-4o 0.679, BSR duplicate rate 0.022 to 0.238, and Dong and Yakura refinement b=0.007 (ns) all check out, but the MUTATE Self-Refine datapoint is about interactive path discovery for Claude Sonnet 4.6 (25/56 vs 30/56), not pool diversity, and Self-Refine matched or beat base for the other three models (GPT-5.4 29 vs 27, Llama 13 vs 13), so it is not a clean 'one more data point'. Corrected claim: Iterative self-refinement of an LLM-made idea pool lowers diversity: in Terwiesch et al. the refine-twice (Bold Ideas) arm ran on GPT-4o and scored 0.575 vs 0.679 for GPT-4o zero-shot (a 0.104 drop); uniform refinement of a pool raised the near-duplicate rate from 0.022 to 0.238 (Budgeted Subset Refinement, preprint by one independent author); refining a person's own seed ideas did not compress diversity (Dong and Yakura). In the MUTATE agent benchmark Self-Refine lowered Claude Sonnet 4.6's path discovery (25/56 vs 30/56) but not the other models'. Frontier-2026 models at equal tokens are untested.
