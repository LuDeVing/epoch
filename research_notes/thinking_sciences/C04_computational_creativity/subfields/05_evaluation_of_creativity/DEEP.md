# Evaluation of creativity: deep document

*Subfield 05 of C04 (computational creativity). Written from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b05, d01 ...) point to lines in those files; claim ids (K01 ...) are C04.05-K01 ... in claims.jsonl. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. "Human-only" or "older models only" means the result has not been shown for current LLM agents.*

*Honest scope note. Most LLM-judge numbers come from 2026 preprints that are not peer reviewed, with small test sets (32, 49, 50, 98 items). The human-side evidence (CAT, rater reliability) is older and solid. Si 2024 appears in three evidence files (a, b, c) but is ONE source. Where two ids come from the same paper, this document says so.*

---

## 1. What it is

Evaluating creativity means deciding, for an idea or artefact, how creative it is. Almost every definition has two parts: it is **new** and it is **valuable or useful**. Some add **surprise** (Boden). Plucker et al. (2004), as read through Jordanous's thesis (a14): of 90 surveyed articles, 34 gave a definition. Uniqueness appeared in 24, usefulness in 17, and all 17 that named usefulness also named novelty.

Four things get measured, and they are not the same:

1. **Novelty**: different from a reference class. Which reference class (the model's own earlier ideas, the literature, what people usually say) is the hard part. Novelty is time-dependent (b12): a project loses novelty as similar ones appear.
2. **Value or usefulness**: does it work, is it sound, is it wanted.
3. **Surprise**: the judge did not expect it. In the one LLM test that measured it, surprise was the weakest-judged axis (b14: Kendall tau -0.01, p=.867).
4. **Diversity of a set**: how many functionally different ideas a generator makes. This is a property of a set, not of one idea.

Four ways to measure:

- **Human raters** (Consensual Assessment Technique, CAT; checklists such as TTCW).
- **Automatic scores** (embedding distance, n-gram rarity, trained scorers, distinct-answer counts).
- **LLM-as-judge** (zero-shot, rubric, retrieval-grounded, pairwise, ranking in batches).
- **Outcomes** (run the idea; wait for later papers; check pass/fail).

Why it matters for our agent. In open mode (SCHEMA.md S3) the agent makes many ideas and something must pick among them. G8 says the generating model must not be the final selector, and novelty is judged by running. This document tests that rule against the evaluation literature and finds it holds. It also finds what can replace the judge: code-run diversity counts, retrieval of prior art, pooled binary checks, and execution.

The central empirical result of the subfield: **rated creativity is a weak, noisy, halo-driven signal even among experts, a worse signal from LLM judges, and it can run opposite to outcomes.** Execution and external criteria are the only validated alternatives, and only one study (Ideation-Execution Gap) measures outcomes directly.

---

## 2. History and theories in depth

### 2.1 Definitions and the three-part view

- **Novelty plus value.** The common core (Mayer 1999 table of seven authors including Boden, as relayed in a14). Everything below refines how to measure the two parts.
- **Boden (background, from memory [M], not opened here).** Combinational, exploratory and transformational creativity; "surprising" is part of her criterion. Jordanous only touches surprise (a14). Bhushan et al. (2026) use an anchored 0-4 rubric of Boden-like levels to judge agent novelty (b16), which is the one operational use of her types in this evidence set.
- **Colton's creative tripod** (a13, a14): skill, imagination, appreciation, as perceived by an audience. It adds the point that perception of the process matters, not only the output.

### 2.2 Ritchie criteria (2007) [V a10, a11]

A formal, output-based framework. It looks at a set of results R and the inspiring set I the program drew on. It uses two ratings per item: **typicality** (does it belong to the genre) and **quality**. It makes no claim about inner process.

- 14 original criteria (from Ritchie 2001). C1-2: average and share of typical items. C3-4: average and share of high-quality items. C5-8: quality among typical and untypical items. C9-10: overlap of R with I. C11-14: typicality and quality of the novel items (R minus I). Revised 8a, 10a and new 15-18.
- Parameters: alpha, beta (typicality bounds), gamma (quality threshold), theta (comparison level). Applications set them to 0.5 "with no reason".
- Applications reinterpreted the terms: typicality was taken as the opposite of originality; value as fit to the program's own goal. In a paraphrase study (192 items, 3-point scales) and a melody study (21 melodies) all thresholds were 0.5. In the WASP study no item from the inspiring set appeared in the results, so criteria 9-14 were vacuous.
- Ritchie warned that users treated the 14 criteria as an equal-weight checklist, which he did not intend.
- Limit: overlap with I is set membership, not graded similarity. Needs human typicality and value ratings.

### 2.3 SPECS (Jordanous 2013) [V a12, a13]

A three-step procedure: (1) define creativity for the domain, (2) state the standards you will test, (3) run the tests and report. Step 1 is filled from 14 empirically derived components (Active Involvement and Persistence, Generation of Results, Dealing with Uncertainty, Domain Competence, General Intellect, Independence and Freedom, Originality, Social Interaction and Communication, Spontaneity and Subconscious Processing, Variety Divergence and Experimentation, Intention and Emotional Involvement, and others). They came from corpus analysis of creativity discourse plus a survey of people.

Meta-evaluation (Case Study 1, musical improvisation): evaluators were the system builders (Biles for all methods, Lewis for SPECS and tripod, Keller comments), 5-point scales. SPECS and the tripod were rated extremely useful; SPECS and Ritchie "quite correct"; an unguided opinion survey was "a bit mushy" and lowest on correctness. Biles called SPECS "not very user-friendly".

What this does and does not show. It shows that a stated rubric beats an unguided "is it creative?" question *in the eyes of the builders*. It does **not** link any framework to downstream success. Weights are chosen by the evaluator, so scores are not comparable across projects. Gap search found no study comparing multi-criterion scores with pass/fail on a checkable task (K18, gap 9). Verdict for us: vocabulary only.

### 2.4 The Consensual Assessment Technique (Amabile 1982 onward)

The human gold standard. Experts judge products independently, with their own sense of "creative", no rubric, no definitions; scores are averaged and checked by inter-rater reliability. Founding paper not opened (a29, [M]); its key claim (alphas typically above .70, often .90s) is quoted in Baer 2004 (a19, opened).

- **Baer, Kaufman, Gentile (2004)** [V a19]: CAT extended to products written to different prompts. 13 expert judges. Coefficient alpha .940 stories, .957 personal narratives, .868 poems. Mean pairwise inter-rater r: poems .66 (range .61-.72), stories .76 (.73-.81), narratives .79 (.78-.80). Alpha is inflated by 13 raters; pairwise r is the conservative figure.
- **Kaufman, Baer, Cole, Sexton (2008)** [V a18]: 10 expert poets vs nonexperts on 205 student poems. Raw alpha: experts .832, nonexperts .935. Standardised to 10 raters (Spearman-Brown): experts .804, nonexperts .575. Correlation of group means r = .21 (4.41% shared variance). Means: novices 4.47 (SD .87), experts 3.09 (SD .90). Novice count is unresolved: the abstract says 106, the table shows 204 novice raters after removing 4 raters and 2 writers (critique).
- **Kaufman, Baer, Cole (2009)** [M a28]: on short fiction, novice-expert mean correlation .71 (search summary only). So the novice failure depends on domain.
- **Kaufman, Christopher, Kaufman (2008)** [V a20]: how a *set* of five poems is rated overall. 10 experts, 2 independent groups, N=40 sets per group. The mean of the five poems explained 74% (group 1) and 92% (group 2) of overall variance. Set rating followed average, best, worst and last poem, not variability. Rating dimensions correlated at least .77 and .89.
- **Clements et al. (2018)** [V a21]: online CAT variant for dance, 850 evaluators, 23 videos. Raters' own creative or choreographic experience shifted ratings.

Lesson: reliability comes from **many competent raters**, not from agreement between any two. Competence matters more than count (a novice pool of 106 looked reliable by raw alpha .935 and was not valid). For a model judge, "many votes from a weak, ungrounded judge" is the novice pool.

### 2.5 Automatic measures, in order of appearance

1. **Semantic distance** (SemDis, Beaty and Johnson 2021, a15). Distance between prompt and response vectors. Latent-level r with human originality .91 (Study 1, N=171, AUT) and .75 (Study 2); word association r .95 (Study 4). Latent correlations remove measurement error and inflate. At item level in S-DAT (c30): r .17, .24, .13 (up to 8,498 responses); original DAT .32, .32, .13. Human AUT originality inter-rater r = .66.
2. **Supervised scorers** (Buczak et al. 2022, a16: RF/XGBoost on embeddings, cross-sample r .57-.64, up to .76-.78 on one validation set; Organisciak et al. 2023, a17, [M] snippet only: up to r .81 with human raters vs .12-.26 for earlier systems; Grouchnikov et al. 2026, b26: poly-encoder r .74 on 18,000 responses, LLaMA-2-7b fine-tune .74, GPT-3/T5 up to .81 on 27,217 AUT responses, GPT-4 zero-shot .2-.67; human rater w=.85, test-retest r=.67).
3. **Count of functionally distinct answers** (NoveltyBench, a25/c17): novelty as diversity of a sample set, not a rating.
4. **Reference-corpus rarity** (c24): harmonic mean of originality (share of 4-6-grams absent from the training corpus) and quality.
5. **LLM-as-judge** (2023 onward): the bulk of the evidence below.

### 2.6 Backward and forward chain

- Ritchie 2001/2007 -> SPECS 2013 (builders' re-interpretation, no outcome link).
- Amabile 1982 -> Baer 2004 -> Kaufman 2008/2009 (novice vs expert) -> TTCW 2024 (CAT with binary tests for LLM stories) -> LLM judges tested against TTCW (kappa near 0).
- Lamb et al. 2015 (crowd inverts poem quality; [M], seen only via Sawicki) -> Sawicki 2025 (LLM batch ranking rho .87).
- Si 2024 (ideas, rated before execution) -> Ideation-Execution Gap 2025 (same ideas executed) -> HindSight 2026 (judge novelty vs later papers) -> Old Ideas 2026 (judge prompt fragility).
- Panickssery 2024 (self-recognition drives self-preference) -> Chae 2026 and Pombal 2026 (when it vanishes and when it stays).

---

## 3. Core findings with exact numbers

Status uses claim status: established [E], single-source [S], contested [C]. "Human-only" or "older models" is added where relevant.

### 3.1 Human raters

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Experts agree only weakly on idea quality | Split-half 56.1% on top/bottom 25% (chance 50%); NeurIPS 2021 66.0%; ICLR 2024 71.9% | Si 2024 (a03, b02) | [E] K01 |
| Novelty is the least reliable axis, even among humans | Cohen kappa novelty 0.18 (2 buckets), 0.04 (5 levels); usefulness 0.53, 0.12; n=30, 2 raters | Falk 2025 (a09, b09) | [E] K01 (small n) |
| Trained raters on creative-writing rubric | Weighted kappa 0.48 (CI 0.43-0.54), 10 raters, 12 LLMs, 1 prompt | Unlikely Duel (c26) | [E] K01 |
| Binary expert tests: moderate singly, strong pooled | Fleiss kappa 0.41 per test (range 0.27-0.66); Pearson 0.69 on pass count; 10 experts, 48 stories, 2,016 judgments | TTCW (a22, b23) | [E] K02 |
| CAT is reliable with enough experts | Alpha .940 stories, .957 narratives, .868 poems with 13 raters; pairwise r .61-.81 | Baer 2004 (a19) | [E] K02 |
| Experts reliable, novices not | Standardised alpha .804 vs .575; group means r .21; novice mean 4.47 vs expert 3.09 | Kaufman 2008 (a18) | [E] K03 |
| Novice-expert agreement depends on domain | r .71 on short fiction | Kaufman 2009 (a28, snippet) | [C] weak evidence |
| Lay raters can invert truth | Crowd Quality SRC -0.33, Skill -0.35, Wellbeing/Effort -0.45; Novelty +0.38 (only positive) vs venue ground truth | Lamb 2015 via Sawicki (a27, b22) | [S] second-hand |
| Rater background shifts ratings | 850 evaluators, 23 videos; own experience predicted rating | Clements 2018 (a21) | [S] (domain far from text) |
| Set rating follows mean item quality | Mean explains 74% / 92% of overall; variability ignored | Kaufman 2008b (a20) | [S], poetry |
| Reviewer "overall" is a novelty and excitement halo | r overall-novelty .725, excitement .854, effectiveness .642, feasibility .097 (<.1); novelty vs feasibility r -.073 | Si 2024 (a02, b04) | [E] K13 (2 sources with Bhushan) |

### 3.2 Pre-execution rating vs outcome

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM ideas rated more novel before execution | Idea level (N=49 per cond.): 4.86 human, 5.62 AI (p=.03), 5.78 AI+rerank (p<.01). Review level (109 per cond.): 4.84, 5.64, 5.81. 79 reviewers, 298 reviews. Overall: 4.68, 4.85 (n.s.), 5.34 (p=.04). Always state the level | Si 2024 (a01, b01, c01; critique item 1) | [S] K04 |
| Execution erased the lead | Novelty human 4.912 -> 4.903, AI 5.778 -> 4.729; excitement 4.404 -> 4.482 vs 5.653 -> 3.896; effectiveness 4.833 -> 4.782 vs 6.003 -> 4.125; overall 4.596 -> 3.968 vs 5.382 -> 3.406. 43 experts, 181 execution reviews | Ideation-Execution Gap (a05, c06) | [S] K04 |
| AI ideas lost far more | Changes: human novelty -0.010, excitement +0.078, effectiveness -0.052, overall -0.628; AI -1.049, -1.760, -1.879, overall -1.976; FDR p=.025, .001, .003, .004 | same (a06, b05) | [S] K04 |
| Post-flip ranking not significant | Excitement 3.90 AI vs 4.48 human; effectiveness 4.13 vs 4.78; per-idea N=43 (19 human, 24 AI) no significant difference | same (b06, c06) | [S] low power |
| Idea-stage score barely predicts execution score | AI: novelty r -.019, excitement -.321, effectiveness .172, overall -.092; human: -.084, .205, .022, .158 (about 20 ideas per group) | same (b07, c07) | [S] |
| Judge novelty ran against later real-world uptake | Spearman judge novelty vs HindSight match -0.291 (p=.003); impact -0.225; feasibility +0.252; 200 ideas; match rate 81% vs 42% for retrieval-augmented vs plain generator while judge overall was 7.44 vs 7.40 (p=.584) | HindSight (d01) | [S] K20; outcome is similarity to later paper, not execution |
| Novelty and value decoupled in agent runs | Spearman of change in impact vs change in creativity: human -0.111 (p<.05), AIDE GPT-5 -0.021, AIDE Qwen3-32B .056, AIRA -0.026 | Bhushan 2026 (b18) | [E] K13 |

### 3.3 LLM judges: accuracy against humans

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Ideas, top/bottom 25% | GPT-4o direct 50.0, pairwise 45.0; Claude-3.5 direct 51.7, pairwise 53.3; AI Scientist reviewer 43.3; human 56.1. Same ranker 71.4% on ICLR accept/reject pairs | Si 2024 (a03, b03, c03) | [E] K05, older models |
| 5-class novelty of ICLR ideas | Macro-F1 at most 17.2 (GPT-5); o3 16.2; GPT-OSS-120B 13.0; Llama-3.1-8B about 12; class 1 F1 = 0.0 for all; MAE 0.93-1.04; 1,381 ideas, test about 277 | RINoBench (c08) | [E] K05 (gold is LLM-derived) |
| Long stories, 14 binary tests | Cohen kappa GPT-3.5 0.016, GPT-4 0.035, Claude v1.3 -0.006; best single test 0.31; GPT-4 above 0.2 on 2 of 14 | TTCW (b25, c15) | [E] K05, 2023 models |
| Judge prompt fragility | Delete one sentence: gpt-5.4 moves 52.6 points; prompts disagree on at least 52.6% of pairs (55.8% in practice); claude-opus-4-6 21 points on Human-Only; a quarter to a third of verdicts flip when ranking two ideation systems; ties up to 35% | Old Ideas (d02) | [E] K21 (with RQ-Bench) |
| Proposals approved though unsound | Standard prompt: 74.0% false-positive on low-soundness (64.8% with expert labels), high-soundness recall 91.8%. Aggressive prompt: false positives 19.9%, high recall 36.2%. ScholarEval still approves 65.7%. 1,099 proposals, 327 expert-labelled | SoundnessBench (d13) | [E] K25 |
| Judge pick equals chance | Self-judge pick matched diversity pick 29% vs 35.3% random; 31 students, 217 answers; ranker and expert rerank overlap 17 of 49 | Creative Beam Search (c27), Si 2024 (c05) | [E] K14 |
| Middle-score compression | Gemma-2-9b gave "3" about 80% novelty, 75% usefulness; Mistral, Llama peaked at 4 (about 65%); 21,318 descriptions | Falk 2025 (a08); Think-Probe-Respond (c10) | [E] K16 |
| Novelty mirage | Experts preferred author RQ 78% and 56%; LLM judges preferred model RQ 82% (gemini-3.1-pro) and 52% (deepseek-v4-pro); human-LLM agreement as low as 22%; expert-expert 60%; 50 pairs, 2 experts | RQ-Bench (c11) | [E] K06; abstract-level in critique |
| Machine text overrated | LLM novelty 4.90 human vs 5.00 AI (p<.001); human 3.03 vs 3.18 (p=.293); 200 stories; AI texts hit 5.00 with zero variance | Tutone 2026 (b13, d08) | [E] K06 |
| Judge-human rank correlation near zero for surprise and novelty | Kendall tau elaboration .31, creativity .23, novelty .10 (p=.224), surprise -.01, usefulness .08 | Tutone (b14) | [S] (dimension labels read from figure order) |
| Automatic metrics near zero | Creativity Index rho .07; perplexity down to -.23; SBERT diversity negative | Tutone (b15) | [S] |

### 3.4 Judges that work better (with boundaries)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Batch ranking beats crowd on poems | Claude-3-Opus Spearman .87 (15 poems per prompt, rank-derived score); GPT-4o .62; all 90 at once .57-.68; best non-expert .38; ICC .9-.99 over 10 runs; ground truth = venue | Sawicki 2025 (a23, b21) | [C] K07; possible contamination |
| Rubric plus run history judge | Spearman with 3 trained annotators (alpha .724) GPT-5 .732 [.675,.781], GLM-5 .703, DeepSeek V3.2 .700, Qwen3-235B .685, GPT-OSS-120B .544; nearest neighbour .637; graph -.329; no examples .684 | Bhushan 2026 (b16, b17) | [C] K08; novelty relative to agent's own earlier episodes |
| Retrieval-grounded judge | Spearman .358 (median human) to .411 (mean) on 98 ideas; binary accuracy .602-.633 vs human-human .571; MAD 1.70 vs 1.73 | Shen 2026 (b19, c19) | [C] K08 |
| Literature-grounded checker with expert examples | gpt-4o 32 items: zero-shot .68, with examples .81, F1 .79, kappa .59; accuracy on not-novel ideas: full 89.66%, generic rerank 13.79%, keyword only 5.17% | Literature-grounded (c21) | [C] K08; 32 items, page summary |
| Trained rubric on a task | Experience-graph judge: Hit@1 up 24.4%, Hit@2 up 29.7% over standalone ChatGPT-4o on 147 expert-rated ideas | DeepInstructor (d15) | [C] K08, gold = human rating |
| Retrieval gains are small and can mislead | At most 16 points, only some judges; hurt some; 22 correct-to-wrong flips studied | Old Ideas (d03, d04) | [C] K08 |
| Moderate LLM-human match on ideas | Mean of six LLMs vs three trained raters r=.50; GPT .52, Grok .49, DeepSeek .46, ERNIE .46, Claude .41, Gemini .41; 1,103 ideas; human ICC1=.45, ICC2=.71 | Lyu 2026 (d11) | [C] K23 |
| Two-stage judge | QWK .64 (PCC .69) vs direct/CoT/ToT/GoT about .2-.25; fine-tune on about 140 labels .47; no decoupling .21; no evidence step .24 | CreaEval (d12) | [S] K24; authors' own task |
| Averaging judge runs | o3-mini 5-run mean Spearman .50, .52, .52; Claude 3.7 single run .38, .35, .38; human alpha .68, .64, .59 | Frontier novelty (c24) | [C] K23 |
| Semantic entropy over clustered continuations | Kappa .56 vs human; cosine .49; Distinct-1 .37; Self-BLEU .35; 50 MacGyver problems; convergent judge 84.7% vs ChatEval 76.7%, single GPT-4o 64.7-67.3%, human 80.0-84.7%; 63% fewer tokens | Automated Creativity Eval (c22) | [E] K11 |

### 3.5 Biases and their fixes

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Length and elaboration inflate scores | Own-response originality 3.49 -> 2.06 (-1.43) when core idea only; 4,813 AUT responses; 65.25% of chosen stories longer; word count a strong predictor | Domanti (b27, b28), LitBench (a24), Buczak (a16) | [E] K10 |
| Pairwise comparison can worsen inflation | gpt-5.5 win rate 27.2% standalone vs 49.1% comparative; ties 59.1% -> 36.8% | RQ-Bench (c12) | [C] K07 |
| Naming the missing dimension helps | With narrowness test model RQs lose 71.7% standalone (win 4.3%); 85.4% comparative | RQ-Bench (c13) | [E] K26 (rubric built after failure) |
| Claim attribution repairs unsupported novelty | Repair rate 72.2% vs 39.1% retrieve-and-revise vs 11.7% self-revision; of 175 exposed proposals 137 recognized relevance, 61 attributed correctly; 37 of 71 "distinctions" covered by the same prior | RINI (d05) | [E] K26 |
| Self-preference, blind and style-neutral | Raw S=+0.181 [.13,.23]; after dropping 2 low-discrimination judges S=+0.003 [-.05,.06]; Originality -0.133; 10 LLMs, 9,000 blind runs; labels alone shift scores | Chae 2026 (d06, d07) | [C] K22 |
| No own-output inflation with rubric on run evidence | GPT-5 minus DeepSeek V3.2: +0.300 on Qwen3 episodes vs +0.129 on its own (p=.000038) | Bhushan (b17, d09) | [C] K22 |
| Objective rubric self-preference | Judges more than 50% more likely to wrongly pass own output; single judge overestimates by about 4 points vs ensemble | Pombal 2026 (d10) | [C] K22 |
| Self-recognition drives self-preference | Fine-tuning on 500 self-recognition examples raised self-preference linearly | Panickssery 2024 (d19) | [C] K22 |
| Prompting for novelty buys nonsense | Quality falls as originality rises; novelty U-shaped in temperature | Frontier novelty (c25) | [S] |
| Longer thinking does not help judges | Reasoning high to low costs at most 7 points; CoT lowered LitBench accuracy; judges do not scale with length unless RL-trained | Old Ideas (d03), LitBench (a24), J1 (d17) | [C] K23 |

### 3.6 Diversity and generation

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Sample pool collapses | 4,000 seed ideas per topic; about 5% (about 200) left at cosine .8 (all-MiniLM-L6-v2) | Si 2024 (a04, c04) | [E] K12 |
| Functional-distinct counting matches humans | Classifier 79% accuracy, F1 .811 on 100 held-out pairs, trained on 1,000 pairs; BERTScore AUC .68 vs DeBERTa .81 | NoveltyBench (a25, c17) | [E] K11 |
| Frontier models are low in diversity | distinct_k of 10: command-r 2.68, Llama-3.3-70B 2.49 vs Llama-3.2-1B 6.74, gemma-2-2b 5.66 | NoveltyBench (c17) | [E] K12 |
| Showing earlier outputs restores diversity | In-context regeneration roughly matched human diversity (Claude 3 Opus, GPT-4o, Gemini 2.0 Pro; 100 prompts, 8 generations); paraphrase and "be creative" prompts only marginal | NoveltyBench (c18) | [E] K12 |
| Thinking mode helps usefulness, not variety | Qwen3 32B thinking .517 vs .436; R1-distill 70B .468 vs Llama 3.3 70B .391; semantic entropy flat or lower with size (Vicuna 7B 2.19, Llama 405B 2.08) | Automated Creativity Eval (c23) | [S] |
| Set diversity did not hurt execution success | success@1/2/3: Claude 13/20/27%, proposed no-think 11/22/33%, think 10/19/29%; 132 ideas, 15 instances; LLM distance judge 0.37 vs human-human 0.36 | Wadhwa 2026 (d14) | [S] K27 |
| LLM ideas cluster on a few types | Narrower distribution than human papers (abstract and intro read only) | Chen 2026 (d16) | [S] |
| Benchmark with no subjective judge | 4,141-law pool; 8 prover configs resolve 2.2%; 20x budget adds 0.6%; best reasoning model 14% proof side, none on construction | ALPS (d18) | [S] |

---

## 4. Mechanisms and models

Each item is written so an engineer can build it.

### 4.1 Reliability of a rating: split-half and Spearman-Brown

- **Split-half agreement** (Si 2024). Randomly split the reviewers of each item into two halves, average each half, rank items by each half, and measure how often the top 25% of one half matches the top 25% of the other (balanced accuracy, 20 random splits). Chance is 50%. Human result: 56.1%.
- **Spearman-Brown.** If the average pairwise correlation among raters is r, the reliability of the mean of k raters is `rho_k = k*r / (1 + (k-1)*r)`. Check against data: r = .66, k = 13 gives .96, which matches the alpha of .94-.96 in Baer 2004. The inverse tells you how many raters you need. Always compare groups at equal k (Kaufman 2008: .935 raw for 106 novices becomes .575 at k=10).
- **Reliability is not validity.** Kaufman 2008 shows a reliable but wrong rater pool. Validity needs an external criterion: venue (Sawicki), later papers (HindSight), execution (Ideation-Execution Gap), expert ratings (CAT).

### 4.2 CAT for a judge ensemble

Procedure to copy (a29, a19): each rater scores every item independently, no rubric beyond "how creative", in randomised order; compute the mean per item; report inter-rater reliability; for model judges the "rater" is a (model, prompt, seed) triple that is fixed and logged. Judge identity is part of the instrument (Clements 2018).

### 4.3 TTCW-style pooled binary tests (a22)

Fourteen yes/no tests over four Torrance dimensions (fluency, flexibility, originality, elaboration). Each expert answers each test. The item score is the count of passes. Single tests agree at kappa .41; the count correlates at .69. Implementation: write many narrow binary checks that code or a short model call can answer; sum the passes. Do not use a model to give one holistic number. Warning: the LLM version of the same tests reached kappa near 0 on long stories, so tests must be code-checkable or run on short outputs.

### 4.4 Distinct-answer counting (NoveltyBench) [a25, c17]

1. Sample k outputs per prompt.
2. Train or use a pairwise "functionally equivalent?" classifier (DeBERTa-v3-large, 1,000 labelled pairs, 79% accuracy).
3. Cluster outputs by equivalence; distinct_k = number of clusters.
4. Utility combines quality and novelty with a patience weight p = 0.8 (a user keeps looking through later generations with decaying patience); quality from a reward model.
5. Lever: put earlier answers in context and ask for something different.

Cheap stand-in: embedding dedup at cosine .8 (Si 2024 a04). Embedding cosine alone and n-gram metrics diverge from humans, so treat it as a duplicate detector, not a score.

Semantic entropy (c22): sample continuations, cluster by meaning, compute entropy of the cluster distribution. Kappa .56 with humans, better than cosine .49, Distinct-1 .37, Self-BLEU .35.

### 4.5 Retrieval-grounded novelty

Two published pipelines:

- **Shen 2026 (c19):** an LLM writes search queries, Semantic Scholar returns papers, SPECTER embeddings rerank, an LLM judges novelty against the top 10.
- **Literature-grounded (c21):** break the idea into facets (purpose, mechanism, evaluation, domain), SPECTER2 shortlist of 100, LLM rerank to 10, LLM verdict with expert examples (idea, papers, class, reasoning).

Key engineering facts: retrieval quality is the lever (accuracy on not-novel ideas 89.66% full vs 13.79% generic rerank vs 5.17% keyword only). Expert examples lift gpt-4o from .68 to .81. Failure modes (d04): the judge calls an idea novel because none of five retrieved papers covers it (source-bounded novelty), or dismisses a real combination as "a direct combination of existing ingredients". Fix: never accept "novel" from absence in a small retrieved set; require the explicit claim attribution step (4.7). Retrieval gains were at most 16 points and sometimes negative (d03).

### 4.6 Rubric plus run history judge (Bhushan) [b16, b17, d09]

For agent trajectories on code tasks: anchor a 0-4 rubric (Boden-style levels), give the judge the run history of the agent's own earlier episodes and the code evidence, ask for novelty *relative to that history*. Spearman .732 with trained humans; falls to .684 without anchor examples. No length bias (partial correlation near zero) and no own-output inflation in this setting. Boundary: relative, anchored, code-grounded. Not absolute novelty of prose against the literature.

### 4.7 Claim attribution check (RINI, RQ-Bench) [d05, c13]

For each claim of novelty in an idea: (1) name the nearest prior (retrieved), (2) state what the prior already establishes, (3) state what is left over, (4) code checks that the left-over is non-empty and not covered by the same prior. In RINI this repaired 72.2% of unsupported novelty claims vs 39.1% retrieve-and-revise and 11.7% self-revision. In RQ-Bench a narrowness test moved judges toward experts (model RQs lose 71.7% standalone). Handing the model the prior was not enough (61 of 175 correct attributions). Both fixes were designed after seeing the failure, so test in our domains.

### 4.8 Decoupled evidence-then-score judge (CreaEval) [d12]

Stage 1: extract quoted evidence for each rubric item from the output. Stage 2: score each item from the evidence only. QWK .64 with experts vs about .2-.25 for chain, tree and graph reasoning and .47 for fine-tuning on about 140 labels. Ablations: no decoupling .21; extracting evidence for all six steps at once .01; no memory .49. Length-score correlation fell by 5.81% but did not vanish.

### 4.9 Batch ranking (Sawicki) [a23, b21]

Give the model 15 items per prompt, force a ranking, shuffle, repeat over 10 runs, derive scores from ranks, average. ICC .9-.99. Ranking all 90 at once was worse (.57-.68). Batch size and scoring method were tuned on the same 90 poems, so some overfit is possible.

### 4.10 Time-split outcome test (HindSight) [d01]

Generate ideas from pre-cutoff papers; match each idea to papers published after the cutoff (similarity threshold 0.96, chosen after looking: ratio 1.1x at 0.93 to 3.8x at 0.965); score by match, citations and venue. It separated a retrieval-augmented generator (match rate 81%, mean .297) from a plain one (42%, .119) that the judge could not separate (7.44 vs 7.40, p=.584). The judge's novelty score correlated at -0.291 with the outcome.

### 4.11 Harmonic mean of originality and quality (c24)

`score = 2*O*Q/(O+Q)` where O = share of 4-6-grams absent from a training corpus and Q = LLM judge quality. Rare nonsense and fluent memorised text both score low. Needs an indexed corpus; exact n-grams miss paraphrase. Fixes the "novelty alone" problem by construction.

### 4.12 Ritchie-style pool audit (a10)

Cheap use of the framework: for a pool R of ideas and a prior set I, split R into copies (in I) and novel (R minus I), then report the share of novel ones that pass a value check. This is criteria C11-14 with a computed value in place of a human rating. Thresholds must be chosen on a rated set, not set to 0.5.

### 4.13 Judge prompt stability check (Old Ideas) [d02]

Run each judgment under two or more paraphrased prompts. If verdicts differ, record "cannot tell". Never validate a judge on human-written ideas only: configurations validated on one backbone or one data type did not transfer.

### 4.14 Core-idea extraction (Domanti) [b27, b28]

Have a separate call extract the core idea in one or two sentences with no elaboration, then judge only that. It cut a machine originality advantage in OCSAI, CLAUS and ChatGPT-4o.

---

## 5. What holds up

### 5.1 Replicated or multi-source

- **Single-rater novelty agreement is weak; pooling fixes reliability, not validity.** Si (56.1%), Falk (kappa .04-.18), TTCW (.41 per test), Unlikely Duel (.48), Baer (r .66) and Kaufman agree. Pooling (alpha .80-.96; count r .69) is replicated across three groups. [E]
- **Competence of the rater matters.** Kaufman 2008 (novices fail), Sawicki re-analysis of Lamb (crowd inverts), Clements (background shifts ratings). Contrary evidence: Kaufman 2009 (novice-expert r .71 on fiction, snippet only). So it depends on domain. [E, with boundary]
- **LLM judges are near chance on idea novelty without help.** Five sources: Si 2024, RINoBench, TTCW, Old Ideas and SoundnessBench (Old Ideas and SoundnessBench measure fragility and approval inflation rather than raw accuracy). [E]
- **Judges overrate machine text.** RQ-Bench, Tutone, Domanti (and Si, where *humans* also rated AI ideas more novel before execution). [E]
- **Length and elaboration inflate scores.** Domanti, Buczak, LitBench, Pombal (self-preference grows with length quartile). [E]
- **Sample pools collapse and history prompting restores diversity.** Si (5% left), NoveltyBench (distinct_k 2.5-2.7 for frontier open models; regeneration works). Two independent lines. [E]
- **Novelty and value are decoupled.** Si (r -.073), Bhushan (Spearman near 0 or negative). [E]
- **Judges squeeze scores to the middle.** Falk, Think-Probe-Respond. [E]

### 5.2 Failures, contradictions, boundaries

- **Pairwise vs direct.** Worse in RQ-Bench (win rate 27.2% to 49.1%) and for GPT-4o on ideas (50.0 vs 45.0); better for Claude-3.5 on ideas (53.3 vs 51.7) and up to 11 points better when voting pairwise (d03); batch ranking in 15s gave rho .87 on poems. Task, model and batch size differ. [C]
- **Judges vs non-experts vs experts.** Sawicki: LLMs (.87) beat crowd raters (-.33 on quality). Chakrabarty and Si: near chance versus experts. Different ground truths (publication venue vs expert rating) and small samples. [C]
- **Self-preference.** Tutone's judge wrote none of the AI stories, so that is machine-text preference. Bhushan used a neutral reference and found GPT-5 more conservative on its own runs. Chae found raw self-preference vanishing under blind, style-neutral conditions, but labels alone moved scores. Pombal found more than 50% excess own-output passing on objective rubrics. Reading: self-preference needs recognisable style or a label (Panickssery). Contested. [C]
- **Semantic distance.** Latent r .91 (Beaty) vs item-level r .13-.24 (S-DAT); latent correlations inflate. For an agent scoring single ideas, the item-level figure is the relevant one. [C]
- **Idea-stage rating flips at execution.** One trial (43 ideas, NLP prompting); the rank flip on several metrics was not significant at idea level (b06). Preregistered per-idea hypothesis not confirmed (c06). Treat as one strong but low-power study. [S]
- **Chat helpfulness agreement does not transfer.** GPT-4 over 80% agreement with human consensus on chatbot quality (Zheng 2023, cited, [M b29]). Not creativity. Do not use it as support.

### 5.3 Moderators

- **Task type and length.** Long holistic text is the weakest case (TTCW kappa near 0). Short responses (under 100 words) fare better. Anchored, comparative, code-grounded judging works (Bhushan .73).
- **Domain of the expert group.** Poetry vs fiction vs dance vs research ideas.
- **Reference class and date.** Retrieved set and date cutoff change verdicts (d02-d04).
- **Granularity.** Falk's kappa falls from 0.18 to 0.04 as buckets go from 2 to 5.
- **Style visibility.** Self-preference tracks recognisable style.
- **Judge model and prompt.** Calibration differs by model (Gemma "3" 80%); one sentence moves 52.6 points.

### 5.4 Interventions that worked

| Intervention | Effect | Condition |
|---|---|---|
| Binary tests, summed | r .69 vs kappa .41 | TTCW experts |
| Forced-choice ranking in batches of 15, averaged over runs | rho .87 vs .57-.68 for 90 at once | poems, venue truth |
| Rubric with anchors and run history | rho .732 (.684 without examples) | agent code runs |
| Expert examples in a retrieval-grounded checker | .68 to .81 accuracy | 32 items |
| Retrieval rerank quality | not-novel accuracy 89.66% vs 5.17% | 32-item test |
| Decoupled evidence-then-score | QWK .64 vs about .2-.25 | one task family |
| Core-idea extraction | -1.43 on self-originality | AUT |
| Explicit narrowness / claim-attribution step | 72.2% repair | proposals, RQs |
| Average 5 judge runs | about +0.14 Spearman | o3-mini |
| Majority of 3 | a few points pointwise, up to 11 pairwise | novelty pairs |
| Showing earlier outputs | matches human diversity | NoveltyBench |

### 5.5 Interventions that did not work

| Intervention | Result |
|---|---|
| Few-shot examples on a couple of TTCW tests | no significant gain |
| Chain of thought on judges | no gain on ideas (Si); lowered LitBench accuracy; inconsistent for reasoning models (c10) |
| Extra reasoning effort | at most 7 points, often neutral (d03) |
| Extra retrieval alone | at most 16 points, sometimes harmful (d03, d04) |
| Costly dedicated novelty pipelines | cheapest prompted baseline beat both (d03) |
| Pooling six different judge models | r .50 vs best single .52 (d11), though Pombal found model mixing cuts self-preference |
| Rewrite all ideas into one plan format | instability not removed (d04) |
| Prompting for "creative" or "novel" | marginal or quality loss (c18, c25) |
| Fine-tuning on about 140 labels | QWK .47, below decomposed rubric .64 (d12) |
| Self-judging to pick the most creative candidate | below random (29% vs 35.3%) |

---

## 6. Language models

### 6.1 As generators being evaluated

- Experts rate LLM ideas more novel before execution (Si: 5.64 vs 4.84) but rate them lower after (novelty 5.778 to 4.729; excitement 5.653 to 3.896; effectiveness 6.003 to 4.125; overall 5.382 to 3.406).
- LLM short stories: professional stories passed 84.7% of TTCW tests; GPT-3.5 under 10%, GPT-4 and Claude v1.3 about 30% (3-10 times fewer). Older models.
- AUT: three chatbots beat the average human on semantic distance (0.95 vs 0.91) and rating (2.91 vs 2.47) over 256 humans, but the best humans matched or beat them (c28, [M] news summary). Compare best-of-n, not means.
- Blind raters saw almost no difference between human and AI WritingPrompts stories (novelty 3.03 vs 3.18, p=.293).
- Diversity: frontier open models give 2.5-2.7 distinct answers of 10 (command-r, Llama-3.3-70B); small models 5.7-6.7. Larger models are not more diverse. Instruction tuning raised novelty at every size, mostly through quality (c25).
- Thinking mode raises judged usefulness (Qwen3 32B .517 vs .436) but not variety (c23).
- Pool collapse: about 5% of 4,000 ideas survive dedup at .8.

### 6.2 As judges

- Zero-shot, ideas: 43-53% on top/bottom 25% (human 56.1%). Macro-F1 17.2 on a 5-class task. Kappa about 0 on long stories. These are 2023-2025 models; the best 2026 models were tested in RINoBench (GPT-5, o3) and Old Ideas (gpt-5.4, claude-opus-4-6) and still failed or were unstable. So newer models did not close the gap.
- Systematic biases: middle-score compression, ceiling for machine text (5.00 with zero variance), approval inflation (74% of unsound proposals approved), length preference, label sensitivity (self/other labels shift scores).
- What changed performance, by how much:
  - Task-specific training: poly-encoder r .74, fine-tuned scorers up to r .81, vs zero-shot GPT-4 .2-.67. Not usable in our scaffold (no training).
  - Rubric plus anchors plus run history: rho .73 (agent code runs).
  - Retrieval plus expert examples: .68 to .81 accuracy on 32 items; rho .36-.43 on 98 ideas (human-human ceiling about .41).
  - Evidence-then-score: QWK .64 vs about .2.
  - Batch ranking of 15: rho .87 on poems.
  - Averaging 5 runs: about +.14.
  - Majority of 3: a few points to 11.
  - More thinking: at most 7 points, often neutral; reasoning models only slightly better than non-reasoning ones (RINoBench).
  - Hidden-state probe (TPR): +22.30% over the best prompted competitor on RINoBench, but needs open weights and in-distribution training (c10).
- Where a judge's explanation helps: justification text is close to human reasoning (78-90 alignment, hallucination 0.2-4.2%; c09) and was rated useful by humans (Prometheus kappa .47 and .44; b11), even when the verdict is wrong. Judges sometimes invented project functions (b11).
- Ceiling. Human-human agreement is the practical ceiling: rho about .41, kappa .36-.48, split-half 56%. A judge that reaches it has not shown validity; Si warns that matching human agreement would not prove validity (c03).

### 6.3 Execution and outcome checks

Only the Ideation-Execution Gap (a05) and HindSight (d01) tie idea scores to outcomes. HindSight found the judge's novelty correlated at -0.291 with later matches. No study checked a retrieval-grounded or rubric-plus-history judge against execution (gap 1, still open).

---

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md.

### Add now (established)

| # | Take | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Never let a model judge's idea-novelty verdict pick the winner.** Judges are at or below human agreement and near chance, and verdicts flip with one deleted sentence. G8 already says this; this subfield adds four more independent sources. Keep it. | G8 | [E] | K01, K05, K14, K21; a03, b03, c03, c08, c15, d02, d13, c27, c05 |
| A2 | **Judge scores are converted to within-batch ranks by code**, ties allowed. Judges compress to the middle and scales differ by model. | G5 | [E] | K16; a08, c10 |
| A3 | **Length and elaboration are removed before any score**: extract the core idea, judge that, and report any score residualised on length. | G5 | [E] | K10, K06; b27, b28, a16, a24 |
| A4 | **Keep novelty and value as separate fields; select on the check, never on a sum.** Novelty is uncorrelated with feasibility and with agent progress. | S7 | [E] | K13; a02, b04, b18 |
| A5 | **Log distinct_k of the open-mode draw set by code** (functional-equivalence clusters or embedding dedup at .8) and use it as the stopping and restart signal. Count ideas, not drafts. | S3 | [E] | K11, K12; a25, c17, a04, c04 |
| A6 | **Condition each open-mode draw on the history of earlier ideas** and demand a different one; generic "be creative" prompts barely help. | S3 | [E] | K12; c18, a04, c04 |
| A7 | **Keep a dated archive of produced ideas** and score novelty against it plus retrieved priors. State the date. | memory | [E] | K19; b12, c21, d02-d04 |
| A8 | **Pool binary, code-checkable tests** (pass counts) rather than one holistic score; report reliability. | S7 | [E] | K02; a22, a19, b23 |
| A9 | **An uncalibrated judge is a novice rater.** Calibrate any judge on a small rated set from our own task class before use; require agreement above the human-human floor; never validate on human-written ideas only. | G5, S0 | [E] | K03, K21, K25; a18, a23, d02, d13 |
| A10 | **Run judgments under two paraphrased prompts; disagreement means "cannot tell".** | G5 | [E] | K21; d02, d03 |
| A11 | **Add a claim-attribution check for novelty claims**: name the nearest prior, say what is left, code checks the leftover is non-empty. Note: the fix was built after seeing the failure, so measure it in our domains (see UNKNOWNS). | S4, G8 | [E] | K26; d05, c13, d04 |
| A12 | **Judge explanations are hints for revision, never evidence** (G10 consistency). | G10 | [E] | K17; b11, c09 |
| A13 | **Strip authorship, normalise style and never label an idea as the judge's own**; prefer a judge from a different model family than the generator. (The raw effect is contested, the label effect is not.) | G5 | [E] for labels; [C] for hidden self-preference | K22; d06, d07, d19, d10 |
| A14 | **Embedding distance is for dedup and coverage only**, not a creativity score (item-level r .13-.24; near zero against humans on stories). | S3 | [C], conservative use | K09; c30, b15, a15 |

### Test first (single-source or contested)

| # | Take | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Execution as the validator.** On items with a runnable check, select by pass after a cheap run, and check whether any judge rank correlates with pass. | G8, S4 | [S] | K04; a05, a06, b05, b07, c06, c07 |
| T2 | **Retrieval of nearest prior solutions for the novelty check in open mode.** | S3, S4 | [C] | K08; b19, c19, c21, b16, d02-d04, d15 |
| T3 | **Rubric plus run history judge** relative to the agent's own earlier episodes. | S7 | [C] | K08; b16, b17, d09 |
| T4 | **Two-stage evidence-then-score judge.** | G5 | [S] | K24; d12 |
| T5 | **k=3 pooled judge calls vs one long call.** | S7 | [C] | K23; d03, d10, d11, d17, c24 |
| T6 | **Pairwise vs direct vs batch-of-15 ranking.** | S7 | [C] | K07; a23, b21, c12, a03 |
| T7 | **Judge novelty vs later success (do not select highest-novelty by judge).** | G5 | [S] | K20; d01 |
| T8 | **Diversity count does not rank; keep k distinct candidates for execution.** | S7 | [S] | K27; d14, d16 |
| T9 | **Hidden self-preference** under authorship-hidden, style-normalised conditions with our own generator. | G5 | [C] | K22; d06, d08, d09, d10 |
| T10 | **Ritchie or SPECS multi-criterion scoring** vs pass/fail. Vocabulary only until tested. | none | [S] | K18; a10-a13, d18 |

---

## 8. Concrete tests on our bench

All tests compare arms at **equal total tokens** (G7) and count setup cost. "Open items" are NoveltyBench-style prompts and our open-mode idea tasks; "checked items" are ARC and BRAINTEASER items with a runnable check; "rated set" is a small expert-rated idea set (target 40-60 items, at least 3 raters, reliability reported first).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| **B1 Judge-vs-random selection** (T1, A1) | Checked items, open-mode ideas that can be run | (a) agent picks top-1 of n=8 candidates by its own judge; (b) random pick; (c) pick by pass on the check; (d) pick by judge-with-retrieval | Pass rate of the picked candidate; Spearman of judge rank with run outcome | (a) not above (b) (consistent with 29% vs 35.3% random); (c) wins by definition; (d) if it beats (b) by 10+ points, keep |
| **B2 Rating reliability baseline** (K01) | Rated set | 2 independent judge samples vs 3 human raters | Split-half top/bottom 25% (human baseline 56.1%); Spearman-Brown projected reliability | Judge-judge split-half 60-80% (self-agreement), judge-human 45-55% |
| **B3 Pool size k** (T5, K23) | Rated set | k=1 long judgment vs k=3 short vs k=5 short, same total tokens | Spearman with pooled human mean; agreement curve | k=3 +2 to +5 points over k=1; saturation at k=3-5 |
| **B4 Pairwise vs direct vs batch-15** (T6, K07) | Rated set and a venue/outcome-labelled set | Direct score; pairwise tournament; forced ranking in batches of 15 with 5 shuffled repeats | Spearman and top/bottom-25% accuracy | Batch ranking best; pairwise worst on model-written ideas (bias toward ties broken to model output) |
| **B5 Length residualisation** (A3, K10) | Open items, long vs core-idea | Raw score; score residualised on token count; core-idea-only score | Win-rate of agent output over a human reference; length-score correlation | Win-rate falls 10+ points when elaboration is removed (cf. -1.43 points on AUT) |
| **B6 Retrieval-grounded novelty** (T2, K08) | Rated set | Bare judge; retrieval top-10 plus bare verdict; retrieval plus claim-attribution step | Spearman with held-out expert rating; false "novel" rate on known-copy ideas | Retrieval +0.05 to +0.15 rho; attribution lowers false "novel" on copies; may raise false rejects |
| **B7 Evidence-then-score** (T4, K24) | Rated set | Direct judge; CoT judge; two-stage extract-then-score | QWK with experts; length correlation | Two-stage higher by 0.1+ QWK and lower length correlation |
| **B8 Prompt stability** (A10, K21) | Rated set and agent ideas | One prompt; two paraphrased prompts with "cannot tell" on disagreement | Share of flipped verdicts; accuracy on the non-flipped subset | 20-50% of verdicts flip; accuracy rises on the kept subset |
| **B9 distinct_k stop rule** (A5, K11) | Open items | Fixed n draws; stop when no new cluster appears in last m draws; with and without history in context | distinct_k per 1,000 tokens; best-of-set utility | History in context doubles distinct_k per token; stop rule saves tokens at same best-of-set |
| **B10 Diversity vs success** (T8, K27) | Checked items with 3 candidates | Execute the 3 most distinct vs 3 top-judge vs 3 random | success@3 | Distinct set at least as good as judge set; no per-idea ranking by distinctness |
| **B11 Self-preference** (T9, K22) | Rated set | Judge from generator family with labels hidden and style normalised; judge from other family; labelled as own | Judge-minus-reference score delta for own vs other-family ideas | Hidden: near 0; labelled: shift of 0.1-0.3 points |
| **B12 Rubric plus history judge** (T3) | Agent trajectories on checked items | Bare novelty judge; rubric with anchors; rubric plus history | Spearman with annotators; correlation with later pass | Rubric-history .65-.75 with annotators; unknown on pass (the open question) |

---

## 9. What does not transfer, and why

- **CAT with human expert panels.** Needs paid experts and many raters (10-13). We keep the *protocol* (independent scores, pooled, reliability reported), not the panel.
- **Fine-tuned scorers (Ocsai, poly-encoders, reward models).** r .74-.81 and 78% need labelled training data and same-task training; we have no training. They show only that zero-shot judges lag.
- **Hidden-state probe (TPR).** Needs open-weight models with hidden-state access and in-distribution training (c10). Out of scope.
- **Ritchie criteria and SPECS.** Built for people evaluating a system; thresholds unprincipled, weights chosen by the evaluator, validated by builder opinion only. Where a check exists, pass/fail is the signal (ALPS).
- **Reference-corpus n-gram rarity (c24).** Needs the model's training data to be indexed. Not available for closed models.
- **Latent-variable correlations (Beaty r .91).** They remove measurement error; an agent scores single ideas, so item-level r (.13-.24) is the right expectation.
- **AUT-style short-answer scorers.** Based on one- to five-word uses of an object; our ideas are longer and task-bound.
- **Agreement on chat helpfulness (>80%).** Different construct.
- **Execution result in NLP prompting (43 ideas).** The flip may depend on vague claims that fail when made concrete (a06). Not shown for ARC, code or puzzles; also in our checked tasks, "execution" is an automatic test, cheaper and less noisy than 100 hours of expert work.
- **Human-vs-AI idea comparisons.** Our question is which of our own candidates to pick, not whether AI beats experts.
- **Poetry and story results.** Chosen venue or upvotes as truth (Sawicki, LitBench) are popularity or prestige, not creativity; contamination possible for published poems.

---

## 10. Open questions

1. Does any cheap judge (retrieval-grounded, rubric plus history) rank ideas by later execution success? Only the Ideation-Execution Gap measures outcomes, and it did not test judges. HindSight is a similarity-to-later-paper outcome, not execution. (gap 1)
2. Does distinct_k or semantic entropy correlate with later usefulness of a single idea, or only with set diversity? (gap 2)
3. At equal tokens, is k-sample pooled judging better than one long judgment, and where does the curve saturate? Only k=3 tested. (gap 3)
4. Does length and elaboration residualisation remove the machine-text bias for ideas, not just AUT answers? (gap 4)
5. How large is the self-preference bias when the judge is the generator and authorship is hidden? Conflicting evidence. (gap 5)
6. How stable is retrieval-grounded novelty to the corpus and its date, measured on the same ideas? (gap 6)
7. Is the novelty mirage reproduced for ideas in our domains with a narrowness test? Fixes were built after the failure. (gap 7)
8. What is the minimum labelled calibration set per task class to make a zero-shot judge usable? Fine-tune on about 140 labels was worse than a decomposed rubric; no curve. (gap 8)
9. Do Ritchie or SPECS-style multi-criterion scores add anything over pass/fail on checkable tasks? (gap 9)
10. Is novelty-by-judge worse than random for the best 2026 models on ideas in our own domain? The negative HindSight correlation is one judge (Qwen3-32B), one generator.
11. Does the Ideation-Execution flip appear when execution is automatic (tests) rather than expert-built papers?
12. Do exact figures held at abstract level only (RQ-Bench 78/56, 82/52, 27.2 to 49.1; RINoBench F1 17.2; Bhushan rho .732; Tutone tau values) survive a full re-read? The critique could not re-open them.

---

## 11. Sources

[V] = opened and read this session (full text or substantial part). [M] = from memory, snippet, news summary or citation only. Some [V] entries were read only in parts (noted).

| # | Source | Mark | URL |
|---|---|---|---|
| 1 | Si, Yang, Hashimoto (2024) Can LLMs Generate Novel Research Ideas? | [V] | https://arxiv.org/abs/2409.04109 |
| 2 | Si, Hashimoto, Yang (2025) The Ideation-Execution Gap | [V] | https://arxiv.org/abs/2506.20803 |
| 3 | Falk et al. (2025) How Do Hackathons Foster Creativity? | [V] | https://arxiv.org/abs/2503.04290 |
| 4 | Ritchie (2007) Some Empirical Criteria for Attributing Creativity to a Computer Program | [V] | https://doi.org/10.1007/s11023-007-9066-2 |
| 5 | Jordanous (2013) Evaluating Computational Creativity: SPECS (thesis) | [V] | https://kar.kent.ac.uk/42388/ |
| 6 | Beaty and Johnson (2021) SemDis | [V] | https://doi.org/10.3758/s13428-020-01453-w |
| 7 | Buczak et al. (2022) The Machines Take Over | [V] | https://eldorado.tu-dortmund.de/handle/2003/42333 |
| 8 | Organisciak et al. (2023) Beyond semantic distance (Ocsai) | [M] | https://doi.org/10.1016/j.tsc.2023.101356 |
| 9 | Kaufman, Baer, Cole, Sexton (2008) Expert vs nonexpert raters, CAT | [V] | https://doi.org/10.1080/10400410802059929 |
| 10 | Baer, Kaufman, Gentile (2004) Extension of the CAT to nonparallel tasks | [V] | https://www.rider.edu/sites/default/files/2024-05/baerkkaufmangentile.pdf |
| 11 | Kaufman, Christopher, Kaufman (2008) The Genius Portfolio | [V] | https://doi.org/10.2190/EM.26.2.c |
| 12 | Clements et al. (2018) Expertise in evaluating choreographic creativity | [V] | https://doi.org/10.3389/fpsyg.2018.01448 |
| 13 | Chakrabarty et al. (2024) Art or Artifice? (TTCW) | [V] | https://arxiv.org/abs/2309.14556 |
| 14 | Sawicki et al. (2025) Can LLMs Outperform Non-Experts in Poetry Evaluation? | [V] | https://arxiv.org/abs/2502.19064 |
| 15 | Lamb, Brown, Clarke (2015) Can human assessment of machine-generated poetry be trusted? | [M] (via Sawicki) | https://arxiv.org/abs/2502.19064 |
| 16 | LitBench (2025) | [V] | https://arxiv.org/abs/2507.00769 |
| 17 | Zhang et al. (2025) NoveltyBench | [V] | https://arxiv.org/abs/2504.05228 |
| 18 | Wu et al. (2026) NovBench | [V] (abstract, set-up, one table) | https://arxiv.org/abs/2604.11543 |
| 19 | Kaufman, Baer, Cole (2009) Expertise, domains, and the CAT | [M] | https://www.rider.edu/sites/default/files/2024-05/ExpertiseDomains%26CAT.pdf |
| 20 | Amabile (1982) Social psychology of creativity: a CAT | [M] | https://doi.org/10.1037/0022-3514.43.5.997 |
| 21 | Zheng et al. (2023), as quoted in Sawicki (chat judge agreement over 80%) | [M] | https://arxiv.org/abs/2502.19064 |
| 22 | Tutone, Franceschelli, Musolesi (2026) The Limits of Automatic Evaluation of Creativity | [V] | https://arxiv.org/abs/2608.23705 |
| 23 | Bhushan, Zhang, Wang (2026) Can LLM Agents Discover? | [V] | https://arxiv.org/abs/2608.30047 |
| 24 | Shen, Druckmann, Zou (2026) Unlocking LLM Creativity in Science through Analogical Reasoning | [V] | https://arxiv.org/abs/2605.11258 |
| 25 | Poly-Encoders for Automated Creativity Assessment (Grouchnikov, Gregory, Noh 2026) | [V] | https://arxiv.org/abs/2608.26165 |
| 26 | Domanti et al. (2026) Effect of Idea Elaboration on Automatic Assessment of Idea Originality | [V] | https://arxiv.org/abs/2604.20569 |
| 27 | Schopf and Farber (2026) Is this Idea Novel? (RINoBench) | [V] | https://arxiv.org/abs/2603.10303 |
| 28 | Schopf, Schreieder, Aizawa (2026) Think-Probe-Respond | [V] | https://arxiv.org/abs/2608.25660 |
| 29 | Sinhahajari, Majumder, Poria (2026) On the Limits of LLM-as-Judge for Scientific Novelty (RQ-Bench) | [V] (abstract level in critique) | https://arxiv.org/abs/2606.12071 |
| 30 | Literature-Grounded Novelty Assessment of Scientific Ideas (2025) | [V] (page-fetch summary) | https://arxiv.org/abs/2506.22026 |
| 31 | Automated Creativity Evaluation of Language Models Across Open-Ended Tasks (2026) | [V] (page-fetch summary; last third unread) | https://arxiv.org/abs/2606.11762 |
| 32 | Measuring LLM Novelty As The Frontier Of Original And High-Quality Output (2025) | [V] (page-fetch summary) | https://arxiv.org/abs/2504.09389 |
| 33 | The Unlikely Duel (2024) | [V] (page-fetch summary) | https://arxiv.org/abs/2406.15891 |
| 34 | Franceschelli and Musolesi (2024) Creative Beam Search | [V] | https://arxiv.org/abs/2405.00099 |
| 35 | Koivisto and Grassini (2023) Best humans still outperform AI in a creative divergent thinking task | [M] (news summary) | https://www.psypost.org/2023/10/artificial-intelligence-outperforms-the-average-human-in-a-creative-thinking-test-213944 |
| 36 | Organisciak et al. project page (Ocsai) | [M] | https://openscoring.du.edu/research |
| 37 | S-DAT (2025) Multilingual, GenAI-driven divergent thinking assessment | [V] (page-fetch summary) | https://arxiv.org/abs/2505.09068 |
| 38 | Jiang (2026) HindSight | [V] | https://arxiv.org/abs/2603.15164 |
| 39 | Sternlicht et al. (2026) Old Ideas, Novel Problems | [V] | https://arxiv.org/abs/2610.02022 |
| 40 | Du, Zhang et al. (2026) RINI: Seeing the Prior Is Not Enough | [V] | https://arxiv.org/abs/2609.33284 |
| 41 | Chae et al. (2026) Self- and Other-Labels Induce Bidirectional Bias in LLM Judges | [V] (Table 7 row mapping garbled) | https://arxiv.org/abs/2608.18091 |
| 42 | Pombal, Rei, Martins (2026) Self-Preference Bias in Rubric-Based Evaluation | [V] | https://arxiv.org/abs/2604.06996 |
| 43 | Lyu, Kim, Xiao, Luan (2026) Why LLMs and Humans Converge and Diverge in Evaluating Ideas | [V] | https://arxiv.org/abs/2607.22218 |
| 44 | Wang et al. (2026) Decoupled Analysis-Judging (CreaEval) | [V] (AUT and TTCW cells not verified) | https://arxiv.org/abs/2609.03432 |
| 45 | Ho et al. (2026) SoundnessBench | [V] | https://arxiv.org/abs/2605.30329 |
| 46 | Wadhwa et al. (2026) Training Reasoning Models to Generate Diverse Ideas | [V] | https://arxiv.org/abs/2610.22324 |
| 47 | Pei, Guo et al. (2026) DeepInstructor | [V] | https://arxiv.org/abs/2609.22104 |
| 48 | Chen, Zhao, Cohan (2026) Measuring the Gap Between Human and LLM Research Ideas | [V] (abstract and introduction) | https://arxiv.org/abs/2607.01233 |
| 49 | Chan et al. (2025) J1: Test-Time Scaling for LLM-as-a-Judge | [V] (abstract, introduction, appendix A) | https://arxiv.org/abs/2505.11875 |
| 50 | Xie, Ye, Zhang (2026) ALPS | [V] (abstract, introduction, method) | https://arxiv.org/abs/2608.15979 |
| 51 | Panickssery, Bowman, Feng (2024) LLM Evaluators Recognize and Favor Their Own Generations | [V] | https://arxiv.org/abs/2404.13076 |
| 52 | Boden (creative types, surprise); Colton (creative tripod); Plucker et al. (2004); Mayer (1999) | [M] (via Jordanous thesis, source 5) | https://kar.kent.ac.uk/42388/ |
