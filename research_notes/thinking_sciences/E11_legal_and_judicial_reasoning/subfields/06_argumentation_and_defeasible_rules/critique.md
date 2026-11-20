# E11.06 Argumentation and defeasible rules: cross-check critique

## Numbers re-opened (full text read this session)
1. Kirkpatrick and Sterken (arXiv 2508.13718): CoT mean drop -11.14% (SD 15.74), Claude 3 Opus 96.51, Claude 3.5 Sonnet 96.01, Claude 3 Sonnet CoT -16.28, GPT-4 0613 CoT -12.62, Gemini Flash CoT -18.77, Opus few-shot -6.81: CONFIRMED.
   CORRECTION: GPT-4 (0613) zero-shot is 93.52 in the table, not 96% (a18 and b07 say 96%; c10 has the right 93.52). Use 93.52. GPT-4 Turbo 2024-04-09 is 92.69, not 93%.
2. Steging et al. (arXiv 2505.01539): linear-graph accuracies 54.38, 72.31, 64.64, 60.32, 58.84, 77.32 and non-linear 8.85% yes-rate, 86.81, 38.15 recall: numbers present. The pdf table layout is scrambled, so the model-to-number assignment (Claude 3.5 Sonnet 77.32 etc.) rests on the earlier agent's reading and on row order, not a clean re-read. Treat per-model labels as probable.
3. Li et al. (arXiv 2412.16725): grounded-extension accuracy Llama3-8B 0.18, Llama3-70B 0.37, Qwen2.5-7B 0.31, Qwen2.5-72B 0.48, GPT-3.5 0.15, GPT-4o 0.54, SFT 0.97 and 0.95; Llama3-8B 0.51/0.42/0.45/0.48 baseline; "sometimes falling to 30%": CONFIRMED.
4. Kazemi et al. BoardgameQA (2306.07934): 1000/500/1000 split, majority baseline 33%, prompt-tuned model predicts unknown 268 times at depth 1 versus 2 at depth 2: CONFIRMED.
5. Bezou Vrakatseli et al. (2021): M=5.61 vs 5.21, t(102)=4.636; Welch t=-0.683 p=.496; F=12.906, 53.66, 1.227 with df (1,211): CONFIRMED. The 130 aimed / 103 analysed split is only partly visible ("130 participants took" each experiment).
6. Simpson et al. (arXiv 2607.23386): 61/68 (89.7%, CI 80.2-94.9), 44/68 (64.7%, CI 52.8-75.0), 98.5% in April, GPT-5.4 7/11 withdrawn to 11/11, 53.9% few-shot vs 92.9% zero-shot (83/154, 143/154), engine 150/154: CONFIRMED. NOTE: the paper itself says the 0/70 rerun "stands as a March finding" after later drift, so it is a dated result.
Not re-opened (taken from earlier agents): Cramer and Guillaume (2018) chi2 values and 100%/97.5% figures, Allaway and McKeown 0.64 F1, Batzoglou ABD numbers, DeFAb counts, Mishra 27% drop, CQoT +4.61%, Horner F1 recompute. Not triangulated beyond the original agents' reading.

## Contradictions and inconsistencies
- GPT-4 0613 zero-shot: 96% (a18, b07) vs 93.52 (c10, paper table). Table wins.
- a21 says Qwen2.5-SFT 0.97 / Llama3-SFT 0.95 on grounded; a22 gives 1.00 and 0.95 for preferred. Different semantics, not a conflict.
- Tachmazidis et al. (a17, c12) and the 2024 benchmark entry (b15) say "errors in 7 of 32 cells" vs a17's per-theory list (4+2+1=7). Consistent.
- Human-semantics studies disagree: Cramer finds CF2/preferred fits near 100% for some items yet 56% / 32% unexplained on others; Bezou finds only a weak reinstatement effect. The field has no stable descriptive winner.
- Toulmin/BoardgameQA: strong models do very well on single exceptions (96%) yet collapse on chains or large graphs. Not contradictory: depth and size are the boundary condition.

## Weak spots
- Most LLM-evidence is single-source per claim; only a few claims reach 2 independent teams (Kirkpatrick appears in three evidence lines but is one source).
- Many model names (Claude 3, GPT-4 era) are old; 2026 models appear only in vendor-style or single-lab papers (Simpson/Aethis has a commercial interest; DeFAb and ABD are single-author-group preprints).
- Few studies compare scaffold versus plain at equal tokens. CQoT uses a GPT-4o judge; ArgLLM gains are a few points.
- The Simpson drift finding (same alias, different accuracy a month later) means any 2026 model number here is time-stamped and may not reproduce.
- No human-expert baseline for exception-chain items; no legal-practitioner study of LLM burden-of-proof handling was found.

## Seen only in snippets / not opened
a26 Ford (2005), a27 Ford and Billington (2000), a28 Hahn and Oaksford (2007), b26 Rahwan et al. (2010; N=20 known only through Bezou), b27-b30, c28 LLM-ASPIC+ (87.1% / 82.6% on BoardGameQA, snippet only; do not cite), c29 Park et al.

## GAPS (most decision-relevant first)
1. Does an explicit exception/undercutter slot (Toulmin rebuttal) raise accuracy on exception-chain items at equal tokens compared with plain CoT, given that CoT alone hurts default reasoning (-11%)?
2. Is the CoT penalty on default reasoning (Kirkpatrick) reproduced by an independent team and on 2026 models, and does a short direct-answer-plus-exception-check route avoid it?
3. Does an external labelling table (in/out/undecided per argument) fix the large-graph collapse (1-25 arguments, non-linear, recall 38%) without fine-tuning?
4. How much does moving the burden of proof or proof standard change LLM verdicts on identical evidence, and do models track it (no direct LLM test found)?
5. Do LLMs propose minimal exceptions on held-out cases (ABD, DeFAb: 1-1.5 extra exceptions, over-broad exceptions) and can a held-out check step cut that?
6. How stable are 2026 model results on exception chains (Simpson silent drift): what repeat count is needed before trusting a scaffold gain?
7. Does false-positive inflation from "check exceptions" prompts (20 new FPs) generalise outside one vendor benchmark?
8. Which human reasoning data (Cramer, Bezou, Rahwan) should the schema follow when LLM and human semantics disagree, and is "void precedence" enough?
9. Do critical-question scaffolds (CQoT) keep their gains with a non-LLM judge and at equal token budget?

## Gap search results (gap searcher, 2026-11-19)
Search tools were limited: arXiv, Semantic Scholar and OpenAlex APIs returned rate-limit errors, so work used WebSearch (7 calls) and page fetches. Evidence is in evidence_d.jsonl (d01-d18).

1. Toulmin exception slot vs plain CoT at equal tokens: PARTLY CLOSED. NormBench (d13) and LogT (d05, d06) show explicit exception structure helps exception-active items, mostly on weaker models, and can be neutral elsewhere. No equal-token comparison exists; LogT uses about 21.5% more steps.
2. CoT penalty replication: STAYS OPEN. No same-task replication found. DERELAB (d01, d02) shows extended thinking helps on belief updating (Qwen3-32B gap 0.670 to 0.008), so the penalty is task-specific. A direct-answer-plus-exception-check route was not tested.
3. External labelling table for large graphs: PARTLY INFORMED. The n 26-35 ablation (d09) shows intermediate steps lift accuracy 0.68 to 0.85 (grounded, Qwen2.5), but this is fine-tuning. No prompt-only or solver-call test found.
4. Burden/standard of proof shifts: STAYS OPEN. No direct LLM test. Closest are the mock-juror study (d12: 21% vs 49% guilty verdicts) and a conceptual paper (d11).
5. Minimal exceptions and held-out check: STAYS OPEN. DeFAb current page (d14) reports no minimality score; only a symbolic verifier caught over-broad exceptions (34 of 34 circular). The "65% on L2" figure cited earlier is not on the current page.
6. Stability of 2026 results: PARTLY CLOSED. DERELAB seed variance is small (ICC 0.95, CV under 4%), but Simpson reports drift on the same alias (d16). A search summary said Simpson's headline was withdrawn in v3.8; the arXiv page lists only v1 with no withdrawal, so this is unverified and conflicting. Use 20 seeds and date-stamp results.
7. False-positive inflation outside one vendor: STAYS OPEN. LogT trace analysis shows false negatives fall 41% to 28% (d06), but no false-positive data. "Blind Refusal" (75.4%) seen only as snippet (d17).
8. Human vs LLM semantics: STAYS OPEN. No new human data found. Keep "void precedence" as the minimal rule.
9. CQoT with non-LLM judge at equal tokens: STAYS OPEN, with a negative update. CQoT used a GPT-4o judge only, no human validation, no token counts, and its text percentages do not match its own table (d07). Nemotron CoT beat CQoT on reasoning.

New claims: K20-K23. Changed: K06, K09, K11, K14, K16 were annotated with boundaries; no status changed to established.
