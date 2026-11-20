# Thinking for speaking: deep document

*Subfield A15.05. Written from evidence_a-d.jsonl (a01-a25, b01-b25, c01-c25, d01-d19), claims.jsonl (K01-K24) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Evidence ids in brackets. Why it matters: background only. The narrow claim is relevant to a text-only agent; the strong claims are not.*

## 1. What it is

"Thinking for speaking" (Slobin 1996) is a narrow claim about language and thought. While a person builds a message to say, they pick out the features of an event that their language forces them to mark. Learning a first language trains the child to do this. The claim covers the time of message building only. It does not say language changes what people can see, remember or think about in general [a01, a20, d07].

It sits between two extremes. The strong Whorfian view says language changes perception and thought all the time. The no-effect view says language changes nothing, even during speech planning. Papafragou, Hulbert and Trueswell (2008) framed these three outcomes and found data for the middle one [a20].

Where it sits in speech production: Levelt (1989) splits speaking into conceptualisation (a preverbal message), formulation, then articulation. Thinking for speaking is the micro-planning step inside conceptualisation. Griffin and Bock (2000) showed gaze reaches an object before the speaker names it [a13].

The typology behind the work is Talmy's. Satellite-framed languages (English, Swedish) put manner in the verb ("run") and path in a satellite ("into"). Verb-framed languages (Greek, Spanish, French, Turkish) put path in the verb ("enter") and give manner optionally [a12].

For our agent, the fit is loose. An LLM has no eyes and no pre-linguistic percept. Its "message building" is the text it writes before an answer. Three parts carry over:
1. The language and format of the task shape what the agent selects at the start of its thinking (an analogy only, K02, K08).
2. The language an agent reasons in changes its accuracy and diversity (measured, K10, K14, K19).
3. A describe-first step may bias later judgements (K04, K21).

## 2. History and theories in depth

**Origin.** Whorf's strong claim (language shapes thought) met heavy criticism. Slobin (1996), in Gumperz and Levinson (eds), *Rethinking Linguistic Relativity*, pp. 70-96, offered a weaker, testable version: "from thought and language to thinking for speaking" [a01, b20]. The paper was not opened in this run (PhilArchive returned 403). What we know is second-hand [d06, d08].

**Slobin's evidence, as described by Gennari et al. (2002) [d06].** Slobin used Spanish-English translations, narrations of the same pictures and mental images linked to narrations. English had more manner verbs and a richer manner vocabulary. Every response pattern was linguistic. His inference: English speakers habitually attend to manner and find it easy to code. The cognitive claim is a hypothesis, not a tested effect [K23].

**Frog stories.** Berman and Slobin (1994) had children and adults in several languages narrate the same picture book. Narratives differ by language in manner, path, tense/aspect marking and scene setting [a11]. The paper was not opened and no rates were obtained. Papafragou et al. report the path/manner difference in child speech is in place by about age 3, and that Naigles et al. 1998 contested this [d07].

**Bowerman.** Wikipedia credits Bowerman with showing that early spatial thought and categorisation develop largely independent of language [a02]. Bowerman and Levinson (2001) and Gentner and Boroditsky (2001) are named as stronger accounts that the non-linguistic results are hard to reconcile with [a20].

**The three-way test.** Papafragou et al. (2008) made the first eye-tracking test. They crossed language (English, Greek) with task (describe vs memorise) [a03-a06]. See section 3.

**Competing explanations of language effects in non-speaking tasks.**
- *Language as strategy* (Gennari 2002; Papafragou 2008): speakers covertly label during tasks that invite labelling. Effects then show up. No labelling, no effect [b05, b06, a06].
- *Online linguistic effect on perception* (Goller 2017; Fu 2023; Soroli 2024): some language effects appear without speech [b14, d01, d03]. Authors disagree on whether covert labelling explains them.
- *Attention-to-structure account* (Gleitman et al. 2007): attention to an entity shapes sentence structure. Capturing gaze on one character raised its chance of being the subject [a07, b21]. This is the reverse direction (attention drives language). Only the abstract was seen.
- *Event structure as a conceptual level* (Bunger et al. 2013): priming works only when primes and targets overlap conceptually, so there is a conceptual event level feeding message planning [a09].
- *Language of vision* (Coco et al. 2026): in English, Portuguese and Japanese, meaning similarity of two descriptions predicts scan-path similarity in all three languages and across languages. Syntax adds only a brief early effect within language and within scene [a19, b17].

**Narrowing of the grammar-to-cognition story.** A future-tense study (Robertson et al. 2025, N=235) reversed the expected sign: English speakers who used the future tense more discounted less [d18]. This is a caution on grammar-to-cognition claims in general.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| English speakers use manner verbs more in bounded motion events than Greek speakers | Bounded: 72% English vs 36% Greek. Unbounded: 76% vs 54%. Path verbs in bounded events: 16% En vs 39% Gr. N=17 per group, 12 clip-art events | Papafragou 2008 [a03, b01] | [E] (production; K01) |
| Swedish uses one satellite frame; Spanish varies by speaker | Swedish satellite-framed 97% of descriptions. Spanish verb-framed 59%, satellite 35%, no path 6%. N=84 (42/42), 32 events. Speaker intercept SD 2.37 vs event SD 0.78 | Montero-Melis 2021 [a15, b08] | [E] (with Gennari) |
| Spanish vs English description in Gennari 2002 | 47 Spanish and 46 English. Spanish path-verb proportion 0.80, manner expression 0.71. English manner 0.86 in all conditions; Spanish 0.64/0.76/0.73 (Naming First/Free/Shadow) | Gennari et al. 2002 [b05] | [E] |
| Gaze while preparing to speak differs by language in the first second | Language x Region F1(1,16)=4.01, printed p=.03 (two-tailed about .06), partial eta2=.20; F2(1,11)=10.14, p=.004. Greek look at path endpoint first. Third second reverses: F1(1,16)=3.43. Median speech onset 1267 ms; 88% spoke within 2000 ms | Papafragou 2008 [a04, b02] | [S] (K02) |
| First-look interaction in the speaking task | F1(1,16)=5.50, p=.03, partial eta2=.26; by items F2(1,11)=3.61, p=.08 (marginal) | [b01] | [S] |
| Both groups look more at path endpoint than manner overall | Linguistic F1(1,16)=19.71, eta2=.55. Nonlinguistic F1(1,14)=28.45, eta2=.67 | [b02] | [E] within that study |
| No language difference in gaze while watching for memory | Interaction first reliable only after freeze: 4th second F1(1,14)=6.31, eta2=.31; 5th F1(1,14)=9.66, eta2=.41, in the opposite direction (people study what their verb omits) | [a05, b03] | [C] (K03) |
| Memory cost for Greek speakers only when not describing | Path-endpoint memory % (bounded/unbounded): Linguistic En 92/91, Gr 92/92. Nonlinguistic En 90/88, Gr 73/71. Language x Task F1(1,25)=4.95, printed p=.01 (two-tailed about .035), eta2=.17. 5 excluded for same-bias | [a06] | [C] (K04) |
| Spanish-English: no recognition-memory difference; similarity differs only after verbal encoding | Naming First 16/15, Free 15/15, Shadow 16/16 per group (En/Sp) | Gennari 2002 [b05, b06] | [C] (K04) |
| Adults and 4-year-olds gaze alike but speak differently | 20 adults, 20 children. Both manner and path in 70% of adult vs 26% of child descriptions. Mean length 7.7 vs 5.8 words | Bunger 2012 [a08] | [S] |
| Event structure primes message content | 70 adults kept (15 excluded). Priming failed with no conceptual overlap | Bunger 2013 [a09] | [S] |
| Goal bias: endpoints attended and mentioned more than sources | Mention Goal 97.7% vs Source 87.5% (beta=-1.048, p=.006). Fixation 1312 vs 913 ms (beta=199.41). Speaking shifts attention toward Source (Condition x AOI beta=-113.42). Memory change detection: Linguistic Goal 62.5 vs Source 53.1; Non-linguistic 50.9 vs 42.9. N=128 (27 excluded from eye analysis) | Chen et al. 2026 [a17, b07] | [S] (K09) |
| English-Turkish: language effect in description, none in segmentation | Turkish more multi-clause: beta=-3.84, SE=0.57, z=-6.67. Enumeration 2-event responses: beta=-0.10, p=.82; Source/Goal path beta=-1.83, p=.002; no interaction p=.73. N=39 vs 42 | Lee et al. 2026 [a16, b15] | [S] (K05) |
| Korean vs German: language-shaped similarity and gaze, no speech | N=27. Language x Pair F(3,75)=8.02, partial eta2=.24. German tight-in/loose-in similar (t(25)=3.31, d=1.27); Korean tight-in/tight-on (t(25)=2.76, d=1.06) | Goller et al. 2017 [b14] | [C] (K06) |
| English vs Mandarin: manner detected faster by English under flash suppression, no speech | 55 Mandarin, 52 English. Condition x Language beta=-0.18, SE=0.06, p=.004. English manner vs path mismatch t=-2.82, p=.006; Mandarin p=.63 | Fu, Vanek & Roberts 2023 [d01] | [C] (K03) |
| Same contrast flips when a sentence is read first | 51 per group. Mandarin manner vs path beta=0.064, p=.524. English full mismatch faster than manner (beta=-0.49, p<.001) and path (beta=-0.23, p=.039) | [d02] | [C] (K20) |
| English vs French non-verbal categorisation differs | French 78% path-congruent vs English 59%. Verbal: English 67% manner vs French 41%, F(1,36)=16.71. Non-verbal gap smaller than verbal. 20 per language | Soroli 2024 [d03] | [C] (K03, K20) |
| Chinese vs English similarity of spontaneous motion; L2 slower | N=160 in 5 groups of 32. Chinese monolinguals faster than English, especially path matches; L2 slower at all levels | 2019 study [b18] | [S] |
| Agent preference; Basque vs Spanish | 300 ms exposure. Basque N=90, Spanish N=88. Agents attended more in both; Basque more accurate on agent probes, less on patient probes | Isasi-Isasmendi 2023 [a14] | [S] |
| Aspect vs non-aspect languages mention goals differently; bilinguals switch construal | Second-hand only; vanished under verbal interference (Athanasopoulos & Bylund) | [b11-b13, d04, d05] | [S] (K07) |
| LLM: reasoning models think in English whatever the input | MATH-500 English prefill vs target prefill: Swahili 57.4/25.9, Spanish 88.0/72.5, Telugu 70.0/46.2, Japanese 84.9/66.3, Korean 83.7/75.4, Russian 86.7/81.6, Chinese 87.7/85.9. Mismatch over 90% for QwQ-32B and Qwen3-30B-A3B | Language Matters [a22] | [E] (K10) |
| LLM: forcing thinking language costs accuracy | Matching 46% to 98%, mean accuracy 26% to 17%. R1-32B AIME 25.5 to 17.0, GPQA 40.3 to 33.4, MGSM 70.2 to 71.7. Skywork-32B AIME 44.8 to 29.6 | Qi et al. 2025 [d09] | [E] (K10) |
| LLM: output diversity depends on thinking language | NoveltyBench Distinct Score English/non-English/mixed: Qwen3-8B 28.55/36.00/43.73; 14B 26.20/31.45/38.00; 32B 35.00/40.30/46.53; R1-Distill-14B 38.33/46.03/52.07. Gain 5.3 to 7.7; quality drop 1.02 to 2.24; r=0.72-0.88 | arXiv 2601.11227 [a21] | [S] (K14) |
| LLM: voting across reasoning languages beats a monolingual control | PolyMath, R1-Distill-Qwen-7B, 18 languages: Low UL-XCoT 83.8 vs UL-CoT 65.5; Medium 31.1 vs 26.3; High 13.6 vs 12.3; Top 10.6 vs 9.4; over 50% fewer tokens than prior sampling baselines | UL-XCoT [d13] | [S] (K19) |
| LLM: self-translate to English | Mean of 5 tasks: XGLM 7.5B +2.2, LLaMA 13B +2.8, LLaMA 30B 43.1 to 46.6 (+3.5). LLaMA 30B: XNLI 37.0 to 43.5, PAWS-X 50.9 to 55.6, XCOPA 55.2 to 58.4, XStoryCloze 56.7 to 59.0, MGSM 15.5 to 16.3 | Etxaniz 2023 [c08, c09] | [S] (K12) |
| LLM: verbal CoT hurts tasks where verbalising hurts people | Face recognition after description: GPT-4o 64.0 to 51.2, Claude 3 Opus 44.0 to 29.6, Gemini 1.5 Pro 66.0 to 54.6, Claude 3.5 Sonnet 97.8 to 94.8. Artificial grammar: GPT-4o 87.5 to 64.4; o1-preview 57.7 vs GPT-4o zero-shot 94.0 | Liu et al. 2024 [d15] | [S] (K21) |

## 4. Mechanisms and models

**4.1 Production pipeline (Levelt).** Stages: (1) macro-planning picks the goal of the message; (2) micro-planning picks which event features to encode, using the language's obligatory distinctions; (3) formulation picks words and syntax; (4) articulation. Thinking for speaking is stage 2. An engineer's reading: a *message template* is chosen by output language, and the template decides which slots must be filled [a13, a20].

**4.2 Obligatory-slot model.** Each language has required slots. A verb-framed language needs a path verb; manner is optional. A satellite-framed language needs a manner verb. Speakers fill required slots by default and fill optional slots by effort or interest. Evidence: Swedish 97% one frame; Spanish speaker-driven variation (speaker SD 2.37 vs event SD 0.78) [b08]. To implement for an agent: define the output schema first, list required fields, and let it fill required fields before optional ones.

**4.3 Time course.** Attention to event parts begins in the first second of motion (before speech, median onset 1267 ms) and reverses by the third second [a04]. Reading: planning for the format begins early and is front-loaded. For an agent: fix the output format before the thinking starts, not after.

**4.4 Compensation account.** Without a speaking task, people attend equally across languages while the event runs, then after it ends they study the component their language does not routinely encode [a05]. Memory costs show up only for the group that does this compensation (Greek, 73/71 vs English 90/88) [a06]. Mechanism: language-linked strategy, not perception.

**4.5 Language-as-strategy.** If a task invites labelling (similarity ratings, memory with verbal encoding), the language's label categories bias the judgement. Verbal interference (shadowing) removes some effects [b05, d04]. Implementation: a label-priming step before the judgement shifts the judgement toward the label's categories (K04, K20).

**4.6 Attention drives structure.** Cueing an entity raises its chance of being the sentence subject [a07]. Gaze and sentence structure interact both ways. Implementation: a cue on an entity in the prompt changes what the answer foregrounds.

**4.7 Goal bias.** Endpoints are attended and mentioned more than sources, in English speakers. Speaking shifts attention a bit toward Source [b07]. Implementation: audit plans for under-covered sources and preconditions.

**4.8 LLM latent-language model.** Logit lens on Llama-2 (7B, 13B, 70B) shows three phases: early layers carry input-language form, middle layers carry the concept with higher probability on English tokens, final layers move to the output language [c03, c04]. Task design: single-token translate, repeat, cloze. Schut et al. (Llama-3.1-70B, French, German, Dutch, Mandarin) find that content words route through English-close representations and non-lexical words do not; steering with English-computed vectors works better [c05, c06, d16]. Zhong et al. show the training mix sets the latent language: Llama2 English only, Swallow and LLM-jp use English and Japanese [c07]. Aya-23-35B is the least English-centric of four, Gemma-2-27b the most [d16]. Wendler and Schut differ mainly in task design (single vs multi-token) [K22]. Reasoning-trained models were not tested in either.

**4.9 Language-consistency RL.** M-Thinker trains with GRPO using a language-consistency reward plus a cross-lingual alignment reward. It gives near 100% consistency and better accuracy, so the cost of non-English reasoning is a property of current models, not of the language [d11].

**4.10 Cross-lingual agreement as signal.** Elhady et al. reward the same answer across equivalent problems in different languages: up to +21.7% average on MGSM over 10 languages, +18.2% on unseen MGSM languages, up to +6.2% on 3 out-of-distribution sets (Qwen2.5-Instruct 1.5B/7B/14B). Soegeng et al.: +5.03% on English queries in BLEnD [d14].

## 5. What holds up

**Holds (production differences).** English vs Greek, Spanish and Turkish speakers differ in what they say [a03, b05, b08, a16]. Swedish-Spanish consistency differs [b08]. Established, but it is an output fact, not a cognition claim.

**Contested (cognition without speech).**
- Papafragou 2008 and Lee et al. 2026 find no language effect on attention or segmentation without speaking [a05, a16].
- Goller 2017, Fu 2023 and Soroli 2024 find language effects without speaking [b14, d01, d03]. Soroli: French 78% vs English 59% path-congruent in a non-verbal categorisation, but the gap is larger in the verbal task (English 67% manner vs French 41%) [d03].
- Reconciliation attempt: effects grow as language involvement grows. Fu 2023 saw opposite patterns in detection vs sentence verification. Athanasopoulos and Bylund: effects vanished under verbal interference (second-hand) [d02, d04, K20]. Explicit similarity ratings invite covert labelling [critique].

**Statistical weaknesses.**
- Printed p-values in Papafragou 2008 look one-tailed. F1(1,16)=4.01 printed p=.03 is about .06 two-tailed; F1(1,25)=4.95 printed .01 is about .035 [critique].
- The first-look interaction is only marginal by items (F2(1,11)=3.61, p=.08); the first-second time-window interaction is significant by items (F2=10.14) [critique].
- Typical N is 17 to 47 per group. Heavy exclusions: about 15% (Papafragou memory), 27 of 128 (Chen eye analysis) [critique].
- No pooled effect size. No large (over 100 per group) or preregistered replication of the 2008 gaze-timing result was found [K24]. Closest: Fu et al. 2023 (51-55 per group) and Soroli 2024 (20 per language), both with different paradigms.

**Moderators.** Event type: bounded vs unbounded [a03]. Task: speaking vs memory vs similarity [a05, a06, b05]. Verbal interference removes effects in the aspect study [d04]. Age: Turkish adults and some 5-year-olds use more units; 4-year-olds do not; eye dwell identical across ages [b16]. L2 proficiency: L2 learners slower at all levels [b18]. Language pair: Basque vs Spanish modulates agent accuracy but not consistently across tasks [a14].

**Interventions that worked (humans).** Verbal interference reduces language effects (second-hand) [d04]. Verbal guidance before an action shifts attention to goals and memory (N=35, one language) [b19].

**Did not work or limits.** Bilingual switching and aspect results were never opened in numbers [K07]. The future-tense effect reversed sign [d18]. Slobin's own evidence is all linguistic [d06]. BICAUSE direction is inconsistent across models [b09].

**Source independence.** a03-a06 and b01-b03 are one paper. a23, b09, b10, c12, c13 are one paper. Chen 2026 (a17, b07) is one paper. Note: evidence a17 words the Goal-bias speaking effect differently; the direction in b07's numbers (speaking raised attention to Source) is used here [critique].

## 6. Language models

No study was found that gives an LLM or vision-language model motion clips in several languages and measures manner and path verb rates against human speakers [K17, a25, c22, d19]. This is a search gap under rate limits, not proof of absence. The studies below are the nearest.

**6.1 What language the model thinks in.**
- Reasoning models default to reasoning in a high-resource language whatever the input language. Reasoning and answer language mismatch over 90% for QwQ-32B and Qwen3-30B-A3B [a22].
- Forcing target-language reasoning (prefill) cuts MATH-500 accuracy: Swahili 57.4 to 25.9 (-31.5), Telugu 70.0 to 46.2 (-23.8), Japanese 84.9 to 66.3 (-18.6), Spanish 88.0 to 72.5 (-15.5), Korean 83.7 to 75.4, Russian 86.7 to 81.6, Chinese 87.7 to 85.9 [a22]. MMMLU Swahili 48.8 vs 35.3. A cultural benchmark gained +1.0 to +2.9 with target-language reasoning [a22]. The page had internal inconsistencies in benchmark sizes.
- XReasoning (6 models, AIME24/25, GPQA, MGSM, 11 languages, 370 questions): default matching 46.3% AIME, 42.3% GPQA, 94.0% MGSM for Distill-R1-32B; a prompt hack raised matching 46% to 98% and cut mean accuracy 26% to 17% [d09]. Zhao et al. agree: compliance under 0.2 for Bengali and Yoruba under explicit instruction; prompt hacking gives full compliance and lower accuracy [d10].
- Fix: language-consistency RL (M-Thinker) restores near 100% consistency with better accuracy [d11]. So the penalty belongs to current models.
- Open: frontier models and non-math tasks.

**6.2 Latent concept space.** English-biased by logit lens on Llama-2 and Llama-3.1-70B [c03, c05]. Wendler: concept space closer to English with a language-neutral element; Schut: content-word route via English in open generation [c05, c06]. Training mix changes it [c07]. Contested [K11, K22].

**6.3 Translate first.** Self-translate beats direct on 5 multilingual tasks, and gains grow with size: +0.3 (smallest XGLM), +2.2, +2.8, +3.5 [c08]. Per task for LLaMA 30B: XNLI +6.5, PAWS-X +4.7, XCOPA +3.2, XStoryCloze +2.3, MGSM +0.8 (flat for small models that solve almost nothing) [c09]. Counter: PaLM-540B CoT average 44.9% (4 underrepresented languages) vs 47.9% (6 high-resource), a 3-point gap (Native-CoT average, not per language); EN-CoT and translate-EN were as good as or better than native-language steps [c10, c11].

**6.4 Language as a source of diversity.** The nearest LLM analogue to thinking for speaking: the language a reasoning model thinks in changes the diversity of its English answers. 15 thinking languages, 100 questions per benchmark. Non-English raises NoveltyBench Distinct Score 5.3 to 7.7 points over English; mixed-language thinking adds more; quality drops 1.02 to 2.24; r=0.72-0.88 with language distance from English [a21]. In the DeepSeek row Mixed (52.07) is below S-best (52.42), so mixed is not always best [critique]. Qwen3 and one distill only.

**6.5 Language as a source of correct candidates.**
- UL-XCoT (7B distill, PolyMath, 18 languages): voting over a few chosen languages with early pruning beat a same-pruning monolingual control: 83.8 vs 65.5 (Low), 31.1 vs 26.3, 13.6 vs 12.3, 10.6 vs 9.4. On MMLU-ProX-Lite (29 languages) CLSP 40.5 to UL-XCoT 43.6 [d13]. Single source; not strictly equal tokens; no frontier models.
- polyGRPO: Qwen2.5-7B on MGSM, average accuracy by response language: en 64.22, zh 65.09, es 63.31, fr 63.24, ru 62.98, ja 60.65, de 60.55, th 57.38, sw 42.29, bn 39.45, te 19.42; unconstrained 63.16. English questions: en 81.2, zh 87.2, es 84.8, fr 84.0. Training gives +6.72 on four English reasoning sets, +6.89 multilingual, +4.9 English commonsense [d12].
- Elhady and Soegeng use cross-lingual agreement as a training signal (section 4.10) [d14].

**6.6 Describe-first and verbal overshadowing in models.** Liu et al.: CoT lowers accuracy on tasks where verbalising hurts people (section 3). Three other tasks hurt people but not models, so the parallel is partial. Not a Gennari design [d15, K21].

**6.7 Language effects on knowledge.**
- Colour naming: GPT-4 agreement with human naming 0.59 (CI 0.56-0.63) English, 0.54 Russian; GPT-3.5 0.50/0.50; GPT-3 0.39/0.35; lab ceiling 0.73-0.75; humans 103 English and 51 Russian. Dominant siniy 18 chips (GPT-4) vs 29 (human); goluboy 33 vs 26; turquoise 46 vs 15 [c01, c02]. Text-only BERT-family embeddings align with CIELAB, and alignment grows with model size [c17, c25].
- BICAUSE (Qwen1.5-1.8B): forward En 91.0, Zh 91.2; reversed En 88.5, Zh 76.5 (table 76.8). Gaps shrink with scale (14B 97.5 both). Llama-3.2-3B is better in Chinese (27.0 vs 56.8), so direction varies [a23, b09, c13, K15].
- 81-language embeddings: socio-cultural adjusted dissimilarity .874 vs nature and motion .924 (mBERT, difference .0503, CrI .0470-.0537; 3,240 pairs) [d17].
- Latin motion annotation: GPT-4 Goal F1 about 0.82, Path 0.79, Source 0.77; small Llama recall 1.00, precision 0.19-0.26, F1 0.33-0.41 (over-labels Goal) [c14, c15].
- Name overlap only: Thinking While Speaking (290,571 examples, 7 small models, within 6.3% of the frontier Reasoner), Think-Before-Speak (multi-agent social simulation), Quiet-STaR (GSM8K 5.9 to 10.9, CommonsenseQA 36.3 to 47.2) [c19-c21, K18].

## 7. What our agent should take

Verdict: little to add now. The human findings are about gaze and memory in speakers and have no direct LLM test. The usable pieces are the LLM measurements on reasoning language.

### Add now (established)

1. **Do not force the reasoning language to equal the input language.** Let the model reason in its strongest language (usually English). Keep the answer language as the task requires. Do not use prompt hacks that force thinking language. Schema part: S0 (mode choice) and G7 (a setting that does not pay for itself is dropped). Status [E] (K10). Evidence: a22, c04, c05, c07, d09, d10, d11, d16. Cost: nothing; it is a default.
2. **Check output language by code, not by the model.** If the task requires an answer language, code compares the answer's language with the required one (models mismatch reasoning and answer language over 90% of the time in some setups, so the answer language needs a code check). Schema part: S8 VERIFY / G5. Status [E] for the failure (a22, d09, d10); the check itself is a design choice, not evidence.
3. **Nothing from the human eye-tracking results enters the schema.** Reasons in section 9.

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Branches reasoned in different languages (diversity and correctness at equal tokens) | S3 / O3, G4 | [S] K14, K19 | a21, d12, d13, d14 |
| Translate to English before answering on non-English items | S1 / O1 | [S] K12 | c08, c09, c10, c11 |
| Describe-first step before a judgement (shifts toward label categories; may hurt) | O1/O2, S2 | [C] K04, K20, K21 | a06, b05, d03, d15 |
| Fix output format first, then plan (format-first vs free planning) | S0 / G | [S] K02 | a04, b02, a20 |
| Entity cue in prompt changes what is foregrounded (an anchoring check) | S1 input hygiene | [S] K08 | a07, a09, b21 |
| Goal-bias audit of plans: source and precondition coverage | G / S2 | [S] K09 | a17, b07 |
| Slobin-style motion test on VLMs and LLMs (manner/path rates by language) | none (background) | [S] K17 | c14, d19 |

Cautions from SCHEMA.md: G4 (samples from one model are not independent) and G9 apply. Language-diverse branches are not persona voters, but they must still beat a same-language branch set at equal tokens. Section 4b says bias checklists did not reliably work, so the goal-bias checklist is low priority.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, same model, same items, code-graded.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 100 items each from MATH-500 and GPQA (plus our bench items with a check) | A: N branches all reasoned in English. B: N branches reasoned in N different languages (for example en, zh, es, de, ja), answers in English. Same token cap | Pass rate of the code-selected answer; candidate diversity (distinct answers); pairwise error overlap | B raises diversity. Correctness gain unknown; UL-XCoT suggests a gain on small models; expect near zero on frontier |
| T2 | Non-English items (MGSM, XNLI) | A: direct. B: self-translate to English then answer. Translation tokens count against B's budget | Accuracy | +2 to +4 points for mid-size models, near 0 on math (c08) |
| T3 | Judgement tasks with exceptions: similarity, category assignment, pattern rules; implicit tasks if available | A: no describe step. B: describe first, then judge. C: distractor step of the same length | Accuracy; shift toward the described category | B below A on implicit tasks (d15). Gennari-type shift expected on similarity items |
| T4 | Items that need a fixed output schema (JSON plans) | A: plan freely, then format. B: schema stated first, plan then fill it | Field coverage, accuracy, token count | Small gain in field coverage; accuracy unknown |
| T5 | 60 planning items with a source or precondition and a goal | A: plain plan. B: plan plus a code-run coverage check of preconditions | Share of plans naming source and preconditions; plan validity | Goal over-mention like 97.7 vs 87.5 expected; gain from the check uncertain (4b) |
| T6 | 50 motion-event clips or text scenarios in en, es, el, tr | Same prompt in each language; no scaffold | Manner-verb rate and path-verb rate by language (code-counted) | If models mimic speakers: en more manner than es/el. A measurement, not an arm test |
| T7 | Our open-ended items (NoveltyBench style) | A: English thinking. B: forced non-English thinking, English answer | Distinct Score; quality score | +5 points diversity, -1 to -2 quality (a21) |

## 9. What does not transfer, and why

- **Gaze and attention timing.** The core human result is eye position before speech. An LLM has no gaze. The nearest analogue (which input parts the model attends to first) has not been measured against language [K02].
- **Perception and memory without speech.** In a text-only setting an LLM has no non-linguistic channel, so the contested debate on silent perception has no analogue for our agent.
- **Habitual language-trained attention.** Slobin's claim needs a child learning a first language. A frozen model carries training statistics, not a development history.
- **Human effect sizes.** N is 17 to 47 per group, one language pair per study, and the key effects are modest and partly contested. They are weak grounds for any engineering rule.
- **BICAUSE and colour naming.** Output-language habits and statistics of text. Small models carry the headline numbers and gaps shrink with scale [c13].
- **Name-overlap papers (Thinking While Speaking, Think-Before-Speak, Quiet-STaR).** They do not test Slobin. The agent-level analogue, a private plan before the answer, is already covered by schema states [K18].
- **Sign of grammar effects.** Robertson 2025 reversed the expected sign [d18]. Caution against extending grammar-to-cognition reasoning to agent rules.
- **Model-size dependence.** Many LLM language effects are large in small models and shrink with scale (BICAUSE 14B 97.5 both). Results from 7B distills (UL-XCoT, XReasoning) may not hold on frontier models.

## 10. Open questions

1. Does a large or preregistered replication of Papafragou 2008 gaze timing hold (over 100 per group; English-Greek, English-Spanish or English-Turkish)? [K24]
2. What do Slobin 1996 and Berman and Slobin 1994 show at page level, with frog-story manner and path rates by language and age? [K23]
3. Do vision-language models given the same motion clips in several languages show human-like manner and path verb differences? None found [K17].
4. Does a describe-first step in an agent shift later judgements toward description-language categories, and does it help or hurt at equal tokens? [K04, K21]
5. Do language-diverse reasoning branches help at strictly equal tokens on frontier models, with correctness and diversity both measured? [K19]
6. Why do Wendler and Schut disagree, and does reasoning-model training change the latent language? [K22]
7. How large is the penalty for input-language reasoning on frontier models and non-math tasks? [K10]
8. Do the aspect-language and bilingual-switching results hold in numbers when opened? [K07]
9. Does the Goal bias appear in LLM-written plans, and does a checklist reduce it? [K09]

## 11. Sources

[V] = opened and read this session (full page or PDF text). [M] = snippet, abstract only, or second-hand.

**Human studies**
- [M] Slobin (1996) From "thought and language" to "thinking for speaking". https://philarchive.org/archive/SLOFTA (403) [a01, b20, c24]
- [V] Wikipedia, Linguistic relativity. https://en.wikipedia.org/wiki/Linguistic_relativity [a02]
- [V] Papafragou, Hulbert and Trueswell (2008) Does language guide event perception? https://pmc.ncbi.nlm.nih.gov/articles/PMC2810627/ [a03-a06, a20, b01-b04, d07]
- [M] Gleitman, January, Nappa and Trueswell (2007). https://pmc.ncbi.nlm.nih.gov/articles/PMC2151743/ [a07, b21]
- [V] Bunger, Trueswell and Papafragou (2012). https://pmc.ncbi.nlm.nih.gov/articles/PMC3246065/ [a08]
- [V] Bunger, Papafragou and Trueswell (2013). https://pmc.ncbi.nlm.nih.gov/articles/PMC3780438/ [a09]
- [V] Gennari, Sloman, Malt and Fitch (2002) Motion events in language and cognition. https://doi.org/10.1016/s0010-0277(01)00166-4 [b05, b06, d06]; a10 was an earlier memory-based summary [M]
- [M] Berman and Slobin (1994) Relating events in narrative [a11]
- [M] Talmy (1985; 2000) [a12]
- [M] Levelt (1989); Griffin and Bock (2000) [a13, b22]
- [V] Isasi-Isasmendi et al. (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10320828/ [a14]
- [V] Montero-Melis (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8042225/ [a15, b08]
- [V] Lee, Unal and Papafragou (2026) Event segmentation. https://pmc.ncbi.nlm.nih.gov/articles/PMC13347761/ [a16, b15]
- [V] Chen, Papafragou and Trueswell (2026) Goal bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC13382187/ [a17, b07]
- [V] Unal et al. (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11358469/ [a18] (abstract and introduction only)
- [V] Coco et al. (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC12930141/ [a19, b17]
- [V] Thierry (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC5006882 [b11]
- [M] Athanasopoulos et al. (2015); von Stutterheim, Flecken, Carroll (2012-2014); Bylund and Athanasopoulos (2013-2014), via Thierry [b12, b13, b24]
- [V] Goller et al. (2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5770776 [b14]
- [V] Turkish children and adults (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13110846 [b16] (abstract and partial text)
- [V] Chinese learners of English (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6902645 [b18]
- [V] Contrastive verbal guidance (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12352477 [b19]
- [M] Gerwien and von Stutterheim (2018) [b23]
- [V] Fu, Vanek and Roberts (2023/2024). https://eprints.whiterose.ac.uk/id/eprint/237284/1/matched-or-moved-asymmetry-in-high-and-low-level-visual-processing-of-motion-events.pdf [d01, d02]; d04 and d05 are second-hand descriptions of other papers inside it [M]
- [V] Soroli (2024) Language and Cognition 16(4). https://www.cambridge.org/core/product/D5D6FCC7D91D98DD3D56AA3EB28F0BBE [d03]
- [V] Robertson et al. (2025) PLoS One. https://pmc.ncbi.nlm.nih.gov/articles/PMC12112090/ [d18]
- [M] Search snippet on framing type and non-verbal categorisation. https://core.ac.uk/download/323053848.pdf [c23] (link not verified)

**LLM and AI studies**
- [V] Language of Thought Shapes Output Diversity in LLMs. https://arxiv.org/html/2601.11227 [a21]
- [V] Language Matters. https://arxiv.org/html/2505.17407v1 [a22]
- [V] Under the Shadow of Babel (BICAUSE). https://arxiv.org/abs/2506.16151 [a23, b09, b10, b25, c12, c13]
- [M] Prompt and response language and content generation, id 2608.26186 (unverified id). https://arxiv.org/pdf/2608.26186 [a24]
- [V] Marjieh et al. (2023). https://arxiv.org/abs/2302.01308 [c01, c02]
- [V] Wendler et al. (2024). https://arxiv.org/abs/2402.10588 [c03, c04]
- [V] Schut, Gal and Farquhar (2025). https://arxiv.org/abs/2502.15603 [c05, c06, d16]
- [V] Zhong et al. (2024). https://arxiv.org/abs/2408.10811 [c07]
- [V] Etxaniz et al. (2023). https://arxiv.org/abs/2308.01223 [c08, c09]
- [V] Shi et al. (2022). https://arxiv.org/abs/2210.03057 [c10, c11]
- [V] Farina et al. (2025) Latin motion. https://ceur-ws.org/Vol-4112/42_main_long.pdf [c14, c15]
- [V] Mahowald et al. (2024). https://arxiv.org/abs/2301.06627 [c16]
- [V] Abdou et al. (2021). https://arxiv.org/abs/2109.06129 [c17, c25]
- [V] Human Language Shapes Emerging Physical Reasoning in LLMs. https://arxiv.org/abs/2609.20666 [c18] (exact accuracies not read)
- [V] Thinking While Speaking. https://arxiv.org/abs/2511.07397 [c19]
- [V] Think-Before-Speak. https://arxiv.org/abs/2606.03137 [c20]
- [V] Quiet-STaR. https://arxiv.org/abs/2403.09629 [c21]
- [V] Qi et al. (2025) XReasoning. https://arxiv.org/abs/2505.22888 [d09]
- [V] Zhao et al. (2025). https://arxiv.org/abs/2510.09555 [d10]
- [V] M-Thinker. https://arxiv.org/abs/2510.07300 [d11]
- [V] polyGRPO. https://arxiv.org/abs/2604.21593 [d12]
- [V] UL-XCoT. https://arxiv.org/abs/2604.20090 [d13]
- [V] Elhady et al. https://arxiv.org/abs/2606.01464; Soegeng et al. https://arxiv.org/abs/2605.22137 [d14]
- [V] Liu et al. (2024) Mind Your Step. https://arxiv.org/abs/2410.21333 [d15]
- [V] Wang, Qin and Liu (2026) 81 languages. https://arxiv.org/abs/2610.30778 [d17]
- [M] Search notes (no LLM Slobin test found; page-level access to Slobin blocked) [a25, c22, d08, d19]

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 4 established claims: 2 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A15.05-K01** (reworded: the sources support less). Numbers verified (72% vs 36%; 97% vs 59%), but 'reliable' overstates: Montero-Melis's point is that Spanish descriptions are inconsistent (59% verb-framed, 35% satellite, variation mainly from the speaker), and the English/Greek result is 17 speakers per language. Corrected claim: Speakers' event descriptions show language-specific tendencies of differing consistency: English speakers used manner verbs in bounded events more than Greek speakers (72% vs 36%, 17 per group), and Swedish speakers used the satellite frame in 97% of caused-motion descriptions versus only 59% verb-framed in Spanish, where variation came mainly from the speaker.
- **A15.05-K10** (reworded: the sources support less). Numbers and the three-group trade-off check out (Tam et al., Qi et al., Zhao et al.), but M-Thinker's abstract only reports near-100% consistency and 'superior performance' on MMATH/PolyMath; it does not show the accuracy cost disappears, so 'the cost belongs to current models and not to the language itself' is an unsupported inference. Corrected claim: Reasoning LLMs think mostly in English whatever the input language, and forcing reasoning in the input language lowers accuracy (MATH-500 Swahili 57.4 to 25.9; Spanish 88.0 to 72.5; XReasoning prompt hack raised matching from 46% to 98% and cut mean accuracy from 26% to 17%, with AIME 25.5 to 17.0 for Distill-R1-32B). Three independent groups agree on the trade-off. Language-consistency RL (M-Thinker) reaches nearly 100% consistency with reported gains on MMATH and PolyMath, suggesting the problem may be fixable in training, though the paper's abstract does not show the accuracy cost vanishes.
