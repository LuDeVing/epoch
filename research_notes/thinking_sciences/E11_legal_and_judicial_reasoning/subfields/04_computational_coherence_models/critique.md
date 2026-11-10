# Critique and cross-check: E11.04 Computational coherence models

## Re-opened sources (10 numbers checked)
Confirmed against the source text (opened this session):
1. IBE-Eval (arXiv 2402.10767): 77% accuracy, +27 over random, +17 (avg +17.5) over GPT-3.5 judge, human 96%/91% -- confirmed (b08, a27).
2. Maieutic prompting (arXiv 2205.11822): "up to 20% better" confirmed from abstract; table numbers 72.5 / 61.4 not re-read, they agree across b03 and c19.
3. ConCoRD Table 1/2 (arXiv 2211.11875): 0.831->0.914, 0.855->0.931, LXMERT 0.656->0.706, ViLT 0.784->0.804 -- confirmed.
4. Logic-LM (ACL 2023): +39.2 / +18.4, and GPT-4 rows (FOLIO 69.11/70.58/78.92; ProntoQA 77.40/98.79/83.20 etc.) -- confirmed.
5. Thagard and Verbeurgt 1998: 0.878 guarantee, NP-hard, "more than a dozen cases" -- confirmed.
6. Deductive closure training: "3-26%" and "12% unsupervised on CREAK", incoherent rate 34.4 / 20.4 -- confirmed.
7. Forst and Glockner 2026: decision times 9241 vs 5583 ms found in the page text; N=128 string not found by simple grep (not re-confirmed).

Corrections made:
- C1 (b01): BeliefBank raw model F1 is about 69%, not "about 72%". The 72% F1 / 74% consistency belongs to the random off-topic feedback arm. Table 1: raw 69.3 at batch 10; constraints-only 85.8; relevant-FB + constraints 86.6; relevant-FB only 79.5. So solver alone gives about +16.5 F1, the paper says "~+17%". Consistency "~95%" (b01 said 96%).
- C2 (b22, b05): "Gold constraints give the highest gains" is wrong for BeliefBank in ConCoRD. Table 1: ConCoRD F1 0.914 beats the gold-constraint solver (0.862) for Macaw-Large; 0.931 vs 0.905 for 3B. Gold wins only on ConVQA (oracle 0.824 vs 0.706) and NQ. Also c22 already noted this; b22 and b05 limits contradict it. Claim K12 marked contested.
- C3: BeliefBank base F1 differs by paper (0.693 in BeliefBank, 0.831 in ConCoRD) because models and constraint sets differ (ConCoRD used 4,060 ConceptNet constraints, 601 predicates, 85 entities). Do not mix them.
- C4: a12 gives parameters excitation .04, inhibition -.06 for von Bulow, versus .05 / -.2 in 1989; a14 says guilt rejected when inhibition exceeds .065. Parameters change per paper, so "defaults" are not stable across the author's own studies.

## Contradictions between sources
- Lehr (a28/c12/c13) says GPT-4o shows dissonance moderated by free choice; Cummins (c14) says valence shifts occur even when the user wrote the essay. Both are about one model and one topic; the Cummins paper was a two-page commentary, sample sizes unknown. Unresolved.
- IBE-Eval: logical consistency is uninformative (b09) while coherence-from-theory is the paper's framing. The coherence idea works only through parsimony and hedging features.
- Thagard says coherence tends toward truth when it broadens and deepens (c03); probabilistic coherence authors say it need not (b20, from memory only).
- a22: strong coherence shift plus mostly disconfirmatory search conflicts with the common confirmation-bias reading.

## Weak spots
- All ECHO legal "successes" (Chambers, Peyer, von Bulow, Vincennes) are retrodictions with author-coded input; Peyer (jury 7-5) is a partial miss read after the fact; Simpson is a failure of pure ECHO fixed after the verdict. No blind coder study, no intercoder reliability (a06).
- The Bayes comparison (a13, a14) used guessed probabilities.
- LLM evidence is all pre-2024 small models except IBE-Eval (GPT-3.5/LLaMA 2) and the GPT-4o dissonance studies. No frontier-model test of solver-over-claims found.
- Self-review by the model's author (a16, a18, c02).

## Seen only in snippets or abstracts (do not quote numbers)
a19 Holyoak and Simon 1999 (paywalled), a20 Simon et al. 2004 (abstract), a21 and a22 Glockner (abstract), a25 Simon and Read 2025 (abstract), a30 Abduction In Silico (abstract), a31 graph-construction benchmark (title only), b11 Simon 2004 (abstract), b12-b18 and b20 (from memory, not opened), b19 Araszkiewicz (record only), c05, c07, c08, c09 (records only; but a12-a14 cover the content from the author's PDFs). c06 scanned PDF unread (a01-a09 read the gwern copy instead).
Impact: the "founding human experiment" numbers (Holyoak and Simon 1999: effect sizes, N) are still missing. K07 rests on abstracts plus one opened preprint (c10) and the opened PMC studies.

## GAPS
1. What are the exact effect sizes and N in Holyoak and Simon 1999 and Simon et al. 2001/2004 (pre/post evidence ratings), and do they persist when the pre-rating is taken in a separate session?
2. Does an LLM (frontier model, 2025-26) show a coherence shift on legal evidence when it rates evidence, gives a verdict, then re-rates in the same context versus a fresh context? (No study found.)
3. Does a code-run coherence solver (ECHO or MaxSAT) over an LLM-built evidence graph beat majority vote or CoT at equal tokens on frontier models? Prior gains are on 2021-22 small models.
4. How much does the verdict vary across independent graph builds of the same case (intercoder reliability of LLM graph construction)? Read the "benchmarking graph construction for coherence-driven inference" paper (a31).
5. Which link source works best on current models: LLM-judged, NLI, or gold? ConCoRD shows no consistent winner.
6. What did Thagard's replies to the 1989 commentators (Achinstein, Chi, Dawes) concede, and did any independent group replicate ECHO on human confidence data (Ranney and Schank, Read and Marcus-Newhall)?
7. How often does a solver flip a true, strongly supported claim to a false, well-connected one (rat/cat type errors)? Need a rate.
8. Are Bovens-Hartmann/Olsson probabilistic coherence results (agreement among sources as evidence) read and tested against ECHO on multiple-testimony tasks?
9. Does Logic-LM-style routing by task type (solver for strict deduction, CoT elsewhere) hold on current models, and what is the formalisation-failure rate?
10. What did Cummins et al. report for sample sizes, and does the context-window account survive a design that varies authorship with matched content?

## Gap search results (2026-11-10)
Evidence in evidence_d.jsonl (d01-d17). Claims K03, K06, K07, K11, K14, K18, K20, K22 updated; K23-K28 added.

1. CLOSED (mostly). Holyoak and Simon 1999 Exp 1: N=54 (48 analysed), verdict x test F(1,44)=35.3; pretest Q .37 v -.20, posttest 1.42 v -1.56. Exp 2 (N=19, pretest one week earlier) still F(1,17)=7.71. Simon et al. 2001 (this is the JEP:LMC paper, not the 2004 Psych Science one): N=50/125/166, F(2,86)=35.3, F(2,236)=59.1, F(2,302)=78.6; baseline gap .80 grew to 2.55. No effect sizes are reported in the papers; pre-ratings were taken in the same session except Exp 2. Independent 2026 replication (Qiao et al., N=130) F(1,128)=96.31 in agreement ratings, but not in likelihood ratios.
2. OPEN. Re-searched; no LLM study of rate, verdict, re-rate in same versus fresh context on legal evidence. Closest is Lehr and Cummins (K20). The cheapest gap to run ourselves.
3. PARTLY CLOSED. VERGE (2026) beats CoT and self-consistency (k=3) on FOLIO (Sonnet 3.7: 87.9 v 72.4 SC, 70.4 CoT) and other benchmarks, but it is SMT entailment on formal-logic tasks, token cost not equalised in the text read, and a specialised baseline wins ProofWriter. No coherence solver over LLM-built legal evidence on frontier models.
4. PARTLY CLOSED. Huntsman and Thomas (2025): 76 synthetic graphs, perfect reconstruction about half the time on sparse graphs (o1/3/4-mini); no repeat-build variance, no real cases. Real-case intercoder reliability is still unmeasured.
5. OPEN. No current-model comparison of LLM-judged, NLI and gold links found. ConCoRD result (K12) stands as contested. VERGE shows unanimous cross-model formalisation helps (76.7% v 56.0%), an indirect hint that agreement across models is the best available link filter.
6. HALF CLOSED. Thagard's 1989 replies read: concedes ECHO analyses are not good psychological tests (Klayman and Hogarth), answers Dawes's Simpson challenge by adding an alternative hypothesis, accepts probabilities where available (Papineau), calls himself a weak explanationist. Independent replications (Schank and Ranney, Read and Marcus-Newhall) not opened; Ranney and Thagard 1988 report was blocked (403). Still open.
7. OPEN. No flip-to-wrong rate in any study. REFLEX gives only net effects (accuracy -0.2 to +1.0 with consistency +8 to +11) and a 50-case failure profile (30% missing rules, 30% uncorrected wrong beliefs, 10% bad rules).
8. OPEN. Bovens-Hartmann and Olsson tests not opened; Koscholke and Jekel (2016) paywalled.
9. PARTLY CLOSED. Routing evidence on 2025-26 models: solver wins on FOLIO, ZebraLogic, AR-LSAT, loses to PoT on ProofWriter. Formalisation failure: 23.3% of unanimous formalisations wrong on FOLIO, gold formulas agree with labels only 72.6%, 20B model about 30% valid syntax. Not tested on legal text.
10. CLOSED on design, open on size. Cummins et al. varied authorship (user-supplied v model-written essay) with matched content in three studies; valence effect in all. Sample sizes are not stated in the commentary; it did not re-test the choice-moderation contrast.

Limits of this pass: Semantic Scholar, OpenAlex and arXiv API were rate limited; web search budget ended after about 5 calls. Cummins and VERGE are preprints; Qiao is a conference paper with Holyoak as co-author.
