# Critique: C02.08 Hybrid and connectionist (CLARION, Sigma)

## Corrections made (re-opened against extracted texts in D:/research_scratch/C02.08/)
Confirmed against full text: SwiftSage 84.68 / 45.34 / 36.43 / 33.82 / 15.56, 757.07 tokens per action, GPT-3.5 62.22 (a25, b11, b12, c14); Logic-LM per-dataset GPT-4 numbers (a26, c22); Distilling System 2 (98.0%, 75.69%, GSM8k 9.40 / 52.77 / 7.13; b15, b16, c15); Trotter AGL (g=1.069, 66 articles, 78 studies, 3,559 subjects, adults g=1.252; b23, b24); SOFAI-LM (graph coloring 42% vs 2%; DebugBench Python 70% / 37%, C++ 73% / 40%; c01); Kambhampati (12%, 82%, 70%; b19, c20); Schooler/Helie (45.8% vs 35.6%; a11).
Corrections and cautions:
1. c22 states Logic-LM "+39.2% over standard, +18.4% over CoT" next to GPT-4 numbers. The paper says the 39.2% is the GPT-3.5 average. Do not pair it with GPT-4 figures.
2. a26/c22: on PrOntoQA GPT-4 CoT (98.79) beats Logic-LM (83.20). The hybrid does not win everywhere (claim K04 marked contested).
3. b19 and c20 are the same Kambhampati paper counted twice. Likewise b11/b12/b13/c14/a25 are one paper, and b15/b16/b17/c15 are one paper. Independent source counts in claims.jsonl are therefore mostly 1.
4. b12: the 49.22 first column in SwiftSage Table 3 is probably the fast module alone; not verified.
5. a11 is typed "replication" but is a model fit to one human experiment (N=76), not a replication of the human effect.

## Contradictions and weak spots
- Almost every CLARION number is Sun's own group fitting its own model; no independent replication of CLARION fits was found. Fit statistics are mostly not reported (a03, b05), and failed fits are not listed.
- All LLM-hybrid positions for CLARION (a23, a24, b06, b07, c08, c10) are position papers with no measurements. The claim "LLM = implicit level" is untested.
- SOFAI results come from one group, compare against a reasoning model with fixed time limits, and are on graph coloring and debugging only.
- SwiftSage uses fine-tuning and hand-written switch rules; gains may come from the trained fast module, not the dual-process idea. No token-matched ablation against a single strong prompt.
- The Sigma LLM-era work is only qualitative (a22); Sigma accuracy is modest (a16).
- Human implicit learning evidence itself is inflated by publication bias (b23) and trust in intuition does not track performance (b25).

## Seen only in snippets or not opened
a27 (Sumers, title page only), b26 (Reber 1989, via Sun quote), b27 (Newell and Shanks 2014, not read), b28 and a02 (Sun, Slusarz, Terry 2005: abstract only), c19 (Sigma neural extensions, cited). Stocco 2018 (a19) and Sigma numbers (a15-a18, c18) were not re-opened in this pass. c17 column order of DPT results unverified.

## GAPS
1. Does a fast-default plus escalate-on-failure scaffold beat always-slow reasoning at equal total tokens on a mixed task set, outside SOFAI's own group? (SwiftSage and SOFAI-LM both lack a token-matched control.)
2. When does formalise-and-solve lose to plain CoT (PrOntoQA case), and can a router predict it per item?
3. Is there any measured test of an explicit-veto or validate layer over an LLM (Sun's four-step loop, b07)?
4. Does bottom-up rule extraction (RER style) from successful LLM outputs into a rule memory improve later accuracy, and does a wrong extracted rule cause cascading harm?
5. Is the CLARION result that explicit rule search hurts on non-salient tasks reproduced in LLMs (does forcing a "find the rule" step hurt)?
6. Do independent groups replicate CLARION's fits (process control, SRT) and report fit statistics and failures?
7. Does verbal overshadowing of insight (Schooler 1993) replicate in humans at larger N, and does it appear in LLMs when narration is forced?
8. Sigma and Standard Model: any quantitative result from using these architectures with LLMs (2024-2026), including Rosenbloom's 2025 arXiv papers (2412.16231, 2506.07807, 2506.12224, unopened)?
9. Does confidence-weighted selection (felt intuition) underperform verifier-weighted selection in LLM agents, mirroring b25?

## Gap search results (evidence_d.jsonl, d01 to d19)
Search limits: the shared WebSearch budget ran out after 4 calls here, and the arXiv, Semantic Scholar and OpenAlex APIs returned 429 or empty. Gap 6 and the insight version of gap 7 therefore stay open for lack of search, not proof of absence.

1. Fast-default plus escalate vs always-slow (PARTLY CLOSED). Independent of SOFAI: DART (d06) matches always-thinking on 13 of 14 model-benchmark pairs with 32-73% fewer thinking tokens; ODAR (d08) beats a proportion-matched random router by 8.3 macro points at the same call mix, and beats self-consistency at 1.78x lower cost. Both are single-group, savings are measured against always-think, and neither is a strict equal-total-token accuracy test. SwiftSage still has no token-matched control.
2. When formalise-and-solve loses (PARTLY CLOSED). Sprague 2025 (d09): CoT gain is +14.2 symbolic, +12.3 math, +6.9 logic, about +0.7 elsewhere; plan plus tool solver beats CoT on symbolic items, with parse failures counted as guesses. A task-type router is supported. Per-item prediction of the PrOntoQA loss was not tested; DART shows agreement between two cheap drafts is a usable trigger on math and code only.
3. Explicit veto layer over an LLM (CLOSED, negative for self-veto). Stechly 2024 and Huang 2024 (d10, d11, d18): GPT-4 self-verification Game of 24 3% vs 5% baseline vs 36-38% with a sound verifier; verifier false negatives 95.8% and 97.09%; GSM8K intrinsic self-correction GPT-4 95.5 to 89.0. The veto must be sound. Not tested on reasoning models.
4. Rule extraction and cascading harm (CLOSED for fixed-schema tasks). HtT (d12): filtered rule library +13.7 to +21.0 pts; random rules -33.7 to -40.7 pts; SCALAR (d13) shows trajectory feedback correcting wrong specs (88% to 67% without). Not tested on open-ended tasks or agent memory.
5. Forced rule search hurts LLMs (CLOSED). Mind Your Step (d01 to d03): AGL GPT-4o 87.5 to 64.4, exceptions task 2.9 to 12.5 passes, faces 64.0 to 51.2. Claude 3.5 Sonnet shows no drop, so it is model dependent. Not token matched.
6. Independent CLARION replication (OPEN). Nothing found (d19).
7. Verbal overshadowing (PARTLY CLOSED). Faces: registered replication (d04) gives -4.01% (31 labs) and -16.31% (22 labs) vs original 22-25%, task-order dependent. LLM analogue positive (d03). Schooler 1993 insight narration: no larger-N replication found.
8. Sigma and Standard Model with LLMs (CLOSED, none found). The three Rosenbloom 2024-2025 arXiv papers are conceptual (d15, d16). Nearest measured results are Soar (d14: 55% to 86%) and a CLARION-like LLM plus RL system (d13).
9. Confidence-weighted vs verifier-weighted selection (PARTLY OPEN). Self-reported-confidence routing trails agreement routing (d07); vote and reward-model selection plateau near 41% on MATH while coverage reaches 98% (d17). No direct felt-confidence vs verifier selection test.

Claims changed: K02, K08, K17 to established; K03, K04, K05, K06, K12, K14 extended; K18 to K23 added. Earlier cautions on a-numbers still stand.
