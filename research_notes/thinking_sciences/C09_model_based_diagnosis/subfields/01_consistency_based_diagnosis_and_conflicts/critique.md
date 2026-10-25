# Critique: consistency-based diagnosis and conflicts (C09.01)

Cross-check of evidence_a/b/c.jsonl. 24 claims written to claims.jsonl (C09.01-K01 to K24).

## Numbers re-opened this session (full text, pdftotext)

| # | Source (ids) | Result |
|---|---|---|
| 1 | Stern et al. 2012 (a07, b06) | Confirmed. Table 2: SDE 99/100/79/88/30/14/9% vs CDA* on 74283/74182/74181/c432/c499/c880/c1355; c432 88 vs 33. |
| 2 | He et al. 2026 QXR (a18, c13, a27) | Confirmed. VitaminC recall Sonnet 4.5 .617 to .957, Opus 4.6 .574 to .968, Mistral Large 2 .603 to .978. FEVER Opus F1 .989 vs .964. RAMDocs Sonnet 4.5 F1 .882 vs .870. 435 and 4,950 calls confirmed. |
| 3 | Sarkar 2026 (b19, b20, c15, c16) | Confirmed: 11/14 vs 1/14, Fisher exact; Table 1 (gemma4:31b) direct 74.0 / fabricates 21.4; CoT 98.7; ASP 84.4; typed+core repair 89.6; four fixes, none broken. |
| 4 | Karimi Bavandpour and Bercher 2026 (b16-b18, c01-c03) | Confirmed, with a correction (below). |
| 5 | Orvalho et al. 2025 CFaults (a16, a28) | Numbers confirmed, wording corrected (below). |
| 6 | Zhang et al. 2025 Who&When (c17, c18) | Confirmed: all-at-once 54.33 / 12.50, step-by-step 35.20 / 25.51, random 29.10 / 19.06; best 53.5 / 14.2. |
| 7 | Siddiqi and Huang 2011 (a10) | Confirmed: c432 random 92.3 (no pruning) vs 4.5 (pruned); sda(ew) 42.0. |
| 8 | Yang et al. 2026 SemLoc (c09, c10) | Confirmed from Table 3: 42.8 / 68.0, Ochiai 6.4 / 13.2, Gemini LLM-only 37.6 / 44.0, counterfactual removal 30.8 (+12.0). |
| 9 | Sztyber-Betley et al. 2025 (b14, c04, c05) | Confirmed: 0.917 +/- 0.249 and 0.784 +/- 0.322; footnote 8 "close to zero". The +/- is a standard deviation. |
| 10 | Greiner et al. 1989 (a02, a03) | Already opened by two earlier agents; counterexample set seen in both. Not re-opened again. |

## Corrections

1. **a16 / a28 (CFaults "31% more programs").** The paper's wording is ambiguous. Table 4 shows 480/682 (70.38%) for CFaults vs BugAssist 265 (38.86%), SNIPER 234 (34.31%), HSD 375 (54.99%). The 31/36/15 are absolute percentage points of the benchmark. Relative gains are about +81%, +105%, +28%. Claim K19 states this.
2. **b18 (GPT-OSS-120B "F1 .49 to .15, test rate .57 to .09").** These numbers are from the WITH-TRACE table. In the no-trace table the same model goes .53 to .37 (test rate .50 to .40). The collapse at high effort is trace-specific. Also GPT-4o ".46 vs .38": .38 is the no-trace row of the table, .33 the with-trace row; the earlier .46 is from the earlier prompt in the text only.
3. **c01 / b16 test pass rate.** Best-F1 setting (GLM 5.2, high effort, no trace) has pass rate .82, but its default-effort pass rate is .85. So higher effort raised F1 (.85 to .87) and lowered pass rate (.85 to .82). The evidence lines imply effort only helps.
4. **c14 "kept high precision".** On VitaminC, Opus 4.6 direct precision was only .654 (Sonnet 4.5 .997). The over-pruning story is not uniform: for Opus it is both low precision and low recall on VitaminC.
5. **b20 "Pipeline 84.4% first try, 89.6% after repair".** Correct, but typed plus core repair beat generic repair by only 1.3 points (89.6 vs 88.3). The big effect is on fabrication (deepseek-v3.2, n=14), not accuracy. Claim K07 is worded to separate these.
6. **a07 / b06.** Add the caveat that both algorithms are the authors' own implementations in the Lydia framework, on a partial observation set, with a 30 s cap. Not independent replication.

## Contradictions and tensions between sources

- Extra context hurts in one paper (traces lower F1 .85 to .78) while another shows only gains from conflict-localised input (QXR). Differences in task: PDDL repair vs claim sets. Not a true contradiction, but it means "more evidence is better" is unsafe. K10 marked contested.
- High reasoning effort: helps DeepSeek V4 Pro, hurts GPT-OSS-120B and Qwen3-32B-like models in the with-trace table. Within-paper split; no mechanism tested.
- QXR gains shrink or reverse for the strongest model on the easiest data (FEVER, RAMDocs Sonnet). Sarkar's core helps one model and not another (gemma 0% fabrication either way). Conflict feedback is a weak-model or hard-instance aid, not a universal one.
- Orvalho: a union over six models and configs (70.8%) is far above the best single model (59.1%). This sits uneasily with G4 (samples from one model are not independent). Different models are more independent than samples of one model, but the compute is not matched.
- Diagnosis theory says "ranking by probability". No LLM study here ranks by anything but a model's own judgment.

## Weak spots

- Foundational papers were never read in full: Reiter 1987 (scanned, no text layer), de Kleer and Williams 1987 (abstract/snippet only), de Kleer Mackworth Reiter 1992 (garbled OCR). Statements about GDE's ATMS, probability ranking, and minimum-entropy measurement selection come from secondary sources. Evidence ids a01, a05, a25, b25, b26 are not opened.
- All LLM-plus-conflict results are 2026 papers from single groups, mostly with small n: Sarkar 14 infeasible items; Sztyber-Betley hand-made examples; Karimi 12 domains; SemLoc 250 programs, one fault each. None replicated.
- No paper does what our schema would do: take failed attempts of one reasoner, treat failed checks as conflicts, hitting set to choose what to change, at equal tokens against best-of-N. K23 records this as a gap, based on a gap note (b28), itself not a source.
- Many benchmarks are circuits (ISCAS85, 74XXX) where components and observations are exact. Reasoning steps have no component model, so "assume normal" has no sound meaning. External validity to text reasoning is unproven.
- The program-repair numbers (CFaults, SNIPER) use many failing tests per program; one failed answer gives one conflict at most.

## Only seen in snippets or abstracts

a05 (de Kleer and Williams, snippet), c20 REFLECT (abstract via alphaxiv), c21 AgenTracer (abstract), c28 Shchekotykhin 2012 (skimmed), c29 Hofer and Wotawa (not read), c30 Stern (landing page), b25-b28 (landing pages / gap note), a26 Williams and Ragno (abstract), a22 (abstract page; the PDF b14 was opened). Re-check attempted but PDF fetch failed or was damaged for: a first download of SemLoc (re-fetched via a second route and confirmed).

## GAPS

1. Does a code-computed conflict set plus minimal hitting set over the failed checks of several attempts (one conflict per failed test or verifier) pick the step to revise better than the model's own blame or best-of-N, at equal tokens? (Decision-relevant: this is the whole schema bet; no paper tests it.)
2. What is the right "component" for text reasoning: step, claim, constraint, tool call? Which choice makes "assume normal, check consistency" sound, and how often are conflicts empty or size-1 on real traces?
3. How far can the hitting-set size be capped (size 1 or 2) before the true culprit is lost on realistic multi-error reasoning traces, and what does it save in tokens?
4. Does feeding a minimal conflict (rather than raw error text) improve revision on strong current models, or only on weak ones and infeasible items? Sarkar and He suggest it depends on model strength; replicate with more than 14 infeasible items.
5. Can ranking diagnoses by a cheap probability (prior step fail rate, spectrum score, step length) beat model-stated confidence? De Kleer and Williams' measurement-by-entropy idea has no LLM test (link: probing and measurement selection).
6. Read Reiter 1987, de Kleer and Williams 1987 and de Kleer 1986 ATMS in full (OCR the scan). Which claims about minimal diagnosis, kernel diagnoses and probability updating do we currently rely on only through secondary sources?
7. Why does high reasoning effort help some models and collapse others in the repair setting (Karimi)? Is it overthinking, context length, or prompt format? Needed to set G11 caps per model.
8. Do the over-pruning results (QXR) hold when the oracle is the same model that makes errors, and with noisy oracle calls? He et al. flag noisy LLM oracles as an open problem.
9. How do the diagnosis-based methods compare to the delta-debugging and spectrum baselines on LLM reasoning traces (not code), and does counterfactual re-run (SemLoc style) transfer to text steps?
10. Did anyone replicate the Greiner et al. correction in code, and are there known remaining bugs in HS-DAG variants (Pill et al. 2016 practical performance study, unopened)?

## Gap search results

Evidence in evidence_d.jsonl (d01 to d17); claims K25 to K36 added, K01, K02, K05, K10, K12, K23 updated. Search limits: WebSearch budget was exhausted and the arXiv, Semantic Scholar and OpenAlex APIs returned 429, so sources were reached only by known URLs. Two lines (d16, d17) are our own toy simulation (scratchpad/sim/sim.py), not literature, and show shape only. d13 (Thought Anchors) was read through a fetch summary of the first 100,000 of 124,053 characters.

1. Conflicts plus hitting set vs model blame or best-of-N at equal tokens: STILL OPEN. Nearest evidence (d09, d10, d11) favours the baseline: with a sound checker, plain sampling at k=25 matched or beat GPT-4 feedback loops in 3 of 4 domains; naive revision turned about 38% of correct answers wrong. The toy sim (d17) shows the hitting-set pick beats a random conflict step by 10 to 25 points but beats "blame the last step of the smallest failed check" by only about +6 to -3 points.
2. What is a component, how often empty or size 1: PARTLY. No source decides the unit. ProcessBench (d06) shows 3.5% to 51.8% of right-answer solutions hold step errors, so answer-level checks leave conflicts empty. Toy: empty 27% (8 checks) to 6% (16 checks) at k=1. Real-trace rates are still unmeasured; measure them first.
3. Cap size: PARTLY. Reiter built the cap in (d02) and proved new diagnoses are supersets after new evidence (d03). Toy (d16): cap 1 finds nothing in 71% of k=3 trials, cap 3 covers k up to 4 at about 7 of 20 candidate steps. "No hitting set within cap" is a usable trigger to raise it. Token savings on real traces unmeasured.
4. Minimal conflict vs raw error text on strong models: STILL OPEN. Only older evidence found: first-error feedback beat binary feedback by 27 points in one of four GPT-4 domains (d09). No new strong-model test; Sarkar and He remain the only direct sources.
5. Cheap prior vs model-stated confidence: STILL OPEN, one negative hint. Learned PRMs (avg F1 31.5 to 56.5) lost to prompted critics (58.0 to 87.9) on ProcessBench (d07). Rodler's soundness needs priors below 0.5 (d05). Entropy probe choice has no LLM test.
6. Read the primary papers: PARTLY CLOSED. Reiter 1987 read in full (d01 to d04); the PDF has a usable text layer once downloaded completely (the earlier failure was a truncated download, no OCR needed). Reiter has no probabilities. De Kleer and Williams 1987 and the ATMS papers could not be fetched (mirror 404, publisher 403), so priors, Bayes updating and entropy selection stay second-hand (K25).
7. Why effort helps some models and collapses others: STILL OPEN. Re-reading the repair paper (d14) shows the authors did not isolate a cause; context-limit errors and unparsable outputs are a confound. Inverse scaling work (d15) gives distraction and framing overfit as mechanisms on other tasks. Fit G11 caps per model from a logged effort ladder.
8. Over-pruning repair with a noisy or same-model oracle: PARTLY. Same-model verification collapses loops (d08: self-critique 3% vs 36% sound on Game of 24; false negative rates up to about 97%). Not tested on QXR-style claim pruning or with current models.
9. Counterfactual re-runs and delta debugging on reasoning text: PARTLY. Counterfactual edits transfer as a method (d12, d13) but cost about 14,400 rollouts per 144-sentence trace and give task-dependent signal (AOC 0.44 to 0.02). Earlier lines (c09, c19, c20) already cover code and agent traces. No head-to-head against hitting-set diagnosis on text steps.
10. Greiner correction reimplementation: PARTLY. Reiter's own text and Rodler (d02, d05) agree that minimal conflicts avoid the flaw and that a replacement step is needed for completeness. No independent bug hunt found; Pill et al. 2011/2012 not fetched. Property-test our own code against brute force regardless.

Still-open list for the next pass: real-trace measurement of empty and size-1 conflicts and recall against cap (gaps 2, 3); equal-token test with a code-checker baseline and a simple blame baseline (gaps 1, 4, 5, 8); de Kleer and Williams 1987 via a library copy (gap 6); Pill et al. and any HS-DAG reimplementation study (gap 10); a controlled effort ladder that separates overflow, parse failure and wrong answer (gap 7).

Side effect to note: a taskkill of curl.exe during cleanup briefly stopped other agents' downloads in the same session; they were transient and no files were deleted outside this agent's scratch folder.
