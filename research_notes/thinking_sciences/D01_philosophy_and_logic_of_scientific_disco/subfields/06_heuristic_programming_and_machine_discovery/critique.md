# Critique: D01.06 Heuristic programming and machine discovery

## Corrections made (sources re-opened this session)
Re-opened: LLM-SRBench, DiscoveryBench, Hypothesis Search, LaSR, Ideation-Execution Gap, AI Feynman, AI Scientist, Si et al. ideas, AlphaEvolve, Eureka, Beel et al.
Confirmed: AI Feynman 100 vs Eureqa 71 and 15% to 90% (a11, b01); LLM-SRBench 31.5% / 28.1% / 7.21% / 30.63% / 10.81% (a15, c05); LaSR 72 vs 59 and R2 0.913 vs 0.070 (c07, c08); Hypothesis Search 17 / 23 / 30 / 33%, Icecuber 43%, 49 correct hypotheses, 33 of 49 (a21); ideation-execution gap -0.010 / +0.078 / -0.052 vs -1.049 / -1.760 / -1.879, N=43 (b14); Si et al. 5.64 vs 4.84, 79 reviewers, 298 reviews (b13, c22); AI Scientist 70% vs 73%, F1 0.57 vs 0.49, AUC 0.65, under $15 (a18); AlphaEvolve 75% and 20% (b09); Eureka 83% and 52% on 29 tasks (c25); Beel 5 of 12 failed, 5 of 34 citations from 2020 or later (b11).
Corrections and flags:
1. a21 gave "human-written 45%" and "SyGuS 94.3% with 8 programs". The text I read only says Icecuber's 43% is "slightly underperforming" human-written, so 45% is plausible but the exact table value was not re-read. SyGuS figure unverified; dropped from claims.
2. a17 and b07 read DiscoveryBench domain hints as a gain 9.9% to 17.5%. The paper's sentence literally says "9.9% (w/ domain knowledge) to 17.5% (w/o)". Direction is ambiguous; claim K13 is marked contested.
3. a11/b01 "AI Feynman 100/100" is the authors' own run with tuned symbol sets (1-2 extra hours on some equations). LaSR's table gives AI Feynman 38/100 and SRBench 53% exact at zero noise. Not a transcription error, a setup difference. Claim K07 marked contested.
4. b04 (EmpiricalBench) and c13 (AI Scientist model table) have cells the original agents flagged as garbled or inferred. Not used in claims.
5. AlphaEvolve rank-48 is for complex-valued 4x4 matrices; the 49 baseline is recursive Strassen; lower ranks exist over other fields. State it that way.

## Contradictions between sources
- AI Feynman strength: own paper 100/100; LaSR 38/100; SRBench 53% (zero noise), worse with noise. (Evidence a11, b01, b03, c07.)
- Self-critique: DiscoveryBench says it does not help; AI co-scientist and AI Scientist rely on model judges and report gains. The gains there are self-graded.
- LLM idea novelty (b13) is high before execution; after execution it reverses (b14).

## Weak spots
- Most strong LLM numbers (LLM-SR, LaSR, AlphaEvolve, Eureka) come from the authors, one backbone family each, and tasks with a hard numeric checker. Not transferable to open reasoning tasks without a checker.
- Symbolic accuracy in LLM-SRBench is judged by GPT-4o.
- Small samples: 100 ARC tasks (one model), 15 curated co-scientist goals, 3 AI Scientist-v2 papers, 41 LaSR synthetic equations.
- No direct test of the founding claim, that a small heuristic list suffices, against a modern LLM at equal tokens.

## Only seen in snippets or secondary
Unopened primaries: King 2004 and 2009 (Adam), Kulkarni and Simon 1988 (KEKADA), Langley 1981 and the 1987 book, FunSearch (Nature). Their numbers come from reviews or press (a07, a09, a25-a28, b18-b20, c12, c26, c27). Not rechecked: co-scientist expert rank 2.36 (a20); Eve 2015 simulation ("a third to a half") beyond what a22 read; MOOSE-Chem and PaperBench not covered.

## GAPS
1. Does a short signal-to-operator table (BACON-style) beat free reasoning by a modern LLM at equal tokens on freshly disguised law-finding tasks? No study tests this directly.
2. What does KEKADA actually do on surprise (heuristic list, experiment counts, how goals were set)? Primary paper never opened; needed to design the impasse trigger.
3. Which part of the LLM-SR/LaSR gain survives when the checker is weak or noisy, or absent (open reasoning tasks)?
4. What is the true DiscoveryBench effect of domain-knowledge hints (direction and size)?
5. Does model-judge ranking (Elo, reviewer) predict external truth better than chance? Only wet-lab and execution studies (b14, a23) speak to it. Need more.
6. How many hypotheses per budget is optimal: Hypothesis Search (64 candidates, 8 summarised) vs sparse-call LaSR vs 16 x 5 Eureka? No equal-token comparison across styles.
7. Do cheap-first ladders (AI Feynman style) beat random operator order in an LLM agent? Only the symbolic-regression case is measured.
8. Do robot-scientist results (Adam 2009, Eve 2004/2015) show a measured advantage of active experiment choice over random choice, with exact numbers? Primaries unread.
9. How does on-line revision of an accepted model after contradicting data work in LLM agents (Langley's open challenge)? No measured study found.
10. Do FunSearch/AlphaEvolve-type gains persist with a small open model at the same token budget (c11 says larger LLMs help, no single number)?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d20). Web search quota ran out during this pass, and the arXiv, Semantic Scholar and OpenAlex search APIs were rate-limited. Papers were opened by known arXiv id, Europe PMC and Crossref. So "no study found" below means "not found with these limits", not "none exists".

1. BACON-style table vs free reasoning at equal tokens: STAYED OPEN. No direct test found. Nearest: Self-Discover (d20), a 39-module generic heuristic library chosen per task, BBH +7/+6 over CoT at far lower cost, but not data-triggered and no random-module control. NewtonBench (d02, d03) is a ready testbed: 324 counterfactual law tasks, interactive, with a noise knob.
2. KEKADA on surprise: STAYED OPEN. Only the abstract was reachable (d17; publisher and ScienceDirect blocked). It confirms surprise leads to explanation goals and that the heuristics are claimed to be largely domain-general. Heuristic list, experiment counts and goal rules are still unread. The impasse trigger should be built from the abstract's claim only, and marked unverified.
3. Gain with a weak or missing checker: MOSTLY CLOSED (direction and rough size). Selection by voting or a reward model plateaus after about 100 samples (d04: 40.50% to 41.41% while coverage goes 82.9% to 98.44%). Stronger search against a learned checker hurts easy items (d05). Noise of 0.0001 cuts exact-form accuracy 12-16% while fit error is flat (d03). No study measures LLM-SR or LaSR itself without its checker.
4. DiscoveryBench hint direction: CLOSED by reading (d01). The labels in the sentence are swapped; 9.9% is without hints and 17.5% with. The gain is +7.6 points on an unstated subset. K13 changed from contested to single-source.
5. Does a model judge predict truth: PARTLY CLOSED. Untrained frontier judges are about chance on real outcomes (51.9%); a fine-tuned judge reaches 77% on published pairs but 63.6% on 33 new ideas (d13). Elo or reviewer scores from the co-scientist and AI Scientist systems remain unvalidated.
6. Best number of hypotheses per budget: STAYED OPEN for a cross-style equal-token comparison. Partial: at 64 programs, hypotheses-then-programs beat raw programs (d07); 2x16 evolution beat 32 fresh samples (d09); compute-optimal allocation depends on difficulty (d05, d06). The hypothesis layer adds nothing when direct attempts succeed (SyGuS 94.3% both, d08).
7. Cheap-first ladders vs random order in an LLM agent: STAYED OPEN. Nothing found beyond symbolic regression. Self-Discover tested module selection but not order.
8. Adam/Eve vs random choice: PARTLY CLOSED. King 2004 abstract gives 3-fold and 100-fold cost cuts vs cheapest and random selection (d14; pairing unconfirmed). Eve 2015 only shows an economic replay (d15). Adam 2009 full text unread; its gene count is 12 per a review (d16), so the earlier "6" is unresolved.
9. On-line revision with contradicting data: PARTLY CLOSED. Nearest measured: WorldCoder revises code world models from exact counterexamples (d19) and LLMs update beliefs poorly across rounds without training (d18). No study contradicts an accepted scientific law mid-run.
10. FunSearch / AlphaEvolve with a small open model: STAYED OPEN. FunSearch primary now opened (d12): about 10^6 samples, "not too sensitive" to the code LLM, StarCoder comparison in an unread supplement. AlphaEvolve says larger models help (d11, no number). ShinkaEvolve (d10) uses a frontier ensemble.

Claims changed: K05 (abstract read), K13 (contested to single-source), K21 and K22 (evidence added), K23 (Adam count flagged, King 2004 numbers added), K25 (evidence added). New: K26-K34. Resolved flags from the cross-check: Hypothesis Search SyGuS 94.3% and human-written 45% are both confirmed from the paper (d07, d08).

Next steps if more budget: read the FunSearch supplement; the King 2009 and Kulkarni-Simon 1988 full texts; run the NewtonBench arm test for gaps 1 and 7.
