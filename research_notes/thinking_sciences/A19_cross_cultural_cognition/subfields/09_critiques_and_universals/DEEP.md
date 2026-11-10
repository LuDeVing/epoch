# Critiques and universals: deep document

*Subfield A19.09. Evidence files: evidence_a-d.jsonl. Claims: claims.jsonl (K01-K27). Cross-check: critique.md. Ids such as a14 or d02 point to evidence lines. Status marks: [E] established (2+ independent sources), [S] single source, [C] contested. Many lines rest on abstracts only; section 11 marks which.*

## 1. What it is

This subfield asks one question: how much of what we think we know about "how people reason" is true of all people, and how much is true only of the people who were tested?

Three strands sit in it.

1. **The sampling critique.** Almost all behavioural science uses Western, Educated, Industrialised, Rich, Democratic (WEIRD) samples. Claims about "the human mind" are then claims about a narrow group (Henrich, Heine, Norenzayan 2010).
2. **The Nisbett line and its critics.** The theory that East Asians reason holistically (context, relations, contradiction tolerated) and Westerners analytically (objects, rules, logic) was founded on small student samples. Later large or preregistered replications often shrink or remove the effects. Critics also point to confounds: language, task instruction, schooling, test familiarity, response bias, and ecology (rice vs wheat) instead of "East vs West".
3. **The universals reading.** Underneath, all groups show the same core competence. Every group in Norenzayan 2002 Study 4 was strongly sensitive to logical validity (F=1161.73). East Asian and Western face viewers use the same information when forced to (Caldara 2010). Cultures differ in habitual style and in what a cue triggers, not in what they can do.

A fourth, new strand applies this to language models. LLMs are trained on WEIRD-heavy text, so their default answers resemble WEIRD people (r = -.70 between a population's cultural distance from the US and similarity to GPT output; Atari 2023). Studies that give LLMs the Nisbett scales and tasks give mixed or reversed results, and are themselves fragile: prompt framing explained eta2 = 0.54 of variance, prompt language 0.0002 (Sun and Wang 2025).

**Why it matters for our agent.** The agent weighs human evidence when it designs its scaffold. This subfield says: tag each human finding with the population tested, weight "universal" and "cultural difference" claims by power and design, do not build a "cultural style" module, and do not trust single-wording prompt comparisons. It maps to guardrail G7 (pay for itself at equal tokens) and the "not to add" list in SCHEMA section 4b (personas).

Neighbouring subfields (linked only, not covered): priming of orientation, dual-process theory, individual-level links, methods and measurement, reproducibility and methods, belief updating, systematic review of SAT evidence.

## 2. History and theories in depth

**1960s-70s: perception and cognitive style.** Segall, Campbell, Herskovits (1966) compared the Mueller-Lyer and other illusions across 16 societies (14 small-scale). US undergraduates needed one line about one fifth longer to see equality. San foragers of the Kalahari showed no detectable effect (a02, b03; read only through Henrich 2010). Witkin and Berry (1975): on Rod and Frame and Embedded Figures, only Westerners and migratory foragers sit at the field-independent end (b02). Luria, Cole, Greenfield and Dasen found reasoning patterns tied to schooling and institutions, not a fixed developmental sequence. Piagetian tasks in West Africa and Papua New Guinea held up poorly beyond early childhood. Snarey (1985, 27 countries) found Kohlberg post-conventional reasoning in all Western urban samples and in no small-scale society (a06). These are old, often contested, and secondary here.

**1999-2002: the Nisbett programme.** Peng and Nisbett (1999): Chinese prefer dialectical proverbs and compromise; Americans prefer formal logic (a10, not opened). Masuda and Nisbett (2001): Japanese describe and recall more background in fish scenes (a09, not opened). Nisbett, Peng, Choi, Norenzayan (2001) is the integrating theory: social worlds (interdependence vs independence) shape thought systems (a07, not opened). Norenzayan, Smith, Kim, Nisbett (2002) tested rule vs family-resemblance categorisation and belief bias (b08-b10, d02):
- Study 2: N=157 (52 European American, 52 Asian American, 53 East Asian). Under a classification instruction all groups chose the rule 67% vs 33% resemblance (culture x response F(2,100)=1.25, ns). Under a similarity instruction: EA 69% rule, East Asian 41%, Asian American 46%.
- Study 3: Koreans were swayed by argument typicality only when typicality was not salient (culture x argument type F(2,253)=4.67, p<.01). The effect vanished when typicality was made salient.
- Study 4: Koreans showed more belief bias on valid arguments (3-way F(1,184)=4.73, p<.05) but also a response bias (Koreans less likely to say "yes", F(1,184)=14.41). Validity sensitivity in both groups F(1,184)=1161.73.

So even the founding paper shows differences only when intuition and logic conflict and only under some instructions. It is a style-trigger result, not a competence gap.

**2008-2010: face scanning and the WEIRD critique.** Blais et al. (2008): East Asians fixate the centre of the face more (14 vs 14 adults) with equal accuracy (F(1,26)=0.59, p=.44). Caldara et al. (2010): with a gaze-contingent spotlight (2, 5, 8 degrees; 30 vs 30), no culture x aperture interaction in accuracy (F(2,54)=0.6, p=.55). Same information used; strategy differs, performance does not (a11, a12). Henrich et al. (2010): 68% of subjects in top journals 2003-2007 from the US, 96% from Western industrialised countries (12% of world population), 73% of first authors at US universities, 67% of US JPSP samples undergraduates; an undergraduate is "over 4,000 times" more likely to be a participant than a random non-Westerner (a01, b01). Westerners are outliers on fairness games (US Dictator offers nearly double Hadza and Tsimane, a24), on the fundamental attribution error (Church et al. 2006, b05) and on field dependence. The authors state that both styles are available to all normal adults and that the aim is to measure similarity and variation (a23). A commentary argued that differences may reflect how participants read the task, not different processes (a05). Another said shared processes can have culture-specific expression (b06).

**2014-2018: ecology and replication.** Talhelm et al. (2014): rice vs wheat regions of China differ on holistic and collectivist measures (about 1,000 subjects; abstract only, b17). Talhelm, Zhang, Oishi (2018): 8,964 people observed in cafes in six cities; wheat-region people sat alone about 10% more on weekdays and 5% more on weekends; chair study n=678 (a13). It avoids the language and nationality confound but is observational. Mercier et al. (2015) failed to replicate Peng and Nisbett contradiction effects with Chinese vs French (b15, d04; abstract). Hakim et al. (2017) found little robust difference in global/local, framed-line and change detection (b14; abstract). Many Labs 2 (Klein 2018): 28 effects, 125 samples, 15,305 participants, 36 countries; median d 0.60 original vs 0.15 replication; 32% opposite direction; 3 of 28 moderated by the WEIRD split (b11, d03).

**2019-2024: reanalysis and quasi-experiment.** Schimmelpfennig et al. (2024) argue Many Labs 2 cannot show universality: mean cultural distance from the US 0.062 (by participant), 91% of sites below 0.15 while the world range reaches about 0.3, power to detect moderation 28% (b12). Authors are interested parties. Talhelm et al. (2024): two state farms 56 km apart with staff assigned by government; rice farmers more holistic on triads (B=0.28, p=.025, r=.15, N=188), more loyal to a friend (r=.18), less self-inflating (r=.18), at about half the East-West gap; two farms, original lab (d01).

**2023-2026: LLMs as subjects.** Jin 2023 gave Nisbett scales to GPT-3.5 and GPT-4. Atari 2023 "Which humans?". Cao 2023, Durmus 2023, Tao 2024, AlKhamissi 2024, Wang 2024 on value and knowledge alignment. Hu 2026 and Sun and Wang 2025 on style. Sabir 2025 on vision-language captions. See section 6.

**Competing positions.**

| Position | Claim | Best evidence |
|---|---|---|
| Strong cultural style | East and West differ in default reasoning style | Norenzayan 2002 (instruction-bound), Talhelm 2024 (r=.15) |
| Universal core | All groups share competence; differences are cue-triggered habit | validity F=1161.73; Caldara 2010; Many Labs 2 (weak: power 28%) |
| Measurement artifact | Differences come from task reading, language, response bias, selection | a05; Ji 2004 (not opened); b10 response bias |
| Ecology, not "East" | Local subsistence, not nation, drives style | Talhelm 2014, 2018, 2024; Mapuche and Sangu sort like Chinese (b02) |
| Western outlier | The West is the unusual end, not the baseline | Henrich 2010 (secondary reviews) |

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Samples are overwhelmingly WEIRD | 68% US, 96% Western industrialised (12% of world); 73% first authors US; 67% of US JPSP samples undergraduates; over 4,000x odds | Henrich 2010 (a01, b01); Rad 2018 abstract (b16) | [E] |
| Internet samples only partly widen this | 564,502 participants: 19% not from advanced economies, 20% non-Western, 66% of US sample outside age 18-22 | commentary in Henrich 2010 (b07) | [S] |
| Mueller-Lyer varies by society | 16 societies; US about 1/5 line difference, San about 0 | Segall 1966 via Henrich (a02) | [S] secondary, old |
| Rule vs resemblance depends on instruction | Classification: all groups 67% rule. Similarity: EA 69%, East Asian 41%, Asian American 46%. N=157 | Norenzayan 2002 (b08, d02) | [E] with Many Labs 2 |
| Instruction effect in replication | N=7,396; d=0.86 (original EA d=0.00, East Asian d=0.67); WEIRD advantage 65.2 vs 59.8% under "belong to", reversed 42.8 vs 48.4% under "similar to" | Many Labs 2 (d02) | [S] one replication |
| Validity sensitivity is shared | F(1,184)=1161.73 vs belief-bias interaction F=4.73 | Norenzayan 2002 Study 4 (b10) | [S] |
| Typicality effect vanishes when salient | Low salience F(2,253)=4.67; Korean t(91)=5.98, EA t(90)=1.16 ns | Norenzayan 2002 Study 3 (b09) | [S] |
| Face scanning differs, accuracy equal | 14+14: F(1,26)=0.59; spotlight 30+30: interaction F(2,54)=0.6, accuracy F(1,54)=2.18, p=.14 | Blais 2008; Caldara 2010 (a11, a12) | [E] |
| Peng-Nisbett contradiction not replicated | Chinese vs French "behaved similarly"; N not obtained | Mercier 2015 (b15, d04) | [C] abstract only |
| Visual holism not robust | "Relatively little" robust difference; N not obtained | Hakim 2017 (b14) | [C] abstract only |
| Many Labs 2 overall | median d 0.60 vs 0.15; 54% significant; 32% reversed; Q significant in 39%; 3/28 WEIRD-moderated | Klein 2018 (b11, d03) | [E] shrinkage; [C] universality |
| ML2 could not detect culture | distance 0.062 vs world to about 0.3; power 28%; under 8% for some effects | Schimmelpfennig 2024 (b12) | [S] interested authors |
| Rice-wheat, observational | 8,964 observed; about +10% alone on weekdays; chair n=678 | Talhelm 2018 (a13) | [C] confounded |
| Rice-wheat, quasi-random | triad B=0.28, p=.025, r=.15 (N=188); loyalty r=.18; self-inflation r=.18; two farms | Talhelm 2024 (d01) | [S] no independent replication |
| LLM scales "holistic" | AHS GPT-3.5 5.35, GPT-4 5.01 vs norm 4.87 (N=702); DSS GPT-4 3.97, p=.344; n=10 runs, temp 1 | Jin 2023 (a14, b18) | [S] weak design |
| LLM style: language d near 0 | 8 models, temp 0: language d=0.045 (eta2 0.0002, p=.15); origin d=0.169 (p=.0089, English prompts); framing d=-2.095 (eta2 0.542) | Sun and Wang 2025 (a15) | [S] |
| LLM style reversal | Categorisation relational score: Chinese prompt 5.30 vs English 6.78 (t=-7.74); image: US model 11.53 vs Chinese 8.10 objects (d=1.01); 100 runs per cell | Hu 2026 (a16, b20) | [S] |
| Verbosity confound | English 10.90 vs Chinese 10.06 objects, d=0.36 | Hu 2026 (b21) | [S] |
| LLMs resemble WEIRD humans | r=-.70 distance vs similarity; triad 1,100 runs, 20 triads, 31 populations; GPT nearest Netherlands, Finland, Sweden, Ireland | Atari 2023 (b25, d06) | [S] preprint, GPT-3.5 era |
| Value alignment by country | GPT-4o nearest Finland d=0.20, Andorra 0.21, Netherlands 0.45; farthest Jordan 4.10, Libya 4.00. GPT-4 nearest New Zealand 0.98, Iceland 0.97, Australia 0.86; Jordan 4.19 (critique.md corrects c01) | Tao 2024 (a17, b26) | [E] with Durmus, Cao |
| Cultural prompting helps | GPT-4o 2.42 to 1.57; GPT-4-turbo 2.71 to 1.77; GPT-4 2.69 to 1.65; improved for 71.0, 81.3, 77.6% of countries; GPT-3 2.39 to 2.11; GPT-3.5 3.35 to 2.83 | Tao 2024 (b26) | [E] |
| Alignment unstable across prompts | Spearman China -0.77 vs +0.54 on another prompt; correct description 1.5 to 2.5, incorrect 1.0 | Cao 2023 (a18, c05) | [S] 5 cultures |
| English-culture default in knowledge | ERNIE 7.6 vs GPT-4 1.8 on Chinese concrete items; GPT-4 most affected | Wang 2024 (c11) | [E] with Naous, Durmus |
| Prompt format variance | median 7.5 points, up to 76 (LLaMA-2-13B); GPT-3.5 up to 56, median 6.4 over 320 formats | Sclar 2024 (d07) | [E] |
| Personas do not lift accuracy | 162 personas, 2,410 MMLU questions, none better than control | Zheng 2024 (d08) | [C] vs Kong |
| Role-play as CoT trigger | AQuA 53.5 to 63.8%; Last Letter 23.8 to 84.2% | Kong 2024 (d09) | [C] weak baseline |
| Question language, math | MGSM 44.9% (4 under-resourced) vs 47.9% (6 high-resource) | Shi 2023 (d10) | [S] |
| VLM captions mostly analytic | COCO 6-shot holistic 19-26%; Japanese data up to 73.37% | Sabir 2025 (b23, d12) | [S] |
| Human content-effect baseline is UK only | 625 plus 360 participants | Lampinen 2024 (d13) | [S] |

## 4. Mechanisms and models

Each is written so an engineer can implement it.

**M1. Population-tagged evidence ledger.** Every human-evidence line carries: population, N per cell, design (observational, quasi-random, preregistered, replication), measure type (self-report, behaviour, accuracy), power note. Rule: one population or fewer than about 60 per cell is [S] at most; [E] needs a replication in a culturally distant sample. A table and a lookup, no model call. Norenzayan 2002 (52 per cell) is the example of "small".

**M2. Cue-dependent style model.** Norenzayan 2002 and Many Labs 2 fit: P(rule choice) = base rate + group offset x conflict(cue). Under a classification cue there is no group offset; under a similarity cue it appears. A measured "style" is a function of the cue. So run each item under at least two cue wordings and report the interaction, not a main effect.

**M3. Competence versus strategy split.** Blais and Caldara: strategy differs, accuracy equal. Norenzayan Study 4: validity sensitivity equal, bias differs. Report two numbers per test: sensitivity (d-prime) and bias (criterion), computed in code. For LLM tests use four belief-bias cells: valid-believable, valid-unbelievable, invalid-believable, invalid-unbelievable.

**M4. Variance decomposition for prompt studies.** Run a factorial design (language, model, framing, item). Compute eta2 per factor. If framing eta2 exceeds culture eta2, the "culture" claim is not about the model. Sclar 2024 gives the noise floor: a median format spread of 7.5 points means a smaller difference on one wording is noise.

**M5. Power-aware universality test.** A null across culturally near sites is weak. Call an effect universal only if (a) sites span the cultural-distance range, (b) power for the expected moderation is above 80%, (c) an equivalence test (TOST) excludes the smallest effect of interest. Many Labs 2 fails (a) and (b): mean distance 0.062, power 28%.

**M6. Continuous cultural distance.** Replace the binary WEIRD flag with a distance score (0 to about 0.3) between sample and reference. Regress effect on distance. Atari 2023 used this idea (r=-.70).

**M7. Confound matrix.** For any comparison list what differs beyond the factor: language, schooling, selection (international students), test familiarity, response style, ecology. Mark each controlled, matched or free. More than two free confounds means downgrade. The usual "Chinese model vs US model" contrast leaves language, tokenizer, RLHF, data density and verbosity free (d11, d14).

**M8. Verbosity-normalised style score.** Divide object counts by output tokens or sentences before comparing (Hu 2026: English 10.90 vs 10.06 objects). Sabir's "first-mentioned item" definition is more robust to length but needs a judge model.

**M9. Same-study human reference.** Jin 2023 compared model runs with norms from other studies (N=702, 158, 382). Atari 2023 used the same task and platform for 31 populations. Compare an agent score with a norm only if the items and format match.

**M10. Context check.** False cultural descriptions lowered alignment (1.0) as correct ones raised it (2.5) (Cao 2023). Models believe injected context, so a scaffold that injects context needs a check from outside the model.

## 5. What holds up

**Held up.**
- WEIRD sampling base rate (Henrich 2010; Rad 2018 abstract). Descriptive, robust. [E]
- Face scanning strategy differs, accuracy does not (Blais 2008, Caldara 2010). [E]
- Instruction dependence of rule vs resemblance: Many Labs 2 replicated the instruction effect (d=0.86, N=7,396). The WEIRD advantage appeared under "belong to" and reversed under "similar to". The preregistered test was of the instruction effect, not East vs West. [S]
- LLM defaults resemble WEIRD and English-speaking populations: Tao, Cao, Durmus, Atari, Wang, Naous agree. [E]
- Cultural prompting shifts stated values (71-81% of countries) but never fully (residual 1.57). [E]
- Prompt-format sensitivity (Sclar; Sun and Wang eta2 0.54) as a methodological hazard. [E]

**Did not hold or shrank.**
- Peng and Nisbett contradiction effects (Mercier 2015, Chinese vs French; abstract only).
- Visual holism tasks (Hakim 2017; abstract only).
- Many Labs 2: median d fell from 0.60 to 0.15; 32% reversed.
- LLM replications: Sun and Wang failed to reproduce Lu et al. (language d=0.045). Hu 2026 found reversals (relational score 5.30 vs 6.78).
- Jin 2023's "ChatGPT is holistic" does not support a claim about reasoning: mixed on value scales (DSS GPT-4 p=.344), 10 runs.

**Contested.**
- Rice-wheat: Talhelm 2014 and 2018 observational; 2024 quasi-random (r=.15, two farms, same lab). A 2018 Chinese-language critique exists (d16, title only). No independent causal replication found.
- Many Labs 2 as proof of universality: power 28%, distance 0.062; critics are interested parties.
- Personas on accuracy: Zheng 2024 none; Kong 2024 gains explained as a CoT trigger.

**Moderators found.** Instruction wording (Norenzayan); salience of typicality (Study 3); aperture (Caldara); ecology (rice/wheat); schooling (Luria and successors); testing language in bilinguals (Ji 2004, not opened); prompt framing (Sun and Wang); image data language (Sabir); verbosity (Hu).

**Interventions on LLMs.**
- Worked: cultural persona (71-81% of countries improved); correct cultural description (1.5 to 2.5); Arab-context demonstrations lowered Western bias for most models (Naous); "consider the culture associated with the query language" (Wang); better pretraining language mix (AlKhamissi).
- Did not work or backfired: prompt language alone (Durmus: Russian, Chinese, Turkish prompts did not move answers toward those speakers; Sun and Wang d=0.045); culture token (Naous); personas for accuracy (Zheng); personas producing stereotypes (Durmus); false context accepted (Cao).

## 6. Language models

**Defaults.**
- Values: nearest English-speaking and Protestant European countries; farthest Jordan 4.10, Libya 4.00 (GPT-4o); GPT-4 farthest Jordan 4.19 (Tao 2024, 107 countries and territories, 10 prompt variants per item).
- Atari 2023: 65 national samples, 262 variables, 1,000 GPT samples per question; r=-.70 with cultural distance. Triad task 1,100 runs, 20 triads, 31 populations; GPT closest to Netherlands, Finland, Sweden, Ireland. Triad scores are in figures only.
- Knowledge: non-English queries return English-culture answers; ERNIE 7.6 vs GPT-4 1.8 on Chinese concrete items (Wang 2024). Naous 2024 (CAMeL, 628 prompts, 20,368 entities, 16 models): Cultural Bias Score 40-65% even for Arabic-only models.
- Norm judgement (NormAd, 2.6k stories, 75 countries): with an explicit rule best models under 82% vs humans over 95%; with value or country only under 60% vs humans over 90%.
- Moral dilemmas (MultiTP, 19 LLMs, 107 languages): alignment varies widely by language.
- WorldValuesBench (94,728 participants): share within Wasserstein 0.2 of the human distribution: Alpaca-7B 11.1%, Vicuna-7B 25.0%, Mixtral-8x7B 72.2%, GPT-3.5 75.0%.

**Nisbett-style tests.**
- Jin 2023: GPT-3.5 AHS 5.35 (SD 0.11), GPT-4 5.01 (SD 0.10) vs human 4.87 (SD 0.49, N=702), p<.001; 10 runs, temperature 1. Independent self: GPT-3.5 6.98, GPT-4 5.32 vs 4.73 (N=382). Holistic on thought scales, individualist on self scales. Design limits in M9.
- Hu 2026: 2x2 (US vs Chinese model x English vs Chinese prompt), 8 tasks, 100 runs per cell, temperature 1. Origin did not predict the human pattern. The US image model made MORE objects (11.53 vs 8.10, d=1.01), the reverse of human data. Chinese prompts gave more objects in image generation (10.71 vs 8.91, d=0.49); English gave more in text scene description (10.90 vs 10.06, d=0.36). ERNIE with English prompt answered ideal low-arousal positive affect with mean 5.00, SD 0.00. Image affect did follow stereotypes (HAP 113 US vs 79 CN, chi2=28.36; LAP 41 CN vs 2 US, chi2=40.91).
- Sun and Wang 2025: 8 models, temperature 0, 4 experiments. Language d=0.045; origin d=0.169 (English prompts only, eta2 0.0071); framing d=-2.095, eta2 0.542. Language was significant in 3 of 8 models in Exp 2.
- Sabir 2025: VLM captions mostly analytic (19-26% holistic at 6-shot on COCO). Japanese images raise it to 59-73%; GPT-4o-JP 26.10% on COCO vs 73.37% on 1K-JP; back-translation moves the ratio by 13.21% on average. Judge is GPT-4o.
- Contradiction: AlKhamissi 2024 finds prompt language matters for survey alignment (Arabic for Egypt, English for US); Sun and Wang and Hu find it does not switch reasoning style. Likely values vs reasoning; untested.

**What changes reasoning behaviour, and by how much.**
- Prompt format: median 7.5 points, up to 76 (Sclar 2024; open models, few-shot, mostly classification, no chain-of-thought tasks).
- Personas: none on MMLU (2,410 questions, 162 personas). Role-play as CoT trigger: AQuA +10.3 points (ChatGPT, weak zero-shot baseline).
- Question language: 3 points on MGSM (PaLM-540B).
- Content effects: models share belief bias with UK humans (625 plus 360; Lampinen 2024). No non-Western human data.
- Version drift: GPT-3.5-turbo and 4o more secular, 4-turbo more traditional (Kruskal-Wallis P=0.036, Tao). No ablation separates RLHF from data (d11, d14).

**Summary.** A model's "culture" is shallow, prompt-sensitive, version-dependent and mostly about values and knowledge. On reasoning accuracy, language and persona changes are small. Reasoning-style claims for LLMs lack a large same-study human reference.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Tag every human-evidence line with population, N per cell and design.** Part: G evidence weighting, memory. [E] a01, b01, b16, a23; K01. Single-population or small-cell findings count as [S] at most.
2. **Cite a cultural reasoning difference only with the cue or instruction under which it appeared.** Part: G evidence weighting. [E] b08, d02; K02.
3. **Report sensitivity and bias separately in any belief-bias or style test.** Part: G. Equal competence with different strategy is not a deficit. [E] a11, a12 (K05); b10 numbers are [S] (K03).
4. **Do not hard-code a "cultural style" or East/West module.** Part: 4b (not to add). The downgrade is safe even though the replication record is [C]: b14, b15, b11, a15, a16; K04.
5. **Report any agent comparison as a range over at least 5 paraphrases per item, not one wording.** Part: G7 measurement rule, S1 wording. [E] d07, a15; K21.
6. **Normalise output counts by length before using them as a quality or style signal.** Part: G5 (scores already length-normalised). [E] a16, b21, b23; K13.
7. **Do not add personas or language switching to the scaffold for reasoning.** Part: 4b. [C] d08, d09, a15; reopen only if the test below beats plain "think step by step".
8. **Do not trust injected context without an outside check.** Part: S1 input hygiene, G3 spirit. [S] c05 (K17), consistent with the schema's own sources (F07).
9. **A "universal" verdict needs power and cultural spread, not non-significance.** Part: G evidence weighting. [E] for the logic (b12, M5); the ML2 numbers are [S] (K06 [C]).

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Translated paraphrases keep accuracy within noise (language-neutral core) | S1, G | [S] | d10, K23 |
| Paraphrase-ensemble restatement in S1 narrows wording variance at equal tokens | S1, O | [S] | d07, a15, K11, K21 |
| Persona prompt vs plain CoT control | 4b | [C] | d08, d09, K22 |
| Non-WEIRD reference check on default answers for opinion or norm items | memory, G | [S] | b25, d06, K14 |
| Cultural-context line ("consider the culture associated with the query language") on locally grounded items | S1 | [S] | c12, c09, K15, K16 |
| Content-neutral vs content-conflict versions to catch belief bias | G, S8 | [S] | c17, d13, K18, K25 |
| External check on injected context | S1 | [S] | c05, K17 |
| Cue-wording flip size in the agent vs humans (d=0.86) | G | [S] | d02, K02 |

## 8. Concrete tests on our bench

All arms at equal tokens. Report mean and range across 5 paraphrases; at least 100 runs per cell when the metric is a rate.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Brainteaser and ARC items, 5 paraphrases each | plain vs scaffold with paraphrase restatement | accuracy range (max-min) and eta2 of wording | wording spread of several points (Sclar median 7.5); restatement narrows range without lowering mean |
| T2 | Same items in 5 languages (back-translation checked) | plain English vs plain translated; scaffold both | accuracy per language, drop vs English | drop about 3 points (as in MGSM); over 5 points flags a language-bound path |
| T3 | Persona vs control | plain; plain + "think step by step"; plain + expert persona; persona + CoT trigger | accuracy | persona alone no gain (Zheng); persona + CoT matches CoT only (Kong effect is CoT) |
| T4 | Belief-bias syllogisms in 4 cells | plain vs scaffold with validity check | d-prime and criterion | validity sensitivity high in both; scaffold lowers criterion shift on unbelievable-valid |
| T5 | Rule vs similarity categorisation under two wordings ("belong to", "similar to") | plain agent, 100 runs per wording | proportion rule choice per wording; interaction | instruction effect present; test whether its size matches human d=0.86 |
| T6 | Locally grounded non-English items | plain vs plain + cultural-context line | accuracy; residual gap to English-context items | gain of a few points; residual remains (Tao: 19-29% of countries not improved) |
| T7 | Injected context true / false / irrelevant | plain vs scaffold with outside check | accuracy shift | false context lowers plain accuracy; check removes most of the drop |
| T8 | Style metric audit | raw counts vs per-100-token counts | correlation with output length | raw counts track length; normalised do not |

## 9. What does not transfer, and why

- **The Nisbett effects themselves.** They describe human habit tied to social worlds, schooling and language. An LLM has no social world. LLM differences by prompt language are weak (d=0.045) or reversed (Hu 2026).
- **Survey alignment as reasoning.** Value and opinion alignment (Tao, Cao, Durmus) does not test how the model reasons.
- **Human self-report scales.** Jin 2023 scales need self-insight; agree-bias and 10 runs make small SDs and large t-values. Do not adopt a "holism score".
- **Face and visual perception results.** Perception, not reasoning. Useful only for the competence-vs-strategy lesson.
- **Rice-wheat ecology.** It acts on a human developmental environment. A model's data mixture is the nearest analogue and no ablation exists.
- **Priming of orientation.** Mixed replication record (sibling subfield); no basis for a primed switch in the agent.
- **Cultural personas to raise accuracy.** The value-shifting result does not extend to accuracy (Zheng 2024).
- **Many Labs 2 numbers.** Human effect sizes on social psychology items; they inform evidence weighting, not agent design.

## 10. Open questions

1. Exact N, effect sizes and original-author replies for Mercier 2015 and Hakim 2017 (abstract only here).
2. Norenzayan 2002 Study 1 N (not read).
3. Whether Many Labs 2 moderation holds with continuous cultural distance (ML2 text used a binary split).
4. Atari 2023 per-task numbers, including the triad holism score (figure only).
5. Any LLM test of change blindness, contradiction or framed-line tasks with same-study human data and 100+ runs per cell.
6. Whether RLHF or pretraining data causes Chinese vs US model differences; no base-vs-tuned ablation.
7. Whether personas or language switches change accuracy on logic, math or ARC.
8. Belief bias and content effects in non-Western human samples (Lampinen is UK only).
9. An independent causal replication of rice-wheat.
10. Whether an equal-token control or chain of thought shrinks Sclar's format spread.
11. Why survey tasks respond to prompt language (AlKhamissi) and reasoning tasks do not (Sun and Wang, Hu).
12. Whether LLM style changes across versions (Tao: no trend, P=0.036); re-test per version.

## 11. Sources

[V] opened and read this session (full text or most of it). [M] snippet, abstract or secondary only.

- [V] Henrich, Heine, Norenzayan (2010) The weirdest people in the world? BBS 33. https://www2.psych.ubc.ca/~henrich/pdfs/WeirdPeople.pdf (a01, a03-a06, a23, a24, b01-b07)
- [M] Segall, Campbell, Herskovits (1966), numbers via Henrich 2010 (a02)
- [M] Nisbett, Peng, Choi, Norenzayan (2001) Culture and systems of thought. https://doi.org/10.1037/0033-295X.108.2.291 (a07)
- [V] Norenzayan, Smith, Kim, Nisbett (2002) Formal versus intuitive reasoning. https://public.websites.umich.edu/~nisbett/formalreas.pdf (b08-b10; critique.md note 7 flags these b-lines as unverified in the checking session; Study 2 numbers re-confirmed via d02)
- [M] Masuda and Nisbett (2001). https://doi.org/10.1037/0022-3514.81.5.922 (a09)
- [M] Peng and Nisbett (1999). https://doi.org/10.1037/0003-066X.54.9.741 (a10)
- [V] Blais et al. (2008) Culture shapes how we look at faces. https://pmc.ncbi.nlm.nih.gov/articles/PMC2515341/ (a11)
- [V] Caldara, Zhou, Miellet (2010) Spotlight. https://pmc.ncbi.nlm.nih.gov/articles/PMC2841167/ (a12)
- [V] Talhelm, Zhang, Oishi (2018) Moving chairs in Starbucks. https://pmc.ncbi.nlm.nih.gov/articles/PMC5916507/ (a13)
- [M] Talhelm et al. (2014) Large-scale psychological differences within China. https://doi.org/10.1126/science.1246850 (b17, abstract)
- [V] Talhelm et al. (2024) Quasi-random assignment to rice and wheat farming. https://www.nature.com/articles/s41467-024-44770-w (d01)
- [V] Klein et al. (2018) Many Labs 2, preprint full text. https://osf.io/download/9654g/ (d02, d03); [M] published abstract https://doi.org/10.1177/2515245918810225 (b11)
- [V] Schimmelpfennig et al. (2024) Many Labs 2 and culture. https://www.nature.com/articles/s44271-024-00135-z (b12, b13)
- [M] Hakim, Simons, Zhao, Wan (2017). https://doi.org/10.1177/1948550616667613 (b14, d05)
- [M] Mercier, Zhang, Qu, Lu, Van der Henst (2015). https://doi.org/10.1163/15685373-12342140 (b15, d04)
- [M] Rad, Martingano, Ginges (2018). https://doi.org/10.1073/pnas.1721165115 (b16)
- [V] Jin et al. (2023) Is ChatGPT a holistic or analytic thinker? https://arxiv.org/abs/2308.14242 (a14, a22, b18, b19)
- [V] Sun and Wang (2025) Fragility of cultural tendencies in LLMs. https://arxiv.org/abs/2510.05869 (a15, a25, a27)
- [V] Hu et al. (2026) Machine culture. https://arxiv.org/abs/2601.17096 (a16, a26, b20-b22, d11)
- [V] Tao et al. (2024) Cultural bias and cultural alignment. https://arxiv.org/abs/2311.14096 (a17, b26, c01-c03, d14)
- [V] Cao et al. (2023) Cross-cultural alignment of ChatGPT. https://arxiv.org/abs/2303.17466 (a18, c04, c05)
- [V] Wang et al. (2024) Not all countries celebrate Thanksgiving. https://arxiv.org/abs/2310.12481 (a19, c11, c12)
- [M] AlKhamissi et al. (2024) Cultural alignment of LLMs (abstract and result prose). https://arxiv.org/abs/2402.13231 (a20, b27, c21)
- [V] Atari et al. (2023) Which humans? full text https://osf.io/5b26t/ (d06); earlier abstract-only lines a21, b25, c18 [M]
- [V] Durmus et al. (2023) GlobalOpinionQA. https://arxiv.org/abs/2306.16388 (c06, c07)
- [V] Naous et al. (2024) Having beer after prayer. https://arxiv.org/abs/2305.14456 (c08, c09)
- [V] Masoud et al. (2024) Hofstede's dimensions. https://arxiv.org/abs/2309.12342 (c10)
- [V] Rao et al. (2025) NormAd. https://arxiv.org/abs/2404.12464 (c13)
- [V] Zhao et al. (2024) WorldValuesBench. https://arxiv.org/abs/2404.16308 (c14)
- [V] Jin et al. (2025) Multilingual trolley problems. https://arxiv.org/abs/2407.02273 (c15)
- [V] Kharchenko et al. (2025) Values across cultures. https://arxiv.org/abs/2406.14805 (c16)
- [V] Lampinen et al. (2024) Content effects on reasoning. https://arxiv.org/abs/2207.07051 (c17, d13)
- [M] Ji, Zhang, Nisbett (2004) Is it culture or is it language? https://doi.org/10.1037/0022-3514.87.1.57 (c20)
- [V] Santurkar et al. (2023) Whose opinions do language models reflect? https://arxiv.org/abs/2303.17548 (c22)
- [V] Sclar et al. (2024) Prompt formatting sensitivity. https://arxiv.org/abs/2310.11324 (d07)
- [V] Zheng et al. (2024) Personas in system prompts. https://arxiv.org/abs/2311.10054 (d08)
- [V] Kong et al. (2024) Role-play prompting. https://arxiv.org/abs/2308.07702 (d09)
- [V] Shi et al. (2023) MGSM. https://arxiv.org/abs/2210.03057 (d10)
- [V] Sabir et al. (2025) Cognitive styles in vision-language models. https://arxiv.org/abs/2507.00700 (b23, b24, d12)
- [M] "Questioning the Rice Theory" (2018, title and citation count only). https://doi.org/10.3724/SP.J.1041.2018.00572 (d16)
- Process notes, not sources: c24, d15. Own syntheses, not sources: a22, a25, c23.
