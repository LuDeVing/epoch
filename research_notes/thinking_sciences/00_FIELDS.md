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

## Deep research by subfield

Each field with researched subfields gets a `SYNTHESIS.md` at its top: established findings merged across subfields, contradictions, recurring mechanisms, merged tests. Established findings that could change the schema are collected in [`../single_agent/SCHEMA_CANDIDATES.md`](../single_agent/SCHEMA_CANDIDATES.md); claim ids are global (`A01.03-K12`).

Subfields are researched in batches. Each gets a folder `<field>/subfields/NN_slug/` holding:

| File | What it is |
|---|---|
| `DEEP.md` | **Read this.** 11 fixed sections: 1 what it is, 2 history and theories, 3 core findings with numbers, 4 mechanisms and models, 5 what holds up, 6 language models, **7 what our agent should take** (add now vs test first), **8 tests on our bench**, 9 what does not transfer, 10 open questions, 11 sources |
| `UNKNOWNS.md` | **what we don't know** and must test before it may enter the schema: one row per candidate with the test at equal tokens, an "add if" rule and a priority; all rows are collected in [`00_TEST_BACKLOG.md`](00_TEST_BACKLOG.md) |
| `claims.jsonl` | findings turned into claims, each with status (established, single-source, contested, refuted), schema part and a test |
| `critique.md` | numbers corrected on re-check, contradictions, gaps and which closed |
| `evidence_a` to `_d.jsonl` | raw evidence: a foundations, b replications and critiques, c language models, d gap search |

| Batch | Date | Subfields | Index |
|---|---|---|---|
| 1 | 2026-10-21 | A01: mental models; Wason task and hypothesis testing; content effects; belief bias; dual-process theories | [`A01_.../SUBFIELDS.md`](A01_cognitive_psychology_of_thinking_and_rea/SUBFIELDS.md#deep-research) |
| 2 | 2026-10-21 | A01: single- versus two-process induction and deduction; dual-strategy model; syllogistic and conditional reasoning; inductive and probabilistic reasoning. A02: problem-space theory | [`A01_.../SUBFIELDS.md`](A01_cognitive_psychology_of_thinking_and_rea/SUBFIELDS.md#deep-research), [`A02_.../SUBFIELDS.md`](A02_problem_solving_research/SUBFIELDS.md#deep-research) |

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

---

## Subfields: what each folder holds (2026-10-20)

Each field folder now has a `SUBFIELDS.md`: the field's subfields with what they study, key people and works, usefulness
for the agent and the schema part they could inform; the subfields to dig into next with research questions; what does
not transfer; and sources marked [V] opened this session or [M] from memory or search results only.

**The two subfields per field most worth digging into**

| Field | Top subfields |
|---|---|
| A01 Reasoning | Wason task and hypothesis testing; belief bias and content effects |
| A02 Problem solving | impasse-driven subgoaling and chunking; progress monitoring |
| A03 Judgment and decision making | heuristics and input cues (anchoring); debiasing by training with feedback |
| A04 Metacognition | monitoring accuracy and cheap signals; regulation and strategy choice |
| A05 Learning science | worked examples with fading; transfer |
| A06 Memory | encoding specificity and cue design; interference |
| A07 Attention | capture by salient cues; load theory |
| A08 Cognitive load | element interactivity; expertise reversal and fading |
| A09 Creative cognition | fixation and structured imagination; Geneplore |
| A10 Creativity and expertise | Einstellung; chunking and templates |
| A11 Analogy and categories | analogical access (retrieval); schema induction |
| A12 Insight | representational change (constraint relaxation, chunk decomposition); progress monitoring as an impasse detector |
| A13 Intelligence research | item difficulty models; capacity versus load in reasoning |
| A14 Development | exploration and choosing informative tests; scientific reasoning skills |
| A15 Language and thought | framing and wording effects; presupposition and suggestive cues |
| A16 Embodied cognition | external representations; epistemic action |
| A17 Collective intelligence | conditions for aggregation; social influence on crowds |
| A18 Comparative cognition | causal reasoning tasks and their controls; the parsimony debate |
| A19 Cross-cultural cognition | analytic versus holistic framing; dialectical reasoning |
| A20 Psychology of programming | debugging strategies; programming plans and schemas |
| B01 Creativity neuroscience | generation versus evaluation; metacognition of insight |
| B02 Neuroeconomics | expected value of control; model-based versus model-free arbitration |
| B03 Predictive processing | information-gain test selection; explore-to-exploit switch |
| B04 Sleep and replay | gist extraction; wake-sleep library learning (DreamCoder) |
| B05 Planning neuroscience | prioritised replay; successor representation and subgoal discovery |
| C01 LLM methods | verification design; adaptive stopping and test-time allocation |
| C02 Cognitive architectures | Soar impasses and substates; Soar chunking as a subgoal library |
| C03 Computational cognitive science | library learning (DreamCoder, LILO); resource-rational strategy selection |
| C04 Computational creativity | quality-diversity and novelty search; evaluating creativity |
| C05 Search and planning | search with restarts at known cost; heuristics by relaxation |
| C06 Theorem proving | lemma discovery and proof libraries; conflict learning (no-goods) |
| C07 Exploration | bandit selection of operators; Go-Explore archive |
| C08 Case-based reasoning | retention and maintenance; retrieval as a learned choice |
| C09 Model-based diagnosis | probe selection; conflict sets over attempts |
| C10 Analogy engines | structure mapping and candidate inferences; MAC/FAC retrieval |
| C11 Minimum description length | MDL as the selection tie-break; MDL program synthesis on ARC |
| C12 Decision analysis | value of computation; optimal stopping for attempts |
| D01 Logic of discovery | proofs and refutations; abduction and inference to the best explanation |
| D02 Bayesian epistemology | belief revision; conditionalisation and Jeffrey updating |
| D03 Formal logic | SAT and SMT consistency and counterexample search; default logic |
| D04 Argumentation | argument schemes and critical questions; formal argumentation frameworks |
| D05 Critical thinking | transfer; debiasing results |
| D06 Philosophy of mind | mental representation; global workspace theory |
| D07 History of science | cognitive-historical case studies; scientists' notebooks |
| E01 Diagnosis | knowledge-based strategies over process instructions; a reflective second look |
| E02 Intelligence analysis | diagnosticity of evidence; why ACH failed |
| E03 Forecasting | base rates and comparison classes; decomposition with a coded combine step |
| E04 Expert decisions | conditions for valid intuition (as the S0 gate); mental simulation |
| E05 Design cognition | framing and reframing; co-evolution against problem-space-first |
| E06 Mathematical problem solving | a coded impasse detector from episode labels; Polya operators with preconditions |
| E07 Engineering design | functional decomposition; TRIZ contradiction as a typed reframe |
| E08 Troubleshooting | half-split and cost-weighted search; hypothesis limits |
| E09 Debugging | supplied hypotheses as a debugging aid; a mental-model-first phase |
| E10 Sensemaking | data-frame theory and frame activities; anomaly handling and fixation |
| E11 Legal reasoning | story model with coverage; case-based reasoning |
| E12 Military planning | course-of-action analysis; wargaming as test by simulation |
| E13 Cognitive systems engineering | anomaly response and failure patterns; error detection and recovery |
| E14 Innovation | recombinant search and distance; exploration versus exploitation |
| E15 Science of science | discovery as reasoning; novelty and atypicality |
| E16 Chess | staged thought process and deepening; chunks and templates |
| E17 Strategy | planning-performance research; scenario planning |
| E18 Behavioural economics | ecological rationality; resource-rational analysis |
| F01 Cognitive linguistics | conceptual blending; computational blending |
| F02 Distributed cognition | epistemic actions; external representations |
| F03 Sociology of knowledge | network epistemology and division of cognitive labour; judgment aggregation |

**Findings from this round worth testing against the schema**

- A short "Don't be blind" warning made over half of Luchins's subjects switch from a habitual method (A10). It pulls
  against G1 and section 4b of the schema; test it before adopting anything.
- Bias training with feedback cut six biases by over 30%, while generic warnings did not (A03). Supports lessons plus
  real feedback over instructions.
- A 2026 monitoring harness for LLMs raised pooled accuracy for Claude Sonnet 4.6 from 48.3 to 56.9 (A04; one source,
  abstract level).
- The working-memory capacity account of fluid reasoning was not supported, and training does not transfer (A13).
- No single program-comprehension strategy was best (A20); supplying hypotheses gave debuggers about a six-fold gain (E09).
- Schoenfeld's episodes have been labelled in LLM traces (E06, arXiv 2509.14662): Read, Analyze, Plan, Implement,
  Explore, Verify, Monitor; GPT-4.1 reproduced human labels at 0.805 sentence accuracy. A ready vocabulary for the
  schema's states and an impasse detector.
- Nudges: d = 0.45 over 200+ studies, but a reanalysis finds no effect after publication-bias correction (E18).

**What the search could not close** (the shared web-search allowance of this session ran out mid-round)

- No LLM work found for model-based diagnosis (C09) and no structure-mapping engine inside an LLM loop (C10). Gaps in
  the search, not proof of absence.
- ACT-R production compilation, Kapur's productive failure, Getzels and Csikszentmihalyi's problem finding, Ko and Myers
  on debugging fixation, and controlled TRIZ outcomes remain unconfirmed ([M]).
- No controlled study of red teaming or scenario planning was found in the pages opened (E12, E17).
- Several key PDFs could not be opened; rows resting on them stay [M] in each file.
