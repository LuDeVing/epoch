# Cross-check critique: E08.03 Hypothesis limits

## Numbers re-opened this session (confirmed or corrected)
1. Mehle 1980 (a01-a03): full PDF from shareok. Confirmed 3.43 novice, 3.36 expert, 12.6/11.2/17.8 pooled, 67.5 expert and 504 percent. Confirmed.
2. Fischhoff et al. 1978 (a05, b01): full PDF. Confirmed .078 should be .468, observed .140; pruned tree 2 .227 vs .611; Exp 1 N=148 (93+29+26); 1 of 55; Exp 2 .217 and .346; Exp 6 .215, z=2.87, tau=.058; split +.066 "about a third greater". Confirmed. Note: b01 says "about doubled" and a05 says .140 (1.8x): consistent.
3. Goh 2024 (b22, c07): Crossref abstract. 76 vs 74, diff 2 (CI -4 to 8, p=.60), 519 s, LLM alone +16 (CI 2-30, p=.03). Confirmed. b22 gives finer values (76.3, 73.7, 1.6, 15.5); only the rounded abstract was re-seen.
4. Handler, Bedi, Shah 2026 (b25, c01): arXiv HTML (2605.15000). Confirmed n=500/490, Table 1 values, 70 to 48 average. Correction: the paper's own text says DeepSeek R1 fell "24 points" on MedQA but Table 1 gives 78 to 53 (25); the "6-46 points" range in the discussion conflicts with the smallest table drop of 7. Also false action is measured only on the 250/245 no-correct-option items, not on all items. Do not quote as general closure rate.
5. Braitsch 2026 (a23, c03, c04): arXiv HTML 2607.10275, first 100k characters. Confirmed 68.1 (Opus 4.6), 32/20/3, gap 23.0, 7.5/4.2/1.8, 56.8/56.7/25.7 percent, 212/323 (65.6) and 156/307 (50.8).
6. Sprenger 2011 (b07, a11): Frontiers full text. Table confirmed 261.8, 265.4, 264.7, 271.5 and F(3,161)=3.13. CORRECTION: the paper's text says "about 10 percent increase" but its own table gives 3.7 percent. Use 3.7 percent. Effect is small. Also N=167 recruited, df implies about 165 analysed.
7. Kourtidis 2022 (a10): Europe PMC abstract. Confirmed the summary: no clear consistent effect, possible biasing when true diagnosis listed. Exp-level numbers (50.0 vs 46.9, OR 1.196) not re-opened.
8. Staal 2021 (b16): Europe PMC abstract. Confirmed N=117, 115 vs 129 s, no bias effect. d=.37 and R2=.03 not re-opened.
9. Ke 2024 (a24, b24): arXiv abstract. Confirmed 0/80, 57/80, 64/80, 16 cases. Weak spot: no control arm is mentioned in the abstract; judge of accuracy not stated; "initial diagnosis 0%" is by construction (cases were chosen where bias caused misdiagnosis). So 71.3 percent is not evidence the multi-agent form beats one agent.
10. McDuff (b23, c08): arXiv abstract confirmed 59.1, 33.6, 51.7, 36.1, 44.4, 302 cases, 20 clinicians. These two lines are the SAME study (arXiv 2023, later journal 2025). Count as one source.

## Not re-opened (still only as the first agents recorded)
Savage 2024 prompt table (c11): abstract has no numbers; paywalled full text not reached. Treat "differential-diagnosis prompt gave no gain for GPT-4, a loss for GPT-3.5" as unverified. All b-lines marked snip (Kostopoulou 2016, Mamede 2010/2020, meta-analyses b18/b19, Sherbino b21, Weber 1993, Elstein book, Rouse 1978, Sprafka 1973, Graber 2005, Kanjee 2023, Barrows 1982). Also not re-opened: c05 Wang, c17 Mehta, c18/c19 Lu, c23 Pokharel, Schmidgall, Echterhoff, Knipper tables.

## Contradictions and tensions
- Count of hypotheses: Mehle (3.4, no skill effect) vs Elstein "3 to 5" vs Weber 1993 and Sprafka (many vs few hypothesis users, snippet inconsistent). The 4 plus or minus 1 may be a task and effort artifact (Mehle subjects typed on a keyboard; instruction was "all plausible"). No direct test of a larger count under prompting.
- Supplying hypotheses: Kourtidis finds no clear effect; earlier Kostopoulou work (a22) reports accuracy gains. Not resolved. Kourtidis also says validation bias when the true cause is listed.
- Availability bias: Mamede 2010 and 2020 find effects; Staal 2021 (N=117, pre-registered-style replication) fails to induce it; Sherbino finds cognitive forcing useless. So the "bias then debias" story is shaky in humans.
- LLM anchoring: strong in Lou and Sun (hints), weak or absent for confirmation bias in GPT-4 (0.2 percent, p=.91), and self-debias can over-correct (Echterhoff). Direction depends on bias type and model.
- Multi-role scaffolds: positive in Ke and MAI-DxO (but MAI-DxO also spends budget and tests; roles not ablated here), while Pokharel (c23) shows multi-agent deliberation hides anchors. Mixed.
- Human-AI: Goh null for physicians vs McDuff positive. Different tasks and rubrics.
- Year labels: b23 and c08 duplicate; b24 and a24 duplicate; a23/b31/c03 are one paper; b25/b26/c01/c02 are one paper; Mehle appears in a01-a04, a13, a14, b10. Raw independent source count is far smaller than line count.

## Weak spots
- Core human findings are old and small: Mehle N=12, Fischhoff students on one car-start tree. Fischhoff Exp 6 N=29 of 60 mailed.
- Most LLM evidence is 2026 preprints with new models; not peer-reviewed; benchmark items (MedQA no-correct-option) are artificial.
- Almost nothing measures breadth of hypotheses an LLM generates per cue set versus tokens. LLM studies measure accuracy, premature action or anchoring, not list size or coverage.
- Medical bias dominates; engineering, software and mechanical fault diagnosis are thin (Lu RCA, FVDebug).
- Rasmussen and Morris and Rouse have no opened sources in this folder (Rouse 1978 abstract only).
- No source tests Soar-like or schema-like external hypothesis ledgers at equal tokens.

## GAPS
1. At equal tokens, does an external hypothesis ledger with a forced "what is not on this list" step beat free-form lists on none-of-the-above tasks (Handler style) and on coverage of the true cause?
2. How many hypotheses does an LLM spontaneously list per cue set, does it plateau at 3 to 5 like humans, and does asking for N (3, 6, 12) change accuracy or only cost?
3. What is the pooled-sample curve for LLM generation: how fast do new distinct causes appear when sampling K independent generations (the Mehle curve for models)?
4. Does a wrong supplied hypothesis, or a correct one in the list, make an LLM seek less information and switch less (the Kourtidis validation effect), and which structural step removes it?
5. Do multi-role (challenger) scaffolds beat a single agent at equal tokens, with a proper control (Ke has none)?
6. Is staged-information anchoring (Braitsch 65.6 percent stuck) cured by forced from-scratch re-ranking each stage, or by keeping a best-seen ledger (Wang)?
7. Rasmussen (1981-86) and Morris and Rouse (1985) hypothesis-limit results: what exactly did they find on how operators generate and discard hypotheses, and with what numbers? (Unopened.)
8. Do the Savage prompt results (differential-diagnosis prompt no help for GPT-4) hold for current models and non-medical fault tasks?
9. Is hypothesis count tied to effort/response format (Mehle typed answers) rather than memory span? Any study varying output cost?
10. Which debiasing instructions help LLMs without over-correction (Echterhoff 40-52 percent decision flips), and does a structural check dominate an instruction?


## Gap search results

Evidence is in `evidence_d.jsonl` (d01 to d19). New claims K20 to K29 and edits to K02, K07, K10, K11, K13, K15, K18 are in `claims.jsonl`. Web search quota ran out partway; several publisher and repository pages were behind bot walls and were not worked around.

Status key: CLOSED = answered with opened sources; PARTIAL = indirect or analog evidence only; OPEN = no usable source.

1. Ledger with forced "what is not on this list" step at equal tokens: **OPEN, with a negative hint.** No study tests it. The closest arm is the chained "give something different" draw in VTC-Bench (d02): on differential diagnosis it lowered true-cause coverage (mean -7.9%, 1 of 8 configurations positive) and per-draw precision. Bedi 2025 (d06) adds a second none-of-the-above baseline (all six models lose 8.8 to 38.2 points). So the baseline is weak, but a bare exclusion instruction is not the fix. K21, K23.
2. Spontaneous list size and effect of asking for N: **OPEN, one indirect point.** No prompted-model study varies N. A trained 7B model lists 7 to 10 when length is free (d15). Prompted VTC caps at 7. No sign of a human-like plateau at 3 to 5, but nothing tests it. K29.
3. Pooled-sample curve for models: **PARTLY CLOSED.** Three sources agree that independent draws repeat a lot and distinct causes grow sublinearly (d01, d03, d04). Numbers: unique hypotheses 1.40, 1.79, 2.92, 4.56, 7.89 for K = 2 to 32 (induction); only +0.131 reference recall from 1 to 5 draws on 302 NEJM cases. Not yet measured on real fault cause spaces with a pooled-people baseline. K20.
4. Wrong or right supplied hypothesis and information seeking: **PARTIAL.** Acceptance of a wrong supplied option is measured and depends on authority and model (d07, d08), and biased test choice is measured (d10). Less information seeking or fewer switches after a supplied hypothesis is not measured for LLMs. Which structural step removes it is untested; instruction-level defenses work for strong models only (d08, d10). K24, K25.
5. Multi-role vs single agent with a control: **PARTLY CLOSED for general reasoning, OPEN for diagnosis.** Five debate methods did not reliably beat CoT or self-consistency (d13); at matched compute debate and mixture-of-agents win by 1.3 to 2.7 points (d14). Ke 2024 still has no control, and no diagnosis study has one. K26, K13 stays contested.
6. Staged anchoring: forced re-rank vs best-seen ledger: **PARTIAL, and K18 corrected.** The Wang scaffold (d11) is a ledger with removal reasons. It stopped silent loss in a 10-case deep subset (6/10 kept vs 0 losses) but cut top-1 from 60% to 40% and access from 90% to 80%. One model, top-3 success. No arm re-ranks from scratch. A second source (d12, triage) shows generic reasoning prompts do not lift early-evidence anchoring. K11, K18.
7. Rasmussen and Morris and Rouse: **STAYS OPEN.** Full texts were not reachable (bot walls). Confirmed only: Rasmussen and Jensen 1974 abstract (fixation and repeating routines after failure), the topographic vs symptomatic split (secondhand), the Morris and Rouse 1985 abstract (training and explicit guidance, no hypothesis count), and a 1985 Georgia Tech aid that displays hypotheses to offload memory (d16 to d19). Do not cite either for a hypothesis count. K28.
8. Savage prompt results: **PARTLY CLOSED.** Figures verified from the arXiv text (d05): GPT-4 76 vs 78 (+2.2, CI -1.4 to +5.8), GPT-3.5 46 vs 38 (-8, CI -13 to -4.5), 518 test items. Still 2023 models and medicine only. K22.
9. Count tied to effort or response format: **OPEN.** No study varies output cost. Nothing new beyond d15 (list length shaped by reward). K29.
10. Debiasing instruction vs structural check: **PARTIAL.** Instruction side is clearer: Echterhoff change rates 5.2% (GPT-3.5), 17.5% (GPT-4), 52.1% and 39.9% (Llama-2-13b, 7b), no ground truth (d09); prompt defense helps GPT-4o a lot and Llama-8B little (d08); counterexample prompting helps rule discovery 42% to 56% (d10). No head-to-head with a structural check. K27.

### New corrections and cautions from this pass
- **Wang 2026 (K18):** "0 regressions in 40 observations" came from a 10-case subset and left out the top-1 drop from 60% to 40%. Claim rewritten.
- **Echterhoff:** the 40 to 52% flip range is two Llama-2 rows (39.9 and 52.1); GPT-4 changed 17.5%. There is no ground truth, so "over-correction" is inferred.
- **Bedi 2025:** the results paragraph and the Table assign model counts in a different order; the Table was used. N is 68.
- **Savage:** read from the arXiv v1 text sitting in a shared scratch folder, not the journal version.
- **Lee 2025 unique-count table:** PDF text was garbled; the K = 2 to 32 series is clean, the MoC unique-gain range is read from parenthesized values.
- **Pareto paper:** abstract says +1.3 over self-consistency for debate, body says +1.4. Small, but quote one source.

### Still unsaid by any source (best next tests for our own harness)
1. Equal-token arms on a none-of-the-above fault set: free list, forced "is the true cause missing" step, independent re-sampling.
2. Request N = 3, 6, 12 on the same items; plot coverage, top-1 and tokens.
3. Wrong and right supplied hypothesis in an agentic fault task; count information requests and switches; add a forced refute-the-leader step.
4. Staged disclosure with three arms: free update, ledger with removal reasons, from-scratch re-rank; score retention and top-1 together.
5. Same-token single-agent self-consistency vs challenger scaffold on faults.
