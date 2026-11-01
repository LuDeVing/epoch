# Critique: C08.06 Adaptation (cross-check)

## Numbers re-opened this session (arXiv PDFs, pdftotext)
- DS-Agent (2402.17453): rank 2.08 / 2.58 (w/o ReviseRank) / 3.41 (w/o CBR) CONFIRMED. One-pass 85% and 99% vs 56%/60% CONFIRMED; the figure shows 99.44 for GPT-4.
- Memento (2508.16153): K=0 59.9/72.2, K=1 63.6/77.9, K=4 64.5/78.5, K=32 63.9/78.1 CONFIRMED; GAIA 87.88 val and 79.40 test CONFIRMED. w/o CBR DeepResearcher 59.9/72.2 line matches the K=0 row.
- Huang et al. (2310.01798): GSM8K 75.9 -> 74.7 (round 2), CSQA 75.8 -> 41.8, HotpotQA 26.0 -> 25.0, oracle GSM8K 84.3 / CSQA 89.7, 74.7% unchanged CONFIRMED.
- Olausson et al. (2306.09896): 1.58x (33.3% -> 52.6% in the abstract), GPT-4 feedback inaccurate 32/80 vs human 7/80, uncertainty 0/80 vs 7/80 CONFIRMED. Note: the c22 "Table 1 cells 42.64 -> 62.21" are not the headline numbers; use 33.3 -> 52.6.
- NOT re-opened (APIs returned no hits for the arXiv search): Ye et al. 2021 table, TextBFGS, CBR-to-SQL, AWM, DomAgent, Hu et al., Lewis and Mitchell. These stay at the extractor's reading; two independent extractors (a, b, c overlap) agree on Ye, TextBFGS and CBR-to-SQL numbers, which is the only cross-check.

## Corrections and inconsistencies
- a18 says "GPT-4 about 99 percent"; b10 says "99-100%". Paper: 99.44 one-pass; 100% is the development-stage success. Use 99.
- a05 says "adaptation always lowered error in novel settings" and a06 says one cell got worse; both agree (the worse cell is the normal setting). a32 "better in 7 of 8" is consistent.
- c18 gives 50-70 as "14.85 to 12.02" (Siamese before/after), a05 lists L1+adapt 14.74 for the same group. Different retrievers, not a conflict, but the L1 before/after for 50-70 is unrecorded.
- c04 development cost ($0.06 / $1.60) vs a18 "cost fell 92.5 / 91.5 percent": consistent.
- b11 and c03 both say "performance falls rapidly as cases increase" for DS-Agent but only from a figure; direction only.
- a17/b30/c28 are the same conceptual review (no measurements); counts as one source, zero data.
- b25 vs c23: same paper, not independent; "independent_sources" counts papers.
- Yasunaga numbers differ between b27 (davinci-003) and c24 (GPT-3.5-turbo): different models; both consistent with "benefit depends on model strength", but davinci-003 and gpt-3.5 gains are small (+1 to +4).

## Contradictions between sources
- Adaptation helps (DS-Agent, CBR-to-SQL, TextBFGS) vs self-edit does not (Huang, Olausson). Resolution in the evidence: edits help when grounded in an external check or a retrieved example, hurt when blind.
- Retrieval: DS-Agent/Memento/fallacy-CBR say few cases; DomAgent says KG-selected 30% equals random 80% (a coverage claim, different variable).
- AWM: big relative gains on WebArena but tiny task-level gains on Mind2Web hard splits.
- TextBFGS: error-keyed retrieval wins cross-domain but loses slightly in-domain.

## Weak spots
- Almost all LLM evidence is from 2024-2026 preprints, single labs, no replications. TextBFGS and CBR-to-SQL are 2026 and unreplicated.
- Few ablations isolate the edit step. In DS-Agent the ReviseRank gain (0.5 rank) is small, 5 trials.
- Confounds: TextBFGS compares to TextGrad, not to plain resampling at equal tokens. Memento adds a planner and tools.
- Classical CBR numbers (CHEF, Hanney-Keane, DIAL, Smyth-Keane) are second-hand or demonstration only.
- Ye et al. is one regression task (face age); regressor won in normal setting.

## Only seen in snippets or second-hand
a07, a10, a11, a12, a13, a14, a15, a16, a28, a29, b07, b08, b09, c21, c29, c30 (opened:false). Search APIs were rate-limited during the extraction run.

## GAPS
1. At equal tokens, does editing one retrieved case beat best-of-N fresh samples on a reasoning (not code) task? No source tests this.
2. Which cases to retrieve for editing: similarity vs adaptation-guided (editability) retrieval, with LLMs? Smyth-Keane and Leake-Ye numbers were never read.
3. Does an external verifier (tests, tools) fully explain the edit gain, or does a retrieved example add value beyond the verifier? (Huang/Olausson vs DS-Agent confound.)
4. What is the best unit of memory for edits: whole solution, abstract workflow, or error-to-operator rule? TextBFGS vs AWM vs DS-Agent never compared directly.
5. Where is the break-even distance between query and memory where editing beats direct solving (Ye et al.: regressor wins when familiar)? Is this true for LLMs?
6. Do edit gains survive on strong frontier models (2025-26), or do they shrink as base accuracy rises (GPT-4 already 95.5 on GSM8K)?
7. Failure modes of LLM edits: how often does editing break a correct retrieved solution (negative transfer, copy errors)? No measured rate for retrieved-case editing.
8. Do Wilkerson and Leake 2024 and Leake-Ye 2021 report measured LLM adaptation or alternating-training results that change K05?
9. Does failure-indexed memory (CHEF-style anticipation) help LLM agents measurably?
10. Cost: does diagnosis-before-edit (separate feedback model) pay for its tokens at equal budget?

## Gap search results
Evidence is in `evidence_d.jsonl` (d01 to d22). 13 arXiv papers were opened. WebSearch was exhausted and the scholar APIs returned HTTP 429, so papers were found by known arXiv ID and Crossref. New claims K20 to K26 were added; K09 was raised to established.

Closed or mostly closed
- Gap 3 (verifier vs example): mostly closed for self-edit. CRITIC and the Kamoi survey (d05, d08) show tools and tests carry the gain. Whether a retrieved example adds value beyond the verifier is still untested.
- Gap 7 (breaking correct answers): partly closed. Measured rates exist for blind edits: 38% (Snell), 15.8% base and 4.2% Self-Refine (SCoRe), 58.8% (Llama-3.1-8B doubt prompt) (K21). Raw retrieved cases also pushed GPT-4o below baseline (K22). The rate for retrieved-case editing is still unmeasured.
- Gap 10 (diagnosis): partly closed. Specific feedback beats generic (d03, d07, K25). No equal-token test.
- Gap 4 (memory unit): partly closed. Distilled items beat raw examples on DC, ReasoningBank, BoT; ExpeL splits by task (K23, contested). TextBFGS, AWM and DS-Agent still not compared directly.
- Gap 6 (strong models): partly. Self-Refine math gain is ~0 at 93% base; CBR-DDI gain holds to 671B; GPT-4o gains vanish on GPQA (K24, contested). No 2026 frontier model tested.
- Gap 5 (familiar queries): partly. CBR-DDI authors say fine-tuned models win on seen drugs (S0), matching Ye et al. No clean LLM break-even curve.

Still open
- Gap 1: edit one retrieved case vs best-of-N at equal tokens on a reasoning task. Only code (Self-Debugging) and a trained reviser on MATH (Snell) exist; neither edits a retrieved case (K20).
- Gap 2: adaptation-guided retrieval. Smyth-Keane 1998 and the 1995 paper are paywalled (HTTP 403). No LLM study found.
- Gap 8: Wilkerson-Leake 2024 and Leake-Ye 2021 are closed access; not read. K05 unchanged.
- Gap 9: CHEF-style anticipation not tested. Nearest is ReasoningBank failure lessons (K26, post-hoc, +3.2 points).

Caveats: several table cells were read from scrambled PDF text (CRITIC, Self-Debugging MBPP, ExpeL Table 3, CBR-DDI columns); directions are safe, exact cell mapping is flagged in the `limits` fields. Most new sources are 2023 to 2025 and use older models.
