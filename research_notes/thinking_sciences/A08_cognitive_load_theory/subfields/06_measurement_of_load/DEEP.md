# Measurement of load: deep document

*Subfield A08.06 of cognitive load theory (CLT). Written 2026-11-20 from evidence_a-d.jsonl (a01 to d17), claims.jsonl (A08.06-K01 to K29) and critique.md in this folder. Evidence ids below (a04, b06, d05 ...) point to lines in those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

*Honesty note up front. Two anchor papers of this subfield were never read: Hart and Staveland (1988) and DeLeeuw and Mayer (2008). Skulmowski and Rey "2020" was not located as a measurement paper. Paas (1992) and Paas and van Merrienboer (1993) were not opened. Numbers for those come only from later papers or from the literature as remembered, and are marked so. Nothing here should be quoted from them as a measured figure.*

## 1. What it is

CLT says working memory is small, and learning or problem solving goes wrong when the load on it is too high. Load is split into three kinds. Intrinsic load comes from the task itself (how many elements must be held and related). Extraneous load comes from how the task is presented (clutter, bad layout, irrelevant detail). Germane load is the effort spent building understanding. Measurement of load asks: how do we find out how much of each kind a person carried?

The field uses four families of measure.

1. **Subjective ratings.** The 9-point single-item mental-effort scale (Paas 1992, a15); a difficulty item; NASA-TLX with six subscales (Hart and Staveland 1988, a01, manual d14); multi-item questionnaires for the three load types (Leppink 2013, Klepsch 2017, Eysink 2009; a06, a08, b01).
2. **Performance and efficiency.** Accuracy, time, and combined scores such as relative condition efficiency (Paas and van Merrienboer 1993, a14).
3. **Dual-task (secondary-task) measures.** A second, simple task runs at the same time. Slower or worse secondary performance means the main task used more capacity (b14, b15).
4. **Physiology.** Eye measures (pupil, blink, fixations), heart (rate, variability), skin, brain (EEG) (b05 to b07, b20).

The central measurement problems, all documented below:

- The measures disagree with each other and respond to different manipulations (K01, K08).
- The three load types are hard to separate by questionnaire; germane load is the weakest (K02, K03).
- A self-rating is a metacognitive judgement shaped by cues, not a clean readout (K06).
- Most validation is on university students in short multimedia lessons (K22).
- Almost nothing has measured load on a language model with a validated instrument (K22, d17).

**Why it matters for our agent.** The schema wants to spend tokens by difficulty (G12), think briefly (G11) and let code, not the model's opinion, decide transitions (SCHEMA section 1). That needs a cheap, trustworthy load or difficulty signal. This subfield tells us which signals to distrust (self-ratings, mixed-type scores). The LLM literature gives one usable proxy: output tokens, with caveats. The subfield row already says "use tokens and accuracy instead". This document tests that advice against the evidence.

## 2. History and theories in depth

### 2.1 Origins (background, partly second-hand)

- **Sweller (1988).** CLT started with intrinsic and extraneous load only (a13 notes this). Germane load was added later. Calls to drop germane load and return to two parts came from Kalyuga (2011) and Leppink and van den Heuvel (2015) (a13).
- **Hart and Staveland (1988), NASA-TLX.** Built from several years of work on what makes workload feel different across tasks (a01). Six subscales: mental demand, physical demand, temporal demand, performance, effort, frustration. The person compares all 15 pairs of subscales, giving each a weight from 0 to 5 (a02, d14). An earlier nine-subscale bipolar version was too long and partly redundant (d14). The NASA manual says one weight set reused across versions of a task added only slight sensitivity for the cost, and that retrospective ratings correlated highly with online ratings in helicopter and supervisory-control simulations. No coefficient is in the manual (d14). The chapter was not read. Reliability and sensitivity figures are unknown to us (GAP 4, open).
- **Paas (1992).** Introduced the single-item 9-point mental-effort scale, "very, very low mental effort" to "very, very high" (a15). Paper not opened; the scale form is confirmed by Ouwehand et al. 2021 (a04).
- **Paas and van Merrienboer (1993), relative condition efficiency.** Standardise effort rating and test performance, then take the signed distance from the line where they are equal: E = (zPerformance - zEffort) / sqrt(2). High performance at low effort is efficient (a14). Formula from the literature, not re-derived from the paper.

### 2.2 The three-measure test: DeLeeuw and Mayer (2008)

DeLeeuw and Mayer compared three measures against manipulations aimed at the three load types: a secondary visual-monitoring reaction-time task, a difficulty rating, and a mental-effort rating (a10). The reported pattern, restated in Ouwehand et al. 2021 (d13, d16): difficulty ratings follow intrinsic load, effort ratings follow germane load, reaction time follows extraneous load. Correlations among the three were low, read as support for separable load types. We have no sample sizes or correlations (second-hand only). The FLoRA replication atlas lists one replication, Zu et al. (2020), recorded as successful and using eye movements (a11, a24). No failed replication is recorded, but atlas coverage is partial, and Korbach et al. (2018) found the eye-tracking index did not separate groups (a09). Status [C].

### 2.3 The questionnaire line

- **Leppink et al. (2013).** Ten-item questionnaire. PCA (n=56 PhD students) gave three components; confirmatory analyses on three cohorts (ns 171, 136, 148) and a randomised experiment (n=58) supported it (a08). Experiments 2 and 4 only partly supported three factors, and germane ratings did not correlate with performance (b09).
- **Leppink et al. (2014).** Said support for germane load as a third factor was limited (b09).
- **Klepsch, Schmitz and Seufert (2017).** Two instruments (a06, a07). Study 1 N=97. Naive item alpha: ICL .86, ECL .80, GCL .80. High vs low load separated by both the trained "informed" rating (F(1,89)=293.32, partial eta2=.77) and the naive items (F(1,89)=199.96, eta2=.69); no difference between methods (p=.28). Study 2 (N 65 to 95 per task): alpha ICL .81, ECL .86, GCL .67 (three items), .85 after dropping an item. The factor analysis describes an ECL factor plus a broad GCL+ICL factor with a nested ICL factor, so intrinsic and germane are hard to separate (a07).
- **Jiang and Kalyuga (2020).** N=60 EFL students. A two-factor model (intrinsic + extraneous, germane items reverse-scored) fit very well: chi2=54.069, df=53, p=.433, CFI .994, TLI .993, RMSEA .018, SRMR .077 (b08). No head-to-head against three factors.
- **Zu, Munsell and Rebello (2021).** Physics students. An eight-item survey gives two components at low prior knowledge (Exp 2, N=139 pre/post) and three at higher knowledge. Exp 3 (N=40) ratings followed the manipulated load type (d12). A clean boundary: the three-factor structure depends on how much the learner knows.
- **Krieglstein et al. (2022) meta-analysis.** The best summary (b01 to b04, b25). Numbers in section 3.

### 2.4 Physiology and dual-task

- **Dual-task.** Schoor, Bannert and Brunken (2012) showed design choices create or hide effects (b14). Esmaeili Bijarsari (2021) states the paradigm lacks standardisation in modality, frequency and timing, and the secondary task can intrude on the main task (b15).
- **Physiology.** Ayres et al. (2021) is a vote count over 28 studies of intrinsic load, 2016 to 2020 (b05 to b07). Scheiter, Ackerman and Hoogerheide (2020) review dissociations and argue effort appraisals are metacognitive judgements that use cues such as response time (b12, b13). Hughes et al. (2019) report in the abstract that several cardiac metrics are sensitive to workload (b20, abstract only).

### 2.5 The "lab did not hold outside the lab" claim

The subfield row says lab correlations did not hold outside the lab and cites Skulmowski and Rey (2020). We could not locate a 2020 measurement paper by them. Found: Skulmowski and Rey (2020, a12, not opened) is characterised by a later review as showing survey wording changes extraneous-load readings in interactive media (a13). Skulmowski and Rey (2017, d15) is a mini-review of embodied learning where the TLX mostly showed no significant differences and the Paas item was significant in some studies, not others. So the claim is a mixed vote count, not a measured lab-to-field gap (K22). Field-like data: Minkley et al. (2021, N=309 school students, d11) found heart-rate variability did not predict performance while ratings did.

### 2.6 The LLM turn (2023 to 2026)

CLT entered LLM work in three ways.

1. **As a lens for benchmarks.** GSM-IC (Shi 2023, c09) added irrelevant sentences to math problems. ICE (Adapala 2025, c01) added junk to multi-hop questions. CogniLoad (Kaiser 2025, a16) varies intrinsic difficulty, distractor ratio and task length separately. ToolLoad-Bench (c26) splits tool-use difficulty into intrinsic and extraneous parts (abstract only).
2. **As a design lens for agents.** CoThinker (Zhou 2025, a20, c23 to c25) spreads intrinsic load over specialist agents. CLAI (Zhang 2025, c05 to c08) proposes load-aware token budgets.
3. **As a measurement idea.** Token counts of reasoning models are compared with human reaction times (de Varda 2025; Hu and Wang 2026; Davidson 2025; b16 to b19). Probes on hidden states and verbalised confidence are compared as difficulty signals (d01 to d04). Within-item token length versus accuracy is studied (d05 to d07, d09).

No study found gives a model a rating scale and validates it against behaviour (K22, d17; the search was narrow).

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Subjective and eye measures detect and match intrinsic-load manipulations best; brain worst | Detection: subjective 94% (30/32), eyes 87% (20/23), skin 85% (11/13), heart 68% (15/22), brain 68% (23/34); Kruskal-Wallis chi2=9.67, df=4, p=.046; no pairwise test survived Benjamini-Hochberg. Match with expected ordering: subjective 78%, eyes 78%, heart 64%, skin 62%, brain 32% (chi2=18.52, p<.001). 28 studies, 33 experiments, mean 29.2 participants (SD 14.8) | Ayres 2021 (b05, b06) | [E] (vote count, no effect sizes) |
| Single-item ratings did best | Single-item: 100% detection, 100% match (8 instances). NASA-demand 100%/86%; NASA-overall 90%/70%; NASA-effort 86%/57%. Blink rate 100%/83%; pupil diameter 73%/64%; EEG beta 71%/0%; theta 50%/17%; HRV 50%/50% | Ayres 2021 (b06) | [E] |
| Validity depends on task type | Memory tasks 90% detection, 90% match; arithmetic 90%/65%; heart measures on word tasks 0% | Ayres 2021 (b07) | [E] |
| Questionnaire reliability is good | Pooled alpha, Leppink 2013: ICL .776, ECL .798, GCL .734; Leppink 2014: ICL .851, ECL .788, GCL .806; Eysink 2009 ECL .740. 53 articles, 67 experiments, N=7413 | Krieglstein 2022 (b01, b02) | [E] |
| Scale points matter | Odd-point and 9-point scales did well; even-point scales gave lower ECL reliability; authors favour 9 points. Subgroup cells small and partly conflicting | Krieglstein 2022 (b02, b25) | [E] on 9-point |
| Load types correlate against theory | ICL-ECL r+=.298 (k=25, CI .221 to .370, Leppink 2013); ECL-GCL r+=-.186 (k=20, Leppink 2013); the larger -.331 comes from k=2 studies (Leppink 2014), weak; Eysink 2009: all three positive | Krieglstein 2022 (b03, critique) | [E] |
| Ratings relate weakly to learning | Leppink 2013: ICL-retention r+=-.061 (ns), ECL-retention -.114, GCL-retention .188 (k=15), ICL-transfer -.188, ECL-transfer -.120, GCL-transfer .173. Klepsch: ECL-transfer -.261, GCL-transfer .217. Eysink 2009 GCL NEGATIVE with retention (-.223) and transfer (-.182) | Krieglstein 2022 (b04) | [E] |
| Germane load is not cleanly separable | Two-factor fit chi2=54.069, df=53, p=.433, CFI .994, RMSEA .018 (N=60). Two components at low prior knowledge, three at higher (N=139). Klepsch GCL alpha .67 (3 items), .85 after dropping one | Jiang and Kalyuga 2020 (b08); Zu 2021 (d12); Klepsch 2017 (a06) | [C] |
| Effort rating works through confidence | 35 papers, 83 samples, 236 effect sizes: effort to monitoring beta=-.19 (CI -.27 to -.12); monitoring to learning beta=.29 (CI .22 to .36); indirect beta=-.05 (CI -.08 to -.03); direct effort to learning beta=-.07 (CI -.16 to .02), ns. Earlier meta-analysis r=-.35 (second-hand). Moderators all ns (weak power) | David 2024 (b11, b24) | [E] |
| Effort and difficulty are different constructs | N=1543 students, 128 items in 32 tasks: effort vs perceived difficulty r=.78; effort vs relative difficulty r=-.69; perceived difficulty vs relative item difficulty r=-.80 for open-ended (n=65) vs r=-.45 for multiple choice (n=61), q=.62, z=3.41 | Schuessler 2024 (b10) | [E] |
| Best rating format depends on item difficulty | N=46, 2x4 within. Scale effect on effort F(1,45)=30.97, eta2=.41; on difficulty F=36.45, eta2=.45; accuracy .95 simple vs .51 complex. Numeric scales tracked performance on complex items, pictorial on simple. Time on complex: weights 70.77 s, Likert 48.94 s, VAS 43.84 s, emoticons 53.15 s | Ouwehand 2021 (a04, a05, d13) | [S] |
| Raw TLX can differ much from weighted TLX | Long arm n=7: weighted 65.29 vs raw 51.81. Median questionnaire time 156 s (long) vs 81 s (short). 34 started, 20 completed | Pahr and Di Bartolomeo 2025 (a02, a03) | [S] (tiny N) |
| Dual-task effects depend on design | N=96. Non-contiguous secondary task: visual-only RT 916.19 (SD 564.57) vs audiovisual 773.87 (SD 393.14), F(1,94)=20.17, p<.001, partial eta2=.17. Contiguous: 526.87 vs 523.37, F=0.03, p=.87. Interaction F(1,94)=10.43, eta2=.10. Learning scores no difference (p=.28) | Schoor 2012 (b14) | [E] (with b15) |
| Separate measures dissociate | Paas 1994: HRV separated only active from rest while ratings tracked design. Korbach 2018 (N=78): rhythm secondary task and ratings higher for mental animation; eye-tracking ICA no difference. Richter and Scheiter 2019: pupil size showed a signalling benefit, ratings did not | Scheiter 2020 (b12); Korbach 2018 (a09) | [E] on the dissociation |
| Field data: ratings beat HRV | N=309 school students. Regression on performance: mental load beta=-.326 (p<.001), effort beta=+.309 (p<.001), LF/HF beta=.174 (p=.051), RMSSD beta=-.084 (p=.344). Most correlations explain under 10% of variance | Minkley 2021 (d11) | [S] |
| TLX in embodied learning mostly null | Two experiments (Skulmowski and Rey 2017), two (Kaspar and Vennekoetter 2015): no difference for most subscales; effort significant in one, physical demand in two. Paas item significant in some, not others | Skulmowski and Rey 2017 (d15) | [S] (review, no effect sizes) |
| Eye-movement replication of DeLeeuw and Mayer | One replication on record (Zu 2020), "successful" from the abstract | FLoRA atlas (a11, a24) | [C] |
| Token count tracks human reaction time | GPT-OSS-20B within-task rho .24 to .87; 120B .27 to .91, all p<.01. DeepSeek-R1 mean rho .57, across tasks r=.97 over 7 tasks (de Varda 2025, second-hand). Distillation lowers it, rho .64 to .34 (second-hand). Abductive task: averaging sampled paths raised GPT-OSS-20B .41 to .55 (snippet) | Hu and Wang 2026 (b16, b17); b23 | [E] weak proxy |
| Token-to-human-time link is weak in a real task | Content moderation, six reasoning models, humans N=1,854, 27,810 decisions (27,071 analysed pairs): overall r=.15 to .19; elasticity 0.09% to 0.28% per 1% CoT length; top vs bottom quintile 26 to 39% longer human time. Mean human time 15.3 s. Close pairs: humans +4.5 s. Mean tokens o3 303.5, Gemini 2.5 Pro 897.9, Grok 4 1600.3. The "one SD about 1 s, Grok beta 1.245" line is unverified | Davidson 2025 (b18, b19, critique) | [S] |
| Effort setting is a cap, not a dial | Mean alignment .570/.567/.562 (low/medium/high); BF10 .41, .43, .42 (inconclusive); complexity direction correct 16/16, 16/16, 15/16; 12 model-by-task units. Vankov 2026: negligible accuracy effect in 5 of 6 tasks (second-hand) | Hu and Wang 2026 (b16, b17) | [C] |
| Longer chains go with lower accuracy within the same item | Ten models, 16 CoTs per question (HARP, GPQA-Diamond): length negative for most models; failed-step fraction predicts better than length; selecting by it gives up to 10% gain on AIME. Omni-MATH, +1000 reasoning tokens: -3.16 points o1-mini, -1.96 o3-mini (medium), -0.81 o3-mini (high). o3-mini (m) uses fewer tokens than o1-mini on 63% of jointly solved items; o3-mini (h) uses over 2x the tokens of (m) for about +4% accuracy | Feng 2025 (d05); Ballon 2026 (d06) | [E] (correlational) |
| Over-reasoning on easy prompts | DNR Bench, 150 prompts, 1000-token cap. Reasoning models emit up to 70x the tokens of GPT-4o; 2x to 20x with instructions. DS-R1-Distill-14B produced over 27,000 tokens and repeated one block 120 times. Budget setting does not cure it: GPT-OSS-120B high Math .16, Redundant .28, Unanswerable .12 | Bamgbose 2026 (d08, d09); c20, d07 (abstract) | [E] |
| LLM accuracy falls with task length most | CogniLoad, 22 models. N=20 to 50: DS-Llama-70B 0.89 to 0.66; Qwen3-8B 0.71 to 0.40. By d=5, 12 of 22 below 50%. d=10: gpt-5 .82, o3 .80. N=250: only gpt-5 .76 and o3 .68 above .50. d and log10 N negative in every model. ECL50: gpt-5 382.8, o3 356.9, gpt-5-mini 164.1, gemini-2.5-pro 153.3 | Kaiser 2025 (a16, c13, c15) | [S] (one paper, counted once) |
| Distractor effect is non-monotonic | Lowest accuracy at 25 to 50% needle; gpt-5 .97/.89/.91 across low/mid/high; gemini-2.5-flash-lite .38 to .53 (opposite direction); Phi-4-reasoning-plus .59 to .45; EXAONE-Deep-32B .47 to .32. Quadratic term better AIC in 18 of 22; five models (incl. o3, gemini-2.5-pro) indifferent. gemini-2.5-flash overflowed on 280/350 at N=250 vs gpt-5 32/350 | Kaiser 2025 (a17, a18, c14, c16) | [S] |
| Irrelevant context hurts; length alone does not explain it | GSM-IC: under 30% of base problems solved under all distractor variants (code-davinci-002, text-davinci-003); role-overlap distractors drove text-davinci-003 macro accuracy to 0 on problems over 2 steps. ICE, Gemini-2.0-Flash: control .85, 20% .82, 50% .78, 80% .72, slope -0.003 per % (CI -.004 to -.002); length-matched control .82 (p=.45); residue .78 (p=.12); hop recall .90 to .75 | Shi 2023 (c09, c11); Adapala 2025 (c01, c02, c04) | [E] on direction; ICE single-author |
| Small models sit on the floor | Llama-3-8B, Llama-3-70B, Mistral-7B 0% in every ICE condition; GPT-4o control .65, 80% load .55, slope -.002 (p=.07); about 32% of GPT-4o outputs lacked a final answer (12% after structured prompting) | Adapala 2025 (c03) | [E] with CogniLoad |
| Ignore-irrelevant prompt line | GSM-IC: "Feel free to ignore irrelevant information" helped; "Solve grade school math problems" alone did not; self-consistency over 20 samples about +11 points micro (+35.5 points on 0-CoT, a gain not a level); right answer in the 20 samples 99.7% (CoT, LTM; 96.5% for 0-CoT); best macro still 45%; clean GSM8K 59.3 to 60.3. DNR Bench, 1000-token cap, with instruction: redundant R1 .00 to .76, Claude-3.7-Thinking .40 to 1.00, o3-mini-high .00 to .04, GPT-4o 1.00 to 1.00; unanswerable R1 .00 to .20, Claude .12 to .82, GPT-4o .42 to .98; indifferent category Claude .80 to .04 (hurt) | Shi 2023 (c10); Bamgbose 2026 (d08) | [S] model specific, can backfire |
| Load-aware prompting saves tokens at near equal accuracy | Llama-3-70B GSM8K: CoT 92.5% at 485 tokens vs CLAI-Prompt 92.3% at 310 (-36.1%); MATH 53.9% at 812 vs 53.5% at 525 (-35.3%); CLAI-Tune (Llama-3-8B student) GSM8K 91.5% at 255 vs 90.1% at 450 | Zhang 2025 (c06, c07) | [S] unreplicated, no variance, baseline mismatch (92.5 vs 90.1) |
| CLT-style multi-agent split | LiveBench Gemini-1.5-Pro: Math 75.3 vs 70.0; Reasoning 44.7 vs 43.0; Instruction 81.8 vs 84.4; Flash-8B Instruction 68.1 vs 84.3; 16 of 25 paired comparisons significant; the 3 significant losses all instruction-following. Tokens per question: IO 650 to 710, CoThinker 13,558 to 14,323, MAD 12,389 to 16,104. At an 8,192-token cap: Gemini-2.5 Math/Reasoning 76.3/69.2 vs IO 59.3/31.0 | Zhou 2025 (a20, c23 to c25) | [C] |
| At equal thinking tokens a single agent matches or beats multi-agent | Qwen3-30B-A3B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash/Pro; FRAMES and MuSiQue; budgets 100 to 10,000 thinking tokens; five MAS designs. Sample cell MuSiQue R1-70B: SAS .418 vs Sequential .327. API budget-control artifacts found | Tran and Kiela 2026 (d10) | [S] multi-hop QA only |
| Internal probes beat length as a difficulty signal | Spearman with model success rate: Qwen2.5-Math 1.5B and 7B .64; GPT-OSS-20B low .58, medium .50, high .40; length baseline .15 to .30. AUROC Qwen2.5-Math-1.5B greedy .84 vs length .61; GPT-OSS-20B Maj@5 AUROC .78 to .64 low to high. Routing matches the best single model (92%) at about 70% lower cost on MATH. Question-only probes beat verbalised confidence on knowledge questions, falter on math | Lugoloobi 2026 (d01, d02); Cencerrado 2026 (d03) | [S] open weights, needs hidden states |
| Pre-solve verbal confidence is weak | Frontier verbal AUROC pre vs post solve: factual .57/.61 and .66/.70; logic .68/.69 and .77/.70; math .72/.75 and .50/.79 (row-to-model mapping partly ambiguous). Pre-solve ECE on math up to .38. Probes gain .09 to .15 AUROC in some domains | Kale 2026 (d04) | [S] |
| Cardiac metrics respond to workload | No numbers read (abstract only) | Hughes 2019 (b20) | [S] |
| Multi-turn and middle-position losses | 39% average drop over 200,000 simulated conversations (six generation tasks); "lost in the middle" position effect | Laban 2025 (c18); Liu 2023 (c19) | [E], abstract-page evidence only |

## 4. Mechanisms and models

### 4.1 Rating-scale mechanics (human)

- **Single-item effort scale.** One question, 9 points. Fast, reliable enough, best in the physiological comparison (b06). Validity depends on timing (delayed ratings follow the harder items in a set, b10) and on task difficulty (numeric scales for hard items, pictorial for easy, a05).
- **Weighted TLX.** Score = sum over six subscales of (rating 0 to 100) x (weight 0 to 5), divided by 15. Weights come from 15 pairwise "which mattered more" choices. Dropping the weights gives Raw TLX, a plain mean. The gap can be large (65.29 vs 51.81 in n=7, a03) or small in other studies. Weighting adds time (156 s vs 81 s median) and frustration (a02).
- **Why ratings are cue-based.** Scheiter et al. (2020) argue effort appraisals are metacognitive judgements. People infer effort from response time, perceived success and similar cues (b12). David et al. (2024) show the learning link runs through confidence: higher effort lowers confidence (beta -.19), confidence predicts learning (beta .29) (b11). An engineer can read this as: the rating is a noisy function of observable behaviour (time, errors) plus a self-belief term, so it adds little beyond the behaviour itself.
- **Resolution.** Scheiter et al. propose measuring the within-person correlation between effort ratings and an objective effort measure, over at least about ten items per person, as done for confidence (b13). A proposal, not a result. It is the right shape for an agent test (B9).

### 4.2 Efficiency model

Relative condition efficiency: E = (zP - zE) / sqrt(2), with z-scores over a reference population (a14). Higher E means better performance per unit effort. It depends on the effort scale and the reference sample. Agent analogue: E = (z accuracy - z tokens) / sqrt(2), computed over items or over arms at a fixed budget (K23). Log it in every test (G7).

### 4.3 Dual-task logic

The secondary task draws from the same limited pool. If main-task load rises, secondary reaction time rises. It breaks when the two tasks do not compete for the same resource (contiguous task, F=0.03, b14) or when the secondary task intrudes on the main one (b15). A model has no separate pool; a distractor inside the same context is the nearest analogue, and ICE and CogniLoad already do it.

### 4.4 LLM load knobs (CogniLoad model)

CogniLoad fits per model: logit P(correct) = b0 + bd*d + bN*log10(N) + br*r + br2*r^2, with d intrinsic difficulty, N task length (the authors' germane-load proxy, an analogy), r distractor ratio (a18). To implement:

- Generate puzzles with three independent dials; score exact match; fit a binomial GLM per model.
- Load capacity = the value of one dial at which predicted accuracy is 50% (ECL50, c15).
- Keep a quadratic term for r, because the response is U-shaped for most models (K13).
- Use enough items per cell. Open models had 100 per cell; proprietary models 10, so noisier (c12, c13).
- The 32K cap and default decoding shape the fits. Capacity numbers are model-, puzzle- and cap-specific.

### 4.5 Token and trace proxies (what an agent can read for free)

- **Output tokens per item.** Tracks human time (rho .24 to .91 within task; r .15 to .19 in content moderation) and, within an item, predicts error (d05, d06).
- **Failed-step or abandoned-branch share.** Better than length at predicting correctness (d05). Needs a parser that marks branches opened then dropped.
- **Answer instability across samples.** Not measured in this subfield; it is the behavioural check the schema already favours (G4: agreement is a hint, not proof).
- **Pre-generation probe.** A linear probe on hidden states predicts success better than length and supports routing at about 70% lower cost, but weakens as reasoning rises and needs hidden states (d01 to d03). A text-only scaffold cannot use it.
- **Attention entropy and perplexity.** Pilot only: entropy 4.44, 4.80, 5.04 across complexity levels 1 to 3; perplexity on hard tasks moved the wrong way (120.50, 88.97, 85.35), so a proxy can mislead (c24).

### 4.6 Why the proxies disagree (a working model)

Measures differ in what they read. Ratings read perceived difficulty after the fact. Reaction-time probes read spare capacity. Physiology reads arousal, which also rises with stress (Ayres notes stress confounds in surgery simulations, b06). Any single measure mixes load with other states and responds to some manipulations and not others. For an LLM the analogue is that tokens mix difficulty with verbosity, model style and cap (the effort setting acts as a ceiling, b16), so the item-level link is real but noisy.

## 5. What holds up

### 5.1 Established

- **Several measures, little agreement.** Single-item ratings and eye measures lead, brain measures trail (b05 to b07, K01). Heart measures fail on some task types (b07).
- **Questionnaires are reliable but not clean.** Alphas .73 to .85; ICL and ECL correlate positively (r+=.298); ratings relate weakly to learning (about .1 to .26); germane ratings are weakest (b01 to b04).
- **The 9-point scale is the best-supported format** (b02, b25, b06). Which format tracks performance depends on item difficulty (a05).
- **Effort ratings are cue-driven.** The learning link runs through confidence (b11). Effort and perceived difficulty are separate (r=.78; b10).
- **Measures do not transfer across task types** (b07, b10).
- **Dual-task is fragile** (b14, b15).
- **LLMs.** More load sources lower accuracy (CogniLoad, ICE, GSM-IC). Distractors hurt beyond length (ICE length control .82 vs .85, p=.45). Small models sit at the floor (c03). Within an item, longer chains mean lower accuracy (d05, d06, d09). Reasoning models overthink easy prompts (d09, c20, d07).

### 5.2 Failures, nulls and replications

- **DeLeeuw and Mayer.** One successful replication on record (Zu 2020, abstract level) and one tension (Korbach 2018, eye-tracking ICA no difference). No failed full replication recorded. The original numbers could not be confirmed (a11, a09, d16).
- **Three-factor structure.** Held in some samples (Klepsch 2017; Leppink 2013 experiments 1 and 3), failed or only partly held in others (Leppink 2013 experiments 2 and 4; Jiang and Kalyuga 2020; Zu 2021 at low knowledge). Eysink 2009's negative GCL-learning correlation is unreplicated and unexplained (GAP 10).
- **Lab to field.** HRV did not predict performance in N=309 school students while ratings did (d11). TLX mostly showed no differences in embodied-learning studies (d15). Both are small or vote-count evidence.
- **Reasoning-effort dial.** Alignment unchanged across settings (BF10 about .4, inconclusive, b16). Vankov reports negligible accuracy effect in 5 of 6 tasks (second-hand). Contested because tight-cap and structure results (c25) point the other way.
- **Multi-agent decomposition.** Wins in CoThinker at about 20x the tokens (a20, c24); a single agent matches or beats five designs at equal thinking tokens in multi-hop QA (d10). Contested.

### 5.3 Moderators

| Moderator | Effect | Source |
|---|---|---|
| Task type | Memory 90%/90%; arithmetic 90%/65%; heart on word tasks 0% | b07 |
| Prior knowledge | Two-factor at low knowledge, three-factor at higher | d12 |
| Item type | Perceived difficulty tracks item difficulty at r=-.80 (open) vs -.45 (multiple choice) | b10 |
| Item difficulty and scale | Numeric scales for hard items, pictorial for easy | a05, d13 |
| Scale points | 9-point and odd-point best; even-point worse | b02, b25 |
| Secondary-task contiguity | Effect appears only if non-contiguous | b14 |
| Model capability | Token-error slope shrinks with capability (-3.16 to -0.81 per 1000 tokens) | d06 |
| Reasoning budget | Probe quality degrades as reasoning effort rises (.58 to .40) | d01 |
| Baseline competence | Models at the floor show no load effect | c03, c15 |
| Task length | Strongest LLM stressor; distractor ratio non-monotonic | a16, a17 |

### 5.4 Interventions that worked and did not

Worked, with caveats: the ignore-irrelevant line (GSM-IC; DNR Bench for R1 and Claude-3.7); self-consistency on distractor problems (GSM-IC, old models); selecting by failed-step fraction (+10% on AIME, d05); removing failed branches (up to 12% in one math setting, d05); probe-based routing (about 70% lower cost, d02); CLAI-style budgets (35% fewer tokens, one unreplicated preprint, c06).

Did not work or backfired: the same instruction line on o3-mini-high (.00 to .04) and on the "indifferent" category (Claude .80 to .04, d08); reasoning-budget settings against over-reasoning (d09); multi-agent coordination on low-load instruction following (81.8 vs 84.4; Flash-8B 68.1 vs 84.3, c23); the effort dial for alignment (b16); verbalised pre-solve confidence (d04).

## 6. Language models

### 6.1 How models behave on load tests

- **Distractors.** In 2022-era models fewer than 30% of base problems survived any distractor (GSM-IC, c09). In 2025 models the drop is milder but present: Gemini-2.0-Flash .85 to .72 at 80% junk (ICE, c01). In CogniLoad, o3, gemini-2.5-pro and gemini-2.5-flash are indifferent to distractor ratio, while Phi-4-reasoning-plus and EXAONE-Deep-32B fall (a18, c14). Direction differs by model, so no single linear rule applies (K13).
- **Length.** Task length N is the strongest limit. Steepest fall N=20 to 50; at N=250 only gpt-5 (.76) and o3 (.68) exceed .50 (c13). Failure type changes: state-tracking errors under length (Qwen3-32B 2,541 at N=250), context overflow or format breaks for small models (gemini-2.5-flash 280/350, c16).
- **Intrinsic difficulty.** Top models degrade slightly d=1 to 3 (o3 .96 to .93; gpt-5 1.00 to .97), then by d=5 12 of 22 are below 50% (a16, c15).
- **Floor.** Weak models give 0% in every ICE condition, so the load effect is invisible (c03).
- **Position and turns.** Middle placement and multi-turn spread both cost accuracy (c18, c19; abstract only).

### 6.2 Tokens as a load measure

- Tokens track human time: GPT-OSS rho .24 to .91 within task (b16), DeepSeek-R1 mean .57 (b17), averaging sampled paths raises .41 to .55 (b23, snippet). In a real labelling task the overall link is weak (r .15 to .19; elasticity 0.09% to 0.28%) but top-quintile items took humans 26 to 39% longer (b18).
- Tokens carry error information: within an item, longer reasoning goes with lower accuracy, with the slope shrinking as models get stronger (d05, d06). Failed-step fraction beats length (d05).
- Tokens are not monotone in difficulty. Reasoning effort rises then falls with complexity before collapse (c21, abstract), and models overthink easy items (d09, c20).
- The effort setting caps tokens but did not change alignment (b16).
- Distillation lowers alignment (rho .64 to .34, b17), so alignment is model-specific.

### 6.3 What changed the numbers

| Change | Effect | Source |
|---|---|---|
| Ignore-irrelevant line | R1 redundant .00 to .76; Claude-3.7 .40 to 1.00; o3-mini-high no change; hurt Claude on "indifferent" (.80 to .04) | d08 |
| Self-consistency, 20 samples | about +11 points micro on GSM-IC (old models) | c10 |
| Select by failed-step fraction | up to +10% AIME | d05 |
| Probe routing | same accuracy, about 70% lower cost | d02 |
| CLAI prompt | -36% tokens at -0.2 points (GSM8K), single author | c06 |
| Multi-agent split | +5.3 points LiveBench Math at about 20x tokens; -2.6 instruction following | c23, c24 |
| Tight 8,192-token cap with structure | Gemini-2.5 Reasoning 69.2 vs 31.0 | c25 |
| Equal thinking tokens | single agent matches or beats multi-agent | d10 |
| More reasoning effort | o3-mini high vs medium: over 2x tokens for about +4% accuracy | d06 |

### 6.4 What is missing

No paper tests a 1 to 9 difficulty rating by the model before solving against correctness and tokens (d17, GAP 1). No replication of CogniLoad on another benchmark (GAP 6). No test of context pruning plus an ignore line on distractor sets for current reasoning models (GAP 2; DNR Bench partial). No LLM evidence on whether a germane-token budget is separable from intrinsic load (GAP 9). ICE, CLAI and CoThinker pilots are single-author or pilots only (K24, K16). Human-user studies of LLM tools that use NASA-TLX (a21, c27 to c29) measure the human, not the model.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = SCHEMA section 5. Evidence ids refer to evidence_a-d.jsonl.

### Add now (established)

1. **Log output tokens per item as the load proxy, with accuracy beside it.** Part: G12 and the run log (SCHEMA section 6). [E]. Evidence b16, b17, b18, d05, d06, d09 (K09, K25). G12 already says spend by difficulty; this says what to log and why: tokens carry both time-like cost and error information.
2. **Do not trust any single proxy; calibrate per task family.** Part: G7 and the log. [E]. Evidence b05 to b07, b10 (K01, K08). No global load threshold.
3. **Do not add a three-score (intrinsic, extraneous, germane) self-rating step.** Part: SCHEMA 4b. [E] that three-score ratings do not separate cleanly (b01 to b04, K02); [C] on whether germane load exists (b08, d12, K03). The schema already avoids it; keep it out.
4. **Do not use the agent's own verbal confidence or self-rated difficulty as a stop or gate signal without a behavioural check.** Part: G1 and 4b (verbal confidence). [E] for the human analogue (b11, b12, K06); [S] for LLMs (d04, K27). Reinforces 4b.
5. **Test load effects only on items where clean plain accuracy is 30 to 90%.** Part: G7 (test design). [E] (c03, a16, K15).
6. **Think briefly; cap tokens per mode; expect longer chains to be worse within an item.** Part: G11, G12. [E] (d05, d06, d09, c20, K19, K25). Already in the schema; adds a measured slope (-0.81 to -3.16 points per +1000 tokens) as a sanity check, not a rule.
7. **Efficiency ledger: (z accuracy minus z tokens) / sqrt 2 next to raw accuracy in every test.** Part: G7. [S] for the human formula (a14, K23), but it is only an accounting choice, so adopting it costs nothing.
8. **Restate the task in one clean message rather than rely on a long dialogue.** Part: S1. [E] on position and multi-turn effects (c18, c19; abstract-page evidence). S1 and fresh context per attempt already do this.

### Test first

| # | Candidate | Part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | Pre-solve 1 to 9 difficulty rating by the model as an S0 gate signal | S0 | [S] | d04, d03, d17 (K27) | No paper; pre-solve confidence is weak (AUROC .50 to .77). Must beat the token baseline |
| T2 | Token or failed-branch count as a re-plan trigger at S6 (per-model threshold) | G1, S6 | [E] direction, [S] threshold | d05, d06 (K25) | Correlational; threshold fitted per model |
| T3 | "Ignore irrelevant information" line plus context filter in S1 input hygiene | S1, G2 | [S] | c10, d08 (K12, K14) | Old models; backfires on some; pruning never tested |
| T4 | Decompose long tasks into fixed-size subtasks (O3) instead of one long chain | O3 | [S] | a16, c13 (K11) | One benchmark; equal-token test missing |
| T5 | Short-budget plan-then-solve prompt (CLAI-like) | G11, S0 | [S] | c06 (K16) | Unreplicated preprint, baseline mismatch |
| T6 | Multi-agent or specialist split | O3 | [C] | c23, c24, d10 (K17, K18) | Equal-token result negative; G9 already blocks debate |
| T7 | Output-side stand-in for probes (abandoned-branch share, answer instability) | S0, S6 | [S] | d01, d05 (K26) | Probes beat length; output stand-ins untested |
| T8 | A separate germane-token budget | budget | [C] | b08, d12 (K03) | No LLM evidence; likely indistinguishable from intrinsic |
| T9 | Probe at three distractor ratios before fitting any linear load model | S0 | [S] | a17 (K13) | One benchmark |

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (setup counted, per G7). Metric defaults to accuracy and accuracy per token. Use items where clean plain accuracy is 30 to 90%.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1. Pre-solve rating as predictor | Mixed-difficulty set with known answers (ARC subset, brainteasers, GSM-style), at least 200 items | Same model, same items: (a) rate difficulty 1 to 9, then solve; (b) solve only, log tokens | AUROC of rating vs correctness; AUROC of tokens vs correctness; Spearman rating vs tokens; rating cost in tokens | Rating AUROC at best .6 to .7, below tokens (K27: pre-solve .50 to .77); it earns a place only if it adds to tokens |
| B2. Token-error slope | Same items, 8 samples each at free length | Plain model, no intervention | Within-item slope of error on tokens (item fixed effect); failed-branch share | Negative slope about 1 to 3 points per 1000 tokens (d06); failed-branch share predicts better than length (d05) |
| B3. Re-plan trigger | Distractor-free and distractor-augmented sets | (a) single attempt with cap; (b) same cap but restart at a fitted token or failed-branch threshold (abandoned tokens count) | Accuracy at equal total tokens | Small gain on hard items, none or loss on easy. Reject if gain under 2 points |
| B4. Ignore line and pruning | Distractor-augmented set (GSM-IC style; ICE-style junk at 0, 20, 50, 80%) plus its clean twin | (a) plain; (b) plain plus ignore line; (c) ignore line plus code pruning of marked irrelevant sentences | Accuracy on distractor set; accuracy on clean twin (must not fall) | Gain for models like R1 (.00 to .76 in DNR), none for models already indifferent (o3-like); watch clean regressions |
| B5. Three distractor ratios | Synthetic state-tracking or QA with ratio 0, 25, 50, 90% | Plain model | Accuracy by ratio | Non-monotonic curve for some models (K13); do not fit a line |
| B6. Fixed-size decomposition | Long tasks (N from 20 to 250 statements) | (a) one chain; (b) decomposed into fixed-size chunks with code carrying state | Accuracy by N | Gain grows with N where plain accuracy is below .5; none at small N |
| B7. Token cap sweep | Same items | Structured scaffold vs plain at caps 1k, 2k, 4k, 8k | Gap vs cap | Gap shrinks as cap grows if the tight-cap win is a budget artifact (c25 vs d10) |
| B8. Efficiency ledger | Every test above | Both arms | (z acc - z tokens) / sqrt 2 | Reported next to raw accuracy so no arm wins by spending |
| B9. Resolution of the agent's effort rating | 10 or more items per run, several runs | Agent rates effort after solving; compare per-run correlation with tokens | Within-run correlation (resolution), averaged | Modest, cue-based correlation; the rating adds little beyond tokens (b13 shape, K06) |

## 9. What does not transfer, and why

- **Physiology (eye, heart, skin, brain).** Models have no body. Ayres' counts (b05 to b07) are not usable. Analogues (attention entropy, logit entropy, probes) are pilots or need hidden states (c24, d01 to d03). Perplexity moved the wrong way in a pilot (c24).
- **Dual-task.** No separate pool inside a model. A distractor in the same context is the nearest thing and is already covered by ICE and CogniLoad.
- **NASA-TLX subscales and pairwise weighting.** Physical demand, frustration and temporal pressure do not apply to a model, and no person weights them. K05 and K28 are not testable on an LLM.
- **Three-way load split.** Human ratings fail to separate the three types (b03, b08, d12), and there is no verified way to say which agent tokens are germane. Mapping task length to germane load is an analogy the authors state (c12).
- **Human reaction time as ground truth.** Human time includes reading and motor time, and token-to-time correlations are low in a real task (r .15 to .19, b18). It says little about whether the answer is right.
- **University-student multimedia findings.** 53 articles, N=7413, mostly students (b01). Item wording, scale preferences and prior-knowledge effects (d12) may not carry to a model.
- **CLT multi-agent designs.** CoThinker's gains arrive at about 20x tokens (c24); at equal thinking tokens a single agent matches or beats five designs on multi-hop QA (d10). G9 already covers this.
- **Prompt remedies tested on 2022 models.** GSM-IC numbers (c09, c10) do not describe current reasoning models.

## 10. Open questions

1. Does an LLM's own 1 to 9 pre-solve difficulty rating predict correctness and token use, and does it add to tokens at the same budget? (GAP 1, no paper.)
2. At equal tokens, does an ignore-irrelevant line plus context pruning help current reasoning models on distractor tasks? (GAP 2; DNR Bench partial.)
3. Does token cost predict error beyond math and science, across families? (K25 covers math and science.)
4. What do Hart and Staveland (1988) report for reliability and sensitivity, and what are DeLeeuw and Mayer's (2008) correlations and samples? Both unread (GAP 4).
5. What did Skulmowski and Rey (2020) report, and is there a measured lab-to-field gap anywhere? (GAP 5.)
6. Does CogniLoad's "task length dominates" replicate, and does fixed-size decomposition recover accuracy at equal tokens? (GAP 6.)
7. Do CLT-inspired structures survive equal-token tests on math and instruction following? Only multi-hop QA is tested (GAP 7).
8. Is there a text-only signal (logit entropy, attention entropy, branch failure) that beats token count? Probes do, but need hidden states (GAP 8).
9. Is a germane-token budget ever separable from intrinsic load for LLM agents? (GAP 9.)
10. Does the Eysink negative GCL-learning correlation replicate, and do effort ratings predict later learning when confidence is controlled? (GAP 10; Minkley gives only effort beta +.309.)
11. Do the Ayres counts hold when effect sizes are pooled? Do EEG sub-measures with 0% match (beta) need separate treatment?
12. Why does the distractor response differ in direction between models (gemini-2.5-flash-lite .38 to .53 versus EXAONE-Deep .47 to .32)?

## 11. Sources

[V] = opened and read this session (full text or substantive page). [M] = snippet, abstract page only, or second-hand.

- [M] Hart and Staveland (1988), Development of NASA-TLX. https://doi.org/10.1016/S0166-4115(08)62386-9 (a01, a25; chapter not read)
- [V] Hart and Staveland, NASA TLX v1.0 computerized manual. https://ntrs.nasa.gov/citations/20000021487 (d14)
- [V] Pahr and Di Bartolomeo (2025), Investigating the Task Load in Visualization Studies. https://arxiv.org/pdf/2509.24643v1 (a02, a03, a22)
- [V] Ouwehand, van der Kroef, Wong and Paas (2021), Measuring Cognitive Load: Are There More Valid Alternatives to Likert Rating Scales? https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.702616/pdf (a04, a05, a23, d13)
- [V] Klepsch, Schmitz and Seufert (2017). https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01997/pdf (a06, a07)
- [M] Leppink et al. (2013). https://link.springer.com/article/10.3758/s13428-013-0334-1 (a08, abstract page)
- [M] Korbach, Brunken and Park (2018). https://link.springer.com/article/10.1007/s10648-017-9404-8 (a09, abstract page)
- [M] DeLeeuw and Mayer (2008). https://doi.org/10.1037/0022-0663.100.1.223 (a10, second-hand)
- [V] FLoRA Replication Atlas record for DeLeeuw and Mayer (2008). https://forrt.org/flora-replication-atlas/doi/10.1037/0022-0663.100.1.223/ (a11, d16)
- [M] Skulmowski and Rey (2020). https://doi.org/10.1002/hbe2.202 (a12, second-hand)
- [V] Skulmowski and Xu (2022). https://link.springer.com/article/10.1007/s10648-021-09624-7 (a13)
- [M] Paas and van Merrienboer (1993). https://doi.org/10.1177/001872089303500412 (a14)
- [M] Paas (1992). https://doi.org/10.1037/0022-0663.84.4.429 (a15)
- [M] Zu et al. (2020). https://psycnet.apa.org/record/2020-27033-001 (a24)
- [V] Kaiser et al. (2025), CogniLoad. https://arxiv.org/abs/2509.18458 (a16 to a19, c12 to c16)
- [V] Zhou/Shang et al. (2025/2026), CoThinker. https://arxiv.org/abs/2506.06843 (a20, c23 to c25; one paper)
- [V] Figliola et al. (2026). https://arxiv.org/pdf/2605.31287 (a21)
- [V] Krieglstein et al. (2022). https://doi.org/10.1007/s10648-022-09683-4 (b01 to b04, b25)
- [V] Ayres, Lee, Paas and van Merrienboer (2021). https://doi.org/10.3389/fpsyg.2021.702538 (b05 to b07)
- [V] Jiang and Kalyuga (2020). https://doi.org/10.20982/tqmp.16.3.p216 (b08, b09)
- [V] Schuessler et al. (2024). https://doi.org/10.1007/s11251-024-09692-6 (b10)
- [V] David et al. (2024). https://doi.org/10.1007/s10648-024-09903-z (b11, b24)
- [V] Scheiter, Ackerman and Hoogerheide (2020). https://doi.org/10.1007/s10648-020-09555-9 (b12, b13)
- [V] Schoor, Bannert and Brunken (2012). https://doi.org/10.1007/s11423-012-9251-8 (b14)
- [V] Esmaeili Bijarsari (2021). https://doi.org/10.3389/fpsyg.2021.648586 (b15)
- [V] Hu and Wang (2026). https://arxiv.org/abs/2605.16938 (b16, b17)
- [V] Davidson (2025). https://arxiv.org/abs/2508.20262 (b18, b19)
- [M] Hughes et al. (2019). https://doi.org/10.1177/0018720819830553 (b20, abstract)
- [M] Usability-testing cognitive load review (2026). https://doi.org/10.1177/00187208261427867 (b21, abstract)
- [M] Human-user LLM tool studies with NASA-TLX and EEG. https://arxiv.org/pdf/2608.01366 (b22, snippet, attribution unverified)
- [M] Thinking effort in abductive reasoning. https://arxiv.org/pdf/2609.01867 (b23, snippet)
- [V] Adapala (2025), ICE. https://arxiv.org/abs/2509.19517 (c01 to c04)
- [V] Zhang (2025), CLAI. https://arxiv.org/abs/2507.00653 (c05 to c08)
- [V] Shi et al. (2023), GSM-IC. https://arxiv.org/abs/2302.00093 (c09 to c11)
- [M] Upadhayay et al. (2024). https://arxiv.org/abs/2410.11272 (c17, abstract)
- [M] Laban et al. (2025). https://arxiv.org/abs/2505.06120 (c18, abstract)
- [M] Liu et al. (2023). https://arxiv.org/abs/2307.03172 (c19, abstract)
- [M] Chen et al. (2024). https://arxiv.org/abs/2412.21187 (c20, abstract)
- [M] Shojaee et al. (2025). https://arxiv.org/abs/2506.06941 (c21, abstract)
- [M] Scaling Competence, Shrinking Reasoning. https://arxiv.org/abs/2511.21743 (c22, abstract)
- [M] ToolLoad-Bench. https://arxiv.org/abs/2601.20412 (c26, abstract)
- [M] RecalibrateGPT. https://arxiv.org/abs/2609.00506 (c27, abstract)
- [M] GuideAI. https://arxiv.org/abs/2601.20402 (c28, abstract)
- [M] Kosmyna et al. (2025). https://arxiv.org/abs/2506.08872 (c29, abstract)
- [M] Epistemic debt and metacognitive scripts (2026). https://arxiv.org/abs/2602.20206 (c30, abstract)
- [M] arXiv listing search, cognitive load + language model + NASA-TLX. https://arxiv.org/search/?query=%22cognitive+load%22+%22language+model%22+NASA-TLX&searchtype=all (c31)
- [V] Lugoloobi et al. (2026). https://arxiv.org/abs/2602.09924 (d01, d02; some table rows garbled)
- [V] Cencerrado, Pacchiardi et al. (2026). https://arxiv.org/abs/2509.10625 (d03)
- [V] Kale (2026). https://arxiv.org/abs/2607.07626 (d04; row mapping partly ambiguous)
- [V] Feng et al. (2025). https://arxiv.org/abs/2509.19284 (d05)
- [V] Ballon, Algaba, Ginis (2026). https://arxiv.org/abs/2502.15631 (d06)
- [M] Su et al. (2025). https://arxiv.org/abs/2505.00127 (d07, abstract and introduction)
- [V] Bamgbose et al. (2026), DNR Bench. https://ojs.aaai.org/index.php/AAAI/article/view/41055 (d08, d09)
- [V] Tran and Kiela (2026). https://arxiv.org/abs/2604.02460 (d10; table headers partly garbled)
- [V] Minkley, Xu, Krell (2021). https://www.frontiersin.org/articles/10.3389/feduc.2021.632907 (d11)
- [V] Zu, Munsell, Rebello (2021). https://www.frontiersin.org/articles/10.3389/feduc.2021.647097 (d12)
- [V] Skulmowski and Rey (2017). https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01191 (d15)
- [M] Search outcome for GAP 1 and GAP 6, null result. https://arxiv.org/abs/2602.09924 (d17)
