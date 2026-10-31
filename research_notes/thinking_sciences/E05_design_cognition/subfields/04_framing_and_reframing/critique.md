# E05.04 Framing and reframing: cross-check critique

## Numbers re-opened this session (arXiv PDFs and ICCC/PMC text)
Confirmed: Shin 2025 (456 recruited, 280 kept, 218 LLM users, 93 reported trouble; times 23.25/28.35; CSI 64.28/64.85/61.01; experts +12.54% novelty). Step-back (PaLM-2L physics 66.4 to 73.2, chem 70.9 to 81.8; GPT-4 69.4 to 84.5 and 80.9 to 85.6; Llama2-70B 51.9 to 64.8; CoT 65.0 and 75.3; GPT-4 CoT 82.9 and 85.3; 20.5% fixed, 11.9% introduced, >90% reasoning errors). RaR (Day 54.29 to 93.33, Month 58.10 to 83.96, Year 57.14 to 89.52, avg 64.95 to 89.77). Mishra 2022 (12.5% and 6.7%; 24% corrected, 4% caused). Huang 2024 (GSM8K 95.5/91.5/89.0 GPT-4; CSQA GPT-3.5 75.8/38.1/41.8). Wadinambiarachchi (N=60, +0.32, BF 124). Sclar (76 points). Qi 2025 (DoT 0.956, CoT 0.395, o1 Task 3 0.126 vs GPT-3.5 0.287). Sood 2026 (29/189 vs 17/189, 7 students). PLOS ONE 2026 (4.64 vs 2.94 dz 2.48; innovation 4.66 human vs 3.40 AI).

## Corrections and cautions
1. Huang rows: columns are number of model calls (1, 3, 5), not rounds 1 and 2 as b18 reads. Values are right.
2. Mishra: "+12.5%" is the average few-shot gain in the abstract; the ROUGE-L figure (44 to 58) is a different metric. Do not mix them.
3. Echterhoff (c18): the "Admit/Reject" columns are admit rates under two wordings; GPT-4 0.375 vs 0.780 is a gap of -0.405. c26's "0.57" is the counterfactual-mitigated gap (-0.570), which is LARGER than baseline: a debiasing prompt amplified the effect. GPT-3.5 baseline has the opposite sign (+0.165). Wording "40.5% more admitted" in c18 is a loose paraphrase.
4. BRAINTEASER size is 1,119 in the data statistics and 1,100 in the abstract (a11 vs b17). Use 1,119 items, "1,100" as the headline figure.
5. PLOS ONE (b25): "problem framing" is a clarity rubric, so the AI win is not a reframing win. Innovation favoured humans.
6. Shin 2025: all tests are non-parametric nulls with no equivalence test; the "expert" split is post hoc from a 5-item quiz.

## Contradictions between sources
- Cheap LLM rewrites (step-back, RaR) give 7 to 25 point gains on benchmarks; the only human-rated design test (Shin) shows nothing. Different outcome type, not a true conflict.
- Sood (Dorst prompt wins, n=7) vs Shin (Dorst structure no gain, N=280). Sood used steps 1-3 and 6 only and measured "interesting".
- Huang (self-revision hurts) vs Li situation puzzles (restart with compacted facts helps): the latter uses accumulated external answers as signal, five puzzles.
- Deng: stronger models gain more from rephrasing; Qi: reasoning models gain nothing on reframing. Both consistent with "model capacity and task fit moderate".

## Weak spots
- No claim reaches "established": almost all rest on one source. Step-back and RaR are single-lab results.
- No study tests goal reframing (Dorst sense) by an LLM with a measured outcome other than Shin 2025.
- Schon, Dorst 2011/2015, Rittel, Lawson, Kaplan and Simon, Knoblich 1999, Paton and Dorst, Valkenburg and Dorst, Sio 2015 meta-analysis were NOT opened (a20-a31, b05, b07, b23, c22-c24). Their text is memory or secondary description. No numbers from them may be quoted.
- b04 (Dorst and Cross 2001) only abstract read; N=9.
- a13 CresOWLve: abstract only (17% drop).
- Computed percentages in a16, a15 read from charts.
- Old models (GPT-2/3, PaLM-2L, GPT-4 2023). No 2025-26 frontier or reasoning model on step-back/RaR.

## GAPS
1. Does an LLM-driven goal reframe (O8) beat no reframe on tasks with a checkable answer at equal tokens, with current models, beyond Shin's human-rated design tasks?
2. Do step-back and RaR gains survive on 2025-26 reasoning models and at matched token budgets with a paraphrase control?
3. What is the signal that should trigger a reframe (G1): repeated failure, low confidence, contradiction, or none, and what is the false-trigger cost?
4. Do equivalence tests (TOST) on Shin's data show the null is a real zero or underpowered?
5. Does exposure to the model's first frame anchor later frames (fixation) in LLM agents, as in Wadinambiarachchi, and does hiding it help?
6. What do the unopened foundations (Dorst and Cross 2001 full text, Sio 2015 effect sizes, Knoblich 1999) actually report in numbers?
7. Does the restart-with-compacted-facts trick (Li 2025) hold on more than five puzzles and on BRAINTEASER with current models?
8. Does a clearer frame (PLOS rubric) trade off against novelty in LLM-assisted work, and can the schema score both?
9. Do reasoning-length effects (Qi: more tokens hurt reframe generation) generalize beyond clinical reframing?
10. Which reframing types (abstraction, rephrase, inversion, goal change) add value separately, in one ablation?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d20, all opened this session from arXiv PDF text, except d18 which came through a hosted copy and a fetch-tool summary). Search quota ran out early, so papers were found through the Hugging Face papers index and arXiv PDFs. `claims.jsonl` now has 29 claims: K05, K06, K07, K10, K11, K12, K19, K20 updated; K21 to K29 new. K07 is now the only claim marked established (Huang, Tyen, Kang), plus K21 and K22 (two groups each).

**Gap 1 (goal reframe vs none on checkable tasks, equal tokens): partly open.** Best new evidence is d13: rewriting 30 hard puzzles into formal maths lifted o3 56.7 to 73.3 (p=0.023) and R1 50.0 to 63.3 (p=0.043), but the rewrite was one offline o3 call, not equal-token, and not a goal change. A hint with the insight helped more than a style rule. No study found that tests an LLM goal change against no reframe at equal tokens.

**Gap 2 (step-back/RaR on 2025-26 models with paraphrase control): still open.** No paper tests step-back or RaR on a reasoning model at matched tokens. Indirect: d11 shows Step-Back below zero-shot CoT on Qwen3.5-27B (56.71 vs 59.79, table read from garbled text) and unrelated prompts beating both; d10 shows prompt tricks add little on o1-preview while voting gives the steady gain; d12 sizes a paraphrase control at about 2 points.

**Gap 3 (trigger for reframe): mostly closed in direction.** Do not trigger on a generic re-check (d01: over 90% of reflections confirm, under 2% correct), or on run agreement (d05: 21 of 94 questions stable and wrong). Use a localised failure (d08) after sustained effort on one line (d07: too many switches cost accuracy; penalty raised AIME pass@1 38.3 to 44.1 on QwQ). Disagreement between self-made frames is a candidate signal (d15). The cost of a false trigger in an O8 agent was not measured.

**Gap 4 (TOST on Shin): partly closed.** The paper gives no means or SDs, so a true TOST is impossible from the text (d20). From group sizes (about 62 vs 218, inferred) the design excludes effects above about 0.45 SD but not small ones (d19). Raw data would be needed.

**Gap 5 (first-frame anchoring in LLM agents): partly closed.** Strong for first step lock-in (d02: wrong first step cuts accuracy about 40%; d01) and for prompted anchors (d03, d04). Hiding or showing opposing anchors helped in part (d03). Still missing: an experiment where the model's own first frame is shown or hidden to later frames.

**Gap 6 (foundations): partly closed.** Dorst and Cross 2001 numbers (9 designers, 2.5 hours, alpha 0.71, r=0.32) came from a hosted copy and need a check against the journal PDF (d18). Sio 2015 and Knoblich 1999 abstracts and effect sizes were not reachable (publisher pages blocked, Crossref has no abstract). Still open.

**Gap 7 (compacted-facts restart beyond 5 puzzles): partly closed.** d06 gives a large-scale analog: repeating all known facts closed about 15-20% of a 39% multi-turn loss across 200,000+ conversations, GPT-4o and 4o-mini. No BRAINTEASER test with current models found.

**Gap 8 (clarity vs novelty): still open.** No new source. Keep scoring clarity and novelty on separate rubrics.

**Gap 9 (token length beyond clinical): closed in direction, task dependent.** d16 (inverse scaling, famous-paradox framing), d17 (GPT-5 reading of 'some' and 'or' shifts -20.6 and -18.8 points with more effort), d07. Long reasoning still helps on hard maths, so claim K11 is marked contested.

**Gap 10 (which reframing type adds value): partly open.** No single ablation exists. Closest: d14 (distinct approaches beat format variants: OlympiadBench avg@3 67.56 vs 55.51) and d15 (+7.2% vs -0.51%). Abstraction and inversion have no isolated test.

**Cautions.** d11 and d04 numbers come from text-extracted tables. d13's conclusion contradicts its own result text on rewriting. d03 is a non-reviewed high-school-authored preprint. Scratch PDFs were left in D:/research_scratch/E05.04/ and are not needed.
