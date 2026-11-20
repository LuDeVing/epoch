# Critique: D05.01 Definitions and ideals (cross-check)

## Corrections made (sources re-opened this session)
1. Ennis-Weir (arXiv 2412.05753): 24.33 = mean of 20, 26, 27. Confirmed. CORRECTION: "undergraduate 13.8" in the abstract is the highest post-treatment mean from training studies, not the plain undergraduate mean. Plain undergraduate mean is 11.51 (SD 8.23), postgraduate 18.39 (SD 6.59), N=100 online. Evidence a18 and c01 mix these; z=1.60 refers to the 13.8 figure.
2. Same paper: computational thinking 3.84 (SD 1.56) vs human 3.92, z -0.15; problem-solving 1.00 vs 3.68 (SD 0.63), z -4.25. LogiQA human N=651. Confirmed.
3. Huang et al. (2310.01798): Table 3 values confirmed (GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5, 91.5, 89.0). The table column is "# calls" (1, 3, 5), so round 1 = 3 calls and round 2 = 5 calls. Oracle table confirmed (GPT-3.5 CSQA 89.7). The 74.7% answer retention is confirmed. The debate vs self-consistency numbers (c12) were not re-checked.
4. CriticBench (2310.04815): 54.14%, 83.5 to 84.0, 91.3 to 92.7, error reductions 3.03/16.09/9.52 confirmed. a16, a17, b20, c07, c08, c09 are one paper and count as one source.
5. Sycophancy (2310.13548): 32% to 86% answer change, 98% wrongly admit, 95% preference-model choice confirmed. The "up to 27% accuracy drop" is attributed to LLaMA 2 in one place and Claude 1.3 in another; treat as "up to 27%, model unclear".
6. Kosmyna (2506.08872): 54 then 18 participants confirmed.
7. Huber and Kuncel: the OpenAlex abstract confirms substantial gains and that curriculum-wide efforts do not necessarily give extra gains. The 50th to 72nd percentile figure was NOT re-confirmed (full text not opened).
8. Gerlich 2025: OpenAlex shows a published "Correction ... Error in Table". Do not use r about -0.68 until re-read.
9. Abrami 2015: the OpenAlex search returned a different paper; g about 0.30 stays unverified (recalled).
10. Facione Delphi numbers (46 experts, 61% / 30% split) rest on one opened source set (a05-a10); b14, c32 are memory-only.

## Contradictions
- The same papers appear in a, b and c (Zhong o1, Huang, Luo, Lee, Kosmyna). Claims count each paper once.
- Ennis-Weir human baseline 13.8 vs 11.51 (correction 1).
- Delphi says CT skills transcend subjects; McPeck denies this. No decisive data either way.
- Huang (self-correction hurts) vs CQoT and self-check filtering (critique helps slightly). Reconcile by the conditions (external signal, certainty gating), not as a true contradiction.

## Weak spots
- Almost all LLM evidence is critique ability, one reading of "critical thinking". Dewey, Ennis and Facione have no LLM test of their own definitions.
- Human-vs-o1 comparison: 3 runs on Ennis-Weir, 10 on LogiQA, mismatched cohorts. Treat as anecdote.
- AI-and-human-CT studies are correlational surveys (Lee N=319, Gerlich) or tiny EEG (18 per group).
- Most LLM numbers come from 2023-2024 models; no frontier 2025-26 re-run of the self-correction or critique results.

## Only seen in snippets or memory
a11 (Ennis 1987), b11, b13, b14, b25 (Bastani), c27 (fallacy awareness 2026), c31 (Gerlich), c32, c33. Do not cite numbers from these.

## GAPS
1. Does intrinsic self-critique still hurt on 2025-26 reasoning models when gated to low-certainty items? Re-run Huang-style tables.
2. Which of the six Delphi skills does the schema cover weakest (explanation and self-regulation are likely holes)? Build a skill-to-operator audit.
3. What is the measured effect of an up-front premise check (is the question well-posed) on faulty-premise benchmarks at equal tokens?
4. Can stance-holding (resisting "are you sure?") be added without raising stubbornness? Need flip rate on right vs wrong answers.
5. What is the false-alarm rate of a critique operator on correct answers, and its token cost?
6. Verify Abrami 2015 (g+) and Huber and Kuncel (percentile) from full text; neither opened.
7. Does a general CT prompt transfer across domains for LLMs, or does it need domain examples (the McPeck question tested on a model)?
8. Is Ennis-Weir usable as a blinded, multi-run probe for the agent? Needs 10+ runs and a fixed judge.
9. Is there a prompt-level analogue of the dispositions (open-mindedness, suspending judgment) that can be measured separately from skills?

## Gap search results (evidence_d.jsonl, d01 to d18)
Search note: WebSearch budget ran out after 2 calls and OpenAlex, arXiv and Semantic Scholar returned 429, so sources were opened by direct page and PDF fetch only.

1. **Partly closed.** CorrectBench (2025) shows intrinsic correction is still task-dependent and marginal on reasoning-trained models (d07, d08); Silver 2025 shows within-response correction of injected errors works (d09); parallel voting beats extended rethinking by up to 20% (d10). No certainty-gated re-run of the Huang tables exists in what we found. Still open: run it ourselves.
2. **Closed (own audit, d15).** Weakest Delphi skills in the schema: explanation (one model-written line) and interpretation (S1 has no fidelity check). Needs a test, not more reading.
3. **Open.** No equal-token premise-check result found. SYCON false-presupposition items (d06) show stance prompts do not fix them, so the two fixes are separate.
4. **Mostly closed.** Flip rates on right vs wrong answers exist (FlipFlop, d01: GPT-4 10.4% vs 30.3%; every model flips wrong more than right). 2026 reasoning models are more consistent except Claude 4.5 (d03). Prompt cues help on opinion and ethics items (d06). Still missing: a measured stance-hold method that reports both flip rates after the fix (d02 reports only accuracy).
5. **Mostly closed.** ProcessBench gives false-alarm rates on correct solutions: o1-mini 2.1% and 4.9%, GPT-4o 8.8% and 23.4% (d11). Token cost per critique not reported; math only.
6. **Half closed.** Abrami 2015 verified: 341 effect sizes, g+ 0.30 (d13). Huber and Kuncel abstract has no numbers; the percentile figure stays unconfirmed (d14).
7. **Open.** No direct test; indirect evidence of uneven transfer (d17).
8. **Open.** No 10+ run blinded Ennis-Weir study found (d18).
9. **Partly closed.** Dispositions can be proxied by flip rate, false-alarm rate and revision on a disconfirming input (d16); no prompt-only disposition manipulation with measured effect was found.

Corrections to earlier notes: FlipFlop headline 46% flips and 17% drop (table averages about 44% and 16%). New claims K17 to K21 added; K11 raised to established (three independent sources); K06, K07, K08, K02 extended.
