# Medical diagnostic reasoning: what it offers one thinking agent

Evidence ids are in brackets, for example [diag-a-02]. Where the round-3 CHECK lines (evidence_d) differ from claims.jsonl, the CHECK lines are used. Our own measurements come from 00_PLAN.md and are marked [ours].

## 1. What the field studies

Diagnostic reasoning research asks how doctors get from a patient's first cues to a correct diagnosis, and why they sometimes fail. Most of the work is human: controlled trials on students and residents solving written cases, plus case reviews of real errors. The standard theory is dual process (fast pattern recognition and slow analysis). An older theory says clinicians form a few hypotheses early from the first cues and then gather data to test them [diag-a-22, from memory only]. The field has run many trials on one question that matters to us: which thinking instructions actually raise accuracy, and which only feel careful. Since 2023 it also tests LLMs on the same cases [diag-a-19, diag-a-18].

Two cautions apply to everything below. Human trials use vignettes and trainees, and a model holds its facts in weights, so some mechanisms may not carry over. Most LLM results use large models on curated cases, while our model is small and our tasks are messy.

## 2. Established findings

**E1. Telling people to slow down and be analytic does not raise diagnostic accuracy.**
- Residents told to be fast scored about 45.0% and residents told to be reflective about 44.5% on 20 cases; the careful group took longer and wrong answers took longer than right ones [diag-a-02, diag-d-01]. The quote from the abstract is that "simply encouraging slowing down and increasing attention to analytical thinking is insufficient" [diag-d-01].
- Across 393 clinicians, fast versus analytic instructions made no difference (F[1,379]=2.44, P=.12). Case complexity and experience had large effects [diag-a-14].
- Two independent studies agree [diag-a-02, diag-a-14, diagnostic-c-02]. The sample sizes of Norman 2014 and the response-time correlation attributed to Sherbino (r = -0.54) are not verified, so neither is used here [diag-d-04, diagnostic-c-03].
- This matches our losses when a schema forced slowing or doubt on single-answer tasks (ARC 2/8 against 4/10; word puzzles about 75% against 92%) [ours].

**E2. Unstructured reflection on one's own first diagnosis rarely changes the answer and fixes about as often as it breaks.**
- 47 residents re-reviewed 16 cases: only 8% of 745 diagnoses were revised and mean score moved from 1.20 to 1.22 on a 0 to 2 scale [diag-a-03, diag-b-02]. Of 158 fully wrong diagnoses only 18% were revised [diag-b-03].
- In 186 students, guided reflection with 2 or 6 own alternatives gave strict accuracy of 0.41 and 0.42 against 0.47 for first impressions. Changes went both ways: 16 corrections and 26 backfires in the short condition, 14 and 14 in the long one [diagnostic-c-04, diagnostic-c-05, diag-b-04].
- Note on references: the link PMC4539330 is Monteiro 2015, not Norman 2014. The Norman 2014 record is PubMed 24362377 [diag-a-03, diag-b-15, diagnostic-c-01].

**E3. Debiasing lessons and bias-focused checklists do not reliably cut error.**
- A debiasing checklist and a knowledge-retrieval checklist each failed to beat no checklist on ECG reading (61 residents and fellows, RCT) [diag-a-07, diag-b-06, diagnostic-c-07].
- A debiasing workshop improved 1 of 4 outcomes; diagnostic concordance was 74% against 78% [diagnostic-c-08].
- A narrative review found bias-recognition teaching did not reduce error, while strategies that reorganize knowledge gave small, consistent gains [diag-a-06]. A 2022 preprint review of 17 studies found mixed results [diagnostic-c-10]. An earlier essay argued for the opposite before these trials [diagnostic-c-12].

**E4. Confidence is a weak signal of correctness, and overconfidence goes with error.**
- 118 internists were right on 55.3% of easy cases and 5.8% of hard ones, yet confidence barely moved (7.2 against 6.4 of 10) [diag-a-10].
- A review of 20 studies (6,810 physicians) linked overconfidence and anchoring to error, but most studies were low quality [diag-a-08, diag-a-11].
- Design consequence: the model's own stated confidence is a poor gate. This is human evidence only; no LLM calibration test was found (section 7).

**E5. A doctor with an LLM did not reliably beat the LLM alone.**
- US trial, 50 physicians: 76% with GPT-4 against 74% without (P=.60); GPT-4 alone scored 92% [diag-a-18, diag-b-09, diagnostic-c-14].
- UK replication (22 physicians) and a 30-case ophthalmology study also had the LLM alone ahead of the assisted humans, by 21 points and 10 points [diagnostic-c-15, diagnostic-c-16]. Both are 2026 abstracts of low credibility, so treat the direction as supported and the sizes as soft.
- Use: the LLM's output should pass through program structure, not wait for a human to apply it.

**E6. Injecting a cognitive-bias cue into a medical question lowers LLM accuracy, most for small open models.**
- On BiasMedQA (1,273 USMLE questions, seven biases, six models) every model lost accuracy. GPT-4 lost about 5%, GPT-3.5 about 18% and Llama 2 70B about 20% on average; false consensus hurt most [diag-a-20, diag-b-10, diagnostic-c-17]. Other lines of the same study report 10 to 26% because of averaging choices [diag-b-10].
- Bias-awareness prompts and few-shot examples recovered only part, and weak open models barely improved [diag-b-11, diag-a-20].
- Independent support: models abandoned correct reasoning when given misleading expert hints [diagnostic-c-20, abstract only], and real-case accuracy depended on the order and amount of information given [diagnostic-c-18].
- Design consequence: any candidate card or hint we give a small model can anchor it.

## 3. Single-source and contested findings

### Single-source

**S1. A differential checklist helps only if it contains the right answer.** One RCT of 90 students: 0.75 with a checklist holding the correct diagnosis, 0.49 control, 0.43 with a checklist lacking it, 0.53 for a prompt to list your own alternatives (not significant) [diag-a-04, diag-b-05, diagnostic-c-06]. The three lines are one study. Indirect support: in Lambe 2018 students named the correct diagnosis among their alternatives more often yet final accuracy did not rise [diag-b-04]. This is the most useful design result in the field and it is one trial.

**S2. Premature closure is the most common cognitive cause of error.** In 100 internal-medicine error cases, cognitive factors appeared in about three quarters and system factors in about two thirds; premature closure was the commonest cognitive cause and knowledge gaps were rare [diag-a-01, diag-b-07, diagnostic-c-11]. It is a case series with no control, so it shows where errors cluster, not what cures them. The three lines are one study.

**S3. Illness scripts.** The concept has a strong theoretical base [diag-a-16, narrative review]. One RCT found a 14% gain on reasoning problems but no change in overall diagnostic thinking (snippet only) [diag-a-17]. Controlled evidence for better diagnosis is thin; untested for LLMs.

**S4. GPT-4 recall beats ranking.** On 70 NEJM cases the right diagnosis was in the differential 64% of the time (45/70) but ranked first only 39% (27/70) [diag-a-19, diag-b-08, diagnostic-c-13]. One study, an old model. It suggests generate-then-discriminate has room to help.

**S5. MAI-DxO.** An orchestrated panel around o3 reached about 80% (85.5% at the maximum setting) on 304 NEJM sequential cases against 20% for generalist physicians, at lower cost [diag-b-12, diagnostic-c-19, diag-d-02]. It is a vendor preprint. Caveats: virtual costs, hard cases, physicians without references, a simulated gatekeeper [diagnostic-c-19]. The abstract page shows no ablation against a single model with equal tokens or against voting, and that question is still unsettled [diag-d-02, diag-d-03]. The report that gains hold across model families was seen once and not independently checked [diag-b-13].

**S6. Medprompt.** Dynamic few-shot, self-generated chain of thought and a choice-shuffle ensemble took GPT-4 above 90% on MedQA with about an order of magnitude fewer calls than Med-PaLM 2 [diag-b-14, diagnostic-c-24]. One preprint on an exam benchmark; the abstract does not say which part carried the gain.

**S7. Partial schemas can score below no schema.** Removing any module of a TCM reasoning pipeline dropped it below zero-shot [diagnostic-c-23]. In a hypertension study the worst LLM setups made physicians' decisions worse [diagnostic-c-22]. Both are 2026 abstracts of credibility 40 to 50. They agree with our own scaffold losses but are not strong proof.

**S8. Context only.** Outpatient diagnostic error occurs in about 5% of US adult visits [diag-a-09]. AMIE, a conversational diagnostic LLM, was rated better than primary care physicians on most axes in 159 simulated scenarios (vendor study, text chat) [diag-a-21]. Neither says anything about schema structure.

### Contested

**C1. When does reflection help?** Positive: reflection helped on complex cases and on cases like earlier ones, and made no difference on simple cases; structured reflection helped delayed but not immediate tests [diag-a-12, diag-a-13, diag-a-15]. A 28-study review called guided reflection the most consistent intervention, though many studies were weak [diag-a-05, diagnostic-c-09]. Negative: E1 and E2. The Mamede lines are snippet-level only [diag-a-12, diag-a-13, diag-a-15]. The likely resolution is that structured reflection can help on hard cases and does nothing by default. That fits both sides, which is also a reason to doubt it. It supports a conditional trigger, not a schedule.

**C2. Size of the human gain from LLM help.** Null in the US trial (+2, P=.60) [diag-a-18], +8.6 points in the UK replication [diagnostic-c-15], +0.15 in the ophthalmology study with 20% of users made worse and 58.6% of failures following wrong LLM advice [diagnostic-c-16], and top-3 up but top-1 not (p=.08) in a 13-physician simulation [diagnostic-c-21]. Different tasks, tiny samples, abstracts.

**C3. Curated cases against real ones.** Frontier LLMs did worse than physicians on 2,400 real MIMIC-IV abdominal cases and ignored guidelines [diagnostic-c-18], in contrast to strong results on curated NEJM cases [diag-a-19, diag-b-12]. Messy real input against published puzzle cases is the likely cause. Our setting is closer to the messy side.

**C4. Longer reasoning.** One 2026 abstract reports that longer reasoning is not always better in medical LLMs and that non-reasoning models saturate fast [diagnostic-c-20]. The human parallel is E1, but the mechanisms differ. Needs a delta check.

## 4. Mechanisms an agent can run

All checks below compare against the plain model at equal total tokens. None has been tested on our model. Every mechanism rests on thin or human-only evidence, so each is a candidate to test, not a recommendation.

**M1. Outside-sourced candidate list, only at an impasse.**
- Trigger: the probe attempts disagree or no check passes. Not on easy items.
- Action: obtain candidates from a source other than the same attempt's own first thought (a separate blind generation call, a retrieved list, or a fixed list for the task type). Then compare them with the case.
- Check: plain model at the same tokens, scored on items where a hard case is known to exist. Count cases where the correct answer is in the list but the model drops it.
- Evidence: [diag-a-04, diag-b-05, diagnostic-c-06, diag-b-04, diag-a-19].
- Risk: the list helps only if it holds the right answer, and a wrong list lowered accuracy in the human arm (0.43 against 0.49, not significant) [diag-a-04]. A small model can be anchored by a wrong card [diag-a-20, diagnostic-c-20]. On single-answer tasks with a right first answer this adds cost and a chance to be talked out of it [ours].

**M2. Generate wide, then discriminate with a separate pass.**
- Trigger: open or hard item where the first answer is not trusted (probe disagreement).
- Action: one call writes a short differential; a second, separate call chooses which input fact would split the top two and reads the case for it, then ranks.
- Check: equal-token majority vote and plain single answer; measure top-1 and whether the correct item moved up.
- Evidence: [diag-a-19, diag-b-08, diagnostic-c-13] (recall above ranking), [diag-b-12] (panel plus test choice, unablated), [diag-d-03].
- Risk: the only support for the panel idea is a vendor preprint with no equal-compute ablation [diag-d-03]. Partial or badly set-up schemas may score below none [diagnostic-c-23, diagnostic-c-22].

**M3. Conditional reflection pass.**
- Trigger: only when a real signal fails: a check does not pass, attempts split, or the case is flagged complex.
- Action: one structured pass that reads the input again and names what the current answer fails to explain, with permission to keep the answer.
- Check: compare revision outcomes. Count corrections against backfires; require corrections to exceed backfires at equal tokens.
- Evidence: positive on complex cases [diag-a-13, diag-a-12]; null or negative unconditionally [diag-a-03, diagnostic-c-05].
- Risk: in the human data unstructured reflection corrected 14 to 16 and broke 14 to 26 [diagnostic-c-05]. Our own always-on doubt cost accuracy [ours]. If it cannot be tied to a hard-case trigger, drop it.

**M4. Keep the first answer unless a check overturns it.**
- Trigger: always, as the default rule; it replaces reflection on simple items.
- Action: the program stores the first answer and only replaces it with a candidate that passes a check that reads the real input.
- Check: plain model at equal tokens on single-answer sets (ARC, word puzzles) where the scaffold lost.
- Evidence: [diag-a-02, diag-a-14, diag-a-03, diagnostic-c-05].
- Risk: low. It can freeze a wrong first answer when no check exists. Premature closure is the commonest human failure [diag-a-01], so pair it with M1 when attempts disagree.

**M5. Agreement, not self-stated confidence, as the hardness signal.**
- Trigger: the probe step.
- Action: gate escalation on disagreement among several plain attempts, and on whether time or length ran long, not on the model saying "I am sure".
- Check: correlation between agreement and correctness on a held-out set, against the correlation for stated confidence.
- Evidence: [diag-a-10, diag-a-08] (human confidence is weak); wrong answers took longer than right ones [diag-d-01].
- Risk: samples from one model are correlated, so agreement is weak evidence [ours]. No LLM calibration test for diagnosis was found.

**M6. Choice shuffle for multiple-choice and ranked items.**
- Trigger: closed-option questions.
- Action: ask the same question with the options in different orders and combine.
- Check: equal-token plain majority of unshuffled samples.
- Evidence: [diag-b-14, diagnostic-c-24, diagnostic-c-18] (order sensitivity).
- Risk: which Medprompt part carried the gain is unknown [diagnostic-c-24]. Possible gain is mostly from removing position bias, not from thinking better.

**M7. Strip cue-bait before reasoning.**
- Trigger: input that contains another party's suggested answer, expert hint or consensus claim.
- Action: have the program remove or isolate such statements and run the reasoning blind to them, then compare.
- Check: accuracy on items with and without injected hints, at equal tokens.
- Evidence: [diag-a-20, diag-b-10, diagnostic-c-17, diagnostic-c-20].
- Risk: the hint may be informative. Blind runs cost tokens. Bias-awareness prompts alone recovered little for weak models [diag-b-11], so use isolation, not a warning.

## 5. Evidence on LLMs and AI agents

- GPT-4 alone beat GPT-4-assisted doctors in the US trial (92% against 76%) [diag-a-18]. The human step was the weak link [diagnostic-c-15, diagnostic-c-16].
- On NEJM cases GPT-4 placed the final diagnosis in its list 64% of the time but first 39% [diag-a-19].
- Cognitive-bias cues lowered accuracy in all six models tested, most in small open ones [diag-a-20]. Misleading hints made models drop correct reasoning [diagnostic-c-20].
- On 2,400 real abdominal cases frontier LLMs trailed physicians and ignored guidelines [diagnostic-c-18].
- Orchestration (MAI-DxO) and prompt composition (Medprompt) report large gains, both from one preprint each, with the structure effect not separated from extra compute [diag-b-12, diag-d-03, diag-b-14, diagnostic-c-24].
- Partial or poorly configured prompt systems can do worse than none [diagnostic-c-23, diagnostic-c-22].
- AMIE rated above primary care physicians in simulated text chats [diag-a-21]; not about schema design.
- Coverage is thin: the search budget ran out in round b, and four planned delta searches were never run [diag-b-16, diag-d-05].

## 6. What does not transfer to a model

- Teaching effects. Workshops, debiasing lessons and illness-script training change what a person knows and notices [diag-a-06, diag-a-17]. A model is not taught between calls, so these findings only say what prompts to avoid.
- Fatigue, time pressure and emotion as causes of error. The case-series errors mix system and cognitive causes [diag-a-01]; the system part is about workflow and has no model analogue.
- Human knowledge gaps. In the case series knowledge gaps were rare [diag-a-01]. A small model may have more of them, so "the doctor knew it and slipped" may not hold.
- Patient outcomes, cost to health systems and error rates in visits [diag-a-09]. Context, not design input.
- Human-plus-LLM collaboration results [diag-a-18, diagnostic-c-21]. Our agent is a program using the model's output directly.
- Answer-switch behavior of students and residents on written vignettes [diagnostic-c-05]. The count of corrections against backfires must be re-measured on the model.

## 7. Open questions

1. Does an LLM that writes a differential and then picks a discriminating check beat equal-token voting? No evidence found for either side; this decides M1 and M2 [diag-d-03].
2. When does a second opinion help: independent or anchored? Planned search not run [diag-d-05].
3. Does LLM agreement or stated confidence predict correctness on diagnosis, for open models near our size? Not run [diag-d-05].
4. Does the Kammer list result replicate, and does it hold for an LLM-built list? Not run [diag-d-05]. M1 depends on it.
5. Is the Mamede reflection effect real, and is its condition (complex or similar-to-earlier cases) detectable by a program? Snippet only [diag-a-12, diag-a-13, diag-d-05].
6. How much of MAI-DxO's gain comes from structure and how much from extra compute? [diag-d-03]
7. Which Medprompt component matters, and is choice shuffle enough alone? [diagnostic-c-24]
8. What base rate of "first answer right" can the router use? Medicine gives no clean number; the best proxy is that difficulty, not instruction, drives accuracy [diag-a-14, diag-a-10].
9. How much does a wrong hint hurt a small open model under a scaffold? BiasMedQA and the test-time scaling abstract cover related ground only [diag-a-20, diagnostic-c-20].

## 8. References

How checked: fetched = page opened; abstract = abstract or record opened; snippet = search result text only; memory = recalled, not opened.

1. Graber ML, Franklin N, Gordon R. 2005. Diagnostic error in internal medicine. Archives of Internal Medicine 165(13):1493-1499. https://pubmed.ncbi.nlm.nih.gov/16009864/ (abstract) [diag-a-01, diag-b-07, diagnostic-c-11]
2. Norman G, Sherbino J, Dore K, Wood T, Young M, Gaissmaier W, Kreuger S, Monteiro S. 2014. The etiology of diagnostic errors: a controlled trial of system 1 versus system 2 reasoning. Academic Medicine 89(2):277-284. https://pubmed.ncbi.nlm.nih.gov/24362377/ (fetched, summary only) [diag-a-02, diag-b-01, diag-d-01, diagnostic-c-02]
3. Monteiro SD, Sherbino J, et al. 2015. Reflecting on diagnostic errors: taking a second look is not enough. Journal of General Internal Medicine 30. https://pmc.ncbi.nlm.nih.gov/articles/PMC4539330 (fetched) [diag-a-03, diag-b-02, diag-b-03, diagnostic-c-01]
4. Kammer JE, Schauber SK, et al. 2021. Differential diagnosis checklists reduce diagnostic error differentially. Medical Education 55(10):1172-1182. https://pmc.ncbi.nlm.nih.gov/articles/PMC9290564/ (fetched) [diag-a-04, diag-b-05, diagnostic-c-06]
5. Lambe KA, O'Reilly G, Kelly BD, Curristan S. 2016. Dual-process cognitive interventions to enhance diagnostic reasoning: a systematic review. BMJ Quality & Safety 25(10):808-820. https://qualitysafety.bmj.com/content/25/10/808 (abstract) [diag-a-05, diagnostic-c-09]
6. Norman GR, Monteiro SD, Sherbino J, et al. 2017. The causes of errors in clinical reasoning: cognitive biases, knowledge deficits, and dual process thinking. Academic Medicine 92(1):23-30. https://doi.org/10.1097/ACM.0000000000001421 (abstract) [diag-a-06]
7. Sibbald M, Sherbino J, Ilgen JS, et al. 2019. Debiasing versus knowledge retrieval checklists to reduce diagnostic error in ECG interpretation. Advances in Health Sciences Education 24(3):427-440. https://pubmed.ncbi.nlm.nih.gov/30694452/ (abstract) [diag-a-07, diag-b-06, diagnostic-c-07]
8. Saposnik G, Redelmeier D, Ruff CC, Tobler PN. 2016. Cognitive biases associated with medical decisions: a systematic review. BMC Medical Informatics and Decision Making. https://europepmc.org/articles/PMC5093937 (abstract) [diag-a-08]
9. Singh H, Meyer AN, Thomas EJ. 2014. The frequency of diagnostic errors in outpatient care. BMJ Quality & Safety 23(9):727-731. https://qualitysafety.bmj.com/content/23/9/727 (abstract) [diag-a-09]
10. Meyer AN, Payne VL, Meeks DW, et al. 2013. Physicians' diagnostic accuracy, confidence, and resource requests. JAMA Internal Medicine 173(21):1952-1958. https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/1730890 (abstract) [diag-a-10]
11. Berner ES, Graber ML. 2008. Overconfidence as a cause of diagnostic error in medicine. American Journal of Medicine 121(5 Suppl). https://doi.org/10.1016/j.amjmed.2008.01.001 (abstract) [diag-a-11]
12. Mamede S, van Gog T, et al. 2010. Effect of availability bias and reflective reasoning on diagnostic accuracy among internal medicine residents. JAMA 304(11):1198-1203. https://jamanetwork.com/journals/jama/fullarticle/186559 (snippet) [diag-a-12]
13. Mamede S, Schmidt HG, et al. 2008. Effects of reflective practice on the accuracy of medical diagnoses. Medical Education 42(5). https://doi.org/10.1111/j.1365-2923.2008.03030.x (snippet) [diag-a-13]
14. Ilgen JS, Bowen JL, McIntyre LA, et al. 2013. Comparing diagnostic performance and the utility of clinical vignette-based assessment under testing conditions designed to encourage either automatic or analytic thought. Academic Medicine 88(10):1545-1551. https://doi.org/10.1097/ACM.0b013e3182a3167a (abstract) [diag-a-14]
15. Mamede S, van Gog T, Moura AS, et al. 2012. Reflection as a strategy to foster medical students' acquisition of diagnostic competence. Medical Education 46(5). https://doi.org/10.1111/j.1365-2923.2012.04217.x (snippet) [diag-a-15]
16. Custers EJFM. 2015. Thirty years of illness scripts: theoretical origins and practical applications. Medical Teacher. https://doi.org/10.3109/0142159X.2014.956052 (abstract) [diag-a-16]
17. Lee A, Joynt GM, Lee AK, et al. 2010. Using illness scripts to teach clinical reasoning skills to medical students. Family Medicine. https://europepmc.org/search?query=%22illness%20scripts%22%20Lee%202010 (snippet) [diag-a-17]
18. Goh E, Gallo R, Hom J, et al. 2024. Large language model influence on diagnostic reasoning: a randomized clinical trial. JAMA Network Open 7(10):e2440969. https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395 (fetched) [diag-a-18, diag-b-09, diagnostic-c-14]
19. Kanjee Z, Crowe B, Rodman A. 2023. Accuracy of a generative artificial intelligence model in a complex diagnostic challenge. JAMA 330(1):78-80. https://pmc.ncbi.nlm.nih.gov/articles/PMC10273128 (fetched) [diag-a-19, diag-b-08, diagnostic-c-13]
20. Schmidgall S, Harris C, Essien I, et al. 2024. Evaluation and mitigation of cognitive biases in medical language models. npj Digital Medicine 7:295. https://pmc.ncbi.nlm.nih.gov/articles/PMC11494053/ (fetched) [diag-a-20, diag-b-10, diag-b-11, diagnostic-c-17]
21. Tu T, Schaekermann M, Palepu A, et al. 2025. Towards conversational diagnostic artificial intelligence. Nature 642:442-450. https://doi.org/10.1038/s41586-025-08866-7 (abstract) [diag-a-21]
22. Elstein AS, Shulman LS, Sprafka SA. 1978. Medical Problem Solving: An Analysis of Clinical Reasoning. Harvard University Press. https://www.hup.harvard.edu/books/9780674561250 (memory) [diag-a-22]
23. Nori H, Daswani M, Kelly C, Lundberg S, Ribeiro MT, Wilson M, et al. 2025. Sequential Diagnosis with Language Models. arXiv 2506.22405 (preprint). https://arxiv.org/abs/2506.22405 (abstract; one earlier line marked fetched) [diag-a-23, diag-b-12, diag-b-13, diagnostic-c-19, diag-d-02, diag-d-03]
24. Nori H, Lee YT, Zhang S, et al. 2023. Can generalist foundation models outcompete special-purpose tuning? Case study in medicine. arXiv 2311.16452 (preprint). https://arxiv.org/abs/2311.16452 (abstract; fetched in round c) [diag-b-14, diagnostic-c-24]
25. Lambe KA, Hevey D, Kelly BD. 2018. Guided reflection interventions show no effect on diagnostic accuracy in medical students. Frontiers in Psychology 9:2297. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.02297/full (fetched) [diag-b-04, diagnostic-c-04, diagnostic-c-05]
26. Smith BW, Slack MB. 2015. The effect of cognitive debiasing training among family medicine residents. Diagnosis 2(2):117-121. https://doi.org/10.1515/dx-2015-0007 (abstract) [diagnostic-c-08]
27. Tung A, Melchiorre M. 2022. Debiasing and educational interventions in medical diagnosis: a systematic review. medRxiv (preprint). Europe PMC record, see evidence_c (abstract) [diagnostic-c-10]
28. Norman G. 2009. Dual processing and diagnostic errors. Advances in Health Sciences Education. Europe PMC record, see evidence_c (abstract) [diagnostic-c-12]
29. Healy J, Kossoff J, Lee M, et al. 2026. Human-AI collaboration in clinical reasoning: a UK replication. Diagnosis (Berl). Europe PMC record, see evidence_c (abstract) [diagnostic-c-15]
30. Ong KT, Seo J, Kim H, et al. 2026. Success and failure of human-AI collaboration in clinical reasoning. International Journal of Medical Informatics 211:106342. Europe PMC record, see evidence_c (abstract) [diagnostic-c-16]
31. Hager P, et al. 2024. Evaluation and mitigation of the limitations of large language models in clinical decision-making. Nature Medicine 30(9):2613-2622. Europe PMC record, see evidence_c (abstract) [diagnostic-c-18]
32. Oh G, Kim S, Park S, Kim, et al. 2026. Test-time scaling in medical LLMs and VLMs. Journal of Medical Internet Research 28:e90693. https://doi.org/10.2196/90693 (abstract) [diagnostic-c-20]
33. Cusacovich I, Pinilla M, et al. 2026. Real-time artificial intelligence diagnostic copilot in simulated primary care. JMIR Formative Research. Europe PMC record, see evidence_c (abstract) [diagnostic-c-21]
34. Li Z, Liu H, Tan W, et al. 2026. Multitype prompt engineering for hypertension treatment decisions. npj Digital Medicine 9(1):526. https://doi.org/10.1038/s41746-026-02645-y (abstract) [diagnostic-c-22]
35. Fan B, Fang Y, Wang Z, Ma, et al. 2026. TCM-CoT-RAG. Frontiers in Pharmacology 17:1884526. https://doi.org/10.3389/fphar.2026.1884526 (abstract) [diagnostic-c-23]
