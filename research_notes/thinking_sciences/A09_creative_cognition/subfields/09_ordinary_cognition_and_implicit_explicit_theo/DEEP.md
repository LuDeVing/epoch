# Ordinary-cognition and implicit-explicit theories: deep document

*Subfield A09.09. Sources: evidence_a-d.jsonl (ids a01-a29, b01-b26, c01-c26, d01-d16), claims.jsonl (A09.09-K01 to K27), critique.md. Honest scope note: no LLM test of the Explicit-Implicit Interaction theory (EII) or of honing theory exists in what we found. The LLM section is built from nearby studies.*

## 1. What it is

Two questions sit under this subfield.

1. **Is creativity a special process or ordinary thinking?** The "ordinary-cognition" view (Weisberg; Fleck and Weisberg) says insight and creative leaps come from normal perception, memory, analogy and step-by-step reasoning. The rival "special-process" view says insight needs something extra: a sudden restructuring, an unconscious stage, or an impasse followed by a flash.
2. **How do explicit (rule-based, verbal, conscious) and implicit (associative, hidden) processes work together?** Helie and Sun's EII theory says both run all the time, hold redundant knowledge, and are integrated iteratively. Insight is the moment an implicit result becomes confident enough to become explicit.

A third theory, Gabora's **honing theory**, rejects "generate many discrete candidates, then select". It says an idea starts as a merged, half-formed state and is reshaped by new contexts until it settles.

Why it matters for our agent. The agent is a scaffold around a language model. The design question is whether creative or insight-type problems need a special stage (a pause, an "incubation" gap, a hidden process) or whether engineered variation plus a code-side check is enough. The evidence mostly says: no hidden stage, yes to engineered variation and external checking. That supports the schema's existing split (S3 generate in fresh contexts, S4 and S7 selection by code) and gives specific guards on where written reasoning hurts.

## 2. History and theories in depth

**Wallas (1926) four stages.** Preparation, incubation, illumination, verification. Special-process theories treat incubation as hidden unconscious work. Ordinary-process theories treat it as a fresh restart, forgetting of a wrong approach, or luck of cues.

**Special-process lines.** Gestalt restructuring. Schooler, Ohlsson and Brooks (1993) claimed that verbalising hurts insight problems but not analytic ones, which would show insight rests on non-verbal processes. Kershaw and Ohlsson (a22) showed nine-dot difficulty comes from prior-knowledge constraints (do not turn on non-dot points, do not cross lines, stay inside the figure).

**Ordinary-process line (Weisberg).** Weisberg and Alba (1981) argued fixation is not the key obstacle in the nine-dot problem (figures second-hand, a23). Fleck and Weisberg (2004, b01-b03) ran the candle problem with verbal protocols. Fleck and Weisberg (2013, b19, snippet only) used five insight problems and concluded that insight and analysis are ends of a set of methods. Weisberg (2015, a18/b18, not read) proposed an integrated "business as usual" account: insight comes mainly from conscious analytic operations, restructuring is a feature, and unconscious processes enter only after an impasse. Impasse is not required.

**Smith, Ward and Finke (1995, b12).** Named the paradox: insight, incubation and activation of distant elements also appear in non-creative tasks. Verbalisation hurts insight problems but also face recognition, so it is not unique to creativity.

**Explicit-Implicit Interaction (Helie and Sun 2010, a01-a06, b09).** Five core principles: (1) explicit and implicit knowledge co-exist and differ; (2) most tasks use both; (3) they hold redundant representations; (4) their outputs are integrated; (5) processing is iterative and may run both ways. Wallas mapping: preparation and verification are mostly explicit, incubation mostly implicit, insight is an "explicitation" step. It is built in the CLARION architecture (a02): a top level of explicit rules and a bottom level of a neural network that settles to soft constraints. Search is Darwin-like: noisy implicit variation, selection against an internal confidence level (ICL), retention. A Bayes-factor version (a09) decides when an association is confident enough to output (BF under 3.2 not worth mentioning, over 10 strong, over 100 decisive). Helie and Sun treat blind-variation-selective-retention (BVSR) as compatible (a29).

**Honing theory (Gabora 2017, a11, b10).** Creativity begins when the mind meets high "psychological entropy" material. The mind re-views it from new contexts until it restructures and arousal drops. The idea is in a "state of potentiality" (a merge of sources), not a list of candidates. A 2019 position paper (a14, b11) recasts convergent and divergent thought as the same process viewed from conventional or unconventional contexts, with associative and analytic modes both used throughout. Gabora's EVOC toy model (a15) found best cultural fitness at about 2 inventors to 1 imitator.

**Theory conflict.** Honing theory and EII disagree on whether variation-selection is the right frame (a02). Simonton's reformulated BVSR (2012) allows "sighted" variation, which Gabora says is no longer clearly Darwinian (a29). No neutral review was opened.

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree; single = one source; contested = sources disagree.

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Incubation helps people a little | 117 studies, 3,606 participants. Unweighted d 0.41 (SD 0.71); weighted random-effects d 0.29 (CI 0.21-0.39). Q=173.99, df=113. 85 studies positive. No funnel-plot bias found | Sio and Ormerod 2009 (b04) | Established |
| Incubation gain depends on the gap task | Divergent tasks gain more than linguistic or visual insight tasks. Longer preparation helps. A demanding break task shrinks the effect. For linguistic insight a low-demand task beat plain rest | b05, b26 | Established (subgroup numbers not extracted) |
| Review of 39 incubation experiments | 29 found a significant effect; misleading clues in the break harm | Dodds, Ward, Smith 2003 via a07/a08 | Second-hand |
| Distractor task effect on free-recall reminiscence | N=114, six groups of 19. Do Nothing 7.26; No Incubation 4.9; Remote Association 4.84; Perceptual-Motor 4.84; Syllogistic 2.47; Dynamic Control 2.26. F(5,108)=10.65, p<.001 | Helie, Sun, Xiong 2008/2010 (a07, c01) | Single (memory task, not insight) |
| Reminiscence rises with break length | 2.90, 3.15, 3.72, 5.00 items at 0, 1, 5, 10 min; F(3,209)=9.4. Test length no effect (F=.27) | a04 | Single, old data fit by model |
| Priming after a near-miss recall | 44 participants; correct trials t(2100)=8.5; incorrect t(2100)=0.7 n.s. Model reproduced it | a03 | Old data re-analysed |
| Unconscious thought has no real advantage | 61 effect sizes. g=0.15 (CI 0.03-0.26) falls to 0.018 (CI -0.10 to 0.14) after trim-and-fill. Replication N=399: 58.2% deliberation vs 61.9% distraction, n.s. | Nieuwenstein et al. 2015 (b06) | Established (choice tasks) |
| Verbalising and the coin problem | 82 participants: 45.8% solved after unrelated task vs 35.6% after verbalising, t(74)=2.13, p<.05. Model 45.3% vs 35.3% (5000 runs). Data are from Schooler 1993, re-used as a model fit | a05 | Contested |
| Verbalising and the candle problem | N=58. Box solution 8/34 (23.5%) verbalisers vs 5/18 (27.7%) silent, chi2=0.113, p=.736. Time 5.97 vs 5.32 min | Fleck and Weisberg 2004 (b01) | Single, no cost found |
| Verbal overshadowing, tighter replication | Insight 57% vs 53% (verbal vs silent), non-insight 48% vs 48%. Bayes factor 0.92 (insensitive). Original (second-hand): insight cost 25 points vs 5 for non-insight | Gilhooly et al. 2010; Schooler et al. 1993, via d01 | Contested |
| Verbal overshadowing for faces | Registered multi-lab replication confirmed it (effect size not read) | Alogna et al. 2014 (b20, b21) | Established, narrow |
| Impasse is not needed for insight | 15 of 34 protocols (44%) showed impasse. Box solution 1/15 (7%) with impasse vs 7/19 (37%) without. chi2(1,N=34)=4.242, p=.039, phi=.35. About 75% of first solutions were not the box | Fleck and Weisberg 2004 (b02); Stuyck et al. 2021 (b08) | Established |
| Insight tied to verbal working memory | N=53. Solved 42% of 60 items; 64% of solved rated partly or fully insight. Verbal WM beta=.40, t=2.25, p=.03. Insight solutions faster than analytic | Chein and Weisberg 2014 (a19) | Contested |
| Insight solutions immune to WM load | N=106, 70 puzzles. Insight accuracy 94% vs 77% (d=-1.57). Non-insight correct 15.8 (no load) vs 7.9 (high load), d=0.66; insight no difference | Stuyck et al. 2022 (a20, b07) | Contested (high-load data trimmed 25%) |
| Fast first answers are mostly final | Two experiments, 100 each, 24 items. Initial accuracy 48.3% and 49.8%; final 65.2% and 66.7%; d=0.35. 72.7% and 71.4% of correct finals were already correct at first response | Beucler and De Neys 2026 (a24) | Single |
| Nine-dot training | N=90. Relaxing constraints: 19/30 (63%) solved the first insight problem; hindering 8/30 (27%); none 11/30 (37%); chi2(2)=8.836 | Kershaw and Ohlsson 2001 (a22) | Single |
| Honing vs search-select responses (art) | 56 artists, 11 judges. 29 honing vs 13 search-select, chi2(1,N=43)=4.57, p<.05 | Carbert et al. 2014 (a13) | Single lab, weak |
| Honing responses in analogy problem | Honing responses significantly more frequent than structure-mapping; N and statistics not available | Gabora and Saab 2011 via a12 | Single, second-hand |
| LLM: chain of thought hurts implicit-type tasks | Artificial grammar GPT-4o 87.5 to 64.4 (-23.1). Claude 3 Opus -8.0, Gemini 1.5 Pro -6.05, Llama 3.1 70B -8.8, Claude 3.5 Sonnet 65.9 to 67.7 (+1.8, n.s.). o1-preview 57.7% vs GPT-4o zero-shot 94.0% on a subset is a cross-model contrast, not CoT on/off | Liu et al. 2025 (c04, c20; critique correction 1) | Established |
| LLM: CoT helps where verbal reasoning helps | Logical-inconsistency task GPT-4o 53.2 to 93.9; Llama 3.1 70B 55.6 to 81.6; Claude 3 Opus fell 62.7 to 58.8 | c20 | Single |
| CoT gain by task class | Symbolic +14.2, math +12.3, logic +6.9 points; other categories about +0.7 (56.8 vs 56.1) | Sprague et al. 2024 (d10) | Established |
| Longer reasoning can hurt | Inverse scaling on distractor, spurious-feature and constraint tasks; failure modes differ by model family | Gema et al. 2025 (d11) | Single (abstract-level read) |
| LLM insight riddles | 201 riddles, 38 models. Non-reasoning 7.6%, reasoning 17.6%, humans 52.9%. Welch t(24.1)=2.98, p=.0066, d=0.946. Grok-4 37.6%, Claude Opus 4 30.3%. Right answers often in thought logs but not endorsed | Mizumoto et al. 2025 (a27, b13, d14) | Single |
| LLM versus human on creativity tests | 100 humans vs 100 instances per model. AUT novelty higher for models (t=5.32, 5.10, 8.89); appropriateness lower for GPT-3.5 (t=-3.37) and GPT-4 (t=-4.60). Humans beat models on representational change by 0.46 (GPT-4-turbo) and 0.31 (GPT-4o), p<.001 | Zhang et al. 2025 (a25, c05-c07) | Established (older models) |
| DAT | GPT-4 greedy 89.1, above 96.1% of humans; GPT-3.5 80.8 above human average | Chen and Ding 2023 (c08) | Single |
| LLM homogeneity | 26,070 open queries; 42 models; mean within-prompt similarity 0.821; under min-p 81% of pairs above 0.7 and 61.2% above 0.8 | Jiang et al. 2025 (b15) | Established (3 sources) |
| Population variability | 22 LLMs vs 102 humans; LLM variability lower on all three tests | Wenger and Kenett 2025 (c09) | Established |
| Temperature is a weak dial | Novelty coefficient 0.308 (SE .138); coherence 0.240 (SE .122, less coherent when hot); perplexity vs novelty 0.730 | Peeperkorn et al. 2024 (b16); c08 | Established |
| Idea diversity operators | Humans 28 categories, 208 combinations; default GPT-4o 23 and 85-89; persona plus CoT raised combinations to about 240 | Deng et al. 2026 (d02) | Single, one domain |
| Verbalized sampling | Diversity 1.6 to 2.1 times over direct prompt; human rating +25.7%; recovers 66.8% of base-model diversity | Zhang et al. 2025 (d03) | Single (own metrics) |
| NoveltyBench | Many leading models give fewer than 3 distinct answers in 10 samples; in-context regeneration strongest simple operator; paraphrase and temperature weak | Zhang et al. 2025 (d05) | Single |
| Two-stage "explore then satisfy" prompt | Qwen3-235B, K=50: about 13 distinct tasks vs about 8 for CoT and base; CoT = base | Nguyen et al. 2026 (d04) | Single |
| Overgenerate, dedup, rank | Novelty 4.84 (human), 5.64 (AI), 5.81 (AI plus human rerank); 49 ideas per condition; 4000 seeds per topic, about 5% non-duplicate at 0.8 similarity; feasibility coefficient -0.330 | Si et al. 2024 (c10) | Established |
| Cross-domain cues | 140 humans, 7 LLMs, 2,800 ideas, 1,002 raters. Human originality 2.93 (cue) vs 2.57; o3 3.83, Claude-Sonnet-4 3.76, Llama-3.3-70b 3.02. LLMs gained nothing on average; only top two on distant sources | Liu et al. 2026 (c11) | Single |
| MacGyver | Humans 79.3% vs GPT-4 73.3%; divergent-convergent prompt +6.5% efficiency; self-reflection cut infeasible solutions 9.7% | Tian et al. 2024 (c03) | Single |
| Spontaneous "aha" in LLM traces | Shifts in 6.31% of traces; accuracy 2.57% shifted vs 16.44% not (N=723,200). Forced reconsideration at high entropy: MATH-500 0.322 to 0.406 (+8.41 pp); crosswords +0.45 pp; Rush Hour +0.01 pp | d'Aliberti and Ribeiro 2026 (b14, b25; critique correction 2) | Single (small tuned models) |
| First sample already correct | First solution round correct in more than 92% of cases (QwQ-32B, R1 on ASDIV, MATH500); first round under 60% of tokens | Chen et al. 2024 (d06) | Single (math) |
| Wrong early turns persist | Average 39% drop from single- to multi-turn; recap recovers only 15-20% | Laban et al. 2025 (d07) | Single |
| Sampling plus verifier | SWE-bench Lite: 15.9% at 1 sample to 56% at 250; voting and reward models plateau after a few hundred | Brown et al. 2024 (d09) | Established with d08 |
| Compute allocation | Compute-optimal mix beats best-of-N with about 4x less compute; sequential wins on easy, parallel on hard | Snell et al. 2024 (d08) | Established |
| Reasoning distillation and brain alignment | DMN alignment vs model size r=0.58; vs AUT score r=0.51; reasoning-distilled Llama-8B negative | Ismayilzada et al. 2026 (c14) | Contested, one lab |
| Semantic networks in ChatGPT-4o | 81 vs 81. Fluency 43.8 vs 19.1 (high-creative) vs 12.2; shortest path 4.378 vs 3.325 vs 3.429 | Domanti et al. 2026 (c13) | Single |

## 4. Mechanisms and models

### 4.1 EII loop (implementable form)
State: a problem, an explicit rule store, an implicit associative generator, a confidence level.
1. **Explicit pass.** Apply known rules. The result is stereotyped. If a rule passes the check, stop.
2. **Implicit pass.** Draw many associations from the generator with noise. Noise is a parameter: higher early, lower to refocus (a02 uses a Boltzmann temperature).
3. **Integrate.** Compare implicit and explicit outputs. Score each with a confidence value.
4. **Threshold.** If confidence is above a set level (or a Bayes factor above a set value, a09), the implicit item is "explicitated": it becomes a candidate the explicit side checks. If not, loop with changed noise or new input.
5. **Verify.** The explicit side tests the candidate (Wallas verification).

Mapping to our schema: the implicit generator is S3 (cheap wide sampling in fresh contexts). Explicit pass and verify are S4, S7, S8, done by code. The confidence threshold is the part the schema lacks as a formal rule. The EII distractor result (a07, c01) predicts that a break only helps if it does not use the same resource. A language model has no hidden process between calls, so the only analogue is changing what is in the context.

### 4.2 Variation-selection (Darwin-like) view
Variation is blind or soft-guided; selection compares to a criterion; retention keeps the winner. For an LLM: sample N, dedup, check, keep. Si et al. (c10) is a direct instance. Weak points: dedup leaves about 5% of 4000 ideas, and LLM ranking of ideas is unreliable.

### 4.3 Honing view
Keep a single blended draft and re-view it under different framings, instead of listing discrete candidates. Implementable as: draft, then N re-readings under distinct framings (each a fresh context given the draft and one framing), then merge. No LLM evidence. Human evidence is judged self-report from one lab (a12, a13).

### 4.4 Business-as-usual view
Insight is the visible end of a stepwise search with restructuring operators. For an agent: the reframe operators (O6, O8) are available at any state, not only after a stall (K05). Log restructurings and impasses as events; do not treat them as a stage.

### 4.5 Fast first answer plus slow check
Beucler and De Neys (a24): most correct answers come fast; deliberation corrects few. Implementation: keep the first sample in the candidate pool; do not discard it for a later "reasoned" answer unless the check prefers the later one.

### 4.6 Trigger for reframe
d'Aliberti (b25): code computes token entropy; in the top 20% highest-entropy items within a domain, force a reconsideration. Generalised: trigger on disagreement among samples or on high entropy, never on a schedule (consistent with G1).

## 5. What holds up

**Holds up well**
- Incubation helps people a little, d about 0.29 weighted, without clear publication bias (b04). Moderators: task type, preparation length, load of the break task.
- Unconscious-thought benefits for choice do not survive bias correction or a 399-person replication (b06).
- Impasse is not necessary for insight; restructuring also appears in non-insight solutions (b02, b08).
- Plain LLM sampling is homogeneous within and across models (b15, c09, d05; c24 snippet).
- Temperature is a weak lever (b16, c08, d05).
- CoT helps on math, symbolic and logic tasks, not elsewhere (d10).
- Overgenerate plus external selection beats single-pass on novelty (c10), and sampling plus a reliable verifier scales (d09). Without a verifier, voting plateaus.

**Failed or weak**
- Verbal overshadowing on insight: contested. Original 25 vs 5 point cost (second-hand); candle-problem null (b01); a tighter replication null with BF 0.92, insensitive (d01); critics cite a spatial/verbal confound and non-standard instructions (d15, snippet). Faces: replicated, but narrow.
- Mind wandering in incubation: mixed (c26, snippets only).
- Honing theory: one lab, small judged samples, p just under .05, no independent replication (a13, critique).
- EII: fits old human data; the one new prediction tested (distractor study, N=114) used free recall, not insight.
- Reasoning-model "aha" shifts: rare and linked with worse accuracy (b14).
- Cross-domain cues: help humans, not LLMs on average (c11).

**Contradictions left open**
- Insight and working memory: Chein and Weisberg (a19) find a link; Stuyck et al. (a20) find immunity to load. Stuyck's authors note the result also fits an integrated view.
- Models match humans on output tasks but not on process measures (c05-c07, c13).
- Reasoning helps riddles (b13, 17.6 vs 7.6) but hurts implicit-pattern tasks (c04).

**Interventions that worked (human)**: relaxing constraints before nine-dot (63% vs 27%, a22); a low-demand filler for linguistic insight (b05); useful clues during the break (a08, second-hand).
**Interventions that did not work**: distraction before choice (b06); heavy explicit distractors (a07: syllogistic 2.47 vs idle 7.26).

## 6. Language models

**Output versus process.** On output tests, current models match or beat students: AUT novelty, DAT, RAT (c05, c08). Appropriateness is lower for GPT-3.5 and GPT-4 but equal for GPT-4o (p=.163). On process tests they differ: association chains stay nearer the cue (c06), representational change is weak (humans +0.46 over GPT-4-turbo, +0.31 over GPT-4o), and ChatGPT-4o's semantic network is more rigid and fragmented (average shortest path 4.378 vs about 3.3; c13). These are older models, one language and culture; contamination of puzzle items was not checked.

**Insight riddles.** NazoNazo (b13): 7.6% non-reasoning, 17.6% reasoning, 52.9% humans. Models often wrote the right candidate in their thought log and did not endorse it. No verifier ablation exists (d14). Han et al. (a28): on 478 Braingle problems, models often find the short insight but all sometimes fall back on brute force; o3 scored 88.8% on the math set with hints plus a math prompt (80.5% on the hardest 50). Brute-force use falls with model size.

**Chain of thought as "verbalisation".** Liu et al. (c04, c20) used human tasks where verbalising hurts. GPT-4o fell 23.1 points on artificial grammar; Claude 3 Opus 8.0; Gemini 1.5 Pro 6.05; Claude 3.5 Sonnet did not fall (+1.8, p=.969). Only three of six tasks showed clear harm. Steering and tree-of-thought repaired it only in part. Hagendorff et al. (b17, b23): blocking CoT left ChatGPT-3.5 unchanged (4 points, n.s.) and cost GPT-4 7 points (95 to 88), so strong models can run the explicit route silently. On trap items (CRT) GPT-4 was 96% correct vs 38% for humans.

**What changed variety, by how much.**
- Temperature: weak (novelty 0.308) with a coherence cost; GPT-4 did not gain (c08).
- Creative system prompt: small gain (c09).
- Persona plus short plan before each idea: combinations 85 to about 240, above 208 for humans (d02).
- In-context regeneration (show prior answers, ask for different): strongest simple operator in NoveltyBench; paraphrase weak (d05).
- Verbalized sampling: 1.6 to 2.1 times diversity (d03).
- Explore-then-satisfy prompt: about 13 vs 8 distinct tasks at K=50 (d04); plain CoT no better than base.
- Distant source cues: no average gain (c11).
- Divergent-then-convergent prompt on MacGyver: +6.5% efficiency; self-reflection -9.7% infeasible (c03).
No study compared these at equal tokens. Some (d03, d04) write more tokens per set than a plain prompt.

**Search and verification.** Sampling covers more problems log-linearly (d09); with a verifier it becomes accuracy (15.9% to 56%). Without a verifier it plateaus. At equal compute, sequential revision wins on easy items, parallel on hard (d08). Models in a multi-turn setting do not recover from a wrong early turn (d07, drop 39%).

**Reasoning models.** Spontaneous mid-trace shifts occur in 6.31% of traces and those traces are less accurate (2.57% vs 16.44%; small tuned models). Triggered reconsideration helped only on MATH-500 (+8.41 pp). Reasoning distillation moved representations away from creative brain-like patterns in one study (c14).

**Not found.** No LLM test of EII, incubation, honing, or an explicit/implicit two-stage scaffold at equal tokens (d16, c16, d12).

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **No incubation by distraction or "sleep on it" step.** Part G (already in 4b). Unconscious-thought effect null after correction. [E] b06, K03. Adds the 399-person replication to 4b.
2. **Do not use temperature as the variation operator.** Part O, S3 open mode. [E] b16, c08, d02, K11.
3. **Engineered variation, not plain resampling, in open mode.** Part O, S3. Plain samples are 0.82 similar; persona-plus-plan, in-context regeneration and verbalized sampling raise distinctness. Choose by measured distinct count. [E] b15, c09, d02, d03, d05, K10, K23.
4. **Code dedups and selects; a model does not rank ideas.** Part O, G5, G8, S7. Overgenerate, dedup by meaning, select by running or by an external rater. [E] c10, K14.
5. **Rationale on or off by task class.** Part G11, S0 mode choice. Use written reasoning for math, symbolic, logic; pilot it on pattern and implicit tasks, since it cost 6 to 23 points on older models but not Claude 3.5 Sonnet. [E] c04, c20, d10, K08, K25.
6. **Sample wide only with a reliable check.** Part S3, S4, G12. Coverage scales with samples when a verifier exists and plateaus without. [E] d08, d09, K24.
7. **Reframe operators available at any state, not only after a stall.** Part O6, O8, S6. Impasse is not needed for insight. [E for humans] b02, b08, K05. The LLM benefit is untested (see tests).

### Test first
8. **Keep the first sample in the pool and audit it.** Part S4, O. [S] a24, d06, K07.
9. **Fresh-context restart with only the question and surviving constraints.** Part O, S6. Human incubation d about 0.29; wrong early LLM turns persist. [S] b04, d07, K01, K26. Test the context reset only; add no time gap.
10. **Wide cheap sampling plus rule check versus stepwise-only on insight items (the EII split).** Part S3, S4. [C] a19, a20, K06, K19.
11. **Entropy or disagreement trigger for reframe.** Part O, S6, consistent with G1. [S] b14, b25, K15. Gains seen only on small models on MATH.
12. **Rationale drop rule for insight items on current models.** Part G11. [S] c04, K08.
13. **Distant-source cue as an O7 seed.** [S] c11, K12; no average gain on LLMs.
14. **Divergent-then-convergent two-stage prompt.** Part S3, O. [S] c03, d04, K13.
15. **External verifier for riddle acceptance.** Part G5, S7. [S] b13, d14, K16.
16. **Honing-style blended draft re-viewed under several framings.** Part O. [S] a12, a13, K21. Weakest evidence; lowest priority.
17. **Process metrics (distance travelled, reframe count) logged beside the output score.** Part logging. [E] that the process gap exists (c05-c07, c13, K17); use for the agent is a proposal.

## 8. Concrete tests on our bench

Both arms at equal total tokens, setup counted. Items: BRAINTEASER items for insight-type, ARC items for rule and pattern, and a small open-idea set scored by distinct count and by running.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Variation operators | Open-idea prompts (30) | Plain n samples; temperature sweep; persona plus plan; in-context regeneration; verbalized sampling | Meaning-based distinct count after dedup; share passing a run check | Plain and temperature lowest; regeneration and persona-plan up by 50% or more (d02, d05) |
| T2 Wide sample plus check | BRAINTEASER, ARC | Stepwise loop (S3-S5 as is) vs k short independent attempts plus code check | Solve rate | Gain where the check is reliable (d09); none where it is not |
| T3 Fresh-context restart | BRAINTEASER, ARC items failed in round 1 | Continue same context vs restart with question and surviving constraints only vs recap | Solve rate in second half of budget | Restart better than recap (d07: recap recovers 15-20%) |
| T4 Rationale on/off | ARC, BRAINTEASER, pattern-learning items | Direct vs short rationale vs long rationale | Accuracy per task class | Rationale hurts pattern tasks on some models, helps symbolic |
| T5 Reframe trigger | Items with a stall | Reframe at fixed steps vs on stall only vs on entropy or disagreement vs never | Solve rate, tokens per solve | Signal-based not worse than fixed; tests d'Aliberti on a frontier model |
| T6 Gap filler | As T3 | Nothing; light task; heavy task between attempts | Solve rate | No effect for any filler; only the context change matters (K02) |
| T7 First-sample audit | BRAINTEASER, RAT-like items | First sample vs final answer | Share of correct finals already correct at first sample | High (human 72%, math 92%) |
| T8 Verifier on riddles | BRAINTEASER | Model self-acceptance vs external rule or second-model check | Accepted-correct rate | Closes part of the 17.6% vs 52.9% gap (untested) |
| T9 Distant source cue | Open design items | No cue vs distant cue vs near cue | Run-judged originality and correctness | No mean gain (c11) |
| T10 Honing draft | Open items | Discrete candidates vs one blended draft re-viewed under 3 framings | Distinct count and quality | Unknown; tests K21 |

## 9. What does not transfer, and why

- **A time gap.** People gain from incubation after a break; an LLM has no process between calls (K02). Only the context change can act. Do not add a wait.
- **Unconscious work and neural settling.** EII's implicit level is a settling neural network. A prompted model has no separate hidden channel, and written reasoning is not evidence of the real computation (G10; Hagendorff b23 shows silent answering works).
- **Verbal overshadowing as a law.** Replicated for faces only. It is not a general reason to ban rationales; LLM harm is task and model dependent (c04).
- **Working-memory load results.** Human limits do not map to context-window use.
- **Honing theory's state of potentiality.** The quantum-style formalism is a metaphor (a11). No operational test for a model.
- **Human mood, arousal and psychological entropy.** No LLM analogue measured.
- **EII fits.** Simulation matches were fitted to old human data (critique correction 3). They do not show the architecture helps a model.
- **Mind wandering.** Mixed even in humans (c26).
- **Memory consolidation effects** (a04): confined to the first minute of the second recall test.
- **TACIT diffusion "eureka" (c15).** Single author, toy mazes; an analogy only.

## 10. Open questions

1. Does a scaffold that separates wide cheap sampling from a rule check beat a plain loop at equal tokens on insight items? No published test (d16).
2. Does a fresh-context restart help an LLM, and does what happens in the gap matter? No LLM test.
3. Which variation operator gives the most real distinctness per token? No equal-token comparison.
4. When should the rationale be dropped, on current models, for insight items?
5. Does program-triggered reframing help frontier models?
6. Original N and statistics of Schooler et al. (1993) and Gabora and Saab (2011): not opened.
7. Full texts of Weisberg 2015 and Fleck and Weisberg 2013 (five problems) not read; the toolbox-of-methods view is untested by us.
8. Does an external verifier close the riddle endorsement gap?
9. Does the fast-first-answer finding hold for LLMs on insight items?
10. Where does diversity plateau after dedup across models (5% non-duplicate in c10 is one point)?
11. Do newer frontier models still show the process-measure gaps found with GPT-3.5 to GPT-4o?

## 11. Sources

[V] opened, [M] snippet, abstract only or second-hand.

- [V] Helie and Sun 2010, EII, Psychological Review 117:994-1024. https://ccn.psych.purdue.edu/papers/Helie-Sun-EII.pdf (a01-a06)
- [M] Helie and Sun 2010 PubMed abstract. https://pubmed.ncbi.nlm.nih.gov/20658861/ (b09)
- [V] Helie, Sun, Xiong 2008 distractor tasks. https://ccn.psych.purdue.edu/papers/pp772-helie.pdf (a07, c01)
- [V] Helie and Sun 2009 EII-BF (intro and method only). https://ccn.psych.purdue.edu/papers/Helie-Sun.pdf (a09)
- [V] RPI press release 2010. https://www.sciencedaily.com/releases/2010/12/101201124345.htm (a10)
- [M] Dodds, Ward, Smith 2003 review (second-hand via a07; a08)
- [V] Gabora 2017 honing theory. https://arxiv.org/pdf/1610.02484 (a11, a12, a15-a17, a29, b10, c17)
- [V] Carbert, Gabora et al. 2014. https://arxiv.org/pdf/1408.6849 (a13)
- [V] Gabora 2019 convergent and divergent thought. https://arxiv.org/pdf/1811.04512 (a14, b11)
- [M] Gabora and Saab 2011 (second-hand via a12)
- [M] Weisberg 2015. https://doi.org/10.1080/13546783.2014.886625 (a18, b18)
- [M] Fleck and Weisberg 2013. https://doi.org/10.1080/20445911.2013.779248 (b19)
- [V] Fleck and Weisberg 2004. https://link.springer.com/content/pdf/10.3758/BF03196876.pdf (b01-b03)
- [V] Chein and Weisberg 2014. https://link.springer.com/content/pdf/10.3758/s13421-013-0343-4.pdf (a19)
- [V] Stuyck, Cleeremans, Van den Bussche 2022. https://dipot.ulb.ac.be/dspace/bitstream/2013/336196/3/AhaUnderPressureStuycketal.pdf (a20, b07, b22)
- [V] Stuyck et al. 2021 (abstract). https://pubmed.ncbi.nlm.nih.gov/33721581/ (b08)
- [V] Insight problem solving is not that special (abstract and intro). https://pmc.ncbi.nlm.nih.gov/articles/PMC10366031 (a21)
- [V] Kershaw and Ohlsson 2001. https://conferences.inf.ed.ac.uk/cogsci2001/pdf-files/0489.pdf (a22)
- [M] Weisberg and Alba 1981 (a23)
- [V] Beucler and De Neys 2026. https://jeremie-beucler.github.io/files/insight_Beucler_2026.pdf (a24)
- [V] Sio and Ormerod 2009. https://www.Gwern.net/doc/psychology/writing/2009-sio.pdf (b04, b05, b26)
- [V] Nieuwenstein et al. 2015, Judgment and Decision Making (b06)
- [V] Smith, Ward, Finke 1995. https://ecologylab.github.io/research/publications/ParadoxesPrinciplesProspects.pdf (b12)
- [M] Alogna et al. 2014 registered replication. https://doi.org/10.1177/1745691614545653 (b20)
- [V] Mickes and Wixted 2015 (abstract). https://pubmed.ncbi.nlm.nih.gov/25987518/ (b21)
- [V] Kiyokawa and Dienes 2019. https://users.sussex.ac.uk/~dienes/Kiyokawa%20&%20Dienes%202019%20Cogsci.pdf (d01)
- [M] Verbal overshadowing summary. https://en.wikipedia.org/wiki/Verbal_overshadowing (d15)
- [V] Zhang et al. 2025 AI creative output. https://arxiv.org/abs/2503.23327 (a25, c05-c07)
- [M] Orru et al. 2023; Raz et al. 2024; Orwig et al. 2024 (second-hand via Zhang; a26, c21, c22)
- [V] Mizumoto et al. 2025 NazoNazo. https://arxiv.org/pdf/2509.14704 (a27, b13, b24, d14)
- [V] Han et al. 2025. https://arxiv.org/pdf/2505.10844 (a28)
- [V] d'Aliberti and Ribeiro 2026. https://arxiv.org/abs/2601.00514 (b14, b25)
- [V] Jiang et al. 2025. https://arxiv.org/pdf/2510.22954 (b15)
- [V] Peeperkorn et al. 2024. https://arxiv.org/pdf/2405.00492 (b16)
- [V] Hagendorff et al. 2023. https://arxiv.org/pdf/2212.05206 (b17, b23)
- [V] Tian et al. 2024 MacGyver. https://arxiv.org/abs/2311.09682 (c03)
- [V] Liu et al. 2025 Mind your step. https://arxiv.org/abs/2410.21333 (c04, c20)
- [M] Fallshore and Schooler 1993; Williams and Lombrozo (via c04; c23)
- [V] Chen and Ding 2023. https://arxiv.org/abs/2310.11158 (c08)
- [V] Wenger and Kenett 2025. https://arxiv.org/abs/2501.19361 (c09)
- [V] Si, Yang, Hashimoto 2024. https://arxiv.org/abs/2409.04109 (c10)
- [V] Liu et al. 2026 cross-domain mapping. https://arxiv.org/html/2603.19087 (c11)
- [M] Nath, Dayan, Stevenson 2024 (abstract). https://arxiv.org/abs/2405.00899 (c12)
- [V] Domanti et al. 2026. https://arxiv.org/html/2602.02048v1 (c13)
- [V] Ismayilzada et al. 2026. https://arxiv.org/html/2604.03480v1 (c14)
- [V] Nobrega Medeiros 2026 TACIT. https://arxiv.org/pdf/2602.07061 (c15)
- [V] Creative problem solving in LLMs: what would it take (position paper). https://arxiv.org/pdf/2405.01453 (c16; d12 snippet)
- [V] Polyak and Balkhyoor 2026. https://computationalcreativity.net/iccc26/papers/ICCC26_paper_134.pdf (c18)
- [V] Franceschelli and Musolesi 2026. https://arxiv.org/html/2604.13242v1 (c19)
- [M] Doshi and Hauser 2024. https://www.science.org/doi/10.1126/sciadv.adn5290 (c24)
- [M] Hubert et al. 2024. https://www.nature.com/articles/s41598-024-53303-w (c25)
- [M] Du, Gordon, Tolmie 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12190454/ (c26)
- [V] Deng, Brucks, Toubia 2026. https://arxiv.org/pdf/2602.20408 (d02)
- [V] Zhang et al. 2025 Verbalized Sampling. https://arxiv.org/pdf/2510.01171 (d03)
- [V] Nguyen et al. 2026 CreativeDC. https://arxiv.org/pdf/2512.23601 (d04)
- [V] Zhang et al. 2025 NoveltyBench. https://arxiv.org/pdf/2504.05228 (d05)
- [V] Chen et al. 2024 overthinking. https://arxiv.org/pdf/2412.21187 (d06)
- [V] Laban et al. 2025. https://arxiv.org/pdf/2505.06120 (d07)
- [V] Snell et al. 2024. https://arxiv.org/pdf/2408.03314 (d08)
- [V] Brown et al. 2024. https://arxiv.org/pdf/2407.21787 (d09)
- [V] Sprague et al. 2024. https://arxiv.org/pdf/2409.12183 (d10)
- [V] Gema et al. 2025 (abstract and figure overview). https://arxiv.org/pdf/2507.14417 (d11)
- [M] Kumar et al. 2025. https://arxiv.org/abs/2410.03703 (d13)
