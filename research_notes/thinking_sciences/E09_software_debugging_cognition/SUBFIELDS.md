# Software debugging cognition: subfields

This field studies how programmers find why a program misbehaves: what they hypothesise, read and run, and where thinking breaks down. It divides into process models, studies of hypotheses and mental models, tool research, automated fault localisation, teaching, and LLM debugging. One answer (the defect) and a real check (tests pass) make it a close fit.

Opened facts, two primary studies.

Alaboudi and LaToza 2020, Using Hypotheses as a Debugging Aid: a within-subjects lab study with 20 developers. Developers formed few hypotheses, about two per defect. A correct hypothesis early predicted later success. Offering fault locations did not help; offering potential hypotheses made developers about six times more likely to succeed. This directly shows that hypothesis generation, not location, is the barrier.

Li and Coblenz 2026, A Grounded Theory of Debugging in Professional Practice: 7 professionals thinking aloud, 5 streamers, 17 tasks, about 11 hours. Four steps: reproduce (about 12% of time), mental model development (about 57%), work on fix (about 13%), validate fix (about 18%). Developers rarely stated formal testable hypotheses; they held vague speculations and tracked uncertainty, building a "good-enough" model. Interview accounts of scientific-method debugging differ from observed behaviour.

Together: a hypothesis is a scarce resource that succeeds when correct, yet real debugging is looser than the textbook method. Fixation on one hypothesis (Ko and Myers, reported in a search snippet only) was not verified by me.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Cognitive breakdowns | Chain from slip to defect | Ko and Myers 2005 | High | G2, G3 (not opened) |
| Hypotheses in debugging | Generation and quality | Alaboudi and LaToza 2020 | High | S3, S4; six-fold gain from supplied hypotheses |
| Mental model of the system | Evidence gathering to build it | Li and Coblenz 2026 | High | S2 as a running model; S6 |
| Debugging as scientific method | Hypothesis, prediction, experiment | Zeller 2009; Whyline | High | Predict-then-observe check |
| Program comprehension | Reading strategies | Brooks; Letovsky; ICSE 2025 | Med | Episode labels |
| Tools and questions | Why/why-not, slicing | Ko and Myers; Weiser 1982 | Med | O5 backwards from the failure |
| Fault localisation and repair | Spectrum, mutation, repair | Jones and Harrold; Le Goues | High | Code locates (G2) |
| Novices and education | Misconceptions | Murphy et al. 2008 | Low | Background |
| LLM debugging | Self-debugging, SWE-bench | Chen et al.; Jimenez et al. | High | Direct evidence (from memory) |
| Verbalisation (rubber duck) | Explaining code aloud | Folklore | Low | Contrast with 4b |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding. The field synthesis is [`SYNTHESIS.md`](SYNTHESIS.md).

| Subfield | Deep document | Status |
|---|---|---|
| Cognitive breakdowns | | not started |
| Hypotheses in debugging | [`subfields/02_hypotheses_in_debugging/DEEP.md`](subfields/02_hypotheses_in_debugging/DEEP.md) | done, batch 3 (2026-10-26) |
| Mental model of the system | | not started |
| Debugging as scientific method | | not started |
| Program comprehension | | not started |
| Tools and questions | | not started |
| Fault localisation and repair | | not started |
| Novices and education | | not started |
| LLM debugging | [`subfields/09_llm_debugging/DEEP.md`](subfields/09_llm_debugging/DEEP.md) | done, batch 3 (2026-10-26) |
| Verbalisation (rubber duck) | | not started |

## Dig into next

**1. Hypotheses supplied as an aid.**
- If supplied hypotheses give a six-fold gain, does a model that generates many independent hypotheses and a program that tests each reproduce it?
- Evidence: Alaboudi and LaToza task set, an LLM test on bug benchmarks at equal tokens.

**2. Vague speculation versus formal hypothesis.**
- Does forcing a written prediction before each run help an LLM, as scientific-method advice says, when professionals do not do it?
- Evidence: Li and Coblenz, equal-token test with code comparing prediction to output.

**3. Mental-model-first phase.**
- Professionals spent about 57% of time on the model. Does a cheap model-building phase (trace, version history) raise success?
- Evidence: Li and Coblenz phase data, our logs.

## Does not transfer

Asking colleagues, reading issue threads, frustration, streaming culture and large-codebase navigation over weeks are human. Tool studies measure human interface use. Novice misconceptions differ from model errors. The hypothesis study used 20 developers on specific defects; results may not generalise.

## Sources

[V] = opened and read this session. [M] = search result only, or from memory. Two further searches were refused (budget exhausted). Opened: 2.

1. Alaboudi and LaToza 2020, Using Hypotheses as a Debugging Aid, arXiv 2005.13652 (abstract and PDF text read). https://arxiv.org/abs/2005.13652 [V]
2. Li and Coblenz 2026, grounded theory of debugging, arXiv 2602.11435 (first 100,000 characters read). https://arxiv.org/html/2602.11435v1 [V]
3. Ko and Myers framework (summary PDF; fetch failed: certificate error). https://people.cs.gmu.edu/~tlatoza/teaching/swe795s17/paperSummaries/A%20Framework%20and%20Methodology.pdf [M]
4. Ko, ICSE 2018 slides (fetch too large). https://faculty.washington.edu/ajko/slides/ICSE2018MIP.pdf [M]
5. ICSE 2025 cognitive model of dynamic debugging. https://conf.researchr.org/details/icse-2025/icse-2025-journal-first-papers/23/Towards-a-Cognitive-Model-of-Dynamic-Debugging-Does-Identifier-Construction-Matter- [M]
6. Zeller 2009, Why Programs Fail. [M]
7. Weiser 1982, Programmers use slices when debugging, CACM. [M]
