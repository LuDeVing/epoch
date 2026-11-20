# A14.05 Simulation vs theory accounts: cross-check critique

Checker pass, 2026-11-19. Re-opened the full text of 7 sources (PDF via pdftotext, one PMC page) and compared the numbers to evidence_a/b/c.

## Numbers re-checked

| # | Source | Result |
|---|---|---|
| 1 | Wilf 2023 SimToM, Table 1 (arXiv 2311.10227) | Confirmed. Rows are garbled in extraction but deltas fix them: Llama2-7b BigToM FB 47.5 to 70.5; GPT-3.5 BigToM FB 41.0 to 70.5, ToMI 67.25 to 81.0; GPT-4 ToMI FB 25.5 (0-shot) / 74.25 (CoT) to 87.75. |
| 2 | SimToM GPT-4 BigToM FB | Corrected wording. 0-shot 89.0, CoT 93.25, SimToM 92.0 (+3.0 vs 0-shot, -1.2 vs CoT). b10 said "slight decrease" and a16 "about the same or slightly lower". The sign depends on the baseline. |
| 3 | SimToM text on SC-CoT and ToT (33.50 vs 81.00) | Confirmed for SC-CoT (text says SC-CoT 33.50 on FB). The Tree-of-Thoughts number in c03 is not given separately in the text I saw; "Tree-of-Thoughts 33.50" in c03 is likely the SC-CoT figure. Treat c03's ToT number as unverified. |
| 4 | SimpleToM Table 3 (arXiv 2410.13648) | Confirmed. GPT-4o behaviour 49.5 to 82.8 with reminder; Claude-3.5-Sonnet 67.0 to 96.9; judgment 24.9 to 84.1; SysP and CoT weak. Llama-3.1-405B behaviour baseline is 58.2 (b18 had 58.3, c19 58.2). b18 wrote "judgment 10% to 24.9%" for baselines; correct range is 10.0 to 24.9 for the three models. |
| 5 | MMToM-QA Table 1 (arXiv 2401.08743) | Confirmed: text GPT-4 48.0, SimToM 52.5, SymbolicToM 63.0, BIP-ALM GPT-J 71.7; multimodal GPT-4V 44.0, BIP-ALM 75.3 / 76.7, humans 93.0 / 82.5; false-belief type 1.2 GPT-4 12.0, SimToM 15.0, SymbolicToM 61.0, BIP-ALM 69.0 (GPT-J). a17's "about 71" is 71.7. |
| 6 | ThoughtTracing Table (arXiv 2502.11881) | Confirmed: GPT-4o ParaphrasedToMi 59.5, +TT 76.0; FANToM AllQs 11.1, +TT 41.5, +TT+CoT 54.7; MMToM avg 56.5 / 60.0 / 69.0; goal 56.1 (CoT) to 37.8 (TT); o1-preview FB 100.0, TB 36.0. c16 and c17 correct. BigToM is near ceiling (98) so it is not informative. |
| 7 | Kosinski 2024 PNAS | Confirmed: 75% (CI 66-84), 90% contents vs 60% transfer, chi2 8.07, P=.01; davinci-003 90 to 60 to 20; GPT-4 95 to 75; GPT-4 failed at least one prompt in 25% of tasks. The "older models 80%" claim in a12 was not seen. |
| 8 | Wellman 2001 | Confirmed: R=.74, R2=.55; odds x2.94 per year; 50% at 44 months; 74.6% for a year older (56 months); below chance at about 41 months, above at about 48. |
| 9 | Kampis 2021 (PMC8386515) | Confirmed: 70 excluded, 90 analysed, 49 (54%) anticipated in familiarization 2 vs original 20 of 31 (65%); 22 of 49 correct at test, p=.568 exact binomial; 15 of 31 in FB1, 7 of 18 in FB2. The a09 limit "original N was 20" is unverified; original data are 20 of 31 passing. |
| 10 | Zhu 2024 (b13) steering table | Not resolved. The paper calls the focal agent "oracle" and I did not re-read the BigToM table; the Mistral row assignment in b13 stays inferred. |

Not re-opened: Strachan 2024 (a11, c24), Aoki 2025 (b12, c22), FANToM (a19, c11), Hi-ToM, Street 2024, UniToMBench, Hypothetical Minds, SymbolicToM table, Epley 2004, and all meta-analyses other than Wellman (abstract only).

## Corrections made

- GPT-4 BigToM SimToM effect: mixed sign, not "decrease" (see 2).
- c03: "Tree-of-Thoughts 33.50" probably SC-CoT; do not cite ToT number.
- Llama-3.1-405B SimpleToM behaviour baseline is 58.2.
- c10 SymbolicToM gains: column to question-type mapping was never done; cite only as "+4 to +99 depending on model and question type".
- a09: original sample statement should read 20 of 31 anticipating, not "original N was 20".

## Contradictions between sources

- Kosinski vs Ullman, Shapira: same tasks, opposite verdicts. Reconciliation: GPT-4 passes classic items; fails altered items; Strachan shows humans fail half of the alterations. Marked contested (K04).
- Reasoning models: ThoughtTracing says o1 over-suspects false belief (36% on true-belief); Street says GPT-4 at adult level on higher-order statements; Hi-ToM says near zero at order 4. Formats differ (true/false statements vs multiple choice vs stories), so these are not direct conflicts but cannot be merged (K19).
- SimToM: big gains in its own paper, tiny gains on MMToM-QA, harm in UniToMBench for small models. Likely because stories differ in structure, not a failure of replication, but no independent replication of SimToM on the same benchmarks exists in our evidence.
- Infant ToM: Onishi & Baillargeon (opened:false, abstract only) vs Kampis and Schuwerk replications. The 2005 finding is a different paradigm (looking time) from the failed anticipatory-looking tasks; its replication status is not checked.
- Zhu 2024 and Aoki 2025 call their findings consistent with simulation, but a decodable self/other belief direction fits theory accounts equally well.

## Weak spots

- The subfield is "background only". Almost no source tests simulation vs theory directly; only SimToM (a prompt), Aoki 2025 (mechanistic) and BIP-ALM (theory model) map onto the split. The mapping of SimToM to "simulation" and BIP-ALM to "theory" is by the authors' framing, not an experiment that varies one while holding the other fixed.
- Tests of the agent are mostly short story benchmarks, many template-built (ToMi, BigToM) and written by GPT-4 (BigToM). Template tracking is easy for symbolic trackers, which inflates SymbolicToM.
- Evidence a08, a10, a23, a24, a25, a26, a27, a29, b26, b27, b28, c26 were not opened. Founding studies (Wimmer & Perner 1983, Baron-Cohen 1985, Onishi 2005, Gopnik & Wellman 1992) have no verified numbers except via meta-analysis and secondary text.
- Many LLM results are 2023 models. Current frontier models (2025-2026) are barely covered except SimpleToM and ThoughtTracing.
- Equal-token comparisons are absent: SimToM uses two calls, ThoughtTracing many; none of the papers match tokens against CoT or self-consistency.
- Snippet-only items: Kulke 2018 (b28), Scholl & Leslie 2001 (b27), Babarczy 2026 (b26), Strachan abstract (c24).

## GAPS

1. At equal tokens, does a separate perspective-filter call (SimToM) beat CoT plus self-consistency on current frontier models, on BigToM, ToMI, SimpleToM and FANToM? No paper matches tokens.
2. Does a code-inserted "what does X know" line (SimpleToM reminder) plus a code-held who-knows-what ledger (SymbolicToM style) stack, and how much does each add on perturbed items (transparent container, informed protagonist)?
3. How good is the model-written perspective filter on multi-agent, evolving stories, and what is the error rate that stops the gain (oracle 96 vs model about 70-81 in SimToM)? UniToMBench suggests the filter collapses agents.
4. Do 2025-2026 reasoning models (o3, R1, Claude, Gemini) still show the true-belief failure seen in o1-preview (100 FB, 36 TB), and does a control-paired scoring rule fix it?
5. Is there any direct experiment varying simulation (role-taking first person) vs theory (explicit rule list about the agent) with everything else fixed, on the same model and items? Not found yet.
6. What is the independent replication status of SimToM, SymbolicToM, ThoughtTracing and Hypothetical Minds? All numbers come from the originating labs.
7. Do infant looking-time (violation-of-expectation) results replicate at scale (Onishi & Baillargeon 2005 paradigm, ManyBabies-style)? Needed to settle the infant-puzzle claim; currently only anticipatory-looking failures are verified.
8. Does applying inferred belief to action (SimpleToM gap) persist in interactive agent loops (Lombardi and Lenci, Riemer), and does a hypothesis list scored by outcomes (Hypothetical Minds) close it at equal tokens?
9. Are the Zhu 2024 steering numbers and the Aoki 2025 flip rates reproducible, and do they predict prompt-level benefit from first-person re-description?
10. How do humans do on the perturbed items per Strachan N=757 item-by-item, and which perturbations are fair tests for ToM (needs the full table, not opened).

## Gap search results

Gap searcher pass, 2026-11-19. Wrote evidence_d.jsonl (16 lines, d01-d16; 11 opened, 5 abstract-only marked opened:false) and updated claims.jsonl (K06 now contested, K21-K25 added). WebSearch budget was exhausted after one useful query, and arXiv, Semantic Scholar and OpenAlex APIs returned 429 for most calls, so ManyBabies 2 and several paywalled replications could not be reached.

| Gap | Status | What was found |
|---|---|---|
| 1 Equal-token SimToM vs CoT+SC | Open, partial | No paper matches tokens against SimToM. Gong 2026 (d01-d03) compares reasoning vs CoT vs capped thinking on HiToM, ToMATO, ToMBench: DeepSeek-V3 plus CoT 0.665 to 0.723, o3 effort high is worse (0.838 to 0.693). Closest compute-aware evidence, but not SimToM. |
| 2 Reminder plus ledger stacking, perturbed items | Open | Nothing tests both together. OmniToM (d04) shows the ledger step is itself weak (F1 61.63 best). |
| 3 Filter quality on multi-agent stories | Partly closed | OmniToM: model-written belief extraction F1 under 0.62, knowledge access 56-75%. Supports "filter quality limits gain". Oracle-vs-model gap not re-measured. |
| 4 2025-26 reasoning models and true-belief failure | Partly closed | No false-belief vs true-belief split found. Gong 2026: o3, R1, Qwen3 reasoning do not beat non-reasoning twins on ToM and more effort hurts. Whether o3 repeats o1-preview's 100/36 pattern is untested. |
| 5 Direct simulation vs theory contrast | Open, one proxy | Chen 2026 (d06) varies first-person vs third-person framing with CoT as control: first-person better on belief structure (pairwise 0.66 vs 0.41). Different domain, one model, no theory-list arm. |
| 6 Independent replication | Partly closed | SimToM independently run by Chen 2026 (d05): mixed, large losses on BigToM belief accuracy (Qwen3-32B 0.355 vs 0.900), gains on SimpleToM action accuracy. Hypothetical Minds (d09) read in full but still the originating lab. SymbolicToM and ThoughtTracing: no independent runs found. |
| 7 Infant looking-time replication | Open | Kulke 2018 (d12) replicated 1 of 4 anticipatory-looking tasks (abstract only). A Song 2008 VoE replication (d13) was mixed. No ManyBabies-scale test of Onishi and Baillargeon 2005 located. |
| 8 Interactive loops, hypothesis lists at equal tokens | Partly closed | Riemer (d08): literal ToM 92-97% but functional regret 0.86-1.0 vs tabular 0.083, oracle inputs still worse. Hypothetical Minds (d09) helps but costs more than PlanReAct; Hanabi (d07): first-order ToM r=0.76. Equal-token test still missing. Lombardi and Lenci not opened. |
| 9 Zhu and Aoki reproducibility | Open | Zhu re-read (d11): +TpFo steering row 0.99/0.98/0.97 forward belief, but row labels are scrambled in extracted text, so mapping stays inferred. Aoki not re-opened. No independent reproduction found. |
| 10 Strachan item-by-item human table | Open | Main text gives N=757 humans failing about half the perturbations; per-item table is in the supplement, not opened (d16). Note: 1,907 is the separate battery sample. |

Correction to earlier notes: Strachan's human N is 1,907 for the battery and 757 for the perturbation study.

Biggest new finding for the schema: the one independent test of SimToM disagrees with the originating paper on belief questions, so a perspective filter should be a tested option, not a default (see K06, now contested).
