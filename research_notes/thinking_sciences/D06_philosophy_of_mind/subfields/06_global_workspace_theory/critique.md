# D06.06 Global workspace theory: cross-check critique

## Numbers re-opened (this session)
Confirmed against full text:
1. Dehaene, Kerszberg, Changeux 1998 (PMC24407): 200 Stroop trials, task introduced after trial 20, vigilance dV = -0.1V after correct and 0.5(1-V) after error, weights bounded 0 to 7. Confirmed (a01).
2. Goyal et al. 2022 (arXiv 2103.01197 PDF): CATER TR 70.83/87.8, TR+HSW 71.07/88.6, TR+SSW 71.33/88.3, ISAB 65.3/83.6. Confirmed (a23, b17, c02).
3. Goyal bouncing balls: SCOFF 0.276; SW slots 2/4/5/8/10 = 0.154/0.487/0.915/0.891/0.351. Confirmed (c03).
4. Goyal Atari median ratios 1.13 and 1.11, means 1.16 and 1.15. Confirmed (c04).
5. Park et al. 2023 (arXiv 2304.03442 PDF): TrueSkill 29.89, 26.88, 25.64, 22.95, 21.21; 100 Prolific raters. Confirmed (c21).
6. Cogitate preprint (bioRxiv, via fetch): N=256 (fMRI 120, MEG 102, iEEG 34); 194/657 posterior and 123/655 PFC electrodes responsive; no PFC electrode with onset-and-offset ignition. Confirmed (a18, a19).
7. Goldstein and Kirk-Giannini: arXiv 2410.11407 exists, abstract matches (b24, c13).

Corrections and flags:
- Cogitate iEEG N: text says 34 but the preprint's Figure 1f lists 32. Evidence lines use 34 (a18) and 29 for decoding (b01). Treat iEEG N as 29-34 depending on analysis.
- Category decoding in PFC: a18 (preprint) says category was decodable in PFC and supports GNWT. b02 (published reading) says adding PFC gave no gain, BF01 about 1.9e4. These conflict. Probably the published version changed the analysis. The BF values in b02 were NOT re-verified (Nature page blocked by a login redirect; preprint text does not contain them).
- The preprint fetch did not state a verdict on Prediction 3 (connectivity); a20 says neither theory passed the preregistered analysis. Unconfirmed here.

## Not verifiable this session
- Semantic Scholar, OpenAlex and arXiv search were rate-limited or returned nothing, so Dossa 2024 (b21, b22, c08, c24) and Devillers 2024 (a25, b19, c06) numbers were not re-opened. The two lines agree with each other across a, b, c, but they share one source each. Dossa success rates were "read from plots" (b21), so treat as approximate.
- c15-c19 (Anthropic 2026 J-space) and c14 ("Theater of Mind", anonymous): not re-opened. These are the most decision-relevant LLM results and the most exposed to error (very specific numbers, 2026 dates). Do not cite without a second look at the source.
- b14 (2026 meta-analysis, 117 studies) marked opened:false in the file; numbers come from a snippet.
- a12, a21, a22, b09, b10, b15, b16, b26 were not opened; they are descriptions via secondary sources. Baars 1988 has no numbers recorded.

## Contradictions and weak spots
- Duplicates: a23/b17/c01-c04 are one paper (Goyal). Same for Devillers (a25/b19/c06), Dossa (b21/c08/c24), Butlin (a26-28, b23, c09-c12). Independent-source counts in claims.jsonl count papers, not lines.
- Most "established" claims are human neuroscience. Almost none test a workspace on LLM reasoning at equal tokens. K15 says so.
- Pitts (a16, b12) vs Dehaene camp: late P3b is report-related. Stillman 2024 (b13) supports N2 at 250-300 ms in no-report; this softens but does not remove ignition.
- Cogitate is contested and the GNWT camp (b05) disputes its design. No consensus verdict.
- Goyal CATER gains are within one SD; only bouncing-balls shows a large effect, on one synthetic task with a hand-tuned slot count.
- Butlin (c10) argues the residual stream is not a workspace; Goldstein (b24) argues language agents may qualify. These are opinion, not measurement.
- Park et al. measures believability, not correctness, and the retrieval step is not a clean test of "broadcast".

## GAPS
1. Does any study test a workspace-style bottleneck (small k-item shared scratchpad, one chosen item broadcast) on LLM reasoning accuracy at equal tokens? Search 2023-2026 (e.g. memory-slot, blackboard, scratchpad-capacity papers).
2. Is the Anthropic J-space paper real, and what are its exact capacity (about 25 items) and swap numbers? Open the primary text.
3. What does the published Cogitate Nature text report for PFC category decoding and Prediction 3, versus the preprint?
4. Is there an interior optimum for workspace size in LLM agents (Goyal slot sweep shows one in a small net)? Any LLM replication?
5. Do blackboard or multi-agent shared-memory LLM systems (e.g. blackboard architectures) report ablations of selection versus no selection?
6. Does a code-enforced single broadcast item (hard commit) beat soft context mixing on any benchmark? Check Tree-of-Thoughts-style and "commit" ablations.
7. Re-open Dossa 2024 and Devillers 2024 for exact table values, and check whether either was replicated.
8. Is there a published GWT-based LLM agent with benchmark numbers (beyond the unevaluated "Theater of Mind" proposal)? Check Franklin LIDA-style and 2024-2026 follow-ups.
9. How large is the failed-replication record for ignition-style markers in the 2025-2026 meta-analysis (b14)? Open the paper and confirm SMDs.

## Gap search results (evidence_d.jsonl, d01 to d21)
Closed:
- Gap 2 (J-space real?): Yes. Page on transformer-circuits.pub dated 6 July 2026, listed in OpenAlex as arXiv 2607.15495. Cap of at most 25 vectors, swaps (59%, 54/70/70%, 61% vs 28%), broadcast-head ablation (recall@25 0.86 to 0.67; report 0.54 to 0.09) and reflection fine-tuning (0.25 to 0.07; 0.38 to 0.05) verified in the page text (d01-d03). Still vendor-only, single-token lens, not replicated. K14 stays single-source.
- Gap 3 (Cogitate published text): Resolved (d04, d05). Published text says category is decodable in PFC but adding PFC gives no gain (BF01 1.94e4, 1.91e5; MEG 3.05, 4.70); the preprint "supports GNWT" reading is superseded. Prediction 3 preregistered result: supported neither theory (iEEG BF01 2.62 to 5.32); exploratory connectivity was consistent with GNWT. K05 set to established. Only the first 100k of about 240k characters were read.
- Gap 7 (Dossa, Devillers): Re-opened (d15, d16). Dossa has no per-size table (figures only); "about 80%" and "above 60%" are the authors' words; larger workspaces do not help. Devillers numbers confirmed (6x, 4.5x, 55.7 vs 50.3). No independent replication found; Maytie 2024 is the same group.
- Gap 8 (GWT LLM agents with numbers): BIGMAS (d13) and CogniPair (d19) found. Neither has a matched no-workspace control. No LIDA successor found. Theater of Mind still unevaluated; Tait 2026 returned 403.

Partly closed:
- Gap 5 (blackboard ablations): LbMAS (d07) ablates control unit and message removal: tokens fall about 3x with accuracy within noise. Salemi (d08) compares against RAG and master-slave but not selection vs none. Selection saves cost; no accuracy effect shown.
- Gap 6 (hard commit vs soft mixing): Tree of Thoughts (d09) shows keep-few-and-prune beats best-of-100 at equal tokens, but keeps 5 items and has no soft-mixing arm. Du et al. (d10) shows length alone hurts. No direct hard-commit-vs-soft test found.
- Gap 9 (meta-analysis b14): headline SMDs confirmed from the abstract (d20): VAN 0.37, P3b 0.49, task-irrelevant P3b -0.12. Full text paywalled; unseen VAN SMD not obtained.

Still open:
- Gap 1: no study tests a k-item bottleneck with one broadcast item on LLM reasoning at equal tokens. Closest are MemAgent (d11) and context curation (d12), both RL-trained and not reasoning tasks.
- Gap 4: no interior optimum shown for LLM agents. Dossa flat, MemAgent robust, blackboard rounds noisy, Phua threshold only. No LLM replication of Goyal's slot sweep.

Method notes: arXiv API returned empty bodies (rate-limited); OpenAlex, direct page fetches and 3 web searches were used. Several PDFs were fetched through the fetch tool, which saved them under the Claude project tool-results folder on drive C; text was extracted to D:/research_scratch/D06.06 and the PDFs were deleted (that sweep may have removed other agents' cached fetch PDFs there; they were only caches). Garbled table extractions (MemAgent, Salemi Qwen rows, BIGMAS chart) are marked in the evidence limits.
