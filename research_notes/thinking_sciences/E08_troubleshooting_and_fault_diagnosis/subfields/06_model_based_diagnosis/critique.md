# Critique: E08.06 Model-based diagnosis (cross-check)

## Corrections made (sources re-opened this session)
Confirmed against the PDF text: Olausson 2024 (GPT-4 feedback 33.30 vs human 52.60; 42.64/62.21, 19.33/45.67, 3.67/14.67); Feldman 2010 Table 4 (c880 CDA 11.6, HA 12.4, SAFARI 100; c1908 CDA 0, HA 6.1, SAFARI 100); Ignatiev 2017 (1140 benchmarks; LBX/RS full enumeration only 177 and 185); Orvalho 2025 (31%, 36%, 15% more programs; 6% fewer circuits; 480 valid = 70.38%); AIOpsLab (GPT-4 shell acc@1 61.54, ReAct 53.85, FLASH 46.15; RCA 45.45 / 40.90; FLASH 59.32); Vaccarino 2026 (1,006 of 8,559 vs 110 of 8,528; +12.9, +8.7); OncoRounds (68%, R=0.69, 57% to 26%, 91%); SemLoc (81.4 vs 82.0, 40.9%, 76.2/84.1, 99.4, 68.4/93.6).

Corrections:
1. a24 and b20 are the same paper (arXiv 2506.23083). Authors are Wu, Yu, Lee, Srinivasa, Zhai, Varghese, Tamir; b20 lists only three. Count as ONE source.
2. NetDx "30 of 33 real faults": the paper maps 33 in-domain faults to 8 equivalence classes and injects one fault per class; the 3 failures are intermittent faults counted as failures conservatively. So it is class coverage, not 33 separate live diagnoses. Fix wording in any synthesis.
3. a19 and b11 are the same paper; a23, b13, c04 are versions of CFaults; b12/c03 are the same paper. Independent-source counts in claims use this de-duplication.
4. CFaults figures differ by version: 2024 version 483/486 (99.38%) on C-Pack-IPAs; 2025 version 480 valid (70.38%) on a tested subset. Do not mix.
5. Greiner 1989 was not opened by anyone (b03 citation-only), though the counterexample in a07 was read. K02 rests on a07.

## Contradictions
- Scaffold vs plain LLM: SemLoc found no accuracy gain over an LLM with the same inputs (81.4 vs 82.0), while Vaccarino found large regression reduction (11.8% vs 1.3%). Benefit is safety and checkability, not raw accuracy.
- Best-first sampling is statistically biased (b08) yet gave fewest measurements; random samples estimated better. Ranking depends on measurement-time assumptions.
- Roy 2024: ReAct correctness (35%) below CoT (39%) but hallucination 4% vs 12%.
- Localisation helps tokens (a29) yet often costs more than it saves.

## Weak spots
- No source tests Reiter/GDE-style hitting-set reasoning inside an LLM loop at equal tokens against an LLM-only baseline. Closest: Vaccarino (MUS, not hitting sets), Matei (two cases), Nakos (synthetic).
- Most numbers are circuits or code with simulated faults; transfer to open-ended reasoning is untested.
- Founding papers have almost no empirical tables (a10 scaling claim is authors' assertion). Davis/Genesereth 1984, Bylander 1991, Greiner 1989, de Kleer 1992 not read in full.
- Contamination risk in Defects4J results (b14, c08).
- AIOpsLab N per task is about 11-13; differences of one problem are 8 points.

## Only seen in snippets
a14, a15, a31, b03, b04 (full text), c22-c28; c21 abstract only; a13 OCR-poor; a29 body skimmed; b18/b19 tables from garbled text (key cells re-checked now).

## GAPS
1. Does a code-run hitting-set / conflict step added to an LLM agent beat LLM-only diagnosis at equal tokens on a structured fault task (circuits, rule bases)?
2. Does code-computed entropy probe selection beat LLM-chosen next tests, and by how much, given the LLM failure to pick information (OncoRounds)?
3. How should the agent get a system model when none is given: can an LLM build a correct behavioural model, and what does an 5-10% wrong model do to diagnoses?
4. What is the regression rate of LLM self-diagnosis across task types, and does conflict-based gating (as in DRAGO) transfer outside specifications and PDDL?
5. Which cheap solver mode (exact, anytime, SAT-based) should a token-limited agent call, and at what problem size does exact fail?
6. How should the agent handle multiple simultaneous faults and intermittent faults (NetDx counted intermittents as failures)?
7. Do independent oracle errors (a quarter of human users erred in Rodler's study) have an analogue in LLM answers to probe queries, and how robust are diagnoses to wrong answers?
8. Is stated LLM confidence usable as the fault prior that entropy selection needs, given 84.1% accuracy at confidence 0.9+?
9. Do the Greiner, Davis/Genesereth and Bylander papers add boundary conditions (complexity of abduction) that limit the code-run reasoner?


## Gap search results (gap searcher, 2026-11-01)
Method note: web search, the arXiv API, OpenAlex and Semantic Scholar were all rate-limited, so sources were taken from known papers and opened as PDFs. New evidence is in evidence_d.jsonl (d01-d16); claims K19-K27 are new and K02, K05, K07, K10, K11, K13, K17 were updated.

Corrections carried from the cross-check: a24 and b20 are one paper (arXiv 2506.23083); the "30 of 33" figure counts fault classes, not 33 live diagnoses; a19 = b11, b12 = c03; a23, b13, c04 are versions of CFaults with different figures in 2024 and 2025. Greiner 1989 was opened in a07, so b03 (opened:false) is superseded.

1. LLM plus conflict/hitting-set vs LLM-only at equal tokens: STILL OPEN. No direct test. Closest: d01 (LLMs doing GDE steps themselves, o3-mini conflicts F1 0.917, diagnoses F1 0.784, falling with diagnosis count, authors say not a replacement) and d08/d09 (solver beats LLM-only on most rule/constraint sets, but CoT won on PrOntoQA 98.79 vs 83.20). K19 contested.
2. Code entropy vs LLM-chosen probes: PARTLY CLOSED. d02 and d03 show information-gain selection beats direct LLM choice by +38.1% and +37.4 points; d04 shows LLMs at 40-50% when picking the right question. Both used LLM-simulated probabilities; fully code-computed entropy on a device model is untested. K20 established for the LLM-simulated form.
3. Source of the system model: PARTLY CLOSED. d06 (GPT-4 2 to 53 errors per domain, GPT-3.5 350+; all 56 factual errors fixed with feedback) and d07 (94% valid, 25% behaviourally matching). Effect of a 5-10% wrong model on diagnoses: STILL OPEN; a30 gives the only model-checking number (97.4% vs 41%). K21, K22.
4. Regression rate: PARTLY CLOSED. d05 shows the same pattern outside specifications (GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0). Whether conflict gating transfers is STILL OPEN. K23.
5. Solver mode and size limit: CLOSED as far as evidence goes (K24): use anytime or SAT-based with a time cap; exact solvers failed at 880+ gates (0-12% in 1 min). No LLM-agent timing study exists.
6. Multiple and intermittent faults: PARTLY CLOSED. d14 gives the method and cost (2.7-5.5 vs 29-126 samples on ISCAS85) under 8 stated assumptions; no LLM study. K25.
7. Oracle errors: STILL OPEN. d13 confirms the algorithm cannot detect wrong answers. No LLM-oracle measurement found. K26.
8. Stated confidence as prior: CLOSED in the negative (K27): d10 AUROC 62.7%, d03 mode collapse; d12 shows entropy selection tolerates poor priors. d11 gives a counterpoint (calibrated over explicit options).
9. Greiner, Davis/Genesereth, Bylander, de Kleer 1992: STILL OPEN. Greiner already read (a07). Bylander blocked (403), Davis/Genesereth not found, de Kleer 1992 still only the OCR copy. Abduction hardness stays secondary-sourced (d16, a15).

Remaining unverified: d11 only partly read; d14 table columns reconstructed from garbled text; d02 reports FloDial GPT-4 as 42.5 to 67.8 in the significance table and 43.7 to 67.3 in the main text.
