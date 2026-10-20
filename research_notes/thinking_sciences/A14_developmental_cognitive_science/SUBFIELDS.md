# Developmental cognitive science: subfields

This field studies how thinking grows from infancy through childhood and how knowledge changes. Its main programmes are Piaget's stages, Vygotsky's sociocultural theory, information-processing and neo-Piagetian accounts (attention and working memory), core knowledge, and the theory theory with its Bayesian form. The strand most useful to us treats the child as a scientist who explores, tests ideas and revises theories, which is a loop we want the agent to run.

Marks: (V) = confirmed in a source opened this session; (M) = from memory.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Theory theory / child as scientist | Children gather evidence, revise working models and make testable causal predictions | Gopnik and colleagues; "Child Scientist" label, Bayesian "Theory Theory 2.0" (V via Wikipedia); Gopnik and Wellman 2014 (S) | High | S5 REVISE; conjecture refinement |
| Bayesian and causal learning | Weighing priors against evidence; causal inference from statistics and action | Bonawitz et al. 2012 (V via Wikipedia); Gopnik and Wellman 2014 (S) | High | S4 TEST; choosing tests |
| Exploration and spontaneous experiments | Preschoolers isolate variables when evidence is ambiguous, but play indiscriminately when evidence is unambiguous | Cook, Goodman, Schulz 2011, Cognition 120 (V) | High | S7 discriminating test; open-mode S3 |
| Expected information gain models | Choosing actions by how much they separate hypotheses | Cook et al. 2011 (V) | High | Code computes the most informative input |
| Simulation vs theory accounts | Understanding others by simulating them versus by theory | Wikipedia theory-theory page (V) | Low | Background only |
| Piagetian and neo-Piagetian stages | Stage shifts; working memory and attention control as drivers | Piaget; neo-Piagetians (V via Wikipedia) | Low | Background only |
| Vygotsky: scaffolding | Learning with a more knowledgeable other | Vygotsky (V via Wikipedia) | Med | Memory: lessons as scaffolds for later problems |
| Core knowledge | Early sensitivity to objects, agents, number, place | Spelke, Feigenson, Dehaene (V via Wikipedia) | Low | Background only |
| Scientific reasoning skills | Controlling variables, coordinating theory and evidence | Kuhn, Klahr (M) | High | S4: one change per test |
| Executive function, exploration vs exploitation | Inhibition, shifting; children explore more widely than adults | Diamond (M); Gopnik (M) | Med | G12 and open mode |

Corrections from the first draft: Cook et al. show exploration is sensitive to ambiguity, so "children explore randomly" and "children always test well" are both wrong. Wikipedia's page on cognitive development does not cover Bayesian models, so that attribution rests on the Cook paper and the theory-theory page.

## Dig into next

**1. Choosing informative tests.**
- Questions: How do children pick interventions that separate two causal hypotheses? Can code compute which input separates two rules that still fit the examples (our S7 discriminating test) with an expected-information measure?
- Evidence needed: Cook et al. 2011 (opened); Gopnik and Wellman 2014; a test on two-rule ARC cases.

**2. Scientific reasoning skills.**
- Questions: Which errors persist (confirming only, changing many variables) and do models make them? Does forcing one change per revision help?
- Evidence needed: Kuhn and Klahr task data (to be opened); our logs of multi-change revisions.

**3. Exploration versus exploitation.**
- Questions: When should the agent widen search and when narrow it?
- Evidence needed: child-adult exploration studies (to be found); our NoveltyBench and puzzle runs at equal tokens.

## Does not transfer

Stage timing, brain maturation, caregiver effects, curiosity as a drive and schooling are about human growth. A model does not develop between calls, so trajectories give analogies, not tuning data.

## Sources

[V] = opened this session. [S] = seen in search results only. [M] = from memory. Opened count: 3. The extra searches could not be run (search budget used up).

1. [V] Cook, Goodman, Schulz 2011, Where science starts, Cognition 120: https://web.stanford.edu/~ngoodman/papers/CookGoodmanSchulz2011.pdf
2. [V] Wikipedia, Theory-theory: https://en.wikipedia.org/wiki/Theory-theory
3. [V] Wikipedia, Cognitive development: https://en.wikipedia.org/wiki/Cognitive_development
4. [S] Gopnik and Wellman 2014 (fetch failed, certificate error): https://sites.socsci.uci.edu/~lpearl/courses/readings/GopnikWellman2014_CausalBayesTheoryTheory.pdf
5. [S] Gopnik, Scientific thinking in young children: https://www.alisongopnik.com/Papers_Alison/Scientific%20Thinking%20in%20young%20Children.pdf
6. [M] Kuhn; Klahr 2000
