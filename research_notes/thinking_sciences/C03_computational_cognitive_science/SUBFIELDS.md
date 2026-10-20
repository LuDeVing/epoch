# Computational cognitive science: subfields

This field builds mathematical or program models of human thinking and tests them on behaviour. It divides by model type: Bayesian (thinking as inference), program induction (thinking as search for short programs), connectionist, and rational-analysis models that ask what is optimal given limited resources. For us the strongest strands are library learning (a memory of solved subgoals) and resource rationality (how much to think). Marks: [V] = page opened this session; [M] = from memory or seen only in a search result. Only two sources in this file were opened; the topic needs more reading.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Bayesian models of cognition | Beliefs updated by evidence with priors | Tenenbaum, Griffiths, Kemp [M] | Med | background; selection by prior and fit |
| Program induction, language of thought | Concepts as short programs | Piantadosi; Goodman [M] | High | S2 REPRESENT, S3 GENERATE |
| Library learning, wake-sleep | Learning reusable abstractions and a search policy from solved tasks | DreamCoder, arXiv 2006.08381 [V] | High | memory: subgoal library |
| Language-guided library learning | LLM search, symbolic compression, auto-documentation | LILO, arXiv 2310.19791 [V] | High | memory with names a model can read |
| Resource-rational analysis | Optimal use of limited computation | Lieder, Griffiths [M] | High | S0 gate |
| Rational strategy selection | Learning which strategy pays when | Lieder and Griffiths [M] | High | operator choice at S6 |
| Probabilistic programming | Languages for models (Church, WebPPL) | Goodman et al. [M] | Low | background only |
| Intuitive theories and simulation | Physics and psychology as simulation | Battaglia, Tenenbaum [M] | Low | background only |
| Metacognition models | Confidence and monitoring | Fleming [M] | Med | guardrail on stated confidence |
| LLMs as cognitive subjects | Testing models with experiments | Binz and Schulz [M] | Low | background only |

## Dig into next

1. **Library learning.** How does the abstraction step decide a fragment is worth keeping (compression gain over solved tasks, using the STITCH compressor in LILO)? Can the same step run on our solved subgoals as helper programs? Does a library raise later solve rates at equal tokens? Evidence: LILO ablations (below); our before/after pass rate on held-out problems of one class.
2. **Resource-rational strategy selection.** Which cheap cue predicts that a strategy will pay? Can S0 be a table of expected gain minus cost per class? Evidence: class records from our logs; Lieder and Griffiths model form (not yet opened).
3. **Program induction as representation.** When is a rule stated as code better than as words at S2? Evidence: our ARC runs, where programs that fit every example were still wrong (G3).

## Combined with LLMs

- LILO (Grand et al., arXiv 2310.19791), full text read in part. LLM-guided search used Codex (code-davinci-002); auto-documentation used gpt-3.5-turbo. Benchmarks: string editing (REGEX), scene reasoning (CLEVR), graphics (LOGO). Online mean solve rate: DreamCoder 43.93 / 94.50 / 28.53; LILO 77.07 / 96.76 / 48.95 (a gain of +33.14, +2.26, +20.42). The best LLM-only solver with search scored 76.60 / 96.44 / 37.84, so on REGEX and CLEVR most of the gain comes from the LLM, and the library adds a margin (and +11 on LOGO). Removing auto-documentation cost 9.73 points on REGEX, 2.27 on CLEVR, 0 on LOGO. Offline with the final library: LILO 64.27 / 92.56 / 41.14 against DreamCoder 41.60 / 91.59 / 30.63 [V].
- DreamCoder (arXiv 2006.08381): abstract only; it rediscovers parts of functional programming and physics laws; no numbers on the page [V].
- I could not run the planned extra searches (search quota used up), so resource-rationality work with LLMs is untested here.

## Sources

1. https://arxiv.org/abs/2006.08381 [V] DreamCoder abstract
2. https://arxiv.org/html/2310.19791v2 [V] LILO full text (first part)
3. https://arxiv.org/abs/2310.19791 [V] LILO abstract
4. https://pldi21.sigplan.org/details/pldi-2021-papers/55/DreamCoder-Bootstrapping-Inductive-Program-Synthesis-with-Wake-Sleep-Library-Learnin [M] DreamCoder PLDI page
5. Lieder and Griffiths 2020, Resource-rational analysis; Tenenbaum et al. 2011, How to grow a mind [M] (no URL)
