# Categorisation and attention: deep document

*Subfield A19.04. Rules and taxonomy vs relations and thematic groups; focal vs context-sensitive attention. Key work: Nisbett, Peng, Choi and Norenzayan 2001. Relevance to our agent: background only. Evidence ids (a01 to d19) are in evidence_a-d.jsonl; claim ids (A19.04-K01 to K25) are in claims.jsonl; checks are in critique.md. Date of last check: 2026-11-20.*

## 1. What it is

Nisbett and colleagues (2001) argued that East Asians and Westerners differ in two linked habits.

- **Attention.** East Asians (interdependent social life, complex visual fields) attend to the whole field: background, context, relations between things. Westerners (independent social life, object-centred ecology) attend to the focal object and its attributes.
- **Categorisation and reasoning.** Westerners sort things by taxonomy and apply formal rules. East Asians sort by relations and thematic links ("the cow eats the grass") and by overall family resemblance.

The theory says these two habits come from one cause: what you attend to decides what you can reason about. If the field is salient, relations are the natural basis for grouping. If the object is salient, category membership is.

Paradigms used to test it:

1. **Triad grouping.** Three items, pick the two that go together, say why. One pair is a relation pair (cow, grass); one is a taxonomic pair (cow, chicken). Chiu 1972 with children; Ji and Nisbett 2000 with adults.
2. **Rule vs family resemblance.** A target sits beside two groups. One group matches by overall resemblance; the other shares one rule (Norenzayan et al. 2002).
3. **Rule-based category learning with conflict.** Allen and Brooks paradigm: cartoon animals, a rule, and exemplars that disagree with the rule.
4. **Induction and typicality.** Category-based arguments (Choi, Nisbett and Smith 1997; Norenzayan, Choi and Nisbett 2000).
5. **Scene memory.** Free recall of animated underwater scenes (Masuda and Nisbett 2001).
6. **Change blindness.** Flicker and animated vignettes with focal or context changes (Masuda and Nisbett 2006).
7. **Eye tracking on scenes.** First fixation on the object, time on object vs background (Chua et al. 2005).
8. **Perceptual tasks.** Framed line test, rod and frame, Navon letters, embedded figures.

Why this is in our research set. Our agent is one language model run through a scaffold. This subfield matters in two ways. First, as a possible source of operators (change representation, O6; map an analogue, O7). Second, and more usefully, as a warning: a large, well-known "style" effect in humans turned out to depend on wording, stimuli, and sample, and the LLM follow-ups show the same fragility. The honest summary is "background only". Nothing here earns a new operator (SCHEMA section 4b).

## 2. History and theories in depth

**Precursors.** Witkin's field dependence (rod and frame) gave the first "context vs object" measure. Kemler-Nelson (1984) and Allen and Brooks (1991) gave the rule vs resemblance paradigms. Chiu (1972) ran the first cross-cultural triad task: American children paired by shared category or feature, Chinese children by relation. Example (a02, a03): man, woman, child. Chinese children grouped woman and child ("the mother takes care of the baby"); Americans grouped man and woman ("both are adults"). Another: chicken, cow, grass. Americans chose chicken and cow ("both animals"); Chinese chose cow and grass ("the cow eats the grass"). The 2001 review gives no counts for Chiu, so the size of that founding effect is unknown from our reading.

**1997 to 2002: the experimental programme.**
- Choi, Nisbett and Smith (1997), as reported (a07, b15): Koreans used category coverage less than Americans in induction, unless the conclusion named the category ("mammals"). Naming it moved Koreans and not Americans. A salient cue switches the taxonomic mode on.
- Ji and Nisbett (2000), as reported (a04): adult Chinese chose relation pairs (pencil, notebook; sky, sunshine) more, Americans category pairs. Percentages not in the review. Ji, Zhang and Nisbett (2004) added a language control (bilingual Chinese grouped more by relation in Chinese than in English); it was not opened (a20).
- Norenzayan, Choi and Nisbett (2000) (a08): Koreans showed a large typicality effect in argument convincingness; making typicality salient made all groups show it. This supports "preference, not ability".
- Norenzayan, Smith, Kim and Nisbett (2002): four studies, details in section 3.
- Masuda and Nisbett (2001): scene recall. Japanese gave about 70% more background statements and about 100% more relation statements than Americans; focal-fish mentions were equal. The figure varies by telling: 65% (PNAS 2003 review), more than 60% (2006 paper), 70% (2001 review, handbook chapter). N is not in any of the reviews we read.
- Masuda and Nisbett (2006): change blindness, three experiments.
- Chua, Boland and Nisbett (2005): eye tracking, N=45.

**Origin account.** Nisbett et al. proposed that Greek individualism and debate vs Chinese collectivism and harmony produced the two styles. That origin story is speculative and was never tested by the work above (b14). Later work offered alternatives: ecology and subsistence (farmers and fishers are more holistic than herders, Uskul et al. 2008; listing only, d19), the physical scene (Miyamoto, Nisbett and Masuda: Japanese town scenes had more objects and were more complex, and priming with them made both groups detect more context changes; a15), and infant differences (15-month-old Japanese infants looked at backgrounds about twice as long in cartoons; Carlson et al. 2025, b12).

**2005 to 2011: failures at the eye level.** Rayner et al. 2007 and 2009 and Evans et al. 2009 failed to reproduce the eye-tracking result (section 5). Unsworth and Medin (2005) reduced the belief-bias claim to response bias (b04).

**2009: Rosetta project.** Klein et al. (2009) ran six analytic-holistic measures in Japan, Korea, Taiwan and the US (N=379). Choices in categorisation did not differ; only response time did (b08, b09).

**2018 to 2025: large replications.** Many Labs 2 (N=7,396) replicated the wording effect from Norenzayan 2002 Study 2 but not the cultural moderation (b05, b06). Lacko et al. (2025; N=993, 11 countries) found cultural differences in Navon and embedded-figures tasks but not along East-West (b10). A 2025 seven-sample eye-tracking study found the same (b11). A 2026 study of Korean, US and Chinese children found relational bias fades in adults (b13).

**2023 to 2026: the LLM turn.** Jin et al. (2023) gave GPT-3.5 and GPT-4 the Analysis-Holism Scale and a triad task and called them holistic. Lu, Song and Zhang (2025, Nature Human Behaviour) said GPT and ERNIE are more holistic in Chinese than English. Sun and Wang (2025) and Hu et al. (2026) did not reproduce a language effect. Sabir et al. (2025) measured holistic captions in VLMs. Section 6 has numbers.

**Where the field stands.** The big picture: the "two styles on an East-West axis" idea is weak. What survives is smaller and more local: instruction wording moves category strategy strongly; some scene and task effects exist in some samples; the rest is contested.

## 3. Core findings with exact numbers

Status key: replicated (confirmed by independent work), partial, contested, single-source, refuted. "Opened" evidence means we read the text this session.

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Wording flips rule vs resemblance: "belongs to" gives more rule answers than "similar to" | Original: belong-to rule 67% vs 33%, F(1,100)=44.40, p<.001. Many Labs 2: N=7,396, rule 64% (SD 25) vs 44% (SD 21), t(7,227.6)=37.05, d=0.86, 95% CI [0.81, 0.91] | Norenzayan 2002 Study 2; Klein 2018 (b02, b05) | Replicated |
| East Asians use resemblance more in the "similar to" condition | Original: n=18 per cell. European Americans rule 69% vs 31%; East Asians rule 41% vs 59% (t(17)=2.09, p=.05); Asian Americans 46% vs 54%; culture x response F(2,51)=8.01, p<.005. ML2 moderation by WEIRDness ran opposite (original condition effect: European Americans d=0.00, East Asians d=0.67) | b02, b05, b06 | Contested |
| Rule learning under conflict: East Asians make more errors when rule and exemplar similarity disagree | Culture x item type F(2,67)=3.81, p<.05; gap larger for East Asians F(1,67)=4.97, p<.05. Exemplar-only control: no culture effect F(2,77)=1.18. Errors fell 20.7% to 11.3% over trials, no culture main effect | Norenzayan 2002 Study 1 (b01, b25) | Contested (Klein 2009 found no rule-condition difference) |
| Klein 2009 categorisation replication | N=379 (17 to 24 years; n=45/44/50/46 Japan/Korea/Taiwan/US in similar-to). Holistic-response count F(3,181)=2.01, ns. US slower, t(89)=4.71, p<.001 vs Japan. Rule condition: no differences | Klein et al. 2009 (b08) | Partial (RT only) |
| Typicality in arguments stronger for Koreans | Culture x argument type F(2,253)=4.67, p<.01; Koreans vs European Americans F(1,253)=9.09, p<.005 | Norenzayan 2002 Study 3 (b03) | Single-source |
| Belief bias worse for Koreans | Response bias F(1,184)=14.41; abstract accuracy 45.1% vs 48.5%, t<1. Reanalysis: Koreans more conservative in saying "valid"; no accuracy gap once bias is handled | b03, b04 | Refuted (bias, not accuracy) |
| Triad grouping, humans | Chinese children pair by relation, Americans by category. Adults the same (Ji and Nisbett 2000). No counts in any source we read | Chiu 1972; Ji and Nisbett 2000 (a02, a04) | Counts unknown |
| Relation bias in children across countries | Korean 18 to 30 months n=91: same condition 28/41 (68%, BF10=4.07), different 25/50 (chance). Korean 3-year-olds n=55: 53% relational (BF10=0.34). Korean adults n=60: 52% relational (BF10=0.31). Korean toddlers fall between US (object bias) and China (relational bias), nearer US | Carstensen et al. 2026 (b13) | Single-source |
| Scene recall: more background statements | About 70% more background statements, about 100% more relation statements; equal focal-fish statements; N not given | Masuda and Nisbett 2001 via reviews (a09, a10, a11) | Single-source |
| Change blindness Exp 1 (30 US, 36 East Asian students) | Culture x change type F(1,64)=3.96, p=.05; East Asians faster on context F(1,64)=4.02; Americans faster on object than context F(1,64)=5.45 | Masuda and Nisbett 2006 (a12) | Single-source |
| Change blindness Exp 2 (19 US, 18 Japanese) | Interaction F(1,35)=9.44, p<.005; context F(1,35)=5.68; object F(1,35)=2.92 (marginal) | a13 | Single-source |
| Change blindness Exp 3 (28 US, 32 Japanese), plus Japanese-looking scenes | Culture x attention F(1,58)=22.72, p<.001; context F(1,58)=16.17; object F(1,58)=5.63; attention x scene type F(1,58)=128.62. Neutral scenes: object-change gap not significant | a14 | Single-source; scene effect as large as culture effect |
| Eye tracking: Americans fixate focal object sooner | N=21 US, 24 Chinese. 118 ms sooner, t(43)=2.41, p=.02 (g about 0.72, 95% CI 0.12 to 1.33, derived). More Chinese fixations F(1,43)=4.43, all from background F(1,43)=9.50. 420 to 1,100 ms Americans favour objects F(1,43)=7.31; 1,100 to 3,000 ms Chinese favour background F(1,43)=6.64. New-background recognition F(1,44)=5.72. Both groups fixated background more overall F(1,43)=72.46; about 32 to 35% of both groups already on the object at onset | Chua et al. 2005 (a16, a27, d04) | Contested |
| Eye tracking: no effect across all scenes | N=74 (Rayner 2007). Background time Chinese 2489 vs American 2565 ms, F<1; foreground 6445 vs 6633 ms, p>.10. Six Chua-like scenes only: foreground 4299 vs 4813 ms, t(45)=2.10, p=.04; background fixation count 16.3 vs 13.8, p=.02; group x area interaction ns | Rayner et al. 2007 (d01) | Failed replication (partial on subset) |
| Eye tracking: no effect for odd objects | N=24 (12 + 12), 20 scene sets. All group effects and interactions F<1. Fixation duration 282/281 vs 280/284 ms | Rayner et al. 2009 (d02) | Failed replication |
| Eye tracking: large effects in a third lab | N=31 (16 US, 15 Singaporean Chinese). Object dwell 254.2 vs 170.3 ms, F(1,29)=8.09, eta2=.22; gaze distance 710.2 vs 477.2 px, eta2=.43; object-background gaze moves 8.0% vs 3.9%, eta2=.43 | Goh et al. 2009 (d03) | Single-source; small N, large effects |
| Eye tracking in seven samples | About 408 participants, F(6,401)=12.77, omega2=0.15. Dwell on focal object: Ghana 1895 ms, Taiwan 1528 ms, Germany 1533 ms. Focal-minus-background gap: Ghana g=1.95, Taiwan g=0.44, others 1.3 to 2.1 | Scientific Reports 2025 (b11) | Culture differs, not along East-West |
| Eye tracking, faces | Priming individualism or collectivism did not change fixations (Gingras 2023). About 25% of British-born Chinese used Western strategies (Kelly 2011) | d05, d06 | Group effects hold; social-orientation mechanism fails |
| Framed line test | Relative errors F(3,375)=16.92; absolute F(3,375)=18.26. All three East Asian groups better than US in both conditions | Klein 2009 (b09) | Reversed vs original prediction |
| 11-country preregistered study | N=993 (Armenia, Australia, Brazil, Bulgaria, Czechia, Germany, Ghana, Philippines, Slovakia, Taiwan, Turkiye). Differences exist, not East-West; individualism and long-term orientation relate to both styles | Lacko et al. 2025 (b10) | Not opened; snippet-level |
| Infants (15 months) | Japan n=45, US n=52. Background looking about twice as long in cartoons; parent speech did not track infant behaviour | Carlson et al. 2025 (b12) | Single-source |
| Covariation, trend prediction, word recall on social backgrounds | Chinese predicted reversals in 11 of 12 curve conditions; Chinese recalled words better on social backgrounds; covariation 0.00 to 0.60 actual | Reviews (a18, b16, b17) | Secondhand, no N |
| Human analogue retrieval: surface similarity wins | Quality of reminding: surface 2.36 > analogy 1.48 > relations-only 0.86, F(2,58)=72.81, p<.0001. Soundness: analogy 4.40, surface 2.80, relations-only 2.74 | Gentner, Rattermann and Forbus 1993 (d16) | Replicated in the analogy literature |
| Irrelevant context hurts, "ignore" instruction helps a little | code-davinci-002: CoT 72.4 to 77.8 (+5.4); least-to-most 77.5 to 80.6 (+3.1); zero-shot CoT 29.0 to 30.5; program 54.4 to 56.7. Only 18% of base problems solved across all distractor types | Shi et al. 2023 (d15) | Single model, 2023 |
| Prompt format noise | Median spread 7.5 accuracy points across tasks, up to 76 (LLaMA-2-13B); GPT-3.5 up to 56, median 6.4 over 320 formats (Sclar 2023). Equivalent query rewrites: 45.48 points worst-to-best on Llama-2-70B-chat (Cao 2024) | d13, d14 | Replicated across two papers |

LLM-specific numbers are in section 6.

## 4. Mechanisms and models

The sources here do not contain a computational model. What they give are procedures and mechanisms that an engineer can use. Each is stated so it can be built.

**4.1 Wording-driven strategy switch (the one robust mechanism).** The same stimulus set yields different grouping rules depending on the instruction verb. Implementation of the test:
1. Build items with a target and two candidate groups. Group A shares one deterministic rule with the target; group B shares overall resemblance (family resemblance over several features) and violates the rule.
2. Make two prompts that differ only in the instruction: "Which group does the target belong to?" vs "Which group is the target more similar to?"
3. Run many samples per prompt (Many Labs 2 effect was d=0.86, so 30 to 50 items per arm gives power).
4. Metric: share of rule choices per arm. Expect higher in the belong-to arm.
The mechanism for humans: "belongs to" cues category membership and rule application; "similar to" cues global comparison. Choi et al. 1997 shows the same: naming the category in the conclusion switched the taxonomic mode on for Koreans (a07).

**4.2 Rule vs exemplar conflict task (Allen and Brooks).** Items have 5 binary features. Rule: any 3 of 5 features present means class V. Training exemplars are shown with labels. Test items come in two types: agree (rule and nearest exemplar give the same label) and conflict (the nearest exemplar has the opposite label). Metrics: errors on conflict items minus errors on agree items. The exemplar-only control separates strategy from ability (b01, b25). This is the structure that matches a coding agent facing a rule given in text and a surface-similar example that disagrees.

**4.3 Triad scoring.** Triad: three items; one relation pair, one taxonomic pair. Score either as relational share (Jin: relation match = holistic, similarity match = analytic) or as R-C score (Hu: higher means more relational). Both are defined by the authors; they are not interchangeable (d11, d12). Fix one rule before running. Use unseen triads: textbook examples (Seagull, Sky, Dog; cow, chicken, grass) are likely in training data.

**4.4 Change detection probe.** Present two versions of a scene (image, table, or described setting) with one change, either to the focal object or to a context element. Measure detection rate and time (for an LLM, detection accuracy and tokens to find it). Human design: flicker paradigm, 30 photo pairs, 60 s cap; or five animated vignettes (a12, a13). Key control from Exp 3: use culturally neutral and culturally mixed scenes, because the scene type moved results as much as culture (a14).

**4.5 First-fixation analysis (humans).** Eye tracker at 120 Hz, 36 pictures, 3 s each; compute time to first fixation on the object ROI, then fixation counts by region in windows (0 to 420 ms, 420 to 1,100 ms, 1,100 to 3,000 ms). Effect on first fixation about g=0.72 with wide CI (0.12 to 1.33). No agent analogue.

**4.6 Bias vs sensitivity separation.** From Unsworth and Medin (b04): score "valid/invalid" judgments with hit rate and correct-rejection rate (a sensitivity measure like d-prime), not raw accuracy. A group that says "yes" less often looks less accurate on believable items without being worse. Apply to any model: compute yes-rate per condition before inferring a reasoning bias.

**4.7 Holistic caption classifier (VLM).** Prompt a captioner with an image; a judge model labels each caption as holistic (background or whole-scene first) or analytic (focal object first). Sabir used GPT-4o with 5 or 6 few-shot examples and checked on 200 human-rated captions. Judge and human differ: GPT4o-JP 17.75% holistic by humans vs 29.00% by the GPT-4o judge (d09, c22). Any LLM-as-judge style metric needs a human spot check.

**4.8 Paraphrase spread (noise floor).** Generate at least 5 meaning-preserving wordings of the task. Run each arm over all wordings. Report mean, worst, best. A gain smaller than the worst-to-best spread is not evidence (d13, d14).

**4.9 Cue steering (VLMs).** In Gavrikov et al. 2025, the vision encoder holds both texture and shape cues and the language model suppresses one. Prompt instructions moved shape bias between 49% and 72% without large accuracy loss; vision-side steering moved it more. 1,280 cue-conflict images. Humans use shape 96% of the time; ImageNet ResNet-50 22%; VLMs about 54 to 74% (c13, c25).

## 5. What holds up

**Holds up.**
- The instruction effect on rule vs resemblance (d=0.86, N=7,396, many countries). Biggest single robust result in this subfield.
- Individual differences are large and strategies are not tied to country. About 25% of British-born Chinese used Western eye strategies (d05). Korean toddlers sit between US and Chinese toddlers and Korean adults show no relational bias (b13).
- Scene content moves attention as much as culture. Exp 3 of change blindness: attention x scene type F(1,58)=128.62 vs culture x attention F(1,58)=22.72 (a14).
- Attention can be primed. Japanese town scenes raised context detection for both Americans and Japanese (a15). But priming individualism or collectivism did not change face eye movements (d06).
- Salience cues switch category use on. Naming the category in the induction conclusion raised Koreans' use of it (a07, b15).

**Failed or weakened.**
- Eye tracking. Rayner 2007 (N=74): no group effect over all scenes. Rayner 2009 (N=24): all F<1. Evans et al. 2009 (not opened): second null. Chua 2005 itself: g about 0.72 with CI near zero at the low end. Goh 2009 found large effects with N=31 (probably inflated). Seven-sample 2025 study: no East-West order (Germany as low as Taiwan). Verdict: small to moderate, scene-dependent.
- Rule vs resemblance by culture. Klein 2009: no choice difference in either condition; only response time. Many Labs 2: moderation by WEIRDness opposite to the original. The original had n=18 per cell with p=.05.
- Belief bias. Reduced to response bias (b04).
- Framed line test. East Asians better in both conditions, reversing the original prediction for the absolute condition (b09). Authors warn of confounded group differences.
- Global East-West axis. Lacko et al. (N=993, 11 countries): no East-West line (b10).

**Moderators and boundary conditions.**
- Stimulus: Chua-like scenes (one or two clear focal objects) show part of the effect; other scenes do not (d01).
- Scene origin: American scenes vs Japanese-looking scenes (a14). In culturally neutral scenes the object-change gap vanished.
- Task: choice vs response time (b08). Culture effect shows in time, not choice.
- Sample: international students at US universities, bilingual Singaporeans, native Chinese in the US. None are random national samples. Rayner et al. link fixation duration to writing system experience (d01).
- Power: Schimmelpfennig et al. 2024 (snippet only) say Many Labs 2 had low power to detect cultural heterogeneity (b07).

**Interventions that worked (in humans).** Changing the instruction verb (d=0.86). Naming the category. Priming with complex scenes. Making typicality salient.

**Interventions that did not work.** Priming social orientation for face scanning (d06). Language of testing for bilinguals is generally not predictive (a19), though Ji, Zhang and Nisbett found a language effect in one study (a20). Mixed.

**Competing explanations.** Ecology and subsistence (d19, listing only). Physical environment (a15). Writing system (d01). General task skill confounds (b09). Response bias (b04). Sample selection (international students).

## 6. Language models

**6.1 Triad grouping.**
- Jin et al. 2023 (a21, b21, c01, c02, c03, d11). GPT-3.5 and GPT-4, 10 runs each at temperature 1. Relational share 0.87 (SD 0.06) and 0.85 (SD 0.05), robust over temperature 0 to 1.5 and prompt language. Analysis-Holism Scale: GPT-3.5 5.35 (SD 0.11), GPT-4 5.01 (SD 0.10) vs human norm 4.87 (SD 0.49, N=702). Dialectical Self Scale: GPT-3.5 4.59 vs 4.00 (p<.001), GPT-4 3.97 vs 4.00 (p=.344). Self-Construal Scale, independent: 6.98 and 5.32 vs 4.73; interdependent 5.85 and 4.95 vs 4.81. GPT-3.5 answered "strongly agree" to nearly everything. Limits: only 10 of the 20 triad items were real, the items are published, runs are the unit of N so p-values are inflated, and the comparison was to Chinese provincial means, not a US norm.
- Hu et al. 2026 (a23, b19, c07, c08, c24, d12). 2x2: US model (GPT-4o) vs Chinese model (ERNIE 4.5) by English vs Chinese prompt, 100 runs per condition per task (N=400 per task), temperature 1, 8 tasks. Task 4 triad (Seagull, Sky, Dog): R-C score US 8.10 (SD 1.44) vs Chinese 6.04 (SD 1.54), t=-13.81, p<.001, d=1.38 (US model more relational, opposite to the human pattern). Prompt language 7.10 (SD 2.15) vs 7.04 (SD 1.40), t(342.66)=0.33, p=.741, d=0.03. Within the Chinese model, Chinese prompts gave less relational pairing: 5.30 vs 6.78, t=-7.74 ("cultural reversal").
- Atari et al. 2023 (c15, snippet only): GPT answers on psychology measures resemble WEIRD populations; reported r about -.70 between cultural distance and similarity. Conflicts with Jin on direction; not opened.
- Reading: Jin and Hu are not comparable (different items, scoring, models). Both rely on famous triads.

**6.2 Prompt language and persona.**
- Lu, Song and Zhang 2025 (b22, c06, d07): GPT and ERNIE more holistic and interdependent in Chinese than English; a Chinese persona shifts English answers. Only the abstract was reachable. Per Sun and Wang: 4 to 12 items per task, 7 tasks, 2 models, items not released.
- Sun and Wang 2025 (a22, b18, c04, c05, c23, d08). Replication with 8 models (gpt-4.1, gemini-2.5, claude-sonnet-4, grok-4, kimi-k2, deepseek-V3, ernie-4.5, qwen3-30b), 30 to 60 items per task, temperature 0. Exp 1 overall language effect: mean difference 0.0053, p=.1501, d=0.045; significant models deepseek and qwen (both preferred Chinese, 0.01<p<0.05). Exp 2: 3 of 8 models significant: ernie d=-0.171, qwen d=0.540, gpt d=-0.190. Other task p-values for language: .25, 1.0, .917. Model origin: no effect. Picture task (4 items): 7 of 8 models gave identical choices across languages. Framing (change-framed vs neutral) in the appendix: d=-2.095, eta-squared 0.54. The summary table calls framing small; the appendix numbers are the data.
- Hu 2026: language effect on triads null (above). On attribution, the Chinese model rose on both collective (3.17 vs 2.81, d=1.14) and individual (4.75 vs 4.67, d=0.27) attribution, contradicting the human trade-off. RLHF-tuned models collapsed variance toward a helpful-assistant persona (b20).
- Tao et al. 2024 (c14, c26): cultural prompting shrinks distance to survey profiles for newer models: GPT-4o 2.42 to 1.57, GPT-4-turbo 2.71 to 1.77, GPT-4 2.69 to 1.65 (all p<.001); GPT-3 2.39 to 2.11; GPT-3.5-turbo 3.35 to 2.83. Improved for 71 to 81% of 107 countries (GPT-4 family). Unprompted GPT-3.5-turbo is closest to Sweden (0.24) and Norway (0.58), farthest from Tunisia (4.16). These are values, not cognitive style.
- Dai et al. 2025 (c16): LLM word associations closer to US than to UK, Australian or Chinese schemas; the CultureSteer method helped more than cultural prompts. 881 shared cue words, 22 semantic classes.

**6.3 Attention probes.**
- Hu 2026 Tasks 1 and 2 (a24, c09). Image generation: DALL-E 3 11.53 objects (SD 4.39) vs iRAG-1.0 8.10 (SD 1.91), d=1.01 (US model more objects; horizon higher 533.47 vs 519.79, d=0.34). Chinese prompts gave more objects in generated landscapes (10.71 vs 8.91, d=0.49, t(286.19)=4.88; horizon 523.20 vs 530.06, p=.096). Scene description (Task 2): English 10.90 vs Chinese 10.06 objects, t(374.94)=-3.60, d=0.36. Object count is a poor stand-in for attention (verbosity confound).
- Sabir et al. 2025 (a25, c10, c11, c22, d09, d10): VLM captions, holistic share. GPT4o-JP 6-shot: 26.10% on COCO vs 73.37% on 1K Japanese photos (+47.3 points). Plain GPT-4o on Japanese set: 57.6 to 59.1%. COCO 1K: GPT-4o 26.2%, GPT4o-JP 35.5%, Gemma-3-27B 19.2%, Gemma-3-27B-JP 28.8%, Gemma-3-12B 13.7 to 19.3%, VILA-JP-14B 14.7%. Caption language (5K captions): English original 12.34% vs Japanese translation 27.54% (+15.2); Japanese original 27.48% vs English translation 16.26% (+11.2); average shift 13.21%. Few-shot example composition alone moved HERON GPT4o-JP from 34.88 to 53.49 (+18.6). Human check on 200 captions: judge inflates holistic share. Image content is the larger factor; language the smaller.
- Ananthram et al. 2024 (c12): nearly all VLMs better on Western than East Asian images; prompting in Chinese did not reliably cut the bias; language mix in text pre-training explained most of it.
- Gavrikov et al. 2025 (c13, c25): prompts alone steer shape bias 49% to 72%.

**6.4 Taxonomy vs theme in models.**
- Klubicka and Kelleher 2023 (c17): static embeddings trained on text mostly encode thematic relations; taxonomic information sits in vector norm only for taxonomic embeddings (norm difference an order of magnitude larger). Not modern LLMs.
- Rodriguez, Mueller and Misra 2025 (c18): four LMs project properties using both taxonomy and similarity, not one exclusive rule; interventions support this.
- No study gives LLMs child-style thematic vs taxonomic triads by age (c21, d18; weak evidence of absence).

**6.5 Distractors and noise.** Shi et al. 2023 (d15): "feel free to ignore irrelevant information" gave +5.4 (CoT) and +3.1 (least-to-most) points on a 2023 model. Sclar 2023 (d13): format changes alone moved accuracy median 7.5 points, up to 76. Cao 2024 (d14): 45.48 point best-worst gap.

**6.6 What the LLM results say together.**
1. Frontier chat models sit near the relational end on the famous triads, or at least not at the taxonomic end (Jin). The Hu result shows direction depends on model and scoring.
2. Prompt language and persona do not reliably move cognitive-style outputs (Sun and Wang; Hu). Wording and framing move them much more (framing d=-2.095 vs language d=0.045).
3. Content of the stimulus moves style more than language (Sabir +47 vs +11 to +15).
4. Method weakness: two models per side, temperature 0 or 1, run-level N, famous items likely seen in training, LLM judges.

## 7. What our agent should take

Relevance is "background only". Items are placed against schema parts (G guardrail, S state, O operator, memory). Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not use persona, culture or prompt-language prompts to switch reasoning style. Language and persona effects on LLM style are small and model-specific (overall d=0.045; 3 of 8 models in one experiment). Supports G4 and the 4b list. | G4, section 4b | [E] | a22, b18, c04, c05, a23 (A19.04-K13) |
| Any scaffold test must report a paraphrase spread: at least 5 wordings of the task, with worst, best and mean. A gain below the spread (median 7.5 points, up to 76) is not evidence. | G7 | [E] | d13, d14 (K22) |
| When comparing groups or conditions on "does it accept this as valid", score with a bias-free measure (hit and correct-rejection rates), not raw accuracy. Check yes-rate before blaming belief bias. | G10 | [E] | b03, b04 (K04) |
| Do not assume a neutral or analytic model default. Models skew WEIRD in values and word associations; do not trust a model's self-reported style. | G7 note | [E] | c14, c16, c15, c12, c26 (K17) |

Note that none of these adds an operator or a state. They are test-design rules. Add them to the G7 test protocol, not to the solve path.

### Test first (not established for the agent)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Rule vs resemblance wording ("belongs to" vs "is similar to") shifts our agent's grouping. If yes, S2 representation wording per task class can be chosen by test. | S2, O6 | [E] in humans (d=0.86); untested on the agent | b02, b05, b25 (K01) |
| Framing control: change-framed vs neutral wording moves answers far more than scaffold steps. Use as control arm. | G7 | [S] | a22, c04, c05, d10 (K14) |
| Context-first vs focal-first vs neutral instruction on distractor-heavy and change-detection tasks. | O6, S1 | [S] (GSM-IC +3 to +5 points for "ignore") | d15, a12 to a14 (K06, K23) |
| Relation-naming cue vs object-matched cue for analogue retrieval (O7). Human retrieval is driven by surface cues; relation cue may need to be named. | O7, memory | [S] | d16, d17 (K24, K18) |
| Triad test on our own model with fresh triads to measure default relational lean. | S2 (informational) | [S]/[C] | a21, a23, d11, d12 (K11, K12) |
| Replicate Sun and Wang (language and persona) on our model at temperature 0 and 1. Closes the Lu et al. dispute for our model. | G4 | [C] | b22, c06, d07, d08 (K13, K25) |
| Instruction naming the relevant cue (object vs surface) when vision input is used. | O6 | [S] | c13, c25 (K20) |
| Child-style thematic vs taxonomic triads (open niche). | none | [S] | c21, d18 (K19) |

## 8. Concrete tests on our bench

All arms at equal tokens. Equal tokens means the same total prompt and output budget; the added instruction replaces a same-length neutral sentence.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Wording lever | 40 target-plus-two-groups classification items (rule group vs resemblance group), fresh, 5 paraphrases each | "belongs to" vs "is similar to" vs neutral "which group" | Rule-choice share per arm; paired difference over items | Human d=0.86. Expect a rule-share gap of 10 to 20 points if the model behaves like humans; may be near zero or larger for LLMs |
| T2 Wording noise floor | Any existing bench set (ARC-like or brain teasers) | Plain model vs scaffold, each over 5 or more paraphrases | Mean, worst, best accuracy; gain vs spread | Gains under about 7 to 10 points likely inside spread |
| T3 Framing control | Same items as T2 | Neutral wording vs change-framed wording vs scaffold | Accuracy difference of framing vs scaffold | Framing may move results as much as a scaffold step (Sun and Wang d=-2.095 on their tasks) |
| T4 Context-first instruction | 60 distractor-heavy problems (GSM-IC-style) and 40 change-detection items (two versions of a table or text scene, one planted change either focal or context) | Focal-first vs context-first vs neutral instruction | Accuracy; detection rate by change type | Ignore-instruction gave +3 to +5 on a 2023 model; context-first untested. Expect small gain, maybe none on current models |
| T5 Triad default | 30 fresh triads (not published; relation pair vs taxonomic pair), plus 10 published ones as contamination check | One model, 100 runs at temperature 1, plus temperature 0 | Relational share; fresh vs published difference | Jin 0.85 to 0.87 on published items. A drop on fresh items signals memorisation |
| T6 Language and persona replication | 40 fixed items spanning attribution, syllogism, triad | English vs Chinese prompt; no persona vs "average person living in China" persona | Mean difference, Cohen's d, per model, at temperature 0 and 1 | Expect d under 0.1 (Sun and Wang). If above 0.3 on a model we use, note it and do not use that lever without a test |
| T7 Analogue retrieval (O7) | 30 problems with one correct precedent among 10 distractors, half with surface-matched distractors | Cue = object description vs cue names the relation or causal structure | Top-1 retrieval rate; downstream solve rate | Human data say surface cue wins retrieval. Naming the relation may help; unknown |
| T8 Bias check | Existing syllogism or validity set | Raw accuracy vs sensitivity (hit and correct-rejection) | Yes-rate per condition | Flags response bias; no prediction on size |

Report for every test: number of items, runs per item, temperature, model name, paraphrase spread (G7), and a human spot check if a judge model scores style.

## 9. What does not transfer, and why

- **Eye movements.** No agent analogue. Chua 2005, Rayner, Goh and the seven-sample study are about fixation timing. Skip.
- **Culture as a property of the agent.** Humans differ by social history and ecology. An LLM has no ecology, and the "Chinese model" also differs in data, alignment and tuning. Model origin did not predict behaviour (Sun and Wang, Hu). Confounds culture with RLHF.
- **Self-report scales on a model.** AHS, DSS, SCS measure self-perception; models answer with acquiescence (GPT-3.5 "strongly agree" to nearly everything). Cognitive-process and value scales also dissociated (Jin).
- **Object counts as an attention proxy.** Verbosity confound (Hu).
- **Social-orientation priming.** It failed for face eye movements (Gingras 2023). A collectivist role prompt is unlikely to change the agent's grouping style.
- **Human-specific attention effects (change blindness, scene recall).** Task presentation differs. A model reads the whole input at once. The only transferable part is whether instruction direction (focal-first vs context-first) changes accuracy.
- **A fixed East-West style axis.** It did not hold in the 11-country study, in the seven-sample eye study or in Rosetta. Not a safe design basis.
- **Famous triads.** Chiu, Ji and Nisbett examples, and "Seagull, Sky, Dog" are likely in training data. Do not read LLM results on them as reasoning.
- **Judge-model style scores.** The judge reads more holistic than humans (29.00% vs 17.75%).

## 10. Open questions

1. Is the high relational triad share in LLMs stable across scoring rules and unseen triads, or memorised? No fresh-item study exists (gap 2).
2. Does a "context first" vs "focus first" instruction change accuracy on distractor and change-detection tasks for current models? Only "ignore irrelevant information" was tested, on one 2023 model (gap 3).
3. Do persona or language prompts change anything on our model at temperature 0 and 1? Sun and Wang used temperature 0, which removes variance (gap 4).
4. What are the real numbers in Lu et al. 2025? Full text paywalled (gap 7).
5. Do LLMs show the child thematic-to-taxonomic shift when given age-labelled triads? No study (gap 6).
6. Does naming a relation in the retrieval cue help analogue retrieval (O7)? Human data suggest surface cues dominate; LLM data secondhand (gap 8).
7. Chiu and Ji and Nisbett triad counts are unknown to us; the size of the original categorisation effect in adults is unchecked.
8. Evans et al. 2009 and Lacko et al. 2025 were not opened in full.
9. How much of the Sabir caption gap is image content and how much output language, in a fully crossed design? Partly answered (content +47, language +11 to +15).
10. Does the wording effect (d=0.86 in humans) appear in LLMs, and with what size?

## 11. Sources

[V] = opened and read this session (full text or PDF text). [M] = snippet or secondary summary only.

- [V] Nisbett, Peng, Choi and Norenzayan (2001) Culture and systems of thought. Psychological Review 108, 291-310. https://public.websites.umich.edu/~nisbett/images/cultureThought.pdf
- [V] Nisbett and Masuda (2003) Culture and point of view. PNAS 100. https://pmc.ncbi.nlm.nih.gov/articles/PMC196945/
- [V] Nisbett and Masuda (2007) Culture and point of view. Intellectica. https://sites.ualberta.ca/~tmasuda/PublishedPapers/NisbettMasuda2007.pdf
- [V] Nisbett and Norenzayan (2002) Culture and cognition, Stevens' Handbook. https://public.websites.umich.edu/~nisbett/cultcog2.pdf
- [V] Norenzayan, Choi and Peng, cultural psychology handbook chapter. https://www2.psych.ubc.ca/~ara/Manuscripts/Norenzayan_etal%20CP%20Handbook%20chapter.pdf
- [V] Norenzayan, Smith, Kim and Nisbett (2002) Cultural preferences for formal versus intuitive reasoning. https://public.websites.umich.edu/~nisbett/formalreas.pdf
- [V] Masuda and Nisbett (2006) Culture and change blindness. Cognitive Science 30. https://sites.ualberta.ca/~tmasuda/PublishedPapers/Masuda&Nisbett2006.pdf
- [V] Chua, Boland and Nisbett (2005) Cultural variation in eye movements during scene perception. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC1194960/
- [V] Rayner, Li, Williams, Cave and Well (2007) Eye movements during information processing tasks. https://pmc.ncbi.nlm.nih.gov/articles/PMC2048814/
- [V] Rayner, Castelhano and Yang (2009) Eye movements when looking at unusual scenes. https://pmc.ncbi.nlm.nih.gov/articles/PMC2668126/
- [M] Evans et al. (2009) eye movements and culture (cited in Rayner 2009; no direct page).
- [V] Goh, Tan and Park (2009) Culture modulates eye-movements to visual novelty. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0008238
- [V] Kelly et al. (2011) Social experience does not abolish cultural diversity in eye movements. https://www.frontiersin.org/articles/10.3389/fpsyg.2011.00095/full
- [V] Gingras et al. (2023) Eye movements for face recognition, Canadian vs Chinese. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0295256
- [V] Cross-cultural analysis of eye-movement patterns, seven cultural samples (Scientific Reports 2025). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12326012/fullTextXML
- [V] Unsworth and Medin (2005) Cultural differences in belief bias. Cognitive Science 29. https://groups.psych.northwestern.edu/medin/documents/unsworthmedin2005culturaldifferences.pdf
- [V] Klein et al. (2018) Many Labs 2. https://uni-potsdam.de/fileadmin/projects/krahe-sozialpsychologie/images/pdf/ML2.manuscript.pdf
- [M] Schimmelpfennig et al. (2024) reanalysis of Many Labs 2 cultural variability. https://doaj.org/article/68846c406a874c64ad7a4377b3348af3
- [V] Klein et al. (2009) Rosetta Phase I. Psychological Reports 105. https://sites.ualberta.ca/%7Etmasuda/PublishedPapers/Krein_2009.pdf
- [M] Lacko et al. (2025) Geography of thought across 11 countries. JEP General 154. https://doi.org/10.1037/xge0001685
- [V] Carlson et al. (2025) Cultural differences in visual attention emerge in infancy. https://pmc.ncbi.nlm.nih.gov/articles/PMC11742511
- [V] Carstensen, Kim, Choi and Walker (2026) Relational reasoning across cultures. https://pmc.ncbi.nlm.nih.gov/articles/PMC13509761
- [M] Uskul et al. (2008) Ecocultural basis of cognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC2438425/
- [V] Gentner, Rattermann and Forbus (1993) The roles of similarity in transfer. https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf
- [V] Jin et al. (2023) The cultural psychology of LLMs. https://arxiv.org/abs/2308.14242
- [V] Sun and Wang (2025) The fragility of cultural tendencies in LLMs. https://arxiv.org/abs/2510.05869
- [V] Hu et al. (2026) Machine culture. https://arxiv.org/abs/2601.17096
- [V] Sabir, Gasper, Loem and Sharma (2025) Contrasting cognitive styles in VLMs. https://arxiv.org/abs/2507.00700
- [M] Lu, Song and Zhang (2025) Cultural tendencies in generative AI. https://www.nature.com/articles/s41562-025-02242-1 (abstract only; secondary: https://mitsloan.mit.edu/ideas-made-to-matter/generative-ai-isnt-culturally-neutral-research-finds)
- [V] Ananthram et al. (2024) See it from my perspective. https://arxiv.org/abs/2406.11665
- [V] Gavrikov et al. (2025) Are VLMs texture or shape biased. https://arxiv.org/abs/2403.09193
- [V] Tao et al. (2024) Cultural bias and cultural alignment of LLMs. https://arxiv.org/abs/2311.14096
- [M] Atari, Xue, Park, Blasi and Henrich (2023) Which humans? https://www.hks.harvard.edu/centers/cid/publications/which-humans
- [V] Dai et al. (2025) From word to world. https://arxiv.org/abs/2505.18562
- [V] Klubicka and Kelleher (2023) Probing taxonomic and thematic embeddings. https://arxiv.org/abs/2301.10656
- [V] Rodriguez, Mueller and Misra (2025) Role of similarity in property inferences of LMs. https://arxiv.org/abs/2410.22590
- [V] Sclar, Choi, Tsvetkov and Suhr (2023) Sensitivity to spurious features in prompt design. https://arxiv.org/abs/2310.11324
- [V] Cao et al. (2024) On the worst prompt performance of LLMs. https://arxiv.org/abs/2406.10248
- [V] Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093
- [M] Chiu (1972); Ji and Nisbett (2000); Ji, Zhang and Nisbett (2004). Read only through the 2001 and 2003 reviews. https://doi.org/10.1037/0022-3514.87.1.57
- [M] Search summaries on analogy retrieval by LLMs (Jiayang et al. 2023; ADR-bench) https://arxiv.org/pdf/2505.00603 and LLM thematic vs taxonomic triads by age https://arxiv.org/html/2505.21301v1
- [M] Choi, Nisbett and Smith (1997); Norenzayan, Choi and Nisbett (2000); Masuda and Nisbett (2001); Hedden et al. (2000); Ji, Peng and Nisbett (2000). Read only through reviews.

Related subfields run in parallel (links only, not covered here): Whorfian psychophysics; Thinking for speaking; Causal attribution; Debiasing; Heuristics and biases; Dual-process accounts of judgment; Analogy and precedent in legal theory; Three attention networks.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 3 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A19.04-K21** (reworded: the sources support less). Gingras 2023 shows only that a pronoun-priming manipulation (N=36) did not change eye movements, and its group differences replicated only partly, so it does not show social orientation fails to explain the differences; Kelly 2011 (about 25% Western, 30% in Exp 1) is correct. Corrected claim: In face-recognition eye tracking, priming individualism or collectivism did not change eye movements (Gingras 2023, 15 Swiss and 21 Chinese participants), and most British-born Chinese kept Eastern strategies with about 25% using Western ones (Kelly 2011), so culture of origin alone does not determine strategy. Faces only.
- **A19.04-K22** (reworded: the sources support less). Sclar and Cao report spreads (median 7.5 points, up to 76; best-worst gap 45.48 on AlpacaEval win-rate for Llama-2-70B-chat) but do not show that a scaffold gain under 7 to 10 points is indistinguishable from noise; that threshold is an extrapolation across different tasks and settings. Corrected claim: Wording and format noise can be large relative to small effects: meaning-preserving prompt format changes give a median 7.5 point and up to 76 point accuracy spread (Sclar 2023); equivalent query rewrites give a 45.48 point best-worst win-rate gap on Llama-2-70B-chat (Cao 2024). Scaffold gains of only a few points should be checked against sampled paraphrases before being trusted.
