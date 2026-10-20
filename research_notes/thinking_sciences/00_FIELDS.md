# Sciences that study thinking: the catalogue

*Started 2026-10-20. Every field that studies how thinking works, or how people think well in a practice. Each field
will get its own folder here (`NN_slug/`) when we research it in depth. This file is the map: what exists, what we
already covered, and what to dig into next for the single-agent schema (`../single_agent/SCHEMA.md`).*

**Coverage**: **Deep** = an evidence-backed brief exists (`../single_agent/fields_v2/`, F01 to F12); **Light** = touched
in older notes; **None** = not researched yet.
**Priority for one agent**: **High** = likely to give a schema step or a control rule; **Med** = useful background or a
single mechanism; **Low** = mostly about traits, groups or the body, which do not transfer to a model.
**Found by** marks fields added after the web search of 2026-10-20 (sources at the end).

---

## A. Psychology and cognitive science

| # | Field | What it studies | Coverage | Priority |
|---|---|---|---|---|
| A1 | Cognitive psychology of thinking and reasoning | deduction, induction, mental models, content effects | Deep (F03) | High |
| A2 | Problem-solving research | problem spaces, means-ends analysis, insight, representation change | Deep (F03), Light | High |
| A3 | Judgment and decision making | heuristics and biases, risky choice, debiasing | Light (team notes) | Med |
| A4 | Metacognition | monitoring and control, feeling of rightness, when to stop or switch | Deep (F11) | High |
| A5 | Learning science | worked examples, productive failure, desirable difficulties, transfer | Deep (F11) | High (for memory) |
| A6 | Memory research | retrieval, schemas, interference, cue-dependent recall | Light (human_thought) | Med |
| A7 | Attention research | selection, capture by salient cues, cognitive load | Light | Med |
| A8 | Cognitive load theory | limits of working memory, element interactivity | Light | Med |
| A9 | Creative cognition | generate-and-explore, conceptual combination, fixation | Deep (F01) | High (open mode) |
| A10 | Psychology of creativity and expertise | Einstellung, chunking, deliberate practice, problem finding | Deep (F02) | Med |
| A11 | Analogy and categorisation research | structure mapping, schema induction, category learning | Light (team notes) | High |
| A12 | Psychology of insight | impasse, restructuring, constraint relaxation, chunk decomposition | Light (F03, F04) | High |
| A13 | Intelligence research (psychometrics) | fluid reasoning, working memory, what predicts problem solving | None | Low |
| A14 | Developmental cognitive science | children as scientists, exploration, theory change | Light (human_thought) | Med |
| A15 | Psycholinguistics, language and thought | how wording changes reasoning, framing effects | Light | Med |
| A16 | Embodied and situated cognition | thinking through the body and environment | Light | Low |
| A17 | Social cognition and collective intelligence | group reasoning, conformity, wisdom of crowds | Light (team notes) | Low (one agent) |
| A18 | Comparative cognition | problem solving in animals, tool use, causal reasoning | None | Low |
| A19 | Cross-cultural cognition | holistic and analytic thinking styles across cultures | None | Low |
| A20 | Psychology of programming *(found by)* | how programmers comprehend, plan and debug code | None | High |

## B. Neuroscience

| # | Field | What it studies | Coverage | Priority |
|---|---|---|---|---|
| B1 | Cognitive neuroscience of creativity and insight | default and control networks, insight signatures | Deep (F04) | Med |
| B2 | Neuroscience of decision making (neuroeconomics) | valuation, exploration and exploitation in the brain | None | Low |
| B3 | Predictive processing and active inference | the brain as a prediction machine, curiosity as information gain | Light (human_thought) | Med |
| B4 | Sleep, replay and consolidation | how memories are reorganised offline | Light (human_thought) | Low |
| B5 | Computational neuroscience of planning | hippocampal replay, cognitive maps, model-based planning | Light (human_thought) | Med |

## C. Computational and formal

| # | Field | What it studies | Coverage | Priority |
|---|---|---|---|---|
| C1 | LLM reasoning methods | chain of thought, test-time compute, self-correction, verification | Deep (F12) | High |
| C2 | Cognitive architectures | Soar, ACT-R: impasse-driven subgoals, chunking, production rules | None | **High** |
| C3 | Computational cognitive science | Bayesian models, program induction, library learning, resource rationality | Light (human_thought) | High |
| C4 | Computational creativity | systems that generate and evaluate novel artefacts | Light | Med |
| C5 | Heuristic search and planning | search control, MCTS, tree and graph search over thoughts | Light (F12) | High |
| C6 | Automated reasoning and theorem proving | proof search, lemma discovery, saturation | None | Med |
| C7 | Reinforcement learning, exploration | curiosity, intrinsic motivation, exploration strategies | Light | Med |
| C8 | Case-based reasoning *(found by)* | solving new problems by retrieving and adapting past cases | None | High (memory) |
| C9 | Model-based diagnosis *(found by)* | finding faults from a model of how the system should work | None | High |
| C10 | Analogy engines | Structure-Mapping Engine, analogical retrieval | None | High |
| C11 | Information theory and minimum description length | simplicity as a prior, compression as understanding | Light | Med |
| C12 | Decision analysis and operations research | value of information, when to stop searching | None | Med |

## D. Philosophy and logic

| # | Field | What it studies | Coverage | Priority |
|---|---|---|---|---|
| D1 | Philosophy and logic of scientific discovery | abduction, falsification, Lakatos's proofs and refutations | Light (team notes) | High |
| D2 | Epistemology and Bayesian epistemology | justification, belief updating, evidence | Light | Med |
| D3 | Formal logic | valid inference, consistency checking | Light | Med |
| D4 | Argumentation theory and informal logic | argument structure, fallacies, critical questions | Light (F10) | Med |
| D5 | Critical-thinking research | what critical thinking is and whether it can be taught | None | Med |
| D6 | Philosophy of mind | what a representation is, consciousness, the global workspace | Light (human_thought) | Low |
| D7 | History of science | how real discoveries happened, case histories | Light (team notes) | Med |

## E. Applied practice: how people think well at work

| # | Field | What it studies | Coverage | Priority |
|---|---|---|---|---|
| E1 | Medical diagnostic reasoning | differential diagnosis, premature closure, illness scripts | Deep (F07) | High |
| E2 | Intelligence analysis | competing hypotheses, diagnosticity of evidence, red teaming | Deep (F08) | Med |
| E3 | Forecasting and calibration | base rates, decomposition, updating, Brier scores | Deep (F09) | Med |
| E4 | Naturalistic and expert decision making | recognition-primed decisions, mental simulation, pre-mortem | Deep (F10) | High |
| E5 | Design cognition | reflection-in-action, problem-solution co-evolution, reframing | Deep (F06) | High |
| E6 | Mathematical problem solving | Polya's heuristics, Schoenfeld's resources, heuristics, control and beliefs | Light | **High** |
| E7 | Engineering design methods | TRIZ, systematic design, functional decomposition | Light (team notes) | Med |
| E8 | Troubleshooting and fault diagnosis *(found by)* | how technicians find faults; hypothesis limits; surface-cue heuristics | None | **High** |
| E9 | Software debugging cognition *(found by)* | building a mental model of the cause of unexpected behaviour | None | **High** |
| E10 | Sensemaking *(found by)* | the data-frame model: frames select data, data reshape frames; reframing on anomalies | None | **High** |
| E11 | Legal and judicial reasoning *(found by)* | the story model of juror decisions, case-based legal reasoning, judges' biases | None | Med |
| E12 | Military planning and red teaming | course-of-action analysis, wargaming, adversarial review | None | Med |
| E13 | Cognitive systems engineering *(found by)* | macrocognition: how people think in complex work systems | None | Med |
| E14 | Innovation studies | recombination, exploration versus exploitation, recognising breakthroughs | Deep (F05) | Med |
| E15 | Science of science | what research practices produce discoveries | Light (team notes) | Med |
| E16 | Chess and game expertise | progressive deepening, templates, look-ahead | Light (F10) | Med |
| E17 | Strategic thinking in business | strategy formation, scenario planning | None | Low |
| E18 | Behavioural economics | bounded rationality, choice architecture | Light | Low |

## F. Language, culture and society

| # | Field | What it studies | Coverage | Priority |
|---|---|---|---|---|
| F1 | Cognitive linguistics | conceptual metaphor, conceptual blending | Light | Med |
| F2 | Cognitive anthropology and distributed cognition *(found by)* | thinking spread across people and tools (Hutchins) | None | Low (one agent), Med (tools) |
| F3 | Sociology of knowledge | how communities decide what counts as knowledge | None | Low |

---

## Where to dig next

The fields most likely to add **structure** to the schema (states, operators, control rules), not just more guardrails:

1. **C2 Cognitive architectures**: the impasse rule and subgoal learning are exactly the schema's S6.
2. **E6 Mathematical problem solving**: Schoenfeld's control episodes (read, analyse, explore, plan, implement,
   verify) have already been applied to reasoning models in a 2025 preprint.
3. **E8 and E9 Troubleshooting and debugging**: single-answer reasoning under a real check, where our schema is
   weakest.
4. **E10 Sensemaking**: the data-frame model gives a concrete reframing procedure with six named moves.
5. **C8 and C10 Case-based reasoning and analogy engines**: the memory and the O7 operator.
6. **D1 Lakatos and abduction**: refining a rule through its counterexamples.
7. **C5 Heuristic search**: the control that would run the idea tree.

---

## Sources from the web search, 2026-10-20

- Holyoak and Morrison, *The Oxford Handbook of Thinking and Reasoning*: https://academic.oup.com/book/34559
- List of branches of psychology: https://en.wikipedia.org/wiki/List_of_branches_of_psychology
- Troubleshooting in mechanics, a heuristic matching process (Besnard and colleagues): https://lpc.univ-amu.fr/en/doc/hal-00722885/_1.html
- Debugging as problem solving (DTIC report): https://apps.dtic.mil/sti/pdfs/ADA050779.pdf
- Starr and Storey 2025, software troubleshooting cognition: https://www.arxiv.org/pdf/2602.10540
- Distributed cognition (Hutchins): https://en.wikipedia.org/wiki/Distributed_cognition
- Sensemaking, data-frame model: https://en.wikipedia.org/wiki/Sensemaking_(information_science)
- FOCUS: a model of sensemaking (Sieck, Klein and colleagues 2007): https://apps.dtic.mil/sti/html/tr/ADA469770/index.html
- Story model of juror decisions (Pennington and Hastie): https://www.cambridge.org/core/books/inside-the-juror/story-model-for-juror-decision-making/61051A1D12C7F7FA58DD4424EA7D03F3
- Judging, fast and slow (Cunliffe 2014): https://vlex.co.uk/vid/judging-fast-and-slow-874254987
- Schoenfeld's episode theory applied to reasoning models (2025 preprint): https://arxiv.org/pdf/2509.14662
- Schoenfeld, mathematical problem solving: https://tecfa.unige.ch/themes/sa2/act-app-dos2-fic-mathemat2.htm
