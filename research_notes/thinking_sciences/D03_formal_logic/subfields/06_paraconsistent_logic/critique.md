# Critique: Paraconsistent logic (D03.06)

Cross-checker pass. I re-opened 9 sources as full PDF text (pdftotext) and checked 10 key number groups against the evidence lines. Claims are in claims.jsonl (K01-K25).

## Numbers re-checked

1. Allen et al. 2025 (arXiv 2507.09751), Table 1 and 2. CONFIRMED: GPQA flagship F1 0.699 vs 0.633, coverage 0.589; SimpleQA flagship 0.736 vs 0.657, coverage 0.584. Tokens 4,781.7 vs 2,212.8 (GPQA flagship), 3,964 vs 2,167 (SimpleQA distilled). I recomputed the mean F1 gain across the four cells as about 0.062 and the mean coverage loss as about 0.456, which matches b25.
2. Allen Table 3 glut/gap shares (0.301/0.211/0.378/0.110). CONFIRMED.
3. Bao et al. (2512.06393): GPT-4o 0.789 base, 56.0% halt on V3; Gemma 0.580 and 43.9%; V2 0.2950/0.2500; V4 0.645 and 0.9925. CONFIRMED.
4. ContraDoc (2311.09182): 449 docs, GPT-4 binary 53.8%, recall 8.0%, precision 97%; evidence hit 70.2% (GPT-3.5 42.8%); wiki 82.0%, story 62.4%; human 74.1%/26.7%, GPT-4 86.7%/34.7%. CONFIRMED. Note: 82.0% and 62.4% are evidence-hit rates by genre, not judgment accuracy.
5. WikiContradict (2406.13805): no-cue (template 4) correct 2.1/4.2/4.2/10.4/6.3 and cue (template 5) 20.8/14.6/22.9/43.8/10.4. CONFIRMED. Llama-3-70b explicit 13.3% to 60.0%, implicit 5.9% to 17.6%. CONFIRMED. The headline "cue" is prompt template 5, "no cue" is template 4; template 1 tests internal knowledge only.
6. PCBench (2505.23715): proactive 11.0% (GPT-4o), 40.5% (DeepSeek-V3), 4.0% (o4-mini); assisted 73.2/77.9/74.2. CONFIRMED. The 53.5% (Llama-4-Maverick) lower bound was not rechecked.
7. Rulebreakers (2410.16502): chance 0.25, only Llama-3-8B above 0.6, GPT-4o 0.0022 on MT categorical entity, +24.13 for the best prompt. CONFIRMED.
8. Cross-query contradiction paper (2604.14525): SetCons 0.56 to 0.94 (R1, No-CoT to SC K=20); deep-subset ablation no solver 0.52 SetCons, check-only 0.84, repair without core 0.88, core-guided 0.91; overhead 1.51x. CONFIRMED. Correction of emphasis: the 0.56 to 0.94 headline is a no-CoT to self-consistency jump, not a solver effect. The solver-based method alone reaches 0.88-0.91 on the deep subset.
9. Alxatib and Pelletier 2011: N=76; 44.7% (34 of 76) "tall and not tall" true; 53.9% neither true (41 of 76); 'tall' true 1.3% to 46.1% to 98.7%. CONFIRMED.
10. Egre et al. / Serchuk table: 66/195/89 and 25/247/78, 113/137/100, 141/88/121 (N=350), and N=148 regression (and -4.35, control False -10.52). CONFIRMED. CORRECTION: the 350-response table is "Serchuk et al.'s data" reported inside the Egre chapter (it is labelled Table 2 there), not Egre's own experiment. Egre's own experiment is the N=148 MTurk study. Claim K06 attributes it correctly.

Corrections made: (a) item 10 attribution above; (b) item 8 emphasis. No numeric value was wrong.

## Contradictions between sources

- Human data on gluts: A and P (44.7% accept "tall and not tall") vs Serchuk (19% and 7%) vs Egre (about 35-66% depending on order and adjective). The range is a method effect, not a stable rate. The headline 44.7% is a high outlier.
- Allen et al. say bilateral judging helps, but coverage falls by about 0.46. Whether a unilateral judge allowed to abstain at the same coverage would match 0.699 is not tested. Cross-query paper shows plain self-consistency matches a solver pipeline. Both point the same way: gains may come from abstention or sampling, not from the paraconsistent structure.
- Bao et al. count "halt" as correct on contradiction; a paraconsistent view says the agent should keep working with the consistent part. The Bao benchmark therefore cannot be read as a test of paraconsistent reasoning. Rulebreakers shows the opposite danger: more logic checking can lower accuracy.
- PCBench/Fan et al. show reasoning models notice the flaw in their trace but do not report it; WikiContradict shows weaker non-reasoning models do not notice. The two failure modes need different fixes.

## Weak spots

- Almost all LLM evidence concerns detecting or reporting contradictions. None tests whether an agent that keeps a contradictory set reasons better than one that repairs or halts.
- Most items are single-source (see claims.jsonl: only 7 established, and those mostly through related benchmarks, not identical designs).
- Allen et al. negatives were partly synthetic (GPT-4o Mini generated); models used are 2024-era.
- Judge models (o3-mini-high, Gemini 2.5 Flash, GPT-4) grade several benchmarks, so measured rates inherit judge error (WikiContradict judge over-rates Mistral-7b, 39.6% vs 20.8% human).
- Small N for human WikiContradict eval (48 instances, 5 models).
- Priest 1979, Belnap 1977, da Costa 1974 were not opened as originals; formal claims rest on the SEP and Jakl 2025.

## Seen only in snippets (opened:false)

a08, a09, a13, a29, a30, c19-c27 (including Logic-LM, 4QL, Arieli and Avron, AGM-Bench, ReviseQA, LogicVault 78% figure). Do not cite their numbers.
Search note: arXiv, OpenAlex and Semantic Scholar returned 429 errors during the search phase, so the "zero hits" claim (K25) is weaker than it looks and should be redone.

## GAPS

1. At equal tokens, does keeping a contradictory set with flagged (for, against) records beat repair-by-retraction and beat halting, on tasks with injected contradictions? (No study; the core decision for S6.)
2. Does bilateral verify-and-refute judging beat a unilateral judge when both are matched on coverage (abstention rate) and on total tokens or on self-consistency votes?
3. Which conflict type matters most for an agent: explicit contradiction between sources, implicit (needs reasoning), or self-contradiction in its own trace? Detection rates differ 5x between explicit and implicit.
4. Why do reasoning models notice a conflict in their trace and then not report it (PCBench, Fan et al.)? Would a forced "conflict line" at S6 raise reporting without raising token cost?
5. Can a da Costa style "mark as consistent" (verified) flag be implemented in the scaffold, and does restricting classical inference to marked facts reduce spread of errors versus unrestricted reasoning?
6. Do adaptive-logic style retractions (drop only derived lines depending on the conflicting premises) beat full re-solve on edited premise sets (DeltaLogic-like tests, belief inertia 0.60)?
7. Is there any 2020-2026 LLM paper on LP, FDE, LFI, or Belnap four-valued scaffolds that our rate-limited search missed? Re-run arXiv, OpenAlex and Semantic Scholar queries.
8. Do the order and adjective effects in human glut acceptance have any analogue in LLMs (premise order effects of 20-30%; are LLM conflict judgments order-sensitive)?
9. How much of the glut rate in LLM judges (30% for flagships, family differences 19.6% to 59%) is calibration noise versus real evidence for both sides, and can it be used as a trigger for tool verification?
10. Do logic-checker add-ons (Logic-LM, SymbolicCoT) hurt on defeasible rulebreaker items in general, and does a paraconsistent checker avoid that harm?

## Gap search results

Tools: arXiv export, OpenAlex and Semantic Scholar APIs returned HTTP 429 on this pass; 4 web searches gave results, the rest were refused (shared budget used up). Papers opened as full PDF text: 2605.14115, 2504.00180, 2410.04068, 2605.27773, 2604.11209, 2604.02733, and re-opened 2507.09751 and 2505.23715. New evidence is in evidence_d.jsonl (d01-d19; d15-d19 are not opened or are syntheses). Claims K26-K32 added; K09, K11, K15, K16, K18, K20, K24, K25 got extra evidence ids.

Closed or mostly closed:
- Gap 3 (conflict type): self-contradiction in one document is hardest (accuracy 0.006-0.456), cross-document pairs easiest (to 0.893), implicit about 3x worse than explicit (d03, d05, d16). Priority for S6 is the own-trace self-check. Mostly closed.
- Gap 4 (notice but not report): PCBench token columns show a forced premise check lifts reporting (R1 19.6% to 67.7%, o3-mini 14.4% to 73.2%) and cuts tokens (R1 2590 to 1014; o3-mini 1279 to 1023) (d13). A written rationale is a poor audit channel (d14, d15). Mostly closed; still needs a test with our own conflict line.
- Gap 8 (order effects): yes. Resolution flips 11.4-25.2% of items on reversal (mean 18.6%, N=920 per model) (d01); detection moves only 0.4-2.8 F1 points for strong LLMs (d06); cross-source sign differs by model (d08). Closed for models tested (small, 2024-2026 open models).
- Gap 9 (glut as trigger): partly. Glut share varies 19.6% to 59.0% by family and 35.7% to 63.6% by topic (d12), so calibrate per model; a learned conflict score beat raw confidence for abstention (d02). Whether glut predicts wrong answers is untested.

Stayed open:
- Gap 1 (keep vs retract vs halt at equal tokens): no study. Closest is XoT (d09), keep-both-then-adjudicate beats plain prompts, not tested against retraction, halting or token-matched. Also ECon shows 24-38% of unprompted resolutions are silent random picks (d07).
- Gap 2 (bilateral vs matched unilateral): confirmed not controlled. Unilateral coverage 1.000 vs bilateral 0.499-0.589 (d11). The F1 gain may be selective classification.
- Gap 5 (da Costa consistent flag): no source found (d19).
- Gap 6 (adaptive retraction vs re-solve): no method tested. DeltaLogic (N=20-30, tiny models) shows failures concentrate on support-removal and defeating edits (d10).
- Gap 7 (missed LLM paraconsistent papers): re-run found only Allen et al.; not reliable because APIs were rate limited (d18). K25 stays single-source and should be re-checked.
- Gap 10 (logic checkers on defeasible items; paraconsistent checker): no new source (d19).

Corrections to earlier lines: none needed. Note d16 is a synthesis of earlier opened lines and is marked opened:false.
