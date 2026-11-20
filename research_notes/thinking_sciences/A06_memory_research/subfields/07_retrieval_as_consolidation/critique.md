# Critique: A06.07 Retrieval as consolidation

Cross-check done 2026-11-19. Evidence files a (33 lines), b (25), c (25) kept as found. 20 claims written to claims.jsonl (K01-K20).

## Numbers re-opened and checked (10 plus extras)
Confirmed exactly against the source text this session:
1. a07 Roediger and Karpicke 2006 Exp 1: 81 vs 75 (5 min, d=0.52), 68 vs 54 (2 d, d=0.95), 56 vs 42 (1 wk, d=0.83), interaction F(2,117)=32.10, partial eta2=.35. Confirmed in PDF. Exp 2 confidence d=0.54 also confirmed.
2. a21 van Kesteren 2013: F(2,66)=5.04, t(22)=2.12 (20 h), 2.55 (48 h). Confirmed.
3. a11 Wing 2013: 0.63 vs 0.51, t(21)=9.25, mean difference 0.12 (SD 0.06). Confirmed.
4. a04 Himmer 2019: hippocampus beta -0.864, R2=.748; F(1,29)=6.680, P=0.015. Confirmed.
5. a05 Ferreira 2018: mPFC retrieval slope t(19)=3.66; hippocampus within-session difference is t(19)=-1.69, p=.107 (the evidence line dropped the minus sign; no change in meaning).
6. b01 Abel 2019: 70.6 vs 48.8 (d=0.78), 65.1 vs 45.8, 54.6 vs 51.2, F(1,70)=29.81. Confirmed.
7. b19 An 2025: 89% vs 73%, about 60 students. Confirmed on the arXiv abstract page.
8. b20 Panthi 2026: 210 of 381 pairs, 11 models, GLM-5.2 64% vs 40%. Confirmed on the abstract page (arXiv 2609.36457 does exist).
9. c05 Lin 2025: abstract says 66% SimpleQA (+313%) and 26% FinanceBench (+160%); matches 66.25 and 26.83.
10. c07 Sleep-time compute: about 5x, +13%, +18%, 2.5x. Confirmed on the abstract page.
11. c08 SEAL: 32.7 base, 33.5 passage, 39.7 base-model implications, 46.3 GPT-4.1, 47.0 SEAL, 58.2 (n=200), 72.5 vs 20 vs 0 ARC. Confirmed in the PDF.
12. b21, b22, b23 headline claims confirmed in abstracts (b23: 1,935 matched questions total, 1,501 in the primary aggregate).

## Corrections made
- c01 (Jiang 2024) was wrong in two places. The abstract and text say PIT lifts accuracy by 17.8 points on Llama-2 7B (30.3 to 48.1) and by 16.3 points on 70B (46.4 to 62.7). The evidence line gave 17.8 for 70B and listed "45.4/62.7" as PIT; 45.4 is a 3-epoch 7B ablation cell, and the 7B headline is 48.1. Treat the 70B gain as 16.3.
- c09 (SEAL "49.3"): in the PDF the 49.3 sits in a prompt-format table with several columns (49.3, 43.7, 47.0, 46.3). It is a different prompt variant, not a baseline for the main table. Still unverified; do not cite.
- b24 and c21 disagree about the search state (b24: about eleven arXiv queries ran; c21: all search APIs returned 429). Treated as one limited, rate-limited search. Absence of LLM replications is a weak negative.

## Contradictions between sources
- Fast-consolidation core prediction: Himmer 2019 saw a hippocampal fall inside one session; Ferreira 2018 did not (fall only across 2 days). Different tasks (word lists with free recall vs scenes/objects with cued retrieval), so not a clean conflict.
- Prior knowledge: Ferreira and Wimber 2023 say meaning matters for the testing benefit; Gupta 2021 says prior study depth does not. They test different things (semantic vs episodic prior learning).
- Suppression: Wimber 2015 found competitor suppression after retrieval; Ye 2020 found old memory not suppressed (only intrusions reduced).
- Reconsolidation: Parks 2022 and Scully meta-analysis support the intrusion effect; Hardwicke 2016 and Levy 2018 fail on other versions; Potts and Shanks 2012 find reminders help rather than hurt.
- Sleep and testing effect: Bauml 2014 and Abel 2019 are the same lab. Ashton 2022 is an independent group but a different paradigm; the independence count for K06 is therefore 3, not more.

## Duplicates (not independent)
a22 = b17 (Rowland 2014); a29 = b09 (Hardwicke 2016); a26 = b25 (Bauml 2014); a01 = b12 (Antony 2017); a13 = b13 (Ye 2020); b01-b03 are one paper; c01/c02 one paper; c05/c06 one paper; c10-c12 one paper; c14/c24 one paper.

## Weak spots
- The founding claim (Antony 2017) is a TICS Forum piece with no data. Its predictions have had one direct test (Ferreira 2018 preprint; published status not checked) with mixed results.
- Many human lines are abstract-only (a15-a20, a22-a33, b08, b15, b17): no effect sizes were read. Tse 2007/2011, Sharon 2011, Lehmann 2009 are cited from abstracts.
- b05 numbers come from a model fit in Liu 2024, not from the human study itself.
- LLM memory papers (MemoryBank, Mem0, A-MEM, Generative Agents) use authors' own baselines and LLM judges. No ablation isolates the "recall strengthens memory" rule (c13).
- The LLM weight-training papers (c01-c08) change weights; our agent is a scaffold with no training. Transfer to a prompt-level scaffold is untested.
- b19 is non-randomised (same students, different weeks, different n: 31 vs 27) and may confound week difficulty.
- b18 (EEG, N=30) is a single 2026 study.
- Snippet-only: the Chinese Advances in Psychological Science 2024 article named in the brief was not found or read.

## GAPS (most decision-relevant first)
1. Does retrieval-before-reread (the agent must answer from memory, then check against notes) beat plain rereading at equal tokens on a delayed fact benchmark? No LLM study found; this is the direct test.
2. Does a question-first self-study step (agent writes questions about new material before storing it), the prompt-level cousin of PIT and Active Reading, raise later recall without weight updates?
3. Does keeping the user's original wording next to a consolidated note remove the temporal-flattening and hedge-to-fact errors (b20, b21), and at what token cost?
4. Does retrieval-induced forgetting appear in LLM agents (retrieving fact A lowers recall of related B in context or in a note store)? No result found.
5. How large is the testing effect in the Rowland 2014 meta-analysis (exact g) and does it shrink for schema-poor material? Only the abstract was read.
6. Did Ferreira 2018 get published, and with the same hippocampal result? Are there other direct tests of the Antony 2017 predictions (vmPFC up, hippocampus down) since 2023?
7. Which of Tse 2007 numbers (days to schema, retention) can be read in full, to size the schema-consistent fast-integration claim?
8. Does the Chinese Advances in Psychological Science 2024 review add schema-consistency data not in the English sources?
9. Does linking on write (A-MEM style) cause drift or overwriting of true detail? Authors did not measure it (c17).
10. What does sleep-time compute gain when the stored context changes between rounds (c25 says unhandled)?

## Gap search results (2026-11-19)
Evidence in evidence_d.jsonl (d01-d19). Claims K01, K03, K05 extended; K21-K26 added (26 claims). Tool limits: arXiv, Semantic Scholar and OpenAlex returned 429 on most calls and WebSearch was exhausted; Europe PMC worked. All "no LLM study" findings are weak negatives.

1. Retrieval-before-reread at equal tokens: OPEN. No LLM study found (d11). Run it ourselves.
2. Question-first self-study without weight updates: OPEN. None found (d12).
3. Original wording kept beside consolidated note: OPEN, no test found (d13). New support: a 2026 Nature Communications model shows consolidation by rewriting drifts recalled stories toward prior knowledge (d08, Mistral 7B).
4. Retrieval-induced forgetting in LLM agents: OPEN. None found (d14).
5. Rowland 2014 g and schema-poor material: PARTLY CLOSED. Rowland's own paper was not opened. Gupta, Pan and Rickard 2026 (opened) quote Rowland: g = 0.66 related vs 0.67 unrelated. Their own N=231 experiment found the benefit 26% smaller for highly related pairs (d03, d04). Mixed; overall g still unread.
6. Ferreira 2018 published: CLOSED. Published as NeuroImage 2019; mPFC rise and gist gain across retrieval, slow (two days), episode detail also strengthened (d01, abstract only). No other direct test of the hippocampus-falls prediction found; a 2026 Current Biology study shows mPFC abstraction across days (d10).
7. Tse 2007 numbers: OPEN. Only the abstract was reachable (d05).
8. Chinese 2024 review: OPEN, low priority (d15).
9. Link-on-write drift: OPEN, but d08 raises its priority (d17).
10. Sleep-time compute with changing context: OPEN (d16).

New boundary evidence: two 2026 Prolific experiments (N=67 and N=129, high attrition) found no testing effect (d06, d07; full text read). Treat as noisy small studies, not a refutation of the large effects in K01.
