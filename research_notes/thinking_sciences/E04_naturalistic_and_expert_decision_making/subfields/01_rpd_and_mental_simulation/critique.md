# Critique: E04.01 RPD and mental simulation (cross-check)

## Corrections made (sources re-opened this session)
1. Klein (1993) Table 6.1 (a33), full book text: confirmed 156/80%, 48/58% expert, 33/46% novice, 110/51% wildfire (56% functional, 39% organisational), 55/42% tank cadets, 51/60% design engineers; coder agreement 87-94%. The OCR row order is garbled but the text agrees. The oft-quoted "80%" is only the first row (all decision points, trivial ones included). Carry forward 42-80%, not 80%.
2. a26 (PMC13061108): 63.3, 67.6, 66.7 confirmed in the abstract. OR values and CIs not re-checked. The missing token-matched control stands.
3. a22 (PMC13100097): t(19)=-5.79, p<.001, d=1.30, Elo 2540-2812 mean 2671, 3 min vs 7.5 s per move confirmed. "18 of 20 worse in blitz" was NOT found in the page text; treat as unverified. The measure is expected blunders per move.
4. b04 Gontar (DLR page): abstract confirms "about one-third" RPD in 120 pilots. The 34%/66% and n=108 figures were not re-checked (full PDF not opened).
5. b14/c01 RAP: 17/2/0 CoT, RAP(10) 100/86/26, RAP(20) 100/88/42, and "33% relative over GPT-4" confirmed. The 33% compares LLaMA-33B RAP (64% average) with GPT-4 CoT, not token-matched.
6. b15/c03 ToT: 7.3/4.0/9.0, 45, 74, best-of-100 49% confirmed; GPT-3.5 ToT 19% confirmed.
7. b22 Stechly: Game of 24 row confirmed (standard 5%, LLM critic 3%, sound verifier 36/38%, sampling k=15 28%, k=25 42%). Emphasis correction: plain 25-sample sampling beat the verifier loops on Game of 24; on graph colouring sampling 40/44% vs verifier 34-38%.
8. c11 PDDL: 85.3/63.7/66.7 and 5.7 times tokens confirmed.
9. c09 MENSA: 22.4/25.9/54.5/70.3 and NetHack 12/10/50 confirmed; all random seeds set to 42 (single seed).
10. b01 Raab: N=92, M=2.2 options, 37.3%, F(3,992)=1.73, p=.159 confirmed.
Not re-checked: a15 (DTIC blocked; "26 FGCs, over 80%, under 12%" is search-summary only, do not cite as primary), b07, Mamede (b08), Johnson and Raab N=85.

## Contradictions between sources
- Klein 80% (FGC-1) vs 58% (FGC-2 experts) vs Gontar about 34% (pilots) vs Ambur 46-96%. Differences come from decision-point definition, coding, domain and training culture (pilots are drilled in an analytic procedure).
- Take-the-first: supported in handball and strong chess; not supported in weaker chess (b01); Moxley chess data (a21) shows the first move kept only 45% overall. Elite players also blunder far more under blitz (a22). The first option is good with expertise and pattern-type tasks only.
- Mental simulation: Klein presents it as the checking step. LLM data show self-simulation and self-critique is poor (b17, b21, b22, b23), while environment- or retrieval-grounded simulation helps (c07, c04 Mind's Eye). The analogue works when the simulator is external or sound.
- Search benefit vs sampling baseline: RAP/ToT gains are large against single-chain CoT, but CoT best-of-100 gets 49% and plain sampling beats verifier loops. Part of the gain is sample count.

## Weak spots
- No direct human experiment isolates the mental-simulation step (b29). The model is a description, with a falsifiability dispute (a09, a38: RPD can be read as non-deliberate comparison).
- Frequency studies are retrospective, coder-involved, with no outcome control and small decision-point counts.
- LLM results mix model scale, tuning and token budget; almost none are token-matched; some are single-seed (MENSA) or one benchmark (a26).
- Only one LLM paper uses RPD language directly (a26), and it is confounded.
- Computational RPD agents (a27, c19) report no hard accuracy numbers.

## Seen only in snippets
a15, a16, a28, b10, b11, b25-b28, c22 (abstract only), c26 (negative search result). No claim rests on these alone.

## GAPS
1. At equal tokens, does recognise-first (one candidate plus a short check) beat best-of-N sampling with a majority or sound-verifier pick on our own tasks, and on which item classes?
2. What cheap signal (retrieval similarity, agreement across 2-3 samples, token confidence) predicts when the first answer is safe, as a replacement for "years of experience"?
3. What rollout depth is best, and does it vary by task? MENSA found 3; the human limit is about 3 parts and 6 steps. Beyond which depth do rollouts lower accuracy for our model?
4. Which checks are sound for our task types (code execution, constraint checkers, unit tests), and how much of the gain comes from check quality rather than from simulation?
5. Does an RPD-style prompt beat a length-matched neutral prompt? (a26 lacks this control.)
6. Does a forced counter-cue step reduce the "falling in love with the simulation" failure at equal tokens?
7. Is prototype-level memory (typical situation, cues, expectancy, action) better than exemplar retrieval, given that commanders rarely used specific cases (a35)?
8. What are the real figures in Calderwood, Klein and Crandall (1988) and Klein et al. (1995) chess studies, the best human tests of first-option quality? Not retrieved.
9. Are there human experiments where a pre-mortem or prospective-hindsight step changed outcome quality (Mitchell et al. 1989; Klein's pre-mortem)? Next-pass target.
10. Does LLM next-state accuracy (about 55-60% on hard changes) set a ceiling on how far rollouts help, and does retrieval grounding (c07) close it on our tasks?

## Gap search results (evidence_d.jsonl, d01-d16; claims K25-K31 added, K20 now contested)

Search note: WebSearch quota ran out after four calls; the rest used arXiv PDFs (pdftotext), WebFetch and Europe PMC. Semantic Scholar and OpenAlex were rate-limited. Several arXiv listings were retried after 429 errors.

Closed or mostly closed
- Gap 2 (cheap gate): mostly closed for reasoning benchmarks. First-sample confidence (ReASC d01), cross-route agreement (CoT vs executed program, d03) and Bayesian stopping (CGES d02) all work, but need per-task calibration and fail on GPQA. Still untested on our own tasks. Added K25.
- Gap 4 (sound checks): mostly closed. Check quality drives the gain: 40 / 55 / 88% for none / LLM critic / sound verifier (d06); value function 24.5 / 37.0 / 43.5% (d05); survey (d07). Added K27.
- Gap 10 (world-model ceiling): mostly closed. Next-state accuracy is 77-86% but plan alignment only 50-65% without retrieval and 85-95% with it (d10, d11). The ceiling is long-horizon coherence. Probe samples are small. Added K31.

Partly answered
- Gap 1 (equal tokens): only indirect evidence. Compute should depend on difficulty; easy items favour one answer plus revision, hard items favour search (d04); compute-matched re-ranking lost to search in a web setting (d05). No token-matched test of one candidate plus short check against majority vote was found. Still needs our own experiment.
- Gap 3 (depth): evidence conflicts, so K20 is now contested. MENSA depth 3 best; web tree search helped to depth 5; reasoning models search about 1.8 plies and depth does not predict wins while breadth does (d08). Treat default cap 3 as a hypothesis; measure per task class.
- Gap 6 (counter-cue): a premortem-style prompt beat a plain instruction on safety at similar tokens, but a structure-matched forward control tied it under SFT (d12). No accuracy test. Added K28.
- Gap 7 (prototype vs exemplar): strategy-level memory beat trajectories (d15) but is confounded. Added K30.

Still open
- Gap 5 (RPD prompt vs length-matched neutral prompt): no new study found. K11 stands as single-source and confounded.
- Gap 8 (chess 1988 and 1995 figures): not retrieved (d16, opened:false). Do not cite numbers. Needs library access.
- Gap 9 (human premortem outcomes): the primary 1989 abstract says temporal perspective had little effect in experiment 1; the 30% figure is not in it; Klein's HBR page has no test (d13, d14). No human outcome study found. Added K29, and treat the 30% claim as unverified.

New knock-on caveat
- Value-of-computation gating has a human analogue (d09): in positions where deeper search does not change the move, time does not improve quality. This supports skipping rollouts when a cheap second look agrees with the first.
- K07 relies on a22, whose "18 of 20" detail was unverified earlier; the t and d figures were not re-checked in this pass.
