# Critique: Story model of juror decisions (cross-check)

## Re-opened this session (text read)
- Bessis et al. 2026 (PMC13024114): GPT-4o cell means 4.24/3.54/6.04/4.77, F(1,711)=424.76, GPT-5.2 F=71.24, PE2 delta -0.32 (SE .11, p=.003). All confirmed.
- Castrellon et al. 2022 (PMC9546442): BIC 40,285 (p=.014), 41,550 (p=.24), 41,947 (p=.72); r=0.904; N=29 usable after 4 of 33 excluded. All confirmed.
- Burd et al. 2025 (PMC12729272): Exp 1 66.2% for plaintiff confirmed. See correction below.
- Dalal et al. (arXiv 2402.10767): "up to 77%", "+17.5% on average", depth 6% and drift 10% confirmed.

## Corrections
1. Burd 2025 (b18): 92.6% vs 40.9% not liable are shares of mock JURIES after deliberation (92.59% special verdict with reasons), not jurors; the juror-level general-verdict figure is 43.30% pre vs 40.91% post. The text says 45.9% found not liable before any verdict form, but the sample table lists "Verdict for Plaintiff 45.9%", so the paper is internally inconsistent on direction. Do not quote 45.9% as not-liable.
2. Order-of-evidence cells (a13/b10): the 78% and 31% cells are corroborated by a second secondary source (web search, study-guide flashcards, not the paper); the both-witness cell is 62% in a13 but 63% in b10 and the flashcards. Unresolved; use "about 62-63%". The original paper (Pennington and Hastie 1988 / 1992 Exp 1) was never opened by any agent. Also the flashcard source gives N=130 students, unverified.
3. Czaban PDF (a13) now returns 403, so a13 cannot be re-opened.
4. Castrellon BICs come from models with different numbers of topic maps; only the comparison to a resampled null is meaningful, not "narrative beats utility" by BIC gap.

## Not re-verifiable this session
Willmott 2018 (403), VeriScene (arXiv PDF came back corrupt), Sun 2025 (not retried), Thagard 2003, Byrne 1995, Ersoz, MuSR, True Detective, Wu 2026, Hastie and Pennington 1993 chapter. These keep their original opened flags but their numbers are single-read.

## Contradictions and weak spots
- Founding evidence is thin: a30, a31 (1986, 1988) were never read; all founding numbers are second-hand. The 1992 paper was abstract-only.
- Thagard shows coherence maximising alone accepts guilt for O.J.; story model coverage/coherence does not decide such cases without emotion or group factors (contested).
- Recency in Bessis, Lin and Paterson (no timing effect), and Law and Order 2022 (recency not primacy) do not fit a clean story-model order account.
- Rival accounts (Bayesian causal models, constraint-satisfaction coherence shift, additive weights) fit much of the data; the story model is hard to falsify (Byrne: constructs not formally defined).
- Willmott is the only direct quantitative test of the certainty principles; it used one rape-trial video, 27 panels, mostly not-guilty verdicts (22 of 27).
- No LLM study manipulates story-model constructs (b32 is a negative search result, only snippets of DataCite/Crossref).
- Most mock-juror samples are students or online panels; boundary: violent, racially charged cases not studied (b06).

## GAPS
1. What are the exact cell sizes, N, and effect statistics for the Pennington and Hastie order-of-evidence experiment (1988 and 1992 Exp 1), and is the both-witness cell 62% or 63%?
2. Does giving an LLM evidence in story (causal-chronological) order versus source-by-source order change accuracy on a reasoning benchmark at equal tokens?
3. Does requiring an LLM to build two or more rival stories and report coverage and uniqueness improve calibration versus single-story answering?
4. Which story-quality measure (coverage count, consistency check, entailment) best separates right from wrong LLM-written stories, given consistency alone fails (IBE-Eval)?
5. Are there replications of Pennington and Hastie 1992 (story order) from 2000-2026 outside the Burd, Curley, Lin and Paterson studies, including failures?
6. Does a coverage audit step (count cited evidence items, as in VeriScene) transfer to non-forensic reasoning tasks, and what does it cost in tokens?
7. How large is the story-first versus verdict-first (judge-style, backward from elements) advantage, and does it differ by task type? Only N=4 judges exist.
8. Does an early tentative answer (coherence shift, Holyoak and Simon, Simon et al. 2001) make an LLM re-weight later evidence toward its lead answer, and by how much?
9. Does structured element-by-element checking (special verdicts) raise or lower accuracy, as opposed to merely shifting thresholds?
10. How do LLM verdict thresholds calibrate versus humans across models (Sun 2025: 21% vs 49% guilty), and does a story-based prompt change the gap?


## Gap search results (evidence_d.jsonl, d01-d20)

Closed
- Gap 1 (order experiment cells): CLOSED for cells and N. The review chapter by Pennington and Hastie (1993, d01, d02, opened) prints the table: story/story 59, pros story/def witness 78, pros witness/def story 31, witness/witness 63 (row means 69, 47; column means 45, 70). So 63 is right and 62 was wrong. N=130 students, 100-item tape, about 32 per cell (not printed). Test statistics still missing (original journal article not opened).

Partly closed
- Gap 2 (story order vs source order at equal tokens in LLMs): order of the same facts moves accuracy. Test of Time shuffled vs best order: GPT-4 60.71 vs 65.36, Gemini 63.04 vs 75.00, Claude-3-Sonnet 45.71 vs 73.57 (d06). Premise order in proof order beats other orders by 20 to over 40 points (d07). Neither is a causal-story order test, so the exact juror manipulation is still untested.
- Gap 9 (element-by-element vs global): humans only. Item-by-item ratings fit anchor-and-adjust and are about 1.5 times weaker than global story judgments (d04). No LLM test of special verdict forms found.
- Gap 3 (rival stories and calibration): nearest is distractor prompting, mean ECE down 0.26 but worse on easy items (d10); hypothesis sets lose diversity as spaces grow (d15). No test of rival stories with coverage and uniqueness scores.
- Gap 4 (best story-quality measure): LLM-judge coverage is trainable and transfers (d11); no head-to-head of coverage vs consistency vs entailment found. Otherwise only IBE-Eval (K15).
- Gap 6 (coverage audit transfer and token cost): transfer shown for RL training on 10 held-out sets (d11); token cost of a prompt-time audit not measured in anything found.
- Gap 8 (early answer, coherence shift in LLMs): open models discount their own prior (0.20-0.65) but are pulled to their own wrong candidate (d12); an overview-level source reports motivated updating in legal evidence (d13, not primary). No Holyoak-and-Simon style test.

Stayed open
- Gap 5 (post-2000 replications and failures): only the 1992 replication (N=414, d03) and a cited Smith 1988; a dissertation hint of sample-dependent reversal (d16, not opened); no dated failure found (d17).
- Gap 7 (story-first vs verdict-first): no new data. IRAC-R1 shows structured legal reasoning helps after training (47.9 to 58.1, d14) but has no story-first arm.
- Gap 10 (threshold calibration, story prompt): Sun and Zappala full text gave 403 (d18); no story-prompt arm exists.

Cautions
- d01 table was recovered from garbled text; cells reconcile with the printed means.
- d13 to d20 are abstracts, overviews or snippets; see opened flags and limits.
- New claims K20-K27 added; K02 rewritten with the fixed cells.
