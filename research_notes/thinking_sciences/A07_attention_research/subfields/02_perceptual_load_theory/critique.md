# A07.02 Perceptual load theory: cross-check critique

Cross-checker pass, 2026-11-01. Files checked: evidence_a.jsonl (34 lines), evidence_b.jsonl (25), evidence_c.jsonl (25). Output: claims.jsonl (29 claims, A07.02-K01 to K29).

## 1. Numbers re-opened and result

Re-checked against full text (PMC text or arXiv PDF) this session.

| Evidence | Number | Result |
|---|---|---|
| a30/b25/c01 Shi 2023 | code-davinci-002 COT micro 72.4, macro 6.0; LTM 77.5/18.0; +INST 77.8; SC 88.1 and 93.4; 99.7% in 20 samples; best macro 45%; at most 18% of solved problems stay solved | Confirmed (Table 3, section 5) |
| a25/b01 Snowden 2025 | Exp 1 distraction 56 vs 67 ms; congruence 197 vs 202; interaction p=.98; Exp 2 58.5 vs 42.4, p=.05 | Confirmed |
| a09 Macdonald and Lavie 2008 | RT 766 vs 593 ms; d' F=15.44 p=.002; beta 5.5 vs 9.0 | Confirmed; RT test is p=.011 (not given before). The F=14.00 in the same paper is a different test (detection rate 37% vs 90%, d' 1.31 vs 3.68). |
| a11 Macdonald and Lavie 2011 | 21/28 vs 7/28; chi2=14.00; 79% deafness | Confirmed (Exp 1, N=56) |
| a13 Lavie et al. 2014 | memory 95% vs 64%, d=1.91; threshold 18% vs 27%, p=.023, d=0.79 | Confirmed |
| a17 Gutteling 2022 | load x salience F=12.9, p=.001, partial eta2=.31 | Confirmed |
| a28 Hung 2020 | 5.36% vs 0.62% slower | Confirmed in text; the same 5.36% also appears in a second experiment (coincidence, not an error). |
| a29 Wiens 2016 | k=6, N=97, -0.46 uV [-0.72, -0.20] | Confirmed |
| c04/c05 Weston 2023 | 62.8 to 80.3; 51.7 to 61.3; keep-original 74.5 | Confirmed |
| a31/c08 Liu 2023 | closed-book 56.1, oracle 88.3, drop over 20 points | Confirmed |
| c07 Cuconasu 2024 | one distractor -0.24 (-25%); -0.38 (-67%) | Confirmed in text; the +0.07 (+35%) for random docs is in the abstract and table, not traced to a specific cell. |
| a07 Forster and Lavie 2009 | TUT 61.6 vs 48.9 (1a), 57.5 vs 44.0 (1b) | Confirmed. |

### Corrections and cautions
1. c01 says "COT macro 8.3 on 2-step vs micro 72.4 overall". In Table 3, 8.3 is 2-step macro; overall macro is 6.0 and >2-step is 2.5. Use 6.0 for overall.
2. a25 and b01 are the SAME paper (Snowden et al. / Snowden and Gray 2025). Counted as one source. Sample sizes: Exp 1 39 recruited, 36 analysed; Exp 5 19 recruited (b01 says 18).
3. a30, b25, c01 are all Shi et al. 2023: one source. a31/c08 (Liu), a32/c06 (Yoran), a27/b09 (de Fockert), a22/b13 (Chen and Cave), a23/b14 (Scalf), a16/b11 (Tan), a19/b06 (Benoni and Tsal), c09/c25 (NoLiMa), a10/b15 (Cartwright-Finch) are also duplicates. Independent-source counts in claims.jsonl use unique papers.
4. a30 says "fewer than 30%" and the paper says both: macro below 30%, and no more than 18% of originally solved problems stay solved. They are different measures.
5. a07: a table row in the paper shows TUTs 41.25% (low) vs 51.90% (high) next to RT 605 vs 793 ms. I could not tell which experiment. The main finding (fewer TUTs at high load) holds in Exp 1a and 1b, but this row suggests a reversal or column mix-up in another experiment. Unresolved.
6. b02 Marciano and Yeshurun 2017 and b01 details beyond Snowden Exp 1-2 were not re-opened (source text not in the cache and the OpenAlex budget was exhausted). Left as the earlier agent wrote them.

## 2. Contradictions between sources
- Classic load effect (a04, a06) vs six null results (a25) and Yeshurun and Marciano (b05). Same task family, different outcomes. Explained, not resolved, by display duration, interleaving and dilution.
- Roper and Vecera (b03) say the effect disappears with response-terminated displays. Forster and Lavie 2008 (a06) found the load effect for response-competing letters at long displays but not for fully irrelevant distractors. Snowden Exp 2 (200 ms) still found no reduction. So "brief displays rescue the effect" is not supported by the strongest replication.
- Weston (c04) finds an ignore-instruction gives no consistent gain; Shi (a30) finds +5.4 micro points. Different models and benchmarks.
- Cuconasu (c07): random documents help; Levy (a33) and NoLiMa (c09): padding hurts. Different tasks (retrieval QA vs fixed-reasoning padding).
- Shin (c15): omission is a threshold, not a gradient; this contradicts a clean Lavie load gradient.
- Load theory predicts harder task means less distraction. Yang (c11) finds the reverse in LLMs. Ertan 2026 (b21) finds a reverse load effect in humans.

## 3. Weak spots
- Founding papers (Lavie and Tsal 1994, Lavie 1995, Lavie and Cox 1997, Cartwright-Finch and Lavie 2007) were never opened; all their numbers are second-hand.
- Support for inattentional blindness comes mostly from one lab; the meta-analyses (b18) and 2026 papers (b19, b20) are abstract-only.
- Human samples are small (N=7 fMRI, N=10-20 many).
- The LLM literature is not framed as load theory. Shi uses 2022 models; none of the LLM studies tests Lavie's manipulation. Shin 2026 is a single-author preprint with disclosed duplicated items.
- Section "LLM" numbers on 2023 models may not hold for current models; Liu's U-shape is said (unverified) to flatten.

## 4. Snippet-only
a03, a04, a05, a10, a15 (numbers), a18 (detection), b15, b16, b18, b19, b20, b24, c23 and the arXiv candidates named in c24 (2603.00270, 2601.11585). Treat as unconfirmed.

## GAPS
1. Does any current model (2025-2026) show a Lavie-style load effect: a planted off-topic distractor intruding LESS when the main task is harder, at equal tokens? Our claims say the reverse so far (K18). This decides whether S1 should expect easy tasks to be more distractible.
2. Does a planted critical or off-topic item get reported less under a harder or narrower main task in current frontier models (Shin-style, with N above 64 per cell and non-LLM judging)?
3. What exactly is the Shin (2026) threshold: does one narrow sub-question or one exclusive instruction suppress reporting, and can a one-line open instruction in S1 remove it at no token cost?
4. Does a hard context-filtering step (S2A, Thread of Thought, Focused CoT) win at EQUAL total tokens against plain, once the extra pass is counted (G7), on current models?
5. Does "ignore irrelevant information" work on current models, and does it depend on distractor similarity (in-topic vs off-topic)?
6. Do results from Liu 2023, Levy 2024 and Cuconasu 2024 (position, padding length, random filler helping) survive on 2025-2026 models and with scaffolded multi-step reasoning?
7. Which findings in the opened Lavie 1995 and Lavie and Tsal 1994 papers carry exact numbers, and do they match the second-hand values (e.g. Cartwright-Finch 10% vs 55% aware)?
8. Which 2020-2026 LLM papers use cognitive-load or attention-capacity framing with a controlled load manipulation (arXiv 2603.00270, 2601.11585 are unopened)?
9. Is the null replication (Snowden 2025) a measurement problem (online, interleaved, one stimulus set) or real, given the reliability concerns (b20, Marciano 2017)? This sets how much weight to give the whole human literature.
10. The unresolved Forster and Lavie 2009 table row (TUT 41.25% vs 51.90%): which experiment, and does the mind-wandering effect reverse there?


## Gap search results

Evidence is in evidence_d.jsonl (d01-d28). claims.jsonl now has 37 claims (K30-K37 are new; K03, K05, K12, K18-K22, K24, K25, K29 were revised). Web search quota was exhausted, so coverage came from direct arXiv PDFs, Europe PMC full text and the DataCite title search. Paywalled papers (Cartwright-Finch and Lavie 2007, Lavie 1995, Lavie and Tsal 1994) could not be opened.

Closed:
- Gap 10 (Forster and Lavie 2009 row): closed. It is Experiment 4 (N=20, flankers added). The text says high load gave 41.25% TUTs and low load 51.90% (t(19)=3.43, p=.003, d=1.57); the table prints the two values in the reverse column order, so the table is mislabelled. The effect does not reverse (d20, K12).
- Gap 8 (which LLM papers use a controlled load manipulation): closed. 2603.00270 is a proactive/retroactive interference study (d18) and 2601.11585 is a context-selection method (d19); neither is a load study. Real controlled manipulations: CogniLoad (d04), ICE (d16), dual-task (d17). None is perceptual load (K29).
- Gap 5 (does "ignore irrelevant information" work): closed for 2023-25 models, open for 2026. It depends on distractor type. Works on generic off-topic trivia (CatAttack 37.5% to 9.9%, small model) and when suspect conditions are named (I3C +11.7). Fails on in-topic or adversarial context (IP lowered accuracy on GPT-3.5; guidance changed seven models by -0.013 to +0.026) (d05, d08, d09, d10; K22).

Partly closed:
- Gap 1 (Lavie-style shield in current models): answered "no evidence of one". CogniLoad, Yang 2025, distractor injection and MedDistractQA all show harm that stays or grows with difficulty; the only reverse pattern (CatAttack easy 5.33x vs hard 1.80x) is a near-zero-baseline artefact. No study uses Lavie's perceptual-load manipulation, and none ran an equal-token easy-vs-hard test with a code-scored planted distractor (d04-d07, d25; K32, K19).
- Gap 2 (planted critical item under harder/narrower task, frontier models): Shin now confirmed on GPT-5, Gemini 2.5 Pro, and Opus 4.8 (robust), but only 24 scenarios per model and LLM judges (d01). Martin and Roger 2026 gives a non-LLM-judged analogue with Opus 4.6, GPT 5.4 and Gemini 3.1 in very long transcripts (d03). The N above 64, non-LLM-judged narrow-task test is still not done.
- Gap 4 (hard context filtering vs plain at equal total tokens): not shown on distracted prompts. Focused CoT is token-negative with equal accuracy on clean problems (d11); 2026 search-agent context management trades more tool calls for accuracy (d12); an oracle filter is free (d13). S2A and Thread of Thought were not rerun on 2026 models.
- Gap 6 (position, padding, random filler on 2025-26 models): position (middle worst) and length effects hold on Opus 4.6, GPT 5.4, Gemini 3.1 and gpt-5.4-mini (d03, d14, d15). Random filler is not harmless there: appended neutral filler was harmless in one 2024 model (d16) but 299K irrelevant characters cut an agent from 8/10 to 3/10 (d15). Scaffolded multi-step reasoning was not tested for position.
- Gap 9 (Snowden null): partly design (interleaved load shrinks the effect about six times in Lavie's own data, d22) and partly unexplained (authors' discussion, d23); reliability is unresolved (d24, abstract only). Treat the human literature as conditional on blocked designs (K34).
- Gap 7 (founding papers): not opened. A same-group adaptation of the cross paradigm gives adult awareness 15/16 vs 2/16 (d21) and the 2008 review says typically 40-50% lower (d22), consistent with 10% vs 55%. Exact 2007 values still unverified (K35).

Still open:
- Gap 3: the Shin threshold is one narrow sub-question (report 1.00 to near 0), with output length 189 vs 1,770 characters. A one-line appended open instruction at no token cost was never tested; the tested fix is a second critic pass (d02). Cheap candidates with some support: reminders under 3% extra tokens and a list-suspicious-items-first step (d03), and a detailed external checklist 10/10 vs 5/10 (d15). Needs a direct test.

Suggested next test for S1: easy vs hard main task x narrow vs narrow-plus-one-open-line x planted critical item at start/middle/end, 65 or more items per cell, code-scored, tokens reported.
