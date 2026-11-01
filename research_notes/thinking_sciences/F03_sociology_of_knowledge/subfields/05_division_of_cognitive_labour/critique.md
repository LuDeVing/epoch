# Cross-check: F03.05 Division of cognitive labour

## Numbers re-opened this session (11 checks)
Confirmed against full text (PDF or PMC page):
- Hong and Page 2004 (a18): 92.56 vs 94.53, diversity 70.98 vs 90.99 (10 agents, l=12). Confirmed.
- Derex and Boyd 2016 (a20): 144 students, 50% A3 and 33.3% B3 fully connected; 91.7%, 66.7%, 58.3% partial; 0% both in full. Confirmed. Group count (24) is inferred, not stated as such.
- Mason and Watts 2012 (a21): 138 of 232 sessions, 59.5%. Confirmed. The 68 vs 39 score line was not re-checked.
- Choi et al. 2026 (b13, b14): T=50, 30 runs, pA 0.6 vs pB 0.5 in the main figure; Table 1 (pA 0.6 vs pB 0.4): 50.0/23.3/0.0/0.0% lock-in, regret 20.0/13.5/9.9/9.8. Confirmed. Note the two settings differ (0.5 vs 0.4 for the second arm); do not merge them.
- Krishnamurthy et al. 2024 (b17, b18): GPT-4 basic prompt suffix failure in over 60% of replicates; only three GPT-4 configurations avoid it. Confirmed.
- Coral Discovery (c01, c02, c04, c05): HHI 1.00/0.66, 1.00/0.36, 0.82/0.29; 1095 vs 1138; 91.78 vs 80.55; 68 vs 41 directions; 34 vs 15; 9/4/15 vs 0/0/4 local records; 76% of 38 evals. Confirmed.
- CORAL (c09, c10, c11, c12): 1103 vs 1350, 18.3%; Jaccard 0.43 and 0.31; 12% code transfer; 87% of rounds cite notes; 1350 to 1601 (18.6%). Confirmed.
- Si et al. 2024 (b25, c17): 4000 seeds, about 200 non-duplicate, about 5%. Confirmed.
- Wang et al. DIV-SE (b19): Blocksworld 3 70/73/94; graph colouring 15/23/97. Confirmed. Blocksworld 4/5 line (40/41.2) not re-checked.
- Brown et al. Large Monkeys (b23): 15.9% to 56%; 82.9% to 98.44%; 40.50% to 41.41%. Confirmed.

## Corrections and additions
1. c02 omitted a key caveat. Coral Discovery's 6 wins, 1 tie, 2 losses is against the authors' reproduced baseline and the better of single agent and 4-agent baseline, best of 3 runs. Against the numbers published by the original CORAL paper it is 4 wins, 2 ties, 3 losses; the 3 losses are to numbers obtained with web access and grader reading. Claim K09 states both.
2. Duplicate records, counted once for independence: b25 = c17 (Si et al.), b26 = c22 (Artificial Hivemind), b29 = c26 (Co-Scientist), b02/b04 share Thoma's reading. Independent-source counts in claims.jsonl already account for this.
3. b14 and b13 use different arm probabilities. Kept separate.
4. Two systems named "CORAL" (MIT Qu et al., Coral AI Labs Ren et al.). They overlap in lineage (Coral Discovery builds on and reproduces CORAL), so they are treated as partly independent: counted separately only where the claim is about different findings.
5. Coral Discovery arXiv 2610.33281 and Choi 2607.11250 are very recent (Oct 2026), single version, not yet peer reviewed; treat as preprints.

## Contradictions between sources
- Connectivity: Derex and Boyd (less contact is better for accumulation) vs Mason and Watts (efficient networks better on a one-peak landscape). Likely a task-structure effect (combination of innovations vs finding a single peak), not a true conflict, but no single study tests both.
- Mavericks vs mixes: Weisberg and Muldoon say mavericks dominate; Thoma says the ranking flips with movement range; Wu (2024) says better-than-best depends on parameters (holds in over 74% of combinations).
- CORAL says sharing helps; Coral Discovery says score-only sharing makes agents follow the leader and collapse. Compatible: sharing notes helps, sharing only scores hurts diversity. Not tested head to head.
- Schema tension: DIV-SE, Hegazy and Heter-MAD report gains from strategy or model diversity, while G4 bans persona or strategy voters on single-answer problems and G9 bans debate. The reconciling reading: diversity helps open search and coverage; for single-answer problems it needs a check and code selection. Unresolved by the evidence.

## Weak spots
- The core theory papers (Kitcher 1990, Strevens 2003, Zollman 2007/2010, Alexander et al. 2015, Thoma abstract-level items, Poyhonen, Bedessem) were not opened or yielded no numbers. K01 rests on a review and a blog summary. The Kitcher 0.51/0.49 phlogiston example is second-hand.
- Hong-Page generality criticisms are known to exist but are not in our evidence; K05 is single-source.
- No LLM study tests a credit or priority rule directly. Coral Discovery frames its direction board as one but has no ablation of claim cap (2) or pivot threshold (5).
- Most agent results are best-of-3 on 9 tasks; margins on several tasks are in the third decimal (Erdos 0.380984 vs 0.381264, Circle-Pack, EPLB).
- Equal-token accounting is missing in most LLM papers (MoA, DIV-SE partly; Coral Discovery matches eval budget, not tokens).
- Evolutionary-search ablations (c19, c20) have no numbers in our records.

## Only seen in snippets or abstracts
a01, a04, a05, a14, a15, a16, a17, a24, a25, a26, a27, b01, b03, b11, b12, b24, c27, c28, c29. Do not cite numbers from these.

## GAPS
1. Does a code-set allocation of untried directions beat the same number of free attempts at equal tokens on an open task? No source runs this ablation (Coral Discovery matches evals, not tokens, and ablates nothing).
2. What is the best pivot or abandon threshold? Both CORAL systems use 5 non-improving evals with no sweep.
3. What is the right per-direction cap (Coral Discovery uses 2) and does a cap beat a quota for a single agent with sequential attempts, not four parallel agents?
4. How should the explore share shrink over a run? Evidence shows champion concentration (76%) but no schedule tested.
5. What does the replication and criticism literature say about Hong-Page, Weisberg-Muldoon (Alexander et al. 2015; Fernandez Pinto 2018) and Zollman (Rosenstock 2017)? Open the full texts and record numbers.
6. Can a single model be made to propose genuinely different directions (verbalized sampling, seed lists, forced negative prompts) and does direction diversity predict final score, or only novelty?
7. Does the Kitcher result hold when success estimates are noisy LLM self-ratings (G8 says model judges are near chance)? Test with a noisy-prior simulation.
8. Do shared notes help a single agent across its own attempts (memory) without causing the follow-the-leader collapse? CORAL and Coral Discovery disagree on the mechanism.
9. Where are the human field studies (peptic ulcer, funding portfolios, Wu and O'Connor on transient diversity) with real counts of researchers per approach? None opened with numbers.
10. How large is the coordination overhead (MAST 41 to 86.7% failure) for a one-agent scaffold that only simulates division of labour in sequence?

## Gap search results (evidence_d.jsonl, d01 to d23; claims K20 to K28 added, K02/K03/K05/K12/K19 updated)

Tool limits this session: WebSearch budget was used up; OpenAlex, Semantic Scholar and the arXiv API returned 429; AMS Notices, PhilSci-Archive, Cambridge and Chicago PDFs returned 403. Opened full text came from arXiv PDFs, PMC/Europe PMC and the Stanford Encyclopedia page. Crossref gave abstracts only (marked opened:false).

Status per gap:
1. CLOSED ONLY IN PART. No study runs the code-set vs free-attempts ablation at equal tokens. Nearest measured: Darwin Godel Machine ablates the parent rule (50.0 vs 39.7 SWE-bench, 38.0 vs 30.0 Polyglot; d01) at equal iterations. Own toy simulation (d22) predicts a code spread wins when the model's own ranking is weak and loses when strong (rho 0.6). The real test is still open.
2. OPEN. No sweep in any source. AIRA-dojo shows exploration settings did nothing with weak operators (d03). Own toy: best threshold 2, 5 never clearly best, flat when direction improvement is slow (d23). Treat as a hypothesis to sweep.
3. OPEN, one lead. DGM uses a soft cap (weight over 1 + children, d02) and no one compares it with a hard cap. Toy: cap 2 then exploit best (d22); cap 3 equal to exploring to the end was worse.
4. OPEN. No schedule tested in the literature. Review (d19) supports explore early and converge later at a cost in time. Toy: exploit for the last 30% of attempts, never-exploit worst (d23).
5. PARTLY CLOSED. Framing confirmed from a review (d13) and abstracts of Alexander et al. 2015, Thoma 2015, Rosenstock et al. 2017, Grim et al. 2019 (d14 to d17). All four contest the original results (maverick dominance, less-connection-is-better, diversity-beats-ability). No numbers: full texts are paywalled. K05 moved to contested, K25 added. Thompson 2014 (AMS Notices) and Fernandez Pinto 2018 were not opened.
6. PARTLY CLOSED. Verbalized sampling raises diversity 1.6 to 2.1x and human-rated diversity from 1.90 to 2.39 (poem; d07). Diversity did lift a downstream score: 30.6 to 36.1 and 37.5 (d08). Self-MoA regression shows diversity predicts score but with lower weight than quality, and mixing weaker models hurts (d09, d10). Seed lists and forced negative prompts: no source found. Not shown for research directions.
7. CLOSED BY SIMULATION ONLY. Own noisy-prior toy (d21): credit-seeking allocation falls below an equal split at log-noise sd about 0.25 to 0.5 and is far below it at chance-level ratings; equal split holds 83 to 91% of optimum at any noise. Supported in kind by AIRA-dojo, where the agent's own score keeps rising while held-out score plateaus (d05). No LLM self-rating experiment exists.
8. PARTLY CLOSED. For a single agent, AIDE with or without a memory of earlier attempts: nearly identical medal rate (d04). Scoped memory (siblings only) is a design claim, untested alone. The CORAL vs Coral Discovery disagreement is not resolved; K22 marked contested.
9. OPEN. Rzhetsky et al. 2015 gives the best field-data evidence (d20: strategy over 3x more costly than best alternative; efficiency peaks at 13% of network discovered) but it is model-based inference on MEDLINE, with no counts of researchers per approach. Wu and O'Connor 2023 is a modelling paper (d18). No peptic-ulcer or funding-portfolio counts found.
10. PARTLY CLOSED. MAST splits failures 41.8% design, 36.9% inter-agent misalignment, 21.3% verification (d12), so a sequential one-agent scaffold avoids at most the 36.9%. No study measures single-agent-simulating-roles overhead. MAD does not reliably beat single agent plus self-consistency (d11).

Caveats on this section: d21 to d23 are my own toy models with assumptions I chose (learning curve, noise, ceilings). They give predictions, not evidence about LLMs. Equal attempts were treated as equal tokens. Scripts are in D:/research_scratch/F03.05/tmp/ (F03.05_kitcher_sim2.py, F03.05_seq_sim.py).
