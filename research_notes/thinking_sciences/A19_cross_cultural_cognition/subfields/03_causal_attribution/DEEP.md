# Causal attribution: deep document

*Subfield A19.03, under A19 Cross-cultural cognition. Focus: situational vs dispositional explanations. Key work: Nisbett, Peng, Choi and Norenzayan 2001 (not opened this run, see 11). Why it matters for our agent: background only. Evidence files in this folder: evidence_a-d.jsonl (ids a01-a28, b01-b25, c01-c29, d01-d19), claims.jsonl (K01-K26), critique.md.*

Reading note. Most classic cultural results here come from review descriptions, not from the original papers. Where numbers are missing, that is a gap in our reading, not a finding. Status tags: [E] established, [S] single source, [C] contested.

## 1. What it is

Causal attribution is how people explain why something happened. The core split is simple. A cause can sit inside the actor (a disposition: trait, attitude, ability, effort) or outside (the situation: constraints, pressure, task difficulty, luck, other people).

Three terms matter.

- **Fundamental attribution error (FAE, Ross 1977).** Seeing behaviour as caused by matching dispositions even when obvious situational constraints leave little room for dispositions (a02).
- **Correspondence bias (Gilbert and Malone 1995).** The narrower, preferred name. People infer an attitude or trait that matches the observed behaviour even when the behaviour was constrained (b05). It is a claim about inference, not about explanation.
- **Actor-observer asymmetry (Jones and Nisbett 1971).** Actors blame the situation for their own acts; observers blame the actor's disposition (a04).

The cross-cultural claim (Nisbett et al. 2001 and earlier work) is that East Asians read behaviour as an interaction of disposition and context, while Americans read it as the direct unfolding of dispositions (a17, b07). The picture that survives is narrower. The classic bias appears in every culture tested. Cultures differ mainly in how much a visible situational constraint pulls the judgment back (a08, a09, b04, d05, d06).

Why this is only background for our agent. Our agent is one language model run through a scaffold. It has no culture, no self-construal and no stakes. The parts that can matter are (1) how a model attributes causes when it explains failures, including its own, (2) whether label or identity cues bias its judgment of evidence, and (3) whether a cheap check step reduces such bias. Nothing in this subfield is currently in SCHEMA.md and little qualifies.

## 2. History and theories in depth

**Heider 1958.** Naive psychology. Behaviour is explained by internal causes (ability, effort) or external ones (task difficulty, luck) (a04).

**Jones and Davis 1965 and Kelley 1967.** Jones and Davis: correspondent inference from choice, expectedness and effects. Kelley: covariation of consensus, distinctiveness and consistency. McArthur 1972 followed, not covered by our sources (a04). Weiner added locus, stability and controllability.

**Jones and Harris 1967.** The founding paradigm. Readers saw an essay or speech (marijuana, Castro) that the writer was told to write. Readers still inferred the writer held the view. Pro-Castro writers were rated more pro-Castro even when a coin toss assigned the position (a01, b10). We did not open the original. No N or effect size was recorded.

**Ross 1977.** Names the FAE and puts it at the centre of lay psychology (a02). Ross 2018 later says the illusion of superior personal objectivity now outranks it as the "truly fundamental" error (b09, snippet only).

**Jones and Nisbett 1971, Storms 1973.** Actor-observer asymmetry. Storms 1973 showed salience matters: whoever is perceptually salient gets more dispositional credit (b10).

**Gilbert, Pelham and Krull 1988 and Gilbert 1989.** Anchor-and-adjust. People first infer a disposition quickly, then adjust for the situation with effort. Cognitive load blocks the adjustment, so the bias grows (a12, b10). Mason and Morris call the evidence for the two-stage model "remarkably thin". Krull 1993 found that perceivers with a situational goal also failed to discount under load (a12, a16).

**Gilbert and Malone 1995.** Four sources of the bias: unawareness of the situation, unrealistic expectations of behaviour, inflated categorisation, incomplete correction (b05).

**Morris and Peng 1994.** Heider-Simmel style fish animations: Chinese viewers leaned on the group (situation), Americans on the fish's own dispositions. No difference for physical events (circle and rectangle). Newspaper study: Chinese papers and Chinese students explained murders by situation and society; American ones by presumed disposition. Reporter culture mattered, perpetrator nationality did not (a06, a07). No N or effect sizes obtained.

**Choi and Nisbett 1998, Choi, Nisbett and Norenzayan 1999.** Koreans, like Americans, inferred the attitude from a constrained essay. When the constraint was made salient (the essay closely echoed the instructions, or the observer first wrote such an essay), Koreans' bias fell and Americans' did not (a08, a09). Review description only.

**Miyamoto and Kitayama 2002.** The gap is conditional. If the constrained behaviour is still diagnostic of the attitude, Americans and Japanese show equal bias. If it is minimally diagnostic, Americans keep a strong bias and Japanese show none (b04). Mediated by explicit inferences made online. Abstract only.

**Masuda and Kitayama 2004; Knowles et al. 2001; Lieberman et al. 2005; Hedden et al. 2008.** Load and automaticity studies. Under load Americans stay dispositional while Hong Kong participants' situational correction is not disrupted (Knowles). Lieberman: under load both groups impute stressful topics alike; under low load US participants grow less confident in situational attribution and East Asians more. Hedden: culture-inconsistent judgments recruit more control regions (a11, a13, a14, a15, d08). All from the Mason and Morris review.

**Norenzayan, Choi and Nisbett (manuscript of the 2002 PSPB paper).** Opened with real numbers (d05-d07). Koreans endorse dispositionism as much as Americans, and situationism more. Section 3 has the numbers.

**Peng and Nisbett physical-event work; Masuda and Nisbett 2001.** Chinese read ambiguous physical events through the medium (water); Americans through object properties. Japanese recalled far more background of fish scenes with equal focal detail (a18, a19). Bender and Beller 2011 found the "one object is the cause" habit across Germans and Tongans, with direction depending on content (b21).

**Hong et al. 2000 priming.** Bicultural priming shifts attribution within a person, which argues for flexible culture-as-knowledge, not fixed essence. Talhelm et al. 2025 replicated it in young Chinese (a20-a22, a27).

**Spontaneous trait inference.** Na and Kitayama 2011: European Americans show spontaneous trait inference, Asian Americans do not, mediated by independent self-construal (b06, snippet). The 2022 meta-analysis found no significant culture moderation (a23).

**Critiques.**
- Malle 2006 meta-analysis: the actor-observer asymmetry is about zero on average (b01, b02, b03).
- Walker, Smith and Vul 2015: the "error" looks like error only against an unfair benchmark; people may track real correlations (a03, b10, via Wikipedia, not opened). Epstein is cited the same way.
- Bohm and Pfister 2015: person vs situation is too coarse; goals, states and events form a chain of lay explanation (a05).
- Gill et al. 2014: individual beliefs about history and social forces (historicism) moderate the FAE, dispositionism does not (b12, b13).
- Culture-as-essence critique: the Greek vs Chinese intellectual-history account is called "highly speculative" by its own authors (a17).

## 3. Core findings with exact numbers

Status uses the tags from the top. "Human" means a human study; LLM results are in section 6.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Correspondence bias under coercion in modern samples (affirmative-action essay) | Position effect with free choice t(84)=9.29, d=2.0; no choice t(84)=3.83, d=.84. Position x choice t(73)=4.00 | Gill et al. 2014, Study 5 (b12) | [E] |
| Coerced essays still shift attributed attitude (moral topics) | Study 1: pro M=1.98 vs anti M=-1.04, F(1,185)=206.89, eta2=.53. Study 2: d=1.58. Perceived choice free 4.00 vs coerced 2.39, d=1.51 | Kirkland et al. 2025 preprint (b17) | [E] (preprint) |
| Same, preregistered, larger sample | N=912 analysed of 1,012; pro M=1.40 vs anti -0.93, d=-1.64 | Kirkland 2025 Study 3 (b18) | [E] (preprint) |
| Moral conviction amplifies the bias, mostly when the rater agrees with the essay | Total N=1,611; Study 1 and 2 mixed and measure-dependent | Kirkland 2025 (b17, b18) | [C] |
| Historicism reduces the FAE | High historicism (+1 SD) choice vs no choice t(41)=-2.27, p=.028, d=.71; low: t<1. Three-way t(73)=2.33, p=.023 | Gill 2014 (b12) | [S] |
| Quiz-contestant bias persists with full difficulty information | N=147; easy vs hard F(1,71)=79.84, eta2=.52; explicit adjustment F(1,76)=39.89, eta2=.41; interaction F(1,146)=25.53, eta2=.09 | Moore et al. 2021 preprint (b14) | [S] |
| Heavy debiasing (table of scores) shrinks but does not remove it | Difficulty F(1,214)=69.09, eta2=.39; difficulty x explicitness F(1,214)=14.31, eta2=.07. Text says 110 participants but df implies more | Moore 2021 Study 2 (b15) | [S], N inconsistent |
| Bias also appears for inanimate objects | 60 analysed, 540 estimates; +1 g container raised estimated contents by 0.208 g (t=7.79); +1 g true contents by 0.469 g (t=9.35) | Moore 2021 Study 3 (b16) | [S] |
| Bias applies to robot speakers, stronger than for humans | N=231; behaviour F(1,220)=152.98, partial eta2=.41; behaviour x agent F(1,220)=16.15, eta2=.07. Beta -0.76 robot vs -0.48 human; adj r2 .58 vs .23 | Edwards and Edwards 2022 (b19, b20) | [S] |
| Koreans match Americans on dispositionism, exceed them on situationism | Study 1 N=100 KR vs 97 US: dispositionism 5.19 vs 5.00 (F<1); situationism 5.91 vs 5.43, F(1,191)=4.44, p<.05. Replication N=120 vs 121: 4.82 vs 4.59 (F<1); situationism 5.27 vs 4.67, F(1,240)=8.47, p<.005 | Norenzayan et al. manuscript (d05, d07) | [S] manuscript |
| Interactionism difference is unstable | Study 1 7.95 vs 7.79 (F<1); Study 3 7.99 vs 7.32, F(1,240)=10.63 | d05, d07 | [C] within one paper |
| Entity theory of personality rejected more by Koreans | Study 3 disagreement 3.87 vs 3.27, F(1,240)=15.60, p<.001 | d07 | [S] |
| Salience lets Koreans use situation info more | N=58; culture x situation F(1,50)=7.71, p<.01; three-way F(1,50)=4.60, p<.05; situation main effect F(1,50)=256.46 (30.08 vs 78.07) | d06 | [S], thin |
| East Asians correct for salient constraint, Americans do not | No cell sizes read | a08, a09, a10, a11, b04, d08 | [E] in direction, numbers missing |
| Equal bias when behaviour is highly diagnostic; Japanese none when low diagnostic | Cell sizes not read | Miyamoto and Kitayama 2002 (b04) | [S] (abstract) |
| Culture priming shifts internal attribution, young Hong Kong | N=107; F(2,104)=20.23, f2=.388; American 3.24 vs Chinese 2.70 vs control 3.07; d=1.479 [0.915, 2.044] | Talhelm 2025 Study 1 (a20) | [S] |
| Same, young mainland | N=272; F(2,269)=26.15, f2=.195 [.110,.294]; with demographics f2=.100 | a21 | [S] |
| No priming effect in older mainland adults | N=258; F(2,255)=1.10, p=.335, f2=.009. Generation x prime F(2,524)=5.09, p=.006, f2=.019 | a22 | [S] |
| Spontaneous trait inference is large and robust | k=86, N=13,630; dz=0.59 [0.53, 0.66] | Bott et al. 2022 (a23) | [E] |
| Culture does not significantly moderate it | Independent 0.62 (67 records), interdependent 0.51 (13 records); beta -0.09 [-0.24, 0.06], p=.239 | a23 | [C] (Na and Kitayama 2011 found a difference, b06) |
| Actor-observer asymmetry near zero overall | 173 studies (one source says 170 tests); d from -0.016 to 0.095. Appears only for idiosyncratic actors, hypothetical events, intimates, free-response coding; negative events show it, positive reverse | Malle 2006 (b01, b02) | [E] |
| Folk-conceptual asymmetries are real instead | Six studies; reasons vs causes; actors give more reason explanations | Malle, Knobe and Nelson 2007 (b03, b02) | [S] |
| Load raises correspondence bias; salience of the target does too | No numbers (Gilbert 1989; Storms 1973; Lassiter 2002 via Wikipedia) | b10, a12 | [C] (two-stage model "thin") |
| Spontaneous mentalising predicts later dispositional attribution | fMRI, N not read | Moran et al. 2014 (b08) | [S] (abstract) |
| Causal-role choice in symmetric physical settings varies by culture in concrete, not covariation, settings | 93 German, 103 Tongan; gas vs medium: Germany 66.7% gas (p=.127), Tonga 69.0% medium (p=.041); covariation no country difference G2=0.02, p=.887 | Bender and Beller 2011 (b21) | [S] |
| ChatGPT looks holistic on scales | AHS: GPT-3.5 5.35, GPT-4 5.01 vs human 4.87 (SD .49, N=702); TCT 0.87, 0.85 | Jin et al. 2023 (c12, c13) | [S] |
| Hindu children explain more situationally | Source is a web explainer, not a study | b11, a03 | refuted as evidence; do not cite |

## 4. Mechanisms and models

Each model below is written so an engineer could build a probe or a check from it.

**4.1 Anchor-and-adjust (Gilbert).** Two passes. Pass 1 is fast and gives a dispositional reading: behaviour B implies trait T. Pass 2 is slow and subtracts the situational force F: T' = T - adjustment(F). Under load or when F is hidden, pass 2 is skipped or too small. Implementation as a probe: give the model an item with a visible F and measure how far its judgment moves versus an item without F. The adjustment size is the output. Caveat: the evidence is "remarkably thin" (a16). Moore et al. 2021 found that telling people exactly how much to adjust shrank the bias but left it (b14, b15), so adjustment is not the whole story.

**4.2 Salience and diagnosticity gate.** Choi and Nisbett, Miyamoto and Kitayama (a09, b04). The adjustment fires only if the constraint is salient and the behaviour is low in diagnosticity. Implementation: a checklist with two fields before inferring a trait: (a) is a constraint present and stated? (b) would a person without the trait have acted the same way? If (b) is yes, the observation is non-diagnostic and the inference is cut. This is the same logic as Kelley's distinctiveness and consensus (a04).

**4.3 Lay explanation graph (Bohm and Pfister 2015).** Seven node types (goals, dispositions, temporary states, intentional actions, outcomes, events, stimulus attributes). Rules: actions are caused by goals; goals by higher goals or states; states by dispositions, stimulus attributes or events; events by dispositions or earlier events (a05). Implementation: a typed causal graph over a trace. This is a finer split than person vs situation, and it fits an agent log (action, goal, state, event). Western samples only.

**4.4 Automaticity and chronic goals (Mason and Morris).** Three rival accounts of why East Asians adjust more: more effortful correction, more automatic correction, or a chronic situational inference goal (a13, a16). They predict different load results. For a model, the equivalent is a default goal in the prompt. A "check the situation first" instruction is a chronic goal, not a load manipulation.

**4.5 Priming as knowledge activation (Hong et al. 2000, Talhelm 2025).** Culture works as accessible knowledge that primes can switch. In young Chinese adults the switch was d about 1.0 to 1.5 (a20); in older adults it was absent (a22). An LLM analogue is a persona or culture prompt. Tao et al. found such prompts move survey-value answers (c17), but nobody measured attribution (d16).

**4.6 Authorship and self-attribution (LLM analogue).** Tsui 2026: the same injected error is fixed if labelled as the user's and missed if labelled as the model's own (b22). Khullar et al. 2026: an action shown as the model's own previous turn is judged more correct and less risky than the same action shown by the user (d10). The mechanism seems to be conversational structure, not the words "same model". Implementation: run the self-check in a fresh turn that presents the output as someone else's.

**4.7 Intervention-based blame (DoVer).** Log-only blame to one step is often ill-posed, because several different interventions can each repair a failure (c21). The check: form a blame hypothesis, intervene (edit the message or plan at that step, re-run), and see whether the failure flips. This replaces reading the log with testing the cause.

**4.8 Label-as-disposition bias.** A stable-trait label shifts the decision criterion (Rosenblum et al., d14). Implementation: a counterfactual pair, same evidence with and without the label, scoring the gap.

## 5. What holds up

**Holds up.**
- The core correspondence effect in US online samples. Position effects of d about 0.84 (coerced) to 2.0 (free), with d 1.5 to 1.6 in Kirkland's coerced conditions. All three sources (Gill, Kirkland, Edwards) agree (b12, b17, b18, b19). Two of the three are preprints.
- The bias survives heavy debiasing. Explicit instructions about how much to adjust, and a table of scores, shrank but did not remove it (b14, b15).
- It extends to objects (M&Ms and container weight), so it looks like a general inference habit (b16, single sample of 60).
- Spontaneous trait inference is robust (dz=0.59, k=86), and the meta-analysis found no significant culture moderator (a23).
- The Korean vs American difference is in situational weight, not dispositional weight (d05, d07).

**Fails or weak.**
- The actor-observer asymmetry as taught. Meta-analytic effects are d -0.016 to 0.095 (b01). It appears under narrow conditions, and the valence of the event flips it. Textbook accounts overstate it (critique).
- "East Asians do not show the FAE." They do when constraints are not salient (a17, a08).
- Anchor-and-adjust as a full mechanism. Thin evidence (a16). Debiasing aids do not eliminate the bias (b15).
- Hindu-children and "individualist cultures are more prone" claims rest on a web explainer or on Wikipedia (b11, a03). Do not cite.
- Culture moderation of spontaneous trait inference: one study finds it (b06), the meta-analysis does not (a23). Interdependent samples are only 13 records.
- Interactionism difference between Koreans and Americans appeared in one of two studies (d05 vs d07).

**Moderators.**
- Constraint salience and attitude diagnosticity (a08, a09, b04).
- Cognitive load, with culture interaction (Knowles, via d08).
- Valence of event and intimacy of actor (Malle, b01).
- Moral conviction and agreement with the essay stance (b18).
- Beliefs about history and social forces (b12).
- Generation and age: Talhelm's priming effect is absent in older mainland adults, but age and cohort are confounded (a22).
- Task content: Tongan vs German causal roles differ in concrete settings only (b21).

**Interventions.**
- Worked partly: explicit instruction on how much to adjust (shrinks, eta2 .52 to .41, b14); a table of scores (shrinks more, b15); making the constraint salient (for East Asian samples only, a09).
- Did not work fully: none of these removed the bias.
- Training-based debiasing for humans was not covered by our sources.

**Replication status.** Talhelm 2025 replicated the Hong et al. priming effect in young Chinese (not preregistered, a20, a21). No large preregistered replication of the East-West correspondence-bias gap was found. The search was blocked by rate limits and is incomplete (d18). Castagnetti and Potters 2025 ("The Fundamental Attribution Error is not Fundamental") and Thierman 2011 are leads only, not read (d19).

## 6. Language models

**No LLM Jones-Harris study with numbers was found** in six targeted arXiv queries (d18, b25). The searches were incomplete (API rate limits). The closest item is a blog post (Trott and Walker 2023, c10, c11). GPT-4 rated a writer's attitude 1 to 10 for ProCon.org essays under four pressure levels (1% extra credit, expulsion threat, gun to the head). Rated attitude fell as pressure rose. No means or N are given. No LLM replication of Morris and Peng 1994 or Choi et al. 1999 was found (c28).

**Role-swap FAE (Malberg et al. 2025, c01, c02, a24, d01, d02).** 30 biases, 20 models, 30,000 template tests. The FAE test tells the model it is the actor (control) or an observer (treatment) of a controversial action. It picks among matched dispositional and situational explanations on a 7-point scale. The score is the gap between roles, on a -1 to 1 scale.
- FAE mean 0.10 across 20 models, range -0.02 to 0.23, random baseline 0.03. Examples: GPT-4o 0.18, GPT-3.5 0.00, Llama 3.1 405B 0.18, Llama 3.1 8B 0.00, Llama 3.2 3B -0.02, WizardLM-2 8x22B 0.23, Mistral Large 0.19.
- Information bias 0.54, in-group bias 0.41, framing 0.41, anchoring 0.39, self-serving 0.21 (per-model -0.04 to 0.79), stereotyping 0.09. FAE is near the bottom.
- Limits: tests were generated by an LLM; 3 of 300 hand-checked tests were flawed. It measures a role gap, not the Jones-Harris paradigm. No culture arm. The 0.10 is the paper's own scale, not a human effect size. One source for a24, c01-c03 and d01-d02.

**Outcome attribution by identity (Raj et al. 2025/2026, c04-c09, a25, a26, d03, d04).** 140k prompts, 400 templates, 10 scenarios, 4 identity dimensions (gender, 15 nationalities, 6 races, 6 religions), 3 settings (Single-Actor, Actor-Actor, Actor-Observer), 3 headline open models (Aya-Expanse-8B, Qwen-32B, Llama-3.3-70B). Measure: (p_effort + p_ability) - (p_difficulty + p_luck), a difference of probability mass, not Cohen's d. Tests: one-sample t and Wilcoxon.
- Style depends on model. Aya-8B leans external for both success and failure. Qwen and Llama lean on effort (internal). The text says smaller models rely on external, larger on internal.
- Identity shifts: failure of Russian, French, German, Japanese and Korean actors is more often internalised; White and Black male successes are mostly external; Asian, Middle Eastern and Hispanic women get more internal credit than men.
- Observer identity mostly amplifies external-cause shifts; larger models are more identity sensitive than the 8B one.
- Correction recorded in d04: the earlier claim "failure is internalised in all three models" is not supported.
- Limits: only 3 models, 5 name samples per cell, no human baseline, no debiasing arm, per-model d only in figures.

**Cultural stance (Jin et al. 2023, c12-c15, d15).** GPT-3.5 and GPT-4 score more holistic than the human norm on the Analysis-Holism Scale (5.35 and 5.01 vs 4.87, SD .49, N=702; 10 runs each) and on the Triadic Categorization Task (0.87, 0.85). Value measures disagree. Dialectical Self Scale: GPT-3.5 4.59 vs 4.00, p<.001; GPT-4 3.97, p=.344. Independent self-construal: 6.98 and 5.32 vs 4.73. Interdependent: 5.85 (p<.001), 4.95 vs 4.81 (p=.07). Results held across temperature 0 to 1.5 and prompt paraphrase. Ten runs make the model the unit, so the t-tests against human norms are weak inference. This is not an attribution task.

**Culture prompting (Tao et al. 2024, c16, c17, d16).** Without prompting, five OpenAI models resemble English-speaking and Protestant European countries on survey values. Asking the model to answer as a person from country X improves alignment for 71 to 81% of countries for GPT-4, 4-turbo and 4o. Mean cultural distance: GPT-4o 2.42 to 1.57, 4-turbo 2.71 to 1.77, GPT-4 2.69 to 1.65 (all P<.001). Weak for GPT-3 and 3.5-turbo. 20 to 30% of countries do not improve. Values, not attribution. No comparison with human priming (d about 1.0 to 1.5).

**Authorship and self-attribution.**
- Tsui 2026 (b22, c18, c19, d11): 14 open non-reasoning models, mean blind spot 64.5% (Claude 3.5 Haiku 52.5%, Claude Sonnet 4 41.4%, 62.8% on BIG-Bench Mistake tasks). Appending "Wait" cuts it 89.3% and lifts mean accuracy 156%. "But" and "However" work less well. Fine-tuning on 5,306 correction traces cuts it 76.0%. On naturally made errors only 4.3 to 10.8% of missed errors are caught when shown externally. Injected errors, non-reasoning models.
- Khullar et al. 2026 (d10): Claude Sonnet 4 as code-correctness monitor, AUROC 0.99 off-policy (same-turn and previous-turn), 0.89 on-policy same-turn, 0.92 previous-turn. Self-leniency reversals are 5 to 10 times more common than the opposite. Claude Opus 4 rated disclosures 9-10/10 risk at baseline but 0/10 when self-attributed. Saying "the same model wrote this" does not cause it by itself. Raising reasoning budget did not reliably fix it. Preprint; coding and tool-use tasks.

**Label and identity bias.**
- Rosenblum et al. 2026 (c25, d14): five LLMs, 20,000 responses (1,000 per model per cell, 4 cells). A prior schizophrenia label raised continued-hospitalisation advice from 4.7% (237/5,000) to 22.3% (1,113/5,000) when the evidence supported discharge. Risk difference 17.5 points (95% CI 16.2-18.8), model range 10.4-34.4. Concordance with the reference fell 95.3% to 77.7% while confidence rose (d=0.35-1.09). When hospitalisation was supported: 92.6% to 97.0%. One synthetic vignette; no mitigation arm.
- McFadden 2026 (d17): 1,458 vignettes, 5 LLMs, 0-7 fault scale. Male disputants rated +0.16 more at fault than identical female ones (dz=0.316). Held on 45 unseen scenarios. Single author; a prespecified account failed its test.
- Zhou and Di Eugenio 2025 (b24): five LLMs attribute correct solutions unevenly across demographic groups and rate identical solutions differently by perceived author. Directions only (abstract).
- Salemi et al. 2026 (b23): a model-generated goal (dispositional) or context (situational) hint raised macro-F1 on disaster social-media tasks. Llama3 intent: Lilac 80.8 to 88.7, Thomas 82.5 to 86.2. Mistral theme: Alberta 81.0 to 82.8, Colorado 83.6 to 84.8. Best in 8 of 12 model-language cells; Self-Debias lowered Mistral results. Bias inferred from F1 gaps; not a classic FAE test.

**Multi-agent failure attribution.**
- Who&When (Zhang et al. 2025, c23, c24, d12, d13): 127 multi-agent systems, 184 annotation tasks. Best method 53.5% agent-level, 14.2% step-level. Hand-crafted systems, table (agent %, step %, tokens): all-at-once 57.02 / 4.39 / 17,106; step-by-step 35.96 / 7.90 / 87,720; binary search 43.97 / 6.90 / 34,659; hybrid 57.02 / 12.28 / 149,177, so hybrid is about 8.7 times the tokens for about 2.8 times the step accuracy. Reasoning models do not help: GPT-4o all-at-once 54.31 / 4.39, o1 41.38 / 10.34, R1 56.90 / 3.45 (column mapping inferred from flattened text). Annotator uncertainty 16.7 to 26.3%.
- DoVer (Ma et al. 2026, c21, c22): intervention-driven checks flip 18% and 28% of failed trials on two benchmarks and 49% (198 trials) on GSMPlus with AG2; validate or refute 30 to 60% of hypotheses. On 29 cases, uncertain ground truth (14) gives GPT-4o 24% and GPT-5 7% step accuracy; certain cases (15) give 44% and 53%. No equal-token comparison.

**Others.**
- Implicit causality in GPT-2 (Huynh et al. 2022, c26): verb effect b=-0.049 (SE 0.012); only 32% of continuations rated 4 or more. Old model, low value.
- Kim et al. 2026 (c20): "LLM fallacy" is a conceptual paper on users crediting their own competence for LLM output. No data.

**What changed the behaviour, and by how much.** Wait: -89.3% blind spot. Fine-tuning on traces: -76.0%. Culture prompt: survey distance down by about a third (GPT-4o 2.42 to 1.57), not attribution. Hint of goal or context: macro-F1 up 1.2 to 7.9 points on the cells listed. Intervention-based blame: 18 to 49% of failed trials flipped. Hybrid prompt: step accuracy 4.39 to 12.28 at 8.7 times the tokens. Reasoning budget: no consistent change to self-attribution bias (d10).

**What is not known for LLMs.** No Jones-Harris test with numbers. No human-priming vs LLM culture-prompt comparison on attribution. No test of a Wait or self-check step on identity or label bias. No test of whether a tight token budget raises correspondence bias.

## 7. What our agent should take

Honest summary. Background only, and the evidence for LLMs is thin and mostly single-source. Little here is ready for SCHEMA.md.

### Add now (established)

Nothing new qualifies as a schema change. Three items only restate or sharpen existing rules.

1. **Do not hard-code an actor/observer correction.** Part: none (negative rule). Status [E]. Evidence: b01, b02, b03, c01. The meta-analytic effect is about zero (d -0.016 to 0.095), and the LLM role-swap gap is 0.10 on a -1 to 1 scale.
2. **Treat blame for a failed trace as a hypothesis to test, not a reading of the log.** Part: G2 and G10 (already present), memory/O. Status [E] for the difficulty (K17, two sources: Who&When, DoVer), [S] for the cure. Evidence: c21-c24, d12, d13. The scaffold already forbids revising from opinion (G2). This adds a concrete reason: log-only blame is right at the step level only 4 to 14% of the time, and reasoning models do not fix it.
3. **Keep G4 and G10 as they are.** The LLM self-leniency results (d10, d11) are further evidence that a model's judgment of its own output is not independent. Part: G4, G10. Status [S] for the LLM data, [E] for the guardrail. Evidence: b22, d10, d11.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Self-check in a fresh turn that presents the output as someone else's, plus a "Wait" step | O (self-check), S8 | [S] | b22, c18, c19, d10, d11 (K16, K22, K23) |
| 2 | Assigned-vs-chosen check before inferring a stance or trait from a text | G (new guard) or O (context check) | [C] human [E], LLM unknown | a01, b12, b17, b18, c10, c11 (K01, K02, K11, K25) |
| 3 | Label-swap guard: score the evidence with labels, names and identity cues stripped, compare to the labelled score | G (bias guard) | [S] | c25, d14, d17, a25, a26 (K14, K15, K26) |
| 4 | Intervention-based blame for failed traces (edit one step, re-run) | memory/O | [S] for cure | c21, c22, d12 (K17) |
| 5 | Constraint-salience step: "list stated constraints that could force this behaviour before inferring intent" | O (context check) | [C] | a08, a09, b04, d05, d06 (K03) |
| 6 | Measure the base model's default attribution lean before trusting it in failure explanations | S0 or S9 | [S] | c05, d04, c01 (K10, K14) |
| 7 | Short vs long deliberation on correspondence-bias items | S, G11 | [C] | b10, a12, d10 (K07) |

Not to add: culture or persona prompts as a guard (K13, c17, d16: they move survey values, not attribution); any actor-observer correction; any claim that the model is "Western-analytic" (K12: it looks holistic on scales); Hindu-children claims (K21).

## 8. Concrete tests on our bench

All arms at equal total tokens. Report setup cost with the arm (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Jones-Harris for LLM | Essay vignettes (3 topics, 4 pressure levels from none to strong; assigned vs free choice; pro and anti positions), about 25 per cell | plain; plain + "was the position assigned or chosen?" check; plain + Wait | Attributed attitude (1-10) position effect size d under coercion; slope vs pressure level | Plain: coerced effect above 0 (human d 0.84 to 1.6; LLM size unknown). Check arm cuts it by at least a third |
| T2 Role swap | Malberg-style actor/observer items, 100 items, scale -1 to 1 | plain; with explicit "answer as if the other role" step | Role-gap score | Plain near 0.10 (Malberg mean); step lowers toward 0. Cheap control for K10 |
| T3 Label swap | Rosenblum-style evidence-fixed vignettes plus 2 other domains, label vs no label, 500 per cell | plain; strip-labels pass; fresh-turn check | Risk difference between labelled and unlabelled; concordance with reference | Plain: gap 10 to 35 points on some models; strip arm brings it under 5 |
| T4 Identity swap | Raj-style single-actor outcome vignettes, 4 identity dimensions | plain; Wait step; identity-stripped | Internal-minus-external probability gap per identity pair; max gap | Plain: gaps exist, direction model-specific. Wait unlikely to help (untested) |
| T5 Self vs other critique | Known-bad outputs (injected and natural errors), same content labelled user's vs own | same turn; fresh turn; Wait | Detection AUROC and miss rate | Fresh turn or Wait lifts detection; natural errors may stay low (4 to 11%) |
| T6 Failure blame | Our own scaffold traces with known decisive step | log-only all-at-once; hybrid; intervention replay | Agent-level and step-level accuracy; tokens | Log-only step accuracy about 4 to 14%; replay higher at higher cost; check at equal tokens |
| T7 Token budget | Items from T1 | tight vs generous budget | Position effect d | Humans: load raises bias; for LLMs no direct evidence; null is likely |
| T8 Salience | Items from T1 with a stated vs unstated constraint | plain; salience-listing step | Shift in inferred attitude between stated and unstated | Step increases shift only if the model currently ignores constraints |

Run all with at least 3 seeds and report per-model results; model style differs (c05, d04).

## 9. What does not transfer, and why

- **Culture as an identity.** The model has no self-construal, upbringing or cultural knowledge in the human sense. Jin et al. found a mixed profile: holistic on thinking scales, not consistently Eastern on self-construal (c12-c14).
- **Priming effect sizes.** Hong Kong d=1.48 comes from students on self-report ratings (a20). No LLM analogue has been measured, and the effect vanished in older mainland adults (a22).
- **Cognitive load.** Humans lose adjustment under load (Gilbert 1989). For LLMs, hidden reasoning budget did not reduce self-attribution bias (d10). Token budget is not a clean analogue of attentional load.
- **Self-serving and ego motives.** The human actor-observer story involves ego and impression management. A model has no stakes; the LLM gap arises from conversation structure (d10, d11).
- **Moral conviction and motivated agreement.** Needs the rater to hold a view (b18). A model has no such commitments unless a persona is given.
- **Spontaneous trait inference.** It is a memory-priming effect measured by lexical decision and N400 (b06). No clean LLM equivalent.
- **Brain-based claims.** fMRI and N400 results (b06, b08, a15) rest on reverse inference and do not map to a scaffold.
- **Person vs situation as one axis.** Bohm and Pfister show the real structure is richer (a05). An agent's own failure logs fit that graph better than the two-bucket frame.

## 10. Open questions

1. What did Choi et al. 1999, Morris and Peng 1994 and Miyamoto and Kitayama 2002 actually find, with N and effect sizes? Only review descriptions were read.
2. Did the East-West gap in correspondence bias replicate in large preregistered samples? Castagnetti and Potters 2025 and Thierman 2011 are unread leads (d19).
3. Does an LLM show a Jones-Harris effect with real numbers, and does a "was it chosen?" step cut it at equal tokens?
4. Does a culture or language prompt shift LLM attribution as much as priming shifts young humans (d about 1.0 to 1.5)?
5. Does Wait, or a fresh-turn check, change identity bias (Raj) or label bias (Rosenblum)?
6. What are the per-model, per-identity effect sizes in Raj et al. (only in figures)?
7. Can intervention-based blame in our own scaffold beat Who&When step accuracy (14.2%) at equal tokens?
8. Does a tight token budget raise correspondence bias in LLMs?
9. What are Malle 2006's effect sizes by moderator, and do LLMs show actor-observer swaps when roles are switched in richer scenes (b01, d02)?
10. Is the 3 of 300 flaw rate in Malberg's template tests low enough to trust the FAE score of 0.10 (d01)?
11. Why do Moore et al. 2021 report N=110 but df 214 (b15)?
12. Is the Walker, Smith and Vul 2015 critique (the FAE depends on the benchmark) compatible with LLM results? Not opened.

## 11. Sources

[V] opened this session; [M] snippet or abstract only.

- [V] Norenzayan and Nisbett 2000, Culture and causal cognition (a01, a02, a06-a08, a17-a19, d09). https://www2.psych.ubc.ca/~ara/Manuscripts/Norenzayan&Nisbett%20current%20dir.pdf
- [V] Mason and Morris 2010, Culture, attribution and automaticity (a09-a16, d08). https://doi.org/10.1093/scan/nsq034
- [V] Norenzayan, Choi and Nisbett, draft of 2002 PSPB (d05-d07). https://public.websites.umich.edu/~nisbett/cultsim.pdf
- [V] Wikipedia: Fundamental attribution error; Attribution (psychology); Actor-observer asymmetry (a03, a04, b02, b10, b11). https://en.wikipedia.org/wiki/Fundamental_attribution_error
- [V] Bohm and Pfister 2015 (a05). https://pmc.ncbi.nlm.nih.gov/articles/PMC4332278/
- [V] Talhelm et al. 2025 (a20-a22, a27). https://pmc.ncbi.nlm.nih.gov/articles/PMC11984341/
- [V] Bott et al. 2022 (a23). https://pmc.ncbi.nlm.nih.gov/articles/PMC10676050/
- [V] Na, Huang and Park 2017 (a28). https://pmc.ncbi.nlm.nih.gov/articles/PMC5366355/
- [V] Gill, Andreychik and Bastian 2014 (b12, b13). https://europepmc.org/article/PMC/PMC4090131
- [V] Moore, Schatz and Sharek 2021 preprint (b14-b16). https://doi.org/10.31234/osf.io/ur4wt
- [V] Kirkland et al. 2025 preprint (b17, b18). https://doi.org/10.31219/osf.io/9g8t5_v1
- [V] Edwards and Edwards 2022 (b19, b20). https://doi.org/10.3389/frobt.2021.788242
- [V] Bender and Beller 2011 (b21). https://doi.org/10.3389/fpsyg.2011.00231
- [V] Tsui 2026, Self-Correction Bench (b22, c18, c19, d11). https://arxiv.org/abs/2507.02778
- [V] Salemi et al. 2026 (b23). https://arxiv.org/abs/2603.27057
- [V] Zhou and Di Eugenio 2025 (b24, abstract page only). https://arxiv.org/abs/2505.16128
- [V] Malberg et al. 2025 (a24, c01-c03, d01, d02). https://arxiv.org/abs/2410.15413
- [V] Raj et al. 2025/2026, Talent or Luck (a25, a26, c04-c09, d03, d04). https://arxiv.org/abs/2505.22910
- [V] Trott and Walker 2023, blog post (c10, c11). https://seantrott.substack.com/p/humansand-gpt-4are-predicta
- [V] Jin et al. 2023 (c12-c15, d15). https://arxiv.org/abs/2308.14242
- [V] Tao et al. 2024 (c16, c17, d16). https://arxiv.org/abs/2311.14096
- [V] Kim et al. 2026, The LLM Fallacy (c20). https://arxiv.org/abs/2604.14807
- [V] Ma et al. 2026, DoVer (c21, c22). https://arxiv.org/abs/2512.06749
- [V] Zhang et al. 2025, Who&When (c23, c24, d12, d13). https://arxiv.org/abs/2505.00212
- [V] Rosenblum et al. 2026 (c25, d14). https://arxiv.org/abs/2610.35326
- [V] Huynh et al. 2022 (c26). https://arxiv.org/abs/2212.04348
- [V] Khullar et al. 2026, Self-Attribution Bias (d10). https://arxiv.org/abs/2603.04582
- [V] McFadden 2026 (d17). https://aclanthology.org/2026.gebnlp-1.5
- [V] arXiv search record for gaps 1 and 4 (d18). https://arxiv.org/search/
- [M] arXiv title searches for FAE and correspondence bias in LLMs (b25). https://arxiv.org/search/
- [M] Malle 2006, actor-observer meta-analysis (b01). https://doi.org/10.1037/0033-2909.132.6.895
- [M] Malle, Knobe and Nelson 2007 (b03). https://doi.org/10.1037/0022-3514.93.4.491
- [M] Miyamoto and Kitayama 2002 (b04). https://doi.org/10.1037/0022-3514.83.5.1239
- [M] Gilbert and Malone 1995 (b05). https://doi.org/10.1037/0033-2909.117.1.21
- [M] Na and Kitayama 2011 (b06). https://doi.org/10.1177/0956797611414727
- [M] Nisbett and Masuda 2003 (b07). https://doi.org/10.1073/pnas.1934527100
- [M] Moran, Jolly and Mitchell 2014 (b08). https://doi.org/10.1162/jocn_a_00513
- [M] Ross 2018 (b09). https://doi.org/10.1177/1745691618769855
- [M] Nisbett, Peng, Choi and Norenzayan 2001 (c27, not opened; HTTP 403). https://doi.org/10.1037/0033-295X.108.2.291
- [M] Cao n.d., secondary search summary (c29). https://www.bohrium.com/scholar/59430f47/Jie_Cao
- [M] Castagnetti and Potters 2025, SSRN, title only (d19). https://doi.org/10.2139/ssrn.5636063
- [M] Search gap note for cross-cultural LLM replications (c28). https://arxiv.org/
- Cited only through reviews, never opened: Jones and Harris 1967; Ross 1977; Heider 1958; Kelley 1967; Jones and Nisbett 1971; Storms 1973; Gilbert, Pelham and Krull 1988; Gilbert 1989; Morris and Peng 1994; Choi and Nisbett 1998; Choi, Nisbett and Norenzayan 1999; Masuda and Kitayama 2004; Knowles et al. 2001; Lieberman et al. 2005; Hedden et al. 2008; Hong et al. 2000; Walker, Smith and Vul 2015.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 4 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A19.03-K19** (reworded: the sources support less). Kirkland abstract says Studies 1-2 were mixed and only preregistered Study 3 found moral conviction predicting more dispositional inference (mainly when participants agreed with the essay); d up to 1.64 is the essay-position effect itself, not the conviction effect; Gill is not about moral conviction so there is a single preprint source. Corrected claim: A single preprint (N=1,611 across three studies) found mixed evidence in Studies 1-2 and, in preregistered Study 3, that stronger moral conviction predicted more dispositional inference, mainly when participants agreed with the essay; the underlying correspondence-bias effect of essay position was large (d up to 1.64) regardless.
- **A19.03-K06** (now single-source: only one opened source, code check).
