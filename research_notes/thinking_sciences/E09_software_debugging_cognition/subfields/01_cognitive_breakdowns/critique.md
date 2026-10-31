# E09.01 Cognitive breakdowns: cross-check critique

Files read: evidence_a (37 lines), evidence_b (30), evidence_c (27), evidence_d (15, gap-search additions). 109 evidence lines, 35 claims in claims.jsonl (K01-K35; K26-K35 are new from evidence_b).

## Numbers re-opened this session (full text, pdftotext, then compared with the evidence line)
Confirmed as written:
1. Ko and Myers (2005): 895 min, 159 breakdowns, 69 roots, 102 errors (33 led to new errors), chain mean 2.3 (SD 2.3) breakdowns and 1.5 errors; 46.4% debugging time; 93% coding agreement; Table 10 shares 77.4 / 18.2 / 4.4.
2. Olausson et al. (2024): human vs GPT-4 feedback 52.60% vs 33.30% (rows 62.21/45.67/14.67 vs 42.64/19.33/3.67); 1.05x repair-vs-pass@k.
3. Huang et al. (2023): GPT-3.5 GSM8K 75.9 to 74.7, CSQA 75.8 to 41.8, HotpotQA 26.0 to 25.0; GPT-4 GSM8K 95.5 to 89.0, CSQA 82.0 to 80.0, HotpotQA 49.0 to 43.0.
4. Zhou et al. (2026): 2,013 actions; 949 biased (47.14%) vs 45.72% of 2,084 earlier; reversal 505/2013 (25%) vs 1104/2084 (52.9%); LLM actions 434/808 biased (53.71%), 238/808 reversed (29.46%); 456/808 (56.4%) under the 15-category scheme; fixation 33 reversed (43.4%).
5. Langhout and Aniche (2021): 132 started, 96 completed; pooled odds ratio 3.82 [2.69, 5.42]; 7 of 14 atoms significant; text lists them as post-increment, pre-increment, remove indentation, logic as control flow, literal encoding, omitted curly braces, type conversion.
6. Jones and Steinhardt (2022): framing drop 22.3 to 30.5 points; copied 81% (Codex) and 70.7% (CodeGen) vs 4.5% and 0.0%; conflicting name 100% to 4.4-4.6%; order flip 50% to 17%; Codex deletes files on at least 80% with 3 or more imports.
7. Fucci et al. (2020): 45 students (23 sleep deprived, 22 normal); correctness -49.73%, CI [-1.58, -0.20]; engagement CI [-1.31, 0.04] includes zero.
Confirmed in the earlier pass of this step (Tyen 52.87 and +43.92 vs +20.39; DebugBench 4,253 / 93.6% / 55.9%; Mehta 1,750 trajectories; TrajDebug 381 / 205 / 104 / 22; Majgaonkar +12.6 / 18.5 / 31.0 / 82.5%; Chen MBPP table). Not re-opened this time.

## Corrections
- b02 says the indentation atoms were not significant. The paper text names "remove indentation atom" among the 7 significant atoms; a separate "indentation" row may be the non-significant one. The PDF table is garbled, so the per-atom odds ratios in b02 (range 2.7 to 56) and the repurposed-variables counts (12/25 vs 18/32) could not be matched to rows. Use only the pooled 3.82 and 7-of-14 figures.
- c01 gives "GPT-4 72.8 to 80.4 (UT)" and "Codex 61.4 to 70.8". In Chen's table, UT alone is 80.6 (GPT-4) and 69.4 (Codex); 80.4 and 70.8 belong to the UT+Expl and +Trace rows. a29 has it right.
- Duplicates counted as one source: Chen (a29, c01), Huang (a26, c04, c05), Olausson (a24, a25, c08, c09), Tian (a27, a28, c10, c11), LDB (a30, c12, c13), Zhou (b15-b18), Langhout (b01-b03), Jones (b10-b14), Mohanani (b04-b07).
- a26 labels the Huang numbers "round 1 / round 2"; in the paper's table 74.7 / 41.8 / 25.0 sit on the five-call row. Direction unchanged.
- a06/a07: Ko and Myers say "18% of all breakdowns" are runtime in one place and "18% of knowledge breakdowns in debugging" in another. Table 10: 18.2 = skill 8.1 + knowledge 10.1 points.
- a35: the 60-90% action-bias range was not checked at figure level.
- b15 (Zhou) is a partial replication of Chattopadhyay 2020: the bias share matches, the reversal rate does not (25% vs 52.9%). The study is a different sample (14 developers, LLM use), so it is not a clean failed replication.

## Contradictions and tensions
- Self-correction hurts (Huang) vs self-debugging helps (Chen, Reflexion). Resolved by the signal: gains need execution feedback or tests. But the Self-Correction Bench result (d01, d02) says reasoning models self-correct injected errors well, so K05 holds for non-reasoning models only.
- Reproduction-first pipelines (Agentless, AutoCodeRover) vs open agents (SWE-agent): confounded by model, year and harness. K16 stays contested.
- LDB (real traces help) vs Chen (model-written trace adds nothing): consistent, but the real-vs-imagined mechanism is inferred, supported directly only by AutoSD (K20).
- Jones (anchoring lowers code accuracy) vs Sovrano (anchoring has the lowest sensitivity, 5.9%). Different tasks and measures; not reconciled.
- Zhou: biased actions are as frequent as in 2020 but reversals are half as frequent. Either LLMs help recovery, or the samples differ; not separated.
- Awareness prompts: small gain for primacy (b22), near nothing for others (b21), and Sovrano's models can name a bias and still follow it.

## Weak spots
- The core human result is 7 novices in Alice, one analyst, no replication found (K18). The Reason skill/rule/knowledge split was never tested in software outside this study.
- The Whyline results (K04) all come from its creators, small samples.
- Gopstein 2017 (b30) was seen only as an abstract; the Java replication is novice-only and output-prediction only.
- Most LLM evidence is 2022-2024 models. 2025-2026 items (Mehta, Qi, Majgaonkar, Zhou, Sovrano, Self-Correction Bench, overthinking) are single preprints.
- SWE-bench contamination (c23) weakens all SWE-bench numbers.
- Nothing tests the skill/rule/knowledge taxonomy on an LLM; the mapping to G2/G3 is ours.
- Human bias studies (b08, b28) are not debugging tasks; sleep loss (K33) has no direct agent analogue.

## Seen only in snippets or abstracts (not re-verified)
a32, a35 range, b22 and b23 (figures, no exact numbers), b30, c14, c16, c21, c25, c26, c27 detail numbers, d-file details beyond the claims. The SWE-Search compute-matched table was garbled.

## GAPS
1. At equal tokens, how many failed agent runs, coded in the Ko and Myers chain (first wrong hypothesis, then fix errors), start with an unrevisited wrong first hypothesis? What fraction?
2. Does forcing 3 rival root-cause hypotheses, each with a cheap test, before the first edit beat direct editing at equal tokens, and is the effect larger on logic bugs than on syntax slips?
3. Which signal carries self-debugging gains: pass/fail, the failing message, or variable state? No controlled design compares them, or compares a cheap signal with the human-feedback 33.3 to 52.6% result.
4. Does a rule to change the hypothesis after one failed fix reduce fixation (the re-pasted fix, 43.4% reversal in Zhou) in agent runs, and what does it cost in tokens?
5. Can a trigger from tests or diffs (not an LLM log reader) decide rollback to the earliest critical step, given Who&When best step accuracy of 14.2%?
6. Does an is-a-change-needed gate (run the failing test first) cut action bias without causing the opposite failure of over-planning seen in 2025 reasoning models?
7. Does a Whyline-style prompt (state the assumption behind each why question, then probe it) help an LLM? Nothing published tests it.
8. Do reasoning models keep the "no blind spot" result on real code defects (not injected math errors) at equal tokens, and does a forced Wait-style recheck add anything?
9. Do the Ko and Myers shares (skill, rule, knowledge) replicate in any later human study (Reason 1990, Parnin and Orso 2011, Gilmore, Vessey are unopened), and do professionals show the same chain?
10. Does token-level surprise (perplexity peaks, 64% atom recall) on an agent's own plan or patch work as a cheap slip flag, and what is its false-alarm rate?


## Gap search results (2026-10-31)

Evidence added: d16 to d26 in evidence_d.jsonl (26 lines now; d01 to d15 kept). Claims: K36 to K42 added; K08, K10, K12, K13, K14, K16, K18, K19, K23 updated. Limits of this pass: the web-search quota ran out after a few searches, and the arXiv and OpenAlex APIs were rate-limited. "Not found" below means not found in the searches run. d23 (Kim 2026) is an abstract-level source only.

Status by gap:

1. Unrevisited wrong first hypothesis at equal tokens: STILL OPEN as asked, but narrowed. No study codes agent runs in the Ko and Myers chain. Nearest data (d16, d18): for strong models, 56.9% of SWE-Agent failures (60-69% for GPT-5 and Qwen3-Coder) reach and edit the right functions and still fail, against 19.3% search failures; about 65% of hand-coded failures were flawed reasoning, with fixation on a failing strategy (3.5 times more steps). So a wrong first location is a minority cause for strong models. Weak models differ (Qwen3-8B 41.1% Search).
2. Three rival hypotheses before the first edit: OPEN. Only CogniGent (d25) uses multiple hypotheses, for localisation, with no isolated ablation read.
3. Which signal carries self-debugging gains: PARTLY CLOSED. Failing message beats bare pass/fail by about 13 points (d23, abstract only); variable-state traces gave the largest ablation drop in TraceCoder (-10.5, confounded, d21); raw error text helps all seven modern models (d22). Still no controlled three-arm test and no comparison with the human-feedback 33.3 to 52.6%.
4. Change hypothesis after one failed fix: PARTLY. A forced "must change" instruction adds only 0.8-1.9 points (d23); an external reviewer broke some deadlocks (24 of 108, d18). Token cost and the specific one-failure rule remain untested.
5. Non-LLM rollback trigger: PARTLY CLOSED. Constraint checks lift step accuracy by about 13 points over a judge alone but stay under 50% on tau-bench (d19); a test-pass freeze recovered 5 of 5 tested lost patches and a consensus trigger gave +3.0 points, p=0.08 (d17); DoVer (d20) shows the decisive step may not be unique. No code-agent test of a test- or diff-based rollback at equal tokens.
6. Is-a-change-needed gate: OPEN. Nothing found.
7. Whyline-style prompt for an LLM: OPEN. Nothing found.
8. Reasoning models on real defects: OPEN. Self-Correction Bench stays on injected errors; Arimbur (d22) tests non-reasoning-era instruction models only.
9. Replication of Ko and Myers shares: OPEN. Parnin and Orso 2011 (d24) was opened; it studies a localisation tool and does not re-measure the shares (it does show fault-line sightings often go unrecognised). Reason 1990, Gilmore, Vessey remain unopened.
10. Token surprise as slip flag: OPEN. Nothing found.

Closed: none fully. Partly closed: 3, 5 (and narrowed 1, 4). Open: 2, 6, 7, 8, 9, 10.

Corrections found this pass: AgentRx now reports 170 trajectories (v2); an earlier version reported 115. The Who&When step-accuracy baseline in AgentRx was re-run by its authors with a modified prompt, so 18.8 is not the original 14.2.
