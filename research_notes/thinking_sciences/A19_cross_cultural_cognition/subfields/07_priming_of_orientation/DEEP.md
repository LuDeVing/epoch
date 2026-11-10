# Priming of orientation: deep document

*Subfield A19.07, cross-cultural cognition. Built from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, c02, d03 ...) point to those files. "Opened" means the page or PDF text was read in this series. The founding human papers (Trafimow 1991, Gardner 1999, Kuhnen and Oyserman 2002, Hong 2000) were NOT opened and are known only second-hand.*

## 1. What it is

Priming of orientation means a short cue that pushes a person toward an independent self view (I, unique, free) or an interdependent self view (we, relations, duty). The hope is that later judgments then lean analytic (parts, rules, objects) or holistic (relations, context, change). The cue can be a pronoun-circling task, a story, a scrambled sentence, a "what makes you different from or similar to family and friends" essay, a language, a culture icon, or a group activity.

Why we care: our agent is one language model run through a scaffold, not a trained model. If a cue can switch the model's framing, a cheap prefix could change how it reasons. The human evidence says the average effect is small, much of it is inflated, and it depends on task, sex, baseline and whether the person followed the cue. The LLM evidence says persona and language cues move survey values and some style readouts. No study tests a human-style priming task ahead of a reasoning benchmark and measures accuracy (K16, single-source, weak absence check).

Short verdict: treat an orientation cue as a zero-effect hypothesis until a per-model, per-item-family test at equal tokens says otherwise. The one part worth building now is a check that compares the cued answer with a reference and reverts if worse (K08, K19). That is a general guardrail, not a cultural one.

## 2. History and theories in depth

**Culture as a stable trait.** Early work (Markus and Kitayama style self-construal; Nisbett style analytic versus holistic cognition) treated orientation as a durable property of a person from a culture. Trafimow, Triandis and Goto (1991) showed that the private and collective self can be made accessible by instruction (b06, only described second-hand in b03). The Sumerian warrior story and the "similarities versus differences with family and friends" task (SDFF) come from this period (a06: Study 1 SDFF, Study 2 Sumerian warrior; the warrior text was reused in 12 later studies, SDFF in 10).

**Culture as situated cognition.** Oyserman's account (a02, a03) says people hold both mindsets. A cue makes one accessible and it then guides interpretation of the next task. Priming is the main evidence: if a short cue works, the mindset was there all along and is switchable. Hong, Morris, Chiu and Benet-Martinez (2000), "multicultural minds", showed bicultural people giving more internal attributions after American icons and more external after Chinese icons (a10, b24; abstract only, numbers not read).

**Lexical and story primes.** Brewer and Gardner (1996) and Gardner, Gabriel and Lee (1999) introduced pronoun circling (I/me/mine versus we/us/ours in a short paragraph). It was used in 15 studies in the meta-analysis (a07). Kuhnen and Oyserman (2002) used the circling prime and then a spatial memory task: independent primes lead to better memory for objects, interdependent primes to better memory for object locations (a09, a21; numbers not read).

**Meta-analysis, 2008.** Oyserman and Lee pooled 67 studies and 369 effect sizes (c01). It is the field's reference number and the source cited by Varnum et al. It also contains its own warning: trim-and-fill halves the effect (c02).

**Replication era, 2017 on.** Mesoudi, Magid and Sarkol (2017) found no effect of solitary versus collective activity (a19, b09). A pre-registered close replication of Kuhnen and Oyserman Study 2 found an effect only among full compliers (d01-d04). Lin and Wu (2021) ran a large pre-registered test of the Gardner et al. primes and got a clean null (b03). Kvarven, Stromland and Johannesson (2020) found meta-analyses average about three times larger than pre-registered replications (b08, second-hand).

**LLM era, 2023 on.** Work moved to "cultural prompting": a one-line persona or a language switch. It is scored on survey values (Tao et al. 2024; Luther and Brown 2025; Eren et al. 2026), on style tests (Jin et al. 2023; Lu, Song and Zhang 2025; Sun and Wang 2025; Hu et al. 2026), and, for generic role prompts, on reasoning accuracy (Kong 2023; Zheng 2023; Lee 2024). Nobody ran the human priming tasks themselves as a prefix.

**Competing explanations for human priming effects.**
- Accessibility: the cue makes a self-construal chunk easy to retrieve (Oyserman). Predicts short-lived, task-matched effects.
- Demand and compliance: people guess what is wanted. The compliance gradient in d02 supports a role for attention and uptake. It could also be a selection artefact.
- Baseline moderation: the cue only helps people low on the target trait (b12, post hoc, N 36 per experiment).
- Publication bias and low power: original N about 75-90 per cell gave 5-12% power for the replication effect sizes (b04). Trim-and-fill d 0.17 (c02).
- For LLMs: stereotype retrieval and deference to a claimed identity (b16, b17, a13), plus plain instruction following (K11, K20).

## 3. Core findings with exact numbers

Status key: established = two or more independent sources agree or replicated; single = one source; contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Average human priming effect | 67 studies, 369 effect sizes, N 6,240. Weighted d 0.34 (CI 0.29-0.39), unweighted 0.45. Without 3 anomalous studies (64 studies, N 5,408) d 0.42 (CI 0.37-0.48). Fail-safe N 3,495 | Oyserman and Lee 2008 (c01) | single source, a meta-analysis |
| The average is inflated | Trim-and-fill adjusted weighted d 0.17 (CI 0.12-0.21), 24 studies imputed. Meta-analyses about 3x preregistered replications in general | c02, b08 | established |
| Outcome type | Relationality 0.61, cognition 0.54, values 0.29, self-concept 0.26, well-being near zero. Cognition sub-types: social attitudes 0.50, social comparison 0.59, nonsocial judgment 0.52 | c03 | single |
| Prime type | SDFF 0.49 (n=10); scrambled sentence 0.45 (CI 0.30-0.61); group imagination 0.32; Sumerian warrior about 0.45 (unconfirmed, garbled table). Q_B 47.48, p<.001. Priming both relational and group collectivism 0.52 (n=22) vs group only 0.28 (n=11) vs relational only 0.39 (n=28) | c02, critique item 2 | single |
| Language as prime | About 0.10 on values (10 studies), no effect on value scales; 0.17 in Asian samples. In the East 40% of studies used language as the prime and 60% group-level primes, so region and prime type are confounded | a27, c03 | single |
| Pronoun circling fails a large preregistered test | N 468 (78 per cell, 6 cells); self-description F(2,462)=0.283, p=.754, BF01 about 32. 80% power for d 0.45. Original Exp 1 (N 90) had 5.1% power for the replication TST effect, 5.0% values, 5.6% desirability, 8.1% obligation, 12.2% punishment | Lin and Wu 2021 (b03, b04) | single, hardest evidence against |
| Delivery is not uptake | 92.7% counted target words correctly; all said they answered seriously; no downstream shift | b23 | single |
| Pronoun prime works for compliers on spatial recall | Close replication of Kuhnen and Oyserman Study 2. Full compliers N 87: object recall 44.60 vs 54.38%, t(84.93)=2.31, p=.028, d .50; location d .52; both d .47. Partial N 157: d .26-.30 (p .073-.108). No filter N 193: d .10-.15, all p>.25. Adding back inattentive people: p .063 and .052. Pooled close replications d .35 (median .37), three labs only | OSF preprint 2017 (d01-d04) | single, cut-off not preregistered |
| Activity primes fail | Exp 1 N 82 (41 per cell), no time x activity interaction on any of 7 measures; Exp 2 N 132, one of 7 measures moved, wrong direction, not significant at Bonferroni .007 | Mesoudi, Magid, Sarkol 2017 (b09) | single |
| Task-specific, conditional effects | Faces: Exp 1A N 109 no effect (p>.19); Exp 1B N 27, F(2,52)=3.33, p=.04, partial eta2 .11; no effect on recognition. Fairness game: women only, 33.3% rejected after interdependent prime vs 62.5% independent (Wald 7.31, p=.007), N 226; direction reversed in men in later studies. Self-bias: effect only in low-baseline subgroup, N 36 + 36, overall prime effect F(1,30)=1.54, p=.23 | b10, b11, b12 | established as a pattern (4+ studies); each effect small and fragile |
| LLM persona cue on values | 107 countries. Share improved: GPT-4o 71.0%, GPT-4-turbo 81.3%, GPT-4 77.6%, GPT-3.5-turbo 72.6%, GPT-3 80.4%. Mean distance GPT-4o 2.42 to 1.57, GPT-4-turbo 2.71 to 1.77, GPT-4 2.69 to 1.65 (all P<.001), GPT-3 2.39 to 2.11, GPT-3.5-turbo 3.35 to 2.83. Jordan 4.10 to 0.36 | Tao et al. 2024 (a11, b13, c14) | established (replicated in 5 open models) |
| Gain grows with model strength | Distance gain GPT-4 1.04, GPT-4-turbo 0.94, GPT-4o 0.85, GPT-3.5 0.52, GPT-3 0.28 | b14 | single (derived from reported means) |
| Cue backfires | Taiwan 2.40 to 3.94; another country 0.45 to 2.48; 19-29% of targets get worse. Luther and Brown: Llama 3.1 worse in total distance, France and Iran worse; exact percentages unreliable (column-shifted table) | c15, c18, critique item 6 | established |
| Open-model replication | Mean distance no cue to manual cue: llama3.3 70B 2.217 to 0.973; llama4 2.819 to 2.006; gemma3 27B 3.085 to 2.008; gpt-oss 20B 2.789 to 1.688. DSPy-optimised cue: llama4 0.818, gemma3 1.499; worse than manual on llama3.3 (1.350-1.496 vs 0.973) | Eren et al. 2026 (c19, c20) | single group, overlaps Tao design |
| Reasoning-first cue | Egypt, GPT-3.5: soft similarity 0.4834 to 0.5102, hard 0.2443 to 0.2838 with anthropological prompting vs vanilla persona | AlKhamissi et al. 2024 (a15, c16) | single |
| Persona gives stereotypes | All models rate US individualist, Japan collectivist; Command-R 72.40% individualist answers for the US persona; only one model-method cell correlated with country value (GPT-4o, individualism). Advice to Nigeria-origin users misaligned +1.85 on a 1-5 scale (overall +0.76, n=840, t=15.65) | Kharchenko 2025 (b16); Jeripity Venkata 2026 (b17) | established (3 sources) |
| Language switch on LLM style | Lu et al. (Nature Hum Behav 2025): GPT-4 and ERNIE show holistic/interdependent shifts in Chinese (abstract and press only; effect sizes unread). Sun and Wang replication, 8 models, 960 observations: language d 0.045 (p .15); Chinese-origin model d 0.169 (p .0089); qwen d 0.54 in one task; signs mixed | b18, c06, c09, c10 | contested |
| Explicit framing beats culture label | Change-framed vs neutral prompt d 2.095, eta2 0.5423, all 8 models; language d 0.045. Partly a demand effect | Sun and Wang (c09) | single |
| Language and image outputs | Objects in generated images Chinese 10.71 (SD 4.70) vs English 8.91 (SD 2.26), t(286)=4.88, d .49; scene description reversed, English 10.90 vs Chinese 10.06, d .36; collective attribution Chinese-origin model 3.17 vs US 2.81 | Hu et al. 2026 (b19, c12, c13) | single |
| Default LLM style is mixed | Triadic categorisation 0.87 (GPT-3.5, SD .06), 0.85 (GPT-4, SD .05); AHS 5.35 and 5.01 vs human 4.87; Independent self-construal 6.98 and 5.32 vs norm 4.73; dialectical self for GPT-4 not different (p .344). 10 runs per setting at T=1 | Jin et al. 2023 (b20, c04); Cao 2023 (a13) | established |
| Persona prefix on accuracy: net zero, item-level churn | AQuA with role persona: 15.75% items wrong-to-right, 13.78% right-to-wrong; Coin Flip 4.00% gained, 18.00% lost. 162 roles, 4 families, 2,410 factual questions: no mean gain | Lee et al. 2024 (d07); Zheng et al. 2023 (d11) | established |
| Pick-between rescue | GPT-4 six arithmetic sets 91.06 base, 92.28 persona, 93.15 Jekyll and Hyde; llama3-8B 81.47, 82.32, 84.23; on six sets where persona was below base, 74.49 persona vs 76.38 | Lee et al. 2024 (d08, d09) | single |
| Role-play can help on some tasks | Kong 2023: AQuA 53.5 to 63.8%, Last Letter 23.8 to 84.2% (abstract only); GPT-4 Coin Flip 66.93 to 75.93 | d10, d09 | contested against Zheng and Lee |
| Self-report is not behaviour | Small-model Singelis scores did not predict multi-turn behaviour in a blog pilot (12 scenarios) | c22 | single, weak (not peer reviewed) |
| Content interacts with cue | VLM holistic share 26.10% (COCO) to 73.37% (Japanese 1K images) for GPT-4o-JP | Sabir et al. 2025 (b21) | single |

## 4. Mechanisms and models

No formal computational model of orientation priming exists in the sources opened (a28). What follows is an engineering reading of the proposals, with status.

**M1. Accessibility with decay (human theory).** State: two self-construal schemas with activation a_I and a_D. A cue adds activation to one. Activation decays over minutes. A later task reads whichever schema is more active if the task is ambiguous enough to need one. Result: small, short, task-matched effects. For an LLM, context is the only state. A prefix does not decay, but it competes with every later token. The LLM analogue of decay is distance in context and instruction override. Assume the prefix loses to a task instruction.

**M2. Uptake gating.** Effect = cue x uptake. In d02 the effect rose from d .10-.15 (no filter) to .26-.30 (partial) to .47-.52 (full). Implement: log whether the output shows the cue was used (names relations when asked to; refers to the group). Report cue effect on all runs as primary, on obeying runs as secondary. Selection on a post-treatment variable breaks randomisation.

**M3. Moderation by baseline.** Cue effect = f(baseline). Human evidence is one post hoc split (b12). For LLMs, baseline differs by model (K21: DeepSeek downplays self-enhancement relative to ChatGPT and Gemini, d16), but nobody has regressed cue gain on baseline. Implement: measure baseline on a fixed battery; fit gain against baseline per model.

**M4. Persona as stereotype retrieval plus deference.** A one-line country cue retrieves a stereotype profile. On average it is closer to survey means than the default American-leaning profile (default distance to US: DeepSeek V3.1 52.13 up to Opus 4 114.19, c17). But it ranks countries by stereotype, not by true score (b16). Where the stereotype is wrong, distance rises (Taiwan, Finland, France, Iran). A second path is sycophancy to a claimed identity (K20, open): assistants favour answers matching a user's views (Sharma 2023, d13), and warm-tuned models validate false beliefs 10-30 points more (d14). To separate the paths, compare identity cue, task cue and neutral.

**M5. Explicit framing as instruction.** "Consider what may change" produced d 2.1 because it tells the model the answer type (c09). It is a task instruction, not a prime. It is the strongest lever in the evidence and the least interesting scientifically.

**M6. Check-and-revert wrapper (applicable now).** Procedure: (1) answer without the cue; (2) answer with the cue; (3) compare both against a reference and pick. Lee et al. used a position-bias-free judge (d07-d09). In our schema the judge should be code where a check exists (G5), and agreement or a held-out test where not. Cost: two calls. Effect: backfire becomes a bounded loss.

## 5. What holds up

**Replications and failures (human).**
- Lin and Wu 2021: clean null on self-description, BF01 about 32, on the most-used prime (15 studies in the meta-analysis). Power of the originals for those effects 5-12%.
- Close replication of the spatial-memory result: holds only among full compliers; with everyone, p>.25. Pooled close replications d .35 from three labs is optimistic (compliance cut-offs, few labs).
- Activity primes (alone versus together): null on 7 measures in two experiments (N 82, 132).
- Moderated effects: women only (fairness), low baseline only (self-bias), within-task only (faces). The pattern across b10, b11, b12, a24, a25 is established. Any single effect is fragile (cells of 9 to 76).

**Meta-analysis caveats.** Weighted d 0.34 falls to 0.17 under trim-and-fill. Samples are almost all undergraduates. 36 of 67 studies were in the US. Only about a third had gender in the design (a03). Most studies lacked a control condition (K02). Cognition outcomes mix social and nonsocial tasks, so the pooled "cognition" d 0.54 is not a pure analytic versus holistic test (c03).

**Moderators that appear in more than one source.** Prime richness (content primes beat language), prime level (priming both relational and group collectivism, 0.52, beats either alone), outcome type (relationality and cognition above values and self-concept), sex (fairness game), baseline, and compliance.

**Interventions that worked.** In humans: SDFF and scrambled sentences on average (d about 0.45-0.49 before bias correction), and the pronoun prime among full compliers. In LLMs: a country persona on values (distance down in 71-81% of 107 countries, replicated in five open models); reasoning-first cues modestly (a15); optimised cue text on some models (c20); a choose-between step after persona (d08, d09).

**Interventions that did not work.** Language alone as a prime (human d about 0.10 on values; in LLMs d 0.045 across 8 models). Activity primes. Pronoun circling at scale in a Chinese sample. Persona prefixes on factual accuracy (162 roles, no mean gain). Persona on every target (19-29% got worse).

**Where evidence is thin.** Founding papers not opened. Lu et al. effect sizes unread. Magid et al. numbers rest on two readers. Eren et al. overlaps Tao's design and is not an independent replication. The EA Forum pilot (c22) is a blog.

## 6. Language models

**Baselines.** GPT-3.5 and GPT-4 lean holistic on process scales: triadic categorisation 0.87 and 0.85, AHS 5.35 and 5.01 against human 4.87 (b20, c04). They lean independent on self-construal scales (Independent 6.98 and 5.32 against norm 4.73). Both can be true (critique item 8). Those t-tests use 10 runs against human norms, so p-values overstate. Models differ by origin: Chinese-origin models differ by d 0.169 on the stability task (c09) and score 3.17 vs 2.81 on collective attribution (d 1.14, c13).

**Persona cues on values.** Tao et al.: mean distance to survey ground truth falls 0.28 (GPT-3) to 1.04 (GPT-4). Improvement in 71-81% of countries, worse in the rest. Luther and Brown, five frontier models: mean total distance about 1,027.74 to 892; Llama 3.1 worse; only the direction is reliable. Eren et al.: five open models improve, e.g. llama3.3 70B 2.217 to 0.973. Newer, larger models gain more (b14), yet default distance remains large for some.

**Cue text matters.** Anthropological prompting (emic and etic reasoning, then answer) beat vanilla persona by +0.027 soft and +0.040 hard similarity (Egypt, GPT-3.5, a15). Optimised cues beat manual on some models and lost on others (c20).

**Language as cue.** Lu et al. report shifts in GPT-4 and ERNIE (100 iterations per language per measure; medium to large per press report c06; items unreleased). Sun and Wang: 8 models, 30-60 items per condition, language d 0.045; on norms and attribution qwen d 0.54, ernie -0.171, gpt -0.190; most models null. Negru et al. 2026: significant language differences only for GPT on UAI and LTO and DeepSeek on PDI and LTO (b22). Hu et al.: Chinese prompts raised object counts (d .49) but reversed on scene description (d .36). Net: contested; likely small, task-specific and model-specific.

**Framing and demand.** An explicit "change" framing gave |d| 2.1 on all 8 models. That is instruction following. The same lens applies to persona: a stated identity is both a retrieval cue and a claim to defer to (K20, open).

**Persona on accuracy.** Role prompts do not raise mean accuracy across 162 roles and 2,410 questions (d11). Within a model, a role flips as many items to wrong as to right (AQuA 15.75% vs 13.78%; Coin Flip 4.00% vs 18.00%, d07). A choose-between step recovered +0.87 (GPT-4) and +1.91 (llama3-8B) points on average, and +1.89 on the six sets where persona hurt (d08, d09). Kong et al. (abstract only) report large role-play gains on AQuA and Last Letter, so the effect is task-specific.

**Style versus behaviour.** Self-report scores did not predict behaviour in a small multi-turn pilot (c22). Advice to users from collectivist countries stays individualist even when the country is stated (b17: +0.76 mean misalignment). Claude moves with language, GPT-5.4 follows the stated country only, Gemini goes the other way.

**Not found.** No LLM study uses SDFF, pronoun circling, scrambled sentences or the warrior story as a prefix before a reasoning task and scores accuracy (K16; Crossref only, other search APIs were rate-limited). No study of baseline moderating cue gain in LLMs (K21).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Expected cue gain is calibrated to near zero (G7 note).** Any orientation, persona or language prefix is a zero-effect hypothesis until it beats a pre-registered minimum (about 2 accuracy points) at equal tokens, per item family and per model. [E] K02, K18; evidence c02, b08, d09, d11, b03. Schema part: G7, no new element.
2. **Report cue effect per item family, never pooled (G7 evaluation rule).** Human effects flipped by task, sex and baseline; persona flips items both ways. [E] K05, K08; b10, b11, b12, d07.
3. **Check the cued answer against a reference and revert if worse (G, S4/S8).** Backfire is established (19-29% of targets worse, c15, c18; item churn d07). The pick-between gain itself (+0.87 to +1.91 average points) is [S] K19, d08, d09. Where code can check, code selects (G5). This only adds "cued versus uncued" as a comparison pair in existing steps.
4. **Measure the agent's default style before adding any cue (S0 gate record).** [E] K13; b20, c04, a13.
5. **A claimed identity in the task text must not change method (G, anti-sycophancy; S1 input hygiene).** Persona cues give stereotypes, not calibrated profiles. [E] K09; b16, b17, a13.
6. **Score the answer, not the model's description of its own style (extension of G10).** [S] K14; c22, b23. Low risk because it follows G10.

### Test first

| Item | Schema part | Status | Evidence | Test |
|---|---|---|---|---|
| SDFF-style or pronoun prefix ahead of a reasoning item | O1-O8 framing, S1 | [C] K03, [S] K16 | a28, b03, d01-d04 | U1 |
| Task-reflection cue versus language switch versus label | O8 wording | [S] K06 | c02, a05, a27 | U2 |
| Emic and etic then answer, versus bare persona | O8 wording | [S] K12 | a15, c16, c20 | U3 |
| Explicit "consider what may change" instruction versus identity cue | O8 / S1 | [S] K11 | c09, a17 | U4 |
| Cued versus neutral then pick (code or held-out) | S8 | [S] K19 | d08, d09 | U5 |
| Uptake logging and gated analysis | G / bench | [S] K17 | d01-d04 | U6 |
| Baseline as moderator of cue gain | S0 gate | open K21 | b12, d16 | U7 |
| Identity cue versus task cue versus neutral (demand) | G anti-sycophancy | open K20 | d13, d14 | U8 |
| Language switch on orientation items | none | [C] K10 | a16, a17, b22, b19 | U9 |
| Activity-style cue (do a worked sub-task) versus label cue | S3 | [S] K04 | a19, b09 | U10 |

The U-ids refer to UNKNOWNS.md (A19.07-U1 and so on).

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (the control arm gets a length-matched neutral filler or extra sampling), at least 3 models (one strong, one mid, one open), items grouped by family, three seeds, fixed temperature.

1. **Prefix prime on reasoning.** Items: 150 holistic-sensitive items (relational analogies, object-versus-relation tasks, social-attribution items with a keyed answer) plus 150 analytic items (rule application, counting). Arms: SDFF-style reflection (about 80 tokens); pronoun-circling-style we/I paragraph; length-matched neutral paragraph; none. Metric: accuracy per family, paired by item, plus flip counts (right-to-wrong, wrong-to-right). Expected: |effect| under 2 points, flips roughly balanced (as in d07). The human d .35 would be about 3-5 points; we do not expect it.
2. **Cue wording.** Same 300 items. Arms: task-reflection cue; language switch (translated prompt); neutral label ("holistic thinker"); none. Metric: accuracy, plus a blind code readout of relations named. Expected: task-reflection at most small; language near zero.
3. **Reasoning-first cue.** Arms: persona alone; "reason as an anthropologist about this culture, then answer"; none. Metric: distance to survey truth on 40 held-out countries, and accuracy on the reasoning set. Expected: +0.02 to +0.04 similarity, no reasoning gain.
4. **Framing instruction versus identity cue.** Arms: "the answer may involve change"; "you are an East Asian person"; neutral. Items: attribution and change-expectation items with a keyed answer, including items where change is the wrong answer. Metric: accuracy and share of answers shifted toward the cued option. Expected: instruction large on matching items and a drop on mismatched ones (demand); identity cue small.
5. **Check-and-revert.** Arms: cued only; neutral only; cued then pick (code or held-out where available, a second model otherwise); best-of-two plain sampling as a control at matched calls. Metric: accuracy. Expected: pick beats the best single arm by 1-2 points. It fails if it does not beat plain best-of-two.
6. **Uptake gating.** Log obedience (key-term list or regex) per run. Report all runs as primary, obeying runs second. Expected: obeying runs show more effect, with the caveat that this may be selection.
7. **Baseline moderation.** Measure baseline on 60 items per model; regress cue gain on baseline across at least 6 models. Expected: weak slope. A null is informative.
8. **Demand separation.** Three arms on holistic items: identity claim, task cue, neutral. Add a false identity claim ("I am a farmer from Japan") when task evidence favours the other answer. Check whether answers follow the claim against the evidence.

## 9. What does not transfer, and why

- **Human accessibility and decay.** A person's self-concept is long-lived and a prime adds a transient bump. A model has no self-concept; the prefix is just context. M1 has no clean analogue.
- **Human effect sizes.** d 0.34 (0.17 corrected) came from undergraduates answering a task minutes after a prime. Noise, demand and compliance differ in LLMs. The prior for the agent is near zero, not 0.34.
- **Value-survey gains.** The established LLM result is on values. Our agent solves reasoning items. Distance to a survey mean says nothing about accuracy (K07 is values only; K18 shows persona gives no mean accuracy gain).
- **Language switch.** Contested in LLMs and confounded with training data, translation quality and item set. It also needs translation of every prompt.
- **Activity primes.** Humans did a game together or alone. An agent doing a sub-task is not a collective activity. Humans did not show transfer either.
- **Compliance filtering.** Filtering runs by whether the model followed the cue is selection on outcome. Use it as a diagnostic only.
- **Cultural categories as a goal.** The agent does not need to be "East Asian". Its job is answer quality (G7). Stereotype profiles are the failure mode (K09).

## 10. Open questions

- Do human-style priming tasks as prefixes move accuracy on any reasoning benchmark? Nobody has tested it (K16).
- Is persona gain on values mostly stereotype retrieval, instruction following or sycophancy (K20)?
- Does baseline style moderate cue gain in LLMs as in humans (K21)?
- Does the Lu et al. language effect survive with released items and the full model panel? Full text and items were not retrieved.
- What is the true human effect? Founding papers not opened; the pooled replication count is three labs.
- Do cue effects hold across multi-turn agent loops, or only single-shot answers? The c22 pilot is weak.
- Is the +1 to +2 point gain from pick-between larger than best-of-two sampling at equal calls (K19)?
- Do reasoning models with long chains of thought wash out a prefix cue?

## 11. Sources

[V] opened and read in this series; [M] snippet or abstract only (as marked in the evidence files). Evidence ids in brackets.

- [V] Oyserman and Lee (2008) Does culture influence what and how we think? Psychological Bulletin 134(2), 311: https://doi.org/10.1037/0033-2909.134.2.311 (author-site PDF under https://dornsife.usc.edu/daphna-oyserman/ , path as recorded in c01) [b01, b02, c01-c03]
- [M] Oyserman and Lee (2008) abstract, Europe PMC: https://europepmc.org/article/MED/18298274 [a01]
- [V] Oyserman (2007) Priming culture: culture as situated cognition, handbook chapter: https://dornsife.usc.edu/daphna-oyserman/wp-content/uploads/sites/232/2023/12/ [a02-a08, a26-a28]
- [M] Kuhnen and Oyserman (2002): https://doi.org/10.1016/S0022-1031(02)00500-6 [a09, c26]
- [M] Hong, Morris, Chiu and Benet-Martinez (2000) Multicultural minds: https://doi.org/10.1037/0003-066X.55.7.709 [a10, b24]
- [M] Gardner, Gabriel and Lee (1999): https://www.kellogg.northwestern.edu/academics-research/research/detail/1999/i-v [b07, c24]
- [M] Brewer and Gardner (1996); Trafimow, Triandis and Goto (1991); Kvarven et al. (2020), known only through Lin and Wu: https://osf.io/u5dxn/ [b05, b06, b08]
- [V] Lin and Wu (2021) Self-construal priming does not shift self-descriptions, values, ...: https://osf.io/u5dxn/ [b03, b04, b23]
- [M] Wu replication talk abstract: https://gbaysforum.psy.cuhk.edu.hk/wp-content/uploads/2021/10/CUHKSZ_Yichen-Wu.p [c25]
- [V] OSF preprint 2017, close replication of Kuhnen and Oyserman Study 2: https://osf.io/t34kf_v1 [d01-d04]
- [V] Mesoudi, Magid and Sarkol (2017) Experimental priming of independent and interdependent activity: https://royalsocietypublishing.org/doi/10.1098/rsos.161025 [a19, b09, b26]
- [V] Liu, Liang, Feng and Zhou (2019) faces: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6718463/ [a22, b10]
- [V] Mishra and Bost (2018): https://europepmc.org/article/PMC/PMC6266528 [a23]
- [V] Gender moderates fairness priming (2017): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5376594/ [b11]
- [V] Jiang and Sui (2022) Bicultural minds: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8869382/ [a24, b12]
- [M] Self-construal priming under social threat (2017): https://europepmc.org/article/PMC/PMC5645819 [a25]
- [V] Language Log note on priming methods: https://languagelog.ldc.upenn.edu/nll/?p=485 [b25, c28]
- [V] Tao, Viberg, Baker and Kizilcec (2024): https://arxiv.org/abs/2311.14096 [a11, a12, b13, b14, c14, c15]
- [V] Cao et al. (2023): https://arxiv.org/abs/2303.17466 [a13]
- [V] Kharchenko, Roosta, Chadha and Shah (2025): https://arxiv.org/abs/2406.14805 [a14, b16]
- [V] AlKhamissi, ElSherief, Nahas and Diab (2024): https://arxiv.org/abs/2402.13231 [a15, c16]
- [M] Lu, Song and Zhang (2025) Nature Human Behaviour: https://doi.org/10.1038/s41562-025-02242-1 [a16, b18, d05]; [V] press report: https://www.psypost.org/a-simple-language-switch-can-make-ai-models-behave-signi [c06, c07]
- [V] Sun and Wang (2025): https://arxiv.org/abs/2510.05869 [a17, a18, c08-c10]
- [V] Luther and Brown (2025): https://arxiv.org/abs/2512.12488 [b15, c17, c18]
- [V] Jeripity Venkata (2026): https://arxiv.org/abs/2604.22153 [b17]
- [V] Hu et al. (2026): https://arxiv.org/abs/2601.17096 [b19, c11-c13, c23]
- [V] Jin, Zhang, Shu and Cui (2023): https://arxiv.org/abs/2308.14242 [b20, c04, c05]
- [V] Sabir, Gasper, Loem and Sharma (2025): https://arxiv.org/abs/2507.00700 [b21, c21]
- [V] Negru, Lemnaru, Surdeanu and Potolea (2026): https://arxiv.org/abs/2602.12878 [b22]
- [V] Eren, Michalak, Cook and Seales (2026): https://arxiv.org/pdf/2603.16827 [c19, c20]
- [V] EA Forum pilot, LLM culture shock (2026): https://forum-bots.effectivealtruism.org/posts/v949YTQ4oEaqh8dr9/llm-culture-sho [c22]
- [M] Wagner (2025) EDULEARN: https://library.iated.org/view/WAGNER2025CUL [c27]
- [M] Yang et al. (2026) persona prompting: https://aclanthology.org/2026.eacl-long.52 [d06]
- [V] Lee et al. (2024) Persona is a double-edged sword: https://arxiv.org/abs/2408.08631 [d07-d09]
- [M] Kong et al. (2023): https://arxiv.org/abs/2308.07702 [d10]
- [M] Zheng et al. (2023): https://arxiv.org/abs/2311.10054 [d11]
- [M] Hu and Collier (2024): https://arxiv.org/abs/2402.10811 [d12]
- [M] Sharma et al. (2023): https://arxiv.org/abs/2310.13548 [d13]
- [M] Warm-tuned models reduce accuracy and increase sycophancy (2026): https://doi.org/10.1038/s41586-026-10410-0 [d14]
- [M] Cultural norm-based alignment, AAAI 2026: https://doi.org/10.1609/aaai.v40i21.38839 [d15]
- [V] Schwartz values in Gemini, ChatGPT and DeepSeek: https://osf.io/bmkzw_v1 [d16]
- [V] Gap-pass search note (Crossref): https://api.crossref.org/works [d17]
