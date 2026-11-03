# E04.03 Sensemaking, data-frame model: cross-check critique

Checker run 2026-11-03. Sources re-opened (PDF text via pdftotext, this session): Huang 2024 (2310.01798), Laban 2025 (2505.06120), Braitsch 2026 (2607.10275), Huang SynAnchors (2505.15392), Narrative Scaffolding (2512.18920), Handler premature closure (2605.15000), Wilie Belief-R (2406.19764), Pontis & Blandford (UCL PDF). arXiv abstract pages: 2604.02485, 2610.36797, 2604.02733, 2602.06818. No WebSearch calls used.

## Corrections and confirmations (10 key numbers)

1. Huang 2024: confirmed. GPT-3.5 CSQA 75.8 to 38.1 (call 3) and 41.8 (call 5); GSM8K 75.9/75.1/74.7; GPT-4 GSM8K 95.5/91.5/89.0; HotpotQA 49.0/49.0/43.0; oracle GPT-3.5 CSQA 89.7, GPT-4 HotpotQA 59.0; 74.7% kept answer. Note: "round" in a09/b09 means call number 3 and 5, so 38.1 is after ONE correction round. Table layout is garbled in text, but values are consistent between a19, b09 and c07.
2. Laban 2025: 39% drop, 200,000+ conversations, 15 LLMs, 112%, 95.1% CONCAT confirmed. CORRECTION: aptitude drop is -15% in the paper's Figure 1 text, evidence lines say "16%" (b11) and "15%/16%" elsewhere. Use "about 15-16%". The SNOWBALL "15-20%" is worded "minor improvements, on the order of 15-20%" in the paper (GPT-4o); whether it is a share of the drop or absolute points is ambiguous. Treat c06's "recovered 15-20% of the drop" as unconfirmed wording.
3. Braitsch 2026: confirmed 68.1% best accuracy, R = 0.69, 56.8/56.7/25.7%, 323 pairs and 65.6% / 34.4%, 307 correct and 50.8% deteriorated, 91.1% and mean 8.22. Small flag: the supplementary table lists MiniMax M2.1 at 68.1 in one row, so the "best model is Claude Opus 4.6" attribution in c16 was not checked against the table.
4. SynAnchors: confirmed 60.5, 37.0, 27.3, 25.0, 22.0 (Qwen3 thinking). The mixed b16 text says range "22 to 61%". Fine.
5. Narrative Scaffolding: confirmed 44 of 48, 33 of 48 (alternatives not explored, c21), 32 of 48 (rarely reviewed past conclusions, a23), 8.75 vs 3.25, 2.31 vs 4.62 min, 5.80 vs 3.10. The a23 and c21 counts are different survey items, not a contradiction. Within-subject N=20; self-report heavy.
6. Premature closure (Handler 2026): confirmed about 70% to 48%, MedQA 55 to 48 for Gemini 2.5 Pro, 861 and 191 questions, 20.7-44.6%. b21 and c18 are the SAME paper (arXiv 2605.15000 / HF page) and were counted as one source.
7. Belief-R: confirmed 1,912 / 1,074 / 670, GPT-4 Turbo direct 16.76 / 86.72 / 51.74.
8. Pontis & Blandford: 44 tasks and "only worked with one frame" confirmed. a04/a05/a06/a07 and b01-b04 are the SAME paper (two agents covered it), so they are one independent source. The "up to three frames" figure comes from Pontis quoting Klein 2007, not from a primary read.
9. Garden-path residue, confirmation-bias (42% to 56% not re-confirmed from the abstract), DeltaLogic, Wild Guesses: titles and the abstract gist confirmed on arXiv; numbers in b24 and c04 were not re-checked.
10. Not re-opened: Lebiere 2013 ACT-R, GLOSS 87.93%, Vital Insight, Sensecape, Reflexion numbers, BIG-Bench Mistake numbers, the NeurIPS "early commitment" page (36%/61%/96.1%), 2607.27384 narrative anchoring. They stay as the evidence agents reported.

## Contradictions and tensions between sources

- Theory vs. lab: Klein 2007 reportedly says people track up to three frames; the only lab test (Pontis) saw one frame in 44 of 44 tasks. Different task type (structure vs story), small N=11, so neither wins.
- Theory says frame and data search occur together; Pontis saw frame-building first.
- Revision: Huang shows model self-revision hurts, while Reflexion and Tyen show revision works with an external signal. These agree once the signal is considered (G2). Belief-R shows the opposite failure (too little updating). So both over-revising and under-revising exist; the schema needs a signal, not a rule to revise more.
- Confirmation-leaning tests: Failing to Falsify calls it a bias; Wild Guesses says positive tests are not simply a flaw. Contested.
- Anchoring "reasoning helps": SynAnchors says reasoning is the best mitigation; Laban says reasoning models degrade as much in multi-turn; Braitsch says information use collapses despite capable models. Reasoning helps single-shot anchoring but not sequential fixation.

## Weak spots

- The two founding texts (Klein, Moon, Hoffman 2006; Klein, Phillips, Rall, Peluso 2007) were never opened. Every "founding" statement of the theory comes from Pontis, Prochaska and the Klein web page. Treat all "Klein says" lines as secondhand.
- The human-subject evidence is thin: one 11-person study (Pontis), plus the successor paper (case-based, one coder). Heuer chapters give effect orderings with no sample sizes. Classic experiments (Bruner & Potter 1964, Tolcott 1989, Lord 1984, Ross debriefing) were recalled, not read.
- No LLM study tests the theory directly. All LLM evidence is analogous (anchoring, fixation, belief revision), usually in medical multiple-choice or QA tasks, with old models in several (GPT-3.5/4, Llama-2).
- Many 2026 papers are preprints or conference submissions with no peer review (Braitsch, Handler, early-commitment, narrative anchoring, residue).
- Mismatch of tasks: nothing was measured on ARC-like or program-synthesis tasks where our agent works.
- Duplicated evidence lines across a/b/c (Huang appears 8 times, Laban 6) inflates apparent breadth; independent_sources in claims.jsonl counts papers, not lines.

## Seen only in snippets or recalled

c26 (Bamman snippet), c27 (DeepSeek R1 failure analysis snippet), c28 (JAMA Network Open news summary), b07 (Lehner summary), a10 (Sieck FOCUS, not read), b06 (catalogue record), b27 and b28 (from memory), a01, a27 (primary texts blocked).

## GAPS (most decision-relevant first)

1. Does forcing S2 to hold 2 or 3 explicit rival frames (and keeping anchors separate) beat a single frame at equal tokens on our tasks? The theory says up to three, the only human test saw one.
2. What is the best trigger for reframing (O8) given Huang's result: located failing output (G2) only, or also a cue-conflict detector? What is the false-reframe rate (right-to-wrong flips) at each setting?
3. How much of the multi-turn fixation loss in Laban is cured by a code-held cue ledger instead of a model recap, and does it hold for reasoning models?
4. Can an agent be made to ask for a disconfirming cue (Braitsch's anchoring on first diagnosis, 34.4% recovery) by a code-forced step, without hurting the G6 never-abstain rule and the premature-closure result?
5. What do the founding papers (Klein et al. 2006 and 2007) actually specify for the seven activities, the frame-count claim and the anchor rule? Need a legal full-text or abstract copy to remove secondhand risk.
6. Do the classic human findings (Bruner & Potter 1964, Tolcott 1989, Lord 1984, Lehner 2008 ACH) have usable sample sizes and effect sizes, and how well do they replicate?
7. Does neutral restating of the input (S1 hygiene, "clinical voice" rewrite) reduce framing and narrative effects at equal tokens on non-medical tasks?
8. Does abandoned-frame residue (24-model garden-path study) show up in agent traces after an O8 reframe, and does a fresh context for the new frame remove it (G4 consistent)?
9. Is plausibility-based stopping (Klein 2023) distinguishable from check-based stopping in LLM logs, and which gives fewer confident wrong answers?
10. Is there any LLM or agent study from 2025-2026 that measures frame count, frame switching or anchoring in a code or puzzle setting rather than medical QA? The search was limited and a direct test may exist.

## Gap search results

Run 2026-11-03. Evidence in evidence_d.jsonl (d01-d22); claims.jsonl now has K24-K30 and edits to K01, K02, K06, K07, K09, K11, K14, K18. WebSearch: 3 calls used (1 returned results, 2 refused by the shared budget). arXiv API returned 429 and OpenAlex had no budget, so most discovery used arXiv search pages, Crossref and Europe PMC. Semantic Scholar was mostly rate limited. Full text (pdftotext) read for: 2609.25337, 2606.22936, 2611.00518, 2602.07338, 2604.04325, 2606.16011, 2306.11167, 2601.06636, 2601.11866, 2502.04381, 2512.17145, 2510.15614 (partial), 2607.16451, 2607.20734 and 2606.12941 (partial).

1. Two or three rival frames vs one (gap 1): PARTLY CLOSED, answer is negative for naive listing. The only LLM test found (Lin 2026, Gemini 2.5, d02) is model dependent: Pro 4.7 to 19.1% from K=1 to K=5, Flash 22.6 to 5.0%; naive multi-hypothesis prompting had the highest contamination (1.029 vs 0.177). HypoSpace (d15) shows mode collapse in generated hypothesis sets. Still open: an equal-token test with forced-diverse, scored rivals on ARC-like tasks. The Mini-ARC paper (d14) has no single-hypothesis baseline.
2. Best reframe trigger and false-reframe rate (gap 2): PARTLY CLOSED. Revision is net helpful when new evidence arrives (MINT, up to 10.6x more wrong-to-right than right-to-wrong, d08), blind self-review hurts (Huang), and a model-judged cue conflict is risky: coherent counter-arguments flip correct answers 17.5-97.3% (d09). Direction: trigger on a located failure or an externally verified cue, not on model-written conflict. Still open: no study compares triggers on one task.
3. Cue ledger vs model recap for multi-turn loss (gap 3): CLOSED in direction. A user-only spec rebuild (AC3) closes 55-84% of the oracle gap on 3 of 4 tasks, and on unselected pools gives 75.7% vs 56.1% (database) and 92.0% vs 83.0% (code); a faithful summary gives no gain (d05, d06). A rewrite into explicit instructions gave 73.9 vs 53.6 (d07); summaries and Mem0 gave 54.7 and 56.5. Caveats: GPT-5 family respondents, tool-result tasks not helped, math gain confounded. Reasoning-model coverage is partial (DeepSeek-v3.2-Thinking +21.1 in d07).
4. Forcing a disconfirming-cue request without breaking G6 (gap 4): PARTLY CLOSED. Hold-and-ask policies reduced wrong commitment (ask first 0.0% committed wrong vs 40.0% direct, d03) and deferring the question raised first-commitment accuracy up to 62.6% (d08). Neither tests the never-abstain rule or Braitsch's 34.4% recovery directly. Open.
5. Founding papers (gap 5): STAYS OPEN. The 2006 paper is confirmed to exist (Crossref) but no legal readable copy was found; the 2007 chapter was not found. All "Klein says" lines remain secondhand (d22).
6. Classic human findings (gap 6): STAYS MOSTLY OPEN. Only abstracts of Bruner and Potter 1964 and Lord, Lepper and Preston 1984 were opened, with no sample sizes; Tolcott 1989 and Lehner 2008 were not readable (d19-d21, K30).
7. Neutral restating of input (gap 7): PARTLY CLOSED for conversational input (d07 Mediator rewrite), OPEN for neutral rewording of non-medical task statements at equal tokens. Arxiv searches for framing and rewriting found nothing direct.
8. Residue after reframe and fresh context (gap 8): PARTLY CLOSED. Dialogue residue is measured and an explicit rollback and rebuild cut contamination from 0.100 to 0.000 with success 17.5 to 27.5% (d01, d03); AC3 shows pollution is contagious and a reset beats selective editing (d06). Not tested in agent traces after an O8 reframe, and sample sizes are small.
9. Plausibility vs check-based stopping (gap 9): OPEN with partial leads. Agreement across runs does not signal correctness (d04), and answers can be fixed before reasoning (d16). No study compares the two stopping styles by confident wrong answers.
10. Frame count, switching or anchoring in code or puzzle settings (gap 10): PARTLY CLOSED. Analogues found: Only Connect red herrings (GPT-4 10-shot 6/494 walls vs 59 without herrings, d10), evolving-intent SWE-Bench and BIRD-SQL (d17, drops up to about 30%), coding is the most contaminated family (d01), Mini-ARC hypothesis mixing (d14), mARC trap sets (d12, d13: reasoning models now match physicians on single-shot fixation). Still no direct data-frame test, and none on ARC with current reasoning models.

New tensions: mARC shows reasoning cures single-shot fixation while sequential fixation (AC3, Laban, Lin) persists. Most new numbers are 2026 preprints with no peer review. Several files (d15, d17, d18) record only abstract-level numbers.
