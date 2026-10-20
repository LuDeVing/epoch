# Mathematical problem solving: subfields

This field studies how people solve non-routine maths problems and how to teach it. It began with Polya's heuristics, was made empirical by Schoenfeld's protocol studies, and spread into expert-novice work, worked examples and now analysis of reasoning-model traces. It has single answers, real checks and named procedures, the closest match to our schema.

Schoenfeld's framework (1985, opened via a summary page) has four parts: resources (facts and procedures), heuristics (strategies such as drawing a figure or working backwards), control (deciding when to use which), and beliefs (a world view that shapes approach). It rests on protocol analysis of students and mainly covers college maths. The summary page does not cover episode analysis.

What the 2025 preprint (arXiv 2509.14662, EMNLP 2025) labels and measured. It labels each sentence with seven episodes: Read (restate givens and goal), Analyze (recall theory, make inferences, no calculation), Plan (announce next step or strategy), Implement (carry out calculation), Explore (tentative guesses and tries), Verify (judge a result or method), Monitor (brief hesitations marking transitions). Paragraphs get one of three labels (General, Explore, Verify). The hand-annotated corpus is 38 DeepSeek-R1 responses to SAT maths problems (2 per each of 19 skills) with 915 paragraphs and 3,087 sentences, drawn from 1,385 items. It measured how well LLMs and classifiers reproduce the labels: GPT-4.1 with examples and a guidebook reached 0.805 sentence accuracy (kappa 0.764), BERT 0.732; the guidebook gave the largest gain. Common transitions were Read to Analyze, Plan to Implement, Explore to Analyze. Confusions were Analyze with Verify and Implement with Verify. It did not test whether the labels predict correctness. The follow-up ThinkARM (arXiv 2512.19995) adds Answer (eight categories), uses 15 models and 410,991 sentences from 1,500 responses, and finds Explore is a branch point linked to correctness (Explore to Monitor positive, high Explore share negative).

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Polya's heuristics | Understand, plan, carry out, look back; operators | Polya 1945 | High | States and O1 to O5 |
| Schoenfeld framework | Resources, heuristics, control, beliefs | Schoenfeld 1985 | High | S6 control |
| Metacognition and control | Monitoring, abandoning approaches | Schoenfeld 1985, 1992; Garofalo and Lester | High | S6 trigger rules |
| Episode analysis of reasoning models | Labelling LLM traces | Li et al. 2025; ThinkARM | High | Coding our logs; spotting control failures |
| Expert-novice schemas | Sorting by deep structure | Chi, Feltovich, Glaser 1981 | High | S0 gate, memory |
| Worked examples | Study before solving | Sweller; Renkl | Med | Subgoal library |
| Teaching heuristics | Transfer evidence mixed | Schoenfeld; Mason et al. | Med | Needs a control layer |
| Problem posing, conjecture | "What if not", refutation | Brown and Walter; Lakatos | Med | O4 |
| Beliefs and affect | Persistence, "5-minute" belief | Schoenfeld | Low | Background |

## Dig into next

**1. Coded impasse detector from episodes.**
- Which episode patterns (long Explore, Explore without Monitor) predict failure, and can code label them live?
- Evidence: ThinkARM correctness coefficients, but only on one benchmark with a model annotator; test on our logs.

**2. Polya operators with preconditions.**
- For each operator, what problem features predict help?
- Evidence: Polya, Schoenfeld protocols, our per-operator solve counts.

**3. Expert sorting.**
- Does structure-based classification improve the S0 gate and retrieval?
- Evidence: Chi et al. 1981, LLM tests of surface against deep retrieval.

## Does not transfer

Motivation, anxiety, schooling beliefs and teacher moves are about people. Teaching studies show weak transfer of heuristics partly because people do not apply them; a program-driven agent does not share that failure. The preprint covers SAT maths and a single annotation scheme.

## Sources

[V] = opened and read this session. [M] = search result only, or from memory. Two further searches were refused (budget exhausted). Opened: 4.

1. Li et al. 2025, arXiv 2509.14662 (HTML and PDF read). https://arxiv.org/html/2509.14662 [V]
2. Schoenfeld's Anatomy of Mathematical Reasoning by Language Models, arXiv 2512.19995 (abstract and HTML). https://arxiv.org/html/2512.19995v1 [V]
3. Summary of Schoenfeld's Mathematical Problem Solving. https://tecfa.unige.ch/themes/sa2/act-app-dos2-fic-mathemat2.htm [V]
4. Schoenfeld's book, publisher page (not opened). https://shop.elsevier.com/books/mathematical-problem-solving/schoenfeld/978-0-12-628870-4 [M]
5. Polya 1945, How to Solve It. [M]
6. Chi, Feltovich, Glaser 1981, Cognitive Science. [M]
7. Lakatos 1976, Proofs and Refutations. [M]
