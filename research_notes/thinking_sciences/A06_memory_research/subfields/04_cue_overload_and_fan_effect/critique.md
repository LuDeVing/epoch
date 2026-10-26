# Critique: cue overload and fan effect (A06.04)

Cross-check of evidence_a, evidence_b, evidence_c. Sources re-opened this session (text extracted from PDF or HTML): Guo et al. 2606.28327, Cao et al. 2509.17138, Wang and Sun 2506.08184, Chattaraj and Raj 2603.00270, Cuconasu et al. 2401.14887, RAG-MCP 2505.03275, NoLiMa 2502.05167, Sohn et al. 2004, Radvansky and Zacks 2005 (PMC1751467), Schneider and Anderson 2012 (PMC3259266), Anderson 1983, Ding et al. CMI 2608.07622, Jiang et al. SYNAPSE, Li et al. Sculptor. Claims are in claims.jsonl (K01 to K26).

## Numbers re-checked (10 most important)

1. Guo et al.: human 91.2 / 82.4 / 71.8 percent at fan 1, 2, 4; DPR 94.1 / 76.3 / 58.2 / 44.7; slopes 0.41, 0.67, 0.53, 0.44; BIC 18.4 / 23.1 / 15.7; false alarms 23.1 vs 41.3 percent. All confirmed.
2. Cao, Schooler, Zafarani: accuracy 0.991 to 0.915 "when the list size is 32"; d-prime about 4.1 (fan 1) and 3.1 (fan 2) for the online model; human 3.7 and 2.5 are the paper's description of Schneider and Anderson, not a table from the original. Confirmed, with the caveat that the human values are second-hand.
3. Wang and Sun: size class t=3.03, p=.005, N=30; context length p=.886; combined R2 .261; Spearman .673 in the 128-131k group. Confirmed.
4. Chattaraj and Raj: d=1.73, mean gap 69.5 points, 39 models, R2 .49 (RI) vs .06 (PI, p=.14), hallucination 0.9 percent (RI) vs 0.2 percent (PI), 8.6 percent refusals in PI failures. All confirmed.
5. Cuconasu et al.: gold-only 0.5642; 1 distractor far 0.4733; 8 distractors far 0.3106; ADORE 0.4068 / 0.3815 / 0.3626; up to -0.38 (-67 percent). Confirmed.
6. RAG-MCP: 43.13 / 18.20 / 13.62 percent. Confirmed. The 18.20 arm is "Actual Match", a keyword prefilter, as stated in a26.
7. Sohn et al.: slopes 98 vs 63 ms (t(18)=2.59) and 118 vs 73 ms (t(16)=2.80); N=19 and 17; F(2,68)=56.80 and 30.91. Confirmed.
8. Radvansky and Zacks 2005 Table 1: all RT and error cells confirmed (young multiple-location 1441, 1615, 1853; old 1833, 1975, 3209 with 18.5 percent errors). The RT interaction F(2,124)=22.5; the error-rate interaction is F(2,124)=10.1.
9. Schneider and Anderson 2012: 10 subjects, 5 sessions, 32 facts (24 persons, 24 locations). Confirmed. Anderson 1983: 600 presentations per sentence, T = 0.36 + 1.15 P^-0.51. Confirmed.
10. CMI (Ding et al.): at count 8 the contrasts against unrelated are -0.32 [-0.46, -0.20] and -0.48 [-0.62, -0.34]; dense repeated-history recall 0.48. Confirmed. NoLiMa: 11 of 13 models fall below 50 percent at 32K; GPT-4o 99.3 to 69.7. Confirmed. SYNAPSE +7.2 over A-Mem (33.3) and Sculptor +5.90 / +6.58 confirmed in text.

## Corrections made

- c02 names the authors "Huang et al.". The paper is Cao, Schooler and Zafarani (2025). Same study as a21, a22, b10, b11, c22: count them as ONE independent source, not three.
- c17 says "10 of 12 models below 50 percent at 32K". The paper says 11 of 13 (b18 is right).
- c07 and c20 list the 18-distractor result as near / mid / far = 0.37 / 0.23 / 0.17. The table gives far 0.2348, mid 0.1795, near 0.3781. So mid is 0.18 and far is 0.23; the order in c07 is wrong. b16 had the order right.
- b16 puts the 18-distractor numbers in the "random documents" entry. They belong to the distractor table. Random-document results are in Table 2: the 0.5681 at 6 random (near) carries an asterisk (not significant); 0.5859 at 14 is significant, about +0.02 over 0.5642. c07's "+0.08 (+36 percent) for one model" was not re-verified.
- c14 says dense same-slot conflict cuts stability "0.92 to 0.54". In the text the 0.54 is dense same-slot Target Recall@3, not stability. Treat the stability figure as unverified.
- c06 notes a mismatch between the arXiv number (2606) and the date (9 May 2026). Confirmed: the header reads "arXiv:2606.28327v1 [cs.IR] 9 May 2026". Provenance is odd; the paper also has a thin human sample (online, 3 fan levels, fan 8 missing). Kept at single-source for the log form (K02).
- a27 says "9 to 18 points per doubling". Human drops are 8.8 then 10.6 points; DPR drops are 17.8, 18.1, 13.5. So "9 to 18" holds only at low fan.
- a21 and a22 say Cao et al. test "seven phenomena over two datasets". The fan test is only fan 1 vs fan 2, one list size. Fan slope for LLM generators in context is NOT measured beyond fan 2.
- Cuconasu, Wang and Sun, RAG-MCP, Guo, Cao are arXiv preprints or workshop papers (Cuconasu is SIGIR 2024). Nothing here was peer reviewed except the human cognition papers and SIGIR.

## Contradictions between sources

- Size vs PI: Wang and Sun say size predicts resistance. Chattaraj and Raj say it does not for PI (R2 .06) but does for retroactive (R2 .49). Chattaraj blames MoE parameter counts. Unresolved (K17).
- Hallucination share: Wang and Sun describe a third stage of never-seen values; Chattaraj measures 0.2 percent. Different definitions.
- Prompt fixes: Wang and Sun find marginal gains; Qiao finds memory integration and 2-shot help most but at single-digit to low-teens points; index numbering hurt (LLaMA3.1-70B fell to 38.33 percent; figure from c10, not re-verified). Consistent in direction: none removes the bias.
- Unrelated load: Cuconasu (random passages near the query help) and CMI (lexical unrelated -0.02) say it is cheap. CMI dense unrelated -0.18 and NoLiMa (length alone cuts accuracy) say it is not (K09).
- Mental models vs ACT-R: Radvansky shows no fan for integrated facts; Sohn shows the focused dimension has the bigger fan; Reder says the size is process, not representation. The human literature is not settled (K13, K14).
- Humans plateau at high interference, LLMs keep falling (Wang and Sun, citing Oberauer and Vockenberg). Chattaraj also finds the reverse of the human PI/RI pattern. Human PI data come from other tasks, so this is not a like-for-like comparison.

## Weak spots

- Founding sources were not read: Watkins and Watkins 1975, Anderson 1974, Anderson and Reder 1999 (image scan). Everything on them is second-hand. The a01 entry carries no numbers.
- The foundation for "log of fan" in LLMs rests on one preprint on retrievers (not LLM readers).
- LLM fan studies use tiny fans (1 or 2). The decision-relevant range for a library (5 to 50 notes per cue) has no human or LLM fan data except PI-LLM (key overwrite), which is a different structure (same key, replaced value).
- Nearly all LLM tests are synthetic (random words, key-value). The one natural-text test (Cuconasu) uses 2023-era small models. No modern-model fan-slope data in natural text.
- RAG-MCP: one model, 20 trials, tool selection not fact retrieval.
- Sculptor, SYNAPSE, MINTEval, Causal-LoCoMo are proposals or benchmarks with their own baselines and mostly one backbone.
- Item-based tests (hit rate) are mixed in humans; the claims must be read for false accepts, not for misses (K10).

## Only seen in snippets or abstracts (not read in full)

Watkins and Watkins 1975, Anderson 1974, Anderson and Reder 1999, Cantor and Engle 1993, Bunting et al. 2004, Radvansky 1999 and the 2002 Chinese replication (b26, snippet), Reder "size of the fan effect" (403), Tehan and Humphreys 1996 (abstract), Verde 2004 (abstract), Link et al. 2025 (poster abstract), Wickelgren and Corbett 1977, Dosher 1981, Surprenant and Neath 2009. Sculptor, SYNAPSE, MINTEval, DKI (Qiao), SleepGate, Causal-LoCoMo were checked only in part by this cross-check (the headline numbers for Sculptor, SYNAPSE and CMI were confirmed; others rest on the finders' reading).

## GAPS (most decision-relevant first)

1. What is the fan slope of a current frontier model in natural text, for 1 to 50 notes per cue, with retrieval from a compact in-context library (not key overwrite)? Existing data stop at fan 2 (recognition) or at synthetic key-value updates.
2. Does a code-side supersede or merge rule (one live value per cue) beat an append-only library at equal tokens in a real agent loop, including setup cost (G7)? Only synthetic tests exist.
3. Does grouping notes under sub-cues or integrated case notes cut the fan cost in LLMs, as integration does in people? No LLM test of the integration boundary exists; the human side is contested.
4. How steep is the quality loss when top-k is increased from 1 to 20 for the same cue, with near-duplicates removed vs left in, on modern models? Cuconasu is 2023-era and small; RAG-MCP is one model.
5. Does cue weighting (making one cue more salient) help or hurt LLM retrieval, as in the Sohn differential-fan result? No LLM test.
6. Does practice or repeated successful use of a note reduce its crowding cost in an agent (the Anderson 600-trial result), or only add noise? The only LLM check found no list-strength effect on tiny lists.
7. Can token probability of the retrieved answer be used by code as a cheap trigger for a second lookup, given that models rarely refuse (8.6 percent) and fan shows in probabilities for only some models?
8. Does quantization, model size or reasoning mode change the PI slope for the model we deploy (Wang vs Chattaraj conflict)?
9. What are the original numbers for Watkins and Watkins 1975 and Anderson 1974 (exact recall and RT cells), which this series still lacks?
10. Is the Guo et al. log-fan result reproducible, given its odd provenance (arXiv id vs date) and small human sample? An independent human or LLM-reader replication at fan 1 to 16 would fix K02.

## Gap search results

Searched 2026-10-26/27. Evidence is in `evidence_d.jsonl` (d01 to d24; 20 opened, 4 not opened). New claims K27 to K34 in `claims.jsonl`. The web search quota ran out partway, so some leads (access-count strengthening, salience) got no second search.

Status by gap:

1. Frontier fan slope in natural text, 1 to 50 notes per cue: STILL OPEN. The nearest design is OpenAI MRCR (2, 4, 8 identical requests; d17), but the dataset card has no per-needle accuracy and the only numbers I found are aggregator copies (d18, d19: 8-needle Gemini 26.3 to 54 percent, 2-needle at 128K from 36.6 to 95.2 percent by model; d19 not opened). Michelangelo MRCR has only 2 confounders (d20). Indirect: first 10 percent of hard distractors caused 58 percent of the loss for a 7B model (d14, K02 note); best models keep gains to 100k tokens (d13). Run the sweep ourselves.
2. Code-side replace vs append-only at equal tokens: STILL OPEN, now K31 (contested). Better cases for write-time handling (Zep 44.4 vs long context 20.0 EM; d10). Counter-signals: a model-written bounded memory lost 15 points to full history (d01, d02), and a vendor moved to add-only (d24, not opened). A code rule is exact only for canonical cues (5 percent on obfuscated ids, d09; K30). No test counts setup cost (G7).
3. Grouping or integrated case notes in LLMs: PARTLY ANSWERED, K29 (single-source). xMemory group routing beat flat top-20 with fewer tokens, and a cap of 12 (about 4.5 average) beat 8, 10 and 14 (d05, d06). Pipeline confounded; group selection alone was flat on F1. The integration boundary (single-location vs multi-location facts) has no LLM test.
4. Top-k 1 to 20, near-duplicates in vs out, modern models: PARTLY ANSWERED, K27 and K28. Best k depends on the reader (k below 5 vs about 10 vs 100k tokens; d11, d12, d13). Dedupe hurts on clean pools and helps only when the pool is redundant and the task is multi-evidence (d03, d04). Still no 2026 frontier model sweep; readers there are 2023 to 2024 models or small.
5. Cue weighting or salience: STILL OPEN. No LLM study found. Nearest: attention on gold collapses under hard distractors (d14) and prompt repetition helps non-reasoning models (d21, K34). Neither tests a differential-fan design.
6. Practice or repeated use of a note: STILL OPEN. No LLM test found. K34 is only a hint from prompt repetition.
7. Token probability as a trigger for a second lookup: PARTLY ANSWERED, K32 (single-source). Entropy gating worked on open 8B readers and cut tokens (d07, d08). Closed models need a proxy. Not tested on crowded cues. Refusal stays rare (0.035 percent of 194,480 calls, d15), which confirms K22.
8. Quantization, size, reasoning mode and the PI slope: PARTLY ANSWERED, K33. Existing data (c08) already show reasoning helps retroactive but o1 ranked 35 of 39 on proactive; Supersede shows a low-reasoning frontier model still loses on model-written notes (d01). The size dispute (K17) and quantization (K23) are unchanged. No direct sweep on the deployed model.
9. Original cells for Watkins and Watkins 1975 and Anderson 1974: STILL OPEN. UMich copy blocked by a Cloudflare check, Elsevier and APA behind paywalls (d22, d23, not opened). Do not quote cells.
10. Replication of Guo et al. log-fan result: STILL OPEN. I found no independent replication. The only new indirect support is the convex curve in d14, which is a different task (K02 stays single-source).

Status changes: no claim was refuted. K02 gains an indirect line (d14) but stays single-source. K22 now has 3 sources. K31 is new and contested. K27 is established (three independent sources), but all on 2023 to 2024 models, so it says "tune k per reader", not "use k=N".

Caveats about this pass: d19 and d24 and the Anderson and Watkins lines were not opened. Chroma (d15) and Du et al. (d16) were read at report and abstract level without per-model tables. The Brouillette, xMemory, Supersede, FORGETEVAL and First-Drop papers are 2026 preprints or workshop-stage and have not been replicated.
