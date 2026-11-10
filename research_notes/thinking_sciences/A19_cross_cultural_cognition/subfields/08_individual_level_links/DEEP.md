# Individual-level links: deep document

*Subfield A19.08. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K28), critique.md in this folder. Evidence ids a01-a30, b01-b26, c01-c25, d01-d18. Date: 2026-11-10.*

## 1. What it is

The claim is simple. Cultures differ in how people think. East Asian samples tend toward holistic thought (attend to the whole field, relations, change). Western samples tend toward analytic thought (objects, categories, rules). The leading theory says the cause is social orientation: interdependent societies train holistic attention, independent societies train analytic attention.

If that theory worked for single people, a person's social-orientation score would predict that person's cognitive style. Na et al. (2010) tested this directly. It does not hold. Inside one group, the measures barely correlate with each other. Yet the same measures separate groups cleanly.

So the pattern is "group yes, individual no". A style that describes a culture or a class does not describe a person drawn from it.

Why this matters for our agent. We build one language-model agent that thinks well through a scaffold. Two cautions follow.
- Never infer how a single case (one user, one prompt, one run) thinks from a group label. Group labels predict groups.
- An LLM is not a person from a culture. It is a mix of cultures that moves with context. Human psychometric scales do not carry over cleanly.

This subfield is mostly a limit on other A19 subfields (holistic/analytic style, priming, language effects, persona simulation). It yields few new schema parts. It yields several things not to add. [E]

Note on naming: the task text says "Na et al. 2009". That is the unpublished manuscript cited by Varnum et al. (2010) (a02). The published paper is PNAS 2010 (a01, d01).

## 2. History and theories in depth

**Between and within structure (1973).** Shweder (1973), "The between and within of cross-cultural research", made the methods point: structure between groups can differ from structure within groups. We know it only through citation in Varnum et al. (a30). The ecological fallacy is the older name for the same family of error.

**Founding statement of the group theory (2001).** Nisbett, Peng, Choi and Norenzayan (2001, a10) set out holistic versus analytic thought. East Asians: whole field, causes in the field, dialectical reasoning, less formal logic. Westerners: objects, categories, rules, formal logic. They speculated that social systems are the origin. Masuda and Nisbett (2001, a11) gave the classic task: Japanese described more context and relations in underwater scenes and recognised old objects better in the original setting. Sample sizes were not read.

**Group-level support (2001-2014).** Tight contrasts inside one nation or region were used to rule out language and genes (a05):
- Farming and fishing villages versus herding villages in Turkey (Uskul et al. 2008, a12).
- Hokkaido settlers versus mainland Japan (Kitayama et al. 2006, a13). Hokkaido residents were nearly as independent as European Americans.
- Rice versus wheat regions of China, N = 1,162 Han Chinese in six sites (Talhelm et al. 2014, a16).
- Northern versus southern Italy, working versus middle class in the US (a05).
Each is a group comparison. That is the level at which the construct holds together.

**Meta-analyses.**
- Oyserman and Lee (2008, a06): priming individualism or collectivism shifts cognition and relationality with moderate effects, and self-concept and values with small effects. The Varnum et al. review gives mean d = .53 and says prime type and sample (Western or Asian) did not matter.
- Oyserman, Coon and Kemmelmeier (2002, a07, b07): European Americans are not more individualistic than African Americans or Latinos, and not less collectivistic than Japanese or Koreans. Among Asians only Chinese show large effects. Attribution and cognitive style show large effects. Abstract only.

**The individual-differences test (2007-2010).** Choi, Koo and Choi (2007, a15) built the 24-item Analysis-Holism Scale (AHS) in six studies. High scorers behaved more holistically on a categorisation and a causal task. This was an early claim that self-report works at the person level. Na et al. (2010) then ran a far larger battery and found near-zero links across tasks. They are not strictly contradictory: one scale predicting two tasks is not the same as 20 measures forming one factor.

**The founding result (Na et al. 2010).** Details in section 3. The authors came from the group-level camp (Nisbett, Kitayama, Varnum), so this is a self-critique from inside.

**Authors' explanation (post hoc).** One trait can be expressed through different behaviours in different people. One person is independent through a strong unique self, another through a drive to compete. So single indicators correlate weakly while an aggregate still marks the group (a03, d05). The authors write "it would seem likely". It is untested. They list as open: whether the link is one-way, and why the constructs cohere at group but not person level (a04). A third variable could explain the group covariation.

**Competing explanation: measurement artefact.**
- Heine, Lehman, Peng and Greenholtz (2002, a08): Likert self-reports of collectivism often fail to show the East Asian versus North American gap that experts agree on. People rate themselves against different reference groups. Fixing the reference group restored differences. In one study, cultural groups inside one country differed more than groups from different countries.
- Kitayama et al. (2009, a14): implicit markers of independence separated North Americans from British, Germans and Japanese, while explicit self-belief did not follow.
- Vignoles et al. (2016, a09, d14): simple independent-versus-interdependent self-report fails to fit global variation. They built a 7-dimension model (Difference, Connection, Self-Direction, Self-Reliance, Consistency, Self-Expression, Self-Interest). Study 1 N = 2,924 students, 16 nations. Study 2 N = 7,279 adults, 55 groups, 33 nations. Person-level strength of links not obtained; full text blocked.
- Na et al. reply: reliability does not fully explain it (test-retest r = .51 on one task; dropping measures with alpha < .60 left mean r = .031). The reliability table was not read (d04).

**Citing literature.** Na et al. has 392 citations (Semantic Scholar, b02). Of the first 60 seen as snippets, none reported a direct replication. Snippets repeat the claim: self-construal scores are largely unrelated to implicit tendencies at the individual level (b04); reliable group measures are often unreliable individual measures (b05); analytic-holistic style does not explain within-culture variation (b06). A 2023 paper, "Analytic and holistic cognitive style as a set of independent manifests", is reported to find no associations among measures (b03, 11 citations). It was not opened.

**The LLM turn (2022-2026).** The question moved to machines in three forms.
1. Do LLMs have a cultural thinking style? (Jin et al. 2023; Lu, Song and Zhang 2025; Sabir et al. 2025; Hu et al. 2026.)
2. Does prompting a language, country or persona switch that style? (Sun and Wang 2025; Tao et al. 2024; Durmus et al. 2023; Cao et al. 2023.)
3. Can LLM personas stand in for individuals? (Argyle 2023; Park 2024; Hu and Collier 2024; Wang 2025; Taday Morocho 2026; Venkit 2026.)
Almost all of this is group-level (country) alignment. None tested the Na et al. structure inside an LLM: correlate social orientation and cognition across many sampled personas (critique.md, gap 2).

## 3. Core findings with exact numbers

Status: established = read in the source and consistent across sources; single-source; contested; plus caveats (human-only, older models only).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Within one US sample, social-orientation measures barely correlate | N=235 adults (phone directory, ages 25-93, three sessions), 10 social + 10 cognitive measures. Social: mean r=.008, median .008 over 45 pairs; 2 of 45 significant and positive; first factor 12.26% of variance (chance for 10 measures is 10%) | Na et al. 2010 (d01) | established, one sample |
| Cognitive-style measures barely correlate | Mean r=.038, median .040; first factor 10.69%. Contrast: WAIS-IV subtests mean r=.48; NEO-PI-R facet loadings mean .64 | d01 | established, one sample |
| Composite social vs composite cognitive | r=.11. Mean within-domain task r<.06 | Varnum et al. 2010 (a02) | established (same authors) |
| The same measures separate groups (class) | Social: working class more interdependent on 7 of 10, 4 significant, 1 opposite; aggregate t(188)=2.81, p<.01. Cognitive: more holistic on 7 of 10, 5 significant, 1 opposite; aggregate t(213)=3.51, p<.001. Published East-West d used to pick measures: .54 social, .62 cognitive | d02 | established |
| Five-culture check of two tasks | US, UK, Germany, Croatia, Japan. Person-level r=.04 pooled; median within-culture r=-.047; US+Japan only r=.070; culture-level r=.73; multilevel second-level r=.82 | d03 | established; secondary analysis, 2 tasks |
| Group effect plus zero within-group r gives tiny pooled r | d=.4 gives r about .038-.039. Simulation 2 groups of n=100, 10 variables, 10,000 runs: mean r=.038. d=1 gives r about .2 | d04 | established (maths) |
| Reliability does not fully explain it | Test-retest r=.51 for one measure (1-4 weeks). Excluding alpha<.60 measures: mean r=.031, median .072. Table S3 not read | d04 | single-source (authors) |
| Priming moves cognition within a person | Moderate for cognition and relationality, small for self-concept and values. Mean d=.53 (as quoted in Varnum et al.) | Oyserman and Lee 2008 (a06) | established (meta-analysis; abstract + review) |
| Self-report collectivism often misses known group gaps | Reference-group effect; fixing reference restored differences | Heine et al. 2002 (a08) | established; abstract only |
| One-axis independence model fits poorly worldwide | 7 dimensions; N=2,924 (16 nations) and N=7,279 (55 groups, 33 nations) | Vignoles et al. 2016 (a09, d14) | contested; person-level strength unknown |
| Early individual-difference scale validity | AHS, 24 items, 6 studies; Koreans > Americans; predicted two tasks | Choi et al. 2007 (a15) | contested against Na et al.; abstract only |
| ChatGPT is holistic on cognition scales | AHS: GPT-3.5 5.35 (SD .11), GPT-4 5.01 (.10), human norm 4.87 (.49, N=702), p<.001 both. Triadic relational share 0.87 and 0.85. 10 runs per cell | Jin et al. 2023 (a17, c01) | single-source; older models only |
| ChatGPT is not clearly Eastern on value scales | DSS 4.59 vs norm 4.00 (N=158) for GPT-3.5; GPT-4 3.97, p=.344. SCS-Independent 6.98 and 5.32 vs 4.73 (N=382). SCS-Interdependent 5.85 and 4.95 vs 4.81 (GPT-4 p=.07, so "near norm" is marginal) | a18, c01, critique | single-source; older models only |
| Prompt language does not reliably switch style | 8 models, temperature 0, 30-60 items per language vs 4-21 originally. Exp 1 mean diff 0.0053, p=.150, d=.045. Exp 3 p=.25, Exp 4 p=.917; most rows "negligible" (diff about .008-.015 on 7-point scale); one row p=.007 d=.137; one p=.021 d=.204 | Sun and Wang 2025 (b10, c03, c04) | contested (original not verified) |
| Original claim that language switches style | GPT and ERNIE more interdependent/holistic in Chinese; 4-21 items per task, 2 models; persona result "exploratory" | Lu, Song and Zhang 2025 (c05, d06) | contested; abstract only |
| Model origin and language reverse the expected pattern | R-C score US model 8.10 (SD 1.44) vs Chinese 6.04 (1.54), t=-13.81, d=1.38 (opposite to humans). Landscape objects US 11.53 vs Chinese 8.10, d=1.01. Chinese vs English prompt objects 10.71 vs 8.91, d=.49; scene objects English 10.90 vs Chinese 10.06, t=-3.60, d=.36; R-C by language 7.10 vs 7.04, p=.741, d=.03; horizon p=.096 | Hu et al. 2026 (a22, a23, b23) | single-source; preprint |
| Image output follows stereotype, text does not | Success images HAP US 113 vs Chinese 79, chi2=28.36; LAP Chinese 41 vs US 2, chi2=40.91. Big smiles ideal: Chinese 0.78 vs US 0.60, t=8.10, d=.40 (opposite to humans). Chinese model with English prompts: Ideal LAP mean 5.00, SD 0.00 (ceiling) | a24, d10 | single-source |
| VLM caption holism depends on judge, language, image | GPT-4o 5-shot 19.22% holistic; GPT-4o-JP 23.64%. 6-shot balanced 19.80% vs 28.64%. Japanese photo set 73.37% (GPT-4o-JP 6-shot) vs 26.10% COCO 1K; plain GPT-4o 59.10% on the Japanese set. Human check (200 images): GPT-4o-JP 17.75% vs judge 29.00% | Sabir et al. 2025 (a20, a21) | single-source |
| LLM values move far more than human values | Largest human mean shift d=0.53 (conformity -0.52 after a movie); ChatGPT up to abs(d)=5.86 (one pair, history vs joke; many pairs 1-3). Rank-order: human lowest r=.57; ChatGPT .42 and .36, down to .04. Ipsative: human lowest r=.59; ChatGPT as low as .05 | Kovac et al. 2023 (b08, c06, c07) | established; mostly one early model |
| Default LLM answers sit near US/Western European respondents | GPT-4o nearest Finland 0.20, Andorra 0.21, Netherlands 0.45; farthest Jordan 4.10, Libya 4.00, Ghana 3.95. Over 93% of GPT-3 training text English | Tao et al. 2024 (a25, c11); Johnson 2022 (b22); Durmus 2023 (b20) | established |
| Country prompting helps on average but fails for some | Mean distance 2.42 to 1.57 (GPT-4o), 2.69 to 1.65 (GPT-4), 2.71 to 1.77 (GPT-4-turbo), 2.39 to 2.11 (GPT-3), 3.35 to 2.83 (GPT-3.5-turbo), all P<.001. Improves 71.0%, 77.6%, 81.3%, 80.4%, 72.6% of 107 countries, so 19-29% get worse. GPT-4o Jordan 4.10 to 0.36, Finland 0.20 to 2.43 | a25, c11 | established |
| Stereotype in country prompt | Prompted as Russian: 73.9% "unacceptable" vs 42.1% of real Russians; default model 0.8% unacceptable | Durmus et al. 2023 (b20) | single-source |
| Country alignment with Hofstede is weak | 36 countries, 5 dimensions: one significant correlation (GPT-4o individualism, r=.71, p<.05); GPT-4 uncertainty avoidance r=-.656 (wrong sign); range about -.49 to +.48. Cao et al.: 5 countries, 24 questions, US .70 (p=.12), China -.77 (p=.07) | Kharchenko 2025 (b16, c12); Cao 2023 (b18, c09) | established (weak) |
| Persona alignment worse for marginalised persons | Egypt 47.16 soft / 27.03 hard vs US 59.07 / 33.78 (mean over 4 models); GPT-3.5 Egypt 48.61 / 25.99, US 64.86 / 39.29 | AlKhamissi et al. 2024 (b14) | single-source |
| LLM scale answers are unstable | One human between-country SD = 0.114; format changes often exceed it. LLM-to-human distance over human-to-human distance: 6.14 (one prompt), 1.94 (optimised prompt) | Khan et al. 2025 (d07) | established (preprint) |
| Demographics explain little of individual variation | <10% of annotation variance (linear R2); 1.5% of response-similarity variance (124 US participants, 7 models, 134 questions); human within-race r=.155 (White), .208 (Black) | Hu and Collier 2024 (a27); Venkit 2026 (d12) | established; annotation and US tasks |
| Demographic personas do not beat no persona | Hard similarity Llama-2-13B .370 vanilla vs .366 persona; Qwen3-4B .391 vs .398; random .273. Soft .621 vs .612 and .627 vs .627. Over 70K instances | Taday Morocho 2026 (d11) | established; 2 small models |
| Personal interview beats demographics | N=1,052. GSS normalized accuracy: interview .83 (raw 65.67% / retest 79.53%), survey .82, survey+interview .86, demographics .74, persona .71; F(4,5255)=577.83. Big Five r: interview .78 (norm .80), demographic .61. Games: interview .66, demographic .48, no significant difference p=.16. 96 of 120 interview minutes removed: .79 | Park et al. 2024 (a28, c18, c19) | established; context length not equalised |
| Group-label simulation flattens and misportrays | 3,200 participants, 16 identities, 4 LLMs; GPT-4 and GPT-3.5 covered about 3 of 5 options in 100 samples | Wang et al. 2025 (a29, c20) | single-source |
| Alignment tuning collapses diversity | Human diversity 37.9; vanilla all above 17.5; every culturally fine-tuned model below 11.0; Gemma-2 +2.2 alignment, -17 diversity (to 0.5); Qwen Nigerian low-status persona 51.52 to 37.59 (-27.04%) | Zhang et al. 2026 (d09) | single-source; 6 models of 7-8B |
| Persona system prompts do not help factual accuracy | 162 roles, 4 model families, 2,410 questions; automatic persona choice no better than random | Zheng et al. 2024 (d13) | single-source |
| Culturally adapted math text costs accuracy | 0.3% (Claude 3.5 Sonnet) to 5.9% (LLaMA 3.1-8B), 14 models | d15 (snippet) | single-source; snippet only |
| Culture in LLM work is proxied by country or language | 37 of 90 papers region, 35 of 90 language, 17 of 90 both; none define culture | Adilazuarda et al. 2024 (c21) | established (survey) |

Warning on numbers: 8.10 appears three ways in Hu et al.: US R-C score, Chinese-model landscape object count (b23 gives 8.10, SD 1.91), and t=8.10 for smiles. Do not mix them. The Jin et al. extracted table labels the GPT-4 AHS row "DSS" (layout glitch). Kovac's 5.86 is one extreme pair, not typical.

## 4. Mechanisms and models

**4.1 Between-group versus within-group correlation (the core model).**
Let each person i in group g have x = mu_g + e and y = nu_g + f, with e and f independent noise. The pooled correlation is within-group covariance plus between-group covariance, over total spread. With zero within-group covariance, pooled r depends only on the group effect size d. For two equal groups and d = .4, r is about .038. For d = 1, r is about .2 (d04). So large group differences and near-zero person-level links are compatible. A high culture-level r (.73) does not imply a person-level r (.04, d03).

Implementation rule: when a claim comes from group means, tag the level. A group mean predicts a group mean. Never turn it into a per-person or per-run rule.

**4.2 Aggregate indices versus single indicators.**
Each single measure carries mostly specific variance plus a small group signal. Averaging 10 measures cancels the specific variance and keeps the group signal. So the aggregate separates groups (t = 2.81 and 3.51, d02) while single pairs correlate about .01-.04 (d01). Authors' reading: one trait, many expressions. Alternative reading: the measures are different constructs (a set of independent manifests, b03). Both predict the same data. The data cannot tell them apart. [C]

**4.3 Reference-group bias (artefact explanation).**
Self-report = true standing minus the standing of the comparison group the person has in mind. If groups pick different reference groups, group means converge and the group signal in self-report shrinks (a08). This damps group effects more than it destroys person-level links, so it does not fully explain the null person-level result. Na et al. check: dropping low-alpha measures left r = .031 (d04).

**4.4 Priming as a within-person causal lever.**
A short prime of independence or interdependence shifts cognition by d about .5 on average (a06). This is a context effect inside one session, a different route from stable traits. For an LLM the analogue is a context change (frame, topic, format). Kovac et al. show LLM expressed values shift much more under irrelevant context (up to abs(d) 5.86) than human values under real primes (largest d .53) (b08). So the LLM is a "superposition of perspectives" selected by context (c06).

**4.5 Stability tiers (how to measure "one individual").**
Kovac et al. use three. Mean-level change (Cohen d). Rank-order stability (correlation of item or person ranks across conditions). Ipsative stability (profile correlation within one individual across value items). Human floors from the literature: rank-order r = .57, ipsative r = .59. ChatGPT falls to .04-.05 under format change. An agent that must act like one stable individual should pass these. Current models do not under text-format changes (c07). Models differ: OpenAssistant most stable at mean level, GPT-3.5-0613 at rank order, Zephyr-7b-beta least at rank order (c08).

**4.6 Stable inside a prompt, unstable across prompts.**
Inside one fixed prompt, SD across runs is tiny (.06-.19 in Jin et al., a18) and zero at temperature 0. So 10 runs per cell give p < .001 against human norms, but this is run noise around one near-deterministic answer, not a population sample (critique). Across contexts the mean moves a lot (Kovac). Both are true (b25; our own synthesis). Report spread across wordings, not across seeds.

**4.7 Steering by label.**
A country, language or persona instruction moves output toward the target group's mean on average. It also flattens variance, leans on stereotype, and worsens 19-29% of countries (a25, b20, a29, d09). Mechanism proposals, all untested: RLHF "Service Persona Camouflage" (a24, d10; no base-versus-tuned test); training mix (more of a culture's language in pretraining gives better alignment, b15); judge and format effects (d07).

**4.8 Individual simulation needs individual data.**
Park et al.: the agent gets the person's two-hour interview in context and is scored against the person's own two-week retest (normalized accuracy = agent accuracy / retest accuracy). Interview .83, demographic .74, persona .71. Removing 80% of the interview still gave .79 (c19). Group labels carry some information (.74) but the person's own text carries more. Equal context length is not controlled (d18): the interview is far longer than a demographic line.

## 5. What holds up

**Holds up (human).**
- Group-level separation on these measures: consistent across cultures and class (d02, a05; a16 abstract). [E]
- Near-zero within-group correlations among the 20 measures, N = 235 (d01). Read in full. [E] for this sample; one sample, authors from the group-level camp.
- The maths of d = .4 and r = .038 (d04). [E]
- Priming effects are moderate (a06). [E]
- Self-report collectivism has a known reference-group problem (a08, a09, a14). [E]

**Not shown or unverified.**
- No independent direct replication of Na et al. was found in 60 citing snippets or later searches. Absence of search hits is not absence of replications (b02, d17). The 2023 "independent manifests" validation was seen only as a snippet (b03). [S]
- The reliability table (Table S3) and per-pair SI table were not read (d04).
- The authors' "one trait, many expressions" account is post hoc (a03, d05). [C]
- Whether a seven-dimension model gives stronger person-level links is unknown (d14).
- Measure counts differ by version: PNAS 10+10, an APS poster 5 social + 11 cognitive (a01). Unresolved.

**Failures and fragility (LLM).**
- Sun and Wang (2025) failed a conceptual replication of Lu, Song and Zhang: 8 models, 30-60 items per language, language effect d = .045, p = .150 (c03). Caveats: items were withheld by the original, so stimuli were rebuilt; preprint; the journal declined the comment (b10). Hu et al. also found reversals (a23). Jin et al. found a stable holistic lean in 2023 ChatGPT across temperature and wording (a19). These test different things: Jin asks about a model's default style; Sun and Wang and Hu ask whether prompt language switches it. Not strictly contradictory (critique).
- Khan et al. (d07, d08): a published LLM preference finding failed when an indifference option was offered. Odd and even Likert scales gave different country patterns.
- Hofstede alignment: one significant country-value correlation in 36 countries (c12). Cao et al. rest on 5 countries (c09).
- A country prompt that improves the mean can still worsen a given country (GPT-4o Finland 0.20 to 2.43).

**Moderators and boundary conditions.**
- Prompt language: no stable effect in 8 models (c03). Language matters more when it is the culture's dominant language and well represented in pretraining (b14, b15), but a balanced multilingual model did worse in English for the US survey than in Arabic (b15). Asking in Russian, Chinese or Turkish did not make answers closest to those speakers (b21).
- Image content dominates caption style: plain GPT-4o labels 59.10% of Japanese photos holistic (a21). Language alone has a small effect.
- Persona class and education: alignment rises with higher class and education, and for male and older personas; marginalised persons are modelled worse (b14, c14).
- Task type: image output follows stereotype; text does not (a24).
- Judge: GPT-4o judge and humans disagree by about 11 points on size (a21).
- Model family: OpenAI models resemble English-speaking and Protestant European countries (a25).

**Interventions that worked.**
- Country prompting: mean distance 2.42 to 1.57 (GPT-4o) (c11).
- Correct cultural description in the prompt improved ChatGPT alignment; wrong or irrelevant text did not (b19; scoring unclear).
- Anthropological prompting on GPT-3.5 raised Egypt alignment: soft .4834 to .5102, hard .2443 to .2838 (b14).
- Personal interview text as the persona: .83 vs .74 (a28).

**Interventions that did not work.**
- Demographic personas against no persona: .366 vs .370, .398 vs .391 (d11).
- Persona system prompts on factual accuracy (d13). The best persona per question cannot be picked in advance (d13).
- Cultural fine-tuning flattened diversity (d09).
- Translating the question into the target language (b21).

## 6. Language models

**Holistic or analytic style?** Jin et al. (a17, c01): GPT-3.5 and GPT-4 score above human norm on AHS (5.35 and 5.01 vs 4.87) and relational on the triadic task (.87, .85). On value scales GPT-3.5 inflated everything (agreement bias, a18); GPT-4 sat at norm on DSS (p = .344) and near norm on interdependence (p = .07). The same model is "holistic" by cognition scale and "not Eastern" by value scale. This echoes the human split, but it may come from acquiescence and pattern-matching, not a person-like structure (c23, untested). Only 10 runs per cell and 2023 models.

**Does prompt language switch style?** Lu et al. (c05, d06): yes for GPT and ERNIE (abstract only). Sun and Wang (c03): no for 8 newer models, d = .045. Hu et al. (a23): mixed, with reversals, and a model-by-language interaction on attribution F(1,396) = 18.21. Net: contested. Do not use language to steer reasoning style.

**Does model origin predict style?** Hu et al. (a22): the US model drew more objects and more relational pairings than the Chinese model, opposite to the human East Asian pattern (d = 1.38). Two models. Single-source.

**Vision-language models.** Japanese captions are somewhat more holistic (12.34% English vs 27.48% Japanese-original on COCO 5K, 6-shot, a21). Japanese images raise it to 59-73%. Few-shot count moves Gemma-JP from 13.50% to 21.14% (a20).

**Value stability.** LLM values move far more than human values under irrelevant context (b08, c06): mean shift abs(d) up to 5.86 vs human max .53. "The LLM has orientation X" is a context-dependent statement.

**Cultural survey alignment.** Defaults near US and Western Europe (a25, b20, c15). Country prompting helps on average and hurts about a fifth to a quarter of countries (c11). It leans on stereotype (b20) and flattens variance (a29, b18, d09).

**Format fragility.** Trivial formatting moves answers more than one human between-country SD (0.114) (d07). Steered LLM-to-human distance is 1.94-6.14 times human-to-human distance.

**Individual simulation.** Demographic personas do not beat no persona at matching real people in two small open models (d11), and demographics explain 1.5% of response-similarity variance (d12). Personal interview text lifts accuracy (a28). In humans, demographic similarity tracks response similarity at only r = .155-.208 (d12). So the ceiling for group-label simulation is low even for people.

**What changed behaviour, by how much.**
- Country prompt: mean distance down about 0.8-1.1 (GPT-4o, GPT-4), 0.3 (GPT-3), 0.5 (GPT-3.5-turbo).
- Interview in context: +0.09 normalized accuracy over demographics.
- Cultural fine-tuning: alignment +2.2 (Gemma-2), diversity -17 points.
- Prompt language: d about .045 (Sun and Wang).
- Format wording: more than one human SD.
- Culturally adapted GSM8K text: -0.3 to -5.9% accuracy (snippet).
- Persona prompts on factual accuracy: about zero on average.

**Gaps (no LLM study found).** No test that correlates social-orientation and cognitive-style scores across many sampled LLM personas. No test of cultural-style personas on real reasoning accuracy at equal tokens. No base-versus-RLHF test of the flattening claim. No 2025-26 model compared with human test-retest on these scales.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **No culture, language or demographic label as a reasoning steer or as voters.** Widens G4 (persona voters already banned). Group effects do not predict a single case; label prompts do not beat no persona; they flatten variance. Part G4. [E]. Evidence: d01, d03, d11, d12, a29, d13; K01, K12, K25.
2. **Do not decide how one user thinks from a group label.** If we adapt to a user, use that user's own text or history. Part memory (per-user record). [E]. Evidence: a28, c18, d11, d12; K15, K25. Caveat: equal context length not controlled (d18).
3. **Never read a self-report scale or stated style as evidence of how the agent reasons.** Judge by output checks. Widens G10 to cover scale and style answers. Part G10. [E] for the instability, [S] for the within-model split. Evidence: a17, a18, c23, d07; K06, K24.
4. **Bench hygiene: report spread across wordings and formats before trusting any difference.** A style or persona effect counts only if it exceeds variation from rewording, option order and format. Part G7 (pays for itself). [E]. Evidence: d07, b08, c07; K11, K24. Human between-country SD is 0.114; LLM shifts reach abs(d) 5.86.

### Test first

- **Orientation framing at S0** (S0, [S]). Add an independent frame, an interdependent frame or a neutral frame; measure answer shift. Human priming is moderate (a06); LLM context sensitivity is large (b08). Evidence a06, a07, b08. See UNKNOWNS U1.
- **Language as a style switch** (O3, [C], leaning not-add). Treat as not-add until a test passes. Evidence b10, c04, a23, c05. See U4.
- **Per-user note over group-profile note** (memory, [S]). Test at equal tokens (a28, d18). See U3.
- **Neutralising culturally flavoured item text** (S1 input hygiene, [S]). Adapted text costs 0.3-5.9% (d15, snippet). See U6.
- **Variance-preserving sampling** (G4 and O7 variance note, [S]). Persona flattening (d09, a29) means persona samples add no vote diversity. See U7.
- **Cultural-style persona on reasoning accuracy** (G4, [S]). d13 tested generic roles on factual questions only. See U2.
- **Persona correlation structure** (G12 side-note, [S]). See U5.

## 8. Concrete tests on our bench

Bench is the HTSA harness (ARC and BRAINTEASER items). All arms at equal tokens. Report pass rate with a bootstrap interval and the spread over three wordings.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | BRAINTEASER sentence and word puzzles, 200 items | Plain vs "answer as a person from [East Asia / US]" persona vs neutral extra sentence of equal length | Accuracy; paired difference vs wording spread | No gain. Difference below wording spread (d13, d11) |
| T2 | Same 200 items; English vs Chinese vs back-translated English | Same system prompt in three languages | Accuracy; item-level flip rate | Under 1 point. Replicates Sun and Wang (d .045) |
| T3 | Triadic categorisation and scene-description probes, 60 fresh items | Plain vs independent frame vs interdependent frame vs neutral frame | Share of relational answers; shift vs wording spread | Frame shift above neutral only if LLM context sensitivity (b08) carries over; unknown size |
| T4 | Probe battery, 3 wordings x 2 option orders | Same item reworded | Per-item answer stability (rank-order r across wordings) | Below human floor .57 for some scales (c07, d07). Confirms hygiene rule |
| T5 | 200 sampled personas answering AHS-type items and social-orientation items | Plain model with persona text | Pearson r between social composite and cognition composite across personas | Unknown. Humans: .11 composite. If LLM r is above .3, personas carry a synthetic stereotype |
| T6 | 50 simulated users each with a short personal note | A personal note; B group-label line; C no note; equal tokens | Match to the user's held-out answers | A above B by at least 0.05 if Park holds; B about equal to C |
| T7 | ARC items with neutral vs culturally flavoured wording | Same task | Accuracy | Costs 0.3-5.9% for weaker models (d15) |
| T8 | 10 attempts per item with and without a persona instruction | Plain vs persona | Distinct-answer count; vote accuracy | Persona flattens answers; no vote gain (a29, d09) |

## 9. What does not transfer, and why

- **The group result.** It is about people drawn from cultures. An LLM has no culture, no development and no social class. It is a mix selected by context (b08, c06).
- **Human scales as tools.** AHS, SCS and DSS were built and validated on people. Their reliability and factor structure for LLMs are unknown. GPT-3.5 gave "strongly agree" to almost everything (a18). Sun and Wang call this anthropomorphism (b11).
- **Run-to-run SD as sample variance.** 10 runs at fixed settings are not 10 people. The p < .001 values are run noise (critique).
- **The person-level null as an LLM fact.** It says nothing about correlation structure across LLM personas (gap 2).
- **Country steering as a reliable lever.** Prompting by country moves means but hurts 19-29% of countries (c11).
- **Survey alignment as reasoning quality.** Alignment to country means is a values measure. No study tied it to reasoning accuracy (gap 3).
- **Vision caption holism.** Judge bias and image content dominate (a21).
- **English-trained models and cultural psychology.** Over 93% of GPT-3 text was English (b22).
- **Hofstede and WVS country means.** Group level; LLM correlations rest on five or few countries (c09, c12).
- **Persona votes.** G4: samples from one model are not independent.

## 10. Open questions

1. Exact per-pair correlations and reliability in Na et al. (SI tables not read). Does an independent sample reproduce near-zero within-group correlations? (gaps 1, 7)
2. Is the weak link measurement artefact or real structure? Reliability per task per sample is missing. (K23)
3. Do LLM personas show the same weak link between social-orientation and cognition scores? (gap 2)
4. Do cultural-style personas help or hurt on real reasoning at equal tokens? (gap 3)
5. Who is right on language effects, Lu et al. or Sun and Wang? Items are withheld. (gap 4)
6. Does RLHF cause the flattening (Service Persona Camouflage)? Needs a base versus tuned comparison. (gap 8, d10)
7. Do individual-data personas beat group-label personas at equal context length? (gap 5, d18)
8. How large is the variance of 2025-26 models over neutral context changes versus human test-retest? (gap 6)
9. Does a seven-dimension self model give stronger person-level links than the one-axis model? (gap 9, d14)
10. Does the measure-count difference between versions (10+10 vs 5+11) matter? (a01)

## 11. Sources

[V] = opened and read (this session or in the earlier evidence pass). [M] = snippet or abstract only.

- Na, Grossmann, Varnum, Kitayama, Gonzalez, Nisbett (2010) Cultural differences are not always reducible to individual differences. PNAS 107(14):6192-6197. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC2851996/ (abstract: https://pubmed.ncbi.nlm.nih.gov/20308553/)
- Varnum, Grossmann, Kitayama, Nisbett (2010) The origin of cultural differences in cognition. Curr Dir Psychol Sci. [V] https://pmc.ncbi.nlm.nih.gov/articles/PMC2838233/
- Shweder (1973) The between and within of cross-cultural research. Ethos. [M] cited in https://pmc.ncbi.nlm.nih.gov/articles/PMC2838233/
- Nisbett, Peng, Choi, Norenzayan (2001) Culture and systems of thought. Psychol Rev. [M] https://pubmed.ncbi.nlm.nih.gov/11381831/
- Masuda and Nisbett (2001) Attending holistically versus analytically. JPSP. [M] https://pubmed.ncbi.nlm.nih.gov/11708567/
- Uskul, Kitayama, Nisbett (2008) Ecocultural basis of cognition. PNAS. [M] https://pubmed.ncbi.nlm.nih.gov/18552175/
- Kitayama et al. (2006) Voluntary settlement and the spirit of independence. JPSP. [M] https://pubmed.ncbi.nlm.nih.gov/16938025/
- Kitayama et al. (2009) A cultural task analysis of implicit independence. JPSP. [M] https://pubmed.ncbi.nlm.nih.gov/19634973/
- Choi, Koo, Choi (2007) Individual differences in analytic versus holistic thinking. PSPB. [M] https://pubmed.ncbi.nlm.nih.gov/17440200/
- Talhelm et al. (2014) Large-scale psychological differences within China. Science. [M] https://pubmed.ncbi.nlm.nih.gov/24812395/
- Oyserman and Lee (2008) Does culture influence what and how we think? Psychol Bull. [M] https://pubmed.ncbi.nlm.nih.gov/18298274/
- Oyserman, Coon, Kemmelmeier (2002) Rethinking individualism and collectivism. Psychol Bull. [M] https://pubmed.ncbi.nlm.nih.gov/11843547/
- Heine, Lehman, Peng, Greenholtz (2002) What's wrong with cross-cultural comparisons of subjective Likert scales? JPSP. [M] https://pubmed.ncbi.nlm.nih.gov/12051579/
- Vignoles et al. (2016) Beyond the East-West dichotomy. J Exp Psychol Gen. [M] https://pubmed.ncbi.nlm.nih.gov/27359126/ and https://doi.org/10.1037/xge0000175
- Semantic Scholar citation list for Na et al. (b02-b06). [M] https://api.semanticscholar.org/graph/v1/paper/DOI:10.1073/pnas.1001911107/citations
- Jin, Zhang, Shu, Cui (2023) The cultural psychology of LLMs. [V] https://arxiv.org/abs/2308.14242
- Lu, Song, Zhang (2025) Cultural tendencies in generative AI. Nat Hum Behav. [M] https://www.nature.com/articles/s41562-025-02242-1
- Sun and Wang (2025) The fragility of "cultural tendencies" in LLMs. [V] https://arxiv.org/abs/2510.05869
- Hu, Peng, Zhao, Qiu, Hung, Peng (2026) Machine culture as an emergent phenomenon. [V] https://arxiv.org/abs/2601.17096
- Sabir, Gasper, Loem, Sharma (2025) Contrasting cognitive styles in vision-language models. [V] https://arxiv.org/abs/2507.00700
- Kovac, Portelas, Dominey, Oudeyer et al. (2023) LLMs as superpositions of cultural perspectives. [V] https://arxiv.org/abs/2307.07870
- Tao, Viberg, Baker, Kizilcec (2024) Cultural bias and cultural alignment of LLMs. PNAS Nexus. [V] https://arxiv.org/abs/2311.14096 and https://academic.oup.com/pnasnexus/article/3/9/pgae346/7756548
- AlKhamissi, ElNokrashy, AlKhamissi, Diab (2024) Investigating cultural alignment of LLMs. [V] https://arxiv.org/abs/2402.13231
- Hu and Collier (2024) Quantifying the persona effect in LLM simulations. [V] https://arxiv.org/abs/2402.10811
- Park, Zou, Kamphorst et al. (2024) Generative agent simulations of 1,000 people. [V] https://arxiv.org/abs/2411.10109
- Wang, Morgenstern, Dickerson (2025) LLMs that replace human participants can harmfully misportray and flatten identity groups. [V] https://arxiv.org/abs/2402.01908
- Kharchenko, Roosta, Chadha, Shah (2025) How well do LLMs represent values across cultures? [V] https://arxiv.org/abs/2406.14805
- Cao et al. (2023) Assessing cross-cultural alignment between ChatGPT and human societies. [V] https://arxiv.org/abs/2303.17466
- Durmus et al. (2023) Towards measuring the representation of subjective global opinions. [V] https://arxiv.org/abs/2306.16388
- Johnson et al. (2022) The ghost in the machine has an American accent. [V] https://arxiv.org/abs/2203.07785
- Santurkar et al. (2023) Whose opinions do language models reflect? [V] https://arxiv.org/abs/2303.17548
- Argyle et al. (2023) Out of one, many. [V] https://arxiv.org/abs/2209.06899
- Adilazuarda et al. (2024) Towards measuring and modeling culture in LLMs: a survey. [V] https://arxiv.org/abs/2403.15412
- Khan, Casper, Hadfield-Menell (2025) Randomness, not representation. [V] https://arxiv.org/abs/2503.08688
- Zhang, Xu, Zhang (2026) Aligned but flattened. [V] https://arxiv.org/abs/2609.00565
- Taday Morocho, Cima, Fagni, Avvenuti, Cresci (2026) Reliability of persona-conditioned LLMs. [V] https://arxiv.org/abs/2602.18462
- Venkit, Li, Pruksachatkun, Wu (2026) Socially-grounded persona framework. [V] https://arxiv.org/abs/2601.07110
- Zheng, Pei, Logeswaran, Lee, Jurgens (2024) When "a helpful assistant" is not really helpful. [V] https://arxiv.org/abs/2311.10054
- Culturally adapted GSM8K search summaries (arXiv 2503.18018). [M] https://arxiv.org/abs/2503.18018

Links to subfields researched in parallel (not covered here): Priming of orientation; Conformity; Task-type limits; Methods and measurement; Pragmatics and shallow comprehension.
