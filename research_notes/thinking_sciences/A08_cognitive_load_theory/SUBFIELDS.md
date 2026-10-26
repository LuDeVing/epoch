# Cognitive load theory: subfields

Cognitive load theory (CLT) is an instructional theory developed by John Sweller in the late 1980s. It starts from a small working memory and a large long-term memory, and asks how to design material so limited processing goes to what matters. It divides by kind of load (intrinsic, extraneous, germane), by the effects that follow (worked example, split attention, redundancy, expertise reversal) and by the key variable, element interactivity: how many elements must be processed together. Its direct value for us is a way to size tasks and prompts.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Intrinsic load and element interactivity | Inherent difficulty of the topic; complexity as the number of interacting elements [V1; M for definition] | Sweller (1994, 2010); Sweller, Ayres, Kalyuga (2011) [M] | High | S0 gate and O3 decompose: split until each part has few interacting elements |
| Extraneous load and split attention | Load caused by presentation; learners must mentally integrate separated sources [V1] | Chandler and Sweller (1992) | High | prompt design: integrate, drop irrelevant text |
| Worked-example effect | Best-known CLT effect: worked examples cut extraneous load early in skill acquisition [V2] | Sweller and Cooper (1985); Renkl; Schwonke et al. (2009) | High | memory: subgoal library |
| Expertise reversal | Support helps novices, hurts experts; found in mechanics, circuits, programming; fix by fading [V2]. One 2016 paper argues it is a case of element interactivity [M, search snippet] | Kalyuga et al. (2003); Chen, Kalyuga and Sweller (2016) [M] | High | S0: fade help as the class pass rate rises |
| Germane load | Working memory devoted to building schemas [V1] | Sweller; Paas | Low | disputed |
| Measurement of load | Rating scales (NASA-TLX), dual task, physiology; different measures respond to different load types; lab correlations did not hold outside the lab [V1] | Paas and van Merrienboer (relative condition efficiency); Hart and Staveland; Deleeuw and Mayer (2008); Skulmowski and Rey (2020) | Low | use tokens and accuracy instead |
| Critiques of the three-load model | Additivity questioned; load types influence each other circularly; need clearer distinctions [V1] | De Jong (2009) | Med | caution on overstated claims |
| Working-memory limits and chunking | Miller (1956) seven plus or minus two; chunk idea from Chase and Simon (1973) [V1] | Miller; Baddeley and Hitch | Med | context-budget analogy only |
| Collective working memory and evolutionary educational psychology | [M] | Kirschner, Paas; Geary | Low | does not apply to one agent |
| Task-type limits | Worked examples suit well-structured tasks; less effective for creative or less-structured tasks [V2] | Nievelstein et al. (2013) | Med | open mode needs other support |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Intrinsic load and element interactivity | [`subfields/01_intrinsic_load_and_element_interactivity/DEEP.md`](subfields/01_intrinsic_load_and_element_interactivity/DEEP.md) | done, batch 5 (2026-10-27) |
| Extraneous load and split attention | | not started |
| Worked-example effect | | not started |
| Expertise reversal | | not started |
| Germane load | | not started |
| Measurement of load | | not started |
| Critiques of the three-load model | | not started |
| Working-memory limits and chunking | | not started |
| Collective working memory and evolutionary educational psychology | | not started |
| Task-type limits | | not started |

## Dig into next

1. **Element interactivity.** Questions: (a) Can code compute a proxy (number of interacting constraints or objects) that predicts the plain model's failure better than text length? (b) Is there a threshold above which O3 decomposition pays? (c) Is the primary definition in Sweller's papers consistent with this? (not opened; Wikipedia's page does not define it). Evidence: graded item set with plain pass rates.
2. **Expertise reversal and fading.** Questions: (a) Is there a cross-over in our logs where lessons help weak classes and hurt strong ones? (b) What fading schedule did Renkl and Kalyuga use? Evidence: library on/off by class pass rate.
3. **Extraneous load: split attention.** Questions: (a) Does integrating labels or examples with the rule text change accuracy? (b) Does removing redundant restatements help? Evidence: prompt-format ablations at equal tokens.

## Does not transfer

A model has no fixed seven-item working memory. Its limits are context length and attention dilution. Subjective load ratings, physiological measures, germane load and collective working memory are about people. Treat CLT as a design heuristic to test, and note that its central constructs are contested.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only. Only two pages were opened for this field; the main CLT papers could not be opened (403 or unreadable PDF).

1. [V] Cognitive load, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Cognitive_load
2. [V] Worked-example effect, Wikipedia: https://en.wikipedia.org/wiki/Worked-example_effect
3. [M] Chen et al., expertise reversal as element interactivity: https://repository.lboro.ac.uk/articles/The_expertise_reversal_effect_is_a_variant_of_the_more_general_element_interactivity_effect/12052695 (403)
4. [M] Kalyuga (2007) Educational Psychology Review 19(4), listed in search: https://www.uky.edu/~gmswan3/EDC608/Kalyuga2007_Article_ExpertiseReversalEffectAndItsI.pdf (certificate error)
5. [M] Sweller (1988); Sweller, Ayres, Kalyuga (2011); Kalyuga et al. (2003). No URLs.
