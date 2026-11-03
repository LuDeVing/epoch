# Critique: E13.01 Joint cognitive systems (cross-check)

## Numbers re-opened this session
Confirmed against arXiv abstract pages or PDF text:
1. Vaccaro et al. (arXiv 2405.06087): g = -0.23 (CI -0.39 to -0.07, p = 0.005); augmentation g = 0.64 (CI 0.53 to 0.74); I2 = 97.7%; 5126 papers screened; 370 effect sizes from 106 experiments. All confirmed. Creation tasks g = 0.19 [-0.09, 0.48] p = 0.186 confirmed in the table.
2. Peng et al. (2302.06590): 55.8% faster confirmed (abstract). Time figures 71.17 vs 160.89 min not re-read.
3. METR (2507.09089): forecast 24%, estimate 20%, measured +19%, experts 39% and 38%: confirmed. 16 developers, 246 tasks: confirmed.
4. Kim et al. (2512.08296): 260 configurations, six benchmarks, five architectures, R2 0.373, +80.8% to -70.0%, beta -0.236 p 0.004 with 45% threshold, PlanCraft -39% to -70%, trace amplification 4.4 / 7.8 / 5.1 / 17.2: all confirmed in text.
5. Cemri et al. (2503.13657): 1642 traces, kappa 0.88 (humans) and 0.77 (LLM judge), 14 modes, clusters 41.8 / 36.9 / 21.3, +9.4% and +15.6%: confirmed.
6. Shao et al. (2412.15701): win rates 86/74/66 and failure rates 65% / 40%: confirmed in abstract.
7. Bucinca et al. (2102.09692): N = 199 and the direction of the finding confirmed in the abstract; the per-cell correct rates (0.03 vs 0.09) were not re-checked.

## Corrections and inconsistencies
- METR candidate factors: the abstract says 20 properties; evidence a18 and b17 say 21. Use "about 20" until the body text is checked.
- METR screen-recording share: b17 says 143 h of video and 44 valid recordings; c09 says recordings cover 29% of hours. These may describe different cuts. Do not quote either as a total.
- Vaccaro augmentation over all effect sizes appears as 0.64 in the text and 0.63 in the Table S row. Treat as 0.63 to 0.64.
- Evidence a25 and c25 (Dell'Acqua) are recalled numbers ("over 40% quality"). b20 opened the paper and gives the numbers used in the claims (+12.2%, 25.1% faster, about 19 points). Rely on b20 only. The quality figure was not re-verified.
- Error amplification (K14): the 17.2 versus 4.4 gap is real in the traces, but Kim et al. state the amplification term was not significant after controls (p 0.658). The claim is marked contested, not established.
- c18 and a20 both cite sample sizes of different surveys; not conflicting.

## Contradictions between sources
- Bansal 2021 (explanations add nothing) versus Vasconcelos 2023 (explanations help when checking is cheap). Reconciled by task difficulty; not a true conflict, but the reconciliation is from one lab.
- Peng 2023 (+55.8%) versus METR 2025 (-19%). Differences in task, expertise and tools; no controlled test separates them.
- Vaccaro (pairs lose on decisions) versus Bansal (pairs beat both when accuracies are matched). Fits the moderator "who is better alone".

## Weak spots
- Almost all human-AI evidence uses crowd workers, simulated AI, or classifiers. Almost none tests an LLM checking an LLM, which is our case.
- Vaccaro covers up to mid-2023 and over 95% of systems had the human decide, so it says little about program-final designs.
- Many claims rest on one source (single-source status). Only reading-cost, weaker-partner, task-class and verification-cost claims reach two or more sources.
- Collaborative Gym and Magentic-UI win rates use simulated users in part.

## Only seen in snippets or not opened
- Hollnagel and Woods 1983 and 2005, Woods and Hollnagel 2006, Hollnagel 2012, Klein et al. 2004, Sarter et al. 1997 were NOT opened. The core CSE ideas (joint system, COCOM, team-player requirements) are second-hand.
- Parasuraman and Manzey 2010, Mosier and Skitka automation-bias primary studies: not opened (b25, a08 via encyclopedia).
- Zhou et al. 2024 (REL-A.I.): abstract only.
- Automation-bias percentages in a08 (46% vs 21%, 29% to 50%) come from an encyclopedia page.

## GAPS
1. Does an LLM checker over-accept wrong LLM candidates the way humans over-accept AI, and does a different model family or independent first pass reduce it at equal tokens?
2. When does a program-side veto beat letting the model's answer stand? Vaccaro suggests it depends on who is better per item class; what is that split for our benchmarks?
3. What do Hollnagel and Woods actually claim on COCOM control modes, and do the mode names map onto a token-budget rule that can be tested?
4. Does extra checking help only on generative items and hurt on decision items (Vaccaro task-type moderator) when applied to a single model with a scaffold?
5. Is the single-agent saturation threshold (about 45%) reproduced outside Kim et al.'s six benchmarks, and does it apply to program-loop scaffolds rather than multi-agent topologies?
6. What is the real cost of verification in tokens (analogue of the 53.2% post-hoc verification in CUPS) for our scaffold versus plain?
7. Are there controlled replications of Bainbridge-style take-over effects with LLM agents (state lost after hand-back to the model)?
8. Does the Dell'Acqua frontier effect (loss outside the frontier) show up as a scaffold-induced loss on the hardest benchmark tier?
9. Which of Klein et al.'s team-player requirements (interpredictability, common ground, directability) have measurable LLM analogues, given Shaikh's finding of missing grounding acts?
10. Do METR-style felt-versus-measured gaps appear when an LLM judges its own scaffolded output?

## Gap search results
Evidence in evidence_d.jsonl (d01-d16); claims K23-K30 added.
1. PARTLY CLOSED. LLM checkers do not over-accept like humans; GPT-4 mostly under-accepts (30 of 500 colorings called correct, 5 right; FNR 20.7% to 97%, FPR 6.5% to 18.6%). Judges favour their own or familiar text (self-recognition 73.5%, tau 0.41). Other-family helps debate (+6.4%, +8.2%) but no equal-token checker test exists. (d01-d08)
2. PARTLY CLOSED. Where an exact program check exists it beats model verdicts (Game of 24 36-38% vs 3% LLM+LLM). The per-item split for our benchmarks is not measurable from literature; run it. (d02, d04, d10)
3. PARTLY CLOSED. Mode table read second-hand from Hollnagel 1993 p.22 (goals, available time, action choice, evaluation). Stanton 2001 test seen only as abstract. Token-budget mapping is a hypothesis, not tested. (d12, d13)
4. PARTLY CLOSED. Self-check hurt on QA (CSQA 75.8 to 38.1 GPT-3.5) and vote systems fall on hard items; no scaffold-vs-task-type split found. (d03, d09)
5. OPEN. No replication of the 45% threshold found; only indirect support. (d14)
6. OPEN. No source reports tokens per solved item for verify vs plain. (d15)
7. PARTLY CLOSED. Laban 2025: 39% multi-turn drop, unreliability +112%, over-reliance on own earlier attempts. Not a hand-back study. (d11)
8. OPEN, indirect support from d09 (easy gain, hard loss).
9. OPEN. No new measured analogue for interpredictability or directability found (search budget ran out).
10. OPEN. No direct study; indirect evidence only. (d16)
Not opened: Hollnagel books, Stanton full text (server 503), Klein 2004.

