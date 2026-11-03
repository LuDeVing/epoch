# Critique: Vygotsky and scaffolding (A14.07)

Cross-check of evidence_a, evidence_b, evidence_c (26 + 29 + 26 lines). Claims are in claims.jsonl (24 claims, K01-K24).

## Corrections made (re-checked this session via arXiv, OpenAlex, Crossref)

1. Tutor CoPilot message count. The arXiv v3 abstract (2410.03017v3) says "550,000+ messages". The files give three different numbers: 241,005 (a16), 350,000 (b03), 550,000+ (v3 abstract). Use 550,000+ for v3 and note that older versions differ. Same for sample size: v3 says 900 tutors and 1,800 students (matches b01); c17 says "700+ tutors, 1,000+ students" (older version). b01 also says 783 tutored (388/395). Headline +4 pp (62% to 66%, p<0.01), +9 pp for lower-rated tutors, $20 per tutor per year: all confirmed in the abstract.
2. Reflexion: 91% vs 80% HumanEval pass@1 confirmed from the arXiv abstract (2303.11366). The c23 sub-numbers (22%, 20%, 11%, 8%) were not re-opened.
3. Kim, Belland, Walker g=0.385: confirmed (OpenAlex abstract, DOI 10.1007/s10648-017-9419-1). Year on b09 is 2018 print, 2017 online.
4. Belland 2017 meta g=0.46 (a09): same study as b10. Counted as ONE source. A 2014 preliminary version (35 studies, 97 outcomes, mean 0.44) found adaptive fading/adding better than fixed fading; a09 says fading type did not matter in the full set. Treated as a change between versions, not a contradiction.
5. HintMR (c08-c10): paper exists (arXiv 2604.12229, v1 April 2026) and the abstract matches the claim of consistent gains and a hint model that cannot solve the problem alone. The exact percentages (64.86, 82.43, 75.68 to 54.05) were NOT re-opened here; they stay as read by agent C.
6. Bastani et al.: PNAS version exists (10.1073/pnas.2422633122, June 2025) and a PNAS correction was published 20 Aug 2025 (10.1073/pnas.2518204122). A separate "Critique of Generative AI Can Harm Learning Study Design" is on SSRN (4898213). The correction text and the critique were not read. The numbers +48%, +127%, -17%, 51% correct (b05, b06, c18) may be affected; mark as unverified until the correction is read.
7. Kestin et al.: Scientific Reports 2025 (10.1038/s41598-025-97652-6); abstract confirms the claim "learn significantly more in less time". The numbers 4.5 vs 3.5 and 0.63 were not re-opened.
8. a10 reports g = 3.13 for learners with learning disabilities from a within-subject pre/post design. That is not comparable to between-group g=0.46 and should not be quoted as an effect of scaffolding.
9. Cui and Sachan (a12, a13): neither Semantic Scholar (rate limited, 429) nor OpenAlex search returned the paper. Not re-verified. The "6 of 8 models" and "~20% lag" figures remain unchecked.
10. c24/c25 describe LLM student simulators; their numbers (0.75 to 0.82 correlations, "100% improvement") were not re-opened. "100% improvement" is the authors' own claim.

## Contradictions between sources

- Is the 3.3x/15.3x Voyager result independent? a21, b18, c21 are one paper counted once.
- Prompting to scaffold: MathTutorBench (c03) found little gain except GPT-4o; Figueiredo (a15/c15) found d=0.41 to 0.46 on rubric scores graded by LLMs. The grader differs and c02 shows LLM judges are near chance on pedagogy, so the Figueiredo gain is weak.
- Guidance: meta-analyses (b08, b13) favour guided learning; Kirschner et al. (a25) argue for worked examples over minimal guidance, which agree with guidance; expertise-reversal (b16) says help can hurt experts. Not a real conflict, but a boundary.
- Tutor CoPilot (help raises scores, +4 pp) vs Bastani (unguarded help lowers later scores, -17%): fits one rule, that help must be designed to withhold the answer. The two studies differ in who receives the help (tutor vs student).
- Cazden/Stone/Wass and Golding: scaffolding and ZPD fit "partly". Wood et al. did not cite Vygotsky as a theory of the study.

## Weak spots

- Founding numbers (a04, a06) come from a secondary revision page, not the 1976 paper. "10%, 50%, 75%" unassisted success is unverified against the paper.
- Vygotsky's mental-age 12 vs 9 example is recalled (a03).
- Opened:false lines: a03, a08, a11, a18, a24, b10 to b17, c26. b11, b12, b13, b14, b15, b16, b17 are "from memory" and must not be quoted as measured.
- Almost no LLM study tests ZPD-style contingent help directly against fixed help at equal tokens. Most compare to no help.
- Many tutoring studies use LLM judges or simulated students (c24, c25, b26-b28), whose realism is itself weak.
- Learners in the human literature are children; none tests a model whose "development" is fixed.
- Nothing here tests lessons as scaffolds at equal compute against a plain retry loop; Reflexion/ExpeL compare to no-memory.

## Only seen in snippets

a03, a08, a11, a18, a24, b10, b11 to b17, c26 (plus a04/a06 via a secondary page).

## GAPS (most decision-relevant first)

1. Does contingent hint escalation (more help after failure, less after success) beat fixed-size help for an LLM at equal tokens? Wood and Middleton 1975 is only from memory and no LLM paper tests it head on.
2. What is the harm rate of a stronger model's lessons when they are wrong? Bastani (51% correct, -17% later) and Saha (misaligned teacher) suggest large harm, but the PNAS correction and critique were not read.
3. Do stored lessons (Reflexion/ExpeL/ReasoningBank) beat a plain retry or best-of-N loop at equal tokens? All reported baselines are no-memory.
4. Which lesson source works best: own failures, stronger model, or hand-written? ExpeL has one table; Zhao 2024 says stronger model better. Need a second source.
5. Can a model estimate its own ZPD (what it can solve with a hint but not alone)? Cui and Sachan is unverified; ZPD-SCA shows other LLMs misjudge difficulty. Needs an independent replication.
6. Does fading (help only at low-confidence steps, SMART) hold up outside math, and does adaptive fading beat fixed fading as in the 2014 meta-analysis preliminary?
7. How do hint effects depend on solver strength: do hints hurt strong models (expertise reversal, untrained hints hurt in HintMR)? Need numbers across at least three solver sizes.
8. Are the Wood, Bruner and Ross pyramid numbers right (unassisted success by age, intervention ratios)? Open the 1976 paper.
9. Does the Kestin physics result (0.63) replicate with other courses, and do gains persist unaided?
10. Do ZPD-ordered curricula beat random order for in-context lessons (not fine-tuning) in a sequence of problems?

## Gap search results (evidence_d, d01 to d18)

Search was hard-limited: the web-search budget was used up, and the arXiv API, Semantic Scholar and OpenAlex all returned 429 or quota errors. Work was done by opening full texts at arxiv.org/pdf, Europe PMC, Crossref and nature.com.

1. Contingent escalation vs fixed help at equal tokens: STAYS OPEN. Wood and Middleton page returned 403 (the DOI in b15 looks wrong; Crossref gives 10.1111/j.2044-8295.1975.tb01454.x). No LLM paper found. HintMR gives stepwise hints but does not vary hint size by success. The van de Pol 2010 review (1,414 citations) exists but was not read.
2. Harm rate of wrong lessons: MOSTLY CLOSED. The PNAS correction (Aug 2025) only fixes an author affiliation, so the numbers stand (d01, d02): about 1,000 students, GPT Base -0.054 (-17%) on the exam, GPT Tutor -0.004, GPT-4 right 51% of the time. The SSRN design critique was not read. HintMR adds a direct harm figure for same-size untrained hints: 75.68 to 54.05 on MATH-500 (d04).
3. Lessons vs plain retry at equal tokens: PARTLY CLOSED. ReasoningBank MaTTS has a no-memory scaling arm at k=5: 39.0 to 42.2 vs 55.1 with memory (d06). Dynamic Cheatsheet has a majority-vote-of-3 arm: no gain (23.3) vs 50.0 with memory (d09). Neither is token-matched and both are author-built. A token-matched retry loop is still not tested.
4. Best lesson source: STAYS PARTLY OPEN. AWM: induced from own successes 35.5 vs 14 human workflows 33.0, different harnesses (d13). ExpeL: gpt-4 writer 39.0 vs gpt-3.5 writer 32.0 vs hand-crafted about 32.0, but writer strength and experience are confounded (d14). No study compares own-failure vs stronger-model lessons with the same writer.
5. Self-estimate of ZPD (Cui and Sachan): STAYS OPEN. Could not be located through any API. No new independent replication.
6. Fading outside math / adaptive vs fixed fading: STAYS OPEN. No new non-math fading study found. The 2014 preliminary vs 2017 full meta-analysis difference is unchanged.
7. Hint effect vs solver strength: PARTLY CLOSED (d03, d04, d10, d15). External hints help weaker solvers more (MATH-500 gains +9.5 for the strongest of four 4B to 8B solvers, +17.6 to +20.3 for the others). Self-hints and stored lessons need a capable solver (Dynamic Cheatsheet: Haiku and GPT-4o-mini gain little or fall; Progressive-Hint gain grows with model power). Only 4B to 8B solvers for external hints; no 3-size ladder up to frontier models. New claim K25.
8. Wood, Bruner, Ross pyramid numbers: STAYS OPEN (PDF 403, no other copy). Do not quote a04/a06 figures as measured.
9. Kestin replication and persistence: STAYS OPEN. Re-read in full (d16): N=233 enrolled (142 AI, 174 in-class post-tests), one course, immediate post-test only, effect 0.63 (0.73 to 1.3 ceiling-corrected). No replication or delayed test found.
10. ZPD-ordered curriculum for in-context lessons: STAYS OPEN. Dynamic Cheatsheet suggests ordering helps but did not test it (d10).

New findings worth carrying forward: (a) half of Dynamic Cheatsheet's AIME 2024 gain for Sonnet came from the empty-memory instruction text (K28), so every lesson test needs an instruction-only control; (b) hint and lesson sources need a validity gate, since bad same-size hints cost about 20 points (K26); (c) ACE keeps most of its gain without ground-truth labels but only with an execution signal (K29).

Status changes in claims.jsonl: K14 single-source/established wording updated and kept established with re-opened numbers; K09 numbers confirmed, correction read; K10 details added; K18, K19, K20 extended; K16, K04, K03 notes added; K25 to K30 added (30 claims).
