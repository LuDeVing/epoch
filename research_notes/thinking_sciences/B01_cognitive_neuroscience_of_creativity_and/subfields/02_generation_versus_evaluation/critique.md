# B01.02 Generation versus evaluation: cross-check critique

Cross-checker pass over evidence_a/b/c.jsonl (83 lines). Claims are in claims.jsonl (K01 to K20).

## 1. Numbers re-opened this session (checked against the paper text or the PubMed/arXiv abstract)

| # | Number | Source | Result |
|---|---|---|---|
| 1 | Novelty 4.84 human, 5.64 AI, 5.81 AI+rerank; 49 ideas per condition; 119/109/109 reviews | Si 2024, Table 7 and Figure 1 (PDF text) | Confirmed. Per-review Bonferroni p shown as 0.00 for both AI conditions; feasibility p=1.00. Overall score AI+rerank 5.34 vs 4.68, p=0.04 confirmed. |
| 2 | LLM judges balanced accuracy 50.0 / 45.0 / 51.7 / 53.3 / 43.3; human 56.1; NeurIPS 66.0, ICLR 71.9 | Si 2024 section 7.2 (PDF text) | Confirmed. |
| 3 | 4000 seeds, 200 non-duplicates, cosine 0.8 | Si 2024 section 7.1 | Confirmed. |
| 4 | 17 of 49 reranked ideas overlap with AI-ranked set | Si 2024 | Confirmed. |
| 5 | Claude-3.5 71.4%, GPT-4o 61.1%, Claude-3-Opus 63.5% on ICLR accept/reject; 1200 submissions | Si 2024 | Confirmed. |
| 6 | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1) to 41.8 (round 2); GSM8K 75.9/75.1/74.7; GPT-4 GSM8K 95.5/91.5/89.0; oracle 75.9 to 84.3, 75.8 to 89.7, HotpotQA 26.0 to 29.0 and GPT-4 49.0 to 59.0 | Huang 2024 Tables 2 and 3 | Confirmed. Table column "# calls" 3 = round 1, 5 = round 2. |
| 7 | Game of 24: IO 7.3, CoT 4.0, SC 9.0, ToT b=1 45, b=5 74, best-of-100 CoT 49; GPT-4 gen + GPT-3.5 eval 64%, reverse 31%, GPT-3.5 ToT 19% | Yao 2023 (PDF text) | Confirmed. |
| 8 | Game of 24: standard 5%, LLM+LLM 3%, LLM+sound verifier 36 to 38%, k=25 rejection 42%; 79.1% / 81.6% labelling | Stechly 2024 table and text | Confirmed. |
| 9 | GPT-4 self-recognition 73.5%; GPT-3.5 and Llama 2 over 90% after 500-example fine-tune | Panickssery 2024 text | Confirmed. |
| 10 | SWE-bench Lite 15.9% to 56% with 250 samples vs 43% prior best | Brown 2024 abstract (arXiv API) | Confirmed. |

Also confirmed at abstract level via PubMed: Ellamil 2012 (MTL for generation; executive+default plus rostrolateral PFC, insula, temporopolar cortex for evaluation; positive default-executive connectivity throughout), Liu 2015 (MPFC both phases; DLPFC/IPS attenuated in generation, re-engaged in revision; experts stronger deactivation), Moreno-Rodriguez 2025 (DMN originality, ECN adequacy, reward system subjective value).

## 2. Corrections and flags

- c04 stated "small balanced set of 98 ideas". Not found in the Si 2024 text. Do not use the 98. The paper says only top and bottom 25% of all collected ideas.
- c05 says the top-10 vs bottom-10 ranker gap "rose with rounds (0.56 at N=1 to 0.97 at N=3)". Values are right but not monotone (N=2 0.90, N=4 0.95); the claim of a rising trend is weak.
- a02 says generation was "associated with widespread default-region activity". The Ellamil abstract says medial temporal lobe for generation and joint executive+default for evaluation. a08 says default and executive were active "not during generation". Use the abstract wording. a02 and a08 are not reliable on regions.
- a22 and c13 disagree on CLIP discrimination on the same West et al. image task (a22: about 72 to 88%; c13: 50 to 76% on hard cases). Different subsets, not reopened. Do not quote either figure.
- a17 effectiveness 6.00 to 4.13 (drop 1.87) and b19 drop 1.879 agree within rounding. The execution-study numbers (AI drops 1.049, 1.760, 1.879; human changes -0.010, +0.078, -0.052; excitement 3.90 vs 4.48; effectiveness 4.13 vs 4.78; Spearman 0.077 and -0.148) were first unreadable (arXiv PDF would not parse) and then confirmed from the text extract left in D:/research_scratch/B01.02/B01.02_2506.20803.txt. All match.
- b22/c15 self-enhancement: Zheng et al. themselves say the data cannot settle it. Treat the self-preference claim (K13) as resting on Panickssery alone.
- a19 and b27 Self-Refine "about 20%" is the authors' headline; later work (Huang) says the gain disappears without an oracle. Both stay listed; K10 records the task dependence.
- b05 participant count (about 28) was inferred from degrees of freedom. Do not quote.

## 3. Independence problem

Many lines in different files describe the same paper: Si 2024 appears as a13-a16, b16-b18, c03-c05; Si 2025 as a17, b19, c06; Huang, Panickssery, Tree of Thoughts, Brown, Lightman and NoveltyBench each appear two or three times. Agreement among a, b and c on these is replication of reading, not independent evidence. Claims were counted by independent source, so the two Si papers (one group, one pipeline, NLP prompting topics only) carry K07 to K09 as single-source even though they are the strongest LLM evidence for G8.

## 4. Contradictions between sources

- Strict split versus cooperation: Ellamil, Liu and the EEG work support distinct modes; Beaty 2015/2016, Lloyd-Cox 2022 and Dynamic switching 2025 show default and executive coupling and an inverted U. Reconciled in K01 and K02 as different configurations that stay coupled. The schema split is a design choice.
- MTL role: Ellamil places MTL in generation; the 2023 MTL lateralisation study finds MTL in evaluation too (K05, contested).
- Self-correction: Huang and Stechly (no gain or loss) against Self-Refine (about 20% gain). The difference is the presence of a checkable metric and task format.
- Judge accuracy: Zheng reports more than 80% agreement with humans; Si reports near-chance on ideas; the AI Scientist reviewer reported near-human on papers (c24) but 43.3% on ideas in Si. Judge quality depends on the object (chat answers and past papers versus unexecuted ideas).

## 5. Weak spots

- The founding human study (Ellamil) is abstract-only in all three files: no N, no thresholds. Human-side numbers with an N are Liu (27), Benedek (35), Moreno-Rodriguez (38), ERP (31), Rominger (86).
- The human evidence covers drawing, poetry, word association and alternate-uses tasks. No study tests an LLM-like generate-judge split, so the human literature only motivates, never tests, G5/G8.
- Some "evaluation" papers do not judge idea quality (b05 rated difficulty of thinking; b08 judged word pairs).
- LLM judge evidence is mostly 2023 models (GPT-4, Claude-3.5). Nothing from 2025 to 2026 frontier models was verified here, except Artificial Hivemind and the NoveltyBench 2025 results.
- The Jansson and Smith fixation and Nijstad premature-evaluation effects (K19) are second-hand through Sowden 2015.

## 6. Seen only in snippets or abstracts (opened:false or abstract only)

a01, a12, a26, a27, b01, b03, b04, b12, b14, c01, c02, c26, c27. Also unverified in full this session: C-file Li 2023, Jiang 2024, Wang 2023, McAleese, Kumar, Olausson, Lu 2024, Chain of Ideas, Cobbe, Lightman, Song 2025 numbers (read by the source agents, not re-opened by the checker).

## GAPS

1. Does separate-call generate-then-judge beat a single-call generate-and-judge on creative quality at equal tokens? No study found (b29). Run the NoveltyBench A/B before building more on G5.
2. Is there any judge for unexecuted ideas that beats the human-agreement ceiling (56%) in 2025 to 2026 models, and does it beat a random pick by outcome? Which cheap code checks (retrieval novelty, dedup, a unit test, a small run) predict execution outcome, using the Si 2025 execution data as ground truth?
3. Does the ideation-execution gap (Si 2025) replicate outside NLP prompting research and with other generators, and what share is regression to the mean from selecting top-scored ideas?
4. Does hiding authorship, using a different model, or both actually reduce self-preference in idea judging (not summaries), and by how much?
5. What is the effect size of the human findings on premature evaluation and example fixation (Jansson and Smith 1991, Nijstad 2010, Zabelina and Beeman 2013), and have they replicated? The primary papers are unopened.
6. Ellamil 2012 full text: sample size, contrast thresholds, and how pure the self-paced phases were. Has anyone replicated the generation/evaluation contrast with a cleaner design (forced phases, pre-registered)?
7. In-generation prior-output display (NoveltyBench regeneration): how much of the diversity gain survives against a human baseline larger than 8 authors, and does the gain carry over to quality, not just distinctness?
8. How many rounds of generate-judge iteration pay before diversity falls (Song 2025 says a few rounds)? Is there a code-measurable stop rule that works on open-ended ideas, not only on answers with labels?
9. Do 2025 to 2026 reasoning models with extended thinking still show no gain from intrinsic self-critique (Huang 2024 used 2023 models)? Direct re-test needed with matched tokens.
10. For multi-criterion judging (novelty, adequacy), does a two-score judge with a code-set weight agree better with held-out raters than a single blended score?

## Gap search results

Gap searcher pass. New evidence is in evidence_d.jsonl (d01 to d24; 19 opened in full text, 5 abstract-level). Claims K01, K05, K07, K08, K10, K13, K17, K19 were edited and K21 to K29 added in claims.jsonl. Web search quota ran out partway; the rest used the arXiv, Crossref and Europe PMC interfaces and arXiv search pages.

| Gap | Status | What was found |
|---|---|---|
| 1 Separate-call vs single-call generate-and-judge at equal tokens | OPEN | No study of this exact A/B. Indirect: judge selection over a diverse team beat a single model (0.810 vs 0.512) but 53 to 67 percent of the margin vanished with independent judges (d14). Rerank-only gave no outside-panel gain with a 3B model, revision did (d12). A human EEG study found evaluation inserted mid-generation raised originality (d20, abstract only). K24 sets the test. |
| 2 Judge better than the 56 percent ceiling; cheap checks vs execution | CLOSED for the judge question, OPEN for cheap checks | Prompt-only frontier judges stay near chance (GPT-4.1 51.9, GPT-5 57.65 to 61.10; d07, d08). Judges beat the human ceiling only when trained on outcomes (64.4 vs 48.9 for 25 experts; 4B model 59.2 vs expert majority 41.6; d07 to d09). For concrete ML code changes, 2026 frontier models reach R2 0.49 and 82 percent direction (d05). Which cheap code checks predict Si 2025 execution scores was not tested: that dataset's per-idea outcomes were not located. |
| 3 Replication of the ideation-execution gap; regression to the mean | OPEN | No execution-grounded replication outside NLP prompting. An economics study with model judges finds the opposite emphasis (idea gap d=2.23, execution d=0.90; d10) and is not a replication. Si 2025 does not analyse regression to the mean or selection of top-scored ideas (d11). Share due to regression is unmeasured. |
| 4 Hiding authorship or using another model for idea judging | PARTLY CLOSED | Labels alone move scores +0.43 while true source moves them +0.02 (d03). Two-word masking helps by a few points in QA; rewriting in the judge's style makes it worse (d01). Controlled for quality, self-preference in selection is near zero (d02) and absent in outcome prediction (d06). In alternate-uses scoring a large part is length: 1.43-point drop when only the core idea is scored (d04). No study of idea judging with a different-model judge vs same-model judge. K13 is now contested, not single-source. |
| 5 Effect sizes for premature evaluation and fixation | OPEN | Jansson and Smith 1991 and the Sio 2015 meta-analysis (177 citations) are paywalled and were not opened. Zabelina and Beeman 2013 is about attentional switching, not this effect, so it does not belong here. Found at abstract level: selectors favour feasibility over originality (Rietzschel 2010, d21) and evaluation mid-generation helped (Hao 2016, d20). No effect sizes obtained. |
| 6 Ellamil full text; cleaner replication | PARTLY CLOSED | Full text unreachable (paywall; the UBC thesis page blocks automated access). A review table gives N=15 (9 female), mean age 22.14, tasks, and the contrast regions (d19). Thresholds and phase purity remain unknown. The two phases differed in output (sketching vs writing), so the contrast is confounded. A 2025 ALE meta-analysis (44 generation, 10 evaluation studies) supports an insula and cingulate evaluation pattern but does not reproduce the medial temporal lobe finding (d18, abstract). No pre-registered forced-phase replication was found. |
| 7 NoveltyBench regeneration vs a larger human baseline | OPEN | Re-opened: baseline is eight authors, called a lower bound by the paper itself; GPT-4o and Gemini 2.0 Pro exceed human utility but utility mixes distinctness with a reward-model score (d22). No larger human baseline and no held-out quality rating found. |
| 8 Rounds and a stop rule | PARTLY CLOSED | Diversity of research ideas rose up to three critique-revision turns then flattened (non-duplicate ratio 0.69, 0.77, 0.80, 0.85, 0.86 for 0 to 4 turns; d13). Embedding dedup is a code-computable stop signal that needs no labels. Quality gain at round three rests on a GPT-4 tournament and is not trusted; token cost not matched. |
| 9 Reasoning models and intrinsic self-critique | PARTLY CLOSED | 2026 models do gain from self-correction on tasks with explicit constraints (SAT 34.6 to 65.0 for Mistral Large; d16). Reasoning models gain only marginally from extra correction passes (d17) and show little blind spot to their own errors (d15). No matched-token test on open-ended ideas. Huang 2024's null should be read as task-bound. |
| 10 Two-score judge with code weight | OPEN | Reviewer overall scores track novelty (r=0.725) and excitement (0.854) but not feasibility (0.097); novelty and feasibility r=-0.073 (d23). That supports separating them, but no comparison of a two-score judge with a blended judge against held-out raters was found. |

### Corrections to earlier files
- Ellamil sample size: the earlier files had no N; use N=15 from the review table (d19).
- K07 is now established (three independent sources) but narrowed to prompt-only judges.
- Do not treat the economics ideation-bottleneck paper as a replication of Si 2025.

### Still needed
Run the K24 and K26 arms (hard split vs mid-generation review; judge-picked vs random-picked vs diversity-picked) at equal tokens with an outside rater. Open Jansson and Smith 1991 and Sio 2015 through a library copy. Locate the per-idea data from Si 2025 for gap 2.
