# Critique and cross-check: E13.07 Human error and recovery

## Input state
- evidence_a (30 lines), evidence_b (25), evidence_c (26), evidence_d (22) were read. The last four lines of c and the b/c overlap on LLM self-correction mean the same paper often appears 2 to 3 times (Huang a13/a14/b01/c01/c02, Tyen a16/b02/c06, ProcessBench a20/b08/c22/d09, Tsui a22/b13/c17/d01, Kamoi a19/b03/c05/d02, CRITIC a26/b09/c15, Self-Refine a25/b10/c13, SCoRe a24/b04/c16). Duplicates are not independent sources. Claims count each paper once.
- Human-error founding work is thin on primary text: Reason 1990 (a03), Rasmussen 1983 (a09), CREAM (a10) were NOT opened (opened:false). Their numbers are recalled, not read.
- Disk: drive D: does not exist on this machine, so no PDFs were saved. Re-checks used arXiv HTML pages, PubMed/Crossref abstracts and the PMC full text, streamed and not stored.

## Re-opened sources (10 key numbers) and result
1. Huang et al.: GPT-3.5 and GPT-4 oracle and intrinsic cells (a13/a14/c01/c02), checked earlier against the paper. CONFIRMED. b01 gave only the final-round numbers; the full progression is in a14/c02.
2. SCoRe Table 1 (arXiv 2409.12917 HTML): base 52.6 -> 41.4 (-11.2), right-to-wrong 15.8%. CONFIRMED. STaR conflict between b04 (-14.2) and c16 (+0.4): both are real rows. -14.2 is STaR on base data (55.4 -> 41.2, wrong-to-right 5.4, right-to-wrong 19.6); +0.4 is STaR with extra data (53.6 -> 54.0). CORRECTION: neither line named the variant (fixed in K12).
3. Snell et al. (arXiv 2408.03314): "around 38% of correct answers get converted back to incorrect ones" with the naive revision model. CONFIRMED (d03).
4. Zhang et al. dark side (arXiv 2412.14959): o1-preview 78.7 (down 4.9), 13.2% right-to-wrong; o1-mini 74.1 (down 4.2), 15.6%; R1 7.9%; V3 28.5%; o1-mini decision making 92.3% right-to-wrong. CONFIRMED. Note: the 92.3% is on one decision-making task, not a general rate.
5. Valmeekam et al. Blocksworld (arXiv 2310.08118): generator alone 40/100, LLM+LLM 55/100 (3.48 iterations), LLM+VAL 88/100 (4.18). CONFIRMED. CORRECTION to c11: the verifier table shows true-positive 54/55 (98.2%) and false-positive 38/45 (84.45%), true-negative 7/45 (15.55%). Accuracy 61/100 = 54 + 7. c11 says "passed 7/45 invalid plans (15.55% false positives)", which is backwards: the LLM verifier passed 38 of 45 invalid plans and rejected only 7. The lesson is stronger than c11 stated. K09 uses the corrected figure.
6. Stechly et al. (arXiv 2310.12397): baseline 16%; 40 instances where the generator produced an optimal colouring, the LLM verifier never recognised it, hallucinated adjacent same-coloured pairs in 39; sound-verifier backprompts about 16% -> nearly 40%. CONFIRMED. The "1 of 100 correct" for the self-critique loop was not re-found in the text snippet read, only the 40-instance paragraph; it is believed from c09 but treat as single reading.
7. Tsui (arXiv 2507.02778 abstract): 64.5% blind spot over 14 open models; Wait cuts it by 89.3%. CONFIRMED (abstract). The 76.0% fine-tune figure and per-dataset cells in d01 not re-opened here.
8. ProcessBench (arXiv 2412.06559): o1-mini 93.2/88.9/87.2/82.4, average 87.9; GPT-4o 79.2/63.6/51.4/53.5, average 61.9. CONFIRMED.
9. Tyen (arXiv 2311.08516): best overall mistake-finding accuracy 52.87 with direct step-level prompting. CONFIRMED. ReaLMistake (arXiv 2404.03602): recall 16.9 +/- 20.3 points higher for Type 1 over 12 LLMs and 3 tasks. CONFIRMED.
10. Human medicine and aviation (PubMed/PMC): Haynes 2009 death 1.5% -> 0.8% (P=0.003), complications 11.0% -> 7.0% (P<0.001): CONFIRMED (b23 now opened). Urbach 2014: death 0.71% -> 0.65% (OR 0.91, 0.80-1.03, P=0.13), complications 3.86% -> 3.82% (OR 0.97, P=0.29), 101 hospitals, 109,341 and 106,370 procedures: CONFIRMED (b24 now opened). Norman 2014 speed 44.5% vs reflect 45.0%, 69 s vs 89 s, wrong cases 17 s longer: CONFIRMED (b20 now opened; sample sizes not re-checked). Perneger 2005: 85 respondents, 15.3 of 23 correct (66.5%) vs 11.5 chance: CONFIRMED. Helmreich 2000 (PMC full text): "more than 3500" flights, two threats and two errors per flight, 1.4 times: CONFIRMED.

## Contradictions and tensions between sources
- Huang (intrinsic correction hurts) vs Liu (c20, temperature 0 and neutral prompts: roughly neutral). Not resolved. Most Liu cells move within noise; Huang used temperature 1 for GPT. K11 marks it contested.
- s1: c19 (abstract) says AIME24 50 -> 57 with budget forcing; d16 reports 50.0 -> 53.3 at 2x with Wait and MATH500 flat. These are different extrapolation budgets, not a conflict, but 57 should not be quoted without the budget.
- MAST (a28 vs c23): group shares 41.8/36.9/21.3 percent and per-mode figures 6.2/8.2/9.1 use different bases. The three verification modes sum to 23.5%, group share is 21.3%; do not mix.
- Spontaneous self-correction: d06 says self-correction in a thinking trace has a positive lift (+12.4 to +20.1%) while d07 says a mid-trace shift goes with much lower accuracy (2.57% vs 16.44%). Likely differing definitions of "shift" and models. K20 contested.
- Checklists and slowing down in humans: positive before-after (Haynes, Pronovost) vs null population study (Urbach) and null speed-vs-reflect trial (Norman). K15, K16 contested.
- c07/a17 versus c08: oracle location helps strongly, but a trained classifier at 60-70% accuracy is only break-even; the paper says its classifier does not reach that threshold.

## Weak spots
- The core human-error theory (Reason GEMS, Rasmussen SRK, CREAM control-mode probabilities) is not read from the source. Reason's 1979 diary figures (433 slips, 35 people, storage failures about 40%) and CREAM intervals are from memory and flagged unverified. Do not cite.
- Human error-detection numbers rest on a review (Blavier 2005) quoting Doireau 1997 (90% self-detected recovered, 30% third-person). The primary was not opened.
- Almost every LLM self-correction result uses GPT-3.5, GPT-4, PaLM 2 or small open models. Only d04, d06 to d10, ProcessBench and Tsui touch reasoning models. Claude-class models are barely tested (Tsui: Claude 3.5 Haiku 52.5%, Sonnet 4 41.4% blind spot, from c17, not re-verified).
- Single-domain results: Stechly (graph colouring, 100 instances), Valmeekam (Blocksworld, 100 instances), Reflexion HumanEval vs MBPP (b11: false-positive tests 0.01 vs 0.16, MBPP got worse).
- CRITIC cell labels (c15) were garbled in extraction; a26 gives cleaner HotpotQA and AmbigNQ values.
- Several 2026 arXiv papers (d06 to d15) are single, unreviewed, and from unreplicated groups.
- The agent_test fields propose tests at equal tokens, but none of the measured results controlled for token count except Huang debate vs vote, Olausson (equal samples) and Snell.

## Seen only in snippets or recalled
- a03, a09, a10 (opened:false): recalled.
- a08 (Allwood 1984): from a search summary, not the paper.
- a30 (KRAIL): abstract only, no numbers.
- b25 Pronovost, b22 Croskerry (opened per file; Pronovost numbers not re-verified here).

## GAPS (most decision-relevant first)
1. At equal tokens, does a code-located error line plus model fix beat plain resampling with vote on our own tasks, and by how much?
2. How often does a Claude-class model approve a known-wrong draft of its own (false-pass rate), compared with a cross-family or fresh-context reviewer? Everything above uses older GPT or open models.
3. Does presenting the model's own draft as someone else's work (the Tsui effect) help for strong, reasoning-class models, or only for non-reasoning ones?
4. What is the break-even precision for a revise trigger? Tyen says about 60-70% locator accuracy; does that hold for non-BIG-Bench tasks and with a keep-best-so-far rule?
5. Do two same-family reviewers add anything over one (joint miss rate vs product of single miss rates), given correlated errors (Kim 2025)?
6. For slips vs mistakes in LLM output (arithmetic copy errors vs wrong plan), which defence catches which? There is no study that splits LLM errors by Reason's slip/lapse/mistake classes.
7. Does a fixed, tiny checklist run by code beat none? Human evidence is split (Haynes vs Urbach); no LLM test exists.
8. What are Reason's 1979/1990 diary numbers and the CREAM control-mode probability intervals in the sources themselves? Open the books or chapter scans before using them.
9. Does Wait / forced reconsideration keep helping after the first use, or flatten, for the model our agent uses (s1 says gains flatten; Tsui measured open models)?
10. Do agreement signals between samples (K21) detect errors when all samples share the same wrong belief, i.e. correlated-error cases?

## Gap search results
Search tools were rate-limited (WebSearch budget used; OpenAlex, Semantic Scholar and arXiv API returned 429), so sources were opened from known arXiv HTML pages. Fifteen new evidence lines (d23-d37) were added to evidence_d.jsonl; claims K27-K32 were added and K03, K05, K06, K08, K09, K14, K18, K21, K23 extended.

1. Code error line vs resample at equal tokens: PARTLY. Self-Debugging (d36) and Olausson (d32) support execution feedback, and repair at equal samples is near break-even (1.05x and 0.97x), but no one controlled tokens. Open for our own tasks.
2. Claude false-pass rate: OPEN. Only the self-preference abstract was read (d26); no Claude number found.
3. Tsui effect for reasoning models: PARTLY CLOSED. Reasoning models show a small or negative blind spot and Wait on a base model matches them (d25). Claude not tested; the earlier Claude blind-spot figures could not be re-found in v2 and are unverified.
4. Break-even precision: PARTLY CLOSED. 60-70% on BIG-Bench Mistake with per-task deltas (d28). Not tested elsewhere or with keep-best.
5. Two same-family reviewers: OPEN. Weaver (d30) shows diminishing gains with correlated biases; no joint miss rate.
6. Slips vs mistakes in LLM output: OPEN. MR-GSM8K (d29) has no split.
7. Fixed code-run checklist: OPEN. Only LLM-generated checklists tested (d33, d35), with gains over holistic scoring.
8. Reason diary numbers and CREAM intervals: PARTLY. CREAM intervals found only in secondary sources (d23); the arXiv table is an image; Reason's 433/35 not confirmed (replication d24: N=189, mean 6.4). Books not opened; keep both unverified.
9. Wait after first use: MOSTLY CLOSED for open models (d37, d27, s1): gains flatten, then accuracy falls; parallel samples beat repeated Wait. Claude-class only via inverse scaling on distraction tasks.
10. Agreement signals under shared wrong belief: OPEN. Semantic entropy (d34) and the vote plateau (d31) imply agreement cannot detect it; no direct test.
