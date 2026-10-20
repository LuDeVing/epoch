# Learning science: subfields

Learning science studies how people acquire knowledge and skill and how to teach so that it lasts and transfers. It divides into cognitive principles of study (retrieval, spacing, interleaving), instruction design (worked examples, fading, self-explanation), constructivist designs (productive failure), and transfer research. Our agent does not learn in weights, but it keeps lessons and a subgoal library and can be shown examples. So the useful parts are what to store, when to show it, and how to make it transfer.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Worked-example research | Studying solutions beats problem solving early in skill acquisition; works best in algorithmic domains; fading into problems; self-explanation needed; three examples did no better than one; partly completed examples did as well as full ones [V3] | Sweller and Cooper (1985); Renkl; Paas; Quilici and Mayer; Nievelstein et al. (2013) | High | memory: subgoal library as worked examples |
| Expertise reversal and fading | Examples become redundant or harmful as knowledge grows [V3] | Kalyuga and colleagues | High | S0: show lessons only on weak classes |
| Testing effect (retrieval practice) | Retrieval beats restudy; harder successful retrieval helps more; feedback helps; short-answer beats multiple choice [V2] | Roediger and Karpicke; Dunlosky et al. (2013); Pashler | Low | background only (agent has no forgetting) |
| Desirable difficulties | Spacing, interleaving, self-testing feel harder and last longer; performance during learning misleads [V1] | Bjork and Bjork; Bjork and Simon keystroke study; Kornell | Med | caution: do not judge a lesson by immediate gain |
| Transfer of learning | Near versus far transfer; identical elements (Thorndike and Woodworth 1901); bridging and hugging; abstraction and analogy; still debated whether far transfer is common [V4] | Perkins and Salomon; Guthrie; Gick and Holyoak [M] | High | O7 analogy, lesson reuse across classes |
| Productive failure | Attempt first, instruction after [M, not confirmed: no page found] | Kapur (2008, 2014) [M] | High if confirmed | memory: lessons after first attempt (in schema) |
| Self-explanation | Learners must explain steps for examples to work [V3] | Chi et al. (1989) [M] | Med | S5: one-line naming of what is wrong |
| Intelligent tutoring and knowledge tracing | Modelling what a learner knows [M] | Anderson; Corbett; Schwonke et al. (2009) cognitive tutor gains [V3] | Med | class record |
| Scaffolding and guided discovery | Support then withdrawal [M] | Wood, Bruner, Ross; Kirschner, Sweller, Clark | Med | S0 mode |
| Motivation, mindset, classroom factors | [M] | Dweck | Low | does not transfer |

## Dig into next

1. **Worked examples with fading.** Questions: (a) Does showing one solved subgoal of the same class beat none at equal tokens? (b) Do partly completed examples work as well as full ones, as Paas found? (c) Does a second, more complex example raise transfer (Reed and Bolstad)? Evidence: library ablation by class pass rate; expertise reversal predicts a cross-over.
2. **Transfer.** Questions: (a) What lesson features (structure versus surface) predict reuse on a new problem? (b) Does an explicit bridging step ("where else does this apply?") help? (c) Is far transfer rare for models too? Evidence: lessons from class A tested on class B.
3. **Productive failure.** Questions: (a) Verify the design and effect size from Kapur's papers (not opened this session). (b) Does lesson-after-attempt beat lesson-before on accuracy and diversity? Evidence: Kapur 2008 and 2014 papers (to fetch), and our order-of-lesson ablation.

## Does not transfer

Spacing, forgetting, retrieval practice and desirable difficulties exist because human memory decays and strengthens with effort. Illusions of comprehension, motivation, mindset, WEIRD-sample limits and classroom factors are about people.

## Sources

[V] = opened this session with WebFetch. [M] = memory or search snippet only. The searches for Kapur's papers returned nothing and the search budget was then exhausted.

1. [V] APS Observer, Desirable Difficulties: https://www.psychologicalscience.org/observer/desirable-difficulties
2. [V] Testing effect, Wikipedia (first 100k characters): https://en.wikipedia.org/wiki/Testing_effect
3. [V] Worked-example effect, Wikipedia: https://en.wikipedia.org/wiki/Worked-example_effect
4. [V] Transfer of learning, Wikipedia: https://en.wikipedia.org/wiki/Transfer_of_learning
5. [M] Kapur (2008) Productive failure, Cognition and Instruction; Chi et al. (1989); Bjork and Bjork (2011). No URLs; unconfirmed.
