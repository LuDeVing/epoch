# Critique and cross-check, E10.03 Anomaly handling and fixation

## Numbers re-opened this session (confirmed)
1. Huang 2024 (arXiv 2310.01798), tables read: GPT-3.5 GSM8K 75.9 -> 75.1 -> 74.7; CSQA 75.8 -> 38.1 -> 41.8; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; CSQA 82.0 -> 79.5 -> 80.0; HotpotQA 49.0 -> 49.0 -> 43.0. Confirmed. Note the table labels rounds as 1/3/5 (calls), not "round 1/2".
2. Laban 2025 (2505.06120): -39%, aptitude -15%, unreliability +112%, SNOWBALL 15-20%, code 850 vs 668 chars (+27%), SQL 129 vs 113 (+14%). Confirmed.
3. Xie 2024 (2305.13300): "GPT-4 shows an 80% memorization ratio for the most popular questions". Confirmed; order sensitivity above 30% for PaLM2 and Llama2-7B in text.
4. ClashEval (2404.10198): over 60% override; Claude Opus 74.3% accuracy, 15.7% context bias, 2.1% prior bias. Confirmed.
5. Tsui 2025 (2507.02778): blind spot 64.5%, "Wait" -89.3%, accuracy +156%, correction markers +179.5% / +73.6%. Confirmed.
6. Handler 2026 (arXiv 2605.15000): false action 55-81% (MedQA) and 53-82% (AfriMed); mean about 70%; safety prompt about 70% -> 48%; 30% of 861 HealthBench and 78% of 191 adversarial. Confirmed. CORRECTION: c02 reports underspecified low-risk 81% vs urgent 19% (not re-read, text lines 268 seen only); and c01 "Claude Opus 4.7 81%" matches the range top.
7. Zhao 2026 (2508.15754): harmful flip 15.2% for Qwen3-Coder-30B and crossing 15.33% vs shuffle 6.1-10.19%. Confirmed in text. The 0.5% figure was not re-seen.
8. Braitsch 2026 (2607.10275, abstract only): 32 models, best 68%, R=0.69, utilization 57% -> 26%, 91% traces above threshold. Confirmed from abstract. The 65.6% persistence (212/323) and 50.8% worsening (156/307) were NOT re-checked (PDF unreadable here).
9. Shidara 2026 (2601.11866, abstract only): top 5 models 55-70% on items most missed by physicians. Confirmed. The 0.751 mean, CI and physician 0.66 are NOT re-verified; the abstract has no CI.
10. Not re-opened (access): Chan 2017 d values, Wood and Porter N>10,100, Fugelsang stats, Trickett counts, Kan 2021. Evidence lines say opened:true; I trust them but did not recheck.

## Corrections and duplications
- Many lines are the same paper counted several times: Huang (a08, b17, b18, c22), Laban (a09, b19-b21, c13, c14), Xie (a06, b15, b16, c26), Kim Einstellung (b23, c20), Kenaston (b24, c10), Xu survey (b25, c27). Counted as ONE source each in claims. Raw line count overstates support.
- b22 (Samadarshi 2024) and c19 (Alavi Naeini 2023) are different papers on the Only Connect wall; b22 cites human about 80% on connection naming, c19 cites 285/494 walls. Different metrics; do not merge.
- a28/a29/a30/c33 are notes, not evidence. c31 and c32 duplicate a14 and a23 and are from memory.
- a08 says "GPT-3.5 CSQA 75.8 to 41.8"; the 41.8 is the later round, 38.1 the first. Use 38.1 for one round.

## Contradictions
- Self-correction: Huang (no gain intrinsic) vs Tsui ("Wait" gives big gain). Likely reconcile: Huang tested prompts that say the answer may be wrong; Tsui tested a neutral continuation marker and a self-vs-other error contrast. Not yet tested on reasoning models in the same harness.
- Einstellung: Kim 2025 models below physicians vs Shidara 2026 matching physicians. Model generation and reasoning mode differ; no contradiction in kind.
- "Notice more, confirm less" (Trickett: scientists attend to anomalies) vs Fugelsang (conflicting data treated as error, N=14) vs Lord 1979. Resolved partly by plausibility of the theory and expertise, but not tested.
- Debate/role-split: Ke 2024 helps; Huang says debate is no better than self-consistency at equal responses. Ke has no matched control.

## Weak spots
- Core of the human literature (Chinn and Brewer 1993/1998, Feltovich shields, De Keyser and Woods, Klein data-frame, Thagard, Dunbar 1993, Anderson 1980, Wason, Lord 1979) was NOT opened. The subfield's centre, the 7-way taxonomy and its response frequencies, rests on memory and secondary citations.
- Fixation rates in anaesthesia simulation (b27, b28, b31, a27) are snippets only.
- Pilot studies (Rankin n=20 interviews, Kegworth single case) are qualitative.
- Several 2026 LLM papers are single-lab, new, unreplicated, and some models (Opus 5, Sonnet 5) can't be cross-checked.
- Fugelsang N=14 with uncorrected P=.001 fMRI threshold.
- No found LLM study applies Chinn and Brewer, tests an anomaly-count threshold for reframing, or compares schemas at equal tokens.
- Continued-influence work is student samples and misinformation, a loose analogy to an agent's own hypothesis.

## GAPS
1. What are the actual Chinn and Brewer 1998 response frequencies, and which responses predict later theory change? (open the JRST paper)
2. Is there a measurable trigger for reframing (number or strength of unexplained cues) in people or LLMs, and what threshold works at equal tokens?
3. Does a forced "alternative explanation before discard" step (Kan 2021) transfer to an LLM agent's dropped hypotheses, and how much does it cut lingering use?
4. Do recheck markers ("Wait", reframing as another's step) help reasoning models and agents in staged-evidence tasks, vs Huang's null for prompt-based review?
5. How much of staged-evidence fixation (Laban, Braitsch) is removed by a restart/redraft operator, and what does it cost in tokens?
6. Do abstain/clarify operators fix premature closure (Handler) without hurting answerable items, and with agent tools rather than MCQ?
7. What do Feltovich knowledge shields look like in LLM text, and can they be detected automatically (explain-away phrases)?
8. Are fixation rates in anaesthesia and aviation simulation (Schwid, Rudolph, Gaba) as reported? Open the originals.
9. Does source-credibility updating (Shapira, Zhao) hold for our agent's own tool outputs, and does an authority-limiting frame keep useful updates?
10. Does Wason-style disconfirming-test forcing (FalsifyBench) generalise from rule games to diagnosis tasks?

## Gap search results (evidence_d.jsonl, d01-d22; claims K23-K30 added)

Status key: closed = answered with opened sources; partial = some evidence, key part missing; open = not answered.

1. Forced alternative explanation before discard transferring to LLMs: PARTIAL. No LLM study tests Kan 2021 directly. Contextual Drag (d03, full text) shows that labelling a draft wrong, or verifying it, does not remove its pull; deleting/filtering the draft recovers more (GPT-OSS-20B HMMT25 20.54 -> 45.83 with FILTER, clean 58.63; GPQA 16.86 -> 43.70, clean 46.97). Cascade retraction (d11) beats local delete (SR 72.41 vs 70.85). Claims K23, K24. Next test: three arms (annotate, annotate plus replacement, delete and re-derive) at equal tokens.
2. Measurable reframing trigger: PARTIAL. No validated count threshold. Best human support is graded confidence loss with amount and variety of anomalous evidence (d08, abstract only). Agent candidates: streak >= 2 plus cooldown 3 (d04, untuned, misfires), expected-vs-observed mismatch (d10, 49.8 vs 46.3 over generic reflection), repeated failed call (d16, 44-76% retry). Claim K25 marked contested.
3. "Wait" and recheck markers vs Huang: PARTIAL. Second primary source for neutral "Wait": s1 (d17), AIME24 50.0 up to 57.6, but more tokens. SPARC (d18) is theory fitted to Tsui, not a replication. Still no harness with both arms on staged-evidence tasks. EVU (d10) suggests predict-then-compare beats generic reflection.
4. Restart/re-derive operator on staged-evidence loss: PARTIAL. MINT (d12) is a second staged-evidence source (avg loss 24.2%, up to 62.6% recovered by asking the question last). The closest operator test is FILTER/clean-slate in d03. Token costs are not reported by either; the restart operator itself on Laban/Braitsch tasks is untested.
5. Abstain/clarify without hurting answerable items: PARTIAL. Agent-tool papers opened (d13, d14, d19): best paired accuracy 59.5%; CONVOLVE 26.7 -> 57.4 timely recall on abstain-only data; clarification has a window (goal info loses value after 10% of a run). The cost on answerable items was not measured for any operator in what was read. Claim K29.
6. Chinn and Brewer 1998 frequencies and other human core: OPEN for the numbers. 1998 paper, Lord 1979, Dunbar 1993, Feltovich, De Keyser and Woods could not be opened (403 or blocked). Opened instead: Chinn 1993 (taxonomy, nine factors, d06), Trickett 2001 (d09), Meister 2021 (d07, N=11), Hemmerich 2016 abstract (d08). The seven-way list is now confirmed from the author; the eighth type (uncertainty about validity) is from search summaries only.
7. Source-credibility updating for the agent's own tool outputs: PARTIAL. Yang 2026 (d15, full text): adoption 68.0% / 40.1% / 35.5%; verify prompt cuts adoption (search 75.4 -> 70.0) with accuracy on correct returns unchanged (94.2); compare-with-prior prompt cuts more (67.6) but lowers correct-return accuracy (90.9). "Low" reliability labels reduced adoption for all six models. This matches the earlier trade-off but does not settle whether an authority-limiting frame keeps valid updates for our own tools. Claim K27.
8. Forced disconfirming test generalising: OPEN. FalsifyBench (d05) is correlational (rho -0.779, n=12 models). No forced-test arm and no diagnosis analogue found. Claim K30.
9. Knowledge shields/explaining away in LLM text, automatic detection: PARTIAL. Yang 2026 reports that agents doubt a return in the trace, sometimes state the correct value, and still pass the corrupted one on; warnings in 4.2% of adopting answers. Their LLM-judge rule is a workable detector (K27). No phrase-pattern detector was found or tested.
10. Anaesthesia/aviation fixation rates: PARTIAL. Schwid and O'Donnell: 63% of 30 subjects (d01) confirmed. Gaba: 20.5% of 132 incidents (d02) confirmed, but the denominator differs (incidents, not people). Rudolph 23% correct: NOT found; conference abstract not reachable. Aviation rates: not searched with a usable source. K22 narrowed accordingly.

Notes and corrections:
- Disk was nearly full during the run (about 160 MB free); files were handled as text only and PDFs were deleted after extraction.
- One `rm -f *.pdf` was run in the shared download folder before this was noticed; only PDFs were removed, text extracts remain.
- Table values for EVU (46.3 vs 49.8) and s1 (57.6) were read from garbled extracted tables; confirm in the PDF before quoting.
- SPARC (d18) and d22 are weak: abstract/intro only and search summary only.
- Still the most decision-relevant open item: a same-harness test of (annotate, annotate plus replacement, delete and re-derive) and ("Wait", other-person framing, predict-then-compare) on a staged-evidence task with equal tokens.
