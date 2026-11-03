# Critique: E08.05 Surface-cue heuristics (cross-check)

## Numbers re-opened this session (checked against source text)
1. HANS (a08, c05): "less than 10% in most cases, when chance is 50%"; BERT 39% conjunction, 0% subject/object swap, 49% conditional. Confirmed. Augmentation: 30,000 extra examples, about 8% of 392,702 MNLI items. Confirmed.
2. GSM-IC (a10, c01): "no more than 18%" consistently solved; code-davinci-002 macro 30.0 and 45.0 and micro 88.1 appear in the paper tables. Confirmed.
3. GSM-NoOp (a12): abstract says up to 65%; text gives Phi-3-mini over 65, o1-preview -17.5, Gemma-7b-it -20.6, Mistral-7b-v0.3 -24.0. Confirmed.
4. Zheng 2024 (a17, b17, c14): 34.6/27.3/22.3/15.8; gpt-3.5 67.2 to 60.9 at D (-6.3); llama-30B +15.2 to 68.2 vs 65.3 at A (originally 53.1 vs 67.2). Confirmed.
5. Turpin (a13): abstract says "as much as 36%" on 13 BBH tasks. Confirmed (the 36.3 decimal was not re-read).
6. Jia and Liang (a07): abstract says 75 to 36 F1 over sixteen models, 7 for four models with ungrammatical words. Confirmed in rounded form; the decimals (75.4/36.4, 75.7/31.3/6.7) were not re-checked.
7. BiasMedQA (a19, b18, c17): 1,273 USMLE questions and six LLMs confirmed in the abstract. Per-bias means were not re-checked.
8. Mamede 2010 (b02): N=36 (18 + 18), PGY2 1.55 vs 2.19, P=.03 confirmed from the abstract.
9. Sherbino 2014 (b03): 52% vs 48% (p=.91), 54% vs 48% (p=.13), 64% vs 77% (p=.12), 45% both (p=.98) confirmed. CORRECTION: the 191 participants are medical students on an emergency medicine rotation, not residents or doctors.
10. O'Sullivan 2019 (b06): N=76, 2.8 vs 3.1, CI -0.94 to 0.45, P=0.49 confirmed. Participants ranged from student to attending; qualitative feedback was positive.
Also confirmed from abstracts: patient-voice study (b20: 1,000 cases, 12 models, -9.6, CI -11.0 to -8.2, 26% more errors, gap halved, +3.9) and the agentic oncology study (b21: 32 models, 68%, R=0.69, 57% to 26%).

Corrections to carry: (a) b03 population is students; (b) b20 says CoT plus debiasing instructions remove only about a fifth of the gap, added to claim K16; (c) decimals in a07 and the BiasMedQA per-bias means rest on the earlier reading only.

## Contradictions between sources
- Human trials: bias teaching and cognitive forcing give null results (b03, b06, b01), but reflection after exposure helped in Mamede (b02) and a review (b05). Speed vs reflect instructions showed no effect (b08, snippet only). b07 reports 71% vs 43% by expertise, not by instruction. Net: contested; the structure of the reanalysis seems to matter, not awareness.
- Take-The-Best (a05) shows cheap cue use can match regression, while HANS-type results show cue use failing. Both can hold: it depends on whether cue validity holds in the test distribution.
- Newer vs older models: c22 (one figure caption) says recent models decline more on NoOp, while BiasMedQA shows GPT-4 as most resilient. Not reconciled.
- CoT: helps Claude 1.0 on always-A (c13) but barely GPT-3.5; b17 says CoT did not remove option-position bias.

## Weak spots
- Rasmussen was read only through a secondary summary (a01, a02). Chi 1981 (a03), Reason 1990, Rouse 1978 and Tversky and Kahneman 1974 (a21, a22, a24) were not opened; their numbers must not be cited.
- Most LLM evidence is on 2022-2023 models (text-davinci-003, GPT-3.5, Claude 1.0, GPT-2). Little on current frontier models with cue-misleading diagnosis.
- Almost no direct LLM fault-diagnosis study of surface cues (device or software); evidence comes from math, NLI, QA and medicine and is transferred by analogy.
- b08 and the Gigerenzer review (b10) were seen only as snippets or abstract openings.
- Many effects come from adversarial sets built to trigger the failure, so real-world base rates are unknown.
- Singh 2026 authors flag that generation settings differ between voices, so cause is not shown.

## GAPS
1. Does a rewrite-then-reason (neutral restatement) step before diagnosis cut cue-induced errors in current frontier models, and at what token cost compared with best-of-N voting?
2. How large are surface-cue failures on current frontier models (2025-2026) in real fault-diagnosis tasks (software incidents, hardware), not just math, QA and exam questions?
3. Which structural check (differential reanalysis, cue-validity audit, permutation vote) beats a plain beware-of-bias instruction at equal tokens, given the null human results?
4. Is there a measured result on when fast symptom matching is good enough to skip the deep path (a cue-validity threshold)?
5. What measurable error rates do Rasmussen's original paper and Reason's strong-but-wrong rule give (primary text still unread)?
6. Does forced evidence re-request after a first guess raise recovery above the 34.4% seen in the agentic oncology study (b21)?
7. Do larger or newer models shortcut more (Tang) or less (BiasMedQA)? A matched scale study on cue-misleading cases is missing.
8. Does evidence order in logs or symptoms (lost in the middle, premise order) change accuracy in agentic tool loops, and does a sorted evidence summary fix it?
9. Is hint-following and sycophancy reduced by separating hypothesis generation from user-supplied hints?
10. Do the null cognitive-forcing results hold for expert clinicians, and is there an LLM analog of Chi's expert-versus-novice deep-structure sorting?

## Gap search results
Sources opened this session were arXiv full texts read with pdftotext (evidence_d.jsonl, d01-d16). Web search budget was exhausted, so the Semantic Scholar and OpenAlex APIs (both rate-limited) and a few direct page fetches were the only other routes.

1. Rewrite-then-reason (gap 1): PARTLY CLOSED. Effect is supported (d01 RaR, d02 S2A: 80.3% vs baseline 62.8%, GSM-IC +10 to +12 points; instruction-only did not match it; keeping the raw input visible lost 5.8 points). Weak models can lose accuracy (d15). Token cost vs best-of-N voting not measured in either paper: STILL OPEN. Models are 2023, not frontier.
2. Frontier fault diagnosis (gap 2): PARTLY CLOSED. ITBench (d08) and AIOpsLab (d09) give real-incident numbers (GPT-4o SRE diagnosis 13.81%; AIOpsLab RCA 9-45%), but they do not isolate surface cues and use 2024-25 models. A cue-conflict fault suite is still missing.
3. Structural check vs bias instruction (gap 3): STAYS OPEN. Only indirect support: plain self-recheck hurts (d07), regenerate-context beats instruction (d02). No head-to-head of differential reanalysis, cue audit and permutation vote at equal tokens.
4. Threshold for skipping the deep path (gap 4): STAYS OPEN. Kahneman and Klein conditions (d14, abstract only) and math overthinking data (d13) give the logic, no diagnosis threshold.
5. Rasmussen and Reason primary error rates (gap 5): STAYS OPEN. No open primary text found (d16). Do not cite rates.
6. Forced evidence re-request vs 34.4% (gap 6): STAYS OPEN. AIOpsLab shows step budget helps ReAct and Flash but plateaus for GPT-3.5 beyond 5 steps (d09); no forced re-request test.
7. Scale vs shortcutting (gap 7): STAYS OPEN, now better framed as contested (d05, d10, K29). No matched scale study on diagnosis cues.
8. Evidence order in agentic loops (gap 8): PARTLY CLOSED for static prompts (d03, d04); no agentic-loop or sorted-summary test.
9. Hint-following and sycophancy (gap 9): MECHANISM SUPPORTED, FIX UNTESTED (d06, d12). Hint use is rarely verbalised, so audit by structure, not by reading rationale.
10. Expert clinicians and Chi-style LLM sorting (gap 10): STAYS OPEN. No source found this session.

Claims changed: K17 upgraded to established (3 sources); K04 to established; K10 to contested; K05, K09, K23, K24 gained evidence; K25-K32 added. Caveats: d14 read as an abstract page only; d07 and d09 table rows were matched from garbled PDF text.
