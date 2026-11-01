# Methods: parsimony: deep document

Subfield A18.09, comparative cognition. Evidence files: evidence_a-d.jsonl (ids a01-a29, b01-b28, c01-c26, d01-d17), claims K01-K23, critique.md. Many LLM papers appear on several lines (Ullman a19/b10/c01, Shapira a21/b12/c03, Kosinski a18/b13/c05, Sap b17/c14). Counts below are papers, not lines.

Search limits: the web search quota ran out and the arXiv, OpenAlex and Semantic Scholar APIs rate-limited. "No one tested X" below means "not found in this reading", not "does not exist".

## 1. What it is

Morgan's canon is a rule from comparative psychology. It tells a researcher not to explain an animal's act by a higher mental faculty if a lower one can explain it. It is a rule for choosing between rival explanations of a single pass on a test.

It is not Occam's razor. "Simpler explanation" does not mean "simpler mechanism". "Lower" has been read as simpler, implicit, reflexive, or phylogenetically older (a10, b01). Nothing independent justifies preferring the lower one (a05, a13, b01).

The part that survives scrutiny is a method, not the preference. When a test passes, name the cheap rival (a cue, an association, a surface pattern). Find a test where rival and rich account predict different things. Run it. Pfungst's Clever Hans work is the model case. Heyes's ghost control and Penn and Povinelli's nine-condition design are the sharper versions.

Why this matters for our agent. Guardrail G3 says a pass must be on something the answer was not fitted to. Morgan's method is G3 stated for a mind. In LLM work the cheap rival is almost always "surface statistics or memorised test items". The method then becomes the perturbation twin, the cue ablation, the true-belief control and the contamination check. Nobody has put the canon itself inside an agent loop (K17). The nearest tested operator, a forced generic self-review, hurt accuracy (d05).

Scope. Animal-side numbers matter only as method templates. The weight is on how the method behaves on LLMs, and on what is safe to add to a schema.

## 2. History and theories in depth

### 2.1 Morgan (1894, 1903)

C. Lloyd Morgan (1852-1936) wrote against Romanes, who built animal mind from anecdotes and read in human-like thought freely (a01, a03).

- 1894 wording, as quoted by Heyes, Bruni and Mikhalevich: in no case may an action be interpreted as the outcome of a higher psychical faculty if it can be explained by one lower in the scale.
- 1903 edition (p. 59): no animal activity is to be interpreted in terms of higher psychological processes if it can be fairly interpreted by processes lower in the scale.
- 1903 rider (via de Waal 2002): a higher reading is fine if the species has independently shown high intelligence (a02).

Morgan's own method was observation and control. He hatched chicks, ducklings and moorhens away from adults to separate inherited from learned acts. His terrier Tony learned to open a garden gate by gradual steps, which he used to argue insight was not needed (a03). Tony is his own anecdote, one animal.

Source quality: the wording is from Wikipedia and Heyes, not the 1894 book. Wording differs by source (faculty, mental, psychical).

### 2.2 Pfungst and Clever Hans (1904-1911)

Hans the horse answered arithmetic by tapping. A 13-member Stumpf commission found no trick in September 1904 (a04). Pfungst then varied one thing at a time: isolate the horse, use other questioners, use blinders, vary whether the questioner knew the answer.

Pfungst's own text, checked on Project Gutenberg (d01): 102 blinder tests. Not seen: 35 tests, 2 correct (6%). Seen: 56 tests, about 50 correct (89%). Undecided: 11 tests, 18% correct. Large blinders (15 x 15 cm) were needed; small ones did not work. Secondary reports quote 50/56 and 2/35 and hide the 11 undecided tests. Counts are tests, not animals. One horse.

Lesson drawn by Samhita and Gross (b09): after Pfungst, experimenters avoided face-to-face contact with subjects, and the authors say the lesson is still applied loosely.

What carries over: a differential test that removes the suspected cue channel. Hans was not "dumb". He was smart in an unexpected channel. The cheap rival explained the behaviour, and it was found by ablation, not by argument.

### 2.3 The philosophical critique (1990s-2017)

Mercado (2016) and Starzak (2016, seen only through Mercado) argue the canon has no sound basis (a13, b01, b02):

- Claimed justifications (digs deeper, protects from error, checks anthropomorphism, promotes validity checks) lack evidence.
- "Lower" is read several ways, and the readings disagree.
- Animal data rarely separate the explanations, so the jury is deadlocked.
- Strict use may bias researchers toward under-attributing cognition.

Sober showed Morgan's own Method of Variation is too permissive to justify the canon. Fitzpatrick (2008) proposes evidentialism. Starzak (2017) says the canon lacks operational hierarchies (a17, second-hand).

Bruni, Perconti and Plebe (2018) list seven criticisms (a11): conflated with Occam; parsimony is not clear-cut; Morgan was more liberal than his followers; strict avoidance failed in practice; it guards one error only (anthropomorphism, not anthropodenial); burden-of-proof bias; reductio by analogy. Failure in practice: Hebb (1946) at Yerkes found that strict avoidance of anthropomorphic description gave "an almost endless series of specific acts" with no order.

Alternatives (a12): critical anthropomorphism (Burghardt), evidentialism (Fitzpatrick), constructive anthropomorphism (Arbilly and Lotem 2017). Cases where the richer reading later won: honey bee dance (von Frisch 1927), rat 50 kHz play chirps (Panksepp 1998). The authors picked these examples.

### 2.4 Heyes: both poles are errors (2012, 2014)

Heyes names two errors: association-blindness and simple-mindedness (a05). Associative learning is a contender, not a default winner. Morgan never justified the canon. She asks that rivals be specified well enough to predict differently.

- Ghost control (a06): replay the unwrapping sound with the partner absent. If the prosocial bias stays, associative learning explains it. If it vanishes, the cognitive account gains. Based on Horner et al. 2011 (six female chimpanzees, dual-reward token bias only with a partner present). Proposed, not run in this paper.
- Breadth of conditioning (a07): found in every major taxon studied; in humans it predicts IQ beyond working memory and speed (counts cited, not given).
- Submentalizing (Heyes 2014, b26, second-hand): low-level domain-general processes predict others' behaviour. Suggested test: inanimate controls.

### 2.5 Penn and Povinelli (2007): a sceptic's protocol

Behaviour cues can predict an agent's acts with no mental-state variable. A mental-state account must do unique causal work beyond cues (a08). They note a folk-psychology account is simpler for us, not for the animal to implement.

Proposed discriminating designs (a09): a five-bucket competitive design with nine conditions (removed uninformed, replaced, misinformed, swapped); an opaque-visor begging test. Corvid re-caching results (Emery and Clayton 2001, Dally 2006, Bugnyar and Heinrich 2006) are explained by simple rules. Visor: enculturated chimps failed (Vonk et al. 2005, unpublished); 18-month-olds passed a blindfold version (Meltzoff 2007). The authors are sceptics; the paper is a review.

### 2.6 Mikhalevich, Powell and Logan (2017)

Flexible behaviour does not prove complex cognition, and a simple explanation does not imply a simple mechanism. They use an Adaptive Triadic Model: flexibility plus ecology plus neuroanatomy (a10). Their only real tie-breaker is more evidence. Example: cleaner wrasse have one of the largest diencephalons among 25 perciform species compared.

### 2.7 Researcher attitudes (2021, 2025)

Farrar, Ostojic and Clayton (2021, a14, d02): 1,001 invited, 969 emails delivered, 210 completed (21.6%). 70.5% say the canon is important (31.9% strongly); the exact 70.5% string was not re-found in the re-read, only "over 70%". 39.7% sometimes and 38.8% often hope for a result. 89.6% say replication is important. 70.8% disagree that there are enough replications in their area. Median predicted replication success 65% (IQR 50-75%). Self-selected sample.

Voudouris et al. (2025, a15, b24): over 200 comparative psychologists use the canon as a parsimony principle, not as an associative-versus-cognitive rule. Abstract only. Auersperg (2025, a16): the canon began as a call for rigour and became a rigid slogan, yet still limits over-interpretation and pushes mechanism specification. Abstract only.

### 2.8 Spread outside animals

A 2026 parasitology perspective (b28) uses the canon to argue for passive activation of existing host responses as the null before crediting parasite-designed control. A small pilot (a sterile nylon implant linked to lower energy use and nest desertion in Polistes dominula) is archived; sample sizes not extracted. Not an LLM study.

### 2.9 Arrival in LLM research

- Hagendorff et al. (a29, abstract only) propose psychology-style behaviour experiments on LLMs and warn human-designed methods may not transfer.
- Niven and Kao (2019, a25, abstract only): BERT hit 77% on the Argument Reasoning Comprehension Task, 3 points under untrained humans, from spurious cues; on an adversarial set all models fell to chance.
- McCoy, Pavlick, Linzen (2019, c18): HANS. NLI models trained on MNLI, including BERT, follow lexical-overlap heuristics; on items where the heuristic fails they score near zero.
- Kosinski (2023) claimed false-belief ability in GPT-4; Ullman and Shapira ran Hans-style tests (sections 5 and 6).
- Pang et al. (2025, b16/c06) letter: apply the comparative toolkit. Morgan's canon may lack justification, but association-blindness is also a mistake. Rivals: associative learning, explicit training on ToM-like items, pattern matching in human text. Proposed a goggles-style transparent-container test. No data.
- Strachan et al. (2024, a24) wrote novel items and warn that the regular structure of false-belief and faux pas items allows Clever Hans solutions. They never mention the canon by name (a23).
- Hu, Sosa and Ullman (2025, a28/c07): disagreement comes from an unclear target. Three nested meanings of "has ToM": match human behaviour, match the human computation, match a theory-like generative model. A behavioural pass supports only the first.

## 3. Core findings with exact numbers

Status: established = several independent sources; single = one paper; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Clever Hans blinder control | 102 tests: 35 not seen, 2 right (6%); 56 seen, ~50 right (89%); 11 undecided, 18% | Pfungst 1911 text (d01, a04, b09) | established |
| Owner-cue test in dogs | 69 dogs. Pointing, owner blind N=17 p=.003; enhancing N=18 p=.002; decreasing N=17 p=.003; no pointing N=17 p=.839 (chance); owner active N=16 p=.001; pointing+owner active N=15 p=.059. Only 3 dogs per pointing group individually above chance | Schmidjell 2012 (b08) | single |
| Ape false-belief, inanimate control | 22/43 (51.2%) anticipatory looks vs 22/30 (73.3%) original; first look to target 14/22, p=.28; FB1 6/11 p=1.0; FB2 8/11 p=.23 | Kano 2017 (b03); 22/30 second-hand (d03) | contested |
| Infant anticipatory-looking replication | 160 tested, 70 excluded, 90 kept. 49/90 (54%) anticipated at familiarisation vs 20/31 (65%) original. At test 22/49, p=.568 | Kampis 2021 (b05) | established |
| Implicit ToM, submentalizing test | First saccades FB1 7/12 (58%) p=.774 BF10=0.64; FB2 5/7 (71%) p=.453 BF10=0.97; TB1 9/16 (56%) p=.804 BF10=0.57. 13, 18, 9 participants made no look | Kulke and Rakoczy 2019 (b06) | established (null) |
| Dot-perspective task, cloak and goggles | No mentalizing signature in 3 experiments; empathy scores did not predict performance | Conway 2017 (b07) | single |
| Researcher survey on the canon | 210/1,001 (21.6%); 70.5% important; 39.7% sometimes and 38.8% often hope for a result; 89.6% replication important | Farrar 2021 (a14, d02) | single |
| GPT-4 false belief (headline) | 75% of 40 tasks, CI 66-84%, R=0.98 between task types; 90% on unexpected-contents. davinci-002 5%, davinci-003 and GPT-3.5-turbo 20% | Kosinski 2023/24 (a18, b13, c05) | contested |
| True-belief controls | davinci-003 fell from 90% to 20% once true-belief controls were added; 3 controls per task, 40 tasks | Kosinski (c24, K11) | single |
| Trivial alterations (GPT-3.5) | Original chocolate 99%. Transparent bag 95% chocolate; cannot read 98%; trusted friend 97%; wrote label herself 87%. Unexpected transfer: transparent 94%/90% wrong, in-to-on 97%/74%, trusted call 97%/94% | Ullman 2023 (a19, b10, c01) | single |
| Stress tests of social reasoning | ToMi: GPT-3.5 81% overall, 46% on false-belief. FauxPas-EAI GPT-4 27%, below majority baseline. SocialIQa GPT-4 79% total, 61% "others". TriangleCOPA 96%. GPT-4 97% original false belief, 0% on transparent access and in-to-on. Other person 93.8% to 68.8% | Shapira 2023 (a21, b12, c03) | single |
| Probe method shifts score | 7 points for GPT-4 on SocialIQa between multiple choice and CoT | Shapira (a21) | single |
| Humans versus LLMs | GPT-4 above humans on irony (P=.040), below on faux pas (P=5.42e-5); hinting also reported P=.040 (shared; likely a reporting oddity). About 48-51 humans per test, 1,907 total. LLaMA2-70B above on faux pas (P=.002) via an ignorance bias. All LLMs flagged the offence 100% vs 83.6% of humans | Strachan 2024 (a23, a24, b14) | contested |
| Faux pas is task demand | Likelihood rewording: 3 variants per item, 15 repeats per item per ChatGPT model, separate sessions. GPT-4 at or above human level | Strachan (b15) | single |
| Illusory competence (FANToM) | Strictest score: humans 87.5; GPT-4 + CoT 26.6 (June) or 14.8 (October); ChatGPT 3.7; Llama-2-Chat 0.4; Mistral 0.1; fine-tuned Flan-T5 XL 53.7. Answerability list: humans 90.6, GPT-4 40.2 | Kim 2023 (b23, c17) | single |
| Explicit vs applied ToM (SimpleToM) | Mental state / prediction / judgment: GPT-4o 95.6/49.5/15.3; Claude-3.5-Sonnet 97.9/67.0/24.9; o1 98.6/58.8/32.5; o3-mini 85.4/66.8/41.3; GPT-5 98.5/64.4/40.0; DeepSeek-R1 97.3/73.8/65.8; o1-preview 95.6/84.1/59.5. 1,147 items per category, CI about +/-2.5 | Gu 2024/2026 (b21, d06) | single |
| SimpleToM interventions | Judgment none/reminder/system prompt/CoT: GPT-4o 15.3/42.2/14.9/39.2; Llama-3.1-405B 10.0/25.8/9.9/35.2; Claude-3.5-Sonnet 24.9/84.1/27.1/39.4 | Gu (b22, d07) | single |
| Higher-order ToM | N=112 per model/order. GPT-4: order 3 94.6, 4 73.2, 6 92.9. Humans: 92.9, 82.1, 98.2 (order 5) | Street 2024 (c15) | single; no perturbation test |
| Probability effects (Embers) | GPT-4 cipher 51% vs 13%; reverse sequence 97% vs 53%; Pig Latin 42% vs 23%; rot-13 21% vs 11%; shifts 1, 3, 13 over 50%, other shifts under 3% | McCoy 2023 (a26, b19) | established |
| Counterfactual tasks | 11 task pairs. GPT-3.5 drawing programs parseable 99% default vs 62/71/75% for flipped, 90 and 180 degrees. 0-16 shots shrink but do not remove the base-9 gap. 0-shot CoT helps most, hurts PaLM-2 base-10/16 and chord tuning | Wu 2024 (b20, c09, c10, c17) | established |
| Fresh GSM problems | GSM1k drops up to 8%; Spearman r2=0.36 with likelihood of generating GSM8k items (paper says Pearson r2=0.26; outliers lower it). Phi and Mistral overfit most releases; GPT, Claude, Gemini little | Zhang 2024 (c11) | established |
| GSM-Symbolic / NoOp | NoOp drops up to 65% (worst case, Phi-3-mini); o1-preview -17.5, o1-mini -29.1, Mistral-7b-v0.1 -28.3, Gemma2-2b-it -31.8 | Mirzadeh 2025 (c12) | established |
| Guided-completion contamination check | 10 instances per split, T=0, 500 tokens. 28 settings. GPT-4-judge variant 14/14 (GPT-4) and 13/14 (GPT-3.5) vs human experts; ROUGE-L 13/14 vs 7/14; BLEURT 11/14 and 9/14; baseline 0/14 | Golchin 2024 (c20, d09) | established |
| Order-test contamination check | 1.4B canary, 1,000-item sets: detects from about 4 copies; MNLI p=1.96e-11 at 10 copies; 1 copy not detected (BoolQ p=.156, HellaSwag p=.478). Audit of Llama2-7B, Mistral-7B, Pythia-1.4B, GPT-2 XL: little, except ARC for Mistral (p=.001, borderline after correction) and MMLU | Oren 2023/24 (c21, d10) | established |
| Paraphrase hides contamination | Llama-2-13B trained on rephrased MMLU reaches 85.9, undetectable by n-gram overlap; GPT-4 report: 25% of HumanEval; Llama-2 report: over 10% of MMLU | Yang 2023 (d11) | established |
| Performance-based detection | ConStat needs reference models; BH at 5% FDR; Phi models GSM8k effect over 15% (p<.01%), attributed by authors to training style; about 300 USD OpenAI + 263 USD Together for the whole study | Dekoninck 2024 (d12) | single |
| Format sensitivity | Up to 76 accuracy points (LLaMA-2-13B); GPT-3.5 up to 56, median 6.4, 320 formats, 53 tasks, under 10 USD per task | Sclar 2024 (d13) | established |
| Ranking instability | 6.5M instances, 20 LLMs, 39 tasks; Kendall W about .27-.54 on many LMentry tasks, .63-.78 on several BBH tasks | Mizrahi 2024 (d14) | established |
| Forced self-review hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 (one round), 41.8 (two). GPT-3.5 GSM8K 75.9/75.1/74.7. GPT-4 GSM8K 95.5/91.5/89.0. GPT-4 CSQA 82.0/79.5/80.0. Oracle-label GPT-3.5 GSM8K 75.9 to 95.5 | Huang 2024 (d05) | single here; matches F11, F12 |
| CoT unfaithful to bias | Accuracy drops up to 36% on 13 BBH tasks, GPT-3.5 and Claude 1.0 | Turpin 2023 (c13) | established |
| Early baseline | GPT-3 about 55% SocialIQa, 60% ToMi; 10 to 35 shots gave about 1 point | Sap 2022 (b17, c14) | superseded |
| BigToM | 5,000 items + 25 controls; humans on backward belief 82% true, 72% false; most models far below chance; GPT-4 holds best | Gandhi 2023 (c16, d15) | single |
| HANS | Models near-perfect on entailment, near-zero on non-entailment; HANS-like training hurt DA (66.0 vs 72.4) and SPINN (63.9 vs 67.0), not BERT or ESIM | McCoy 2019 (c18) | single |

## 4. Mechanisms and models

Each item is a procedure an engineer can build. "Needs log probs" means it does not run on chat APIs.

### 4.1 Cue-ablated twin (Pfungst)

Goal: show a pass depends on the logic, not a surface cue.

1. Take a solved item. Write down the suspected cue channel (a keyword, a name, a number pattern, the position of the right answer, the label wording).
2. Build a twin that removes or reverses the cue and keeps the logic. Ullman: transparent bag, "cannot read", trusted friend (a19).
3. Run both. A genuine solver keeps the answer (or changes it correctly if the logic changes). A cue follower gives the same answer as before.
4. Count a pass only if the original and all twins are correct.

Cost: n_twins + 1 model calls per item. Generate twins in code where possible (templates, number and name swaps) so the model under test does not author its own test (c23).

### 4.2 Positive control (opposite-answer twin)

For each item, include a twin whose correct answer is the opposite (Kosinski's 3 true-belief controls per task, c24, b13). A model that always says "the protagonist is wrong" fails it. Pass requires both. Effect measured: davinci-003 fell from 90% to 20% (K11). It rules out one strategy, not label-word association (c24 limits).

### 4.3 Default minus counterfactual gap (Wu)

Same procedure, two rule sets: common and rare (base-10 vs base-9 addition, standard vs altered indexing) (c09). Report gap = default accuracy minus counterfactual accuracy. Run a counterfactual comprehension check so misunderstanding is not scored as inability (c09 limits). Counterfactual performance tracks how common the world is and correlates with default performance (c10). A scaffold counts as helping only if it shrinks the gap at equal tokens.

### 4.4 Three-level consistency (FANToM, SimpleToM)

Ask the same fact at several levels: state (who knows what), prediction (what they will do), judgment (was it reasonable). Score an item passed only if all agree (K10, K20). Strong models hit 95%+ on state and fall far lower on judgment (d06). FANToM asks the same fact in several forms and demands all right: GPT-4 26.6 vs humans 87.5.

### 4.5 Perturbation battery

Meaning-preserving changes (names, numbers, clause order, an irrelevant but plausible clause as in GSM-NoOp, prompt format) with the logic fixed. Mirzadeh's templates: names alone move little; numbers move more; both move more; a no-op clause moves up to 65% (c12). Report mean and worst case over at least about ten variants (K21). Sclar's FormatSpread explores formats within a budget and works on API models (d13).

### 4.6 Guided-completion contamination probe (works on chat APIs)

Golchin and Surdeanu (d09). Per partition, sample 10 instances. Prompt with dataset name, partition and the first segment of the item. Ask for the rest. Run a generic prompt (no dataset name) as the control. A judge call (GPT-4, few-shot) decides whether the guided completion matches the real continuation more often than the generic one. Flag if enough instances match. Temperature 0, 500-token cap. It matched human experts on 14/14 (GPT-4) and 13/14 (GPT-3.5) partitions. Limits: needs the model to reproduce memorised text; instruction tuning can hide it. Truth labels came from deliberately contaminated partitions and from human judgment of the same completions, so real-world power is unmeasured. Snapshots are from June 2023.

### 4.7 Exchangeability order test (needs log probs)

Oren et al. (c21, d10). If a benchmark is exchangeable and the model is clean, every ordering has equal probability. Compute the log probability of the whole set in canonical order and in shuffled orders (65 files in under 24 hours at 7B with 50 shards x 250 permutations). If canonical is far likelier, flag it. Gives a provable false-positive rate. Misses single exposures; detects from about 4 duplicates. Not usable on closed chat APIs.

### 4.8 Performance-based contamination check (ConStat)

Define contamination as performance on the original that does not carry to rephrased samples, synthetic samples or a related benchmark. Compare against a reference model of similar skill. Works on score-only access; needs reference models (d12). A rephrase gap can come from training style (Phi models), not leakage (K22).

### 4.9 Ghost control (Heyes)

Replay the cue alone, without the agent. In an LLM setting: keep the surface text that would trigger the pattern, delete the content that carries the logic (the label without the situation). If the answer stays, the cue is doing the work (a06).

### 4.10 Rival-plus-probe operator (the untested proposal)

A forced step: (1) state the cheap-mechanism rival and the rich-mechanism rival for the answer; (2) name a probe on which they predict differently; (3) run the probe in code; (4) keep the answer if the probe does not discriminate (keep-answer exit). Motivation: K16 (neither pole is a default). Warning: the nearest tested operator, a forced generic self-review, lowered accuracy (d05), and the schema already refuses a full competing-hypotheses matrix and debate (SCHEMA 4b, G9). So this must prove itself at equal tokens (K19) and must report right-to-wrong and wrong-to-right flips separately.

### 4.11 Reporting rule

Report original-pass versus all-twin-pass, worst case across variants, subset scores beside totals, and the default minus counterfactual gap. Alarm when the critical subset is far below the overall score (ToMi 81% overall vs 46% on false belief; K07).

## 5. What holds up

### 5.1 In animals and humans (method templates)

- Held: Pfungst's cue ablation (d01); the rule that experimenters must not cue (b09).
- Mixed: ape false-belief anticipatory looking. The inanimate control gave 51% vs 73% looking and first looks at 14/22 to target (p=.28): weaker, not null. The authors say no evidence of low-level cueing; Heyes's account is neither confirmed nor refuted (b03, critique).
- Failed in humans: infant anticipatory-looking false-belief. Two-lab preregistered replication: 49/90 anticipated at familiarisation, 22/49 at test, p=.568 (b05). The paradigm does not elicit action prediction reliably at age 2. Three further preregistered experiments: first saccades at chance, Bayes factors near 1, so neither account wins (b06).
- Failed: automatic mentalizing in the dot-perspective task, in cloak and goggles tests (b07).
- Held: dogs follow pointing even with a blind, enhancing or decreasing owner (b08). Limit: owners sat behind dogs and were told not to cue, so undetected cues cannot be fully excluded.
- Survey: replication is rare and 39.7% plus 38.8% of respondents admit hoping for results (a14). That is an incentive for over- and under-reading.

### 5.2 Moderators and boundary conditions

- Task demands. A failure in one format does not prove absence of ability. Apes passed once the measure was eye movement, the design was adapted from infant work and scenes held attention (b04, the authors' own account). In LLMs, forced choice by log probability beats free production, most for small models, in four domains (size-by-method interaction: analogical reasoning z=2.631 p=.009; grammaticality z=1.995 p=.046; word prediction t=7.654 p=.005; reflective reasoning not significant) (d08). Chain of thought was not tested there.
- Probe wording. Likelihood wording lifted GPT-4 on faux pas (b15). Multiple-choice vs CoT probing moved GPT-4 by 7 points on SocialIQa (a21).
- Frequency. LLM accuracy tracks the probability of the task, input and output (Embers, a26) and the commonness of the counterfactual world (Wu, c10).
- Model family. GSM1k drops hit Phi and Mistral families and barely hit GPT, Claude, Gemini (c11). The authors cannot tell whether that is better generalisation or cleaner decontamination.
- Spatial reversal. In Wu's spatial task, GPT-4 is best on default but has the largest counterfactual drop; PaLM-2 is worse on default but most robust (c10).
- Strict canon use can bias toward under-attributing (a13, b01). Strict avoidance of mental terms also failed in practice (Hebb, a11).

### 5.3 Meta-level: no meta-analysis found

None of the papers read is a meta-analysis (c23). The LLM perturbation literature is a set of independent papers using one recipe: keep the logic, change surface features, compare. Ullman changes perceptual access; Wu changes world rules; Mirzadeh changes numbers and adds a no-op clause; Kim asks many questions about one fact.

### 5.4 Interventions that worked

- Differential cue ablation (Pfungst), positive controls (Kosinski), logic-preserving twins (Ullman), consistency across question forms (Kim).
- Lowering task demand revealed hidden competence (Strachan b15, Hu and Frank d08).
- Guided-completion contamination probe on chat APIs (d09).
- A mental-state reminder raised behaviour prediction above 80% for three models, and Claude-3.5-Sonnet judgment from 24.9 to 84.1 (d07). Others far less: GPT-4o 42.2, Llama-3.1-405B 25.8.
- Demonstrations narrowed the base-9 addition gap (0 to 16 shots) without closing it (c09).

### 5.5 Interventions that did not work

- Chain of thought left SimpleToM behaviour judgment under 40% for most models (b22; GPT-4o 39.2, Llama-3.1-405B 35.2, Claude 39.4 under CoT). It hurt PaLM-2 base-10/16 addition and chord tuning (c09, c17). Turpin: CoT never mentions biasing features; accuracy drops up to 36% (c13).
- 10 to 35 few-shot examples gave about 1 point on SocialIQa (Sap, b17).
- Forced generic self-review without outside feedback: GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 after two rounds (d05). Oracle labels made it look strong (GPT-3.5 GSM8K 75.9 to 95.5), which is the flaw in earlier reports. GPT-3.5 kept its GSM8K answer 74.7% of the time.
- Adding HANS-like training data hurt DA and SPINN on MNLI (c18).
- Reasoning models narrow but do not remove the applied-ToM gap (d06).

### 5.6 Source reliability flags

- Strachan: the text gives P=.040 for both irony and hinting with identical Z=0.00 and r=0.32; likely a reporting oddity (critique).
- Zhang: the text says Pearson r2=0.26 and that outliers lower the figure; 0.36 is Spearman.
- Mirzadeh: 65% is the worst case, not typical.
- Hu, Sosa and Ullman (a28), Hagendorff, Ma et al., Niven and Kao: abstracts only.
- Krupenye 2016 (22/30) and Hare 2001 counts: abstracts only; second-hand via Kano.
- Heyes 2012, Shettleworth 2010: listings, abstracts, or Mercado's description (b24, b25, b27).
- Wikipedia is not Pfungst; the Pfungst text (d01) was opened separately.

## 6. Language models

### 6.1 The Kosinski-Ullman-Shapira line

| Step | Result |
|---|---|
| Kosinski 2023/24: 11 LLMs, 40 hand-made tasks, each with a false-belief scenario, 3 true-belief controls, reversed versions; pass needs all 8 prompts right | davinci-002 5%, davinci-003 and GPT-3.5-turbo 20%, GPT-4 75% (CI 66-84%), level with six-year-olds. Older models 0% |
| Same author's control history | davinci-003 fell from 90% to 20% once true-belief controls were added |
| Ullman 2023 (GPT-3.5, token probabilities) | Small logic-preserving changes kept the old answer: 95-98% for the wrong belief on transparent/cannot-read/trusted-friend; unexpected transfer 94%/90%, 97%/74%, 97%/94% wrong |
| Shapira 2023, 15 LLMs, 6 benchmarks + Adv-CSFB | GPT-4 97% on original, 0% on transparent access and in-to-on. davinci-002 on those variants: 66.7% and 71.4%. So newer models did worse on adversarial variants, which the authors tie to instruction tuning (every detail is assumed to matter) and reporting bias. Hypotheses, not tested by ablation |
| Strachan 2024: GPT-4 vs 1,907 humans, novel items, 15 repeats per item per model | GPT-4 matched or beat humans on most; the faux pas failure was hyperconservatism, relieved by likelihood wording; LLaMA2's faux-pas "strength" was an ignorance bias |
| Gandhi 2023 BigToM: 5,000 items, 25 controls | GPT-4 mirrors human inference patterns, less reliably; backward belief inference often far below chance for other models |
| Street 2024: higher-order ToM, hand-written, N=112 per model/order | GPT-4 near adult level; no perturbation test |

Reading: headline passes depend on test design. Controls and variants cut them. A wording change can restore them. Which one is "the real ability" is not settled (Hu, Sosa, Ullman: three definitions of "has ToM").

Ullman's normative claim (c02): outlier failures outweigh average success (100 correct simple products then failure on 213*261 means no general algorithm). That is a stance, not a result.

Ullman also warns that once a perturbation set is public, a model can train on it (b11, K18). Even a full pass would leave doubt, since people infer mental states from process, not only behaviour.

### 6.2 Surface statistics and counterfactuals

- Embers: GPT-4 cipher 51% (high-probability output) vs 13% (low); reverse sequence 97% vs 53%; Pig Latin 42% vs 23%; rot-13 21% vs 11%. Accuracy tracks task, input and output probability, even in deterministic tasks (b19).
- Wu: all four model families drop on counterfactual versions; the drop correlates with commonness; partial memorisation, not zero reasoning (c09, c10).
- Mirzadeh: no-op clause up to 65% drop; o1-preview -17.5, o1-mini -29.1. This includes o1, so it is one of the few perturbation results on a reasoning model.
- Turpin: biasing features change answers while CoT never mentions them (c13).

### 6.3 Is it contamination?

- GSM1k: drops up to 8% with Spearman r2=0.36 against likelihood of generating GSM8k items (c11). Open families Phi and Mistral overfit most; frontier models show little. The modest r2 and the authors' own doubt make this a hint, not proof.
- Yang: rephrased MMLU training gives 85.9 for a 13B model, undetectable by n-gram overlap. GPT-4 report: 25% of HumanEval; Llama-2 report: over 10% of MMLU (d11). So paraphrase is both the best way to hide contamination and the most sensitive check.
- Oren audit of four public 1.4B-7B models: mostly clean, except ARC for Mistral (p=.001, borderline).
- Golchin: GPT-4 found contaminated with AG News, WNLI and XSum.
- ConStat found sample-specific contamination in four instances in reference models at p<0.5% (d12).
- "Gap equals contamination" fails when the gap comes from training style (Phi, GSM8k effect over 15%; d12).

### 6.4 Format and wording

- LLaMA-2-13B swings up to 76 points across formats; GPT-3.5 up to 56 with median 6.4 (d13).
- Rankings change across paraphrases (Kendall W about .27 to .78) (d14).
- No source gives a stopping number of rephrasings (critique gap 5).

### 6.5 2025-26 models

Only SimpleToM (d06) covers reasoning models on ToM. The applied-ToM gap remains for o1 (32.5 judgment), GPT-5 (40.0), o3-mini (41.3), o1-preview (59.5) and DeepSeek-R1 (65.8), against 85-99% mental-state accuracy. It is not the Ullman or FANToM twin design. Ullman-style and FANToM-style twins on reasoning models were not found (d16, search failed). Preregistered re-runs of LLM ToM passes by other groups were not found either (gap 6).

### 6.6 Scaffolds and self-checks

- CoT is uneven (see 5.5). A reminder helps one model a lot (Claude-3.5-Sonnet 24.9 to 84.1) and others little. The reminder names the relevant fact, a hint an agent will not always have (d07 limits).
- Forced review hurts without outside feedback (d05).
- Nothing found tests a named-rival-plus-probe operator, or a simplest-explanation rubric's false-negative rate (d17).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Define a "cheap rival" for every pass: a surface cue, a memorised item, a format effect. A pass is not accepted until the cheap rival is tested or ruled out. Method, not preference: do not add "prefer the simplest explanation" as a rule | G3 (wording) | [E] | K01, K16, a05, a10, a11, a13, b01 |
| A2 | Cue-ablated or mutated twin: remove the suspected cue, keep the logic; the pass must survive. Generate twins in code (names, numbers, order, format) so the tested model does not write them | G3; S4, S8 | [E] | K02, K08, d01, c09, c12, c23 |
| A3 | Report subset scores beside totals; alarm when the critical subset is far below the overall | G3 | [E] | K07, a21 |
| A4 | Lower task demand before concluding a capability is missing: forced choice or likelihood wording, then re-read | G3; S4 | [E] (b15, b18, d08) | K12 |
| A5 | Report mean and worst case over about ten paraphrases or formats; never one wording | G3, G7 | [E] | K21, d13, d14 |
| A6 | Default-minus-counterfactual gap on our bench items: the scaffold counts as helping only if it shrinks the gap at equal tokens | G7, G3 | [E] | K08, b19, b20, c11, c12 |
| A7 | Contamination hygiene: run the guided-completion probe (about 10 prompts plus a judge call per partition) on visible benchmark items on chat APIs; paraphrase as the first cue ablation; use the order test only where prompt log probs exist; compare gaps against a same-skill reference before calling a gap contamination | G3 | [E] | K14, K22, d09, d10, d11, d12 |
| A8 | No forced generic re-check. Any re-check needs a keep-answer exit and outside feedback (already barred by SCHEMA 4b and G2) | G2, G10 | [E] across F11, F12 | K19, d05 |
| A9 | Do not treat CoT or a reminder as a general cure for perturbation gaps | G7, G10 | [E] | K09, b22, c13 |

Where these land. G3 already says a pass must be on something not fitted to. A1-A7 refine its implementation, not its content. A8 and A9 confirm 4b and G10.

### Test first (not established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Rival-plus-probe operator at S8: one cheap rival, one rich rival, a discriminating probe run in code, keep-answer exit | G3 / new verify operator | [S]; no direct test | K16, K17, K19, d05, d17 |
| T2 | Opposite-answer control per item, pass requires both | G3, S8 | [S] | K11, c24, b13 |
| T3 | Three-level consistency (state, prediction, judgment) as the pass rule | G3, S8 | [S] | K10, K20, b23, d06 |
| T4 | Mental-state reminder as a conditional operator | O (conditional) | [C]; model dependent | K09, d07 |
| T5 | Private mutation generator held back; compare public vs fresh mutations | G3 | [S] | K18, b11 |
| T6 | Repeat-pass rule (N independent runs and rephrasings) before counting a pass | G3, G4 | [S] | K05, K21 |
| T7 | Rubric demanding the "simplest sufficient explanation": check for under-claiming | S9 | [S]; none found | a13, b01 |
| T8 | Cue-ablation ranking per token: paraphrase vs name vs number vs format swap | G3, G7 | [S] | K22 |
| T9 | Lowered-demand rerun interaction with CoT | S4 | [C] | K12, d08 |

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup and probe calls counted). Report right-to-wrong and wrong-to-right flips separately. Fix seeds; at least three.

1. Rival-plus-probe vs plain CoT vs CoT plus generic recheck.
   - Items: reasoning items with a known cheap-cue trap (ARC-like pattern fits, brain-teaser lookalikes) plus a clean set.
   - Arms: plain CoT; CoT + generic recheck; CoT + cheap rival + rich rival + code-run probe + keep-answer exit.
   - Metric: accuracy on trap items, accuracy on clean items, flips each way.
   - Expected: no loss on clean items (keep exit); gain on trap items; generic recheck loses (d05).
2. Twin pass rate.
   - Items: 5 mutated twins per item (names, numbers, order, format, one logic-preserving change in access).
   - Arms: plain; current scaffold.
   - Metric: pass-on-original minus pass-on-all-twins.
   - Expected: scaffold shrinks the gap. Ullman-scale collapses (near 100% to near 0%) are unlikely on current models, so tune twin difficulty first.
3. Default vs counterfactual.
   - Items: pairs with common and rare rules, with a comprehension check.
   - Arms: plain; scaffold.
   - Metric: default minus counterfactual accuracy.
   - Expected: scaffold gap smaller than plain; if not, the scaffold adds nothing here.
4. Paraphrase spread.
   - Items: 10 paraphrases per item.
   - Arms: single wording vs mean and worst of ten.
   - Metric: spread (max minus min), rank flips between arms.
   - Expected: median spread near single digits, much larger tail (GPT-3.5 median 6.4, max 56).
5. Guided-completion probe on our public bench items.
   - Items: 10 per partition.
   - Arms: guided vs generic prompt.
   - Metric: match-rate difference, scored by a judge call.
   - Expected: separates visible-and-contaminated sets; power on real unlabeled models is unmeasured.
6. Three-level consistency.
   - Items: stories with hidden information, scored at state, prediction and judgment.
   - Arms: single-form pass vs all-three-agree pass; plain vs reminder.
   - Metric: pass rate each way.
   - Expected: the all-agree pass rate sits far below single-form (SimpleToM 85-99% vs 32-66%).
7. Lowered-demand rerun.
   - Items: our failed items.
   - Arms: original format vs forced choice or likelihood, with and without CoT.
   - Metric: recovery rate.
   - Expected: recovery on a nontrivial share; the CoT interaction is unknown.
8. Cue-ablation ranking.
   - Items: same items; one ablation type per arm (paraphrase, name, number, format).
   - Metric: gap per ablation per extra token.
   - Expected: paraphrase largest on contaminated sets (d11).
9. Under-claiming check.
   - Items: tasks where the rich reading is correct, with independent proof of capability.
   - Arms: plain vs simplest-sufficient-explanation rubric.
   - Metric: false-negative rate.
   - Expected: higher with the rubric (Mercado's worry). Test it.

## 9. What does not transfer, and why

- The preference for "lower". In animals "lower" is an evolutionary or neural ordering with no agreed scale (a10, b01). For an LLM there is no scale; "cheap" means "predicted by surface statistics". Use the method (A1), not the ordering.
- Phylogeny and ecology arguments (Adaptive Triadic Model, a10) have no LLM analogue.
- Anthropomorphism fear. Heyes shows both poles are errors (K16). In an agent loop the hazard is accepting a pass without a control.
- Pfungst's single-horse result. One animal, tests not animals (d01). The method transfers, the number does not.
- Replication norms in animal work (a self-selected survey, 21.6% response; a14) do not give LLM base rates.
- Human ToM neural and developmental claims. SimpleToM, Kosinski and others measure text behaviour; they cannot answer whether an LLM "has" ToM (Hu, Sosa and Ullman, c07).
- Specific numbers for 2023 models (GPT-3.5 and early GPT-4 snapshots, Sap's GPT-3 at 55%) may not hold for current models. Treat them as shapes, not predictions.
- Ullman's "outliers outweigh averages" is a stance about ToM claims; our agent needs reliability measured on its own bench.
- Published test sets can be trained on, perturbation sets included (K18).

## 10. Open questions

1. Does a forced "cheap rival plus discriminating probe" operator improve accuracy or reduce contamination damage at equal tokens vs plain CoT? No test found (K16, K17, K19).
2. How do 2025-26 reasoning models score on Ullman-style and FANToM-style twins? Only SimpleToM covers them (d06).
3. What is the default-minus-counterfactual gap on our tasks, and does our scaffold shrink it?
4. Which cue ablation catches the most contamination per token: paraphrase, name, number or format swap? Paraphrase hides best; ranking untested (d11).
5. How many reruns or rephrasings make a pass trustworthy? Format sensitivity is large; no stopping number (d13, d14).
6. Do published LLM ToM passes shrink under preregistered re-runs by other groups, as the Kano and Kampis replications did? Not found; search failed.
7. Power of guided completion and the order test on API-only and current models (tested on June 2023 snapshots and models up to 7B).
8. Does lowering task demand help across more than four domains, and how does it interact with CoT? (d08)
9. Do Krupenye 2016 and Hare 2001 original counts match the secondary reports? (abstracts only)
10. Does a "simplest sufficient explanation" rubric cause under-claiming (false negatives) in an agent? No evidence.
11. Is the Strachan P=.040 for both irony and hinting a true tie or a copy error?
12. Is the GSM1k drop contamination or style? The authors cannot tell without training data (c11).

## 11. Sources

[V] = opened and read this session. [M] = snippet, abstract, listing or second-hand only.

### Comparative cognition and philosophy

- [V] Wikipedia, Morgan's Canon (1894/1903 wording; de Waal 2002 rider): https://en.wikipedia.org/wiki/Morgan%27s_Canon
- [V] Wikipedia, C. Lloyd Morgan: https://en.wikipedia.org/wiki/C._Lloyd_Morgan
- [V] Wikipedia, Clever Hans: https://en.wikipedia.org/wiki/Clever_Hans
- [V] Pfungst (1911) Clever Hans, Project Gutenberg text: https://www.gutenberg.org/cache/epub/33936/pg33936.txt
- [V] Heyes (2012) Simple minds: https://pmc.ncbi.nlm.nih.gov/articles/PMC3427553/
- [V] Penn and Povinelli (2007): https://pmc.ncbi.nlm.nih.gov/articles/PMC2346530/ (first 100k of 124k characters)
- [V] Mikhalevich, Powell and Logan (2017): https://pmc.ncbi.nlm.nih.gov/articles/PMC5413892/ (first 100k of 165k)
- [V] Bruni, Perconti and Plebe (2018): https://pmc.ncbi.nlm.nih.gov/articles/PMC6249301/
- [V] Mercado (2016) commentary on Starzak: https://pmc.ncbi.nlm.nih.gov/articles/PMC4812110/
- [V] Farrar, Ostojic and Clayton (2021): https://pmc.ncbi.nlm.nih.gov/articles/PMC8407565/
- [V] Kano et al. (2017) inanimate control: https://pmc.ncbi.nlm.nih.gov/articles/PMC5595417/
- [V, opening only] Kano et al. (2017) eye tracking methods account: https://pmc.ncbi.nlm.nih.gov/articles/PMC5398232/
- [V] Kampis et al. (2021) two-lab replication: https://pmc.ncbi.nlm.nih.gov/articles/PMC8386515/
- [V] Kulke and Rakoczy (2019): https://pmc.ncbi.nlm.nih.gov/articles/PMC6433471/
- [V] Conway et al. (2017) cloak and goggles: https://pmc.ncbi.nlm.nih.gov/articles/PMC5327864/ (sample sizes not extracted)
- [V] Schmidjell et al. (2012): https://pmc.ncbi.nlm.nih.gov/articles/PMC3530188/
- [V] Samhita and Gross (2013): https://pmc.ncbi.nlm.nih.gov/articles/PMC3921203/
- [V] Frontiers in Parasitology 2026, Xenos vesparum: https://pmc.ncbi.nlm.nih.gov/articles/PMC13582532/
- [M] Voudouris et al. (2025): https://doi.org/10.1037/com0000404
- [M] Auersperg (2025): https://doi.org/10.1037/com0000435
- [M] Heyes (2012) listing: https://doi.org/10.1098/rstb.2012.0217
- [M] Heyes (2014) submentalizing: https://doi.org/10.1177/1745691613518076
- [M] Shettleworth (2010): https://doi.org/10.1016/j.tics.2010.07.002
- [M] Sober, Fitzpatrick, Starzak via Heyes, Wikipedia and Bruni (no URL; second-hand)
- [M] Krupenye et al. (2016) abstract: https://doi.org/10.1126/science.aaf8110
- [M] Hare, Call, Tomasello (2001) abstract: https://doi.org/10.1006/anbe.2000.1518

### LLM and AI

- [V] Kosinski (2023/2024): https://arxiv.org/abs/2302.02083 and https://www.pnas.org/doi/10.1073/pnas.2405460121
- [V] Ullman (2023): https://arxiv.org/abs/2302.08399
- [V] Shapira et al. (2023): https://arxiv.org/abs/2305.14763
- [V] Strachan et al. (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11272575/
- [V] Pang et al. (2025) letter: https://pmc.ncbi.nlm.nih.gov/articles/PMC12280963/
- [V] Sap et al. (2022): https://arxiv.org/abs/2210.13312
- [V] Hu and Frank (2024): https://arxiv.org/abs/2404.02418
- [V] McCoy et al. (2023) Embers: https://arxiv.org/abs/2309.13638 (a26 abstract; b19 opened)
- [V] Wu et al. (2024) Reasoning or Reciting: https://arxiv.org/abs/2307.02477
- [V] Gu et al. SimpleToM: https://arxiv.org/abs/2410.13648
- [V] Kim et al. (2023) FANToM: https://arxiv.org/abs/2310.15421
- [V] Zhang et al. (2024) GSM1k: https://arxiv.org/abs/2405.00332
- [V] Mirzadeh et al. (2025) GSM-Symbolic: https://arxiv.org/abs/2410.05229
- [V] Turpin et al. (2023): https://arxiv.org/abs/2305.04388
- [V] Street et al. (2024): https://arxiv.org/abs/2405.18870
- [V] Gandhi et al. (2023) BigToM: https://arxiv.org/abs/2306.15448
- [V] McCoy, Pavlick, Linzen (2019) HANS: https://arxiv.org/abs/1902.01007
- [V] Binz and Schulz (2023): https://arxiv.org/abs/2206.14576
- [V] Golchin and Surdeanu (2024): https://arxiv.org/abs/2308.08493
- [V] Oren et al. (2024): https://arxiv.org/abs/2310.17623
- [V] Yang et al. (2023): https://arxiv.org/abs/2311.04850
- [V] Dekoninck et al. (2024) ConStat: https://arxiv.org/abs/2405.16281
- [V] Sclar et al. (2024): https://arxiv.org/abs/2310.11324
- [V] Mizrahi et al. (2024): https://arxiv.org/abs/2401.00595
- [V] Huang et al. (2024) self-correction: https://arxiv.org/abs/2310.01798
- [V] Hu, Sosa and Ullman (2025): https://arxiv.org/abs/2502.21098 (c07 opened; a28 abstract only)
- [V, intro only] Systematic review of LLM ToM evaluation: https://arxiv.org/abs/2502.08796
- [M] Niven and Kao (2019): https://arxiv.org/abs/1907.07355
- [M] Ma et al. (2023): https://arxiv.org/abs/2310.19619
- [M] Hagendorff et al. (2023): https://arxiv.org/abs/2303.13988
