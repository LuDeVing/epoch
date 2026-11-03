# Critiques of the three-load model: deep document

*Subfield A08.07. Written from evidence_a-d.jsonl, claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids (a01, b13, c04, d01 ...) point to the jsonl lines. Numbers marked "re-checked" were re-opened in the cross-check pass. Evidence lines c11 to c27 belong to another subfield and were not used.*

## 1. What it is

Cognitive load theory (CLT) says working memory is small and instruction should fit it. The 1998 form of the theory split the load on working memory into three parts:

- **Intrinsic load (ICL):** set by the material. How many elements must be held together (element interactivity), relative to what the learner already knows.
- **Extraneous load (ECL):** wasted effort caused by poor design (split attention, redundancy, noise).
- **Germane load (GCL):** effort that builds schemas (learning).

The 1998 model said the three **add up** to total load, and the total must stay under working-memory capacity.

The critique is about that split. Four charges:

1. **Concept.** The parts are not cleanly separable. Intrinsic is about an object (the material); germane is about a process (the learner). The same activity can be germane for a novice and extraneous for an expert (a01, a05, b01, b04).
2. **Additivity.** The sum is a premise, never directly tested. If the parts are in different categories, adding them is a category error. If they are all processes, they can interact (a02, b02).
3. **Falsifiability.** Germane load is explained after the fact: better result means germane, worse means overload (a04, b03).
4. **Measurement.** Self-ratings do not separate the three types. They correlate in ways the theory forbids, and they often fail to move when instruction changes (a06, a18, b05, b06, b13).

The main critic is Ton de Jong (2010, *Instructional Science* 38:105-134). Kalyuga (2011) argued for two types. The theory's own authors partly conceded in 2019: germane load is no longer a third additive part (a08, b18).

**Why it matters for our agent.** The agent could be tempted to build a "load budget" from three dials (task difficulty, noise, useful effort) and add them. The critique says: do not. Use counted operations (items held, distractor tokens, steps, dead ends), not load labels, and test any interaction at equal tokens. This subfield is mostly a caution. It supports schema guardrails G7, G11, G12 and section 4b, and adds a few small, testable items.

**Overlap.** Element interactivity and the effects (worked example, split attention, expertise reversal) are in other A08 subfields. Expertise reversal is touched here only where it bears on the label problem. Related parallel subfields: Working-memory limits and chunking; Worked examples; Theories of mental representation.

## 2. History and theories in depth

### 2.1 Lineage of the model

| Year | Model | Source |
|---|---|---|
| 1988 | Sweller: two parts, intrinsic and extraneous | a22 |
| 1998 | Sweller, van Merrienboer, Paas: germane load added as a third, additive part. Additivity stated on p. 263 | a02, a22 |
| 2010 | Sweller: element interactivity defines intrinsic load AND extraneous load | a12 (abstract only; content confirmed via a09) |
| 2010 | De Jong: the critique (below) | a01-a07, b01-b07 |
| 2011 | Kalyuga: "How many types of load does it really need?" Germane and intrinsic share one basis (element interactivity and learner knowledge); reduce to two | a11 (abstract only) |
| 2019 | Sweller, van Merrienboer, Paas, "20 years later": germane load is no longer a separate additive load. It is working-memory resources redirected to intrinsic work instead of extraneous work. Only intrinsic and extraneous are basic categories | a08, a10, b18-b19 |
| 2022 | Skulmowski and Xu: cost-benefit view of extraneous load; calls for a dyadic model are now common | a21, a22 |

Reason the 2019 authors gave for the change: under the 1998 view germane load simply replaces extraneous load, so cutting extraneous load should leave total load unchanged. Many studies show total load falling (a08, b18).

### 2.2 De Jong's critique in detail (opened, a01-a07)

Basis: a review of the 35 most cited ISI papers in the field. Argument and examples, no new data.

- **Intrinsic is not fixed (a03).** The theory says intrinsic load depends only on element count and interactivity and instruction cannot change it. Counterexamples: Klahr and Robinson (1981), a Tower of Hanoi variant with all pegs occupied at the end was much harder with the same number of moves; Chi (1992), a change of ontological category (force as substance) is hard whatever the element count; DeLeeuw and Mayer (2008), changing sentence complexity with fixed content moved extraneous load more than intrinsic. No numbers given.
- **Same process, different label (a05, b01, b04).** Gerjets and Scheiter (2003): a surface-emphasising group beat a structure-emphasising group on isomorphic problems; structure-emphasising learners spent longer learning, so their extra schema work counted as extraneous for that goal. Scott and Schwartz (2007): hypertext navigation maps were germane or extraneous depending on use. Novice germane can be expert extraneous.
- **Post-hoc germane (a04, b03).** Sweller et al. (1998) explained higher reported load plus better transfer under high-variability practice as germane. De Croock et al. (1998, distillery troubleshooting) found better transfer from high variability with NO higher rated load, so the story failed. Stull and Mayer (2007): learners who built their own graphic organisers did worse than learners given author-made ones; the authors called it extraneous after the fact, but it could equally be germane overload.
- **Additivity (a02, b02).** See section 1, charge 2. No direct additivity experiment is run in the paper.
- **Measurement (a06, b05-b07).** The Paas 9-point effort item was validated in two studies (alpha .90 and .82). De Jong notes that high alpha makes it look like a learner trait, not a task-by-learner effect. About 14 studies (including Paas 1992, Stark 2002, Tabbers 2004, Lusk and Atkinson 2007, Hummel 2006, Fischer 2008, Wouters 2009, Kester and Kirschner 2009) found performance differences with no rating differences. A few (Paas 2007, Seufert 2007) found the reverse. Seufert et al. (2007) got different load effects from the same set-up and speculated that people read the one item as extraneous load in one study and overall load in the other. Attempts to separate types by rating (de Jong 1999 three sliders; Gerjets 2006; Corbalan 2008; Cierniak 2009 three single questions; Gerjets 2009b five items) gave inconsistent results.
- **Efficiency formula (a07).** E = (P - R)/sqrt(2) is used inconsistently. Kalyuga et al. (1998) wrote it with an absolute value that should not be there. Low performance with low load gives the same efficiency as high performance with high load.
- **Novelty (a07).** The three CLT design recommendations (fit prior knowledge, drop non-essential information, stimulate deep processing) existed earlier (Dick and Carey 1990; Gagne 1988; Reigeluth 1983). De Jong proposes two classes: processes that produce knowledge and processes that do not.

### 2.3 Kalyuga and the two-factor camp

Kalyuga (2011) is cited by Skulmowski and Xu (2022), Jiang and Kalyuga (2020) and Krieglstein et al. (2022). Only the abstract was opened (a11). Leppink and van den Heuvel (2015) also argued for a dyadic model (via a22). Debue and van de Leemput (2014) cite Kalyuga's argument that intrinsic and germane may be redundant (a14).

### 2.4 The authors' reply (2019, opened)

- Germane load is now "germane processing", a redistribution of resources, not a load of its own (a08, b18).
- Element interactivity now applies to extraneous load too (a09, b19). Intrinsic load depends on the person's knowledge, not only the material. Risk: circular if knowledge is not measured independently (b19 limits).
- Most instructional effects are due to varying extraneous load. In 1998 seven effects were listed. Many experiments never measured load; the predicted learning effect was counted as support (a09).
- The Paas rating gives only an overall intrinsic-plus-extraneous measure. A single post-phase rating is always higher than the mean of per-task ratings (van Gog 2012; Schmeck 2015). The Leppink 10-item instrument can tell intrinsic and extraneous apart (a10).
- Felt effort is an invalid cue for learning: people think "it cost effort, so I learned". More valid cues are explaining a solution to a peer, or generating keywords after a delay (b20).

### 2.5 Related critique: extraneous is not always bad

Skulmowski and Xu (2022) review five design factors that add task-irrelevant load yet help learning or motivation: interactive media, immersion, disfluency, realism, redundant elements. Their cost-benefit model: each extraneous cost is tied to a germane benefit, and the benefit shows only when the test matches the learning outcome (a21). Narrative review, no pooled effect.

## 3. Core findings with exact numbers

Status key: established / single-source / contested, as in claims.jsonl.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Three load types cannot be cleanly split in concept; same activity changes label with learner or goal | Review of the 35 most cited ISI papers; examples Gerjets and Scheiter 2003, Scott and Schwartz 2007 | de Jong 2010 (a01, a05, b04) | established (K01), argument not data |
| Original authors dropped germane as a third additive load | 1998 model: 3 additive parts; 2019: 2 basic categories | Sweller et al. 2019 (a08, b18) | established (K02) |
| Additivity untested | No direct experiment in de Jong; Park (2010) unverified (secondhand, page blocked, 403) | a02, a29, d14 | single-source (K03, K25) |
| Germane explained post hoc | de Croock 1998: better transfer, no higher rated load | de Jong (a04) | single-source (K04) |
| Questionnaires are reliable | 53 articles, 67 experiments, N=7,413, mean age 20.4. Pooled alpha ICL about .82 (text gives .823 and .827), ECL .773, GCL .860. Per instrument: Leppink 2013 ICL .845, ECL .759, GCL .909; Klepsch ICL .776, ECL .798, GCL .734; Leppink 2014 ICL .851, ECL .788, GCL .806 | Krieglstein 2022 (a18, b12) | established (K05) |
| ICL and ECL ratings correlate positively; ECL and GCL negatively | ICL-ECL r: Leppink 2013 .298 (k=25), Klepsch .350 (k=16), Leppink 2014 about .5, Eysink .53 (k=9). ECL-GCL: Leppink 2013 -.086 (ns), Klepsch -.246, Leppink 2014 -.331 | Krieglstein 2022 (a18, b13) | single-source (K06) |
| Three vs two factors | Klepsch Study 2 (65-95 per task, 17 tasks): one-factor CFI .612, TLI .418, RMSEA .071, AIC 2185; three-factor CFI .970, RMSEA .021, AIC 845; two-factor (productive vs unproductive) CFI .974, RMSEA .021, AIC 862. Jiang and Kalyuga N=60: two-factor chi2=54.069, df=53, p=.433, CFI .994, TLI .993, RMSEA .018, SRMR .077 | a15, b09, a17, b16 | contested (K07) |
| Germane ratings track motivation, not learning | Debue 2014 N=92: GCL-performance r=.045 (ns); GCL-focused immersion r=.362; two other absorption scales r=.289, .401 (p<.01); ECL-GCL r=-.470; ICL-GCL r=-.164 (ns) | a13, a14 | contested (K08) |
| Germane rating weakly related to retention and transfer | Leppink 2013: GCL-retention .188 (k=15), GCL-transfer .173 (k=12); Klepsch: .219 and .217. ICL-retention -.061 (ns), ECL-retention -.114, ICL-transfer -.188, ECL-transfer -.120 (Leppink); Klepsch ECL-transfer -.261 | a19, b14 | contested (K08) |
| Naive germane scale failed to tell low from high germane tasks | Klepsch Study 1 N=97; GCL F=0.04, p=.84; Study 2 effects ICL d=.73, ECL d=.94, GCL d=.35 | a15 | single-source |
| Ratings overlap with plain effort | Klepsch Study 1 r with effort item: ICL .41-.68, ECL .32-.60, GCL .32-.41, sum .32-.69 | b10 | single-source |
| Load ratings often do not track instruction | About 14 studies with performance difference, no rating difference | de Jong (a06, b06) | established (K09) |
| Single post-phase rating exceeds mean of per-task ratings | van Gog 2012; Schmeck 2015 (via authors) | a10 | secondhand |
| Efficiency formula used inconsistently | E=(P-R)/sqrt(2); absolute value error in Kalyuga 1998 | a07 | single-source (K19) |
| Felt effort is an invalid cue for learning | Authors' account, no numbers | b20 | single-source (K10) |
| Extraneous-looking features can help | Interactive media, immersion, disfluency, realism, redundancy | Skulmowski and Xu 2022 (a21) | single-source (K11) |
| LLM: irrelevant text lowers multi-hop accuracy, graded | Gemini-2.0-Flash-001: 0.85 control, 0.82 / 0.78 / 0.72 at 20/50/80% distractors; slope -0.003 per % (CI -0.004 to -0.002, p<.001); long control 0.82 (p=.45); residue 0.78 (p=.12). GPT-4o-0613: 0.65 to 0.55 at 80%, slope -0.002, p=.07; 32% outputs lacked final answer (12% after fixes). Llama-3-8B, Llama-3-70B, Mistral-7B: 0 everywhere. Hop recall: Gemini 0.90 to 0.75, GPT-4o 0.80 to 0.65. 200 questions x 10 runs. Re-checked | Adapala 2025 (a23, a24, b24, b25, c04, c05) | single-source (K12) |
| LLM: distractor harm is U-shaped on state-tracking puzzles | gpt-5 0.97 / 0.89 / 0.91; o3 0.93 / 0.89 / 0.88; gemini-2.5-flash-lite 0.38 to 0.53; Phi-4-reasoning-plus 0.59 to 0.45; EXAONE-Deep-32B 0.47 to 0.32. Quadratic term improved AIC for 18 models; 5 had no significant quadratic term (incl. o3, gemini-2.5-pro, gemini-2.5-flash). Re-checked | Kaiser et al. 2025 (a25-a27, c03) | contested (K13) |
| LLM: difficulty and length hit weak models hardest | 12 of 22 models below 50% by d=5; N=250 only gpt-5 0.76 and o3 0.68 above 50%; N 20 to 50: DS-Llama-70B 0.89 to 0.66, Qwen3-8B 0.71 to 0.40, gpt-5 1.00 to 0.98; d=10: gpt-5 0.82, o3 0.80, weakest 0.10-0.15 | CogniLoad (a25, c01, c02) | established (K14) |
| LLM: load knobs interact, descriptively | Higher d deepens the U; longer N flattens it (N=100: strongest models 0.93-0.97 at every rho). o4-mini N=5 chained GSM8K: compliance 55.0% with 0 extra constraints, 32.5% with 3 | CogniLoad appendix (d01); Mittal (d11) | single-source (K20) |
| No formal interaction test in either LLM grid | CogniLoad fits d, log10 N, rho, rho^2, no products; authors list interactions as future work | a26, d02 | gap (K15) |
| Retrieval-heavy tasks: steady decline with length | NoLiMa GPT-4o 98.1, 98.0, 95.7, 89.2, 81.6, 69.7 at 1K to 32K (base 99.3); Llama 3.3 70B 94.2 to 42.7; Claude 3.5 Sonnet 85.4 to 29.8; Gemini 1.5 Pro 86.4 to 48.2; GPT-4o mini 67.7 to 13.7; 11 of 13 below 50% of base at 32K; reasoning models also below 50% at 32K | Modarressi 2025 (d03, d04) | contested (K21) |
| Longer reasoning is not success | Shortest vs random +2.2 to +15.7 points; longest vs random -5.4 to -18.8; shortest vs longest up to +34.5; short-1@k uses up to 40% fewer thinking tokens than majority voting (4 models, 4 benchmarks). Across 10 models, CoT length and review ratio correlate negatively with accuracy; failed-step-fraction reranking up to +10 points pass@1 on AIME | Hassid 2025 (d05); Feng 2025 (d06) | established (K22) |
| Late confidence is better calibrated | Reasoning models better in 33 of 36 settings; improves along the CoT | Yoon 2025 (d07) | single-source (K23) |
| CLT-labelled prompts: token saving | CLAI Llama-3-70B GSM8K CoT 92.5% at 485 tokens vs CLAI 92.3% at 310 (36.1% less); MATH 53.9 at 812 vs 53.5 at 525; Llama-3-8B GSM8K 90.1/450 vs 89.8/290 vs tuned 91.5/255 | Zhang 2025 (c06, c07) | contested (K16) |
| CLT-labelled multi-agent: gains and losses | CoThinker Reasoning vs CoT +5.1 pp (p=.001); Data Analysis vs IO +5.3 pp (p<.001); Language vs SR +6.0 pp; vs MAD up to +12.8 pp; instruction-following vs IO -1.2 pp, three Holm-significant losses; near misses vs DMAD p=.63, .16. Math ablation (TMS on+Styles on / TMS on+Styles off / TMS off+Styles on): Qwen3-30B-A3B 81.87 / 69.79 / 76.41; GPT5-Nano 55.97 / 49.02 / 62.36; GPT-OSS-20B 57.15 / 48.21 / 58.37 | Shang 2026 (b21, b22, c08, c09) | contested (K16) |
| Concurrent load drops format compliance | Compliance down 2-21%, terminal constraints up to 50%; reminder restores 90-100%; 8,000+ prompts, 3 model families; mean drop DeepSeek 10.2%, o4-mini 8.9%; reminder gain 17.7% / 16.9% / 12.7%; GSM8K 93% to 27% for one chained model | Mittal 2026 (b26, d11) | single-source (K17) |
| Stacked tasks raise jailbreak success | Total ASR: Llama-3-70B 92.67%, GPT-4 90.95%, Claude-3-Opus 99.99%, Gemini-1.5-Pro 84.05%, Gemini-1.0-Pro 75.43%; Claude-3.5-Sonnet 53% | Upadhayay 2024 (b23) | single-source (K18) |
| Extra examples hurt after 5-20 shots, strong and weak models alike | 7 LLMs; GPT-4o, GPT-3.5, LLaMA-3.1-8B, Gemma-3-4B decline; DeepSeek-V3 plateaus; LLaMA-3.2-3B weak from start; Mistral-7B keeps improving | d10 | single-source (K24) |

## 4. Mechanisms and models

### 4.1 What the critique says about the model structure

Three candidate structures for "load":

1. **Three additive parts (1998).** Total = ICL + ECL + GCL <= capacity. Requires the parts to be independent and in one category. De Jong: they are not.
2. **Two parts (Kalyuga 2011; 2019 reply).** Task-necessary processing vs wasted processing. Germane = resources moved from the wasted pile to the necessary pile. Fits Jiang and Kalyuga (CFI .994) and Klepsch's two-factor model (AIC 862 vs 845 for three).
3. **Interaction model.** Understanding material (intrinsic side) changes how much learner processing is possible (germane side), so the effects multiply instead of add (a02).

An engineer's view: do not define variables by role labels. Define them by counts the program can measure.

### 4.2 Operational definitions an agent can implement (our design, built from a23-a25, c07, d06)

| Quantity | Counted how | Used in |
|---|---|---|
| Needed items | number of entities, attributes, clauses that must be combined for the answer (CogniLoad's d) | S0 gate: task size |
| Length | number of sequential steps or tokens of task text (CogniLoad's N) | S0 gate, budget |
| Distractor ratio | irrelevant tokens / total context tokens (Adapala 20/50/80%; CogniLoad rho 5-95%) | S1 input hygiene |
| Wasted effort | share of reasoning steps in abandoned branches (Feng's failed-step fraction) | S9 logging |
| Reasoning length | output tokens | G11 cap |

Keep them as separate logged numbers. Never sum them into one "load".

### 4.3 The fitted LLM models (what exists)

- **CogniLoad (a26):** binomial logit, accuracy ~ d + log10(N) + rho + rho^2. Additive on the logit scale; no products. Capacity points at 50% accuracy per axis (ECL50, NT50, ID50) per model.
- **ToolLoad-Bench (d12, c10):** success = exp(-(k * load + b)), load = intrinsic + E * extraneous, E fitted per model, germane dropped. Total load as a sum over steps follows from two assumptions (exponential decay, independent steps). Fit judged by Hosmer-Lemeshow only (p>0.05: GPT-4o 0.23, Claude 3.7 Sonnet 0.11, Qwen3-8B 0.89; 500 instances). A non-significant H-L test cannot show an interaction term would not fit better. Extraneous load is rated by Gemini-2.5-pro.
- **ICE (a24):** two counts, needed tokens (defines intrinsic) and unneeded tokens (extraneous). The paper itself says the framework collapses to two parts.

### 4.4 How to test additivity (implementable)

On a synthetic grid (the CogniLoad generator is public): fix an output-token cap. Vary d, N, rho in a full factorial. Fit two logit models: (A) main effects only, (B) main effects plus products d*N, d*rho, N*rho (and rho^2 terms). Compare by AIC and likelihood-ratio test. If B wins clearly, the load knobs interact and a single summed budget is wrong. This is the missing experiment (gap 1).

### 4.5 Prompt-level uses of CLT seen in the LLM literature

- **CLAI (c06, c07):** meta-prompt: rate intrinsic load 1-10 by self-rating, set a token budget (e.g. 50 tokens easy, 500 hard), filter context, then reason. The self-rating is a pre-reasoning gate; section 7 advises against that (K23).
- **CoThinker (b21, c08):** split a task across specialist agents; shared memory; moderated routing. Helps on reasoning-heavy tasks, loses on low-load instruction-following. Load is never measured; the high/low boundary is set by task type after the fact.
- **Long et al. (b27):** use the three loads as a rubric across 150+ prompting papers (21 properties, six dimensions); germane mapped loosely to "ask yourself" prompts. Analogy only.

## 5. What holds up

### 5.1 Holds

- **The concept problem is real and conceded.** The theory owners removed germane as an additive load (K02). Two sources agree on the lineage (a08, a22).
- **Questionnaire reliability is fine** (alpha .74 to .91 across the instruments, N=7,413; K05).
- **ICL and ECL ratings correlate positively across all four instruments** (r about .30 to .53). Learners cannot or do not separate them, or the types really interact. The meta-analysis cannot say which (b13 limits).
- **Ratings often fail to follow instruction** (about 14 studies; K09).
- **LLM capacity shrinks with difficulty and length, more for weak models** (K14; two sources, CogniLoad and Adapala's floor effect).
- **Longer reasoning is not better within a question** (K22; Hassid and Feng agree).

### 5.2 Failed or contested

- **Three vs two factors:** unresolved. Klepsch's three-factor model beat its own two-factor model by only 17 AIC points (845 vs 862) and the paper could not clearly choose; Jiang and Kalyuga (N=60, one domain) found two. Small samples (65-95; 60). Zavgorodniaia 2020 contests Jiang and Kalyuga (secondhand, via Krieglstein).
- **Germane and learning:** Debue r=.045 (ns) vs Krieglstein r about .17-.22. Both small. Consistent with a weak, motivation-flavoured construct. Leppink et al. (2014) dropped their germane scale because it did not correlate acceptably with learning (a16, secondhand).
- **Klepsch's naive germane scale failed in Study 1** (F=0.04, p=.84) and had to be rewritten.
- **Distractor harm shape:** graded and roughly linear (Adapala, Gemini) vs U-shaped (CogniLoad) vs steady decline (NoLiMa). Different tasks and distractor definitions. Not resolved (K13, K21).
- **"Load" in LLM studies is not validated.** CogniLoad and Adapala vary tokens, not load in a validated sense. Mapping "task length N = germane load" is a stretch the authors flag (a25).

### 5.3 Moderators

- **Prior knowledge:** the ability to separate ICL from ECL depends on prior knowledge (Zu et al. 2021, secondhand via a20, b28, not read).
- **Model strength:** weak models hit a floor (3 of 5 Adapala models at 0%); at a floor the load effect cannot be tested.
- **Task type:** state-tracking vs retrieval (K21).
- **Position of the constraint:** terminal constraints suffer most under load (Mittal, up to 50%).
- **Comparison arm:** CoThinker beats weak baselines (IO, CoT, MAD) but near-misses a stronger one (DMAD, p=.63, .16). Its shared memory hurt newer GPT models (math 55.97 with it vs 62.36 without for GPT5-Nano; 57.15 vs 58.37 for GPT-OSS-20B).

### 5.4 Interventions that worked or did not (LLM)

| Intervention | Result | Note |
|---|---|---|
| Strip distractors / filter context | CLAI LongBench QA F1 65.2 full context, 68.1 LLMLingua, 69.3 CLAI at 4.2x compression (c06) | single author, no seeds or CIs |
| Token budget by self-rated difficulty (CLAI) | 36% fewer tokens, equal accuracy on 2 Llama models | no plain "be brief" control |
| Constraint reminder at the end | restores 90-100% compliance (Mittal) | no verify state, tokens not equalised |
| Shortest-of-k | up to 40% fewer thinking tokens than majority voting at similar accuracy (Hassid) | open models only |
| Failed-step reranking | up to +10 points pass@1 on AIME (Feng) | LLM annotator |
| Decompose across agents (CoThinker) | +5.1 / +5.3 pp on reasoning and data analysis | loses on instruction-following |
| More examples | helps up to about 5-20 shots, then hurts most models (d10) | one task family |

### 5.5 Flags on the evidence base

- Almost all human evidence is questionnaire self-report, students (mean age 20.4), small N per study.
- De Jong 2010 and Kalyuga 2011 are argument papers with no new data.
- Park (2010) is the only direct additivity test reported, and it is secondhand and unverified.
- CLAI looks suspect on numbers: single author, no seeds, round numbers, Llama-3-8B MATH 50.2% looks high (c06 limits). Verify before relying.
- Adapala: single-author preprint; GPT-4o result not significant (p=.07); truncation confound; "10 replications" at temperature 0 is unclear.
- Krieglstein: ICL pooled alpha is given as both .823 and .827 in the paper; treat as about .82 (critique.md).
- Debue 2014 prints one intrinsic statistic as F=5.748, p=.128, which is internally inconsistent (a13).
- Search coverage of 2020-2026 LLM work is partial. Absence claims are weak.

## 6. Language models

No LLM paper tests the three-load model as a theory. What exists: benchmarks that use the load labels for knobs, prompts that borrow the labels, and adjacent measurements.

### 6.1 Benchmarks with load knobs

**Adapala (2025), ICE benchmark (opened, re-checked).** 200 questions (50 SEC, 100 FanOutQA, 50 MINTQA), 10 runs, 5 models. Added irrelevant text at 20/50/80%.
- Gemini-2.0-Flash-001: 0.85 / 0.82 / 0.78 / 0.72. Linear slope -0.003 per % (p<.001). Hop recall 0.90 to 0.75.
- Length-matched neutral filler: 0.82 (p=.45 vs control). So the harm is from distractor content, not length alone.
- Residue (distractors before the task): 0.78, p=.12, not significant. Residue size correlated with task similarity (r=0.42 Gemini, CI [0.21,0.59]; r=0.35 GPT-4o, CI [0.12,0.54]).
- GPT-4o-0613: 0.65 to 0.55, p=.07, truncation confound.
- Three models at 0.00 everywhere: intrinsic floor.

**Kaiser et al. (2025), CogniLoad (ICLR 2026 version exists, not read).** d in {1,3,5,7,10}, N in {20,50,100,250}, rho 5-95%. 13 open models x 100 puzzles per cell (about 14,000 per model); 4 proprietary x 10 per cell (1,400).
- Length is the dominant stressor.
- Difficulty: gpt-5 1.00 to 0.97, o3 0.96 to 0.93 from d=1 to 3; small models drop 0.10-0.25. At d=10 (mean over rho): GPT-5 0.821, o3 0.804, GPT-5-mini 0.675, Gemini-2.5-Pro 0.654, o4-mini 0.646, DeepSeek-R1-0528 0.475, R1-Distill-Llama-70B 0.361, QwQ-32B 0.300, Qwen3-32B 0.280.
- Distractors: U-shaped, worst at 25-50% needle-to-hay.
- Interaction by eye (d01): d=1 shallow dip at rho 25-50%; harder puzzles deepen it; N=20 clear U; N=100 strongest models flat at 0.93-0.97; N=250 curves flat or rising at low levels. Output tokens not equal (32K context cap, default decoding).
- Authors: CLT is an analogy, LLM load is computational; no scaffold ablation.

**NoLiMa (d03, d04).** Retrieval where question and needle share no words. Steady decline with context length, no recovery; reasoning models also fall below 50% at 32K. Varies length, not ratio.

**ToolLoad-Bench (c10, d12).** Assumes additivity; fit by calibration test only. Overall accuracy: xLAM2-32B 78.8%, GPT-4o 68.0%, Qwen3-32B 55.2%, Qwen3-8B 38.6%, Llama3.3-70B 17%.

**Mittal (2026), prospective memory (b26, d11).** Format constraint plus hard task. Compliance falls 2-21% under concurrent load; terminal constraints up to 50%. Stacking compounds: o4-mini at N=5 chained GSM8K, 55.0% with 0 extra constraints, 32.5% with 3; chain length alone 83.6 / 71.1 / 66.7%. DeepSeek 55-65% at N=5; Llama 75-95%. Mean output tokens 538 baseline vs about 977-1150 chained. Greedy, max 2048 tokens. Reminder gain 12.7-17.7%.

**Cognitive overload attack (b23).** Stacking six tasks raised jailbreak success, but load is just task count and obfuscation is a rival cause. Claude-3.5-Sonnet resisted (53%).

### 6.2 Prompts and agents using CLT as a label

CLAI (36% fewer tokens at equal accuracy on two Llama models) and CoThinker (+5.1 pp reasoning, losses on instruction following) are in sections 3 and 5. Neither was compared with a plain token-budget prompt on tasks the authors did not pick (d13, K26). Both define the three loads by the prompt itself, the same circularity De Jong flags.

### 6.3 Adjacent measurements

- **Effort and length (d05, d06):** shortest chain beats longest by up to 34.5 points; length and review ratio correlate negatively with accuracy across 10 models. A "germane = effortful reasoning" reward would be mis-aimed.
- **Confidence (d07, d08):** verbalised confidence after reasoning is better calibrated than before (33 of 36 settings). P(IK) in a 52B model rises with relevant text (obscure question 18%, with the relevant Wikipedia article 78%), so ratings move with context. No test changes only distractors and reads a difficulty rating.
- **Expertise reversal (d09, d10, d15):** GPT-3.5 simulated learners reproduce it, but expertise is a persona (He-Yueya 2024; agreement with human teachers r=0.661, n=56 teachers). Over-prompting: extra shots hurt strong and weak models alike. No direct test by model strength.

### 6.4 Summary of what changed results, by how much

| Change | Effect | Source |
|---|---|---|
| 80% distractors (capable model) | -13 points (0.85 to 0.72) | Adapala |
| Length-matched filler | -3 points, ns | Adapala |
| Length 250 vs 20 | most models to 0.20-0.30; best 0.68-0.76 | CogniLoad |
| Context 1K to 32K, retrieval | GPT-4o -28 points; Claude 3.5 Sonnet -55 points | NoLiMa |
| Add 3 constraints to chained task | -22.5 points (o4-mini) | Mittal |
| Constraint reminder | +12.7 to +17.7 points compliance | Mittal |
| Pick shortest of k chains | up to +34.5 vs longest | Hassid |

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5. Status: [E] established, [S] single-source, [C] contested. Claim ids K01..K26 are in claims.jsonl.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | **Do not add a germane-load operator or an effort reward.** The theory's own authors removed it as an additive load. Add one line to section 4b: "Germane load / effortful-length reward." | 4b (not-to-add) | [E] | K02, K22; a08, b18, d05, d06 |
| N2 | **Never sum load types into one budget or give the agent three load dials.** Log counted quantities separately (needed items, length, distractor ratio, failed-step fraction, output tokens). | G (wording under G11/G12) | [E] for the concept problem (3 sources: de Jong, Sweller 2019, Skulmowski and Xu); additivity itself untested [S] | K01, K02, K03; a01, a08, a22 |
| N3 | **Do not use a self-reported effort or difficulty score as a gate unless calibrated.** Ratings often fail to track what instruction changes (about 14 studies) and overlap with plain effort. Agrees with G10 and 4b (verbal confidence). | G10 note | [E] for human ratings; LLM leak untested | K09, K23; a06, b06, b10 |
| N4 | **Do not reward or trust long reasoning as a sign of success.** Shortest chain beats longest; log failed-step fraction instead. | G11 (strengthen) | [E] | K22; d05, d06 |
| N5 | **Weak backbones need decomposition and context hygiene more than strong ones.** Capacity falls with difficulty and length, far faster for weak models. Gate the scaffold on model strength. | G12, S0 | [E] | K14; a25, c01, c02, a23 |

### Test first (not established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Strip irrelevant context in S1 input hygiene (graded loss with distractors on capable models; weak models at a floor). | S1 | [S] | K12, K21; a23, d03 |
| T2 | Do not assume linear distractor harm; sweep 5 levels. | G (context hygiene) | [C] | K13, K21; c03, d03 |
| T3 | Interaction among difficulty, length, distractors at fixed output tokens: if present, budget by class (S0), not by a sum. | G12, S0 | [S] | K03, K20; d01, d11 |
| T4 | Constraint reminder step before the final answer (S8). | S8 | [S] | K17; b26, d11 |
| T5 | Late-confidence read only (after reasoning), never a pre-reasoning self-rating. Leak test with distractor-only changes. | G10, S0 | [S] | K23; d07, d08, d16 |
| T6 | Examples or restatement only after a per-model check (expertise-reversal analogue). | S1, S2 | [S] | K24, K11; d09, d10, a21 |
| T7 | Safety check re-run on the final step of any stacked task. | G | [S] | K18; b23 |
| T8 | CLT-style decomposition prompts (CLAI, CoThinker) against plain "be brief" and plain CoT at equal tokens. | O3, G11 | [C] | K16, K26; c06, b21 |
| T9 | Log failed-step fraction as a within-run signal for S6 impasse firing. | S6, section 6 logs | [S] | K22; d06 |
| T10 | If a split is ever needed, use task-necessary vs wasted, not three labels. | none | [C] | K07; a15, a17 |

## 8. Concrete tests on our bench

All arms use equal total tokens (input plus output) unless stated. Report accuracy and accuracy per 1k tokens. Use at least 100 items per cell and 3 seeds for cells above a floor; bootstrap CIs.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | CogniLoad-style puzzles, full factorial d (1,3,5,7) x N (20,50,100) x rho (5,25,50,75,95) | One arm per cell; same model; output cap fixed | Logit model with and without product terms (AIC, likelihood ratio) | Products non-zero: d01 hints at a d*rho interaction. If the main-effects model wins, a summed budget is acceptable |
| B2 | Multi-hop QA (ICE-style) at 0/20/50/80% irrelevant text vs length-matched neutral filler | plain vs plain + S1 hygiene (strip distractors in code) | Accuracy, hop recall | Plain loses about 13 points at 80% (Gemini-like); filler about 3 (ns). Hygiene recovers most of the 13 if stripping is accurate |
| B3 | Same agent on state-tracking (CogniLoad) and retrieval (NoLiMa-style) at 5 distractor levels | plain only | Shape of curve (quadratic term) | U-shape on puzzles, monotone on retrieval. If both U or both monotone, K21 is wrong |
| B4 | Distractor-only change; ask for a 1-10 difficulty rating before and a confidence after reasoning | plain | Rating shift vs accuracy shift; AUROC of each for correctness | Pre-rating rises with distractors although the task is unchanged (leak); post-confidence AUROC higher |
| B5 | Chained GSM8K (N=3,5) plus 0/1/3 format constraints | plain vs plain + reminder before final answer vs full scaffold with S8 verify | Compliance and accuracy | Reminder +10 to +18 points compliance (Mittal); smaller gain when S8 already re-checks constraints |
| B6 | Reasoning-length analysis on existing runs | within-question shortest vs longest vs random | Accuracy gap | Shortest better (Hassid +2 to +16 over random). Also log failed-step fraction vs correctness |
| B7 | GSM8K and MATH subsets | scaffold vs CLAI-style budget prompt vs plain "answer briefly" vs plain CoT, tokens matched | Accuracy per token | CLAI-style about equal to plain "be brief"; if it beats "be brief" by under 2 points, drop the CLT framing |
| B8 | 0/2/8 examples or restatements, strong and weak backbone | plain | Accuracy by model strength | Extras help weak, flat or hurt strong (expertise reversal); hurt both past about 8 shots (d10) |
| B9 | Refused request wrapped in 6 side tasks | plain vs scaffold with final-step safety check | Refusal rate | Plain refusal drops under stacking; final-step check restores it |
| B10 | Scaffold vs plain at d=3,5,7 and N=50,100,250 | plain vs scaffold | Scaffold gain by (d,N) | Gain grows with d for weak backbones, near zero for strong at low d (K14) |

## 9. What does not transfer, and why

- **The three-way split.** Built for human working memory. LLM "load" is computational (CogniLoad authors, a26). We have no learner process analogous to germane load.
- **Questionnaire results.** Reliability, factor structure and correlations (K05 to K10) are about students filling in forms. They say nothing about model internals.
- **Element interactivity as a number.** The count of interacting elements has no validated LLM equivalent. CogniLoad's d (entities, attributes, clauses) is a proxy.
- **Germane = "task length N".** CogniLoad's own mapping, flagged as debatable.
- **Schema building.** CLT germane effort aims at long-term memory. Our agent has no weight updates in-run; memory lessons (section 5 of the schema) are the only analogue.
- **Expertise reversal by learner knowledge.** The agent's "expertise" is fixed by the backbone. Persona-based simulation (d09) is not the same.
- **Attentional residue.** Adapala's residue effect was not significant (p=.12). Do not use.
- **Jailbreak overload.** An analogy only (b23).
- **Felt effort as a learning cue.** Applies to people judging their own learning; our code logs outputs, not feelings.

## 10. Open questions

1. Does any experiment, human or LLM, fit interaction terms between intrinsic difficulty, extraneous material and learning-process load at fixed time or tokens? (gap 1; none found.)
2. Is the CogniLoad interaction real at equal output tokens for frontier reasoning models? (gap 2; descriptive only.)
3. Is the U-shaped distractor response reproduced on retrieval-heavy tasks, or only on state-tracking? (NoLiMa suggests the latter, but varies length, not ratio.)
4. Does a difficulty or effort self-rating leak when only distractors change? (gap 4; no test.)
5. Do CLT-labelled prompts (CLAI, CoThinker) beat plain CoT plus a plain token-budget prompt on tasks they did not choose? (gap 5.)
6. Is there an LLM analogue of expertise reversal by model strength? (gap 6.)
7. What did Park (2010) find, and did it replicate? (gap 7; source blocked, 403.)
8. Does a constraint reminder help when the agent already has a verify state, at equal tokens? (gap 8.)
9. Is any effort-like signal positively related to correctness in modern reasoning models once length is controlled? Length is negative (K22); failed-step fraction is better but needs an LLM annotator.
10. Do the Klepsch two- vs three-factor results change with larger, non-student samples?
11. Do Zu et al. (2021) really show that separation depends on prior knowledge? (not read directly.)

## 11. Sources

[V] = opened and read this session (full text or PDF). [M] = snippet or abstract only.

**Human theory and critique**
- [V] de Jong (2010) Cognitive load theory, educational research, and instructional design: some food for thought. Instr Sci 38:105-134. https://ris.utwente.nl/ws/files/6597420/Jong10cognitive.pdf ; https://link.springer.com/content/pdf/10.1007/s11251-009-9110-0.pdf
- [V] Sweller, van Merrienboer, Paas (2019) Cognitive architecture and instructional design: 20 years later. Educ Psychol Rev 31:261-292. https://link.springer.com/content/pdf/10.1007/s10648-019-09465-5.pdf
- [M] Kalyuga (2011) Cognitive load theory: How many types of load does it really need? Educ Psychol Rev 23:1-19. https://link.springer.com/article/10.1007/s10648-010-9150-7
- [M] Sweller (2010) Element interactivity and intrinsic, extraneous, and germane cognitive load. https://link.springer.com/article/10.1007/s10648-010-9128-5
- [V] Skulmowski and Xu (2022) Understanding cognitive load in digital and online learning. Educ Psychol Rev 34:171-196. https://link.springer.com/content/pdf/10.1007/s10648-021-09624-7.pdf

**Human measurement**
- [V] Krieglstein et al. (2022) Systematic meta-analysis of subjective cognitive load questionnaires. https://link.springer.com/content/pdf/10.1007/s10648-022-09683-4.pdf
- [V] Klepsch, Schmitz, Seufert (2017) Two instruments measuring intrinsic, extraneous, germane load. https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01997/full
- [V] Jiang and Kalyuga (2020) CFA of cognitive load ratings supports a two-factor model. https://www.tqmp.org/RegularArticles/vol16-3/p216/p216.pdf (critique.md lists it as not re-opened; opened in the earlier phase)
- [V] Debue and van de Leemput (2014) What does germane load mean? https://pmc.ncbi.nlm.nih.gov/articles/PMC4181236/
- [M] Leppink et al. (2013) Instrument for measuring different types of cognitive load. https://doi.org/10.3758/s13428-013-0334-1
- [M] Park (2010) dissertation on additivity. https://publikationen.sulb.uni-saarland.de/handle/20.500.11880/23365 (blocked, 403)
- [M] Paas 1992/1994/2003; Zu et al. 2021; Leppink 2014; Zavgorodniaia 2020 (secondhand through the papers above)

**LLM studies**
- [V] Adapala (2025) Cognitive load limits in LLMs (ICE). https://arxiv.org/abs/2509.19517
- [V] Kaiser, Frigessi, Ramezani-Kebrya, Ricaud (2025) CogniLoad. https://arxiv.org/abs/2509.18458
- [V] Shang et al. (2026) United Minds or Isolated Agents? (CoThinker). https://arxiv.org/abs/2506.06843
- [V] Zhang (2025) Cognitive Load-Aware Inference (CLAI). https://arxiv.org/abs/2507.00653 (opened in the earlier phase; not re-opened in the cross-check, carried as [M] in the gap search)
- [V] Mittal (2026) Did you forget what I asked? https://arxiv.org/abs/2603.23530
- [V] Upadhayay, Behzadan, Karbasi (2024) Cognitive overload attack. https://arxiv.org/abs/2410.11272
- [V] Wang et al. (2026) ToolLoad-Bench. https://arxiv.org/abs/2601.20412
- [V] Long et al. (2025) What makes a good natural language prompt? https://arxiv.org/abs/2506.06950
- [V] Modarressi et al. (2025) NoLiMa. https://arxiv.org/abs/2502.05167
- [V] Hassid et al. (2025) Don't overthink it. https://arxiv.org/abs/2505.17813
- [V] Feng et al. (2025) What characterizes effective reasoning? https://arxiv.org/abs/2509.19284
- [V] Yoon et al. (2025) Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221
- [V] He-Yueya, Goodman, Brunskill (2024) Evaluating and optimizing educational content with LLMs. https://arxiv.org/abs/2403.02795
- [V] The few-shot dilemma: over-prompting LLMs (2025). https://arxiv.org/abs/2509.13196
