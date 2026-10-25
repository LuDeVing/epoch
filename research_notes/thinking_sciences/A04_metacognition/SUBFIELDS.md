# Metacognition: subfields

Metacognition is thinking about and controlling one's own thinking. Flavell (1979) coined it; Nelson and Narens added the key frame: an object level and a meta level joined by monitoring (information up) and control (commands down). The field divides by what is monitored (learning, memory retrieval, confidence), by the kind of knowledge (declarative, procedural, conditional), by regulation (planning, monitoring, evaluating), and by how accurate the monitoring is.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Monitoring and control framework | Object and meta level; monitoring up, control down, during acquisition, retention, retrieval [V1] | Nelson and Narens (1990, 1994) | High | structure of S6: code monitors, model acts |
| Metamemory judgments | Ease-of-learning (before), judgments of learning (during), feeling of knowing (before retrieval or after failure), knowing that you do not know [V1] | Hart (1965); Koriat; Metcalfe | Med | S0 gate (will this class be easy?) |
| Accuracy and dissociation of monitoring | Feeling of knowing is accurate when partial information is; judgments can dissociate from memory (altitude lowers FOK, not recall) [V1] | Hart; Nelson | High | evidence for G10: do not trust self-report; build signals in code |
| Metacognitive knowledge: declarative, procedural, conditional | Knowing what, how and when/why to use a strategy [V2] | Flavell; Schraw | Med | class record: which operator for which class |
| Metacognitive regulation | Planning, monitoring progress, evaluating; self-questions such as "Is it getting me anywhere?" [V2] | Perkins and Salomon; Swanson (1990): metacognition compensated for lower IQ and prior knowledge | High | S6 trigger and review; but note effect is human-trained |
| Confidence and signal-detection measures | Bias, sensitivity, efficiency of confidence [V2] | Fleming and Lau; Koriat | High | confidence from consistency of samples, by code |
| Meta-reasoning | Feeling of rightness, when to rethink or stop [M] | Ackerman and Thompson (meta-reasoning framework) | High | G1 doubt only on signal; S6 |
| LLM metacognitive harness | A harness separating monitoring from reasoning: use pre-task and post-answer self-assessments to decide to trust, retry with compact feedback, or aggregate; Claude Sonnet 4.6 pooled accuracy 48.3 to 56.9, as reported by the authors [V3] | Cao et al. (2026) | High | S0, S6, S7; single source, test at equal tokens |
| Social, organisational and clinical metacognition | Beliefs about others' minds; metacognitive therapy [V2] | Wells; Demetriou | Low | does not transfer |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Monitoring and control framework | | not started |
| Metamemory judgments | | not started |
| Accuracy and dissociation of monitoring | [`subfields/03_accuracy_and_dissociation_of_monitoring/DEEP.md`](subfields/03_accuracy_and_dissociation_of_monitoring/DEEP.md) | done, batch 3 (2026-10-26) |
| Metacognitive knowledge: declarative, procedural, conditional | | not started |
| Metacognitive regulation | | not started |
| Confidence and signal-detection measures | | not started |
| Meta-reasoning | | not started |
| LLM metacognitive harness | [`subfields/08_llm_metacognitive_harness/DEEP.md`](subfields/08_llm_metacognitive_harness/DEEP.md) | done, batch 3 (2026-10-26) |
| Social, organisational and clinical metacognition | | not started |

## Dig into next

1. **Monitoring accuracy and cheap signals.** Questions: (a) Which signals (token count, agreement across 3 short samples, answer entropy, pre-task self-rating of solvability) predict that an attempt is right, per class? (b) Does the LLM harness's "know when it knows" claim hold on our suites, and does acting on it beat our impasse detector? (c) How does it square with G4 (samples correlated)? Evidence: logged attempts; replicate the harness idea at equal tokens; calibration curves.
2. **Metacognitive regulation and strategy choice.** Questions: (a) Which regulation decisions (plan, monitor, switch) are code-decidable? (b) Can conditional knowledge ("when does operator X work") be learned into the class record? Evidence: operator-by-class logs.
3. **Confidence measures (signal detection).** Questions: (a) What are the LLM equivalents of metacognitive sensitivity and efficiency? (b) Can they replace stated confidence in S7? Evidence: Fleming and Lau definitions applied to our logs.

## Does not transfer

Illusions of knowing driven by fluency feelings, self-efficacy, study motivation, classroom self-regulation, clinical and neurological impairments (Korsakoff's, frontal injury) and age effects are about people. A model has no felt sense of knowing; its stated confidence is not a monitoring signal. Use only the structure and build signals in code.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only.

1. [V] Metamemory, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Metamemory
2. [V] Metacognition, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Metacognition
3. [V] Cao et al., LLMs Know When They Know, but Do Not Act on It (abstract page): https://arxiv.org/abs/2605.14186
4. [M] Narens, Graf and Nelson (1996): https://sites.socsci.uci.edu/~lnarens/1996/NarensGrafNelson_Book%20Chapter_1996.pdf (PDF unreadable)
5. [M] Nelson and Narens (1990); Flavell (1979); Ackerman and Thompson (2017); Koriat (2012). No URLs.
