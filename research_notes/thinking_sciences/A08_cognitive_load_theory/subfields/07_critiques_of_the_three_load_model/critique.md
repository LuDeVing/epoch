# Critique and cross-check: Critiques of the three-load model (A08.07)

Cross-checker pass. Inputs: evidence_a.jsonl (30 lines), evidence_b.jsonl (29), evidence_c.jsonl (25). Output: claims.jsonl (19 claims, A08.07-K01 to K19).

## 1. Numbers re-opened and checked (this session)

| # | Number | Source re-opened | Result |
|---|---|---|---|
| 1 | Adapala: Gemini-2.0-Flash 0.85 control, 0.82 / 0.78 / 0.72 at 20/50/80% | arXiv 2509.19517v2 PDF | Confirmed |
| 2 | Adapala: slope -0.003 per % load, CI -0.004 to -0.002 | same | Confirmed |
| 3 | Adapala: Long Control 0.82, p=0.45; Residue 0.78, p=0.12 | same | Confirmed |
| 4 | Adapala: residue vs similarity r=0.42 (Gemini), 0.35 (GPT-4o); hop recall 0.90 to 0.75, 0.80 to 0.65 | same | Confirmed |
| 5 | CogniLoad: U-shape in distractor ratio, gpt-5 0.97/0.89/0.91, o3 0.93/0.89/0.88 | arXiv 2509.18458v2 PDF | Confirmed |
| 6 | CogniLoad: 12 of 22 models below 50% by d=5; N=250 only gpt-5 0.76, o3 0.68 above 50% | same | Confirmed |
| 7 | CogniLoad: no interaction terms; interactions listed as future work | same (limitations paragraph) | Confirmed, and stronger than evidence a26 (it says outright the design supports interaction tests but they were not run) |
| 8 | Klepsch 2017 Study 1: F(1,89)=293.32 (eta2 .77), 199.96 (.69), approach difference F=1.18, p=.28 | Frontiers full text | Confirmed |
| 9 | Klepsch 2017 Study 2 fit: one-factor TLI .418, CFI .612, RMSEA .071, AIC 2185; three-factor CFI .970, RMSEA .021, AIC 845 | Frontiers full text, Table 5 | Confirmed |
| 10 | Krieglstein 2022: 53 articles, 67 experiments, N=7413, mean age 20.4; alpha ICL/ECL/GCL | Springer full text | Sample confirmed. **Correction:** the paper gives the pooled ICL alpha as both .823 (results paragraph) and .827 (discussion example); ECL .773 and GCL .860 are consistent. Evidence a18 used .827. Treat ICL alpha as about .82. |

Not re-opened (carried as reported): Jiang and Kalyuga 2020 (paywalled), Debue 2014, de Jong 2010 details, Shang 2026, Zhang CLAI, Mittal 2026, Upadhayay 2024.

## 2. Problem found in the evidence files

- evidence_c.jsonl lines c11 to c27 (red herrings, BRAINTEASER, insight problems, Illusion of Insight, Jones 2003, Knoblich) belong to an insight-problem-solving subfield, not to critiques of the three-load model. They look pasted from another run. They were NOT used in claims. Only c01 to c09 (CogniLoad, Adapala, CLAI, CoThinker) are on topic. c10 (Wang 2026, tool-use cognitive load framework) was only partly read in my pass; not used.
- Evidence a18/a19 and b12 to b14 are the same paper (Krieglstein 2022) opened twice; a15/b08 to b10 are the same paper (Klepsch 2017); a17/b16 same (Jiang and Kalyuga); a23/b24/c04/c05 same (Adapala); a25 to a27/c01 to c03 same (CogniLoad); b21/c08/c09 same (CoThinker). I counted these as one independent source each.

## 3. Contradictions between sources

- Three vs two factors: Klepsch 2017 favours three correlated factors (CFI .970) but its own Study 2 could not separate it from a two-factor model; Jiang and Kalyuga 2020 (N=60) find two factors. Sample sizes are small (65 to 95 per task; 60).
- Distractor harm shape: Adapala sees graded, roughly linear decline (Gemini); CogniLoad sees a U-shape. Different tasks (multi-hop QA with relevant-fact retrieval vs. state-tracking puzzles), different distractor definitions. Not resolved.
- Germane load and learning: Debue 2014 finds no link to performance (r=.045); Krieglstein finds small positive (r about .17 to .22). Both small; consistent with a weak, motivation-flavoured construct.
- CLT-inspired agents: CoThinker gains on reasoning but its shared-memory part hurt newer GPT models (Table 4, math: 55.97 with it vs 62.36 without for GPT5-Nano). CLAI saves tokens at equal accuracy only on two Llama models.

## 4. Weak spots

- Almost all human evidence is questionnaire self-report with students (mean age 20.4); small N per study.
- De Jong 2010 and Kalyuga 2011 are argument papers with no new data. No direct additivity experiment was opened; Park 2010 is secondhand.
- LLM evidence is thin and uses CLT only as a label. CogniLoad and Adapala vary tokens, not "load" in a validated sense. The mapping "task length N = germane load" in CogniLoad is a stretch.
- Adapala: only 2 of 5 models informative; 3 scored zero everywhere. GPT-4o result did not reach significance in regression.
- Shang 2026 near-misses vs a stronger baseline (p=.63, .16) mean the gain depends on the comparison arm.
- Search coverage of 2020-2026 LLM work is partial (two APIs rate-limited in the earlier phases).

## 5. Snippet-only / not opened

Sweller 2010 (abstract only), Kalyuga 2011 (abstract only), Park 2010 dissertation, Leppink 2013 (full text not opened), Paas 1994/2003, Zu et al. 2021 (via Krieglstein only).

## GAPS

1. Does any experiment, human or LLM, fit a model with interaction terms between intrinsic difficulty, extraneous material and learning-process load at fixed time or tokens? (Decides whether our budget may be a sum.)
2. In CogniLoad-style grids, are the distractor and length effects interactive for frontier reasoning models at equal output tokens? (CogniLoad left this as future work.)
3. Is the U-shaped distractor response reproduced on retrieval-heavy tasks, or only on state-tracking puzzles? (Adapala vs CogniLoad conflict.)
4. Does asking the model to self-rate difficulty or effort predict its own errors, and does it leak (rise when only distractors change)? (Decides whether any self-rating gate is safe.)
5. Do CLT-labelled prompt designs (CLAI, CoThinker) beat plain CoT and a plain token-budget prompt at equal tokens on tasks the authors did not pick?
6. Is there an LLM analogue of expertise reversal: do helpful extras (examples, restatement) hurt strong models but help weak ones? (Zu 2021, de Jong; not tested on LLMs.)
7. Does Park (2010) or any later direct additivity test exist with numbers, and do they replicate?
8. Does a constraint-reminder step (Mittal 2026) still help when the agent already has a verify state, at equal tokens?
9. Are germane-style rewards (longer, effortful reasoning) correlated with correctness or only with fluency in modern reasoning models?

## Gap search results

Evidence: evidence_d.jsonl (16 lines, d01 to d16; 12 opened this session). Search budget: web search ran out after 2 searches (shared limit); arXiv, Semantic Scholar and OpenAlex APIs returned 429, so I used direct arXiv PDFs.

Closed or mostly closed
- Gap 2 (CogniLoad interactions): partly closed. The appendix shows by eye that higher difficulty deepens the distractor U-shape and longer length flattens it (d01). Not a formal test, tokens not equal. Interaction is real in descriptive terms.
- Gap 3 (U-shape beyond state tracking): leaning answered. NoLiMa shows a steady fall with length and no recovery on retrieval (GPT-4o 98.1 to 69.7 from 1K to 32K), reasoning models too (d03, d04). Caveat: it varies length, not needle/hay ratio.
- Gap 9 (germane-style reward): closed against length. Shortest chain beats longest by up to 34.5 points (Hassid) and length correlates negatively with accuracy across 10 models (Feng); failed-step fraction is the better signal (d05, d06).

Narrowed, still open
- Gap 1 (interaction terms at fixed budget): no study fits them. Descriptive hints in d01 and d11 (o4-mini 55.0% to 32.5%). ToolLoad assumes additivity across steps (d12).
- Gap 4 (self-rated difficulty and leak): no distractor-only test found. Late answer confidence is calibrated better in reasoning models (33 of 36 settings), and P(IK) moves with context (d07, d08). Do not use a pre-reasoning rating gate.
- Gap 6 (LLM expertise reversal): no direct test. Simulated learners reproduce it (persona); extra shots hurt both strong and weak models (d09, d10).
- Gap 8 (reminder with a verify state): Mittal has no verify state and does not equalise tokens (d11). Open.

Stayed open
- Gap 5 (CLAI, CoThinker versus plain CoT and token budget on unpicked tasks): nothing new (d13).
- Gap 7 (Park 2010): source blocked by a bot check, no numbers, no replication found (d14).

Caveat: absence claims come from a small search budget and should not be read as proof that no study exists.
