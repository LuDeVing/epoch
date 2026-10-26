# Critique and cross-check: A11.03 Analogical access (retrieval)

## What I re-opened (full text, this session)
Checked against the arXiv PDFs (text extracted with pdftotext, PDFs deleted afterwards):

1. Yasunaga et al. 2024 (2310.01714): Table 1 confirmed (GSM8K GPT-3.5 75.0 / 75.8 / 76.7 / 77.8; text-davinci-003 14.8 / 50.3 / 54.0 / 61.0; PaLM2 60.8 / 78.2 / 80.7 / 81.7; MATH 33.0 / 33.9 / 34.9 / 37.3). K ablation (K=3 77.5 / 37.3, K=5 77.8 / 37.1) confirmed. Failure analysis confirmed: correct 6 irrelevant, 9 relevant-but-wrong, 35 good; incorrect 10 irrelevant, 12 relevant-but-wrong, 28 good-but-failed (12 gap, 8 over-reliance, 8 other).
2. Qin et al. (2404.12728): Relevant 71.5 / 33.3, none 75.5 / 36.1, random-same 75.1 / 36.3, random-diff 76.3 / 34.1, ICL-math 75.7, ICL-bio 77.9, Llama-3.1-8B 74.8 vs 81.0, Qwen2.5-14B 86.5 vs 91.1 confirmed.
3. Rashid and Kellis (2609.01556): 500 queries, 117,088 items, easy tier 12.2 / 89.8 / 97.6, hard tier Hit@1 0.0 for both embedders (Hit@10 55.4 Gemini, 21.0 Qwen) confirmed.
4. Sultan, Stern, Shahaf (2505.14479): base1,1 vs ours1,1 10/22/28/44 to 48/48/60/64; base3,5 vs ours3,5 52/72/78/88 to 80/86/86/96 confirmed. Added caveats: only 50 test problems (one problem = 2 points); baseline prompt carries an 18K-token theorem list and costs about 3x more, so token cost favours the analogy arm.
5. Graph-retrieval maths paper (2411.16454): averages confirmed, but the PDF text layer shifts row labels by one line. Reading the rows in order gives random / BGE / graph = 18.6 / 27.6 / 34.3 (0.5B), 27.6 / 40.7 / 47.1, 52.7 / 57.6 / 60.8, 59.7 / 66.2 / 68.8, 66.3 / 72.8 / 74.4. Evidence line c17 is right; note b25 labels the 1.5B Math23k row consistently with this.
6. Strategic-decisions paper (2505.00603): n=199 humans, 60 GPT-4 trials, factory 6.3 percent to 4/46, HR 20.3 to 17/46, G&H 1983 29 percent (8/28) to 50 percent (14/28) confirmed. The GPT-4 1/15 and 14/15 figures were not found by grep in the text layer (likely in a table); left as recorded.
7. Alfieri et al. 2013: a web search confirmed only the citation. d = 0.50 and 57 experiments are NOT confirmed this session.

## Corrections and inconsistencies in the evidence files
- G&H no-hint rate varies: a01 says about 30 percent, a04 says about 20 percent, the 1983 condition quoted in c12 is 29 percent (8/28), Exp 2 gives about 30 percent. Treat as "20 to 30 percent". The 75 percent total is also 80 percent (Pedone) in other places. Use ranges.
- MAC/FAC numbers disagree between a12 and c14 (surface MAC .78 vs .67; average MAC items 3.4 vs 3.3; a10 says "9 of 20 story sets (45 stories)" while b03 says "9 sets (36 stories)"; 36 is the memory with four variants per base, 45 includes the bases). Not resolved; the qualitative ordering LS > SF > AN > FOR is the same in all.
- b01 says Exp 2 had 36 undergraduates; a06 gives no N. Not rechecked.
- a28 (truncated in my view) is consistent with the paper only if the "12 r..." entry is 12 relevant-but-wrong.
- c17 reports "+1.6 to +6.7" averages; the Math23k +14.5 and +8 figures are single-dataset, not averages.
- b22 and c04/c05 are the same paper (Qin et al.) under different labels; c04 is tagged "replication" but it is a separate test of a claim, not a replication. Counted as one source.
- b24 vs c27 are the same paper (Sultan et al.); counted once.
- b20/b21/a25-a28/c01-c03 are all Yasunaga; counted once.

## Contradictions between sources
- Yasunaga: relevant self-generated exemplars give +2 on GSM8K (GPT-3.5 77.8 vs 75.8). Qin: relevant exemplars score 71.5, below no exemplars (75.5) and below random (about 75 to 76). The two use different prompts and seeds; the original shows small gains even with its own baseline at 75.8, so the difference is partly protocol. Unresolved; the "analogical prompting works via relevance" story is not safe.
- Mechanism: human work says access fails because surface cues dominate; the LLM work (Qin) says the model does not need relevant analogues at all, so the human analogy is weak for prompting-by-self-recall. It fits better for retrieval from an external store (Rashid, graph retrieval).
- Expertise: Blanchette and Dunbar style field results (far analogies) vs Trench's generation-task account (b19) vs surface effects in production (b18).
- Comparison effect: Loewenstein 2003 is only p=.06; Gentner 2009 effects are in consultants and students. The teams study barely passes.
- MAC/FAC vs LISA vs ARCS: all fit; speed comparison is by the MAC/FAC authors.

## Weak spots
- Almost all human-access evidence comes from one research tradition (Gick/Holyoak, Gentner/Forbus/Loewenstein). Independent replications are few (Keane, Trench, the 2025 business-problem study).
- Original Gick and Holyoak 1980, Catrambone and Holyoak 1989, Kurtz and Loewenstein 2007, Trench and Minervino 2015, Novick and Holyoak 1991, Holyoak and Koh 1987 numbers (b14 text) were seen only in secondary sources or snippets (opened:false).
- Alfieri meta-analysis was not read; subgroup lag numbers (b11) are from a snippet.
- BRIGHT (c26) was not opened.
- LLM retrieval studies use math and geometry; none runs a retrieval of structurally analogous problems inside an open-ended agent loop at equal tokens.
- Several 2026 papers (Rashid, SEAM, cross-domain, CHAIRO, teaching analogies) have no peer review and could not be independently checked; they should be treated as preprints.
- Equal-token accounting is mostly absent: analogical prompting and thought propagation cost extra generated tokens.

## GAPS (most decision-relevant first)
1. At equal tokens, does structure-keyed retrieval of the agent's own past solved subproblems beat embedding retrieval inside a multi-step agent loop (not single-shot maths)?
2. Does a failure-triggered cue (at an impasse) recover more than always-on retrieval, in terms of solve rate per token? Humans need a cue; is the LLM's analogue of "a hint" a retrieval trigger or a rerank step?
3. How much of the analogical-prompting gain survives when exemplars are fixed, vetted and cached (Qin) across tasks beyond GSM8K and MATH, and across newer frontier models where 0-shot CoT is already strong?
4. What representation makes cheap MAC-style prefiltering work for an LLM memory (predicate or relation tags, goal type, constraint type), and how well do model-generated tags agree across writes (consistency of abstraction at encoding)?
5. Does comparison of two stored cases (schema induction at write time) or comparison of probe plus sibling at read time give the larger gain for an LLM agent, and at what token cost? (Human data: both help; LLM data: none.)
6. What is the false-transfer rate when relational retrieval is loosened (GPT-4 precision about 0.5 with hints), and what cheap check (mapping step, verifier) keeps it low?
7. Do the human dissociations (soundness judged well, retrieval poor) hold for LLMs: is a model better at choosing between a decoy and a structural match shown side by side than at retrieving it?
8. How does retrieval quality change with memory size (117K items in Rashid vs tens of cases in the human work), and where does reranking depth (top-10 vs top-50) stop paying?
9. Is "reformulate the problem relationally before searching memory" (MetaLadder restate step, probe abstraction) the active ingredient, and does it work without training?
10. Which of the Novick and Holyoak and Gick 1980 original numbers hold up when read in the primary source (many figures here come from restatements)?


## Gap search results

Evidence file: evidence_d.jsonl (d01 to d21; d01 to d17 read in full or in the relevant sections, d18 to d21 are abstract pages or search restatements and marked opened:false). New claims K19 to K27 were added to claims.jsonl, and K01, K07, K08, K10, K15 were extended. Web search quota ran out during the run, and arXiv and Semantic Scholar rate-limited, so the search was by known and surfaced papers only; coverage of 2026 literature is incomplete.

Status by gap:

1. Structure key vs embedding key inside an agent loop at equal tokens. PARTLY CLOSED, still open on the exact test. InsightEmb (d06) and ExpeL (d13) show the key changes outcomes inside a loop by up to 13 points, and a progress-blind text key can be worse than no memory. But the better key was trained, and tokens were not equalised. No zero-training relation key was compared. (K15, K20)
2. Failure-triggered cue vs always-on. OPEN. Only indirect data: FLARE (d11) gating, RAAC (d12) stagnation control, ThinkRetrieve (d09) always-on at boundaries. Nobody compares a failure-triggered analogue cue with always-on at equal tokens. No data on whether a human-style hint maps to a trigger or a rerank step. (K22)
3. Survival of the analogical-prompting gain with fixed vetted exemplars, beyond maths, on newer models. PARTLY CLOSED. Beyond maths the gain is small and task-dependent (BBH +1.3, d16). For strong models only a one-line developer note (R1, d17) and the shrinking ThinkRetrieve gains (d09). No test on a current frontier model, and no fixed-vs-generated comparison off GSM8K. (K26, K10)
4. Representation for a cheap prefilter and tag consistency. OPEN on consistency. Practice evidence only: EconSkills retrieved by names and purposes, BoT used six coarse classes plus a threshold, AWM used placeholders (d08, d14, d15). Nobody measured agreement of model-generated tags across writes. (K27)
5. Write-time comparison vs read-time comparison. OPEN on the comparison itself. Write-time abstraction is supported (AWM +4.0 step success, EconSkills +8.3 points, ExpeL; K24), but no study has a two-case schema arm or a read-time sibling arm, and no token costs were given.
6. False-transfer rate and cheap check. CLOSED enough to act on. EconSkills (d08): forced approximate top-1 cut success 16.7 to 11.4 percent when no true match existed, even with an 'ignore if unsuitable' instruction; dumping all 50 skills gave 11.4 vs 28.1 percent. What cheap check works is not tested; the mapping step or verifier remains a design assumption. (K20)
7. Decoy vs structural match side by side. CLOSED for 2023-era models: no, models are not better when both are shown together. GPT-4 29.1 percent on far-analogy vs near-decoy (chance 50, humans 91.4) and 83.2 vs 95.5 percent once cause-effect decoys were added (humans 96). Newer models untested. (K19)
8. Memory size and rerank depth. PARTLY CLOSED. BRIGHT (d03): top-10 vs top-100 LLM rerank is about flat; ThinkRetrieve works with 309,609 items at top-1; EconSkills shows large context dumps hurt. Rashid and Kellis only reranked top-10, so top-10 vs top-50 on analogue retrieval is still unmeasured. (K25)
9. Relational reformulation before search. PARTLY CLOSED. Training-free probe rewriting works (BRIGHT up to +12.2 points; BoT distiller; ThinkRetrieve query with intermediate answer +0.8). MetaLadder's restate step is shown only after fine-tuning. Whether the relational wording specifically is the active ingredient is not isolated. (K23)
10. Primary-source check of Gick and Holyoak 1980 and Novick and Holyoak 1991. OPEN. Michigan repository and ScienceDirect returned 403 and the UCLA lab PDF host timed out. The only new material is secondary (d21) and again shows the no-hint rate ranging from 10 to 43 percent by experiment. K01 and K13 keep range wording.

Cautions on the new evidence: most new LLM sources are 2026 preprints without peer review (InsightEmb, EconSkills, ThinkRetrieve, RAAC). EconSkills' library study has one run per task, so differences of about 2 points are not significant. ThinkRetrieve's corpus keeps structural analogs at similarity 0.85 to 0.90, so it is retrieval of near-analogues, not pure structure. ARN and ParallelPARC predate current frontier models. d01 and d13 were read partly through page extraction or jumbled table text; the specific cells are flagged in their limits fields.
