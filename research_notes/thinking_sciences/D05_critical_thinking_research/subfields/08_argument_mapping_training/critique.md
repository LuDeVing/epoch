# D05.08 Argument mapping training: cross-check critique

Checked 2026-11-19 by re-opening primary PDFs (stored under D:/research_scratch/D05.08/, to be deleted). 80 evidence lines read (a 25, b 30, c 25); 19 claims written to claims.jsonl.

## Numbers re-opened and confirmed

1. van Gelder, Bissett, Cumming (2004): mean gain 0.80 SD, CI95 0.66 to 0.94, t(231)=14.08, pre 18.82, post 22.40. Confirmed (b04).
2. Reason! Technical Report 2002/1 table: CCTST 2000 n=50 d=0.84 raw, 0.89 with the manual SD 4.457; 2001 n=114 0.82 raw, 0.89 manual; 2002 n=117 0.72 raw, 0.73 manual; traditional WGCTA 1999 n=46 d=0.02; Monash philosophy n=61 d=0.32 (CI -0.05 to 0.69). Confirmed (b01, b02).
3. Butchart et al. (2009): AM with automated feedback 0.45 SD, mean gain 13.7%; standard course 0.19; AM without feedback 0.22; AOMT 0.14; Peer Instruction 0.40 (+/-0.25). Confirmed (b07, a07).
4. Alvarez-Ortiz via Dwyer thesis: 0.68 SD CI [.51,.86], LAMP 0.78 CI [.67,.89] present in the thesis text. Confirmed as reported there only (a01, a02).
5. Dwyer thesis Study 2: overall CT F(2,77)=1.65 p=.198; analysis F(2,77)=4.74 p=.011, partial eta2 .11. Confirmed (a15).
6. Freedman et al. (2025) ArgLLM Table 1: extra GPT-4o MedClaim row is 0.85 direct, 0.82 estimated confidence, 0.85 CoT, 0.74/0.76 for 0.5-base depth 1/2, 0.83/0.80 estimated-base depth 1/2. Confirmed b24; the PDF table is column-garbled for other rows, so per-model claims beyond this row are lower confidence.
7. Baur et al. (2026) Argument Graph Uncertainty Table: Nemotron-3 Nano 30B PRR 0.65 vs 0.24 vs 0.41; GPT-OSS-120B 0.56 vs 0.36 vs -0.27; DeepSeek-R1-Distill-Llama-70B 0.34 vs 0.46 consistency. Confirmed. Blend 0.68 for Nemotron (extra detail, added to K14).
8. Graphionale (2026): 223 recruited, 204 valid; hard BBH over-trust -0.199 p=.002; collapsed -0.144 p=.033 and error correction +0.127 p=.040; hard error correction +0.182 and appropriate trust -0.165 appear as read in the lines. Confirmed (c01, c02).

Not re-opened this pass (taken from earlier lines): Harrell 2011 numbers (a10, a11; paywalled, flaws listed by Harrell himself), Dwyer 2012 d=.81 and control d=.55 (a14, read through the thesis), Fang GoV and Wang trace-graph numbers (c18 to c20), Pirozelli numbers (c06 to c08, noted as garbled table).

## Corrections and clarifications

- Reason! effect sizes come in two versions: raw SD of each cohort and a fixed manual SD of 4.457. The famous 0.8 mixes both; 2002 cohort is 0.72 raw / 0.73 manual, so "about 0.8" slightly overstates the later cohorts. b01 uses the manual-SD figures, which is right but should be labelled.
- b01 lists 2001 n=114 d=0.89 (manual SD); raw is 0.82. No error, but state the SD used.
- Butchart's mapping-with-feedback CI is +/-0.29, so it excludes zero only narrowly; Peer Instruction 0.40 +/-0.25 overlaps it. a09 and a07 should not be read as "mapping beats peer instruction".
- Evidence a03 describes van Gelder 2000 as effect .41 (WGCTA) while b01 lists the 1999 prototype as d=0.39 (n=53) and a03 gives 53 AM students; these agree within rounding (0.41 with a different SD).
- a05 and b06 give Twardy (2004) 0.72 vs the 0.8 founder gain ("90%"): consistent. The a05 line is second-hand, b06 first-hand.
- a22 and c21 are the same survey (Li et al. 2025); counted as one independent source in K17.
- a21 and c06 to c08 are the same Pirozelli paper; one source.
- b21 (Davies, Barnett, van Gelder 2015) is written by the developers and only its introduction was read, so it adds no independent confirmation of 0.8 SD.

## Contradictions between sources

- Developers report about 0.8 SD; independent replications give 0.45 (Butchart), and Dwyer finds no overall advantage over outlining. The difference may be teacher quality, practice hours (about 10 h Melbourne vs 5 to 7 h Monash), or feedback, but none of these explanations was tested.
- Dwyer 2012 shows mapping beating control on argument analysis and verbal reasoning, while the thesis Study 2 (same lab) shows no overall CT gain. Different tests (Halpern vs CCTST), duration and attrition.
- Harrell Study 1 (gain difference t(53)=1.35, n.s.) vs Study 2 (posttest d=.66, p=.01). The effect appears only for low-pretest students and is small in the ANCOVA (partial eta2 .03).
- LLM side: ArgLLM stays at parity or below CoT (Freedman, Zhou), while MArgE and the fact-checking framework report gains. The gains involve stronger scorers and adversarial retrieval, so they are not a clean test of the graph.
- Graphionale: graphs help calibration on verbal hard items but hurt on visual items, and liking and objective effect point in opposite directions.

## Weak spots

- No randomised controlled trial of argument mapping with an active control appears in the evidence; every large number is pre/post or cross-cohort.
- The CCTST is multiple choice and the training tasks resemble it, so near transfer is likely. Maturation and retesting are only estimated (about 0.3 SD).
- Publication and developer bias: the strongest results come from the method's authors (van Gelder, Twardy, Davies). Chang et al. (2025) warn of a bias toward positive reports.
- The Alvarez-Ortiz LAMP effect is built from the same few uncontrolled studies listed above, so it is not independent of them. Count it once.
- Human CT training does not map onto an LLM. There is no LLM study of the van Gelder protocol, so every agent claim here is by analogy.
- Search depth on the LLM side was thin (API rate limits); the "no direct study" claim K18 is an absence found, not proven.

## Only seen in snippets or abstracts (not opened)

- b13 (Dwyer 2012 abstract), b14 (Harrell 2008), b15 (Harrell 2011 fragment), b16 (MANCOVA dissertation, no N), b19 and b20 (2025 and 2026 systematic reviews, abstracts only), c14 (UMSL thesis), c23 and c24 (background).
- Numbers for b20 ("large" pooled effect) were never obtained, so it cannot support or refute 0.8 SD.

## GAPS

1. Is there any randomised, actively controlled trial of argument mapping on a standardised CT test (not only the CCTST), and what is its effect size? The two 2025/2026 systematic reviews (b19, b20) could settle this if their effect tables are read.
2. What does the 2026 systematic review (b20, 86 documents) actually report as the pooled g or d, and how does it change after removing conference papers and developer-authored studies?
3. Does an LLM given a map-first step (claims, supports, objections) beat plain chain of thought, and an equal-length free-form outline, at equal tokens on a held-out task class (the K02 test)? No study found; this is the direct experiment.
4. Does a mapping step help only where the plain attempt is inconsistent (a gate), as the low-pretest finding (r=-0.54; Harrell d=1.1 vs none) suggests, or does mapping every item cost more than it gains?
5. What hurts maps in LLMs: size (the 30 vs 50 proposition ceiling, node overload) or parse errors (full-pipeline span F1 59.65 vs 70.93)? Needed: accuracy as a function of node count with a code-validated map format.
6. Can graph features of a model's own trace (argument-graph uncertainty, exploration density) be used as a code-computed selection hint at S7 without violating G4 and G10, and how do they compare with sample consistency across models (R1-Distill-Llama-70B was the exception)?
7. Is the feedback effect (0.45 vs 0.22) real? Does a located-failure feedback loop on a map revision (G2) beat a self-critique loop at equal tokens?
8. Do maps carry any transfer beyond the training task class (human data: only near transfer; retention n=20)? Test: tune on one task class, evaluate on another.
9. Harrell 2008 and 2011 full texts: do the 180-student numbers and the reported gains for students who built maps hold, and what are the exact effect sizes?
10. Is there evidence on map-building tools for LLM agents (Rationale, Carneades, Argdown) used inside deployed agent loops, and what measured benefit do they show?

## Gap search results

Gap pass 2026-11-19. 17 evidence lines in evidence_d.jsonl (d01 to d17; 13 opened, 4 not opened). Claims: K05 downgraded to contested, K03, K06, K08, K12, K18 extended, K20 to K26 added. OpenAlex, Semantic Scholar and the arXiv API were rate limited; WebSearch budget ran out; philpapers, philarchive, kilthub, Wiley, Galway and Taylor and Francis blocked bots (403). Several gaps therefore stay open.

1. Randomised, actively controlled trial: STAYED OPEN. None found. Harrell 2011 is a quasi-experiment (N=269, intact sections, own test): gain 0.22 vs 0.18 in both studies, not significant (d01). The Frontiers 2022 study is concept mapping, not argument mapping (d07). The Dwyer 81-student chapter (mapping equals hierarchical summary) was only seen in a snippet (d08).
2. Pooled g or d of the 2026 review: STAYED OPEN. The chapter is by Davies and Calma (Davies is a Reason!/Rationale developer), so it is not independent, and no abstract numbers were retrievable (d06). The 2025 Higher Education Quarterly review (124 studies) reports no pooled effect (d05).
3. Map-first vs CoT vs free outline at equal tokens: STAYED OPEN, with the nearest tests found. Pro/con Argument Generation gives mean gains over CoT of 3.18% (small), 2.72% (medium), 0.95% (large) models, task-dependent (d09). Critical-Questions-of-Thought wins 18 of 20 cells on 40 questions per model with many extra calls (d10). Neither controls tokens against a free-form outline. arXiv keyword search found no direct test (d16).
4. Gate vs always map: PARTLY CLOSED for humans, OPEN for LLMs. Harrell shows the low-pretest benefit in Study 2 (0.39 vs 0.24, p=.007) but not reliably in Study 1 (p=.14, n=6) and not for intermediate students in Study 2 (d02). The earlier d=1.1 was not in the paper text; K05 is now contested. The 2024 Argument Generation paper shows gains shrink with model size (d09), a weak LLM analogue.
5. Size vs parse errors: STAYED OPEN. No node-count experiment was found.
6. Graph features vs sample consistency at S7: STAYED OPEN. Self-consistency is the baseline (+17.9 on GSM8K, d13); Baur (b28) is the only head-to-head. A post-hoc justification can use a different scheme from the reasoning in about 20% of cases (d15), a risk for any map built after the answer.
7. Located-failure feedback vs self-critique: PARTLY CLOSED for LLMs by analogy. Self-critique alone hurts (GPT-3.5 CommonSenseQA 75.8 to 41.8) and oracle feedback helps (GSM8K 75.9 to 84.3) (d11, d12). The human 0.45 vs 0.22 feedback effect is still uncontrolled.
8. Transfer beyond the task class: STAYED OPEN. No new evidence.
9. Harrell 2008 and 2011 full texts: PARTLY CLOSED. The 2011 numbers were verified (d01 to d03); the paper has internal mismatches in its printed effect sizes. The 2008 paper could not be opened (d04).
10. Tools in deployed agent loops: STAYED OPEN. ArgEval (2026) is the one code-aggregated argument-graph system with a measured cost win: similar label-match to the base LLM at 2.4x fewer completion tokens (d14). No Rationale, Carneades or Argdown agent-loop benefit found (d16, d17).

Corrections to earlier lines: b14's "180 students" and K05's "Harrell d=1.1" are unverified or wrong. Use raw gains.
