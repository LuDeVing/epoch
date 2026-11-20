# Whorfian psychophysics: deep document

*Subfield A15.06. Written from evidence_a-d.jsonl (a01-a28, b01-b28, c01-c26, d01-d21), claims.jsonl (K01-K23) and critique.md in this folder. Verdict of the subfield for our agent: background only. Most schema mappings are "none". [V]/[M] marks are in section 11.*

## 1. What it is

Whorfian psychophysics is Casasanto's name for tests of linguistic relativity that use non-linguistic tasks. The person does not speak or read words during the measurement. They reproduce a pitch, judge a line's duration, place a card, press a key or tell two colours apart. If the answer shifts with the language they speak, language has reached "below" language use.

Casasanto (2016, Routledge Handbook of Semantics) splits relativity into two kinds:
- Thinking for speaking: language shapes thought only while you are about to speak or listen (the Shallow View).
- Effects beyond language use: long-term experience with a metaphor reshapes non-verbal mappings (the Deep View).

Non-verbal psychophysics is the discriminating test between the two (b21). His Language (2016) paper adds a continuity claim: linguistic, cultural and bodily experience work by one mechanism. Experience strengthens some implicit associations in memory and weakens others. Language is not special (d01). Only that abstract was read. The handbook chapter was not opened (a22).

Domains covered:
- Time and space: does talk of time as "ahead/behind", "up/down", "long/short" or "much/little" change how people lay out or estimate time?
- Pitch: "high/low" (Dutch) versus "thin/thick" (Farsi, Turkish).
- Colour: do Russian blue words speed discrimination?
- Reading direction, a rival cultural cause.

Why it matters for us: our agent has no non-verbal channel. Every input and output is text. So only the Shallow View (online wording effects) can be tested on a language model directly (b21). The subfield mainly gives method lessons: how a wording effect should be tested, how fragile such effects are, and which confounds fake them. No study tests a Whorfian time, space or pitch effect on an LLM's behaviour (K15, d20).

## 2. History and theories in depth

**Sapir-Whorf, strong and weak.** The strong form (language determines thought) is rejected. The weak form (language biases some habits of thought) has mixed support. Boroditsky 2001 itself says language "does not entirely determine" thought (a01).

**Boroditsky 2001.** English talks of time mostly on a horizontal axis (ahead, behind). Mandarin also uses vertical terms: shang (up, earlier) and xia (down, later). Prediction: Mandarin speakers show a vertical bias on time tasks even when working in English (a01-a03).

**Metaphor Theory versus a Theory of Magnitude (ATOM)** (a09):
- ATOM (Walsh 2003): space, time and number share one analog magnitude system. Interference should be symmetric.
- Metaphor Theory (Lakoff and Johnson 1999): time depends on space asymmetrically, as language does.
Casasanto and Boroditsky (2008) found distance leaks into duration judgements but not the reverse, favouring Metaphor Theory (a07, b01). ATOM defenders point to task artefacts (discriminability, a persistent visible space cue). Bottini and Casasanto (2013) removed one such artefact by making the stimuli vanish at the end (a08).

**Shallow versus Deep View.** Casasanto (2010) framed it: if language only matters while speaking, non-verbal tasks should show no cross-language difference. If it matters deeply, they should differ in line with metaphor use (b21). That chapter predates the failed replications (b10) and the 2020 pitch results, and its author favours the Deep View.

**Rival explanation: cultural artefacts.** Reading and writing direction, not spoken metaphor, may produce horizontal time layouts (Fuhrman and Boroditsky 2010, a17; Casasanto and Bottini 2014, b16). Chen and colleagues argued the Mandarin vertical bias tracks vertical text experience (b10-b12).

**Associative learning account.** Each use of a metaphor strengthens a mapping between two domains. It predicts a dose-response with phrase frequency and that training moves people (b28).

**Bayesian view.** Cibelli et al. (2016): a universal perceptual space plus language-specific categories. Categories matter most when perceptual memory is uncertain. This explains why some effects do not replicate (b20).

**Infant data.** Infants of 3 to 4 months prefer height-pitch congruence (Walker et al. 2010, via b28). Dolscheid 2014 (second-hand) found 4-month-olds sensitive to both height and thickness (a11). So the adult language-specific mapping looks like a selection from a shared early set, not a creation by language.

**Timeline.**
- 2001: Boroditsky Mandarin-English priming.
- 2004 to 2010: Casasanto distance-versus-amount metaphors (English, Greek, Indonesian, Spanish). Kuuk Thaayorre east-west time cards (Boroditsky and Gaby 2010).
- 2007 to 2008: three failed replications of the 2001 result (Chen; January and Kako; Tse and Altarriba). 2007: Winawer Russian blues.
- 2011 and 2013: Dolscheid Dutch-Farsi pitch. 2011 to 2017: Taiwan versus China tied to reading habit. 2013: Lai and Boroditsky meeting question.
- 2020: pitch associations (thickness shared, height differs); Russian blues close replication fails.
- 2021: Tsimane' show no stable direction. 2022: Yang et al. find a vertical effect again. 2025: Crossley and Bylund, reading not writing.
- 2023 to 2026: LLM work (section 6).

## 3. Core findings with exact numbers

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Mandarin speakers answer purely temporal earlier/later questions faster after vertical primes; English faster after horizontal | English horizontal 2128 vs vertical 2300 ms, F(1,25)=13.76. Mandarin earlier/later vertical 2347 vs horizontal 2503 ms; before/after horizontal 2340 vs vertical 2509. Three-way F(1,44)=5.24. N=26 English, 20 Mandarin | Boroditsky 2001 (a02) | Contested; three failed replications |
| Vertical bias fell with earlier age of English acquisition | r=.47 (N=25, p<.01); exposure years r=.12; one outlier at 582 ms | a03 | Single-source |
| Training English speakers in vertical time talk gave a Mandarin-like pattern | N=70, 90 training questions; vertical 2185 vs horizontal 2262 ms; interaction F(1,68)=10.25 | a04 | Single-source; lasts minutes |
| Failed replications of the 2001 result | Chen 2007 (four attempts reported); January and Kako 2007 (six experiments, English monolinguals); Tse and Altarriba 2008 (both groups faster after vertical prime). Ns and effect sizes not read | b10, b26, d02-d04 | Contested |
| Mandarin vertical bias depends on region and reading | Taiwan: vertical bias; China: none or reversed. N=56 per site; vertical prime interaction F(1,3952)=18.51, horizontal prime F(1,3927)=.35 | Chen et al. 2011/2017 (b10-b12) | Contested |
| Vertical advantage in Mandarin monolinguals, not English | N=91 (51 Mandarin, 40 English); Language x Direction (vertical) F(1,89)=12.58, eta_p2=.124; Mandarin t(50)=-5.76, d=.806; English p=.33 | Yang et al. 2022 (b13) | Single-source; conflicts with Chen |
| Learning English did not move Mandarin bilinguals | Proficiency x Axis x Direction F<1 (df 1,92) | b14 | Single-source |
| Bilinguals keep two timelines | 736 ms compatible vs 772 ms incompatible in both orientations; three-way F(1,42)=4.90 | Miles et al. 2011 (d05) | Single-source |
| "Move the meeting forward" resolved as Friday | English 68.2% (n=66), bilingual 38.2% (n=55), Mandarin 0% (n=51); chi2(1,N=121)=9.7. Clock question, 2 pm: 100% / 41.0% / 12.5% | Lai and Boroditsky 2013 (a05) | Single-source; test site confounded (beta=1.583) |
| Spatial cues steer the layout bilinguals draw | Vertical 40% after up-down cues vs 19% after front-back; sagittal 24% vs 11%; N=98 | a06 | Single-source |
| Space distorts time, not the reverse | Exp 1: 162 lines, 200-800 px, 1-5 s. Dutch children F(1)=16.53, r2=.09; Brazilian F(1)=8.69, r2=.05 | Casasanto 2010; Bottini and Casasanto 2013 (b01, a08) | Replicated across languages (human) |
| English distance vs Greek amount metaphors predict non-verbal time bias | Language x Task F(1,56)=10.41, p=.002; N about 60 | Casasanto 2010 (b02) | Single-source |
| 30 min amount training moves English toward Greek | difference 0.89, t(28)=1.73, p<.05; N about 30 | b03 | Weak |
| Dutch height vs Farsi thickness shape sung pitch | N=40 per group; Language x Task F(1,79)=10.73, p=.002; Dutch height > Farsi t(38)=2.65; Farsi thickness t(38)=2.00, p=.05 | Dolscheid et al. 2011/2013 (b04) | Single-source (conference numbers) |
| 20 min thickness training makes Dutch Farsi-like | N=60; thickness slope 1.46 vs 0.08; group contrast t(58)=1.84, p=.07 | b05 | Weak; key contrast not significant |
| Thickness-pitch is shared; height-pitch differs by language | Thickness above chance in both (Dutch 95%, d=2.58); height-pitch language difference chi2(1)=54.72; thickness chi2(1)=.91, p=.34; N=40 per group | Dolscheid et al. 2020 (b07) | Single-source |
| Thick-high vs thin-low conflict | Turkish pick height-pitch 15%, t(39)=-9.71, d=-1.54; 36 of 39 (92%) thickness. Dutch 50% (17 of 35 height) | b08 | Single-source; Dutch split in two strategy groups |
| Tall/short and high/low map to pitch (metaphor), not polarity | high/low t=4.5; front/back t=0.2; tall/short works, big/small does not; Exp 2 N=24 | Dolscheid and Casasanto 2015 (a10, a11) | Single-source |
| Reading direction, not writing, flips time layout | Reading N=64: standard 87.5% past-left vs mirror about 53% (baseline unresolved: 46.9% or 53.1%); chi2=9.06, BF10=25.58. Replication N=64: 78.1% vs 40.6%, BF10=30.71. Writing nulls BF10=.23 and .24; 5-day writing 23% vs 25.8%, p=.77 | Crossley and Bylund 2025 (b15) | Replicated (human) |
| Mian speakers use three layouts | N=9: 6 body-relative (4 left-right, 2 sagittal), 3 absolute east-west | a15 | Tiny N |
| Tsimane' have no stable direction | N=60; all three domains same direction 42% (CI .32-.54); number-size 80%, size-time 61%, time-number 53% | Pitt et al. 2021 (a14) | Single-source |
| Russian blue boundary speeds discrimination | Winawer 2007: abstract only read; baseline about 180 ms | a13, b19 | Contested |
| Close replication of Russian blues fails | N=18 Russian, 20 English; boundary effect chi2(1)=1.10, p=.29; boundary x language chi2(1)=1.19, p=.28 | Martinovic et al. 2020 (b17) | Failed replication |
| Russian category boundary shifts with trial frequency | Only the Russian boundary moved | b18 | Single-source |
| Probes recover space and time from LLM activations | Llama-2-70b linear R2 at 60% depth: world 0.911, USA 0.864, NYC 0.359, historical 0.835, headlines 0.746 | Gurnee and Tegmark 2024 (a23) | LLM; established |
| Causal-order accuracy by prompt language | Qwen1.5-1.8B reversed: En 88.5 vs Zh 76.5; Mistral-7B paraphrased 93.8 vs 81.5; Qwen 14B 97.5 vs 97.5, 32B 90.5 vs 94.0, 72B 97.0 vs 96.2 | Wang et al. 2025 (b22, d10, d11) | LLM; single-source |
| Discounting by prompt language | Larger-later chosen 22% GPT-3.5, 16% GPT-4, 34.5% GPT-4 with CoT; weak vs strong FTR CIs [1.715,1.948] vs [1.948,2.210] | Goli and Singh 2024 (c01, c02) | LLM; contested |
| LLM pitch similarity | GPT-4 r=.92 with 55 humans, English only | Marjieh et al. 2023/2024 (c04, d13) | LLM; height-vs-thickness untested |
| LLM colour naming by language | ARI vs humans: English 0.59, Russian 0.54 (ceiling 0.73-0.75) | d14 | LLM; single-source |

## 4. Mechanisms and models

Each is described so an engineer could build a test or a toy model.

**M1. Asymmetric cross-domain interference (Metaphor Theory).**
- Setup: source S (space) and target T (time), varied independently per trial.
- Prediction: error on T grows with the irrelevant S value; error on S does not grow with irrelevant T.
- Implementation: fit the slope of T-judgement on S, and of S-judgement on T. Asymmetry = slope_TS minus slope_ST. ATOM predicts about zero; Metaphor Theory predicts clearly positive.
- Human size: r2 .05 to .09 in children (a08). Small.

**M2. Metaphor-frequency (associative) strengthening.**
- Each use of "high pitch" strengthens a height-pitch link; each "thick sound" strengthens thickness-pitch.
- Prediction: mapping strength scales with phrase frequency. Short training with the other phrase shifts it, weakly and briefly (a04, b03, b05).
- For a model, the analogue is training-corpus phrase frequency. We cannot change it, only the prompt wording.

**M3. Selection from an innate set.**
- Infants hold both height-pitch and thickness-pitch links (a11, b28). Language keeps one strong and lets the other fade: height-pitch differs by language, thickness-pitch is shared (b07).
- Implementation: a mapping with two weights. Language sets the relative gain, not the existence.

**M4. Online language-use effect.**
- Winawer's advantage was reported to vanish under verbal interference (a13, b19). The meeting-question answer depends on current language and immediate cues (a05, a06). Reading vertical text just before a task creates a vertical bias; horizontal text removes it (b11).
- Implementation: effect = f(current context cues) + small chronic term. For a text model every effect is of this type, and the context window is the "just-read" input.

**M5. Bayesian category-plus-perception model (Cibelli et al. 2016).**
- Estimate = precision-weighted mix of a noisy perceptual signal s and a category prototype c: posterior mean = (s/sp2 + c/sc2) / (1/sp2 + 1/sc2). Weight on the category rises when perceptual noise sp2 is high.
- Prompt reading: wording should matter most when the input is ambiguous or underspecified. This is the only mechanism with a clear prediction for prompts (b20). It was fit to earlier data, not preregistered.

**M6. Culture-practice route (reading direction).**
- The time axis follows reading direction. Minutes of mirror reading flip it. Writing practice does not (b15).
- A model analogue would be token order, not meaning (K05). Untested.

**M7. Ambiguity resolution by frame.**
- "Move the meeting forward" is ambiguous. Ego-moving reading: we move toward the future, so forward means later (Friday). Time-moving reading: the meeting moves toward us, so forward means earlier (Monday).
- Implementation: a binary frame variable whose prior is set by context (spatial primes, language) (a05). A text model can be run on this question with different primes. Nobody has done so (d20).

**M8. Linear internal coordinates in LLMs.**
- Linear probes recover latitude, longitude and year from hidden states. R2 peaks mid-depth and rises with scale. There are single space and time neurons (a23).
- Implementation: ridge regression from layer activations to coordinates. This is a representation fact. It shows information present, not used, and is not a Whorfian effect.

## 5. What holds up

**Replicates well (human).**
- Space-to-time asymmetry across languages and ages (Dutch and Brazilian children; Casasanto 2010; Bottini and Casasanto 2013). Small effects, one lab family (K02). It is the same in each language, so it shows a general space-to-time dependence, not a language effect (a08).
- Reading direction shapes the horizontal time line. Mirror reading flips it (Bayes factors 25.6 and 30.7). Writing-only manipulations give clean nulls (BF10 .23, .24) (b15).
- Thickness-pitch is shared across Dutch and Turkish; height-pitch differs (b07).
- Spatial priming steers the layout of time inside bilinguals (a06).

**Failed or fragile.**
- Boroditsky 2001 priming: three failed replications. Per-study N and effect sizes were not recovered because the papers are paywalled (K01). Tse and Altarriba partly replicated the bilingual half, but both groups were faster after vertical primes (d04).
- Partial rescue: the vertical bias appears in Taiwan, not China, and follows vertical reading (b10-b12). Yang 2022 (N=91) found a vertical effect again in a mainland sample. The literature stays split.
- Russian blues: Martinovic 2020 found no boundary effect (p=.29) with N=18 and 20. A frequency-context shift survived in Russian speakers only (b17, b18).
- Linguistic-savings hypothesis (future tense and patience): randomised wording tests found no causal effect (c24, search summary only). Two direct tests found that more future-tense use predicted less discounting (N=235 and N=606, d07, d08).
- Grammatical gender: not supported in embeddings once noun meaning is controlled (a27, a28; K16).
- Tsimane' and Mian: no stable direction; education confounds language (a14, a15).

**Moderators and boundary conditions.**
- Task type: association and interference tasks give different pictures of the same pitch mapping (b07 vs b04).
- Individual strategy: Dutch speakers split 49/51 between height and thickness in the conflict task (b08). Group means hide the split.
- Verbal load: removed the Russian-blues advantage in the original claim (a13).
- Immediate context: reading direction just before the task overrides a supposed chronic effect (b11, b16).
- Perceptual uncertainty: category effects are largest when memory is noisy (b20).
- Sample: Farsi speakers in the Netherlands are bilingual and acculturated (b04). Different test sites confound language (a05).

**Interventions.**
- Worked, weakly and briefly: 20 to 30 minutes of metaphor training (a04, b03, b05). The 20-minute thickness contrast between trained groups was p=.07 (b05). The amount-training contrast was t=1.73 (b03). No retention test.
- Did not work: writing-direction practice, even 5 days (b15). Learning English did not move Mandarin timelines (b14).

**Overall.** Effects are tens of ms to about 170 ms, or r2 near .05 to .09. Samples are 20 to 100 people. Several rest on one lab. Treat the line as small, context-sensitive and fragile.

## 6. Language models

No LLM study tests Whorfian psychophysics as this subfield defines it. About 29 web and API queries across two passes found none on ego-moving versus time-moving framing, the space-time distance-duration asymmetry, or height-versus-thickness pitch wording (K15, K17, d20). API tools were rate-limited, so absence is only partial evidence.

**Representation of space and time.** Llama-2 holds linear coordinates for place and date. R2 at 60% depth, 70b: world 0.911, USA 0.864, NYC 0.359, historical figures 0.835, entertainment 0.885, headlines 0.746. 7b: world 0.881, headlines 0.564 (a23). Larger models do better; nonlinear probes add little. (The 0.896 row in c15 is the 13b row, per critique.)

**Perception from text.** Colour-term embeddings align with CIELAB (RSA tau up to about 0.33; warm better than cool) (a24). GPT-4 predicts human pitch similarity at r=.92, loudness .89, colour .84 to .89, consonants .57, taste .54, timbre .42, and recovers octave equivalence (c04, d13). Image co-training gave no domain-specific gain (c06). Across 39 models in 6 families, larger instruction-tuned models name colours more like English speakers; only Gemini 2.0 recovers the human range of complexity (c07).

**Language as a variable on behaviour.**
- Wang 2025 (BICAUSE, 400 samples per language). Qwen1.5-1.8B forward: 91.0 En vs 91.2 Zh. Reversed: 88.5 vs 76.5. Second table (paraphrased data): Mistral-7B 93.8 vs 81.5; Qwen 1.8B 88.5 vs 76.8; Qwen 14B 97.5 vs 97.5; 32B 90.5 vs 94.0; 72B 97.0 vs 96.2. The plain table has Llama-3.2-3B at 27.0 En vs 56.8 Zh. The gap changes direction by model and shrinks with scale. No data-mix control exists, so language and training frequency are not separated (K11). Attention followed typology (Chinese focused more on causes); SVCCA 0.73 EN-ZH forward, 0.64 EN forward vs reversed (b22).
- Goli and Singh (22 languages). GPT-3.5 chooses larger-later 22%, GPT-4 16%, GPT-4 with CoT 34.5%. Malay 37.2% (GPT-3.5) and 29% (GPT-4) down to Russian 6.6% and 4.9%. Language ranking changes with the elicitation method. Weak-FTR CIs [1.715,1.948] vs strong-FTR [1.948,2.210] touch. Strong-FTR explanations mention risk 20% less, opportunity cost 13.8% less, urgency 8.3% less. Unreplicated, and the human mechanism failed direct tests (K12).
- Zhang and Rayz 2026. Qwen3-4B and 30B give frame-dependent similarity for real events. Under the deictic frame similarity falls sharply for the future and slowly for the past. Under the sequential frame it is strongly negative between separated events. 2,916,927 deictic entries. No effect sizes, English only (d12, K23).
- Marjieh 2024 colour naming. GPT-4 ARI 0.59 English vs 0.54 Russian, with different partitions from the same hex codes. Dominant-category chips: sinij 18 (GPT-4) vs 29 (humans); goluboj 33 vs 26 (c05, d14). This is vocabulary, not discrimination speed.
- Wang (2026): much of the cross-language colour difference is a spelling artifact. Spelling similarity explains 0-5% of alignment in English and Spanish, 32-71% in Chinese (r=0.84 with the share of self-naming terms). On a matched 43-colour set four languages are not separable (d16). Layer geometry is shared early (congruence 0.61-0.71 at layer 0) and diverges late (0.29-0.56) (d15).
- 81-language embeddings: sociocultural concepts correspond more across languages than nature-and-motion ones (RSA dissimilarity .883 vs .921 mBERT; .938 vs .973 XLM-R). Static embeddings only (a26).

**Space frames.** VLMs prefer the English egocentric frame with reflected front-back mapping, even across 109 languages (GPT-4o); Hausa and Tamil still get the English pattern. Under explicit frame prompts accuracy is 47 to 63% (GPT-4o 60.3%; egocentric prompt 78.3%) (c11, c12). Llama3-70B swaps left and right; best conversion 55.5%; humans above 90%; Spatial-Guided prompting raised perspective identification by 2.9% to 30% (c13). Cardinal directions: above 0.8 on simple items, best 0.595 on complex, only 5.10% of questions solved by all models (c14). MENTALMAP (13 LLMs, 8 languages): viewpoint-taking (L3) is under half of L0 everywhere. Humans also score 0% at L3 on the text task, so the authors read the cliff as a text working-memory limit, not language. CoT +32 pp DeepSeek-V4-Flash, -16 pp Qwen2.5-7B at L3 (b24).

**Sound-shape.** CLIP 52% (AUC 0.77) and Stable Diffusion 80% (AUC 0.74) vs humans 89% on kiki-bouba (c18). GPT-4o and CLIP only partly show the effect (c19). GPT-4 iconicity ratings Spearman about .54 to .58 with humans; Llama-2 70B .304 (c20). Preregistered human tests confirmed model-derived letter profiles (N=1,388; 85.3% selected items) (c21). GPT-4 reproduced four human manner-of-motion studies, Spearman .73 to .96 (c22).

**Imposed vocabulary on agents.** Jehu-Appiah 2026 (preprint; N=4,470 trials; 7 tasks; three models): No-Have raised ethical reasoning +19.1 pp (p<0.001), classification +6.5, calibration +7.4, with 92.8% compliance. E-Prime ranged from -27.5 pp (GPT-4o-mini calibration) to +42.3 pp (Gemini ethics); cross-model r=-0.75. A 3-agent ensemble with different vocabulary constraints covered 100% of ground truth vs 88.2% on 17 debugging problems. No length-matched control (d18). Yoruba prompting: cultural grounding index 0.795 vs 0.128, n=10 pairs, one model, topic confounded (d17).

**Summary.** (1) Models carry linear space and time axes. (2) Prompt language changes outputs, but through vocabulary, topic, data mix and model idiosyncrasy. (3) The gaps shrink with scale in the one set tested. (4) Wording constraints can move reasoning, with a sign that depends on model.

## 7. What our agent should take

Honest summary: the subfield supplies method cautions, not new schema parts. The items touching the schema restate guardrails we already have.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | When claiming a wording or prompt-language effect on our agent, control the confound first (length, topic, translation quality, training-language share, vocabulary and spelling). The field's best-known effects failed or shrank under such controls. A bench discipline, not a prompt rule. | G7 (equal tokens) | [E] | b10-b12, b17, d16, a28, b15 |
| A2 | Context just before a task can override a supposed chronic language effect, so the first lines of the context window matter more than the prompt language. Already covered by S1 input hygiene. | S1 | [E] for humans | b11, b16, a04, b03 |
| A3 | Do not add metaphor-priming prompts ("think of time as moving up") as a scaffold element. Human metaphor priming is short-lived, small and fragile. Candidate for section 4b. | none | [E] that human priming is fragile | b03, b05, a04, K01 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | State the temporal and spatial frame explicitly in prompts that depend on direction ("forward = later"). Humans resolve the ambiguity by frame cues; LLM time judgements are frame-dependent. | S1 | [S] | a05, a06, d12, c13 |
| T2 | Re-ask a question in a second language or paraphrase and log disagreement as a wording-sensitivity probe. Gaps appear around 7B and shrink at scale. | S0 (class record), G4 | [S] | b22, d10, d11 |
| T3 | Vocabulary-constraint diversity as one ensemble member (No-Have, E-Prime), with a length-matched control. | S3 | [S], preprint | d18 |
| T4 | Space-time asymmetry: does an irrelevant distance cue shift an LLM's duration answer more than the reverse? | S1 hygiene | human [E], LLM untested | a08, b01, K15 |
| T5 | Explicit reference-frame statement raises spatial accuracy at equal tokens. | S1 | [S] | c13, c11 |
| T6 | Probe our model's linear time and place axes before designing a spatial scratchpad. Low prompt value. | memory | [E] representation | a23 |
| T7 | Pitch height versus thickness wording on an acoustic judgement task. | none | untested | c04, d13 |

## 8. Concrete tests on our bench

All tests compare two arms at equal total tokens, with the same items and fixed seeds. Report the difference with a bootstrap CI over items.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) Frame statement | 60 ambiguous time-direction items ("move the meeting forward") keyed given the stated frame, plus 60 left/right perspective items | A plain; B plus one line fixing the frame | Accuracy; disagreement across 3 samples | +5 to +15 pp on perspective items if the c13 gain carries; about 0 on unambiguous items |
| B2 (T2) Prompt-language gap | 100 existing single-answer bench items, translated two ways into 2 languages | A original; B translation; same max_tokens | Accuracy gap; cross-language agreement | Under 2 pp at our working size if scale holds; 5 to 12 pp if near 7B (Mistral-7B gap 12.3 pp) |
| B3 (T3) Vocabulary-diverse member | 40 checked problems (code or arithmetic with a check) | A 3 plain members; B 2 plain plus 1 No-Have or E-Prime. Equal tokens | Ground-truth coverage; final accuracy | Coverage up only if diversity is real; likely null on easy checked items |
| B4 (T4) Space-time interference | Path lengths (200-800 m) and walk times (1-5 min); judge time with an irrelevant distance cue and distance with an irrelevant time cue | Cue present vs removed | Slope of the judgement on the irrelevant dimension, both directions | slope_TS > slope_ST likely (time words borrow space words); size unknown |
| B5 (T5) Spatial frame | 80 FoREST- or COMFORT-style items | A plain; B explicit frame or Spatial-Guided | Accuracy | +3 to +30 pp where context and question share a perspective (c13) |
| B6 (T7) Pitch metaphor | 40 pitch-order and interval items described as tones | high/low vs thick/thin wording | Accuracy; r with human similarity | Probably none; tells us whether wording metaphors move numeric judgement |
| B7 (A3) Metaphor prime | 60 duration-estimation items | A no prime; B 5-line distance prime; C amount prime | Shift of estimate vs distance and quantity cues | Small; analogue of the Casasanto distance-versus-amount training |
| B8 Order bias | 60 time-ordering items | events listed forward vs reversed vs shuffled | Accuracy | Gap >= 5 pp would justify an order-shuffle step |

Run order is in UNKNOWNS.md.

## 9. What does not transfer, and why

- **Reaction-time and psychophysical measures.** An LLM has no speeded non-verbal response. Millisecond priming (Boroditsky 2001) has no analogue. Token counts are not reaction times.
- **Chronic language experience.** The Deep View needs years of use. A prompt gives minutes. Even for humans, 20 to 30 minutes of training gave weak, brief effects (b03, b05).
- **Reading direction.** Mirror reading and writing practice act through scanning. Token order is the nearest analogue and is untested.
- **Infant, field and bodily data.** Pre-verbal mapping, Tsimane', Mian and Kuuk Thaayorre tell us about human origins, not a text model.
- **Colour discrimination.** The Winawer effect is a perceptual speed advantage and its close replication failed (b17). LLM naming differences are vocabulary effects, partly spelling artifacts (d16).
- **Cross-language LLM gaps as Whorfian evidence.** They mix data mix, translation quality, spelling and topic. No study separates these.
- **Human strategy splits.** The Dutch 49/51 split (b08) has no direct model equal, though sampling spread behaves similarly. Averages hide spread.
- **Low relevance.** The subfield's own tag is "background only". Mapped schema parts are mostly none.

## 10. Open questions

1. Do ego-moving or time-moving wording, or spatial primes, shift LLM answers to ambiguous time questions? (0 direct studies, K15)
2. Does the space-time asymmetry (distance distorts duration more than the reverse) appear in LLM estimates?
3. Does the Goli and Singh language effect replicate on other models with translation-quality and training-share controls? The human mechanism failed (d07, d08).
4. Is the Chinese-English causal-order gap a language or data-mix effect, and does it persist above 7B in other families (b22, d10, d11)?
5. What are the Ns and effect sizes of the three failed replications of Boroditsky 2001? What does Casasanto 2016 conclude about robustness (K21, abstract only)?
6. What is the exact mirror-reading baseline in Crossley and Bylund 2025 (46.9% or 53.1%)?
7. Do Zhang and Rayz asymmetries survive effect sizes, other languages and other models (d12)?
8. Is there a Winawer-style discrimination effect in vision-language models? One search summary reports a language-conditioned colour boundary shift only in language-aligned VLM layers (c09, b25, not opened).
9. Does pitch-metaphor wording change an LLM's acoustic judgement?
10. Which human effects hold under preregistered large-N replication? The Mandarin-English time work has none.

## 11. Sources

[V] = opened and read in the evidence pass. [M] = snippet, abstract or citation only.

**Human, time and space**
- [V] Boroditsky 2001. http://lera.ucsd.edu/papers/mandarin.pdf
- [V] Lai and Boroditsky 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3621230/
- [V] Bottini and Casasanto 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3817359/
- [V] Casasanto 2010, Space for Thinking. https://casasanto.com/papers/Casasanto_SpaceForThinking.pdf
- [M] Casasanto and Boroditsky 2008 (via a07). https://pmc.ncbi.nlm.nih.gov/articles/PMC3817359/
- [M] Casasanto, Boroditsky et al. 2004. https://doi.org/10.1167/4.8.2
- [M] Boroditsky and Gaby 2010. https://doi.org/10.1177/0956797610386621
- [M] Fuhrman and Boroditsky 2010. https://doi.org/10.1111/j.1551-6709.2010.01105.x
- [V] Fedden and Boroditsky 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3503482/
- [V] Pitt et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8357228/
- [V] Chen et al. 2011 (abstract page). https://escholarship.org/uc/item/0w11p20c
- [V] Chen, Friederich, Shu 2017. https://escholarship.org/uc/item/2zs378dp
- [M] Boroditsky, Fuhrman, McCormick 2011. https://www.morrissey.unibe.ch/lecture/02_Boroditsky_et_al_%282011%29_English_and_Mandarin_speakers_think_about_time.pdf
- [V] Yang et al. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8867009
- [V] Miles et al. 2011. https://doi.org/10.3758/s13423-011-0068-y
- [V] Crossley and Bylund 2025. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/E6EF809D0235A311468C83167059623E/S1866980825100082a.pdf/direction-of-reading-not-writing-shapes-concepts-of-time.pdf
- [M] Casasanto and Bottini 2014. https://escholarship.org/uc/item/8xt744x6
- [M] Chen 2007. https://doi.org/10.1016/j.cognition.2006.09.012
- [M] January and Kako 2007. https://doi.org/10.1016/j.cognition.2006.07.008
- [M] Tse and Altarriba 2008. https://doi.org/10.1163/156853708x358218
- [M] Chen and O'Seaghdha 2013 review. https://scholar.lib.ntnu.edu.tw/en/publications/do-mandarin-and-english-speakers-think-about-time-differently-rev-2/

**Human, pitch**
- [V] Dolscheid et al. 2011 (CogSci). https://escholarship.org/uc/item/9jx5103t
- [M] Dolscheid et al. 2013 (Psych Sci). https://www.mpi.nl/publications/item767564/thickness-musical-pitch-psychophysical-evidence-whorfian-hypothesis
- [M] Dolscheid et al. 2014. https://pure.mpg.de/pubman/item/item_1936459_6/component/file_2056418/Dolscheid_etal_pss_2014.pdf
- [V] Dolscheid et al. 2020. https://eprints.whiterose.ac.uk/158204/1/Pitpitch_Cognition_Final.pdf
- [V] Dolscheid and Casasanto 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4659873/

**Human, colour, theory, economics**
- [M] Winawer et al. 2007. https://pmc.ncbi.nlm.nih.gov/articles/PMC1876524/
- [V] Martinovic et al. 2020. https://hira.hope.ac.uk/3058/1/Martinovic%20Paramei%20MacInnes_Cognition_2020_postprint.pdf
- [V] Cibelli et al. 2016. https://cocosci.princeton.edu/papers/SapirWhorfColor.PDF
- [M] Casasanto 2016, Routledge Handbook chapter. https://doi.org/10.4324/9781315685533
- [M] Casasanto 2016, Language (abstract only). https://doi.org/10.1111/lang.12192
- [V] Future tense and discounting, PLOS ONE 2025. https://doi.org/10.1371/journal.pone.0317422
- [M] Chen, He, Riyanto 2019 and Angerer 2025 (search summary). https://www.cambridge.org/core/journals/journal-of-the-economic-science-association/article/effects-of-language-on-patience-an-experimental-replication-study-of-the-linguisticsavings-hypothesis-in-austria/B4921969CF497425BCD4895C778D4E6B

**LLM and AI**
- [V] Gurnee and Tegmark 2024. https://arxiv.org/abs/2310.02207
- [V] Abdou et al. 2021. https://arxiv.org/abs/2109.06129
- [V] Wang et al. 2025, Babel. https://arxiv.org/abs/2506.16151 and https://aclanthology.org/2025.findings-emnlp.1321.pdf
- [V] Wang, Qin, Liu 2026, 81 languages. https://arxiv.org/abs/2610.30778
- [V] Kann 2019. https://arxiv.org/abs/1910.09729
- [V] Stanczak et al. 2023. https://arxiv.org/abs/2311.18567
- [V] Zhang and Rayz 2026. https://arxiv.org/abs/2510.16685
- [V] Pan et al. 2026, MENTALMAP. https://arxiv.org/pdf/2605.28277
- [M] Maharjan and Cangelosi 2026 (VLM relativity). https://escholarship.org/uc/item/3r30c3b5
- [V] Goli and Singh 2024. https://arxiv.org/abs/2305.02531
- [V] Marjieh et al. 2023/2024. https://arxiv.org/abs/2302.01308 and https://doi.org/10.1038/s41598-024-72071-1
- [V] Imel and Zaslavsky 2026. https://arxiv.org/abs/2509.08093
- [M] Akbarinia et al. 2024. https://www.biorxiv.org/content/10.1101/2024.01.25.577209.full.pdf
- [V] Zhang et al. 2025, COMFORT. https://arxiv.org/abs/2410.17385
- [V] Premsri and Kordjamshidi 2025, FoREST. https://arxiv.org/abs/2502.17775
- [V] Cohn and Blackwell 2024. https://arxiv.org/abs/2406.16528
- [V] Alper and Averbuch-Elor 2023. https://arxiv.org/abs/2310.16781
- [V] Verhoef et al. 2024. https://arxiv.org/abs/2407.17974
- [V] Loakman et al. 2024. https://arxiv.org/abs/2409.14917
- [V] Zhao 2026. https://arxiv.org/abs/2603.17306
- [V] Illan Castillo and Valenzuela 2025. https://arxiv.org/abs/2507.10342
- [V] Cultural interpretability 2024. https://arxiv.org/abs/2411.05200
- [V] Loyola et al. 2026. https://arxiv.org/abs/2610.18331
- [V] Wang, R. 2026, colour spelling. https://aclanthology.org/2026.oracle-main.33.pdf
- [V] Yoruba prompting preprint (Zenodo). https://doi.org/10.5281/zenodo.19540639
- [V] Jehu-Appiah 2026, Umwelt Engineering. https://arxiv.org/abs/2603.27626
- [M] Pratim Ray 2025 (via d19). https://doi.org/10.5281/zenodo.19540639
- [V] He et al. 2026, LLMs value human time. https://arxiv.org/abs/2610.18515

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 6 established claims: 2 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A15.06-K02** (reworded: the sources support less). Dutch and Brazilian samples in Bottini and Casasanto 2013 are children only (Dutch 4-9y, Brazilian 6-10y); the adult evidence is English (and Greek) in Casasanto 2010, so 'Dutch, Brazilian adults' is wrong; the metaphor-frequency link comes from the English vs Greek corpus and tasks in Casasanto 2010. Corrected claim: Space influences time estimates more than time influences space in English-speaking adults (Casasanto 2010) and in Dutch and Brazilian Portuguese-speaking children (Bottini and Casasanto 2013, interference x target dimension F=16.53 and 8.69), and English vs Greek speakers' asymmetries follow how often each language uses distance vs amount words for time (Casasanto 2010).
- **A15.06-K05** (reworded: the sources support less). Claim says reading and writing direction drive the timeline, but Crossley and Bylund 2025 find reading, not writing, matters; '(not spoken metaphor)' is not tested by either paper (they show orthography can shift the timeline independent of language, not that metaphor is irrelevant); the mirror baseline is resolved by the paper: 46.9% mapped past to the right, so 53.1% past-left. Corrected claim: Reading direction, not writing direction, shapes the horizontal mental timeline: mirror-reversed reading reversed Dutch speakers' space-time congruity (Casasanto and Bottini 2014), and in Crossley and Bylund 2025, 87.5% placed the past on the left after standard reading vs 53.1% after mirror reading (replication 78.1% vs 40.6%), while mirror-writing manipulations did not change the mapping.
- **A15.06-K14** (reworded: the sources support less). FoREST's 55.5% is the best accuracy only for converting from camera-given context to the relatum's perspective (Llama3-70B CoT); the reverse direction reaches 82.4% for GPT-4o, so '55.5% best conversion' is too broad. COMFORT 47-63% (InstructBLIP 47.2, XComposer2 63.3, GPT-4o 60.3) and humans above 90% match. Corrected claim: VLM spatial frame-of-reference reasoning is weak and prompt-dependent: COMFORT aggregate accuracy under explicit frame prompts is 47-63% (GPT-4o 60.3%); in FoREST the hardest direction (camera-perspective context to relatum-perspective question) tops out at 55.5% (Llama3-70B CoT) while the reverse direction reaches 82.4% for GPT-4o; humans exceed 90%.
- **A15.06-K16** (reworded: the sources support less). Stanczak et al. 2023 does control for noun meaning (gender-adjective link near zero), but Kann 2019 does not control meaning, it only finds embedding evidence against the neo-Whorfian prediction in 9 languages; both are distributional-model analyses, so they cannot show that grammatical categories do not produce the human behavioural effect. Corrected claim: Distributional-embedding analyses do not support a neo-Whorfian grammatical-gender effect: Kann 2019 (9 languages) finds evidence against it, and Stanczak et al. 2023 find the gender-adjective relationship near zero once noun meaning is controlled; this concerns text-based models, not human cognition.
- **A15.06-K03** (now single-source: only one opened source, code check).
- **A15.06-K04** (now single-source: only one opened source, code check).
