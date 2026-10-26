# D04.02 Argument schemes and critical questions: cross-check

Files checked: evidence_a.jsonl (27 lines), evidence_b.jsonl (25), evidence_c.jsonl (32). Claims: claims.jsonl (K01-K21).
Method: re-opened 10 arXiv/ACL PDFs this session and compared the numbers (pdftotext). PDFs were deleted afterwards.

## Numbers re-opened

Confirmed as recorded:
- ArgMed-Agents Table I (2403.06294): GPT-3.5 52.7/48.0/62.1 MedQA, 68.4/71.5/78.3 PubMedQA; GPT-4 67.8/71.4/83.3 and 72.9/77.2/81.6.
- CQoT (2412.15177): Table 1 and 2 values (Llama 8.05/8.3/8.4 and 8.95/9.25/9.55; Nemotron 6.75/6.85/7.3), pass thresholds 7/8 then 5/8, +4.61% and +5.4%.
- ELLIS Alicante (2506.14371): judge +3.4 points over random (p<0.05, McNemar), oracle +34.2; table 57.7/56.5/51.6/62.4 with judge; best score 67.6 after organiser labelling; test split is small.
- Ruiz-Dolz & Lawrence (2503.14626): RoBERTa 99.2 F1 on textbook text; QT30 31.7 and 44.8; 3,566 of 4,000 (89.1%); 53.3% yes on negative CQs for the generative model.
- Singh et al. (2609.18644): 16.6 vs 58.9, 5.7 vs 62.0, 85.9%, judge precision 93.1% (67 of 72), 56.6% (30 of 53, CI 43.4-69.8).
- Henselmans et al. (2609.05088): 18.2% failures, 67.8% from two models, 89.6% judge agreement (3,389 paired cells), 6,778 cells, VBPR about 72%/67%.
- Bezou-Vrakatseli et al. (ACL Findings 2025): best EthiX F1 0.65 (Claude 3.5, few-shot with descriptions), 686 arguments; CoT effects and Llama 0.47 to 0.79 stated in text.
- DeceptionAnalyser (2609.24369): 100/0/0 and stability 1.00 for the fable; 800 assessments.

Corrections and flags:
1. Benchmark scores (Calvo Figueras & Agerri 2025, 2505.11341). Evidence lines c02 and b01 give claude-3.5-sonnet 56.65, o4-mini 54.14, gpt-4o 53.70. In the version I opened (Table 3) claude-3.5-sonnet averages 56.32 (56.21 on one column), gpt-4o 54.47, o4-mini 54.14. The ordering and the "no model above about 56-57" statement hold; the third decimal differs by version. Use "about 56" and cite the version.
2. Henselmans (a21): "51.1% global sufficiency" for Claude Sonnet 4.6 is the table column "Fail (global)", i.e. a failure rate on global checks, not a score. Read it as a failure share. The text pairs it with "22.5% local grounds".
3. ELLIS candidate count (c15): the line says 4+4 candidates was best yet lists 6 candidates 59.3 above 8 candidates 57.2. The paper says differences are within noise. Treat the candidate number as unsettled.
4. ELLIS scheme ablation: a17 gives questioner-only numbers (54.7, 53.4, 46.0, 54.0) and c13 gives with-judge numbers (57.7, 56.5, 51.6, 62.4). Both are right but are different conditions; the "mixed prompts help" result is only the with-judge number, on a 79-item test split with 27-34% of questions not evaluable. This is weak.
5. Benchmark "useful" is matched to annotator reference questions, so a valid new question counts as a miss. Scores are lower bounds on real quality (the 2024 paper found 155 valid LLM-only questions).

## Contradictions between sources
- Scheme information in prompts: Alicante (mixed prompts help), DayDreamer (plain baseline best on percent Useful, scheme steps cut Unhelpful/Invalid), ARG2ST (no gain), shared-task overview (helps usefulness, lowers diversity). Status: contested (K04).
- Expert opinion: Mizrahi says weak; Walton, Seidel, Hinton say it depends on the full scheme (K18). A decisive empirical test was not found.
- Henselmans says models defend reasoning slightly better than justification, but the gap is 0.02-0.04 normalised; read as small, not a finding that reasoning text is trustworthy (G10 stays).

## Weak spots
- Almost all LLM-CQ evidence comes from one group (Calvo Figueras, Agerri) and the one shared task they ran. Independence is lower than the count of papers suggests.
- Pipeline gains (ArgMed, CQoT) come from direct and CoT baselines, not token-matched best-of-N, and use GPT-3.5/GPT-4-era or mid-2024 models. ArgMed is 300 items per set, no intervals. CQoT scores come from a GPT-4o judge on MT-Bench (1-10).
- No study tests whether scheme-specific CQs beat generic CQs at equal tokens on answer accuracy. CQoT used generic CQs; ArgMed used domain schemes; nothing compares them.
- Henselmans: two models carry two thirds of the failures, so the "LLMs fail 18%" figure is not a model-general rate. Judges are LLMs.
- Singh: negatives are constructed; authors say rates are not deployment estimates.
- Human-subject work (Hoeken 2001, Hornikx 2008, Schellens 2017) is old, narrow (Dutch samples, one claim) and not about accuracy gains.

## Seen only in snippets or abstracts (not read in full)
a04 Mizrahi 2013 (via Makula), a06 Lumer 2022 (bot check), a08 Oaksford & Hahn 2004 (via 2006), a11 Harris et al. 2016 (403), a07 Nussbaum et al. 2018 (abstract), b19 Hoeken 2001 (abstract), b25 and c23 Pan et al. (abstract and partial table; I could not re-fetch it), a25, a26, a27 and c32 (the Walton 2008 book itself), c30 Betz et al., c31 Jo et al. (abstracts), b23 TRACE (design only). Hahn & Oaksford 2006 statistics (N=73, F values) and Schellens counts were not re-opened; they stand as recorded.

## GAPS (most decision-relevant first)
1. Does a scheme-specific CQ list beat a generic objection list (and a plain "check this" prompt) on answer accuracy at equal tokens? No paper isolates this; CQoT is generic and ArgMed is scheme-specific.
2. Does a CQ-test step beat best-of-N / self-consistency at the same token budget? ArgMed and CQoT never ran that comparison.
3. Which CQs can be answered by code (search the source, check a quoted passage, recompute a number) rather than by the model, and how much does this close the 34-point oracle gap that the LLM judge leaves?
4. How well can a cheap router (keywords, a small classifier, or the generic CQ list) pick the scheme on real, incomplete arguments? LLM F1 is 0.65 at best and classifiers collapse on dialogue; is the generic list good enough without routing?
5. Do CQ-based checks have a yes-bias that makes them pass flawed arguments (GPT-4 said yes to 53.3% of negative CQs)? What forced-choice or quote-required format removes it, measured on seeded-wrong arguments?
6. Are frontier 2026 models still as poor at CQ generation as the 2025 benchmark (best about 56)? Newer reasoning models were not tested.
7. Is there a model-size threshold for CQ pipelines (CQoT suspects about 70B)? Results below 70B and with small open models are untested.
8. Which of the 60 schemes matter for our tasks (ARC, BrainTeaser, novelty)? Authority, analogy and cause are the focus but analogy CQs (a27) and cause CQs were never opened in the book.
9. Does the scheme-matched false-positive problem (58.9%) also affect an LLM acting as CQ judge, or only fine-tuned classifiers?
10. Is the Walton 2008 text itself (CQ wording per scheme, especially expert opinion, analogy, cause to effect) available in a form we can code, and do its templates need the 39% hand-editing found by Calvo Figueras?

## Gap search results

Files: evidence_d.jsonl (d01-d22), claims K22-K29 added, K04, K07, K10 and K12 extended. Search note: the web search quota ran out early, and the arXiv, Semantic Scholar and OpenAlex APIs were rate-limited, so papers were found through the Hugging Face paper index, the ACL Anthology ArgMining 2025 volume, and known arXiv ids. A 2026 literature sweep for new CQ papers could not be done.

| Gap | Status | What the new evidence says |
|---|---|---|
| 1 Scheme CQs vs generic list vs plain "check this" at equal tokens | Open (partly informed) | Still no paper isolates it on answer accuracy. On question quality, scheme text in the prompt gave no consistent gain (COGNAC 0.83 vs 0.81 and 0.79 vs 0.82; ARG2ST: scheme labels worst; Webis dropped them). PCBench shows an explicit "check for errors" instruction lifts flaw detection a lot (GPT-4o 11.0% unprompted; assisted rates 60-78%), so the plain check prompt is a real arm, not a null arm (d09, d13, d14, d15). |
| 2 CQ test step vs best-of-N at equal budget | Closed for the generic case, open for CQs | Model-run critique or verification loses to majority voting at equal calls unless the budget is large: SC 82.5/85.3/88.2 at 3/6/9 responses beat debate (d01); a generative verifier needs about 8x compute to match SC and 128x for +3.8 points (d07); sampling plus a sound verifier matched critique (d02). Nobody ran a CQ step in that comparison. We must run it (K23). |
| 3 Which CQs code can answer; closing the 34-point oracle gap | Partly closed on principle, open on numbers | Tool or code checks give the gain and model self-critique gives about nothing (CRITIC: own critique -0.03 and +2.33 F1; Stechly: sound verifier 8-87% vs LLM critic 0-55% accuracy) (d02, d03). A trained small reranker lifted Webis from 0.49 to 0.57 while LLM judges did not (d10, d15). Nobody measured how much of the 34.2-point oracle gap a code selector closes. |
| 4 Cheap router on incomplete real arguments | Open | No new router results. ARG2ST found that giving the gold scheme label did not help generation, which suggests routing matters less for generation than for per-scheme checks (d14). Scheme frequencies in real debates are dominated by example, practical reasoning, cause and consequences (d17). A generic list as default is untested. |
| 5 Yes-bias and a format that removes it | Partly closed | Yes-bias in an LLM usefulness judge is confirmed (8.4 of 10 accepted, 44.4% really useful; debate and deliberation did not fix it) (d10). Open fact-style questions in a fresh context beat yes/no restatements (d06). Judges are near chance at absence and fine at presence, and a closed list-then-verify format recovered detection (d20). Model-level compliance with invalid arguments ranges from 0.2% to 95% (d19). No study ran quote-required vs forced-choice on seeded-wrong arguments; we must. |
| 6 2026 frontier models on CQ writing | Open | Leaderboard scores are in a private dataset; no new numbers found (d22). The "about 56" ceiling is unconfirmed for 2026 models. |
| 7 Size threshold | Closed in part, answer "no clean 70B cliff" | Writing CQs: 8B to 405B gave +1.3 points and 24B matched 70B (d10, d11). Judging: small and medium models are near chance on critique (CriticBench), 13B self-verifiers are weak (d05, d08), but open models were within 10% of frontier on proof checking with more inconsistency (d21). Treat judge reliability, not parameter count, as the test. |
| 8 Which schemes matter for ARC, BrainTeaser, novelty | Open | Debate-data counts exist (d17) but do not cover our tasks. We need to count scheme types in our own agent traces. Analogy and cause lists from the book remain unopened. |
| 9 Scheme-matched false positives in an LLM judge | Partly closed | The yes-bias seen in LLM usefulness judges (d10) and sycophancy to invalid arguments (d19) are the same family of error. The 58.9% figure for fine-tuned classifiers has not been measured for an LLM CQ judge on scheme-matched wrong arguments. |
| 10 Can Walton wording be coded; 39.44% hand edit | Partly closed | The six expert-opinion questions are available and codable (d18, secondary). Short analogy and cause templates come from the ELLIS appendix (d16), not from the book. The 39.44% edit rate still applies to slot-filled templates, so code the slots and have the model reword. |

### New corrections and cautions
- The Webis paper's text says scheme-aware prompting scored lower, but its table shows 0.72 on validation for both. Counted as no gain.
- Several "2026" sources (SycoBench, omission blindness, proof verification) use models and numbers I could not cross-check elsewhere. Each is single-source.
- d18 was read through a summariser tool and is secondary.
- Several tables (Huang, Stechly, Tyen, Zhang) extracted with scrambled columns; only numbers that could be matched to captions or text are used.

### Gaps still open after this pass
Gap 1 (equal-token scheme vs generic vs plain), gap 4 (router), gap 6 (2026 models), gap 8 (our task schemes), and the oracle-gap number in gap 3. All five need our own experiments, not more reading.
