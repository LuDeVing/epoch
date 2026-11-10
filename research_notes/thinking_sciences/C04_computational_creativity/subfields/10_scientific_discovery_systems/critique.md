# Critique: C04.10 Scientific discovery systems (cross-check)

## Corrections made (sources re-opened as arXiv PDF text this session)
1. Si et al. 2024 (2409.04109): novelty 4.84 / 5.64 / 5.81, 49 ideas per arm, agreement 56.1%: confirmed. Note a16, b09, c13 are one study, so independent_sources = 1.
2. Si et al. 2025 ideation-execution gap (2506.20803): human 4.596 to 3.968, AI 5.382 to 3.406, novelty human 4.912 to 4.903, AI 5.778 to 4.729: confirmed.
3. LLM-SRBench (2504.10415): 31.5% and 28.1%: confirmed.
4. LaSR (2409.09359): CORRECTION. Abstract says 66 of 100 vs 59 for the best prior method; the table lists exact solves 59, 67, 69, 71, 72 for different settings. Use "66 to 72 vs 59" and name the setting.
5. AI Feynman 2.0 (2006.10782): 73 of 100 at noise 10^-1: confirmed (Table 3).
6. Beel et al. (2502.14297): 5 of 12 (42%), 4 of 7 missing figures, 4 of 7 wrong or hallucinated numbers, 5 of 34 citations from 2020+, $6-15 per paper: confirmed.
7. Kosmos (2511.02824): 79.4 / 85.5 / 82.1 / 57.9 confirmed. Wording: 85.5% "reproducible", 82.1% "validated with primary sources".
8. AlphaEvolve (2506.13131): 75% matched, 20% surpassed: confirmed.
9. Gupta and Pruthi (2502.16487): 24% of 50 documents; 88.8% / 89.0% with oracle access, 1.3% parametric only for Claude 3.5 Sonnet: confirmed.
10. Not re-opened: AI Feynman 1 (100 vs 71), DiscoveryWorld, DiscoveryBench, AI Scientist tables, PaperBench, co-scientist, MOOSE-Chem.

## Contradictions between sources
- AI Feynman wins its own papers (100/100) but in an independent comparison (b06) recovers 53% with no noise and is beaten by other methods above noise 0.01. Benchmark and noise decide the winner.
- LLM-SR reports large gains over baselines; LLM-SRBench shows best system under 32% once memory is removed. Gains do not generalise as far as first claimed.
- Si 2024 (AI ideas better) vs Si 2025 (AI ideas worse after execution): same group; the flip is the main result, so idea novelty alone should not guide the agent.
- LaSR 66 (abstract) vs 72 (table).
- AI Scientist reviewer 0.65 balanced accuracy on paper accept/reject (a10) vs 43.3% on idea ranking (b11): different tasks.

## Weak spots
- The BACON era (a01, a02, a03, b02, b03, b04, c01, c02, c28) was NOT opened (403 or snippets). Founding numbers (laws rediscovered, 4 of 14 subjects) are unverified.
- Many LLM-system claims are self-scored by the authors (co-scientist, ResearchAgent, Chain of Ideas, Robin, AlphaEvolve). Not independent.
- Some rows have no numbers extracted (c17 MOOSE, c23, c24, a03).
- Outside replications are few: only AI Scientist (Beel) and SRBench (La Cava).
- No evidence line directly tests "open mode with a running check at equal tokens". Nearest is the LLM-SR ablation (K21) and the ideation-execution gap (K02).
- Snippet-only: b03, b04, c28.
- Almost nothing here is "established" with two truly independent teams; most single-source claims are single because several evidence lines repeat one paper.

## GAPS
1. Does running a cheap execution check before ranking ideas close the ideation-execution gap, at equal tokens?
2. Has an independent group replicated Si et al. (ideation and execution), and with 2025-2026 models?
3. What exactly did BACON-era systems achieve (laws, noise tolerance, human subject study 4 of 14), from the original papers?
4. In equation discovery, how much of the LLM-SR/LaSR gain comes from the feedback loop vs the model's prior knowledge? What survives on LSR-Synth?
5. Can voting or self-consistency lift idea-ranking above judge accuracy of about 50%? Is any ranker above 60%?
6. Does retrieval-grounded novelty checking cut the 24% plagiarism rate, and at what token cost?
7. Do evolve-with-evaluator loops (AlphaEvolve style) work where the evaluator is noisy or non-code?
8. Which error types dominate in 2025-2026 discovery agents (coding, method, invented numbers), and which guardrail removes the most?
9. Is the Kosmos gap (85.5% computed vs 57.9% interpreted) reproduced elsewhere, and does tagging statements by type help self-audit?
10. Does a hypothesis bank (HypoGeniC) transfer to open-ended tasks without labelled data?

## Gap search results (evidence_d.jsonl, d01 to d22)

1. Execution check before ranking: PARTLY CLOSED. Liu et al. 2025 (d05, d06): a data-based validation shown to the judge raised ranking accuracy (Claude 69.0 to 78.9) and won human comparisons on feasibility (p=0.03) and expected effectiveness (p=0.02) but not overall (p=0.29). Si et al. 2026 (d07) shows execution-in-the-loop works on code-checkable tasks. No study compares at equal tokens. New claims K23, K24.
2. Independent replication of Si et al.: STILL OPEN. Searches found no independent replication of the ideation or execution studies, only follow-ups by the same group (d07, d09) and a different-domain study (d04) that is not a replication.
3. BACON-era numbers: PARTLY CLOSED. Simon 1995 (d01) settles 4 of 14 for Kepler's law and says BACON re-created a dozen or more discoveries; the 1984 tech report (d02) gives the noise-robust design. The 1987 book and the Qin and Simon paper were not opened, so exact law lists and noise tolerances stay unverified. K19 updated.
4. Loop versus prior knowledge: MOSTLY CLOSED. LLM-SRBench table (d19), LaSR synthetic test (d20) and SR-Scientist ablation (d18) show the loop and data tools give most of the gain on memorisation-resistant problems, but exact structure recovery stays low. K08 updated.
5. Ranker above 60%: PARTLY CLOSED. Off-the-shelf judges sit near 50% (d09, d10); above 60% needed outcome fine-tuning (77%) or a computed validation (d05). Self-consistency was the best prompting baseline for novelty ranking (d13, numbers not extracted). Voting on idea quality was not tested directly. K03 updated.
6. Retrieval-grounded novelty and plagiarism: PARTLY CLOSED. Staged retrieval and rerank gets 89.66% on known non-novel ideas vs 5 to 14% for single-stage (d12, 58 ideas); search cut false novelty 6.14 to 2.38 (d11). Effect on the 24% plagiarism rate and token cost: still open. K25 added.
7. Evolve loops with noisy or non-code evaluators: CLOSED in direction, open in size. AlphaEvolve authors report gaming of leaky and noisy evaluators (d16, d17). No measured rate. K26 added.
8. Error types in 2025-2026 agents: PARTLY CLOSED. Luo et al. (d14, d15) show silent scope change and positional benchmark choice (82.4%) and that logs lift detection from 55% to 82%. No cross-system tally exists. K27 added.
9. Kosmos computed vs interpreted gap reproduced: STILL OPEN. No independent source found this session.
10. Hypothesis bank without labels: STILL OPEN. HypoBench (d22) tests only labelled tasks (best recovery 93.8% falling to 38.8%).

Caveats: d03 is snippet-only (opened:false). d21 is a cross-reading. Several extracted tables are from PDF text and some cells in d19 are uncertain.
