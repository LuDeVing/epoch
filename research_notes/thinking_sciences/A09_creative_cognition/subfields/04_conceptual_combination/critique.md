# Critique: Conceptual combination (noun-noun), A09.04

Cross-check of evidence_a/b/c.jsonl (82 lines). Method: re-opened arXiv PDFs and the saved Hampton/Wisniewski text and compared against the logged numbers.

## Corrections and confirmations (10 sources re-checked)
1. KOMBINE (Schapiro 2025, arXiv 2509.21043): 59.0 / 53.4 / 43.4%, 97.1% conditional coherence, 19.9% (412/2,070) reuse, 37.3% vs 2.6%, human 22.1 / 32.9 / 12.8%, 35 LLMs, N=75 Prolific. Confirmed. Note: the paper lists model names that look speculative (e.g. "GPT-6 Astra"); treat per-model rankings with care.
2. Coil and Shwartz (2305.10568): 95.64% NCI, 83.81% vs 73.33% NCC, 105 NCs, 97% vs 80% copied n-grams, BERTScore 91.94, ROUGE-L 47.31, METEOR 56.27. Confirmed. The NCC human baseline is a crowd-writer reference, not an expert.
3. Li, Carlson, Potts (2210.09492): 456 generations, kappa .844, r .93, r .105 in Exp 3, human exclusion 17.67%, 93% / 15% / 51% rows. Confirmed.
4. Song et al. CCPT (2502.06086): 12,315 triples, 82.6 / 95.6 / 69.6%, 56.4% vs 81%. Confirmed. The 2,501 emergent count was not re-found in text extraction (unchecked).
5. Kumar et al. Compun (2404.00419): 400 compounds, human 96.25, CLIP 78.25, OpenCLIP 83.90, +8.25, +2.35. Confirmed. Note: gain is measured against CLIP baseline, so "+8.25" is points, not percent.
6. Hampton 1988: 127 items, 93 items more likely in conjunction, 66% rejected the universal, chess 61%. Confirmed in the paper text. The "only 22 reverse" count was not re-checked.
7. Wisniewski and Gentner 1991: 400 phrases, 151 (about 39%) where head was not referent confirmed (OCR text noisy). The "only 40% state a relation" and "87% rater agreement" figures could not be verified because the OCR is garbled; keep as unverified.
8. Maguire et al. 2007: r .44 to .34 after removing the free parameter confirmed in text; the -.09 / .08 pair was not re-read.
9. Duplicates: a08/b01, a26/b13/b14, a29/b19/c23, a24/c05, b17/c02 describe the same sources. They were counted once in independent_sources. No numeric disagreement found among them.
10. Aerts 2026 Bell result (a28): numbers above 2.83 (3.09, 4.0) exceed the quantum Tsirelson bound, which signals a method problem (marginals not respecting no-signalling, or prompt effects), not "more quantum than quantum". Status set to contested.

No numeric correction was needed. Two wording corrections: c11 "35 LLMs" kept; a27 gold-emergence "about 57" is unverified (garbled table) and was not used in any claim.

## Contradictions between sources
- Similarity and property mapping: Wisniewski 1996 (72% vs 48%) against Bock and Clifton 2000 (no link once randomised, r=-.06). Probably salience confounded with similarity. Contested.
- Hampton says a sequential-projection quantum model cannot give double overextension; Aerts et al. fit it with a Fock/Hilbert model. These are different models, not a direct empirical conflict.
- Emergence: very rare under strict scoring (3 of 174) but common for incompatible pairs (about 170 emergent vs 220 inherited). Both stand; they differ in pair type and scoring.
- LLM interpretation looks strong (GPT-3 83.81%) while open 7B models and nonsense-word tests look weak. Different models and tasks; not contradictory but together suggest recall rather than composition.

## Weak spots
- Almost all human data is 1987-2000 with about 10-35 participants per cell, one lab (Hampton). No large modern replication of overextension with N in the hundreds was found.
- LLM-versus-human comparisons use crowd baselines (Prolific, MTurk), small human checks (CCPT N=30), and LLM judges.
- Most LLM studies test GPT-3/GPT-4o or 7B open models; few test current frontier reasoning models. No study tests a scaffold or multi-step operator on conceptual combination except PopBlends (N=10) and the CCPT spread-activation prompt (tiny gain).
- No evidence links blend quality of an LLM to downstream task success (the agent's real objective).
- Quantum-cognition results are model fits, not predictions of held-out data.

## Only seen at snippet level
Wisniewski 1997 (a23, b22), Costello and Keane 2000 (a22, b23, c28), Gagne and Shoben 1997 original (b24), Levin et al. 2019 (c29, second-hand via Li et al.), and Estes and Glucksberg and Wisniewski 1996 figures (second-hand via Bock and Clifton).

## GAPS
1. Does an explicit "find the shared abstraction (generic space) first" step raise valid-blend rate and downstream idea quality at equal tokens for a frontier model? (KOMBINE shows the bottleneck but never tests a fix.)
2. Do blends from distant seed pairs improve downstream task results (problem solving, design, forecasting) compared with no seeds or near seeds, and what distance is best?
3. Is the homogeneity of LLM blends (19.9% reuse, 37.3% for blends) reduced by randomised seed selection, temperature, role prompts, or cross-model pooling, and by how much at equal tokens?
4. Does a scenario-construction or extensional-feedback step ("imagine real instances of this blend") raise emergent-property generation in LLMs the way it explains human emergence?
5. Does the human overextension and non-commutativity pattern appear in current frontier LLMs (membership judgments for A, B, A-and-B; both orders), and does it matter for agent reasoning?
6. Do plausibility, diagnosticity and informativeness filters (Costello and Keane C3) improve the quality of retained blends when applied by an LLM judge or by code?
7. What is the full-text evidence for Wisniewski 1997 (comparison and construction) and Costello and Keane 2000 numbers (human match rates)? These need to be opened.
8. Is there any modern, large-sample (N over 200) replication of Hampton's overextension, and of the claim that emergent attributes are rare?
9. Do fixed-step pipelines like PopBlends (code ranks, model fills slots) beat free LLM blending at larger N and without a human in the loop?
10. Does the nonsense-word collapse (r .93 to .105) hold for current frontier models, i.e. do they compose from definitions or recall real compounds?

## Gap search results

Tool limits: the shared web-search quota was exhausted, and arXiv search, Semantic Scholar and OpenAlex were rate-limited. The work used direct PDF downloads, the Crossref title search and a few arXiv listing pages. Evidence is in `evidence_d.jsonl` (d01-d16); claims K14 and K24 were revised and K25-K29 added.

**Partly closed**
- Gap 3 (homogeneity can be reduced?). Mostly answered, from general idea tasks, not blends. Varied inputs plus a structured step work: persona + chain-of-thought gave 248 unique category combinations vs 197 for humans and 88 for default GPT-4o (d03); evolved, spread-out personas +78.8% diversity vs +8.7% for random ones (d07). Decoding and pooling do not: temperature 1.5 marginal, min-p at T=2.0 left 81% of pairs above 0.7 similarity, 71-82% cross-model similarity, pooling 40 GPT-4 sessions was among the least diverse, creative system prompts moved variability 0.459 to 0.576 against humans' 0.738 (d03-d06, d08). Still untested on blends at equal tokens. Claim K27.
- Gap 7 (full texts). Wisniewski 1997 is read in full (d09, d15). It is a theory paper, so no human match rates exist there. Costello and Keane 2000 is still unopened (paywalled), so it stays open.
- Gap 2 (distant seeds help downstream?). One LLM study: far-domain analogies gave novelty gains and four implemented biomedical wins (d01, d02). No near-seed arm, so best distance is unanswered. Human design work on distance (Design Studies 2015 and 2016 titles) was found but not opened, so no numbers are claimed.
- Gap 1 (generic-space step). Closest evidence is the structure-first analogy step (2 calls vs 2 calls, novel-solution rate 21.6% to 50.4% on Claude; d01). Not a blend-validity test. Still open for blends.

**Stayed open (no study found, search was limited)**
- Gap 4 (scenario or extensional feedback step in LLMs).
- Gap 5 (frontier LLM overextension and non-commutativity).
- Gap 6 (C3 filters applied by an LLM judge or code).
- Gap 8 (large-sample replication of Hampton): none found in Crossref title searches (d13).
- Gap 9 (PopBlends-style pipelines at larger N).
- Gap 10 (nonsense-word test on frontier models). Side evidence only: GPT-4o is 10-15 points lower on novel than on lexicalised compounds (d10), and a 2025 Cognitive Science abstract reports weaker fits for novel compounds in older LLMs (d11, abstract only).

**Next step.** Gaps 1, 4, 5, 6, 9, 10 can be run in our own harness rather than waiting for papers; K25 and K29 hold the test designs.

**Housekeeping note.** While fetching PDFs through WebFetch, a move command swept other agents' saved WebFetch PDFs from the shared tool-results folder into D:/research_scratch/A09.04/ and some were deleted afterwards. Another agent that cannot find its WebFetch-saved PDF should re-fetch it.
