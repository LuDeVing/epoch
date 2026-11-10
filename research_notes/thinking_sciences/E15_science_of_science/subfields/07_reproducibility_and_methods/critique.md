# Critique and cross-check: E15.07 Reproducibility and methods

## Corrections made (sources re-opened this session)
1. Many Labs 2 (b06 said "about 14 of 28"). Re-opened PDF: 15 of 28 (54%) at p<.05; 14 (50%) at p<.0001. a06 is right; b06 is wrong.
2. Franco et al. (b08 said "about 65% vs 20%, from memory"). Crossref abstract of the Science summary: 10 of 48 null results published (21%), 56 of 91 strongly significant published (62%). a13's "40 and 60 percentage points" are from the paper abstract and were not re-checked. b08 numbers are approximately right but should be replaced by 62% vs 21%.
3. PaperBench (a18 label). a18 calls 24.4 (o1-high), 16.1 (Claude), 8.5 (o3-mini-high) and 26.0 (o1, 36 h) "CodeDev with IterativeAgent". Re-opened PDF: those are full PaperBench with IterativeAgent. Code-Dev (o1, IterativeAgent) is 43.4 +-0.8 (Table 6; the appendix table shows 43.3). b13 and c05 are right. 21.0/13.2 BasicAgent, 41.4 vs 26.6 human subset: confirmed. Note the appendix gives human best@3 on a different metric (72.4 on one rubric level).
4. Errington 2021 (b23, from memory): median effect 85% smaller confirmed in the eLife text. Also found: 92% or 97% of replication effects smaller than original (two text variants, both present); the 97% is for the overall sample, so use "85% smaller".
5. LLM hacking (Baumann): 31%, 50%, 94.4%, 98.1%, 68.3% all confirmed in the paper text.
6. Button et al.: the 21% median power (b09) is not in the abstract I could open. Abstract says only "very low". Keep as unverified.
7. Simmons et al.: abstract confirmed; the 61% figure (b07) could not be re-checked (publisher blocked the PDF). Keep as from memory.
8. OSC 2015 (36%, 35/97, r 0.403 to ~0.20) was read in full by agent A; I did not re-open it. Treated as trusted.

## Contradictions
- b06 vs a06 on Many Labs 2 (resolved above).
- a18 vs b13/c02 on which PaperBench variant the 24.4 number belongs to (resolved above).
- Replication of an LLM scaffold: IterativeAgent helps o1 (13.2 to 24.4) and hurts Claude 3.5 Sonnet (21.0 to 16.1). Not a contradiction, but it blocks any "scaffold X helps" claim without per-model tests.
- OSC headline vs Gilbert et al.: success rate depends on the definition (significance 36%, interval overlap higher). Only a Gilbert abstract was seen.
- Camerer markets calibrated in Nature/Science but overshot in economics (75.2 vs 61.1).

## Weak spots
- Three agent files cover the same ~20 papers; "independent sources" in claims.jsonl counts distinct papers, not evidence lines.
- Many founding-paper numbers in file B were written "from memory" (OSC, Camerer 2018, ML2, Simmons, Franco, Button, Benjamin, Errington median, Gilbert). Only the ones listed above were checked.
- Ioannidis 2005 is a model, not a measured rate. It is the main support for "search width lowers PPV", which is an analogy to LLM search, not a tested result.
- Almost all agent-replication results (PaperBench, CORE-Bench, REPRO-Bench, SocSci-Repro, ReplicatorBench) come from 2025-2026 preprints. Rubric graders are LLMs (PaperBench judge F1 0.83). Not peer reviewed in most cases.
- Models tested are old for PaperBench (Claude 3.5 Sonnet, o1). SocSci-Repro shows modern agents score far higher; the older numbers are not a guide to current capability.
- No direct study of "does a freeze-the-metric or pre-registration scaffold reduce false gains in an LLM agent loop at equal tokens". Everything on that is inference.

## Seen only as snippets or abstracts
Simmons 2011 (abstract), Franco 2014 (abstract), John 2012 (abstract), Button 2013 (abstract), Gilbert 2016 (abstract), Benjamin 2018 (not opened), Camerer 2018 BF figures (read by A, not rechecked), Head 2015 (read by A, not rechecked), Hardwicke/Obels row meanings (garbled table header; b25 unverified), Park et al. details (c17 read, b22 no figures).

## GAPS (most decision-relevant first)
1. At equal tokens, does best-of-N selection by a self-scored metric overstate the gain, and how large is the selected-vs-fresh gap as N grows? (Direct winner's-curse measurement on our agent; no LLM study found.)
2. Does freezing the scoring rule, prompt and stopping rule before the first run (pre-registration analogue) lower the false-gain rate in LLM agent loops? Any 2024-2026 study with measured numbers?
3. What is the false-positive rate of LLM-as-judge comparisons between two prompts or scaffolds, by number of items and seeds? What minimum N and seed count is needed to detect a 3-point gain?
4. Does showing the agent its earlier failed attempts (file-drawer analogue) reduce overclaiming? Evidence from agent self-correction or reflection studies with measured effects.
5. How well does an agent's own forecast of "will this claim replicate" calibrate (Brier score), compared with the human market/survey benchmark (Camerer 2018)? Any LLM forecasting-of-replication result beyond Saynova and Holtdirk?
6. What is the real median power in neuroscience and the exact Simmons per-practice false-positive rates (full-text check), plus Benjamin's Bayes-factor mapping, so the thresholds in the schema rest on read numbers?
7. Results on the same PaperBench and CORE-Bench tasks with 2026 frontier models, and with a verify-before-claim step: how much of the early-finish and anchoring failure disappears?
8. How should "cannot be reproduced" be rewarded in an agent loop? Measured effect of explicit abstention rewards or checklists on the 100-to-63% drop in non-reproducible-task accuracy.
9. Replication-crisis boundary: which effect types (large, simple, low p) survive, and does that map to which agent improvements (large vs marginal) survive re-test on fresh items?
10. Do independent samples from a single LLM (Park et al. near-zero variance) ever act as independent replications? Measured diversity vs vote-accuracy gain for self-consistency with temperature, persona and model mixing.

## Gap search results
Search limits: the WebSearch budget ran out after one call, and arXiv, Semantic Scholar and OpenAlex returned 429 for most of the session. Gaps 4, 5, 7, 8 (mostly) and 10 could not be searched properly. New evidence is in evidence_d.jsonl (d01-d17); claims K26-K35 added, K09, K11, K19 edited.

1. CLOSED. Hu and Tang 2026 (d01, d02) and SIREN (d04) measure the winner's curse for LLM prompt selection. Selection score exceeded held-out by 13-20 points at 16 items, 1-5 at 256; simulated optimism +1.5 pp (3 candidates) to +4.0 pp (50); MMLU-Pro bias +3.06 points for same-data winner vs -0.01 with a frozen shortlist and held-out splits. Caveat: small Qwen models, preprints.
2. PARTLY CLOSED. PACE (d05) and the pre-registered tests of acceptance rules (d03) exist. Pre-set rules cut false commits (72-100% false edits under greedy, under 1 edit per run for gates) but did not raise whole-run held-out accuracy; PACE's degradation claim did not replicate in Hu and Tang's pre-registered runs. No study freezes the scoring rule and stopping rule as a package. Status: contested (K29).
3. PARTLY CLOSED. Judge prompt sensitivity measured (JudgeSense, d07); judge calibration with 100 human labels (d08); minimum N derived by me (d09: about 690-1,370 paired items for 3 points). No study gives false-positive rate of two-prompt LLM-judge comparisons by item and seed count. My N is arithmetic, not measured.
4. OPEN. No reflection or failed-attempt-memory study with overclaiming outcomes found (searches blocked).
5. OPEN. No new LLM replication-forecast Brier results beyond Saynova and Holtdirk.
6. PARTLY CLOSED. Benjamin 2018 re-read: BF 2.5-3.4 at p=.05, 14-26 at p=.005, FPR above 33% at prior odds 1:10 (d12). Button 2013: page abstract says median power about 8-31%, so the 21% is not supported (d13). Simmons per-practice rates still unread (d14).
7. OPEN. No 2026 PaperBench or CORE-Bench frontier results found. Only the harness-evolution abstract (d10) on matched-budget baselines.
8. PARTLY CLOSED. One pre-registered verifier ablation (d11): precision 0.471 vs 0.353; abstract only, security domain. No abstention-reward study for non-reproducible tasks.
9. PARTLY CLOSED. Within LLM loops, large gains from weak starts survive any selection size, small gains do not (d17, d10). Mapping to psychology effect types is inference.
10. PARTLY OPEN. Candidate error correlation 0.44-0.60 (d16). No self-consistency diversity vs vote-accuracy study found.

Remaining weakness: all new LLM results are 2026 preprints from small models; none is peer reviewed. d10, d11, d15 are abstract or citation only.
