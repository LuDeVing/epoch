# Philosophy of mind: subfields

Philosophy of mind asks what minds are, what mental states are about, and what consciousness is. It divides into metaphysics of mind (dualism, physicalism, functionalism), intentionality and representation, philosophy of cognitive science (computation, modularity), consciousness studies, and philosophy of action and agency. Most of it is conceptual. Two parts give architecture ideas: the theories of representation and the global workspace theory of consciousness.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Theories of mental representation | What it is for a state to carry content | Fodor; Dretske; Millikan; Block; SEP "Mental Representation" | Med | Represent (S2): the question of what a good representation preserves |
| Language of thought | Structured, symbol-like thought; productivity and systematicity | Fodor; Pylyshyn | Low | Background only |
| Connectionism and distributed representation | Patterns of activation, learned weights | Rumelhart and McClelland; Smolensky | Low | Background (it describes the model itself) |
| Imagery debate | Pictorial versus propositional images | Kosslyn; Pylyshyn; Tye | Med | Change representation (O6): spatial versus symbolic forms |
| Computational theory of mind | Thinking as computation | Turing; Putnam; Fodor | Low | Background only |
| Global workspace theory | Selected content broadcast to many specialist processes | Baars (1988); Dehaene; SEP "Neuroscience of Consciousness" | Med | Architecture analogue: code as the workspace that broadcasts one chosen item, memory, selection |
| Other consciousness theories | Recurrent processing, higher-order, integrated information | Lamme; Rosenthal; Tononi | Low | Background only |
| Metacognition and higher-order representation | Representing one's own states | Rosenthal; Proust | Med | Guardrail view: self-report is unreliable (G10) |
| Extended and situated mind | Tools and environment as part of cognition | Clark and Chalmers (1998) | Med | Memory and tools: external notes and code as part of the thinker |
| Mental causation and reasons | Do reasons cause thoughts | Davidson; Kim | Low | Background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Theories of mental representation | [`subfields/01_theories_of_mental_representation/DEEP.md`](subfields/01_theories_of_mental_representation/DEEP.md) | done, batch 8 (2026-11-01) |
| Language of thought | | not started |
| Connectionism and distributed representation | | not started |
| Imagery debate | [`subfields/04_imagery_debate/DEEP.md`](subfields/04_imagery_debate/DEEP.md) | done, batch 9 (2026-11-09) |
| Computational theory of mind | | not started |
| Global workspace theory | [`subfields/06_global_workspace_theory/DEEP.md`](subfields/06_global_workspace_theory/DEEP.md) | done, batch 9 (2026-11-09) |
| Other consciousness theories | | not started |
| Metacognition and higher-order representation | [`subfields/08_metacognition_and_higher_order_representation/DEEP.md`](subfields/08_metacognition_and_higher_order_representation/DEEP.md) | done, batch 9 (2026-11-09) |
| Extended and situated mind | | not started |
| Mental causation and reasons | | not started |

## Dig into next

**1. Representation theories.** Questions: (a) What properties make a representation good for a task (structure-preserving, supports needed operations)? (b) Can they become a test that S2 or O6 outputs must pass (e.g. recompute the answer from the new form)? Evidence: examples where a change of representation solved a task, with code-checkable criteria.

**2. Global workspace theory.** Questions: (a) What are the mechanisms: competition, ignition, broadcast, limited capacity? (b) Does a limited-capacity workspace with code-run competition among candidates match S4 to S7? Evidence: Baars and Dehaene accounts, and cognitive architecture implementations.

**3. Metacognition.** Question: which signals about one's own states are reliable? Evidence: studies of confidence and self-report accuracy, to tie to G10.

## Purely conceptual

The hard problem, qualia, the mind-body problem, personal identity and free will give nothing to run. Consciousness theories matter for the ethics of AI, not for our schema. Treat them as background.

## Sources

1. https://plato.stanford.edu/entries/mental-representation/ [V]
2. https://plato.stanford.edu/entries/consciousness-neuroscience/ [V]
3. Baars, *A Cognitive Theory of Consciousness* (1988) [M]
4. Clark and Chalmers (1998), "The extended mind," *Analysis* [M]
5. https://www.doc.ic.ac.uk/~mpsha/ShanahanBaarsCog05.pdf [M] (seen in a search listing only)
