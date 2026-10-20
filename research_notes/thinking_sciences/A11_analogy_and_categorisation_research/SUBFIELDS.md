# Analogy and categorisation research: subfields

This field asks how people notice that two situations share a structure, how they carry a solution across, and how they form and use categories. The Stanford Encyclopedia entry on analogy lists the sub-processes under study as retrieval of a source, mapping, transfer, and learning of new categories or schemas. Work divides into mapping theories (structure mapping and connectionist models), access (retrieval), induction (schemas), and category learning (rules, prototypes, exemplars, Bayesian). Computer models run through all of it. It is close to our operator O7 (map an analogue) and the planned subgoal library.

Marks in the table: (V) = confirmed in a source opened this session; (M) = from memory, not confirmed.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Structure mapping | Aligning two cases by relations; systematicity: prefer connected systems of higher-order relations | Gentner 1983 (V, cited in SME paper); Falkenhainer, Forbus, Gentner 1989/90 SME (V) | High | Operator O7: a typed mapping scored by code |
| Analogical inference | Carrying over conjectures from source to target; SME lists "candidate inferences" as a step | SME paper (V); CASI consistency checks (S) | High | O7 check; guardrail G3 |
| Analogical access (retrieval) | Why surface-similar cases are recalled and structure-similar ones are not | Gick and Holyoak 1980 (M); Gentner, Rattermann, Forbus 1993 MAC/FAC (M) | High | Memory: indexing the subgoal library |
| Schema induction | Generalising several experiences into an abstract schema | Named in the SME paper's opening as a use of analogy (V); Gick and Holyoak 1983 (M); SAGE (M) | High | Memory: solved subgoals as reusable rules |
| Connectionist and hybrid mapping models | ACME, LISA (access, mapping, inference in one architecture), Copycat | Holyoak and Thagard 1989, 1995; Hummel and Holyoak 1997, 2003; Hofstadter and Mitchell (all V via SEP) | Med | Background; design of the mapping step |
| Logic and philosophy of analogical arguments | When an analogical argument is strong; Hesse's material criteria, Bartha's articulation model | Hesse 1966, Bartha 2010 (V via SEP) | Med | Guardrail: criteria a code check can test (causal link, no essential difference) |
| Category learning: rule, prototype, exemplar | Learning categories by rules, central tendency or stored instances | Rouder and Ratcliff 2006; Goodman et al. 2008 (V via Wikipedia) | Med | Memory: problem classes for the S0 gate |
| Category learning: clustering, explanation-based, Bayesian | Multiple prototypes; generalising from examples with background knowledge; priors against likelihood | Anderson 1991; Love, Medin, Gureckis 2004; Mitchell, Keller, Kedar-Cabelli 1986; Tenenbaum 1999 (V via Wikipedia) | Med | S2 REPRESENT (rules from examples); S7 (rules still fitting) |
| Comparison and relational language | Comparison highlights alignable differences | Gentner and Markman 1997 (M) | Med | S2: compare examples to find what changes |

Correction from the first draft: Barsalou's ad hoc categories and relational categories were listed from memory and are dropped as low value.

## Dig into next

**1. Analogical access (retrieval).**
- Questions: What cue retrieves a structurally matching solved subgoal rather than a surface match? Does a cheap surface filter followed by a code-run structural match beat plain similarity search? Is a retrieved case better shown after the first attempt?
- Evidence needed: MAC/FAC and Gick and Holyoak retrieval data (to be opened); our subgoal library tested at equal tokens.

**2. Schema induction.**
- Questions: How many cases are needed before a schema beats the cases? How can code check that an induced schema is more than one case reworded?
- Evidence needed: SAGE and CASI papers; our measurement of schema reuse.

**3. Structure mapping and its scoring.**
- Questions: Which SME scoring parts (structural consistency, systematicity) can code apply to a model-written mapping? How often are model mappings inconsistent?
- Evidence needed: SME paper (opened); a small case set with known good mappings.

## Does not transfer

Child development of relational reasoning, human working memory limits on mapping, and neural data are about people. Judgments of how apt an analogy feels are human taste. The philosophical justification debates are background only.

## Sources

[V] = opened this session. [S] = seen in a search result only, not opened. [M] = from memory. Opened count: 3. The web search budget ran out before the extra searches could be run.

1. [V] Falkenhainer, Forbus, Gentner, The Structure-Mapping Engine, Artificial Intelligence 41: https://groups.psych.northwestern.edu/gentner/newpdfpapers/FalkenhainerForbusGentner89.pdf (scanned PDF, text extracted)
2. [V] Stanford Encyclopedia, Analogy and Analogical Reasoning: https://plato.stanford.edu/entries/reasoning-analogy/
3. [V] Wikipedia, Category learning: https://en.wikipedia.org/wiki/Category_learning
4. [S] Hummel and Holyoak 1997 (LISA); fetch failed on a certificate error: https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Hummel-Holyoak.1997.pdf
5. [S] CASI: https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2022/CASI_Final.pdf
6. [M] Gick and Holyoak 1980, 1983; Gentner, Rattermann, Forbus 1993
