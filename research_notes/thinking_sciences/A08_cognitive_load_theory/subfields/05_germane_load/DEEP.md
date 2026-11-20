# Germane load: deep document

*Subfield A08.05 of cognitive load theory (CLT). Focus: working memory devoted to building schemas. Key works: Sweller; Paas. Status of the construct: disputed. Built from evidence_a-d.jsonl, claims.jsonl (K01-K21) and critique.md in this folder. Evidence ids (a01, b05, d12 ...) refer to those files.*

## 1. What it is

Germane load was meant to be the part of working memory that goes into learning itself: building and automating schemas (stored patterns in long-term memory that chunk many elements into one). In the 1998 model, total load = intrinsic + extraneous + germane. Intrinsic load comes from the material (element interactivity, given what the learner already knows). Extraneous load comes from how the material is presented. Germane load was the effort that goes into schema building, and it could use spare capacity freed by cutting extraneous load [a01, a25].

Where it stands in 2026:
- Sweller himself says germane load was never generated from data. It was added as a plausible idea. In 25 years there were many extraneous effects, several intrinsic effects and no germane effects [a08, b09].
- The 2019 model (Sweller, van Merrienboer, Paas) no longer treats germane load as a third additive load. It is the share of working memory resources that go to intrinsic load, redistributed away from extraneous activity [a02, b06].
- Critics (de Jong 2010, Kalyuga 2011, Leppink and van den Heuvel 2015) say it is a post hoc label, indistinguishable from intrinsic load, and "never really found support in empirical research" [b11, a10, a14].
- Questionnaire germane scales are reliable but weakly valid (K02, K03).
- No LLM study manipulates germane load directly. LLM papers manipulate length, distractors, tool count or presentation, and the germane label is the authors' mapping (critique, K09-K12).

Plain reading for an engineer: there is no germane knob to tune. What is real is (a) the cost of extraneous and intrinsic load, (b) the value of activities that force the learner to link elements together (integration), and (c) the fact that these only help when total load is within capacity.

## 2. History and theories in depth

**Origins (1980s).** Sweller and Levine (1982): conventional goal problems force means-ends analysis, which uses working memory and has little to do with schema building. Goal-free problems ("calculate as many variables as you can") cut load and focus attention on structure [a04]. Original counts not read.

**1994, the founding germane evidence.** Paas and van Merrienboer (1994) variability result. The prediction: high-variability practice helps transfer when learners study worked examples (low load) and hurts when they solve conventional problems (high load). The format-by-variability interaction was found [a03, b07]. This is the only founding data for the idea that extra effort can be "good load". Cell means were not read (original paper blocked) and no 2024-2026 replication was found (critique gap 10).

**1998.** Sweller, van Merrienboer and Paas: the additive three-load model. Germane load substitutes for extraneous load [a01].

**Measurement era.** Paas (1992) 9-point mental effort scale gives one number (intrinsic plus extraneous) and cannot split load types. One rating after a whole phase runs higher than the mean of per-task ratings [a07]. Leppink et al. (2013) built a 10-item scale with three components and confirmed the structure in three more lectures [a12]. Later scales: Klepsch 2017 (8 items), Leppink 2014, Eysink 2009 [b01, a16].

**Critique era (2010-2015).**
- de Jong (2010): variability gave higher rated load plus better transfer, and that was called germane after the fact. But de Croock et al. (1998) found better transfer without higher rated load. Germane processing can overload (Stull and Mayer 2007: learner-built organisers did worse than author-made ones). Whether load is germane or extraneous depends on expertise and goal (Paas et al. 2004; Gerjets and Scheiter 2003) [b11, b12, b13].
- Kalyuga (2011): germane load is indistinguishable from intrinsic load; added from theory, not from results that needed it [a10, b14].
- Sweller (2010): defines germane as the working memory resources actually used on intrinsic load [b15, a11].
- Leppink 2014 follow-ups (secondary report only): two experiments separated intrinsic from extraneous but "support ... is limited" for the third factor [a13]. Numbers not opened.

**2019 redefinition.** Reason: if germane simply replaced extraneous load, total load would not fall when extraneous load falls, yet many studies show it falls [a02]. Self-explanation prompts and imagination instructions help only if total load stays within capacity and the learner has enough knowledge (Renkl 1998; Cooper et al. 2001) [a05, b08]. Effort is an invalid learning cue (de Bruin and van Merrienboer 2017): learners read high effort as "I learned a lot". A better germane cue is being able to explain the solution to a peer [a06].

**2022 cost-benefit view.** Skulmowski and Xu compare three models: the 1998 additive model, the 2019 model, and a cost-benefit model in which some extraneous load buys germane processing (motivation, immersion). The same information can be extraneous for an expert and intrinsic for a novice. Learning to tell relevant from irrelevant is itself part of the task [a18, a19, b20, b21]. Mayer (2014) made a related point about generative processing.

**2023.** Sweller: replication failures drove the intrinsic/extraneous split. Worked examples failed with geometry and kinematics but worked with algebra. Split attention gave no advantage for self-sufficient text and diagram (Chandler and Sweller 1991), giving the redundancy effect. Failures were traced to element interactivity and expertise reversal [a09, b10, b26]. Chen et al. (2023): element interactivity depends on learner expertise ("dog" is three elements to a novice reader, one to an expert) [a24].

**2020-2026 factor analysis.** Jiang and Kalyuga (2020): 12 items fit a two-factor model when germane items count as extra intrinsic indicators [a15]. Klepsch: three-factor fit is better, but germane is the weakest scale [a16, d14]. Krieglstein 2022 meta-analysis judged the data as supporting three factors while noting correlations that contradict theory [b27].

**Net.** Two live positions: (1) germane is a processing/benefit dimension, not a load (Sweller 2019, Skulmowski and Xu); (2) germane is not needed at all (Kalyuga, Leppink). Nobody argues for the 1998 additive version any more.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| No germane-specific effects were generated in 25 years | Extraneous effects many, intrinsic several, germane none | Sweller 2023 [a08, b09] | Established (author's own statement) |
| Germane scale reliability is high | Pooled alpha ICL .823, ECL .773, GCL .860 (k=42) | Krieglstein 2022 [b01] | Established |
| Germane scale reliability varies by format | GCL alpha natural sciences .872 (k=30), logic and maths .795 (k=5); static .866, dynamic .884, interactive .774 (k=6); 7-point .732 (k=12), 11-point .915 (k=16) | Krieglstein 2022 [b25] | Established |
| Germane ratings weakly predict learning | Leppink scale GCL-retention r=.188 (k=15), GCL-transfer r=.173 (k=12); Klepsch r=.219 (k=7) and .217 (k=6); ECL-retention r=-.114 | Krieglstein 2022 [b02] | Established |
| Germane overlaps with intrinsic in ratings | ICL-GCL r=.403 (k=19, Leppink), r=.533 (k=10, Klepsch); ECL-GCL r=-.086 ns and -.246 | Krieglstein 2022 [b03] | Established |
| Germane rating unrelated to prior knowledge | GCL-PK r=.073 ns (k=15), .014 ns (k=9); Eysink -.193 (k=6) | Krieglstein 2022 [b04] | Established |
| Germane rating tracks engagement, not performance | N=128: GL-performance r=.045 ns; GL-immersion .362; GL-enjoyment .401; GL-temporal dissociation .289; EL-GL -.470 | Debue and van de Leemput 2014 [a17, b19] | Single study |
| Same study: load ratings did not separate versions that differed in performance | N=92, F(2,91)=5.605, eta2=.112; means text+pictures .65, +animations .52, text only .50 (paper prints "p=0.05", a typo; p is about .005) | Debue 2014 [a17, critique] | Single study |
| Naive raters could not separate low and high germane tasks (Study 1) | 4.68 vs 4.88, p=.84; F(1,88)=0.04; N=97 | Klepsch 2017 [a16, b16] | Single study |
| Revised germane scale is still weak | Study 2 GCL alpha .67 (3 items), .85 (2 items); task discrimination d=.35 vs ICL .73, ECL .94 | Klepsch 2017 [b16, d14] | Single study |
| Three-factor model fits better than one factor | Klepsch CFI .970 vs .612 (one factor), .974 for two factors; RMSEA .021 vs .071; AIC 845 vs 2185 | Klepsch 2017 [b17] | Contested (two-factor fits almost as well) |
| Two-factor fit with germane items as intrinsic | N=60, chi2=54.069, df=53, p=.433, CFI .994, RMSEA .018; one item loaded .28 | Jiang and Kalyuga 2020 [a15, b18] | Single small study |
| Drawing supports: integration helps, "germane" and "extraneous" labels do not | 14 studies, 16 comparisons, N=1213; overall comprehension g=0.04 (SE .11, p=.738), transfer g=-0.10 (k=7); moderators germane Q=0.92 ns, extraneous Q=0.00, integration Q=7.90; g=0.35 with integration, -0.15 without | Leutner and Biele 2025 [b05] | Single meta-analysis; author-coded moderators |
| Variability effect depends on load | Interaction of format (worked vs problem) by variability (low vs high) | Paas and van Merrienboer 1994 via review [a03, b07] | Contested; cell means unread |
| Variability helped transfer without higher rated load | Distillery troubleshooting | de Croock 1998 via de Jong [b11] | Single study |
| Learner-built organisers worse than author-made | Direction only | Stull and Mayer 2007 via de Jong [b12] | Single study |
| Self-explanation and imagination help only within capacity | Self-explanation prompts beat plain examples if load within capacity; imagination beats study only after expertise | Renkl 1998; Cooper 2001 via review [a05, b08] | Established as a pattern (expertise reversal) |
| Single end-of-phase effort rating higher than mean of per-task ratings | Direction only | van Gog et al. via review [a07] | Established |

## 4. Mechanisms and models

Each model below is written so it can be turned into code or a prompt rule.

**M1. 1998 additive model.** load_total = IL + EL + GL; capacity C. Learning needs IL + EL + GL <= C, with GL filling spare room. Prediction: cut EL, then spend the savings on GL. Problem: nobody can measure GL separately, so the prediction cannot fail [a01, a25].

**M2. 2019 redistribution model.** load_total = IL + EL. GL is not a term. It is the fraction of resources working on IL. Cutting EL frees resources; whether they go to IL is the "germane" part [a02, a25]. For an agent: remove distractors from context, and also make sure the remaining steps work on the task, not on housekeeping.

**M3. Cost-benefit model (Skulmowski and Xu).** benefit = processing that builds schemas (driven by motivation and engagement); cost = IL + EL. Some EL is worth paying if it buys benefit. Decision rule: keep an extra feature only if it raises outcome at equal total cost [a18, b20, b21].

**M4. Capacity gate (expertise reversal).** Helpful activity A (variability, self-explanation, worked steps) has benefit b(A, k) for a learner with knowledge k and cost c(A). Net effect = b(A, k) minus an overload penalty when IL + EL + c(A) > C. The same A helps low-knowledge learners with low IL and hurts high-load or high-knowledge ones (redundancy) [b07, b08, b13]. Engineer reading: every scaffold stage needs an on/off condition that depends on item difficulty and model strength (K06, K08, K19).

**M5. Element interactivity.** Count of elements that must be held and processed together. Depends on the solver's knowledge: chunked knowledge reduces the count [a11, a24]. Not validated as a per-task LLM measure (K16). Candidate implementation: ask a strong model to list interacting sub-facts for a task, score the count, check it against failure rate.

**M6. Load proxies for LLMs (not germane measures).**
- CogniLoad: length N for sustained maintenance, difficulty d for intrinsic load, needle-to-hay ratio for extraneous. Logistic regression on d, log10 N, quadratic in the ratio; capacity indices ECL50, NT50, ID50 [a21, a22, c04].
- ToolLoad: accuracy = exp(-(k * CL_total + b)), intrinsic = tool interaction graph complexity, extraneous = ambiguity and distractor tools. Weights are author-set, so the fit is partly by construction [a23, c09].
- CoThinker: attention entropy and perplexity as load proxies [c06].
- CLAI: GCL_LLM = share of generated tokens with high attention weight; ECL = low-attention context tokens; token budget set from an intrinsic estimate. No test that attention weight equals schema building [c11, c12].

**M7. Difficulty-adaptive gating.** A probe on the model's hidden state routes each question to an Easy, Normal or Hard strategy (DiffAdapt). Alternative: cascade, try cheap, run a check, escalate on fail [d01, d02, d12]. Implementation of the cascade: run plain; if the code check fails or samples disagree, enable the heavier scaffold stage.

**M8. Integration step.** A step that forces the solver to link given elements (a drawing that maps text to picture; a self-explanation naming why a step follows). Humans: g=0.35 with integration support vs -0.15 without [b05]. Implementation: a state that must output explicit links between elements, with a length-matched control that lacks the links (K05, K18).

## 5. What holds up

**Holds up (human).**
- Reducing extraneous load works (many effects; split attention, redundancy, worked examples). Details live in sibling documents of A08 and Sweller 2023 [b09, b10].
- Support only helps when total load is within capacity, and the same support reverses for experts [b07, b08, b13] (K06, established, two independent sources).
- Explicit integration support beats generic "load-raising" support (single meta-analysis) [b05].
- Germane questionnaire scales are internally consistent (alpha .86) [b01].

**Does not hold up.**
- Germane load as a separate, measurable, additive load. Sweller dropped it; no germane effects found [a08, b09] (K01).
- Germane scale validity: r=.17-.22 with learning, .40-.53 with intrinsic load; tracks immersion and enjoyment; naive raters did not separate tasks [b02, b03, a17, b16] (K02, K03).
- "Increase germane load" as an intervention: moderator ns in the drawing meta-analysis (Q=0.92) [b05].
- Learner effort as a cue: invalid [a06].

**Failures and boundary conditions.**
- Worked examples failed for geometry and kinematics but worked for algebra; split-attention integration failed when text and diagram were each self-sufficient [b10, b26].
- Variability: better transfer without higher rated load (de Croock) contradicts the germane reading [b11].
- Self-generated structure (Stull and Mayer) worse than supplied [b12].
- Interactive media lowered GCL reliability (.774) [b25].
- Factor structure is contested: Jiang and Kalyuga two-factor fit vs Klepsch three-factor fit [a15, b17].

**Moderators.** Learner expertise (strongest), element interactivity, whether total load is under capacity, whether the support forces integration (author-coded, overlaps with the germane coding in Leutner and Biele) [b05, critique].

**Interventions that worked.** Self-explanation prompts on worked examples (within capacity); goal-free problems; variability with worked examples; integration-forcing drawing support; explain-to-a-peer as a learning check [a04, a05, a06, b05].

**Interventions that did not.** Generic "raise germane load" supports (g=0.04); mere effort; learner-built organisers (Stull and Mayer); questionnaire-guided design relying on GCL.

**Evidence quality limits.** Many evidence lines duplicate one paper; independent source counts count papers, not lines. Leppink 2014 and Kalyuga 2011 numbers were never opened. The founding studies (Sweller and Levine 1982; Paas and van Merrienboer 1994; Renkl 1998; Cooper 2001; de Croock 1998; Stull and Mayer 2007) are known only through reviews. No 2024-2026 human replication of the variability-by-format interaction was found (critique gap 10, not searched).

## 6. Language models

No study manipulates germane load on a model. Evidence below is from papers that map CLT onto LLMs loosely, plus analogues. Everything here holds for the models and tasks named; none is token-matched against a germane control unless stated.

**Load degrades accuracy.**
- CogniLoad (22 reasoning models): length N is the dominant stressor. N=20 to 50: DS-Llama-70B .89 to .66; Qwen3-8B .71 to .40; gpt-5 1.00 to .98. At N=250 only gpt-5 (.76) and o3 (.68) pass 50%. d=1 to 3: o3 .96 to .93; gpt-5 1.00 to .97; weaker models drop .10-.25. By d=5, 12 of 22 models are below 50%. At d=10: gpt-5 .82, o3 .80, weakest .10-.15. Distractor ratio gives a U-shape, not a monotone drop. Frontier models have only 10 puzzles per config, so their numbers are noisy. N is confounded with load [a21, a22, c01-c04] (K09, single source).
- Multi-hop retrieval (Adapala 2025): Gemini-2.0-Flash EM .85 control, .82 long control, .82 at 20%, .78 at 50%, .72 at 80% filler; slope -0.003 per % (95% CI -.004 to -.002); GPT-4o slope ns (p=.07); three open models at 0.00 even on clean input. 200 questions, 10 replications, 5 models [b22] (K10).
- Tool use (ToolLoad): overall xLAM2-32B 78.8, GPT-4o 68.0, Qwen3-8B 38.6; decay rate k from 0.034 (xLAM2) to 0.088 (Gemini 2.5 Pro) [a23, c09] (K11).
- Working memory: ChatGPT n-back d' falls to about 1 at n=3; CoT raises scores but the limit persists; small transformers show attention entropy rising with n [c18, c19] (K15).
- Overload attack: stacking tasks and distractors raised attack success to 99.99% (Claude-3-Opus), 90.95% (GPT-4), 89.22% (GPT-4-Turbo), 84.05% (Gemini-1.5-Pro) on forbidden questions [c15-c17] (K17).
- Extraneous-load benchmark (Gupta 2026, CogLoadBench): higher extraneous load lowers accuracy; steering activations to low-load directions helps. Snippet only, no numbers [b23].

**Scaffolds that cut load or add structure.**
- CLAI-Prompt (Llama-3-70B): GSM8K 92.3 vs 92.5 CoT at 310 vs 485 tokens (-36.1%); MATH 53.5 vs 53.9 at 525 vs 812 (-35.3%). LongBench QA (Llama-3-8B) F1 69.3 at 980 tokens vs LLMLingua 68.1 vs full context 65.2. Accuracy differences are within noise; the germane attention-weight rationale is untested; unreplicated [b24, c11, c12] (K12).
- Chain of Draft (5 words per step): date understanding GPT-4o CoT 90.2 vs CoD 88.1; Claude 3.5 Sonnet CoT 87.0 vs CoD 89.7; sports on Claude tokens 189.4 to 14.3; as low as 7.6% of CoT tokens [d13]. Length is not the active ingredient on these tasks.
- CoThinker (multi-agent CLT design): LiveBench Flash-8B Math 33.8 to 37.7, Language 16.1 to 29.4, Instruction following 84.3 to 68.1; Pro Math 60.9 to 75.3; GPT-5 reasoning 68.38 to 81.88. 16 of 25 Holm-corrected comparisons significant; the three significant losses are instruction following. Shared-memory ablation is mixed: Qwen3-30B 81.87 with vs 76.41 without; GPT5-Nano 55.97 vs 62.36; GPT-OSS-20B 57.15 vs 58.37. Pilot proxies: attention entropy 4.44/4.80/5.04 by difficulty; hard-task PPL 120.50 to 88.97 to 85.35 with richer instructions, easy-task PPL 3.37 to 3.45. No verified token-matched single-agent control [a20, c05-c08] (K13, contested).

**Support hurts when the task is easy (expertise reversal analogue).**
- AdaptMI: skill-based examples cost 5 small models an average of 4% on easy MATH questions; cells down to -10.3 and -8.7 points (Qwen2.5-1.5B). Giving them only on hard questions gains up to 3.6%, and with iterative skill targeting (AdaptMI+) up to 6% Pass@1 [c13, c14] (K08).
- DiffAdapt (1.5B-8B models): token saving vs Normal 22.4% (Qwen3-4B), 9.7% (R1-Qwen-7B), 10.1% (ThinkPrune-7B). Oracle on Qwen3-4B: MATH 98.0 at 1279 tokens vs 96.2 at 2662; GPQA 70.20 at 1001 vs 50.51 at 3022; AIME24 66.67 at 4429 vs 60.00 at 10672. Applying Easy to hard items loses heavily (AIME25 16.67 vs 53.33) [d01, d02] (K21).
- Scaffold benefit falls with stronger models: multi-agent gain over single agent HumanEval +10.7 to +3.0, MBPP +16.0 to +1.2; a cascade beats both; multi-agent used 4-220x more prefill tokens [d12]. CoT hurt: implicit statistical learning GPT-4o direct 94.00 vs o1-preview CoT 57.70 (a 36.3-point drop on 440 problems; full set GPT-4o 87.5 to 64.4, Claude 3.5 Sonnet 65.9 to 67.7, no drop) [d10]. Plain models beat reasoning models at low complexity, reasoning wins at medium, both collapse at high (abstract only) [d11]. CoT meta-analysis: gain mainly on math and symbolic tasks [d09] (K19, contested).

**Length vs content.**
- Same-length filler gave no gain (Lanham 2023) [d06]. Filler helps only in small models trained with dense supervision (Pfau 2024) [d07]. Longer demonstration steps without new content raised accuracy for GPT-3.5-era models (Jin 2024; zero-shot baseline numbers look odd, treat as unverified) [d08]. Net: content matters, length alone mostly does not (K18, contested). The integration step itself is untested.

**Debate and revision.**
- Five debate frameworks on 9 benchmarks usually fail to beat single-agent CoT or self-consistency; GSM8K GPT-3.5 self-consistency 85.3 at 6 responses vs debate 83.2; mixing different models helps (Heter-SoM +6.4%, Heter-EoT +8.2% over the two-model average) [d03-d05] (K20, established).

**Human-AI learning (not agent-facing).**
- Bastani 2025 PNAS RCT, nearly 1,000 students: GPT Base practice +0.137 (48%), exam -0.054 (17%, p<.05); GPT Tutor practice +0.361 (127%), exam -0.004 (ns). The guardrailed tutor prevented harm but gave no gain. Dispersion fell in practice and returned on the exam [c24, d15, d16] (K14).
- Taneja 2026, N=124: post-test F(2,121)=4.60, p=.012, eta2=.071; multimodal beat text-only conversational by 0.69 (p=.010) on a 10-item MCQ; conversational felt easier and more engaging yet scored lowest [c21, c22].
- Kosmyna 2025 EEG: connectivity fell with external support; only 18 completed session 4 [c23].
- Prism: clarification questions ordered by dependency; logical conflicts 11.5%, satisfaction +14.4%, completion time -34.8% (reported figures only) [c25].

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Do not build a germane budget or score.** No germane knob exists; self- or model-rated germane scores track effort, not understanding. Schema part: none; add to section 4b "not to add". [E] K01, K02, K03; a08, b09, b01-b04, a17.
2. **Gate every helper stage on difficulty or on a failed check.** Support helps below capacity and hurts above it or when the task is easy. Schema part: G12 and S0, with a per-stage off switch. [E for small and mid models; frontier unverified] K06, K08; b07, b08, b13, c13, c14, d01, d02, d12.
3. **No revision or debate stage without an external verifier; compare against self-consistency at the same budget.** Schema part: G2, G9 (already present; this adds weight). [E] K20; d03, d04, d05.
4. **Keep the learning-critical step in the main loop (human-facing only).** Do not let a helper do the integration for the user. Schema part: G note for human-facing tools, not an agent score. [S] K14; c24, d15, d16.

### Test first

5. **Explicit integration step beats a length-matched elaboration step.** Schema part: O3 decompose and S2 represent (a state that writes links between elements). [S] K05, K18; b05 (humans only), d06, d13. Not yet tested on LLMs.
6. **Cascade gate (try cheap, check, escalate) vs always-on scaffold at equal tokens on frontier models.** Schema part: S0, G12. [S] K21, K19; d01, d02, d12.
7. **Cap step count per sub-task and decompose beyond it (chunking).** Schema part: S0, O3. [S] K09, K15; a21, a22, c01, c18.
8. **Element-interactivity score as an S0 difficulty signal.** Schema part: S0, memory (per-class record). [S] K16; a11, a24. Compare against token length.
9. **Compress reasoning text (short drafts) to save tokens at equal accuracy.** Schema part: G11. [S] K12, K18; b24, c11, d13.
10. **Multi-agent decomposition with shared memory,** only against a token-matched single-agent schema baseline. Schema part: S3 (conflicts with G9 unless it passes). [C] K13; a20, c05-c08, d03, d12.
11. **Supplied vs self-generated intermediate structure.** Schema part: S2. [S] K07; b11, b12.
12. **Distractor stripping and an overload guard in S1 input hygiene.** Schema part: S1, G. [S] K10, K17; b22, c15-c17.

## 8. Concrete tests on our bench

All arms at equal total tokens (count setup tokens, G7). Report accuracy per difficulty bucket (easy, medium, hard), not only the mean.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-like and BrainTeaser items with a checkable answer | A: plain; B: plain plus a length-matched elaboration with no explicit links; C: plain plus a forced "link the elements" step | Accuracy at equal tokens; paired test C vs B | C > B by 2-5 points on hard items if integration matters; B about equal to A (K18) |
| T2 | Mixed easy and hard items from one benchmark | A: always-on scaffold; B: no scaffold; C: cascade (cheap, check, escalate) | Accuracy and tokens per item by bucket | C >= A on hard, C >= B on easy; token saving 10-20% (DiffAdapt range) |
| T3 | Same scaffold on a model ladder (small, mid, frontier) | scaffold on vs off per model | Accuracy delta per model and bucket | Delta shrinks with stronger model; locate the crossover (K19) |
| T4 | Synthetic tracking puzzles (CogniLoad style) at N = 20, 50, 100, 250 | A: single pass; B: chunked with a running summary every k steps | Accuracy per N | B holds accuracy at N=50-250 if the N=20-50 drop is a chunking limit |
| T5 | Items scored for element interactivity (strong model lists interacting elements) | Predict failure from (a) interactivity count, (b) token length | Correlation or AUC with plain-model failure | Interactivity beats length if AUC gap > 0.05 |
| T6 | Same items as T1 | Compressed short-draft reasoning vs full CoT | Accuracy and tokens | Accuracy within 1 point, tokens 30% or more lower (CLAI, CoD) |
| T7 | Multi-step items | A: one agent with schema; B: split agents with shared memory; C: self-consistency at equal calls | Accuracy | If B <= C, drop B (G9) |
| T8 | Reasoning with a given outline | Supplied outline vs model-built outline vs none | Accuracy at equal tokens | Supplied >= self-built (Stull and Mayer analogue) |
| T9 | Items padded with irrelevant context (0, 20, 50, 80%) | no filter vs code-side filter (S1 hygiene) | Accuracy slope per % filler | Filter flattens the slope (Adapala slope -0.003 per %) |
| T10 | Agent self-report ("I understood") vs outcome | Correlate stated understanding or token effort with correctness beyond length | Partial correlation | Expect near zero (K03 analogue); if so, never use self-ratings as a gate |

## 9. What does not transfer, and why

- **Germane load as a feeling or rating.** LLMs have no learning step at inference time; weights do not change, so there is no schema construction to be germane to. Upadhayay et al. define in-context "learning" as executing the task given the prompt [c17]. Only in-context pattern use remains.
- **Spare-capacity logic.** Humans have a fixed working memory; a transformer's context is large and degrades gradually (U-shaped distractor curve, no clean cliff) [c03]. Capacity is task and model dependent, not a constant.
- **Questionnaires.** Subjective ratings (Paas, Leppink, Klepsch) have no direct analogue. Model self-reports of effort are not evidence (G10).
- **Motivation and engagement.** Much of the "germane" signal in humans is enjoyment and immersion [a17, b19]. Models have none; this part is dropped.
- **Learner expertise reversal as a stable trait.** Model strength varies per task; the crossover must be measured, not assumed [d10-d12].
- **Attention weight as germane proxy (CLAI).** Not validated even in the paper [c12].
- **Human-AI learning harm (Bastani, Kosmyna).** About humans offloading, not about agent reasoning. Only the design rule transfers to human-facing tools.
- **Variability with worked examples.** A human transfer benefit; for few-shot in-context examples the only relevant evidence is that skill-based examples can hurt on easy items [c13].

## 10. Open questions

1. Does forcing an explicit integration step beat a length-matched elaboration at equal tokens in LLMs? (Humans g=0.35 vs -0.15.)
2. Does an adaptive gate beat always-on scaffolding on frontier models? (Evidence only on 1.5B-8B and older models.)
3. Where is the expertise-reversal crossover for one scaffold on a model ladder?
4. Does CoThinker survive a token-matched single-agent baseline?
5. Can element interactivity be scored per task and predict LLM failure better than length?
6. Is the CogniLoad N=20-to-50 drop a working-memory-like limit that chunking removes?
7. Do Leppink 2014 numbers and 2023-2026 scale validations show the same weak GCL validity? (Not checked.)
8. Do self-generated structures help or hurt LLMs at equal tokens?
9. What is the agent analogue of preventing offloading of the learning step? (Tentative: keep the integration step with the main loop.)
10. Do 2024-2026 human replications of the variability-by-format interaction exist, and what are the cell means?
11. Is the redistribution idea (cut extraneous so resources go to the task) testable in LLMs apart from simply shortening context?

## 11. Sources

[V] opened (page or PDF text read), [M] snippet, abstract or secondary report only.

**Theory and critique**
- [V] Sweller, van Merrienboer and Paas (2019) Cognitive Architecture and Instructional Design: 20 Years Later. https://link.springer.com/content/pdf/10.1007/s10648-019-09465-5.pdf
- [V] Sweller (2023) The Development of Cognitive Load Theory: Replication Crises and Incorporation of Other Theories. https://link.springer.com/content/pdf/10.1007/s10648-023-09817-2.pdf
- [M] Kalyuga (2011) How many types of load does it really need? (abstract and references only). https://link.springer.com/article/10.1007/s10648-010-9150-7
- [M] Sweller (2010) Element interactivity and intrinsic, extraneous and germane load (abstract only). https://link.springer.com/article/10.1007/s10648-010-9128-5
- [V] de Jong (2010) Cognitive load theory, educational research, and instructional design: some food for thought. https://link.springer.com/content/pdf/10.1007/s11251-009-9110-0.pdf
- [V] Leppink and van den Heuvel (2015) The evolution of cognitive load theory and its application to medical education. https://link.springer.com/content/pdf/10.1007/s40037-015-0192-x.pdf
- [V, intro only] Chen et al. (2023) Element interactivity as a measure of task complexity. https://link.springer.com/content/pdf/10.1007/s10648-023-09782-w.pdf
- [V] Skulmowski and Xu (2022) Understanding cognitive load in digital and online learning. https://link.springer.com/content/pdf/10.1007/s10648-021-09624-7.pdf

**Measurement**
- [V] Leppink et al. (2013) Development of an instrument for measuring different types of cognitive load. https://link.springer.com/content/pdf/10.3758/s13428-013-0334-1.pdf
- [M] Leppink et al. (2014) follow-up (via Leppink and van den Heuvel 2015). Numbers not opened.
- [V] Klepsch, Schmitz and Seufert (2017). https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01997/full
- [V] Debue and van de Leemput (2014) What does germane load mean? https://www.frontiersin.org/articles/10.3389/fpsyg.2014.01099/full
- [V] Jiang and Kalyuga (2020) CFA of cognitive load ratings. https://www.tqmp.org/RegularArticles/vol16-3/p216/p216.pdf
- [V] Krieglstein et al. (2022) Meta-analysis of reliability and validity of cognitive load questionnaires. https://link.springer.com/content/pdf/10.1007/s10648-022-09683-4.pdf
- [V] Leutner and Biele (2025) Without integration, everything is nothing. https://link.springer.com/content/pdf/10.1007/s10648-025-10067-7.pdf

**Founding studies, known only through the reviews above [M]:** Sweller and Levine (1982); Paas (1992); Paas and van Merrienboer (1994); Chandler and Sweller (1991); Renkl et al. (1998); de Croock et al. (1998); Cooper et al. (2001); Stull and Mayer (2007); de Bruin and van Merrienboer (2017); Mayer (2014).

**LLM and AI studies**
- [V] Kaiser et al. (2025) CogniLoad. https://arxiv.org/abs/2509.18458
- [V] Shang et al. (2026, TMLR) CoThinker. https://arxiv.org/abs/2506.06843
- [V] Wang et al. (2026) ToolLoad. https://arxiv.org/abs/2601.20412
- [V] Zhang (2025) CLAI. https://arxiv.org/abs/2507.00653
- [V] Adapala (2025) Cognitive load limits in LLMs. https://arxiv.org/abs/2509.19517
- [M] Gupta, Liu and Zou (2026) CogLoadBench. https://neurips.cc/virtual/2026/poster/150343
- [V] He et al. (2025) AdaptMI. https://arxiv.org/abs/2505.00147
- [V] Upadhayay et al. (2024) Cognitive Overload Attack. https://arxiv.org/abs/2410.11272
- [V] Gong, Wan and Wang (2024) Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731
- [V] Gong and Zhang (2024) Self-attention limits working memory capacity. https://arxiv.org/abs/2409.10715
- [V] Taneja, Singh and Goel (2026). https://arxiv.org/abs/2604.02221
- [V] Kosmyna et al. (2025) Your Brain on ChatGPT. https://arxiv.org/abs/2506.08872
- [V] Bastani et al. (2025) PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/
- [V, reported figures only] Liao et al. (2026) Prism. https://arxiv.org/abs/2601.08653
- [V] Chen et al. (2025) DiffAdapt. https://arxiv.org/html/2510.19669v3
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Lanham et al. (2023) Measuring faithfulness in CoT. https://arxiv.org/abs/2307.13702
- [V] Pfau, Merrill and Bowman (2024) Let's think dot by dot. https://arxiv.org/abs/2404.15758
- [V] Jin et al. (2024) Impact of reasoning step length. https://arxiv.org/abs/2401.04925
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183
- [V] Liu et al. (2024) Mind your step (by step). https://arxiv.org/abs/2410.21333
- [M] Shojaee et al. (2025) The illusion of thinking (abstract). https://arxiv.org/abs/2506.06941
- [V] Gao et al. (2025) Single-agent or multi-agent systems? Why not both? https://arxiv.org/abs/2505.18286
- [V] Xu et al. (2025) Chain of Draft. https://arxiv.org/abs/2502.18600
- [M] Sirbu et al. (2025), Guidroz et al. (2025): named in the ToolLoad reference list only.
