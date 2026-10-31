# Critique, E08.01 Cognitive models of troubleshooting

## Corrections made (checked against arXiv full texts of 8 papers)
1. b09 said step limits beyond 5 gave no gain for agents in general. AIOpsLab says that only for GPT-3.5; ReAct and FLASH improved with more steps, FLASH peaking at 59.32% at limit 20. c04 is right. Claim K15 uses the corrected reading.
2. a26 said the ablations ran on "303 forum threads". The SIA paper (b12) used 100 cases drawn from 303 threads.
3. ITBench: main text says GPT-4o diagnosis 13.81% with traces vs 9.52% without; the appendix says 18.10% vs 9.52%. The paper contradicts itself.
4. SADE: ReAct F1 is 0.40 in the abstract and 0.44 in the body. Confirmed inconsistency.
5. UoT: "38.1%" is an average improvement across datasets (apparently relative); the troubleshooting move 43.7 to 67.3 is +23.6 points absolute. Do not mix them.
6. Huang et al.: c19 labels "rounds 0,1,2" are wrong; the table is by number of calls (1, 3, 5) and is garbled. Direction (decline) and GPT-4 numbers (95.5, 91.5, 89.0; oracle 97.5/85.5/59.0) confirmed.
7. Confirmed unchanged: Roy 2024 (66% insufficient evidence; CoT 32%, RB 18%), AIOpsLab (49.15, 15.25, 55.93, 59.32), SIA ablation (79.2, 72.8, 74.0, 76.5 with potential 79.3), FaulT-Bench (0.912/0.942/0.941, 0.820, 24% = 51/210).
Not re-opened: Mamede, Lambe and PMC7807127 medical studies (earlier agents read PubMed pages), Savage, Flow-of-Action, MAST.

## Contradictions between sources
- Reflection: Mamede helps residents on hard cases; Lambe and PMC7807127 find no effect; the review says it depends on how reflection is instructed.
- Structured scaffolds win in SADE and Flow-of-Action, but Roy finds ReAct no more accurate than CoT (only less hallucination).
- Case retrieval helps little (Ahmed, Roy) although Jonassen and Hung propose case libraries.

## Weak spots
- The founding human result (Schaafstal 2000) is known from an abstract only: no N, no effect size. Jonassen and Hung 2006 never opened. Schaafstal 1993 not found. Johnson 1988 and Van Gog 2005-2008 only in reference lists.
- Human evidence for the cycle is 8 student pairs on one circuit, with no outcome link.
- Most LLM results use authors' own judges, simulated users, 2024-era models or tiny problem sets (AIOpsLab about 11-13 per level, one run). 2026 papers are unreplicated.
- No source tests the four-task cycle as a prompt against a free baseline at equal tokens.
- Software fault localisation (Kang, Agentless) is outside the human-cognition core.

## Only seen in snippets
a19, a21, a22, a23, a28, b24, b25, c31, c32; QoEReasoner (b18) partly garbled.

## GAPS
1. Does an explicit describe-causes-test-verify cycle beat a plain ReAct loop at equal tokens on the same fault set (the missing direct test)?
2. Does a "no fault found" exit plus verify gate cut over-diagnosis without losing true detections (FaulT-Bench, AIOpsLab Noop)?
3. Does code-computed split-half or information-gain probe selection beat LLM-chosen probes on realistic fault graphs?
4. What are the exact N, error counts and effect sizes in Schaafstal et al. 2000, and did anyone replicate it?
5. What does Jonassen and Hung 2006 report empirically, and has its case-library design been tested?
6. When is forced reflection helpful vs harmful for LLMs (signal-triggered vs always-on)?
7. Do case libraries of past faults help LLM agents when judged by humans rather than lexical metrics?
8. How much does recall-first diagnosis cause needless repairs in LLMs compared with humans (5 of 8 pairs)?
9. What do Van Gog et al. give in numbers on expert vs novice orientation (S1)?
10. Are the 2026 results (SADE, SIA, FaulT-Bench) reproducible with independent judges?

## Gap search results (evidence_d.jsonl d01-d20; claims K20-K29 added)
Search note: WebSearch quota ran out early; the OpenAlex and arXiv search APIs returned 429. Work was done by opening arXiv full texts, Springer, Crossref and PMC pages directly.

Closed or mostly closed:
- Gap 5 (Jonassen and Hung 2006): mostly closed. It is an untested design proposal (conceptual model, hypothesis-testing simulator, case library). No participants or effect sizes in the abstract, and I found no test of the case-library design. Full text is paywalled, so the body was not read (d02, K24).
- Gap 6 (reflection): mostly closed as far as evidence allows. Correction: Mamede 2020 tested a feedback-based immunisation exercise, not in-the-moment reflection (0.40 vs 0.24 on bias-exposed vignettes, N=91; no gain on neutral ones). Lambe 2018: strict accuracy 0.47/0.42/0.41, N=186, no gain, 62% backfire in the short condition; lenient scoring faked a gain. LLMs: always-asking cost 11.3% and confidence-gated asking gave +22.3% (MediQ); Kamoi's survey finds gains only with external feedback. Best-supported rule: signal-triggered, not always-on. No direct LLM test of signal-triggered vs always-on reflection on faults (d12, d14-d16, K13, K23, K26).
- Gap 3 (partly): BED-LLM shows code-computed expected information gain beats LLM choice among the same candidates in 20 Questions (+37.4 points over prompt-only; example 93 vs 70). Not tested on realistic fault graphs, and table column labels are inferred from the header (d11, d13, K22). Still open for fault graphs.
- Gap 2 (problem measured, fix untested): FaulT-Bench measures 11-24% false alarms on healthy networks, up to 74% for a vague ticket; AIOpsLab's no-fault problems (N=2) were failed by 3 of 4 agents. No study adds a "no fault" exit or verify gate and measures false alarms against missed true faults (d04, d05, d10, K05, K20, K21).

Partly closed:
- Gap 8: no LLM study measures needless repairs after recall. Indirect evidence only: 39% multi-turn drop from early commitment (Laban) and 10-26% loss from planted bias cues (Schmidgall) (d17, d18, K27).
- Gap 9: Van Gog 2005 abstract gives direction (experts orient longer and fixate on a fault-related component) but no numbers. The worked-example papers (2006, 2007) have no accessible abstract; ScienceDirect returned 403 (d03, K25).
- Gap 10: not reproducible by independent judges yet. SADE and FaulT-Bench share first and senior authors and both use gpt-5-mini as judge, so FaulT-Bench is not an independent replication. SIA uses its own LLM rubric and simulator; its margin over ReAct has overlapping 95% intervals. SIA keeps its lead on two other backbones (+6.2, +7.7) in the same paper (d04, d06, d08, d09, K28).
- Gap 7: no human-judged case-library study found. RCACopilot reports only qualitative on-call engineer satisfaction, and 24.96% of incidents (163 of 653) were new (d19, K17).

Still open:
- Gap 1: no study compares an explicit describe-causes-test-verify cycle with plain ReAct at equal tokens. SADE used a median of 344k input tokens vs 55k for ReAct (1.8x the same-backbone baseline); SIA asks twice the questions of ReAct. A token-matched arm must be built by us (d07, d08, d20, K29).
- Gap 4: Schaafstal et al. 2000 numbers are unreachable (abstract only on Pure, TNO and Crossref). No replication found. Do not quote more than "about twice as many malfunctions, in less time" (d01).

Corrections to earlier files:
- K13 said Mamede showed forced reflection helps; it tested an immunisation exercise with feedback. Fixed.
- K06 moved to contested: SIA agrees ReAct is no better than direct prompting, SADE shows ReAct far below a structured agent.
- Earlier critique treated FaulT-Bench as a possible independent check of SADE; it is the same group.
- Not re-opened this pass: Savage, Flow-of-Action, MAST, UoT.
