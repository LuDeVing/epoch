# Medical diagnostic reasoning: subfields

Diagnostic reasoning research asks how clinicians get from signs to a working diagnosis, and why they sometimes err. It divides into the early hypothetico-deductive model, knowledge-structure theories (scripts, categories), dual-process and bias research, error and debiasing studies, and tests of LLMs on cases. The fit with our agent is strong: one answer, a later check, and trained procedures. The review by Monteiro and Norman (2013), which I opened, gives the key warning: strategies that tell students to slow down, use System 2 or be aware of biases showed no effect on error rates, while strategies that add relevant knowledge had some success.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Hypothetico-deductive model | Early hypotheses (a few) guide data search | Elstein, Shulman, Sprafka 1978 | Med | S3 generate, S4 test. Review says it was dropped in the 1980s: experts did not generate more hypotheses, only better ones, so the gain was in content knowledge |
| Forward and backward reasoning | Experts reason data to diagnosis, novices hypothesis to data | Patel and Groen | Low | Background only; link to the expertise artefact is doubted |
| Knowledge organisation: illness scripts, categories | Diagnosis as recognition from rich stored knowledge | Schmidt and Rikers; Charlin; Norman | High | Memory (class library), S2 represent |
| Dual-process theory | Fast retrieval against slow analysis | Croskerry; Evans; Kahneman | Med | S0 mode choice. Default-interventionist form is criticised in the review |
| Cognitive bias and premature closure | Anchoring, early stopping; mostly missed common diseases | Graber et al. 2005; Croskerry | Med | Not-to-add list (4b) |
| Debiasing and cognitive forcing | Slow down, bias awareness, checklists | Croskerry 2003; Norman et al. | Med | Evidence: no impact on error rate in review. Guardrail G1 |
| Reflective reasoning and second look | Structured re-examination of a case | Mamede, Schmidt | High | S5 revise, S8 verify (not searched further, see Sources) |
| Probabilistic and test-based reasoning | Likelihood ratios, test thresholds | Sox; Pauker and Kassirer | High | S7 discriminating test; G5 code normalises |
| Clinical decision support and LLMs | Differential generators, LLMs vs physicians | Goh et al. 2024 | High | Direct LLM evidence |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Hypothetico-deductive model | | not started |
| Forward and backward reasoning | | not started |
| Knowledge organisation: illness scripts, categories | | not started |
| Dual-process theory | | not started |
| Cognitive bias and premature closure | | not started |
| Debiasing and cognitive forcing | | not started |
| Reflective reasoning and second look | [`subfields/07_reflective_reasoning_and_second_look/DEEP.md`](subfields/07_reflective_reasoning_and_second_look/DEEP.md) | done, batch 5 (2026-10-27) |
| Probabilistic and test-based reasoning | | not started |
| Clinical decision support and LLMs | | not started |

## Dig into next

**1. Knowledge-based strategies over process instructions.**
- Which knowledge structures (contrast tables, script fields) improved accuracy in teaching trials, and by how much?
- Can an LLM be given a retrieved script after its first attempt and fix errors without new anchoring?
- Evidence: Monteiro and Norman's cited trials, then an equal-token test with lessons shown after the first attempt (schema section 5).

**2. Reflective reasoning and second look.**
- Does structured re-examination help on hard cases only?
- Does it help when the reviewer sees no first answer (schema G5)?
- Evidence needed: the Mamede and Schmidt randomised studies (not opened; my extra searches were refused by the session search budget), effect sizes by difficulty.

**3. Test selection by separation.**
- How do clinicians choose the next test, and is "split the candidates" better than "confirm the favourite"?
- Evidence: Elstein protocols, test-threshold studies, LLM trials with known diagnoses.

## Does not transfer

Patient talk, exam by hand, emergency room time pressure, lost results, fatigue and malpractice culture are about people and institutions. In Goh et al. 2024 (50 physicians, 60 minutes, up to 6 vignettes), giving physicians an LLM did not raise their score (76% against 74%, adjusted difference 2 points, 95% CI -4 to 8). The LLM alone scored 16 points higher than the conventional-resource group (CI 2 to 30). That is a human-AI teaming result, not an agent-alone one.

## Sources

[V] = page opened and read this session. [M] = seen only in a search result, or from memory. Two further searches for this field were refused (shared session search budget exhausted). Opened: 2.

1. Monteiro and Norman 2013, Diagnostic reasoning: where we have been, where we are going. https://wikiMSK.org/w/img_auth.php/b/b5/Monteiro2013_Diagnostic_Reasoning_Where_We%27ve_Been%2C_Where_We%E2%80%99re_Going.pdf [V] (text read from the saved PDF)
2. Goh et al. 2024, JAMA Netw Open 7(10):e2440969 (abstract page). https://experts.umn.edu/en/publications/large-language-model-influence-on-diagnostic-reasoning-a-randomiz/ [V]
3. AAMC, We all make diagnostic errors (page failed to load when opened). https://www.aamc.org/news-insights/we-all-make-diagnostic-errors [M]
4. JAMA Viewpoint on illness scripts (search result only). https://jamanetwork-com.libproxy.ajou.ac.kr/journals/jama/fullarticle/2839306 [M]
5. Elstein, Shulman, Sprafka 1978, Medical Problem Solving. [M]
6. Graber, Franklin, Gordon 2005, Diagnostic error in internal medicine. [M]
7. Mamede and Schmidt, reflective practice studies. [M]
