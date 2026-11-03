# Critique: Fluid reasoning (Gf), cross-check

## Re-opened sources (arXiv text, 2026-11-03) and results
- ARC-AGI-2 paper (2505.11831): 407 participants, 515 sessions, 1,848 test pairs, 13,405 attempts, 8,277 solved (62%), median 2.3 min: CONFIRMED. Table values o3-medium 53.0 vs 3.0, o3-mini-high 34.5 vs 3.0, ARChitects 56.0 vs 2.5, Icecuber 17.0 vs 1.6: CONFIRMED. Two testers 97% and 98%, high-end humans over 97%: CONFIRMED.
- H-ARC (2409.01374): 1,729 people, 76.2% [73.3, 77.2] training, 64.2% [55.9, 68.9] evaluation, 790 of 800: CONFIRMED.
- Camposampiero 2025 (2503.11207): 86.6% to 17.0% (o3-mini), 80.6% to 23.2% (R1), neuro-symbolic 98.6% to 88.0%, chance 12.5%: CONFIRMED. The text also gives R1 as 22.8% in one condition.
- Akyurek 2025 (2411.07279): 17.5 to 45.0 pass@2 on 80 tasks, 53.0, 61.9, BBH 50.5 to 57.8: CONFIRMED.
- ConceptARC (2305.07141): Center 0.97 vs 0.20, Count 0.86 vs 0.03, Copy 0.93 vs 0.07, Inside/Outside 0.83 vs 0.27: CONFIRMED. Three guesses and 30 test inputs per concept: CONFIRMED.
- Lewis and Mitchell (2402.08955): 1,876 human and 6,840 per-model samples, humans 0.753 [0.734, 0.773]: CONFIRMED. The PDF text layout scrambles the row labels, so the GPT-3 0.488 / GPT-3.5 0.350 / GPT-4 0.452 assignment was not independently certain.

## Corrections
1. b09 said "482 human participants, 12 excluded". The paper says 55 of 482 were excluded for inadequate explanations plus 12 more for failing minimal tasks: 67 excluded, 415 kept. Fix b09.
2. ARChitects scores 53.5% (ARC Prize 2024 private set) and 56.0% (ARC-AGI-1 semi-private, in the ARC-AGI-2 paper). Different sets; not one number.
3. a11 and b09 quote GPT-4 25% overall for ConceptARC. The per-concept table (0.03 to 0.33) was confirmed; the 25% overall was not found in the table text. Treat it as from the paper's prose.
4. Camposampiero token multiplier is 3.4x (c13) or 2.7x (c22) depending on the condition. Different settings, not a contradiction.

## Contradictions between sources
- Webb 2023: GPT-3 matches or beats humans on digit matrices. Hodel and West, and Lewis and Mitchell: GPT-3 falls below 0.1 on several letter-string tasks with changed alphabets. Webb 2024: GPT-4 with code matches humans. Net: contested (K05).
- Gendron: text form beats symbolic form for Raven. Xu: object form beats raw grid for ARC. The direction of the representation effect depends on the task.
- ARC-AGI-1 looked nearly solved by o3 preview (76 to 88%) while the same families score about 3% on ARC-AGI-2. ARC-AGI-1 was partly searchable or learnable at high cost.

## Weak spots
- Several results are single paper (hypothesis search, reasoning-model Raven collapse, eye movements, g in LLMs).
- Human comparison samples are crowd workers (MTurk, Prolific) with exclusion rules; human numbers depend on the filtering.
- No source tests novelty sorting as a gate. The S0 claims are inferred, not measured.
- Most papers compare methods at unequal token cost.

## Seen only in snippets or secondhand
- Cattell 1943, Horn and Cattell 1967, Carpenter-Just-Shell 1990, Kyllonen and Christal 1990, Chuderski and Necka 2012 (a01, a07, a25, a26, c24, c25) were not read. Ritchie and Tucker-Drob (b24) was not opened. Jaeggi 2008 and Melby-Lervag 2016 numbers were not re-opened in this pass.
- Wikipedia lines (a02 to a04) are encyclopedia summaries, including the peak age of about 27.

## GAPS
1. Does a "novel vs familiar" sort at S0 predict where scaffolding helps? No paper measures this at equal tokens.
2. Do longer reasoning chains help or hurt on novel items (o3-mini fell as tokens rose)? Need a token-matched curve by novelty level.
3. How much of LLM ARC performance is memorisation of public ARC-AGI-1 tasks versus skill? Need counterfactual or fresh-task comparison.
4. Which representation step (object extraction, text vs symbolic) is robust across models and tasks?
5. Does hypothesis-then-program verification replicate beyond one 100-problem GPT-4 subset, on current reasoning models?
6. What do prompt-only scaffolds (no fine-tuning) score on ARC-AGI-2 at fixed cost per task in 2025-2026?
7. What do Cattell 1943 and Horn and Cattell 1967 report (sample sizes, Gf loadings)? Not read.
8. Do LLM Gf scores track working-memory-like limits (items held, context length), as in humans?
9. Do human Raven or matrix norms (reliability, g loading) transfer when LLMs are scored, given contamination?

## Gap search results (2026-11-03)
Evidence in evidence_d.jsonl (d01 to d16). Search tools were rate limited (arXiv, OpenAlex 429; WebSearch budget ran out), so papers were found by a few searches and by direct arXiv PDF fetch.

1. Novelty sort at S0: STAYED OPEN, with a warning. No paper tests a novelty gate at equal tokens. Li et al. 2024 (d05, d16) show human difficulty is anti-aligned with model difficulty at both ends (models beat humans on the hardest 20% of ARC tasks, trail them on the easiest 20%). A human-style novelty rating is a weak gate; use pilot-attempt signals. New claim K19 (single source).
2. Reasoning length vs novelty: PARTLY CLOSED. Gema 2025 (d03, d12) and NeuroCognition 2026 (d04) show longer reasoning lowers accuracy on constraint puzzles, distractor tasks and 8-option text matrices (turning reasoning off helps, p=.021), and model-chosen length is worse than a forced cap. No curve indexed by novelty level exists. New claim K18 (established).
3. Memorisation of ARC: STAYED OPEN. ARC Prize 2025 report (d01) asserts knowledge-dependent overfitting but gives no size. Xie 2025 (d09) gives a perturbation method on Knights and Knaves, not ARC. New claim K20 (contested).
4. Robust representation step: CLOSED NEGATIVELY. Pixel canvas wins for vision models (VARC 54.5% ARC-1, d07); objects help GPT-4 (earlier c09); text beats symbols for Raven (earlier). No single step is robust across model types. Note on K03.
5. Hypothesis-then-verify beyond one subset: MOSTLY CLOSED. SOAR (d06) and Li et al. (d05) replicate program induction with execution check on ARC with current open models and some frontier models (GPT-4.1 8%, Claude-4-Sonnet 20.75%, o3-mini 38.25% one-shot). Not a replication of the exact 100-problem GPT-4 hypothesis-search setup, and those systems fine-tune. New claim K21 (established).
6. Prompt-only scaffold cost on ARC-AGI-2: PARTLY CLOSED. Poetiq harness on Gemini 3 Pro 31% at $0.81 to 54% at $31 per task (d01, d02), verified by ARC Prize. Claude Opus 4.5 about $60 per task. Only vendor-reported; no open equal-cost comparison. K10 updated.
7. Cattell 1943 and Horn and Cattell 1967: STAYED OPEN. Publisher text not retrievable; only the citation was confirmed (d15). K15 remains single-source.
8. Working-memory-like limits in LLMs: PARTLY CLOSED. Evidence says the limits are state use and consistency, not human-like item counts (d10, d11); n-back reading disputed (d13, snippet); a backward-digit-span and Raven correlation paper is a lead not opened (d14). New claim K22 (single-source).
9. Transfer of human norms: PARTLY CLOSED. NeuroCognition (d04) shows human image norm 0.814 vs human text pilot 0.43 (N=9), and format swings. Reliability and g loading of LLM Raven scores remain unmeasured. New claim K23 (single-source).

Unverified corrections: none of the earlier corrections were revisited. Open leads for a later pass: eScholarship backward-digit-span paper, Hu and Lewis n-back critique, a full-text copy of Horn and Cattell 1967.
